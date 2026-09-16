"""Figures for Chapter 9, Musical Scales and Tuning Systems."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style

NOTE_NAMES = ["C", "C♯", "D", "E♭", "E", "F",
              "F♯", "G", "A♭", "A", "B♭", "B", "C"]


def cents(ratio):
    return 1200.0 * np.log2(ratio)


def pythagorean_ratios():
    """Twelve notes from a chain of pure fifths, folded into one octave."""
    ratios = []
    for step in range(-1, 11):
        value = (3 / 2) ** step
        while value < 1:
            value *= 2
        while value >= 2:
            value /= 2
        ratios.append(value)
    return np.array(sorted(ratios))


JUST_RATIOS = np.array([1, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 9/5, 15/8])
EQUAL_RATIOS = np.array([2 ** (n / 12) for n in range(12)])


def comma_spiral():
    """Twelve pure fifths overshoot seven octaves."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.8),
                                      gridspec_kw={"width_ratios": [1.0, 1.15]})

    # The chain of fifths folded into one octave. A spiral drawn in angle does
    # not read: a fifth is 0.585 of a turn, so consecutive points jump across
    # the circle and the picture becomes a star polygon rather than a drift.
    # Laying the pitch classes on a line shows the drift directly.
    steps = np.arange(0, 13)
    pitch_class = (steps * cents(1.5)) % 1200.0
    for step, position in zip(steps, pitch_class):
        colour = GREEN if step == 0 else (RED if step == 12 else BLUE)
        size = 10 if step in (0, 12) else 5
        left.plot([position], [step], "o", color=colour, ms=size)
        left.plot([position, position], [-0.6, step], color=colour, lw=0.7, alpha=0.35)
    left.plot(pitch_class, steps, color=BLUE, lw=0.9, alpha=0.5)
    left.set_xlim(-60, 1260)
    left.set_ylim(-1.2, 13.2)
    left.set_xlabel("pitch class (cents within the octave)")
    left.set_ylabel("fifths taken")
    left.set_xticks([0, 300, 600, 900, 1200])
    left.annotate("start: C", xy=(0, 0), xytext=(60, 1.1), fontsize=10.5, color=GREEN)
    left.annotate(f"after 12 fifths:\n{pitch_class[12]:.1f} cents sharp of C",
                  xy=(pitch_class[12], 12), xytext=(150, 11.0),
                  fontsize=10.5, color=RED,
                  arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
    left.set_title("Each fifth, folded back into one octave",
                   fontsize=12, fontweight="bold")

    # The arithmetic, in cents.
    twelve_fifths = 12 * cents(1.5)
    seven_octaves = 7 * 1200.0
    bars = right.bar(["12 pure fifths", "7 octaves"], [twelve_fifths, seven_octaves],
                     color=[BLUE, GREEN], width=0.5)
    for bar, value in zip(bars, (twelve_fifths, seven_octaves)):
        right.text(bar.get_x() + bar.get_width() / 2, value + 30,
                   f"{value:.1f} cents", ha="center", fontsize=11, fontweight="bold")
    right.set_ylim(8000, 8800)
    right.set_ylabel("cents")
    right.annotate("", xy=(0.5, twelve_fifths), xytext=(0.5, seven_octaves),
                   arrowprops=dict(arrowstyle="<->", color=RED, lw=2.0))
    right.plot([0, 0.5], [twelve_fifths] * 2, color=RED, lw=1.0, ls=":")
    right.plot([0.5, 1], [seven_octaves] * 2, color=RED, lw=1.0, ls=":")
    right.text(0.5, seven_octaves - 90,
               f"the Pythagorean comma:\n{twelve_fifths - seven_octaves:.1f} cents",
               fontsize=11, color=RED, ha="center", va="top", fontweight="bold")
    right.set_title("A gap of about a quarter of a semitone",
                    fontsize=12, fontweight="bold")
    for side in ("right", "top"):
        right.spines[side].set_visible(False)

    fig.tight_layout()
    save(fig, "ch09-comma-spiral")


def system_comparison():
    """Every note of the chromatic scale, in three tunings, against equal temperament."""
    use_style()
    fig, ax = plt.subplots(figsize=(9.4, 4.0))

    pyth = pythagorean_ratios()
    x = np.arange(12)
    width = 0.27
    for offset, ratios, label, colour in (
            (-width, pyth, "Pythagorean", BLUE),
            (0.0, JUST_RATIOS, "Just intonation", GREEN),
            (width, EQUAL_RATIOS, "Equal temperament", GRAY)):
        deviation = cents(ratios) - cents(EQUAL_RATIOS)
        ax.bar(x + offset, deviation, width=width, color=colour, label=label)

    ax.axhline(0, color="#333333", lw=1.0)
    ax.axhspan(-6, 6, color=LIGHT, alpha=0.6, zorder=0)
    ax.text(11.4, 7, "within about 6 cents:\nhard to hear", fontsize=9.5,
            color=GRAY, ha="right")
    ax.set_xticks(x)
    ax.set_xticklabels(NOTE_NAMES[:12])
    ax.set_ylabel("cents from equal temperament")
    ax.set_xlabel("note of the chromatic scale, from C")
    ax.legend(fontsize=10, loc="lower left")
    ax.set_title("Three tunings compared, note by note", fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch09-system-comparison")


def interval_errors():
    """How far each system's fifths and thirds are from pure."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.4), sharey=True)

    pure_fifth, pure_third = cents(1.5), cents(1.25)
    systems = {
        "Pythagorean": (cents(1.5), cents((3 / 2) ** 4 / 4)),
        "Quarter-comma\nmeantone": (cents(1.5) - 5.377, pure_third),
        "Just (in C)": (pure_fifth, pure_third),
        "Equal": (700.0, 400.0),
    }

    names = list(systems)
    fifth_error = [systems[n][0] - pure_fifth for n in names]
    third_error = [systems[n][1] - pure_third for n in names]

    for ax, errors, title in ((left, fifth_error, "The perfect fifth"),
                              (right, third_error, "The major third")):
        colours = [RED if abs(e) > 10 else (ORANGE if abs(e) > 5 else GREEN) for e in errors]
        bars = ax.bar(range(len(names)), errors, color=colours, width=0.55)
        for bar, value in zip(bars, errors):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    value + (1.0 if value >= 0 else -2.6),
                    f"{value:+.1f}", ha="center", fontsize=10.5, fontweight="bold")
        ax.axhline(0, color="#333333", lw=1.0)
        ax.axhspan(-6, 6, color=LIGHT, alpha=0.6, zorder=0)
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels(names, fontsize=9.5)
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.set_ylim(-18, 18)
    left.set_ylabel("cents from pure")
    fig.suptitle("Every system is a choice about where to put the error",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.82)
    save(fig, "ch09-interval-errors")


def wolf_fifth():
    """Just intonation in C: which fifths are pure and which is not."""
    use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.4))

    # The six *perfect* fifths available within the just C major scale. B-D-F is
    # a diminished fifth rather than a perfect one and belongs to a different
    # discussion, so it is excluded rather than plotted at -92 cents.
    scale = {"C": 1.0, "D": 9/8, "E": 5/4, "F": 4/3, "G": 3/2, "A": 5/3, "B": 15/8}
    pairs = [("C", "G"), ("D", "A"), ("E", "B"), ("F", "C"), ("G", "D"), ("A", "E")]
    labels, errors = [], []
    for root, fifth_note in pairs:
        ratio = scale[fifth_note] / scale[root]
        while ratio < 1.2:
            ratio *= 2
        while ratio >= 2.4:
            ratio /= 2
        labels.append(f"{root}\u2013{fifth_note}")
        errors.append(cents(ratio) - cents(1.5))

    colours = [RED if abs(e) > 15 else GREEN for e in errors]
    bars = ax.bar(range(len(labels)), errors, color=colours, width=0.55)
    for bar, value in zip(bars, errors):
        ax.text(bar.get_x() + bar.get_width() / 2, value - 2.2 if value < 0 else value + 0.8,
                f"{value:+.1f}", ha="center", fontsize=10.5, fontweight="bold")
    ax.axhline(0, color="#333333", lw=1.0)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_ylabel("cents from a pure fifth")
    ax.annotate("the wolf", xy=(1, errors[1]), xytext=(2.0, errors[1] + 5),
                fontsize=11.5, color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.4))
    ax.set_ylim(-27, 7)
    ax.set_title("Perfect fifths within a just C major scale: five are pure, one howls",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    save(fig, "ch09-wolf-fifth")


def main():
    print("Chapter 9 figures:")
    comma_spiral()
    system_comparison()
    interval_errors()
    wolf_fifth()


if __name__ == "__main__":
    main()
