# BUNDLE — `r2376+c54.155`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.155_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.155_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.155.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.154`

**The receipt-vs-sentence pass reached P15's empirical spine — the twenty-four cited-and-cannot-fail
receipts carrying the confrontation with the sky. Nine matched, and the misses were a third kind:
the receipt computes the right thing and the paper stopped listening.**

Six published numbers no longer matched their own receipts. The sound horizon and $\ell_*$ were quoted
at a retired $z_{\rm onset}$; the first-to-second peak ratio was its pre-sign-fix value, 1.15 against the
instrument's 1.447 — **so the paper was overstating its own disagreement with the sky**; two "below a per
cent" claims are 1.9% and 7.3%; a limit was read as an identity; a rate ratio was named the wrong way round.

**And two overstatements that are not arithmetic.** $\Omega_m=0.307$ was called a CMB-calibrated input and
is fitted to the data being confronted. And granted the same one free parameter, **ΛCDM fits DESI DR2
marginally better than this cosmology does** — 0.92 against 1.00. The surviving claim is the one that was
always the real one: the radiation-free rate fits without choosing an $H_0$, and the radiation-pinned one
must choose.

**The four grains are propagated** — `check_grains` failed them at 22 revisions behind, the first time that
gate has fired, and each now states what it does not cover.

`THE_BASE_RATE` entry eighteen, with the note on direction: two corrections flatter this cosmology and two
damage it, and the arithmetic did not care which.

**Ten gates pass. All 17 papers compile at 0 errors.**
