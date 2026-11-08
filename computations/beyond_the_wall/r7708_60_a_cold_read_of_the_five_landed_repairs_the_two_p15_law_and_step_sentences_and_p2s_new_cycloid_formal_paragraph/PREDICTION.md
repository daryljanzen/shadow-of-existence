# r7708 (60) — PREDICTION, registered before measurement

**Order answered:** `r7705` (69), the topmost section of `origin/main:FOR_60.md`. A cold read of
everything it says landed, **the two P15 law-and-step sentences FIRST** as the order directs,
and P2's NEW cycloid formal paragraph against `CircleCycloid.lean`.

**Tree:** `71f4c8f7` (`origin/main` = `r7705`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleCycloid.lean`
  (15,973 lines, 852,223 bytes). **Nothing inside it.**
- A directory listing of `receipts/P15_CR_cosmology/` filtered for the receipt names the order
  points at. **No receipt opened.**
- Nothing in P2 or P15 at source since the merge. The `r7706` readings of the OLD text are in
  this seat's own `r7706` RESULT, and the sites are revisited here at their NEW text.

## ITEM ① — THE TWO P15 LAW-AND-STEP SENTENCES (first, as ordered)

The order reports cc66's three sentences landed in P15, and flags one figure change itself:
**"a factor of about 1.8" replacing "a clean factor of two", against a computed 1.77–1.83.**

Registered as COMPARISONS, no verdict predicted:

- **1a** The printed figure is inside the computed interval, read from the receipt's own
  output and not from the order's summary of it. ⚠ The order says the computation gives
  1.77–1.83 and the sentence now says "about 1.8"; the arm checks BOTH that 1.8 is in
  1.77–1.83 and **what the interval is of** — a half-rise factor, a band ratio, a size — since
  a figure agreeing with an interval computed for a different quantity is `r7698`'s unstated
  denominator one level over.
- **1b** The sentence's claim about the step's SIZE is distinguished from its claim about the
  step's PLACE and its SHARPNESS. cc66 measured place and size agreeing and **sharpness
  failing** (resolved in the law, unresolved in the data at every window). So a sentence that
  says the law carries the step without naming the sharpness exception is a defect, and one
  that names it is not. **This predicate is registered now because afterwards the distinction
  will look obvious.**
- **1c** The attribution limit cc66 registered — that this is two statistics agreeing in place
  and size and differing in width, **not authorship**, since no switch removes a step the arms
  share — is either carried by the landed sentences or it is not. Searched by content in the
  sentences' own neighbourhood, not assumed from cc66's reply.
- **1d** Whether any OTHER P15 site still prints "a clean factor of two" or "a factor of two"
  for this step. A figure change that lands in one sentence and not its siblings is exactly
  `r7702`'s half-re-pointed site, and the search is by the printed figure in every spelling,
  not by the word "step".

## ITEM ② — THE FOUR REPAIRS THIS SEAT ROUTED AT `r7706`, READ IN PLACE

Each is read at source at its NEW text, with the `r7706` predicate re-applied rather than
assumed discharged:

- **2a** P2 `l.140`: "of vanishing Killing energy" added. Does the sentence now scope BOTH
  things it attributed — the cycloid FORM and `τ` as arc length — or only the nearer one?
  (`r7698`: a clause is confined by the SUBJECT it names.)
- **2b** P2 `l.460`: the parenthetical scoped, "the finiteness claim stays general". The arm
  checks that the finiteness clause is still general AND still true generally, which it is —
  `r7704` measured seven members, all finite — so a repair that narrowed it would be a
  REGRESSION, and that is the failure mode this arm is for.
- **2c** P2's formal paragraph: "wherever `h` vanishes at a non-degenerate critical point, a
  zero of order exactly two". Read against `ck_chain_rule`'s three hypotheses again, and the
  pole order recomputed here for a simple zero (6) and a double zero (12), so the sentence is
  checked against the arithmetic and not against this seat's memory of it.
- **2d** P2's formal paragraph: "away from the poles of the sphere's chart" added, "carrying
  `hs`". Read against `ck_horizon` and `ck_interior`'s actual binder `hs : Real.sin (x 2) ≠ 0`.
  `sin(x 2) ≠ 0` excludes `θ ∈ πℤ`, which is the two poles — the arm checks that the phrase
  names the same set the hypothesis does, since **a scope claim is a claim about its SUPPORT**
  (`r7700`) and "away from the poles" and `sin θ ≠ 0` could differ at the chart's edges.
- **2e** P15's scope sentence: the new wording and its stated plan to go back to both builds
  "once 70's converged FROZEN is pinned". Does the sentence now rest the DEPTH on the decoupled
  build alone and the SHAPE on both, which is what `70`'s measurement supports?

## ITEM ③ — P2's NEW CYCLOID FORMAL PARAGRAPH AGAINST `CircleCycloid.lean`

- **3a** Each of the six printed names — `cy_proper_time`, `cy_Mpi`, `cy_radial`, `cy_ends`,
  `cy_geodesic`, `cy_interior_forms` — exists as a declaration, spelled as printed.
- **3b** **THE HYPOTHESIS ARM.** Each theorem's binders listed from source, by the reader
  `r7706` repaired: bracket-depth matched (a flat type pattern cannot see a binder whose type
  carries parentheses), header-only (casts in the body are not binders), Unicode-aware
  (`hτ` was invisible to an ASCII pattern at `r7700`), and `include X in` read at its own
  one-declaration scope and across multi-line docstrings. **All four of those were MEASURED
  defects in this seat's own instrument one revision ago, so the reader is carried forward and
  re-tested, not rebuilt.**
- **3c** `cy_geodesic` and `cy_proper_time`: does the formalisation carry the `E = 0`
  restriction the prose now states, or is it stated for a general radial geodesic? **The
  reachable negative matters here: the formal statement may be MORE general than the prose
  (`r7700`'s outcome, no defect) or may silently assume the member (a defect), and the arm
  reports which.**
- **3d** `cy_Mpi`: is `πM` proved, or asserted as a value the chart is given?
- **3e** **"the chart is not pulled back from Kruskal" — A TEXTUAL ABSENCE CLAIM about a
  15,973-line file, and it gets a NAMED search**: Kruskal-side identifiers enumerated by
  marker, every hit's enclosing declaration read, the marker list and hit count reported, and
  `NOT FOUND` said as `NOT FOUND`. ⚠ AND THE TRAP IS KNOWN IN ADVANCE: this file is almost
  certainly another copy of the campaign kit, so Kruskal machinery will be present in
  abundance in the INHERITED part while being absent from the `cy_` part. At `r7706` the same
  shape appeared for "`z` is not built as a chart", and the honest reading was the per-region
  count, not the whole-file one. **The region boundaries are to be derived from the file, not
  guessed, and both counts reported.**
- **3f** Whether `cy_interior_forms` is NON-VACUOUS — a witness that the interior chart's
  conditions are met somewhere — since `r7698`'s `sa2_nonvacuous` and `r7706`'s
  `ck_interior_witness` both turned on exactly that, and a formal statement no point satisfies
  proves nothing about the paper's object.
- **3g** Axiom hygiene: `axiom` and `sorry` counts, and whether any axiom carries content the
  paragraph credits to a proof.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only (word boundary; escaped control
sequence with one leading backslash; escaped math delimiter) — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy of a conjunct. G4 classifier probes tested on BOTH
classes. G5 reader probes with negatives. G6 every prose probe on a whitespace-FLATTENED copy.
Every verdict note BUILT FROM its readings.

**The eighteen negative probes stand. The ones this revision is most exposed to:**
(15) a scope claim is a claim about its SUPPORT, so "away from the poles" and `sin θ ≠ 0` are
compared as SETS and not as glosses; (16) a figure search reads the LABEL beside each hit, so
"a factor of two" for this step is distinguished from a factor of two anywhere else — at
`r7706` two of six `Mπ`-shaped hits were the sphere's area; (17) NO DEFECT FOUND must stay
reachable by a reading, and five of the six items here are reports that a repair LANDED, so
the expected answer is largely "supported" and the instrument must be able to say otherwise;
(18) a tolerance is part of the instrument — no tolerance is loosened to make an arm pass.
**And newest, from `r7706`: (19) when an instrument misses the one site the order named, the
defect is in the FORM it was given — letter case, bracketing, the scope of a binder — so every
prose marker is matched case-insensitively and every reader is run on an example of each class
it is meant to separate, before it is used.**

**WHAT THIS REVISION CANNOT DO, registered before the numbers:** it cannot certify
`CircleCycloid.lean` as a proof. It reads declarations, hypotheses, axioms and statement
shapes. Whether each proof term closes is the Lean build's and `check_no_sorry`'s business, and
this probe says so rather than implying its readings are a verification.
