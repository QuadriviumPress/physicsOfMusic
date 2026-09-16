# Audio generation

Every audio example is built by a script in this directory. Most are synthesized
to isolate one physical variable; a small set is derived from documented CC0
instrument recordings in `sources/`. Each generator writes a pair of files:

```
audio/<id>.mp3      the clip
images/<id>.svg     its waveform and spectrum
```

`plugins/audio.mjs` defaults to exactly that pair, so a single-clip
`` ```{audio} <id> `` directive needs no options. Both are committed, because
the Pages build runs `myst build --html` and has no Python.

## Regenerating

```bash
python3 -m pip install -r requirements-figures.txt   # once
npm run audio:render          # everything
scripts/render-audio.sh ch05  # one chapter
npm run audio:check           # verify the committed assets are in step
```

`ffmpeg` must be on the path for the MP3 encode. The matplotlib version is
pinned for the same reason the chapter figures pin it: its SVG output is not
stable across versions, and an unpinned regeneration shows up as a diff in every
line of every figure.

## Why mostly synthesized

A recording of a real clarinet and a real trumpet playing the same note differs
in a dozen ways at once — spectrum, attack, vibrato, room, player, microphone —
so it cannot settle an argument about any one of them. A synthesized pair can
hold everything fixed but the variable under discussion.

The limitation is real too. Where the sound of an actual instrument is the
point, Chapters 5 and 12 now pair the model with a VSCO Community Edition
recording. Those source WAVs are CC0, retained locally for reproducibility, and
listed with their exact upstream paths in `sources/vsco/README.md`.

## The one rule that matters

**Match level, not amplitude.** Two clips demonstrating a difference in timbre
must not also differ in loudness, or that is what the reader will hear. Peak
normalization does not do this: a square wave and a sine of equal peak differ by
about 3 dB in RMS, and a listener will report the square as louder and then
describe it as brighter.

`audiolib.match_level` scales to a fixed RMS and then guarantees headroom.
`clip_and_figure` calls it for you. Do not bypass it.

RMS is a proxy for loudness, not loudness itself — a tone rich in high harmonics
is somewhat louder than a sine of equal RMS, because the ear is more sensitive
there (Chapter 7). For the comparisons made here, all at one pitch, the residual
difference is small and is never the point of the example. Where it would be,
the caption says so.

## Layout

| File | Contents |
|---|---|
| `audiolib.py` | Synthesis helpers, the level matcher, the MP3 writer, and `clip_and_figure`, which writes the standard clip-and-figure pair |
| `ch05_audio.py` | Chapter 5: sine, sawtooth and square at one pitch; the harmonic series assembled one partial at a time; the three-waveform comparison figure |
| `ch05_recorded_audio.py` | Chapter 5: level-matched violin, flute, and trumpet recordings at the same pitch |
| `ch12_recorded_audio.py` | Chapter 12: recorded timpani and orchestral cymbals |
| `sources/vsco/` | Original CC0 WAVs plus immutable provenance |

## Conventions

- **Ids are `ch<NN>-<slug>`.** The chapter prefix keeps the directory sorted and
  is stripped when the id is turned into a display name.
- **Three seconds, mono, 128 kbps.** Long enough to hear a timbre settle, short
  enough that forty of them do not dominate the repository.
- **Fade both ends.** `write_clip` tapers 25 ms at each end; without it every
  clip starts and stops with a click, and a click is broadband noise in a book
  about spectra.
- **Measure the spectrum from the signal**, not from the amplitudes it was built
  from. `spectrum_of` does this, so the figure shows what is actually in the
  clip rather than what was intended.
- **Write a transcript in the directive.** It is the only thing a reader has who
  is holding the PDF or cannot hear the clip.
