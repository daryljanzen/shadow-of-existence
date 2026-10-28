# `r7619+71.1` — PRE-REGISTRATION: campaign 61, `r7619` ①, the limit-curve lemma, then the tangency clause. ⌗ `1200` lines in up to two probes (band 500–3000), ⛔ stop `4000`. ⌗ p: Lipschitz causal class + bridge to the C¹ class `0.7`, limit-curve lemma `0.55`, null generators of `∂J⁻` `0.15`, tangency clause `0.1`

*Under `r7619` ①. The setting is campaign 60's: `probes/CausalStructure.lean`, one chart, with `g` continuous and
locally Lipschitz where needed. No Lean was written before this registration.*

## ① The Lipschitz causal class (`probes/LimitCurves.lean`)

- A ***Lipschitz future-causal curve*** is `γ : [a,b] → M`, Lipschitz. Its difference quotients lie, in the
  limit, in the closed future cone. The working definition is the cone form: for all `s < t`,
  `γ(t) − γ(s)` lies in the closed convex hull of the future causal cones over the image of `γ([s,t])`, up to an
  error `o(t − s)` that is uniform on compact pieces. An equivalent a.e.-velocity form is used if Rademacher
  (`LipschitzWith.ae_differentiableAt`) makes it the cleaner route. RESULT will say which.
- ***The bridge:*** every C¹ causal step of campaign 60 is a Lipschitz causal curve, so campaign 60's
  `≤` is contained in the Lipschitz relation.

## ② The limit-curve lemma

- ***Statement.*** Let `γₙ : [0,1] → K` be curves into a compact `K ⊆ M` that are uniformly Lipschitz and
  future-causal. Suppose `γₙ → γ` uniformly. Then `γ` is Lipschitz and future-causal.
- ***Corollary.*** Such a sequence has a uniformly convergent subsequence, by Arzelà–Ascoli
  (`BoundedContinuousFunction.arzela_ascoli`), and its limit is causal.
- ***The key piece*** is that the closed future cone field is closed under limits: `g` and `T` are continuous, so
  the set `{(x, v) : g_x(v,v) ≤ 0, g_x(v, T x) ≤ 0}` is closed. Closedness then passes to the convex hulls and to
  the difference quotients.

## ③ Stretch: the tangency clause

- ***Null generators.*** For `p ∈ ∂J⁻(S) ∖ closure S`, there is a past-directed Lipschitz causal curve from `p`
  lying in `∂J⁻(S)`. This is the achronal-boundary generator lemma, proved by limit curves plus push-up.
- ***Tangency.*** Then the convergence or tangency clause of `prop:causal-alignment`, in whatever form those
  generators support.

***Failable:*** each piece is BUILT, BUILT IN PART, or REPORTED.

***Reachable negative:*** `②` may close only with a hypothesis that the curves are uniformly timelike-bounded, or
with the a.e.-velocity definition and no equivalence to the cone form. If so, that is BUILT IN PART, with the
missing step named. `③` is expected to stop. If it does, RESULT names its first missing lemma, which is likely
inextendibility of limit curves, or the fact that "null" means maximising along `∂J⁻`.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched. No census row moves.*
