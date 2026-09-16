"""Audio examples for Chapter 5, Fourier Analysis, Harmonics, and Timbre.

Every clip here is 220 Hz (A3) and every clip is matched in RMS level, so the
only thing that differs between them is which harmonics are present. That is
the whole argument of the chapter, and it is the one comparison a recording of
real instruments could not make cleanly.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

import audiolib as A  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

F0 = 220.0
N = 24


def sine():
    t = A.time_axis()
    A.clip_and_figure("ch05-sine", A.sine(t, F0), F0,
                      title="A pure tone: one partial only")


def sawtooth():
    t = A.time_axis()
    signal = A.harmonics(t, F0, A.sawtooth_amplitudes(N))
    A.clip_and_figure("ch05-sawtooth", signal, F0,
                      title="Sawtooth: every harmonic, amplitude falling as $1/n$",
                      color=figstyle.RED)


def square():
    t = A.time_axis()
    signal = A.harmonics(t, F0, A.square_amplitudes(N))
    A.clip_and_figure("ch05-square", signal, F0,
                      title="Square: odd harmonics only, amplitude falling as $1/n$",
                      color=figstyle.GREEN)


def build_up():
    """The harmonic series assembled one partial at a time.

    Each second adds the next harmonic of a sawtooth. The point is audible
    rather than visual: the pitch never changes, and the tone brightens.
    """
    seconds_each = 0.8
    pieces = []
    for count in range(1, 9):
        t = A.time_axis(seconds_each)
        amplitudes = A.sawtooth_amplitudes(count)
        piece = A.harmonics(t, F0, amplitudes) * A.envelope(t, attack=0.02, release=0.05)
        pieces.append(A.match_level(piece))
    signal = np.concatenate(pieces)
    A.write_clip("ch05-harmonic-build-up", signal)

    # The figure for this one is a picture of the recipe, not of the waveform:
    # a waveform of an eight-part sequence is unreadable at page size.
    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.0, 3.0))
    for step in range(1, 9):
        amplitudes = A.sawtooth_amplitudes(step)
        ax.vlines(np.arange(1, step + 1) * F0, 0, amplitudes + step * 0.0,
                  color=figstyle.CYCLE[(step - 1) % len(figstyle.CYCLE)],
                  lw=2.0, alpha=0.85)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("amplitude (arb.)")
    ax.set_title("Eight steps: each adds the next harmonic of 220 Hz", fontsize=12,
                 fontweight="bold")
    ax.set_xlim(0, 9 * F0)
    fig.tight_layout()
    figstyle.save(fig, "ch05-harmonic-build-up")


def three_waveforms():
    """One figure for the three-clip comparison directive."""
    figstyle.use_style()
    t = A.time_axis(0.02)
    span = int(round(3 * A.RATE / F0))
    fig, axes = plt.subplots(2, 3, figsize=(9.5, 4.4))
    specs = [
        ("Sine", np.array([1.0]), figstyle.BLUE),
        ("Sawtooth", A.sawtooth_amplitudes(N), figstyle.RED),
        ("Square", A.square_amplitudes(N), figstyle.GREEN),
    ]
    for column, (name, amplitudes, color) in enumerate(specs):
        signal = A.match_level(A.harmonics(t, F0, amplitudes))
        figstyle.waveform(axes[0][column], t[:span], signal[:span], color=color)
        axes[0][column].set_title(name, fontsize=12, fontweight="bold")
        freqs = np.arange(1, len(amplitudes) + 1) * F0
        figstyle.spectrum(axes[1][column], freqs, amplitudes / amplitudes.max(), color=color)
        axes[1][column].set_xlim(0, 12 * F0)
        if column:
            axes[0][column].set_ylabel("")
            axes[1][column].set_ylabel("")
    fig.suptitle("Same pitch, same level, three spectra", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.87)
    figstyle.save(fig, "ch05-three-waveforms")


def phase_scramble():
    """Identical spectra, wildly different waveforms, near-identical sound.

    This is the cleanest demonstration in the book that timbre lives in the
    spectrum rather than in the shape of the waveform, and it only works as
    audio -- the two pictures look nothing alike.
    """
    t = A.time_axis()
    amplitudes = A.sawtooth_amplitudes(16)
    aligned = A.harmonics(t, F0, amplitudes)
    rng = np.random.default_rng(11)
    phases = rng.uniform(0, 2 * np.pi, amplitudes.size)
    scrambled = A.harmonics(t, F0, amplitudes, phases)
    for name, signal in (("ch05-phase-aligned", aligned), ("ch05-phase-scrambled", scrambled)):
        A.write_clip(name, A.match_level(signal * A.envelope(t, attack=0.03, release=0.25)))


def attack_stripped():
    """The same note with and without its first tenth of a second.

    Cutting the attack off a note is the classic demonstration that transients
    carry an instrument's identity. Here the steady state is deliberately
    identical, so everything a listener notices is in the onset.
    """
    t = A.time_axis(2.0)
    amplitudes = A.sawtooth_amplitudes(14)

    # A struck attack: the high partials arrive first and die first.
    with_attack = np.zeros_like(t)
    for index, amplitude in enumerate(amplitudes, start=1):
        onset = 0.004 * index
        rise = np.clip((t - onset) / 0.012, 0, 1)
        with_attack += amplitude * np.sin(2 * np.pi * index * F0 * t) * rise * np.exp(-t / (1.1 / index ** 0.5))

    # The same tone faded in gently, with no onset structure at all.
    without = A.harmonics(t, F0, amplitudes) * A.envelope(t, attack=0.35, release=0.3)

    A.write_clip("ch05-with-attack", A.match_level(with_attack))
    A.write_clip("ch05-without-attack", A.match_level(without))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 2.9), sharey=True)
    window = int(0.006 * A.RATE)
    for ax, signal, title, colour in (
            (axes[0], with_attack, "With its attack", figstyle.RED),
            (axes[1], without, "Faded in instead", figstyle.BLUE)):
        envelope = np.convolve(np.abs(signal), np.ones(window) / window, mode="same")
        ax.plot(t, envelope / envelope.max(), color=colour, lw=2.0)
        ax.set_xlabel("time (s)")
        ax.set_title(title, fontsize=12, fontweight="bold", color=colour)
        ax.set_xlim(0, 2.0)
    axes[0].set_ylabel("amplitude")
    axes[0].set_yticks([])
    fig.suptitle("Same steady-state spectrum, different first tenth of a second",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    figstyle.save(fig, "ch05-attack-compare")


def main():
    print("Chapter 5 audio:")
    sine()
    sawtooth()
    square()
    build_up()
    three_waveforms()
    phase_scramble()
    attack_stripped()


if __name__ == "__main__":
    main()
