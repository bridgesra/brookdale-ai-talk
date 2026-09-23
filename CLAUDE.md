# Project: the Brookdale AI talk

This repo builds a talk **Robert "Bobby" Bridges** is giving at **Brookdale**, an
assisted-living facility in south Kansas City where his mother Mary lives. Audience:
elderly residents, mixed AI familiarity (nationally only ~10% of adults 65+ had tried
ChatGPT in 2025). Session is **60 min = ~30 min talk + ~30 min discussion**.

Tone/design rules for this audience: large high-contrast type, plain language, concrete
analogies, no jargon without a plain-English gloss, reputable sources cited in footnotes.
Verify any statistic or headline before putting it on a slide (see `docs/research-notes.md`
for sourced facts). Locale details are real and correct: Kansas City / Leawood KS
(119th & Lamar), Chiefs — keep them.

## Deliverables & how to work with them

- **`talkplan.md`** — Bobby's source outline (titles, content, dialogue). Source of truth
  for narrative; refine, don't discard.
- **`slides/`** — the deck: a **single self-contained `index.html`** (no framework
  dependency) using the "SafeCare" theme — navy/white `.slide` sections, Newsreader +
  IBM Plex fonts, yellow accent. Its look is modeled on `2026-09-04-safecare-kickoff.html`
  (kept at repo root as the theme reference).
  - **Contrast rule (hard):** never yellow or light-grey text on a white/light background.
    Yellow appears only on navy (cover, callouts, badges, thank-you). Secondary text on
    light slides is `--navy-soft`, never `--ink-soft-dark` (dark-slide only).
  - `slides/fonts/` + `slides/fonts.css` — vendored woff2 (latin) so it works **offline**.
  - `slides/assets/` — images + charts. Uses METR's **official** figure
    `metr-actual-plot.png` (not the recreation).
  - Present: open `index.html`, `F` fullscreen, ←/→ (or space) to navigate,
    **`S`** opens a speaker-notes presenter window (current note + next preview + timer;
    each slide's dialogue lives in a hidden `<div class="notes">`). Nav/notes JS is inline
    at the bottom of the file; the AI Sweden logo is injected via JS (`LOGO` const).
  - Optional live-demo slide is badged; skip it if short on time.
  - Verify rendering with Playwright (Chromium + `sudo playwright install-deps` needed
    once); load `file://…/slides/index.html`, advance with `keyboard.press('ArrowRight')`,
    read position via `window.__deck.current`.
- **`charts/`** — Python (managed with **`uv`**, no system pip; use the 3.12 venv, the
  system 3.14 lacks stdlib modules) that generates figures into `charts/out/`, copied to
  `slides/assets/`:
  - `line_fit.py` → `line-fit.gif` (gradient descent fitting a line to Ames housing data).
  - `house_scatter.py` → `house-scatter.png` (same data, points only, for the
    "Predicting house prices" slide). Imports `load_data` from `line_fit`.
  - `metr_plot.py` → `metr-plot.png` — a recreation kept only as provenance; the deck now
    shows METR's official plot instead.
  - Run: `charts/.venv/bin/python charts/line_fit.py` (deps: matplotlib, numpy, pyyaml,
    pillow). Re-copy outputs to `slides/assets/` after editing.
- **`docs/research-notes.md`** — every sourced fact/stat/headline used, with citations.

# Project standards

- Write clean, declarative, testable functions.
- Enforce explicit, strict typing; avoid using `any`.
- Never hardcode credentials, tokens, or environment keys.
- Prefer small, focused changes over large refactors unless asked.
- Do not read or modify files listed in `.claudeignore` unless the user explicitly asks.
- After files are moved, renamed, added, or deleted, use the folder-explore skill to refresh `docs/repo-map.md`.
