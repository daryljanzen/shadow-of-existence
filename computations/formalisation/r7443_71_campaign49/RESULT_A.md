# `r7443+71.58` — RESULT: campaign 49 BUILT. ⌗ Row 62's two data gates are closed: every one of the ~40 000 contraction entries is Lean-computed, and the six configurations' S³ integrals are proved in closed form. ⌗ p `0.40` came true. ⌗ Row 62 → `DONE`; GENERIC-METRIC → `0`

*Scored against `PREDICTION.md` (pushed at `r7443+71.49` before any Lean), not revised. `probes/Row62Data.lean`:
38 theorems, standard axioms (`enumeration` on `propext` alone), `3217 s`, 2967 lines (band 400–2200, MISSED HIGH by
767, because it carries K's file wholesale; the stop of `3000` was not fired). No `sorry`, no `native_decide`, no
meta-code. The build was delegated and re-run by 71 (`PROBE_RUN_A.txt`).*

## (i) The contraction entries: BUILT

- ***A fast evaluator over `Nat`.***
  - Integer jets are packed 64 bits per entry, so a lookup is a shift and a mask.
  - Each pattern is compiled to strides, and a nested loop does only `Nat` add and multiply.
  - Decoding is exact because entries are at most 100, which bounds every value below `2⁶³`.
- ***Proved equal to the contraction generically.*** `fast4_correct` and `fastD_correct` hold for every good pattern
  and every bounded integer jet.
- ***Kernel cost.*** About 25 ms per entry, against about 1–3 s for the ℚ evaluator. The gain is GMP-backed `Nat`
  arithmetic.
- ***Every table is proved equal to the evaluator on the receipt's jets*** (`tA_eq` … `falsRows_eq`). The rank
  theorems are restated on the ***Lean-computed*** matrices, and both sides of the identity are computed.

## (ii) The six configurations' S³ integrals: BUILT

- The configurations are built on the Euler chart. The frame rule is proved with real derivatives
  (`rad_rows_frame`), and every component is traceless and transverse.
- A general engine integrates trigonometric monomials over the Euler box. On top of it:
  - the 35 sphere moments of degree ≤ 4;
  - `moment4` for all real coefficients;
  - `six_configurations_integrals`: every one of the 48 entries equals the receipt's value times `π²`;
  - the measurement rank `4 < 7`.

## Census

Row 62 → `DONE`. Claim 1 was complete at campaign 48, and claims 2–5 now rest on no receipt data. ***No
disagreement with the receipt***: every exported entry and all 48 integrals match.
