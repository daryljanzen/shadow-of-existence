# `r7801+cc66.1` — RESULT: both items

**9 of 9 gates**, `rc=0`, **18 of 18 published figures pinned**
(`receipts/P15_CR_cosmology/P15_the_frozen_build_measured_on_the_one_rate_is_3_3_not_the_carried_3_4_and_theta_star_at_the_combs_own_point_is_plus_4_8_sigma.py`).
Every registered row held.

## ① The frozen build, measured

The leg the order needs — `distances__armB_frozen__one_clock__*` — **was the hole in the lattice**:
`r7703+70` banked the (L) legs at the distances and refit points and the one-clock legs at the
*control* point, so the one combination was missing. Added by giving that producer's own `POINTS`
table one more entry (the distances' background with **no `SPLITCLOCK` key**) and running its two
rungs.

| | ℓ=2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| NS3 = 1800 | 0.4743 | 0.4363 | 0.3453 | 0.6558 | 0.9082 | 0.9818 | 0.9975 |
| NS3 = 2400 | 0.4747 | 0.4370 | 0.3462 | 0.6563 | 0.9084 | 0.9819 | 0.9975 |
| **h² extrapolated** | **0.4752** | **0.4379** | **0.3474** | **0.6569** | **0.9087** | **0.9820** | **0.9975** |

| one-rate frozen, distances' point | vs exact transfer | vs decoupled |
|---|---|---|
| **MEASURED (h²)** | **3.339 %** (ℓ=4) | **1.837 %** (ℓ=3) |
| carried at `r7799` (additive) | 3.395 % | 1.767 % |
| carried at `r7799` (multiplicative) | 3.351 % | 1.740 % |
| the (L) baseline the paper had | 3.167 % | 1.809 % |

### ⛔ The carry held — and that is only worth saying because the row could have said otherwise

Deltas **−0.056** and **+0.070** percentage points, inside the **±0.3** registered. So the clock- and
point-stability argument under the carry was sound, and the largest per-multipole depth disagreement
is `0.0033`.

**But it was just enough to move the printed digit.** The carried `3.395` rounds to **3.4**, which
`P15` prints today; the measured `3.339` rounds to **3.3**. The decoupled figure rounds to **1.8**
either way. ⇒ **`P15` has one digit to change, not two.**

### Both guards held, and both are inherited rather than invented

- `max|Φ| = 0.926779` on each rung, inside the `≤ 0.93` every banked rung keeps. `r7703` item 1 found
  that a **finite** blow-up passes the harness's `isfinite` test and silently returns `r = 1` — so the
  rung that *looks* converged is the one to distrust.
- `NS3` stayed at 1800/2400. `NS3 ≥ ~3000` is unusable: at 3600 the mode at the `HKCAP` edge
  (`h·k = 0.079998`) blows up at `k·η ≈ 250`.
- The launcher additionally **asserts `SPLITCLOCK` is absent from the child's environment**, because
  "one rate" here *is* the absence of that switch.

## ② θ\* — and the order's premise corrected

⛔ The order says the `+2.3σ` figure is *"from the early leaf-rate refit (r7753)"* and asks for it
re-solved *"on the build the comb's 298.5 comes from"*, as though it were one quantity at a stale
revision. **It is a different point.**

`spectra/r7749_leafgeom_nofit_L2000_cr.npz`'s own `__SWITCHES__` read
`ARM=cr CRH0=68.60 CROM=0.2973 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1`, and its manifest records
`point: {CRH0: 68.60, CROM: 0.2973}` — **the distances' point.**

| point | 100θ\*, leaf rate | pull | matching onset |
|---|---|---|---|
| **distances' (68.60, 0.2973, 0.02237)** ← the 298.5 build | **1.04235** | **+4.84 σ** | 1.231e6 (ρ_r/ρ_m 365.25) |
| arm-of-record refit (68.5707, 0.29125, 0.021643) | 1.04215 | +4.18 σ | 1.404e6 |
| leaf-rate refit minimum (68.5857, 0.29446, 0.022181) | 1.04157 | **+2.33 σ** ← the printed figure | 2.437e6 |

⇒ **The figure `P15` can cite for that build is `+4.8σ`, and it is worse than the `+2.3σ` now in
print by about a factor of two in the pull.**

**Re-solved, not quoted:** `theta_corpus.py` was executed and all six stored rows reproduced, **0
moved**. On the arm of record at the same point the pull is `−11.92σ` and **no onset reaches
`θ_obs`** in `[1.2e3, 1e9]` — so the onset is the half of the result saying the leaf-rate assignment
is not merely closer but *reachable*.

## Failability — measured, not asserted (`failability.py`)

| probe | reddens | holds |
|---|---|---|
| **P1** the measured h² leg ×1.01 | ③ ④ ⑧ | ① ② ⑤ ⑥ ⑦ ⑨ |
| **P2** the comb build's switches rewritten to the refit minimum | **⑥ only** | the rest |
| **P3** a rung's `max|Φ|` pushed past 0.93 | ② ⑧ | the rest |

P2 reddening ⑥ alone is the point: the premise row is identified from the bank's own switches and
nothing else.

## Not claimed

Which point `P15` should quote, and whether `+4.8σ` is acceptable, are 69's. Nothing is refitted, no
minimum is sought, `θ_obs = 0.0104085 ± 3.1e-6` is inherited, and **this receipt writes no bank** —
the measured depths stay in `frozen_one_clock.json`; banking them into a shared `spectra` bank is
69's or 70's call. Gate ⑨ asserts that against the receipt's own AST (no `savez`).
