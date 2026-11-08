#!/usr/bin/env python3
"""`r7707+cc66`: where the step's sharp transition first appears in the chain.

Three readings of the SAME sliding window, by the same locator the step receipt is validated with:
  ⓵ the step as the paper has it -- the arm/control ratio of band RMS on the projected spectra;
  ⓶ EACH ARM'S OWN projected spectrum -- `Ra` and `Rc` slid separately, which the ratio divides away;
  ⓷ the SOURCE-SIDE ratio -- the same construction on the eta-integrated sources.

⛔ Every "no transition here" is established by the TRANSLATION control and never by the locator
returning a number: `r7703`'s withdrawal was a locator reporting its own scan window for a curve with
no feature in it.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC                                                        # noqa: E402
import own_comb_kinds as OCK                                                 # noqa: E402

HALVES = (0.175, 0.25, 0.35)


def fine_banks():
    out = {}
    for t, n in (('lcdm', 'r6941_fine_lcdm'), ('cr', 'r6941_fine_cr_leafrec1')):
        d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
        out[t] = (d['ls'].astype(float) / float(d['l_A']), np.asarray(d['Dl'], float))
    return out


def source_banks(square=True):
    """the eta-integrated source on x = k r_s / pi -- the SAME acoustic phase variable as q = l / l_A,
    because l_A = pi D_M / r_s, and only under l = k D_M."""
    out, meta = {}, {}
    for t, n in (('lcdm', 'r6911_source_lcdm_leafrec1'), ('cr', 'r6911_source_cr_leafrec1')):
        d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
        x = np.asarray(d['k'], float) * float(d['r_s']) / np.pi
        S = np.asarray(d['S_i'], float)
        out[t] = (x, S ** 2 if square else S)
        meta[t] = dict(l_A=float(d['l_A']), r_s=float(d['r_s']), D_M=float(d['D_M']),
                       lA_from_geometry=float(np.pi * float(d['D_M']) / float(d['r_s'])))
    return out, meta


def locate(fn, lo_hi=(1.4, 2.2), grid=(0.85, 3.0, 0.05), shift=0.0):
    """the step receipt's own locator: FIRST crossing of the re-measured midpoint, per half-width.

    `shift` translates the interval the curve is read on.  A LOCATED feature moves by -shift; a broad
    monotone ramp does not move at all, because it crosses its own re-measured midpoint wherever it is
    translated.  That is the control, and it is the only thing that tells the two apart.
    """
    out = []
    for half in HALVES:
        row = [(c, fn(c - half + shift, c + half + shift))
               for c in np.arange(grid[0] + half, grid[1], grid[2])]
        lo = float(np.mean([v for c, v in row if c < lo_hi[0]]))
        hi = float(np.mean([v for c, v in row if c > lo_hi[1]]))

        def xat(frac, near=None):
            tgt = lo + frac * (hi - lo)
            xs = [(row[i - 1][0] + (tgt - row[i - 1][1]) / (row[i][1] - row[i - 1][1]) * grid[2])
                  for i in range(1, len(row)) if row[i - 1][1] < tgt <= row[i][1]]
            if not xs:
                return float('nan')
            return min(xs, key=lambda v: abs(v - near)) if near is not None else xs[0]

        h = xat(0.5)
        out.append(dict(half=half, half_rise=h, w25_75=xat(0.75, h) - xat(0.25, h),
                        lo=lo, hi=hi, factor=(hi / lo if lo else float('nan'))))
    return out


def translation_control(fn, name, shifts=(0.0, 0.15, 0.30)):
    """⛔ the only test that distinguishes a located feature from a locator returning its scan window"""
    rows = []
    for s in shifts:
        h = float(np.mean([r['half_rise'] for r in locate(fn, shift=s)]))
        rows.append((s, h))
    moved = [abs((h - rows[0][1]) + s) for s, h in rows[1:]]      # a feature moves by -s
    tracks = all(m < 0.3 * s for (s, _), m in zip(rows[1:], moved))
    return dict(name=name, rows=rows, tracks_translation=bool(tracks),
                residual=[float(m) for m in moved])


def main():
    res = {}
    FB = fine_banks()
    SB, SM = source_banks(True)
    res['geometry'] = SM
    print("  ⛭ `r7707` THE TWO ABSCISSAE ARE ONE VARIABLE ONLY UNDER l = k D_M")
    for t in SM:
        print(f"      {t:5s} l_A banked {SM[t]['l_A']:.4f}   pi D_M / r_s {SM[t]['lA_from_geometry']:.4f}"
              f"   ratio {SM[t]['lA_from_geometry'] / SM[t]['l_A']:.6f}")

    # ---- the registered precondition, MEASURED -------------------------------------------------
    print("\n  ⛔ `r7707` THE REGISTERED PRECONDITION: (y - e)/e NEEDS AN ENVELOPE THAT DOES NOT CROSS ZERO")
    pre = {}
    for t, n in (('lcdm', 'r6911_source_lcdm_leafrec1'), ('cr', 'r6911_source_cr_leafrec1')):
        d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
        x = np.asarray(d['k'], float) * float(d['r_s']) / np.pi
        S = np.asarray(d['S_i'], float)
        for lab, y in (('S_i', S), ('S_i**2', S ** 2)):
            e = OCK.envelope(x, y, 1.0, 'mean')
            nz = int(np.sum(np.diff(np.sign(e)) != 0))
            m = (x >= 0.85) & (x <= 5.75)
            T = float(OC.comb(x[m], y[m])[1])
            pre[f'{t}/{lab}'] = dict(env_zero_crossings=nz, min_abs_env=float(np.min(np.abs(e))), T=T)
            print(f"      {t:5s} {lab:7s} envelope zero crossings {nz:3d}   min|e| {np.min(np.abs(e)):.3g}"
                  f"   fitted comb T {T:.5f}")
    res['precondition'] = pre
    for t, n in (('lcdm', 'r6941_fine_lcdm'), ('cr', 'r6941_fine_cr_leafrec1')):
        d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
        q = np.asarray(d['ls'], float) / float(d['l_A'])
        Dl = np.asarray(d['Dl'], float)
        m = (q >= 0.85) & (q <= 5.75)
        res.setdefault('spectrum_T', {})[t] = float(OC.comb(q[m], Dl[m])[1])
        print(f"      {t:5s} D_l     (positive by construction)              "
              f"   fitted comb T {res['spectrum_T'][t]:.5f}")

    # ---- the three readings --------------------------------------------------------------------
    STS = OCK.own_state(FB, 'mean', 1.0)
    STK = OCK.own_state(SB, 'mean', 1.0)

    def ratio_spec(a, b):
        return float(OCK._rms(STS['ua'], STS['oa'], a, b) / OCK._rms(STS['xc'], STS['oc'], a, b) - 1.0)

    def arm_spec(a, b):
        return OCK._rms(STS['ua'], STS['oa'], a, b)

    def ctl_spec(a, b):
        return OCK._rms(STS['xc'], STS['oc'], a, b)

    def ratio_src(a, b):
        return float(OCK._rms(STK['ua'], STK['oa'], a, b) / OCK._rms(STK['xc'], STK['oc'], a, b) - 1.0)

    def arm_src(a, b):
        return OCK._rms(STK['ua'], STK['oa'], a, b)

    def ctl_src(a, b):
        return OCK._rms(STK['xc'], STK['oc'], a, b)

    READ = (('① the step, arm/control on the SPECTRA', ratio_spec),
            ('② the ARM\'s own spectrum (Ra)', arm_spec),
            ('② the CONTROL\'s own spectrum (Rc)', ctl_spec),
            ('③ the SOURCE-SIDE ratio', ratio_src),
            ('③ the ARM\'s own source (Ra)', arm_src),
            ('③ the CONTROL\'s own source (Rc)', ctl_src))
    print("\n  ⛭ `r7707` THE SAME LOCATOR ON EACH READING")
    print("      reading                                 half-rise (mean of 3)   25-75 width   hi/lo")
    res['readings'] = {}
    for name, fn in READ:
        L = locate(fn)
        h = float(np.mean([r['half_rise'] for r in L]))
        w = float(np.mean([r['w25_75'] for r in L]))
        f = float(np.mean([r['factor'] for r in L]))
        res['readings'][name] = dict(half_rise=h, w25_75=w, factor=f, per_half=L)
        print(f"      {name:40s}  {h:8.4f}            {w:8.4f}     {f:7.3f}")

    print("\n  ⛔ `r7707` THE TRANSLATION CONTROL -- a LOCATED feature moves by -d, a ramp does not move")
    res['translation'] = {}
    for name, fn in READ:
        tc = translation_control(fn, name)
        res['translation'][name] = tc
        cells = "   ".join(f"+{s:.2f}: {h:.4f}" for s, h in tc['rows'])
        print(f"      {name:40s}  {cells}   -> {'TRACKS (located)' if tc['tracks_translation'] else 'DOES NOT TRACK (no feature)'}")

    json.dump(res, open(os.path.join(HERE, 'where_the_sharpness_is.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
