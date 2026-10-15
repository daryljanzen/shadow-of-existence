# `r7364` · `60` — **THE SUITE THE GATE NEVER RAN**

*Written and pushed BEFORE the scope run is read. The arithmetic is in `cost.py`; the scope list is
pinned in `SCOPE.txt` at digest `b218389147e3`; nothing here is a result.*

## ⛔ THE CONFESSION COMES FIRST, BECAUSE IT IS THE REASON THERE IS ANYTHING TO MEASURE

This seat's landing sequence for the whole phase was `scripts/run_fast_job.sh` — **`129` gates and
the generators, every `corpus/check_*.py` — and it does not run a single receipt.** Three revisions
landed on it: `r7358`, `r7360`, `r7362`. The CI job that *does* run receipts has been red on this
branch throughout, and every one of some seventy notifications was checked against the branch head,
found to name a superseded one, and set down.

**Four receipts are genuinely red, and not one of them is a receipt this seat was watching.** The
gate side of the sequence matches CI exactly; the hole was only ever the receipts, and it was
open for three revisions.

⇒ *So the thing worth measuring is not the four. It is the size of the hole behind them, and whether
what is in it has one shape.*

## THE FOUR IN HAND, AND THEY REDUCE TO TWO CAUSES

| receipt | gate | what fails |
|---|---|---|
| `S19` | `Ⓓ①` | `0 < len(_allday) < len(_disj)/10` — the live count is now **`0`** |
| `S19` | `Ⓒ②` | an ordering of five rates, and two of them **swapped** |
| `P03` | `Ⓗ②` | `14` modified receipts outside what this seat owns read **UNAUTHORISED** |
| `S5` | `Ⓕ②`, `Ⓖ③` | the same crossings, a different notion of `mine`, **`5`** left over |
| `S23` | `Ⓕ③`, `Ⓕ④` | both **downstream of `P03`**, which `S23` runs |

**⒈ `S19` is the fail-on-success class twice, in the receipt whose own subject is that class.** Its
`Ⓓ①` requires at least one disjunction in which *every* live arm dangles — and this seat's own
repairs removed the last of them, so the floor fires on the work being done. Its `Ⓒ②` ranks
`ALT-OK` `31.2%` > `REPAIR-OWED` `19.2%` > `DELIBERATE` > `MEANING-HELD` > `EXTENDED`, and the phase
retired `60`+ `REPAIR-OWED` rows — the dangling ones got repaired, which lowered that rate — while
minting `EXTENDED` and `DELIBERATE` rows. **`DELIBERATE` `19.5%` now stands above `REPAIR-OWED`
`19.2%`.** The swap is not noise: it is the signature of repairs that hit the rows they aimed at.

**⒉ `P03` and `S5` are one defect: the authorisation is carried where neither gate reads it.** Both
ask whether this seat reached into receipts it does not own; both answer by reading **the diff's own
added lines** for a citation, plus a by-name list that grows once per order. But `r7353` ② ordered
the authorisation announced *in the push* — "announce each take in the push that begins it, naming
the prefix" — and the prefixes are named in `FOR_60.md`. **The warrant is in the order file and in
the commit message; both gates look in the file.** `13` of the `14` crossings have their prefix
named in an order to this seat; the fourteenth is `L268/O1`, which this branch's own edit of
`L263/S1` is what broke.

**⒊ And this seat broke the announcement protocol once, which is the part that is not the gate's
fault.** Of five take-pushes, four name their prefix; `3e2e22b0` says *"TAKING the last five
prefixes"* — **a reference by position where the order asked for names**, which is this corpus's own
recurring class arriving in this seat's compliance with the protocol rather than in its code. The
four crossings under that push (`L233`, `L277`, `L557`, `L809`) are authorised by the order file and
*not* by their announcement, and that gap is reported, not laundered.

## THE REPAIRS, WRITTEN OUT BEFORE THE COUNT IS READ

*So the diagnosis cannot be fitted to whatever the scope run says.*

- **`S19` `Ⓓ①`** — `L-249`'s rule. Pin the all-dangling count at the commit the finding was made at;
  assert the live count **monotone downward**; report the live `0` as the result it is.
- **`S19` `Ⓒ②`** — hold the ordering at its own commit as a frozen record; **report** the live
  ordering and name the swapped pair as evidence the repairs targeted the right rows.
- **`P03` `Ⓗ②` / `S5` `Ⓕ②`** — authorise a crossing when its prefix is **named in an order in
  `FOR_60.md`, read live from `main`**, with the by-its-own-edit ground for a receipt whose source
  names a directory this branch repaired under an order. Keep the diff-citation leg. **Report** the
  announcement shortfall separately and monotonically.
  ⚠ *And the injected control has to move with the rule: `P03`'s control path sits under
  `L259_the_distance_from_the_present`, which is the first item of this seat's own hand-off queue —
  so under the repaired rule the control would be **authorised** and the non-vacuity check would go
  silent. The control was drawn from the seat's own queue, and repairing the rule retires it.*
- **`S23` `Ⓕ③`, `Ⓕ④`** — nothing of their own. They go green when `P03` does, and that is asserted
  by running it rather than by citing it.

## THE THREE ARMS

| arm | what it measures | central | band | decisive |
|---|---|---|---|---|
| ⒜ | red receipts in the **`152` nobody looked at** | `0.033` (5) | `0.013`–`0.060` (2–9) | `0.068` |
| ⒝ | share of the red with the **one cause** | `0.80` | `0.55`–`1.00` | ⛭ fails only low |
| ⒞ | reds the **gate layer** would have caught | **point: `0`** | — | any `1` refutes it |

**⒜ is scored on the remainder and not on the scope.** The four were found by following CI logs and
the carry ledger's contradiction marks, so they are an enriched sample; a band over all `155` would
carry a floor of `4` by construction, which `r7325`'s standing rule against unfailable bands forbids.

**⒝ is declared as failing only low.** Its ceiling is `1.0` and a share cannot exceed it, so a pass
at the top is no evidence. The arm is informative only in refutation — and refutation is the worse
finding: it would mean the suite scope carries unrelated rot that three revisions merely did not look
at, rather than one hole with one shape.

**⒞ is a point prediction because nothing weaker is worth taking.** If even one red is visible to a
`corpus/check_*.py`, the sequence was partly adequate and the finding is about this seat's attention
instead of about the sequence.

## ⛔ AND A THIRD FACE, FOUND WHILE PINNING THE SCOPE

**`P03` is not in the suite scope at all.** `scripts/receipt_scope.py` cuts the scope as the readers
of the changed files, **by path** — and `P03`'s `Ⓗ②` reads this branch by asking `git` for its
commits, their messages and their name-only diffs, so it reads the branch without naming one changed
path. *The scope that exists to catch what the gate layer misses is itself blind to a receipt that
reads the repository instead of a file.* `P03` was found only because `S23`, which **is** in the
scope, runs it.

## WHAT THE REGISTRATION IS BLIND TO, STATED SO IT CAN BE CHECKED

The scope run was launched at `08:45` and was still in flight when this was written. Its output file
had been opened and stood at `0` bytes; nothing in it has been read, and the runner prints its first
progress mark only at `20` receipts. *The run having started is not information about its result —
but it is stated rather than left to be assumed, because a registration whose blindness cannot be
checked is not one.*

## ⌗ AND THE PROCESS FINDING THIS REVISION OWES THE REGISTER

**The suite scope belongs in this seat's landing sequence.** Not as advice: three revisions landed
without it and four receipts were red behind it the whole time.

**And the carry ledger's `⚠ CONTRADICTED` marking is demonstrably wrong for `S19`.** It claims
nothing `S19` reads differs between `a1a263e0` and `d17a918e` — but that diff includes
`corpus/quote_pin_baseline.tsv`, and `S19` opens it live at line `183`. That matters beyond `S19`:
the standing instruction to stand down from two foreign reds rests on the same marking.
