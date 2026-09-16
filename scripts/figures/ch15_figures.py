"""Figures for Chapter 15, Electronic and Recorded Sound."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def polar_patterns():
    """The four standard microphone patterns."""
    use_style()
    fig, axes = plt.subplots(1, 4, figsize=(9.8, 2.9),
                             subplot_kw={"projection": "polar"})
    theta = np.linspace(0, 2 * np.pi, 720)

    patterns = [
        ("Omnidirectional", np.ones_like(theta), BLUE),
        ("Cardioid", 0.5 + 0.5 * np.cos(theta), GREEN),
        ("Figure-of-eight", np.abs(np.cos(theta)), RED),
        ("Hypercardioid", np.abs(0.25 + 0.75 * np.cos(theta)), PURPLE),
    ]
    for ax, (name, response, colour) in zip(axes, patterns):
        ax.plot(theta, response, color=colour, lw=2.4)
        ax.fill(theta, response, color=colour, alpha=0.18)
        ax.set_theta_zero_location("N")
        ax.set_ylim(0, 1.1)
        ax.set_yticks([])
        ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2])
        ax.set_xticklabels(["front", "", "rear", ""], fontsize=9)
        ax.set_title(name, fontsize=11, fontweight="bold", color=colour, pad=14)

    fig.suptitle("Microphone polar patterns: what the microphone hears, by direction",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.76)
    save(fig, "ch15-polar-patterns")


def sampling():
    """Sampling a waveform, and reconstructing it."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.2))

    rate = 20.0
    t = np.linspace(0, 1, 1200)
    signal = np.sin(2 * np.pi * 3 * t) + 0.4 * np.sin(2 * np.pi * 7 * t)
    samples_t = np.arange(0, 1, 1 / rate)
    samples = np.sin(2 * np.pi * 3 * samples_t) + 0.4 * np.sin(2 * np.pi * 7 * samples_t)

    left.plot(t, signal, color=GRAY, lw=1.6, alpha=0.7, label="original")
    left.vlines(samples_t, 0, samples, color=BLUE, lw=1.6)
    left.plot(samples_t, samples, "o", color=BLUE, ms=6, label="samples")
    left.axhline(0, color=GRAY, lw=0.7)
    left.set_xlabel("time")
    left.set_yticks([])
    left.legend(fontsize=9.5, loc="upper right")
    left.set_title("Sampling: keep the value at regular instants",
                   fontsize=11.5, fontweight="bold")

    # Reconstruction by sinc interpolation, which is what the theorem promises.
    reconstructed = np.zeros_like(t)
    for sample_time, value in zip(samples_t, samples):
        reconstructed += value * np.sinc((t - sample_time) * rate)
    right.plot(t, signal, color=GRAY, lw=2.6, alpha=0.5, label="original")
    right.plot(t, reconstructed, color=RED, lw=1.6, ls="--", label="reconstructed")
    right.plot(samples_t, samples, "o", color=BLUE, ms=5)
    right.axhline(0, color=GRAY, lw=0.7)
    right.set_xlabel("time")
    right.set_yticks([])
    right.legend(fontsize=9.5, loc="upper right")
    right.set_title("Reconstruction is exact, not approximate",
                    fontsize=11.5, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch15-sampling")


def aliasing():
    """What happens above the Nyquist frequency."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.2))

    rate = 10.0
    t = np.linspace(0, 1, 1200)
    samples_t = np.arange(0, 1.001, 1 / rate)

    true_f, alias_f = 9.0, 1.0
    left.plot(t, np.sin(2 * np.pi * true_f * t), color=BLUE, lw=1.6,
              label=f"{true_f:.0f} Hz (the real signal)")
    left.plot(t, np.sin(2 * np.pi * alias_f * t), color=RED, lw=2.2, ls="--",
              label=f"{alias_f:.0f} Hz (what you get)")
    left.plot(samples_t, np.sin(2 * np.pi * true_f * samples_t), "o",
              color="#333333", ms=7, zorder=5)
    left.axhline(0, color=GRAY, lw=0.7)
    left.set_xlabel("time")
    left.set_yticks([])
    left.legend(fontsize=9.5, loc="upper right")
    left.set_title("Both curves pass through every sample",
                   fontsize=11.5, fontweight="bold")

    # The folding diagram.
    nyquist = 22.05
    inputs = np.linspace(0, 4 * nyquist, 800)
    folded = np.abs(((inputs + nyquist) % (2 * nyquist)) - nyquist)
    right.plot(inputs, folded, color=RED, lw=2.4)
    right.plot([0, nyquist], [0, nyquist], color=GREEN, lw=3.0,
               label="reproduced correctly")
    right.axvline(nyquist, color=GRAY, lw=1.0, ls=":")
    right.text(nyquist * 1.05, 4, "Nyquist\n22.05 kHz", fontsize=9.5, color=GRAY)
    right.set_xlabel("input frequency (kHz)")
    right.set_ylabel("frequency heard (kHz)")
    right.set_xlim(0, 4 * nyquist)
    right.set_ylim(0, nyquist * 1.1)
    right.legend(fontsize=9.5, loc="lower right")
    right.set_title("Everything above Nyquist folds back",
                    fontsize=11.5, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch15-aliasing")


def quantization():
    """Bit depth, and what dither does."""
    use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.0))
    t = np.linspace(0, 1, 1500)
    signal = 0.9 * np.sin(2 * np.pi * 2 * t)

    def quantize(values, bits, dither_amount=0.0, seed=0):
        levels = 2 ** bits
        rng = np.random.default_rng(seed)
        noise = rng.uniform(-0.5, 0.5, values.size) * (2.0 / levels) * dither_amount
        return np.round((values + noise) * levels / 2) / (levels / 2)

    panels = [("3 bits, no dither", quantize(signal, 3), RED),
              ("3 bits, dithered", quantize(signal, 3, dither_amount=1.0), GREEN),
              ("8 bits", quantize(signal, 8), BLUE)]
    for ax, (title, values, colour) in zip(axes, panels):
        ax.plot(t, signal, color=GRAY, lw=1.4, alpha=0.6)
        ax.plot(t, values, color=colour, lw=1.6)
        ax.set_title(title, fontsize=11.5, fontweight="bold", color=colour)
        ax.set_xlabel("time")
        ax.set_yticks([])
        ax.set_ylim(-1.15, 1.15)
    axes[0].set_ylabel("amplitude")
    fig.suptitle("Quantization: dither trades a correlated error for an uncorrelated one",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    save(fig, "ch15-quantization")


def perceptual_coding():
    """What a codec throws away."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    freqs = np.logspace(np.log10(50), np.log10(16000), 900)

    threshold = 3.64 * (freqs / 1000) ** -0.8 - 6.5 * np.exp(
        -0.6 * (freqs / 1000 - 3.3) ** 2) + 1e-3 * (freqs / 1000) ** 4
    ax.plot(freqs, threshold, color=GRAY, lw=2.0, ls="--",
            label="threshold in quiet")

    masker_f, masker_level = 900.0, 72.0
    octaves = np.log2(freqs / masker_f)
    masking = np.where(octaves > 0,
                       masker_level - 11 * octaves,
                       masker_level - 78 * (-octaves))
    combined = np.maximum(masking, threshold)
    ax.plot(freqs, combined, color=RED, lw=2.4, label="masked threshold")
    ax.fill_between(freqs, threshold, combined, where=combined > threshold,
                    color=RED, alpha=0.12)

    rng = np.random.default_rng(6)
    tone_f = np.array([160, 380, 900, 1500, 2600, 4200, 7000, 11000], dtype=float)
    tone_l = np.array([48, 44, 72, 34, 31, 26, 20, 15], dtype=float)
    kept = tone_l > np.interp(tone_f, freqs, combined)
    ax.vlines(tone_f[kept], -10, tone_l[kept], color=GREEN, lw=3.0, label="kept")
    ax.vlines(tone_f[~kept], -10, tone_l[~kept], color=LIGHT, lw=3.0, label="discarded")

    ax.set_xscale("log")
    ax.set_xlim(50, 16000)
    ax.set_ylim(-10, 90)
    ax.set_xticks([100, 250, 500, 1000, 2500, 5000, 10000])
    ax.set_xticklabels(["100", "250", "500", "1k", "2.5k", "5k", "10k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("level (dB SPL)")
    ax.legend(fontsize=9.5, loc="upper right")
    ax.set_title("Perceptual coding: anything under the masked threshold costs no bits",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch15-perceptual-coding")


def synthesis_methods():
    """Three ways to build a spectrum."""
    use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.0), sharey=True)
    n = np.arange(1, 25)
    f0 = 220.0

    # Additive: specify every partial.
    additive = np.array([1.0, 0.0, 0.7, 0.0, 0.45, 0.0, 0.3, 0.2] + [0.0] * 16)
    axes[0].vlines(n * f0, 0, additive, color=BLUE, lw=2.2)
    axes[0].set_title("Additive\nbuild it partial by partial", fontsize=11.5,
                      fontweight="bold", color=BLUE)

    # Subtractive: a rich source through a filter.
    source = 1.0 / n
    cutoff = 1400.0
    filtered = source / np.sqrt(1 + (n * f0 / cutoff) ** 6)
    axes[1].vlines(n * f0, 0, source, color=LIGHT, lw=2.2)
    axes[1].vlines(n * f0, 0, filtered, color=GREEN, lw=2.2)
    axes[1].plot(n * f0, 1.0 / np.sqrt(1 + (n * f0 / cutoff) ** 6),
                 color=GRAY, lw=1.4, ls="--")
    axes[1].set_title("Subtractive\nfilter a rich source", fontsize=11.5,
                      fontweight="bold", color=GREEN)

    # FM: sidebands from one modulator.
    from scipy.special import jv
    index = 4.0
    fm = np.abs(jv(np.arange(0, 24), index))
    axes[2].vlines(n * f0, 0, fm / fm.max(), color=RED, lw=2.2)
    axes[2].set_title("FM\nsidebands from one oscillator", fontsize=11.5,
                      fontweight="bold", color=RED)

    for ax in axes:
        ax.set_xlim(0, 5400)
        ax.set_xlabel("frequency (Hz)")
        ax.set_ylim(0, 1.15)
    axes[0].set_ylabel("amplitude")

    fig.suptitle("Three ways to arrive at a spectrum", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.76)
    save(fig, "ch15-synthesis-methods")


def main():
    print("Chapter 15 figures:")
    polar_patterns()
    sampling()
    aliasing()
    quantization()
    perceptual_coding()
    synthesis_methods()


if __name__ == "__main__":
    main()
