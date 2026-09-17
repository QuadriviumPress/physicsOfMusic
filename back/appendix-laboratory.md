---
title: Laboratory Exercises
short_title: Laboratory
label: appendix-laboratory
---

The claims this book makes about spectra, air columns, beats, and reverberation
are all measurable, most of them in an afternoon, several of them with a
telephone. This appendix is a set of ten exercises that take the book's
assertions and check them.

They are written to be run with whatever is available. Where a laboratory has an
oscilloscope and a function generator, use them: reading a waveform off a
calibrated screen builds an intuition that a software display does not. Where it
does not, every exercise here has a software path, and the software is free.

## Equipment

**The short list.** A laptop, a pair of headphones, and a phone will do all ten
exercises at reduced precision.

| Item | Laboratory version | Substitute |
|---|---|---|
| Signal source | Function generator | A tone-generator app, or an online tone generator |
| Waveform display | Oscilloscope | [Audacity](https://www.audacityteam.org/) or [Sonic Visualiser](https://www.sonicvisualiser.org/), recording from the microphone |
| Spectrum analyzer | Dedicated analyzer, or a scope with `FFT` | Audacity's *Analyze > Plot Spectrum*; Sonic Visualiser's spectrogram |
| Sound level meter | Calibrated Type 2 meter | A phone `SPL` app, **uncalibrated**, so use it for *differences*, never absolute levels |
| Microphone | Measurement microphone | The laptop's built-in microphone |
| Miscellaneous | Meter rule, thermometer, tuning fork, a length of string, a set of masses, a pulley, a long tube or a graduated cylinder |, |

**One warning about phone apps.** A phone microphone rolls off sharply below
about 100 Hz and its automatic gain control fights you. Turn off any
noise-suppression or "voice enhancement" setting before recording, and never
trust a phone for an absolute sound level.

:::{warning}
Several of these exercises involve sustained tones through headphones. Set the
level **before** you put them on, keep it at a comfortable conversational
loudness, and do not use a tone to test "how loud you can stand". Chapter 6
explains why hearing damage is cumulative and permanent; this is a course where
the equipment includes your ears.
:::

## How to Write These Up

Each exercise ends with an analysis section. A complete write-up has four parts,
and the third is the one most often skipped:

1. **What you measured**: the raw numbers, with units, in a table.
2. **What you calculated**: the derived quantity, with the formula used.
3. **How well it agrees**: the percentage difference from the prediction, *and
   an estimate of your own uncertainty*. "Within 3%" means nothing until you say
   whether your measurement was good to 1% or to 10%.
4. **What the discrepancy means**, either the prediction is confirmed within
   uncertainty, or something is unaccounted for. Say which, and if the latter,
   name a candidate.



## B.1 The Oscilloscope and the Function Generator

**Supports** Chapters 1–2. **Time** 60–90 minutes.

The point of the first exercise is not to discover anything. It is to learn to
read the two instruments the rest of the exercises depend on, and to connect
what you see on a screen to what you hear.

### Procedure

1. Set the function generator to a 440 Hz sine wave and display it on the
   oscilloscope. Adjust the time base until two or three full cycles fill the
   screen.
2. Measure the period directly from the screen. Calculate the frequency and
   compare with the generator's setting.
3. Double the frequency to 880 Hz. Predict what happens to the trace before you
   press the button, then check.
4. Return to 440 Hz and halve the amplitude. Record what changes on the screen
   and what changes in what you hear.
5. Switch the generator to square, triangle, and sawtooth at the same 440 Hz.
   Sketch each waveform and describe in one sentence how each sounds compared
   with the sine.
6. Sing or play a sustained note into a microphone and display it. Identify the
   period on the screen and calculate the frequency.

### Analysis

- From your measured period in step 2, what is your frequency and its
  uncertainty? Which is the limiting factor: the resolution of the time base, or
  your ability to judge where a cycle begins?
- Rank the four waveforms of step 5 from dullest to brightest. Chapter 5 will
  explain the ranking; record the order now, before you know the answer.
- The trace in step 6 is not a clean sinusoid. List two things visible in it
  that are not visible in the generator's sine.



## B.2 The Speed of Sound

**Supports** Chapter 2. **Time** 60 minutes.

### Method A, Resonance in a tube

1. Hold a vibrating tuning fork of known frequency $f$ over the open end of a
   tube whose length can be varied (a graduated cylinder being filled with water
   works well).
2. Find the shortest length $L_1$ at which the tube resonates loudly, and then
   the next length $L_2$.
3. The distance $L_2 - L_1$ is half a wavelength. Calculate $\lambda$ and then
   $v = f\lambda$.

Using the *difference* of two resonance lengths rather than the first length
alone eliminates the end correction, which is exactly what you want here and
exactly what you will measure in [B.9](#lab-b9).

### Method B, Time of flight

1. Place two microphones a measured distance apart, several meters, as far as
   your interface allows, both recording to the same file.
2. Make a sharp impulsive sound (a hand clap, two blocks struck together) beyond
   one microphone, on the line joining them.
3. Measure the delay between the two arrivals in the recording, and divide the
   separation by it.

### Analysis

- Record the air temperature. Calculate the predicted speed of sound and compare.
- Which method gave the smaller uncertainty, and why?
- Method B is sensitive to where you stand. Explain why standing off the line
  joining the microphones makes the measured speed come out too high.



(lab-b3)=
## B.3 Standing Waves on a String

**Supports** Chapter 3. **Time** 90 minutes.

### Procedure

1. Stretch a string horizontally from a mechanical vibrator over a pulley to a
   hanging mass, so that the tension is $T = mg$ and the vibrating length $L$ is
   between the vibrator and the pulley.
2. Drive the string and sweep the frequency slowly upward from a few hertz.
   Record every frequency at which a clean standing-wave pattern appears, and the
   number of loops in each.
3. Repeat for at least four different hanging masses.
4. If a second string of different thickness is available, repeat step 2 for it
   at one fixed tension.

### Analysis

- For one tension, plot $f_n$ against $n$. The points should lie on a straight
  line through the origin. Do they? What is the slope, and what does it mean?
- Plot $f_1$ against $\sqrt{T}$ for your four masses. Is it linear? Extract the
  linear mass density $\mu$ from the slope and compare with the value you get by
  weighing a measured length of the string.
- The frequency at which a pattern looks *best* is not sharply defined. Estimate
  the width of the frequency range over which each resonance is visible, and use
  it to put an uncertainty on $f_n$.



## B.4 Resonance and the Quality Factor

**Supports** Chapter 4. **Time** 60 minutes.

### Procedure

1. Choose a resonator: a wine glass, a length of pipe, a guitar body, or the
   string apparatus of [B.3](#lab-b3) held at one mode.
2. Drive it with a loudspeaker fed from the function generator, and measure the
   response amplitude with a microphone as you step the frequency through the
   resonance in small increments.
3. Take at least fifteen points, closely spaced near the peak.
4. Separately, excite the resonator impulsively (tap it) and record the decay.

### Analysis

- Plot amplitude against frequency. Find the peak frequency $f_0$, and the two
  frequencies either side at which the amplitude has fallen to $1/\sqrt{2}$ of
  the peak. The difference between them is the bandwidth $\Delta f$; calculate
  $Q = f_0/\Delta f$.
- From your impulse recording, measure the time for the amplitude to fall to
  $1/e$ of its initial value. Estimate $Q$ from the decay and compare with the
  value from the response curve.
- A wine glass has a $Q$ in the hundreds; a guitar body's main resonance has a
  $Q$ of order ten. Explain, in terms of the instrument's job, why a guitar
  should not have a high-$Q$ body.



## B.5 The Spectra of Musical Instruments

**Supports** Chapter 5. **Time** 90 minutes.

This is the central exercise of the course.

### Procedure

1. Record the **same pitch**, A3 at 220 Hz is convenient, played by at least
   four sources: a sung vowel, a plucked string, a bowed or blown sustained
   tone, and a pure sine from the generator. Record several seconds of steady
   tone from each, at roughly equal loudness.
2. For each recording, select a window from the *middle* of the sustained
   portion, well clear of the attack, and compute its spectrum.
3. Record the frequency and relative amplitude of the first eight partials of
   each.
4. Now record just the **first half-second** of each note, including the attack,
   and make a spectrogram of it.

### Analysis

- Tabulate the partial amplitudes, in dB relative to the strongest partial, for
  all four sources. Which instrument has the strongest high harmonics? Does the
  ranking match the brightness you hear?
- Are the measured partial frequencies exact integer multiples of the
  fundamental? Report the deviation of the eighth partial as a percentage. Which
  source is least harmonic, and why might that be?
- From the spectrograms: describe how each note's spectrum changes during the
  first tenth of a second. Which partials arrive first?
- **The listening test.** Using an audio editor, cut the attack off each
  recording and play only the steady portions to a listener who has not seen
  which is which. How well can they identify the instruments? Relate the result
  to §5.4.



## B.6 Sound Level, Distance, and Addition

**Supports** Chapter 7. **Time** 60 minutes.

Use a sound level meter if one is available. A phone app will do, provided every
conclusion is drawn from *differences* between readings.

### Procedure

1. Outdoors, or in the largest and least reverberant space available, set up a
   loudspeaker playing steady pink noise.
2. Measure the level at 1, 2, 4, and 8 meters on the axis of the speaker.
3. Return to a fixed distance. Measure the level with one speaker, then with two
   identical speakers side by side playing the *same* noise file, then with two
   playing *different* noise files.
4. Measure the level of several ordinary sounds: a quiet room, conversation at a
   meter, a hand clap, traffic.

### Analysis

- Plot level against $\log_{10}(\text{distance})$. The slope should be
  $-20\ \text{dB}$ per decade: that is, $-6$ dB per doubling. What slope did
  you get? If it is shallower, what does that tell you about the room?
- In step 3, two speakers playing *different* noise should add to about $+3$ dB.
  What did two playing the *same* file give, and why is it different?
- Using the equal-loudness contours of §7.4, estimate the loudness level in
  phons of your measured traffic noise, and say what you had to assume about its
  spectrum to do so.



## B.7 Beats and the Just-Noticeable Difference

**Supports** Chapter 8. **Time** 45 minutes.

### Procedure

1. Sound two tones together: one fixed at 440 Hz, one variable. Sum them
   electrically if you can, or use two speakers.
2. Set the second tone to 441, 443, 446, 450, 460, and 480 Hz in turn. For each,
   record: the beat rate you count, and a one-word description of the sensation
   (*beating*, *rough*, *two separate tones*).
3. Now find your own frequency discrimination. Have a partner alternate between
   440 Hz and a slightly different frequency, and narrow the difference until you
   can no longer reliably tell which is which.
4. Repeat step 3 at 220 Hz and at 3520 Hz.

### Analysis

- Plot your counted beat rate against the frequency difference. The prediction is
  a straight line of slope 1. Up to what difference does it hold, and what
  happens beyond?
- At what frequency difference did beating give way to roughness, and roughness
  to two separate tones? Compare the second of these with the critical bandwidth
  at 440 Hz quoted in §7.5.
- Express your discrimination threshold from steps 3 and 4 as a *percentage* of
  the center frequency at each of the three frequencies. Is the percentage
  constant? What does that tell you?



## B.8 Measuring a Tuning

**Supports** Chapter 9. **Time** 90 minutes.

### Procedure

1. Choose a fixed-pitch instrument: a piano, an electronic keyboard, or a
   fretted guitar.
2. Record every note of one chromatic octave in the middle of its range, and
   measure the fundamental frequency of each to the nearest 0.1 Hz.
3. Also record notes two or three octaves apart, near the extremes of the
   instrument's range.
4. If a second instrument of a different kind is available, repeat.

### Analysis

- Convert each measured frequency to cents above the lowest note of your octave.
  Tabulate alongside the equal-tempered values (0, 100, 200, …).
- Plot the deviation in cents from equal temperament for each note. Is the
  instrument equally tempered within your measurement uncertainty?
- Compare your measured major third and perfect fifth with both the just ratios
  (5:4 and 3:2) and the equal-tempered values. Which is the instrument closer to?
- From step 3: is the instrument's octave exactly 1200 cents? If you measured a
  piano, it very likely is not. Explain the result using §10.6.

(lab-b9)=
## B.9 Air Columns and the End Correction

**Supports** Chapter 11. **Time** 60 minutes.

### Procedure

1. Take a tube open at both ends. Measure its length and inside diameter.
2. Excite it, by blowing across one end, or with a loudspeaker at one end, and
   measure the frequencies of its first three resonances.
3. Close one end and repeat.
4. Repeat the whole procedure for a tube of noticeably different diameter but
   similar length.

### Analysis

- For the open tube, are the resonances in the ratio 1: 2: 3? For the stopped
  tube, are they in the ratio 1: 3: 5? Report the measured ratios.
- Using the speed of sound at your measured temperature, calculate the
  *effective* length of each tube from its fundamental. Subtract the physical
  length to get the end correction.
- Divide your end correction by the tube radius. Compare with the theoretical
  value of about $0.6r$ per open end quoted in §11.2. Does the second tube give
  a consistent answer?
- A stopped tube of the same length sounds roughly an octave lower. Verify this
  from your measurements, and state the discrepancy.



## B.10 Reverberation Time

**Supports** Chapter 14. **Time** 60 minutes, plus access to two very different rooms.

### Procedure

1. Choose two rooms of markedly different character: a stairwell and a carpeted
   office, say. Measure the dimensions of each and estimate its volume.
2. In each, make a loud impulsive sound (a balloon burst is the classic; two
   hardwood blocks work) and record it.
3. From the recording, plot the decay of level in dB against time.
4. Repeat the measurement at three different positions in each room.

### Analysis

- Measure $T_{60}$, the time for a 60 dB decay, by fitting a straight line to
  the decay curve. In most rooms you will not get a clean 60 dB above the noise
  floor; fit over the first 20 or 30 dB and extrapolate, and say that you did.
- Use the Sabine equation with your measured $T_{60}$ and volume to find each
  room's total absorption, and then its average absorption coefficient. Is the
  value plausible for the surfaces you can see?
- Filter the recordings into octave bands and measure $T_{60}$ in each. Is the
  reverberation time the same at 125 Hz as at 4 kHz? What does the difference
  say about the room's furnishings?
- How much did your three positions disagree? Is the reverberant field as
  uniform as the Sabine model assumes?
