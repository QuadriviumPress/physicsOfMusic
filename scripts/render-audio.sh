#!/usr/bin/env bash
#
# Regenerate every audio example and its companion figure.
#
#   scripts/render-audio.sh            all chapters
#   scripts/render-audio.sh ch05       one chapter
#
# Writes audio/<id>.mp3 and images/<id>.svg for each clip. Both are committed,
# because the Pages build runs `myst build --html` and has no Python.
#
# Requires ffmpeg on the path, and the pinned versions in
# requirements-figures.txt -- matplotlib's SVG output is not stable across
# versions, and a figure regenerated with a different one shows up as a diff in
# every line.
set -euo pipefail
cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-python3}"

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg is required to encode the clips; install it and try again." >&2
  exit 1
fi

"$PYTHON" - <<'PY'
import matplotlib
if matplotlib.__version__ != "3.11.1":
    raise SystemExit(
        f"Matplotlib 3.11.1 is required for deterministic SVGs; found {matplotlib.__version__}. "
        "Install requirements-figures.txt first."
    )
PY

pattern="${1:-ch}"
found=0
for script in scripts/audio/"$pattern"*_audio.py; do
  [ -e "$script" ] || continue
  found=1
  echo "==> $(basename "$script")"
  "$PYTHON" "$script"
done

if [ "$found" = 0 ]; then
  echo "No generators matched scripts/audio/${pattern}*_audio.py" >&2
  exit 1
fi

echo
echo "Audio examples and figures are up to date."
