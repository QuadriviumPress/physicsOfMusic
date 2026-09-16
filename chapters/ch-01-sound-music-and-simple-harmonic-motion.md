---
title: "Sound, Music, and Simple Harmonic Motion"
short_title: "Chapter 1. Sound, Music, and Simple Harmonic Motion"
label: ch-sound-and-shm
numbering:
  enumerator: "1.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 1.1, 1.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-01-sound-music-and-simple-harmonic-motion.pdf
    chapter: 1
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Describe sound as a longitudinal pressure disturbance in a medium, and explain why sound cannot travel through a vacuum while light can.
- Distinguish the physical properties of a sound wave (frequency, amplitude, spectrum, duration) from the perceptual attributes they mostly control (pitch, loudness, timbre, length), and give an example where the correspondence fails.
- State the condition a restoring force must satisfy to produce simple harmonic motion, and explain why so many different vibrating objects satisfy it approximately.
- Write the displacement of a simple harmonic oscillator as a sinusoid, and identify its amplitude, frequency, period, and phase from a graph or an equation.
- Calculate the natural frequency of a mass on a spring and of a simple pendulum, and explain why the frequency of a mass on a spring does not depend on how hard it is struck.
- Relate the energy of a vibrating system to the square of its amplitude, and trace the exchange between kinetic and potential energy over one cycle.
- Explain what damping does to a free vibration, and connect the rate of decay to how long a note sounds after the player stops driving it.
- Estimate the frequency, wavelength, and period of a musical tone from its pitch name, and place it on the range of human hearing.

### Introduction

Strike a tuning fork and hold it up. Nothing looks as though it is happening. Touch the tines and you feel a buzz, and the sound stops; let go and it starts again. Put the base of the fork against a table and the room fills with the note. Take the fork into a vacuum chamber and pump the air out, and the tines go on vibrating in plain sight while the sound dies away to nothing.

Those four observations contain most of what this chapter is about. Something has to **vibrate**. The vibration has to be passed to the **air**: a fork alone is quiet and a fork on a table is loud. Without air, or water, or wood, or some other material, there is no sound at all, however vigorously the source moves. And the sound has a definite **pitch**, the same one every time that fork is struck, whether it is struck gently or hard.

This book is about the physics that connects those facts, and it begins at the beginning: with what sound is, and with the particular kind of motion that musical sources almost always turn out to be doing. That motion is **simple harmonic motion**. Everything later, from the string and air column to the drumhead, vocal folds, microphone diaphragm, and basilar membrane inside your ear, either does it or is built from things that do.

```{figure} ../images/open/ch01-tuning-fork.jpg
:label: fig:ch01-open-tuning-fork
:alt: A tuning fork resting on a page of sheet music.

A tuning fork makes the central idea visible: a small vibrating source can have a definite musical frequency. Image: Lukasz Kobus / European Commission, CC BY 4.0.
```

:::{margin}
A vacuum chamber demonstration is easy to find on video, and worth two minutes: a ringing alarm clock or a small buzzer fades to silence as the pump runs, and comes back as air is let in.
:::

## What Sound Is

### A Disturbance, Not a Substance

Sound is not a substance that travels from a source to your ear. Nothing material makes that trip. What travels is a **disturbance**: a pattern of squeezing and stretching that passes through the air, leaving the air itself essentially where it was.

The standard picture is a line of people standing shoulder to shoulder. Shove the person at one end, and they bump into the next, who bumps into the next, and a shove travels down the line. Everyone ends up roughly where they started; only the shove moves along the row. Sound is the same, with molecules of air instead of people and with collisions instead of bumping.

This matters because it explains the vacuum chamber. A disturbance needs something to disturb. Take away the air and there is nothing to pass the shove along, and no matter how hard the source vibrates, nothing arrives. Light behaves differently, and that difference is worth holding onto: light reaches us across the emptiness between stars, and sound does not cross a meter of vacuum.

:::{note}
The nineteenth century assumed light must also need a medium, and named it the luminiferous ether. The experiments that failed to find it are the subject of relativity rather than acoustics, but the instinct behind the search is exactly the one this section is training: a wave was understood to be a disturbance *of something*.
:::

### Longitudinal Waves and Pressure

The shove down the row of people has a direction, and it is the same direction the disturbance travels. That makes a sound wave **longitudinal**: the air moves back and forth along the direction of travel, not across it.

Waves on a string are the other kind. There, the string moves up and down while the wave moves sideways, and the motion of the medium is perpendicular to the motion of the wave. Those are **transverse** waves. Both kinds matter in this book: a guitar string carries transverse waves, while the air around it carries longitudinal ones. The handover between them at the bridge and soundboard is one of the central problems of instrument design ([Chapter 10](#ch-string-instruments)).

Because the air bunches up in some places and thins out in others, sound can be described either as a **displacement** of the air or as a **pressure** variation. The two descriptions are equivalent but they are not the same picture, and confusing them is the most common early mistake in acoustics.

```{figure} ../images/ch01-longitudinal-wave.svg
:label: fig:ch01-longitudinal-wave
:alt: Dots representing air molecules, bunched into compressions and spread into rarefactions, above a graph of pressure against distance whose maxima line up with the compressions.

A sound wave drawn twice. Above: air molecules, bunched where the wave has pushed them together and thinned where it has pulled them apart. Below: the pressure that bunching produces. A compression is a pressure maximum and a rarefaction is a pressure minimum. Note that the pressure peaks are a quarter of a wavelength away from where the *displacement* of the air is greatest, where the air has moved furthest, it has not yet piled up.
```

Where the molecules are packed more tightly than usual, the pressure is above atmospheric: a **compression**. Where they are spread thinner, the pressure is below atmospheric: a **rarefaction**. The pressure changes involved are startlingly small. Atmospheric pressure is about $101{,}000$ Pa; the quietest sound a healthy young ear can detect is a pressure variation of about $2\times10^{-5}$ Pa, some five thousand million times smaller. A very loud sound, a rock concert at the front, is perhaps $20$ Pa, still only two ten-thousandths of the pressure it rides on. Sound is a whisper of a ripple on an ocean of static pressure.

:::{tip} Self-check
A loudspeaker cone moves out, then back, then out again. At the instant the cone has moved as far *out* as it will go, is the air just in front of it at maximum pressure, minimum pressure, or atmospheric? (Think about whether the cone is still compressing the air at that moment, or has stopped.)
:::

### What a Microphone and an Eardrum Measure

Both a microphone and an eardrum are pressure detectors. Each is a thin membrane with air on one side, and each is pushed in when the pressure outside rises and pushed out when it falls. What the membrane does is trace, over time, the pressure at one point in space.

That is worth dwelling on, because it means everything the rest of this book discusses is somehow encoded in a single wiggling number: pitch, loudness, timbre, the difference between a violin and a clarinet, and the sound of a concert hall: the pressure at your eardrum as a function of time. Two eardrums give two such numbers. There is nothing else. Whatever your auditory system knows about the world of sound, it works it out from that.

The graph of that pressure against time is the **waveform**, and it is the object an oscilloscope displays and an audio file stores. [Chapter 5](#ch-fourier-and-timbre) will show that a waveform contains more structure than it looks like it does, and [Chapter 6](#ch-the-ear) will show how the ear takes it apart.

```{phet} sound-waves
:label: fig:ch01-sound-waves-sim

A loudspeaker driving air, with the compressions and rarefactions drawn directly. Switch between the particle view and the pressure view and check that a compression really does sit where the pressure graph peaks; then change the frequency and watch the spacing of the bands change while their speed does not.
```

## From Sound to Music: Four Attributes

```{figure} ../images/open/ch01-django-reinhardt.jpg
:label: fig:ch01-open-guitarist
:alt: Django Reinhardt playing a guitar.

Music begins with a physical performer and instrument, then becomes a signal at the ear. William P. Gottlieb, public domain.
```

### Pitch, Loudness, Timbre, Duration

Ask a musician to describe a note and you will get four things: how high or low it is, how loud, what it sounds like, and how long it lasts. Those are **pitch**, **loudness**, **timbre**, and **duration**, and they are the perceptual vocabulary this book has to connect to physics.

The connections are, to a first approximation:

| Perceptual attribute | Physical property mostly responsible |
|---|---|
| Pitch | Frequency, how many times per second the pattern repeats |
| Loudness | Amplitude, how large the pressure variation is |
| Timbre | Spectrum and envelope, which frequencies are present, and how they change |
| Duration | Duration |

The phrase "mostly responsible" is doing real work in that table, and the four chapters of [Part III](#ch-the-ear) are largely about the exceptions. Loudness depends on frequency as well as amplitude: a 40 Hz tone and a 1000 Hz tone of identical amplitude are not equally loud, and are not close ([Chapter 7](#ch-loudness)). Pitch depends slightly on loudness. Most strikingly, a sound can have a definite pitch at a frequency that is not present in it at all ([Chapter 8](#ch-pitch-and-consonance)).

For now the first column is a useful map and the second column is where the physics is. One entry is exact: duration is duration.

### Physical Cause and Perceptual Effect

The difference between the two columns needs care, because the language of music runs them together constantly and the physics does not.

**Frequency is a property of the sound. Pitch is a property of your experience of it.** A frequency can be measured with a counter, by anyone, with no listener present. A pitch cannot: it is a judgment, made by an auditory system, and it can be influenced by things the frequency counter knows nothing about. The same is true of amplitude and loudness, and of spectrum and timbre.

This is not pedantry. It is the reason [Chapter 9](#ch-scales-and-tuning) has something to explain: if pitch were simply frequency, there would be no such thing as a tuning system, only arithmetic. And it is the reason [Chapter 15](#ch-electronic-and-recorded-sound) can compress an audio file to a tenth of its size: the parts of the physical signal that the perceptual system cannot use can be thrown away.

:::{warning}
"Pitch" and "frequency" are used interchangeably in ordinary musical speech, and mostly no harm is done. In this book they are kept apart. When the text says *frequency*, it means a number of cycles per second; when it says *pitch*, it means what a listener hears.
:::

### Tone and Noise

One more distinction, and then the physics. Some sounds repeat and some do not.

A sound whose waveform repeats, the same shape, over and over, many times a second, is **periodic**, and periodic sounds have a clear pitch. A sung vowel, a bowed string, a blown pipe: hold any of them steady and the waveform settles into a pattern that repeats. The number of repeats per second is the **frequency**, measured in hertz (Hz), and one cycle takes the **period** $T = 1/f$.

A sound whose waveform does not repeat is **noise**, and noise has no definite pitch. A cymbal crash, a handclap, a consonant, the hiss of air escaping: the waveform wanders and never comes back to where it was.

Music uses both, and the boundary is not sharp. A snare drum is mostly noise, a flute is mostly tone, and the breathy attack of a flute note is noise on the front of a tone. [Chapter 5](#ch-fourier-and-timbre) makes this quantitative; [Chapter 12](#ch-percussion) is largely about instruments that sit between the two.

```{figure} ../images/ch01-frequency-ranges.svg
:label: fig:ch01-frequency-ranges
:alt: A logarithmic frequency axis from 12 Hz to 60 kHz, with horizontal bars showing the ranges of human hearing, the piano, the singing voice, the violin, the double bass, and speech, and a dotted line marking A440.

Where music sits inside the range of hearing. The frequency axis is logarithmic, because that is how pitch works: each doubling of frequency is one octave, and the octaves are therefore equally spaced along this axis. A piano's lowest note is $27.5$ Hz and its highest is $4186$ Hz, seven octaves, and less than half the span of human hearing, most of which is above the highest note any orchestral instrument plays.
```

Two things in that figure deserve comment. First, the audible range is about $20$ Hz to $20{,}000$ Hz: a factor of a thousand, or very nearly ten octaves. Second, almost all musical *fundamentals* live in the bottom half of it. The upper octaves are not empty, but what fills them is the harmonics that give instruments their character ([Chapter 5](#ch-fourier-and-timbre)). A recording that discards everything above 5 kHz therefore sounds muffled rather than merely missing a few high notes.

## Simple Harmonic Motion

### The Linear Restoring Force

Something has to vibrate. The question is why so many different somethings vibrate in the same way.

Take any object sitting at a stable equilibrium: a mass hanging on a spring, a pendulum at the bottom of its swing, a guitar string pulled taut, a diving board, a wine glass rim. "Stable" means that if you displace it slightly, something pushes it back. Call the displacement $x$ and the restoring force $F$. The force is zero at $x = 0$, by the definition of equilibrium, and it points back toward $x = 0$ on either side.

Now the key step. For *small* displacements, the restoring force of essentially any stable system is proportional to the displacement:

$$
F = -kx.
$$

The constant $k$ is the **stiffness**, measured in newtons per meter, and the minus sign says the force opposes the displacement. This is **Hooke's law**, and the reason it applies so widely is not that nature is fond of springs. It is that any smooth restoring force, whatever its true form, looks like a straight line if you zoom in far enough on the point where it crosses zero, and small vibrations never leave that neighborhood.

:::{dropdown} Why any stable system obeys Hooke's law for small displacements
This is the argument that justifies the whole chapter, and it needs one line of calculus.

Let the potential energy of the system be $U(x)$, with a stable equilibrium at $x = 0$. Expand it as a Taylor series:

$$
U(x) = U(0) + U'(0)\,x + \tfrac12 U''(0)\,x^2 + \tfrac16 U'''(0)\,x^3 + \cdots
$$

$U(0)$ is a constant and can be set to zero; it does not affect the force. $U'(0) = 0$, because the force $F = -\mathrm{d}U/\mathrm{d}x$ vanishes at equilibrium, that is what equilibrium means. So the first surviving term is the quadratic one, and

$$
F = -\frac{\mathrm{d}U}{\mathrm{d}x} = -U''(0)\,x - \tfrac12 U'''(0)\,x^2 - \cdots
$$

For small enough $x$, the $x^2$ term and everything after it are negligible beside the $x$ term, and what remains is $F = -kx$ with $k = U''(0)$. Stability requires $U''(0) > 0$, a minimum, not a maximum, so $k$ is positive.

The generality is the point: nothing was assumed about the system beyond having a smooth potential with a minimum. A mass on a spring, a molecule in a crystal, and a drumhead all vibrate sinusoidally at small amplitude for that reason, and "small amplitude" is the caveat on nearly every result in this book. Where it fails, a cymbal driven hard ([Chapter 12](#ch-percussion)), a loudspeaker pushed past its limits ([Chapter 15](#ch-electronic-and-recorded-sound)), the consequences are audible and specific.
:::

### The Sinusoid and Its Four Numbers

A system obeying $F = -kx$ moves in a particular way, and only that way. Displaced and released, it traces out a sine curve in time:

$$
x(t) = A\sin(2\pi f t + \phi).
$$

This is **simple harmonic motion**, and the equation has exactly four numbers in it. Three describe the motion and the fourth describes when you started the clock.

```{figure} ../images/ch01-sinusoid-anatomy.svg
:label: fig:ch01-sinusoid-anatomy
:alt: A sine curve with the amplitude marked as the distance from the axis to the peak, the period marked from peak to peak, and a second dashed curve shifted sideways to illustrate phase.

The anatomy of a sinusoid. The amplitude is measured from the equilibrium line to the peak, not from trough to peak. The period is the time for one complete cycle, and the frequency is its reciprocal. The dashed curve has the same amplitude and the same frequency and differs only in phase, it is the same motion, started at a different moment.
```

- **Amplitude $A$** is the maximum displacement, measured from equilibrium. It is half the peak-to-trough distance, and confusing the two is worth a factor of two in any calculation that follows.
- **Frequency $f$** is the number of complete cycles per second, in hertz. Its reciprocal is the **period** $T = 1/f$, the time one cycle takes.
- **Phase $\phi$** says where in the cycle the motion is at $t = 0$. On its own it means nothing, shifting your clock changes it, but the phase *difference* between two sinusoids is physical and important, and it is the whole subject of [Chapter 3](#ch-superposition).

You will also meet the **angular frequency** $\omega = 2\pi f$, which is measured in radians per second and exists to keep $2\pi$s out of equations. In terms of it, $x(t) = A\sin(\omega t + \phi)$.

:::{margin}
Both conventions are common: $f$ in hertz is what a tuner displays and what a musician names; $\omega$ in radians per second is what appears in the algebra. Convert with $\omega = 2\pi f$ and check units when in doubt.
:::

```{audio} ch01-a440
:label: fig:ch01-a440
:transcript: A steady, plain, slightly thin tone at concert A. It sounds a little like a hearing test, which is exactly what a pure tone is.

A pure tone at 440 Hz: a single sinusoid, and nothing else. Almost nothing in music sounds like this, and that is the point, every musical instrument in this book produces something more complicated, and [Chapter 5](#ch-fourier-and-timbre) explains what it is made of.
```

### Mass on a Spring

The simplest system that obeys Hooke's law exactly is a mass $m$ on a spring of stiffness $k$, and its frequency is

$$
f = \frac{1}{2\pi}\sqrt{\frac{k}{m}}.
$$

```{figure} ../images/ch01-mass-spring.svg
:label: fig:ch01-mass-spring
:alt: A mass on a spring drawn at three moments: displaced to one side with the force arrow pointing back toward equilibrium, at equilibrium with no force and maximum speed, and displaced to the other side with the force again pointing back.

One cycle of simple harmonic motion, in three snapshots. The restoring force is largest where the displacement is largest and the mass is momentarily at rest; it is zero as the mass passes through equilibrium, where the speed is greatest. Force and displacement are always in opposite directions, which is the entire content of $F = -kx$.
```

Two features of that formula are worth more than the formula itself.

**Stiffer means faster; heavier means slower.** Tighten the spring and the frequency rises; hang more mass on it and the frequency falls. Every pitch-changing mechanism in every instrument in this book is a version of one of those two levers. A guitar string is tuned by changing its tension, stiffness, and a bass string is made low by winding metal around it, mass. The vocal folds go up in pitch when their tension rises.

**The frequency does not depend on the amplitude.** Pull the mass twice as far and release it, and it takes exactly as long to come back. This is a peculiar property of the *linear* restoring force, and it is not a general fact about vibrating things. But it is the property that makes music possible at all: a piano string struck gently and struck hard sounds the same note. If frequency depended on amplitude, every instrument would go sharp or flat as it got louder, and no fixed-pitch instrument could exist.

::::{tip} Worked example: tuning by mass and by tension
A mass of $0.20$ kg on a spring oscillates at $2.5$ Hz.

*(a) What is the spring's stiffness?*

Rearranging $f = (1/2\pi)\sqrt{k/m}$ gives $k = m(2\pi f)^2$, so

$$
k = (0.20\ \text{kg})\,[2\pi(2.5\ \text{Hz})]^2 = (0.20)(15.7)^2 = 49\ \text{N/m}.
$$

*(b) What mass would oscillate at exactly half that frequency on the same spring?*

Frequency goes as $1/\sqrt{m}$, so halving $f$ requires multiplying $m$ by four: $0.80$ kg.

*(c) A guitar's low E string is tuned to $82.4$ Hz. Its maker wants a string one octave lower, $41.2$ Hz, of the same length and the same tension. By what factor must its mass per unit length increase?*

The same $1/\sqrt{m}$ scaling applies to a string ([Chapter 3](#ch-superposition) derives it), so halving the frequency requires four times the mass per unit length. Winding wire around a thin core is how this is done in practice; making the core four times as massive by making it thicker would also make it far too stiff to bend over the bridge, which is the subject of §10.1.
::::

### The Pendulum, and the Small-Angle Approximation

A pendulum is the other classic example, and it is instructive precisely because it obeys Hooke's law only approximately. A bob of mass $m$ on a string of length $L$, displaced by an angle $\theta$, feels a restoring force $F = -mg\sin\theta$ along its arc. That is not proportional to $\theta$, but for small angles, $\sin\theta \approx \theta$, and it becomes so. The frequency is then

$$
f = \frac{1}{2\pi}\sqrt{\frac{g}{L}},
$$

which, strikingly, does not contain the mass at all.

The approximation is good to better than $1\%$ out to about $14°$, and it fails slowly rather than suddenly: at $30°$ the real period is about $1.7\%$ longer than the formula predicts, and a pendulum swinging through $90°$ is nearly $18\%$ slow. This is the general behavior of a real vibrating system driven beyond its linear range; keep it in mind when [Chapter 12](#ch-percussion) reaches instruments that are never in it.

```{phet} masses-and-springs
:label: fig:ch01-masses-and-springs-sim

Hang masses on springs of different stiffness and time the oscillations. Two experiments are worth doing deliberately: change the amplitude while keeping the mass and spring fixed, and confirm that the period does not move; then quadruple the mass and confirm that the period exactly doubles.
```

## Energy, Amplitude, and Damping

### Energy Goes as Amplitude Squared

A vibrating system carries energy, and it carries it in two forms that trade back and forth. At the extremes of the motion the mass is momentarily at rest and all the energy is stored in the stretched spring; as it passes through equilibrium the spring is relaxed and all the energy is kinetic. In between, it is some of each. For a system obeying $F = -kx$, the total is

$$
E = \tfrac{1}{2}kA^2,
$$

and the fact to carry forward is the **square**. Doubling the amplitude of a vibration quadruples its energy. A sound wave of twice the pressure amplitude carries four times the energy, and delivers four times the power to your eardrum.

That squaring is why [Chapter 7](#ch-loudness) needs logarithms. The range of sound energies the ear handles is not merely large, it is the *square* of an already large range of pressures, about $10^{12}$ to one, from the quietest audible sound to the threshold of pain. No linear scale is usable across that span, and the decibel exists to tame it.

```{audio} ch01-amplitude-steps
:label: fig:ch01-amplitude-steps
:transcript: One tone, five times, each quieter than the last by a clearly audible but not dramatic step. The last is about a sixteenth the amplitude of the first, and still perfectly audible.

The same 440 Hz tone at five amplitudes, each half the one before. Each halving of amplitude is a factor of four in energy, and a drop of $6$ dB. Notice how *un*dramatic four steps sound: a sixteen-fold reduction in amplitude, a $256$-fold reduction in energy, is not remotely "a sixteenth as loud". Making that observation precise is the business of [Chapter 7](#ch-loudness).
```

### Damped Vibration and the Decay of a Note

An undamped oscillator would ring forever. Real ones do not, because energy leaks away: into friction inside the material, into the mountings, and, usefully, since this is the point of a musical instrument, into the surrounding air as sound.

The result is that the amplitude falls off over time, and for light damping it falls off *exponentially*:

$$
A(t) = A_0 e^{-t/\tau}.
$$

The **decay time** $\tau$ is the time for the amplitude to fall to $1/e$, about $37\%$, of where it started. A large $\tau$ means a long ring; a small $\tau$ means a quick thud.

```{figure} ../images/ch01-damping.svg
:label: fig:ch01-damping
:alt: Three damped sinusoids drawn with their exponential envelopes, decaying at three different rates, from a long slow decay to a very fast one.

Three decay rates at the same frequency and the same starting amplitude. The frequency is barely affected by damping this light, the zero crossings stay where they were, but the length of the note is completely transformed. An instrument's sustain is therefore a design parameter independent of its pitch.
```

Every instrument makes a choice here, and the choice is a trade-off that [Chapter 4](#ch-resonance) makes precise. Energy radiated as sound is energy lost from the vibration, so **a loud instrument is a short-lived one**. A guitar string coupled tightly to a good soundboard is loud and dies quickly; the same string on a solid plank is quiet and rings for a long time. A pianist who wants a longer note lifts the dampers; a pianist who wants a shorter one puts them back.

```{audio} ch01-struck, ch01-sustained
:names: Struck, Sustained
:figure: ../images/ch01-decay-compare.svg
:label: fig:ch01-decay-compare
:transcript: Two notes of the same pitch and the same tone color. The first begins abruptly and fades away like a plucked string; the second grows in, holds steady, and stops.

The same pitch, the same harmonics, the same loudness, and two envelopes. Nothing differs between these but how the amplitude changes with time, and it is enough to make the first sound struck and the second sound bowed or blown. [Chapter 5](#ch-fourier-and-timbre) shows that this is not a minor effect: strip the attack off a recorded note and listeners struggle to name the instrument.
```

### Why Anything Vibrates Sinusoidally At All

Why does simple harmonic motion deserve a chapter to itself, given that almost nothing in music is a mass on a spring?

The answer has three parts, and each is developed later in the book.

**First, everything stable is a spring for small displacements.** That is the Taylor-series argument above. Air in a pipe, a stretched membrane, a steel bar, the fluid in your cochlea: displace any of them slightly and the restoring force is linear in the displacement, so the motion is sinusoidal.

**Second, complicated objects are collections of simple ones.** A guitar string does not have one natural frequency; it has an unlimited number, and each of them behaves exactly like an independent mass on a spring. These are its **normal modes**, and [Chapter 4](#ch-resonance) shows that any motion of any such system, however complicated, is a sum of its modes vibrating simultaneously.

**Third, any periodic sound is a sum of sinusoids.** This is Fourier's theorem, the subject of [Chapter 5](#ch-fourier-and-timbre), and it is the reason a chapter about the simplest possible vibration is the right place to start a book about the most complicated ones. A clarinet's waveform looks nothing like a sine curve. It is nevertheless a sum of sine curves, and once you know which ones, you know why a clarinet sounds like a clarinet.

Simple harmonic motion is not an approximation the book will later outgrow. It is the alphabet.

## Summary

- **Sound is a longitudinal disturbance in a medium**, not a substance in transit. The medium moves back and forth along the direction of travel and stays where it was; only the disturbance goes anywhere. No medium, no sound, light crosses a vacuum and sound does not.
- **A sound wave can be described as displacement or as pressure**, and the two are a quarter of a wavelength out of step. Compressions are pressure maxima and rarefactions are pressure minima. Both microphones and eardrums measure pressure, so the whole of what a listener has to work with is pressure at a point as a function of time.
- **Musical sounds are described by four perceptual attributes**, pitch, loudness, timbre, duration, which correspond roughly to frequency, amplitude, spectrum-and-envelope, and duration. Only the last correspondence is exact, and the exceptions are the subject of [Part III](#ch-the-ear).
- **Periodic waveforms have pitch; non-periodic ones are noise.** Frequency $f$ and period $T$ are reciprocals, $T = 1/f$. Human hearing spans roughly $20$ Hz to $20$ kHz; musical fundamentals occupy only the lower half of it.
- **Any stable system obeys $F = -kx$ for small displacements**, because any smooth potential looks quadratic near its minimum. That is how so many unlike objects come to vibrate in the same way, and why "small amplitude" qualifies nearly every result in this book.
- **Simple harmonic motion is a sinusoid**, $x(t) = A\sin(2\pi f t + \phi)$, described by amplitude, frequency, and phase. For a mass on a spring $f = (1/2\pi)\sqrt{k/m}$: stiffer is faster, heavier is slower, and **the frequency does not depend on the amplitude**, without which no fixed-pitch instrument could exist.
- **Energy goes as the square of the amplitude**, $E = \frac12 kA^2$. The enormous dynamic range this produces is why loudness is measured logarithmically ([Chapter 7](#ch-loudness)).
- **Damping makes amplitude decay exponentially**, $A(t) = A_0e^{-t/\tau}$. Radiating sound is a loss of energy from the vibration, so loudness and sustain trade against each other: a design decision every instrument maker has to make.

## Conceptual Questions

1. An alarm clock ringing inside a bell jar goes silent as the air is pumped out, but the hammer can still be seen striking the bell. Explain what has stopped and what has not.

2. A tuning fork held in the air is quiet; the same fork with its base pressed against a table is loud, and stops ringing sooner. Account for both observations with one explanation.

3. A sound wave is sometimes drawn as a wavy line. Explain what is actually wavy, given that the air does not move up and down at all, and say what quantity the vertical axis of such a drawing represents.

4. At the moment a small parcel of air has been displaced furthest from its rest position, is the pressure there a maximum, a minimum, or atmospheric? Explain your answer without using calculus.

5. A piano string struck hard and struck gently produces the same pitch. Which property of simple harmonic motion guarantees this, and what would music be like if it did not hold?

6. Two guitar strings have the same length and the same tension, but one is twice as massive per unit length. Which sounds the lower note, and by roughly what interval?

7. A pendulum clock keeps good time when its swing is small, but runs slow when the swing is large. Explain which assumption of §1.3 has failed, and in which direction the error goes.

8. Explain, in terms of where the vibrational energy goes, why an electric guitar unplugged is both quieter and longer-sustaining than an acoustic guitar.

## Problems

:::{exercise}
:label: ex-sound-and-shm-1

A tuning fork vibrates at $512$ Hz. (a) What is its period? (b) How many complete cycles does it make in the $2.4$ s it takes to fade to inaudibility?
:::

:::{solution} ex-sound-and-shm-1
:label: sol-sound-and-shm-1
:class: dropdown

(a) The period is the reciprocal of the frequency:

$$
T = \frac{1}{f} = \frac{1}{512\ \text{Hz}} = 1.95\times10^{-3}\ \text{s} = 1.95\ \text{ms}.
$$

(b) The number of cycles is the frequency times the time:

$$
N = ft = (512\ \text{s}^{-1})(2.4\ \text{s}) = 1.2\times10^{3}\ \text{cycles}.
$$

Therefore, the period is $1.95$ ms and the fork completes about $1200$ cycles.
:::

:::{exercise}
:label: ex-sound-and-shm-2

The A above middle C is tuned to $440$ Hz. (a) What is the frequency of the A one octave above it, and one octave below? (b) What is the frequency four octaves above $440$ Hz, and is it audible?
:::

:::{solution} ex-sound-and-shm-2
:label: sol-sound-and-shm-2
:class: dropdown

(a) An octave is a factor of two in frequency. One octave above: $2\times440 = 880$ Hz. One octave below: $440/2 = 220$ Hz.

(b) Four octaves is a factor of $2^4 = 16$:

$$
f = 16 \times 440\ \text{Hz} = 7040\ \text{Hz}.
$$

Therefore, the note is $7040$ Hz, which is well inside the audible range of roughly $20$ Hz to $20$ kHz, though it is above the highest note on a piano ($4186$ Hz).
:::

:::{exercise}
:label: ex-sound-and-shm-3

A mass of $0.35$ kg hangs from a spring of stiffness $k = 84$ N/m. (a) At what frequency does it oscillate? (b) What mass would be needed to halve that frequency?
:::

:::{solution} ex-sound-and-shm-3
:label: sol-sound-and-shm-3
:class: dropdown

(a) Using $f = (1/2\pi)\sqrt{k/m}$:

$$
f = \frac{1}{2\pi}\sqrt{\frac{84\ \text{N/m}}{0.35\ \text{kg}}}
  = \frac{1}{2\pi}\sqrt{240\ \text{s}^{-2}}
  = \frac{15.5}{6.283} = 2.47\ \text{Hz}.
$$

(b) Since $f \propto 1/\sqrt{m}$, halving the frequency requires quadrupling the mass:

$$
m = 4 \times 0.35\ \text{kg} = 1.4\ \text{kg}.
$$

Therefore, the frequency is $2.47$ Hz, and $1.4$ kg would halve it.
:::

:::{exercise}
:label: ex-sound-and-shm-4

A simple harmonic oscillator has amplitude $A = 3.0$ mm and frequency $f = 250$ Hz. (a) Write its displacement as a function of time, taking $x = 0$ at $t = 0$ and moving in the positive direction. (b) What is its maximum speed?
:::

:::{solution} ex-sound-and-shm-4
:label: sol-sound-and-shm-4
:class: dropdown

(a) Starting at $x = 0$ and moving positive means a sine with zero phase:

$$
x(t) = (3.0\times10^{-3}\ \text{m})\sin\bigl[2\pi(250\ \text{Hz})\,t\bigr]
     = (3.0\ \text{mm})\sin\bigl[(1571\ \text{s}^{-1})\,t\bigr].
$$

(b) For simple harmonic motion the maximum speed is $v_{\max} = \omega A = 2\pi f A$:

$$
v_{\max} = 2\pi(250\ \text{Hz})(3.0\times10^{-3}\ \text{m}) = 4.7\ \text{m/s}.
$$

Therefore, the displacement is $x(t) = (3.0\ \text{mm})\sin[(1571\ \text{s}^{-1})t]$ and the maximum speed is $4.7$ m/s, which is reached as it passes through equilibrium, where the restoring force is zero.
:::

:::{exercise}
:label: ex-sound-and-shm-5

The threshold of hearing corresponds to a pressure amplitude of about $2.0\times10^{-5}$ Pa, and the threshold of pain to about $20$ Pa. (a) What is the ratio of these pressures? (b) What is the ratio of the *energies* they carry?
:::

:::{solution} ex-sound-and-shm-5
:label: sol-sound-and-shm-5
:class: dropdown

(a) The pressure ratio is

$$
\frac{20\ \text{Pa}}{2.0\times10^{-5}\ \text{Pa}} = 1.0\times10^{6}.
$$

(b) Energy goes as the square of amplitude, so

$$
\left(1.0\times10^{6}\right)^2 = 1.0\times10^{12}.
$$

Therefore, the ear handles a millionfold range of pressures, which is a million-million-fold range of energies. A linear scale covering this span is unusable, which is the reason for the decibel ([Chapter 7](#ch-loudness)).
:::

:::{exercise}
:label: ex-sound-and-shm-6

A guitar string's vibration decays with $\tau = 1.8$ s. (a) What fraction of its initial amplitude remains after $3.0$ s? (b) After how long has the amplitude fallen to $10\%$ of its initial value? (c) What fraction of the initial *energy* remains at that moment?
:::

:::{solution} ex-sound-and-shm-6
:label: sol-sound-and-shm-6
:class: dropdown

(a) Using $A(t) = A_0 e^{-t/\tau}$:

$$
\frac{A}{A_0} = e^{-3.0/1.8} = e^{-1.667} = 0.189.
$$

(b) Setting $A/A_0 = 0.10$ and solving:

$$
e^{-t/\tau} = 0.10 \;\Rightarrow\; \frac{t}{\tau} = \ln 10 = 2.303
\;\Rightarrow\; t = 2.303 \times 1.8\ \text{s} = 4.1\ \text{s}.
$$

(c) Energy goes as amplitude squared, so at $10\%$ amplitude the energy is $(0.10)^2 = 1.0\%$ of its initial value.

Therefore, about $19\%$ of the amplitude remains after $3.0$ s, $10\%$ remains after $4.1$ s, and at that point only one part in a hundred of the energy is left, yet the note is still clearly audible, which is another demonstration of the ear's range.
:::

:::{exercise}
:label: ex-sound-and-shm-7

Two identical springs, each of stiffness $k$, support the same mass $m$, first one at a time, then both side by side in parallel. By what factor does the oscillation frequency change when the second spring is added?
:::

:::{solution} ex-sound-and-shm-7
:label: sol-sound-and-shm-7
:class: dropdown

Two springs in parallel both stretch by the same displacement $x$, and each contributes a restoring force $kx$, so the total force is $2kx$. The effective stiffness is therefore $k_{\text{eff}} = 2k$.

Since $f \propto \sqrt{k}$,

$$
\frac{f_2}{f_1} = \sqrt{\frac{2k}{k}} = \sqrt{2} = 1.41.
$$

Therefore, the frequency rises by a factor of $\sqrt2$, about $41\%$, which, as [Chapter 9](#ch-scales-and-tuning) will point out, is almost exactly a musical tritone, the interval of six equal-tempered semitones.
:::

:::{exercise}
:label: ex-sound-and-shm-8

A pendulum is to be built with a period of exactly $1.00$ s. (a) How long must it be? Take $g = 9.81$ m/s². (b) The same pendulum is taken to the Moon, where $g = 1.62$ m/s². What is its period there?
:::

:::{solution} ex-sound-and-shm-8
:label: sol-sound-and-shm-8
:class: dropdown

(a) From $f = (1/2\pi)\sqrt{g/L}$ and $T = 1/f$, the period is $T = 2\pi\sqrt{L/g}$. Rearranging:

$$
L = g\left(\frac{T}{2\pi}\right)^2 = (9.81\ \text{m/s}^2)\left(\frac{1.00\ \text{s}}{6.283}\right)^2 = 0.248\ \text{m}.
$$

(b) The period goes as $1/\sqrt{g}$:

$$
T_{\text{Moon}} = T_{\text{Earth}}\sqrt{\frac{g_{\text{Earth}}}{g_{\text{Moon}}}}
= (1.00\ \text{s})\sqrt{\frac{9.81}{1.62}} = 2.46\ \text{s}.
$$

Therefore, the pendulum is $24.8$ cm long and swings with a period of $2.46$ s on the Moon. Note that the mass of the bob never entered either calculation.
:::

:::{exercise}
:label: ex-sound-and-shm-9

A loudspeaker cone moves in simple harmonic motion at $80$ Hz with an amplitude of $1.5$ mm. (a) What is the maximum speed of the cone? (b) What is its maximum acceleration, in units of $g$?
:::

:::{solution} ex-sound-and-shm-9
:label: sol-sound-and-shm-9
:class: dropdown

First, $\omega = 2\pi f = 2\pi(80\ \text{Hz}) = 503\ \text{s}^{-1}$.

(a) The maximum speed is

$$
v_{\max} = \omega A = (503\ \text{s}^{-1})(1.5\times10^{-3}\ \text{m}) = 0.75\ \text{m/s}.
$$

(b) For simple harmonic motion the maximum acceleration is $a_{\max} = \omega^2 A$:

$$
a_{\max} = (503\ \text{s}^{-1})^2(1.5\times10^{-3}\ \text{m}) = 380\ \text{m/s}^2,
$$

which is $380/9.81 = 39$ times $g$.

Therefore, the cone reaches $0.75$ m/s and $39g$. Accelerations of this order are routine in loudspeakers, and they are the reason cones are made as light and as stiff as materials allow ([Chapter 15](#ch-electronic-and-recorded-sound)).
:::

:::{exercise}
:label: ex-sound-and-shm-10

A note played on a violin has a waveform that repeats every $2.27$ ms. (a) What is its frequency? (b) Which note is it, given that A440 lies $440$ Hz and each semitone is a factor of $2^{1/12}$? (Count semitones from A440.)
:::

:::{solution} ex-sound-and-shm-10
:label: sol-sound-and-shm-10
:class: dropdown

(a) The frequency is the reciprocal of the period:

$$
f = \frac{1}{2.27\times10^{-3}\ \text{s}} = 441\ \text{Hz}.
$$

(b) The ratio to A440 is $441/440 = 1.0023$. One semitone is $2^{1/12} = 1.0595$, so the number of semitones is

$$
n = \frac{\ln 1.0023}{\ln 1.0595} = \frac{0.00227}{0.0578} = 0.039\ \text{semitones}.
$$

Therefore, the note is A440, sharp by about four hundredths of a semitone, four **cents**, in the units of [Chapter 9](#ch-scales-and-tuning). That is far too small to hear as mistuning, and is well within the precision with which a violinist places a finger.
:::

:::{exercise}
:label: ex-sound-and-shm-11

Show that for a simple harmonic oscillator the speed at displacement $x$ is

$$
v = \omega\sqrt{A^2 - x^2},
$$

and use it to find at what fraction of the amplitude the kinetic and potential energies are equal.
:::

:::{solution} ex-sound-and-shm-11
:label: sol-sound-and-shm-11
:class: dropdown

Energy is conserved, and the total is the potential energy at the turning point:

$$
\tfrac12 m v^2 + \tfrac12 k x^2 = \tfrac12 k A^2.
$$

Solving for $v$:

$$
v^2 = \frac{k}{m}\left(A^2 - x^2\right) = \omega^2\left(A^2 - x^2\right),
$$

using $\omega^2 = k/m$. Taking the square root gives $v = \omega\sqrt{A^2 - x^2}$, which correctly gives $v = \omega A$ at $x = 0$ and $v = 0$ at $x = \pm A$.

The two energies are equal when each is half the total:

$$
\tfrac12 k x^2 = \tfrac12\left(\tfrac12 k A^2\right)
\;\Rightarrow\; x^2 = \tfrac12 A^2
\;\Rightarrow\; x = \frac{A}{\sqrt2} = 0.707A.
$$

Therefore, the energy is evenly split at about $71\%$ of the amplitude, not at half the amplitude, which is the natural but wrong guess.
:::

:::{exercise}
:label: ex-sound-and-shm-12

A piano string and a wine glass are both struck and left to ring. The string's amplitude falls to half in $0.9$ s; the glass's falls to half in $4.5$ s. (a) Find $\tau$ for each. (b) Which radiates sound more efficiently, and how do you know? (c) Estimate how long each remains audible if a note becomes inaudible once its amplitude has fallen by a factor of $10^{3}$.
:::

:::{solution} ex-sound-and-shm-12
:label: sol-sound-and-shm-12
:class: dropdown

(a) Setting $A/A_0 = \tfrac12 = e^{-t_{1/2}/\tau}$ gives $\tau = t_{1/2}/\ln 2$:

$$
\tau_{\text{string}} = \frac{0.9\ \text{s}}{0.693} = 1.3\ \text{s},
\qquad
\tau_{\text{glass}} = \frac{4.5\ \text{s}}{0.693} = 6.5\ \text{s}.
$$

(b) The string. A short decay time means energy is leaving the vibration quickly, and for an instrument designed to be heard, the dominant loss channel is radiation as sound. The glass holds its energy, which is why a wine glass is loud only when it is rubbed continuously, and why the string, losing its energy fast, is loud straight away.

(c) A factor of $10^3$ takes $t = \tau\ln(10^3) = 6.91\tau$:

$$
t_{\text{string}} = 6.91 \times 1.3\ \text{s} = 9.0\ \text{s},
\qquad
t_{\text{glass}} = 6.91 \times 6.5\ \text{s} = 45\ \text{s}.
$$

Therefore, the string rings for about $9$ s and the glass for about $45$ s. The comparison is the trade-off of §1.4 in numbers: the glass sustains five times longer because it is five times worse at the job of turning vibration into sound.
:::

:::{exercise}
:label: ex-sound-and-shm-13

A student claims that because sound is a pressure wave, a loudspeaker must push a "packet of air" from the cone to the listener's ear. (a) Estimate how long a packet of air would take to travel $5$ m if it moved at the maximum cone speed of $0.75$ m/s found in [](#ex-sound-and-shm-9). (b) Sound actually covers $5$ m in about $15$ ms. Use the comparison to explain what is wrong with the student's picture.
:::

:::{solution} ex-sound-and-shm-13
:label: sol-sound-and-shm-13
:class: dropdown

(a) At a steady $0.75$ m/s:

$$
t = \frac{5\ \text{m}}{0.75\ \text{m/s}} = 6.7\ \text{s}.
$$

(b) The actual travel time is about $15$ ms, some $440$ times shorter. Worse, the cone's motion is *oscillatory*, it moves out and back, so no parcel of air makes net progress at all; each one jiggles about a fixed position with an amplitude of a fraction of a millimeter.

Therefore, the student's picture is wrong in both magnitude and kind. What travels from the loudspeaker to the ear is not air but a *disturbance* in the air, and its speed is set by how quickly molecular collisions pass the squeeze along: a property of the medium, not of the source ([Chapter 2](#ch-wave-motion)).
:::

:::{exercise}
:label: ex-sound-and-shm-14

A mass–spring system is set oscillating with amplitude $A$. A second, identical system is set oscillating with amplitude $3A$. (a) Compare their frequencies. (b) Compare their maximum speeds. (c) Compare their energies. (d) Which comparison explains why a piano stays in tune as the pianist plays louder?
:::

:::{solution} ex-sound-and-shm-14
:label: sol-sound-and-shm-14
:class: dropdown

(a) Identical, since $f = (1/2\pi)\sqrt{k/m}$ contains no amplitude.

(b) $v_{\max} = \omega A$, so the second is three times faster.

(c) $E = \frac12 kA^2$, so the second has $3^2 = 9$ times the energy.

(d) Part (a). The independence of frequency from amplitude is exactly what guarantees that a string struck harder sounds the same note, only louder. Were it otherwise, the instrument would go out of tune with every change of dynamic, and fixed-pitch instruments could not exist.
:::
