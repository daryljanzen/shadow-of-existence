# `r7443+71.62` — PRE-REGISTRATION: campaign 53, programme stage P2 — the polynomial spectrum of `∇²` on symmetric traceless tensor fields on S³. ⌗ `1600` lines (band 800–3000), ⛔ stop `4000`. ⌗ p `0.30`

*The second stage of `r7443_71_pw_programme/PROGRAMME.md`. It builds on campaign 51's `probes/S3TTSpectrum.lean`
(the frame derivations `D a` on `ℂ[x₀..x₃]`, the quotient `Q` by the ideal of S³, the two `sl₂` triples, and the TT
eigen-tensors). No Lean was written before this registration.*

## ① The piece: `probes/S3PolySpectrum.lean`

Let `Pd` be the symmetric traceless tensor fields whose components are polynomials of degree `≤ d`, taken in `Q`,
i.e. restricted to S³.
1. ***Finite and invariant.*** `Pd` is finite-dimensional. `∇²`, the divergence and the two `sl₂` actions all
   preserve it (frame fields preserve degree).
2. ***`∇²` through Casimirs.*** On tensor fields, `−∇²` is an explicit combination of the right-invariant `sl₂`
   Casimir and the frame `sl₂` acting on components and indices. So its eigenvalues on `Pd` are the corresponding
   Casimir values.
3. ***The degree bound.*** A `−∇²`-eigenvector at eigenvalue `λ` lies in `P_{D(λ)}` for an explicit `D(λ)`. That is,
   eigenvectors at a fixed `λ` cannot have growing degree. This is the key input to P4.
4. ***The count.***
   - The eigenvalues of `−∇²` on the TT tensors in `Pd` are exactly `{m² − 3 : 3 ≤ m}` (for `d` large enough).
   - The TT eigenspace at `m² − 3` has dimension ***exactly*** `2(m² − 4)` over ℂ.
   - It also has dimension `2(m² − 4)` over ℝ, for real-coefficient tensors. That closes campaign 51's real-from-complex
     caveat.
   - It is spanned by campaign 51's eigen-tensors.

***Route.*** Harmonic decomposition of `ℂ[x₀..x₃]` restricted to S³ into spaces `H_N` of dimension `(N+1)²`, as
`V_{N/2} ⊗ V_{N/2}` under the two `sl₂`s. Tensor with the 5-dimensional symmetric traceless index space (spin 2
under the frame `sl₂`). Then Clebsch–Gordan for `sl₂`, done concretely: weight counting under the Cartan elements,
plus the `HasPrimitiveVectorWith` API. The count follows from weights.

***Failable:*** BUILT, BUILT IN PART (per item: the degree bound 3 is the one P4 needs, and the count 4 is the one
the rows need), or REPORTED. p `0.30`. ***Risk:*** Clebsch–Gordan and the harmonic decomposition are not in Mathlib
and are built here; the upper-bound direction of the count is the hard part.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
