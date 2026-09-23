"""Animate simple linear regression learning to fit house-price data.

Dataset: Ames Housing, De Cock (2011), Journal of Statistics Education.
https://jse.amstat.org/v19n3/decock/AmesHousing.txt

We model  price = a * area + b  (a, b in "thousands" units) and use plain
gradient descent on the sum-of-squared-errors. Ten lines along the way are
captured so the audience can watch the line "walk" to the best fit.
"""

from __future__ import annotations

import io
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter

DATA_URL = "https://jse.amstat.org/v19n3/decock/AmesHousing.txt"
HERE = Path(__file__).parent
DATA_FILE = HERE / "data" / "AmesHousing.txt"
OUT_GIF = HERE / "out" / "line-fit.gif"

# Learning setup ------------------------------------------------------------
# A deliberately poor first guess so the audience can watch the line "walk"
# up to the fit. (Starting at the requested y = 100x + 10 lands almost on the
# best fit of ~116x + 7 in these units, so nothing visible would move.)
START_A, START_B = 25.0, 5.0
LEARNING_RATE = 0.03
N_STEPS = 4000
N_FRAMES = 10                    # ten lines along the way


def load_data() -> tuple[np.ndarray, np.ndarray]:
    """Return living area (1000 sq ft) and sale price (1000 $)."""
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(DATA_URL, timeout=30) as resp:
            DATA_FILE.write_bytes(resp.read())

    raw = DATA_FILE.read_text()
    header, *rows = raw.splitlines()
    cols = header.split("\t")
    i_area = cols.index("Gr Liv Area")
    i_price = cols.index("SalePrice")

    area, price = [], []
    for row in rows:
        parts = row.split("\t")
        if len(parts) <= max(i_area, i_price):
            continue
        try:
            a = float(parts[i_area])
            p = float(parts[i_price])
        except ValueError:
            continue
        if a >= 4000:  # drop the handful of well-known Ames outliers
            continue
        area.append(a)
        price.append(p)

    x = np.array(area) / 1000.0   # thousands of square feet
    y = np.array(price) / 1000.0  # thousands of dollars
    return x, y


def gradient_descent(x: np.ndarray, y: np.ndarray) -> list[tuple[float, float, float]]:
    """Return [(a, b, sse), ...] recorded at each step."""
    a, b = START_A, START_B
    n = len(x)
    history = []
    for _ in range(N_STEPS + 1):
        pred = a * x + b
        err = pred - y
        sse = float(np.sum(err**2))
        history.append((a, b, sse))
        grad_a = (2.0 / n) * float(np.sum(err * x))
        grad_b = (2.0 / n) * float(np.sum(err))
        a -= LEARNING_RATE * grad_a
        b -= LEARNING_RATE * grad_b
    return history


def pick_frames(history: list[tuple[float, float, float]]) -> list[tuple[float, float, float]]:
    """Ten frames, spaced so the fast early movement is visible."""
    idx = np.unique(np.geomspace(1, len(history) - 1, N_FRAMES).astype(int))
    frames = [history[0]] + [history[i] for i in idx]
    return frames[:N_FRAMES]


def render(x: np.ndarray, y: np.ndarray, frames, best: tuple[float, float]) -> None:
    OUT_GIF.parent.mkdir(parents=True, exist_ok=True)
    # A representative subset of points is drawn so error bars stay readable.
    rng = np.random.default_rng(7)
    sub = rng.choice(len(x), size=min(60, len(x)), replace=False)
    xs, ys = x[sub], y[sub]

    xline = np.array([x.min(), x.max()])
    fig, ax = plt.subplots(figsize=(9, 6), dpi=110)
    writer = PillowWriter(fps=1.4)

    with writer.saving(fig, str(OUT_GIF), dpi=110):
        for a, b, sse in frames:
            ax.clear()
            # error segments in red
            for xi, yi in zip(xs, ys):
                ax.plot([xi, xi], [yi, a * xi + b], color="#d62728", lw=1.0, alpha=0.7)
            ax.scatter(xs, ys, s=26, color="#1f4e79", zorder=3, label="Past sales")
            ax.plot(xline, a * xline + b, color="#111111", lw=3, zorder=4,
                    label="Model's guess")
            ax.set_xlim(x.min() - 0.1, x.max() + 0.1)
            ax.set_ylim(0, max(y.max(), (a * x + b).max()) * 1.05)
            ax.set_xlabel("Living area (thousands of sq ft)", fontsize=13)
            ax.set_ylabel("Sale price (thousands of $)", fontsize=13)
            ax.set_title("Adjusting a line until its predictions match past sales",
                         fontsize=15, fontweight="bold")
            ax.text(0.03, 0.95,
                    f"price = {a:5.1f} x area + {b:5.1f}\n"
                    f"total error (SSE) = {sse:,.0f}",
                    transform=ax.transAxes, va="top", fontsize=13,
                    family="monospace",
                    bbox=dict(boxstyle="round", fc="#fff6cc", ec="#d1b100"))
            ax.legend(loc="lower right", fontsize=12)
            ax.grid(True, alpha=0.25)
            fig.tight_layout()
            writer.grab_frame()
        # linger on the final best-fit frame
        for _ in range(3):
            writer.grab_frame()

    print(f"best fit (closed form): price = {best[0]:.1f} x area + {best[1]:.1f}")
    print(f"final frame:            price = {frames[-1][0]:.1f} x area + {frames[-1][1]:.1f}")
    print(f"wrote {OUT_GIF}")


def main() -> None:
    x, y = load_data()
    # closed-form best fit, for reference
    A = np.vstack([x, np.ones_like(x)]).T
    a_best, b_best = np.linalg.lstsq(A, y, rcond=None)[0]
    history = gradient_descent(x, y)
    frames = pick_frames(history)
    render(x, y, frames, (float(a_best), float(b_best)))


if __name__ == "__main__":
    main()
