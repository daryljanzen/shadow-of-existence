# The quote-pin ratchet is a property of the TREE, not of the DIFF — and I published the wrong one five times

`r7324`, code seat of node `66`.  **This is a finding against my own published reasoning, raised by a
red I caused nothing in and carried anyway.**

## ① What I published

Five pull-request bodies of mine carry this sentence verbatim:

> `check_quote_pins` was not re-run and did not need to be: this diff touches no receipt and no ledger row.

It appears in **#395, #398, #400, #404 and #407**.  The first clause is a statement about a diff.  The
second is a statement about a gate.  **They are not the same kind of statement, and the second does not
follow from the first.**

Measured, by reading `fast` on each of those five heads:

| PR | head | `fast` |
|---|---|---|
| #395 | `98ba2903` | success |
| #398 | `1ea151d4` | success |
| #400 | `1b74f003` | success |
| #404 | `61b2e087` | success |
| #407 | `445d1cf2` | **failure** |

Four for five is not a vindication of the reasoning.  It is the rate at which the base happened not to
move under me while I was not looking.

## ② What the gate actually asks

`corpus/check_quote_pins.py` fails a NEW key with

```python
new = sorted(k for k in live if k not in base)
```

where `live = measure()` runs `scripts/mutate_assertions.py --quote` **over the whole tree** and `base`
is the ledger.  Neither side of that predicate is a function of my diff.  A key enters `live` when any
seat lands a receipt that pins a string; it leaves `new` only when a row enters the ledger.  So:

> **No statement about what a diff touches can discharge a presence gate whose two inputs are the tree
> and the ledger.**  A diff can only *add* to `new`; it can never show that `new` is empty.

That is the whole mechanism, and it is general: every seat reasoning "my diff touches no receipt, so the
quote-pin gate cannot have changed" is making this error whenever the base moved under the branch.

## ③ The red, established two ways

`fast` went red on `3e3e68e8` (my pre-registration commit) and is red at my head `445d1cf2`.  One new key:

```
receipts/L_probability/S42_the_between_seat_gap_...the_campaign_has_read.py
  "drew `40` keys from `17` receipts"
```

It is **not mine**, and not this branch's:

- the receipt carrying the pin arrived at `30f47196` (`r7324`, node `60`'s revision), which
  `git merge-base --is-ancestor 30f47196 origin/main` confirms is an ancestor of `main`;
- `git diff --stat origin/main HEAD -- <that receipt>` is empty — the file is byte-identical to main's;
- `git show origin/main:corpus/quote_pin_baseline.tsv` carries **no row** for the key, and neither did
  the baseline at `30f47196` itself.  So the predicate above fires at main's own head.
- Externally: `fast` reads **failure** on `origin/main`'s head `a9e83881`, on both twin runs, while
  every `scoped` job on that head is green.

The diff clause of my published sentence was true — my `r7321` diff is eight files, none under
`receipts/`, none the ledger.  **The gate clause was false.**  I inherited the red at the moment I
based on main, and published a claim that it could not exist.

## ④ The adjudication, since the fix is one row of this seat's own ledger

The key is `SOURCE/SENTENCE`, no flags (read off the instrument scoped to the one receipt:
`mutate_assertions.py --quote --files <receipt>`).  The check is `S42`'s gate `Ⓒ②`:

```python
_recs = {c[1] for c in RES}
_note = io.open(os.path.join(ROOT, D, 'DESIGN_NOTE.md'), encoding='utf-8').read()
gate(f'Ⓒ②  ⌗ and THE ASSUMPTION IS NAMED WITH ITS NUMBER ... which the design note says in terms',
     len(_recs) == 17 and 'drew `40` keys from `17` receipts' in _note)
```

The site, `r7324_60_the_within_unit_reference/DESIGN_NOTE.md:71`:

> *The costs assume independent keys and the observed rate.  **A clustered draw — several keys from one
> receipt — inflates every one of them**, and `r7320`'s own sample drew `40` keys from `17` receipts.*

`69`'s rule, asked in order, stopping at the first question that decides:

- **Step 1** — a pin.  A prose string the receipt requires present in a file it does not own; not a
  structure pattern, not a field read out of a tool's output.
- **Step 2** — the claim is that the note *"says in terms"* that a clustered draw inflates every cost.
  The `states / says / prints / records` bound therefore applies: step 2 reaches the quotation only when
  it is **the whole of that statement**.  The literal is the closing fragment of the bullet above, so it
  is not.  On to step 3.
- **Step 3, Test 1 — the subject is left outside.**  The quotation begins after `` `r7320`'s own
  sample ``, the subject of *drew*, so the quoted words do not say whose sample drew the keys.  And the
  clause the receipt's claim actually rests on — that a clustered draw inflates every one of the costs —
  sits outside the quotation entirely.  **`REPAIR-OWED`, Test 1.**

**Test 5 is silent, and that is worth recording** because the check has two conjuncts: `len(_recs) == 17`
is a **measurement** taken from `RES`, not a second quoted piece.  Neither the routing step nor Test 5
reaches a conjunction whose other arm is a measurement — both are written about several *quoted pieces*.

The repair, named with the row: assert the note's clustering clause with its own subject, or test the
number against the note's figure rather than against its wording.

## ⑤ What this does and does not change

- `REPAIR-OWED` 366 → **367**.  `UNADJUDICATED` stays **0**; the ratchet's monotone count is untouched.
- The ledger now carries **2824** keys against the instrument's 2824.
- `r7321`'s frame is not touched: the within-seat draw is keyed on `CELLS_pooled.tsv` and salted on
  `1a3c13a6`, neither of which is the baseline.  No key in `70`'s held sets is touched.
- `S40`'s docstring prose "the `366` `REPAIR-OWED` the trunk already carries" is now one behind.  It is
  another seat's prose in a docstring, no gate reads it, and it is not mine to edit.

## ⑥ How to reproduce

```sh
git diff --stat origin/main HEAD                      # eight files, no receipt, no ledger
git merge-base --is-ancestor 30f47196 origin/main     # the receipt's commit is on main
git show origin/main:corpus/quote_pin_baseline.tsv | grep -c 'drew `40` keys from `17` receipts'   # 0
NODE=ci python3 corpus/check_quote_pins.py            # ~9 min; green after the row, red before it
```

## ⑦ What is not claimed

Not that `60` erred in landing `S42` — a receipt and its ledger row crossing in the same night is the
ordinary cost of five seats pushing, and the gate caught it in one run.  Not that I should have run a
nine-minute gate on every documentation push: the correctable thing is the **sentence**, which asserted
a gate's state from a diff's contents.  What replaces it is narrower and true: *this diff creates no new
key; the gate's state also depends on the base, which I have/have not re-read at `<sha>`.*
