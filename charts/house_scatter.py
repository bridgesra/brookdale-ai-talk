"""Scatter of house price vs living area — data points ONLY.

Used on the "Predicting house prices" slide, before we introduce the fitted
line. Same Ames data and axes as line_fit.py so the two slides line up.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from line_fit import load_data

HERE = Path(__file__).parent
OUT_PNG = HERE / "out" / "house-scatter.png"

NAVY = "#121f2b"
POINT = "#1f4e79"


def main() -> None:
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    x, y = load_data()

    fig, ax = plt.subplots(figsize=(8.4, 6.0), dpi=130)
    ax.scatter(x, y, s=34, color=POINT, alpha=0.55, edgecolor="white", linewidth=0.4)
    ax.set_xlim(x.min() - 0.1, x.max() + 0.1)
    ax.set_ylim(0, y.max() * 1.05)
    ax.set_xlabel("Living area (thousands of sq ft)", fontsize=14, color=NAVY)
    ax.set_ylabel("Sale price (thousands of $)", fontsize=14, color=NAVY)
    ax.set_title("Past home sales", fontsize=16, fontweight="bold", color=NAVY)
    ax.tick_params(colors=NAVY)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(OUT_PNG, facecolor="white")
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
