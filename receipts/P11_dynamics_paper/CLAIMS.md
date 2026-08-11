# P11 — dynamics_paper — claim inventory (Avenue 11 sweep, r1372; cited no receipts)
From the static operator to the bend: the dynamical/wave sector. Polarized Gowdy-dS wave, the nonlinear
Lambda>0 de Sitter attractor, the Type-I edge, the wall (generative boundary), chirality/handedness.

| # | §label | claim | verifiable? | receipt | status |
|---|--------|-------|-------------|---------|--------|
| 1 | sec:gowdy | polarized Gowdy-dS: R_munu=Lambda g_munu <=> the four field equations | YES | `P11_gowdy_dS.py` | ✔✔ |
| 2 | prop:twoKV | Gowdy-dS with generic psi admits exactly two Killing vectors d_x, d_y | YES | `P11_twoKV.py` | ✔✔ |
| 3 | sec:nonlinear (attractor) | de Sitter attractor: exact background (const H) + conserved shear charge dilutes anisotropy | YES | `P11_deSitter_attractor.py` | ✔✔ |
| 3b | sec:nonlinear (Mukhanov) | linear mode -> Mukhanov W''+(k^2-2/eta^2)W=0, effective mass exactly zero | YES | `P11_mukhanov.py` | ✔✔ |
| 4 | prop:wall | wall = non-degenerate (det g=-1) Type-N Brinkmann wave, NOT a metric singularity | YES | `P11_wall_ppwave.py` | ✔✔ |
| 5 | sec:chirality | H=h_+(x^2-y^2)+2h_x xy vacuum for any h_+,h_x; varying ratio = chirality | YES | `P11_wall_ppwave.py` | ✔✔ |
| 6 | sec:discrete | the strata and their discrete markers | conceptual (classification summary) | — | analytic |

**P11 COMPLETE — 5 computational receipts (r1372-r1376).** gowdy_dS, twoKV, deSitter_attractor, mukhanov, wall_ppwave (covers prop:wall + sec:chirality). sec:discrete is a conceptual classification summary. Coverage audit next.
