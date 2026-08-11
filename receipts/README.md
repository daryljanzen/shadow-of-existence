# receipts/ — the corpus reproducibility layer
Every verifiable computational claim in the corpus, traced + run + classified. Built by the Avenue 11 sweep
(`../AVENUE_11_SWEEP_PLAN.md`). **`INDEX.md` is the source of truth.** One dir per paper (P01…P14, then P15/16),
plus `shared/` (multi-paper receipts) and `opens/` (receipts-in-waiting for open-problems computations).
Each receipt carries a standard header (status, run cmd, what it computes, honest bound, origin path).
Run everything: `python3 run_all.py`.  Status legend: ✔✔ verified · ◐ partial · ✗ broken · ? unclear · ∅ missing.

## ⌗ DEPENDENCIES (recorded r2376, c54)
The receipt set needs **`numpy`, `scipy`, `sympy`, `camb`** (26 receipts import `sympy`, one imports `camb`).
Missing deps present as `ModuleNotFoundError`, which is **not** a broken receipt — all 75 receipts registered
at r2376 run clean once these are installed. Install: `pip install numpy scipy sympy camb`.

## ⌗ THE ORIGIN DRIFT GUARD (added r2376, c54)
`../corpus/check_receipts.py` now compares every `receipts/` copy carrying an `ORIGIN:` line against that
origin's **code** (docstrings may differ; executable content may not) and reports divergence. It exists because
a sweep updated an origin and left its **cited** copy stale — silently, and the gate could not see it.
**It currently reports 8 pre-existing divergences**, and in the pairs sampled the `receipts/` copy is the
*developed* one, so those `ORIGIN:` lines name stale ancestors rather than sources of truth. **Each needs
per-pair adjudication** — which side is authoritative — and none should be swept.
