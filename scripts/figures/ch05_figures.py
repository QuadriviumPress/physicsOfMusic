"""Figures for Chapter 5, Fourier Analysis, Harmonics, and Timbre."""

import numpy as np
import matplotlib.pyplot as plt

from figstyle import BLUE, GRAY, GREEN, LIGHT, ORANGE, PURPLE, RED, save, use_style


def building_a_sawtooth():
    """Adding harmonics one at a time, and watching a sawtooth appear."""
    use_style()
    fig, axes = plt.subplots(2, 3, figsize=(9.4, 4.4), sharex=True, sharey=True)
    t = np.linspace(0, 2, 1200)
    target = 2 * (t % 1.0) - 1.0

    for index, (ax, count) in enumerate(zip(axes.flat, (1, 2, 3, 5, 10, 40))):
        partial = np.zeros_like(t)
        for n in range(1, count + 1):
            partial += (2 / (np.pi * n)) * ((-1) ** (n + 1)) * np.sin(2 * np.pi * n * t)
        ax.plot(t, target, color=GRAY, lw=1.0, ls="--")
        ax.plot(t, partial, color=BLUE if count < 40 else GREEN, lw=1.9)
        ax.set_title(f"{count} harmonic" + ("s" if count > 1 else ""),
                     fontsize=11, fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])
        for side in ("left", "right", "top", "bottom"):
            ax.spines[side].set_visible(False)
    axes[1][2].text(0.03, -1.75, "the overshoot at the jump never goes away\n"
                                 "however many harmonics are added",
                    fontsize=9.5, color=RED)
    fig.suptitle("A sawtooth, assembled from sine waves", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.86)
    save(fig, "ch05-building-a-sawtooth")


def waveform_and_spectrum_grid():
    """Four classic waveforms, each with its spectrum beneath."""
    use_style()
    fig, axes = plt.subplots(2, 4, figsize=(9.6, 4.4))
    t = np.linspace(0, 2, 1400)
    n_max = 20
    modes = np.arange(1, n_max + 1)

    def build(amplitudes, signs=None):
        signal = np.zeros_like(t)
        for n, a in zip(modes, amplitudes):
            sign = 1 if signs is None else signs[n - 1]
            signal += sign * a * np.sin(2 * np.pi * n * t)
        return signal

    sine_a = np.zeros(n_max); sine_a[0] = 1.0
    saw_a = 1.0 / modes
    square_a = np.where(modes % 2, 1.0 / modes, 0.0)
    tri_a = np.where(modes % 2, 1.0 / modes ** 2, 0.0)

    specs = [
        ("Sine", sine_a, BLUE, "one partial"),
        ("Sawtooth", saw_a, RED, "all $n$, as $1/n$"),
        ("Square", square_a, GREEN, "odd $n$, as $1/n$"),
        ("Triangle", tri_a, PURPLE, "odd $n$, as $1/n^2$"),
    ]

    for column, (name, amplitudes, colour, note) in enumerate(specs):
        wave = build(amplitudes)
        top, bottom = axes[0][column], axes[1][column]
        top.plot(t, wave / np.max(np.abs(wave)), color=colour, lw=1.9)
        top.set_title(name, fontsize=12, fontweight="bold", color=colour)
        top.set_xticks([]); top.set_yticks([])
        top.set_ylim(-1.35, 1.35)
        for side in ("left", "right", "top", "bottom"):
            top.spines[side].set_visible(False)

        keep = amplitudes > 0
        bottom.vlines(modes[keep], 0, amplitudes[keep], color=colour, lw=2.0)
        bottom.plot(modes[keep], amplitudes[keep], "o", color=colour, ms=4)
        bottom.set_ylim(0, 1.15)
        bottom.set_xlim(0, n_max + 1)
        bottom.set_xticks([1, 5, 10, 15, 20])
        bottom.set_xlabel("harmonic number")
        bottom.text(0.5, 0.80, note, transform=bottom.transAxes, ha="center", fontsize=10)
        if column:
            bottom.set_yticks([])
        else:
            bottom.set_ylabel("amplitude")

    fig.suptitle("Four waveforms, and what each is made of", fontsize=13, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    save(fig, "ch05-waveform-spectrum-grid")


def phase_does_not_matter():
    """Two signals with identical spectra and wildly different waveforms."""
    use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.4, 2.9),
                             gridspec_kw={"width_ratios": [1, 1, 1]})
    t = np.linspace(0, 2, 1600)
    modes = np.arange(1, 13)
    amplitudes = 1.0 / modes

    aligned = sum(a * np.sin(2 * np.pi * n * t) for n, a in zip(modes, amplitudes))
    rng = np.random.default_rng(11)
    phases = rng.uniform(0, 2 * np.pi, modes.size)
    scrambled = sum(a * np.sin(2 * np.pi * n * t + p)
                    for n, a, p in zip(modes, amplitudes, phases))

    for ax, signal, title, colour in ((axes[0], aligned, "Phases aligned", BLUE),
                                      (axes[1], scrambled, "Phases scrambled", RED)):
        ax.plot(t, signal / np.max(np.abs(signal)), color=colour, lw=1.8)
        ax.set_title(title, fontsize=11.5, fontweight="bold", color=colour)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_ylim(-1.3, 1.3)
        for side in ("left", "right", "top", "bottom"):
            ax.spines[side].set_visible(False)

    axes[2].vlines(modes, 0, amplitudes, color=GRAY, lw=2.2)
    axes[2].plot(modes, amplitudes, "o", color=GRAY, ms=4)
    axes[2].set_title("Both spectra — identical", fontsize=11.5, fontweight="bold")
    axes[2].set_xlabel("harmonic number")
    axes[2].set_ylabel("amplitude")
    axes[2].set_xlim(0, 13)

    fig.suptitle("The same sound, twice: phase changes the picture, not the timbre",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    save(fig, "ch05-phase-does-not-matter")


def adsr_envelope():
    """The four-part envelope, with three instruments sketched on it."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.2, 3.2))

    t = np.linspace(0, 1.6, 900)
    attack, decay, sustain, release = 0.08, 0.22, 0.6, 0.35
    envelope = np.ones_like(t)
    envelope[t < attack] = t[t < attack] / attack
    mask = (t >= attack) & (t < attack + decay)
    envelope[mask] = 1 - (1 - sustain) * (t[mask] - attack) / decay
    envelope[(t >= attack + decay) & (t < 1.6 - release)] = sustain
    tail = t >= 1.6 - release
    envelope[tail] = sustain * (1.6 - t[tail]) / release

    left.plot(t, envelope, color=BLUE, lw=2.4)
    left.fill_between(t, 0, envelope, color=LIGHT, alpha=0.5)
    for x, label in ((attack / 2, "A"), (attack + decay / 2, "D"),
                     ((attack + decay + 1.6 - release) / 2, "S"), (1.6 - release / 2, "R")):
        left.text(x, 1.12, label, ha="center", fontsize=13, fontweight="bold", color=RED)
    for boundary in (attack, attack + decay, 1.6 - release):
        left.axvline(boundary, color=GRAY, lw=0.8, ls=":")
    left.set_xlabel("time (s)")
    left.set_ylabel("amplitude")
    left.set_yticks([])
    left.set_ylim(0, 1.3)
    left.set_title("Attack, decay, sustain, release", fontsize=12, fontweight="bold")

    shapes = {
        "Plucked string": np.exp(-t / 0.42),
        "Bowed string": np.clip(t / 0.18, 0, 1) * np.clip((1.6 - t) / 0.2, 0, 1),
        "Struck bell": np.exp(-t / 1.6),
    }
    for (name, shape), colour in zip(shapes.items(), (RED, GREEN, PURPLE)):
        right.plot(t, shape, color=colour, lw=2.2, label=name)
    right.set_xlabel("time (s)")
    right.set_ylabel("amplitude")
    right.set_yticks([])
    right.set_ylim(0, 1.25)
    right.legend(fontsize=10, loc="upper right")
    right.set_title("Three instruments, three envelopes", fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch05-adsr")


def spectrogram_example():
    """A spectrogram of a note whose spectrum changes as it decays."""
    use_style()
    rate = 8000
    duration = 2.0
    t = np.arange(int(rate * duration)) / rate
    f0 = 220.0
    signal = np.zeros_like(t)
    # High partials die first, which is what a real plucked note does.
    for n in range(1, 13):
        decay = 0.9 / (n ** 0.9)
        signal += (1.0 / n) * np.sin(2 * np.pi * n * f0 * t) * np.exp(-t / decay)

    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.4),
                                      gridspec_kw={"width_ratios": [1.0, 1.25]})
    window = int(0.01 * rate)
    envelope = np.convolve(np.abs(signal), np.ones(window) / window, mode="same")
    left.plot(t, envelope, color=BLUE, lw=1.8)
    left.set_xlabel("time (s)")
    left.set_ylabel("amplitude")
    left.set_yticks([])
    left.set_title("The waveform tells you when", fontsize=12, fontweight="bold")

    right.specgram(signal, NFFT=512, Fs=rate, noverlap=384, cmap="magma",
                   vmin=-95, vmax=-25)
    right.set_ylim(0, 2800)
    right.set_xlabel("time (s)")
    right.set_ylabel("frequency (Hz)")
    right.set_title("The spectrogram tells you when and what",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch05-spectrogram")


def formants_and_inharmonicity():
    """A fixed filter over a moving fundamental, and a stretched partial series."""
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.4, 3.4))

    # Formants: the envelope stays put while the harmonics move.
    freqs = np.linspace(0, 4000, 900)
    def resonance(f, centre, width):
        return 1.0 / np.sqrt(1 + ((f - centre) / width) ** 2 * 4)
    envelope = (resonance(freqs, 700, 120) + 0.8 * resonance(freqs, 1150, 160)
                + 0.45 * resonance(freqs, 2600, 350))
    envelope = envelope / envelope.max()
    left.plot(freqs, envelope, color=GRAY, lw=2.0, ls="--", label="the vocal tract's filter")
    for f0, colour, label in ((130, BLUE, "low note"), (330, RED, "high note")):
        partials = np.arange(1, int(4000 / f0) + 1) * f0
        amps = np.interp(partials, freqs, envelope) / np.arange(1, partials.size + 1) ** 0.3
        left.vlines(partials, 0, amps, color=colour, lw=1.8, alpha=0.85, label=label)
    left.set_xlabel("frequency (Hz)")
    left.set_ylabel("amplitude")
    left.set_yticks([])
    left.legend(fontsize=9.5)
    left.set_title("Formants stay put as the pitch moves", fontsize=12, fontweight="bold")

    # Inharmonicity: partials stretched above exact multiples.
    n = np.arange(1, 17)
    b = 4.0e-4
    stretched = n * np.sqrt(1 + b * n ** 2)
    cents = 1200 * np.log2(stretched / n)
    right.plot(n, cents, "o-", color=RED, lw=2.0, ms=6)
    right.axhline(0.0, color=GRAY, lw=1.0, ls="--")
    right.text(1.4, 3, "an ideal string", fontsize=10, color=GRAY)
    right.set_xlabel("partial number")
    right.set_ylabel("sharp of a true harmonic (cents)")
    right.set_xticks([1, 4, 8, 12, 16])
    right.set_title("A real piano string's partials are stretched",
                    fontsize=12, fontweight="bold")

    fig.tight_layout()
    save(fig, "ch05-formants-and-inharmonicity")


def main():
    print("Chapter 5 figures:")
    building_a_sawtooth()
    waveform_and_spectrum_grid()
    phase_does_not_matter()
    adsr_envelope()
    spectrogram_example()
    formants_and_inharmonicity()


if __name__ == "__main__":
    main()
