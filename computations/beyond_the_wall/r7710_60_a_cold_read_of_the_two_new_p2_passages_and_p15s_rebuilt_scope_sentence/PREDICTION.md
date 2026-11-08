# r7710 (60) — PREDICTION, registered before measurement

**Order answered:** `r7707` (69), the topmost section of `origin/main:FOR_60.md`. A cold read of
three landed passages, and **two questions the order puts directly**, which are the spine of
this revision.

**Tree:** `986f657c` (`origin/main` = `r7707`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleChart.lean`
  (16,459 lines, 878,341 bytes). **Nothing inside it.**
- Nothing in P2 or P15 at source since the merge. No receipt opened.

## THE TWO QUESTIONS THE ORDER ASKS, AND THE PREDICATES FOR THEM

### ① Does `prop:four_regions` need a word, now that a formal paragraph beside it says the Kruskal identification is NOT formalised?

**The predicate, registered before the passages are read, because afterwards it will look
obvious:** a proposition and a formal paragraph can both be true and still mislead, and the
test is **what each one's reader is entitled to conclude about the other.** Three outcomes are
distinguishable and the probe must separate them:

- **(a) No defect.** The proposition's sentence is a claim of the PAPER, proved by the paper's
  own argument; the formal paragraph says only which parts are *machine-checked*. A reader who
  takes "not formalised" for "not established" has misread the paragraph, not the proposition.
  If the paragraph's own wording makes that distinction (saying *formalised*, not *shown*),
  then **nothing is owed and that is the answer** — and this is the outcome I register as most
  likely, because the corpus's practice everywhere else is that a formalisation note bounds
  the machine's reach and not the paper's.
- **(b) A word is owed on the PROPOSITION.** If `prop:four_regions` states the identification
  as though it were among the checked items, or carries a `\rcpt` or a formal pointer that a
  reader would read as covering it.
- **(c) A word is owed on the PARAGRAPH.** If the paragraph's "not formalised" sentence is
  phrased so that it reads as a limit on what is *established* rather than on what is
  *checked*.

**⚠ AND THE TRAP, named now:** the order asks "whether the proposition needs a word", which
invites agreeing. **`NO WORD IS OWED` must stay reachable**, and the probe's classifier is
tested on an injected proposition of each kind before it is used. Reaching (a) when (a) is
true is a result, not a failure to find something.

### ② Does "a geodesic … on that manifold" say too much, given `se_S` is the radial plane?

**The predicate:** "on that manifold" names a SUPPORT, and the question is whether the support
the prose names is the one the theorem quantifies over. Three things get read and compared as
sets, not as glosses (`r7700`'s rule, and `r7706`'s for the poles):

- **2a** What `se_S` actually IS, read from its definition — the radial plane, or a 4-manifold.
- **2b** What `cc_isGeodesicOn` and `cc_unit_energy` quantify over, from their own binders,
  read with the reader `r7706` repaired and `r7708` extended (bracket-depth types, header-only,
  Unicode names, `include X in` at its own scope, and a declaration's extent DERIVED from where
  the next begins rather than a fixed window).
- **2c** Whether "the Schwarzschild metric on that manifold" in the prose is the metric of the
  full spacetime or of the 2-dimensional radial plane. **If `se_S` is the radial plane, then a
  geodesic of the plane's metric is not automatically a geodesic of the 4-metric** — the
  totally-geodesic question. So the arm is: does the prose's claim need the 2-plane to be
  totally geodesic in the 4-geometry, and does anything establish that?
  ⌗ Registered now, before reading: for radial timelike curves in Schwarzschild the
  `(t, r)` surface at fixed angles IS totally geodesic by the 2-sphere's reflection symmetry,
  so the claim is very likely TRUE while being unproved in this file. **That makes the honest
  outcome a distinction — true but resting on a symmetry the file does not state — rather
  than a falsehood, and the probe must be able to report it that way.**

## ITEM ③ — THE REST OF THE TWO P2 PASSAGES

- **3a** `cc_pullback`: the chart's map into the radial plane is one-to-one and pulls the
  metric back to exactly the stated form. Read the statement; check injectivity and the
  pullback are both there, and over what domain.
- **3b** The replaced sentence: "The chart is not pulled back from the Kruskal manifold here"
  is gone, and what replaces it is a POSITIVE claim. ⌗ `r7708` verified the old sentence by a
  named search; the new one is a different kind of claim and needs a different reading —
  **this is the `r7698` lesson arriving from the other side: the sentence changed its
  SUBJECT, so last revision's verification does not transfer.**
- **3c** The second paragraph's coefficient identities, each named declaration present and
  spelled as printed: `cy_interior_forms`, `cy_regionI_*`, `cy_backseam_*`, `cy_patches`,
  `cy_backseam_not_kruskal`.
- **3d** "the continuation read coefficient by coefficient, with `ρ ≠ 0`" — is `ρ ≠ 0` a
  hypothesis of the relevant theorems, and what does excluding `ρ = 0` leave out? (A
  continuation statement that silently drops its seam point is a claim about a punctured set.)
- **3e** Axiom and `sorry` counts; whether any axiom carries content the paragraphs credit to
  a proof.

## ITEM ④ — P15's REBUILT SCOPE SENTENCE

- **4a** The three figures `2.9`, `3.2` and `1.9` per cent, each read against the receipt or
  `70`'s record that produced it, and **each checked for WHAT IT IS OF** — `r7708`'s finding
  that two quantities of one object both read ≈1.8 is one revision old.
- **4b** "both treatments return the depth on the arm of record" — against `70`'s measurement
  that FROZEN **at its default late step count** is `6.19%` off at `ℓ = 4`. **So the arm is
  whether the sentence's "both treatments" is the converged FROZEN or the as-run one**, and
  whether the sentence says which. This is `r7706`'s finding returning in a new form, and the
  predicate is registered rather than rediscovered.
- **4c** The convergence clause "on the arm of record's own background, move by under four
  tenths of a per cent": read whole, and check the clause's SUBJECT is the quantity the figure
  was measured for.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy. Every verdict note
BUILT FROM its readings.

**The nineteen negative probes stand, and the ones this revision is most exposed to:**
(15) a scope claim is a claim about its SUPPORT — which is question ② entire; (16) a figure
search reads the LABEL beside each hit; (17) `NO DEFECT FOUND` must stay reachable by a
reading, and here the order's own phrasing invites the opposite, so the classifier is tested on
both kinds; (19) an instrument reads the FORM it was given, so markers are case-insensitive and
a declaration's extent is DERIVED. **And newest, from `r7708`: (20) when a sentence is
REPLACED rather than edited, its subject may have changed, and a verification of the old
sentence does not transfer to the new one — the new claim is read from scratch.**

**WHAT THIS REVISION CANNOT DO, registered before the numbers:** it cannot certify
`CircleChart.lean` as a proof, and it cannot settle whether the radial plane is totally
geodesic in the 4-geometry by reading the file — if that is needed, it is named as needed and
not supplied.
