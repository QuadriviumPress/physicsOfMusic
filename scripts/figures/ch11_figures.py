"""Figures for Chapter 11, Wind Instruments and Air-Column Resonance."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def bore_shapes():
    """Three bores and the harmonic series each supports."""
    use_style()
    fig, axes = plt.subplots(3, 2, figsize=(9.4, 5.0),
                             gridspec_kw={"width_ratios": [1.0, 1.35]})
    x = np.linspace(0, 1, 500)

    rows = [
        ("Open cylinder\n(flute)", "cylinder", False, [1, 2, 3, 4, 5, 6], BLUE),
        ("Stopped cylinder\n(clarinet)", "cylinder", True, [1, 3, 5, 7, 9, 11], RED),
        ("Cone\n(oboe, saxophone)", "cone", True, [1, 2, 3, 4, 5, 6], GREEN),
    ]

    for row, (label, shape, stopped, harmonics, colour) in enumerate(rows):
        left, right = axes[row][0], axes[row][1]

        if shape == "cylinder":
            profile = np.full_like(x, 0.28)
        else:
            profile = 0.04 + 0.30 * x
        left.fill_between(x, -profile, profile, color=LIGHT, edgecolor="#333333", lw=1.4)
        if stopped and shape == "cylinder":
            left.plot([0, 0], [-0.32, 0.32], color="#333333", lw=4)
        left.set_xlim(-0.06, 1.06)
        left.set_ylim(-0.42, 0.42)
        left.axis("off")
        left.text(0.5, -0.40, label, ha="center", va="top", fontsize=10.5,
                  color=colour, fontweight="bold")

        base = 150.0
        freqs = np.array(harmonics) * base
        right.vlines(freqs, 0, 1.0 / np.sqrt(np.array(harmonics)), color=colour, lw=2.4)
        right.plot(freqs, 1.0 / np.sqrt(np.array(harmonics)), "o", color=colour, ms=5)
        for f, h in zip(freqs, harmonics):
            right.text(f, 1.06 / np.sqrt(h), f"{h}", ha="center", fontsize=9.5, color=colour)
        right.set_xlim(0, 1900)
        right.set_ylim(0, 1.3)
        right.set_yticks([])
        if row == 2:
            right.set_xlabel("frequency (Hz)")
        else:
            right.set_xticklabels([])
        right.text(0.99, 0.82, "overblows to " + ("an octave" if harmonics[1] == 2 else "a twelfth"),
                   transform=right.transAxes, ha="right", fontsize=10, color=colour)

    fig.suptitle("Bore shape decides which harmonics exist",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.91)
    save(fig, "ch11-bore-shapes")


def end_correction():
    """How much longer a pipe sounds than it measures."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.2))

    x = np.linspace(-0.25, 1.35, 500)
    left.fill_between(np.linspace(0, 1, 200), -0.16, 0.16, color=LIGHT,
                      edgecolor="#333333", lw=1.4)
    left.plot(x, 0.30 * np.cos(np.pi * (x - 0.0) / 1.22), color=RED, lw=2.2)
    left.axvline(0.0, color=GRAY, lw=0.9, ls=":")
    left.axvline(1.0, color=GRAY, lw=0.9, ls=":")
    left.axvline(1.22, color=RED, lw=1.2, ls="--")
    left.annotate("", xy=(1.0, -0.36), xytext=(1.22, -0.36),
                  arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
    left.text(1.11, -0.46, "$\\Delta L \\approx 0.6r$", ha="center", fontsize=11, color=RED)
    left.text(0.5, 0.42, "physical length $L$", ha="center", fontsize=10.5)
    left.text(1.22, 0.42, "where the antinode\nreally is", ha="center",
              fontsize=10, color=RED)
    left.set_xlim(-0.3, 1.6)
    left.set_ylim(-0.6, 0.62)
    left.axis("off")
    left.set_title("The antinode sits outside the tube", fontsize=12, fontweight="bold")

    # Fractional pitch error from ignoring it, against bore-to-length ratio.
    ratio = np.linspace(0.005, 0.20, 300)     # radius / length
    cents_error = -1200 * np.log2(1 / (1 + 2 * 0.6 * ratio))
    right.plot(ratio, cents_error, color=BLUE, lw=2.4)
    right.axhline(5, color=GRAY, lw=1.0, ls="--")
    right.text(0.006, 8, "5 cents", fontsize=9.5, color=GRAY)
    for r, label, colour in ((0.012, "organ pipe,\nnarrow", GREEN),
                             (0.055, "flute", ORANGE),
                             (0.14, "a wide\nstopped pipe", RED)):
        value = -1200 * np.log2(1 / (1 + 2 * 0.6 * r))
        right.plot([r], [value], "o", color=colour, ms=8)
        right.annotate(f"{label}\n{value:.0f} cents", xy=(r, value),
                       xytext=(r + 0.008, value + 14), fontsize=9.5, color=colour)
    right.set_xlabel("bore radius / pipe length")
    right.set_ylabel("pitch error if ignored (cents)")
    right.set_xlim(0, 0.2)
    right.set_title("Wide pipes cannot ignore it", fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch11-end-correction")


def reed_valve():
    """The reed as a pressure-controlled valve, and the feedback loop."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.2),
                                      gridspec_kw={"width_ratios": [1.1, 1.0]})

    # Schematic: mouth, reed, bore.
    left.add_patch(plt.Rectangle((0.0, -0.45), 1.1, 0.9, facecolor="#f2e8e8",
                                 edgecolor="none"))
    left.text(0.55, 0.62, "mouth\n(steady pressure)", ha="center", fontsize=10, color=RED)
    left.add_patch(plt.Rectangle((1.6, -0.22), 3.4, 0.44, facecolor=LIGHT,
                                 edgecolor="#333333", lw=1.4))
    left.text(3.3, 0.62, "bore (the resonator)", ha="center", fontsize=10, color=BLUE)
    # The reed itself.
    left.plot([1.15, 1.6], [0.30, 0.20], color=PURPLE, lw=4)
    left.plot([1.15, 1.6], [-0.30, -0.20], color=PURPLE, lw=4, alpha=0.4)
    left.text(1.37, -0.62, "reed", ha="center", fontsize=10.5, color=PURPLE)
    left.add_patch(FancyArrowPatch((0.6, 0.0), (1.1, 0.0), arrowstyle="-|>",
                                   mutation_scale=14, color=RED, lw=2.0))
    # The feedback arrow, which is the whole point.
    left.add_patch(FancyArrowPatch((4.6, -0.42), (1.5, -0.42),
                                   arrowstyle="-|>", mutation_scale=14, color=GREEN,
                                   lw=2.0, connectionstyle="arc3,rad=0.28"))
    left.text(3.0, -0.95, "the bore's reflected pressure wave\ntells the reed when to close",
              ha="center", fontsize=10, color=GREEN)
    left.set_xlim(-0.2, 5.4)
    left.set_ylim(-1.3, 0.95)
    left.axis("off")
    left.set_title("A pressure-controlled valve", fontsize=12, fontweight="bold")

    # Why the resonator wins: bore impedance peaks pick the frequency.
    freqs = np.linspace(50, 1400, 1400)
    impedance = np.zeros_like(freqs)
    for n in (1, 3, 5, 7, 9):
        impedance += (1.0 / n ** 0.6) / np.sqrt(
            (1 - (freqs / (147 * n)) ** 2) ** 2 + (freqs / (147 * n * 28)) ** 2)
    right.plot(freqs, impedance / impedance.max(), color=BLUE, lw=2.0)
    right.set_xlabel("frequency (Hz)")
    right.set_ylabel("input impedance of the bore")
    right.set_yticks([])
    right.set_xlim(0, 1400)
    right.annotate("the reed oscillates at a peak,\nnot at its own natural frequency",
                   xy=(147, 1.0), xytext=(330, 0.72), fontsize=10, color=RED,
                   arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    right.set_title("The bore's impedance peaks", fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch11-reed-valve")


def brass_resonances():
    """A trumpet's resonances before and after the bell and mouthpiece do their work."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.8, 3.6))

    n = np.arange(2, 11)
    ideal = n * 116.5
    # A plain cylinder of the same length would give odd multiples of a quarter-wave;
    # the flare and mouthpiece pull the peaks onto a harmonic series from the 2nd up.
    plain = (2 * np.arange(1, 10) - 1) * 58.25
    ax.plot(n, ideal, "-o", color=GREEN, lw=2.2, ms=7,
            label="a real trumpet: nearly harmonic from the 2nd")
    ax.plot(n, plain, "-o", color=RED, lw=2.2, ms=7, ls="--",
            label="a plain cylinder of the same length")
    for index, value in zip(n, ideal):
        ax.annotate(f"{index}", xy=(index, value), xytext=(index, value + 45),
                    ha="center", fontsize=9.5, color=GREEN)
    ax.set_xlabel("resonance number")
    ax.set_ylabel("frequency (Hz)")
    ax.legend(fontsize=10, loc="upper left")
    ax.set_title("What the mouthpiece and bell are for",
                 fontsize=12, fontweight="bold")
    ax.text(6.4, 200,
            "The player selects a resonance with their lips. Only a harmonic set\n"
            "gives the familiar bugle notes; a plain tube would give a different scale.",
            fontsize=9.5, color=GRAY)
    fig.tight_layout()
    save(fig, "ch11-brass-resonances")


def bell_behaviour():
    """A bell reflects low frequencies and radiates high ones."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    freqs = np.logspace(np.log10(60), np.log10(6000), 500)
    cutoff = 800.0
    reflected = 1.0 / (1.0 + (freqs / cutoff) ** 3)
    ax.plot(freqs, reflected, color=BLUE, lw=2.4, label="reflected back into the bore")
    ax.plot(freqs, 1 - reflected, color=RED, lw=2.4, label="radiated into the room")
    ax.axvline(cutoff, color=GRAY, lw=1.0, ls=":")
    ax.text(cutoff * 1.08, 0.5, "cut-off\nfrequency", fontsize=10, color=GRAY)
    ax.set_xscale("log")
    ax.set_xlim(60, 6000)
    ax.set_xticks([100, 200, 500, 1000, 2000, 5000])
    ax.set_xticklabels(["100", "200", "500", "1k", "2k", "5k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("fraction")
    ax.legend(fontsize=10, loc="center right")
    ax.set_title("The bell: a reflector below, a loudspeaker above",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch11-bell-behaviour")


def main():
    print("Chapter 11 figures:")
    bore_shapes()
    end_correction()
    reed_valve()
    brass_resonances()
    bell_behaviour()


if __name__ == "__main__":
    main()
