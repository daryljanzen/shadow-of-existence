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

## ✔✔ PASS 5 DONE — `CR_framework` (P7)'s story-move, r2585. **The paper had already done half the separation itself.**

**⌗ P7 STATED THE PRINCIPLE BEFORE WE DID.** *"a frontier list is a map of where the work is, and **an item that has
been answered is no longer part of that map**" — and: **"The detail belongs to §`sec:lift-initial-rate` and is not
repeated; what follows is the account as the frontier item carried it, kept because the item's own framing … is the
record of how the question closed."***
⇒ ***It named its own content as the RECORD. So the account moved to `CONSOLIDATE` — intact, 8,638 characters.***

**⚠ AND ONE THING WAS REHOMED UPSTREAM FIRST, because a story-move is only safe after the physics in it is found.**
*Checked: **`0.78899` and the Euclidean null were already upstream**; the clause that **the lap is the portion of
history the $dS_4$ background represents on a single minimal $S^3$ at the throat** — and is therefore ***the region
where the null rulings and the synchronous reading are not available as they are on the horns*** — was **not**.
Moved into `sec:lift-initial-rate`.*

⌗ **P7's below-the-list content: 11,344 → 3,264 characters.** *Net **−8,095** from the paper, **+10,263** to
`CONSOLIDATE` (the account plus its framing).* ⇒ ***Nothing lost, and the growth is where the record belongs.***

⌗ *And the move tripped `check_depmatrix` — P7's citation counts fell by two — **in the `\textbf`-wrapped row that
c54.206 reported its own patch script skipping**. Both copies updated by hand.*

---

## ⛔⛔⛭ PASS 4 SCOPED, NOT DONE — `CR_cosmology`, and it is a different animal

**⌗ WHAT THE FIRST THREE PASSES WERE:** *one misplaced paragraph each, rehomed in a turn.*
**⌗ WHAT THIS IS:** *`sec:refit-bound` — ***57,452 characters, 46 paragraphs, and 59% of it (37,902 chars) narrates
the paper's own revision history***.*

*· "This was reported here as a transfer argument contradicted by a direct computation, and **at
r2376+c54.164** that…"*
*· "That missing propagation **is built at r2376+c54.168**…"*
*· "That last sentence was measured against a target that could not carry it, and **we correct our own protocol
here**"*
*· "**We wrote at this point** that the acoustic statement had reached its final form … and that is **the third
thing in this section we now withdraw**"*

⇒⇒ ***A physics section written as a lab notebook — and it is the most valuable record in the corpus of how a hard
result was actually reached, which is exactly why it must go to `CONSOLIDATE` intact rather than be cut.***

**⚠ NOT ATTEMPTED IN THIS TURN, DELIBERATELY.** *Losslessness is the campaign's hard rule, and **38 KB of
interleaved narrative and physics cannot be split safely in one pass**. ⇒ ***This needs its own planned campaign:
paragraph by paragraph, each to CONSOLIDATE or to the present-state rewrite, with the receipts re-resolving after
each move.***

**✔ WHAT WAS DONE INSTEAD — the one part that IS mechanical.** *Measured corpus-wide: ***29 internal revision
references in published paper bodies across thirteen papers*** (`r2376+c54.9` alone appears in nine).*
⇒ *`corpus/check_revleak.py`, **wired and seeded**, **grandfathered at 29** on r2557's rule. ***A reference added
after r2584 fails, so the leak stops growing while the campaign drains it — and each pass removes baseline entries
as it goes.***
⌗ ***Deciding where a paragraph belongs is a reading. Deciding that `r2376+c54.164` does not belong in a physics
paper is not.***

---

## ✔✔ PASS 3 DONE — `cosmogenesis` (P16), r2583. **And the discriminator's limits are now known from both sides.**

**⌗ THE PARAGRAPH.** *The multi-abundance network result, written as a **debt discharged**: "was the one computation
**not yet run**… **It has now been run**… **That debt is therefore paid**, and the title's ``produces`` **now stands
earned** … rather than **marked open**."*
⇒ ***The physics was true and stated. It was framed as the settling of an account rather than as a result.***
⇒ *Rewritten in the present. **Net −214 characters**, and the removed text was **the accounting**, not the physics.*

**⛔ AND THE DISCRIMINATOR FAILED IN BOTH DIRECTIONS, WHICH IS WORTH MORE THAN EITHER PASS.**
*· **Too loose**: `boundary_paper` flagged on **"where the count no longer bites"** — ***ordinary physics prose
about where a count applies***, nothing to do with the paper's past. **P13 is clean.***
*· **Too tight**: a self-referential-only test scoped the campaign to five paragraphs in one paper — ***and dropped
this one***, whose tell is "was the one computation not yet run".*
⇒⇒ ***No keyword test is right. Use the LOOSE test as triage and READ each hit — which is what the campaign plan
said before I drifted into trying to auto-scope it.***

---

## ✔✔ PASS 2 DONE — `matter_sector` (P14), r2582. **A third $D=4$ argument was filed under "scope".**

*The paragraph — "What the flavour skeleton fixes about the dimension" — is a **derivation**: $2M=r_0^{D-3}-r_0^{D-1}$
in $D$ dimensions, with the **collapse** and the **parity** conditions between them selecting $D=4$.*
⇒ ⛭ ***A THIRD independent argument that $D=4$ is picked out*** *— beside `L-240`'s Lovelock/Rule 2 and `L-533`'s
emptying — **sitting in "Scope, and consistency with the boundary".***
⇒ *Rehomed to **`\section{Three walls: the count}`**, after the boxed $=3$, because **the constraint runs from the
count to the dimension**.*

⌗ **Net −72 characters.** *The paragraph's own framing — "it is worth asking what the sector would deliver at other
dimensions… it runs the other way" — was **redundant once it sat where the constraint is stated**.*
⇒ ***Daryl's signal, confirmed twice: content in the wrong place needs prose to explain why it is there, and that
prose is what disappears.***

---

## ✔✔ PASS 1 DONE — `slicing_operator` (P8), r2581. **The method works and here is what it looks like.**

**⌗ THE PARAGRAPH:** *"The emergence of the bend" — 3,061 characters in `\section{Scope and open problems}`,
carrying **"the corpus has since substantially worked it"**.*

**⓵ WHAT WENT UPSTREAM.** *Buried in it: **"for a general spatial leaf the energy density is the leaf's
intrinsic-curvature departure from the de Sitter substrate, $16\pi\rho={}^{3}R+K^{2}-K_{ij}K^{ij}-2\Lambda$, the
Hamiltonian constraint, of which $\rho=m'/4\pi r^{2}$ is the spherical instance."***
⇒ ⛭ ***That is the GENERAL FORM of this paper's own central identity — `prop:bend` — and it was filed under "what
is open." Rehomed beside the proposition as `eq:bend-general`, with a paragraph saying the reading is not an
artefact of the symmetry.***

**⓶ WHAT WENT TO `CONSOLIDATE`.** *The account of what was known when, and where each piece came from — opened as
**THE REHOMING RECORD**, which is where every pass's story goes from here.*

**⓷ WHAT STAYED, AND IT IS NARROWER.** ⇒ ***Not "the emergence of the bend" but the matter content's own generative
law where the construction does not supply one — a dynamics for the CURVE, as against the ordinary leaf evolution
that carries it.***

⌗ **3,061 → 1,796 characters, and the paper GREW by 784** *(the rehomed identity).* ***Nothing lost: the identity
moved, the results kept their citations, the story is recorded.*** *`check_compile` green.*

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
| ~~**`cosmogenesis`**~~ | 5 | ✔ **0** | ***DONE r2583*** |
| ~~**`boundary_paper`**~~ | 12 | ✔ **clean** | ***FALSE POSITIVE — "no longer bites" is physics prose about where a COUNT applies, not the paper's past*** |
| ~~**`matter_sector`**~~ | 10 | ✔ **0** | ***DONE r2582*** |
| ~~**`slicing_operator`**~~ | 5 | ✔ **0** | ***DONE r2581*** |
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
