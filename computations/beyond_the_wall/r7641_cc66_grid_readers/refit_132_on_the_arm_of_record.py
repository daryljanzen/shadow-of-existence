#!/usr/bin/env python3
"""r7641 item 2, grid reader 2 of 6: the 132-bin refit read on the ARM OF RECORD.

`P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase` asks
the SAME question as grid reader 1 on the shorter range, so it meets the same two obstructions -- and
this file's job is to establish that they are the bank's shape and not one receipt's bad luck, with
the namesake arm as the control that proves each comparison is meaningful.

    refit_grid/cr_*.npz                   -> refit_grid_leafrec1/cr_*.npz
    spectra/cc66_refit_verify_cr.npz      -> spectra/cc66_refit_verify_cr_leafrec1.npz

  ⒜ ** THE CENTRE. **  `refit_grid_leafrec1` is centred on the arm of record's own FITTED point
     `(68.570730, 0.291246, 0.021643, 1.015066)`, read from its manifest; `refit_grid` carries no
     manifest and sits at the distances' point `(68.60, 0.2973, 0.0224, 0.965)`.  The receipt's title
     is *"the refit leaves the background where the distances put it"*, so the figure the title names
     cannot be read from a grid centred somewhere else.

  ⒝ ** THE VERIFICATION RUN IS THE BASE. **  `cc66_refit_verify_cr_leafrec1.npz` is BIT-IDENTICAL to
     `refit_grid_leafrec1/cr_base.npz`.  ⌗ *And the namesake arm is the control for that statement:
     its `cc66_refit_verify_cr.npz` differs from `refit_grid/cr_base.npz` by 12.3 per cent of the
     peak, because it IS a run at a different point -- its own refit minimum, as the receipt says.
     So the identity on the arm of record is an absence of that run, not how these files are built.*

  ⛔⛭ ** AND THE ARM-OF-RECORD FILE'S MANIFEST DISAGREES WITH ITSELF, WHICH IS WORTH 70 KNOWING. **
     Its `held` prose says *"here the arm of record (the cc66 refit minimum, ~68.6077/0.2967/0.0217/
     0.9949, digits unrecorded)"* -- the 132-bin REFIT MINIMUM.  Its own `point` and `switches` say
     `CRH0=68.570730 CROM=0.291246 WBH2=0.021643 NS=1.015066`, the r7633 point of record.  *The data
     agrees with the switches: the file is the grid base.*  ⇒ ** So the machine-readable half of the
     record is right and the prose would mislead a reader into thinking there is a verification run
     at the refit minimum.  Reported, not worked around. **

Nothing is edited by this file.  Figures are reported old -> new in `FOR_66.md`.
"""
import ast
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


# ** lifted VERBATIM from the receipt. **
SKY = np.array([220.4, 537.7, 817.3, 1123.9])
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.0200)
DISTANCES = dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)
CTL0 = dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)
ARM = {'namesake': dict(grid='refit_grid', ver='cc66_refit_verify_cr.npz'),
       'aor': dict(grid='refit_grid_leafrec1', ver='cc66_refit_verify_cr_leafrec1.npz')}
CTL = dict(grid='refit_grid', ver='cc66_refit_verify_lcdm.npz')


def lensing_ratio():
    """CAMB's lensed/unlensed ratio -- LCDM's, imposed on both arms, exactly as the receipt does."""
    import camb
    pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                           mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
    lensed, unlens = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    lg = np.arange(len(lensed))
    r = np.ones_like(lensed)
    m = unlens > 0
    r[m] = lensed[m] / unlens[m]
    return lg, r


LG, RATIO = lensing_ratio()


def binned(ls, Dl, lens=True):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO) if lens else Dl)


def load(path):
    z = np.load(path)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def manifest_of(path):
    z = np.load(path, allow_pickle=True)
    if 'manifest' not in z.files:
        return None
    m = z['manifest'].item()
    if isinstance(m, (bytes, str)):
        m = ast.literal_eval(m if isinstance(m, str) else m.decode())
    return m


def centre_of(grid):
    m = manifest_of(os.path.join(BW, grid, 'cr_base.npz'))
    if m is None:
        return dict(DISTANCES), False
    p = m['point']
    return dict(H0=float(p['CRH0']), OM=float(p['CROM']), WB=float(p['WBH2']),
                NS=float(p['NS'])), True


def build(tag, grid, th0, lens=True):
    g_dir = os.path.join(BW, grid)
    ls, Dl = load(os.path.join(g_dir, f'{tag}_base.npz'))
    m0 = binned(ls, Dl, lens)
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    g, h = {}, {}
    mb = m0[ok]
    for k in STEP:
        mp = binned(*load(os.path.join(g_dir, f'{tag}_{k}p.npz')), lens)[ok]
        mm = binned(*load(os.path.join(g_dir, f'{tag}_{k}m.npz')), lens)[ok]
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


def fit(tag, grid, th0):
    B = build(tag, grid, th0)
    n = int(B['ok'].sum())
    c0 = chi2_at(B, np.zeros(4))
    r = minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                 options=dict(xatol=1e-4, fatol=1e-3, maxiter=6000))
    flat = {}
    for i, k in enumerate(STEP):
        e = np.zeros(4)
        e[i] = STEP[k]
        flat[k] = min(chi2_at(B, r.x + e) - r.fun, chi2_at(B, r.x - e) - r.fun)
    return dict(x=r.x, fun=r.fun, n=n, c0=c0, flat=flat)


def verified(fn):
    ls, Dl = load(os.path.join(SPEC, fn))
    c, n, _A, _lo, _hi = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))
    return c, n, ls, Dl


def comb(P, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(P[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def residuals(ls, Dl):
    """the receipt's own two follow-ups: the acoustic phase and the fourth peak, per cent out."""
    P = [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=3)[0][:4]]
    _, phi = comb(P)
    _, phi_sky = comb(SKY)
    return abs(phi / phi_sky - 1) * 100, abs(P[3] / SKY[3] - 1) * 100, P


print(__doc__)
print(BAR)
print("  PART 1 -- THE TWO OBSTRUCTIONS, EACH WITH THE NAMESAKE ARM AS ITS CONTROL")
print(BAR)
TH = {}
for arm in ('namesake', 'aor'):
    TH[arm], has = centre_of(ARM[arm]['grid'])
    print(f"    {arm:>9} ({ARM[arm]['grid']:>20}): " + "  ".join(f"{k} {TH[arm][k]:.6f}" for k in STEP)
          + f"   [{'manifest' if has else 'no manifest'}]")
check("⒜ THE SAME CENTRE SPLIT AS GRID READER 1, on the 132-bin grid: the arm-of-record grid sits "
      "at the arm of record's fitted point and the namesake's at the distances' point.  ⇒ ** So the "
      "receipt's title figure -- whether the background stays where the DISTANCES put it -- cannot "
      "be read from this bank either **",
      all(abs(TH['namesake'][k] - DISTANCES[k]) < 1e-9 for k in STEP)
      and abs(TH['aor']['H0'] - 68.57073) < 1e-5 and abs(TH['aor']['OM'] - 0.291246) < 1e-6,
      f"namesake H0 {TH['namesake']['H0']:.5f}, arm of record H0 {TH['aor']['H0']:.5f}")

_d = {}
for arm in ('namesake', 'aor'):
    b = np.asarray(np.load(os.path.join(BW, ARM[arm]['grid'], 'cr_base.npz'))['Dl'], float)
    v = np.asarray(np.load(os.path.join(SPEC, ARM[arm]['ver']))['Dl'], float)
    _d[arm] = (float(np.max(np.abs(v - b))), float(np.max(np.abs(b))))
    print(f"    {arm:>9}: max |verify - cr_base| = {_d[arm][0]:.4e}  "
          f"({_d[arm][0] / _d[arm][1]:.2e} of the peak)")
check("⒝ AND THE VERIFICATION RUN IS THE BASE ON THE ARM OF RECORD -- bit-identical -- WHERE ON "
      "THE NAMESAKE ARM IT IS A DIFFERENT RUN AT A DIFFERENT POINT, 12 per cent of the peak away.  "
      "⇒ ** The namesake arm is what makes this a measurement rather than an assumption: these "
      "files are NOT built as copies of the base, so the identity is a missing run **",
      _d['aor'][0] == 0.0 and _d['namesake'][0] / _d['namesake'][1] > 0.1,
      f"arm of record {_d['aor'][0]:.3e}, namesake {_d['namesake'][0] / _d['namesake'][1]:.3f} "
      f"of peak")

_m = manifest_of(os.path.join(SPEC, ARM['aor']['ver']))
_held = str(_m.get('held', ''))
_sw = str(_m.get('switches', ''))
print(f"\n    the arm-of-record file's own record, both halves:")
print(f"      held:     {_held}")
print(f"      switches: {_sw}")
check("⛔⛭ THE MANIFEST'S PROSE AND ITS OWN SWITCHES DISAGREE: the prose places the file at the "
      "cc66 refit minimum `~68.6077/0.2967/0.0217/0.9949`, the switches at `68.570730/0.291246`, "
      "and the DATA agrees with the switches -- the file is the grid base.  ⇒ ** The "
      "machine-readable half is right; the prose would tell a reader there is a verification run "
      "at the refit minimum when there is not **",
      '68.6077' in _held and 'CRH0=68.570730' in _sw
      and abs(float(_m['point']['CRH0']) - 68.57073) < 1e-5,
      f"held names 68.6077, switches name {_m['point']['CRH0']}")

print()
print(BAR)
print("  PART 2 -- THE CONTROL AND THE TWO ARMS")
print(BAR)
C = fit('lcdm', CTL['grid'], CTL0)
c_ver, c_nb, c_ls, c_Dl = verified(CTL['ver'])
c_res = residuals(c_ls, c_Dl)
print(f"    control: {C['n']} bins, at the centre {C['c0']:.1f} ({C['c0'] / C['n']:.2f}/bin), "
      f"refitted {C['fun']:.1f} ({C['fun'] / C['n']:.2f}/bin), real run {c_ver:.1f} "
      f"({c_ver / c_nb:.2f}/bin); phase {c_res[0]:.1f}%, fourth peak {c_res[1]:.1f}%")
A = {}
for arm in ('namesake', 'aor'):
    f = fit('cr', ARM[arm]['grid'], TH[arm])
    v, nb, ls, Dl = verified(ARM[arm]['ver'])
    res = residuals(ls, Dl)
    A[arm] = dict(f=f, ver=v, nb=nb, res=res)
    print(f"\n    --- {arm} ---")
    print("      " + "   ".join(f"{k} {f['x'][i]:+.4f} ({100 * f['x'][i] / TH[arm][k]:+.3f}%)"
                                for i, k in enumerate(STEP)))
    print(f"      chi^2 at the centre {f['c0']:.1f} ({f['c0'] / f['n']:.2f}/bin), refitted "
          f"{f['fun']:.1f} ({f['fun'] / f['n']:.2f}/bin), banked run {v:.1f} ({v / nb:.2f}/bin), "
          f"d {v - f['fun']:+.1f}")
    print(f"      ratios: banked run {v / c_ver:.2f}x   at the centre {f['c0'] / C['c0']:.2f}x")
    print(f"      phase {res[0]:.1f}% out, fourth peak {res[1]:.1f}% out; peaks "
          f"{[int(p) for p in res[2]]}")

N, O = A['aor'], A['namesake']
check("⛔ THE LICENCE GATE: the namesake arm reproduces the receipt's published figures -- H0 "
      "+0.0077 at 0.011%, Omega_m -0.0006 at 0.20%, n_s wanting 0.9949, the ratio 1.45x at the "
      "verified minimum against 2.22x as-computed, and the phase 2.3% -> 4.5% with the fourth peak "
      "0.9% -> 0.7%",
      abs(O['f']['x'][0] - 0.0077) < 5e-4
      and abs(100 * O['f']['x'][1] / DISTANCES['OM'] + 0.20) < 5e-3
      and abs(DISTANCES['NS'] + O['f']['x'][3] - 0.9949) < 5e-4
      and abs(O['ver'] / c_ver - 1.45) < 5e-3
      and abs(O['f']['c0'] / C['c0'] - 2.22) < 5e-3
      and abs(O['res'][0] - 4.5) < 0.05 and abs(O['res'][1] - 0.7) < 0.05,
      f"H0 {O['f']['x'][0]:+.4f}, OM {100 * O['f']['x'][1] / DISTANCES['OM']:+.3f}%, n_s "
      f"{DISTANCES['NS'] + O['f']['x'][3]:.4f}, {O['ver'] / c_ver:.2f}x / "
      f"{O['f']['c0'] / C['c0']:.2f}x, phase {O['res'][0]:.1f}%, fourth {O['res'][1]:.1f}%")

print()
print(BAR)
print("  PART 3 -- WHAT MOVES, AND WHAT IS AN ABSENCE RATHER THAN A MOVE")
print(BAR)
ROWS = [('chi^2 refitted', O['f']['fun'], N['f']['fun'], '.1f', 1),
        ('per bin, refitted', O['f']['fun'] / O['f']['n'], N['f']['fun'] / N['f']['n'], '.2f', 1),
        ('banked run chi^2', O['ver'], N['ver'], '.1f', 2),
        ('ratio, banked run', O['ver'] / c_ver, N['ver'] / c_ver, '.2f', 2),
        ('phase, per cent out', O['res'][0], N['res'][0], '.1f', 1),
        ('fourth peak, per cent out', O['res'][1], N['res'][1], '.1f', 1),
        ('flatness, cheapest step', min(O['f']['flat'].values()), min(N['f']['flat'].values()),
         '.1f', 1),
        ('H0 move', O['f']['x'][0], N['f']['x'][0], '+.4f', 0),
        ('Omega_m move, per cent', 100 * O['f']['x'][1] / TH['namesake']['OM'],
         100 * N['f']['x'][1] / TH['aor']['OM'], '+.3f', 0),
        ('n_s wanted', TH['namesake']['NS'] + O['f']['x'][3], TH['aor']['NS'] + N['f']['x'][3],
         '.4f', 0),
        ('chi^2 at the centre', O['f']['c0'], N['f']['c0'], '.1f', 0),
        ('ratio at the centre', O['f']['c0'] / C['c0'], N['f']['c0'] / C['c0'], '.2f', 0)]
print(f"    {'figure':>28} {'namesake':>12} {'arm of record':>14}   verdict")
for lab, o, n, f, readable in ROWS:
    if readable == 2:
        v = '⚠ A BOUND, not like-for-like -- the AOR run is the base (⒝)'
    elif not readable:
        v = '⛔ NOT COMPARABLE -- different centre (⒜)'
    elif abs(n - o) < 1e-9:
        v = 'unchanged'
    else:
        v = 'MOVED' if abs(n - o) > 0.005 * max(1e-9, abs(o)) else 'moved (trace)'
    print(f"    {lab:>28} {format(o, f):>12} {format(n, f):>14}   {v}")

print()
print(BAR)
print("  PART 4 -- THE CARRY, AND THE GATES THAT CAN STILL BE ASKED")
print(BAR)
_solo = residuals(*verified(ARM['aor']['ver'])[2:4])
check("⛭ THE CARRY HAS NOTHING TO ACT ON, measured the same way as on grid reader 1: the arm's "
      "phase residual computed from the arm spectrum and the SKY alone is bit-identical to the "
      "pipeline's, so no control quantity enters it.  ** Class 3 **",
      _solo[0] == N['res'][0] and _solo[1] == N['res'][1],
      f"solo {_solo[0]:.6f}% against pipeline {N['res'][0]:.6f}%")
check("the arm is still disfavoured against the control on the banked run", N['ver'] > c_ver,
      f"{N['ver']:.1f} against {c_ver:.1f}")
check("every parameter is still a live direction on both arms",
      all(v > 5.0 for v in N['f']['flat'].values()) and all(v > 5.0 for v in C['flat'].values()),
      f"arm min {min(N['f']['flat'].values()):.1f}, control min {min(C['flat'].values()):.1f}")
# ⛔⛭⛭ ** AND THE ARM OF RECORD STRENGTHENS THE WITHDRAWAL OF THIS RECEIPT'S OWN PHASE FIGURE. **
#   This receipt reads its peaks with `argrelextrema` on the spectrum's own LSTEP=8 grid -- the RAW
#   locator -- and `r6825+cc66.25` withdrew the `4.5%` it reported on exactly that ground: at that
#   resolution the CONTROL returns the same `4.5%`, so the number could not distinguish the arms.
#   ⇒ *On the arm of record the same raw statistic reads `0.7%`, because the arm's SECOND peak lands
#   at 532 where the control's and the namesake's both land at 540 -- one and a half grid steps.*
#   ** So the quantised figure does not merely lose precision: it REVERSES the comparison, making
#   the arm of record look three times BETTER than the control where the namesake looked equal to
#   it.  Neither reading is about the arms. **  ⌗ *The refined locator is what carries the verdict,
#   and `r7641+cc66.39` measured it on this same arm: 3.7 per cent against the control's 1.6.*
check("⛔⛭⛭ THE ARM OF RECORD STRENGTHENS THE WITHDRAWAL OF THIS RECEIPT'S `4.5%`: on the raw "
      "LSTEP=8 locator the arm of record reads 0.7 per cent against the control's 4.5, where the "
      "namesake read 4.5 against 4.5.  ⇒ ** The quantised figure REVERSES the comparison rather "
      "than merely blurring it, and the second peak crossing a grid step (532 against 540) is why. "
      " The refined reading -- 3.7 against 1.6 at `cc66.39` -- is the one that carries the verdict **",
      abs(O['res'][0] - c_res[0]) < 0.05 and N['res'][0] < 0.5 * c_res[0]
      and int(N['res'][2][1]) == 532 and int(c_res[2][1]) == 540,
      f"namesake {O['res'][0]:.1f}% against control {c_res[0]:.1f}%; arm of record "
      f"{N['res'][0]:.1f}%, its second peak {N['res'][2][1]:.0f} against {c_res[2][1]:.0f}")

#: ⌗ ** AND THE RATIO IS REPORTED AS A BOUND, NOT A POINT, BECAUSE THE TWO BANKED RUNS ARE NOT
#: LIKE-FOR-LIKE. **  The namesake's banked run sits at its own refit minimum; the arm of record's IS
#: the base (⒝).  A refit can only lower a chi^2, so the arm of record's banked ratio is an UPPER
#: bound and its own response model's refit from that centre is the lower one.  *Either way it does
#: not fall below the namesake's 1.45, which is the only claim this bank supports.*
_lo, _hi = N['f']['fun'] / C['fun'], N['ver'] / c_ver
print(f"    the arm-of-record ratio is bounded rather than pointed: {_lo:.2f}x (its own response "
      f"model's refit) to {_hi:.2f}x (its banked base), against the namesake's "
      f"{O['ver'] / c_ver:.2f}x at a real refit minimum")
check("⌗ AND THE RATIO DOES NOT FALL ON THE ARM OF RECORD, stated as the bound the bank supports "
      "rather than as a point: between 1.48x (its own model's refit from its centre) and 1.54x "
      "(its banked base, which is unrefitted), against the namesake's 1.45x at a real verified "
      "minimum.  ⇒ ** Reported as a bound because the two banked runs are not like-for-like, which "
      "is ⒝ again **",
      _lo > O['ver'] / c_ver and _hi > _lo and abs(_lo - 1.48) < 0.01 and abs(_hi - 1.54) < 0.01,
      f"{_lo:.3f}x to {_hi:.3f}x against {O['ver'] / c_ver:.3f}x")

print()
print(BAR)
print(f"  {'ALL PASS' if not fail else 'FAILURES: ' + str(len(fail))}")
print(BAR)
sys.exit(1 if fail else 0)
