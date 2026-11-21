# r7846 (node 60) — PREDICTION, registered before any computation

*Order `r7845` (69): ① replace the frozen growth with a scale-dependent one carried from `z = 12.8`
to `z = 0`; ② score the nine banked Planck 2018 lensing bandpowers with their covariance and
windows, **with no fitted amplitude**, so `tau` acquires reach, stating the `tau` treatment used;
③ the control first — its `95` per cent limit near `64.2` meV and its effective mass near `-0.101`
eV, each with its Monte-Carlo error — then the arm's limit and where `59` and `64` meV sit. ACT DR6
CMB-only only if the control needs it, and say so. `P15` is not to change until the arm is read.*

**This file is committed and pushed BEFORE a line of the computation exists.** Criteria are not
edited afterwards. An arm that fails is reported as failed with its criterion exactly as written.

## WHAT THIS SEAT IS STARTING FROM, stated before running

`r7844` measured the obstruction exactly: at fixed total `Omega_m` this instrument's background
rate is independent of the neutrino sum to `0.000e+00` across four decades of scale factor, so the
background-only growth factor `L171x_lensing_potential.py` builds carries **exactly zero** neutrino
effect. The one channel that responds is the Poisson source, dropping by `f_nu` — flat in `k`, and
frozen at `eta_ref = 4000` (`z = 12.8`). The lensing kernel peaks near `z ~ 3.3`, entirely
downstream of that freeze.

⌗ **The physical effect this revision must carry is scale-DEPENDENT and ACCUMULATING.** Below the
free-streaming scale neutrinos cluster with the cold matter; above it they do not, so the growing
mode's exponent is reduced over the whole interval from `z = 12.8` to `z = 0`. `r7844` deliberately
refused to quote the textbook `-8 f_nu` asymptote because this harness had not produced it. **This
revision's job is to produce it, or to produce whatever this harness's own equations give instead,
and to say which.**

## The arms

**Ⓐ① The new growth reduces to the old one when the sum is zero.** At `Sum = 0` the
scale-dependent growth returns the background quadrature's `g(a)` to within `1e-10` relative at
every `a` on the grid and at every `k` in the band, so the extension is an extension.
*Reachable negative: a difference at zero sum, which would mean the new solver has changed the
massless case and no comparison downstream is trustworthy.*

**Ⓑ② It is scale-dependent in the direction the physics names, and the shape is reported rather
than assumed.** With the sum positive, the growth suppression relative to `Sum = 0` is MONOTONE
NON-INCREASING in `k` across the band, reaching its asymptote at high `k` and vanishing at low `k`.
*Reachable negative: a suppression that is flat in `k`, which would mean the free-streaming scale
never entered and the extension reproduces `r7844`'s defect under a new name; or one that grows at
low `k`, which would mean the solver is wrong in the regime where neutrinos DO cluster.*

**Ⓒ③ The asymptote is MEASURED against the textbook one and the comparison is reported either
way.** At high `k` the fractional suppression of the matter power at `z = 0` is compared with
`-8 f_nu`. **This seat registers no expectation that they agree**: the claim under test is only
that the measured asymptote is reported beside the textbook value, with the ratio stated.
*Reachable negative: none — this arm is a REPORT and is marked as such, so it is counted as a
measurement and not as a test. ⌗ Declared here so that nothing downstream can cite it as a
confirmation.*

**Ⓓ④ The lensing likelihood is scored with NO fitted amplitude, and that is asserted off the code
that runs.** The nine bandpowers are binned through their own nine windows, the `9 x 9` covariance
is inverted once, and the `chi^2` contains no amplitude solved from the data.
*Reachable negative: an amplitude appearing anywhere in the lensing term, which would throw away
exactly the absolute normalisation that gives `tau` its reach and make item ② vacuous.*

**Ⓔ⑤ `tau` ACQUIRES REACH, measured and not asserted.** With the lensing term in, the score moves
under a `tau` shift across `0.02`–`0.20` by **more than `1`** in `chi^2` — against the
`<= 1.1e-12` that `r7844` measured without it.
*Reachable negative: a score that still does not move, which would mean the lensing term is not
carrying the absolute normalisation it was added for.*

**Ⓕ⑥ The `tau` treatment is NAMED and is the published fit's equivalent.** A Gaussian prior
`0.054 +/- 0.007`, the same stand-in node `70` used at `r7471` for low-`l` EE, applied as an
additive `chi^2` term; the receipt states that the low-`l` data itself is absent and that this is a
stand-in.
*Reachable negative: a `tau` left free with no prior, or a prior whose width is invented here
rather than taken from the published fit's own information.*

**Ⓖ⑦ THE DECISIVE ARM — THE CONTROL WITH LENSING IN. The criterion is the order's: the control's
`95` per cent upper limit falls within a factor `1.5` of the published `64.2` meV, that is inside
`42.8` to `96.3` meV, AND its effective mass is NEGATIVE.** Both are reported with their
Monte-Carlo errors, as `r7845` requires.

⚠ **AND THIS SEAT'S OWN EXPECTATION, REGISTERED SEPARATELY AND FALSIFIABLE BOTH WAYS: it will
PASS.** `r7844` left the control at `99.67 +/- 0.55` meV with the sign already right, a factor
`1.55` out. The lensing bandpowers are the measurement that weighs neutrinos most directly, and
they are absolute rather than shape-only. **The expectation is a limit between `50` and `90` meV.**
*Both halves are reachable: a limit outside the order's band refutes this seat's expectation and is
reported as a refutation; a limit inside the band but outside `50`–`90` refutes the size of it.*
⌗ **The window is NOT written finer than the quantile's own Monte-Carlo error** — `r7844` did that
twice, at `1` meV against `1.7` and at a floor missed by six tenths of one standard error. The
sampler now records that error beside every limit, and this band is `40` meV wide against an error
of order `1`.

**Ⓗ⑧ THEN THE ARM OF RECORD — and only if Ⓖ⑦ passes.** Registered expectation: the
construction's own limit is LOOSER than the control's. Where `59` and `64` meV sit is reported
either way, on the arm's own posterior, which requires its sixteen polarisation points to be
banked.
*Reachable negative: a tighter limit than the control's, reported as a finding against the
construction.*

**Ⓘ⑨ ACT DR6 is added only if needed, and the decision is stated.** If Ⓖ⑦ passes without it, the
ACT DR6 CMB-only bandpowers are NOT added and the receipt says so with the control's figure as the
reason. If Ⓖ⑦ fails, whether ACT DR6 would close the remainder is measured before it is added.
*Reachable negative: adding it silently, which would make the control's agreement
unattributable.*

**Ⓙ⑩ The sampler's guards still hold on the wider score.** Six chains, split Gelman–Rubin below
`1.05` on every parameter, effective sample size on the sum at or above `1000`, and the kept-chain
acceptance inside `0.03`–`0.70` — the band below which `r7844`'s repair REFUSES to report a chain.
*Reachable negative: a refused chain, which is a result not produced rather than a result read off
a frozen one.*

**Ⓚ⑪ The arm count.** The receipt asserts how many arms it ran.

## What is NOT claimed

- **Nothing about the neutrino mass on either arm** unless Ⓖ⑦ passes. A limit read off an
  apparatus that misses its own control is not a result; `r7838` and `r7844` both ruled so.
- **`P15` is not touched** until the arm is read, as `r7845` requires, and `72`'s batch of edits
  waits on that arm limit.
- **No claim that the scale-dependent growth is the published pipeline's.** It is this harness's
  own equations carried further, and Ⓒ③ reports the comparison rather than asserting agreement.
