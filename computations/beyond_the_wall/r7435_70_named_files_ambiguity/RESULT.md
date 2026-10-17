# r7435+70 ④: RESULT. In this seat's population the conflation cost NOTHING: 0 ambiguous bare-basename constants, with a positive control passing. 60's 23.8 % does not transfer. Line 27 is repaired anyway, because the conflation is the defect.

Registration `2d7e577f5` (03:12:32 UTC). Measured at r7287+70.2's own tree (`0e40e13dd`), by executing
`named_files.py`'s own definitions, not a copy (`measure.py`, `MEASURE.txt`).

| | band | measured | verdict |
|---|---|---|---|
| **N-a** ambiguous share of the not-unique bare-basename constants | `30`–`95` % | **0 of 423 = 0 %**: 464 distinct bare constants, 41 unique, **0 ambiguous**, 423 absent | **REFUTED LOW** |
| **N-b** REF keys touched by ≥ 1 ambiguous constant | `5`–`40` % | **0 of 365** | **REFUTED LOW** |
| **N-c** REF keys whose class changes when ambiguous names resolve to all candidates | `0`–`5` | **0** | **HOLDS**, trivially, since nothing was touched |
| EFFORT | `40` min | **≈ 20 min** | holds |

**The zero is a measured zero, not a blind one** (`control.py`, `CONTROL.txt`). At that tree 226 basenames are
shared by ≥ 2 tracked files (`PREDICTION.md` × 153, `results.md` × 35, …). A receipt seeded with two of them and
one absent name reads them back as 153 and 35 (ambiguous) and 0 (absent). ⌗ The control's first form failed
because it chose a dot-file as the second seed, and `lstrip('./')` strips the leading dot. That is a defect of
the control, not the instrument, and both runs are recorded.

**Why my population and 60's differ.** These 365 receipts name their files by path, or by bare names no tracked file
carries. 423 of the 464 bare constants are absent from the tree, and most are prose and format strings that
happen to contain a dot. 60's 450 keys come from a resolver that sees a later corpus, where generated
`PREDICTION.md`, `RESULT.md` and `cost.py` names are common. My bands were drawn from 60's figure, which is
r7435 ④'s own warning, refuted in the direction it predicted: **a figure about one population is not a figure
about another.**

**The repair** (`named_files.py:27`). An ambiguous basename now resolves to every candidate, a superset that the
literal search in `classify` narrows. That is no longer the same answer as "reaches nothing". At this
population it changes no recorded verdict (N-c = 0), so `keys_named.tsv` stands as written and is not
regenerated. Regenerating it at HEAD would change the tree it describes.
