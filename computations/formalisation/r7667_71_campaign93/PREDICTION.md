# `r7667+71.1` — PRE-REGISTRATION: campaign 93, `r7667`. ① The future direction: (a) the futureward (S2) from a named generator hypothesis, discharged on every witness, BUILT now; (b) the general achronal-boundary theorem on `N`, **priced, and one hypothesis it needs put to 69 before building**. ② The inventory refreshed first, then the cheapest row registered separately before its Lean. ⌗ ①(a) `250` new lines (band 100–700), p `0.9`. ①(b) one chart `2500` lines at p `0.3`, on `N` `6000` at p `0.15`, not built here. ② the refresh, no Lean, p `0.95`. **Expected stop for ①(a): none expected. For ①(b): the limit-curve theorem on `N`**

*Under `r7667`. No Lean was written before this registration.*

## ①(a) The futureward stretch, given generators

***The hypothesis `HasFutureGenerators`.*** Through every `q ∈ 𝓗⁺` passes a curve `γ : [0, ∞) → N` with:
- `γ 0 = q`;
- `γ t ∈ 𝓗⁺` for all `t`;
- `q ≤ γ t`;
- `γ` leaves every compact set.

This is exactly what the achronal-boundary theorem supplies. The theorem below takes it as a hypothesis and names it.

***`gs_future_stretch`.*** Under `hs_stretch_N`'s hypotheses and `HasFutureGenerators`: for every `q ∈ 𝓗⁺`, `ε > 0` and
compact `K`, eventually in `τ` the ε-stretch contains a point of `𝓗⁺ ∩ J⁺(q)` outside `K`.
- **Route.** Take the generator's tail outside `K`. Apply (S1) to the compact `γ([0, t₀]) ∪ {γ t₀}`, with `t₀` chosen
  so that `γ t₀ ∉ K`.
- **Witnesses.** The hypothesis is discharged on each of:
  - the 4D witness, by the generator `(0, V + s, y, z)` (`hs_generator_subset`);
  - the 3D warped witness;
  - `Pt`;
  - the cylinder, by `(0, V + s)`.

  So it is non-vacuous on every witness the remark names.

## ①(b) Generators in general: what the probes carry and what they lack

***What the probes already carry.***
- Campaign 67's `cg_generator`, in one chart: every `p ∈ ∂J⁻_Lip(A) ∖ closure A` has an achronal causal curve in
  `∂J⁻_Lip(A)` that either ends on `closure A` or is future-inextendible. It uses:
  - a limit-curve theorem (campaigns 61/65);
  - closedness of the Lipschitz relation on compact sets.
- Campaigns 69 and 77: the generators are null a.e., and are null geodesics.

***What it needs beyond them.***
1. **A global C¹ temporal function on `M`** with `dθ > 0` on the nonzero cones, which `cg_generator` takes. P1 assumes
   global hyperbolicity of `D` only, and a time function near `𝓗⁺` is outside `D`. **This hypothesis is not P1's.**
   P1's asymptotic flatness does not give it either; stable causality of `M` would.
2. **The bridge between the two causal relations.** The headline's `𝓗⁺` is `∂J⁻` of the C¹-chain relation, while
   campaign 67's is `∂J⁻` of the Lipschitz relation. It needs `closure J⁻_{C¹} = closure J⁻_{Lip}` and the same
   interiors: push-up for Lipschitz curves, plus approximation of Lipschitz causal curves by C¹ chains near a
   timelike one. Only the one-chart interior half is in campaign 63's `cr_interior_JpastL_subset`.
3. **The observer has no limit point in `M`.** This is P1's own "`O(τ) → i⁺`", which the Lean has not needed until now.
   Without it, generators may end on `closure (range O)`.
4. **On `N`:**
   - Lipschitz causal curves on a manifold;
   - Arzelà–Ascoli through an exhaustion by compact chart-covered sets;
   - the limit-curve theorem;
   - Lipschitz push-up.
   None of these is on `N`.

***The price.***
- **One chart**, from campaign 67 plus items 1–3: about `2500` lines, p `0.3`.
- **On `N`**, adding item 4: about `6000` lines, p `0.15`. The expected stop is the limit-curve theorem on `N`.
- **Asked of 69:** whether a global temporal function on `M` (item 1) is acceptable as a stated hypothesis beyond P1.
  Or should the general result instead wait for a proof from `D`'s global hyperbolicity plus the extension? I know no
  short route for that. ①(b) is not built until 69 answers.

## ② The inventory, refreshed

`r7667_71_inventory/INVENTORY.md` (new) re-reads P1 as it stands at `5dac5ff9` against every probe through campaign 92.

***Expected changes.***
- `prop:causal-alignment` moves to BUILT, clause by clause through campaigns 87–92, with the gaps the remark states.
- `lem:killing` 4d's "no non-vacuity witness" is outdated: campaigns 82–83's `KillingWitness.lean` built one. 4b–4d's
  remaining gap is the `LocalKillingChart` link.

Then the cheapest BUILT-IN-PART row is registered on its own, with p and lines, before any Lean.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
