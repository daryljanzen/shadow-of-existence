# r7705+70 — PREDICTION (registered before any edit or run)

The order (`FOR_70.md`, `r7705`) has three items:
1. Add the magnitude guard to the arm-B harness, with a gate.
2. One diagnostic run on the neutrino tower, to name the k·η ≈ 250 instability.
3. Tonight's nightly.

## Item 1 — the guard

**The edit.** It goes in `_RUN`, in `receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap…`. That is the only copy of the harness: `rederive_lowell_sweep.engine()` and my r7703 scripts read it from there.
- After the stored window `ee, Yv` is cut, if max|Φ| over it exceeds 10, print `RESULT NONFINITE | max|Phi| … eta_end …` and stop.
- `armB` already maps `RESULT NONFINITE` to `(None, meta)`, so no reader changes.
- **It is not a switch.** No environment variable turns it on or off, so it does not enter the switch census.
- HIER is untouched.

**The re-bank rule:**
- No banked `config` records the receipt's blob. Every arm-B bank records `HIER_blob`, and the edit does not move it.
- **Prediction: nothing is re-banked.**

**The byte-identity gate (`gate_guard.py`):**
- Run the harness before and after the edit on:
  - every configuration in `rederive_lowell_sweep.CASES`;
  - the four (L) rows of `p15_lowell_depths_leafpert_leafrec1`;
  - FROZEN (L) `NS3` 1800 and 2400 at the distances point.
- Compare the `RESULT` lines byte for byte.
- **Prediction: identical on every one.** Every banked run has max|Φ| ≤ 0.93, so the guard cannot fire on it.
- **Positive control:** FROZEN (L) `NS3` 3600 at the distances point. Before the edit it returns `RESULT 1.000000 …`. After the edit it returns `RESULT NONFINITE`, so `armB` gives `None`.

**Readers, run by stem:**
- the low-ℓ receipt: it must still end ALL CHECKS PASSED, and its own `armB` calls must be unchanged;
- `rederive_lowell_sweep.py`, the engine read;
- `--class1`.

## Item 2 — the neutrino tower

One run: FROZEN (L), distances point, `NS3` 3600, `LN` 20 (neutrino multipoles 12 → 20), all else as the degenerate run.
- **If the neutrino truncation sets the onset:** the k = 0.02118 blow-up moves to larger k·η or vanishes.
- **If it does not:** the same onset at k·η ≈ 250 and the same peak, as `LG` 20 gave.

**Registered expectation: the neutrino tower does NOT set it (55%).** My reason is that `LG` 20 left the onset identical to the step. If the neutrino tower is excluded too, the next candidate is the Φ / δ_c / θ_b fluid block's own explicit-RK4 limit, which the late-time `k²/(3ℋ)` rate controls. The stored state (Φ only) cannot separate those, so I will say so rather than name an eigenvalue I have not computed.

## Item 3

The 11-08 nightly, read by the nightly routine at about 11:04 UTC, with its walls recorded against 180 min.
