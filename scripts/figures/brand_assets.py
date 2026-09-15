"""Brand assets for the *Physics of Music* site: social card, favicon, and header logos.

These are not chapter figures, so they sit slightly outside the conventions in
``README.md``:

* The **social card** is PNG, not SVG. Some social platforms will not render an
  SVG ``og:image``, which is the whole reason this file exists.
* The **favicon** is a genuine multi-size ``.ico``. MyST copies whatever
  ``site.options.favicon`` points at to ``/favicon.ico`` byte-for-byte and the
  theme hardcodes ``<link rel="icon" href="/favicon.ico">``, so the file has to
  really be an ICO rather than a PNG wearing the extension.
* The **logos** are hand-written SVG rather than matplotlib output. The mark is
  pure geometry, and ``svg.fonttype: "path"`` bloat buys nothing when there is
  no text to render.

No banner is generated: ``book-theme`` validates the ``banner`` frontmatter key
but has no render path for it (only ``article-theme`` draws one), so the asset
would never appear on this site.

The mark is the **second mode of a vibrating string**: one full sine between two
fixed ends, with the node at the centre picked out. It is the book's central
picture -- an instrument sounds a pitch because only certain shapes fit -- and a
single wave between two posts stays legible down to 16 px, which a five-line
staff does not.

Regenerate with::

    python3 scripts/figures/brand_assets.py
"""

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw

from figstyle import BLUE, GRAY, RED, use_style

IMAGES = Path(__file__).resolve().parents[2] / "images"

TITLE = "Physics of Music"
# Set two lines: one line at a readable size collides with the mark.
SUBTITLE = ("Vibration, Hearing, Instruments,", "and the Sound of a Room")
FOOTER = "Martin Veillette  ·  Open textbook  ·  CC BY-NC-SA 4.0"

# The string is the accent colour; the fixed ends and the node are drawn in a
# muted tone so the eye lands on the wave rather than on its supports.
STRING = BLUE
SUPPORT = "#8dabc4"
NODE = RED
# Dark-theme variants: #1769aa disappears against a dark header.
STRING_DARK = "#5aa9e6"
SUPPORT_DARK = "#5b7185"
NODE_DARK = "#e8706b"

CARD_W, CARD_H = 1200, 630
DPI = 100


def _mode_points(cx, cy, half_w, amplitude, samples=180):
    """The n=2 mode between two fixed ends, centred on ``(cx, cy)``."""
    x = np.linspace(-1.0, 1.0, samples)
    return cx + x * half_w, cy + amplitude * np.sin(2.0 * math.pi * (x + 1.0) / 2.0)


def draw_mark(ax, cx, cy, half_w, amplitude, string, support, node, lw=3.0):
    """Draw the standing-wave mark, plus its mirror image as the opposite phase."""
    x, y = _mode_points(cx, cy, half_w, amplitude)
    # Both phases, because a standing wave is the envelope, not one snapshot.
    ax.plot(x, y, color=string, lw=lw, solid_capstyle="round", zorder=3)
    ax.plot(x, 2 * cy - y, color=string, lw=lw, alpha=0.45, solid_capstyle="round", zorder=2)
    # The fixed ends.
    for end in (cx - half_w, cx + half_w):
        ax.plot([end, end], [cy - amplitude * 1.35, cy + amplitude * 1.35],
                color=support, lw=lw * 1.1, solid_capstyle="round", zorder=1)
    # The node at the centre: the one point that never moves.
    ax.plot([cx], [cy], "o", color=node, ms=lw * 2.6, zorder=4)


def social_card():
    """The 1200x630 og:image."""
    use_style()
    fig = plt.figure(figsize=(CARD_W / DPI, CARD_H / DPI), dpi=DPI)
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, CARD_W)
    ax.set_ylim(0, CARD_H)
    ax.axis("off")
    ax.set_facecolor("white")

    draw_mark(ax, cx=250, cy=CARD_H / 2, half_w=150, amplitude=78,
              string=STRING, support=SUPPORT, node=NODE, lw=7.0)

    ax.text(470, CARD_H / 2 + 88, TITLE, fontsize=52, fontweight="bold",
            color="#1a1a1a", va="center")
    for index, line in enumerate(SUBTITLE):
        ax.text(470, CARD_H / 2 + 16 - index * 42, line, fontsize=25, color="#41505c", va="center")
    ax.text(470, CARD_H / 2 - 110, FOOTER, fontsize=18, color=GRAY, va="center")

    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / "social-card.png"
    fig.savefig(path, format="png", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")


def _favicon_layer(size, scale=8):
    """One square favicon layer, drawn large and downsampled for clean edges."""
    big = size * scale
    image = Image.new("RGBA", (big, big), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    half_w = big * 0.36
    amplitude = big * 0.20
    cx = cy = big / 2
    width = max(2, int(big * 0.055))

    x, y = _mode_points(cx, cy, half_w, amplitude, samples=120)
    draw.line(list(zip(x, y)), fill=STRING, width=width, joint="curve")
    for end in (cx - half_w, cx + half_w):
        draw.line([(end, cy - amplitude * 1.4), (end, cy + amplitude * 1.4)],
                  fill=SUPPORT, width=width)
    r = big * 0.055
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=NODE)
    return image.resize((size, size), Image.LANCZOS)


def favicon():
    """A real multi-size ICO, because MyST copies this file byte-for-byte."""
    sizes = [16, 32, 48, 64, 128, 256]
    layers = [_favicon_layer(n) for n in sizes]
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / "favicon.ico"
    layers[-1].save(path, format="ICO", sizes=[(n, n) for n in sizes])
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")


def _logo_svg(string, support, node):
    """The header mark as hand-written SVG: pure geometry, no text, no font embedding."""
    x, y = _mode_points(cx=32.0, cy=20.0, half_w=22.0, amplitude=11.0, samples=64)
    points = " ".join(f"{px:.2f},{py:.2f}" for px, py in zip(x, y))
    mirror = " ".join(f"{px:.2f},{40.0 - py:.2f}" for px, py in zip(x, y))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 40" role="img"
     aria-label="A string vibrating in its second mode between two fixed ends">
  <g fill="none" stroke-linecap="round">
    <polyline points="{mirror}" stroke="{string}" stroke-width="2.4" opacity="0.45"/>
    <polyline points="{points}" stroke="{string}" stroke-width="2.4"/>
    <line x1="10" y1="5.5" x2="10" y2="34.5" stroke="{support}" stroke-width="2.8"/>
    <line x1="54" y1="5.5" x2="54" y2="34.5" stroke="{support}" stroke-width="2.8"/>
  </g>
  <circle cx="32" cy="20" r="3" fill="{node}"/>
</svg>
"""


def logos():
    """Light and dark header marks."""
    IMAGES.mkdir(exist_ok=True)
    for name, colors in (
        ("logo.svg", (STRING, SUPPORT, NODE)),
        ("logo-dark.svg", (STRING_DARK, SUPPORT_DARK, NODE_DARK)),
    ):
        path = IMAGES / name
        path.write_text(_logo_svg(*colors), encoding="utf-8")
        print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size} B)")


def main():
    print("Brand assets:")
    social_card()
    favicon()
    logos()


if __name__ == "__main__":
    main()
