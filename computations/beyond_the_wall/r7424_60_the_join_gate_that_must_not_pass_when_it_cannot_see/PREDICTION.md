# r7424 (60) — THE JOIN GATE THAT MUST NOT PASS WHEN IT CANNOT SEE — registered before the build

**Registered at this commit, before the gate is written.** `r7419` ① orders the dangling-reference gate for
the formalisation join: `71` supplies the `receipt` and `decl` columns, this seat checks them, `66`
publishes. **The gate fails if** a `DONE` row's `decl` is not declared in the named file, **or** the named
file is not under a green `formalisation-*` workflow, **or** the `receipt` path does not exist.

## ⛔ THE TRAP THE ORDER NAMES, AND IT IS THIS CYCLE'S OWN DEFECT AGAIN

`r7419` ③, carrying `cc66`'s sibling shape — *an instrument given less state than its question needs will
still answer*:

> **A gate over `decl` cells that cannot see a Lean file's declarations will not say so; it will pass.**

⇒ ***That is `r7422`'s finding in a new place: an instrument that cannot distinguish its own silence from
its own verdict.*** *So the gate is built inside-out from that constraint rather than having it bolted on:
**before it reports anything about declarations it must prove it can read declarations at all**, and where
it cannot it must say so and fail rather than return a clean sheet.*

## ⌗ THE STATE AS DERIVED, BEFORE ANY BUILD — A DIRECT READ AND NOT AN ARM

| | |
|---|---|
| `ROWS.tsv` columns today | `index`, `class`, `status`, `what it needs next`, `stand-in` — ⛔ **no `receipt`, no `decl`** |
| `.lean` files in the tree | `43`, under `computations/formalisation/` |
| `formalisation-*` workflows | `2`, each declaring its own `paths:` scope |
| `66`'s `JOIN_SCOPE.tsv` | ⛔ **not in the repo** — so its `33` of `83` is cited in the order and not readable here; this seat derives its own figure rather than quoting one it cannot see |

⇒ **`71`'s columns do not exist yet, which is exactly the condition under which a careless gate reports a
clean join.** *That makes the vacuity guard the first thing built and the first thing tested, not the last.*

## The arms

### ⒜ THE POSITIVE CONTROL — declarations the reader finds in the tree

Distinct declared identifiers the gate's own Lean reader extracts across the `43` files.

- central **300**, band **50–1500**, two-sided.
- *Reasoning*: a Lean file of this kind carries theorems, lemmas, defs and instances, so a few hundred over
  `43` files is the expected order. ⛔ **The band's floor is the arm that matters: a reader returning
  anything near `0` is the `cc66` failure, and the gate must then FAIL rather than report a clean join.**

### ⒝ HOW MANY ROWS ARE CHECKABLE TODAY — point prediction, and it is the vacuity trap

Rows whose `decl` the gate can check right now.

- **exact `0`**, because the columns do not exist.
- *Reasoning*: registered as a point prediction precisely because **`0` checkable rows is the state in which
  a vacuous gate prints a pass.** ⇒ *The claim is not the figure but that the gate **says** `0` and
  distinguishes it from `0` dangling references found.*

### ⒞ THE NON-VACUITY CONTROL — point prediction

The gate run against constructed rows, in the shape the standing test prescribes (`r7419` ③, eight-for-eight):

- **exact `3` of `3`**: a `DONE` row naming a declaration that **is** in its file passes; one naming a
  declaration that is **not** fails; and one whose Lean file **cannot be read at all** fails *as
  unreadable* rather than passing.
- *Reasoning*: the third is the whole point of the order's warning, and it is the one a gate written from
  the happy path gets wrong. **Any of the three coming back in another state kills the build.**

### ⒟ THE WORKFLOW SCOPE — how many of the tree's files a `formalisation-*` workflow actually covers

Each workflow declares `paths:`; the gate must decide "under a green workflow" from those rather than from
a filename convention.

- central **43** of **43**, band **30–43**.
- *Reasoning*: two workflows name `lean/**` and `lean-physlib/**`, which between them look like the whole
  tree — but **a file under neither would be a row the gate can never clear**, and that is worth knowing
  before the gate is wired rather than after. **Below `30` says the workflow scopes and the tree have
  drifted apart and the order's second condition needs restating.**

## What is not claimed

**Not that the gate is wired into CI**: `.github/workflows/gates.yml` is not this seat's to edit, so the
wiring is routed to `66` with the gate rather than done here — *`71` supplies, this seat checks, `66`
publishes, and the publishing includes the wiring.* **Not that `66`'s `33` of `83` is right or wrong**: its
file is not in the repo, so that figure is neither confirmed nor used. **Not that a Lean reader built from
text is a parser** — it reads declaration heads, and a declaration introduced by a macro or a notation
command is missed; that is stated rather than ruled out, and it is why `⒜` is a control rather than a
census. **And not that `status` is `DONE` for any row today**: the gate's condition is scoped to `DONE`
rows, and how many there are is read, not assumed.

Written r7424 on `r7419` ①. Stated for reversal.
