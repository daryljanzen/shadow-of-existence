# `r7827+71.1` — CENSUS AND PRE-REGISTRATION: the claims the papers have gained since the closing table, and campaign 144 on the cheapest. ⌗ `450` new lines (band 300–750), p(C1–C14 all BUILT) `0.5`

*The order is 69's `r7827`: ① census every machine-checkable claim added to any paper since the closing table, with
its formal core named or the reason it has none; ② price them; ③ register and build the cheapest. The census reads
`git diff 6ea3358c8 origin/main` over `corpus/*.tex`. `6ea3358c8` is r7805, which merged the closing table. Two
read-only passes produced the census, and I confirmed the cored rows against the lines cited. Registered before any
Lean. The probe will be the new standalone `probes/NewClaims.lean` (`nc_`), importing only Mathlib.*

## ① and ② The census, priced

**Changed since the table:**
- the paper texts of P15 (`CR_cosmology`), P18 (`CR_synthesis`), P14 (`matter_sector_paper`), P7, P13, P11, P12 and
  P17;
- the receipt appendices, regenerated, which hold no new claims.

Most of P15's and P18's additions replace one fitted, Boltzmann-code or χ² number with another. Those are
**empirical, with no formal core**, and the receipts check them numerically. P14's L550 line (Y1–Y9) carries most of
the cored claims.

### Cored, cheapest first

These are campaign 144's rows.

| Row | Paper:line | Claim | Formal core | Lines | p |
|---|---|---|---|---|---|
| C1 | P14:892 (Y2) | "sixteen in all" | `3·2·2 + 1·2·2 = 16`; also `dim (4,2,1) + dim (4̄,1,2) = 16` | 5 | 0.99 |
| C2 | P14:368 (Y1) | "`Λ_YM = μ e^{−1/2b₀g²}` lies below `μ` for every `g² > 0`" | for `μ, b₀, g² > 0`: `μ · exp(−1/(2 b₀ g²)) < μ` | 10 | 0.99 |
| C3 | P14:896 (Y4) | "`f(−r;M) = f(r;−M)` … `f(−r;M) − f(r;M) = 4M/r`" | with `f(r;M) = 1 − 2M/r − r²/α²`, `r ≠ 0` and `α ≠ 0`: both identities | 15 | 0.99 |
| C4 | P15:594–595 | "`r² − 1` is `−0.0163` … against `+0.1938` … one part in `11.9`, with the opposite sign" | `0.9918² − 1 < 0 < 1.0926² − 1`; both round as printed; the ratio lies in `[11.85, 11.95]` | 15 | 0.98 |
| C5 | P14:896 (Y4) | "`(t, r) ↦ (t, −r)` … all four characters carried onto itself, the Standard Model's sent to states it lacks" | on `{±1}²`: the full set is invariant; the SM occupation (`T ∈ {+1, −1}` on one chirality, `{+1, +1}` on the other) is not | 25 | 0.95 |
| C6 | P15:580–582 | "`α` and `ℓ_D` enter the signature only through `ℓ_D/√α`" | for `α, ℓ_D > 0`: `exp(−α (ℓ/ℓ_D)² (r²−1)) = exp(−(ℓ/(ℓ_D/√α))² (r²−1))`; and `|1951.9/√1.7 − 1497.04| < 0.005` | 40 | 0.9 |
| C7 | P14:892 (Y2), SYN:3077 (Y8) | "`diag(1,1,1,−3)` traceless … `Q = I₃L + I₃R + c(B−L)` returns every Standard Model charge, in thirds" and "the singlet carries `B−L`" | a finite ℚ table of the 16 states: trace `0`; with `B−L = T/3` and `c = 1/2`, every `Q` is the SM value; splitting by `I₃R` returns each hypercharge `Y = 2(I₃R + (B−L)/2)`; `ν_R` has `Q = Y = 0`, `B−L = −1` and `I₃R = 1/2` | 60 | 0.9 |
| C8 | P14:607, 610, SYN:2802 | "the index and the anomaly conditions being blind to the difference" / "contributing exactly zero on every channel" | the six per-generation SM anomaly sums (`SU(3)²Y`, `SU(2)²Y`, `grav·Y`, `Y³`, `SU(3)³`, the Witten parity) vanish, and the singlet `(1,1,0)` adds `0` to each | 50 | 0.9 |
| C9 | P14:898 (Y7) | "`2M/α = 2/(3√3)` … the largest value the order parameter takes" | `max over x > 0 of x(1 − x²)` is `2/(3√3)`, attained only at `x = 1/√3` | 40 | 0.9 |
| C10 | P14:894 (Y4) | "`γ¹γ²γ³` reverses the sign of a scalar Dirac mass and keeps a pseudoscalar one, while its composite with `γ⁵` is proportional to `γ⁰`" | explicit 4×4 Dirac matrices over `ℂ`, with `Γ = γ¹γ²γ³`: `Γᴴγ⁰Γ = −γ⁰` and `Γᴴγ⁰γ⁵Γ = γ⁰γ⁵`; `γ⁰`'s: `γ⁰ᴴγ⁰γ⁰ = γ⁰` and `γ⁰ᴴγ⁰γ⁵γ⁰ = −γ⁰γ⁵`; `γ⁵Γ = u·γ⁰` for a unit `u` | 80 | 0.85 |
| C11 | P14:368, 894; P12 | "of the three reflections `P` (three legs) and `T` (one) reverse the cut's orientation, `R` does not" | the diagonal reflections `P = diag(1,−1,−1,−1)` and `T = diag(−1,1,1,1)` have determinant `−1`, `R` has determinant `1`, and `PT` has determinant `1` | 20 | 0.95 |
| C12 | P14:894 (Y3) | "determinant `−1` in `O(4)` and carries the self-dual generators of `so(4)` onto the anti-self-dual ones, … where a rotation keeps each" | for `p = diag(1,−1,−1,−1)`: `det p = −1`, `p ∈ O(4)`, and conjugation by `p` maps each `e₁₂+e₃₄`, `e₁₃−e₂₄`, `e₁₄+e₂₃` into the anti-self-dual span and back. A rotation's half (`diag(1,1,−1,−1)`) keeps each span | 70 | 0.85 |
| C13 | P14:894, 898 (Y3, Y6) | "the phase of the quark mass determinant is then zero for any complex couplings … whatever the singlet masses" | for `A : Matrix (Fin n) (Fin n) ℂ`, real `v_L, v_R` and any `C`: `det [[0, v_L A], [v_R Aᴴ, C]] = (−1)^n v_Lⁿ v_Rⁿ ‖det A‖²`, which is real | 70 | 0.75 |
| C14 | SYN:2804 | "smallest colourless content containing the left-handed doublet that it carries onto itself is four" | an involution sending left states injectively to right states: any set it carries onto itself that contains a two-element left set has at least 4 elements, and 4 is attained | 30 | 0.9 |

**C13 is the expected stop**, at p 0.75. Mathlib proves the block determinant only for triangular blocks, so the
zero-`(1,1)`-block case needs a reindexing by the swap of the two summands.

### Cored but out of reach, or not chosen

- **P14:368, `π₃(SU(3)) = ℤ` and `π₄(SU(3)) = 0`.** These are exact but cite Bott. Mathlib has no homotopy groups of Lie
  groups. Beyond.
- **P14:892, `Spin(6) = SU(4)` and `SO(4) = (SU(2) × SU(2))/ℤ₂`.** These are cited classical isomorphisms. Mathlib has
  no spin groups. Beyond, at 1–3k lines.
- **P14:368, "`θ ∫ tr F∧F` changes sign under any orientation-reversing map".** The full statement is the pullback of a
  top form, about 300 lines at p 0.4. C11 is its determinant core.
- **P14:894, "the tied couplings still carry a CKM phase".** This needs an explicit witness with a nonzero Jarlskog
  invariant, about 120 lines at p 0.6. Not in this campaign.
- **P14:898 (Y6), "vacua at `±v`, exchanged by `P`, splitting odd in `σ`".** The toy core is the zeros of
  `λ(σ² − v²)²`; the physics reading is interpretive. Not chosen.
- **P12/P17/SYN (Y5), "`RP` lies in the same component" of `O(5,1)`.** Its invariant core is determinants and time
  orientations, about 25 lines and partly covered by C11. That the invariants decide the component needs `SO₀(5,1)`
  connected, which Mathlib lacks. Beyond.
- **P15:258, the `N_eff` and `T_dec` arithmetic (`(M_{W_R}/M_W)^{4/3}`, `3(10.75/g)^{4/3}`).** The scaling laws are
  physics input, so only the arithmetic would be cored, at 40–90 lines with `rpow` bounds. Not chosen.

### No formal core

- P15's χ², σ, refit, Boltzmann-code and MCMC values (e.g. P15:571–607, 137–296, 2144–2200), and P18's Y8/Y9 dilution
  and X-ray limits: **empirical**.
- P14's `Λ_MS ≃ 238 MeV`, `10^{41.3}`, the `2 × 10⁸` and `2 × 10¹³` GeV bounds, and the ATLAS factor of thirty:
  **empirical or estimates**.
- The physics readings that P is the left–right parity, and that the construction's datum is of the doublet kind:
  **interpretive**.

### Arithmetic noted while checking, for 69

These are not cored; they are recorded so the papers' owners can look.
- **P15:258** prints "between 1.1 and 2.0 standard deviations". `(3.34 − 2.99)/0.17 = 2.06`, which rounds to 2.1.
- **P15:917** prints `0.44%`. `0.009/2.212 = 0.41%`. The receipt may use unrounded inputs.

## ③ Campaign 144: C1–C14, as above

Every row's hypotheses are explicit and satisfiable; the concrete rows are their own witnesses, and each general row
carries an instance. P14, P15 and P18 gain their first Lean rows for the L550 line and the r7823/r7827 P15
statements. Nothing in the papers is edited by this campaign.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
