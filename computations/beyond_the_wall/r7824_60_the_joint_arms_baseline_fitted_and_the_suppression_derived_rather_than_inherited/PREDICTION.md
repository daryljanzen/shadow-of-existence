# r7824 (60) — PRE-REGISTRATION: the best fit to the joint Planck + ACT data

**Order `r7821` (69), item ①:** *"The best fit to the joint data, through the harness's `fit.py`, and
the signature's distance from the sky's tilt on that fitted baseline, Planck-only beside joint as
before. Register first."*

Committed and pushed **before** anything is fitted or measured.

---

## 0. WHAT IS BEING REPAIRED, AND WHY A FIT IS THE REPAIR

`r7822` measured the joint arm on a **banked control**, amplitude-normalised to `plik_lite` but never
fitted to it. That control misfits Planck's own tail at `χ²/bin 5.04` over `ℓ 1000–1500` and `9.59`
over `1500–1760`. ⇒ *A tilt fitted against the sky on such a baseline absorbs the baseline's own
shape error together with any signature*, which is exactly why `r7822` kept the `19.25σ` out of
`P15` and why `69` ruled that decision right.

**So the quantity this revision needs is a baseline that is a best fit to the data it is being scored
against.** Two things follow, and both are registered rather than discovered later:

1. **The engine is the harness's.** `computations/planck_tt_likelihood/fit.py` fits `ΛCDM` through
   `CAMB` on five parameters — `H0`, `ω_b`, `ω_c`, `A_s`, `n_s`, with `τ` held at `0.054` — by
   Nelder–Mead. **This revision reuses that engine and that parameterisation, and replaces only the
   likelihood**: `fit.py` scores against `plik_lite` TT+TE+EE over the full range, while the joint
   arm is Planck TT below the `PlanckActCut` multipole plus ACT DR6 TT above it, each block carrying
   its own analytically marginalised amplitude. ⌗ `fit.py` is not edited; its suppression function is
   reproduced verbatim and Ⓑ② asserts that by comparing source text.
2. **A CAMB baseline is computed on every integer `ℓ`, so the reach that bound `r7820` is gone.**
   `r7820`'s GUARD — *check a window's support against the theory's reach, because flat extrapolation
   is silent* — forced it to drop every ACT bandpower whose window support left the banked control's
   `ℓ = 3200`. A theory evaluated to `ℓ = 8700` covers ACT's full window support. **That makes the
   arm bigger than `r7820`'s, so both subsets are reported (Ⓙ⑩) rather than the new one silently
   replacing the old.**

### ⚠ THE ONE THING A FITTED BASELINE CHANGES ABOUT THE QUESTION

On a fitted baseline the sky's preferred tilt should come out **near zero by construction**, because
the baseline was fitted to the same data. ⇒ *The tilt distance therefore stops being a measurement of
the sky and becomes a measurement of the signature's required excursion against the fit's own error
bar.* That is what the order asks for and it is reported, **but it cannot be the whole of the
answer**, so Ⓗ⑧ registers the statistic that does not have this property: the `Δχ²` between the two
fits at **equal parameter count** — `ΛCDM` fitted, against `ΛCDM × S(ℓ)` fitted, where `S` carries no
free parameter of its own because the construction derives it from the cosmology.

---

## 1. THE CONSTRUCTION, FIXED BEFORE THE MEASUREMENT

- **Data.** Planck `plik_lite` TT bins with `ℓ_hi < CUT`, `CUT` read from the banked
  `PlanckActCut.yaml`; ACT DR6 CMB-only TT bandpowers whose window **support** begins above Planck's
  highest used `ℓ` — the support split `r7820` established, not the effective-multipole split.
- **Amplitudes.** One per block, marginalised in closed form, as `r7820`: `A_planck` and `A_act` are
  not tied, because `A_act` is flat `0.5–1.5` in the shipped likelihood against Planck's
  `Normal(1, 0.0025)`.
- **No cross-covariance**, because no multipole is used twice; `DR6`'s own neglect is inherited and
  stated, as at `r7816` Ⓕ⑥.
- **Theory.** `CAMB`, lensed total TT, `CMB_unit='muK'`, `lens_potential_accuracy=0`,
  `AccuracyBoost=1.0`, on `ℓ = 2 … 8700`.
- **Arm I** — `ΛCDM`: the five parameters above.
- **Arm II** — the construction: the same five parameters, with the suppression `S(ℓ)` **derived from
  each trial cosmology** by `fit.py`'s `cr_supp` (its `r` from the two sound-horizon/driving
  integrals, its `ℓ_D` from that spectrum's own damping over `1400 < ℓ < 2400`, onset
  `z = 6797.0`). **Arm II has no free parameter arm I lacks.**

---

## 2. THE ARMS — each a comparison, each with a reachable negative

**Ⓐ① This probe reproduces `r7822`'s landed figures on the banked control.** Run on
`L824_lcdm_L3200_nk960` with `r7820`'s bandpower subset, it must return
`Δn_sky = −0.020658 ± 0.003782`, `Δn_sig = −0.093474`, `19.25σ`, to the digits `r7822` printed.
*Negative, reachable:* it does not, in which case this harness is not the one that produced the
landed numbers and **nothing measured here may be compared with them** — reported as that, not
patched.

**Ⓑ② The suppression is `fit.py`'s own, asserted by source text and not by resemblance.** The
`cr_supp` body used here is compared character-for-character with `fit.py`'s. *Negative, reachable:*
they differ, and then the figure is this seat's construction rather than the harness's and is
reported as such.

**Ⓒ③ Arm I converges in the interior of `fit.py`'s own bounds.** Every best-fit parameter strictly
inside `55<H0<85`, `0.018<ω_b<0.026`, `0.09<ω_c<0.16`, `1.5<A_s/10⁻⁹<3.0`, `0.85<n_s<1.25`.
*Negative, reachable:* a parameter lands on a bound, in which case the minimum is a boundary artefact
and **every `Δχ²` below is a limit, not a value.**

**Ⓓ④ The fit repairs the tail misfit that motivated it.** `χ²` per bin on the fitted baseline over
`ℓ 1000–1500` and `1500–1760`, against the banked control's `5.04` and `9.59`. *Negative, reachable
and it would matter:* the misfit does **not** fall materially, which would mean the tail deficit is
not a `ΛCDM`-parameter direction — and then the footing the paper waits on is still missing, whatever
the fit does to `χ²` elsewhere.

**Ⓔ⑤ On the fitted baseline the sky's own tilt is consistent with zero.** `|Δn_sky| < 2σ` of the
joint fit's own width. *Negative, reachable:* it is not, which would mean the joint minimum is not at
the tilt direction's minimum — the fit minimises over all bins and both amplitudes, so this is a
real possibility and not a formality.

**Ⓕ⑥ The suppression's two numbers are derived from the fitted cosmology, not inherited.** `r` and
`ℓ_D` computed on arm I's best fit, printed beside `r7611+70`'s `1.0926` and `1489.5783`. *Negative,
reachable:* they move far enough to change Ⓖ⑦'s verdict, in which case **the inherited pins were
doing load-bearing work** and every earlier figure that used them inherits that dependence.

**Ⓖ⑦ THE MEASUREMENT — the signature's distance from the sky's tilt on the fitted baseline**, with
the strict `2σ` rule applied to that number and nothing else. *Registered as a comparison, and the
negative is the one that would overturn the row:* **if the distance falls below `2σ`, the signature
survives the best fit and `r7822`'s `19.25σ` was an artefact of the baseline's misfit.** Either way
it is reported as measured.

**Ⓗ⑧ `Δχ²` between the two fits, at equal parameter count.** Arm I against arm II, both minimised,
same five parameters. *Negative, reachable:* `Δχ² < 0` — the construction fits the joint data
**better** than `ΛCDM` — which would reverse the direction of the whole row and is reported first if
it happens.

**Ⓘ⑨ Planck-only beside joint on the fitted baseline**, over the three published windows
`100–1758`, `700–1760`, `1000–1760`, as every earlier revision of this row has reported them.
*Negative, reachable:* the Planck-only and joint verdicts disagree under the `2σ` rule, in which case
**no single arm decides** and both are carried.

**Ⓙ⑩ The reach no longer binds, and the two subsets are compared.** The count of ACT bandpowers
usable above the split with a theory to `ℓ 8700`, against the count `r7820` could use under the
banked control's `ℓ 3200`; and Ⓖ⑦'s verdict computed on both subsets. *Negative, reachable:* the
verdict differs between subsets, in which case the arm's extent is itself load-bearing and is
reported as a range rather than a number.

**Ⓚ⑪ Arm count asserted at the end: eleven.** Any arm that fails is reported **as failed**, with its
criterion unchanged from this file.

---

## 3. What this revision does NOT do

It does not edit `fit.py`, the instrument, any gate, or any receipt belonging to another seat. It
does not touch `sec:coherence`: the sentence `69`'s order asks for is written *from* Ⓖ⑦ and Ⓗ⑧ once
they exist, and **this file has no result in it.** It does not begin item ② of the order — the
recompute of `r7804`, `r7806`, `r7808`, `r7812` and `r7814` on `L824_lcdm_L3200_nk960` — which is its
own revision, as `69` specified.
