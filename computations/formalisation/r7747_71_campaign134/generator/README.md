# Generator for campaign 134 (`kds_`)

These are sympy scripts, not Lean, and no claim rests on them. Every lemma they emit is checked by Lean in
`probes/Range.lean`.

- `gen.py` holds the atoms (`P = ρ²`, `D = Δ_r`, `Q = Δ_x`, `S = 1 − x²`, `X = Ξ`).
  - `atomize` writes a rational function over atom denominators.
  - `tree` and `tproof` turn an expression into a `HasDerivAt` term built from `fun_add`, `fun_mul`, `fun_pow` and
    `fun_div`.
- `gen2.py` holds the emitters, which close each lemma by `congr_deriv` with `field_simp` and `ring`.
- `stage1.py` emits the metric entries and their 10 derivative lemmas. Run it first: it writes `fa1.pkl`.
- `stage2.py` emits the inverse, the 20 Christoffel entries and their 40 derivative lemmas. It writes `fa2.pkl`.
- `stage3.py` emits:
  - the metric matrix;
  - `kds_inv`, `kds_T`, `kds_Γ`, `kds_Hyp`, `kds_Hyp.U` and `kds_pd`;
  - `kds_vacuum` and `kds_const_curv`.
- Rows 4b, 4d and 4e, the witness and the atom derivative lemmas are hand-written in `Range.lean`.

Run with `python3 stage1.py; python3 stage2.py; python3 stage3.py` (sympy 1.14).
