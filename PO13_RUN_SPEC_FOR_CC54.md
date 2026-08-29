---
name: PO13_RUN_SPEC_FOR_CC54
description: PO-13's run specification for a node with compute — what to run, with which flags, and what each run decides. Held outside the corpus beside PO13_WORKING_STATE.
status: WORKING DOCUMENT — deliberately not a paper
# ⛭ r3548 (node 60): DECLARED-UNKNOWN, which is the true statement from this line — nobody
# here has brought this document current and its position is not known. Written because
# classifying it (it had gone unclassified since it was added, failing
# `classify_documents --check` on every push — and under the fast job's `set -e` that
# aborted the step before anything after it ran) made it visible to `check_currency` for
# the first time. ** Declaring ignorance is not declaring currency, and only the owning
# line can do the second. **
current: none
---

# PO-13 RUN SPEC — for a node with compute

Everything here is blocked in the chat environment by memory and turn limits, not by
uncertainty about what to run. The instrument is `computations/beyond_the_wall/ACOUSTIC_two_arm.py`.
Two env-gated flags exist, both DEFAULT OFF; with both unset the file is byte-identical in
behaviour to its pre-r3408 form.

## WHY THERE IS A NEW FLAG

The framework assigns the perturbations to the LEAF, in two places, verbatim:

- P15 `sec:properframe`: "a process running in the content --- rs, r_D, recombination,
  THE PERTURBATIONS --- takes the leaf's."
- P7's rate-rule remark: the same sentence, same assignment.

The instrument carried ONE rate (`Hphys`, "the ONLY place the two arms' rates differ"), and in
the CR arm that is the STACKING rate. So the perturbation sector ran on L1 where the framework
says L2. The discrepancy is |Jac - 1| = 0.128 at recombination, rising to 0.998 at a = 1e-9 ---
largest exactly where the driving is set.

`LEAFPERT=1` puts the perturbation equations on the leaf rate by an exact chain rule,

    dY/deta_stack = (H_stack / H_leaf) * F(Y, Hcal_leaf)

so every spline and grid is untouched and `rs`, `D_M` and the projection keep the stacking rate
(L1 --- which is what `sec:tensions` assigns them, and what the Tier-4 receipt
`P15_hubble_expansion_confrontation_v2.py` already does).

`GSRC=1` is the OTHER repair --- rescaling the Poisson source by rho_tot(full)/rho_tot(free).
It is retained for the record and IS NOT THE ONE THE FRAMEWORK SELECTS. Do not run it as a
candidate; run it only if someone asks what option (a) does.

## THE SELF-CHECK THAT IS ALREADY EXACT

In the `lcdm` arm, `Hphys` takes its `RAD_IN_RATE=True` branch, which is character-for-character
the same expression as `Hleaf`. So `Jac == 1` and `Hl_of == Hc_of` identically, and LEAFPERT is
provably a no-op there. RUN 1 below confirms it numerically; the proof does not depend on it.

## RUNS, IN ORDER, WITH WHAT EACH DECIDES

**RUN 1 --- the control, with the flag on. THE GATE ON EVERYTHING BELOW.**

    ARM=lcdm NK=900 LEAFPERT=1 python3 ACOUSTIC_two_arm.py

MUST return the control's validated first peak at l = 220 against the sky's 220.6, identical to
the flag-off control. It did not fit in memory in chat (2700 modes). **If this does not
reproduce the control, stop --- the implementation is wrong and nothing below means anything.**

**RUN 2 --- the measurement, and its continuum check.**

    ARM=cr LEAFPERT=1 python3 ACOUSTIC_two_arm.py
    ARM=cr LEAFPERT=1 NK=400 KCONT=1 python3 ACOUSTIC_two_arm.py

The ladder run returned, in chat: peaks 204, 516, 828, 1164; l_1/l_A = 0.6764; P1/P2 = 2.013;
P1/P3 = 2.373. Sky: 220.6, 538.1, 809.8; 0.7312; 2.217; 2.277. The KCONT run is NOT confirmation
of the physics --- it tests only whether the discrete ladder set the answer. For the baseline the
two agreed to the digit; that has not been shown for this configuration.

**RUN 3 --- OWED (624)'S PRECONDITION. DO THIS BEFORE READING ANY l_1 ABOVE.**

    ARM=cr LEAFPERT=1 SAVE=/tmp/lp.npz python3 ACOUSTIC_two_arm.py

then count EVERY local maximum below l = 500, at filter orders 1 through 4:

    from scipy.signal import argrelextrema as ar
    d = np.load('/tmp/lp.npz'); ls, Dl = d['ls'], d['Dl']
    for o in (1,2,3,4):
        print(o, [int(ls[q]) for q in ar(Dl, np.greater, order=o)[0] if ls[q] < 500])

r3325 found that undriven, DRC alone and DRE=0.42 each give ONE feature below l = 500 while both
couplings together give TWO. Baseline and GSRC both give two. **If LEAFPERT gives two, then 204
is not necessarily the first peak and comparing it to 220.6 is a category error --- the same
error made twice in chat.** If it gives ONE, that is itself a major result and should be reported
as such rather than folded into a peak-position claim.

**RUN 4 --- the DRE scan, abandoned in chat for want of compute.**

    for D in 0.42 0.50 0.60 0.70 0.80 0.90 1.00; do
      ARM=cr DRC=1 DRE=$D SAVE=/tmp/dre_$D.npz python3 ACOUSTIC_two_arm.py
    done

Count features below l = 500 for each, as in RUN 3, with LEAFPERT OFF (this scans the baseline's
structure). r3325 brackets the transition between DRE = 0.42 (one feature) and DRE = 1 (two).
**If a single feature BIFURCATES at a threshold, the second is interference between the two
driving couplings and is not a peak. If two are present throughout and one merely emerges from
under the other, both are real and 624's question changes shape.** Either outcome settles it.

Then repeat the scan with `LEAFPERT=1` --- if the leaf rate removes the bifurcation, that is the
cleanest possible statement of what was wrong.

## WHAT TO WRITE DOWN, AND WHERE

`PO13_WORKING_STATE.md`, under OWED (624) as its stated precondition. Report RUN 1 first and
plainly; if it fails, report only that. Do not report an improved `l_1` before RUN 3 has settled
which feature is the first peak.

## WHAT IS ALREADY SETTLED AND NEED NOT BE RE-DERIVED

Tiers 1--4 of the bottom-up audit are pushed (r3406, r3407) and clean: the field equations give
the kernel, the kernel's E=1 geodesic gives the rate, alpha comes from stellar ages and x_0 from
a pure late-time shape ratio in which the dimensionful prefactor cancels. `Omega_m` appears
nowhere in that chain. The leaf receipts already name their level and their rate. The Tier-4
projection receipt integrates `rs` UP TO `z_onset` on the stacking rate --- both of which I got
wrong in chat before the audit, and both of which the corpus had right.
