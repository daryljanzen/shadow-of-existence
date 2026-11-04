# `r7667` (cc66) — PO-87's LIST IS 49 ITEMS, AND ITEM 2 HAS **NO** CHEAP HALF: NOTHING IS RE-DERIVABLE BY REPOINTING

**Receipt:** `census.py` in this directory — 12 checks, 0 failures, ~1 s.
**The list:** `LIST.md`, the census's own output: 49 items with sentence, receipt and spectra.
**Registered:** `PREDICTION.md`, its own commit (`r7667+cc66.0`), pushed before `census.py` existed.
**Tree:** `5dac5ff9a` (`origin/main` at `r7667`).

## THE RESULT IN ONE LINE

**49 figure-printing items** rest on a namesake spectrum or a superseded instrument state — and
**not one of them can be re-derived by repointing to a spectrum the tree already holds.** Of the 49,
**25 demonstrably load a namesake** and **24 are on the list only because none of their load sites
can be decided from the source**, which makes them candidates for a *read* rather than for a
rebuild.

## ⛔ WHAT ITEM 2 ACTUALLY FACES

The order says *"re-derive the cheapest half of them"*. Measured:

| | items |
|---|---|
| re-derivable by repointing alone | **0** |
| need a spectrum built first, or carry an undecidable load site | **49** |
| of the 49: demonstrably load a namesake (a rebuild question) | **25** |
| of the 49: every load site undecidable from source (a reading question) | **24** |
| distinct namesake spectrum **paths** with no arm-of-record counterpart | **32** |

⇒ **There is no cheapest half to re-derive.** The cheapest work on this list is not a rebuild at all:
it is **reading the 24** whose load sites are built from variables, because some of them may already
be on the arm of record — exactly the error this census made twice about itself. Only after that does
a build budget have a well-defined target, and `r7640+60` establishes that twelve configurations
cannot be rebuilt under their own recorded `KFAC=1` in any case. **That sequencing is 69's call and
is not taken here.**

## THE REGISTERED ARMS, SCORED — THREE OF FOUR MISSED

**① MISSED by six.** Registered **55–73** of the body-cited candidates printing a figure; scored
**49**. *Not rounded into the band: the band was mine to pick.*

**② FALSIFIED AS STATED.** Registered: every `_leafrec1` spectrum has a plain sibling. Six do not —
five are `*_distances.npz`, a different *product*, and one is a configuration only ever run on the
leaf rate. **An unpaired `_leafrec1` file is one born on the arm-of-record side**, not a namesake
that lost its rebuild. The same arm's `≥30` clause **hit, at 32 paths.**

**③ FALSIFIED BADLY.** Registered: at least **eight** of `r7640+60`'s twelve un-rebuildable
namesakes are read by a receipt the paper cites. **One is** — `c54.178`. ⇒ **Eleven of the twelve are
not a live dependency of any paper sentence**, so the order's *"include the twelve"* is a
completeness instruction and nothing more.

**④ HIT.** `EXPLAINER.md` cites none of the candidates through a `\rcpt`.

## ⛔⛭⛭⛭ THE INSTRUMENT WAS WRONG TWICE, AND BOTH ARE SHOWN WRONG RATHER THAN WITHDRAWN

**Cut 1 classified by FILENAME.** Outside `computations/beyond_the_wall/spectra/` (251 of the tree's
441 `.npz`) the LEAFREC distinction is carried by the **directory**:

```
refit_grid/cr_base.npz            <- namesake
refit_grid_leafrec1/cr_base.npz   <- arm of record          SAME BASENAME
```

All 20 `cr_base.npz` tokens were counted namesakes whatever directory they are read from. **44
tokens resolve both ways**, so no filename test could have separated them — `Ⓐ④`'s first half.

**Cut 2 counted every `.npz` TOKEN in the source, and a token is not a read.** The clearest case:
`P15_the_visibility_width_is_not_the_carrier…` declares
`NEED = ('r6919_injected_lcdm.npz', 'r6919_injected_cr.npz', 'r6919_geometry.npz')` as a **presence
manifest**, while its figures come from `np.load(f'r6919_injected_{t}_leafrec1.npz')` — which the
regex saw only as the fragment `_leafrec1.npz`. ⇒ **Cut 2 put an item on PO-87's list that is
already entirely on the arm of record, and called it the one cheap repointing.** Measured across the
scope: **14 receipts carry a namesake token while loading the arm of record**, and `Ⓐ④`'s second half
asserts it.

**Cut 3 reads LOAD SITES out of the AST**, keeping the three-way discipline: `aor` **22**, `namesake`
**116**, `undecidable` **210** of 348 sites. The undecidable majority is why the list separates
evidence from conservative inclusion rather than presenting 49 equal items.

**What moved across the three cuts** — monotonically toward the same conclusion:

| | cut 1 (filename) | cut 2 (paths) | cut 3 (load sites) |
|---|---|---|---|
| candidates | 102 | 100 | **96** |
| body-cited | 73 | 72 | **69** |
| figure-printing items | 54 | 53 | **49** |
| re-derivable by repointing | 2 | 1 | **0** |
| of the twelve, live | 3 | 3 | **1** |

⌗ **Four corrections in two revisions now share one shape.** `r7665+cc66.1`: I searched for strings
the paper could not contain. `cc66.1`: I counted `{base}`, which matches the appendix's
`\rcptlabel`. `cc66.2`: I keyed on a filename where the tree keys on a path. `cc66.3`: I keyed on a
token where the question is what the code *loads*. ⇒ **Each time the instrument was cheaper than the
question, and each time the error was found by pulling on a number of my own output that did not sit
right** — an "arm-of-record" entry whose filename was a bare fragment, in this last case.

## WHAT THIS DOES NOT SETTLE

Nothing here re-derives anything, and **no figure in the list is asserted to be wrong.** `LEAFREC=0`
is not itself a defect: a sentence may legitimately be about the namesake configuration, and the
order allows an item to leave the list by having its **sentence re-grounded** rather than its figure
recomputed. ⚠ And **24 of the 49 are on the list conservatively** — their load sites are built from
variables, so this census cannot say what they read. Treating those as rebuild work without reading
them first would repeat, at 69's cost, the mistake cut 2 made at mine.
