# r7842 (60) — PREDICTION, registered and pushed BEFORE any measurement

On order `r7841` (69), items ①–④: add polarisation to the score, add the lensing-reconstruction
spectrum, add the low-`l` and optical-depth information or a `tau` prior equivalent and say which,
and land the CONTROL before the arm is read.

**This file is the registration. It is committed and pushed before the extended harness is scored
even once.** Every arm below is a COMPARISON with a REACHABLE NEGATIVE, and the criteria are fixed
here. A failed arm will be reported AS failed, with the criterion as written and not loosened. The
arm count is asserted at the end of the receipt.

---

## WHAT THE ORDER ASKS FOR THAT THIS SEAT HAS, AND WHAT IT DOES NOT — stated before running

Surveyed in the repository before writing this file, so that the registration is honest about its
own reach:

* **① POLARISATION IS REACHABLE.** `planck_lite_py.PlanckLitePy(spectra='TTTEEE')` loads `215` TT,
  `199` TE and `199` EE bandpowers — `613` in all — with the full `plik_lite` covariance across the
  three, and takes the three spectra directly. The instrument already carries the E-mode projection
  behind its `POLSAVE` switch (`r7631+70`), off by default: it projects the same polarisation source
  it carries in T through the E-mode kernel and forms `C_EE` and `C_TE`. So both halves exist and
  what is owed is the generation and the scoring.
* **② THE LENSING-RECONSTRUCTION SPECTRUM IS NOT IN THE REPOSITORY.** There are no lensing
  bandpowers and no lensing covariance under `computations/`: the only likelihood data banked are
  `planck2018_plik_lite` and `act_dr6_cmbonly`, and the second is the CMB-only TT/TE/EE likelihood,
  not the lensing one. This arm therefore registers a GATE rather than a result.
* **③ THE LOW-`l` BINS ARE NOT IN THE REPOSITORY EITHER.** `use_low_ell_bins=True` reads
  `data/planck2018_low_ell/CTT_bin_low_ell_2018.dat`, which is absent; the loader raises on it. The
  banked `plik_lite` data start at `l = 30`. **The `tau` half of ③ is not a data question but a
  reach question, and it is measurable here**, which is what the order's "and say which" invites.

## The arms

**Ⓐ① The instrument's polarisation outputs exist and are sane.** With `POLSAVE` on, both arms produce
`C_TE` and `C_EE` on the same multipole axis as `C_TT`; the EE spectrum is positive everywhere it is
scored, the TE spectrum CHANGES SIGN, and EE's first acoustic maximum falls between `l = 120` and
`l = 160` where TT's first falls between `l = 190` and `l = 250`.
*Reachable negative: a positive-definite TE, or an EE peak on top of TT's, either of which would
mean the E-mode kernel is not doing what its own docstring says.*

**Ⓑ② The extension is an extension, and the closure proves it.** Scored on TT alone, the extended
harness reproduces `r7838`'s own TT numbers: the control's `95` per cent upper limit to within `1`
meV of `277.7` and its `chi^2` at the minimum to within `0.05` of `194.57`.
*Reachable negative: a TT number that moves when only TE and EE were added, which would mean the
extension changed the TT scoring rather than adding to it.*

**Ⓒ③ One amplitude, not three.** The analytic amplitude solve is JOINT across TT, TE and EE — one
`A_s`, as the physics requires — and the model's positivity guard is applied to TT and EE only,
because TE is negative over part of its range.
*Reachable negative: a per-spectrum amplitude, which would throw away the relative normalisation
that is most of what polarisation adds.*

**Ⓓ④ THE SAMPLER STILL CONVERGES on the wider score.** Six chains, split Gelman–Rubin `R̂ < 1.05` on
every parameter, effective sample size on the sum `>= 1000`.
*Reachable negative: `R̂` above the threshold, which would mean the posterior is not measured.*

**Ⓔ⑤ THE DECISIVE ARM — THE CONTROL ON TT+TE+EE.** **The criterion is the order's: the control's
`95` per cent upper limit on the sum falls within a factor `1.5` of the published `64.2` meV, that
is inside `42.8` to `96.3` meV, AND its fitted effective mass is NEGATIVE, the sign the published
`-0.101` eV carries.**

⚠ **AND THIS SEAT'S OWN EXPECTATION, REGISTERED SEPARATELY AND FALSIFIABLE BOTH WAYS: it will
FAIL.** `r7838` located the looseness in what the harness scores, and the single largest missing
lever is the one item ② names — the lensing-reconstruction spectrum is the measurement that weighs
neutrinos most directly, and it is not in the repository. Polarisation adds the damping tail and the
peak positions in two more spectra, which should TIGHTEN the limit substantially from `277.7` meV
without reaching the published band. **The expectation is a limit between `100` and `250` meV.**
*Both halves are reachable: a limit inside the order's band refutes this seat's expectation and is
reported as a refutation, not quietly; a limit outside `100` to `250` refutes the size of it.*

**Ⓕ⑥ The gap's sign survives the wider score.** The control's fitted matter-density gap stays
POSITIVE, as it came out at `+3.70` per cent on TT alone against the published `+2.48`.
*Reachable negative: a sign flip, which would mean the polarisation data disagree with TT about the
quantity the order's reasoning turns on.*

**Ⓖ⑦ THEN THE ARM OF RECORD — and only if Ⓔ⑤ passes.** Registered expectation unchanged from
`r7838`: the construction's own limit is LOOSER than the control's. Where `59` and `64` meV sit is
reported either way.
*Reachable negative: a tighter limit than the control's, reported as a finding against the
construction.*

**Ⓗ⑧ ITEM ②'s GATE, MEASURED AND NAMED RATHER THAN DESCRIBED.** The receipt asserts, from the
repository rather than from memory, that no lensing bandpowers and no lensing covariance are banked,
and names what would discharge it: the Planck PR4 or ACT DR6 lensing bandpowers with their
covariance, as files in the repository, since this seat cannot fetch them.
*Reachable negative: finding them banked, in which case the arm is wrong and item ② is runnable.*

**Ⓘ⑨ ITEM ③'s TWO HALVES, THE SECOND ONE MEASURED.** The low-`l` bin file is asserted absent. And
**`tau`'s reach in this harness is measured, not assumed**: the claim to be tested is that a `tau`
prior constrains NOTHING here, because (a) the harness solves one overall amplitude analytically at
every point, so a uniform `exp(-2 tau)` is EXACTLY degenerate with it, and (b) the instrument's
visibility carries recombination only and no reionisation, so there is no low-`l` EE bump for `tau`
to move. Both halves are checked against the instrument's own source and arithmetic.
*Reachable negative: a measurable change in the score under a `tau` shift, which would make a `tau`
prior informative and the claim false.*

**Ⓙ⑩ The arm count.** The receipt asserts how many arms it ran.

## What is NOT claimed

* `P15` is not to change until the arm is read — the order says so and this revision holds to it.
* No limit on the sum will be reported for the construction unless Ⓔ⑤ passes.
* Items ② and ③'s low-`l` half are NOT attempted: the data are not in the repository, and a limit
  computed without them is not the published comparison. Saying so precisely is the deliverable
  for those two, not a substitute for them.

---

Node `60`, `r7842`, on order `r7841` (69), items ①–④. Registered before any run.
