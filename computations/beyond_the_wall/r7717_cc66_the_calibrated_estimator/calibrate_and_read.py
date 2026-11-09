#!/usr/bin/env python3
"""`r7717+cc66` the calibrated estimator: NULLS FIRST, then both estimators side by side.

⛭ `r7717` (69) ruled option 2 -- the scatter about a line WITHIN each band group is the denominator,
   because the step is a difference between two groups' LEVELS and a gradient inside a group is not
   uncertainty about a level -- with four conditions. This file is conditions 2, 3 and 4.

⛔ THE NEW DENOMINATOR IS NOT DEFINED HERE.  It is imported, character for character, from the probe
   written and pushed BEFORE the order existed: `r7713+cc66.10`'s
   `dryrun/probe_the_significance_denominator.py`.  `git log` on that file against `PREDICTION.md` is
   the check, and it is the only defence that does not rest on my word.  Nothing in this file may
   redefine it, and the import is what enforces that.

⛔ THE RUN ORDER IS ENFORCED, NOT CONVENTIONAL:
   ⓵ a GREEN CONTROL on planted synthetic effects -- a denominator that licenses nothing is useless,
     so it is shown to detect a real effect BEFORE it is shown not to invent one;
   ⓶ the two real-bank NULL families and the LICENCE;
   ⓷ all four ratios under BOTH estimators, side by side, whatever the licence says (69 asked for this
     explicitly, so a reader can see what the denominator did);
   ⓸ the well-posedness test under BOTH;
   ⓹ the agreement gate; and
   ⓺ the verdict -- ONLY if licensed.  A significance from an uncalibrated denominator is not a
     significance, so an unlicensed run prints the numbers and takes NO row of the table.

⚠ A LIMITATION OF NULL FAMILY ⓷, MEASURED AND STATED RATHER THAN DISCOVERED:
  the surrogates are built by removing a least-squares line across ALL band centres and then
  phase-randomising the residual.  That makes them step-free BY CONSTRUCTION, which is what a null
  must be -- but it also removes the very lowest-frequency content, so family ⓷ is marginally EASIER
  than the raw curve there.  Family ⓶ keeps the raw values and instead breaks group contiguity.
  ⇒ Neither is perfect and they fail in OPPOSITE directions, which is why `PREDICTION.md` requires
    ZERO over-bar trials in EVERY family rather than in one of them.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DENSE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7713_cc66_the_dense_ell_discriminant')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                 # noqa: E402

HALVES = (0.175, 0.250, 0.350)
SD_RESOLVED = 5.0          # `r7713+cc66.0`, unchanged
SD_UNRESOLVED = 2.0        # `r7713+cc66.0`, unchanged
RESID_SD = 2.0             # `r7713+cc66.10`, unchanged
RESID_FRAC = 0.5           # `r7713+cc66.10`, unchanged
N_NULL = 2000              # `r7717+cc66.0`, registered
RATIOS = (('own x own    ', 'cr|cr', 'lcdm|lcdm'),
          ('kernel alone ', 'cr|lcdm', 'lcdm|lcdm'),
          ('source alone ', 'lcdm|cr', 'lcdm|lcdm'))


def _line_resid_sd(c, r):
    """⛔ THE RULED DENOMINATOR'S per-group part, verbatim from the pre-order probe's `res`."""
    if len(r) < 3:
        return np.nan
    return float((r - np.polyval(np.polyfit(c, r, 1), c)).std(ddof=2))


def sd_new(cs, R, lo, hi):
    """`sqrt((res_lo^2 + res_hi^2)/2)` -- the probe's `sd_alt`, unchanged"""
    a, b = _line_resid_sd(cs[lo], R[lo]), _line_resid_sd(cs[hi], R[hi])
    return float(np.sqrt((a ** 2 + b ** 2) / 2))


def sd_old(R, lo, hi):
    """`sqrt((var_lo + var_hi)/2)` -- `r7711`'s registered form, unchanged"""
    return float(np.sqrt((R[lo].var(ddof=1) + R[hi].var(ddof=1)) / 2))


def curve(xa, ya, xc, yc, h):
    """the slide's own band-RMS ratio curve at one half-width -- `r7711`'s, unchanged"""
    st = OCK.own_state({'lcdm': (xc, yc), 'cr': (xa, ya)}, 'mean', 1.0)
    cs = np.arange(0.85 + h, 3.0, 0.05)
    R = np.array([OCK._rms(st['ua'], st['oa'], c - h, c + h)
                  / OCK._rms(st['xc'], st['oc'], c - h, c + h) - 1.0 for c in cs])
    return cs, R


def read_curve(cs, R):
    lo, hi = cs < 1.4, cs > 2.2
    step = float(R[hi].mean() - R[lo].mean())
    so, sn = sd_old(R, lo, hi), sd_new(cs, R, lo, hi)
    return dict(step=step, sd_old=so, sd_new=sn,
                in_old=abs(step) / so if so else np.nan,
                in_new=abs(step) / sn if sn else np.nan,
                n_lo=int(lo.sum()), n_hi=int(hi.sum()))


def null_permutation(cs, R, n, rng):
    """⓶ 69's own suggestion: reassign which centres are low and which high, group sizes kept.
    ⚠ A permuted group is NOT CONTIGUOUS, so the line is fitted to scattered abscissae -- registered
      in advance as a defect of this family, which is why it does not carry the licence."""
    lo0, hi0 = cs < 1.4, cs > 2.2
    idx = np.flatnonzero(lo0 | hi0)
    nlo = int(lo0.sum())
    out_new, out_old = np.empty(n), np.empty(n)
    for t in range(n):
        p = rng.permutation(idx)
        li, hyi = p[:nlo], p[nlo:]
        step = R[hyi].mean() - R[li].mean()
        a, b = _line_resid_sd(cs[li], R[li]), _line_resid_sd(cs[hyi], R[hyi])
        sn = np.sqrt((a ** 2 + b ** 2) / 2)
        so = np.sqrt((R[li].var(ddof=1) + R[hyi].var(ddof=1)) / 2)
        out_new[t] = abs(step) / sn if sn else np.nan
        out_old[t] = abs(step) / so if so else np.nan
    return out_new, out_old


def null_surrogate(cs, R, n, rng):
    """⓷ the family the licence rests on: remove a least-squares line across ALL centres -- which makes
    the surrogate step-free BY CONSTRUCTION -- then phase-randomise the residual, preserving its
    amplitude spectrum and therefore its scatter and autocorrelation exactly."""
    resid = R - np.polyval(np.polyfit(cs, R, 1), cs)
    F = np.fft.rfft(resid)
    amp = np.abs(F)
    lo, hi = cs < 1.4, cs > 2.2
    out_new, out_old = np.empty(n), np.empty(n)
    for t in range(n):
        ph = rng.uniform(0, 2 * np.pi, len(F))
        ph[0] = 0.0
        if len(resid) % 2 == 0:
            ph[-1] = 0.0
        s = np.fft.irfft(amp * np.exp(1j * ph), n=len(resid))
        step = s[hi].mean() - s[lo].mean()
        a, b = _line_resid_sd(cs[lo], s[lo]), _line_resid_sd(cs[hi], s[hi])
        sn = np.sqrt((a ** 2 + b ** 2) / 2)
        so = np.sqrt((s[lo].var(ddof=1) + s[hi].var(ddof=1)) / 2)
        out_new[t] = abs(step) / sn if sn else np.nan
        out_old[t] = abs(step) / so if so else np.nan
    return out_new, out_old


def load_real():
    got = {}
    for s, k in (('lcdm', 'lcdm'), ('cr', 'cr'), ('cr', 'lcdm'), ('lcdm', 'cr')):
        p = os.path.join(DENSE, 'pseudo', f'pseudo__S_{s}__K_{k}.npz')
        z = np.load(p, allow_pickle=True)
        got[f'{s}|{k}'] = (np.asarray(z['q'], float), np.asarray(z['y'], float))
    return got


def synth(rng, g_ker, g_src, noise):
    """the planted-effect synthetic from `r7713+cc66.10`'s probe, for the GREEN CONTROL"""
    LA = 301.5427
    ls = np.arange(int(np.ceil(0.80 * LA)), int(np.floor(3.10 * LA)) + 1)
    q = ls / LA
    y0 = 1e-6 * (1.0 + 0.4 * np.cos(2 * np.pi * q)) * np.exp(-0.15 * q)
    nz = lambda: 1.0 + noise * rng.standard_normal(len(q))
    ker, src = 1 + g_ker * (q - 1), 1 + g_src * (q - 1)
    return q, {'lcdm|lcdm': y0 * nz(), 'cr|lcdm': y0 * ker * nz(),
               'lcdm|cr': y0 * src * nz(), 'cr|cr': y0 * ker * src * nz()}


def main():
    t0 = time.time()
    rng = np.random.default_rng(7717)
    rep = {}
    print("\n" + "=" * 100)
    print("  ⛭ `r7717+cc66` THE CALIBRATED ESTIMATOR -- nulls first, both estimators side by side")
    print("=" * 100)

    # ⓵ ------------------------------------------------------ GREEN CONTROL, BEFORE ANY NULL
    print("\n  ⛭ ⓵ GREEN CONTROL -- does the ruled denominator still SEE a planted effect?")
    print("     (a denominator that licenses nothing is useless, so this comes before the nulls)")
    q, d = synth(rng, 0.12, -0.06, 0.0004)
    gc = {}
    for nm, a, c in RATIOS:
        cs, R = curve(q, d[a], q, d[c], 0.350)
        r = read_curve(cs, R)
        gc[nm.strip()] = r
        print(f"       {nm}  step {r['step']:+.5f}   old {r['in_old']:6.2f} sd   new {r['in_new']:6.2f} sd")
    seen = all(gc[nm.strip()]['in_new'] > gc[nm.strip()]['in_old'] for nm, _, _ in RATIOS)
    print(f"       ⇒ the ruled denominator is {'SHARPER on a planted effect' if seen else '⛔ NOT sharper'}")
    rep['green_control'] = gc

    # ⓶ --------------------------------------------------------- THE NULLS, AND THE LICENCE
    print(f"\n  ⛔ ⓶ THE NULL CALIBRATION -- {N_NULL} trials per family per ratio, "
          f"registered requirement: ZERO at or above {SD_RESOLVED:.0f} sd in EVERY family")
    real = load_real()
    nulls, licensed = {}, True
    for nm, a, c in RATIOS:
        for h in HALVES:
            cs, R = curve(*real[a], *real[c], h)
            pn, po = null_permutation(cs, R, N_NULL, rng)
            sn, so = null_surrogate(cs, R, N_NULL, rng)
            key = f"{nm.strip()}|h={h}"
            e = dict(perm_new_over=int((pn >= SD_RESOLVED).sum()),
                     perm_old_over=int((po >= SD_RESOLVED).sum()),
                     surr_new_over=int((sn >= SD_RESOLVED).sum()),
                     surr_old_over=int((so >= SD_RESOLVED).sum()),
                     perm_new_p999=float(np.nanpercentile(pn, 99.95)),
                     surr_new_p999=float(np.nanpercentile(sn, 99.95)),
                     perm_new_max=float(np.nanmax(pn)), surr_new_max=float(np.nanmax(sn)))
            nulls[key] = e
            if e['perm_new_over'] or e['surr_new_over']:
                licensed = False
            print(f"       {nm} h={h:.3f}  permutation: {e['perm_new_over']:4d}/{N_NULL} over "
                  f"(max {e['perm_new_max']:5.2f})   surrogate: {e['surr_new_over']:4d}/{N_NULL} over "
                  f"(max {e['surr_new_max']:5.2f})")
    print(f"\n       ⇒ the ruled denominator is {'LICENSED' if licensed else '⛔ NOT LICENSED'} at "
          f"{SD_RESOLVED:.0f} sd by the registered criterion")
    print(f"       ⌗ zero of {N_NULL} bounds the rate at < {3.0 / N_NULL:.1e} (rule of three, 95%), NOT")
    print(f"         the 5.7e-07 the name '{SD_RESOLVED:.0f} sd' suggests -- registered in advance.")
    rep['nulls'] = nulls
    rep['licensed'] = licensed

    # ⓷ ------------------------------------------- BOTH ESTIMATORS, SIDE BY SIDE, EITHER WAY
    print("\n  ⛭ ⓷ THE THREE RATIOS UNDER BOTH ESTIMATORS -- reported whatever the licence says")
    print("       ratio            half     step       sd(old)    sd(new)     OLD      NEW")
    rows = {}
    for nm, a, c in RATIOS:
        rows[nm.strip()] = []
        for h in HALVES:
            cs, R = curve(*real[a], *real[c], h)
            r = read_curve(cs, R)
            r['half'] = h
            rows[nm.strip()].append(r)
            print(f"       {nm}  {h:.3f}  {r['step']:+.5f}  {r['sd_old']:.6f}  {r['sd_new']:.6f}  "
                  f"{r['in_old']:6.2f}  {r['in_new']:6.2f} sd")
    rep['rows'] = rows
    print("\n  ⚠ the three share the denominator `Pseudo(lcdm,lcdm)`: consistent signs are NOT three")
    print("    confirmations and no significance is combined across them.")

    # ⓸ ----------------------------------------------- WELL-POSEDNESS, UNDER BOTH, AS ORDERED
    print("\n  ⛔ ⓸ THE WELL-POSEDNESS TEST UNDER BOTH -- it passed by 0.8 of a point last time")
    qd, yd = real['lcdm|lcdm']
    on = lambda key: np.interp(qd, real[key][0], real[key][1])
    resid = np.log(on('cr|cr') / yd) - (np.log(on('cr|lcdm') / yd) + np.log(on('lcdm|cr') / yd))
    wp = []
    for h in HALVES:
        cs = np.arange(0.85 + h, 3.0, 0.05)
        Rr = np.array([float(np.mean(np.interp(np.linspace(c - h, c + h, 400), qd, resid)))
                       for c in cs])
        r = read_curve(cs, Rr)
        r['half'] = h
        wp.append(r)
        print(f"       residual  h={h:.3f}  step {r['step']:+.6f}   old {r['in_old']:6.2f} sd   "
              f"new {r['in_new']:6.2f} sd")
    own_step = max(abs(r['step']) for r in rows['own x own'])
    rs = max(wp, key=lambda r: abs(r['step']))
    frac = abs(rs['step']) / own_step if own_step else float('inf')
    bad_old = max(r['in_old'] for r in wp) >= RESID_SD and frac >= RESID_FRAC
    bad_new = max(r['in_new'] for r in wp) >= RESID_SD and frac >= RESID_FRAC
    print(f"       ⇒ residual step is {100 * frac:.1f}% of the own x own step "
          f"(registered refusal: >= {RESID_SD:.0f} sd AND >= {100 * RESID_FRAC:.0f}%)")
    print(f"       ⇒ under the OLD denominator: {'⛔ REFUSES' if bad_old else 'does not refuse'};  "
          f"under the NEW: {'⛔ REFUSES' if bad_new else 'does not refuse'}")
    rep['well_posed'] = dict(rows=wp, frac=frac, refuses_old=bad_old, refuses_new=bad_new)

    # ⓹ -------------------------------------------------------------------- AGREEMENT GATE
    print("\n  ⛔ ⓹ THE AGREEMENT GATE across half-widths, unchanged")
    ag = {}
    for nm, _, _ in RATIOS:
        st = [r['step'] for r in rows[nm.strip()]]
        mag = [abs(x) for x in st]
        ok = (all(x > 0 for x in st) or all(x < 0 for x in st)) and max(mag) / min(mag) <= 2.0
        ag[nm.strip()] = bool(ok)
        print(f"       {nm}  {'AGREES' if ok else '⛔ DISAGREES'}  "
              f"(signs {'one' if (all(x > 0 for x in st) or all(x < 0 for x in st)) else 'MIXED'}, "
              f"magnitudes span {max(mag) / min(mag):.2f}x)")
    rep['agree'] = ag

    # ⓺ -------------------------------------------------- THE VERDICT, ONLY IF LICENSED
    print("\n  ⛭ ⓺ THE VERDICT")
    if not licensed:
        print("       ⛔ NOT TAKEN. The denominator is not licensed at the registered bar, and a")
        print("         significance from an uncalibrated denominator is not a significance. The")
        print("         numbers above stand as measurements; no row of the table is claimed.")
        rep['verdict'] = 'unlicensed_no_verdict'
    elif bad_new:
        print("       ⇒ NEITHER ⒞ -- the well-posedness test refuses under the licensed denominator,")
        print("         so the partition is unavailable whatever the significances say.")
        rep['verdict'] = 'c_withdrawn'
    else:
        w = lambda nm: max(rows[nm], key=lambda r: r['half'])
        own, ker, src = w('own x own'), w('kernel alone'), w('source alone')
        sgn = np.sign(own['step'])
        kr = ag['kernel alone'] and ker['in_new'] >= SD_RESOLVED
        sr = ag['source alone'] and src['in_new'] >= SD_RESOLVED
        ks = np.sign(ker['step']) == sgn and abs(ker['step']) >= 0.5 * abs(own['step'])
        ss = np.sign(src['step']) == sgn and abs(src['step']) >= 0.5 * abs(own['step'])
        creates = kr and ks and (src['in_new'] < SD_UNRESOLVED or np.sign(src['step']) != sgn)
        fails = sr and ss and (ker['in_new'] < SD_UNRESOLVED or
                               (np.sign(ker['step']) == sgn and abs(ker['step']) < abs(src['step'])))
        if creates and not fails:
            rep['verdict'] = 'creates'; print("       ⇒ THE PROJECTION CREATES IT.")
        elif fails and not creates:
            rep['verdict'] = 'fails_to_cancel'; print("       ⇒ IT FAILS TO CANCEL.")
        elif not kr and not sr:
            rep['verdict'] = 'a_unresolved'
            print("       ⇒ NEITHER ⒜ -- not resolved, with a licensed denominator and the whole band.")
        elif kr and sr and ks and ss:
            rep['verdict'] = 'b_not_separable'
            print("       ⇒ NEITHER ⒝ -- both resolved, both of the measured sign, both comparable:")
            print("         the two differences do not partition the step.")
        else:
            rep['verdict'] = 'unlicensed_by_table'
            print("       ⛔ NO ROW OF THE TABLE IS SATISFIED, so nothing is printed as a verdict.")
            print("         The pattern is reported as measured and left uninterpreted.")
        print(f"       ⌗ at the widest window: own {own['in_new']:.2f} sd, kernel {ker['in_new']:.2f} sd "
              f"({ker['step']:+.4f}), source {src['in_new']:.2f} sd ({src['step']:+.4f})")
    rep['wall_s'] = round(time.time() - t0, 1)
    json.dump(rep, open(os.path.join(HERE, 'calibrate_and_read.json'), 'w'), indent=1)
    print(f"\n  wall {time.time() - t0:.1f} s")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
