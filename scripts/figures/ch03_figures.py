"""Figures for Chapter 3, Superposition, Interference, and Standing Waves."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def _pulse(x, centre, width=0.55, height=1.0):
    return height * np.exp(-((x - centre) / width) ** 2)


def superposition():
    """Two pulses meeting: they add where they overlap, then carry on unchanged."""
    use_style()
    fig, axes = plt.subplots(2, 3, figsize=(9.2, 4.2), sharey=True)
    x = np.linspace(-6, 6, 900)

    for row, (height, label, colour) in enumerate((
            (1.0, "Same sign: they reinforce", GREEN),
            (-1.0, "Opposite sign: they cancel", RED))):
        for column, separation in enumerate((3.2, 0.0, -3.2)):
            ax = axes[row][column]
            offset = abs(separation)
            left = _pulse(x, -offset)
            right = _pulse(x, offset, height=height)
            ax.plot(x, left, color=BLUE, lw=1.2, ls="--", alpha=0.8)
            ax.plot(x, right, color=ORANGE, lw=1.2, ls="--", alpha=0.8)
            ax.plot(x, left + right, color=colour, lw=2.2)
            ax.axhline(0.0, color=GRAY, lw=0.7)
            ax.set_ylim(-1.6, 2.3)
            ax.set_xticks([])
            ax.set_yticks([])
            for side in ("left", "right", "top", "bottom"):
                ax.spines[side].set_visible(False)
            if row == 0:
                ax.set_title(["approaching", "overlapping", "past each other"][column],
                             fontsize=11)
        axes[row][0].text(-5.9, 1.85, label, fontsize=11, fontweight="bold", color=colour)

    fig.suptitle("Two pulses pass through each other", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.86)
    save(fig, "ch03-superposition")


def path_difference():
    """Two loudspeakers, and the quiet lines between them."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.8),
                                      gridspec_kw={"width_ratios": [1.15, 1.0]})

    # Geometry: two sources, a listener, two path lengths.
    left.plot([0, 0], [1.2, -1.2], "o", color=RED, ms=11)
    left.text(-0.35, 1.2, "$S_1$", fontsize=12, ha="right", va="center")
    left.text(-0.35, -1.2, "$S_2$", fontsize=12, ha="right", va="center")
    listener = (4.4, 0.55)
    left.plot([listener[0]], [listener[1]], "o", color=GREEN, ms=10)
    left.text(listener[0] + 0.2, listener[1], "listener", fontsize=11, va="center")
    for y0, colour in ((1.2, BLUE), (-1.2, PURPLE)):
        left.plot([0, listener[0]], [y0, listener[1]], color=colour, lw=1.6)
    left.text(2.0, 1.15, "$r_1$", color=BLUE, fontsize=12)
    left.text(2.0, -0.6, "$r_2$", color=PURPLE, fontsize=12)
    left.set_xlim(-1.2, 6.2)
    left.set_ylim(-2.0, 2.0)
    left.axis("off")
    left.set_title("Two sources, two path lengths", fontsize=12, fontweight="bold")
    left.text(2.5, -1.75, "path difference  $\\Delta r = r_2 - r_1$",
              fontsize=11, ha="center")

    # What the listener hears as the path difference is swept.
    delta = np.linspace(0, 3, 600)          # in wavelengths
    amplitude = np.abs(np.cos(np.pi * delta))
    right.plot(delta, amplitude, color=GREEN, lw=2.2)
    right.fill_between(delta, 0, amplitude, color=LIGHT, alpha=0.5)
    for m in (0, 1, 2, 3):
        right.axvline(m, color=GRAY, lw=0.7, ls=":")
    for m in (0.5, 1.5, 2.5):
        right.plot([m], [0], "o", color=RED, ms=6)
    right.text(0.5, 0.1, "quiet", color=RED, ha="center", fontsize=10.5)
    right.text(1.0, 1.06, "loud", color=GREEN, ha="center", fontsize=10.5)
    right.set_xlabel("path difference (wavelengths)")
    right.set_ylabel("amplitude at the listener")
    right.set_yticks([])
    right.set_xlim(0, 3)
    right.set_ylim(0, 1.25)
    right.set_title("Loud where $\\Delta r = m\\lambda$, quiet at $(m+\\frac{1}{2})\\lambda$",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch03-path-difference")


def reflection():
    """A pulse reflecting from a fixed end and from a free end."""
    use_style()
    fig, axes = plt.subplots(2, 3, figsize=(9.2, 4.0), sharey=True)
    x = np.linspace(0, 10, 900)

    for row, (inverted, title, colour) in enumerate((
            (True, "Fixed end: the pulse comes back upside down", RED),
            (False, "Free end: it comes back the same way up", GREEN))):
        for column, stage in enumerate(("before", "at the wall", "after")):
            ax = axes[row][column]
            if stage == "before":
                y = _pulse(x, 3.0)
            elif stage == "at the wall":
                # Incident and its image arrive together; at a fixed end they cancel.
                y = _pulse(x, 9.4) + (-1 if inverted else 1) * _pulse(x, 10.6)
            else:
                y = (-1 if inverted else 1) * _pulse(x, 7.0)
            ax.plot(x, y, color=colour, lw=2.2)
            ax.axhline(0.0, color=GRAY, lw=0.8)
            ax.plot([10, 10], [-1.4, 1.4], color="#333333", lw=3 if inverted else 1.2,
                    ls="-" if inverted else ":")
            if not inverted:
                ax.plot([10], [y[-1]], "o", color="#333333", ms=6)
            ax.set_xlim(0, 10.6)
            ax.set_ylim(-1.6, 1.6)
            ax.set_xticks([])
            ax.set_yticks([])
            for side in ("left", "right", "top", "bottom"):
                ax.spines[side].set_visible(False)
            if row == 0:
                ax.set_title(stage, fontsize=11)
        axes[row][0].text(0.2, 1.25, title, fontsize=11, fontweight="bold", color=colour)

    fig.tight_layout()
    save(fig, "ch03-reflection")


def standing_wave_formation():
    """Two travelling waves in opposite directions, summed at five moments."""
    use_style()
    fig, axes = plt.subplots(5, 1, figsize=(8.0, 5.6), sharex=True)
    x = np.linspace(0, 2, 900)
    k = 2 * np.pi / 1.0

    for index, ax in enumerate(axes):
        phase = index * np.pi / 4
        right_going = 0.5 * np.sin(k * x - phase)
        left_going = 0.5 * np.sin(k * x + phase)
        ax.plot(x, right_going, color=BLUE, lw=1.0, ls="--", alpha=0.8)
        ax.plot(x, left_going, color=ORANGE, lw=1.0, ls="--", alpha=0.8)
        ax.plot(x, right_going + left_going, color=GREEN, lw=2.4)
        ax.axhline(0.0, color=GRAY, lw=0.6)
        # The nodes never move, which is the whole point.
        for node in np.arange(0, 2.01, 0.5):
            ax.plot([node], [0], "o", color=RED, ms=5, zorder=5)
        ax.set_ylim(-1.15, 1.15)
        ax.set_yticks([])
        for side in ("left", "right", "top", "bottom"):
            ax.spines[side].set_visible(False)
        ax.text(2.03, 0, f"$t_{index}$", fontsize=11, va="center")

    axes[-1].set_xlabel("position")
    axes[-1].set_xticks([])
    fig.suptitle("A right-going and a left-going wave, and their sum",
                 fontsize=13, fontweight="bold")
    axes[0].text(0.02, 0.85, "red dots mark the nodes — they never move",
                 fontsize=10, color=RED)
    fig.tight_layout()
    fig.subplots_adjust(top=0.90)
    save(fig, "ch03-standing-wave-formation")


def string_modes():
    """The first four modes of a string fixed at both ends."""
    use_style()
    fig, axes = plt.subplots(4, 1, figsize=(8.0, 5.0), sharex=True)
    x = np.linspace(0, 1, 700)
    names = ["fundamental, $n=1$", "2nd harmonic, $n=2$",
             "3rd harmonic, $n=3$", "4th harmonic, $n=4$"]
    colours = [BLUE, GREEN, PURPLE, ORANGE]

    for n, (ax, name, colour) in enumerate(zip(axes, names, colours), start=1):
        shape = np.sin(n * np.pi * x)
        ax.plot(x, shape, color=colour, lw=2.2)
        ax.plot(x, -shape, color=colour, lw=2.2, alpha=0.35)
        ax.fill_between(x, shape, -shape, color=colour, alpha=0.10)
        ax.axhline(0.0, color=GRAY, lw=0.7)
        for node in np.arange(0, n + 1) / n:
            ax.plot([node], [0], "o", color=RED, ms=6, zorder=5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_yticks([])
        ax.set_xticks([])
        for side in ("left", "right", "top", "bottom"):
            ax.spines[side].set_visible(False)
        ax.text(-0.015, 0, name, ha="right", va="center", fontsize=10.5, color=colour)
        ax.text(1.015, 0, f"$\\lambda = 2L/{n}$\n$f = {n}f_1$",
                ha="left", va="center", fontsize=10.5)
        # The fixed ends.
        for end in (0.0, 1.0):
            ax.plot([end, end], [-1.25, 1.25], color="#333333", lw=2.5)

    fig.suptitle("A string fixed at both ends: only whole numbers of half-wavelengths fit",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.90, left=0.20, right=0.86)
    save(fig, "ch03-string-modes")


def pipe_modes():
    """Open and stopped pipes, drawn as displacement envelopes."""
    use_style()
    fig, axes = plt.subplots(3, 2, figsize=(9.2, 4.8), sharex=True)
    x = np.linspace(0, 1, 700)

    # Open at both ends: antinodes at both ends, all harmonics.
    open_modes = [(1, "$f_1$"), (2, "$2f_1$"), (3, "$3f_1$")]
    # Stopped at the left: node there, antinode at the open right end. Odd only.
    stopped_modes = [(1, "$f_1$"), (3, "$3f_1$"), (5, "$5f_1$")]

    for row in range(3):
        n_open, label_open = open_modes[row]
        ax = axes[row][0]
        shape = np.cos(n_open * np.pi * x)
        ax.plot(x, shape, color=BLUE, lw=2.0)
        ax.plot(x, -shape, color=BLUE, lw=2.0, alpha=0.35)
        ax.fill_between(x, shape, -shape, color=BLUE, alpha=0.10)
        ax.text(1.03, 0, label_open, fontsize=11, va="center")

        n_stop, label_stop = stopped_modes[row]
        ax2 = axes[row][1]
        shape2 = np.sin(n_stop * np.pi * x / 2)
        ax2.plot(x, shape2, color=RED, lw=2.0)
        ax2.plot(x, -shape2, color=RED, lw=2.0, alpha=0.35)
        ax2.fill_between(x, shape2, -shape2, color=RED, alpha=0.10)
        ax2.text(1.03, 0, label_stop, fontsize=11, va="center")

        for a, closed_left in ((ax, False), (ax2, True)):
            a.axhline(0.0, color=GRAY, lw=0.7)
            a.set_ylim(-1.5, 1.5)
            a.set_xlim(-0.02, 1.16)
            a.set_yticks([])
            a.set_xticks([])
            for side in ("left", "right", "top", "bottom"):
                a.spines[side].set_visible(False)
            # Pipe walls.
            a.plot([0, 1], [1.3, 1.3], color="#333333", lw=2.0)
            a.plot([0, 1], [-1.3, -1.3], color="#333333", lw=2.0)
            if closed_left:
                a.plot([0, 0], [-1.3, 1.3], color="#333333", lw=3.5)

    axes[0][0].set_title("Open at both ends\nall harmonics: 1, 2, 3, …",
                         fontsize=12, fontweight="bold")
    axes[0][1].set_title("Stopped at one end\nodd harmonics only: 1, 3, 5, …",
                         fontsize=12, fontweight="bold")
    fig.suptitle("Air-column modes, drawn as the displacement of the air",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    save(fig, "ch03-pipe-modes")


def main():
    print("Chapter 3 figures:")
    superposition()
    path_difference()
    reflection()
    standing_wave_formation()
    string_modes()
    pipe_modes()


if __name__ == "__main__":
    main()
