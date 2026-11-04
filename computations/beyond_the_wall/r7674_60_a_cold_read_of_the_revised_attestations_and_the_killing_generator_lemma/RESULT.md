# `r7674` — the verdict: all three repairs hold, the new attestation repeats on a new theorem the fault just corrected on the old one, and one of its clauses is classical rather than checked

Order `r7673` asked a cold read of the revised remark sentences and of the two new sentences at the
end of `lem:killing`'s proof. Eight claims were fixed in `PREDICTION.md` before any bank.
**6 SUPPORTED · 2 NOT SUPPORTED.** All seven arms HIT.

## The three repairs hold, and one of them to the letter

**①** The first attestation now names every hypothesis the theorem has — the split, `N ≥ 0`, and
`h(γ̇,γ̇)` **non-negative and continuous along the curve**, which is the load-bearing continuity
`r7672` found unstated. The spurious `C¹` curve class is gone, replaced by "it needs no
differentiability class of the curve and no smoothness of the atlas" — the stronger and true
reading. And "both legs vanish at every point of the curve" carries the two pointwise conjuncts the
earlier sentence dropped. The Lean file is **unchanged**, so the repair is entirely in the prose,
which is where the fault was.

**②** The second names all three: `N > 0`, the curve differentiable, and `h` positive definite on
`ker dt` — the hypothesis the conclusion actually rests on. `ac_witness_no_positive_lapse` is named,
which is the sharper half: on the Rindler generator **no** positive-lapse splitting satisfies (a)
and (b), so the lapse's vanishing is forced rather than chosen.

**③** The word collision is gone. `Δτ` is now "the temporal leg **integrated** along it", the word
"accumulated" is no longer used of it at all, and the remark names what it is distinguishing itself
from — "not the coordinate difference accumulated along a path that the proof below sets aside".
**The proof's own sentence is unchanged**, verified by comparing its text against `54e854a6`'s tree
rather than from memory. The fork was decided as recommended and executed in the direction that
left the proof intact.

## ⑧ — the honesty clause is correctly scoped, which is the opposite of the last one

Every one of `kg_lemma_killing_generator`'s five conjuncts is quantified over the **whole segment**
`Icc a b`, and that globality is **earned**, not assumed: the proof glues chart-local boxes with
`isPreconnected_Icc.induction₂'`. So "machine-checked along a whole generator" is accurate. The
chart-local objects are the isometry witnessing each pair and the adapted transverse coordinates —
which do not appear in the file at all — not the null condition or the relation, which hold across
the segment. The clause states the limitation where it bites, which is exactly what `r7672` found
"on any manifold" failing to do when it flattened two theorems into one claim.

## ④ — the new attestation repeats, on a new theorem, the fault just corrected on the old one

The sentence names four hypotheses: the field nowhere zero, null at one point, Killing, and the
curve an integral curve of it. The theorem has **two more**, both regularity:

- **`hg`**: the metric's chart representative is eventually differentiable near each `γ t`;
- **`hX`**: the field is `C¹` as a section of the tangent bundle.

Neither is stated. This is the same class of omission as the continuity hypothesis in the first
attestation — repaired in this very revision — now reproduced on the theorem that arrived with it.
The conclusion is otherwise exactly as described: null throughout the segment from nullity at a
single parameter, any two parameters related, injectivity giving distinct events, and the lapse
integral vanishing.

## ⑤ — "every invariant takes the same value at both" is classical, not checked

Conjunct 3 gives a genuine local isometry: an open `U ∋ γ t₁` with `F` satisfying
`g (F x) (DF v) (DF w) = g x v w` on `U`, `F (γ t₁) = γ t₂`, and `F (γ s) = γ (s + t₂ − t₁)` near
`t₁`, so it carries the generator into itself. That half is exact. But **no theorem in the file
mentions an invariant**, and the only invariant equality proved is **one** — the norm-squared of the
field — used internally to propagate the null condition. "Every invariant takes the same value"
follows from the isometry as mathematics and is true; it is a classical inference, and the remark's
own discipline is to mark those, as it does for Bernal–Sánchez, the achronal boundary and the
Cotton criterion. Marking it would also make the paragraph's logic visible: it is the step that
carries hypothesis (b).

## The arms, scored

| arm | outcome |
|---|---|
| ⓵ cited names resolve | **HIT** — 6 of 6 |
| ⓶ the first hypothesis list matches its binders | **HIT** |
| ⓷ the second matches its binders | **HIT** |
| ⓸ the collision repair, both directions | **HIT** — and the proof's sentence verified by comparison |
| ⓹ the headline carries the three claims | **HIT** |
| ⓺ the quantifier comparison | **HIT** — all five global, earned; the limitation correctly scoped |
| ⓻ the guard | **HIT**, with three repairs recorded below |

## What the guard caught, three times, in one instrument

1. **The anchor rule refused a math-mode marker.** `$N>0$` carries no word boundary and no control
   sequence. A `$` is a delimiter and cannot occur inside a word, so it is a third anchor form; it
   is now accepted explicitly, with a probe that the marker matches `$N>0$` and **not** `$N>0.5$`.
   That is the second widening of this rule in three revisions, each recorded rather than quietly
   loosened.
2. **The quantifier reader tested only for `Icc a b`** and so scored the lapse integral — a
   statement about the whole segment — as chart-local, which drove ⑧ to the wrong verdict.
3. **Then it used `\d?` for the parameter subscript**, which does not match `t₁`, and scored the
   two-parameter conjuncts local for that reason alone.

Three drafts, three wrong readings, and **the flip test caught none of them**: each verdict did
depend on its reading; the reading was simply wrong. *A guard that checks whether a verdict depends
on its input cannot check whether the input was read correctly.* The reader now carries probes
pinning every shape the file actually contains — plain quantifier, subscripted quantifier, segment
integral, and a chart-local statement that must **not** read global — and a fourth mis-reading
cannot pass silently. That is a new form of the standing lesson, and the sharpest one yet: *a
dependence test is not a correctness test.*
