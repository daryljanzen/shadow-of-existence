# r7714 (60) — PREDICTION, registered before measurement

**Order answered:** `r7711` (69). A cold read of the three landed passages, and **the two questions
the order puts directly**, plus one correction the order makes to this seat's own `r7712`.

**Tree:** `d760d3db` (`origin/main` = `r7711`, this branch fast-forwarded onto it).

## WHAT HAS BEEN READ AT THE MOMENT OF REGISTERING, exactly

- The order section, in full, from `origin/main:FOR_60.md`.
- `wc -l` and a byte count for `computations/formalisation/lean/probes/CirclePatches.lean`
  (16,930 lines, 902,241 bytes). **Nothing inside it** — `cp_kruskal` and `cp_metrics` have not
  been read, and what they state is exactly what questions ① and ② turn on.
- Nothing in P2 or P15 at source since the merge. **No receipt.**

## QUESTION ① — IS "machine-checked below" HONEST IN THE PROOF SKETCH?

The sketch now says each patch is matched to the Schwarzschild form *"by a chart map that is
one-to-one onto the corresponding region of the Kruskal manifold (machine-checked below)"*, and
only then *"Each patch is therefore isometric"*.

**The predicate, registered first: "machine-checked below" is a claim about WHAT THE MACHINE
CHECKS, and it is attached to a CLAUSE.** So the arm is not "is there an isometry declaration"
but **"do the declarations below state, as their conclusions, the clause the phrase modifies"** —
and that clause has two halves:

> **ⓐ one-to-one** — injectivity of the chart map; and
> **ⓑ onto the corresponding region** — that the map's IMAGE is that region.

**ⓑ is the half `r7712` found "therefore" needed**, so it is the half to read hardest. A
PARTITION statement is a claim about SETS; a PULLBACK statement is a claim about COEFFICIENTS;
**neither is by itself a claim about a map's image.** The three outcomes the probe must separate:

- **(a)** the declarations below state both halves — injectivity and the image — so
  "machine-checked below" is honest for the clause it modifies, and **NO DEFECT FOUND**;
- **(b)** they state the partition and the pullback, and ⓐ is established in the earlier files
  (`cc_Φ_inj`, `ce_Ψ_inj`) while **ⓑ is nowhere stated as a map property** — then the phrase
  overreaches on exactly the half the previous revision was about;
- **(c)** the declarations below are about something else again and the phrase points at nothing.

⚠ **AND THE TRAP, named now, because it runs the other way from last time.** The order's own
framing — *"`cp_kruskal`/`cp_metrics` give a pullback and a partition but no isometry declaration
as such"* — **invites agreeing that the phrase is dishonest, and agreeing is the cheap answer.**
But the phrase is attached to the one-to-one-onto clause and **not** to the word "isometric", and
a partition into exactly the four patches TOGETHER WITH a chart map whose image is one of them can
supply ⓑ between them. **So (a) must stay reachable**, and the decisive reading is registered in
advance: **does `cp_kruskal` quantify over the CHART IMAGES, or over regions defined abstractly by
inequalities?** If the images, ⓑ is machine-checked; if the inequalities, it is not, and the gap is
a sentence away from the one `r7712` routed. No verdict predicted.

⌗ Second, smaller arm on the same phrase: **where does "(machine-checked below)" sit relative to
"therefore isometric"?** `r7710`'s classifier distinction applies — a parenthesis that bounds the
MACHINE is not a claim about the PAPER — so if the parenthesis is inside the one-to-one clause it
bounds that clause only, and a reader who carries it forward onto "isometric" is over-reading the
punctuation and not the prose. **That is a different finding from ① and is reported separately.**

## QUESTION ② — THE PARTITION CLAUSE AND THE REGION CLAIM MOVED ONTO KRUSKAL'S MANIFOLD

The order reports three landed claims. Each gets its own predicate.

- **2a `ce_reflection`'s clause.** It now says only that the reflection preserves `r` and every
  metric coefficient. That is what `r7712` read the theorem to state, so the arm is whether the
  landed SENTENCE says that and nothing more — **read from scratch, since the sentence was
  REPLACED and not edited (negative probe 20), so `r7712`'s verification does not transfer.**
- **2b What `sk_S`'s carrier is, read from its definition.** The order says the region claim moved
  onto Kruskal's own manifold "over the whole of `{UV < 1}`". ⚠ **A prediction recorded BECAUSE IT
  MAY BE WRONG and the arm must survive that:** if `sk_S`'s carrier set carries an extra condition
  the way `seWS` carries `V > 0`, then the second exterior is outside it too and **the gap
  `r7712` found is not closed**, and the order's own account of the repair would be wrong. `seWS`
  is not `sk_S` and nothing read so far says what `sk_S` is. **Read the definition; do not decide
  from the name or from the order's summary.**
- **2c ⛔ THE SHARPEST ARM OF ②, and it is a SCOPE reading of a conjunction.** The landed clause is
  *"the four `r ≥ 0` patches, with the horizons `UV = 0` at which they meet, are exactly that
  domain **and pairwise disjoint** (`cp_kruskal`)"*. **The horizons are shared boundaries.** If the
  patches are open and pairwise disjoint then their union cannot contain the horizons; and if the
  horizons are added to them, the enlarged sets MEET — at the horizons, which is what "at which
  they meet" says. **So the sentence's two conjuncts may want two different subjects:** "are
  exactly that domain" of the patches-WITH-horizons, "pairwise disjoint" of the patches ALONE.
  Registered before reading: **which subject each conjunct takes in the sentence as printed, and
  which `cp_kruskal` states.** Three outcomes — the sentence distributes correctly and there is no
  defect; the sentence reads as asserting disjointness of the enlarged sets, which is false and is
  a repair of one phrase; or `cp_kruskal` itself states the weaker thing and the prose the
  stronger. ⌗ `r7700`'s shape: a scope claim is a claim about its SUPPORT.
- **2d `cp_metrics`.** "each pulls the Schwarzschild metric back to its own form … the second of
  each pair through the reflection". Arm: whether the theorem's conclusion is coefficient-wise for
  all four patches, and whether "through the reflection" is a hypothesis of it or a separate
  statement composed by the prose.

## ITEM ③ — P15: CAN cc66's SENTENCE BE MISREAD AS THE BAND-AVERAGE STATISTIC?

The landed sentence: *"the located transition belongs to the contrast between the arms and not to
their sources …"*. The order asks whether it can be misread as the band-average statistic it dates
to `l.1411`.

**⚠⚠ THE TARGET IS LOCATED BY ITS TEXT AND NOT BY THE ORDER'S LINE NUMBER** — this is the standing
instruction and `l.1411` is a number in a file that has been edited since. **Both objects are
found by their own text**, and then the arm is: **do the two name the same object?** A sentence
about what a located transition BELONGS TO is a claim about attribution; a band-average statistic
is a NUMBER with a definition. Registered: the misreading is available only if the sentence's own
words — "the contrast between the arms" — are also the words that define the statistic, so the
probe reads the statistic's definition and compares the NOUN PHRASES, not the topic.
⌗ And **NO, IT CANNOT BE MISREAD** must stay reachable: the order asks "whether", which invites
yes.

## ITEM ④ — THE REST OF THE LANDING

- **4a The formal paragraph's last sentence** now reads *"That this extension is maximal, and the
  `r < 0` patches as a geometry in their own right, are not formalised."* **Its first clause was
  REPLACED** — it used to bound the four-patch identity, which `cp_kruskal` now covers. ⚠ So the
  arm is whether the NEW bound is right: **a set identity with `{UV < 1}` is not the same claim as
  identity with the MAXIMAL extension**, and if the prose elsewhere claims the latter while the
  machine checks the former, the sentence must be the thing that keeps them apart. Read it against
  what the paragraph above it now claims.
- **4b** `cp_kruskal` and `cp_metrics` exist as declarations, spelled as printed, with their
  binders listed; and the names P2 prints are matched by **SKELETON** and not by literal
  character, the fix `r7712` was forced into.
- **4c** `axiom` and `sorry` counts for `CirclePatches.lean`.

## ⌗ THE ORDER'S CORRECTION TO `r7712`, AND THE NEGATIVE PROBE IT BUYS

The order says the `3.23 per cent` **is** computed, as `_F9`, and printed `(3.23%)` on a gate
line — and that this seat's digit search missed it *because the digits appear only in the run
output, not in the source*. **That is accepted as a correction and it is also verified rather than
taken:** the arm is to find `_F9` and its gate line at source. `r7712` said NOT FOUND **over a
named search**, which was true of those searches and is why the gap was visible; the searches were
nonetheless of the wrong KIND.

**NEGATIVE PROBE (22), registered here:** *a named search over SOURCE cannot find a value that
exists only at RUN TIME. A computed quantity has no digits in the file that computes it, so
"searched by the digits" is a search for a LITERAL and bounds only the literals.* ⌗ Which is the
seventh family's own shape one turn on — **an instrument reads the FORM it was given** — and this
time the form was not a name but a NUMERAL.

## GUARDS AND SELF-TESTS

G1 one predicate per conjunct. G2 three anchor forms only — unanchored markers REFUSED.
G3 the flip family, striking EVERY copy. G4 classifier probes tested on BOTH classes.
G5 reader probes with negatives. G6 every prose probe on a FLATTENED copy.

**The twenty-two negative probes stand. The ones this revision is most exposed to:** (15) and
(17) — the order reports repairs landed, so "supported" is the expected answer and the instrument
must be able to say otherwise, and it must equally be able to say SUPPORTED where the order's own
framing invites a defect; (19) a NAME is a form, so the citation test matches skeletons;
(20) a REPLACED sentence may have changed its subject — which bites at 2a and 4a both;
(21) a "therefore" is load-bearing; and (22) above.

**WHAT THIS REVISION CANNOT DO:** it cannot certify any Lean file as a proof, and it cannot settle
a geometric fact the files do not state. Where a question turns on something outside the files,
that is NAMED as outside and not supplied.
