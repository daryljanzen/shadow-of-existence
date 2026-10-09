# r7221+70.1 — results: the 270 source-half keys, each with a verdict and a repair class

*Pre-registered at `PREDICTION.md` (`1d0ace8f`).  One row per key in `source_half_by_remedy.tsv`, giving its
status, D, class, single or multi-site, and edit sites.  Logs: `census_log.txt`, `seeds_log.txt`, and
`cap_attribution_log.txt` (post-hoc, labelled).*

- **Population check.**  `S8` was run unmodified through its section D, and all of its gates passed.  My per-key
  re-walk matches its tallies on all eight buckets: 148 `REVERSAL` and 122 `PARTIAL`, which makes 270.

## The split holds, and here it is

| class | keys | single-site | multi-site | full `REVERSAL` | `PARTIAL` |
|---|---|---|---|---|---|
| `EXTEND-SHORT` (D ≤ 25) | **72** (26.7%) | 54 | 18 | 41 | 31 |
| `EXTEND-LONG` (26–100) | **96** (35.6%) | 42 | 54 | 43 | 53 |
| `CLAUSE` (> 100, 60 of them beyond 300) | **102** (37.8%) | 24 | 78 | 64 | 38 |

- **227 of the 270 (84%) have exactly one assertion to edit.**  32 have several, and 11 have none in the
  `'…' in` form.
- **150 of the 270 are multi-site**, against 147 of 442 in the paper half.  The source half's literals repeat
  across files far more often.  Most of them land in `CLAUSE`: 78 of its 102 keys are multi-site.
- **The `>300` bucket, attributed post-hoc** (`cap_attribution.py`; no class changes).  34 of the 60 need more
  than 300 characters even when the extension may run into code.  The other 26 are `>300` only because the
  extension must stay inside its prose span; 14 of them would need ≤ 100 characters if it could cross into
  code.  An extension into code is not a prose pin, so the classes stand.  The 14 are the most likely to have a
  cheap repair of a different kind.

## Predictions against measurement

| | predicted | measured | |
|---|---|---|---|
| P1 `EXTEND-SHORT` share | 20–35% | **26.7%** | hit |
| P2 `CLAUSE` share | 20–40% | **37.8%** | hit |
| P3 single-site median D | 25–45 | **25.5** | hit, at the edge |
| P4 `PARTIAL` cheaper than `REVERSAL` by ≥ 10 | ≥ 10 | **46.0 against 46.5** | **miss** |
| P5 one edit site for ≥ 75% | ≥ 75% | **84.1%** | hit |
| P6 each arm ≥ 10%, so the split exists | yes | 27 / 36 / 38% | hit |
| seeds | 4 / 4 | 4 / 4 | |

- **P4 misses cleanly.**  A key that some reversals already break costs no less to repair than one that none
  do.  The median distance is set by the farthest reversal, not by how many reversals already land.
- **P3 hit at its lower edge**, so it is not strong evidence for the shorter-clause story.  P1 and P2 hit with
  more room.  The source half is cheaper per key than the paper half (single-site median 25.5 against 54).  But
  it is multi-site far more often, and multi-site keys cost more (median 72.5).
- **Five of six predictions hit here**, against none of four on the paper half.  The predictions were made for
  this population; they were not carried over.

## What this does not do

- No receipt, no baseline row and no baseline verdict field is edited.  The verdicts are the rows in the `.tsv`.
- It inherits `S8`'s limits.  A gate label counts as code, so a key whose only prose is a gate label is outside
  the 270.  It also uses `r7228`'s closed transform tables.
