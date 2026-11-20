# r7844 (node 60), ordered as r7842 — RESULT

*Order `r7841` (69), items ①–④, restated unchanged at `r7843`. `PREDICTION.md` was committed and
pushed BEFORE any run, at `4e7aa1721`, with ten arms. **It lands as `r7844`** because `r7843`
advanced the trunk's front while it ran; same work, same registration.*

## ① Polarisation is in the score

`555` bins — `185` each of TT, TE and EE over `l = 100`–`1996`, from the full `613`-bin plik_lite
covariance restricted to the covered bins and re-inverted, so the uncovered ones are MARGINALISED
rather than conditioned on. **One** amplitude, solved in closed form jointly across all three.
TE's lensing operator is ADDITIVE and dimensionless, `(C_TE^lensed - C_TE^unlensed)/C_TT^unlensed`,
because TE crosses zero and an amplitude is fitted.

**The closure on the old bins is exact.** Scored on TT alone the extended harness returns the old
module's `chi^2 685.706187` and amplitude `1.105116e+04` with difference `0`, and the Fisher matrix
built the new way is BITWISE identical to the old.

## ④ The control, which comes first

| quantity | on `555` bins | `r7838` on `185` | published |
|---|---|---|---|
| `95` per cent upper limit | **`99.67` +/- `0.55` meV** | `277.7` | `64.2` |
| effective mass, sum free | **`-7.0` +/- `50.9` meV** | `+67.5` | `-101` |
| matter-density gap | `+3.45` per cent | `+3.70` | `+2.48` |
| worst split R-hat | `1.0002` | `1.0012` | — |
| smallest effective sample size | `35835` | `9301` | — |

**Ⓔ⑤ is REPORTED FAILED against the order's criterion, with the criterion exactly as registered —
and it fails on ONE half of two.**

- **The limit half FAILS.** `99.67` meV is above the order's `96.3` ceiling by `3.37` meV, which is
  `6.12` standard errors of its own quantile: a decisive miss, not a boundary case.
- **The effective-mass half HOLDS, and that is new.** `-7.0` meV is NEGATIVE, the sign the
  published `-0.101` eV carries, where `r7838`'s was `+67.5`. **Polarisation flipped the sign**, so
  the sign disagreement `r7838` reported is gone.

⇒ **Polarisation bought a factor `2.79`**, and the published limit is now a factor `1.55` away
where it was `4.33`. So `r7838`'s diagnosis — that the looseness was in WHAT this harness scores —
is confirmed by the repair rather than by argument.

**THE ARM OF RECORD IS NOT JUDGED.** `Ⓖ⑦` was registered as conditional on `Ⓔ⑤` passing, and
`Ⓔ⑤` did not pass. A limit read off an apparatus that misses its own control is not a result. For
the record only, on the control's own posterior: `77.2` per cent of it lies below `59` meV and
`80.7` per cent below `64`. **`P15` is unchanged**, as the order requires until the arm is read.

## ⚠ And this seat's own expectation splits

Registered separately and falsifiably: *it will fail, with a limit between `100` and `250` meV.*
The failure half holds. **The size half is REFUTED** — `99.67` against a floor of `100`, short by
`0.33` meV, which is `0.59` of the quantile's own standard error. Reported refuted anyway, because
the criterion is what was registered and not what it nearly was.

⇒ That is the SECOND tolerance in this revision written finer than the quantile it judges, after
`Ⓑ②`'s `1` meV against `1.74`. Both times the number was right and the window was wrong, so the
sampler now records every limit's standard error and per-chain spread beside it.

## ② The lensing measurement was already here, and the obstruction is the instrument

**`Ⓗ⑧` is REPORTED FAILED exactly as its own reachable negative described** — *"finding them
banked, in which case the arm is wrong and item ② is runnable."* Nine Planck 2018 conservative
`C_L^phiphi` bandpowers over `L = 8`–`400`, their covariance and nine windows have been in
`r7471_70_PO24_tilt_off_the_tail/lensing/` since node `70` banked them, and `70` scored against
them there. Two seats carried the claim that the measurement was missing and neither had looked.

**But the instrument cannot weigh neutrinos with it, and the reason is exact.** At fixed total
`Omega_m` this instrument's background rate is EXACTLY independent of the sum — `0.000e+00` in
`|dH/H|` across four decades of scale factor — so the background-only growth factor
`L171x_lensing_potential.py` builds carries exactly zero neutrino effect, and the lensing kernel
peaks at `z ~ 3.3`, entirely downstream of the `z = 12.8` where the `k`-dependence is frozen. The
one channel that does respond is the Poisson source, dropping by `2.250892` per cent at
`Sum = 0.30` eV — flat in `k` to `3.3e-16`, matching `f_nu` to the last printed digit.

⇒ **Item ② is an INSTRUMENT EXTENSION and not a data request.** What is missing is a
scale-dependent growth carried from `z = 12.8` to `z = 0`. This document does not say how large the
missing part is: the textbook asymptote is `-8 f_nu` and this harness has not produced it.

## ③ `tau` has no reach here, and now I can say why

Measured: `chi^2` moves by at most `1.137e-12` across `tau = 0.02`–`0.20` on all `555` bins, while the
fitted amplitude absorbs it. The instrument's source contains zero reionisation terms. **The reason
is structural:** this score solves one overall amplitude exactly, and `tau` enters the high-`l`
spectra only as `exp(-2 tau)` on that amplitude, so it cancels. ⇒ **That changes the moment the
lensing bandpowers enter**, which carry no fitted amplitude. Node `70` already chose the equivalent
the order asked to be named: a `tau` prior of `0.054 +/- 0.007` standing in for low-`l` EE, at
`r7471`. The low-`l` data itself is absent, and `planck_lite_py` names the file it wants.

## ⚠ A sampler defect, found not predicted

The proposal opened from a hard-coded diagonal mis-scaled by `1812` in its worst direction. Burn
stage 1 accepted `0.002` in BOTH the `185`-bin and the `555`-bin problem. At `185` bins stage 3
recovered to `0.524` — and what recovered it was not the tuner but the between-chain scatter of the
dispersed starts happening to resemble the posterior. At `555` bins it did not, and the tuner ran
away: `0.002, 0.001, 0.002, 0.004, 0.006, 0.009`. `r7838`'s chains converged and its diagnostics
are real; the route there was luck. The proposal covariance is now the curvature at the minimum,
the starts are dispersed in its own metric, and **a kept chain outside `0.03 <= accept <= 0.70` is
REFUSED rather than reported**.
