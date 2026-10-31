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
import json
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

    # ---- ⓸ AND THE REFIT HALF OF THE PAIR, WHICH CORRECTS A REASON I PUBLISHED AT `.29` -------
    # ⛔ At `.29` I argued ⑵ could not be landed alone because moving the no-fit ratio to 1.41 while
    #   the refit's 1.57 stood would say "refitting makes the arm worse, which a refit cannot do".
    #   ** That reason is WRONG. **  Both figures are RATIOS against a control that is refitted too,
    #   so the ratio can RISE while both arms' chi^2 FALL.  The conclusion -- that the pair must move
    #   together -- survives; the reason does not.  ⇒ Measured here instead of argued.
    #   `cc66_r185_verify_*` are the spectra at each arm's OWN refit minimum: the arm of record's is a
    #   different point from the namesake's (68.57073/0.291246/0.021643/1.015066 against
    #   68.5898/0.287754/0.0206020/0.991504), verified by `refit_grid_leafrec1/verify_cr.npz`.
    V_CTL, V_NSK, V_AOR = 'cc66_r185_verify_lcdm', 'cc66_r185_verify_cr', 'cc66_r185_verify_cr_leafrec1'
    RCPT_REFIT = {'ctl': 186.51, 'nsk': 292.42}      # the refit's own reported chi^2, 185 bins

    def refit_chi2(tag):
        # ⛔ the verify banks are UNLENSED model spectra and the refit's chi^2 is scored with the
        #   derived lensing operator applied -- `mb_of` in the position receipt does this.  Omitting
        #   it put the control at 592.81 against its own 186.51, and the instrument's own gate caught
        #   it as "a refit raised a chi^2, which cannot happen".
        ls, Dl = load(tag)
        mb = CS.bin_spectrum(ls, Dl * np.interp(ls, lg, rat))
        k = np.isfinite(mb) & (CS.BIN_LO >= 100) & (CS.BIN_HI <= 1996)
        k &= np.isfinite(CS.bin_spectrum(*(lambda t: (t[0], t[1] * np.interp(t[0], lg, rat)))(
            load(V_CTL))))
        m, d = mb[k], CS.X_DATA[k]
        Fi = np.linalg.inv(CS.COV_TT[np.ix_(k, k)])
        A = float(m @ Fi @ d / (m @ Fi @ m))
        r = A * m - d
        return float(r @ Fi @ r), int(k.sum())

    rc, nb = refit_chi2(V_CTL)
    rn, _ = refit_chi2(V_NSK)
    ra, _ = refit_chi2(V_AOR)
    print(f"\n  ⓸ THE REFIT HALF, each arm at its OWN refit minimum, {nb} bins:")
    print(f"       control        {rc:8.2f}  {rc / nb:.3f}/bin")
    print(f"       namesake arm   {rn:8.2f}  {rn / nb:.3f}/bin   -> {rn / rc:.3f}x")
    print(f"       arm of record  {ra:8.2f}  {ra / nb:.3f}/bin   -> {ra / rc:.3f}x")
    for nm, got, want in (('control', rc, RCPT_REFIT['ctl']), ('namesake', rn, RCPT_REFIT['nsk'])):
        if abs(got - want) > 0.05:
            fails.append(f"the refit's own {nm} chi^2 is not reproduced: {got:.2f} against {want}")
    print(f"\n  ⛔ SO THE PAPER'S PAIR INVERTS: no-fit {R_L_AOR:.2f}x then refit {ra / rc:.2f}x on the "
          f"arm of record, against no-fit {R_L_NSK:.2f}x then refit {rn / rc:.2f}x on the namesake.")
    print(f"     *Freedom CLOSED {100 * (1 - (rn / rc - 1) / (R_L_NSK - 1)):.0f} per cent of the gap "
          f"on the namesake and WIDENS it by {100 * ((ra / rc - 1) / (R_L_AOR - 1) - 1):.0f} per cent "
          f"on the arm of record -- and both arms' chi^2 still FALL under the refit "
          f"({aL:.1f}->{ra:.1f} for the arm, {cL:.1f}->{rc:.1f} for the control), which is why the "
          f"ratio may rise without anything being impossible.*")
    if not (rn / rc < R_L_NSK and ra / rc > R_L_AOR):
        fails.append("the refit pair does not invert as measured -- re-read ⓸")
    # ⛔ AND THE ARM-OF-RECORD REFIT MUST BE AT ITS OWN FITTED POINT, which is the fact that made this
    #   measurement trustworthy and was NOT gated until it was perturbed: swapping `V_AOR` to the
    #   namesake bank left every limb above passing, because the namesake's refit ratio ALSO exceeds
    #   the arm of record's no-fit ratio.  ⇒ The bank's own manifest point is compared with the
    #   NAMESAKE's fitted minimum and required to differ, and the two spectra required to be distinct.
    # ⌗ and a MISSING manifest is reported, not raised: perturbed, swapping `V_AOR` to the namesake
    #   bank crashed with a KeyError, which is an instrument that stops rather than one that measures.
    _z = np.load(os.path.join(SPEC, V_AOR + '.npz'), allow_pickle=True)
    if 'manifest' not in _z.files:
        fails.append(f"{V_AOR} carries no manifest, so its fitted point cannot be checked -- it is "
                     f"not an arm-of-record bank")
        _man, _pt = {}, {'CRH0': 0.0, 'CROM': 0.0, 'WBH2': 0.0, 'NS': 0.0}
    else:
        _man = json.loads(str(_z['manifest']))
        _pt = _man['point']
    _nsk_best = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                     'refit_grid', 'best_cr.npy'))
    _mine = np.array([_pt['CRH0'], _pt['CROM'], _pt['WBH2'], _pt['NS']], float)
    print(f"\n  the arm of record's refit point {list(np.round(_mine, 6))} against the NAMESAKE's "
          f"fitted minimum {list(np.round(_nsk_best, 6))}")
    if not (_man.get('namesake') == V_NSK
            and bool(np.all(np.abs(_mine / _nsk_best - 1.0) > 1e-5))
            and load(V_AOR)[1].tobytes() != load(V_NSK)[1].tobytes()
            and abs(ra / rc - 1.596) < 5e-3):
        fails.append(f"the arm-of-record refit is not at its own fitted point, or its ratio "
                     f"{ra / rc:.4f} is not 1.596 -- the bank may be the namesake's")
    if not (ra < aL and rc < cL):
        fails.append("a refit raised a chi^2, which cannot happen -- the banks are mismatched")

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
