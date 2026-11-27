# -*- coding: utf-8 -*-
"""r7882+60 arm Ⓠ⓸ᵇ — THE MASSLESS LIMIT READ ON WHAT THE FIT ACTUALLY READS.

`PREDICTION.md`'s declared amendment: *"the fit of record, executed on the hierarchy-on and
hierarchy-off spectra, must return an `A` in TT and in EE differing by less than `0.003`"* — the
same tenth of `r7879`'s `0.03` band that `Ⓠ⓶` and `Ⓠ⓷` are held to, asserted on the quantity the
fit actually reads, which is the clause `Ⓠ⓸`'s argument reasons FROM: that at `Σ → 0` nothing the
fit reads moves.

⛔ *WHY THE SLOTS CARRY THE LIMIT SUMS.  `shift.py`'s slots ARE the validation sums and it fits
  against CAMB at those sums, so there is no CAMB target at `1e-3` or `1e-4`.  This arm is a
  DIFFERENCE AT A FIXED TARGET — on against off on legs that share it — so the target CANCELS and
  need not be the right one for the sum in the slot.  `S030` holds `Σ = 1e-3` and `S060` holds
  `1e-4`, which reads the criterion at BOTH limit sums rather than one.*

⛔ **NO `A` FROM THESE LEGS IS A VALIDATION NUMBER** and none is reported as one.  The legs are not
  fitted against their own sum's target, so their `A` is meaningless on its own and only the
  on-against-off difference is read.  The validation numbers come from `valid/`, and only after
  this gate is met.

⌗ NOT RETYPED: the fit is `r7874`'s own `shift.py`, executed with exactly the two lines rebound,
  the rebinding function imported from `r7876`'s `refit.py`.  *The twelve-line harness around it is
  this revision's because the output path is; the FIT is not re-implemented.*

⌗ THE REPRODUCTION LEG RUNS FIRST on the landed bank and must return `r7874`'s four headline
  amplitudes, or nothing downstream of it is read.

    NODE=60 python3 limitfit.py
"""
import io
import json
import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7874 = os.path.join(_BTW, 'r7874_60_the_sum_response_by_source_term_and_the_correction_that'
                            '_decides_one_object')
_R7876 = os.path.join(_BTW, 'r7876_60_the_epoch_consistent_neutrino_perturbations_and_whether_the'
                            '_amplitude_excess_is_the_lean')
SHIFT = os.path.join(_R7874, 'shift.py')
BANK = os.path.join(_BTW, 'bank')
LANDED_DIR = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
LEGS = os.path.join(_HERE, 'limitfit')
WORK = os.path.join(_HERE, '_legs')
sys.path.insert(0, _R7876)
from refit import the_two_rebindings                                            # noqa: E402

SUMS = ('0.30', '0.60')          # shift.py's SLOT names; the sums IN them are 1e-3 and 1e-4
SLOT = {'0.30': 'Σ = 1e-3', '0.60': 'Σ = 1e-4'}
BLOCKS = ('TT', 'EE')
#: `r7874`'s four headline amplitudes on the landed bank -- the reproduction gate
A_WAS = {'TT|0.30': 1.15162, 'TT|0.60': 1.29592, 'EE|0.30': 1.01405, 'EE|0.60': 1.04630}
LANDED = 'pol_grid_bvel1_nufd_only'
MOVE = 0.003                     # PREDICTION.md: the registered tenth of r7879's 0.03 band


def legs(tag):
    """a leg directory in `shift.py`'s own naming, which is NOT the bank's naming.

    ⚑ `shift.py` opens ONE file per slot, `lcdm_<tag>.npz`, and reads `ls`, `Dl`, `Dl_EE` and
    `l_A` out of it — all of which the POL leg carries.  So the slot file is the pol leg under the
    bare name.  ⚑ NOT INVENTED HERE: this is `r7876`'s own `legs()` shape, which did the same for
    the same fit; only the source directory and the suffix differ.
    ⛔ *The zero leg is the LANDED bank's, at every reading, for the reason `gen_limitfit.sh`
    gives: the switch refuses a zero sum, so the zero leg is the same spectrum either way.*
    """
    d = os.path.join(WORK, tag)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    os.symlink(os.path.join(LANDED_DIR, 'lcdm_S000.npz'), os.path.join(d, 'lcdm_S000.npz'))
    for slot in ('S030', 'S060'):
        src = os.path.join(LEGS, tag, 'lcdm_%s_pol.npz' % slot)
        if not os.path.isfile(src):
            raise SystemExit('  ⛔ missing leg %s -- run gen_limitfit.sh first' % src)
        os.symlink(src, os.path.join(d, 'lcdm_%s.npz' % slot))
    return d


def run_fit(label, bank_dir):
    """execute `r7874`'s fit against this bank and hand back its own record"""
    out = os.path.join(_HERE, 'fit_%s.json' % label)
    keep = dict(os.environ)
    os.environ['R7876_ON'], os.environ['R7876_OUT'] = bank_dir, out
    ns = {'__name__': '_shift_of_r7874', '__file__': SHIFT}
    try:
        sys.path.insert(0, _R7874)
        print('\n' + '#' * 100)
        print('#  %s   (%s)' % (label, bank_dir))
        print('#' * 100)
        exec(compile(the_two_rebindings(io.open(SHIFT, encoding='utf-8').read()), SHIFT, 'exec'),
             ns)
    finally:
        sys.path.pop(0)
        os.environ.clear()
        os.environ.update(keep)
    return json.load(io.open(out, encoding='utf-8'))


def amps(rec):
    return dict(('%s|%s' % (b, s), rec['fits']['%s|%s' % (b, s)]['best_A'])
                for b in BLOCKS for s in SUMS)


def main():
    print(__doc__)
    rec = {'MOVE': MOVE, 'slots': SLOT}

    # ══ THE REPRODUCTION LEG ════════════════════════════════════════════════════════════════════
    base = amps(run_fit('reproduction', os.path.join(BANK, LANDED)))
    bad = ['%s: %.6f against %.5f' % (k, base[k], A_WAS[k])
           for k in A_WAS if abs(base[k] - A_WAS[k]) > 5e-05]
    rec['reproduction'] = {'A': base, 'expected': A_WAS, 'reproduced': not bad}
    print('\n-- REPRODUCTION LEG: %s' % ('REPRODUCED' if not bad else '** NOT ** ' + '; '.join(bad)))
    if bad:
        json.dump(rec, io.open(os.path.join(_HERE, 'limitfit.json'), 'w', encoding='utf-8'),
                  indent=1, sort_keys=True)
        raise SystemExit('  ⛔ the fit of record does not reproduce its own landed amplitudes, so '
                         'nothing downstream of it is read')

    # ══ THE ARM ═════════════════════════════════════════════════════════════════════════════════
    got = {}
    os.makedirs(WORK, exist_ok=True)
    for tag in ('off', 'on'):
        got[tag] = amps(run_fit('limit_%s' % tag, legs(tag)))
    rec['A'] = got

    print('\n' + '=' * 100)
    print('  ARM Ⓠ⓸ᵇ: the fit of record on the hierarchy ON against OFF, at the two limit sums')
    print('=' * 100)
    print('%6s %14s %14s %14s %14s   %s'
          % ('block', 'slot', 'A off', 'A on', '|difference|', 'against %.3f' % MOVE))
    rows = {}
    for b in BLOCKS:
        for s in SUMS:
            k = '%s|%s' % (b, s)
            dif = abs(got['on'][k] - got['off'][k])
            rows[k] = dif
            print('%6s %14s %14.6f %14.6f %14.3e   %s'
                  % (b, SLOT[s], got['off'][k], got['on'][k], dif,
                     'inside' if dif < MOVE else '** OUTSIDE **'))
    rec['difference'] = rows
    rec['worst'] = max(rows.values())
    rec['met'] = bool(rec['worst'] < MOVE)
    print('\n  worst over both blocks and both limit sums: %.3e against the registered %.3f'
          % (rec['worst'], MOVE))
    if rec['met']:
        print('  ⇒ ** ARM Ⓠ⓸ᵇ MET, so GATE Ⓠ⓸ IS MET on its registered criterion: at the')
        print('       massless limit nothing the fit reads moves, and the hierarchy IS the landed')
        print('       massless one continued.  The validation numbers may now be read. **')
    else:
        print('  ⇒ ** ARM Ⓠ⓸ᵇ NOT MET, so GATE Ⓠ⓸ FAILS on its own registered criterion, and no')
        print('       validation number is read. **')
    json.dump(rec, io.open(os.path.join(_HERE, 'limitfit.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote limitfit.json')
    return 0 if rec['met'] else 1


if __name__ == '__main__':
    sys.exit(main())
