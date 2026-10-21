# `r7443+71.48` — RESULT: campaign 48. ⌗ J BUILT: row 62's general-jet series through order 4, so claim 1 is now complete. ⌗ K BUILT IN PART: claims 2–5 on the receipt's own jets, with every rank certified, but the contraction entries taken as the receipt's data, spot-checked at 11 entries. ⌗ p `0.25` for J came true; p `0.45` for K did not. ⌗ Row 62 stays `GENERIC-METRIC`, by the registration's own condition

*Scored against `PREDICTION.md` (pushed at `r7443+71.44` before any Lean), not revised. Both probes build with no
error and were re-run by 71 (`PROBE_RUN_A.txt`): J in `1324 s`, K in `966 s`. Every theorem prints `[propext,
Classical.choice, Quot.sound]`, except K's `enumeration`, which prints `[propext]`. No `native_decide`.*

## J — `probes/Row62Jet4.lean`: BUILT

- `jet_series4`: `Scal F h 4 = scT4`, an explicit 745-term polynomial in the fifty jet coordinates. It is proved
  layer by layer like campaign 31, under the same hypotheses.
- `jet_series` is restated through order 4. That ***completes claim 1***; campaign 31 built orders 0–3.
- ***How it fit:*** 5.9 GB, where campaign 31 needed more than 12. Every layer is stated entry by entry. The Ricci
  layer at orders 3 and 4 is split into 216 block lemmas, and polynomials are printed as balanced sums. ***The
  cause of the earlier out-of-memory kills was info-tree retention, not proof size.*** A one-line command wrapper,
  `noinfo` (`withEnableInfoTree false (elabCommand c)`), switches that retention off. It changes nothing the kernel
  checks; the axioms above confirm it. Recorded as meta-code in a probe.
- An independent sympy recomputation matches campaign 31's tables exactly.

## K — `probes/Row62Claims.lean`: BUILT IN PART

***Built:***
- the enumeration `372/672/60/945`, computed in Lean;
- the 17 jets, transverse-traceless and satisfying the frame commutator;
- the `ε⁴` coefficient at every jet, from the receipt's Koszul series ported over ℚ;
- every rank, as `Matrix.rank`, with certificates (an invertible minor below, row combinations above): A 8, B 4,
  Q 1, A+B 12, Q inside, div 5 inside, dimension 7;
- the control rank 11;
- the eight selected columns independent;
- 7 + 5 spanning the 12, with a unique split;
- the identity holding on all 17 jets;
- the twelve coefficients, sharing the denominator 192;
- the frame-constant measurement rank 1, computed in Lean.

***Open, named exactly:***
- ***(i)*** The ~35 000 contraction entries of the rank matrices are the receipt's exported values. They are checked
  against Lean's own contraction at 11 entries only, because the kernel takes about 1 s and 100 MB per 3⁵-term
  contraction.
- ***(ii)*** The six configurations' 6×8 rows are the receipt's S³ integrals, taken as data.

***Not a disagreement, a unit:*** the receipt's `−7/12 p₂²` is per unit volume. In its π²-normalised rows it is
`−7/6 p₂²`, and K states it that way. ***No disagreement with the receipt on substance.***

## The census

The registration made row 62 `DONE` conditional on K being BUILT, so ***row 62 stays `GENERIC-METRIC`***. Its
`decl` stays empty by the rule for that status. What is now open is (i) and (ii) above, and nothing in claim 1.
The next campaign is (i): a faster kernel evaluator for the contraction entries, priced and registered on its own.
