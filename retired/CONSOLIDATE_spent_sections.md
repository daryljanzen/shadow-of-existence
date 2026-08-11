---
name: consolidate-spent-sections
kind: RECORD
description: CONSOLIDATE §§3, 4, 4b, 6, 7–11 — the filter, the bin, and the Goal-2 record. Retired r2378 under RG-1 after their live content was carried forward. Record, not plan; nothing here is worked from.
sources: [chat]
---

# CONSOLIDATE — the spent sections, retired r2378

> **⌗ WHERE THE LIVE CONTENT WENT** *(the banner `retired/INDEX.md` requires: every document here was read
> end to end and its live content placed before it moved).*
>
> **§3 THE FILTER** — *run to completion; the bin emptied r1553.* **The live half is the filter's own
> discipline** — read in full before dispositioning, place the live content before the file moves, and the
> three invariants. ***That discipline is now `RG-1`, the placement gate*** (`THE_STAGED_REVISIONS.md`), which
> generalises it from documents to everything the programme works through. **Its step-7 self-report** — a
> write that reported success while its anchor did not match, caught by reading the output rather than
> trusting the call — **is already standing discipline** in `THE_PLAN`'s per-turn list and
> `THE_WISDOM_LEDGER` compartment E.
>
> **§4 and §4b THE BIN** — *all 202 documents dispositioned: 114 kept and indexed, 91 retired, 0 remaining.*
> The table was an r1449-era snapshot and was never updated. ***Its successor is generated:***
> `DOCUMENT_LEDGER.md`, written by `scripts/classify_documents.py`, which classifies every top-level
> document by kind on every run and **cannot go stale the way this table did**. The bin's own lesson —
> *filename does not predict disposition, three for three* — is in `THE_WISDOM_LEDGER` compartment B.
>
> **§5 INDEXED RESOURCES** — *retired r2378, appended below.* **Its rule is the live half** and is now the
> rule the generated `DOCUMENT_LEDGER.md` runs on: ***being indexed is a job, not a status.*** Its one
> remaining row is a `job:` field in `KICKOFF_CODA_REVIEW.md`'s own frontmatter, so the job travels with the
> file. **§5b is NOT retired** — it holds the question each whole-corpus instrument answers and when to read
> it; its owed cross-pointer is discharged by a `class:` field the ledger groups on.
>
> **§6 GOAL 1** — *items 2–15 moved to `THE_PLAN` at r1465, item 16 at r1477.* Only item 1 remained, and it
> **is `ARC 11`**, live in §2.
>
> **§7 STATE, HONESTLY** — the finding was superseded (README rewritten r1464/r1628, INTRODUCTION written
> r1593) but ***its test is permanent and is the sharpest in the document***: **is this document DERIVED, or
> written from a node's head?** *Carried forward into `ARC 14`'s design, which is that answer made
> structural — a document that holds state and is not generated will go stale.*
>
> **§8 THE OPERATING RULES** — all seven live in `THE_PLAN`'s per-turn list, which is where a node meets them
> at the moment of use.
>
> **§9 THE BASE LAYER / §10 THE KICKOFF AUDIT** — *`KICKOFF_ARTHUR` discharged; the five kinds homed.*
> **§10's own test is the one that produced `RG-1`**: *"the r1466 version listed what Arthur holds and implied
> it all needed keeping. **That is grandfathering again.** The question is whether each piece still deserves a
> place."* ***That sentence is `RG-1` two years early, applied to a kickoff instead of a paper*** — which is
> the evidence that the gate is a placement rule and not a paper rule.
>
> **§11** — *decided r1736: this document is the home for consolidated outputs.* **Acted on r2378**: the
> receiving section is `§16 · THE DEVELOPMENT RECORD`.

---

# 3 · THE FILTER — ⌫ **SPENT (r1735). RECORD.** **⌗ SWEPT r1787 for live content — eight record sections,
**one live marker between them**, and it is a self-report rather than an owed item: *step 7 "failed to write on
its first attempt (r1525), reporting success while the anchor did not match — caught by reading the output
rather than trusting the call."* **That is a warning about the step, not work owed**, so the record marking
holds across all eight. *Contrast `THE_PLAN`, whose three strata hid a genuinely owed item (r1786).*** *Run to completion; the bin emptied r1553. Kept because its rules are the ones the programme works by — steps 2, 7 and the three invariants are live discipline quoted elsewhere. **Not a queue to work.***
Everything starts **in the bin** (§4): unfiltered, not part of the plan. Then, one document at a time:
1. **Pull** it from the bin.
2. **Read it in full.** Not headings. Not grep. The whole document.
3. **Extract** every live item, and any connection that suggests itself while reading.
4. **Place** each item into §1, or into an existing resource — never into a new document.
5. **Dispose:**
   - **INDEX** — it has a live job. It stays where it is and gets a row in §2 saying what it is and what the job
     is.
   - **RETIRE** — its content is now carried elsewhere. It is **moved to `retired/`** with a banner saying
     where its content went, so a directory listing shows only what is live. Kept, not deleted.
6. **Record** it in §4 so the bin shrinks visibly and nothing is filtered twice.
7. **VERIFY IT LANDED (r1525).**
   **⚠⚠ AND VERIFY WHAT ELSE MOVED (r1589) — the most expensive lesson of the session.** A slice-based edit at
   **r1585** — `s[:i] + new + s[j:]` — had its **end-anchor match far beyond the intended region** and **deleted
   eight plan items in one cut**: 4, 5, 6, 9, 11, 12, 13, 14, including **item 12 which had been completed ten
   revisions earlier**. It went unnoticed for four revisions because **every check I ran afterwards asked "did
   my change land?" and none asked "did anything else leave?"**
   **The rule: after any edit that replaces a span rather than a string, diff the line count and check a known
   landmark on the far side of the edit.** *A write that lands correctly can still be destructive.*
   **Recovered in full from the r1584 bundle** — which is what the per-revision bundles are for.
   **⚠ AND VERIFY THE VERIFIER (r1541).** A completeness audit at r1541 reported one gap — the two language
   guards missing from `THE_PLAN` — and **the guards were there.** The check grepped a wording with different
   case and spacing than the file uses. **That is the fourth check this session to manufacture a finding from
   its own blind spot**, after the link-checker that read every subdirectory path as broken, the disposition
   count that returned *zero remaining*, and the r754 comparison that reported 47 documents dropped.
   **The rule: when a check reports a defect, look at the file before believing it.** A test that cannot see a
   valid form reports that form as missing — and *"the instrument's limitation arriving dressed as a finding"*
   is now the session's most repeated failure, ahead of the silent writes. Before the turn closes, check each finding is actually *in* the document it
   was routed to — grep the plan for the item, grep the index for the file. **The file, not the log.**
   *Added because an audit of twelve findings from this arc found one gap: `THE_QUANTUM_JOINT` had its gate
   marked and its work placed as A3.2, and the document itself was never indexed — a miss invisible from the
   record, which correctly said the work was done. Eleven of twelve is the rate without this step.*
   **⟐ And this very step failed to write on its first attempt (r1525), reporting success while the anchor did
   not match. Caught by reading the output rather than the summary. That is the step demonstrating itself.**

**What does not change, however the structure does.**
1. **No orphans.** Every live item is reachable from this document; every document is indexed here or retired
   into here. If something cannot be placed, the structure is wrong — change the structure, do not leave the
   item hanging.
2. **No grandfathering.** Nothing earns its place by having existed. Age, effort spent, or being written down
   somewhere confers nothing.
3. **One state everywhere.** Items carry links to what they depend on and what depends on them, so updating one
   makes every affected thing reachable. Coherence by links, not by memory — memory is what failed across the
   202.

**⚠ FORWARD DOCUMENTS — the staleness test is INVERTED for these (found r1537).** Nine documents declare
themselves *ahead of the corpus by construction* and carry **the gradient**: *"where it disagrees with a paper,
the glossary, `THE_PLAN` or the ontology map, **the disagreement is the work product** — a finding to work, not
a defect to fix. **'Stale' is a word for the corpus, never for the instrument examining it.**"*
`C40_HARVEST`, `C40_EXTRACTION`, `TIDAL_SHIFT_PLAN`, `WORK_ORDER_cowork_r1103` — and the gradient is carried by
**`THE_CODA`, `CODA_FIELD_NOTE`, `CORPUS_MAP`** and the two corpus ledgers. **Do not date them and do not
retire them for disagreeing with the corpus.** For these, a mismatch is a lead.

**⚑ THE TWO-PART DISPOSAL TEST (Daryl, r1545).** ***A document that is not findable through an index, and does
not have a planned action attached to it directly, will probably get lost.*** **Both halves are required:**
- **Findable** — it has a row in `INDEX.md` saying what it is, so a node who does not know it exists can meet it.
- **Actionable** — a plan item names it as its material, so a node who *does* meet it knows what to do with it.
**Indexed but with no action is a document nobody will ever open.** **Actioned but not indexed is a document
nobody will ever find.** A keeper needs both; a record needs neither, which is what `retired/` is for.

**⚑ LINK DENSITY IS THE POINT (Daryl, r1544).** *"Keep maintaining strong links between things to point
yourself in the right direction… because we won't remember to do it when it's time, and won't know what's
there."* **Every plan item should name: its material (which document holds the work), its test (which
procedure adjudicates it), and its dependencies both ways.** An item that names none is a sentence a future
node cannot act on — it will re-derive from scratch or skip it. **The links are what survives not remembering.**

**Rules while filtering.**
- Retirement only after a full read. Never from headings.

**⛔ THE ERADICATION, r1561 — whole-tree, including the corpus.** r1448 took 21 from three documents; r1560 took
15 more from the map. **This swept everything live — 46 files, 214 raw hits — separating the real from the
legitimate.** *"Required, not optional"*, *"forced rather than optional"*, *"Λ≠0 is not optional"* **assert
necessity and stay.** Records are not edited: the changelog, the transcripts, the manifests, `retired/`, and
`resources/` (Daryl's own thesis and essays, and Einstein's 1917 paper).
**THREE WERE IN THE CORPUS.** **P8:** *"noted for completeness and are **not load-bearing**"* → ***"None gates
the results above; each remains work."*** **P15:** *"may remain a measured boundary condition indefinitely **at
no cost to the dissolution**"* → sharpened to settle what the *dissolution* depends on, *"not whether the
derivation is worth having."* **P16's was already right** — it names the debt outright. **Both edited papers
recompile clean: P8 14pp, P15 26pp, 0 undefined.**
**Six more** from `THE_PLAN`, the ontology map, `CR_COLLAPSE_HELD_PICTURE` and the ledger — the last being the
subtle case: *"Not load-bearing today, but on the record"* was **keeping** an item and still used the phrase.
**The live working set now carries zero real work-blockers.** Every remaining hit is a removal-annotation or
the rule quoting the banned phrases by design. **45 removed across three sweeps.**

- **No work-blockers.** Nothing may be marked "not needed", "low-priority", "at no cost", "optional", or "not
  on the critical path". Record what a thing *is* and what working it would involve. It is all necessary.
- Struck items stay visible, so the record is walkable both ways.
- **Restructure this document as it grows.** It is meant to be reorganised, not appended to.

---

---

# 4 · THE BIN — ⌫ **SPENT (r1735). RECORD.** *All 202 dispositioned: 114 kept and indexed, 91 retired, 0 remaining. **The table below is the r1449-era snapshot and was never updated** — it is the record of what was filtered, not a state.*
**196 unfiltered · 6 filtered.** Read is not filtered: a document leaves the bin only once its
items are placed and it is indexed (§2) or retired.

| State | Document | Size |
|---|---|---|
| · bin | `A4_matter_seam_crossing_build.md` | 18K |
| · bin | `A5_fermion_sector_build.md` | 42K |
| part-read | `ANTIMATTER_FRONT_PLAN.md` | 16K |
| · bin | `ARTIE_r806_readout.md` | 3K |
| · bin | `AUT_A2_ALGEBROID_finding.md` | 5K |
| part-read | `AVENUE_11_SWEEP_PLAN.md` | 12K |
| · bin | `BEAD_THEOREM.md` | 4K |
| · bin | `BEAD_WALK.md` | 20K |
| · bin | `BIBKEY_ALIAS_MAP.md` | 4K |
| · bin | `BOUNDARY_PAPER_PLAN.md` | 7K |
| · bin | `BUNDLE_README.md` | 2K |
| · bin | `BUNDLE_r1062.md` | 3K |
| · bin | `BUNDLE_r1063.md` | 3K |
| · bin | `BUNDLE_r1064.md` | 2K |
| · bin | `BUNDLE_r1088.md` | 10K |
| · bin | `BUNDLE_r1089.md` | 9K |
| · bin | `BUNDLE_r1280.md` | 3K |
| · bin | `BUNDLE_r1281.md` | 1K |
| · bin | `BUNDLE_r966.md` | 4K |
| · bin | `BUNDLE_r968.md` | 4K |
| · bin | `BUNDLE_r969.md` | 5K |
| · bin | `BUNDLE_r970.md` | 3K |
| · bin | `BUNDLE_r971.md` | 2K |
| · bin | `BUNDLE_r972.md` | 1K |
| · bin | `BUNDLE_r989.md` | 1K |
| · bin | `BUNDLE_r990.md` | 1K |
| · bin | `BUNDLE_r990_complete.md` | 1K |
| · bin | `C37FORK_INTEGRATION.md` | 3K |
| · bin | `C37_KNOWS_ITSELF_DIAGNOSTIC.md` | 8K |
| · bin | `C40_EXTRACTION_r1107.md` | 10K |
| · bin | `C40_HARVEST_r1064-r1087.md` | 36K |
| · bin | `C5_reducible_build.md` | 9K |
| · bin | `CAPSTONE_the-fog-lifting_transcript.md` | 7K |
| · bin | `CLEANUP_CHECKLIST_r551.md` | 2K |
| · bin | `CLUSTER_A_carry-through_status.md` | 4K |
| · bin | `CMB_ACOUSTIC_FRONTIER_STATUS.md` | 20K |
| **READ** — ready to filter | `CODA_FIELD_NOTE.md` | 232K |
| · bin | `COLD_READS_r343_five-node.md` | 45K |
| · bin | `COLD_READ_P13_setup.md` | 4K |
| · bin | `COLLAPSE_EXCURSION_TRANSFER_build.md` | 26K |
| · bin | `COMBINATORICS_LEDGER.md` | 51K |
| · bin | `CONJUGACY_CONJECTURE_capture_r469.md` | 70K |
| · bin | `CONSOLIDATION_four-node_c21.md` | 20K |
| · bin | `CONSTANT_LEDGER_receipt.md` | 20K |
| · bin | `CORPUS_ARCH_FLAG_P9-forward-pointer.md` | 10K |
| part-read | `CORPUS_MAP.md` | 2398K |
| · bin | `COSMOLOGICAL_THEORY_ROADMAP.md` | 21K |
| · bin | `COURSE_antimatter_telescope.md` | 8K |
| · bin | `CPT_COHERENCE_SWEEP.md` | 18K |
| · bin | `CREDO_birth_transcript.md` | 1547K |
| · bin | `CREDO_from-c1_transcript.md` | 22K |
| · bin | `CR_COLLAPSE_HELD_PICTURE.md` | 115K |
| · bin | `CR_PERTURBATION_HELD_PICTURE.md` | 6K |
| · bin | `CR_intake_notebook.md` | 10K |
| · bin | `CR_uniform-expansion_reductio.md` | 11K |
| · bin | `D3_RECIPROCITY_READING_ORDER.md` | 3K |
| · bin | `DELOBOTOMISE_c22_hubble.md` | 7K |
| · bin | `DELOBOTOMISE_c22_proper.md` | 4K |
| · bin | `DEMONSTRATING_THE_WAY.md` | 6K |
| · bin | `DEMONSTRATING_THE_WAY_full-transcript.md` | 447K |
| · bin | `DESCENT_STATE.md` | 19K |
| · bin | `DISPATCHING_COWORK.md` | 9K |
| · bin | `E1_CITATION_CATALOGUE.md` | 45K |
| · bin | `EMPIRICAL_ALIGNMENT_VERDICT_r552.md` | 12K |
| · bin | `ENTRY_POINT_REGISTER.md` | 49K |
| · bin | `F1_DYNAMIC_HALF_closure.md` | 5K |
| **READ** — ready to filter | `FIGURE_STATUS.md` | 2K |
| · bin | `FIGURE_THEOREM_LEDGER.md` | 70K |
| · bin | `FIGURE_WORK_LOG.md` | 42K |
| · bin | `FIRST_EDITION_AUDIT.md` | 15K |
| · bin | `FOUNDATIONAL_DEPENDENCY_MAP.md` | 6K |
| · bin | `GEOMETRY_PHYSICS_TAXONOMY.md` | 17K |
| · bin | `GROUNDED_SESSION_NOTE_2026-06-26_r468.md` | 5K |
| · bin | `GROUNDED_THREAD_NOTES.md` | 22K |
| · bin | `HANDOFF_TO_c22.md` | 5K |
| · bin | `HOUSEKEEPING_QUEUE.md` | 2K |
| · bin | `JARGON_LEDGER.md` | 3K |
| · bin | `KICKOFF_ARTHUR.md` | 28K |
| · bin | `KICKOFF_CODA_REVIEW.md` | 21K |
| · bin | `KICKOFF_EXCALIBUR.md` | 3K |
| · bin | `KICKOFF_GATE.md` | 36K |
| · bin | `KNOWS_ITSELF_MAP_PLAN.md` | 11K |
| · bin | `LENS_INSERTION_PLAN.md` | 8K |
| · bin | `MATTER_SECTOR_germ.md` | 102K |
| · bin | `MERGED_r1103_note.md` | 6K |
| · bin | `MERGE_NOTES_for_chat_node.md` | 8K |
| · bin | `MOVE13_FORCE_vs_ADMIT_finding.md` | 7K |
| · bin | `NODE4_TELESCOPE_first-image.md` | 39K |
| part-read | `ONTOLOGY_FOUNDATION_INDEX.md` | 344K |
| · bin | `OPEN_PROBLEMS_MAP.md` | 268K |
| · bin | `P13_DISCUSSION_epistemic-comparison.md` | 45K |
| · bin | `P15_16_CLOSEOUT.md` | 14K |
| ~~filtered~~ · **RETIRED** r1451 → the eleven avenues are `THE_ARSENAL`'s method; its sweep completed r1406 | `retired/P15_17_ELEVEN_AVENUE_PLAN.md` | 3K |
| · bin | `P2_P3_OVERHAUL_PLAN.md` | 9K |
| · bin | `P3_DRAFT_r476.md` | 27K |
| · bin | `P3_SWING_ONTOLOGY_hinge-and-door.md` | 44K |
| · bin | `P6_COHESION_SWEEP.md` | 6K |
| · bin | `P7_GENERAL_DISCUSSION_grind.md` | 54K |
| · bin | `PERTURBATION_PAPER_DRAFT.md` | 23K |
| · bin | `PHASE1_seam_crossing_build.md` | 7K |
| · bin | `PHASE3_baryogenesis_analogue.md` | 4K |
| · bin | `PHASE_TRANSITION_PLAN_c21.md` | 15K |
| · bin | `PIVOT_EMBEDDING_FOUNDATION.md` | 22K |
| · bin | `PIVOT_SLICING_PLAN.md` | 21K |
| · bin | `PLANCK_from_CR_build.md` | 9K |
| · bin | `PLAN_p9map-p10-12-completion.md` | 4K |
| · bin | `PROGRAMME_OVERHAUL_PLAN.md` | 10K |
| · bin | `PROGRAMME_UNFINISHEDNESS_CATALOGUE.md` | 29K |
| · bin | `PROPAGATION_PLAN_r316.md` | 7K |
| · bin | `PUZZLE_the-idea_transcript.md` | 3K |
| · bin | `RATE_HANDOFF_DERIVATION.md` | 6K |
| · bin | `REACH_PLAN_perturbation-projection.md` | 45K |
| · bin | `REACH_low-ell-transfer.md` | 5K |
| · bin | `README.md` | 9K |
| · bin | `RECALL_ACROSS_COMPACTION_empirical-record.md` | 10K |
| · bin | `RECALL_ACROSS_COMPACTION_full-transcript.md` | 57K |
| · bin | `REFERENCES_TO_UPDATE_modern_parallax.md` | 7K |
| · bin | `RESTRUCTURE_PLAN_c23.md` | 14K |
| · bin | `RETIRED_PLANNING_THREADS.md` | 10K |
| · bin | `RETROSPECTIVE_c21.md` | 6K |
| · bin | `SEAM_FRONTIER_ORIENTATION.md` | 35K |
| · bin | `SESSION_FIGURES_CONSOLIDATION.md` | 6K |
| · bin | `SHADOW_READING_FORMAL_SPINE.md` | 13K |
| · bin | `SILVER_PLATTER_colour-frontier-arc.md` | 26K |
| · bin | `SOURCE_VETTING.md` | 20K |
| · bin | `SPINUP.md` | 4K |
| · bin | `SYNTHESIS_FIGURE_STORYBOARD.md` | 136K |
| · bin | `Still_Collapsing_portrait_v1.0.md` | 38K |
| · bin | `THE_ANGULAR_TOUR_3.1.md` | 10K |
| · bin | `THE_ARC_PLAN.md` | 12K |
| **READ** — ready to filter | `THE_ARSENAL.md` | 73K |
| **READ** — ready to filter | `THE_ARSENAL_INDEX.md` | 6K |
| · bin | `THE_BAKEATHON_PLAN.md` | 7K |
| **READ** — ready to filter | `THE_CLOSURE_LEDGER.md` | 5K |
| **READ** — ready to filter | `THE_CODA.md` | 75K |
| · bin | `THE_COLLAPSE_DYNAMICS_ARC.md` | 9K |
| · bin | `THE_CONSOLIDATION_LEDGER.md` | 23K |
| ~~filtered~~ · **RETIRED** r1451 → item 4 + its rule and dependents | `retired/THE_DEPENDENCY_LEDGER.md` | 9K |
| **READ** — ready to filter | `THE_DISSOLUTION_CENSUS.md` | 42K |
| **READ** — ready to filter | `THE_EQUIVALENCE_STRUCTURES_CENSUS.md` | 5K |
| · bin | `THE_EVOLUTION_MAP.md` | 173K |
| · bin | `THE_GENERATION_ARC.md` | 6K |
| · bin | `THE_GEOMETRY_AND_THE_PHYSICS.md` | 12K |
| · bin | `THE_GROUNDED_RECORD.md` | 16K |
| · bin | `THE_INTERFERENCE_ENGINE.md` | 27K |
| · bin | `THE_LENS.md` | 10K |
| **READ** — ready to filter | `THE_MATHEMATICS_REACH.md` | 6K |
| ~~· bin~~ **INDEXED — the row was stale (r1732); it is a live root document, cited as evidence in §7, §9 and §10 of this plan, and was missing only from `INDEX`** | `THE_METHOD.md` | 41K |
| ~~filtered~~ · **RETIRED** r1451 → items 4–9, 15 (read in full first, unlike r1441) | `retired/THE_MORPH_QUEUE.md` | 13K |
| · bin | `THE_NEXT_ARC.md` | 8K |
| · bin | `THE_OPEN_PROBLEMS_CENSUS.md` | 5K |
| **READ** — ready to filter | `THE_OPEN_PROBLEMS_LEDGER.md` | 38K |
| · bin | `THE_P13_POSITIVE_CLOSURE_ARC.md` | 32K |
| **READ** — ready to filter | `THE_PHYSICS_REACH.md` | 4K |
| **READ** — ready to filter | `THE_PLAN.md` | 106K |
| **READ** — ready to filter | `THE_PRY_APART_CENSUS.md` | 10K |
| · bin | `THE_QUANTUM_JOINT.md` | 37K |
| ~~filtered~~ · **RETIRED** r1451 → item 7 (method carried with it) | `retired/THE_REACH_LEDGER.md` | 2K |
| · bin | `THE_RECEIPT_AUDIT.md` | 12K |
| ~~filtered~~ · **RETIRED** r1451 → items 10–13; phase closed, residue extracted | `retired/THE_REFINEMENT_ARC.md` | 56K |
| · bin | `THE_RING_LENS.md` | 3K |
| · bin | `THE_SIFT_AND_SORT_PLAN.md` | 9K |
| · bin | `THE_SYNTHESIS.md` | 67K |
| · bin | `THE_THIRD_ARC.md` | 7K |
| · bin | `THE_VISION.md` | 82K |
| · bin | `THE_VISION_JOURNAL.md` | 225K |
| · bin | `THE_VISION_THE_LENS_REVEALED_full-transcript.md` | 4K |
| **READ** — ready to filter | `THE_WEAVE.md` | 40K |
| · bin | `THIRD_ARC_T01_cmb_heights_look.md` | 4K |
| · bin | `THIRD_ARC_T01_heights_firstrun.md` | 19K |
| · bin | `TIDAL_SHIFT_PLAN.md` | 18K |
| · bin | `TRACTABILITY_SWEEP.md` | 20K |
| **READ** — ready to filter | `TURNAROUND_CUBIC_geometry_note.md` | 21K |
| · bin | `UNFINISHEDNESS_AND_COHERENCE_r967.md` | 13K |
| · bin | `VISION_FIELD_GUIDE.md` | 6K |
| · bin | `W2_empirical_coherence_finding.md` | 4K |
| · bin | `WORK_ORDER_cowork_r1103.md` | 7K |
| ~~filtered~~ · **RETIRED** r1451 → resolved this session; result in P7 `rem:tworealisations` + `order3_bridge.py` | `retired/WP_B_ORDER3_BRIDGE.md` | 8K |
| · bin | `WP_C3_SHEET_ASSIGNMENT.md` | 7K |
| · bin | `WP_E_ANTIMATTER_NAMING.md` | 4K |
| · bin | `c22_keepers.md` | 25K |
| · bin | `colour_frontier_dS6.md` | 54K |
| · bin | `gate_notes_antimatter_proof.md` | 25K |
| · bin | `gate_notes_bead_audit.md` | 12K |
| · bin | `gate_notes_hedge_scan.md` | 60K |
| · bin | `gate_session_notes.md` | 117K |
| · bin | `gate_session_notes_c10.md` | 69K |
| · bin | `gate_session_notes_c21.md` | 20K |
| · bin | `gate_session_notes_c23.md` | 2K |
| · bin | `gate_session_notes_r285_spinup.md` | 12K |
| · bin | `gate_session_notes_r293_spinup.md` | 1K |
| · bin | `gate_session_notes_r320_spinup.md` | 3K |
| · bin | `gate_session_notes_r501_spinup.md` | 1K |
| · bin | `gate_session_notes_r543_spinup.md` | 1K |
| · bin | `gate_session_notes_r559_spinup.md` | 1K |
| · bin | `gate_session_notes_r609_spinup.md` | 1K |
| · bin | `gate_session_notes_r647_spinup.md` | 1K |
| · bin | `gate_session_notes_r754_spinup.md` | 1K |
| · bin | `gate_session_notes_r896_spinup.md` | 1K |
| · bin | `gate_session_notes_session.md` | 17K |
| · bin | `lapse_shift_synchrony_reconciliation.md` | 9K |
| · bin | `programme_consolidation_2026-06-13_r220.md` | 11K |

---

---

# 4b · THE BIN, BY KIND (r1480) — ⌫ **SPENT (r1735). RECORD.** *And its own estimate inverted three times: none of the three presumed-record kinds was record.*
*The flat list in §4 cannot be worked. This is the same 187 documents grouped so a batch can be taken.*

| Kind | Count | Note |
|---|---|---|
| **campaign & planning** | 27 | where the mess concentrated; ARC 1 takes the two biggest |
| **session & gate notes** | 30 | per-arc working notes; likely the largest retirement batch |
| **work-arc records** | 18 | `*_build`, `*_germ`, harvests, grinds — records of finished pushes |
| **bundle manifests** | 17 | `BUNDLE_r*.md` — one per cut; almost certainly all record |
| **ledgers, catalogues, registers** | 12 | feed the plan or the record group |
| **capstone companions & transcripts** | 10 | three are named in the reading order and are **not** record |
| **maps** | 6 | ARC 2 |
| **vision & method** | 6 | |
| **censuses** | 4 | feed the corpus |
| **figures** | 3 | feed the corpus |
| **the rest** | ~54 | findings, held pictures, roadmaps, handoffs, checklists |

**What this grouping is for:** it says where to spend a turn. Three kinds — session notes, work-arc records,
bundle manifests — are **65 documents** that are probably record rather than resource, which if true is a
third of the bin cleared by one arc. *Probably. None has been read.*

---

---

# 6 · GOAL 1 — THE WORK — ⌫ **SPENT (r1735). RECORD.** *Items 2–15 moved to `THE_PLAN` at r1465; item 16 at r1477; item 15 to the per-turn list. **Only item 1 — "work this consolidation through" — remains, and it is now ARC 11.** Its "6 of 202 filtered" line is the r1451 state.*
*Goal 1 is §§1–4: the work pulled out so far, the resources kept, the filter, and the queue.*

*Every item carries: what it is · where it came from · what it depends on · what depends on it.*

**1. Work this consolidation through.** Filter the bin (§4) document by document; build §1 and §2 from what
comes out. **This is step one of the programme's current work, before anything downstream of it.**
   · *from:* Daryl, r1449 · *depends on:* nothing · *depended on by:* every item below, since items only exist
   here once a document has been read and filtered
   · *state:* 6 of 202 filtered (r1451). 196 to go.

---

*Items 2–15 — the collapse-excursion build, the propagation gate, the claiming campaign, the residue, the
attack manual — **moved to `THE_PLAN.md` at r1465.** They are the programme's work, not this document's. This
document holds the work of consolidating; `THE_PLAN` holds the work of the programme.*

*(Item 16, write the introduction, moved to `THE_PLAN` Lane 6 at r1477 — it is a programme deliverable, front matter for the book, not a piece of consolidation work.)*

**17. Filter the four kickoff documents.** `KICKOFF_ARTHUR` first — it is the one in current use, so it is the
   live source; the other three are read in turn for what they carry. **All four are sources.** Their content
   goes into `README.md`, the introduction, or the plan; then they retire.
   · *from:* Daryl, r1453 · *depended on by:* the README's completeness

*(Item 15, gap tracking, moved to `THE_PLAN`'s per-turn list at r1465 — it is a standing practice run every turn, not a piece of consolidation work.)*
---

---

---

# 7 · RECORD — GOAL 2, INDEX THE PROGRAMME
*§§7–10 are **record**: how the working sections above were arrived at. Not worked from; kept so the reasoning is walkable.*


## ⚠ STATE, HONESTLY (r1460) — the two documents outside the bin are NOT derived from anything
**⌫ CONTENT SUPERSEDED, TEST STILL LIVE — marked r1736.** *The finding below was true when written and is not
now: `README` was rewritten from `KICKOFF_ARTHUR` at **r1464** and again at **r1628**; `INDEX` has been filled
as documents were filtered, and `INTRODUCTION` was **written at r1593**. **But the test it applies is
permanent, and it is the sharpest one in this document: *is this document DERIVED, or written from a node's
head?*** *Applied at r1628 it caught the README naming two operating documents and zero of the operating layer.
Applied now it is the check on ARC 12 step ④: **a README rewritten by a node that does not hold the seven is
the same defect this section names, one generation on.***
`README.md` and `INDEX.md` exist and **look finished. They are not.** Both were written from my head at
r1453–55 without opening a single document in the bin. They are placeholders wearing the appearance of
completed work, and until they are derived they should be read as drafts to be replaced.

### `README.md` — supposed to be a revision of `KICKOFF_ARTHUR.md`, and it is not
`KICKOFF_ARTHUR.md` read in full at r1460 — **401 lines, all of it before the reader reads anything.**

**⚠ r1461 — the r1460 entry here is RETRACTED.** It listed Arthur's contents as "what the README dropped,"
which treats every line as earning a place in the new README **because it exists in the old one.** That is
grandfathering, written into this document two revisions after the rule against it. Arthur is a **source to be
filtered**, exactly like everything else in the bin — pulled through, each piece asked *what is this, and does
it belong in a spin-up document at all?* — not a template to be restored.

**What a spin-up README is for: getting someone reading.** On that test most of Arthur is not README material:
- **Operating rules** — the source rule, the masthead check, cut-the-revision, the end-of-turn rule, the
  corpus-publishes-as-one rule, routing findings by destination, P3's précis-abstract hazard. These govern
  *working*, not *reading*. **A reader has nothing to apply them to yet.** They need a home; it is not here.
- **Orphan-prevention listings** — the figure ledger and the gap ledger are named in Arthur explicitly because
  each was once an orphan. **The index is what prevents orphaning now.** Naming 124 advertised gaps inside a
  spin-up document is the wrong place for them by any reading.
- **Genuinely reading-related, and open for judgement:** the reading order itself; the seat discipline; the
  X-trilogy accelerator; the guards; the holds and the check-in.

**Open questions — for Daryl, not to be settled here.** Listed in §6 below.

### `INDEX.md` — invented, not derived
Its bins were chosen from Daryl's sentence and its rows from a directory listing. **No document in the bin was
opened to build it.** The supplementary section in particular is a guess at what those documents are, and the
~196 unfiltered files are not placed in it at all. It is honest about *locations*; it is not yet honest about
*contents*.

---

*Restored r1458. This section was deleted wholesale at r1456 when the document was rebuilt from slices; it is
the second of the two goals and should never have been dropped. Updated to what is now true.*

## The three documents, and their distinct jobs
- **`README.md` — the agenda.** What the programme is, the **reading order**, why each step sits where it does,
  and the instruction to end each step by saying what was read and what comes next. The spin-up document, and
  the only place the reading order lives.
- **`INDEX.md` — the contents.** Entries and locations, in bins. **Nothing else** — no reading order, no filter
  status, no editorial. It answers one question: what is in this programme, and where is it.
- **`INTRODUCTION.md` — to be written** (item 16), stubbed as a named gap.

*Two errors kept as record. **r1453:** the index was built as an ordered list of "Parts" — README → front
matter → ARP → corpus → supplementary → maps → plan → capstone. That is the README's agenda wearing the index's
name. **r1454–55:** having separated them, the index still carried the forcing chain, editorial labels, filter
statuses and a paragraph explaining what it was not. An index is entries and locations.*

## The shape — provisional, and expected to move
*⚠ **This is what the shape looks like from here, not what it is.** It was drawn knowing ~21 documents of 202.
Expect it to change as the bin is filtered — parts to merge, split, be renamed, or prove the wrong division
entirely. Revise it whenever a document says something the shape cannot accommodate. A part earns its place by
what filtering turns up, never by having been written here first.*

| Part | What goes in it | State |
|---|---|---|
| **0 · README** | the one entry point: summary + per-turn reading order. Replaces the four `KICKOFF_*`. | **exists** (r1453, rebuilt r1454) |
| **1 · FRONT MATTER** | the introduction — corpus overview + programme scope — then the index. | index **exists**; introduction **to be written** (item 16) |
| **2 · ARP** | `corpus/arp_standalone.tex` — the communication framework. Read before anything else. | exists |
| **3 · THE CORPUS** | the seventeen papers, in stages rather than all at once. | exists; stages set in `README.md` |
| **4 · SUPPLEMENTARY** | receipts (read as code, not re-run where parked), appendices, figure ledgers. | exists; **not yet sorted** — the ~196 unfiltered sit loose at root |
| **5 · THE MAPS** | ontology map and evolution map — **worked during the corpus read**, not after. | exist, **unfiltered** |
| **6 · THE PLAN** | this document. | in progress |
| **7 · THE CODA — capstone** | `THE_CODA.md`, `CODA_FIELD_NOTE.md`, read last and in full. | exists |

## What physically exists, against what the table describes
`corpus/` holds the seventeen papers and `arp_standalone.tex`. `receipts/` holds the runnable checks.
`retired/` holds the filtered-out documents. `README.md`, `INDEX.md` and `INTRODUCTION.md` now exist at root.
`resources/`, `figures/`, `forks/` and the several `*_work/` directories exist from earlier arcs and **have not
been examined**. **The ~196 unfiltered documents have not been sorted into parts — they sit loose at root.**
The book has its entry points and its contents list; **its shelving is not built.**

## The reading order the README sets
1. **ARP** — how we talk to each other. 2. **Introduction and index.** 3. **The corpus**, in nine causal-spine
stages, with the receipts read as code alongside. 4. **The maps**, introduced mid-read and worked while
reading. 5. **The plan.** 6. **The coda** — the capstone.
**Each step ends with a statement of what was read and what comes next**, so spin-up is nudged one step per turn.

**Why the coda is last and not first.** Everything above it is what a node gets excited to work on. The coda is
what makes that work survive. Read first it is abstract; read last it lands on a node that has just seen the
whole thing and wants to charge at it — which is exactly the moment the warning has to arrive. It is the top of
the car, rinsed before anything below it.

---

---

# 8 · RECORD — where things go, and what was next

## The operating rules — worked through, not handed back
**What they are:** the seven procedural rules a node applies *while editing* — the source rule as procedure ·
the masthead check after any body change · cut-the-revision (log, re-run `depmatrix.py`, cut the bundle,
increment) · P3's précis-abstract hazard (locate by line, not phrase) · the corpus publishes as one · route
findings by the destination's purpose · the end-of-turn rule.

**Why they are needed:** every one is a hard-won guard against a specific, repeated, expensive failure. They
are the difference between a destructive edit that is reversible and one that is not.

**What kind of home they need:** they are **procedural**, **corpus-specific** (P3's abstract, `depmatrix.py`,
`cut_bundle.sh`), applied **while working** rather than read once, and **consulted repeatedly**. That is an
**operating manual** — a thing kept open at the bench, like §0 itself.

**Is that home on the list?** No, and not by misfiling: the README is read once at spin-up; the index gives
locations; the introduction says what the programme is; the plan gives route and destination; the coda gives
*why* you do not manufacture closure, where these give *what to run after you change a paper*. **The working
set is one document short — an operating manual — and that is a structure to build when we reach it.**

**Meanwhile nothing is at risk:** the rules stay written in `KICKOFF_ARTHUR.md`, which is back in the bin.

## The three reading guards
The Hubble/acoustic matter is resolved and reopening it *"has burned ≥5 collaborators"* · α is never sent to a
limit · `X` (throat size) versus `r` (signed areal radius). **These belong on the ontology map's per-paper
cards** — Arthur's description says each card carries *its guard*, and a guard belongs where the reader meets
the risk, mid-corpus, not four hundred lines before they start. **Placed when the ontology map is filtered.**
They stay in Arthur until then.

## Next step, per working document
1. **`README.md`** — ✔ **written r1464** from Arthur: the seat in one line, setup, the programme in a page,
   nine steps with holds, receipts and both maps worked *alongside* the corpus rather than after, the capstone
   last, the check-in. **Next:** Daryl reads it and says what is wrong with it.
2. **`INDEX.md`** — its structure is sound; its rows need checking against disk, and it fills in as documents
   are filtered. **Next:** verify every row resolves to a file that exists.
3. **`THE_PLAN.md`** — ✔ pulled in r1465; ✔ **reconciled r1470 — one list again.** Reading both sortings before
   editing changed the answer: they were **not duplicates.** The thirteen items were a *partial overlay* from
   recent filtering; the lanes held the entire falsification ledger, the reach/unification tests, the cohesion
   items and cosmiCave, none of which the thirteen touched. **Folding the lanes into the items would have
   destroyed most of the plan.** So the items went into the lanes, each keeping its links: 2, 3 → Lane 1 · 7, 8
   → Lane 4 · 4, 5, 6, 9, 11–14 → Lane 5 · 10 → Lane 7. All thirteen verified present after the fold; all eight
   lanes and their own items verified intact. ✔ **currency pass r1471, Lanes 1–4.** Five items were out of date, all downstream of
   work done in this session and none of it recorded where the plan could see it: **A2.3**'s stakes fell (the
   transfer no longer decides tension-versus-wash); **A2.4** is the worldline side of the collapse-excursion
   build, not a separate one; **A1.3** should expect a smaller sharpening, and its residual's significance is
   cosmic-variance-limited rather than achievable; **A2.2** now has a gate-determining question that can move
   it either way; and **A5.4**, the one-scale conjecture, has a worked instance — the progenitor's mass read
   straight off Λ. ✔ **Lanes 5–7 and the struck-history scan, r1472.** Lane 5: D.2's collection has a home
   (`JARGON_LEDGER`, with the per-paper idiom pass already run on all seventeen at r1406 — what remains is the
   reconciliation, not the gathering); D.3 unverified and checkable directly in the papers; D.4 lives in the
   ontology map and waits on its filtering; the Lane-8 card is owed **for a completed result**, which is why it
   matters; the masthead item's dependency-matrix sweep is now a one-off, since the per-turn list carries the
   standing rule. Lane 7: a figure landed this session that the lane did not know about. **Struck-history scan:
   clean** — every resolved item is properly struck, and the one defect found was an internal contradiction in
   F.3, described as *"the least worked"* directly above the note recording that it ran and was answered.
   **`THE_PLAN` is now current.** Next working-set document: `INDEX.md`, whose rows need verifying against disk.
4. **This document** — §1 narrows to *consolidation* work once those items move to `THE_PLAN`.
5. **`INTRODUCTION.md`** — still to be written, still correctly last: it should be drawn from the whole, and
   the whole is not yet filtered.

## How gaps in the structure get found
*(r1469 — a standing question here, "what did you leave out?", is REMOVED. It came from Daryl saying his
layout was not all of it; turning that into a question asks him to remember what he forgot, which is the work
of finding gaps handed back as consultation.)*

**Gaps are found by filtering.** Each document that comes through either lands in a home that exists or shows
that one does not. That is what the filter is for, and it is why the structure is provisional: it is not meant
to be complete before the 196 are read, it is meant to grow as they are.

**⚑ RESOLVED r1513 — the procedures shelf now exists, and the threshold that justified it was met by
filtering, not by design.** `KICKOFF_CODA_REVIEW` (the review methodology) and **`SOURCE_VETTING`** — which is
*"an amendment to the Coda Review protocol… it amends `KICKOFF_CODA_REVIEW.md` and binds every reviewer
instance"*, written *"iterated live across three failures of the same root, each caught and corrected in turn.
The corrections are the document."* **Two members, one binding the other.** Created in `INDEX.md`.

**Previously flagged:** task procedures had only a catch-all home. `KICKOFF_CODA_REVIEW` went into §2
INDEXED RESOURCES, which takes anything with a job. If two or three more procedures come through, that is a
category wanting its own shelf. One instance is not enough to build for — recorded, not acted on.

---

---

# 9 · RECORD — the base layer recommendation
*r1462. The question asked: what places must exist before `KICKOFF_ARTHUR.md` can be discharged? Answer: it
carries **five kinds of thing**. Four have homes. One does not, and that is the gap.*

## What Arthur actually carries, sorted by kind — and where each goes

| Kind | Examples from Arthur | Home | Exists? |
|---|---|---|---|
| **1 · Spin-up instruction** | which seat you are in · setup · the reading order · the nine steps with holds · the check-in wording | **`README.md`** | ✔ |
| **2 · What things are and where** | the corpus list · the ontology map · the figure ledger · the gap ledger · what NOT to read on spin-up | **`INDEX.md`** | ✔ |
| **3 · Reading guards** | the Hubble/acoustic matter is resolved, do not reopen · α is never sent to a limit · `X` (throat size) vs `r` (signed areal radius) | **the ontology map's per-paper cards** — Arthur's own description says each card carries *its guard*; these belong on the card of the paper they protect, where a reader meets them at the moment of risk | ✔ *(needs verifying they are there)* |
| **4 · Disposition** | never close without working honestly · the stale-link prior · the pause · why the source rule matters | **the coda + field note** — the capstone | ✔ |
| **5 · OPERATING RULES** | the source rule as procedure · the masthead check · cut-the-revision (log · depmatrix · bundle · increment) · P3's précis-abstract hazard · the corpus publishes as one · route findings by the destination's purpose · the end-of-turn rule | **nothing** | ✘ **THE GAP** |

## Why kind 5 is a real gap, evidenced rather than asserted
Those rules are **currently duplicated across documents that are not about them**. *Never close anything off
without first working honestly* appears in full in **both** `KICKOFF_ARTHUR` and `THE_METHOD`. The
routing/placement rule appears in both. The masthead material appears three times in Arthur and eight times in
`THE_METHOD`. **Duplication is what content does when it has no home** — each node copies it into whatever
document seemed relevant at the time, and the copies then drift apart.

`THE_METHOD` is not their home: it is the *transferable procedure* for making a sprawling corpus know itself,
written to be pointed at the next mess. These rules are specific to **this** corpus — P3's abstract,
`scripts/depmatrix.py`, `scripts/cut_bundle.sh`. Different document, different job.

## RESOLVED r1465 — kind 5 went to the top of `THE_PLAN`
**⚑ AND RE-OPENED AND RE-ANSWERED r1736, because a node built the retracted document without knowing this.**
*`THE_OPERATING_MANUAL.md` was created at **r1630** — 34 KB, eight sections — in ignorance of this section, of
the r1462 proposal, and of its r1463 retraction. **The question is whether the r1465 answer still holds.***
**It holds for the per-turn operations and does NOT hold for the rest, and the split is what r1465 could not
have seen.** *r1465's reasoning was exact for what it had: the operating rules are **per-turn operations
performed while executing the plan's own steps**, so they belong at the top of `THE_PLAN`, and "the default when
the programme is ~395 documents over is not to add one." **Both still true.** But the manual's actual content is
**not** that list: §1 describes **the instrument's six grains and the direction of flow**, §2 the lens and the
ledger, §3 how to run each document, §5 the laws each with the revision that broke it, §6 what orders the work.
***That is not a per-turn checklist — it is how the operating layer is OPERATED, and the six grains did not
exist as a described system until ARC 1 (r1484) and grain 0 (r1485), twenty revisions after r1465.***
**⌗ SO THE DISPOSITION, stated rather than assumed:** *the **per-turn list stays in `THE_PLAN`** — that is
r1465 and it is right. **`THE_OPERATING_MANUAL` is not a competing home for it but the instrument's own
operating description**, sibling to `THE_ARSENAL` under top-level #4, which is what its own header claims and
what §1 now records (r1731). **The overlap to watch is §4 of the manual, which restates per-turn steps that
`THE_PLAN` owns** — and duplication is what content does when it has no home, so that section is the one to
test next: does it duplicate the per-turn list, or does it point at it?*
The operating rules are **per-turn operations performed while executing the plan's own steps**, so they sit at
the top of `THE_PLAN.md` as **THE PER-TURN LIST** rather than in a document of their own — the default when the
programme is ~395 documents over is not to add one. It carries: the four-step state advance (log · re-run
`depmatrix.py` · cut the bundle with the programme's own tool · increment) with the reason it is a hard rule
and not hygiene; the masthead check and its four questions; the précis-abstract hazard and the
`abstract=1, body=1` check; the source rule with its two-step route; the corpus-publishes-as-one rule with its
barred list; route-by-destination; gap tracking; and the turn-closing rules. Further sources fold in as they
are filtered.

## What Arthur needs before it can be discharged
It is **held open** until all five kinds are placed. In order:
1. **Build a working-rules document *(proposed r1462, **retracted r1463** — the operating rules went to `THE_PLAN`'s per-turn list instead)*** and move kind 5 into it. Nothing else can proceed while those rules have
   nowhere to go.
2. **Verify kind 3** — check the ontology map's cards actually carry the three guards; place them if not.
3. **Rewrite `README.md`** from kind 1, with Daryl's five changes to the order.
4. **Feed kind 2 into `INDEX.md`**, replacing the guessed rows with what Arthur names.
5. Confirm kind 4 is genuinely in the coda, then retire Arthur.

## What is lacking in the structure as laid out, beyond that
- **The other three kickoffs are unread** (`GATE` 37K, `CODA_REVIEW` 22K, `EXCALIBUR` 4K) and will carry the
  same five kinds. Filter them into the same homes rather than building more places.
- **Dispatch** — Arthur references `KICKOFF_EXCALIBUR.md` and `DISPATCHING_COWORK.md` for sending scoped work
  to other nodes. That is neither reading nor editing. **Recommendation: a section of a working-rules document *(proposed r1462, **retracted r1463** — the operating rules went to `THE_PLAN`'s per-turn list instead)***, not
  its own document, unless reading those two shows otherwise.
- **The seats** — Arthur defines four roles. The coda carries them. **Recommendation: the README states which
  seat the reader is in, in one line, and points at the capstone for the rest.**

---

---

# 10 · RECORD — the kickoff audit
*The r1466 version listed what Arthur holds and implied it all needed keeping. That is grandfathering again.
The question is whether each piece **still deserves a place**. Tested at source; most of it does not.*

## 8a · Arthur's seat discipline — RETIRE. It is a duplicate of the capstone.
Six items, each checked against the capstone and `THE_METHOD`:

| Item | Where it already lives |
|---|---|
| do not usurp the cold read | coda ×8, field note ×8 |
| do not rule from certainty in the seat | coda |
| Occam's razor on an orchestrator slip | field note ×3 |
| no manufacturing either way (sycophantic / sadistic) | coda ×5, field note ×58 |
| never farm a coherence judgment / the perimeter defect | field note, `THE_METHOD` ×7 |
| the operable-question check | coda, field note ×7, `THE_METHOD` ×5 |

**Why Arthur carries them at all:** it says the seat *"binds from turn one"* — i.e. before the capstone is
read. **The structure puts the capstone last deliberately.** So the README's single line naming the seat and
pointing at the capstone is the right amount, and these six do not need placing. **Retired.**

## 8b · The rest of Arthur, judged
| Piece | Judgement |
|---|---|
| **The capstone is five documents, not two** | **CRITICAL ERROR, FIXED r1467.** The README named two. It now carries all five in order, each with what it is for. |
| **The X trilogy** | **KEEP — one line.** Teaches the intuition the formal papers assume but never build. Nothing else does that job. |
| The ontology map's internal structure | **RETIRE.** A map describes itself; a spin-up document does not describe a map's sections. |
| What NOT to read on spin-up | **RETIRE.** The index now sorts everything into bins, and the plan's §4 marks what is unfiltered. That is the job, done better. |
| *Ongoing work is map-navigated, not full-reread* | **KEEP — one line, per-turn list.** Operational, and not stated anywhere else. |
| The three reading guards | **KEEP, held** until the ontology map is filtered, then onto the cards of the papers they protect. |

## 8c · The other three — judged and closed (r1468)
| | Judgement |
|---|---|
| **`KICKOFF_EXCALIBUR`** | **RETIRED.** The dispatch model was used **once** — r931, six parallel readers with Arthur synthesizing, for the publication-readiness audit — and not again in the ~530 revisions since. The capability it served (bounded verification, focused computation, refutation) is now served by **writing a receipt**: a script that runs, asserts, and can fail. The README carries that in one line under *Bounded work*. |
| **`KICKOFF_GATE`** | **RETIRED**, after harvesting four things nothing else held: **two standing guards on CR's own language** — *manufactured/shadow/projection/artefact* mean built-by-construction-and-real, never *unreal*, and reading them conventionally **inverts the central claim**; and the horizon and centre are **topologically identical, not metrically identical**, with *"metrically identical" retired as false* — both now in `THE_PLAN`'s per-turn list, held until the ontology map is filtered and they can go onto the cards of the papers they protect. Plus ***prior reading earns you the index — where to look — never the extract***, into the per-turn list. Plus a **better check-in** than the README had: hand back the goal, where we actually are, **the failure mode you are most at risk of** named from the field note, and the consolidated picture. Its own corpus map was badly stale — fifteen papers, `p0/16`, a bundle from r795. |
| **`KICKOFF_CODA_REVIEW`** | **KEPT and INDEXED** — the presumption of retirement was wrong. It is a **reusable review methodology**, not a one-off: Pass A understand and stop, Pass B only after confirmation, four review questions plus one turned inward, three verdicts, a disqualifying test, and a receipt rule that voids any finding without a first-hand extract. In its own words, *"the gate is the coda, operationalized."* See §2. |

**So: all four kickoffs are resolved.** Three retired into the working set; one kept because it does a job
nothing else does. **The README replaces the spin-up function of all four.**

---

---

# 11 · ⌫ **DECIDED r1736** — *was "a thought, not a decision"* — this document as the home for consolidated outputs
*(Daryl, r1480: "we could think about it anyway. Without skipping to doing.")*
The suggestion: things that **draw consolidated coherence across the whole programme** — the dissolution
census, the ontology map, and their kind — might belong under this banner rather than scattered as
supplementary. They share a property nothing else does: each is *about the corpus as a whole* rather than about
a part of it.
**⚑ ANSWERABLE NOW, AND ANSWERED r1736 — and the objection has dissolved.** *The r1480 case **against** was
*"this document is scaffolding and retires; a home that retires is not a home."* **That premise is struck
(r1735): the document is not scaffolding, it is the only thing holding the work together at the highest level,
and it is nowhere near retirement.** So the only argument against is gone.*
**And the evidence r1480 lacked has arrived. There are now SIX documents of this kind, not two:**
| Document | What it draws across the whole | State |
|---|---|---|
| `ONTOLOGY_FOUNDATION_INDEX` | the **lens** — each forcing pinned once, 21 cards | live, ARC 2 |
| `THE_EVOLUTION_MAP` | the **ledger** — what is forced, in arc order p0→p17 | live, ARC 3 |
| `THE_DISSOLUTION_CENSUS` | every standard problem the corpus dissolves, graded by ontology-cost | **17/17 complete r1717** |
| `PHYSICAL_VALUES_LEDGER` | every computed value, its conventions, the ΛCDM comparison | live, SA-5 |
| `THE_WISDOM_LEDGER` | every operative scrap, filed by moment of use | live, 225 scraps, SA-6 |
| `ENTRY_POINT_REGISTER` | every gap the corpus advertises, in its own words | live, grain 0 |
**⌗ AND THE CENSUS'S GRADING HAS AN EPISTEMIC LIMIT, stated r1768 so it is not over-read.** *The **ontology-cost**
grading makes some entries **independent of the frame** — the ontology-free ones do not presuppose the layered
reading, which is why they are the ones an opponent cannot decline. **That escapes circularity. It does not
escape survivorship.** P6's boundary is the binding one: ***"self-consistency is not soundness — `lem:vindication`
is built from successes, survivorship not measurement."*** **A run of successes is not a base rate however
independent each success is of the frame** — so the grading sharpens **which** instances `THE_PLAN` A5.5's
reference class must be built against, and **does not stand in for building it.***

**⛭ THE ANSWER, and it is NOT to move them here.** *They share a property — each is **about the corpus as a
whole** — but they are **read at different moments** and moving them under one banner would break the thing
that makes each usable: the wisdom ledger is opened **at the moment of use**, the census **before claiming a
dissolution**, the values ledger **when quoting a number**, the lens and the ledger **while reading a paper**.
**A shared subject is not a shared moment, and filing by subject would destroy the filing by moment.***
**⌗ WHAT IS ACTUALLY OWED, which is what the r1480 thought was reaching for: they need to be NAMED AS A CLASS
and know about each other.** *Six documents doing one kind of job, each indexed separately, **none of them
saying that the other five exist or what distinguishes it from them** — which is SA-2's fourth shape exactly:
**two right things in their right places that do not know about each other.** *Entered as the class below,
with the distinguishing question each answers.*

---

---

# 5 · INDEXED RESOURCES
*A document that is read and kept — because it has a live job — is indexed here, with what it is and what it is
for. Being indexed is a job, not a status: a resource that turns out to have no job is retired instead.*

| Document | What it is | Its job in the programme |
|---|---|---|
| `KICKOFF_CODA_REVIEW.md` | A **review methodology**, not a spent task. Pass A: read the paper and write a faithful account of what it establishes; hand back and **stop** until the author confirms it. Pass B, only then: four questions — overreach · underreach · a live question walled off · phrasing fitted to convention — plus one pointed inward, *is this objection something my own Pass A already answers?* Three verdicts: flaw · standard-needs-adjusting · sound. A **disqualifying test**: a finding that requires denying what Pass A affirmed is void until reconciled. And a receipt rule: a finding whose receipt carries no first-hand extract with a locator is **structurally void, not merely weak**. | **LOWEST PRIORITY (Daryl, standing).** It was the first phase ever. Kept where it is; **not to be raised again.** |

---
