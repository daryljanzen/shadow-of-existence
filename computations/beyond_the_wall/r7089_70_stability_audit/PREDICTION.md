# r7089 (70) — the audit of the stability verdict, which rests on a banded statistic

*Pre-registered before any run of the instrument. The order is `FOR_70.md` `r7089` Q1, and the object is `receipts/P15_CR_cosmology/P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting.py`. I name the statistic's error structure, then test whether "nothing moves it" is stability or insensitivity. **No prose is edited, and no other seat's receipt or bank is touched.***

## What is already established by reading, stated before any run

- **The floor's provenance.** `r6911`'s 0.6 % is the largest of:
  - the estimator's bias in reading back one KNOWN injected contrast factor, 1.040, at three rungs (1.039, 1.046 and 1.038);
  - a resample null (0.9996 and 0.9975).

  It is **one injected amplitude on one source**: a **bias (accuracy) figure for reading a difference between two arms**. It is not a resolution limit on a step.
- **The sweep is deterministic.** It projects an analytic injected source, so a step between two refinements is resolved to the banked precision of about 1e−12, not to 0.6 %.
- **The statistic is a ratio of the two arms**, `Σ A·B / Σ B·B` over q ∈ [0.85, 5.75], each arm run at the same setting. A numerical error that moves both arms alike cancels in it.
- On `NK` the arm is byte-identical across the refinements, because it is inert by construction. **On that one axis, cancellation is impossible**, and the ratio's step is the control's own movement (about 1e−10 relative, from the banked table).

## What is measured, if the instrument runs here in reasonable time

`ACOUSTIC_two_arm.py` is run with `SRCINJ=fixed` and the launcher's own environments, to a scratch directory outside the repository, on a reduced set of runs:

1. **PER-ARM MOVEMENT, the cancellation test.** For each arm and each refinement axis available in budget, I compute the arm's **self-ratio**: the same `Σ A·B / Σ B·B` with A the refined run and B the same arm's base. I compare it with the cross-arm ratio's step on that axis.
   - If the per-arm steps are of the same order as the cross-arm step, each arm is itself stable and **nothing is cancelling**.
   - If they are much larger, the ratio's stability is **common-mode cancellation**: stability of the ratio, but not of either arm.
2. **RESPONSIVENESS, the insensitivity test.** One arm only is deliberately under-resolved on the `η` grid (`NLOS` and `NLOSW` well below the base), and the other is held at base. The question is whether the cross-arm ratio moves by **more than the floor** under a known integration defect on one arm.
   - If it does, the statistic can see the defect class the sweep guards against, and a 0.008 % step is evidence of stability.
   - If it does not, the stability verdict is insensitivity for that class.
3. **BAND-RESOLVED STEPS.** For the same pairs, I compute the ratio per acoustic band (one period of q each). This tests whether the scalar's 0.008 % hides opposing movements across bands. That is the effective-count question asked of a stability claim.

## Outcomes, the one that costs another seat most first

1. **The cancellation test shows per-arm steps far above the cross-arm step** (more than ×10), or the **responsiveness test shows the ratio blind** to a gross one-arm defect. Either way, the paper's "nothing moves it" overstates, and that routes to 66. **Predicted: neither.** The per-arm steps are predicted within ×3 of the cross-arm steps, and a gross one-arm `η` under-resolution is predicted to move the ratio by **more than 0.6 %**. Both are guesses.
2. **Band-resolved steps larger than the scalar step by more than ×10 in some band.** **Predicted: no**, within ×10.
3. **The floor.** **Predicted:** its single-point provenance does **not** bear on the verdict. The verdict's two halves are, first, every step under a threshold, which survives any threshold ≥ 0.01 %, and second, the sign-based turnover rule, which is limited by precision, not by the floor. I state this as reasoning, which outcome 2 of the run can only support, not prove.
4. **UNMEASURED**, if a base run here exceeds about 60 minutes. Then items 1–3 are reported as not run, and the audit is the reading above alone.
