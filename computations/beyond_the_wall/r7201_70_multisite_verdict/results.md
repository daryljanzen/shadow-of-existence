# r7201+70.1 — the measurement, against `PREDICTION.md` (the build follows in its own commit)

## E1/E2 — the MULTI-SITE verdict on the operator's own key set (`measure_keys.py`, `keys.tsv`)

- `mutate_assertions.py --quote` at `HEAD` reports **2,762 sites** and **2,570 (receipt, literal) keys**.  It takes 6 s.
- **1,454 keys (57%) target a PAPER.**  Taking the `.tex` from the operator's own read trace, they split as:
  - **1,047 SINGLE**;
  - **243 MULTI-SITE**;
  - **86 ABSENT**, which is not this class;
  - **78 UNRESOLVED**, where the trace names no readable `.tex`.
- **MULTI-SITE is 243, 16.7% of PAPER keys.**  Of those:
  - **121 are SECTION-UNIQUE**, which a section scope would make single-site;
  - **122 are SECTION-SHARED**, which need a neighbourhood.
- ⇒ *The verdict's backlog starts at 243, not r7183's 139.  The r7183 figure was my own counter on a different
  population.*

## E3/E4 — the `r7197` pin-like collections

- **v1, the pre-registered definition** (loop variable tested with `in`): **60 collections in 39 receipts, 354
  strings**.  Only 6 collections trace to a paper.  Of their 36 presence strings, **8 are MULTI-SITE (22%)**.
- ⛔ **v1 misses `S2`'s `ABSENT` list**, the one the order names.  That list is passed whole to
  `reach_baseline.survey()` and asserted on the counts, so no `in` ever touches a loop variable.  **The pre-registered
  recall half of E3 MISSED.**
- **v2** (iterated with any comparison, or passed to any call) finds S2: **197 collections in 122 receipts, 990
  strings.**  A seeded sample of 20 reads **7 PIN, 12 NOT, 1 UNCLEAR, about 35% precision**
  (`lists_v2_sample20_verdicts.md`).  That puts the class at roughly **70 collections and a few hundred strings**.

## E5 — the decision rule, applied as fixed

Both v1's floor (60 and 354) and v2's estimate clear the "20 collections and 100 strings" bound.  ⇒ **The class is
not small, so the extension is built.**  The sample also says how to build it: every PIN reaches one of the
operator's own site forms through a loop or index variable.  The operator resolves that variable back to the
module-level collection and keys each string.  `reach_baseline.survey()` calls are treated as a site form of their own.

## Scored

| | predicted | measured | |
|---|---|---|---|
| E1 keys | 2,250-2,450 | **2,570** | **MISSED** (high) |
| E1 PAPER share | 55-80% | 57% | held |
| E1 MULTI-SITE of PAPER | 15-30% | 16.7% | held |
| E2 SECTION-UNIQUE share | 35-60% | 49.8% | held |
| E3 collections / strings | 30-150 / 200-1,500 | v1 60 / 354; v2 197 / 990, about 35% precise | held on both |
| E3 S2 found | yes | **v1 no; v2 yes** | **v1 MISSED** |
| E4 MULTI-SITE of presence strings on a paper | 15-35% | 22% (v1, n = 36) | held, on a small n |
| E5 decision | rule fixed | build | applied |
| E6 discriminator | monotone live | the backlog is ratcheted at <= 243, interior to its range | holds |
