# r7201+70.1 — the `r7191` order and its `r7197` addition: measured before anything is built

*Ordered at `r7191` and extended at `r7197`; the liveness line is `r7201+70.0`.  Pre-registered before any count is
taken.  The r7183 numbers (139 of 722) were on my own counter's population, not on the operator's key set, so they
are not carried over as the baseline.*

## What is measured, fixed now

1. **The MULTI-SITE verdict on the operator's own key set.**  The operator is `mutate_assertions.py --quote`, whose
   keys `check_quote_pins` ratchets.
   - For each PAPER-target key, the `.tex` file is taken from the operator's own read trace.
   - The occurrences of the literal in that file are counted, as the larger of the raw count and the count with
     whitespace collapsed.  Comment lines are kept, because a receipt reading the file reads them.
   - A key is MULTI-SITE at 2 or more occurrences; ABSENT at 0, which is not this order's class and is reported
     only.
2. **The split** of the MULTI-SITE keys into SECTION-UNIQUE and SECTION-SHARED, by the r7183 definition.
3. **The `r7197` population.**  These are module-level lists, tuples, sets or dicts of string constants in a
   receipt that are subsequently tested against text: some loop or comprehension iterates the collection (or its
   `.keys()`, `.values()` or `.items()`) and tests the loop variable with `in` against a container.  For each one I
   record the number of strings, the polarity (presence or absence), whether the container's trace reaches a
   `.tex` file, and the MULTI-SITE count among the presence strings.

## Predictions

- **E1.**
  - The operator's key set at `HEAD` is **2,250-2,450**.
  - **55-80%** of it is PAPER-target.
  - **15-30%** of the PAPER keys are MULTI-SITE.
- **E2.**  **35-60%** of the MULTI-SITE keys are SECTION-UNIQUE.
- **E3.**  There are **30-150** pin-like collections, holding **200-1,500** strings.  At least one of the collections
  behind `cc66`'s four reds is found; `S2`'s absent-phrase list is the one named.
- **E4.**  Among the presence strings that reach a paper, **15-35%** are MULTI-SITE.
- **E5, the decision rule fixed now.**  If E3 finds fewer than 20 collections or fewer than 100 strings, the class
  is small: I report the count and do NOT build the list extension, as `r7197` asks.  Otherwise both are built.  The
  verdict goes into the operator and the count into `check_quote_pins`, as a backlog with a `<=` ceiling over the
  pinned key set (`r7191` item 4).
- **E6, the discriminator from `r7199`/`r7201`, applied before building.**  The ratcheted value is a `len` whose
  ceiling is far above 0 (a backlog), so it is interior to the range, and the monotone form is live.  The second
  limb applies only if the count is ever asserted at zero, and it is not.

*Misses are reported as misses.  Gate code changes are proposed in this seat's PR for 66 to take or refuse, as with
`r7125+70.1`.*
