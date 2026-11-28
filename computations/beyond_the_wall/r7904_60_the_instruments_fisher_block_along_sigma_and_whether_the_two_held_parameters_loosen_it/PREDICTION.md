# r7904 (60) — REGISTER BEFORE THE BLOCK IS READ: is the instrument LOCALLY degenerate between Σ and the two parameters the reference holds?

Order `r7903` (69) item ①. **Nothing below is measured. This file is committed and pushed before the
first Fisher entry exists.**

## What is being read, stated so it cannot be moved afterwards

The **instrument's Fisher block over five parameters** — `Σ`, `H0`, `Ω_m`, `ω_b`, `n_s` — **at `Σ = 0`,
at the control's own point**, on the instrument's **555 bins**.

- **The object is the scorer that reads every limit on this line**, which is `model3.Model3('lcdm')`:
  a quadratic Taylor model of the binned 555-vector in the four parameter deviations, with a cubic
  spline in `Σ`. ⛔ *It is therefore the instrument AS USED, not the raw Boltzmann solve. A Fisher
  block read off the interpolant inherits the interpolant's error, and that is a limit on this
  reading which is stated here rather than discovered later.*
- **The point** is `x4 = r7888`'s banked `calibrated.x_at_node['0.0']`, first four entries, read out
  of that record and never typed. `Σ = 0` exactly.
- **The amplitude is marginalised, not held.** `chi2_cmb` profiles one closed-form amplitude `A`
  across all three blocks, so the registered block is the `A`-marginalised one: the projection
  `P = F − F m mᵀ F / (mᵀ F m)`, scaled by `A²`, contracted with the parameter derivatives.
- **Units: physical.** `Σ` in eV, `H0` in km/s/Mpc, `Ω_m` and `n_s` dimensionless, `ω_b = Ω_b h²`.
  The instrument's internal deviations are in units of `STEP = (2.0, 0.015, 0.0008, 0.02)` and are
  divided out, so the block's entries are comparable to the reference's entry for entry. ⌗ *The
  correlations are invariant under this rescaling; the entries are not, which is why it is done.*
- ⚠ **`Σ = 0` is a BOUNDARY of this model, not an interior point.** The direction splines are
  evaluated at `max(Σ, 0)`, so a central difference across zero crosses a kink. **Every `Σ`
  derivative here is the RIGHT derivative**, taken analytically from the splines on the physical
  side `Σ ≥ 0`. A two-sided reading of this block is not available and is not attempted.

## Two readings, and what each predicts

69's two candidate readings of the remaining factor of `3.3`:

- **THE INSTRUMENT IS DEGENERATE.** `Σ` can be traded against the tilt (and possibly the baryon
  density) in the instrument in a way the reference does not permit. Then the instrument's local
  block should show a LARGE `Σ`–`n_s` correlation, and fixing `ω_b` and `n_s` should materially
  tighten `σ(Σ)`.
- **THE REFERENCE IS STIFF.** The instrument's correlations are ordinary; the asymmetry is the
  reference's, and only `cc66`'s block on the same mask can say so.

## The registered quantities, with their bars

**ρ** is the correlation coefficient read from the INVERSE of the five-parameter block.
**R** is the degradation factor `σ_marg(Σ) / σ_cond(Σ | ω_b, n_s fixed)`: how much the two
parameters the reference holds loosen `Σ` locally, with `H0` and `Ω_m` marginalised in both.

| | outcome | criterion |
|---|---|---|
| `Ⓕ⓵` | degenerate in the TILT | `abs(ρ(Σ, n_s)) ≥ 0.90` **and** it is the largest of the four `abs(ρ(Σ, ·))` |
| `Ⓕ⓶` | degenerate in the BARYON DENSITY | `abs(ρ(Σ, ω_b)) ≥ 0.90` **and** it is the largest of the four |
| `Ⓕ⓷` | degenerate in BOTH | both `≥ 0.90` |
| `Ⓕ⓸` | NEITHER is large | both `< 0.90`; sub-case `ᵃ` both `< 0.50`, sub-case `ᵇ` at least one in `[0.50, 0.90)` |
| `Ⓕ⓹` | a THIRD direction dominates | the largest of the four `abs(ρ(Σ, ·))` is `H0` or `Ω_m` |

| | the degradation factor | criterion |
|---|---|---|
| `Ⓓ⓵` | the two parameters MATERIALLY loosen `Σ` | `R ≥ 2.0` |
| `Ⓓ⓶` | they do NOT | `R < 1.2` |
| `Ⓓ⓷` | intermediate | `1.2 ≤ R < 2.0`, reported as intermediate and **not** called a degeneracy |

⛭ **NON-EXCLUSIVITY, STATED IN ADVANCE.** `Ⓕ⓷` overlaps `Ⓕ⓵` and `Ⓕ⓶` by construction: if both
clear `0.90` the verdict is `Ⓕ⓷` and **both are named**. `Ⓕ⓹` can co-occur with `Ⓕ⓷` — a third
direction can be the largest while both named ones still clear their bar, and then both facts are
reported. `Ⓕ` and `Ⓓ` are independent readings of the same block and may disagree: a large `ρ` with
`R` near one is possible when the loosening is absorbed by `H0` or `Ω_m` instead, and if that is what
lands it is reported as that rather than resolved by preferring one.

## The expectation, with its grounds

- **STRONG grounds:** `abs(ρ(Σ, n_s)) > abs(ρ(Σ, ω_b))`. `r7896` measured, on this same instrument, that
  the cross-block interference the four parameters absorb is the TILT's and the tilt's alone.
- **WEAK grounds:** that either clears `0.90`. ⛔ *`r7896`'s object is a share of a non-additivity
  residual over a thirty-six-bin subset on a held clock. This object is a local correlation of the
  full 555-bin block at a point. **One label, two objects** — so `r7896` licenses an ORDERING and
  gives no information about where the ordering sits relative to an absolute bar.*
- **NO grounds either way** on `R`. The `320`-fold asymmetry `r7898` measured is a GLOBAL statement
  about a profile over `Σ ∈ [0, 0.6]` eV with the parameters re-profiled at every node; `R` is a
  LOCAL statement at one point. ⚠ **A small `R` does not refute the degeneracy reading** — it
  locates it away from the origin's curvature, in the profile's nonlinearity — **and a large `R`
  does not establish it against the reference**, which needs `cc66`'s block. Either way this
  revision reports the instrument's side and names the cross-pipeline verdict as waiting.

## The controls, registered as gates

- `Ⓒ⓵` **Two routes to the same block.** The registered primary is the derivative contraction with
  the `A` projection. The control is the finite-difference Hessian of `½ χ²` on `chi2_cmb` itself,
  which profiles `A` internally — a different code path to the same curvature. **Bar: every
  correlation the two routes report agrees to `0.02`, and `R` to `5` per cent.** The `Σ` row of the
  control uses second-order FORWARD differences, because of the boundary stated above.
- `Ⓒ⓶` **The point is the control's, not a nearby one.** `chi2_cmb(x4, 0)` at the point read from
  `r7888`'s record is reported, and the four physical parameters are printed.
- `Ⓒ⓷` **An ill-conditioned block is refused, not inverted.** If the five-parameter block's
  condition number exceeds `1e12` the correlations are NOT reported and the arm fails, because a
  correlation read from the reciprocal of rounding noise is a number with no referent.
- `Ⓒ⓸` **Signed.** Every correlation is reported with its sign; the bars are on magnitudes and the
  signs are printed beside them, because the DIRECTION of a trade is a fact about the mechanism.

## What this revision will NOT claim

- **No mechanism.** A correlation is not a mechanism, exactly as a block and a parameter are not.
- **No limit.** `r7888`'s `193.545` meV is untouched, and no crossing is read here.
- **Nothing about the reference.** `cc66`'s block (its `⑲ ②`) has not landed. Any sentence comparing
  the two pipelines' stiffness is **named as waiting** and not written as a result.
