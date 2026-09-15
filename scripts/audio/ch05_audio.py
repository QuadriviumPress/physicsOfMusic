"""Audio examples for Chapter 5, Fourier Analysis, Harmonics, and Timbre.

Every clip here is 220 Hz (A3) and every clip is matched in RMS level, so the
only thing that differs between them is which harmonics are present. That is
the whole argument of the chapter, and it is the one comparison a recording of
real instruments could not make cleanly.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audiolib as A  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402

F0 = 220.0
N = 24


def sine():
    t = A.time_axis()
    A.clip_and_figure("ch05-sine", A.sine(t, F0), F0,
                      title="A pure tone: one partial only")


def sawtooth():
    t = A.time_axis()
    signal = A.harmonics(t, F0, A.sawtooth_amplitudes(N))
    A.clip_and_figure("ch05-sawtooth", signal, F0,
                      title="Sawtooth: every harmonic, amplitude falling as $1/n$",
                      color=figstyle.RED)


def square():
    t = A.time_axis()
    signal = A.harmonics(t, F0, A.square_amplitudes(N))
    A.clip_and_figure("ch05-square", signal, F0,
                      title="Square: odd harmonics only, amplitude falling as $1/n$",
                      color=figstyle.GREEN)


def build_up():
    """The harmonic series assembled one partial at a time.

    Each second adds the next harmonic of a sawtooth. The point is audible
    rather than visual: the pitch never changes, and the tone brightens.
    """
    seconds_each = 0.8
    pieces = []
    for count in range(1, 9):
        t = A.time_axis(seconds_each)
        amplitudes = A.sawtooth_amplitudes(count)
        piece = A.harmonics(t, F0, amplitudes) * A.envelope(t, attack=0.02, release=0.05)
        pieces.append(A.match_level(piece))
    signal = np.concatenate(pieces)
    A.write_clip("ch05-harmonic-build-up", signal)

    # The figure for this one is a picture of the recipe, not of the waveform:
    # a waveform of an eight-part sequence is unreadable at page size.
    figstyle.use_style()
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8.0, 3.0))
    for step in range(1, 9):
        amplitudes = A.sawtooth_amplitudes(step)
        ax.vlines(np.arange(1, step + 1) * F0, 0, amplitudes + step * 0.0,
                  color=figstyle.CYCLE[(step - 1) % len(figstyle.CYCLE)],
                  lw=2.0, alpha=0.85)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("amplitude (arb.)")
    ax.set_title("Eight steps: each adds the next harmonic of 220 Hz", fontsize=12,
                 fontweight="bold")
    ax.set_xlim(0, 9 * F0)
    fig.tight_layout()
    figstyle.save(fig, "ch05-harmonic-build-up")


def three_waveforms():
    """One figure for the three-clip comparison directive."""
    figstyle.use_style()
    import matplotlib.pyplot as plt
    t = A.time_axis(0.02)
    span = int(round(3 * A.RATE / F0))
    fig, axes = plt.subplots(2, 3, figsize=(9.5, 4.4))
    specs = [
        ("Sine", np.array([1.0]), figstyle.BLUE),
        ("Sawtooth", A.sawtooth_amplitudes(N), figstyle.RED),
        ("Square", A.square_amplitudes(N), figstyle.GREEN),
    ]
    for column, (name, amplitudes, color) in enumerate(specs):
        signal = A.match_level(A.harmonics(t, F0, amplitudes))
        figstyle.waveform(axes[0][column], t[:span], signal[:span], color=color)
        axes[0][column].set_title(name, fontsize=12, fontweight="bold")
        freqs = np.arange(1, len(amplitudes) + 1) * F0
        figstyle.spectrum(axes[1][column], freqs, amplitudes / amplitudes.max(), color=color)
        axes[1][column].set_xlim(0, 12 * F0)
        if column:
            axes[0][column].set_ylabel("")
            axes[1][column].set_ylabel("")
    fig.suptitle("Same pitch, same level, three spectra", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.87)
    figstyle.save(fig, "ch05-three-waveforms")


def main():
    print("Chapter 5 audio:")
    sine()
    sawtooth()
    square()
    build_up()
    three_waveforms()


if __name__ == "__main__":
    main()
