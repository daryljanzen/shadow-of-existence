# `r7443+71.44` — PRE-REGISTRATION: campaign 48, row 62's open parts — claims 2–5 on the receipt's own jets, and the general-jet order 4. ⌗ `3000` lines (band 1500–6000; the tables are long lines), ⛔ stop `8000`. ⌗ p `0.45` for claims 2–5; p `0.25` for order 4

*Under `r7443`, and `r7471`'s order: row 89, then row 62's general jet. The receipt is
`receipts/P10_canonical_time/P10_the_covariant_quartic_is_seven_rationals_carried_by_an_identity_and_no_measurement_route_reaches_them.py`.
Campaign 31 built claim 1 in part (`probes/Row62Jet.lean`). No Lean was written before this registration.*

## ① The pieces, scored separately

***K — claims 2–5 on the receipt's own finite data*** (`probes/Row62Claims.lean`).
- The receipt's computations are finite, and so is the formal statement:
  - the enumeration `372 / 672 / 60 / 945` of admissible contractions;
  - the ranks `8, 4, 1`, union `12`, divergences `5` inside the union, and integrated dimension `7`, ***as
    ranks of the receipt's own matrices*** on its own transverse-traceless jets. The jets are regenerated
    exactly from the receipt's seeded construction;
  - the control (dropping transversality raises A's rank);
  - the eight selected columns independent;
  - the seven rationals with denominator 192 solving the identity on every listed jet, held-out jets included;
  - the measurement-route ranks: `1` on the frame-constant sector, `4` on six configurations.
- Each rank is a nonzero minor, which bounds it from below, and exhibited kernel vectors, which bound it from
  above. Everything is over ℚ, checked by `decide +kernel` or `norm_num`.
- The `ε⁴` coefficient at each jet is evaluated numerically, not as the general polynomial. Each rational jet is
  pushed through the layered frame-Koszul tables of `Row62Jet.lean` at concrete values.
- ***Caveat, registered:*** the ranks are statements about the receipt's sampled jets, exactly as the receipt
  computes them. "Pointwise rank on the whole TT variety" is not claimed by K.

***J — the general-jet order 4*** (`probes/Row62Jet4.lean`).
- Campaign 31's order-4 Ricci layer has `6421` terms and exhausted `12 GB` as single lemmas.
- Route: split it by output component and by term block into lemmas of at most about 400 terms, each proved from
  the layer below, with `Elab.async false`, then sum the pieces.
- If the peak still exceeds about 11 GB, J is reported with the measured peak per block.

***Failable:*** K and J are each BUILT, BUILT IN PART, or REPORTED. ***Row 62 → `DONE`*** needs K BUILT. J is
claim 1's remainder. If J is not built, row 62 is `DONE` with claim 1's order 4 named as its one open part.

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
