---
name: housekeeping-queue
description: The accumulated non-P8 housekeeping/retrofit debts, planned as a path and worked before P9. Check off as done.
sources: [chat]
---

> **⌖ RETIRED r1550.** This was the housekeeping queue opened r1284 — the dangling debts from the P8 comb, *"planned so none is left loose."* **Complete: 13 of 13 checked, none open.** Its Task 1 is why `depmatrix.py` emits the styled HTML in one step — the fix this session used at r1473 to restore the empty matrix.
> Kept as record; **do not work from it.**


# HOUSEKEEPING QUEUE — worked before P9 (opened r1284, Daryl-directed)

The list of dangling things accumulated through the P8 comb, planned so none is left loose. Work top to bottom, then P9.

## TASK 1 — Dependency matrix: make it run smoothly, then refresh (corpus-wide; stale since r976)
- [x] **1a. Make the regen one-step.** Extend `scripts/depmatrix.py` to emit the *styled* HTML table (per-cell
  colour by value), not just the number array — so a refresh is one command → paste, and the HTML never drifts
  from the tab again. ("Running smoothly," Daryl.)
- [x] **1b. Refresh the tab.** Paste the 17 regenerated LaTeX rows into P7 `tab:dependency-matrix` (§996–1013).
- [x] **1c. Refresh the HTML.** Write the regenerated styled table into `BOOK_INTRO_cosmiCave/assets/dependency_matrix.html`.
- [x] **1d. Reconcile the caption + figure.** P7 caption (§1016) specific counts and `fig:dependency-structure`
  (§983) feeds/edges brought current if stale.
- [x] **1e. Verify.** P7 compiles 0/0; HTML renders; script re-run is idempotent.

## TASK 2 — Unification-placement recap retrofit for P1–P6 (P7 is the synthesis; P8 done; P9+ as combed)
For each paper: identify its contribution to the unification, confirm P7's synthesis gives it its place, and add
its **context-relevant recap** (re-presents the one-substrate-read-many-ways from that paper's vantage, at the
place its result enters). Provisional vantages:
- [x] **P1** (BH_causality) — the metric-singularity result: the structural-test anchor the unification's correspondence rests on.
- [x] **P2** (circle) — Schwarzschild as one cycloid arc of the substrate: the GR face in its simplest instance.
- [x] **P3** (slicing) — the slicing curve / gnomonic / $A_2$ / lap: the GR-generation gauge object, the SM-flavour doorway, the cosmogenesis seed (the hub — touches several faces).
- [x] **P4** (modern parallax) — the empirically forced foliation: the empirical grounding of the whole.
- [x] **P5** (groupoid) — the deck group / $\mathrm{Aut}(A_2)=D_6$: the discrete-symmetry structure the vantage-groupoid and SM flavour rest on.
- [x] **P6** (shadow) — the theory-choice discipline: the method holding the unification at coherence-not-correspondence.

## TASK 3 — Close-out
- [x] **3a.** Bundle the pending arsenal refinement (unification-placement recap upgrade) + minor rev-label tidy.
- [x] **3b.** Cut the rev for the whole housekeeping batch; present.

## NOT on this list (correctly parked, not housekeeping)
- The **matter/baryon structural-inventory** mapping (the $2/\sqrt3$ roots/rulings/foci/sky-angles) — genuine
  forward physics, logged in the open-problems ledger, worked when the matter/baryon sector is.
- **P9 §275** "wall / deepest open problem" reframe — P9 comb work, flagged in the ledger for when we hit P9.
