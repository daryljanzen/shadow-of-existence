"""
P15_the_acceptance_does_not_move_under_refinement_and_three_of_the_twelve_axes_could_not_have_moved_it

** THE KERNEL'S k-ACCEPTANCE DOES NOT MOVE UNDER ANY REFINEMENT THAT CAN MOVE IT -- and three of the twelve
   axis-arm pairs COULD NOT HAVE MOVED IT, so their silence is not convergence and is not reported as it. **

`r7049` offered the observation this answers: *"A_l is a sharper probe of the same thing and it is now free:
it is built from W_l = G_l^2 dk/k over the k-grid, so truncating k_max truncates the window the law
integrates over -- and A_l carries NO FITTED AMPLITUDE to absorb the truncation, where a height ratio
does."*  It cost no re-run: `GRIDSAVE` writes the background `A_l` needs -- vis(eta), x0(eta), k, dk, r_s* --
in 1.45 s per configuration WITHOUT computing a spectrum at all.

⛔⛔ AND THE FINDING THAT MATTERS IS THE ONE THAT NEARLY DID NOT HAPPEN.  THE READER WAS ABOUT TO PRINT
   "THE ACCEPTANCE HAS STOPPED MOVING, AT THE FLOOR" FOR THREE AXES WHOSE INPUTS NEVER MOVED.
  `A_l` is built from the background alone.  So an axis that leaves every one of `k`, `dk`, `eta`, `x0`,
  `vis` byte-identical CANNOT move it, and its sequence reads `base=X  s1=X  s2=X`: step 0.0000 per cent,
  three points, not monotone, and the verdict falls straight through to converged.  Two such axes exist
  here and they are NOT the same defect:
    ① `NK` ON THE ARM.  The arm's k ladder is sqrt(L(L+2))*stretch out to `KMAXL` and `NK` is only a
      decimation cap that is never reached -- 1452 modes at `base`, `nk15` and `nk20` alike.  *** On the
      CONTROL the same knob takes 2547 modes to 3822 to 5094 and the spectra differ outright, which is
      what makes the arm's silence a reading rather than a broken test. ***
    ② `LSTEP` ON BOTH ARMS.  `A_l` is read at the SAME multipoles at every setting by construction, so the
      reported ell grid cannot enter it at all.  *This one is a property of the QUESTION, not of the arm.*
  ⇒ *** AN AXIS WHOSE INPUTS DO NOT MOVE IS NOT A CONVERGED AXIS, and the cheapest way for a sequence to
      look converged is to be asked a question the instrument cannot answer. ***  That is this row's
      recurring defect once more -- an instrument not matching its question -- and this time it was caught
      in the READER, before the number reached a reply.
  ⌗ The test is therefore read off the inputs and not held as a list: an axis is inert for an arm when every
  configuration in it digests identically to `base`.  A list would have to be remembered and would not
  notice a knob that starts mattering; ** gate ⓪ refuses to print if that test is not discriminating. **

⛭ WHAT THE ARM'S INERT NK COST AND BOUGHT.  Six of `r7041`'s 72 configurations were dropped as the same
computation repeated -- 588 slices to 557 -- on evidence banked here at the SPECTRUM level, not merely at
the grid: `real_cr_nk15_k0` and `real_cr_nk20_k0` against `real_cr_base_k0` at max|Dl| = 0 exactly, with an
identical ell list.  *The sweep reads the arm's `base` for them as an IDENTITY, under a gate.*

⛔ WHAT IS NOT CLAIMED.  ** This is NOT `r7041`'s sweep and does not substitute for it. **  The sweep asks
what the RETENTION and the peak heights do, measured on spectra; this asks what the kernel's k-acceptance
does, computed from the background.  *A converged acceptance with an unconverged retention would itself be
a finding, and the two are reported separately -- as this receipt's own pre-registration required.*  Nor is
a nine-of-twelve reading a convergence claim for the ROW: the pre-registered criteria are printed beside
every axis unaltered, including "a sequence that has not turned over is not converged whatever its last
step" and "a two-point axis cannot turn over".  Nothing here says which cosmology is right.
"""
# ⛭ ** COST, MEASURED, AND WHY IT IS NOT DECLARED LONG. **  354 s end to end on this container WITH FOUR
#   instrument solvers live on four cores -- so this is a CONTENDED reading, not a standalone one, and it
#   sits inside the 600 s cap with 41 per cent of margin.
#   ⌗ *`r6476`'s two declarations set the convention: measure STANDALONE, multiply by `C63`'s own measured
#   1.7x spread under `--jobs 4`, and declare if the product leaves the cap.  A contended figure is already
#   roughly that product, so applying 1.7x to this one would double-count the spread and manufacture
#   headroom from a number nobody measured.*  ⇒ ** Not declared.  If the runner reports it SLOW, that is the
#   measurement that would justify a declaration -- made on the runner rather than guessed here.**
#   The dominant cost is gate ⓷: `spherical_jn` at up to l = 1735 over the full (eta x k) grid for four
#   configurations, the largest of them 5094 modes by 560 eta points.
import hashlib
import os

import numpy as np
from scipy.special import spherical_jn

FAILS = []


def check(name, cond, got=None):
    ok = bool(cond)
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}" + (f"   {got}" if got is not None else ""))
    if not ok:
        FAILS.append(name)


def bail(msg):
    print(f"\n  ⛔ {msg}")
    print(f"\nGATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TAGS = ['base', 'kfac26', 'kfac32', 'kfac40', 'nk15', 'nk20',
        'nlos1120', 'nlos2240', 'nlosw9', 'nlosw12', 'nlosf90', 'lstep4']
KEYS = ('k', 'dk', 'eta', 'x0', 'vis')
SEQ = {'k_max via KFAC': ['base', 'kfac26', 'kfac32', 'kfac40'],
       'the mode count NK': ['base', 'nk15', 'nk20'],
       'the eta resolution NLOS': ['base', 'nlos1120', 'nlos2240'],
       'the eta half-width NLOSW': ['base', 'nlosw9', 'nlosw12'],
       'the eta split NLOSF': ['base', 'nlosf90'],
       'the reported ell grid LSTEP': ['base', 'lstep4']}
INERT_CLAIMED = {('cr', 'the mode count NK'),
                 ('cr', 'the reported ell grid LSTEP'),
                 ('lcdm', 'the reported ell grid LSTEP')}
FLOOR = 0.006                      # r6911's, on a KNOWN injected contrast
R6919_NARROWING = 0.128            # r6919's INDEPENDENT dr_s/dchi reading

print(__doc__)
print("=" * 100)

NEED = ['r7041_accept_digest.npz', 'r7041_accept_Al.npz',
        'r7041_accept_sample.npz', 'r7041_accept_nk_slices.npz']
for n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{n}`",
          os.path.exists(os.path.join(SP, n)), n)
if FAILS:
    bail("A BANK THIS RECEIPT READS IS NOT ON DISK, so nothing is read and this receipt FAILS rather\n"
         "     than reporting the parts it could run as the whole.")

DG = np.load(os.path.join(SP, 'r7041_accept_digest.npz'))
AL = np.load(os.path.join(SP, 'r7041_accept_Al.npz'))
SM = np.load(os.path.join(SP, 'r7041_accept_sample.npz'))
NKS = np.load(os.path.join(SP, 'r7041_accept_nk_slices.npz'))


def inert(arm, seq):
    """an axis is inert for an arm when EVERY configuration in it digests identically to its first"""
    return all(all(str(DG[f'{arm}_{t}_{q}']) == str(DG[f'{arm}_{seq[0]}_{q}']) for q in KEYS)
               and str(DG[f'{arm}_{t}_r_s']) == str(DG[f'{arm}_{seq[0]}_r_s'])
               for t in seq[1:])


print("\n  ⛭ GATE ZERO -- THE INERT TEST MUST DISCRIMINATE, OR NOTHING BELOW IS PRINTED")
print("  " + "-" * 98)
print("  *A test that answers the same way on every axis is not a test.  This one is required to fire on")
print("  the three pairs claimed inert and to stay silent on the other nine, BEFORE any A_l is read.*")
fired = {(a, n) for a in ('cr', 'lcdm') for n, s in SEQ.items() if inert(a, s)}
check("⓪ the inert test fires on EXACTLY the three axis-arm pairs claimed, and on no other of the twelve",
      fired == INERT_CLAIMED, f"fired on {len(fired)} of 12: {sorted(fired)}")
check("⓪ and it is discriminating rather than constant -- it both fires and stays silent",
      0 < len(fired) < 12, f"{len(fired)} fired, {12 - len(fired)} did not")
if FAILS:
    bail("GATE ZERO FAILED: the test this receipt's central claim rests on does not separate the\n"
         "     axes it is supposed to separate, so NO acceptance reading is printed.")

print("\n  ⓵ THE INERT CLAIM IS A BYTE CLAIM, AND SO IS ITS CONTROL")
print("  " + "-" * 98)
for arm in ('cr', 'lcdm'):
    for name, seq in SEQ.items():
        moved = [t for t in seq[1:]
                 if any(str(DG[f'{arm}_{t}_{q}']) != str(DG[f'{arm}_{seq[0]}_{q}']) for q in KEYS)]
        if (arm, name) in INERT_CLAIMED:
            check(f"⓵ `{arm}` {name}: every input digests IDENTICALLY to base -- it cannot move A_l",
                  not moved, f"{len(seq) - 1} refinement(s), 0 moved an input")
        else:
            check(f"⓵ `{arm}` {name}: at least one input DOES move, so the axis is a real question",
                  len(moved) == len(seq) - 1, f"{len(moved)} of {len(seq) - 1} moved an input")

print("\n  ⓶ NK ON THE ARM AT THE SPECTRUM, NOT ONLY AT THE GRID -- AND THE CONTROL THAT MOVES")
print("  " + "-" * 98)
for nm in ('nk15', 'nk20'):
    d = float(np.max(np.abs(NKS[f'arm_{nm}_Dl'] - NKS['arm_base_Dl'])))
    check(f"⓶ arm `{nm}` against arm `base`: max|Dl| is EXACTLY zero and the ell list is identical",
          d == 0.0 and np.array_equal(NKS[f'arm_{nm}_ls'], NKS['arm_base_ls']),
          f"max|Dl| = {d:.3e}")
cd_ = float(np.max(np.abs(NKS['ctl_nk15_Dl'] - NKS['ctl_nk20_Dl'])))
check("⓶ and on the CONTROL the same two settings give DIFFERENT spectra -- the test is not vacuous",
      cd_ > 0.0, f"control max|Dl(nk15) - Dl(nk20)| = {cd_:.4e}")

print("\n  ⓷ A_l RE-DERIVED FROM THE BANKED BACKGROUND -- THE BANK'S OWN NUMBERS ARE NOT TRUSTED")
print("  " + "-" * 98)
print("  *Four configurations carry their full background, so A_l is recomputed from vis, x0, k and dk")
print("  rather than read.  The KFAC axis is walked end to end this way on both arms.*")
for arm in ('cr', 'lcdm'):
    for t in ('base', 'kfac40'):
        k, dk = SM[f'{arm}_{t}_k'], SM[f'{arm}_{t}_dk']
        ee, x0, v = SM[f'{arm}_{t}_eta'], SM[f'{arm}_{t}_x0'], SM[f'{arm}_{t}_vis']
        RS = float(SM[f'{arm}_{t}_r_s'])
        ls, banked = AL[f'{arm}_{t}_ls'], AL[f'{arm}_{t}_A']
        got = np.empty(len(ls))
        for i, l in enumerate(ls):
            J = spherical_jn(int(l), k[None, :] * x0[:, None])
            G = np.trapezoid(v[:, None] * J, ee, axis=0)
            W = G ** 2 * dk / k
            got[i] = abs(np.sum(W * np.exp(2j * k * RS))) / float(W.sum())
        e = float(np.max(np.abs(got - banked)))
        check(f"⓷ `{arm}` `{t}`: A_l recomputed from the background reproduces the bank at {len(ls)} multipoles",
              e < 1e-12, f"max|recomputed - banked| = {e:.2e}")

print("\n  ⓸ WHAT THE ACCEPTANCE DOES ON EVERY AXIS THAT CAN MOVE IT -- WORST SINGLE MULTIPOLE")
print("  " + "-" * 98)
print(f"  *Against r6911's {FLOOR * 100:.1f} per cent floor, measured on a KNOWN injected contrast.  The")
print("  worst single multipole is printed, not the mean over the range: a mean can hide a moving tail.*")
worst_all = 0.0
for arm in ('cr', 'lcdm'):
    for name, seq in SEQ.items():
        if (arm, name) in INERT_CLAIMED:
            print(f"    [--]    `{arm}` {name}: ⛔ INERT BY CONSTRUCTION -- not read as a sequence")
            continue
        b = AL[f'{arm}_{seq[0]}_A']
        w = max(float(np.max(np.abs(AL[f'{arm}_{t}_A'] - b) / np.abs(b))) for t in seq[1:])
        worst_all = max(worst_all, w)
        pts = len(seq)
        note = ("" if pts > 2 else
                "  ⌗ TWO POINTS ONLY -- inside the floor but a two-point axis cannot turn over")
        check(f"⓸ `{arm}` {name}: worst single multipole {w * 100:.5f}% is inside the floor{note}",
              w < FLOOR, f"{FLOOR / w:.0f}x inside" if w > 0 else "exactly 0")
check("⓸ and the LARGEST excursion anywhere among the nine axes that can move it is inside the floor",
      worst_all < FLOOR, f"worst of all nine = {worst_all * 100:.5f}%, {FLOOR / worst_all:.0f}x inside")

print("\n  ⓹ THE ARM-TO-CONTROL ACCEPTANCE RATIO, AT EVERY SETTING, AGAINST AN INDEPENDENT READING")
print("  " + "-" * 98)
print("  *This is the quantity the law's prediction rides on.  `r6919` measured the arm's chi-extent")
print("  narrowing as 12.8 per cent from dr_s/dchi, by a route that never computes an acceptance.*")
nar = []
for t in TAGS:
    sc, sa = float(AL[f'lcdm_{t}_span'][0]), float(AL[f'cr_{t}_span'][0])
    nar.append(1 - sa / sc)
    print(f"      {t:10s} control {sc:.4f}  arm {sa:.4f}   arm narrower by {nar[-1] * 100:5.2f}%")
sprd = float(np.max(nar) - np.min(nar))
check("⓹ the narrowing is the SAME at all twelve settings -- it is not an artefact of one grid",
      sprd < 0.001, f"spread across twelve settings = {sprd * 100:.4f} percentage points")
check("⓹ and it agrees with r6919's independent dr_s/dchi reading of 12.8%",
      abs(float(np.mean(nar)) - R6919_NARROWING) < 0.01,
      f"{np.mean(nar) * 100:.2f}% against 12.8%, {abs(np.mean(nar) - R6919_NARROWING) * 100:.2f} pp apart")

print("\n  ⓺ SCOPE, GATED RATHER THAN ASSERTED IN PROSE ALONE")
print("  " + "-" * 98)
# ⛭ ** THE SCOPE TEST IS NORMALISED, AND THAT IS NOT A LOOSENING -- IT IS WHAT MAKES IT A TEST OF THE
#   CLAIM RATHER THAN OF THE TYPESETTING. **  *The first version compared raw substrings and failed twice on
#   its own docstring: one sentence is written in capitals for emphasis, and another is wrapped across a
#   line so the phrase contains a newline and two spaces.  Neither is a missing claim.*
#   ⇒ A gate that fires when prose is re-flowed is a gate that will fire spuriously and be silenced, which
#   is worse than no gate.  The sentence tested is still the exact sentence; only case and run-of-whitespace
#   are folded first.
_d = ' '.join(__doc__.lower().split())


def says(phrase):
    return ' '.join(phrase.lower().split()) in _d


check("⓺ the receipt states in its own text that this is NOT the sweep and does not substitute for it",
      says("NOT `r7041`'s sweep and does not substitute for it"))
check("⓺ and that an inert axis is not reported as converged",
      says('an axis whose inputs do not move is not a converged axis')
      and says('is not convergence and is not reported as it'))
check("⓺ and the pre-registered criteria are carried here unaltered, not loosened after the numbers",
      says('a sequence that has not turned over is not converged whatever its last step')
      and says('a two-point axis cannot turn over'))

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print("  ⛭ The acceptance does not move on any of the NINE axes that can move it: the largest excursion at")
print("     any single multipole is inside r6911's floor by two orders of magnitude.  THREE of the twelve")
print("     axis-arm pairs could not have moved it and are reported inert, never converged.")
print("  ⛔ AND THIS IS NOT THE SWEEP.  The retention and the peak heights are measured on spectra and are")
print("     r7041's own question, still running.  A converged acceptance with an unconverged retention")
print("     would be a finding in itself, which is why the two are reported apart.")
