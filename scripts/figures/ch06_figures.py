"""Figures for Chapter 6, The Ear and the Physiology of Hearing."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import Ellipse, FancyArrowPatch, PathPatch

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def ear_anatomy():
    """Trace sound through the ear and across its two impedance boundaries."""
    use_style()
    fig, ax = plt.subplots(figsize=(9.4, 4.25))
    ax.set_xlim(0, 12)
    ax.set_ylim(-1.85, 3.05)
    ax.axis("off")

    # The subtle bands organize the anatomy without pretending that the middle-ear
    # cavity itself is made of bone.  The badges name the medium carrying the signal.
    sections = ((0.15, 4.25, "OUTER EAR", "air pressure", BLUE, "#edf4f9"),
                (4.25, 6.90, "MIDDLE EAR", "bone motion", PURPLE, "#f2eef6"),
                (6.90, 11.85, "INNER EAR", "fluid pressure", GREEN, "#edf6f1"))
    for x0, x1, region, medium, colour, fill in sections:
        ax.add_patch(plt.Rectangle((x0, -1.45), x1 - x0, 3.95,
                                   facecolor=fill, edgecolor="none", zorder=0))
        xc = (x0 + x1) / 2
        ax.text(xc, 2.25, region, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color="#41505c")
        ax.text(xc, 1.88, medium, ha="center", va="center", fontsize=9.2,
                fontweight="bold", color=colour,
                bbox={"boxstyle": "round,pad=0.24", "facecolor": "white",
                      "edgecolor": colour, "linewidth": 0.9})

    # Incoming pressure waves make the direction of the whole story unambiguous.
    for x in (0.36, 0.58, 0.80):
        ax.add_patch(FancyArrowPatch((x, 0.05), (x, 0.85),
                                     connectionstyle="arc3,rad=-0.55",
                                     arrowstyle="-", color=BLUE, lw=1.25))
    ax.add_patch(FancyArrowPatch((0.45, 0.45), (1.28, 0.45), arrowstyle="-|>",
                                 mutation_scale=12, color=BLUE, lw=1.8))
    ax.text(0.62, -0.15, "sound in", ha="center", fontsize=9.2, color=BLUE)

    # Pinna: a recognisable outline with a concha that funnels into the canal.
    pinna_path = Path(
        [(1.62, -0.83), (0.88, -0.78), (0.78, -0.12), (0.93, 0.63),
         (1.05, 1.34), (1.55, 1.62), (2.04, 1.35),
         (2.35, 1.17), (2.27, 0.79), (1.92, 0.54),
         (1.76, 0.38), (1.82, 0.08), (2.02, -0.08),
         (1.92, -0.48), (1.77, -0.73), (1.62, -0.83), (0.0, 0.0)],
        [Path.MOVETO] + [Path.CURVE4] * 15 + [Path.CLOSEPOLY])
    ax.add_patch(PathPatch(pinna_path, facecolor=LIGHT, edgecolor="#38434b", lw=1.35))
    inner_path = Path([(1.42, 1.20), (1.10, 0.83), (1.19, 0.14), (1.73, 0.08),
                       (1.48, 0.82), (1.66, 0.79), (1.88, 0.93), (1.99, 0.68)],
                      [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                       Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
    ax.add_patch(PathPatch(inner_path, fill=False, edgecolor="#667681", lw=1.1))
    ax.text(1.47, -1.12, "pinna", ha="center", fontsize=9.5)

    # Ear canal: gently curved and narrowing toward the membrane.
    canal_path = Path(
        [(1.70, 0.48), (2.40, 0.59), (3.28, 0.55), (4.12, 0.31),
         (4.08, -0.11), (3.22, 0.09), (2.38, 0.08), (1.70, 0.15), (1.70, 0.48)],
        [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
         Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY])
    ax.add_patch(PathPatch(canal_path, facecolor="white", edgecolor="#38434b", lw=1.35))
    ax.add_patch(FancyArrowPatch((2.32, 0.32), (3.54, 0.31), arrowstyle="-|>",
                                 mutation_scale=11, color=BLUE, lw=1.6))
    ax.text(2.95, 0.89, "ear canal · 2.5 cm", ha="center", fontsize=9.5, color=BLUE)
    ax.text(2.95, 0.68, "quarter-wave resonator", ha="center", fontsize=8.4, color=GRAY)

    # Eardrum and malleus.  Their physical attachment is visible instead of implied.
    ax.plot([4.10, 4.30], [-0.17, 0.72], color=RED, lw=3.2,
            solid_capstyle="round", zorder=5)
    ax.plot([4.22, 4.72], [0.27, 0.70], color=PURPLE, lw=2.9,
            solid_capstyle="round", zorder=6)
    ax.add_patch(plt.Circle((4.78, 0.76), 0.14, facecolor="white",
                            edgecolor=PURPLE, lw=2.2, zorder=7))

    # Incus and stapes: simplified silhouettes, but with the three bones distinct.
    ax.plot([4.88, 5.28, 5.55], [0.77, 0.69, 0.32], color=PURPLE, lw=3.0,
            solid_capstyle="round", zorder=6)
    ax.add_patch(plt.Circle((5.18, 0.72), 0.13, facecolor="white",
                            edgecolor=PURPLE, lw=2.2, zorder=7))
    ax.plot([5.55, 5.95], [0.32, 0.32], color=PURPLE, lw=2.5, zorder=6)
    ax.plot([5.93, 6.23, 5.93], [0.32, 0.49, 0.65], color=PURPLE, lw=2.2, zorder=6)
    ax.plot([5.93, 6.30], [0.49, 0.49], color=PURPLE, lw=2.2, zorder=6)

    ax.text(4.72, 1.16, "malleus", ha="center", fontsize=8.2, color=PURPLE)
    ax.text(5.25, 1.02, "incus", ha="center", fontsize=8.2, color=PURPLE)
    ax.text(6.08, 0.91, "stapes", ha="center", fontsize=8.2, color=PURPLE)
    ax.text(5.25, -0.72, "ossicles · 1.3× lever", ha="center", fontsize=9.4,
            fontweight="bold", color=PURPLE)
    ax.add_patch(FancyArrowPatch((4.55, 0.51), (5.78, 0.39), arrowstyle="-|>",
                                 mutation_scale=11, color=PURPLE, lw=1.5,
                                 connectionstyle="arc3,rad=0.13"))

    # The oval window is the second highlighted boundary; the small vestibule
    # makes the connection into the cochlea legible.
    ax.add_patch(Ellipse((6.54, 0.49), 0.18, 0.55, facecolor="white",
                         edgecolor=GREEN, lw=2.7, zorder=6))
    ax.plot([6.63, 7.16], [0.49, 0.49], color=GREEN, lw=2.7,
            solid_capstyle="round")

    # Cochlea, starting at its base on the left and winding inward.
    theta = np.linspace(np.pi, 5.55 * np.pi, 900)
    radius = 1.15 * np.exp(-(theta - np.pi) / 16.5)
    cochlea_x = 8.26 + radius * np.cos(theta)
    cochlea_y = 0.47 + 0.78 * radius * np.sin(theta)
    ax.plot(cochlea_x, cochlea_y, color=GREEN, lw=2.9, solid_capstyle="round")
    ax.add_patch(FancyArrowPatch((7.29, 0.31), (7.82, -0.16), arrowstyle="-|>",
                                 mutation_scale=11, color=GREEN, lw=1.5,
                                 connectionstyle="arc3,rad=-0.28"))
    ax.text(8.30, -0.93, "cochlea · fluid wave", ha="center", fontsize=9.5,
            fontweight="bold", color=GREEN)

    # Several fibres merge into the auditory nerve; orange marks the change from
    # mechanical motion to neural signalling.
    for y0, y1 in ((0.16, 0.55), (0.48, 0.68), (0.78, 0.82)):
        ax.add_patch(FancyArrowPatch((9.10, y0), (9.78, y1), arrowstyle="-",
                                     color=ORANGE, lw=1.2,
                                     connectionstyle="arc3,rad=-0.10"))
    ax.add_patch(FancyArrowPatch((9.74, 0.68), (11.17, 1.21), arrowstyle="-|>",
                                 mutation_scale=14, color=ORANGE, lw=2.1))
    ax.text(10.51, 1.46, "auditory nerve", ha="center", fontsize=9.5,
            fontweight="bold", color=ORANGE)
    ax.text(11.18, 1.05, "neural signal\nto the brain", ha="center", va="top",
            fontsize=8.8, color=ORANGE)

    # Boundary callouts state the physics directly and make the colour coding
    # redundant for readers who cannot distinguish it.
    ax.text(4.20, -1.12, "Eardrum", ha="center", fontsize=9.2,
            fontweight="bold", color=RED)
    ax.text(4.20, -1.36, "AIR → BONE", ha="center", fontsize=8.1, color=RED)
    ax.text(6.55, -1.12, "Oval window", ha="center", fontsize=9.2,
            fontweight="bold", color=GREEN)
    ax.text(6.55, -1.36, "BONE → FLUID", ha="center", fontsize=8.1, color=GREEN)

    ax.set_title("How the ear carries sound across two impedance boundaries",
                 fontsize=13, fontweight="bold", pad=5)
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
