"""Figures for Chapter 12, Percussion: Membranes, Bars, and Plates."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style

# Frequency ratios of the transverse modes of a uniform free-free bar. These are
# the squares of the roots of cos(x)cosh(x) = 1, normalized to the first.
BAR_RATIOS = np.array([1.000, 2.756, 5.404, 8.933, 13.345])


def bar_modes():
    """A free-free bar's modes are not harmonic, and undercutting fixes the second."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.6))

    x = np.arange(len(BAR_RATIOS))
    width = 0.36
    tuned = np.array([1.0, 4.0, 10.0, 8.933, 13.345])
    left.bar(x - width / 2, BAR_RATIOS, width, color=RED, label="plain bar")
    left.bar(x[:3] + width / 2, tuned[:3], width, color=GREEN, label="undercut bar")
    for index, (plain, cut) in enumerate(zip(BAR_RATIOS[:3], tuned[:3])):
        left.text(index - width / 2, plain + 0.4, f"{plain:.2f}", ha="center", fontsize=10)
        left.text(index + width / 2, cut + 0.4, f"{cut:.0f}", ha="center", fontsize=10,
                  fontweight="bold", color=GREEN)
    for harmonic in (1, 2, 3, 4):
        left.axhline(harmonic, color=GRAY, lw=0.6, ls=":")
    left.set_xticks(x)
    left.set_xticklabels([f"mode {n+1}" for n in x])
    left.set_ylabel("frequency / first mode")
    left.set_ylim(0, 15)
    left.legend(fontsize=10)
    left.set_title("A bar's modes are not whole numbers",
                   fontsize=12, fontweight="bold")

    # Where the wood is removed, and why.
    s = np.linspace(0, 1, 400)
    thickness = 1.0 - 0.62 * np.exp(-((s - 0.5) / 0.26) ** 2)
    right.fill_between(s, -thickness / 2, thickness / 2, color=LIGHT,
                       edgecolor="#333333", lw=1.4)
    right.plot(s, 0.62 * np.sin(np.pi * s) * 0.0 + 0.0, lw=0)
    right.axhline(0, color=GRAY, lw=0.7)
    right.annotate("wood removed here", xy=(0.5, -0.2), xytext=(0.5, -0.62),
                   ha="center", fontsize=10.5, color=RED,
                   arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    right.text(0.5, 0.62,
               "Thinning the middle lowers the\nsecond mode more than the first,\n"
               "until their ratio is 4:1 — two octaves.",
               ha="center", fontsize=10, color=GREEN)
    right.set_xlim(-0.03, 1.03)
    right.set_ylim(-0.85, 1.0)
    right.axis("off")
    right.set_title("Undercutting a marimba bar", fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch12-bar-modes")


def membrane_modes():
    """The first six modes of an ideal circular membrane."""
    use_style()
    fig, axes = plt.subplots(2, 3, figsize=(9.2, 5.0))
    grid = np.linspace(-1, 1, 260)
    X, Y = np.meshgrid(grid, grid)
    R = np.hypot(X, Y)
    THETA = np.arctan2(Y, X)

    modes = [(0, 1), (1, 1), (2, 1), (0, 2), (3, 1), (1, 2)]
    base = jn_zeros(0, 1)[0]

    for ax, (m, n) in zip(axes.flat, modes):
        root = jn_zeros(m, n)[n - 1]
        shape = jn(m, root * R) * np.cos(m * THETA)
        shape = np.where(R <= 1, shape, np.nan)
        ax.imshow(shape, extent=(-1, 1, -1, 1), cmap="RdBu_r",
                  vmin=-np.nanmax(np.abs(shape)), vmax=np.nanmax(np.abs(shape)))
        ax.contour(X, Y, np.where(R <= 1, shape, np.nan), levels=[0],
                   colors="#333333", linewidths=1.2)
        circle = plt.Circle((0, 0), 1, fill=False, color="#333333", lw=1.8)
        ax.add_patch(circle)
        ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"({m},{n})   $f = {root/base:.2f}f_1$",
                     fontsize=11, fontweight="bold")

    fig.suptitle("Modes of an ideal circular membrane: the ratios are not whole numbers",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.90)
    save(fig, "ch12-membrane-modes")


def timpani_modes():
    """Air loading turns the kettledrum's modes into a near-harmonic set."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.8, 3.6))

    labels = ["(1,1)", "(2,1)", "(3,1)", "(4,1)", "(5,1)"]
    ideal_roots = np.array([jn_zeros(m, 1)[0] for m in (1, 2, 3, 4, 5)])
    ideal = ideal_roots / ideal_roots[0]
    # Measured timpani ratios: close to 1 : 1.5 : 2 : 2.5 : 3.
    measured = np.array([1.00, 1.50, 2.00, 2.44, 2.90])

    x = np.arange(len(labels))
    width = 0.36
    ax.bar(x - width / 2, ideal, width, color=RED, label="ideal membrane in vacuum")
    ax.bar(x + width / 2, measured, width, color=GREEN, label="real timpano, air-loaded")
    for index, (a, b) in enumerate(zip(ideal, measured)):
        ax.text(index - width / 2, a + 0.05, f"{a:.2f}", ha="center", fontsize=9.5)
        ax.text(index + width / 2, b + 0.05, f"{b:.2f}", ha="center", fontsize=9.5,
                fontweight="bold", color=GREEN)
    for ratio in (1.0, 1.5, 2.0, 2.5, 3.0):
        ax.axhline(ratio, color=GRAY, lw=0.6, ls=":")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("frequency / lowest mode")
    ax.set_ylim(0, 3.6)
    ax.legend(fontsize=10, loc="upper left")
    ax.set_title("Why a timpano has a pitch and a drumhead does not",
                 fontsize=12, fontweight="bold")
    ax.text(3.4, 0.35, "the measured set is 2 : 3 : 4 : 5 : 6\n"
                       "of a missing fundamental",
            fontsize=10, color=GREEN, ha="center")
    fig.tight_layout()
    save(fig, "ch12-timpani-modes")


def chladni():
    """Nodal patterns on a square plate, as sand would show them."""
    use_style()
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.8))
    grid = np.linspace(0, 1, 320)
    X, Y = np.meshgrid(grid, grid)

    patterns = [(2, 3), (3, 4), (4, 5), (5, 7)]
    for ax, (m, n) in zip(axes, patterns):
        shape = (np.cos(m * np.pi * X) * np.cos(n * np.pi * Y)
                 - np.cos(n * np.pi * X) * np.cos(m * np.pi * Y))
        ax.imshow(np.abs(shape) < 0.045, extent=(0, 1, 0, 1), cmap="gray_r")
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"$({m},{n})$", fontsize=11.5, fontweight="bold")
        for spine in ax.spines.values():
            spine.set_color("#333333")

    fig.suptitle("Chladni figures: sand collects where the plate does not move",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    save(fig, "ch12-chladni")


def bell_partials():
    """A tuned church bell's five named partials."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.8, 3.2))

    names = ["hum", "prime", "tierce", "quint", "nominal"]
    ratios = np.array([0.5, 1.0, 1.2, 1.5, 2.0])
    intervals = ["octave below", "the strike note", "minor third", "fifth", "octave above"]
    colours = [BLUE, GREEN, RED, ORANGE, PURPLE]

    for ratio, name, interval, colour in zip(ratios, names, intervals, colours):
        ax.vlines(ratio, 0, 1, color=colour, lw=9)
        ax.text(ratio, 1.08, name, ha="center", fontsize=11.5, fontweight="bold", color=colour)
        ax.text(ratio, -0.14, interval, ha="center", fontsize=9.5, color=GRAY)
    ax.set_xlim(0.35, 2.25)
    ax.set_ylim(-0.3, 1.35)
    ax.set_yticks([])
    ax.set_xlabel("frequency, relative to the prime")
    ax.set_title("A tuned bell: five partials placed deliberately",
                 fontsize=12, fontweight="bold")
    ax.text(1.75, 0.55, "the minor third is why\nbells sound solemn",
            fontsize=10, color=RED, ha="center")
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "ch12-bell-partials")


def main():
    print("Chapter 12 figures:")
    bar_modes()
    membrane_modes()
    timpani_modes()
    chladni()
    bell_partials()


if __name__ == "__main__":
    main()
