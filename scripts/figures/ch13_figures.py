"""Figures for Chapter 13, The Singing Voice."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style

# First three formant frequencies (Hz) for a few vowels, adult male ranges.
VOWELS = {
    "ee (heed)": (280, 2250, 2890),
    "eh (head)": (530, 1840, 2480),
    "ah (hard)": (730, 1090, 2440),
    "aw (hawed)": (570, 840, 2410),
    "oo (who)": (300, 870, 2240),
}


def tract_filter(freqs, formants, bandwidths=(80, 110, 160)):
    """The vocal tract's transfer function: a product of resonances."""
    response = np.ones_like(freqs)
    for centre, width in zip(formants, bandwidths):
        response = response * (centre ** 2) / np.sqrt(
            (centre ** 2 - freqs ** 2) ** 2 + (freqs * width) ** 2)
    return response


def source_filter():
    """Source spectrum, times filter, gives output."""
    use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.8, 3.0))
    f0 = 120.0
    n = np.arange(1, 41)
    partials = n * f0
    freqs = np.linspace(20, 5000, 2000)
    formants = VOWELS["ah (hard)"]

    source = 1.0 / n ** 1.2
    axes[0].vlines(partials, 0, source, color=RED, lw=1.8)
    axes[0].set_title("Source\nthe vocal folds", fontsize=11.5, fontweight="bold", color=RED)
    axes[0].set_ylabel("amplitude")

    def db(values):
        return 20 * np.log10(values / values.max())

    response = tract_filter(freqs, formants)
    axes[1].plot(freqs, db(response), color=BLUE, lw=2.2)
    for index, centre in enumerate(formants):
        axes[1].axvline(centre, color=GRAY, lw=0.7, ls=":")
        axes[1].text(centre, 3, f"$F_{index+1}$", ha="center", fontsize=10.5, color=BLUE)
    axes[1].set_title("Filter\nthe vocal tract", fontsize=11.5, fontweight="bold", color=BLUE)

    output = source * tract_filter(partials, formants)
    axes[2].vlines(partials, -60, db(output), color=PURPLE, lw=1.8)
    smooth = tract_filter(freqs, formants) * (f0 / freqs) ** 1.2
    axes[2].plot(freqs, db(smooth), color=GRAY, lw=1.2, ls="--")
    axes[2].set_title("Output\nthe vowel 'ah'", fontsize=11.5, fontweight="bold", color=PURPLE)

    axes[0].set_ylim(0, 1.15)
    axes[0].set_yticks([])
    for ax in axes[1:]:
        ax.set_ylim(-60, 8)
        ax.set_ylabel("level (dB)")
    for ax in axes:
        ax.set_xlim(0, 4200)
        ax.set_xlabel("frequency (Hz)")

    fig.suptitle("The source-filter model: a harmonic source shaped by fixed resonances",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.74)
    save(fig, "ch13-source-filter")


def glottal_cycle():
    """One cycle of vocal fold oscillation, and the flow it produces."""
    use_style()
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.6, 4.0), sharex=True,
                                      gridspec_kw={"height_ratios": [1.0, 1.1]})

    t = np.linspace(0, 2, 900)
    phase = t % 1.0
    # Glottal area: opens smoothly, closes abruptly, then stays shut.
    area = np.where(phase < 0.62,
                    np.sin(np.pi * phase / 0.62) ** 2,
                    0.0)
    top.plot(t, area, color=BLUE, lw=2.2)
    top.fill_between(t, 0, area, color=LIGHT, alpha=0.6)
    top.set_ylabel("glottal area")
    top.set_yticks([])
    top.text(0.31, 1.06, "open", ha="center", fontsize=10.5, color=BLUE)
    top.text(0.81, 0.12, "closed", ha="center", fontsize=10.5, color=RED)

    flow = area ** 1.1
    derivative = np.gradient(flow, t)
    bottom.plot(t, derivative / np.max(np.abs(derivative)), color=RED, lw=2.0)
    bottom.axhline(0, color=GRAY, lw=0.8)
    bottom.set_ylabel("rate of change of flow")
    bottom.set_yticks([])
    bottom.set_xlabel("time (periods)")
    bottom.annotate("the sharp closure is what makes the sound",
                    xy=(0.60, -0.95), xytext=(0.95, -0.55), fontsize=10.5, color=RED,
                    arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))

    for ax in (top, bottom):
        ax.set_xlim(0, 2)
        for side in ("right", "top"):
            ax.spines[side].set_visible(False)

    fig.suptitle("One glottal cycle: a slow opening and a fast closing",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.89)
    save(fig, "ch13-glottal-cycle")


def vowel_chart():
    """Vowels in the F1-F2 plane."""
    use_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.2))

    for (name, (f1, f2, _)), colour in zip(VOWELS.items(), (BLUE, GREEN, RED, ORANGE, PURPLE)):
        ax.plot([f2], [f1], "o", color=colour, ms=13)
        ax.annotate(name, xy=(f2, f1), xytext=(f2 + 60, f1 + 22),
                    fontsize=11, color=colour, fontweight="bold")

    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.set_xlabel("second formant $F_2$ (Hz)   ← back        front →")
    ax.set_ylabel("first formant $F_1$ (Hz)\n← close        open →")
    ax.set_title("Vowels live in a two-dimensional space",
                 fontsize=12, fontweight="bold")
    ax.text(2400, 760,
            "$F_1$ tracks how open the jaw is;\n$F_2$ tracks how far forward the tongue is.",
            fontsize=10, color=GRAY)
    fig.tight_layout()
    save(fig, "ch13-vowel-chart")


def formant_tuning():
    """Why a soprano cannot be understood at the top of her range."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.4), sharey=True)
    freqs = np.linspace(20, 4000, 1600)
    formants = VOWELS["ah (hard)"]
    envelope = tract_filter(freqs, formants)
    envelope = envelope / envelope.max()

    for ax, f0, title, colour in ((left, 220.0, "At 220 Hz: the formants are well sampled", GREEN),
                                  (right, 880.0, "At 880 Hz: $F_1$ falls in a gap", RED)):
        ax.plot(freqs, envelope, color=GRAY, lw=2.0, ls="--")
        n = np.arange(1, int(4000 / f0) + 1)
        partials = n * f0
        amps = tract_filter(partials, formants) / tract_filter(freqs, formants).max() / n ** 0.5
        ax.vlines(partials, 0, amps / amps.max(), color=colour, lw=2.6)
        ax.plot(partials, amps / amps.max(), "o", color=colour, ms=5)
        ax.axvline(formants[0], color=BLUE, lw=1.0, ls=":")
        ax.set_xlabel("frequency (Hz)")
        ax.set_xlim(0, 4000)
        ax.set_ylim(0, 1.2)
        ax.set_title(title, fontsize=11.5, fontweight="bold", color=colour)
    left.set_ylabel("amplitude")
    left.set_yticks([])
    right.annotate("no harmonic near $F_1$,\nso the vowel is lost",
                   xy=(formants[0], 0.15), xytext=(1200, 0.62), fontsize=10, color=RED,
                   arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))

    fig.suptitle("The same vowel at two pitches", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    save(fig, "ch13-formant-tuning")


def singers_formant():
    """How a soloist is heard over an orchestra."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    freqs = np.linspace(50, 6000, 2000)

    def bump(centre, width, height_db):
        """A resonance peak of the given height in dB."""
        return height_db / (1 + ((freqs - centre) / width) ** 2)

    # Levels are set explicitly rather than by normalizing each curve to its own
    # maximum: the whole point is where the voice sits *relative to the
    # orchestra*, and normalizing separately destroys exactly that comparison.
    orchestra = -6 - 13 * np.log2(np.maximum(freqs, 300) / 300.0)
    ax.plot(freqs, orchestra, color=GRAY, lw=2.4, label="orchestra")
    ax.fill_between(freqs, -60, orchestra, color=LIGHT, alpha=0.5)

    # Both voices: a source falling about 12 dB per octave, with formants on top.
    tilt = -12 * np.log2(np.maximum(freqs, 200) / 200.0)
    formant_peaks = bump(600, 90, 16) + bump(1100, 130, 12)
    untrained = tilt + formant_peaks + bump(2500, 220, 6)
    trained = tilt + formant_peaks + bump(2900, 280, 30)

    ax.plot(freqs, untrained, color=BLUE, lw=2.2, label="untrained voice")
    ax.plot(freqs, trained, color=RED, lw=2.4,
            label="trained voice, with singer's formant")

    ax.axvspan(2400, 3400, color=RED, alpha=0.07)
    ax.annotate("the singer's formant rises above the orchestra\nin the one band the ear "
                "is most sensitive to",
                xy=(2900, -20), xytext=(3250, -44), fontsize=10.5, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    ax.set_xlim(50, 6000)
    ax.set_ylim(-60, 6)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("level (dB)")
    ax.legend(fontsize=10, loc="lower left")
    ax.set_title("Being heard: the orchestra's spectrum and the voice's",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch13-singers-formant")


def main():
    print("Chapter 13 figures:")
    source_filter()
    glottal_cycle()
    vowel_chart()
    formant_tuning()
    singers_formant()


if __name__ == "__main__":
    main()
