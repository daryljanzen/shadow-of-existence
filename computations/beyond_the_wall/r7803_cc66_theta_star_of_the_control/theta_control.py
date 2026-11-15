"""r7803+cc66: theta_* of the LCDM CONTROL on the corpus's own definition, at the distances' point
and at the control's own refit minimum.

The corpus's definition is `r7749_70_leafgeom_refit/theta_corpus.py`'s.  Its background functions are
EXECUTED FROM ITS OWN SOURCE here (the prefix up to its `POINTS` table) rather than transcribed, so
there is no second copy of E_leaf, E_stack, D_M, r_snd or theta to drift.

What makes a point "the control" rather than "the construction's leaf-rate assignment":
  * theta_corpus's r_snd is ALWAYS on E_leaf, and E_leaf is flat LCDM's own E(z) -- matter,
    radiation at the standard photon+neutrino density WR/h^2, and Lambda = 1 - Om.
  * so with E_geom = E_leaf BOTH integrals are LCDM's, and the only thing left that distinguishes
    LCDM's theta_* from the construction's leaf-rate assignment at the same (H0, Om, wb) is the
    UPPER LIMIT of the sound-horizon integral: the construction stops at the arm's start, LCDM
    carries it to z -> infinity.
  * that limit is therefore swept here (3e7, 1e8, 1e12, 1e14) with r_snd's sample count scaled to
    hold the step in ln(1+z) fixed, so the convergence is shown rather than asserted.

Run: python3 theta_control.py        (numpy, scipy; a few seconds; writes control.json)
"""
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), 'r7749_70_leafgeom_refit', 'theta_corpus.py')

# ---- the corpus's own background, executed from its own source (definitions only) ----------------
_txt = open(SRC).read()
_cut = _txt.index('POINTS = {')
CORPUS = {'__file__': SRC, '__name__': 'theta_corpus_defs'}
exec(compile(_txt[:_cut], SRC, 'exec'), CORPUS)                                    # noqa: S102
for _n in ('E_stack', 'E_leaf', 'D_M', 'r_snd', 'theta', 'ZREC', 'THETA_OBS', 'THETA_SIG', 'WG', 'WR'):
    assert _n in CORPUS, f'theta_corpus.py no longer defines {_n}'
E_stack, E_leaf = CORPUS['E_stack'], CORPUS['E_leaf']
D_M, r_snd = CORPUS['D_M'], CORPUS['r_snd']
ZREC, TOBS, TSIG = CORPUS['ZREC'], CORPUS['THETA_OBS'], CORPUS['THETA_SIG']
# the sentence the exec is standing on, checked against the source rather than trusted:
assert re.search(r'return r_snd\(H0, Om, wb, z_hi, ZREC, E_leaf\) / D_M\(ZREC, H0, Om, Egeom\)', _txt), \
    'theta_corpus.py no longer puts r_snd on E_leaf unconditionally'
assert (CORPUS['WG'], CORPUS['WR'], ZREC, TOBS, TSIG) == (2.47e-5, 4.15e-5, 1090.0, 0.0104085, 3.1e-6)


def theta_at(H0, Om, wb, z_hi, Egeom, n=None):
    """theta_corpus's theta(), with r_snd's sample count scaled so the step in ln(1+z) is held
    fixed as z_hi grows (its default 60000 is for z_hi = 3e7)."""
    if n is None:
        span = np.log(1 + z_hi) - np.log(1 + ZREC)
        ref = np.log(1 + 3e7) - np.log(1 + ZREC)
        n = int(round(60000 * max(1.0, span / ref)))
    return r_snd(H0, Om, wb, z_hi, ZREC, E_leaf, n=n) / D_M(ZREC, H0, Om, Egeom)


def pull(t):
    return (t - TOBS) / TSIG


# ---- the points ----------------------------------------------------------------------------------
# The construction's two PRINTED points (P15's +4.84 and +2.33) and its arm-of-record refit, for the
# side-by-side; then the CONTROL's own points.  "The control's own refit minimum" is its like-for-
# like 185-bin minimum -- same range, same STEP, same lensing operator as the arm's, the companion of
# the arm of record's (68.570730, 0.291246, 0.021643, ns 1.015066).
POINTS = [
    ('CONSTRUCTION  distances\' point              (68.60, 0.2973, 0.02237)', 68.60, 0.2973, 0.02237, 'cr'),
    ('CONSTRUCTION  arm-of-record 185-bin refit    (68.570730, 0.291246, 0.021643)', 68.570730, 0.291246, 0.021643, 'cr'),
    ('CONSTRUCTION  leaf-rate refit minimum        (68.585672, 0.294463, 0.022181)', 68.585672, 0.294463, 0.022181, 'cr'),
    ('CONTROL       at the distances\' point        (68.60, 0.2973, 0.02237)', 68.60, 0.2973, 0.02237, 'ctl'),
    ('CONTROL       own 185-bin refit minimum      (67.410309, 0.309826, 0.021966)', 67.410309, 0.309826, 0.021966, 'ctl'),
    ('CONTROL       own 132-bin refit minimum      (67.4054, 0.3095, 0.0220)', 67.4054, 0.3095, 0.0220, 'ctl'),
    ('CONTROL       Planck\'s own point, un-refitted (67.40, 0.3150, 0.02237)', 67.40, 0.3150, 0.02237, 'ctl'),
]
ZHI = (3e7, 1e8, 1e12, 1e14)

out = {}
print(f'  theta_corpus definition | THETA_OBS {TOBS}  sigma {TSIG}  z_rec {ZREC}  '
      f'WR {CORPUS["WR"]}  WG {CORPUS["WG"]}')
print(f'  E_leaf IS flat LCDM E(z); r_snd is ALWAYS on it; only D_M changes rate.\n')
hdr = '  ' + ' ' * 62 + ''.join(f'{"100th@" + f"{z:.0g}":>14}' for z in ZHI) + f'{"pull(z->inf)":>14}'
print(hdr)
for name, H0, Om, wb, kind in POINTS:
    row = {}
    for Eg, gname in ((E_leaf, 'leaf'), (E_stack, 'stack')):
        ts = {f'{z:.0g}': theta_at(H0, Om, wb, z, Eg) for z in ZHI}
        row[gname] = dict(theta=ts, pull={k: pull(v) for k, v in ts.items()})
    lf = row['leaf']['theta']
    print(f'  {name:<60}' + ''.join(f'{100 * lf[f"{z:.0g}"]:>14.6f}' for z in ZHI)
          + f'{row["leaf"]["pull"][f"{ZHI[-1]:.0g}"]:>+14.3f}')
    out[name] = row

# ---- the readings the order asks for -------------------------------------------------------------
K = f'{ZHI[-1]:.0g}'
D_CR = out[POINTS[0][0]]['leaf']['pull']
D_CTL = out[POINTS[3][0]]['leaf']['pull']
print(f'\n  ** (1) THE CONTROL AT THE DISTANCES\' POINT **')
print(f'    construction, leaf-rate assignment, z_hi=3e7 : {D_CR["3e+07"]:+.3f} sigma   (P15 prints +4.84)')
print(f'    the control, same point, z_hi -> infinity    : {D_CTL[K]:+.3f} sigma')
print(f'    difference, i.e. ALL that the construction adds at this point: '
      f'{D_CTL[K] - D_CR["3e+07"]:+.3f} sigma')
STACK = out[POINTS[0][0]]['stack']['pull']
print(f'\n  ** (2) WHAT THE CONSTRUCTION ACTUALLY OWNS AT THAT POINT: THE RATE ASSIGNMENT **')
print(f'    D_M on the stacking rate (arm of record) : {STACK["3e+07"]:+.3f} sigma')
print(f'    D_M on the leaf rate                     : {D_CR["3e+07"]:+.3f} sigma')
print(f'    the swing that is the construction\'s      : {D_CR["3e+07"] - STACK["3e+07"]:+.3f} sigma')
print(f'\n  ** (3) THE CONTROL AT ITS OWN REFIT MINIMUM **')
for i in (4, 5, 6):
    print(f'    {POINTS[i][0][14:]:<48} {out[POINTS[i][0]]["leaf"]["pull"][K]:+.3f} sigma')
print(f'    construction, leaf-rate refit minimum            '
      f'{out[POINTS[2][0]]["leaf"]["pull"]["3e+07"]:+.3f} sigma   (P15 prints +2.33)')

json.dump(out, open(os.path.join(HERE, 'control.json'), 'w'), indent=1)
print(f'\n  wrote {os.path.join(HERE, "control.json")}')
