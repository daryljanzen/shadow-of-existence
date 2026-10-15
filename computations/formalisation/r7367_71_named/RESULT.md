# `r7367+71.1` — the seven unnamed DONE rows are named, and one leaves DONE. ⌗ Rows 29, 41, 42, 43, 74 and 92 now cite their declarations. Row 77 moves to DONE (chartable half), because its receipt's "exactly two Killing vectors" was never built. ⌗ Re-run: ***`57` of `57` DONE rows re-run clean from HEAD, `0` not clean, `0` unresolved.*** ⌗ Census: DONE `50`, halves `7`

*Answers `FOR_71.md` §`r7367` ③: "name each one's declaration, or move the row off DONE". The measurement is
`RERUN_CENSUS.txt` beside this file. It was taken with the same committed `rerun_census.py` as `r7365+71.2`, on
the census as edited here.*

## What each row now cites

| row | stand-in | declarations named | where |
|---|---|---|---|
| 29 | the cycloid solves the radial geodesic | `unitU_geodesic`, `interior_chart`, `interior_geodesic`, `cycloid_proper_time` | `ShadowEngine.lean`, `StaticDiag` (r7297 C4) |
| 41 | `κ = f′/2` | `surface_gravity`, `kappa_half_fprime` | `ShadowEngine.lean`, `SurfGrav` (r7297 C3) |
| 42 | I20: conformal Killing, the charge on null geodesics, `1 + z` | `conformalKilling_cov`, `charge_const`, `xi_isConformalKilling`, `a_omega_const`, `one_plus_z` | `probes/InstanceProbe.lean` (r7277 R4 and earlier) |
| 43 | the homothety charge, conserved on null geodesics only | `flat_isLeviCivita`, `homothety_nabla`, `homothety_charge` | `ShadowEngine.lean`, `FlatLC` (r7297 C1) |
| 74 | Gowdy–dS `3H² = Λ`, the shear charge | `gowdy_ds_field`, `gowdy_shear_charge` | `probes/CurvatureInstances.lean` (E4) |
| 92 | `sinh^{2/3}` solves the `E = 1` radial geodesic | `rain_geodesic`, `sds_rain_geodesic`, `sinh23_flow` | `ShadowEngine.lean`, `RainPG` (r7297 C2) |
| ***77*** | Killing equation: EXACTLY two Killing vectors | `killing_of_invariant`, `gowdy_killing` | `ShadowEngine.lean`, `KillingTrans` (r7297 C5) |

***Row 77 leaves DONE.*** The two theorems prove `∂_x` and `∂_y` are Killing. The receipt also claims there are
EXACTLY two, so no third exists.
- `r7297`'s own RESULT ("beside the score", item 1) recorded that uniqueness as NOT built. It is a Lie-derivative
  statement with no connection in it.
- The census still read DONE. Naming the declarations is what exposed this: the named theorems do not cover the row.
- So the row is now `DONE (chartable half)`, with the uniqueness named as its open half.

***Some names resolve in more than one file.*** `conformalKilling_cov` is declared in `ConnectionProbe.lean`,
`GeodesicProbe.lean` and `InstanceProbe.lean`, and `one_plus_z` and `a_omega_const` also in `ShadowFormal/I20.lean`.
The script checks EVERY declaration of a cited name, and all of them are CLEAN.

## The re-run

| | `r7365+71.2` | ***now*** |
|---|---|---|
| DONE-status rows (whole or half) | `57` | `57` (`50` whole, `7` halves) |
| re-run CLEAN from HEAD | `50` | ***`57`*** |
| not clean | `0` | `0` |
| unresolved | `7` | ***`0`*** |
| axiom lines, all CLEAN | `297` over `17` files | `345` over `22` files |

***So DONE now means re-runnable from what is committed, for every row that carries it.***

## Census (moved in this push)

| status | before | now |
|---|---|---|
| DONE | `51` | ***`50`*** (77 out) |
| DONE (chartable half) | `6` | ***`7`*** (+ 77) |
| generic-metric / no-connection / library gap / real obstruction | `2` / `32` / `17` / `3` | unchanged |

*Nothing in the quote-pin stride. The `21` calibration keys are untouched.*
