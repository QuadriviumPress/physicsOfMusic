"""Audio examples for Chapter 11, Wind Instruments and Air-Column Resonance."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

F0 = 147.0     # D3, near a clarinet's lowest written notes


def wind_tone(t, f0, harmonics, rolloff=1.0, breath=0.04):
    """A sustained wind tone: a chosen set of harmonics plus a little breath noise.

    The noise is not decoration. Section 5.5 argued that a purely harmonic
    synthesis sounds sterile, and a wind instrument is the clearest case --
    without breath it is unmistakably an organ stop rather than a flute.
    """
    signal = np.zeros_like(t)
    for n in harmonics:
        signal += (1.0 / n ** rolloff) * np.sin(2 * np.pi * n * f0 * t)
    if breath:
        rng = np.random.default_rng(int(f0) + len(harmonics))
        noise = rng.normal(0, 1, t.size)
        # Roughly band-limited: a running mean removes the harshest top end.
        window = 9
        noise = np.convolve(noise, np.ones(window) / window, mode="same")
        signal += breath * noise / np.max(np.abs(noise))
    return signal


def bore_timbres():
    """Three bores of the same sounding length."""
    t = A.time_axis(2.6)
    envelope = A.envelope(t, attack=0.07, release=0.25)
    odd = list(range(1, 20, 2))
    allh = list(range(1, 17))

    clips = {
        "ch11-open-cylinder": wind_tone(t, 2 * F0, allh, rolloff=1.3),
        "ch11-stopped-cylinder": wind_tone(t, F0, odd, rolloff=1.1),
        "ch11-cone": wind_tone(t, F0, allh, rolloff=1.0),
    }
    for name, signal in clips.items():
        A.write_clip(name, A.match_level(signal * envelope))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.9), sharey=True)
    specs = [("Open cylinder", 2 * F0, allh, 1.3, figstyle.BLUE),
             ("Stopped cylinder", F0, odd, 1.1, figstyle.RED),
             ("Cone", F0, allh, 1.0, figstyle.GREEN)]
    for ax, (label, base, harmonics, rolloff, colour) in zip(axes, specs):
        freqs = np.array(harmonics) * base
        amps = 1.0 / np.array(harmonics) ** rolloff
        ax.vlines(freqs, 0, amps, color=colour, lw=2.2)
        ax.plot(freqs, amps, "o", color=colour, ms=4)
        ax.set_xlim(0, 2200)
        ax.set_xlabel("frequency (Hz)")
        ax.set_title(f"{label}\nsounds {base:.0f} Hz", fontsize=11, fontweight="bold",
                     color=colour)
    axes[0].set_ylabel("amplitude")
    fig.suptitle("Three bores of the same length", fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.74)
    figstyle.save(fig, "ch11-bore-timbres")


def overblowing():
    """A cylinder overblowing a twelfth and a cone overblowing an octave."""
    segment = 1.3
    pieces_stopped, pieces_cone = [], []
    for multiple, harmonics in ((1, list(range(1, 20, 2))), (3, list(range(1, 20, 2)))):
        t = A.time_axis(segment)
        signal = wind_tone(t, F0 * multiple, harmonics, rolloff=1.1)
        pieces_stopped.append(A.match_level(signal * A.envelope(t, attack=0.05, release=0.15)))
    for multiple in (1, 2):
        t = A.time_axis(segment)
        signal = wind_tone(t, F0 * multiple, list(range(1, 17)), rolloff=1.0)
        pieces_cone.append(A.match_level(signal * A.envelope(t, attack=0.05, release=0.15)))

    A.write_clip("ch11-overblow-twelfth", np.concatenate(pieces_stopped))
    A.write_clip("ch11-overblow-octave", np.concatenate(pieces_cone))


def bugle():
    """The notes a brass instrument can play without valves.

    Resonances 2 to 8 of a fixed tube -- which is exactly the set of notes a
    bugle call is made of, and the reason bugle calls all sound alike.
    """
    base = 116.5
    sequence = [2, 3, 4, 5, 6, 8, 6, 5, 4, 3, 2]
    pieces = []
    for resonance in sequence:
        t = A.time_axis(0.55)
        frequency = base * resonance
        signal = wind_tone(t, frequency, list(range(1, 13)), rolloff=0.85, breath=0.02)
        pieces.append(A.match_level(signal * A.envelope(t, attack=0.03, decay=0.08,
                                                        sustain=0.8, release=0.12)))
    A.write_clip("ch11-bugle", np.concatenate(pieces))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.4, 2.9))
    n = np.arange(1, 11)
    freqs = base * n
    ax.vlines(freqs, 0, 1, color=figstyle.LIGHT, lw=8)
    for resonance in sorted(set(sequence)):
        ax.vlines([base * resonance], 0, 1, color=figstyle.GREEN, lw=8)
        ax.text(base * resonance, 1.08, f"{resonance}", ha="center",
                fontsize=11, fontweight="bold", color=figstyle.GREEN)
    ax.text(base * 1, 1.08, "1", ha="center", fontsize=11, color=figstyle.GRAY)
    ax.text(base * 7, 1.08, "7", ha="center", fontsize=11, color=figstyle.RED)
    ax.annotate("the 7th is 31 cents flat\nand is avoided",
                xy=(base * 7, 0.55), xytext=(base * 7.4, 0.62),
                fontsize=9.5, color=figstyle.RED,
                arrowprops=dict(arrowstyle="->", color=figstyle.RED, lw=1.0))
    ax.set_xlabel("frequency (Hz)")
    ax.set_yticks([])
    ax.set_ylim(0, 1.35)
    ax.set_xlim(0, base * 11)
    ax.set_title("The notes a valveless brass instrument can play",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch11-bugle")


def main():
    print("Chapter 11 audio:")
    bore_timbres()
    overblowing()
    bugle()


if __name__ == "__main__":
    main()
