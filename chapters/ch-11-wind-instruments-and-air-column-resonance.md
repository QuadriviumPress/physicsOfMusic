---
title: "Wind Instruments and Air-Column Resonance"
short_title: "Chapter 11. Wind Instruments and Air-Column Resonance"
label: ch-wind-instruments
numbering:
  enumerator: "11.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 11.1, 11.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-11-wind-instruments-and-air-column-resonance.pdf
    chapter: 11
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Determine the resonant frequencies of open and stopped cylindrical air columns, and explain the octave difference between them.
- Explain why a conical bore produces a complete harmonic series while a cylindrical bore closed at one end produces only odd harmonics.
- Apply the end correction to an open pipe, and explain why the effective length exceeds the physical length.
- Explain how an air jet at an edge produces and sustains oscillation in a flute or a flue organ pipe.
- Describe the operation of a reed as a pressure-controlled valve, and distinguish inward- and outward-striking reeds.
- Explain why the clarinet overblows a twelfth while the saxophone and oboe overblow an octave, in terms of bore shape.
- Explain how the lips of a brass player act as a reed, and how the player selects among the instrument's resonances.
- Explain why the resonances of a brass instrument are nearly, but not exactly, a harmonic series, and describe the roles of the mouthpiece, the bore flare, and the bell.
- Describe the four ways of changing the sounding length of a wind instrument -- holes, keys, valves, and slides -- and state the intonation compromise each involves.

### Introduction

```{figure} ../images/open/ch11-clarinet.jpg
:label: fig:ch11-open-clarinet
:alt: A clarinet with its component parts labeled.

The bore, keys, mouthpiece, and bell are a coupled acoustic system. Gisbert K, CC0.
```

Wind instruments are organized differently from string instruments, and the difference comes first, before any details.

In a string instrument, the string decides the pitch. The body responds to whatever the string offers, and could be removed, leaving a quiet instrument, but one playing the same notes.

In a wind instrument, the **resonator decides the pitch**. The reed, the lips, or the air jet is a valve that will oscillate at almost any frequency if left to itself; what makes it oscillate at a *musical* frequency is feedback from the air column. Remove the bore from a clarinet and the reed produces a thin squawk at whatever frequency the player's lip happens to allow. Attach the bore and the reed plays what the bore tells it to.

This inverts the usual relationship. The air column is not an amplifier for the reed; the reed is a power supply for the air column.

Three questions organize the chapter. **What set of resonances does a given bore have?**, which turns out to depend on bore *shape* far more than on anything else. **How does the excitation lock onto them?**: the mechanisms differ interestingly between flutes, reeds, and lips. **How is the sounding length changed?**, by holes, keys, valves, or a slide, each with its own compromise.

## Resonances of an Air Column

### Pressure and Displacement Nodes

[Chapter 3](#ch-superposition) established the boundary conditions; they are restated carefully here because they are the commonest source of confusion in the subject.

At a **closed** end the air cannot move. That is a **displacement node**. But it is exactly where the pressure swings hardest, since the air is being alternately compressed against the wall and pulled away from it; so it is a **pressure antinode**.

At an **open** end the air is free to move, and the pressure is held close to atmospheric by the enormous reservoir outside. That is a **displacement antinode** and a **pressure node**.

Any diagram of an air column must therefore say which quantity it is drawing, because the two pictures are each other's inverses. This book draws displacement unless it says otherwise.

### The Open Pipe

A pipe open at both ends needs displacement antinodes at both, which requires a whole number of half-wavelengths:

$$
f_n = n\,\frac{v}{2L}, \qquad n = 1, 2, 3, \ldots
$$

A complete harmonic series. The flute, the recorder, and an open organ flue pipe all behave this way.

### The Stopped Pipe and Its Odd Harmonics

A pipe closed at one end needs a node at that end and an antinode at the other, which are a quarter wavelength apart:

$$
f_n = n\,\frac{v}{4L}, \qquad n = 1, 3, 5, \ldots
$$

Two consequences, both audible. The fundamental is an **octave lower** for the same length. And **every even harmonic is missing**, which makes the tone hollow.

The clarinet is effectively a stopped pipe: the reed end is closed, the reed is a stiff barrier for most of the cycle, and the bell end is open.

## Bore Shape

### Cylinders and Cones

Now a result that surprises everyone the first time.

A **cone**, closed at the apex, has a *complete* harmonic series:

$$
f_n = n\,\frac{v}{2L}, \qquad n = 1, 2, 3, \ldots
$$

the same as an open cylinder, despite being closed at one end.

```{animation} ch11-bore-shapes
:label: fig:ch11-bore-shapes
:alt: Three rows, each pairing a bore profile with its harmonic spectrum. An open cylinder gives harmonics 1 to 6 and overblows to an octave; a stopped cylinder gives only odd harmonics and overblows to a twelfth; a cone gives all harmonics and overblows to an octave.

Three bores and the resonances each supports. The stopped cylinder is the odd one out: only odd harmonics, and therefore a hollow tone and an overblow to a twelfth rather than an octave. The cone, despite being closed at its apex, behaves like the open cylinder.
```

### Why the Cone Restores the Even Harmonics

The physical reason is worth having, because it is not obvious.

In a cylinder the wave is **plane**: the same pressure across the whole cross-section, traveling straight down the tube. In a cone the wave is **spherical**, spreading from the apex, and a spherical wave's amplitude falls as $1/r$ as it expands.

Solving the wave equation in a cone gives pressure solutions of the form $\sin(kr)/r$. That function is zero at the apex regardless of $k$; so the apex's boundary condition costs nothing, and the resonances are set entirely by the open end. The result is the full series.

Put crudely: **a cone's closed end is not really a constraint**, because the spherical spreading already forces the pressure to behave correctly there.

The musical consequences are large. A saxophone and a clarinet both have single reeds and are both closed at the reed end. The saxophone is conical and the clarinet cylindrical, and they differ accordingly:

| | Clarinet | Saxophone |
|---|---|---|
| Bore | Cylindrical | Conical |
| Harmonics | Odd only | All |
| Overblows to | A twelfth | An octave |
| Tone | Hollow, woody | Full, reedy |
| Length for a given pitch | Half | Full |

```{audio} ch11-open-cylinder, ch11-stopped-cylinder, ch11-cone
:names: Open cylinder, Stopped cylinder, Cone
:figure: ../images/ch11-bore-timbres.svg
:label: fig:ch11-bore-timbres
:transcript: Three sustained tones. The first is bright and flute-like. The second is an octave lower and distinctly hollow. The third is the same pitch as the second but full and reedy rather than hollow.

Three bores of the same physical length. Compare the second and third carefully: they sound the *same pitch*, both being closed at one end, and differ entirely in whether the even harmonics are there.
```

```{audio} ch11-overblow-twelfth, ch11-overblow-octave
:names: Cylinder overblowing, Cone overblowing
:figure: ../images/ch11-bore-shapes.svg
:label: fig:ch11-overblow
:transcript: Two pairs of notes. In the first, the second note is a twelfth above the first, an octave and a fifth. In the second, the second note is exactly an octave above.

Overblowing. A cylindrical stopped pipe has no second harmonic to jump to, so it jumps to the third, a twelfth. A clarinet's register key therefore produces a twelfth, and a clarinetist must learn different fingerings for the two registers, while a saxophonist's fingerings simply repeat at the octave.
```

### The End Correction

A pipe sounds as though it were slightly longer than it is, because the pressure node does not fall exactly at the opening: the air just outside is still being driven.

$$
L_{\text{eff}} = L + 0.6\,r \quad \text{per open end.}
$$

```{figure} ../images/ch11-end-correction.svg
:label: fig:ch11-end-correction
:alt: Left, a pipe with the standing-wave pattern extending past the physical opening, with the extra length marked as 0.6 r. Right, the pitch error in cents from ignoring the correction, against the ratio of bore radius to length, rising steeply for wide pipes.

The end correction. **Left**: the antinode falls outside the tube. **Right**: what ignoring it costs. For a narrow organ pipe it is a few cents; for a wide, short pipe it can exceed a semitone.
```

This is not a refinement to be mentioned and forgotten. An organ builder cutting pipes to length must include it, and because it depends on radius rather than on length, it matters more for short wide pipes than for long narrow ones: that is, more in the treble than in the bass, where a naive calculation would put the whole top of the instrument sharp.

## The Air Jet

```{figure} ../images/open/ch11-recorders-set.jpg
:label: fig:ch11-open-flutes
:alt: Five recorders of different sizes, from sopranino to bass, arranged in a row beside a ruler for scale.

Different lengths and constructions expose the geometric choices behind the simple air-column model. Saskii, English Wikipedia, public domain.
```

### Edge Tones

The flute family has no reed. Instead, a thin **jet** of air is directed across a sharp edge.

A jet crossing an edge is unstable. Small disturbances on it grow as it travels, so the jet flaps from one side of the edge to the other, alternately blowing into the pipe and outside it. On its own, this produces an **edge tone** whose frequency depends on the jet speed and the distance to the edge, and which glides continuously as the player blows harder.

### Flutes and Recorders

Couple that jet to a pipe and the pipe takes control. A standing wave in the bore produces an oscillating flow at the mouth hole, which pushes the jet from side to side at the pipe's resonant frequency, which reinforces the standing wave. The jet locks to the pipe.

Two things follow that a player will recognize.

**Blowing harder raises the pitch a little.** The jet has a natural preference of its own, and forcing it away from that preference pulls the locked frequency slightly. Flutists correct constantly by rolling the instrument in or out, changing the effective mouth-hole geometry.

**The edge tone is the noise you hear.** A flute's characteristic breathiness is the jet's unlocked, turbulent component, and it is present in every note. Synthesizing a flute without it produces something that sounds like an organ.

### Flue Organ Pipes

An organ flue pipe is the same mechanism made permanent. The jet speed is set by the wind pressure of the whole organ rather than by a player, and everything a flutist does with embouchure is instead built into the pipe's geometry at the time of voicing: the height of the mouth, the sharpness of the lip, the width of the windway.

An organ pipe therefore has exactly one tone color and one dynamic. An organ needs so many pipes for that reason: every note of every color needs its own, and a large instrument has five thousand of them.

## Reed Instruments

### The Reed as a Valve

A reed does not vibrate like a string, and treating it as one gets the physics wrong.

A reed is a **pressure-controlled valve**. The player supplies steady pressure; the reed opens and closes a gap; the rate of opening and closing determines the frequency of the puffs of air entering the bore.

```{figure} ../images/ch11-reed-valve.svg
:label: fig:ch11-reed-valve
:alt: Left, a schematic of a mouth at steady pressure driving a reed at the entrance to a bore, with a curved arrow showing the bore's reflected pressure wave returning to control the reed. Right, the input impedance of the bore, showing sharp peaks at odd harmonics.

The feedback loop. The reed lets a puff of air into the bore; the bore reflects a pressure wave back; that returning pressure helps close the reed at the right moment. The reed oscillates at a frequency the **bore** chooses, not at its own natural frequency.
```

The evidence that the bore is in charge is immediate: a clarinet reed's own natural frequency is a couple of kilohertz, and the instrument plays notes from $147$ Hz upward. The reed is being driven far below its own resonance, and it goes where it is told.

The same reed therefore plays every note of the instrument, and changing the fingering changes the pitch without the player touching the reed.

:::{note}
A reed's behavior depends on whether increasing pressure tends to *close* it or *open* it. A clarinet's reed is **inward-striking**: mouth pressure pushes it toward closed, so it must be driven below its own resonance. A harmonium's or accordion's free reed is **outward-striking** and behaves quite differently, playing at a frequency close to its own. It is the inward-striking geometry that lets one reed serve a whole instrument.
:::

### The Clarinet and the Twelfth

The clarinet is a cylindrical stopped pipe, so §11.2 applies in full: odd harmonics, a tone that is hollow in the low register, and an overblow to a twelfth.

That twelfth is the clarinet's central practical problem. A twelfth spans nineteen semitones, so nineteen different fingerings are needed before the register key can be used at all, against eleven for an octave-overblowing instrument. This is the reason the clarinet has so many keys, why its fingering is so much harder to learn than the saxophone's, and why the awkward "throat" notes around the register break are the weakest on the instrument.

The compensation is that the clarinet gets a low register out of a short tube, and gets it with a distinctive hollow color that no other woodwind provides.

### The Conical Reeds: Oboe, Bassoon, Saxophone

The oboe and bassoon use double reeds and the saxophone a single one, but acoustically the important thing they share is a **conical** bore. All three therefore produce complete harmonic series and overblow at the octave.

The conical bore also explains a structural point. A cone must come to a point to be acoustically complete, and a real instrument's reed sits where the point would be. The reed and its staple are designed so that their internal volume is approximately equal to that of the missing conical tip: an equivalent-volume substitution which, if it is wrong, throws the instrument's octaves out. Oboists trimming a reed are adjusting this, whether or not they describe it that way.

## Brass Instruments

```{figure} ../images/open/ch11-trumpet.png
:label: fig:ch11-open-trumpet-range
:alt: A historical diagram comparing the ranges of trumpet and slide trumpet.

Changing the effective tube length changes the available resonance series. Victor Charles Mahillon and Kathleen Schlesinger, public domain.
```

### The Lip Reed

A brass player's lips are a reed made of flesh, and the feedback mechanism is the same as §11.4's. The lips buzz; the bore reflects; the reflection controls the buzz.

The difference is that lips are **adjustable**. A player changes their tension and aperture continuously, and by doing so chooses which of the bore's resonances to lock onto. A trumpeter plays a scale on a fixed tube by changing nothing but their lips.

```{video} https://www.youtube.com/watch?v=tGdyrXz4Wg8
:video-title: The Physics of Brass Instruments, Part 1: The Lips
:label: fig:ch11-brass-lips-video
:alt: A physicist demonstrates how a brass player's lips vibrate and couple to an instrument.

A physicist explains the lips as an adjustable oscillating valve and the air column as the resonator that selects its pitch. The demonstration shows the feedback loop behind the compact description above.
```

### Mouthpiece, Bore, and Bell

Now a problem. A cylindrical tube closed at one end gives odd harmonics only, $1, 3, 5, \ldots$, which would make a brass instrument's playable notes an unmusical set. Yet a bugle plays a recognizable harmonic series.

The resolution is that a brass instrument is not a cylinder. It is a carefully shaped combination of three elements that between them force the resonances into line.

```{figure} ../images/ch11-brass-resonances.svg
:label: fig:ch11-brass-resonances
:alt: A plot of resonance frequency against resonance number, comparing a real trumpet whose resonances lie on a near-exact harmonic series from the second upward with a plain cylinder of the same length whose resonances are odd multiples of a quarter-wave frequency.

What the mouthpiece and bell are for. A plain cylindrical tube's resonances are an unusable set. A trumpet's are pulled into a harmonic series from the second resonance upward, and the player's lips then select among them.
```

The **mouthpiece** is a small cavity with a constriction: a Helmholtz resonator ([Chapter 4](#ch-resonance)) with a resonance around $800$ Hz. Its effect is to pull the upper resonances down into alignment, and to boost the output in the region where the ear is most sensitive.

The **bore** is mostly cylindrical in a trumpet, mostly conical in a horn, and the mixture determines how the resonances line up as well as the instrument's character.

The **bell** does two jobs, and they are opposite.

```{figure} ../images/ch11-bell-behaviour.svg
:label: fig:ch11-bell-behavior
:alt: Two curves against logarithmic frequency: the fraction of energy reflected back into the bore, falling from one to zero around 800 Hz, and the fraction radiated into the room, rising from zero to one across the same region.

The bell as a frequency-dependent mirror. Below the cut-off it reflects almost everything, which is what keeps the standing wave alive. Above it, it radiates almost everything, which is what makes the instrument loud and directional.
```

Below a **cut-off frequency** set by the flare, the bell reflects sound back into the bore, which is essential, because without reflection there is no standing wave and no resonance to lock onto. Above the cut-off, it radiates efficiently into the room, so brass instruments are loud and their high harmonics beam forward.

This split is audible. It is why a trumpet's low notes fill a hall while its high notes go where the bell points ([Chapter 2](#ch-wave-motion)), and why a player turning aside changes the sound so completely.

### Making the Resonances Harmonic

The first resonance stubbornly refuses to join the series. A brass instrument's lowest resonance is typically well below where a true fundamental would sit, and it is essentially unusable.

Players nonetheless produce a note there, the **pedal tone**, and the mechanism is [Chapter 8](#ch-pitch-and-consonance)'s missing fundamental: the lips buzz at the fundamental frequency, the higher resonances (2, 3, 4, …) all support harmonics of it, and the ear supplies the fundamental that the instrument is barely radiating.

```{audio} ch11-bugle
:label: fig:ch11-bugle
:transcript: A rising and falling sequence of eleven notes on a single brass tone, unmistakably a bugle call, using only the notes available without valves.

Resonances 2 through 8 of a fixed tube, the complete vocabulary of a valveless brass instrument. Every bugle call in every army is made from these notes, so they all sound alike. The 7th resonance is skipped: [Chapter 9](#ch-scales-and-tuning) showed it is $31$ cents flat of any key.
```

## Changing the Length

```{figure} ../images/open/ch11-flute-met.jpg
:label: fig:ch11-open-flute-met
:alt: A historical transverse flute photographed in a museum collection.

An air column is shaped by its physical length and by the openings that interrupt it. The Metropolitan Museum of Art, CC0.
```

### Tone Holes and the Register Hole

A woodwind changes its sounding length by opening holes. Opening a hole creates a pressure node near it, effectively ending the tube there.

The approximation is imperfect. A hole is not a complete opening: some of the standing wave leaks past it and continues down the remaining tube, so the effective end is a little beyond the hole and depends on the hole's size. Large holes approximate a true open end better, but large holes are hard to cover with fingers: a tension that runs through the whole history of woodwind design and that keywork exists to resolve.

::::{tip} Worked example: what a tone hole does to the pitch
*The flute of [](#ex-wind-instruments-1) has a sounding length of $65.5$ cm and a fundamental of $262$ Hz. A tone hole is opened $49.1$ cm from the embouchure hole, three-quarters of the way down the tube. Treating the open tone hole as a new open end, what note does the flute now sound, as an interval above the original?*

The tube behaves as an open pipe of the new, shorter length:

$$
f_1' = \frac{v}{2L'} = \frac{343\ \text{m/s}}{2(0.491\ \text{m})} = 349\ \text{Hz}.
$$

The interval above the original $262$ Hz is

$$
1200\log_2\!\left(\frac{349}{262}\right) = 1200\log_2\!\left(\frac{4}{3}\right) = 498\ \text{cents},
$$

a perfect fourth, because $65.5/49.1$ is very nearly $4/3$.

Therefore a single tone hole, placed at three-quarters of the tube's length, raises the pitch a fourth: exactly the kind of arithmetic a woodwind maker uses when laying out a scale of holes along a bore. Real instruments depart from this idealization in the direction already noted above, some of the standing wave leaks past even an open hole, so the effective end sits a little beyond it, and the true pitch comes out slightly lower than this calculation predicts, more so for a small hole than a large one.
::::

A **register hole** is a small hole placed near a pressure node of the desired higher mode. It barely disturbs that mode while spoiling the fundamental, so the instrument jumps up. Its placement is a compromise, because one hole must serve many notes, and this is the origin of the weak, stuffy notes near a clarinet's register break.

### Keys and the Woodwind Compromise

Keywork exists to put holes where acoustics wants them rather than where fingers reach. The Boehm system, developed for the flute in the 1830s and adapted to the clarinet and saxophone, uses rods and levers so that one finger can close a distant or oversized hole.

The gain is intonation and evenness; the cost is mechanical complexity, and a modern clarinet has around twenty keys.

### Valves, Slides, and Their Intonation Problems

Brass instruments change length by adding tube.

A **slide**, as on a trombone, adds a continuously variable length. It is acoustically perfect, any length is available, so any pitch is, and it is why a trombonist can play in just intonation with a string section.

**Valves** divert the air through fixed extra loops: conventionally the second lowers by a semitone, the first by a tone, and the third by a minor third. Combinations give the rest.

The combinations are systematically sharp, and the reason is arithmetic. Each valve is cut to lower the pitch of the *open* instrument by its interval. But using two valves together means the second is lengthening an already-lengthened tube, and lowering a longer tube by a fixed interval requires a *longer* addition than lowering the original. The fixed loop is now too short, and the note comes out sharp, by around $20$ cents for two valves and $35$ or more for three.

Players and makers address this in three ways: alternate fingerings, a movable slide on the first or third valve operated while playing, and compensating systems that route the air through extra tubing when certain combinations are used. None is a complete solution, so brass intonation is a skill rather than a property of the instrument.

## Summary

- **In a wind instrument the resonator sets the pitch**, and the reed, lips, or air jet is a valve that locks to it. This inverts the string instrument's arrangement.
- A **closed end** is a displacement node and a pressure antinode; an **open end** is the reverse. Any diagram must say which it shows.
- **Open cylinder**: $f_n = nv/2L$, all harmonics. **Stopped cylinder**: $f_n = nv/4L$, odd harmonics only: an octave lower for the same length, hollow, and overblowing to a twelfth.
- **A cone closed at the apex has a complete harmonic series**, because the spherical solution $\sin(kr)/r$ vanishes at the apex for every $k$, so the closed end imposes no constraint. This is the whole difference between the clarinet and the saxophone.
- **The end correction** adds about $0.6r$ per open end, and matters most for short wide pipes.
- **An air jet at an edge** is unstable and locks to the pipe's resonance; the unlocked component is the breathiness, which is part of the sound rather than a defect.
- **A reed is a pressure-controlled valve** driven far below its own resonance. The bore's impedance peaks choose the frequency, so one reed plays every note.
- **A brass instrument's mouthpiece and bell force its resonances into a harmonic series** from the second upward. The bell reflects below its cut-off, essential for the standing wave, and radiates above it, which makes the instrument loud and directional.
- **The pedal tone** is a missing fundamental: the lips buzz at a frequency the instrument barely radiates, and the ear supplies it from the harmonics.
- **Valve combinations are systematically sharp**, because a fixed length added to an already-lengthened tube lowers the pitch by less than intended. Slides have no such problem.

## Check Your Understanding

Five short, auto-graded questions cycle within one compact activity, using five different response styles.

:::{h5p} ch11-chapter-review
:label: check:ch11-chapter-review
:title: Chapter 11 interactive review

1. **Multiple choice.** Compared with an open cylindrical pipe of the same length, what are the fundamental and harmonic series of a stopped cylindrical pipe?
2. **True or false.** A cone closed at its apex has only odd harmonics, just like a stopped cylinder.
3. **Drag the words.** Complete the pressure and displacement node/antinode conditions at open and closed pipe ends.
4. **Fill in the blanks.** A clarinet’s stopped-cylinder bore overblows to the ___, while a conical saxophone overblows to the ___.
5. **Mark the words.** Identify the two brass-instrument features that pull resonances toward a useful harmonic series: “The mouthpiece lowers upper resonances and the bell raises lower resonances.”
:::

## Conceptual Questions

1. Explain why removing the bore from a clarinet stops it playing a musical note, and why removing the body from a violin does not.

2. State the boundary conditions at a closed and an open end for both displacement and pressure, and explain why a figure must say which it shows.

3. Explain why a clarinet overblows to a twelfth while a saxophone overblows to an octave, given that both are closed at the reed end.

4. Explain, without algebra, why the closed apex of a cone imposes no constraint on the resonant frequencies.

5. A flutist blows harder and the pitch rises slightly. Explain the mechanism, and say what the player does about it.

6. Explain why a brass instrument's bell must reflect some sound rather than radiating all of it.

7. A brass player produces a pedal tone at a frequency where the instrument has no usable resonance. Explain how.

8. Explain why pressing two valves together produces a note that is sharp, and name one remedy.

## Problems

:::{exercise}
:label: ex-wind-instruments-1

*(Straightforward)* A flute behaves as an open cylinder. Its lowest note is $262$ Hz at $20$ °C. (a) What is its sounding length? (b) What are its next two resonances?
:::

:::{solution} ex-wind-instruments-1
:label: sol-wind-instruments-1
:class: dropdown

(a) For an open pipe, $f_1 = v/2L$:

$$
L = \frac{v}{2f_1} = \frac{343\ \text{m/s}}{2(262\ \text{Hz})} = 0.655\ \text{m}.
$$

(b) All harmonics: $524$ Hz and $786$ Hz.

Therefore about $65.5$ cm of sounding length, with resonances at $262$, $524$, $786$ Hz: a complete harmonic series, so a flute overblows to the octave.
:::

:::{exercise}
:label: ex-wind-instruments-2

*(Moderate)* A clarinet behaves as a stopped cylinder and its lowest note sounds $147$ Hz. (a) What is its sounding length? (b) What are its next two resonances? (c) What interval is the first overblow?
:::

:::{solution} ex-wind-instruments-2
:label: sol-wind-instruments-2
:class: dropdown

(a) For a stopped pipe, $f_1 = v/4L$:

$$
L = \frac{343\ \text{m/s}}{4(147\ \text{Hz})} = 0.583\ \text{m}.
$$

(b) Odd harmonics only: $3 \times 147 = 441$ Hz and $5 \times 147 = 735$ Hz.

(c) From $147$ to $441$ Hz is a ratio of $3$:

$$
1200\log_2 3 = 1902\ \text{cents} = 19\ \text{semitones},
$$

a twelfth.

Therefore a clarinet gets its low register from $58$ cm of tube where a flute would need $117$ cm, and pays for it with a nineteen-semitone overblow.
:::

:::{exercise}
:label: ex-wind-instruments-3

*(Moderate)* A pipe is $42.0$ cm long and $2.2$ cm in radius, open at both ends. (a) Find its fundamental ignoring end corrections. (b) Find it including them. (c) Express the difference in cents.
:::

:::{solution} ex-wind-instruments-3
:label: sol-wind-instruments-3
:class: dropdown

(a) $f_1 = (343\ \text{m/s})/(2 \times 0.420\ \text{m}) = 408$ Hz.

(b) Two open ends, each adding $0.6r = 0.0132$ m:

$$
L_{\text{eff}} = 0.420\ \text{m} + 2(0.0132\ \text{m}) = 0.446\ \text{m},
\qquad
f_1 = \frac{343\ \text{m/s}}{2(0.446\ \text{m})} = 384\ \text{Hz}.
$$

(c)

$$
1200\log_2(384/408) = -105\ \text{cents}.
$$

Therefore ignoring the correction would put the prediction more than a semitone sharp. For a pipe of this proportion the correction is not optional.
:::

:::{exercise}
:label: ex-wind-instruments-4

*(Moderate)* A saxophone and a clarinet both sound $147$ Hz. (a) Compare their sounding lengths. (b) Compare the frequencies of their first four resonances. (c) Which is heavier to carry, and why is it worth it?
:::

:::{solution} ex-wind-instruments-4
:label: sol-wind-instruments-4
:class: dropdown

(a) The clarinet is a stopped cylinder: $L = v/4f_1 = 0.583$ m. The saxophone is a cone, so $L = v/2f_1 = 1.17$ m, twice as long.

(b) Clarinet: $147$, $441$, $735$, $1029$ Hz (odd harmonics). Saxophone: $147$, $294$, $441$, $588$ Hz (all harmonics).

(c) The saxophone, being twice the tube for the same pitch. What it buys is a complete harmonic series, a fuller tone, and an octave overblow, which halves the number of distinct fingerings a player must learn.

Therefore the clarinet trades tone and fingering simplicity for compactness, and the saxophone trades compactness for both.
:::

:::{exercise}
:label: ex-wind-instruments-5

*(Moderate)* A trumpet's tube is $1.48$ m long. (a) Treating it as an open pipe, find the first four resonances. (b) Which of these can a player sound with the lips? (c) What are the corresponding musical intervals?
:::

:::{solution} ex-wind-instruments-5
:label: sol-wind-instruments-5
:class: dropdown

(a) $f_1 = (343\ \text{m/s})/(2 \times 1.48\ \text{m}) = 116$ Hz, so the series is $116$, $232$, $348$, $464$ Hz.

(b) Resonances 2, 3, 4 and upward. The first is not properly supported by a real trumpet, for the reasons of §11.5, it lies below where the bell and mouthpiece pull the series into line.

(c) From $232$ to $348$ Hz is a fifth ($3{:}2$); $348$ to $464$ is a fourth ($4{:}3$); $232$ to $464$ is an octave.

Therefore the playable notes are the harmonic series from the second upward, and the intervals between successive resonances narrow as the player goes higher, high brass playing therefore requires fine lip control.
:::

:::{exercise}
:label: ex-wind-instruments-6

*(Moderate)* A trumpet's second valve lowers the pitch by a semitone. (a) By what factor must the tube lengthen? (b) If the open tube is $1.48$ m, how much tube must the valve add? (c) Repeat for the first valve, which lowers by a whole tone.
:::

:::{solution} ex-wind-instruments-6
:label: sol-wind-instruments-6
:class: dropdown

(a) Frequency goes as $1/L$, so lowering by a semitone requires

$$
L' = L \times 2^{1/12} = 1.05946\,L.
$$

(b) The addition is

$$
\Delta L = 1.48(1.05946 - 1) = 0.088\ \text{m} = 8.8\ \text{cm}.
$$

(c) A whole tone needs $L' = L \times 2^{2/12} = 1.12246\,L$:

$$
\Delta L = 1.48(0.12246) = 0.181\ \text{m} = 18.1\ \text{cm}.
$$

Therefore about $8.8$ cm and $18.1$ cm of extra tubing. Note that the second is more than twice the first, which is the seed of the next problem.
:::

:::{exercise}
:label: ex-wind-instruments-7

*(Challenging)* Using the trumpet of [](#ex-wind-instruments-6), a player presses valves 1 and 2 together, intending a minor third. (a) What total length results? (b) What length would a true minor third need? (c) How sharp is the note, in cents?
:::

:::{solution} ex-wind-instruments-7
:label: sol-wind-instruments-7
:class: dropdown

(a) The two additions simply sum:

$$
L = 1.48 + 0.088 + 0.181 = 1.749\ \text{m}.
$$

(b) A true minor third is three semitones:

$$
L_{\text{true}} = 1.48 \times 2^{3/12} = 1.48 \times 1.18921 = 1.760\ \text{m}.
$$

(c) The tube is short by $0.011$ m, so the pitch is sharp by

$$
1200\log_2\!\left(\frac{1.760}{1.749}\right) = 10.9\ \text{cents}.
$$

Therefore the combination is about $11$ cents sharp. The cause is exactly as §11.6 describes: valve 1's loop was cut to lower the *open* tube by a tone, but here it must lower a tube already lengthened by valve 2, and a fixed length does less lowering on a longer tube.
:::

:::{exercise}
:label: ex-wind-instruments-8

*(Straightforward)* A brass instrument's bell has a cut-off frequency of $1.5$ kHz. (a) What happens to a $400$ Hz component reaching the bell? (b) A $4$ kHz component? (c) Explain why both behaviors are necessary.
:::

:::{solution} ex-wind-instruments-8
:label: sol-wind-instruments-8
:class: dropdown

(a) $400$ Hz is well below cut-off, so almost all of it is **reflected** back into the bore.

(b) $4$ kHz is well above, so almost all of it is **radiated** into the room.

(c) Reflection is what sustains the standing wave: without a returning pressure wave there is no resonance for the lips to lock onto, and no note. Radiation is what the audience hears. An instrument that reflected everything would resonate beautifully and be inaudible; one that radiated everything would be loud for an instant and then have nothing left to oscillate with.

Therefore the bell must do both, and the cut-off is where it changes its mind, which is also why brass instruments sound so different on and off axis, since the radiated high components are the directional ones.
:::

:::{exercise}
:label: ex-wind-instruments-9

*(Moderate)* An organ builder must make a stopped pipe sounding $65.4$ Hz at $15$ °C, with a bore radius of $5.0$ cm. (a) Find the speed of sound. (b) Find the required effective length. (c) Find the physical length to cut.
:::

:::{solution} ex-wind-instruments-9
:label: sol-wind-instruments-9
:class: dropdown

(a) $v = 331.3 + 0.606(15) = 340.4$ m/s.

(b) For a stopped pipe:

$$
L_{\text{eff}} = \frac{v}{4f_1} = \frac{340.4}{4(65.4)} = 1.301\ \text{m}.
$$

(c) One open end, so one correction of $0.6r = 0.030$ m:

$$
L = 1.301 - 0.030 = 1.271\ \text{m}.
$$

Therefore cut $127.1$ cm. Cutting the uncorrected $130.1$ cm would give an effective length of $133.1$ cm and a pitch of $63.9$ Hz, about $40$ cents flat, which on an organ is unusable.
:::

:::{exercise}
:label: ex-wind-instruments-10

*(Challenging)* A clarinet's register key must be placed near a pressure node of the third harmonic. The instrument's sounding length is $58.3$ cm and it is stopped at the reed end. (a) Where along the tube is that node? (b) Explain why one hole cannot serve every note perfectly.
:::

:::{solution} ex-wind-instruments-10
:label: sol-wind-instruments-10
:class: dropdown

(a) The third mode of a stopped pipe has $3\lambda/4 = L$, so $\lambda = 4L/3 = 0.777$ m. Pressure nodes occur at odd quarter-wavelengths from the closed end:

$$
x = \frac{\lambda}{4} = 0.194\ \text{m},
$$

about $19.4$ cm from the reed. (The next is at $3\lambda/4 = 58.3$ cm, the open end.)

(b) Because the sounding length changes with every fingering. As tone holes open, the effective tube shortens and the position of the third mode's pressure node moves with it, but the register hole is drilled once, in one place. It is therefore correctly placed for only one note and progressively wrong for the others.

Therefore the register break is inherently a compromise, and the notes furthest from the hole's ideal position are the stuffy, unreliable ones every clarinetist knows.
:::

:::{exercise}
:label: ex-wind-instruments-11

*(Challenging)* Show that a cone closed at its apex has resonances at $f_n = nv/2L$, using the fact that pressure solutions in a cone have the form $p(r) \propto \sin(kr)/r$.
:::

:::{solution} ex-wind-instruments-11
:label: sol-wind-instruments-11
:class: dropdown

Take the apex at $r = 0$ and the open end at $r = L$.

**At the apex.** The solution $p \propto \sin(kr)/r$ is finite there, since $\sin(kr)/r \to k$ as $r \to 0$. There is no condition to impose: the closed apex is automatically satisfied for *every* $k$, which is the whole point.

**At the open end.** The pressure must vanish:

$$
\frac{\sin(kL)}{L} = 0 \;\Rightarrow\; \sin(kL) = 0 \;\Rightarrow\; kL = n\pi,
$$

for $n = 1, 2, 3, \ldots$

Since $k = 2\pi f/v$:

$$
\frac{2\pi f_n}{v}L = n\pi
\qquad\Rightarrow\qquad
f_n = \frac{nv}{2L}.
$$

Therefore the cone gives every integer $n$, a complete harmonic series: the same as an open cylinder. Compare the stopped cylinder, where the closed end *does* impose a condition ($\mathrm{d}p/\mathrm{d}x = 0$) and halves the available set.
:::

:::{exercise}
:label: ex-wind-instruments-12

*(Moderate)* A trumpeter plays a pedal tone. The instrument's resonances are at $232$, $348$, $464$, $580$ Hz. (a) What is the common fundamental of these? (b) Does the instrument have a strong resonance there? (c) Explain what the listener hears and why.
:::

:::{solution} ex-wind-instruments-12
:label: sol-wind-instruments-12
:class: dropdown

(a) The spacing is $116$ Hz and each listed frequency is a multiple of it, so the fundamental is $116$ Hz.

(b) No. These are resonances 2, 3, 4, 5, and the first resonance of a real trumpet lies well away from $116$ Hz, it is the one the bell and mouthpiece fail to pull into line.

(c) The player's lips buzz at $116$ Hz. Each of its harmonics, $232$, $348$, $464$, …, coincides with a strong resonance and is supported, so the instrument radiates a full harmonic series on $116$ Hz while radiating almost nothing at $116$ Hz itself. The ear then does what [Chapter 8](#ch-pitch-and-consonance) describes and reports the fundamental.

Therefore the pedal tone is a missing fundamental, and a spectrum analyzer pointed at the bell would show very little energy at the pitch everyone in the room is hearing.
:::

:::{exercise}
:label: ex-wind-instruments-13

*(Moderate)* A flute is tuned at $21$ °C and played outdoors at $8$ °C. (a) How far flat does it go? (b) The player pushes the head joint in to shorten the instrument. If the sounding length was $65.5$ cm, by how much must they shorten it?
:::

:::{solution} ex-wind-instruments-13
:label: sol-wind-instruments-13
:class: dropdown

(a) The speeds are $v(21) = 344.0$ m/s and $v(8) = 336.1$ m/s. Pitch follows the speed:

$$
1200\log_2\!\left(\frac{336.1}{344.0}\right) = -40\ \text{cents}.
$$

(b) To recover $40$ cents the length must fall by the same ratio:

$$
L' = 0.655 \times \frac{336.1}{344.0} = 0.640\ \text{m},
$$

a shortening of $1.5$ cm.

Therefore the flute goes $40$ cents flat and needs about $15$ mm of head-joint adjustment, which is a large movement, and more than the joint allows on some instruments. Outdoor performance in the cold is genuinely difficult for wind players for that reason.
:::

:::{exercise}
:label: ex-wind-instruments-14

*(Moderate)* Compare a trombone and a valved trumpet as instruments for playing in just intonation with a string quartet. (a) Which is better suited, and why? (b) What must the trumpeter do instead? (c) Relate your answer to [Chapter 9](#ch-scales-and-tuning).
:::

:::{solution} ex-wind-instruments-14
:label: sol-wind-instruments-14
:class: dropdown

(a) The trombone. Its slide provides a continuously variable tube length, so any pitch whatever is available: the player can place a third $14$ cents flat of equal temperament to match a string section without effort.

(b) The trumpeter has only fixed valve combinations, each of which gives a pitch determined by the tubing. They must bend the note with their lips, "lipping" it up or down, which works over perhaps $\pm30$ cents but costs tone quality and stability, or use an alternate fingering, or operate a movable slide on the first or third valve while playing.

(c) [Chapter 9](#ch-scales-and-tuning) divided instruments into fixed-pitch and flexible-pitch, and noted that the compromise always falls on the flexible ones. A trombone is fully flexible and belongs with the strings and voices. A valved trumpet is *partly* fixed, which puts it in an awkward middle position: flexible enough to be expected to adjust, constrained enough that adjusting is work.
:::
