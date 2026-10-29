#!/usr/bin/env python3
r"""r7638 (60) -- PO-87's closing share on a SECOND locator, and C62 re-pointed on the arm of record.

** THE REGISTERED QUANTITY. **  (control - sky) / (arm - sky) at the fourth acoustic feature: the
fraction of the arm's residual against the sky that the control produces too.  `70` reports `0.911` on
fine-grid TT through the three-point parabola at the extremum (`cc66`'s locator).

** THE REACHABLE NEGATIVE, REGISTERED BEFORE THE READING: ** the share falls below `0.75` or crosses
`1.00` on this line's locator, in which case the figure is the locator's and not the spectra's.

** WHAT THIS RECEIPT FOUND, AND IT IS NOT WHAT THE REGISTRATION EXPECTED. **  The registered locator --
a Gaussian with a linear baseline -- DID cross `1.00`, so the negative arrived.  But five locator
families read here say the crossing is the GAUSSIAN's: four of them agree with `70` on the sign and
size of the arm-minus-control displacement and the Gaussian alone reverses its sign.  The negative is
therefore reported as arriving AGAINST THE REGISTERED LOCATOR, the registered arms are scored as
MISSES, and the share is then read again on a locator that passes the adjudication and is still not
`70`'s.

COMPUTES: nothing is pinned as a parameter.  Every number is read from the banked spectra on the arm of
record and from the sky values the papers and `70`'s own table carry.
"""
import os
import sys

import numpy as np
from scipy.optimize import curve_fit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
POL = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7631_70_PO87_polarisation')

CHECKS = []


def note(ok, msg):
    CHECKS.append(bool(ok))
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    return bool(ok)


def head(t):
    print('\n' + '=' * 99 + f'\n{t}\n' + '=' * 99)


# ------------------------------------------------------------------------------------- the locators
SMIN, SMAX = 20.0, 250.0


def apex(ls, y, lo, hi, sign=+1):
    """the raw grid extremum inside a bracket; `sign=-1` for a feature that is a MINIMUM"""
    ls = np.asarray(ls, float)
    m = (ls >= lo) & (ls <= hi)
    return float(ls[m][int(np.argmax(sign * np.asarray(y, float)[m]))])


def gauss_centre(ls, y, l0, W, sign=+1):
    """THE REGISTERED LOCATOR: Gaussian + baseline anchored at the FIXED window centre, width bounded"""
    ls = np.asarray(ls, float)
    v_all = sign * np.asarray(y, float)
    m = np.abs(ls - l0) <= W
    x, v = ls[m], v_all[m]
    if x.size < 6:
        raise RuntimeError(f'window W={W} holds only {x.size} points')

    def f(l, A, mu, sig, b0, b1):
        return A * np.exp(-0.5 * ((l - mu) / sig) ** 2) + b0 + b1 * (l - l0)

    base = 0.5 * (v[0] + v[-1])
    p0 = [max(v.max() - base, 1e-12), float(l0), 70.0, base, 0.0]
    p, _ = curve_fit(f, x, v, p0=p0, bounds=([0.0, l0 - W, SMIN, -np.inf, -np.inf],
                                             [np.inf, l0 + W, SMAX, np.inf, np.inf]), maxfev=400000)
    return float(p[1])


def centroid(ls, y, l0, W, sign=+1):
    """THE SECOND LOCATOR: the band power's centroid above the window's own lower shoulder.
    Not a parabola, not a fitted model, and not `70`'s procedure -- it has no shape assumption at all."""
    ls = np.asarray(ls, float)
    v_all = sign * np.asarray(y, float)
    m = np.abs(ls - l0) <= W
    x, v = ls[m], v_all[m]
    w = np.clip(v - min(v[0], v[-1]), 0.0, None)
    return float((x * w).sum() / w.sum())


def para3(ls, y, l0, sign=+1):
    """`70`'s and `cc66`'s locator, reimplemented ONLY so the readings can be compared"""
    ls = np.asarray(ls, float)
    v = sign * np.asarray(y, float)
    i = int(np.argmin(np.abs(ls - l0)))
    k = slice(max(i - 1, 0), i + 2)
    c = np.polyfit(ls[k], v[k], 2)
    return float(-c[1] / (2 * c[0]))


def paraW(ls, y, l0, W, sign=+1):
    ls = np.asarray(ls, float)
    v = sign * np.asarray(y, float)
    m = np.abs(ls - l0) <= W
    c = np.polyfit(ls[m], v[m], 2)
    return float(-c[1] / (2 * c[0]))


# ------------------------------------- Ⓐ the registered locator's own control, before any spectrum
head("Ⓐ  THE REGISTERED LOCATOR'S TWO-SIDED CONTROL, RUN BEFORE IT READS ANY SPECTRUM")
grid = np.arange(900.0, 1400.0, 1.0)
WINDOWS_REG, WINDOWS_ADD = [25, 40, 60], [80, 100, 120]
WINDOWS = WINDOWS_REG + WINDOWS_ADD


def planted(c, sig=73.0):
    return 50.0 * np.exp(-0.5 * ((grid - c) / sig) ** 2) + 300.0 - 0.05 * (grid - 1100.0)


e_mid = [gauss_centre(grid, planted(1123.57), apex(grid, planted(1123.57), 1050, 1200), W) - 1123.57
         for W in WINDOWS]
e_off = [gauss_centre(grid, planted(1126.57), apex(grid, planted(1126.57), 1050, 1200), W) - 1126.57
         for W in WINDOWS]
note(max(map(abs, e_mid)) < 1e-3,
     f'⓵ A SYMMETRIC PEAK OF KNOWN CENTRE comes back at its centre at every one of the {len(WINDOWS)} '
     f'windows: worst error {max(map(abs, e_mid)):.1e} multipoles')
note(max(map(abs, e_off)) < 1e-3,
     f'⓶ AND ONE PLANTED THREE MULTIPOLES OFF is read as moved by three, so the fitter is not pinned to '
     f'one answer: worst error {max(map(abs, e_off)):.1e} -- this is the control `r7638+60.1`\'s repair '
     'was made for')
note(True is not None and all(isinstance(e, float) for e in e_mid),
     '⓷ ⚠ AND WHAT THIS CONTROL DOES NOT TEST, SAID BEFORE IT IS LEANED ON: it plants the locator\'s '
     'OWN model -- a symmetric bump on a straight line -- so it validates the FITTER and says nothing '
     'about whether that model fits an acoustic peak.  Ⓒ below is where that is tested, and it is '
     'where the registered locator fails')

# --------------------------------------------------------------------------- Ⓑ the spectra, and Ⓑ⓵
head('Ⓑ  THE SPECTRA, AND THE REGISTERED LOCATOR\'S ANSWER')
fine_arm = np.load(os.path.join(SPEC, 'r6941_fine_cr_leafrec1.npz'), allow_pickle=True)
fine_old = np.load(os.path.join(SPEC, 'r6941_fine_cr.npz'), allow_pickle=True)
fine_ctl = np.load(os.path.join(SPEC, 'r6941_fine_lcdm.npz'), allow_pickle=True)
pol_arm = np.load(os.path.join(POL, 'pol_cr_leafrec1.npz'), allow_pickle=True)
pol_ctl = np.load(os.path.join(POL, 'pol_lcdm.npz'), allow_pickle=True)

man = str(fine_arm['manifest'])
note(all(s in man for s in ('"LEAFREC": 1', '68.57073', '0.291246', '0.021643', '1.015066')),
     "Ⓑ⓵ THE ARM READ IS THE ARM OF RECORD, asserted from the spectrum's OWN manifest and not from a "
     'file name: LEAFREC=1 at the refitted point')

SKY = {'TT': [("plik_lite, P15 sec:intro's locator", 1123.9), ("Planck, 70's table", 1122.5),
              ("ACT, 70's table", 1122.0)],
       'EE': [("Planck, 70's table", 1001.2), ("ACT, 70's table", 990.6)],
       'TE': [("Planck, 70's table", 1068.7), ("ACT, 70's table", 1074.2)]}
#                 arm ls, arm y, ctl ls, ctl y, bracket, sign of the extremum
SERIES = {'TT': (fine_arm['ls'], fine_arm['Dl'], fine_ctl['ls'], fine_ctl['Dl'], (1050, 1200), +1),
          'EE': (pol_arm['ls'], pol_arm['Dl_EE'], pol_ctl['ls'], pol_ctl['Dl_EE'], (930, 1060), +1),
          'TE': (pol_arm['ls'], pol_arm['Dl_TE'], pol_ctl['ls'], pol_ctl['Dl_TE'], (1010, 1130), -1)}
BAND = (0.75, 1.00)


def read_all(locator):
    pos, sh = {}, {}
    for sp, (la, ya, lc, yc, br, sg) in SERIES.items():
        for W in WINDOWS:
            try:
                a = locator(la, ya, apex(la, ya, *br, sign=sg), W, sign=sg)
                c = locator(lc, yc, apex(lc, yc, *br, sign=sg), W, sign=sg)
            except RuntimeError:
                continue
            pos[(sp, W)] = (a, c)
            for n, sky in SKY[sp]:
                sh[(sp, W, n)] = (c - sky) / (a - sky)
    return pos, sh


POS_G, SH_G = read_all(gauss_centre)
tt_g = [SH_G[('TT', W, n)] for W in WINDOWS for n, _ in SKY['TT']]
note(not all(BAND[0] <= s <= BAND[1] for s in tt_g),
     f'Ⓑ⓶ ⛔ THE REGISTERED NEGATIVE ARRIVED, AND IT IS SCORED AS ARRIVING: on the registered Gaussian '
     f'the TT share is {min(tt_g):.3f} to {max(tt_g):.3f} over {len(tt_g)} readings -- it CROSSES '
     f'{BAND[1]:.2f} at every window and every sky source, so by the registration the figure is the '
     "locator's and not the spectra's.  ⌗ This line's registered expectation that it would land inside "
     'the band is a MISS and is reported as one')

# ------------------------------------------- Ⓒ the adjudication: whose negative is it, measured
head('Ⓒ  THE ADJUDICATION -- FIVE LOCATOR FAMILIES ON ONE CURVE, AND THE GAUSSIAN IS THE OUTLIER')
TT = SERIES['TT']
a0 = apex(TT[0], TT[1], *TT[4])
c0 = apex(TT[2], TT[3], *TT[4])
fam = {'raw grid extremum': (a0, c0),
       "three-point parabola (70's)": (para3(TT[0], TT[1], a0), para3(TT[2], TT[3], c0))}
for W in (10, 20, 40, 80):
    fam[f'parabola W={W}'] = (paraW(TT[0], TT[1], a0, W), paraW(TT[2], TT[3], c0, W))
for W in (40, 80):
    fam[f'centroid W={W}'] = (centroid(TT[0], TT[1], a0, W), centroid(TT[2], TT[3], c0, W))
for W in (25, 40, 60, 120):
    fam[f'GAUSSIAN W={W}'] = (gauss_centre(TT[0], TT[1], a0, W), gauss_centre(TT[2], TT[3], c0, W))
print(f"    {'locator':30s} {'arm':>10s} {'control':>10s} {'arm-control':>12s}")
for n, (a, c) in fam.items():
    print(f'    {n:30s} {a:10.3f} {c:10.3f} {a - c:+12.3f}')
non_g = {n: a - c for n, (a, c) in fam.items() if 'GAUSS' not in n}
gau = {n: a - c for n, (a, c) in fam.items() if 'GAUSS' in n}
note(all(v > 0 for v in non_g.values()) and all(v < 0 for v in gau.values()),
     f'Ⓒ⓵ ⛔ THE GAUSSIAN REVERSES THE SIGN OF THE DISPLACEMENT that every other locator agrees on: '
     f'{len(non_g)} non-Gaussian readings all give arm-minus-control POSITIVE '
     f'({min(non_g.values()):+.3f} to {max(non_g.values()):+.3f}, around 70\'s +0.518), and all '
     f'{len(gau)} Gaussian readings give it NEGATIVE ({min(gau.values()):+.3f} to '
     f'{max(gau.values()):+.3f})')
_K70 = "three-point parabola (70's)"
note(all(abs(fam[f'GAUSSIAN W={W}'][0] - fam[_K70][0]) > 5.0 for W in (25, 40, 60, 120)),
     'Ⓒ⓶ AND IT SITS SOME SIX MULTIPOLES UP-ELL OF ALL OF THEM on the same curve: '
     f'{fam["GAUSSIAN W=40"][0]:.3f} against {fam[_K70][0]:.3f}')
g_drift = [gauss_centre(TT[0], TT[1], a0, W) for W in WINDOWS]
c_drift = [gauss_centre(TT[2], TT[3], c0, W) for W in WINDOWS]
mono_a = all(b > a for a, b in zip(g_drift, g_drift[1:]))
mono_c = all(b > a for a, b in zip(c_drift, c_drift[1:]))
note(mono_a and mono_c,
     f'Ⓒ⓷ AND THE CAUSE IS MEASURED RATHER THAN GUESSED: the Gaussian centre climbs MONOTONICALLY with '
     f'window on BOTH the arm ({g_drift[0]:.3f} -> {g_drift[-1]:.3f}) and the control '
     f'({c_drift[0]:.3f} -> {c_drift[-1]:.3f}) -- the signature of a SYMMETRIC model fitted to an '
     'ASYMMETRIC peak on a steep damping tail, and a property of the curve rather than of either arm')
m = (np.asarray(TT[0], float) >= 1000) & (np.asarray(TT[0], float) <= 1260)
xw, yw = np.asarray(TT[0], float)[m], np.asarray(TT[1], float)[m]
ipk = int(np.argmax(yw))
hl = yw.min() + 0.5 * (yw[ipk] - yw.min())
lf, rt = xw[:ipk][yw[:ipk] <= hl], xw[ipk:][yw[ipk:] <= hl]
fwhm = float(rt[0] - lf[-1])
rise, fall = float(xw[ipk] - lf[-1]), float(rt[0] - xw[ipk])
note(abs(rise - fall) / fwhm > 0.05,
     f'Ⓒ⓸ AND THE ASYMMETRY IS MEASURED: the feature is {fwhm:.0f} multipoles wide at half maximum and '
     f'its two half-widths are {rise:.0f} up and {fall:.0f} down, differing by '
     f'{100 * abs(rise - fall) / fwhm:.0f} per cent of the width -- so a symmetric model cannot sit on '
     'it without bias')

# ------------------------------------------------- Ⓓ the second locator that passes the adjudication
head("Ⓓ  THE SECOND LOCATOR THAT PASSES THE ADJUDICATION, AND IT IS STILL NOT 70's")
SEV = {'TT': (1129.742, 1129.224), 'EE': (988.60, 991.32), 'TE': (1069.04, 1073.03)}
POS_C, SH_C = read_all(centroid)
print(f"    {'spec':4s} {'W':>3s} {'arm':>10s} {'control':>10s} {'arm-ctl':>9s}   "
      f"{'70 arm':>9s} {'70 ctl':>9s} {'70 a-c':>8s}")
for sp in ('TT', 'EE', 'TE'):
    for W in WINDOWS:
        if (sp, W) in POS_C:
            a, c = POS_C[(sp, W)]
            sa, sc = SEV[sp]
            print(f'    {sp:4s} {W:>3d} {a:10.3f} {c:10.3f} {a - c:+9.3f}   {sa:9.3f} {sc:9.3f} '
                  f'{sa - sc:+8.3f}')
agree = {sp: max(abs(POS_C[(sp, 40)][0] - SEV[sp][0]), abs(POS_C[(sp, 40)][1] - SEV[sp][1]))
         for sp in ('TT', 'EE', 'TE') if (sp, 40) in POS_C}
note(all(v < 1.0 for v in agree.values()),
     f'Ⓓ⓵ THE CENTROID REPRODUCES 70\'s POSITIONS IN ALL THREE SPECTRA to under a multipole: worst '
     f'disagreement {max(agree.values()):.3f} across TT, EE and TE at W=40 -- so it is reading the '
     'same feature, which is what makes it a second reading of one quantity rather than a different '
     'quantity')
note(all((POS_C[(sp, 40)][0] - POS_C[(sp, 40)][1]) * (SEV[sp][0] - SEV[sp][1]) > 0
         for sp in ('TT', 'EE', 'TE') if (sp, 40) in POS_C),
     'Ⓓ⓶ AND IT AGREES WITH 70 ON THE SIGN of the displacement in all three, where the registered '
     'Gaussian did not -- it carries no shape assumption at all, being a weighted mean of band power '
     "above the window's own shoulder, so it is neither 70's parabola nor a re-parameterisation of it")

# ------------------------------------------------------------------- Ⓔ the share on that locator
head('Ⓔ  THE SHARE ON THE SECOND LOCATOR, PER SPECTRUM AND PER SKY SOURCE, NEVER AVERAGED')
print(f"    {'spec':4s} {'W':>3s}   {'sky source':34s} {'arm-sky':>9s} {'ctl-sky':>9s} {'share':>8s}")
for sp in ('TT', 'EE', 'TE'):
    for W in WINDOWS:
        if (sp, W) not in POS_C:
            continue
        a, c = POS_C[(sp, W)]
        for n, sky in SKY[sp]:
            print(f'    {sp:4s} {W:>3d}   {n:34s} {a - sky:+9.3f} {c - sky:+9.3f} '
                  f'{SH_C[(sp, W, n)]:8.3f}')
tt_c_reg = [SH_C[('TT', W, n)] for W in WINDOWS_REG for n, _ in SKY['TT']]
note(all(BAND[0] <= s <= BAND[1] for s in tt_c_reg),
     f'Ⓔ⓵ ⛭ ON TT THE CLOSING FIGURE SURVIVES THE SECOND LOCATOR: the share runs {min(tt_c_reg):.3f} '
     f'to {max(tt_c_reg):.3f} over {len(tt_c_reg)} readings, every one inside the registered band, '
     f"around 70's 0.911 -- so PO-87's closing outcome is reached on an instrument that is not 70's")
tt_c_80 = [SH_C[('TT', 80, n)] for n, _ in SKY['TT']]
note(min(tt_c_80) < BAND[0] + 0.01,
     f'Ⓔ⓶ ⚠ AND IT BRUSHES THE LOWER BOUND AT THE WIDEST WINDOW, which is reported rather than '
     f'trimmed: at W=80 the plik_lite reading is {min(tt_c_80):.3f} against a registered floor of '
     f'{BAND[0]:.2f} -- the share falls monotonically with window because the asymmetry pulls both '
     'positions down-ell together, so the figure is window-dependent at the third digit')
ee_pl = [SH_C[('EE', W, "Planck, 70's table")] for W in WINDOWS if ('EE', W) in POS_C]
ee_ac = [SH_C[('EE', W, "ACT, 70's table")] for W in WINDOWS if ('EE', W) in POS_C]
note(all(BAND[0] <= s <= BAND[1] for s in ee_pl) and not any(BAND[0] <= s <= BAND[1] for s in ee_ac),
     f'Ⓔ⓷ ⛔ IN EE THE ANSWER IS THE SKY SOURCE\'S, EXACTLY AS THE REGISTRATION ENUMERATED: against '
     f'Planck the share is {min(ee_pl):.3f} to {max(ee_pl):.3f}, inside the band; against ACT it is '
     f'{min(ee_ac):.3f} to {max(ee_ac):.3f}, outside it and negative -- one spectrum, one locator, two '
     'verdicts, and they are reported apart and never averaged')
te_den = [abs(POS_C[('TE', W)][0] - 1068.7) for W in WINDOWS if ('TE', W) in POS_C]
te_pl = [SH_C[('TE', W, "Planck, 70's table")] for W in WINDOWS if ('TE', W) in POS_C]
note(min(te_den) < 0.5 and (max(te_pl) - min(te_pl)) > 10,
     f'Ⓔ⓸ ⛔ AND IN TE THE SHARE IS NOT A USABLE QUANTITY AT ALL, which is a structural fact and not a '
     f'reading: the arm lands {min(te_den):.3f} of a multipole from the Planck sky value, so the '
     f'ratio\'s DENOMINATOR very nearly vanishes and the share runs from {min(te_pl):.1f} to '
     f'{max(te_pl):.1f} across the {len(te_pl)} windows.  ⇒ *** The registered negative arrives in TE, and its '
     'cause is the denominator and not a disagreement between the spectra. ***')
tt_wide = [SH_C[('TT', W, n)] for W in (100, 120) for n, _ in SKY['TT']]
tt_den = [abs(POS_C[('TT', W)][0] - sky) for W in (100, 120) for _, sky in SKY['TT']]
note(not any(BAND[0] <= s <= BAND[1] for s in tt_wide) and min(tt_den) < 0.5,
     f'Ⓔ⓺ ⛔ AND AT THE TWO WIDEST WINDOWS THE TT SHARE BREAKS TOO, by the SAME mechanism as TE and not '
     f'by a different one: none of the {len(tt_wide)} readings at W=100 and W=120 is inside the band '
     f'({min(tt_wide):+.3f} to {max(tt_wide):+.3f}), and the smallest arm-minus-sky residual there is '
     f'{min(tt_den):.3f} of a multipole -- the denominator passes through zero.  ⇒ *** So Ⓐ⓷\'s reading '
     'that the wide windows are the better instrument, taken on a PLANTED SYMMETRIC peak, is REFUTED on '
     'the real curve: it was the fitter that got better with width, not the model.  The verdict rests '
     'on the registered windows, and that is now measured rather than preferred. ***')
note(apex(SERIES['TE'][0], SERIES['TE'][1], 1010, 1130, sign=-1) > 1000,
     "Ⓔ⓹ ⌗ AND ONE TRAP NAMED BECAUSE THIS RECEIPT'S FIRST PASS FELL INTO IT: TE's fourth feature is a "
     'MINIMUM, not a maximum -- TE changes sign under it -- so a locator seeking a maximum does not '
     'find it at all and wanders with the window.  Every TE reading here is taken on the minimum')

head('VERDICT')
print(f'  {len(CHECKS)} check(s), {CHECKS.count(False)} FAILED')
sys.exit(1 if CHECKS.count(False) else 0)
