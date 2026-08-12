# For the node that commits this

*You are landing a batch of **drafts**, not corpus changes. Read this whole file before touching
the tree. It is short.*

---

## What this is

Eleven findings from a long read of the CR corpus at `r2376+c54.108`, produced by a Cowork node
with no repo access. Every one was verified at source; every runnable artefact was executed
against the live tree immediately before packaging. `README_START_HERE.md` is the cover note and
`INDEX.md` is the table.

## The one rule that matters

**Nothing in this batch is a closure, and nothing in it may be landed as one.**

`PROTECTED_OPEN.md`: *"A node MAY write a BOUNDED NEGATIVE … A node may NOT write a CLOSURE on a
registered item."* Bounded negatives are the node's; closures on protected items are Daryl's.

So: **commit these files as they are.** Do not merge their recommendations into the papers, do not
strike a lead in `THE_LIVE_ARC.md`, do not edit `corpus/*.tex` or `corpus/check_*.py` on the
strength of them. Each finding states what it does not claim and what would reverse it; that
framing is load-bearing and must survive the commit intact.

If you disagree with a finding, **say so in a new file beside it** rather than editing it. The
corpus's own practice is to keep the wrong version and record the correction — two of these
findings do exactly that about their own author.

## Where to put it

```
_dig/findings/          <- the whole directory, as-is
```

`_dig/` is a working area created for this dig. It is not part of the corpus proper and nothing
in the ten gates reads it. If the repo has a better home for node-side drafts, use that instead —
but keep the directory intact rather than scattering the files, because several findings cross-
reference each other by filename.

## Run the gate first

Before committing, from the repo root:

```
python3 corpus/check_kills.py        # must report: no unauthorised closures
python3 corpus/check_compile.py      # must stay green — nothing here touches corpus/
```

Both were green at packaging time. If either fails, **something else changed** — this batch adds a
directory and edits nothing.

## Suggested commit

```
_dig: eleven findings from a full-corpus read at r2376+c54.108

Drafts only — bounded negatives and offered additions, no closures.
Four drop-in gate patches (currency anchor, self-reference, citation-number
report, receipt fingerprints) each run against the live tree; one blessed
fingerprint baseline over all 249 receipts; four closed forms for quantities
the papers quote as decimals.

See _dig/findings/README_START_HERE.md.
```

## The artefacts, and what they do when run

Every `DRAFT_*.py` is standalone and expects to be run from `_dig/findings/` with the repo root two
levels up. Deps: `numpy scipy sympy` (and `camb pynucastro` only for `capture_receipt_output.py`).

| file | run result at packaging | note |
|---|---|---|
| `DRAFT_check_currency_patched.py` | **rc=1**, 5 stale registers | this is the correct result — the current gate returns 0 and should not |
| `DRAFT_check_compile_selfref.py` | **rc=1**, 1 hit in 35 files | prints the directory and file count it scanned, on purpose |
| `DRAFT_receipt_fingerprints.py` | **rc=0** against the blessed baseline | needs `/tmp/rcpt_out/all.json` from `capture_receipt_output.py`, or it re-runs everything (~40 min) |
| `DRAFT_check_numbers_at_citations.py` | 15 flags / ~250 citations, 1 real | ships as a **report**, not a gate — see its docstring for why |
| `DRAFT_P03_…`, `DRAFT_P07_…`, `DRAFT_P09_…`, `DRAFT_P10_…` ×2, `DRAFT_P15_…` | **rc=0** | the physics receipts; each asserts its own results |

`receipt_fingerprints.json` is a **blessed baseline at this cut**. If receipts have changed since
r2376+c54.108, re-bless rather than reporting a failure — the file records what the tree printed on
2026-08-12, nothing more.

## Two things in here are wrong on purpose

- `DRAFT_P09_which_homogeneous_cosmologies_are_cuts.py` PART 7 opens by quoting an **over-claim its
  own author nearly published** and then dismantling it. That is the point of the section; do not
  tidy it away.
- `F04` records that the self-reference gate, on its first packaging, **scanned zero files and
  returned green** — the exact defect it exists to catch. Also deliberate.

## What is not done

Eight papers are unworked at source: **P02, P05, P06, P11, P12, P13, P14, P17.** The matter sector
is the gap that matters — `L-136` is where two items converged and where the remaining conceptual
debt has collected. Whoever picks this up next has that runway.
