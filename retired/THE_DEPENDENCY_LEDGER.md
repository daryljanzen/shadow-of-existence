# THE DEPENDENCY & STALENESS LEDGER — the ordering tool: what depends on what, what went stale, what to do first
> **⌖ RETIRED r1451 — read in full, then filtered into `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md`.** Its live content went to
> item 4, with its ordering rule and its list of dependents. Kept as record; **do not plan from this file.** If something here is not reachable from
> `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md`, that is a filtering miss — raise it there rather than reviving this.


*Opened r1279 (Daryl). The living record that keeps us from working against ourselves. The corpus work is
recursive: one move can NEGATE a finished piece by changing what it depended on — finish P6's reciprocal
reference to P7's dissolution card, then add three more dissolutions to that card, and P6's reference is now
STALE. This ledger records the dependency edges, flags the staleness they create, and gives an ORDERING that
minimizes self-inflicted rework and cascades the work toward completion. Read at the top of the arsenal and
the index; it drives prioritization. **Living; never "done."** Kin to the closure self-check: a stale piece
is a close that later moves un-earned.*

## ★ THIS STRUCTURE STAYS OPEN — it maintains itself by learning-by-doing (Daryl, r1279, top-level)
The interdependency structure is never fixed and never complete. It gains its OWN operative check, fired on
two triggers:
1. **Whenever the arsenal's architecture is worked** — any adjustment or addition to the levels, campaigns,
   tools, or ledgers — ask: *what new dependency edges does this create, and what does it stale?*
2. **As we work WITHIN it** — interdependencies we did not know existed emerge as we do the work and realize
   what we are actually doing. When one surfaces, add the edge, re-check staleness, re-order.
So this is a living, learning-by-doing document: the edge set is **discovered, not declared**, and the map is
only ever the interdependencies found so far. Treat a missing edge as *likely*, not as absence — the same
stale-link prior the coda carries. **Never close the edge set.**

## THE MODEL (the rules)
- **Dependency edge:** piece **A depends on** piece **B** when A's correctness relies on B's *current*
  content — a reciprocal reference, a cross-link, a citation, a claim that quotes B's result. Write `A ⟵ B`.
- **Stability:** a target B is **OPEN** (still expected to change — its dependents are NOT yet safe to
  finalize) or **STABLE** (frozen at a rev — dependents may be finalized against it).
- **Staleness (the detector, by rev):** tag B with its current rev; tag each finalized A with the rev of B it
  was built against. **A is FRESH iff `A.against-rev ≥ B.current-rev`, else STALE** (owed a re-run). The
  convention that makes this work: *bump a target's rev whenever its content changes; record the against-rev
  on every dependent when you finalize it.*
- **The ordering rule (the whole point):** **stabilize upstream before finalizing downstream.** Never run a
  dependent (A) against an OPEN target (B) — it will stale the moment B advances. Bring B to STABLE first,
  then sweep its dependents in one batch.
- **The prioritization rule (cascade toward completion):** pick the target that is (a) closest to STABLE and
  (b) unblocks the most dependents; stabilize it; then kill its dependents together. And **do not re-touch a
  STABLE target without cause** — reopening it re-stales everything downstream.
- **The impact-ordering rule (Daryl, r1279 — order the dependents by the fundamentality of their content):**
  within a target's dependents, run the **primary dissolutions of the most famous problems first** — the
  fundamental ones, structural (P1 — the black-hole problems) and empirical (P4 — the measured foundation),
  the top-docket highest-impact results with immediate implications. They come first after the source because
  they are *what the synthesis gathers and what the weigher weighs*: the weigher needs its full subject laid
  down before it can weigh it. THEN the **weigher** (P6), which consolidates the now-established content and
  gives it its epistemic gravity. THEN the **smaller / lighter** contributing references, which tap the
  now-established-and-weighed structure and so reference it at full weight. **Order: source → fundamental
  trump cards → weigher → the rest.** *(Supersedes an earlier "weigher first" read of this rule: the weigher
  weighs content, so the most impactful content is laid down first. The run P7 → P1/P4 → P6 → the rest was
  right; the structured reason is here so it need not rest on instinct.)*

## WHY THIS MATTERS (Daryl, r1279)
The recursion is expensive, and the intuition-walk steps on its own toes when it finalizes a dependent before
its dependency is stable, or reopens a stabilized dependency after its dependents are done. This ledger is the
small optimization away from that: **finish things in dependency order, and stop making things stale right
after finishing them.** As a paper or axis reaches stability, its dependents unlock and can be killed in a
cascade. Intuition still picks the direction; this keeps the direction from stepping on finished work.

## THE CURRENT EDGES (seeded — grow as the sweep creates them)

### Target: **P7's dissolution card** — the `sec:applications-synthesis` synthesis + the individual dissolution subsections. **STATUS: OPEN** (r1279 — NOT yet declared stable; the call is Daryl's)
> Progress r1279 (B4): the applications section is comprehensive (14 subsections + the synthesis), and the
> intro + abstract now announce the three-movement structure with the dissolutions as the paper's FIRST
> SYNTHESIS. The card's content and framing are substantially filled. Honest remaining risk to stability: a
> further generative pass could still find or deepen a dissolution (the base rate on this dig), which would
> stale any dependent finalized now. So the card is CLOSE to stable but not declared — the stability call is
> Daryl's, and until it is made the propagation stays gated.
Dependents (the reciprocity propagation — each owes a back-link to its home in P7's dissolution synthesis).
**GR-axis dependents are propagatable now (the GR axis is locally stable, r1279):**
- `P1 ⟵ P7-card` — censorship / Hawking / info / BH-mechanics homed in P7. **✓ DONE r1279** (against the
  GR axis; back-link in `sec:problems` intro → P7's first synthesis).
- `P4 ⟵ P7-card` — the measured foliation / augmentation necessary-half grounds the synthesis's altitude.
  **✓ DONE r1279** (against the GR axis; back-link at the augmentation theorem's close).
- `P10 ⟵ P7-card` — canonical unitarity + the problem of time. **✓ DONE r1279** (against the GR axis;
  back-link in the conclusion).
- `P6 ⟵ P7-card` — P6's weighing of the cluster as its THIRD assessment (after the central theorem and the
  local–cosmic boundary), via require-vs-permit at the coherence altitude. **✓ DONE r1279** (against the GR
  axis; P6 `sec:place`). **Re-check:** P1/P4/P10 were done just before P6 — which, per the corrected
  impact-ordering rule, was the RIGHT order (fundamental trump cards P1/P4 first, then the weigher P6, then
  the lighter P10). Confirmed at weight: their back-links echo the theory-choice / dissolution-by-identity /
  coherence framing, and P7's synthesis carried that weight already. No staling.
- `P3, P8 ⟵ P7-card` — the local–cosmic boundary. **✓ DONE r1279** (against the GR axis; back-links at
  P3 §636 [the flat locus] and P8 §248 [the E=1 handover] → gathered in P7's first synthesis and weighed by
  the discipline, P6).
- `P15, p0 ⟵ P7-card` — cosmology / maximal symmetry. **GATED** (physics/cosmology axis, until that axis fills).
- `THE_DISSOLUTION_CENSUS P3–p0 verdicts ⟵ P7-card` — completed *against* the card, **per-axis**: GR verdicts
  doable now, math/physics verdicts later.
> **Ordering consequence (refined r1279, axis-level):** the propagation is gated on the relevant AXIS of
> P7's card reaching local stability, not the whole card. **The GR axis is assessed locally complete** (r1279,
> checked at source — the apparent danglers, the problem of time and the singularity theorems, are
> deliberately placed / folded, not owed), pending Daryl's stability call. Once confirmed, the GR-linked
> dependents (P1's censorship/Hawking/info/mechanics; P4's foliation; P10's problem-of-time/unitarity) can
> propagate now, while the math/physics axes keep growing; the math/physics-linked dependents stay gated until
> those axes fill (after the reach bakes).

### (more targets/edges added as they arise — e.g. the math-ledger decisions will spawn their own edges; a stabilized P7 will spawn the P8→P7, P9→P7, … arsenal-run edges)

## HOW IT DRIVES THE NEXT MOVE
Scan the OPEN targets by how many dependents they gate. Right now **P7's dissolution card** gates ~8
dependents (all the reciprocity + the census). So the highest-leverage move toward completion is to bring
that card to STABLE — finish the dig far enough that we agree it is ready — after which the whole downstream
batch unlocks and cascades. Running any single reciprocal reference *now* would just stale on the next P7
addition. **The ledger's verdict: don't walk downstream yet.**

## ⟐ THIS LEDGER'S OWN OPENS (dangling)
- Granularity: **REFINED to AXIS-level (Daryl, r1279).** The card will not fully stabilize until all math and
  physics bakes have been thrown at it, so whole-card stability is the wrong target. The natural unit is the
  **axis** of the card — the GR dissolutions, the math dissolutions, the physics dissolutions — each of which
  can reach local stability and be propagated to its dependents *while other axes keep growing*. This sits
  between per-card and per-claim, and it is what enables "propagate occasionally to catch up": once an axis is
  locally stable, finalize its dependents; a later dissolution on a *different* axis does not stale them.
  Per-claim remains the fallback if an axis proves too coarse.
- Whether staleness flags live here, in the index cells, or both.
- Auto vs manual rev-bumping — for now manual, on the honour of recording the against-rev.
