# F07 — 191 of 249 receipts have no assertion, so "run everything and check the return codes" is a smoke test for three-quarters of the layer — including 76 of the 100 rows marked ✔✔

*status: BOUNDED NEGATIVE, structural (measured, this cut). Also a correction to my own F01 headline.*
*artefact: `DRAFT_receipt_fingerprints.py` + `receipt_fingerprints.json` (blessed, 249 receipts / 23 390 printed numbers).*

---

## The measurement

| | count |
|---|---|
| receipts under `receipts/` | **249** |
| containing at least one `assert` | **58** |
| containing none — exit code 0 unconditionally | **191** |
| of those 191, printing no verdict token at all (`True/False/OK/PASS/CONFIRMED/…`) | **52** |
| `INDEX.md` rows marked **✔✔** whose receipt is print-only | **76 of 100** |
| `INDEX.md` rows marked **OK** whose receipt is print-only | **97 of 127** |

## What follows, and what does not

**What does not follow: that anything is wrong with those receipts.** ✔✔ is a *reader's* verdict on
printed output, and the corpus's practice is plainly to read them — the print-only receipts are
some of the best documents in the tree. `K9_isotropy_obstruction` kills its own author's proposed
argument and gets a better result from the wreckage. `O2_sightline_null_on_lift` prints a table
whose every row says `False`, explains in the next paragraph that the planar section cannot be
null by construction, re-tests on the substrate and gets `NULL: True`. `alpha_alone` has a section
headed *"WHERE I WAS WRONG, precisely."*

I swept every receipt's output for failure language — `FAIL`, `MISMATCH`, `WRONG`, `does not
match`, `disagree` — expecting to find a broken check hiding in a print-only receipt. **135 lines
across ~60 receipts, and essentially every one is the corpus recording its own prior error on
purpose.** That is the opposite of the defect I went looking for, and it is the reason the
print-only convention has worked.

**What does follow: a reader's verdict is pinned to the revision it was given at.** After that, a
print-only receipt that starts computing something different keeps returning 0, keeps printing a
well-formatted table, and nothing notices. The channel is:

> a shared module changes · a library version bumps · an origin is edited and its copy is not ·
> a constant is retuned upstream → **the numbers move and every gate stays green.**

That is not hypothetical. **F06 is exactly this shape**: a paper and a receipt sitting at different
libraries with all ten gates green, found only by running the receipts and comparing their output
to the prose by hand.

## And it corrects my own F01

F01's headline was *"**248 of 249 receipts return 0** — nothing in the reproducibility layer is
computationally broken at this cut."* That sentence is true and it is weaker than it sounds, and I
should have said so when I wrote it. For 191 of those 249, returning 0 is not evidence: it is what
they do. The honest version is:

> **58 receipts self-check and pass. 191 ran to completion and printed output that no machine
> examined.** One (`ROBUST_p1p2_scan.py`) could not run in place at all.

I record the correction here rather than editing F01, because how a census overstates itself is
worth keeping.

## The fix, and it needs no per-receipt work

A receipt's printed **numbers** are its content. Store them at the revision a reader signs off;
fail when they move. `DRAFT_receipt_fingerprints.py`:

```
python3 DRAFT_receipt_fingerprints.py --bless    # baseline
python3 DRAFT_receipt_fingerprints.py           # compare, nonzero on drift
```

Run against the live tree:

```
blessed 249 receipts, 23390 printed numbers, 10 significant figures
RECEIPT FINGERPRINTS: 249 receipts compared against the baseline
No receipt's printed numbers have moved.
```

Perturb one digit of one receipt's D/H and it bites:

```
[FAIL] P16_cosmogenesis_paper/P16_validate_bbn.py printed different numbers
```

**Determinism checked, because the gate is worthless if receipts wobble on their own.** Re-ran a
random 40-receipt sample live against the baseline: **0 fingerprints moved**. No receipt in the
sample prints a timing, an address or an unseeded random draw. The comparison is at 10 significant
figures — loose enough to absorb BLAS last-bit differences across machines, tight enough that any
real change shows. It reads only the numbers, so prose edits, comment rewrites and table-width
changes do not trip it.

**What it deliberately does not do**, and this belongs in the docstring so it is never trusted for
the wrong job: it judges whether a number *changed*, not whether it is *right*. A receipt whose
numbers were wrong when blessed stays wrong and silent. This closes the **regression** channel,
not the **correctness** one. And it does not replace reading — it makes a reader's verdict
**durable**, which is precisely what the ✔✔ mark currently asserts and cannot enforce.

## A smaller companion suggestion

`INDEX.md`'s status legend distinguishes ✔✔ / ◐ / ✗ / ? / ∅ — how *well* a claim is receipted. It
does not distinguish *who can re-check it*. A one-character marker (or a column) separating
`self-checking` from `read-and-judged, blessed at rN` would make the layer's own census honest at a
glance, and would tell a future reader which 191 rows the fingerprint baseline is standing in for.

## Not claimed

- No claim that any print-only receipt is wrong. I looked for one and did not find one; what I
  found was a tree that documents its own mistakes unusually well.
- No claim that assertions are the right style for these receipts. Many are symbolic derivations
  whose value is the argument, and burying that in `assert` would cost more than it buys — which
  is exactly why the fingerprint approach is external to them.
- No closure on any registered item.
