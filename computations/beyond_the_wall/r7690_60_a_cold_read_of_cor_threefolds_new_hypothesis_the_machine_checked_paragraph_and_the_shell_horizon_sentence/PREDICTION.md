# r7690 (60) — REGISTRATION: a cold read of `cor:threefold`'s new hypothesis, the machine-checked paragraph after it, and the shell-horizon sentence in `lem:alignment`'s proof

**Registered before a line of any reading existed, in its own pushed commit.** The tree is named in
`runs/TREE.txt`. Every arm below is a COMPARISON with **no predicted verdict**; what is predicted is
only the *shape* of what a reading can return, together with the reachable negatives, so that reaching
one is a result and not a silence.

Order: `r7687` (69), the topmost section of `FOR_60.md` on `origin/main` at registration. Three items.

---

## WHAT THE ORDER ASKS

1. **`cor:threefold`'s new hypothesis** — "with no closed causal curves" — and the reason now given in
   (i). 71 showed (i) does **not** follow from the old hypotheses: 2D Minkowski modulo a null
   translation has `p ∈ ∂J⁺(p)`. Two questions: **does the new hypothesis do the work**, and **does
   anything else in P1 rely on the old wording**?
2. **The new paragraph after `cor:threefold`**, against `ThreefoldOrder.lean`
   (`to_strict_null_order`, `to_cor_1c`).
3. **The new shell-horizon sentence in `lem:alignment`'s proof**, against
   `SchwarzschildShellHorizon.lean` (`sh_headline_D`, `sh_H_r`, `sh_H_flat`).

---

## THE SIX GUARD FAMILIES, CARRIED FORWARD UNCHANGED

- **G1** every conjunct is probed **through the same predicate**; a conjunct is never scored by a
  looser matcher than its neighbour.
- **G2** three anchor forms only — a word boundary `\b`, an escaped control sequence (`\\texttt`),
  and an escaped math delimiter (`\$`). An **unanchored marker is REFUSED**, and a boundary is never
  placed AFTER a delimiter.
- **G3** the flip family: every reading is run against a deliberately altered copy and must change
  its answer.
- **G4** classifier probes: each reading states which of its categories it assigned and why.
- **G5** reader probes **with NEGATIVE probes** (below).
- **G6** every prose probe runs on a **whitespace-FLATTENED** copy of the source.
- **Every verdict note is BUILT FROM its readings**, so it cannot contradict its own verdict.

## THE SIX STANDING NEGATIVE PROBES, EACH AIMED AT A SLIP THIS SEAT ACTUALLY MADE

1. a figure in the `.tex` but absent from the cited receipt ⇒ **NOT SUPPORTED**;
2. a variable bound in a later binder group after a `:` must still parse **BOUND**;
3. a conjunct under `∃` must **not** be reported at TOP;
4. a reading naming *which* comb must return **UNMEASURED** if the source does not distinguish;
5. a reading scoring two figures said to be the same quantity must **FAIL** when handed two that differ;
6. a dependence reading must be able to answer "does not rest on it" and still **FAIL** on a sentence
   that does.

## TWO NEW NEGATIVE PROBES THIS REVISION ADDS

7. **A hypothesis probe must distinguish "the hypothesis is stated" from "the hypothesis does the
   work."** Handed a statement line that names a hypothesis which the proof text never invokes, the
   reading must return **STATED-BUT-UNUSED**, not SUPPORTED.
8. **A reliance probe must be able to answer "nothing else relies on it" and still FIRE on a site
   that does.** Handed a copy of P1 with one extra passage reasoning from the OLD hypothesis set, the
   reliance reading must name that passage; on the unaltered P1 it must be able to return NONE.

---

## ARM 1 — DOES THE NEW HYPOTHESIS DO THE WORK?

`cor:threefold`'s statement (l.167) now reads "a smooth Lorentzian manifold **with no closed causal
curves**". (i) (l.170-171) now reasons "since a segment returning to the event it left would be a
closed causal curve".

Registered as a **three-way comparison**, scored by one predicate per clause (G1):

- **1a — SUFFICIENCY.** Does the stated hypothesis, together with the stated hypotheses on `γ` (a
  future-directed null geodesic segment joining `p,q` with `q ∈ ∂J⁺(p)`), entail `p ≠ q`?
- **1b — THE REASON AS GIVEN.** Does the reason *as written in (i)* derive `p ≠ q` from the stated
  hypothesis, or does it need a step the sentence does not state? Negative probe 7 governs: a
  hypothesis that is stated but not invoked returns **STATED-BUT-UNUSED**.
- **1c — 71's COUNTEREXAMPLE.** Is 71's witness (2D Minkowski modulo a null translation, where
  `p ∈ ∂J⁺(p)`) **excluded** by the new hypothesis? This is a check on the new hypothesis against the
  one object known to defeat the old one; it is recomputed from the construction, not recalled.

Reachable verdicts per clause, and each is a result: **SUPPORTED** / **NOT SUPPORTED** /
**STATED-BUT-UNUSED** / **TWO-TO-ONE** (one sentence carrying two claims) / **UNMEASURED** (the source
does not distinguish what the clause asks about).

⚠ The standing lesson applies: **a conjunct's QUANTIFIER is part of the claim.** "no closed causal
curves" is a claim about the WHOLE manifold `(M,g)`, not about `γ` or its neighbourhood; if the proof
needs only a local statement, or needs a strictly stronger one (e.g. causal simplicity, strong
causality, or stable causality), the gap between what is assumed and what is used is the finding.

## ARM 2 — DOES ANYTHING ELSE IN P1 RELY ON THE OLD WORDING?

A **reliance** reading, not a presence reading: the standing lesson is that **a dependence test is not
a correctness test**, and its converse — that *"there is a gap in the probe"* and *"the sentence rests
on a gap"* are two claims and only the second is about the paper.

Registered procedure: enumerate every site in P1 that (α) cites `cor:threefold` or any of its parts,
(β) states or restates the corollary's hypotheses, or (γ) reasons from "smooth Lorentzian manifold"
without the causality condition; then for each site decide, from its own text, whether its conclusion
**rests on** the old hypothesis set. Negative probe 8 governs: the reading must be able to return
**NONE** and must still fire on an injected site that does rely.

Reachable verdicts: **NONE RELIES** / **n SITES RELY** (each named with its line and its clause) /
**UNMEASURED** (a site whose reliance cannot be decided from its own text — recorded as owed, never
scored either way).

## ARM 3 — THE NEW PARAGRAPH AFTER `cor:threefold`, AGAINST `ThreefoldOrder.lean`

The paragraph (l.186) is **two sentences carrying several distinct claims**, and the standing lesson is
that **a citation is a claim that the probe proves the thing — so several citations on one paragraph
are several claims, and they can disagree.** Registered as one comparison per claim, each scored
through the same predicate (G1), each against the probe's own statement text read at source:

- **3a** "Part (ii) ... is machine-checked" — the scope claim: does `to_strict_null_order` state (ii)?
- **3b** "all four parts together on one pair ... machine-checked" — does `to_cor_1c` state all four
  on ONE pair? ⚠ **a label is attached by POSITION, not by presence**: four parts named in a
  statement is not four parts proved, and the pair must be the SAME pair in all four.
- **3c** "In the setting of Remark `rem:formalised`, with the metric `C¹` and the time orientation
  continuous in a chart about each point" — are these the probe's actual hypotheses, no weaker and no
  stronger?
- **3d** "if `q ∈ ∂J⁺(p)` then no event causally after `p` and causally before `q` lies in `I⁺(p)`" —
  the statement claim, read against the theorem's own binders. ⚠ **a claim about "no event" is a claim
  about a BINDER**, and a binder list is not found by looking for the first colon.
- **3e** "the proof pushes a chronological relation along a causal one and **uses no geodesic**" — a
  claim about the PROOF, not the statement. Registered as a reachable negative: if the proof body
  mentions a geodesic, this is **NOT SUPPORTED** even though 3d holds.
- **3f** the five conjuncts of the Rindler sentence — distinct / causally and not chronologically
  ordered / the later on `∂J⁺` of the earlier / null-separated along the generator / assigned
  `Δx = Δτ = 0` by the adapted splitting whose lapse vanishes there — each probed separately, and
  **"all in one theorem"** probed as its own sixth claim.

Reachable verdicts per claim: **SUPPORTED** / **NOT SUPPORTED** / **TWO-TO-ONE** /
**STRONGER-THAN-CLAIMED** (the probe proves more than the sentence says — a result, recorded, never
silently upgraded to SUPPORTED) / **UNMEASURED**.

## ARM 4 — THE SHELL-HORIZON SENTENCE, AGAINST `SchwarzschildShellHorizon.lean`

The sentence (l.384, sentence 12) carries **four conjuncts and one quantifier word**, and is registered
as five claims:

- **4a** "the exterior is the causal past of the observer";
- **4b** "its boundary is the future horizon **alone**" — ⚠ the word **alone** is exactly the word
  `r7688` found to be an unstated inference in the *eternal* sentence; here it is a DIFFERENT sentence
  about a DIFFERENT model, so it is a fresh claim and is read fresh. Does a probe state that the
  boundary is that horizon and nothing else?
- **4c** "at `r = r_h` once the shell has passed" — the locus claim, with its temporal qualifier;
- **4d** "and already formed inside the flat body before it arrives" — the formation claim, whose
  quantifier ("already", "before") is part of it;
- **4e** "the slicing is Cauchy on the exterior that horizon bounds".

Each of the three cited names (`sh_headline_D`, `sh_H_r`, `sh_H_flat`) is read at source and matched to
the claim(s) it can carry; a claim no cited name carries is **NOT SUPPORTED** even if some *other*
theorem in the file would carry it — and if such a theorem exists, that is recorded as
**MIS-CITED, SUPPORTED ELSEWHERE**, which is a distinct verdict and a distinct finding.

Same reachable verdicts as Arm 3, plus **MIS-CITED, SUPPORTED ELSEWHERE**.

---

## WHAT WOULD MAKE THIS REVISION WRONG

- A reading that returns SUPPORTED for a claim the probe does not state ⇒ the matcher answered about
  itself. Guarded by G1/G2/G3 and by negative probes 1, 5, 7.
- A reading that reports a conjunct at TOP that the probe states under a binder ⇒ negative probe 3.
- A reliance reading that returns NONE because it could not fire at all ⇒ negative probe 8.
- A verdict note that does not follow from its own readings ⇒ every note is BUILT from them.

## EXIT CODES REGISTERED IN ADVANCE

`0` every registered reading ran and its verdict is recorded (whatever the verdict).
`1` a reading could not be run, or a guard refused an anchor, or a negative probe failed to fire.
No other exit code is reachable; **no verdict is an exit code.**

## RECORDED NON-GOALS

- Nothing in `corpus/`, `receipts/`, `scripts/` or `computations/formalisation/` is edited. This is a
  READ. Every repair found is **routed** in `FOR_66_FROM_60.md` with its six-or-so words, never landed
  here.
- `r7685`'s item 2 stays **held by the order**: the own-comb block waits on cc66 again this turn, for
  its second paragraph, and the order says to hold.
