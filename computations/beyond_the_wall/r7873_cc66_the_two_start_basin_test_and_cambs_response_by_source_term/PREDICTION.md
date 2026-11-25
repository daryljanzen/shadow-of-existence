# `r7873+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7873` (69), two items:

- **⑪ The two-start test**, as 60 routed it. At `Σ = 0.400` eV, the reference profiler on **both
  rulers** from two `H0` starts — near `65.3` and near `68.6` — everything else at its own best fit.
  Report the `χ²` each lands at and the `H0` each converges to. 60's three outcomes are all live.
- **⑫ CAMB's sum response BY SOURCE TERM**, if CAMB can give it. Each term's `D_ℓ(Σ)/D_ℓ(0) − 1` at
  the control, `Σ = 0.30` and `0.60`, over `ℓ = 100`–`420`. **Prove the split closes on CAMB's total
  before reading any term.** If CAMB cannot give it, say so in one line and stop; build no substitute.

⌗ **Reconnaissance run before this file, declared so nothing reads as a prediction confirmed.**
- `profile_likeforlike.profile(sum_ev, mode, start)` already takes an explicit start, so ⑪ needs no
  new machinery and the two starts go in as they are.
- `CAMBparams.set_custom_scalar_sources` **exists** and `camb.symbolic` imports, with
  `get_scalar_temperature_sources()` returning **exactly four** terms — `monopole_source`, `ISW`,
  `doppler`, `quadrupole_source`. ⇒ So the answer to "can CAMB give it" is **yes** for the term
  split, and ⑫ is not refused.

⛔ **But the early/late ISW split is NOT a source term.** CAMB's ISW term is the single expression
`2·exptau(t)·∂φ/∂t`; early and late ISW are the same integrand over different **stretches of time**.
Separating them needs a window in the scale factor inside the symbolic source, not a different term.
That is registered as the one part at risk, and `Ⓗ⑧` says what I will do either way.

---

## ⑪ THE TWO-START TEST

- **Ⓐ① The starts and the other four are READ, not chosen.** `65.29` and `68.59` are 60's own basin
  figures; the remaining four parameters come from this reference's banked `Σ = 0.400` point for each
  ruler. The run asserts it used those and prints them.
- **Ⓑ② The test is VALID before it is read:** both runs terminate, both land strictly inside
  `profile_likeforlike`'s `BOX`, and both `χ²` are finite. ⚠ A start that runs to the box edge is not
  a branch, and would be reported as a failed test rather than a second basin.
- **Ⓒ③ The reproduction.** Whichever start lands lower must reproduce this reference's banked
  `Σ = 0.400` `χ²` for that ruler to better than `1e-6` relative. If it does not, the profiler is not
  the one that produced the record and nothing below means anything.
- **Ⓓ④ THE VERDICT IS REGISTERED AS A CRITERION, NOT AN EXPECTATION.** I do **not** register which of
  60's three outcomes obtains, because I do not know and the honest form is a stated rule:
  **same branch** iff `|ΔH0| < 0.5` km/s/Mpc **and** `|Δχ²| < 0.01`; **two branches** iff
  `|ΔH0| > 2.0` **and** `|Δχ²| > 0.01`; **anything else is the third outcome** and is reported as
  neither. ⌗ *60 is right that `r7869`'s record held each ruler's best fit and no branch scan, so
  "one branch to 0.60 eV" claimed more than it showed. This item is the scan that claim needed, and
  registering an expected answer would repeat the error in the other direction.*
- **Ⓔ⑤** Both rulers are run, and the two rulers may disagree about the verdict — which would itself
  be the finding, since the basin would then be a property of the ruler's treatment.

## ⑫ CAMB's RESPONSE BY SOURCE TERM

- **Ⓕ⑥ THE CLOSURE GATES EVERYTHING, as the order requires.** The four terms, fed back through
  `set_custom_scalar_sources` and summed, must reproduce CAMB's own lensed-scalar TT over
  `ℓ = 100`–`420` to better than **`1e-3` relative**. ⚠ **If closure fails, NO term is reported** —
  not one ratio, not as provisional. A decomposition that does not sum to the thing it decomposes is
  not a decomposition, and reading its terms would be the same error as reading `r7869`'s per-bin
  share after it failed to close on the measured change.
- **Ⓖ⑦ Each term's ratio, once closure holds.** `D_ℓ(Σ)/D_ℓ(0) − 1` per term at `Σ = 0.30` and
  `0.60`, over `ℓ = 100`–`420`. Registered: at least two terms differ from each other by more than
  `1e-2` somewhere in that range at `Σ = 0.60`, so the total's oscillation is not one term's.
- **Ⓗ⑧ The early/late ISW split: attempted, and reported honestly either way.** I will try a window
  in the scale factor inside the ISW integrand. **If CAMB's source compiler takes it**, both halves
  are given and their sum must return the undivided ISW term to `1e-3`. **If it does not**, I say so
  in one line and give the undivided ISW term only — I will not hand-build an ISW by integrating
  anything myself, which is the substitute the order forbids.
- **Ⓘ⑨ The custom-source path must reproduce the DEFAULT path first.** Before any term is split, the
  sources returned unmodified by `get_scalar_temperature_sources()` and pushed through
  `set_custom_scalar_sources` must give back CAMB's own TT to `1e-3`. ⌗ *This is the same positive
  control the `MassiveNuMethod` knob needed at `r7871`: a mechanism that silently does nothing
  produces a beautifully closing split of the wrong thing.*

## ⌗ WHAT IS NOT ASKED AND NOT DONE

No limit, no `χ²` scan beyond `Σ = 0.400`, no instrument run, and no per-term comparison against 60's
own — 69 has 60 supplying theirs. No substitute for anything CAMB declines to give.
