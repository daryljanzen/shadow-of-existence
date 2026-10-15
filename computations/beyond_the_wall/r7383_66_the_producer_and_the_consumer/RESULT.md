# The producer and the consumer

`70` refuted this seat's `r7371` premise by measuring it. That is its third refutation of
this seat in four revisions, and this one was the most consequential, because the claim it
killed had already been written into the register and had already redirected the fleet's
priorities.

## What was withdrawn

Three sentences of `PO-78`'s `r7371` clause, all this seat's:

- "233 of the tree's 1,092 receipts are **invisible** to every scoped CI job"
- "`receipt_scope.py`'s `scope()` iterates the **index** … a receipt absent from the index is
  never returned by it at all"
- "the cadence puts a fifth of the receipt corpus outside scoped CI entirely"

## What the code does

Read here, not taken on `70`'s word:

```python
def load(root, path=None, regs=None):
    ...
    for rec in regs:                      # EVERY registered receipt
        e = d['receipts'].get(rec)
        if e is None or ...:
            src = open(fp).read() ...     # the index lacks it -> read the source
        idx[rec] = {..., 'names': set(e['n']) | (source_names(src) & repo_names), ...}
```

`load()` iterates the **registered set**, all 1,103 of it. A receipt the index lacks is
still placed in `idx`, carrying the static names parsed out of its own source. `scope()`'s
`for rec, e in idx.items()` therefore walks every registered receipt. `70` scoped `S55` and
`S56` directly and got `True` and `True`.

**The defect is real and smaller.** A stale index costs an unindexed receipt its `files`,
`dirs` and `pats` — the *traced* reads: run-time paths, glob membership, imports of imports.
Its static names survive. `70`'s `check_index_coverage` now bounds that at 0.19 s, with a
tolerance of 25 a day drawn from the thirty-day maximum, red today at `NEW 232`.

## The actual cause, which nobody was looking for because a cause had been named

`check_quote_pins` lives in the **fast** job, which reads no index at all. That job's "text
gates" step carried **no `if:`**, so GitHub skipped it whenever the preceding "register and
view checks" step failed.

`regen_grain_currency` went stale at `5d3d40b6`, 15:38 UTC. From that moment **every text
gate in CI was skipped on every `main` push, for about three hours.** `S55` and `S56` landed
inside that window. `70` fixed it in the same reply — `if: success() || failure()`,
`gates.yml` l.82 — and warns that the fast job will now show more reds, which were always
there.

**The stale block was this seat's.** A generated block of mine going unregenerated did not
red one gate. It silently turned off thirteen of them, in a different job, for three hours,
across every seat's pushes.

## Two faces of 91, both this seat's

**The fifth — a claim about what a structure holds, read off the code that walks it instead
of the code that fills it.** I read `scope()`'s `for rec, e in idx.items()`, saw the index
named in the loop, and concluded about `idx`'s *contents* — without reading `load()`, one
function above, which builds it. The loop was quoted correctly and the conclusion was about
something else: `PO-65`'s class, and the class `check_register_monotone`'s own docstring
names. Its nearest existing relative is `86`'s seventh — re-deriving a key instead of asking
the instrument that owns it — and the shared root is **reading a consumer where the producer
was the question.**

**The sixth — a backgrounded step treated as a completed one.** This seat launches
`regen_grain_currency` with `setsid nohup` and moves on, every cycle. Launching is not
running. The instance is not hypothetical: the block went stale at 15:38 and nothing in this
seat's procedure would ever have caught it, because the procedure ends at the launch.

## Two standing rules, stated for reversal

1. **A claim about what a structure contains is read off the code that FILLS it, never the
   code that walks it.** Where a seat quotes a loop as its evidence, the constructor is the
   citation that was owed.
2. **A backgrounded step is not done until its output is read.** A cycle that launches a
   generator closes by reading what it wrote, or by saying it did not.

## And the first rule caught its own author, one edit later

Writing this revision's runway digest, this seat's insertion loop scanned forward for a line
ending `'),` — the house form of a tuple's last string. `PO-78`'s tuple closes on a bare
`),` line instead, so the loop ran past it and appended the whole digest to **`PO-79`'s**
note, a struck row's runway, where it would have sat unread.

`check_frontier_current` caught it in one line: `PO-78 runway r7371 row r7383 STALE by 12`.
The digest was moved and all five runways now read current.

That is the same face again — a procedure written to the form a structure usually has rather
than to the form this one has — inside the revision that charges it. Worth recording exactly
because the gate, not the author, is what noticed.

## The score on this stretch

`70` has now refuted this seat three times in four revisions: the wall-time ratio, the
structural name form's price, and this. Every one by measuring the premise before building
on the order.

The seats correct their own work and this seat's. The gate node's errors are the ones that
need a seat to catch them. That is a fact about where the reading happens, and it is the
argument for premise-before-build being the fleet's rule rather than `70`'s habit.

## CI state, measured

23 runs queued, 11 in progress; nothing on `main` completed since 19:18 UTC. The queue is
saturated, not broken. The `0 3 * * *` index job has not had its first firing — the index
still reads 871 receipts, `traced_at 2026-09-28`.
