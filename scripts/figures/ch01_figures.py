"""Figures for Chapter 1, Sound, Music, and Simple Harmonic Motion."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def longitudinal_wave():
    """Molecules bunching and thinning, with the pressure they produce beneath.

    The two panels share an x axis on purpose: the whole point is that a
    compression in the top panel sits directly above a pressure maximum in the
    bottom one, and that the wave in the graph is a picture of density, not of
    anything moving sideways.
    """
    use_style()
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.4, 3.8), sharex=True,
                                      gridspec_kw={"height_ratios": [1.0, 1.2]})

    wavelength = 2.0
    rng = np.random.default_rng(7)
    # Undisplaced positions, then pushed along x by the wave itself.
    x0 = np.linspace(0, 8, 900)
    y = rng.uniform(0.12, 0.88, x0.size)
    displacement = 0.16 * np.sin(2 * np.pi * x0 / wavelength)
    top.scatter(x0 + displacement, y, s=5, color=BLUE, alpha=0.75, linewidths=0)
    top.set_ylim(0, 1)
    top.set_yticks([])
    for side in ("left", "right", "top", "bottom"):
        top.spines[side].set_visible(False)

    # Displacement s = A sin(kx) bunches the dots where ds/dx is most negative,
    # so the compression is at x = lambda/2, a quarter wavelength from where the
    # displacement itself peaks. Getting this wrong is the classic way to draw
    # this figure, and it makes the pressure graph a lie.
    for centre, label, colour in ((wavelength * 0.5, "compression", RED),
                                  (wavelength * 1.0, "rarefaction", BLUE)):
        top.annotate(label, xy=(centre, 0.5), xytext=(centre, 1.18),
                     ha="center", fontsize=10, color=colour,
                     arrowprops=dict(arrowstyle="->", color=colour, lw=1.2))

    x = np.linspace(0, 8, 800)
    # Excess pressure is proportional to -ds/dx, not to s.
    pressure = -np.cos(2 * np.pi * x / wavelength)
    bottom.plot(x, pressure, color=RED)
    bottom.axhline(0.0, color=GRAY, lw=0.8)
    bottom.set_ylabel("pressure\n(relative to still air)")
    bottom.set_xlabel("distance along the direction of travel")
    bottom.set_yticks([0.0])
    bottom.set_yticklabels(["0"])
    bottom.set_xticks([])
    bottom.set_xlim(0, 8)

    # One wavelength, marked where it can be read off both panels.
    bottom.annotate("", xy=(wavelength * 0.5, -1.35), xytext=(wavelength * 1.5, -1.35),
                    arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.1))
    bottom.text(wavelength * 1.0, -1.62, "one wavelength $\\lambda$",
                ha="center", fontsize=10, color=GRAY)
    bottom.set_ylim(-1.9, 1.35)

    fig.tight_layout()
    save(fig, "ch01-longitudinal-wave")


def sinusoid_anatomy():
    """The four numbers that describe a sinusoid, marked on one."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    t = np.linspace(0, 2.6, 900)
    period, amplitude = 1.0, 1.0
    y = amplitude * np.sin(2 * np.pi * t / period)
    ax.plot(t, y, color=BLUE, lw=2.0)
    ax.axhline(0.0, color=GRAY, lw=0.8)

    # Amplitude: from equilibrium to the peak, not peak to trough.
    ax.annotate("", xy=(0.25, 0), xytext=(0.25, amplitude),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.3))
    ax.text(0.31, amplitude / 2, "amplitude $A$", color=RED, va="center", fontsize=11)

    # Period: peak to peak.
    ax.annotate("", xy=(0.25, 1.28), xytext=(1.25, 1.28),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.3))
    ax.text(0.75, 1.37, "period $T$", color=GREEN, ha="center", fontsize=11)

    # A second trace, shifted, to show what phase means.
    shift = 0.3
    ax.plot(t, amplitude * np.sin(2 * np.pi * (t - shift) / period),
            color=PURPLE, lw=1.6, ls="--")
    ax.annotate("", xy=(1.0, -1.28), xytext=(1.0 + shift, -1.28),
                arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.3))
    ax.text(1.0 + shift / 2, -1.52, "phase shift", color=PURPLE, ha="center", fontsize=11)

    ax.set_xlabel("time")
    ax.set_ylabel("displacement")
    ax.set_yticks([0])
    ax.set_xticks([])
    ax.set_ylim(-1.75, 1.6)
    ax.set_xlim(0, 2.6)
    ax.text(2.55, 1.1, "$f = 1/T$", ha="right", fontsize=11, color=GREEN)
    fig.tight_layout()
    save(fig, "ch01-sinusoid-anatomy")


def mass_spring():
    """A mass on a spring at three moments, with the restoring force drawn."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.0, 3.0))
    ax.set_xlim(-0.6, 9.4)
    ax.set_ylim(-1.9, 2.2)
    ax.axis("off")

    def coil(x0, x1, y, turns=9, height=0.28):
        t = np.linspace(0, 1, 400)
        return x0 + t * (x1 - x0), y + height * np.sin(2 * np.pi * turns * t)

    states = [
        (0.0, "released here", "$F$ pulls back", RED),
        (1.0, "passing equilibrium", "$F = 0$, speed greatest", GREEN),
        (2.0, "far side", "$F$ pulls back", RED),
    ]
    offsets = [1.0, 0.0, -1.0]
    for index, ((_, caption, force, colour), offset) in enumerate(zip(states, offsets)):
        base = index * 3.1
        wall = base
        rest = base + 1.6
        mass_x = rest + offset * 0.55
        ax.plot([wall, wall], [-0.75, 0.75], color=GRAY, lw=3)
        cx, cy = coil(wall, mass_x - 0.22, 0.0)
        ax.plot(cx, cy, color=BLUE, lw=1.4)
        ax.add_patch(plt.Rectangle((mass_x - 0.22, -0.34), 0.44, 0.68,
                                   facecolor=LIGHT, edgecolor="#333333", lw=1.0, zorder=2))
        ax.plot([rest, rest], [-0.95, 0.95], color=GRAY, lw=1.0, ls=":", zorder=3)
        if offset:
            direction = -np.sign(offset)
            ax.add_patch(FancyArrowPatch((mass_x + direction * 0.28, 0.0),
                                         (mass_x + direction * 0.95, 0.0),
                                         arrowstyle="-|>", mutation_scale=13,
                                         color=colour, lw=1.8))
        ax.text(rest, 1.55, caption, ha="center", fontsize=10.5, fontweight="bold")
        ax.text(rest, -1.35, force, ha="center", fontsize=10, color=colour)
    ax.text(4.65, -1.85, "The dotted line is the equilibrium position; "
                         "the force always points back toward it.",
            ha="center", fontsize=10, color=GRAY)
    fig.tight_layout()
    save(fig, "ch01-mass-spring")


def frequency_ranges():
    """Where music sits inside the range of human hearing."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    rows = [
        ("Human hearing", 20, 20000, GRAY),
        ("Piano (fundamentals)", 27.5, 4186, BLUE),
        ("Singing voice", 70, 1400, PURPLE),
        ("Violin", 196, 3136, GREEN),
        ("Double bass", 41, 262, ORANGE),
        ("Speech (most energy)", 250, 4000, RED),
    ]
    for index, (label, low, high, colour) in enumerate(rows):
        y = len(rows) - index
        ax.plot([low, high], [y, y], lw=9, color=colour, solid_capstyle="butt", alpha=0.85)
        ax.text(17, y, label, ha="right", va="center", fontsize=10.5)
        ax.text(high * 1.12, y, f"{low:g}–{high:g} Hz", va="center",
                fontsize=9.5, color=GRAY)

    ax.axvline(440, color="#333333", lw=1.0, ls=":")
    ax.text(440, 0.24, "A440", ha="center", fontsize=10, color="#333333")
    ax.set_xscale("log")
    ax.set_xlim(12, 60000)
    ax.set_ylim(0.0, len(rows) + 0.8)
    ax.set_yticks([])
    ax.set_xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000])
    ax.set_xticklabels(["20", "50", "100", "200", "500", "1k", "2k", "5k", "10k", "20k"])
    ax.set_xlabel("frequency (Hz), logarithmic")
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "ch01-frequency-ranges")


def damping():
    """Three decay rates, and the note length each one produces."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.2))
    t = np.linspace(0, 4, 2000)
    carrier = np.sin(2 * np.pi * 6 * t)
    for tau, label, colour in ((3.0, "lightly damped — a struck bell", BLUE),
                               (0.8, "moderately damped — a plucked string", GREEN),
                               (0.18, "heavily damped — a damped string", RED)):
        ax.plot(t, np.exp(-t / tau) * carrier, color=colour, lw=1.0, alpha=0.75)
        ax.plot(t, np.exp(-t / tau), color=colour, lw=2.0, label=label)
        ax.plot(t, -np.exp(-t / tau), color=colour, lw=2.0)
    ax.axhline(0.0, color=GRAY, lw=0.8)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("displacement")
    ax.set_yticks([0])
    ax.set_xlim(0, 4)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Same frequency, same starting amplitude, three decay rates",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch01-damping")


def main():
    print("Chapter 1 figures:")
    longitudinal_wave()
    sinusoid_anatomy()
    mass_spring()
    frequency_ranges()
    damping()


if __name__ == "__main__":
    main()
