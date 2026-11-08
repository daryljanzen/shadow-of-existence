# r7703+70 — RESULT: the NS3 3600 degeneracy, FROZEN converged, and the receipt block

**Headline: converged, FROZEN agrees with the arm of record as DECOUPLED does.**
- FROZEN (L) is within 3.2% of arm A (L) and within 1.9% of DECOUPLED (L) at every ℓ = 2–8, at both points.
- The minimum stays at ℓ = 4, and recovery comes by ℓ = 8, on each row.
- The `NS3` 3600 "depths" were not depths. One mode at the freeze edge blew up but stayed finite, and the harness's `isfinite` guard let it through.

## Item 1 — the `NS3` 3600 degeneracy: diagnosed (hypothesis (a))

`diag_ns3.py` runs the receipt's own `_RUN`, read from its source, with a dump of the stored state. The dumps went to scratch (16 MB each); the logs are here.

**What happens at 3600:**
- One mode out of 738 is affected: k = 0.021181 Mpc⁻¹.
- It sits at **h·k = 0.079998**, a hair under the freeze cap `HKCAP` 0.08, so it is never frozen.
- It holds |Φ| ≈ 0.35 until η ≈ 11,100 (k·η ≈ 235). It then grows about 10⁸-fold over roughly 700 Mpc, an e-fold about every 10 steps, peaks at |Φ| = 7.9×10¹¹ at k·η ≈ 280, and falls back.
- It never becomes non-finite. So the guard (`RESULT NONFINITE` only on inf or NaN) passes it.
- Its contribution is smooth in k and dominates every Δ_ℓ, so Cd and Cc become proportional. Their normalised ratio is then exactly 1.000000 at every ℓ.
- Cd and Cc are about 10¹⁶–10¹⁷ at 3600, against about 10⁻² at 2400.

**The discriminating runs at 3600:**

| run | ℓ = 2 / 3 / 4 | reading |
|---|---|---|
| `HKCAP` 0.0799 (freezes just that mode) | 0.4697 / 0.4442 / 0.3415 | sane, on the 2400 trend (0.4695 / 0.4439 / 0.3411) |
| `LG` 20 (photon tower 12 → 20) | 1.0000 at every ℓ | the same mode blows up at the same η to the same peak, so the photon truncation plays no part |

**Why only 3600:**
- At 900, 1800 and 2400 the largest live mode also sits near h·k = 0.08 (0.0796, 0.07998, 0.0798).
- But its k·η₀ is 72, 153 and 204, below the k·η ≈ 250 where the blow-up begins.
- At 3600 the edge mode is k = 0.0212, so it reaches k·η ≈ 250 before η₀.
- At 3600 a mode at h·k = 0.0792 crosses k·η = 304 cleanly. So `HKCAP` 0.08 sits on the stability edge of the late-time system, between 0.0793 and 0.0800, and it bites only once a near-edge mode gets that far.
- **This is outside the registered list's specifics:** the onset tracks k·η, not h·k alone. I have not identified which eigenvalue sets the k·η ≈ 250 onset. The photon tower is ruled out; the neutrino tower (`LN` 12) is the untested candidate.

**What follows, as proposals (instrument edits, so 69's call):**
1. A magnitude guard in the harness, beside `isfinite`, for example `max|Φ|` over the stored window above 10 → `NONFINITE`. Every sane run here has max|Φ| ≤ 0.93.
2. A margin on `HKCAP`, for example 0.075. That needs a byte-identical gate for 900, because at 900 no mode near the edge reaches k·η = 250.

This item's runs carry the guard locally (`PHIMAX` printed per run), not in the instrument.

## Item 2 — FROZEN converged, banked

`run_frozen.py` + `bank_frozen.py` → `spectra/p15_lowell_depths_frozen_converged_leafrec1.npz`.
- The bank has 10 rows: `NS3` 1800 and 2400 plus the h² limit (h ∝ 1/`NS3`), at the distances (L), refit (L) and control (one clock) points, plus the control's 900.
- `config` carries `SPLITCLOCK` and `clock` per row, `numerics` per row, the HIER blob, the three points and the defining switches as null.
- The distances point's rungs come from r7701's follow-up, at 1800 and 2400. The 2400 rung was reproduced here to 1e-4 (`diag_2400.log`).
- Every run's max|Φ| is ≤ 0.93.

**Converged FROZEN, the h² limit:**

| point | ℓ = 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| distances (L) | 0.4701 | 0.4447 | 0.3424 | 0.6476 | 0.9057 | 0.9818 | 0.9978 |
| refit (L) | 0.4741 | 0.4536 | 0.3438 | 0.6434 | 0.9035 | 0.9815 | 0.9977 |
| control (one clock) | 0.4622 | 0.4129 | 0.3451 | 0.6687 | 0.9132 | 0.9842 | 0.9975 |

**Against the references, largest |Δ| over ℓ = 2–8:**

| point | 2400 vs h² | `NS3` 900 → h² | vs DECOUPLED | vs arm A (L) |
|---|---|---|---|---|
| distances (L) | 0.38% | +3.23% (ℓ = 4) | 1.81% (ℓ = 3) | 3.17% (ℓ = 4) |
| refit (L) | 0.38% | +3.18% (ℓ = 4) | 1.75% (ℓ = 3) | 3.07% (ℓ = 4) |
| control | 0.35% | +3.01% (ℓ = 4) | 2.03% (ℓ = 3) | — |

The control's 900 rung reproduces cc66's banked `FROZEN_control_KLO_0_1` exactly. Its DECOUPLED reference is cc66's `DECOUPLED_control_KLO_0_1_NS3_60000`.

**Against the predictions:**
- **P1 ✓:** the 2400 rung reproduces to 1e-4.
- **P2 ✓:** within 3.1% of arm A (L) against a 4% bar, and within 1.8% of DECOUPLED against a 3% bar.
- **P3 ✓:** the control is unconverged in the same direction. Raising the count raises the ℓ = 4 value, by +3.0%, inside 1–5%. ⚠ My registration also called this "deepens", which is the wrong word: the value rises, so the trough gets shallower.
- **P4 ✓:** 0.35–0.38%, against a 0.5% bar.

## Item 3 — the receipt block, routed to cc66 and not pushed

- `receipt_block.py` holds the 63-line block. `receipt_block.diff` inserts it after line 1026 of `P15_the_low_multipole_depth_gap…` at main `f38156a93`: after cc66's last `(L)` block and before the closing "WHAT THIS SETTLES" section.
- **It reads both banks and asserts their own `config` first:** `SPLITCLOCK` `L` on every (L) row, `STACKPERT` unset, `NS3` named per row.
- **It then pins:**
  - DECOUPLED (L)'s moves under the three knobs: 0.00%, 0.00% and ≤ 0.36%;
  - converged FROZEN at 2400 within 0.4% of its h² limit;
  - the banked 900 row 2–4.5% off at ℓ = 4;
  - converged FROZEN within 3.2% of arm A (L) and 1.9% of DECOUPLED at both points, with the minimum at ℓ = 4 and recovery by ℓ = 8.
- **Tested on a scratch copy at main:** all 7 new checks pass and the receipt ends ALL CHECKS PASSED.
- The block reuses the names cc66's (L) block defines (`_LAZ`, `_LBZ`, `_LE`, `_ARMA`, `_LDEC`, `_LFRO`). So it must sit after that block.

## Gates

- `check_banked_config`: PASS, 308 banked.
- `--class1`: see the commit.
- The receipt with the block applied, on a scratch copy: ALL CHECKS PASSED. The receipt in the tree is untouched.
