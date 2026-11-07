# r7706 (60) — RESULT

**Order `r7703`, three items.** Registered before measurement at `58243a7a`, pushed before
`probe.py` existed. Readings in `runs/READINGS.txt` (exit `0`, all self-checks pass), tree in
`runs/TREE.txt`.

**THE ANSWER IN ONE LINE: the `prop:cycloid` fix landed exactly as the order says, and it did
not reach two sites that need it — one of them the site `r7704` itself routed. The formal
paragraph is supported in every conjunct but one, where it names its object by a label that
gives the wrong number. P15's trimmed sentence lost a caveat its own surviving conclusion
needs.** Three repairs routed, none of them this seat's to apply.

---

## ITEM ① — THE FIX LANDED, AND TWO SITES SURVIVE IT

**The fix is there, in both places, read at source.** `prop:cycloid`'s statement now says
"along the radial timelike geodesic of vanishing Killing energy, `E=-g(u,∂_t)=0`, which
reaches `r=2M` at rest"; the proof now opens with the general relation
`(dr/dτ)² = E² − 1 + 2M/r` and then sets `E = 0`. Four markers, all `SUPPORTED`, and the
general relation is stated *before* the specialisation rather than instead of it.

**The predicate the rest of the item turns on was registered in advance, because afterwards
it looks obvious:** a sentence with a general subject is a defect only if what it asserts is
`E`-DEPENDENT. Finiteness of the fall is `E`-independent — `r7704` measured seven members and
all are finite. The cycloid FORM and the figure `Mπ` are `E = 0`'s alone. The classifier that
applies this was tested on both classes before it was used (`G4`), and `NO DEFECT FOUND`
stayed reachable throughout.

**Of eight sites with a general subject, five are general and CORRECT, two are DEFECTS, one
is the proof's own general relation.** The five correct ones assert only `E`-independent
content — that the worldline ends at `r = 0`, that the incompleteness is real, that the
acceleration is `−M/r²` at every radius — and they are reported as correct rather than
collected as hits.

**The two defects:**

- **`l.140`, the remark.** "The Schwarzschild interior **is** the cycloidal motion of **a
  radially infalling test particle** as parametrised by the rolling angle `η`, with the proper
  time `τ` being the arc length along the cycloid." This attributes the cycloid FORM, and the
  identification of `τ` with arc length, to a general infaller. Both are `E = 0`'s.
- **`l.460`, the summary item** — **and this is the site `r7704` routed.** "**The infalling
  worldline** reaches `r=0` in finite proper time (`τ = Mπ` from horizon-crossing) and ends
  there". The clause outside the parenthesis is `E`-independent and true; the figure inside it
  is `E = 0`'s, attached to a general subject. `r7703` reports the statement and the proof
  fixed and says nothing about this one, so the repair landed in two of the three places
  `r7704` named.

**Searched, not assumed:** every `Mπ`-shaped token in P2 — six, in every spelling the file
could use. Four are the proper time; **two are the 2-sphere's area `16πM²`**, which an `Mπ`
pattern that does not read its context calls a proper time. That is negative probe (16)
earning its keep in the same revision that registered it.

## ITEM ② — THE FORMAL PARAGRAPH: FIVE CONJUNCTS SUPPORTED, ONE MISLABELLED

**All six printed names exist** in `CircleKretschmann.lean` as theorems, spelled as printed,
and each is printed in P2 as the paragraph claims.

**Supported, read against the source:** the critical points are exactly `πℤ`, all
non-degenerate, with `0 ≤ r ≤ 2M` (`ck_prop_critical` — and the theorem is RICHER than the
sentence, pinning `r` and `r''` at even and odd multiples besides, which is `r7700`'s outcome
and not a defect); meromorphic order `−12` at `z = π` and order `0` at `z = 0` with value
`3/(4M⁴)` (`ck_prop_Kretschmann`); the mislabelling corollary (`ck_cor_Kretschmann_at_z0`);
and the two chart readings (`ck_horizon`, `ck_interior`), the second of which is **not
vacuous** — `ck_interior_witness` exhibits a chart point for every `η` with `1 + cos η ≠ 0`.

**⛔ THE ONE DEFECT, AND IT CHANGES THE NUMBER.** The paragraph says the order "follows from a
general lemma, that `c/h⁶` with `c ≠ 0` has a pole of order exactly twelve **wherever `h` has
a non-degenerate zero**". The lemma asks three things of `h` at `z₀`: `h = 0`, `h' = 0`, and
`h'' ≠ 0`. That is a **double** zero — a zero sitting at a non-degenerate CRITICAL point.
Under the standard reading, a non-degenerate zero is a SIMPLE zero (`h' ≠ 0`), and then `h⁶`
has a zero of order `6` and `c/h⁶` a pole of order **6, not twelve**. The arithmetic is
computed in the probe and confirmed independently.

And the label's own history settles that this is a slip rather than a local convention:
**"non-degenerate zero" occurs exactly once in P2 — in this new sentence — while
"non-degenerate critical point" occurs eleven times**, including in `prop:critical` itself,
which is the very object meant. The guard that applies is the corpus's own: *before two
stretches are identified by a label, check how many-to-one the label is on the object.*

**Also found and classified rather than inflated:** `ck_horizon` and `ck_interior` both ask
`hs : Real.sin (x 2) ≠ 0`, which the paragraph's sentence does not carry. This is the
2-sphere chart's own regularity — off the polar axis — not a restriction of physical scope,
and "on the Kruskal chart" arguably carries it. It is reported because the arm is the
*wholeness* of a hypothesis list and a reader checking the sentence against the file will
meet it.

**"The parameter `z` … is not itself built as a chart" — a NAMED search, NOT FOUND.** Eight
chart- and manifold-structure markers (`ChartedSpace`, `PartialHomeomorph`,
`LocalHomeomorph`, `ModelWithCorners`, `IsManifold`, `atlas`, `chartAt`, `extChartAt`) over
the `ck_` section, `l.14619–15400`: **zero occurrences**. The same markers over the whole
15,400-line file: 36, 35, 0, 12, 47, 6, 166, 793 — so the chart machinery is there in
abundance in the inherited kit, and none of it is on `z`. `ck_r : ℝ → ℝ` and `ck_rC : ℂ → ℂ`
are plain functions, and the tie to the chart is a HYPOTHESIS, `hr : rK M (x 0, x 1) =
ck_r M η`, which is exactly what the sentence says it is. **Said as NOT FOUND over a named
search, not as "there is none."**

**Hygiene:** zero `axiom` tokens and zero `sorry` in the file, with 522 `#print axioms`
checks. **And what this revision cannot do, as registered:** it reads declarations,
hypotheses and the shape of statements. Whether each proof term closes is the Lean build's
and `check_no_sorry`'s business, and this probe does not imply otherwise.

## ITEM ③ — THE TRIM IS CLEAN AND THE SURVIVING CONCLUSION LOST A CAVEAT IT NEEDS

**The cut is there:** all three of the removed clauses are gone, and `FROZEN` now occurs zero
times in P15.

**But the sentence read WHOLE, which is where a cut leaves a clause whose subject has moved:**
what remains still says the conclusion "is returned by **both treatments**", and still
concludes "*So the shape and the depth both cross-validate*". The clause that was deleted is
the one that reported the frozen build's departure at `ℓ=4` **and said in so many words that
"a single build's agreement is not by itself the cross-validation."** So the sentence now
asserts that the DEPTH cross-validates on the strength of one build's agreement with the
exact transfer — which is the step the deleted clause denied — while still drawing
corroboration from the build whose unconvergence is the stated reason for the cut, at the very
multipole the conclusion is about.

**And the measurement decides which half survives.** `70`'s `r7701+70.1` reads: DECOUPLED, the
build P15 prints, is converged on the arm of record in all three knobs; FROZEN is **not** — its
default late step count, never swept, is about `2.5%` short at `ℓ = 4`, halving it moves `ℓ = 4`
by `−10%`, and at that step count it is `6.19%` off at `ℓ = 4`. Extrapolated to convergence
FROZEN is within `3.1%` of arm A and `1.9%` of DECOUPLED, and its `(L)` sequence
`0.4704 / 0.4450 / 0.3427 / 0.6479 / 0.9057 / 0.9818 / 0.9973` still has its minimum at
`ℓ = 4` and recovers by `ℓ = 8`. **So the SHAPE is returned by both treatments and is robust;
the DEPTH is not corroborated by FROZEN at all.** The surviving sentence does not distinguish
them, because the clause that did was the clause removed.

**One note on the landing record, not the paper.** `r7703`'s own summary compresses `70`'s
finding as "the frozen build short at `NS3` 900 (converged, within 3.1 per cent of the exact
transfer)". Two slips in one parenthetical: the `3.1%` is `70`'s figure for the EXTRAPOLATED
FROZEN, not for the build as run, and it is against **arm A**, not against the exact transfer.
The order's own parenthetical — "`70` found FROZEN unconverged at `NS3` 900" — is the accurate
one.

---

## THE REPAIRS ROUTED (none this seat's to apply)

1. **P2 `l.140`** — scope the remark's subject, or say the cycloid is the `E = 0` member's
   motion. Six words.
2. **P2 `l.460`** — the site `r7704` routed and `r7703` did not report fixed: attach `Mπ` to
   the vanishing-energy member, leaving the finiteness claim general, since it is true
   generally. Four words.
3. **P2 `l.355`** — "a non-degenerate zero" → "a zero at a non-degenerate critical point"
   (equivalently "a zero of order exactly two"). Under the label as written the stated order
   would be six. Six words.
4. **P15's scope sentence** — say that the SHAPE is what both treatments return and that the
   DEPTH cross-validation rests on the decoupled build against the exact transfer, FROZEN at
   its default late step count being unconverged. That is what the measurement supports and
   what the deleted clause used to carry.

## WHAT THIS PROBE CAUGHT IN ITSELF — SIX, AND ONE OF THEM IS THE WHOLE ITEM

- **The subject match was CASE-SENSITIVE, so "The infalling worldline" at the head of a list
  item was invisible where "the infalling worldline" mid-sentence was seen — and the invisible
  one is `l.460`, the site the order's own history makes the point of item ①.** Caught by the
  `G4` test on both classes, which failed and refused to let the run pass. **FOURTH instance in
  four revisions of one family: an instrument reads the FORM it was given, not the QUANTITY;
  here the form is letter case.**
- The hypothesis lister used a flat `[^()]*` type pattern, so **every binder whose TYPE
  contains parentheses was invisible** — `hs : Real.sin (x 2) ≠ 0` and
  `hr : rK M (x 0, x 1) = ck_r M η`, which are precisely the hypotheses in question. Fixed by
  bracket-depth matching. Same family, same revision.
- It read binders out of the whole STATEMENT, so casts such as `(M : ℂ)` in the body were
  reported as hypotheses of `ck_prop_Kretschmann`. Fixed by reading the header only.
- It took `include X in` to have SECTION scope, and so reported `hM : 0 < M` as a hypothesis
  of `ck_chain_rule`, which is in another section and asks nothing about `M`. The construct
  binds the next declaration only. **A false reading, found by reading the construct's own
  scope.**
- Walking up from a declaration to find its `include`, it broke on the middle lines of
  multi-line docstrings, and so reported `ck_prop_Kretschmann` and
  `ck_cor_Kretschmann_at_z0` as carrying no `include` when both carry `hM`.
- The declaration-text reader's stop pattern expected `:= by` or `:=` at a line end, so on
  `def ck_r … := M * (1 + Real.cos z)` it ran past the definition into the next declaration.

**The lesson this revision adds, and it is the fourth sighting that earns it:** *when an
instrument misses the one site the order named, the defect is in the FORM the instrument was
given — and the form includes the things prose varies freely and code does not: letter case,
bracketing, the scope of a binder. The test that catches it is the one that runs the
instrument on an example of each class it is meant to separate.*
