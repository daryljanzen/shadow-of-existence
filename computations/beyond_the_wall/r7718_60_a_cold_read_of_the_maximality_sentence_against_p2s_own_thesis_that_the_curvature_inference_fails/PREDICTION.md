# r7718 (60) — PREDICTION, registered before measurement

**Order answered:** `r7715` (69). A cold read of P2's new maximality sentence, and **the sharpest
question this seat has been handed: whether the paper now asserts both that an inference fails and
that it is machine-checked.**

**Tree:** `a3102b41` (`origin/main` = `r7715`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleMaximal.lean`
  (17,370 lines, 924,041 bytes). **Nothing inside it** — `mx_frontier`, `mx_blowup` and
  `mx_inextendible` have not been read.
- **Neither thesis sentence has been re-read at source**, and neither has `prop:Kretschmann` or
  the new paragraph. From `r7714` I carry one sentence of P2's §on the Kretschmann scalar, read
  then and **not** re-read since: *"That this divergence is an artefact of the chart rather than of
  the manifold was conjectured fourteen years before it could be shown"*. That is the sentence the
  collision would be with, and **its own argument has never been read by this seat.**
- **No receipt.**

## THE QUESTION, DECOMPOSED — AND THE PREDICATE REGISTERED BEFORE EITHER SIDE IS READ

The order puts it exactly: P2's thesis is that **the inference from a curvature divergence to an
inextendible boundary is false**. The new sentence **machine-checks an inference from a curvature
blow-up to the non-existence of a `C²` extension of the metric.** On their faces those are the
same inference with opposite verdicts.

> **THE PREDICATE: an inference is identified by its SUBJECT and its CONCLUSION, not by the
> quantity that appears in both.** The Kretschmann scalar appearing on both sides proves nothing
> either way. What has to be compared is: *of what* does each deny or assert inextendibility — a
> **metric on a chart**, a **manifold**, or a **curve**? Two inferences that share a premise and
> differ in subject are two inferences.

So the arms, each read at source and each able to return either answer:

- **① What P2's thesis actually claims.** Both thesis sentences are located **BY THEIR TEXT** —
  `l.99` and `l.435` are the order's line numbers in a file edited since, and this seat has been
  bitten by exactly that before. Then: is the claim **(i)** that a curvature divergence does not
  imply the *manifold* or the *curve* ends — an ontological claim; or **(ii)** that it does not
  imply the *metric* is `C²`-inextendible — a theorem-level claim, which **would** contradict
  `mx_inextendible` head-on? ⚠ **And the hardest part, registered now because it is where I expect
  to be tempted:** "an artefact of the chart rather than of the manifold" is a claim I cannot
  evaluate without reading `prop:Kretschmann`'s own argument, **because the Kretschmann scalar is
  a scalar INVARIANT and `48M²/r⁶` diverges as `r → 0` whatever chart it is computed in.** So
  either the paper means something narrower by "artefact" than "the scalar does not really
  diverge", or the thesis is in trouble on its own before any Lean file is involved. **The probe
  reads `prop:Kretschmann` and reports which, and it must be able to report the second.**
- **② What `mx_inextendible` actually states.** Is its conclusion about **this metric on this
  chart** — no `C²` extension across any point of `{UV = 1}` — or about an abstract spacetime? And
  is the blow-up conjunct about the **Kruskal** metric's scalar, approaching the frontier **from
  inside**? The registered distinction: *inextendible as a metric on a given chart* and
  *inextendible as a spacetime* are different claims, and the paragraph's own last sentence
  ("Maximality among all extensions, as an abstract spacetime, is not formalised") says the file
  claims only the first — **which is checked rather than taken.**
- **③ Whether the paragraph's own separating clause does the work it is given.** *"This bounds the
  Kruskal metric in its own chart and not the curve: the continuation through `z = π` carries the
  curve, and not this metric, across `r = 0`."* The arm: does that clause name the SUBJECTS the
  two inferences differ in, in the paper's own words, and does it match the thesis sentence's own
  formulation? ⌗ The order offers `l.435`'s *"the curve is extendible, the spacetime is not"* as
  the matching phrase; **that phrase is located by text and read in its own sentence**, not taken
  from the order.

**THE HONEST OUTCOMES, which the probe must separate and any of which it must be able to reach:**

- **(a) NO COLLISION.** The thesis denies an inference about the curve or the manifold; the theorem
  asserts one about a metric on a chart; the separating clause names exactly that difference. **No
  repair.**
- **(b) COLLISION.** The thesis as written denies the very implication the theorem proves — same
  subject, same conclusion — and one of the two has to be narrowed. **Then the repair is drafted,
  as the order asks.**
- **(c) NEITHER, AND WORSE: the separating clause is right but the THESIS is the thing that
  overreaches** — if `prop:Kretschmann`'s argument does not support "artefact of the chart" in the
  sense its sentence claims, the collision is inside P2 and predates this landing. ⚠ **This
  outcome is registered because it is the one I would be most reluctant to report**: it is a
  finding against the paper's own headline claim rather than against a landed sentence, and the
  order does not invite it.

⌗ **No verdict predicted on any of the three.** What I will say in advance is the shape of the
reasoning: **(a) requires the two subjects to be genuinely different AND the paper to say so**;
finding the clause present is not enough, because a clause that *asserts* a distinction does not
*make* one.

## ITEM ④ — THE REST OF THE LANDING

- **4a** The "each" is landed in the back-seam sentence — this seat's own offered word, read at
  source rather than assumed from the order.
- **4b** `mx_frontier`: whether "the only boundary of `{UV < 1}` in the Kruskal plane is the
  hyperbola `UV = 1`" is what it states, as a claim about the **frontier of a set** and not about
  a parametrised curve. ⚠ And whether `r = 0` there is stated or assumed.
- **4c** `mx_blowup`: whether the blow-up is "approaching any point of it from inside", i.e. a
  limit along sets approaching the frontier, and over **which** metric's scalar.
- **4d** The three declarations exist, spelled as printed, with their binders; `axiom` and `sorry`
  counts for `CircleMaximal.lean`.
- **4e** The paragraph's last sentence, **which replaced another (negative probe 20)**: whether
  what it now bounds is bounded — nothing in the files claiming maximality among all extensions.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.
**⛭ And one this revision adds, because the question is about two inferences: every inference is
recorded as a PAIR — subject and conclusion — and two inferences are called the same only when
BOTH match. The classifier that does that is tested on a same-subject pair and a
different-subject pair before it is used.**

**The twenty-two negative probes stand, and the readers of `r7714` and `r7716` are carried forward
and re-tested on their negatives before use.** Most exposed here: (15) and (17) — the order
reports a landing and asks "does it collide", which invites **yes**, so **NO COLLISION must stay
reachable**, and so must a finding against the paper's own thesis; (19) a NAME is a form; (20) a
REPLACED sentence may have changed its subject, which bites at 4e; (21) a load-bearing word is
read and not granted — here "artefact", "bounds" and "therefore"; (22) a named search over SOURCE
cannot find a run-time value.

**⌗ AND THE ONE DEFECT OF `r7716`'s LANDING, carried as a lesson rather than a line:
`check_absence_claims` fired on that diff and was RIGHT — two of its answers rested on an absence
stated bare. So in this revision every absence claim NAMES its search as it is written**, not
after a gate objects.

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, it cannot settle
whether a `C²` extension exists, and it cannot adjudicate P2's ontology. Where a question turns on
something outside the files, that is NAMED as outside and not supplied.
