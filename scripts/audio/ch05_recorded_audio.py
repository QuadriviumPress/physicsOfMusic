"""CC0 recordings that put real instrumental timbres beside Chapter 5's models."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402

SOURCE = Path(__file__).resolve().parent / "sources" / "vsco"
RECORDINGS = [
    ("ch05-real-violin", "violin-arco-vibrato-a4-p.wav", "Violin", figstyle.BLUE),
    ("ch05-real-flute", "flute-expressive-vibrato-a4.wav", "Flute", figstyle.GREEN),
    ("ch05-real-trumpet", "trumpet-sustain-a4.wav", "Trumpet", figstyle.RED),
]


def steady_excerpt(signal, rate, seconds=3.5):
    """Keep the performed attack and a compact stretch of the sustained note."""
    active = np.flatnonzero(np.abs(signal) > max(1e-5, np.max(np.abs(signal)) * 0.015))
    start = max(0, int(active[0]) - int(0.04 * rate)) if active.size else 0
    return signal[start:start + int(seconds * rate)]


def main():
    figstyle.use_style()
    fig, axes = plt.subplots(3, 1, figsize=(8.8, 5.7), sharex=True, sharey=True)
    for ax, (name, filename, label, colour) in zip(axes, RECORDINGS):
        rate, signal = A.read_wav(SOURCE / filename)
        signal = A.match_level(steady_excerpt(signal, rate), target_rms=0.105)
        A.write_clip(name, signal, rate=rate)
        start = min(int(0.75 * rate), max(0, len(signal) - rate))
        windowed = signal[start:start + rate]
        windowed *= np.hanning(len(windowed))
        magnitude = np.abs(np.fft.rfft(windowed))
        frequencies = np.fft.rfftfreq(len(windowed), 1 / rate)
        db = 20 * np.log10(np.maximum(magnitude / magnitude.max(), 1e-4))
        keep = (frequencies >= 100) & (frequencies <= 8000)
        ax.plot(frequencies[keep], db[keep], color=colour, lw=0.9)
        for harmonic in range(1, 10):
            ax.axvline(880 * harmonic, color=figstyle.GRAY, lw=0.45, alpha=0.22)
        ax.set(xlim=(100, 8000), ylim=(-60, 2), ylabel=label)
    axes[-1].set_xlabel("frequency (Hz)")
    fig.supylabel("level relative to each peak (dB)", x=0.01, fontsize=10)
    fig.suptitle("Three real instruments sustaining the same note (about 880 Hz)",
                 fontsize=12.5, fontweight="bold")
    axes[-1].text(890, -54, "dotted lines: 880 Hz spacing", color=figstyle.GRAY, fontsize=9)
    fig.tight_layout()
    fig.subplots_adjust(top=0.90, left=0.11)
    figstyle.save(fig, "ch05-real-instruments")


if __name__ == "__main__":
    main()
