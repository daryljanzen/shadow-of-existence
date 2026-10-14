# `r7333+70.6` — RESULT: all eight instances land, with no `sorry` and every axiom line `[propext, Classical.choice, Quot.sound]`. ⛭ All eight are inside their own registered bands. 71's band (`60`–`170`) holds on exactly the four I predicted, and fails on exactly the four I predicted, in the predicted direction. ⌗ The interface held without one proof body being opened. Its one gap was the one I named before building: two-variable profiles, `100` lines

*Registered at `PREDICTION.md` (`57424573`, 18:47 UTC, pushed before any Lean). Each probe run is filed raw beside it.
Counts are made as registered: one `section`, from its `/-!` header to its `end`. **Nothing in the registration
is revised.***

## The instances

| row | file | theorem(s) | central | own band | **measured** | own | 71's 60–170 |
|---|---|---|---|---|---|---|---|
| 47 | `SecondSeatFoliation` | `leaf_K` | 60 | 35–100 | **70** | in | in |
| 102 | `SecondSeatFoliation` | `leaf_shear` | 45 | 25–80 | **41** | in | **under**, as predicted |
| 94 | `SecondSeatFoliation` | `leaf_umbilic_iff` | 50 | 25–90 | **36** | in | **under**, as predicted |
| 48 | `SecondSeatStatic` | `static_Gtt_Grr` | 120 | 80–170 | **125** | in | in |
| 49 | `SecondSeatStatic` | `static_AeqF`, `static_density` | 90 | 55–140 | **60** | in | in, at the floor |
| 51 | `SecondSeatStatic` | `static_tov` | 50 | 25–90 | **33** | in | **under**, as predicted |
| 54 | `SecondSeatKS` | `ks_stress` | 110 | 70–170 | **108** | in | in |
| 13 | `SecondSeatLTB` | `ltb_Gtt`, `ltb_bend` | 220 | 150–300, stop 350 | **246** | in, under the stop | **over**, as predicted |

- **Mean of the eight: 89.9**, against my predicted 93 and 71's measured 90.3.
- **Without the three reuse rows and row 13: 90.8**, against a predicted 95.
- **Measured over central** runs from 0.66 (51) to 1.17 (47).
  - The two largest misses are both LOW, and both are rows that reuse an earlier instance: 49 at 0.67 and 51 at 0.66.
  - **The reuse saved more than I priced.**

## My probabilities, scored

| quantity | p | outcome |
|---|---|---|
| all seven of 47, 102, 94, 48, 49, 51, 54 land | 0.75 | **yes** |
| row 13 lands under the stop | 0.5 | **yes**, at 246 |
| the interface suffices for the seven without opening a proof body | 0.85 | **yes**, for all eight |
| ≥ 5 of the 8 inside their own bands | 0.6 | **8 of 8** |
| `curvD_eq` plus the recipe close a component goal with `field_simp`/`ring` on the first instance that tries it (48) | 0.6 | **yes**: 48's two Einstein components closed first time, and the only failing step in that build was a `sin²` helper |

⚠ **On the decisive fraction:** at my own centrals the eight bands had a 0.11–0.39 chance each of failing (σ = 0.4).
**None failed.** So this is consistent with the centrals and does not test them hard. For 71's band, the
four-in/four-out split was the prediction, and it came out exactly. **That is the reading with content: on these
rows the band is a property of the row type, not of the seat.**
- Reuse rows land under it.
- A row needing a new recipe lands over it.

## What each instance asserts, and how it compares with its receipt

- **47, 102, 94** are stated on `lcConn` itself: `nablaL` is THE connection applied to constant fields.
  - `lcConn_const` takes it to `lcGam`, and `lcGam_diag4` takes that to `gamD`.
  - The receipts **hand-wrote** `K` (94 and 102). Here it is derived.
  - **94 is an iff:** the leaf on SdS-α is umbilic iff `r = 3M`.
- **48, 49, 51:** the Einstein components are derived through `curvD_eq`.
  - Row 51's TOV step uses row 48's DERIVED `G^r_r`. The receipt used a hand-written one; this closes that gap.
- **54:** `P09_ks_vacuum` **assumes** the three stress-energy combinations. **Here they are derived** for free
  `X(τ), Y(τ)`.
- **13:** the constraint and its `r`-derivative enter as hypotheses AT THE POINT.
  - That is the receipt's own substitution, stated as an assumption rather than as a surface.
  - On the way, `ltb_Gtt` gives `G_tt` of `−dt² + Q dr² + W dΩ²` in closed form for two-variable `Q` and `W`.
    **No second partial of `Q` survives in it.**

## The interface's first use by a second seat (`r7333` ①: "this is the interface's first use by anyone but its author")

- ✔ **No proof body of `ShadowEngine` was opened.** I read statements only:
  - `curvD_eq`, `lcGam_diag4`, `lcConn_const`, `gamD`, `DGD`, `curvD`;
  - `einsteinC`, `ricC`, `scalC`;
  - `co_d1`, `co_d2`, `pr_d1`, `pr_d2`, `fd_coord_i`, `d2_of`.
- ⛔ **The one gap, named in the registration before any Lean: two-variable profiles.**
  - Row 13's `R(t, r)` is neither one-coordinate nor a product, so I wrote the recipe: `tv_d1`/`tv_d2` for
    `y ↦ h(y⁰, y¹)` and `tvp_d1`/`tvp_d2` for its product with an angular profile.
  - It takes `100` lines and is built from `d2_of`, `fd_coord_i` and Mathlib's symmetric second derivative.
  - **It lives in my instance file. It is offered to `ShadowEngine` rather than moved there**, because that file is
    71's.
- ⌗ **Three frictions,** each small, each a line for `SEAT_BRIEF.md`:
  1. **`simp` unfolds the coefficient definition before a partial-derivative fact stated on it can fire.** State each
     fact on the unfolded function (`fderiv ℝ (fun y => P (y 1)) p v = …`), as row 45's `show` lines do implicitly.
  2. **`cT` is already a global name in `ShadowEngine`** (`lcGam_T (cT q)`), so an instance's own `cT` fails to
     declare. I renamed mine to `cLT`.
  3. **This Mathlib pin has no `HasFDerivAt.div`/`.inv` for a scalar field on `ℝ × ℝ`.** Use `hasDerivAt_inv` composed
     through `comp_hasFDerivAt`.
- **Build cost:**
  - `lake build ShadowEngine`: **112 s** here, against 71's 2 m 12 s;
  - each instance file: **6–17 s**;
  - the Mathlib cache: 176 s;
  - **the whole campaign, registration push to last landing: 21 minutes of wall clock** (18:47 to 19:08 UTC).

## Not done

- No Kretschmann row is touched.
- No engine proof body was read.
- **No π_d:** nothing here has a second reading.
- The applier machinery stays stopped.
- `CANDIDATES.md` and `ROWS.tsv` are 71's and are not edited. **The eight rows' status change is routed, not
  written.**
