"""Audio examples for Chapter 2, Wave Motion and the Speed of Sound."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402


def speed_of_sound(temperature):
    """The standard linear fit, good to a fraction of a percent over musical temperatures."""
    return 331.3 + 0.606 * temperature


def cold_and_warm():
    """The same pipe, played cold and warm.

    A wind instrument's sounding length is fixed; its pitch follows the speed of
    sound, which follows the temperature. This is why orchestras warm up their
    instruments and not just their players.
    """
    reference = 20.0
    tuned_to = 440.0
    amplitudes = np.array([1.0, 0.35, 0.5, 0.18, 0.12, 0.05])
    clips = {}
    for name, temperature in (("ch02-pipe-cold", 5.0), ("ch02-pipe-warm", 20.0)):
        frequency = tuned_to * speed_of_sound(temperature) / speed_of_sound(reference)
        t = A.time_axis(2.5)
        signal = A.harmonics(t, frequency, amplitudes) * A.envelope(t, attack=0.06, release=0.2)
        signal = A.match_level(signal)
        A.write_clip(name, signal)
        clips[name] = frequency

    cold, warm = clips["ch02-pipe-cold"], clips["ch02-pipe-warm"]
    cents = 1200 * np.log2(cold / warm)

    figstyle.use_style()
    fig, ax = plt.subplots(figsize=(8.0, 2.8))
    temps = np.linspace(0, 35, 200)
    shift = 1200 * np.log2(speed_of_sound(temps) / speed_of_sound(reference))
    ax.plot(temps, shift, color=figstyle.BLUE, lw=2.2)
    ax.axhline(0.0, color=figstyle.GRAY, lw=0.8)
    for temperature, colour, label in ((5.0, figstyle.ORANGE, "cold"), (20.0, figstyle.GREEN, "warm")):
        value = 1200 * np.log2(speed_of_sound(temperature) / speed_of_sound(reference))
        frequency = tuned_to * speed_of_sound(temperature) / speed_of_sound(reference)
        ax.plot([temperature], [value], "o", color=colour, ms=8)
        ax.annotate(f"{label}: {temperature:.0f} °C\n{frequency:.1f} Hz  ({value:+.0f} cents)",
                    xy=(temperature, value), xytext=(temperature + 1.4, value + (6 if value > 0 else -14)),
                    fontsize=10, color=colour)
    ax.set_xlabel("air temperature inside the instrument (°C)")
    ax.set_ylabel("pitch shift (cents)")
    ax.set_title(f"A pipe tuned to A440 at 20 °C, played at 5 °C: {cents:+.0f} cents",
                 fontsize=12, fontweight="bold")
    ax.set_xlim(0, 35)
    fig.tight_layout()
    figstyle.save(fig, "ch02-pipe-temperature")


def doppler_pass():
    """A source passing the listener at constant speed.

    The geometry is exact rather than a two-step up-then-down: the observed
    frequency depends on the component of the source velocity along the line of
    sight, so the pitch glides continuously and falls fastest at closest
    approach. That glide is the audible signature, and a simple two-tone
    caricature misses it.
    """
    v_sound = 343.0
    v_source = 30.0            # about 110 km/h
    miss_distance = 12.0       # how far the source passes from the listener
    emitted = 620.0
    duration = 6.0

    t = A.time_axis(duration)
    # Position of the source relative to closest approach.
    x = v_source * (t - duration / 2)
    distance = np.hypot(x, miss_distance)
    # Rate of change of distance: positive means receding.
    closing = v_source * x / distance
    observed = emitted * v_sound / (v_sound + closing)

    # Integrate the instantaneous frequency to get the phase, or the pitch glide
    # will not be continuous.
    phase = 2 * np.pi * np.cumsum(observed) / A.RATE
    amplitudes = np.array([1.0, 0.6, 0.4, 0.25, 0.15])
    signal = np.zeros_like(t)
    for index, amplitude in enumerate(amplitudes, start=1):
        signal += amplitude * np.sin(index * phase)
    # Loudness falls off with distance too; without it the pass sounds unreal.
    signal *= (miss_distance / distance) ** 1.0
    signal = A.match_level(signal)
    A.write_clip("ch02-doppler-pass", signal)

    figstyle.use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.0))
    left.plot(t, observed, color=figstyle.RED, lw=2.2)
    left.axhline(emitted, color=figstyle.GRAY, lw=1.0, ls=":")
    left.text(0.15, emitted + 3, "frequency emitted", fontsize=9.5, color=figstyle.GRAY)
    left.set_xlabel("time (s)")
    left.set_ylabel("frequency heard (Hz)")
    left.set_title("The pitch glides, it does not step", fontsize=12, fontweight="bold")
    left.set_xlim(0, duration)

    right.plot(t, (miss_distance / distance), color=figstyle.BLUE, lw=2.2)
    right.set_xlabel("time (s)")
    right.set_ylabel("relative amplitude")
    right.set_title("and it is loudest at closest approach", fontsize=12, fontweight="bold")
    right.set_xlim(0, duration)
    fig.tight_layout()
    figstyle.save(fig, "ch02-doppler-pass")


def main():
    print("Chapter 2 audio:")
    cold_and_warm()
    doppler_pass()


if __name__ == "__main__":
    main()
