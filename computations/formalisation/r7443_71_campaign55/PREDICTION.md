# `r7443+71.68` — PRE-REGISTRATION: campaign 55, programme stage P4 — the assembly: T★, completeness of the TT spectrum of S³. ⌗ `1500` lines (band 700–3200), ⛔ stop `4500`. ⌗ p `0.35`

*The last stage of `r7443_71_pw_programme/PROGRAMME.md`. It builds on P1 (`probes/S3Integration.lean`, campaign 52),
P2 (`probes/S3PolySpectrum.lean`, campaign 53) and P3 (`probes/S3Density.lean`, campaign 54), all copied because
probes cannot import probes. No Lean was written before this registration.*

## ① The theorem: `probes/S3TTComplete.lean`

***T★, as stated here.*** Let `h` be a symmetric traceless 2-tensor field (frame components `ℝ⁴ → ℂ`, of class
`C²`) whose divergence vanishes on S³, and which satisfies `−∇²h = λh` on S³. If `h` is not identically zero on S³,
then:
- `λ = m² − 3` for some `m ≥ 3`;
- the restriction of `h` to S³ equals the restriction of a polynomial tensor in P2's `TTQ d (m² − 3)`. That space
  is spanned by campaign 51's level-`m` eigen-tensors and has dimension exactly `2(m² − 4)`.

***The route.***
1. ***Bridges.***
   - P1's analytic `∇²` (`lapA`) on polynomial tensors equals P2's algebraic `lap`, through P1's `evT_lap` and an
     unfolding of P2's `nab`.
   - P3's real `L²` density, applied to real and imaginary parts, gives complex density for complex tensor fields.
   - A single `L²` inner product on tensor fields, `∫ Σ_bc conj(h_bc) k_bc dσ`, which is P1's `ip`.
2. ***Orthogonality.*** For each `−∇²`-eigenvector `p` in P2's eigenbasis `Ev` of `P_d` (for every `d`) with eigenvalue
   `μ ≠ λ`: `⟨h, p⟩ = 0`, by P1's `lap_symm` and `μ, λ` real (`λ` real by `neg_lap_nonneg` applied to `h` itself).
3. ***Finite-dimensionality.*** By P2's `degree_bound`, the polynomial `λ`-eigenspace `E_λ` lies in `P_{D(λ)}`, so it
   is finite-dimensional. Orthogonal projection `π` onto `E_λ` in `L²(σ)` exists.
4. ***Vanishing.*** `h − πh` is orthogonal to `E_λ` and, by 2, to every other eigenvector. It is therefore orthogonal
   to every polynomial tensor, since `Ev` spans each `P_d` by P2's `Sd_eq_span`. By P3's density, `h − πh = 0` in
   `L²`. Both are continuous and `σ` has full support on S³ (to be proved), so `h = πh` pointwise on S³.
5. ***The TT condition carries.*** `πh` is a polynomial tensor equal to `h` on S³, so its divergence vanishes on S³ and
   its class lies in `TTQ d λ`. Then P2's `tt_spectrum` and `tt_count` give the conclusion.

***Scope, registered.***
- `C²` fields on ℝ⁴ restricted to S³. The extension of a field given only on S³ (`h(x/|x|)` times a radial bump) is
  an optional item 6. Without it, T★ is stated for restrictions, which every smooth field on S³ is.
- `σ`'s full support is needed for step 4 and is built here (an open subset of S³ has positive measure).

***Failable:*** BUILT (T★ as stated), BUILT IN PART (per step), or REPORTED. p `0.35`. ***Risks:***
- the complex `L²` bridge;
- full support of `toSphere`;
- matching three files' conventions (P1's `nabP` with P2's `nab`; P3's real frame with the complex one).

***Census if BUILT:*** rows 65 and 66 → `DONE`; the census reaches `111` DONE.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
