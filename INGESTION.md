---
name: ingestion
kind: METHOD
current: r2657+c54.207
description: INGESTION — how a 54 batch is folded. 54 cannot write, so there is no merge problem; the risk is that a plausible finding acquires this line's receipt without this line having derived it. Written r2657.
sources: [chat]
---

# INGESTION

> ***Daryl, r2657: "54 can't write and you are folding its updates while doing your own. And I can tell
> 54 whatever we are taking." … "Or you can just leave it your own status updates in the anti collision
> register. On GitHub."***

⇒ ***Three corrections, each deleting work. There is **no write collision**, so no claim mechanism —
`scripts/claim.py` was built and removed inside one revision. And **the anti-collision channel already
exists**: the repo. 54 reads it. So this line writes what it is on, at the bottom of this file, and
nobody relays anything.***

⌗ ***The lesson is the cheaper one: **when a coordination problem appears, check whether the shared
artefact already coordinates.** Two nodes reading the same repo need a LINE, not a protocol.***

---

## ⛔ THE REAL RISK

**54's output arrives as PROSE. This line folds it and writes the receipt.**

⇒⇒ ***So a 54 finding acquires THIS LINE'S receipt — its `✔✔` in `receipts/INDEX.md`, its assertions, its
place in the corpus — without this line having derived it. The receipt says "checked", and what was
checked is that the prose was transcribed faithfully.***

⌗ **AND THE FAILURE IS ASYMMETRIC:** *a wrong 54 finding that this line rejects costs one read. A wrong
54 finding that this line folds becomes indistinguishable from its own work — **and the corpus has no
record that it arrived from elsewhere**.*

---

## ⓵ THE RULE: RE-DERIVE, DO NOT TRANSCRIBE

**A folded finding is worked from the corpus as if 54 had not said it.**

*· if 54 says a passage states X — **find the passage** and quote it with `scripts/quote.py`, do not quote
54's quotation;*
*· if 54 computes a number — **compute it**, by a different route where one exists (r2641: "reproducing a
step is not repeating it — run the cases the original EXCLUDED");*
*· if 54 says a row is answered — **read the row's OBJECT column** and check it against the corpus, which
is r2625's rule and has caught four rows this session.*

⌗ ***The test: could this receipt have been written without 54's message? If not, it is not a receipt, it
is a transcription with a checkmark.***

## ⓶ AND EVERY FOLDED RECEIPT SAYS SO

**`receipts/INDEX.md` gains a provenance note: `folded from 54 batch <n>, re-derived rXXXX`.**
⇒ ***So that a later read can tell which findings this line derived and which it inherited — and if 54's
batch turns out to have a systematic error, the affected receipts are listable rather than archaeological.***

## ⓷ WHAT IS RE-VERDICTED REGARDLESS

*From `THE_HANDOFF`, unchanged: **`rank_open`'s REACH** and **`TABLE_HISTORY`'s REASON** are judgements no
script derives. `LATENT_HISTORY`'s KIND is now gated (`check_kind`, r2656).*

⚠ **AND ONE MORE, SPECIFIC TO A READ-ONLY 54:** ***it cannot run the gates.*** *So every folded finding
must be gate-run here before it counts — a 54 receipt that has never met `lint_assertions` is a draft.*

---

---

# ⛭ THE REGISTER — what this line is on

***Updated at the top of every turn. 54 reads this file; nothing is relayed.***

    r2657   PO-12   the bespoke transfer, step 2 -- unblocks BOTH of PO-10's runs
    r2658   PO-12   six-eighths built; what remains is the ABSOLUTE spectrum (visibility + LOS integral)
    r2659   PO-12   CORRECTED: the instrument carries both. The debt is the BACKGROUND it runs on -- H(a).
    r2660   PO-12   sharpest form: TWO legs joined at the branch point, L1 rate for every expansion-leg observable
    r2661   PO-12   THE JOIN IS COMPUTED: Phi_exp/Phi_coll = 9/10, super-horizon. Sub-horizon modes next.
    r2662   PO-12   caveat removed -- at the branch point EVERY mode is outside. The join is unrestricted.
    r2663   PO-12   SUPER-HORIZON TRANSFER CLOSES: Phi_exp(k) = (9/10) Phi_i(k), scale-invariant.
    r2664   PO-12   NUMBERS: 7.5% low-ell deficit; 0.823 at l_D; 0.459 at 2 l_D. Peaks are the gap.
    r2665   PO-10   gap SIZED (estimate): ~0.813 at the peaks. Deviation is BROAD, not tail-confined.
    r2666   PO-5    coupling CANNOT come from the colour bundle -- flat holonomy gives phases, never force.
    r2667   PO-5    P14 already walls holonomy AND isometry. Real content: is there a THIRD mechanism?
    r2669   PO-11   obstruction is HORIZON-located, not singularity-located -- the ordinary scattering problem
    r2671   PO-6    D3 WITHDRAWN on 54's finding. PO-6 is FREE -- 54 has the live thread there.
    r2672   ---     CLAIMED: the 14 self-falsifying absence-assertions (my defect, r2670). DONE 40/40.
    r2673   ---     TRIAGE done: 41 timeouts, 21 now-pass, 17 real. Two of the 17 were mine, repaired.
    r2674   ---     cc54 CI blocker cleared: LATENT_HISTORY/TABLE_HISTORY classified RECORD. Mine to fix.
    r2675   ---     check_no_stdlib_shadow built+seeded+wired. All four collision classes gated.
    r2676   PO-4    su(2)_L gap characterised: the swap is the WEYL Z_2, so the torus is what is missing.
    r2677   ---     folded c54.210 by re-derivation. PO-6 stays 54s -- their L-543 successor is the calculation.
    r2678   ---     unbanked.py built; excentre found and routed as FOR_54 item 29.
    r2679   ---     unbanked: pushforward -> colour at the CENTRE vs isospin at the WEYL element.
    r2680   ---     monomial was sympys API; unbanked.py now counts prose only. 91 -> 46.
    r2681   ---     certified = meta-vocabulary; found 12 cited receipts that cannot exit non-zero.
    r2682   ---     absence class measured: 4 ended, 3 stand. 2 fixed, 5 reverted, routed item 31.
    r2683   PO-2    three levels audited: (1) grounded (2) PASSED (3) walled on the FORCE not the map.
    r2684   ---     PO-6 halves restated; check_declared_parts built.
    r2685   ---     convergence audit: 4 BOUNDED, 1 UNBOUNDED, 3 gated. Frontier line in the stamp.
    r2686   PO-12   substitution itemised; r_D carries a square root so the ratio does not cancel.
    r2687   PO-12   gap closed by integration; the answer is set by the ONSET.
    r2688   PO-12   the onset is FIXED; the residual is the weight g(R)/x_e.
    r2689   PO-12   +9.4% BRACKETED [7.0, 13.1] from outside the papers instrument. Ordering forced.
    r2690   PO-11   obstruction UNIFORM in lambda -- no high-j corner rescues the tower.
    r2691   ---     folded c54.211/212; BACKLOG emptied, r2677 scope withdrawn. Both errors mine.
    r2692   ---     gates.yml stray do fixed -- MY insertion, misattributed to 54. CI unblocked.
    r2693   PO-7    turnaround is a segment endpoint crossed by rotation, not a singularity.
    r2694   ---     LEDGER 7 -> 1. Three duplicated PO rows, three were the papers own weight-marks.
    r2695   ---     4 stale row heads corrected; routed() taught 5 close-markers; check_row_state built.
    r2696   ---     DARK 2 -> 0 distinct; audit complete. Table 11.
    r2697   ---     unbanked.py paper-side citation blindness fixed; Unruh misattribution corrected.
    r2698   ---     item 60 CLOSED (10/10 verified).
    r2699   ---     item 58 HALVED -- the sixth equivalence was already in print. ROUTED now 0.
    r2700   PO-12   9.4% is an ANGLE ratio; four revisions compared it to a LENGTH ratio. Debt smaller.
    r2701   PO-12   remaining half has NO CONTENT -- at w=0 the potential equation loses k.
    r2702   PO-12   STRUCK. PO-10 UNGATED. Table 8. Frontier 4 BOUNDED, 1 UNBOUNDED, 2 gated.
    r2703   PO-10   CLAIMED: newly ungated and least explored -- what are its two halves, exactly?

## ⓸ WHAT THIS LINE IS TAKING

**`PO-12` — the bespoke transfer, step ②.** *Rank #1: `sec:envelope` supplies step ①, and step ② unblocks
**both** of `PO-10`'s runs (r2646, with the escape route closed at r2647).*

⇒ *Everything else on the ranked queue is free: **`PO-6`** (the measure on the tower, after r2651–r2652),
**`PO-5`** (the coupling), **`PO-4`** ($\su(2)_L$ as a gauging), **`PO-2`**, **`PO-11`**, and the **seven
ledger items**.*

*Written r2657. Stated for reversal.*
