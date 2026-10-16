# The plain wording of the formalisation's status classes

The public page that lists every formalisation row uses these words. The page's generator reads them from this directory.

- `WORDING.tsv`. One line per status class as it appears in `computations/formalisation/r7325_71_inventory/ROWS.tsv`. Each line gives a heading for the page and one sentence a reader can follow.
- `GAPS.tsv`. The four named library gaps, said plainly.

**What a row is**, for the page's opening: each row is one calculation that a receipt performs and a paper relies on. The page says, for each row, whether that calculation is also proved in Lean.

**Rules for the wording:**
- No class reads as a shortfall. Each sentence says where the claim is settled: in a proved theorem, in a proved general identity, in rows named beside it, or in a receipt that runs.
- A class the inventory adds later gets a line here before it is published. The generator should refuse a status that has no line, rather than print the bare label.
