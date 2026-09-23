# Brookdale AI Talk

A ~60-minute talk — **~45m of presentation + discussion** — introducing
artificial intelligence to the residents of **Brookdale** assisted living (south Kansas City).
By Robert "Bobby" Bridges (AI Sweden). Audience: older adults with mixed AI familiarity, so the
deck favors large type, high contrast, plain language, concrete analogies, and cited sources.

The deliverable is a **self-contained HTML slide deck** (`slides/index.html`) plus the Python
that generates its charts. No build step, no server, no internet required to present.

---

## Run the talk

1. Open **`slides/index.html`** in any modern web browser (double-click it, or drag it into a
   browser window).
2. Press **`F`** for fullscreen.
3. Navigate with **← / →** (or space, Page Up/Down; `Home`/`End` jump to first/last).
4. Press **`S`** to open the **speaker-notes window** — a separate window showing the current
   slide's script, a preview of the next note, and a running timer. Put it on your laptop while
   the deck is fullscreen on the projector.

It works fully **offline** — fonts and images are bundled in the repo.

> Tip: the "Three things to try" slide has copy-paste demo prompts (one click selects a whole
> box). It's marked *optional* — skip it straight to the questions if you're short on time.

---

## What's in each folder

| Path | What it is |
|------|------------|
| **`slides/`** | The deck. `index.html` is the whole presentation (inline CSS + navigation + speaker-notes JS). `fonts.css` + `fonts/` are the bundled web fonts (offline). `assets/` holds every image and chart shown on the slides. |
| **`charts/`** | Python that generates the deck's figures (see below). `line_fit.py`, `house_scatter.py`, `metr_plot.py`; outputs land in `charts/out/` and are copied into `slides/assets/`. |
| **`docs/`** | `research-notes.md` — every fact, statistic, and headline used, with sources (read this before asserting a claim on stage). `repo-map.md` — a one-line index of every file. |
| **`aise-logos/`** | AI Sweden logo source files (the deck inlines the logo, so these are just the originals). |
| **`backups/`** | Timestamped snapshots for quick revert (e.g. an earlier `index.html` / chart). Copy a file back to restore it. |
| **`talkplan.md`** | Bobby's original outline — slide titles, content, and intended dialogue. The narrative source of truth. |
| **`2026-09-04-safecare-kickoff.html`** | Reference deck whose visual style this talk copies (navy/white slides, Newsreader + IBM Plex fonts, yellow accent). |
| **`CLAUDE.md`** | Project brief + working conventions (kept for future editing sessions). |
| **`notes.md`** | Dev-container tooling notes (unrelated to talk content). |

---

## Regenerate the charts

The charts are pre-rendered and already in `slides/assets/`, so you only need this if you edit
the data or plotting code. Python is managed with [`uv`](https://github.com/astral-sh/uv):

```bash
# one-time: create the environment
cd charts
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python matplotlib numpy pyyaml pillow

# regenerate figures
.venv/bin/python line_fit.py       # -> out/line-fit.gif  (regression animation)
.venv/bin/python house_scatter.py  # -> out/house-scatter.png (data-only scatter)

# then copy the outputs the deck uses into slides/assets/
cp out/line-fit.gif out/house-scatter.png ../slides/assets/
```

- `line_fit.py` fits a line to real Ames, Iowa home-sale data by gradient descent and animates
  it "walking" to the best fit.
- `house_scatter.py` draws the same data as points only (the setup slide).
- `metr_plot.py` recreates the METR capability trend from their published data — kept for
  provenance; the deck shows METR's official figure (`metr-actual-plot.png`) instead.

Data sources and the reasoning behind each number are documented in
[`docs/research-notes.md`](docs/research-notes.md).

---

## Editing the deck

Everything is in `slides/index.html`:

- Each slide is a `<section class="slide light">` (white) or `class="slide dark"` (navy).
- Speaker dialogue lives in a hidden `<div class="notes">` at the end of each slide.
- Styling uses CSS variables at the top of the file. **House rule:** never put yellow or
  light-grey text on a light background — yellow appears only on navy (cover, callouts, badges,
  closing).

---

## Credits

Content by Robert Bridges; slides built and polished interactively with AI. Chart data:
[Ames Housing (De Cock 2011)](https://jse.amstat.org/v19n3/decock), [METR](https://metr.org),
and the sources listed in `docs/research-notes.md`.
</content>
