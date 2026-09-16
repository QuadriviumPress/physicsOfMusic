---
title: "String Instruments: Guitar, Violin, and Piano"
short_title: "Chapter 10. String Instruments: Guitar, Violin, and Piano"
label: ch-string-instruments
numbering:
  enumerator: "10.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 10.1, 10.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-10-string-instruments.pdf
    chapter: 10
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Calculate the fundamental frequency of a string from its length, tension, and linear density, and predict the effect of changing each.
- Explain why a bass string is wound rather than simply made thicker or slacker.
- Explain how the point and the manner of excitation determine which harmonics are strong, and predict the spectral effect of plucking a guitar string near the bridge rather than over the soundhole.
- Describe Helmholtz motion of a bowed string, and explain how the stick-slip mechanism sustains it.
- Explain why a string alone radiates almost no sound, and describe how the bridge and body solve the impedance-matching problem.
- Describe the principal resonances of a guitar body, including the Helmholtz air resonance, and explain what each contributes.
- Explain inharmonicity in piano strings, identify its cause in string stiffness, and connect it to stretched piano tuning.
- Explain why piano strings are struck at about one-seventh of their length, and why the piano uses multiple strings per note.
- Compare the three instrument families in terms of how energy enters the string, how long it stays, and how it leaves.

### Introduction

Part V takes the machinery of the first nine chapters and applies it to instruments, one family at a time. Each chapter asks the same three questions:

1. **What vibrates?**
2. **How is energy put into it?**
3. **How does the vibration reach the air?**

For string instruments, the first answer is already known. [Chapter 3](#ch-superposition) derived the modes of a string fixed at both ends, and found $f_n = (n/2L)\sqrt{T/\mu}$: a complete harmonic series, so a string has a definite pitch and a good one.

The other two questions are where the instruments differ, and where the interesting physics lies.

The **second** question, how energy gets in, turns out to control the timbre almost entirely. [Chapter 4](#ch-resonance) showed that a pluck decomposes into modes, and that the pluck point determines which. Plucking, bowing, and striking excite quite different spectra from the same string, and within each, exactly where you do it matters as much as how hard.

The **third** question is a problem rather than a mechanism. A vibrating string, on its own, is almost silent. [Chapter 2](#ch-wave-motion) gave the reason: the impedance mismatch between a thin dense string and thin light air is enormous, and almost no energy crosses. Everything else about a string instrument, the bridge, the body, the soundboard, the shape, the wood, exists to solve that problem, and the solutions are what make a guitar sound different from a violin.

## The Vibrating String

### Frequency, Length, Tension, and Mass

The governing formula, from [Chapter 3](#ch-superposition):

$$
f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}.
$$

Three levers, and each has a characteristic use.

**Length** is the player's lever. A finger on a fingerboard or a fret shortens the string, and pitch goes as $1/L$: the only one of the three that is a simple inverse, and so the only one suited to rapid, accurate, continuous control.

**Tension** is the tuner's lever. Pitch goes as $\sqrt{T}$, so an octave costs four times the tension. Strings already run close to their breaking stress, so this lever has very little travel, which is exactly what makes it good for fine tuning.

**Mass per unit length** is the maker's lever. Pitch goes as $1/\sqrt{\mu}$, so a string four times as heavy sounds an octave lower at the same length and tension.

::::{tip} Worked example: why bass strings are wound
*A guitar's high E string is $0.25$ mm in diameter. Its low E is two octaves lower, at the same length and a similar tension. How thick would a plain steel string need to be, and what goes wrong?*

Two octaves is a factor of four in frequency, so $\mu$ must rise by a factor of $16$. For a solid cylinder $\mu \propto d^2$, so the diameter must rise by $\sqrt{16} = 4$:

$$
d = 4 \times 0.25\ \text{mm} = 1.0\ \text{mm}.
$$

That is a steel rod a millimeter thick. Two things go wrong with it.

**It is far too stiff to bend.** [Chapter 5](#ch-fourier-and-timbre) showed that stiffness makes the partials inharmonic, and the inharmonicity coefficient rises steeply with diameter: a $1$ mm plain string would be audibly and unpleasantly out of tune with itself.

**It will not bend over the bridge or turn round a tuning peg** without taking a permanent set.

The solution is a **wound** string: a thin, flexible core carrying the tension, with a heavy wire wrapped loosely around it adding mass. The winding contributes $\mu$ without contributing bending stiffness, because the turns are free to move relative to one another. A wound low E achieves the sixteenfold mass with a core no thicker than about $0.4$ mm.
::::

```{phet} wave-on-a-string
:label: fig:ch10-wave-on-a-string-sim

Pluck a string and watch the pulse reflect. Two things are worth doing
deliberately: switch the far end between fixed and loose and confirm the
inversion of [Chapter 3](#ch-superposition), and then set the damping to zero and
drive the string to see the standing-wave modes appear one at a time.
```

### The Mode Shapes

The modes are $\sin(n\pi x/L)$, and [Chapter 4](#ch-resonance) established the rule that matters most for what follows:

> **Exciting the string at a point excites only those modes that move at that point.**

Since the $n$th mode has nodes at $x = L/n, 2L/n, \ldots$, touching or driving at $L/n$ affects mode $n$ not at all.

### Real Strings: Stiffness and Inharmonicity

An ideal string resists only stretching. A real one also resists **bending**, and that extra restoring force stiffens the high modes more than the low ones, because they are more sharply curved. [Chapter 5](#ch-fourier-and-timbre) gave the result:

$$
f_n = nf_1\sqrt{1 + Bn^2}.
$$

The coefficient $B$ grows with the fourth power of the string's diameter and falls with the square of its length, so **short thick strings are the worst**. That combination describes the extremes of a piano, and §10.6 follows the consequence.

## Setting the String in Motion

### Plucking: Where You Pluck Is What You Hear

A pluck displaces the string into a triangle and releases it. [Chapter 4](#ch-resonance) derived the mode amplitudes:

$$
c_n \propto \frac{1}{n^2}\,\sin\!\left(\frac{n\pi a}{L}\right),
$$

with $a$ the distance of the pluck from one end.

Two factors, doing two different jobs. The $1/n^2$ makes high harmonics weak whatever you do, this is why a plucked string is not harsh. The $\sin(n\pi a/L)$ is the interesting one: it vanishes whenever $a = L/n$, so **plucking at $L/n$ removes the $n$th harmonic and all its multiples**, and it also tilts the whole spectrum according to where $a$ is.

```{figure} ../images/ch10-pluck-position.svg
:label: fig:ch10-pluck-position
:alt: Three columns, each showing a triangular pluck shape above the resulting harmonic spectrum. Plucking at the middle removes all even harmonics; plucking at one fifth removes the fifth and tenth; plucking near the bridge leaves all harmonics strong and flat.

Three pluck positions on one string. At the middle, every even harmonic vanishes and the tone is hollow and mellow. At $L/5$, only the 5th and 10th are lost. Near the bridge, no low harmonic is suppressed and the high ones are relatively strong, which is the bright, thin, nasal sound.
```

```{audio} ch10-pluck-middle, ch10-pluck-fifth, ch10-pluck-bridge
:names: At the middle, At L/5, Near the bridge
:figure: ../images/ch10-pluck-position.svg
:label: fig:ch10-pluck-audio
:transcript: The same string plucked three times. The first is soft and hollow; the second full and balanced; the third thin, bright and nasal, like a harpsichord.

The same string, the same pitch, the same loudness, three right-hand positions. A guitarist's right hand moves as much as the left for that reason, and it is [Chapter 4](#ch-resonance)'s mode-decomposition made audible.
```

The guitar vocabulary follows directly: *sul tasto* or "over the fingerboard" means plucking near the middle for a mellow sound; *sul ponticello* or "at the bridge" means plucking near the end for a bright one.

### Bowing and Helmholtz Motion

Bowing is not plucking repeated. It is a genuinely different mechanism, and the first person to work out what actually happens was Helmholtz, using a vibration microscope.

The intuition that the bow drags the string smoothly along is wrong. What happens instead is **stick–slip**:

1. The rosined bow hair grips the string by static friction and carries it along at the bow's speed.
2. The string's restoring force grows until it exceeds what static friction can hold.
3. The string breaks free and slips back rapidly, in the opposite direction, past the bow.
4. The bow catches it again, and the cycle repeats.

The remarkable part is the *shape* the string takes while this happens.

```{figure} ../images/ch10-helmholtz-motion.svg
:label: fig:ch10-helmholtz-motion
:alt: Left, a string drawn at five instants, in each case as two straight segments meeting at a kink, with the kink at successive positions along a dashed parabolic envelope. Right, the string's velocity at the bow, holding constant at bow speed and then dropping sharply for a brief slip once per period.

**Helmholtz motion.** At every instant the string is exactly two straight lines meeting at a sharp kink, and the kink travels around a parabolic envelope once per period. The right panel shows the consequence at the bow: the string moves with the bow for most of the cycle and slips back quickly once, one slip per period, which is what sets the pitch.
```

Two consequences follow, and both matter.

**The pitch is set by the string, not by the bow.** One slip occurs per round trip of the kink, and that round trip takes exactly one period of the fundamental. Bow speed and pressure change the loudness and the timbre; they do not change the pitch.

**The spectrum is a sawtooth.** The force the string applies to the bridge is proportional to the string's slope there, and the kink passing the bridge makes that slope jump abruptly once per cycle. A sawtooth contains every harmonic, falling as $1/n$, much richer than a pluck's $1/n^2$, so a bowed note is brighter and more penetrating than a plucked one.

```{audio} ch10-bowed, ch10-plucked
:names: Bowed, Plucked
:figure: ../images/ch10-bowed-vs-plucked.svg
:label: fig:ch10-bowed-vs-plucked
:transcript: The same pitch twice. The first grows in, holds steady and is bright and sustained; the second starts immediately and dies away, and is mellower.

The same string, excited two ways. Note that two things differ, and they are independent: the envelope (sustained against decaying) and the spectrum ($1/n$ against $1/n^2$). A synthesizer that gets one right and the other wrong is instantly recognizable as wrong.
```

:::{note}
Helmholtz motion only establishes itself within a certain range of bow force and bow position, mapped out by John Schelleng in 1973. Too little force and the string never sticks: the result is a whistling, unfocused sound called *surface sound*. Too much and the string sticks too long, producing a raucous crunch. The window narrows sharply as the bow moves toward the bridge, which is precisely why *sul ponticello* is difficult to control and why beginners sound scratchy.
:::

### Striking: The Hammer and the Contact Time

A piano hammer is the third mechanism. It differs from a pluck in two ways that both matter.

**The contact time is finite.** A hammer stays on the string for a millisecond or two, long enough to span a significant fraction of the period of the high harmonics. Any harmonic whose half-period is shorter than the contact time is suppressed, because the hammer is still there when it tries to come back. The hammer therefore acts as a low-pass filter, and a soft hammer, which stays in contact longer, produces a mellower note than a hard one.

**The hammer is nonlinear.** Felt compresses stiffer the harder it is squeezed, so a loud blow has a shorter contact time than a quiet one. The consequence is that **a piano played louder is also brighter**, not merely louder: a coupling between dynamics and timbre that is a large part of what the instrument is expressive with.

## From String to Air

### The Impedance Problem Restated

Now the third question. A string moving in air pushes very little air: it is thin, so it cuts through rather than driving, and the air offers almost no resistance to being pushed. In the language of [Chapter 2](#ch-wave-motion), the string's impedance is far higher than the air's, so almost all the energy reflects back into the string.

```{figure} ../images/ch10-impedance-chain.svg
:label: fig:ch10-impedance-chain
:alt: Four circles connected by arrows, labeled string with high impedance, bridge coupling the two, soundboard large and light with low impedance, and air with very low impedance.

The chain. No single step bridges the gap between a steel string and open air; the instrument steps down the impedance in stages, and each stage is a piece of the instrument a maker can adjust.
```

A useful check on how bad the mismatch is: an electric guitar has a solid body and therefore an almost perfect mismatch. Unplugged, it is barely audible, and it sustains for a very long time, because the energy has nowhere to go. That is [Chapter 4](#ch-resonance)'s trade-off in its purest form.

### The Bridge

The **bridge** is the coupling element, and it does two jobs.

It **transmits** the string's transverse force to the top plate. The string's tension pulls down over the bridge, and as the string vibrates, that downward force varies, driving the plate.

It **filters**. A bridge has mass and stiffness of its own, so it has resonances, and it passes some frequencies better than others. A violin bridge has a strong resonance around $3$ kHz, the **bridge hill**, which lands squarely in the region of greatest hearing sensitivity ([Chapter 7](#ch-loudness)) and contributes a good deal of the violin's carrying power.

Bridge design is therefore a filter-design problem, and violin makers adjust it by carving: thinning the bridge's waist lowers its resonance, and cutting away the "kidneys" changes its coupling.

### Soundboards, Bodies, and Radiation

The **soundboard** is the actual radiator. Its job is to present a large, light surface to the air.

- **Large**, because a small source radiates poorly at low frequencies: the wavelengths involved are meters and a small body cannot get a grip on them ([Chapter 2](#ch-wave-motion)).
- **Light**, because a heavy plate is hard for the string to drive.
- **Stiff**, because a floppy plate will not move as a unit.

Light and stiff are contradictory in most materials, and this is why instrument soundboards are made of spruce and have been for five hundred years. Spruce has an exceptionally high stiffness-to-density ratio along the grain, and [Chapter 2](#ch-wave-motion) noted that sound travels along the grain some four times faster than across it. Soundboards are cut with the grain running the length of the instrument for exactly that reason.

## The Guitar

### Scale Length, Frets, and Intonation

A guitar's frets are placed so that stopping at fret $n$ shortens the string by a factor of $2^{n/12}$: each fret is a semitone, and the twelfth fret sits at exactly half the string length.

The scheme has a systematic error. Pressing a string to a fret **stretches** it slightly, raising its tension and therefore its pitch. The effect is worse higher up the neck, where the string must be pushed further, and worse on thick strings.

The remedy is **compensation**: the bridge saddle is set slightly *further* from the nut than the theoretical scale length, and by a different amount for each string, so that the stretching error cancels. Look at an electric guitar's bridge and the six saddles are visibly staggered, that stagger is this correction.

### Body Resonances and the Helmholtz Air Mode

A guitar body's response is not flat.

```{figure} ../images/ch10-body-response.svg
:label: fig:ch10-body-response
:alt: A response curve for a guitar body on logarithmic frequency axes, showing three isolated peaks below 300 Hz labeled air, top plate and back plate, and a dense forest of overlapping peaks above 400 Hz.

A guitar body's frequency response. Below about $300$ Hz there are a few isolated, individually identifiable modes. Above it, the modes become so numerous and closely spaced that they merge into a lumpy continuum. Makers can tune the low modes deliberately; the forest above can only be influenced statistically.
```

The lowest peak is the **Helmholtz air resonance** of [Chapter 4](#ch-resonance): the body cavity and soundhole acting as a mass of air bouncing on a spring of air, typically around $100$ Hz on a steel-string guitar. It is deliberately placed near the bottom of the instrument's range, where the top plate alone radiates poorly, and it is why a guitar has a soundhole rather than merely a hollow body.

Above it come the plate modes: the top plate flexing, the back plate flexing, and the two coupled through the air and through the sides.

### Why Two Guitars Sound Different

Everything in this chapter so far applies equally to any guitar. What distinguishes one instrument from another is almost entirely the **filter**: the placement, strength, and $Q$ of the body's resonances.

The bracing pattern under the top plate is therefore the central object of guitar design, and makers argue about it. The braces set the top's stiffness distribution, which sets its mode shapes and frequencies, which sets the filter. Thin a brace by half a millimeter and the filter changes.

It is also why the argument is hard to settle. [Chapter 4](#ch-resonance)'s trade-off is unavoidable, bracing for volume costs sustain and evenness, and different makers and players weigh those differently.

## The Violin Family

### Bowing in Practice

A violinist controls three things continuously: bow **speed**, bow **force**, and the bow's **distance from the bridge**. Together they determine where the note sits in Schelleng's diagram, and therefore both its loudness and its timbre.

The rule of thumb is that these three must be traded against one another. Playing close to the bridge permits a very loud, bright tone but demands high force and allows little error. Playing over the fingerboard is forgiving and produces a flute-like sound that cannot be made loud.

### The Bridge, the Soundpost, and the Bass Bar

Inside a violin are two pieces of wood that do not touch the strings and are essential.

The **soundpost** is a spruce dowel wedged between the top and back plates under the treble foot of the bridge. It does two things at once. Structurally, it resists the downward force of the strings, some $90$ N pressing on the bridge. Acoustically, it pins one foot of the bridge so that the bridge **rocks** about it rather than moving up and down as a whole, which is what converts the string's motion into an efficient drive of the top plate. Moving a soundpost by half a millimeter audibly changes an instrument, and it is the first thing a luthier adjusts.

The **bass bar** is a spruce strip glued under the top on the bass side. It stiffens the plate lengthwise, spreads the bridge's drive along the instrument, and lowers the frequency of the important low modes.

### The Bridge Hill, Air Modes, and the Wolf Note

Three named features of the violin's response are worth knowing.

The **air mode** near $280$ Hz is the Helmholtz resonance of the body through the f-holes, and it supports the bottom of the instrument's range, close to the open G string.

The **bridge hill** near $3$ kHz is the bridge's own resonance, and it is the violin's projection. It coincides with the ear's most sensitive region and with the singer's formant of [Chapter 13](#ch-the-singing-voice), several unrelated traditions have independently converged on putting energy at $3$ kHz, because that is where the ear is listening.

The **wolf note** is a defect rather than a feature. If a strongly radiating body resonance lies at the same frequency as a note the player wants, the body absorbs energy from the string so efficiently that the string cannot maintain steady Helmholtz motion. The two alternately grab the energy, and the result is a stuttering, howling note, usually around E or F on a cello. The standard remedy is a **wolf eliminator**, a small mass clamped to the string beyond the bridge, which splits the offending resonance into two weaker ones on either side.

## The Piano

### A String Under Great Tension

A modern piano is an extreme instrument. Its strings carry a total tension of around $200$ kN, some twenty tonnes, so it needs a cast-iron frame, and the modern piano could not exist before the industrial techniques to cast one.

The range is seven and a quarter octaves, a factor of $150$ in frequency, and the formula $f = (1/2L)\sqrt{T/\mu}$ cannot cover that with length alone: the lowest string would have to be over ten meters. So all three levers are used at once: the bass strings are longer, heavier (wound), and at somewhat lower tension.

### Hammers, Strike Point, and Unisons

Piano hammers strike at about $1/7$ to $1/8$ of the string's length, and the choice is deliberate. §10.2's rule says this suppresses the 7th (or 8th) harmonic and its multiples, and the 7th harmonic is $31$ cents flat of any equal-tempered note ([Chapter 9](#ch-scales-and-tuning)), so it clashes with every chord the instrument plays. Striking at $L/7$ removes it.

Most notes have **two or three strings** tuned to the same pitch. The reason is not simply loudness: three strings give $10\log_{10}3 = 4.8$ dB, which is a small return for tripling the hardware. The real reason is **sustain**. A single string coupled to a soundboard efficient enough to be loud dies very quickly. Three strings, very slightly detuned and coupled through the bridge, exchange energy back and forth, and the note decays in two stages, a fast initial fall followed by a long, quiet "aftersound". That two-stage decay is one of the most recognizable features of a piano, and the *una corda* pedal, which shifts the action so the hammer strikes fewer strings, changes it deliberately.

### Inharmonicity and Stretched Tuning

Finally, the consequence of §10.1's stiffness.

```{figure} ../images/ch10-railsback.svg
:label: fig:ch10-railsback
:alt: Left, the inharmonicity coefficient against piano key number, high at both ends and lowest around key 35. Right, the Railsback curve, showing tuning deviation from equal temperament reaching about plus thirty cents at the top of the keyboard and minus thirty at the bottom.

Left: string stiffness across the keyboard, worst at the extremes, the bass strings because they are thick, the treble because they are short. Right: the **Railsback curve**, the stretched tuning that results. The curve shown is representative of measured tunings rather than computed from the left panel, since how much a tuner stretches depends on which partials they choose to match.
```

The mechanism: a tuner setting an octave listens for beats between the lower note's **second partial** and the upper note's fundamental. Because of inharmonicity that second partial is *sharp* of twice the fundamental, so a beatless octave is wider than $2{:}1$. Repeat up and down the keyboard and the errors accumulate.

```{audio} ch10-octave-exact, ch10-octave-stretched
:names: Exact 2:1 octave, Stretched octave
:figure: ../images/ch10-stretched-octave.svg
:label: fig:ch10-stretched-octave
:transcript: Two octaves on a simulated piano. The first, tuned to an exact 2:1, has a clear slow beating in it. The second, tuned slightly wide, is still.

The mathematically exact octave is the one that beats. This is the reverse of what a reader expects, and it is the whole justification for the Railsback curve: on an instrument with inharmonic partials, "in tune" means matching the partials that are actually there rather than the ratio that ought to be.
```

A well-tuned concert grand is therefore about $30$ cents sharp at the top and $30$ cents flat at the bottom: a spread of more than half a semitone across the instrument. Nobody hears it as out of tune. Played against an exactly equal-tempered synthesizer, the piano is the one that sounds right.

## Summary

- **A string's modes are harmonic**, $f_n = (n/2L)\sqrt{T/\mu}$. Length is the player's lever ($1/L$), tension the tuner's ($\sqrt{T}$, so an octave costs four times), mass the maker's ($1/\sqrt\mu$).
- **Bass strings are wound** because a plain string heavy enough would be too stiff, inharmonic and unbendable. Winding adds mass without adding bending stiffness.
- **Pluck position sets the spectrum**: $c_n \propto n^{-2}\sin(n\pi a/L)$, so plucking at $L/n$ removes the $n$th harmonic and its multiples, and plucking near the bridge tilts the spectrum toward the high harmonics.
- **Bowing produces Helmholtz motion**: stick–slip, with the string always two straight lines meeting at a kink that circulates once per period. The pitch is set by the string; the force at the bridge is a sawtooth, giving a $1/n$ spectrum.
- **A hammer's finite contact time low-passes the spectrum**, and felt's nonlinearity shortens contact at higher force, so a piano played louder is also brighter.
- **The impedance mismatch between string and air is the central problem.** Bridge and soundboard step it down; an electric guitar, which does not, is nearly silent and sustains for a very long time.
- **The guitar's lowest body resonance is a Helmholtz air mode** near $100$ Hz. Above about $300$ Hz the body's modes merge into a forest, and what distinguishes two instruments is the shape of that filter.
- **The violin's soundpost makes the bridge rock rather than translate**, which is what couples the string to the plate efficiently. The **bridge hill** near $3$ kHz gives projection, in the ear's most sensitive region.
- **Piano hammers strike at about $L/7$** to suppress the seventh harmonic, which is $31$ cents flat of any key. Multiple strings per note exist mainly for the two-stage decay they produce, not for loudness.
- **Piano tuning is stretched** because string stiffness makes partials sharp: a beatless octave is wider than $2{:}1$, and the accumulated result is the Railsback curve, about $\pm30$ cents at the extremes.

## Conceptual Questions

1. Explain why instruments change pitch mainly by changing length rather than tension, using the exponents in $f = (1/2L)\sqrt{T/\mu}$.

2. Explain why a bass guitar string is wound rather than simply made thicker, giving two distinct reasons.

3. A guitarist plucks near the bridge and the tone becomes bright and thin. Explain this in terms of mode amplitudes rather than by saying "it excites more harmonics".

4. Explain why the pitch of a bowed note does not depend on bow speed, given that bow speed clearly affects loudness.

5. Explain why a bowed note is brighter than a plucked note on the same string, referring to the two spectra.

6. A piano played loudly sounds brighter as well as louder. Explain the mechanism, and say why this would not happen with a rigid hammer.

7. An unplugged electric guitar is quiet and sustains for a long time. Explain both facts with one argument.

8. Explain why the octave that beats on a piano is the mathematically exact one, and what a tuner does instead.

## Problems

:::{exercise}
:label: ex-string-instruments-1

A guitar string is $64.8$ cm long with $\mu = 4.3\times10^{-3}$ kg/m, tuned to $110$ Hz. (a) What is its tension? (b) What tension would tune it to $146.8$ Hz?
:::

:::{solution} ex-string-instruments-1
:label: sol-string-instruments-1
:class: dropdown

(a) From $f_1 = (1/2L)\sqrt{T/\mu}$, so $T = \mu(2Lf_1)^2$:

$$
T = (4.3\times10^{-3})\,[2(0.648)(110)]^2 = (4.3\times10^{-3})(142.6)^2 = 87.4\ \text{N}.
$$

(b) Tension goes as $f^2$:

$$
T' = 87.4\left(\frac{146.8}{110}\right)^2 = 87.4(1.781) = 156\ \text{N}.
$$

Therefore about $87$ N and $156$ N. Note that a musical fourth, five semitones, needs nearly double the tension, so this is not how instruments are played.
:::

:::{exercise}
:label: ex-string-instruments-2

A string is plucked at $1/6$ of its length. (a) Which harmonics are absent? (b) If the fundamental is $147$ Hz, what are the frequencies of the two lowest absent harmonics? (c) Where would you pluck to remove the 4th harmonic?
:::

:::{solution} ex-string-instruments-2
:label: sol-string-instruments-2
:class: dropdown

(a) The 6th and its multiples: 6, 12, 18, …

(b) $6 \times 147 = 882$ Hz and $12 \times 147 = 1764$ Hz.

(c) At $L/4$, which is a node of the 4th mode.

Therefore the pluck point acts as a comb, and the guitarist choosing a right-hand position is choosing which teeth of the comb to apply.
:::

:::{exercise}
:label: ex-string-instruments-3

A guitar's high E string is $0.23$ mm in diameter and sounds $330$ Hz. A plain steel string of the same length and tension is wanted at $82.4$ Hz. (a) By what factor must $\mu$ increase? (b) What diameter would that need? (c) Comment.
:::

:::{solution} ex-string-instruments-3
:label: sol-string-instruments-3
:class: dropdown

(a) $f \propto 1/\sqrt\mu$, and $330/82.4 = 4.0$, so

$$
\mu' = 4.0^2\,\mu = 16\,\mu.
$$

(b) For a solid cylinder $\mu \propto d^2$:

$$
d' = \sqrt{16}\,(0.23\ \text{mm}) = 0.92\ \text{mm}.
$$

(c) Nearly a millimeter of solid steel. The inharmonicity coefficient goes as $d^4$, so it would rise by a factor of $16^2 = 256$, making the string audibly inharmonic, and it would be far too stiff to bend over the bridge. Hence winding.
:::

:::{exercise}
:label: ex-string-instruments-4

A violin's A string sounds $440$ Hz, is $32.5$ cm long, and is bowed. (a) How many times per second does the kink complete a round trip? (b) How long does one round trip take? (c) What is the wave speed on the string?
:::

:::{solution} ex-string-instruments-4
:label: sol-string-instruments-4
:class: dropdown

(a) Once per period, so $440$ times per second.

(b) $T = 1/440 = 2.27\times10^{-3}$ s.

(c) The kink travels the length twice in one period:

$$
v = \frac{2L}{T} = 2Lf = 2(0.325)(440) = 286\ \text{m/s}.
$$

Therefore the kink makes $440$ round trips a second at $286$ m/s, which is, as it must be, the same wave speed the standing-wave formula gives.
:::

:::{exercise}
:label: ex-string-instruments-5

A piano hammer is in contact with a string for $1.3$ ms. (a) Which harmonics of a $262$ Hz note have half-periods shorter than the contact time? (b) What does this do to the spectrum? (c) How does a harder hammer change the answer?
:::

:::{solution} ex-string-instruments-5
:label: sol-string-instruments-5
:class: dropdown

(a) The $n$th harmonic has period $1/(262n)$ and half-period $1/(524n)$. Setting this below $1.3$ ms:

$$
\frac{1}{524n} < 1.3\times10^{-3}
\;\Rightarrow\;
n > \frac{1}{524 \times 1.3\times10^{-3}} = 1.47.
$$

So harmonics from the 2nd upward are affected, increasingly so as $n$ rises.

(b) The hammer is still in contact while those harmonics try to reverse, so it damps them. The effect is a low-pass filter whose cutoff is around $1/(2 \times 1.3\ \text{ms}) = 385$ Hz and which rolls off progressively above it.

(c) A harder hammer compresses less and leaves sooner, raising the cutoff and letting more high harmonics through: a brighter note. Voicing a piano is therefore done by pricking the hammer felt with needles to soften it, or by hardening it with lacquer.
:::

:::{exercise}
:label: ex-string-instruments-6

A piano string sounds $110$ Hz with $B = 3.5\times10^{-4}$. (a) Find the frequency of its 2nd partial. (b) To what frequency must the octave above be tuned for a beatless octave? (c) How many cents wide of $2{:}1$ is that?
:::

:::{solution} ex-string-instruments-6
:label: sol-string-instruments-6
:class: dropdown

(a) Using $f_n = nf_1\sqrt{1 + Bn^2}$ with $n = 2$:

$$
f_2 = 220\sqrt{1 + (3.5\times10^{-4})(4)} = 220\sqrt{1.0014} = 220.154\ \text{Hz}.
$$

(b) The upper note's fundamental must match it: $220.154$ Hz.

(c)

$$
1200\log_2\!\left(\frac{220.154}{220}\right) = 1.2\ \text{cents}.
$$

Therefore this octave must be stretched by about $1.2$ cents. A single octave's stretch is small; seven of them, each a little larger than the last as the strings get stiffer, is what produces the Railsback curve.
:::

:::{exercise}
:label: ex-string-instruments-7

A guitar body has a Helmholtz air resonance at $98$ Hz with $Q = 6$, and the guitar's lowest note is $82.4$ Hz. (a) Find the bandwidth. (b) Is the lowest note inside it? (c) Comment on the design choice.
:::

:::{solution} ex-string-instruments-7
:label: sol-string-instruments-7
:class: dropdown

(a) $\Delta f = f_0/Q = 98/6 = 16.3$ Hz, so the half-power band runs from about $89.8$ to $106.2$ Hz.

(b) No: $82.4$ Hz is about $7$ Hz below the lower half-power point.

(c) The resonance sits just *above* the lowest note rather than on it, which is the usual arrangement. Placing it exactly on the lowest note would make that one note boom and the ones above it comparatively weak. Placing it a little higher lets its skirt support the bottom note while the peak reinforces the notes just above, giving a more even bass across several semitones: the low-$Q$ design philosophy of [Chapter 4](#ch-resonance) applied deliberately.
:::

:::{exercise}
:label: ex-string-instruments-8

A cello has a wolf note at $174.6$ Hz (F$_3$). (a) Explain the mechanism. (b) A wolf eliminator of mass $8$ g is fitted to the string beyond the bridge. Explain qualitatively why adding a mass helps.
:::

:::{solution} ex-string-instruments-8
:label: sol-string-instruments-8
:class: dropdown

(a) A strong, well-radiating body resonance coincides with F$_3$. The body absorbs energy from the string so efficiently at that frequency that the string cannot sustain steady Helmholtz motion: the string builds up, dumps energy into the body, loses its stick–slip regime, re-establishes it, and repeats. The result is a stuttering warble at a few hertz.

(b) The eliminator adds a small resonant system coupled to the offending one. Two coupled resonators, as [Chapter 4](#ch-resonance) showed, have two normal modes with frequencies split either side of the original; so the single strong peak at $174.6$ Hz becomes two weaker peaks, neither of which absorbs enough energy to break the Helmholtz regime.

Therefore the fix is not damping the string but splitting the body's resonance, and the mass must be tuned: too light or too heavy and the split is in the wrong place.
:::

:::{exercise}
:label: ex-string-instruments-9

A piano note has three strings, each producing $70$ dB alone. (a) What level do all three give? (b) Why is this a poor argument for having three strings? (c) What is the real reason?
:::

:::{solution} ex-string-instruments-9
:label: sol-string-instruments-9
:class: dropdown

(a) Three incoherent sources add $10\log_{10}3 = 4.8$ dB:

$$
L = 70 + 4.8 = 74.8\ \text{dB}.
$$

(b) Under $5$ dB is barely more than half a doubling of loudness ([Chapter 7](#ch-loudness)), for three times the strings, three times the tension on the frame, and three times the tuning work. As a loudness argument it is feeble.

(c) **Sustain.** A single string coupled tightly enough to the soundboard to be loud would decay very fast. Three slightly detuned strings coupled through the bridge exchange energy with one another, producing a fast initial decay followed by a much longer aftersound. That two-stage decay is what a piano sounds like, and it cannot be had from one string.
:::

:::{exercise}
:label: ex-string-instruments-10

Show that plucking a string at $a = L/2$ removes every even harmonic, and explain why the resulting tone is the mellowest available.
:::

:::{solution} ex-string-instruments-10
:label: sol-string-instruments-10
:class: dropdown

The mode amplitude is $c_n \propto n^{-2}\sin(n\pi a/L)$. With $a = L/2$:

$$
\sin\!\left(\frac{n\pi}{2}\right) =
\begin{cases}
\pm 1 & n \text{ odd}\\
0 & n \text{ even}.
\end{cases}
$$

So every even harmonic vanishes.

The tone is mellowest for two reasons acting together. First, half the partials are gone outright, which removes the octave, the second octave, and so on: the same hollowing that distinguishes a stopped pipe in [Chapter 3](#ch-superposition). Second, the surviving odd harmonics still carry the $1/n^2$ factor, so they are weak: the 3rd is at $1/9$ of the fundamental, the 5th at $1/25$.

Therefore the midpoint pluck gives the fewest and weakest partials of any pluck position, which is what "mellow" means spectrally.
:::

:::{exercise}
:label: ex-string-instruments-11

A violin string is bowed at $1/11$ of its length from the bridge. (a) Which harmonic does this most affect, and how? (b) Helmholtz motion still produces a full harmonic series. Reconcile these two statements.
:::

:::{solution} ex-string-instruments-11
:label: sol-string-instruments-11
:class: dropdown

(a) The bow sits at a node of the 11th mode, so it cannot drive that mode.

(b) The reconciliation is that bowing is a *sustained, nonlinear* process, not a single impulse. The stick–slip cycle is locked to the round trip of the kink, and that round trip forces the whole motion to be periodic at $f_1$. Fourier's theorem ([Chapter 5](#ch-fourier-and-timbre)) then guarantees that a periodic waveform has a complete harmonic series: the 11th harmonic is present because periodicity requires it, even though the bow is not driving it directly.

Therefore the bow position affects the *balance* of the harmonics, and quite strongly, there is an audible weakening around the 11th, but it cannot delete one, as a pluck can. This is a real difference between impulsive and sustained excitation, and it is why the "pluck at a node" rule does not transfer to bowing unchanged.
:::

:::{exercise}
:label: ex-string-instruments-12

A grand piano's strings carry a total tension of $200$ kN. (a) Express this as a mass under gravity. (b) The frame is cast iron with a tensile strength of about $200$ MPa. What cross-sectional area is needed for a safety factor of $4$?
:::

:::{solution} ex-string-instruments-12
:label: sol-string-instruments-12
:class: dropdown

(a) From $F = mg$:

$$
m = \frac{200\times10^{3}\ \text{N}}{9.81\ \text{m/s}^2} = 2.0\times10^{4}\ \text{kg} = 20\ \text{tonnes}.
$$

(b) A safety factor of $4$ means designing to $200/4 = 50$ MPa:

$$
A = \frac{F}{\sigma} = \frac{200\times10^{3}\ \text{N}}{50\times10^{6}\ \text{Pa}} = 4.0\times10^{-3}\ \text{m}^2 = 40\ \text{cm}^2.
$$

Therefore about $40$ cm² of iron in cross-section: a bar roughly $6$ cm square, or the equivalent spread across the frame's several members. A grand piano weighs several hundred kilograms for that reason, and the instrument in its modern form had to wait for industrial iron casting.
:::

:::{exercise}
:label: ex-string-instruments-13

Two guitars are identical except that one has a body $Q$ of $4$ and the other $Q$ of $9$ at its main air resonance. (a) Compare their peak responses and bandwidths. (b) Which will sound more even across the bass register? (c) Which will sustain longer?
:::

:::{solution} ex-string-instruments-13
:label: sol-string-instruments-13
:class: dropdown

(a) Peak response is proportional to $Q$, so the second is $9/4 = 2.25$ times higher at the peak. Bandwidth is $f_0/Q$, so the second's is $4/9 = 0.44$ times as wide.

(b) The first, with $Q = 4$. Its broad, low peak supports a wider range of notes roughly equally; the second boosts a narrow band strongly and leaves the notes either side comparatively weak.

(c) The second. A higher $Q$ means less energy leaving per cycle, which is exactly [Chapter 4](#ch-resonance)'s trade-off, and it means a quieter instrument.

Therefore the choice is between a loud, even guitar and a quieter, more colored one with longer sustain. Neither is correct; makers and players genuinely disagree, and this is what they are disagreeing about.
:::

:::{exercise}
:label: ex-string-instruments-14

A piano tuner stretches each octave by matching the lower note's 2nd partial. Take $B = 2.0\times10^{-4}$, constant. (a) How many cents is one octave stretched? (b) If four octaves are tuned upward in succession from the middle, what is the accumulated deviation at the top? (c) Compare with the $\pm30$ cents of a real Railsback curve, and say why the real answer is larger.
:::

:::{solution} ex-string-instruments-14
:label: sol-string-instruments-14
:class: dropdown

(a) The stretch per octave is the amount the 2nd partial is sharp:

$$
1200\log_2\sqrt{\frac{1 + 4B}{1 + B}}
= 600\log_2\!\left(\frac{1.00080}{1.00020}\right)
= 600(0.000865) = 0.52\ \text{cents}.
$$

(b) Four octaves: $4 \times 0.52 = 2.1$ cents.

(c) Two reasons the real figure is an order of magnitude larger.

First, $B$ is **not** constant. It rises steeply toward both ends of the keyboard, as {numref}`Figure %s <fig:ch10-railsback>` shows, so the top octaves are stretched far more than $0.5$ cents each.

Second, tuners do not only match 2nd partials. Fifths, fourths, and double octaves are checked too, each involving higher partials which are sharper still, and the stretch a tuner settles on reflects all of them.

Therefore the single-partial calculation gives the right mechanism and the wrong magnitude, so the figure plots a measured curve rather than a computed one.
:::
