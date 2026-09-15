"""Audio examples for Chapter 3, Superposition, Interference, and Standing Waves."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

F1 = 165.0     # the open string


def string_harmonics():
    """Touching a string at 1/2, 1/3 and 1/4 of its length.

    Lightly touching a node forces a node there, suppressing every mode that
    does not already have one -- so the string jumps to the corresponding
    harmonic. The pitch rises by an octave, an octave and a fifth, and two
    octaves, and the tone becomes progressively purer, because fewer partials
    survive.
    """
    seconds = 1.6
    pieces = []
    for n in (1, 2, 3, 4):
        t = A.time_axis(seconds)
        # Only harmonics that are multiples of n survive the touch.
        amplitudes = np.zeros(16)
        for index in range(n, 17, n):
            amplitudes[index - 1] = 1.0 / (index / n) ** 1.3
        signal = A.harmonics(t, F1, amplitudes) * np.exp(-t / 0.9)
        pieces.append(A.match_level(signal))
    A.write_clip("ch03-string-harmonics", np.concatenate(pieces))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 4, figsize=(9.4, 2.9), sharey=True)
    for ax, n, colour in zip(axes, (1, 2, 3, 4), figstyle.CYCLE):
        amplitudes = np.zeros(16)
        for index in range(n, 17, n):
            amplitudes[index - 1] = 1.0 / (index / n) ** 1.3
        freqs = np.arange(1, 17) * F1
        keep = amplitudes > 0
        ax.vlines(freqs[keep], 0, amplitudes[keep], color=colour, lw=2.2)
        ax.plot(freqs[keep], amplitudes[keep], "o", color=colour, ms=4)
        ax.set_xlim(0, 17 * F1)
        ax.set_xticks([])
        ax.set_title(f"touched at $L/{n}$" if n > 1 else "open string",
                     fontsize=11, fontweight="bold", color=colour)
        ax.text(0.5, 0.86, f"sounds ${n}f_1$", transform=ax.transAxes,
                ha="center", fontsize=10.5)
    axes[0].set_ylabel("amplitude")
    fig.suptitle("Forcing a node: the surviving partials, on one string",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    figstyle.save(fig, "ch03-string-harmonics")


def open_vs_stopped():
    """Two pipes of the same length: one open at both ends, one stopped.

    The stopped pipe sounds an octave lower and has only odd harmonics. Both
    differences are audible, and they are different differences: the octave is
    pitch, the missing evens are timbre.
    """
    t = A.time_axis(2.5)
    n = 16

    open_amps = 1.0 / np.arange(1, n + 1) ** 1.2
    open_pipe = A.harmonics(t, 2 * F1, open_amps) * A.envelope(t, attack=0.05, release=0.2)
    open_pipe = A.match_level(open_pipe)
    A.write_clip("ch03-open-pipe", open_pipe)

    stopped_amps = np.zeros(n)
    odd = np.arange(1, n + 1, 2)
    stopped_amps[::2] = 1.0 / odd ** 1.2
    stopped_pipe = A.harmonics(t, F1, stopped_amps) * A.envelope(t, attack=0.05, release=0.2)
    stopped_pipe = A.match_level(stopped_pipe)
    A.write_clip("ch03-stopped-pipe", stopped_pipe)

    figstyle.use_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.0), sharey=True)
    for ax, (amps, base, title, colour) in zip(axes, (
            (open_amps, 2 * F1, f"Open pipe — sounds {2*F1:.0f} Hz, all harmonics", figstyle.BLUE),
            (stopped_amps, F1, f"Stopped pipe — sounds {F1:.0f} Hz, odd harmonics only", figstyle.RED))):
        freqs = np.arange(1, len(amps) + 1) * base
        keep = amps > 0
        ax.vlines(freqs[keep], 0, amps[keep], color=colour, lw=2.2)
        ax.plot(freqs[keep], amps[keep], "o", color=colour, ms=4)
        ax.set_xlabel("frequency (Hz)")
        ax.set_title(title, fontsize=11.5, fontweight="bold")
        ax.set_xlim(0, 2800)
    axes[0].set_ylabel("amplitude")
    fig.suptitle("Same length of tube, one end closed", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    figstyle.save(fig, "ch03-open-vs-stopped")


def beating_dead_spot():
    """Two sources drifting through a path difference, heard as a fade.

    This is interference in space, sampled by walking: the listener passes
    through positions where the two arrivals are in step and positions where
    they are opposed.
    """
    duration = 6.0
    t = A.time_axis(duration)
    frequency = 500.0
    # Path difference sweeping through three wavelengths as the listener walks.
    delta = np.linspace(0.0, 3.0, t.size)
    amplitude = np.abs(np.cos(np.pi * delta))
    signal = A.sine(t, frequency) * amplitude
    signal = A.match_level(signal)
    A.write_clip("ch03-walking-through-interference", signal)

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.2, 2.8))
    # Plot a coarse grid, not the audio-rate array: 264,600 points of
    # fill_between is a 13 MB SVG that draws the same curve as 600 points.
    plot_delta = np.linspace(0.0, 3.0, 600)
    plot_amplitude = np.abs(np.cos(np.pi * plot_delta))
    ax.plot(plot_delta, plot_amplitude, color=figstyle.GREEN, lw=2.2)
    ax.fill_between(plot_delta, 0, plot_amplitude, color=figstyle.LIGHT, alpha=0.5)
    for m in (0.5, 1.5, 2.5):
        ax.plot([m], [0], "o", color=figstyle.RED, ms=7)
        ax.text(m, 0.06, "silent", color=figstyle.RED, ha="center", fontsize=10)
    ax.set_xlabel("path difference as the listener walks (wavelengths)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, 3)
    ax.set_title("Walking through the interference pattern of two loudspeakers",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch03-walking-through-interference")


def main():
    print("Chapter 3 audio:")
    string_harmonics()
    open_vs_stopped()
    beating_dead_spot()


if __name__ == "__main__":
    main()
