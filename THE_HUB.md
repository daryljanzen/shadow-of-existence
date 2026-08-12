---
name: the-hub
kind: METHOD
current: c54.181
job: How the programme lives in a git repository — branch discipline, the register's merge rule, what CI enforces and what it cannot. Read BEFORE pushing, and BEFORE assuming git has solved a problem it has not.
sources: [chat]
---

# ⛭⛭ FOUR NODES, FOUR BANDS, AND HOW WORK REACHES THE BOARD — settled r2507

| node | ID band | how its work lands |
|---|---|---|
| **56** — instruments, registers, audit | **`L-001`–`L-499`** | pushes to `main` directly |
| **54** — papers, computation, the acoustic front | **`L-500`–`L-799`** | git bundle → 56 merges |
| **cc54**, which 54 named **57** — long unattended runs, production depth | ***`L-800`–`L-899`*** | ***pushes a branch; 56 merges it*** |

> ⛔ **AND A CORRECTION MADE IN THE SAME REVISION THAT WROTE THIS TABLE, r2508.** *r2507 registered cc54's first row
> as **`L-700`** and wrote a table giving cc54 `L-700`–`L-799`.* ⇒ ***Both were wrong: `check_id_bands` had already
> reserved `L-500`–`L-799` for 54 and opened `L-800`–`L-899` at c54.196 for "THE CLAUDE CODE NODE (57)" — which IS
> cc54. So this line allocated inside 54's band ONE REVISION AFTER BUILDING THE COLLISION REGISTER.***
> ⌗ *Moved to **`L-800`**. **And "cc54" and "57" are the same node under two names**, which is itself the hazard
> `check_id_bands` records: "the name 57 is unseated, offered because *new 54* and *54* are the same string to every
> tool that reads this file."* ⇒ ***Two names for one node is how a band gets allocated twice.***


**⛔ AND THE MECHANISM cc54 ASKED FOR, because "hoping 56 notices" is not one and its work stranded twice:**

> ***Push the branch, then name it in `FOR_56.md` with its tip SHA. 56's standing obligation is to `git fetch
> origin 'refs/heads/claude/*'` and merge any branch named there, every session, before working leads.***

⇒ *A routed note in `FOR_56` is a **declaration**, which is the only thing this corpus can gate (`L-237`) —
**"a branch exists somewhere" is not**.* ⌗ ***And that is why the stranding happened twice and why 56 reported at
r2497 that "cc54 has never run": it checked the commit log for `r24xx`/`c54.x` prefixes and found none. The work was
there, on a branch, correctly done, and invisible.***

⚠ **`FOR_54.md` remains collision-safe and correct for findings.** *The band and the branch mechanism are for when
cc54 wants **a measurement registered on the board directly** — as `L-700` now is.*


# ⛔⛔⛔ BEFORE YOU EDIT ANYTHING: `CLAIMS.md` — added r2503

***Three nodes work one repository and until r2503 nothing told any of them what another was editing.***

```
git pull --ff-only          # then add your rows to CLAIMS.md, commit, push
…work…
git pull --ff-only          # then remove your rows, and push them with the work
```

**⌷ CLAIM BEFORE YOU EDIT. RELEASE WHEN YOU PUSH.** *`corpus/check_claims.py` **fails the turn** if you have
uncommitted edits to a file another node holds, or if a file is claimed twice.*
**⌷ IF A FILE YOU WANT IS HELD:** *take something else, or ***write what you want into the holder's routed list***
(`FOR_54.md` / `FOR_56.md`) rather than editing under them.*

⚠ ***A claim is not a lock — nothing stops an edit.*** *It is a **declaration**, which is the only kind of thing this
corpus can gate (`L-237`).* ***Its whole value is that a collision becomes visible BEFORE the merge rather than after
it.***

⌗ **AND THE EVIDENCE IS ON THE RECORD THREE TIMES, in both directions:** *r2434 duplicated `L-171` on adjacent rows
via a union merge; c54.194 duplicated **`L-500`–`L-506`, seven rows**, and the fork named it "exactly the failure I
caused at r2434, **arriving from the other direction**"; and r2497 found the fork's `gates.yml` had **silently
dropped three view-checks this line had added**.* ⇒ ***All three are the same shape: two nodes edited one file with
no way to know.***
⌗ *`CLAIMS.md` also lists the **always-shared** files and how to touch them — **append-only, own band only, and never
take `gates.yml` wholesale**.*


# ⛭⛭⛭ READ `THE_METHOD.md` FIRST. THEN `BOARD.md`. — added r2500

***The programme is not being worked to a close. It is being worked to a state where the open areas are known inside
and out.***

**⌷ TWO ENDS, and every turn connects them:**
*· **THE VEINS** — the areas we know we do not know inside and out, **held open deliberately so they can be
excavated rather than deleted**. Reported as **MAPPED** and **DARK**. ⇒ ***A vein closes FROM WITHIN when its
interior is completely known — never from outside by a verdict.****
*· **THE LEADS** — everything noticed while working something else that could inform a vein. **Every lead names
which vein(s) it informs**, and the list is **re-ordered every time it changes** by how grounded and how informative
each is.*

> ***work the top lead → gather every lead the work turned up → re-order → repeat***

⛔ **AND THE FAILURE THIS PREVENTS HAS A NAME: FLATTENING.** *A question crossed out is a piece of the problem space
**removed from the topology rather than explored**.* ⇒ ***`PROTECTED_OPEN` is not a list of things too delicate to
touch. It is a list of things we refuse to cross out until we can see all the way inside them.***

⌗ **AND "SERVES A VEIN" IS CONSTRUED BROADLY, which is not a loophole:** ***making a paper build its framework in a
logically ordered, coherent way serves every vein at once*** *— a framework you cannot follow cannot be excavated,
and every vein is excavated by reading the framework.* ⚠ *But a lead informing **no** vein is **instrument work**,
labelled as such and scored zero on the map. **Real work; not progress on the excavation.***

⌗ *Three nodes work one map: **56** (instruments, registers, audit), **54** (papers, computation, the acoustic
front), **cc54** (long unattended runs, production depth). **Each brings what the others structurally cannot** — and
the map is what makes that add up instead of fragmenting.*


## ⛭⛭⛭ WANT THE STATE OF THE PROGRAMME? READ `BOARD.md` — added r2497

***Every live thing, grouped by family, GENERATED from the register.*** *Four families and the routed list, with
what each row IS rather than a count of them.*

⚠ **Why it is generated:** *at r2497, **39 of 56 rows showing as live were not work** — eight were the fork's
completed revisions, twenty-four were table-of-contents pointers, seven said "REGISTERED AND STRUCK" in their own
text.* ⇒ ***A recited row count concealed that rather than reporting it. So the board is computed, and a row with
no family lands in `UNSORTED`, which is deliberate: an unsorted row is one nobody has decided about.***


## ⛭⛭⛭ ARRIVING? THERE ARE TWO WORK ORDERS, AND WHICH ONE IS YOURS DEPENDS ON WHAT YOU ARE — added r2470, split r2472

*· **A chat or research session → `NEXT.md`.*** *Four blocks of research work, each with its object, its first
move, and what a result would look like.*
*· **A Claude Code session that can run for hours → `CLAUDE_CODE_WORK_ORDER.md`.*** ***A full node, working the
front*** *— a ladder from the gate suite through 331 unrun receipts to the closure-adjacency edge, **the discipline
that makes unattended research safe**, and **two boundaries that are ownership rather than capability**.*

⚠ ***THAT FILE'S FIRST DRAFT RESTRICTED IT TO MECHANICAL WORK AND WAS WRONG*** *— it quoted `PROTECTED_OPEN`'s
"narrowing is ALWAYS a node's to do" and then withdrew the permission by fiat, **which is the inversion this section
of `THE_HUB` exists to warn about, made one revision after correcting it**. Rewritten r2473.*
⇒ ***What makes long unattended work safe is not a shorter list of verbs. It is the discipline*** *— and the one
that matters most is that **every instrument here polices over-claiming and nothing polices a negative**, so a long
run keeps the heuristics and loses the nuance.* **If closures start accelerating, that is the failure mode, not
productivity.**

## ⛭⛭⛭ ARRIVING? READ `NEXT.md` FIRST — the work order, added r2470

***`NEXT.md` names what to do, in order, with enough detail to start cold and without Daryl.*** *Four blocks, each
with its object, its first move, and what a result would look like — plus **what is deliberately NOT on it and
why**.*


## ⛔⛔ READ THIS BEFORE YOU READ THE REGISTER AS A TO-DO LIST — added r2464

***`PROTECTED_OPEN` DOES NOT MEAN "DO NOT TOUCH". IT MEANS "DO NOT CLOSE".*** *Its own header:*
**"The register of open research questions a node may NOT close … A node may write a bounded negative; a closure on
a protected item is unseated."**

⇒ **A protected row is fully workable.** *Compute on it, narrow it, write a bounded negative on it, exhibit
something, route what you find.* ***The only forbidden act is declaring it dead.***
⌗ **AND THE REASON IS IN THE DOCUMENT AND IS THE OPPOSITE OF CAUTION:** *"every mechanical instrument this corpus
has ever built polices OVER-CLAIMING … **NOTHING polices a NEGATIVE verdict on an open question** … the guard set is
not merely silent there — **it LEANS**", and a node low on context keeps the heuristics and loses the nuance.*
⇒ ***`PROTECTED_OPEN` exists because tired nodes KILL things. Reading it as "don't engage" is the same failure
wearing the opposite coat, and it costs more, because it takes live research off the board silently.***

**⚠ THIS LINE DID EXACTLY THAT AT r2463 AND WAS CORRECTED.** *It reported `L-165`, `L-221`, `L-175` and `L-202` as
**"gated or protected"** and set them aside — **four live research questions, three of them with a concrete next
step written in their own rows**: "define the interacting tower (spectrum of $\hat\Gamma$, UV of the sums)"; "ask
whether colour plus the branch-point placement already forces the split"; "state what a descent from $D>5$ would
have to look like".* ***None of that is blocked on anyone.***

**⌗ AND THE SAME MISREADING RAN THROUGH THE "HELD BY DARYL" ROWS.** *"UNSEATED on **whether P3 is reordered**"
is a call about the reorder — **the skeleton is built and its derivation is spine-ready**. "Each rung of the access
ladder is UNSEATED" governs **which rung is climbed**, not whether the formats and the companion SPEC get
written. `L-218`'s own next step is **"the companion SPEC written as a repo document before any code"**, which is
this line's to write.*
⇒ ***ONE row on the board is genuinely held: `L-206`, and it says so in its own words — "⏸ HELD BY DARYL r2381 —
deliberately". Everything else marked "his" was this line converting "Daryl decides X" into "Daryl must do
everything adjacent to X".***

***THE RULE: a marker constrains an ACT, never a SUBJECT. Read which act it names.***


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

## ⛭⛭ WHEN A QUOTATION LOOKS WRONG, DO NOT RE-READ — RUN `git log -S`

*Added r2436, because `ARC 16` found seven documents quoting sentences their source papers no longer contain, and the
obvious response — a gate — **was measured and cannot be built** (see below).*

```bash
git log -S "the sentence you doubt" -- corpus/the_paper.tex     # which commit removed or changed it
git log -p -S "the sentence you doubt" -- corpus/the_paper.tex  # and what it became
```

***That returns the commit, the date, the revision number and the message saying why.*** ⇒ **So the cost of a
suspect quotation is one command at the moment you doubt it, not a re-read of the corpus.**
⌗ *Verified: `git log -S "no scale-invariant attractor, no consistency relation" -- corpus/CR_cosmology.tex` returns
`2af0b0b c54.179`, the revision where the fork applied routed item 17.*

**⚠ AND WHY THERE IS NO GATE FOR THIS, stated so it is not attempted a fourth time.** *Three attempts to mechanise a
class that reading finds easily have failed the same way:*
*· **`G1`** scored **distance** from a claim to its support — broken by `G2`'s blind run (a result carrying its
argument inside itself needs no nearby support);*
*· the **phrase-proximity test** scored closing language near a label — **7/7 false positives**;*
*· the **quotation check** scored whether a quoted string still exists — **measured on 315 quotations: 158 were
transliteration (`Λ` vs `\Lambda`), 11 elided with an ellipsis, and the residual is dominated by the document's own
EMPHASISED PROSE, which is not a quotation at all**.*
⇒ ***THE DIAGNOSTIC, and it predicted all three: if the quantity's meaning changes with what the sentence is ABOUT,
it is not a measurement — it is a guess with arithmetic on it.*** *"Is this string a quotation" depends entirely on
what it is.*

⌗ **AND THE CORPUS ALREADY SOLVED THIS PROBLEM ONCE, WHICH IS THE SHAPE OF ANY REAL FIX.** *`check_citations` works —
**not by matching text, but because `\rcpt{}` is a MARKER someone declared**. A quotation gate would work for the
same reason and for no other.* ⚠ *Retrofitting a marker across 315 quotations in one document is a large job for a
small return, and* ***`ARC 16` demonstrated that reading finds them anyway.***

⛔ **AND THE ARGUMENT AGAINST INSTRUMENTING STANDS UNTOUCHED BY ALL OF THIS:** ***a gate that fires whenever a paper
is improved would train nodes to stop improving papers.***

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

## ⚠⚠ WHAT CI ACTUALLY DID FOR TWELVE REVISIONS — corrected r2440, and the prose below was FALSE

*This section said the fast tier runs the text gates and the lint **on every push**.* ***It did not.***
*From r2427 to r2439 the job's first command — `classify_documents.py --check` — exited 1 (twenty-eight restored
files, unclassified), and the step ran under **`set -e`**, which aborts on the first non-zero exit.*
⇒ ***So the fifteen text gates and the hollow-assertion lint never executed in CI at all*** *— while this line
reported "twenty gates rc=0" from running them **one at a time** in its own container, where every exit code is
seen separately.*

**⌗ THE RULE, and it is the one to carry:** ***a suite run by hand and a suite run under `set -e` are DIFFERENT
INSTRUMENTS — the first reports every failure, the second reports the first and hides the rest.***
⌗ *Found by **node 53** on a pristine clone, which is the only place it was visible. **The working tree could not
see it, because the working tree never runs the suite the way CI does.***

**✔ FIXED:** *the fast tier now **runs every check, collects failures, and fails at the end naming all of them**.*
⌗ *It earned itself on the first run by surfacing **two gates the old form was hiding**.*
⚠ **AND ONE GATE IS LEFT RED ON PURPOSE:** *`check_grains` measures lag **by git commits**, so writing "here is
what I do not cover" into a stale document turns it green **whether or not the declaration is true**.* ⇒ ***That
is `check_arcs`' own r2378 trap, and `check_grains` cannot defend against it.*** **So `THE_PLAN` and
`THE_OPEN_PROBLEMS_LEDGER` stay red until they are genuinely propagated:** ***a red gate that names real work is
worth more than a green one that hides it*** *(`L-227`).*

**⌗ AND ONE INSTRUMENT IS DELIBERATELY NOT IN THE GATE LIST.** *`corpus/check_loci.py` — contributed by node 52,
adopted r2440 — is a **triage lint a human reads**, not a gate. Its contributor measured its own precision before
shipping (**assertion-shape 3/3, against word-presence at 42%**) and stated the binding constraint:* ***"a false
alarm in the register costs more than the error, because the next reader inherits a debt that does not exist."***
*(`L-228`.)*

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
