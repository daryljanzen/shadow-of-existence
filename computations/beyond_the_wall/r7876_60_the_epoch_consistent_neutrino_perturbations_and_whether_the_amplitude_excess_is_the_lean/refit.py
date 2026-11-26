# -*- coding: utf-8 -*-
"""r7876+60 item ③'s VALIDATION — `A` and `eps` refitted against CAMB on the repaired perturbations.

Order `r7875` item ③: *"Validate before any limit: refit `A` and `eps` against CAMB at `0.30` and
`0.60` eV.  `A` must fall from `1.15` and `1.30` toward 1, and EE must not move away from its
present agreement."*  The verdict bands Ⓓ–Ⓖ were fixed in this directory's `PREDICTION.md` before
the repair was written.

⌗ **NOT RETYPED, AND NOT APPROXIMATED EITHER: THE FIT IS `r7874`'s OWN `shift.py`, EXECUTED.**
  Two lines of it are rebound -- the bank it reads and the file it writes -- and nothing else is
  touched, so the CAMB legs, the `eps` allowance measured from `l_A` against `theta*`, the `eps`
  grid, the `A`-across-the-band measurement and the verdict logic are all the ones `r7874` was
  judged on.  *A fit re-implemented here would be a second instrument, and the comparison
  `A: 1.152 -> ?` would then be between two of them.*

⌗ **THE REPRODUCTION ARM.** The same code is run first on `r7874`'s own bank, and it must return
  `A = 1.152` and `1.296`.  Only then are the repaired legs readable.

⌗ **THE ZERO LEG IS THE LANDED ONE** at every reading, for the reason `gen_nupert.sh` gives: `NUFD`
  is gated on a non-zero sum, so `NUPERT` is provably inert there.

    NODE=60 python3 refit.py
"""
import io
import json
import os
import shutil
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7874 = os.path.join(_BTW, 'r7874_60_the_sum_response_by_source_term_and_the_correction'
                            '_that_decides_one_object')
SHIFT = os.path.join(_R7874, 'shift.py')
LANDED = os.path.join(_BTW, 'bank', 'pol_grid_bvel1_nufd_only')
NUP = os.path.join(_HERE, 'nupert')
WORK = os.path.join(_HERE, '_legs')

#: `r7874`'s headline, the thing this validation is read against
A_WAS = {'TT|0.30': 1.152, 'TT|0.60': 1.296}
#: the registration's bands, fixed before the repair existed
TOL_D = 0.03                 # Ⓓ: |A - 1| within this at both sums
FRAC_E = 1.0 / 3.0           # Ⓔ: at least this much of the excess removed at both sums
FRAC_F = 0.10                # Ⓕ: less than this at either sum -> the defect is elsewhere
#: EE's present agreement, `r7874`'s measured band, which must not worsen
EE_BAND = 0.05


def the_two_rebindings(src):
    """`shift.py` verbatim but for the bank it reads and the file it writes"""
    a = "ON = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')"
    b = "OUT = os.path.join(_HERE, 'shift.json')"
    assert src.count(a) == 1 and src.count(b) == 1, 'shift.py has moved; stop rather than guess'
    return src.replace(a, "ON = os.environ['R7876_ON']").replace(
        b, "OUT = os.environ['R7876_OUT']")


def legs(name, suffix):
    """a leg directory in `shift.py`'s own naming: the landed zero, this arm's two sums"""
    d = os.path.join(WORK, name)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    os.symlink(os.path.join(LANDED, 'lcdm_S000.npz'), os.path.join(d, 'lcdm_S000.npz'))
    for tag in ('S030', 'S060'):
        srcf = os.path.join(NUP, 'lcdm_%s%s_pol.npz' % (tag, suffix))
        if not os.path.isfile(srcf):
            raise SystemExit('  ⛔ missing leg %s -- run gen_nupert.sh first' % srcf)
        os.symlink(srcf, os.path.join(d, 'lcdm_%s.npz' % tag))
    return d


def run_fit(label, on_dir):
    """execute `r7874`'s fit against `on_dir` and hand back its own record"""
    out = os.path.join(_HERE, 'refit_%s.json' % label)
    keep = dict(os.environ)
    os.environ['R7876_ON'], os.environ['R7876_OUT'] = on_dir, out
    ns = {'__name__': '_shift_of_r7874', '__file__': SHIFT}
    try:
        sys.path.insert(0, _R7874)
        print('\n' + '#' * 100)
        print('#  %s' % label)
        print('#' * 100)
        exec(compile(the_two_rebindings(io.open(SHIFT, encoding='utf-8').read()), SHIFT, 'exec'),
             ns)
    finally:
        sys.path.pop(0)
        os.environ.clear()
        os.environ.update(keep)
    return json.load(io.open(out, encoding='utf-8'))


def main():
    print(__doc__)
    os.makedirs(WORK, exist_ok=True)
    rec = {}

    # ⚠ THE REPRODUCTION ARM FIRST.
    rep = run_fit('landed', LANDED)
    rec['landed'] = rep
    bad = []
    for k, want in A_WAS.items():
        got = rep['fits'][k]['best_A']
        if abs(got - want) > 5e-4:
            bad.append('%s: %.6f against %.3f' % (k, got, want))
    print('\n-- REPRODUCTION ARM: %s' % ('REPRODUCED' if not bad
                                         else '** NOT REPRODUCED ** ' + '; '.join(bad)))
    rec['reproduced'] = not bad
    if bad:
        print('   ⛔ the repaired legs are not readable until the fit reproduces r7874.')

    for label, suffix in (('shear_on', 'on'), ('shear_off', 'off')):
        rec[label] = run_fit(label, legs(label, suffix))

    print('\n' + '=' * 100)
    print('  THE VALIDATION, on the bands fixed in PREDICTION.md before the repair was written')
    print('=' * 100)
    print('%-10s %-6s %10s %10s %10s %12s %12s' % ('arm', 'block', 'A was', 'A now', '|A-1|',
                                                   'frac removed', 'best eps'))
    summ = {}
    for label in ('shear_on', 'shear_off'):
        for k in sorted(rec[label]['fits']):
            f = rec[label]['fits'][k]
            was = A_WAS.get(k)
            now = f['best_A']
            frac = ((abs(was - 1.0) - abs(now - 1.0)) / abs(was - 1.0)) if was else None
            summ['%s|%s' % (label, k)] = dict(A_now=now, A_was=was, frac=frac,
                                              eps=f['best_eps'], resid=f['resid_best'])
            print('%-10s %-6s %10s %10.5f %10.5f %12s %12.2e'
                  % (label, k, ('%.3f' % was) if was else '--', now, abs(now - 1.0),
                     ('%+.4f' % frac) if frac is not None else '--', f['best_eps']))
    rec['summary'] = summ

    # ── the verdict, read on the shear-ON arm with the spread to shear-OFF as the uncertainty ──
    tt = {s: summ['shear_on|TT|%s' % s] for s in ('0.30', '0.60')}
    tto = {s: summ['shear_off|TT|%s' % s] for s in ('0.30', '0.60')}
    ee = {s: summ['shear_on|EE|%s' % s] for s in ('0.30', '0.60')}
    spread = {s: abs(tt[s]['A_now'] - tto[s]['A_now']) for s in tt}
    print('\n  the approximation\'s own uncertainty on A, from the two shear arms: %s'
          % ', '.join('%.5f at Sigma %s' % (spread[s], s) for s in sorted(spread)))
    ee_worse = {s: (abs(ee[s]['A_now'] - 1.0) > EE_BAND) for s in ee}
    print('  EE: |A-1| = %s  (present band %.2f)  -> %s'
          % (', '.join('%.5f at %s' % (abs(ee[s]['A_now'] - 1.0), s) for s in sorted(ee)),
             EE_BAND, 'WORSENED' if any(ee_worse.values()) else 'not worsened'))

    away = any(tt[s]['frac'] < 0.0 for s in tt)
    if away or any(ee_worse.values()):
        v = ('G', 'the repair is REFUTED on its own validation -- A moves away from 1 or EE '
                  'worsens past its band; no limit is read through it')
    elif all(abs(tt[s]['A_now'] - 1.0) <= TOL_D for s in tt):
        v = ('D', 'the repair IS the physics: A within %.2f of 1 at both sums, EE unmoved -- the '
                  'arm of record may follow' % TOL_D)
    elif any(tt[s]['frac'] < FRAC_F for s in tt):
        v = ('F', 'the defect is ELSEWHERE, and that is the finding: A moves by less than a tenth '
                  'of its excess at a sum')
    elif all(tt[s]['frac'] > FRAC_E for s in tt):
        v = ('E', 'the repair is PART of it: A moves toward 1 by more than a third of its excess '
                  'at both sums but stays outside %.2f' % TOL_D)
    else:
        v = ('E', 'the repair is PART of it, between the bands -- reported as the fraction with '
                  'the shear spread')
    print('\n  ⇒ VERDICT (%s): %s' % v)
    rec['verdict'], rec['verdict_text'] = v[0], v[1]
    rec['A_spread_shear'] = spread
    rec['bands'] = dict(D=TOL_D, E=FRAC_E, F=FRAC_F, EE=EE_BAND)
    json.dump(rec, io.open(os.path.join(_HERE, 'refit.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote refit.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
