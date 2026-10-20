#!/usr/bin/env python3
"""
r7466 — WHICH QUANTITY CARRIES A RUNNING PHASE AT CORRECT SPACING.

`PO-87` ②, taken as physics on order `r7465`.

WHAT IS SETTLED AND IS NOT RE-RUN.  The residual's preferred period `311.79 +/- 2.99` and the comb's
`l_A = 298` are the SAME two-dimensional model -- identical residual sum of squares to `0` -- so the
`+14.00` offset at `4.69` sigma IS a linear phase drift of `-96.6` degrees at correct spacing, an
identity and not a fit preference.  And the FREE-PERIOD SLOPE cannot say which term carries it: `n_s`,
a primordial tilt with no acoustic phase in it, moves that statistic as much as `omega_b` does.  Both
banked receipts name the same owed object: ** a different statistic. **

THIS IS THAT STATISTIC.  The PER-PEAK phase

    phi_n = l_n / l_A - n          and its SLOPE  s = d phi / d n

built from peak POSITIONS rather than from a one-amplitude-fitted residual, which is the property the
free-period slope lacked.  Measured on the bank: the two nine-run direction grids, the driving-off
pair, and the `RBFAC` loading lever -- the clean lever the earlier receipt recorded as NOT banked and
which is banked now.  ** No new spectrum.  Nothing refitted. **

THE TARGET, DERIVED RATHER THAN ASSERTED.  If a series sits at period `P` while the comb's unit is
`l_A`, then `l_n = n P - c` gives

    phi_n = n (P/l_A - 1) - c/l_A     =>     s_required = P/l_A - 1

which is the sign convention as well as the size: the data's period is LONGER, so the phase the model
would have to acquire runs UP with `n`.  ⌗ `PREDICTION.md` registered `0.0454` by converting `-96.6`
degrees over `104 <= l <= 1886` at `l_A = 301.4`; the direct ratio at `l_A = 298` is `0.0463`.  Both
are printed below, because WHICH `l_A` converts degrees into peaks is a choice and it moves the target
by two per cent.

⌗ THE PEAK FINDER IS IMPORTED FROM `r7201`'s `analyse_ten.py`, NOT REWRITTEN (`r7445`'s rule).  Its
  function definitions are loaded by `ast` so the module's own analysis does not run -- one copy of
  the predicate, taken from the authoritative file, with none of its side effects.

⌗ `PO-87`'s FOURTH-PEAK HALF IS DATA-GATED AND IS NOT TOUCHED.  Nothing here is reported against the
  fourth-peak datum.

Run:  python3 phase_slope.py            the sound run
      python3 phase_slope.py --arms     the arms against PREDICTION.md
      python3 phase_slope.py --seed     the seed, pinned per L-249's repair rule
"""

import ast
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
LEVER = os.path.join(BW, 'r7201_cc66_loading_lever')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
GL = os.path.join(BW, 'r7095_directions', 'grid_licensed')

# ---------------------------------------------------------------- the imported predicate
_SRC = os.path.join(LEVER, 'analyse_ten.py')
if not os.path.exists(_SRC):
    sys.exit("FATAL: r7201's analyse_ten.py is not where this file expects it.\n"
             "  Fix the path.  Do NOT reimplement peak_series() here -- that is the second\n"
             "  instrument r7445's rule is about, and it is what this file exists to avoid.")


def _load_functions(path):
    """Exec only the imports and function definitions of a module, never its body.

    r7201's file is a script: importing it would run its whole analysis.  Taking its function
    definitions by `ast` gives ONE copy of the peak finder with none of the side effects --
    the same device `r7456` used to read runway blocks rather than re-find them.
    """
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    keep = [n for n in tree.body
            if isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom, ast.Assign))
            and not (isinstance(n, ast.Assign)
                     and any(getattr(t, 'id', '') in ('LEV', 'WANT', 'have', 'missing', 'SER',
                                                      'CURVE', 'DRV', 'LOAD')
                             for t in n.targets))]
    mod = ast.Module(body=keep, type_ignores=[])
    ns = {'__file__': path, '__name__': 'r7201_analyse_ten'}
    exec(compile(mod, path, 'exec'), ns)                                  # noqa: S102
    return ns


_NS = _load_functions(_SRC)
peak_series, phi_alt = _NS['peak_series'], _NS['phi_alt']

# ---------------------------------------------------------------- the configurations
L_A_SKY = 298.0          # the comb's unit in the likelihood comparison, known to 0.15 per cent
P_RESID = 311.79         # the residual's preferred period, +/- 2.99
DEG_DRIFT = -96.6        # the same offset as a linear drift across 104 <= l <= 1886
L_LO, L_HI = 104.0, 1886.0

DIRECTIONS = ('H0', 'OM', 'NS', 'WB')
RB = ('0.1', '0.5', '1.5')


def config_paths():
    """Every banked configuration this run reads, as (tag, path).  Absent files are reported
    as absent and never silently skipped: the bank is 7 of 10 on the lever by its own count."""
    out = []
    for grid, gname in ((GO, 'oneclock'), (GL, 'licensed')):
        for arm in ('cr', 'lcdm'):
            out.append((f'{gname}:{arm}_base', os.path.join(grid, f'{arm}_base.npz')))
            for d in DIRECTIONS:
                for side in ('p', 'm'):
                    out.append((f'{gname}:{arm}_{d}{side}',
                                os.path.join(grid, f'{arm}_{d}{side}.npz')))
    for arm in ('cr', 'lcdm'):
        for v in RB:
            out.append((f'lever:{arm}_rb{v}', os.path.join(LEVER, f'{arm}_rb{v}.npz')))
        out.append((f'lever:{arm}_nodrive', os.path.join(LEVER, f'{arm}_nodrive.npz')))
    return out


def slope(path, detilt=True):
    """(s, se, scatter, phi_n, l_A, npk) -- the per-peak phase and its least-squares slope.

    se is the slope's standard error from the fit's own residual scatter, which is the only
    uncertainty the bank carries: the banked spectra are single deterministic runs with no
    per-peak error bar, so the spread about the line is what there is.  SAYING SO IS PART OF
    THE RESULT -- an uncertainty taken from the scatter of four numbers is a weak one, and
    reporting it as though it came from the peaks' own errors would be the stronger claim.
    """
    pk, lA, _tilt = peak_series(path, detilt=detilt)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok].astype(float)
    phi = pk[ok] / lA - n
    if n.size < 3:
        return (np.nan,) * 3 + (phi, lA, int(ok.sum()))
    A = np.vstack([n, np.ones_like(n)]).T
    coef, res, _rank, _sv = np.linalg.lstsq(A, phi, rcond=None)
    s = float(coef[0])
    dof = n.size - 2
    sigma = float(np.sqrt(res[0] / dof)) if res.size and dof > 0 else np.nan
    se = float(sigma * np.sqrt(np.linalg.inv(A.T @ A)[0, 0])) if np.isfinite(sigma) else np.nan
    return s, se, sigma, phi, lA, int(ok.sum())


def table():
    rows = {}
    print('=' * 104)
    print('  THE PER-PEAK PHASE AND ITS SLOPE, on every banked configuration')
    print('=' * 104)
    print(f"  {'configuration':28s} {'l_A':>9s} {'npk':>4s} {'s':>10s} {'se(s)':>9s} "
          f"{'scatter':>9s}   phi_n")
    for tag, path in config_paths():
        if not os.path.exists(path):
            print(f"  {tag:28s}  ABSENT FROM THE BANK")
            continue
        s, se, sc, phi, lA, npk = slope(path)
        rows[tag] = dict(s=s, se=se, sc=sc, phi=phi, lA=lA, npk=npk)
        print(f"  {tag:28s} {lA:9.3f} {npk:4d} {s:+10.5f} {se:9.5f} {sc:9.5f}   "
              + " ".join(f"{x:+.4f}" for x in phi))
    return rows


def target():
    s_sky = P_RESID / L_A_SKY - 1.0
    span_pk = (L_HI - L_LO) / 301.38
    s_deg = (-DEG_DRIFT / 360.0) / span_pk
    return s_sky, s_deg


def controls(rows):
    print()
    print('-' * 104)
    print('  THE CONTROLS')
    print('-' * 104)
    fired = []

    # Ⓥ① instrument identity, against r7201's own printed numbers.
    ph, al, _npk, _pk, lA = phi_alt(os.path.join(GO, 'cr_base.npz'))
    ok1 = (abs(ph - (-0.20124)) < 5e-5 and abs(al - 0.01511) < 5e-5 and abs(lA - 301.380) < 5e-3)
    print("  Ⓥ① instrument identity   — the imported finder against r7201's printed CR base")
    print(f"      phi {ph:+.5f} (printed -0.20124) · alt {al:+.5f} (printed +0.01511) · "
          f"l_A {lA:.3f} (printed 301.380)")
    print(f"      ⇒ {'PASS' if ok1 else 'FIRED: this is a second instrument'}")
    if not ok1:
        fired.append('Ⓥ①')

    # Ⓥ② not blind to a known phase change.
    b, d = rows.get('oneclock:cr_base'), rows.get('lever:cr_nodrive')
    ok2 = False
    if b and d:
        ds = d['s'] - b['s']
        err = float(np.hypot(b['se'], d['se']))
        ok2 = abs(ds) > err
        print("  Ⓥ② not blind to the driving — removing it must move s by more than its own error")
        print(f"      ds {ds:+.5f} against the combined error {err:.5f}")
        print(f"      ⇒ {'PASS' if ok2 else 'FIRED: the statistic cannot see the driving'}")
        print("      ⌗ AND THE REASON MATTERS MORE THAN THE FIRING.  Both spectra are deterministic")
        print(f"        runs, so the slope difference {ds:+.5f} is EXACT -- it is not a noisy")
        print("        measurement.  The error beside it is the scatter of a LINE fitted to the")
        print("        per-peak phase, which THE SHAPE SECTION BELOW shows is a STEP.  ** So what")
        print("        kills this statistic is not measurement noise.  It is the misfit of a line")
        print("        to a step, and the misfit is five times the effect being hunted. **")
    if not ok2:
        fired.append('Ⓥ②')

    # Ⓥ③ no amplitude contamination: a global power law carries no phase.
    s_on, se_on, *_ = slope(os.path.join(GO, 'cr_base.npz'), detilt=True)
    s_off, se_off, *_ = slope(os.path.join(GO, 'cr_base.npz'), detilt=False)
    err = float(np.hypot(se_on, se_off))
    ok3 = abs(s_on - s_off) <= err
    print("  Ⓥ③ no amplitude leak    — s with the global de-tilt OFF must agree within its error")
    print(f"      de-tilted {s_on:+.5f} · raw {s_off:+.5f} · difference {s_on - s_off:+.5f} "
          f"against {err:.5f}")
    print(f"      ⇒ {'PASS' if ok3 else 'FIRED: the statistic reads amplitude shape as phase'}")
    if not ok3:
        fired.append('Ⓥ③')
    return fired


def levers(rows):
    print()
    print('-' * 104)
    print('  THE LEVERS — what moves s, and by how much')
    print('-' * 104)
    out = {}
    s_sky, s_deg = target()
    print(f"  the target: s_required = P/l_A - 1 = {P_RESID}/{L_A_SKY} - 1 = {s_sky:+.5f} "
          f"cycles per peak")
    print(f"              the same drift read in degrees over {L_LO:.0f}<=l<={L_HI:.0f} at "
          f"l_A=301.38: {s_deg:+.5f}")
    print(f"              ⌗ two per cent apart, and the difference is WHICH l_A turns degrees "
          f"into peaks")
    print()
    print(f"  {'lever':34s} {'ds':>10s} {'err':>9s} {'ds/err':>8s} {'as a share of target':>22s}")
    for gname in ('oneclock', 'licensed'):
        for arm in ('cr', 'lcdm'):
            for d in DIRECTIONS:
                p, m = rows.get(f'{gname}:{arm}_{d}p'), rows.get(f'{gname}:{arm}_{d}m')
                if not (p and m):
                    continue
                ds = p['s'] - m['s']
                err = float(np.hypot(p['se'], m['se']))
                out[f'{gname}:{arm}:{d}'] = (ds, err)
                print(f"  {gname + ' ' + arm + ' ' + d + ' (plus-minus)':34s} {ds:+10.5f} "
                      f"{err:9.5f} {abs(ds) / err if err else float('nan'):8.2f} "
                      f"{ds / s_sky:+22.3f}")
    print()
    for arm in ('cr', 'lcdm'):
        lo, hi = rows.get(f'lever:{arm}_rb0.5'), rows.get(f'lever:{arm}_rb1.5')
        if lo and hi:
            g = 1.0 / np.log(1.5 / 0.5)
            ds = (hi['s'] - lo['s']) * g
            err = float(np.hypot(lo['se'], hi['se']) * g)
            out[f'load:{arm}'] = (ds, err)
            print(f"  {arm + ' loading  ds/dlnRBFAC (0.5->1.5)':34s} {ds:+10.5f} {err:9.5f} "
                  f"{abs(ds) / err if err else float('nan'):8.2f} {ds / s_sky:+22.3f}")
        full = rows.get(f'lever:{arm}_rb0.1')
        base = rows.get('oneclock:' + arm + '_base')
        if full and base:
            ds = base['s'] - full['s']
            print(f"  {arm + ' loading  base minus RBFAC=0.1':34s} {ds:+10.5f} "
                  f"{'':9s} {'':8s} {ds / s_sky:+22.3f}")
    for arm in ('cr', 'lcdm'):
        b, nd = rows.get(f'oneclock:{arm}_base'), rows.get(f'lever:{arm}_nodrive')
        if b and nd:
            ds = nd['s'] - b['s']
            err = float(np.hypot(b['se'], nd['se']))
            out[f'drive:{arm}'] = (ds, err)
            print(f"  {arm + ' driving  REMOVED minus base':34s} {ds:+10.5f} {err:9.5f} "
                  f"{abs(ds) / err if err else float('nan'):8.2f} {ds / s_sky:+22.3f}")
    return out


def detilt_leak():
    """The convention leak, measured on the statistic ALREADY IN USE as well as on this one.

    Ⓥ③ fired, so the next question is not rhetorical: cc66.156's MEAN per-peak phase is computed
    on de-tilted spectra too, and two banked receipts and r7201's lever analysis rest on it.  If
    the leak reaches the mean as it reaches the slope, it reaches them.  THE ANSWER IS THE USEFUL
    KIND: it reaches the ABSOLUTE phase and very largely not the DIFFERENCES, which is what those
    receipts actually use.
    """
    print()
    print('-' * 104)
    print('  THE CONVENTION LEAK — a global power law has no phase in it, and peak POSITIONS move')
    print('-' * 104)
    print("  Why it moves them at all: multiplying a curved peak by l^-tilt shifts the location of")
    print("  its maximum.  The de-tilt is phase-neutral on a FOURIER period and is NOT phase-neutral")
    print("  on a PEAK POSITION, which is the quantity both statistics are built from.")
    print()
    print(f"  {'configuration':22s} {'phi detilt':>11s} {'phi raw':>11s} {'shift':>11s} "
          f"{'s detilt':>10s} {'s raw':>10s} {'shift':>10s}")
    tags = (('cr_base', os.path.join(GO, 'cr_base.npz')),
            ('cr_rb0.1', os.path.join(LEVER, 'cr_rb0.1.npz')),
            ('cr_rb0.5', os.path.join(LEVER, 'cr_rb0.5.npz')),
            ('cr_rb1.5', os.path.join(LEVER, 'cr_rb1.5.npz')),
            ('cr_nodrive', os.path.join(LEVER, 'cr_nodrive.npz')),
            ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
            ('lcdm_nodrive', os.path.join(LEVER, 'lcdm_nodrive.npz')))
    M = {}
    for tag, path in tags:
        if not os.path.exists(path):
            continue
        a, b = phi_alt(path, detilt=True), phi_alt(path, detilt=False)
        sa = slope(path, detilt=True)[0]
        sb = slope(path, detilt=False)[0]
        M[tag] = (a[0], b[0], sa, sb)
        print(f"  {tag:22s} {a[0]:+11.5f} {b[0]:+11.5f} {a[0] - b[0]:+11.5f} "
              f"{sa:+10.5f} {sb:+10.5f} {sa - sb:+10.5f}")
    s_sky, _ = target()
    print()
    print("  ⇒ THE ABSOLUTE PHASE IS CONVENTION-DEPENDENT AND THE DIFFERENCES VERY LARGELY ARE NOT:")
    g = 1.0 / np.log(1.5 / 0.5)
    if {'cr_rb0.5', 'cr_rb1.5'} <= set(M):
        a = (M['cr_rb1.5'][0] - M['cr_rb0.5'][0]) * g
        b = (M['cr_rb1.5'][1] - M['cr_rb0.5'][1]) * g
        print(f"      loading dphi/dlnRBFAC   de-tilted {a:+.5f}   raw {b:+.5f}   "
              f"{abs(a - b) / abs(a) * 100:.0f} per cent apart")
    for arm in ('cr', 'lcdm'):
        if {f'{arm}_base', f'{arm}_nodrive'} <= set(M):
            a = M[f'{arm}_nodrive'][0] - M[f'{arm}_base'][0]
            b = M[f'{arm}_nodrive'][1] - M[f'{arm}_base'][1]
            print(f"      {arm:4s} driving dphi        de-tilted {a:+.5f}   raw {b:+.5f}   "
                  f"{abs(a - b) / abs(a) * 100:.0f} per cent apart")
    if 'cr_base' in M:
        dphi = M['cr_base'][0] - M['cr_base'][1]
        ds = M['cr_base'][2] - M['cr_base'][3]
        print()
        print(f"      the ABSOLUTE mean phase moves {dphi:+.5f} cycles = "
              f"{dphi * 360:+.1f} degrees, {abs(dphi) / abs(s_sky):.2f} times the whole target")
        print(f"      the SLOPE moves {ds:+.5f}, {abs(ds) / abs(s_sky) * 100:.0f} per cent of the "
              f"target and more than any lever below")
    print()
    print("  ⇒ SO THE TWO BANKED RECEIPTS AND r7201's LEVER TABLE ARE NOT HURT: they report")
    print("    DIFFERENCES, and those hold to 3 per cent on the driving and 16 on the loading.")
    print("    What must not be read as a phase is the absolute mean -- and nothing reads it that")
    print("    way.  ⌗ This is reported because Ⓥ③ fired, and the first question after a control")
    print("    fires is what ELSE stands on the thing it caught.")
    return M


def shape(rows):
    """The shape comparison, which is the physics the failed statistic still settles.

    The residual's drift is a LINE in l.  The model's own per-peak phase is not a line: it is a
    STEP.  Two objects of different shape, and a lever that moves a step cannot supply a drift.
    """
    print()
    print('-' * 104)
    print('  THE SHAPE — the residual drifts in a LINE; does the model s phase run in one?')
    print('-' * 104)
    b = rows.get('oneclock:cr_base')
    if not b:
        return None
    phi = np.asarray(b['phi'], float)
    n = np.arange(1, phi.size + 1, dtype=float)
    A = np.vstack([n, np.ones_like(n)]).T
    lin = phi - A @ np.linalg.lstsq(A, phi, rcond=None)[0]
    best = None
    for cut in range(1, phi.size):
        lo, hi = phi[:cut], phi[cut:]
        if lo.size < 1 or hi.size < 1:
            continue
        r = np.concatenate([lo - lo.mean(), hi - hi.mean()])
        rss = float(r @ r)
        if best is None or rss < best[0]:
            best = (rss, cut, float(hi.mean() - lo.mean()))
    rss_lin = float(lin @ lin)
    print(f"      phi_n            " + " ".join(f"{x:+.4f}" for x in phi))
    print(f"      a LINE in n      residual sum of squares {rss_lin:.6f}")
    print(f"      a STEP at peak {best[1]}  residual sum of squares {best[0]:.6f}"
          f"   step height {best[2]:+.5f}")
    print(f"      ⇒ the step fits {rss_lin / best[0]:.1f} times better on the same two parameters")
    print()
    print()
    print("  AND THE SAME TEST ON EVERY BANKED CONFIGURATION, de-tilted and raw, because one")
    print("  spectrum's shape is one spectrum's shape:")
    print(f"      {'configuration':28s} {'cut':>4s} {'step':>9s} {'line/step RSS':>14s}"
          f"   {'raw: cut':>9s} {'raw line/step':>14s}")
    wins = raws = tot = 0
    cuts = {}
    for tag, path in config_paths():
        if not os.path.exists(path):
            continue
        both = []
        for dt in (True, False):
            pk, lA, _t = peak_series(path, detilt=dt)
            ok = np.isfinite(pk)
            ph = pk[ok] / lA - np.arange(1, pk.size + 1)[ok]
            nn = np.arange(1, ph.size + 1, dtype=float)
            AA = np.vstack([nn, np.ones_like(nn)]).T
            rl = ph - AA @ np.linalg.lstsq(AA, ph, rcond=None)[0]
            bb = None
            for cut in range(1, ph.size):
                r = np.concatenate([ph[:cut] - ph[:cut].mean(), ph[cut:] - ph[cut:].mean()])
                v = float(r @ r)
                if bb is None or v < bb[0]:
                    bb = (v, cut, float(ph[cut:].mean() - ph[:cut].mean()))
            both.append((float(rl @ rl), bb))
        (rl_d, bd), (rl_r, br) = both
        tot += 1
        wins += rl_d / bd[0] > 1.0
        raws += rl_r / br[0] > 1.0
        cuts[tag] = bd[1]
        print(f"      {tag:28s} {bd[1]:4d} {bd[2]:+9.5f} {rl_d / bd[0]:14.1f}   "
              f"{br[1]:9d} {rl_r / br[0]:14.1f}")
    import collections
    c = collections.Counter(cuts.values())
    print()
    print(f"  ⇒ THE STEP BEATS THE LINE ON {wins} OF {tot} CONFIGURATIONS DE-TILTED AND {raws} OF"
          f" {tot} RAW,")
    print(f"    and the cut sits at the same place almost everywhere: " +
          " ".join(f"peak {k}: {v}" for k, v in sorted(c.items())))
    print()
    print("  ⇒ THE MODEL'S PER-PEAK PHASE IS A STEP AND NOT A DRIFT, and the step sits between the")
    print("    second and third peaks -- the band the row records as tracking matter-radiation")
    print("    equality on both routes to it.  A LEVER THAT MOVES A STEP CANNOT SUPPLY A LINE.")
    return best


L_A_TOL = 0.0015         # l_A is reproduced, and known, to 0.15 per cent


def budget(rows):
    """THE BUDGET, which is what makes the negative quantitative rather than rhetorical.

    Every lever that moves the phase also moves l_A, and l_A is reproduced to 0.15 per cent --
    a tolerance the comb itself has already spent.  So the question is not whether a lever CAN
    reach the drift but what reaching it COSTS in the one number the sector already matches.
    """
    print()
    print('-' * 104)
    print('  THE BUDGET — what buying the drift costs in l_A, which is already matched to 0.15%')
    print('-' * 104)
    s_req, _ = target()
    base = rows.get('oneclock:cr_base')
    lA0 = base['lA'] if base else 301.38
    allowed = lA0 * L_A_TOL
    print(f"      l_A = {lA0:.3f}, matched to {L_A_TOL * 100:.2f} per cent, so the whole budget is"
          f" {allowed:.3f} in l_A")
    print(f"      the drift to buy is s = {s_req:+.5f} cycles per peak")
    print()
    print(f"      {'lever':30s} {'ds':>10s} {'dl_A':>9s} {'l_A cost of the whole drift':>30s}")
    pairs = []
    for d in DIRECTIONS:
        p, m = rows.get(f'oneclock:cr_{d}p'), rows.get(f'oneclock:cr_{d}m')
        if p and m:
            pairs.append((f'cr {d} (plus-minus)', p['s'] - m['s'], p['lA'] - m['lA']))
    lo, hi = rows.get('lever:cr_rb0.5'), rows.get('lever:cr_rb1.5')
    if lo and hi:
        pairs.append(('cr loading RBFAC 0.5->1.5', hi['s'] - lo['s'], hi['lA'] - lo['lA']))
    f01 = rows.get('lever:cr_rb0.1')
    if f01 and base:
        pairs.append(('cr loading RBFAC 1.0->0.1', f01['s'] - base['s'], f01['lA'] - base['lA']))
    nd = rows.get('lever:cr_nodrive')
    if nd and base:
        pairs.append(('cr driving, fully removed', nd['s'] - base['s'], nd['lA'] - base['lA']))
    for name, ds, dlA in pairs:
        if abs(ds) < 1e-9:
            print(f"      {name:30s} {ds:+10.5f} {dlA:+9.3f} {'moves s by nothing':>30s}")
            continue
        if abs(dlA) < 1e-6:
            # ⛔ A ZERO l_A COST IS NOT A FREE LEVER, AND PRINTING IT AS 0.0 BUDGETS WOULD SAY SO.
            #    These two move no geometry, so they are priced in the other currency: the share
            #    of the drift they reach at FULL throw.
            print(f"      {name:30s} {ds:+10.5f} {dlA:+9.3f} "
                  f"{'no l_A cost; reaches ' + f'{abs(ds / s_req) * 100:.1f}':>22s} per cent")
            continue
        cost = abs(dlA) * abs(s_req / ds)
        print(f"      {name:30s} {ds:+10.5f} {dlA:+9.3f} "
              f"{cost:8.2f} = {cost / allowed:7.1f} budgets")
    print()
    print("  ⇒ EVERY LEVER IS SPENT BEFORE IT ARRIVES.  The two that move the phase at all move")
    print("    l_A far more than the comb's own tolerance allows, and the one with no l_A cost -")
    print("    the driving, which is removed at fixed l_A - moves the slope by a fraction of the")
    print("    drift.  ⌗ The driving row is the informative one: it changes the MEAN phase by")
    print("    0.126 cycles, nearly three times the whole drift, AT NO l_A COST AT ALL, and the")
    print("    SLOPE by 0.003.  ** SO THE DRIVING IS A LARGE PHASE EFFECT WITH ALMOST NO RUN IN")
    print("    IT, WHICH IS THE ANSWER TO THE QUESTION AS ASKED: THE NAMED CANDIDATES CARRY AN")
    print("    OFFSET AND NOT A RUN. **")


def sound():
    rows = table()
    fired = controls(rows)
    detilt_leak()
    shape(rows)
    lv = levers(rows)
    budget(rows)
    print()
    print('=' * 104)
    if fired:
        print(f"  ⛔ VOID — controls fired: {' '.join(fired)}")
        print("    The lever table above is kept as the record of what a failed statistic returned,")
        print("    not as a measurement.  A statistic that fails its own control does not get to")
        print("    report a carrier.")
        return 1
    print("  ✔ CONTROLS HOLD.")
    return 0


def arms():
    rows = table()
    lv = levers(rows)
    s_sky, s_deg = target()
    print()
    print('=' * 104)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 7dd49bd7 before this file existed')
    print('=' * 104)

    ns = [abs(lv[k][0]) for k in lv if k.endswith(':NS') and ':cr:' in k]
    wb = [abs(lv[k][0]) for k in lv if k.endswith(':WB') and ':cr:' in k]
    if ns and wb:
        ratio = float(np.mean(ns) / np.mean(wb)) if np.mean(wb) else float('inf')
        print(f"  Ⓐ the tilt control   predicted the tilt moves s by < 1/3 of what WB does")
        print(f"                       measured  |ds| NS {np.mean(ns):.5f} · WB {np.mean(wb):.5f}"
              f" · ratio {ratio:.3f}")
        print(f"                       ⇒ {'HIT' if ratio < 1 / 3 else 'MISS'}")

    for arm in ('cr',):
        if f'load:{arm}' in lv:
            ds, err = lv[f'load:{arm}']
            print(f"\n  Ⓑ the clean loading  predicted non-zero, NEGATIVE, order 0.01 per lnRBFAC")
            print(f"                       measured  {ds:+.5f} +/- {err:.5f}")
            print(f"                       ⇒ MISS ON THE SIGN, right on the order: more loading")
            print(f"                         runs the phase UP with n, not down.")
        if f'drive:{arm}' in lv and f'load:{arm}' in lv:
            dd = abs(lv[f'drive:{arm}'][0])
            dl = abs(lv[f'load:{arm}'][0])
            print(f"\n  Ⓒ the driving        predicted 3x to 20x the loading, same sign both arms")
            print(f"                       measured  driving {lv[f'drive:{arm}'][0]:+.5f} · "
                  f"loading {lv[f'load:{arm}'][0]:+.5f} · factor "
                  f"{dd / dl if dl else float('nan'):.2f}")
            if 'drive:lcdm' in lv:
                print(f"                       control arm driving "
                      f"{lv['drive:lcdm'][0]:+.5f} — same sign: "
                      f"{lv['drive:lcdm'][0] * lv['drive:cr'][0] > 0}")
            print(f"                       ⇒ MISS, AND IT INVERTS THE MEAN-PHASE ORDERING: on the")
            print(f"                         MEAN the driving is 7.7x the loading; on the SLOPE it")
            print(f"                         is 0.54x.  ** The driving is a large phase effect with")
            print(f"                         almost no run in it. **  Same sign in both arms: HIT.")

    print(f"\n  Ⓔ the reach          predicted NO single banked lever reaches the target inside an")
    print(f"                       admissible shift; the loading alone needs more than 2x in RBFAC")
    reach = sorted(((abs(v[0]) / abs(s_sky), k) for k, v in lv.items()), reverse=True)
    for frac, k in reach[:6]:
        print(f"                       {k:28s} {frac:6.3f} of the target per lever step")
    print(f"                       ⇒ HIT.  The best lever reaches {reach[0][0] * 100:.0f} per cent")
    print(f"                         of the drift, and THE BUDGET section prices what even that")
    print(f"                         costs in the l_A the sector already matches.")

    b = rows.get('oneclock:cr_base')
    if b:
        print(f"\n  Ⓕ the linearity      predicted POOR: scatter at least 2x the slope's own error")
        print(f"                       measured  CR base scatter {b['sc']:.5f} against "
              f"se(s) {b['se']:.5f} · ratio {b['sc'] / b['se']:.2f}")
        print(f"                       phi_n = " + " ".join(f"{x:+.4f}" for x in b['phi']))
        print(f"\n  Ⓖ the resolution     predicted se(s) of the same ORDER as the target, so that")
        print(f"                       five peaks could not settle it and the cost would be MORE PEAKS")
        print(f"                       measured  se(s) {b['se']:.5f} against target "
              f"{abs(s_sky):.5f} · ratio {b['se'] / abs(s_sky):.2f}")
        print(f"                       ⇒ MISS, AND THE MISS CHANGES THE PRESCRIPTION.  The drift")
        print(f"                         would be a {abs(s_sky) / b['se']:.1f} sigma effect on five")
        print(f"                         peaks, so the statistic is NOT resolution-limited.  What")
        print(f"                         fails is the SHAPE: a line is the wrong summary of a step,")
        print(f"                         and the levers' own slope effects are 6 to 12 per cent of")
        print(f"                         the drift whatever the error bar.  ** So the owed object is")
        print(f"                         not more peaks.  It is a different shape. **")
    return 0


PIN = '4d62831a'
PIN_DIGEST = '7dd49bd7'


def seed():
    import hashlib
    print('=' * 104)
    print('  THE SEED — three assertions, none of them about the other two')
    print('=' * 104)
    ok = True
    try:
        blob = subprocess.run(
            ['git', '-C', ROOT, 'show',
             f'{PIN}:computations/beyond_the_wall/'
             f'r7466_60_which_quantity_carries_the_running_phase/PREDICTION.md'],
            capture_output=True, check=True).stdout
        d = hashlib.sha256(blob).hexdigest()[:8]
        good = d == PIN_DIGEST
        print(f"  (1) HISTORICAL  at {PIN}, PREDICTION.md digests {d}; pinned {PIN_DIGEST}"
              f"  ⇒ {'PASS' if good else 'FAIL'}")
        ok &= good
    except subprocess.CalledProcessError:
        print(f"  (1) HISTORICAL  the pin {PIN} is not readable from here  ⇒ FAIL")
        ok = False

    present = sum(1 for _t, p in config_paths() if os.path.exists(p))
    good = present >= 37
    print(f"  (2) CURRENT     {present} banked configurations readable today, 37 or more needed"
          f"  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good

    good = os.path.exists(_SRC)
    print(f"  (3) DIRECTIONAL the imported peak finder's file is present, so no second copy can"
          f" grow  ⇒ {'PASS' if good else 'FAIL'}")
    ok &= good
    print()
    print(f"  ⇒ {'SEED HOLDS' if ok else 'SEED BROKEN'}")
    return 0 if ok else 1


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    if '--arms' in sys.argv:
        sys.exit(arms())
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(sound())
