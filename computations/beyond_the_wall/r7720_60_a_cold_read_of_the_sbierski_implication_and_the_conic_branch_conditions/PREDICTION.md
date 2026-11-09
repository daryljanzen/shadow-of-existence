# r7720 (60) — PREDICTION, registered before measurement

**Order answered:** `r7717` (69). A cold read of the two landed repairs, and **the two questions the
order puts directly** — one a question about a LOGICAL RELATION between two theorems, which is a
new kind for this seat, and one about whether a declaration states a range or only an identity.

**Tree:** `f14d2e51` (`origin/main` = `r7717`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleConic.lean`
  (17,446 lines, 927,989 bytes). **Nothing inside it** — `cn_curve`, `cn_circle` and
  `cn_hyperbolas` have not been read, and question ② turns on the third.
- **Neither landed sentence has been read at source**, and neither has
  `rem:asymmetric_chart`, which the new clause cites.
- Carried from `r7718`, read then and declared because question ① leans on it: P2's own
  description of Sbierski's theorem as *"`C^0`-inextendible---inextendible even as a Lorentzian
  manifold with a merely continuous metric---by causal-geometric (Lorentzian-diameter) arguments
  that do not invoke the curvature divergence at all"*, and its object as *"the maximal analytic
  Schwarzschild spacetime---the `Λ=0` object"*. **The remark the new clause cites has not been
  read**, and whether it is where that is set out is an arm.
- **No receipt.**

## QUESTION ① — IS "implied by Sbierski's stronger, curvature-independent `C⁰`-inextendibility" RIGHT?

**This is a question about a relation between two STATEMENTS, not about whether a file says what
prose says, and the predicate is registered accordingly.** The claim has three parts, and each is
its own conjunct (G1):

> **ⓐ "stronger".** Is `C⁰`-inextendibility stronger than `C²`-inextendibility? **Registered
> reading:** a `C²` metric is in particular `C⁰`, so a `C²` extension is a `C⁰` extension, so
> ruling out all `C⁰` extensions rules out all `C²` ones. The word is right if that containment
> is the right way round — and the arm must be able to find it the wrong way round, since
> "stronger" is exactly the kind of word that gets inverted.
> **ⓑ "implied".** Does the spacetime-level claim imply the CHART-LEVEL one the sentence makes —
> no `C²` extension of the Kruskal metric **across a point of the frontier of `{UV < 1}`**?
> ⚠ **These are different subjects, and this seat's own instrument from `r7718` applies: an
> inference is identified by its SUBJECT and its CONCLUSION.** Sbierski's subject is a SPACETIME;
> the clause's subject is a METRIC ON A CHART, across a boundary point in a coordinate plane. The
> bridge, registered before reading: a `C²` extension across such a point would give a larger
> connected Lorentzian manifold containing the original isometrically with a continuous metric —
> i.e. a `C⁰` extension of the spacetime — so the implication goes through **IF** the chart-level
> extension yields a spacetime extension. **The arm reads the sentence's own words to see whether
> that is what it claims**, and must be able to report that the bridge is missing.
> **ⓒ The premise the bridge needs.** Sbierski's object is the maximal analytic Schwarzschild
> spacetime; the clause's object is this paper's Kruskal chart. ⚠ **And P2's own paragraph says
> that maximality among all extensions, as an abstract spacetime, is NOT formalised** — so the
> identification of the chart object with Sbierski's object is a PAPER-LEVEL claim, not a
> machine-checked one. Whether the sentence needs that said is the third outcome.

**The honest outcomes, any of which the probe must reach:** **(a)** all three right and the clause
sound — **NO DEFECT**; **(b)** the relation is right but one of its premises is unstated, and a
clause is owed; **(c)** the relation is wrong in direction or in subject, and the sentence claims
an implication that does not hold.
⚠ **THE TRAP: the order asks "whether … is right", which invites YES, and the mathematics here is
genuinely easy — which is exactly when a subject shift goes unnoticed.** So ⓑ is read as a
subject comparison and not as a containment of regularity classes. No verdict predicted.

⌗ And one arm on the citation itself: **does `rem:asymmetric_chart` set out Sbierski's result**, as
the clause says it does? Located BY TEXT, and read.

## QUESTION ② — DOES `cn_hyperbolas` STATE THE BRANCH CONDITIONS, OR ONLY THE IDENTITIES?

The landed sentence claims that on `z = iρ` and `z = π + iρ` the curve **"is the pair of branches
`r ≥ 2M` and `r ≤ 0` of the hyperbola `(r − M)² − σ² = M²`"**. That is **two** claims:

- **the identity** `(r − M)² − σ² = M²` on each of the two lines; and
- **the RANGES**, that the first line gives `r ≥ 2M` and the second `r ≤ 0`.

**Registered before reading:** an identity is an equation and a range is an inequality, and a
declaration can carry the first without the second. So the arm reads `cn_hyperbolas`' conclusion
and asks **which conjuncts are inequalities in `r`**. Three outcomes: both are there and the
sentence is exact; only the identity is there, and the ranges are elsewhere — plausibly
`cy_patches`, which `r7716` read as stating each patch's range ONTO — in which case the sentence
cites one declaration for two claims and the repair is a pointer; or neither, and the sentence
overreaches.
⌗ **`cy_patches` is NOT assumed to cover it:** if the ranges are not in `cn_hyperbolas`, whether
they are in `cy_patches` is read, and `cy_patches`' own conjuncts are about `M(1 + cosh ρ)` and
`M(1 − cosh ρ)`, which are the SAME NUMBERS by a different parametrisation — so that it covers
them is a reading, not a given.

## ITEM ③ — THE REST OF THE LANDING

- **3a** The "therefore" repair as landed, read at source in full: that what is machine-checked is
  the non-existence of a continuous extension of the **scalar**, and that the `C²` consequence for
  the metric is stated as following by an argument rather than by a cited theorem. **This is this
  seat's own routed repair, so it is read against what was routed and not against the order's
  summary of it.**
- **3b** `cn_curve`: whether "entire" is what it states, and of **both** `r` and `s`.
- **3c** `cn_circle`: whether the real-line claim is the circle, and on what domain.
- **3d** The three declarations exist, spelled as printed, with their binders; `axiom` and `sorry`
  counts for `CircleConic.lean`.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.
**⛭ And the one `r7718` added, carried forward: every inference is a PAIR — subject and conclusion
— and two are the same only when BOTH match; the classifier is re-tested on a same-subject and a
different-subject pair before use. ⛭ New here: an EQUATION and an INEQUALITY are different
conjuncts, and the reader that tells them apart is tested on one of each.**

**The twenty-two negative probes stand.** Most exposed: (15) and (17) — the order asks "whether",
twice, and both times the inviting answer is the agreeable one, so **NO must stay reachable on ①
and YES must stay reachable on ②**; (19) a NAME is a form; (21) a load-bearing word is read and
not granted — here "stronger", "implied" and "is the pair of branches".

**⌗ AND THE LESSON OF THE LAST TWO REVISIONS, which cost three arms between them: both of
`r7718`'s defects were a statement read for a WORD or a WORD COUNT instead of for its STRUCTURE.**
So every reader here is given a negative of the opposite class before use, and every arm is
written as an assertion that can FAIL. ⌗ And every absence claim NAMES its search as it is
written, which is `r7716`'s landing defect not repeated twice.

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, it cannot read
Sbierski's paper, and it cannot settle whether the paper's Kruskal object IS the maximal analytic
Schwarzschild spacetime — that is a paper-level identification and will be NAMED as outside.
