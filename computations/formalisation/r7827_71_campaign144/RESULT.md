# `r7827+71.2` — RESULT: campaign 144, **all fourteen rows BUILT (C1–C14): the claims P14, P15 and P18 gained since the closing table, at their formal cores. The registered stop (C13) did not hold.** ⌗ `477` new lines (band 300–750, estimate 450, **in band**), at p `0.5`

*The registration and census are in `PREDICTION.md`. The probe is the new standalone file `probes/NewClaims.lean`
(`nc_`), 477 lines. It imports only Mathlib, carries no copies, and sets no option.*

## Verification

- `lake env lean probes/NewClaims.lean` gives **0 errors and 0 warnings**, in about 23 s.
- **16 axiom lines:**
  - 15 read `[propext, Classical.choice, Quot.sound]`;
  - one, `nc_four_witness`, a pure `decide` on `Fin 4`, reads `[propext, Quot.sound]`, a subset of the three.
- The forbidden-token grep is clean, the only import is `Mathlib`, and `check_no_sorry.py` reports ALL 29.

## Rows

| Row | Paper:line | Lean | Mark |
|---|---|---|---|
| C1 | P14:892 (Y2) | `nc_sixteen`: `3·2·2 + 1·2·2 = 16 = 4·2·1 + 4·1·2` | **BUILT** |
| C2 | P14:368 (Y1) | `nc_LambdaYM_lt`: `μ e^{−1/(2b₀g²)} < μ` for `μ, b₀, g² > 0` | **BUILT** |
| C3 | P14:896 (Y4) | `nc_f_parity`: `f(−r;M) = f(r;−M)`. `nc_f_diff`: `f(−r;M) − f(r;M) = 4M/r`, which is zero only for `M = 0` | **BUILT** |
| C4 | P15:594–595 | `nc_r2_signs`: `0.9918² − 1 = −0.01633276 < 0 < 0.19377476 = 1.0926² − 1`; these print as `−0.0163` and `+0.1938`; the size ratio lies in `(11.85, 11.95)` | **BUILT** |
| C5 | P14:896 (Y4) | `nc_characters`: `(t, r) ↦ (t, −r)` maps the four characters onto themselves, and sends the SM occupation to `(−1, −1)`, which it lacks | **BUILT** |
| C6 | P15:580–582 | `nc_signature_scale`: `exp[−α(ℓ/ℓ_D)²(r²−1)] = exp[−(ℓ/(ℓ_D/√α))²(r²−1)]`. `nc_signature_number`: `|1951.9/√1.7 − 1497.04| < 0.005` | **BUILT** |
| C7 | P14:892 (Y2), SYN:3077 (Y8) | `nc_charges`, on the sixteen-state table: `diag(1,1,1,−3)` is traceless; `Q = I₃L + I₃R + (B−L)/2` with `B − L = T/3` gives every SM charge; `Y = 2(I₃R + (B−L)/2)` gives every hypercharge (`Q = I₃L + Y/2`); `ν_R` has `Q = Y = 0` and `B − L = −1` | **BUILT** |
| C8 | P14:607/610, SYN:2802 | `nc_anomalies`: the `SU(3)²Y`, `SU(2)²Y`, gravitational-`Y`, `Y³` and `SU(3)³` sums vanish per generation, and there are 4 doublets (no Witten anomaly). Adding `ν^c (1,1,0)` changes none of them | **BUILT** |
| C9 | P14:898 (Y7) | `nc_nariai_max`: `x(1 − x²) ≤ 2/(3√3)` for `x > 0`, with equality exactly at `x = 1/√3`. The proof is the factorisation `2√3/9 − x(1−x²) = (x − √3/3)²(x + 2√3/3)` | **BUILT** |
| C10 | P14:894 (Y4) | `nc_dirac`, detailed after the table | **BUILT** |
| C11 | P14:368 | `nc_reflections`: `det P = det T = −1` and `det R = det PT = 1` | **BUILT** |
| C12 | P14:894 (Y3) | `nc_selfdual_swap`, detailed after the table | **BUILT** |
| C13 | P14:894/898 (Y3, Y6) | `nc_det_real`, detailed after the table | **BUILT** |
| C14 | SYN:2804 | `nc_four`: if `P` is an involution taking left states to right states, any `P`-closed set containing a two-element left set has at least 4 elements, and `L ∪ P(L)` has exactly 4. Witnessed by `nc_four_witness` | **BUILT** |

**C10 in detail (`nc_dirac`).** In the Dirac basis over `ℂ`:
- `Γ = γ¹γ²γ³` and `γ⁵ = iγ⁰γ¹γ²γ³`, and the ten Clifford relations hold;
- `Γᴴ = Γ` and `Γ² = 1`;
- `Γᴴγ⁰Γ = −γ⁰`, so the scalar mass reverses, and `Γᴴ(γ⁰γ⁵)Γ = γ⁰γ⁵`, so the pseudoscalar is kept;
- `γ⁵Γ = iγ⁰`, and `γ⁰` keeps the scalar mass and reverses the pseudoscalar.

**C12 in detail (`nc_selfdual_swap`).** `p = diag(1,−1,−1,−1)` lies in `O(4)` with determinant `−1`. Conjugation by
`p` carries each self-dual generator to minus its anti-self-dual partner, and back. The rotation `diag(1,1,−1,−1)`
keeps each self-dual generator, up to sign.

**C13 in detail (`nc_det_real`).** For `n × n` complex `A`, any `C` and real `v_L, v_R`:
`det [[0, v_L A], [v_R Aᴴ, C]] = (−1)ⁿ v_Lⁿ v_Rⁿ |det A|²`, so it is real. Two supporting lemmas:
- `nc_det_swap`: the block swap has determinant `(−1)ⁿ`, by the factorisation `diag(−I, I)·L·U·L` into block
  triangles;
- `nc_det_zero11`: `det [[0, B], [C, D]] = (−1)ⁿ det B det C`.

The non-vacuity witness is `nc_det_witness` (`n = 1`, giving `−6`).

## Against the registration

- **All fourteen rows are built**, so the joint event (p 0.5) held.
- **The named stop, C13 (p 0.75), did not hold.** Mathlib has no zero-`(1,1)` block lemma and no sign of the block
  swap as a permutation, so the swap's determinant is computed through a product of block triangles.
- **One change of method, inside C10.** `decide` over Gaussian-integer matrices timed out. The identities are proved
  over `ℂ` instead, entry by entry, each as its own lemma, with `Γ` and `γ⁵` written out and identified with their
  products.
- **One arithmetic correction to the census.** It quoted `0.9918² − 1` as `−0.01632776`; it is `−0.01633276`. It
  still prints as `−0.0163`, and C4 states the correct value.
- **Size:** 477 lines, in band (estimate 450).

**Mathlib gap: none found.**

## For 69

These are the first Lean rows for P14's L550 line (Y1–Y4, Y6–Y8), for P15's r²−1 and `ℓ_D/√α` statements, and for
P18's anomaly and closure sentences. Whether and where the papers cite them is 69's to rule. The papers are not edited
here.

The two arithmetic notes in `PREDICTION.md` stand for P15's owners:
- l.258 prints "2.0σ" for `2.06`;
- l.917 prints `0.44%` for `0.41%`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
