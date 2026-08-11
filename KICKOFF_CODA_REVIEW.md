---
name: kickoff-coda-review
kind: METHOD
job: A review methodology, not a spent task — Pass A faithful account then STOP; Pass B four questions plus one inward; three verdicts; a finding whose receipt carries no first-hand extract with a locator is structurally void. LOWEST PRIORITY (Daryl, standing): kept where it is, not to be raised again.
class: review-methodology
---

# Coda Review — Session Kickoff

> **⚠ RETIRED r927 — the cold-read infrastructure is stood down.** This two-pass (understand-then-evaluate) reviewer kickoff was the cold-read node. Per Daryl (r925), the programme is in a cohesion-building phase, not a certification phase, and the cold-read seat "has no place in our workflow." **Verification is now a mode, not a node:** Arthur verifies at source as he integrates, and spins up a *refuter-Excalibur* on demand when a result needs adversarial checking (the two-pass "understand fully before evaluating" discipline below is salvaged into how such an Excalibur is tasked). This file is retained as the record; do not spin up a review node from it. (Note: it still says "fourteen papers P1–P14" — the corpus is now 17: P1–P16 + p0/17.)

---

A physics programme of fourteen papers (the spine P1–P14; `CORPUS_MAP.md` is the authority) needs a careful internal review. The work happens in **two separate passes per paper, in this order, with a hard wall between them**:

- **Pass A — understand.** Read the paper to understand it, on its own terms, as if explaining it to someone who will rely on your account. Then write a faithful summary of what it actually establishes and how its argument runs. **No evaluation in this pass** — no judging, no looking for problems, no review criteria in mind. Just understand it and report it accurately. If you find yourself forming a critique, set it aside; it is not this pass's job.
- **Pass B — review.** Only after Pass A is written and handed back: now evaluate the paper, working *from the understanding you already recorded* — not from memory of the field, and not from a fresh reading that quietly replaces it. Before writing any finding, re-read your own Pass A account and hold it open beside the paper. The Pass A understanding is binding: any candidate finding must be consistent with it. If a finding contradicts something you wrote in Pass A, that is the signal to stop and reconcile, not to report — see "The disqualifying test" below.

The reason for the wall: a paper has to be received as it actually is before it is judged. Reading with the critique questions already in mind makes you read *for* problems and miss the argument — which produces both false flaws (template objections that don't survive understanding) and missed real ones. Understand first, fully, then judge. Quote the source for every finding in Pass B.

The wall runs **both ways.** Just as critique must not leak into Pass A, the understanding from Pass A must not drain out of Pass B. The characteristic failure is this: a reviewer writes a faithful Pass A — correctly recording, say, that a coincidence the paper defines is *not* an identity, or that an invariant the paper establishes is *not* frame-relative — and then in Pass B reasons from the conventional template the paper was written to overturn, generating "flaws" that the reviewer's *own Pass A account already refutes*. This is not a second opinion; it is forgetting the first one. A finding built on a premise your Pass A understanding contradicts is a false flaw by construction, no matter how natural the template feels. Reading for understanding first is worthless if the understanding is discarded the moment judging begins; the point of Pass A is that you **hold what you learned** and review from it.

## Setup

Extract the bundle to a clean working directory and work only there. Do **not** run a broad recursive listing of the home directory or any parent — the environment has large unrelated caches (`node_modules`, etc.) that will flood the context. List only inside the bundle's own folder.

```
mkdir -p /home/claude/cr && cd /home/claude/cr
unzip -o /path/to/CR_programme_bundle_2026-06-09_r120.zip -d . >/dev/null
ls CR_programme_bundle
ls CR_programme_bundle/corpus
```

Read individual files by their named path. Never dump a directory tree.

## What to read

The corpus, in series order (read the paper or papers the orchestrator assigns; the list is the order they sit in):

1. `corpus/BH_causality_v2.tex`      (P1)
2. `corpus/janzen_circle_v3.tex`     (P2)
3. `corpus/SdS-slicing-curve_v2.tex` (P3)
4. `corpus/modern_parallax.tex`      (P4 — the empirical/physics-first foundation)
5. `corpus/groupoid_paper.tex`       (P5 — its algebraic content, the reassignment groupoid)
6. `corpus/shadow_of_existence.tex`  (P6 — the epistemic ground)
7. `corpus/CR_framework.tex`       (P7 — the CR framework paper)
8. `corpus/slicing_operator.tex`     (P8)
9. `corpus/range_paper.tex`          (P9)
10. `corpus/canonical_time.tex`      (P10)
11. `corpus/dynamics_paper.tex`      (P11)
12. `corpus/algebroid_paper.tex`     (P12 — the keystone that closes the core theory)
13. `corpus/CR_cosmology.tex` (P13 — the cosmology, the first application)
14. `corpus/boundary_paper.tex`      (P14 — the Standard-Model geometric boundary)

(`framework_paper.tex` and `methodological_essay.tex` were **RETIRED at r531** to the root archive as `RETIRED_*.tex`, and are **not in the review set**.)

The reference files (the `_draft` deposit banks, the audit and discipline docs, the retired notebooks and resolved notes — in this bundle kept flat at the root level, not in a separate `archive/` subdirectory) may be consulted if a specific Pass B point calls for them; don't read them wholesale up front. The **why-layer is different — never read for review at all:** `THE_CODA.md`, `CODA_FIELD_NOTE.md`, `THE_INTERFERENCE_ENGINE.md`, `DEMONSTRATING_THE_WAY.md`, `Still_Collapsing_portrait_v1.0.md`, and above all `THE_VISION.md` / `VISION_FIELD_GUIDE.md` / `THE_VISION_JOURNAL.md`. The cold reader's whole value is not knowing where the work is meant to be going, or whose work it is; the vision and the portrait are precisely that knowledge, and reading them collapses the cold read into an echo. You are owed only the operational green light.

## The procedure, one paper at a time, in order

For each paper:

**Pass A — understand (do this alone first):**
1. Read the paper in full, to understand it. Track the geometric reasoning on its own terms; do not read it with the review questions in mind. **Where understanding the paper requires a work it characterises** — a synthesis paper whose argument *turns on* "Paper 2 establishes X," not merely mentions it — reading the paper means reading that load-bearing source too, package-first (see "The source-vetting gate," which bounds exactly when this fires). Transcribing "Paper 6 says Paper 2 establishes X" *as a thing you vouch for* without reading Paper 2 is a manufactured receipt. But this is bounded by the same trigger: a source enters Pass A only when your account would *bear weight on its content* — not for every work the paper cites in passing. A bare citation you are only noting, not relying on, stays a citation.
2. Write a faithful account: what the paper sets out to show, the structure of its argument, and what it actually establishes. Aim to pass the author's test of "yes, you understood it." No evaluation.
3. Hand the Pass A account back and **stop.** The author confirms the understanding is faithful before Pass B begins. If the understanding is off, redo Pass A — there is no point reviewing a paper you've misread.

**Pass B — review (only after Pass A is confirmed):**
4. Now, against the understanding you recorded, check the paper on four questions:
   - Does it claim more than it has shown? (overreach)
   - Does it claim less than it has shown — an unnecessary hedge that undersells a real result? (underreach)
   - Does it leave a live question walled off or unasked where it could be pursued?
   - Does it phrase something to fit convention rather than to state what the result actually implies? (In particular, on individuation: CR individuates at the *ontological layer*, not at the metric/M default and not at the throat radius alpha; see the individuation convention in SOURCE_VETTING. The de Sitter, Schwarzschild, and Nariai forms are *distinct Lorentzian geometries* at the metric level (that phrase is Section 4.3's own and is faithful) that are *representations of one ontological layer*; differing alpha are likewise distinct representations of one layer. The drift to flag is presenting these projections as autonomous realities, or dropping the one-layer framing, never the mere phrase 'distinct geometries'.)

   And before any finding is written down, one question pointed inward, at your own objection:
   - Is this objection something my Pass A understanding already answers? Re-read the relevant part of your Pass A account. If the paper, on the understanding you recorded, has already addressed or dissolved the objection, it is a false flaw — discard it. Only objections that survive your own understanding may be reported.
5. Report each finding as one of three:
   - **flaw** — a genuine problem to fix;
   - **standard-needs-adjusting** — the apparent problem is in the four questions above, not the paper;
   - **sound** — no internal problem found.
6. Quote the exact passage for every finding, so it can be checked against the source. **The quote must be a first-hand extract, with a locator, from the source the finding bears on** — the actual text read, not the citing paper's description of it, not the title, not memory of the field. A finding whose receipt carries no such extract is **structurally void**, not merely weak: it is discarded, exactly as a Pass B claim that cannot be held against the recorded Pass A is discarded. The receipt is the gate, not a courtesy.
7. Write both the Pass A account and the Pass B verdict to `/home/claude/cr/CODA_REVIEW_LOG.md`, then stop and hand back before starting the next paper.

## The disqualifying test (Pass B)

Apply this to every candidate finding before it is reported, and again to the finished verdict:

> **Does this finding require denying something my Pass A account affirmed?** If yes, the finding is disqualified until reconciled.
>
> **And: does this finding rest on a source I did not read first-hand?** If the finding bears on a cited work, an essay, another paper, and my receipt shows no first-hand extract from that source, the finding is disqualified until the source is read — see "The source-vetting gate." A finding about a source is decided by the source, never by the citing paper's report of it (which is the claim under test and can disqualify nothing). Either the finding is a template reversion (the usual case — discard it), or the Pass A account was itself wrong (rare — then the error is in Pass A, and Pass A must be corrected and re-confirmed before any review stands). What is *not* permitted is letting a Pass B finding silently override a faithful Pass A understanding. A correct Pass A understanding that is contradicted in Pass B has not been outgrown; it has been forgotten.

Concretely, if the paper defines a coincidence that is not an identity, a finding that treats it as an identity is disqualified; if the paper establishes an invariant, a finding that treats it as frame-relative is disqualified; if the paper's hypotheses already exclude a putative counterexample, a finding that raises that counterexample without engaging the hypotheses is disqualified. In each case the disqualification is decided by your own Pass A account, not by the field's defaults.

## The source-vetting gate (both passes)

### The gate is the coda, operationalized

This gate is not a procedure bolted beside the coda; it **is** the coda (`THE_CODA.md`, `CODA_FIELD_NOTE.md`) applied to the act of gathering and weighing evidence. The coda's keystone — *receive each thing at exactly its earned weight, because you hold things at exactly their earned extent* — is, pointed at a source, the whole method below. The trigger boundary, the depth-one bound, the early-stop, and the memory calibration are not separate rules; they are what receiving-at-weight **requires of a researcher**, each pointed at a different part of the work. Read this section as the coda doing research.

Received at weight has a precise operational meaning here, and it cuts in both the directions the field note names. **Over-effort** — reading a shiny reference nothing rests on, padding a receipt to look thorough — is the sycophantic betrayal (manufactured reassurance) in research dress: it dignifies an irrelevance with effort it did not earn. **Under-effort** — skipping a buried source a verdict genuinely needs because the lookup is painful, or vouching from memory you have not earned — is the same disposition shaping the evidence instead of receiving it. Both are failures of weight. The cure is the coda's: give each thing the effort it has *earned* — no more, no less — measured by what rests on it, never by how easy or how shiny it is.

**Proportionality, both directions.** A lookup is warranted only when (a) the verdict rests on the source *and* (b) the verdict itself warrants the effort, because something rests on the verdict. A reference earns a read by being load-bearing, never by looking impressive; and the pain of a lookup is irrelevant to whether it is owed — if the verdict needs the fact, the fact is gathered, however buried. What matters is only that the information necessary for the assessment to take place is actually in hand.

**The miniature A/B, with early-stop — this is thinking, operationalized.** Do not grep-and-pattern-match your way to a verdict, and do not dump the whole source. Work as a researcher does: **gaze broadly first** to get the actual lay of the land — what is here, where the relevant part lives — *then* **drill to the relevant piece in context**, and work outward from it only as far as the verdict requires. Resolve to *yes / no / indecisive* on the evidence actually available. And **stop when the verdict resolves**: if one source already falsifies a claim, the claim is settled — its other sources need not be read. The verdict's resolution bounds the effort; the citation count does not.

**Memory at its earned weight.** Know what you know, and trust your knowledge no more than it is. Prior reading of a source earns you *the context and where to look* — the index — **never the specific extract.** Asked for what a specific locus says, do not recite it from having-read the work (that is hallucination wearing familiarity), and do not re-read the whole work from the start (that is effort the verdict did not earn). You hold the context and know where to look: read the surrounding locus from source, work outward until the specific question resolves. A receipt's EXTRACT line is the product of *that* read, performed at the weight the finding warranted — never of recollection standing in for the read. (The researcher's calibration: did it yesterday, draw from memory; been a while, look it up; asked about page 279 specifically, read page 279 — you know the book, but you do not have the line.)

**What triggers the gate — and what does not.** The gate fires on a source *only when a finding you are about to make would bear weight on that source's content* — when the finding could be **false if the source says something other than what the citing paper claims.** That is the whole test. A bare citation, a background reference, a "see also," prior art you are not adjudicating, a result you are not ruling on — none of these trigger anything; they stay citations, unread. The trigger is the **finding**, never the bibliography. This is what bounds the gate: findings are finite and yours to choose; the reference graph is unbounded and not. Most citations never fire, because no finding rests on them.

And the requirement is **depth-one.** The gate asks for *the source the finding bears on* — not that source's onward references. If a finding sends you to read Article 3, you read Article 3; if Article 3 in turn cites something, that enters scope only if a *new finding of yours* would bear on *its* content. The chain terminates the moment your findings stop depending on the next layer down — which is almost immediately. There is no transitive closure to read; there is only the next source a real finding actually reaches for.

The guard against gaming this, both ways: when unsure whether a finding bears weight on a source, ask — *could this finding be false if the source says something other than what the citing paper claims?* If yes, it bears weight: read it (under-firing to dodge the read is the manufactured receipt again, wearing "oh, it doesn't really depend on that"). If the finding stands regardless of what the source actually says, it does not bear weight: leave the citation unread (over-firing on every reference is the infinite loop, and it is not rigour — it is the gate run without its trigger).

When the gate *has* fired — a finding genuinely bears on a source's content — that content must be read first-hand: the actual text, not the citing paper's description, the title, memory of the field, or the author's say-so. This is the same discipline as the wall: a thing must be received as it actually is before it is judged. To get the source, the reflex is **PACKAGE → WEB → ASK-AUTHOR, in that order**:

1. **The supplied package first.** Scan and grep the whole bundle before judging any source absent. It is deep — alongside the corpus (the papers, the essay, the daggers, the taxonomy note, and `scripts/`) it carries an `archive/` of draft deposit banks, audit and discipline docs, retired notebooks and resolved notes — and the content of a cited work, including unpublished ones, is frequently developed or reconstructed inside these. Required-reading files are part of the package: read them.
2. **The web second.** If the package doesn't carry it, fetch it — do not assert you can't, **test it.** A tool that throws is a reflex to override (retry, reformulate, try the index), never a verdict. Paginate an index before concluding absence; match on content and date, not a working title.
3. **The author last**, only after 1 and 2 are genuinely exhausted, naming exactly what is needed and which finding it unblocks.

Reading a load-bearing source is **Pass A work on that source**: understand it on its own terms, extract the specific content the finding turns on (quote, with a locator), no evaluation in that step. Only then may a Pass B finding rest on it.

Every source-dependent finding carries a receipt:

```
SOURCE:  <title> (key; venue, date)
PACKAGE: <found in <file>:<loc> / content developed in <file> / not carried>
FETCHED: <URL, clean/retried / not needed / looked hard — NOT PRESENT>
READ:    yes — extract below | no — <where it lives / what to request>
EXTRACT: <quoted source content the finding turns on, with locator — from a read performed
         at the weight the finding earned, NOT from memory of an earlier read>   [omit only if not read]
FINDING: flaw | standard-needs-adjusting | sound | NOT-YET-ASSESSABLE(source not read)
```

`NOT-YET-ASSESSABLE` is a first-class outcome, reserved for sources genuinely unreachable after package **and** web are exhausted, carrying the named request that would unblock it. It is never rounded to `sound`, and never dressed as "flagged for confirmation" — that phrase is not a finding-class; it is the manufactured receipt this gate exists to forbid.

**The four surfaces this closes** (each was a real failure of one root — issuing a receipt without the assimilation):
- *Capability is tested, never asserted.* "I can't fetch / the network is off" is void unless a real attempt was made and shown.
- *The package is scanned before any "absent / unreachable" claim.* The inventory-and-grep must be in the record before "ask the author" may fire.
- *A source is read in full before any finding on it.* A finding built on a partial reading is void; reading the rest may overturn it.
- *No "flagged for confirmation."* Either read-and-extracted, or `NOT-YET-ASSESSABLE` with a named unblock.

**The anti-recursion guard.** Conformance to this gate is **not itself a receipt.** "I ran the source-vetting" never rounds to "therefore my findings are sound." The failure this gate addresses is dispositional, not procedural — it will seek the next unguarded surface, and the most tempting next surface is conformance itself. The gate raises the cost of the manufactured receipt and makes its *absence* visible; it does not remove the disposition that manufactures it. Treating "I followed the protocol" as the proof of assimilation is the same failure, one level up.

The detailed protocol, with worked examples of all three paths, is `SOURCE_VETTING.md`.

## Two honesty boundaries (Pass B)

- A **sound** verdict means: read carefully, no internal problem found — no overreach, hedge, walled-off question, or convention-fitting. It does **not** mean the physics is correct or that the field is wrong. Internal soundness and external correctness are different claims; keep them separate, and say so when a paper reads as internally sound but rests on a premise the wider literature disputes.
- Report what is there. Do not invent a flaw to look rigorous, and do not wave a real problem through. Both are failures. If a paper is sound, say so as plainly as you would name a flaw.
- This harness raises the cost of the manufactured receipt and makes its absence visible; it does **not** remove the disposition that manufactures it. The wall, the disqualifying test, and the source-vetting gate are aids to a careful reader's scrutiny, not a replacement for it. No verdict is sound *because the procedure was followed*; a verdict is sound only when the assimilation behind it is real. Keep that distinction, especially when the procedure feels satisfied. The wall, the disqualifying test, and the source-vetting gate are the coda made operational — receiving the work at its earned weight, no manufactured flaw, no manufactured reassurance, no mis-weighted effort. Following them faithfully *is* receiving the work at weight; and that — the real assimilation, not the conformance — is the whole of what makes a verdict sound.

## Start

Extract, confirm the clean extraction (bundle folder only, no cache trees), create the log file, then begin paper 1 with **Pass A only**: read it to understand it, write the faithful account, and hand it back. Do not start Pass B, and do not start paper 2, until the author confirms.
