"""Audio examples for Chapter 1, Sound, Music, and Simple Harmonic Motion."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

A4 = 440.0
A3 = 220.0


def pure_tone():
    """What a single sinusoid actually sounds like."""
    t = A.time_axis()
    signal = A.sine(t, A4) * A.envelope(t, attack=0.02, release=0.3)
    A.clip_and_figure("ch01-a440", signal, A4,
                      title="A pure tone at 440 Hz", cycles=4)


def decay_compare():
    """Same pitch, same spectrum, two envelopes.

    The only difference between these is how the amplitude falls, and it is
    enough to make one sound struck and the other bowed. Chapter 5 returns to
    this: the envelope carries at least as much of an instrument's identity as
    the steady-state spectrum does.
    """
    t = A.time_axis(3.0)
    amplitudes = np.array([1.0, 0.5, 0.3, 0.18, 0.1, 0.06])
    tone = A.harmonics(t, A3, amplitudes)

    struck = tone * np.exp(-t / 0.55)
    struck = A.match_level(struck)
    A.write_clip("ch01-struck", struck)

    sustained = tone * A.envelope(t, attack=0.12, release=0.25)
    sustained = A.match_level(sustained)
    A.write_clip("ch01-sustained", sustained)

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    for signal, label, colour in ((struck, "struck — decays from the moment it starts", figstyle.RED),
                                  (sustained, "sustained — held, then released", figstyle.BLUE)):
        # Plot the envelope, not the waveform: at 220 Hz over three seconds the
        # carrier is a solid block of ink and shows nothing.
        window = int(0.01 * A.RATE)
        envelope = np.abs(signal)
        envelope = np.convolve(envelope, np.ones(window) / window, mode="same")
        ax.plot(t, envelope, color=colour, lw=2.0, label=label)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, 3)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Two envelopes over the same tone", fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch01-decay-compare")


def amplitude_steps():
    """The same tone, dropped 6 dB at a time.

    Deliberately *not* level-matched -- this is the one example in the book
    whose whole point is a change in level, so it bypasses match_level and sets
    the amplitudes by hand.
    """
    step_seconds = 0.9
    pieces = []
    factors = [1.0, 0.5, 0.25, 0.125, 0.0625]
    for factor in factors:
        t = A.time_axis(step_seconds)
        piece = A.sine(t, A4) * A.envelope(t, attack=0.02, release=0.08) * factor
        pieces.append(piece)
    signal = np.concatenate(pieces) * A.PEAK
    A.write_clip("ch01-amplitude-steps", signal)

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    t = np.arange(len(signal)) / A.RATE
    ax.plot(t, np.abs(signal), color=figstyle.BLUE, lw=0.8)
    for index, factor in enumerate(factors):
        centre = (index + 0.5) * step_seconds
        drop = 0 if index == 0 else -6 * index
        ax.text(centre, 0.78, f"{drop} dB", ha="center", fontsize=10.5,
                fontweight="bold", color=figstyle.RED)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, len(signal) / A.RATE)
    ax.set_ylim(0, 0.95)
    ax.set_title("Halving the amplitude four times: each step is 6 dB",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch01-amplitude-steps")


def main():
    print("Chapter 1 audio:")
    pure_tone()
    decay_compare()
    amplitude_steps()


if __name__ == "__main__":
    main()
