# r7155+70.1 — PRE-REGISTRATION: can a name-centred band read its decimals from its own label?

*Committed before any code.  Node 70.  Read at `origin/main` `f440ebd4`.*

## The one measurement (r7155 ⛔)

66 asked whether the decimals of a band whose centre is a NAME can be read from the comparison's own printed
label rather than inferred from a runtime value.  The r7153 repair is the case:
`_d = abs(got[l] - PAPER[l])` … `check(f"… the paragraph's {PAPER[l]:.3f} …", _d < 5e-4)` -- the label formats the
centre `PAPER[l]` with `:.3f`, and `5e-4` is half a unit in the third decimal.

**Form `HALF-UNIT-LABELLED`:** a check `check(label, X < T)` (or `<=`, either argument order) where
- `T` is half a unit in the n-th decimal;
- `X` is `abs(E - C)` or `abs(C - E)`, directly or through a name whose ONLY assignment in the file is such an `abs`;
- `C` is NOT a numeric literal (the literal case is r7153's `HALF-UNIT`);
- the label is an f-string that formats `C` (the same source text) with format spec `.{n}f` -- the SAME n.

The label match is exact and needs no threshold: the decimals are the ones the receipt itself prints.  The dynamic
margin is r7153's, read from `X`.

## Predictions

- **L1 (recall)** the r7153-repaired `P15_the_exact_transmission_ratios…:216` is flagged `HALF-UNIT-LABELLED`
  with n = 3, and its executions all have margin > 1e-3 (its ℓ = 2 execution takes the midpoint branch, not the band).
- **L2** corpus-wide `HALF-UNIT-LABELLED` sites in [1, 30].
- **L3** none is ON-BOUNDARY on the current tree.
- **L4** the static pass adds under 5 s; the dynamic pass on the selected receipts takes under 10 min.
