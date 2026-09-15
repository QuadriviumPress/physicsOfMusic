"""Shared matplotlib styling for figures in *Physics of Music*.

All generated figures are written as SVG into ``images/`` and committed, because
the MyST build on GitHub Pages runs ``myst build --html`` only -- there is no
Python kernel at build time. Regenerate with::

    python3 scripts/figures/ch03_figures.py
    python3 scripts/figures/ch05_figures.py

The palette matches the hand-authored SVG schematics in ``images/`` and the
audio companion figures in ``scripts/audio/``.
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

IMAGES = Path(__file__).resolve().parents[2] / "images"

# Palette shared with the hand-drawn SVG schematics.
BLUE = "#1769aa"
RED = "#b33a3a"
GREEN = "#2e7d5b"
PURPLE = "#6a4c93"
ORANGE = "#d97706"
GRAY = "#555555"
LIGHT = "#c9d6e0"

CYCLE = [BLUE, RED, GREEN, PURPLE, ORANGE]

RC = {
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "font.size": 11,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.9,
    "axes.grid": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "legend.frameon": False,
    "legend.fontsize": 10,
    "lines.linewidth": 1.8,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "path",
    # Stable element ids make regenerated SVGs byte-for-byte comparable in CI.
    "svg.hashsalt": "physics-of-music",
    "path.simplify": True,
    "path.simplify_threshold": 1.0,
}


def use_style():
    plt.rcParams.update(RC)


def save(fig, name):
    """Save *fig* as ``images/<name>.svg`` and report the byte size."""
    IMAGES.mkdir(exist_ok=True)
    path = IMAGES / f"{name}.svg"
    fig.savefig(
        path,
        format="svg",
        bbox_inches="tight",
        pad_inches=0.12,
        metadata={"Date": "2026-01-01"},
    )
    plt.close(fig)
    print(f"  wrote {path.relative_to(IMAGES.parent)}  ({path.stat().st_size // 1024} KB)")
    return path


def waveform(ax, t, y, color=BLUE, label=None, ms_axis=True):
    """Plot one cycle-scale slice of a signal as a labelled waveform."""
    ax.plot(t * (1000 if ms_axis else 1), y, color=color, label=label)
    ax.axhline(0.0, color=GRAY, lw=0.6, zorder=0)
    ax.set_xlabel("time (ms)" if ms_axis else "time (s)")
    ax.set_ylabel("pressure (arb.)")
    ax.set_yticks([])
    ax.set_xlim((t[0] * (1000 if ms_axis else 1)), (t[-1] * (1000 if ms_axis else 1)))
    return ax


def spectrum(ax, freqs, amps, color=BLUE, fundamental=None, db=False, label=None):
    """Plot a harmonic spectrum as stems.

    A line spectrum, not a filled curve: the point of nearly every spectrum in
    this book is *which* partials are present, and a filled curve invites the
    reader to see energy between them where there is none.
    """
    values = 20.0 * np.log10(np.maximum(amps, 1e-4)) if db else amps
    floor = values.min() if db else 0.0
    ax.vlines(freqs, floor, values, color=color, lw=2.0, label=label)
    ax.plot(freqs, values, "o", color=color, ms=4)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("level (dB)" if db else "amplitude (arb.)")
    if fundamental:
        # Harmonic numbers are what the reader is actually counting.
        ticks = [n * fundamental for n in range(1, int(freqs.max() / fundamental) + 1)]
        ax.set_xticks(ticks)
        ax.set_xticklabels([str(n) if n % 2 or n <= 2 else "" for n in range(1, len(ticks) + 1)])
        ax.set_xlabel(f"harmonic number  (fundamental {fundamental:g} Hz)")
    ax.set_xlim(0, freqs.max() * 1.05)
    return ax


def wave_and_spectrum(name, t, y, freqs, amps, title=None, color=BLUE, cycles_label=None):
    """The standard two-panel companion figure for an ``{audio}`` example.

    Left: a few cycles of the waveform. Right: the line spectrum. This pair is
    what a reader gets in the PDF in place of the player, so it has to carry the
    whole point of the example on its own.
    """
    use_style()
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.0))
    waveform(left, t, y, color=color)
    if cycles_label:
        left.set_title(cycles_label, fontsize=11)
    spectrum(right, freqs, amps, color=color)
    if title:
        fig.suptitle(title, fontsize=12, fontweight="bold")
        fig.subplots_adjust(top=0.84)
    fig.tight_layout()
    return save(fig, name)


def cents_ruler(ax, entries, reference_label="equal temperament"):
    """Compare tunings on a cents axis: ``entries`` is ``(label, cents, color)``.

    Cents, not hertz, because the comparison the reader needs is of *intervals*,
    and a cent is the same size wherever it lands on the keyboard.
    """
    for index, (label, cents, color) in enumerate(entries):
        ax.plot(cents, [index] * len(cents), "|", color=color, ms=18, mew=2.0)
        ax.text(-12, index, label, ha="right", va="center", fontsize=10)
    ax.axvline(0.0, color=GRAY, lw=0.8, ls=":")
    ax.set_yticks([])
    ax.set_ylim(-0.6, len(entries) - 0.4)
    ax.set_xlabel(f"cents from {reference_label}")
    for side in ("left", "right", "top"):
        ax.spines[side].set_visible(False)
    return ax
