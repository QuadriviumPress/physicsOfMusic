---
title: "Percussion: Membranes, Bars, and Plates"
short_title: "Chapter 12. Percussion: Membranes, Bars, and Plates"
label: ch-percussion
numbering:
  enumerator: "12.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 12.1, 12.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-12-percussion-membranes-bars-and-plates.pdf
    chapter: 12
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Explain why the modes of a two-dimensional vibrator are generally inharmonic, and why this makes most percussion instruments indefinite in pitch.
- Describe the transverse modes of a free-free bar, and state the frequencies of the first few relative to the fundamental.
- Explain how undercutting a marimba bar brings its second mode into a harmonic relation with its first, and what that does to the perceived pitch.
- Describe the mode shapes of a circular membrane, identify nodal diameters and circles, and explain why an ideal drumhead has no definite pitch.
- Explain how the air loading of a kettle turns the timpani's inharmonic modes into a near-harmonic set, and identify which mode sounds the pitch.
- Describe the modes of a flat plate, interpret a Chladni pattern, and explain what the sand reveals.
- Explain why cymbals and gongs produce a dense, noise-like spectrum, and describe the nonlinear energy cascade responsible.
- Describe the modes of a church bell and the tuning practice that makes the hum, prime, tierce, quint, and nominal fall in fixed relations.
- Explain what it means to tune an inharmonic instrument, and identify the strategies used for bars, kettles, and bells.

### Introduction

```{figure} ../images/open/ch12-timpani-kettle-drums.jpg
:label: fig:ch12-open-timpani
:alt: A pair of ornate silver kettle drums with their bowls, membranes, and tensioning screws visible.

Percussion instruments make mode shapes physical: a stretched membrane, a bowl, and an adjustable boundary all contribute to the sound. The Metropolitan Museum of Art, CC0.
```

Every instrument so far has had a harmonic spectrum. Strings and air columns are one-dimensional, and their boundary conditions force their modes into exact whole-number ratios; so they have clear pitches, their tones blend, and [Chapter 9](#ch-scales-and-tuning)'s tuning systems are built out of small integers.

Percussion is different, and the difference is not a matter of degree.

A drumhead, a metal bar, a plate, a bell: these are two-dimensional or three-dimensional vibrators, and their modes fall in ratios like $1: 1.59: 2.14: 2.30: 2.65$. Nothing forces those into whole numbers, and they are not. The ear, presented with such a set, cannot find a fundamental that explains it ([Chapter 8](#ch-pitch-and-consonance)), and reports a sound with a rough pitch region rather than a note.

Percussion therefore divides so sharply into instruments of **definite** and **indefinite** pitch, and the definite ones, timpani, marimba, tuned bells, are the result of considerable ingenuity. Each is an object that has been *made* to have a pitch, by moving its modes into place. This chapter is largely about how.

It is also where the book's model starts to strain. [Chapter 5](#ch-fourier-and-timbre)'s spectrum assumed periodicity; a cymbal is not periodic. [Chapter 8](#ch-pitch-and-consonance)'s consonance assumed harmonic partials; a gamelan's are not. The physics still works, it is just that the answers stop looking like music theory.

## Why Percussion Is Different

### One Dimension Versus Two

A string is a one-dimensional system, and its modes are indexed by a single number $n$. The boundary conditions, zero at both ends, force $\lambda_n = 2L/n$ and hence $f_n = nf_1$. The whole-number ratios come from counting half-wavelengths along one direction.

A membrane is two-dimensional, and a mode must satisfy a boundary condition around a whole *curve* rather than at two points. Its modes are indexed by two numbers, and the frequencies are set by the zeros of **Bessel functions** rather than by the zeros of a sine. Bessel zeros are irrational numbers with no arithmetic relationship to each other.

```{animation} ch12-membrane-modes
:label: fig:ch12-membrane-modes
:alt: Six panels showing the first six modes of a circular membrane as red and blue regions with black nodal lines, labeled (0,1) at 1.00 f1, (1,1) at 1.59, (2,1) at 2.14, (0,2) at 2.30, (3,1) at 2.65 and (1,2) at 2.92.

The first six modes of an ideal circular membrane. Each is labeled $(m, n)$ with $m$ nodal **diameters** and $n{-}1$ nodal **circles** inside the rim. The frequency ratios, $1.00$, $1.59$, $2.14$, $2.30$, $2.65$, $2.92$, are not whole numbers, are not close to whole numbers, and are not multiples of anything.
```

A bar is one-dimensional but obeys a different equation. A string's restoring force comes from **tension**; a bar's comes from **bending stiffness**, and the resulting equation has a fourth derivative rather than a second. Its modes come out in the ratios

$$
1: 2.756: 5.404: 8.933: \ldots
$$

which are the squares of the roots of $\cos x \cosh x = 1$, again, no whole numbers anywhere.

```{phet} normal-modes
:label: fig:ch12-normal-modes-sim
:placeholder: /images/phet/normal-modes-600.png

Switch to the two-dimensional screen. The modes of a rectangular array are
indexed by two numbers, and their frequencies are emphatically not whole-number
multiples of the lowest, which is this chapter's opening claim, in the simplest
two-dimensional system there is.
```

### Inharmonic Modes and Indefinite Pitch

[Chapter 8](#ch-pitch-and-consonance) explained what the ear does with a set of partials: it looks for a fundamental of which all are harmonics. Given $200, 300, 400, 500$ Hz it finds $100$ Hz and reports it, even if nothing is there.

Given $200, 318, 428, 460, 530$ Hz it finds nothing. There is no fundamental that explains this set, and the pattern-matching mechanism has no answer to return. The listener hears a sound with a *center of gravity*, they can say it is high or low, and can tell one drum from another, but not a note. They cannot sing it back, and it does not participate in harmony.

```{audio} ch12-membrane-ideal, ch12-timpani
:names: Ideal membrane, Modeled timpano
:figure: ../images/ch12-timpani-modes.svg
:label: fig:ch12-membrane-vs-timpani
:transcript: Two struck drum sounds. The first is a dull thud with no identifiable note in it. The second is recognizably a timpano and has a clear pitch that could be sung back.

An ideal membrane and a modeled kettledrum, struck the same way. The difference is entirely in where the partials sit, and §12.3 explains how the kettle moves them.
```

```{audio} ch12-real-timpani
:label: fig:ch12-real-timpani
:transcript: A real timpani strike begins with a short mallet impact, settles into a clearly pitched low ring, and decays for several seconds.

A recorded timpani. The synthesized comparison above isolates the shifted mode
ratios; this CC0 recording restores everything the model leaves out: mallet
noise, room sound, small mistunings, and interacting decays.
```

### Strike Tone and Decay

Two more features distinguish percussion.

**The strike transient is a large part of the sound.** [Chapter 5](#ch-fourier-and-timbre) showed that attack carries an instrument's identity; for percussion it may carry most of it. The initial contact is broadband noise, a click, and removing it makes a struck bar sound like an organ.

**Different partials decay at very different rates.** High modes lose energy faster, so the spectrum thins as the sound dies. A struck bell begins as a clangorous mixture and ends as a nearly pure hum tone, and the change is one of the most recognizable things about it.

## Bars

### Modes of a Free-Free Bar

A xylophone or marimba bar is supported at two points and otherwise free. Its transverse modes are in the ratios $1: 2.756: 5.404: \ldots$, and the second is the problem: $2.756$ is close to neither $2$ (an octave) nor $3$ (a twelfth), and it clashes with the fundamental.

The supports are placed at the **nodes** of the fundamental mode, about $22\%$ of the length from each end, so that holding the bar does not damp the note it is supposed to produce. This is the same principle as touching a string at a node ([Chapter 3](#ch-superposition)).

```{figure} ../images/ch12-bar-modes.svg
:label: fig:ch12-bar-modes
:alt: Left, a bar chart comparing the mode ratios of a plain bar, 1, 2.76, 5.40, with the tuned values 1, 4, 10 of an undercut bar, against dotted lines at whole numbers. Right, a bar profile thinned in the middle, with a note explaining that removing wood there lowers the second mode more than the first.

Left: a plain bar's modes against an undercut bar's. Right: where the wood comes off. Thinning the middle is not decoration, it is what makes a marimba a pitched instrument.
```

### Undercutting: Xylophone, Marimba, Vibraphone

The fix is to remove material from the underside of the bar, and the reasoning is elegant.

The fundamental has its maximum displacement, its antinode, at the center of the bar. The second mode has a *node* there. Removing material from the center therefore weakens the bar where the fundamental is bending hardest and where the second mode is barely bending at all, so it lowers the fundamental far more than it lowers the second mode.

Remove enough and the ratio $2.756$ can be driven up to $4.0$, two octaves, an exact harmonic. Continue and the third mode can be brought to about $10$.

The amount of undercutting distinguishes the instruments:

| Instrument | Second mode tuned to | Character |
|---|---|---|
| Xylophone | $3f_1$ (a twelfth) | Bright, sharp, penetrating |
| Marimba | $4f_1$ (two octaves) | Warm, full, mellow |
| Vibraphone | $4f_1$ | Mellow, sustained (aluminum, long decay) |

```{audio} ch12-bar-plain, ch12-bar-undercut
:names: Plain bar, Undercut bar
:figure: ../images/ch12-bar-comparison.svg
:label: fig:ch12-bar-comparison
:transcript: Two struck bars at the same fundamental. The first is clangorous and hard to assign a note to; the second has a clear, warm pitch.

The same fundamental, with the second mode at $2.76$ and at $4.0$ times it. Moving one partial is enough to turn a clang into a note.
```

### Struck Bars That Are Not Undercut

A glockenspiel's bars are not undercut, and its steel bars keep the $2.756$ ratio.

It works anyway, for a reason worth noticing: the glockenspiel plays **high**. Its fundamentals are above $2$ kHz, so the inharmonic second mode lands above $5$ kHz: a region where [Chapter 8](#ch-pitch-and-consonance) showed pitch perception is poor and where the ear largely stops trying to match patterns. The partial is audible as brightness rather than as a clashing pitch.

Tubular bells exploit the same loophole from the other direction: their modes are inharmonic, but modes 4, 5, and 6 happen to fall close to the ratios $2: 3: 4$, and the ear constructs a **missing fundamental** from them. A tubular bell's perceived pitch is an octave below its lowest strong partial and corresponds to no mode of the tube at all.

## Membranes

### Modes of a Circular Membrane

The modes of an ideal circular membrane, fixed at the rim, are

$$
f_{mn} = \frac{\alpha_{mn}}{2\pi a}\sqrt{\frac{T}{\sigma}},
$$

where $a$ is the radius, $T$ the tension per unit length, $\sigma$ the mass per unit area, and $\alpha_{mn}$ the $n$th zero of the Bessel function $J_m$.

The ratios were listed in §12.1, and none of them is anything.

::::{tip} Worked example: the fundamental of a drumhead
*A snare drum's batter head has radius $a = 0.178$ m (a $14$-inch drum), areal mass density $\sigma = 0.20$ kg/m², and is tensioned to $T = 3200$ N/m. Using $\alpha_{01} = 2.405$, find its $(0,1)$ fundamental.*

$$
f_{01} = \frac{\alpha_{01}}{2\pi a}\sqrt{\frac{T}{\sigma}} = \frac{2.405}{2\pi(0.178)}\sqrt{\frac{3200}{0.20}} = (2.151)(126.5) = 272\ \text{Hz}.
$$

The next mode up, $(1,1)$, sits at $1.59$ times this, about $432$ Hz, an interval of

$$
1200\log_2(1.59) = 804\ \text{cents}.
$$

The nearest ratio of small whole numbers is $8{:}5$ ($813.7$ cents), itself an unremarkable interval, not a number that organizes a scale, and even that near-miss does not extend to the modes above it. A snare drum, unlike a timpano, has no enclosed kettle of air to pull this family of ratios toward consonance, so its head produces this pattern undisguised: a perfectly well-defined $f_{01}$, and no definite pitch at all.
::::

### Nodal Diameters and Nodal Circles

The index $m$ counts **nodal diameters**, straight lines across the head that do not move, and $n-1$ counts **nodal circles**.

This has a practical consequence percussionists use constantly. Striking at the center excites only the modes with no nodal diameter, $(0,1)$, $(0,2)$, and so on, because every mode with $m \ge 1$ has a node there. Striking near the rim excites the $(m,1)$ family strongly.

Timpanists strike about a quarter of the way in from the rim, and §12.3 explains why that is exactly right.

### The Timpani: How the Kettle Fixes the Pitch

A timpano is a membrane with a pitch, and it gets one from three things at once.

**The air in the kettle loads the head.** The enclosed air resists being compressed, which adds stiffness, and it has mass, which the head must drag along. Crucially the loading is *different for different modes*: the $(0,1)$ mode moves the whole head in the same direction and compresses the kettle air strongly, so it is stiffened a great deal. The $(1,1)$ mode moves one half up while the other goes down, so the air merely sloshes sideways and is barely compressed at all.

**The result is that the modes move by different amounts**, and they move into a near-harmonic set.

```{figure} ../images/ch12-timpani-modes.svg
:label: fig:ch12-timpani-modes
:alt: A bar chart comparing the mode ratios of an ideal membrane, 1, 1.59, 2.14, 2.65, 3.16, with measured timpani values of 1, 1.50, 2.00, 2.44, 2.90, against dotted lines at 1, 1.5, 2, 2.5 and 3.

Ideal against real. The air-loaded timpani modes sit very close to the ratios $1: 1.5: 2: 2.5: 3$, which is $2: 3: 4: 5: 6$ of a fundamental one octave below the lowest mode. The ear finds that fundamental and reports it.
```

**The pitch heard is a missing fundamental.** Multiply the measured set by two and it reads $2: 3: 4: 5: 6$, harmonics 2 through 6 of a note an octave below the $(1,1)$ mode. Exactly as with the brass pedal tone of [Chapter 11](#ch-wind-instruments), the ear supplies what the instrument does not radiate.

The $(0,1)$ mode, which moves the whole head as a piston, is the one mode that does *not* fit this series. It is also the loudest radiator, because a piston pushes far more air than a mode with nodal diameters. So a timpanist strikes about a quarter of the way in, near a node of $(0,1)$, suppressing the one mode that would spoil the pitch, and favoring the ones that make it.

## Plates, Shells, and Bells

### Flat Plates and Chladni Patterns

A flat plate has modes indexed by two numbers, like a membrane, but stiffness-controlled, like a bar. Their ratios are inharmonic and depend on the plate's shape and boundary conditions.

The classic way to see them is **Chladni's** method, published in 1787: scatter sand on the plate and excite a mode, and the sand bounces away from the moving regions and collects along the nodal lines.

```{video} https://www.youtube.com/watch?v=wYoxOJDrZzw
:video-title: Singing Plates: Standing Waves on Chladni Plates
:label: fig:ch12-singing-plates-video
:alt: Sand on a metal plate forms distinct geometric patterns at successive resonant frequencies.

Physics Girl excites successive resonances of a Chladni plate. Sand leaves the moving regions and gathers on nodal lines, making each two-dimensional mode visible as a different geometric pattern.
```

```{openlyceum} Resonance
:screens: 4
:placeholder: ../images/ch12-chladni.png
:label: fig:ch12-chladni
:sim-name: Resonance — Chladni patterns
:alt: Four square plates showing nodal-line patterns of increasing complexity, from a simple diagonal cross to an intricate lattice with a star at the center.

Select different resonant frequencies and watch the particles collect along the lines that do not move. Each pattern belongs to one mode, and the number of lines generally rises with the mode number. Violin makers still use the method to check the symmetry of a top or back plate before assembly; an asymmetric pattern means the plate is thicker on one side.
```

```{video} https://www.youtube.com/watch?v=-CZlrgq8syE
:video-title: Seeing Sound With Sand
:label: fig:ch12-seeing-sound-with-sand-video
:alt: Sand rearranges into nodal patterns as a plate is driven at different frequencies.

BBC Earth Science gives a slower explanatory view of the same method, showing why grains migrate away from vibrating regions and settle along the lines that do not move.
```

### Cymbals, Gongs, and the Nonlinear Cascade

A cymbal's modes are so numerous and so closely spaced that by a few hundred hertz the ear cannot resolve them. Its spectrum is effectively continuous, and it is heard as noise.

Something further happens when a cymbal is struck hard, and it is genuinely different physics. The plate's deflection becomes large enough that the restoring force is no longer proportional to displacement, the small-amplitude assumption of [Chapter 1](#ch-sound-and-shm) fails, and the modes stop being independent. Energy fed into low modes **cascades** into higher ones, spreading across the spectrum over a few tenths of a second.

A crash cymbal therefore *blooms*: it does not simply start loud and decay, it starts with a limited spectrum and then fills out, brightening as it goes. It is one of the very few places in this book where superposition genuinely fails, and it is audible.

```{audio} ch12-cymbal
:label: fig:ch12-cymbal
:transcript: A metallic crash that swells slightly after the initial strike and then decays over several seconds, with no pitch in it at all.

A cymbal-like sound built from hundreds of randomly spaced partials. There are no lines to count in the spectrum, and no fundamental for the ear to find, which is the definition of indefinite pitch.
```

```{audio} ch12-real-cymbal
:label: fig:ch12-real-cymbal
:transcript: A real pair of orchestral clash cymbals produces a sharp metallic impact followed by a dense, shimmering decay with no stable pitch.

The real orchestral instrument. Its continuously filled spectrum makes clear
why a list of a few ideal modes cannot capture a cymbal crash. CC0 recording
from VSCO Community Edition.
```

### The Church Bell and Its Five Tuned Partials

A bell is the most remarkable object in this chapter: a three-dimensional shell whose modes have been forced, by centuries of trial and refinement, into deliberate musical relationships.

A tuned bell has five named partials:

```{figure} ../images/ch12-bell-partials.svg
:label: fig:ch12-bell-partials
:alt: Five labeled vertical bars at frequency ratios 0.5, 1.0, 1.2, 1.5 and 2.0, named hum, prime, tierce, quint and nominal, and annotated as octave below, the strike note, minor third, fifth and octave above.

The five tuned partials of a church bell. Four are placed on consonant intervals; the **tierce** is deliberately a *minor* third, so bells sound solemn rather than bright, and a major-third bell, which founders can now make, sounds subtly wrong to most listeners.
```

Two things are worth drawing out.

**The strike note is not a partial.** The pitch a listener assigns to a bell corresponds to the prime, but it is largely constructed by the ear from the nominal, the quint, and higher partials, another missing fundamental. A bell's perceived pitch can be measured, and it does not correspond to any single measured mode.

**The minor third is a choice.** Bell founders tune by turning the bell on a lathe and removing metal from the inside at specific heights, each of which affects different modes by different amounts. The traditional tierce is minor, and Dutch founders in the 1980s worked out how to produce a major-third bell. It sounds, to ears raised on the traditional kind, slightly wrong, which is a nice demonstration that expectation is doing work alongside acoustics.

```{audio} ch12-bell
:figure: ../images/ch12-bell-partials.svg
:label: fig:ch12-bell-audio
:transcript: A bell strike: an initial clang containing many partials, resolving over several seconds into a steady low hum tone as the higher partials fade.

A bell with the five tuned partials and several above them. Listen to the *change* rather than the sound: the high partials die first, so the clangorous strike settles into the hum tone. That evolution is what makes a bell sound like a bell.
```

## Tuning the Untunable

### Three Strategies

Percussion instruments with definite pitch are made so by one of three strategies. They are named together here because the whole chapter is instances of them.

**Move the modes.** Undercut a bar, turn a bell on a lathe, load a membrane with air. This is direct and it is what most tuned percussion does.

**Suppress the modes that do not fit.** Strike a timpano off-center to avoid the $(0,1)$ piston mode. Support a bar at the fundamental's nodes.

**Exploit the missing fundamental.** Arrange for several partials to be harmonics of a note that is not there, and let the ear construct it. Timpani, tubular bells, and church bells all do this.

### Pitch Where the Spectrum Is Inharmonic

"Pitch" for these instruments is not quite what it means for a violin.

For a harmonic instrument, the pitch is the fundamental, and the partials agree unanimously about what it is. For an inharmonic one, the partials disagree, and the perceived pitch is a **best compromise** the auditory system arrives at. It can therefore be ambiguous, some listeners hear a bell an octave away from others, and it can depend on how loud the sound is and what came before it.

This is not a defect of hearing. It is what happens when a mechanism evolved to group harmonically related partials is presented with partials that are not harmonically related, and the fact that it produces any answer at all is impressive.

### The Steelpan as a Modern Solution

The steelpan, developed in Trinidad in the 1940s, is the newest acoustic instrument in this book and a genuine addition to the strategies above.

A section of oil drum is hammered into a concave dish, and distinct areas of the surface are shaped into **individual note regions**. Each region is a local resonator, tuned to a note, and the skill of the pan tuner is in shaping each so that its own second and third modes fall on the octave and twelfth above its fundamental.

So the steelpan turns one inharmonic plate into many nearly harmonic vibrators, and it does so by geometry alone, no undercutting, no air loading, no exploiting a missing fundamental. It is the best evidence in this chapter that tuned percussion is an engineering problem rather than a natural category, and that the problem is still being solved in new ways.

## Summary

- **Two-dimensional and stiffness-controlled vibrators have inharmonic modes.** A circular membrane's are set by Bessel zeros ($1: 1.59: 2.14: 2.30: \ldots$); a free-free bar's by the roots of $\cos x\cosh x = 1$ ($1: 2.76: 5.40: \ldots$).
- **Inharmonic partials give indefinite pitch**, because the pattern-matching mechanism of [Chapter 8](#ch-pitch-and-consonance) finds no fundamental that explains them.
- **Undercutting a bar** removes material at the center, where the fundamental has an antinode and the second mode a node, lowering the first far more than the second. Xylophone bars are tuned to $3f_1$, marimba bars to $4f_1$.
- **Bars are supported at the fundamental's nodes**, about $22\%$ from each end, so that holding them does not damp the note.
- **A timpano's kettle loads the modes unequally**, moving them into the near-harmonic set $1: 1.5: 2: 2.5: 3$. The perceived pitch is a **missing fundamental** an octave below the lowest of these.
- **Striking a timpano a quarter of the way in** suppresses the $(0,1)$ piston mode, which is the loudest radiator and the one that does not fit the series.
- **Chladni figures** show nodal lines directly, and are still used to check the symmetry of violin plates.
- **A hard-struck cymbal is nonlinear**: energy cascades from low modes into high ones over a few tenths of a second, which is the audible "bloom".
- **A tuned bell has five named partials**, hum, prime, tierce, quint, nominal, placed deliberately, with the tierce a *minor* third by tradition. The strike note is a construction of the ear rather than a measured mode.
- **Tuned percussion uses three strategies**: move the modes, suppress the ones that do not fit, or exploit the missing fundamental. The steelpan adds a fourth by making many small resonators out of one plate.

## Check Your Understanding

Five short, auto-graded questions cycle within one compact activity. One question uses the chapter’s Chladni-pattern figure as a visual prompt.

:::{h5p} ch12-chapter-review
:label: check:ch12-chapter-review
:title: Chapter 12 interactive review

1. **Multiple choice.** Where should a free-free bar be supported to preserve its fundamental vibration: the center antinode, both ends, or the nodes about $22\%$ from each end?
2. **Visual true or false.** In a Chladni pattern, sand collects along antinodes where the plate moves most.
3. **Drag the words.** Match the initial modal-frequency ratios $1:2$, $1:2.76$, $1:1.59$, and $1:1.5$ to an ideal string, free-free bar, circular membrane, and timpano.
4. **Fill in the blanks.** The perceived timpani pitch is a ___ fundamental one ___ below its lowest prominent partial.
5. **Mark the words.** Identify the five named bell partials: “The five named partials are hum, prime, tierce, quint, and nominal; the traditional tierce is a minor third.”
:::

## Conceptual Questions

1. Explain why a one-dimensional string has harmonic modes and a two-dimensional membrane does not, without invoking Bessel functions by name.

2. A drum and a violin are struck and bowed respectively. Explain why one has a definite pitch and the other does not, in terms of what the ear is trying to do.

3. Explain why removing wood from the center of a marimba bar lowers the fundamental much more than the second mode.

4. Explain why a marimba bar is supported at about $22\%$ of its length from each end rather than at the ends themselves.

5. A timpanist strikes about a quarter of the way in from the rim rather than at the center. Give two reasons.

6. The pitch a listener assigns to a timpano corresponds to no mode of the instrument. Explain how this can be.

7. A glockenspiel's bars are not undercut and yet it sounds pitched. Explain why it gets away with it.

8. Explain what is happening in a hard-struck cymbal that does not happen in a lightly struck one, and why this violates an assumption made throughout the book.

## Problems

:::{exercise}
:label: ex-percussion-1

*(Straightforward)* A circular membrane's lowest mode is at $180$ Hz. Using the ratios $1$, $1.59$, $2.14$, $2.30$, $2.65$: (a) Find the next four mode frequencies. (b) Is there any fundamental of which these are all harmonics?
:::

:::{solution} ex-percussion-1
:label: sol-percussion-1
:class: dropdown

(a) Multiplying through:

$$
286\ \text{Hz},\quad 385\ \text{Hz},\quad 414\ \text{Hz},\quad 477\ \text{Hz}.
$$

(b) No. For these to be harmonics of some $f_0$, every ratio between them would have to be a ratio of small whole numbers. But $286/180 = 1.59$, and $1.59$ is not a ratio of small integers: the nearest is $8/5 = 1.60$, and even accepting that, $2.14$ and $2.30$ cannot be fitted to the same $f_0$ consistently.

Therefore there is no fundamental, the ear's pattern matcher returns nothing, and the membrane has no definite pitch.
:::

:::{exercise}
:label: ex-percussion-2

*(Moderate)* A marimba bar's plain modes are at $262$, $722$, and $1416$ Hz. (a) Express the ratios. (b) After undercutting, the second mode is at $1048$ Hz. What ratio is that? (c) What musical interval?
:::

:::{solution} ex-percussion-2
:label: sol-percussion-2
:class: dropdown

(a) $722/262 = 2.756$ and $1416/262 = 5.405$.

(b) $1048/262 = 4.00$.

(c) A ratio of $4$ is $1200\log_2 4 = 2400$ cents, two octaves exactly.

Therefore the undercutting has moved the second mode from $2.76$ to $4.00$, turning a clashing partial into a consonant one. The shift is $1200\log_2(4/2.756) = 645$ cents, over five semitones of retuning achieved with a gouge.
:::

:::{exercise}
:label: ex-percussion-3

*(Moderate)* A timpano's measured modes are $146$, $219$, $292$, $356$, $423$ Hz. (a) Express them as ratios of the lowest. (b) Show that they are close to harmonics 2 to 6 of a missing fundamental. (c) What is that fundamental, and what note does the listener hear?
:::

:::{solution} ex-percussion-3
:label: sol-percussion-3
:class: dropdown

(a) Dividing by $146$: $1.00$, $1.50$, $2.00$, $2.44$, $2.90$.

(b) Doubling: $2.00$, $3.00$, $4.00$, $4.88$, $5.79$, close to $2, 3, 4, 5, 6$.

(c) The fundamental is $146/2 = 73$ Hz.

Therefore the listener hears about $73$ Hz, D2, which is an octave below the lowest mode present and which the instrument radiates essentially nothing at. The fourth and fifth of these are a little flat of exact harmonics, so a timpano's pitch, while definite, is less crisply defined than a string's.
:::

:::{exercise}
:label: ex-percussion-4

*(Moderate)* A membrane's fundamental is $f_{01} = (\alpha_{01}/2\pi a)\sqrt{T/\sigma}$ with $\alpha_{01} = 2.405$. A timpano head has radius $0.33$ m and mass per unit area $0.26$ kg/m². (a) What tension per unit length gives a fundamental of $146$ Hz? (b) By what factor must the tension change to raise the pitch a whole tone?
:::

:::{solution} ex-percussion-4
:label: sol-percussion-4
:class: dropdown

(a) Rearranging:

$$
T = \sigma\left(\frac{2\pi a f}{\alpha_{01}}\right)^2
= 0.26\left(\frac{2\pi(0.33)(146)}{2.405}\right)^2.
$$

The bracket is $302.7/2.405 = 125.9$, so

$$
T = 0.26(125.9)^2 = 4.12\times10^{3}\ \text{N/m}.
$$

(b) Frequency goes as $\sqrt T$, and a whole tone is a factor $2^{2/12} = 1.1225$:

$$
\frac{T'}{T} = 1.1225^2 = 1.26.
$$

Therefore about $4.1$ kN/m of tension, and a $26\%$ increase for a whole tone: a timpano's pedal therefore has to move a considerable distance, and the instrument's range is limited to about a fifth.
:::

:::{exercise}
:label: ex-percussion-5

*(Moderate)* A xylophone bar's second mode is tuned to $3f_1$ and a marimba bar's to $4f_1$. If both have $f_1 = 440$ Hz: (a) Find each second mode. (b) Which sounds brighter, and why? (c) Which is a more consonant relationship?
:::

:::{solution} ex-percussion-5
:label: sol-percussion-5
:class: dropdown

(a) Xylophone: $1320$ Hz. Marimba: $1760$ Hz.

(b) The **xylophone** sounds brighter, which is initially counterintuitive since its second mode is lower. The reason is relative strength: a partial at $3f_1$ is a twelfth above the fundamental and sits in a region of high ear sensitivity, whereas at $4f_1$ it is two octaves up and, for the same amplitude, contributes less to the sense of a hard, edgy tone. The xylophone's shorter, less deeply cut bars also decay faster, which concentrates the energy into a sharper attack.

(c) Both are exact harmonics and therefore consonant. $4{:}1$ is the simpler ratio and blends more completely into the fundamental, so the marimba sounds warm and unified while the xylophone sounds like a fundamental with a distinct twelfth on top.
:::

:::{exercise}
:label: ex-percussion-6

*(Moderate)* A glockenspiel bar has $f_1 = 2093$ Hz and is not undercut. (a) Where is its second mode? (b) Why does the inharmonicity matter less than it would on a marimba? (c) Estimate how many cents the second mode is from the nearest harmonic.
:::

:::{solution} ex-percussion-6
:label: sol-percussion-6
:class: dropdown

(a) $2093 \times 2.756 = 5768$ Hz.

(b) [Chapter 8](#ch-pitch-and-consonance) showed that pitch perception degrades above about $5$ kHz, where phase locking fails. At $5768$ Hz the partial contributes brightness but the auditory system is not attempting to fit it into a harmonic pattern, so its failure to fit costs nothing.

(c) The nearest harmonic is the third, at $3 \times 2093 = 6279$ Hz:

$$
1200\log_2\!\left(\frac{5768}{6279}\right) = -147\ \text{cents}.
$$

Therefore the second mode is nearly a semitone and a half from the nearest harmonic: an enormous error by the standards of [Chapter 9](#ch-scales-and-tuning), and entirely inaudible as mistuning because of where it falls.
:::

:::{exercise}
:label: ex-percussion-7

*(Straightforward)* A church bell's partials are at $131$, $262$, $314$, $393$, and $524$ Hz. (a) Identify each by name. (b) Express the tierce as an interval above the prime. (c) What would a major-third bell's tierce be?
:::

:::{solution} ex-percussion-7
:label: sol-percussion-7
:class: dropdown

(a) Taking $262$ Hz as the prime: $131$ is the **hum** (an octave below), $262$ the **prime**, $314$ the **tierce**, $393$ the **quint**, $524$ the **nominal** (an octave above).

(b) $314/262 = 1.198$:

$$
1200\log_2(1.198) = 313\ \text{cents},
$$

which is a minor third (the just minor third $6{:}5$ is $316$ cents).

(c) A major third would be $5{:}4$:

$$
262 \times 1.25 = 328\ \text{Hz}.
$$

Therefore this is a conventional minor-third bell, and a major-third bell would need its tierce moved up $14$ Hz, about $73$ cents, which is a great deal of metal to remove from exactly the right place.
:::

:::{exercise}
:label: ex-percussion-8

*(Straightforward)* A timpanist strikes a head at its exact center. (a) Which modes are excited? (b) Which are not? (c) Describe the resulting sound and explain why timpanists never do this.
:::

:::{solution} ex-percussion-8
:label: sol-percussion-8
:class: dropdown

(a) Only the modes with **no nodal diameter**: $(0,1)$, $(0,2)$, $(0,3)$, … These are the circularly symmetric ones, which move at the center.

(b) Every mode with $m \ge 1$, $(1,1)$, $(2,1)$, $(3,1)$, and so on, because all of them have a nodal diameter through the center.

(c) The $(m,1)$ family is precisely the near-harmonic set that gives the timpano its pitch, so striking at the center removes it entirely. What remains is the $(0,n)$ family, whose ratios are $1: 2.30: 3.60$, thoroughly inharmonic, plus the $(0,1)$ piston mode, which radiates very loudly and decays fast.

Therefore a center strike produces a loud, dull, pitchless thud. Timpanists strike about a quarter of the way in precisely to avoid it, which puts the mallet near a node of $(0,1)$ and at a strong antinode of $(1,1)$.
:::

:::{exercise}
:label: ex-percussion-9

*(Challenging)* Show that supporting a free-free bar at $22.4\%$ of its length from each end places the supports at nodes of the fundamental, and explain what would happen if they were placed at the center instead.
:::

:::{solution} ex-percussion-9
:label: sol-percussion-9
:class: dropdown

The fundamental transverse mode of a free-free bar has **two** nodes, symmetrically placed. Solving the bar equation places them at approximately $0.2242L$ and $0.7758L$: that is, at $22.4\%$ from each end.

A support at a node touches the bar where the fundamental is not moving. It therefore removes no energy from that mode, and the note rings.

Supporting at the center would put the support at an **antinode** of the fundamental: the point of maximum motion. The support would absorb energy at the greatest possible rate, and the fundamental would be heavily damped. What would survive is the second mode, which has a node at the center.

Therefore a centrally supported bar would sound its second mode, weakly and briefly, at $2.76$ times the intended pitch. The node placement is not a convenience; it is what makes the instrument work.
:::

:::{exercise}
:label: ex-percussion-10

*(Moderate)* A cymbal is struck softly and then hard. (a) Describe the difference in how the spectrum evolves. (b) Which assumption made throughout this book fails in the second case? (c) Name one other place in the book where the same assumption fails.
:::

:::{solution} ex-percussion-10
:label: sol-percussion-10
:class: dropdown

(a) Struck softly, the cymbal behaves linearly: the modes excited by the strike ring and decay independently, and the spectrum only ever gets thinner. Struck hard, energy transfers *between* modes after the strike, so the spectrum broadens over a few tenths of a second before it decays: the sound blooms.

(b) **Superposition** ([Chapter 3](#ch-superposition)), which requires the restoring force to be proportional to displacement. At large deflection a plate's restoring force is not, and the modes cease to be independent.

(c) A brass instrument played very loudly ([Chapter 11](#ch-wind-instruments)): the wave steepens as it travels down the bore, because compressions travel faster than rarefactions, adding brightness to a fortissimo that is not present at lower dynamics.

Therefore nonlinearity is rare in this book but not absent, and in both cases it is audible and musically useful rather than a defect.
:::

:::{exercise}
:label: ex-percussion-11

*(Moderate)* A steelpan note region has a fundamental of $392$ Hz. Its tuner aims to place the second and third modes on the octave and the twelfth. (a) What frequencies are those? (b) Explain why this makes the note pitched. (c) Contrast the strategy with the timpani's.
:::

:::{solution} ex-percussion-11
:label: sol-percussion-11
:class: dropdown

(a) Octave: $784$ Hz. Twelfth: $1176$ Hz.

(b) The three modes are then at $1: 2: 3$ times $392$ Hz: an exact harmonic series. [Chapter 8](#ch-pitch-and-consonance)'s pattern matcher finds $392$ Hz immediately and unambiguously, and the note has a pitch as clear as a string's.

(c) The timpani places its modes at $2: 3: 4: 5: 6$ of a fundamental that is **not present**, and relies on the ear to construct it. The steelpan places its modes at $1: 2: 3$ with the fundamental **present and strong**. The steelpan's is the more direct solution and gives a clearer pitch; the timpani's is forced on it by the fact that a membrane's lowest mode cannot be moved into the series.

Therefore the two instruments solve the same problem by different strategies from §12.5, and the difference in clarity of pitch between them is audible.
:::

:::{exercise}
:label: ex-percussion-12

*(Moderate)* A bar's mode frequencies scale as $f \propto h/L^2$, where $h$ is thickness and $L$ length. A marimba bar sounds $262$ Hz. (a) What length would sound $131$ Hz at the same thickness? (b) Why is this a problem, and what do makers do instead?
:::

:::{solution} ex-percussion-12
:label: sol-percussion-12
:class: dropdown

(a) Since $f \propto 1/L^2$, halving the frequency requires

$$
L' = L\sqrt{2} = 1.414\,L.
$$

(b) That is only a $41\%$ increase in length for a whole octave, which sounds convenient until you notice the consequence for the instrument's **range**. Five octaves would need a length ratio of $(\sqrt2)^5 = 5.7$, so if the top bar is $12$ cm the bottom is $68$ cm, which is manageable. The real problem is the other direction: to keep the bars a reasonable width and the instrument playable, the low bars must also be made **thinner**, and a thin bar is fragile and radiates poorly.

Makers therefore combine the levers: low bars are longer, thinner, and more deeply undercut, and a resonator tube is tuned beneath each to make up the radiation the thin bar cannot provide on its own.

Therefore the scaling law explains the shape of a marimba directly, and the resonator tubes exist because the scaling alone would leave the bass inaudible.
:::

:::{exercise}
:label: ex-percussion-13

*(Challenging)* Explain why a gamelan ensemble sounds in tune to a listener familiar with it and out of tune to one who is not, using this chapter and [Chapter 8](#ch-pitch-and-consonance) together.
:::

:::{solution} ex-percussion-13
:label: sol-percussion-13
:class: dropdown

Gamelan instruments are metallophones and gongs: bars, plates and shells, whose partials are inharmonic in the ratios this chapter has been describing.

[Chapter 8](#ch-pitch-and-consonance) showed that the consonance of an interval is not a property of its ratio but of whether the two tones' *partials* coincide or clash. For instruments with harmonic partials, the intervals that make partials coincide are the simple ratios, and the Western scale sits on them. For instruments with inharmonic partials, the intervals that make partials coincide are somewhere else, and the slendro and pelog scales sit on those.

So a gamelan is in tune *for its own instruments*. Played on a piano, its intervals would clash, because the piano's partials are harmonic and the coincidences would not occur. Played on gamelan instruments, the Western scale would clash for the same reason in reverse.

A listener's judgment follows what they are used to hearing, and both judgments are correct about different things: the unfamiliar listener is hearing a real acoustic mismatch between the intervals and their *expectations*, which were formed on harmonic instruments.

Therefore neither tradition is approximating the other. Each has chosen intervals that minimize roughness for the instruments it actually has, which is the same procedure producing different answers.
:::

:::{exercise}
:label: ex-percussion-14

*(Moderate)* A tubular bell's strong partials are at $436$, $654$, and $872$ Hz. (a) Express them as ratios of the lowest. (b) Find the missing fundamental. (c) Does the tube have a mode at that frequency? (d) Comment on what this means for how the instrument is notated.
:::

:::{solution} ex-percussion-14
:label: sol-percussion-14
:class: dropdown

(a) $1.00: 1.50: 2.00$.

(b) Multiplying by two gives $2: 3: 4$, so these are harmonics 2, 3 and 4 of

$$
f_0 = \frac{436}{2} = 218\ \text{Hz}.
$$

(c) No. A tube's modes are in the inharmonic ratios of a bar, and $218$ Hz corresponds to none of them; the tube does not vibrate there and radiates essentially nothing there.

(d) The instrument is notated, played, and conducted at $218$ Hz: a note that exists only in the listener's auditory system. A microphone at the bell would find no energy at the written pitch.

Therefore tubular bells are a case where the *musical* fact and the *acoustic* fact genuinely differ, and the musical fact is the one everyone acts on. It is the same situation as the brass pedal tone in [Chapter 11](#ch-wind-instruments) and the organ's resultant stop in [Chapter 8](#ch-pitch-and-consonance).
:::
