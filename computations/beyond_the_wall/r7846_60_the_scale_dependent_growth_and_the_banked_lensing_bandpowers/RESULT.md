# r7846 (node 60) — RESULT

*Ordered by `r7845` (69). Registered at `PREDICTION.md`, committed and pushed at `0859200f7`
before a line of the computation existed, with eleven arms. It lands as **r7848**, because the
trunk's front advanced to 69's own `r7845` while this was running and this line's next id of its own
parity above the front is `r7848`. Same work, same registration.*

## The shape of the result

**Three registered arms fail, and each failure is the informative half of the revision.**

- **Ⓐ① fails** at `5.276e-03` against a registered `1e-10`, and the cause is isolated rather than
  guessed: the thing compared against is wrong, not the new solver.
- **Ⓖ⑦ fails BOTH halves.** The control's limit got *looser* when the lensing term was added —
  `111.38 ± 0.41` meV against `99.67 ± 0.55` without it — and its effective mass came back
  `+44.3 ± 39.8` meV, the wrong sign, where temperature-plus-polarisation alone gave `−7.0 ± 50.9`,
  which is the published sign. The limit sits **`36.91` standard errors above the order's own
  ceiling of `96.3` meV** and `52.33` above the ceiling of this seat's separately registered
  expectation of `50`–`90` meV. **My expectation was PASS, and it is refuted.**
- **Ⓗ⑧, the arm of record, is therefore NOT JUDGED** — it was registered as conditional on Ⓖ⑦, and
  `r7838` and `r7844` both ruled the same way. Its chain was run only for the `59`/`64` meV
  placement the order asks for either way. **`P15` is not touched.**

## ① The scale-dependent growth

The two-fluid growth equation on this instrument's own rate, in `N = ln a`:

```
d²δ_cb/dN² + (2 + dlnH/dN) dδ_cb/dN = 1.5 Ω_tot(a) [ (1−f_ν) δ_cb + f_ν δ_ν ]
```

with `δ_ν = δ_cb / (1 + (k/k_fs)²)` and `k_fs(a) = √(3/2)·a·H(a)/v_th(a)`. **The filter is the one
approximation and it is named in the module's docstring**: both limits are right by construction and
the interpolation between them is not a Boltzmann solution. `f_nu = 0.0225069` at the control's sum.

**Ⓑ② holds.** The suppression at `a = 1` is monotone non-increasing in `k` across the whole band,
from `−1.790e-06` at `k = 1e-4` to `−0.026649` at `k = 1` /Mpc.

**Ⓐ① fails, and the quadrature is the defect.** I registered that at `Sum = 0` the new growth must
reproduce `L171x`'s background quadrature to `1e-10` relative at every one of 25 scale factors and
40 wavenumbers. It reproduces it to `5.276e-03`. *Reported failed with the criterion exactly as
registered.* The gap is `1.110e-16` at the start — zero by construction, the solver being handed the
quadrature's own growing mode there — and grows monotonically to `z = 0` while the radiation share
falls to nothing, so it accumulates rather than being an offset. `isolate_against_matter_lambda`
then builds **both** the quadrature and the ODE on one pure matter + Λ rate: they agree to
`9.799e-09`, which is solver tolerance.

⇒ **The ODE is the growth equation.** `growth_over_a()` is the matter + Λ closed form evaluated on a
background that carries radiation, outside the validity its own docstring states, and its `D` is
wrong by about half a per cent by `z = 0`. That cancels in `r7844`'s ratios between sums and does
**not** cancel once bandpowers are scored with no fitted amplitude.

⌗ Ⓐ①'s `1e-10` is `r7844`'s mistake in a new place: not a tolerance finer than a Monte-Carlo error
but a tolerance finer than **the accuracy of the thing compared against.** I had assumed a closed
form was exact.

**Ⓒ③ is reported, not tested.** The high-`k` asymptote on the power is `−0.053298` against the
textbook `−8 f_nu = −0.180055`, a ratio of `0.296012`. Carried instead from the non-relativistic
transition at `z = 187.92` it is `−0.120083`, a ratio of `0.666922`. **So the ordered interval
carries `44.4` per cent of what the full post-non-relativistic one does, and even the longer one
reaches two thirds of the textbook figure rather than all of it** — the remainder is the filter
being an interpolation. Neither number is called agreement.

## The carry fork: decided, routed, and then REVERSED on measurement

The two rows above made `z = 188` look like the better start, and the φφ score agreed loudly:
`chi²/dof` `2.049` from the ordered `z = 12.8` against `1.071` from `z = 188`, with the monotone
drift cut from `+49.8` to `+19.6` per cent. I routed that fork to `66` with the recommendation to
move.

**`carry_validity.py` then reversed it, and the reversal is in the channel beside the original.**
The closed test asks whether a matter-only growth equation links the two start times at all: carry
`Φ(k)` from `z = 188` to `z = 12.8` with this instrument's own growth and compare with the
instrument's own `Φ(k)` there. **The ratio is k-dependent** — `0.9638` at the largest scales,
`0.7362` at the smallest, median `0.7807` — which is sub-horizon `Φ` decay through the residual
radiation era, `5.47` per cent of matter at `z = 188` against `0.39` per cent at `z = 12.8`.

⇒ The better `χ²` at `z = 188` was **a truncation error partly cancelled by a growth error**, not a
better model. **The ordered carry at `z = 12.8` is correct, `r7845` was right, and the grid was
built on it.** The `44.4` per cent of missing suppression and the `2.05` of shape error are both
real and neither is fixed by moving the start: that needs `Φ` carried through the radiation era,
which is a larger instrument change than this order asks for.

⌗ The superseded reading is left standing in `phiphi_carry_compare.json` with its measurements
intact and its conclusion marked superseded, so that the reversal is visible rather than tidied
away.

## ② The nine banked bandpowers, scored with no fitted amplitude

**The convention was read off node 70's own scoring code, not assumed.** `like.py` computes
`PPm = pp[:,0] * (L(L+1))² / (2π)`, so the banked bandpowers are `[L(L+1)]² C_L^φφ / (2π)` and not
raw `C_L^φφ`. Binning raw `C_L^φφ` against them gave a drift of 188,000 per cent rising with `L`,
which is how the convention came to be checked.

**The absolute normalisation is a prediction here, and it was confirmed.** Every mode starts at
`Φ = −1`, so `CMB = AMP·e^{−2τ}·shape_cmb` while `φφ = AMP·shape_φφ`: the CMB fit fixes
`AMP·e^{−2τ}`, and the lensing prediction is that number times `e^{+2τ}/T_CMB²`. Held:
`1.617967e-09`. The bandpowers' own preference: `1.471643e-09`. **Ratio `0.909563` — the prediction
is high by nine per cent, with nothing fitted.**

⌗ Dropping the `e^{+2τ}` makes the same comparison look like `1.3` per cent, and that comparison is
wrong: the reionisation suppression is in the CMB amplitude and not in the matter potential. **The
agreement this revision claims is nine per cent, not one.**

**The shape systematic is characterised and the term is informative anyway.** At the ordered carry
`χ²` is `16.389` on `8` degrees of freedom, `2.049` per degree of freedom, with a monotone `+49.8`
per cent drift. Against that, moving the sum across the grid moves `χ²_lens` by `94.497` — the
minimum sitting near `Σ = +0.15` eV — so the sum's signal is five to six times the systematic and
the term carries information. `32` of `32` grid points are banked on the ordered carry.

**Ⓔ⑤ holds.** τ's reach goes from `1.137e-12` without the lensing term to `355.161` with it, a ratio
of `3.124e+14`. Lensing alone prefers `τ = +0.0065`, a `6.79σ` pull against the `0.054 ± 0.007`
prior, **recorded as confounded with the sum and with the shape systematic rather than as a
measurement of τ.** The prior is named for what it is: 70's stand-in for the low-ℓ likelihood.

## ③ The control first — and it fails

| | limit (meV) | effective mass (meV) |
|---|---|---|
| `r7838`, temperature only | `277.7` | `+67.5` |
| `r7844`, with polarisation | `99.67 ± 0.55` | `−7.0 ± 50.9` |
| **this revision, with lensing and τ** | **`111.38 ± 0.41`** | **`+44.3 ± 39.8`** |
| published | `64.2` | `−101` |

`R̂ ≤ 1.0001` on every parameter, `ESS ≥ 46369`, acceptance `0.231` and `0.232`. **The chains are
healthy; the answer is wrong.** Adding information made the limit looser and flipped the effective
mass back to the wrong sign. Below `59` meV: `60.64` per cent. Below `64` meV: `65.99` per cent.

## Ⓘ⑨ ACT DR6 CMB-only: banked, measured, NOT added

**The data was already in the harness** — `computations/planck_tt_likelihood/data/act_dr6_cmbonly/`,
banked at `r7815+70.1`: 45 foreground-marginalised bandpowers each in TT, TE and EE over
`ell 600.5`–`6125.5`, the full `135 × 135` covariance, windows on `ell 2`–`8501`. **That is the
second consecutive revision in which an order offered data conditionally and the data was already
banked;** `r7844`'s Ⓗ⑧ found the lensing bandpowers the same way.

Ⓖ⑦ failed, so Ⓘ⑨ requires the question measured before the data is added. Measured:

1. **The tightening required.** Shrinking the control's own posterior about its own centre, the 95
   per cent limit reaches `64.2` meV at `f = 3.2738` — a width of `12.155` meV — so an independent
   dataset would have to deliver `12.765` meV on its own. The rescaling reproduces the chain's own
   limit at `f = 1` to `1.24` per cent empirically and `0.93` per cent in closed form.
2. **What ACT could contribute, as an UPPER BOUND.** `84` of its `135` bandpowers lie wholly inside
   this instrument's reach (`ell 600.5`–`1950.5`); the other `51` carry weight past `ell 1996` and
   are dropped, which costs nothing illegitimate because a sub-vector of a Gaussian has the
   sub-block as its own covariance. On those `84`, a marginalised Fisher built from this
   instrument's own spectra gives `σ(Σ) = 104.1` meV with the amplitude shared with Planck and
   `106.3` meV with it free. **Combined with the control it buys `3.56` meV of the `47.18` meV
   remainder: seven and a half per cent.**
   ⌗ Every choice in that bound is generous to ACT, so the shortfall is robust: its calibration and
   polarisation-efficiency nuisances are left unmarginalised because they are not banked
   (`DR6-ACT-lite` is refused from this container), and it is treated as independent of Planck
   although its footprint is inside Planck's sky **and** the kept bandpowers sit inside the band
   Planck already scores here. Both amplitude treatments are reported rather than one pinned.
3. **Which remainder is at issue.** Shrinking a width moves a limit and leaves a centre exactly
   where it is. At the `f` that would close the limit, the effective mass goes from `3.65` to
   `11.95` standard errors from the published value. **The operation that would mend one half of Ⓖ⑦
   makes the other half worse.**

⇒ **DO NOT ADD, with the control's figure as the reason.** The reachable negative was a bound
comfortably below the required width, and it was not met.

⌗ And the measurement says something the order did not ask: **the control's shortfall is not a
precision deficit.** More of the same observable cannot move a central value, and this harness's
central value is on the wrong side of the published one.

## Ⓙ⑩ The sampler's guards — and a guard that passed what it was built to catch

The control satisfies every registered guard: six chains, split `R̂ ≤ 1.0001` against a threshold of
`1.05`, `ESS ≥ 46369` against `1000`, kept-chain acceptance `0.231` and `0.232` inside `0.03`–`0.70`.

**But the arm of record's first attempt exposed a hole in `r7844`'s own repair.** Its unbounded
minimum sits at `Σ = −0.1200` eV, **exactly the model's lower bound**, so the curvature probe hits
the bound at once, its step returns at the floor, and the sum's proposal width came back `1.08e-08`
eV — the chain could not move in the one direction the limit is read off. `r7844`'s refusal guard
did not catch it, **because it tests the AGGREGATE acceptance and the other five directions were
moving at `0.303`.**

The run was stopped rather than left to produce a number. Two repairs: `laplace_cov` now records
which directions' curvature could not be measured, gives those a **stated** fallback width instead
of the curvature's and announces each swap; and the kept chain is checked **per direction**, with a
frozen direction refused by name.

⌗ That is the second time in two revisions that a guard I wrote passed something it was built to
catch, and both times for the same reason: **the guard tested a summary of the thing rather than the
thing.** `r7844`'s Ⓒ③ asserted a definition instead of the code that ran; this one asserted an
average instead of the direction the result is read off.

⌗ And the boundary is itself a finding. The arm's joint fit wants the sum pressed against the floor
of the grid at `−0.12` eV, so whatever limit it yields is set by where the grid stops rather than by
the data — which is one more reason Ⓗ⑧ stays NOT JUDGED.
