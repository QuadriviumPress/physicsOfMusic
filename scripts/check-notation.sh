#!/usr/bin/env bash
#
# Re-render the VexFlow notation figures and check that nothing has drifted.
#
# The generated SVGs are committed, so a change to a definition must be
# committed together with its output. This is the figures check of
# check-figures.sh, for the other generator.
set -euo pipefail
cd "$(dirname "$0")/.."

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cp -a notation scripts node_modules package.json "$work/" 2>/dev/null
mkdir -p "$work/images/notation"
original="$PWD/images/notation"
cd "$work"

node scripts/render-notation.mjs >/dev/null
python3 scripts/notation_text_to_path.py >/dev/null

if [ ! -d "$original" ]; then
  echo "No committed notation figures yet; nothing to compare." >&2
  exit 0
fi

if ! diff -qr "$original" images/notation; then
  echo "Notation figures are stale. Run 'npm run notation:render' and commit the output." >&2
  exit 1
fi

# Each SVG must be self-contained and free of music-font text: the print and
# DOCX paths cannot fetch an external font or a linked raster, and Inkscape does
# not resolve the WOFF2 @font-face that render-notation.mjs embeds. A plain
# `grep ... && exit` would be wrong here -- under `set -e`, a grep that finds
# nothing fails, and the failing && takes the whole script down on the good path.
for file in images/notation/*.svg; do
  if grep -q 'font-family="Bravura' "$file"; then
    echo "$file still draws glyphs as Bravura text; the path conversion did not run." >&2
    exit 1
  fi
  if ! grep -q 'viewBox=' "$file"; then
    echo "$file has no viewBox." >&2
    exit 1
  fi
  if grep -qE '<image\b|(href|src)="https?://' "$file"; then
    echo "$file embeds external or raster content." >&2
    exit 1
  fi
done

echo "Notation figures match their committed outputs."
