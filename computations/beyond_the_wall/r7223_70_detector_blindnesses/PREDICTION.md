# r7223+70.1 — the two detector blindnesses `60` routed: diagnosed, repaired, re-measured. Pre-registered before any repair or count

*Ordered at `r7223`.  This file fixes what was seen before writing it, the repairs, the predicted size of each
effect, and what is re-measured.*

## Seen before this file was written (diagnosis, not a measurement of the population)

- **② does not reproduce as described.**  On `r7234`'s receipt
  (`P15_the_spacing_drift_is_made_in_the_projection…`), `--quote`'s list walk **does** find all three
  `_CLAUSES` strings at the `all(c in _tex_pin for c in _CLAUSES)` site.  Generator expressions over
  module-level collections have been handled since `r7201+70.1`.
  - They are dropped one step later, because `_reads` cannot trace `_tex_pin` to a file.
  - It was read with `subprocess.run(['git', 'show', f'{PIN}:corpus/CR_cosmology.tex'], …)`.
  - `_READ` recognises `open(`, `.read_text(`, `read_*(` and the like, but **not a `git show` read**, neither
    inline nor through a helper (`S7`/`S8`'s `_at`).
  - ⇒ The blindness is real, but its cause is **a pinned read is not a file read to the walk**, not a name bound
    away from the clause.  `git grep` finds 61 receipts with a `'git', 'show'` call.  I have not counted their
    keys.
- **① is not in `--quote` itself.**  The operator stores every literal whitespace-collapsed (`' '.join(lit.split())`),
  and `_multi_flags` already tests against the collapsed `.tex` too.  The line-wrap false negative lives in
  instruments that test a raw literal against a raw body.  Among the counts `r7223` names, that is `60`'s `S7`
  and `S8`, which locate sites with raw `x.find(lit)`.  I may not edit those receipts.  So ① is re-measured by
  running `S7`/`S8`'s own code through my loaders, with both sides collapsed, and leaving the receipts untouched.

## The repairs, fixed now

- **R2, the pinned read (mine, in `scripts/mutate_assertions.py`):** `_READ` learns a `git show` read, meaning a
  call whose text carries `'git'` and `'show'` as adjacent list elements, or the string `git show`.  Because
  `_reads` already checks helper bodies against `_READ`, a helper such as `_at` becomes a read with no further
  change.  Nothing else in the operator changes.
- **R1, the wrap (re-measurement only):** run `S7`'s classify and `S8`'s measure with the bodies, the sources and
  the literals all whitespace-collapsed, and compare their buckets with the shipped ones.

## Predictions

- **P1 (R2, new keys).**  Repairing the pinned read adds **between 60 and 250** new `(receipt, literal)` keys to
  the `--quote` population.  Point guess: 120.  Most come from `60`'s `S`-series receipts, which pin through `_at`.
- **P2 (R2, which side).**  Most of the new keys are `PAPER`-targeted, more than half, because the pinned reads
  are mostly of `corpus/*.tex`.
- **P3 (R2, `r7234`'s three).**  All three `_CLAUSES` strings appear among the new keys.  This is the seed for R2.
- **P4 (R1, paper half).**  Collapsing whitespace moves **5 to 25** keys out of `S7`'s `ABSENT` (218).  The 442
  `REVERSAL` count rises by at most that many.
- **P5 (R1, source half).**  Collapsing moves **0 to 10** keys out of `S8`'s `ABSENT` (469).  Python sources wrap
  their docstrings, but most pins quote single lines.
- **P6 (the 2,167).**  R1 changes the unadjudicated 2,167 by **0**, because `--quote`'s keys are already
  collapsed.  R2 changes it only by adding the new keys, and none of the existing keys move.

## What changes in the gate, and how

- New keys from R2 would fail `check_quote_pins` as NEW.  As at `r7201+70.1`, where list keys got their own
  bucket rather than eating the main ceiling, they enter `corpus/quote_pin_baseline.tsv` as a separate
  `UNADJUDICATED-PINNED` bucket.  Its ceiling equals its measured count, and the main 2,287 ceiling is untouched.
- Seeds go in `mutate_assertions.py`'s own seed set.  A pinned read through `subprocess.run(['git','show',…])`,
  and one through a helper wrapping it, must both be keyed.  An `open()` read must still be keyed exactly as
  before.
- No receipt is edited.  No existing baseline verdict is changed.
