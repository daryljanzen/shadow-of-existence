# `r7257+70.1` — results: the board is generated, not committed; R\* leaves 61 keys undecided, so it replaces the rule

*Pre-registered at `PREDICTION.md` (`9be17a66`). The scripts are `race.py` (B1–B3) and `measure_rule.py` (T1–T4). Their
outputs are `race.txt`, `measure_rule.txt` and `disagreements.tsv`. `measure_rule.txt` was taken on the operator
BEFORE R\* went in, so its "current" rows are the old rule; re-running it now prints R\* in both columns.*

## ① The board

| # | quantity | predicted | measured |
|---|---|---|---|
| B1 | a seeded merge race fails the OLD gate | yes | **only on one side**: branch A's copy (the earlier progress) is stale after the merge, branch B's is not |
| B2 | the same race passes the NEW gate | yes | **yes, by construction**: there is no committed copy to compare |
| B3 | a void double claim still fails | yes | **yes** |

**B1 is weaker than I stated it.** The merged expiry equals the later branch's, so a merge that keeps the later
branch's board is current. The race reddens the old gate only when the merge keeps the earlier side's file. The
mechanism that actually reddened `main` is the plainer one: a seat adjudicates and does not regenerate (`cc66.182`,
210 adjudications). Retiring the committed copy removes both mechanisms, because there is nothing left to forget.

**What changed.**

- `corpus/pin_adjudication_board.tsv` is untracked and git-ignored.
- `check_pin_board` totals the board it generates itself, every run. It keeps (a) void claims, (c) expiry and (d)
  seeds. (b) is now the generated total against the baseline.
- `scripts/gen_pin_board.py` still writes the file for a seat to read. `--check` now says the gate generates it, and
  exits 0, so no CI line needs changing.
- The claims ledger stays hand-kept and committed.

## ② The `target` rule

| # | quantity | predicted | measured |
|---|---|---|---|
| T1 | live keys R\* leaves UNDECIDED | 300 (100–700) | **61**: refuted low, outside the band |
| T2 | decided, R\* `PAPER`, baseline `SOURCE` | 15 (0–60) | **2** |
| T3 | decided, R\* `SOURCE`, baseline `PAPER` | 15 (0–60) | **3** (plus one baseline `RECEIPT`, a value outside the column) |
| T4 | current rule against the baseline | 20 (15–40) | **24**: 20 `PAPER`→`SOURCE` (r7255's `ACOUSTIC` flips), 3 the other way, 1 `RECEIPT` |

⛔→✔ **The reachable negative does not fire.** 61 is 2.2% of 2,775, against the 10% (278) set in advance. R\* replaces
the rule, and the undecided keys are hand-kept by a named list.

**The six disagreements, each read.**

| key | baseline | R\* | read | right |
|---|---|---|---|---|
| B57 `baryon 1, diquark 0, meson 1` | SOURCE | PAPER | reads `matter_sector_paper.tex` | **R\*** |
| G50 `eta fixes the abundances…` | SOURCE | PAPER | reads `cosmogenesis_paper.tex` through `git show` | **R\*** |
| S6 `r_s=2M` | PAPER | SOURCE | reads `KRE`, a receipt `.py` | **R\*** |
| P15 `mp\.mpf…` regex | RECEIPT | SOURCE | reads a receipt `.py`; `RECEIPT` is not a target | **R\*** |
| P15 transmission-ratios regex | PAPER | SOURCE | reads a paper; the trace names **no file kind** | baseline |
| P15 `Because the distance slicing is flat` | PAPER | SOURCE | in `CR_cosmology.tex`; the trace names **no file kind** | baseline |

**One deviation from the registered rule, from the measurement.** R\* as written sends an empty kind set to `SOURCE`
("no `tex`"). Its only two wrong calls are both empty-kind keys: a trace that names no file decides nothing. The
implemented rule sends an empty set to UNDECIDED too. That adds the 79 empty-kind keys (77 baseline `SOURCE`, 2
`PAPER`) to the annotation, for **140 annotated keys, 5.0%**, still under the negative. T1 is scored on the registered
rule (61). The 140 are the implemented rule's.

**What went in.**

- `scripts/mutate_assertions.py` `_rstar`: the target is per KEY, over the union of its sites' wide-trace kinds.
  `{tex}` → `PAPER`; kinds without `tex` → `SOURCE`; `tex` beside another kind, or no kind → UNDECIDED, resolved from
  `corpus/target_annotations.tsv`. The old `.tex`-in-narrow-trace test and `_only_tex` are gone.
- `corpus/target_annotations.tsv`: 140 rows. They are seeded from the baseline's hand-corrected column and **not
  re-read row by row**. The `evidence` column records only whether the literal (or a regex match) is in a
  `corpus/*.tex` today.
  - I read the 4 `PAPER` rows marked `tex-absent`. Three (`_POLC`, `taup_of`, `R^2/(1+R)`) test `fsrc`, the
    likelihood instrument's `.py`, which the baseline's own what-was-read says. They are `SOURCE`. The fourth is an ALT
    arm whose sibling arm is in the paper, so `PAPER`.
- `check_quote_pins` ⓼: an UNDECIDED key with no annotation fails, an annotation R\* does not need fails, and the
  baseline's `target` must equal the instrument's. So a hand correction lives in one place.
- `quote_pin_baseline.tsv`: 6 targets corrected to the instrument (G50 → `PAPER`; S6, the `RECEIPT` row, and the
  three `fsrc` rows → `SOURCE`). No verdict or what-was-read text changed.
- **B57 is left `SOURCE` and named in `TARGET_DISPUTED`, routed to 66.** The site tests `p14`
  (`matter_sector_paper.tex`), so R\* is right that it reads a paper. But the paper writes `baryon $1$, diquark $0$,
  meson $1$` in math mode, so the plain literal is not there. Its row is `MEANING-HELD`, re-filed `SOURCE` by 66 at
  r7255 so that H3 holds. Filed `PAPER`, H3 fails, which the first fast-suite run showed. That makes it a verdict
  question, and the verdict is not this seat's to edit.
- MULTI-SITE reads 246, under its ceiling of 249. MULTI is computed only on `PAPER` rows, so a re-filed key can move it.
- All 18 receipts that read the baseline ran green, and none needed a conversion.

**Not touched.** The T5 ubiquity arm in `cannot_fail` still picks its haystack from the narrow trace. It decides
which files to count, not a ledger column, so it is out of this order's scope.
