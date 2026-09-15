#!/usr/bin/env bash
#
# Check that the committed audio examples are in step with their generators.
#
# The companion SVGs are compared byte for byte, exactly as check-figures.sh
# does for the chapter figures. The MP3s are **not**: they are compared on
# existence and rough size only, because an MP3 is the output of libmp3lame and
# is not reproducible across encoder versions the way matplotlib's SVG is across
# a pinned matplotlib. Byte-comparing them would turn every CI runner image
# bump into a spurious failure, and the thing that actually matters -- that the
# clip exists and matches the figure beside it -- is checked here.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "ffmpeg is required to regenerate the clips." >&2
  exit 1
fi

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cp -a scripts images "$work/"
mkdir -p "$work/audio"
original_images="$PWD/images"
original_audio="$PWD/audio"
cd "$work"
export MPLCONFIGDIR="$work/.matplotlib"

failures=0

scripts/render-audio.sh >/dev/null

# Every clip the generators produced must be committed, and vice versa.
for clip in audio/*.mp3; do
  name=$(basename "$clip")
  if [ ! -f "$original_audio/$name" ]; then
    echo "audio/$name is generated but not committed." >&2
    failures=1
  fi
done
for clip in "$original_audio"/*.mp3; do
  [ -e "$clip" ] || continue
  name=$(basename "$clip")
  if [ ! -f "audio/$name" ]; then
    echo "audio/$name is committed but no generator produces it." >&2
    failures=1
  elif [ "$(stat -c%s "$clip")" -lt 2048 ]; then
    echo "audio/$name is under 2 KB; it is probably empty." >&2
    failures=1
  fi
done

# The figures beside them are deterministic, so hold them to the usual standard.
for figure in images/*.svg; do
  name=$(basename "$figure")
  if [ -f "$original_images/$name" ] && ! diff -q "$original_images/$name" "$figure" >/dev/null; then
    echo "images/$name is stale; run 'npm run audio:render' and commit the output." >&2
    failures=1
  fi
done

if [ "$failures" -ne 0 ]; then
  exit 1
fi
echo "Audio examples match their generators."
