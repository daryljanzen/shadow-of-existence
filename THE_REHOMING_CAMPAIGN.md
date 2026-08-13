---
name: the-rehoming-campaign
kind: PLAN
current: r2580+c54.207
description: THE REHOMING CAMPAIGN — 114 paragraphs across 13 frontier sections, to be rehomed upstream into the physics or into CONSOLIDATE, so each paper reads as a map of the present state rather than an accident of when it was written. Written r2580.
sources: [chat]
---

# THE REHOMING CAMPAIGN

> ## ⛭⛭⛭ THE PRINCIPLE, IN DARYL'S WORDS AND THEN IN THE FORM THAT MAKES IT ACTIONABLE
>
> *"A paper that WAS properly organised, saying all it can say and ending with a frontier section,
> should be edited by **pulling every unknown to its proper place UPSTREAM of the frontier section**.
> The horizon moved further back, and the paper as a map of everything known with a pointer to the
> horizon should have become properly informed about its previous frontier stuff that became part of
> the rest."*
>
> ⇒ ***A PAPER IS A MAP OF THE PRESENT STATE. A FRONTIER SECTION IS A POINTER TO THE HORIZON. When the
> horizon moves back, the newly-known content is REHOMED UPSTREAM into the physics — not annotated in
> place.***
>
> ⇒⇒ ***AND THE STORY OF HOW IT MOVED BELONGS IN `CONSOLIDATE`, NOT IN THE PAPER.*** *That is the record
> of what was known and not known at different junctures. **A paper that carries it is carrying a
> changelog.***

## ⛔ WHAT THIS LINE HAS BEEN DOING WRONG, NAMED

*Revising sentences **in place**, so a frontier entry changes from "this is open" to "this was open and
we worked it out and now it is known."*
⇒ ⛔ ***That is neither destination. It leaves settled physics in a section headed "what is not done",
and it puts the STORY in the paper.***
⌗ *r2579 measured the result: **P7's frontier section is 11% of its body and 35% of that sits below the
list** — roughly eleven thousand characters of settled physics under a heading that says it is not done.*

**⇒ THE END STATE, stated so it can be checked:** ***"this is what we currently know about the whole
thing" — and a smaller, diminished section: "this is what we still don't know."***

---

# 0 · ⛭⛭⛭ THE SCOPE IS FIVE PAPERS AND THIRTEEN PARAGRAPHS, NOT 114 — measured r2580

**⌗ THE FIRST TEST CASE FOUND THE DISCRIMINATOR.** *`algebroid_paper` has **one** frontier paragraph, so the whole
pass is visible. Read: its three items are **`Computed:`**, **"the handoff, not an open closure on this sector"**,
and **"The sector itself:"**.*
⇒ ***All three are SCOPE-DELIMITATION — "this paper covers X and not Y" — which is exactly what a scope section is
for. P12 is CLEAN.***

**⇒⇒ AND THAT GIVES THE DISCRIMINATOR: TIMELESS vs TEMPORAL.**
*· ***Scope-delimitation is timeless***: "the closure is the finite, symmetry-reducible reduction."*
*· ***A resolved frontier is temporal***: "has since", "no longer", "was open", "we wrote", "moved below", "opened
at".*
⌗ ***A paper is a map of the present state, so a TENSE that refers to the paper's own past is the defect's
signature.*** *Nothing else needs judging.*

**⌗ APPLIED TO ALL THIRTEEN:**

| paper | frontier paras | temporal | |
|---|---|---|---|
| **`CR_cosmology`** | 51 | **8** | ⛔ |
| **`cosmogenesis`** | 5 | **2** | ⛔ |
| **`boundary_paper`** | 12 | **1** | ⛔ |
| **`matter_sector`** | 10 | **1** | ⛔ |
| **`slicing_operator`** | 5 | **1** | ⛔ |
| `CR_framework` (P7) · `SdS-slicing-curve` · `algebroid` · `dynamics` · `geometric_core` · `groupoid` · `janzen_circle` · `range_paper` | 41 | **0** | ✔ clean |

⇒⇒ ***FIVE PAPERS, THIRTEEN PARAGRAPHS. The campaign is an afternoon per paper, not a rewrite of the corpus.***

**⚠ AND P7 IS CLEAN, WHICH CORRECTS r2579.** *Its frontier section is 11% of its body and 35% of that sits below the
list —* ***but that below-the-list content is prose ABOUT the list ("it opened at seven and stands at four"), not
misfiled physics.*** ⇒ ***That prose IS the story, and the story belongs in `CONSOLIDATE` — so P7's item is a MOVE,
not a rehoming.*** *r2579 measured the size correctly and inferred the defect wrongly.*

---

# I · THE SCOPE AS FIRST MEASURED — kept, because the correction is the finding

| | |
|---|---|
| frontier/open/scope sections | **13 papers** |
| total | ***191,530 characters*** |
| paragraphs of 120+ chars | ***114*** |

**⌗ AND A FIRST-PASS TRIAGE OF THE 114** *(keyword classification — **a triage, not a verdict**; this line
has had three general prose classifiers fail on precision this session, at r2553, r2554 and r2556):*

| bucket | count | destination |
|---|---|---|
| **OPEN** | 13 | ***stays*** — this is what a frontier section is for |
| **RESOLVED** | 24 | ***rehome UPSTREAM*** into the physics it belongs to |
| **MIXED** | 27 | ⛭ ***SPLIT*** — states an open edge AND a resolution in one paragraph, which is exactly the in-place revision that has to come apart |
| **STORY** | 8 | ***move to `CONSOLIDATE`*** — what was known when |
| **NEITHER** | 42 | ***needs reading*** — the classifier does not reach them |

⇒ ***So ~51 paragraphs likely carry settled content in a frontier section, 42 need a read, 13 stay, and 8
are story.***

---

# II · THE THREE DESTINATIONS, AND THE TEST FOR EACH

**⓵ UPSTREAM — into the physics.** *The test: **does this paragraph state something the corpus now
KNOWS?*** ⇒ *Then it belongs where that knowledge lives — in the section that develops it — **written as
what is known**, with no trace of its having once been a frontier.*
⌗ ***And the destination is findable: the content almost always already appears in the body*** *(P7's
`causal reassignment` **21 times**). **So rehoming is usually MERGING a frontier paragraph into an
existing passage, not creating a new one** — which is why it can be lossless.*

**⓶ `CONSOLIDATE` — the story.** *The test: **does this paragraph say what was known WHEN?*** ⇒ *"We wrote
at this point that…", "the list opened at seven and stands at four", "this was withdrawn at…".* ***That
is the programme's record of its own working, and it is valuable — in the document built for it.***

**⓷ STAYS — the frontier.** *The test: **is this still not known?*** ⇒ *Six of the fourteen outstanding
items are real physics and their paragraphs belong exactly where they are.*

⚠ **THE LOSSLESSNESS CONSTRAINT, which is the campaign's hard rule.** ***Nothing is deleted. Every
paragraph goes to one of the three destinations, and a paragraph that cannot be assigned STAYS until it
can be.*** *A gate should check the total content is conserved across a rehoming commit.*

---

# III · THE ORDER OF WORK

**⌗ BY SIZE, SMALLEST FIRST — because the method has to be proven on a paper that can be held whole.**

| # | paper | paragraphs | why here |
|---|---|---|---|
| **1** | `algebroid_paper` | **1** | ***the method's test case*** — one paragraph, one decision, and the whole pass is visible |
| **2** | `geometric_core_paper` | 1 | p0, and the highest-read paper in the corpus |
| **3** | `dynamics_paper` | 2 | |
| **4** | `range_paper` · `SdS-slicing-curve` | 4 each | |
| **5** | `groupoid` · `slicing_operator` · `cosmogenesis` | 5 each | |
| **6** | `janzen_circle` | 6 | |
| **7** | `CR_framework` (P7) | 8 | ***where the defect was found, and where its 35% below-the-list sits*** |
| **8** | `matter_sector` | 10 | |
| **9** | `boundary_paper` | 12 | **33% of its body** |
| **10** | `CR_cosmology` | ***51*** | ***last, and it is nearly half the campaign on its own*** |

⇒ ***Ten passes. Nine of them are small. `CR_cosmology` is a campaign inside the campaign and should be
planned again when the other nine are done.***

---

# IV · WHAT WOULD MAKE IT STICK

**⓵ A GATE ON PLACEMENT, not on prose.** *The rejected classifiers all tried to judge meaning. **This one
does not need to**: after a paper is passed, its frontier section should contain **no paragraph whose
content also appears upstream in the same paper**.* ⇒ ***That is a duplication check, and duplication is
mechanical.***

**⓶ A CONSERVATION CHECK.** *Total non-comment characters across the paper plus `CONSOLIDATE` should not
FALL across a rehoming commit.* ⇒ ***It can rise, since merging often needs connective prose. Losing
content is the failure to prevent.***

**⓷ AND THE ONE THING THAT CANNOT BE MECHANISED:** ***deciding where upstream a paragraph belongs.*** *That
is a reading of the physics, and it is the campaign's actual work. **Everything else is bookkeeping.***

---

# V · THE HONEST CAVEATS

⚠ *· **The triage is keyword-based and 42 of 114 fall outside it.** Treat the bucket counts as an
ordering, not a plan — ***the reading is the work and the triage only says where to start.***
*· **"Poor writing julienne along the way"** — Daryl's phrase, and the campaign should fix prose where it
finds it, but ***rehoming is the objective and rewriting is the side-effect; a pass that becomes a style
edit has lost the thread.***
*· **This will change every paper's shape**, and every change must survive `check_compile` and the
receipt gates. ***A paper whose receipts stop resolving after a rehoming pass has lost content the
conservation check did not see.***

*Written r2580. Stated for reversal.*
