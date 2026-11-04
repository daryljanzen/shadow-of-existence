# `r7674` — a cold read of the revised attestations and the Killing-generator lemma

**Registered before any bank is taken.**  Order `r7673` asks a cold read, in `r7672`'s form, on a
named tree, of two things: the **revised remark sentences** after `thm:metric-singularity`, and the
**two new sentences at the end of `lem:killing`'s proof** against `KillingGenerator.lean`.

## The objects

**Object A, the three repairs**, in three claims: ① `ac_metric_singularity_along` now stated with
*all* its hypotheses — the split `g = h − N²dt²`, `N ≥ 0`, and `h(γ̇,γ̇)` non-negative **and
continuous** along the curve — with both legs vanishing at every point, and needing no
differentiability class of the curve and no smoothness of the atlas; ② `ac_lapse_pos_forces_point`
now stated with `N > 0`, the curve differentiable, and `h` positive definite on `ker dt`, with
`ac_witness_no_positive_lapse` named; ③ the word collision removed — `Δτ` the temporal leg
**integrated** along the geodesic, an invariant integrand, and the proof's own sentence untouched.

**Object B, the `lem:killing` attestation**, in five claims: ④ along an integral curve of a Killing
field nowhere zero and null at one point, the curve is **null throughout**; ⑤ any two of its points
are related by a **local isometry carrying the generator into itself**, so every invariant takes the
same value at both; ⑥ `Δτ = ∫|χ|dλ = 0`; ⑦ it is witnessed on a generator of the Rindler horizon;
⑧ the adapted coordinates are formalised **on each local chart rather than along the whole
generator**, so there (b) is carried by the equality of the transverse invariants.

## The arms

- **⓵ Every cited name must resolve** in the file named.  **Registered prediction: all resolve.**
- **⓶ ①'s hypothesis list must now match the binders exactly.**  **Registered prediction: the
  stated hypotheses and `ac_metric_singularity_along`'s binders agree, with the continuity
  hypothesis `r7672` found unstated now stated and the spurious curve class gone.**
- **⓷ ②'s hypothesis list must match `ac_lapse_pos_forces_point`'s binders exactly.**  **Registered
  prediction: all three stated, including the positive-definiteness `r7672` found unnamed.**
- **⓸ ③'s repair, in both directions.**  The remark must no longer use "accumulated" of `Δτ`, and
  the proof's own sentence must be **unchanged**.  **Registered prediction: the remark says
  "integrated" and the proof's sentence is identical to the one on `r7672`'s tree** — checked by
  comparing against that commit, not by memory.
- **⓹ `kg_lemma_killing_generator` must carry ④, ⑤ and ⑥.**  **Registered prediction: nowhere-zero
  and null-at-one-point are its hypotheses; null-throughout, the local isometry, and `Δτ = 0` are
  conjuncts of its conclusion.**
- **⓺ ⑧'s honesty clause is the arm to watch.**  "Machine-checked along a whole generator" and
  "formalised on each local chart rather than along the whole generator" sit in the same paragraph,
  and the second is a limitation on the first.  The question is whether the limitation is stated
  where it bites: **is the isometry of ⑤ local — a chart-bounded shift — and if so does ④'s
  "null throughout" hold globally along the curve or only chart by chart?**  Registered as the
  **comparison**, not a verdict (`r7670`'s correction): the instrument reads the quantifiers of
  each conjunct and reports which are global in the curve's parameter and which are chart-local,
  whatever it finds.
- **⓻ The guard, three families**, anchored markers only in the two forms `r7670` fixed, every
  verdict a function of its readings, a flip family over all of them.  **If any probe does not flip,
  every verdict is withdrawn.**

## What would falsify the reading

A claim scored from the order's account of the repair rather than from the paper and the Lean; a
cited name taken on trust; the proof's sentence declared unchanged from memory rather than by
comparison; a quantifier reported rather than parsed; a guard probe that does not flip.
