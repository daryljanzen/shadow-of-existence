---
name: absorption
kind: SOURCE
current: c54.178
job: The DECLARED record of every absorption of the working fork — fork revision, the main-line revision that absorbed it, the date. Read by corpus/check_absorption.py. Nothing else in the tree can prove the fork has advanced.
sources: [chat]
---

# ABSORPTION — the declared record

> **⌗⌗ WHY THIS FILE EXISTS, AND IT IS THE ONE GAP NO OTHER GATE COULD SEE.**
>
> *Every currency measurement in this tree is taken against "the fork front", and **the fork front is read out
> of this tree's own documents**. So if the working fork advances twenty revisions and nothing is absorbed, the
> front does not move, every document still measures as current, and*
>
> ***the tree reports itself perfectly up to date with respect to a number it wrote itself.***
>
> *That is the r2377 defect one level up. `check_currency` used to read the front from a document frozen at
> c54.35, so **the baseline sank with the documents it measured** and every register looked current while
> `CORPUS_MAP` was 76 revisions behind. The fix there — take the max over all fork-carrying documents — is
> still, unavoidably, **a maximum over our own files.***
>
> ⇒ **So absorption is DECLARED, not inferred**, like `current: none` and `DECLARED-UNDATED` and `[REPORTED]`
> before it. ***The only thing that moves this file is an absorption actually happening.***

## The record

| fork revision | absorbed at | date |
|---|---|---|
| c54.108 | r2377 | 2026-08-10 |
| c54.134 | r2377 | 2026-08-10 |
| c54.153 | r2385 | 2026-08-10 |
| c54.163 | r2393 | 2026-08-11 |
| c54.178 | r2427 | 2026-08-11 |

## What each absorption cost, so the next one is planned rather than discovered

- **c54.108 → c54.134** *(first trail audit).* `audit_trail.py` written for it. The fork's own 124-revision
  changelog gap found and recorded as unrepairable rather than papered over.
- **c54.134 → c54.153** *(19 revisions).* ⚠ ***The most instructive one so far, and none of its three findings
  appeared in the diff:***
  - *The auditor **cried wolf**: 58 "DROPPED" files, all of them build cruft, because `cut_bundle.sh` excludes
    build output by design. **A correctly-cut bundle will always look like it dropped ~58 files**, so the section
    printed first and labelled irrecoverable would have been noise on every run. Partitioned.*
  - ***Three annotations were silently lost.*** *Absorption takes the fork's version of the files the fork owns.
    Our **rows** survive as re-inserted lines; **an annotation written INTO one of the fork's rows is guaranteed
    to be dropped, every absorption, forever.** Found only by `id_space_census --check` flipping to name `PO-4`
    and `A·2`. Fixed as `scripts/reapply_annotations.py`, declared and idempotent.*
  - *Seven files needed **real three-way merges**; 27 documents were **duplicated** (top level from the fork,
    `retired/` from our record cut) and had to be removed.*
  - ⚠ ***And the ID space was a near-miss by luck***: our rows begin at `L-174` because the fork's maximum was
    `L-173` and the fork has not added one since. **Had it, the two lines would have collided in the one
    namespace both write to.**

- **c54.153 → c54.163** *(10 revisions, **337 files changed** — the largest span by file count and the
  smallest by register movement: registered/struck/open unchanged at 166/162/4).*
  ⌗ ***IT IS THE RECEIPT SWEEP, and it is `L-208` answered***: **191 receipts changed and 186 gained assertions.**
  *Re-run after the merge:* **277 receipts, 277 carry a failure path, ZERO cannot fail** *— from 99 with none and
  95 of those cited. The gate that was built from the fork's own three-receipt finding now passes on the whole
  corpus.*
  - *Zero dropped, nothing shrank, no frontier list changed. New: `computations/baryon_edge` (25 files) and
    `computations/dimension_question` (9).*
  - ⚠ ***ONE GENUINE CONTENT COLLISION, and it reversed one of this line's own placement decisions.*** *At r2378
    this line **folded a paragraph out of P7's frontier list** under `RG-1`; at c54.163 the fork **extended that
    same paragraph in place**, adding the fixed-$k$ reading that makes the selection rule "a criterion on
    **species**".* **Checked before deciding: every phrase of our folded version is present in theirs** — *same
    physics, better developed, in the place its author chose.* ⇒ **Took the fork's paper wholesale.**
    ***The fork owns the papers; `RG-1` is this line's discipline and not a claim on the fork's text, and a
    placement decision the author has since worked against is superseded, not defended.***
  - *The other half of our P7 change was the dependency matrix, which is generated and simply regenerates.*
  - *ID space clean again: 36 rows re-inserted, **zero collisions** — the fork still has not opened a row above
    `L-173`.*

- **c54.163 → c54.178** *(15 revisions, **26 changed, 40 added, ZERO dropped, nothing lost**). The acoustic
  front: a **Boltzmann photon hierarchy to $\ell=24$ with polarisation inside the transfer**, the shear
  coefficient **derived rather than remembered** (and $\chi^2$ preferring the other value by 1123 units, recorded
  and refused), and the height target found to be **below the resolution of its own statistic** — the sky's own
  ratios are $2.256\pm0.077$ and $2.280\pm0.074$, so the earlier $2$–$3\%$ claims were inside the error and the
  $13\%$/$34\%$ were four and ten sigma and stand.*
  - ⛭⛭ ***FIVE OF THE SEVENTEEN ROUTED ITEMS WERE APPLIED BY THE FORK***: *`PO-8`'s closed gate, family 6's
    pointer at struck `L-164`, "seven families are open" in **both** `README` and `INTRODUCTION`, **all four
    published-paper typos**, and `A·1` folded.* ⇒ **This line's four text repairs are RETIRED — the fork made
    them.** *Protocol step 4 paying off exactly as designed:* ***check the fix, not just the diagnosis.***
  - ⛔ ***THE ID COLLISION FIRED.*** *At c54.166 the fork opened its own **`L-174`**, folding `A·1` — and this
    line's `L-174` was `PO-5`. **`THE_HUB` had called it a near-miss twice by luck.** This line yielded: the row
    moved to **`L-221`** and every live citation was repointed. **The bands were corrected and the gate rewritten**
    — see `THE_HUB`.*
  - ⌗ *And the fork's `L-174` **splits `A·1` into an ungated classical half and a `PO-6`-gated non-perturbative
    half** — **exactly the split this line made at `L-207` at r2383**. Two lines, same map item, same split,
    different IDs.*
  - ⌗ **`FOLD52_ASSESSMENT.md` arrived** — the 52/53 acoustic fold, and it carries the strongest corroboration this
    front has: ***"two nodes, two instruments, two fork lines, same result, neither knowing of the other"*** on the
    comb's invariance under initial data. ⚠ *And its own honesty: **the fold's reproduction gate does not reproduce
    in the fork's environment** ($\ell_1=229.6$ against the required $221.1$), diagnosed as a stale-path import.*
  - ⚠ *The fork's whole c54.164–178 changelog block is **absorbed verbatim** into `CORPUS_MAP`, kept unedited,
    because* ***the fork's account of what it did is the thing a file-level diff cannot produce.***

## ⛔⛔ STEP 6 WAS WRONG FOR THREE ABSORPTIONS — corrected r2427

*The duplicate sweep removed a top-level file whenever a copy existed in `retired/`, "after verifying against the
pristine incoming tree". **The verification asked the wrong question.***

| | |
|---|---|
| **what it asked** | *did the fork **change** these since the baseline?* |
| **what it should ask** | ***does the fork still HAVE them at top level?*** |

***Unchanged is not absent.*** *All twenty-nine so-called duplicates were present in the fork's tree the whole
time — **the fork does not retire by moving; it keeps both copies** — so the sweep was deleting live files on the
strength of a filename match.

**⌗ WHAT IT COST: `README.md` and `INDEX.md` were deleted from this line's tree at r2385 or r2393** *and never
existed in git at all.* ⚠ **And the reason nobody noticed for three absorptions is the sharp part:** *routing item
3 checked `README.md` for "seven families are open" —* ***and read the FORK's copy, because this line's did not
exist.*** **Every check of those files silently went to the other tree.**

⌗ ***AND THE GUARD FIRED AND WAS IGNORED.*** *At r2427 the sweep printed **"changed by the fork since c54.163:
['README.md', 'INDEX.md']"** and the removal ran anyway, because the removal loop did not consult the check it had
just performed.* ⇒ **A guard that prints and does not gate is a comment.** *The check now decides.*

**⌗ THE CORRECTED STEP 6.** *Remove a top-level file only if **the pristine incoming tree does not carry it at top
level**. Never on a filename match with `retired/`, and never on "the fork did not change it".*

## The protocol, in the order that survived contact

1. **Re-extract the previous bundle into a clean directory.** ***A baseline is a record, and a record you have
   run scripts inside is no longer one*** — the c54.134 baseline on disk carried six of our own instrument files
   from a one-off `cp`, and diffing against it would have reported them as **dropped by the fork**, at the top of
   the one section whose findings cannot be recovered. `audit_trail.py` now refuses such a baseline by name.
2. **Run `audit_trail.py old new`** and read DROPPED and SHRANK before anything else.
3. **Three-way diff** against the pristine baseline: files changed by both need real merges; by the fork alone,
   take theirs; by us alone, take ours.
4. **Re-apply the text repairs** — and check each against the new tree first, because the fork may have fixed it.
5. **Run `scripts/reapply_annotations.py`** — step 3 covers annotations, not only repairs.
6. **Remove duplicates** created by the merge, after verifying the fork changed none of them. *Verify against the
   **pristine incoming tree**, never against the merged one: doing it against a tree our own repair pass had just
   edited returned three false positives.*
7. **Regenerate every view**, refresh the dependency matrix and the appendices, then run the whole gate suite.
8. **Record the absorption here.**
