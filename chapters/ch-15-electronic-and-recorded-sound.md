---
title: "Electronic and Recorded Sound"
short_title: "Chapter 15. Electronic and Recorded Sound"
label: ch-electronic-and-recorded-sound
numbering:
  enumerator: "15.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 15.1, 15.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-15-electronic-and-recorded-sound.pdf
    chapter: 15
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Describe how dynamic and condenser microphones convert sound pressure into a voltage, and compare their characteristics.
- Read a microphone polar pattern, and choose an appropriate pattern for a stated recording situation.
- Explain how a loudspeaker converts a signal back into sound, and why a single driver cannot cover the audible range.
- Explain how a magnetic pickup converts string motion into a voltage, and why pickup placement changes an electric guitar's timbre.
- Interpret a frequency-response curve, and distinguish linear distortion from nonlinear distortion.
- State the sampling theorem, calculate the Nyquist frequency for a given sampling rate, and explain why 44.1 kHz was chosen for the compact disc.
- Explain aliasing, predict the frequency of an aliased component, and describe the role of the anti-aliasing filter.
- Relate bit depth to dynamic range through the six-decibel-per-bit rule, and explain what dither does and why it helps.
- Explain how perceptual coding uses masking to discard information, and state what is and is not recoverable afterward.
- Compare additive, subtractive, FM, and sampling synthesis, and identify which chapter of the book each one is an application of.
- Explain how two loudspeakers produce a stereo image, and describe the cues a recording uses to place a source in space.

### Introduction

```{figure} ../images/open/ch15-microphone-studio.jpg
:label: fig:ch15-open-microphone
:alt: A close-up photograph of a condenser microphone on a stand in a recording studio.

Recording begins with a membrane converting pressure into motion and then voltage. Shixart1985, CC BY 2.0.
```

Almost all the music anybody hears has been through a microphone, a wire, and a loudspeaker. Live acoustic performance is now the exception rather than the rule, and this chapter is about the chain that has replaced it.

It is a satisfying place to end, because very little in it is new. The chain turns out to be an application of everything already established:

- A **microphone** is a resonator with a diaphragm ([Chapter 4](#ch-resonance)) whose directivity is governed by size against wavelength ([Chapter 2](#ch-wave-motion)).
- **Digital audio** rests on Fourier's theorem ([Chapter 5](#ch-fourier-and-timbre)): a signal with no energy above some frequency can be captured by samples taken fast enough.
- **Perceptual coding** works because masking ([Chapter 7](#ch-loudness)) makes much of a signal inaudible, so it need not be stored.
- **Synthesis** is the spectrum of [Chapter 5](#ch-fourier-and-timbre) and the source–filter model of [Chapter 13](#ch-the-singing-voice), built deliberately rather than found in an instrument.
- **Stereo** exploits the localization cues of [Chapter 6](#ch-the-ear), and artificial reverberation is the impulse response of [Chapter 14](#ch-room-acoustics).

There is one genuinely new idea, and it is a deep one: a continuous signal can be represented **exactly** by a finite list of numbers. The rest is engineering.

```{video} https://www.youtube.com/watch?v=3DdUvoc7tJ4
:video-title: How Do Vinyl Records Hold Stereo Sound?
:label: fig:ch15-vinyl-stereo-video
:alt: Diagrams and close views of a record groove show how its two walls encode stereo channels.

Technology Connections explains the 45/45 groove geometry that stores two audio channels in one mechanical trace. The construction is a compact example of turning two electrical signals into motion and back again.
```

```{video} https://www.youtube.com/watch?v=GuCdsyCWmt8
:video-title: Vinyl LP in an Electron Microscope
:label: fig:ch15-vinyl-microscope-video
:alt: Electron-microscope images reveal the modulated groove of a vinyl record.

Ben Krasnow images a record groove directly with an electron microscope. The magnified walls make the physical waveform traced by a playback stylus visible rather than abstract.
```

## Microphones and Loudspeakers

### Turning Pressure Into Voltage

A microphone is a pressure detector with a diaphragm, and there are two common ways to read its motion.

A **dynamic** microphone attaches a coil of wire to the diaphragm and suspends it in a magnetic field. Motion induces a voltage. It is rugged, needs no power, and handles very loud sources, but the coil's mass limits its high-frequency response and its transient accuracy.

A **condenser** microphone makes the diaphragm one plate of a capacitor. Motion changes the capacitance and hence the voltage across it. The diaphragm can be made extremely light, so the response extends further and transients are tracked more faithfully, at the cost of needing a power supply and being more fragile.

The mechanical requirement is the same in both cases and is worth stating: the diaphragm's resonance should be placed *outside* the band of interest, and it should be heavily damped, so that the microphone responds evenly rather than coloring everything with its own resonance. This is [Chapter 4](#ch-resonance)'s low-$Q$ design philosophy, for the same reason a guitar body needs it.

### Polar Patterns

A microphone's directivity is set by whether its diaphragm is exposed to pressure on one side or both.

```{figure} ../images/ch15-polar-patterns.svg
:label: fig:ch15-polar-patterns
:alt: Four polar plots showing an omnidirectional pattern as a circle, a cardioid as a heart shape with a null at the rear, a figure-of-eight with nulls at the sides, and a hypercardioid with a narrower front lobe and a small rear lobe.

The four standard patterns. **Omnidirectional** responds to pressure alone and hears everything equally. **Figure-of-eight** responds to the pressure *difference* across the diaphragm, so it is deaf at the sides. **Cardioid** is the sum of the two, giving a rear null. **Hypercardioid** is a different mixture, trading a small rear lobe for a narrower front.
```

The choice is a practical one. A cardioid rejects the room and the audience, which suits a close-miked instrument in a poor room. An omnidirectional captures the room, which suits a good hall. A figure-of-eight rejects sound from the sides, and is used to isolate two instruments facing each other.

:::{note}
Any directional microphone, that is, any that responds to pressure *difference*, exhibits **proximity effect**: the bass response rises sharply as the source comes close, by $10$ dB or more within a few centimeters. Broadcasters exploit it deliberately for an authoritative voice, and singers who work close to the microphone must either compensate or lean back.
:::

### Loudspeakers, Drivers, and Crossovers

A loudspeaker runs the microphone backwards: current through a coil in a magnetic field produces force, which moves a cone, which pushes air.

It faces a problem [Chapter 2](#ch-wave-motion) identified. Directivity depends on the source's size compared with the wavelength, and a single driver has one size while music spans a factor of a thousand in wavelength. A driver large enough to move air at $40$ Hz beams badly at $4$ kHz; one small enough to radiate $10$ kHz evenly cannot shift enough air to produce bass at all.

The solution is multiple drivers, a **woofer**, sometimes a midrange, and a **tweeter**, with a **crossover** network dividing the signal between them. The crossover is itself a compromise, since the drivers must blend through the handover region without canceling, and crossover design is much of what distinguishes loudspeakers.

The low-frequency problem is attacked separately. A cone radiates from both faces, in opposite phase, so at long wavelengths the front and rear outputs meet around the edge and cancel. An enclosure prevents that. A **sealed** box is simple and well-behaved; a **bass-reflex** box adds a tuned port, a Helmholtz resonator ([Chapter 4](#ch-resonance)), that reinforces the bottom octave at the cost of a steeper roll-off below it.

```{video} https://www.youtube.com/watch?v=jhg90zsjqt4
:video-title: How Do Speakers Work?
:label: fig:ch15-speakers-video
:alt: A cutaway animation shows a loudspeaker magnet, voice coil, suspension, and moving cone.

Branch Education follows an electrical signal through the magnet and voice coil to the moving cone and the pressure wave radiated into the room. The cutaway view shows how the components described above fit together.
```

### Electromagnetic Pickups: A Different Transducer

A microphone reads pressure in the air; an electric guitar's **pickup** reads the string directly, and it works on a different principle entirely.

A magnetic pickup is a coil of wire wound around a permanent magnet. The magnet's field passes through the string, provided the string is ferrous (steel, or steel-wound), and magnetizes a section of it. As the string vibrates, it disturbs that field, and the changing flux through the coil induces a voltage by Faraday's law. No power supply, no diaphragm: the string *is* the diaphragm.

One consequence is easy to miss. Because the induced voltage depends on the *rate of change* of flux, the pickup's output is proportional to the string's **velocity**, not its displacement. This is the same distinction [Chapter 10](#ch-string-instruments) draws between the bridge force a soundboard responds to and the string's actual shape.

A second consequence is audible on every electric guitar. A pickup samples the string's motion at one fixed point along its length, and [Chapter 10](#ch-string-instruments) showed that the plucking or driving point determines which harmonics are strong: a point that is a node for some harmonic contributes almost nothing at that harmonic to the output. A **neck pickup**, positioned nearer the string's midpoint, favors the fundamental and sounds warm; a **bridge pickup**, positioned near a region where high harmonics have their antinodes, emphasizes them and sounds bright and biting. Switching pickups, or blending them, is comb filtering by another name, chosen by ear rather than calculated.

Not every electric or amplified string instrument uses this principle. A **piezoelectric pickup**, common on acoustic-electric guitars, basses, and violins, is mounted under the bridge saddle and generates a voltage from mechanical stress rather than magnetic flux, so it works on nylon or gut strings that a magnetic pickup cannot see at all, and it responds to the bridge's motion rather than the string's.

## Signals and Their Imperfections

### Frequency Response

The **frequency response** of any component is its gain against frequency. A perfect one would be flat across the audible range.

Nothing is. Loudspeakers are the worst offenders by a wide margin: even a good one varies by several decibels across its range, while a competent amplifier is flat to a fraction of a decibel. In any audio chain, the transducers, microphone, loudspeaker, and the room, are where essentially all of the frequency-response error lives.

```{openlyceum} Oscilloscope
:label: fig:ch15-oscilloscope-sim

An oscilloscope with a signal generator behind it. Set a sine wave and measure
its period from the screen; then add a second channel and look at what a sum
looks like. This is the instrument the laboratory exercises in
[](#appendix-laboratory) assume; fluency with it helps before meeting a real one.
```

### Linear and Nonlinear Distortion

Two kinds of error, and conflating them causes endless confusion.

**Linear distortion** changes the *balance* of the frequencies present. A frequency-response error is linear distortion, and so is a phase shift. It adds nothing new: whatever comes out was in the input, at a different level. It can, in principle, be corrected by an inverse filter, which is what room equalization attempts.

**Nonlinear distortion** creates frequencies that were **not present in the input**. If the output is not proportional to the input, [Chapter 3](#ch-superposition)'s superposition fails, and a sum of two tones produces components at sums and differences of their frequencies. This cannot be corrected by filtering, because the new components are entangled with the wanted ones.

Two measures are quoted. **Total harmonic distortion** measures added harmonics of a single input tone. **Intermodulation distortion** measures the sum and difference components from two tones, and is the more revealing, because harmonics of a musical note are at least musically related to it while intermodulation products are not.

:::{warning}
Nonlinearity is not always a defect. A guitar amplifier driven into distortion is a nonlinear device used deliberately, and its intermodulation products are the sound. The distinction is whether the nonlinearity is chosen. This is the same point [Chapter 12](#ch-percussion) made about cymbals.
:::

### Noise and Dynamic Range

Every stage adds noise, and the **dynamic range** of a system is the span between its noise floor and the level at which it distorts.

The requirement follows from [Chapter 7](#ch-loudness). An orchestra spans about $50$ dB from *pianissimo* to *fortissimo*, and a good hall has a background around $25$ dB SPL. A system with $90$ dB of dynamic range has ample margin; one with $50$ dB does not, and either the quiet passages disappear into hiss or the loud ones distort.

## Digital Audio

### Sampling and the Nyquist Frequency

Here is the central result.

**The sampling theorem.** A signal containing no frequencies above $f_{\max}$ is **completely determined** by samples taken at any rate greater than $2f_{\max}$.

Not approximately. Completely. The samples contain every bit of information in the original, and the original can be reconstructed from them exactly.

```{figure} ../images/ch15-sampling.svg
:label: fig:ch15-sampling
:alt: Left, a waveform with sample points marked as dots on vertical stems. Right, the original waveform and a reconstruction from the samples, lying exactly on top of one another.

Sampling and reconstruction. The right panel is the surprising half: the reconstruction is not a join-the-dots approximation but an exact recovery, obtained by summing a $\mathrm{sinc}$ function centered on each sample. Nothing has been lost.
```

The **Nyquist frequency** is half the sampling rate: the highest frequency a given rate can represent.

The compact disc samples at $44.1$ kHz, giving a Nyquist frequency of $22.05$ kHz, comfortably above the $20$ kHz limit of hearing. The awkward number is historical: early digital recorders stored data on video tape, and $44.1$ kHz was what fitted the existing video line rates.

### Aliasing and the Anti-Aliasing Filter

The theorem's condition, no frequencies above Nyquist, is not optional, and violating it is not a gentle degradation.

```{animation} ch15-aliasing
:label: fig:ch15-aliasing
:alt: Left, a 9 Hz sine and a 1 Hz sine both passing exactly through the same sample points. Right, a folding diagram showing input frequency against the frequency actually heard, rising to Nyquist and then folding back down repeatedly.

**Left**: a $9$ Hz signal sampled at $10$ Hz produces exactly the same samples as a $1$ Hz signal. Nothing in the data can distinguish them. **Right**: the general rule, every frequency above Nyquist is **folded** back below it, reappearing as a different frequency altogether.
```

The consequence is severe. Aliased components are not a distortion of the original; they are *new frequencies at unrelated pitches*, and once the samples are taken there is no way to remove them.

```{audio} ch15-aliasing-sweep
:label: fig:ch15-aliasing-sweep
:transcript: A rising tone that climbs for about half the clip, then turns round and descends, and then turns again, even though the generator is sweeping steadily upward the whole time.

A sweep from $200$ Hz to $7$ kHz, synthesized at $8$ kHz with no anti-aliasing filter. Above $4$ kHz the tone folds back and descends. Nothing in the generator ever descends; what you are hearing is the folding diagram above, made audible.
```

The cure is to filter **before** sampling. An **anti-aliasing filter** removes everything above Nyquist while the signal is still continuous, so the theorem's condition is satisfied. It must come first, after sampling, the aliased components are indistinguishable from real ones.

This is the technical reason for sampling faster than strictly necessary. A perfect filter is impossible, so a real one needs a transition band, and the gap between $20$ kHz and $22.05$ kHz is where the CD's filter does its work.

### Quantization, Bit Depth, and Dither

Sampling discretizes time. **Quantization** discretizes amplitude, rounding each sample to the nearest of a finite set of levels, and unlike sampling it is *not* lossless.

The error is bounded by half a level, and the resulting dynamic range is

$$
\text{dynamic range} \approx 6.02\,b + 1.76\ \text{dB},
$$

with $b$ the number of bits: the useful rule being **about $6$ dB per bit**. A 16-bit CD gives $98$ dB, comfortably beyond any listening room. A 24-bit studio format gives $146$ dB, which is far beyond any microphone, and exists to provide headroom during processing rather than for final delivery.

```{figure} ../images/ch15-quantization.svg
:label: fig:ch15-quantization
:alt: Three panels showing a sine wave quantized to three bits with visible steps, the same with dither added showing a noisier but less stepped result, and eight-bit quantization which is nearly smooth.

Quantization at three bit depths. The middle panel shows what **dither** does: adding a small amount of noise *before* quantizing.
```

Dither seems perverse, deliberately adding noise to improve quality, and it is one of the more elegant ideas in signal processing. Without it, the quantization error is **correlated** with the signal: it follows the waveform, producing harmonic distortion that is worst on quiet passages, exactly where it is least welcome. Adding a small random noise decorrelates the error, converting it into a steady, signal-independent hiss.

The total error energy is slightly greater. The audible result is much better, because the ear is far more tolerant of steady noise than of signal-dependent distortion.

```{audio} ch15-16-bit, ch15-6-bit, ch15-6-bit-dithered
:names: 16-bit, 6-bit undithered, 6-bit dithered
:figure: ../images/ch15-bit-depth.svg
:label: fig:ch15-bit-depth
:transcript: The same decaying note three times. The first is clean. The second is clean at first and then breaks up into a gritty, buzzy crackle as it fades. The third has an audible steady hiss but fades away smoothly.

The same note at three quantizations. Listen to the **tails**. The undithered version does not merely get noisy as it decays, it becomes distorted and granular, because the error is following the signal. The dithered version has more noise overall and sounds better, which is the whole argument for dither.
```

## Perceptual Coding

### Using Masking to Throw Things Away

A CD carries about $1.4$ megabits per second. An MP3 at $128$ kbit/s carries a tenth of that and most listeners cannot reliably tell them apart. Something is being thrown away, and the question is what.

The answer comes straight from [Chapter 7](#ch-loudness). **If a component is masked, the listener cannot hear it; so it does not need to be stored.**

```{figure} ../images/ch15-perceptual-coding.svg
:label: fig:ch15-perceptual-coding
:alt: A plot of level against frequency showing the threshold of hearing in quiet as a dashed curve, a raised masked threshold around a loud 900 Hz tone, and a set of tones of which those above the threshold are marked kept and those below are marked discarded.

How a codec decides. It computes the **masked threshold**, the level below which nothing is audible, given what else is present, and discards everything under it. The discarded components are not approximated or attenuated; they are simply not stored.
```

A codec works in short blocks, and for each one it transforms to the frequency domain, computes the masked threshold from a psychoacoustic model, allocates bits so that quantization noise in each band sits just below that threshold, and encodes the result.

```{audio} ch15-codec-full, ch15-codec-stripped
:names: All components, Masked components removed
:figure: ../images/ch15-perceptual-coding.svg
:label: fig:ch15-codec
:transcript: Two tones that sound essentially identical. The second has had three quiet partials removed entirely, and it is very hard to hear any difference at all.

A loud $900$ Hz tone with three quiet partials, and the same with those partials deleted. They are hard to tell apart because the partials were masked, they were present in the signal and absent from your perception of it, so removing them changed nothing you could hear.
```

### What a Lossy Codec Keeps

The bit allocation follows the ear's own priorities, and the consequences are visible in what codecs are good and bad at.

**Low frequencies get more bits**, because the critical bands are narrower there and masking is less generous.

**Steady tones compress well**; sharp transients compress badly. A transient needs short blocks to be located in time, and short blocks have poor frequency resolution ([Chapter 5](#ch-fourier-and-timbre)'s trade-off, in a new guise). Applause, castanets, and harpsichords are the classic hard cases, and codecs switch block length dynamically for that reason.

**Stereo is exploited.** Much of the two channels is common, and encoding a sum and a difference is cheaper than encoding both.

### What Is Lost for Good

Two honest caveats.

**Lossy is lossy.** The discarded information is gone. Re-encoding an MP3, decoding and re-encoding, as happens when a file is edited or converted, applies the model to a signal that has already been altered, and the errors accumulate. Archives should be stored losslessly.

**The model can be wrong.** The masking model is built on average listeners and typical signals. Unusual material can defeat it, and the artifacts are characteristic: pre-echo, where a transient's quantization noise is spread backwards in time and becomes audible *before* the event that caused it, and a swirling, watery quality in cymbals where the codec's decisions change from block to block.

## Synthesis

### Additive Synthesis: Fourier in Reverse

```{figure} ../images/ch15-synthesis-methods.svg
:label: fig:ch15-synthesis-methods
:alt: Three spectra. Additive shows a few individually specified partials; subtractive shows a full harmonic series with a filter curve cutting the upper partials; FM shows a symmetric cluster of sidebands.

Three routes to a spectrum. Additive builds it partial by partial, subtractive carves it out of a rich source, and FM generates a whole family of sidebands from two oscillators.
```

**Additive synthesis** builds a sound by summing sinusoids with individually chosen amplitudes and envelopes. It is Fourier's theorem run backwards, and it can produce any periodic sound whatever.

Its weakness is not sound quality but **control**. A realistic instrument needs dozens of partials, each with its own time-varying amplitude, which is hundreds of parameters per note. The Hammond organ is additive synthesis with nine drawbars, and it sounds like a Hammond organ rather than like anything else, which says something about how far nine partials get you.

### Subtractive Synthesis and the Source–Filter Model Again

**Subtractive synthesis** starts with a spectrally rich source, a sawtooth, a square, or noise, and removes what is not wanted with a filter.

This is exactly the **source–filter model** of [Chapter 13](#ch-the-singing-voice), and the analogy is not loose: the oscillator is the vocal folds and the filter is the vocal tract. A resonant low-pass filter with a swept cutoff is imitating a formant, and a synthesizer player sweeping a filter is doing what a singer does moving their tongue.

It dominated analogue synthesis because it is efficient. Two or three controls, cutoff, resonance, and an envelope on the cutoff, produce an enormous range of usable timbres, where additive synthesis needs hundreds.

```{audio} ch15-additive, ch15-subtractive, ch15-fm
:names: Additive, Subtractive, FM
:figure: ../images/ch15-synthesis-methods.svg
:label: fig:ch15-synthesis-audio
:transcript: Three tones at the same pitch. The first is hollow and organ-like. The second starts bright and darkens as its filter closes. The third is metallic and bell-like, becoming purer as it decays.

The same pitch by three methods. The subtractive example's filter sweep and the FM example's falling modulation index are doing the same job, making the spectrum change over the course of the note, which [Chapter 5](#ch-fourier-and-timbre) identified as the thing static synthesis most obviously lacks.
```

### FM Synthesis and Sampling

**FM synthesis**, discovered by John Chowning in 1967 and commercialized in the Yamaha DX7 in 1983, uses one oscillator to modulate another's frequency.

Modulating a carrier at $f_c$ with a modulator at $f_m$ produces sidebands at

$$
f_c \pm n f_m, \qquad n = 0, 1, 2, \ldots
$$

whose amplitudes are Bessel functions of the **modulation index**: the ratio of frequency deviation to modulator frequency. Raising the index spreads energy into more sidebands.

Two features made it commercially decisive. It is **cheap**: two oscillators produce dozens of partials, which mattered enormously with 1980s hardware. And the **index can be varied over the note**, so a falling index makes a bright attack settle to a pure sustain, precisely the behavior of a struck bar or a bell ([Chapter 12](#ch-percussion)). FM's metallic and bell-like sounds were therefore much better than anything else available at the time.

If $f_c$ and $f_m$ are in a simple ratio, the sidebands land on a harmonic series and the sound is pitched. If not, they do not, and the result is inharmonic, which is the same distinction [Chapter 12](#ch-percussion) drew between a string and a gong, arrived at from the other direction.

**Sampling**, playing back recordings of real instruments, sidesteps synthesis entirely and dominates commercial music production. Its difficulty is that a sample is one note, at one dynamic, at one moment; covering an instrument's range requires many, and the couplings [Chapter 10](#ch-string-instruments) described: a piano played louder is also *brighter*, must be reproduced by switching between samples recorded at different dynamics. A sampler that changes only loudness sounds instantly wrong.

## Space in a Recording

### Two Speakers, One Image

Two loudspeakers can produce a sound that appears to come from a point between them, where nothing is.

The mechanism is **summing localization**. Identical signals from both give a phantom image at the center. Making one louder: an **intensity** difference, pulls the image toward it, and about $15$–$18$ dB places it fully at one speaker. Making one earlier: a **time** difference, does the same, with about $1$ ms sufficing.

Both work because they crudely reproduce what a real source would do at the two ears.

### Localization Cues and the HRTF

Real localization uses three cues, and a recording can only approximate them.

**Interaural time difference** dominates below about $1.5$ kHz: a sound from the left reaches the left ear up to $0.7$ ms sooner.

**Interaural level difference** dominates above: the head shadows the far ear, by up to $20$ dB at high frequencies.

**Spectral cues from the pinna** resolve front from back and above from below ([Chapter 6](#ch-the-ear)), and they are the only cue that can. The whole direction-dependent filter is called the **head-related transfer function**.

Ordinary stereo reproduces only the first two, and only crudely, so a stereo image is a line between the speakers rather than a space. **Binaural** recording, made with microphones in the ears of a dummy head, captures the HRTF as well, and over headphones produces a startling sense of height and behindness. Its limitation is that it encodes *somebody else's* ears, and that it breaks as soon as the listener turns their head, hence the rise of head-tracked systems.

### Reverberation, Real and Artificial

Every recording must decide how much room to include, and the decision cannot be postponed: reverberation recorded into a track cannot be removed.

Modern practice therefore records **dry**, close-miked, in a treated room, and adds reverberation afterwards. Two methods.

**Algorithmic** reverberation builds a decaying field from networks of delays and filters. It is efficient, adjustable in every parameter, and can produce spaces that could not be built.

**Convolution** reverberation uses a measured impulse response of a real hall and convolves the dry signal with it ([Chapter 14](#ch-room-acoustics)). It sounds exactly like that hall, from that seat, because it *is* that hall's response, at the cost of being fixed, since the response encodes one source position, one listening position, and one room.

And so the book's last idea is one of its first. [Chapter 3](#ch-superposition) established superposition; [Chapter 14](#ch-room-acoustics) established that a room's effect is completely described by its impulse response; and convolution reverb is nothing but those two facts applied at forty-four thousand samples per second. A recording engineer placing a soloist in the Concertgebouw is doing linear superposition, very fast.

## Summary

- **Dynamic microphones** use a coil and magnet; **condensers** use a variable capacitor and a much lighter diaphragm. Both want a well-damped resonance outside the audio band, low $Q$, as in [Chapter 4](#ch-resonance).
- **Polar patterns** follow from whether the diaphragm senses pressure (omnidirectional) or pressure difference (figure-of-eight); cardioid is their sum. Every pressure-difference microphone shows **proximity effect**.
- **Loudspeakers need multiple drivers**, because directivity depends on size against wavelength and music spans a factor of a thousand in wavelength. Enclosures prevent front-to-back cancellation; a bass-reflex port is a Helmholtz resonator.
- **A magnetic pickup** induces a voltage from a ferrous string's motion directly, no diaphragm required; its output tracks string velocity, and its fixed sampling point along the string means placement (neck versus bridge) reshapes the harmonic balance, the same driving-point physics as [Chapter 10](#ch-string-instruments).
- **Linear distortion** rebalances existing frequencies and is in principle correctable; **nonlinear distortion** creates new ones and is not.
- **The sampling theorem**: a signal with no energy above $f_{\max}$ is *completely* determined by samples at any rate above $2f_{\max}$. Reconstruction is exact.
- **Aliasing** folds everything above the Nyquist frequency back below it, producing new frequencies at unrelated pitches. The anti-aliasing filter must act **before** sampling, because afterwards nothing can distinguish an alias from a real component.
- **Quantization gives about $6$ dB of dynamic range per bit.** **Dither** adds noise before quantizing, converting signal-correlated distortion into steady hiss, more total error energy, much better sound.
- **Perceptual coding discards masked components**, which by definition cannot be heard. It struggles with transients, because locating them in time requires short blocks and short blocks resolve frequency poorly.
- **Additive synthesis** specifies every partial; **subtractive** filters a rich source and is the source–filter model again; **FM** generates Bessel-weighted sidebands from two oscillators, giving inharmonic spectra cheaply.
- **Stereo works by summing localization**, reproducing interaural time and level differences but not the pinna cues that distinguish front from back. **Convolution reverb** is superposition plus a measured impulse response.

## Conceptual Questions

1. Explain why a condenser microphone tracks transients better than a dynamic one.

2. Explain why an omnidirectional microphone shows no proximity effect while a cardioid does.

3. Explain why a single loudspeaker driver cannot reproduce the whole audible range, referring to source size and wavelength.

4. A guitarist blends a neck and a bridge pickup and notices the tone changes even though nothing about the string or the amplifier has changed. Explain why, referring to the driving-point argument of [Chapter 10](#ch-string-instruments).

5. Distinguish linear from nonlinear distortion, and explain why only one of them can in principle be corrected.

6. State the sampling theorem, and explain what is surprising about the word "completely" in it.

7. Explain why an anti-aliasing filter must be applied before sampling rather than after.

8. Explain why adding noise before quantizing improves the perceived quality, given that it increases the total error.

9. Explain why perceptual codecs handle a sustained organ chord better than applause.

## Problems

:::{exercise}
:label: ex-electronic-and-recorded-sound-1

A system samples at $48$ kHz. (a) What is the Nyquist frequency? (b) What is the highest frequency it can represent? (c) A $30$ kHz component reaches the converter unfiltered. What frequency appears?
:::

:::{solution} ex-electronic-and-recorded-sound-1
:label: sol-electronic-and-recorded-sound-1
:class: dropdown

(a) $48000/2 = 24$ kHz.

(b) Anything below $24$ kHz.

(c) Frequencies above Nyquist fold back:

$$
f_{\text{alias}} = |48000 - 30000| = 18\ \text{kHz}.
$$

Therefore a $30$ kHz component, inaudible in itself, appears as an $18$ kHz component, which is audible to many listeners and is not in the original at all.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-2

A CD samples at $44.1$ kHz with $16$ bits per sample, in stereo. (a) What is the data rate? (b) How many megabytes is a 74-minute disc?
:::

:::{solution} ex-electronic-and-recorded-sound-2
:label: sol-electronic-and-recorded-sound-2
:class: dropdown

(a) Samples per second times bits per sample times channels:

$$
44100 \times 16 \times 2 = 1.41\times10^{6}\ \text{bits/s} = 1.41\ \text{Mbit/s}.
$$

(b) $74$ minutes is $4440$ s:

$$
1.41\times10^{6} \times 4440 = 6.27\times10^{9}\ \text{bits} = 7.83\times10^{8}\ \text{bytes} = 783\ \text{MB}.
$$

Therefore about $780$ MB, which is the familiar capacity of an audio CD: the format's storage was designed around exactly this calculation.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-3

Find the dynamic range of (a) an 8-bit system, (b) a 16-bit system, (c) a 24-bit system. (d) Which is adequate for a concert hall with a $25$ dB background and a $105$ dB peak?
:::

:::{solution} ex-electronic-and-recorded-sound-3
:label: sol-electronic-and-recorded-sound-3
:class: dropdown

Using $6.02b + 1.76$ dB:

(a) $6.02(8) + 1.76 = 49.9$ dB.

(b) $6.02(16) + 1.76 = 98.1$ dB.

(c) $6.02(24) + 1.76 = 146.2$ dB.

(d) The hall requires $105 - 25 = 80$ dB. The 8-bit system is inadequate; 16-bit has $18$ dB of margin and is sufficient; 24-bit is far beyond any microphone's own noise floor and exists to give headroom during processing rather than for delivery.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-4

An MP3 at $128$ kbit/s replaces a CD stream. (a) What is the compression ratio? (b) What fraction of the original data remains? (c) What justifies discarding the rest?
:::

:::{solution} ex-electronic-and-recorded-sound-4
:label: sol-electronic-and-recorded-sound-4
:class: dropdown

(a) $1411/128 = 11.0$.

(b) $1/11 = 9.1\%$.

(c) **Masking** ([Chapter 7](#ch-loudness)). At any instant, most of the spectral detail in a musical signal lies below the masked threshold set by the louder components, and a listener cannot hear it. A codec computes that threshold and spends bits only above it.

Therefore the discarded $91\%$ is not "detail the listener might miss"; it is information the auditory system was never going to receive. The compression is therefore much more effective than a general-purpose lossless compressor, which manages only about $2{:}1$ on audio.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-5

An FM synthesizer has a carrier at $440$ Hz and a modulator at $440$ Hz with index $3$. (a) Where are the first four sideband pairs? (b) Is the result harmonic? (c) Repeat with a modulator at $311$ Hz.
:::

:::{solution} ex-electronic-and-recorded-sound-5
:label: sol-electronic-and-recorded-sound-5
:class: dropdown

(a) Sidebands are at $f_c \pm nf_m$:

$$
440 \pm 440 = 880, 0;\quad 440 \pm 880 = 1320, -440;\quad
440 \pm 1320 = 1760, -880;\quad 440 \pm 1760 = 2200, -1320.
$$

Negative frequencies fold back with inverted phase, so the set is $440$, $880$, $1320$, $1760$, $2200$ Hz.

(b) **Yes**, every component is a multiple of $440$ Hz, so the result is a harmonic series and the sound is clearly pitched.

(c) With $f_m = 311$ Hz: $440 \pm 311 = 751, 129$; $440 \pm 622 = 1062, -182$; $440 \pm 933 = 1373, -493$. The set is $129$, $182$, $440$, $493$, $751$, $1062$, $1373$ Hz, no common fundamental, so the result is **inharmonic** and bell-like.

Therefore the ratio $f_c: f_m$ decides whether FM produces a pitched instrument or a percussion instrument, which is exactly the distinction of [Chapter 12](#ch-percussion) reached from the other direction.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-6

A stereo pair is fed a signal with the left channel $6$ dB louder. (a) Where does the phantom image appear? (b) What time difference would place it similarly? (c) Why do both work?
:::

:::{solution} ex-electronic-and-recorded-sound-6
:label: sol-electronic-and-recorded-sound-6
:class: dropdown

(a) Full deflection to one speaker takes about $15$–$18$ dB, so $6$ dB places the image roughly a third of the way from center to the left speaker.

(b) Full deflection takes about $1$ ms, so a comparable shift needs roughly $0.3$ ms of delay on the right channel.

(c) Both crudely reproduce what a real source to the left would produce at the ears: it would arrive sooner and louder at the left ear. The auditory system integrates the two loudspeakers' outputs and infers a direction consistent with the cues it receives.

Therefore intensity and time panning are interchangeable to a first approximation, and are used interchangeably, though they are not identical, and combining them inconsistently produces an unstable image.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-7

A loudspeaker's woofer is $25$ cm across and its tweeter $25$ mm. (a) Above what frequency does each become larger than a wavelength? (b) Suggest a crossover frequency. (c) Explain the reasoning.
:::

:::{solution} ex-electronic-and-recorded-sound-7
:label: sol-electronic-and-recorded-sound-7
:class: dropdown

(a) Setting $\lambda = d$, so $f = v/d$:

$$
f_{\text{woofer}} = \frac{343}{0.25} = 1.37\ \text{kHz},
\qquad
f_{\text{tweeter}} = \frac{343}{0.025} = 13.7\ \text{kHz}.
$$

(b) Somewhere around $1.5$–$2.5$ kHz.

(c) The crossover should hand over before the woofer starts beaming: that is, at or below about $1.4$ kHz by the calculation above, though in practice a little above is tolerated. It must not be so low that the tweeter is asked to move air at frequencies where its small cone cannot produce enough displacement without distorting.

Therefore the choice is squeezed from both sides, and $2$ kHz is the usual compromise, which is unfortunate, since it sits in the region where hearing is most sensitive and where the ear most easily detects the discontinuity.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-8

Explain quantitatively why a $44.1$ kHz sampling rate is used rather than exactly $40$ kHz, given that hearing extends to $20$ kHz.
:::

:::{solution} ex-electronic-and-recorded-sound-8
:label: sol-electronic-and-recorded-sound-8
:class: dropdown

At exactly $40$ kHz the Nyquist frequency is $20$ kHz, so the anti-aliasing filter would need to pass $20$ kHz unattenuated and stop everything above $20$ kHz completely: an infinitely steep transition, which is impossible.

At $44.1$ kHz the Nyquist frequency is $22.05$ kHz, leaving a transition band from $20$ to $22.05$ kHz. Expressed as a slope requirement, the filter must fall from passband to stopband over

$$
1200\log_2\!\left(\frac{22050}{20000}\right) = 169\ \text{cents},
$$

under a tone and a half, still a demanding filter, but a buildable one.

Therefore the extra $4.1$ kHz buys the filter room to work. The precise figure is historical rather than acoustic: early digital audio was stored on video recorders, and $44.1$ kHz is what fell out of the available line and field rates.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-9

A guitar amplifier is driven into distortion. Two notes at $220$ Hz and $330$ Hz are played. (a) Name four intermodulation products. (b) Are any of them musically related to the input? (c) Comment on why this is nonetheless a popular sound.
:::

:::{solution} ex-electronic-and-recorded-sound-9
:label: sol-electronic-and-recorded-sound-9
:class: dropdown

(a) Sums and differences and their combinations:

$$
330 - 220 = 110\ \text{Hz},\quad 330 + 220 = 550\ \text{Hz},
$$
$$
2(220) - 330 = 110\ \text{Hz},\quad 2(330) - 220 = 440\ \text{Hz}.
$$

(b) Yes, in this case, all of them. The two inputs are a perfect fifth apart ($3{:}2$), so they are harmonics 2 and 3 of a common fundamental at $110$ Hz, and every intermodulation product is therefore also a harmonic of $110$ Hz.

(c) That is precisely why the sound works. For **consonant** intervals the distortion products fall on the existing harmonic series and add weight rather than dissonance. Power chords, built on fifths, sound so good through a distorted amplifier for that reason.

For a more complex chord, a major third, say, the products do *not* all fall on a common series, and the result is muddy. Guitarists know this as the rule that distorted chords should be kept to two notes, and the reason is the arithmetic above.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-10

A convolution reverb uses an impulse response $3.5$ s long, sampled at $48$ kHz. (a) How many samples? (b) A naive convolution of a $4$-minute track requires how many multiply operations? (c) Comment.
:::

:::{solution} ex-electronic-and-recorded-sound-10
:label: sol-electronic-and-recorded-sound-10
:class: dropdown

(a) $3.5 \times 48000 = 1.68\times10^{5}$ samples.

(b) A $4$-minute track is $240 \times 48000 = 1.15\times10^{7}$ samples, and each output sample requires one multiply per impulse-response sample:

$$
1.15\times10^{7} \times 1.68\times10^{5} = 1.9\times10^{12}\ \text{multiplies}.
$$

(c) Two trillion multiplications per channel is far too many for real time on modest hardware.

The remedy is the **convolution theorem**: convolution in time is multiplication in frequency, so the operation can be done by transforming both signals, multiplying, and transforming back. Using the fast Fourier transform this reduces the cost by roughly a factor of $N/\log_2 N$, which here is about $10^4$, bringing two trillion operations down to a few hundred million, which is entirely practical.

Therefore convolution reverb is possible because of Fourier's theorem, which is a pleasing place for a book that began with a vibrating string to end.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-11

Show that quantization gives approximately $6$ dB of dynamic range per bit.
:::

:::{solution} ex-electronic-and-recorded-sound-11
:label: sol-electronic-and-recorded-sound-11
:class: dropdown

With $b$ bits there are $2^b$ levels. Let the full-scale signal be a sine of amplitude $A$, so peak-to-peak it spans $2A$ and each quantization step is

$$
\Delta = \frac{2A}{2^b}.
$$

The quantization error is uniformly distributed over $\pm\Delta/2$, so its mean square is

$$
\langle e^2\rangle = \frac{\Delta^2}{12}.
$$

The signal's mean square is $A^2/2$. The signal-to-noise ratio is therefore

$$
\frac{A^2/2}{\Delta^2/12} = \frac{A^2/2}{(2A/2^b)^2/12} = \frac{12\,A^2\,2^{2b}}{2 \cdot 4A^2} = \frac{3}{2}\,2^{2b}.
$$

In decibels:

$$
10\log_{10}\!\left(\frac{3}{2}\,2^{2b}\right)
= 10\log_{10}(1.5) + 20b\log_{10}(2)
= 1.76 + 6.02\,b\ \text{dB}.
$$

Therefore each additional bit doubles the number of levels, halves the step, and buys $20\log_{10}2 = 6.02$ dB, and the $1.76$ dB offset comes from the ratio between a sine's mean square and a uniform error's.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-12

A recording is made with a cardioid microphone $30$ cm from a singer, in a room with a critical distance of $1.2$ m. (a) Is the recording dominated by direct or reverberant sound? (b) The engineer moves to $2.5$ m. What changes? (c) Which would be preferred, and why?
:::

:::{solution} ex-electronic-and-recorded-sound-12
:label: sol-electronic-and-recorded-sound-12
:class: dropdown

(a) At $30$ cm the microphone is well inside the critical distance, so the direct sound dominates heavily, this is a dry, close recording.

(b) At $2.5$ m the microphone is beyond the critical distance, so the reverberant field dominates and the recording captures mostly room.

(c) For most modern production, the **close** position. A dry recording can have reverberation added afterwards by convolution ([Chapter 14](#ch-room-acoustics)), and the amount can be chosen at mixing time. Reverberation recorded into a track cannot be removed.

Two caveats. The close position will show **proximity effect**, boosting the bass substantially, which must be corrected or exploited. And if the room is genuinely good, a fine hall, the distant position captures something an artificial reverberation cannot quite reproduce. Classical recording still uses distant main pairs for that reason.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-13

Explain, using [Chapter 5](#ch-fourier-and-timbre)'s time–frequency trade-off, why perceptual codecs produce "pre-echo" on sharp transients.
:::

:::{solution} ex-electronic-and-recorded-sound-13
:label: sol-electronic-and-recorded-sound-13
:class: dropdown

A codec works on blocks. Within each block it transforms to the frequency domain, decides how much quantization noise each band can carry without being audible, and quantizes accordingly.

The quantization noise it introduces is spread **uniformly over the whole block**, because the quantization happens in the frequency domain and a frequency-domain error has no localization in time.

Now consider a block containing a castanet click: silence for most of its duration, then a loud transient. The masking model computes a threshold from the block's overall spectrum, which the loud transient dominates, so a generous amount of noise is permitted. That noise is then spread across the entire block, including the silent part *before* the click.

The result is a burst of noise audible in the silence preceding the transient: **pre-echo**.

[Chapter 5](#ch-fourier-and-timbre)'s trade-off is what makes this unavoidable in principle: locating the transient precisely in time requires a short block, and a short block resolves frequency poorly, which degrades the masking model. Codecs respond by **switching block length dynamically**, using short blocks when a transient is detected and long ones otherwise, which mitigates the problem without eliminating it.
:::

:::{exercise}
:label: ex-electronic-and-recorded-sound-14

A sampler reproduces a piano by pitch-shifting one recorded note. (a) What goes wrong if a note recorded at C4 is shifted up an octave? (b) What goes wrong if only one dynamic level was recorded? (c) Relate both to [Chapter 10](#ch-string-instruments).
:::

:::{solution} ex-electronic-and-recorded-sound-14
:label: sol-electronic-and-recorded-sound-14
:class: dropdown

(a) Pitch-shifting by resampling scales *every* frequency in the recording, including the resonances of the soundboard and body. But those resonances are properties of the instrument and do **not** move when the pitch changes, they are formants, in the sense of [Chapter 13](#ch-the-singing-voice). Shifting an octave moves them an octave too, and the result sounds like a smaller instrument. Shifting down produces the well-known "munchkinization" in reverse.

The note's *duration* also scales, so the shifted note decays twice as fast, which is wrong, since a real piano's high notes decay faster for reasons of string mass, not by a factor of exactly two.

(b) [Chapter 10](#ch-string-instruments) showed that a piano hammer's felt is nonlinear: struck harder, contact time shortens and more high harmonics survive. **A piano played louder is brighter, not merely louder.** A sampler with one dynamic level can only change the volume, so a *fortissimo* sounds like a *pianissimo* turned up, instantly recognizable as wrong.

(c) Both failures come from the same source: an instrument is not a single sound with adjustable pitch and volume. Its spectrum depends on the note and on the dynamic, through mechanisms [Chapter 10](#ch-string-instruments) described.

Therefore good samplers record many notes across the range, at several dynamic levels, and cross-fade between them. A convincing sampled piano therefore runs to many gigabytes.
:::
