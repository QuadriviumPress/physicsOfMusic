"""CC0 timpani and cymbal recordings for Chapter 12."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402

SOURCE = Path(__file__).resolve().parent / "sources" / "vsco"


def render(name, filename, title, colour, seconds=5.0):
    rate, signal = A.read_wav(SOURCE / filename)
    active = np.flatnonzero(np.abs(signal) > max(1e-5, np.max(np.abs(signal)) * 0.012))
    start = max(0, int(active[0]) - int(0.02 * rate)) if active.size else 0
    signal = A.match_level(signal[start:start + int(seconds * rate)], target_rms=0.10)
    A.write_clip(name, signal, rate=rate)

    figstyle.use_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.0))
    t = np.arange(len(signal)) / rate
    step = max(1, len(signal) // 2400)
    axes[0].plot(t[::step], signal[::step], color=colour, lw=0.75)
    axes[0].set(xlabel="time (s)", ylabel="pressure (arb.)", title="Waveform")
    axes[0].set_yticks([])
    magnitude = np.abs(np.fft.rfft(signal * np.hanning(len(signal))))
    frequencies = np.fft.rfftfreq(len(signal), 1 / rate)
    db = 20 * np.log10(np.maximum(magnitude / magnitude.max(), 1e-4))
    keep = (frequencies >= 20) & (frequencies <= 10000)
    axes[1].plot(frequencies[keep], db[keep], color=colour, lw=0.75)
    axes[1].set(xscale="log", xlim=(20, 10000), ylim=(-60, 2), xlabel="frequency (Hz)",
                ylabel="relative level (dB)", title="Spectrum")
    fig.suptitle(title, fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, name)


def main():
    render("ch12-real-timpani", "timpani-hit.wav", "Recorded timpani strike", figstyle.BLUE, 4.5)
    render("ch12-real-cymbal", "cymbal-crash.wav", "Recorded orchestral cymbal crash", figstyle.ORANGE, 5.0)


if __name__ == "__main__":
    main()
