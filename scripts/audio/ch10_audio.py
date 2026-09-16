"""Audio examples for Chapter 10, String Instruments."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

F0 = 196.0     # the G string of a guitar
N_MODES = 20


def plucked(position, seconds=2.6, damping=0.9):
    """A plucked string, with mode amplitudes set by the pluck point.

    Higher modes decay faster, which is what makes a plucked note darken as it
    dies (5.4). Without it the synthesis sounds like an organ.
    """
    t = A.time_axis(seconds)
    n = np.arange(1, N_MODES + 1)
    amplitudes = np.abs(np.sin(n * np.pi * position)) / n ** 2
    signal = np.zeros_like(t)
    for index, amplitude in zip(n, amplitudes):
        if amplitude < 1e-9:
            continue
        signal += amplitude * np.sin(2 * np.pi * index * F0 * t) * np.exp(-t / (damping / index ** 0.6))
    return signal


def pluck_positions():
    """The same string plucked in three places."""
    for name, position in (("ch10-pluck-middle", 0.5),
                           ("ch10-pluck-fifth", 0.2),
                           ("ch10-pluck-bridge", 0.08)):
        A.write_clip(name, A.match_level(plucked(position)))


def bowed_vs_plucked():
    """Same string, same spectrum, two ways of putting energy in."""
    t = A.time_axis(2.8)
    n = np.arange(1, N_MODES + 1)

    # Helmholtz motion gives a sawtooth at the bridge: every harmonic, as 1/n.
    bowed = np.zeros_like(t)
    for index in n:
        bowed += (1.0 / index) * np.sin(2 * np.pi * index * F0 * t)
    bowed *= A.envelope(t, attack=0.14, release=0.22)

    pluck = plucked(0.2, seconds=2.8)

    A.write_clip("ch10-bowed", A.match_level(bowed))
    A.write_clip("ch10-plucked", A.match_level(pluck))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 2.9))
    window = int(0.008 * A.RATE)
    for signal, label, colour in ((bowed, "bowed — energy supplied continuously", figstyle.GREEN),
                                  (pluck, "plucked — one impulse, then decay", figstyle.RED)):
        envelope = np.convolve(np.abs(signal), np.ones(window) / window, mode="same")
        ax.plot(t, envelope / envelope.max(), color=colour, lw=2.2, label=label)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, 2.8)
    ax.legend(fontsize=10)
    ax.set_title("The same string, excited two ways", fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch10-bowed-vs-plucked")


def stretched_octave():
    """A piano octave tuned exactly 2:1 and tuned to the partial.

    With inharmonic partials, the mathematically exact octave beats and the
    stretched one does not -- the opposite of what a reader expects, and the
    whole justification for the Railsback curve.
    """
    b = 4.0e-4
    lower_f = 110.0
    t = A.time_axis(3.2)
    envelope = np.exp(-t / 1.6)

    def piano_string(f1, partials=10):
        signal = np.zeros_like(t)
        for n in range(1, partials + 1):
            frequency = n * f1 * np.sqrt(1 + b * n ** 2)
            signal += (1.0 / n ** 1.1) * np.sin(2 * np.pi * frequency * t)
        return signal

    exact = piano_string(lower_f) + piano_string(2 * lower_f)
    # Tune the upper note's fundamental to the lower note's second partial.
    stretched_f = 2 * lower_f * np.sqrt(1 + b * 4)
    stretched = piano_string(lower_f) + piano_string(stretched_f)

    A.write_clip("ch10-octave-exact", A.match_level(exact * envelope))
    A.write_clip("ch10-octave-stretched", A.match_level(stretched * envelope))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    n = np.arange(1, 7)
    lower_partials = n * lower_f * np.sqrt(1 + b * n ** 2)
    ax.vlines(lower_partials, 0, 1.0 / n ** 1.1, color=figstyle.GRAY, lw=2.4,
              label="lower note's partials")
    for f1, label, colour, offset in ((2 * lower_f, "exact 2:1 octave", figstyle.RED, 0.0),
                                      (stretched_f, "stretched octave", figstyle.GREEN, 0.0)):
        upper = n * f1 * np.sqrt(1 + b * n ** 2)
        ax.vlines(upper, offset, offset + 0.55 / n ** 1.1, color=colour, lw=1.8,
                  label=label, linestyles="dashed" if colour == figstyle.RED else "solid")
    ax.annotate("the lower note's 2nd partial is sharp of 220 Hz,\n"
                "so an exact 220 Hz upper note beats against it",
                xy=(lower_partials[1], 0.55), xytext=(420, 0.78),
                fontsize=10, color=figstyle.RED,
                arrowprops=dict(arrowstyle="->", color=figstyle.RED, lw=1.1))
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, 1400)
    ax.legend(fontsize=9.5, loc="upper right")
    ax.set_title("Why a piano octave must be stretched", fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch10-stretched-octave")


def main():
    print("Chapter 10 audio:")
    pluck_positions()
    bowed_vs_plucked()
    stretched_octave()


if __name__ == "__main__":
    main()
