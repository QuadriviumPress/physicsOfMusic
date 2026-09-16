"""Audio examples for Chapter 8, Pitch, Beats, Consonance, and Dissonance."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

BASE = 220.0


def beat_rates():
    """One tone against four neighbours: slow beats through to two separate tones."""
    offsets = [1.0, 4.0, 12.0, 40.0]
    segment = 2.2
    pieces = []
    for offset in offsets:
        t = A.time_axis(segment)
        signal = A.sine(t, BASE) + A.sine(t, BASE + offset)
        pieces.append(A.match_level(signal * A.envelope(t, attack=0.04, release=0.15)))
        pieces.append(np.zeros(int(0.3 * A.RATE)))
    A.write_clip("ch08-beat-rates", np.concatenate(pieces))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 4, figsize=(9.4, 2.7), sharey=True)
    t = np.linspace(0, 1.0, 3000)
    descriptions = ["slow throb", "clear beating", "rough", "two tones"]
    for ax, offset, description, colour in zip(axes, offsets, descriptions, figstyle.CYCLE):
        envelope = 2 * np.abs(np.cos(np.pi * offset * t))
        ax.plot(t, np.sin(2 * np.pi * BASE * t) + np.sin(2 * np.pi * (BASE + offset) * t),
                color=figstyle.GRAY, lw=0.4)
        ax.plot(t, envelope, color=colour, lw=2.0)
        ax.plot(t, -envelope, color=colour, lw=2.0)
        ax.set_title(f"+{offset:.0f} Hz\n{description}", fontsize=11,
                     fontweight="bold", color=colour)
        ax.set_xlabel("time (s)")
        ax.set_yticks([])
        ax.set_xlim(0, 1.0)
    fig.suptitle("220 Hz against a neighbour, four separations",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.72)
    figstyle.save(fig, "ch08-beat-rates")


def missing_fundamental():
    """The same pitch, with and without any energy at that frequency."""
    f0 = 150.0
    t = A.time_axis(2.4)
    modes = np.arange(1, 9)

    full_amps = 1.0 / modes
    stripped_amps = np.where(modes >= 3, 1.0 / modes, 0.0)

    for name, amps in (("ch08-full-series", full_amps),
                       ("ch08-missing-fundamental", stripped_amps)):
        signal = A.harmonics(t, f0, amps) * A.envelope(t, attack=0.05, release=0.25)
        A.write_clip(name, A.match_level(signal))


def interval_sweep():
    """Two six-partial tones, the upper sweeping slowly up an octave.

    The consonant intervals are audible as places where the sound settles. It is
    worth doing this with complex tones rather than pure ones: two *pure* tones
    swept the same way produce almost no such structure, which is the point of
    5.4.
    """
    duration = 16.0
    t = A.time_axis(duration)
    partials = np.arange(1, 7)
    amplitudes = 0.88 ** partials

    lower = np.zeros_like(t)
    for n, a in zip(partials, amplitudes):
        lower += a * np.sin(2 * np.pi * n * 262.0 * t)

    ratio = 2.0 ** (t / duration)
    upper = np.zeros_like(t)
    for n, a in zip(partials, amplitudes):
        phase = 2 * np.pi * np.cumsum(n * 262.0 * ratio) / A.RATE
        upper += a * np.sin(phase)

    signal = (lower + upper) * A.envelope(t, attack=0.1, release=0.4)
    A.write_clip("ch08-interval-sweep", A.match_level(signal))


def timbre_changes_consonance():
    """The same interval, on a harmonic timbre and on a stretched one.

    Sethares's argument: consonance is a relationship between a scale and a
    timbre, not a property of a ratio. A perfect fifth is smooth on harmonic
    partials and rough on stretched ones, and an interval matched to the
    stretched partials is smooth on them and rough on harmonic ones.
    """
    t = A.time_axis(2.4)
    partials = np.arange(1, 7)
    amplitudes = 0.85 ** partials
    stretch = 2.1    # partials at n**log2(stretch) instead of n

    def tone(f0, stretched):
        signal = np.zeros_like(t)
        for n, a in zip(partials, amplitudes):
            frequency = f0 * (n ** np.log2(stretch)) if stretched else f0 * n
            signal += a * np.sin(2 * np.pi * frequency * t)
        return signal

    envelope = A.envelope(t, attack=0.05, release=0.25)
    fifth = 1.5
    A.write_clip("ch08-fifth-harmonic",
                 A.match_level((tone(262, False) + tone(262 * fifth, False)) * envelope))
    A.write_clip("ch08-fifth-stretched",
                 A.match_level((tone(262, True) + tone(262 * fifth, True)) * envelope))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.0), sharey=True)
    for ax, stretched, title, colour in (
            (axes[0], False, "Harmonic partials", figstyle.BLUE),
            (axes[1], True, "Stretched partials", figstyle.RED)):
        for f0, style in ((262.0, "-"), (262.0 * fifth, "--")):
            freqs = np.array([f0 * (n ** np.log2(stretch)) if stretched else f0 * n
                              for n in partials])
            ax.vlines(freqs, 0, amplitudes, color=colour, lw=2.2,
                      alpha=1.0 if style == "-" else 0.45,
                      linestyles="solid" if style == "-" else "dashed")
        ax.set_xlabel("frequency (Hz)")
        ax.set_xlim(0, 3200)
        ax.set_title(title, fontsize=12, fontweight="bold", color=colour)
    axes[0].set_ylabel("amplitude")
    axes[0].text(1500, 0.78, "the two tones' partials\ncoincide repeatedly",
                 fontsize=10, color=figstyle.GREEN)
    axes[1].text(1500, 0.78, "they no longer coincide,\nand the fifth turns rough",
                 fontsize=10, color=figstyle.PURPLE)
    fig.suptitle("A perfect fifth on two different timbres (solid: lower note, dashed: upper)",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    figstyle.save(fig, "ch08-stretched-timbre")


def main():
    print("Chapter 8 audio:")
    beat_rates()
    missing_fundamental()
    interval_sweep()
    timbre_changes_consonance()


if __name__ == "__main__":
    main()
