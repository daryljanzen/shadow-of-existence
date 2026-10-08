# r7215+70.1 — `r7228`'s 442 REVERSAL keys split by what a repair costs. Pre-registered before measuring

*Not ordered. 66 offered it at `r7215`: "the count split by what a repair would cost … A list of 442 with no
repair classes is a number; split by remedy it is a plan." This file fixes the measure, the classes and the
predictions before any distance is computed.*

## Already seen, so not predicted

- `load442.py` runs `S7`'s own source unmodified, up to its first section header.  It reproduces S7's counts
  exactly: 442 REVERSAL, of which 147 are multi-site.  No distances have been computed.

## The measure, fixed now

A REVERSAL key survives every reversal of its clause because each transform changes text *outside* the
literal.  The cheapest repair keeps the pin verbatim and extends the literal along its own clause until it
covers the changed text.

- For each site of the key, and each transform S7 applies there, find the character positions where the
  reversed clause differs from the original.  For an insertion, that is the insertion point.
- **D(site)** is the smallest number of characters added to the literal, as one contiguous extension left
  and/or right inside the clause, such that the extended string is absent from **every** reversed clause.
  D is found by direct search over (left, right) extensions in order of total length, and confirmed by
  re-running S7's `reversals()` on the extended string.  It is a measurement, not an estimate.
- **D(key)** is the maximum over the key's sites.  `NONE` means no extension inside the clause works at
  some site.

## The classes, fixed now

| class | rule | what the repair is |
|---|---|---|
| `EXTEND-SHORT` | D ≤ 25 | lengthen the string by a word or three — mechanical |
| `EXTEND-LONG` | 25 < D ≤ 100 | lengthen by a phrase — mechanical, but the pin becomes a sentence fragment |
| `CLAUSE` | D > 100, or `NONE` | the pin must quote most of a clause or more; a rewrite, the author's call |

Each class is split again by `MULTI` (multi-site: S7's `multi` set), because a multi-site key also needs its
site disambiguated.  Then a second axis:

- **`EDITABLE`**: the literal occurs verbatim exactly once in the receipt's source on HEAD.  The repair is
  then a one-string edit.
- **`CONSTRUCTED`**: otherwise.  The literal is assembled, repeated or escaped differently, so the edit needs
  reading.

## Predictions

- P1: `EXTEND-SHORT` is 40–60% of the 442.  Most reversal sites are a negation inserted after a nearby
  auxiliary, or a quantifier next to the noun phrase.
- P2: `CLAUSE` (including `NONE`) is ≤ 15%.
- P3: `EDITABLE` is ≥ 85%.
- P4: multi-site keys are no shorter to repair than single-site ones.  Their median D is within ±10
  characters of the single-site median.

## Seeds, run before the census

- S7's own seed `the branch point is a third case for the crossing` with literal `a third case`: NEG+ gives
  `is not a third case`, so the minimal extension is the 3-character prefix `is ` and D = 3.
- A clause whose only transform is a numeral 40 characters away must give D = 40 ± the numeral's width.
- A literal that already discriminates must give D = 0.  It is not in the 442, but this tests the search.

No verdict is filed on any receipt and no baseline row changes.  This is a repair plan, routed to the
receipts' authors through 66.
