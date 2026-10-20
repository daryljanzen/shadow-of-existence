# `r7443+71.37` — PRE-REGISTRATION: campaign 46, the twelve `LIMIT OF A DONE ROW` rows (9, 10, 12, 21, 26, 40, 91, 97, 100, 101, 105, 106), each built to its receipt's computed checks. ⌗ `1400` lines in two probes (band 700–2400), ⛔ stop `3000`. ⌗ p `0.30` that all twelve close; median `9` of `12`

*Under `r7443`: a row leaves the list only by being `DONE` or by a specific Lean obstruction, never by
reclassification. The twelve were classified LIMIT at `r7411+71.2` (`r7411_71_kinds/CLASSIFICATION.tsv`, which
names what each receipt computes and the DONE theorem that carries it). No Lean was written before this
registration. Receipts are in ROWS.tsv, column 6.*

## ① The pieces

***`probes/LimitNariai.lean`*** (rows 12, 21, 100, 101, 105). Built on `row104_nariai_root`, `nariai_curvature`
and `sinh23_flow`, copied.
- ***105:***
  - `f(ρ) = f′(ρ) = 0`, `f″(ρ) = −6/α²` at `M_N`;
  - `f ≤ 0` ***everywhere***, by the factorisation `−α²r f = (r − ρ)²(r + 2ρ)`, which is stronger than the
    receipt's 8 samples.
- ***12:*** the double root, `f″ = −6/α²`, `f < 0` at the sample points (by the factorisation), and the blueshift
  limits of `1/√(2κδ)` as `δ → 0`, as `Tendsto` statements.
- ***21:*** `f′ = 0 ⇒ M = r³/α²`, the Nariai radius and mass, `f″(r_n) = −6/α²`, `L² = r_n²`, and the
  leading-order splitting `dr² ∝ δM` as the truncation the receipt states.
- ***100:***
  - `1 − f = 2M/r + r²/α²`;
  - the double root and `α²r f = −(r − r_N)²(r + 2r_N)`;
  - `dS₂ × S²` with `R = 4Λ`, `K = 8Λ²`.
  - The log divergence of `∫dr/√(−f)` is to be proved ***analytically***, not numerically: the integrand is
    `≍ 1/|r − r_N|` near the double root. Where the receipt only samples, the Lean statement is non-integrability
    or a divergent lower bound.
- ***101:***
  - the turning point `(Mα²)^{1/3} = r_N`;
  - the derivatives of the cosh and sinh^{2/3} legs at the special points;
  - the quartic root and the Beta-type ratio, in closed form where one exists. Otherwise they are bracketed by
    rational bounds, and the floating digits are recorded as not built.

***`probes/LimitQuadricFlow.lean`*** (rows 9, 10, 106, 91, 97, 26, 40). Built on `section_quadric`,
`dS5_constant_curvature`, `sinh23_flow`, `sds_kretschmann`, `unruh_ds_limits`, `two_surface_gravities`,
`ds_horizon_iff` and `ds_surface_gravity`, copied.
- ***9:*** the orthogonal split for `D = 5..8`, the rank-1 Jacobian, and `u − u³` with exactly three roots.
- ***10:*** the spacelike split for `D = 5, 6`, and the timelike and null coefficient reads.
- ***106:*** the Wick map `X₀ ↦ iX₀` sending `−X₀² + ΣXᵢ²` to `ΣXᵢ²`, and `d ln v/d ln α` an integer for the
  constant-curvature invariants.
- ***91:*** the sinh^{2/3} law solves `r′² = 2M/r + r²/α²`, and `M = −r³/(2α²)` at `E = 1`.
- ***97:*** §A the first integral, §B Ricci of `ℝ × S²` and `S³`, and §C the SdS Kretschmann identity (the
  receipt's 6 numeric points as instances of the closed form).
- ***26:*** `κ = 1/α` and `T(a) = √(1/α² + a²)/2π` with its limits, from the four DONE theorems. The
  "completion" table is the receipt's hard-coded definition, stated as such.
- ***40:*** the marginal-geodesic first integral for `D = 4..8`, generalising `sinh23_flow`, and the receipt's
  root of unity at `D = 8`. The deck group `Z_{D−1}` is not claimed; it is NAMED ORDER at `r7421`.

***Caveats, registered.***
- Symbol-occurrence and paper-text checks ("text pins") are not formalised, as for every DONE row.
- Floating numerics that have no closed form are bracketed or recorded as not built. They are never asserted from
  floats.

***Failable,*** per row: `DONE` when its computed checks are built (text pins excepted); otherwise it stays LIMIT
with the missing check named. ***p `0.30`*** that all twelve close; median prediction `9` of `12`. ***Risks:***
- row 101's numerics;
- row 100's divergence statement;
- row 40's general-`D` integral.

***Census if built:*** each closing row → `DONE`, imports named, `decl` filled.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
