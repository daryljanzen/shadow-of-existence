# `r7443+71.31` — RESULT: campaign 43 BUILT. ⌗ The transgression identity `∂_μK^μ = −√−g *RR` for the engine's Levi-Civita connection of ANY smooth nondegenerate metric on `ℝ⁴`, at every point where `det g < 0`. ⌗ The receipts' measured ratio `−1` (rows 89 Part 8, 96 Part 3) is now a theorem for every such metric with `*RR ≠ 0`. ⌗ `1000` lines against `550` (band 300–1000, IN BAND at the edge). ⌗ p `0.45` came true

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.29` before any Lean was written. It is not
revised. `probes/Transgression.lean` builds with no error. All 9 headline theorems print `[propext,
Classical.choice, Quot.sound]` (`PROBE_RUN_A.txt`, `15 s`). No `native_decide`. The build was done by a delegated
agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired.*** `1000` lines, under `1500`. About 330 lines are row 96's `formG … csLC` machinery, copied
verbatim because probes cannot import probes.

## The verdict, against the registration's own definitions

The registration defined BUILT as "algebraic layer, bridge and corollary". It defined BUILT IN PART as "the
algebraic layer without the bridge". ***Both the layer and the bridge are built, so the verdict is BUILT.*** The
delegated agent reported "BUILT IN PART" because of how far the corollary goes; that limit is recorded below as a
caveat, not as the verdict.

## What was built

| layer | theorems | what they prove |
|---|---|---|
| algebraic | `transgression_alg` | for ANY `Γ : Fin 4 → Matrix (Fin 4) (Fin 4) ℝ`, any `dΓ`, any `ddΓ` symmetric in its derivative slots, with `F_{μν} = ∂_μΓ_ν − ∂_νΓ_μ + [Γ_μ,Γ_ν]`: `Σ ε^{mnrs} tr(F_{mn}F_{rs}) = 4 Σ_μ ∂_μ[ε^{μνρσ} tr(Γ_ν∂_ρΓ_σ + ⅔Γ_νΓ_ρΓ_σ)]`. ***Proved without expanding into components***: one reindexing lemma applied to six permutations, trace cyclicity, the quartic term killed by the odd 4-cycle, and the `∂²Γ` term killed by Schwarz symmetry. The registered risk (ε-sum cost) did not occur |
| bridge | `Fc_eq_curv`, `L1_pair`, `pont_tab`, `csArr_eq_CS`, `div_csLC`, `transgression` | on the engine's `lcConn`: `F` is the engine's `curv` on coordinate fields. `√−g · pontArr = −½ Σ ε tr(FF)`; the sign is ***derived*** from pair symmetry and first-pair antisymmetry (metric compatibility) of the lowered curvature, not chosen. `K = 2 CS`, and `div K = 2 Σ ∂CS` via Fréchet derivatives of the Christoffel symbols and `isSymmSndFDerivAt`. ***Result: `Σ_μ ∂_μ csLC^μ = −√(−det g) · pontryaginLC`*** |
| corollary | `ratio_neg_one`, `plane_divergence` | `(Σ ∂K)/(√−g *RR) = −1` for every metric and point with `det g < 0` and `*RR ≠ 0`. Row 96's `member_divergence`, stated for ANY metric on the `(t,z)` plane: if `K^x`, `K^y` vanish near the point, then `∂_tK^t + ∂_zK^z = −√−g *RR` |

## Caveats, beside the score

- ***`det g < 0` at the point is a hypothesis.*** `pontryaginLC` divides by `√(−det g)`, which Lean sets to `0`
  when `det g > 0`. So the identity as stated holds for Lorentzian signature at the point, not for signature (2,2).
- ***The member corollary specialises; it does not re-run.*** `plane_divergence` takes as hypotheses exactly what
  row 96's `member_cs` and `member_pontryagin` prove on its member. Re-proving those here would mean copying about
  700 lines of row 96's Gowdy tables, which would pass the stop.
- Coordinates on `ℝ⁴` only; the coordinate-free `d CS = tr(R ∧ R)` and covariance of `K` are not claimed, as
  registered.
- ***Independent numeric check*** (the agent's, on a random cubic Lorentzian metric): `∂K = 6.68657`,
  `√−g *RR = −6.68657`, ratio `−1.000000000`.

***Census:*** none moves, as registered. This is a foundation. It is the piece `r7453_71_gap_class/CLASS.md` ⓒ
priced. Mathlib has no counterpart; see that file's search table.
