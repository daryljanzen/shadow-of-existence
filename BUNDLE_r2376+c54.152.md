# BUNDLE — `r2376+c54.152`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.152_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.152_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.152.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.151`

**The registry debt is discharged.** `check_withdrawn` goes from two registered withdrawals to six,
each with its grounds, and gains two structural pieces: a **self-test** (every registered pattern must
still fire on the text its withdrawal removed — a pattern that matches nothing is indistinguishable
from one that is broken) and a rule that **in a markdown table the correction must sit in the same
row**. Verified retrospectively on the pre-c54.151 tree: the gate goes from flagging nothing in
`THE_WORK` to flagging five, and from nothing in P16 to eleven.

**And the pass found three more defects.** P16 asserted the withdrawn cycle a second time, as the
stated ground for withdrawing the five composition bounds — rewritten, and the withdrawal now stands
on two grounds that survive. **The scalar monodromy $4\pi/\rho$ was cited to the receipt that computes
the tensor's $2\pi/\rho$** — the link resolved, the receipt passed, and the claim had no computation
behind it; the receipt is now built and cited. **And building it found the closed form itself was an
$A=2$ specialisation** — $z_S=a(a+2B/3)/a'$ adds a length to an area at any other $A$; the variable is
$z_S=a(a+4B/3A)/a'$, corrected in two papers and four standing documents. Nothing numerical moves.

`THE_BASE_RATE` entries fourteen and fifteen. **Ten gates pass. All 17 papers compile at 0 errors, 0
undefined citations, 0 undefined refs, 0 dead receipt links.**
