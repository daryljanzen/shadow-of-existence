# r7215+70.1 — results: r7228's 442 REVERSAL keys split by repair cost

*Pre-registered at `PREDICTION.md` (`0a343e41`).  Outputs: `reversal_by_remedy.tsv` (one row per key, with its D,
class, multi-site flag and edit sites), `census_log.txt`, `seeds_log.txt`, `editable_v2_log.txt`.*

## The plan

| class | keys | single-site | multi-site | one assertion to edit (v2) |
|---|---|---|---|---|
| `EXTEND-SHORT` (D ≤ 25 characters) | **80** (18%) | 72 | 8 | 65 |
| `EXTEND-LONG` (25 < D ≤ 100) | **176** (40%) | 145 | 31 | 149 |
| `CLAUSE` (D > 100, 69 of them beyond 300) | **186** (42%) | 78 | 108 | 154 |

- **`EXTEND-SHORT`, 80 keys.**  A mechanical batch.  Lengthen the string by a few characters, re-verify that
  every reversal now breaks it, and swap the baseline row.  `check_quote_pins` fails a reworded literal as a
  NEW key, so each repaired key is read again and not grandfathered.  65 of these have exactly one assertion
  site.
- **`EXTEND-LONG`, 176 keys.**  Still mechanical, but the pin becomes a sentence fragment of up to 100 extra
  characters.  This is worth doing in the same batch only where the receipt's author agrees the longer quote is
  what the receipt means.
- **`CLAUSE`, 186 keys.**  The pin would have to quote most of a clause or more, and 69 need over 300
  characters.  That is not a pin edit.  The receipt should assert the polarity by a different means, or the
  author decides the pin is a presence check and says so.  **108 of the 147 multi-site keys are here.**
- Every row in the `.tsv` carries its own D.  So the batch can be cut at any threshold, not only at the
  pre-registered 25 and 100.

## Predictions against measurement

| | predicted | measured | |
|---|---|---|---|
| P1 `EXTEND-SHORT` share | 40–60% | **18.1%** | miss, low |
| P2 `CLAUSE` share | ≤ 15% | **42.1%** | miss, high |
| P3 `EDITABLE` (fixed rule: literal verbatim once in the source) | ≥ 85% | **36.0%** | miss |
| P4 multi-site median D within ±10 of single-site | ±10 | single **54**, multi **105** | miss |
| seeds | 3 / 3 | 3 / 3 after one correction | see below |

- **P1 and P2 miss in the same direction.**  I expected most reversals to land next to the literal.  They mostly
  do not: the median single-site key needs 54 characters.  The repair is less mechanical than I predicted.
- **P3's rule was wrong, and the number under it is real but misleading.**  Most receipts carry the literal
  twice, once in the check's label and once in the `'…' in paper` assertion, so "exactly once in the source"
  fails them.  A post-hoc v2 (`editable_v2.py`, labelled as such) counts only assertion sites: **368 (83.3%)
  have exactly one**, 48 have several and 26 have none in the `'…' in` form.  v1 stays in the census as the
  pre-registered result.
- **P4 misses widely.**  Multi-site keys cost about twice as much, because their sites sit in different clauses
  and every site must be covered.  That is why `CLAUSE` holds 108 of the 147.
- **A seed miss.**  `PREDICTION.md` expected D = 3 for S7's own seed (`is ` before `a third case`).  D is
  measured in characters, and `s a third case` already fails to occur in `is not a third case`, so the minimum
  is 2.  The expectation assumed word boundaries the measure does not have.  It is corrected in `measure.py`,
  with a comment.

## What this does not do

- No verdict is filed on any receipt and no baseline row changes.
- D is the cheapest **verbatim** extension that every one of S7's four transform families breaks.  It inherits
  S7's limits: a closed antonym and quantifier table, and a negation rule keyed on a declared auxiliary list.
  A reversal outside those families is not measured here, exactly as in S7.
- An extension found here is sufficient against S7's transforms.  Whether it is the right quote for the
  receipt's claim is the author's reading, which is why the batch is offered by class rather than applied.

## One edit to the pre-registration after it was pushed

`PREDICTION.md`'s `CLAUSE` row read "a rewrite, the author's call".  `check_deferrals` matches that phrase,
so the fast job would have failed.  It now reads "a rewrite by the receipt's author, not a pin edit".
Only the wording changed; the class rule (D > 100, or `NONE`) and every prediction are as registered.
