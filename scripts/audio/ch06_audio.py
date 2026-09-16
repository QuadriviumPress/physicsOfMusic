"""Audio examples for Chapter 6, The Ear and the Physiology of Hearing."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def upper_limit_sweep():
    """A sweep from 2 kHz to 18 kHz, for finding your own upper limit.

    The clip is amplitude-flat, not loudness-flat: it is deliberately *not*
    corrected for the ear's frequency response, because the point is to hear
    where your own hearing stops, not to hear a tone of constant loudness.
    Chapter 7 makes the distinction.
    """
    duration = 14.0
    t = A.time_axis(duration)
    low, high = 2000.0, 18000.0
    frequency = low * (high / low) ** (t / duration)
    phase = 2 * np.pi * np.cumsum(frequency) / A.RATE
    signal = np.sin(phase) * A.envelope(t, attack=0.15, release=0.4)
    A.write_clip("ch06-upper-limit-sweep", A.match_level(signal))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.2, 2.6))
    marks = [(0, 2000), (4, 4400), (8, 9600), (12, 16000)]
    ax.plot(np.linspace(0, duration, 400),
            low * (high / low) ** (np.linspace(0, duration, 400) / duration),
            color=figstyle.BLUE, lw=2.4)
    for seconds, f in marks:
        ax.plot([seconds], [f], "o", color=figstyle.RED, ms=6)
        ax.annotate(f"{f/1000:.1f} kHz", xy=(seconds, f), xytext=(seconds + 0.3, f * 1.12),
                    fontsize=10, color=figstyle.RED)
    ax.set_yscale("log")
    ax.set_xlabel("time into the clip (s)")
    ax.set_ylabel("frequency (Hz)")
    ax.set_yticks([2000, 4000, 8000, 16000])
    ax.set_yticklabels(["2k", "4k", "8k", "16k"])
    ax.set_xlim(0, duration)
    ax.set_title("Note the time at which it disappears, and read off the frequency",
                 fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch06-upper-limit-sweep")


def missing_low_end():
    """A tone as heard through a telephone band, and in full.

    The ear canal and middle ear pass roughly 300 Hz to 3.4 kHz best, and a
    telephone was designed around that. Removing everything outside that band
    leaves speech intelligible and music thin -- a useful demonstration that
    intelligibility and fidelity are different requirements.
    """
    t = A.time_axis(2.6)
    f0 = 165.0
    amplitudes = 1.0 / np.arange(1, 25) ** 0.9
    full = A.harmonics(t, f0, amplitudes) * A.envelope(t, attack=0.05, release=0.25)

    # Keep only partials inside the telephone band.
    banded_amps = amplitudes.copy()
    for index in range(len(banded_amps)):
        frequency = (index + 1) * f0
        if frequency < 300 or frequency > 3400:
            banded_amps[index] = 0.0
    banded = A.harmonics(t, f0, banded_amps) * A.envelope(t, attack=0.05, release=0.25)

    A.write_clip("ch06-full-band", A.match_level(full))
    A.write_clip("ch06-telephone-band", A.match_level(banded))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    freqs = np.arange(1, 25) * f0
    ax.vlines(freqs, 0, amplitudes, color=figstyle.LIGHT, lw=3.0, label="removed")
    keep = banded_amps > 0
    ax.vlines(freqs[keep], 0, banded_amps[keep], color=figstyle.BLUE, lw=3.0, label="kept")
    ax.axvspan(300, 3400, color=figstyle.GREEN, alpha=0.10)
    ax.text(1850, 0.92, "the telephone band, 300 Hz – 3.4 kHz",
            ha="center", fontsize=10.5, color=figstyle.GREEN)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("amplitude")
    ax.set_xlim(0, 4200)
    ax.legend(fontsize=10)
    ax.set_title("A 165 Hz tone with everything outside the telephone band removed",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch06-telephone-band")


def main():
    print("Chapter 6 audio:")
    upper_limit_sweep()
    missing_low_end()


if __name__ == "__main__":
    main()
