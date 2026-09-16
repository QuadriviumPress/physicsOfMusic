"""Figures for Chapter 10, String Instruments."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def pluck_amplitudes(position, n_max=16):
    """Mode amplitudes for a string plucked at a fraction `position` of its length."""
    n = np.arange(1, n_max + 1)
    return np.abs(np.sin(n * np.pi * position)) / n ** 2


def pluck_position():
    """Where you pluck decides which harmonics you get."""
    use_style()
    fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.4))
    n = np.arange(1, 17)
    x = np.linspace(0, 1, 500)

    for column, (position, label) in enumerate(((0.5, "at the middle ($L/2$)"),
                                                (0.2, "at $L/5$"),
                                                (0.08, "near the bridge"))):
        colour = [BLUE, GREEN, RED][column]
        top, bottom = axes[0][column], axes[1][column]
        shape = np.where(x < position, x / position, (1 - x) / (1 - position))
        top.plot(x, shape, color=colour, lw=2.2)
        top.plot([position], [1.0], "o", color="#333333", ms=7)
        top.set_ylim(-0.15, 1.35)
        top.set_xticks([]); top.set_yticks([])
        top.set_title(label, fontsize=11.5, fontweight="bold", color=colour)
        for side in ("left", "right", "top", "bottom"):
            top.spines[side].set_visible(False)

        amplitudes = pluck_amplitudes(position)
        amplitudes = amplitudes / amplitudes.max()
        bottom.vlines(n, 0, amplitudes, color=colour, lw=2.2)
        bottom.plot(n, amplitudes, "o", color=colour, ms=4)
        missing = [k for k in n if abs(np.sin(k * np.pi * position)) < 1e-9]
        for k in missing:
            bottom.plot([k], [0], "x", color="#333333", ms=9, mew=2)
        bottom.set_xlabel("harmonic number")
        bottom.set_ylim(0, 1.12)
        bottom.set_xlim(0, 17)
        if column == 0:
            bottom.set_ylabel("amplitude")
        else:
            bottom.set_yticks([])

    fig.suptitle("Plucking the same string in three places (✕ marks a suppressed harmonic)",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.84)
    save(fig, "ch10-pluck-position")


def helmholtz_motion():
    """The bowed string: a kink circulating inside a two-part envelope."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4),
                                      gridspec_kw={"width_ratios": [1.2, 1.0]})

    # Helmholtz motion: at every instant the string is exactly two straight
    # segments meeting at a kink, and the kink runs around a parabolic envelope.
    # Drawing it as a smooth curve, or letting the segments miss the endpoints,
    # loses the only thing the picture is for.
    amplitude = 0.26
    envelope_x = np.linspace(0, 1, 400)
    envelope_y = 4 * amplitude * envelope_x * (1 - envelope_x)
    left.plot(envelope_x, envelope_y, color=GRAY, lw=1.4, ls="--")
    left.plot(envelope_x, -envelope_y, color=GRAY, lw=1.4, ls="--")

    for phase, alpha in zip((0.18, 0.38, 0.58, 0.78, 0.94), (0.3, 0.45, 0.62, 0.8, 1.0)):
        kink_y = 4 * amplitude * phase * (1 - phase)
        left.plot([0, phase, 1], [0, kink_y, 0], color=BLUE, lw=1.8, alpha=alpha)
        left.plot([phase], [kink_y], "o", color=RED, ms=6, alpha=alpha)

    for end in (0.0, 1.0):
        left.plot([end, end], [-0.30, 0.30], color="#333333", lw=2.5)
    left.set_xticks([]); left.set_yticks([])
    left.set_xlim(-0.05, 1.05)
    left.set_ylim(-0.34, 0.40)
    left.set_title("The kink travels; the string is always two straight lines",
                   fontsize=11.5, fontweight="bold")
    left.text(0.5, -0.30, "red dot: the kink, running round the dashed envelope",
              ha="center", fontsize=10, color=RED)
    for side in ("left", "right", "top", "bottom"):
        left.spines[side].set_visible(False)

    # Velocity of the string at the bow: stick, then slip.
    t = np.linspace(0, 2, 800)
    frac = t % 1.0
    slip_start = 0.78
    velocity = np.where(frac < slip_start, 0.25, -0.25 * slip_start / (1 - slip_start))
    right.plot(t, velocity, color=RED, lw=2.2)
    right.axhline(0.25, color=GREEN, lw=1.2, ls="--")
    right.text(0.05, 0.31, "bow speed", fontsize=10, color=GREEN)
    right.text(0.35, 0.05, "STICK", fontsize=11, color=GREEN, fontweight="bold")
    right.text(0.87, -0.55, "SLIP", fontsize=11, color=RED, fontweight="bold", ha="center")
    right.set_xlabel("time (periods)")
    right.set_ylabel("string velocity at the bow")
    right.set_yticks([])
    right.set_xlim(0, 2)
    right.set_title("Stick and slip, once per period", fontsize=11.5, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch10-helmholtz-motion")


def body_response():
    """A guitar body's response: a few named modes and a forest above them."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.8, 3.4))
    freqs = np.logspace(np.log10(60), np.log10(6000), 2000)

    def peak(f0, q, height):
        return height / np.sqrt((1 - (freqs / f0) ** 2) ** 2 + (freqs / (f0 * q)) ** 2)

    named = [(100, 12, 1.0, "air (Helmholtz)"), (200, 14, 0.85, "top plate"),
             (270, 16, 0.6, "back plate")]
    response = np.zeros_like(freqs)
    for f0, q, height, _ in named:
        response += peak(f0, q, height)
    rng = np.random.default_rng(5)
    for f0 in np.exp(rng.uniform(np.log(400), np.log(6000), 55)):
        response += peak(f0, rng.uniform(18, 45), rng.uniform(0.05, 0.3))

    ax.plot(freqs, 20 * np.log10(response / response.max()), color=BLUE, lw=1.6)
    for f0, _, _, label in named:
        ax.axvline(f0, color=GRAY, lw=0.8, ls=":")
        ax.annotate(label, xy=(f0, 2), xytext=(f0 * 1.05, 4 - 7 * named.index(
            [n for n in named if n[0] == f0][0])),
            fontsize=10, color=RED)
    ax.set_xscale("log")
    ax.set_xlim(60, 6000)
    ax.set_ylim(-45, 10)
    ax.set_xticks([100, 200, 500, 1000, 2000, 5000])
    ax.set_xticklabels(["100", "200", "500", "1k", "2k", "5k"])
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("response (dB)")
    ax.set_title("A guitar body: three isolated low modes, then a forest",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch10-body-response")


def railsback():
    """The stretched tuning a real piano needs."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4))

    # Inharmonicity coefficient across the keyboard: high at both ends.
    keys = np.arange(1, 89)
    b = 1.0e-4 * (10 ** (0.020 * (keys - 50))) + 8e-4 * np.exp(-(keys - 1) / 9)
    left.semilogy(keys, b, color=BLUE, lw=2.2)
    left.set_xlabel("piano key number")
    left.set_ylabel("inharmonicity coefficient $B$")
    left.set_xlim(1, 88)
    left.set_title("Stiffness across the keyboard", fontsize=11.5, fontweight="bold")

    # A representative measured Railsback curve. This is *not* computed from the
    # B values on the left: doing that properly requires knowing which partial
    # the tuner matched at every step, which varies by tuner and by instrument.
    # The shape and the roughly plus or minus thirty cents at the extremes are
    # what every published measurement agrees on.
    middle = 49.0
    # Normalize each side by its own distance to the end of the keyboard, so
    # both extremes reach about 30 cents rather than the bass running off scale.
    span = np.where(keys >= middle, 88.0 - middle, middle - 1.0)
    offset = (keys - middle) / span
    deviation = 30.0 * np.sign(offset) * np.abs(offset) ** 2.6
    right.plot(keys, deviation, color=RED, lw=2.4)
    right.axhline(0, color=GRAY, lw=1.0, ls="--")
    right.text(30, 2.5, "exact equal temperament", fontsize=9.5, color=GRAY)
    for key, note in ((1, "A0"), (49, "C4"), (88, "C8")):
        this_span = 88.0 - middle if key >= middle else middle - 1.0
        this_offset = (key - middle) / this_span
        value = 30.0 * np.sign(this_offset) * np.abs(this_offset) ** 2.6
        right.plot([key], [value], "o", color=BLUE, ms=7)
        right.annotate(f"{note}\n{value:+.0f} cents", xy=(key, value),
                       xytext=(key + (4 if key < 60 else -14), value + (5 if key < 60 else -9)),
                       fontsize=9.5, color=BLUE)
    right.set_xlabel("piano key number")
    right.set_ylabel("cents from equal temperament")
    right.set_xlim(1, 88)
    right.set_ylim(-40, 40)
    right.set_title("Stretched: sharp at the top, flat at the bottom",
                    fontsize=11.5, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch10-railsback")


def impedance_chain():
    """Why a string needs a bridge and a soundboard."""
    use_style()
    fig, ax = plt.subplots(figsize=(9.0, 2.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.2, 1.6)
    ax.axis("off")

    stages = [("string\nthin, dense,\nhigh impedance", 1.2, RED),
              ("bridge\ncouples the two", 4.0, PURPLE),
              ("soundboard\nlarge, light,\nlow impedance", 6.8, GREEN),
              ("air\nvery low\nimpedance", 9.3, BLUE)]
    for label, x, colour in stages:
        ax.add_patch(plt.Circle((x, 0.3), 0.55, facecolor=LIGHT,
                                edgecolor=colour, lw=2.2))
        ax.text(x, -0.72, label, ha="center", va="top", fontsize=10, color=colour)
    for start, end in zip([s[1] for s in stages[:-1]], [s[1] for s in stages[1:]]):
        ax.add_patch(FancyArrowPatch((start + 0.6, 0.3), (end - 0.6, 0.3),
                                     arrowstyle="-|>", mutation_scale=15,
                                     color="#333333", lw=1.8))
    ax.text(5.2, 1.28,
            "A string driving air directly radiates almost nothing. Each stage steps the "
            "impedance down.",
            ha="center", fontsize=10.5, color=GRAY)
    fig.tight_layout()
    save(fig, "ch10-impedance-chain")


def main():
    print("Chapter 10 figures:")
    pluck_position()
    helmholtz_motion()
    body_response()
    railsback()
    impedance_chain()


if __name__ == "__main__":
    main()
