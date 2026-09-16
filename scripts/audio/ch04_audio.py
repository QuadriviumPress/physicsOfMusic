"""Audio examples for Chapter 4, Resonance and Normal Modes."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

F0 = 330.0


def _resonator(signal, f0, q, rate=A.RATE):
    """Pass a signal through a single damped resonance.

    A two-pole filter, stepped sample by sample. This is the same second-order
    system as the mass on a spring of Chapter 1, driven by ``signal`` instead of
    being released and left alone.
    """
    omega = 2 * np.pi * f0 / rate
    alpha = np.sin(omega) / (2 * q)
    b0, b1, b2 = alpha, 0.0, -alpha
    a0, a1, a2 = 1 + alpha, -2 * np.cos(omega), 1 - alpha
    out = np.zeros_like(signal)
    x1 = x2 = y1 = y2 = 0.0
    for index, x0 in enumerate(signal):
        y0 = (b0 * x0 + b1 * x1 + b2 * x2 - a1 * y1 - a2 * y2) / a0
        out[index] = y0
        x2, x1 = x1, x0
        y2, y1 = y1, y0
    return out


def resonance_sweep():
    """A slow sweep past a sharp resonance: nothing, then everything, then nothing."""
    duration = 7.0
    t = A.time_axis(duration)
    low, high = 120.0, 900.0
    # Sweep the frequency exponentially, so the ear hears an even glide.
    frequency = low * (high / low) ** (t / duration)
    phase = 2 * np.pi * np.cumsum(frequency) / A.RATE
    drive = np.sin(phase)
    response = _resonator(drive, F0, q=22.0)
    A.write_clip("ch04-resonance-sweep", A.match_level(response))

    # The measured response, as an experimenter would plot it.
    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.2, 3.0))
    window = int(0.02 * A.RATE)
    envelope = np.convolve(np.abs(response), np.ones(window) / window, mode="same")
    ax.plot(frequency, envelope / envelope.max(), color=figstyle.BLUE, lw=2.0)
    ax.axvline(F0, color=figstyle.GRAY, lw=0.9, ls=":")
    ax.text(F0 * 1.05, 0.9, f"$f_0 = {F0:.0f}$ Hz", fontsize=11, color=figstyle.GRAY)
    ax.set_xscale("log")
    ax.set_xlabel("driving frequency (Hz)")
    ax.set_ylabel("response")
    ax.set_yticks([])
    ax.set_xlim(low, high)
    ax.set_xticks([150, 200, 300, 400, 600, 900])
    ax.set_xticklabels(["150", "200", "300", "400", "600", "900"])
    ax.set_title("Sweeping a steady drive past one resonance",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch04-resonance-sweep")


def q_comparison():
    """The same tap through a sharp and a broad resonance."""
    duration = 2.5
    t = A.time_axis(duration)
    # A short click: broadband, so it excites whatever the resonator prefers.
    drive = np.zeros_like(t)
    drive[:int(0.002 * A.RATE)] = 1.0

    clips = {}
    for name, q in (("ch04-high-q", 120.0), ("ch04-low-q", 6.0)):
        response = _resonator(drive, F0, q)
        clips[name] = response
        A.write_clip(name, A.match_level(response))

    figstyle.use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.0))
    window = int(0.005 * A.RATE)
    for (name, q, colour, label) in (("ch04-high-q", 120.0, figstyle.BLUE, "$Q = 120$ — rings"),
                                     ("ch04-low-q", 6.0, figstyle.RED, "$Q = 6$ — thuds")):
        envelope = np.convolve(np.abs(clips[name]), np.ones(window) / window, mode="same")
        left.plot(t, envelope / envelope.max(), color=colour, lw=2.0, label=label)
    left.set_xlabel("time (s)")
    left.set_ylabel("amplitude")
    left.set_yticks([])
    left.set_xlim(0, duration)
    left.legend(fontsize=10)
    left.set_title("Struck once, then left alone", fontsize=12, fontweight="bold")

    ratio = np.linspace(0.5, 1.6, 900)
    for q, colour in ((120.0, figstyle.BLUE), (6.0, figstyle.RED)):
        response = 1.0 / np.sqrt((1 - ratio**2) ** 2 + (ratio / q) ** 2)
        right.plot(ratio * F0, response / response.max(), color=colour, lw=2.0)
    right.set_xlabel("frequency (Hz)")
    right.set_ylabel("response")
    right.set_yticks([])
    right.set_title("The same two, driven", fontsize=12, fontweight="bold")
    fig.suptitle("A long ring and a narrow peak are the same fact",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.80)
    figstyle.save(fig, "ch04-q-comparison")


def main():
    print("Chapter 4 audio:")
    resonance_sweep()
    q_comparison()


if __name__ == "__main__":
    main()
