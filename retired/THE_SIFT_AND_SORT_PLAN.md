> **⌖ RETIRED r1550.** This was the plan for turning the unfinishedness catalogue into retired-vs-kept (r925). **It ran** — its product is `RETIRED_PLANNING_THREADS.md`, *"the survivors live in `THE_PLAN`"*, and its gate is the rule this consolidation rediscovered: *source-verified, not status-read-trusted*.
> Kept as record; **do not work from it.**


# The Sift-and-Sort Plan — turning the unfinishedness catalogue into an actionable plan

**Drafted r924 (c37) for Daryl's review before execution.** Input: `PROGRAMME_UNFINISHEDNESS_CATALOGUE.md` (the raw, un-sifted mess) + `THE_METHOD.md` (the procedure). Output (next turn, after your input): a sifted catalogue, a retired scrap heap, and one actionable plan-map. **This document is the review gate — nothing below is executed yet.** Read it, adjust it, then I run it.

---

## 1. The frame: this is the method pointed at the planning mess

`THE_METHOD` was built on the corpus, whose spine was *coherent* — so the method there ran as a completeness checker and came up dry (a proof-of-closure). The planning documents are the messier target the method was always meant to generalize to: they contain items that may be **incoherent when held against the current corpus and its map** — superseded plans, threads the programme already blew past, ducks that were parked and never adjudicated, and a few genuine standing contradictions. So here the same both-ways closure runs as a **coherence/contradiction detector**, and its failures are diagnostic: an item that won't reconcile with the corpus+map is telling us *which pile it belongs in*.

The three adaptations `THE_METHOD §6` flagged all bite here:
- **No keystone-first.** We can't cherry-pick — we sift the whole catalogue, because we don't yet know which items are the live spine of the *next* arc.
- **Restraint shifts meaning.** A "keep" isn't "this is done"; it may be "this is a genuine standing open thing we hold, unresolved." Some items are kept precisely *because* they're unresolved and honest about it (the data-gated tests).
- **Ducks generalize.** Some items are undrawable not because the geometry hasn't forced them yet, but because they're superseded or forced-both-ways. Those get *retired honestly*, not silently dropped.

---

## 2. The sift — keep / maybe / discard (liberal on keep, confident on discard)

Every catalogued item held against two authorities — the **corpus** (`.tex` at source) and **its map** (`CORPUS_MAP` current state + the §1-cards + `THE_EVOLUTION_MAP`). Three piles:

- **KEEP** — a genuine, still-open thread that coheres with the current corpus and represents real undone work or a real standing hold. *Bias: liberal.* When in doubt, keep.
- **MAYBE** — coheres but is speculative (off-runway), or its status is genuinely ambiguous, or it's a "held [reach]/eyes-not-hands" item. Kept, but flagged as not-yet-actionable; parked in a clearly-labeled holding pen so it isn't mistaken for live work.
- **DISCARD (retire)** — demonstrably superseded, already resolved, or incoherent against the current corpus. *Bias: confident, but never deleted* — moved to a **retired scrap heap** (`RETIRED_PLANNING_THREADS.md`) with a one-line reason and its source, so the record survives and any retirement is reversible. Retiring ≠ erasing.

**The gate for DISCARD is source-verified, not status-read-trusted.** The catalogue's STATUS-READ is provisional. An item is only retired when I've confirmed at source (in the corpus/map) that it's genuinely resolved or superseded. This is the "dig, don't grep / restraint" discipline: a report is not a check.

### 2a. A verification sub-pass first (the UNKNOWN / RESOLVED? items)

Before sorting, I resolve the items whose status the sweep couldn't determine — these are exactly where a wrong call would either bury live work or carry dead weight. Concretely, dig at source to settle:
- **B.1** overcritical low-point size law — computed r476 (CONJUGACY) or still open (OPEN_PROBLEMS C6)? Reconcile the conflict.
- **D.1** the α→∞ Schwarzschild-limit defect — did the Knows-Itself P3 edits retire it, or does it survive in P2/P3?
- **D.2** the [TERMS] seam/throat terminology overhaul — executed or not?
- **F.1** the dependency-matrix artifacts (LaTeX + HTML) — still lagging the renumber to 17 / missing P16?
- **F.5 / E.6** the lens WIP and the Track-F standalone papers — discharged via the Knows-Itself pass, or genuinely still owed?
- **G.1** the P13 cold read — does the c37 independent diagnostic discharge the certification gap, or is a fresh corpus-wide cold read still owed?

This sub-pass is small (targeted source digs, parallelizable) and it converts the biggest UNKNOWNs into clean keep/discard calls.

---

## 3. The sort — survivors into one actionable plan-map

The KEEP + MAYBE survivors sorted on the axes the programme already uses (the `OPEN_PROBLEMS_MAP` runway logic), re-cut for the current state:

**Axis 1 — actionability (can we move it now?).** Four bands:
1. **Buildable now** — a computation or construction inside established machinery we could start (e.g. explicit matter functionals A6.3; the seam-crossing worldline dynamics A2.4; the low-ℓ exact shape A1.2).
2. **Waiting on the world** — data-gated decisive tests where the honest move is to state the prediction sharply and wait (P1 no-horizons A1.1; the radiation-free-rate discriminator A1.4; the octopole verdict). These are *strengths to state*, not work to grind.
3. **Deep / gated** — the hard reaches gated on prerequisites (the quantum completion A3; the matter content A4; the grand claim past the wall A6.4).
4. **Daryl-led** — dissemination + judgment calls (the book, publication, the essays, face-science, the seat fork).

**Axis 2 — dependency (what gates what).** Draw the gating graph among survivors — the matter sector's content (A4) gates the interior remainder (A6.2) and the abundance derivation (A2.2); the quantum completion (A3) is downstream of everything. This is a both-ways closure on the *plan* itself: each item's prerequisites and its dependents, so nothing is scheduled before its gate.

**Axis 3 — kind (so unlike things aren't sorted together).** Physics-frontier vs contained-computation vs off-runway-speculation vs hygiene vs scholarship vs dissemination. The off-runway conjugacy cluster (C) travels as one unit; the hygiene items (D, F) are a separate low-priority lane that shouldn't compete with research fronts.

**The output of the sort** is a single **plan-map** — the survivors laid out by band × dependency, with the "runway" (buildable-now × high-impact) called out explicitly, the "waiting on the world" items collected as the standing falsification ledger, and the deep/gated and Daryl-led items as clearly-marked separate lanes. This becomes the successor to the stale `THE_PLAN` / `OPEN_PROBLEMS_MAP` runway — a current route from here.

---

## 4. Deliverables next turn

1. **`PROGRAMME_UNFINISHEDNESS_CATALOGUE.md` annotated** — each entry tagged KEEP / MAYBE / DISCARD with a one-line reason, post-verification.
2. **`RETIRED_PLANNING_THREADS.md`** — the scrap heap: every discarded item with its source and retirement reason (reversible record).
3. **`THE_PLAN.md` re-cut (or a new `THE_ACTIONABLE_PLAN.md`)** — the sorted survivors as the actionable plan-map (bands × dependency × kind, runway called out). *Which of these two — overwrite the stale `THE_PLAN` or write a fresh doc and retire the old — is a call I'd like your input on (see §6).*
4. A short **changelog entry (r925)** logging the sift-and-sort, stated for reversal.

---

## 5. How I'll run it (mechanics)

Foundation-first, mirroring the corpus passes: **verify (§2a) → sift (§2) → sort (§3) → log.** The verification sub-pass and the per-item source checks fan out as parallel source-digs (the same harness the catalogue sweep used), each returning a hard keep/discard verdict with a source citation; I synthesize the piles and draw the plan-map myself (the judgment that shouldn't be delegated). Restraint throughout: a clean "already resolved" is a verdict logged to the scrap heap with its receipt, not a silent drop.

---

## 6. Input wanted before I execute (the review gate)

These are the judgment calls where your steer changes the output — I'd rather have them now than guess:

1. **The off-runway conjugacy cluster (C).** Keep it parked as one holding-pen unit (my default), thin it to the few sub-items with the most teeth (e.g. C.9 exit-branch → branching ratios, C.3 coupling origin), or retire the cluster wholesale to the scrap heap? It's the single biggest keep/park/discard call in the sift.

2. **Dissemination + face-science (H).** In-scope for this plan-map as their own lane, or out-of-scope (a separate Daryl-led track that shouldn't sit in the research plan at all)?

3. **`THE_PLAN`: overwrite or supersede?** Re-cut the existing `THE_PLAN.md` in place (keeping its identity as the standing route-doc), or write a fresh `THE_ACTIONABLE_PLAN.md` and retire the old one to the scrap heap with a pointer?

4. **Discard confidence.** How aggressive on the DISCARD pile — retire anything source-confirmed resolved/superseded (leaner plan, my default given the reversible scrap heap), or keep a wider MAYBE penumbra (nothing retired unless it's incoherent, not merely done)?

5. **The certification / seat questions (G).** Are the cold-read and referee-vs-vision-seat items live decisions for this plan, or standing process matters to hold outside it?

Tell me where you land on these (or just react to my defaults), adjust anything else, and I'll run the verify → sift → sort and hand you the three deliverables.
