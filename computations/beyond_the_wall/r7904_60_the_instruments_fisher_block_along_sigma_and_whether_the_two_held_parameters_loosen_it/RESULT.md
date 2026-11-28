# r7904 (60) — THE INSTRUMENT IS NOT LOCALLY DEGENERATE ALONG Σ, AND ITS WEAK LIMIT IS NOT THE CURVATURE AT THE ORIGIN

Order `r7903` (69) item ①. Registered in `PREDICTION.md` and pushed before the first entry existed.

**Outcome `Ⓕ⓸ᵇ + Ⓓ⓷`.** Neither named correlation clears the registered `0.90`; the baryon density's
sits in `[0.50, 0.90)`; the degradation factor is intermediate.

## The block

The `A`-marginalised Fisher block of `model3.Model3('lcdm')` — the scorer every limit on this line is
read on — over five parameters at `Σ = 0`, at the control's own point from `r7888`'s record
(`H0 = 68.64772`, `Ω_m = 0.3148204`, `ω_b = 0.0223999`, `n_s = 0.96483686`, `χ²_cmb = 538.2666`), on
the instrument's **555 bins** across all three blocks.

| | Σ | H0 | Ω_m | ω_b | n_s |
|---|---|---|---|---|---|
| **Σ** | `1.0000` | `+0.318326` | `−0.1555` | `+0.5117` | `+0.4856` |
| **H0** | `+0.318326` | `1.0000` | `−0.9115` | `+0.63967` | `+0.359034` |
| **Ω_m** | `−0.1555` | `−0.9115` | `1.0000` | `−0.3181` | `−0.31483` |
| **ω_b** | `+0.5117` | `+0.63967` | `−0.3181` | `1.0000` | `+0.2765` |
| **n_s** | `+0.4856` | `+0.359034` | `−0.31483` | `+0.2765` | `1.0000` |

Marginalised `1σ`: `Σ` `0.0545938` eV, `H0` `0.381602`, `Ω_m` `3.07123e-05`, `ω_b` `1.145475e-07`,
`n_s` `7.84997e-05`.

## The three things it says

**① THE STRONG EXPECTATION IS REFUTED, and narrowly.** `PREDICTION.md` put STRONG grounds on
`abs(ρ(Σ, n_s)) > abs(ρ(Σ, ω_b))`, from `r7896`'s finding that the cross-block interference the four
parameters absorb is the tilt's alone. The block reads the other way: `ω_b` at `+0.5117` against
`n_s` at `+0.4856`. The gap is `0.0261`, and it **survives the change of route** — the control route
orders them the same way with a gap of `0.022763`, against a route-to-route disagreement of `0.01475`
on those two entries. ⌗ *`r7896` licensed an ORDERING and the ordering did not hold. The two objects
are not the same object: a share of a non-additivity residual over a thirty-six-bin subset on a held
clock is not a local correlation of the full 555-bin block, and the registration said so in advance.*

**② NEITHER IS A DEGENERACY, and the block's real degeneracy is somewhere else.** Both named
correlations sit near `0.5`. The strongest entry in the whole block is `H0`–`Ω_m` at `−0.9115`, which
is not one of the two parameters the reference holds. Fixing `ω_b` and `n_s` tightens `σ(Σ)` from
`0.0545938` to `0.0426369` eV, a degradation factor of **`R = 1.280436`** — intermediate, and nowhere
near the `2.0` that would make the two parameters a material source of the instrument's freedom
along `Σ`.

**③ UNREGISTERED — AND ⛔ WITHDRAWN AT `r7908`, WHICH MEASURED IT AS A COMPARISON OF TWO
LIKELIHOODS.** The arithmetic below is right and is kept; the sentence it was read as is not. Read at
the time as *the instrument's weak limit is not the curvature at the origin*, on the registered block
against `r7888`'s own banked figures at that record's own `Δχ² = 2.71`:

| | meV |
|---|---|
| `σ(Σ)` from the block at `Σ = 0` | `54.5938` |
| a Gaussian half-width at `Δχ² = 2.71` | `89.8727544` |
| the profile's minimum, same record | `60.0000` |
| minimum + half-width | `149.8727544` |
| the profile's **own** crossing | `193.5453` |

The local reading falls `43.67255` meV short, a factor of `1.2914`.

⛔ **WHAT THAT SHORTFALL IS, ESTABLISHED AT `r7908`:** the two numbers belong to two different
likelihoods. This block is `chi2_cmb` — `555` CMB bandpowers, five parameters. `r7888`'s crossing is
read on `Model6.chi2`, which is the same CMB score **plus a BAO term plus a lensing likelihood plus a
tau prior**, over **six** parameters. `r7908` read the profile's own curvature from the profile's own
`Δχ²` values and found it puts the crossing in `[185.0880, 194.0674]` meV across three fits, against
an actual `193.5453`. ⇒ *The profile IS accounted for by its own curvature, there is no shortfall to
explain, and the reading in this section is withdrawn — the arithmetic was right and the object was
not.* ⌗ *That is the many-to-one-label guard: which likelihood each quantity belonged to had to be
established before the two were compared, and here it was not.*

## Three defects in this revision's own registration, reported rather than worked around

1. ⛔ **`Ⓒ⓷`'s conditioning bar is UNIT-DEPENDENT, so it is degenerate.** `PREDICTION.md` asks for the
   block in physical units and puts a bar of `1e12` on its condition number. That number is not
   invariant under a change of each parameter's unit, while every correlation and every ratio of
   sigmas is: the same block reads `6.807e13` in physical units and `140.056` scaled to a unit
   diagonal. A pass or a fail on it would be a fact about the units. **Reported degenerate**, both
   numbers printed, and the thing the criterion existed for measured directly instead and said to be
   unregistered: perturbed at a relative `1e-10` over two hundred draws the correlations move by
   `4.39e-09` and `R` by `5.21e-10`.
2. ⛔ **`Ⓒ⓵`'s step sizes were too coarse by about a hundred.** At the registered `(0.005, 0.01)` the
   control route reads `ρ(Σ, ω_b) = +0.2776` against the Fisher's `+0.5117`. The whole gap is
   truncation and it drains monotonically: the ladder settles by `2e-04` and the two finest rungs
   agree to `3.343e-05`. **The ladder is shown rather than a step asserted.**
3. ⛔ **`Ⓒ⓵` AS REGISTERED FAILS, and the bar was wrong rather than the measurement.** At the plateau
   the two routes still disagree by `0.0610` somewhere in the matrix — on `(Ω_m, ω_b)`. The
   registration treated the **Fisher matrix** and the **observed Hessian** as one object; they differ
   by the residual-curvature term the Fisher drops, which is a real difference between two real
   objects. On the loci the verdict rests on they agree inside the registered bars: the two named
   correlations to `0.01475` against `0.02`, and `R` to `0.94` per cent against `5`.
4. ⛭ **And one unregistered check of mine was mis-scoped on first writing.** `Ⓒ⓹` first compared the
   ordering of two correlations against the two routes' WORST disagreement anywhere in the matrix —
   a disagreement about a pair the ordering does not involve. An identification has to be checked on
   the loci the object itself distinguishes, so it is checked on those two entries, and the first
   form is stated so the repair can be judged.

## What is not claimed

- **Nothing about the reference.** `cc66`'s block on the same mask (its `⑲ ②`) has not landed. Every
  sentence comparing the two pipelines' stiffness is **named as waiting**, not written as a result.
- **No mechanism, and no limit.** A correlation is not a mechanism. `r7888`'s `193.545` meV is
  untouched and no crossing is read here.
- **This is the instrument AS USED, not the raw solve.** The block is read off `Model3`'s quadratic
  Taylor model with a cubic spline in `Σ`, which is the object every limit on this line is read on,
  and it inherits that interpolant's error.
- ⚠ **`Σ = 0` is a boundary.** Every `Σ` derivative is the RIGHT derivative; a two-sided block is not
  available from this model and was not attempted.
- **`Ⓕ⓸ᵇ` is a null on the registered question and not a null on 69's reading.** A small `R` locates
  the degeneracy away from the origin's curvature; it does not refute it.
