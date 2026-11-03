# `r7665+71.2` — RESULT: campaign 92 ①, **the unbounded-stretch clause BUILT** for every metric inducing `N`'s topology. Compact parts of `𝓗⁺` are eventually inside the ε-stretch, and the ε-stretch leaves every compact set. The futureward direction is BUILT on the 4D witness. The registered stop, the uniformity step, was not hit. ⌗ `6403` lines in one probe (`260` new, band 100–900). ⌗ p `0.8` came true

*Against `PREDICTION.md` (`r7665+71.1`). 71 re-ran `lake env lean probes/HorizonStretch.lean`. It exits 0 with no
errors and no warnings. All `82` `#print axioms` lines read `[propext, Classical.choice, Quot.sound]`: `71` are kept
and `11` are new. The forbidden-token grep is clean. The probe copies campaign 91's `FourDWitness.lean`.*

## The statements

`hs_stretch A H τ ε := {q ∈ H | infDist q (A τ) < ε}`.

***On any metric space.***
- **(S1)** `hs_uniform_on_compact (hH : H ⊆ KLi A) (hε : 0 < ε) (hKH : K ⊆ H) (hK : IsCompact K) : ∀ᶠ τ, K ⊆ hs_stretch A H τ ε`.
  - `hs_uniform_on_compact_pts` is the stronger form: eventually every `q ∈ K` has an actual cone point within `ε`.
- **(S2)** `hs_unbounded (hH) (hnc : ∀ K compact, ¬ H ⊆ K) (hε) (hK : IsCompact K) : ∀ᶠ τ, ¬ hs_stretch A H τ ε ⊆ K`.

***On the manifold.***
- `MSpacetime.hs_stretch_N` takes campaign 88's cone hypotheses (`hL`, `hOD`, `hmono`, `hJM`) and **any metric `m` with
  `m`'s topology `= N`'s**. It gives (S1) and (S2) for `A = S.cone O` and `H = S.H J`.
- The metric is an explicit argument, together with the equation of topologies. This avoids a second topology
  instance on `N`.

***The 4D witness*** (`FourD.hs_witness`).
- `𝓗⁺ = {U = 0}` lies in no compact set.
- (S1) and (S2) are instantiated through `hs_stretch_N`.
- **Futureward:** for every `ε` and `T`, eventually the ε-stretch contains a point with `V > T`.
- For each `q ∈ 𝓗⁺`, `J⁺(q) ∩ 𝓗⁺` lies in no compact set. `hs_generator_subset` gives the null generator
  `{V + s : s ≥ 0} ⊆ J⁺(q) ∩ 𝓗⁺`.
- **Non-vacuity:** `hs_origin` shows the cones come within `1` of the origin, so the 1-stretch is non-empty.

## Why the statement is P1's clause

- "The stretch of `𝓗⁺` they approach to within any given distance" is `hs_stretch (cone) 𝓗⁺ τ ε`.
- "Extending without bound" is (S1) and (S2): every bounded part of `𝓗⁺` is eventually inside the stretch, so the
  stretch leaves every compact set.
- The statement holds for every compatible distance.

## Not in the general statement, as registered

- **"To the future" along the generators.** It is shown on the witness only. The general case needs the generators'
  future inextendibility.
- **"Monotonically from outside."**

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
