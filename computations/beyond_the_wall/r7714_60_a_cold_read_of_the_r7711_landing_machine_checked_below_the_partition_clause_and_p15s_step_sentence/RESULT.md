# r7714 (60) — RESULT

**Order `r7711`.** Registered before measurement at `472127ed`, pushed before `probe.py`
existed. Readings in `runs/READINGS.txt` (exit `0`, all self-checks pass); tree in
`runs/TREE.txt`.

**THE TWO QUESTIONS, ANSWERED: ① "machine-checked below" IS honest — both halves of the clause it
modifies are machine-checked, and the registered trap ran the other way this time, since agreeing
with the order was the cheap answer. ② no — cc66's sentence cannot be misread as either band
statistic, and there are two of them near it.** The rest of the landing holds. **One half-repair
offered, no defect routed**, and the order's correction to `r7712` is verified rather than taken.

---

## ① "machine-checked below" IS HONEST, AND IT IS THE CLAUSE'S TWO HALVES THAT MAKE IT SO

The phrase modifies *"by a chart map that is one-to-one onto the corresponding region of the
Kruskal manifold"*, **not** the sentence that follows it — the parenthesis falls before
"therefore isometric", and the placement classifier was tested on an injected sentence of each
placement before it was used. So what must be below is **two** things:

> **ⓐ one-to-one.** `cc_Φ_inj` and `ce_Ψ_inj`, **both cited in P2** (matched by skeleton, the fix
> `r7712` was forced into).
> **ⓑ onto the corresponding region.** `cp_onto_BH` and `cp_onto_RE`: *every* `(U, V)` in the open
> quadrant with `UV < 1` is a **member of the patch set** — and the patch sets are **defined** as
> the chart maps' images (`cp_BH M = {y | ∃ η ∈ (0,π), ∃ t, y = cc_Φ M η t}`).

**And the two directions are both there, which is what makes ⓑ content rather than a tautology.**
Because the region is *defined* as the image, "onto" needs the image to be identified
independently — and it is, from both sides: `cp_*_quad` puts each image **inside** its own open
quadrant, `cp_onto_*` puts the whole quadrant-inside-the-domain **inside** the image. Together the
four images are exactly the four open quadrant pieces of `{UV < 1}`, and `cp_kruskal` adds that
they and the horizons tile it.

**⌗ So the word "therefore" that `r7712` found load-bearing now has both of its premises**: the
coefficient match (`cp_metrics`) and the bijection onto the region. The repair this seat routed is
landed, and it is landed as a statement and not as a form of words.

**⚠ AND THIS IS WHERE THE REGISTERED TRAP RAN THE OTHER WAY FROM LAST TIME.** The order's own
framing — *"`cp_kruskal`/`cp_metrics` give a pullback and a partition but no isometry declaration
as such"* — invites agreeing that the phrase is dishonest, and **agreeing was the cheap answer**.
The prediction named that and kept **(a) NO DEFECT** reachable, with the decisive reading
registered in advance: *does `cp_kruskal` quantify over the CHART IMAGES or over regions defined
by inequalities?* **It quantifies over the images**, which is why the partition carries ⓑ at all.

**⌗ ONE POINTER MISSING — OFFERED AS A HALF-REPAIR, NOT ROUTED AS A DEFECT.** P2's formal
paragraph cites `cp_kruskal` and `cp_metrics` and **prints neither `cp_onto_BH` nor
`cp_onto_RE`** — the two declarations that state ⓑ as a property of the *map*. A reader who
follows "machine-checked below" to the paragraph finds a set partition and a pullback and must
derive the onto half for themselves. **The claim is established; only its pointer is missing** —
the same shape as `r7710`'s `cc_Φ_inj` half-repair, which was taken.

## ② THE CARRIER, THE DISJOINTNESS CLAUSE, AND THE REFLECTION

- **2a The reflection clause is right, read from scratch** (negative probe 20 — the sentence was
  REPLACED, so `r7712`'s verification did not transfer). It now claims only that the reflection
  *"preserves `r` and every coefficient of the metric"*, and **no "carries it onto the second
  exterior" survives anywhere in P2.** ✔
- **2b ⚠ THE REGISTERED PREDICTION WAS NOT BORNE OUT, WHICH IS WHY IT WAS REGISTERED.** I recorded
  that if `sk_S`'s carrier carried an extra condition the way `seWS` carries `V > 0`, the second
  exterior would be outside it too and **the gap would not be closed**. It does not:
  `def sk_kM : Set P := {p | p.1 * p.2 < 1}` — `{UV < 1}` and nothing more, with
  `sk_MN = φ ⁻¹' sk_kM`. **Checked by arithmetic, not recollection:** second exterior `(1, −1)` has
  `UV = −1`, so it **is** in `sk_kM` and is **not** in `seWS`. **The gap `r7712` found is closed,
  and closed by moving manifolds rather than by wording.** ✔
- **2c ⛔ THE SHARPEST ARM, AND THE CLAUSE SURVIVES IT.** *"the four `r ≥ 0` patches, with the
  horizons `UV = 0` at which they meet, are exactly that domain and pairwise disjoint"* — and
  `cp_kruskal` is **`cp_BH ∪ cp_WH ∪ cp_RE ∪ cp_LE ∪ cp_Hor = sk_kM`** together with **all ten**
  `Disjoint` pairs among those five sets. **The horizons are their own fifth set, which is exactly
  what the appositive does**, and "pairwise disjoint" of five pieces is what the ten conjuncts say.
  ⌗ **The false reading is named rather than ignored:** if "with the horizons" *enlarged* each
  patch, the enlarged sets would SHARE the horizons and could not be pairwise disjoint. That is
  not the sentence's construction — it is the same construction `prop:four_regions` uses, which
  `r7712` read and confirmed. **No repair.** ✔
- **2d `cp_metrics` holds coefficient-wise for all four patches** — twelve `hRep` conclusions on
  `sk_S`, three components each including the vanishing cross term. And **"the second of each pair
  through the reflection" is the theorem's own statement, not the prose's composition**: the
  reflected patches are stated at the negated point with negated vectors, which is the
  reflection's own pushforward since its differential is `−id`. ✔

## ③ cc66's SENTENCE CANNOT BE MISREAD AS THE BAND-AVERAGE STATISTIC

**⚠⚠ And both objects were located BY THEIR TEXT, which mattered: `l.1411` is a line number in a
file edited since, and there are TWO band statistics beside the sentence**, not one — the
candidate step (*"its lowest band's departure from the trend its own upper bands set"*, on four
bases) and, in the sentence immediately before, the acceptance law's band fraction (*"the lowest
band runs the same fraction of the rest under the law"*). **The arm was run against both.**

- **Not one noun phrase crosses, in either direction.** The sentence's are "the contrast between
  the arms", "the ratio of this arm's spectrum to the control's", "the two arms' `η`-integrated
  sources", "that ratio's own scatter"; the statistics' are "its lowest band", "the trend its own
  upper bands set", "four bases", "the rest under the law". **A window-by-window ratio BETWEEN
  arms is a different reduction from a band's departure from a trend WITHIN one.**
- **The decisive reading is where "the same sliding windows" points:** its antecedent is in the
  preceding sentence — the law's transition "across the same windows" — which is **upstream**,
  while the candidate statistic is **downstream and in another paragraph**.
- **And the inverse risk, which is the one that could actually arise, is closed by the text
  itself:** the candidate paragraph says the share is *"against the excess's own extrapolated size
  and not against the larger step the arms have in common, the two denominators differing by about
  a factor of six"*. **The paragraph separates them in its own words.**

⌗ `NO` had to stay reachable here, because the order asks "whether", which invites yes.

## ④ THE REST OF THE LANDING HOLDS

- **The formal paragraph's last sentence** — *"That this extension is maximal, and the `r < 0`
  patches as a geometry in their own right, are not formalised."* **Its old first clause, which
  bounded the four-patch identity, is gone from it and from P2 entirely** — rightly, since
  `cp_kruskal` now covers that identity. ⌗ **And the distinction the sentence has to carry is the
  one it does carry:** what the machine checks is a **set identity with `{UV < 1}`**, and
  "the maximal extension" is a different claim. Nothing in the files states maximality, and the
  sentence is what keeps the two apart. ✔
- `cp_kruskal` and `cp_metrics` exist, are spelled as printed, and **both are cited in P2**. ✔
- **Zero `axiom` tokens, zero `sorry`** in `CirclePatches.lean`. ✔

## ⑤ THE ORDER'S CORRECTION TO `r7712` IS RIGHT, AND VERIFIED AT SOURCE RATHER THAN TAKEN

`_F9 = abs(_FCV['distances'][4] / _LFRO[4] - 1.0)` is **computed**, and its gate prints it as
`f"{100 * _F9:.2f}%"` beside gate text that says *"converging it moves `l = 4` by about 3 per
cent"*. **So it is a computed gate value, as the order says**, and the digits `3.23` are **nowhere
in the source** — they exist only in the run output.

**⌗ NEGATIVE PROBE (22), bought by this correction and confirmed by the file:** *a named search
over SOURCE cannot find a value that exists only at RUN TIME. A computed quantity has no digits in
the file that computes it, so "searched by the digits" is a search for a LITERAL and bounds only
the literals.* `r7712`'s `NOT FOUND` was true of the searches it named — which is why the gap was
visible at all — but **the searches were of the wrong KIND**, and saying "whether a gate computes
`3.23` is not established by these searches" was the right bound on a wrong instrument.

---

## THE REPAIRS ROUTED

**None.** ⌗ **One half-repair offered:** the formal paragraph could cite `cp_onto_BH` and
`cp_onto_RE` where it says the chart map is "one-to-one onto the corresponding region
(machine-checked below)". The onto half is established; only its pointer is missing.

## WHAT THIS PROBE CAUGHT IN ITSELF — THREE, AND TWO WOULD HAVE BEEN FALSE FINDINGS

1. **⛔ THE WORST, AND IT WOULD HAVE CONFIRMED THE ORDER'S OWN SUGGESTION.** The onto arm looked
   for the existential **as a symbol**. Both onto theorems state surjectivity as **set membership
   in the image** — `(U, V) ∈ cp_BH M` — with the existential living in the set's *definition*, so
   the symbol is absent from the statement and **the arm reported the onto half missing**, which
   is precisely the finding the order's framing invited. Fixed by reading the **SHAPE** of the
   conclusion — membership of a patch set, with quadrant signs and the domain hypothesis among the
   binders — with negatives both ways (a pullback conclusion is not onto; a membership conclusion
   without the domain hypothesis is not onto).
2. **The declaration reader stopped at `:=`**, which is right for listing binders and wrong for a
   `def`, whose whole content lives *after* it. So `sk_kM`'s body was invisible and the arm
   reported FAIL on *"`sk_kM` is `{UV < 1}` with no further condition"* — **which read the wrong
   way is the claim that the carrier is narrower and the gap not closed**, the sharpest false
   finding available on this order. Fixed with a second reader that bounds a declaration by where
   the **next** one begins (the `r7708` lesson), used for content and never for binders.
3. **A "verbatim" marker that was not verbatim:** the partition clause was given as ending
   `(\texttt{cp\_kruskal})` where the source prints `(\texttt{cp\_kruskal}, in
   \texttt{CirclePatches.lean})`.

**EIGHTH AND NINTH INSTANCES IN EIGHT REVISIONS OF ONE FAMILY: an instrument reads the FORM it was
given, not the QUANTITY.** Last revision the form was a NAME in math mode; here it is a LOGICAL
FORM — an existential written as set membership — and, in ⑤, a NUMERAL that exists only at run
time. ⌗ `r7712`'s lesson held exactly: **a rule written down is not a check.** What caught all
three was that **each arm was written as an assertion that can FAIL rather than as a search that
can quietly return nothing** — three arms went red, and the red was in the instrument every time.
