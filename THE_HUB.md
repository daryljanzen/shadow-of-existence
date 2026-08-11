---
name: the-hub
kind: METHOD
current: c54.163
job: How the programme lives in a git repository — branch discipline, the register's merge rule, what CI enforces and what it cannot. Read BEFORE pushing, and BEFORE assuming git has solved a problem it has not.
sources: [chat]
---

# THE HUB — the programme in a repository

> **⛭⛭ WHY, AND IT IS NOT PRIMARILY THE MERGING (Daryl, r2407).**
> ***"This is how we eventually make contact with 54. By inviting it to the repo."***
> *The working fork has **first contact slated as its item 18**. The repo is the venue: a place both lines can
> hold the same object without either handing the other a tarball and hoping.* **Private to start** — *which
> makes the publish decision a separate, deferrable one and costs nothing to defer.*

---

## ⌗ WHAT GIT SOLVES HERE, and these are real

*Four problems this line has been solving by hand, each with a revision number attached:*

| the hand-rolled thing | what git does |
|---|---|
| **the pristine baseline** *(r2384: six of our own files in a baseline would have reported as **dropped by the fork**)* | a baseline is a **commit**; the failure mode ceases to exist |
| **`reapply_annotations.py`** *(r2385/r2393: an annotation to a fork-owned file is dropped by every absorption **with no trace in the diff**)* | a merge **keeps both sides** and conflicts loudly when it cannot |
| **`check_absorption`'s declared record** | `git rev-list --count` — *exact, not declared* |
| **bundles and three-way merges** | branches |

## ⚠⚠ WHAT GIT DOES **NOT** SOLVE — and this is the part to hold

***Every defect the r2377–r2406 consolidation found was SEMANTIC, and git merges text, not meaning.***
*Git would have caught **none** of:*

- *`PO-8` listed open while its register row is struck;*
- *ledger family 6 pointing at `L-164` after `L-164` was struck;*
- *`README`/`INTRODUCTION` saying "seven families are open" and naming two that closed;*
- *a verdict written into a prose block instead of the row the parser reads;*
- *a section **heading** indexed as a door;*
- *95 receipts that ran green and **could not fail**.*

⇒ ***THE GATES ARE THE LOAD-BEARING PART AND THEY STAY.*** *What changes is that they run **in CI on every
push** rather than because somebody remembered — which matters given the lesson already banked:*
**an instrument that cannot finish inside the harness that calls it will be skipped by every caller who does not
know that.**

---

## ⛔ THE ONE HARD PROBLEM: `THE_LIVE_ARC`

*It is a **423 KB single-line-per-row table that every node writes to**. Git merges it line by line, so two nodes
adding rows land at the same place — a conflict every time, or worse, a **silent interleave**.*
⚠ *And the ID space has been a **near-miss twice by luck**: this line's rows begin at `L-174` only because the
fork's maximum was `L-173`, and the fork has still not opened a row above it.*

### ⌗ THE DISCIPLINE, in three parts, and none of them is inferred

**① RESERVED ID RANGES, declared per line.** *A node allocates only inside its own band, so two nodes cannot
choose the same number even offline:*

| band | line | note |
|---|---|---|
| `L-001` – `L-173` | **the working fork (54)** | *historical; the fork's own numbering* |
| `L-174` – `L-499` | **the main line (56)** | *this line's rows since r2378* |
| `L-500` – `L-799` | **reserved — the fork's new rows** | *so the fork may open rows without collision* |
| `L-800` +  | **reserved — future lines** | |

**② `merge=union` ON THE REGISTER.** *Declared in `.gitattributes`. Union merge **keeps both sides' added
lines**, which is exactly right for an append-only table and exactly wrong for anything else — so it is set on
the register and the queue views alone.* ⌗ *Union merge cannot detect a duplicate ID, which is why ① exists and
why ③ does.*

**③ A CI CHECK FOR DUPLICATE IDs AND OUT-OF-BAND ALLOCATION.** *`scripts/check_id_bands.py`.* ***Belt and
braces, and deliberately: ① prevents the collision, ② survives the merge, ③ proves neither silently failed.***
*This is the same "declare, do not infer" pattern as `current: none`, `DECLARED-UNDATED` and `[REPORTED]`.*

---

## ⌗ BRANCHES

```
main                  the consolidated state; only merges land here
  ├── line/56         this line — the consolidation, the gates, the registers
  ├── line/54         the working fork — the live edge
  └── work/<topic>    short-lived, off whichever line owns the work
```

*· **A line branch is never rebased**; its history is the record.*
*· **A merge into `main` requires the fast gates green** (below).*
*· **Absorption becomes a merge**, and `audit_trail.py` stays — because it reports **register deltas, frontier
departures and grain currency**, which `git diff` does not.*

---

## ⌗ CI, AND IT IS TIERED FOR A REASON

*The suite is not uniform in cost, and pretending otherwise would produce a pipeline nobody waits for.*

| tier | what runs | when | cost |
|---|---|---|---|
| **fast** | the sixteen text/register gates + all six view `--check`s + `check_id_bands` | **every push** | seconds |
| **compile** | `check_compile` (17 papers through LaTeX) | **every push to `main`, nightly on lines** | minutes |
| **heavy** | `run_all_receipts` (~9 min), `check_receipts_run` | **nightly and on demand** | minutes, and **needs `camb` + `pynucastro`** |

⚠ ***The heavy tier is where this container cannot verify***: *ten receipts import `camb`/`pynucastro`, declared
by name in `check_receipts_run`. **In CI they can actually run**, which is a genuine gain — the fork's own rule,*
**"a registered receipt that does not run where it is registered is not a receipt"**, *becomes checkable
everywhere rather than only where the fork sits.*

---

## ⌗ WHAT IS TRACKED, AND WHAT IS NOT

*Text is **31 MB** of 72; the rest is binaries.*

| | |
|---|---|
| **tracked** | `*.md`, `*.tex`, `*.py`, `*.sh`, `*.bib`, `receipts/`, `computations/` sources |
| **ignored** | LaTeX build output (`.aux .log .out .toc .fls .fdb_latexmk .synctex.gz .bbl .blg`), `__pycache__`, `*.pyc` — *the same list `cut_bundle.sh` excludes, which is why a correctly-cut bundle always looked like it dropped 58 files* |
| **LFS** | `*.pdf` (12 MB), `*.png`/`*.eps` (27 MB), `*.dat` (3 MB) — *the Planck likelihood matrix, the thesis figures, the compiled papers* |

⌗ *`CORPUS_MAP.md` is 4.2 MB and **append-only**, so it diffs cheaply and should stay in-tree: **git gives you
what changed; the changelog gives you why, and what was learned** — and the second is the one a later node cannot
reconstruct.*

---

## ⛭ AND THE THING THE REPO DOES NOT CHANGE

***The register is still the one ID space, the gates are still the instruments, and a verdict still has to be
written where the parser reads it.*** *A repository makes concurrent work possible and provenance exact. It does
not make a claim true, a receipt able to fail, or a document current.* **Those were always the work, and they
remain it.**
