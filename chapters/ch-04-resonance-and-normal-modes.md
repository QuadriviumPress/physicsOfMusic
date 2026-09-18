---
title: "Resonance and Normal Modes"
short_title: "Chapter 4. Resonance and Normal Modes"
label: ch-resonance
numbering:
  enumerator: "4.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 4.1, 4.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-04-resonance-and-normal-modes.pdf
    chapter: 4
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish free vibration at a natural frequency from forced vibration at a driving frequency.
- Sketch the response of a driven oscillator against driving frequency, and identify the resonance peak, its height, and its width.
- Explain why a system driven at resonance builds up a large amplitude, in terms of energy delivered in step with the motion.
- Relate damping to the sharpness of a resonance, define the quality factor $Q$, and calculate it from the bandwidth of a measured response curve.
- Explain the trade-off a Q value represents for an instrument: a sharp resonance is loud and selective, a broad one is even and responsive.
- Define a normal mode, and explain why a system with $N$ degrees of freedom has $N$ of them.
- Explain how an arbitrary motion of a vibrating system can be written as a combination of its normal modes, and why the modes are the natural description.
- Identify the resonator in a guitar, a violin, a trumpet, and the human voice, and describe what each contributes to the sound.

### Introduction

```{figure} ../images/open/ch04-guitar-strings-vibrating.jpg
:label: fig:ch04-open-guitar
:alt: An extreme close-up of six guitar strings caught mid-vibration, each blurred into a wide band whose width traces the string's actual oscillation envelope.

A guitar is a compact collection of resonators: strings, plates, an enclosed air cavity, and the room beyond them. Here the strings themselves are doing it, each blurred band the shape of one string's vibration. Matt Stetzel, CC BY 4.0.
```

[Chapter 3](#ch-superposition) established that a string fixed at both ends can only vibrate at certain frequencies. That is a statement about what the string will do if left alone. This chapter is about what happens when it is *not* left alone, when something drives it.

The answer is the single most useful idea in instrument design. Drive a system at one of its natural frequencies and it responds enormously; drive it anywhere else and it barely responds at all. That selectivity is **resonance**, and every instrument in this book depends on it twice over: once to choose which frequency will sound, and again to get that frequency out into the room loudly enough to hear.

Two ideas run through the chapter, and they turn out to be the same idea seen from two sides.

The first is the **trade-off**. A sharply tuned resonator responds hugely, but only to a narrow band of frequencies, and it rings for a long time after the driving stops. A broadly tuned one responds modestly, to almost anything, and stops as soon as the driving does. An instrument maker must choose, and different instruments choose differently.

The second is the **normal mode**. A real object does not have one natural frequency; it has many, each with its own characteristic shape. The remarkable fact, and the reason [Chapter 5](#ch-fourier-and-timbre) can exist, is that any motion whatsoever of such an object is a sum of its modes.

## Free Vibration and Natural Frequency

### Natural Frequencies of Real Objects

Displace something and let go, and it vibrates at its **natural frequency**. A mass on a spring does it at $(1/2\pi)\sqrt{k/m}$; a string fixed at both ends does it at $(1/2L)\sqrt{T/\mu}$; a wine glass, a tuning fork, a wooden bar, a column of air, a bridge, and a building all do it at frequencies set by their own stiffness and mass.

This is **free vibration**: no one is driving it, the amplitude decays as [Chapter 1](#ch-sound-and-shm) described, and the frequency is whatever the object's construction dictates.

Notice that damping barely changes the frequency. A lightly damped oscillator rings at almost exactly the frequency it would have had with no damping at all: the correction is of order $1/Q^2$, and for any $Q$ above about 5 it is negligible. A guitar string therefore sounds the same note whether you let it ring or mute it quickly, and the formulas of [Chapter 3](#ch-superposition), which ignored damping entirely, were safe to write down.

### Why Every Object Has More Than One

A mass on a spring has exactly one natural frequency, because it has exactly one way to move: the mass goes left or it goes right.

A string is different. It can bow out in one arch, or in two, or in three, and each of those shapes has its own frequency. The number of natural frequencies is the number of independent ways the object can move, its number of **degrees of freedom**, and for anything continuous, that number is unlimited.

This matters for a reason that will not be obvious yet: it means the word "resonance" is almost always plural. A guitar body does not have *a* resonance; it has dozens, and the shape of the resulting response curve is what a luthier is actually adjusting when they thin a brace by a fraction of a millimeter.

## Driven Oscillation and Resonance

### Driving an Oscillator Off and On Resonance

Now apply a force that oscillates at a frequency $f$ of your choosing, and ask how large a response you get.

After any initial transient dies away, the system settles into oscillating **at the driving frequency**, not at its own. That is worth stating clearly because it is counterintuitive: the driven system abandons its natural frequency and does what it is told. What its natural frequency controls is not the frequency of the response but its **size**.

- Drive it very slowly, far below $f_0$: the mass simply follows the force. The response is small and in step with the drive.
- Drive it at $f_0$: each push arrives exactly when it helps, cycle after cycle, and the amplitude builds far beyond anything the force could achieve on its own.
- Drive it far above $f_0$: the mass cannot keep up. It barely moves, and what motion there is lags half a cycle behind.

```{animation} ch04-response-curves
:label: fig:ch04-response-curves
:alt: Left, a constant-strength oscillating force drives a mass on a spring; the mass moves much farther as the drive approaches resonance and its motion changes phase. Right, three amplitude-response curves peak at resonance above phase-lag curves that pass through ninety degrees there.

The response of a driven oscillator as the drive frequency sweeps back and forth through resonance. **Left**: a constant-strength force drives the $Q=5$ oscillator shown by the green curve. Its motion grows dramatically near $f=f_0$, and its timing shifts from following the force to opposing it. **Right, top**: the amplitude for three amounts of damping. **Right, bottom**: the corresponding phase lag. At resonance the response lags the drive by exactly $90°$, whatever the damping, which is the precise statement of "pushing at the right moment".
```

```{video} https://www.youtube.com/watch?v=PIUdZaoZmx8
:video-title: Resonance: Breaking a Wine Glass
:label: fig:ch04-wine-glass-resonance-video
:alt: A wine glass vibrates beside a loudspeaker during a resonance demonstration.

In this University of British Columbia outreach demonstration, a loudspeaker drives a wine glass at its natural frequency. High-speed footage shows the resonant motion growing until the glass fails: a vivid example of a small periodic force transferring energy efficiently when its frequency is correctly matched.
```

### The Response Curve

The curve in that figure is the object an experimenter measures; reading it is a skill of its own.

Its **peak** is at the natural frequency. Its **height** says how much amplification the resonance provides. Its **width** says how fussy the resonator is about frequency. Height and width are not independent: a taller peak is always a narrower one, for reasons the next section makes precise.

```{audio} ch04-resonance-sweep
:label: fig:ch04-resonance-sweep
:transcript: A tone gliding slowly upward. For most of the sweep it is barely audible; as it passes about 330 Hz it swells dramatically, then dies away again as the glide continues.

A steady drive of constant strength, swept slowly from $120$ Hz to $900$ Hz past a resonance at $330$ Hz. The *drive* does not change in strength at any point. Everything you hear is the resonator's selectivity.
```

```{openlyceum} Resonance
:screens: 1
:label: fig:ch04-resonance-sim
:sim-name: Resonance — single oscillator
:alt: A driven mass on a spring beside controls for mass, spring constant, damping, driving frequency, and driving amplitude.

Set the damping low and sweep the driving frequency slowly through the natural frequency. The mass always moves at the *driving* frequency; it is the amplitude that changes, rising sharply at resonance. Increase the damping and repeat: the peak becomes lower and broader. Then change the mass or spring constant, predict which way the resonance will move, and test your prediction.
```

:::{note}
The most famous demonstration of resonance, a singer shattering a wine glass, is real but demanding. It needs the singer to hit the glass's natural frequency within a few hertz, to hold it, and to be loud enough that a $Q$ of several hundred multiplies the amplitude past the glass's breaking strain. Amplification is usually involved. The physics is exactly the curve above; what makes it hard is the narrowness of the peak.
:::

### Phase: Pushing at the Right Moment

Why does driving at $f_0$ work so well? The answer is about timing, and it is better than the usual "the pushes add up".

To feed energy into an oscillator you must push in the direction it is already moving, push in phase with the **velocity**, not with the displacement. For a sinusoid, velocity leads displacement by a quarter cycle. So the drive must lead the displacement by $90°$, which is exactly the phase relationship the bottom panel of the figure shows at resonance.

Off resonance, the drive and the motion drift in and out of step, so some pushes add energy and others take it away, and the amplitude never builds. At resonance the relationship is locked, and every push helps.

This is also why a child on a swing must push at the right moment rather than merely often, and why pushing twice as often does not work at all.

```{video} https://www.youtube.com/watch?v=aCocQa2Bcuc
:video-title: Tuning Forks
:label: fig:ch04-tuning-forks-video
:alt: Two tuning forks mounted on resonant boxes demonstrate sympathetic vibration.

MIT's Physics Instructional Resources Lab demonstrates natural frequency and sympathetic vibration with matched tuning forks. One resonator responds strongly because the other drives it at the frequency it already prefers.
```

## Damping, Bandwidth, and the Quality Factor

### Damping Sets the Height and the Width

What stops the amplitude at resonance from growing without limit is damping. Energy is fed in by the drive and lost to friction and radiation, and the amplitude settles where the two balance.

So a lightly damped system reaches a very large amplitude before it balances: a tall peak. It is also fussy: because it loses so little energy per cycle, it takes many cycles to build up, and during those cycles the drive must stay in step, which it will only do if the frequency is very close to $f_0$. Tall and narrow go together.

A heavily damped system balances quickly at a modest amplitude and is not fussy, because it never needed many consecutive well-timed pushes. Short and broad go together.

### Defining $Q$

The **quality factor** $Q$ measures this, and it can be defined in three equivalent ways:

$$
Q = \frac{f_0}{\Delta f}
= 2\pi\,\frac{\text{energy stored}}{\text{energy lost per cycle}}
= \pi f_0 \tau,
$$

where $\Delta f$ is the width of the response peak between the points at which the amplitude has fallen to $1/\sqrt2$ of its maximum, and $\tau$ is the free-decay time of [Chapter 1](#ch-sound-and-shm).

```{figure} ../images/ch04-q-and-bandwidth.svg
:label: fig:ch04-q-and-bandwidth
:alt: A single resonance peak with a dashed horizontal line at 0.707 of the peak height, two marked crossing points, and a double-headed arrow between them labeled bandwidth.

How $Q$ is measured. Find the peak, drop to $0.707$ of its height, which is half the *power*, since power goes as amplitude squared, and measure the width between the two crossings. The quality factor is the peak frequency divided by that width.
```

The third definition, $Q = \pi f_0\tau$, is the one that connects this chapter to the last. It says that **a narrow resonance and a long ring are the same fact**, measured two different ways. Something that takes a long time to stop is something that is fussy about what starts it.

### The Shape of the Response Curve

$Q$ summarizes the response curve with a single number, its ratio of peak frequency to width. The curve itself, amplitude against driving frequency, has a definite shape, and it is worth writing down, because it is what a real measurement produces and what the rest of the book quietly assumes.

Write the driving frequency as a ratio to the natural frequency, $r = f/f_0$, so $r=1$ is exactly on resonance. The steady-state amplitude, relative to how far the same force would push the system if applied very slowly ($r \to 0$), is

$$
\frac{A}{A_{\text{static}}} = \frac{1}{\sqrt{(1-r^2)^2 + (r/Q)^2}}.
$$

Three checks confirm this is the curve already described in words. Far below resonance ($r \ll 1$), both terms under the root vanish and $A/A_{\text{static}} \to 1$: the mass simply follows the force, as §4.2 said. Exactly on resonance ($r=1$), the first term vanishes and only the damping term survives, leaving $A/A_{\text{static}} = Q$: the peak height is nothing but $Q$ itself, restated as a formula. Far above resonance ($r \gg 1$), the $(1-r^2)^2$ term dominates and the response falls as $1/r^2$: the mass cannot keep up, and doubling the driving frequency above resonance cuts the response to a quarter.

:::{dropdown} Where the response formula comes from
The equation of motion for a mass $m$ on a spring $k$ with damping constant $b$, driven by a force $F_0\cos(2\pi f t)$, is

$$
m\ddot{x} + b\dot{x} + kx = F_0\cos(2\pi f t).
$$

After the initial transient dies away, the system settles into oscillating at the driving frequency, $x(t) = A\cos(2\pi f t - \phi)$, for some amplitude $A$ and phase lag $\phi$. Substituting this trial solution and collecting the sine and cosine parts separately gives two equations, which combine to

$$
A = \frac{F_0}{\sqrt{(k - m\omega^2)^2 + (b\omega)^2}}, \qquad \omega = 2\pi f.
$$

The static response, at $\omega \to 0$, is just $A_{\text{static}} = F_0/k$. Dividing the general expression by this, and writing everything in terms of $r = f/f_0 = \omega/\omega_0$ and $Q = \sqrt{mk}/b$ (which is equivalent to the definitions already given), reduces the ratio to the compact form quoted above. None of the algebra changes the physics already argued from the shape of the curve; it only makes the peak height, the low- and high-frequency limits, and the $1/r^2$ falloff exact rather than qualitative.
:::

```{audio} ch04-high-q, ch04-low-q
:names: Q = 120, Q = 6
:figure: ../images/ch04-q-comparison.svg
:label: fig:ch04-q-comparison
:transcript: Two struck sounds at the same pitch. The first rings on clearly for a second or more, like a struck glass; the second is a dull thud that is over almost at once.

The same brief tap, through two resonators tuned to the same frequency and differing only in damping. The left panel of the figure shows what you hear; the right panel shows the response curves of the same two resonators when driven instead. A long ring and a narrow peak are two views of one property.
```

::::{tip} Worked example: $Q$ from a measurement
*A guitar body's main air resonance is measured by driving it and recording the response. The peak is at $102$ Hz, and the response falls to $0.707$ of its peak at $94$ Hz and $112$ Hz. Find $Q$ and the time the resonance would ring for.*

The bandwidth is $\Delta f = 112 - 94 = 18$ Hz, so

$$
Q = \frac{f_0}{\Delta f} = \frac{102\ \text{Hz}}{18\ \text{Hz}} = 5.7.
$$

The decay time follows from $Q = \pi f_0\tau$:

$$
\tau = \frac{Q}{\pi f_0} = \frac{5.7}{\pi(102\ \text{Hz})} = 0.018\ \text{s}.
$$

That is a very low $Q$ and a very short ring, under two hundredths of a second. It is exactly what a guitar needs: the body must respond to whatever note is played, not impose a note of its own, and it must follow the player's rhythm rather than smearing it.
::::

### The Instrument Maker's Trade-off

Now the trade-off can be stated properly, and it is the central design tension in acoustic instruments.

Energy radiated as sound is energy lost from the vibration, and energy lost from the vibration lowers $Q$. So:

$$
\text{loud} \;\Longleftrightarrow\; \text{low } Q \;\Longleftrightarrow\; \text{short ring and broad response.}
$$

| | High $Q$ | Low $Q$ |
|---|---|---|
| Response | Huge, but only very near $f_0$ | Modest, over a wide band |
| Ring | Long | Short |
| Loudness | Quiet | Loud |
| Examples | Tuning fork, wine glass, bell | Guitar body, violin body, drum head |

A tuning fork has a $Q$ of several thousand: it is a superb frequency standard and an almost useless loudspeaker, so it must be pressed against a table to be heard. A guitar body has a $Q$ of around five: a poor frequency standard and an excellent radiator.

The requirement for a *resonator* in an instrument is therefore almost the opposite of the requirement for the *vibrator*. The string should have high $Q$, it holds the pitch and sustains the note. The body should have low $Q$, it should amplify everything the string offers, equally, and get it into the room. [Chapter 10](#ch-string-instruments) shows how the bridge mediates between the two.

## Normal Modes

### Two Masses, Two Modes

Move from one mass to two, coupled by a spring between them, and something new appears.

```{animation} ch04-two-mass-modes
:label: fig:ch04-two-mass-modes
:alt: Two panels each showing two masses between walls, connected by three springs. In the upper panel both masses move the same way; in the lower panel they move in opposite directions.

The two normal modes of a two-mass system. In the **in-phase** mode the masses move together and the connecting spring is never stretched, so it contributes no restoring force and the frequency is lower. In the **out-of-phase** mode they move oppositely, the connecting spring is stretched hardest, and the frequency is higher.
```

A **normal mode** is a pattern of motion in which every part of the system oscillates at the *same* frequency with a *fixed* relative amplitude and phase. Set a normal mode going and it persists, keeping its shape, exactly like a single mass on a single spring.

Two masses give two modes. The general rule is that a system with $N$ degrees of freedom has exactly $N$ normal modes, no more, and no fewer.

Start such a system in some arbitrary way, and it will *not* keep its shape: the motion looks complicated and never quite repeats. That is because you have excited both modes at once, and they are running at different frequencies.

### Many Masses, Many Modes

Add masses and you add modes. A string is the limit of this process: infinitely many infinitesimal masses, and therefore infinitely many modes, which is exactly the family of standing waves [Chapter 3](#ch-superposition) found.

The modes of a string are special in one respect, and the specialness is the reason music exists. Their frequencies are $f_n = nf_1$: exact whole-number multiples. Nothing guarantees this in general. The modes of a *drumhead* are in the ratios $1: 1.59: 2.14: 2.30: \ldots$, and the modes of a *bar* are in the ratios $1: 2.76: 5.40: \ldots$: the reason [Chapter 12](#ch-percussion) is a chapter about instruments with no definite pitch.

### Any Motion Is a Sum of Modes

Here is the central result of the chapter.

**Any motion of the system, however complicated, can be written as a sum of its normal modes**, each with its own amplitude and phase. The modes form a complete set. Nothing the system can do lies outside them.

This transforms the problem of a plucked string from something apparently intractable, a triangle of string, released from rest, into bookkeeping. Decompose the initial shape into modes, let each mode oscillate at its own frequency, add them back up.

```{figure} ../images/ch04-mode-superposition.svg
:label: fig:ch04-mode-superposition
:alt: Left, a dashed triangular pluck shape with successive approximations from one, two, and eight modes converging on it. Right, a stem plot of mode amplitudes for a pluck at one fifth of the length, with the fifth mode marked as absent.

A string plucked one-fifth of the way along. **Left**: the triangular shape, rebuilt from its modes, one mode is a poor fit, eight are very nearly exact. **Right**: how much of each mode the pluck contains. The fifth mode is entirely absent, because the pluck point is a node of it: you cannot excite a mode by pulling on a place that mode does not move.
```

That missing fifth mode is not a curiosity; it is a technique. Guitarists pluck near the bridge for a bright sound and over the soundhole for a mellow one, and what they are doing is choosing which modes to leave out. [Chapter 10](#ch-string-instruments) makes the rule explicit: **plucking at $L/n$ silences the $n$th harmonic and every multiple of it.**

:::{dropdown} Finding the mode amplitudes: Fourier's method in advance
Decomposing the pluck is a calculation, and [Chapter 5](#ch-fourier-and-timbre) is about to do the same thing to sound.

The modes of a string fixed at both ends are $\sin(n\pi x/L)$. The claim is that any initial shape $y(x)$ satisfying $y(0) = y(L) = 0$ can be written

$$
y(x) = \sum_{n=1}^{\infty} c_n \sin\!\left(\frac{n\pi x}{L}\right).
$$

To find a particular $c_n$, use the fact that the modes are **orthogonal**:

$$
\int_0^L \sin\!\left(\frac{n\pi x}{L}\right)\sin\!\left(\frac{m\pi x}{L}\right)\mathrm{d}x =
\begin{cases} L/2 & n = m\\ 0 & n \ne m.\end{cases}
$$

Multiply both sides of the expansion by $\sin(m\pi x/L)$ and integrate over the string. Every term on the right vanishes except the one with $n = m$, leaving

$$
c_m = \frac{2}{L}\int_0^L y(x)\,\sin\!\left(\frac{m\pi x}{L}\right)\mathrm{d}x .
$$

For a string plucked to a height $h$ at a point $a$ along its length, this integral evaluates to

$$
c_n = \frac{2h L^2}{\pi^2 n^2\,a(L-a)}\,\sin\!\left(\frac{n\pi a}{L}\right).
$$

Two things fall out immediately. The $1/n^2$ makes the high modes weak, so a plucked string is not harsh. And the $\sin(n\pi a/L)$ vanishes whenever $a = L/n$: the missing-mode rule, now derived rather than asserted.
:::

```{phet} normal-modes
:label: fig:ch04-normal-modes-sim
:placeholder: /images/phet/normal-modes-600.png

A chain of masses whose number you can change. Excite one mode at a time and watch it hold its shape; then excite two at once and watch the motion stop looking like anything in particular. Note that $N$ masses always give exactly $N$ modes.
```

## Resonators in Musical Instruments

### The Helmholtz Resonator

The simplest acoustic resonator is a cavity with a narrow opening: a bottle. Blow across the top and it sounds one note, and only one.

The mechanism is a mass on a spring, made entirely of air. The plug of air in the neck is the mass. The much larger body of air in the cavity is the spring: push the plug in and you compress the cavity, which pushes back. Its frequency is

$$
f_0 = \frac{v}{2\pi}\sqrt{\frac{A}{V L_{\text{eff}}}},
$$

where $A$ is the neck's cross-sectional area, $L_{\text{eff}}$ its effective length, and $V$ the cavity volume.

```{figure} ../images/ch04-helmholtz.svg
:label: fig:ch04-helmholtz
:alt: Left, a schematic bottle with the plug of air in the neck marked as the mass and the air in the cavity marked as the spring. Right, resonant frequency against cavity volume for a fixed neck, falling as one over the square root of volume, with a beer bottle and a wine bottle marked.

The Helmholtz resonator. Unlike a pipe, it has essentially **one** resonance, not a harmonic series, because there is no length along which standing waves can fit, only a single mass bouncing on a single spring. Filling the bottle with water reduces $V$ and raises the pitch, in inverse proportion to the square root of what is left.
```

A guitar body is a Helmholtz resonator whose neck is the soundhole, and its air resonance, around $100$ Hz on a typical steel-string, is deliberately placed near the bottom of the instrument's range, where the top plate alone radiates poorly. The same trick appears as a bass-reflex port in a loudspeaker cabinet ([Chapter 15](#ch-electronic-and-recorded-sound)).

### Bodies, Bores, and Cavities

Every acoustic instrument contains at least one resonator. The list below names which is which before [Part V](#ch-string-instruments) takes them one at a time.

| Instrument | The vibrator | The resonator |
|---|---|---|
| Guitar, violin, piano | The string | The body, the soundboard, and the air inside |
| Flute, clarinet, trumpet | The air jet, reed, or lips | The air column in the bore |
| Timpani | The membrane | The kettle of air beneath it |
| Voice | The vocal folds | The vocal tract |

The wind instruments are the odd family out, and the difference is fundamental. In a string instrument the resonator merely *responds* to the vibrator, which sets the pitch on its own. In a wind instrument the resonator **controls** the vibrator: the air column feeds back on the reed or the lips and tells them what frequency to oscillate at. That feedback is why a clarinetist can play a scale with one reed, and why [Chapter 11](#ch-wind-instruments) needs a different kind of argument from [Chapter 10](#ch-string-instruments).

### Resonance as Amplifier and as Filter

A final framing, which will be used repeatedly.

A resonator does not create energy. It is not an amplifier in the electrical sense, nothing is being added. What it does is provide a much better path for energy to leave the vibrator and enter the air, by presenting a large radiating surface where there was a thin string. The sound is louder and the note is shorter, and the total energy is unchanged.

A resonator is also a **filter**. It responds strongly to the frequencies near its peaks and weakly to the rest, so it reshapes the spectrum of whatever drives it. A guitar body's dozens of resonances are collectively a fixed filter through which every note passes, and two guitars differ because their filters differ.

That view, a source with a spectrum, passed through a filter with a shape, is the single most useful model in the rest of this book. It is the model of the singing voice ([Chapter 13](#ch-the-singing-voice)), of the vowel, of subtractive synthesis ([Chapter 15](#ch-electronic-and-recorded-sound)), and of why a violin sounds like a violin whatever note it plays.

## Summary

- **Free vibration** happens at an object's natural frequency; **driven vibration** happens at the driving frequency. What the natural frequency controls is not the frequency of the response but its size.
- **Resonance** is the large response obtained by driving at a natural frequency. It works because at resonance the drive leads the displacement by exactly $90°$, in phase with the velocity, so every push adds energy.
- **The quality factor** $Q = f_0/\Delta f = \pi f_0\tau$ measures the sharpness of a resonance. A narrow peak and a long ring are the same fact stated two ways.
- **Loudness and sustain trade against each other**, because radiating sound is a loss of energy and losses lower $Q$. Instruments therefore want a high-$Q$ vibrator and a low-$Q$ resonator: a tuning fork has $Q$ in the thousands and is nearly silent, a guitar body has $Q$ near five and is loud.
- **A normal mode** is a pattern in which every part oscillates at one frequency with fixed relative amplitudes. A system with $N$ degrees of freedom has exactly $N$ of them; a continuous object has unlimited numbers.
- **Any motion is a sum of normal modes.** A plucked string is decomposed into modes, each oscillates at its own frequency, and the sum is the motion. Plucking at $L/n$ excites no $n$th mode, because the pluck point is a node of it.
- **A string's modes are harmonic**, exact whole-number ratios, but this is special. Bars and membranes are not, so percussion instruments mostly lack definite pitch.
- **A Helmholtz resonator** is a plug of air on a spring of air, with a single resonance at $f_0 = (v/2\pi)\sqrt{A/VL_{\text{eff}}}$. It is a bottle, a guitar's air mode, and a loudspeaker's bass port.
- **A resonator is both an amplifier and a filter**: it speeds energy out into the air, and it reshapes the spectrum passing through it. Source-plus-filter is the model used for the rest of the book.

## Conceptual Questions

1. A driven oscillator settles into oscillating at the driving frequency rather than its own. Explain what role its natural frequency then plays.

2. A child on a swing is pushed once per swing, and the swing grows. Explain why pushing twice per swing does not work, in terms of the phase of the drive relative to the velocity.

3. A tuning fork has a $Q$ of several thousand and a guitar body a $Q$ of about five. Which is louder, which rings longer, and explain why those two answers must go together.

4. Explain why a tall resonance peak is necessarily a narrow one, without using any formula.

5. Two masses connected by springs have two normal modes. Explain why the in-phase mode has the lower frequency.

6. A guitarist plucks a string exactly one-third of the way along. Which harmonics are missing from the resulting note, and why?

7. Explain why a bottle has essentially one resonance while an organ pipe has a whole harmonic series, even though both are containers of air.

8. In a violin, the string sets the pitch and the body responds. In a clarinet, the air column tells the reed what pitch to sound. Explain why this difference makes the two instruments require different kinds of analysis.

## Problems

:::{exercise}
:label: ex-resonance-1

*(Straightforward)* A resonance is measured with a peak at $440$ Hz and half-power points at $426$ Hz and $454$ Hz. (a) What is the bandwidth? (b) What is $Q$? (c) How long would this resonance ring after being struck?
:::

:::{solution} ex-resonance-1
:label: sol-resonance-1
:class: dropdown

(a) $\Delta f = 454 - 426 = 28$ Hz.

(b) $Q = f_0/\Delta f = 440/28 = 15.7$.

(c) From $Q = \pi f_0\tau$:

$$
\tau = \frac{Q}{\pi f_0} = \frac{15.7}{\pi(440\ \text{Hz})} = 0.0114\ \text{s}.
$$

Therefore, $Q \approx 16$ and the free decay time is about $11$ ms.
:::

:::{exercise}
:label: ex-resonance-2

*(Straightforward)* A wine glass rings at $720$ Hz and takes $2.8$ s for its amplitude to fall to $1/e$ of its initial value. (a) Find its $Q$. (b) Find the bandwidth of its resonance. (c) Comment on how precisely a singer would have to match the pitch to excite it.
:::

:::{solution} ex-resonance-2
:label: sol-resonance-2
:class: dropdown

(a) From $Q = \pi f_0\tau$:

$$
Q = \pi(720\ \text{Hz})(2.8\ \text{s}) = 6.3\times10^{3}.
$$

(b) From $Q = f_0/\Delta f$:

$$
\Delta f = \frac{f_0}{Q} = \frac{720}{6330} = 0.11\ \text{Hz}.
$$

(c) The singer must land within roughly a tenth of a hertz of $720$ Hz, about a quarter of a cent, and hold it. That is far finer than any singer can aim deliberately, so the demonstration is usually done by sweeping slowly through the region until the glass responds, rather than by hitting the note directly.
:::

:::{exercise}
:label: ex-resonance-3

*(Moderate)* A guitar's air resonance is at $98$ Hz with $Q = 6.0$. (a) Find the bandwidth. (b) Over what range of notes does the resonance provide at least half its peak power? (c) Express that range in semitones.
:::

:::{solution} ex-resonance-3
:label: sol-resonance-3
:class: dropdown

(a) $\Delta f = f_0/Q = 98/6.0 = 16.3$ Hz.

(b) Centered on $98$ Hz, the half-power range runs from about $98 - 8.2 = 89.8$ Hz to $98 + 8.2 = 106.2$ Hz.

(c) In semitones:

$$
n = 12\log_2\!\left(\frac{106.2}{89.8}\right) = 12(0.2420) = 2.9\ \text{semitones}.
$$

Therefore, the resonance usefully covers about three semitones. A low $Q$ is what makes even that possible; the wine glass of the previous problem covers about four *thousandths* of a semitone.
:::

:::{exercise}
:label: ex-resonance-4

*(Straightforward)* A bottle of internal volume $0.75$ L has a neck of cross-sectional area $3.8$ cm² and effective length $7.5$ cm. Take $v = 343$ m/s. (a) What note does it sound when blown across? (b) It is half filled with water. What note does it sound now?
:::

:::{solution} ex-resonance-4
:label: sol-resonance-4
:class: dropdown

(a) Converting to SI: $V = 7.5\times10^{-4}$ m³, $A = 3.8\times10^{-4}$ m², $L_{\text{eff}} = 0.075$ m.

$$
f_0 = \frac{343}{2\pi}\sqrt{\frac{3.8\times10^{-4}}{(7.5\times10^{-4})(0.075)}}
= 54.6\sqrt{6.76} = 54.6(2.60) = 142\ \text{Hz}.
$$

(b) Halving the air volume, with the neck unchanged:

$$
f_0' = f_0\sqrt{2} = 142\sqrt{2} = 201\ \text{Hz}.
$$

Therefore, the empty bottle sounds about $142$ Hz and the half-full one about $201$ Hz: a rise of $1200\log_2\sqrt2 = 600$ cents, exactly a tritone. Halving the volume always raises the pitch by exactly this interval, whatever the bottle.
:::

:::{exercise}
:label: ex-resonance-5

*(Straightforward)* A string is plucked at exactly one-quarter of its length. (a) Which harmonics are absent? (b) If the string sounds $220$ Hz, what are the frequencies of the three lowest absent harmonics? (c) Where should the player pluck to suppress the third harmonic instead?
:::

:::{solution} ex-resonance-5
:label: sol-resonance-5
:class: dropdown

(a) Plucking at $L/4$ puts the pluck point at a node of the 4th mode and of every multiple of 4. So harmonics 4, 8, 12, … are absent.

(b) $4 \times 220 = 880$ Hz, $8 \times 220 = 1760$ Hz, $12 \times 220 = 2640$ Hz.

(c) At $L/3$, which is a node of the 3rd mode (and of the 6th, 9th, …).

Therefore, the pluck position acts as a comb filter on the harmonic series, removing one harmonic and all its multiples, which is exactly the control a guitarist exercises by moving the right hand.
:::

:::{exercise}
:label: ex-resonance-6

*(Challenging)* A resonator has $f_0 = 250$ Hz. It is driven at (a) $250$ Hz, (b) $125$ Hz, (c) $500$ Hz, all with the same force amplitude. Using the response formula with $Q = 10$, find the amplitude in each case relative to the response to a very slow push.
:::

:::{solution} ex-resonance-6
:label: sol-resonance-6
:class: dropdown

The response is $A/A_{\text{static}} = 1/\sqrt{(1-r^2)^2 + (r/Q)^2}$, with $r = f/f_0$.

(a) $r = 1$: the first term vanishes, leaving

$$
A = \frac{1}{\sqrt{(1/10)^2}} = 10.
$$

(b) $r = 0.5$:

$$
A = \frac{1}{\sqrt{(1 - 0.25)^2 + (0.05)^2}} = \frac{1}{\sqrt{0.5625 + 0.0025}} = 1.33.
$$

(c) $r = 2$:

$$
A = \frac{1}{\sqrt{(1 - 4)^2 + (0.2)^2}} = \frac{1}{\sqrt{9 + 0.04}} = 0.333.
$$

Therefore, the amplitude at resonance is $Q = 10$ times the static response, while an octave below it is only $1.3$ times and an octave above it is *one third*: the resonator suppresses frequencies above its peak rather than merely failing to boost them.
:::

:::{exercise}
:label: ex-resonance-7

*(Moderate)* Two identical masses are joined by a spring of stiffness $k_c$ and each is joined to a wall by a spring of stiffness $k$. The in-phase mode has frequency $f_1 = (1/2\pi)\sqrt{k/m}$ and the out-of-phase mode $f_2 = (1/2\pi)\sqrt{(k + 2k_c)/m}$. (a) If $k_c = k$, what is the ratio $f_2/f_1$? (b) What happens to the ratio as the coupling spring becomes very weak?
:::

:::{solution} ex-resonance-7
:label: sol-resonance-7
:class: dropdown

(a) With $k_c = k$:

$$
\frac{f_2}{f_1} = \sqrt{\frac{k + 2k}{k}} = \sqrt{3} = 1.73.
$$

(b) As $k_c \to 0$,

$$
\frac{f_2}{f_1} = \sqrt{\frac{k + 2k_c}{k}} \to 1.
$$

Therefore, strong coupling splits the two mode frequencies widely apart, and weak coupling brings them together. In the limit of no coupling the two masses are independent oscillators of identical frequency: the "two modes" have become indistinguishable, which is what you would expect of two unconnected copies of the same thing.
:::

:::{exercise}
:label: ex-resonance-8

*(Straightforward)* A resonator stores $2.4$ mJ of energy and loses $0.15$ mJ per cycle. (a) Find its $Q$. (b) If its frequency is $180$ Hz, how long does it ring? (c) How many cycles is that?
:::

:::{solution} ex-resonance-8
:label: sol-resonance-8
:class: dropdown

(a) From $Q = 2\pi\times(\text{energy stored})/(\text{energy lost per cycle})$:

$$
Q = 2\pi\,\frac{2.4}{0.15} = 2\pi(16) = 101.
$$

(b) From $Q = \pi f_0 \tau$:

$$
\tau = \frac{101}{\pi(180)} = 0.178\ \text{s}.
$$

(c) The number of cycles in $\tau$ is $f_0\tau = (180)(0.178) = 32$ cycles.

Therefore, $Q \approx 100$, the amplitude falls to $1/e$ in about $0.18$ s, and that is about $32$ cycles. Note the general rule visible here: a resonator rings for roughly $Q/\pi$ cycles, whatever its frequency.
:::

:::{exercise}
:label: ex-resonance-9

*(Moderate)* An engineer wants a loudspeaker enclosure with a bass-reflex port tuned to $45$ Hz. The cabinet's internal volume is $32$ L and the port is a tube of radius $2.5$ cm. Ignoring end corrections, what length of port is needed?
:::

:::{solution} ex-resonance-9
:label: sol-resonance-9
:class: dropdown

Rearranging the Helmholtz formula for length:

$$
f_0 = \frac{v}{2\pi}\sqrt{\frac{A}{VL}}
\;\Rightarrow\;
L = \frac{A}{V}\left(\frac{v}{2\pi f_0}\right)^2 .
$$

With $A = \pi(0.025)^2 = 1.963\times10^{-3}$ m², $V = 0.032$ m³:

$$
L = \frac{1.963\times10^{-3}}{0.032}\left(\frac{343}{2\pi(45)}\right)^2
= (0.0614)(1.213)^2 = 0.0903\ \text{m}.
$$

Therefore, a port about $9.0$ cm long is needed. In practice the end correction would shorten this by several centimeters, which for a port this wide is a large fraction of the answer: the same warning as §3.5.
:::

:::{exercise}
:label: ex-resonance-10

*(Challenging)* Show that a resonator rings for approximately $Q/\pi$ cycles, and use the result to estimate how many cycles a tuning fork of $Q = 4000$ rings for.
:::

:::{solution} ex-resonance-10
:label: sol-resonance-10
:class: dropdown

The number of cycles in one decay time $\tau$ is $N = f_0\tau$. From $Q = \pi f_0\tau$,

$$
\tau = \frac{Q}{\pi f_0}
\;\Rightarrow\;
N = f_0\,\frac{Q}{\pi f_0} = \frac{Q}{\pi}.
$$

The frequency has canceled: **the number of cycles depends only on $Q$.**

For the tuning fork,

$$
N = \frac{4000}{\pi} = 1.3\times10^{3}\ \text{cycles}.
$$

Therefore, a fork of $Q = 4000$ rings for about $1300$ cycles before falling to $1/e$. At $440$ Hz that is about three seconds; at $256$ Hz, about five. The lower fork rings *longer in time* while ringing the same number of cycles.
:::

:::{exercise}
:label: ex-resonance-11

*(Moderate)* A drumhead has modes at $1.00$, $1.59$, $2.14$, $2.30$, and $2.65$ times its lowest frequency. A string has modes at $1$, $2$, $3$, $4$, $5$ times its lowest. (a) Express each set as intervals in cents above the lowest mode. (b) Explain, from the two lists, why the string has a definite pitch and the drumhead does not.
:::

:::{solution} ex-resonance-11
:label: sol-resonance-11
:class: dropdown

(a) Using $n = 1200\log_2(\text{ratio})$:

| Mode | Drumhead ratio | cents | String ratio | cents |
|---|---|---|---|---|
| 1 | 1.00 | 0 | 1 | 0 |
| 2 | 1.59 | 804 | 2 | 1200 |
| 3 | 2.14 | 1318 | 3 | 1902 |
| 4 | 2.30 | 1444 | 4 | 2400 |
| 5 | 2.65 | 1688 | 5 | 2786 |

(b) The string's partials are exact whole-number multiples of one frequency, so they are all harmonics of a single fundamental, and the auditory system can assign one pitch to the whole set ([Chapter 8](#ch-pitch-and-consonance)). The drumhead's are not multiples of anything: $1.59$, $2.14$, and $2.30$ have no common fundamental, so there is no single frequency the set points to.

Therefore, the drumhead gives the ear a collection of unrelated frequencies rather than a harmonic series, and the ear reports a sound with a rough pitch region rather than a note.
:::

:::{exercise}
:label: ex-resonance-12

*(Moderate)* A violin body has its main resonances near $280$ Hz and $460$ Hz, each with $Q \approx 25$, and the instrument's range runs from $196$ Hz to about $3000$ Hz. (a) Find the bandwidth of each resonance. (b) What fraction of the instrument's range is covered by the two together? (c) What does your answer imply about how the rest of the range is radiated?
:::

:::{solution} ex-resonance-12
:label: sol-resonance-12
:class: dropdown

(a) $\Delta f_1 = 280/25 = 11.2$ Hz and $\Delta f_2 = 460/25 = 18.4$ Hz.

(b) Together they cover about $30$ Hz out of a range of $3000 - 196 = 2804$ Hz, or about $1\%$.

(c) Two resonances plainly cannot account for the instrument's ability to radiate every note. The real body has *dozens* of modes above these, increasingly closely spaced, which merge into a broad and lumpy response rather than a set of isolated peaks. The two named resonances matter because they are isolated and therefore individually audible, they are the ones a maker can tune, but the rest of the range is radiated by a forest of overlapping higher modes.
:::

:::{exercise}
:label: ex-resonance-13

*(Straightforward)* A string is plucked at its exact midpoint. (a) Which harmonics are absent? (b) Compare the brightness of this note with one plucked near the bridge, and explain the difference in terms of the mode amplitudes.
:::

:::{solution} ex-resonance-13
:label: sol-resonance-13
:class: dropdown

(a) The midpoint is a node of every even mode, so harmonics 2, 4, 6, 8, … are absent. Only odd harmonics remain.

(b) A midpoint pluck is the *least* bright pluck available. It removes every even harmonic outright, and the $\sin(n\pi a/L)$ factor together with the $1/n^2$ falloff leaves the surviving odd harmonics weak as well. A pluck close to the bridge, at small $a$, makes $\sin(n\pi a/L)$ small for low $n$ and comparatively large for high $n$, so the spectrum tilts toward the high harmonics and the note is bright and thin.

Therefore, the same string can be made mellow or brilliant by nothing more than the choice of pluck point: a guitarist's right hand moves as much as the left for that reason.
:::

:::{exercise}
:label: ex-resonance-14

*(Moderate)* A maker is deciding how heavily to brace a guitar top. Heavier bracing raises the body's $Q$ from $5$ to $9$. (a) By what factor does the peak response change, at fixed damping-independent drive? (b) By what factor does the bandwidth change? (c) State in words what the player would notice.
:::

:::{solution} ex-resonance-14
:label: sol-resonance-14
:class: dropdown

(a) The peak response at resonance is proportional to $Q$, so it rises by $9/5 = 1.8$.

(b) The bandwidth is $f_0/Q$, so it falls by the same factor: to $5/9 = 0.56$ of what it was.

(c) The player would find that notes near the body resonance are louder and ring longer, while notes away from it are relatively weaker: the instrument has become less even across its range, and more colored. It would also sustain more and project less overall, since a higher $Q$ means less energy is leaving as sound per cycle.

Therefore, the trade-off of §4.3 appears directly as a design decision: bracing for evenness and volume means accepting a shorter sustain, and bracing for sustain means accepting an uneven instrument.
:::
