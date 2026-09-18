---
title: "Musical Scales and Tuning Systems"
short_title: "Chapter 9. Musical Scales and Tuning Systems"
label: ch-scales-and-tuning
numbering:
  enumerator: "9.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 9.1, 9.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-09-musical-scales-and-tuning-systems.pdf
    chapter: 9
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Express a musical interval as a frequency ratio, and explain why intervals multiply where pitches add.
- Define the cent, convert between a frequency ratio and an interval in cents, and use cents to compare tunings that differ by only a few parts per thousand.
- Construct the Pythagorean scale from a chain of pure fifths, and calculate the Pythagorean comma that results from twelve of them.
- Explain why no stack of pure fifths ever closes into an octave, as a consequence of the fact that no power of 3/2 is a power of 2.
- Construct a just major scale from the ratios 3:2, 5:4, and 6:5, and identify the syntonic comma and the two sizes of whole tone it produces.
- Explain concretely why a keyboard tuned in just intonation cannot modulate, using the wolf fifth as the example.
- Describe quarter-comma meantone and the well temperaments as deliberate distributions of the comma, and state what each was optimizing for.
- Derive equal temperament from the requirement that twelve equal semitones make an octave, and calculate the ratio of the equal-tempered semitone.
- Compare equal-tempered intervals with their just counterparts in cents, and identify which are nearly exact and which are noticeably wide or narrow.
- Explain why fretted and keyboard instruments are bound to a fixed tuning while singers, string quartets, and trombonists are not.

### Introduction

```{figure} ../images/open/ch09-horn-violin.jpg
:label: fig:ch09-open-horn-violin
:alt: A historical horn-violin with a horn-shaped resonator.

Instrument makers have repeatedly reshaped resonators to change how partials reach the listener. Historical image, public domain.
```

[Chapter 8](#ch-pitch-and-consonance) ended with a result worth restating: intervals whose frequency ratios are simple whole numbers sound smooth, because the partials of the two tones coincide instead of clashing. The octave is $2{:}1$, the perfect fifth is $3{:}2$, the major third is $5{:}4$.

So building a musical scale ought to be easy. Take the good ratios and stack them up.

It cannot be done. Not approximately, not with more effort, not with better arithmetic, **the good ratios do not fit into an octave**, and no amount of cleverness will make them. This is an arithmetical fact, not a historical accident or a limitation of any instrument, and every tuning system ever devised is a different answer to the question of what to do about it.

The obstruction is easy to state. Stack twelve perfect fifths and you get *almost* seven octaves, missing by about a quarter of a semitone. Stack four perfect fifths and you get *almost* a major third plus two octaves, missing by about a fifth of a semitone. Those two small discrepancies, the **Pythagorean comma** and the **syntonic comma**, are the entire subject of this chapter. Every tuning system is a decision about where to put them.

That decision has consequences musicians can hear, and the history of Western music is bound up with it. The reason Bach could write in all twenty-four keys, and his grandfather's generation could not, is a change in where the comma was hidden.

## Intervals as Ratios

### The Octave and the Fifth

An interval is a **ratio** of frequencies, not a difference. The octave above $220$ Hz is $440$ Hz, and the octave above $440$ Hz is $880$ Hz. The differences are $220$ and $440$ Hz; the ratio is $2$ in both cases, and it is the ratio the ear reports.

This follows directly from [Chapter 6](#ch-the-ear): the cochlea's frequency map is logarithmic, so equal ratios occupy equal distances along it, and [Chapter 8](#ch-pitch-and-consonance) showed that pitch discrimination is likewise constant in proportional terms.

The intervals that matter most are the first few of the harmonic series:

| Interval | Ratio | Harmonics involved |
|---|---|---|
| Octave | $2{:}1$ | 1 and 2 |
| Perfect fifth | $3{:}2$ | 2 and 3 |
| Perfect fourth | $4{:}3$ | 3 and 4 |
| Major third | $5{:}4$ | 4 and 5 |
| Minor third | $6{:}5$ | 5 and 6 |

```{figure} ../images/notation/harmonic-series-on-c2.svg
:label: fig:ch09-harmonic-series
:alt: The first sixteen harmonics of C2 on bass and treble staves, each labeled with its harmonic number and its deviation in cents from the nearest equal-tempered note, with the seventh and fourteenth 31 cents flat, the eleventh 49 cents sharp, and the thirteenth 41 cents sharp.

The harmonic series again, now read as a source of intervals. The first six partials give the octave, the fifth, the fourth, and the major third, the consonances of Western music, in order. From the seventh partial upward the series diverges sharply from anything a keyboard can play, which is why those partials play almost no part in common-practice harmony.
```

### Intervals Multiply

Stack two intervals and the ratios **multiply**:

$$
\text{fifth} \times \text{fourth} = \frac{3}{2}\times\frac{4}{3} = 2 = \text{octave}.
$$

This is why a fifth plus a fourth is an octave, and it is also the source of a persistent confusion. Musicians count intervals by *adding*, a third plus a third is a fifth, because they are counting note names, which is a logarithmic count. The physics multiplies. The two are consistent, and cents are what reconciles them.

### The Cent

The **cent** is one hundredth of an equal-tempered semitone, so there are $1200$ to the octave. Converting between a ratio $r$ and an interval $n$ in cents:

$$
n = 1200\log_2 r,
\qquad
r = 2^{n/1200}.
$$

Cents are logarithmic, so they **add** the way musicians expect while representing ratios exactly. And the unit is well matched to the ear: [Chapter 8](#ch-pitch-and-consonance) put the just-noticeable difference at $3$–$6$ cents, so an error of a cent or two is inaudible and one of fifteen is obvious.

The essential values, worth memorizing:

| Interval | Ratio | Cents |
|---|---|---|
| Octave | $2{:}1$ | $1200.0$ |
| Pure fifth | $3{:}2$ | $701.955$ |
| Pure fourth | $4{:}3$ | $498.045$ |
| Pure major third | $5{:}4$ | $386.314$ |
| Pure minor third | $6{:}5$ | $315.641$ |
| Equal semitone | $2^{1/12}$ | $100.0$ |

```{figure} ../images/ch09-piano-keyboard.svg
:label: fig:ch09-piano-keyboard
:alt: One octave of a piano keyboard from C4 to C5, with the white keys of C major highlighted and the black keys labeled with their sharp and flat names.

Reading notes on a keyboard. The white keys trace the C-major scale, while each black key has two names: for example, C-sharp and D-flat are the same equal-tempered key. Moving to the next key, white or black, raises the pitch by one semitone; the octave from C4 to C5 contains twelve such steps.
```

::::{tip} Worked example: converting to and from cents
*(a) How many cents is the ratio $7{:}4$, the interval of the seventh harmonic? (b) What ratio is $350$ cents?*

(a)

$$
n = 1200\log_2(7/4) = 1200\log_2(1.75) = 1200(0.80735) = 968.8\ \text{cents}.
$$

The nearest equal-tempered interval is the minor seventh at $1000$ cents, so the seventh harmonic is $31$ cents flat of it, as the staff figure above says.

(b)

$$
r = 2^{350/1200} = 2^{0.29167} = 1.2240.
$$

That lies between the pure minor third ($1.2$) and the pure major third ($1.25$): a "neutral third", which appears in Arabic and Turkish music and in no Western keyboard.
::::

## Pythagorean Tuning

### A Chain of Pure Fifths

The oldest systematic tuning takes the two simplest ratios, the octave $2{:}1$ and the fifth $3{:}2$, and uses nothing else.

Start on a note and go up by fifths: C, G, D, A, E, B, F♯, … Each new note is $3/2$ times the last; whenever the pitch leaves the octave, halve it to bring it back. After twelve steps every chromatic note has been generated.

This produces beautiful fifths, by construction: every fifth in the chain is exactly pure. The fourths are pure too, being octave complements of fifths.

### The Pythagorean Comma

Now the problem. Twelve fifths should return to the starting note, seven octaves higher. They do not.

$$
\left(\frac{3}{2}\right)^{12} = 129.746, \qquad 2^7 = 128.
$$

The ratio between them is

$$
\frac{129.746}{128} = 1.013643,
$$

which is

$$
1200\log_2(1.013643) = 23.46\ \text{cents}.
$$

This is the **Pythagorean comma**, and it is not going away. The reason is elementary number theory: $(3/2)^{12} = 3^{12}/2^{12}$, and no power of $3$ is ever a power of $2$, since $3$ and $2$ are distinct primes. The chain of fifths can *never* close, at twelve steps or at any other number.

```{animation} ch09-comma-spiral
:label: fig:ch09-comma-spiral
:alt: Left, the pitch class of each successive fifth plotted against the number of fifths taken, showing that after twelve steps the chain lands 23.5 cents above where it started. Right, a bar chart comparing twelve pure fifths at 8423.5 cents with seven octaves at 8400 cents, with the 23.5 cent gap marked.

The chain of fifths fails to close. **Left**: each fifth folded back into a single octave; the twelfth lands not on C but $23.5$ cents above it. **Right**: the same fact as arithmetic. Twelve pure fifths overshoot seven octaves by the Pythagorean comma.
```

### The Scale It Produces

Pythagorean tuning gives pure fifths and fourths, and, as the price, a major third of

$$
\left(\frac{3}{2}\right)^4 \div 4 = \frac{81}{64} = 407.8\ \text{cents},
$$

against a pure $5{:}4$ of $386.3$ cents. That is $21.5$ cents sharp, an error known as the **syntonic comma**.

```{figure} ../images/notation/tuning-comparison.svg
:label: fig:ch09-tuning-comparison
:alt: A C major scale on a treble stave with three rows of numbers beneath giving each degree's deviation in cents from equal temperament under just intonation, Pythagorean tuning and equal temperament, with departures over ten cents marked in red.

The same seven notes, tuned three ways. Every system agrees on C, F, and G to within a couple of cents; they disagree about the thirds and sixths, and they disagree in opposite directions. Pythagorean thirds are sharp, just thirds are flat of equal temperament, and the gap between them is the syntonic comma.
```

Twenty-one cents is four times the threshold of detection, and on sustained tones it beats audibly. For medieval music this was tolerable, because the third was treated as a *dissonance* requiring resolution: the consonances were the octave, fifth, and fourth, which Pythagorean tuning renders perfectly. When the third became a consonance in the fifteenth century, the tuning had to change.

## Just Intonation

### Bringing In the Fifth Harmonic

**Just intonation** adds the ratio $5{:}4$ to the toolkit and builds the scale from three pure triads: on the tonic, the subdominant, and the dominant. Each triad is tuned $4{:}5{:}6$: a pure major third and a pure fifth.

The resulting C major scale:

| Note | Ratio | Cents |
|---|---|---|
| C | $1{:}1$ | $0$ |
| D | $9{:}8$ | $203.9$ |
| E | $5{:}4$ | $386.3$ |
| F | $4{:}3$ | $498.0$ |
| G | $3{:}2$ | $702.0$ |
| A | $5{:}3$ | $884.4$ |
| B | $15{:}8$ | $1088.3$ |
| C | $2{:}1$ | $1200$ |

Played in C, this is gorgeous. The tonic, subdominant, and dominant triads are all exactly pure, with every partial coinciding and nothing beating at all.

```{audio} ch09-triad-just, ch09-triad-equal
:names: Just, Equal-tempered
:figure: ../images/ch09-third-comparison.svg
:label: fig:ch09-triad-comparison
:transcript: Two C major triads. The first is still and glassy, with no movement in it at all. The second has an audible shimmer, a slow waver that the first does not have.

A C major triad, tuned justly and in equal temperament. The difference is not one of pitch, both are unmistakably C major, but of *stillness*. The just triad has nothing beating in it; the tempered one beats about ten times a second in its third.
```

```{audio} ch09-third-just, ch09-third-equal
:names: Just 5:4, Equal-tempered
:figure: ../images/ch09-third-comparison.svg
:label: fig:ch09-third-comparison
:transcript: Two major thirds. The first is perfectly steady; the second has a distinct and rather fast beating in it, about ten beats a second.

The major third alone, where the effect is clearest. The figure shows why: the lower note's fifth partial and the upper note's fourth partial coincide exactly when the third is pure, and differ by about $10$ Hz when it is tempered.
```

### Two Sizes of Whole Tone, and the Wolf

The trouble appears as soon as you look at the intervals *between* the scale degrees.

$$
\text{C to D} = \frac{9}{8} = 203.9\ \text{cents},
\qquad
\text{D to E} = \frac{5/4}{9/8} = \frac{10}{9} = 182.4\ \text{cents}.
$$

There are **two different whole tones**, differing by $21.5$ cents: the syntonic comma again. A keyboard has one key for each, so it must choose.

The consequence is a fifth that is badly out of tune:

$$
\text{D to A} = \frac{5/3}{9/8} = \frac{40}{27} = 680.4\ \text{cents},
$$

against a pure $702$ cents. That fifth is $21.5$ cents narrow, and it beats violently. It is the **wolf fifth**, named for its howl.

```{figure} ../images/ch09-wolf-fifth.svg
:label: fig:ch09-wolf-fifth
:alt: A bar chart of the six perfect fifths within a just C major scale, five of them exactly pure and one, D to A, twenty-one and a half cents narrow, marked as the wolf.

The fifths inside a just C major scale. Five are exactly pure. One, D–A, is a syntonic comma narrow, and it is unusable in sustained harmony.
```

```{audio} ch09-fifth-pure, ch09-fifth-wolf
:names: A pure fifth, The wolf fifth
:figure: ../images/ch09-wolf-fifth.svg
:label: fig:ch09-wolf-fifth-audio
:transcript: Two fifths. The first is perfectly still. The second has a fast, insistent beating that makes it sound actively wrong rather than merely different.

A pure fifth and the wolf. The wolf is not subtly out of tune; it is the kind of thing a listener assumes is a mistake.
```

### Why Just Intonation Cannot Modulate

The deeper problem is not the single wolf. It is that just intonation is tuned **for one key**, and there is no way to make a fixed set of twelve pitches serve them all.

```{audio} ch09-just-in-c, ch09-just-in-d
:names: I–IV–V–I in C, The same progression in D
:figure: ../images/ch09-system-comparison.svg
:label: fig:ch09-modulation
:transcript: The same four-chord progression, played twice on the same twelve fixed pitches. In C it is clean and settled. Moved up a tone to D, the same chords are audibly sour, with obvious beating.

One set of twelve pitches, tuned justly for C, playing the same progression in two keys. The instrument has not been retuned between the two; the *music* has moved, and the tuning has not moved with it. This is the practical argument that ended just intonation as a keyboard tuning.
```

Singers, string quartets, and trombonists do not have this problem, because they adjust continuously. They routinely play closer to just intonation than to equal temperament: a good choir will tune a sustained chord pure without being asked. **Just intonation was never abandoned by musicians who can bend their pitch. It was abandoned by keyboards**, and only because a keyboard has to decide in advance.

## Meantone and the Well Temperaments

### Spending the Comma Deliberately

The insight that unlocked the problem is that the comma has to go *somewhere*, but it does not have to go all in one place. Distribute it and no single interval is ruined.

A system that does this deliberately is a **temperament**, and the choice of how to distribute is a choice about which keys will sound best.

### Quarter-Comma Meantone

The most important historical temperament narrows every fifth by a quarter of a syntonic comma, about $5.4$ cents, which is just at the edge of audibility.

Four narrowed fifths then produce a major third that is *exactly* pure:

$$
4 \times (701.955 - 5.377) = 2786.3\ \text{cents},
$$

which, less two octaves, is $386.3$ cents: the pure $5{:}4$.

```{figure} ../images/ch09-interval-errors.svg
:label: fig:ch09-interval-errors
:alt: Two bar charts comparing the error in cents of the perfect fifth and the major third under Pythagorean tuning, quarter-comma meantone, just intonation and equal temperament, with a shaded band marking six cents.

Where each system puts its error. Pythagorean tuning buys pure fifths at the cost of a $22$ cent third. Quarter-comma meantone buys pure thirds at the cost of a $5$ cent fifth, which is barely audible. Equal temperament splits the difference, with a fifth $2$ cents narrow and a third $14$ cents sharp.
```

Meantone dominated European keyboard music for two centuries, and for good reason: it makes major thirds beatless, and thirds are what Renaissance and early Baroque harmony is built on. Its price is that the twelve fifths still cannot close, so the accumulated error is dumped into one interval, traditionally G♯–E♭, which becomes a wolf of about $737$ cents, $35$ cents wide and completely unusable. Composers simply avoided the keys that needed it.

### Well Temperament and Key Color

By the late seventeenth century composers wanted more keys, and **well temperaments** were the answer: distribute the comma unevenly, so that no interval is unusable but the distribution is not uniform either.

The consequence is that **each key sounds different**. Keys with few accidentals are nearly pure; remote keys are progressively more tempered and sound more restless. This is "key color", and eighteenth-century writers described keys in terms that sound like synesthesia, D major brilliant, E♭ major solemn, F minor mournful, and were describing something real about their instruments.

:::{note}
Bach's *Das wohltemperirte Clavier* means "the well-tempered keyboard", not "the equal-tempered keyboard", and the distinction matters. The collection demonstrates that all twenty-four keys are *usable*, which is a well-temperament claim. In equal temperament all keys are not merely usable but identical, and the point of writing in all of them would largely vanish.
:::

## Equal Temperament

### Twelve Equal Semitones

**Equal temperament** takes the distribution to its limit: divide the octave into twelve exactly equal steps.

The requirement is that twelve semitones make an octave, so each semitone is

$$
r = 2^{1/12} = 1.059463,
$$

which is $100$ cents by definition. Every interval of $n$ semitones is $2^{n/12}$.

The mathematics is forced. Twelve equal multiplicative steps making a factor of two admits exactly one solution, and the twelfth root of two is irrational; so **no** equal-tempered interval except the octave is ever a whole-number ratio.

::::{tip} Worked example: the whole keyboard from one number
*Given A$_4$ = $440$ Hz, find the frequency of C$_5$ (three semitones up) and of A$_2$ (two octaves down).*

$$
f_{\mathrm{C}_5} = 440 \times 2^{3/12} = 440 \times 1.18921 = 523.25\ \text{Hz}.
$$

$$
f_{\mathrm{A}_2} = 440 \times 2^{-24/12} = \frac{440}{4} = 110\ \text{Hz}.
$$

Every note on a modern keyboard follows from $f = 440 \times 2^{n/12}$, with $n$ the number of semitones from A$_4$. That single formula replaced two thousand years of argument about ratios.
::::

### What It Costs and What It Buys

```{figure} ../images/ch09-system-comparison.svg
:label: fig:ch09-system-comparison
:alt: A grouped bar chart showing, for each of the twelve chromatic notes, the deviation in cents from equal temperament under Pythagorean tuning and just intonation, with equal temperament flat at zero by definition and a shaded band marking six cents.

Three tunings, note by note. Equal temperament is the zero line by construction. Pythagorean and just intonation disagree with it, and with each other, by up to about $20$ cents, mostly on the thirds and sixths.
```

The accounting for equal temperament:

| Interval | Equal | Pure | Error |
|---|---|---|---|
| Octave | $1200$ | $1200$ | $0$ |
| Fifth | $700$ | $701.96$ | $-1.96$ |
| Fourth | $500$ | $498.04$ | $+1.96$ |
| Major third | $400$ | $386.31$ | $+13.69$ |
| Minor third | $300$ | $315.64$ | $-15.64$ |
| Major sixth | $900$ | $884.36$ | $+15.64$ |

The fifth is $2$ cents narrow, well below the threshold of detection, and essentially perfect. The thirds and sixths are $14$ to $16$ cents out, which is clearly audible on sustained tones.

So equal temperament is a *worse* compromise than meantone for any single key. What it buys is that **the compromise is the same everywhere**. Every key is equally usable, unlimited modulation is possible, and any piece can be transposed without retuning.

The nineteenth century decided that was worth an audibly imperfect third, and the decision has held. Notice that this was a trade of *quality* for *freedom*, made by a musical culture that had begun to care more about harmonic adventure than about the purity of a sustained chord.

### Comparing the Systems in Cents

A summary of the three main systems in one table:

| | Fifths | Major thirds | Modulation |
|---|---|---|---|
| Pythagorean | All pure | $22$ cents sharp | Impossible (comma) |
| Just | Mostly pure, one wolf | Pure in home key | Impossible (wrong key) |
| Quarter-comma meantone | $5$ cents narrow | Pure | Limited (wolf at G♯–E♭) |
| Equal | $2$ cents narrow | $14$ cents sharp | Unlimited |

Read down the last column and the history explains itself.

```{video} https://www.youtube.com/watch?v=gtkeDDcXu9M
:video-title: Equal Temperament vs. Just Intonation
:label: fig:ch09-equal-vs-just-video
:alt: A musician compares the pitches and interval ratios of equal temperament and just intonation.

Adam Neely compares equal temperament with just intonation from a working musician's perspective. The examples make audible both the pure intervals that just tuning gains and the freedom to change key that equal temperament buys.
```

## Tuning in Practice

### Fixed-Pitch and Flexible-Pitch Instruments

Equal temperament is universal on **fixed-pitch** instruments, piano, organ, harp, fretted strings, mallet percussion, because those instruments must commit in advance.

It is much less universal among **flexible-pitch** instruments, which adjust as they play:

- A **string quartet** tunes sustained chords toward just intonation, narrowing thirds instinctively.
- A **choir** does the same, more strongly; a well-tuned a cappella chord is close to pure.
- A **trombonist** has a continuously variable slide and uses it.
- **Wind players** adjust with embouchure and alternate fingerings continuously.

Ensembles mixing the two families negotiate. A string quartet plays closer to just; add a piano and the strings bend toward it, because the piano cannot bend toward them.

:::{warning}
It is tempting to say flexible-pitch players "play in just intonation". They do not, quite. They play *expressively*, which often means the opposite: a leading note is frequently played **sharp**, sharper even than equal temperament, to intensify its pull toward the tonic. That is a melodic impulse pulling against the harmonic one, and good players trade between them constantly.
:::

### Stretched Tuning on the Piano

One place where even equal temperament is not quite applied is the piano, for the reason [Chapter 5](#ch-fourier-and-timbre) gave.

Piano strings are stiff, so their partials are **inharmonic**: the $n$th partial is sharp of $n$ times the fundamental. A tuner setting an octave listens to the lower note's second partial against the upper note's fundamental, and since that second partial is sharp, the octave must be stretched to match it.

The result is the **Railsback curve**: a piano's treble is tuned progressively sharp and its bass progressively flat, by as much as $30$ cents at the extremes. A piano tuned to a mathematically exact equal temperament sounds *out of tune*, and every tuner stretches without needing to be told to. [Chapter 10](#ch-string-instruments) works through the mechanism.

### Scales Outside the Western Tradition

Twelve equal divisions is one solution among many, and the alternatives are not approximations to it.

**Indian classical music** uses *shrutis*, traditionally twenty-two per octave, and raga performance draws on just ratios with ornaments that pass between them. The tradition has no fixed-pitch keyboard to force a compromise, so it never needed one.

**Arabic and Turkish music** use intervals near the quarter tone, including the neutral third of about $350$ cents computed in §9.1: an interval with no equal-tempered equivalent at all.

**Javanese and Balinese gamelan** use *slendro* (roughly five near-equal steps) and *pelog* (seven unequal steps), and no two gamelan sets are tuned alike. [Chapter 8](#ch-pitch-and-consonance) gave the reason this is coherent rather than arbitrary: gamelan instruments have **inharmonic** partials, so their dissonance curve has its minima somewhere other than the simple ratios, and the scales sit on those minima.

The general principle is the one §8.4 established. A scale and a timbre belong together. Western tuning theory is the theory of scales for instruments with harmonic partials, and it is not more fundamental than the alternatives, it is more *specialized*, and its specialization is to strings and pipes.

## Summary

- **An interval is a ratio**, and intervals multiply. The **cent**, $1200$ to the octave, $n = 1200\log_2 r$, makes ratios additive and is well matched to the ear, whose discrimination is $3$–$6$ cents.
- **The chain of fifths never closes.** Twelve pure fifths exceed seven octaves by the **Pythagorean comma**, $23.5$ cents, because no power of $3$ is a power of $2$. Four pure fifths exceed a pure major third plus two octaves by the **syntonic comma**, $21.5$ cents.
- **Pythagorean tuning** gives every fifth pure and every major third $22$ cents sharp. Acceptable while the third was a dissonance; untenable once it became a consonance.
- **Just intonation** gives pure triads on the tonic, subdominant, and dominant, at the cost of two sizes of whole tone, a wolf fifth at D–A, and the impossibility of modulating.
- **Quarter-comma meantone** narrows every fifth by $5.4$ cents to make major thirds exactly pure, and dumps the remaining error into one unusable wolf. **Well temperaments** distribute it unevenly, making every key usable and each key different.
- **Equal temperament** makes every semitone $2^{1/12}$. Fifths are $2$ cents narrow (inaudible), thirds $14$ cents sharp (audible). It is a worse compromise than meantone in any one key and the only one that is the same in all of them.
- **Fixed-pitch instruments use equal temperament; flexible-pitch ones do not.** Singers and string players bend toward just intonation harmonically and away from it melodically, and negotiate with any keyboard present.
- **Pianos are tuned stretched**, because string stiffness makes their partials sharp, and an octave must match the partial rather than the arithmetic.
- **Other traditions divide the octave differently**, and where their instruments have inharmonic partials those divisions are as well founded as ours.

## Conceptual Questions

1. Explain why intervals are ratios rather than differences, and connect the answer to the cochlea.

2. Explain, in terms of prime factorization, why a chain of pure fifths can never close into a whole number of octaves, at twelve steps or at any other number.

3. Pythagorean tuning was satisfactory for medieval music and unsatisfactory for Renaissance music. Explain what changed.

4. A choir sings a sustained chord and a piano plays the same chord. Explain why the choir's version is likely to be closer to just intonation, and why the piano's cannot be.

5. Explain why the wolf fifth in just intonation arises from there being two sizes of whole tone.

6. Quarter-comma meantone has a fifth $5.4$ cents narrow and equal temperament has one $2.0$ cents narrow, yet meantone's thirds are much better. Explain how meantone can be worse on fifths and better on thirds.

7. Explain what "key color" meant in a well temperament and why the concept largely evaporates in equal temperament.

8. A piano tuned to mathematically exact equal temperament sounds out of tune. Explain why, and say what a tuner does instead.

## Problems

:::{exercise}
:label: ex-scales-and-tuning-1

*(Straightforward)* Convert to cents: (a) the pure fifth $3{:}2$, (b) the pure major third $5{:}4$, (c) the ratio $7{:}6$.
:::

:::{solution} ex-scales-and-tuning-1
:label: sol-scales-and-tuning-1
:class: dropdown

Using $n = 1200\log_2 r$.

(a) $1200\log_2(1.5) = 1200(0.58496) = 701.96$ cents.

(b) $1200\log_2(1.25) = 1200(0.32193) = 386.31$ cents.

(c) $1200\log_2(7/6) = 1200\log_2(1.16667) = 1200(0.22239) = 266.87$ cents.

Therefore $702.0$, $386.3$, and $266.9$ cents. The last lies between the equal-tempered minor third ($300$) and major second ($200$), and belongs to no Western key.
:::

:::{exercise}
:label: ex-scales-and-tuning-2

*(Straightforward)* Convert to frequency ratios: (a) $700$ cents, (b) $400$ cents, (c) $1200$ cents.
:::

:::{solution} ex-scales-and-tuning-2
:label: sol-scales-and-tuning-2
:class: dropdown

Using $r = 2^{n/1200}$.

(a) $2^{700/1200} = 2^{0.58333} = 1.49831$.

(b) $2^{400/1200} = 2^{0.33333} = 1.25992$.

(c) $2^{1} = 2.00000$.

Therefore $1.4983$, $1.2599$, and $2$. Comparing with the pure values $1.5$ and $1.25$: the tempered fifth is $0.11\%$ narrow and the tempered third $0.79\%$ sharp: the third is seven times worse.
:::

:::{exercise}
:label: ex-scales-and-tuning-3

*(Moderate)* Calculate the Pythagorean comma from scratch. (a) Find $(3/2)^{12}$. (b) Find $2^7$. (c) Express the ratio in cents.
:::

:::{solution} ex-scales-and-tuning-3
:label: sol-scales-and-tuning-3
:class: dropdown

(a) $(3/2)^{12} = 3^{12}/2^{12} = 531441/4096 = 129.7463$.

(b) $2^7 = 128$.

(c)

$$
\frac{129.7463}{128} = 1.0136433,
\qquad
1200\log_2(1.0136433) = 23.46\ \text{cents}.
$$

Therefore the comma is $23.5$ cents, very nearly a quarter of a semitone, about four to eight times the threshold of detection, and unmistakable on sustained tones.
:::

:::{exercise}
:label: ex-scales-and-tuning-4

*(Moderate)* Calculate the syntonic comma. (a) Find the Pythagorean major third $(3/2)^4$ reduced to one octave. (b) Compare with the pure $5{:}4$. (c) Express the difference in cents.
:::

:::{solution} ex-scales-and-tuning-4
:label: sol-scales-and-tuning-4
:class: dropdown

(a) $(3/2)^4 = 81/16 = 5.0625$. Dividing by $4$ to bring it into one octave: $81/64 = 1.265625$.

(b) The pure third is $5/4 = 1.25$.

(c)

$$
\frac{81/64}{5/4} = \frac{81}{80} = 1.0125,
\qquad
1200\log_2(1.0125) = 21.51\ \text{cents}.
$$

Therefore the syntonic comma is $21.5$ cents, the ratio $81{:}80$. It is the difference between the third you get from stacking fifths and the third the harmonic series offers, and it is what meantone temperament distributes.
:::

:::{exercise}
:label: ex-scales-and-tuning-5

*(Moderate)* Take C$_4$ = $261.63$ Hz. Find the frequency of E$_4$ (a) in equal temperament, (b) in just intonation, (c) in Pythagorean tuning. (d) Express the spread in cents.
:::

:::{solution} ex-scales-and-tuning-5
:label: sol-scales-and-tuning-5
:class: dropdown

(a) $261.63 \times 2^{4/12} = 261.63 \times 1.259921 = 329.63$ Hz.

(b) $261.63 \times 5/4 = 327.04$ Hz.

(c) $261.63 \times 81/64 = 331.12$ Hz.

(d) From lowest to highest:

$$
1200\log_2\!\left(\frac{331.12}{327.04}\right) = 21.5\ \text{cents}.
$$

Therefore the three Es span $327.0$ to $331.1$ Hz, a spread of $21.5$ cents: the syntonic comma, with equal temperament sitting about two-thirds of the way up.
:::

:::{exercise}
:label: ex-scales-and-tuning-6

*(Moderate)* A quarter-comma meantone fifth is narrowed by a quarter of the syntonic comma. (a) By how many cents? (b) What is the meantone fifth, in cents and as a ratio? (c) Verify that four of them, less two octaves, give a pure major third.
:::

:::{solution} ex-scales-and-tuning-6
:label: sol-scales-and-tuning-6
:class: dropdown

(a) $21.51/4 = 5.377$ cents.

(b) $701.955 - 5.377 = 696.578$ cents, which is

$$
r = 2^{696.578/1200} = 1.495349.
$$

(c) Four such fifths:

$$
4 \times 696.578 = 2786.31\ \text{cents}.
$$

Two octaves is $2400$ cents, so the third is

$$
2786.31 - 2400 = 386.31\ \text{cents},
$$

which is exactly $1200\log_2(5/4)$.

Therefore the construction works exactly, and that exactness is the whole point of the quarter: it is chosen to make the third pure, not as a rough compromise.
:::

:::{exercise}
:label: ex-scales-and-tuning-7

*(Moderate)* In just intonation on C, find the interval D–A. (a) Give the ratio and the cents. (b) How far is it from a pure fifth? (c) If A$_4$ = $440$ Hz in this tuning, what beat rate would a listener hear between the third harmonic of D and the second harmonic of A?
:::

:::{solution} ex-scales-and-tuning-7
:label: sol-scales-and-tuning-7
:class: dropdown

(a) D is $9/8$ and A is $5/3$, so

$$
\frac{5/3}{9/8} = \frac{40}{27} = 1.48148,
\qquad
1200\log_2(1.48148) = 680.45\ \text{cents}.
$$

(b) $701.96 - 680.45 = 21.5$ cents narrow, one syntonic comma.

(c) If A = $440$ Hz then D $= 440 \times 27/40 = 297.0$ Hz. The relevant harmonics:

$$
3 \times 297.0 = 891.0\ \text{Hz},
\qquad
2 \times 440 = 880.0\ \text{Hz},
$$
$$
f_{\text{beat}} = 11.0\ \text{Hz}.
$$

Therefore the wolf beats eleven times a second, far too fast to count and squarely in the range [Chapter 8](#ch-pitch-and-consonance) identified as maximally rough. This is why it howls.
:::

:::{exercise}
:label: ex-scales-and-tuning-8

*(Challenging)* Show that in just intonation the whole tones C–D and D–E are different sizes, and find the difference. Explain why a keyboard cannot accommodate both.
:::

:::{solution} ex-scales-and-tuning-8
:label: sol-scales-and-tuning-8
:class: dropdown

C–D is $9/8 = 203.91$ cents. D–E is

$$
\frac{5/4}{9/8} = \frac{10}{9} = 182.40\ \text{cents}.
$$

The difference is

$$
\frac{9/8}{10/9} = \frac{81}{80} = 21.5\ \text{cents},
$$

the syntonic comma again.

A keyboard has one key per note name, so it must assign a single pitch to D. If D is placed to make C–D a $9{:}8$ tone, then D–E is a $10{:}9$ tone and the fifth D–A is a comma narrow. If D is placed the other way, some other interval breaks instead.

Therefore the instrument is short of keys, not short of cleverness. Some seventeenth-century keyboards addressed this literally, with split black keys giving separate D♯ and E♭, and they were abandoned as unplayable.
:::

:::{exercise}
:label: ex-scales-and-tuning-9

*(Moderate)* An equal-tempered perfect fifth is built on A$_3$ = $220$ Hz. (a) Find the upper frequency. (b) Find the beat rate between the third harmonic of the lower note and the second of the upper. (c) Repeat for the major third, using the fifth and fourth harmonics. (d) Comment.
:::

:::{solution} ex-scales-and-tuning-9
:label: sol-scales-and-tuning-9
:class: dropdown

(a) $220 \times 2^{7/12} = 220 \times 1.498307 = 329.63$ Hz.

(b) $3 \times 220 = 660.00$ Hz against $2 \times 329.63 = 659.26$ Hz:

$$
f_{\text{beat}} = 0.74\ \text{Hz}.
$$

(c) The third: $220 \times 2^{4/12} = 277.18$ Hz. Then $5 \times 220 = 1100.0$ Hz against $4 \times 277.18 = 1108.7$ Hz:

$$
f_{\text{beat}} = 8.7\ \text{Hz}.
$$

(d) The tempered fifth beats less than once a second, slow enough to pass for still. The tempered third beats nearly nine times a second, which is right in the roughest range.

Therefore equal temperament's compromise is very uneven in its audible effect: the fifths are essentially free and the thirds are paid for dearly. This is exactly what the meantone temperaments refused to accept.
:::

:::{exercise}
:label: ex-scales-and-tuning-10

*(Moderate)* Consider a system dividing the octave into $19$ equal steps. (a) How many cents is each step? (b) Which multiple of a step best approximates a pure fifth, and with what error? (c) The pure major third?
:::

:::{solution} ex-scales-and-tuning-10
:label: sol-scales-and-tuning-10
:class: dropdown

(a) $1200/19 = 63.16$ cents.

(b) A pure fifth is $701.96$ cents:

$$
\frac{701.96}{63.16} = 11.12,
$$

so eleven steps, giving $11 \times 63.16 = 694.7$ cents: an error of $-7.2$ cents.

(c) A pure third is $386.31$ cents:

$$
\frac{386.31}{63.16} = 6.12,
$$

so six steps, giving $6 \times 63.16 = 378.9$ cents: an error of $-7.4$ cents.

Therefore 19-tone equal temperament has a fifth $7$ cents narrow (worse than $12$-tone's $2$) but a third $7$ cents flat (much better than $12$-tone's $14$ sharp). It is, in effect, a closed version of meantone, and it was advocated on exactly those grounds in the sixteenth century and again in the twentieth.
:::

:::{exercise}
:label: ex-scales-and-tuning-11

*(Challenging)* Show that no equal division of the octave can contain an exactly pure fifth.
:::

:::{solution} ex-scales-and-tuning-11
:label: sol-scales-and-tuning-11
:class: dropdown

Suppose the octave is divided into $N$ equal steps, so each step is the ratio $2^{1/N}$, and suppose $k$ steps give exactly a pure fifth:

$$
2^{k/N} = \frac{3}{2}.
$$

Raising both sides to the power $N$:

$$
2^{k} = \left(\frac{3}{2}\right)^{N} = \frac{3^N}{2^N},
\qquad\text{so}\qquad
2^{k+N} = 3^{N}.
$$

The left side has only the prime factor $2$; the right has only the prime factor $3$. By unique factorization these can be equal only if both are $1$, requiring $N = 0$, not a division of the octave at all.

Therefore no equal temperament of any size contains a pure fifth, and the same argument rules out a pure major third, since $5$ is likewise not a power of $2$. **Every equal temperament is a compromise**; the only choice is how good an approximation $N$ buys, which is why $12$, $19$, $31$, and $53$ recur in the literature, they are the divisions where the approximations happen to be unusually good.
:::

:::{exercise}
:label: ex-scales-and-tuning-12

*(Moderate)* A well temperament has fifths tempered by different amounts: C–G by $-6$ cents, G–D by $-6$, D–A by $-4$, A–E by $-4$, and the remaining eight fifths by whatever is needed. (a) How much of the comma has been absorbed so far? (b) How much remains to spread over the other eight? (c) Comment on the resulting key color.
:::

:::{solution} ex-scales-and-tuning-12
:label: sol-scales-and-tuning-12
:class: dropdown

(a) $6 + 6 + 4 + 4 = 20$ cents.

(b) The Pythagorean comma is $23.5$ cents, so

$$
23.5 - 20 = 3.5\ \text{cents}
$$

remains, spread over eight fifths, about $0.44$ cents each, which is imperceptible.

(c) The heavily tempered fifths lie among the naturals, so the keys built on them, C, G, D, A, have thirds noticeably closer to pure than equal temperament provides. The remote keys, whose fifths are essentially untempered, inherit almost-Pythagorean thirds, some $20$ cents sharp, and sound correspondingly tense and bright.

Therefore every key is usable and no two sound alike: the common keys are sweet and the remote ones are edgy. That is precisely what eighteenth-century writers meant by key character, and it is a real acoustic property of the instrument rather than a literary conceit.
:::

:::{exercise}
:label: ex-scales-and-tuning-13

*(Moderate)* A piano's A$_2$ has an inharmonicity coefficient $B = 3.0\times10^{-4}$ and a nominal fundamental of $110$ Hz. (a) Find its second partial. (b) If A$_3$ is tuned so that its fundamental matches that partial, what is A$_3$'s frequency? (c) How many cents sharp of an exact octave is that?
:::

:::{solution} ex-scales-and-tuning-13
:label: sol-scales-and-tuning-13
:class: dropdown

(a) Using $f_n = nf_1\sqrt{1 + Bn^2}$ with $n = 2$:

$$
f_2 = 2(110)\sqrt{1 + (3.0\times10^{-4})(4)} = 220\sqrt{1.0012} = 220.13\ \text{Hz}.
$$

(b) The tuner matches A$_3$'s fundamental to it: $220.13$ Hz.

(c) An exact octave would be $220.00$ Hz:

$$
1200\log_2\!\left(\frac{220.13}{220.00}\right) = 1.0\ \text{cent}.
$$

Therefore this octave is stretched by one cent. That is small, but it *accumulates*: seven octaves tuned this way, each stretched a little and each stretching more as the strings get shorter and stiffer, produces the tens of cents of the Railsback curve at the extremes of the keyboard.
:::

:::{exercise}
:label: ex-scales-and-tuning-14

*(Moderate)* A composer writes for an ensemble of a string quartet and a piano. (a) Explain the tuning conflict. (b) The quartet plays a sustained A major triad alone, then the piano enters with the same chord. Describe what a listener hears. (c) Suggest what the quartet will actually do.
:::

:::{solution} ex-scales-and-tuning-14
:label: sol-scales-and-tuning-14
:class: dropdown

(a) The quartet can adjust its pitches continuously and will naturally tune a sustained triad toward just intonation, with the third about $14$ cents flat of equal temperament. The piano is fixed in equal temperament and cannot move.

(b) Alone, the quartet's chord is still and beatless. When the piano enters, its C♯ is $14$ cents sharp of the quartet's, and the two thirds beat against each other at roughly $10$ Hz: a clearly audible sourness that was not there a moment before.

(c) The quartet will bend toward the piano, because it is the only party that can. In practice string players in this situation play thirds sharper than they would unaccompanied, sacrificing the purity of their own chord to avoid beating against the fixed instrument.

Therefore the compromise falls entirely on the flexible players, which is the general rule whenever fixed and flexible instruments play together, and one reason string players often describe playing with piano as harmonically constraining.
:::
