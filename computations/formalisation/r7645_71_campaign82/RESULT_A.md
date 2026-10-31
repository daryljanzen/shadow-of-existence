# `r7645+71.3` — RESULT: campaign 82. The witness for `kh_lemma_killing` and `kh_cor_stationary` is BUILT: Minkowski 1+1 in light-cone form, with the adapted direction a null translation. A finding comes with it: `KillingChart` does not require a nondegenerate metric, so the **zero metric satisfies every hypothesis trivially**. The witness is shown Lorentzian, so it is a genuine instance. ⌗ `409` lines in one probe (about `150` new, band 50–600 new). ⌗ p: `0.85` and `0.75`, both came true

*Against `PREDICTION.md` (`r7645+71.2`). 71 re-ran `lake env lean probes/KillingWitness.lean`. It exits 0 with no
errors. All `30` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The forbidden-token grep is
clean. Campaign 59's `KillingHorizon.lean` is copied verbatim under `ShadowProbe.KillingWitnessProbe`, with the prefix
`kw_`.*

## The witness — BUILT

***The chart.*** `kw_chart` has the constant `g = kw_lightCone`, which is `ds² = 2 dλ dx`. The Killing condition holds
by `rfl`. `g₀₀ = 0`, so `χ = ∂_λ` is null.

***`kw_lemma_killing_witness`.*** `MetricallyCoincident` holds for the concrete pair `p = (0,0) ≠ q = (1,0)` on one
orbit. It follows from `kw_lemma_killing`, with `hnull` proved (`kw_hnull`).

***`kw_cor_stationary_witness`.***
- `H` is the union of orbits through `X = {0}`, which is the null line. It is non-empty.
- `Rigidity 1 H` is built from the chart.
- The corollary's conclusion is exhibited, with the same concrete pair.

## The finding: the hypotheses admit the zero metric

- **`kw_zero_rigidity`.** `KillingChart` asks only that `g` be symmetric and `λ`-independent, so `g ≡ 0` gives
  `Rigidity 1 univ`. Every point is then "metrically coincident" with every other on its orbit.
- **So the Lean lemma is satisfiable trivially.** That is not a contradiction like campaigns 74–75, but the
  hypotheses are weaker than P1's.
- **The witness is genuinely Lorentzian.** `kw_lorentzian` proves it: `det = −1`, a timelike vector `(1,−1)`, an
  orthogonal spacelike `(1,1)`, signature `(−,+)`, and `ds²(χ) = 0`.
- **P1's `lem:killing` is about a Lorentzian `g`.** The inventory's row now reads: BUILT IN PART (one global adapted
  chart; no nondegeneracy hypothesis in `KillingChart`), witnessed non-trivially in flat space.
- **The cheap repair** is to add nondegeneracy to `KillingChart`. Campaign 59's theorems would not use it, so they
  re-check unchanged. That is a suggested follow-up, not done here, to keep campaign 59's interface fixed.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
