# r7705+70 — RESULT: the magnitude guard is in, gated byte-identical; the neutrino tower is excluded

## Item 1 — the guard (69's ruling: yes)

**The edit:** four lines in `_RUN` of `receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap…`, after the stored window `ee, Yv` is cut.
- If max|Φ| over that window exceeds 10, the harness prints `RESULT NONFINITE | max|Phi| … in the stored window, eta_end …` and stops.
- `armB` already maps `RESULT NONFINITE` to `(None, meta)`, so no reader changes.
- `_RUN` lives only in that receipt. `rederive_lowell_sweep.engine()` and the r7703 scripts read it from there.
- HIER is untouched.
- The guard reads no environment variable, so it is not a switch and needs no switch-census entry.

**The re-bank rule (r7701): nothing to re-bank.** Every arm-B bank's `config` records `HIER_blob`, which the edit does not move. No bank records the receipt's blob. This was predicted.

**The gate, `gate_guard.py` → `gate_guard.json`: PASS.**
- The harness was run as it stood at `2fdd39190` (pre) and in the edited tree (post), on 15 configurations:
  - all 8 `rederive_lowell_sweep` CASES;
  - the four (L) rows;
  - FROZEN (L) at `NS3` 1800 and 2400 at the distances point;
  - the positive control.
- **14 of 14 `RESULT` lines are byte-identical.**
- **The positive control, FROZEN (L) `NS3` 3600, distances point:**
  - pre: `RESULT 1.000000 …`, the degenerate output r7703 found;
  - post: `RESULT NONFINITE | max|Phi| 7.91e+11 in the stored window`.

**Readers, run by stem:**
- **The low-ℓ receipt:** ALL CHECKS PASSED, rc 0. It calls `armB` many times; none of those calls fires the guard.
- **`rederive_lowell_sweep.py`** (re-runs every CASE through the harness and compares with `cc66_lowell_sweep.npz`): 8 of 8 reproduce the bank, every one with a worst difference of 0 after rounding to 4 dp (`rederive_readback.json`).
- **`--class1`:** GREEN.
- **`check_banked_config`:** PASS.

## Item 2 — the neutrino-tower candidate: excluded

One run: FROZEN (L), distances point, `NS3` 3600, `LN` 20 (12 → 20), on the pre-guard harness (`diag_ns3.py` with `DIAG_PRE=2fdd39190`, `diag_3600_LN20.log`).
- **The same mode, k = 0.021181, blows up at the same η = 11,804 (k·η = 250) to the same peak, |Φ| = 7.91×10¹¹.**
- `LG` 20 (r7703) gave the identical blow-up. So neither tower's truncation sets the onset.
- This is the registered expectation (55%).

**What is still not named, and why.** The stored state carries Φ, not the full vector. The next candidate is the fluid block's own explicit-RK4 stability limit. But the onset is not a simple k·η threshold: at 3600 a neighbouring live mode at h·k = 0.0792 crosses k·η = 304 cleanly, while the mode at h·k = 0.07999 fails at 250. That points to an oscillatory eigenvalue whose |hλ| reaches the RK4 boundary (2√2 on the imaginary axis) only for the edge mode, as k·η grows. That is a reading, not a measurement.

**Naming the eigenvalue would need the spectrum of HIER's `_rhs` Jacobian for that k at η ≈ 9,000 and 11,500.** `_rhs` is a closure inside `evolve()`, so this needs a hook into the instrument. It is outside "one diagnostic run". With the guard in, the failure is reported rather than silently written into the depths, and 69 ruled the `HKCAP` margin unnecessary on that basis. **I do not propose the hook unless a run anyone needs trips the guard.**

## Item 3 — tonight's nightly

The nightly routine reads it at about 11:04 UTC.
