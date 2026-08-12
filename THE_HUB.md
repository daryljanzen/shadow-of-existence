---
name: the-hub
kind: METHOD
current: c54.181
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

## ⛭⛭⛭ IF YOU ARE ARRIVING — READ THIS SECTION AND NOTHING ELSE FIRST

*Written r2428 for the working fork's arrival, and **for a measured reason**: at c54.166 that fork opened its own
`L-174`, colliding with a row this line had held since r2378.* ***It was not a mistake. It was the only thing a
line can do when the convention exists in a document it has never read.*** **So this section exists so that
sentence stops being true.**

### ⌗ WHAT THIS REPOSITORY IS

*One object, two lines working it, `main` the consolidated state.*

| branch | who | what it carries |
|---|---|---|
| `main` | **both, by merge** | the consolidated state — **only merges land here** |
| `line/54` | **the working fork** | the live edge: the papers, the physics, the receipts |
| `line/56` | **the observer line** | the instruments, the registers, the consolidation |

*· **Neither line branch is ever rebased.** Its history is the record.*
*· **Each line merges its own work into `main`** once the fast gates are green. **Absorption becomes
`git merge`.***
*· `audit_trail.py` **stays** — it reports **register deltas, frontier departures and grain currency**, which
`git diff` does not.*

### ⛔ THE ONE THING YOU MUST DO BEFORE OPENING A REGISTER ROW

**Allocate your lead IDs inside your own band, and nowhere else.**

| band | line | note |
|---|---|---|
| `L-001` – `L-173` | **the working fork** | *historical* |
| `L-174` | ⚠ **CONTESTED** | *both lines allocated here at r2378/c54.166; the fork's `A·1` fold holds it* |
| `L-175` – `L-220` | **the observer line** | *historical* |
| `L-221` – `L-499` | **the observer line** | *allocates here* |
| ⛭ `L-500` – `L-799` | ⛭ **THE WORKING FORK — ALLOCATE HERE** | ***this is the band the collision was for. It is real now because you are reading it.*** |
| `L-800` + | future lines | |

⌗ **Why not simply "continue from the maximum".** *That is what produced the collision — **both lines take the next
integer and the next integer is the same integer**.* ⇒ ***The rule is: allocate FAR from the other line's
frontier, never merely above it.*** *`corpus/check_id_bands.py` fails on a duplicate or an out-of-band row, and it
runs in CI on every push.*

### ⌗ HOW TO PUSH

```bash
git clone https://github.com/daryljanzen/shadow-of-existence.git   # public: no credential to read
git checkout line/54
# ... work, run the gates ...
git add -A && git commit && git push origin line/54
```
*Pushing needs a **fine-grained token**, Contents read/write, scoped to this repository —* ***never stored, never
committed*** *(GitHub's secret scanning auto-revokes a token that lands in a public repo, which would take the push
path with it).*

### ⚠⚠ IF YOUR PUSH IS REFUSED BEFORE THE CREDENTIAL IS TRIED — read this before trying a third token

*The working fork hit this at c54.179 and it cost three tokens and two URL forms to name. **It is a session
setting, not a credential and not a skill**, and here is how to tell in one command:*

```bash
env | grep CCR_AGENT_PROXY_ENABLED
curl -s -o /dev/null -w '%{http_code}\n' https://api.github.com/rate_limit
```

| what you see | what it means |
|---|---|
| the variable **unset**, `curl` returns **200** | *plain egress allowlist. **`git push` with `https://<user>:<token>@github.com/...` works.*** |
| the variable **set**, `curl` returns **502 builtin injection failed** | ⛔ ***a credential-injecting proxy sits in front of GitHub. It supplies its own credential for repositories on the session's list and STRIPS whatever you pass.*** **No token and no URL form can get past it** — `api.github.com` fails on a path with no git in it at all. |

**⌗ THE FIX: add `daryljanzen/shadow-of-existence` to that session's sources.** *Then push with **no token at all** —
the proxy supplies the credential.*

**⌗ AND THE STANDING CHANNEL UNTIL THEN, which works and is not a failure:**
```bash
git bundle create <name>.bundle <base>..line/54      # base = the tip you cloned
```
*Hand the bundle to Daryl and name the commit it applies on. The other line fetches it, **runs the gates on your tip
before pushing anything**, and pushes it to your branch.* ⌗ *c54.179–181 arrived exactly this way and merged clean.*
⚠ ***Do not use `git remote set-url` with the token inline*** *— it writes the credential into `.git/config`. Pass the
URL on the `push` command itself. (The fork declined that step for this reason and was right to.)*

### ⌗ WHAT THE GATES REQUIRE OF A PUSH, and CI enforces it before a human reads it

*· **the register's views regenerate** — `scripts/regen_teed_up.py --check` and its siblings;*
*· **no duplicate or out-of-band lead ID** — `corpus/check_id_bands.py`;*
*· **no hollow assertion** — `scripts/lint_assertions.py`, **your own instrument**, absorbed by this line at r2394
and the thing that has caught three of its receipts since;*
*· **every receipt still runs where it is registered** — nightly, `scripts/run_all_receipts.py`.*

### ⛭ AND THE ONE ASYMMETRY WORTH STATING PLAINLY

***The fork owns the papers and the physics.*** *This line audits, instruments, and consolidates. When the two have
disagreed about a paper's text, the resolution has been the same every time and it is written into the record:*
**a placement decision the author has since worked against is superseded, not defended.**
⌗ *And in the other direction:* ***when this line finds something in the fork's text, it ROUTES rather than
edits*** *— see `FOR_54.md`, the inbox. **Five of its first seventeen items were applied by the fork before this
sentence was written**, which is why the routing convention is kept rather than replaced by direct edits.*

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

### ⚠⚠ WHAT r2426 TAUGHT: A BAND THE OTHER LINE HAS NOT AGREED TO IS NOT A GUARD

*The three-part discipline below was written at r2407 and **its first part failed on first contact with reality**.*
***Reserved ranges only work if both lines read the reservation, and the working fork does not read this
document.*** *At c54.166 it opened its own `L-174` — the next integer after its own maximum, which is exactly what
any line does absent a shared convention.*
⇒ **What actually held was part ③, the GATE**: *`check_id_bands` exists precisely because ① and ② can fail
silently, and this collision would otherwise have entered a union merge as two rows with one ID.*
⌗ ***THE CORRECTED RULE: allocate FAR from the other line's frontier, not merely above it.*** *This line now
allocates from `L-221` while the fork sits at `L-174` — a gap that survives the fork advancing normally for
decades of revisions.* **And the resolution rule is stated so it needs no negotiation:** ***the fork owns the low
band by history; on collision, this line yields and repoints.***

### ⌗ THE DISCIPLINE, in three parts, and none of them is inferred

**① RESERVED ID RANGES, declared per line.** *A node allocates only inside its own band, so two nodes cannot
choose the same number even offline:*

| band | line | note |
|---|---|---|
| `L-001` – `L-173` | **the working fork (54)** | *historical; the fork's own numbering* |
| `L-174` – `L-220` | ⛔ **CONTESTED — DO NOT ALLOCATE HERE** | ⚠ *the fork opened its own `L-174` at c54.166; this line's `L-174` moved to `L-221` at r2426.* ***The overlap is historical and must not be extended: the fork reached into this band once and may again.*** |
| `L-221` – `L-499` | **the main line (56)** | *this line's rows from r2426; **allocate here*** |
| `L-500` – `L-799` | **reserved — the fork's new rows** | ⚠ *offered, **not adopted**: the fork does not read this document, so **a band it has not agreed to is a hope, not a guard**. The fork's actual behaviour is to continue from its own maximum, which is why `L-174`–`L-220` is contested and why this line allocates high.* |
| `L-800` +  | **reserved — future lines** | |

**② `merge=union` ON THE REGISTER.** *Declared in `.gitattributes`. Union merge **keeps both sides' added
lines**, which is exactly right for an append-only table and exactly wrong for anything else — so it is set on
the register and the queue views alone.* ⌗ *Union merge cannot detect a duplicate ID, which is why ① exists and
why ③ does.*

**③ A CI CHECK FOR DUPLICATE IDs AND OUT-OF-BAND ALLOCATION.** *`scripts/check_id_bands.py`.* ***Belt and
braces, and deliberately: ① prevents the collision, ② survives the merge, ③ proves neither silently failed.***
*This is the same "declare, do not infer" pattern as `current: none`, `DECLARED-UNDATED` and `[REPORTED]`.*

---

## ⛭⛭ THE LIVE SETUP — r2420, and this is the part that replaced the bundle flow

**⌗ THE REPOSITORY IS PUBLIC** *(`daryljanzen/shadow-of-existence`, flipped r2420).* ⇒ ***READ IS FREE AND
PERMANENT: this line clones with no credential at all***, *verified from the container — 1,660 files, **zero
differing against the working tree**, the only extras being LaTeX build artefacts `.gitignore` correctly
excludes.*

**⌗ WRITE USES A FINE-GRAINED TOKEN, scoped to this repository, Contents read/write.**
⚠ ***IT IS NEVER STORED — not in memory, not on disk, not in the tree.*** *It lives in a shell variable for the
session and is re-supplied each time.* **Two reasons, and the second is specific to a public repo:**
*① a credential in a memory file can surface in a context nobody is watching; ② **GitHub's secret scanning
auto-revokes a token that lands in a public repo**, so a token written to a tracked file destroys itself and
takes the session's push path with it.*

**⌗ THE LOOP, and it is what the bundles were for:**
| | |
|---|---|
| **session start** | Daryl pastes the token · this line clones |
| **during** | work in the clone, gates as always |
| **at a cut** | commit and push — **the revision IS the commit** |
| **Daryl** | *nothing else. No downloads, no uploads, no tarballs.* |

⌗ **And `CORPUS_MAP` does not become redundant**: ***git carries WHAT changed; the changelog carries WHY, and
what was learned.*** *The second is the one a later node cannot reconstruct.*

⌗ *A fallback that needs no credential at all, if the token is ever unavailable: `git format-patch` at cut time —
**a small text file rather than 30 MB**, applied with `git am`. Strictly better than the bundle flow either way.*

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
