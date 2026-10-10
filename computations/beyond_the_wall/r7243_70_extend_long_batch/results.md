# r7243+70.1 — the EXTEND-LONG batch: results (node 70)

Pre-registered at `PREDICTION.md` (`9fdd1a15`) before any extension was computed.

**Files.**
- **Extensions:** computed at `fae76e75` (`extensions.json`).
- **Receipt green before any edit:** 146 of 146 (`pre_run_log.txt`).
- **Per-key ledger:** `ledger.json`. **Apply log:** `apply_log.txt`.

## Outcome: 167 of 295 extended in 127 receipts; 128 restored, each with its reason

| outcome | paper | source | total | predicted |
|---|---:|---:|---:|---|
| **EXTENDED (OK)** | 140 | 27 | **167** | 110–160 (point 135) |
| DIVERGENT | 33 | 62 | 95 | 70–90 (point 80) |
| RED-AFTER | 1 | 18 | 19 | 40–75 |
| NO-TOKEN | 8 | 0 | 8 | 4–15 |
| NOT-DISCRIMINATING, caught in the engine before any edit | 5 | 1 | 6 | 2–12 |

- **DIVERGENT is every multi-site key, 95 of 95.** At r7225 it was 20 of 24. At these lengths, a key with more than
  one site never shared an extension across them.
- **Paper keys went through at 75 %; source keys at 25 %.** Source keys are mostly multi-site: 62 of 108.
- **The paper half's single-site keys failed almost only on NO-TOKEN:** 8 of 154. Only one was RED-AFTER.
- **NOT-DISCRIMINATING never reached a receipt.** Acceptance (b) now runs inside the engine, which was r7225's P5
  lesson, so none of the six was edited and later reverted.

## Counts, against the statement made in advance

N = 167 went through. By prior verdict: 151 UNADJUDICATED, 11 DELIBERATE, 3 ENCODING-OK and 2 UNADJUDICATED-LIST.
**K = 2 converged:**
- **two accepted keys** in `L211/A1` extended to one literal, and became one row recording both;
- **one extension** in `L221/C1` landed on a key the baseline already held; that row now records the convergence.

| verdict | before | after | stated in advance | |
|---|---:|---:|---|---|
| UNADJUDICATED | 2,073 | **1,922** | − N_U = −151 | ✔ |
| DELIBERATE | 326 | **315** | −11 | ✔ |
| ENCODING-OK | 21 | **18** | −3 | ✔ |
| UNADJUDICATED-LIST | 60 | **58** | −2 | ✔ |
| EXTENDED | 107 | **272** | + N − K = +165 | ✔ |
| UNADJUDICATED-PINNED | 102 | **102** | unchanged | ✔ |
| MULTI (ratchet) | 249 | **249** | unchanged | ✔ |
| total keys | 2,784 | **2,782** | − K = −2 | ✔ |

**Checks after the swap, all green:**
- `check_quote_pins`: ratchet 1,922 against a ceiling of 2,287; 0 duplicate keys.
- `check_exact_counts`.
- 60's `S2`–`S8` and `S10`–`S12`.

## Predictions: two of six

| # | prediction | measured | |
|---|---|---|---|
| P1 | DIVERGENT 70–90 | **95** (every multi-site key) | ✘ high |
| P2 | RED-AFTER 40–75 | **19** | ✘ low |
| P3 | NO-TOKEN 4–15 | **8** | ✔ |
| P4 | NOT-DISCRIMINATING 2–12 | **6** | ✔ |
| P5 | go through 110–160; K 0–2 | **167; K = 2** | ✘ on the count (above the band); ✔ on K |
| P6 | MULTI and PINNED move by 0 | **0 and 0** | ✔ |

P5 was a two-part prediction, so this table scores it as a miss: the 167 lies above its 110–160 band, while K = 2
lies inside its band.

**What the misses say.**
- **P1 and P2 point the same way.** I expected the longer extension to fail on text at HEAD.
- **In fact the difficulty is concentrated in which keys are multi-site, not in how long the extension is.** Every
  multi-site key diverged, and the single-site keys nearly all went through. Drift since `fae76e75` cost one paper
  key.
- **The source half's RED-AFTER rate (18 of 46 tried) is the r7225 shape.** Source keys pin another receipt's
  source text, and that text moves.

## 66's reachable negative did not fire

DIVERGENT is 95 of 295 (32 %), under the stopping line of 147. The cheap mechanical fraction was 200 keys, and 167
of them went through.

**What it changes for `PO-78`'s plan:** the 95 DIVERGENT keys, all multi-site, are the arm's residue. Each needs
one extension per site, which means a per-site edit in the receipt, not a token swap. That is the repair this
mechanism cannot make.
