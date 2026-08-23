---
name: the-arsenal-index
kind: REFERENCE
current: r2676+c54.211
job: The grid — which paper × which tool, run or owed, in what order. Campaign R (the two reach theatres) and Campaign C (opens · closures · dissolutions · equivalences · pry-aparts).
sources: [cowork]
---

> **▣ REFERENCE — the grid.** *Which paper $\times$ which tool, run or owed, in what order: Campaign R
> (the two reach theatres) and Campaign C (opens, closures, dissolutions, equivalences, pry-aparts).*
>
> *It records its own worst failure and the lesson is the reason to keep it: a row read **"OWED P8--p0"
> for roughly 140 revisions after the sweep that discharged it had finished.** **What is open is
> `THE_FRONTIER.md`.***


## ⛭⛭ BROUGHT CURRENT c54.211 — **four gates entered the arsenal since c54.201, and one of them is a gate ON a gate**

*· **`check_kind`** (r2656) — *did every turn marked COMPUTED actually compute something?* **Built after
56 predicted the failure for a 54 and found three instances in its own log.** The hand-kept KIND ledger
is the only thing that can answer it, so the gate checks the ledger against the receipts.*
*· **`check_no_stdlib_shadow`** (r2675) — *does any script shadow a stdlib module name?* **Built from
`L-541`'s finding that `scripts/queue.py` shadowed `queue`**, which `concurrent.futures` imports, so the
receipt runner died in its first second and left the last good result on disk. ⇒ ***A crash that leaves
a cached success presents as staleness, not as failure.***
*· **`check_receipts_run`, re-armed** (`L-541`, c54.208) — *the gate itself was green on a result file
written 294 commits earlier.* **A cache with no expiry is not a measurement.** The runner now stamps a
`TREE-DIGEST` over everything a receipt can READ and the gate fails on a mismatch or on its absence;
both failure modes seeded, and a forged cache claiming "436 pass, 0 fail" is rejected on the digest.*
*· **`check_dupes`** (r2649) — *a paper cannot say the same thing twice.*

⌗ ***WHAT THE GRID SHOULD NOW CARRY AS A COLUMN: whether a tool reads a CACHE or the TREE.*** *That was
the distinction the arsenal had no way to express, and it is the one that let a green gate stand for
294 commits.*

---

## ⛭⛭ BROUGHT CURRENT r2449, TO c54.185 — **AND TWO INSTRUMENTS EXIST THAT THIS GRID DOES NOT LIST**

> ⚠ *This index is "the grid — which paper × which tool". **Two tools were adopted at r2443 and r2446 and never
> entered here**, which is the grid failing at its own job rather than a marker going stale.* ⌗ *Caught by
> `check_currency` while triaging twenty-four stale documents; **two of the twenty-four were missed landings and
> not stale markers**, and this is one.*

### ⌗ THE LINT LAYER — new, and deliberately NOT the gate layer

| tool | from | paper × cell | what it asks | why it is not a gate |
|---|---|---|---|---|
| `corpus/check_loci.py` | **node 52** | **P15** (2 flags, 1 a predicted false positive) | *does a sentence assert a property of the **locus its receipt computed**?* | ***its contributor measured its own precision before shipping*** — assertion-shape **3/3** against word-presence at **42%** |
| `corpus/scope_table.py` | **node 55** | **P15 only** — every flag, corpus-wide | *what parameter values does each receipt **actually run at**?* | the `DELIBERATE`/`BY_DESIGN` lists are **maintainer judgements**, and ***a gate can check a declaration, not a judgement*** |

**⇒ AND THE GRID GAINS A NEGATIVE RESULT WORTH MORE THAN EITHER TOOL** *(`L-230`, r2447): a blind run of
`scope_table` across all seventeen papers put **every flag in P15 and none in P14** — where the class's clearest
instance lives.* ⌗ **The reason is structural:** *`scope_table` measures **disagreement between receipts**, and that
defect's signature is **agreement**.* ⇒ ***INCONSISTENCY IS MANY VALUES WHERE ONE IS CLAIMED; OVERREACH IS ONE VALUE
WHERE MANY ARE CLAIMED — an instrument tuned to the first is blind to the second by construction.***
⚠ ***So this grid should not record an overreach cell as covered. It is not, and no tool here covers it*** *— the
route is a **convention** (`COMPUTES:` headers, carried by 39 of 309 receipts), routed to the fork as item 30.*

### ⌗ AND THE GATE LAYER ITSELF MOVED

*· **`check_loci` and `scope_table` are NOT in the CI gate list**, by decision.*
*· **The fast tier ran none of its text gates from r2427 to r2439** — `classify_documents --check` failed on
twenty-eight unclassified restored files, and `set -e` aborted the step on its first command (`L-227`). **Fixed:
the tier now runs every check, collects failures, and fails at the end naming all of them.***
⇒ ***A suite run by hand and a suite run under `set -e` are different instruments — the first reports every failure,
the second reports the first and hides the rest.***


# THE ARSENAL INDEX — the grid: which paper × which tool, run / owed, in what order

> **⌗ RE-READ AGAINST c54.163 AND DECLARED CURRENT r2396.** *No `species`, no harmonics, no receipt claims —
> **none of the span's three results touches a grid cell**. What did change is this line's own doing and is
> already recorded: Campaign C gained `C-E` and `C-P` at r2388 and their cells were filled by the r2388 combs.*


> **⌗ DATED r2389 — `c54.34`, the revision of its own `L-39` call, and it is the one instrument this audit
> actively CHANGED rather than only read.** *At c54.34 it settled the math-ledgers question **both ways**: three
> **instrument** ledgers get columns, five **archives** get a cross-reference and none — because* **"an archive's
> queue must be pruned against its own runs, and nothing did that"** *(`L-105`, now `check_queues`).*
> ⌗ **And at r2388 its Campaign C gained `C-E` and `C-P`**, *so the grid now carries all three censuses instead of
> one — the two duals had asked for a column and neither had been given one.* ⌗ *Its own dangling opens are
> unchanged and stated there: the R-M columns, the su(3)-upgrade fold, the GR corrective/generative split.*

> **⌗ `L-39` SETTLED r2376+c54.34 — the R-M columns, by my own call, since this is apparatus I built and keeping it usable is mine.** *The blocking question (the morph's face Q) was whether the **math ledgers** are arsenal rows at all — instruments the programme wields, or records of excursions it made.* ***The evidence now decides it, and it decides BOTH ways, which is why the question stalled: the answer is not one class.***
>
> **⌗ INSTRUMENTS — rows in the arsenal, with readiness states:** *`FIGURE_THEOREM_LEDGER` (it produced the hinge-null structure, ⊢58's falsifier and the Euclid protocol, and `L-77`'s locus sweep drew a live result out of it three turns ago) · `COMBINATORICS_LEDGER` (it adjudicates counts **14 papers now carry**) · `QUADRIC_GEOMETRY_LEDGER` (the doubly-ruled structure and the confocal identification are live).*
>
> **⌗ RECORDS — archive, cross-referenced but not rows:** *`OPTICS_LENSING` · `CATEGORY_THEORY` · `CONFORMAL_GEOMETRY` · `COMPLEX_ANALYSIS` · `VARIATIONAL`. **Basis: the c54.13 deepening re-ran 49 exposed probes across these and 39 came back clean — the behaviour of an archive.** And at c54.34 three of their queue entries turned out to be **stale text quoting questions the ledgers themselves had already answered** (`L-25`, `L-31`, `L-33`).*
>
> **⚠ AND THE CONSEQUENCE, WHICH IS WHY THE CALL MATTERS:** *an archive's queue must be **pruned against its own runs**, and nothing did that — which is `L-105`, now a gate to build. **The columns stay open only for the three instrument ledgers; the five archives get a cross-reference and no column.***

> *(r1444: this file's `§972` references were stale line-numbers — P7's open-problems section had moved to line 1152. Replaced with its label `sec:frontiers`. Cite by label, never by line.)*
*Opened r1279 (Daryl). The readable tracking card across the whole arsenal grid, so nothing is lost as we
build and run — "so we're not only driven by intuition but also tracked systematically, to clean up the
places intuition doesn't reach and complete the thorough comprehensive thing." **We do NOT run the arsenal
again until this index is built and reflects the true state.** Living; updated every time a tool is run on a
paper. Structure mirrors the layered face in `THE_ARSENAL.md`. This is a v1 DRAFT — some cells carried from
the r1276 coverage tracker are marked to verify in the morph; the R-M columns are placeholders pending the
math-ledgers question.*

**Legend:** ✓ run at weight · ~ partial/started · `·` owed · ⚠ STALE (a dependency advanced past it — owed a
re-run) · — n/a. Cell = status (+ rev). **Ordering & staleness across the grid are governed by
`retired/THE_DEPENDENCY_LEDGER.md`:** bring an upstream target to STABLE before finalizing its dependents, so a
finished cell isn't staled by a later move; the dependency ledger names the highest-leverage next target
(the open one gating the most dependents).
**Uniform baseline (not gridded):** Level-3 ground tools (base up-to-weight + bespoke) and Level-2
passes 1–3 (up-to-weight, su(3)-upgrade, open-problems) + pass-4-**corrective**: **DONE P1–p0, ALL 17**
(corrected r1444 — this line read "DONE P1–P7, OWED P8–p0" for ~140 revisions after the r1406 sweep finished
P8–p0 on the eleven-avenue gamut and certified the corpus. The *grid below* remains accurate: it tracks the
REACH and CONSOLIDATION campaigns, which are a different thing from the per-paper up-to-weight sweep and are
genuinely still mostly owed.)
The grid below tracks the LIVE edges: GR-**generative**, the other physics sub-axes, and the Consolidation
divisions.

---

## Campaign R — THE REACH · Theater R-P — Physics
| paper | GR (generative) | QM | QFT | SM/gauge/SU(3) |
|---|---|---|---|---|
| P1  | ✓ r1210/1267 (BH problems, 4th) | · | · | ~ su3-upgrade |
| P2  | ✓ r1269 (cycloid/OS) | · | · | ~ su3-upgrade |
| P3  | · (corr✓; local-cosmic used in P7) | · | · | ~ su3-upgrade |
| P4  | · (empirical anchor; used in P7) | · | · | ~ su3-upgrade |
| P5  | ✓ r1276 (S₃=Galois) | · | · | ~ su3-upgrade |
| P6  | · (corr✓; discipline used in P7) | · | · | ~ su3-upgrade |
| P7  | ~ **OPEN** r1278–79 (2 passes, more likely) | · | · | ~ su3-loc |
| P8  | · | · | · | · |
| P9  | · | · | · | · |
| P10 | · | · | · | · |
| P11 | · | · | · | · |
| P12 | · | · | · | · |
| P13 | · | · | · | ~ su3-loc (the home) |
| P14 | · | · | · | ~ generations (3 chiral) |
| P15 | · | · | · | · |
| P16 | · | · | · | · |
| p0  | · | · | · | ~ su3 + ħ co-location |

## Campaign R — THE REACH · Theater R-M — Mathematics
> ⟐ COLUMNS UNSETTLED — the R-M sub-axes depend on the math-ledgers question (face Q). Placeholder until the
> morph decides which of `THE_GEOMETRY_AND_THE_PHYSICS` / `GEOMETRY_PHYSICS_TAXONOMY` / `COMBINATORICS_LEDGER`
> / `FIGURE_THEOREM_LEDGER` / `CONSTANT_LEDGER` (+ new forms) are the live columns. **Do not populate yet.**
>
> **⌗ AND THE GRID HAS A MISSING AXIS, found r2376+c54.11 — it is not a column, it is a ROW CONDITION.**
> *This index tracks **which paper × which tool**. Every cell so far was filled against a **four-dimensional
> cut**, and at the time nothing distinguished **structural** from **true at $D=4$** — so a probe could be
> marked ✓ *run at weight* while carrying a verdict wider than its computation's scope. **One has been found
> (optics `O6`); five others re-ran and survived, narrowed, or answered an open queue item.***
> ⇒ ***a cell is not `✓ run at weight` until its constants have been re-derived on the $D$-dimensional $f$.***
> **Audit and re-runs: `THE_DIMENSION_DEEPENING_AUDIT.md`.** *This is a staleness condition of the same kind as
> the ⚠ flag the legend already carries, and it applies **retroactively to every filled cell in both theaters**.*

| paper | geometry? | combinatorics? | figures/thm? | constants? | [new?] |
|---|---|---|---|---|---|
| P1–p0 | — pending R-M decision — | | | | |

> ## ⌗⌗ `C-E` AND `C-P` ADDED r2383 — **the two duals of `C-D` had no column, and both censuses had asked for one**
>
> ***`THE_EQUIVALENCE_STRUCTURES_CENSUS` and `THE_PRY_APART_CENSUS` each close with the same unmade request***:
> **"register as a FAMILY-of-families in the arsenal, each item to comb + propagate across the corpus (both ways
> on the identified papers), feeding the full-corpus read-through."** *Neither was registered.* **`C-D
> dissolutions` had a column and its two duals did not** — *the same finding as the `whole-corpus-instrument`
> class one layer down: the dissolution census was classed, its duals were not.*
>
> **⌗ THE THREE ARE A DUAL TRIPLE, and the columns now show it.** *A **dissolution** says a standard problem
> stops being a problem · an **equivalence** says two apparent things are ONE read two ways · a **pry-apart**
> says one apparent thing is TWO a conflation welded.* **Both duals state the same level rule:** *the census
> metadoc is the single consolidated list at project level, and* ***"the CORPUS is NOT forced into one
> consolidated list — instances live distributed at synthesis-seams… more homes are to be FOUND by combing."***
>
> **⌗ CELL BASIS, so that no cell is invented.** *`✓ landed` **only** where a census records the entry as landed
> in the corpus: the equivalence census's two-turning-cubics (**P7 `rem:tworealisations` + P8
> `rem:turningfamily`, "landed both ways r1433"**) and the pry-apart census's turnaround-vs-$r{=}0$ (**P7
> `rem:twocritical`, r1425**). `~ seed home` where the census names that paper in its seed list. `·` where the
> comb has not reached.* ***Nothing here asserts a comb was run — `L-205` IS that comb, and these two columns are
> what it fills.***
>
> ⌗ **AND THE INDEX'S OWN `L-39` CALL IS WHY THIS FITS:** *at c54.34 the math ledgers were split — three
> **instruments** get columns, five **archives** get a cross-reference and none. **The censuses are neither**:
> they are the consolidation campaign's own product, which is why they belong in Campaign C beside `C-D` rather
> than among the reach theatres' ledgers.*

## Campaign C — THE CONSOLIDATION
| paper | C-O opens | C-C closures | C-D dissolutions | **C-E equivalences** | **C-P pry-aparts** |
|---|---|---|---|---|---|
| P1  | ✓ | ~ r1213 (cite-unread find) | ✓ (homed in P7) | · | · |
| P2  | ✓ | · | ~ (gestured, §454) | ~ seed home, comb owed | ~ seed home, comb owed |
| P3  | ✓ | · | · (owed vs P7 section) | ~ **+1 combed r2388** (one arc read two ways) | ~ seed home, comb owed |
| P4  | ✓ | · | · | · | ~ seed home, comb owed |
| P5  | ✓ | · | · | · | ~ **+1 combed r2388** (σ/R/ξ) |
| P6  | ✓ | · | · | · | ~ seed home, comb owed |
| P7  | ✓ | ~ r1212 (r=0 false-open) + r1279 | ✓ (**the home**: dissolution synthesis) | **✓** landed | **✓** landed · **+1 combed r2388** (α vs α/√3) |
| P8  | **✓ r1281** | · | **✓ r1281** | **✓** landed · **+1 combed r2388** (the seam IS an event horizon) | ~ seed home, comb owed |
| P9  | **✓ r1285** | · | **✓ r1285** | ~ **+2 combed r2388** (range boundary = dynamical matter · interior = expanding universe) | · |
| P10 | **✓ r1290** | · | **✓ r1290** | ~ **+1 combed r2388** (frozen constraint = true Hamiltonian) | · |
| P11 | · | · | **✓ r1296** | · | · |
| P12 | · | · | **✓ r1298** | ~ seed home, comb owed | · |
| P13 | · | · | **✓ r1302** | · | ~ **+1 combed r2388** — the three routes, the colour arc's central pry-apart |
| P14 | · | · | **✓ r1304** | ~ **+1 combed r2388** (the three walls, one object read three ways — **predicts NO mixing**) | · |
| P15 | · | · | **✓ r1416** | ~ seed home, comb owed | ~ **+3 combed r2388** — L1/L2/L3 · index vs multipole · possible vs required |
| P16 | · | · | **✓ r1415** | ~ seed home, comb owed | · |
| p0  | · | · | · | ~ seed home, comb owed | ~ seed home, comb owed |
> *(r1447: this row read `| P8–p0 | · | · | · |` — all owed. Corrected against `THE_OPEN_PROBLEMS_LEDGER`'s
> STATUS entries and `THE_DISSOLUTION_CENSUS`'s own per-paper sections, both read at source. The C-C closures
> column stays owed throughout — that sweep is genuinely unstarted.)*

---

## THE RUN LOG (chronological — what was run when, so the order is legible)
- **r1208–1210** — P1 dissolution census + dissolutions pulled from the origin paper (GR + C-D).
- **r1226–1230** — do-not-assert census / completion-shield disciplines forged (Level-3).
- **r1228–1229** — su(3) connection-upgrade (topological→analytic, S⁵) — the SM/gauge sub-axis's tool, P1–P7.
- **r1240–1244** — open-problems axis: false-opens struck, the seven `sec:frontiers` families fixed (C-O, P1–P7).
- **r1259–1264** — local-cosmic boundary (P3/P8/P6) — GR generative fallout.
- **r1267** — P1 laws of BH mechanics (the 4th) — GR generative.
- **r1269–1270** — P2 cycloid/OS identity — GR generative.
- **r1276** — P5 S₃ = Galois group of the horizon cubic — GR generative.
- **r1278–1279** — P7 GR generative: the dissolution synthesis + comprehensive applications section. **OPEN.**
- **r1279** — the fifth axis + closure self-check built (Level 1 frame + Level-3 discipline); this index opened.
- **r2376+c54.11** — **the dimension re-read**: six probes across the quadric, optics and category bakes re-run at general $D$. `O1` **strengthened** · `K8b` **grounded** · `K5` and `Q4` **narrowed** · quadric `4d` **answered** (the hinge triangle is NOT self-polar, and the question exists only at $D=4$) · `O6` **found with a verdict wider than its computation's scope**. R-M station **Ⓑ reopened one level up**; the trends map's **CUBIC** entry gains a fourth reading — *the cubic's degree is $D-1$*; `GEOMETRY_PHYSICS_TAXONOMY`'s standing obsession is **half answered**. No cell status changed; the row condition above is what changed.

## ⟐ THE INDEX'S OWN OPENS (dangling)
- The R-M columns await the math-ledgers question (face Q).
- Whether su(3)-upgrade is its own column or folds into SM/gauge/SU(3) (drafted as folded).
- The GR column collapses corrective+generative into one live-edge mark; if the morph wants them split, split.
- Cells carried from the r1276 tracker (esp. the ~ su3-upgrade row) to be verified paper-by-paper.
- Whether the baseline (passes 1–3 + corrective, P1–P7) wants its own gridded row rather than a prose note.
