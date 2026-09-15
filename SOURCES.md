# Sources

Overall book licence: **CC-BY-NC-SA-4.0**.

## Licence compatibility — read this before adapting anything

Not every open licence can be redistributed under this book's terms, and the
distinction matters:

| Licence | Can it be adapted into this book? | Why |
|---|---|---|
| CC-BY 4.0 / 2.0 | **Yes** | Attribution only; downstream may add restrictions, including NonCommercial. |
| CC-BY-NC-SA 4.0 | **Yes** | Identical terms. |
| Public domain | **Yes** | No conditions. |
| **CC-BY-SA 4.0** | **No** | ShareAlike requires the adaptation to be released under BY-SA 4.0 or a listed BY-SA-compatible licence. **BY-NC-SA is not one**: adding a NonCommercial restriction is exactly what ShareAlike forbids. |

This rules out adapting prose from *Open Music Theory*
(`QuadriviumPress/musicTheory`, CC-BY-SA-4.0), which this book therefore
**links to and cross-references but never copies from**. Linking is unrestricted
and nothing is lost: it is an analysis and harmony text with essentially no
acoustics content.

Note also that LibreTexts pages can carry different licences page by page within
one bookshelf. Re-check the licence notice on the specific page being adapted,
even for sources listed below.

## Primary sources

| Source | Licence | URL |
|---|---|---|
| OpenStax, *College Physics 2e*, chs. 16–17 | CC-BY 4.0 | https://openstax.org/details/books/college-physics-2e |
| OpenStax, *University Physics Volume 1*, ch. 17 | CC-BY 4.0 | https://openstax.org/details/books/university-physics-volume-1 |
| Catherine Schmidt-Jones, *Understanding Basic Music Theory* | CC-BY 2.0 | https://quadriviumpress.com/UnderstandingMusicTheory/ |
| Howard Georgi, *The Physics of Waves* | CC-BY-NC-SA 4.0 | https://quadriviumpress.com/physicsOfWaves/ |

## Supplementary sources

| Source | Licence | URL |
|---|---|---|
| PhET Interactive Simulations (University of Colorado Boulder) | CC-BY 4.0 | https://phet.colorado.edu/ |
| OpenLyceum simulations | AGPL-3.0 | https://github.com/OpenLyceum |
| VexFlow (used to engrave the staff notation) | MIT | https://www.vexflow.com/ |
| Bravura music font (SMuFL reference font, used via VexFlow) | SIL OFL 1.1 | https://github.com/steinbergmedia/bravura |

## Referenced but not adapted

The acoustics literature the book cites for data and for results it states
without deriving is listed in [`back/references.bib`](back/references.bib) and
cited in the text. Those are ordinary scholarly citations, not adapted content:
no text or figure is reproduced from any of them.

*Open Music Theory* (CC-BY-SA-4.0) is cross-referenced only, for the reason
given above.

## Per-chapter attribution

| Chapter | Primary source | Notes |
|---|---|---|
| 1. Sound, Music, and Simple Harmonic Motion | OpenStax *College Physics 2e* §16.1–16.6; Schmidt-Jones ch. 25 | |
| 2. Wave Motion and the Speed of Sound | OpenStax *College Physics 2e* §16.9, §17.1–17.2 | |
| 3. Superposition, Interference, and Standing Waves | OpenStax *College Physics 2e* §16.10, §17.5; Schmidt-Jones ch. 26 | |
| 4. Resonance and Normal Modes | OpenStax *College Physics 2e* §16.8; Georgi chs. 2–3 | |
| 5. Fourier Analysis, Harmonics, and Timbre | Georgi chs. 6, 10; Schmidt-Jones chs. 18, 27 | |
| 6. The Ear and the Physiology of Hearing | OpenStax *College Physics 2e* §17.6 | |
| 7. Loudness, Decibels, and the Equal-Loudness Contours | OpenStax *College Physics 2e* §17.3 | Contours redrawn from ISO 226:2023 values |
| 8. Pitch, Beats, Consonance, and Dissonance | OpenStax *College Physics 2e* §17.5; Schmidt-Jones ch. 38 | |
| 9. Musical Scales and Tuning Systems | Schmidt-Jones chs. 33, 44 | |
| 10. String Instruments | OpenStax *College Physics 2e* §17.5; Schmidt-Jones ch. 26 | |
| 11. Wind Instruments and Air-Column Resonance | OpenStax *College Physics 2e* §17.5; Georgi ch. 7 | |
| 12. Percussion: Membranes, Bars, and Plates | — | |
| 13. The Singing Voice | — | |
| 14. Room Acoustics and Concert-Hall Design | — | |
| 15. Electronic and Recorded Sound | — | |

Chapters with no primary source listed are written from standard textbook and
reference material rather than adapted from a specific openly licensed text;
their citations are in `back/references.bib`. **This table is filled in as each
chapter is written** — an empty Notes cell means the chapter's prose is original
to this book, not that its provenance is unrecorded.

## Figures, audio, and notation

Every figure, audio example, and staff-notation figure in this book is
**generated from source in this repository** — matplotlib for the diagrams and
plots, numpy for the audio, VexFlow for the notation — rather than copied from
any source publication. The generators are in `scripts/figures/`,
`scripts/audio/`, and `notation/definitions/`, and their outputs are committed
to `images/`, `images/notation/`, and `audio/`. All are covered by the book's
CC-BY-NC-SA-4.0 licence.

Where a generated figure plots published data — the equal-loudness contours of
Chapter 7 are the main case — the data source is named in the figure caption and
in the per-chapter table above.

Simulation screenshots in the print editions are fetched from PhET and
OpenLyceum at build time and are used under their own licences; each caption
links to the running simulation.
