---
title: "Wave Motion and the Speed of Sound"
short_title: "Chapter 2. Wave Motion and the Speed of Sound"
label: ch-wave-motion
numbering:
  enumerator: "2.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 2.1, 2.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-02-wave-motion-and-the-speed-of-sound.pdf
    chapter: 2
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish transverse from longitudinal waves and identify which each of a string, an air column, and a drumhead supports.
- Apply the relation $v = f\lambda$ to find any one of wave speed, frequency, or wavelength given the other two, and explain which of the three a musician changes when playing a different note.
- Explain why the speed of a wave is set by the medium rather than by the source, and predict what happens to frequency and to wavelength when a sound crosses from one medium into another.
- Calculate the speed of sound in air as a function of temperature, and estimate the pitch error a wind instrument suffers when it is played cold.
- Compare the speed of sound in gases, liquids, and solids using the stiffness-to-density ratio, and explain why sound travels faster in helium than in air.
- Define sound intensity, apply the inverse-square law to a point source in the open air, and explain why it fails indoors.
- Define acoustic impedance and explain, in terms of impedance mismatch, why very little sound crosses from a vibrating string directly into air.
- Describe the Doppler effect for a moving source and for a moving listener, calculate the shifted frequency, and identify where it is heard in music.

### Introduction

```{figure} ../images/open/ch02-tuning-fork-history.jpg
:label: fig:ch02-open-tuning-fork
:alt: A historical illustration of a tuning fork producing visible sound vibrations.

An early illustration of a tuning fork producing a visible sound vibration. Public-domain illustration from *Popular Science Monthly* (1878).
```

[Chapter 1](#ch-sound-and-shm) left a vibrating object pushing on the air next to it. This chapter follows what happens next.

The answer is not obvious. The sound arrives at your ear far faster than any air could get there, and the air that arrives is not the air that left. A trumpet player thirty meters away blows a note, and a fifteenth of a second later you hear it, but the breath that made it is still in the trumpet. Something crossed the room, and it was not a substance.

What crossed the room was a **wave**, and this chapter is about how fast it goes, what it looks like on the way, and what happens to it as it spreads. Three results will be used constantly for the rest of the book. The first is the relation $v = f\lambda$, which connects the frequency a musician cares about to the wavelength the physics cares about. The second is that the speed $v$ is a property of the *medium*, not of the source, not of the frequency, not of how loud the sound is, so an orchestra stays together and a cold clarinet plays flat. The third is that sound spreads out, and spreading has a cost, which is the beginning of the story of why instruments need bodies and bells at all.

## From a Vibration to a Wave

### How a Disturbance Propagates

Return to the row of people standing shoulder to shoulder. Shove the first one and a shove travels down the line. Two questions are worth asking about it.

*What decides how fast the shove travels?* Two things. If the people are **stiff**, they resist being compressed and push back hard: the shove passes quickly. If they are **heavy**, hard to get moving, it passes slowly. Nothing else matters: not how hard you shoved, not how often you shove, not how far down the line you look.

*What decides how far the shove goes?* In an idealized line, nothing; it goes forever. In reality some energy is lost to friction at each step, and the shove fades. Both effects have acoustic counterparts, and the first, speed set by stiffness and inertia, is the one that runs this chapter.

The same reasoning applies to air. Air is stiff because compressing it raises its pressure, and it has inertia because it has mass. The ratio of those two properties fixes the speed of sound, and §2.3 makes the statement quantitative.

### Transverse and Longitudinal

Two kinds of wave appear throughout this book, and every instrument uses both.

```{animation} ch02-transverse-longitudinal
:label: fig:ch02-transverse-longitudinal
:alt: Top, a wavy string with a vertical double arrow showing the string moving across the direction of travel. Bottom, a field of dots bunched and thinned, with a horizontal double arrow showing the air moving along the direction of travel. Both have an arrow showing the wave traveling to the right.
:aspect: 4:3

The two kinds of wave. In a **transverse** wave the medium moves across the direction of travel; in a **longitudinal** wave it moves along it. A guitar string carries transverse waves, the air around it carries longitudinal ones, and the instrument's job is to get energy from the first into the second.
```

The distinction is not cosmetic. It determines what a wave can do: only transverse waves can be polarized, so light can and sound cannot. It also determines what has to happen at a boundary between the two. That handover, from the transverse motion of a string to the longitudinal motion of air, turns out to be the hardest engineering problem in the design of a string instrument, and §2.4 explains why.

:::{margin}
A wave on the surface of water is neither, quite: a floating cork traces a small circle rather than a straight line. Surface waves are a mixture, and a poor analogy for sound even though everyone reaches for them first.
:::

### The Wave Pulse and the Periodic Wave

Shove the row of people once and a single **pulse** travels down it. Shove them rhythmically and a **periodic wave** travels instead: a repeating pattern, moving at the same speed the single pulse would have moved.

A handclap is a pulse. A sung note is a periodic wave. Musically the periodic case is the interesting one, but the pulse is the more fundamental: a periodic wave is what you get by sending pulses one after another, and its speed is the pulse speed. **The speed does not know or care about the frequency.** This is worth stating plainly because it is the single most useful fact in the chapter, and because the exceptions to it, media in which speed *does* depend on frequency, called dispersive media, are rare in air and consequential when they occur. A piano string is mildly dispersive, and [Chapter 10](#ch-string-instruments) shows that this small fact is why pianos are tuned the way they are.

## Wavelength, Frequency, and Wave Speed

### The Relation $v = f\lambda$

A periodic wave has a repeating pattern in space as well as in time. The **wavelength** $\lambda$ is the distance between one crest and the next; the **period** $T$ is the time between one crest and the next passing a fixed point.

In one period, the wave advances exactly one wavelength. So its speed is

$$
v = \frac{\lambda}{T} = f\lambda.
$$

That is the whole derivation, and the equation carries an enormous amount of this book.

```{animation} ch02-wavelength-frequency
:label: fig:ch02-wavelength-frequency
:alt: Three sine waves of different wavelengths drawn one above another against a common distance axis, labeled 110 Hz with wavelength 3.1 m, 220 Hz with 1.6 m, and 440 Hz with 0.78 m.

Three notes in the same air. The speed is the same for all three, $343$ m/s, so a higher frequency must mean a shorter wavelength, in exactly inverse proportion. Doubling the frequency, which is going up an octave, halves the wavelength.
```

Notice the *sizes*. Musical wavelengths in air are comparable to the dimensions of rooms and of people: a low A on a bass is about eight meters long, middle C about $1.3$ m, and the top note of a piccolo about $8$ cm. Sound therefore bends around corners and light does not; bass notes are hard to control in a small room ([Chapter 14](#ch-room-acoustics)); and a loudspeaker that is small compared with a wavelength radiates in all directions while one that is large does not.

::::{tip} Worked example: wavelengths across the piano
*The speed of sound in air at 20 °C is $343$ m/s. Find the wavelengths of the lowest and highest notes on a piano, $27.5$ Hz and $4186$ Hz.*

$$
\lambda_{\text{low}} = \frac{v}{f} = \frac{343\ \text{m/s}}{27.5\ \text{Hz}} = 12.5\ \text{m},
\qquad
\lambda_{\text{high}} = \frac{343\ \text{m/s}}{4186\ \text{Hz}} = 8.2\ \text{cm}.
$$

The lowest note's wavelength is longer than most rooms; the highest note's is the width of a hand. That range, a factor of $152$, is the reason no single loudspeaker driver can reproduce a piano, and the reason bass is the hardest part of a room to get right.
::::

### A Wave Crossing a Boundary

When a wave passes from one medium into another, one of its three quantities is forced to stay the same and the other two must adjust.

**Frequency is conserved.** The far side of the boundary is driven by the near side, wiggle for wiggle; the boundary cannot swallow cycles or invent them. Whatever the frequency was, it still is.

**Speed changes**, because the speed belongs to the medium.

**Wavelength therefore changes too**, since $\lambda = v/f$ with $f$ fixed.

Sound entering water from air quadruples its wavelength, because water carries sound over four times as fast. A singer's note does not become a different note when it reaches a listener underwater; it is the same pitch, stretched out in space.

:::{warning}
It is tempting to think that "the note changes" when sound enters a new medium, because the speed changes and $v = f\lambda$ has $f$ in it. It does not. Fix on what the boundary physically does: it shakes the next medium at the rate it is being shaken, so the conserved quantity is obvious.
:::

### The Wave Equation

Everything above can be compressed into one statement, which is the standard starting point of a more mathematical treatment. Any disturbance $y(x,t)$ that travels at a fixed speed $v$ without changing shape satisfies

$$
\frac{\partial^2 y}{\partial t^2} = v^2\,\frac{\partial^2 y}{\partial x^2}.
$$

This is the **wave equation**. Nothing in the rest of this book requires it, and it will not be used again in the main text; it is stated so the derivation can answer the question "why is the speed what it is?"

:::{dropdown} Where the wave equation comes from, and why $v = \sqrt{T/\mu}$
Take a stretched string of tension $T$ and mass per unit length $\mu$, displaced by a small amount $y(x,t)$, and apply Newton's second law to a short segment between $x$ and $x + \mathrm{d}x$.

The tension pulls on each end of the segment along the string. Because the string is curved, the two pulls do not quite cancel: the vertical components are $T\sin\theta$ at each end, and for small slopes $\sin\theta \approx \tan\theta = \partial y/\partial x$. The net upward force is therefore the *difference* of the slopes at the two ends,

$$
\mathrm{d}F = T\left[\left.\frac{\partial y}{\partial x}\right|_{x+\mathrm{d}x} - \left.\frac{\partial y}{\partial x}\right|_{x}\right]
= T\,\frac{\partial^2 y}{\partial x^2}\,\mathrm{d}x .
$$

The segment's mass is $\mu\,\mathrm{d}x$ and its vertical acceleration is $\partial^2 y/\partial t^2$, so Newton's second law reads

$$
\mu\,\mathrm{d}x\,\frac{\partial^2 y}{\partial t^2} = T\,\frac{\partial^2 y}{\partial x^2}\,\mathrm{d}x,
\qquad\text{that is}\qquad
\frac{\partial^2 y}{\partial t^2} = \frac{T}{\mu}\,\frac{\partial^2 y}{\partial x^2}.
$$

Comparing with the wave equation identifies the speed:

$$
v = \sqrt{\frac{T}{\mu}}.
$$

**Stiffness over inertia, exactly as §2.1 argued.** Tension is what pulls the string back; mass per unit length is what resists being moved. This is the formula [Chapter 3](#ch-superposition) uses to work out the pitch of a string, and it contains no reference to amplitude or frequency: the small-slope approximation is what removes them.

To confirm that the equation really describes traveling waves, substitute $y = f(x - vt)$ for any twice-differentiable $f$. The chain rule gives $\partial^2 y/\partial t^2 = v^2 f''$ and $\partial^2 y/\partial x^2 = f''$, so the equation is satisfied for *any* shape $f$. That is the mathematical statement that a pulse travels without changing shape, and that its speed does not depend on what shape it is.
:::

## What Sets the Speed of Sound

### Stiffness and Inertia

The pattern of the dropdown above is general. For any medium,

$$
v = \sqrt{\frac{\text{stiffness}}{\text{density}}},
$$

where "stiffness" is whatever resists the deformation the wave makes, and "density" is whatever has to be accelerated. For a string it is tension over mass per unit length. For a gas it is the bulk modulus over the mass density. For a solid bar it is Young's modulus over density.

Two consequences follow immediately, and both are counterintuitive on first meeting.

**Denser is slower, other things being equal.** Heavier things are harder to shake. Sound travels faster in helium than in air not because helium is thinner in some vague sense but because it is about seven times less dense while being similarly stiff.

**Stiffer is faster, and stiffness wins.** Steel is eight thousand times denser than air, and sound travels through it seventeen times *faster*, because steel is some two million times stiffer. When a medium is both denser and stiffer, the stiffness usually wins by more.

```{figure} ../images/ch02-speed-in-media.svg
:label: fig:ch02-speed-in-media
:alt: A horizontal bar chart of the speed of sound in carbon dioxide 259, air 343, helium 965, water 1482, spruce along the grain 3800, and steel 5960 meters per second.

The speed of sound in six media. The ordering is not by density. Steel is the densest thing here and the fastest, so the order follows the ratio of stiffness to density. Spruce is anisotropic: sound runs along the grain about four times faster than across it, which is exactly why soundboards are cut the way they are ([Chapter 10](#ch-string-instruments)).
```

### Sound in Air, and the Temperature Dependence

For air at ordinary temperatures, the speed of sound is very nearly

$$
v = 331.3 + 0.606\,T \quad \text{m/s},
$$

with $T$ the temperature in degrees Celsius. At $0$ °C sound travels at $331$ m/s; at $20$ °C, at $343$ m/s; at $35$ °C, at $353$ m/s.

The dependence is on temperature and essentially nothing else. Air pressure does not appear, which surprises people: raising the pressure makes air both stiffer and denser, in the same proportion, and the two effects cancel exactly. Humidity has a small effect, moist air is very slightly faster, because water molecules are lighter than the nitrogen they displace, but it is a fraction of a percent and rarely matters.

Temperature matters a great deal, because a wind instrument's sounding length is fixed and its pitch follows the speed of sound directly.

```{figure} ../images/ch02-speed-vs-temperature.svg
:label: fig:ch02-speed-vs-temperature
:alt: Left, a straight-line graph of the speed of sound rising from about 325 to 355 meters per second between minus ten and forty degrees Celsius. Right, the resulting pitch shift in cents for a fixed-length pipe tuned at twenty degrees, running from about minus 95 cents to plus 50 cents, with a shaded band marking plus or minus five cents.

Left: the speed of sound in air against temperature. Right: what that does to a pipe of fixed length, expressed in **cents**, hundredths of a semitone, the units of [Chapter 9](#ch-scales-and-tuning). A pipe tuned at $20$ °C and played at $5$ °C is about $46$ cents flat, very nearly a quarter of a semitone, and unmistakably out of tune.
```

```{audio} ch02-pipe-cold, ch02-pipe-warm
:names: At 5 °C, At 20 °C
:figure: ../images/ch02-pipe-temperature.svg
:label: fig:ch02-pipe-temperature
:transcript: The same instrument twice. The second is noticeably higher than the first, not by a semitone, but clearly enough that the two would clash if played together.

A pipe of fixed length, cold and warm. Wind players blow warm air through their instruments before a performance for this reason, and an orchestra retunes after the interval because the strings have not moved while the winds have warmed up and gone sharp.
```

:::{note}
The effect works in the other direction for strings. A guitar left in a cold car goes *sharp*, because the steel strings contract and their tension rises. A temperature change therefore pushes the winds and the strings in opposite directions, and a mixed ensemble in a cold hall is harder to tune than either section alone.
:::

### Sound in Liquids and Solids

Sound travels about $1482$ m/s in water, some $4.3$ times its speed in air. In solids it is faster still, and in a wooden soundboard it depends sharply on direction: along the grain of spruce, about $3800$ m/s; across the grain, about a quarter of that. Instrument makers have exploited this for centuries without needing the number: a soundboard is cut so the grain runs the length of the instrument, because that is the direction along which vibrations must be distributed quickly.

::::{tip} Worked example: locating a hammer blow along a rail
*A steel rail is struck at one end. A listener $600$ m away, with one ear to the rail, hears two distinct sounds. How far apart are they?*

Through the steel, at $5960$ m/s:

$$
t_{\text{steel}} = \frac{600\ \text{m}}{5960\ \text{m/s}} = 0.101\ \text{s}.
$$

Through the air, at $343$ m/s:

$$
t_{\text{air}} = \frac{600\ \text{m}}{343\ \text{m/s}} = 1.75\ \text{s}.
$$

The gap is $1.75 - 0.10 = 1.65$ s, easily long enough to hear as two separate events, which is the classic demonstration that the speed of sound belongs to the medium and not to the source.
::::

## Sound Spreading in Three Dimensions

### Intensity and the Inverse-Square Law

So far the wave has been drawn as though it traveled along a line. In the open air it does not: it spreads out in all directions, and spreading dilutes it.

**Intensity** $I$ is the power carried by a wave per unit area, in watts per square meter. A source radiating power $P$ uniformly in all directions spreads that power over a sphere, so at distance $r$

$$
I = \frac{P}{4\pi r^2}.
$$

This is the **inverse-square law**, and it is a statement about geometry rather than about sound: double the distance and the same power is spread over four times the area, so the intensity falls to a quarter. In the units of [Chapter 7](#ch-loudness) that is a drop of $6$ dB per doubling of distance.

```{figure} ../images/ch02-inverse-square.svg
:label: fig:ch02-inverse-square
:alt: Level against distance on logarithmic axes. A straight blue line falls six decibels per doubling; a dashed red line follows it at short range then flattens out beyond a marked critical distance.

Level against distance. Outdoors, the level falls $6$ dB for every doubling, a straight line on these axes. Indoors it does not: beyond the **critical distance**, the reflected sound bouncing around the room is stronger than the sound arriving directly, and moving further away stops making much difference. A lecturer at the back of a reverberant hall is audible but unintelligible for just this reason; [Chapter 14](#ch-room-acoustics) takes up the indoor case in detail.
```

The indoor case is the more common one in music, and the difference is worth stating plainly: **inside a room, the inverse-square law fails beyond a few meters.** Someone at the back of a concert hall is not hearing a sound $40$ dB weaker than the front row; they are hearing a sound perhaps $8$ dB weaker, most of which has bounced off something.

### Directivity: Why Instruments Do Not Radiate Evenly

The inverse-square law assumed a source radiating equally in all directions. Real instruments do no such thing.

The controlling quantity is the size of the source compared with the wavelength. A source much *smaller* than a wavelength radiates nearly uniformly, it has no way to favor one direction, because the whole of it is effectively at one point as far as the wave is concerned. A source much *larger* than a wavelength beams: the different parts of it interfere, and the sound goes mostly where they all agree.

Since instruments are fixed in size and wavelength shrinks as pitch rises, **every instrument becomes more directional at high frequencies**. A trumpet's low notes spill around the hall; its high notes go where the bell points, so a trumpet sounds quite different from the side. A cello radiates low notes in all directions and high notes in a complicated pattern of lobes. Recording engineers know this as microphone placement: moving a microphone $30$ cm can change a recorded timbre more than changing the microphone does.

### Acoustic Impedance and the Coupling Problem

There is one more property of a medium that matters, and it explains a puzzle raised in [Chapter 1](#ch-sound-and-shm): why is a vibrating tuning fork almost silent until you touch it to a table?

**Acoustic impedance** measures how hard a medium is to set moving: the ratio of the pressure applied to the flow that results. A stiff, dense medium like steel has a high impedance: large pressures produce small motions. A light, springy medium like air has a low one: small pressures produce large motions.

Sound crosses a boundary efficiently only when the impedances on the two sides are **similar**. When they are very different, almost all of the energy reflects and almost none is transmitted. The mismatch between a solid and air is enormous, and the consequence is that a thin vibrating object, a string, a tine, a reed, is a terrible radiator of sound. It shakes the air, the air offers almost no resistance, and hardly any energy is handed over.

Every acoustic instrument is, in large part, a solution to this problem. A soundboard is a large light surface that presents an impedance intermediate between string and air. A brass bell is a gradual flare that converts a narrow high-impedance column into a wide low-impedance one. The middle ear, remarkably, is a mechanical lever-and-piston arrangement solving the same problem in reverse, matching air to the fluid of the inner ear ([Chapter 6](#ch-the-ear)).

:::{seealso}
The impedance argument is used four more times in this book, each time as the key to a different instrument: [](#ch-string-instruments) for the bridge and soundboard, [](#ch-wind-instruments) for the bell, [](#ch-the-ear) for the middle ear, and [](#ch-electronic-and-recorded-sound) for the loudspeaker.
:::

## The Doppler Effect

### Moving Source, Moving Listener

If the source of a sound is moving, the wavefronts it leaves behind are not evenly spaced. Each crest is emitted from a slightly different place, so ahead of the source they are bunched closer together and behind it they are stretched further apart.

```{figure} ../images/ch02-doppler.svg
:label: fig:ch02-doppler
:alt: Concentric circles representing successive wavefronts, whose centers shift progressively to the left, so that the circles are crowded together on the right and widely spaced on the left, with a red dot and arrow marking the moving source.

Wavefronts from a moving source. The wave speed is unchanged, every circle expands at the same rate, but the crests pile up ahead of the source and spread out behind it. A listener ahead meets more crests per second and hears a higher pitch. (The source here is drawn moving at $0.7$ of the speed of sound so that the effect is visible; a passing car is nearer $0.09$.)
```

Since frequency is crests per second, a listener ahead of the source hears a higher frequency and one behind hears a lower one:

$$
f' = f\,\frac{v}{v \mp v_s},
$$

with the minus sign for a source approaching and the plus sign for one receding. If instead the *listener* moves and the source is still, the formula is $f' = f(v \pm v_l)/v$: a different expression, because the two cases are physically different. A moving source changes the wavelength in the air; a moving listener does not, and merely meets the existing crests at a different rate.

::::{tip} Worked example: an ambulance
*A siren sounds at $700$ Hz. The ambulance passes you at $25$ m/s. What frequencies do you hear as it approaches and as it recedes? Take $v = 343$ m/s.*

Approaching:

$$
f' = (700\ \text{Hz})\frac{343}{343 - 25} = (700)(1.0786) = 755\ \text{Hz}.
$$

Receding:

$$
f' = (700\ \text{Hz})\frac{343}{343 + 25} = (700)(0.9321) = 652\ \text{Hz}.
$$

The drop across the pass is $755 \to 652$ Hz, a ratio of $1.158$, which is $1200\log_2(1.158) = 254$ cents, or about two and a half semitones. That is a musically large interval, which is why the effect is so obvious.
::::

### The Rotating Loudspeaker

The Doppler effect has one deliberate musical use, and it is a good one. A **Leslie speaker**, built for the Hammond organ, mounts a loudspeaker on a rotating baffle so that the source is continuously swinging toward and away from the listener. The result is a rich, swirling modulation of both pitch and loudness, quite unlike the flat vibrato of an electronic oscillator, and it became the characteristic sound of an entire era of organ playing.

What makes it sound organic rather than mechanical is that the modulation is not a simple oscillation. The pitch shift depends on the component of the source's velocity along the line to the listener, which varies as a sinusoid; the loudness depends on distance and on the direction the horn happens to be facing; and the room adds reflections that arrive with their own, different, modulations. The effect is a mixture of many slightly different versions of the same swirl.

```{audio} ch02-doppler-pass
:label: fig:ch02-doppler-pass
:transcript: A tone approaching, passing, and receding: the pitch glides steadily downward, falling fastest at the moment of closest approach, and the loudness peaks at the same moment.

A source passing a listener at $30$ m/s, about $110$ km/h, missing by $12$ m. The pitch does not step from high to low; it *glides*, and it glides fastest at the closest approach, because that is where the component of the velocity along the line of sight changes most rapidly. A two-tone caricature of a passing siren misses exactly this, which is why it never sounds convincing.
```

```{openlyceum} DopplerEffect
:label: fig:ch02-doppler-sim

Move the source and the listener independently and watch the wavefronts. Two things are worth confirming deliberately: that the *wave speed* is unchanged in every case, and that moving the source and moving the listener at the same speed do not produce quite the same shift.
```

### Why a Passing Siren Falls and a Vibrato Does Not

A final observation that ties the section to music. A string player's **vibrato** rocks the finger back and forth, changing the string's sounding length and therefore its frequency, several times a second. The pitch really does go up and down. A Doppler shift would do something similar; so why does a violinist's vibrato not sound like a passing ambulance?

Two reasons. The vibrato's excursion is small, a few tens of cents rather than a few hundred, and it is *periodic*: it returns, several times a second, to the note it started from. The ear tracks the average and hears a single pitch with a shimmer on it. The siren's shift is large and monotonic, it goes down and stays down, so the ear has no average to settle on and hears the change itself. [Chapter 8](#ch-pitch-and-consonance) takes up the question of what the auditory system does with a frequency that is moving.

## Summary

- **A wave carries a disturbance, not matter.** Its speed is set by the medium, through $v = \sqrt{\text{stiffness}/\text{density}}$, and not by the source, the frequency, or the amplitude.
- **Transverse waves move the medium across the direction of travel; longitudinal waves move it along.** Strings carry the first, air the second, and the handover between them is the central design problem of a string instrument.
- **$v = f\lambda$** follows from the observation that a wave advances one wavelength per period. Musical wavelengths in air run from about $12$ m to about $8$ cm, comparable to rooms and to hands, so sound diffracts around everyday obstacles.
- **Crossing a boundary conserves frequency**, not wavelength: the far side is driven by the near side at whatever rate it is shaken. Speed and wavelength both change.
- **In air, $v = 331.3 + 0.606\,T$ m/s**, depending on temperature and essentially nothing else, not on pressure, and only slightly on humidity. A fixed-length pipe tuned at $20$ °C is about $46$ cents flat at $5$ °C, so winds and strings drift apart as a hall warms.
- **Intensity falls as $1/r^2$ in the open air**, $6$ dB per doubling of distance, because the same power is spread over a growing sphere. Indoors this fails beyond the critical distance, where reflected sound dominates.
- **Instruments become more directional as pitch rises**, because directivity is governed by source size compared with wavelength, and only the wavelength changes.
- **Acoustic impedance governs how much sound crosses a boundary.** The mismatch between solids and air is huge, so a bare string radiates almost nothing; soundboards, bells, and the middle ear all exist to bridge that gap.
- **The Doppler effect** shifts the frequency of a moving source to $f' = f v/(v \mp v_s)$, by bunching or stretching the wavefronts. A moving listener gives a different formula, because the physics is different.

## Conceptual Questions

1. A trumpeter thirty meters away plays a note. Explain why you hear it a tenth of a second later even though no air travels from the trumpet to your ear.

2. Explain why the speed of sound in air depends on temperature but not on atmospheric pressure, given that both affect how tightly packed the air is.

3. A sound wave passes from air into water. State which of frequency, wavelength, and speed change, and justify the one that does not.

4. A soundboard is cut so that the grain runs along the length of the instrument. Explain the acoustic reason, using the figures for spruce in §2.3.

5. Two listeners stand $2$ m and $8$ m from a singer, outdoors. By how many decibels do their levels differ? Explain why the same pair of positions in a small room would differ by much less.

6. Explain why a trumpet sounds much brighter to a listener directly in front of it than to one standing beside it, and why the effect is stronger for high notes.

7. A vibrating tuning fork is nearly silent in the air but loud when its base touches a table. Explain this using impedance, and say where the energy goes in each case.

8. A police car passes you at constant speed with its siren on. Sketch the pitch you hear against time, and explain why the steepest part of the curve occurs at the moment the car is closest, rather than before or after.

## Problems

:::{exercise}
:label: ex-wave-motion-1

The speed of sound in air at $20$ °C is $343$ m/s. Find the wavelength of (a) a $100$ Hz note, (b) a $1000$ Hz note, (c) a $10{,}000$ Hz note.
:::

:::{solution} ex-wave-motion-1
:label: sol-wave-motion-1
:class: dropdown

Using $\lambda = v/f$ throughout:

$$
\lambda_{100} = \frac{343}{100} = 3.43\ \text{m},\qquad
\lambda_{1000} = \frac{343}{1000} = 0.343\ \text{m},\qquad
\lambda_{10000} = \frac{343}{10000} = 0.0343\ \text{m}.
$$

Therefore, the wavelengths are $3.43$ m, $34.3$ cm, and $3.43$ cm. Each factor of ten in frequency is a factor of ten in wavelength, in the opposite direction.
:::

:::{exercise}
:label: ex-wave-motion-2

Find the speed of sound in air at (a) $0$ °C, (b) $25$ °C, (c) $-15$ °C.
:::

:::{solution} ex-wave-motion-2
:label: sol-wave-motion-2
:class: dropdown

Using $v = 331.3 + 0.606\,T$:

$$
v(0) = 331.3\ \text{m/s},\qquad
v(25) = 331.3 + 15.2 = 346.5\ \text{m/s},\qquad
v(-15) = 331.3 - 9.1 = 322.2\ \text{m/s}.
$$

Therefore, the speeds are $331$, $347$, and $322$ m/s: a spread of about $7\%$ over a range of temperatures a marching band might actually meet.
:::

:::{exercise}
:label: ex-wave-motion-3

You see a lightning flash and hear the thunder $4.2$ s later. The air temperature is $18$ °C. How far away was the strike? (Light's travel time is negligible.)
:::

:::{solution} ex-wave-motion-3
:label: sol-wave-motion-3
:class: dropdown

First the speed:

$$
v = 331.3 + 0.606(18) = 342.2\ \text{m/s}.
$$

Then the distance:

$$
d = vt = (342.2\ \text{m/s})(4.2\ \text{s}) = 1.44\times10^{3}\ \text{m}.
$$

Therefore, the strike was about $1.4$ km away. The familiar rule of thumb, three seconds per kilometer, follows from $1000/342 = 2.9$.
:::

:::{exercise}
:label: ex-wave-motion-4

An organ pipe is tuned to sound A440 in a church at $18$ °C. The heating fails and the church cools to $6$ °C. (a) What frequency does the pipe now sound? (b) Express the change in cents. (c) Would a listener notice?
:::

:::{solution} ex-wave-motion-4
:label: sol-wave-motion-4
:class: dropdown

(a) The pipe's length is fixed, so its frequency is proportional to the speed of sound:

$$
v(18) = 342.2\ \text{m/s},\qquad v(6) = 331.3 + 3.64 = 334.9\ \text{m/s},
$$

$$
f' = (440\ \text{Hz})\frac{334.9}{342.2} = 430.6\ \text{Hz}.
$$

(b) In cents:

$$
n = 1200\log_2\!\left(\frac{430.6}{440}\right) = 1200 \times (-0.0312) = -37\ \text{cents}.
$$

(c) Yes, unmistakably. The just-noticeable difference for a trained listener comparing two sustained tones is a few cents; $37$ cents is more than a third of a semitone, and any other instrument playing alongside would clash badly.
:::

:::{exercise}
:label: ex-wave-motion-5

A guitar string of length $65$ cm has mass per unit length $\mu = 6.3\times10^{-3}$ kg/m and is under tension $T = 110$ N. (a) What is the wave speed along the string? (b) The lowest mode has a wavelength twice the string length. What frequency does the string sound?
:::

:::{solution} ex-wave-motion-5
:label: sol-wave-motion-5
:class: dropdown

(a) Using $v = \sqrt{T/\mu}$:

$$
v = \sqrt{\frac{110\ \text{N}}{6.3\times10^{-3}\ \text{kg/m}}} = \sqrt{1.746\times10^{4}} = 132\ \text{m/s}.
$$

(b) With $\lambda = 2L = 1.30$ m:

$$
f = \frac{v}{\lambda} = \frac{132\ \text{m/s}}{1.30\ \text{m}} = 102\ \text{Hz}.
$$

Therefore, waves travel at $132$ m/s along the string and it sounds about $102$ Hz, close to the G$_2$ of a guitar's third string. Note how much *slower* this is than sound in air: the wave on the string and the sound it radiates have quite different speeds and therefore quite different wavelengths, though they share a frequency.
:::

:::{exercise}
:label: ex-wave-motion-6

A tone of $440$ Hz travels from air ($v = 343$ m/s) into water ($v = 1482$ m/s). Find its wavelength in each medium, and state its frequency in the water.
:::

:::{solution} ex-wave-motion-6
:label: sol-wave-motion-6
:class: dropdown

In air:

$$
\lambda_{\text{air}} = \frac{343\ \text{m/s}}{440\ \text{Hz}} = 0.780\ \text{m}.
$$

Frequency is conserved across the boundary, so in water it is still $440$ Hz, and

$$
\lambda_{\text{water}} = \frac{1482\ \text{m/s}}{440\ \text{Hz}} = 3.37\ \text{m}.
$$

Therefore, the wavelength grows by the ratio of the speeds, $1482/343 = 4.32$, while the pitch is unchanged.
:::

:::{exercise}
:label: ex-wave-motion-7

A busker plays outdoors. A listener $3.0$ m away measures a sound intensity of $4.0\times10^{-5}$ W/m². (a) What is the busker's acoustic power output, assuming uniform radiation? (b) What intensity would a listener $12$ m away measure?
:::

:::{solution} ex-wave-motion-7
:label: sol-wave-motion-7
:class: dropdown

(a) From $I = P/4\pi r^2$:

$$
P = 4\pi r^2 I = 4\pi(3.0\ \text{m})^2(4.0\times10^{-5}\ \text{W/m}^2) = 4.5\times10^{-3}\ \text{W}.
$$

(b) Four times the distance is sixteen times the area:

$$
I = \frac{4.0\times10^{-5}}{16} = 2.5\times10^{-6}\ \text{W/m}^2.
$$

Therefore, the busker radiates about $4.5$ mW of sound, and the distant listener receives $2.5\ \mu$W/m². Note how small the power is: a few milliwatts is a perfectly audible musical performance, which says more about the sensitivity of the ear than about the efficiency of the busker.
:::

:::{exercise}
:label: ex-wave-motion-8

A train sounds a $520$ Hz horn and approaches a station platform at $31$ m/s. Take $v = 343$ m/s. (a) What frequency does a waiting passenger hear as it approaches? (b) As it recedes? (c) Express the total change in cents.
:::

:::{solution} ex-wave-motion-8
:label: sol-wave-motion-8
:class: dropdown

(a) Approaching:

$$
f' = (520)\frac{343}{343 - 31} = (520)(1.0994) = 572\ \text{Hz}.
$$

(b) Receding:

$$
f' = (520)\frac{343}{343 + 31} = (520)(0.9171) = 477\ \text{Hz}.
$$

(c) In cents:

$$
n = 1200\log_2\!\left(\frac{572}{477}\right) = 1200(0.2622) = 315\ \text{cents}.
$$

Therefore, the horn falls from $572$ Hz to $477$ Hz, a drop of $315$ cents: a little over three semitones, roughly a minor third.
:::

:::{exercise}
:label: ex-wave-motion-9

Sound travels at $5960$ m/s in steel and $343$ m/s in air. A steel pipe $180$ m long is struck at one end. (a) Find the two arrival times at the far end. (b) A listener claims to hear only one sound. Suggest the most likely reason.
:::

:::{solution} ex-wave-motion-9
:label: sol-wave-motion-9
:class: dropdown

(a) Through the steel and through the air:

$$
t_{\text{steel}} = \frac{180}{5960} = 0.0302\ \text{s},\qquad
t_{\text{air}} = \frac{180}{343} = 0.525\ \text{s}.
$$

The gap is $0.49$ s.

(b) Half a second is ample separation, so a listener hearing one sound is most likely not in contact with the pipe: the steel-borne pulse has to be coupled into the listener, by touch or by the pipe radiating at the far end, and if the pipe is well isolated at that end the steel-borne arrival may be too faint to notice.
:::

:::{exercise}
:label: ex-wave-motion-10

A loudspeaker $20$ cm across is used to reproduce a range of frequencies. Estimate the frequency above which the speaker's diameter exceeds one wavelength, and comment on what happens to its radiation pattern above that frequency.
:::

:::{solution} ex-wave-motion-10
:label: sol-wave-motion-10
:class: dropdown

Setting $\lambda = 0.20$ m and solving for frequency:

$$
f = \frac{v}{\lambda} = \frac{343\ \text{m/s}}{0.20\ \text{m}} = 1.7\times10^{3}\ \text{Hz}.
$$

Therefore, above roughly $1.7$ kHz the driver is larger than a wavelength. Below that it radiates nearly uniformly into the room; above it, different parts of the cone interfere and the output narrows into a beam along the axis, so the listener hears progressively less treble as they move off-axis. This is precisely why loudspeakers use a small tweeter for high frequencies rather than one driver for everything ([Chapter 15](#ch-electronic-and-recorded-sound)).
:::

:::{exercise}
:label: ex-wave-motion-11

A flute is tuned to A440 in a $21$ °C rehearsal room, then carried outdoors to play at $9$ °C. (a) What frequency does it sound outdoors, before the player compensates? (b) A flutist can compensate by rolling the instrument and adjusting the embouchure over a range of about $\pm 25$ cents. Is that enough?
:::

:::{solution} ex-wave-motion-11
:label: sol-wave-motion-11
:class: dropdown

(a) The speeds are

$$
v(21) = 331.3 + 12.7 = 344.0\ \text{m/s},\qquad v(9) = 331.3 + 5.5 = 336.8\ \text{m/s},
$$

so

$$
f' = (440)\frac{336.8}{344.0} = 430.8\ \text{Hz}.
$$

(b) In cents:

$$
n = 1200\log_2\!\left(\frac{430.8}{440}\right) = -37\ \text{cents}.
$$

Therefore, the flute plays $37$ cents flat, which exceeds the $\pm25$ cent range the player can cover. The physical remedy is to shorten the instrument by pushing the head joint in, which is exactly what flutists do when the temperature changes.
:::

:::{exercise}
:label: ex-wave-motion-12

Two microphones on a line are $4.00$ m apart. A hand clap made beyond one of them, on that line, arrives at the second microphone $11.9$ ms after the first. (a) What speed of sound does this imply? (b) What air temperature does that correspond to? (c) If the clap were actually made $1.0$ m off the line, would the inferred speed be too high or too low? Explain.
:::

:::{solution} ex-wave-motion-12
:label: sol-wave-motion-12
:class: dropdown

(a) From speed as distance over time:

$$
v = \frac{4.00\ \text{m}}{11.9\times10^{-3}\ \text{s}} = 336\ \text{m/s}.
$$

(b) Solving $336 = 331.3 + 0.606\,T$:

$$
T = \frac{336 - 331.3}{0.606} = 7.8\ \text{\textdegree C}.
$$

(c) Too high. Off the line, the *difference* in path lengths to the two microphones is less than their $4.00$ m separation, so the measured delay is shorter than it should be for that separation. Dividing the full $4.00$ m by that too-short delay overestimates the speed. This is the systematic error the laboratory exercise in [](#appendix-laboratory) warns about.
:::

:::{exercise}
:label: ex-wave-motion-13

Helium's speed of sound is $965$ m/s, against $343$ m/s for air. A singer inhales helium and sings a sustained vowel. (a) By what factor do the resonances of their vocal tract shift? (b) Does the pitch of the note change? Explain carefully, and say what the listener actually hears differently.
:::

:::{solution} ex-wave-motion-13
:label: sol-wave-motion-13
:class: dropdown

(a) The vocal tract's resonances are set by its length and by the speed of sound in the gas filling it. The length is unchanged, so the resonant frequencies scale directly with the speed:

$$
\frac{965}{343} = 2.81.
$$

(b) **No, the pitch is essentially unchanged.** The pitch is set by the rate at which the vocal folds open and close, which is governed by their mass and tension and by the air pressure driving them, not by the speed of sound in the gas. What shifts is the *filter*, not the *source*.

Therefore, the listener hears the same note with its resonances moved up by nearly a factor of three, which strips the low-frequency emphasis out of the vowel and leaves the characteristic thin, quacking timbre. This is the clearest everyday demonstration of the source–filter model of [Chapter 13](#ch-the-singing-voice), and the popular description of helium as "raising your voice" gets the physics exactly backwards.
:::

:::{exercise}
:label: ex-wave-motion-14

A Leslie speaker's horn rotates on a circle of radius $0.17$ m at $6.6$ revolutions per second. (a) What is the speed of the horn's mouth? (b) What is the maximum Doppler shift, in cents, for a $500$ Hz tone heard by a distant listener? (c) How many times per second does the listener hear the pitch rise and fall?
:::

:::{solution} ex-wave-motion-14
:label: sol-wave-motion-14
:class: dropdown

(a) The speed is the circumference divided by the period:

$$
v_s = 2\pi r f_{\text{rot}} = 2\pi(0.17\ \text{m})(6.6\ \text{s}^{-1}) = 7.05\ \text{m/s}.
$$

(b) The extreme shifts occur when the horn moves directly toward and directly away from the listener:

$$
f'_{\text{near}} = (500)\frac{343}{343 - 7.05} = 510.5\ \text{Hz},\qquad
f'_{\text{far}} = (500)\frac{343}{343 + 7.05} = 489.9\ \text{Hz}.
$$

In cents, relative to $500$ Hz:

$$
1200\log_2\!\left(\frac{510.5}{500}\right) = +36\ \text{cents},\qquad
1200\log_2\!\left(\frac{489.9}{500}\right) = -35\ \text{cents}.
$$

(c) Once per revolution, so $6.6$ times per second.

Therefore, the pitch swings about $\pm36$ cents at $6.6$ Hz: a wide, fast vibrato, which together with the accompanying loudness modulation is the characteristic Leslie swirl.
:::
