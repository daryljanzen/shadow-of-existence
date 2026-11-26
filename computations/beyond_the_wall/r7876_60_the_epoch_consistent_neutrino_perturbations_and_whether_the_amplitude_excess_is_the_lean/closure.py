#!/usr/bin/env python3
"""r7876+60 item ① — THE DESIGN NUMBER: the closure deficit of the perturbation weights.

Registered in `PREDICTION.md` S8.  The four weights the potential's source is built from, plus
`OL/_rt`, do not close on 1, and what is missing is exactly the mass the perturbations do not see:

    Dclose(a) = (Og + On + Oc + Ob + OL/_rt) - 1 = -(Onu_of(a) - FNU*OR/a^4)/_rt

⌗ NOT RETYPED.  The splines are not reimplemented here: this script EXECUTES the instrument's own
  prelude -- `ACOUSTIC_two_arm.py` lines 1..`_CUT`, which ends at the `D_M` line, the last line
  before the heavy part begins -- in a fresh namespace with the control's environment.  So every
  number below comes from the file's own definitions, and the cut line is pinned in the receipt.

⌗ The comparison the registration asks for: `|Dclose|` at recombination beside the instrument's own
  sum response over l = 100-420, read off `r7874`'s banked control arm.  That ratio bounds what
  item ③ can do.
"""
import os
import sys
import json
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
SRC = os.path.join(BW, 'ACOUSTIC_two_arm.py')
_CUT = 645                                   # the `D_M = eta_0 - eta_rec` line

LC = dict(LH0='67.40', LOM='0.3150', WBH2='0.0224', NS='0.965')   # gen_srcdec.sh's control


def prelude(mnu, nufd='1'):
    """execute the instrument's own prelude at this sum and hand back its namespace"""
    with open(SRC) as fh:
        head = ''.join(fh.readlines()[:_CUT])
    keep = dict(os.environ)
    os.environ.update(LC)
    os.environ.update(ARM='lcdm', MNU=str(mnu), NUFD=nufd, BVEL='1', HIER='1')
    ns = {'__name__': '_prelude', '__file__': SRC}
    try:
        sys.path.insert(0, BW)
        exec(compile(head, SRC, 'exec'), ns)
    finally:
        sys.path.pop(0)
        os.environ.clear()
        os.environ.update(keep)
    return ns


def dclose(ns, e):
    """the closure deficit at conformal time `e`, from the file's own splines"""
    tot = (float(ns['Og_of'](e)) + float(ns['On_of'](e))
           + float(ns['Oc_of'](e)) + float(ns['Ob_of'](e)))
    a = float(ns['a_of_eta'](e))
    rt = float(np.interp(e, ns['eg'], ns['_rt']))
    lam = ns['OL'] / rt
    return tot + lam - 1.0, tot, lam, a, rt


def response_size(tag):
    """the instrument's own TT sum response over l = 100-420, off r7874's banked control arm"""
    d = os.path.join(BW, 'r7874_60_the_sum_response_by_source_term_and_the_correction'
                         '_that_decides_one_object', 'srcdec')
    z0 = np.load(os.path.join(d, 'lcdm_S000_tt.npz'))
    zs = np.load(os.path.join(d, 'lcdm_%s_tt.npz' % tag))
    ell = z0['ell'] if 'ell' in z0 else z0[z0.files[0]]
    k0 = 'Dl' if 'Dl' in z0 else [k for k in z0.files if k != 'ell'][0]
    m = (ell >= 100) & (ell <= 420)
    r = zs[k0][m] / z0[k0][m] - 1.0
    return float(np.max(np.abs(r))), float(np.sqrt(np.mean(r ** 2))), int(m.sum())


ARMS = []
print('== r7876+60 (1): THE CLOSURE DEFICIT, from the instrument\'s own prelude ==')
print('   source: %s lines 1..%d' % (os.path.relpath(SRC, BW), _CUT))

rows = {}
for mnu, tag in ((0.30, 'S030'), (0.60, 'S060')):
    ns = prelude(mnu)
    e_rec, e_0 = ns['eta_rec'], ns['eta_0']
    d_rec = dclose(ns, e_rec)
    d_now = dclose(ns, e_0)
    rmax, rrms, nl = response_size(tag)
    rows[tag] = dict(mnu=mnu, d_rec=d_rec[0], d_now=d_now[0], a_rec=d_rec[3], a_now=d_now[3],
                     onu=float(ns['ONU']), onu_fd=float(ns['ONU_FD']),
                     nuf_rec=float(ns['NUF_of'](np.log(d_rec[3]))),
                     w_rec=float(ns['NUW_of'](np.log(d_rec[3]))),
                     w_now=float(ns['NUW_of'](0.0)),
                     r_max=rmax, r_rms=rrms, nl=nl)
    r = rows[tag]
    print('\n-- Sigma = %.2f eV' % mnu)
    print('   a_rec = %.6e   Dclose(rec) = %+.6e      (|.| = %.4f %%)'
          % (r['a_rec'], r['d_rec'], 100 * abs(r['d_rec'])))
    print('   a_now = %.6e   Dclose(now) = %+.6e      (|.| = %.4f %%)'
          % (r['a_now'], r['d_now'], 100 * abs(r['d_now'])))
    print('   FD energy factor at rec NUF_of = %.6f ;  w_nu(rec) = %.6f ;  w_nu(1) = %.6e'
          % (r['nuf_rec'], r['w_rec'], r['w_now']))
    print('   ONU = %.6e   ONU_FD = %.6e' % (r['onu'], r['onu_fd']))
    print('   instrument TT sum response over l = 100-420 on %d multipoles:'
          '  max |r| = %.6e   rms r = %.6e' % (r['nl'], r['r_max'], r['r_rms']))
    print('   RATIO  |Dclose(rec)| / max|r| = %.4f ;  / rms r = %.4f'
          % (abs(r['d_rec']) / r['r_max'], abs(r['d_rec']) / r['r_rms']))

# ⌗ the registration's reachable negative, decided on the measured ratio and not on a reading
print('\n== THE BOUND THE REGISTRATION SET ==')
for tag, r in rows.items():
    q = abs(r['d_rec']) / r['r_rms']
    verd = ('BELOW a tenth of the response -- (3) is NOT expected to bring A to one'
            if q < 0.10 else 'COMPARABLE to the response -- (3) can account for the excess')
    print('   Sigma = %.2f eV :  |Dclose(rec)| / rms r = %.4f  ->  %s' % (r['mnu'], q, verd))

with open(os.path.join(HERE, 'closure.json'), 'w') as fh:
    json.dump(rows, fh, indent=1, sort_keys=True)
print('\n   wrote closure.json')
