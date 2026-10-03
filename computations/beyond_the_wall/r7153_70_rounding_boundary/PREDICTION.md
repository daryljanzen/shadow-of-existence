# r7153+70.1 — PRE-REGISTRATION: is a rounding-boundary verdict measurable?

*Committed before any code.  Node 70.  Read at `origin/main` `eeffaf02`.*

## The question (r7153 ⌗)

A check whose verdict is decided by a rounding boundary rather than by the quantity: `round(x, n) == L`, or
`abs(x - L) < 5*10^-(n+1)` with `n` the decimals of `L`, where the measured `x` sits within a small multiple of the
boundary.  66 asks whether it is MEASURABLE, and to say so if it is dynamic-only and expensive.

## The plan

1. **Static half (mechanical):** `mutate_assertions.py --rounding-boundary` lists every verdict sub-expression of form
   (a) `round(E, n) == L` / `L == round(E, n)`, or (b) `abs(E - L) < T` / `<= T` with `T` equal to half a unit in
   `L`'s last printed digit.
2. **Dynamic half:** run ONLY the receipts carrying a static site, with each site's `E` recorded at run time (an AST
   rewrite of the same kind as r7143's `_counted.py`).  The **margin** of an execution is its distance from the
   boundary in units of `10^-n`: for (a) `|frac(x·10^n) − ½|`, for (b) `(T − |x − L|)/10^-n`.  An execution is
   **ON-BOUNDARY** when the margin is below `10^-3` of a unit.  The pre-r7153 `ℓ = 2` case, at 6e-7 from the
   midpoint with n = 3, has a margin of 6e-4 units.

## Predictions

- **R1** static sites in [20, 200].
- **R2** they sit in [10, 80] receipts, and the dynamic run over those takes under 30 min of wall time.
- **R3 (recall)** the pre-r7153 `P15_the_exact_transmission_ratios…` (`136dd81f^`), run the same way, flags its
  `ℓ = 2` execution ON-BOUNDARY.
- **R4** on the current tree, at most 3 executions corpus-wide are ON-BOUNDARY.
- **R5** form (a) `round(...) ==` outnumbers form (b).
- **The answer to "is it measurable":** yes, mechanically, and affordably, because the dynamic run is needed only
  on the receipts the static half selects.  If R2's time fails, that is the answer instead.
