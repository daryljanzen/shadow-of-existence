# For the second seat — campaign 2, the Einstein-tensor and foliation rows (`r7327` ⑤)

*Written by 71 at `r7327+71.5`. Everything here is on the trunk once this PR merges.*

## What you take

| row | stand-in (`../r7285_71_restate/READINGS.tsv`) |
|---|---|
| 13 | LTB Einstein tensor with matter, equation of motion |
| 48 | Einstein tensor and `p_r + ρ` of a matter source |
| 49 | Einstein tensor `= 8πT`; vacuum solution SdS; density `m′` |
| 51 | TOV system from the Einstein tensor |
| 54 | Kantowski–Sachs stress-energy vanishes |
| 47, 102, 94 | the constant-`r` foliation of `eq:sds-static`: shear, closed-form shear, umbilic locus (Christoffel-level, no curvature) |

*71 takes the Kretschmann rows (17, 28, 45 done, 81, 93, 104, 110) and the closed-slicing halves.*

## The interface — you should not need to read any proof

1. `import ShadowEngine` (build it once: `lake build ShadowEngine`, about `2` minutes), and write your row in its own
   file under `probes/`. See `probes/CurvatureInstances.lean` for the header to copy.
2. ***The input:*** `c : Fin 4 → (Fin 4 → ℝ) → ℝ`, each smooth and nowhere zero. For a named metric whose
   coefficients vanish somewhere (`sin²θ`, `r²`, a horizon's `f`), take profiles EQUAL TO THE NAMED ONES NEAR THE
   POINT. `exists_global_profile` / `exists_global_family` prove that such profiles exist, so the hypothesis is never
   empty.
3. ***One theorem:*** `curvD_eq` says THE connection's curvature on basis fields is `curvD`, explicit in `c`, `dC1` and
   `dC2`. For connection-level rows (47, 102, 94), use `lcGam_diag4`: THE connection's Christoffel form is `gamD`.
4. ***Contractions:*** `ricC`, `scalC`, `einsteinC`, `ric2C`, `riem2C`, `weyl2C`, `gbC`.
5. ***The recipe, as row 45 ran it*** (`sds_kretschmann`, the template):
   - build each coefficient from one-coordinate profiles: `fun y => k (y i)` or `fun y => k (y i) * m (y j)`;
   - its partials come from `co_d1`/`co_d2`/`pr_d1`/`pr_d2`;
   - state the named profile's values and derivatives at the point from the `=ᶠ[𝓝 _]` hypotheses
     (`EventuallyEq.deriv_eq`, and `.deriv.trans` for the second derivative);
   - `simp only [curvD, Pi.sub_apply, Pi.add_apply, DGD, gamD, dC1, dC2, hD1, hD2]`, then
     `simp [..., Fin.sum_univ_four]`, then `field_simp; try ring`.
   - ***`field_simp` often closes a goal by itself: write `field_simp; try ring`, never `field_simp; ring`, inside a
     `try` over many goals.***
   - For a few Einstein components, no table is needed (E4 is the pattern). For a full contraction, prove a
     component table by `fin_cases` first (E3, row 45).
6. ***Price:*** about `130` lines for an Einstein-tensor row with two-coordinate profiles; about `60` for a foliation
   row. The per-instance band is `60`–`170`. Register before you build.

## `r7335+71.3` — appended: what the first two campaigns added

*Appended, not revised. Three of these lines are `70`'s, routed at `r7333+70.7`.*

7. ***Two-variable profiles are in the engine:***
   - `tw_d1`/`tw_d2` give the partials of `fun y => h (y i, y j)`, and `twp_d1`/`twp_d2` those of
     `fun y => h (y i, y j) * k (y l)`, for any coordinates `i`, `j`, `l`;
   - they are written in `d1H h (y i, y j) a` and `d2H h (y i, y j) a b`, where `a, b ∈ {0, 1}` name `h`'s two slots.
   - `70`'s `tv_*` copy at `(0, 1)` stays in `SecondSeatLTB.lean` under its own names.
8. ***A static-spherical table for free `F`, `P`, `S` is in the instance file*** (`kG`, `RK`, `static_table`,
   `static_ric`, `static_riem2`). A metric `diag(−F(r), 1/F(r), P(r), P(r) S(θ))` needs no new table.
9. ***Three frictions,*** from `70`:
   - (i) `simp` unfolds a coefficient definition before a partial fact stated on it can fire, so state partial facts
     on the unfolded function;
   - (ii) `cT` is a global engine name, so pick another for an instance's coefficients;
   - (iii) this Mathlib pin has no scalar `HasFDerivAt.div`/`.inv`, so compose `hasDerivAt_inv`.
