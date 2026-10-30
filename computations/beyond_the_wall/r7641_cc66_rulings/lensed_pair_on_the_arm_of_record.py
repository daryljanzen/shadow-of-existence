#!/usr/bin/env python3
r"""r7641+cc66 -- ** RULING ⑵ MEASURED, AND IT INVERTS, SO IT IS HELD. **

`r7641` ⑵ orders the full-range lensed receipt re-pointed onto the arm of record and the trio
`214.1 / 550.5 / 2.57` moved -- and makes it conditional: *"The clause 'lensing is worth
proportionally more to a spectrum whose peaks are already in place' is a claim. Keep it only if the
lensed ratio still exceeds the unlensed one on the arm of record. If it does not, report and hold."*

** IT DOES NOT, AGAINST THE COMPARISON THE PAPER ACTUALLY MAKES -- AND IT DOES, AGAINST THE ONE THE
RECEIPT GATES. **  Those are two different comparisons and the whole ruling turns on which is meant:
  ⒜ the paper's sentence pairs the 185-bin LENSED ratio against the 133-bin UNLENSED one.  On the
     namesake that is 2.57 against 1.98, so the lensed configuration is the UNFAVOURABLE one and
     is the one quoted.  ** On the arm of record it is 1.41 against 1.601 -- so the lensed
     configuration is the FAVOURABLE one and the sentence inverts. **
  ⒝ the receipt's own gate pairs LENSED against UNLENSED on the SAME 185 bins.  Namesake 2.57
     against 1.68; arm of record 1.41 against 1.35.  ** The claim's PHYSICS survives there -- the
     control still gains more from lensing than the arm does -- but the margin collapses from 53
     per cent to 4. **
⇒ *⒜ is a cross-configuration comparison, which the receipt itself warns against in the same
breath it makes it: "a number scored on one may not be quoted against the other".  So the inversion
is in a pairing that was already a licence defect, and ⒝ is the licensed form of the same claim.*

** WHAT THIS SCRIPT IS FOR. **  The move is large -- the arm's lensed chi^2 falls 550.5 -> 302.1 and
the ratio 2.57 -> 1.41 -- and `2.57` is carried by SEVEN corpus sites across THREE papers.  A number
that big does not get reported on one run's word, so every figure below is validated against a
figure computed somewhere else first: the receipt's own printed namesake row, and the 185-bin arm
value an already-landed receipt (`r7639+cc66.2`) computes independently.

Exits 1 if the namesake row is not reproduced, if the independently-landed cross-check is missed, or
if the inversion is not present on the arm of record.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                                # noqa: E402

CTL = 'cc66_lcdm_L2000'
NSK = 'cc66_cr_x_h686_L2000'
AOR = 'cc66_cr_x_h686_L2000_leafrec1'

# the receipt's own printed namesake row, and `r7639+cc66.2`'s independently computed arm-of-record
# 185-bin unlensed value -- both computed elsewhere, both required before anything below is believed
RCPT_NSK = {'ctl_u': 696.0, 'ctl_L': 214.1, 'arm_u': 1169.8, 'arm_L': 550.5, 'ratio_L': 2.57}
LANDED_AOR_ARM_U = 938.3175        # r7639+cc66.2, PART 2's own prose
LANDED_AOR_133 = 1.601078          # r7639+cc66.2: the 133-bin unlensed ratio on the arm of record
NSK_133 = 1.98                     # the paper's own figure, cc66.7


def load(tag):
    z = np.load(os.path.join(SPEC, tag + '.npz'))
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def lensing_ratio():
    """the SAME derived operator the receipt uses, on both arms"""
    pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * (0.674 ** 2) - 0.02237,
                           mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
    le, un = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    lg = np.arange(len(le))
    rat = np.ones_like(le)
    m = un > 0
    rat[m] = le[m] / un[m]
    return lg, rat


def score(tag, lg, rat):
    ls, Dl = load(tag)
    u = CS.chi2_of(ls, Dl)
    L = CS.chi2_of(ls, Dl * np.interp(ls, lg, rat))
    return u[0], L[0], u[1]


def main():
    fails = []
    lg, rat = lensing_ratio()
    cu, cL, cn = score(CTL, lg, rat)
    nu, nL, nn = score(NSK, lg, rat)
    au, aL, an = score(AOR, lg, rat)
    if not (cn == nn == an == 185):
        fails.append(f"the three spectra do not cover the same 185 bins: {cn}, {nn}, {an}")

    print(f"  {'':>24} {'bins':>5} {'unlensed':>10} {'/bin':>7} {'lensed':>10} {'/bin':>7}")
    for nm, (u, L, n) in (('control LCDM', (cu, cL, cn)), ('the NAMESAKE arm', (nu, nL, nn)),
                          ('the ARM OF RECORD', (au, aL, an))):
        print(f"  {nm:>24} {n:>5d} {u:>10.1f} {u / n:>7.2f} {L:>10.1f} {L / n:>7.2f}")

    # ---- ⓵ the namesake row, reproduced before anything is believed ---------------------------
    for k, got in (('ctl_u', cu), ('ctl_L', cL), ('arm_u', nu), ('arm_L', nL)):
        if abs(got - RCPT_NSK[k]) > 0.1:
            fails.append(f"the namesake row is not reproduced at {k}: {got:.1f} against "
                         f"the receipt's {RCPT_NSK[k]}")
    if abs(nL / cL - RCPT_NSK['ratio_L']) > 5e-3:
        fails.append(f"the namesake lensed ratio is {nL / cL:.3f}, not the receipt's 2.57")

    # ---- ⓶ and the arm of record against a figure a LANDED receipt computes --------------------
    print(f"\n  the arm of record's 185-bin unlensed chi^2 is {au:.4f}; `r7639+cc66.2` computes "
          f"{LANDED_AOR_ARM_U} independently")
    if abs(au - LANDED_AOR_ARM_U) > 0.05:
        fails.append(f"the arm-of-record 185-bin unlensed value {au:.4f} misses the landed "
                     f"{LANDED_AOR_ARM_U}")

    # ---- ⓷ THE TWO COMPARISONS, AND THE INVERSION ---------------------------------------------
    R_L_NSK, R_U_NSK = nL / cL, nu / cu
    R_L_AOR, R_U_AOR = aL / cL, au / cu
    print(f"\n  ⒜ the PAPER's pairing -- 185-bin LENSED against 133-bin UNLENSED:")
    print(f"       namesake      {R_L_NSK:.3f} against {NSK_133:.3f}  -> lensed is the "
          f"{'UNFAVOURABLE' if R_L_NSK > NSK_133 else 'FAVOURABLE'} one")
    print(f"       arm of record {R_L_AOR:.3f} against {LANDED_AOR_133:.3f}  -> lensed is the "
          f"{'UNFAVOURABLE' if R_L_AOR > LANDED_AOR_133 else 'FAVOURABLE'} one  ⛔ INVERTED")
    print(f"  ⒝ the RECEIPT's gate -- lensed against unlensed on the SAME 185 bins:")
    print(f"       namesake      {R_L_NSK:.3f} against {R_U_NSK:.3f}  -> the gap widens by "
          f"{100 * (R_L_NSK / R_U_NSK - 1):.0f} per cent")
    print(f"       arm of record {R_L_AOR:.3f} against {R_U_AOR:.3f}  -> the gap widens by "
          f"{100 * (R_L_AOR / R_U_AOR - 1):.0f} per cent  ⛭ the claim HOLDS, the margin collapses")
    print(f"\n  and lensing's own gain: the control falls by {cu / cL:.2f}x, the arm of record by "
          f"{au / aL:.2f}x, the namesake by {nu / nL:.2f}x")

    if not (R_L_NSK > NSK_133 and R_L_AOR < LANDED_AOR_133):
        fails.append("the inversion in the PAPER's pairing is not present -- re-read the ruling")
    if not (R_L_AOR > R_U_AOR and (R_L_AOR / R_U_AOR - 1) < 0.25 * (R_L_NSK / R_U_NSK - 1)):
        fails.append("the same-bins claim does not hold with a collapsed margin -- re-read ⒝")

    print()
    if fails:
        print("FAILED:")
        for f in fails:
            print("  - " + f)
        return 1
    print("  OK -- the namesake row is reproduced, the arm-of-record value matches a landed")
    print("  receipt's independent computation, and the inversion is present in the paper's pairing")
    print("  while the same-bins claim holds with a collapsed margin.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
