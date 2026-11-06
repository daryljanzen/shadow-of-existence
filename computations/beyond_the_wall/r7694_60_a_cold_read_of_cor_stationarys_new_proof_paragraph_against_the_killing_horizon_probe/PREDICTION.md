# r7694 (60) — REGISTRATION: a cold read of `cor:stationary`'s new proof paragraph, against `StationaryHorizon.lean`

**Registered before a line of any reading existed, in its own pushed commit.** The tree is named in
`runs/TREE.txt`. Every arm is a COMPARISON with **no predicted verdict**; what is registered is the
shape of what a reading may return and the reachable negatives, so reaching one is a result.

Order: `r7691` (69), the topmost section of `FOR_60.md` on `origin/main` at registration. It asks a
cold read of `cor:stationary`'s new proof paragraph against `st_cor_stationary`, `st_witness` and
`IsKillingHorizon`, and it names **two things to check above all**:

1. **that the hypotheses are stated WHOLE**, and
2. **that "the rigidity theorem itself being cited and not formalised" is right.**

⌗ `r7692`'s count fork is CLOSED by this order: 69 meant seven corpus places and this seat counted
six receipt-citing sites in P15, and both counts are right for what they count. It is not re-opened
here.

---

## THE SIX GUARD FAMILIES AND THE TEN STANDING NEGATIVE PROBES, CARRIED FORWARD

Guards: **G1** one predicate per conjunct; **G2** three anchor forms only, an unanchored marker
REFUSED and no boundary after a delimiter; **G3** every reading run against an altered copy and
required to change its answer; **G4** classifier probes state the category assigned and why;
**G5** reader probes with NEGATIVE probes; **G6** every prose probe on a whitespace-FLATTENED copy.
**Every verdict note is BUILT FROM its readings.**

Negative probes 1–10 carried forward unchanged: (1) a figure absent from the cited probe ⇒ NOT
SUPPORTED; (2) a variable bound in a later binder group still parses BOUND; (3) a conjunct under a
binder is not reported at TOP; (4) UNMEASURED when the source does not distinguish; (5) two figures
said to be one quantity must FAIL when they differ; (6) a dependence reading must answer both ways;
(7) a hypothesis probe separates "stated" from "does the work"; (8) a reliance probe must be able to
answer NONE and still fire on an injected site; (9) a carrier probe separates "present in the
computation" from "rides on it" by a COUNTERFACTUAL; (10) a count probe must be able to return a
count other than the one the prose states.

## TWO NEW NEGATIVE PROBES THIS REVISION ADDS

11. **A WHOLENESS probe must be able to find a hypothesis the prose leaves out.** Handed a copy of
    the paragraph with one of its stated hypothesis clauses struck out, the reading must return
    **HYPOTHESIS OMITTED** and name which. A probe that can only confirm "whole" is a probe that
    answers about itself. ⚠ This is the arm the order says to check above all, so its negative
    control is registered before the reading.
12. **A NOT-FORMALISED probe must be able to catch the opposite error in BOTH directions.** Handed a
    sentence that says a result is cited-and-not-formalised when the probe does prove it, it must
    return **UNDERSTATED**; handed one that claims machine-checking the probe does not carry, it must
    return **OVERSTATED**. Both are reachable and both are results.

---

## ARM 1 — ARE THE HYPOTHESES STATED WHOLE? (the order's first "above all")

The paragraph states the Killing-horizon hypothesis as a list: `X` continuously differentiable and
nonzero on the horizon; the metric's chart representative differentiable and `L_X g = 0` near it; and
through each of its points an integral curve of `X` lying in it and null somewhere.

Registered as a **two-way field-by-field comparison** against `IsKillingHorizon`'s own fields, read
at source:

- **1a EVERY FIELD OF THE STRUCTURE IS STATED.** For each field of `IsKillingHorizon`, is there a
  clause of the paragraph that states it? A field with no clause is **HYPOTHESIS OMITTED**, which is
  the finding the order is asking for. Negative probe 11 governs.
- **1b EVERY CLAUSE OF THE PARAGRAPH IS A FIELD.** The converse direction: a clause with no field
  behind it is **HYPOTHESIS INVENTED** — stated in the paper and not asked by the probe, which would
  make the paper's hypothesis stronger than the theorem's and is equally a result.
- **1c THE QUANTIFIERS AND THE LOCI.** ⚠ *A conjunct's QUANTIFIER is part of the claim*, and *a
  quantity keeps its NAME outside the region where it measures anything*. So each clause's scope is
  read, not assumed: "on it" against "near it" against "through each of its points", and "null
  somewhere" against "null everywhere" — a clause whose locus or quantifier differs from its field's
  is **SCOPE-DIFFERS**, recorded with both readings beside each other.
- **1d THE AMBIENT SETTING.** "In the setting of Remark `rem:formalised`" — are the probe's ambient
  hypotheses (the manifold, the regularity, the time orientation) those of that remark, no weaker and
  no stronger? **STRONGER-THAN-CLAIMED** is recorded and never upgraded to SUPPORTED, as at `r7690`
  and `r7692`.

Reachable verdicts: **SUPPORTED** / **HYPOTHESIS OMITTED** / **HYPOTHESIS INVENTED** /
**SCOPE-DIFFERS** / **STRONGER-THAN-CLAIMED** / **UNMEASURED**.

## ARM 2 — IS "CITED AND NOT FORMALISED" RIGHT? (the order's second "above all")

The sentence makes **two claims at once** and they are scored separately, because *a sentence can be
safe from a gap that is really there* and because *two claims on one sentence can disagree*:

- **2a THE POSITIVE HALF.** "The corollary is machine-checked **with the rigidity theorem's
  conclusion as its hypothesis**." Does the probe take that conclusion — being a Killing horizon — as
  a hypothesis, and conclude the corollary's own content?
- **2b THE NEGATIVE HALF.** "**the theorem itself being cited and not formalised.**" Is the rigidity
  theorem genuinely absent from the probe? This is an ABSENCE claim and is read as one: the reading
  **names what was searched** — the probe's own text for the theorem's content (stationarity implying
  a Killing horizon, analyticity, the rigidity name itself) — and reports the search, never a bare
  absence. Negative probe 12 governs both directions: **UNDERSTATED** if the probe does prove it,
  **OVERSTATED** if the paragraph claims machine-checking the probe does not carry.
- **2c WHAT THE FIRST PARAGRAPH CLAIMS.** `l.290` says the rigidity theorem's hypotheses "include
  analyticity". Registered as its own comparison against the probe: the probe should ask **no**
  analyticity, precisely because it takes the conclusion as hypothesis. If it asks analyticity the
  paragraph's division of labour is wrong; if the paper's citation of analyticity is at odds with
  what `lem:killing` then applies to, that is a separate finding.

## ARM 3 — THE FOUR CONCLUSIONS, AGAINST `st_cor_stationary`

The paragraph lists four conclusions "along every integral curve of `X` in the horizon": the tangent
is null; distinct points stay distinct; every pair is metrically coincident; and the horizon's adapted
splitting assigns `Δx = Δτ = 0`. Four claims, one predicate each (G1), each against the theorem's own
statement text, with the binder each sits under read rather than inferred (negative probe 3, and
*a claim about "every" is a claim about a BINDER*).

Reachable per claim: **SUPPORTED** / **NOT SUPPORTED** / **TWO-TO-ONE** / **STRONGER-THAN-CLAIMED** /
**MIS-CITED, SUPPORTED ELSEWHERE** / **UNMEASURED**.

## ARM 4 — THE WITNESS, AGAINST `st_witness`

"On the radial plane of the Eddington–Finkelstein domain `{V>0, UV<1}`, the static field
`∂_t = (V∂_V − U∂_U)/4M` satisfies that hypothesis on `∂J⁻(𝓘⁺)`, and two distinct events of that
horizon are metrically coincident." Registered as four claims: the **domain**; the **field** as
written, factor and signs included; that it **satisfies the hypothesis** — i.e. the witness discharges
`IsKillingHorizon`, so Arm 1 is **not vacuous**; and the **two distinct metrically coincident events**.
⚠ A witness that discharges a *weaker* predicate than Arm 1's would make the non-vacuity claim
hollow, so which predicate it discharges is read, not assumed.

---

## WHAT WOULD MAKE THIS REVISION WRONG

- A wholeness reading that can only say "whole" ⇒ negative probe 11.
- An absence claim in Arm 2b that does not name what was searched ⇒ this seat's own `r7684` lesson,
  and the gate that caught it.
- A conclusion scored at TOP that the theorem states under a binder ⇒ negative probe 3.
- A verdict note that does not follow from its own readings ⇒ every note is BUILT from them.

## EXIT CODES REGISTERED IN ADVANCE

`0` every registered reading ran and its verdict is recorded (whatever the verdict).
`1` a reading could not be run, or a guard refused an anchor, or a negative probe failed to fire.
No other exit code is reachable; **no verdict is an exit code.**

## RECORDED NON-GOALS

- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited. This is a
  READ; every repair found is **routed** in `FOR_66_FROM_60.md`.
- The three repairs `r7692` routed (the `_car_flat` gate, the `ℓ=5` phrase, the
  `td_ne_of_transGen` citation) have all landed or been ordered by `r7691` and are **not** re-routed.
- `sh_H_r`'s docstring remains 71's, already routed at `r7690`, and is not routed again.
