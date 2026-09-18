---
title: "The Singing Voice"
short_title: "Chapter 13. The Singing Voice"
label: ch-the-singing-voice
numbering:
  enumerator: "13.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 13.1, 13.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-13-the-singing-voice.pdf
    chapter: 13
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Describe the voice as a source-filter system, and identify the anatomical structure serving as each.
- Explain how the vocal folds oscillate, and why the oscillation is self-sustaining rather than driven at a chosen frequency.
- Relate the fundamental frequency of phonation to vocal-fold length, mass, and tension, and explain the typical difference between adult voices.
- Describe the spectrum of the glottal source, and state approximately how its harmonic amplitudes fall with frequency.
- Define a formant, explain how the vocal tract produces formants, and calculate the formant frequencies of a uniform tube of the length of the adult vocal tract.
- Identify vowels from the frequencies of the first two formants, and read a vowel chart in the $F_1$-$F_2$ plane.
- Explain why the vowel of a sung note is harder to identify at high pitch, in terms of harmonic spacing relative to formant width.
- Describe the vocal registers and what changes physically between them.
- Explain the singer's formant, state approximately where it lies, and explain how it lets an unamplified soloist be heard over an orchestra.

### Introduction

The voice is the oldest instrument and the only one everybody has. It is also the one that shows most clearly a model this book has been assembling since [Chapter 4](#ch-resonance): the **source–filter model**.

The idea is that an instrument can be described as two independent stages. A **source** produces a raw signal with a rich spectrum, and a **filter** shapes that spectrum by emphasizing some frequencies and suppressing others. The two can be varied independently, and what a listener hears is the product.

In the voice, the separation is unusually clean. The **vocal folds** are the source: they chop the airflow into puffs, producing a harmonic series whose fundamental is the pitch. The **vocal tract**, the tube from the larynx to the lips, is the filter: its resonances, called **formants**, emphasize whichever harmonics fall near them.

The crucial point, and the one that makes speech possible at all, is that **the two are independent**. You can change the pitch without changing the vowel, by tensing the folds; and you can change the vowel without changing the pitch, by moving the tongue and jaw. Singing is exactly the ability to do both at once, deliberately.

This chapter also explains one thing that ought to be impossible: how a single unamplified voice is heard over a hundred-piece orchestra. The answer is a trick of spectrum placement, and it is a good one.

## The Voice as Source and Filter

### Two Independent Stages

```{figure} ../images/ch13-source-filter.svg
:label: fig:ch13-source-filter
:alt: Three panels. Left, a harmonic line spectrum falling steadily, labeled source, the vocal folds. Center, a decibel plot of a filter with three labeled formant peaks, labeled the vocal tract. Right, the resulting output spectrum with the filter's shape visible as an envelope over the harmonics.

The source–filter model. The source supplies a harmonic series at the pitch being sung. The filter has fixed resonances. The output is their product: the same harmonics, with their amplitudes reshaped. Note that the filter is drawn in decibels, the third formant is some $35$ dB below the first, and on a linear axis it would be invisible.
```

The model is an idealization, and the idealization is good. There *is* some interaction, the tract's pressure fluctuations feed back on the folds, and at extremes of range a singer can exploit this deliberately, but for most purposes the two stages can be treated as independent, and doing so explains a great deal.

### Why the Model Works

The reason the separation holds so well is a difference of impedance, and it is the same argument as [Chapter 11](#ch-wind-instruments)'s reed.

The vocal folds present a high impedance to the tract: they are relatively massive and stiff, and the tract's pressure oscillations are not strong enough to push them around much. So the tract does not tell the folds what to do, and the source frequency is set by the folds alone.

This is the **opposite** of a wind instrument, where the bore controls the reed. Acoustically, then, the voice is more like a string instrument, source sets pitch, resonator shapes tone, than like the wind instrument it superficially resembles.

### The Anatomy in Brief

Three parts, in the order air meets them.

The **lungs and diaphragm** supply a steady pressure: a few hundred pascals above atmospheric for normal speech, more for loud singing. This is the power supply, and the entire art of breath support is keeping it steady.

The **larynx** houses the vocal folds: two layered flaps of muscle and ligament, about $17$–$25$ mm long in adult men and $12$–$17$ mm in adult women, covered in mucous membrane. They can be brought together to close the airway or held apart to breathe.

The **vocal tract** runs from the folds to the lips, about $17$ cm in an adult man. It includes the pharynx, the mouth, and, when the soft palate is lowered, the nasal cavity. Its shape can be changed continuously by the tongue, jaw, lips, and larynx height.

## The Source: The Vocal Folds

### Self-Sustained Oscillation

The folds are not vibrated by anything. They oscillate **themselves**, driven by a steady airflow, and the mechanism is a feedback loop with no oscillating input at all.

The cycle runs like this. Air pressure below the closed folds builds until it forces them apart. Air rushes through the gap, and, by the Bernoulli effect, the fast-moving air in the narrow gap is at *reduced* pressure, which sucks the folds back together. Their own elasticity helps. They close, the pressure builds again, and the cycle repeats.

The essential feature is that the folds do not move as a single stiff object. They have a layered structure, and the mucous membrane travels over the deeper tissue as a surface wave, so the lower edge opens before the upper edge and closes before it too. That phase difference between the opening and the closing is what allows net energy to be extracted from a steady airflow, without it, the work done pushing the folds open would exactly cancel the work recovered as they close, and the oscillation would die.

```{animation} ch13-glottal-cycle
:label: fig:ch13-glottal-cycle
:alt: Top, the glottal area over two cycles, opening smoothly, closing rapidly and then staying shut for part of each cycle. Bottom, the rate of change of airflow, showing a sharp negative spike at each closure.

One glottal cycle. The opening is gradual and the closing is abrupt, and the folds stay shut for a substantial fraction of each cycle. **The sharp closure is what makes the sound**: it produces a rapid change in airflow, which is a broadband excitation of the tract, in the same way that a sharp-cornered waveform contains high harmonics ([Chapter 5](#ch-fourier-and-timbre)).
```

```{video} https://www.youtube.com/watch?v=9kHdhbEnhoA
:video-title: High-Speed Video of the Vocal Folds
:label: fig:ch13-vocal-folds-video
:alt: High-speed laryngeal imaging shows the vocal folds repeatedly opening and closing during phonation.

High-speed laryngeal imaging slows the vocal folds' oscillation enough to reveal the opening and closing cycle. The footage shows the vibrator that supplies the source in the source--filter model.
```

### What Sets the Fundamental

The folds are a mass–spring system, so [Chapter 1](#ch-sound-and-shm) applies: frequency rises with tension and falls with mass.

| Change | Effect on pitch | How a singer does it |
|---|---|---|
| Increase fold tension | Higher | Cricothyroid muscle tilts the thyroid cartilage |
| Increase effective mass | Lower | Thicker, looser folds; chest voice |
| Increase subglottal pressure | Slightly higher | More breath pressure |

That last row is a nuisance for singers: getting louder tends to sharpen the pitch, so a singer must actively compensate. It is also why breath support and intonation are taught together.

The anatomical difference between voice types is straightforward. Adult male folds are longer and more massive, hence roughly $85$–$180$ Hz in speech, while adult female folds are shorter and lighter, at roughly $165$–$255$ Hz. The ratio is close to a factor of two, so men and women speaking naturally are about an octave apart.

### The Spectrum of the Glottal Pulse

The glottal waveform is not a sine. It is a series of pulses, and [Chapter 5](#ch-fourier-and-timbre) guarantees that a periodic pulse train has a full harmonic series.

The amplitudes fall at roughly $12$ dB per octave: that is, as $1/n^2$. This is the **source spectrum**, and it is important that it is smooth: it has no peaks of its own, so every peak in the output belongs to the filter.

A singer *can* change the source spectrum. Pressed, forceful phonation with a sharper closure produces a brighter source; breathy phonation with incomplete closure produces a weaker, noisier one with a steeper roll-off. These are real timbral controls, but they are secondary to what the tract does.

## The Filter: The Vocal Tract

### A Tube, Stopped at One End

To a first approximation the vocal tract is a uniform tube about $17$ cm long, closed at the glottis and open at the lips: a **stopped pipe**, exactly as in [Chapter 3](#ch-superposition):

$$
f_n = n\,\frac{v}{4L}, \qquad n = 1, 3, 5, \ldots
$$

With $L = 0.17$ m and $v = 350$ m/s (warm, moist air):

$$
f_1 = \frac{350\ \text{m/s}}{4(0.17\ \text{m})} = 515\ \text{Hz},
\qquad f_3 = 1545\ \text{Hz},
\qquad f_5 = 2575\ \text{Hz}.
$$

Roughly $500$, $1500$, $2500$ Hz, and those are, to a remarkable degree, the measured formant frequencies of a neutral vowel. A crude stopped-pipe model gets the human vocal tract approximately right.

### Formants

A **formant** is a resonance of the vocal tract. It is a property of the *tube*, not of the pitch being sung, and this is the single most important fact in the chapter.

Formants are numbered upward: $F_1$, $F_2$, $F_3$. Each has a bandwidth of $50$–$150$ Hz, which is a $Q$ of order ten, deliberately low, so that the tract responds usefully over a wide range of pitches rather than only at isolated frequencies ([Chapter 4](#ch-resonance)).

**Formants do not move when the pitch does.** Sing "ah" on a low note and then on a high one: the fundamental changes, every harmonic changes, and the formants stay exactly where they were, because the shape of your throat has not changed. That is why the vowel is still recognizable.

::::{tip} Worked example: what leaves the mouth
*A baritone sings $F_0 = 110$ Hz. His glottal source spectrum falls at $12$ dB per octave, that is, amplitude $\propto 1/n^2$. His first formant sits at $550$ Hz, exactly on the 5th harmonic, with a peak gain of $15$ dB over the surrounding response. Find the level of the 5th harmonic relative to the fundamental (a) in the source alone, (b) after the filter.*

(a) The 5th harmonic's source amplitude, relative to the fundamental's, is $1/5^2 = 1/25$:

$$
20\log_{10}\!\left(\frac{1}{25}\right) = -28\ \text{dB}.
$$

(b) The formant sits exactly on this harmonic, adding its full $15$ dB of peak gain:

$$
-28 + 15 = -13\ \text{dB}.
$$

Therefore, on its way from the folds to the lips, the 5th harmonic starts $28$ dB below the fundamental and leaves only $13$ dB below it: the formant has clawed back more than half its disadvantage. This is the source–filter model doing exactly what its name promises, source and filter multiply, which in decibels means their contributions simply add, and it is why a formant's placement matters as much as a source's raw output.
::::

### Shaping the Tube

A singer changes formants by changing the tract's shape, and the controls map onto the first two formants in a usefully simple way.

**$F_1$ tracks how open the tract is.** Constricting the tract near the front raises $F_1$; opening the jaw raises it. Roughly, $F_1$ says how open your mouth is.

**$F_2$ tracks where the tongue is.** A tongue hump far forward raises $F_2$; a tongue pulled back lowers it.

**$F_3$ and above** depend on finer details, including the space under the tongue and the position of the larynx, and §13.5 shows that $F_3$ is where trained singing does something distinctive.

```{video} https://www.youtube.com/watch?v=J3TwTb-T044
:video-title: Singing in the MRI: Making the Voice Visible
:label: fig:ch13-singing-mri-video
:alt: Real-time magnetic resonance images show a singer's tongue, jaw, lips, and vocal tract changing shape.

Real-time MRI makes the filter half of the voice visible. As Tyley Ross changes vowels and pitch, the tongue, jaw, lips, and vocal tract reshape the resonant cavities that determine the formants.
```

## Vowels, Registers, and Range

### Vowels in the Formant Plane

Because $F_1$ and $F_2$ are controlled by two roughly independent gestures, vowels occupy a two-dimensional space.

```{figure} ../images/ch13-vowel-chart.svg
:label: fig:ch13-vowel-chart
:alt: A scatter plot of five vowels positioned by their first and second formant frequencies, with both axes inverted so that the layout matches the traditional vowel quadrilateral, with ee at high F2 and low F1 and ah at low F2 and high F1.

Vowels plotted by their first two formants. With both axes reversed, the plot reproduces the vowel quadrilateral that phoneticians drew from articulation long before formants could be measured, which is a nice confirmation that the acoustic and articulatory descriptions are the same thing.
```

The identification is robust. Two speakers with very different vocal tract lengths produce quite different absolute formant frequencies for the same vowel, yet listeners have no difficulty: the auditory system evidently normalizes by the speaker rather than reading absolute values.

```{audio} ch13-vowel-ee, ch13-vowel-ah, ch13-vowel-oo
:names: ee, ah, oo
:figure: ../images/ch13-vowels.svg
:label: fig:ch13-vowels
:transcript: Three sung vowels at the same pitch. They are clearly different vowels and clearly the same note, sung by the same voice.

Three vowels at $130$ Hz. The source is identical in all three, the same harmonic series at the same pitch. Only the filter differs, and it is enough to produce three recognizably different speech sounds.
```

### Formant Tuning at High Pitch

Now a problem that is specific to singing, and it is the reason opera has the reputation it does for incomprehensibility.

The tract's formants are sampled by the harmonics of whatever is being sung. At a low pitch the harmonics are closely spaced, so there is always one near any formant, and the formant's peak is well represented in the output. At a high pitch they are widely spaced, and a formant can fall in the gap between two harmonics, in which case there is *nothing in the output* to tell the listener the formant is there.

```{figure} ../images/ch13-formant-tuning.svg
:label: fig:ch13-formant-tuning
:alt: Two panels showing the vocal tract filter envelope with harmonic lines beneath it. At 220 Hz the harmonics are dense and several land near the first formant; at 880 Hz they are widely spaced and none lands near it.

The same vowel, sung at $220$ Hz and $880$ Hz. At the low pitch the harmonics sample the filter closely and the formant peaks are faithfully rendered. At the high pitch the first formant falls between harmonics, and its peak simply does not appear in the output.
```

```{audio} ch13-ah-low, ch13-ah-high
:names: "ah" at 196 Hz, "ah" at 784 Hz
:figure: ../images/ch13-formant-tuning.svg
:label: fig:ch13-formant-tuning-audio
:transcript: The same vowel at two pitches two octaves apart. The low one is clearly "ah"; the high one is much less definite, and could be almost any open vowel.

The vowel at a low and a high pitch, with an identical filter. The vowel identity degrades at the top, and no amount of effort by the singer can put information into a frequency region where there is no harmonic to carry it.
```

Sopranos deal with this by **formant tuning**: they modify the vowel, opening the jaw to raise $F_1$ until it coincides with a harmonic, usually the fundamental itself. The note becomes much louder, because a harmonic is now sitting on a resonance peak, and the vowel becomes whatever $F_1$ placement requires. Above about C6 a soprano is essentially singing one vowel whatever the text says, and this is a physical necessity rather than a failure of technique.

### Registers and the Passaggio

**Registers** are distinct modes of vocal fold vibration, and they are physically real rather than metaphorical.

In **chest voice** (or *modal* register) the folds vibrate over their full depth, closing completely on each cycle. The tone is strong and rich in harmonics.

In **head voice** (or *falsetto*) only the thin upper edges vibrate, and the folds may not close completely. The tone is weaker and much poorer in harmonics.

Between them lies the ***passaggio***, where the singer must change from one mode to the other. Left to itself the transition is abrupt and audible, the "break", and a great deal of vocal training consists of learning to blend across it by adjusting fold tension and tract shape together so that the change is gradual.

The **whistle register**, available to some sopranos above about C6, involves only a small portion of the folds and produces a nearly pure tone with very few harmonics, which is exactly why it sounds flute-like and why the words are entirely lost.

## Being Heard

### The Singer's Formant

Here is the problem. An orchestra playing fortissimo produces around $100$ dB in the hall. A single unamplified human voice produces perhaps $90$ dB at a meter, and less by the time it reaches the audience. Adding one voice to a hundred instruments should be inaudible, by [Chapter 7](#ch-loudness)'s addition rule.

Yet an opera singer is heard clearly. The trick is not loudness but **spectral placement**.

```{figure} ../images/ch13-singers-formant.svg
:label: fig:ch13-singers-formant
:alt: Level against frequency showing an orchestra's spectrum falling steeply above 500 Hz, an untrained voice following it down, and a trained voice with a strong peak near 2.9 kHz that rises well above the orchestra's level there.

Why a trained soloist is heard. An orchestra's spectrum is concentrated below about $500$ Hz and falls away steeply. A trained voice puts a strong resonance near $2.9$ kHz, precisely where the orchestra has little energy and where the ear is most sensitive ([Chapter 7](#ch-loudness)).
```

The **singer's formant** is a strong peak around $2.8$–$3.2$ kHz, and it is produced by clustering $F_3$, $F_4$, and $F_5$ together. The mechanism is lowering the larynx, which widens the pharynx just above it and creates a small, separately resonant cavity; that cavity's resonance coincides with the upper formants and reinforces them.

Its effect is large: $20$ dB or more of extra output in that band.

```{audio} ch13-voice-plain, ch13-voice-trained
:names: Without singer's formant, With singer's formant
:figure: ../images/ch13-singers-formant.svg
:label: fig:ch13-singers-formant-audio
:transcript: The same voice against the same orchestral background twice. In the first it is buried and hard to follow; in the second it cuts through clearly, without being obviously louder overall.

A voice mixed with a low-biased orchestral background, with and without the singer's formant. The overall level of the voice is the same in both. What has changed is *where* its energy sits.
```

### Competing With an Orchestra

Three features of the solution are worth drawing together, because it is a genuinely clever piece of physics that nobody designed.

It exploits a **gap in the competition**. The orchestra's energy is concentrated low, so the $3$ kHz region is comparatively empty.

It exploits the **ear's sensitivity peak**. [Chapter 6](#ch-the-ear) showed the ear canal resonates near $3.4$ kHz, and [Chapter 7](#ch-loudness) showed that hearing is most sensitive there. A decibel spent in that band buys more loudness than a decibel spent anywhere else.

It exploits **masking asymmetry**. [Chapter 7](#ch-loudness) showed that masking spreads upward far more readily than downward, so low-frequency orchestral energy masks the voice's low harmonics severely and its $3$ kHz region much less.

The same logic appears elsewhere. A violin's **bridge hill** is at $3$ kHz ([Chapter 10](#ch-string-instruments)), and a trumpet's bell radiates most efficiently in the same region ([Chapter 11](#ch-wind-instruments)). Several unrelated instrument traditions converged on the same band, because that is where the ear is listening.

### Vibrato, Projection, and the Limits of the Voice

**Vibrato** is a periodic modulation of pitch, typically $5$–$7$ Hz and $\pm 50$ to $\pm100$ cents. It arises partly from a natural oscillation in the laryngeal muscles and partly from training.

Two things it does. It makes a voice **stand out** against a steady background, because the auditory system groups components that change together and separates those that do not: a moving signal against a static one is easier to follow. And because the harmonics sweep back and forth across the formant peaks, vibrato *samples* the filter over a range rather than at a point, which fills in the missing information of §13.4 and makes the vowel more identifiable at high pitch than a steady tone would be.

Finally, the limits. The voice is a small instrument. A trained singer produces perhaps $1$ mW of acoustic power at full voice, comparable to a single violin, and against sixty of them. Its range is about two and a half octaves for most singers and rarely more than three. Its dynamic range is far narrower than an orchestra's.

Everything in this chapter is, in one way or another, a response to those constraints. The voice cannot win on power, so it wins on placement.

## Summary

- **The voice is a source–filter system.** The vocal folds are the source, producing a harmonic series at the pitch; the vocal tract is the filter, whose resonances, **formants**, shape it. The two are essentially independent, so pitch and vowel can vary separately.
- **The folds oscillate on their own**, driven by steady airflow. The layered structure makes the upper and lower edges move out of phase, which is what allows net energy extraction from a steady flow.
- **The sharp closure makes the sound.** A rapid cut-off of airflow is a broadband excitation, and the glottal source spectrum falls smoothly at about $12$ dB per octave with no peaks of its own.
- **Fundamental frequency rises with fold tension and falls with fold mass**, and rises slightly with breath pressure; so loud singing tends to go sharp.
- **The tract is approximately a $17$ cm stopped pipe**, giving formants near $500$, $1500$, $2500$ Hz. $F_1$ tracks jaw opening; $F_2$ tracks tongue position; vowels occupy the $F_1$–$F_2$ plane.
- **Formants do not move when the pitch does**, so a vowel survives across a singer's range, up to a point.
- **At high pitch the harmonics are too widely spaced to sample the formants.** Sopranos respond with **formant tuning**, opening the jaw to put $F_1$ on a harmonic, which gains loudness and loses vowel identity.
- **Registers are distinct modes of fold vibration**: chest voice uses the full fold depth, falsetto only the edges, and the *passaggio* between them is what training smooths.
- **The singer's formant**, near $2.9$ kHz, is produced by clustering $F_3$ to $F_5$ via a lowered larynx. It exploits a gap in the orchestra's spectrum, the ear's sensitivity peak, and the asymmetry of masking, and it is worth $20$ dB where it matters.
- **Vibrato** helps the ear separate the voice from a steady background, and sweeps the harmonics across the formants, restoring some of the information lost at high pitch.

## Check Your Understanding

Five short, auto-graded questions cycle within one compact activity, using five different response styles.

:::{h5p} ch13-chapter-review
:label: check:ch13-chapter-review
:title: Chapter 13 interactive review

1. **Multiple response.** Why does the singer’s formant near $2.9$ kHz improve projection? Consider the orchestral spectrum, ear sensitivity, masking, and the vocal fundamental.
2. **True or false.** In the source–filter model, the vocal folds can change pitch while the vocal tract largely preserves the vowel filter.
3. **Drag the words.** Match vocal folds, vocal tract, jaw opening, and tongue position to the harmonic source, formant filtering, $F_1$, and $F_2$.
4. **Fill in the blanks.** A roughly ___ cm tract has formants near $500$, ___, and $2500$ Hz.
5. **Mark the words.** Identify two vocal registers: “Chest voice uses more of the fold depth, while falsetto uses mainly the edges; the passaggio is the transition between them.”
:::

## Conceptual Questions

1. Explain what it means to say the voice is a source–filter system, and give one observation that shows the two stages are independent.

2. Explain why the vocal tract controls the *timbre* of the voice but not its pitch, and contrast this with a clarinet.

3. Explain why the abrupt closure of the vocal folds, rather than their opening, is what produces most of the sound.

4. A singer gets louder and the pitch drifts sharp. Explain the mechanism.

5. Explain why a vowel remains recognizable when the same person sings it an octave higher, and why this eventually fails.

6. A soprano singing above C6 is hard to understand whatever the language. Explain why this is a physical limitation rather than a matter of diction.

7. Explain how a single unamplified voice is heard over an orchestra, naming the three separate effects that make it work.

8. Explain two distinct benefits of vibrato, one about separating the voice from the background and one about vowel identity.

## Problems

:::{exercise}
:label: ex-the-singing-voice-1

*(Straightforward)* Model the vocal tract as a stopped pipe of length $17.5$ cm, with $v = 350$ m/s in warm moist air. (a) Find the first three formant frequencies. (b) Compare with the measured neutral-vowel values of about $500$, $1500$, $2500$ Hz.
:::

:::{solution} ex-the-singing-voice-1
:label: sol-the-singing-voice-1
:class: dropdown

(a) A stopped pipe gives odd harmonics of $v/4L$:

$$
f_1 = \frac{350\ \text{m/s}}{4(0.175\ \text{m})} = 500\ \text{Hz},
\quad f_3 = 1500\ \text{Hz},
\quad f_5 = 2500\ \text{Hz}.
$$

(b) The agreement is essentially exact.

Therefore a uniform tube of the right length predicts the neutral vowel's formants almost perfectly. Departures from this pattern are what produce the *other* vowels: a vowel is a deviation from the neutral tube.
:::

:::{exercise}
:label: ex-the-singing-voice-2

*(Moderate)* An adult male tract is $17.5$ cm and an adult female tract about $15$ cm. (a) Find the neutral formants for each. (b) Express the difference as a musical interval. (c) How do listeners cope?
:::

:::{solution} ex-the-singing-voice-2
:label: sol-the-singing-voice-2
:class: dropdown

(a) Male: $500$, $1500$, $2500$ Hz. Female, with $L = 0.15$ m:

$$
f_1 = \frac{350\ \text{m/s}}{4(0.15\ \text{m})} = 583\ \text{Hz},
\quad f_3 = 1750\ \text{Hz},
\quad f_5 = 2917\ \text{Hz}.
$$

(b) The ratio is $583/500 = 1.167$:

$$
1200\log_2(1.167) = 267\ \text{cents},
$$

between a whole tone and a minor third.

(c) The auditory system **normalizes** for the speaker rather than reading absolute formant values. It uses the pattern of formants relative to one another, and cues from the speaker's fundamental and from surrounding speech, to calibrate. A child, a woman, and a man can all say "ah" and be understood as saying the same thing despite formants differing by a factor of $1.3$.
:::

:::{exercise}
:label: ex-the-singing-voice-3

*(Moderate)* A bass sings at $F_0 = 98$ Hz and a soprano at $F_0 = 880$ Hz, both with $F_1 = 700$ Hz. (a) Which harmonic is closest to $F_1$ in each case? (b) How far is it, in hertz? (c) Comment on vowel clarity.
:::

:::{solution} ex-the-singing-voice-3
:label: sol-the-singing-voice-3
:class: dropdown

(a) Bass: $700/98 = 7.14$, so the 7th harmonic at $686$ Hz. Soprano: $700/880 = 0.80$, so the fundamental at $880$ Hz is the nearest, there is nothing below it.

(b) Bass: $700 - 686 = 14$ Hz away. Soprano: $880 - 700 = 180$ Hz away.

(c) The bass has a harmonic essentially sitting on the formant, so the formant's peak appears faithfully in the output and the vowel is clear. The soprano's nearest harmonic is $180$ Hz above the formant, well outside its $100$ Hz bandwidth, so the formant contributes almost nothing and the vowel is poorly defined.

Therefore this is the formant-sampling problem of §13.4 in numbers, and it is why sopranos resort to formant tuning.
:::

:::{exercise}
:label: ex-the-singing-voice-4

*(Moderate)* A soprano at $880$ Hz raises $F_1$ from $700$ Hz to $880$ Hz by opening her jaw. (a) What does this do to the output level of the fundamental? Assume the formant peak is $15$ dB above the surrounding response. (b) What does it do to the vowel?
:::

:::{solution} ex-the-singing-voice-4
:label: sol-the-singing-voice-4
:class: dropdown

(a) The fundamental moves from the skirt of the resonance onto its peak, gaining most of the $15$ dB. In intensity terms:

$$
10^{15/10} = 32,
$$

a thirty-twofold increase in the fundamental's radiated intensity: an enormous gain for a change in jaw position.

(b) $F_1$ has been moved from $700$ Hz to $880$ Hz. Consulting the vowel chart, raising $F_1$ moves the vowel toward a more open one, "ah" territory and beyond, whatever the text calls for.

Therefore the singer trades intelligibility for power, and above a certain pitch she has no real choice: the alternative is to be inaudible. Sung text at the top of the soprano range is conventionally supported by surtitles for that reason.
:::

:::{exercise}
:label: ex-the-singing-voice-5

*(Moderate)* The singer's formant provides $20$ dB of extra output near $3$ kHz. (a) By what factor in intensity? (b) An orchestra produces $95$ dB in the hall and an untrained voice $72$ dB in the $3$ kHz band. What does the trained voice produce there? (c) Comment.
:::

:::{solution} ex-the-singing-voice-5
:label: sol-the-singing-voice-5
:class: dropdown

(a) $10^{20/10} = 100$.

(b) $72 + 20 = 92$ dB in that band.

(c) The orchestra's $95$ dB is its *total* level across the spectrum; in the narrow $3$ kHz band it produces far less, perhaps $70$ dB. The trained voice's $92$ dB in that band therefore **exceeds** the orchestra's contribution there by some $22$ dB, even though the voice's total output is $20$ dB below the orchestra's.

Therefore the voice loses the broadband contest decisively and wins the $3$ kHz contest decisively, and the second is the one that determines whether it is heard.
:::

:::{exercise}
:label: ex-the-singing-voice-6

*(Moderate)* Vocal folds are modeled as a mass on a spring. A singer raises the pitch from $220$ Hz to $440$ Hz. (a) If the effective mass is unchanged, by what factor does the tension rise? (b) In practice the folds also thin as they stretch. How does that affect the answer?
:::

:::{solution} ex-the-singing-voice-6
:label: sol-the-singing-voice-6
:class: dropdown

(a) $f \propto \sqrt{k}$, so doubling the frequency needs

$$
\frac{k'}{k} = 2^2 = 4.
$$

(b) Stretching the folds makes them thinner, which **reduces** the effective vibrating mass. Since $f \propto \sqrt{k/m}$, a falling $m$ contributes to the rise in $f$, so less than a fourfold increase in stiffness is needed.

Therefore the naive answer of four times overestimates the tension required. This is one reason the vocal folds can cover two and a half octaves while a guitar string covers far less by tension alone: the folds change both levers at once.
:::

:::{exercise}
:label: ex-the-singing-voice-7

*(Moderate)* A singer's vibrato is $5.5$ Hz at a depth of $\pm 70$ cents on a $440$ Hz note. (a) What frequency range does the note sweep? (b) $F_1$ is at $700$ Hz. Which harmonic sweeps across it, and by how much?
:::

:::{solution} ex-the-singing-voice-7
:label: sol-the-singing-voice-7
:class: dropdown

(a) $\pm 70$ cents is a ratio of $2^{\pm70/1200} = 1.0412$ and $0.9604$:

$$
440 \times 0.9604 = 422.6\ \text{Hz} \quad\text{to}\quad 440 \times 1.0412 = 458.1\ \text{Hz}.
$$

(b) The nearest harmonic to $700$ Hz is the 2nd, at $880$ Hz, too high. Actually $700/440 = 1.59$, so no harmonic is near $F_1$ at all; the fundamental at $440$ Hz is the closest below.

The fundamental sweeps from $422.6$ to $458.1$ Hz, a range of $35.5$ Hz. Since $F_1$'s bandwidth is around $100$ Hz, this sweep moves the fundamental appreciably across the lower skirt of the resonance.

Therefore vibrato causes the output amplitude of each harmonic to fluctuate as it moves across the filter's slopes. Vibrato therefore produces amplitude modulation as well as frequency modulation, and makes a voice easier to pick out of a texture.
:::

:::{exercise}
:label: ex-the-singing-voice-8

*(Moderate)* Explain, using [Chapter 7](#ch-loudness)'s masking asymmetry, why an orchestra masks a voice's low harmonics more effectively than its high ones.
:::

:::{solution} ex-the-singing-voice-8
:label: sol-the-singing-voice-8
:class: dropdown

[Chapter 7](#ch-loudness) established that masking spreads **upward** in frequency far more than downward, because a low-frequency traveling wave must traverse the whole basilar membrane to reach its own place and excites the high-frequency region on the way ([Chapter 6](#ch-the-ear)).

The orchestra's energy is concentrated below about $500$ Hz. That energy therefore masks:

- the voice's fundamental and low harmonics, which lie in the same region, strongly, since masker and masked coincide;
- the voice's mid harmonics, at $1$–$2$ kHz, appreciably, by upward spread;
- the voice's $3$ kHz region, much less, because the upward spread has weakened considerably by two and a half octaves above the masker.

Therefore the region where the voice is least masked is the region where the singer's formant puts its energy, and it is also where the ear is most sensitive. The three effects reinforce each other, and the solution works as well as it does.
:::

:::{exercise}
:label: ex-the-singing-voice-9

*(Challenging)* A trained singer produces about $1$ mW of acoustic power. (a) What sound level does this give at $10$ m outdoors? (b) An orchestra produces about $1$ W. What level at the same distance? (c) Reconcile with the fact that soloists are heard.
:::

:::{solution} ex-the-singing-voice-9
:label: sol-the-singing-voice-9
:class: dropdown

(a) $I = P/4\pi r^2 = (10^{-3}\ \text{W})/(4\pi \times 100\ \text{m}^2) = 7.96\times10^{-7}$ W/m²:

$$
L = 10\log_{10}\!\left(\frac{7.96\times10^{-7}}{10^{-12}}\right) = 59\ \text{dB}.
$$

(b) A thousand times the power is $30$ dB more: $89$ dB.

(c) The voice is $30$ dB below the orchestra **overall**, which by [Chapter 7](#ch-loudness)'s addition rule should make it entirely inaudible: a sound $30$ dB down adds nothing.

It is heard because the comparison is not made broadband. In the narrow $3$ kHz band where the singer's formant concentrates the voice's output and where the orchestra has little, the voice is *above* the orchestra. The ear analyzes by critical band ([Chapter 7](#ch-loudness)), so what matters is the signal-to-masker ratio within a band, not the total.

Therefore the solution is to lose the overall contest and win a local one, and the ear's band-by-band analysis is what makes that a winning strategy.
:::

:::{exercise}
:label: ex-the-singing-voice-10

*(Moderate)* A tenor lowers his larynx, shortening the effective tract above the larynx from $17.5$ cm to $16.0$ cm while creating a separate cavity below. (a) What happens to the main formants? (b) The new cavity resonates near $2.9$ kHz. Estimate its dimensions, treating it as a stopped pipe.
:::

:::{solution} ex-the-singing-voice-10
:label: sol-the-singing-voice-10
:class: dropdown

(a) Shortening the tract raises the formants in proportion to $1/L$:

$$
\frac{17.5}{16.0} = 1.094,
$$

so $F_1$ moves from $500$ to $547$ Hz and $F_2$ from $1500$ to $1641$ Hz, and so on, about $155$ cents upward.

(b) Treating the pharyngeal cavity as a stopped pipe resonating at $2.9$ kHz:

$$
L = \frac{v}{4f} = \frac{350\ \text{m/s}}{4(2900\ \text{Hz})} = 0.030\ \text{m} = 3.0\ \text{cm}.
$$

Therefore the extra cavity is about $3$ cm long, which is roughly the dimension of the widened pharynx just above a lowered larynx, and the reason the technique works.
:::

:::{exercise}
:label: ex-the-singing-voice-11

*(Challenging)* Show that a uniform tube closed at one end has resonances at odd multiples of $v/4L$, and explain why the vocal tract's formants are not *exactly* at these values.
:::

:::{solution} ex-the-singing-voice-11
:label: sol-the-singing-voice-11
:class: dropdown

The closed end requires a displacement node and the open end a displacement antinode. Node and antinode are separated by a quarter wavelength, so the shortest fit is $L = \lambda/4$, and further fits add half-wavelengths:

$$
L = (2m - 1)\frac{\lambda}{4}, \qquad m = 1, 2, 3, \ldots
$$

so $\lambda_m = 4L/(2m-1)$ and

$$
f_m = \frac{v}{\lambda_m} = (2m-1)\frac{v}{4L}.
$$

Three reasons the real tract departs from this:

1. **It is not uniform.** The tract's cross-section varies enormously along its length, and that variation is precisely what distinguishes one vowel from another. A uniform tube describes only the neutral vowel.
2. **The end correction applies** ([Chapter 11](#ch-wind-instruments)). The lips are an open end of substantial radius, so the effective length exceeds the anatomical one.
3. **The nasal cavity can be coupled in** by lowering the soft palate, which adds a side branch with its own resonances and, more importantly, its own *anti*-resonances.

Therefore the stopped-pipe model gives the right ballpark and the right ordering, and everything interesting about vowels is a departure from it.
:::

:::{exercise}
:label: ex-the-singing-voice-12

*(Straightforward)* A singer moves from chest voice to falsetto. (a) Describe the change in fold vibration. (b) Predict the effect on the spectrum. (c) Explain why the transition is audible if untrained.
:::

:::{solution} ex-the-singing-voice-12
:label: sol-the-singing-voice-12
:class: dropdown

(a) In chest voice the folds vibrate through their full depth and close completely on each cycle. In falsetto only the thin upper edges vibrate, and closure is often incomplete.

(b) Complete, abrupt closure produces a sharp discontinuity in the airflow, which by [Chapter 5](#ch-fourier-and-timbre) means strong high harmonics. Incomplete, gentler closure produces a smoother waveform and a spectrum that rolls off much faster, plus added breath noise where air leaks through continuously.

So falsetto is spectrally poorer and breathier, and this is audible as a change of timbre quite apart from any change in pitch.

(c) At the transition, the mode of vibration changes discontinuously, so the spectrum changes discontinuously. The listener hears a sudden shift in tone quality, often with a momentary instability or crack as the folds reorganize.

Therefore training consists of learning to blend the two modes, mixing partial fold depth with adjusted tension, so that the spectral change is spread over several semitones instead of happening at one note.
:::

:::{exercise}
:label: ex-the-singing-voice-13

*(Moderate)* Explain why the voice is acoustically more like a violin than like a clarinet, despite being a wind-driven instrument.
:::

:::{solution} ex-the-singing-voice-13
:label: sol-the-singing-voice-13
:class: dropdown

The distinction is which stage sets the pitch.

In a **clarinet** ([Chapter 11](#ch-wind-instruments)), the bore's impedance peaks control the reed. The reed's own natural frequency is a couple of kilohertz and irrelevant; it oscillates at whatever the resonator dictates. Change the fingering and the pitch changes without touching the reed.

In a **violin** ([Chapter 10](#ch-string-instruments)), the string sets the pitch and the body merely responds. The body could be replaced with a different one and the same notes would sound, differently colored.

In the **voice**, the folds set the pitch, determined by their own mass and tension, and the tract merely shapes the result. Change the tract and the vowel changes; the pitch does not. The reason is impedance: the folds are massive and stiff enough that the tract's pressure oscillations cannot push them around.

Therefore the voice belongs with the violin: source sets pitch, resonator shapes timbre. Its wind-driven appearance is misleading, and the source–filter model is exactly the statement that the two stages are separable, which is what fails in a clarinet.
:::

:::{exercise}
:label: ex-the-singing-voice-14

*(Moderate)* A speech synthesizer produces vowels with correct formants and a perfectly steady pitch, and listeners describe it as robotic. Name three additions that would improve it, drawing on this chapter and [Chapter 5](#ch-fourier-and-timbre).
:::

:::{solution} ex-the-singing-voice-14
:label: sol-the-singing-voice-14
:class: dropdown

1. **Pitch variation.** Real speech has continuous intonation contours and small random fluctuations (jitter) of a fraction of a percent. A perfectly steady fundamental is the single strongest cue that a voice is synthetic, because no biological oscillator is that stable.

2. **Breath noise.** Real phonation leaks air continuously, adding a noise component with a continuous spectrum that no harmonic synthesis contains ([Chapter 5](#ch-fourier-and-timbre)). Its absence is what makes synthetic speech sound clean in an unnatural way.

3. **Moving formants.** Formants do not jump between target values; they glide, and the glides between vowels, the *transitions*, carry much of the information that identifies neighboring consonants. A synthesizer that hits formant targets and holds them produces separately correct vowels and unnatural speech.

A fourth worth adding is **amplitude variation**: real speech varies in level constantly with stress and syllable structure.

Therefore what is missing is again everything the steady-state model leaves out, which is the same conclusion [Chapter 5](#ch-fourier-and-timbre) reached about synthesized instruments, and for the same reason.
:::
