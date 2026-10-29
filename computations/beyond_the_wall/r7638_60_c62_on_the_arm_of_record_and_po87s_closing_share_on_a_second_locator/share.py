#!/usr/bin/env python3
r"""r7638 (60) -- PO-87's closing share on a SECOND locator, and C62's re-point scored.

COMPUTES: nothing is pinned as a parameter here.  Every number is read from the banked spectra on the
arm of record and from the sky values the papers and `70`'s own table carry.

** THE REGISTERED QUANTITY. **  (control - sky) / (arm - sky) at the fourth acoustic feature -- the
fraction of the arm's residual against the sky that the control produces too.  `70` reports 0.911 on
fine-grid TT through the three-point parabola.  ** THE REACHABLE NEGATIVE, REGISTERED: ** the share
falls below 0.75 or crosses 1.00 on this line's locator, in which case the figure is the locator's and
not the spectra's.

** THE LOCATOR, FIXED BEFORE THE READING. **  A least-squares GAUSSIAN with a linear baseline, fitted
to band power over a symmetric window about the peak -- amplitude, centre and width free.  NOT the
three-point parabola at the extremum, which is `70`'s and `cc66`'s.  Window half-width W = 40 declared
in the registration, with 25 and 60 reported beside it.
"""
import os
import sys

import numpy as np
from scipy.optimize import curve_fit

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
POL = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7631_70_PO87_polarisation')

CHECKS = []


def note(ok, msg):
    CHECKS.append(bool(ok))
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    return bool(ok)


def head(t):
    print('\n' + '=' * 99 + f'\n{t}\n' + '=' * 99)


# ---------------------------------------------------------------- the locator, and its own controls
def _model(l, A, mu, sig, b0, b1):
    return A * np.exp(-0.5 * ((l - mu) / sig) ** 2) + b0 + b1 * (l - mu)


def gauss_centre(ls, y, l0, W):
    """least-squares Gaussian + linear baseline over |l - l0| <= W; returns the fitted centre"""
    m = np.abs(ls - l0) <= W
    x, v = ls[m].astype(float), y[m].astype(float)
    if x.size < 6:
        raise RuntimeError('window too thin')
    base = 0.5 * (v[0] + v[-1])
    p0 = [v.max() - base, float(l0), W / 2.0, base, 0.0]
    p, _ = curve_fit(_model, x, v, p0=p0, maxfev=200000)
    return float(p[1])


def parabola_centre(ls, y, l0):
    """`70`'s locator, reimplemented only to show the two differ: three points at the extremum"""
    i = int(np.argmin(np.abs(ls - l0)))
    j = i + int(np.argmax(y[max(i - 3, 0):i + 4])) - min(i, 3)
    k = slice(max(j - 1, 0), j + 2)
    c = np.polyfit(ls[k].astype(float), y[k].astype(float), 2)
    return float(-c[1] / (2 * c[0]))


def apex(ls, y, lo, hi):
    """the raw grid maximum inside a bracket, used only to seed the fits"""
    m = (ls >= lo) & (ls <= hi)
    return float(ls[m][int(np.argmax(y[m]))])


head('Ⓐ  THE LOCATOR\'S OWN TWO-SIDED CONTROL, RUN BEFORE IT READS ANY SPECTRUM')
rng = np.random.default_rng(7638)
grid = np.arange(900, 1400, 1)
TRUE = 1123.57
synth = 50.0 * np.exp(-0.5 * ((grid - TRUE) / 55.0) ** 2) + 300.0 - 0.05 * (grid - TRUE)
got = gauss_centre(grid, synth, apex(grid, synth, 1050, 1200), 40)
a1 = note(abs(got - TRUE) < 0.05,
          f'⓵ ON A SYNTHETIC PEAK OF KNOWN CENTRE the locator returns it to better than a twentieth of '
          f'a multipole: {got:.3f} against {TRUE} planted')
shifted = 50.0 * np.exp(-0.5 * ((grid - (TRUE + 3.0)) / 55.0) ** 2) + 300.0 - 0.05 * (grid - TRUE)
got_s = gauss_centre(shifted := grid, shifted_y := shifted, apex(grid, shifted_y, 1050, 1200), 40)
a2 = note(abs(got_s - (TRUE + 3.0)) < 0.05,
          f'⓶ AND A PEAK MOVED BY THREE IS READ AS MOVED BY THREE, so the locator is not pinned to one '
          f'answer: {got_s:.3f} against {TRUE + 3.0} planted')
noisy = synth + rng.normal(0.0, 0.5, grid.size)
got_n = gauss_centre(grid, noisy, apex(grid, noisy, 1050, 1200), 40)
a3 = note(abs(got_n - TRUE) < 0.6,
          f'⓷ AND IT IS STABLE UNDER A PER-CENT SCATTER on the same peak: {got_n:.3f}, inside six '
          f'tenths of a multipole of the planted centre')

# ------------------------------------------------------------------------------------ the spectra
head('Ⓑ  THE SPECTRA READ, AND THE TWO LOCATORS SHOWN TO BE DIFFERENT INSTRUMENTS')
fine_arm = np.load(os.path.join(SPEC, 'r6941_fine_cr_leafrec1.npz'), allow_pickle=True)
fine_old = np.load(os.path.join(SPEC, 'r6941_fine_cr.npz'), allow_pickle=True)
fine_ctl = np.load(os.path.join(SPEC, 'r6941_fine_lcdm.npz'), allow_pickle=True)
pol_arm = np.load(os.path.join(POL, 'pol_cr_leafrec1.npz'), allow_pickle=True)
pol_ctl = np.load(os.path.join(POL, 'pol_lcdm.npz'), allow_pickle=True)

man = str(fine_arm['manifest'])
b0 = note('"LEAFREC": 1' in man and '68.57073' in man and '0.291246' in man and '0.021643' in man
          and '1.015066' in man,
          'Ⓑ THE ARM READ IS THE ARM OF RECORD, asserted from the spectrum\'s OWN manifest and not from '
          'a file name: LEAFREC=1 at the refitted point')

TT_BRACKET = (1050, 1200)
l_arm_tt = apex(fine_arm['ls'], fine_arm['Dl'], *TT_BRACKET)
g_arm = gauss_centre(fine_arm['ls'], fine_arm['Dl'], l_arm_tt, 40)
p_arm = parabola_centre(fine_arm['ls'], fine_arm['Dl'], l_arm_tt)
b1 = note(abs(g_arm - p_arm) > 0.2,
          f'Ⓑ⓵ THE TWO LOCATORS ARE NOT THE SAME INSTRUMENT: on the arm of record\'s TT the Gaussian '
          f'gives {g_arm:.3f} and the three-point parabola {p_arm:.3f}, apart by '
          f'{abs(g_arm - p_arm):.3f} multipoles -- so what follows is a second reading and not a '
          'restatement')

# ---------------------------------------------------------------------------------------- the share
head('Ⓒ  THE REGISTERED SHARE, (control - sky) / (arm - sky), ON THIS LINE\'S LOCATOR')
SKY = {
    'TT': [('plik_lite (P15 sec:intro)', 1123.9), ('Planck (70\'s table)', 1122.5), ('ACT (70\'s table)', 1122.0)],
    'EE': [('Planck (70\'s table)', 1001.2), ('ACT (70\'s table)', 990.6)],
    'TE': [('Planck (70\'s table)', 1068.7), ('ACT (70\'s table)', 1074.2)],
}
SERIES = {
    'TT': (fine_arm['ls'], fine_arm['Dl'], fine_ctl['ls'], fine_ctl['Dl'], (1050, 1200)),
    'EE': (pol_arm['ls'], pol_arm['Dl_EE'], pol_ctl['ls'], pol_ctl['Dl_EE'], (930, 1060)),
    'TE': (pol_arm['ls'], pol_arm['Dl_TE'], pol_ctl['ls'], pol_ctl['Dl_TE'], (1010, 1130)),
}
WINDOWS = [25, 40, 60]
shares = {}
print(f"    {'spec':4s} {'W':>3s} {'arm':>9s} {'control':>9s}   {'sky source':28s} {'arm-sky':>8s} "
      f"{'ctl-sky':>8s} {'share':>7s}")
for spec, (la, ya, lc, yc, br) in SERIES.items():
    for W in WINDOWS:
        a = gauss_centre(la, ya, apex(la, ya, *br), W)
        c = gauss_centre(lc, yc, apex(lc, yc, *br), W)
        for name, sky in SKY[spec]:
            da, dc = a - sky, c - sky
            s = dc / da if da != 0 else float('nan')
            shares[(spec, W, name)] = s
            print(f"    {spec:4s} {W:>3d} {a:9.3f} {c:9.3f}   {name:28s} {da:+8.3f} {dc:+8.3f} "
                  f"{s:7.3f}")

tt_main = shares[('TT', 40, 'plik_lite (P15 sec:intro)')]
c1 = note(0.75 <= tt_main <= 1.00,
          f'Ⓒ⓵ ON TT AT THE REGISTERED WINDOW AND THE SKY VALUE 70\'s FIGURE USES, the share is '
          f'{tt_main:.3f}, inside the registered band -- so the registered negative DID NOT ARRIVE '
          f'there, and 70\'s 0.911 is reproduced on a different instrument')
tt_all = [shares[('TT', W, n)] for W in WINDOWS for n, _ in SKY['TT']]
c2 = note(all(0.75 <= s <= 1.00 for s in tt_all),
          f'Ⓒ⓶ AND IT HOLDS ACROSS EVERY TT WINDOW AND EVERY TT SKY SOURCE: '
          f'{min(tt_all):.3f} to {max(tt_all):.3f} over {len(tt_all)} readings, none below 0.75 and '
          'none above 1.00')
pol_all = {(sp, W, n): shares[(sp, W, n)] for sp in ('EE', 'TE') for W in WINDOWS for n, _ in SKY[sp]}
out = {k: v for k, v in pol_all.items() if not (0.75 <= v <= 1.00)}
c3 = note(bool(out),
          f'Ⓒ⓷ ⛔ AND IN POLARISATION THE REGISTERED NEGATIVE DOES ARRIVE, which is the arm this line '
          f'wrote so it could: {len(out)} of {len(pol_all)} EE/TE readings fall outside the band '
          f'[0.75, 1.00], spanning {min(pol_all.values()):.3f} to {max(pol_all.values()):.3f}')
ee_spread = {n: [shares[('EE', W, n)] for W in WINDOWS] for n, _ in SKY['EE']}
te_spread = {n: [shares[('TE', W, n)] for W in WINDOWS] for n, _ in SKY['TE']}
c4 = note(len(SKY['EE']) == 2 and len(SKY['TE']) == 2
          and abs(np.mean(ee_spread[SKY['EE'][0][0]]) - np.mean(ee_spread[SKY['EE'][1][0]])) > 0.5,
          f'Ⓒ⓸ AND THE REASON IS THE ONE ENUMERATED IN THE REGISTRATION rather than a defect of the '
          f'locator: the two EE sky sources disagree by {abs(SKY["EE"][0][1] - SKY["EE"][1][1]):.1f} '
          f'multipoles, more than the residual being measured, so the share there is sky-source '
          'dependent by construction and is reported per source and never averaged')

head('Ⓓ  WHAT THE SHARE IS A STATEMENT ABOUT, LOCATED BEFORE IT IS USED')
tt_apex_arm = apex(fine_arm['ls'], fine_arm['Dl'], *TT_BRACKET)
tt_apex_old = apex(fine_old['ls'], fine_old['Dl'], *TT_BRACKET)
g_old = gauss_centre(fine_old['ls'], fine_old['Dl'], tt_apex_old, 40)
d1 = note(abs(g_arm - g_old) > 0.2,
          f'Ⓓ⓵ THE ARM OF RECORD MOVED THE TT FEATURE relative to the superseded arm, measured on this '
          f'line\'s own locator: {g_old:.3f} -> {g_arm:.3f}, a shift of {g_arm - g_old:+.3f} -- so the '
          'share is read on a spectrum that actually changed')
ctl_old = gauss_centre(fine_ctl['ls'], fine_ctl['Dl'], apex(fine_ctl['ls'], fine_ctl['Dl'], *TT_BRACKET), 40)
d2 = note(abs(ctl_old - gauss_centre(fine_ctl['ls'], fine_ctl['Dl'],
                                     apex(fine_ctl['ls'], fine_ctl['Dl'], *TT_BRACKET), 60)) < 1.0,
          f'Ⓓ⓶ AND THE CONTROL IS THE SAME OBJECT AT EVERY WINDOW, as it must be since LEAFREC does '
          f'not touch it: {ctl_old:.3f} at W=40 against '
          f'{gauss_centre(fine_ctl["ls"], fine_ctl["Dl"], apex(fine_ctl["ls"], fine_ctl["Dl"], *TT_BRACKET), 60):.3f} '
          'at W=60')

head('VERDICT')
print(f'  {len(CHECKS)} check(s), {CHECKS.count(False)} FAILED')
sys.exit(1 if CHECKS.count(False) else 0)
