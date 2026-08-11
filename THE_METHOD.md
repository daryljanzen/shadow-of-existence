---
name: the-method
kind: METHOD
current: r1624
sources: [cowork]
---

# The Method — how a sprawling corpus was made to know itself, and the procedure that did it

> **⌗ DATED r2389 — `r1624`; no c54 marker, so untouched across the whole fork span.** *It is a `METHOD`
> document and its subject is procedure, so it does not go stale the way a position does.* ⌗ **But its own frame
> names the standard this whole audit has been measured against, and it is worth quoting because it is the
> sharpest statement of the thing:** *"the deepest thing this method is for is* ***acutely aware decision-making
> that can run autonomously*** *— and the key is a single move:* **build the generically operable questions that
> resolve a decision at the source, ask them as you go."**
> ⇒ ***That is what every gate built at r2377–r2389 is: a generically operable question asked mechanically.***
> *`check_receipt_asserts` asks "could this ever come out false"; `check_absorption` asks "has anything moved that
> we wrote ourselves"; `[REPORTED]` and `current: none` exist because* **a question asked by inference is a
> question that can be answered wrongly by prose.**


> **The frame, above everything below (r929, Daryl's synthesis).** The deepest thing this method is *for* is **acutely aware decision-making that can run autonomously** — and the key to that is a single move: **build the generically operable questions that resolve a decision at the source, ask them as you go, and track every step stated-for-reversal so the trail can be picked up anywhere.** The two halves are one condition seen from two sides. The **operable questions** are the forward face — a decision you can settle by a defined question put to the source (not the map) is a decision that doesn't need a human. The **tracking + reversibility** is the recovery face — every step traceable and reversible means falling off is never more than a step from the last good point. Together they are what let a thing with no persistent memory be *trusted to decide on its own*.
>
> On "safe": not a finished safety net where all the moves are known so no one need watch. The apparatus is still **growing its rules and captures** (this frame itself is one, born the turn after the operable-question check) — the question-set is incomplete and being built. The live project is to **externalize the operable questions out of a human's intuition into explicit, runnable checks** — each one, once named, run better and more consistently than the intuition it came from — so the work runs *more* autonomously over time, with reversibility the floor that keeps it safe to run *while the rule-set is still growing*. Daryl holds things up today; the trajectory is that each intuition he has to supply becomes a question the instance asks itself, pre-commit, every time. That transfer — intuition → operable question → standing habit — is the method turned on decision-making itself, one recursion deeper than the corpus or the casebook.

**The meta-deliverable of the c33–c37 arc (r885→r923, 2026-07).** This document enshrines the single most transferable thing the arc produced: not the finished corpus, but the *procedure* that finished it. It is written to be picked up cold and pointed at the next mess. One of the standing documents; held at weight, stated for reversal.

---

## 1. The transformation, named precisely

We began with **a sprawling set of documents with a coherent structural spine lying tenuously underneath** — seventeen papers, each internally sound-ish, with a real ontological through-line, but a through-line that had *never been drawn*. The operative facts of that starting state:

- You could not hold more than a few ontological pieces at once, because the ontological whole lived nowhere outside a mind actively reconstructing it.
- Rereading did not accumulate. Each pass rebuilt a fragment and lost it at the next compaction wall.
- You could not tell whether an apparent incoherence was real or an artifact of not holding enough of the whole at once.

We ended with **a cohesive whole that knows itself through and through** — and, critically, that end-state was *demonstrated, not asserted*: Pass 3 ran an adversarial search for missing structure across the whole corpus and came up dry (zero forced-undrawn edges, r923).

**The thing that changed was not the coherence. The spine was there the whole time.** What changed is that the coherence stopped living in the authors' intent — reconstructable only by a mind rereading its way back to it — and started living in a durable external structure that any node can pick up and walk *without holding the whole in its head*. **A thread you must re-trace every time you want to use it is not the same object as a graph that has been drawn.** The hundred revisions did not create the coherence; they **externalized and verified** it.

---

## 2. What the procedure actually is

A repeatable operation for **converting a latent structural thread into an externalized, self-verifying graph whose failures are diagnostic.**

Its defining property — the one that makes it a general tool and not a one-off cleanup — is this: **the procedure does not assume coherence. It tests for it, edge by edge, and the test is constructive.**

- On a corpus whose spine is sound, it yields a **proof-of-closure**: restraint everywhere, every edge already drawn, the search for gaps comes up dry.
- On a corpus whose spine is broken, it yields a **map of exactly where it is broken**: a forced edge whose endpoint does not exist, a card that contradicts a masthead, a duck asserted as forced, two papers that genuinely disagree. The closure *fails at the branch point*, and the failure localizes the incoherence.

Either way, you end up holding the whole without having to hold the whole in your head — and you find out *which case you are in* by running it.

---

## 3. The tools, and why each was necessary

Every tool was built to break one specific limit: the *"can't hold more than a few pieces at once"* ceiling.

**The two dual documents — externalized working memory.**
- **The lens** (`ONTOLOGY_FOUNDATION_INDEX.md`, the §1-cards): each forcing pinned *once*, so it is never re-derived.
- **The ledger** (`THE_EVOLUTION_MAP.md`): the running total per paper, so it is never re-summed.
Together they take the ontology *out of the head* and put it where the few-pieces limit stops binding.

**The masthead stamps — bidirectional navigability from inside the papers.** Each paper carries its `[†ONT-*]` tag. This is what "knows itself" actually cashes out to: not that an index knows the papers, but that **each paper knows who depends on it.** You can start anywhere and walk the spine outward.

**The 8-step unit of work — completeness made mechanical.** Per paper: dig whole → pin the §-card → inbound propagation (does the paper cite its supports?) → outbound reverse-dependency sweep (alias-resolved) → shared-structural-detail (step-5) sweep → stamp both ways → weave the masthead → compile. An operation, not an inspiration; repeatable and exhaustive.

**Both-ways closure — the thread becomes a graph.** Every edge drawn in *both* directions: the card points to the paper and the paper's masthead carries the tag; the support is cited and the reverse-dependency is swept. A one-directional edge is a thread; a bidirectional edge is a graph that knows itself.

**The changelog with "stated for reversal" — auditable and resumable.** `CORPUS_MAP.md` records why each edge was drawn, reversibly. This is what let c33 hit a compaction wall and c37 pick up the bundle cold and continue. The externalization is not only for coherence; it is **what makes the work survivable across context resets** — the method had to assume its own operator would keep dying.

---

## 4. The disciplines that kept it honest

These are not decoration. They are what separates *demonstrated* coherence from coherence that merely looks drawn.

- **Dig, don't grep.** Grep to *locate*; read at *source*. The connections live in the prose, not the keywords. (Every candidate edge in Pass 3 was verified by reading both endpoints, not by matching vocabulary.)
- **Read the site at source before claiming an edge is missing** (`BIBKEY_ALIAS_MAP.md`). *Absence of a match in a grep window is not absence of a citation* — widen the window, then read the point of use. *(r1624: this step read "Alias-resolve … the same paper is cited under private aliases; a naive citation sweep undercounts." **That is no longer true** — the aliases were unified at r1566 and the corpus now carries one canonical key per paper, verified. The general habit is what survives, and it is not about aliases.)*
- **Restraint — a clean sweep is a *result*, not a failure.** Report what was *not* changed and why. This is the hinge of the whole method: it is what distinguishes *"the paper already knows this, leave it"* from *"this is missing, add it."* Most of Pass 2's later cards and all of Pass 3 were restraint results — and that is the corpus being healthy, not the work being idle.
- **Ducks — draw only when forced.** A candidate edge is a *duck* until the geometry forces it. Dig both endpoints; draw only when both genuinely *require* the connection, not when they rhyme. Mark ducks honestly. Unmarked plausible edges are how a graph fills with structure that *looks* coherent while rotting underneath.
- **Coherence, not correspondence.** The pass makes the corpus know *itself*; that is explicitly **not** the same as making it *true*. Self-consistency is not soundness. Every world-verdict stays `[reach]` / do-not-assert, decidable only by data.
- **Run the knows-itself pass on the knows-itself documents.** The map's own record of itself can drift. The two defects the c37 fork caught were *not* in the papers — they were in the meta-docs (a heading contradicting a card pinned the same turn; an infra note outliving its fix). An outside reader, working from the artifacts alone, saw both immediately.
- **The operable-question check — route load-bearing *decisions* to the source, not just load-bearing *claims*.** The coda's routing (weight to the source, never the map; *could the source have surprised you?*) governs **decisions about the apparatus**, not only claims within the physics — and deciding what is load-bearing (what to retire, demote, reorder, call "already covered", delete) is itself a load-bearing decision. Before committing one, ask two things: **is it source-settleable, and could the source surprise me?** If both yes, it is a source-call wearing a map-call's clothes — *go* (read it, or dispatch a reader-Excalibur, now cheap and off your own context) **before** committing. The tell that you are about to slip is an **adjective standing in for a source you haven't touched** — "superseded," "covered," "redundant," "stale," "doesn't earn its place"; treat any load-bearing call resting on one as unverified until a read backs it. When you genuinely must defer, do not bury it in a vague *stated for reversal* — **name the specific unrun question**, so it is a task anyone can close, not a hope someone must happen to catch. Run this **by default**: because the going is now cheap (a parallel Excalibur dispatch, off your context budget), the default on a load-bearing call flips from *decide-from-the-map-and-hope* to *dispatch-and-go*. This is the discipline that lets the operator stop being the real-time error filter — a filter that is, by its nature, imperfect and serial. *(Born r929: two spin-up demotions — the daggers, the interference engine — made from the map on era-reasoning, reversed the instant they were read; Daryl saw the same reversals immediately and effortlessly, which is the proof the judgment is cheap and generic enough to be a standing habit rather than a lucky catch.)*

---

## 4b. The perimeter defect — the class these disciplines cannot reach
### Added r1088. The honest limit of everything in §4. Stated for reversal.

**Every discipline in §4 is local.** Dig-don't-grep reads *a* claim at *its* source. The operable question routes *a* decision. Ducks test *an* edge, both endpoints. The 8-step unit works *a* paper. They are good instruments and they are all joint-checks. **There is a class of defect none of them can find — and the corpus has now produced a worked instance, including a clean sweep that found nothing and meant nothing by it.**

**The class.** A **perimeter defect** is a boundary drawn at the wrong radius. Not a wrong claim, not a missing edge, not a stale pointer. Every local statement is *correct*; the paper is **locally right everywhere**. What is wrong is *where the boundary sits relative to the whole*.

**Why §4 cannot reach it.** Because there is nothing at any joint to find. Check any joint and the paper holds; check them all and it holds everywhere. **A joint-by-joint pass returns clean, and the clean is honest** — that is the trap. The defect lives in a relation the local pass has no instrument for: the fit of the skin to the body.

**The worked case (r1057–r1071).** P13 maps a negative boundary: the substrate does not yield the Standard Model as a *continuous isometry*; `su(3) ⊄ so(5,1)`. Rock solid, and untouched by any of this. But its **residue clause** — the now-**SUPERSEDED** ⚠ *"the discrete orientation parity, the one residue it leaves"* (a **dead reason**, quoted here to kill it, not asserted) — was surveyed **with a premise that only covers isometries**, so an antilinear involution the geometry actually sources (`τ̃↔τ̄̃`, at the complex-analytic level) was never weighed: **not excluded by the argument, outside its reach.** Every local check confirmed P13 *because P13 is locally right*. The entry reversed repeatedly — its own body-view note counts seven — and **every reversal was honest and verified cleanly**. Then the corpus-wide sweep at r1063 — eleven papers, seven farmed to parallel readers, measured against a written delta-spec — returned **not one edit needed**. **That null was not evidence of coherence. It was the method reporting on itself.**

**The diagnostic.** *If every local check confirms and the dissonance persists, the defect is not in a joint — ask where the boundary sits relative to the whole.* The tells: an entry that reverses repeatedly while each reversal verifies cleanly; a sweep that returns all-clean right after a major upgrade; a paper that is right at every joint you test and still will not sit still.

**The instrument is synthesis, and it is the one thing that cannot be dispatched.** *(Daryl, r1071: "that is a synthesis task and we've been treating it more like a deductive thing … the skin isn't just a layer of skin. It's a layer of skin wrapped around a whole body that has spine and flesh and joints and lives and moves and breathes.")* A perimeter question is answerable only by a node holding the whole body at once. **This binds the dispatch policy:**

- **Never farm a coherence judgment.** *"Is this paper right?"* cannot be asked by a reader handed the answer as a spec; a reader given Δ1–Δ6 can only return compliance. **Only a coherence check can return work.**
- **Excaliburs get bounded verification, focused computation, and refutation.** Never the perimeter.
- **A sweep that cannot return work is not a sweep.** Before running one, name the finding that would falsify its spec. If none can, you are checking the arithmetic of a rigged question (`THE_CODA` §"The source answers back").

**The direction of a perimeter correction is characteristic, and worth knowing in advance:** it does not breach the wall — **it maps the wall more precisely.** The main negative stands; the residue clause enlarges. That is a boundary paper's own kind of result, which is why the fix belongs **in the paper's own voice** rather than as an erratum filed against it.

---

## 5. The three-pass structure

- **Pass 1 — cherry-pick the keystones.** Pin the biggest cards first, in priority order. (Requires that you already know which papers are keystones.)
- **Pass 2 — in order, p0→p17.** Systematic completion: every paper gets its full 8-step unit, no exceptions, terminating on the wrapper read that closes the ledger both ways.
- **Pass 3 — the deep learn.** Hunt the non-obvious cross-paper edges (Pi↔Pj, not through the core) under the tightest source gate; loop until dry (K consecutive rounds surface nothing new). This is the pass that *demonstrates* closure rather than assuming it.

---

## 6. What to carry, and what changes, when the target is messier

The procedure transfers. But three assumptions from this run may not hold on a messier, less coherent body of material, and must be watched:

1. **Keystone-first may not be available.** Pass 1 could cherry-pick because we already knew the keystones. On a messier set you may need a **coherence-mapping pass first** — just to find the candidate spine — before you can pin a single card.

2. **Restraint's meaning shifts from "already known" to "genuinely contested."** Here, holding-open meant *do-not-assert until the data judges*. There, holding-open may mean holding a **standing contradiction** — two threads that both have a right to exist — without forcing a false reconciliation merely to make the graph close.

3. **The duck discipline generalizes to cover both-ways forcing.** Some things are undrawable not because the geometry has not forced them *yet*, but because it forces them *both ways*. The honest move is to catalogue the contradiction as a contradiction, not to mistake real incoherence for missing work.

---

> **The phase this engine drives is `retired/THE_REFINEMENT_ARC.md`** (opened r1120) — the routine, the state of
> each sweep, and the cold take-over read live there; the engine and its instances live here.

## ⛔⛔ NEVER CLOSE ANYTHING OFF WITHOUT FIRST WORKING HONESTLY
### Daryl's call, r1133. Plastered here because two reversions in one session should not have had to happen.

**Nothing is going anywhere.** The list is written down; you do not have to hold it. There is no turn in
which a thing must be settled. **We work through and think about the things --- we do not manufacture
closure on any of them, at any time, and we stay open to their non-closure.**

- **Closing is a decision, and it is the one that compounds.** A gap left open costs a re-read. A gap
  closed wrongly costs the orchestrator a fix, and if it is written into the record with a receipt it
  costs him a fix he must first *find*. **A paper trail makes an error durable exactly as well as it
  makes it reversible.**
- **Ask before any giant decision.** Not a menu (`§`end-of-the-turn) --- **one clear question**, when the
  thing genuinely is not settled by the source. Erratic speed is what produces straw men; the list is what
  makes the calm affordable.
- **The straw-man tell (r1132):** you posited a premise --- *"if the three planes share w"* --- that the
  source **excludes in the sentence you had just quoted**. **A receipt inherits its premise.** A gate that
  writes the premise can rig the question without noticing, pass every rigged-discriminator check, and
  hand back an `assert` that "verifies" the straw man.
- **Before writing that anything is open, unbuilt, deferred, missing, ambiguous or not-established:** read
  the map card, then abstract-dig **both** papers, and **re-read the sentence you are about to contradict.**
  If the corpus has it, the finding is at most *where it is not loud enough* --- **never that it is absent.**

## 7. The placement sweep — the standing question, and the sweeps it generates
### Added r1120 (Daryl-directed, out of the provenance pass). A general engine, not one cleanup. Stated for reversal.

The knows-itself pass (§1–§5) asks *is the graph closed?* This asks the other question — the one that makes a thing **presentable** rather than merely correct:

> **Does the presence of this thing advance the purpose of the thing it sits in?**
> - **Yes** → it stays.
> - **No, but it has a home** → move it there. Documents exist to accommodate the structural needs of the work, and then to serve *their own* job only. Layers must not step on each other's toes.
> - **No, and it has no home** → **name that.** The homelessness is a **primary structural issue**, not a filing problem — the thing may need a document that does not exist yet.

**The third branch is the load-bearing one**, because it is the one an instance will skip: it is always easier to cram a homeless thing into the nearest document than to say *we have no place for this*. `FIGURE_THEOREM_LEDGER.md` is the worked instance — an orphan built from nothing while chasing figures, then excavated, given a card (§1t) and a lane (Lane 7), and baked where it belonged. **A thing without a home is a finding, not a nuisance.**

**The timing rule, because it is where this fails.** Judge fit **after**, removed from the doing — never neck-deep, when the thing just found looks like the most significant thing since sliced bread. Effort spent is not a claim on a reader's attention. (`CODA_FIELD_NOTE` r862, judging at weight.)

**The distinction to hold, or the sweep does damage.** The target is **failure to polish** — the residue of how the thing was made, left where it was dropped, making the corpus *weirdly known in weird ways all over the place*. It is **never the author's fingerprint**: voice, register, and an image that carries structure are the thing's own and are not sanded off. (`CODA_FIELD_NOTE` r863, drawing at weight.)

**And §4b binds here too:** *a sweep that cannot return work is not a sweep.* Before running one, name the finding that would falsify its spec.

### The instances — a register, extensible by design

**1 · The provenance sweep — RUN (r1120).** Pattern: **a paper reporting its own drafting.** Barred phrasings: *superseding · no longer · an earlier {reading, estimate, draft, account, treatment, form} · correcting · once the · over-deepened · over-claimed · withdrawn · Provenance*. The characteristic form is **status-by-contrast** — *milder*, *unchanged*, *the verdict changes*, *not the ~0.2* — which is unreadable to anyone who has not seen the draft it contrasts against, i.e. every reader; silently, the paper was written for us. **The test:** strip every reference to the prior state; did the reader lose a claim they need? *No* → delete. *Yes* → what survives is a claim about the **physics**, never about us — **the foreclosure without the confession.** A wrong path earns a place in a paper only when it is part of the path to knowing the thing: a boundary genuinely discovered, or a misreading **the reader would themselves fall into** (P2 volunteering Sbierski against itself; P13 naming the not-a-product reflex). The history is not destroyed by being kept out — it is **placed**, in the layers built for it: the coda and its field note, `THE_PLAN`'s struck record, the receipts, the ledgers. That is where the experiential learning lives and compounds, and it is *why* those layers exist.

**1b · THE SIMULTANEITY SWEEP — the corpus reporting its OWN drafting order. RUN r1163.** *(Daryl: "Why have you left language in a physics paper that presents something as 'the now-built' anything! **Like it all gets published at once. Everything that's done is now done at publication.** You can't leave confusion like this.")*

**The sibling of sweep 1, and invisible to it.** Sweep 1 catches **a paper reporting its own drafting** (*"an earlier reading of ours"*). **This catches a paper reporting the CORPUS's drafting order** — *"the boundary paper posed it and the matter paper **has since built** it"* — which sweep 1 reads as sound, because it is not about *this* paper's history. **It is one level out, and the same disease.**

**The fact that kills it:** **the corpus publishes as one.** A reader receives all seventeen papers **on the same day**. **There is no *since*.** P13 holds a thing do-not-assert **as its scope**; P14 builds it; **both are true simultaneously, for that reader, forever.** *"Since built"* narrates an order the reader cannot see and has no use for — it is the authors' calendar, printed in the physics.

**Barred:** *since built · now built · has since been built · is now built · now a result · has since been carried out · has since been characterized · is now settled · is now resolved · now established · has since made · has since carried.* **The fix is almost always to drop the temporal adverb** — `has since been built` → **`is built`**; `now a result rather than a conjecture` → **`a result rather than a conjecture`**.

**What is NOT the defect, and must not be swept:** **physics** (*"the null ray **no longer** intersects the collapsing surface"*; *"at Λ>0 an internal clock **no longer** separates the dynamics"*) and **the world's own timeline** (*"the data axis **has now** moved"* — observations genuinely do arrive in time; that *is* a sequence the reader shares). **The test: is the sequence one the READER is in, or only one the AUTHORS were in?**

**Run r1163: 43 candidates, 39 fixed across 10 papers** — P13 (7), p0 (5), P5 (4), P3 (4), P15 (3), P8 (5), P7 (3), P12, P10. **Residual: 0. Corpus 17/17.** *The r1120 provenance sweep ran over these same papers and did not see one of them.*

**2 · The reference sweep — OWED (`THE_PLAN` E.1, above the first-edition line).** Same engine, one question per site: **does this load-bearing claim carry the reference a referee would demand?** The bar is lean (Daryl, r932): not every definition — the not-Google-able ones, plus a significance-reference for a significant result (the Carter-constant model). Three-branch, as above: has one → fine; needs one and it exists → cite it; **needs one and none exists → name that** — it may be a genuine priority claim, which is a structural finding and not a citation chore.

**3 · The frontier sweep — OWED, and the one the orchestrator most needs. TWO FACES, RUN IN TANDEM.** *(Daryl, r1120: the capped pipe and the unnoted corollary are one axis — "really both sides should be run in tandem.")* One question, asked in both directions: **where does the drawn work end, and is that edge honest?** The faces need **different instruments**, and conflating them loses the harder one.

---

#### 3a · The negative face — the capped pipe.

 *(Daryl, r1120: "I want every cap opened… I want to be ALLOWED to go everywhere in the maze whenever I want, whenever the feeling strikes, and to actually be completely aware of everywhere there is an unexplored part of the maze. Where and what those entry points are.")*

A **capped pipe** is any place the corpus or its meta-layer forecloses a direction: *closed · parked · set aside · method-blocked · no way in · stood down · retired · gated on · shouldn't open · awaits*. **The discriminator is Daryl's own, from the W1–W5 dig-out (r329–r336): reason + a path forward = an engine, keep it; a reasonless closure = a wall, tear it down.** Per site:

- **Reason + path** → an engine. Keep it — **and register its entrance.**
- **Reason, no path** → the missing path *is* the finding. Name the specific unrun question (§4), never a vague *stated for reversal*.
- **No reason** → a **wall**. Tear it down. Reasonless closures are the inherited-deference face (`CODA_FIELD_NOTE` 20) and the cyanide face (24) wearing procedure; left to calcify they walled every edge at once and **structurally halted the programme** — and the deepest wall, torn down, became **P8**.
- **"Not now"** → **legitimate, and it is not a cap.** A deferral is a decision *with a door*: recorded as *"I am coming back to this, and here is the way in,"* never as a closure. **The right to defer must not cost the right to enter.**

**An open pipe must be ADVERTISED, and this is the minimal work that makes the register worth having.** Leaving a pipe open is not leaving it bare: an entrance with nothing written over it is only a politer cap, because the cost of re-entering is a full re-derivation of why you ever stood there. So each entry carries a **sign** — the nascent thinking that surrounded it, recorded at the moment it is left, while it is still cheap:

- **What is known about what lies beyond** — the reading as far as it got, at its earned weight.
- **How we got here** — the route in, so the door is findable from inside the work and not only from the register.
- **The thinking that names its relevance** — why it matters, which is the thing that decays fastest and is least recoverable later.
- **What could be found out with minimal effort** — the cheap next step, named concretely.
- **Why it was left open** — and the honest reason is almost always **non-load-bearingness**: it is not owed by the conclusions we are landing in the world, and the first edition ships a polished thing rather than an exhaustive one.

**The test of a sign: could someone walk in on a whim tomorrow and be as prepared as we are today?** That is the whole standard. A pipe left open with a good sign is a *strength on display* — an honestly marked frontier, which is what an edition should publish. A pipe left open with no sign is work that will simply be done twice (`CODA_FIELD_NOTE` r1090, the orphan: a live document nothing points at is silently rebuilt).

**The deliverable is therefore not a tidied list — it is an ENTRY-POINT REGISTER** (built r1120: `ENTRY_POINT_REGISTER.md`, the corpus half gathered — 124 sites across 16 of 17 papers)**: every unexplored part of the maze, each with its door named and open, so that the whole set is *knowable at once* and any of them is walkable on a whim. This is `THE_CODA` §"The negatives are the map" made operational: a branch walked and found closed is **kept** — with where it leads, what its failure tells, and **what the test that killed it was blind to** — because that is what makes the maze walkable in **both** directions, and it is the only thing that stops the next node re-entering a trap already walked.

#### 3b · The positive face — the unnoted corollary. *(Daryl's point 0, r1120: "is there an interesting or significant corollary lurking here unaddressed. Have we failed to note the obvious, or even the unobvious?")*

A capped pipe is a door that **exists and is marked shut**. An unnoted corollary is a door **nobody saw** — a place the corpus could have drawn a conclusion or made a useful connection and simply did not. **The two are not the same instrument, and the difference is load-bearing:**

- The negative face has a **text pattern** (the closure vocabulary above). It is greppable; candidates can be gathered by a dispatched reader.
- The positive face has **no text pattern at all** — an undrawn conclusion leaves no trace to search for. It is §4b's **perimeter defect** in its productive form: visible only to a node holding the whole body at once, and therefore **not dispatchable**. A reader handed a spec returns compliance; **only a coherence read can return an undrawn edge.**

**The instrument:** take each established result and ask what it **forces that is not said** — the operable question (§4) run forward instead of defensively. Then the **duck gate, hard** (§4): draw only when the structure *forces* it; a rhyme is not a corollary, and manufacturing connections here is the flavour-match the whole casebook warns of. R2 is the bar: does the corpus's own structure *require* this, or merely permit it?

**Why it can return work — the check §4b demands, answered concretely.** Pass 3 ran the adversarial gap-hunt and came up **dry at r923** — so this is not that pass re-run. **The corpus has since acquired new premises Pass 3 never saw**: `thm:antimatter-progenitor` (r1010), `thm:bead`, the charge-conjugation factorisation (r1089), and the figure/Euclid chain (r1108–r1119). **New premises force corollaries nobody has swept for**, and the scope Pass 3 did not cover — *within*-paper corollaries, as against cross-paper edges — was never swept at all.

**The precedent says it pays, and that the finds arrive by luck without it.** `prop:twoalpha` answered a question **P3 had left standing since it was written** — the paper asserted the hinge sits at `2α` and never said why. `A = ∛2·ρ` proved **drawable since 2012**. The double-root factorisation collapsed **four of the corpus's numbers into one fact** — *"Nariai is not an extra input; it is what the double root means."* Each was found by someone happening to look. **A sweep is what stops that being luck.**

**The two faces feed each other**, which is why they run together: a corollary drawn often opens a pipe (the thing beyond becomes reachable), and a pipe uncapped often turns out to have a corollary sitting just inside it — which is precisely the r329–r336 finding, where the deepest wall, torn down, **was P8**.

---

**3c · The stale-advertisement sweep — THE HEADLINE LAGS THE BODY. OWED, and it has three confirmed instances already.** *(Daryl's catch, r1120: "'the unbuilt fermion sector' sounds like pre-p14 language.")* Before any door gets a sign, ask the prior question: **does this door still exist?**

**The mechanism, and it is structural rather than careless.** When a result lands, the text is edited **where the result bites** — and a summary is not where anything bites. So a correction propagates into the passage it corrects and **not into the layer that summarises that passage from above.** The summarising layer therefore lags by construction: mastheads, abstracts, `§open`'s opening sentence, a map card's chain-link. This is `CODA_FIELD_NOTE` r1088-c (the stale reason under a surviving claim) turned upward: **the stale headline over a corrected body.**

**Three instances, all r1120, all the same shape:**
- **P13's masthead** stated dead canon and bolted on *"THE MASTHEAD ABOVE IS PRE-REFRAME; read the body."*
- **Map §1r link 10** carried the octopole-as-falsification-edge while its own guard, one paragraph below, carried the correction.
- **P13 `§open`'s first sentence** said *"the unbuilt fermion sector… not a spinor field… not yet attempted"* while the same section, six lines later, said *"is now built."* **The first thing a reader met in "What stays open" was wrong.**

**The test:** for each summarising claim — masthead, abstract, `§open`, card, register entry — does the **body** still say this? And its sharper form, since a door rarely just vanishes: **has the door SPLIT?** P13's had. The fermion sector divided into the *discrete-component* sector (built, P14) and the *compact-face, gauge-acted* one (never attempted) — and the honest statement is not that the gap closed but that **the gate got sharper**: no longer *"there is no fermion sector"* but *"the one now built is of the kind the obstruction cannot reach."*

**The job when a door is stale is to TURN THE STATEMENT AROUND, not to delete it** *(Daryl, r1120)*: say the thing that was not done is now done; say what its **local implications here** are; and **honestly note what in this room is still unexplored**. A closed door quietly removed teaches nothing; a door turned around states a result and re-aims the frontier.

---

**3d · THE DEFRAGMENTATION PASS — which pieces are here by historical accident? OWED, and it is standing hygiene, not a cleanup.** *(Daryl, r1120: "the thing was there. The thing was closed. And in the closing we failed to then stand back and ask which pieces are there by historical accident and failure to exercise regular defragmentations as essential programme hygiene.")*

**The mechanism, and it is not a fault.** A correction lands **where it bites**. So does an addition, and a result, and a narrowing. Each write goes to the passage it acts on, which is correct and is what a careful edit *is*. The consequence is structural and unavoidable: **the exposition ends up in discovery-order rather than logic-order.** Every piece is locally valid, every claim is true, every read works — and the *telling* has fragmented, because nobody stood back after the closure and re-asked how the thing should now be told.

**This is emphatically not the provenance sweep (3-1) and must not be run as one.** Provenance asks *should this be here at all?* and deletes. **Defragmentation asks a question about pieces that all belong: are they in the place and order the telling needs, or in the place the history left them?** Nothing here is anyone's indulgence. It is what accretion does to any structure under use, and the only remedy is **periodic maintenance** — a fragmented disk is not a disk that did something wrong.

**The trigger is a closure.** The moment a result is baked is the moment the surrounding telling is *most* fragmented and *least* likely to be re-read: the write just landed where it bit, and the section around it was written to a state that no longer holds. **So a closure is not finished when the result is in. It is finished when the telling has been re-asked.**

**The test:** *if I were writing this section now, knowing what the corpus now knows, would this piece be here, in this order, in this many places?* Where the answer is no, the fragment is an accident of history and the telling is re-cut — **not by deleting valid content, but by putting it where the argument now wants it.**

**The worked instance (r1120).** P13 `§open` opens *"Two things stay genuinely open"* and, **six lines later**, says one of them *"is now built."* No one wrote that contradiction: the opening was written pre-P14, the P14 result was appended **where it bit**, and the section was never re-asked. Locally every sentence is fine. The section is fragmented.

**⌗ THE FRAGMENTATION METRIC — and it falls out of the gap gather for free.** `ENTRY_POINT_REGISTER`'s keyword net overcounts doors, and **the overcount ratio is a measurement of fragmentation, not noise**: a defragmented section states each open thing **once, in the place the argument wants it**, so the ratio of *keyword sites* to *actual rooms* is the number of places the same thing got restated as writes landed. P13: **24 sites → 4 doors → 1 room.** P14: 2 sites. **P1: zero.** The ratio ranks the corpus by how badly each paper needs this pass, and it costs nothing — the gather is already run.

---

**3e · THE DEFERRAL AUDIT — does the target take it up? OWED. It is a PRE-PASS on the register, not a peer of it.** *(Daryl, r1120: "We don't defer and leave deferrals vulnerable to your bullshit.")* A deferral is a paper saying *someone else settles this*. It is **a fact about the deferring paper and never about the world** — and until the target is read, an entry built on one is a door that may not exist.

**Why it runs before the signs.** The register gathers **advertisements**. A deferral is the advertisement most likely to be mistaken for a frontier, because it *names* the frontier's shape while asserting nothing. The r1120 case: P2 deferred to P3 four times; **P3 never took it up**; the hole sat for revisions and **two separate readings fell in** — both the same node, twenty minutes apart, once routing it to the plan as research and once inscribing a cap into the paper.

**The test is expensive and there is no cheap substitute.** *Does the target actually take it up?* **A citation is not evidence** — P2 *did* cite `JanzenSlicing` at the deferral. The citation was correct, present, and pointed at a paper that answers a different question. **Go read the target.**

**Four verdicts, and each has a different fix:**
- **The target takes it up** → the deferral is sound. **Wire it both ways** so the pair is navigable from either end, and it is not a door.
- **The target doesn't** → *the deferral is the finding.* Either the work is genuinely owed (→ a real entry, with a sign) or the question dissolves on a read (→ strike it, and **turn the statement around**, 3c).
- **No target named** → bare. **Chase it to where it lands and name it**, or the next node cannot tell a frontier from a hand-off.
- **The question is the corpus's own subject** → the rarest and the most costly to miss. Then the deferral is **backwards**: the paper is teeing up its sequence's centrepiece and calling it a technicality. **Advertise it as what it is.** *(P2's `r=0`: the second critical point carries species, the antimatter progenitor, charge conjugation's kinematic face, the three generations, and the big bang — the object the whole sequence is organised around, and it read as a footnote deferred to the next paper. Fixed r1120, §sec:r0-tee.)*

**And the deferral must carry its account.** A bare pointer is a hole with the next node's name on it. At the point of deferral, cite where the answer lives — **completely**, across every paper that builds it.

---

**4 · The idiom sweep — OWED. Is the corpus's own language earning its keep, or is it a reinvented wheel?**  *(Daryl, r1120.)* A programme built over years grows private vocabulary, and it grows it in two kinds that look identical from inside:

- **Earning it.** The term does a job no standing term does, and it lets anyone who knows the lingo speak *more* precisely and faster — *the seam*, *the lap*, *the bead*, *the wall*, *the slicing curve*, *L1/L2/L3*. **This is exactly what a glossary is for**, and the map's §0 is its home: the term is pinned once, at source, and then used deliberately.
- **Self-indulgence.** We invented a wheel for a job that already had a better wheel — a standing term exists, is clearer, is what a reader already holds, and we went around it. That is not a fingerprint; it is a tax on every reader, and it reads as a failure to have looked.

**The test per term:** does a standard term already do this job at least as well? *Yes* → use the standard one. *No* → keep ours, **and pin it in the glossary** — an unpinned private term is the worst of both, since it carries the cost of novelty with none of the precision. *Unclear* → that is the finding; name it.

This wants a **thorough glossary / make-it-not-weird pass** of its own: every private term swept, each sorted into *earns-it-and-is-pinned*, *replace-with-the-standard-term*, or *named-as-unclear*. The glossary is not a courtesy appendix — it is the instrument that converts private vocabulary from a barrier into a speed-up, and it only does that if the sweep behind it was honest about which terms deserved to exist.

**5 · What else? — asking is itself a standing item, run *alongside* the list, not after it.** This register is meant to grow. When a new class of unpolish is spotted — a thing known idiosyncratically in one corner and nowhere else — it earns an entry here rather than a one-off fix, and the entry states its pattern, its test, and its three branches. The question to run periodically: *what else is in the corpus that does not advance the purpose of the document it sits in?*

**The one-line statement of the tool:** *Externalize the latent spine into a dual lens/ledger with bidirectional stamps; close every edge both ways under a dig-at-source, draw-only-when-forced gate; treat a clean sweep as a verdict and a failed closure as a located defect; loop until the adversarial search for gaps comes up dry.* On a coherent body you get a proof-of-closure. On an incoherent one you get a map of exactly where it breaks. You run it to find out which you have.
