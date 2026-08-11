# BUNDLE — `r2376+c54.161`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.161_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.161_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.161.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.160`

**The assertion debt is zero — from 188 when the census was taken — and the runner is built.**

59 receipts swept across P14, P17, P07, P08 and P09. All 276 now carry at least one check, none is hollow by
any form the lint detects, and **every registered receipt has been run, in place, and exits 0**: 275 pass, 0
fail, 463 seconds. `scripts/run_all_receipts.py` is the eleventh gate, deliberately outside the standing ten
because it costs wall clock the others do not.

**And its first pass found a live failure.** `P15_the_low_ell_minimum_is_at_ell_four` pins the paper's prose
at eight sites, and six broke when c54.155 rewrote that paragraph — the edit inserted a `\rcpt{}` marker
inside the very sentences it matches. Every claim was still true; the citation moved, not the physics.
***But the receipt had been failing for five revisions and nothing knew, because nothing ran it.***

**The lint also caught three hollow assertions the sweep itself had written** — `assert 3*2*2 == 12` and two
like it, arithmetic dressed as claims — plus two more on the same extension, one pre-existing in a sector
nobody was sweeping. Nine earlier markings were retired by computing the missing thing rather than restating
it.

`THE_BASE_RATE` entry twenty-four. Its point is the sequence's: **all three instrument lessons were learned
from the work they were meant to govern**, and the sweep was the only thing dense enough to find them,
because it touched every file rather than the files someone suspected.

What zero means is stated exactly in the debt file: every receipt carries a check, none is hollow, every one
runs. It does *not* mean every claim is pinned — 24 receipts carry only UNPINNED structural checks.

**Ten gates pass. All 17 papers compile at 0 errors. 275 of 275 receipts run.**
