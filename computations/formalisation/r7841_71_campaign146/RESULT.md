# `r7841+71.2` — RESULT: campaign 146 BUILT WHOLE (F1–F3) AND LANDED IN P14 AND P16. P15's `0.4835` row is not built: it is arithmetic only. The registered stop (F2) did not hold, and no Mathlib gap was found. ⌗ `94` Lean lines (band 70–200, estimate 120: **in band**), at p `0.75`

*The census and registration are in `PREDICTION.md`. The probe is the new standalone `probes/ColdReads.lean` (`cr_`,
94 lines). It imports only Mathlib, carries no copies and sets no option.*

## Verification

- `lake env lean probes/ColdReads.lean`: **0 errors, 0 warnings**.
- **Six axiom lines**, all `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.

## Rows

| Row | Lean | Mark |
|---|---|---|
| F1 (P14:745) | `cr_discriminant`: `−4(−1)³ − 27(r₀ − r₀³)² = (4 − 3r₀²)(3r₀² − 1)²`, by `ring`. `cr_crest`: at `r₀ = 1/√3` the squared factor vanishes, `4 − 3r₀² = 3`, and the discriminant is `0` | **BUILT** |
| F2 (P16 sec:peak) | `cr_throat`: at `2M = 2α/(3√3)`, `α/√3 = (3/2)·2M`. `cr_extremum`: the ratio `y = (2Mα²)^{1/3}/(2M)` has `y³ = 27/4` and `1.889 < y < 1.891`, so `y > 1` | **BUILT** |
| F3 (P16 sec:peak) | `cr_peak`: `M/((4/3)π((9/2)GMt²)) = 1/(6πGt²)` for every `M > 0`. `cr_planck`: `1/(6πG·ħG/c⁵) = (c⁵/ħG²)/(6π)` | **BUILT** |
| P15 sec:coherence | `1 − (0.4835/0.5)²`: arithmetic only, so it is **not built**, per 69's criterion. The census records why: `1 − x² = (1−x)(1+x)` on one printed number. `0.4835` itself is the receipt's integration | — |

## The landing

There are two plain paragraphs, each after its claim paragraph:
- **P14:745:** F1;
- **P16, after the sec:peak paragraph (P16:575–598):** F2 and F3.

The landings write `27/4` and `3/2` as `\tfrac` and refer to "the printed figure" instead of restating `1.89` and
`1.50`. That keeps the transposition gate clean.

Checks on the committed tree:
- **PDFs:** P14 and P16 build with 0 errors, citations, references and dead links.
- **Overfull boxes:** unchanged against a baseline build (P14 140, P16 54). One first-draft overfull line in P14's
  landing was reworded before the commit.
- **Served pages:** regenerated. They differ only by the two new paragraphs.
- **Gates:** `check_pages_current`, `check_pdf_current`, `check_marker_transposition`, `check_paper_pins_present`,
  `check_figures_pinned`, `check_unread_figure`, `check_depmatrix`, `check_open_item_coherence`,
  `check_open_references`, `check_prose_pins`, `check_source_hygiene`, `check_glyph_coverage` and
  `check_citations_resolve` all pass. The local gate is GREEN.
- **Formalisation join:** `check_formalisation_join` reads UNANSWERABLE until CI records the formalisation-mathlib run
  for the new `.lean` tree. This happened for campaign 145 too, as expected.

## Against the registration

- **All three rows were built and landed**, so the joint event (p 0.75) held.
- **The named stop did not hold.** F2 (p 0.85) reused campaign 145's cube bound.
- **Size: 94 lines**, in band and below the estimate.

**Mathlib gap: none.**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
