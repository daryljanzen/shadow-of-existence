# `r7443+71.32` — PRE-REGISTRATION: campaign 44, library-gap row 89 (the constituent count is conserved on every static member and the twist alone violates it). ⌗ `1800` lines (band 1100–2600), ⛔ stop `3200`. ⌗ p `0.30`

*Under `r7443` ②, step 4, and `r7453` ③: the last row of structure I in `r7453_71_gap_class/CLASS.md`. The receipt is
`receipts/P14_matter_sector_paper/P14_the_constituent_count_is_conserved_on_every_static_member_and_the_twist_alone_violates_it.py`.
No Lean was written before this registration.*

## ① The piece: `probes/Row89Pontryagin.lean`

The receipt's computed parts, as `PRICING.md` §1 lists them. It is built on the engine, row 69's Pontryagin core,
row 96's parity framework (`pontryagin_parity`, `warped_pontryagin`) and campaign 43's `transgression`, all copied
because probes cannot import probes.

- ***Part 1, Kerr.***
  - In Boyer–Lindquist with `u = cos θ` at `M = 1`: `*RR(0) = 0`, `*RR(1/2) ≠ 0`, `*RR(a) + *RR(−a) = 0`.
  - The closed form `−96M²a r u(3r² − a²u²)(r² − 3a²u²)/(r² + a²u²)⁶`, at least at the receipt's three values of
    `a`.
  - `= −48 Im Ψ₂²` with `Ψ₂ = −M/(r − iau)³`.
- ***Part 2.*** U(3) determinant-circle charges from the generator's eigenvalues: `Λ³ → 3`, `Λ² → 2`,
  `V⊗V̄ → 0`, `V → 1`, trivial `→ 0`.
- ***Part 3.*** The linear traces `3, 0, 1`, including the convention sign flip.
- ***Part 4.***
  - `D(gΨ) − gDΨ = g′Ψ`;
  - the Clifford relation for explicit Dirac matrices;
  - the Dirac equation fixing `∂₀Ψ`;
  - `∂_μ(Ψ̄γ^μΨ) = 0` on shell and `≠ 0` off shell;
  - `j⁰ = Σ|Ψ_i|²`.
- ***Part 5.*** `*RR ≡ 0` for:
  - `diag(−f, 1/f, r², r² sin²θ)`;
  - `diag(−f, h, S², S² sin²θ)`;
  - the static Weyl form;
  - the named instances.

  All of these come structurally from the parity lemma with `k = t`, for arbitrary profiles.
- ***Part 6.*** General unpolarised Gowdy (A, ψ, ω, R arbitrary of `(t,z)`):
  - `*RR(−ω) = −*RR(ω)` by a sign-twist lemma;
  - `*RR = 0` at constant ω;
  - the explicit member `(t/3, z/5, ctz, t)` nonzero, odd in `c`, zero at `c = 0`.
- ***Part 8.*** `∂_μK^μ/(√−g *RR) = −1` on the member, as a corollary of campaign 43's `ratio_neg_one`; `∂K` odd in
  `c`.

***Caveats, registered.***
- "Only the powers {1, 3} of ε" and "every monomial in ω's derivatives has odd degree" (Part 6) need the explicit
  four-function expansion. They are ***priced out***: oddness is proved structurally, and the degree bound is
  reported as not built unless it comes cheaply.
- Kerr's closed form for symbolic `a` may be reduced to the receipt's three values if `field_simp; ring` times out.
- ***Imported:*** the anomaly normalisation `1/384π²` and the representation semantics (physics). Paper-text checks
  (Part 7) are not formalised.

***Failable:***
- BUILT: Parts 1–6 and 8, with the two Part 6 caveats above allowed.
- BUILT IN PART: per part. Kerr is the likeliest gap.
- REPORTED.

p `0.30`. ***Risk:*** Kerr's Riemann tables in `(r, u)` as rational functions of degree about 20.

***Census if BUILT:*** row 89 → `DONE`, imports named, `decl` filled.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
