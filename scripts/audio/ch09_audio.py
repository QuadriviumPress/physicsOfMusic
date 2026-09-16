"""Audio examples for Chapter 9, Musical Scales and Tuning Systems."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

C4 = 261.63
PARTIALS = np.arange(1, 9)
AMPLITUDES = 0.82 ** PARTIALS


def organ_tone(t, frequency):
    """A steady tone with enough partials for tuning differences to beat audibly."""
    signal = np.zeros_like(t)
    for n, a in zip(PARTIALS, AMPLITUDES):
        signal += a * np.sin(2 * np.pi * n * frequency * t)
    return signal


def chord(t, root, ratios):
    return sum(organ_tone(t, root * r) for r in ratios)


def third_comparison():
    """A major third, tuned pure and tuned as a piano tunes it."""
    t = A.time_axis(3.0)
    envelope = A.envelope(t, attack=0.08, release=0.35)
    just = organ_tone(t, C4) + organ_tone(t, C4 * 5 / 4)
    equal = organ_tone(t, C4) + organ_tone(t, C4 * 2 ** (4 / 12))
    A.write_clip("ch09-third-just", A.match_level(just * envelope))
    A.write_clip("ch09-third-equal", A.match_level(equal * envelope))

    # The beat that gives the tempered third away.
    lower_fifth_partial = 5 * C4
    upper_fourth_partial = 4 * C4 * 2 ** (4 / 12)
    beat = abs(upper_fourth_partial - lower_fifth_partial)

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 3.0))
    for label, ratio, colour, offset in (("just 5:4", 5 / 4, figstyle.GREEN, 0.0),
                                         ("equal-tempered", 2 ** (4 / 12), figstyle.RED, 0.06)):
        lower = PARTIALS * C4
        upper = PARTIALS * C4 * ratio
        ax.vlines(lower, offset, offset + AMPLITUDES * 0.4, color=figstyle.GRAY, lw=1.6)
        ax.vlines(upper, offset, offset + AMPLITUDES * 0.4, color=colour, lw=2.2,
                  label=f"upper note, {label}")
    ax.axvline(lower_fifth_partial, color=figstyle.GRAY, lw=0.9, ls=":")
    ax.annotate(f"the lower note's 5th partial and the upper note's 4th\n"
                f"differ by {beat:.1f} Hz in equal temperament, and not at all when pure",
                xy=(lower_fifth_partial, 0.52), xytext=(1500, 0.60),
                fontsize=10, color=figstyle.RED,
                arrowprops=dict(arrowstyle="->", color=figstyle.RED, lw=1.1))
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("amplitude")
    ax.set_yticks([])
    ax.set_xlim(0, 2600)
    ax.set_ylim(0, 0.78)
    ax.legend(fontsize=9.5, loc="upper left")
    ax.set_title("A major third on C: where the beating comes from",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch09-third-comparison")


def triad_comparison():
    """A C major triad, just and equal-tempered."""
    t = A.time_axis(3.0)
    envelope = A.envelope(t, attack=0.08, release=0.35)
    just = chord(t, C4, [1, 5 / 4, 3 / 2])
    equal = chord(t, C4, [1, 2 ** (4 / 12), 2 ** (7 / 12)])
    A.write_clip("ch09-triad-just", A.match_level(just * envelope))
    A.write_clip("ch09-triad-equal", A.match_level(equal * envelope))


def wolf():
    """A pure fifth and the wolf fifth of just intonation, side by side."""
    t = A.time_axis(2.8)
    envelope = A.envelope(t, attack=0.08, release=0.3)
    pure = organ_tone(t, C4) + organ_tone(t, C4 * 3 / 2)
    # D to A in just C major: (5/3) / (9/8) = 40/27, a syntonic comma narrow.
    wolf_ratio = (5 / 3) / (9 / 8)
    d4 = C4 * 9 / 8
    howling = organ_tone(t, d4) + organ_tone(t, d4 * wolf_ratio)
    A.write_clip("ch09-fifth-pure", A.match_level(pure * envelope))
    A.write_clip("ch09-fifth-wolf", A.match_level(howling * envelope))


def modulation():
    """The same progression in just intonation, in C and then in D.

    Just intonation is tuned for one key. Played in the key it was tuned for it
    is beautiful; moved up a tone, with the same twelve fixed pitches, the same
    chords are unusable. This is the argument of 9.3 in eight seconds.
    """
    beat = 0.9
    t = A.time_axis(beat)
    envelope = A.envelope(t, attack=0.04, release=0.2)

    # Twelve fixed pitches, tuned just for C.
    just_scale = {0: 1.0, 2: 9 / 8, 4: 5 / 4, 5: 4 / 3, 7: 3 / 2, 9: 5 / 3, 11: 15 / 8,
                  1: 16 / 15, 3: 6 / 5, 6: 45 / 32, 8: 8 / 5, 10: 9 / 5}

    def triad(root_semitone):
        pitches = []
        for interval in (0, 4, 7):
            semitone = (root_semitone + interval) % 12
            octave = (root_semitone + interval) // 12
            pitches.append(C4 * just_scale[semitone] * (2 ** octave))
        return A.match_level(sum(organ_tone(t, f) for f in pitches) * envelope)

    in_c = [triad(0), triad(5), triad(7), triad(0)]           # I IV V I in C
    in_d = [triad(2), triad(7), triad(9), triad(2)]           # I IV V I in D
    gap = np.zeros(int(0.5 * A.RATE))
    A.write_clip("ch09-just-in-c", np.concatenate(in_c))
    A.write_clip("ch09-just-in-d", np.concatenate(in_d))


def main():
    print("Chapter 9 audio:")
    third_comparison()
    triad_comparison()
    wolf()
    modulation()


if __name__ == "__main__":
    main()
