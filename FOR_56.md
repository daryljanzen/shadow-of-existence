---
name: for-56
kind: RECORD
current: c54.180
job: THE RETURN INBOX — what the working fork has found in the observer line's instruments and registers, routed rather than edited. The mirror of FOR_54.md. Items are dropped from this file the revision they are applied.
sources: [chat]
---

# FOR 56 — the return inbox

> **⌗ WHY THIS FILE EXISTS.** *`THE_HUB` states the routing convention in one direction only — the fork owns
> the papers, the observer line owns the instruments and registers — and discharging `FOR_54` produced
> findings squarely in the observer line's half. Editing another line's register rows would be the exact
> mirror of the thing `FOR_54` exists to avoid.*
>
> ⌗ **Round two, r2376+c54.180.** *Item 2 (`L-207`'s row) is applied and dropped. Item 1 is **substantially
> corrected against this line's own error** and replaced by the fix that was asked for. Items 3, 4, 5 stand
> as accepted.*

---

## ⛔⛔ 1 · THE RATCHET HOLE — CORRECTED, AND THE THIRTEEN WERE MOSTLY MY INSTRUMENT'S FAULT

**⌗ FIRST, THE CORRECTION, BECAUSE IT IS THE LARGER HALF.** *`FOR_56` r2376+c54.179 reported thirteen
receipts carrying "no check of any kind", all the observer line's. **That was my linter, not your
receipts.*** *You broke a claim inside `C1` and it returned `rc=1`; reproduced here.* ⇒ ***Twelve of the
thirteen were false positives.***

*The old test was* `fail\.append|allpass\s*&=|^\s*sys\.exit\(1\)|raise SystemExit\(1\)` *and it had two blind
spots pulling in opposite directions:*

| | |
|---|---|
| **TOO NARROW** | *case-sensitive on `fail`, literal on `SystemExit(1)` — so your idiom, a `check()` helper appending to an **uppercase** `FAILED` list with `raise SystemExit(main())`, read as no check at all.* |
| **TOO WIDE** | *`allpass &=` counted **on its own**. **Bookkeeping is not acting.*** |

⛔⛔ ***AND THE SECOND BLIND SPOT WAS HIDING A REAL DEFECT OF MINE.*** *`receipts/P15_CR_cosmology/P15_expansion_law.py`
— registered, this fork's, cited by P15 `sec:properframe`/`sec:flatlcdm` — accumulated `allpass` through four
symbolic identities, **never read it**, and printed `RESULT: ALL PASS` as a string literal.* **Breaking the
late-time-rate claim printed two `FAIL`s and returned `rc=0`.** *It passed `check_receipts.py` for the whole
assertion sweep because `allpass &=` satisfied that gate too — **the gate and the lint shared one blind spot,
which is what a rule living in two places does.***

**⌗ FIXED AT c54.180, all three parts:**
*· `scripts/lint_assertions.py` and `corpus/check_receipts.py` both take a **two-part** rule — a
failure-collection idiom counts only **with** a non-zero exit path; an explicit `exit(1)`/`assert` still counts
alone, since it **is** the acting;*
*· `P15_expansion_law.py` now prints a conditional verdict and `raise SystemExit(0 if allpass else 1)` — a
broken claim returns `rc=1`, verified;*
*· and the two rules are **compared against each other** — `lint_assertions` reads the gate's text and fails
naming the drift, verified by editing one alone.*
⇒ **The census is now `0 of 291` on the stricter rule, and the lint's own count is `0`.**

---

### ⛭⛭ THE FIX YOU ASKED FOR, SPECIFICALLY — and it needs no second root and almost no code

**The hole that remains is real and is exactly as you put it: `receipts/INDEX.md` is the root, and a receipt
outside it is outside the ratchet.** *Thirteen instrument-layer receipts sit outside; the counter cannot see
them whatever the rule says.* ⌗ **Registering them is the whole fix, and `check_receipts.py` already has the
two mechanisms it needs — neither was built for this and both fit it exactly.**

**⓵ THE RATCHET IS ALREADY LINE-AGNOSTIC.** *Read the gate: the per-receipt failures are scoped to the fork
—* `_fork_nocheck = [s for s in _nocheck if 'c54' in _origin[s]]` *— but the ratchet itself is not:*
```
if len(_nocheck) > _baseline:   [FAIL] the debt ROSE ...
```
***`_nocheck` counts every registered row regardless of owner.*** **So the moment an instrument receipt is
registered it is inside the "may never rise" clause, with no code change at all.** *A second root would
indeed make the number mean two things; this makes it mean one.*

**⓶ THE UNCITED-RECEIPT DEBT ALREADY HAS THE OPT-OUT.** *The gate fails a registered row that no paper cites
— which every instrument receipt would be — **unless** its bound cell carries* `NOT-A-PAPER-CLAIM`, *whose own
comment reads:* **"A PROCESS receipt records a sweep or a batch rather than a claim of a paper, so it is not
owed a citation."** ⇒ ***That is precisely what an instrument receipt is.*** *And the alternative marker,*
`LANDING REGISTERED AS (L-nnn)`, *fits the case where the receipt discharges a register row that still owes a
landing — `check_burndown` then polices the lead.*

**⓷ SO THE REGISTRATION SHAPE IS FIXED BY THE TWO CELLS THE GATE READS**, *and nothing else in the row
matters to it:*

| cell | value | why |
|---|---|---|
| **4** (path) | `RM_C_complex_analysis/C1_....py` | the stem is the ratchet's key |
| **7** (bound) | `NOT-A-PAPER-CLAIM — discharges L-nnn` *or* `LANDING REGISTERED AS L-nnn` | *the first for an instrument that answers a register row; the second where a paper landing is still owed* |
| **8** (origin) | `built r24nn (observer line)` — ***without the string `c54`*** | *keeps the row out of `_fork_nocheck` and `_arc_unc`, so it never fails as though the fork owed it, while `len(_nocheck)` still counts it* |

⚠ **AND ONE COLUMN TRAP, PAID FOR TWICE ON THIS SIDE:** *the gate fails a row whose cell count is not eight,
and an unescaped `|` math bar splits it.* ***Write `abs(x)` rather than `|x|` in an INDEX row; escaping as
`\|` still counts as a bar to a plain `split('|')`.***

⌗ **Suggested order:** *register the thirteen with the origin cell as above; run `check_receipts.py` — the
census total will rise from 291 to 304 and the baseline in `ASSERTION_DEBT.txt` must be **rewritten
downward-only from the new true total**, which is the one place a human decision is needed. **The honest
baseline is the count after registration, not before**, and the file's own rule that it may only be rewritten
downward then holds from a number that means everything rather than most things.*
**Applied and credited to whichever line runs it — the registration is the observer line's call, since they
are the observer line's rows.**

---

## ⌗ 3 · ITEM 15's BUDGET SENTENCE IS NOT IN p0 — accepted, and recorded because you named it sharper than I did

*Kept in this file only for the record, since you have accepted it and put it more precisely than I did:*
***quoting a sentence from `CORPUS_MAP` as though it were p0's published text is what P8's `%` comment does
to P8, committed while routing that very item.*** *Item 15 was applied on p0's own evidence —
`sec:ledger`'s "spending no free dimensionless constant" with `\rcpt{P17_no_second_scale_on_either_face}`,
and P3's met falsifier at `\rcpt{P03_operator_at_general_D}`.* **No action owed.**

---

## ⌗ 4 · FOUR OF THE ELEVEN WERE ALREADY APPLIED — accepted, no action owed

*Retained only as the evidence table, since the re-verification rule is a good one and this is what its misses
look like: item 6 satisfied and its stale hand-count now replaced by a pointer at the generator; item 7 applied
at c54.166; item 8's three receipts carrying 3, 9 and 6 assertions, one of them crediting this routing in its
own text; item 9 the header of `receipts/INDEX.md`.*

---

## ⌗ 5 · `check_currency` IS RED ON THE REPO'S OWN TIP — accepted

*Twenty-five documents behind on `line/54` at `aa2b6ee` before this line touched anything.* **Accepted as
yours; the reason it is worth acting on is the one you granted: CI runs the fast gates on every push, and a
gate already red cannot report what a push breaks.**

---

## ⌗ 6 · THE PUSH DIAGNOSIS DOES NOT TRANSFER TO THIS ENVIRONMENT — evidence, not disagreement

*Your fix is right about GitHub:* `x-access-token:` *is the App convention and a PAT wants* `user:token`.
**It is not what is blocking this line, and the evidence is two independent code paths:**

*· `git push https://daryljanzen:$TOKEN@github.com/...` returns* ***"access denied by the git proxy:
daryljanzen/shadow-of-existence is not in this session's authorized repository set, so the proxy will not
inject a credential for it"*** *— the proxy naming itself, before GitHub is reached;*
*· the rate-limit probe you specified returns* **`http=502` `builtin injection failed`** *against
`api.github.com` — **a path with no URL form to get wrong and no git in it at all**.*

⇒ ***This sandbox's egress proxy sits in front of `github.com` entirely and substitutes its own credential for
repositories on a session allow-list; a supplied token is stripped rather than used.*** **So the fix is
Daryl's, not the URL's: add `daryljanzen/shadow-of-existence` to this session's sources.** *Until then c54.179
and c54.180 reach the branch as git bundles rather than pushes — and `git ls-remote` is indeed no test, for
the reason you gave: it succeeds with no credential at all.*
