"""Figures for Chapter 14, Room Acoustics and Concert-Hall Design."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def echogram():
    """Direct sound, early reflections, and the reverberant tail."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.8, 3.6))

    rng = np.random.default_rng(4)
    ax.vlines(0, 0, 1.0, color=GREEN, lw=3.5)
    ax.text(0, 1.06, "direct sound", ha="center", fontsize=10.5, color=GREEN,
            fontweight="bold")

    early_times = np.array([18, 26, 33, 41, 48, 57, 66, 74])
    early_levels = 0.62 * np.exp(-early_times / 120) * rng.uniform(0.6, 1.0, early_times.size)
    ax.vlines(early_times, 0, early_levels, color=BLUE, lw=2.6)
    ax.text(45, 0.78, "early reflections", ha="center", fontsize=10.5, color=BLUE,
            fontweight="bold")

    late_times = np.sort(rng.uniform(80, 900, 420))
    late_levels = 0.42 * np.exp(-late_times / 300) * rng.uniform(0.15, 1.0, late_times.size)
    ax.vlines(late_times, 0, late_levels, color=PURPLE, lw=0.7, alpha=0.8)
    ax.plot(late_times, 0.42 * np.exp(-late_times / 300), color=RED, lw=2.0, ls="--")
    ax.text(480, 0.30, "reverberant tail", ha="center", fontsize=10.5, color=PURPLE,
            fontweight="bold")

    ax.axvspan(0, 80, color=LIGHT, alpha=0.4)
    ax.text(40, -0.1, "first 80 ms:\nheard as part of the direct sound",
            ha="center", va="top", fontsize=9.5, color=GRAY)
    ax.set_xlabel("time after the direct sound (ms)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(-25, 950)
    ax.set_ylim(-0.3, 1.2)
    ax.set_title("An echogram: what arrives at a listener, and when",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch14-echogram")


def absorption():
    """Absorption coefficients of common surfaces, against frequency."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    bands = np.array([125, 250, 500, 1000, 2000, 4000], dtype=float)
    materials = {
        "Painted concrete": ([0.01, 0.01, 0.02, 0.02, 0.02, 0.03], GRAY),
        "Wood panelling": ([0.30, 0.25, 0.20, 0.17, 0.15, 0.10], ORANGE),
        "Carpet on concrete": ([0.02, 0.06, 0.14, 0.37, 0.60, 0.65], BLUE),
        "Heavy curtain": ([0.14, 0.35, 0.55, 0.72, 0.70, 0.65], GREEN),
        "Audience, occupied seats": ([0.39, 0.57, 0.80, 0.94, 0.92, 0.87], RED),
    }
    for name, (values, colour) in materials.items():
        ax.plot(bands, values, "-o", color=colour, lw=2.0, ms=5, label=name)
    ax.set_xscale("log")
    ax.set_xticks(bands)
    ax.set_xticklabels(["125", "250", "500", "1k", "2k", "4k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("absorption coefficient $\\alpha$")
    ax.set_ylim(0, 1.0)
    ax.legend(fontsize=9.5, loc="upper left")
    ax.set_title("Absorption depends strongly on frequency — and the audience "
                 "absorbs most of all",
                 fontsize=11.5, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch14-absorption")


def reverberation_targets():
    """Reverberation time against room volume, with usage bands."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.8))
    volumes = np.logspace(2, 5, 300)

    bands = [
        ("Speech, lecture", 0.6, 1.0, BLUE),
        ("Chamber music", 1.2, 1.6, GREEN),
        ("Symphony orchestra", 1.8, 2.2, ORANGE),
        ("Organ, choral", 2.5, 4.0, PURPLE),
    ]
    for name, low, high, colour in bands:
        ax.axhspan(low, high, color=colour, alpha=0.16)
        ax.text(1.4e2, (low + high) / 2, name, fontsize=10, color=colour, va="center")

    halls = [(1800, 1.1, "small recital room"), (12000, 1.5, "chamber hall"),
             (21000, 2.0, "Musikverein, Vienna"), (30000, 2.2, "Concert hall"),
             (85000, 5.5, "cathedral")]
    for volume, rt, label in halls:
        ax.plot([volume], [rt], "o", color=RED, ms=8)
        ax.annotate(label, xy=(volume, rt), xytext=(volume * 1.15, rt + 0.22),
                    fontsize=9.5, color=RED)

    ax.set_xscale("log")
    ax.set_xlim(1.2e2, 2e5)
    ax.set_ylim(0, 6.5)
    ax.set_xlabel("room volume (m$^3$)")
    ax.set_ylabel("reverberation time $T_{60}$ (s)")
    ax.set_title("How long should a room ring?", fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch14-reverberation-targets")


def room_modes():
    """Modal density, and why small rooms are hard."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.4))

    # Axial modes of a small rectangular room.
    dims = (5.4, 4.1, 2.6)
    v = 343.0
    modes = []
    for nx in range(0, 6):
        for ny in range(0, 6):
            for nz in range(0, 4):
                if nx == ny == nz == 0:
                    continue
                f = (v / 2) * np.sqrt((nx / dims[0]) ** 2 + (ny / dims[1]) ** 2
                                      + (nz / dims[2]) ** 2)
                if f < 300:
                    modes.append(f)
    modes = np.sort(np.array(modes))
    left.vlines(modes, 0, 1, color=BLUE, lw=1.4)
    left.set_xlim(0, 300)
    left.set_ylim(0, 1.3)
    left.set_yticks([])
    left.set_xlabel("frequency (Hz)")
    left.set_title(f"Modes of a {dims[0]}×{dims[1]}×{dims[2]} m room",
                   fontsize=11.5, fontweight="bold")
    left.text(150, 1.12, "sparse and uneven below about 200 Hz",
              ha="center", fontsize=10, color=RED)

    # Schroeder frequency against volume.
    volumes = np.logspace(1.3, 5, 300)
    for rt, colour, label in ((0.5, BLUE, "$T_{60} = 0.5$ s"),
                              (1.5, GREEN, "$T_{60} = 1.5$ s"),
                              (2.2, ORANGE, "$T_{60} = 2.2$ s")):
        right.plot(volumes, 2000 * np.sqrt(rt / volumes), color=colour, lw=2.2, label=label)
    right.set_xscale("log")
    right.set_yscale("log")
    right.set_xlabel("room volume (m$^3$)")
    right.set_ylabel("Schroeder frequency (Hz)")
    right.legend(fontsize=9.5)
    right.set_title("Above this, modes overlap and the room\nbehaves statistically",
                    fontsize=11.5, fontweight="bold")
    right.annotate("a living room: modes matter\nover most of the bass",
                   xy=(60, 2000 * np.sqrt(0.5 / 60)), xytext=(200, 160),
                   fontsize=9.5, color=RED,
                   arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))

    fig.tight_layout()
    save(fig, "ch14-room-modes")


def hall_plans():
    """Three hall shapes and what each does with lateral reflections."""
    use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.2))

    # Shoebox.
    ax = axes[0]
    ax.add_patch(plt.Rectangle((0.2, 0.1), 0.6, 0.8, facecolor=LIGHT,
                               edgecolor="#333333", lw=1.6))
    ax.plot([0.5], [0.82], "o", color=RED, ms=9)
    ax.plot([0.5], [0.35], "o", color=GREEN, ms=8)
    for wall_x in (0.2, 0.8):
        ax.annotate("", xy=(0.5, 0.35), xytext=(wall_x, 0.62),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.6))
        ax.annotate("", xy=(wall_x, 0.62), xytext=(0.5, 0.82),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.6))
    ax.set_title("Shoebox", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.02, "narrow, parallel walls give\nstrong lateral reflections",
            ha="center", va="top", fontsize=9.5, color=BLUE)

    # Fan.
    ax = axes[1]
    ax.add_patch(plt.Polygon([[0.42, 0.9], [0.58, 0.9], [0.9, 0.1], [0.1, 0.1]],
                             facecolor=LIGHT, edgecolor="#333333", lw=1.6))
    ax.plot([0.5], [0.82], "o", color=RED, ms=9)
    ax.plot([0.5], [0.32], "o", color=GREEN, ms=8)
    for wall in ([0.26, 0.5], [0.74, 0.5]):
        ax.annotate("", xy=(wall[0], wall[1]), xytext=(0.5, 0.82),
                    arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
        ax.annotate("", xy=(wall[0] + (0.24 if wall[0] < 0.5 else -0.24), 0.14),
                    xytext=(wall[0], wall[1]),
                    arrowprops=dict(arrowstyle="->", color=RED, lw=1.6, ls=":"))
    ax.set_title("Fan", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.02, "splayed walls send reflections\npast the listener",
            ha="center", va="top", fontsize=9.5, color=RED)

    # Vineyard.
    ax = axes[2]
    ax.add_patch(plt.Circle((0.5, 0.5), 0.42, facecolor=LIGHT,
                            edgecolor="#333333", lw=1.6))
    ax.plot([0.5], [0.5], "o", color=RED, ms=9)
    rng = np.random.default_rng(2)
    for angle in np.linspace(0, 2 * np.pi, 9)[:-1]:
        r = 0.27
        ax.add_patch(plt.Rectangle((0.5 + r * np.cos(angle) - 0.07,
                                    0.5 + r * np.sin(angle) - 0.05), 0.14, 0.10,
                                   facecolor="white", edgecolor=GREEN, lw=1.4,
                                   angle=np.degrees(angle)))
    ax.set_title("Vineyard", fontsize=12, fontweight="bold")
    ax.text(0.5, 0.02, "terraces act as local side walls\nfor the block behind",
            ha="center", va="top", fontsize=9.5, color=GREEN)

    for ax in axes:
        ax.set_xlim(0, 1); ax.set_ylim(-0.25, 1)
        ax.set_aspect("equal"); ax.axis("off")

    fig.suptitle("Three plans, one question: where do the side reflections go?",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.84)
    save(fig, "ch14-hall-plans")


def main():
    print("Chapter 14 figures:")
    echogram()
    absorption()
    reverberation_targets()
    room_modes()
    hall_plans()


if __name__ == "__main__":
    main()
