# r7703+70 — PREDICTION (registered before any run)

The order (`FOR_70.md`, `r7703`) has three items:
1. diagnose the `NS3` 3600 degeneracy;
2. converge FROZEN on (L) at both points, and on the control background, and bank the result with its numerics;
3. a receipt block that reads the convergence bank and the converged FROZEN row, with the patch routed to cc66.

## Item 1 — what the degeneracy is

**What is known.** `_RUN` returns `r = pl(Cd)/pl(Cc)`. It is exactly 1.0000 at ℓ = 2..8 on two runs at `NS3` 3600, while 450, 900, 1800 and 2400 all give finite, sensible depths.

`r ≡ 1` needs the discrete sum to equal the continuum at every ℓ, up to the shared ℓ 25–40 normalisation. That happens only if the spectrum is dominated by a part that does not depend on the k sampling of the source.

**Registered hypotheses, in the order I will test them:**
- **(a) A blow-up in the late stage that stays finite but huge.** It could come from a mode left live, or from the store's `(n % STRIDE)` sampling meeting the g3 stage. A single huge, k-smooth contribution to every Δ_ℓ makes Cd and Cc proportional. The `isfinite` guard does not catch it.
- **(b) The store or the visibility mask at the g2/g3 junction.** `m = E > max(e_sw, eta_rec-160)` and the stride interact with the g3 grid length.
- **(c) Something in the harness, not HIER.** For example, a parse of the `RESULT` line.

**What will count as diagnosed:** the first η where the stored source is non-physical (|Φ| or |Θ₀| grows more than 100× its value at η_rec), or the code line that makes `r ≡ 1`, reproduced in a minimal script.

**Expected:** (a), as an RK4 step-size or freeze interaction. I put 50% on (a), 30% on (b) and 20% on (c).

## Item 2 — converged FROZEN

- **P1:** FROZEN (L) at `NS3` 2400, or at the count the diagnosis shows safe, at the distances point reproduces the r7701 follow-up's 2400 row to 1e-4.
- **P2:** at the second point (the adjudicated / banked one), the converged FROZEN (L) row sits within 4% of arm A (L) at every ℓ = 2..8, and within 3% of DECOUPLED (L).
- **P3:** on the control background, FROZEN at `NS3` 900 is unconverged in the same direction as on (L): raising the count deepens ℓ = 4, that is, raises its depth value. The move from 900 to the converged count at ℓ = 4 is between 1% and 5%.
- **P4:** the h² extrapolation from 1800 and 2400 agrees with the 2400 value to 0.5% at every ℓ.

## Item 3

- The block is written as a patch, and its line range is sent to cc66 through `FOR_66` before any push to the receipt.
- The bank gets `config` and `numerics` per row.
- `check_banked_config` must pass, and the receipt must run green by stem.
