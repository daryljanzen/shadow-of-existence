# Generator for campaign 135 (`car_`)

These are sympy scripts, not Lean, and no claim rests on them. Every lemma they emit is checked by Lean in
`probes/Range.lean`. The method is campaign 134's, re-parametrised for abstract structure functions.

- `genc.py` holds the atoms and the term builder:
  - `Σ = r² + p²` (`car_S`);
  - `R`, `R1`, `R2` (`Δ_r` and its derivatives);
  - `P`, `P1`, `P2` (`Δ_p` and its derivatives).
- `emit.py` writes `part1.lean` and `p1.pkl`:
  - the metric entries and their 10 derivative lemmas;
  - the inverse;
  - the 20 Christoffel entries and their 40 derivative lemmas;
  - the Ricci table.
- `emit2.py` writes `car_inv`, `car_T`, `car_Γ`, `car_Hyp`, `car_pd`, `car_RicM` and `car_Ric`.
- Row 5's "if" and "only if", rows 7a, 7b and 8b, and the witnesses are hand-written in `Range.lean`.

Run with `python3 emit.py > /dev/null; python3 emit2.py > part2.lean` (sympy 1.14).
