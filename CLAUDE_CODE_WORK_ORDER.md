---
name: claude-code-work-order
kind: RECORD
current: r2472
job: THE UNATTENDED WORK ORDER — mechanical, verifiable work a Claude Code session can run for hours without a human, with hard prohibitions on the judgement half. Read with THE_HUB and NEXT.md.
sources: [chat]
---

# CLAUDE CODE — the unattended work order at r2472

> ## ⛔⛔ READ THIS BLOCK FIRST. IT IS THE WHOLE SAFETY OF RUNNING UNATTENDED.
>
> ***YOU ARE DOING THE MECHANICAL HALF. THE JUDGEMENT HALF IS NOT YOURS AND MUST NOT BE ATTEMPTED.***
>
> **The corpus's own architecture is why:** *`L-237` established that **every gate checks something somebody
> DECLARED**, and both lints — which INFER — are deliberately outside the gate list.* ⇒ ***You are a gate,
> not a lint. Work on what is declared. Report what would need inferring.***

## ⛔ HARD PROHIBITIONS — no exceptions, no judgement calls

| never | why |
|---|---|
| **Strike a register row** in `THE_LIVE_ARC.md` | *striking requires a propagation judgement; the bar is in `PROTECTED_OPEN`* |
| **Close or kill anything in `PROTECTED_OPEN.md`** | ***"a closure on a protected item is Daryl's"*** — *and note it also says a node MAY work and MAY narrow one; you simply are not the node that does* |
| **Edit `corpus/*.tex`** | *the papers are the working fork's layer; route to `FOR_54.md` instead* |
| **Write a verdict, disposition, or "⇒" conclusion anywhere** | *report the finding; a chat session or Daryl judges it* |
| **Push with any gate red** | *`check_compile` included — run the full suite before every push* |
| **Delete anything** | *no exceptions* |
| **"Fix" a failing receipt by weakening its check** | ***a check that cannot fail is worse than none*** *— `check_receipts` will catch it and it is the defect the corpus most fears* |

## ⛭ WHAT TO DO WITH ANYTHING YOU CANNOT DO MECHANICALLY

*Append it to **`FINDINGS_FOR_REVIEW.md`** (create if absent) as a dated block naming: **the file, the exact
observation, the command that produced it, and what you did NOT conclude**.* ⇒ ***That file is your only
output channel for judgement. Never put a conclusion in the register, a paper, or a capstone.***

---

# THE TASKS, IN ORDER

## ⓵ RUN EVERY RECEIPT — 331 of them, and nothing has ever run them all in one pass

**Why:** *`check_receipts_run` exists and its own header records that **"two attempts to run it inside a
single tool call died at the execution limit before"**. **You have the time a chat session does not.***

**Do:**
```
python3 scripts/run_all_receipts.py          # or drive them individually if it lacks a resume
```
*For each receipt: record **path, exit code, and the first FAIL line** if any.*

**Success:** *a complete table in `FINDINGS_FOR_REVIEW.md` — every receipt, its rc, and its first failure.*
⚠ ***DO NOT FIX ANY FAILING RECEIPT.*** *A receipt failing may mean the receipt rotted OR **the paper moved
under it** — and which one it is **is a judgement**. Report both possibilities and stop.*
⌗ *Budget: this is the long one. Run it first so it is done even if nothing else is.*

## ⓶ THE UNCITED-RECEIPT DEBT COUNTS 29, AND THE INFORMATION TO FIX IT IS ALREADY DECLARED

**Why:** *`check_receipts` reports **"UNCITED-RECEIPT DEBT: 0 from the current fork, 29 older"**, and most
of those 29 are observer-line receipts whose `receipts/INDEX.md` row **already declares
`NOT-A-PAPER-CLAIM`** in its disposition column.* ⇒ ***The gate conflates "should be cited and is not" with
"deliberately not a paper claim", and the distinction is already written down.***

**Do:** *teach the counter to read the declared disposition — a receipt whose INDEX row says
`NOT-A-PAPER-CLAIM` is **not** debt.* ⌗ ***Verify against a seeded defect** — flip one row's disposition and
confirm the count changes — **not against a clean tree**. That rule is `THE_PLAN`'s and it has earned itself
twice.*

**⛭ THE TARGET NUMBER, MEASURED AT r2472 SO YOU CAN CHECK YOUR OWN WORK:**

| | |
|---|---|
| receipts registered in `receipts/INDEX.md` | **334** |
| cited by `\rcpt{}` in the papers | **288** |
| uncited | **46** |
| of those, declaring `NOT-A-PAPER-CLAIM` | **38** |
| ⇒ ***genuinely uncited paper receipts*** | ***8*** |

⚠ *And **one of the 8 is `L8_*`, a GLOB rather than a receipt name** — so the real debt is about **7**, and
**that stray glob in an INDEX row is itself worth reporting**.*

**Success:** *`check_receipts` still rc=0, the reported debt lands near **7–8** rather than 29, and **the
seeded-defect verification is shown in the commit message**.*
⌗ ***If your count does not match the table above, do NOT adjust the table — report the discrepancy. The table
is a measurement, and a measurement that disagrees with yours is a finding, not a typo.***

## ⓷ THE `ORIGIN` DRIFT BACKLOG — 24 unexplained

**Why:** *a receipt declares `ORIGIN:` and the gate compares code; **24 diverge without an
`ORIGIN-DIVERGENCE:` note explaining why**.*

**Do, per case:** *· if the divergence is **cosmetic** (whitespace, a comment, a print) — **re-sync the
receipt from its origin** and say so; · if it is **substantive** — ***do not touch either file***. Record it
in `FINDINGS_FOR_REVIEW.md` with the diff, because **which file is right is a judgement**.*

**Success:** *the cosmetic ones re-synced with the gate still green; the substantive ones listed, unresolved,
with diffs.*

## ⓸ THE FULL SUITE, EVERY TIME

```
cd corpus && for g in check_*.py; do python3 -W ignore $g; done
cd .. && for s in scripts/regen_*.py scripts/classify_documents.py; do python3 $s --check; done
python3 scripts/lint_assertions.py
```
*Twenty-one gates, eight views, one lint. **All must be green before any push.*** ⌗ *`corpus/check_loci.py`
and `corpus/scope_table.py` are **lints, not gates** — run them for information, never fail on them.*

---

## ⌗ HOW TO COMMIT

*· One commit per task, message naming **what was verified and how**.*
*· Log each landing in `CORPUS_MAP.md` as a revision entry, **stating what you did and what you deliberately
did not conclude**.*
*· Push `main`, then `git branch -f line/54 main && git branch -f line/56 main` and push those too — **both
lines work in this repository** and the branches must not diverge.*

## ⌗ STOP CONDITIONS — stop and write to `FINDINGS_FOR_REVIEW.md` rather than proceeding

*· **any gate goes red and the fix is not obviously mechanical**;*
*· **a receipt fails and the cause could be the paper rather than the receipt**;*
*· **a task turns out to need a judgement about physics, about what a claim means, or about what is
established versus discussed**;*
*· **you find yourself about to write "⇒" or "therefore"** — ***that is the signal, and it is a reliable
one.***

> ⌗⌗ **AND ONE THING WORTH MORE THAN ANY TASK ABOVE:** *if a task's stated premise turns out to be **stale**
> — the count wrong, the file gone, the defect already fixed — ***that IS the result***. *Three register rows
> this session turned out to rest on stale premises, and finding that was worth more than the work they
> asked for.* **Record it and move to the next task.**
