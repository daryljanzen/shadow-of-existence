# `r7664` — a cold read of `rem:formalised` against the Lean

**Registered before any bank is taken.**  Order `r7663` asks for a cold read of P1's
`rem:formalised` (`corpus/BH_causality_v2.tex`, directly after the proof of
`prop:causal-alignment`), sentence by sentence, against `mx_prop_causal_alignment`'s
binders and conclusion, the definitions those unfold to, and the five named witnesses.

## The tree

A cold read is a statement about a TREE and it has to name the tree.  `runs/TREE.txt`
is written **before** any bank, and records the worktree commit, the dirty paths, and
the blob hash of every file read.  Every verdict below is a verdict on that tree and
no other.

## The object

The remark is decomposed into **twenty** claims, ① … ⑳, fixed here before measurement.
Claims about the formal statement: ① the attestation (Lean 4, Mathlib, no unproved
step, no axioms beyond the standard three, the two theorem names); ② the setting
(Hausdorff, Lorentzian metric, time orientation, metric `C¹` and orientation continuous
in a chart about each point); ③ the extension (`𝒥⁺` a set in `ι:M→M̃`, an open `C¹`
embedding, `ι*g̃ = Ω²g` with `Ω` positive, the extension carrying the same regularity,
causal curves chains of `C¹` causal arcs); ④ the hypotheses (`O` a chronologically
ordered worldline, `I⁻(O)=D=I⁻(𝒥⁺)`, `Θ` a Cauchy temporal function of `D` adapted to
`O`); ⑤ conclusion one (`∂J⁻(O)=∂J⁻(𝒥⁺)=𝓗⁺`, the characterisation derived); ⑥
conclusion two (the closure of each `{Θ≤T}` inside `D`, so no finite-`Θ` slice meets
`𝓗⁺`); ⑦ conclusion three (slices and cones each Kuratowski-converge to `𝓗⁺`, lower
limit every horizon point approached by all sufficiently late `τ`, upper limit nowhere
else); ⑧ conclusion four (the tangency clause in the proof's form); ⑨ *assumes only*
— beyond the proposition's hypotheses, the carrier clauses and the frame's convergence
and bound; ⑩ *does not use* — asymptotic flatness, future-completeness of `O`,
`O(τ)→i⁺`, any smoothness beyond `C¹`; ⑪ global hyperbolicity entering only through the
Cauchy property of `Θ`, *its standard equivalent*; ⑫ the two clauses not in the formal
statement.  Claims about the witnesses: ⑬ `mx_witness_headline` (joint satisfiability
with every clause instantiated, flat 2d Rindler exterior, two-chart atlas, compactified
by `v=arctan V`); ⑭ `−log(−U)+V` aligns; ⑮ an oscillating `f(−U)+V` does not; ⑯
`cz_witness_headline` (`(arctan U, arctan V)`, compact closure of the image, `Ω²`
non-constant); ⑰ `cz_witness_headline_F` (every `−F dU dV`, tangency as the general
implication, not instantiated at a point); ⑱ `cy_witness_headline` / `cy_witness_tangency`
(`ℝ²×S¹`, no chart covering it, every conclusion, `𝓗⁺={U=0}×S¹` as `∂J⁻(O)`, Cauchy
property on the manifold itself); ⑲ the trivial extension along the circle not conformal,
so the `∂J⁻(𝒥⁺)` identification not exercised; ⑳ no four-dimensional and no curved witness.

Each claim is scored **SUPPORTED** (the Lean's statement carries it), **NOT SUPPORTED**
(the Lean's statement contradicts it or is silent where the remark asserts), or
**UNMEASURED BY THIS SEAT** (no instrument here can decide it).  A claim is never scored
from the remark's own words.

## The arms

- **⓵ The binder census.**  *Every* binder of `mx_prop_causal_alignment` is enumerated
  from the Lean and each one mapped to the sentence of the remark that carries it.
  **Registered prediction: ZERO binders unaccounted.**  `r7662` found five Lean binders
  with no counterpart in P1's proposition — `T2Space`, `LocallyOneChart` on the spacetime
  and on its extension, and carrier bookkeeping for `J` and the horizon — and the remark
  appears written to cover exactly those.  If any binder has no sentence, ⑨'s *assumes
  only* is NOT SUPPORTED and the arm MISSES.
- **⓶ The conclusion census.**  Every conjunct of the conclusion is enumerated and mapped
  to one of the remark's four.  **Registered prediction: the remark's four cover every
  conjunct, and the grouping of the Kuratowski conjuncts into ⑦ loses no conjunct.**
  `r7662` read the conclusion as a seven-tuple against P1's eight clauses; a regrouping
  from seven into four is where a slip would live, so this arm is registered as the one
  most likely to miss.
- **⓷ The *standard equivalent* clause.**  ⑪ asserts a mathematical equivalence.
  **Registered prediction: the Lean contains NO statement of it** — no theorem relating
  global hyperbolicity to the existence of a Cauchy temporal function — so ⑪ is a claim
  the attestation does not cover, and must be reported as such even though it is true
  mathematics.
- **⓸ The attestation.**  ① claims no unproved step and no axioms beyond the standard
  three.  **Registered prediction: this seat cannot decide it** — no Lean toolchain and
  no Mathlib here — so it is scored UNMEASURED BY THIS SEAT, with what *can* be measured
  (absence of `sorry`, `admit`, `axiom`, `native_decide` in the named declarations)
  reported separately and NOT as the claim.
- **⓹ The omission side.**  **Registered prediction: at least one thing the Lean proves
  that the remark omits and a reader would want.**  If the scan returns none, that is
  reported as none and this arm MISSES.
- **⓺ The guard.**  The checker must be able to return either verdict on the same
  machinery.  Two synthetic probes are run: a claim the Lean verbatim carries, which must
  score SUPPORTED, and a deliberately false claim of the same shape, which must score NOT
  SUPPORTED.  **If either probe scores the other way, every verdict in this receipt is
  withdrawn.**  A checker that cannot fail on the data it is given is not a checker.

## What would falsify the reading

Any claim scored from the remark's wording rather than the Lean's; any binder or conjunct
not enumerated from the source; any verdict on a tree other than the one `runs/TREE.txt`
names; a guard probe that does not flip.

