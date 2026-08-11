> **⌗ RETIRED r2380 under `RG-1`.** *The r2377 edit log. **Its content is the `### Revision r2377` entry in
> `CORPUS_MAP`**, which carries every finding; this file's unique contribution is the **per-edit reversal
> instruction**, kept for exactly that. r2377 is cut, checksummed and handed over, so this is a record of a
> shipped revision.* ⌗ *Later revisions record their edits in the changelog directly — this file was a
> first-session scaffold and is not continued, which is itself the disposition: **a scaffold that outlives its
> session becomes a second changelog**, and the corpus already learned that lesson at `CONSOLIDATE` §11.*

---

# Edits carried into r2377 (from r2376+c54.108)

Working tree: /home/claude/cr/x — this is the bundle content.
Each entry: file · locus · what · why · how to reverse.

1. `corpus/janzen_circle_v3.tex` §sec:ring (L511)
   - **Was:** `...the ones the cosmological constantThe cycloid itself establishes only that the extra roots are the ones the cosmological constant supplies;`
   - **Now:** the single clean clause; the duplicated truncated copy removed.
   - **Why:** verified textual defect — a doubled sentence-head with no line break, ungrammatical as written.
   - **Reverse:** restore the doubled string.

2. `corpus/groupoid_paper.tex` `rem:family-global` (L637) — one insertion-splice, two sites
   - A later block (*"The same partition is reached independently from the substrate's null
     structure…off the cover."*) was spliced into the middle of an existing sentence, between
     `…rather than assumed~\cite{…};` and `the discrete skeleton this grades…`. The result read
     `…; The same partition…` (capital after a semicolon) and `…off the cover. the discrete
     skeleton…` (lowercase after a full stop).
   - **Fix:** `…assumed~\cite{…}; The` → `…assumed~\cite{…}. The`; and `off the cover. the
     discrete skeleton` → `off the cover. The discrete skeleton`. The inserted block stays where
     it is; the host sentence's second clause now stands as its own sentence.
   - **Why:** verified splice — the two punctuation errors are complementary halves of one
     interruption, and the minimal repair preserves both authors' content without reordering.
   - **Reverse:** restore the semicolon+capital and the period+lowercase.

## Scan run (r2377)
`corpus/*.tex` swept for (a) words duplicated with no intervening space and (b) sentences opening
lowercase after a full stop. Two real defects found, both above. All other hits are inside `%`
comment blocks or the all-caps note prose of `appendix_receipts_*.tex`, where they are not defects.

3. `corpus/range_paper.tex` abstract
   - **Was:** `…which is what one closed family read two ways requires.. \emph{Charge enters…`
   - **Now:** single full stop.
   - **Why:** stray double period. Swept `corpus/*.tex` for the pattern; this was the only instance.
   - **Reverse:** restore the second period.

## Scan run 2 (r2377, after step 5)
`corpus/*.tex` swept for doubled function-words outside `%` comments. No defects: all five hits
are intentional (`ONE one-dimensional`, `two two-dimensional`, `not not-geometric`).

4. `corpus/make_receipt_appendix.py` (per-paper scope branch) + the 5 appendices it regenerates
   - **Was:** the `corpus` scope deduped rows by stem; the per-paper scope did not. A duplicate
     ledger row in `receipts/INDEX.md`, or one stem borrowed from two papers, therefore emitted
     `\label{rcpt:<stem>}` twice in a paper's Appendix R — multiply defining it, so `\rcpt{}`
     resolved to whichever copy came last.
   - **Now:** the same first-row-wins dedupe applied in the per-paper branch, with a comment
     naming why.
   - **Effect on regeneration** (`python3 make_all_appendices.py`, run): P6 −4, P13 −1,
     P14 −1, P3 / P5 / P7 duplicates cleared. Corpus-wide sweep for duplicate `\label`s and
     dangling `\ref`s now comes back clean.
   - **Why:** verified defect, fixed at the generator rather than in the generated `.tex`, so it
     does not come back on the next regeneration. The generator's own docstring already names
     "a duplicate ledger row (which multiply-defines the label in the book build)" as a prior
     workaround for this gap — the gap was simply left open on the per-paper side.
   - **Note (not fixed):** the duplicate rows in `receipts/INDEX.md` are still there (e.g.
     `P14_even_crossing_index` at L23 and L199, the second with a different `label`/`claim`).
     The generator now tolerates them; whether the ledger should carry one row or two is Daryl's
     call, not a defect I can settle.
   - **Reverse:** delete the added dedupe block and re-run `make_all_appendices.py`.

## Scan run 3 (r2377, after step 7)
`corpus/*.tex` swept for duplicate `\label`s and `\ref`/`\eqref` with no target, comments
excluded. Clean after the above. (One apparent hit, `prop:twoalpha` in
`geometric_core_paper.tex`, is inside a trailing `%` comment recording an earlier fix.)

## Verification run (r2377, after step 8)
Ran the corpus's own gates from `corpus/`:
- `check_compile.py` — **all 17 papers compile at 0 errors, 0 undefined citations, 0 undefined
  refs, 0 dead receipt links.** This is the confirmation the edit-4 generator fix landed cleanly:
  the appendices were regenerated and every `\rcpt{}` still resolves.
- `check_citations.py`, `check_receipts.py`, `check_withdrawn.py`, `check_supersession.py` — all
  exit 0. `check_receipts` reports 0 uncited-receipt debt from the current fork (2 older backlog);
  `check_withdrawn` reports no bare occurrences.
- The 20 cross-paper label collisions `check_compile` lists are all `[note]` class (`sec:intro`
  and the like), 0 of theorem class — the gate's own reading is that these are benign in
  standalone builds. Not touched.

## Position correction (r2377 read)
I numbered the read one step ahead from step 7 onward: P15–P17 is **one** step (README step 7), and I
split it across two turns as "7" and "8". Material order intact — every document read in README order,
nothing skipped, merged, rearranged or revisited — so the break-condition was not met and no repair was
needed beyond renumbering. Corrected before step 8 (the coda) was read. Recorded here because the drift
was mine and the record should carry it.

5. The r2234 insertion splice — 10 sites across 6 top-level documents
   `c22_keepers.md` ×4 · `ONTOLOGY_FOUNDATION_INDEX.md` ×2 · `RATE_HANDOFF_DERIVATION.md` ·
   `A4_matter_seam_crossing_build.md` · `OPEN_PROBLEMS_MAP.md` · `CR_COLLAPSE_HELD_PICTURE.md`
   - **Was:** `…the beginning is the branch point at $r=0$ (well-posed because $r_*$ CONVERGES, **not**
     because curvature is finite -- it diverges there; r2234) $r=0$, …` — the r2234 parenthetical was
     inserted with an anchor ending before the original `$r=0$`, and the replacement restated `$r=0$`,
     so every site carries the symbol twice with the parenthetical wedged between.
   - **Now:** the stranded second `$r=0$` deleted at all ten sites.
   - **Second defect at 3 of the 10** (the `[†ONT-COSMO]` guard block, copied verbatim into
     `RATE_HANDOFF_DERIVATION` / `OPEN_PROBLEMS_MAP` / `CR_COLLAPSE_HELD_PICTURE`): the same edit left the
     superseded clause `, not r=0.` standing immediately after the sentence that now asserts the beginning
     **is** $r=0$ — the pre-r2234 claim contradicting its own correction, in the same sentence.
     **Now:** `, not the seam.` — which is the contrast the sentence was drawing, and is settled by the
     naming rule's own line on the branch point: ***NOT a seam.*** Stated for reversal.
   - **Why:** verified defect at both levels. The stranded symbol is mechanical; the fossil clause is a
     live contradiction inside a guard block that exists to stop a veer, so it was the more costly of the
     two. Note this is the eighth face's exact signature — a correction reaching one grain of several, the
     `c22_keepers` and index copies never carrying the `not r=0` tail while the three guard copies did.
   - **Reverse:** restore the doubled `$r=0$`; restore `, not r=0.` at the three guard sites.

## The currency audit (r2377) — Daryl asked whether the plan still holds the live edge

**The plan itself is current** (head sections at c54.86–c54.106; the operating layer intact). **The
register layer around it is not, and the gate built to catch that could not fire.**

6. `corpus/check_currency.py` — **the baseline was itself a watched document.**
   - **The defect:** the gate read the fork's current state from `FORK_c54.md` alone. `FORK_c54.md` is a
     standing record that lapses like any other, and it did — its header still declares
     `**Fork state:** r2376+c54.35` while the fork has run to **c54.108**. So the reference point sank
     with the documents it was measuring, and the gate reported *"Every standing register is current"*
     with `CORPUS_MAP` at lag 3 and `INDEX` at lag 0. **A manufactured null:** for exactly the documents
     that lag hardest, the instrument could not return a non-null result.
   - **Now:** the front is the maximum over the watched registers **plus** `FORK_HISTORY_c54.txt` and
     `THE_PLAN.md`; a register that is ahead *defines* the front and can no longer be dragged down by one
     that stopped moving. `FORK_c54.md` added to the watch list. Rationale written into the docstring.
   - **What it says now (rc=1):** `CONSOLIDATE` −76 · `CORPUS_MAP` −76 · `INDEX` −73 · `FORK_c54` −73.
   - **Reverse:** restore the single-file baseline.

7. `WHATS_TEED_UP.md` + new `scripts/regen_teed_up.py` — **the working queue had inverted.**
   - Its own frontmatter says it is *"regenerated by parsing THE_LIVE_ARC each turn"*, and nothing did the
     parsing — it was regenerated **by hand at c54.65** and not again. At c54.108 it listed
     **44 leads, all 44 of them struck**, and **none of the 14 actually open**. Not merely stale:
     exactly inverted. *A stale card misinforms a node; a stale queue dispatches one* — a node opening it
     would have been sent to re-work forty-four finished leads.
   - **Now:** `scripts/regen_teed_up.py` parses the register (`| **L-N** |` live, `| ~~L-N~~ |` struck) and
     writes the queue with state, origin and first-move columns; `--check` exits 1 when the queue and the
     register disagree, naming both directions. Queue regenerated at c54.108: **14 open, 141 struck.**
   - **Reverse:** delete the script and restore the hand-written file.

**⚠ SURFACED, NOT WORKED — these are Daryl's, not mine.**
   - **`CORPUS_MAP.md` carries ONE c54 changelog entry (`c54.10`) for a fork that has run 108 revisions.**
     The plan's "closing a state advance" step 1 requires a dated `### Revision` entry per advance. I will
     not reconstruct 76 revisions of changelog from the arc — that would be fabricating a record, and the
     changelog is the one grain where a claim and its later correction sit together.
   - **`INDEX.md` (−73), `CONSOLIDATE` (−76), `FORK_c54.md` (−73).** `FORK_c54.md`'s `Fork state:` line is
     a one-line factual error I could correct, but its body (merge notes, collision surfaces) describes
     c54.35; updating only the header would make it claim a currency the body does not have.
   - **`FORK_HISTORY_c54.txt` stops at c54.93** (15 behind), which may simply be uncommitted work.

**What ran clean:** `check_compile` (17 papers, 0 errors / 0 undefined refs / 0 dead receipt links),
`check_citations`, `check_receipts`, `check_withdrawn`, `check_supersession`, `check_burndown`
(155 registered, 141 struck, 14 open, 0 HOT), `check_queues`, `check_kills` (12 protected items, no
unauthorised closures). `check_grains` **SKIPPED** — it needs git history the bundle does not carry, so
that gate has not been running here either.

8. `CONSOLIDATE_THE_PLAN_AND_INDEX_THE_PROGRAMME.md` — **`ARC 14 · THE SINGLE EDGE` written into §2**
   (Daryl-directed), plus four wiring edits: the arc named as LAYER 1's instrument in the arc sequence;
   the head banner's stale currency claim (c54.32) corrected with the reason the gate could not say so;
   the live-queue line updated to say the queue is now generated; §0's working set annotated to point at
   the register as the live edge.
   - The arc's own §① records a **third instrument defect, found by writing the arc**: `check_currency`
     measures currency as "highest fork revision mentioned in the file", so writing a section about being
     76 revisions behind made the file pass. The fix (a declared `current:` frontmatter marker, written
     only by the pass that brings a file current) is step ①'s deliverable; until then the gate's FAILs are
     findings and its PASSes are not.
   - **Reverse:** delete the `ARC 14` section and the four wiring edits.

## ARC 14 — first working session (r2377)

**New scripts (5):**
- `scripts/classify_documents.py` → `DOCUMENT_LEDGER.md`. 141 documents: **1 SOURCE · 4 VIEW ·
  27 STATE · 17 METHOD · 52 RECORD · 40 UNCLASSIFIED**. Classification is *declared* (frontmatter
  `kind:` or an explicit table), never guessed; the unclassified count is step ④'s worklist.
- `scripts/regen_teed_up.py` → `WHATS_TEED_UP.md` (14 open / 141 struck), with `--check`.
- `scripts/regen_burn_down.py` → `THE_BURN_DOWN.md` live block. It had been reporting **88 / 19 /
  74 / 20 HOT** against an actual **155 / 141 / 14 / 0** — 80 revisions behind. The c54.27–c54.28
  historical argument is preserved verbatim below the generated block.
- `scripts/id_space_census.py` → `ID_SPACE_CENSUS.md`. Six namespaces still outside the register:
  `PROTECTED_OPEN` 6/12 · ledger families 8 · **P7 `sec:frontiers` 6** (independently confirming
  the c54.86 audit's "seven items, now six") · p0 `sec:frontiers` 4 · CONSOLIDATE arcs 14 and
  phases 9 · 12 residual map codes. **It censuses; it does not fold.**
- `scripts/build_fork_span.py` → `CORPUS_MAP` §`THE c54 FORK SPAN`: 56 commit subjects copied
  **verbatim** from `FORK_HISTORY_c54.txt`, marked as commit subjects and not changelog entries,
  with the 3 revision numbers missing from the commit record named rather than smoothed over.

**Rewritten:** `corpus/check_currency.py` — front = max over all fork-carrying documents; watch
list = the classifier's LIVE set (30 documents, 22 failing); currency read from a declared
`current:` marker where present, with the body scrape reported as the weak proxy it is.

**Declared markers added:** `THE_LIVE_ARC` (SOURCE, c54.108) · `WHATS_TEED_UP` / `THE_BURN_DOWN` /
`DOCUMENT_LEDGER` / `ID_SPACE_CENSUS` (VIEW, emitted by their generators) · `CORPUS_MAP`
(STATE, **c54.32 — the truth, so the gate keeps failing on it**).

**Verified after all edits:** `check_compile` 17 papers, 0 errors / 0 undefined refs / 0 dead
receipt links · `check_receipts` 0 debt from this fork · `check_withdrawn` clean · `check_kills`
12 protected items, no unauthorised closures · `check_burndown` ID space intact.

**Owed and stated, not hidden:** step ② the fold itself (a reading job) · step ③'s remaining two
views · step ④ the 40-document record cut (must not be batched) · `check_grains`'s no-git
fallback · a `check_changelog` · and the `current:` marker on the other 26 STATE documents.

## ARC 15 — the observer line (r2377, second session)

**The two-line structure written into `CONSOLIDATE` §2 as `ARC 15`**: the working fork runs the
live edge; this line audits the trail, absorbs the advances, and makes the programme
self-maintaining. **Prime directive: this line does not collaborate with the working fork.** The
one exception is a catastrophe ahead of it, which is the orchestrator's call to carry, and the bar
is destruction, not disagreement.

**New instrument: `scripts/audit_trail.py`** — takes two trees, reports DROPPED · SHRANK (a
look-signal, never a verdict) · ADDED · THE WAKE · STALENESS DELTA · REGISTER DELTA · PAPER
FRONTIERS. Renders no verdict on the physics. First run filed as `TRAIL_AUDIT_c54.134.md`.

**The absorption protocol** (6 steps, in `ARC 15`): audit before reading · read every dropped and
shrunken file at source · re-apply this line's repairs **after checking the fork did not fix them
first** · regenerate every view · run every gate · file the audit as a RECORD.

**The merge, c54.134 + r2377:**
- 0 files dropped by the fork; all 10 r2377 text repairs re-checked against c54.134 and **all 10
  still needed** — re-applied (P2 duplicate, P5 splice ×2, P9 double period, 10 stranded `$r=0$`
  across 6 documents, 3 `not r=0` fossils).
- `make_receipt_appendix.py` dedupe re-applied; appendices regenerated; `check_compile` clean.
- `check_currency`, the five generators and `audit_trail` ported. `CONSOLIDATE` and `CORPUS_MAP`
  copied whole after verifying the fork touched neither.
- Views regenerated at c54.134: `WHATS_TEED_UP` **6 open / 160 struck**, `THE_BURN_DOWN` likewise,
  `DOCUMENT_LEDGER` 141 documents, `ID_SPACE_CENSUS` 6 namespaces unfolded, `CORPUS_MAP` fork span.

**The catch, fixed here and NOT routed to the fork:** `README.md` and `INTRODUCTION.md` both still
read *"seven families are open and named"*, naming two the fork closed at c54.113 and c54.118 and
propagated to the papers and the ledger. Corrected to four, each with the closing revision named
and a pointer to the ledger as the source.

**Gates on the merged tree:** `check_compile` 17 papers / 0 errors / 0 dead receipt links ·
`check_kills` clean · `check_burndown` ID space intact · `check_receipts` clean · `check_withdrawn`
clean · `check_currency` **rc=1, 28 documents named** — which is the honest number.
