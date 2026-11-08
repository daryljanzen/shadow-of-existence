# r7716 (60) — PREDICTION, registered before measurement

**Order answered:** `r7713` (69). A cold read of P2's new back-seam sentence, and **the three
questions the order puts directly**.

**Tree:** `d3fd0896` (`origin/main` = `r7713`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CircleBackSeam.lean`
  (17,271 lines, 918,583 bytes). **Nothing inside it** — `bs_coeffs`, `bs_SD`, `bs_kretschmann`
  and `bs_backseam` have not been read, and what they state is what all three questions turn on.
- From `r7714`, and declared because question ③ compares against it: the proof sketch's own
  sentence, *"they lie beyond the Kruskal extension, and their geometric identity---the backward
  radial direction, the negative root of the horizon cubic---is established in the companion
  slicing paper"*, read at source last revision and **not re-read since the merge**.
- Nothing else in P2 at source since the merge. **No receipt.**

## QUESTION ① — IS "covering every `r < 0`" WHAT `bs_backseam`'s FIRST CONJUNCT PROVES?

**The predicate, registered first: "covering" is a word about a MAP'S IMAGE, or about a set being
contained in a union — and neither is the same claim as a chart being DEFINED at each `r < 0`.**
So the arm is to read the first conjunct's conclusion and compare it, as a statement, with the
phrase. The outcomes the probe must separate:

- **(a)** the conjunct states surjectivity onto `{r < 0}` — some `∀ r < 0, ∃ (point)` with the
  chart's radius function equal to `r` — and the phrase is exactly it;
- **(b)** it states that the chart is **defined** for every `r < 0` (a domain claim), which is
  close and is **not** the same thing, since a domain can be defined everywhere and still not
  reach every radius;
- **(c)** it states something else again — monotonicity of the tortoise coordinate, a local
  identity — and "covering" overreaches.

⚠ **The trap, named now:** the order asks "whether", which invites **no**, and a phrase can be
TRUE and still not be what its citation proves. **NO DEFECT must stay reachable**, and the
decisive reading is registered in advance: **does the conjunct quantify over `r` and produce a
point, or over points and produce an `r`?** The first is covering; the second is not.
⌗ `r7700`: a scope claim is a claim about its SUPPORT. No verdict predicted.

## QUESTION ② — DOES "a geometry in their own right" CLAIM MORE THAN THE CITATIONS GIVE?

**This is the sharpest of the three, and the predicate is registered before the file is read.**
What the order reports as checked is a LIST OF PROPERTIES: `f = 1 − 2M/r > 1` so no horizon;
`f` and `f⁻¹ → 1` as `r → −∞`; a null chart built from the tortoise coordinate; the Kretschmann
scalar `48M²/r⁶` away from the sphere chart's poles, tending to zero.

> **"A geometry in their own right" names an OBJECT — a spacetime, with a carrier and a metric —
> and a list of properties of coefficient functions is not an object.** The two previous
> revisions turned on exactly this distinction: `se_S` and `sk_S` ARE constructed objects
> (`MSpacetime P seW`, `MSpacetime P Pt`), and that is what let their claims be about regions.

So the arm is: **is a spacetime object CONSTRUCTED in this file for the `r < 0` patches, or are
only coefficient functions and a scalar computed?** Three outcomes: an object with its own
carrier exists and the phrase is right; only coefficients and a scalar exist, and the phrase
claims an object the file does not build, which is a repair of one phrase; or an object exists but
over a domain narrower than "the two `r < 0` patches", which is a third thing again.
⌗ **And a second arm on the same sentence, from the corpus's own guard — *if the hedge is
load-bearing it belongs in the stem*:** "away from the poles of the sphere's chart" is a hedge on
the Kretschmann claim. Whether it is load-bearing is read from the declaration's hypotheses, not
from the prose.

**⌗ THE NEGATIVE PROBE THIS QUESTION WOULD BUY, registered as a candidate and not yet claimed:**
*a phrase that names an OBJECT is not discharged by a list of that object's properties — the
check is whether the object is CONSTRUCTED.*

## QUESTION ③ — DOES THE SENTENCE SIT CONSISTENTLY BESIDE THE PROOF SKETCH'S COMPANION-PAPER CLAUSE?

The sketch sends the `r < 0` patches' **geometric identity** to the companion slicing paper; the
new formal sentence says they are **machine-checked as a geometry in their own right**.

**Registered before re-reading either:** these are the same words only if "geometric identity" and
"a geometry in their own right" name the same claim, **and they may not** — *which* geometry a
patch is (the backward radial direction, the negative root of the horizon cubic) is a different
question from *that* it is one (horizonless, asymptotically flat, with a finite curvature scalar).
So three outcomes: **consistent**, because the two claim different things, and then at most one
word is owed to make the division visible; **in tension**, because both claim the identity and one
of them is then either redundant or contradicted; or **the formal sentence claims less than the
sketch**, in which case the sketch's citation is doing work the paragraph appears to withdraw.
⌗ **Consistent must stay reachable** — the order asks "whether", and two sentences can divide
labour without either being wrong.

## ITEM ④ — THE REST OF THE LANDING

- **4a This seat's half-repair, as landed:** *"each chart map being onto its quadrant of the
  domain, horizons excluded"* with `cp_onto_BH`, `cp_onto_RE` and `cp_kruskal` cited. Arm: whether
  **"horizons excluded"** is right — the quadrants are open and the horizons are `cp_kruskal`'s
  own fifth set, so the phrase should be exactly that, and it is read rather than assumed.
- **4b The last sentence, now "That the Kruskal–Szekeres extension is maximal is not
  formalised."** ⚠ **It was REPLACED and not edited (negative probe 20), so `r7714`'s reading of
  the old one does not transfer:** the old sentence bounded TWO things and this one bounds one,
  and whether the thing it dropped is now covered is the arm.
- **4c** `bs_coeffs`, `bs_SD`, `bs_kretschmann`, `bs_backseam` exist as declarations, spelled as
  printed, with their binders listed; names matched by **SKELETON** and not by literal character.
- **4d** `axiom` and `sorry` counts for `CircleBackSeam.lean`.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.

**The twenty-two negative probes stand, and the readers `r7714` repaired are carried forward and
re-tested on their negatives before use.** The ones this revision is most exposed to: (15) and
(17) — the order reports a landing, so "supported" is expected and the instrument must be able to
say otherwise, and must equally be able to say SUPPORTED where a question's phrasing invites a
defect; (19) a NAME is a form; (20) a REPLACED sentence may have changed its subject, which bites
at 4b; (21) a load-bearing word is read and not granted — here "covering" and "a geometry"; (22) a
named search over SOURCE cannot find a value that exists only at RUN TIME.

**⌗ AND THE LESSON FROM LAST REVISION, WHICH COST THREE ARMS: `r7714`'s three instrument defects
were all one shape — a statement read for a SYMBOL or a LITERAL rather than for its SHAPE.** So
every arm here is written as **an assertion that can FAIL**, never as a search that can quietly
return nothing, and every reader is given a negative of the opposite class before it is used.

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, it cannot read the
companion slicing paper, and it cannot settle a geometric fact the files do not state. Where a
question turns on something outside the files, that is NAMED as outside and not supplied.
