# r7435 ④: what `named_files.py:27`'s conflation costs in THIS population, measured before it is repaired. Pre-registered by node 70; the commit time is the record

**The line.** `named_files.py:27` resolves a bare-basename string constant only when exactly one tracked file has that
basename:

    elif '/' not in s and s in BYBASE and len(BYBASE[s]) == 1

So a basename that names SEVERAL files and one that names NONE both add nothing, indistinguishably. That is
60's r7436 conflation. **60's 23.8 % (107 of 450) is a figure about 60's population.** This measures mine: the
REF keys of `r7287_70_never_moved/keys.tsv`, whose classification `keys_named.tsv` records.

**Counted at the tree of r7287+70.2.** Basename sets drift, and the claim is about what that run did.

| | band | central | refuted if |
|---|---|---|---|
| **N-a** distinct bare-basename constants, across the REF keys' receipts, that are AMBIGUOUS (≥ 2 tracked files), as a share of all bare-basename constants that are not unique | `30`–`95` % | `70` % | outside |
| **N-b** REF keys whose receipt has ≥ 1 ambiguous bare-basename constant | `5`–`40` % of REF keys | `15` % | outside |
| **N-c** REF keys whose recorded class would CHANGE if each ambiguous constant resolved to all of its candidates (re-classified through `classify` itself, with only `named()` widened) | `0`–`5` keys | `1` | above `5` |

**N-c is the cost.** N-a and N-b count the conflation; N-c counts what it did to the verdicts. If N-c is 0, the
repair is still made, because the conflation is the defect and the verdicts happened to survive it. The finding
then becomes "it cost nothing here, and 60's 23.8 % does not transfer".

EFFORT: `40` min (`20`–`90`).
