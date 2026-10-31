#!/usr/bin/env python3
"""r7641 item 2, grid reader 1 of 6: the 185-bin full-range refit read on the ARM OF RECORD.

70's second bank put the CR side of the response grids in sibling `<dir>_leafrec1/` directories, so
`P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised` can be read on
the arm of record for the first time.  Three pointers move and the control's do not:

    refit_grid185/cr_*.npz            -> refit_grid185_leafrec1/cr_*.npz   (the 9 response runs)
    spectra/cc66_r185_verify_cr.npz   -> spectra/cc66_r185_verify_cr_leafrec1.npz  (the real run)
    spectra/r6941_fine_cr.npz         -> spectra/r6941_fine_cr_leafrec1.npz  (the locator substrate)

** AND THE RE-POINT IS PARTIAL, FOR A REASON THE BANK ITSELF STATES.  TWO OF THIS RECEIPT'S FIGURES
CANNOT BE READ ON THE ARM OF RECORD AT ALL, AND BOTH ARE DECLARED AND GATED BELOW RATHER THAN
QUIETLY ANSWERED WITH THE NEAREST AVAILABLE NUMBER: **

  ⒜ ** THE BACKGROUND-PINNING FIGURE.  **  The receipt's question is whether four free parameters
     prise the background off the point the DISTANCES fix -- `(68.60, 0.2973)`, from DESI DR2 BAO and
     theta_* "with no spectrum involved".  The arm-of-record grid is centred on the arm of record's
     OWN FITTED point, `(68.57073, 0.291246, 0.021643, 1.015066)` (r7633), which a spectrum chose.
     ⇒ *A residual move from a fitted centre measures how well that fit converged; it cannot measure
     whether the distances' point survives freedom, because the distances' point is not the centre.*
     ** So this is a BANK REQUEST, not a result: a LEAFREC=1 response grid centred on the BAO point. **

  ⒝ ** THE VERIFIED MINIMUM.  **  `refit_grid185_leafrec1/verify_cr.npz` and
     `spectra/cc66_r185_verify_cr_leafrec1.npz` are BIT-IDENTICAL to `cr_base.npz` -- measured here,
     0.0 of the peak -- which is what 70's `RESULT.md` means by "`best_cr` and `verify_cr`, which on
     the arm of record are its base".  ⇒ *So the receipt's Part 2 licence ("the response model says
     WHERE to go; only a full run says what is there") has nothing to exercise on this arm: there is
     no run AT the arm of record's refitted minimum.*  ** A second bank request. **
     ⛔ *Read without that measurement the comparison returns `+2.3` and LOOKS like a failed
     verification.  It is not: it is the model's own gain from its base, with no run to check it.*

** THE CARRY (`band_excess_own`, r7639+cc66.22) DOES NOT APPLY, AND THAT IS MEASURED NOT ASSERTED. **
The phase residual is `|phi_arm/phi_sky - 1|`: each arm's own comb, fitted from its own first three
peaks, against THE SKY'S.  No control quantity enters it -- checked below by recomputing the arm's
residual from the arm spectrum and the sky alone and requiring it bit-exact against the pipeline's.
A comb-offset carry needs an arm-against-control comb-band ratio to act on, and there is none here;
the parameter moves and the chi^2 ratios are not band ratios either.  ** Class 3, computed. **

Every figure is reported old -> new in `FOR_66.md`.  Nothing is edited by this file.
"""
import ast
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize
from scipy.signal import argrelextrema

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SPEC = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BAR = "=" * 100
fail = []


def check(label, ok, witness=''):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}"
          + (f"   ({'' if ok else 'got '}{witness})" if witness else ''))
    if not ok:
        fail.append(label)


# ** lifted VERBATIM from the receipt: the sky peaks, the steps, the two starting points. **
SKY = np.array([220.4, 537.7, 817.3, 1123.9])
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)
BAO = dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)        # what the DISTANCES fix -- the receipt's
CTL0 = dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)       # question is about THIS point

#: the two arms as pointer sets.  The control is in neither column because it does not move: 70's
#: bank says so and the grid listing bears it out (the `_leafrec1` directories hold `cr_*` only).
ARM = {'namesake': dict(grid='refit_grid185', ver='cc66_r185_verify_cr.npz',
                        fine='r6941_fine_cr.npz'),
       'aor': dict(grid='refit_grid185_leafrec1', ver='cc66_r185_verify_cr_leafrec1.npz',
                   fine='r6941_fine_cr_leafrec1.npz')}
CTL = dict(grid='refit_grid185', ver='cc66_r185_verify_lcdm.npz')

#: ** the lensing operator, lifted verbatim including its fallback. **  `cc66_lens_ratio.npz` is not
#: banked in this checkout, so the receipt's `camb` branch is the live one -- imposed on BOTH arms
#: alike at the CONTROL's parameters, so it cannot favour either.
_LRP = os.path.join(SPEC, 'cc66_lens_ratio.npz')
if os.path.exists(_LRP):
    _LR = np.load(_LRP)
    LG, RATIO = np.asarray(_LR['lg'], float), np.asarray(_LR['ratio'], float)
else:
    import camb                                                            # noqa: E402
    _p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                         mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    _cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
    _le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
    LG = np.arange(len(_le), dtype=float)
    RATIO = np.ones_like(_le)
    _m = _un > 0
    RATIO[_m] = _le[_m] / _un[_m]


def centre_of(grid, tag, fallback):
    """** the grid's OWN centre, read from its manifest rather than assumed. **

    This is the whole reason ⒜ above is a bank request and not a result: the namesake grid carries
    no manifest and IS centred on the distances' point, while the arm-of-record grid names a fitted
    point in its own `manifest['point']`.  A hard-coded starting point would have reported a move
    from a centre the bank does not have.
    """
    z = np.load(os.path.join(BW, grid, f'{tag}_base.npz'), allow_pickle=True)
    if 'manifest' not in z.files:
        return dict(fallback), None
    m = z['manifest'].item() if hasattr(z['manifest'], 'item') else z['manifest']
    #: ⌗ *the manifest is stored as a 0-d string array holding a PYTHON repr, not JSON, so
    #: `json.loads` fails on it and `ast.literal_eval` is what reads it.  Measured, not guessed.*
    if isinstance(m, (bytes, str)):
        try:
            m = ast.literal_eval(m if isinstance(m, str) else m.decode())
        except (ValueError, SyntaxError):
            m = json.loads(m)
    p = m.get('point', {})
    got = dict(H0=float(p.get('CRH0', fallback['H0'])), OM=float(p.get('CROM', fallback['OM'])),
               WB=float(p.get('WBH2', fallback['WB'])), NS=float(p.get('NS', fallback['NS'])))
    return got, m


def binned(ls, Dl, lens=True):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO) if lens else Dl)


def build(tag, grid, th0, lens=True):
    """the receipt's own `build`, with the grid directory and the centre passed in."""
    g_dir = os.path.join(BW, grid)
    z = np.load(os.path.join(g_dir, f'{tag}_base.npz'))
    ls = np.asarray(z['ls'], float)
    m0 = binned(ls, np.asarray(z['Dl'], float), lens)
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    mb = m0[ok]
    g, h = {}, {}
    for k in STEP:
        zp = np.load(os.path.join(g_dir, f'{tag}_{k}p.npz'))
        zm = np.load(os.path.join(g_dir, f'{tag}_{k}m.npz'))
        mp = binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float), lens)[ok]
        mm = binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float), lens)[ok]
        g[k] = (mp - mm) / (2 * STEP[k])
        h[k] = (mp - 2 * mb + mm) / STEP[k] ** 2
    return dict(m0=mb, ok=ok, F=F, d=CS.X_DATA[ok], g=g, h=h, th0=th0)


def chi2_at(B, x):
    m = B['m0'].copy()
    for k, v in zip(STEP, x):
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


def comb(P, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(P[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def peaks_sub(ls, Dl, n=4, order=3):
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        if i < 1 or i > len(ls) - 2:
            out.append(float(ls[i]))
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return out


def fit(tag, grid, th0):
    B = build(tag, grid, th0)
    n = int(B['ok'].sum())
    c0 = chi2_at(B, np.zeros(4))
    r = minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                 options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))
    flat = {}
    for i, k in enumerate(STEP):
        e = np.zeros(4)
        e[i] = STEP[k]
        flat[k] = min(chi2_at(B, r.x + e) - r.fun, chi2_at(B, r.x - e) - r.fun)
    return dict(B=B, x=r.x, fun=r.fun, n=n, c0=c0, flat=flat, th0=th0)


def verified(fn):
    z = np.load(os.path.join(SPEC, fn))
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    c, nb, _A, _lo, _hi = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))
    return c, nb, ls, Dl


def phase_of(ls, Dl):
    """the arm's own statistic: its own comb's phase against THE SKY'S, and its fourth peak's."""
    _, phi_sky = comb(SKY)
    out = {}
    for lab, f in (('raw', peaks_raw), ('refined', peaks_sub)):
        P = f(ls, Dl)
        _, phi = comb(P)
        out[lab] = (abs(phi / phi_sky - 1) * 100, abs(P[3] / SKY[3] - 1) * 100, P)
    return out


def substrate(fine):
    z = np.load(os.path.join(SPEC, fine))
    l1, D1 = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    native = peaks_sub(l1, D1, order=20)
    e_raw = e_sub = 0.0
    for st in (2, 4, 8):
        ls, Ds = l1[::st], D1[::st]
        o = max(3, 20 // st)
        e_raw = max(e_raw, max(abs(a - b) for a, b in zip(peaks_raw(ls, Ds, order=o), native)))
        e_sub = max(e_sub, max(abs(a - b) for a, b in zip(peaks_sub(ls, Ds, order=o), native)))
    return e_raw, e_sub, int(l1[1] - l1[0])


print(__doc__)
print(BAR)
print("  PART 1 -- THE TWO GRIDS' OWN CENTRES, READ FROM THEIR MANIFESTS")
print(BAR)
TH = {}
for arm in ('namesake', 'aor'):
    TH[arm], man = centre_of(ARM[arm]['grid'], 'cr', BAO)
    src = 'manifest' if man else 'NO manifest -- the distances\' point, as the receipt states'
    print(f"    {arm:>9} ({ARM[arm]['grid']:>22}): "
          + "  ".join(f"{k} {TH[arm][k]:.6f}" for k in STEP) + f"   [{src}]")
check("⛔⒜ THE ARM-OF-RECORD GRID IS NOT CENTRED ON THE DISTANCES' POINT, which is what makes the "
      "background-pinning figure unreadable here rather than merely different: the namesake grid "
      "sits at (68.60, 0.2973) with no manifest, the arm of record's at its own FITTED "
      "(68.57073, 0.291246).  ⇒ ** A move from a fitted centre cannot answer a question about the "
      "distances' point.  Reported as a bank request, not as a result **",
      abs(TH['namesake']['H0'] - 68.60) < 1e-9 and abs(TH['namesake']['OM'] - 0.2973) < 1e-9
      and abs(TH['aor']['H0'] - 68.57073) < 1e-5 and abs(TH['aor']['OM'] - 0.291246) < 1e-6,
      f"namesake ({TH['namesake']['H0']:.5f}, {TH['namesake']['OM']:.6f}), "
      f"arm of record ({TH['aor']['H0']:.5f}, {TH['aor']['OM']:.6f})")

_b = np.load(os.path.join(BW, 'refit_grid185_leafrec1', 'cr_base.npz'))['Dl']
_pk = float(np.max(np.abs(np.asarray(_b, float))))
_dv = max(float(np.max(np.abs(np.asarray(np.load(os.path.join(p))['Dl'], float)
                               - np.asarray(_b, float))))
          for p in (os.path.join(BW, 'refit_grid185_leafrec1', 'verify_cr.npz'),
                    os.path.join(SPEC, 'cc66_r185_verify_cr_leafrec1.npz')))
print(f"\n    max |verify - base| on the arm of record: {_dv:.3e}  ({_dv / _pk:.2e} of the peak)")
check("⛔⒝ AND ON THE ARM OF RECORD THE VERIFICATION RUN *IS* THE GRID BASE, bit-identical -- both "
      "the grid's `verify_cr` and `spectra/cc66_r185_verify_cr_leafrec1`.  ⇒ ** So there is no run "
      "at this arm's refitted minimum, and the receipt's Part 2 licence has nothing to exercise.  "
      "The `+2.3` that a naive read returns is the model's gain from its own base, not a failed "
      "verification **", _dv == 0.0, f"{_dv:.3e} of peak {_pk:.1f}")

print()
print(BAR)
print("  PART 2 -- THE CONTROL, ONCE.  The same file on both arms, so it is fitted once.")
print(BAR)
C = fit('lcdm', CTL['grid'], CTL0)
c_ver, c_nb, c_ls, c_Dl = verified(CTL['ver'])
c_ph = phase_of(c_ls, c_Dl)
print(f"    control: {C['n']} bins, as-computed {C['c0']:.1f} ({C['c0'] / C['n']:.2f}/bin), "
      f"refitted {C['fun']:.1f} ({C['fun'] / C['n']:.2f}/bin), verified {c_ver:.1f} "
      f"({c_ver / c_nb:.2f}/bin)")
print(f"    control phase residual: raw {c_ph['raw'][0]:.1f}%, refined {c_ph['refined'][0]:.1f}%; "
      f"fourth peak refined {c_ph['refined'][1]:.1f}%")
print(f"    control raw peaks " + " / ".join(f"{v:.0f}" for v in c_ph['raw'][2]))
#: ⌗ *The published per-bin pair `1.01`/`1.58` is the VERIFIED chi^2 over the bins, not the response
#: model's -- 186.5/185 against the model's 185.1/185, which prints 1.00.  Checked before gating.*
check("the control's 185 bins and its published 1.01 per bin (verified) and 1.6 per cent all "
      "reproduce",
      C['n'] == 185 and abs(c_ver / c_nb - 1.01) < 5e-3
      and abs(c_ph['refined'][0] - 1.6) < 0.05 and abs(c_ph['refined'][1] - 0.5) < 0.05,
      f"{C['n']} bins, verified {c_ver / c_nb:.2f}/bin, phase {c_ph['refined'][0]:.2f}%, "
      f"fourth {c_ph['refined'][1]:.2f}%")

print()
print(BAR)
print("  PART 3 -- THE TWO ARMS IN ONE PIPELINE.  The namesake is the LICENCE: it must reproduce")
print("  the receipt's published figures before the arm of record's are read at all.")
print(BAR)
A = {}
for arm in ('namesake', 'aor'):
    P = ARM[arm]
    f = fit('cr', P['grid'], TH[arm])
    v, nb, ls, Dl = verified(P['ver'])
    ph = phase_of(ls, Dl)
    A[arm] = dict(f=f, ver=v, ph=ph, sub=substrate(P['fine']))
    print(f"\n    --- {arm} ({P['grid']}, {P['ver']}) ---")
    print("      " + "   ".join(
        f"{k} {f['x'][i]:+.4f} ({100 * f['x'][i] / TH[arm][k]:+.3f}%)" for i, k in enumerate(STEP)))
    print(f"      chi^2 at the centre {f['c0']:.1f} ({f['c0'] / f['n']:.2f}/bin), "
          f"refitted {f['fun']:.1f} ({f['fun'] / f['n']:.2f}/bin), banked run {v:.1f} "
          f"({v / nb:.2f}/bin)")
    print(f"      ratios against the control: banked run {v / c_ver:.2f}x   "
          f"at the centre {f['c0'] / C['c0']:.2f}x")
    print(f"      phase residual raw {ph['raw'][0]:.1f}%  refined {ph['refined'][0]:.1f}%   "
          f"fourth peak refined {ph['refined'][1]:.1f}%")
    print("      raw peaks     " + " / ".join(f"{v_:.0f}" for v_ in ph['raw'][2]))
    print("      refined peaks " + " / ".join(f"{v_:.1f}" for v_ in ph['refined'][2]))
    print(f"      locator substrate ({P['fine']}, spacing {A[arm]['sub'][2]}): "
          f"raw errs {A[arm]['sub'][0]:.2f}, refined {A[arm]['sub'][1]:.3f}")

N, O = A['aor'], A['namesake']
check("⛔ THE LICENCE GATE: the namesake arm reproduces every figure the receipt publishes -- "
      "0.028%/0.031% in H0/Omega_m, 1.58 and 1.01 per bin verified, 1.57x against 2.56x at the "
      "centre, and 3.4% against the control's 1.6%.  ⇒ ** So the fit in this file IS the receipt's "
      "fit, and what moves below is the arm **",
      abs(abs(100 * O['f']['x'][0] / BAO['H0']) - 0.028) < 5e-4
      and abs(abs(100 * O['f']['x'][1] / BAO['OM']) - 0.031) < 5e-4
      and abs(O['ver'] / O['f']['n'] - 1.58) < 5e-3
      and abs(c_ver / c_nb - 1.01) < 5e-3
      and abs(O['ver'] / c_ver - 1.57) < 5e-3
      and abs(O['f']['c0'] / C['c0'] - 2.56) < 5e-3
      and abs(O['ph']['refined'][0] - 3.4) < 0.05,
      f"H0 {abs(100 * O['f']['x'][0] / BAO['H0']):.3f}%, "
      f"OM {abs(100 * O['f']['x'][1] / BAO['OM']):.3f}%, "
      f"verified {O['ver'] / O['f']['n']:.2f}/bin, {O['ver'] / c_ver:.2f}x, "
      f"{O['f']['c0'] / C['c0']:.2f}x, phase {O['ph']['refined'][0]:.2f}%")

print()
print(BAR)
print("  PART 4 -- WHAT MOVES, OLD -> NEW -- AND WHAT IS NOT A MOVE BUT AN ABSENCE")
print(BAR)
ROWS = [('chi^2 refitted', O['f']['fun'], N['f']['fun'], '.1f', 1),
        ('per bin, refitted', O['f']['fun'] / O['f']['n'], N['f']['fun'] / N['f']['n'], '.2f', 1),
        ('banked run chi^2', O['ver'], N['ver'], '.1f', 1),
        ('ratio, banked run', O['ver'] / c_ver, N['ver'] / c_ver, '.2f', 1),
        ('phase residual, refined %', O['ph']['refined'][0], N['ph']['refined'][0], '.1f', 1),
        ('phase residual, raw %', O['ph']['raw'][0], N['ph']['raw'][0], '.1f', 1),
        ('fourth peak, refined %', O['ph']['refined'][1], N['ph']['refined'][1], '.1f', 1),
        ('second raw peak', O['ph']['raw'][2][1], N['ph']['raw'][2][1], '.0f', 1),
        ('locator raw error', O['sub'][0], N['sub'][0], '.2f', 1),
        ('locator refined error', O['sub'][1], N['sub'][1], '.3f', 1),
        ('flatness, cheapest step', min(O['f']['flat'].values()), min(N['f']['flat'].values()),
         '.1f', 1),
        ('H0 move, per cent', abs(100 * O['f']['x'][0] / TH['namesake']['H0']),
         abs(100 * N['f']['x'][0] / TH['aor']['H0']), '.3f', 0),
        ('Omega_m move, per cent', abs(100 * O['f']['x'][1] / TH['namesake']['OM']),
         abs(100 * N['f']['x'][1] / TH['aor']['OM']), '.3f', 0),
        ('chi^2 at the centre', O['f']['c0'], N['f']['c0'], '.1f', 0),
        ('ratio at the centre', O['f']['c0'] / C['c0'], N['f']['c0'] / C['c0'], '.2f', 0)]
print(f"    {'figure':>28} {'namesake':>12} {'arm of record':>14}   verdict")
for lab, o, n, f, readable in ROWS:
    if not readable:
        v = '⛔ NOT COMPARABLE -- different centre (⒜)'
    elif abs(n - o) < 1e-9:
        v = 'unchanged'
    else:
        v = 'MOVED' if abs(n - o) > 0.005 * max(1e-9, abs(o)) else 'moved (trace)'
    print(f"    {lab:>28} {format(o, f):>12} {format(n, f):>14}   {v}")

print()
print(BAR)
print("  PART 5 -- THE CARRY, MEASURED RATHER THAN CLASSIFIED BY ASSERTION")
print(BAR)
_solo = phase_of(*verified(ARM['aor']['ver'])[2:4])
check("⛭⛭ THE CARRY HAS NOTHING TO ACT ON: the arm's phase residual computed from the arm spectrum "
      "and the SKY alone is bit-identical to the pipeline's, so no control quantity enters it.  ⇒ "
      "** A comb-offset carry needs an arm-against-control comb-band ratio; this statistic is the "
      "arm's own comb against the sky's, and the parameter moves and chi^2 ratios are not band "
      "ratios either.  CLASS 3, and computed **",
      _solo['refined'][0] == N['ph']['refined'][0] and _solo['raw'][0] == N['ph']['raw'][0],
      f"solo {_solo['refined'][0]:.6f}% against pipeline {N['ph']['refined'][0]:.6f}%")

print()
print(BAR)
print("  PART 6 -- THE GATES THE RECEIPT CAN CARRY ON THE ARM OF RECORD")
print(BAR)
check("the arm is still disfavoured against the control", N['ver'] > c_ver,
      f"{N['ver']:.1f} against {c_ver:.1f}")
check("every parameter is still a live direction: a one-step excursion costs chi^2 on both arms",
      all(v > 5.0 for v in N['f']['flat'].values()) and all(v > 5.0 for v in C['flat'].values()),
      f"arm min {min(N['f']['flat'].values()):.1f}, control min {min(C['flat'].values()):.1f}")
check("the REFINED locator still separates the arms, which is the half of the correction that "
      "carries the verdict", N['ph']['refined'][0] > 1.5 * c_ph['refined'][0],
      f"{N['ph']['refined'][0]:.1f}% against {c_ph['refined'][0]:.1f}%, a factor "
      f"{N['ph']['refined'][0] / c_ph['refined'][0]:.1f}")
# ⛔⛭ ** AND THE RAW COINCIDENCE IS ABSENT ON THIS ARM, WHICH IS MEASURED AND NOT A SAMPLING
#   ARTEFACT: ** both verification spectra are on the same ell grid at spacing 8, and the arm of
#   record's SECOND raw peak lands at 532 where the control's and the namesake's both land at 540.
#   ⇒ *The receipt's demonstration -- "on the raw locator the two arms return the same residual,
#   which is how a number that measures the grid shows itself" -- holds on the NAMESAKE arm, where
#   it was made, and does not hold here.  The withdrawal of cc66.18's 4.5% stands on that arm; what
#   this arm adds is that the quantised reading is not even stable across arms.*
check("⛔ the raw coincidence is ABSENT on the arm of record, and the reason is its second peak "
      "crossing a grid step -- same ell grid, spacing 8, so this is not a sampling artefact.  ⇒ "
      "** Reported, not smoothed over: the receipt's raw-locator demonstration is the namesake "
      "arm's, and the refined reading is what carries the verdict on this one **",
      int(N['ph']['raw'][2][1]) == 532 and int(c_ph['raw'][2][1]) == 540
      and int(O['ph']['raw'][2][1]) == 540
      and abs(N['ph']['raw'][0] - c_ph['raw'][0]) > 0.05,
      f"arm of record 2nd raw peak {N['ph']['raw'][2][1]:.0f}, control {c_ph['raw'][2][1]:.0f}, "
      f"namesake {O['ph']['raw'][2][1]:.0f}; raw residuals {N['ph']['raw'][0]:.1f}% vs "
      f"{c_ph['raw'][0]:.1f}%")
check("the locator substrate still validates on the arm of record's own fine spectrum, and more "
      "strictly than on the namesake's", N['sub'][0] > 2.0 and N['sub'][1] < 0.2,
      f"raw {N['sub'][0]:.2f}, refined {N['sub'][1]:.3f}")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
