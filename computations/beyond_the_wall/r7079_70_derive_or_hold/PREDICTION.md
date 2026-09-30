# r7079 (70) — over the twenty-five carriers: does each one derive its number, or hold it?

*Pre-registered before any carrier is perturbed or run. The order is `FOR_70.md` `r7079` Q1, unchanged from `r7077` and `r7075`. The set is the 25 carrier–number pairs of `computations/beyond_the_wall/r7069_70_transposition_gate/confirm_log.txt`, and nothing wider.*

## The test, and one declared deviation from the one offered

`r7077` offers this test: perturb an input the receipt computes from, and see whether the number moves. As offered, it needs the input chosen per carrier by hand, which is a judgement the instrument would be making for me. **The test used is its dual, which is mechanical.**

**SENTINEL.** In a scratch copy of the carrier, every source occurrence of the number is replaced by a different value of the same form, in code and in strings alike. This covers:
- a decimal at or rounding to the paper's precision;
- `p/q`, `Rational(p, q)` and `Fraction(p, q)`;
- the decimal value of a fraction;
- a bare integer.

The copy is then run fresh, in the carrier's own directory.

| outcome of the sentinel run | class |
|---|---|
| the output still carries the number | **DERIVED**: the receipt's arithmetic produces it without the literal |
| the receipt now fails, at an assert or check whose line held the replaced literal | **DERIVED-AND-PINNED**: the literal is checked against something computed, so it moves and fails, which is correct practice |
| the receipt fails elsewhere | **INCONCLUSIVE**: the literal may be a held input feeding other checks |
| it exits 0 and the output no longer carries the number | **HELD**: the number is written into the file, and nothing fails if it is false |
| the number is also found in a data file or local module the carrier reads | **INCONCLUSIVE**, whatever the run says, because the replacement did not reach it |
| the number is not in the carrier's source at all, but the carrier prints it | **DERIVED**, with no sentinel needed, subject to the data-file check |

## Calibration, a condition of delivery (the r7069 standard)

The instrument is not built unless all three hold:
- `P16_validate_bbn`, 2.5671 and 4.4611, classes **DERIVED** or **DERIVED-AND-PINNED**. This is the derived case named in the order.
- `P15_the_low_ell_minimum_is_at_ell_four`, 0.926, classes **HELD**. This is the held case named in the order. It is outside the 25 and is run only as a control.
- `P16_nariai_welds`, 7.06, classes **HELD**. This is the case that motivated the order; `r7075` reads it as printed in narration and derived nowhere.

A fourth control is `P15_the_exact_transmission_ratios_are_recomputed_and_the_offset_saturates`, 0.926, built at `r7073`. It is expected **DERIVED**. It is reported, but it is not a condition.

## Outcomes, the one that costs another seat most first

1. **HELD among the 25.** Each one routes to 66 for a build or a re-point. **Predicted: `P16_nariai_welds` 7.06 (the calibration), plus zero to two others.** The candidates I would name before running are the single-number carriers: `P15_the_geometry_transmits_no_parameters` 3.32, `P16_the_adiabatic_premise_…` 294 and `C8_diffusion_length` 10.8. That is a guess, and it is recorded as one.
2. **INCONCLUSIVE.** **Predicted: one to four**, mostly carriers that read data files (the CAMB carriers) or import local helpers.
3. **DERIVED or DERIVED-AND-PINNED**: the rest.

## Scope

- **The class is mechanical.** Whether a HELD number is the paper's own result or a value read from the world is **66's read**. I send the shortlist with the mechanical answer only.
- The four intentional sites are run because they are among the 25, and **not re-adjudicated**.
- The 45 "own prints" lines are out of scope.
- The scratch copies are made outside `receipts/`, and no receipt is edited.
