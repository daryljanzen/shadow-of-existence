# For the node that commits this — BATCH 2

*Same rules as batch 1. If you have not read `_dig/findings/COMMIT_INSTRUCTIONS.md`, read it first;
this file only records what is different.*

---

## What is different

- **This is additive.** It lands in `_dig/findings_batch2/` and touches nothing in
  `_dig/findings/`. If batch 1 is already committed, this is a new directory and a clean diff.
- **Batch 2 works the papers batch 1 left unread at source** — P11, P12, P13, P14. P02, P05, P06
  and P17 were probed and returned nothing, which is recorded in `INDEX.md` rather than dropped.
- **F15 ships an instrument** (`DRAFT_receipt_scope_table.py`) whose value is the `DELIBERATE`
  allowlist it asks a maintainer to curate. Landing the script without ever curating that list
  wastes it.

## The one rule, again

**Nothing here is a closure.** Commit the files as they are; do not merge their recommendations into
the papers, do not strike a lead, do not edit `corpus/*.tex`. `check_kills.py` was green at
packaging.

## The artefacts

Run from `_dig/findings_batch2/` with the repo root two levels up. Deps: `numpy sympy`.

| file | result at packaging |
|---|---|
| `DRAFT_P11_where_the_two_notions_part_company.py` | rc=0 |
| `DRAFT_P12_the_bianchi_stratum_is_six_of_nine.py` | rc=0 |
| `DRAFT_P13_su3_fits_exactly_one_real_form.py` | rc=0 |
| `DRAFT_P14_the_leaf_is_compact_except_at_the_seam.py` | rc=0 |
| `DRAFT_receipt_scope_table.py` | rc=0, ~1 s; `--full` for the per-receipt table |

## If you land only one thing

**F14.** It is the only item here that touches a load-bearing claim: P14 offers leaf compactness in
place of the bulk index P13's non-compactness obstructs, the supporting receipt runs at M = 0.62 M_N
where the roots are simple, and the integral **diverges logarithmically at the Nariai member** —
which is the corpus's own seam. The paper does not name its member. That sentence should.

## If you land only one *instrument*

**F15's scope table.** It is one second, no dependencies, and it found in one run the thing F11 had
caught only one seam of.

## The arc worth reading as a unit

`_dig/findings/F05` → `F12` → `F16`. Three findings that converge on a single cheap question — **is
the orthogonally-transitive unpolarized G₂ class in the range?** — which settles one sentence in
each of P11 and P12 and closes F05. It is the item I would most like a physicist's eye on.

## What is still not done

**P17 (geometric core, 1589 lines)** is the largest paper in the corpus and was not worked at
source. P02, P05 and P06 were probed at specific claims, not read whole.
