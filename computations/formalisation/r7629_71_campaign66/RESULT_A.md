# `r7629+71.3` — RESULT: campaign 66, `r7629` ②, the section form BUILT; `lem:killing` (b) on a manifold BUILT as a local Killing chart, with the metric and Killing condition in chart form; the coordinate-free Killing condition REPORTED. ⌗ `1543` lines in one probe (registered `500`, band 150–1500: 43 over the top of the band, from the 968-line copy of campaign 64, and under the `2500` stop). ⌗ both registered p came true (`0.7`, `0.45`)

*Against `PREDICTION.md` (`r7629+71.2`). 71 re-ran `lake env lean probes/FlowManifold.lean`. It exits 0 with no
errors. All `70` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`.*

## ① The section form

- `fm_chartRep_eq_triv` shows that `chartRep X p` is the fibre coordinate of the tangent-bundle trivialisation at
  `p`. The `TangentSpace`/`E` mismatch the registration feared closes by `rfl`.
- `fm_chartRep_contDiffAt_of_section` and `fm_chartRep_ball_of_section`: a tangent-bundle section `C¹` at `p`, in
  the `ContMDiffAt … 𝓘(ℝ,E).tangent` sense, gives `chartRep X p` `C¹` at `φ p` and on a ball around it. This works
  on a `C¹` manifold.
- `fm_chartRep_contDiffOn_of_section`: a section `C¹` on the chart source gives `C¹` on the whole chart target. This
  needs a `C²` manifold.
  - Mathlib's tangent bundle is a `C¹` vector bundle only from `C²` onward.
  - This is a mathematical limit, not a missing declaration: on a `C¹` manifold the chart changes' derivatives are
    only `C⁰`.
- `fm_manifold_flowBox_section` and `fm_manifold_flowBox_sectionOn`: the manifold flow-box chart, with
  `mfderiv ψ q (1,0) = X(ψ q)`, now holds under the section hypothesis. The chart-form hypothesis is gone.

## ② `lem:killing` (b) on a manifold

***Localized Killing results on `E`.*** `fm_flow_isometry_loc` and `fm_flowBox_pullback_loc` need the Killing
equation only on the trajectory ball. `fm_flowBox_killing_of_contDiffOn` gives the local flow box with a
`λ`-independent pulled-back metric.

***The chart record.*** `LocalKillingChart X p gc` is the local form of campaign 59's `KillingChart`. It is a chart
`ψ` around `p` with:
- `mfderiv ψ q (1,0) = X(ψ q)`;
- the metric pulled back through `ψ` depends only on the transverse coordinate;
- `fm_lambda_indep`: `∂_λ g_ab = 0`.

***The theorems.*** `fm_manifold_killingChart` and `fm_manifold_killingChart_section`: if `X` is `C¹` as a section
at `p`, `X p ≠ 0`, and the chart-form metric `gc` satisfies the Killing equation for `chartRep X p` on the chart
target, then a `LocalKillingChart` exists. This is `lem:killing`'s adapted chart, derived on a manifold rather than
assumed.

## REPORTED: the coordinate-free Killing condition

The metric is `gc` on the chart target, and the Killing equation is `IsKilling` for the chart representative.

***First missing declaration:*** a Lie derivative of `(0,2)`-tensor fields on a manifold. Mathlib has none, and
`LieDerivProbe`'s `lieDerivForm` is defined only through test fields. Nothing else is missing.

## Census

`lem:killing` is a P1 theorem, not a `ROWS.tsv` row, and all 111 rows are `DONE`. **No census row moves**, as
`r7629` asked to be told.
