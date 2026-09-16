"""Convert the Bravura glyphs in the notation SVGs into plain paths.

``scripts/render-notation.mjs`` produces SVGs in which every notehead, clef,
and accidental is a ``<text>`` element holding a SMuFL private-use codepoint,
drawn in the Bravura music font that the file embeds as a base64 WOFF2
``@font-face``. A browser renders that correctly. **Nothing else does.**

That matters here more than it would in a web-only book. The print pipeline
converts every SVG to PDF with Inkscape, which does not resolve a WOFF2
``@font-face`` from a data URI: the noteheads silently fall back to whatever
font is to hand, and a staff of music turns into a row of dingbats in the PDF
and in the Word edition. The failure is silent and it is invisible on the
website, which is the worst combination available.

So this script replaces each of those ``<text>`` elements with the ``<path>``
that the glyph actually is, and then removes the embedded font. The result has
no font dependency at all, and renders identically in a browser, in Inkscape,
in LaTeX, and in Word -- the same guarantee ``svg.fonttype: "path"`` gives the
book's matplotlib figures.

Text that carries its own ``font-family`` is left alone: that is the overlay
labelling from ``notation/figure-helpers.mjs``, which is ordinary sans-serif
and needs no special handling.

Run through ``npm run notation:render``, which does both steps in order.
"""

import base64
import io
import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
NOTATION = ROOT / "images" / "notation"

# CSS resolves `pt` against 96 dpi, not 72: 1pt is 4/3 user units. VexFlow sets
# its glyph sizes in points, so dropping this makes every notehead 25% small.
PT_TO_USER = 4.0 / 3.0

# Remove only the embedded Bravura rule.  The style element also carries the
# notation palette (including its dark-mode media query), so deleting the whole
# element makes the path-converted score black-on-dark in the website build.
FONT_FACE = re.compile(
    r"@font-face\{font-family:Bravura;src:url\(data:[^)]*\) format\('woff2'\);\}\s*",
    re.S,
)
TEXT = re.compile(r"<text\b([^>]*)>(.*?)</text>", re.S)
ATTR = re.compile(r'(\w[\w-]*)\s*=\s*"([^"]*)"')


def load_font(svg):
    """Pull the embedded WOFF2 out of the SVG and open it."""
    match = re.search(r"base64,([A-Za-z0-9+/=]+)\)", svg)
    if not match:
        return None
    return TTFont(io.BytesIO(base64.b64decode(match.group(1))))


def glyph_path(font, glyph_set, character, size, x, y):
    """The SVG path data for one character, placed at ``(x, y)`` at ``size`` units.

    Font coordinates are y-up from the baseline; SVG is y-down. The transform
    therefore flips y and translates to the text origin, which for VexFlow's
    glyphs is the baseline at the left edge -- it never sets ``text-anchor`` on
    them.
    """
    cmap = font.getBestCmap()
    name = cmap.get(ord(character))
    if name is None:
        return None, 0.0
    pen = SVGPathPen(glyph_set)
    glyph_set[name].draw(pen)
    data = pen.getCommands()
    upem = font["head"].unitsPerEm
    scale = size / upem
    advance = font["hmtx"][name][0] * scale
    if not data:
        return None, advance
    return (
        f'<path d="{data}" transform="translate({x:.3f} {y:.3f}) '
        f'scale({scale:.6f} {-scale:.6f})"',
        advance,
    )


def convert(path):
    """Rewrite one notation SVG in place. Returns the number of glyphs converted."""
    svg = path.read_text(encoding="utf-8")
    font = load_font(svg)
    if font is None:
        return 0
    glyph_set = font.getGlyphSet()
    converted = 0

    def replace(match):
        nonlocal converted
        raw_attrs, content = match.group(1), match.group(2)
        attrs = dict(ATTR.findall(raw_attrs))
        # Overlay labelling names its own font and is left as text.
        if "font-family" in attrs:
            return match.group(0)
        text = re.sub(r"<[^>]*>", "", content)
        if not text:
            return ""
        size_attr = attrs.get("font-size", "10pt").strip()
        size = float(re.sub(r"[a-z%]+$", "", size_attr))
        if size_attr.endswith("pt"):
            size *= PT_TO_USER
        x = float(attrs.get("x", "0"))
        y = float(attrs.get("y", "0"))
        fill = attrs.get("fill", "black")
        pieces = []
        for character in text:
            head, advance = glyph_path(font, glyph_set, character, size, x, y)
            if head:
                pieces.append(f'{head} fill="{fill}"/>')
                converted += 1
            x += advance
        return "".join(pieces)

    svg = TEXT.sub(replace, svg)
    # The embedded font is now dead weight -- and it is most of the file size.
    svg = FONT_FACE.sub("", svg)
    svg = re.sub(r'\s*font-family="Bravura[^"]*"', "", svg, count=1)
    path.write_text(svg, encoding="utf-8")
    return converted


def main(argv):
    targets = [Path(a) for a in argv] or sorted(NOTATION.glob("*.svg"))
    if not targets:
        print("No notation SVGs found; run scripts/render-notation.mjs first.")
        return
    for path in targets:
        before = path.stat().st_size
        count = convert(path)
        after = path.stat().st_size
        print(f"  {path.relative_to(ROOT)}: {count} glyphs to paths, "
              f"{before // 1024} KB -> {after // 1024} KB")


if __name__ == "__main__":
    main(sys.argv[1:])
