# BUNDLE — `r2376+c54.154`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.154_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.154_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.154.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.153`

**The gate was taught to see what the audit saw, and the census is the finding: 188 of 276 receipts
carried no check at all** — two thirds of the reproducibility layer, where `OK` certifies that Python
exited zero. `check_receipts` now enforces a ratchet: a receipt of this fork with no check fails unless
it is *named* in `receipts/ASSERTION_DEBT.txt`, the total may never rise, and that file may only ever be
rewritten downward. **Verified by making it fail on demand.** Debt worked 188 → 180 this revision, each
receipt given a check of its *claim* — the throat tower's split proved for every $\ell$ rather than six
sampled; the leg factor's $k$-independence computed across four decades; the closed-$S^3$ weight shown
equal to $\mathrm{d}\ln k_L/\mathrm{d}L$ exactly.

**And the pass rerun on the receipts that are cited AND cannot fail returned one match in sixteen.** A
receipt that prints `False` for its own claim and states the conclusion anyway — its docstring diagnosed
the bug and the code kept it. A "check that could have failed" which is a tautology on any rational. A
paper clause cited to a receipt that retracts it in its own text. A census that never opens a file. All
four fixed, six `INDEX` rows corrected, eleven verdicts registered.

`THE_BASE_RATE` entry seventeen, which revises sixteen rather than repeating it: **the assertion-free
receipt is not the mechanism but the selector** — 14/28 on a sector chosen at random, 1/16 when the
subset is chosen by "cannot fail". The property predicts the failure, so what is owed is not another
blind pass but the debt list, and the debt list is written down.

**Ten gates pass. All 17 papers compile at 0 errors, 0 undefined citations, 0 undefined refs, 0 dead
receipt links.**
