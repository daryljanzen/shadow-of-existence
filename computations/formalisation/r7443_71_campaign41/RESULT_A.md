# `r7443+71.27` — RESULT: campaign 41 BUILT. ⌗ Row 70: the formal second-order energy `(6g₄w² − 11g₃²)/(8w⁴)` on EVERY ladder truncation, the cubic's own completion `g₄ = 11g₃²/(6w²)` as the unique zero locus, closed de Sitter's eight dimension-six scalars and vanishing Weyl tensor on THE Levi-Civita connection, and the Bianchi I control. ⌗ `1407` lines against `800` (band 450–1400, MISSED HIGH by `7`). ⌗ Row 70 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.26` before any Lean was written. It is not
revised. `probes/Row70Quartic.lean` builds with no error and no warning. All 41 theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `233 s`). No `native_decide`; rational evaluations use
`decide +kernel`. The build was done by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `1407` lines, under `1900`. ***The band is missed high by `7` lines*** and recorded as it stands.
The overrun is the copied FRWk curvature-table lemma (`frw_tab_k`) the de Sitter section needs, because probes
cannot import each other.

## What was built

All matrices are `(N+4)×(N+4)` truncations for every `N` (the receipt's sizes 8, 12, 16, 18 are instances); `ħ = 1`.

| part | theorems | what they prove |
|---|---|---|
| A | `dE2_closed`, `dE2_receipt_sizes`, `conj_zero`, `conj_q3`, `conj_q3qpq` | `dE₂ = ⟨H₄⟩ − Σ_{s≠0}\|⟨s\|H₃\|0⟩\|²/(E_s−E₀) = (6g₄w² − 11g₃²)/(8w⁴)` on every truncation. For ANY Hermitian `A`, `H₃ = i[A,H₀]`, `H₄ = −[A,[A,H₀]]/2` gives `dE₂ = 0`, proved in general. `A = q³` and `A = q³ + qpq` give channels `27/(8w²)` and `27/(8w²) + 19/8`, both nonzero |
| B | `gen_solves`, `fake_vev`, `fake_zero`, `deviation`, `cubic_nonres`, `fake_receipt`, `locus` | for any non-resonant Hermitian `H₃`: `i[A,H₀] = H₃`, `⟨H₄fake⟩` equals the cubic channel, `dE₂(H₃,H₄fake) = 0`, and `dE₂ = ⟨H₄ − H₄fake⟩`. Non-resonance by parity. `⟨H₄fake⟩ = 11g₃²/(8w⁴)`; `dE₂ = 0 ⟺ g₄ = 11g₃²/(6w²)`, with `∂/∂g₄ = 3/(4w²) ≠ 0` |
| C | `no_cancellation`, `pure_cubic_even`, `g3_derivs`, `trace_cube`, `trace_cube_cases` | every cubic-channel term `≥ 0`, nonzero exactly at `s = 1, 3` (`9/8`, `2/8` of `g₃²/w⁴`); pure cubic `−11g₃²/(8w⁴)`, even in `g₃`; `tr h³ = 3 det h` for traceless 3×3 over any commutative ring |
| D | `bookkeeping`, `frw_tab_k`, `fRk_maxsym`, `closed_dS`, `ms_q`, `frame_values`, `frame_weyl`, `eight_homogeneous`, `RiemQ_eq`, `RlT_bi`, `bianchi_connection`, `bi_scal`, `bi_gradient`, `bi_q`, `control`, `ratios_distinct` | closed de Sitter `a = α cosh(T/α)` on the engine's `lcConn` via `curvD_eq`: all 256 components maximally symmetric with `K = 1/α²`, `R = 12/α²`; the eight scalars `(64, 16, 4, 32/3, 4, 8/3, 16/9, 8/9)Λ³`; Weyl `≡ 0`, so `C²` and both cubic Weyl contractions vanish. Bianchi I `diag(−1,T²,T⁴,T⁶)` at `T = 1`, on THE connection (`curv_T`): `C² = 28/3`, cubic contractions `40/9` and `20/9`, `R = 38/T²`, `R′(1) = −76`, all 8 ratios to de Sitter distinct |
| E | `derivative_test`, `gauge_ratio`, `combo_homogeneous` | the homogeneity checks; `α/ℓ_P` has nonzero `Λ`-derivative |
| F | `ranks`, `residue_scheme`, `cited_bound`, `any_target` | ranks `1` against `2`; `H_M − log M → γ`, `H_M − log 2M → γ − log 2`; the arithmetic; solving `dE₂ = target` for `g₄` |

## Caveats, beside the score

- ***`dE₂` is the receipt's formal formula on finite matrix elements, not an eigenvalue***, as registered: the
  cubic oscillator is unbounded below. The docstring says so.
- ***Imported, as registered:*** the `r6990` bound and the `1/60` (cited constants); the TT spectrum `m² − 1`,
  `2(m² − 4)`, `6π² det h` (data in E only). The closed-slicing profiles `sin²χ`, `sin²θ` are hypotheses near the
  point and nowhere zero, as FRWk has them. The paper-text checks are not formalised.
- ***De Sitter's `∇R`*** is shown only as `R` constant at every admissible point; there is no separate gradient
  theorem.
- ***The Bianchi I profiles are smoothed below `T = 1/2`*** so the engine's everywhere-nondegenerate hypothesis
  holds; they are unchanged near `T = 1`.
- ***One discrepancy, in the agent's own cross-check and not in the receipt:*** a first sympy value of the
  control's sixth scalar dropped inverse-metric factors and the kernel refused it. With the receipt's definition it
  is `4080`, not `2800`; the eight ratios stay distinct, so the receipt's conclusion stands.
- ***Peak memory about 6.3 GB***, from `frw_tab_k`.

## The library-gap label, read

Row 70 carried `LIBRARY GAP: spectral theory`. ***What it needed was not in fact a spectral library:*** the
receipt's checks are a formal formula on finite ladder truncations, curvature on the engine's own
pseudo-Riemannian Levi-Civita connection, and imported TT data. The spectral content (the TT spectrum) enters as
cited data in E, as it does for row 73, which is `DONE` on the same terms. That reading goes to the class finding
`r7453_71_gap_class/`.
