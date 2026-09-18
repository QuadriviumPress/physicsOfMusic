---
title: Glossary
short_title: Glossary
label: glossary
---

Terms are defined here as this book uses them. Where a word is used differently
elsewhere, *overtone* and *partial* are the notorious pair, the entry says so.

Abbreviations that are merely expansions (sound pressure level, fast Fourier
transform, ADSR, and the rest) are not repeated here; they are expanded on
hover throughout the text.

:::{glossary}
absorption coefficient
: The fraction of the sound energy striking a surface that is not reflected
  back into the room. Runs from 0 (a perfect mirror) to 1 (an open window), and
  depends strongly on frequency. See §14.2.

acoustic impedance
: The ratio of acoustic pressure to volume flow at a point: a measure of how
  hard it is to push a medium into motion. Sound crosses a boundary efficiently
  only when the impedances on either side are similar, which is why a bare
  string radiates almost nothing and why the middle ear exists. See §2.4, §6.2.

aliasing
: The appearance of a frequency above the {term}`Nyquist frequency` as a
  spurious lower one, after sampling. Prevented by filtering before the
  converter, not after. See §15.3.

antinode
: A point of maximum motion in a standing wave. See {term}`node`.

attack
: The initial rise of a note, from silence to its full amplitude. Along with the
  rest of the {term}`envelope`, it carries much of an instrument's identity,
  more, for many instruments, than the steady-state spectrum. See §5.4.

basilar membrane
: The membrane running the length of the {term}`cochlea` whose stiffness and
  width vary along it, so that different frequencies produce maximum motion at
  different places. See §6.3.

beat
: The slow rise and fall in loudness heard when two tones of nearly equal
  frequency sound together, at a rate equal to the difference between their
  frequencies. See §8.2.

cent
: One hundredth of an equal-tempered semitone; $1200$ cents to the octave. The
  natural unit for comparing tunings, because it is logarithmic and so the same
  size at every pitch. See §9.1.

Chladni pattern
: The figure formed when sand on a vibrating plate collects along the nodal
  lines of the mode being excited. See §12.4.

cochlea
: The coiled, fluid-filled organ of the inner ear in which mechanical vibration
  is separated by frequency and converted into neural signals. See §6.3.

comma
: A small interval left over when a chain of pure intervals fails to close. The
  **Pythagorean comma** (about 23.5 cents) is the amount by which twelve pure
  fifths exceed seven octaves; the **syntonic comma** (about 21.5 cents) is the
  difference between four pure fifths and a pure major third plus two octaves.
  Every tuning system is a decision about where to put one. See §9.2, §9.3.

critical band
: The range of frequencies within which two tones interact, masking each other,
  and producing {term}`roughness`. Roughly a third of an octave over most of the
  audible range. See §7.5, §8.4.

critical distance
: The distance from a source, in an enclosed room, beyond which the
  reverberant field is stronger than the direct sound and the inverse-square
  law no longer describes how the level falls off. See §2.4, §14.1.

decibel
: Ten times the base-ten logarithm of a power ratio, or twenty times the
  logarithm of a pressure ratio. A ratio, not a level, until a reference is
  stated: **dB SPL** is referred to 20 μPa. See §7.2.

end correction
: The extra effective length, roughly $0.6r$ per open end, that must be added
  to a pipe's physical length because the pressure antinode falls slightly
  outside the opening rather than exactly at it. Matters most for pipes that
  are short and wide. See §3.5, §11.2.

envelope
: The outline of a note's amplitude over time, conventionally divided into
  attack, decay, sustain, and release. See §5.4.

equal temperament
: The tuning in which the octave is divided into twelve equal steps, each in the
  frequency ratio $2^{1/12}$. Every interval except the octave is slightly
  mistuned, and every key is mistuned identically. See §9.5.

formant
: A resonance of a fixed cavity, most importantly the vocal tract, that
  emphasizes whatever harmonics fall near it. Formants stay put as the
  fundamental moves, which is why a vowel is recognizable across a singer's
  range. See §5.5, §13.3.

fundamental
: The lowest frequency present in a harmonic sound, and the one whose period is
  the period of the whole waveform. Usually, but not always, the perceived
  pitch; see {term}`missing fundamental`.

harmonic
: A partial whose frequency is an exact integer multiple of the fundamental. All
  harmonics are {term}`partial`s; not all partials are harmonics. See §5.2.

Helmholtz motion
: The motion of a bowed string, in which a single kink travels around a
  two-part envelope, sticking to the bow on the way out and slipping back on the
  way in. See §10.2.

Helmholtz resonator
: A cavity with a narrow opening, resonating at a single low frequency set by
  the cavity volume and the neck dimensions. The air resonance of a guitar body
  and of a bottle blown across the top. See §4.5.

inharmonicity
: The departure of a vibrator's partials from exact integer ratios. In piano
  strings it arises from stiffness, and it is the reason piano tuning is
  stretched. See §5.5, §10.6.

just intonation
: A tuning in which the intervals of the scale are exact small-integer frequency
  ratios. Maximally smooth in one key and unusable in the others. See §9.3.

masking
: The raising of the threshold of audibility for one sound by the presence of
  another, strongest when the two lie within a {term}`critical band`. The
  mechanism perceptual audio codecs exploit. See §7.5, §15.4.

missing fundamental
: The pitch heard at the fundamental frequency of a harmonic series when that
  frequency is not physically present. Evidence that pitch is inferred from the
  pattern of partials rather than read off a single place. See §8.3.

mode
: One of the specific patterns in which a system can vibrate at a single
  frequency, with a fixed shape. See {term}`normal mode`.

node
: A point of zero motion in a standing wave. See {term}`antinode`.

normal mode
: A pattern of vibration in which every part of a system oscillates at the same
  frequency with a fixed relative amplitude and phase. A system with $N$ degrees
  of freedom has $N$ of them, and any motion is a sum of them. See §4.4.

Nyquist frequency
: Half the sampling rate: the highest frequency a digitally sampled signal can
  represent. Anything above it is {term}`aliasing`. See §15.3.

overtone
: Any partial above the fundamental. The numbering is off by one from the
  harmonic numbering, the first overtone is the second harmonic, which is
  precisely why this book avoids the word except when quoting. See §5.2.

partial
: Any single frequency component of a complex tone, whether or not it is an
  integer multiple of the fundamental. See §5.2.

phon
: The unit of loudness *level*: a sound has a loudness level of $N$ phons if it
  is judged as loud as a 1 kHz tone at $N$ dB SPL. Equal-loudness contours are
  lines of constant phon. See §7.4.

pitch
: The perceptual attribute by which sounds are ordered from low to high. Closely
  related to frequency, but not identical to it. See §8.1.

quality factor
: A dimensionless measure of how sharp a resonance is, equal to the resonant
  frequency divided by the bandwidth between the half-power points. High $Q$
  means selective and long-ringing; low $Q$ means even and quick-responding.
  See §4.3.

reverberation time
: The time for the sound level in a room to fall by 60 dB after the source
  stops, written $T_{60}$. Estimated by the Sabine equation from the room's
  volume and total absorption. See §14.2.

roughness
: The harsh, beating sensation produced when two partials lie close enough to
  fall within one {term}`critical band` but far enough apart not to be heard as
  slow beats. The principal physical correlate of dissonance. See §8.4.

Sabine equation
: $T_{60} = 0.161\,V/A$ in SI units, relating reverberation time to room volume
  $V$ and total absorption $A$. Valid for a diffuse field in a room that is not
  too absorbent. See §14.2.

Schroeder frequency
: The frequency above which a room's modes overlap densely enough for its
  response to be treated statistically rather than as individually
  resolvable peaks. Below it, bass response is sparse and depends strongly on
  position in the room. See §14.3.

simple harmonic motion
: Motion under a restoring force proportional to displacement, producing a
  sinusoid whose frequency does not depend on amplitude. See §1.3.

singer's formant
: A strong resonance near 3 kHz, produced by clustering the third, fourth, and
  fifth vocal-tract formants, that lets a trained soloist be heard over an
  orchestra without amplification. See §13.5.

sone
: The unit of loudness itself, defined so that doubling the number of sones
  means a sound twice as loud. One sone is 40 phons, and each further 10 phons
  roughly doubles the sone value. See §7.5.

source–filter model
: The description of an instrument as a vibrating source whose spectrum is
  subsequently shaped by a resonator that is independent of it. The standard
  account of the voice, and the basis of subtractive synthesis. See §13.1,
  §15.5.

spectral centroid
: The amplitude-weighted average frequency of a sound's partials. Correlates
  well with the perceived brightness of a tone, and is the single number most
  often used when a machine has to judge what a sound is like. See §5.3.

spectrogram
: A display of spectrum against time, with intensity shown as brightness or
  color. The natural picture of a sound that changes. See §5.4.

spectrum
: The list of frequency components present in a sound, with their amplitudes.
  Drawn as a line spectrum for a periodic tone, since only harmonics are
  present. See §5.2.

standing wave
: The stationary pattern of nodes and antinodes formed when two identical waves
  travel through each other in opposite directions. The reason an instrument has
  a definite pitch. See §3.3.

stretched tuning
: The practice of tuning a piano's upper register slightly sharp and its lower
  register slightly flat, so that octaves match the {term}`inharmonicity` of the
  strings rather than an exact 2:1 ratio. See §10.6.

timbre
: The perceptual attribute by which two sounds of the same pitch, loudness, and
  duration are distinguished. Determined by the {term}`spectrum` and the
  {term}`envelope` together. See §5.3.

wolf fifth
: The badly out-of-tune fifth left over in a tuning system where the comma has
  been pushed into one interval rather than distributed. By extension, the
  **wolf note** of a cello or violin: a note at which a strong body resonance
  fights the string. See §9.3, §10.5.
:::
