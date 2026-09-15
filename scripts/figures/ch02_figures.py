"""Figures for Chapter 2, Wave Motion and the Speed of Sound."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def transverse_and_longitudinal():
    """The two kinds of wave, with the medium's motion marked on each."""
    use_style()
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.4, 4.2))

    x = np.linspace(0, 6, 700)
    top.plot(x, 0.5 * np.sin(2 * np.pi * x / 2.0), color=BLUE, lw=2.2)
    top.annotate("", xy=(1.5, 0.9), xytext=(1.5, -0.9),
                 arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    top.text(1.66, 0.0, "the string moves\nacross the wave", color=RED,
             va="center", fontsize=10)
    top.annotate("", xy=(4.6, 0.0), xytext=(3.6, 0.0),
                 arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8, mutation_scale=16))
    top.text(4.1, 0.16, "wave travels", color=GREEN, ha="center", fontsize=10)
    top.set_title("Transverse: a wave on a string", fontsize=12, fontweight="bold")
    top.set_ylim(-1.15, 1.15)
    top.set_xlim(0, 6)
    top.set_xticks([])
    top.set_yticks([])
    for side in ("left", "right", "top", "bottom"):
        top.spines[side].set_visible(False)

    rng = np.random.default_rng(3)
    x0 = np.linspace(0, 6, 700)
    y = rng.uniform(0.2, 0.8, x0.size)
    bottom.scatter(x0 + 0.13 * np.sin(2 * np.pi * x0 / 2.0), y, s=5,
                   color=BLUE, alpha=0.75, linewidths=0)
    bottom.annotate("", xy=(1.9, 1.02), xytext=(1.1, 1.02),
                    arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    bottom.text(1.5, 1.14, "the air moves along the wave", color=RED,
                ha="center", fontsize=10)
    bottom.annotate("", xy=(4.6, 0.5), xytext=(3.6, 0.5),
                    arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.8, mutation_scale=16))
    bottom.text(4.1, 0.62, "wave travels", color=GREEN, ha="center", fontsize=10)
    bottom.set_title("Longitudinal: a sound wave in air", fontsize=12, fontweight="bold")
    bottom.set_ylim(0, 1.35)
    bottom.set_xlim(0, 6)
    bottom.set_xticks([])
    bottom.set_yticks([])
    for side in ("left", "right", "top", "bottom"):
        bottom.spines[side].set_visible(False)

    fig.tight_layout()
    save(fig, "ch02-transverse-longitudinal")


def wavelength_frequency():
    """One medium, three frequencies: the speed is fixed, so the wavelength is not."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.4))
    x = np.linspace(0, 4, 1200)
    for index, (freq, label, colour) in enumerate((
            (110.0, "110 Hz  —  $\\lambda = 3.1$ m", BLUE),
            (220.0, "220 Hz  —  $\\lambda = 1.6$ m", GREEN),
            (440.0, "440 Hz  —  $\\lambda = 0.78$ m", RED))):
        wavelength = 343.0 / freq
        offset = 2.4 * (2 - index)
        ax.plot(x, offset + 0.85 * np.sin(2 * np.pi * x / wavelength), color=colour, lw=1.8)
        ax.axhline(offset, color=GRAY, lw=0.6)
        ax.text(4.08, offset, label, va="center", fontsize=10.5, color=colour)
        # One wavelength, marked.
        ax.annotate("", xy=(0.0, offset - 1.25), xytext=(wavelength, offset - 1.25),
                    arrowprops=dict(arrowstyle="<->", color=colour, lw=1.1))
    ax.set_xlabel("distance (m)")
    ax.set_xlim(0, 4)
    ax.set_ylim(-1.5, 6.6)
    ax.set_yticks([])
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    ax.set_title("Same air, same speed of 343 m/s, three frequencies",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch02-wavelength-frequency")


def speed_vs_temperature():
    """Why a wind instrument plays flat when it is cold."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.4))

    temps = np.linspace(-10, 40, 300)
    speeds = 331.3 + 0.606 * temps
    left.plot(temps, speeds, color=BLUE, lw=2.2)
    for t, colour in ((5.0, ORANGE), (20.0, GREEN)):
        v = 331.3 + 0.606 * t
        left.plot([t], [v], "o", color=colour, ms=7)
        left.annotate(f"{t:.0f} °C\n{v:.0f} m/s", xy=(t, v), xytext=(t + 2, v - 9),
                      fontsize=9.5, color=colour)
    left.set_xlabel("air temperature (°C)")
    left.set_ylabel("speed of sound (m/s)")
    left.set_title("$v = 331.3 + 0.606\\,T$", fontsize=12, fontweight="bold")
    left.set_xlim(-10, 40)

    # The pitch of a fixed-length pipe follows the speed directly.
    cents = 1200 * np.log2((331.3 + 0.606 * temps) / (331.3 + 0.606 * 20.0))
    right.plot(temps, cents, color=RED, lw=2.2)
    right.axhline(0.0, color=GRAY, lw=0.8)
    right.axvline(20.0, color=GRAY, lw=0.8, ls=":")
    right.fill_between(temps, -5, 5, color=LIGHT, alpha=0.6)
    right.text(-8.5, 0.0, "within 5 cents\nof in tune", fontsize=9.5, color=GRAY, va="center")
    for t in (5.0, 35.0):
        c = 1200 * np.log2((331.3 + 0.606 * t) / (331.3 + 0.606 * 20.0))
        right.plot([t], [c], "o", color=RED, ms=6)
        right.annotate(f"{c:+.0f} cents", xy=(t, c), xytext=(t + 1.5, c + (4 if c > 0 else -9)),
                       fontsize=9.5, color=RED)
    right.set_xlabel("air temperature (°C)")
    right.set_ylabel("pitch shift (cents)")
    right.set_title("A fixed-length pipe, tuned at 20 °C", fontsize=12, fontweight="bold")
    right.set_xlim(-10, 40)

    fig.tight_layout()
    save(fig, "ch02-speed-vs-temperature")


def speed_in_media():
    """Stiffness beats density: sound is fastest in the stiffest materials."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.6))
    media = [
        ("Carbon dioxide", 259, ORANGE),
        ("Air, 20 °C", 343, BLUE),
        ("Helium", 965, PURPLE),
        ("Water", 1482, GREEN),
        ("Wood (spruce, along grain)", 3800, ORANGE),
        ("Steel", 5960, RED),
    ]
    names = [m[0] for m in media]
    values = [m[1] for m in media]
    colours = [m[2] for m in media]
    y = np.arange(len(media))
    ax.barh(y, values, color=colours, height=0.6, alpha=0.9)
    for index, value in enumerate(values):
        ax.text(value + 90, index, f"{value} m/s", va="center", fontsize=10)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=10.5)
    ax.set_xlabel("speed of sound (m/s)")
    ax.set_xlim(0, 7400)
    ax.set_title("Sound is fastest where the medium is stiffest",
                 fontsize=12, fontweight="bold")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    fig.tight_layout()
    save(fig, "ch02-speed-in-media")


def inverse_square():
    """Level against distance outdoors, and why it fails indoors."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.0, 3.4))
    r = np.logspace(0, 2, 300)
    free = -20 * np.log10(r)
    ax.plot(r, free, color=BLUE, lw=2.2, label="outdoors: $-6$ dB per doubling")

    # Indoors the reverberant field holds the level up beyond a critical distance.
    critical = 6.0
    indoor = 10 * np.log10(1.0 / r**2 + 1.0 / critical**2) - 10 * np.log10(1.0)
    ax.plot(r, indoor, color=RED, lw=2.2, ls="--", label="indoors: flattens out")
    ax.axvline(critical, color=GRAY, lw=0.9, ls=":")
    ax.text(critical * 1.1, -34, "critical distance", fontsize=10, color=GRAY)

    for distance in (1, 2, 4, 8):
        ax.plot([distance], [-20 * np.log10(distance)], "o", color=BLUE, ms=5)
    ax.set_xscale("log")
    ax.set_xlabel("distance from the source (m)")
    ax.set_ylabel("level relative to 1 m (dB)")
    ax.set_xlim(1, 100)
    ax.set_ylim(-42, 4)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("The inverse-square law, and where it stops being true",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch02-inverse-square")


def doppler():
    """Wavefronts from a moving source, bunched ahead and stretched behind."""
    use_style()
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    # Fast enough that the bunching ahead is unmistakable at page size; a
    # realistic siren is far slower, and the figure says so in its caption.
    speed_source = 0.72
    emissions = np.arange(0, 8)
    for n in emissions:
        age = emissions[-1] - n
        centre = -speed_source * age
        radius = age
        if radius <= 0:
            continue
        ax.add_patch(plt.Circle((centre, 0), radius, fill=False,
                                color=BLUE, lw=1.3, alpha=0.85))
    ax.plot([0], [0], "o", color=RED, ms=9, zorder=5)
    ax.annotate("", xy=(1.4, 0), xytext=(0.25, 0),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0, mutation_scale=16))
    ax.text(0.8, 0.35, "source moves", color=RED, ha="center", fontsize=10.5)
    ax.text(6.9, 0.0, "ahead:\nbunched,\npitch raised", color=GREEN,
            ha="center", va="center", fontsize=10.5, fontweight="bold")
    ax.text(-8.6, 0.0, "behind:\nstretched,\npitch lowered", color=PURPLE,
            ha="center", va="center", fontsize=10.5, fontweight="bold")
    ax.set_xlim(-10.5, 8.6)
    ax.set_ylim(-6.6, 6.6)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Wavefronts from a source moving to the right",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch02-doppler")


def main():
    print("Chapter 2 figures:")
    transverse_and_longitudinal()
    wavelength_frequency()
    speed_vs_temperature()
    speed_in_media()
    inverse_square()
    doppler()


if __name__ == "__main__":
    main()
