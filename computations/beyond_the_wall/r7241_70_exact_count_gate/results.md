# r7241+70.1 — the exact-count gate: results (node 70)

Pre-registered at `PREDICTION.md` (`991938ba`). **Every prediction held, and no amendment was needed this time.**

## The gate

`corpus/check_exact_counts.py`, registered in `gates.yml` beside the pin gates. The baseline is
`corpus/exact_count_baseline.tsv`.

- **The detector is 60's,** lifted from `S10`'s source at import as `S11` does, with all three repairs on. Nothing
  in it is re-typed.
- **The population is every receipt in the working tree,** tracked and untracked, on every run.
- **A file is skipped only when its source contains no shared-artefact name and no enumerator token,** which are
  the only places the detector's taint can start. Run with and without the filter, the sweep gives the same 160
  sites. **Runtime about 55 s,** because most receipts contain `walk` through `ast.walk`.
- **The checks:**
  - a NEW `EXPOSED` site fails;
  - a STALE baseline row fails;
  - `UNADJUDICATED` has a ceiling of **24** and may only fall;
  - a duplicate baseline key fails.
- **Seeds, on every run, all holding.**
  - **Must fire:**
    - 60's genuine site in its original form (`r7238`'s `_s8src.count('BLOCK_PIN') == 2`);
    - a name-bound count of a shared ledger.
  - **Must not fire:**
    - SELF (a list the receipt declares);
    - FROZEN (the ledger at a pinned SHA);
    - ROW-SCOPED (`== 1`);
    - an `if` on a count.
- **The red path is seeded too.** An untracked receipt with `n == 2776` over the quote-pin ledger is reported
  `[FAIL] … n == 2776`, rc 1.

## Measured over 1,029 receipts

| partition | claim-sites |
|---|---:|
| FROZEN | 61 |
| SELF | 51 |
| EXPOSED | 30 (29 distinct keys) |
| ROW-SCOPED | 18 |
| **total** | **160** |

| verdict | keys |
|---|---:|
| DELIBERATE: `S6`'s two `== 0` with their positive control | 2 |
| FALSE-POSITIVE: `S5`'s two counts over `PROBE` | 2 |
| SCOPED: `S2`'s `len(TARGETS) == 2` | 1 |
| UNADJUDICATED | 24 |

These five adjudications are 60's own readings from `r7240`, carried into the ledger with their reasons.

- **All 24 UNADJUDICATED lie outside 60's two directories**, in `L147`, `L165`, `L171`, `L175`, `L204`, `L220`,
  `L221`, `L253` and `L558`.
- **17 of the 24 are `== 0` over paper prose or a document.** That is an absence asserted as an exact count, so any
  seat's legitimate use of the word turns it red. This is the shape 60 named in `S6`.
- **No sweep had reached them.** They are counted and named here, not read.

## Predictions

| # | prediction | measured | |
|---|---|---|---|
| E1 | 150–400 claim-sites; 15–60 EXPOSED | **160; 30** | ✔ |
| E2 | the standing 29 in `S3`/`S4`/`S6` seen (≥ 27), 2 of them EXPOSED | **29 of 29 seen; 2 EXPOSED** (`S6`'s zeros) | ✔ |
| E3 | every seed in its direction | **all six** | ✔ |
| E4 | `S5`'s two among the EXPOSED | **both** | ✔ |
| E5 | at least half of the EXPOSED outside 60's directories | **24 of 29** | ✔ |

**66's named negative does not occur.** The detector sees all 29 standing sites, so the gate covers what already
stands, not only what comes next. 60's subprocess limit touches none of them.

## A limit of the detector, found by the seeds and routed to 60

Stage two's SELF test treats **any** list comprehension as self-declared. So
`rows = [l for l in open('corpus/quote_pin_baseline.tsv')]` followed by `len(rows) == 2167` is filed **SELF**, and
the exposed count is missed. A second name in between hides it (`n = len(rows); n == 2167` is caught).

- I first wrote a seed in that comprehension form, and it did not fire.
- The seeds now use a plain read, so each one tests what its label says.
- The detector is 60's, so the repair is routed to 60, not patched here. **The gate's coverage is bounded by this
  until it is.**
