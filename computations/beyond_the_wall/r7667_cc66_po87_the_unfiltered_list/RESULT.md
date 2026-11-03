# `r7667` (cc66) — PO-87's LIST IS 53 ITEMS, AND ITEM 2's PREMISE DOES NOT HOLD: THE CHEAP SET IS **ONE**, NOT HALF

**Receipt:** `census.py` in this directory — 11 checks, 0 failures, 1 s.
**The list:** `LIST.md` in this directory, the census's own output, 53 items with sentence, receipt and spectra.
**Registered:** `PREDICTION.md`, its own commit (`r7667+cc66.0`), pushed before `census.py` existed.
**Tree:** `5dac5ff9a` (`origin/main` at `r7667`).

## THE RESULT IN ONE LINE

**53 figure-printing items** rest on a namesake spectrum or a superseded instrument state, each
listed with its sentence, its receipt and the spectra it reads — and **exactly one of the 53 can be
re-derived by repointing to a spectrum the tree already holds.** The other 52 need a spectrum
**built** first, or carry a token this census refuses to guess at.

## ⛔ THE FINDING ITEM 2 TURNS ON

The order says *"then re-derive the cheapest half of them"*. That presumes a cheap half. **There
isn't one.** Measured, with the `_leafrec1` siblings counted against the bank:

| | items |
|---|---|
| re-derivable by repointing alone (every namesake path it reads has an arm-of-record counterpart) | **1** |
| need a spectrum built first, or carry an undecidable token | **52** |
| distinct namesake spectrum **paths** with no arm-of-record counterpart | **55** |

⇒ *"The cheapest half" is not 27 repointings; it is **one** repointing and 52 builds.* Which 27 are
cheapest is therefore a question about **build cost on today's instrument**, not about what the bank
already holds — and `r7640+60` establishes that twelve namesake configurations cannot be rebuilt at
all under their own recorded `KFAC=1`. **That is 69's call and I have not made it**: the list is
complete and ordered, and item 2's scope needs a ruling before a build budget is spent.

## THE REGISTERED ARMS, SCORED — THREE OF FOUR MISSED

**① MISSED, by two.** Registered: between **55 and 73** of the body-cited candidates print a figure
in the citing sentence. Scored: **53**. *Reported as a miss rather than rounded into the band — the
band was mine to choose and 53 is outside it: 72 body-cited candidates, 53 of which print a figure.*

**② FALSIFIED AS STATED, and its failure mode is the useful part.** Registered: every `_leafrec1`
spectrum has a plain sibling, so the naming is a total pairing. **Six do not.** They are not
mis-named: **five are `*_distances.npz`**, a different *product* from a spectrum, and the sixth is
`cc66_cr_fluid_leafrec1.npz`, a configuration only ever run on the leaf rate. ⇒ **A `_leafrec1` file
with no sibling is one born on the arm-of-record side, never a namesake that lost its rebuild.** And
the direction this census actually *uses* — *no suffix ⇒ namesake* — is untouched by the exception
class, so the classifier is sound where it is load-bearing. Also registered at **≥30** namesake
spectra with no sibling: **HIT at 52.**

**③ FALSIFIED, and in the direction that matters.** Registered: at least **eight** of `r7640+60`'s
twelve un-rebuildable namesakes are read by a receipt the paper cites, so the twelve are a live
dependency. **Three are** — `c54.175`, `c54.177`, `c54.178`. ⇒ **Nine of the twelve are read only by
receipts no body sentence cites**, so they are far cheaper to leave un-rebuilt than I registered, and
the order's *"include the twelve"* is a completeness instruction rather than a nine-item backlog.

**④ HIT.** `EXPLAINER.md` cites **zero** of the candidates through a `\rcpt`.

## ⛔ A CORRECTION TO MY OWN REGISTRATION

`PREDICTION.md` warns that a citation in a generated `appendix_receipts_*.tex` is not a figure in
print, and reports a **90-vs-73** gap as the reason to key the list on the body. **The caution is
right in principle and the gap was my own measurement error.** The generated appendices do not cite
at all — they *define* the anchor with `\rcptlabel{base}{P15R143}`, a different macro — and my
orientation pass counted a loose `{base}`, which matches those labels. Measured properly:
`\rcpt{` appears **328** times in `CR_cosmology.tex`, **0** times in the generated appendices, and
`\rcptlabel{` **1620** times there. ⇒ **The "cited only by a generated appendix" class is empty by
construction, not by accident**, and `Ⓑ①` now asserts the macro distinction rather than the count it
produces. *Same shape as `r7665+cc66.1`: a count over a corpus is only evidence if the pattern is one
the corpus would use.*

## THE LIST'S EDGE, STATED RATHER THAN LEFT IMPLICIT

The 102 candidates split **73 body-cited / 29 cited by no body sentence**. The 29 rest on namesake
spectra and are **off** PO-87's list by the order's own terms — it asks for figures the papers
*print* — but they are the population a later order would reach for, so the number is on the record.
Of the 73, **54** print a figure and **19** cite the receipt without printing any of its numbers.

## ⛔⛭⛭⛭ A SECOND CORRECTION, TO THE FIRST CUT OF THIS CENSUS — IT CLASSIFIED ON THE FILENAME AND WAS WRONG FOR A WHOLE CLASS

The first cut of `census.py`, committed and pushed at `r7667+cc66.1`, decided "namesake or arm of
record" **from the filename**: no `_leafrec1` in the name ⇒ namesake. **That is wrong for 190 of the
tree's 441 `.npz` files**, because outside `computations/beyond_the_wall/spectra/` the LEAFREC
distinction is carried by the **directory**:

```
computations/beyond_the_wall/refit_grid/cr_base.npz            <- namesake
computations/beyond_the_wall/refit_grid_leafrec1/cr_base.npz   <- arm of record     SAME BASENAME
```

So every `cr_base.npz` token — 20 of them — was counted a namesake whatever directory its receipt
reads it from, and the cheap/expensive split inherited the error.

**The fix is to resolve each token against the whole tree and classify three ways**, with the
undecidable bucket named rather than guessed, the way `S56`'s own three-way test does:

| resolution | meaning | tokens |
|---|---|---|
| every match under a `leafrec1` path | arm of record | **73** |
| no match under one | namesake | **322** |
| **both** | **UNDECIDABLE from the token** — the receipt's own directory logic decides, and this census does not guess | **44** |
| no match at all | unresolved: a fragment of a built filename (`_leafrec1.npz`, `_base.npz`) or a file not in the tree | **35** |

⇒ **44 tokens could not have been classified by any filename test**, which is `Ⓐ④`'s content: the
replaced method is shown to be wrong rather than quietly withdrawn. And the counterpart test is now
path-aware too — a namesake at `D/X.npz` counts as already rebuilt if either `D_leafrec1/X.npz` or
`D/X_leafrec1.npz` exists.

**What moved:** candidates 102 → **100**; body-cited 73 → **72**; figure-printing 54 → **53**;
cheap 2 → **1**; unbanked 52 → **55** paths. *The headline is unchanged and slightly sharper: there
is no cheap half.* ⌗ Three corrections in two revisions now share one shape — `r7665+cc66.1`'s
search strings, this revision's `\rcptlabel` miscount, and this one: **a test over the tree is only
as good as the thing it keys on, and a filename is not a path.**

## WHAT THIS DOES NOT SETTLE

Nothing here re-derives anything, and **no figure in the list is asserted to be wrong.** `LEAFREC=0`
is not by itself a defect: a sentence may be legitimately about the namesake configuration, and the
order allows an item to leave the list by having its sentence **re-grounded** rather than its figure
recomputed. The census records what rests on what.
