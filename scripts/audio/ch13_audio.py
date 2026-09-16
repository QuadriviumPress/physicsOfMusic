"""Audio examples for Chapter 13, The Singing Voice."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audiolib as A  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "figures"))
import figstyle  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from ch13_figures import VOWELS, tract_filter  # noqa: E402


def sung(f0, formants, seconds=2.4, bandwidths=(80, 110, 160), vibrato=0.0,
         extra=None, n_max=60):
    """Source-filter synthesis: a glottal harmonic series through a fixed filter.

    The filter is applied to the *amplitudes of the harmonics*, which is the
    whole content of the source-filter model: the source supplies the harmonics,
    the tract decides how loud each one comes out.
    """
    t = A.time_axis(seconds)
    signal = np.zeros_like(t)
    if vibrato:
        # A real sung note is never perfectly steady, and a perfectly steady one
        # is instantly recognizable as synthetic.
        depth = vibrato * f0
        phase_mod = depth / (2 * np.pi * 5.5) * np.sin(2 * np.pi * 5.5 * t)
    for n in range(1, n_max + 1):
        frequency = n * f0
        if frequency > 12000:
            break
        gain = tract_filter(np.array([frequency]), formants, bandwidths)[0]
        if extra is not None:
            gain *= extra(frequency)
        amplitude = gain / n ** 1.2
        if vibrato:
            signal += amplitude * np.sin(2 * np.pi * frequency * t + n * 2 * np.pi * phase_mod)
        else:
            signal += amplitude * np.sin(2 * np.pi * frequency * t)
    return signal * A.envelope(t, attack=0.08, release=0.3)


def vowels():
    """Three vowels at one pitch: same source, different filter."""
    f0 = 130.0
    names = [("ch13-vowel-ee", "ee (heed)"), ("ch13-vowel-ah", "ah (hard)"),
             ("ch13-vowel-oo", "oo (who)")]
    for clip_name, vowel in names:
        A.write_clip(clip_name, A.match_level(sung(f0, VOWELS[vowel], vibrato=0.012)))

    figstyle.use_style()
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.9), sharey=True)
    freqs = np.linspace(20, 4000, 1400)
    for ax, (_, vowel), colour in zip(axes, names, (figstyle.BLUE, figstyle.RED, figstyle.GREEN)):
        formants = VOWELS[vowel]
        response = tract_filter(freqs, formants)
        ax.plot(freqs, 20 * np.log10(response / response.max()), color=colour, lw=2.2)
        for index, centre in enumerate(formants[:2]):
            ax.axvline(centre, color=figstyle.GRAY, lw=0.7, ls=":")
            ax.text(centre, 3, f"$F_{index+1}$", ha="center", fontsize=10, color=colour)
        ax.set_xlim(0, 4000)
        ax.set_ylim(-55, 10)
        ax.set_xlabel("frequency (Hz)")
        ax.set_title(vowel, fontsize=12, fontweight="bold", color=colour)
    axes[0].set_ylabel("level (dB)")
    fig.suptitle("Same vocal folds, same pitch, three tract shapes",
                 fontsize=12.5, fontweight="bold")
    fig.tight_layout()
    fig.subplots_adjust(top=0.78)
    figstyle.save(fig, "ch13-vowels")


def vowel_across_pitch():
    """The same vowel low and high, where the harmonics stop sampling the formants."""
    formants = VOWELS["ah (hard)"]
    A.write_clip("ch13-ah-low", A.match_level(sung(196.0, formants, vibrato=0.012)))
    A.write_clip("ch13-ah-high", A.match_level(sung(784.0, formants, vibrato=0.012)))


def singers_formant():
    """A voice with and without the singer's formant, against an orchestra."""
    formants = VOWELS["ah (hard)"]
    seconds = 3.2
    t = A.time_axis(seconds)

    def cluster(frequency):
        """The singer's formant: a strong extra resonance near 2.9 kHz."""
        return 1.0 + 5.0 / np.sqrt(1 + ((frequency - 2900) / 300) ** 2)

    plain = sung(220.0, formants, seconds=seconds, vibrato=0.012)
    trained = sung(220.0, formants, seconds=seconds, vibrato=0.012, extra=cluster)

    # A stand-in orchestra: dense low-biased noise, as in the figure.
    rng = np.random.default_rng(21)
    noise = rng.normal(0, 1, t.size)
    spectrum = np.fft.rfft(noise)
    freqs = np.fft.rfftfreq(t.size, 1 / A.RATE)
    spectrum *= 1.0 / (1 + (np.maximum(freqs, 1) / 320) ** 1.1)
    orchestra = np.fft.irfft(spectrum, n=t.size)
    orchestra = orchestra / np.max(np.abs(orchestra))

    for name, voice in (("ch13-voice-plain", plain), ("ch13-voice-trained", trained)):
        mixed = 0.55 * orchestra + 1.25 * A.match_level(voice) / 0.12
        A.write_clip(name, A.match_level(mixed))


def main():
    print("Chapter 13 audio:")
    vowels()
    vowel_across_pitch()
    singers_formant()


if __name__ == "__main__":
    main()
