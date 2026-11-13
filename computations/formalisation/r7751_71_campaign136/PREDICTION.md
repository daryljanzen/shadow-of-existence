# `r7751+71.1` — PRE-REGISTRATION: campaign 136, **closing P9: `I` and `J` defined, `I = J = 0` for the vacuum pp-wave (8b) and `I³ ≠ 27J²` for vacuum Bianchi I (7b)**. ⌗ `550` new lines (band 400–750), p(both) `0.5`

*Registered before any Lean. This is the price 69 ordered in r7751, and one campaign covers both rows, so it runs. The
probe is `probes/Range.lean`, appended (`ij_`). Mathlib only.*

## The definitions
- **`rn_lc a b c d`** is the Levi-Civita symbol. It is `Π_{i<j}(x_j − x_i)/12` over the index values: `+1`/`−1` on
  even/odd permutations of `(0,1,2,3)` and `0` on repeats. A lemma checks it on the identity and on one transposition.
- **`ε_{abcd}`** is `√|det g| · rn_lc`. The dual operator is `(*W)^{ab}{}_{cd} = ½ ε^{ab}{}_{ef} W^{ef}{}_{cd}`, with
  `W` the Weyl bivector operator of campaign 135 (`pw_W`, generalised as `ij_W`).
- **The four real invariants:**
  - `K₁ = C_{abcd}C^{abcd}`;
  - `K₂ = C_{abcd}{*C}^{abcd}`;
  - `K₃ = C_{ab}{}^{cd}C_{cd}{}^{ef}C_{ef}{}^{ab}`;
  - `K₄ = C_{ab}{}^{cd}C_{cd}{}^{ef}{*C}_{ef}{}^{ab}`;
  - all four as traces over ordered index pairs.
- **The complex invariants:** `I = (K₁ − iK₂)/16` and `J = (K₃ − iK₄)/96`.

## Rows

| Row | Statement | Lines | p | Expected stop |
|---|---|---|---|---|
| 8b | For a vacuum pp-wave (harmonic `H`, mixed partials commuting): `I = 0` and `J = 0`. **The proof is structural:** each trace has two adjacent `W`'s after reordering the finite sums, and `W∘W = 0` (`pw_nilpotent`). This holds for any `ε`. With `pw_witness` (Weyl ≠ 0), this is type N | 120–200 | 0.85 | Reindexing the sums (`Finset.sum_comm`) |
| 7b | For vacuum Bianchi I with distinct `Cᵢ` at `cosh 3t > 3`: `I³ ≠ 27J²`. The route: (i) the full Weyl table of `bi_g` (every `C_{abcd}`: the `0i0i` and `ijij` families, all others zero); (ii) `K₂ = K₄ = 0` and explicit `K₁`, `K₃` in the electric eigenvalues; (iii) `I³ − 27J² = c·Π_{i<j}(Eᵢ − E_j)²` with `c ≠ 0`, using `ΣEᵢ = 0`; (iv) non-zero by `bi_typeI` | 280–550 | 0.55 | The 4096-term sums for `K₃` and `K₄` under `simp` (time-out). **Fallback:** prove the contractions on the explicit `W` table by reorganising into pair-diagonal sums |

**If 7b stops,** it stays BUILT IN PART, with `K₁`, `K₂` and the stop named, and 8b closes alone.

**Interpretive, not formalised:** that `I³ = 27J²` characterises algebraic speciality (the Petrov classification
itself). The rows formalise the invariants' values, as `prop:typeI` and `prop:radiative` state them.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
