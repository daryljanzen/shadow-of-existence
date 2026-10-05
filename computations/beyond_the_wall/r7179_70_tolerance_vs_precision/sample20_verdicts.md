# B4 — the seeded sample of 20 SLACK sites at HEAD (`random.seed(7179)`, `sample20.tsv`), read by hand

The verdicts are as follows.
- **GENUINE** means `T` exceeds half the printed ulp of a figure the paper prints for that quantity, and nothing in
  the receipt argues the width.
- **COINCIDENTAL** means the paper prints the number, but for a different quantity.
- **ARGUED** means the width is justified in the receipt, or a tight pin on the same quantity stands beside it.

| # | site | L | T | x half-ulp | verdict |
|---|---|---|---|---|---|
| 1 | `C22_the_end_to_end_number:151` | 1.016 (printed `1.0160`) | 0.002 | 40 | GENUINE |
| 2 | `P15_the_harmonic_expansion…:190` | 5051 (`r_0\approx5051`) | 5.0 | 10 | GENUINE |
| 3 | `C23_the_gap_estimated:156` | 0.010 | 0.002 | 4 | COINCIDENTAL: the paper's `0.010` is a spread and a log-slope |
| 4 | `P15_the_harmonic_expansion…:205` | 7.8 (`\ell_2\approx7.8`) | 0.15 | 3 | GENUINE |
| 5 | `P15_the_fitted_onset…:559` | 0.789 | 0.03 | 60 | ARGUED: "to within two per cent -- a different grid" |
| 6 | `P15_the_segments_conformal_length…:202` | 1.96 | 0.01 | 2 | GENUINE |
| 7 | `P15_the_projection_join…:259` | 4.868603 | 1e-5 | 20 | GENUINE |
| 8 | `P15_the_height_target…:294` | 1.03 (sigma) | 0.05 | 100 | COINCIDENTAL: the paper's `1.030` is an arm-to-control ratio |
| 9 | `C28_length_against_angle:152` | 10.8 (`10.8\%`) | 0.1 | 2 | GENUINE |
| 10 | `C8_diffusion_length:134` | 10.8 | 0.1 | 2 | ARGUED: `abs(pct - 10.83) < 0.01` stands two lines above |
| 11 | `P15_the_expansion_in_the_de_sitter…:169` | 5051 | 5.0 | 10 | GENUINE (the stretch beside it was tightened at r7179) |
| 12 | `P15_the_freezing_census…:157` | 1.96 | 0.01 | 2 | GENUINE |
| 13 | `P15_the_kernels_distance…:319` | 5051 | 5.0 | 10 | GENUINE (the `D_C` beside it is at +-0.5) |
| 14 | `P15_the_projection_join…:253` | 9.443377 | 1e-5 | 20 | GENUINE |
| 15 | `P15_the_shear_coefficient…:210` | 1.1996 | 0.0012 | 24 | GENUINE (a 0.1% relative width, not argued) |
| 16 | `P15_the_height_target…:287` | 0.0772 | 5e-4 | 10 | GENUINE |
| 17 | `P15_the_harmonic_expansion…:545` | 5051 | 5.0 | 10 | GENUINE |
| 18 | `C11_early_isw:127` | 3.80 | 0.01 | 2 | GENUINE |
| 19 | `C10_highl_ratio:100` | 1.082 | 0.001 | 2 | GENUINE |
| 20 | `P15_the_kernels_distance…:170` | 7.8 | 0.15 | 3 | GENUINE |

**Totals: 16 GENUINE, 2 COINCIDENTAL, 2 ARGUED.**  Of the 16 GENUINE:
- **7 are mild (x2-3).**  They admit a value one printed digit off.
- **9 are x10-x40.**
- **The `r_0 = 5051 +- 5` pin appears 4 times** in exactly the four receipts r7179 tightened.  Only their stretch and
  `D_C` were tightened, and this pin was left at 10x.
