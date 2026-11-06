# r7689+70 — RESULT, item 1: the one-clock leg at the distances point

**The clock carries the octopole's excess.**
- With one clock, the hierarchy sits **1.0% (FROZEN) and 1.1% (DECOUPLED) below** the exact transfer at ℓ = 3.
- With the split clock, at the same point, it sits 4.9% and 5.5% above.
- The tower builds disagree by 0.1% at ℓ = 3 on one clock (0.67% on the split). So the +5.5% is the split clock's shift (+0.026 / +0.029), not the tower treatment's.

**The one-clock namesake is now pinned to this point.** The leg reproduces `cc66_lowell_sweep.npz`'s two adjudicated rows to **0.0000 at every ℓ = 2–8**. So the namesake's adjudicated rows are this point's one-clock rows. That is now read from a bank that records its point, not from a manifest sentence.

Bank change: **addition**, `spectra/p15_lowell_depths_distances_oneclock_leafrec1.npz`:
- `ells`, `armB_frozen`, `armB_decoupled`;
- `config`: H0, Om, WBH2, radiation, BR0, `SPLITCLOCK=False`, the HIER blob, and the defining keys written as null with a note;
- `manifest`: the point and `SPLITCLOCK=False`.

## What was run

`bank_one_clock.py` → `one_clock.json`.
- r7683's `bank_depths.py` arm-B legs, with `SPLITCLOCK=1` removed and nothing else changed.
- The harness is the receipt's arm B, through `rederive_lowell_sweep.engine()`, at the two adjudicated cases.
- The point is 68.60 / 0.2973, ω_b 0.02237, radiation 4.1833e-5/h² (`OBF`/`ORF` unset).
- **LEAFREC:** with `ARM` and `SPLITCLOCK` both unset, HIER runs the content-carrying leaf rate for everything, ionisation history included. So recombination is on the leaf rate. HIER has no `LEAFREC` switch, and the config says so.
- **Wall time:** FROZEN 82 s, DECOUPLED 716 s, in parallel.

## The table: depth by ℓ, and residual against arm A

| ℓ | arm A | one clock FROZEN | one clock DECOUPLED | split FROZEN (r7683) | split DECOUPLED (r7683) |
|---|---|---|---|---|---|
| 2 | 0.4874 | 0.4707 (−3.43%) | 0.4774 (−2.05%) | 0.4658 (−4.43%) | 0.4781 (−1.91%) |
| **3** | **0.4348** | **0.4304 (−1.01%)** | **0.4300 (−1.10%)** | **0.4560 (+4.88%)** | **0.4589 (+5.54%)** |
| 4 | 0.3590 | 0.3365 (−6.27%) | 0.3485 (−2.92%) | 0.3405 (−5.15%) | 0.3581 (−0.25%) |
| 5 | 0.6663 | 0.6517 (−2.19%) | 0.6587 (−1.14%) | 0.6363 (−4.50%) | 0.6508 (−2.33%) |
| 6 | 0.9113 | 0.9086 (−0.30%) | 0.9091 (−0.24%) | 0.9004 (−1.20%) | 0.9061 (−0.57%) |
| 7 | 0.9831 | 0.9827 (−0.04%) | 0.9820 (−0.11%) | 0.9820 (−0.11%) | 0.9818 (−0.13%) |
| 8 | 0.9981 | 0.9966 (−0.15%) | 0.9975 (−0.06%) | 0.9997 (+0.16%) | 0.9977 (−0.04%) |

- Minimum at ℓ = 4 and recovery at ℓ = 8 on both one-clock rows.
- **Split minus one clock:**
  - FROZEN: −0.0049, **+0.0256**, +0.0040, −0.0154, −0.0082, −0.0007, +0.0031;
  - DECOUPLED: +0.0007, **+0.0289**, +0.0096, −0.0079, −0.0030, −0.0002, +0.0002.

## What this says, and what it does not

- **The octopole exception is the split clock's.** On one clock the hierarchy is below arm A at every ℓ = 2–8 on both builds, and ℓ = 3 is not an exception. The split lifts ℓ = 3 by 0.026 / 0.029, which turns −1% into +5%.
- **Not every residual shrinks on one clock.** DECOUPLED's largest one-clock residual is −2.92% at ℓ = 4, where the split's is −0.25%. Its largest away from ℓ = 3 is 2.92% on one clock against 2.33% on the split. So one clock is not uniformly closer to arm A; it only removes the ℓ = 3 exception.
- **Which clock is right is not decided here.** That is the arm-of-record question (the split is ACOUSTIC_two_arm's construction), and it was settled at r7677/r7679. This bank attributes the excess; it does not adjudicate it.

## The receipt gate

The `the_low_multipole_depth_gap…` gate (the ⛔ "what this bank cannot say" check) asserts `'config' not in cc66_lowell_sweep.npz`. That file is a namesake, and banks are additions only, so this run leaves it untouched and **the gate stays green as written**. The gate goes red, as intended, only when it reads the new sibling. The repoint is cc66's.

## Predictions

- **P1 (namesake reproduced to ≤ 0.001): holds, exactly** (max |Δ| 0.0000).
- **P2 (one-clock ℓ = 3 about 1% below arm A, within −0.5% to −1.5%): holds**, at −1.01% and −1.10%.
- **P3 (minimum at 4, recovery at 8): holds.**
- **The reachable negative (ℓ = 3 ≥ 0.450) did not fire:** 0.4304 and 0.4300.
- **Price:** about 12 min registered; 12 min run.

## Gates

- `check_banked_config`: passes.
- `P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py` run by stem: ALL CHECKS PASSED. No receipt reads the new bank yet.
- `run_touched_readers.sh --class1`: GREEN.
