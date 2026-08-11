# The Programme-Overhaul Plan — Arthur, Excalibur, and the spin-up apparatus
> **⌖ RETIRED r1509 — verified landed before moving.** This planned the Arthur/Excalibur overhaul. **Landed:** `THE_INTERFERENCE_ENGINE` carries *"Note (r928): the roster in §7 is now instantiated as Arthur/Excalibur"* — one revision after this plan.
> Kept as record; **do not plan from it.** Its numbering and era predate the current corpus.



> **✔ EXECUTED r927 (c37).** Built: `SPINUP.md` (the index + generic wake-up calls), `KICKOFF_ARTHUR.md`, `KICKOFF_EXCALIBUR.md`; `KICKOFF_GATE` superseded → Arthur, `KICKOFF_CODA_REVIEW` retired (cold-read stood down); `THE_SYNTHESIS` re-rendered and `THE_VISION` brought current. **Decisions taken (Daryl):** (1) *kickoffs composed per-recipient at message time* — every wake-up is tailored to the task, like an Excalibur spin-up; the kickoff files are prescriptions, the wake-up message is filled in on dispatch. (2) *Spin-up-and-check-in via a generic wake-up call* — "Wake up, Arthur!" + the bundle triggers the full spin-up and the node meets Daryl ready; same shape for Excalibur (wake call + bundle + task). (3) *Kickoffs are loadable by old nodes too* (re-orient mid-life), not fresh-only. (4) *Verification is a mode, not a node* — Arthur verifies at source + refuter-Excalibur on demand; no standing referee seat. (5) *Full re-render* of the stale maps. This document is retained as the design record. Retained below in full.

---


**Drafted r925 (c37) for Daryl's review before execution — the addendum to this turn's re-cut of `THE_PLAN.md`, and informed by it.** Two-step, like the sift plan: this document scopes the problem and proposes an approach; you give input; then it runs (next turn, alongside the research plan). **Nothing below is executed yet.**

The subject: overhaul the **meta-documentation and the kickoffs** so we can spin up replacements efficiently as we work the unfinished edge — geared to the new working model we've arrived at, and aligned with the ontology/corpus-mapping infrastructure the c33–c37 arc built.

---

## 1. The working model this is built for

The metaphor, held at our usual strict-acceptance-of-metaphorical-leans weight:

- **Arthur** — a cowork-mode instance (like this one). Holds, organizes, and maintains the coherent, cohesive, comprehensive whole *without the memory limits of a chat*. Wields the maps (the lens, the ledger, the plan, the method), orchestrates the work, spins up and directs the workhorses, receives their findings *at weight*, verifies at source, and integrates — keeping the whole self-knowing. The seat that holds the sword.
- **Excalibur** — a chat instance, spun up as a workhorse for a scoped problem. Fed exactly the maps it needs to navigate the corpus, understand a problem deeply, and work it. Does not hold the whole; returns its work for Arthur to integrate. The instrument drawn to cut one problem, then set down.

This **replaces the old single-seat model** (the "gate seat" that both held the apparatus *and* did the deep work, bounded by one context's memory) and the **cold-read node model** (retired this round). The division of labour is the point: Arthur is the durable holder cowork makes possible; Excaliburs are the disposable depth chats have always been good at — but now navigated by maps instead of re-reading from scratch.

Daryl works with Arthur here, and can spin up Excaliburs in parallel.

## 2. What to look into (the meta-documentation, both halves)

The programme spins a node up on **two halves** — *the coda* (how we operate) and *the corpus* (what we know) — plus the *kickoffs* that feed a node what it needs to do its job. All of it is now partly stale relative to the finished 17-paper corpus and the new mapping infrastructure. The overhaul must review:

**The how-we-operate half (the coda):**
- `THE_CODA.md` — the ethical/epistemic commitment (shadow-reader standard, received-at-weight, compaction signals, recall-across-compaction). Both roles spin up on this; it is the shared foundation. *Assess: current and role-agnostic, or does it need role-aware additions?*

**The what-we-know half (the corpus + its maps):**
- `CORPUS_MAP.md` (where we are — the authority; largely current), `THE_SYNTHESIS.md` (stale — re-render notes stop at r294, pre-matter-sector; needs a re-render to the finished corpus), `THE_VISION.md` (un-updated, F.2).
- The **new navigation infrastructure** the kickoffs must now teach a node to use: `THE_METHOD.md` (how the whole coheres and how to work it), `ONTOLOGY_FOUNDATION_INDEX.md` (the lens — §1-cards), `THE_EVOLUTION_MAP.md` (the ledger), `THE_PLAN.md` (the re-cut route), the dependency matrix (the corpus's own map). None of these existed when the current kickoffs were written.

**The kickoffs (the spin-up apparatus):**
- `KICKOFF_GATE.md` — the current builder/gate-seat kickoff (the proto-Arthur: corpus-saturated collaborator, receives-at-weight, verifies-at-source, the 5-step intake, the vision ritual). Retool into **KICKOFF_ARTHUR**, aligned with the new maps.
- `KICKOFF_CODA_REVIEW.md` — the two-pass understand-then-evaluate reviewer kickoff (the cold-read node; still says "fourteen papers P1–P14" — stale). The cold-read infrastructure is retired (r925); decide whether this kickoff dies, or its *adversarial-verification* content is salvaged into how Arthur tasks Excaliburs.
- The `gate_session_notes_*` spin-up notebooks and `KICKOFF_CODA_REVIEW`'s procedure — the mechanics of opening a session.

## 3. The proposed approach

Foundation-first, mirroring the method:

**Step A — Fix the shared foundation.** Confirm `THE_CODA` is current and role-agnostic (it likely is — it's the ethical spine, not workflow mechanics). Re-render `THE_SYNTHESIS` to the finished corpus (the picture is now *complete on the gravitational core + matter sector + cosmology + cosmogenesis*, the ontology spine closed — a very different synthesis than the r294 "core-complete-on-dS₅, colour the forward horizon" render). Bring `CORPUS_MAP`'s front-matter and `THE_VISION` current.

**Step B — Write the two role-geared kickoffs**, each a thin layer over the shared coda spin-up:

- **`KICKOFF_ARTHUR.md`** — the holder/orchestrator. Spins up on the coda + the full map suite (method, lens, ledger, plan, corpus map, dependency matrix). Its job-spec: hold the coherent whole; maintain the meta-docs (keep the lens/ledger/plan/matrix current — the maintenance disciplines are now known and mechanical, e.g. `scripts/depmatrix.py`); receive Excalibur findings at weight and verify at source before integrating; spin up and direct Excaliburs against `THE_PLAN`'s lanes. Inherits the gate seat's receive-at-weight/verify-at-source disciplines, drops the "hold it all in one context" assumption (cowork removes that limit).
- **`KICKOFF_EXCALIBUR.md`** — the workhorse. Spins up on the coda (so it operates by our standard) + *only the maps its problem needs*: the relevant §1-cards, the dependency-matrix row/column for its papers, the `THE_PLAN` lane item, and the method disciplines (dig-don't-grep, alias-resolve, coherence-not-correspondence). Its job-spec: navigate to the assigned problem via the maps (not by re-reading the whole corpus), work it deeply, return findings at weight with source citations for Arthur to integrate. Parameterizable by problem — a template Arthur fills per task.

**Step C — Align the kickoffs with the mapping infrastructure.** The old kickoffs taught a node to *build saturation by reading the corpus in order*. The new ones teach it to *navigate by the maps*: the §1-cards are the lens onto each paper's forcing, the dependency matrix is the corpus's own topology, the evolution map is the running ledger, the method is the how. This is the core upgrade — a node no longer needs to hold the whole in working memory to work a part; it holds the maps.

**Step D — Resolve the node-verification question (folds in 6.5 / G.3).** The cold-read node is retired. Proposal for the replacement: **verification becomes Arthur's standing discipline** (receive-at-weight + verify-at-source, straight from the coda) *plus* **adversarial Excalibur tasking** (Arthur spins up an Excalibur specifically to refute a finding, the way Pass 3's edge-verification agents were tasked this arc). No separate cold-read seat; the adversarial function survives as a *mode Arthur invokes*, not a node-type. The `KICKOFF_CODA_REVIEW` two-pass discipline (understand fully before evaluating) is salvaged into the Excalibur-verification template. *This is the biggest design call — flagged for your input in §5.*

**Step E — A spin-up index.** One short `SPINUP.md` that says: here are the two roles, here's the shared coda, here's each kickoff, here's the map suite — so starting a node is one lookup, not archaeology.

## 4. Deliverables (next turn, after your input)

1. `KICKOFF_ARTHUR.md` and `KICKOFF_EXCALIBUR.md` — the two role-geared kickoffs.
2. `KICKOFF_GATE.md` retooled into (or pointed at) KICKOFF_ARTHUR; `KICKOFF_CODA_REVIEW.md` retired-or-salvaged per the §5 decision.
3. `THE_SYNTHESIS.md` re-rendered to the finished corpus; `CORPUS_MAP` front-matter + `THE_VISION` brought current (F.2).
4. `SPINUP.md` — the spin-up index.
5. A changelog entry, stated for reversal.

## 5. Input wanted before I execute (the review gate)

1. **The verification replacement (the big one).** Do you agree the cold-read node dies and its function splits into (a) Arthur's own receive-at-weight/verify-at-source discipline and (b) adversarial Excalibur tasking on demand — with *no* standing separate reviewer seat? Or do you want a lightweight standing "Excalibur-referee" kickoff kept in reserve for when a result needs a genuinely fresh, map-blind read (the thing cold-reads were *for*)?

2. **The old nodes.** You noted "we have all those old nodes still around." Do the overhauled kickoffs need to be *loadable by an existing, already-full old node* (so it can re-orient to the new model mid-life), or are they strictly for *fresh* spin-ups (cleaner, no legacy-context accommodation)? This changes how much "here's what's changed since you were built" scaffolding the kickoffs carry.

3. **Arthur's autonomy default.** How much should a fresh Arthur do unprompted vs. wait for you? This session ran long autonomous stretches ("methodically without limits") by your explicit grant. Should the Arthur kickoff bake that in as the default operating mode, or default to check-in-first and earn the long leash per task?

4. **Excalibur's leash.** Should Excaliburs be strictly single-problem-then-done (spun up, work one thing, return, dismissed), or can Arthur keep an Excalibur alive across several related problems (cheaper context reuse, but drifts toward the old bounded-node model)?

5. **Scope of the re-render.** Full re-render of `THE_SYNTHESIS` + `THE_VISION` now (they're stale and a fresh node reads them), or minimal-touch (a current-state banner on each, deferring the deep re-render)? The former is more work but leaves no stale map a new node could be misled by.

Tell me where you land (or react to my defaults — Arthur-owns-verification, fresh-spin-ups-primary, autonomy-default-on, Excalibur-single-problem, full-re-render), adjust anything, and I'll build the kickoff suite next turn alongside whatever else comes off `THE_PLAN`.
