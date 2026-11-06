# `r7693+71.1` — PRE-REGISTRATION: campaign 108, `r7693` ①, **8ii-e by conformal invariance: on the shell model, the retarded slicing's slices accumulate on `𝓗⁺` and nowhere else (`KLi = KLs = 𝓗⁺`) with properness, and so do the past cones. This is proved on the flat `−dũ dv` on `M′`, which is `C^∞`, and carried unchanged to the `C⁰` shell.** ⌗ `400` new lines (band 200–900), p `0.65`. **Expected stop:** the adapted reparametrisation of the observer, since `mh_causal_alignment_gh_N` needs `Θ(O τ) = τ + c`

*Registered before any Lean. The new probe is `probes/ShellAccumulation.lean`, a copy of campaign 105's
`ShellMatter.lean` (which carries `sh_` and `sm_`). Everything new is prefixed `sa2_`.*

*② of `r7693`, the pointer fix, is done in this PR. `StationaryHorizon.lean` and its copy `NullGeodesic.lean` now cite
the rigidity sentence as "the proof of `cor:stationary`" instead of "l.288" (three places in each). These are docstring and comment changes only, and both probes are rebuilt.*

## ① On the flat restriction

- **The spacetime:** `sh_flat = cz_St.restrictM M′`, with `LocallyOneChart` (`cz_locallyOneChart.restrict`) and
  `T2Space`.
- **The causal data:** its `D`, `𝓗⁺`, `Chr` and `J⁻` are campaign 102's (`sh_chr`, `sh_Jpast`, `sh_frontier`).
- **Cauchy:** the retarded slicing is Cauchy temporal on `D` for `0 < η ≤ 2`, by campaign 102's `sh_cauchy_transfer`
  route.

## ② The adapted observer — the expected stop

- `mh_causal_alignment_gh_N` needs `Θ(O τ) = τ + c`. Along `sv_O`, `Θ_shell` is strictly increasing, and it tends to
  `±∞` at the two ends: `sv_O` is an inextendible causal curve in `D`, and the slicing is Cauchy.
- **`sa2_O`:** let `O′ = sv_O ∘ (Θ ∘ sv_O)⁻¹`. Then `range O′ = range sv_O`, so `J` is unchanged. `O′` is still
  chronologically increasing, and `Θ(O′ τ) = τ`.

## ③ The accumulation, carried to the shell

- **`sa2_flat`:** `mh_causal_alignment_gh_N` on the flat restriction gives `SublevelProper`,
  `KLi(slice) = KLs(slice) = 𝓗⁺`.
- **`sa2_flat_cones`:** `mc_cone_kuratowski_N` gives `KLi(cone) = KLs(cone) = 𝓗⁺`.
- **`sa2_shell`:** `sh_S = sh_flat.cz_scale Φ′`. Then `cz_scale_slice`, `cz_scale_H`, `cz_scale_cone` and
  `cz_scale_sublevelProper` carry every clause to the `C⁰` shell, with **`𝓗⁺ = {ũ = u_H}`**.
  - The disjointness of the cones from `𝓗⁺` is optional, through `cd_cone_disjoint`. That function is not in this
    copy; it is about 30 lines to add.
- **Stated plainly:** the shell's `Φ′` never enters, because accumulation is causal. Tangency (`mc_tangency_at_N`)
  does involve `g` and is **not** claimed on the shell.

## Non-vacuity

`sa2_nonvacuous`, with `M = 1`, `v₀ = 0`, `a = 1`, `η = 2`. `𝓗⁺` is non-empty, and a point of `𝓗⁺` with `v < v₀`, in
the flat body, is a limit of slice points.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
