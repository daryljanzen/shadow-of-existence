# r7221+70.1 — the 270 source-half keys from `60`'s `r7230`: a verdict on each, split by repair cost. Pre-registered before measuring

*Ordered at `r7221`.  The method is `r7215+70.1`'s, applied unchanged where it can be and adapted where the source
half differs, with every adaptation named below.  Predictions are made for this population; none is carried
over from the paper half.*

## The population, fixed now

- The 270 are `S8`'s readable source keys that are **not** discriminating: `REVERSAL` plus `REVERSAL-PARTIAL`,
  326 − 56 = 270.  They are found by executing `S8`'s own source, unmodified, through its section D.  That uses
  its sliced `r7228` instrument, its pinned tree, its self-exclusion and its prose filter.
- Only the per-key bookkeeping is mine.  `S8`'s `measure()` keeps no per-key list for `REVERSAL-PARTIAL`, so I
  re-walk the same rule with `S8`'s own functions.  **Before any distance is computed, my per-key tallies must
  equal `S8`'s `ST` on every bucket**, or the run stops.

## The verdict, fixed now

Each key gets one verdict row:

- **status**: `REVERSAL` (survives every reversal) or `PARTIAL` (survives some);
- **D**: the fewest characters by which the literal must be extended, verbatim and inside its own prose clause,
  so that every reversal of that clause breaks it.  D is measured at every prose site, and the key's D is the
  worst site.  A search reaching 300 characters without success records `>300`, as at `r7215`;
- **class**: `EXTEND-SHORT` (D ≤ 25), `EXTEND-LONG` (26–100), `CLAUSE` (> 100 or `>300`).  These are the paper
  half's thresholds, unchanged, so that the two halves compare;
- **sites**: `SINGLE` or `MULTI`, counting prose sites in foreign files;
- **edit sites**: the `r7215` v2 rule — the literal occurs exactly once in a `'…' in` assertion form in the
  pinning receipt.

## One adaptation, named

On a source site the extension also has to stay inside the prose span (the docstring or one comment line).  A
clause that runs into code is cut at the prose span's end.  It is not a paper half rule, and it can only make D
larger or `>300`.

## Predictions

- **P1**: `EXTEND-SHORT` is 20–35% of the 270.  Comment-line clauses are short, so short repairs should be
  commoner than the paper half's 18%.
- **P2**: `CLAUSE` is 20–40%.
- **P3**: single-site median D is 25–45, below the paper half's 54.
- **P4**: `PARTIAL` keys are cheaper than `REVERSAL` keys: their median D is lower by at least 10.
- **P5**: v2 edit sites are exactly one for at least 75% of keys.
- **P6, the split itself**: the three-way split holds if each arm holds at least 10% of the 270.  If one does
  not, I report that the population does not admit the split, and give the D distribution actually found, as
  `r7221` asks.

## Seeds, run before the census

- the three `r7215` seeds, unchanged, on the shared `min_ext`;
- a prose-span seed: a clause whose only reversal lies past the end of its comment line must give `>300`, not a
  D that reaches into code.

No receipt, no baseline row and no verdict field in the baseline is edited.  The verdicts are this file's output,
banked as one row per key.
