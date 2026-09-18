---
title: "Superposition, Interference, and Standing Waves"
short_title: "Chapter 3. Superposition, Interference, and Standing Waves"
label: ch-superposition
numbering:
  enumerator: "3.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 3.1, 3.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-03-superposition-interference-and-standing-waves.pdf
    chapter: 3
---

### Learning Objectives

By the end of this chapter, you should be able to:

- State the superposition principle, apply it graphically to find the resultant of two overlapping waves, and identify the condition under which it fails.
- Convert a path-length difference into a phase difference, and predict whether two waves from separated sources interfere constructively or destructively at a given point.
- Explain why two loudspeakers playing the same tone produce dead spots in a room, and estimate the spacing between them.
- Describe what happens to a wave pulse reflected from a fixed end and from a free end, and explain the inversion at a fixed end.
- Explain how a standing wave arises from two identical waves traveling in opposite directions, and locate its nodes and antinodes.
- Derive the frequencies of the standing-wave modes of a string fixed at both ends, $f_n = n v / 2L$, and use them to explain why a shorter or tighter string sounds higher.
- Derive the mode frequencies of an open and of a stopped air column, and explain why a stopped pipe sounds an octave lower than an open pipe of the same length and produces only odd harmonics.
- Explain why a standing wave is the reason an instrument has a definite pitch at all.

### Introduction

```{figure} ../images/open/ch03-chladni-historical.png
:label: fig:ch03-open-chladni
:alt: Historical drawing of a metal plate bowed at its edge to produce Chladni patterns.

An early experiment in making modes visible: a bowed plate gathers sand along its nodal lines. Public-domain illustration from 1879.
```

So far the book has followed one wave at a time. Music never does. A room is full of waves, the direct sound from the instrument, the reflection off the back wall, the note the second violin is playing, the reflection of *that* off the ceiling, all arriving at your ear at once and all adding up.

What they add up to is the subject of this chapter, and it is governed by one very simple rule with one very surprising consequence.

The rule is **superposition**: where two waves overlap, the displacements simply add. There is no interaction, no collision, no scattering of one wave off the other. Two waves pass through each other and emerge unchanged, as though nothing had happened.

The consequence is that waves can cancel. Two sounds can arrive at a point and produce silence there. And when a wave meets a wall, reflects, and runs back into itself, the adding-and-canceling settles into a stationary pattern, a **standing wave**, that can only exist at certain frequencies.

That last sentence is the reason musical instruments have pitches. Everything in [Part V](#ch-string-instruments) is an elaboration of it.

## The Superposition Principle

### Adding Waves Point by Point

The rule is as simple as it sounds. If wave 1 alone would produce a displacement $y_1$ at some point and some moment, and wave 2 alone would produce $y_2$ there and then, the two together produce

$$
y = y_1 + y_2.
$$

That is all. The waves do not know about each other.

```{animation} ch03-superposition
:label: fig:ch03-superposition
:alt: Two rows of three panels. In the top row two pulses of the same sign approach, overlap into a single taller pulse, and separate again unchanged. In the bottom row a positive and a negative pulse approach, cancel momentarily to a flat line, and separate again unchanged.

Two pulses passing through each other. In the top row they have the same sign and momentarily reinforce; in the bottom row they have opposite signs and momentarily cancel. In both cases they emerge on the other side exactly as they went in. The cancellation in the middle of the bottom row is complete, at that instant the medium is flat, but it is not the end of the pulses.
```

The bottom row of that figure deserves a moment's thought, because it looks like a violation of energy conservation. At the instant the two pulses exactly cancel, the string is perfectly straight. Where has the energy gone?

Into motion. The string is straight but it is not still: every point of it is moving, fast, and the energy is entirely kinetic at that instant. A moment later the pulses re-emerge. Superposition adds *displacements*, and displacement is not the only place a wave keeps its energy.

### Constructive and Destructive Interference

When two waves of the same frequency overlap steadily, what matters is their relative **phase**.

- In step, crest on crest, they reinforce. This is **constructive interference**, and the resulting amplitude is the sum of the two.
- Exactly out of step, crest on trough, they cancel. This is **destructive interference**, and if the amplitudes are equal the result is nothing at all.
- In between, something in between.

Two loudspeakers playing the same steady tone are the standard demonstration. Walk across the room in front of them and the tone rises and falls: loud where the two arrivals are in step, and startlingly near-silent where they are opposed.

:::{warning}
Destructive interference does not destroy energy; it moves it. The energy missing from a quiet spot is in the loud spots, which are *four* times as intense as either source alone would produce, not twice. Adding amplitudes and then squaring is not the same as adding intensities, and the difference is exactly what interference is.
:::

### Where Superposition Breaks Down

Superposition holds because the wave equation is **linear**: the restoring force is proportional to the displacement, as in [Chapter 1](#ch-sound-and-shm). Everything in this chapter depends on that.

It is an approximation, and it fails at large amplitudes. In an extremely loud sound wave the compressions travel slightly faster than the rarefactions, because compressed air is hotter and therefore stiffer; a wave that starts sinusoidal steepens as it travels, and at the limit it becomes a shock. This is not a musical regime, it takes something like a jet engine or an explosion, but it lurks in two places the book will return to: inside a brass instrument played very loudly, where the wave really does steepen on its way down the bore and adds a characteristic brightness to a fortissimo ([Chapter 11](#ch-wind-instruments)), and in a cymbal driven hard, where nonlinearity spills energy into a dense forest of new frequencies ([Chapter 12](#ch-percussion)).

## Interference in Space

### Path Difference and Phase Difference

The phase relationship between two arrivals at a listener is set by how far each has traveled. If the two sources emit in step, then all that matters is the **path difference**

$$
\Delta r = r_2 - r_1.
$$

A path difference of exactly one wavelength puts the two arrivals back in step: the second has been delayed by exactly one full cycle. A path difference of half a wavelength puts them exactly opposed. In general, the phase difference is

$$
\phi = \frac{2\pi}{\lambda}\,\Delta r,
$$

and the conditions are:

$$
\text{loud (constructive):}\quad \Delta r = m\lambda, \qquad
\text{quiet (destructive):}\quad \Delta r = \left(m + \tfrac12\right)\lambda,
$$

with $m = 0, 1, 2, \ldots$

```{animation} ch03-path-difference
:label: fig:ch03-path-difference
:alt: Left, two sources with lines drawn to a listener, labeled with path lengths r1 and r2 and their difference. Right, a graph of amplitude at the listener against path difference in wavelengths, peaking at whole numbers and falling to zero at half-integers.

Two sources and a listener sweeping past them. Everything depends on the difference between the two path lengths, measured in wavelengths, tracked by the moving dot on the right. The listener hears maximum loudness whenever that difference is a whole number of wavelengths and silence whenever it is a half-integer.
```

::::{tip} Worked example: finding a dead spot
*Two loudspeakers, $2.4$ m apart, both play a steady $860$ Hz tone in step. A listener stands $4.0$ m from one speaker. How far from the other must they be to hear nothing? Take $v = 343$ m/s.*

The wavelength is

$$
\lambda = \frac{v}{f} = \frac{343\ \text{m/s}}{860\ \text{Hz}} = 0.399\ \text{m}.
$$

Silence requires a path difference of half a wavelength, or one and a half, or two and a half. The smallest is

$$
\Delta r = \tfrac12\lambda = 0.199\ \text{m},
$$

so the listener must be $4.0 \pm 0.20$ m from the other speaker: that is, $4.20$ m or $3.80$ m.

Notice how *small* that displacement is. Moving your head twenty centimeters can take you from full loudness to near-silence at this frequency, which is why the effect is so easy to demonstrate and so disconcerting the first time.
::::

### Two Sources in a Room

The worked example understates the problem in a real room, because a real room has far more than two sources. Every reflecting surface acts as an image of the loudspeaker, so a single speaker in a rectangular room behaves like a large array of them, all radiating the same signal from different distances.

The result is that the sound field in a small room at low frequencies is a lumpy landscape of loud and quiet regions that does not change with time. Move your head and the bass changes. This is the room-mode problem, and [Chapter 14](#ch-room-acoustics) shows that it is worst exactly where it is most annoying: at low frequencies, where wavelengths are comparable to the room dimensions.

```{audio} ch03-walking-through-interference
:label: fig:ch03-walking-through-interference
:transcript: A steady tone that fades almost completely to silence three times, then returns to full loudness, as though someone were walking slowly past two loudspeakers.

What a listener hears walking through the interference pattern of two loudspeakers playing the same $500$ Hz tone. The loudspeakers are not changing; the *listener's position* is, and with it the path difference. Each near-silence is a half-integer number of wavelengths.
```

### Interference You Can Walk Through

Two things about that demonstration are worth drawing out, because both bear on music.

**It is frequency-dependent.** The pattern's spacing scales with the wavelength, so a given pair of sources produces a coarse pattern for bass and an extremely fine one for treble. Play *music* through two speakers rather than a single tone and no listener hears silence, because the nulls for different frequencies are in different places. What they hear instead is a position-dependent coloring of the sound, some frequencies reinforced, others suppressed, which is precisely the "comb filtering" that recording engineers work to avoid.

**It requires a stable phase relationship.** Two speakers fed from the same source stay in step indefinitely, so the pattern stands still. Two *different* instruments playing the same written note do not: their frequencies differ slightly and continuously, so the pattern drifts rather than standing still, and the listener hears beats ([Chapter 8](#ch-pitch-and-consonance)) rather than a fixed geography of loud and quiet.

```{phet} wave-interference
:label: fig:ch03-wave-interference-sim
:screen: 2
:placeholder: /images/phet/wave-interference-600.png

Two sources on the sound screen, with the interference pattern drawn out. Raise the frequency and note that the pattern's spacing narrows, the geometry is fixed, and only the wavelength has changed. The water screen shows the identical geometry with ripples instead of sound, if a visible medium helps first.
```

## Reflection and the Standing Wave

### Reflection at a Fixed and a Free End

A wave traveling along a string reaches the end. What happens next depends entirely on what is there.

If the end is **clamped**, it cannot move. But the arriving pulse is trying to move it, so the clamp must push back with an equal and opposite force, and the reflected pulse comes back **inverted**.

If the end is **free**, attached to a ring that can slide on a frictionless rod, say, nothing resists the motion. The end overshoots, and the pulse comes back **the same way up**.

```{animation} ch03-reflection
:label: fig:ch03-reflection
:alt: Two rows of three panels showing a pulse traveling toward a boundary. In the top row, against a thick wall, it returns inverted. In the bottom row, against a dotted free end marked with a ring, it returns upright.

Reflection at the two extreme boundaries. A fixed end forces the displacement to zero there, which can only be arranged if the reflected pulse is inverted; a free end imposes no such condition and the pulse returns upright. Real boundaries lie between these extremes, and the fraction of energy reflected is governed by the impedance mismatch of §2.4.
```

The same distinction applies to air columns, with one twist that catches everyone out. The **closed** end of a pipe is a place where the air cannot move: a displacement node, but it is a place where the pressure swings most: a pressure antinode. The **open** end is the reverse. Section 3.5 returns to this; you need to decide now which of the two quantities you are drawing, because the two pictures look like each other's opposites.

### Two Waves, Opposite Directions

Now put the two together. Send a continuous wave down a string toward a fixed end. It reflects and travels back, and from then on the string carries two identical waves traveling in opposite directions at once. Superposition says to add them.

```{animation} ch03-standing-wave-formation
:label: fig:ch03-standing-wave-formation
:alt: Five stacked panels showing a right-going dashed wave, a left-going dashed wave, and their solid sum, at five successive moments. The sum changes amplitude but its zero crossings stay at the same positions, marked with red dots.

A right-going wave and a left-going wave of the same frequency and amplitude, added continuously. The sum does not travel. It stands still and breathes: the whole pattern grows, shrinks, inverts, and grows again, but the points where it crosses zero never move.
```

That is a **standing wave**, and the striking thing about it is that nothing propagates. Energy sloshes back and forth locally; the pattern itself goes nowhere.

:::{dropdown} The trigonometry, in two lines
Two identical waves traveling in opposite directions are $y_1 = A\sin(kx - \omega t)$ and $y_2 = A\sin(kx + \omega t)$. Adding them, and using $\sin P + \sin Q = 2\sin\frac{P+Q}{2}\cos\frac{P-Q}{2}$:

$$
y = y_1 + y_2 = 2A\sin(kx)\cos(\omega t).
$$

The result has factored: one factor depends only on position, the other only on time. That separation *is* the standing wave. The shape $\sin(kx)$ is fixed in space; the factor $\cos(\omega t)$ scales the whole of it up and down together.

Compare this with the traveling wave it came from, $\sin(kx - \omega t)$, in which $x$ and $t$ appear only in the combination $kx - \omega t$, which is what makes the pattern move. The difference between a wave that travels and a wave that stands is exactly whether space and time can be separated.

The nodes are where $\sin(kx) = 0$, that is $kx = m\pi$, or $x = m\lambda/2$. They are spaced half a wavelength apart, and they are *permanently* at zero: no value of $t$ makes them move.
:::

### Nodes, Antinodes, and What Does Not Move

Two names for the parts of a standing wave:

- A **node** is a point that never moves. Nodes are half a wavelength apart.
- An **antinode** is a point that moves most. Antinodes lie halfway between nodes, also half a wavelength apart.

You can find the nodes of a guitar string by touching it very lightly at various points while it sounds. Touch an antinode and the note dies; touch a node and it carries on, because you are holding a point that was not moving anyway. This is not a party trick, it is exactly how a string player produces harmonics, and §3.4 uses it.

## Standing Waves on a String

```{figure} ../images/open/ch03-chladni-figures.jpg
:label: fig:ch03-open-chladni-pattern
:alt: Sand gathered into a branching Chladni pattern on a vibrating surface.

Nodal lines are not merely a drawing convention: powder makes them visible on a vibrating surface. Émile Desbeaux, public domain.
```

### Fitting Half-Wavelengths Between Two Ends

A string fixed at both ends must have a node at each end. That is a boundary condition, and it is very restrictive: only those standing waves which happen to have nodes exactly $L$ apart can exist on the string at all.

Since nodes are half a wavelength apart, the condition is that a whole number of half-wavelengths must fit into the length:

$$
L = n\,\frac{\lambda_n}{2}, \qquad n = 1, 2, 3, \ldots
$$

so

$$
\lambda_n = \frac{2L}{n}, \qquad f_n = \frac{v}{\lambda_n} = n\,\frac{v}{2L}.
$$

```{animation} ch03-string-modes
:label: fig:ch03-string-modes
:alt: Four panels showing the first four standing-wave modes of a string fixed at both ends, each drawn as an envelope with red dots marking nodes, labeled with wavelength 2L over n and frequency n times f1.

The first four modes of a string fixed at both ends, each drawn as an envelope the string sweeps between, with the instantaneous shape oscillating inside it. The $n$th mode has $n$ half-wavelengths in the length, $n-1$ nodes between the ends, and a frequency $n$ times the fundamental — watch the higher modes oscillate faster.
```

Combining this with the string's wave speed from [Chapter 2](#ch-wave-motion), $v = \sqrt{T/\mu}$:

$$
\boxed{\;f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}\;}
$$

This is the single most useful formula in the book's treatment of instruments, and every term in it is a lever an instrument maker or player can pull:

| Change | Effect on pitch | Who uses it |
|---|---|---|
| Shorten $L$ | Higher | Every fretting or stopping hand |
| Raise tension $T$ | Higher | Tuning pegs |
| Raise mass per length $\mu$ | Lower | Wound bass strings |

Note the **square roots**. Doubling the tension does not double the frequency; it raises it by a factor of $\sqrt{2}$, about seven semitones. To raise a string by an octave you must quadruple its tension; so instruments are tuned by shortening rather than by tightening, and the strings of a piano are of enormously varied length and mass rather than of varied tension alone.

### The Harmonic Series of a String

The set of frequencies $f_n = nf_1$ is the **harmonic series**, and the fact that it comes out as exact whole-number multiples is not an accident of the algebra. It is a consequence of the boundary conditions being the same at both ends and of the wave speed being the same at every frequency.

It is also, arguably, the reason Western music sounds the way it does. Chapters [5](#ch-fourier-and-timbre), [8](#ch-pitch-and-consonance), and [9](#ch-scales-and-tuning) are all downstream of it: the harmonic series determines what a plucked string's spectrum contains, which determines which intervals sound smooth, which determines what a scale is.

```{figure} ../images/notation/harmonic-series-on-c2.svg
:label: fig:ch03-harmonic-series-staff
:alt: The first sixteen harmonics of C2 written on a bass stave and a treble stave, each labeled with its harmonic number and its deviation in cents from the nearest equal-tempered note; the seventh and fourteenth are 31 cents flat, the eleventh 49 cents sharp, and the thirteenth 41 cents sharp.

The harmonic series on C2, written out. The first few partials are the intervals a musician already knows: an octave, a fifth, another octave, a major third. Further up, the series starts to disagree with the piano, the seventh partial is a third of a semitone flat of any key, and the eleventh sits almost exactly between two. That disagreement is the subject of [Chapter 9](#ch-scales-and-tuning). Notice early that the notes in this figure are what a *string* produces, not what a keyboard can play.
```

### Playing Harmonics

Touch a sounding string lightly at its midpoint. You have forced a node there. Every mode with a node at the midpoint: the 2nd, 4th, 6th, …, survives untouched; every mode without one: the 1st, 3rd, 5th, …, is killed. What remains sounds at $2f_1$, an octave above.

Touch at a third of the length and the surviving modes are the 3rd, 6th, 9th, …, sounding at $3f_1$, an octave and a fifth above. Touch at a quarter and you get $4f_1$, two octaves up.

```{audio} ch03-string-harmonics
:label: fig:ch03-string-harmonics
:transcript: Four notes on one string. The first is the full open string; the next three rise by an octave, an octave and a fifth, and two octaves, and each sounds purer and glassier than the last.

One string, touched at four places. The pitch rises through the harmonic series, and the tone becomes progressively thinner, because each touch removes more partials than the last. The glassy quality of a string harmonic is the sound of a spectrum with most of its members missing.
```

This is why the technique is called "playing harmonics", and it is a direct, audible demonstration that the modes really are all present at once in an ordinary plucked note. You are not adding anything by touching the string. You are subtracting.

```{openlyceum} StandingWaves
:label: fig:ch03-standing-waves-sim

Drive one end of a string and sweep the frequency slowly. Almost everywhere nothing much happens; at a handful of frequencies the string leaps into a clean pattern. Count the loops and check against $f_n = nf_1$, then change the tension and watch every resonance move by the same factor.
```

```{video} https://www.youtube.com/watch?v=PVX4V5Adbzk
:video-title: Standing Wave Harmonics
:label: fig:ch03-standing-wave-harmonics-video
:alt: A driven string displays successive standing-wave patterns with increasing numbers of loops.

Successive resonances on a driven string make the nodes, antinodes, and first several harmonics directly visible. Each higher mode fits one additional half-wavelength between the fixed ends.
```

## Standing Waves in an Air Column

### Open and Stopped Pipes

The same argument applies to the air in a tube, with different boundary conditions.

At a **closed** end the air cannot move, so there is a displacement node. At an **open** end the air is free to move and the pressure is forced to atmospheric, so there is a displacement antinode.

A pipe **open at both ends** therefore needs antinodes at both ends. That is satisfied by the same family as the string, a whole number of half-wavelengths, and gives

$$
f_n = n\,\frac{v}{2L}, \qquad n = 1, 2, 3, \ldots
$$

A pipe **stopped at one end** needs a node at one end and an antinode at the other, which are a *quarter* wavelength apart. The shortest fit is $L = \lambda/4$, and the next fits are $3\lambda/4$, $5\lambda/4$, and so on:

$$
f_n = n\,\frac{v}{4L}, \qquad n = 1, 3, 5, \ldots
$$

```{animation} ch03-pipe-modes
:label: fig:ch03-pipe-modes
:alt: Six panels in two columns. The left column shows the first three modes of a pipe open at both ends, with displacement antinodes at each end, labeled f1, 2f1, 3f1. The right column shows the first three modes of a pipe stopped at the left, with a node at the closed end and an antinode at the open end, labeled f1, 3f1, 5f1.
:aspect: 4:3

Air-column modes, drawn as the *displacement* of the air, oscillating inside their envelopes. The open pipe has antinodes at both ends and supports every harmonic. The stopped pipe has a node at the closed end and supports only the odd ones. Drawing the same modes as *pressure* would interchange nodes and antinodes everywhere, so a figure like this must say which quantity it shows.
```

### Odd Harmonics and the Missing Even Ones

Two consequences follow from that pair of formulas, and both are audible.

**A stopped pipe of a given length sounds an octave lower than an open pipe of the same length.** Compare $v/4L$ with $v/2L$. Organ builders use this constantly: a stopped rank gives a 16-foot pitch from 8 feet of pipe, which is a considerable saving in a church.

**A stopped pipe has only odd harmonics.** This is not a small change of color. Removing every even partial removes the octave, the second octave, and the octave-plus-fifth from the spectrum, leaving a characteristic hollow, woody sound. It is why the clarinet, effectively a stopped pipe, since the reed end is closed, sounds so unlike the flute, which is an open one, and it is why a clarinet overblows to a twelfth rather than an octave ([Chapter 11](#ch-wind-instruments)).

```{audio} ch03-open-pipe, ch03-stopped-pipe
:names: Open pipe, Stopped pipe
:figure: ../images/ch03-open-vs-stopped.svg
:label: fig:ch03-open-vs-stopped
:transcript: Two tones. The first is bright and full; the second is an octave lower and noticeably hollow, as though something had been taken out of the middle of it.

The same length of tube, played open and then stopped. Two things change at once; try to hear them separately: the pitch drops an octave, and the tone goes hollow because every even harmonic has vanished.
```

### Why the Pipe Length Is Not Quite the Wavelength

One correction, because it matters for anyone who tries to check these formulas by measurement.

The pressure at an open end is not *exactly* atmospheric, because the air just outside the tube is still being pushed around by the air inside it. The antinode therefore falls a little way *beyond* the physical opening, and the pipe behaves as though it were slightly longer than it is. The correction is about $0.6$ times the tube's radius, per open end.

For a narrow pipe this is negligible. For a wide one it is not: a pipe $30$ cm long and $5$ cm across has an effective length of about $31.5$ cm at one open end, or $33$ cm at two: a pitch error of nearly a semitone if you ignore it. [Chapter 11](#ch-wind-instruments) treats the correction properly, and the laboratory exercise in [](#appendix-laboratory) measures it.

:::{tip} Self-check
A stopped organ pipe sounds middle C, $262$ Hz, at $20$ °C. Without a calculator, say roughly how long it is. (Use $v \approx 343$ m/s, and remember which formula applies.)
:::

## Summary

- **Superposition**: where waves overlap, displacements add, and the waves emerge unchanged. This holds because the wave equation is linear, and it fails at extreme amplitudes, audibly so in a loud brass instrument and in a struck cymbal.
- **Interference** is superposition with a steady phase relationship. Two waves in step reinforce; two exactly opposed cancel. Energy is redistributed, not destroyed: the loud spots are four times the intensity of one source, not twice.
- **Path difference sets phase difference**: $\phi = (2\pi/\lambda)\Delta r$. Constructive interference requires $\Delta r = m\lambda$, destructive requires $\Delta r = (m+\frac12)\lambda$. The pattern is fine at high frequencies and coarse at low ones, which is why music through two speakers is colored rather than silenced.
- **Reflection inverts a pulse at a fixed end** and returns it upright at a free end. For air columns, a closed end is a displacement node and a pressure antinode; an open end is the reverse.
- **A standing wave is two identical waves traveling in opposite directions**, and it factorizes: $2A\sin(kx)\cos(\omega t)$. The shape is fixed in space and only its amplitude varies in time. Nodes never move and are half a wavelength apart.
- **A string fixed at both ends** admits only $\lambda_n = 2L/n$, giving $f_n = (n/2L)\sqrt{T/\mu}$: a complete harmonic series. Shorter, tighter, or lighter means higher, but tension enters as a *square root*, so an octave costs four times the tension.
- **Touching a string at a node** kills every mode that lacks one there, leaving a harmonic. This demonstrates that all the modes are present simultaneously in an ordinary note.
- **An open pipe gives $f_n = nv/2L$ with all harmonics; a stopped pipe gives $f_n = nv/4L$ with odd harmonics only.** A stopped pipe sounds an octave lower than an open pipe of the same length and sounds hollow, because every even partial is missing.
- **The effective length of a pipe exceeds its physical length** by about $0.6r$ per open end, which matters for wide tubes.

## Conceptual Questions

1. Two pulses of opposite sign meet on a string and momentarily cancel completely, leaving the string straight. Explain where the energy is at that instant.

2. Two loudspeakers play the same steady $1$ kHz tone. A listener walks slowly across the room and hears the loudness rise and fall. Explain why playing music instead of a tone produces no such silences.

3. Explain why a pulse reflecting from a clamped end comes back inverted, using only the requirement that the clamped point cannot move.

4. A standing wave transports no energy along the string, yet the string is full of moving parts. Reconcile these two statements.

5. A guitarist touches a sounding string lightly at its exact midpoint and the pitch jumps up an octave. Explain what has been removed, and why touching at the midpoint removes it.

6. Explain why raising a string's tension by a factor of two does not raise its pitch by an octave, and state what factor would.

7. A clarinet and a flute of similar length sound roughly an octave apart. Explain which sounds lower and why, in terms of boundary conditions.

8. The end correction for an open pipe is roughly $0.6r$. Explain why this makes the correction important for an organ's largest pipes and negligible for a piccolo, even though the *fractional* pitch error is what matters.

## Problems

:::{exercise}
:label: ex-superposition-1

Two loudspeakers, driven in step, play a $686$ Hz tone. Take $v = 343$ m/s. (a) What is the wavelength? (b) What is the smallest non-zero path difference that produces silence at a listener? (c) The smallest that produces maximum loudness?
:::

:::{solution} ex-superposition-1
:label: sol-superposition-1
:class: dropdown

(a) $\lambda = v/f = 343/686 = 0.500$ m.

(b) Destructive interference needs $\Delta r = (m + \frac12)\lambda$; the smallest is

$$
\Delta r = \tfrac12(0.500\ \text{m}) = 0.250\ \text{m}.
$$

(c) Constructive interference needs $\Delta r = m\lambda$. The smallest non-zero value is $\Delta r = 0.500$ m (the case $m = 0$, equal paths, is also loud but is not a *difference*).

Therefore, $25$ cm of extra path silences the tone and $50$ cm restores it.
:::

:::{exercise}
:label: ex-superposition-2

A string $0.62$ m long is fixed at both ends and waves travel along it at $240$ m/s. Find the frequencies of its first four modes.
:::

:::{solution} ex-superposition-2
:label: sol-superposition-2
:class: dropdown

The fundamental is

$$
f_1 = \frac{v}{2L} = \frac{240\ \text{m/s}}{2(0.62\ \text{m})} = 194\ \text{Hz},
$$

and the higher modes are whole-number multiples:

$$
f_2 = 387\ \text{Hz},\qquad f_3 = 581\ \text{Hz},\qquad f_4 = 774\ \text{Hz}.
$$

Therefore, the first four modes are $194$, $387$, $581$, and $774$ Hz: an exact harmonic series.
:::

:::{exercise}
:label: ex-superposition-3

A guitar string of length $64.0$ cm sounds $196$ Hz when played open. (a) What is the wave speed along it? (b) Where must the player's finger go to sound $261.6$ Hz? (c) What is the wavelength of the $196$ Hz *sound* in air, and why is it so different from the wavelength on the string?
:::

:::{solution} ex-superposition-3
:label: sol-superposition-3
:class: dropdown

(a) From $f_1 = v/2L$:

$$
v = 2Lf_1 = 2(0.640\ \text{m})(196\ \text{Hz}) = 251\ \text{m/s}.
$$

(b) The tension and mass per length are unchanged, so $v$ is unchanged and $f \propto 1/L$:

$$
L' = L\,\frac{f_1}{f'} = (64.0\ \text{cm})\frac{196}{261.6} = 47.9\ \text{cm},
$$

measured from the bridge; so the finger goes $64.0 - 47.9 = 16.1$ cm from the nut.

(c) In air,

$$
\lambda_{\text{air}} = \frac{343\ \text{m/s}}{196\ \text{Hz}} = 1.75\ \text{m},
$$

against $2L = 1.28$ m on the string. They differ because the wave *speeds* differ, $251$ m/s on the string against $343$ m/s in air, while the frequency is necessarily shared, the string being what drives the air.
:::

:::{exercise}
:label: ex-superposition-4

A string is tuned to $110$ Hz. By what factor must its tension change to tune it to (a) $165$ Hz, (b) $220$ Hz? (c) Comment on whether (b) is practical.
:::

:::{solution} ex-superposition-4
:label: sol-superposition-4
:class: dropdown

Since $f \propto \sqrt{T}$, the tension ratio is the square of the frequency ratio.

(a) $(165/110)^2 = 1.5^2 = 2.25$.

(b) $(220/110)^2 = 2^2 = 4.00$.

(c) Quadrupling the tension is not practical. String tensions are already set close to the breaking point of the material for good reasons, higher tension gives a louder, brighter note, so a factor of four would break the string, and if it did not, it would very likely pull the instrument apart. This is exactly why instruments span their range by changing length and mass per unit length rather than tension alone.
:::

:::{exercise}
:label: ex-superposition-5

An organ pipe open at both ends is $1.10$ m long. Take $v = 343$ m/s. (a) What is its fundamental frequency? (b) What are its next two modes? (c) If one end is stopped, what does the fundamental become?
:::

:::{solution} ex-superposition-5
:label: sol-superposition-5
:class: dropdown

(a) For an open pipe, $f_1 = v/2L$:

$$
f_1 = \frac{343}{2(1.10)} = 156\ \text{Hz}.
$$

(b) All harmonics are present: $f_2 = 312$ Hz, $f_3 = 468$ Hz.

(c) For a stopped pipe, $f_1 = v/4L$:

$$
f_1 = \frac{343}{4(1.10)} = 77.9\ \text{Hz}.
$$

Therefore, stopping one end drops the pitch by exactly an octave, and the surviving modes become $77.9$, $234$, $390$ Hz: the odd harmonics only.
:::

:::{exercise}
:label: ex-superposition-6

A stopped organ pipe is to sound $131$ Hz at $20$ °C. (a) What length of pipe is needed, ignoring the end correction? (b) If the pipe is $4.0$ cm in radius, what is the end correction, and what length should actually be cut?
:::

:::{solution} ex-superposition-6
:label: sol-superposition-6
:class: dropdown

(a) From $f_1 = v/4L$:

$$
L = \frac{v}{4f_1} = \frac{343}{4(131)} = 0.655\ \text{m}.
$$

(b) A stopped pipe has one open end, so one correction of about $0.6r$:

$$
\Delta L = 0.6(0.040\ \text{m}) = 0.024\ \text{m}.
$$

The *effective* length must be $0.655$ m, so the physical length cut should be

$$
0.655 - 0.024 = 0.631\ \text{m}.
$$

Therefore, cutting the naive $65.5$ cm would give an effective length of $67.9$ cm and a pitch of $126$ Hz, about $67$ cents flat, two-thirds of a semitone, and grossly out of tune.
:::

:::{exercise}
:label: ex-superposition-7

A violin string sounds $440$ Hz. A player touches it lightly one-third of the way along. (a) What frequency sounds? (b) Which harmonics survive? (c) Why does the note sound thinner than the open string?
:::

:::{solution} ex-superposition-7
:label: sol-superposition-7
:class: dropdown

(a) Touching at $L/3$ forces a node there, which only modes with $n$ a multiple of 3 possess. The lowest survivor is $n = 3$:

$$
f = 3 \times 440\ \text{Hz} = 1320\ \text{Hz}.
$$

(b) Harmonics 3, 6, 9, 12, … of the original string: that is, 1, 2, 3, 4, … of the new sounding pitch.

(c) Because two-thirds of the original partials have been removed. The surviving set is still a complete harmonic series on $1320$ Hz, but each of its members was a *high* partial of the original string and was therefore weak to begin with. The result is a spectrum with far less energy in it and fewer strong partials, which the ear reports as thin and glassy.
:::

:::{exercise}
:label: ex-superposition-8

Two identical waves, each of amplitude $A$, interfere. (a) What is the resulting amplitude when they are exactly in step? (b) When exactly opposed? (c) By what factor is the intensity of the in-step case greater than that of one wave alone, and where does the extra energy come from?
:::

:::{solution} ex-superposition-8
:label: sol-superposition-8
:class: dropdown

(a) $2A$. (b) Zero.

(c) Intensity goes as the square of amplitude, so the in-step case has $(2A)^2/A^2 = 4$ times the intensity of one wave alone, not twice.

The extra energy comes from the places where the waves cancel. Averaged over all positions, the mean intensity is $2A^2$, exactly twice one wave's, as conservation of energy requires. Interference redistributes energy from the nulls into the maxima; it does not create it.
:::

:::{exercise}
:label: ex-superposition-9

The A string of a bass is $1.06$ m long, of mass per unit length $\mu = 1.5\times10^{-2}$ kg/m, and sounds $55$ Hz. (a) What tension is it under? (b) The string is replaced by one of twice the mass per unit length, tuned to the same pitch. What tension is now needed?
:::

:::{solution} ex-superposition-9
:label: sol-superposition-9
:class: dropdown

(a) From $f_1 = (1/2L)\sqrt{T/\mu}$:

$$
T = \mu\,(2Lf_1)^2 = (1.5\times10^{-2})\,[2(1.06)(55)]^2
= (1.5\times10^{-2})(116.6)^2 = 204\ \text{N}.
$$

(b) At fixed $L$ and $f_1$, $T \propto \mu$, so doubling the mass per unit length doubles the required tension:

$$
T' = 408\ \text{N}.
$$

Therefore, the original tension is about $204$ N, roughly the weight of a 21 kg mass, and the heavier string would need twice that. This is the trade-off behind wound strings: mass lowers the pitch, but keeping the pitch while adding mass costs tension.
:::

:::{exercise}
:label: ex-superposition-10

Two speakers $3.0$ m apart face a listener standing $8.0$ m from the midpoint between them, on the perpendicular bisector. (a) What is the path difference? (b) The listener now walks $1.0$ m to one side. Find the new path difference, and state whether a $1720$ Hz tone is loud or quiet there. Take $v = 343$ m/s.
:::

:::{solution} ex-superposition-10
:label: sol-superposition-10
:class: dropdown

(a) On the perpendicular bisector the two distances are equal, so $\Delta r = 0$ and the listener is at a maximum.

(b) Put the speakers at $y = \pm1.5$ m and the listener at $(8.0, 1.0)$. Then

$$
r_1 = \sqrt{8.0^2 + (1.0 - 1.5)^2} = \sqrt{64.0 + 0.25} = 8.0156\ \text{m},
$$
$$
r_2 = \sqrt{8.0^2 + (1.0 + 1.5)^2} = \sqrt{64.0 + 6.25} = 8.3815\ \text{m},
$$

so $\Delta r = 0.366$ m. The wavelength is $\lambda = 343/1720 = 0.1994$ m, so

$$
\frac{\Delta r}{\lambda} = \frac{0.366}{0.1994} = 1.84.
$$

Therefore, the path difference is $1.84$ wavelengths, close to $1.5$ or $2.5$? It is nearer the whole number $2$ than the half-integer $1.5$, so the listener is closer to a loud position than a quiet one, though not exactly at a maximum.
:::

:::{exercise}
:label: ex-superposition-11

Show that the nodes of the standing wave $y = 2A\sin(kx)\cos(\omega t)$ are spaced half a wavelength apart, and that the antinodes lie exactly midway between them.
:::

:::{solution} ex-superposition-11
:label: sol-superposition-11
:class: dropdown

A node is a position where $y = 0$ for all $t$. Since $\cos(\omega t)$ is not always zero, this requires

$$
\sin(kx) = 0 \;\Rightarrow\; kx = m\pi \;\Rightarrow\; x = \frac{m\pi}{k} = \frac{m\lambda}{2},
$$

using $k = 2\pi/\lambda$. Successive nodes therefore differ by $\lambda/2$.

An antinode is a position where $|y|$ reaches its largest value, which requires $|\sin(kx)| = 1$, that is

$$
kx = \left(m + \tfrac12\right)\pi \;\Rightarrow\; x = \frac{(2m+1)\lambda}{4}.
$$

These are the odd multiples of $\lambda/4$, which lie exactly halfway between the even multiples that give the nodes.

Therefore, nodes and antinodes alternate at intervals of a quarter wavelength, with each kind spaced half a wavelength from its own neighbors.
:::

:::{exercise}
:label: ex-superposition-12

A clarinet behaves as a pipe stopped at the reed end. Its lowest note is written E$_3$, sounding about $147$ Hz. (a) Estimate its sounding length at $20$ °C. (b) A flute of the same length behaves as an open pipe; what is its lowest note? (c) Explain why the clarinet is the longer-sounding instrument for its physical size.
:::

:::{solution} ex-superposition-12
:label: sol-superposition-12
:class: dropdown

(a) For a stopped pipe, $L = v/4f_1$:

$$
L = \frac{343}{4(147)} = 0.583\ \text{m}.
$$

(b) For an open pipe of the same length, $f_1 = v/2L = 343/(2\times0.583) = 294$ Hz, exactly an octave higher.

(c) Because a stopped pipe sounds at $v/4L$ while an open one sounds at $v/2L$. The stopped pipe gets an octave lower out of the same physical length, since the shortest standing wave it can hold is a quarter wavelength rather than a half. A clarinet is therefore about half the length of a flute sounding the same low note: a real and substantial advantage, paid for by having only odd harmonics.
:::

:::{exercise}
:label: ex-superposition-13

A stopped pipe and an open pipe are both tuned to sound $220$ Hz. (a) Find the length of each. (b) List the first four modes of each. (c) A listener hears both play their second mode. What interval do they hear?
:::

:::{solution} ex-superposition-13
:label: sol-superposition-13
:class: dropdown

(a) Stopped: $L = v/4f_1 = 343/(4\times220) = 0.390$ m. Open: $L = v/2f_1 = 343/440 = 0.780$ m.

(b) Stopped, odd harmonics only: $220$, $660$, $1100$, $1540$ Hz. Open, all harmonics: $220$, $440$, $660$, $880$ Hz.

(c) The stopped pipe's second mode is $660$ Hz; the open pipe's is $440$ Hz. The ratio is $660/440 = 3/2$.

Therefore, the listener hears a perfect fifth, and one which is *exactly* 3:2, since both frequencies are exact harmonics of the same fundamental. [Chapter 9](#ch-scales-and-tuning) takes up what happens when a keyboard has to approximate that ratio.
:::

:::{exercise}
:label: ex-superposition-14

A pipe open at both ends is $28.0$ cm long and $3.0$ cm in radius. (a) Find its fundamental ignoring end corrections. (b) Find it including them. (c) Express the difference in cents, and say whether it matters.
:::

:::{solution} ex-superposition-14
:label: sol-superposition-14
:class: dropdown

(a) Ignoring corrections:

$$
f_1 = \frac{v}{2L} = \frac{343}{2(0.280)} = 613\ \text{Hz}.
$$

(b) Two open ends, each adding about $0.6r = 0.018$ m:

$$
L_{\text{eff}} = 0.280 + 2(0.018) = 0.316\ \text{m},
\qquad
f_1 = \frac{343}{2(0.316)} = 543\ \text{Hz}.
$$

(c) In cents:

$$
n = 1200\log_2\!\left(\frac{543}{613}\right) = 1200(-0.1750) = -210\ \text{cents}.
$$

Therefore, ignoring the correction would put the pipe more than two semitones sharp of where it actually sounds. For a tube this wide relative to its length, the end correction is not a refinement, it dominates any attempt to predict the pitch.
:::
