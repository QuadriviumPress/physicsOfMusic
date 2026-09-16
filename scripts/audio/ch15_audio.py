"""Audio examples for Chapter 15, Electronic and Recorded Sound."""

import sys
from pathlib import Path

import numpy as np
from scipy.special import jv

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def aliasing_sweep():
    """A rising sweep sampled too slowly, so it turns round and comes back down.

    Synthesized directly at the low rate without an anti-aliasing filter, which
    is exactly the mistake the filter exists to prevent -- and the only way to
    demonstrate the effect rather than describe it.
    """
    low_rate = 8000
    duration = 8.0
    n = int(duration * low_rate)
    t = np.arange(n) / low_rate
    frequency = 200 + (7000 - 200) * t / duration
    phase = 2 * np.pi * np.cumsum(frequency) / low_rate
    aliased = np.sin(phase)

    # Resample to the project rate by simple repetition, keeping the artefact.
    factor = A.RATE // low_rate
    upsampled = np.repeat(aliased, factor)
    t_full = np.arange(upsampled.size) / A.RATE
    upsampled *= A.envelope(t_full, attack=0.1, release=0.4)
    A.write_clip("ch15-aliasing-sweep", A.match_level(upsampled))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    nyquist = low_rate / 2
    heard = np.abs(((frequency + nyquist) % (2 * nyquist)) - nyquist)
    ax.plot(t, frequency, color=figstyle.GRAY, lw=2.0, ls="--", label="frequency generated")
    ax.plot(t, heard, color=figstyle.RED, lw=2.4, label="frequency heard")
    ax.axhline(nyquist, color=figstyle.GRAY, lw=1.0, ls=":")
    ax.text(0.2, nyquist + 150, f"Nyquist = {nyquist:.0f} Hz", fontsize=10,
            color=figstyle.GRAY)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("frequency (Hz)")
    ax.set_xlim(0, duration)
    ax.legend(fontsize=10, loc="upper left")
    ax.set_title("A sweep sampled at 8 kHz with no anti-aliasing filter",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch15-aliasing-sweep")


def bit_depth():
    """The same passage at three bit depths, with and without dither."""
    t = A.time_axis(3.0)
    amplitudes = 1.0 / np.arange(1, 13) ** 1.1
    signal = A.harmonics(t, 220.0, amplitudes) * np.exp(-t / 1.4)
    signal = A.match_level(signal)

    def quantize(values, bits, dither=False, seed=0):
        levels = 2 ** (bits - 1)
        rng = np.random.default_rng(seed)
        noise = rng.uniform(-0.5, 0.5, values.size) / levels if dither else 0.0
        return np.round((values + noise) * levels) / levels

    A.write_clip("ch15-16-bit", quantize(signal, 16))
    A.write_clip("ch15-6-bit", quantize(signal, 6))
    A.write_clip("ch15-6-bit-dithered", quantize(signal, 6, dither=True))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    bits = np.arange(4, 25)
    ax.plot(bits, 6.02 * bits + 1.76, color=figstyle.BLUE, lw=2.4)
    for depth, label, colour in ((8, "8-bit", figstyle.RED),
                                 (16, "CD, 16-bit", figstyle.GREEN),
                                 (24, "studio, 24-bit", figstyle.PURPLE)):
        value = 6.02 * depth + 1.76
        ax.plot([depth], [value], "o", color=colour, ms=8)
        ax.annotate(f"{label}\n{value:.0f} dB", xy=(depth, value),
                    xytext=(depth - 3.2, value + 9), fontsize=10, color=colour)
    ax.set_xlabel("bit depth")
    ax.set_ylabel("dynamic range (dB)")
    ax.set_xlim(4, 26)
    ax.set_title("Every bit buys about 6 dB", fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch15-bit-depth")


def synthesis():
    """The same pitch by additive, subtractive, and FM synthesis."""
    t = A.time_axis(2.6)
    envelope = A.envelope(t, attack=0.04, decay=0.25, sustain=0.7, release=0.3)
    f0 = 220.0

    # Additive: specify each partial.
    additive_amps = np.array([1.0, 0.0, 0.7, 0.0, 0.45, 0.0, 0.3, 0.2])
    additive = A.harmonics(t, f0, additive_amps)

    # Subtractive: a sawtooth through a sweeping low-pass.
    saw = A.harmonics(t, f0, A.sawtooth_amplitudes(40))
    cutoff = 400 + 3000 * np.exp(-t / 0.7)
    subtractive = np.zeros_like(t)
    for n in range(1, 41):
        gain = 1.0 / np.sqrt(1 + (n * f0 / cutoff) ** 6)
        subtractive += (1.0 / n) * np.sin(2 * np.pi * n * f0 * t) * gain

    # FM: one carrier, one modulator, with the index falling over the note.
    index = 6.0 * np.exp(-t / 0.5)
    fm = np.sin(2 * np.pi * f0 * t + index * np.sin(2 * np.pi * f0 * t))

    for name, signal in (("ch15-additive", additive),
                         ("ch15-subtractive", subtractive),
                         ("ch15-fm", fm)):
        A.write_clip(name, A.match_level(signal * envelope))


def codec():
    """A tone with and without its masked components.

    The two should be very hard to tell apart, which is the entire argument for
    perceptual coding: the discarded components were never audible.
    """
    t = A.time_axis(2.8)
    envelope = A.envelope(t, attack=0.05, release=0.3)
    masker = 0.8 * np.sin(2 * np.pi * 900.0 * t)
    quiet_partials = [(1500.0, 0.010), (2600.0, 0.006), (4200.0, 0.004)]
    extras = sum(a * np.sin(2 * np.pi * f * t) for f, a in quiet_partials)

    A.write_clip("ch15-codec-full", A.match_level((masker + extras) * envelope))
    A.write_clip("ch15-codec-stripped", A.match_level(masker * envelope))


def main():
    print("Chapter 15 audio:")
    aliasing_sweep()
    bit_depth()
    synthesis()
    codec()


if __name__ == "__main__":
    main()
