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

## Openly licensed works covering the same ground

These are listed for licence completeness and because a reader may want them.
As stated below, **no prose was adapted from any of them**; had it been, these
are the terms under which it could have been.

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

**The prose of all fifteen chapters is original to this book.** No text, figure,
or exercise has been copied or adapted from any source listed above; the
chapters were written from standard textbook and reference material on musical
acoustics. The works in the tables above are listed because they cover the same
ground and because the treatment here is consistent with them — not because
sentences were taken from them.

That distinction matters for the licence, and it is why the table below records
*specific data* rather than *adapted passages*. Where a chapter states a number
that came from somewhere, it is named here and in the figure caption.

| Chapter | Specific data, and where it comes from |
|---|---|
| 1. Sound, Music, and Simple Harmonic Motion | Threshold and pain pressures, audible range, instrument ranges: standard reference values. |
| 2. Wave Motion and the Speed of Sound | $v = 331.3 + 0.606T$ and the speeds of sound in six media: standard tabulated values. |
| 3. Superposition, Interference, and Standing Waves | End correction $\approx 0.6r$: standard result. |
| 4. Resonance and Normal Modes | — (derived throughout) |
| 5. Fourier Analysis, Harmonics, and Timbre | Piano inharmonicity coefficients: Young (1952), in `back/references.bib`. |
| 6. The Ear and the Physiology of Hearing | Eardrum and oval-window areas, ossicular lever ratio, cochlear length, Greenwood's place–frequency map, hair-cell counts, exposure limits: standard values, consistent with Moore (2012). |
| 7. Loudness, Decibels, and the Equal-Loudness Contours | **Equal-loudness contours computed from the ISO 226:2003 parameters** ($a_f$, $L_U$, $T_f$), reproduced in `scripts/figures/ch07_figures.py`. Critical-band widths after Zwicker and Fastl (1999). |
| 8. Pitch, Beats, Consonance, and Dissonance | **Dissonance curves computed from the Plomp–Levelt (1965) roughness model**; the timbre-and-scale argument follows Sethares (1993). Just-noticeable differences: standard values. |
| 9. Musical Scales and Tuning Systems | All ratios and comma values computed from first principles in `scripts/figures/ch09_figures.py`. Historical account consistent with Barbour (1951). |
| 10. String Instruments | Helmholtz motion; bow-force limits after Schelleng (1973). The Railsback curve shown is **representative of published measurements**, not computed — the caption says so. |
| 11. Wind Instruments and Air-Column Resonance | Bore acoustics and the conical-bore result: standard, consistent with Fletcher and Rossing (1998) and Benade (1990). |
| 12. Percussion: Membranes, Bars, and Plates | **Membrane mode ratios computed from Bessel function zeros**; bar mode ratios from the roots of $\cos x\cosh x = 1$. Timpani and bell partial ratios: measured values from the literature, consistent with Fletcher and Rossing (1998). |
| 13. The Singing Voice | Formant frequencies for five vowels, singer's-formant region: standard values, consistent with Sundberg (1987) and Titze (2000). |
| 14. Room Acoustics and Concert-Hall Design | Sabine equation derived in the text. Absorption coefficients and reverberation-time targets: standard tabulated values. Hall descriptions consistent with Beranek (2004) and Barron (2009). |
| 15. Electronic and Recorded Sound | Sampling theorem (Shannon 1949); $6.02b + 1.76$ derived in the text. Codec behavior consistent with Pohlmann (2011). |

## Figures, audio, and notation

Every figure, audio example, and staff-notation figure in this book is generated
from source in this repository — matplotlib for the diagrams and plots, numpy
for synthesized audio, and VexFlow for notation. Most audio is synthesized to
hold all but one variable fixed. Five real-instrument examples are derived from
the **VSCO 2 Community Edition** by Versilian Studios LLC, released under
[CC0 1.0](https://github.com/sgossner/VSCO-2-CE/blob/master/LICENSE): violin,
flute, trumpet, timpani, and orchestral cymbals. The unmodified source WAVs and
exact upstream paths are preserved in `scripts/audio/sources/vsco/`.

The generators are in `scripts/figures/`, `scripts/audio/`, and
`notation/definitions/`, and their outputs are committed to `images/`,
`images/notation/`, and `audio/`. Original project material is covered by the
book's CC-BY-NC-SA-4.0 licence; the VSCO source recordings remain CC0.

Where a generated figure plots published data — the equal-loudness contours of
Chapter 7 are the main case — the data source is named in the figure caption and
in the per-chapter table above.

Simulation screenshots in the print editions are fetched from PhET and
OpenLyceum at build time and are used under their own licences; each caption
links to the running simulation.
