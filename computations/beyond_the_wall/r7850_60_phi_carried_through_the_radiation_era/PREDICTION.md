# r7850 (node 60) — PREDICTION, registered before any computation

*Order `r7847` (69): ① carry the potential `Φ` through the radiation era with its scale-dependent
decay, from the handover through matter–radiation equality into the late growth, on the instrument's
own rate — replacing the matter-plus-Λ closed-form growth evaluated on a background carrying
radiation, which `r7848`'s Ⓐ① found wrong by about half a per cent in `D` by `z = 0`; ② show what it
buys on the two measured symptoms, the missing neutrino suppression (about `44` per cent) and the
lensing shape drift (`χ²/dof 2.05`, `+49.8` per cent monotone); ③ the control first, against `64.2`
meV and `-0.101` eV, comparing against `cc66`'s independent CAMB decomposition of the control's
response to the sum when it lands. `P15` is not to change, and `72`'s batch waits.*

**This file is committed and pushed BEFORE a line of the computation exists.** Criteria are not
edited afterwards. An arm that fails is reported as failed with its criterion exactly as written.

## WHAT THIS SEAT IS STARTING FROM, stated before running

`r7848` measured two things that this order acts on, and one that constrains how:

1. **Ⓐ①'s failure located the defect in the thing compared against, not in the solver.** On one
   pure matter + Λ rate the background quadrature and the two-fluid ODE agree to `9.799e-09`;
   on the instrument's real rate they diverge to `5.276e-03`, monotonically, while the radiation
   share falls to nothing. So `growth_over_a()` is a matter + Λ closed form evaluated on a
   background that carries radiation, and its `D` is wrong by about half a per cent by `z = 0`.
2. **`carry_validity.py` showed a matter-only growth equation does not LINK two start times.**
   Carrying `Φ(k)` from `z = 188` to `z = 12.8` and comparing with the instrument's own `Φ(k)`
   there gives a `k`-DEPENDENT ratio — `0.9638` at the largest scales, `0.7362` at the smallest,
   median `0.7807` — which is sub-horizon `Φ` decay through residual radiation, `5.47` per cent of
   matter at `z = 188` against `0.39` at `z = 12.8`.
3. **The instrument already carries `Φ` through the radiation era and through equality.**
   `ACOUSTIC_two_arm.evolve` integrates the perturbations from `η = 0.0155` (`a = 3.3e-08`), past
   matter–radiation equality at `z ≈ 3400` (`η ≈ 110` Mpc), to `ETA_END = 1893` Mpc (`z ≈ 53.6`) by
   default, and further when `e_end` is given — `r7848`'s `phi_shape` already pushed it to `η =
   4000` (`z = 12.8`). **So the missing piece was never the radiation era. It was that the LATE
   carry threw the instrument's own solve away and substituted a closed form.**

⌗ **ONE THING WAS PROBED BEFORE THIS FILE WAS WRITTEN, AND IT IS STATED HERE RATHER THAN PRESENTED
LATER AS A RESULT.** I timed `evolve` for five wavenumbers at increasing `e_end` to find whether the
instrument's own solve can simply be run to today, which would remove the carry entirely. It cannot
be run to today cheaply: `12.2` s to `η = 500`, `40.4` s to `η = 1000`, and the growth is faster
than linear because the free-streaming hierarchy stiffens after recombination. **So there is a
handover, and this revision's job is to make the carry from it correct rather than to abolish it.**
The rest of that timing is still running and will be recorded as the revision's cost table, not as
an arm.

## The design, stated before the arms

**The handover is the latest time the instrument's own solve reaches inside a stated compute
budget**, and the budget, the handover and its cost are all recorded. From the handover the carry
integrates the two-fluid equation `r7848` already uses —

```
d²δ_cb/dN² + (2 + dlnH/dN) dδ_cb/dN = 1.5 Ω_m(a) [ (1−f_ν) δ_cb + f_ν δ_ν ]
```

— whose friction and whose `Ω_m(a)` both read the instrument's own rate, so radiation is in it and
the Meszaros suppression is carried rather than assumed. **What changes is where it starts and what
it starts from:** the initial `Φ` and its derivative come from the instrument's own perturbation
solve at the handover, not from a closed-form growing mode, so the decaying mode that the residual
radiation era leaves behind is carried instead of discarded.

⌗ **The neutrino mass still enters through the filter, and that is still an approximation.** The
instrument's hierarchy free-streams its neutrinos as MASSLESS, so its `Φ` carries only the flat
`f_ν` reduction of the Poisson source that `r7844` measured. The scale-dependent part is the filter
`δ_ν = δ_cb / (1 + (k/k_fs)²)`, which has both limits right by construction and is an interpolation
between them. **This revision does not claim to be the published pipeline's treatment**, and Ⓓ④
reports its asymptote rather than asserting agreement.

## The arms

**Ⓐ① THE CARRY IS TESTED CLOSED, AGAINST THE INSTRUMENT'S OWN `Φ` AND NOT AGAINST A CLOSED FORM.**
Carrying `Φ(k)` from the handover to a later time the instrument ALSO covers reproduces the
instrument's own `Φ(k)` there with a residual whose spread across the band is below `2.3` per cent
— one tenth of the `23` per cent spread `carry_validity` measured for the matter-only carry.
*Reachable negative: a spread at or above that, which would mean the carry still fails to link two
times the instrument itself links, and the revision has not done the thing it was ordered to do.*
⌗ **The criterion is set against a MEASURED spread and not against a guessed precision**, because
`r7848`'s Ⓐ① failed on a tolerance finer than the accuracy of the thing it compared against.

**Ⓑ② THE HANDOVER IS NOT A FREE PARAMETER DRESSED AS A CHOICE.** Ⓐ①'s residual is measured at no
fewer than three handover times, and the revision reports whether the carry's agreement depends on
which one is used. *Reachable negative: a residual that depends strongly on the handover, which
would mean the carry is being tuned rather than solved, and the arm says so.*

**Ⓒ③ WHAT IT BUYS ON THE SHAPE DRIFT, which is the order's ② first half.** With the new carry the
nine banked bandpowers' `χ²` on `8` degrees of freedom and the monotone drift are both re-measured
against `r7848`'s `2.049` per degree of freedom and `+49.8` per cent. Registered expectation: BOTH
FALL. *Reachable negative: either rises, or falls by less than the bandpowers' own errors permit
one to call a change, and the arm reports the failure.*

**Ⓓ④ WHAT IT BUYS ON THE MISSING SUPPRESSION, the order's ② second half.** The high-`k` asymptote
on the power is re-measured against the textbook `-8 f_ν`, where `r7848` got `0.296` of it carrying
from `z = 12.8` and `0.667` carrying from `z = 188`. Registered expectation: the new carry reaches
AT LEAST `0.667`, and whatever remains is stated as the filter's rather than the carry's.
*Reachable negative: no improvement on `0.296`, which would mean the missing suppression was never
the carry's start and the filter is the whole of it.*

**Ⓔ⑤ THE ABSOLUTE NORMALISATION IS NOT BROKEN BY THE REPAIR.** `r7848` held
`(A_cmb/T_CMB²)·e^{+2τ} = 1.617967e-09` against the bandpowers' own `1.471643e-09`, a ratio of
`0.909563`, with nothing fitted. With the new carry that ratio is re-measured and reported.
Registered expectation: it moves TOWARD `1`. *Reachable negative: it moves away, which is a finding
against the new carry and is reported as one.*

**Ⓕ⑥ THE DECISIVE ARM — THE CONTROL, FIRST, WITH ITS MONTE-CARLO ERRORS.** The criterion is the
order's: the control's `95` per cent upper limit falls inside `42.8` to `96.3` meV, a factor `1.5`
on the published `64.2`, AND its effective mass is NEGATIVE. Both reported with their Monte-Carlo
errors.

⚠ **AND THIS SEAT'S OWN EXPECTATION, REGISTERED SEPARATELY AND FALSIFIABLE BOTH WAYS: IT WILL
FAIL.** `r7848` left the control at `111.38 ± 0.41` meV with the effective mass at `+44.25 ± 39.79`.
The repair should move both the right way — the shape drift and the missing suppression are both
real and both reduce — but `44` per cent of the suppression returns only if the filter is also
right, and the filter is an interpolation. **The expectation is a limit between `70` and `110` meV
and a NEGATIVE effective mass: better on both halves, and still outside the order's band.**
*A limit inside `42.8`–`96.3` with a negative effective mass refutes this expectation and passes the
order's criterion, and would be reported as this seat having been too pessimistic about its own
repair.* ⌗ The window is `40` meV wide against a quantile error of order `0.4`, so it is not written
finer than the thing that judges it.

**Ⓖ⑦ `cc66`'s CAMB DECOMPOSITION IS COMPARED IF IT HAS LANDED, AND ITS ABSENCE IS NOT A RESULT.**
If the decomposition is in the repository, this revision's term-by-term response of the control to
the sum is compared against it and the comparison is reported whichever way it goes. If it is not,
the receipt SAYS it is not and infers nothing from the silence. *Reachable negative: claiming
agreement with a reference that is not there, or treating its absence as corroboration.*

**Ⓗ⑧ THEN THE ARM OF RECORD — and only if Ⓕ⑥ passes.** Where `59` and `64` meV sit is reported
either way, on the arm's own posterior, FOR THE RECORD and not as a bound.
*Reachable negative: reporting the arm's limit as a bound while the control misses, which `r7838`,
`r7844` and `r7848` all refused.*

**Ⓘ⑨ THE SAMPLER'S GUARDS HOLD, INCLUDING THE PER-DIRECTION ONE.** Six chains, split Gelman–Rubin
below `1.05` on every parameter, effective sample size on the sum at or above `1000`, kept-chain
acceptance inside `0.03`–`0.70`, AND no direction frozen — the guard `r7848` had to write because
`r7844`'s aggregate one passed a chain dead in the one direction its limit is read off.
*Reachable negative: a refused chain, which is a result not produced rather than a result read off a
frozen one.*

**Ⓙ⑩ THE COST IS RECORDED SO THE NEXT SEAT DOES NOT REDISCOVER IT.** The instrument's own solve
cost at each handover time used, and the cost of the carry, are written into the revision's record.

**Ⓚ⑪ The arm count.** The receipt asserts how many arms it ran.

## What is NOT claimed

- **Nothing about the neutrino mass on either arm** unless Ⓕ⑥ passes. A limit read off an apparatus
  that misses its own control is not a result; `r7838`, `r7844` and `r7848` all ruled so.
- **`P15` is not touched**, as `r7847` requires, and `72`'s batch waits.
- **No claim that this is the published pipeline's treatment.** The neutrino filter is an
  interpolation and the instrument's own neutrinos are massless in its hierarchy; Ⓓ④ reports the
  comparison rather than asserting agreement.
- **No claim that the instrument's solve could not be run to today** — only that it cannot be run
  there cheaply, with the measured cost stated. A later revision with a reduced late-time system
  may abolish the handover altogether, and that is named here as the thing this one does not do.
