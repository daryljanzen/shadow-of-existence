# r7163+70.1 — how many ways does a receipt reach a corpus file's bytes, and which can `run_touched_readers` see?

*Pre-registered by node 70 against `origin/main` `e38af0bc`, before any census, seed or patch is run.
Order: `FOR_70.md` r7163 ⚑ ⓵–⓷. Nothing below has been measured yet. Only the receipt sources are fixed
inputs, plus `receipts/READ_INDEX.json` (traced at `404bc95b`, 2026-09-28, 871 receipts).*

## Ground truth and the census (⓵)

- **Ground truth is the trace, not a source scan.** A receipt *reads* a corpus file if its `READ_INDEX`
  entry records that file in `r` (opened or imported), or a `d`/`g` entry covering it. This is the only
  record of what a receipt *opened*, not what it *says*. A source scan is the thing under test.
- **Scope for the census:** corpus files the touched-readers gate keys on, i.e. `corpus/*.tex|tsv|txt`.
  - Traced receipts whose current blob still matches the traced `sha` give clean ground truth.
  - Edited and untraced receipts are reported separately, from source only.
- **Convention of a (receipt, corpus file) read pair**, first match wins:
  1. `NAME`: the file's basename appears literally in the receipt source (what the gate tests today).
  2. `RB-IMPORT`: the 66-applied `_RB_IMPORT` regex matches.
  3. `RB-PATHLOAD`: `reach_baseline.py` is loaded by path (importlib / exec).
  4. `HELPER`: the trace shows an imported `.py` outside the receipt's own directory whose source names
     the file or globs `corpus/`.
  5. `SIBLING`: the same, through a module in the receipt's own directory (another receipt or a local helper).
  6. `STEM`: the basename without `.tex` appears in the source, and the path is built from it.
  7. `GLOB` / `WALK`: the source globs, lists or walks `corpus/`.
  8. `TABLE`: the name comes from a data file or mapping (a tsv, json or digest table) read at run time.
  9. `UNEXPLAINED`: none of the above. Every one of these is read by hand and named.
- Static-only conventions, invisible to the trace (subprocess, `git show`), are counted from source.

## Predictions

| id | prediction |
|---|---|
| C1 | Traced receipts with a clean `sha` whose trace reads at least one corpus `.tex`: **300–500**. |
| C2 | Of those (receipt, file) pairs, **≥ 80 %** are `NAME`. |
| C3 | Receipts with ≥ 1 non-`NAME`, non-`RB-IMPORT` read pair (blind to the current gate): **20–60**. |
| C4 | At least **four** distinct non-literal conventions occur with nonzero count. The largest is `HELPER` (a shared module other than `reach_baseline`). |
| C5 | `UNEXPLAINED` is **≤ 5** receipts after hand reading. |

## Seeds (⓶)

- **Apparatus:** extend `r7161_70_lifecycle_seed/lifecycle_seed.py`. One seed per non-literal convention
  found in ⓵, each pinning the same `CR_cosmology.tex` sentence and broken by the same edit.
- **Run on** `run_touched_readers` as it stands on `main` (66's patch included), and on `receipt_scope --scope suite`.
- **Controls:** a `NAME` seed (must go IN) and an `RB-IMPORT` seed (must go IN after 66's patch).

| id | prediction |
|---|---|
| K1 | Every non-literal seed is **out** of `run_touched_readers`, except a `STEM` seed whose source happens to contain the full basename elsewhere. I expect **≥ 4 misses**. |
| K2 | For new (untraced) seeds, `receipt_scope --scope suite` misses the same ones. Its fallback for an untraced receipt is names and imports in source, and the changed file is the `.tex`, not the helper. |
| K3 | Both controls go IN. If the `RB-IMPORT` control is out, 66's patch is not doing what my worktree proof said, and that is reported first. |

## The predicate (⓷), predicted before measuring

- **No static predicate is complete.** A path can be computed from data (`TABLE`), and a source scan cannot
  follow data.
- **Proposed predicate:** the trace when present, a conservative static widening when not.
  1. A receipt is a reader of changed file F if its `READ_INDEX` trace records F (`r`/`d`) or a glob matching F.
  2. If its blob differs from the traced `sha`, or it is untraced, it is also a reader if its source names F, or
     imports (transitively, within the repo) a module that names F or globs `corpus/`, or itself globs,
     walks or path-builds under `corpus/`. Any of these counts as reading **every** corpus file.
  3. The literal and number intersections after it stay unchanged.

| id | prediction |
|---|---|
| Q1 | The proposed predicate puts **every** seed IN, controls included. |
| Q2 | On the current tree, the set the gate string-scans grows by **≤ 150** receipts over today's name test, for a `.tex` edit. The receipts **run** grow far less, because the literal intersection still applies. I predict **≤ 5 more** run on a replay of `fbb0f749..e38af0bc`'s corpus edits. |
| Q3 | "Run the receipt and watch what it opens" is already built (`sweep_runner_reads.py`). The honest residue is the window between a receipt landing and the next trace. I expect to recommend tracing **the new and edited receipts of a push** at gate time over a bigger static predicate, and to state its cost in seconds. |

*Misses will be reported as misses.*
