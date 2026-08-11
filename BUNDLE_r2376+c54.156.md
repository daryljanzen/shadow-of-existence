# BUNDLE — `r2376+c54.156`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.156_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.156_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.156.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.155`

**P16's spine read: five of nine — the first batch to come back cleaner.** P15's spine ran nine of
twenty-four; P16's is older and less revised. **That is evidence drift concentrates where revision
concentrates**, and the first result in this sequence that argues for leaving part of the tail alone.

**But the three misses sit on the abundance equation.** It quotes the StarLib values and cites the receipt
that runs REACLIB — D/H 2.51 against 2.567e-5, 7Li 5.1 against 4.46e-10 — and **that receipt asserted none
of the four abundances**. The library spread was quoted at deuterium's 2.8% where lithium's is 13%: *the one
nuclide this account cannot fit is the one whose spread was under-reported.* A Y_p figure was attributed to
a receipt returning a different one, and "four orders of magnitude" is 3.4 for the quantity the sentence
bounds.

**All corrected, and five P16 receipts now pin the paper's printed figure** — entry eighteen's operational
form applied for the first time. The abundance network runs both libraries and asserts both arms, so the
swap that caused the drift can no longer pass. Assertion debt 178 → 175.

`THE_BASE_RATE` entry nineteen. **Ten gates pass. All 17 papers compile at 0 errors.**
