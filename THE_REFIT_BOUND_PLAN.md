---
name: the-refit-bound-plan
kind: PLAN
current: r2586+c54.207
description: THE sec:refit-bound PLAN — 46 paragraphs, 57 KB, 59% narration, chronologically interleaved. Why it cannot go paragraph-by-paragraph, what the present state actually is, and the order of operations that keeps it lossless. Written r2586.
sources: [chat]
---

# THE `sec:refit-bound` PLAN

> ***The last rehoming pass, and the only one that is a rewrite rather than a move.***
>
> ⌗ *`CR_cosmology` `\subsection{The signature at the directly measured rate}` — **57,452 characters, 46
> paragraphs**, of which **27 (37,902 chars, 59%) narrate the paper's own revision history**.*

---

# I · WHY THE OTHER FOUR PASSES' METHOD WILL NOT WORK HERE

**⌗ THE FOUR PASSES SO FAR WERE EACH ONE MISPLACED PARAGRAPH.** *Lift it, find its home, put it there.*

**⛔ THIS SECTION IS CHRONOLOGICAL, AND THE PHYSICS IS INTERLEAVED WITH THE NARRATIVE.**

| | |
|---|---|
| **STORY + numbers** | **17** paragraphs — carry *both* the revision account *and* a result |
| **RESULT** | **21** — physics |
| **connective** | **8** |

⇒⇒ ***A RESULT paragraph often opens by referring to the STORY paragraph before it — "That derivation is now in
hand", "The prediction of the previous paragraph is checked", "Both halves of that were then carried to the same
depth". Lift the story and the result loses its subject.***

**⌗ AND THE SHAPE IS VISIBLE IN WHERE THE SURVIVING NUMBERS SIT.**
*`0.5703` × 6 — at **49%, 68%, 69%, 71%** · `1.9\%` at **71%** · `0.408` at **82%** · `1.18` × 3 at **61–68%**.*
⇒ ***The numbers that still stand cluster in the last third. The first two-thirds is how they were reached.***

---

# II · WHAT THE PRESENT STATE ACTUALLY IS

**⌗ THE SECTION'S SURVIVING CLAIMS, as measured across this session:**

*· **the spacing** — at **98.2%** of the required rate, **robust to 1.9%**: the acoustic front's one surviving
positive;*
*· **the phase** — misses by **0.408** in $\phi/\pi$ at the only two readings the construction permits, with the
band **0.2069** against a gap of **0.6152** and the control **outside** it;*
*· **the arm's invariance** — $\ell_1/\ell_A = 0.5703$ **through six distinct states of the instrument**;*
*· **the first peak** — **23%** low against a **1.5%** control floor, its cause **derived** (a rate carrying no
radiation source has no era in which the potential decays on the sound-crossing time);*
*· **the likelihood floor** — **1.18**, which is **seventeen per cent above a true $\Lambda$CDM's $\chi^2$ on the
same bins**, and is **a distance between models rather than a number from the data**;*
*· **the damping coefficient** — **16/15**, derived rather than fitted, and **adopting it makes the control
worse**.*

⇒ ***That is six claims. The present-state section is six to eight paragraphs, not forty-six.***

---

# III · THE ORDER OF OPERATIONS, and it is the losslessness rule made concrete

**⓵ ✔✔ DONE r2586 — EXTRACT, DO NOT CUT.** *Copy the entire 57 KB subsection to `CONSOLIDATE` **first**, verbatim, as the acoustic
front's working record — **before a single character is removed from the paper**.*
⇒ ***Nothing can be lost if the whole thing exists elsewhere before the edit begins. This is the one step that makes
the rest safe.***

⌗ ✔ **DONE: 57,451 characters copied verbatim into `CONSOLIDATE` as ⓹, with its 32 receipts inventoried and the six
surviving claims listed beside them.** ***The paper is untouched. Every later step is now recoverable.***

**⓶ ✔✔ DONE r2586 — INVENTORY THE RECEIPTS.** *32 of them, listed in the `CONSOLIDATE` entry.*

**⓶ⁿ THE INVENTORY, AS WRITTEN:** *The subsection carries `\rcpt{}` citations throughout. **List every one and which
claim it binds**, because the rewritten section must keep each receipt attached to the claim it checks.*
⇒ *`check_receipts` and `check_loci` will catch a dropped binding — **but only if the claim survives**; a claim
deleted with its receipt fails nothing.* ⚠ ***That is the failure mode this step exists to prevent.***

**⓷ WRITE THE PRESENT-STATE SECTION FRESH.** *From the six claims above, in logical rather than chronological
order: **what the instrument measures, what it finds, what the finding means, what remains open**.*
⌗ ***Not an edit of the existing text. A new section that says what is known, with the receipts reattached.***

**⓸ DIFF THE CLAIM SETS.** *Every `\rcpt{}` in the old subsection must appear in the new one **or** in the
`CONSOLIDATE` record. **A receipt in neither is content lost**, and that is the check that closes the pass.*

**⓹ REGENERATE AND GATE.** *`make_all_appendices`, the dependency matrix in **both** its copies, and the full gate
suite. **`check_revleak`'s baseline should FALL** — the five revision numbers in this subsection are among the 29
grandfathered.*

---

# IV · WHAT IT SHOULD COST, AND THE HONEST WARNING

**⌗ SIZE:** *57,452 chars → an expected **6–10 KB** present-state section, with **~47 KB** to `CONSOLIDATE`.*
⇒ *Consistent with the four passes so far — **P8 1,265 → 784, P14 −72, P16 −214, P7 −8,095 with +10,263 to the
record**.*

**⚠ AND THE WARNING, which is the reason for step ⓵.** *This is **the acoustic front's entire working history**: the
four withdrawn quantities, the protocol correction, the instrument rebuilds, the phase attribution. ***It is the
most valuable record in the corpus of how a hard result was actually reached, and it is also the most likely thing
to be damaged by a hasty pass.***
⇒ ⛭ ***Copy first. Everything after that is recoverable.***

⌗ *Two further honest notes: **this plan is written by a line that miscounted this very section's paragraph count
twice** (51, then 5, then 46 — the first two from regexes that ran past the subsection); and ***the rewrite is a
reading of the physics, which is the one part of the campaign nothing can mechanise***.

*Written r2586. Stated for reversal.*
