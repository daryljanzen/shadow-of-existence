# `r7443+71.18` — PRE-REGISTRATION: campaign 38, library-gap row 63 (the degeneracy needs r constant, not the cosh). ⌗ `380` lines (band 200–800), ⛔ stop `1200`. ⌗ p `0.40` for A, B and formal D; p `0.20` that C is built

*Under `r7443` ②, step 4, registered with campaign 37 in one push. The receipt is
`P10_the_degeneracy_needs_r_constant_not_the_cosh_so_the_anomaly_is_what_makes_its_own_constant_observable.py`.
No Lean was written before this registration.*

## ① The piece: `probes/Row63Anomaly.lean`

- ***A1.*** `R = 6(ä/a + ȧ²/a² + 1/a²)`, which is `12/α²` on `α cosh(T/α)`.
- ***A2.*** The variance identity and its consequences.
- ***A3.*** `Λ + radiation` gives `R = 4Λ` with `dR/da = 0`.
- ***B.*** The bare trace `Θ = 0` for `ρ ∝ a⁻⁴`. The renormalised trace `Θ = r/(2π²a⁴)`, independent of `μ` and
  `C`. Then `R = 4Λ + 8πGΘ`, with `dR/da ≠ 0` iff `r ≠ 0`.
- ***D, in the receipt's formal sense.*** `ζ_Δ(0)` by the receipt's asymptotic rule, using Mathlib's `ζ(0) = −½`,
  `ζ(−2) = 0` and the residue at `1`:
  - the free tower gives `10`;
  - the shifts `+δ`, `×L`, `+b/m²` and `+b/m⁴` leave `10`;
  - `+cm` gives `10 + 3c − c³/3`;
  - `+c/m` gives `10 − c`.
- ***C, the hard part, registered as such.*** The receipt computes `∫√g R^k` (`k = 0, 1, 2`) over three regions by
  40-digit quadrature, then takes an SVD: rank `1` for the null controls and rank `3` with the anomaly.
  - Rank `1` is structural when `R` is constant, and will be built.
  - Rank `3` needs either verified numerical integration or a structural determinant argument. If neither is
    reached, that is ***REPORTED as the specific obstruction***, per `r7443` ③: which integrals, which property, and
    what a from-scratch version would assume.

***Caveats, registered.***
- ***Imported:***
  - the residue `r = 15/4` and `ζ₀ = 10` ("banked" in the receipt);
  - the semiclassical form `C + r log(aμ)`;
  - the TT spectrum and degeneracy.
- ***The genuine `ζ_Δ`*** (meromorphic continuation of the level sum) is not in this campaign. D is the receipt's
  formal rule, as the receipt computes it.
- The paper-text parses are pins.

***Failable:*** BUILT, BUILT IN PART, or REPORTED.

***Census:***
- If BUILT including C: row 63 → `DONE`.
- If C is reported as the obstruction: row 63 → `DONE (chartable half)`, the half named exactly.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
