# -*- coding: utf-8 -*-
"""r7876+60 item ② — THE AMPLITUDE CORRECTION ARM: IS THE EXCESS THE LEAN?

Order `r7875` item ②, registered in this directory's `PREDICTION.md`.  `r7874` measured the
instrument's TT sum response to be `A` times CAMB's over `l = 100-420`, stably, with `A = 1.152`
at `Sigma = 0.30` eV and `1.296` at `0.60`, EE matching.  This file divides that excess out of the
instrument's own TT response and re-reads the lean.

**The correction is affine in the spectrum, so it is the SAME operator at every parameter point:**

    X_corr(s) = X(0) + (X(s) - X(0)) / A(s)       on the TT bins inside l = 100-420

applied to the binned model `base` AND to its four gradients `g` and curvatures `h`, which is what
"the instrument's TT response is scaled by `1/A`" means for a Taylor-expanded score.  Outside those
bins, and in TE and EE, nothing is touched.

⌗ *NOT RETYPED: the removal, the crossing and the profile are `r7866`'s own `same_bins.py`
  functions, imported.  What this file adds is the correction and nothing else, so the uncorrected
  column it prints first must reproduce `r7866`'s move to the digit -- and that reproduction is an
  arm, not a courtesy.*

    NODE=60 python3 amp_arm.py
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7866 = os.path.join(_BTW, 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the'
                            '_repaired_background')
sys.path.insert(0, _R7866)
import same_bins as SB                                                      # noqa: E402
import score_ttteee as SC                                                   # noqa: E402
import model3 as M3                                                         # noqa: E402
import model6 as M6                                                         # noqa: E402
from lean import fit_x4                                                     # noqa: E402

#: the two numbers this arm corrects by, DECLARED reads from `r7874`'s record
A_AT = {0.30: 1.152, 0.60: 1.296}
#: the two numbers it is read against, DECLARED reads from `r7866`'s record as carried by `r7869`.
#: ⚠ **The headline `-20.09` is the FROZEN column** -- the instrument's four parameters held at
#: their zero-sum fit, "as the reference's are" -- and the move is `whole - minus36`, which is how
#: `r7866`'s own table defines it (`57.08 - 77.16`).  The re-profiled column's move is `-48.20`
#: (`68.13 - 116.34`), the `389`-fold.  *This file's first run had the re-profiled column and the
#: opposite sign, and the reproduction arm is what said so; both are fixed here at the cause and
#: both columns are now reported.*
MOVE_UNCORRECTED = -20.09
MOVE_REPROFILED = -48.20
MOVE_REFERENCE = -0.1238
#: the registration's verdict bands, fixed before this ran
BAND_A = 0.36            # |m| <= this, i.e. within 3x the reference's own move -> the excess IS the lean
BAND_B = 0.30            # f <= this -> they are two things
F_A = 1.0 - BAND_A / abs(MOVE_UNCORRECTED)
ELL_LO, ELL_HI = 100, 420


def a_forms():
    """the two no-free-parameter interpolations of `A(Sigma)`, both with `A(0) = 1` exactly"""
    s = np.array(sorted(A_AT))
    y = np.array([A_AT[v] - 1.0 for v in s])
    # form Q: the quadratic through (0,1) and both measured points -- exact at all three
    cq = np.linalg.solve(np.vstack([s, s ** 2]).T, y)
    # form L: linear through (0,1), the single slope that least-squares both points
    kl = float((s @ y) / (s @ s))
    return {
        'Q': (lambda v, _c=cq: 1.0 + _c[0] * v + _c[1] * v ** 2, 'A = 1 + %.6f S %+.6f S^2'
              % (cq[0], cq[1])),
        'L': (lambda v, _k=kl: 1.0 + _k * v, 'A = 1 + %.6f S' % kl),
    }


def the_band(ok):
    """the TT bins wholly inside l = ELL_LO..ELL_HI, on the score's own `ok` mask"""
    lo, hi, blk = SC.BIN_LO[ok], SC.BIN_HI[ok], SC.BLOCK[ok]
    return (blk == 0) & (lo >= ELL_LO) & (hi <= ELL_HI)


def corrected(fn, band, afun):
    """wrap one of `base`/`g[k]`/`h[k]` so the response is divided by `A(s)` inside `band`"""
    def wrapped(s, nu=0, _f=fn, _b=band, _a=afun):
        v = np.asarray(_f(s, nu), float).copy()
        if s == 0.0:
            return v
        z = np.asarray(_f(0.0, nu), float)
        v[_b] = z[_b] + (v[_b] - z[_b]) / _a(s)
        return v
    return wrapped


def inst_profile(keep, afun=None):
    """`r7866`'s instrument profile, optionally with the TT response corrected by `1/A`"""
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    newok = ok.copy()
    newok[ok] = keep
    c = mod.cmb
    base, g, h = c.base, dict(c.g), dict(c.h)
    if afun is not None:
        band = the_band(ok)
        base = corrected(base, band, afun)
        g = {k: corrected(g[k], band, afun) for k in M3.KEYS4}
        h = {k: corrected(h[k], band, afun) for k in M3.KEYS4}
    c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
    c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.ok, c.nb = newok, int(newok.sum())
    c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
    out = []
    for s in SB.SUMS:
        _, v = fit_x4(mod, s)
        out.append(float(v))
    return out


def inst_profile_frozen(keep, afun=None):
    """`r7866`'s FROZEN instrument column: the four parameters held at their zero-sum fit, which is
    the reference's own treatment.  This is the column the `-20.09` headline is read on."""
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    band = the_band(ok) if afun is not None else None
    #: the frozen point is fitted on the WHOLE mask at `Sigma = 0`, where the correction is the
    #: identity, so it is the same point corrected or not -- taken on the corrected model anyway,
    #: so that nothing depends on that being true.
    m0 = M6.Model6('lcdm')
    if afun is not None:
        c0 = m0.cmb
        c0.base = corrected(c0.base, band, afun)
        c0.g = {k: corrected(c0.g[k], band, afun) for k in M3.KEYS4}
        c0.h = {k: corrected(c0.h[k], band, afun) for k in M3.KEYS4}
    x4f, _ = fit_x4(m0, 0.0)
    newok = ok.copy()
    newok[ok] = keep
    c = mod.cmb
    base, g, h = c.base, dict(c.g), dict(c.h)
    if afun is not None:
        base = corrected(base, band, afun)
        g = {k: corrected(g[k], band, afun) for k in M3.KEYS4}
        h = {k: corrected(h[k], band, afun) for k in M3.KEYS4}
    c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
    c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.ok, c.nb = newok, int(newok.sum())
    c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
    return [float(c.chi2_cmb(x4f, s)) for s in SB.SUMS], [float(v) for v in x4f]


def move_of(afun, frozen):
    """the lean, `r7866`'s own sign: crossing(whole) - crossing(minus 36), in meV"""
    mod0 = M6.Model6('lcdm')
    ok = mod0.cmb.ok
    keep_all = np.ones(int(ok.sum()), bool)
    keep_36 = SB.the_thirty_six(ok)
    if frozen:
        pw = inst_profile_frozen(keep_all, afun)[0]
        pm = inst_profile_frozen(keep_36, afun)[0]
    else:
        pw, pm = inst_profile(keep_all, afun), inst_profile(keep_36, afun)
    cw, cm = SB.cross_of(SB.SUMS, pw), SB.cross_of(SB.SUMS, pm)
    if cw is None or cm is None:
        return None, cw, cm
    return float(cw - cm), cw, cm


def main():
    print(__doc__)
    print('=' * 100)
    mod0 = M6.Model6('lcdm')
    ok = mod0.cmb.ok
    band = the_band(ok)
    lo, hi = SC.BIN_LO[ok][band], SC.BIN_HI[ok][band]
    print('\n  the corrected band: %d TT bin(s) of %d scored, multipoles %d..%d'
          % (int(band.sum()), int(ok.sum()), int(lo.min()), int(hi.max())))
    n36 = int((~SB.the_thirty_six(ok) & band).sum())
    print('  of the thirty-six removed, %d are TT bins inside it' % n36)

    res = {'band_bins': int(band.sum()), 'band_lo': int(lo.min()), 'band_hi': int(hi.max()),
           'removed_in_band': n36, 'A_at': A_AT,
           'bands': {'A_abs_m': BAND_A, 'B_f': BAND_B, 'A_f': F_A}}

    # ⚠ THE REPRODUCTION ARM, on BOTH columns: uncorrected, each must give `r7866`'s own move.
    REF = {'frozen': MOVE_UNCORRECTED, 'reprofiled': MOVE_REPROFILED}
    res['uncorrected'] = {}
    for col, frozen in (('frozen', True), ('reprofiled', False)):
        m0, cw0, cm0 = move_of(None, frozen)
        d = abs(m0 - REF[col])
        good = d <= 0.05
        print('\n-- UNCORRECTED, %s column (the reproduction arm)' % col)
        print('   crossing whole = %.2f meV   minus36 = %.2f meV   move = %+.2f meV'
              % (cw0, cm0, m0))
        print('   r7866 recorded %+.2f meV  ->  %s (|d| = %.4f meV)'
              % (REF[col], 'REPRODUCED' if good else '** NOT REPRODUCED **', d))
        res['uncorrected'][col] = dict(move=m0, whole=cw0, minus36=cm0, reproduced=bool(good),
                                       recorded=REF[col], dev=d)
    if not all(v['reproduced'] for v in res['uncorrected'].values()):
        print('\n   ⛔ a column does not reproduce r7866 -- the corrected columns below are not'
              ' readable until it does.')

    res['forms'] = {}
    for name, (afun, desc) in sorted(a_forms().items()):
        print('\n-- form %s : %s' % (name, desc))
        print('   A(0.05) = %.6f   A(0.15) = %.6f   A(0.30) = %.6f'
              % (afun(0.05), afun(0.15), afun(0.30)))
        res['forms'][name] = dict(desc=desc)
        for col, frozen in (('frozen', True), ('reprofiled', False)):
            m, cw, cm = move_of(afun, frozen)
            f = 1.0 - abs(m) / abs(REF[col])
            print('   %-11s whole = %.2f   minus36 = %.2f   move = %+.2f meV   f = %+.4f'
                  % (col, cw, cm, m, f))
            res['forms'][name][col] = dict(move=m, whole=cw, minus36=cm, f=f)

    # ⌗ the verdict is read on the FROZEN column, because that is the column the registration's
    #   `-20.09` and its bands belong to.  The re-profiled column is reported beside it.
    fs = [res['forms'][k]['frozen']['f'] for k in res['forms']]
    ms = [abs(res['forms'][k]['frozen']['move']) for k in res['forms']]
    spread = max(fs) - min(fs)
    print('\n== THE VERDICT, on the bands fixed in the registration, frozen column ==')
    print('   f across the two forms: %.4f .. %.4f   (spread %.4f)' % (min(fs), max(fs), spread))
    verds = set()
    for k in sorted(res['forms']):
        m, f = res['forms'][k]['frozen']['move'], res['forms'][k]['frozen']['f']
        v = ('A' if abs(m) <= BAND_A else ('B' if f <= BAND_B else 'C'))
        verds.add(v)
        print('   form %s : |m| = %.4f meV, f = %.4f  ->  %s'
              % (k, abs(m), f, {'A': 'A -- the amplitude excess IS the lean',
                                'B': 'B -- they are two things',
                                'C': 'C -- PARTIAL, reported as the fraction'}[v]))
    print('   re-profiled column, for the record: f = %s'
          % ', '.join('%.4f' % res['forms'][k]['reprofiled']['f'] for k in sorted(res['forms'])))
    if len(verds) > 1:
        print('   ** THE TWO FORMS DISAGREE ACROSS A VERDICT BOUNDARY -- the arm is reported as'
              ' NOT DECIDED by this interpolation, as registered. **')
    res['verdicts'] = sorted(verds)
    res['agree'] = len(verds) == 1
    res['f_spread'] = spread
    res['m_span'] = [min(ms), max(ms)]

    with open(os.path.join(_HERE, 'amp_arm.json'), 'w') as fh:
        json.dump(res, fh, indent=1, sort_keys=True, default=float)
    print('\n   wrote amp_arm.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
