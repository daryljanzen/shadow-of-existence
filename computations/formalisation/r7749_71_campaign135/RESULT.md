# `r7749+71.2` — RESULT: campaign 135, **P9's last cored rows. The Carter "iff" (5) is BUILT in both directions; vacuum Bianchi I (7a) is BUILT; its type I (7b) and the pp-wave's type N (8b) are BUILT IN PART, stopping at `I` and `J` as registered.** ⌗ `1075` new lines (band 1200–2400, **under by 125**), at p(all four) `0.25`: two of four are BUILT, and the registered fallbacks are what landed for 7b and 8b

*The registration is `PREDICTION.md`. The probe is `probes/Range.lean`, P9's citable file, now 2161 lines, with sections
`car_`, `bi_` and `pw_` appended.*

## Verification
- `lake env lean probes/Range.lean` gives **0 errors and 0 warnings** in about 10 minutes.
- **44 axiom lines** (23 earlier, 21 new), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- `KrCurvature` is byte-identical to `StaticEinstein.lean`'s.
- **Options, stated in terms:**
  - `car_Γ`, `car_Ric` and `pw_Rlow_vanish` carry `maxHeartbeats 0`.
  - The first two also carry `linter.unusedSimpArgs false`. They are generated all-cases proofs.
- **The generator** (sympy) is in `generator/`. It emits 50 derivative lemmas and the Ricci table, and Lean checks each
  one.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| 5 | `car_Ric`: the Ricci tensor of `eq:carter` for **arbitrary** `Δ_r = R(r)` and `Δ_p = P(p)`, all 16 components, from the coordinate Riemann tensor. **"If"** (`car_vacuum_if`): the quartics of `eq:quartics` with a shared `c₀` give `R_μν = Λg_μν` wherever `Σ, Δ_r, Δ_p ≠ 0`. **"Only if"** (`car_only_if`): on an open preconnected rectangle `I × J` where `Σ, Δ_r, Δ_p ≠ 0`, the `rr` and `pp` equations alone force both quartics, with one `c₀`. The steps are the cleared equations of `thm:pd`'s proof, the separation `Δ_r″ + Δ_p″ = −4ΛΣ`, two integrations by `IsOpen.is_const_of_deriv_eq_zero`, and `d₀ = c₀` (the `rr` equation is exactly `d₀ − c₀ = 0`). **Witnesses:** `car_witness` (`Λ = 3`, mass, rotation and NUT all non-zero) and `car_only_if_witness` (the hypotheses discharged on `(1, 3) × (0, 1)`) | **BUILT** |
| 7a | `bi_Ric`: the Bianchi-I Ricci tensor for arbitrary scale factors on `t > 0`. `bi_vacuum`: `aᵢ = sinh(3t)^{1/3} tanh(3t/2)^{Cᵢ/3}` (`Real.rpow`), `ΣCᵢ = 0`, `ΣCᵢ² = 6` gives `R_μν = 3g_μν` at every `t > 0`, via `log aᵢ` with `(log aᵢ)′ = (cosh 3t + Cᵢ)/sinh 3t`. **Witness:** `bi_witness`, `C = (√3, 0, −√3)` | **BUILT** |
| 7b | `rn_Weyl` (the 4-D Weyl tensor). `bi_electric`: the electric eigenvalues are `Eᵢ = C_{0i0i}/aᵢ² = (2 + Cᵢ cosh 3t − Cᵢ²)/sinh² 3t`, and every magnetic component `C_{0jkl}` vanishes. `bi_typeI`: distinct `Cᵢ` give pairwise distinct `Eᵢ` once `cosh 3t > 3` (`bi_typeI_witness`: `t = 1`). `bi_typeD`: `C = (2, −1, −1)` gives `E₂ = E₃` at every `t` | **BUILT IN PART** |
| 8b | `pw_Weyl_eq`: a vacuum pp-wave's Weyl tensor is its Riemann tensor. `pw_nilpotent`: the bivector operator `W^{ab}{}_{cd}` squares to zero, for all 256 components. `pw_invariants`: `tr W² = tr W³ = 0`. `pw_witness`: `H = x² − y²` has `C_{uxux} = −1 ≠ 0` | **BUILT IN PART** |

**The two gaps, named:**
- **7b.** The step from "three distinct electric eigenvalues, zero magnetic part" to `I³ ≠ 27J²` is not formalised.
- **8b.** The step from nilpotency to `I = J = 0` is not formalised. The traces with a Hodge dual need `ε` and the
  left–right duality of the Weyl tensor.
- In both cases `I` and `J` are not defined in Lean. This is the registered stop (the `ε` contraction), which was not
  attempted.

## Findings the build turned up
1. **8b needs a hypothesis the registration did not state.** The pp-wave's Riemann component `R_{uuxy}` is
   `−½(∂_y∂_x H − ∂_x∂_y H)`, which `kr_pd` does not make vanish by itself. `pw_Rlow_vanish` and everything after it
   assume that the mixed partials of `H` commute at the point. That holds for any `C²` profile, and trivially for the
   witness.
2. **7b's Type I holds generically, not at every `t`.** We have `E_i − E_j = (C_i − C_j)(cosh 3t + C_l)/sinh² 3t`. So
   two eigenvalues meet at the one time when `cosh 3t = −C_l`, which is possible whenever some `C_l < −1`. For
   `C = (√3, 0, −√3)`, `E₁ = E₂` at `cosh 3t = √3`. This fits P9's "its speciality varies with time and departs from
   the special value". A reading of `prop:typeI` as "Type I at every `t`" would be false at that instant; `bi_typeI`
   states the honest version (`cosh 3t > 3`).

**Against the registration:**
- **Size:** 1075 lines against a band of 1200–2400.
- **The stops that did not hold:** the Carter integrations and the `rpow` bridge both went through.
- **The stop that held:** the `ε` contraction, which was not attempted, as the fallback allowed.
- **The generator's sympy `simplify`** took over 30 minutes on the abstract Ricci tensor. `cancel` replaced it in
  seconds. Lean's own build of the abstract Ricci tensor took 54 seconds.

**P9 tally:** all 13 cored rows have been attempted.
- **11 BUILT:** 3a, 3b, 3c, 4a, 4b, 4c, 4d, 4e, 5, 7a, 8a.
- **2 BUILT IN PART:** 7b and 8b, both stopping at defining `I` and `J`.

**Interpretive, not formalised:** `cor:carter`, `rem:carter-chain`, the Goldberg–Sachs reading, Zipoy–Voorhees, and
"high symmetry forbids it".

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
