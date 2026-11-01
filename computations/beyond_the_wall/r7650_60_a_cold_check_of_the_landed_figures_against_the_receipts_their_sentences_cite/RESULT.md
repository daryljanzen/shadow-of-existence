# r7650 (60) — RESULT

**The order's reachable negative is NOT reached. Of the `93` figures in scope, `85` reproduce in the
receipts their own sentences cite and `8` do not — and `3` of those are proved MIS-CITED by a run:
the number is right and the corpus computes it, but the sentence points at receipts that do not.
One of the three is `0.958`, in *"inside the distance data's own width"* — one of the three claims the
order named to test hardest.**

**And before any of that could be measured: the cold check was not runnable in this container at all,
because the verified environment was missing one of its own pinned dependencies.**

Receipts: `build_sites.py`, `run_cited.py`, `rerun_blocked.py`, `cold_check.py`, `locate.py`.
Twelve arms: **eight hold, one fires as the order's negative, two miss, and one is a MISS that is the
point of the revision.**

---

## ① ⚑ The container finding, which came first and is worth the most

Nine of the cited receipts died on `ModuleNotFoundError: No module named 'camb'` — among them
`…the_licensed_rebuild…`, cited for *"level with the control's own value"*.

- `requirements-ci.txt` — *"the environment the corpus's float comparisons are verified on"* —
  **pins `camb==2.0.4`**, and says it is pinned *"because it computes the spectra the whole acoustic
  sector measures on"*.
- This container's pinned interpreter had **python 3.11.17, numpy 2.4.6, scipy 1.17.1 and no camb at
  all**. The only interpreter here that had camb had **2.0.5**, beside **numpy 2.5.3 and scipy
  1.18.1** — three libraries off the pin, which is the `ENV_FINGERPRINT` event itself.
- ⇒ `camb==2.0.4` was installed **with `--no-deps`** and **verified to have moved nothing**: python,
  numpy and scipy unchanged, `check_env_fingerprint` **green**. All nine then ran **green in under
  ten seconds each**. **Arms ⑥, ⑦, ⑧ hold.**

⌗ *So the whole of this check was one missing pinned dependency away from being impossible, and
nothing else stood in its way.*

⛔ **And the gap that let it happen, routed and not repaired here:** `check_env_fingerprint` pins
blas, numpy, python and scipy and **does not fingerprint camb** — the one library most able to move
the acoustic figures with no push and no gate, which is the exact event that fingerprint exists for.

## ② What ran

| | |
|---|---|
| receipts the sentences in scope cite | **35** |
| RAN to completion (one bounded run each) | **34** — **arm ② holds** |
| UNRUN, reported with its budget rather than dropped | 1, at 420 s |
| `INCONCLUSIVE (container)` after the install | **0** |

## ③ The figures

**34 sentences, 93 figures**: **85 REPRODUCES** (80 of them verbatim in the output), **8 ABSENT**,
0 UNRUN, 0 inconclusive.

Of the 8 absent, **3 are cc66's already-tabled namesake leftovers** — `0.2974` twice (its item 10,
the caption's DESI-alone background) and `0.855` (item 2, the shared-fraction cosine) — and are
**excluded, not reported as defects**. **Arm ⑤ holds.** The remaining **five**:

| figure | sentence cites | computed instead by | verdict |
|---|---|---|---|
| **`0.958`** | `…at_its_own_preferred_H0…`, `…the_133_bin_pair…` | **`…the_phase_moves_with_the_datum…`** and **`C22_the_end_to_end_number`** | **MIS-CITED** |
| **`298.0`** | `…at_its_own_preferred_H0…` | **`…the_crossing_spectrum_reproduces…`**, **`…the_likelihood_pair…`** | **MIS-CITED** |
| **`298.0`** | `…the_symmetric_comparison…` | the same two | **MIS-CITED** |
| `0.75` | `…the_selection_does_not_truncate…`, `…the_peak_plane_survives…` | **not located** | ABSENT, unlocated |
| `12.5` | the same pair | **not located** | ABSENT, unlocated |

**Each mis-citation is proved by a RUN, not by a grep:** the receipt that does print the figure was
executed and printed it. *A wrong address is only a finding if the right one exists* — and for
`0.75` and `12.5` it was not found, so they are reported as **unlocated** rather than as wrong.

## ④ ⛔ The three claims the order said to test hardest

| claim | verdict |
|---|---|
| *"level with the control's own value"* — `186.135`, `87` | **both REPRODUCE** |
| the unreachable `276.4` and its gap `90.4` | **both REPRODUCE** |
| *"closes more than half of the arm's excess"* | no figure in the sentence; it is a **share**, and its receipts ran |
| *"inside the distance data's own width"* — `0.958` | ⛔ **ABSENT from both cited receipts — MIS-CITED** |

⇒ **ARM ③ MISSES, and it is the point of the revision.** The claim stands — `0.958` is real and the
corpus computes it twice — but **the sentence that makes it cites neither receipt that does.** A
reader following the citation finds no `0.958`.
⇒ **ARM ① FIRES**: the order's reachable negative — *every landed figure reproduces* — is **not
reached**.
⇒ **ARM ④ HOLDS**, and it was registered **against** that negative before anything ran.

## ⑤ `P7` and `P18`

Neither passage carries a `\rcpt{}`; both cite the paper, so `P15` itself is the address. **`P7`
l.1863's four figures were checked against this seat's own scorer from `r7646`** — a colder
instrument than any receipt in the corpus for exactly these numbers — and **all four reproduce**:
`1.16` and `2.71` per bin on 185 bins (`1.1573`, `2.7141`), `2.35` no-fit (`2.3460`), `1.60`
refitted (`1.5960`). `P18` l.1558's `58 times` is cc66's item 8 and is left alone.

## ⑥ ⛔ Four of this revision's own rule conditions were corrected, every one by a measurement

1. The verdicts did not cover *ran, but crashed before computing* → `INCONCLUSIVE (container)` added,
   restrictively, so a missing dependency could never be reported as a mis-citation.
2. **The unit of the check was wrong.** The first form made one site per `(sentence, receipt)` pair,
   each carrying all the sentence's figures, so a figure one cited receipt computes read ABSENT
   against the others: **65 absences, nearly all that artefact.** Corrected to the **sentence with
   its whole citation set** — *an identification has to be checked on the loci the object itself
   distinguishes* — and the count fell to **8**. **Arm ⑩ holds** (under 25). The 65 is kept above.
3. A grep was not allowed to stand for a run: the computing receipts were executed.
4. The verbatim count is printed beside the total, because the registered match rule admits a numeric
   hit within half a printed digit and a long table can meet that by coincidence.

⌗ **A routed observation, not a repair:** `check_figures_pinned` keys its own sites on
`(population, paper, RECEIPT, figure)` and therefore **has the same property by design** — a
multi-cited sentence's figures are flagged against every cited receipt that does not pin them. That
is plausibly part of why its baseline is as large as it is. The gate is not this seat's.

## Scope

No paper is edited, no figure moves, no parameter is pinned, no quote-pin key is minted, no gate,
ledger or census is added, and no receipt of `70`'s or cc66's is touched. The only change to the
container is the installation of the version `requirements-ci.txt` already pins, verified green.
