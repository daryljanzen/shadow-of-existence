# `r7443+71.33` — RESULT: campaign 42 BUILT. ⌗ Row 96: the Pontryagin density and the Chern–Simons current on THE Levi-Civita connection, both zero on every warped (spherically symmetric) metric, `K^φ` included; Nariai and rotated Nariai, polarised Gowdy, the plane wave; the member's `∂K = −√−g *RR` and Stokes on `[3,5]×[0,1]`. ⌗ `2060` lines against `900` (band 500–1600, MISSED HIGH by `460`). ⌗ p `0.35` came true. ⌗ Row 96 → `DONE`

*Scored against `PREDICTION.md` in this directory, pushed at `r7443+71.26` before any Lean was written. It is not
revised. `probes/Row96ChernSimons.lean` builds with no error. 33 theorems print `[propext, Classical.choice,
Quot.sound]` and `net_count` prints `[propext]` (`PROBE_RUN_A.txt`, `1711 s`). No `native_decide`. The build was
done by a delegated agent and re-run by 71 before this record.*

## ⛔ The stop, scored

***Not fired, by `40` lines:*** `2060` against `2100`. ***The band is missed high by `460`*** and recorded as it
stands. The excess has three sources:
- about 650 lines of engine and row 69 Gowdy machinery, copied because probes cannot import probes;
- about 400 lines of the parity framework, which the registration did not foresee;
- two sets of curvature tables.

## What was built

| receipt check | theorems | status |
|---|---|---|
| definitions | `eps4_sign`, `eps4_det`, `sum_eps`, `pontryaginLC_eq`, `riemLC_tab`, `csLC_tab`, `tabs_bridge` | `*RR` and `K^μ = 2ε(Γ∂Γ + ⅔ΓΓΓ)` on THE connection, equal to the receipt's coordinate recipe |
| structure | `pontryagin_parity`, `cs_parity`, `csArr_three`, `warped_pontryagin`, `warped_cs` | a coordinate set that does not mix and on which nothing depends kills `*RR` when it is odd, and kills `K^μ` when the parity does not match. Hence `*RR ≡ 0` and all four `K^μ ≡ 0` on every warped metric |
| Part 1 | `nariai_pontryagin_zero`, `nariai_apply`, `nariai_rotated_pontryagin_zero`, `nariai_general_pontryagin_zero` | Nariai and rotated Nariai `*RR = 0`; the general form allows any `a(χ), b(χ), c(θ), e(θ), w` |
| Part 2 | `polarised_pontryagin_zero`, `unpolarised_nonzero`, `GW_apply`, `gowdy_pontryagin`, `gowdy_cs`, `gowdy_plane_wave_pontryagin`, `gowdy_areal_pontryagin`, `gowdy_areal_silenced`, `areal_profile_exists` | polarised Gowdy is `0` for arbitrary `A, ψ, R`; one unpolarised member gives `*RR = −7/16`; the plane wave gives `0` at `R = 1`, a nonzero value at `R = t`, and `0` when either channel is silenced; plus the closed-form current |
| Part 3 | `GM_apply`, `member_cs`, `member_pontryagin`, `member_divergence`, `member_stokes`, `member_volume` | on the member, `K^x = K^y = 0` and `√−g *RR = −8u/t²`. `∂_tK^t + ∂_zK^z = −√−g *RR` on the open region. Volume equals minus the boundary flux, by Mathlib's `integral2_divergence_prod_of_hasFDerivAt_off_countable`. Value `8/15 − 8 log(5/3) < 0` |
| Part 4 | `sph_pontryagin_zero`, `sph_cs_zero` | `*RR ≡ 0` and all four `K^μ ≡ 0`, ***`K^φ` included***. The registration had named `K^φ` the likeliest gap |
| Part 6 | `net_count` | `3 × 0 = 0` |

***Since campaign 43*** the ratio `−1` is a theorem for every metric, not only for the member: `ratio_neg_one` in
`probes/Transgression.lean`.

## Caveats, beside the score

- ***The engine needs a metric that is globally smooth and nondegenerate on `ℝ⁴`.*** So `sin²θ`, `1 − χ²`,
  `log(t − z)` and `R = t` enter as global profiles that equal them where the checks are made:
  - Part 4: any nowhere-zero `h(θ)`;
  - Part 1: any positive `f, h`;
  - Part 3: an explicit smoothed `ρ` equal to `t` for arguments `≥ 3/2`.
- ***"Unpolarised ≠ 0"*** is an exhibited member, not the receipt's general symbolic nonvanishing.
- Covariance is not proved. The seven paper-text checks are not formalised.
- ***Peak memory about 7.9 GB*** with `Elab.async false`, from the 256-entry Gowdy `∂Γ` table. It was accepted
  rather than split, because splitting would cost about 150 lines and pass the stop.
- ***Lean against the receipt: no disagreement.***
