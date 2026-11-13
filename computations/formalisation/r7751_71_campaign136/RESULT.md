# `r7751+71.2` — RESULT: campaign 136, **`I` and `J` defined; 8b (`I = J = 0`, type N) and 7b (`I³ ≠ 27J²`, type I) BUILT. P9 is closed: 13 of 13 cored rows BUILT.** ⌗ `282` new lines (band 400–750, **under by 118**), at p(both) `0.5`

*The registration is `PREDICTION.md`. The probe is `probes/Range.lean` (2443 lines), with sections `ij_` and `bi_`
appended.*

## Verification
- `lake env lean probes/Range.lean` gives **0 errors and 0 warnings** in about 8 minutes.
- **54 axiom lines** (44 earlier, 10 new), every one `[propext, Classical.choice, Quot.sound]`.
- The forbidden-token grep is clean, imports are `Mathlib` only, and `check_no_sorry.py` reports ALL 29.
- `KrCurvature` is byte-identical to `StaticEinstein.lean`'s.
- **Options, stated in terms:**
  - `bi_Rfull`, `bi_W` and `ij_tr3` carry `maxHeartbeats 0`.
  - The first two also carry `linter.unusedSimpArgs false`. They are all-cases proofs.

## The definitions
- `ij_lc a b c d = Π_{i<j}(x_j − x_i)/12` is the Levi-Civita symbol. `ij_lc_values` checks `+1` on `(0,1,2,3)`, `−1`
  on a transposition and `0` on a repeat.
- `ij_W` is the Weyl bivector operator `W^{ab}{}_{cd}` on ordered pairs.
- `ij_E` is the Hodge dual `½ε^{ab}{}_{ef}`, with `ε_{abcd} = √|det g| · ij_lc`.
- **The four real invariants:**
  - `K₁ = tr W² = C_{abcd}C^{abcd}`;
  - `K₂ = tr(W·*W)`;
  - `K₃ = tr W³`;
  - `K₄ = tr(W²·*W)`.
- **The complex invariants:** `ij_I = (K₁ − iK₂)/16` and `ij_J = (K₃ − iK₄)/96`.

## Rows

| Row | Statement (Lean) | Mark |
|---|---|---|
| 8b | `pw_IJ`: a vacuum pp-wave (harmonic `H`, mixed partials commuting) has `I = 0` and `J = 0`. The proof is structural: `W² = 0` (`pw_nilpotent`) and the trace is cyclic, `tr(W·E·W) = tr(E·W²)`, so it holds for any dual. `pw_typeN`: `H = x² − y²` has `I = J = 0` and Weyl ≠ 0, which is type N | **BUILT** |
| 7b | `bi_Rfull`: Bianchi I's full Riemann tensor, all 256 components, `R_{abcd} = s_ab(δ_acδ_bd − δ_adδ_bc)`. `bi_W`: the vacuum Weyl operator is the block table with `U₀ᵢ = −Eᵢ` and `Uᵢⱼ = −E_l`. **Dual traces:** `K₂ = K₄ = 0`, because the operator is supported on pair blocks and the dual kills each block (`ij_tr_dual`). `ij_tr2` and `ij_tr3` give `I = ½ΣEᵢ²` and `J = −⅙ΣEᵢ³`. With `ΣEᵢ = 0`, **`I³ − 27J² = ¼Π_{i<j}(Eᵢ − E_j)²`**, which is non-zero for distinct `Cᵢ` at `cosh 3t > 3` (`bi_IJ`). **Witness:** `bi_IJ_witness`, `C = (√3, 0, −√3)` at `t = 1` | **BUILT** |

**Against the registration:**
- **Size:** 282 lines against a band of 400–750.
- **The expected stop for 7b did not hold.** The 4096-term contraction for `tr W³` closed by `simp` on the explicit
  table, and the dual traces needed no brute force.
- **The definitions are standard** (Penrose–Rindler normalisation). The Petrov classification itself, that `I³ = 27J²`
  characterises algebraic speciality and `I = J = 0` with `C ≠ 0` is N or III, stays interpretive, as registered.

**P9 tally: closed.**
- **13 of 13 cored rows BUILT:** 3a, 3b, 3c, 4a, 4b, 4c, 4d, 4e, 5, 7a, 7b, 8a, 8b.
- 4 rows have no formal core.
- 4a and 4c are in the chart `x = cos θ`; the transfer to the θ chart is not formalised.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
