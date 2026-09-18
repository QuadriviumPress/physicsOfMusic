---
title: "The Ear and the Physiology of Hearing"
short_title: "Chapter 6. The Ear and the Physiology of Hearing"
label: ch-the-ear
numbering:
  enumerator: "6.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 6.1, 6.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-06-the-ear-and-the-physiology-of-hearing.pdf
    chapter: 6
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Name the principal structures of the outer, middle, and inner ear and state the function of each.
- Explain how the shape of the pinna and the resonance of the ear canal shape the sound reaching the eardrum, and relate the canal resonance to the region of greatest sensitivity.
- Explain the impedance-matching problem between air and the fluid of the cochlea, and calculate the pressure gain the middle ear achieves through the area ratio and the ossicular lever.
- Describe the structure of the cochlea and the traveling wave on the basilar membrane.
- State the place principle, and use the tonotopic map to predict where a given frequency produces its maximum response.
- Describe how hair cells transduce mechanical motion into neural signals, and distinguish the roles of inner and outer hair cells.
- Explain phase locking and the volley principle, and state the frequency range over which timing information is available to the auditory nerve.
- Explain how excessive sound exposure damages hearing, why the damage is permanent, and what the exposure limits are.
- Explain why hair-cell damage can produce tinnitus, a phantom sound, rather than simple silence at the affected frequency.

### Introduction

```{figure} ../images/open/ch06-ear-anatomy-illustration.png
:label: fig:ch06-open-ear
:alt: A labeled illustration of the outer, middle, and inner ear, showing the ear canal, eardrum, ossicles, and cochlea.

The ear is both anatomy and an acoustic pathway. This illustration gives the reader a physical object to keep in mind while the chapter develops its transduction model. BruceBlaus / Blausen Medical, CC BY 3.0.
```

The book now turns around. Chapters 1 to 5 followed sound from a vibrating object out into the room. The next three follow it from the room into a listener, and the story changes character completely.

Up to this point everything has been measurable with instruments. A microphone and an oscilloscope can tell you the frequency, the amplitude, and the spectrum of a sound, and two competent experimenters will agree on all three. From here on, the quantities are **judgments**: how loud something seems, how high it seems, whether two notes seem to go together. No instrument measures those. They are produced by a listener, and to understand them you have to understand the machinery that produces them.

That machinery begins with a mechanical problem that is worth appreciating before any biology appears. Sound in air must be transferred into fluid, and [Chapter 2](#ch-wave-motion) showed that a boundary between media of very different acoustic impedance reflects almost everything. Air to water reflects about $99.9\%$ of the incident energy: a loss of some $30$ dB. An ear made simply of a membrane over a fluid-filled cavity would be nearly deaf.

The middle ear exists to solve exactly that problem, and it recovers almost all of the $30$ dB. The rest of the chapter is about what the inner ear does with the sound once it has got it: how it separates frequencies, how it turns motion into nerve impulses, and what its limits are.

```{video} https://www.youtube.com/watch?v=LkGOGzpbrCk
:video-title: The Science of Hearing
:label: fig:ch06-science-of-hearing-video
:alt: A cutaway animation traces sound through the outer, middle, and inner ear.

TED-Ed and Douglas L. Oliver give an anatomical overview of hearing, following a sound from the outer ear through the ossicles and cochlea. It provides a visual map for the structures examined separately below.
```

## The Outer Ear

### The Pinna and Direction

The visible ear, the **pinna**, is a collecting funnel, but that is the least interesting thing about it. Its folds and ridges are not decorative. They reflect incoming sound with small delays that depend on the direction it came from, and those delays reinforce some frequencies and cancel others.

The result is that the spectrum arriving at your eardrum is stamped with a direction-dependent pattern. A sound from above is filtered differently from one in front, which is differently from one behind.

This is the only cue available for distinguishing front from back, or up from down. The two-eared cues, a sound reaching one ear sooner and louder than the other, locate sound left and right very well, but they are identical for a source in front and the same source directly behind. The pinna breaks that ambiguity, and it is why a recording made with microphones in a dummy head's ears can produce a startlingly convincing sense of height and behindness through headphones ([Chapter 15](#ch-electronic-and-recorded-sound)).

```{figure} ../images/ch06-ear-anatomy.svg
:label: fig:ch06-ear-anatomy
:alt: A left-to-right schematic traces incoming sound through the pinna and curved ear canal, across the eardrum and the three named ossicles, through the oval window into the spiral cochlea, and out along the auditory nerve. The two impedance boundaries are labeled air to bone and bone to fluid.

The ear, drawn for the argument rather than as an anatomy plate. Arrows follow one continuous signal path through air, bone, fluid, and finally the auditory nerve. The two changes of medium, at the eardrum and oval window, are where the interesting physics happens.
```

### The Ear Canal as a Resonator

The ear canal is a tube about $25$ mm long, closed at the far end by the eardrum. That is a stopped pipe, and [Chapter 3](#ch-superposition) gives its fundamental resonance immediately:

$$
f_1 = \frac{v}{4L} = \frac{343\ \text{m/s}}{4(0.025\ \text{m})} = 3.4\ \text{kHz}.
$$

The canal therefore boosts sounds near $3$–$4$ kHz by about $10$ dB before they reach the eardrum at all.

This is not a coincidence, and it is a genuinely satisfying piece of physics. **The region of greatest hearing sensitivity is at $3$–$4$ kHz**, and a good part of the reason is a quarter-wave resonance in a $2.5$ cm tube. It is also the region of the consonants that carry most of the intelligibility of speech, and the region in which a singer's voice must compete with an orchestra ([Chapter 13](#ch-the-singing-voice)).

:::{tip} Self-check
Predict what happens to the ear canal's resonance when a person puts in an earplug that shortens the effective canal. Does the peak move up or down, and by roughly how much for a plug that occupies the outer third?
:::

### The Eardrum

The eardrum is a thin conical membrane, about $55$ mm² in area, that moves when the pressure in front of it differs from the pressure behind. Its displacement at the threshold of hearing is astonishing: roughly $10^{-11}$ m, about a tenth the diameter of a hydrogen atom, and considerably less than the thermal jiggling of the membrane's own molecules.

That the ear works at all at such amplitudes is possible because it averages over time and area, and because it is not actually detecting a *displacement* below the thermal noise, it is detecting a *correlated* displacement against an uncorrelated background. Hearing sits very close to the physical limit of what a detector in a warm, noisy body could achieve.

## The Middle Ear

### Three Bones and a Lever

Behind the eardrum is an air-filled cavity containing the three smallest bones in the body: the **malleus**, **incus**, and **stapes**, or hammer, anvil, and stirrup. They form a chain from the eardrum to the **oval window**, the membrane-covered opening into the fluid-filled cochlea.

The chain is a lever. The hammer's arm is slightly longer than the anvil's, so the force at the stirrup is about $1.3$ times the force at the eardrum, at $1.3$ times less displacement.

### Impedance Matching by Area Ratio

The lever is the smaller half of the trick. The larger half is area.

The eardrum has an area of about $55$ mm²; the oval window has an area of about $3.2$ mm². The whole force collected over the eardrum is delivered to the much smaller oval window, and pressure is force over area, so the pressure is multiplied by the ratio of the areas, about $17$.

```{figure} ../images/ch06-middle-ear-gain.svg
:label: fig:ch06-middle-ear-gain
:alt: Left, two circles drawn to scale showing the eardrum at 55 square millimeters and the oval window at 3.2 square millimeters, with an arrow marked times seventeen. Right, a bar chart showing a gain of 17.2 from the area ratio, 1.3 from the ossicular lever, and 22.3 in total.

Where the middle ear's gain comes from. The area ratio does most of the work; the ossicular lever adds a little more. Together they multiply the pressure by about $22$, which is $27$ dB, close to the $30$ dB that would otherwise be lost at the air–fluid boundary.
```

The total pressure gain is about $17 \times 1.3 \approx 22$, or $27$ dB. Set against the $30$ dB that a bare air–fluid boundary would lose, the middle ear recovers all but a few decibels of what would otherwise be thrown away.

::::{tip} Worked example: what hearing would be without a middle ear
*Roughly $99.9\%$ of sound energy incident on a water surface from air is reflected. Express that loss in decibels, and compare with the middle ear's gain.*

The transmitted fraction is $0.001$, so the level loss is

$$
10\log_{10}(0.001) = -30\ \text{dB}.
$$

The middle ear supplies $+27$ dB. The net loss is therefore about $3$ dB rather than $30$ dB.

In terms of what that means for a listener: $27$ dB of extra sensitivity is a factor of $500$ in intensity. A conversation at four meters would become a conversation shouted from the next room. This is not a small refinement, it is most of the difference between hearing and not.
::::

### The Acoustic Reflex

The middle ear is not a passive lever. Two small muscles, the tensor tympani and the stapedius, contract in response to loud sound, stiffening the chain and reducing its transmission by up to $20$ dB at low frequencies.

It is a protection mechanism, and it has two limitations worth knowing, because both bear on musicians. It takes $50$–$100$ ms to engage, so it offers no protection at all against a gunshot or a snare hit. And it fatigues, so it does not protect against sustained loud sound either. The reflex is good at conversation-level fluctuations and useless against the two things that actually damage hearing.

## The Cochlea

### Anatomy of a Coiled Tube

The **cochlea** is a fluid-filled tube about $35$ mm long, coiled into two and a half turns: the coiling is a packing convenience and has no acoustic significance. Running along its length is the **basilar membrane**, and the membrane's properties change systematically from one end to the other:

- At the **base**, near the oval window, it is narrow (about $0.1$ mm) and stiff.
- At the **apex**, the far end, it is wide (about $0.5$ mm) and floppy.

Narrow and stiff means a high natural frequency; wide and floppy means a low one, exactly as [Chapter 1](#ch-sound-and-shm) would predict for anything on a spring. The membrane is therefore a continuous graded series of resonators, running from about $20$ kHz at the base to about $20$ Hz at the apex.

```{figure} ../images/ch06-cochlea-map.svg
:label: fig:ch06-cochlea-map
:alt: Top, the basilar membrane drawn unrolled as a wedge, narrow and stiff at the base where sound enters and wide and floppy at the apex. Bottom, a logarithmic plot of the frequency of maximum response against distance from the base, marked with A2, A4 and A7.

The basilar membrane unrolled, and the map of frequency onto place. The frequency axis is logarithmic and the distance axis is linear, and the relationship is close to a straight line, which means **equal musical intervals occupy equal distances along the cochlea**. An octave is about $3.5$ mm, anywhere in the middle of the range.
```

That last observation is worth dwelling on. The cochlea is laid out logarithmically in frequency, which is the same way music is laid out. The octave is the same physical distance whether it is the octave above middle C or three octaves higher. Much of [Chapter 8](#ch-pitch-and-consonance) follows from this one fact.

### The Traveling Wave on the Basilar Membrane

Georg von Békésy won the 1961 Nobel Prize for working out what actually happens in there, and the answer is subtler than "each place resonates".

A sound entering at the oval window sets off a **traveling wave** that moves along the membrane from base toward apex. As it travels it grows, reaches a peak at the place matched to its frequency, and then dies away very rapidly.

```{animation} ch06-travelling-wave
:label: fig:ch06-traveling-wave
:alt: Three envelope curves along the length of the basilar membrane, for 4 kHz, 1 kHz and 250 Hz, each rising gradually, peaking at a different place, and falling away steeply on the apex side of the peak.

Envelopes of the traveling wave at three frequencies. Each rises gradually and falls steeply. The asymmetry is not cosmetic: a low-frequency wave travels the whole length of the membrane and excites everything on the way, while a high-frequency wave never reaches the apex at all.
```

The asymmetry of those envelopes has a direct musical consequence, and it is one of the few places where anatomy explains something a listener notices. **A loud low tone masks a quiet high one far more effectively than the reverse** ([Chapter 7](#ch-loudness)), because the low tone's traveling wave passes over, and excites, the region belonging to the high tone on its way to its own place. The high tone's wave never gets near the low tone's region at all. This is called **upward spread of masking**, and it is why a bass guitar buries a triangle and a triangle does not bury a bass guitar.

### The Tonotopic Map

The place-to-frequency correspondence is called **tonotopic organization**, and it is preserved all the way up: the auditory nerve, the brainstem nuclei, and the auditory cortex are all laid out as maps of frequency. The brain receives something that is already sorted by frequency before any neural processing has happened.

This is the physiological basis of Ohm's acoustic law from [Chapter 5](#ch-fourier-and-timbre). The ear is, mechanically, something very like a Fourier analyzer. And because it encodes *place*, while the relative timing between distant places is not preserved, the phase relationships among widely separated harmonics are discarded, exactly as the listening experiment showed.

```{video} https://www.youtube.com/watch?v=eQEaiZ2j9oc
:video-title: Journey of Sound to the Brain
:label: fig:ch06-sound-to-brain-video
:alt: An anatomical animation follows vibrations from the eardrum into the cochlea and auditory nerve.

The National Institutes of Health follows vibration through the eardrum and ossicles, into the cochlea and hair cells, and finally along the auditory nerve. The animation connects the traveling wave on the basilar membrane to the neural signal it produces.
```

## From Motion to Nerve Impulse

### Hair Cells and the Organ of Corti

Sitting on the basilar membrane is the **organ of Corti**, containing about $16{,}000$ **hair cells**, each carrying a bundle of fine projections called stereocilia.

When the membrane moves, the stereocilia are bent sideways. Bending them one way pulls open molecular gates and lets ions flood into the cell; bending them the other way closes them. The cell's voltage therefore follows the motion of the membrane, and that voltage change triggers the release of neurotransmitter onto the auditory nerve fibers beneath.

The mechanism is direct, a mechanical gate, opened by a physical tug, so hearing is fast. There is no chemical cascade of the kind vision uses, and the latency is a matter of microseconds.

### Inner and Outer Hair Cells

There are two kinds, in very different numbers, and their roles were a genuine surprise.

**Inner hair cells**, about $3{,}500$ of them in a single row, are the sensors. They carry roughly $95\%$ of the fibers going *to* the brain. These are what hearing is made of.

**Outer hair cells**, about $12{,}000$ in three rows, are mostly not sensors at all. Most of their connections run *from* the brain, and their job is to **change length** in response to the voltage across them, fast enough to follow an audio-frequency signal.

That makes them an active amplifier. An outer hair cell detects the local motion and pushes in phase with it, feeding energy back into the membrane. The consequence is a sharpening of the traveling wave's peak, a rise in the effective $Q$ of [Chapter 4](#ch-resonance), by a factor of $100$ to $1000$ at low levels, and a corresponding improvement in both sensitivity and frequency selectivity.

:::{note}
The cochlea's active amplifier can be caught in the act. A sensitive microphone in the ear canal can detect faint sounds coming *out* of a healthy ear, **otoacoustic emissions**, generated by the outer hair cells. Their presence is now the standard screening test for hearing in newborns, since it requires nothing of the infant at all. An ear that is not emitting is an ear whose amplifier is not working.
:::

Outer hair cells are also the first casualties of noise exposure, so noise-induced hearing loss shows up first as a loss of *clarity* in noisy places rather than as a loss of volume: the amplifier has gone, taking the sharpening with it, and sounds that used to be separable now blur together.

### Place, Timing, and the Volley Principle

There is a second stream of information alongside place.

Auditory nerve fibers tend to fire at a particular phase of the basilar membrane's motion, **phase locking**. A fiber does not fire on every cycle, but when it fires, it fires at the same point in the cycle. Pool many fibers and the aggregate firing pattern carries the waveform's period directly, a mechanism known as the **volley principle**.

Phase locking works up to about $4$–$5$ kHz and degrades above that, because the nerve cannot maintain timing precision at those rates.

That number is suspicious. **The top note of a piano is $4186$ Hz.** Almost all melodic instruments have their fundamentals below about $4$ kHz: that is, within the range where timing information is available. Above it, pitch perception becomes markedly worse: listeners are poor at recognizing melodies made of pure tones above $5$ kHz, and poor at tuning them. The musical range appears to stop about where the temporal mechanism does, and [Chapter 8](#ch-pitch-and-consonance) takes up what that implies about how pitch is computed.

```{video} https://www.youtube.com/watch?v=Sn07AMCfaAI
:video-title: These Illusions Fool Almost Everyone
:label: fig:ch06-auditory-illusions-video
:alt: A presenter demonstrates auditory illusions involving pitch, direction, and expectation.

Veritasium demonstrates illusions that depend on how the ear and brain localize and interpret sound. They are reminders that hearing is an inference made from neural evidence, not a literal copy of the pressure waveform.
```

## Limits and Damage

### The Audible Range and How It Narrows

The nominal range of human hearing is $20$ Hz to $20$ kHz, and the upper figure applies to a young person with undamaged ears. It falls steadily with age, a process called **presbycusis**, at roughly a kilohertz per decade after the twenties, and it falls from the top down, because the base of the cochlea, which handles high frequencies, bears the brunt of a lifetime's exposure.

```{audio} ch06-upper-limit-sweep
:label: fig:ch06-upper-limit-sweep
:transcript: A rising tone that climbs steadily for about fourteen seconds. At some point it becomes inaudible; when depends on the listener, on the playback system, and on the volume.

A sweep from $2$ kHz to $18$ kHz. Note the moment it disappears and read the frequency off the figure. Two warnings before drawing conclusions: many playback systems roll off above $15$ kHz on their own, and the clip is *not* corrected for the ear's frequency response, so the apparent loudness changes as it climbs. This is an indication, not an audiogram.
```

```{figure} ../images/ch06-hearing-loss.svg
:label: fig:ch06-hearing-loss
:alt: Left, three audiogram curves showing typical threshold shift at ages 20, 40 and 60, with the loss concentrated at high frequencies. Right, a logarithmic plot of safe daily exposure time against sound level, falling from eight hours at 85 dB to under a minute above 110 dB.

Left: typical threshold shift with age, which is concentrated at the high-frequency end. Right: safe exposure limits. Every $3$ dB doubles the sound energy and therefore **halves** the time you can safely be exposed: the difference between $100$ dB and $112$ dB is the difference between fifteen minutes and under a minute.
```

### Noise-Induced Hearing Loss

The damage is mechanical, and it is permanent.

Excessive sound overdrives the hair cells, and the stereocilia break or fuse. Hair cells in mammals **do not regenerate**. There is no recovery, no treatment, and no replacement, only prevention.

Three things make this more dangerous for musicians than for most people.

**Temporary threshold shift is misleading.** After a loud rehearsal, hearing is dulled and returns to normal within a day, which feels like the ear repairing itself. It is not. Each episode leaves a small permanent component, and the permanent components accumulate over years.

**It is painless and gradual.** Nothing hurts, and the loss appears first at frequencies above the range that carries most musical fundamentals. By the time a player notices, a great deal has usually been lost.

**Damage can announce itself as a sound rather than a silence.** Many musicians who lose hair cells at some frequency band do not experience that band as simply quieter; they experience **tinnitus**, a persistent ringing, hissing, or whining heard in the absence of any external sound. The leading explanation follows directly from the mechanism above: the brain's auditory pathway, deprived of its normal input at the damaged frequencies, turns up its own gain there, and the resulting spontaneous neural activity is heard as a tone. Tinnitus is common, often permanent once established, and, like the hearing loss that usually causes it, is easier to prevent than to treat.

**The exposure limits are stricter than they look.** The right-hand panel above is a $3$ dB exchange rate: $85$ dB for eight hours, $88$ dB for four, $91$ dB for two. An orchestra pit routinely reaches $95$ dB, and a brass section measures over $110$ dB at the player's own ear.

### Exposure Limits for Musicians

The practical measures are unglamorous and they work.

**Wear musician's earplugs.** These are not foam plugs. Foam attenuates the high frequencies much more than the low ones, which makes music sound muffled and wrong, and players take them out. Musician's plugs use an acoustic filter to attenuate roughly evenly across the spectrum, typically $9$, $15$, or $25$ dB, so the sound is quieter but not distorted. Nine decibels is a factor of eight in energy, and it multiplies safe exposure time by eight.

**Use distance.** The inverse-square law of [Chapter 2](#ch-wave-motion) is free protection: doubling your distance from a loud source buys $6$ dB, which quadruples the safe time.

**Use time.** Damage depends on total energy, so breaks are not merely a rest, they are a direct reduction in the dose.

:::{warning}
This is the one part of the book with a practical consequence that cannot be undone. Hearing loss is cumulative, painless, and permanent, and the people most at risk from it are exactly the people most interested in this subject. Take the limits in the figure seriously.
:::

```{audio} ch06-full-band, ch06-telephone-band
:names: Full spectrum, Telephone band only
:figure: ../images/ch06-telephone-band.svg
:label: fig:ch06-telephone-band
:transcript: The same note twice. The first is full and warm; the second is thin and boxy, like a voice on an old telephone, though the pitch is identical.

Everything outside $300$ Hz to $3.4$ kHz removed. Speech through this band stays perfectly intelligible, which is what the telephone was designed around, and it is roughly the band the outer and middle ear favor. Music through it does not survive nearly as well, which is a useful reminder that intelligibility and fidelity are different requirements.
```

## Summary

- **The ear solves an impedance-matching problem.** An air–fluid boundary reflects about $99.9\%$ of incident sound, a loss of $30$ dB; the middle ear recovers about $27$ dB of it.
- **The pinna** imposes a direction-dependent filter on the spectrum, which is the only cue distinguishing front from back and up from down.
- **The ear canal is a stopped pipe** about $25$ mm long, resonating near $3.4$ kHz, which is a large part of why hearing is most sensitive there.
- **The middle ear's gain is mostly area ratio** ($55\ \text{mm}^2$ to $3.2\ \text{mm}^2$, a factor of $17$) with a smaller contribution from the ossicular lever ($1.3$), giving about $22$ times the pressure, or $27$ dB.
- **The basilar membrane is stiff and narrow at the base, floppy and wide at the apex**, so each place responds best to one frequency. The map is logarithmic: **equal musical intervals occupy equal distances**, an octave being about $3.5$ mm.
- **A traveling wave** builds gradually and cuts off sharply past its peak. The asymmetry produces the **upward spread of masking**: low tones mask high ones far more than the reverse.
- **Inner hair cells sense; outer hair cells amplify.** The outer cells change length in phase with the motion, sharpening the response by a factor of $100$–$1000$ and producing measurable otoacoustic emissions. They are also the first thing noise destroys.
- **Phase locking** carries timing information up to about $4$–$5$ kHz, very nearly the top note of a piano, and roughly where reliable pitch perception stops.
- **Noise-induced hearing loss is mechanical, cumulative, painless, and permanent**, since mammalian hair cells do not regenerate. Every $3$ dB halves the safe exposure time. Musician's earplugs, distance, and breaks all work.
- **Tinnitus**, a phantom ringing or hissing, often accompanies hair-cell damage: the brain raises its gain at frequencies it no longer receives input from, and the spontaneous activity is heard as sound.

## Conceptual Questions

1. Explain why an ear consisting only of a membrane over a fluid-filled cavity would be about $30$ dB less sensitive than a human ear, and what the middle ear does about it.

2. The ear canal is about $2.5$ cm long. Explain why this produces a sensitivity peak near $3$–$4$ kHz, and identify which boundary condition applies at each end.

3. Explain why the pinna is necessary for telling a sound in front from the same sound behind, given that the two ears alone locate sounds left and right perfectly well.

4. The basilar membrane's frequency map is logarithmic in frequency and linear in distance. State what this implies about the physical distance occupied by an octave, and connect it to why the octave is musically special.

5. A loud bass note masks a quiet high note much more than a quiet high note masks a loud bass note. Explain this using the shape of the traveling wave.

6. Distinguish the roles of inner and outer hair cells, and explain why damage to the outer cells shows up first as difficulty understanding speech in a noisy room rather than as a loss of loudness.

7. The acoustic reflex takes about $50$ ms to engage and fatigues over time. Explain why this makes it useless against the two kinds of exposure that actually damage hearing.

8. Phase locking fails above about $4$–$5$ kHz, and the highest note on a piano is $4186$ Hz. Discuss whether this is likely to be a coincidence.

9. Tinnitus is usually described as a sound heard in the absence of any external stimulus, yet it typically follows damage at a *specific* frequency band. Explain why the pitch of the phantom sound and the location of the damage are connected, using the tonotopic map.

## Problems

:::{exercise}
:label: ex-the-ear-1

*(Straightforward)* The ear canal is $2.5$ cm long and behaves as a stopped pipe. Take $v = 343$ m/s. (a) Find its fundamental resonance. (b) Find its next resonance. (c) Is the second resonance inside the range of hearing?
:::

:::{solution} ex-the-ear-1
:label: sol-the-ear-1
:class: dropdown

(a) A stopped pipe has $f_n = nv/4L$ for odd $n$:

$$
f_1 = \frac{343}{4(0.025)} = 3430\ \text{Hz}.
$$

(b) The next mode is the third harmonic:

$$
f_3 = 3(3430) = 10.3\ \text{kHz}.
$$

(c) Yes, comfortably, $10.3$ kHz is well within the $20$ Hz to $20$ kHz range, though the ear is considerably less sensitive there than at $3.4$ kHz.

Therefore, the canal contributes resonances at about $3.4$ kHz and $10$ kHz, and the first of these coincides with the region of greatest sensitivity.
:::

:::{exercise}
:label: ex-the-ear-2

*(Moderate)* The eardrum has area $55$ mm² and the oval window $3.2$ mm². The ossicular lever gives a force advantage of $1.3$. (a) Find the total pressure gain. (b) Express it in decibels. (c) What would the gain be if the lever were absent?
:::

:::{solution} ex-the-ear-2
:label: sol-the-ear-2
:class: dropdown

(a) Pressure gain is the area ratio times the lever ratio:

$$
G = \frac{55}{3.2}\times1.3 = 17.2 \times 1.3 = 22.3.
$$

(b) For a pressure ratio, in decibels:

$$
20\log_{10}(22.3) = 27.0\ \text{dB}.
$$

(c) Without the lever, $G = 17.2$, which is $20\log_{10}(17.2) = 24.7$ dB.

Therefore, the lever contributes only $2.3$ dB of the $27$ dB total. The area ratio does almost all of the work.
:::

:::{exercise}
:label: ex-the-ear-3

*(Moderate)* The threshold of hearing at $1$ kHz corresponds to an eardrum displacement of about $1\times10^{-11}$ m. (a) Compare this with the diameter of a hydrogen atom, about $1\times10^{-10}$ m. (b) At the threshold of pain, $120$ dB above threshold, what is the displacement?
:::

:::{solution} ex-the-ear-3
:label: sol-the-ear-3
:class: dropdown

(a) The ratio is

$$
\frac{1\times10^{-11}}{1\times10^{-10}} = 0.1,
$$

so the threshold displacement is about a tenth of an atomic diameter.

(b) A level difference of $120$ dB in pressure corresponds to an amplitude ratio of

$$
10^{120/20} = 10^{6}.
$$

So the displacement at the threshold of pain is

$$
(1\times10^{-11}\ \text{m})(10^{6}) = 1\times10^{-5}\ \text{m} = 10\ \mu\text{m}.
$$

Therefore, the eardrum's working range runs from a tenth of an atomic diameter to about a hundredth of a millimeter: a millionfold span, handled by one membrane.
:::

:::{exercise}
:label: ex-the-ear-4

*(Straightforward)* The basilar membrane is $35$ mm long and maps roughly logarithmically onto $20$ Hz to $20$ kHz. (a) How many octaves does it span? (b) How many millimeters does one octave occupy? (c) A semitone?
:::

:::{solution} ex-the-ear-4
:label: sol-the-ear-4
:class: dropdown

(a) The range is a factor of $1000$, so

$$
n = \log_2(1000) = 9.97 \approx 10\ \text{octaves}.
$$

(b) Dividing the length by the octaves:

$$
\frac{35\ \text{mm}}{9.97} = 3.5\ \text{mm per octave}.
$$

(c) One semitone is a twelfth of an octave:

$$
\frac{3.5\ \text{mm}}{12} = 0.29\ \text{mm}.
$$

Therefore, a semitone occupies about three tenths of a millimeter of membrane. Given that the just-noticeable frequency difference is far smaller than a semitone ([Chapter 8](#ch-pitch-and-consonance)), the ear plainly resolves pitch far more finely than this spacing alone would allow, which is one of several reasons place cannot be the whole story.
:::

:::{exercise}
:label: ex-the-ear-5

*(Moderate)* A musician is exposed to $94$ dB for an eight-hour rehearsal day. (a) Using a $3$ dB exchange rate with a limit of $85$ dB for eight hours, what is the permitted daily exposure at $94$ dB? (b) By how many times has the musician exceeded it? (c) What attenuation of earplug would bring them inside the limit?
:::

:::{solution} ex-the-ear-5
:label: sol-the-ear-5
:class: dropdown

(a) Each $3$ dB halves the allowed time. From $85$ to $94$ dB is $9$ dB, or three halvings:

$$
T = \frac{8\ \text{h}}{2^3} = 1\ \text{h}.
$$

(b) Eight hours against one hour permitted: a factor of $8$.

(c) To come back inside the limit the level must drop by $9$ dB, so a plug of $9$ dB attenuation or more: the lowest rating musician's plugs are commonly made in.

Therefore, a $94$ dB rehearsal day is eight times the safe dose, and the standard $9$ dB musician's plug is exactly enough to fix it.
:::

:::{exercise}
:label: ex-the-ear-6

*(Moderate)* A violinist measures $103$ dB at their left ear and $91$ dB at their right. (a) Find the permitted daily exposure for each ear. (b) Explain why the asymmetry arises and what practical step would reduce it.
:::

:::{solution} ex-the-ear-6
:label: sol-the-ear-6
:class: dropdown

(a) Using the $3$ dB rule from $85$ dB for $8$ h:

Left ear, $103 - 85 = 18$ dB, six halvings:

$$
T = \frac{8}{2^6} = 0.125\ \text{h} = 7.5\ \text{minutes}.
$$

Right ear, $91 - 85 = 6$ dB, two halvings:

$$
T = \frac{8}{2^2} = 2\ \text{h}.
$$

(b) The left ear is very close to the instrument, perhaps $15$ cm from the f-holes, while the right is nearly an arm's length away and shadowed by the head. The inverse-square law of [Chapter 2](#ch-wave-motion) accounts for most of the $12$ dB.

The practical step is an earplug in the left ear at minimum. Left-ear hearing loss is a well-documented occupational pattern among violinists and violists, and it follows directly from this geometry.
:::

:::{exercise}
:label: ex-the-ear-7

*(Straightforward)* A sound at $250$ Hz produces its peak response about $26$ mm from the base of the cochlea, and a sound at $4$ kHz about $12$ mm from the base. (a) How far apart are the two peaks? (b) Using $3.5$ mm per octave, check this against the musical interval between the two frequencies.
:::

:::{solution} ex-the-ear-7
:label: sol-the-ear-7
:class: dropdown

(a) $26 - 12 = 14$ mm.

(b) The frequency ratio is $4000/250 = 16$, which is

$$
\log_2(16) = 4\ \text{octaves}.
$$

At $3.5$ mm per octave that predicts

$$
4 \times 3.5 = 14\ \text{mm}.
$$

Therefore, the two agree exactly, confirming that the map really is logarithmic: four octaves is four octaves' worth of membrane wherever on the cochlea it falls.
:::

:::{exercise}
:label: ex-the-ear-8

*(Moderate)* The outer hair cells sharpen the cochlear response by raising its effective $Q$ from about $1$ to about $10$ at low levels. Using the definitions of [Chapter 4](#ch-resonance): (a) By what factor does the bandwidth at $1$ kHz narrow? (b) Express each bandwidth in semitones.
:::

:::{solution} ex-the-ear-8
:label: sol-the-ear-8
:class: dropdown

(a) Bandwidth is $\Delta f = f_0/Q$, so raising $Q$ from $1$ to $10$ narrows the bandwidth by a factor of $10$.

At $1$ kHz: from $\Delta f = 1000$ Hz to $\Delta f = 100$ Hz.

(b) A bandwidth of $1000$ Hz centered on $1000$ Hz runs roughly $500$ to $1500$ Hz:

$$
12\log_2(1500/500) = 12(1.585) = 19\ \text{semitones}.
$$

A bandwidth of $100$ Hz runs roughly $950$ to $1050$ Hz:

$$
12\log_2(1050/950) = 12(0.1444) = 1.7\ \text{semitones}.
$$

Therefore, the active amplifier takes the ear's frequency resolution from about an octave and a half down to under two semitones. Losing the outer hair cells does not merely make sounds quieter; it makes them run together, which is exactly what people with noise damage report.
:::

:::{exercise}
:label: ex-the-ear-9

*(Straightforward)* A person's hearing threshold at $4$ kHz has shifted by $35$ dB. (a) By what factor in intensity has their sensitivity fallen? (b) A cymbal produces $4$ kHz energy at $70$ dB SPL at their seat. Do they hear it?
:::

:::{solution} ex-the-ear-9
:label: sol-the-ear-9
:class: dropdown

(a) A $35$ dB shift in intensity terms is

$$
10^{35/10} = 3.2\times10^{3},
$$

so the sound must be about $3200$ times more intense to be detected.

(b) Their threshold at $4$ kHz is now $35$ dB SPL rather than roughly $0$. A $70$ dB SPL cymbal is $35$ dB above their threshold, so yes, they hear it, but at what a normal listener would experience as a much quieter sound.

Therefore, moderate high-frequency loss does not silence the cymbal; it dulls it. Such loss often goes unnoticed for a long time, and is usually detected first by an audiogram rather than by the person.
:::

:::{exercise}
:label: ex-the-ear-10

*(Moderate)* Estimate the cochlea's "channel count" by treating it as a bank of filters each one critical band wide. Take the critical band as roughly a third of an octave across most of the range, and the range as $10$ octaves. (a) How many filters is that? (b) Compare with the number of inner hair cells, about $3500$.
:::

:::{solution} ex-the-ear-10
:label: sol-the-ear-10
:class: dropdown

(a) At three filters per octave over ten octaves:

$$
N = 3 \times 10 = 30\ \text{filters}.
$$

(b) There are about $3500$ inner hair cells, so roughly

$$
\frac{3500}{30} \approx 120
$$

inner hair cells per critical band.

Therefore, the cochlea has of order thirty independent frequency channels but more than a hundred sensors in each. The redundancy is what allows the system to average away noise, which is how a detector working below the thermal-motion limit can function at all, and it also explains why substantial hair-cell loss can occur before any change is noticed.
:::

:::{exercise}
:label: ex-the-ear-11

*(Moderate)* Phase locking in the auditory nerve fails above about $4.5$ kHz. (a) What is the period of a $4.5$ kHz tone? (b) A nerve fiber's refractory period, the minimum time between firings, is about $1$ ms. How many cycles of a $4.5$ kHz tone pass during it? (c) Explain how the volley principle allows the population to encode a period no single fiber can follow.
:::

:::{solution} ex-the-ear-11
:label: sol-the-ear-11
:class: dropdown

(a) $T = 1/4500 = 2.2\times10^{-4}$ s, or $0.22$ ms.

(b) $1\ \text{ms}/0.22\ \text{ms} = 4.5$ cycles.

(c) No single fiber can fire on every cycle: it must sit out at least four of every five. But each fiber, when it does fire, fires at the same *phase*. Different fibers sit out different cycles, so pooling across many fibers reconstructs a firing pattern with a peak on every cycle, even though no individual contributor managed one.

Therefore, the population encodes a periodicity far faster than any of its members. This is the volley principle, and it is the mechanism that gives the auditory system timing information across the whole musically useful range.
:::

:::{exercise}
:label: ex-the-ear-12

*(Moderate)* A musician can either (a) move from $2$ m to $4$ m from a loud source, or (b) wear a $9$ dB earplug. Which gives more protection, and by how much? Assume the source radiates freely.
:::

:::{solution} ex-the-ear-12
:label: sol-the-ear-12
:class: dropdown

(a) Doubling the distance in a free field reduces the level by

$$
20\log_{10}(2) = 6.0\ \text{dB}.
$$

(b) The earplug gives $9$ dB.

The earplug wins by $3$ dB, which, on the $3$ dB exchange rate, is a further factor of two in safe exposure time.

Therefore, the plug is better, and the two combine: moving *and* plugging gives $15$ dB, which is a factor of $32$ in permitted time. It is also worth noting that in a real hall the distance benefit would be less than $6$ dB, because beyond the critical distance of [Chapter 2](#ch-wave-motion) the reverberant field stops falling off with distance at all.
:::

:::{exercise}
:label: ex-the-ear-13

*(Challenging)* Explain quantitatively why a foam earplug is a poor choice for a musician, given that it typically attenuates $10$ dB at $250$ Hz and $35$ dB at $4$ kHz, while a musician's plug attenuates about $15$ dB at both.
:::

:::{solution} ex-the-ear-13
:label: sol-the-ear-13
:class: dropdown

The foam plug's attenuation differs by

$$
35 - 10 = 25\ \text{dB}
$$

between $250$ Hz and $4$ kHz. In amplitude terms the high frequencies are attenuated

$$
10^{25/20} = 18
$$

times more than the low ones.

The effect is a drastic tilt of the spectrum: an instrument's fundamental passes nearly unaffected while its upper harmonics are cut to a twentieth. Since [Chapter 5](#ch-fourier-and-timbre) showed that the upper harmonics are what timbre is made of, the result is a muffled, boxy sound in which a player can neither judge their own tone nor hear the rest of the ensemble properly.

The musician's plug attenuates by the same $15$ dB at both ends, so the spectrum is preserved and only the level changes.

Therefore, the foam plug offers more attenuation but destroys the information the musician needs, so it gets taken out, and a plug that is not worn attenuates nothing at all.
:::

:::{exercise}
:label: ex-the-ear-14

*(Challenging)* A tone at $200$ Hz and a tone at $3000$ Hz are played at the same level. (a) Using the traveling-wave picture, explain which is more effective at masking the other. (b) A recording engineer complains that a bass guitar is "burying" a hi-hat. Suggest, from this chapter's physics, why reducing the bass level helps more than raising the hi-hat.
:::

:::{solution} ex-the-ear-14
:label: sol-the-ear-14
:class: dropdown

(a) The $200$ Hz tone. Its traveling wave must run almost the full length of the basilar membrane to reach its own place near the apex, and it excites the $3000$ Hz region on the way past. The $3000$ Hz wave peaks near the base and dies before reaching the apex, so it never disturbs the low-frequency region at all.

(b) Raising the hi-hat increases the total level without changing the fact that the bass is still spreading excitation across the hi-hat's region, and a louder mix simply moves both closer to the point where masking is strongest. Reducing the bass removes the masker itself, which lets the hi-hat through at a level it was already loud enough to reach.

Therefore, masking is asymmetric, and the remedy is to attend to the masker rather than the masked. Mixing engineers talk about "making space" by cutting rather than boosting for exactly this reason: it is the asymmetry the traveling wave predicts.
:::
