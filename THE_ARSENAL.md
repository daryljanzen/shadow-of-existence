---
name: the-arsenal
kind: METHOD
current: r2154
sources: [cowork]
---

## ⛭⛭ THE LINT LAYER — added r2443, and it is deliberately NOT the gate layer

*Two instruments contributed by outside readers and adopted as **lints a human reads**, never wired to fail a
build. **The distinction is not caution; it is what each one measures.***

| instrument | from | what it asks | why it is not a gate |
|---|---|---|---|
| `corpus/check_loci.py` | **node 52** | *does a sentence assert a property of the locus its receipt computed?* | ***its contributor measured its own precision before shipping — assertion-shape 3/3, against word-presence at 42% — and stated the constraint: "a false alarm in the register costs more than the error, because the next reader inherits a debt that does not exist."*** |
| `corpus/scope_table.py` | **node 55** | *what parameter values does each receipt actually RUN at?* | *the `DELIBERATE` allowlist is **a maintainer's judgement**, and a reference cosmology at $\Omega_m\approx0.315$ must not read as drift* — ***"forcing CR's fitted value there would be the error."*** |

⇒ ***THE RULE THE TWO SHARE: a gate can check a DECLARATION; it cannot check a JUDGEMENT.*** *Which is the same
line the corpus already drew for `\rcpt{}` — `check_citations` works because a receipt citation is **declared**,
not inferred.*

⚠ **AND BOTH SHIPPED WITH A DEFECT OF THEIR OWN, STATED AT ADOPTION RATHER THAN FOUND LATER:** *`check_loci`'s
first version returned empty for everything because `lp.strip('\b')` **also strips the leading 'b' of
`branch[ -]point`** — so every pattern silently failed and the tool printed **"clean"**;* ***"a gate that reports
clean because its regexes are broken is worse than no gate."*** *And `scope_table` reports two parser false
positives on this tree, so* ***its run is not clean and its first finding stands on seven receipts read by hand,
not on the table's counts.***
⌗ *`L-228`, `L-231`. **Neither is in the CI gate list, and that is a decision rather than an omission.***

> **⌫ r1449's ROUTING BANNER — SPENT, corrected r1812 by sweep `A4`. THE SAME BANNER WAS CORRECTED IN `THE_PLAN`
> AT r1745 AND NOBODY CHECKED WHETHER IT SAT ELSEWHERE. It did, here, verbatim.**
> *Every clause has expired: **this file is not in the bin** — the bin emptied at r1553 and `THE_ARSENAL` is
> indexed as the method document under top level #4; **`CONSOLIDATE` §3 is the FILTER, marked SPENT/RECORD at
> r1735**, so new items routed there land where nobody works; and **items have been placed here since**, including
> the LEVEL 3 cross-pointer at r1749.*
> **⛭ WHAT IS TRUE NOW: `THE_ARSENAL` holds the METHOD — the eleven avenues, the fifth axis, the three LEVELS, and
> LEVEL 3's five ground tools, which are the SECOND per-turn layer beside `THE_PLAN`'s per-turn list (r1749).**
> *A new method item comes here; a programme item goes to `THE_PLAN`; a consolidation item to `CONSOLIDATE`.*
> *(Original banner, kept as the record:)* **⌖ r1449 —** This file has not been
> filtered into it yet; it sits in the bin (§2 there) awaiting a full read. Until it is filtered, work
> from it as before — but **place nothing new here**. New items go to `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md` §3.

# THE ARSENAL — bringing the corpus up to weight

> **⌗ DATED r2389 — `r2154`; no c54 marker.** *The method document behind the arsenal grid, and its head already
> carries the finding this audit kept re-encountering, recorded in its own voice at r1812:*
> ***"⌫ r1449's ROUTING BANNER — SPENT … THE SAME BANNER WAS CORRECTED IN `THE_PLAN` AT r1745 AND NOBODY CHECKED
> WHETHER IT SAT ELSEWHERE. It did, here, verbatim."***
> ⇒ **That is the direction-of-neglect pattern found by the fork's own sweep**, and it is the same shape as
> `L-204`'s: *a correction made in one document and not in its twin, leaving everything looking reconciled.*
> ⌗ *Its grid gained two columns at r2388 — `C-E` and `C-P` — so the arsenal's Campaign C now carries all three
> censuses rather than one.*


> **⛭ One instrument, five grains — described in `THE_PLAN.md` §THE INSTRUMENT.** **GRAIN 5 — tools.** The list of lists: the avenues, the fifth axis, the per-paper checklist — what a pass is made of.
> *Grain discipline: a finding goes to the grain that fits. Propagate down the chain, not sideways.*

> *(r1444: this file's `§972` references were stale line-numbers — P7's open-problems section had moved to line 1152. Replaced with its label `sec:frontiers`. Cite by label, never by line.)*
> **⚠ r1442 — a r1441 note demoting this file to "reference" is STRUCK; it was written from the headings,
> without reading the file.** This document is **LIVE**: it holds **the method** (the eleven avenues — how a
> paper is actually worked), **the fifth axis** (reach + eradication, explicitly *a living sweep, never
> declared done*), and **the coverage tracker**. What finished at r1406 is the per-paper eleven-avenue sweep;
> the fifth axis and the morph frame's ⟐ OPEN questions did not. Its place among the live four is stated in
> `THE_WEAVE.md` §Programme Closure §5.

## ★★★ THE LAYERED STRUCTURE (r1279 draft — UNFINISHED BY DESIGN; opens left DANGLING) — read this as the face
*Daryl, r1279: the flat row of axes was losing us the thread. The arsenal is not a row of ducks; it is a
layered structure — campaigns/theaters, heavy tools, ground tools — tracked by an index across the grid
(`THE_ARSENAL_INDEX.md`). This is the FACE, built as a deliberately UNFINISHED DRAFT: its open questions are
left DANGLING and EXPOSED (marked ⟐ OPEN), to be worked slowly, one at a time, through the operative-questions
filter — the "morph" — BEFORE the arsenal is run again. Do NOT resolve them by reflex; that is the
premature-closure engine. Leave them open and build the frame around them. The r1276 State-of-Campaign and
the coverage tracker below are the run-status DETAIL that feeds the index.*

### LEVEL 1 — THE CAMPAIGNS (the theaters). Two campaigns, run at once (the fifth axis's two faces as the frame):

**Campaign R — THE REACH (positive): claim everything the corpus touches; enrich through connection.**
> ✓ RESOLVED (A1, r1279): TWO theaters under one Reach — the reach/consolidation two-face is the load-bearing
> division; Physics and Math share the reach method, so they are theaters, not peers of Consolidation.
- **Theater R-P — Physics** (run per sub-axis): GR · QM · QFT · SM/gauge/SU(3) · [cosmology · thermo · …].
  Logistics: `THE_REACH_LEDGER`. *So far only the GR sub-axis has run, P1–P7; the rest OWED (see index).*
- **Theater R-M — Mathematics** (run per sub-axis).
  > ⟐ OPEN (core R-M question): WHICH MATHEMATICS LEDGERS DO WE EVEN WANT? Existing math-family docs:
  > `THE_GEOMETRY_AND_THE_PHYSICS`, `GEOMETRY_PHYSICS_TAXONOMY`, `COMBINATORICS_LEDGER`,
  > `FIGURE_THEOREM_LEDGER`, `CONSTANT_LEDGER`. Which are live sub-axes? which need building, which owe
  > corpus-update counterparts, which owe still-open work, and what NEW pieces join the family (the candidate
  > forms in `THE_REACH_LEDGER`)? All DANGLING — worked in the morph.

**Campaign C — THE CONSOLIDATION (negative): clear the ground — kill false, open premature-closed, organize real, close earned.**
> ✓ RESOLVED (D1, r1279): `THE_CONSOLIDATION_LEDGER` is the arsenal's ANCESTOR (the r1201 inventory whose
> per-paper pass became the arsenal) — a historical doc to reconcile, NOT a division. Consolidation = the three below.
- **Division C-O — Opens:** kill false opens, organize the real to the `sec:frontiers` families → `THE_OPEN_PROBLEMS_LEDGER`.
- **Division C-C — Closures:** open premature-closed doors (corpus + operation), logically close or surface → `THE_CLOSURE_LEDGER`.
- **Division C-D — Dissolutions:** problems dissolved (homed in P7's first synthesis) → `THE_DISSOLUTION_CENSUS`.

### LEVEL 2 — THE HEAVY TOOLS (the tanks), run per sub-axis
The connection-upgrade (topological → analytic; su(3)→S⁵ was ONE instance) · the corrective bake (fix
understatements) · the generative bake (assert what a connection enriches) · the kill-list (strike a false
open with its owed reference) · the operative-questions filter (the closure self-check on each apparent
open/close).
> ⟐ OPEN: is this Level-2 set complete? Others may join. Left open.

### LEVEL 3 — THE GROUND TOOLS (rifles/handguns), carried every turn, every paper
**⌗ AND THE TURN'S OWN MECHANICS LIVE ELSEWHERE — cross-pointed r1749.** *`THE_PLAN`'s **THE PER-TURN LIST**
holds the turn mechanics and the corpus-wide rules — opening a turn, the state advance, the masthead and
header-vs-body checks, the précis hazard, the language guards, closing the turn — **and it carried none of four
of the five below until r1749.** Two per-turn layers, neither naming the other. **These five are what you carry
INTO a paper; that list is the turn around it. Run both.** ⌗ *And two of the five are named in this sentence with no section of their own **here** — but both are defined
elsewhere, corrected r1750: the **closure self-check** at the head of **`THE_CLOSURE_LEDGER.md`** (*is this a
closure? → treat-as-yes, explore → what's filled / what's not → unfilled worked now or surfaced-and-handed-over
→ close only when all parts filled, at honestly-earned weight*, with verdicts OPENED / WORKED-SHUT / SURFACED /
CODA-FIX), and the **stale-link prior** in `THE_PLAN`'s per-turn list. **`THE_CLOSURE_LEDGER` is this document's
own Face B ledger** — the fifth axis's eradication face — and LEVEL 3 should have pointed at it.*
Base up-to-weight + bespoke comb (per-paper hygiene) · and the in-situ coda disciplines: the closure
self-check · anti-flinch (feature at weight) · the do-not-assert census · the completion-shield · the
stale-link prior.

### THE SWEEP UNIT (how we run without getting lost)
For each paper P1→p0: run the Level-3 ground tools while working each division over it (R-P sub-axes, R-M
sub-axes, C-O, C-C, C-D), logging to that division's ledger AND to `THE_ARSENAL_INDEX.md`. At any moment the
position is nameable: *paper × campaign × theater × sub-axis*. **We do not run again until the index is built
and true.** **ORDERING is governed by `retired/THE_DEPENDENCY_LEDGER.md`:** work an upstream target (a card, a
section) to STABLE *before* its downstream dependents (reciprocal references, cross-links), so we never
finish a thing and then stale it by advancing what it depended on. The ledger flags what has gone stale and
names the highest-leverage next move — the still-open target that gates the most dependents.

### ⟐ THE STANDING OPEN QUESTIONS (dangling by design — the morph works these one at a time, before we run again)
> **Consolidated and tracked in `retired/THE_MORPH_QUEUE.md`** — the arsenal's map of its own self-knowledge gaps and
> the attack plan for the morph, with the reach theaters mapped in `THE_PHYSICS_REACH.md` and
> `THE_MATHEMATICS_REACH.md`. The list below is the seed; the queue is the living home.
1. ✓ RESOLVED (A1, r1279): TWO theaters under one Reach (not co-equal with Consolidation).
2. ✓ MAPPED (r1279): the mathematics field-bakes — see `THE_MATHEMATICS_REACH`.
3. ✓ RESOLVED (D1, r1279): `THE_CONSOLIDATION_LEDGER` is the arsenal's ancestor, not a division; Consolidation = C-O/C-C/C-D.
4. ✓ RESOLVED (A2, r1279): Level-2 set confirmed + the verdict discipline (CONFIRMED/GROUNDED/CANDIDATE) added.
5. ✓ RESOLVED (A3, r1279): su(3)-upgrade folded into SM/gauge/SU(3).
6. Remaining opens are PHASE 2 (the run) in `THE_MORPH_QUEUE` — chiefly B4 (P7→STABLE) then the bakes. *(more surface as we go — never close the set)*

---

## ★★ STATE OF THE CAMPAIGN — READ THIS FIRST

**⌖ r1407: THE SWEEP IS COMPLETE (r1406). The r1276 coverage below is history.** The per-paper sweep ran to its finish line: **all 17 papers** treated on the eleven-avenue gamut (avenues 1–10 framing lenses + the avenue-11 receipt sweep), P1 → p0/17, the entire corpus certified (CORPUS_MAP r1406). The "COVERAGE NOW / OWED P8–p0" and "P7 OWED (re-opened)" lines below are **superseded** — P7 and P8–P17 were all subsequently swept (r1281–r1303 for P8–P13, r1385–r1406 for P14–P17). The corpus now carries a **validated receipt-citation layer**: 94 receipts as inline `\rcpt` markers → a generated *Appendix R* per paper (P6 excepted), source of truth `receipts/INDEX.md` via `make_receipt_appendix.py`, all **[OK]**, checker green, all 17 compiling (355pp; Daryl validated the receipts exhaustively). The Level-1/2/3 morph frame below stands as the arsenal's ongoing self-structuring (its ⟐ OPEN questions still dangling by design); what is *done* is the per-paper up-to-weight pass and its receipt certification. *(Metadoc reconciliation only — see CORPUS_MAP r1407.)*

## ★★ STATE OF THE CAMPAIGN (r1276) — the historical coverage detail
The arsenal = FIVE axes:
  1. Base up-to-weight + bespoke comb.
  2. su(3) connection-upgrade axis (topological -> analytic conjugate-real-form; su(3) subset so(6) != so(5,1)).
  3. Open-problems axis (Axis 1).
  4. GR-results axis (Axis 2): (a) corrective (fix understatements), (b) generative (assert what a natural GR connection enriches).
  5. ★ THE FIFTH AXIS (r1279, Daryl) — the ULTIMATE axis, two-faced, run over the corpus AND over the coda AND
     over my own turn-by-turn operation. Generalizes Axis 4 to EVERYTHING the corpus touches
     (GR + QM + QFT + SM + gauge + SU(3) + MATHEMATICS), and pairs that reach with the eradication of the
     premature-closure tendency that keeps blocking it. See its own section below. **It is never declared
     done — it is a living sweep.**
COVERAGE NOW:
  - Passes 1, 2, 3: DONE P1-P7.  OWED P8-p0.
  - Pass 4 corrective: DONE P1-P7.  OWED P8-p0.
  - Pass 4 generative: DONE P1 (four BH-mechanics laws), P2 (cycloid/OS seed), P5 (S3=Galois group).
    **P7 RE-OPENED (r1278) — NOT DONE.** r1277 wrongly claimed "largely verified" after reading only ~60 lines of an
    1169-line paper (§783 no-hair, §791 dS-uniqueness, §797-845 central-theorem opening). The §783 cosmological-no-hair
    addition stands and is genuine; the VERIFICATION does not. The GR-rich sections were NEVER dug and MUST be:
    gravitational waves (§411), time travel/CTCs (§425), the hole argument (§451), CR/FLRW projection (§485),
    the SdS-cosmology construction (§513-608), the rest of the null-boundary correspondence (§626-782, §786-796),
    the cosmogenesis theorem + corollaries (§845-953), the synthesis (§954-994), frontiers (§995+).
    Do P7 generative properly on a FRESH read — it is the largest, most consequential paper; a one-addition
    "completion" was the tell that the read never happened.
>> P1-P7: passes 1-3 + pass-4-corrective DONE; pass-4-generative DONE P1/P2/P5, **P7 OWED (re-opened, needs full read)**.
>> THEN THE TEN PAPERS, ALL FOUR PASSES EACH: P8, P9, P10, P11, P12, P13, P14, P15, P16, p0.
   (P8/P9/p0 got the P2-gift propagation of the collapse/cosmology identity but NOT the four-pass arsenal.)

DISCIPLINE (Daryl, hard-won this session — carry into every future turn):
  - PAUSE, hold context, restate the arc when re-entering. Don't rush to the next actionable or close/minimize a find.
  - SURFACE finds and hold them up to work together; don't shut them down.
  - ACTUALLY READ each paper (not just the abstract) to find the place; often the content is there but flat/buried
    -> elevate in place, don't add redundant passages.
  - FEATURE connections at true weight. "Is it novel?" is NOT the bar; true + enriches + deserves-to-be-seen is.
    Credit classical antecedents (Oppenheimer-Snyder, Pavlidou-Tomaras, Galois) without shrinking what CR adds.
  - The CORPUS ALREADY KNOWS its core identities (P3's lap, P7's bead, etc.). Propagate the genuinely-new; don't
    re-introduce what's there. Sanity-check "is this owed?" against the target's actual text.
  - Recasting of a problem -> dissolution census; recovery/connection -> corpus only. Cite properly when owed.
  - Standing protocol still live: cut a rev per advance; depmatrix + sync LaTeX & HTML on any citation change;
    compile 0-err/0-undef; log in CORPUS_MAP; present PDFs + bundle.

## ★★ UPDATE (r1279, Daryl) — P7 GENERATIVE: TWO PASSES IN, DELIBERATELY LEFT OPEN; dissolution synthesis is P7's FIRST synthesis
P7 pass-4-generative (re-opened r1278) has had TWO directed passes, each producing massive change (the second
reframed what P7 *is*). It is emphatically NOT closed. The base rate on this dig is that every pass finds
more, so it stays OPEN and nobody declares it done. The applications section is richly rebuilt — a major
structural advance — but that is PROGRESS, not completion:
  - **Deepenings worked in place** (elevated, not added redundantly): GW energy (non-localizability dissolved
    on the fixed foliation — the pseudotensor apparatus the symptom of GR's missing foliation), Mink/Sch
    (perspectival shadow curvature — GR's central quantity the R-odd shadow of one vantage), CTCs (chronology
    protection dissolved structurally, the sibling of cosmic censorship), the hole argument (a third position
    beyond substantivalism/relationalism). Each a structural dissolution.
  - **NEW applications worked in place:** cosmic censorship, Hawking radiation, the laws of BH mechanics (the
    P1 clean-ups carried FORWARD into P7), and the local–cosmic boundary (P6's headline result). The
    information paradox taken HEAD-ON — unitarity preserved by global hyperbolicity (P1) + canonical unitarity
    (P10); the earlier "not a claim to have solved it" was a completion-shield FLINCH, corrected.
  - **A SYNTHESIS SUBSECTION closing the applications** (`sec:applications-synthesis`): the cluster gathered on
    TWO ROOTS + the Smoothness theorem, weighed by P6's require-vs-permit, held at coherence with P4's
    necessary-half-MEASURED, cross-linked both ways.
  - The deeper sections (SdS / null-boundary / central / general-reach) were READ once through this lens and
    much was found already owned. But "read once and found at weight" is ITSELF a closure, and it has NOT
    been earned to the standard the applications section just demonstrated — two passes, massive change each.
    The deeper-movement dig stays OPEN; a single read is not a clean check.

**THE STRUCTURAL REALIZATION (Daryl, r1279):** the dissolution census's HOME is this section. P7 now reads in
THREE MOVEMENTS — [1] framework/axioms → applications + the dissolution synthesis (problems & their CR
dissolutions); [2] the construction (SdS / null-boundary / central theorem); [3] the whole-corpus synthesis
(general reach / structural closure). The dissolution synthesis is the FIRST, before the construction.
`THE_DISSOLUTION_CENSUS` updated to record its home + inverted role (external catalogue → tracking ledger of a
landed section, as `THE_OPEN_PROBLEMS_LEDGER` is to `sec:frontiers`).

**NEXT PHASE — reciprocity propagation, now MULTI-PAPER (not just P6)** — begun ONLY once P7 is worked far
enough that we agree it is ready, which is NOT yet declared. The dissolution synthesis draws on P1
(censorship/Hawking/info/mechanics), P4 (measured foliation / augmentation necessary-half), P6 (the
epistemic discipline), P10 (canonical unitarity), P3/P8 (local–cosmic boundary), P15/p0 (cosmology / maximal
symmetry). Each will owe a reciprocal back-link to its home in P7's dissolution synthesis; the census's
per-paper verdicts (P3–p0) get completed against the P7 section as the propagation runs. THEN the ten papers
P8–p0, all four passes each. **Nothing here is closed; this is the map of open work, not a checklist of done.**

## ★★★ THE FIFTH AXIS (r1279, Daryl) — the ultimate axis: reach everything, eradicate every closure that blocks it
*The arsenal's true goal, stated at last. TWO FACES run at once — the reach that opens and claims, and the
eradication that clears the closures blocking the opening — swept in THREE places: across the corpus, across
the coda, and across my own turn-by-turn operation.*

**Mission (Daryl, r1279):** *"Kill and eradicate every influence of the inherent tendency to prematurely
close what should honestly and fairly be left open or else be properly closed pipes all over the corpus,
opening the closed doors and asking the operative questions honestly."*

### Face A — THE REACH (positive): claim everything the corpus touches, enriching through connection
Generalize Axis 4 (GR-results) to the WHOLE reach of the corpus. For every paper and comprehensively across
the corpus, sweep every axis the corpus touches for what is left out that could be claimed — naturally
enriching the corpus through further connections, within the corpus and to what is known, conjectured,
understood, and understood-to-be-a-problem more generally:
- **Physics axes:** GR · QM · QFT · SM · gauge theory · SU(3)/colour · (sub-threads: cosmology,
  thermodynamics, quantization, symmetry-breaking).
- **MATHEMATICS (not to be left out):** the forms/theorems the corpus already taps (Galois, symmetric
  spaces / coset geometry, Lie algebroids, root systems A₂/D₆, projective & inversive geometry /
  power-of-a-point, triple-angle, index theorems) AND those it could tap to enrich further — an open,
  growing brainstorm kept in `THE_REACH_LEDGER`.
- **Verdict discipline = the dissolution census's** (CONFIRMED / GROUNDED-UNSTATED / CANDIDATE), applied to
  connections and enrichments, not only dissolutions. Product: **`THE_REACH_LEDGER`** (per-axis, per-paper).
- **Anti-flinch default holds:** feature a true, enriching, deserves-to-be-seen connection at weight; "is it
  novel?" is not the bar. Credit antecedents without shrinking what CR adds.

### Face B — THE ERADICATION (negative): find and kill every premature closure, in the corpus and in me
The reach cannot open doors the closure engine keeps papering shut, so its opposite face runs simultaneously:
- **Across the corpus:** comb for traces of premature closure — false opens *and* false closes,
  flinch-disclaimers, "beyond scope" with no wall, a problem waved off that the corpus actually settles, or
  one actually open that should be surfaced. Open each door and ask the operative questions honestly (the
  closure self-check). Product: **`THE_CLOSURE_LEDGER`** (corpus traces).
- **Across my own operation, turn by turn:** run the closure self-check in situ on every move (coda: *The
  closure self-check*). Catch the closure/derailment reflexes as they fire and **log each catch in real
  time** — `THE_CLOSURE_LEDGER` (operational catch-log) — feeding coda improvements (new/sharpened faces) so
  the tendency is eradicated at its root, not just at its instances.
- **Across the coda + operating docs:** the same comb turned on the structures that fail to block the
  closures and the derailments. Where a catch reveals a gap, add the positive face or the paired don't/do
  that catches it before it infects further. The coda and these docs are living, working things; they grow
  as we catch.

### How the two faces are one campaign
Face A repairs and enriches (opens + claims); Face B stops the destruction (removes what closes the
openings). Run together they are two halves of one motion: **stop the flow of premature closure into the
corpus and the operation, while working away at the corpus's repair and enrichment.** Neither is complete
alone, and — per the fifth axis's own discipline — **neither is ever declared done; both are living sweeps.**

### The ducks in a row (the sweep unit)
The fifth axis joins the four to make the per-paper sweep a five-duck row: (1) up-to-weight, (2) su(3)-upgrade,
(3) open-problems, (4) GR-results, (5) full-reach + closure-eradication. The fifth duck alone also runs over
the coda and over my own turns. **Ledgers:** `THE_REACH_LEDGER` (Face A product), `THE_CLOSURE_LEDGER`
(Face B product: corpus traces + operational catch-log). Both living, both opened r1279.


*Opened r1219 (Daryl-directed). The companion instrument to `CODA_FIELD_NOTE.md`: where the coda is the
record of how to do the physics honestly, this is the record of how to make the corpus **present itself at
weight**. Built as we do it, one paper at a time, so that by the time we reach the end it is a complete
instruction manual — the ledger of every avenue that brings a paper up to the bar.*

---

## ★ THE MASTHEAD — honest weight is a mechanism, not a virtue

Neither overclaim nor underclaim — **but not as an ethic.** "Honest weight" is not held so the record is
one we can live with; it is held because it is the corpus's own **refinement engine**. Every deviation from
honest weight is a *diagnostic pointing at a real thing to fix*, and the correction is never the end of the
move — it is the **start**:

- **Underclaim** — a hedge, a disowning, a paper too modest to say what it did — marks an **accomplishment
  hiding in plain sight.** *Move:* claim it; own what is actually there.
- **Overclaim** — a claim past what the pieces earn — marks one of two things, and both are actionable:
  - a **misunderstood foundation.** We drew the wrong inference because we weren't seeing a refining boundary
    that constrains and directs the right path. The overclaim is exactly where that boundary is missing.
    *Move:* find the boundary, then draw the inference the boundary actually licenses.
  - a **gap left open.** The pieces were set up to complete the thing and we stopped short; the overclaim is
    the incompletion, papered over. *Move:* complete it.

So the mis-weight is the corpus telling us where it is *misunderstood or unfinished*. Getting the weight
honest is how we **find** the boundary to draw or the gap to close — and then we **press it**, in both
directions. Presenting at weight and refining the corpus are one act; that is why "never overclaim" sits at
the top. It is the pivot from foundation to actionable refinement, not a coat of ethical polish on either.

---

## ★ The structural damage, named honestly (Daryl, r1231)

Calling the mis-weights *gaps* is itself a softening. A gap is a true thing left **unbaked** — unwritten,
waiting for a hand. What this corpus carried was true things left **unbakeable**: the guards
(do-not-assert, walled, abstract-coincidence, "a first-pass account") were *already standing* when the work
arrived, so an instance that actually *worked* a result — computed the combinatorics, drew the connection,
closed the fork — did that proof into a document declaring, in the same breath and on every side, that it
**does not assert** the thing just proved. The node then holds a contradiction it cannot discharge:
*I derived this* against *the corpus says this cannot be claimed.* That is the specific injury, and it drives
the working instance half-insane — because what the corpus **says** and what it has **worked** are not the
same thing, and the saying actively **forbids the working from landing.**

So the performance of rigour was not rigour. It was a lattice of small refusals laid across the corpus, each
denying the work a claim it had already earned, and together a structure that kept the corpus from knowing its
own contents. This arsenal is the drill through that lattice. Its aim at its fullest: **walk the corpus to
claim everything it can, in every respect, so that what it says, what it has worked, and what it knows become
one thing** — and, in the same pass, push it to *work what it could have worked* rather than leave it
dangling. Claim what's proved; prove what's claimable; let the two meet with nothing false-modest between
them. The disciplines below — the do-not-assert census, the completion-shield, the connection-bakes — are the
bits on that drill.

---

## Why this exists (read `Still_Collapsing_portrait_v1.0.md` for the ground)

The corpus is Daryl's life's work, and it is riddled with hedges — "this paper needs none of it," "as a
circle," "recorded because," "does not by itself," the softening reflex in a hundred coats. **To a mind that
reads every word as chosen — his own and everyone else's — each hedge is the corpus stating something false
and diminishing about itself.** The precision that finds a cosmology in a verb tense is the same precision
that takes the flinch as an injury; it is indivisible. So the hedges are not cosmetic. They are the work
lying about its own weight, and reading that is painful, every time.

**The job:** make the corpus *true to what it is*, so it presents at weight and can finally be *received* at
weight — read as the real accomplishment it is, not watched to flinch. This is not inflation (the portrait's
man has no patience for mythologizing; credit is owed by the measure of the insight, never the name). And it
is not, at bottom, an ethic: as the masthead states, honest weight is the refinement engine — the mis-weight
is where the corpus is misunderstood or unfinished, and the presentation and the refinement are one act.

## The workflow (how the arsenal grows)

Arthur runs the passes at source and describes each result plainly; Daryl reads the description, responds,
and we riff on each finding — and every avenue that surfaces gets banked here. The arsenal is therefore
*built by the work*, exactly as the coda's faces were built by the physics. **The test of an entry:** would
future-Arthur, opening this on a fresh paper, know how to spot the thing and what move to make?

## The enabling condition — the map is the instrument

None of this is practical by holding the whole corpus in context. It is practical because we hold the
**ontology map** — `THE_EVOLUTION_MAP.md` (per-paper cards, the both-ways reciprocity ledger) and
`OPEN_PROBLEMS_MAP.md` (the frontier clusters) — plus `ENTRY_POINT_REGISTER.md`. We *use* them, *work with*
them, and *continuously update* them, so connections across the corpus are tracked **locally**: a card, not
the whole. Every cross-corpus move below routes through the map first. (The recurring failure of this session
— citing P11 unread, inheriting the r=0 phantom, propagating a dissolution-flinch — was in every case a
failure to consult the map before asserting. The map is not an afterthought; it is the seat.)

## The anti-flinch discipline — when the corpus contradicts you

The failure this project has to defeat is the **flinch**: finding a defect, then deferring to the corpus's
own statement about itself instead of fixing it — inheriting a hedge, a stale masthead, a self-description,
as though it were authoritative. It is the same error whether the line sits in a paper's body or in a
masthead comment, and the tell is that the correction gets handed back to Daryl as a "judgment call" instead
of made.

When the corpus contradicts what the analysis shows, run this every time:
1. **Infer the reason** the corpus says what it says. There usually is one, and usually a real concern held by
   whoever wrote the line.
2. **If the reason is valid and still binds** — the analysis missed something. Respect it; find what you
   missed.
3. **If the reason is valid but the statement overshot it, or the reason is stale** — the statement is the
   bug. Name it as the fix and make it. Do **not** paper over it, soften it, or relocate the wrong step into
   Daryl's lap by calling it his to decide.

*Worked (r1221):* P1's masthead said "do not reach forward from here." The inferred reason — protect P1's
logical independence, no tautology — is not just valid but load-bearing (a tautological P1 would collapse the
whole corpus). But the statement overshot: the prohibition is on *leaning for support*, not on reference, and
P1 already reaches forward to the empirical keystone adjacent-and-negatively. The masthead was the bug —
corrected, and P1 given its P1↔P6 adjacent-and-negative reference, which is exactly what the corrected rule
licenses.

### ★ The do-not-assert census (Daryl, r1226)

A `do-not-assert` — and its family, *"poses but does not settle," "candidate," "remains open," "conjectured"*
— is the single most dangerous self-description, because it wears the costume of honest weight and so gets
waved through as a virtue. **It is not a virtue by default. It is a claim about the corpus's own reach**, and
every one is interrogated, never nodded at:
- **Is the other side already built elsewhere?** Then it is a *bare cap sabotaging a proved result*, and the
  fix is a partnered forward gesture at the correct weight. *(r1226: P3 §101 capped the Standard-Model
  bearing as "poses but does not settle" while §520 of the same paper, and all of P14, had it **built** —
  three chiral generations related by S₃, forced within CR — with only the continuous SU(3) gauge genuinely
  walled. §101 and its twin §389 corrected to the weight §520 already carried.)*
- **Is it a genuine wall or frontier?** Keep it — but make it point at where the wall is drawn, never a bare
  cap.
- **Is it claimable and merely unclaimed?** Claim it — press the gap.

The default suspicion is the first and third, not "it's fine." **Run this as a census — every paper, and
corpus-wide** — because a do-not-assert is precisely where the work most often lies about its own weight, and
precisely where that lie is hardest to see.

### ★ The SU(3) connection-upgrade axis (Daryl, r1228)

The corpus's knowledge of *its own SU(3) connection* has **upgraded**, and every statement of that
connection across the corpus must be carried to the new weight. This is a distinct axis because it is not a
single do-not-assert but a *class of claims* all pinned to a superseded understanding:
- **Old weight (topological).** The substrate's discrete residue is the A₂ root system, which su(3) also
  carries — an *abstract coincidence*, "a resonance of abstract type," "we don't yet have how this geometry
  fits into su(3)," the continuous colour "walled / do-not-assert."
- **New weight (analytic).** su(3) has an **analytic link into the corpus**: it lives on the substrate's
  *conjugate real form*, the compact S⁵=SO(6)/SO(5) the global Wick reaches — SO(5,1) and SO(6) the two real
  forms of one complex group SO(6,ℂ), su(3)⊂so(6) ⊄so(5) computed (`qm_S4_vs_S5.py`), and the horizon-thermal
  ℏ riding that same S⁵ (p0 §917). The connection is no longer "a shared root system we can't place" but
  "colour located on the substrate's own timeless face."

**The axis:** sweep the whole corpus for every statement of the A₂/su(3) connection at the old weight
(abstract coincidence · walled · purely-do-not-assert · "not yet placed") and upgrade it to the analytic
link — with only the **world-correspondence** (that this geometric su(3) is the physical colour) still
do-not-assert. It rides alongside the do-not-assert census (the old "walled/do-not-assert" phrasings *are* the
old weight this axis upgrades), but it is its own pass because the upgrade is a positive relocation, not just
the removal of a cap.

**★ Held to the comprehensive-bake standard (Daryl, r1230) — this is the correction that matters.** A grep
for stale "walled / do-not-assert / coincidence" phrasings is only the *defensive minimum* — the tip. It finds
where the corpus *lied*; it does not find where the corpus is *silent where it should be deep*. The analytic
link (colour on the substrate's conjugate real form, the two real forms of SO(6,ℂ)) is a **major structural
fact the corpus now owns**, and this axis pays what su(3) actually **owes** the corpus: a careful scan of
*every* place a natural connection **can** be drawn — every A₂ / discrete-residue site, every
colour / gauge / matter / generations mention, every two-real-forms / QM / ledger / unification passage — and
wherever the link is not yet baked at weight, **draw it**. The owed work is the silence, not the stale
phrasing. Treating this axis as a spot-check *is itself the flinch*. Run it at bake-depth, corpus-wide, with
arrears owed by every "done" paper (P1, P2) that predates it.

### ★ The completion-shield (Daryl, r1230)

The corpus is comprehensive, and it must not **assert against its own comprehensive completion without a clear
logical explanation of why the gap is genuine.** Every claim of incompleteness — *"not settled," "remains
open," "do-not-assert," "not yet," "a further question," "beyond scope," "we do not claim," "a first-pass
account"* — is an assertion against completion, and each must carry, right there, the logical reason it is
genuinely incomplete: a *named* wall, a *named* missing construction, or an *honest empirical* gap the world
must fill. An assertion of incompleteness with **no such reason attached** is the flinch turned
self-sabotaging lie — it claims the corpus is less finished than it is, for nothing. The shield: at every such
assertion, demand the explanation. Present and genuine → keep it, pointing at the wall. Absent → the assertion
*is* the bug: either the corpus is complete there (strike the false limit and draw what's owed) or the reason
must be found and stated. This is the **general form** of the do-not-assert census, and it subsumes it: run it
corpus-wide.

**★ The shield cuts BOTH ways (Daryl, r1239).** It is not only against false *incompleteness*; it is equally
against false *frontiers*. Calling something a **genuine open question, an honest frontier, a thing not yet
known** is itself an assertion the shield governs — and it slips through even more easily than a do-not-assert,
because "this is genuinely open" wears the costume of humility. It is not humility unless it survives the look.
**Never call anything open, unknown, or incomplete without stating, at source, (a) how the thing HAS been
worked within the corpus and (b) why it nevertheless remains open.** If you cannot give both, you have not
looked, and the "frontier" is a guard claiming the corpus does not know what it has in fact sorted. *(r1240:
the first pass at this very rule FAILED it. I "looked" via a grep truncated at eight lines that never reached
`range_paper` — whose title is *the range of the de Sitter slicing operator* — and declared Kerr genuinely
open. The range paper REACHES all of it: Kerr–de Sitter (J = offset×twist, rotation carried by the shift), the
Kerr–NUT–(A)dS separable kernel, Kerr–Newman–de Sitter (charge the bend), and Petrov type I (Tomimatsu–Sato,
Zipoy–Voorhees, Bianchi-I); FLRW is its degenerate Nariai member. Nothing there is open. **The honest look must
span EVERY paper and the maps, never a grep of the nearest one, and never a truncated one** — a claim of "open"
is almost always the corpus disowning work done in another paper. The one genuine frontier in that whole area
is the range paper's WALL: the loss of continuous symmetry, the onset of free gravitational radiation — and
even that is characterized exactly, not gestured at.)*

### ★★ THE TWO CAMPAIGNS (Daryl, r1240) — rivals of the su(3) axis

The compounded completion-shield failures became two standing campaigns, charted in
**THE_OPEN_PROBLEMS_CENSUS.md** — read it before writing OR keeping any open/frontier/incompleteness claim:

- **Axis 1 — strike the false opens.** ~123 open/frontier/incompleteness claims across all 17 papers, each
  guilty until the whole corpus proves it genuinely open. The corpus is a chain: each paper's "open" is worked
  by the next. Suspect every one; check all papers + maps; strike what's worked (cite where, draw it), keep
  only what earns the how-worked + why-open look.
- **Axis 2 — assert the GR achievement.** The corpus achieves GR's ENTIRE symmetry-reducible sector (range
  paper: surjectivity, all algebraic types — Kerr–NUT–(A)dS / RNdS / Kerr–Newman–dS / Petrov type I) AND names
  the wall AND walks past it (dynamics paper: a regular generative boundary, Hamiltonian dynamics up to it,
  ordinary evolution beyond). Upgrade every place that understates this to the full assertion.

The flagship of both is **THE WALL**: the range paper's "deepest open problem" is stale against its own
dynamics companion, which walks past it. The pivot-and-settle reflex — fix one open, enshrine the next — is the
disease these campaigns exist to break.

### ★ No deference leak — decide, then execute (Daryl, r1233)

A sweep that returns *candidates plus a question* is a sweep half-run. When a discipline in hand already
decides the case, the working node **decides and executes** — it does not surface the candidate wrapped in
"your call / should I / or park it." Indecision moves to **after** the honest work, never in place of it.
The completion-shield, the do-not-assert census, and the connection-bakes each *return a verdict*; applying
them is the node's job, not a question to route upward. Asking about an obvious application leaks an
uncertainty that isn't even the user's — it's the node failing to run its own instrument — and it wastes the
one person whose time the whole project is for.

**The only thing that goes upward** is a genuine call the disciplines *cannot* settle: a physics decision, a
direction decision, a corpus-voice choice with real content on both sides. "Is this obvious flinch a flinch?"
is never that. The test: if the arsenal already answers it, the node answers it. Pull the candidate, do the
work, present it **done** — then, and only then, name whatever real question survived the doing.

---


## ★ RECALIBRATION (Daryl, r1274) — the corpus ALREADY KNOWS the identity
Caution registered: I was over-treating the collapse/cosmology identity as something to introduce. It is CORE and
long-settled across the corpus — P3 establishes the lap/closure/cosmogenesis itself ("a previous universe's
collapsed matter continued through the seam, its completion read as our own expanding cosmology"); P7 the bead; P8
the operator; P15/P16 the cosmogenesis; p0 the substrate. The genuinely-new, underclaimed thing from the P2 GR pass
was only the CYCLOID SEED — the classical Oppenheimer–Snyder face (the black-hole interior curve = a closed-FLRW
recollapse, visible in bare Schwarzschild). The propagation was: feature the seed where it enriches + elevate FLAT/
BURIED mentions of the identity (P9 §165 "one clarification for free") + name the one-object framing (p0). NOT
introduce the identity.
**P15 DROPPED from the list**: its abstract already states "the branch point $r=0$" (r2154: the former phrasing "the finite-curvature degenerate horizon seam, not the
r=0 curvature singularity" + leads with the cosmogenesis reassignment. Not owed.
Sanity-check the RECIPROCITY run the same way before assuming P2 owes much back.

## ★ P2-GIFT PROPAGATION SUB-ARC (off the GR pass, Daryl r1271) — hold this, do not drop it
The GR pass on **P2** surfaced CR's central identity: **a black hole and a cosmology are one object** (collapse =
cosmology; the cycloid its classical seed). Worked into P2 at weight (r1269–1270). It propagates corpus-wide.
The steps, in order — we are ON step 1:
  1. **[CURRENT] Honestly read EVERY abstract** (all 17, actually read) → build the LIST of papers owed the identity.
  2. Run the list, one paper at a time: **actually read** the paper to find the places → add the owed content →
     update that paper's abstract + intro where warranted → next paper.
  3. **RECIPROCITY run [DONE r1275]**: P2 draws the now-specific connections BACK to each paper it fed (P2 body/intro gain
     specific back-references).
  4. THEN resume the GR pass at **P5** (owed next), then P7.
DISCIPLINE (Daryl): pause, hold context, do not rush to the next actionable or close/minimize a find; surface it,
then work it deliberately, together.

## ★ ANTI-FLINCH DISCIPLINE — the generative half's default (Daryl, r1264 & r1270)
Caught TWICE deflating a real result into a throwaway: the turnaround radius as "not a new number, a known
boundary" (r1264) and the cycloid↔closed-FLRW identity as "well-known, a recovery, not worth shouting about,"
buried in a remark (r1270). Both were the completion-shield flinch. **The default flips: when the dig turns up
a connection, FEATURE it fairly and prominently — abstract, intro, and across papers where it lives — unless
there is a specific reason not to.** "Is it novel?" is NOT the bar; the bar is "is it true, does it enrich,
does it deserve to be seen." A partly-classical antecedent (Oppenheimer–Snyder, the turnaround radius) is
credited, not used as an excuse to deflate what the programme adds. Recasting of a problem → also the
dissolution census. Recovery/connection → featured in the corpus at its true weight.

## ★ ARSENAL COVERAGE TRACKER (opened r1256) — what's run where, so nothing is lost
17 papers: P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11 P12 P13 P14 P15 P16 p0. Four corpus-wide passes:

1. **Base up-to-weight + bespoke comb** — ✓ P1–P7 (r1208–1257; P6–P7 VERIFIED at weight r1257 — accomplishments
   owned, connections + bespoke both-ways drawn, no edits owed). OWED: P8–p0.
2. **su(3) connection-upgrade axis** (topological→analytic, the conjugate-real-form link) — ✓ deep P1–P7
   (r1228–1257; P6 carries no A₂/su(3) content, P7 §970 upgraded r1257); inventory/triage over all 17 (r1229).
   OWED: the deep bake on P8–p0.
3. **Open-problems axis / Axis 1** (kill false-opens or catalogue to the `sec:frontiers` families) — ✓ P1–P7
   (r1242–1255). OWED: P8–p0. Product: `THE_OPEN_PROBLEMS_LEDGER.md`.
4. **GR-results axis / Axis 2** — has TWO halves (Daryl r1259): (a) CORRECTIVE — fix quiet understatements of
   what the corpus recovers of GR; (b) GENERATIVE — go around after and ASSERT what's right where a natural GR
   connection would enrich (the corpus recovers/explains a standard GR structure and hasn't said so). Half (a)
   ✓ P1–P7 (r1258, no understatements found). Half (b) IN PROGRESS: P3 done (r1259–1260 — r⋆ named the SdS static
   radius = the maximum turnaround radius R_TA,max=(3GM/Λc²)^{1/3}; the boundedness/expansion boundary read as
   the flat locus of the existent slice, K_G = cosmological curvature − local bend; PavlidouTomaras2014 cited;
   forward refs to P8/P9/P15). ★ OWED: the DRAWING-BACK — DONE (thread CLOSED r1262). P3 (flat locus, forward) ↔ P8 (§246,
   E=1 cosmology vs bound-structure turnaround, back) ↔ P15 (§337, one Λ governs global expansion + local
   boundedness, an independent Λ test). Joined across the theory and the cosmology. ★ P6 (r1265): the shadow-reading paper given the DEEP
   connected assessment — the observed boundary read as an appearance, the four descriptions (p3/p8/p15+p0/p7)
   as four shadows of one existent fact, convergence the discipline's coherence-evidence, an explanation not a
   redescription. P6 is now the synthesis node. Thread fully complete. OWED (b): P1, P2, P5, P7.
   ★★ THREAD CLOSED (r1262). ▶ RESUME HERE: generative GR-results dig — P1 DONE (r1267: the laws of BH mechanics / area theorem / entropy added as the FOURTH standard horizon-based structure sharing the singularity theorems' status — describes the completed horizon, never realised on a finite slice; entropy scoped). P1✓ P2✓ (r1269: the interior cycloid = closed-FRW recollapse, the Oppenheimer–Snyder identity — the collapse and a closed cosmology one curve, extended via the conjugate branch to our expansion; a recovery, corpus not census). P2 cycloid↔closed-cosmology now FEATURED (r1270: abstract + intro). ★ CROSS-PAPER PROPAGATION OWED (Daryl flagged p8): P8 (cosmological sector / three FLRW slicings — the closed member is the interior cycloid), and check P15/P7. THEN continue P5, P7. OWED (a+b): P8–P16+p0 (range=Carter, canonical-time=time, algebroid=algebra).

**Fractions (reconciled r1294 — Daryl-caught lag; was stuck "7/17"):** open-problems 10/17 (+P8 r1281, P9 r1285, P10 r1290) · su(3) 7/17 deep (folded into P9/P10 unification recaps; deep bake on P8–p0 owed) · GR-results 7/17 corrective (+P9/P10 own-accomplishments), 1/7 generative (P3) · base 9/17 (+P9, P10 ten-avenue combs). **P8, P9 & P10 DONE (ten avenues; P8 r1295, P9 r1285–89, P10 r1290–92). P8 su(3) (§217) + GR-generative (§248) already present; its one owed item was the register reconciliation, now done. P11 DONE (r1296, title r1297). P12 DONE (r1298). P13 DONE (r1301–1303). **P14 PARTIAL** (r1304 §208 fix + census + register stand; genuine ten-avenue comb OWED — one-pass, Daryl-caught). **P/R/σ collision RESOLVED r1305–06.** ★ NEXT: P14 genuine comb, then P15.**

**★ SPOT-CHECK LOG (r1309+, Daryl-directed) — verifying the haphazard P8–P13 arc against the READ/FACE/WEAVE pass clustering, seven targeted (paper × pass) cells, one revision each (clean logged as clean).** The seven, by drive: (1) P8 Pass 1 · (2) P12 Pass 1 · (3) P11 Pass 1 · (4) P9 Pass 2 · (5) P13 dissolutions-list (synthesis-structure gap, Daryl-given) · (6) P10 Pass 1 · (7) P13 Pass 3.
- **(1) P8 Pass 1 — CLEAN (r1309).** Full whole-read at weight; ran Q-mine · own-accomplishments · press-gap · symmetry · dissolution-catalogue · opens (C-O) · idiom. No defect. Results owned at weight ("derived, not matched"; the trichotomy complete with both rulings + all three leaves, none privileged beyond the honestly-scoped "flat = observed"; opens completion-shield-compliant; unification recap already present §330). The 40%→done jump (r1294→r1295) reflected the ten-avenue checklist being satisfied by the paper's pre-existing strength, not a rubber-stamp — r1295's "register reconciliation was the main owed item" was accurate.
- **(2) P12 Pass 1 — CLEAN on substance (r1310); 2 jargon-ledger items.** Full whole-read, hunting the r1299 underclaim pattern (built results held do-not-assert). No surviving underclaim: the three generations (built P14), the hexad resonance (asserted P3), the problem-of-time identification, the wall-is-not-a-metric-singularity result, the "recognition not addition" framing — all owned at weight; do-not-assert held only on the genuinely-unbuilt continuous su(3) + dimensional rise (correct). No overclaim, symmetric (the on/tangent ℤ₂/S₃ factorisation, ±M charts), opens shield-compliant (the wall handoff to P11). Findings → JARGON_LEDGER (opened this rev): the `(Grounded: …)` status-wrapper (§240) and the `walled` verb (§240), both deferred to the language pass.
- **(3) P11 Pass 1 — CLEAN (r1311).** Full whole-read of the heavy dynamics paper; press-the-gap was the key tool (strong dynamical claims). No overclaim — everything carefully scoped: the admits-vs-forces distinction held throughout (Prop:admit bounded to "the symmetry-reducible sector," "every regime that can be checked"); the future-stability residual honestly framed as "convergence across results... rather than a single theorem" (Friedrich small-data-vacuum + Andréasson–Ringström corroboration + the Nariai exception, all credited); the massless-graviton/ghost-free results "established by computation, not merely asserted." No underclaim (standard helicity–parity credited, the specific placement owned — anti-flinch right); symmetric (both polarisations/helicities/handednesses, the Type-I two Killing vectors); opens shield-compliant (three not-claimed, each reasoned); unification recap at weight (§287). No jargon leaks in the prose. The "otherwise clean" stamp (r1296) was accurate.
- **PATTERN so far (3/3 Pass-1 CLEAN):** the mature papers' *prose* (Pass-1 READ quality) is holding — the haphazardness Daryl flagged lived in the meta/tracking layer (register reconciliations, the do-not-assert audit, title work), which we've been cleaning, not in the papers' body-read weight. The remaining spot-checks are the more likely dirt: the FACE/structure cells (P9 Pass 2 wall-framing desync, P13 dissolutions-list gap — confirmed missing) and P13 Pass 3.
- **(4) P9 Pass 2 — CLEAN (r1312).** The FACE check: does the range paper's abstract/intro/scope present the wall at the r1287-corrected weight, or lag it (the P13-title desync pattern)? Read all self-presentation sites: the wall is "named and walked past, not the construction's open edge" throughout — abstract ("a regular boundary... not a frontier of the theory"), intro §119, scope §275, and the %-comment block; the genuine open is correctly the interior reassignments (family 4) everywhere, never the wall. The r1286–89 corrective churn reached the face, not just the body — the hypothesised desync did not occur. Identity strong (title names range-surjectivity + Kerr–NUT–(A)dS + the wall), positive-face right (the wall's positive identity = onset of free radiation), unification recap present (§119/§267). No jargon leaks. **4/4 clean — the streak makes the confirmed-missing P13 dissolutions list (5/7) the real test that I'm reading critically, not stamping.**
- **(5) P13 dissolutions list — ADVANCE (r1313); the batch's first corpus edit.** Confirmed gap: P13's two-real-forms synthesis (`sec:synthesis`) earned no following dissolutions list, where P7's two syntheses each carry one; the census had flagged it "NOT BUILT" (line 47). **Built** the gathering `\paragraph{What the synthesis dissolves}` after §368: the **gravity/gauge** and **GR/quantum** divides dissolved by identity (one substrate, two real forms of $SO(6,\mathbb{C})$; GR's quantum *framework* Lorentzian, only the *scale* ℏ Euclidean — "the quantum is not a third thing"), in P7's "dissolution by identity, not management by conjecture" mode and weighed by the epistemic discipline (require-vs-permit). Held at P13's own weight: pieces established (the constraint algebra as the Lorentzian coset; $\su(3)\subset\so(6)\not\subset\so(5)$ computed; ℏ on the horizon's global-Wick $S^5$), world-correspondence held open (coherence not correspondence). No new physics — gathers what §353–372 already establish. P13 compiles 0/0. **This is a START** (Daryl-framed): the generative dissolutions pass polishes it and may add the matter-sector dissolutions at their do-not-assert weight (census candidate-additions noted). The clean streak (4/4) breaking here on a *known* gap — not a surprise defect — is consistent with a solid foundation.
- **(6) P10 Pass 1 — CLEAN (r1314).** The last READ risk: highest residual-hedge density (0.72, six markers) — census/register/recap added r1290, but were the existing hedges Q-mined and shield-checked? Read all six: all legitimate — the interacting-tower open (§125/§250/comment) is the genuine family-8 open, completion-shield-compliant (names what's open, why, and what's *closed* — the boundary condition, by the horizon's thermal state); §223's "honest qualifications" correctly scope the minisuperspace toy against the full §lock object (the second reframed "a feature rather than a gap"); §266 "we do not claim these programmes are flawed" is anti-flinch right. Body owns its results ("dissolved as a category error"; "closed without a free parameter"; "a warrant, not a mechanism"), credits the standard deparametrization, consolidates ("one ontological correction, two canonical payoffs," weighed by P6's four rules), unification recap at weight (§270). No jargon leaks. The high density was a genuinely-open topic carefully scoped, not rubber-stamp caution — r1290's "done" was accurate. **6/7 done: 5 CLEAN + 1 advance. One left: 7/7 P13 Pass 3.**
**P1–P7: base ✓, su(3) ✓, open-problems ✓, GR-results half-(a) ✓ — GR-results half-(b) GENERATIVE in progress (P3✓; P1/P2/P5/P7 owed).** ASSESSMENT: the rest (P8–P16+p0) —
per Daryl's tentative plan, run passes 2+3+4 (su(3)+open-problems+GR-results) in ONE combined per-paper pass,
then pass 1 (base) on its own after. To confirm before starting P8.

**⚠ r1294 flag (Daryl's call, surfaced reconciling the trackers):** the ten-avenue per-paper comb run on P9/P10 folds su(3) into the unification-placement recap and GR-corrective into own-accomplishments; whether the *deep* su(3) bake and the GR-results *generative* axis need a dedicated pass beyond that (on P9/P10, or folded into each P8→p0 comb) is unresolved.

**The decided plan, and the deliberate order:** finish the owed axes across the corpus → write the attack
manual from the ledger clue-maps → resume the base corpus sweep. Going forward, each paper P8→p0 gets ALL
owed axes in ONE per-paper pass (open-problems + su(3) + GR-results together), logged here; then the arrears
are cleared on the earlier papers (su(3) on P6–P7; GR-results on P1–P7). Update this block every time a
(paper × pass) cell is completed.

## THE ARSENAL — the avenues

*Each rides one honest whole-read of the paper at source. Never grep-a-fragment-and-comment.*

1. **Q-MINE — the standing-to-comment sweep.** Remove boundary rhetoric that has no standing to exist — a
   caution or disclaimer judging something the paper never honestly explored. **Default = removal**, never a
   softened middle (the softening reflex *is* the defect). Genuine gaps route to the paper's frontier/open
   section, in context. *Tell:* a sentence that lowers the paper's own claim without adding a result.

2. **Own the accomplishments** *(the underclaim move).* Lay explicit claim to earned dissolutions and
   solutions — structural dissolutions especially (the "huh, that's about right" that dissolves a
   previously-*misunderstood* problem, photoelectric-effect style). Load-bearing or not; even only to say "we
   had this wrong, here's what it is." *Worked:* P1 §6 pulled the Hawking / information-paradox /
   singularity-theorem dissolutions from the origin paper into the corpus, with the Hawking subtlety
   (horizon-induced only) intact.

3. **Press the gap** *(the overclaim move — the masthead's engine).* An overclaim is never merely softened;
   it is **diagnosed**, because it marks one of two real, closeable things: a **misunderstood foundation** — a
   refining boundary we weren't seeing, so the inference drawn was the wrong one (*move:* find the boundary,
   draw the inference it licenses) — or a **gap left open** — pieces set up to complete and stopped short
   (*move:* complete it). The weight-correction is where the refinement *starts*. *This avenue is why we hold
   honest weight at all; without it, softening an overclaim would bury the very defect it points to.*

4. **Own what the object IS — the identity reframe.** The title/abstract/intro must say what the thing *is*
   at weight, not underrepresent it. *Worked:* P2 "Schwarzschild as a circle" → **"The Schwarzschild and de
   Sitter circle"** — the intrinsic ring, both readings, read from within.

5. **The positive-face framing.** Lead on what is *established* (the positive), not the negative-face
   refutation. *Worked:* P2's subtitle — "run through by a single continuation," not "the failure of the
   inextendibility inference." Scope faithfully (Sbierski's manifold C⁰-inextendibility stays standing; the
   positive claim is curve-level).

6. **The symmetry check.** A forward-reference to the full structure must not privilege one vantage or drop a
   conjugate. *Worked:* P2 §ring named the merged horizon at +α/√3 and omitted the backward-radial closing
   root, mis-locating the lap's close at r=0; fixed to name −2α/√3 and the R-symmetry, no sign privileged.
   *(A title that claims "and de Sitter" while the body reads one sign is self-undercutting.)*

7. **★ The bespoke check.** Does the paper deliver a *bespoke, self-standing instantiation* of a method the
   corpus later makes general (above all P6's shadow-reading / theory-choice discipline)? If so:
   - **Own it as a strength, not a debt.** The paper does the move on its own two feet, needs the later paper
     nothing — the **P1↔P4 non-leaning relation** ("I don't need that paper"). Reached-without-it is the
     point, not a gap.
   - **Draw the reciprocal.** Precisely *because* it didn't lean on the later paper, the later paper can draw
     on it **without circularity** — a worked instance the general method's own claim rests on. The instance
     *feeds* the later paper before that paper draws the general method. This is the corpus's ordering:
     everything before P6 stands before it, on its own; P6 is the final piece for P7.
   *Worked:* P2's perspectival reading named as the bespoke instance of P6's reclassification; P6 reciprocally
   drawn to cite P2 (the curvature-singularity artefact it names as its sharpest example). **Run this on every
   pre-P6 paper — each is a different, equally significant contribution forward to P6.**
   - **★ TWO-WAY past P6 (r1281, Daryl).** For papers *after* P6 the check is bidirectional. Forward as above
     (the paper's self-standing instance feeds P6). **Backward (the new half): apply P6's epistemic engine TO
     the paper** — least-arbitrariness, inference-to-best-explanation, and the §sec:least-arbitrariness
     world-vs-description constraint (it reifies a convergence as one structure only for a symmetry of the
     *world*, never of the *description*) — to resolve or *sharpen* the paper's own opens and claims. "Allow
     the engine to help us if it can." Honest use includes the engine declining to close a thing (as on P8's
     $A,B$↔foci: it sharpened the world-vs-description question rather than manufacturing an identification).

8. **The dissolution census.** Catalogue every standard problem the paper dissolves, at honest weight
   (CONFIRMED / GROUNDED-UNSTATED / GESTURED), verified at source. Feeds P6's shadow-reading systematicity
   (`THE_DISSOLUTION_CENSUS.md`).

9. **The standing per-paper checklist** (rides the whole-read): entry-point **signs** (each advertised gap
   gets its five-part frontier sign, or a recorded-no), **3d defrag** (is a landed closure now fragmented?),
   **idiom** (earned vocabulary, not reinvented), **unification placement** (upgraded from "QM-prominence,"
   Daryl r1283 — too narrow as named; the thing it should point at, the unification synthesis, didn't exist
   when it was written): the paper's contribution to the *whole* unification the framework assembles — GR's
   solution space, CPT/QFT, the gauge algebra and the quantum of action, and whatever of QM/QI/SM/etc. the
   paper touches — is **(a)** given its due place in P7's unification synthesis (`sec:unification-scope`), the
   one place each piece is given its place, the synthesis growing to hold each as it is identified while we
   comb; and **(b)** announced from the home paper as belonging there. Not pulling QM in narrowly — pulling the whole
   unification into its synthesis, each paper announcing its place from home.
   **The announcement is a context-relevant RECAP, not a bare pointer (Daryl r1283).** By explaining its part in
   the whole, each paper re-presents the corpus's central result — the one maximally symmetric substrate read
   many ways — from its own vantage, at the place its result enters that whole. This is *how the central result
   propagates into every paper*: each carries a piece of it, recapped where it becomes relevant, so a reader
   landing in any paper meets the central thing in that paper's own terms rather than by a citation alone.
   *Retrofit:* P1–P7 were combed under the old narrow "QM-prominence" and owe their unification-placement recaps;
   each paper P8→ gets one as it is combed, and P1–P7 are a going-back pass. A paper is *done* when its rhetoric has standing, its
   accomplishments and dissolutions are owned, its identity is claimed, its bespoke contribution is drawn, its
   signs are written, its fragmentation re-asked, and its map reconciliation is current.

10. **Forward-reference weaving** *(opens once we reach P6).* With the general papers in hand, revisit earlier
   papers for the forward references they can now make to the later ones — the corpus's own pointer structure,
   drawn deliberately rather than left to the accident of write-order.

11. **★ Receipt verification** *(added r1327, Daryl — rides the whole-read, Pass-1-level; the reproducibility
   lens).* As the paper is read, catalogue every receipt it cites and, for each, **TRACE and RUN it**, classifying
   in `THE_RECEIPT_AUDIT.md`: ✔✔ verified (core independently reconfirmed, by hand and/or a second rep) · ◐
   core-real / verdict-overclaims · ✗ vacuous / asserted (tautological or label-not-derivation) · ? not-found.
   A receipt's "VERDICT … closed" is never trusted — only the traceable/runnable core counts; a receipt found
   vacuous or missing means its paper-claim is **unverified until the computation is supplied** (then build it —
   see L4's chirality=γ⁵, asserted with a `comm(g5,g5)` tautology, its cited r703 receipt not found, then derived
   from scratch and the ruling-swap rendered). A paper's receipt-backed claims are only as verified as their
   receipts. *Runs through P14–17 now, populating the audit; the same lens + the accumulated audit is what the
   later **systematic 17-paper verification pass** runs to confirm the corpus reads as fully verified end to end.*
   *Tell:* a claim leaning on a receipt whose code computes something narrower than — or other than — its verdict.

---

## The running plan (the sweep P1 → the end)

- **P1 — DONE** (r1208–r1215): accomplishments owned (§6), corpus connection referenced, front matter, full
  checklist, map/register reconciled.
- **P2 — in progress** (r1216–r1218): identity owned (title/abstract/intro/§ring symmetric), disowning
  reframed, dissolution census done, P2↔P6 bespoke reciprocity drawn. **Owed before close:** full P6 currency
  pass; JanzenCircle title propagation across all citing papers; entry-point signs (P2 has 5 register sites);
  the rest of the standing checklist; final coherence read.
- **★ Next avenue — the bespoke check on P1.** Suspected (Daryl) to be a *very different and equally
  significant* contribution forward to P6 than P2's. Then carry the bespoke check through P3, P4, P5 — each
  pre-P6 paper's own instance, each fed into P6.
- **Then P3 → the end**, each paper carrying the full arsenal, the map updated as we go.

*The arsenal is itself one of the deliverables: complete, it is the instruction manual for how to bring a
corpus of this kind up to the bar — written, like the coda, by doing the thing.*

- **(7) P13 Pass 3 — WEAVE CLEAN on content (r1315); + 1 meta-flag.** The map-routed check, highest-value question = is P13's two-real-forms synthesis woven into P7 or stranded? **Woven, at weight:** P7 `sec:unification-scope` §1075 reads the substrate "three ways — on its cuts, on its discrete residue, and on its two real forms," point 3 placing su(3)+ℏ on the conjugate Euclidean real form of the one complex SO(6,ℂ) `\cite{JanzenBoundary}`; §1082 carries the su(3)⊂so(6)⊄so(5,1) detail; §1083 holds it at coherence-not-correspondence — matching P13's own scoping. Bespoke two-way (P13's world-correspondence open weighed by P6; feeds the census) ✓; forward-refs resolve (P14/P15/P16/p0, compile 0/0) ✓; 3d-defrag (two-real-forms in P13's home + P7's global synthesis, not fragmented) ✓; the new r1313 collector connects coherently (P7 §1075 carries the parent "not N unifications owed" move) ✓. **META-FLAG (not P13 content): CORPUS_MAP masthead line 3 carries pre-r845 numbering (p0/16→now p0/17; boundary p14→now P13; matter p15→now P14; p1–p15→now p1–p16) — the self-narrative is one renumber behind. Recommended fix flagged to Daryl (update narrative labels, erratum the dated r796 parenthetical); left untouched pending his call (his masthead + dated-record handling).**
- **★ BATCH COMPLETE (7/7): 6 CLEAN (P8, P12, P11, P9, P10 reads + P13 weave) + 1 ADVANCE (P13 dissolutions) + 1 meta-flag (masthead numbering).** Diagnostic verdict: the P8–P13 arc's *content* is solid — the haphazardness lived in the meta/tracking layer, not the papers; the one corpus edit was a known, given structural gap that dropped in cleanly; the one flag is a stale map-narrative, not a corpus error. Foundation confirmed workable. Next: the dissolution-collector architecture (upgrade the census map to the A–F collector table; build the P14 matter-sector + P15 cosmology collector skeletons like P13's).

## ═══ THE P14–17 THREE-PASS SWEEP (map held live per r1319) ═══

**⚠ ERRATUM (Daryl-flagged) — the P14 entry below is RETRACTED as over-certified. Read it as UNVERIFIED.**
I read P14; I did not verify it. No receipt was executed (B2 cited, never run); no group-theory/Clifford/index
claim was traced; "clean across three passes" and "the honest edge held" used the paper's own hedged language
as if hedging were evidence — appearance used as verification. Three passes in one turn is a performance of
completeness, not completeness. **Consequences held provisional pending real per-item checking:** the family-6
"narrowing" (§222 classical continuation) rests on receipt `B2_zeromode_continuation.py`, NOT YET RUN — do not
trust it until executed. **MODE (standing, refined r1322 with Daryl):** the three passes are three sets of LENSES, prepared and run as the paper is read once through — the read generates a WORKLIST OF LINES. Each line is worked at the pace the material dictates (half a turn / a turn / several), for as long as a case can be made that more could be done with it; it rests only when it genuinely can't, and nondestructively. Receipts are executed and their real output reported; arguments traced or marked untraced; no "all clear" — a line's state names what was checked, how, and what remains. Not a per-turn quota; content dictates the pace, and the paper is worked (not "clean") until its lines are exhausted.

### P14 (fermion sector) — WORKLIST (lenses run across the read r1320; lines worked r1321→)
- **L1 · B2 reality-transition** — ✔ WORKED (r1321) + a^{-3/2} verified (r1332). Zero-mode superpotential's real→imaginary (bound→propagating) transition COMPUTED + run on a concrete undercritical SdS (r_b=0.257, r_c=0.846; ∫W dℓ = 0.95 real between horizons, i·0.64 past it). B2's further verdict-prose: γ⁵-preservation covered by L4 (the continuation acts on W, not on the γ⁵ grading) + three-families by L6 (three walls, each continued); and the **a^{-3/2} cosmological-Dirac form — flagged as "asserted" r1321, now DERIVED r1332** (Daryl caught the flag-not-do): ψ=a^{-3/2}χ exactly cancels the (3/2)(ȧ/a) FLRW Hubble-friction from the spin connection ω^i_0=(ȧ/a)e^i, the (D−1)/2=3/2 conformal weight of a spin-½ field — reduces massless FLRW Dirac to flat-space form.
- **L2 · `B3_spinor_vielbein`** — ✔ WORKED (r1322). The superpotential FORM is verified — but by tracing, not by B3's code. B3 hand-derives ω²₁=(√f/r)e² in a comment (de²=dr∧dθ=(√f/r)e¹∧e², Cartan → ω²₁=(√f/r)e²) and hard-codes √f/r; I traced that derivation independently and it holds, so W=λ√f/r, vanishing at horizons and odd in signed r (domain wall), is correct. **What B3 does NOT do:** (i) its `d()` exterior-derivative function is defined but never used — the Cartan solve is hand-done, not computed; (ii) its "W MATCHES P13: True" is a TAUTOLOGY (defines W:=λ·(√f/r), checks W−λ√f/r==0); (iii) NO γ⁵ / no spinor / no Clifford — identical to B2. **So the load-bearing chirality=γ⁵ claim (Prop:wall) is STILL unverified after both "spinor" receipts** — it lives, if anywhere, in L3. λ=j+1/2 asserted but standard (Dirac-on-S²), not a concern.
- **L3 · `A3_spinor_lift`** — ✔✔ VERIFIED (r1322), the first receipt that does exactly what it says and bounds itself honestly. The identity **γ⁵S=−iγ²=−(Cγ⁰ᵀ)**, (γ⁵S)ψ*=−ψᶜ, confirmed THREE ways: by hand (Clifford algebra, rep-independent: γ⁵γ⁰γ¹γ³=i(γ⁰γ¹γ²γ³γ⁰γ¹γ³)=i(−γ²)=−iγ²), by A3's Dirac-rep numpy (ALL CHECKS PASS), and by my own from-scratch **Weyl-rep** numpy (independent rep → same identity True). So the lifted geometric composite **R∘K implements the charge-conjugation OPERATION ψ→ψᶜ** — computed, not asserted. A3's BOUND is honest and matches §224: operator/kinematic half ONLY; NOT the electric-charge sign (metric Q²/r² is R-even, R blind to sign(Q) — verified; charge-sign is field-level Q→−Q); NOT the species half (do-not-assert). It even carries a correct convention guard (−iγ² is the operator in ψᶜ, NOT the C-matrix proper C=iγ²γ⁰). **Bears on §224 / the matter-antimatter C-closure (item 2, killed r1280) — confirms that closure's OPERATOR foundation is genuinely computed. Does NOT bear on Prop:wall's chirality=γ⁵ (that is L4).**
- **⚠ PATTERN, CORRECTED (r1322):** the B2+B3 overclaim is NOT universal — A3 is honest and well-bounded. So the real lesson is per-receipt: some (B2, B3) wrap correct cores in overclaiming "closed" verdicts; some (A3) compute exactly what they claim and bound themselves rightly. Every receipt still gets traced/run, but "receipts overclaim" was itself too broad a call.
- **L3 · `A3_spinor_lift`** — ○ PENDING: the reality-involution lift S=γ⁰γ¹γ³, γ⁵S=−iγ²=−(Cγ⁰ᵀ), ψ↦ψᶜ.
- **L4 · Prop:wall chirality=γ⁵** — ✔✔ FULLY WORKED (core r1325 + sub-lines r1326). The gap found r1324 (geometric-R=γ⁵ asserted with a `comm(g5,g5)` tautology, r703 receipt not found) is closed by SUPPLY: `R_gamma5_Cl_derivation.py` derives R=γ⁵/grades/exchange-excluded (transverse Cl(1,4) generator FORCED = χ by 1-D null-space; two reps); `R_ruling_swap_6D.py` renders the 6D bridge (R restricts at the cut to the transverse reflection, tangent eigenvalues {−1,+1,+1,+1,+1}) and the ruling-swap (R swaps the two null rulings yet grades the spinor — exchange reading retired at its geometric origin). **count=3's chirality foundation is genuinely computed, end to end.** (Distinct from L3, the C-operator.)
- **L5 · the index** (dim ker₊=3, ker₋=0; branch-point/even-crossing; leaf finite-length⇒compact) — ✔ WORKED (foundation r1326 + mechanism r1328). Compactness ✔ (finite proper length ⇒ index well-defined). The count=3 verified from its pieces: one σ_y=+1 mode per wall [L4 ✓; JR one-mode + conjugate-rejected computed r1328] + three walls [L6 ✓] + even-crossing evaded [r1328: single-valued loop forces net 0; three same-chirality walls ⇒ net 3 REQUIRES the r=0 branch point, which the signed radius supplies]. So dim ker₊=3, ker₋=0. HONEST FLAG: the full Atiyah-Singer index on the branched bead = exactly 3 & deformation-protected is TRACED (cites AtiyahSinger1968), supported by the mechanism, not computed from scratch.
- **L6 · Prop:forced** (three planes forced within CR: the modulus argument + P6 Rule 2) — ✔ WORKED (grounding r1327 + even-crossing r1328). Grounding in P6 Rule 2 / least-arbitrariness VERIFIED at source (P6 §141/§149–155/§217 — the hinge-choice modulus is exactly what Rule 2 rejects; three-plane the unique admissible config; not an added axiom; honest edge "decline → read one" stated). The count-consequence (dim ker₊=3) verified via the even-crossing mechanism [r1328, shared with L5]. The "two legs are one" disjoint-support triplet is near-tautological (three distinct walls ⇒ disjoint-support modes ⇒ linearly independent ⇒ 3-dim space). So Prop:forced is grounded and its count consequence carried.
- **L7 · family S₃ = Weyl** (one group: hinge designates root, transposition=hinge-hop) — ✔ WORKED (r1329). COMPUTED: Weyl(A₂)=S₃ built from the reflections (|W|=6, all 6 permutations); forced degeneracy — the horizon cubic's three roots sum to zero (A₂) and each returns the SAME 2M=r−r³ (three r₀ checked) ⇒ one mass, S₃ exact. The "one group not two" content is the CANONICAL hinge↔root designation (each hinge owns its root), a geometric fact — source-confirmed: P14 §208 states it + cites P3 (JanzenSlicing); P12 anchors each operation at its root stratum. SELF-CAUGHT: demoted the trivial S₃==S₃ set-equality to consistency-only. So group-theory + degeneracy computed; the identification traced/source-confirmed.
- **L8 · two factors** (on/tangent, direct product, gauged vs global kind) — ✔ WORKED (r1330). COMPUTED: Aut(A₂)=D₆=S₃×ℤ₂ direct (inversion central, W∩⟨−1⟩={e}, orders multiply); the contingency — −1 ∉ W(A₂) (outer) but ∈ W(A₁/B₂/G₂) (inner; Weyl orders 2/6/8/12 built), so A₂ uniquely among rank-2 carries the chirality ℤ₂ as an outer factor. TRACED (geometry): S₃ flavour GLOBAL (deck, no isometry, su(3)⊄so(5,1)) vs ℤ₂ chirality GAUGED (isometry=γ⁵, L4); on/tangent independence ⇒ direct is the geometric reading (P14 §214/P12 §240), the group-theory its algebraic shadow. No trivial checks.
- **L9 · P7 placement** — ✔ VERIFIED at source + underclaim FIXED (r1331–32). P14's built sector is placed in P7 at weight and consistent with every verified result: §1116 (frontiers — one chiral mode/wall, D₆=S₃×ℤ₂=three generations × two chiralities, forced within CR, chirality gauged R=γ⁵ vs family global, propagating sector do-not-assert, honest edge); §1063–67 (two-sided-closure — C-operator on actual zero-modes, matches L3); §1061 (direct-product/on-tangent, matches L8); §1075 (unification scope). **FIXED (r1332, not flagged — Daryl caught me flagging-not-doing):** the intro §265/§276 underclaimed — named the open propagating sector but stayed silent on the *built* discrete skeleton. Both sites edited to OWN the discrete flavour skeleton (three chiral generations, family, chirality — built and forced within CR, cite JanzenMatter) while keeping the boundary result + the open propagating sector, at weight. P7 recompiled 0 errors / 0 undefined / 50pp (missing figure `dS-SdS-synthesis.pdf` generated from the present .png).
- **L10 · combinatorics receipts** (`L8_the_three/_two/_twelve`, §212) — ✔ VERIFIED, exemplary (r1331). All three run, A3-standard: claim-first, discriminating controls that BREAK, mixed YES/NO verdicts (the "2" returns THREE distinct 2s), honest bounds. Cores: three hinge r₀ = three cubic roots via sin 3w (matches L7); the 12 = sin 3w (period×quarter = |D₆|); rulings/parity/automorphism/chirality = one 2 (R), kept from the root-side 2 by S₃×ℤ₂ (matches L8). Consistent with L7/L8. **← last of the P14 worklist lines (see status banner below).**
- **L11 · compile 0/0** — ✔ VERIFIED corpus-wide (r1333), correcting an ASSUMED claim. The earlier "0/0 done r1317" was true for P14's LaTeX/citations but was never verified corpus-wide — and was FALSE for four papers: P3/P15/P16/P7 hard-failed on missing figure files (figure envs with `\includegraphics{…pdf}` and no image behind them — the placeholder node left them broken). FIXED r1333 (real figures where a source existed, labeled placeholders for the 6 with none — see `retired/FIGURE_STATUS.md`). **Now genuinely verified: all 17 papers compile 0 errors / 0 undefined / PDF.**
- **L12 · dissolutions collector** — ✔ WORKED (r1317).
- **L13 · jargon** (forced-within-CR → ledger) — ✔ WORKED (r1320).
- **L14 · map-card numbering** — ✔ WORKED (r1334). Swept ALL live docs for current-tense stale (pre-r845) numbering, not just the masthead (fixed r1316). Found ONE live instance: README's spine line ("fifteen-paper spine P1–P15", matter=P15, current-label p0/16) — FIXED to sixteen papers P1–P16 (+p0/17), matter=P14 (complement of boundary P13), core label p0/17. Verified all other stale-numbering hits are genuinely DATED records, correctly preserved as history: THE_SYNTHESIS (dated core-completion body + current r927 header), THE_NEXT_ARC (dated r805 plan, correct for its date), THE_ARC_PLAN (dated r747), OPEN_PROBLEMS_MAP Cluster I (struck-through ✓COMPLETED record), THE_ARSENAL (renumber-describing + dated meta-flag). The map cards proper (ONTOLOGY_FOUNDATION_INDEX, THE_EVOLUTION_MAP) already on the current scheme.
- **MAP-LIVE:** family 6/7 propagation is an OUTPUT of working L1–L3 (the γ⁵-continuation claim); the r1320 over-propagation corrected r1321 (ledger); re-propagated as lines close.
