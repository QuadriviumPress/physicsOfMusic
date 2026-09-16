"""Audio examples for Chapter 7, Loudness, Decibels, and the Equal-Loudness Contours."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from ch07_figures import equal_loudness_spl, ISO_F  # noqa: E402


def equal_amplitude_tones():
    """Three tones of identical amplitude, which are emphatically not equally loud.

    Deliberately bypasses match_level: every other comparison in this book holds
    the level fixed so that the reader hears something else, and this one holds
    the *amplitude* fixed so that the reader hears the level.
    """
    frequencies = [60.0, 300.0, 1000.0, 4000.0]
    step = 1.1
    pieces = []
    for frequency in frequencies:
        t = A.time_axis(step)
        pieces.append(A.sine(t, frequency) * A.envelope(t, attack=0.03, release=0.12) * A.PEAK)
    A.write_clip("ch07-equal-amplitude-tones", np.concatenate(pieces))

    # What the ear makes of them: read the phon value off the ISO curves.
    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    spl = 70.0
    phons = np.arange(10, 95, 5)
    table = np.array([equal_loudness_spl(p) for p in phons])
    apparent = []
    for frequency in frequencies:
        column = np.interp(frequency, ISO_F, np.arange(ISO_F.size))
        levels = np.array([np.interp(column, np.arange(ISO_F.size), row) for row in table])
        apparent.append(float(np.interp(spl, levels, phons)))
    bars = ax.bar([f"{f:g} Hz" for f in frequencies], apparent,
                  color=[figstyle.PURPLE, figstyle.BLUE, figstyle.GREEN, figstyle.ORANGE],
                  width=0.55)
    for bar, value in zip(bars, apparent):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 1.5, f"{value:.0f} phon",
                ha="center", fontsize=11, fontweight="bold")
    ax.axhline(spl, color=figstyle.RED, lw=1.4, ls="--")
    ax.text(3.35, spl + 1.5, "all four are 70 dB SPL", ha="right",
            fontsize=10.5, color=figstyle.RED)
    ax.set_ylabel("loudness level (phon)")
    ax.set_ylim(0, 85)
    ax.set_title("Four tones at the same physical level, and how loud each sounds",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch07-equal-amplitude-tones")


def masking_demo():
    """A quiet high tone, alone and then buried under a loud low one."""
    quiet_f, masker_f = 1600.0, 400.0
    segment = 1.6
    t = A.time_axis(segment)
    quiet = A.sine(t, quiet_f) * A.envelope(t, attack=0.04, release=0.12) * 0.045
    masker = A.sine(t, masker_f) * A.envelope(t, attack=0.04, release=0.12) * 0.55
    silence = np.zeros(int(0.35 * A.RATE))

    signal = np.concatenate([quiet, silence, masker, silence, masker + quiet])
    A.write_clip("ch07-masking-demo", signal * A.PEAK / np.max(np.abs(signal)))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 2.8))
    labels = ["the quiet 1.6 kHz tone\nalone", "the loud 400 Hz\nmasker alone", "both together"]
    starts = [0, segment + 0.35, 2 * (segment + 0.35)]
    for start, label, colour in zip(starts, labels, (figstyle.BLUE, figstyle.RED, figstyle.PURPLE)):
        ax.add_patch(plt.Rectangle((start, 0), segment, 1, color=colour, alpha=0.25))
        ax.text(start + segment / 2, 0.5, label, ha="center", va="center", fontsize=10.5)
    ax.set_xlim(0, 3 * segment + 2 * 0.35)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("time (s)")
    ax.set_title("The third segment contains both tones — can you still hear the high one?",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch07-masking-demo")


def main():
    print("Chapter 7 audio:")
    equal_amplitude_tones()
    masking_demo()


if __name__ == "__main__":
    main()
