"""Figures for Chapter 4, Resonance and Normal Modes."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def _response(ratio, q):
    """Amplitude of a driven damped oscillator, normalized to its static value."""
    return 1.0 / np.sqrt((1 - ratio**2) ** 2 + (ratio / q) ** 2)


def response_curves():
    """Amplitude and phase against driving frequency, for three dampings."""
    use_style()
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.0, 5.0), sharex=True,
                                      gridspec_kw={"height_ratios": [1.5, 1.0]})
    ratio = np.linspace(0.05, 2.4, 900)

    for q, colour in ((15.0, BLUE), (5.0, GREEN), (1.5, RED)):
        top.plot(ratio, _response(ratio, q), color=colour, lw=2.2, label=f"$Q = {q:g}$")
        phase = np.degrees(np.arctan2(ratio / q, 1 - ratio**2))
        bottom.plot(ratio, phase, color=colour, lw=2.2)

    top.axvline(1.0, color=GRAY, lw=0.9, ls=":")
    top.set_ylabel("amplitude (relative to a slow push)")
    top.set_yscale("log")
    top.set_ylim(0.05, 30)
    top.legend(loc="upper right", fontsize=10)
    top.set_title("Driving an oscillator: the response depends on how close you are to $f_0$",
                  fontsize=12, fontweight="bold")

    bottom.axvline(1.0, color=GRAY, lw=0.9, ls=":")
    bottom.axhline(90, color=GRAY, lw=0.8, ls="--")
    bottom.set_ylabel("phase lag (degrees)")
    bottom.set_xlabel("driving frequency / natural frequency,  $f/f_0$")
    bottom.set_yticks([0, 90, 180])
    bottom.text(0.08, 100, "at resonance the response lags the drive by exactly 90°",
                fontsize=9.5, color=GRAY)
    bottom.set_xlim(0, 2.4)

    fig.tight_layout()
    save(fig, "ch04-response-curves")


def q_and_bandwidth():
    """How Q is read off a measured response curve."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.0, 3.6))
    q = 8.0
    ratio = np.linspace(0.6, 1.45, 900)
    amplitude = _response(ratio, q)
    peak = amplitude.max()
    ax.plot(ratio, amplitude, color=BLUE, lw=2.4)

    half_power = peak / np.sqrt(2)
    ax.axhline(half_power, color=RED, lw=1.2, ls="--")
    crossings = ratio[np.isclose(amplitude, half_power, atol=peak * 0.012)]
    lo, hi = crossings.min(), crossings.max()
    ax.plot([lo, hi], [half_power, half_power], "o", color=RED, ms=7)
    ax.annotate("", xy=(lo, half_power * 0.62), xytext=(hi, half_power * 0.62),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
    ax.text((lo + hi) / 2, half_power * 0.44, "bandwidth $\\Delta f$",
            color=RED, ha="center", fontsize=11)
    ax.text(1.02, peak * 0.97, "peak at $f_0$", fontsize=11, color=BLUE)
    ax.text(hi + 0.02, half_power, "$0.707$ of the peak\n(half the power)",
            color=RED, va="center", fontsize=10)
    ax.axvline(1.0, color=GRAY, lw=0.9, ls=":")

    ax.set_xlabel("driving frequency / natural frequency")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0.6, 1.62)
    ax.set_title("$Q = f_0/\\Delta f$ — read straight off the curve",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch04-q-and-bandwidth")


def two_mass_modes():
    """Two coupled masses have exactly two normal modes."""
    use_style()
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 3.6))

    def draw(ax, displacements, title, colour, note):
        wall_left, wall_right = 0.0, 6.0
        rest = [2.0, 4.0]
        positions = [r + 0.45 * d for r, d in zip(rest, displacements)]
        ax.plot([wall_left, wall_left], [-0.55, 0.55], color=GRAY, lw=3)
        ax.plot([wall_right, wall_right], [-0.55, 0.55], color=GRAY, lw=3)
        anchors = [wall_left] + positions + [wall_right]
        for start, end in zip(anchors[:-1], anchors[1:]):
            t = np.linspace(0, 1, 260)
            ax.plot(start + t * (end - start), 0.18 * np.sin(2 * np.pi * 7 * t),
                    color=BLUE, lw=1.2)
        for rest_x, x in zip(rest, positions):
            ax.plot([rest_x, rest_x], [-0.5, 0.5], color=GRAY, lw=0.9, ls=":", zorder=1)
            ax.add_patch(plt.Rectangle((x - 0.2, -0.28), 0.4, 0.56,
                                       facecolor=LIGHT, edgecolor="#333333", zorder=2))
        for x, d in zip(positions, displacements):
            if d:
                ax.annotate("", xy=(x + np.sign(d) * 0.75, 0), xytext=(x + np.sign(d) * 0.28, 0),
                            arrowprops=dict(arrowstyle="-|>", color=colour, lw=1.8,
                                            mutation_scale=13))
        ax.set_xlim(-0.4, 8.4)
        ax.set_ylim(-0.95, 0.95)
        ax.axis("off")
        ax.text(6.35, 0.18, title, fontsize=11.5, fontweight="bold", color=colour)
        ax.text(6.35, -0.32, note, fontsize=10, color=GRAY)

    draw(axes[0], [1, 1], "In phase — lower frequency", GREEN,
         "the middle spring\nnever stretches")
    draw(axes[1], [1, -1], "Out of phase — higher frequency", RED,
         "the middle spring\nstretches hardest")
    fig.suptitle("Two masses, two normal modes", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.86)
    save(fig, "ch04-two-mass-modes")


def mode_superposition():
    """A plucked triangular shape, rebuilt from its modes."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.4))

    x = np.linspace(0, 1, 900)
    pluck_at = 0.2
    shape = np.where(x < pluck_at, x / pluck_at, (1 - x) / (1 - pluck_at))

    left.plot(x, shape, color="#333333", lw=2.4, ls="--", label="the actual pluck")
    total = np.zeros_like(x)
    for n in range(1, 9):
        coefficient = (2 / (n * np.pi) ** 2) * np.sin(n * np.pi * pluck_at) / (pluck_at * (1 - pluck_at))
        total = total + coefficient * np.sin(n * np.pi * x)
        if n in (1, 2, 8):
            left.plot(x, total, lw=1.8, alpha=0.9,
                      color={1: BLUE, 2: GREEN, 8: RED}[n], label=f"first {n} mode" + ("s" if n > 1 else ""))
    left.set_title("A pluck is a sum of modes", fontsize=12, fontweight="bold")
    left.set_xticks([])
    left.set_yticks([])
    left.legend(loc="upper right", fontsize=9.5)
    left.set_xlabel("position along the string")

    modes = np.arange(1, 13)
    amplitudes = np.abs([(2 / (n * np.pi) ** 2) * np.sin(n * np.pi * pluck_at)
                         / (pluck_at * (1 - pluck_at)) for n in modes])
    right.vlines(modes, 0, amplitudes / amplitudes.max(), color=PURPLE, lw=2.4)
    right.plot(modes, amplitudes / amplitudes.max(), "o", color=PURPLE, ms=5)
    right.plot([5], [0], "o", color=RED, ms=9)
    right.annotate("the 5th is missing:\nthe pluck is at a node of it",
                   xy=(5, 0.02), xytext=(6.1, 0.40), fontsize=10, color=RED,
                   arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))
    right.set_xlabel("mode number $n$")
    right.set_ylabel("amplitude")
    right.set_xticks(modes)
    right.set_title("Plucked at $L/5$", fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch04-mode-superposition")


def helmholtz():
    """The Helmholtz resonator: a plug of air on a spring of air."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.4),
                                      gridspec_kw={"width_ratios": [1.0, 1.25]})

    # The cavity and neck.
    left.add_patch(plt.Circle((0.0, -0.55), 0.62, facecolor=LIGHT,
                              edgecolor="#333333", lw=1.6))
    left.add_patch(plt.Rectangle((-0.13, 0.0), 0.26, 0.62, facecolor=LIGHT,
                                 edgecolor="#333333", lw=1.6))
    left.add_patch(plt.Rectangle((-0.13, 0.36), 0.26, 0.16, facecolor=RED,
                                 edgecolor=RED, alpha=0.8))
    left.annotate("", xy=(0.34, 0.58), xytext=(0.34, 0.24),
                  arrowprops=dict(arrowstyle="<->", color=RED, lw=1.8,
                                  mutation_scale=13))
    left.text(0.46, 0.44, "the plug of air\nin the neck\n(the mass)",
              fontsize=10, color=RED, va="center")
    left.text(0.75, -0.55, "the air in the cavity\n(the spring)", fontsize=10,
              color=BLUE, va="center")
    left.annotate("", xy=(0.4, -0.55), xytext=(0.72, -0.55),
                  arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
    left.set_xlim(-1.0, 2.4)
    left.set_ylim(-1.35, 1.05)
    left.set_aspect("equal")
    left.axis("off")
    left.set_title("A bottle, and why it has one note", fontsize=12, fontweight="bold")

    # Frequency against cavity volume, for one fixed neck. A guitar's soundhole
    # is nothing like a bottle's neck -- far wider and far shorter -- so putting
    # a guitar on this curve would be meaningless; the text makes the comparison
    # instead.
    def helmholtz_frequency(volume_litres, area, length):
        return (343.0 / (2 * np.pi)) * np.sqrt(area / ((volume_litres * 1e-3) * length))

    neck_area, neck_length = 4.5e-4, 0.075
    volumes = np.linspace(0.15, 3.0, 300)
    right.plot(volumes, helmholtz_frequency(volumes, neck_area, neck_length),
               color=BLUE, lw=2.4)
    for volume, label, colour, dy in ((0.33, "a beer bottle", ORANGE, 30),
                                      (0.75, "a wine bottle", GREEN, 34)):
        f = helmholtz_frequency(volume, neck_area, neck_length)
        right.plot([volume], [f], "o", color=colour, ms=8)
        right.annotate(f"{label}\n{f:.0f} Hz", xy=(volume, f),
                       xytext=(volume + 0.22, f + dy), fontsize=10, color=colour)
    right.set_xlim(0, 3)
    right.set_xlabel("cavity volume (litres)")
    right.set_ylabel("resonant frequency (Hz)")
    right.set_title("One neck, varying cavity: $f_0 \\propto 1/\\sqrt{V}$",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch04-helmholtz")


def main():
    print("Chapter 4 figures:")
    response_curves()
    q_and_bandwidth()
    two_mass_modes()
    mode_superposition()
    helmholtz()


if __name__ == "__main__":
    main()
