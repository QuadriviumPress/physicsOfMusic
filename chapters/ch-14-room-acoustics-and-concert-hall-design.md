---
title: "Room Acoustics and Concert-Hall Design"
short_title: "Chapter 14. Room Acoustics and Concert-Hall Design"
label: ch-room-acoustics
numbering:
  enumerator: "14.%s"
  heading_1: true
exports:
  # A standalone offprint of this chapter, for students who want to print
  # or work from one chapter. `chapter:` is a templates/book option: it
  # switches the class to article and starts the section counter, so the
  # reading sections stay numbered 14.1, 14.2 ... as in the full book.
  - id: chapter-pdf
    format: pdf
    template: ../templates/book
    output: ../exports/ch-14-room-acoustics-and-concert-hall-design.pdf
    chapter: 14
---

### Learning Objectives

By the end of this chapter, you should be able to:

- Distinguish the direct sound, the early reflections, and the reverberant field, and sketch the echogram of a room.
- Explain why the inverse-square law fails indoors, and define the critical distance at which the reverberant field equals the direct sound.
- Define the absorption coefficient, calculate the total absorption of a room from its surfaces, and explain why absorption depends on frequency.
- Apply the Sabine equation to estimate reverberation time from room volume and absorption, and state the assumptions under which it is valid.
- State the reverberation times appropriate to speech, chamber music, orchestral music, and organ music, and explain why they differ.
- Explain the roles of specular reflection, diffusion, and absorption in a hall, and identify the acoustic defects each is used to address.
- Calculate the lowest room modes of a rectangular room, and explain why they matter in a small room and not in a large one.
- Identify the objective measures that correlate with the subjective judgment of a hall -- early decay time, clarity, and lateral energy -- and state what each measures.
- Compare the shoebox, fan, and vineyard hall plans, and explain the acoustic argument for and against each.

### Introduction

```{figure} ../images/open/ch14-hall.jpg
:label: fig:ch14-open-hall
:alt: Walt Disney Concert Hall viewed from outside.

The geometry of a hall is part of the instrument. This public-domain USGS photograph gives the abstract room models an architectural scale.
```

Everything so far has treated the instrument as the source of the sound a listener hears. It is not. Between the instrument and the ear is a room, and in almost every case **most of what reaches the listener has bounced off something.**

In a concert hall, a listener in the middle of the stalls receives perhaps a tenth of their sound energy directly from the stage. The rest arrives later, from every direction, having reflected once, twice, or a hundred times. The room is not a transparent medium through which music passes; it is part of the instrument.

This has two consequences that run through the chapter.

**The room is unavoidable.** A performance in a different hall is a different performance, in a way a listener notices immediately. Composers have written for particular acoustics, Gabrieli for the reverberation of San Marco, chamber composers for small dry rooms, and a piece played in the wrong acoustic can be incoherent.

**The room is designable**, but only partly. The quantities that matter have been measurable for a century and the correlations with subjective judgment are good but not perfect. Halls built on the best available understanding have failed, and the failures have generally taught more than the successes.

The chapter builds three things in order: a picture of what arrives at a listener and when; the single most useful number, the reverberation time; and then the harder question of why some halls with the right reverberation time are nevertheless bad.

## Sound in an Enclosure

### Direct, Early, and Reverberant

A short sound on stage produces, at a listener's ear, a long and structured sequence of arrivals.

```{figure} ../images/ch14-echogram.svg
:label: fig:ch14-echogram
:alt: An echogram showing a single tall green spike at time zero labeled direct sound, a group of blue spikes in the first 80 milliseconds labeled early reflections, and a dense field of purple spikes under an exponentially decaying envelope labeled reverberant tail.

An echogram. The **direct sound** arrives first, by the shortest path. **Early reflections** follow within about $80$ ms, having bounced once or twice. The **reverberant tail** is the accumulation of everything else, arriving so densely and from so many directions that individual reflections can no longer be distinguished.
```

The three parts do different perceptual jobs.

The **direct sound** tells you where the source is. It arrives first, and the auditory system's precedence effect locates the source by it, disregarding the later arrivals for the purpose of direction.

The **early reflections** are *not* heard as echoes. Anything arriving within roughly $50$–$80$ ms of the direct sound is fused with it, this is the **Haas effect**, and it makes the sound louder and fuller rather than doubled. Early reflections are therefore free loudness, and §14.4 shows that where they come *from* matters a great deal.

The **reverberant tail** provides the sense of a space. It is what makes a hall sound large, and it is what a recording engineer adds artificially when a recording sounds dead.

### The Echogram

The echogram is the room's **impulse response**: what a listener at one position receives from a source at one position, in response to a single impulse.

It contains everything linear about the room. Convolve any dry signal with it and you obtain what that signal would sound like at that seat, which is exactly how the audio examples in this chapter were made, and exactly how convolution reverb works in a recording studio ([Chapter 15](#ch-electronic-and-recorded-sound)).

### Critical Distance

[Chapter 2](#ch-wave-motion) noted that the inverse-square law fails indoors. The place where it fails is the **critical distance**: the distance at which the direct sound and the reverberant field are equally strong.

$$
r_c \approx 0.057\sqrt{\frac{V}{T_{60}}}
$$

with $V$ in cubic meters and $T_{60}$ in seconds.

Inside $r_c$, moving closer makes a real difference. Beyond it, the reverberant field dominates and moving further away changes the level very little. That is how the back row of a large hall stays audible at all, and also why it is so much less *clear* than the front.

::::{tip} Worked example: where the back row stops getting quieter
*A hall of $20{,}000$ m³ has $T_{60} = 2.0$ s. Find the critical distance, and comment.*

$$
r_c = 0.057\sqrt{\frac{20000}{2.0}} = 0.057\sqrt{10000} = 5.7\ \text{m}.
$$

Only the first few rows are inside it. Everyone else is hearing a sound field dominated by reflections, at a level that barely changes from row ten to row forty.

This is the central fact of concert-hall listening. It is why a hall can seat two thousand people without the back half straining to hear, and it is also why the back half hears something appreciably less clear than the conductor does.
::::

## Absorption and Reverberation Time

### The Absorption Coefficient

Every reflection loses energy. The **absorption coefficient** $\alpha$ of a surface is the fraction of incident energy it does not reflect: $0$ for a perfect mirror, $1$ for an open window.

```{figure} ../images/ch14-absorption.svg
:label: fig:ch14-absorption
:alt: Absorption coefficient against frequency for five materials, with painted concrete near zero everywhere, wood paneling absorbing more at low frequencies, carpet and curtains absorbing much more at high frequencies, and an occupied audience absorbing strongly across the range.

Absorption coefficients of common surfaces. Two things matter here. Absorption depends strongly on **frequency**, most soft materials absorb treble far better than bass, so untreated rooms tend to sound boomy. And **the audience is the most absorbent thing in the hall**.
```

That last point is a practical problem rather than a curiosity. A full hall and an empty hall are acoustically different rooms, and a rehearsal in an empty hall is a poor guide to the concert. Halls are designed with heavily upholstered seats chosen so that an empty seat absorbs approximately as much as an occupied one: concert-hall seating is therefore much plusher than cinema seating, and it is a specified acoustic component rather than a comfort decision.

### The Sabine Equation

Wallace Sabine, working at Harvard in the 1890s on a lecture room that nobody could hear in, established the first quantitative result in architectural acoustics.

The **reverberation time** $T_{60}$ is the time for the sound level to fall by $60$ dB after the source stops: a factor of a million in energy. Sabine found

$$
T_{60} = \frac{0.161\,V}{A}, \qquad A = \sum_i \alpha_i S_i,
$$

with $V$ the volume in cubic meters, $S_i$ each surface's area, and $A$ the total absorption in square meters of equivalent open window.

The equation says something simple: **bigger rooms ring longer, more absorbent rooms ring less**, and the trade is linear in both.

:::{warning}
The Sabine equation assumes a **diffuse** field, sound arriving equally from all directions and absorption spread evenly over the surfaces. It fails when a room is very absorbent (an anechoic chamber's predicted $T_{60}$ is nonsense), when absorption is concentrated on one surface, and when the room is long and thin. The Eyring and Millington refinements address the first case; nothing addresses a badly shaped room except not building it.
:::

### How Long Should a Hall Ring?

There is no single right answer, because different music wants different things.

```{figure} ../images/ch14-reverberation-targets.svg
:label: fig:ch14-reverberation-targets
:alt: Reverberation time against room volume on a logarithmic volume axis, with shaded bands for speech at 0.6 to 1.0 seconds, chamber music at 1.2 to 1.6, symphony orchestra at 1.8 to 2.2 and organ or choral music at 2.5 to 4.0, with several named halls marked.

Reverberation times for different purposes. Speech needs a short time, because syllables arriving on top of one another destroy intelligibility. Orchestral music wants around $2$ s. Organ and choral music, written for buildings with $4$ s or more, want the reverberation to be part of the texture.
```

```{audio} ch14-dry, ch14-small-room, ch14-concert-hall, ch14-cathedral
:names: Dry (anechoic), Small room, Concert hall, Cathedral
:figure: ../images/ch14-rooms.svg
:label: fig:ch14-rooms
:transcript: The same four-note phrase four times. The first is completely dry and sounds artificial and close. The second is natural but small. The third is full and spacious. The fourth blurs the notes into each other so that the last chord contains all of them.

One phrase, four rooms. Listen to the *last* note in each: in the cathedral it is still audible long after the phrase has ended, and the earlier notes are still sounding underneath it. That blurring is why music written for such buildings moves slowly and changes harmony rarely.
```

The conflict between speech and music is real and unresolvable. A hall optimized for an orchestra is poor for a lecture and vice versa, and a multi-purpose hall is a compromise that satisfies nobody completely. Section 14.5 therefore takes up variable acoustics.

## Reflection, Diffusion, and Modes

### Specular Reflection and Its Defects

A flat, hard surface reflects sound **specularly**: angle in equals angle out, like a mirror. Useful for directing sound where you want it, and the source of three classic defects.

An **echo** is a single reflection arriving late enough, more than about $80$ ms after the direct sound, so more than about $27$ m of extra path, and strongly enough to be heard separately. A flat rear wall in a long hall is the usual culprit.

**Flutter echo** is a rapid series of reflections bouncing between two parallel hard surfaces, heard as a metallic ringing after a handclap. Splaying one wall by a few degrees eliminates it entirely.

**Focusing** occurs when a concave surface, a domed ceiling, a curved rear wall, concentrates reflections at a point. The focus is much too loud and the surrounding seats are starved. Concave surfaces facing an audience are avoided for this reason, and where architecture demands one it is usually broken up or covered.

### Diffusion

The remedy for all three is **diffusion**: surfaces that scatter sound in many directions rather than reflecting it in one.

Diffusion is why historic halls sound as good as they do. The Musikverein in Vienna and the Concertgebouw in Amsterdam are covered in statuary, coffered ceilings, niches, balustrades, and moldings, all on the scale of a few tens of centimeters, comparable to the wavelengths of musical sound, and therefore excellent scatterers. The decoration was not acoustically motivated, and it turned out to be acoustically essential.

Twentieth-century halls with large smooth surfaces often disappointed for exactly this reason, and modern designs restore diffusion deliberately, sometimes using mathematically designed diffusers whose depths follow a number-theoretic sequence.

### Room Modes and Why Small Rooms Are Hard

In a large hall the sound field is dense enough to treat statistically. In a small room it is not.

A rectangular room's modes are at

$$
f_{lmn} = \frac{v}{2}\sqrt{\left(\frac{l}{L_x}\right)^2 + \left(\frac{m}{L_y}\right)^2 + \left(\frac{n}{L_z}\right)^2},
$$

and at low frequencies they are **sparse**.

```{figure} ../images/ch14-room-modes.svg
:label: fig:ch14-room-modes
:alt: Left, a spectrum of room mode frequencies below 300 Hz for a five by four by two and a half meter room, sparse at the bottom and denser above 200 Hz. Right, Schroeder frequency against room volume for three reverberation times, falling from hundreds of hertz for small rooms to tens for large ones.

Left: the modes of a small room, individually resolvable below about $200$ Hz. Right: the **Schroeder frequency**, above which modes overlap enough that the room behaves statistically. For a living room it is a few hundred hertz; for a concert hall it is around $20$ Hz. Halls can therefore be analyzed statistically; bedrooms cannot.
```

Below the Schroeder frequency the room's response is a sparse set of peaks and nulls that does not average out. Bass notes at a modal frequency boom; bass notes between modes disappear. Moving your head changes the bass. This is the fundamental difficulty of small-room acoustics, and a studio control room costs more to treat than a concert hall costs per cubic meter for just that reason.

## What Makes a Hall Sound Good

### Beyond Reverberation Time

By the mid-twentieth century $T_{60}$ was well understood, and halls were being built with correct reverberation times that musicians disliked. Something was missing.

What was missing was that $T_{60}$ is a single number describing an average over the whole room and the whole decay, and listeners respond to much more: to *when* the energy arrives, from *which direction*, and at *which frequencies*.

### Clarity, Warmth, and Intimacy

Several measures now supplement $T_{60}$, and each corresponds to something a musician can name.

**Early decay time (EDT)** measures the slope of the first $10$ dB of decay rather than extrapolating from $60$. It corresponds far better to perceived reverberance, because the first $10$ dB is what a listener actually hears before the next note arrives.

**Clarity** $C_{80}$ is the ratio, in decibels, of energy arriving in the first $80$ ms to everything after:

$$
C_{80} = 10\log_{10}\frac{\int_0^{80\,\text{ms}} p^2\,\mathrm{d}t}{\int_{80\,\text{ms}}^{\infty} p^2\,\mathrm{d}t}.
$$

High $C_{80}$ means detail and articulation; low means blend and wash. Around $0$ dB suits orchestral music; higher suits opera, where words matter.

**Warmth** (bass ratio) compares reverberation time at low frequencies to that at mid frequencies. A hall whose bass rings longer sounds warm; one whose bass dies first sounds thin. Since [Chapter 14](#ch-room-acoustics)'s absorption figure showed that soft materials absorb bass *worst*, warmth is usually easy to obtain and thinness usually means too much paneling.

**Intimacy** is the delay between the direct sound and the first reflection. A short delay makes a large hall feel small, and it is the reason side walls close to the audience matter.

### Lateral Energy and Spatial Impression

The most important discovery of twentieth-century hall acoustics is that **the direction the early reflections come from matters more than their strength**.

Reflections arriving from the **sides** make the sound seem to come from a broad source and make the listener feel surrounded. Reflections from the **ceiling** do not, because they reach both ears nearly identically.

The reason is binaural: a lateral reflection reaches the two ears at different times and levels, and that difference is what produces the impression of spaciousness. A ceiling reflection is symmetric and the auditory system simply folds it into the direct sound.

The measure is the **lateral fraction**, the proportion of early energy arriving from the sides, and it correlates with subjective preference better than almost anything else.

This single result explains the enduring success of the **shoebox** hall. A narrow rectangular room puts every listener close to a side wall; a wide fan-shaped one does not.

## Halls in Practice

### Shoebox, Fan, and Vineyard

```{figure} ../images/ch14-hall-plans.svg
:label: fig:ch14-hall-plans
:alt: Three schematic hall plans. A narrow rectangular shoebox with arrows showing reflections from the side walls reaching a listener; a fan-shaped hall with arrows showing reflections from splayed walls passing behind the listener; and a circular vineyard hall with terraced blocks acting as local side walls.

Three plans. The question in each case is where the early side reflections go.
```

The **shoebox**, Vienna's Musikverein (1870), Amsterdam's Concertgebouw (1888), Boston Symphony Hall (1900), is narrow, high, rectangular, and heavily decorated. It is consistently at the top of every ranking of concert halls, and the reasons are now understood: narrow width gives strong lateral reflections, high ceilings give volume without width, and the decoration diffuses.

Its disadvantage is capacity. A shoebox cannot be widened without losing what makes it work, so seats must go into balconies, and the hall becomes tall and expensive.

The **fan** shape spread in the twentieth century because it seats more people closer to the stage. Acoustically it is usually worse: splayed side walls reflect sound toward the *back* of the hall rather than across it, so the lateral fraction is low and the sound is clear but flat.

The **vineyard**, introduced at the Berlin Philharmonie (1963), surrounds the orchestra with terraced blocks of seating. The retaining walls of each terrace act as local side walls for the block behind, providing lateral reflections that a single large volume could not. It also allows large capacity with everyone close to the stage.

### Famous Successes and Famous Failures

The literature's standard cautionary tale is the original Philharmonic Hall at New York's Lincoln Center (1962), which was widely judged a failure on opening, thin bass and poor blend, and was rebuilt more than once, eventually being gutted entirely.

The useful lesson is not that its designers were careless; they were not. It is that the quantities known to matter in 1962 were fewer than the quantities that do matter, and that a hall is a single very expensive experiment that cannot be run twice. Much of what is now known about lateral energy was learned from halls that had already been built.

### Variable Acoustics and Electronic Enhancement

Since no fixed acoustic suits everything, modern halls increasingly vary theirs.

**Mechanically**: retractable curtains and banners over wall and ceiling absorbers; adjustable reverberation chambers, which are volumes coupled to the main hall through openings that can be closed; movable ceiling reflectors above the stage.

**Electronically**: a system of microphones, processors, and many distributed loudspeakers that adds reverberant energy. Modern systems are good enough that listeners cannot reliably detect them, and they can turn a dry drama theater into a plausible concert hall at the press of a button.

Electronic enhancement remains controversial, and the argument is worth stating honestly. The objection is not that it does not work, it does, but that a hall's acoustic has been part of the compositional and performing tradition, and that a variable acoustic makes it a production decision rather than a fact about the building. That is an aesthetic disagreement rather than a physical one, and this book takes no side in it.

## Summary

- **Most of what a listener hears has reflected.** The room is part of the instrument, and beyond the **critical distance** $r_c \approx 0.057\sqrt{V/T_{60}}$ the reverberant field dominates and the inverse-square law fails.
- **Three parts of the arrival**: the **direct sound** locates the source; **early reflections** within about $80$ ms fuse with it and add loudness and fullness (the Haas effect); the **reverberant tail** gives the sense of space.
- **The echogram is the room's impulse response**, and convolving a dry signal with it reproduces what that seat would hear, which is how convolution reverb works.
- **The absorption coefficient** is frequency-dependent: soft materials absorb treble far better than bass. **The audience is the most absorbent element**, so seats are designed to absorb like occupied ones.
- **The Sabine equation** $T_{60} = 0.161V/A$ gives reverberation time from volume and total absorption. It assumes a diffuse field and fails for very absorbent, awkwardly shaped, or unevenly treated rooms.
- **Target reverberation times** run from $0.6$–$1.0$ s for speech through $1.8$–$2.2$ s for orchestral music to $4$ s and beyond for organ and choral music.
- **Specular reflection produces echo, flutter, and focusing**; diffusion cures all three, and is why heavily decorated historic halls sound good.
- **Below the Schroeder frequency, room modes are individually audible.** This is the fundamental difficulty of small rooms and is why bass is position-dependent in a living room and not in a hall.
- **$T_{60}$ is not enough.** Early decay time, clarity $C_{80}$, warmth, and intimacy each correspond to something musicians can name.
- **Lateral energy is the key discovery**: early reflections from the *sides* produce spaciousness because they reach the two ears differently, while ceiling reflections do not. Narrow shoebox halls outperform wide fan-shaped ones for that reason.

## Conceptual Questions

1. Explain why a listener in the back row of a large hall hears a sound only a little quieter than one in row ten, but appreciably less clear.

2. Explain why a reflection arriving $30$ ms after the direct sound is not heard as an echo, while one arriving $150$ ms later is.

3. A hall sounds very different when empty and when full. Explain why, and say what hall designers do about it.

4. Explain why a room treated only with thin carpet and curtains tends to sound boomy.

5. A handclap in a corridor produces a metallic ringing. Name the defect, explain its cause, and give a cure.

6. Explain why room modes are a serious problem in a living room and not in a concert hall.

7. Explain why an early reflection from a side wall contributes more to a sense of spaciousness than an equally strong one from the ceiling.

8. Explain why fan-shaped halls seat more people and generally sound worse than shoebox halls.

## Problems

:::{exercise}
:label: ex-room-acoustics-1

A hall has a volume of $18{,}000$ m³ and a total absorption of $1450$ m². (a) Find its reverberation time. (b) Is this suitable for orchestral music?
:::

:::{solution} ex-room-acoustics-1
:label: sol-room-acoustics-1
:class: dropdown

(a) Using the Sabine equation:

$$
T_{60} = \frac{0.161 V}{A} = \frac{0.161(18000)}{1450} = 2.00\ \text{s}.
$$

(b) Yes. Two seconds sits squarely in the $1.8$–$2.2$ s band that orchestral music wants, as {numref}`Figure %s <fig:ch14-reverberation-targets>` shows.
:::

:::{exercise}
:label: ex-room-acoustics-2

A rectangular hall is $40$ m by $22$ m by $16$ m. Its surfaces have an average absorption coefficient of $0.15$. (a) Find the volume. (b) Find the total surface area. (c) Find the reverberation time.
:::

:::{solution} ex-room-acoustics-2
:label: sol-room-acoustics-2
:class: dropdown

(a) $V = 40 \times 22 \times 16 = 1.41\times10^{4}$ m³.

(b) Two of each pair of faces:

$$
S = 2(40\times22) + 2(40\times16) + 2(22\times16) = 1760 + 1280 + 704 = 3744\ \text{m}^2.
$$

(c) $A = \alpha S = 0.15(3744) = 562$ m², so

$$
T_{60} = \frac{0.161(14080)}{562} = 4.03\ \text{s}.
$$

Therefore about $4$ s, far too long for orchestral music. The hall would need its absorption roughly doubled, which is what an audience and upholstered seating provide.
:::

:::{exercise}
:label: ex-room-acoustics-3

The hall of [](#ex-room-acoustics-2) is fitted with $1200$ seats, each with an absorption of $0.45$ m² when empty and $0.85$ m² when occupied. (a) Find $T_{60}$ empty. (b) Find $T_{60}$ full. (c) Comment on rehearsing there.
:::

:::{solution} ex-room-acoustics-3
:label: sol-room-acoustics-3
:class: dropdown

(a) Empty: $A = 562 + 1200(0.45) = 562 + 540 = 1102$ m²:

$$
T_{60} = \frac{0.161(14080)}{1102} = 2.06\ \text{s}.
$$

(b) Full: $A = 562 + 1200(0.85) = 562 + 1020 = 1582$ m²:

$$
T_{60} = \frac{0.161(14080)}{1582} = 1.43\ \text{s}.
$$

(c) The hall is $0.6$ s longer empty: a difference every musician would notice. An orchestra rehearsing in the empty hall hears more reverberation than the audience will, so it will tend to play with less sustain and less blend than the concert requires, and balances set in rehearsal will be wrong.

This is exactly why hall designers specify seats whose empty absorption is close to their occupied absorption. Here the ratio is $0.45$ to $0.85$, which is poor; a well-designed seat would be nearer $0.75$ to $0.85$.
:::

:::{exercise}
:label: ex-room-acoustics-4

A hall has $V = 25{,}000$ m³ and $T_{60} = 2.2$ s. (a) Find the critical distance. (b) A listener moves from $8$ m to $32$ m from the stage. How much does the level drop, and how much would it drop outdoors?
:::

:::{solution} ex-room-acoustics-4
:label: sol-room-acoustics-4
:class: dropdown

(a)

$$
r_c = 0.057\sqrt{\frac{25000}{2.2}} = 0.057\sqrt{11364} = 6.1\ \text{m}.
$$

(b) Both positions are beyond the critical distance, so both are in the reverberant field, where the level is essentially uniform. The drop is small: a couple of decibels at most.

Outdoors, the inverse-square law gives

$$
20\log_{10}\!\left(\frac{32}{8}\right) = 12\ \text{dB}.
$$

Therefore the room saves the distant listener about $10$ dB, which is most of the reason a two-thousand-seat hall works without amplification.
:::

:::{exercise}
:label: ex-room-acoustics-5

A reflection travels a path $19$ m longer than the direct sound. (a) What is the delay? (b) Is it heard as an echo or fused with the direct sound? (c) What path difference would make it an echo?
:::

:::{solution} ex-room-acoustics-5
:label: sol-room-acoustics-5
:class: dropdown

(a) $t = 19/343 = 0.055$ s $= 55$ ms.

(b) Fused. Anything within about $80$ ms is integrated with the direct sound by the Haas effect, and contributes loudness rather than being heard separately.

(c) The threshold is about $80$ ms, so

$$
d = vt = 343(0.080) = 27\ \text{m}
$$

of extra path. In a hall $40$ m long, a listener near the front and a hard rear wall can easily produce this, so rear walls are treated.
:::

:::{exercise}
:label: ex-room-acoustics-6

A room is $6.0$ m by $4.5$ m by $2.8$ m. (a) Find the three lowest axial modes. (b) Find the Schroeder frequency if $T_{60} = 0.5$ s. (c) Comment on bass reproduction.
:::

:::{solution} ex-room-acoustics-6
:label: sol-room-acoustics-6
:class: dropdown

(a) Axial modes are at $f = v/2L$ along each dimension:

$$
\frac{343}{2(6.0)} = 28.6\ \text{Hz},
\quad \frac{343}{2(4.5)} = 38.1\ \text{Hz},
\quad \frac{343}{2(2.8)} = 61.3\ \text{Hz}.
$$

(b) $V = 6.0 \times 4.5 \times 2.8 = 75.6$ m³:

$$
f_S = 2000\sqrt{\frac{0.5}{75.6}} = 2000(0.0813) = 163\ \text{Hz}.
$$

(c) Below $163$ Hz the modes are individually resolvable, and the three lowest are widely separated at $29$, $38$, and $61$ Hz. A bass note landing on a mode will boom; one landing between modes will nearly disappear; and both effects depend on where the listener sits.

Therefore bass in this room is position-dependent and uneven over the whole of the lowest two octaves of music, which is the normal state of domestic listening, and the reason studio control rooms need extensive low-frequency treatment.
:::

:::{exercise}
:label: ex-room-acoustics-7

A lecture room of $600$ m³ has $T_{60} = 1.8$ s and is unintelligible. (a) How much absorption does it currently have? (b) How much is needed for $T_{60} = 0.8$ s? (c) If acoustic panels have $\alpha = 0.85$, what area is needed?
:::

:::{solution} ex-room-acoustics-7
:label: sol-room-acoustics-7
:class: dropdown

(a) From $A = 0.161V/T_{60}$:

$$
A = \frac{0.161(600)}{1.8} = 53.7\ \text{m}^2.
$$

(b) For $0.8$ s:

$$
A = \frac{0.161(600)}{0.8} = 120.8\ \text{m}^2.
$$

(c) The extra absorption needed is $120.8 - 53.7 = 67.1$ m². Panels of $\alpha = 0.85$ provide $0.85$ m² of absorption per square meter, but they also cover an existing surface. Taking the existing wall as roughly $\alpha = 0.05$, each square meter of panel adds a net $0.80$ m²:

$$
\text{area} = \frac{67.1}{0.80} = 84\ \text{m}^2.
$$

Therefore about $84$ m² of paneling: a substantial fraction of the room's surface, and the reason retrofitting a bad lecture room is expensive. This is essentially the problem Sabine was hired to solve.
:::

:::{exercise}
:label: ex-room-acoustics-8

A hall has $T_{60} = 2.4$ s at $125$ Hz and $1.9$ s at $1$ kHz. (a) Find the bass ratio. (b) Is the hall warm or thin? (c) What would raise the bass ratio?
:::

:::{solution} ex-room-acoustics-8
:label: sol-room-acoustics-8
:class: dropdown

(a) The bass ratio is the low-frequency reverberation time divided by the mid:

$$
\frac{2.4}{1.9} = 1.26.
$$

(b) **Warm.** A bass ratio above about $1.1$–$1.2$ is the usual criterion for warmth, and this hall exceeds it.

(c) Anything that absorbs more mid and high frequency or less bass. In practice the lever is usually the other way round: to *lower* a bass ratio you add bass traps, since [Chapter 14](#ch-room-acoustics)'s absorption figure shows that ordinary soft furnishing absorbs bass poorly. To raise it further one would reduce thin paneling, which acts as a low-frequency absorber by flexing, and use massive rigid surfaces instead, which is what the stone and plaster of historic halls provide.
:::

:::{exercise}
:label: ex-room-acoustics-9

Explain quantitatively why a listener $30$ m from an orchestra hears mostly reflected sound, in a hall with $V = 20{,}000$ m³ and $T_{60} = 2.0$ s.
:::

:::{solution} ex-room-acoustics-9
:label: sol-room-acoustics-9
:class: dropdown

The critical distance is

$$
r_c = 0.057\sqrt{\frac{20000}{2.0}} = 5.7\ \text{m}.
$$

By definition, at $r_c$ the direct and reverberant energies are equal. The reverberant energy is uniform throughout the room, while the direct energy falls as $1/r^2$. So at $30$ m the direct sound has fallen relative to its value at $r_c$ by

$$
\left(\frac{5.7}{30}\right)^2 = 0.036,
$$

while the reverberant energy is unchanged.

Therefore the direct sound is only about $3.6\%$ of the total: the listener is receiving roughly $96\%$ reflected energy. In decibels the direct sound is $10\log_{10}(0.036) = -14$ dB relative to the reverberant field.

This is the quantitative form of the chapter's opening claim, and it is why the room matters as much as the orchestra.
:::

:::{exercise}
:label: ex-room-acoustics-10

A hall's impulse response has $2.4$ units of energy in the first $80$ ms and $3.1$ units afterwards. (a) Find $C_{80}$. (b) Is this hall better suited to symphonic music or to opera? (c) What change would raise $C_{80}$?
:::

:::{solution} ex-room-acoustics-10
:label: sol-room-acoustics-10
:class: dropdown

(a)

$$
C_{80} = 10\log_{10}\!\left(\frac{2.4}{3.1}\right) = 10\log_{10}(0.774) = -1.1\ \text{dB}.
$$

(b) **Symphonic music.** A slightly negative $C_{80}$ means the late energy slightly exceeds the early, which gives blend and fullness at some cost in articulation, good for orchestral texture. Opera wants words to be intelligible and is usually happier with $C_{80}$ around $+1$ to $+4$ dB.

(c) Raising $C_{80}$ means shifting energy earlier. In practice: reflectors placed to return sound to the audience quickly, a lower ceiling over the stage, and more absorption on distant surfaces to shorten the tail. Reducing the overall volume does both at once.
:::

:::{exercise}
:label: ex-room-acoustics-11

Derive the Sabine equation's form, given that sound energy in a room decays exponentially with the mean time between reflections and the fraction absorbed at each.
:::

:::{solution} ex-room-acoustics-11
:label: sol-room-acoustics-11
:class: dropdown

In a diffuse field, the mean free path between reflections is $4V/S$, where $S$ is the total surface area. The mean time between reflections is therefore

$$
\tau = \frac{4V}{Sv}.
$$

At each reflection a fraction $\bar\alpha$ of the energy is absorbed, so after $n$ reflections the energy is $E_0(1-\bar\alpha)^n$. Writing $n = t/\tau$:

$$
E(t) = E_0\,(1-\bar\alpha)^{\,t/\tau} = E_0\exp\!\left(\frac{t}{\tau}\ln(1-\bar\alpha)\right).
$$

For small $\bar\alpha$, $\ln(1-\bar\alpha) \approx -\bar\alpha$, so

$$
E(t) = E_0\exp\!\left(-\frac{\bar\alpha S v\,t}{4V}\right).
$$

Set $E/E_0 = 10^{-6}$, which is $-60$ dB:

$$
\frac{\bar\alpha S v\,T_{60}}{4V} = \ln(10^6) = 13.82,
$$
$$
T_{60} = \frac{55.3\,V}{v\,\bar\alpha S} = \frac{55.3\,V}{343\,A} = \frac{0.161\,V}{A}.
$$

Therefore the constant $0.161$ is $55.3/343$, it contains the speed of sound, and would differ in another medium or at another temperature. Note also where the small-$\bar\alpha$ approximation entered: it is exactly why the equation fails for very absorbent rooms, and the Eyring correction is what you get by keeping $\ln(1-\bar\alpha)$ intact.
:::

:::{exercise}
:label: ex-room-acoustics-12

Two halls have identical $T_{60}$ of $2.0$ s. One is a $22$ m wide shoebox and the other a $42$ m wide fan. (a) Estimate the delay of the first side-wall reflection for a listener on the center line, $20$ m from the stage, in each. (b) Which sounds more spacious, and why?
:::

:::{solution} ex-room-acoustics-12
:label: sol-room-acoustics-12
:class: dropdown

(a) Take the source on the center line at the stage and the listener $20$ m back. For a wall at distance $w/2$ from the center line, the reflected path is approximately

$$
2\sqrt{\left(\frac{w}{2}\right)^2 + \left(\frac{20}{2}\right)^2}.
$$

Shoebox, $w = 22$ m: path $= 2\sqrt{11^2 + 10^2} = 2(14.87) = 29.7$ m, against $20$ m direct: an extra $9.7$ m, so a delay of $28$ ms.

Fan, $w = 42$ m: path $= 2\sqrt{21^2 + 10^2} = 2(23.26) = 46.5$ m: an extra $26.5$ m, so a delay of $77$ ms.

(b) The **shoebox**. Its side reflections arrive at $28$ ms, comfortably inside the fusion window, strongly, and from the sides, exactly the lateral energy that produces spatial impression. The fan's arrive at $77$ ms, at the very edge of the window, much weaker for having traveled further, and from a shallower angle that is closer to frontal than lateral.

Therefore the same reverberation time can produce very different halls, which is the whole point of §14.4 and the reason $T_{60}$ alone was never enough.
:::

:::{exercise}
:label: ex-room-acoustics-13

A recording engineer wants to place an instrument in a virtual hall using convolution reverb. (a) What must they measure in the real hall? (b) What operation do they perform? (c) What does this assume about the room?
:::

:::{solution} ex-room-acoustics-13
:label: sol-room-acoustics-13
:class: dropdown

(a) The **impulse response** of the hall, from the source position to the listening position, in practice measured with a swept sine or a starter pistol and a microphone, then processed to recover the response.

(b) **Convolution** of the dry recording with the impulse response. Every sample of the dry signal is replaced by a scaled copy of the whole impulse response, and the copies are summed.

(c) That the room is **linear** and **time-invariant**. Linear means superposition holds ([Chapter 3](#ch-superposition)), so the response to a sum of sounds is the sum of the responses, true for any room at musical levels. Time-invariant means the room does not change during the recording, which fails if the audience arrives, the temperature drifts, or a door opens.

It also assumes the source and listener stay where they were when the response was measured, so a moving source in a convolution reverb never sounds quite right.
:::

:::{exercise}
:label: ex-room-acoustics-14

A multi-purpose hall must serve both speech ($T_{60} = 0.9$ s) and orchestral music ($T_{60} = 2.0$ s). Its volume is $12{,}000$ m³. (a) What absorption does each require? (b) How much absorption must be removable? (c) Suggest two mechanisms.
:::

:::{solution} ex-room-acoustics-14
:label: sol-room-acoustics-14
:class: dropdown

(a) For speech:

$$
A = \frac{0.161(12000)}{0.9} = 2147\ \text{m}^2.
$$

For music:

$$
A = \frac{0.161(12000)}{2.0} = 966\ \text{m}^2.
$$

(b) The difference is $2147 - 966 = 1181$ m² of absorption that must be introduced for speech and removed for music, more than the entire absorption required in the music configuration.

(c) Two mechanisms:

- **Retractable absorbers**: heavy velour banners on motorized rollers, deployed over wall and ceiling surfaces. Roughly $1400$ m² of banner at $\alpha \approx 0.85$ would do it, which is a great deal of fabric and storage volume.
- **Coupled reverberation chambers**: volumes adjoining the hall, connected through motorized doors. Opening them increases the effective volume and the reverberation; closing them shortens it. This is the more elegant solution, since it changes $V$ rather than $A$, and it is used in several modern halls.

Therefore the required change is large, and a hall that does both well is a genuinely difficult and expensive building. Most venues therefore choose one purpose and accept being mediocre at the other.
:::
