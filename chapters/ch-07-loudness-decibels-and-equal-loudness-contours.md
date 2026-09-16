---
title: "Loudness, Decibels, and Equal-Loudness Contours"
short_title: "Chapter 7. Loudness, Decibels, and Equal-Loudness Contours"
label: ch-loudness
numbering:
  enumerator: "7.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 7.1, 7.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-07-loudness-decibels-and-equal-loudness-contours.pdf
    chapter: 7
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish sound pressure, sound intensity, and loudness, and state which are physical and which is perceptual.
- Explain why the enormous range of audible intensities makes a logarithmic scale the natural one.
- Calculate sound intensity level and sound pressure level in decibels from intensity or pressure, and convert back.
- Explain why a factor of ten in intensity is 10 dB and a factor of two is 3 dB, and use those two facts to do decibel arithmetic without a calculator.
- Combine the levels of two or more incoherent sources, and explain why doubling the number of violins does not double the loudness.
- Distinguish the decibel as a ratio from the decibel as an absolute level referred to a stated reference, and use dB SPL correctly.
- Read the equal-loudness contours, define the phon, and explain why bass disappears first when music is played quietly.
- Define the sone, use the rule that ten phons doubles the loudness, and explain why a 60-piece orchestra is not sixty times as loud as one instrument.
- Explain masking and the critical band, and give a musical consequence of each.

### Introduction

Turn the volume knob halfway down. Is the music half as loud?

Nobody thinks so, and the reason is the subject of this chapter. Between the sound pressure at your eardrum and the loudness you experience lie two transformations, and neither is a simple proportion.

The first is **enormous range**. The quietest audible sound and the loudest tolerable one differ in pressure by a factor of about a million, and in energy by a factor of about a million million. No linear scale copes with that, and the decibel exists to tame it.

The second is **frequency dependence**. The ear is far more sensitive at some frequencies than at others, and, the awkward part, *how much* more depends on how loud the sound is. A bass note and a mid-range note that match in loudness when played loudly will not match when played quietly. Music therefore sounds thin at low volume, and it is a fact about you rather than about your loudspeakers.

This chapter separates three things that ordinary speech runs together:

| Quantity | What it is | Units |
|---|---|---|
| Sound pressure level | Physical, measurable with an instrument | dB SPL |
| Loudness level | How loud it sounds, expressed as the level of an equally loud $1$ kHz tone | phon |
| Loudness | How loud it sounds, on a scale where twice the number means twice as loud | sone |

Only the first is physics in the sense of Chapters 1 to 5. The other two are properties of a listener, and getting from the first to the third is what the chapter does.

## Pressure, Intensity, and the Range of Hearing

### Two Physical Measures

Two physical quantities describe the strength of a sound, and both are used.

**Sound pressure** $p$ is the amplitude of the pressure variation, in pascals. It is what a microphone and an eardrum actually respond to.

**Intensity** $I$ is the power per unit area carried by the wave, in watts per square meter. It is related to pressure by

$$
I = \frac{p^2}{\rho v},
$$

where $\rho v$ is the acoustic impedance of the medium, about $413$ kg m⁻² s⁻¹ for air at room temperature.

The essential relation is the one [Chapter 1](#ch-sound-and-shm) established: **intensity goes as the square of pressure.** Double the pressure and you quadruple the intensity. Every factor-of-two confusion in acoustics comes from losing track of this.

### Twelve Orders of Magnitude

The numbers are worth writing out.

| | Pressure (Pa) | Intensity (W/m²) |
|---|---|---|
| Threshold of hearing at $1$ kHz | $2\times10^{-5}$ | $1\times10^{-12}$ |
| Quiet conversation | $2\times10^{-3}$ | $1\times10^{-8}$ |
| Orchestra, fortissimo | $2\times10^{-1}$ | $1\times10^{-4}$ |
| Threshold of pain | $20$ | $1$ |

The pressure range is $10^6$ and the intensity range is $10^{12}$. For comparison, the total acoustic power radiated by a full symphony orchestra playing as loudly as it can is somewhere around one watt, less than a small light bulb. The ear is an extraordinarily sensitive instrument working with extraordinarily small quantities.

A linear scale is hopeless here. If one millimeter on a graph represented the threshold of hearing, the threshold of pain would be a thousand kilometers away.

### The Reference Values

The values in the first row of that table are not accidents; they are **definitions**, chosen because they are close to the average threshold of hearing at $1$ kHz:

$$
p_0 = 2\times10^{-5}\ \text{Pa} = 20\ \mu\text{Pa},
\qquad
I_0 = 1\times10^{-12}\ \text{W/m}^2 .
$$

Every decibel figure in this book is referred to one of these, and they are consistent with each other: a pressure of $p_0$ in air carries an intensity of very nearly $I_0$.

## The Decibel

### A Logarithmic Scale

The **decibel** compresses a huge range into a manageable one by taking a logarithm. For a ratio of intensities,

$$
L = 10\log_{10}\!\left(\frac{I}{I_0}\right) \ \text{dB}.
$$

Because intensity goes as pressure squared, and $\log(p^2) = 2\log(p)$, the same level in terms of pressure is

$$
L = 20\log_{10}\!\left(\frac{p}{p_0}\right)\ \text{dB}.
$$

**The factor is $10$ for power quantities and $20$ for amplitude quantities.** They give the same answer for the same physical sound; the difference is entirely in which quantity you started from. Using $10$ where you need $20$ halves every answer, and it is the most common error in the subject.

```{figure} ../images/ch07-decibel-scale.svg
:label: fig:ch07-decibel-scale
:alt: A vertical decibel scale from 0 to 130 dB with everyday and musical landmarks marked, and a second axis showing the corresponding intensities from ten to the minus twelve to one watt per square meter, with the region above 85 dB shaded as damaging.

The decibel scale, with landmarks. The right-hand axis shows the intensities the same sounds correspond to: each $30$ dB is a factor of a thousand. Note how compressed the *audible* world is on a decibel scale and how spread out it is in watts.
```

### dB SPL and Other References

A decibel on its own is a **ratio** and says nothing absolute. "The passage is $6$ dB louder" is meaningful. "The passage is $6$ dB" is not, until a reference is stated.

**dB SPL** means referred to $p_0 = 20\ \mu$Pa, and is the one used throughout this book for absolute levels. Others exist, dBu and dBV in audio electronics, dBFS in digital audio ([Chapter 15](#ch-electronic-and-recorded-sound)), and mixing them up produces errors of tens of decibels.

You will also meet **dB A**, which is a measurement weighted by a filter approximating the ear's sensitivity at moderate levels. Exposure limits are quoted in dB A precisely because a sound's damage potential depends on where its energy lies, not just how much there is.

### Decibel Arithmetic Without a Calculator

Two facts make most decibel problems mental arithmetic.

$$
\text{a factor of } 10 \text{ in intensity} = 10\ \text{dB},
\qquad
\text{a factor of } 2 \text{ in intensity} = 3\ \text{dB}.
$$

The second is approximate, $10\log_{10}2 = 3.01$, and the approximation is excellent.

From those two, by adding:

| Intensity ratio | dB | | Amplitude ratio | dB |
|---|---|---|---|---|
| $2$ | $3$ | | $2$ | $6$ |
| $4$ | $6$ | | $4$ | $12$ |
| $10$ | $10$ | | $10$ | $20$ |
| $100$ | $20$ | | $100$ | $40$ |
| $1000$ | $30$ | | $1000$ | $60$ |

:::{tip} Self-check
A sound is $23$ dB above another in intensity. Without a calculator, what is the intensity ratio? (Break $23$ into tens and threes.)
:::

## Combining and Comparing Levels

### Adding Incoherent Sources

Two violinists play the same note. How much louder than one?

The answer depends on whether their sounds are **coherent**, locked in a fixed phase relationship, or not.

Two loudspeakers fed from the same signal are coherent, and their pressures add: $2p$, which is $6$ dB. Two violinists are *not* coherent: their frequencies and phases drift independently, so the interference at any point averages away over time and their **intensities** add instead: $2I$, which is $3$ dB.

Real musicians are incoherent, so for $n$ identical independent sources,

$$
L_n = L_1 + 10\log_{10}(n).
$$

```{figure} ../images/ch07-adding-and-sones.svg
:label: fig:ch07-adding-and-sones
:alt: Left, a logarithmic plot of level above one source against number of sources, marked at 1, 2, 10 and 60. Right, a logarithmic plot of loudness in sones against loudness level in phons, marked at 40, 50, 60 and 80 phons.

Left: adding incoherent sources. Sixty violins are only $18$ dB louder than one. Right: loudness in sones against loudness level in phons, each $10$ phons doubles the loudness.
```

The consequence for orchestration is sharp and slightly deflating. Sixty violins produce $10\log_{10}(60) = 18$ dB more than one. And since §7.5 will show that $10$ phons is a doubling of loudness, $18$ dB is under two doublings: **sixty violins sound less than four times as loud as one.** Orchestras have so many strings and so few trumpets for that reason: the section needs numbers merely to keep up.

### Distance, Level, and the Six-Decibel Rule

Combining the inverse-square law of [Chapter 2](#ch-wave-motion) with the definition of the decibel:

$$
L_2 - L_1 = 20\log_{10}\!\left(\frac{r_1}{r_2}\right).
$$

Doubling the distance therefore costs $20\log_{10}(2) = 6$ dB. Ten times the distance costs $20$ dB.

This holds outdoors. Indoors it fails beyond the critical distance, for the reason [Chapter 2](#ch-wave-motion) gave and [Chapter 14](#ch-room-acoustics) develops: most of what reaches a distant listener has bounced.

::::{tip} Worked example: a hall's back row
*A soloist produces $85$ dB at $1$ m. What level reaches a listener $32$ m away, (a) outdoors and (b) in a hall where the reverberant field holds the level constant beyond a critical distance of $6$ m?*

(a) Outdoors, $32$ m is five doublings from $1$ m:

$$
L = 85 - 5(6) = 55\ \text{dB}.
$$

(b) Indoors, the level falls by the inverse-square law only out to $6$ m. From $1$ m to $6$ m:

$$
20\log_{10}(6) = 15.6\ \text{dB},
$$

so the level at the critical distance is about $69$ dB, and it stays near that out to $32$ m.

The difference between the two answers is $14$ dB, a factor of $25$ in intensity, and it is the single biggest reason unamplified concerts are possible at all.
::::

### Levels of Real Musical Sounds

A rough table, for calibration. All at the listener's position in a concert hall:

| Marking | Level (dB SPL) |
|---|---|
| *pp* | $50$–$60$ |
| *mf* | $70$–$80$ |
| *ff* | $90$–$100$ |

An orchestra's usable dynamic range is therefore about $40$–$50$ dB, which is far less than the $120$ dB the ear can handle. The limit at the bottom is the noise of the hall and the audience; at the top it is what the instruments can produce.

Note also that dynamic markings are **not** absolute levels. A *pianissimo* in a Mahler symphony and a *pianissimo* in a string quartet differ by a good deal, and performers read the marking as an instruction about relative level and character rather than about decibels.

## Loudness Level: The Phon

### Equal-Loudness Contours

Now the frequency dependence. The experiment is straightforward to describe: play a $1$ kHz reference tone at a known level, then play a tone at some other frequency and ask the listener to adjust it until the two sound equally loud. Repeat across the spectrum, and across reference levels, and average over many listeners.

The result is the set of **equal-loudness contours**, standardized as ISO 226.

```{figure} ../images/ch07-equal-loudness.svg
:label: fig:ch07-equal-loudness
:alt: Equal-loudness contours on logarithmic frequency axes, showing curves at 10, 20, 40, 60, 80 and 90 phons that rise steeply below 200 Hz, dip to a minimum around 3 to 4 kHz, and flatten at higher levels, with a dashed threshold-of-hearing curve beneath.

The equal-loudness contours. Every point on one curve sounds equally loud. The curves are labeled in **phons**: by definition, a tone has a loudness level of $N$ phons if it sounds as loud as a $1$ kHz tone at $N$ dB SPL. At $1$ kHz, therefore, phons and dB SPL agree exactly; everywhere else they do not.
```

Three features of those curves carry most of the content.

**The ear is most sensitive around $3$–$4$ kHz.** This is the ear-canal resonance of [Chapter 6](#ch-the-ear), and it is why that region is where speech intelligibility lives and where a singer must compete ([Chapter 13](#ch-the-singing-voice)).

**Sensitivity falls sharply at low frequencies.** At $50$ Hz the threshold is about $45$ dB SPL: a sound $45$ dB above the $1$ kHz threshold is only just audible.

**The curves flatten as level rises.** This is the important one, and it is the subject of the next subsection.

### Reading the Contours

The **phon** is defined by those curves: a sound has a loudness level of $N$ phons if it is judged as loud as a $1$ kHz tone at $N$ dB SPL.

```{audio} ch07-equal-amplitude-tones
:label: fig:ch07-equal-amplitude-tones
:transcript: Four tones in succession at identical physical level. The first, at 60 Hz, is faint; the second louder; the third and fourth clearly the loudest. They are the same level throughout.

Four tones, all at the same sound pressure level, rising in frequency. They are emphatically not equally loud, the $60$ Hz tone sounds around $34$ phon while the $4$ kHz tone sounds around $72$ phon, a difference of nearly four doublings in loudness for identical physical sound. (Judge this at a moderate volume; the effect depends on level, which is exactly the point.)
```

### Why Quiet Music Loses Its Bass

Because the contours are not parallel, **the ear's frequency response depends on level**.

```{figure} ../images/ch07-bass-loss.svg
:label: fig:ch07-bass-loss
:alt: Two curves of sensitivity relative to 1 kHz against frequency, one for loud listening at 80 phon and one for quiet listening at 30 phon, with the shaded gap between them below 500 Hz marking the bass lost when the volume is reduced.

The same music, played loudly and quietly, relative to $1$ kHz. Turning the volume down does not scale everything equally: the low frequencies fall away faster than the middle, because the contours crowd together at low levels.
```

The consequence is familiar to everyone. **Music played quietly sounds thin.** Turning the volume down does not merely make everything smaller; it changes the balance, taking the bass first.

:::{note}
This is what the "loudness" button on old hi-fi amplifiers did. It applied a bass boost at low volume settings, attempting to compensate for the crowding of the contours. The idea is sound in principle and hard in practice, because the correct compensation depends on the *absolute* level at the listener's ears, which the amplifier has no way of knowing.
:::

## Loudness Itself: The Sone

### Doubling Loudness

The phon says when two sounds are equally loud. It does not say when one is *twice* as loud, and it cannot: phons are defined by a matching procedure, and matching says nothing about ratios.

To get ratios, ask listeners directly: adjust this sound until it is twice as loud as that one. The answer, robustly reproduced, is

$$
\text{an increase of } 10 \text{ phons doubles the loudness.}
$$

The **sone** encodes this. One sone is defined as $40$ phons, and

$$
S = 2^{(P - 40)/10},
$$

with $S$ in sones and $P$ in phons. So $40$ phons is $1$ sone, $50$ phons is $2$ sones, $60$ phons is $4$ sones.

Ten phons is a factor of ten in intensity. So **a tenfold increase in intensity is only a doubling in loudness**, which is the compression that makes the ear's enormous range usable.

::::{tip} Worked example: how much louder is the orchestra?
*A passage marked* pp *is $55$ dB SPL and one marked* ff *is $95$ dB SPL, both broadband so that phons and dB SPL are roughly equal. How much louder does the* ff *sound?*

The difference is $40$ phons, which is four doublings:

$$
\frac{S_{ff}}{S_{pp}} = 2^{40/10} = 2^4 = 16.
$$

Therefore, the *fortissimo* sounds about sixteen times as loud, from a sound that is $10^4$, ten thousand times, more intense.

That compression is worth pausing on. It is what lets one pair of ears handle a whisper and an orchestra, and it is also why adding musicians is such an inefficient way to get louder.
::::

### Masking

A sound that would be perfectly audible on its own can be rendered completely inaudible by another sound. This is **masking**, and [Chapter 6](#ch-the-ear) supplied the mechanism: a masker's traveling wave excites a region of the basilar membrane, and anything whose own region falls inside that excitation is lost in it.

```{figure} ../images/ch07-masking.svg
:label: fig:ch07-masking
:alt: Three masking patterns produced by a 400 Hz tone at 40, 60 and 80 dB, each rising steeply on the low-frequency side and falling gradually on the high-frequency side, with the higher-level maskers spreading further upward.

Masking patterns produced by a $400$ Hz tone. Each curve shows the level another tone needs in order to be heard. Two features matter: masking is **asymmetric**, spreading far further upward in frequency than downward, and the asymmetry gets worse as the masker gets louder.
```

```{audio} ch07-masking-demo
:label: fig:ch07-masking-demo
:transcript: A quiet high tone, clearly audible on its own. Then a loud low tone. Then both together, in which the high tone has become difficult or impossible to hear.

Masking in three segments. The high tone in the third segment is present at exactly the level it had in the first. Nothing has been removed from the signal; it has been removed from your perception of it.
```

The upward spread of masking has direct musical consequences. A loud bass line buries a quiet high part far more than the reverse, so arrangers give the melody to a high instrument and a mix engineer who wants to hear the hi-hat turns the bass *down* rather than the hi-hat up.

It is also, remarkably, what makes MP3 possible. If a component of a signal is masked, a listener cannot hear it, so a codec can simply discard it and spend the saved bits elsewhere. [Chapter 15](#ch-electronic-and-recorded-sound) develops this.

### The Critical Band

Masking is strongest when masker and masked are close in frequency, and the width of the region over which they interact strongly is the **critical band**.

It is roughly $100$ Hz wide below $500$ Hz, and roughly a third of an octave above that, which means it is approximately **constant in musical terms**, a little wider than a major third, across most of the range. That is not a coincidence: the critical band corresponds to a roughly constant distance along the basilar membrane, and [Chapter 6](#ch-the-ear) showed that the membrane's map is logarithmic.

The critical band is the ear's frequency-resolution limit, and it does a great deal of work in what follows:

- Two tones within a critical band interfere audibly and sound **rough**; two tones further apart do not. This is the physical basis of dissonance ([Chapter 8](#ch-pitch-and-consonance)).
- Noise masks a tone only if the noise lies within about a critical band of it.
- Loudness adds differently within and across critical bands. Spread the same energy across several bands and it sounds louder than if it is concentrated in one; so a chord is louder than a single note of the same total intensity, and a full orchestration carries further than a doubled unison.

## Summary

- **Intensity goes as pressure squared.** The decibel therefore has two forms: $10\log_{10}$ for intensity and power, $20\log_{10}$ for pressure and amplitude. They describe the same sound.
- **Hearing spans $10^{12}$ in intensity**, from $10^{-12}$ W/m² to about $1$ W/m², referred to $p_0 = 20\ \mu$Pa. A decibel figure without a stated reference is a ratio, not a level.
- **Two facts do most decibel arithmetic**: a factor of ten is $10$ dB, a factor of two is $3$ dB (in intensity).
- **Incoherent sources add in intensity**, so $n$ of them give $10\log_{10}(n)$ dB. Sixty violins are $18$ dB above one, less than four times as loud.
- **Distance costs $6$ dB per doubling** outdoors, and much less than that indoors beyond the critical distance.
- **Equal-loudness contours** describe the ear's frequency dependence. The **phon** is defined by matching against a $1$ kHz tone, so phons and dB SPL agree at $1$ kHz and nowhere else. Sensitivity peaks near $3$–$4$ kHz and collapses at low frequencies.
- **The contours flatten as level rises**, so the ear's frequency balance depends on volume. Quiet music loses its bass first.
- **The sone measures loudness itself**: $1$ sone is $40$ phons, and each $10$ phons doubles it. A tenfold increase in intensity is a twofold increase in loudness.
- **Masking** renders an audible sound inaudible, spreading much further upward in frequency than downward. It is the basis of perceptual audio coding.
- **The critical band** is the ear's resolution limit, roughly a third of an octave, hence roughly constant in musical terms. It underlies roughness, dissonance, and the way loudness sums across a spectrum.

## Conceptual Questions

1. Explain why the decibel scale uses $10\log$ for intensity and $20\log$ for pressure, and why both give the same level for the same sound.

2. A student writes "the sound was $70$ dB". Explain what is missing from this statement and why it matters.

3. Explain why two loudspeakers fed from the same signal give $+6$ dB while two violinists playing the same note give $+3$ dB.

4. An orchestra has sixty violins and three trumpets. Use the addition rule to comment on whether this is a sensible balance.

5. Explain why music played quietly sounds thin, using the shape and spacing of the equal-loudness contours.

6. A $50$ Hz tone and a $3$ kHz tone are played at the same dB SPL. Which sounds louder, and roughly by how many phons at moderate levels?

7. Explain why a loud bass line masks a quiet cymbal much more than a quiet cymbal masks a loud bass line.

8. Explain how masking allows an audio codec to discard part of a signal without an audible change, and state what would go wrong if the codec's model of masking were inaccurate.

## Problems

:::{exercise}
:label: ex-loudness-1

A sound has intensity $3.5\times10^{-6}$ W/m². (a) What is its sound intensity level in dB? (b) What pressure amplitude does it correspond to, taking $\rho v = 413$ kg m⁻² s⁻¹?
:::

:::{solution} ex-loudness-1
:label: sol-loudness-1
:class: dropdown

(a) Using $L = 10\log_{10}(I/I_0)$ with $I_0 = 10^{-12}$ W/m²:

$$
L = 10\log_{10}\!\left(\frac{3.5\times10^{-6}}{1\times10^{-12}}\right) = 10\log_{10}(3.5\times10^{6}) = 65.4\ \text{dB}.
$$

(b) From $I = p^2/\rho v$:

$$
p = \sqrt{I\rho v} = \sqrt{(3.5\times10^{-6})(413)} = \sqrt{1.446\times10^{-3}} = 0.038\ \text{Pa}.
$$

Therefore, the level is $65$ dB and the pressure amplitude about $38$ mPa, roughly conversational.
:::

:::{exercise}
:label: ex-loudness-2

Without a calculator, find the level difference corresponding to an intensity ratio of (a) $100$, (b) $8$, (c) $40$, (d) $1/2$.
:::

:::{solution} ex-loudness-2
:label: sol-loudness-2
:class: dropdown

Using $\times10 \to 10$ dB and $\times2 \to 3$ dB.

(a) $100 = 10\times10 \to 10 + 10 = 20$ dB.

(b) $8 = 2\times2\times2 \to 3 + 3 + 3 = 9$ dB.

(c) $40 = 10\times2\times2 \to 10 + 3 + 3 = 16$ dB.

(d) $1/2 \to -3$ dB.

Therefore: $20$, $9$, $16$, and $-3$ dB. (Exact values: $20.0$, $9.03$, $16.02$, $-3.01$.)
:::

:::{exercise}
:label: ex-loudness-3

One clarinet produces $72$ dB at a listener. (a) What level do four identical clarinets produce? (b) How many clarinets would be needed for $82$ dB? (c) Comment on the practicality.
:::

:::{solution} ex-loudness-3
:label: sol-loudness-3
:class: dropdown

(a) Four incoherent sources add $10\log_{10}(4) = 6.0$ dB:

$$
L = 72 + 6 = 78\ \text{dB}.
$$

(b) A rise of $10$ dB needs

$$
10\log_{10}(n) = 10 \;\Rightarrow\; n = 10.
$$

(c) Ten clarinets for $10$ dB, which is one doubling of loudness. Getting a second doubling would take a hundred. An ensemble cannot get much louder by recruiting, so composers reach for instruments with intrinsically higher output, brass, rather than for more of the same.
:::

:::{exercise}
:label: ex-loudness-4

A singer produces $88$ dB at $1$ m. Outdoors, find the level at (a) $2$ m, (b) $8$ m, (c) $50$ m.
:::

:::{solution} ex-loudness-4
:label: sol-loudness-4
:class: dropdown

Using $L_2 = L_1 - 20\log_{10}(r_2/r_1)$.

(a) $88 - 20\log_{10}(2) = 88 - 6.0 = 82$ dB.

(b) $88 - 20\log_{10}(8) = 88 - 18.1 = 70$ dB.

(c) $88 - 20\log_{10}(50) = 88 - 34.0 = 54$ dB.

Therefore, $82$, $70$, and $54$ dB. At $50$ m outdoors the singer is at about the level of a quiet conversation, outdoor performance essentially requires amplification; indoor performance does not.
:::

:::{exercise}
:label: ex-loudness-5

A tone at $100$ Hz must be played at $50$ dB SPL to sound as loud as a $1$ kHz tone at $30$ dB SPL. (a) What is the loudness level of each, in phons? (b) How much more intense is the $100$ Hz tone?
:::

:::{solution} ex-loudness-5
:label: sol-loudness-5
:class: dropdown

(a) The loudness level is defined by the $1$ kHz match, so **both are $30$ phons**.

(b) The level difference is $50 - 30 = 20$ dB, so the intensity ratio is

$$
10^{20/10} = 100.
$$

Therefore, the $100$ Hz tone must be a hundred times more intense to sound equally loud. This is exactly the message of the equal-loudness contours: physical equality and perceptual equality are different things.
:::

:::{exercise}
:label: ex-loudness-6

A sound has a loudness level of $70$ phons. (a) What is its loudness in sones? (b) What loudness level would sound twice as loud? (c) Four times?
:::

:::{solution} ex-loudness-6
:label: sol-loudness-6
:class: dropdown

(a) Using $S = 2^{(P-40)/10}$:

$$
S = 2^{(70-40)/10} = 2^3 = 8\ \text{sones}.
$$

(b) Twice as loud is $16$ sones, which is $2^4$, so $P = 40 + 40 = 80$ phons.

(c) Four times is $32$ sones, $2^5$, so $P = 90$ phons.

Therefore, $8$ sones; doubling needs $+10$ phons and quadrupling $+20$. Note that quadrupling the loudness requires a hundredfold increase in intensity.
:::

:::{exercise}
:label: ex-loudness-7

A rock concert measures $112$ dB. (a) How many times more intense is this than the $85$ dB eight-hour limit? (b) Using the $3$ dB exchange rate, what is the safe exposure time?
:::

:::{solution} ex-loudness-7
:label: sol-loudness-7
:class: dropdown

(a) The difference is $112 - 85 = 27$ dB:

$$
10^{27/10} = 501.
$$

(b) $27$ dB is nine steps of $3$ dB, so nine halvings of eight hours:

$$
T = \frac{8\ \text{h}}{2^9} = \frac{8}{512}\ \text{h} = 0.0156\ \text{h} = 56\ \text{seconds}.
$$

Therefore, the sound is about $500$ times more intense than the limit, and the safe unprotected exposure is under a minute. A three-hour concert at that level is roughly two hundred times the permitted daily dose.
:::

:::{exercise}
:label: ex-loudness-8

Two sounds of $70$ dB and $76$ dB are played together. (a) What is the combined level? (b) What is it if the second is $60$ dB instead? (c) State the general rule your second answer illustrates.
:::

:::{solution} ex-loudness-8
:label: sol-loudness-8
:class: dropdown

Intensities add, so convert, add, and convert back.

(a) Relative to $I_0$: $10^{7.0} = 1.00\times10^{7}$ and $10^{7.6} = 3.98\times10^{7}$. The sum is $4.98\times10^{7}$, so

$$
L = 10\log_{10}(4.98\times10^{7}) = 77.0\ \text{dB}.
$$

(b) $10^{7.0} = 1.00\times10^{7}$ and $10^{6.0} = 0.10\times10^{7}$. The sum is $1.10\times10^{7}$:

$$
L = 10\log_{10}(1.10\times10^{7}) = 70.4\ \text{dB}.
$$

(c) **A sound $10$ dB below another adds almost nothing**, less than half a decibel. Anything more than about $10$ dB down can usually be ignored when adding levels, which is a useful shortcut and also the reason a single loud instrument can dominate an ensemble entirely.
:::

:::{exercise}
:label: ex-loudness-9

An orchestra plays a passage at $95$ dB SPL and a passage at $60$ dB SPL. Treating both as broadband so phons and dB SPL agree: (a) Find the loudness of each in sones. (b) Find the ratio. (c) Find the intensity ratio, and comment.
:::

:::{solution} ex-loudness-9
:label: sol-loudness-9
:class: dropdown

(a) $S_{95} = 2^{(95-40)/10} = 2^{5.5} = 45.3$ sones; $S_{60} = 2^{(60-40)/10} = 2^2 = 4$ sones.

(b) The loudness ratio is $45.3/4 = 11.3$.

(c) The intensity ratio is $10^{35/10} = 3.2\times10^{3}$.

Therefore, a sound over three thousand times more intense sounds about eleven times louder. The compression is enormous, roughly a cube root, and it is what allows a single dynamic range to accommodate both a solo flute and a full orchestra.
:::

:::{exercise}
:label: ex-loudness-10

The critical band is about a third of an octave above $500$ Hz. (a) How wide is the critical band at $1$ kHz, in hertz? (b) At $4$ kHz? (c) Express each in semitones.
:::

:::{solution} ex-loudness-10
:label: sol-loudness-10
:class: dropdown

A third of an octave is a frequency ratio of $2^{1/3} = 1.26$.

(a) A band centered on $1$ kHz running from $f/\sqrt[6]{2}$ to $f\sqrt[6]{2}$:

$$
1000/1.122 = 891\ \text{Hz} \quad\text{to}\quad 1000 \times 1.122 = 1122\ \text{Hz},
$$

a width of $231$ Hz.

(b) The same fractional width at $4$ kHz gives $3565$ to $4487$ Hz, a width of $922$ Hz.

(c) A third of an octave is four semitones in both cases, since the band is defined as a fixed ratio.

Therefore, the critical band is four times wider in hertz at $4$ kHz than at $1$ kHz, but identical in musical terms: a major third. That constancy in musical units is what makes the critical band useful for explaining consonance ([Chapter 8](#ch-pitch-and-consonance)).
:::

:::{exercise}
:label: ex-loudness-11

Show that if $n$ incoherent sources each of intensity $I$ combine, the level rise is $10\log_{10}(n)$, and explain why the corresponding result for $n$ coherent sources is $20\log_{10}(n)$.
:::

:::{solution} ex-loudness-11
:label: sol-loudness-11
:class: dropdown

**Incoherent.** The phases are uncorrelated, so the cross terms in the squared sum average to zero over time, and the intensities add: $I_{\text{tot}} = nI$. The level rise is

$$
10\log_{10}\!\left(\frac{nI}{I}\right) = 10\log_{10}(n).
$$

**Coherent.** The phases are locked, so the *pressures* add: $p_{\text{tot}} = np$. Since intensity goes as pressure squared, $I_{\text{tot}} = n^2 I$, and

$$
10\log_{10}(n^2) = 20\log_{10}(n).
$$

Therefore, coherent addition gives exactly twice the decibel rise of incoherent addition. For $n = 2$ that is $6$ dB against $3$ dB: the difference between two loudspeakers and two violinists.

The coherent result cannot hold everywhere in space: constructive interference at one point must be paid for by destructive interference elsewhere ([Chapter 3](#ch-superposition)). The $6$ dB applies on the axis where the two arrive in step.
:::

:::{exercise}
:label: ex-loudness-12

A $60$ Hz tone and a $3$ kHz tone are both played at $70$ dB SPL. Using the equal-loudness contours, estimate the loudness level of each in phons, and then the loudness of each in sones. What is the ratio?
:::

:::{solution} ex-loudness-12
:label: sol-loudness-12
:class: dropdown

Reading the contours of {numref}`Figure %s <fig:ch07-equal-loudness>` at $70$ dB SPL:

At $60$ Hz the $70$ dB point lies near the $35$ phon contour. At $3$ kHz it lies a little above the $70$ phon contour, call it $75$ phon, since the ear is *more* sensitive than at $1$ kHz there.

In sones:

$$
S_{60} = 2^{(35-40)/10} = 2^{-0.5} = 0.71,
\qquad
S_{3000} = 2^{(75-40)/10} = 2^{3.5} = 11.3.
$$

The ratio is $11.3/0.71 = 16$.

Therefore, two sounds of *identical physical level* differ by a factor of about sixteen in loudness, four doublings. Any claim about how loud something "is", made without reference to its frequency content, is close to meaningless.
:::

:::{exercise}
:label: ex-loudness-13

A mixing engineer boosts a vocal by $3$ dB. (a) By what factor has its intensity increased? (b) By what factor its pressure amplitude? (c) By roughly what factor its loudness? (d) Comment on which of these the engineer is thinking about.
:::

:::{solution} ex-loudness-13
:label: sol-loudness-13
:class: dropdown

(a) Intensity: $10^{3/10} = 2.0$.

(b) Pressure: $10^{3/20} = 1.41$.

(c) Loudness: $3$ dB is $0.3$ of a $10$-phon doubling, so

$$
2^{0.3} = 1.23,
$$

about a $23\%$ increase.

(d) None of them explicitly, but (c) is the one that matters. A $3$ dB boost doubles the energy and is barely a noticeable change in loudness, so mixing moves are typically made in steps of $1$ to $3$ dB and the smallest audible change in a mix context is often quoted as about $1$ dB.
:::

:::{exercise}
:label: ex-loudness-14

A hall has a background noise level of $30$ dB SPL. A solo flute produces $58$ dB at the back row. (a) What is the combined level? (b) What is the signal-to-noise ratio? (c) The audience arrives and the background rises to $42$ dB. Recompute both, and comment on what the audience has cost the flutist.
:::

:::{solution} ex-loudness-14
:label: sol-loudness-14
:class: dropdown

(a) Relative to $I_0$: flute $10^{5.8} = 6.31\times10^{5}$, noise $10^{3.0} = 1.00\times10^{3}$. Sum $6.32\times10^{5}$:

$$
L = 10\log_{10}(6.32\times10^{5}) = 58.0\ \text{dB}.
$$

(b) The signal-to-noise ratio is $58 - 30 = 28$ dB.

(c) With noise at $42$ dB: $10^{4.2} = 1.58\times10^{4}$. Sum with the flute: $6.31\times10^{5} + 0.158\times10^{5} = 6.47\times10^{5}$, so $L = 58.1$ dB, essentially unchanged.

The signal-to-noise ratio, however, falls to $58 - 42 = 16$ dB.

Therefore, the audience has not made the hall measurably louder but has removed $12$ dB of the flutist's headroom. The quietest passages the player could previously shape are now within a few decibels of the noise floor and cease to be audible as music. Halls are built with such low background-noise specifications for that reason, and a *pianissimo* is the first thing a noisy audience destroys.
:::
