# r7850 (node 60) — RESULT

*Ordered by `r7847` (69). Registered at `PREDICTION.md`, committed and pushed at `77f16be96` before
a line of the computation existed, with eleven arms.*

## The shape of the result

**The order asked for one thing and the measurement says it is the wrong thing — and then an
independent pipeline, found installed in this container, says where the real fault is.**

- **Item ① cannot be delivered as asked.** The instrument already carries `Φ` through the radiation
  era and through equality; what the late carry threw away was the instrument's own solve. Carrying
  from *inside* the radiation era, which is what the order asked for, is measurably **worse**, and
  the error is of order the radiation-to-matter ratio at the handover.
- **Item ②'s two halves are in direct opposition**, with numbers on both sides: recovering the
  missing suppression needs an early handover, and an early handover costs the radiation share.
- **Item ③ is delivered and the decisive arm fails** — but the limit improves by `10.981` meV and
  the effective mass closes `0.88` of the `3.65` standard errors it was out by.
- ⛔ **And `camb 2.0.4` is installed here, where `FOR_66` says it will not install.** It fits the
  nine bandpowers with **nothing fitted** at `χ² = 8.8173` on nine bins. **So the `χ²/dof ≈ 2` this
  line has been attributing to its carry is the instrument's lensing potential disagreeing with an
  independent one by up to `28` per cent in shape at fixed cosmology.**

## ① Where the carry belongs — the opposite of what was ordered

**Ⓐ① FAILS on the full band, with its criterion exactly as registered.** The closed test carries
`Φ(k)` from a handover to a later time the instrument also covers and compares with the instrument's
own `Φ(k)` there. Registered: a spread below `0.023`, one tenth of the `0.2276` the matter-only carry
scored. Measured, at five handover/judge combinations: `0.3206` to `0.6295`.

**The cause is isolated rather than guessed, and there are two.**

| handover | `z` | radiation/matter | full-band spread | on the modes the identity covers |
|---|---|---|---|---|
| `500` | `482.20` | `0.1401` | `0.6295` | `0.0986` |
| `914` | `188.06` | `0.0548` | `0.4912` | `0.0615` |
| `1400` | `91.51` | `0.0268` | `0.3206` | `0.0239` |
| `1893` | `53.55` | `0.0158` | `0.4877` | `0.0264` |
| `4000` | `12.83` | `0.0040` | `0.3651` | `0.0224` |

- **The test's own identity does not range over the band.** `Φ(a₂)/Φ(a₁) = [δ/a₂]/[δ/a₁]` is the
  Poisson relation, which is sub-horizon. It holds to one per cent on `16`–`23` of `40` modes and
  only above `kη ≈ 19`–`33`. At the lowest `k` its residual is `0.94`–`0.998`, so the identity is
  wrong by a factor two there and says nothing. **More than half of Ⓐ①'s full-band spread comes from
  modes where Ⓐ①'s own comparison is invalid.**
- **The restricted residual floors at the radiation share.** At the handover the production path
  uses, tightening the admission threshold takes the spread `0.0224 → 0.0124 → 0.00514 → 0.00378`,
  where it stops — and `0.00378` is the radiation-to-matter ratio `0.00401` to within six per cent.
  **So the carry's own error is first order in the one thing the growth equation omits: the
  radiation perturbations' contribution to the source.**

⇒ **The handover belongs as LATE as the instrument can afford.** `r7848` had it in the right place
for a reason `r7848` did not know, and the order's premise is refuted precisely rather than vaguely.

⌗ **A repair written here is provably not one.** The baryons have not caught up at any handover —
`δ_b/δ_c` is `1.0000` at `k = 2e-4` and `0.0101` at `k = 1` at `z = 482`, and negative later — so
carrying the two clustering species separately looked necessary. It changes nothing: both obey the
same equation with the same source, so their weighted sum obeys it too, with the weighted sum of
their initial conditions. **The two carries agree to `1.672e-12` across five configurations.** The
guard walked into is this seat's own: when a fork names two objects, check that the thing they are
alternatives for has a slot for only one.

## ② The two symptoms, and they pull against each other

**Ⓓ④ FAILS.** At `f_nu = 0.0225069`, which is `r7848`'s value exactly:

| | suppression of the power | of the textbook `−8 f_ν` |
|---|---|---|
| `r7848`, growth from the quadrature | `−0.053298` | `0.296012` |
| `r7850`, growth from the instrument | `−0.053012` | `0.294419` |

Registered: **at least `0.667`.** Measured: `0.294419`, a `−0.54` per cent move *away* from the
textbook. **The initial-condition repair does essentially nothing for the missing suppression**,
because the missing suppression is about the interval not covered and the initial conditions do not
change the interval. Recovering it needs an early handover, which Ⓐ① has just priced.

**Ⓒ③ FAILS on its `χ²` half.** Registered: both the `χ²` per degree of freedom and the drift fall.

| | `χ²` on 8 dof | per dof |
|---|---|---|
| growth from the quadrature | `16.389450` | `2.048681` |
| growth from the instrument | `17.049457` | `2.131182` |

⌗ **The quadrature reading reproduces `r7848`'s to every digit** — `16.389450` against
`16.389449912869935` — which is the closure that says this pipeline is wired to `r7848`'s and the
difference is the repair rather than the plumbing.

⌗ **Ⓒ③'s drift half cannot be compared, and that is a defect in `r7848`'s record that this seat
owns.** Its `+49.8` per cent figure lives only in a JSON; the code that computed it was not kept, so
the definition is unrecoverable. My own drift, by a definition the file states, is `−20.65` per cent
with the quadrature's initial conditions and `−21.32` with the instrument's — **a different quantity,
and not a refutation of r7848's.**

**Ⓔ⑤ HOLDS, and it is the revision's one clear win.** The held prediction comes from the CMB fit and
does not depend on the growth; only what the bandpowers prefer can move.

| | preferred | ratio to the held `1.617967e-09` | miss |
|---|---|---|---|
| `r7848` | `1.471643e-09` | `0.909563` | `9.04` per cent |
| `r7850` | `1.576671e-09` | `0.974476` | `2.55` per cent |

## ③ The control, first, with its Monte-Carlo errors

**Ⓕ⑥ FAILS both halves.** The criterion as registered: a limit inside `42.8`–`96.3` meV **and** a
negative effective mass.

| | limit (meV) | effective mass (meV) | above the ceiling | from `−101` |
|---|---|---|---|---|
| `r7848` | `111.383 ± 0.409` | `+44.253 ± 39.792` | `36.91σ` | `3.650σ` |
| **`r7850`** | **`100.402 ± 0.353`** | **`+21.913 ± 44.423`** | **`11.61σ`** | **`2.767σ`** |

The limit improves by `10.981` meV (`9.86` per cent) and the distance above the order's own ceiling
falls from `36.91` standard errors to `11.61`. `χ²` at the minimum falls from `576.0427` to
`570.3427`. Below `59` meV: `70.5125` per cent, from `60.6444`. Below `64`: `75.2014`, from
`65.9875`.

⚠ **And this seat's registered expectation splits, reported as a split.** It said: FAIL, with a limit
between `70` and `110` meV and a **negative** effective mass. The failure is right. The limit's
window is right — `100.402` sits inside it. **The sign is wrong.** Two of three, and the third is
the half that matters most, so the expectation is not claimed as vindicated.

**Ⓘ⑨ HOLDS.** Six chains, worst split `R̂` `1.000101` against `1.05`, smallest effective sample size
`44608` against `1000`, acceptance `0.2440` and `0.2383`, the six chains' limits spanning `1.088`
meV — and the per-direction guard has nothing to catch: the unbounded minimum is **not** on a bound
and the curvature probe returns a real width in every direction.

**Ⓗ⑧ is NOT JUDGED**, as registered conditional on Ⓕ⑥. So the arm of record's sixteen grid points are
**not run** — three hours not spent, which is the whole reason the order's *control first* was taken
literally. **`P15` is untouched** and `72`'s batch waits.

## ⛔ Ⓖ⑦ — the reference was already here, and it moves the fault

`cc66`'s ordered decomposition has not landed; there is no `cc66` revision above `r7843`. The arm
says that in that case the receipt says so and infers nothing from the silence. **But `FOR_66` states
repeatedly that `camb 2.0.4` will not install in this container, and it is installed** —
`camb.__version__ == '2.0.4'`, and it runs. **That is the third consecutive revision on this line in
which a stated absence turned out false on probing:** `r7844` found the lensing bandpowers banked,
`r7848` found ACT DR6 banked, this finds the reference pipeline installed.

CAMB at the control's own cosmology, with `A_s = 2.1e-9` stated as a parameter:

| | `χ²` | per dof | amplitude |
|---|---|---|---|
| nothing fitted | `8.8173` on 9 bins | `0.9797` per bin | — |
| one amplitude fitted | `8.8074` on 8 dof | `1.1009` | `1.002494` |

Every bin within `1.34` of its own error. Against this instrument at the same cosmology and zero
sum: `χ² 16.3894` with the quadrature's initial conditions and `17.0507` with the instrument's, and
a shape disagreement with CAMB of `−14.3` to `+27.2` per cent and `−14.6` to `+28.0` respectively.

⇒ **The nine bandpowers are not hard to fit.** An independent pipeline fits them with no amplitude
freedom at about one per degree of freedom, and the amplitude it would choose is `1.0025`. **So this
instrument's `χ²/dof` of `2.05` and its normalisation miss are the instrument's, not the data's — and
the repair moves its shape slightly away from CAMB rather than toward it.**

⇒ **That refutes the premise the whole repair programme rests on, this revision's own included.** The
lensing half of the control does not fail because the carry starts in the wrong place, nor because
its initial conditions came from a closed form, nor because of the radiation era. It fails because
this instrument's lensing potential disagrees with an independent one by up to `28` per cent in
shape at fixed cosmology.

⌗ **The convention is settled empirically rather than assumed.** `get_lens_potential_cls` binned
straight through the nine windows lands at `0.84`–`1.13` of the data. A missing or extra factor of
`[L(L+1)]²/(2π)` would put that out by nine orders of magnitude and a single missing factor of `L`
by `28`–`377`. It is neither.

## Ⓙ⑩ The cost, recorded — and `r7848`'s record corrected

Re-measured at the production mode count, with every switch printed beside the number:

| `ETAREF` | `z` | seconds, 220 modes |
|---|---|---|
| `914` | `188.06` | `40.8` |
| `4000` | `12.83` | `667.0` |

`r7848` recorded `40.38` s and **did not record its `ETAREF`**, while its own script takes `ETAREF`
from the environment with no default. The closest carry measured here is `914` — a factor `1.011`
away. ⇒ **The record was taken at the carry that same revision then reversed, and it understates the
carry it actually landed on by a factor `16.5`.** The per-parameter-point figure of `93.1` s is
really about `720`.

And a fact worth having for its own sake: **the cost is essentially independent of the mode count** —
five wavenumbers to `η = 1000` cost `40.4` s and `220` to `η = 914` cost `40.8` — because the system
is vectorised over `k` and the step count dominates. The expensive axis is the END TIME. That is why
running the instrument to today is out of reach (`1095.7` s to `η = 6000` for five modes, and
`η₀ = 14145` **unmeasured**, stopped at a limit and not extrapolated), and why one solve now serves
both the growth and the Limber shape.

## What is NOT claimed

- **Nothing about the neutrino mass on either arm.** Ⓕ⑥ failed, so Ⓗ⑧ is not judged — the same ruling
  `r7838`, `r7844` and `r7848` made.
- **`P15` is not touched**, as `r7847` requires.
- **No claim that CAMB is right and this instrument wrong in general.** What is measured is that at
  one cosmology, on these nine bandpowers, CAMB fits with nothing fitted and this instrument does
  not. Which of the two is wrong about the lensing potential is not settled here.
- **No claim that the instrument could not be run to today** — only that it cannot be run there
  cheaply, with the cost stated and the last point unmeasured rather than extrapolated.

## ⌗ Five figures restated in two revisions, all for one reason

The absolute normalisation read `1.3` per cent instead of `9.0` for want of `e^{+2τ}`. Two seats'
Fisher matrices read `1.000e+00` instead of `1.9e-17` for want of a denominator. The cost read `40` s
instead of `667` for want of the `ETAREF` it was taken at. The asymptote read a small improvement
instead of a small regression because the two sides were at different sums. A restricted spread read
`0.0224` instead of `0.00378` because an admission threshold was leaking.

⇒ **GUARD, now earned five times: a comparison between two numbers is not a measurement until the
switches on both sides are read and shown equal, and the cheapest place to show that is in the record
itself.** Every record this revision writes is keyed by its own configuration, and the registered one
was twice rescued from being silently overwritten by exactly the mechanism this guard names.
