# r7681+70 — RESULT

**The low-ℓ depths at ℓ = 2–8 on the arm of record are banked as one source:** `spectra/p15_lowell_depths_leafrec1.npz` (an addition). It holds three rows, `armA_exact`, `armB_frozen` and `armB_decoupled`, plus `ells`, `config` and `manifest`.

Every row has its minimum at ℓ = 4 and recovers by ℓ = 8. "Recovers" means the first ℓ ≥ 5 with depth ≥ 0.99.

## The rows, at the refit licensed point

The point is H0 68.570730, Ωm 0.291246, ω_b 0.021643, radiation 4.15e-5/h².

| ℓ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | recovery |
|---|---|---|---|---|---|---|---|---|
| **arm A, exact transfer (CAMB)** | 0.4920 | 0.4434 | 0.3601 | 0.6627 | 0.9097 | 0.9827 | 0.9980 | ℓ=8 |
| **arm B, split clock, FROZEN** | 0.4697 | 0.4649 | 0.3424 | 0.6321 | 0.8985 | 0.9805 | 1.0003 | ℓ=8 |
| **arm B, split clock, DECOUPLED** | 0.4826 | 0.4680 | 0.3604 | 0.6469 | 0.9046 | 0.9808 | 0.9982 | ℓ=8 |
| *P15 l.2809–2810 (arm A, adjudicated point)* | *0.487* | *0.435* | *0.359* | *0.666* | *0.911* | *0.983* | *0.998* | *ℓ=8* |

## How

`bank_depths.py` → `depths.json`.
- **Arm A** is the receipt's own `armA`, lifted by `ast`. Each run takes about 7 s.
- **Arm B** is the receipt's arm-B harness with its own CASES, lifted by `rederive_lowell_sweep.engine()`, with `SPLITCLOCK=1`. FROZEN took 74 s and DECOUPLED 766 s.

**Checks:**
- **R1 holds.** Arm B reproduces r7675's banked `cc66_lowell_sweep_leafrec1` keys exactly (max difference 0), so the `SPLITIC` edit since then changed nothing.
- **R2 holds.** Arm A at the adjudicated point reproduces P15's printed seven exactly at their three decimals.
- **R3 holds.** Every row recovers at ℓ = 8.

**These values were measured at r7675 before this order.** PREDICTION.md says so and registers only R1–R3.

## Gates

- `check_banked_config`: passes, with the four ACOUSTIC defining keys written as `null` and said so in the config.
- No receipt reads the new file yet, so there is no reader to run by stem. cc66's draft and receipts will be its readers.
