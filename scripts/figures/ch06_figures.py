"""Figures for Chapter 6, The Ear and the Physiology of Hearing."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, Polygon, Wedge

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def ear_anatomy():
    """A schematic of the three sections, drawn for the argument rather than for anatomy."""
    use_style()
    fig, ax = plt.subplots(figsize=(9.2, 3.8))
    ax.set_xlim(0, 10.4)
    ax.set_ylim(-1.9, 2.6)
    ax.axis("off")

    # Section bands.
    for x0, x1, label, colour in ((0.2, 3.4, "OUTER EAR\nair", "#e8eef3"),
                                  (3.4, 5.9, "MIDDLE EAR\nbone", "#eae4f0"),
                                  (5.9, 10.2, "INNER EAR\nfluid", "#e4f0ea")):
        ax.add_patch(plt.Rectangle((x0, -1.55), x1 - x0, 3.85,
                                   facecolor=colour, edgecolor="none", zorder=0))
        ax.text((x0 + x1) / 2, 2.05, label, ha="center", fontsize=10.5,
                fontweight="bold", color="#41505c")

    # Pinna: a wedge standing in for the outer ear.
    ax.add_patch(Wedge((0.9, 0.3), 1.0, -80, 80, width=0.34,
                       facecolor=LIGHT, edgecolor="#333333", lw=1.2))
    ax.text(0.85, -1.15, "pinna", ha="center", fontsize=10)

    # Ear canal.
    ax.add_patch(plt.Rectangle((1.25, 0.02), 2.05, 0.56,
                               facecolor="white", edgecolor="#333333", lw=1.2))
    ax.text(2.3, 0.86, "ear canal\n(a stopped pipe, $\\approx2.5$ cm)",
            ha="center", fontsize=10, color=BLUE)

    # Eardrum.
    ax.plot([3.34, 3.34], [-0.12, 0.72], color=RED, lw=3.4)
    ax.text(3.34, -0.62, "eardrum", ha="center", fontsize=10, color=RED)

    # Ossicles: three linked bones, drawn as a lever.
    ax.plot([3.4, 4.3, 5.0, 5.6], [0.35, 0.95, 0.55, 0.35], "-o",
            color=PURPLE, lw=2.6, ms=9)
    ax.text(4.5, 1.38, "hammer, anvil, stirrup\n(a lever)", ha="center",
            fontsize=10, color=PURPLE)

    # Oval window.
    ax.plot([5.72, 5.72], [0.14, 0.56], color=GREEN, lw=3.4)
    ax.text(5.72, -0.62, "oval\nwindow", ha="center", fontsize=10, color=GREEN)

    # Cochlea: a spiral.
    theta = np.linspace(0, 4.6 * np.pi, 800)
    radius = 0.90 * np.exp(-theta / 16)
    ax.plot(7.6 + radius * np.cos(theta), 0.35 + radius * np.sin(theta),
            color=BLUE, lw=2.6)
    ax.plot([5.8, 7.6 + radius[0]], [0.35, 0.35], color=BLUE, lw=2.6)
    ax.text(7.6, -1.15, "cochlea\n(coiled, fluid-filled)", ha="center", fontsize=10, color=BLUE)

    # The auditory nerve leaving.
    ax.add_patch(FancyArrowPatch((8.6, 0.9), (9.9, 1.5), arrowstyle="-|>",
                                 mutation_scale=15, color=ORANGE, lw=2.0))
    ax.text(9.9, 1.72, "to the brain", ha="center", fontsize=10, color=ORANGE)

    ax.text(5.2, -1.82,
            "Sound crosses two boundaries: air to bone at the eardrum, and bone to fluid "
            "at the oval window.",
            ha="center", fontsize=10, color=GRAY)
    ax.set_title("The ear, as three stages of an impedance-matching problem",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch06-ear-anatomy")


def middle_ear_gain():
    """Where the middle ear's pressure gain comes from."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4),
                                      gridspec_kw={"width_ratios": [1.15, 1.0]})

    # Area ratio, drawn to scale.
    eardrum_area, oval_area = 55.0, 3.2       # mm^2
    r_drum = np.sqrt(eardrum_area / np.pi)
    r_oval = np.sqrt(oval_area / np.pi)
    left.add_patch(plt.Circle((-5.0, 0), r_drum, facecolor=LIGHT,
                              edgecolor=RED, lw=2.0))
    left.add_patch(plt.Circle((3.0, 0), r_oval, facecolor=LIGHT,
                              edgecolor=GREEN, lw=2.0))
    left.text(-5.0, -r_drum - 0.7, f"eardrum\n{eardrum_area:.0f} mm$^2$",
              ha="center", va="top", fontsize=10.5, color=RED)
    left.text(3.0, -r_drum - 0.7, f"oval window\n{oval_area:.1f} mm$^2$",
              ha="center", va="top", fontsize=10.5, color=GREEN)
    left.add_patch(FancyArrowPatch((-0.8, 0), (1.6, 0), arrowstyle="-|>",
                                   mutation_scale=16, color="#333333", lw=2.0))
    left.text(0.4, 0.75, f"$\\times{eardrum_area/oval_area:.0f}$", ha="center",
              fontsize=13, fontweight="bold")
    left.set_xlim(-9.5, 6.5)
    left.set_ylim(-7.0, 5.5)
    left.set_aspect("equal")
    left.axis("off")
    left.set_title("The same force, over a much smaller area",
                   fontsize=12, fontweight="bold")

    # The gain budget as a bar chart.
    contributions = [("area ratio\n55 : 3.2", eardrum_area / oval_area, RED),
                     ("ossicular lever\n×1.3", 1.3, PURPLE)]
    total = contributions[0][1] * contributions[1][1]
    labels = [c[0] for c in contributions] + [f"total\n×{total:.0f}"]
    values = [c[1] for c in contributions] + [total]
    colours = [c[2] for c in contributions] + [BLUE]
    right.bar(range(3), values, color=colours, width=0.6)
    for index, value in enumerate(values):
        right.text(index, value + 1.0, f"×{value:.1f}", ha="center",
                   fontsize=11, fontweight="bold")
    right.set_xticks(range(3))
    right.set_xticklabels(labels, fontsize=10)
    right.set_ylabel("pressure gain")
    right.set_ylim(0, 30)
    right.set_title(f"About {20*np.log10(total):.0f} dB of pressure gain",
                    fontsize=12, fontweight="bold")
    for side in ("right", "top"):
        right.spines[side].set_visible(False)

    fig.tight_layout()
    save(fig, "ch06-middle-ear-gain")


def cochlea_map():
    """The basilar membrane unrolled, with the tonotopic map on it."""
    use_style()
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(9.0, 4.6),
                                      gridspec_kw={"height_ratios": [1.0, 1.15]})

    # The unrolled membrane: narrow and stiff at the base, wide and floppy at the apex.
    x = np.linspace(0, 35, 400)
    width = 0.08 + 0.030 * x
    top.fill_between(x, -width, width, color=LIGHT, edgecolor="#333333", lw=1.2)
    top.text(1.0, 1.35, "BASE\nstiff, narrow\nhigh frequencies", fontsize=10,
             color=RED, ha="left", fontweight="bold")
    top.text(34.0, 1.35, "APEX\nfloppy, wide\nlow frequencies", fontsize=10,
             color=BLUE, ha="right", fontweight="bold")
    top.add_patch(FancyArrowPatch((1.2, 0), (3.2, 0), arrowstyle="-|>",
                                  mutation_scale=14, color=GREEN, lw=2.0))
    top.text(2.2, -1.5, "sound enters here", fontsize=10, color=GREEN, ha="center")
    top.set_xlim(-1, 36)
    top.set_ylim(-2.1, 2.5)
    top.axis("off")
    top.set_title("The basilar membrane, unrolled (about 35 mm long)",
                  fontsize=12, fontweight="bold")

    # Greenwood's map: which frequency peaks where.
    distance = np.linspace(0, 35, 400)
    frequency = 165.4 * (10 ** (2.1 * (1 - distance / 35)) - 0.88)
    bottom.plot(distance, frequency, color=BLUE, lw=2.4)
    bottom.set_yscale("log")
    for f, label, colour in ((110, "A2", ORANGE), (440, "A4", GREEN), (3520, "A7", PURPLE)):
        d = 35 * (1 - np.log10(f / 165.4 + 0.88) / 2.1)
        bottom.plot([d], [f], "o", color=colour, ms=8)
        bottom.annotate(f"{label}\n{f} Hz", xy=(d, f), xytext=(d + 1.0, f * 1.5),
                        fontsize=10, color=colour)
    bottom.set_xlabel("distance from the base (mm)")
    bottom.set_ylabel("frequency of maximum response (Hz)")
    bottom.set_xlim(0, 35)
    bottom.set_ylim(20, 20000)
    bottom.set_title("Each place responds best to one frequency",
                     fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch06-cochlea-map")


def travelling_wave():
    """Envelopes of the travelling wave for three frequencies."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.4))
    x = np.linspace(0, 35, 900)

    for f, colour, label in ((4000, RED, "4 kHz"), (1000, GREEN, "1 kHz"), (250, BLUE, "250 Hz")):
        peak = 35 * (1 - np.log10(f / 165.4 + 0.88) / 2.1)
        # Rises gradually, peaks, then cuts off sharply toward the apex.
        envelope = np.exp(-((x - peak) / 7.0) ** 2) * np.where(x > peak, np.exp(-((x - peak) / 3.2) ** 2), 1.0)
        ax.plot(x, envelope, color=colour, lw=2.4, label=label)
        ax.axvline(peak, color=colour, lw=0.8, ls=":")
    ax.set_xlabel("distance from the base (mm)")
    ax.set_ylabel("displacement envelope")
    ax.set_yticks([])
    ax.set_xlim(0, 35)
    ax.legend(fontsize=10.5, loc="upper left")
    ax.set_title("A travelling wave builds gradually, peaks, and stops abruptly",
                 fontsize=12, fontweight="bold")
    ax.text(18.0, 0.18, "the sharp apex-side cut-off is why a loud low tone\n"
                        "masks a quiet high one far more than the reverse",
            fontsize=9.5, color=GRAY)
    fig.tight_layout()
    save(fig, "ch06-travelling-wave")


def hearing_loss():
    """Threshold shift with age, and safe exposure times."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4))

    freqs = np.array([125, 250, 500, 1000, 2000, 4000, 8000])
    curves = {
        "age 20": np.array([0, 0, 0, 0, 0, 0, 2]),
        "age 40": np.array([2, 2, 3, 4, 6, 12, 18]),
        "age 60": np.array([5, 6, 8, 10, 18, 32, 45]),
    }
    for (label, shift), colour in zip(curves.items(), (BLUE, GREEN, RED)):
        left.plot(freqs, -shift, "-o", color=colour, lw=2.0, ms=5, label=label)
    left.set_xscale("log")
    left.set_xticks(freqs)
    left.set_xticklabels(["125", "250", "500", "1k", "2k", "4k", "8k"])
    left.set_xlabel("frequency (Hz)")
    left.set_ylabel("hearing level (dB)")
    left.set_ylim(-60, 8)
    left.legend(fontsize=10)
    left.set_title("Typical threshold shift with age", fontsize=12, fontweight="bold")

    levels = np.array([85, 88, 91, 94, 97, 100, 103, 106, 109, 112])
    hours = 8.0 / 2 ** ((levels - 85) / 3.0)
    right.plot(levels, hours, "-o", color=RED, lw=2.2, ms=5)
    right.set_yscale("log")
    right.set_xlabel("sound level (dB A)")
    right.set_ylabel("safe exposure per day (hours)")
    right.set_yticks([0.01, 0.1, 1, 8])
    right.set_yticklabels(["36 s", "6 min", "1 h", "8 h"])
    for level, note, colour in ((85, "busy street", BLUE),
                                (100, "orchestra pit", ORANGE),
                                (112, "front row,\nrock concert", PURPLE)):
        h = 8.0 / 2 ** ((level - 85) / 3.0)
        right.plot([level], [h], "o", color=colour, ms=9)
        right.annotate(note, xy=(level, h), xytext=(level - 12, h * 2.4),
                       fontsize=9.5, color=colour)
    right.set_title("Every 3 dB halves the safe time",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch06-hearing-loss")


def main():
    print("Chapter 6 figures:")
    ear_anatomy()
    middle_ear_gain()
    cochlea_map()
    travelling_wave()
    hearing_loss()


if __name__ == "__main__":
    main()
