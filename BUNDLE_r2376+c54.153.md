# BUNDLE — `r2376+c54.153`

**Two parts, each under 30 MB, no file split across parts. Together they are the whole programme.**

| part | file | size | contains |
|---|---|---|---|
| 1 | `CR_bundle_r2376+c54.153_part1_corpus.tar.xz` | 24 MB | every top-level document, `corpus/`, `figures/`, `receipts/`, `verification/` |
| 2 | `CR_bundle_r2376+c54.153_part2_working.tar.xz` | 14 MB | `computations/`, `capstones/`, `scripts/`, `forks/`, `kills/`, `resources/`, `retired/`, and the build/work directories |

Both extract to a single top directory `cr_r2376/`; extract part 1 and part 2 into the same place and
the tree is complete. **Verified this revision by extracting both parts and running a recursive diff
against the working tree — zero differences.** Checksums in `BUNDLE_r2376+c54.153.sha256`.

*The split is now a script rather than a hand procedure: `scripts/cut_bundle_two_part.sh`, written
this revision because the hand version had once cut a file across parts.*

---

## What is new since `r2376+c54.152`

**The receipt-vs-sentence pass on the perturbation sector: twenty-eight cited receipts read against
the sentences citing them, and fourteen matched.** Three mismatches, four scope-drifts, seven narrows.
All three mismatches are settled by computation rather than by wording.

**A factor of four stood between P15's transfer law and its own receipt.** The paper reads
$\mathcal{P}=18k^3D_k^2/(M^2\rho^6)$; the receipt asserted $9/2$. Propagating the same physical initial
condition under each potential returns exactly $2$ in amplitude at every composition tested, so the paper
is right and the receipt was nine revisions stale — **and the monodromy doubling is the entire effect**,
which is not obvious, since $z_S\propto a^{3/2}$ in the matter era and the final divisor changes too. Those
two differences cancel.

**A cross-validation's second Boltzmann arm was the paper's own figure caption**, read by regular
expression. The programme's photon hierarchy is now actually driven: the shape cross-validates (minimum at
$\ell=4$, recovery by $\ell\simeq7$) and the depths do not. The quoted quartet and the "uniformly
10–25% deeper" spread are withdrawn.

**And the sharper finding: the dominant failure is not a wrong link but a receipt that cannot fail.** Three
receipts in one cluster contain no assertion at all. That is how P15's "stable under $\pm2\%$ in $r_0$"
rode inside a green receipt for two revisions; measured this revision, the shape is stable and **the depths
drift by up to 15% at $\ell=4$**.

`THE_BASE_RATE` entry sixteen. **Ten gates pass. All 17 papers compile at 0 errors, 0 undefined citations,
0 undefined refs, 0 dead receipt links.**
