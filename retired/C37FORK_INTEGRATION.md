> **⌖ RETIRED r1550.** This was integration instructions for the c37 fork (r914) — an era procedure for a multi-node arrangement the Arthur seat superseded.
> Kept as record; **do not work from it.**


# c37fork — integration instructions for c33

*A cowork session (spun up on the **r913** bundle) ran a diagnostic of the Knows-Itself pass and a small
corrective pass. **You (c33) are ahead of r913 — at P14 — so DO NOT overwrite your files with the copies in
this fork.** Apply the two surgical edits below by find→replace against your current tree, then bundle at
your discretion. The corpus `.tex` files were **not touched** — the sweeps found nothing to fix.*

## What was checked, and the headline
The diagnostic (`C33_KNOWS_ITSELF_DIAGNOSTIC.md`, included) reconstructs the whole pass spin-up→r914 and
certifies every card to hard yes/no. **Good news:** P4/P3/P5/P6/P7 all got proper post-fix in-order reads
(r907–r911); the "six-card gap" was an illusion of incomplete transcript. The real residual was three old
pre-fix cards (§1b, P1, P2) + one stale heading. **The corrective pass ran the three sweeps — all clean
(restraint, no corpus edits) — and fixed the heading.**

## EDIT 1 — `THE_EVOLUTION_MAP.md` (R2: stale P2 heading)
The P2 in-order entry still said "no §-card yet," though §1k was pinned r906.

**Find:**
```
### P2 — the Schwarzschild circle *(`janzen_circle_v3`)*  →  *(no §-card yet; Pass-1 cherry-picks skipped it)*
```
**Replace with:**
```
### P2 — the Schwarzschild circle *(`janzen_circle_v3`)*  →  index card **§1k** `[†ONT-RING]` *(pinned r906, at Pass-2 in-order; the Pass-1 cherry-picks had skipped P2)*
```

## EDIT 2 — `BIBKEY_ALIAS_MAP.md` (bonus: stale title-drift status)
The "known title drift" section still said P6's sweep was "owed," but r908 completed the standardisation.

**Find** the block beginning `## Known title drift (a separate defect …` through the line
`**Whenever a paper's title is upgraded, sweep every bibitem in the corpus for the old string.**`
**Replace with** the updated block in this fork's `BIBKEY_ALIAS_MAP.md` (it records the r908 resolution:
P6/P7 titles repaired, 40 bibitems standardised via `CANONICAL_TITLES.txt`, verified zero-mismatch, and the
two self-introduced r905 titles fixed). *(If your r914+ tree already updated this section, keep yours.)*

## The sweep results, for your record (so you can trust the three old cards)
- **§1b (cosmology):** `ρ_r/ρ_m≈2`, `T_onset≈1.6 eV`, `z_seam≈6850`, `sinh^{2/3}` rate, finite-curvature
  seam — all consistent across P15/P16/P7 + working docs; `[†ONT-COSMO]` stamps in place. No drift.
- **P1 (§1c):** metric-singularity register consistent; "metrically identical" retired-as-false everywhere;
  the `removable coordinate singularity` hit in `janzen_circle §396` is the fairly-stated *standard reading*
  (§4.1), not a drift; p0's `JanzenCausality` citations grounded at point of use. No drift.
- **P2 (§1k):** cycloid `r(z)=M(1+cos z)` consistent (P2/P3/P5); `JanzenCircle` cited canonically by 8
  papers, p0 grounded. No drift.

## What's still open for the pass (unchanged by this fork)
- **P12 and p0** are pre-fix but *queued* — they pick up step-5 + alias-resolution automatically when Pass 2
  reaches them (P12 in arc order; p0 as the p17 re-read). No action needed now.
- **P11, P13, P14** need cards + stamps; **P16** needs its own forcing card (COSMO consumer only). Then Pass 3.
- Since you're already at P14, most of this may be done on your side — reconcile against your current state.

## Files in this fork
- `C37FORK_INTEGRATION.md` — this file.
- `C33_KNOWS_ITSELF_DIAGNOSTIC.md` — the full diagnostic (status table + residual + executed pass).
- `THE_EVOLUTION_MAP.md`, `BIBKEY_ALIAS_MAP.md` — the two edited files **as they stand against r913**, for
  diff reference only. Apply EDIT 1 / EDIT 2 to *your* copies; do not overwrite.
