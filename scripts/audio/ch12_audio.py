"""Audio examples for Chapter 12, Percussion: Membranes, Bars, and Plates."""

import sys
from pathlib import Path

import numpy as np
from scipy.special import jn_zeros

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def struck(ratios, f0, amplitudes=None, decays=None, seconds=3.0, rng_seed=0):
    """A struck object: a set of inharmonic partials, each decaying at its own rate."""
    t = A.time_axis(seconds)
    ratios = np.asarray(ratios, dtype=float)
    if amplitudes is None:
        amplitudes = 1.0 / ratios ** 0.8
    if decays is None:
        decays = 1.4 / ratios ** 0.55
    signal = np.zeros_like(t)
    for ratio, amplitude, decay in zip(ratios, amplitudes, decays):
        signal += amplitude * np.sin(2 * np.pi * ratio * f0 * t) * np.exp(-t / decay)
    # A brief strike transient: broadband, and what makes it sound hit.
    rng = np.random.default_rng(rng_seed)
    click = rng.normal(0, 1, t.size) * np.exp(-t / 0.004)
    return signal + 0.25 * click / np.max(np.abs(click))


def bars():
    """A plain bar and an undercut one, at the same pitch."""
    plain = [1.0, 2.756, 5.404, 8.933, 13.345]
    undercut = [1.0, 4.0, 10.0, 8.933, 13.345]
    A.write_clip("ch12-bar-plain", A.match_level(struck(plain, 262.0, rng_seed=1)))
    A.write_clip("ch12-bar-undercut", A.match_level(struck(undercut, 262.0, rng_seed=1)))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 2.9), sharey=True)
    for ax, ratios, title, colour in ((axes[0], plain, "Plain bar", figstyle.RED),
                                      (axes[1], undercut, "Undercut bar", figstyle.GREEN)):
        freqs = np.array(ratios) * 262.0
        amps = 1.0 / np.array(ratios) ** 0.8
        ax.vlines(freqs, 0, amps, color=colour, lw=2.4)
        ax.plot(freqs, amps, "o", color=colour, ms=5)
        for harmonic in (1, 2, 3, 4):
            ax.axvline(harmonic * 262.0, color=figstyle.GRAY, lw=0.6, ls=":")
        ax.set_xlim(0, 1600)
        ax.set_xlabel("frequency (Hz)")
        ax.set_title(title, fontsize=12, fontweight="bold", color=colour)
    axes[0].set_ylabel("amplitude")
    axes[1].annotate("the 2nd mode has been pulled\nonto 4:1, two octaves up",
                     xy=(1048, 0.33), xytext=(500, 0.62), fontsize=10,
                     color=figstyle.GREEN,
                     arrowprops=dict(arrowstyle="->", color=figstyle.GREEN, lw=1.1))
    fig.suptitle("Dotted lines mark exact harmonics of the fundamental",
                 fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    figstyle.save(fig, "ch12-bar-comparison")


def membranes():
    """An ideal membrane against a real timpano."""
    ideal_roots = np.array([jn_zeros(m, 1)[0] for m in (0, 1, 2, 3, 4, 5)])
    ideal = ideal_roots / ideal_roots[0]
    timpani = np.array([1.00, 1.50, 2.00, 2.44, 2.90, 3.36])

    A.write_clip("ch12-membrane-ideal",
                 A.match_level(struck(ideal, 150.0, seconds=2.4, rng_seed=2)))
    A.write_clip("ch12-timpani",
                 A.match_level(struck(timpani, 146.0, seconds=2.8, rng_seed=2)))


def bell():
    """A tuned bell: hum, prime, tierce, quint, nominal, and a few above."""
    ratios = [0.5, 1.0, 1.2, 1.5, 2.0, 2.5, 2.67, 3.0, 4.0, 5.33]
    amplitudes = np.array([0.7, 1.0, 0.85, 0.6, 0.9, 0.35, 0.3, 0.25, 0.2, 0.15])
    decays = np.array([6.0, 4.0, 3.0, 2.2, 2.6, 1.2, 1.0, 0.8, 0.5, 0.35])
    A.write_clip("ch12-bell", A.match_level(
        struck(ratios, 262.0, amplitudes, decays, seconds=6.0, rng_seed=3)))


def cymbal():
    """A cymbal: hundreds of closely spaced partials, heard as noise.

    Built by scattering partials at random rather than from any mode formula.
    That is not laziness -- above a few hundred hertz a cymbal's modes really
    are too dense to enumerate, and the point of the example is that the ear
    receives something it cannot resolve into lines.
    """
    rng = np.random.default_rng(7)
    t = A.time_axis(4.0)
    signal = np.zeros_like(t)
    for _ in range(320):
        frequency = rng.uniform(280, 12000)
        amplitude = (1.0 / frequency ** 0.55) * rng.uniform(0.4, 1.0)
        decay = rng.uniform(0.6, 3.0) * (2000.0 / frequency) ** 0.35
        signal += amplitude * np.sin(2 * np.pi * frequency * t + rng.uniform(0, 2 * np.pi)) \
            * (1 - np.exp(-t / 0.02)) * np.exp(-t / decay)
    A.write_clip("ch12-cymbal", A.match_level(signal))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    window = np.hanning(8192)
    segment = signal[int(0.3 * A.RATE):int(0.3 * A.RATE) + 8192] * window
    spectrum = np.abs(np.fft.rfft(segment))
    freqs = np.fft.rfftfreq(8192, 1 / A.RATE)
    ax.semilogx(freqs[1:], 20 * np.log10(spectrum[1:] / spectrum.max()),
                color=figstyle.PURPLE, lw=0.7)
    ax.set_xlim(100, 16000)
    ax.set_ylim(-70, 2)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("level (dB)")
    ax.set_title("A cymbal's spectrum: no lines to count",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch12-cymbal")


def main():
    print("Chapter 12 audio:")
    bars()
    membranes()
    bell()
    cymbal()


if __name__ == "__main__":
    main()
