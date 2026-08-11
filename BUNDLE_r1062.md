# Bundle r1062 — charge conjugation worked through the corpus (algebra → group → geometry), and the P7 synthesis figure landed

This bundle captures the corpus after the charge-conjugation-parity finding was worked in at every
level it touches, and the P7 flagship's grand synthesis figure (`fig:dS_SdS`) was brought current in
caption and body. All six edited papers compile clean (0 errors, 0 undefined refs), verified by a
full recompile at the close.

## The finding, worked in
Charge conjugation is present in the geometry **as a symmetry**, not an absence: the metric carries
charge only through `Q²`, so `Q↦−Q` is an even degeneracy. Mass is the **R-odd** datum, charge the
**R-even** datum, of the substrate's one discrete reflection (`R` = the mass-reflection `2M↦−2M` =
the `A₂` diagram automorphism = the outer `ℤ₂` of `Aut(A₂)=D₆` = `γ⁵`). The full antilinear `C` stays
field-level; and — settled by receipt — charge conjugation is **not** the outer `ℤ₂` (`R` moves the
horizon roots; `Q↦−Q` fixes them), but an **independent `ℤ₂`** the charged cut adjoins, `D₆→D₆×ℤ₂`.

## Edited (all recompile clean, latexmk/pdflatex, 0 undefined)
- **P13 boundary (15pp):** new `prop:conjugation-parity` (charged extension of the dS↔Schwarzschild
  eigenspace split, anchored to `R`); new `rem:C-not-R` (the outer `ℤ₂` is `R`, not `C`); §258
  "charge-conjugation blind" → "`C` present as a symmetry (even-face degeneracy)".
- **P5 groupoid (23pp):** `rem:P-dS-Schw` extended with the charged eigenspace split (charge `R`-even,
  joins de Sitter); underbrace slip `P-even/P-odd`→`R-even/R-odd` fixed (per the paper's own convention).
- **P3 slicing (33pp):** new `sec:charge` ("Adding charge: mass is `R`-odd, charge `R`-even") — the
  finding at the GEOMETRIC level (charge reading-swap-neutral, joins the invariant geometry; `Q↦−Q`
  leaves the slicing curve identical; honest scope: with `Q≠0` the `r=0` lap changes character, inner
  horizon, so the charged closed loop is a flagged extension). Two existing charge sentences pointed at
  it; missing `\bibitem{JanzenRange}` added.
- **P9 range (12pp):** `rem:charge` reframe — "charge-conjugation blind" → "carries charge conjugation
  as a *symmetry*", cross-ref `JanzenBoundary`.
- **p0 geometric_core (20pp):** l654 "substrate charge-conjugation-blind" → "carrying it as a symmetry,
  not a datum".
- **P7 CR_framework (41pp):** the six-panel synthesis figure `fig:dS_SdS` brought current — caption
  preamble (purple), panels (A) both-bundles/three-thirds, (C) rebuilt with the theorem's own
  continuations, (E) slicing-roots vs comoving-turnaround, (F) rebuilt unfurled cosmological bundle;
  body "three complementary readings" sentence updated. `singlelinecheck=false` added to `\captionsetup`
  (the lengthened caption overflowed the caption package's single-line measurement).

## Receipts (in storyboard_receipts/)
- `conjugation_parity.py` — 6 checks: mass odd / charge even parity; `Q↦−Q` metric invariance;
  `R=γ⁵` vs `P=γ¹γ²γ³` distinct (grades vs flips); `2M` odd under offset `r₀↦−r₀`; the corpus-`R`
  charged split; and CHECK 6 — charge conjugation is NOT the `D₆` outer `ℤ₂` (roots fixed vs moved).
- `charged_slicing_geometry.py` — the P3 geometric receipt (reading-swap eigenspaces of the RN-dS
  cut, `Q↦−Q` invisible on the slicing curve, the three-horizon RN-dS regime, honest `r=0` scope).

## Living planning doc
`SYNTHESIS_FIGURE_STORYBOARD.md` §7 carries the baked-edit ledger (P13-CP, P3-CP, P7-FIG) and §10 the
staged/now-baked caption drafts. The `τ̃↔τ̄̃` "geometric home for C" reach is retired (superseded by the
all-real metric-parity resolution).

## Excludes
LaTeX build artifacts (`.aux/.log/.fls/.fdb_latexmk/.out/.synctex.gz/.toc`), in-session pre-edit
backups (`corpus/*.pre_P13CP`), and `__pycache__/`. Compiled paper PDFs are included (current).
