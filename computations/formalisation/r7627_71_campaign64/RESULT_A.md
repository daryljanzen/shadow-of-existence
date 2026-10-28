# `r7627+71.3` — RESULT: campaign 64, `r7627` ②, the local `FlowData` constructor BUILT; the flow-box chart on a manifold BUILT, with the field's `C¹` hypothesis in chart form. ⌗ `968` lines in one probe (registered `700`, band 200–2000). ⌗ both registered p came true (`0.7`, `0.35`)

*Against `PREDICTION.md` (`r7627+71.2`). 71 re-ran `lake env lean probes/FlowLocal.lean`. It exits 0 with no
errors. All `44` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. Campaign 62's flow machinery
is copied in under `fl_` names.*

## ① The local constructor, by the registered cutoff route

***The pieces.***
- `fl_cutoff`: if `ContDiffOn ℝ 1 f (ball x₀ ρ)`, there is a global `C¹` field `g = χ•f`, with `χ` a
  `ContDiffBump` with radii `ρ/4` and `ρ/2`, such that `g = f` near every point of `ball x₀ (ρ/4)`.
- `fl_flowData_small`: flow data for a global field with an arbitrarily small trajectory ball. The speed bound
  keeps trajectories inside it.
- `fl_agree`, `FlowData.transfer` and `fl_transfer_isFlowBox`: flow data for `g` is flow data for `f`, and its
  flow-box chart is a flow-box chart for `f`.

***The constructor.*** `fl_flowData_exists_of_contDiffOn : ContDiffOn ℝ 1 f (ball x₀ ρ) → ∃ D : FlowData f x₀,
D.R < ρ/4`. This is the declaration campaign 62 named as missing.

***The usable form.*** `fl_flowBox_chart_of_contDiffOn` gives, when `f x₀ ≠ 0`, a chart `Φ` with:
- `Φ(0,0) = x₀`, and `Φ` maps into `ball x₀ (ρ/4)`;
- `Φ` is `C¹`, with `DΦ(0,0)(a,h) = a·f x₀ + h`;
- `DΦ·(1,0) = f∘Φ` on the source;
- `Φ⁻¹` is `C¹` near `x₀`.

## ② The flow-box chart on a manifold

***Setting.***
- `N` is a `C¹` manifold modelled on `E`, and `X` is a vector field, a section `Π x, TangentSpace x`.
- `chartRep X p` is `X` pushed forward by `extChartAt p` through `mfderiv`.
- `fl_chartRep_inv` recovers `X` from it through the chart's inverse.

***`fl_manifold_flowBox`.*** If `chartRep X p` is `C¹` on the chart target and `X p ≠ 0`, there is a flow box `Φ`
for which `ψ = (extChartAt p).symm ∘ Φ` satisfies:
- `ψ(0,0) = p`;
- `mfderiv ψ q (1,0) = X(ψ q)` on the source, i.e. `X = ∂_λ` in the chart `ψ⁻¹`.

***Scope.***
- `X`'s `C¹` hypothesis is stated in chart form, on `chartRep`, not as `ContMDiff` of the section.
- No Mathlib declaration is missing for the section form. The translation through `contMDiffAt_section` and the
  tangent-bundle trivialisation is simply not written.
- The link to a local version of campaign 59's `KillingChart`, and the coordinate-free Killing part on `N`, are not
  written.

No census row moves.
