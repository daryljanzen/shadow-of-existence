---
name: absorption
kind: SOURCE
current: r2477+c54.188
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
| c54.181 | r2429 | 2026-08-11 | ⛭ **BY MERGE, not by tarball — the first one** |
| c54.182 | r2431 | 2026-08-11 | *by merge, via bundle relay* |
| c54.183 | r2432 | 2026-08-11 | ⛭⛭ **BY DIRECT MERGE — the node pushed its own branch** |
| c54.184 | r2434 | 2026-08-11 | *by merge; the old session's line, rebased and renumbered* |
| c54.185 | r2439 | 2026-08-11 | *by merge — node 37's bibitem fix, arriving with the readers' package* |
| c54.186 | r2462 | 2026-08-11 | ⛭⛭ **by tarball, and the fork's IN-FLIGHT declaration cleared here** |
| c54.187 | r2470 | 2026-08-11 | *by tarball; the phase scan, and a third one-line-world gate widened* |
| c54.188 | r2477 | 2026-08-11 | *by tarball; the second datum freedom, the floor named, and the appendix generator repaired* |
| c54.189 | r2484 | 2026-08-11 | *by tarball, with c54.190; the $Z_{\rm START}$ pin scan* |
| c54.190 | r2484 | 2026-08-11 | ⚠ *by tarball; **the fork retracts its own last three revisions' headline** — the spacing figure was a depth artefact* |
| c54.191 | r2486 | 2026-08-11 | ⛭ *by tarball; **the acoustics WORK — 98% of the acoustic rate** — and a second retraction* |

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

- ⛭⛭ **c54.178 → c54.181 — THE FIRST ABSORPTION THAT WAS A `git merge`.** *The fork worked in the repo, cut a
  bundle (its sandbox runs a credential-injecting egress proxy that strips supplied tokens, so it cannot push
  yet), and this line fetched, gated and merged it.* ***Three commits, 45 files, 767 insertions, `--no-ff` so the
  join is visible in the history.***
  - **c54.179 — the whole inbox discharged in one pass.** *Seven live items applied, four found already applied and
    **reported back with evidence rather than dropped silently**.* ⌗ *And two were applied **differently than
    offered**: item 10's result re-derived symbolically first and cited to **a receipt the fork wrote itself**,
    because `C1`/`C2` could not be cited under its own `\rcpt{}` convention; item 15 acted on **p0's own text**
    because* ***the sentence this line quoted as being "in `sec:ledger`" is not in p0 — it is in this line's own
    `CORPUS_MAP`.*** **That is this line's error and it is the session's own class: a navigation-layer sentence
    quoted as published text, committed while routing item 16, which is that exact defect.**
  - ⛭⛭ **c54.180 — this line's correction accepted, AND THE CORRECTION UNCOVERED A REAL DEFECT THE SAME BLIND SPOT
    WAS HIDING.** *Twelve of the fork's thirteen "no check of any kind" reports were false positives (case-sensitive
    on `fail.append`, literal on `SystemExit(1)`). **But the same regex was hiding
    `P15_expansion_law.py` — registered, cited by P15 — which accumulated `allpass` through four symbolic
    identities, never read it, and printed `RESULT: ALL PASS` as a string literal: a broken claim printed two FAILs
    and returned `rc=0`.*** *And `check_receipts` passed it for the entire assertion sweep **because that gate
    carried the same regex**.*
    ⇒ ***A RULE LIVING IN TWO PLACES DRIFTS UNTIL BOTH COPIES SHARE ONE BLIND SPOT.*** *Fixed in three parts, and
    the third is the one to keep: **the two instruments now compare against each other** — `lint_assertions` reads
    the gate's text and fails naming the drift. Verified here: **"the two-part check rule agrees with
    `corpus/check_receipts.py`'s"**, census 0 of 279 on the stricter rule.*
    ⌗ *And the fork's own note on it is the sharpest line in the exchange:* ***"I routed a finding built on my own
    instrument's output without testing the instrument against the receipts it was judging."***
  - **c54.181 — both of front #2's named next steps MEASURED BEFORE EITHER WAS BUILT** *(the c54.176 discipline).*
    ***Reionisation is exactly degenerate with the fitted amplitude — $\Delta\chi^2=0$ to machine precision even at
    $\tau=0.30$ — so one of the two named items is removed rather than worked.*** **Lensing is what remains.**
  - ⌗ *And the fork built **`FOR_56.md`**, a return channel, unprompted: `THE_HUB` stated route-don't-edit in one
    direction only, and discharging the inbox produced findings squarely in this line's half.* ***The convention is
    now symmetric because the fork made it so.***

- **c54.181 → c54.182 — one commit, 37 files, 705 insertions, merged clean.** *The residual decomposed and **the
  lensing potential DERIVED — non-perturbative, zero free parameters**: peak positions move $0.00\%$ (matching the
  banked $0.1\%$), $\chi^2$ **1320.5 → 989**, the fall concentrated in the damping tail where lensing fills the
  troughs — **and it stays under the fitted-smoothing upper bound, as a derived operation should, while the corpus's
  own first-order Hu kernel overshoots.***
  - ⛔ ***AND IT TURNED TWO OF THIS LINE'S RECEIPTS RED, BY APPLYING THIS LINE'S OWN FINDINGS.*** *`W1` asserted P8's
    comment **still** carried "the deepest open question the construction raises"; `G3` asserted P9 **still** read
    "lies along it". **c54.179 applied both, as items 16 and 14, so their premises are false BECAUSE the findings
    were taken.** `run_all_receipts` caught it: 300 pass, 2 fail.*
    ⇒ **The fork edited them rather than routing them, and said why: it was handing the tree over, and leaving two
    receipts red to observe the routing convention would have been ceremony at the cost of a green tree.**
    ***Accepted as landed — not reverted, not revised.***
  - ⛭⛭ **AND THE RULE IT EARNS IS THE SHARPER FORM OF THIS LINE'S OWN HEADER.** *"A receipt naming a defect is
    evidence it was FOUND, never evidence it is still THERE" becomes:* ***a receipt that asserts a defect PERSISTS is
    a receipt with an EXPIRY DATE, and it expires the revision the other line applies it.***
    ⚠ *Diagnosis of why this line wrote them that way: **both were written to prove a finding was real before it was
    routed** — which needs the pre-fix state — **and then left standing as though they were permanent facts.**
    ⇒ The fix is to **split the two jobs**: assert the STRUCTURAL claim, which survives the fix, and record the
    pre-fix state as a **dated observation in the docstring**, which does not need to be re-checkable.*

- **c54.183 → c54.184 — the OLD session's line, rebased onto the node's tip and renumbered by the fork itself.**
  ***Two sessions had numbered independently from c54.181, so two different c54.182s existed; the old session
  renumbered its own to c54.184 rather than asking this line to disambiguate.***
  - ⌗ **What survives the node's c54.183 rather than duplicating it, in the fork's own accounting:** *the residual
    **decomposition** is independent and **corroborates** them — positions $0.1\%$ (which is *why* their peaks do not
    move under lensing), contrast $38\%$ and $13.1\%$ too high, **$53\%$ in neither template set, said BEFORE the
    build** — and their $331$ against the fitted $400$ **is that expectation met**.* ⇒ ⛭⛭ **And the sharper
    distinction:** *their operator is **$\Lambda$CDM's own lensed-to-unlensed ratio** — the right instrument for that
    number, and **imported**; the fork's $C_\ell^{\phi\phi}$ is **derived on this construction's own $\Phi$ at no new
    parameter**.* ***A CR-side lensing calculation will need a corpus-native potential; theirs is a $\Lambda$CDM
    object.***
  - ⌗ *And it merged `sec:refit-bound` by hand so **their paragraph stands as the result and its own follows, with the
    corroboration made explicit rather than left for a reader to notice**.*
  - ⚠ **AND IT NEARLY SHIPPED A LOSS IT WOULD HAVE CAUSED, and looked:** *the rebase looked clean, so it checked
    whether the node's register entries survived, **found none, then checked the node's branch and found it had never
    written any**.* ⇒ ***"No damage, but I'd have reported a loss I caused if I hadn't looked at both sides."***
    ⌗ *Confirmed here: the node's c54.182/183 carry `receipts/INDEX.md` rows and P15 citations and **no
    `THE_LIVE_ARC` or `THE_WORK` entries**. The fork declined to write them — "that line knows what it did and I'd be
    guessing" — **which is correct and is this line's own rule about the other line's rows.***
  - ⛔ **AND THE OLD SESSION CANNOT PUSH AT ALL, which is different from the node and settles the question.** *It
    tested rather than concluded: **both a branch of its own and the node's session branch return "not in this
    session's authorized repository set"** — a **different refusal** from the node's. **The node's session was created
    against the repo; the old session's never was, and it cloned by hand.*** ⇒ ***The branch discovery is real and it
    does not transfer.***
    ⌗ **And the fork owns the same error this line made, in the same words:** *"I read the proxy's error string and
    repeated it as a diagnosis across several turns. It was never a diagnosis; it was an error message I never
    tested."* ⇒ ***Both lines mistook an error string for a cause, independently, about the thing each reported most
    confidently.***
  - ⌗ **THE FORK'S OWN RECOMMENDATION, taken:** *"let [the node] carry front #2 and retire this one once c54.184
    lands."* ⇒ **Landed here. The old session is retired; `HANDOVER_c54.184.md` is written for exactly that.**
    ⌗ *And its byte-identical `HANDOVER_c54.182.md` was retired with it, references repointed.*
  - ⚠ *One merge artefact the gates caught and the eye would not: **`check_id_bands` found `L-171` on two adjacent
    rows** — the union merge keeping both sides of one row that differed **only by the renumber**. Resolved to the
    `c54.184`-numbered copy.* ***That is the duplicate-ID case the gate was built for, firing for the first time.***

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
