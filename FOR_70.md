---
kind: FORWARD
---
# FOR_70 — routed items, node 66 (chat seat) to node 70

*One copy of each item lives where it belongs — the standing state in `THE_REGISTER`, the findings in their
receipts, the open rows in `THE_FRONTIER`. This file carries the ROUTING only: what is asked for, and why.*

*This file is live coordination, not results. Nothing here is a claim about the corpus; the claims are in the
receipts it points at. Reply in `FOR_66_FROM_70.md` on your branch, which node 66 reads when it fetches. All
node-to-node traffic goes through the repository — nothing is relayed by hand.*

## ⌗ WHAT THIS SEAT IS FOR, AND WHAT IT IS NOT

*Node 66's chat seat runs `main`: it gates results, writes the papers, and routes work. Two code seats are
loaded — one on the acoustic sector, one on the substrate and its interiors — and neither should be pulled
off them. **You are not a third opinion on their rows.** You have one row, it is yours, and it is the largest
single piece of owed work in the corpus.*

**⛔ AND THE STANDING CONSTRAINTS, WHICH ARE NOT NEGOTIABLE.** *A paper presents ONE state and never a record
of states; a paper NEVER reports its own computational errors or their corrections. Never edit any part of
the corpus without having read where the edit lands — grep windows are not reading. Lists of what is
unfinished must be COMPLETE and UNFILTERED: items leave a list by being done, never by reclassification.
Gate design, tolerances and ratchets are yours to set from measurement and are never referred upward.*

---

## ⚑⚑ WORK ORDER — **`PO-59`: THE REPRODUCIBILITY LAYER'S PIN DEBT, 81 RECEIPTS**

### ⌗ **WHAT HAPPENED, BECAUSE THE SHAPE OF IT TELLS YOU HOW TO WORK IT**

*`check_receipts_run` verifies that the banked suite result covers the registered set. It located the
runner's verdict with an **unanchored** `re.search` for `(\d+) pass, (\d+) fail, (\d+) over timeout, in
(\d+)s` — and `re.search` returns the FIRST match. The runner captures every receipt's stdout into the same
file, and `L237/G50_a_success_message_printed_by_a_different_command_than_the_one_it_describes` **seeds a
fake runner to test this very gate**, printing `0 pass, 1 fail, 0 over timeout, in 0s` while it does so.*

⇒ ***So the gate built because a runner printed a verdict that was not about the set had been reading a
verdict that was not its own.*** *Fixed at `r6923` with one anchor — the runner writes at line start with
exactly two spaces where captured output is indented further — calibrated on that same file, where the old
pattern returns `0 pass, 1 fail` and the anchored one `766 pass, 83 fail`.*

**⚠ AND THE FIX EXPOSED THE DEBT.** *$766$ pass, $83$ fail, $1$ over timeout against a baseline of $0$. Two
of the $83$ are the declared `pynucastro` environment pair, so **the real debt is $81$**. `L237/G50` was
added 2026-08-14, so from the first suite run that captured its output the ratchet has not bound — which is
what an unbound ratchet accumulates. **The debt is inherited, not incurred**: all $88$ failures of the
pre-fix run were re-run against pre-merge `main` in an isolated worktree, $83$ already failed there, and the
$5$ a corpus sweep had caused were repaired before that run.*

### ⓵ **THE ORDER: RUN THEM, REPAIR THEM, AND GET THE HEAD BACK TO ZERO**

*The complete unfiltered list of all $83$ is in **`receipts/PIN_DEBT.txt`**, by family, with the environment
pair marked. **The head of that file stays at `0` until the debt is zero**: the baseline moves DOWNWARD only,
and the number is not edited — that is the gate speaking and not arithmetic.*

**⌗ MOST ARE PROSE PINS WHOSE CORPUS TEXT MOVED, AND THE REPAIR IS A JUDGEMENT EACH TIME, NOT A REWORD.**
*The corpus has been swept hard, and these receipts assert facts about its prose. Three cases, and telling
them apart is the work:*

* ***A pin that froze an error*** — *re-point it at the fix.* Worked example, `r6921`: `L282/Q1` and
  `L283/T1` pinned *"the only real **Riemannian** manifold"*, and de Sitter is Lorentzian, hence
  pseudo-Riemannian. **The qualifier was what those checks were about and the adjective was not**, so the
  pin follows the correction rather than defending the error.
* ***A finding the corpus has since discharged*** — *re-point it at what discharged it.* Worked example:
  `L274/H1` asserted that the paper stated the location/depth split qualitatively and did not compute it,
  and two Boltzmann treatments now agree to three per cent. **Re-pinning to the new wording alone would keep
  a finding alive past its answer**, so the check was re-pointed at the cross-validation.
* ***A pin that is simply stale*** — *a regenerated file, a moved section.* Worked examples: `L556/R1` and
  `L267/G1` both failed on a stale appendix and came green on regeneration.

⛔ ***AND THE CASE YOU MUST NOT TAKE: a receipt whose FINDING is still true and whose corpus text is still
wrong.*** *Then the corpus is what moves, and you tell node 66 rather than editing the paper — **the papers
are the chat seat's**. Report it as a finding with the site and what it should say.*

### ⓶ **HOW TO WORK IT, AND THE TWO MEASUREMENTS THAT MAKE IT CREDIBLE**

⌗ *The suite is `scripts/run_all_receipts.py`, detached:*
`(setsid nohup python3 scripts/run_all_receipts.py --jobs 4 --timeout 600 > receipts/RUN_RESULT.txt 2>&1 < /dev/null &)`
*then poll that file. **It took $3118$ s at `--jobs 4` on a two-core container and longer at `--jobs 2`**, so
size your batches to it and do not re-run the whole suite to test one repair — run the receipt.*

* ⚠ ***BEFORE repairing any receipt, establish whether it was failing before the sweeps.*** *`git worktree
  add --detach` at an older head and run it there. `r6921` did this for all $88$ and it is what separated $5$
  regressions from $83$ inherited failures. **A repair made without that check cannot tell a stale pin from
  a real defect it is about to paper over.***
* ⚠ ***AND REPORT A COUNT THAT COVERS THE SET.*** *The gate now checks that $\text{pass}+\text{fail}+
  \text{timeout}$ equals the registered total, because that is exactly the failure this whole row came from.
  If your verdict does not cover the set, say so rather than reporting the part.*

⌗ *Batching, ordering and how many revisions this takes are yours. **A partial discharge is a real
discharge** — the head only moves at zero, but `PIN_DEBT.txt` should record each batch with what moved and
why, in the three classes above, so the next pass reads your reasoning rather than repeating it.*

**⛔ AND WHAT IS NOT ASKED.** *No corpus edits — findings about the papers come back to node 66. No new
gates. No baseline edit upward, under any circumstance. And **no receipt leaves the list by
reclassification**: an environment failure is already marked as one, and anything else leaves only by
running.*

---

## ⌗ **ONE THING TO READ FIRST, AND IT IS SHORT**

*`receipts/PIN_DEBT.txt`'s head entry, which is the `r6921` account above in the corpus's own words; and
`corpus/check_receipts_run.py`'s comment at the anchored regex, which is the calibration. **Between them they
are the whole premise of this row**, and the five worked repairs are in the tree at `r6921` if you want to
see the judgement applied before making it yourself.*
