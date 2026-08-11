# BUNDLE — `r2376+c54.159`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.159_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.159_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.159.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.158`

**P03 is cleared in full — all 36 — and the assertion debt is 124 -> 88.** The fork's own grandfathered share
is down to 15. Three dispatched batches, every added check mutation-tested by its author, 102 files touched
and re-run with zero failures. And the findings are now folded into their `INDEX` rows the same revision
rather than banked.

**Three findings, all the same shape: a check that cannot fail.** One computes
`sqrt(Rv**2-1) - sqrt(Rv**2-1) == 0` and prints PASS at every dimension; one hardcodes `True`; one is a loop
that never touches the variable whose variation it claims to test. A fourth prints "CLOSURES ARE MOSTLY
QUALIFIED IN PLACE (0% carry a bound or a proof on the same line)" -- a sentence contradicting its own number,
because the sweep scans the wrong directory.

**And the lint could not see any of them.** It reads `assert`; these use a local `check(label, condition)`
helper that prints PASS/FAIL. *The scorer built to stop the sweep producing hollow work could not detect
hollow work already there in a different syntax.* Extended to read check-shaped calls and the difference form,
it immediately found two live hardcoded `True` conditions -- including one in `P08_E1_cosmology` that no
worker had looked at, printing PASS for the claim that a marginally bound geodesic never turns around.

`THE_BASE_RATE` entry twenty-two: **an instrument built against one syntax measures a syntax, not a property**
-- and a sweep samples densely enough to show you what your own gate is blind to, which an audit cannot,
because an audit reads what it was pointed at.

**Ten gates pass. All 17 papers compile at 0 errors.**
