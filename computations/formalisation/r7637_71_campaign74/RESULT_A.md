# `r7637+71.3` — RESULT: campaign 74, `r7637` ④, the slice lower limit `𝓗⁺ ⊆ KLi(S_τ)` BUILT, and so `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`, with `Θ` temporal on `D` only, under a stated properness hypothesis and local connectedness at `𝓗⁺`; properness from the Cauchy property REPORTED, and argued to be a genuine extra hypothesis. ⌗ `776` lines in one probe (about `345` new, band 150–1500 new). ⌗ p: blow-up `0.5` and slice lower limit `0.45` came true, each from its stated hypothesis

*Against `PREDICTION.md` (`r7637+71.2`). 71 re-ran `lake env lean probes/SliceConvergence.lean`. It exits 0 with no
errors. All `44` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`. The probe is campaign 72's,
copied in, together with campaign 60's `IsCauchyTemporal` and `ExteriorGH` definitions.*

## Extra: `Θ` temporal on `D` only

- `sc_temporalD_chr`: a function temporal on `D` (as a spacetime in its own right) increases along `x ≪ y` whenever
  `y ∈ D`.
- The reason is that a timelike step ending in `D` stays inside `D` (`sc_D_of_chr`, `tstep_tail`).
- This closes campaign 72's gap, which had needed `Θ` temporal on all of `M`.

## ① `Θ → ∞` at `𝓗⁺`, from properness

***The hypothesis.*** `SublevelProper J Θ` says `closure {x ∈ D | Θ x ≤ T} ⊆ D` for every `T`.
- `sc_sublevelProper_iff`: for continuous `Θ`, this is the same as each sublevel set being closed in `V`.
- `sc_sublevelProper_iff_tendsto`: it is exactly `Θ → ∞` along `𝓝[D] p` at every `p ∉ D`.

***The conclusion.*** `sc_blowup_H` and `sc_tendsto_atTop_H` give the registered form: near every horizon point, `Θ` is
large on `D`.

***REPORTED: deriving properness from the Cauchy property.***
- The Cauchy property gives `Θ → ∞` along every causal curve of `D` that runs into `𝓗⁺`.
- Going from those curves to arbitrary approaches needs limit curves.
- The build argued that properness is a genuine extra hypothesis and not a consequence. The argument is on paper and
  is not formalised:
  - Schwarzschild `t` is Cauchy temporal on region I, yet every `t`-level reaches the bifurcation sphere.
  - Whether that sphere lies in this `𝓗⁺` depends on how `𝒥⁺` and `D` are set up.
- **This bears on the paper's use of "Cauchy temporal", and 69 may want to weigh it.**

## ② The slice lower limit

***The hypothesis.*** `LocConnAt J p` holds at every `p ∈ 𝓗⁺`: every neighbourhood of `p` contains one, `W`, with
`W ∩ D` preconnected.

***The proof.*** Pick a point of `W ∩ D`. By ①, `Θ` is arbitrarily large on `W ∩ D`. Then the intermediate value
theorem on the preconnected set `W ∩ D` gives every large level.

***Theorems.***
- `sc_mem_KLi_slice` (pointwise).
- **`sc_slice_lower_limit`**: `𝓗⁺ ⊆ KLi(S_τ)`.
- `sc_slice_lower_limit_exists` and `sc_slice_lower_limit_seq`: the registered and sequence forms.

## ③ `KLi(S_τ) = KLs(S_τ) = 𝓗⁺`

- `sc_slice_kuratowski`: the general form.
- **`sc_slice_kuratowski_temporalD`**: the paper's setting, with `Θ` temporal on `D` only and adapted to the observer
  (`Θ(O τ) = τ + c`). The increase along `≪` is derived, not assumed.

***Hypotheses, in full.***
- From campaign 72: the observer hypotheses, `hcl` and `hint`.
- `hadapt`.
- `SublevelProper`.
- `LocConnAt` at `𝓗⁺`.

***Not attempted.*** Deriving local connectedness of `D` at `𝓗⁺`.

No census row moves.
