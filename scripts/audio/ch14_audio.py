"""Audio examples for Chapter 14, Room Acoustics and Concert-Hall Design."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def impulse_response(rt60, early_gain=0.55, seconds=None, rate=A.RATE, seed=0):
    """A synthetic room impulse response: direct sound, early reflections, tail.

    Exponentially decaying noise is the standard model of a diffuse reverberant
    tail, and it is what 14.1 describes. The early reflections are placed
    individually because they are not diffuse and the chapter's argument is
    about them specifically.
    """
    seconds = seconds if seconds is not None else rt60 * 1.6 + 0.2
    n = int(seconds * rate)
    rng = np.random.default_rng(seed)
    response = np.zeros(n)
    response[0] = 1.0

    # Early reflections in the first 80 ms.
    for delay_ms in (17, 24, 31, 39, 46, 55, 63, 71):
        index = int(delay_ms * rate / 1000)
        if index < n:
            response[index] += early_gain * np.exp(-delay_ms / 90) * rng.uniform(0.5, 1.0)

    # The diffuse tail: noise under a -60 dB decay over rt60.
    t = np.arange(n) / rate
    tail = rng.normal(0, 1, n) * 10 ** (-3 * t / rt60)
    tail[:int(0.08 * rate)] = 0.0
    response += 0.30 * tail

    # Air and surfaces absorb the top end faster than the bottom.
    smoothed = np.convolve(response, np.ones(5) / 5, mode="same")
    response = 0.55 * response + 0.45 * smoothed
    return response / np.max(np.abs(response))


def phrase(seconds=3.4):
    """A short musical phrase, dry, to be put into the rooms."""
    notes = [(392.0, 0.42), (440.0, 0.42), (523.3, 0.42), (659.3, 0.85)]
    pieces = []
    for frequency, duration in notes:
        t = A.time_axis(duration)
        amplitudes = 1.0 / np.arange(1, 13) ** 1.1
        signal = A.harmonics(t, frequency, amplitudes) * np.exp(-t / 0.5)
        pieces.append(signal)
    dry = np.concatenate(pieces)
    padding = np.zeros(int(seconds * A.RATE) - dry.size)
    return np.concatenate([dry, padding])


def rooms():
    """One phrase, four rooms."""
    dry = phrase()
    A.write_clip("ch14-dry", A.match_level(dry))

    settings = [("ch14-small-room", 0.4, 0), ("ch14-chamber-hall", 1.4, 1),
                ("ch14-concert-hall", 2.1, 2), ("ch14-cathedral", 5.5, 3)]
    for name, rt60, seed in settings:
        response = impulse_response(rt60, seed=seed)
        wet = np.convolve(dry, response)[:dry.size + int(rt60 * A.RATE)]
        A.write_clip(name, A.match_level(wet))

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    for (name, rt60, seed), colour in zip(settings, figstyle.CYCLE):
        response = impulse_response(rt60, seed=seed)
        t = np.arange(response.size) / A.RATE
        window = int(0.01 * A.RATE)
        envelope = np.convolve(np.abs(response), np.ones(window) / window, mode="same")
        envelope = np.maximum(envelope, 1e-6)
        ax.plot(t, 20 * np.log10(envelope / envelope.max()), color=colour, lw=1.8,
                label=f"{name.replace('ch14-', '').replace('-', ' ')}  ($T_{{60}}={rt60}$ s)")
    ax.axhline(-60, color=figstyle.GRAY, lw=1.0, ls="--")
    ax.text(0.15, -57, "$-60$ dB", fontsize=10, color=figstyle.GRAY)
    ax.set_xlabel("time (s)")
    ax.set_ylabel("level (dB)")
    ax.set_xlim(0, 7)
    ax.set_ylim(-75, 5)
    ax.legend(fontsize=9.5, loc="upper right")
    ax.set_title("Decay curves of the four rooms", fontsize=12, fontweight="bold")
    fig.tight_layout()
    figstyle.save(fig, "ch14-rooms")


def main():
    print("Chapter 14 audio:")
    rooms()


if __name__ == "__main__":
    main()
