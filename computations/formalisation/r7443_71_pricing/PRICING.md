# `r7443+71.10` — PRICING: step 4, the seventeen `LIBRARY GAP` rows, under the instrument rule, before any foundation is built

*Under `r7443` ②, step 4: "each as a from-scratch foundation SIZED TO WHAT THE ROWS NEED and not a general library.
Priced first under the instrument rule, then built."* Each receipt was read for what it COMPUTES, as distinct from
what it imports and from its paper-text pins. No Lean was written for this pricing. The line counts below are
estimates, not registrations; each build will be registered on its own.

***The headline, verified against the tree before writing.***
- ***Most of the seventeen need none of the library their gap names.*** The nine spectral rows all take the TT
  spectrum on `S³` as input, and none does spectral theory. The three spinor rows need no spin geometry. Row 80 needs
  no homogeneous space. Row 46 needs no volume form.
- ***Two are already built or nearly built.***
  - Row 23's receipt (`L818_po6_running_layer/S1`) is the receipt row 19's campaign 12 formalised in
    `probes/RunningLayer.lean`.
  - Row 24's Weyl² is `probes/BianchiI.lean`'s `row1_shear`, on the receipt's own family.
- ***Only rows 69, 89 and 96 need a genuinely new core***: the ε-contracted Pontryagin density and the Chern–Simons
  current, on the non-diagonal engine.

***The order, easiest first:*** 23, 24, 82, 46, 84, 85, 80, 64, 68, 73, 63, 57, 69, 70, 96, 89, 60.

---

# Pricing the 17 LIBRARY-GAP rows: what each receipt computes, and the smallest foundation that reproduces it

*Read-only survey of `computations/formalisation/r7325_71_inventory/ROWS.tsv` (the rows with status `LIBRARY GAP`).
I read each row's receipt and set it against the existing Lean: `ShadowEngine.lean`, `probes/NonDiag.lean`,
`Bianchi2.lean`, `S3Frame.lean`, `Row59Series.lean`, `Row62Jet.lean`, and also `BianchiI.lean`, `RunningLayer.lean`
and `FRWk.lean`, which turned out to matter. Nothing was built. The line counts are estimates.*

Size bands: **S** = under 150 lines, **M** = 150–500, **L** = 500–1500, **XL** = over 1500.

Axiom policy: `check_no_sorry.py` accepts only `{propext, Classical.choice, Quot.sound}`, so `native_decide`
(`Lean.ofReduceBool`) is not allowed. The repo has no `native_decide` anywhere. Every finite computation below must
therefore go through `decide`, `simp`, `norm_num` or `ring`, or through a precomputed table proved layer by layer, as
`NonDiag.lean` and `Row62Jet.lean` already do. For the large finite checks (rows 60, 80, 68 and 70) this is the main
practical risk.

---

## 0. Headline findings

1. **None of the nine "spectral theory" rows does any spectral theory.** Every one takes the TT spectrum on `S³` as
   given input: frequency `μ² = m² − 1` (or `λ = m² − 3`) and degeneracy `d = 2(m² − 4)`. Rows 23 and 24 take the
   one-loop `b₄` coefficients ('t Hooft–Veltman and Gilkey: 53/90, 7/20, 1/120) as given input. What the receipts
   actually compute is FRW/Bianchi curvature algebra, rational ranks, asymptotics at `m → ∞`, Faulhaber and harmonic
   sums, Riemann-ζ special values and the residue at 1, truncated-oscillator (Fock) matrix algebra, and the
   contraction of maximally symmetric curvature tensors.
2. **Row 23 is already built.** `probes/RunningLayer.lean` (campaign 12, which closed row 19's running-layer half)
   formalises *the same receipt*, `L818…/S1`, items 1–5: `frw_invariants`, `tv_identity`, `ledger_general`,
   `ledger_layer` and `ledger_ds_point`, with the engine's `frw_weyl`, `frw_scal`, `layer_scal` and `layer_late`.
   Only item 6 is left, and it is a paper-string check.
3. **Row 24 is nearly built.** `probes/BianchiI.lean`'s `row1_shear` gives `Weyl² = 12σ²(H − 2σ)²` on exactly the
   receipt's family `A = e^{(H−2s)t}, B = e^{(H+s)t}`. That covers the "zero at s = 0, no linear term, nonzero s²"
   checks. The `b₄` re-basing is rational arithmetic.
4. **Row 46 needs no volume form.** Its "areas" are the literal formulas `4πr²` and `16πM²`. What it computes is
   polynomial algebra on `f = 1 − 2M/r − r²/α²`.
5. **The three spinor rows need no spinors.** Rows 82 and 84 take the Dirac spectrum `±(n/2 + k)/a` as a
   *definition* and do rational and decimal arithmetic. Row 85 checks that a tetrad is orthonormal and evaluates
   `W = λ√f/r` at points. Its spin connection is derived by hand in comments: the helper `d()` is defined but never
   called.
6. **Row 80 needs no homogeneous space.** It is a finite Lie-algebra computation: the Killing form of `so(5,1)`
   restricted to the span of `M_{a5}`.
7. **Only the Levi-Civita rows 69, 89 and 96 need a real new mathematical core.** That core is the ε-contracted
   Pontryagin density and the gravitational Chern–Simons current on top of the existing non-diagonal engine
   (`formG`/`curvG`). Row 89 also does a Kerr computation that could be very large.
8. The rows with a genuinely out-of-reach piece are listed in §3. The two that bite are row 63's 40-digit quadrature
   with SVD, which needs verified numerics, and row 68's level-summed density for general `m`, which needs the TT
   harmonics and Schur's lemma on `S³`. Neither is needed for the rest of those rows.

---

## 1. Per-row analysis

Each row lists (a) what the receipt **computes**, what it **imports**, and its **paper-text** checks; (b) the
minimal foundation; (c) a size and the main risk; (d) what is beyond reach.

### Foundation 1: the Levi-Civita volume form (rows 46, 69, 89, 96)

#### Row 46: `P07_the_double_root_removes_the_first_law…`
- **(a) Computed:**
  - **Part 1:** the photon sphere from `d/dr(f/r²) = 0`, which gives exactly `[3M]` and contains no `α`. At Nariai,
    `M_N = √3α/9` and `r_N = α/√3`, so `3M_N = r_N`. `f(r_N) = 0` and `f′(r_N) = 0`. The quantity
    `λ² = f(2f − r²f″)/(2r²)` vanishes at Nariai.
  - **Part 2:** `A_coll = 16πM²` and `A_cos = 4πα²` are equal only at `M = α/2`, which differs from `M_N`.
    `A_seam = 4πr_N² = 4πα²/3`, and its ratio to `A_cos` is 1/3.
  - **Parts 3–4:** `S = A/(4ℓ_P²)` with `α = √(3/Λ)`. The ratios to `8π/(Λℓ_P²)` are 3/8 and 1/8. `S_coll` depends
    on `M` and `S_sub` does not.
- **Imported:**
  - the area formulas `4πr²` (there is no integral);
  - the Lyapunov formula;
  - `S = A/4`.
- **Paper text:** `pf.rhs(_GC, 'eq:ds-entropy', …)` parses the ledger's entropy from `geometric_core_paper.tex`.
  That check is a parse, not mathematics, though the comparison against it is algebra.
- **(b) Minimal foundation:**
  - real field algebra (`field_simp`, `ring`, `nlinarith`);
  - one derivative (`HasDerivAt` of `f/r²`);
  - "the only positive root is `3M`" (`f/r²` has derivative `(6M − 2r)/r⁴`);
  - `Real.sq_sqrt` for the `√3` facts.
  - No volume form. The existing `ShadowFormal.Nariai` (`nariai_double_root`) already covers the double root.
- **(c) S** (about 80–120 lines). Low risk. The ledger value would be typed in as a constant, which loses the "parsed
  from the paper" property. That is a provenance check, not mathematics.
- **(d)** If "area" is to mean an integral, it needs the induced area form on the horizon `S²`. Mathlib's
  `Measure.toSphere` and the sphere's surface area would do that in about 150–300 lines. The receipt never does
  this, so it is not needed.

#### Row 69: `P10_the_parity_odd_density_goes_with_the_relative_phase…`
- **(a) Computed:** the receipt `exec`s `pontryagin` from row 89's receipt and `gowdy` from row 96's.
  - The Gowdy form is `g = e^{2A}(−dt² + dz²) + e^{2ψ}(dx + ω dy)² + R²e^{−2ψ}dy²`, with `A = 0`, `ψ = ψ(t−z)` and
    `ω = ω(t−z)` arbitrary.
  - With `R = 1`, `*RR = 0`.
  - With `R = t`, `*RR ≠ 0`.
  - Rebuilding the metric with ω constant, or with ψ constant, gives `*RR = 0`.
  - With `R = t`, `*RR/(ψ′ω′) = −8e^{2ψ}/(t²|t|)`. No derivative of either channel is left and no ω is left.
  - The cycle average `⟨ψ′ω′⟩` with `ψ = ε sin(ku)` and `ω = ε sin(ku + δ)` is `(k²ε²/2)cos δ`. It takes the values
    0 at δ = π/2 and ±k²ε²/2 at 0 and π. The reflection ω → −ω equals δ → δ + π and flips the sign.
- **Imported:** nothing mathematical. There are no paper-text checks.
- **(b) Minimal foundation:**
  - **Fin-4 Levi-Civita symbol:** `ε σ = Equiv.Perm.sign σ` summed over `Equiv.Perm (Fin 4)` (24 terms), or an
    explicit 24-entry table.
  - **Pontryagin density** `*RR = ½ ε^{mnrs} R_{mnab} R_{rs}{}^{ab} / √−g`, defined on `NonDiag`'s
    `curvG`/`formG`/`Gi`, with index lowering and raising and `√−det g` (here `e^{2A}|R|`).
  - **The instance:** the plane-wave Gowdy metric with free profiles ψ, ω : ℝ → ℝ. There is precedent: `NonDiag`'s
    `GE (F P S : ℝ → ℝ)` and `ef_kretschmann` already carry free profile functions. Use sympy-generated tables
    (D1, D2, Γ, R) proved layer by layer.
  - **The cycle average:** `intervalIntegral` of a trigonometric product, via product-to-sum and `integral_cos`.
- **(c) M** (about 300–450 lines) once the Pontryagin core exists. The core itself is priced under §2.1. Main risk:
  the table size for a non-diagonal 4×4 metric with `e^{2ψ(t−z)}`, `ω(t−z)` and `R = t`, though only two
  coordinates are live. The `|t|` in `√−g` needs a sign hypothesis (`t > 0`).
- **(d) Nothing.**

#### Row 89: `P14_the_constituent_count_is_conserved…` (the machinery's home receipt)
- **(a) Computed:**
  - **Part 1:** Kerr in Boyer–Lindquist with `u = cos θ` (a rational metric) at `M = 1`, `a = 1/2, −1/2, 0`.
    `*RR(0) = 0`, `*RR(1/2) ≠ 0`, and `*RR(a) + *RR(−a) = 0`. Each of the three equals the closed form
    `−96M²a r u(3r² − a²u²)(r² − 3a²u²)/(r² + a²u²)⁶`. The closed form is `−48·Im Ψ₂²` with
    `Ψ₂ = −M/(r − iau)³`, and is odd in symbolic `a`.
  - **Part 2:** U(3) determinant-circle charges, read off the generator's eigenvalues. Λ³ has charge 3, Λ² (2×2
    minors) has 2, V⊗V̄ has 0, V has 1, and the trivial representation has 0.
  - **Part 3:** linear traces 3, 0 and 1, including the convention sign flip.
  - **Part 4:**
    - `D(gΨ) − gDΨ = g′Ψ` for non-constant g, and 0 for a constant phase;
    - explicit Dirac matrices (Dirac basis, η = diag(1,−1,−1,−1)) satisfy the Clifford relation;
    - for a free complex 4-spinor with 8 real symbols and free spatial derivatives, the time derivative is fixed by
      the Dirac equation;
    - on shell `∂_μ(Ψ̄γ^μΨ) = 0`; off shell it is nonzero;
    - `j⁰ = Σ|Ψ_i|²`.
  - **Part 5:** `*RR ≡ 0` for:
    - `diag(−f, 1/f, r², r²sin²θ)` with f arbitrary;
    - `diag(−f, h, S², S²sin²θ)` with f, h, S arbitrary;
    - the static Weyl form with U(r,θ), K(r,θ) arbitrary;
    - the named instances Schwarzschild, SdS, dS and Nariai.
  - **Part 6:** general unpolarised Gowdy with A, ψ, ω, R arbitrary functions of (t,z).
    - `*RR ≠ 0`.
    - Under ω → εω only the powers {1, 3} of ε appear.
    - Bare ω never appears, and every monomial in ω's derivatives has odd degree.
    - `*RR(−ω) = −*RR(ω)`, and `*RR = 0` at constant ω.
    - The explicit member `(t/3, z/5, ctz, t)` gives a nonzero value, odd in c and zero at c = 0.
  - **Part 8:** the Chern–Simons current `K^μ = 2ε^{μνρσ}(Γ∂Γ + ⅔ΓΓΓ)` on the explicit member.
    `∂_μK^μ / (√−g *RR) = −1` as a constant ratio, and `∂K` is odd in c.
- **Imported:**
  - the anomaly prefactor `1/384π²` (stated as not computed);
  - "seats" and representation semantics (physics).
- **Paper text (Part 7):**
  - a regex count of `Chern–Simons` across the corpus `.tex` files (it must be 0);
  - the strings "the ledger counts no counterterm coefficient" and "A topological term's coefficient is of the third
    kind";
  - three substring checks on r6752's receipt.
- **(b) Minimal foundation:**
  - the Pontryagin core above, plus the CS current;
  - a **parity lemma**: if `g` is block-diagonal with respect to one coordinate index `k` (`g_{kj} = 0` for `j ≠ k`)
    and `∂_k g = 0`, then every `R_{abcd}` with an odd number of `k`'s vanishes, and so does every `Γ` with an odd
    number of `k`'s. Hence `*RR = 0`, because ε forces exactly one `k`. With `k = t` this covers **all of Part 5 at
    once**, for arbitrary profiles, in place of three brute-force tables;
  - a **sign-twist (reflection-covariance) lemma**: if `g′_{ij}(x) = s_i s_j g_{ij}(Sx)` with `S` a diagonal ±1 map,
    then `R′` is twisted by `Π s` and `*RR′(x) = (Π s_i)·*RR(Sx)`. With `y → −y` (which takes ω to −ω) this gives
    `*RR(−ω) = −*RR(ω)` for arbitrary A, ψ, ω and R. That is the content of "odd in the twist", without expanding;
  - a **transgression identity**, `√−g *RR = −∂_μK^μ`, proved once for any torsion-free connection. It is a
    polynomial identity in (Γ, ∂Γ, ∂²Γ) with Schwarz symmetry, which is the `Bianchi2.lean` style. The receipt's
    measured ratio of −1 then becomes a corollary instead of a computation on one member;
  - **Kerr:** a rational metric in (r,u) with `a ∈ {±1/2, 0}`, through `formG`/`curvG` tables and
    `field_simp; ring`;
  - **Parts 2–4:** `Matrix (Fin 3)` determinant and minors, Kronecker products, eigenvalues of diagonal generators,
    and `Matrix (Fin 4) (Fin 4) ℂ` Clifford products (`decide` or `simp` with `fin_cases`). The current conservation
    is a `ring` identity over 32 real variables and m.
- **(c) XL** (about 1500–2500 lines including Kerr; about 900–1300 without it). Main risks:
  1. Kerr's Riemann tables in BL coordinates are large rational functions in (r,u). `field_simp; ring` at degree
     around 20 can time out. This is the single biggest risk in the Levi-Civita foundation. Mitigation: the type-D
     route (Ψ₂) is only an algebraic identity, but it still needs the curvature to connect to it.
  2. "Exactly the powers {1, 3}" and "every monomial has odd degree" need the *explicit* expansion of the general
     four-function Gowdy density. The sign-twist lemma proves oddness but not the bound "degree ≤ 3". A brute-force
     table over four arbitrary functions of two variables (up to second mixed derivatives) is XL by itself.
     Recommendation: prove oddness and the polarised zero structurally, and price "powers exactly {1, 3}" separately
     or drop it.
  3. Orientation and sign conventions in ε against sympy's `Matrix.det` permutation sign.
- **(d) Beyond reach:** nothing mathematical. The normalisation `1/384π²` of the mixed anomaly is a QFT result,
  imported. The receipt says so.

#### Row 96: `P15_the_history_is_spherically_symmetric…`
- **(a) Computed:**
  - **Part 1:** Nariai `dS₂×S²`, `diag(−L(1−χ²), L/(1−χ²), L, L sin²θ)` with `L = α²/3`, has `*RR = 0`. With a
    `dτdφ` rotation term `ω₀L sin²θ` (non-diagonal) it is still 0.
  - **Part 2:**
    - polarised Gowdy (ω = 0; A, ψ, R arbitrary functions of t,z): 0;
    - unpolarised: nonzero;
    - plane wave with R = 1: 0;
    - plane wave with R = t: nonzero;
    - silencing either channel: 0. These are row 69's facts again.
  - **Part 3, Stokes:** the member `gowdy(0, log(t−z), t−z, t)`.
    - `∂K/(√−g *RR) = −1`.
    - The volume integral of `√−g *RR` over `[3,5]×[0,1]` equals minus the boundary flux of `(K^t, K^z)`, exactly,
      and is nonzero.
  - **Part 4:** the general dynamic spherically symmetric metric (A, B, C, S arbitrary functions of (t,r), including
    a `dt dr` cross term) has `*RR ≡ 0`, and **all four** `K^μ ≡ 0`.
  - **Part 6:** `3 × 0 = 0`.
- **Imported:** none.
- **Paper text (7 checks):** P16 strings ("…is a premise of the construction…", "one may not drop the symmetry…",
  count('twist') = 0, count('Gowdy') = 0), P11 'torus block', P15 'closed $S^3$' plus P16's 'tensor tower starts at
  $L=2$', a P10 string and a P14 string.
- **(b) Minimal foundation:**
  - the same core;
  - the **parity lemma with k = φ**, which gives `*RR ≡ 0` on the general spherical class and the zero in the polarised
    Gowdy cut (k = x or y);
  - **`K^μ ≡ 0`**: the parity lemma kills `K^t`, `K^r` and `K^θ`. A term with ν or σ = φ has odd φ-count in the Γ
    chain, and the term with ρ = φ dies under ∂_φ. **`K^φ` is not killed by φ-parity.** It needs a second structural
    argument (the warped (t,r)×S² block structure) or a brute-force table with four arbitrary functions of (t,r);
  - **Stokes:** Mathlib's `integral2_divergence_prod_of_hasFDerivAt_off_countable` on the rectangle, plus the
    transgression identity. The receipt's "exact agreement" then follows from the theorem. Producing the receipt's
    *closed-form value* additionally needs explicit `K^t`, `K^z` and FTC on functions built from `log(t−z)`;
  - **Nariai** (both forms): small tables. The rotated one is non-diagonal.
- **(c) L** (about 600–1000 lines on the shared core). Main risk: `K^φ ≡ 0` for the general class. The CS current is
  cubic in Γ and not covariant, so no tensor-parity shortcut is known for it, and brute force means large tables.
- **(d) Nothing.** The paper-string checks are not mathematics.

### Foundation 2: homogeneous spaces G/H (row 80)

#### Row 80: `P12_coset_metric.py`
- **(a) Computed:**
  - the 15 generators `M_{μν}` of so(5,1) as 6×6 integer matrices, `(M)_{ρσ} = δ_{ρμ}η_{νσ} − δ_{ρν}η_{μσ}`;
  - the structure constants, by coefficient extraction from commutators;
  - the 15×15 `ad` matrices, and `B_{ij} = tr(ad_i ad_j)`;
  - `B` restricted to `m = span{M_{a5}}`: the off-diagonal entries are 0, `B|_m = diag(8, −8, −8, −8, −8)`, the
    constant of proportionality to `η_{ab}` is −8, the signature counts are (1,4), and `B(M₀₅,M₀₅)` and
    `B(M₁₅,M₁₅)` have opposite signs.
- **Imported:** the reading that "B|_m is the coset metric of SO(5,1)/SO(4,1) = dS₅ and the structure function of
  eq:HH". That is interpretation; no G/H is constructed.
- **(b) Minimal foundation:**
  - `Matrix (Fin 6) (Fin 6) ℤ` generators;
  - either (i) the Killing form computed directly as `tr(ad X ∘ ad Y)` on the 15-dimensional span (needs a
    basis-coefficient map), or (ii) the cheaper identity `B(X,Y) = (n−2)·tr(XY)` for so(p,q) with n = 6. Route (ii)
    itself needs the 15-dimensional computation once to be honest. Better: compute `ad_X` on the basis by explicit
    commutator expansion and take the trace;
  - optionally, tie to Mathlib's `LieAlgebra.killingForm` on `LieAlgebra.Orthogonal.so'`. That is extra cost and not
    needed.
- **(c) M** (about 150–350 lines). Main risk: kernel and elaboration time for 15×15×15 integer sums without
  `native_decide`. Mitigation: only the 5×5 block on m is needed, which takes 25 traces of 15×15 products, each
  simp-able. Coefficient extraction in Lean needs a basis and a coordinate function, which is easy for the `M_{μν}`
  (read off entry (μ,ν)).
- **(d) Beyond reach:** the actual homogeneous space. A smooth quotient `SO(5,1)/SO(4,1)` with its G-invariant
  metric, and its identification with dS₅, is not in Mathlib (there is no Riemannian structure on Lie-group
  quotients). A from-scratch version would have to *assume* that the invariant metric on G/H at the base point is
  `B|_m`, which is exactly the receipt's reading. None of this is needed for the computed checks.

### Foundation 3: spinors and the Dirac operator (rows 82, 84, 85)

#### Row 82: `P13_the_compact_face_is_odd_dimensional.py`
- **(a) Computed:** with `R(n) = n(n−1)/a²`, `λ(n,k) = (n/2 + k)/a` (a *definition* in the file) and the Friedrich
  bound `nR/(4(n−1))`:
  - for n = 4 and 5, `λ_min² = bound`, i.e. saturation;
  - `λ_min(5) = 5/(2a) > 0`, and no k ≥ 0 solves `n/2 + k = 0`;
  - `R(5)/4 = 5/a²`;
  - `5 % 2 = 1`.
- **Imported:**
  - the Dirac spectrum on round Sⁿ;
  - the Friedrich bound;
  - Lichnerowicz;
  - the Atiyah–Hirzebruch theorem (prose).
- **(b) Minimal foundation:** `field_simp; ring` and `positivity`, with the spectrum as an explicitly labelled
  definition. If wanted, `R(n) = n(n−1)/a²` for the round sphere could be tied to the engine (`HigherDim`/Tangherlini
  probes exist), but the receipt types it in.
- **(c) S** (about 40–80 lines). No risk.
- **(d) Beyond reach:** the spectrum `±(n/2 + k)/a` itself. A from-scratch version needs the spinor bundle on Sⁿ, the
  Clifford module, the Dirac operator, and its eigen-decomposition (Killing spinors or representation theory of
  Spin(n+1)). Lichnerowicz/Friedrich and Atiyah–Hirzebruch are further index-theory layers. This is far beyond the
  current scale (≫ 5000 lines, with no Mathlib support for spin structures) and is *not used* by any computed check.

#### Row 84: `P13_the_one_scale_forbids_the_isometry_route.py`
- **(a) Computed:**
  - `α = √(3/Λ)` and `R = n(n−1)/α² = 20Λ/3`;
  - `λ_min = (5/2)/α = (5/2)√Λ/√3`;
  - **floating-point physics:** `α = c/(H₀√Ω_Λ)` with H₀ = 73 km/s/Mpc and Ω_Λ = 0.7, `m_min = 2.5ħc/α`, then
    `m_min < 10⁻³⁰ eV` and `m_e/m_min > 10³⁰`.
- **Imported:** the Dirac spectrum, the CODATA-style constants, and the physical reading.
- **(b) Minimal foundation:** real algebra with `Real.sqrt` (`Real.sqrt_div` and `sq_sqrt`). The decimal claims
  become exact rational inequalities. The only non-rational step is `√0.7`, which needs a bound such as
  `0.83 < √0.7 < 0.84` via `Real.lt_sqrt`/`Real.sqrt_lt'`.
- **(c) S** (about 50–100 lines). Low risk.
- **(d) Same spectrum caveat as row 82.** "Eigenvalue ≠ mass" is physics, not mathematics.

#### Row 85: `P14_B3_spinor_vielbein.py`
- **(a) Computed:**
  - **(0)** `η_{ab}e^a_μ e^b_ν = diag(−f, 1/f, r², r²sin²θ)` for the tetrad `(√f dt, dr/√f, r dθ, r sinθ dφ)`, with
    `f = 1 − 2M/r − r²/α²`;
  - **(1)** `W − λ√f/r = 0`, which is definitional, as the receipt itself says;
  - **(2)** `√f/r = 1.0392305` at r = 1/2, with M = 0.12 and α = 1;
  - **(3)** `|f(r_h)| < 10⁻⁹` and `|W(r_h)| < 10⁻⁴` at the two decimal horizon roots 0.2569683156 and 0.8464391538;
  - **(4)** `W(−1/2) = −2.2181073 < 0`;
  - **(5)** `|√f/r| > 10³` at r = 1/1000.
- **Not computed:** the spin connection. `ω²₁ = (√f/r)e²` is solved by hand in comments, and the helper `d()` is never
  called.
- **Imported:** that the massless radial Dirac operator separates with angular eigenvalue `λ = j + ½` and
  superpotential `λ·ω²₁`.
- **(b) Minimal foundation:**
  - **(0)** `Real.sq_sqrt` under `f > 0` (or `f ≠ 0`), then `field_simp`, over `Fin 4` matrices;
  - **(2)–(5)** exact rational evaluation of f at decimals, plus square-root bounds;
  - **optional, for honesty, M:** derive `ω^a{}_{bμ} = e^a_ν(∂_μE_b^ν + Γ^ν_{μλ}E_b^λ)` from the engine's diagonal
    Christoffels for SdS (the existing `diag4Metric` and the SdS instances), and show `ω^{2}{}_{1θ} = √f`. That would
    make the "derived frame" claim true. No spinors are needed.
- **(c) S–M** (about 100–150 lines as the receipt stands; about 250–400 with the frame connection derived). Main
  risk is a **fidelity trap in check (5)**. At r = 0.001, f is about −239 < 0. sympy's `sqrt` is then imaginary and
  `abs(complex(…)) ≈ 1.5×10⁴`, but Lean's `Real.sqrt(−239) = 0`, so a literal transcription *fails*. The check needs
  `Complex.sqrt`/`Complex.abs`, or `√|f|`. It also means the receipt's "W unbounded at the throat" is evaluated where
  the tetrad is not real. Check (3)'s `|f(r_h)| < 10⁻⁹` is fine.
- **(d) Beyond reach:** the Dirac operator on SdS, its separation, and the spinor monopole harmonics (`λ = j + ½`).
  This is the same spin-geometry gap as rows 82 and 84 and is imported. The computed checks need none of it.

### Foundation 4: spectral theory (rows 23, 24, 57, 60, 63, 64, 68, 70, 73)

#### Row 23: `L818_po6_running_layer/S1`
- **(a) Computed:**
  1. `R(T)` for `a = sinh^{2/3}(3T/2α)`: dR/dT ≠ 0 and R → 12/α². The FRW invariants are typed in terms of
     (H, Ḣ), and Weyl² = 0.
  2. `E_GB` is identical to its definition.
  3. `(7/20)Ric² + (1/120)R² = E_{mn}f^{mn}`.
  4. The general `a₁Riem² + a₂Ric² + a₃R²` minus a 7-parameter model is solved by `sp.solve` with remainder 0.
  5. At Ḣ = 0 and H² = Λ/3: R = 4Λ and tr E = 0.
- **Imported:** the `b₄` coefficients 53/90, 7/20 and 1/120.
- **Paper text:** check 6 (strings from the S50 receipt and from canonical_time.tex).
- **(b) Already built.** `probes/RunningLayer.lean` (`frw_invariants`, `tv_identity`, `ledger_general`,
  `ledger_layer`, `ledger_ds_point`) and the engine (`frw_weyl`, `frw_scal`, `layer_scal`, `layer_late`) prove items
  1–5 under THE connection. `RunningLayer`'s own docstring names this receipt.
- **(c) S** (about 0–30 lines: a re-pointing note, or a wrapper theorem stating the five checks together). No risk.
- **(d)** Deriving the `b₄` coefficients from scratch (a heat-kernel `a₂` for the graviton operator with ghosts) would
  be XL, around 3000 lines or more. It is never needed, because the reduction is coefficient-independent and the
  receipt says so.

#### Row 24: `L819_shear_boundary_coupling/S1`
- **(a) Computed:**
  1. With `Ric² = ½W − ½GB + ⅓R²`, `b₄ = (7/40)W + (149/360)GB + (1/8)R²`, as rational coefficients.
  2. `4ΛR − R·E_tr − R² = 0` with `E_tr = −R + 4Λ`.
  3. Weyl² of `diag(−1, A², B², B²)` from an independent Christoffel/Riemann computation, then
     `A = e^{(H−2s)t}` and `B = e^{(H+s)t}`. It is 0 at s = 0, the s¹ coefficient is 0, and the s² coefficient is
     nonzero.
  4. The coefficient 7/40, restated.
- **Imported:** the `b₄` coefficients.
- **(b) Minimal foundation:** `BianchiI.lean`'s `row1_shear`, which proves `Weyl² = 12σ²(H − 2σ)²` on
  `p = (H − 2σ, H + σ, H + σ)`, the same family. Then `ring`/`linear_combination` for (1) and (2), and the coefficient
  extraction of the polynomial `12H²σ² − 48Hσ³ + 48σ⁴` for (3). "s² coefficient ≠ 0" needs `H ≠ 0`, which the
  receipt leaves implicit in symbolic `!= 0`.
- **(c) S** (about 40–80 lines). No risk.
- **(d)** As row 23: the `b₄` derivation is imported, and not needed.

#### Row 57: `P10_second_order_is_an_order_the_construction_does_not_reach…`
- **(a) Computed (23 checks):**
  - **A1:** `α cosh(T/α)` has its single stationary point at T = 0 with second derivative 1/α. The parameter
    `ℓ²/a²` there equals `ℓ²Λ/3`.
  - **A2:** mpmath decimals: `ε_max = 1.1056e−52 · 2.6121e−70 / 3 < 10⁻¹²²`, and `ε_max²` lies in
    `(10⁻²⁴⁶, 10⁻²⁴⁴)`.
  - **A3:** a sectional-curvature model with `F = Λ/3 + εu/3 + extra − 1/a²` and `u = (1 + ν log a)/a⁴`. The
    invariants are `R³`, `R·Ric²`, `R·Riem²`, `trRic³` and `trRm³`, written in K₁ and K₂ (these formulas are typed
    in). A source `σε²/a⁸` moves every ε² coefficient and no ε¹ coefficient.
  - **B1:** at K₁ = K₂, `∂P/∂K₁ = ∂P/∂K₂` for 5 dimension-six and 4 dimension-eight invariants. The rank of the 5×4
    coefficient matrix is 3, equal to the condition `3c₀ + c₁ − c₂ − 3c₃ = 0`, and K₂³ raises the rank.
  - **B2:** `dK₁ + dK₂ = ν/(6a⁴)` has no log, while `dK₁ − dK₂` has one. The ranks at the sample points a = 1, 3/2,
    …, 7/2 are 1 at order 0, 1 at order 1 and 2 at order 2. The ε² values decompose on `{a⁻⁸, (3 + 6 log a +
    4 log²a)a⁻⁸}`.
  - **Asymptotics:** `2(m²−4)√(m²−1)` as m → ∞ has 1/m coefficient `L = 15/4`.
  - **Harmonic sum:** `Σ_{m=3}^{M}(2m³ − 9m + L/m)`, with the substitution `H_M → log M + γ`, has log coefficient L
    and no M⁵ term.
  - **C:** mpmath probes of `L·h·ζ(1+h)` near h → 0 tend to L, with linear error decay. The trace `ρ − 3p` of
    `L log a/a⁴` is `L/a⁴`. The curvature satisfies `R − 4Λ = εν/a⁴`. For a general L′ the faces move together, and
    the control weight `2(m²−4)·m` has no 1/m term, no harmonic number and no anomaly.
  - **D:** a scaled vertex factor A₆ leaves the ranks unchanged.
- **Imported:**
  - the TT weights `d = 2(m²−4)` and `μ = √(m²−1)`;
  - the FRW sectional-curvature invariant formulas in K₁ and K₂;
  - the measured Λ and ℓ_P².
- **(b) Minimal foundation:**
  - **algebra:** rational functions in (a, ε, ν, log a), with truncated ε-series computed as exact polynomial
    division;
  - **rank and nullspace:** a small toolkit. "Rank = r" means an r×r minor ≠ 0 plus every (r+1)-minor = 0, or an
    exhibited kernel. Sample-point matrices contain `log(3/2)`, `log 2` and so on. Rank-1 claims hold structurally
    (proportional columns). The order-2 rank-2 claim needs one 2×2 minor ≠ 0, i.e. bounds on logs such as
    `Real.log_two_gt_d9`;
  - **asymptotics:** an explicit identity, `2(m²−4)√(m²−1) − (2m³ − 9m + 15/(4m)) = O(m⁻³)`, via a bound on
    `√(1−x)` (Taylor with remainder), or simply the coefficient identity in a formal expansion;
  - **harmonic:** Mathlib's `harmonic` and `Real.tendsto_harmonic_sub_log` (Euler–Mascheroni);
  - **ζ:** Mathlib's `riemannZeta_residue_one`, which replaces the numeric probe with the limit `s·ζ(1+s) → 1`.
- **(c) L** (about 500–800 lines). Main risks: rank proofs for matrices with log entries, and stating "the log
  coefficient after substituting `H_M ≈ log M + γ`" as a genuine limit theorem rather than a formal substitution.
- **(d) Beyond reach:** the TT spectrum on S³, which is imported. The *meromorphic continuation* of the Dirichlet
  series `Σ d(m)μ(m)m⁻ˢ` and its residue at s = 0 could be done as
  `D(s) = 2ζ(s−3) − 9ζ(s−1) + (15/4)ζ(s+1) + (holomorphic for Re s > −2) − (m = 1, 2 terms)`, using Mathlib's
  `riemannZeta` continuation and an analytic-tail lemma. That is L (500–1000 lines) and *not done by the receipt*,
  which only probes `ζ(1+h)`.

#### Row 60: `P10_the_assembly_gives_both_level_sums…`
- **(a) Computed:**
  - **A:** an SO(3)-invariant tensor solver. Candidate structures (products of δ's, or one ε with δ's) are pruned by
    rank over the 3^r components. Linear conditions are imposed (symmetries, tracelessness, transversality, pair
    exchange). The invariant dimensions come out as (1,1,2) at ranks (4,5,6). `A = (deg/5)P` with tr P = 5. The
    trace relation `Σ_a C_{aij,akl} = (λ·deg/5)P_{ijkl}` fixes one of C's two parameters, and the full trace is
    `λ·deg`, independent of the free one.
  - **B, the second-order identity:**
    - the frame-Koszul scalar of `exp(εH)` on S³ (structure constants 2ε), to ε⁴, on 9 random TT jets (h, u, w)
      solved from the linear TT and commutator constraints;
    - a fit of the ε² coefficient to the admissible two-derivative and zero-derivative contractions, validated on 4
      or more held-out jets;
    - the mixed contraction's coefficient is 0;
    - **controls:** for a frame-constant h it is `−2 tr h²`; on the position-dependent harmonic `adjH(0)` it
      integrates over the Euler box to `−16π²`.
  - **C:** 372 admissible quartic contractions, of which 7 are used with the r7032 coefficients
    (−5/48, 1/8, 1/24, 19/192, 7/48, −53/192, 1/8). Level values are sums over 3⁵ index assignments of
    C⊗A + B⊗B + B⊗B, polynomial in (c_C, c_B, λ, deg). Then:
    - the c_B² weight ≠ 0;
    - both remaining weights ≠ 0;
    - with `λ = m² − 3`, `deg = 2(m²−4)` and `c_C = −(m²−4)(m²+5)/35`, the second-order level sum is
      `−¼·deg·μ²` and the fourth-order one is `−(1/120)deg²(5μ² + 4)`;
    - both vanish at m = 2 and are negative for m = 3..59.
  - **D:** the cross-level double sum factorises, and its diagonal equals C. The unweighted Faulhaber sums have
    degrees 5 and 7 with negative leading coefficients.
  - **E:** sign algebra for `2c₄ − g²/μ²` against the rearranged form.
- **Imported:**
  - the spectrum (λ, deg);
  - **the value of c_C**;
  - parity c_B = 0 (r7020);
  - the 7 rational coefficients (r7032, row 62);
  - the A/B/C Wick-tensor ansatz, i.e. that level sums of harmonic products are invariant tensors (homogeneity).
- **(b) Minimal foundation:**
  - **Part B is mostly built already.** `Row62Jet.lean`'s `jet_series` gives the ε⁰..ε⁴ coefficients of the frame
    scalar as explicit polynomials in the 50 jet coordinates, and `frame_constant_closed_form` gives
    `6 − 2p₂ε² − …`, which matches the −2 tr h² control. `Row59Series.lean`'s `section_e_integrals` gives the
    Euler-box integrals, with a −16π² value at ε². The new work for B is the identity
    `scT2 = Σ q2coef·(contractions)` *restricted to the TT constraint variety*: a polynomial identity modulo linear
    constraints, i.e. substitute the solved jet coordinates, then `ring`.
  - **Part A:** an explicit A, B, C (sympy-generated) with componentwise verification of every condition and trace
    relation over `Fin 3`. That gives *sufficiency*. The "dimension exactly (1,1,2) within the candidate span" claim
    needs a rank certificate over a 729-column matrix, which is heavy.
  - **Part C:** the 7 level values as polynomial identities, from sums over `Fin 3`⁵ with tables, then the
    substitution and `ring`. Negativity for every m ≥ 3 can be proved rather than sampled.
  - **D and E:** Faulhaber identities (induction) and sign lemmas.
- **(c) XL** (about 1500–2500 lines; around 900 if Part A is reduced to sufficiency only). Main risks:
  - the elaboration and kernel cost of the 3⁵- and 3⁶-index sums, and of A's rank certificate, without
    `native_decide`;
  - matching the TT jet constraints to `Row62Jet`'s parameterisation;
  - the provenance of the imported c_C, which cannot be checked here.
- **(d) Beyond reach:**
  - **Completeness of the candidate span:** that every SO(3)-invariant tensor is built from δ and ε (the First
    Fundamental Theorem of invariant theory for SO(3)). Not in Mathlib; a from-scratch version would assume it. The
    receipt only searches inside the span, so the Lean version would match the receipt if it states the dimensions
    *within the span*.
  - **That the actual level sums of TT harmonics are these invariant tensors:** this needs the harmonics, the SO(4)
    action and Schur's lemma. It is imported.

#### Row 63: `P10_the_degeneracy_needs_r_constant…`
- **(a) Computed:**
  - **A1:** `R = 6(ä/a + ȧ²/a² + 1/a²)`, and on `α cosh` it equals the parsed `12/α²`.
  - **A2:** the variance identity `I₂I₀ − I₁² = I₀²Var` and its consequences, with a sample gap > 0.
  - **A3:** Λ + radiation (`ȧ² = Λa²/3 + C/a² − 1`) gives R = 4Λ (parsed) with dR/da = 0.
  - **B:** the bare trace Θ = 0 for ρ ∝ a⁻⁴. With ρ_ren = (C + r log(aμ))/(a·2π²a³), `Θ = r/(2π²a⁴)`, independent
    of μ and C, and 0 at r = 0. R from the constraint equals `4Λ + 8πGΘ`, with dR/da ≠ 0 iff r ≠ 0.
  - **C, mpmath at 40 digits:** `∫√g R^k` for k = 0, 1, 2 over three a-regions (quadrature with `1/ȧ`), then SVD.
    Two null controls give rank 1 (floor about 10⁻³⁰). The tower with r = 15/4 gives rank 3. `(s₃/s₁)/r²` is constant
    to 10⁻³ over three decades.
  - **D:** `ζ_Δ(0)` for `λ(m)` with degeneracy `2(m²−4)` by a formal asymptotic rule. The series of
    `d·(λ/m²)^{−s}` in x = 1/m has `B₃(0) = 0` and `B₃′(0)`, and the formula is
    `hd + 2(0 − Σm²) − 8(−½ − Σ1) + B₃′(0)/2`. That uses `ζ(0) = −½`, `ζ(−2) = 0` and the pole of ζ at 1 for j = 3.
    - The free tower gives 10.
    - The shifts `+δ`, `×L`, `+b/m²` and `+b/m⁴` leave 10.
    - `+cm` gives `10 + 3c − c³/3`.
    - `+c/m` gives `10 − c`.
    - The result is independent of M and J.
- **Imported:**
  - the residue r = 15/4 and ζ₀ = 10 ("BANKED");
  - the renormalised-energy form `C + r log(aμ)` (semiclassical);
  - the TT degeneracy and spectrum.
- **Paper text:** `pf.inline` parses `12/\alpha^{2}` and `R=(4\Lambda)` from canonical_time.tex.
- **(b) Minimal foundation:**
  - **A and B:** real algebra and derivatives. The closed-FRW R is the engine's `frw_scal_weyl_k` at k = 1.
  - **D (formal version):** polynomial algebra in s, x and c for the coefficients, plus Mathlib's
    `riemannZeta_zero`, `riemannZeta_neg_two_mul_nat_add_one` and the residue at 1. `S3Frame.zeta_count` already
    proves the free-tower 10 *in exactly this formal sense*: `2((ζ(−2) − 5) − 4(ζ(0) − 2)) = 10`.
  - **D (genuine version):** define `ζ_Δ(s) = Σ_{m≥3} d(m)λ(m)^{−s}` for Re s > 2, prove meromorphic continuation
    near 0, and compute the value at 0 for each perturbation family. This needs the binomial expansion of
    `(1 + u_m)^{−s}` with a remainder uniform in s, analyticity of the tail sum, and shifted ζ's.
- **(c) M** for A, B and formal D (about 250–400 lines). **L** for genuine D (about 700–1200 lines). Risk: the uniform
  remainder estimates for complex powers and the analytic-tail lemma.
- **(d) Beyond reach:** **section C**. A rank-3 statement about a 3×3 matrix of non-elementary integrals
  (`∫ a³R^k/√(Λa²/3 − 1 + κ(C + r log a)/a²) da`) can only be proved with verified numerical integration (interval
  arithmetic with error bounds), which the project does not have. A structural substitute could be built: rank 1 is
  trivial when R is constant, and independence of `1, a⁻⁴, a⁻⁸`-moments needs a determinant ≠ 0 of weighted moments
  over disjoint intervals, which is not automatic. The order-r² scaling is likewise numeric. Separately, the
  semiclassical stress tensor (the `log(aμ)` form) is imported physics.

#### Row 64: `P10_the_descent_is_free_at_the_order…`
- **(a) Computed:**
  - **A:** for `f₁ = q₆(64Λ³ + 48εΛ²ν/a⁴)`, `f₂ = q₄Λ²` and `f₃ = L/a⁴`, the matrix rank is 2 on a four-point
    spectrum and 1 on a one-point spectrum. The nullspaces agree with the coefficient-matrix kernel. The phase is
    absent from `⟨ψ|diag(1,4)|ψ⟩` but present in `⟨ψ|σ_x|ψ⟩`.
  - **B:** closed FRW on `α cosh(T/α)`: R = 4Λ, Ric² = 4Λ², Riem² = 8Λ²/3, and λ₀ = λ₁ = Λ. On the deformation
    `F = Λ/3 + εu/3 − 1/a²`: R = 4Λ + εν/a⁴, the four dimension-six invariants are (64, 16, 32/3, 4)Λ³, the
    first-order shifts are each `(3/4)(ν/a⁴)` times order 0 over Λ, and the ranks are 1, 1 and 2 at orders 0, 1 and 2.
    The ε² terms carry log a, and the a⁻⁶ control gives rank 2 at order 1.
  - **C:** L = 15/4 from the weights, the harmonic sum, an a-dependent control weight, and the limits
    `g(D − parts) → ∞`. The convention kernel `Mk` has rank 2 and dim ker 1. The kernel's third entry is nonzero with
    the anomaly and 0 without it, the ratio is `−L/(48Λ²ενq₆)`, and it diverges as ε → 0.
  - **D:** rank survives an extra A₆ factor.
- **Imported:**
  - the closed-FRW formulas for λ₀, λ₁ and Riem² (typed);
  - the TT weights;
  - the forms of f₁, f₂ and f₃.
- **Paper text:** `pf.inline R=(4\Lambda)`.
- **(b) Minimal foundation:** the same algebra, rank and asymptotics toolkit as row 57. The closed-FRW values on the
  cosh member can be derived with the engine (`FRWk`). Limits use `tendsto` of polynomials, and the nullspaces are
  exhibited vectors.
- **(c) M** (about 250–400 lines). Risk: as row 57 (log-valued sample-point ranks).
- **(d) Nothing new** beyond the imported spectrum.

#### Row 68: `P10_the_overlap_does_not_fall_off_at_all…`
- **(a) Computed:**
  - **A:** an orthonormal 5-element basis of symmetric traceless 3×3 matrices (entries `1/√2` and `1/√6`). The
    completeness relation `Σ_k h_k^{ab}h_k^{cd} = P^{abcd}` holds in all 81 components, with tr P = 5. Each `tr h²` is
    1, giving 5 per chirality and 10 = d(3). Dropping one element breaks the relation.
  - **B:** trivial derivative and exponent arithmetic (`6 − 2s`).
  - **C:** 3 modes, each truncated at 5 levels (a 125-dimensional space), `q_i = (a + a†)/√(2w_i)`. Two-point
    functions are diagonal, equal to `1/2w`. All 81 quartic vacuum expectation values equal the Wick sum, they are
    supported on 1 or 2 distinct labels only, and the two-label product factorises.
  - **D:** maximally symmetric `R = K(ηη − ηη)` in an orthonormal frame. Ten dimension-eight invariants, with up to
    8-index contractions over Fin 4 (65536 terms), are nonzero rationals times Λ⁴ (K = Λ/3), homogeneous of degree 4,
    rank 1, and so on.
  - **E:** trivia: `log 2 ≠ 0`.
- **Imported:**
  - the *level-summed density for general m* (Schur and homogeneity, in prose);
  - ∇Riem = 0 (r6998);
  - d(m).
- **(b) Minimal foundation:**
  - **A:** `Matrix (Fin 3)` with `Real.sqrt` entries, `fin_cases` and `norm_num [Real.sq_sqrt]`;
  - **C:** an **abstract ladder (Fock) algebra** on finitely supported vectors `ℕ³ →₀ ℝ` (or `ℕ →₀ ℝ` per mode,
    tensored), with `a|n⟩ = √n|n−1⟩` and `a†|n⟩ = √(n+1)|n+1⟩`. Prove `⟨0|q_Aq_Bq_Cq_D|0⟩ = Wick` once for all label
    tuples, by computing `q|0⟩`, `q²|0⟩` and so on. This beats transcribing 125×125 matrices;
  - **D:** a **maximal-symmetry contraction lemma**. For `R^{ab}{}_{cd} = K(δ^a_cδ^b_d − δ^a_dδ^b_c)` in dimension n,
    each chain contraction is K^k times an explicit polynomial in n. Prove closed forms for `Ric = (n−1)K·g`,
    `R = n(n−1)K`, `Riem² = 2n(n−1)K²` and the chain traces symbolically, without 4⁸ brute force.
- **(c) M** (about 300–450 lines). Risk: the Fock algebra's `√n` bookkeeping, which needs a clean `Finsupp`
  representation.
- **(d) Beyond reach:** the **level-summed overlap for general m**,
  `Σ_{a∈m}(Y_a·Y_a)(x) = d(m)/V`, independent of x. It needs the TT harmonics on S³ at every level, the isometry
  action, and Schur's lemma. That is the genuine spectral foundation. A from-scratch version would have to *assume*
  that each level is an invariant subspace on which SO(4) acts by isometries. The receipt computes it only at m = 3,
  where the harmonics are frame-constant, and imports the rest.

#### Row 70: `P10_the_second_order_term_is_the_quartics_deviation…`
- **(a) Computed:**
  - **A:** truncated oscillator matrices (N = 8, 12, 18). `dE₂ = ⟨H₄⟩₀₀ − Σ|⟨s|H₃|0⟩|²/(E_s − E₀)` equals
    `(6g₄w² − 11g₃²)/(8w⁴)` exactly and is independent of N. For unitary conjugation by `e^{iλA}` with A = q³ or
    q³ + qpq, `dE₂ = 0`, with both channels nonzero.
  - **B:** H₃ = g₃q³ is non-resonant, a generator A with `i[A,H₀] = H₃` exists, `H₄fake = i[A,H₃]/2`, and
    `dE₂(H₃, H₄fake) = 0`. Hence `dE₂ = ⟨H₄ − H₄fake⟩`, and the locus `g₄ = 11g₃²/(6w²)` is unique.
  - **C:** the cubic channel is a sum of positive terms, the pure cubic gives `−11g₃²/(8w⁴)`, `tr h³ = 3 det h`, and
    the result is even in g₃.
  - **D:**
    - `j = 2k − 4`;
    - the closed de Sitter metric `diag(−1, a², a²sin²χ, a²sin²χ sin²θ)` with a = α cosh(T/α), Riemann from
      Christoffels, R = 12/α², and all 256 components maximally symmetric;
    - on the maximally symmetric frame form: 8 algebraic dimension-six scalars `(64, 16, 4, 32/3, 4, 8/3, 16/9, 8/9)Λ³`,
      Weyl ≡ 0, and both cubic Weyl contractions 0;
    - the control Bianchi I `diag(−1, T², T⁴, T⁶)` at T = 1: C² = 28/3 and both cubic Weyl contractions nonzero;
    - R has nonzero gradient there, and the eight values give more than one distinct ratio.
  - **E:** derivative tests in (Λ, ħ, G, c), which are trivial, and a homogeneity check on an arbitrary combination.
  - **F:** rank 1 against rank 2. `lim(H_M − log M) = γ` and `lim(H_M − log 2M) = γ − log 2`. Also `3/10¹²²` and
    `solve(dE₂ = target)`.
- **Imported:** the r6990 bound and the 1/60 (cited), and the TT spectrum (only as data in E).
- **(b) Minimal foundation:**
  - the Fock ladder algebra (shared with row 68). The "fake" identity is a general algebraic lemma: for H₀ diagonal
    with simple gaps and A defined by `i[A,H₀] = H₃` entrywise, the vacuum second-order energy of
    `(H₃, i[A,H₃]/2)` is 0. That is a finite-sum statement on the support of `H₃|0⟩`;
  - closed de Sitter curvature: existing `FRWk`/`SecondSeatFRW` instances at k = 1 with a = α cosh, plus maximal
    symmetry of the full tensor (`frw_closed_slicing` exists);
  - the maximal-symmetry contraction lemma (shared with row 68), plus the Weyl tensor definition;
  - power-law Bianchi I: a new separable instance (`cS` with profiles T^{2k}), evaluated at T = 1. The cubic Weyl
    sums are 4⁶-index sums of rationals;
  - `Real.tendsto_harmonic_sub_log`.
- **(c) L** (about 600–900 lines). Main risk: the 4⁶-term cubic-Weyl sums at the Bianchi I control point, and the
  engine-level Weyl tensor (the engine has `weyl2C` but no cubic contractions).
- **(d) Beyond reach:** Rayleigh–Schrödinger as a statement about the *actual spectrum* of `H₀ + λH₃ + λ²H₄` on
  L²(ℝ). The cubic oscillator is unbounded below and has no ground state, so it is not even well defined without
  extra structure. The receipt only uses the formal RS formula on finite matrix elements. The Lean version should
  state *that*, and must not claim an eigenvalue expansion.

#### Row 73: `P10_the_vertex_numbers_are_exact…`
- **(a) Computed:**
  - **A:**
    - the Misner `KK − K² = −6H² + 6(β̇₊² + β̇₋²)` with zero cross term, compared against the formula parsed from the
      paper;
    - the unimodular product = 1;
    - `R₃ = 2(2Σλ_iλ_j − Σλ_i²)`, with value 6 at β = 0;
    - the Taylor coefficients to order 4: `−48(β₊² + β₋²)`, `160(β₊³ − 3β₊β₋²)` and `−336(β₊² + β₋²)²`;
    - μ² = 48/6 = 8 = m² − 1 at m = 3, and d = 10.
  - **B:** the kinetic term in h, `6ḣ²(1 − 4h + 12h² …)`, against the exponential variable. The Jacobian at 0 is 1.
  - **C:** 2-mode Fock space (NF = 7). `⟨V₄⟩ = 8c₄s²`. The cubic V₃ reaches only 3-quantum states (2 states), so the
    one-quantum amplitude cancels, and `dE₃ = −8g²s³/ħω`. Then:
    - the normalisation gives `c₄ = 14κ/3V` and `g² = 800κ/27V`;
    - total = `4κħ²(63μ² − 200)/(27Va³μ⁴)`, which is `19κħ²/(27Va³)` > 0 at μ = 2√2;
    - the threshold is 200/63;
    - the density scales as a⁻⁶.
  - **D:** linear solve families, and the Jacobian rank is 2.
  - **E:** asymptotic coefficients of `dμ` and `d/μ` (2, −9 and 15/4; 2 and −7). The Faulhaber leading terms are
    residue over location, the log coefficient is 15/4, the product is ½, and `Σ2m³` has an M² term.
- **Imported:**
  - the closed form of R₃ (typed, but it is Milnor's formula);
  - TT spectrum values (partly *re-derived* here at m = 3);
  - the RS formula.
- **Paper text:** the `pf.inline` parse of the KK formula.
- **(b) Minimal foundation:**
  - `S3Frame.milnor_scalar`, which already proves `R = 2(4e₂ − e₁²)/e₃`. With e₃ = 1 that is the receipt's R₃;
  - Taylor coefficients of `R₃(β)` via `Real.exp` series with a remainder (`Real.exp_bound`), or by showing that the
    4-jet at 0 matches via iterated derivatives;
  - the Fock ladder algebra (shared);
  - the asymptotics, Faulhaber and harmonic toolkit (shared with rows 57 and 64).
- **(c) M** (about 350–500 lines). Risk: 2-variable Taylor bookkeeping.
- **(d) Beyond reach:** the RS spectrum, as in row 70, and the tower beyond m = 3 (imported). Nothing else.

---

## 2. Per-foundation summary

### 2.1 Levi-Civita volume form (rows 46, 69, 89, 96)
- **Common core (about 800–1200 lines):**
  1. `eps4 : Fin 4 → Fin 4 → Fin 4 → Fin 4 → ℤ` from `Equiv.Perm.sign` (or a table), with its antisymmetry lemma.
  2. Index lowering and raising on `NonDiag`'s `curvG` for an explicit `Gi`.
  3. `pontryagin g := ½ Σ ε R_{mnab}R_{rs}{}^{ab} / √(−det g)`.
  4. The **parity lemma** for an ignorable, block-orthogonal coordinate. It kills `*RR` for static, spherically
     symmetric and polarised families with *arbitrary* profiles, in one theorem instead of seven brute-force tables.
  5. The **sign-twist lemma** under coordinate reflections, which gives oddness in the twist for arbitrary Gowdy
     data.
  6. The CS current `K^μ` and the **transgression identity** `√−g *RR = −∂_μK^μ`, as a polynomial jet identity in the
     `Bianchi2.lean` style.
  7. Mathlib's divergence theorem on a rectangle for the Stokes check.
- **Row costs on top of the core:** 46 ≈ 100 (needs none of it), 69 ≈ 350, 96 ≈ 700, 89 ≈ 1200–2200 (Kerr and the
  "powers {1, 3}" expansion dominate).
- **Easiest first:** 46 → 69 → 96 → 89.
- **Overall: about 3000–4500 lines.** About 2000–2500 if Kerr is cut to its closed-form algebra (the Ψ₂ identity plus
  oddness) and "powers {1, 3}" is replaced by the proved oddness.

### 2.2 Homogeneous spaces G/H (row 80)
- **Common core:** none. What is needed is so(5,1) as 6×6 integer matrices, explicit `ad` on the basis, and the trace.
  No G/H.
- **Overall: about 150–350 lines.** Risk: computation time without `native_decide`.

### 2.3 Spinors and the Dirac operator (rows 82, 84, 85)
- **Common core:** none of spin geometry. A small "round-sphere data" section holds `R = n(n−1)/a²` and the Dirac
  spectrum `±(n/2 + k)/a` as an **explicitly labelled imported definition**. Row 85 needs a frame/tetrad lemma (an
  orthonormal coframe for a diagonal metric). Optionally, deriving the spin connection from the engine's Christoffels
  adds about 150–250 lines and makes "the frame P13 deferred, derived" true.
- **Easiest first:** 82 → 84 → 85.
- **Overall: about 200–600 lines.**
- **Beyond reach:** a genuine Dirac operator and its spectrum, which no computed check uses.

### 2.4 Spectral theory (rows 23, 24, 57, 60, 63, 64, 68, 70, 73)
- **Common core (about 600–900 lines; none of it is spectral theory):**
  1. **A TT-level data interface:** `μ²(m) = m² − 1`, `deg(m) = 2(m² − 4)` (and c_C for row 60), declared as *imported
     spectral data* so that no theorem pretends to have derived it. Row 73 re-derives μ²(3) and deg(3) from the
     metric.
  2. **Asymptotics at ∞:** `d·μ^{±1} = polynomial + r/m + O(m⁻³)`. Faulhaber sums. `harmonic` and
     `Real.tendsto_harmonic_sub_log`. `riemannZeta` special values and `riemannZeta_residue_one`.
  3. **Fock ladder algebra** on finitely supported vectors: vacuum moments, Wick, and the formal RS second-order
     energy (rows 68, 70, 73).
  4. **Maximal-symmetry contraction lemmas and the Weyl tensor**, plus closed-FRW/dS and power-law Bianchi I instances
     (rows 64, 68, 70; rows 23 and 24 already have theirs).
  5. **A small rational-rank toolkit:** a minor ≠ 0 plus all (r+1)-minors = 0, or exhibited kernels, with log bounds
     for log-valued entries (rows 57, 60, 64).
- **Row costs on top of the core:** 23 ≈ 0–30, 24 ≈ 60, 64 ≈ 300, 68 ≈ 350, 73 ≈ 400, 63 ≈ 300 (formal ζ; +700–1200
  for a genuine ζ_Δ continuation), 57 ≈ 600, 70 ≈ 750, 60 ≈ 1500–2500.
- **Easiest first:** 23 → 24 → 64 → 68 → 73 → 63 (formal) → 57 → 70 → 60.
- **Overall: about 5000–7000 lines** with row 60 in full and a formal row 63. About 3500–4500 if row 60's Part A is
  sufficiency-only. **Add about 700–1200 lines** for a genuine ζ_Δ(0).
- **Beyond reach:**
  - row 63's numeric SVD rank (needs verified numerics);
  - row 68's general-m level sum (needs harmonics plus Schur);
  - row 60's invariant-theory completeness and harmonic level sums;
  - an honest RS spectrum (rows 70, 73);
  - the `b₄` coefficients (rows 23, 24).
  None of these is required for the receipts' computed checks, except row 63 section C.

---

## 3. Genuinely beyond reach: the specific objects

| row | object or property | what a from-scratch version would have to assume |
|---|---|---|
| 23, 24 | graviton one-loop `b₄` coefficients (53/90, 7/20, 1/120) | the heat-kernel coefficients of the Lichnerowicz operator with ghosts; imported constants (the result is coefficient-independent anyway) |
| 46 | horizon "area" as an integral | none needed; the formula `4πr²` is used directly (`Measure.toSphere` would reach it if wanted) |
| 57, 64, 73 | the TT spectrum μ², deg on S³ | eigen-decomposition of the Lichnerowicz Laplacian on TT tensors of S³; imported data |
| 60 | (i) every SO(3) invariant is built from δ and ε (FFT); (ii) level sums of harmonic products are invariant tensors; the value of c_C; the seven r7032 rationals | (i) classical invariant theory (assume it, or state results "within the candidate span"); (ii) TT harmonics plus isometry action plus Schur; imported numbers |
| 63 | rank 3 of the 3×3 matrix of integrals, by 40-digit quadrature and SVD; the r² scaling | verified numerical integration with rigorous error bounds (interval arithmetic); not available |
| 63 | ζ_Δ(0) as a true analytic continuation (rather than the formal rule) | reachable at L size; the formal version needs only ζ(0), ζ(−2) and the residue at 1, and it already exists as `S3Frame.zeta_count` for the free case |
| 68 | `Σ_{a∈m} Y_a·Y_a = d(m)/V` for every m | the TT harmonics at each level as an SO(4)-invariant subspace, plus Schur's lemma |
| 70, 73 | the second-order energy shift as an eigenvalue of the perturbed Hamiltonian | the formal RS formula only; the cubic oscillator is unbounded below, so there is no spectral statement to make |
| 80 | SO(5,1)/SO(4,1) as a manifold with an invariant metric equal to dS₅ | assume the invariant metric at the base point is `B|_m` (the receipt's reading) |
| 82, 84, 85 | the Dirac spectrum ±(n/2+k)/a on Sⁿ; Friedrich, Lichnerowicz, Atiyah–Hirzebruch; Dirac separation on SdS with λ = j+½ | the spinor bundle, the Dirac operator and its spectral theory; imported as a labelled definition |
| 85 | check (5) evaluates √f where f < 0 (complex modulus) | use `Complex.sqrt`, or restate; a `Real.sqrt` transcription fails |
| 89 | anomaly prefactor 1/384π² | QFT; imported (the receipt says so) |
| 89 | "the ω-grading powers are exactly {1, 3}" | not beyond reach, but needs the explicit four-function expansion (XL); oddness is reachable structurally |
| 96 | K^φ ≡ 0 on the general dynamic spherical class | not beyond reach; no structural shortcut is known, so it needs either a warped-block lemma or large tables |

**Paper-text checks (not mathematics; out of scope for any Lean build):** 23 (#6), 46 (`eq:ds-entropy` parse),
63 (two `pf.inline` parses), 64 (`pf.inline`), 73 (KK parse), 89 (Part 7: a corpus regex count, two strings, r6752's
receipt strings), 96 (seven .tex string checks). Rows 24, 57, 60, 68, 69, 70, 80, 82, 84 and 85 have none.

---

## 4. Global easiest-first order (all 17)

| # | row | foundation | size | why here |
|---|---|---|---|---|
| 1 | 23 | spectral | S (≈0–30) | already proved in `RunningLayer.lean`; only re-point it |
| 2 | 24 | spectral | S | `BianchiI.row1_shear` plus rational `b₄` arithmetic |
| 3 | 82 | spinors | S | rational arithmetic on an imported spectrum |
| 4 | 46 | LC | S | polynomial algebra on f; no volume form |
| 5 | 84 | spinors | S | algebra plus decimal and √0.7 bounds |
| 6 | 85 | spinors | S–M | `sq_sqrt` tetrad check plus numeric √ bounds (fix check 5); optional frame connection |
| 7 | 80 | G/H | M | finite so(5,1) Killing form; timing risk only |
| 8 | 64 | spectral | M | algebra, ranks, asymptotics toolkit |
| 9 | 68 | spectral | M | completeness relation, abstract Wick, maximal-symmetry contractions |
| 10 | 73 | spectral | M | Milnor (exists), Taylor, Fock, pole data |
| 11 | 63 | spectral | M (formal) / L (genuine ζ) | algebra plus formal ζ; section C is beyond reach |
| 12 | 57 | spectral | L | rank-with-logs, asymptotics, ζ residue |
| 13 | 69 | LC | M on core (core L) | first consumer of the Pontryagin core |
| 14 | 70 | spectral | L | RS identity, de Sitter maximal symmetry, cubic Weyl, power-law Bianchi I |
| 15 | 96 | LC | L | parity lemma, Stokes, K^φ risk |
| 16 | 89 | LC | XL | Kerr tables, general Gowdy grading, transgression identity |
| 17 | 60 | spectral | XL | invariant-tensor solver, 3⁵/3⁶ sums, TT jet fit on `Row62Jet` |

**Grand total: about 9000–13000 Lean lines** for all 17 at full receipt fidelity (genuine ζ_Δ excluded; row 63
section C excluded as beyond reach). **About 6000–8000 lines** with the three trims recommended above: Kerr reduced
to its closed form; "powers {1, 3}" replaced by proved oddness; row 60 Part A sufficiency-only. Rows 23, 24, 82, 46,
84 and 85 together cost **under about 600 lines** and can be done immediately, on the engine as it stands.
