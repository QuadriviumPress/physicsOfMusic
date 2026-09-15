"""Shared synthesis helpers for the audio examples in *Physics of Music*.

Every clip in the book is **synthesized rather than recorded**. That is a
deliberate limitation. A synthesized clip can isolate exactly one variable --
the same pitch, the same level, differing only in which harmonics are present
-- in a way no recording of a real instrument can, and it carries no third-party
licence. Where the real thing matters, the text says so and sends the reader to
an instrument.

Each generator writes a **pair** of files:

    audio/<id>.mp3     the clip
    images/<id>.svg    its waveform and spectrum

``plugins/audio.mjs`` defaults to exactly that pair, so a single-clip
``{audio} <id>`` directive needs no options at all. Both are committed, because
the Pages build runs ``myst build --html`` and has no Python.

Regenerate everything with::

    scripts/render-audio.sh

Requires ``ffmpeg`` on the path for the MP3 encode.
"""

import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))

import figstyle  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
AUDIO = ROOT / "audio"

RATE = 44100
# Long enough to hear a timbre settle, short enough that forty of them do not
# dominate the repository.
DEFAULT_SECONDS = 3.0
# Headroom below full scale. MP3 encoding can overshoot the peak of the PCM it
# was given, and a clip that clips is a clip about distortion.
PEAK = 0.7
FADE_MS = 25.0
# Mono, and modest: these are tones, not music, and the artefacts of a low
# bitrate would be a distraction in a book that later explains them.
BITRATE = "128k"


def time_axis(seconds=DEFAULT_SECONDS, rate=RATE):
    """Sample times for a clip of the given length."""
    return np.arange(int(round(seconds * rate)), dtype=np.float64) / rate


def harmonics(t, fundamental, amplitudes, phases=None):
    """Sum a harmonic series: ``amplitudes[k]`` multiplies harmonic ``k + 1``.

    Phases default to zero, which makes a waveform whose shape is easy to read
    on the page. Section 5.3 discusses how little that choice matters to the
    ear and how much it matters to the picture.
    """
    amplitudes = np.asarray(amplitudes, dtype=np.float64)
    if phases is None:
        phases = np.zeros_like(amplitudes)
    signal = np.zeros_like(t)
    for index, (amplitude, phase) in enumerate(zip(amplitudes, phases), start=1):
        if amplitude:
            signal += amplitude * np.sin(2.0 * np.pi * index * fundamental * t + phase)
    return signal


def sine(t, frequency, amplitude=1.0, phase=0.0):
    """A pure tone."""
    return amplitude * np.sin(2.0 * np.pi * frequency * t + phase)


def sawtooth_amplitudes(n):
    """Harmonic amplitudes of an ideal sawtooth: every harmonic, falling as 1/n."""
    return 1.0 / np.arange(1, n + 1)


def square_amplitudes(n):
    """Harmonic amplitudes of an ideal square wave: odd harmonics only, falling as 1/n."""
    amplitudes = np.zeros(n)
    amplitudes[::2] = 1.0 / np.arange(1, n + 1, 2)
    return amplitudes


def triangle_amplitudes(n):
    """Harmonic amplitudes of an ideal triangle wave: odd harmonics falling as 1/n^2."""
    amplitudes = np.zeros(n)
    odd = np.arange(1, n + 1, 2)
    amplitudes[::2] = (1.0 / odd ** 2) * np.where((odd // 2) % 2 == 0, 1.0, -1.0)
    return np.abs(amplitudes)


def envelope(t, attack=0.01, decay=0.0, sustain=1.0, release=0.2):
    """A simple ADSR envelope over the whole of ``t``."""
    total = t[-1]
    out = np.ones_like(t)
    rising = t < attack
    out[rising] = t[rising] / attack
    if decay > 0.0:
        decaying = (t >= attack) & (t < attack + decay)
        out[decaying] = 1.0 - (1.0 - sustain) * (t[decaying] - attack) / decay
        out[t >= attack + decay] = sustain
    releasing = t > total - release
    out[releasing] *= (total - t[releasing]) / release
    return out


def match_level(signal, reference=None, target_rms=0.12):
    """Scale ``signal`` to a fixed RMS, then guarantee headroom.

    **This is the function that makes the comparisons in the book honest.** Two
    clips demonstrating a difference in timbre must not also differ in level, or
    the reader hears the level. Peak normalization would not do: a square wave
    and a sine of the same peak differ by about 3 dB in RMS, and the listener
    would report the square as louder and call it brighter.

    RMS is a proxy for loudness, not loudness itself -- a tone rich in high
    harmonics is somewhat louder than a sine of equal RMS, because the ear is
    more sensitive there (Chapter 7). For the narrow comparisons made here, all
    at the same pitch, the residual difference is small and is never the point
    of the example. Where it would be, the caption says so.
    """
    rms = float(np.sqrt(np.mean(np.square(signal))))
    if rms > 0.0:
        signal = signal * (target_rms / rms)
    if reference is not None:
        signal = signal * reference
    peak = float(np.max(np.abs(signal)))
    if peak > PEAK:
        signal = signal * (PEAK / peak)
    return signal


def _fade(signal, rate=RATE, milliseconds=FADE_MS):
    """Taper both ends, so a clip starts and stops without a click."""
    n = int(rate * milliseconds / 1000.0)
    if n * 2 >= len(signal):
        return signal
    ramp = np.linspace(0.0, 1.0, n)
    signal = signal.copy()
    signal[:n] *= ramp
    signal[-n:] *= ramp[::-1]
    return signal


def write_clip(name, signal, rate=RATE, bitrate=BITRATE):
    """Write ``audio/<name>.mp3`` from a float signal in [-1, 1]."""
    AUDIO.mkdir(exist_ok=True)
    signal = _fade(np.clip(signal, -1.0, 1.0), rate)
    pcm = (signal * 32767.0).astype("<i2")

    path = AUDIO / f"{name}.mp3"
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as scratch:
        with wave.open(scratch.name, "wb") as handle:
            handle.setnchannels(1)
            handle.setsampwidth(2)
            handle.setframerate(rate)
            handle.writeframes(pcm.tobytes())
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-i", scratch.name,
             "-codec:a", "libmp3lame", "-b:a", bitrate, "-ac", "1",
             # Strip the encoder tag and timestamps so a regenerated clip is
             # byte-identical and does not show up as a spurious diff.
             "-map_metadata", "-1", "-write_xing", "0", "-id3v2_version", "0",
             str(path)],
            check=True,
        )
    print(f"  wrote {path.relative_to(ROOT)}  ({path.stat().st_size // 1024} KB)")
    return path


def spectrum_of(signal, rate=RATE, fundamental=None, count=16):
    """Measure the amplitude of the first ``count`` harmonics of ``fundamental``.

    Measured from the signal rather than taken from the amplitudes it was built
    from, so the figure shows what is actually in the clip.
    """
    window = np.hanning(len(signal))
    magnitude = np.abs(np.fft.rfft(signal * window))
    freqs = np.fft.rfftfreq(len(signal), 1.0 / rate)
    if fundamental is None:
        fundamental = float(freqs[int(np.argmax(magnitude))])
    wanted = np.arange(1, count + 1) * fundamental
    # Take the local peak, so a slightly off-bin harmonic is not under-read.
    amps = np.array([magnitude[np.argmin(np.abs(freqs - f)) - 2:
                               np.argmin(np.abs(freqs - f)) + 3].max() for f in wanted])
    return wanted, amps / amps.max() if amps.max() else amps


def clip_and_figure(name, signal, fundamental, title=None, cycles=3, color=figstyle.BLUE,
                    rate=RATE, count=16, transcript_note=None):
    """The standard pair: write the clip and its waveform-and-spectrum figure.

    This is what almost every generator calls. The figure is what a reader in
    print gets in place of the player, so it has to carry the point of the
    example on its own.
    """
    signal = match_level(signal)
    write_clip(name, signal, rate)

    span = int(round(cycles * rate / fundamental))
    # Start clear of the fade-in so the waveform shown is the steady state.
    start = int(0.5 * rate)
    t = np.arange(span) / rate
    freqs, amps = spectrum_of(signal[start:start + rate], rate, fundamental, count)
    figstyle.wave_and_spectrum(
        name, t, signal[start:start + span], freqs, amps,
        title=title, color=color,
        cycles_label=f"{cycles} cycles at {fundamental:g} Hz",
    )
    if transcript_note:
        print(f"      transcript: {transcript_note}")
