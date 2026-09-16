"""Figures for Chapter 8, Pitch, Beats, Consonance, and Dissonance."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def plomp_levelt(f1, f2, a1=1.0, a2=1.0):
    """Dissonance between two pure tones, after Plomp and Levelt (1965).

    The standard parametrization: dissonance peaks at about a quarter of a
    critical bandwidth apart and falls to nothing when the two tones are either
    identical or more than a critical band apart.
    """
    low, high = np.minimum(f1, f2), np.maximum(f1, f2)
    s = 0.24 / (0.0207 * low + 18.96)
    difference = high - low
    return np.minimum(a1, a2) * (np.exp(-3.5 * s * difference) - np.exp(-5.75 * s * difference))


def beats():
    """Two nearby tones adding to a slowly pulsing envelope."""
    use_style()
    fig, axes = plt.subplots(3, 1, figsize=(8.4, 4.6), sharex=True)
    t = np.linspace(0, 1.0, 4000)
    f1, f2 = 220.0, 223.0

    axes[0].plot(t, np.sin(2 * np.pi * f1 * t), color=BLUE, lw=0.7)
    axes[0].set_ylabel(f"{f1:.0f} Hz", fontsize=10)
    axes[1].plot(t, np.sin(2 * np.pi * f2 * t), color=ORANGE, lw=0.7)
    axes[1].set_ylabel(f"{f2:.0f} Hz", fontsize=10)

    total = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    envelope = 2 * np.abs(np.cos(np.pi * (f2 - f1) * t))
    axes[2].plot(t, total, color=GRAY, lw=0.6)
    axes[2].plot(t, envelope, color=RED, lw=2.2)
    axes[2].plot(t, -envelope, color=RED, lw=2.2)
    axes[2].set_ylabel("sum", fontsize=10)
    axes[2].set_xlabel("time (s)")

    for index in range(int(f2 - f1)):
        axes[2].axvline((index + 0.5) / (f2 - f1), color=GREEN, lw=0.9, ls=":")
    axes[2].text(0.5, 2.55, f"{f2-f1:.0f} beats per second", ha="center",
                 fontsize=11, color=RED, fontweight="bold")

    for ax in axes:
        ax.set_yticks([])
        ax.set_xlim(0, 1.0)
        for side in ("left", "right", "top"):
            ax.spines[side].set_visible(False)
    axes[2].set_ylim(-3.1, 3.1)

    fig.suptitle("Two tones three hertz apart", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.90)
    save(fig, "ch08-beats")


def just_noticeable_difference():
    """How finely the ear resolves pitch, across the range."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.2))

    freqs = np.array([100, 200, 400, 800, 1000, 2000, 4000, 8000], dtype=float)
    # Representative values for trained listeners comparing successive tones.
    jnd_hz = np.array([1.8, 2.0, 2.6, 4.0, 5.0, 11.0, 32.0, 110.0])
    left.plot(freqs, jnd_hz, "-o", color=BLUE, lw=2.2, ms=6)
    left.set_xscale("log")
    left.set_yscale("log")
    left.set_xlabel("frequency (Hz)")
    left.set_ylabel("just-noticeable difference (Hz)")
    left.set_xticks(freqs)
    left.set_xticklabels(["100", "200", "400", "800", "1k", "2k", "4k", "8k"])
    left.set_title("In hertz, it grows steeply", fontsize=12, fontweight="bold")

    cents = 1200 * np.log2(1 + jnd_hz / freqs)
    right.plot(freqs, cents, "-o", color=RED, lw=2.2, ms=6)
    right.axhline(100, color=GRAY, lw=1.0, ls="--")
    right.text(110, 108, "one semitone", fontsize=10, color=GRAY)
    right.set_xscale("log")
    right.set_xlabel("frequency (Hz)")
    right.set_ylabel("just-noticeable difference (cents)")
    right.set_xticks(freqs)
    right.set_xticklabels(["100", "200", "400", "800", "1k", "2k", "4k", "8k"])
    right.set_ylim(0, 130)
    right.set_title("In cents, it is nearly flat below 2 kHz",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch08-jnd")


def missing_fundamental():
    """The same periodicity, with and without energy at the fundamental."""
    use_style()
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 4.2))
    f0 = 200.0
    t = np.linspace(0, 0.02, 2000)
    modes = np.arange(1, 7)

    for column, (keep_from, title, colour) in enumerate((
            (1, "All harmonics present", BLUE),
            (3, "Fundamental and 2nd removed", RED))):
        amplitudes = np.where(modes >= keep_from, 1.0 / modes, 0.0)
        signal = sum(a * np.sin(2 * np.pi * n * f0 * t) for n, a in zip(modes, amplitudes))
        top, bottom = axes[0][column], axes[1][column]
        top.plot(t * 1000, signal, color=colour, lw=1.8)
        for k in range(5):
            top.axvline(k * 1000 / f0, color=GREEN, lw=0.9, ls=":")
        top.set_title(title, fontsize=12, fontweight="bold", color=colour)
        top.set_xlabel("time (ms)")
        top.set_yticks([])
        top.set_xlim(0, 20)

        keep = amplitudes > 0
        bottom.vlines(modes[keep] * f0, 0, amplitudes[keep], color=colour, lw=2.4)
        bottom.plot(modes[keep] * f0, amplitudes[keep], "o", color=colour, ms=5)
        if keep_from > 1:
            bottom.plot([f0, 2 * f0], [0, 0], "x", color=GRAY, ms=10, mew=2)
        bottom.set_xlabel("frequency (Hz)")
        bottom.set_xlim(0, 1400)
        bottom.set_ylim(0, 1.15)
        if column == 0:
            bottom.set_ylabel("amplitude")
        else:
            bottom.set_yticks([])

    fig.suptitle("Both waveforms repeat every 5 ms, so both are heard at 200 Hz",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.86)
    save(fig, "ch08-missing-fundamental")


def roughness_curve():
    """Plomp and Levelt's dissonance curve for two pure tones."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.2, 3.2))
    base = 440.0
    ratios = np.linspace(1.0, 1.35, 700)
    dissonance = plomp_levelt(base, base * ratios)
    ax.plot(1200 * np.log2(ratios), dissonance / dissonance.max(), color=RED, lw=2.4)
    ax.fill_between(1200 * np.log2(ratios), 0, dissonance / dissonance.max(),
                    color=LIGHT, alpha=0.5)
    peak = 1200 * np.log2(ratios[np.argmax(dissonance)])
    ax.axvline(peak, color=GRAY, lw=0.9, ls=":")
    ax.annotate(f"worst at about {peak:.0f} cents", xy=(peak, 0.98),
                xytext=(peak + 40, 0.88), fontsize=10.5, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    ax.text(6, 0.12, "unison:\nno roughness", fontsize=10, color=GREEN)
    ax.text(330, 0.12, "more than a critical band apart:\nheard as two smooth tones",
            fontsize=10, color=BLUE)
    ax.set_xlabel("separation of two pure tones near 440 Hz (cents)")
    ax.set_ylabel("roughness")
    ax.set_yticks([])
    ax.set_xlim(0, 480)
    ax.set_title("Two pure tones: roughness peaks close together, not far apart",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch08-roughness")


def dissonance_curve():
    """Total dissonance between two complex tones, swept across an octave."""
    use_style()
    fig, ax = plt.subplots(figsize=(9.0, 3.8))
    base = 262.0
    n_partials = 6
    partials = np.arange(1, n_partials + 1)
    amplitudes = 0.88 ** partials

    ratios = np.linspace(1.0, 2.02, 1400)
    total = np.zeros_like(ratios)
    for index, ratio in enumerate(ratios):
        a = base * partials
        b = base * ratio * partials
        value = 0.0
        for fa, aa in zip(a, amplitudes):
            for fb, ab in zip(b, amplitudes):
                value += plomp_levelt(fa, fb, aa, ab)
        total[index] = value
    total = total / total.max()
    cents = 1200 * np.log2(ratios)
    ax.plot(cents, total, color=RED, lw=2.2)

    named = [(1/1, "unison"), (6/5, "m3"), (5/4, "M3"), (4/3, "P4"),
             (3/2, "P5"), (5/3, "M6"), (2/1, "octave")]
    for ratio, label in named:
        c = 1200 * np.log2(ratio)
        value = np.interp(c, cents, total)
        ax.plot([c], [value], "o", color=BLUE, ms=7, zorder=5)
        ax.annotate(label, xy=(c, value), xytext=(c, value - 0.13),
                    ha="center", fontsize=10, color=BLUE)
        ax.axvline(c, color=GRAY, lw=0.6, ls=":", zorder=0)

    ax.set_xlabel("interval (cents above the lower note)")
    ax.set_ylabel("total dissonance")
    ax.set_yticks([])
    ax.set_xlim(0, 1200)
    ax.set_ylim(-0.2, 1.05)
    ax.set_xticks([0, 200, 400, 600, 800, 1000, 1200])
    ax.set_title("Two six-partial tones swept through an octave: the minima land on "
                 "the simple ratios",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch08-dissonance-curve")


def main():
    print("Chapter 8 figures:")
    beats()
    just_noticeable_difference()
    missing_fundamental()
    roughness_curve()
    dissonance_curve()


if __name__ == "__main__":
    main()
