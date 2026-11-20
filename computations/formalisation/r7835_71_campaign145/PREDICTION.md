# `r7835+71.1` — CENSUS AND PRE-REGISTRATION: 72's L550 Y10–Y17, and campaign 145 on the reachable rows. ⌗ `320` new Lean lines (band 200–500), p(E1–E8 all BUILT and landed) `0.55`

*The order is 69's `r7831`, carried by `r7833` and `r7835`:
- ① census every machine-checkable claim among 72's Y10–Y17, with its formal core named or the reason it has none;
- ② register and build the reachable ones as campaign 145, and land them beside their claims in the same campaign;
- ③ state exactly any gap Mathlib cannot cross.

The census reads the five paragraphs that cite a Y10–Y17 receipt, at `6cfab7d85`: P14:914, P15:258, P16:669, P16:681
and P16:804. It also reads each receipt's own statement of what it computes. This is registered before any Lean.

The probe will be the new standalone file `probes/NeutrinoSector.lean` (`ns_`), importing only Mathlib. Landing
follows campaign 144's form: a plain paragraph directly after the claiming paragraph, naming each `ns_` theorem and
`NeutrinoSector.lean`, with the PDFs and served pages rebuilt.*

## ① and ② The census, priced

### Cored, cheapest first: campaign 145's rows

| Row | Paper:line (receipt) | Claim | Formal core | Lines | p |
|---|---|---|---|---|---|
| E1 | P15:258 (Y12) | "the mixing is `θ = v_L/v_R` and obeys the seesaw relation `θ² = m_ν/m_N` exactly" | with `m_ν = v_L²/M`, `m_D = v_L v_R/M`, `m_N = v_R²/M` (`M, v_R ≠ 0`): `θ² = m_ν/m_N` and `m_D² = m_ν m_N` | 15 | 0.99 |
| E2 | P14:914, P15:258 (Y13) | the fermion channel is "a total singlet or an adjoint" (`4 × 4̄`), the scalar channel `4 × 4` | the dimension counts only: `4·4 = 1 + 15 = 6 + 10` and `2·2 = 1 + 3`. The representation decomposition itself is not built (see below) | 5 | 0.99 |
| E3 | P14:914 (Y14) | "a generation's colour, isospin and chirality labels make sixteen slots and the sixteen states fill them, the four colourless ones each occupied once" | any injective assignment of 16 states to the `4·2·2` slots is a bijection, so no slot is free; the colourless slots number `1·2·2 = 4`, and each is hit exactly once | 35 | 0.95 |
| E4 | P15:258, P16:804 (Y11) | "`ΔN_eff = 3(10.75/g_{*s})^{4/3}`: `0.29` at the bound, falling to `0.14`" | `3(10.75/61.75)^{4/3} ∈ (0.285, 0.295)` and `3(10.75/106.75)^{4/3} ∈ (0.140, 0.142)`, each by cubing (`y³ = x⁴`) | 50 | 0.85 |
| E5 | P15:258, P16:804 (Y11) | "`T_dec ≃ (M_{W_R}/M_W)^{4/3}` MeV: about `340` MeV at … `6.4` TeV" | `(6400/80.38)^{4/3} ∈ (335, 345)` | 30 | 0.85 |
| E6 | P15:258, P14:914 (Y12, Y13) | the scale arithmetic: `2.5×10⁻⁵` eV at the reduced Planck mass, "two thousand times short", `M ≃ 1.2×10¹⁵` GeV, `m_N ≃ 1` GeV at `3.5×10⁷`, the window of ratios `10⁻¹¹`–`10⁻⁵`, and the caps `2.4×10¹³` and `1.2×10¹⁰` | with `v = 246.22`, `M_Pl = 2.435×10¹⁸` and `m_ν = 0.05` eV, each figure inside its printed rounding; caps `M·√(10⁻¹⁰)` | 60 | 0.9 |
| E7 | P16:681 (Y17) | "a Majorana mass `v_R²/M_Pl` … a hundred million times more widely than the solar neutrino data allow" | `v_R = 2·6400/0.65`; `μ = v_R²/M_Pl ∈ (0.155, 0.165)` eV; `μ_allowed = 2×10⁻¹¹/(2√(7.42×10⁻⁵)) eV`; `10⁸ < μ/μ_allowed < 2×10⁸` | 40 | 0.85 |
| E8 | P15:258, P14:914 (Y13) | "the neutral mass matrix having one zero for each singlet short of six, so the two measured splittings need at least five" | for any `D : 6 × n` and any `M_S : n × n` over `ℂ`, the matrix `[[0, D], [Dᵀ, M_S]]` has rank `≤ 2n`, so its kernel has dimension `≥ 6 − n`. Hence `n ≤ 4` leaves at least two massless states, and `n = 3` leaves three. Proof: the matrix splits as `[[D],[0]]·[0 | I] + [[0],[I]]·[Dᵀ | M_S]` | 120 | 0.75 |

**E8 is the expected stop, at p 0.75.** The rank of a block matrix has no ready lemma, and the kernel's dimension needs
rank–nullity on `mulVecLin`.

"Exactly" `6 − n` zeros for generic couplings (Y13's random draws) is not claimed. The Lean states the bound that holds
for every coupling. That bound is all that "need at least five" uses.

### Cored but out of reach, or not chosen

- **Y13, the `SU(4)` decompositions `4 ⊗ 4̄ = 1 ⊕ 15` and `4 ⊗ 4 = 6 ⊕ 10`, by Casimir.** Mathlib has no
  representation theory of `su(4)`. The explicit-matrix route, Casimir eigenvalues on 16-dimensional tensor products,
  is about 400 lines at p 0.4. Not chosen; E2 is its dimension core.
- **Y14, "the compact face carries no Dirac zero mode"** (the Lichnerowicz bound on `S⁵`) **and the `S⁴` index one.**
  These need spin geometry, which Mathlib lacks. Beyond.

### No formal core

- **Y10:** the cosmogenesis network's helium and deuterium shifts. These are numerical outputs of the BBN network:
  **empirical**.
- **Y15:** lepton number violation in equilibrium above `≈ 5×10¹²` GeV. **Y16:** flavoured-washout scales,
  `3×10¹⁰`, `6×10¹²`, `4×10⁸` and `2.5×10⁻⁸`. These are **physics estimates and Boltzmann-type bounds**, not exact
  statements.
- **Y17:** the ordering odds, the lightest mass and the double-beta range (`1.5`–`8` meV) come from random-coefficient
  draws: **numerical**. "Least-arbitrariness reads the masses as Majorana" is **interpretive**. Its one exact
  arithmetic statement is E7.
- **P15:258** `N_eff` placements (`2.7`–`4.1σ`, `1.1`–`2.0σ`): arithmetic on measured inputs. They are covered by the
  receipts, and are not chosen.

## ③ Campaign 145: E1–E8, built and landed

Every row's hypotheses are explicit and satisfiable. The numeric rows are their own witnesses, and E8 carries an
instance (`n = 3`).

Landing sites:
- **P14:914:** E2, E3, E6 and E8.
- **P15:258:** E1, E2, E4, E5, E6 and E8.
- **P16:681:** E7.
- **P16:804:** E4 and E5.

Each landing is placed after its paragraph and read before it is edited.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
