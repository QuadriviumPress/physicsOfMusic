---
title: "Fourier Analysis, Harmonics, and Timbre"
short_title: "Chapter 5. Fourier Analysis, Harmonics, and Timbre"
label: ch-fourier-and-timbre
numbering:
  enumerator: "5.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 5.1, 5.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-05-fourier-analysis-harmonics-and-timbre.pdf
    chapter: 5
---

### Learning Objectives

By the end of this chapter, you should be able to:

- State Fourier's theorem for a periodic signal, and explain what it guarantees about any sustained musical tone.
- Build a sawtooth, square, and triangle wave by adding harmonics, and predict the effect on the waveform of adding or removing a given partial.
- Read a line spectrum: identify the fundamental, name the partials by harmonic number, and relate the spectrum to the waveform beside it.
- Distinguish harmonic from partial from overtone, and use each term correctly.
- Explain why two tones of the same pitch and loudness can sound entirely different, and identify the spectral features responsible.
- Explain why the phase relationships among harmonics change the waveform dramatically but the timbre hardly at all, and state the limits of that rule.
- Describe the attack, decay, sustain, and release of a note, and give evidence that transients matter at least as much as the steady-state spectrum for recognizing an instrument.
- Read a spectrogram, and use it to describe how the spectrum of a real note changes over its duration.
- Distinguish harmonic spectra from inharmonic ones and from noise, and identify which instruments produce each.

### Introduction

A clarinet and a violin play the same note, at the same loudness, for the same length of time. Nobody has any difficulty telling them apart.

That is a problem for everything the book has said so far. [Chapter 1](#ch-sound-and-shm) established that what reaches your ear is a single wiggling number, pressure at a point, as a function of time. If the pitch is the same and the loudness is the same, what is left for the difference to live in?

The answer is the **shape** of the wiggle, and the tool that makes shape analyzable is the subject of this chapter.

Jean-Baptiste Joseph Fourier, working on heat conduction in the 1800s, proved something that at first seems too strong to be true: **any periodic waveform, however jagged, is a sum of sine waves at whole-number multiples of one frequency.** Not approximately, exactly, and in only one way.

Applied to music, this says that a sustained note is completely specified by a list: how much of each harmonic it contains. That list is the **spectrum**, and it is the single most useful object in the rest of this book. Chapters [10](#ch-string-instruments) through [13](#ch-the-singing-voice) are, in the end, four long answers to the question "what spectrum does this instrument produce, and why?"

This chapter also delivers the first serious complication. The spectrum is not the whole story, and the part it leaves out, how the sound *starts*, turns out to matter at least as much.

## Fourier's Theorem

### Any Periodic Wave Is a Sum of Sinusoids

The statement, precisely: if a function repeats with period $T$, it can be written as

$$
y(t) = A_1\sin(2\pi f_1 t + \phi_1) + A_2\sin(2\pi\cdot 2f_1 t + \phi_2) + A_3\sin(2\pi\cdot 3f_1 t + \phi_3) + \cdots
$$

where $f_1 = 1/T$. Every component is a **harmonic** of $f_1$: its frequency is an exact whole-number multiple.

Two features of this deserve emphasis.

**Only harmonics appear.** Not arbitrary frequencies, multiples of one fundamental. This is forced by the repetition: any component at a non-multiple frequency would not come back to where it started after time $T$, and so the whole would not repeat.

**The decomposition is unique.** One waveform, one list of amplitudes and phases. There is no ambiguity about what a sound "is made of".

### Building a Sawtooth by Hand

The theorem is easier to believe once you have watched it happen.

```{animation} ch05-building-a-sawtooth
:label: fig:ch05-building-a-sawtooth
:alt: Six panels showing a dashed sawtooth target with a solid approximation built from 1, 2, 3, 5, 10 and 40 sine waves, converging closely by 40 but with a persistent overshoot at each jump.

A sawtooth wave, assembled from sine waves whose amplitudes fall as $1/n$. One harmonic is a sine; by ten it is recognizably a sawtooth; by forty the approximation is very close. The overshoot at each vertical jump, however, never disappears, it only gets narrower. That is the **Gibbs phenomenon**, and it is a genuine property of the sum rather than an error in the drawing.
```

That figure should be uncomfortable the first time. The building blocks are smooth, endless, curvy sinusoids; the target has sharp corners and instantaneous jumps. Adding smooth things and getting a corner seems like cheating. It is not: the corner is what infinitely many harmonics, in exactly the right proportions, add up to.

:::{dropdown} The Fourier coefficients, as integrals
Finding the amplitudes is the same trick as §4.4 used for a plucked string, and for the same reason: sinusoids of different harmonic numbers are **orthogonal** over one period.

Write the series in the equivalent form

$$
y(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\Bigl[a_n\cos(2\pi n f_1 t) + b_n\sin(2\pi n f_1 t)\Bigr].
$$

The orthogonality relations are that, over one period $T$,

$$
\int_0^T \cos(2\pi n f_1 t)\cos(2\pi m f_1 t)\,\mathrm{d}t =
\begin{cases} T/2 & n = m \ne 0\\ 0 & n \ne m,\end{cases}
$$

with the same for sines, and $\int_0^T \cos(2\pi n f_1t)\sin(2\pi m f_1 t)\,\mathrm{d}t = 0$ for all $n$ and $m$.

So multiply the series by $\cos(2\pi m f_1 t)$ and integrate. Every term dies except one, leaving

$$
a_m = \frac{2}{T}\int_0^T y(t)\cos(2\pi m f_1 t)\,\mathrm{d}t,
\qquad
b_m = \frac{2}{T}\int_0^T y(t)\sin(2\pi m f_1 t)\,\mathrm{d}t .
$$

The amplitude and phase of the $m$th harmonic are then $A_m = \sqrt{a_m^2 + b_m^2}$ and $\phi_m = \arctan(a_m/b_m)$.

For the sawtooth $y(t) = 2(t/T) - 1$ on $0 \le t < T$, the integrals give $a_m = 0$ and $b_m = -2/(\pi m)$: every harmonic present, falling as $1/n$, which is what the figure above plots.

The general rule worth carrying away is that **the sharper the waveform, the more slowly its harmonics die off**. A discontinuity gives $1/n$; a kink in the slope gives $1/n^2$; a perfectly smooth wave has harmonics that vanish faster than any power. This is why sharp-cornered waveforms sound bright.
:::

### Analysis and Synthesis

The theorem runs in both directions, and both are used constantly.

**Analysis** takes a sound and finds its spectrum. This is what a spectrum analyzer does, what the fast Fourier transform computes, and what the laboratory exercises in [](#appendix-laboratory) ask you to do to real instruments.

**Synthesis** takes a spectrum and builds the sound. This is additive synthesis ([Chapter 15](#ch-electronic-and-recorded-sound)), and it is how every audio example in this book was made.

The two are exact inverses, which is a stronger claim than it may look. It means the spectrum contains *everything* about a periodic sound: no information is lost in going from the waveform to the list of harmonics and back again.

```{audio} ch05-harmonic-build-up
:label: fig:ch05-harmonic-build-up
:transcript: A tone that brightens in eight steps, growing from a plain hollow sound to a buzzy one. The pitch does not change at any point.

Synthesis, one harmonic at a time. Each step adds the next harmonic of $220$ Hz at the amplitude a sawtooth calls for. Listen for what *does not* happen: the pitch never moves. Adding higher frequencies to a tone makes it brighter, not higher, which is the first and most important thing the ear does with a harmonic series.
```

```{openlyceum} WaveComposer
:label: fig:ch05-wave-decomposer-sim
:screen: 2

The decomposer screen: hand it an arbitrary periodic wave and watch it resolve into a stack of harmonic amplitudes in real time. This is analysis running the other direction from the sawtooth built by hand above, spectrum from waveform rather than waveform from spectrum, and the two screens of this simulation are the theorem's two directions made concrete.
```

## The Harmonic Series and the Spectrum

### Harmonics, Partials, and Overtones

Three words, frequently confused, and worth fixing now.

- A **partial** is any frequency component of a complex tone. It is the general word and it carries no assumption.
- A **harmonic** is a partial whose frequency is an exact whole-number multiple of the fundamental. The $n$th harmonic has frequency $nf_1$. The fundamental is the 1st harmonic.
- An **overtone** is any partial above the fundamental. The 1st overtone is the 2nd harmonic.

That last off-by-one is a standing trap, and the reason this book avoids the word "overtone" except when quoting someone who used it.

The distinction between *partial* and *harmonic* is not pedantry, because plenty of musical sounds have partials that are not harmonics. A bell, a drum, a cymbal, and, by a small but audible amount, a piano string all produce partials at frequencies that are not whole-number multiples of anything. Section 5.5 and [Chapter 12](#ch-percussion) take those up.

### Reading a Line Spectrum

A spectrum is conventionally drawn as a **line spectrum**: a vertical stem at each harmonic, whose height is that harmonic's amplitude. Stems, not a filled curve, because in a periodic sound there is genuinely *nothing* between the harmonics, and a filled curve would suggest otherwise.

```{figure} ../images/ch05-waveform-spectrum-grid.svg
:label: fig:ch05-waveform-spectrum-grid
:alt: A four-column grid. Top row shows sine, sawtooth, square and triangle waveforms; bottom row shows their line spectra, with one partial for the sine, all harmonics falling as one over n for the sawtooth, odd harmonics as one over n for the square, and odd harmonics as one over n squared for the triangle.

Four waveforms and their spectra. The **sawtooth** contains every harmonic, falling as $1/n$. The **square** contains only odd harmonics, also falling as $1/n$, and sounds hollow, exactly like the stopped pipe of [Chapter 3](#ch-superposition), for exactly the same reason. The **triangle** contains only odd harmonics but they fall as $1/n^2$, which makes it much closer to a sine in character.
```

The vertical axis is often drawn in **decibels** rather than linear amplitude, for the reason [Chapter 7](#ch-loudness) will give: the ear's response is logarithmic, and a partial $40$ dB below the fundamental, a hundredth of its amplitude, is still perfectly audible and can matter a great deal to the timbre. On a linear plot it would be invisible.

### Why Periodic Means Harmonic

Why do the partials of a sustained musical tone come out as exact multiples?

A vibrating string has modes at $nf_1$ because of its boundary conditions ([Chapter 3](#ch-superposition)). But the deeper reason applies to any sustained tone, whatever produces it: **if the waveform repeats exactly, its partials must be exact harmonics**, because anything else would prevent the repetition.

This works in reverse too, and it is the key to [Chapter 8](#ch-pitch-and-consonance). When the ear encounters a set of partials at $200$, $300$, $400$, $500$ Hz, it can infer that the waveform repeats $100$ times a second, and it reports a pitch of $100$ Hz, whether or not any energy is present at $100$ Hz at all.

## Spectrum and Timbre

### The Same Pitch, Different Sounds

Now the chapter's opening question can be answered. A clarinet and a violin playing the same note differ in their spectra, and that is what you hear.

```{audio} ch05-sine, ch05-sawtooth, ch05-square
:names: Sine, Sawtooth, Square
:figure: ../images/ch05-three-waveforms.svg
:label: fig:ch05-three-waveforms
:transcript: Three tones of the same pitch and the same level. The sine is hollow and plain, the sawtooth buzzy and bright, the square hollow but reedy.

The same fundamental, the same loudness, three different sounds. Nothing separates them but which harmonics are present and how strong each one is. This is the whole of the chapter in twelve seconds.
```

Ideal waveforms make the rule clean, but instruments make it musical. The next
example holds the performed pitch fixed while changing the entire mechanism
that produces and filters it.

```{audio} ch05-real-violin, ch05-real-flute, ch05-real-trumpet
:names: Violin, Flute, Trumpet
:figure: ../images/ch05-real-instruments.svg
:label: fig:ch05-real-instruments
:transcript: Three musicians sustain the same high note. The violin is textured and continuously wavering, the flute is breathy and comparatively pure, and the trumpet is bright and brassy with strong upper harmonics.

Three real instruments, one nominal fundamental near 880 Hz. Their spectral lines share the
same spacing, but their envelopes, noise, attacks, and small performance
fluctuations differ. These CC0 recordings are from the VSCO Community Edition;
the exact source files are recorded in `SOURCES.md`.
```

Some rough rules connect a spectrum to what it sounds like:

| Spectral feature | Perceived as |
|---|---|
| Strong high harmonics | Bright, brilliant, harsh |
| Harmonics dying quickly | Dark, mellow, round |
| Odd harmonics only | Hollow, woody, reedy |
| Very few harmonics | Pure, thin, flute-like |
| Many closely spaced inharmonic partials | Clangorous, metallic |

The **spectral centroid**, the amplitude-weighted average frequency of the partials, correlates well with judgments of brightness, and is the single number most often used when a machine has to guess what a sound is like.

### Spectral Centroid, Brightness, and Roll-off

Two cautions about that correlation, because it is easy to lean on it too hard.

First, the centroid is a *summary*. Two spectra with the same centroid can sound quite different if one has its energy concentrated in a narrow band and the other spreads it widely.

Second, and more interesting: **the ear is much more sensitive to the presence or absence of a harmonic than to its exact level.** Removing every even harmonic from a tone, turning a sawtooth into a square, is instantly audible and transforms the character of the sound. Halving the amplitude of the seventh harmonic alone is barely audible at all. The pattern matters more than the precise numbers.

### The Phase Question

Fourier's theorem gives each harmonic an amplitude *and* a phase. What does the phase do?

To the *waveform*, a great deal. Change the phases and the shape of the wave changes completely.

To the *ear*, remarkably little.

```{figure} ../images/ch05-phase-does-not-matter.svg
:label: fig:ch05-phase-does-not-matter
:alt: Three panels. Two show very different-looking waveforms, one with aligned phases and one with scrambled phases. The third shows the single line spectrum that both of them share.

Two signals with identical spectra and randomized relative phases. The waveforms look nothing like each other. They sound almost exactly the same.
```

```{audio} ch05-phase-aligned, ch05-phase-scrambled
:names: Phases aligned, Phases scrambled
:figure: ../images/ch05-phase-does-not-matter.svg
:label: fig:ch05-phase-audio
:transcript: Two buzzy tones. They are very hard to tell apart, at most there is a slight difference in the quality of the buzz, and many listeners hear none at all.

The two signals of the figure above. Try to hear a difference before reading on. This is **Ohm's acoustic law**: the ear analyzes a steady sound into its component frequencies and is largely deaf to the phase relationships between them.
```

This is a genuinely strange fact, and it has two important consequences.

It means the ear is doing something like a Fourier analysis and then discarding half of the result. [Chapter 6](#ch-the-ear) shows the mechanism: the cochlea sorts frequencies by *place*, and place is preserved while relative timing between widely separated frequencies is not.

It also means audio engineers can be relaxed about phase in ways they cannot be about amplitude. A loudspeaker that shifts the phases of different frequencies by different amounts, and all of them do, is not thereby ruining the sound.

:::{warning}
The rule has limits, and they are worth knowing. Phase matters when it changes the *envelope*: two partials very close in frequency beat against each other, and their relative phase determines when. Phase matters between the two ears, where it is a primary cue for direction ([Chapter 15](#ch-electronic-and-recorded-sound)). And extreme phase manipulation is audible on transient-rich material. What Ohm's law says is that for a **steady** tone, phase is nearly inaudible, not that phase never matters.
:::

## Beyond the Steady State

### Attack, Decay, Sustain, Release

Everything so far has assumed a sound that goes on forever. Real notes start and stop, and the way they do it is described by the **envelope**, conventionally divided into four stages.

```{animation} ch05-adsr
:label: fig:ch05-adsr
:alt: Left, an idealized envelope with attack, decay, sustain and release segments labeled A, D, S, R. Right, three real instrument envelope shapes: a plucked string decaying from the start, a bowed string rising and holding, and a struck bell decaying slowly.

Left: the idealized four-stage envelope, borrowed from synthesizer design. Right: three real shapes. A plucked string has essentially no sustain, it starts decaying immediately. A bowed string has no decay at all while the bow keeps moving. A struck bell is a plucked string with a much longer decay.
```

The envelope alone distinguishes whole families of instrument. Anything struck or plucked must decay, because no energy is being added after the initial event. Anything bowed, blown, or sung can sustain indefinitely, because the player keeps supplying energy. That division, **impulsive** against **sustained** excitation, organizes [Part V](#ch-string-instruments) as much as the choice of vibrator does.

### Transients Carry the Identity

Here is the result that unsettles the neat picture of §5.3.

Record a note on a real instrument. Cut off the first tenth of a second. Play the remainder to a listener and ask them to name the instrument.

They will struggle. Piano, guitar, and bowed notes with their attacks removed are surprisingly easy to confuse, and a piano with its attack removed does not sound much like a piano at all. The steady-state spectrum, the thing this chapter has spent five sections on, turns out to be a weaker cue than the first fraction of a second.

```{audio} ch05-with-attack, ch05-without-attack
:names: With its attack, Faded in instead
:figure: ../images/ch05-attack-compare.svg
:label: fig:ch05-attack-compare
:transcript: Two notes with the same pitch and the same harmonics. The first begins with a sharp, percussive onset and sounds struck; the second fades in smoothly and sounds like an organ or a synthesizer, despite being made of exactly the same partials.

The same steady-state spectrum, with and without a struck attack. Nothing about the harmonic content differs. What differs is the first tenth of a second, and it is enough to move the sound into a different instrumental family.
```

What is happening in that first tenth of a second? Several things at once: the partials do not all arrive together, they do not all arrive at their final amplitudes, and there is usually a burst of **noise**: the scrape of a bow catching, the breath of a flute, the thump of a hammer, the click of a key. None of it is periodic, so none of it is in the spectrum, and all of it is informative.

### The Spectrogram

A single spectrum describes a sound that is not changing. Real sounds change constantly, and the tool for those is the **spectrogram**: a picture with time across the bottom, frequency up the side, and intensity shown as brightness.

```{figure} ../images/ch05-spectrogram.svg
:label: fig:ch05-spectrogram
:alt: Left, the decaying envelope of a plucked note. Right, a spectrogram of the same note showing horizontal bands at harmonic frequencies, with the higher bands fading out sooner than the lower ones.

A plucked note, twice. The waveform on the left shows *when* things happen. The spectrogram on the right shows when **and what**: each horizontal band is a harmonic, and the higher bands fade first. This is the general behavior of struck and plucked instruments, and it is why a note gets darker as it dies away.
```

The spectrogram is made by chopping the signal into short overlapping windows and taking the spectrum of each. That construction contains an unavoidable trade-off, which [Chapter 15](#ch-electronic-and-recorded-sound) meets again in a different guise: a **short** window locates events precisely in time but cannot resolve closely spaced frequencies, and a **long** window does the opposite. You cannot have both, and the choice of window length is the first thing to check when reading someone else's spectrogram.

```{phet} fourier-making-waves
:label: fig:ch05-fourier-sim
:placeholder: /images/phet/fourier-making-waves-600.png

Build a waveform by dragging the amplitude of each harmonic and watch the shape respond. Two experiments repay the effort: reproduce the square wave by setting the even harmonics to zero, and then change the *phase* of a single harmonic and watch the waveform transform while the spectrum does not move at all.
```

## When the Spectrum Is Not Harmonic

### Inharmonicity

A real piano string is not an ideal string. It has **stiffness**, it resists being bent, not merely being stretched, and stiffness adds a restoring force that grows with curvature. High modes are more curved than low ones, so they are stiffened more, and their frequencies are pushed up:

$$
f_n = n f_1\sqrt{1 + Bn^2},
$$

where $B$ is a small **inharmonicity coefficient**, typically around $10^{-4}$ for a piano's middle register.

```{figure} ../images/ch05-formants-and-inharmonicity.svg
:label: fig:ch05-formants-and-inharmonicity
:alt: Left, a fixed dashed filter curve with three peaks, over which two sets of harmonic stems at different fundamentals are drawn, showing that the envelope stays put as the pitch changes. Right, a rising curve showing how far each partial of a piano string is sharp of a true harmonic, reaching about 85 cents by the sixteenth partial.

Left: **formants**, resonances fixed by the instrument's body, which shape whichever harmonics happen to fall near them. Right: **inharmonicity**, the partials of a real piano string, stretched progressively sharp of exact multiples. By the sixteenth partial the departure is most of a semitone.
```

The consequence is audible and important: **a piano's octaves must be stretched.** If the upper octave were tuned to exactly twice the lower fundamental, it would beat against the lower note's stretched second partial. Tuners tune the octave to the partial instead, which makes the top of a piano sharp and the bottom flat relative to equal temperament, by as much as $30$ cents at the extremes. [Chapter 10](#ch-string-instruments) works this through.

### Formants: Fixed Resonances, Moving Fundamental

The left panel of that figure shows the other way a spectrum acquires structure.

So far the spectrum has been described as a property of the *source*. But every instrument has a resonator ([Chapter 4](#ch-resonance)), and the resonator is a filter with its own fixed peaks. Those peaks are **formants**, and they emphasize whichever harmonics fall near them.

The crucial point is that **formants do not move when the pitch does**. Sing "ah" on a low note and then a high one: the fundamental changes, the harmonics change, but the resonances of your vocal tract stay where they are, because your throat has not changed shape. That is why the vowel remains recognizable, and it is the entire basis of [Chapter 13](#ch-the-singing-voice).

This is the **source–filter model** of §4.5, now stated spectrally: the source supplies a harmonic series, the filter shapes it, and what you hear is the product. It applies to the voice, to every wind instrument, to a violin body, and to a subtractive synthesizer.

### Noise and Its Musical Uses

Finally, the sounds Fourier's theorem does not cover.

A periodic sound has a line spectrum. A sound that never repeats has a **continuous** spectrum, energy at all frequencies rather than at a discrete set. That is **noise**, and music is full of it: the breath in a flute tone, the scrape of rosin, the consonants in sung text, the wash of a cymbal, the snares on a snare drum.

Noise is not a defect. Synthesized instruments that get the harmonic spectrum exactly right and leave the noise out sound sterile, and the single most effective improvement to an early digital instrument is usually to put the breath back. What a listener recognizes as "a real flute" is partly the harmonic series and partly the hiss that accompanies it.

There is a continuum here rather than a boundary. A cymbal's partials are so numerous and so closely spaced that the ear cannot separate them, and hears noise. A slightly unsteady sung note has partials that wander, smearing each line into a band. [Chapter 12](#ch-percussion) works along this continuum from the nearly harmonic to the frankly noisy.

## Summary

- **Fourier's theorem**: any periodic waveform is a sum of sinusoids at whole-number multiples of one fundamental frequency, uniquely. Periodicity forces the partials to be exact harmonics.
- **The spectrum**, the list of harmonic amplitudes, is drawn as a line spectrum, because a periodic sound genuinely has nothing between its harmonics. A decibel axis is usually more informative than a linear one.
- **Sharper waveforms have slower-decaying harmonics.** A discontinuity gives $1/n$, a kink gives $1/n^2$. This is why sharp-cornered waveforms sound bright.
- **Timbre lives in the spectrum**: same pitch, same loudness, different harmonic content, different sound. Odd harmonics alone sound hollow; strong high harmonics sound bright; few harmonics sound pure.
- **Phase changes the waveform but barely changes the sound** (Ohm's acoustic law), for a steady tone. The exceptions are beating partials, binaural cues, and transient-rich material.
- **The envelope**, attack, decay, sustain, release, divides instruments into impulsive and sustained families, and **transients carry an instrument's identity** at least as strongly as its steady-state spectrum does. Removing a note's attack makes it hard to name the instrument.
- **A spectrogram** shows spectrum against time, at the cost of an unavoidable trade-off: short windows resolve time, long windows resolve frequency, and no window does both.
- **Inharmonicity**, caused by string stiffness, stretches a piano's partials as $f_n = nf_1\sqrt{1+Bn^2}$, which forces stretched tuning.
- **Formants** are the fixed resonances of an instrument's body. They stay put as the pitch moves, so a vowel stays recognizable across a singer's range. Source-plus-filter is the model the rest of the book uses.
- **Noise** has a continuous spectrum and is a genuine part of musical sound, not a defect.

## Conceptual Questions

1. Explain why the partials of a sustained musical tone must be exact whole-number multiples of the fundamental, without referring to any particular instrument.

2. A square wave and a sawtooth wave at the same pitch sound clearly different. State the difference in their spectra and predict which sounds hollower.

3. Explain why a waveform with a sharp corner has more high-frequency content than a smooth one.

4. Two signals have identical spectra but scrambled relative phases, and look completely different on an oscilloscope. Explain why they sound nearly the same, and name one situation in which they would not.

5. Explain why cutting the first tenth of a second off a recorded piano note makes it difficult to identify the instrument, given that the spectrum of the remainder is unchanged.

6. A spectrogram of a plucked note shows the upper bands fading before the lower ones. Explain what this says about how the note's timbre changes as it decays.

7. Explain what a formant is, and why singing a vowel at a higher pitch does not move it.

8. A cymbal has a spectrum with no clear lines in it. Explain why it has no definite pitch, and relate your answer to the modes of a plate.

## Problems

:::{exercise}
:label: ex-fourier-and-timbre-1

A periodic waveform repeats every $4.55$ ms. (a) What is its fundamental frequency? (b) What are the frequencies of its first five harmonics?
:::

:::{solution} ex-fourier-and-timbre-1
:label: sol-fourier-and-timbre-1
:class: dropdown

(a) The fundamental is the reciprocal of the period:

$$
f_1 = \frac{1}{4.55\times10^{-3}\ \text{s}} = 220\ \text{Hz}.
$$

(b) Harmonics are whole-number multiples:

$$
220,\; 440,\; 660,\; 880,\; 1100\ \text{Hz}.
$$

Therefore, the tone is A3 and its first five harmonics run up to $1100$ Hz, spanning, in musical terms, two octaves and a major third above the fundamental.
:::

:::{exercise}
:label: ex-fourier-and-timbre-2

A sawtooth wave has harmonic amplitudes proportional to $1/n$. (a) What is the amplitude of the 8th harmonic relative to the fundamental? (b) Express that ratio in decibels. (c) Repeat for a triangle wave, whose odd harmonics fall as $1/n^2$.
:::

:::{solution} ex-fourier-and-timbre-2
:label: sol-fourier-and-timbre-2
:class: dropdown

(a) For the sawtooth, $A_8/A_1 = 1/8 = 0.125$.

(b) In decibels, using $20\log_{10}$ for an amplitude ratio:

$$
20\log_{10}(0.125) = -18.1\ \text{dB}.
$$

(c) For the triangle, $A_8 = 0$: the 8th harmonic is even and therefore absent. Taking the 7th instead:

$$
\frac{A_7}{A_1} = \frac{1}{49} = 0.0204, \qquad 20\log_{10}(0.0204) = -33.8\ \text{dB}.
$$

Therefore, the sawtooth's 8th harmonic is $18$ dB down and the triangle's 7th is $34$ dB down: the triangle therefore sounds much closer to a pure tone.
:::

:::{exercise}
:label: ex-fourier-and-timbre-3

A tone contains partials at $300$, $400$, $500$, $600$, and $700$ Hz. (a) What is the fundamental frequency? (b) Which harmonic numbers are these? (c) Is any energy present at the fundamental?
:::

:::{solution} ex-fourier-and-timbre-3
:label: sol-fourier-and-timbre-3
:class: dropdown

(a) The partials are spaced $100$ Hz apart and each is a multiple of $100$ Hz, so $f_1 = 100$ Hz.

(b) They are the 3rd, 4th, 5th, 6th, and 7th harmonics.

(c) No, there is nothing at $100$ Hz, and nothing at $200$ Hz either.

Therefore, the waveform repeats $100$ times a second and a listener hears a pitch of $100$ Hz despite the complete absence of energy there. This is the **missing fundamental**, taken up in [Chapter 8](#ch-pitch-and-consonance).
:::

:::{exercise}
:label: ex-fourier-and-timbre-4

A piano string sounds $262$ Hz and has an inharmonicity coefficient $B = 1.3\times10^{-4}$. (a) Find the frequency of its 2nd partial. (b) Find its 8th. (c) Express each as cents sharp of a true harmonic.
:::

:::{solution} ex-fourier-and-timbre-4
:label: sol-fourier-and-timbre-4
:class: dropdown

Using $f_n = nf_1\sqrt{1 + Bn^2}$.

(a) For $n = 2$:

$$
f_2 = 2(262)\sqrt{1 + (1.3\times10^{-4})(4)} = 524\sqrt{1.00052} = 524.14\ \text{Hz},
$$

against an exact $524$ Hz. In cents:

$$
1200\log_2(524.14/524) = 0.45\ \text{cents}.
$$

(b) For $n = 8$:

$$
f_8 = 8(262)\sqrt{1 + (1.3\times10^{-4})(64)} = 2096\sqrt{1.00832} = 2104.7\ \text{Hz},
$$

against an exact $2096$ Hz:

$$
1200\log_2(2104.7/2096) = 7.2\ \text{cents}.
$$

Therefore, the 2nd partial is sharp by half a cent, inaudible alone, and the 8th by $7$ cents, which is easily enough to produce audible beating against another string's true harmonic. That beating is what forces stretched tuning.
:::

:::{exercise}
:label: ex-fourier-and-timbre-5

A tone is built from harmonics of $200$ Hz with amplitudes $1.0$, $0.5$, $0.33$, $0.25$, $0.2$ for $n = 1$ to $5$. Calculate its spectral centroid.
:::

:::{solution} ex-fourier-and-timbre-5
:label: sol-fourier-and-timbre-5
:class: dropdown

The spectral centroid is the amplitude-weighted mean frequency:

$$
\text{centroid} = \frac{\sum A_n f_n}{\sum A_n}.
$$

The numerator:

$$
(1.0)(200) + (0.5)(400) + (0.33)(600) + (0.25)(800) + (0.2)(1000)
$$
$$
= 200 + 200 + 198 + 200 + 200 = 998.
$$

The denominator:

$$
1.0 + 0.5 + 0.33 + 0.25 + 0.2 = 2.28.
$$

So

$$
\text{centroid} = \frac{998}{2.28} = 438\ \text{Hz}.
$$

Therefore, the centroid is about $438$ Hz, roughly the 2nd harmonic. Note the pattern visible in the numerator: with amplitudes falling as $1/n$, every harmonic contributes equally to the centroid, so $1/n$ spectra sound as bright as they do.
:::

:::{exercise}
:label: ex-fourier-and-timbre-6

A spectrogram is computed with a window of $46$ ms. (a) Approximately what frequency resolution does this give? (b) Could it separate the 1st and 2nd harmonics of a $100$ Hz tone? (c) Could it resolve two events $10$ ms apart in time?
:::

:::{solution} ex-fourier-and-timbre-6
:label: sol-fourier-and-timbre-6
:class: dropdown

(a) The frequency resolution of a window of duration $T$ is roughly $\Delta f \approx 1/T$:

$$
\Delta f \approx \frac{1}{46\times10^{-3}\ \text{s}} = 22\ \text{Hz}.
$$

(b) Yes. The two harmonics are $100$ Hz apart, comfortably more than the $22$ Hz resolution.

(c) No. The window is $46$ ms long, so two events $10$ ms apart fall inside the same window and are smeared together.

Therefore, this window is good for frequency and poor for time. Resolving the $10$ ms events would need a window under about $10$ ms, which would degrade the frequency resolution to roughly $100$ Hz, no longer able to separate the harmonics of part (b). This is the trade-off of §5.4, in numbers.
:::

:::{exercise}
:label: ex-fourier-and-timbre-7

A clarinet's spectrum contains strong odd harmonics and weak even ones in its low register. Its lowest note sounds $147$ Hz. (a) List the frequencies of its first four strong partials. (b) A flute at the same pitch has all harmonics. List its first four. (c) Explain the timbral consequence.
:::

:::{solution} ex-fourier-and-timbre-7
:label: sol-fourier-and-timbre-7
:class: dropdown

(a) Odd harmonics of $147$ Hz: $147$, $441$, $735$, $1029$ Hz.

(b) All harmonics: $147$, $294$, $441$, $588$ Hz.

(c) The clarinet is missing the octave ($294$ Hz), the second octave ($588$ Hz), and every other even partial. The octave above the fundamental is the partial that most reinforces a sense of a full, rounded tone, so removing it leaves the characteristic hollow, woody clarinet sound.

Therefore, the difference is not a matter of degree but of which partials exist at all: the same distinction the stopped and open pipes of [Chapter 3](#ch-superposition) demonstrated.
:::

:::{exercise}
:label: ex-fourier-and-timbre-8

Two tones have identical harmonic amplitudes and different phases. (a) Do they have the same waveform? (b) Do they sound the same? (c) Do they carry the same energy? Justify each answer.
:::

:::{solution} ex-fourier-and-timbre-8
:label: sol-fourier-and-timbre-8
:class: dropdown

(a) No. Phase determines how the harmonics line up, and shifting them changes the shape of the sum entirely, often changing the peak amplitude by a factor of two or more.

(b) Essentially yes, for a steady tone. This is Ohm's acoustic law: the ear analyzes into frequency components and is largely insensitive to the relative phases among them.

(c) Yes. The energy is $\sum A_n^2$, which contains no phases at all.

Therefore, the two differ in waveform, agree in energy, and agree in sound, which is only strange if one assumes the ear works on the waveform. It does not; it works on something much closer to the spectrum.
:::

:::{exercise}
:label: ex-fourier-and-timbre-9

A guitar string is plucked $1/7$ of the way along its length. (a) Which harmonics are missing? (b) Explain, in terms of this chapter's vocabulary, why guitar makers often place the bridge so that the string is *not* plucked at a simple fraction.
:::

:::{solution} ex-fourier-and-timbre-9
:label: sol-fourier-and-timbre-9
:class: dropdown

(a) Plucking at $L/7$ puts the pluck at a node of the 7th mode and all its multiples, so harmonics 7, 14, 21, … are absent.

(b) Removing the 7th harmonic is, in this case, desirable rather than accidental. The 7th harmonic is $31$ cents flat of any equal-tempered note ([Chapter 9](#ch-scales-and-tuning)) and clashes with the harmonies of common-practice music, so plucking near $L/7$ is a way of suppressing a partial that would otherwise sound out of tune.

Therefore, the pluck point is a spectral design choice rather than an arbitrary one, and the same reasoning explains why piano hammers strike at about $1/7$ of the string length.
:::

:::{exercise}
:label: ex-fourier-and-timbre-10

A sung vowel has formants at $700$ Hz and $1200$ Hz. It is sung first at $f_1 = 140$ Hz and then at $f_1 = 350$ Hz. (a) Which harmonic falls nearest each formant, at each pitch? (b) Comment on which pitch will render the vowel more clearly.
:::

:::{solution} ex-fourier-and-timbre-10
:label: sol-fourier-and-timbre-10
:class: dropdown

(a) At $f_1 = 140$ Hz the harmonics are $140$, $280$, $420$, $560$, $700$, $840$, … The 5th harmonic ($700$ Hz) lands exactly on the first formant; the closest to $1200$ Hz is the 9th at $1260$ Hz, $60$ Hz away.

At $f_1 = 350$ Hz the harmonics are $350$, $700$, $1050$, $1400$, … The 2nd ($700$ Hz) lands on the first formant; the closest to $1200$ Hz is the 3rd at $1050$ Hz or the 4th at $1400$ Hz, both $150$–$200$ Hz away.

(b) The low pitch. Its harmonics are spaced $140$ Hz apart, so there is nearly always one close to any formant, and the formant peaks are well sampled. At the high pitch the harmonics are $350$ Hz apart, and a formant can fall in a gap between them, leaving the ear with no evidence that it is there.

Therefore, the vowel is clearer at the lower pitch: the reason a soprano's words become hard to make out at the top of her range, and the reason singers modify vowels there ([Chapter 13](#ch-the-singing-voice)).
:::

:::{exercise}
:label: ex-fourier-and-timbre-11

Show that for a waveform built from harmonics with amplitudes $A_n$, the total energy is proportional to $\sum A_n^2$ and is independent of the phases.
:::

:::{solution} ex-fourier-and-timbre-11
:label: sol-fourier-and-timbre-11
:class: dropdown

The energy of a signal over one period is proportional to the mean of its square:

$$
\langle y^2\rangle = \left\langle \left(\sum_n A_n\sin(2\pi n f_1 t + \phi_n)\right)^2\right\rangle .
$$

Expanding the square gives terms of two kinds. The "diagonal" terms are

$$
A_n^2\,\langle \sin^2(2\pi n f_1 t + \phi_n)\rangle = \tfrac12 A_n^2,
$$

since the mean square of a sinusoid is $\frac12$ whatever its phase. The "cross" terms, with $n \ne m$, are

$$
A_nA_m\,\langle \sin(2\pi n f_1 t + \phi_n)\sin(2\pi m f_1 t + \phi_m)\rangle = 0,
$$

by the orthogonality of §5.1, and this vanishes for *any* pair of phases.

So

$$
\langle y^2\rangle = \tfrac12\sum_n A_n^2,
$$

which contains no phases at all.

Therefore, the energy depends only on the amplitudes. This is Parseval's theorem, and it is the formal statement of why two signals with the same spectrum and different phases are equally loud however different they look.
:::

:::{exercise}
:label: ex-fourier-and-timbre-12

A note's partials decay with time constants $\tau_n = \tau_1/n$: the $n$th partial decaying $n$ times as fast as the fundamental. Take $\tau_1 = 2.0$ s. (a) After $1.0$ s, what fraction of its initial amplitude does the 1st partial retain? The 6th? (b) Describe how the timbre changes over the note.
:::

:::{solution} ex-fourier-and-timbre-12
:label: sol-fourier-and-timbre-12
:class: dropdown

(a) Using $A_n(t) = A_n(0)e^{-t/\tau_n}$ with $\tau_n = 2.0/n$:

$$
\frac{A_1(1.0)}{A_1(0)} = e^{-1.0/2.0} = e^{-0.5} = 0.61,
$$
$$
\frac{A_6(1.0)}{A_6(0)} = e^{-1.0/(2.0/6)} = e^{-3.0} = 0.050.
$$

(b) The high partials die far faster than the low ones, so the spectral centroid falls steadily and the note becomes progressively darker and more sine-like as it decays.

Therefore, the timbre of a plucked or struck note is not a fixed property but a moving one, bright at the onset and mellow at the end. This is exactly the behavior visible in the spectrogram of §5.4, and it is one of the things that makes a sustained synthesized tone sound artificial when it is left unchanged throughout.
:::

:::{exercise}
:label: ex-fourier-and-timbre-13

A synthesizer produces a tone with harmonics at exactly $1/n$ amplitude and no noise, no envelope variation, and no inharmonicity. Listeners describe it as "sterile". Name three specific additions that would make it more realistic, and say what each contributes.
:::

:::{solution} ex-fourier-and-timbre-13
:label: sol-fourier-and-timbre-13
:class: dropdown

Three, drawing on this chapter:

1. **A transient onset**, partials arriving at slightly different times, with the high ones leading. §5.4 showed that the attack carries more identifying information than the steady spectrum, and a tone that simply switches on has none.

2. **Noise**, breath, bow scrape, key click, at the onset and continuing at low level. Noise has a continuous spectrum and so is entirely absent from a purely harmonic synthesis, yet every real instrument produces it.

3. **Time-varying partial amplitudes**, high harmonics decaying faster than low ones, and small independent fluctuations in each. A real note's spectrum is never constant, and [](#ex-fourier-and-timbre-12) showed how much the timbre moves over a single note.

A fourth worth mentioning is slight inharmonicity or slight pitch instability, which smears each spectral line into a narrow band and removes the unnaturally perfect periodicity.

Therefore, what is missing from the sterile tone is precisely everything Fourier's theorem does not describe: the theorem covers steady periodic sound completely, and real instruments are never quite steady and never quite periodic.
:::

:::{exercise}
:label: ex-fourier-and-timbre-14

A square wave at $150$ Hz is passed through a filter that removes everything above $1000$ Hz. (a) Which harmonics survive? (b) Sketch in words how the waveform changes. (c) How does the sound change?
:::

:::{solution} ex-fourier-and-timbre-14
:label: sol-fourier-and-timbre-14
:class: dropdown

(a) A square wave has odd harmonics only: $150$, $450$, $750$, $1050$, $1350$, … Hz. Those below $1000$ Hz are the 1st, 3rd, and 5th, $150$, $450$, and $750$ Hz.

(b) With only three partials left, the sharp vertical edges disappear. What remains is a rounded, rippling approximation to a square, recognizably square-ish in outline, but with visible oscillation along the flat tops, since three harmonics is far too few to build a corner.

(c) The tone becomes much duller and less reedy. The pitch is unchanged at $150$ Hz, because the fundamental and the harmonic spacing are untouched.

Therefore, the filter has changed the timbre substantially while leaving the pitch exactly where it was: a clean separation of the two attributes, and the basic operation of subtractive synthesis ([Chapter 15](#ch-electronic-and-recorded-sound)).
:::
