# r7712 (60) — PREDICTION, registered before measurement

**Order answered:** `r7709` (69). A cold read of the whole landing, and **three questions the
order puts directly**, which are the spine of this revision.

**Tree:** `d01ac482` (`origin/main` = `r7709`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleExterior.lean`
  (16,661 lines, 888,139 bytes). **Nothing inside it.**
- From `r7710`, and declared because it bears on question ③: the single line
  `def seW : Opens P := ⟨seWS, seWS_open⟩` and `abbrev P := ℝ × ℝ`. **`seWS` itself has not
  been read**, and what region it is is exactly what question ③ turns on.
- Nothing in P2 or P15 at source since the merge.

## QUESTION ① — IS "with the horizons at which they meet" RIGHT IN ALL FIVE PLACES?

The order says the identity claim now appears in five places — the abstract, the introduction,
`prop:four_regions`, its proof, and the formal paragraph — each carrying the horizons clause.

**Registered as a reading, with the predicate stated first:** the clause is right where the
claim is about the four patches AS A SET OF POINTS whose union needs the horizons to be the
whole extension, and it is **wrong or redundant** where the sentence's subject is something
else — the *curve*, the *analytic structure*, or a claim about what Kruskal does not contain.
So the arm is not "is the clause present five times" but **"is each of the five sentences a
claim the clause belongs to"**, and the five are read one at a time with their own subjects.

⚠ **AND THE TRAP, named now:** finding the clause in five places and reporting five
SUPPORTED is the cheap answer. **A place where the clause is redundant, or where it has been
attached to a sentence whose subject is the curve rather than the point set, is a defect of
the same family this seat has found six times — a clause confined by the SUBJECT it names
(`r7698`).** The expectation registered: at least one of the five is a sentence about
something other than the point set. Moderate confidence, no verdict predicted.

## QUESTION ② — DOES "Each patch is therefore isometric to the corresponding region" FOLLOW?

**This is the sharpest of the three, and the predicate is registered before the proof is
read.** What the proof sketch shows, on the order's own account, is **a match to the
Schwarzschild FORM in each domain of `r`** — an identity of metric COEFFICIENTS in a
coordinate chart.

> **An isometry needs two things: the coefficient identity AND that the chart map is a
> bijection onto the region.** A coefficient match alone gives an isometry onto the IMAGE of
> the map, which is the region only if the map is onto it.

So the arm is: does the proof sketch invoke injectivity-and-ontoness, or does "therefore" rest
on the coefficient match alone? ⌗ And the honest outcomes are three, which the probe must
separate: **(a)** the sketch cites or states the bijection, and "therefore" is sound;
**(b)** the bijection is established elsewhere — `cc_Φ_inj`, `ce_Ψ_inj` — but the SKETCH does
not reach for it, so the word "therefore" is doing work the sketch does not show and a
citation is owed; **(c)** nothing establishes it, and the claim is unsupported.
**(b) is what I expect, at moderate-to-high confidence**, because the order itself reports the
injectivity lemmas as separate items.

## QUESTION ③ — DOES "carries it onto the second exterior" SAY MORE THAN `ce_reflection` PROVES?

71 notes the second exterior lies outside `se_S`'s `W`. **Registered before reading `seWS`:**

- **3a** What region `seWS` is, read from its definition.
- **3b** Whether the second exterior (`U > 0 > V`, by the reflection of `U < 0 < V`) lies
  inside it. ⚠ **A prediction I am recording because it may be wrong and the arm must survive
  that:** if `seWS` is `{UV < 1}` then `U > 0 > V` has `UV < 0 < 1` and the second exterior
  would be INSIDE it, which would contradict 71's note. **So either `seWS` is narrower than
  `{UV < 1}`, or 71's note is about something else — and the probe reads the definition rather
  than deciding between them from memory.** `r7710` read only the one-line `def seW`, never
  `seWS`, so this is genuinely open.
- **3c** What `ce_reflection` actually states: a map ONTO the second exterior, or that the
  reflection PRESERVES `r` and the coefficients wherever both sides are defined. Those are
  different claims, and "carries it onto" asserts the first.
- **3d** If the second exterior is outside the spacetime's domain, then "carries it onto the
  second exterior" names a target the formalisation does not contain — **which would make the
  prose's claim about an object the theorem cannot mention, the `r7700` support question in
  its sharpest form.**

## ITEM ④ — THE REST OF THE LANDING

- **4a** P2's repaired clauses, at source: "on that plane"; "into the radial plane of that
  manifold, onto the black-hole interior `U, V > 0`"; and `cc_Φ_inj` cited beside
  "one-to-one". ⚠ **AND ONE THING TO CHECK RATHER THAN ACCEPT: "onto the black-hole interior
  `U, V > 0`"** — the interior of a Kruskal diagram is usually `UV > 0` with both positive for
  the future interior; whether `U, V > 0` is the region the theorem's hypothesis names is a
  reading, not a given.
- **4b** `ce_Ψ_inj`, `ce_pullback`, `ce_reflection` exist as declarations, spelled as printed,
  with their binders listed by the reader carried forward.
- **4c** P15's `about three per cent`: the receipt computes `3.23` and its gate text says
  "about 3 per cent". Read both at source, and check the collision with the converged build's
  `3.2` is gone — **which is this seat's own `r7710` finding, so the arm is whether the repair
  removed the collision or moved it.**
- **4d** Axiom and `sorry` counts for the new file.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.

**The twenty negative probes stand. The ones this revision is most exposed to:** (15) a scope
claim is a claim about its SUPPORT — questions ① and ③ both; (17) `NO DEFECT FOUND` must stay
reachable, and here the order reports repairs landed, so "supported" is the expected answer and
the instrument must be able to say otherwise; (19) an instrument reads the FORM it was given,
and a NAME is a form, so declarations are found by the SHAPE of their conclusions as well as by
name; (20) a REPLACED sentence may have changed its subject, so no verification transfers.
**And newest, from `r7710`: (21) a "therefore" is a load-bearing word. When a conclusion is
stronger in KIND than what precedes it — a coefficient identity to an isometry, a bijection to
an identity of spacetimes — the step is the claim, and it is read rather than granted.**

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, and it cannot
settle a geometric fact the files do not state. Where question ② or ③ turns on something
outside the files, that is NAMED as outside and not supplied.
