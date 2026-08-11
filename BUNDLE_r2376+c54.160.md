# BUNDLE — `r2376+c54.160`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.160_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.160_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.160.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.159`

**P15 is cleared in full — all 29 — and the assertion debt is 88 -> 59.**

This is the sector where number-drift is measurably concentrated: the c54.155 audit found six published
figures its own receipts no longer produced. The paper was corrected then; **this revision makes the
correction permanent by pinning the current figure inside the receipt**, so the next retune breaks the gate
instead of the sentence.

**And a registered, cited receipt turned out to be unrunnable where it is registered.** `ROBUST_p1p2_scan`
exits 1 on `ImportError` before reaching a single line of computation. *No gate saw it, because nothing in
the corpus has ever RUN the receipts* — the census reads source, the lint parses it, the compile gate builds
the papers. So a receipt could be broken outright and every gate would stay green. Fixed; a gate that runs
every registered receipt is registered as **owed** rather than built, because it costs an hour of wall clock
and the place to decide that is against the sweep's end.

Three further paper-receipt divergences folded into their `INDEX` rows the same revision — including a
redshift the paper reported as 6873 which the current integrals return as **6844**, now carried in the paper
with both numbers, because 6844 sits nearer the retired value and *sharpens* the withdrawal it was written to
support.

`THE_BASE_RATE` entry twenty-three: **an instrument that reads a file has not run it.**

**Ten gates pass. All 17 papers compile at 0 errors.**
