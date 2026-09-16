"""Figures for Chapter 7, Loudness, Decibels, and the Equal-Loudness Contours."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style

# ISO 226:2003 parameters. `af` is the exponent of loudness perception at each
# frequency, `Lu` the transfer function relative to 1 kHz, and `Tf` the threshold
# of hearing. Cited in SOURCES.md; the curves below are computed from these
# rather than traced from a published figure.
ISO_F = np.array([20, 25, 31.5, 40, 50, 63, 80, 100, 125, 160, 200, 250, 315,
                  400, 500, 630, 800, 1000, 1250, 1600, 2000, 2500, 3150, 4000,
                  5000, 6300, 8000, 10000, 12500], dtype=float)
ISO_AF = np.array([0.532, 0.506, 0.480, 0.455, 0.432, 0.409, 0.387, 0.367, 0.349,
                   0.330, 0.315, 0.301, 0.288, 0.276, 0.267, 0.259, 0.253, 0.250,
                   0.246, 0.244, 0.243, 0.243, 0.243, 0.242, 0.242, 0.245, 0.254,
                   0.271, 0.301])
ISO_LU = np.array([-31.6, -27.2, -23.0, -19.1, -15.9, -13.0, -10.3, -8.1, -6.2,
                   -4.5, -3.1, -2.0, -1.1, -0.4, 0.0, 0.3, 0.5, 0.0, -2.7, -4.1,
                   -1.0, 1.7, 2.5, 1.2, -2.1, -7.1, -11.2, -10.7, -3.1])
ISO_TF = np.array([78.5, 68.7, 59.5, 51.1, 44.0, 37.5, 31.5, 26.5, 22.1, 17.9,
                   14.4, 11.4, 8.6, 6.2, 4.4, 3.0, 2.2, 2.4, 3.5, 1.7, -1.3,
                   -4.2, -6.0, -5.4, -1.5, 6.0, 12.6, 13.9, 12.3])


def equal_loudness_spl(phon):
    """Sound pressure level, at each ISO frequency, of a tone of the given loudness level."""
    af, lu, tf = ISO_AF, ISO_LU, ISO_TF
    a = 4.47e-3 * (10 ** (0.025 * phon) - 1.15) + (0.4 * 10 ** ((tf + lu) / 10 - 9)) ** af
    return (10 / af) * np.log10(a) - lu + 94


def equal_loudness_contours():
    """The ISO 226 contours, and what they mean for quiet listening."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 4.6))

    # ISO 226:2003 is specified over 20-90 phon; 100 would be an extrapolation.
    for phon, colour in zip((10, 20, 40, 60, 80, 90),
                            (LIGHT, "#a8b8c8", BLUE, GREEN, ORANGE, RED)):
        spl = equal_loudness_spl(phon)
        ax.plot(ISO_F, spl, color=colour, lw=2.0)
        ax.annotate(f"{phon} phon", xy=(ISO_F[-4], spl[-4]),
                    xytext=(ISO_F[-4] * 1.15, spl[-4] + 2.5),
                    fontsize=9.5, color=colour if phon > 20 else GRAY)

    threshold = equal_loudness_spl(0)
    ax.plot(ISO_F, threshold, color="#333333", lw=2.2, ls="--")
    ax.annotate("threshold of hearing", xy=(70, threshold[5]),
                xytext=(26, 46), fontsize=10, color="#333333")

    ax.axvline(1000, color=GRAY, lw=0.8, ls=":")
    ax.text(1050, 108, "at 1 kHz, phons\nequal dB SPL", fontsize=9.5, color=GRAY)

    ax.set_xscale("log")
    ax.set_xlim(20, 12500)
    ax.set_ylim(-10, 120)
    ax.set_xticks([20, 50, 100, 250, 500, 1000, 2500, 5000, 10000])
    ax.set_xticklabels(["20", "50", "100", "250", "500", "1k", "2.5k", "5k", "10k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("sound pressure level (dB SPL)")
    ax.set_title("Equal-loudness contours (ISO 226): every point on a curve sounds equally loud",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch07-equal-loudness")


def bass_loss_when_quiet():
    """Why turning music down takes the bass away first."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    loud = equal_loudness_spl(80)
    quiet = equal_loudness_spl(30)
    # Referenced to 1 kHz, so the curves show relative sensitivity rather than level.
    reference = list(ISO_F).index(1000)
    ax.plot(ISO_F, -(loud - loud[reference]), color=RED, lw=2.4, label="playing loud (80 phon)")
    ax.plot(ISO_F, -(quiet - quiet[reference]), color=BLUE, lw=2.4, label="playing quietly (30 phon)")
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.fill_between(ISO_F, -(loud - loud[reference]), -(quiet - quiet[reference]),
                    where=ISO_F < 500, color=LIGHT, alpha=0.6)
    ax.annotate("the bass you lose\nby turning it down", xy=(60, -20),
                xytext=(24, -40), fontsize=10, color=PURPLE,
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.2))
    ax.set_xscale("log")
    ax.set_xlim(20, 12500)
    ax.set_xticks([20, 50, 100, 250, 500, 1000, 2500, 5000, 10000])
    ax.set_xticklabels(["20", "50", "100", "250", "500", "1k", "2.5k", "5k", "10k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("sensitivity relative to 1 kHz (dB)")
    ax.legend(fontsize=10, loc="lower center")
    ax.set_title("The ear's frequency response changes with level",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch07-bass-loss")


def decibel_scale():
    """The range of levels, with musical and everyday landmarks."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 4.4))
    entries = [
        (0, "threshold of hearing", GRAY),
        (20, "recording studio, empty", GRAY),
        (40, "quiet library", BLUE),
        (60, "conversation at 1 m", BLUE),
        (75, "violin, practice level", GREEN),
        (85, "eight-hour exposure limit", ORANGE),
        (95, "orchestra, fortissimo (audience)", ORANGE),
        (105, "orchestra pit, brass section", RED),
        (115, "rock concert, front row", RED),
        (130, "threshold of pain", RED),
    ]
    for level, label, colour in entries:
        ax.barh(level, 1, height=2.6, color=colour, alpha=0.85)
        ax.text(1.06, level, f"{level} dB   {label}", va="center", fontsize=10.5, color=colour)
    ax.axhspan(85, 130, color=RED, alpha=0.06)
    ax.text(0.5, 128, "hearing damage accumulates", fontsize=10, color=RED,
            ha="center", style="italic")

    secondary = ax.twinx()
    secondary.set_ylim(0, 135)
    secondary.set_yticks([0, 30, 60, 90, 120])
    secondary.set_yticklabels(["$10^{-12}$", "$10^{-9}$", "$10^{-6}$", "$10^{-3}$", "$10^{0}$"])
    secondary.set_ylabel("intensity (W/m$^2$)")

    ax.set_ylim(0, 135)
    ax.set_xlim(0, 6)
    ax.set_xticks([])
    ax.set_ylabel("sound pressure level (dB SPL)")
    ax.set_title("Twelve orders of magnitude, on one scale", fontsize=12, fontweight="bold")
    for side in ("top", "bottom"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "ch07-decibel-scale")


def adding_sources():
    """Combining incoherent sources, and why more players is not much louder."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4))

    n = np.arange(1, 65)
    level = 10 * np.log10(n)
    left.plot(n, level, color=BLUE, lw=2.4)
    for count, colour in ((1, GRAY), (2, GREEN), (10, ORANGE), (60, RED)):
        left.plot([count], [10 * np.log10(count)], "o", color=colour, ms=8)
        left.annotate(f"{count} → +{10*np.log10(count):.0f} dB",
                      xy=(count, 10 * np.log10(count)),
                      xytext=(count * 1.15, 10 * np.log10(count) - 2.6),
                      fontsize=10, color=colour)
    left.set_xscale("log")
    left.set_xlabel("number of identical, independent sources")
    left.set_ylabel("level above one source (dB)")
    left.set_xticks([1, 2, 5, 10, 20, 60])
    left.set_xticklabels(["1", "2", "5", "10", "20", "60"])
    left.set_title("Adding incoherent sources", fontsize=12, fontweight="bold")

    # Loudness in sones against loudness level in phons.
    phons = np.linspace(20, 110, 300)
    sones = 2 ** ((phons - 40) / 10)
    right.plot(phons, sones, color=RED, lw=2.4)
    right.set_yscale("log")
    for phon in (40, 50, 60, 80):
        right.plot([phon], [2 ** ((phon - 40) / 10)], "o", color=BLUE, ms=6)
        right.annotate(f"{2 ** ((phon - 40) / 10):g} sone",
                       xy=(phon, 2 ** ((phon - 40) / 10)),
                       xytext=(phon - 16, 2 ** ((phon - 40) / 10) * 1.5),
                       fontsize=9.5, color=BLUE)
    right.set_xlabel("loudness level (phon)")
    right.set_ylabel("loudness (sone)")
    right.set_title("Ten phons doubles the loudness", fontsize=12, fontweight="bold")
    right.set_xlim(20, 110)

    fig.tight_layout()
    save(fig, "ch07-adding-and-sones")


def masking():
    """A masking pattern, and the asymmetry it inherits from the cochlea."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.6))

    masker = 400.0
    freqs = np.logspace(np.log10(80), np.log10(8000), 700)
    octaves = np.log2(freqs / masker)
    for level, colour in ((80, RED), (60, ORANGE), (40, BLUE)):
        # Shallow on the high side, steep on the low side, and shallower still
        # at higher masker levels -- the standard shape.
        upward_slope = 27 - 0.23 * level
        spread = np.where(octaves > 0,
                          level - upward_slope * octaves,
                          level - 90 * (-octaves))
        pattern = np.maximum(spread, equal_loudness_spl(0).min())
        ax.plot(freqs, pattern, color=colour, lw=2.2, label=f"masker at {level} dB")
    ax.axvline(masker, color=GRAY, lw=1.0, ls=":")
    ax.text(masker * 1.06, 86, "masker\n400 Hz", fontsize=10, color=GRAY)
    ax.annotate("masking spreads upward\nfar more than downward",
                xy=(2200, 34), xytext=(900, 62), fontsize=10, color=PURPLE,
                arrowprops=dict(arrowstyle="->", color=PURPLE, lw=1.2))
    ax.set_xscale("log")
    ax.set_xlim(80, 8000)
    ax.set_ylim(0, 95)
    ax.set_xticks([100, 200, 400, 800, 1600, 3200, 6400])
    ax.set_xticklabels(["100", "200", "400", "800", "1.6k", "3.2k", "6.4k"])
    ax.set_xlabel("frequency of the masked tone (Hz)")
    ax.set_ylabel("level needed to be heard (dB SPL)")
    ax.legend(fontsize=10, loc="upper right")
    ax.set_title("Masking patterns of a 400 Hz tone", fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch07-masking")


def main():
    print("Chapter 7 figures:")
    equal_loudness_contours()
    bass_loss_when_quiet()
    decibel_scale()
    adding_sources()
    masking()


if __name__ == "__main__":
    main()
