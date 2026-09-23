"""Recreate METR's time-horizon figure from their published data.

Source: METR, "Measuring AI Ability to Complete Long Tasks" (2025-03-19)
https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Data:   https://metr.org/assets/benchmark_results_1_1.yaml

We plot each model's p50 time horizon (the length of software task it can
complete with 50% success) against its release date, on a log scale, coloured
green -> yellow -> red as the horizon grows.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import yaml
from matplotlib.colors import LinearSegmentedColormap, LogNorm

HERE = Path(__file__).parent
DATA_FILE = HERE / "data" / "metr_benchmark_results_1_1.yaml"
OUT_PNG = HERE / "out" / "metr-plot.png"

# A few frontier models we label by name (others are drawn but unlabelled).
# Label a well-separated subset so text does not overlap. Each entry maps the
# data key to (display name, (x_offset_pts, y_offset_pts)).
LABELS = {
    "gpt2": ("GPT-2", (8, -2)),
    "gpt_3_5_turbo_instruct": ("GPT-3.5", (8, 4)),
    "gpt_4": ("GPT-4", (8, -14)),
    "claude_3_5_sonnet_20241022": ("Claude 3.5 Sonnet", (-6, -16)),
    "o1": ("o1", (10, 6)),
    "claude_3_7_sonnet": ("Claude 3.7 Sonnet", (8, -14)),
    "claude_4_1_opus": ("Claude 4.1 Opus", (8, 6)),
}


def load_points():
    doc = yaml.safe_load(DATA_FILE.read_text())
    pts = []
    for key, rec in doc["results"].items():
        try:
            horizon = rec["metrics"]["p50_horizon_length"]["estimate"]  # minutes
            rel = rec["release_date"]
        except (KeyError, TypeError):
            continue
        if horizon is None or rel is None:
            continue
        d = rel if isinstance(rel, date) else date.fromisoformat(str(rel))
        base = key.replace("_inspect", "")
        pts.append((d, float(horizon), base))
    pts.sort(key=lambda p: p[0])
    return pts


def fmt_minutes(m: float) -> str:
    if m < 1:
        return f"{m * 60:.0f} sec"
    if m < 60:
        return f"{m:.0f} min"
    return f"{m / 60:.1f} hr"


def main() -> None:
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    pts = load_points()
    dates = [p[0] for p in pts]
    horizons = np.array([p[1] for p in pts])

    cmap = LinearSegmentedColormap.from_list(
        "gyr", ["#2ca02c", "#e0d000", "#d62728"]
    )
    norm = LogNorm(vmin=0.3, vmax=max(horizons.max(), 120))

    fig, ax = plt.subplots(figsize=(10, 6.2), dpi=130)

    # trend line (exponential): fit log2(horizon) vs time in years
    t0 = min(dates)
    years = np.array([(d - t0).days / 365.25 for d in dates])
    coef = np.polyfit(years, np.log2(horizons), 1)
    doubling_months = 12.0 / coef[0]
    yy = np.linspace(years.min(), years.max(), 100)
    trend = 2 ** (coef[1] + coef[0] * yy)
    trend_dates = [t0.toordinal() + int(y * 365.25) for y in yy]
    ax.plot([date.fromordinal(o) for o in trend_dates], trend,
            color="#888888", ls="--", lw=2, zorder=1,
            label=f"doubling ≈ {doubling_months:.0f} months")

    ax.scatter(dates, horizons, c=horizons, cmap=cmap, norm=norm,
               s=90, edgecolor="#333333", linewidth=0.6, zorder=3)

    for d, h, base in pts:
        if base in LABELS:
            name, off = LABELS[base]
            ax.annotate(name, (d, h), textcoords="offset points",
                        xytext=off, fontsize=10, fontweight="bold")

    ax.set_yscale("log")
    ax.set_yticks([1 / 60 * 60, 1, 4, 15, 60, 240])
    ax.set_yticks([0.5, 1, 2, 4, 8, 15, 30, 60, 120, 240])
    ax.set_yticklabels(["30s", "1m", "2m", "4m", "8m", "15m", "30m",
                        "1h", "2h", "4h"])
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_ylabel("Task length a model finishes\nwith 50% success", fontsize=12)
    ax.set_title(
        "Length of software tasks that different AI models\n"
        "can complete 50% of the time",
        fontsize=15, fontweight="bold")
    ax.grid(True, which="both", alpha=0.2)
    ax.legend(loc="upper left", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG)
    print(f"doubling time ~= {doubling_months:.1f} months")
    print(f"points plotted: {len(pts)}")
    print(f"wrote {OUT_PNG}")


if __name__ == "__main__":
    main()
