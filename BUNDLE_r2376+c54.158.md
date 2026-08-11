# BUNDLE — `r2376+c54.158`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.158_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.158_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.158.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.157`

**The assertion sweep opens: debt 172 -> 124, forty-eight receipts, zero hollow assertions corpus-wide.**

**The scorer was built before any of the sweep was written.** The work is mechanical enough to dispatch, and
that is exactly what makes it dangerous -- a worker measured by a count can satisfy the count with a check
that cannot fail. `scripts/lint_assertions.py` classifies every assertion HOLLOW / UNPINNED / PINNED, is wired
into `check_receipts`, and was verified by planting a hollow file and watching the gate go red.

**What the workers returned:** not one hollow assertion, every check mutation-tested by its author, and four
of them **refused to weaken an assertion that failed**, reporting the disagreement instead. They also found
defects nobody asked for -- a printed coefficient of $-9/2$ where the file's own normalisation gives
$-\sqrt3$, a receipt printing "$\alpha$ is invariant, $2M$ is not" above a computation showing the reverse,
two transposed endpoint labels, a control block testing the literal `2 <= 3`. *A sweep for one defect finds
others, because the only way to write an assertion of a claim is to understand the claim.*

And the sweep's own side effect -- ORIGIN drift, caught by the guard at $24\to35$ -- is closed by
`scripts/propagate_to_origin.py`, now at **21, below where it started**.

`THE_BASE_RATE` entry twenty-one. **Ten gates pass. All 17 papers compile at 0 errors.**
