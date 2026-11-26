# -*- coding: utf-8 -*-
"""r7878+60 items ① and ② — `A` and `eps` refitted on each component, and on the exact sound speed.

⌗ **NOT RETYPED TWICE OVER.** The fit is `r7874`'s own `shift.py`, executed with exactly two lines
  rebound, and the rebinding itself is imported from `r7876`'s `refit.py` rather than written again
  — so the fit every number below is read through is the one `r7874` was judged on and `r7876` used,
  and there is no second copy of it anywhere.

⌗ **THE ZERO LEG IS THE LANDED ONE** at every reading, for the reason the generators give: the
  background switch is gated on a non-zero sum, so every switch in this family is provably inert
  there.

⌗ **THE REPRODUCTION LEG RUNS FIRST** and must return `r7874`'s four headline amplitudes on the
  landed bank, or nothing else here is readable.

    NODE=60 python3 refit_parts.py
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
_R7876 = os.path.join(_BTW, 'r7876_60_the_epoch_consistent_neutrino_perturbations_and_whether'
                            '_the_amplitude_excess_is_the_lean')
SHIFT = os.path.join(_R7874, 'shift.py')
LANDED = os.path.join(_BTW, 'bank', 'pol_grid_bvel1_nufd_only')
PARTS = os.path.join(_HERE, 'parts')
WORK = os.path.join(_HERE, '_legs')

sys.path.insert(0, _R7876)
from refit import the_two_rebindings                                        # noqa: E402

#: `r7874`'s headline, which the reproduction leg must return, and `r7876`'s all-three result
A_LANDED = {'TT|0.30': 1.15162, 'TT|0.60': 1.29592, 'EE|0.30': 1.01405, 'EE|0.60': 1.04630}
A_WCE = {'TT|0.30': 0.86401, 'TT|0.60': 0.81466, 'EE|0.30': 0.94474, 'EE|0.60': 0.91120}
#: the registration's bands, fixed before any of this ran
TOL_TT = 0.03
TOL_EE = 0.05


def legs(name, tag_suffix):
    """a leg directory in `shift.py`'s own naming: the landed zero, this arm's two sums"""
    d = os.path.join(WORK, name)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    os.symlink(os.path.join(LANDED, 'lcdm_S000.npz'), os.path.join(d, 'lcdm_S000.npz'))
    for tag in ('S030', 'S060'):
        srcf = os.path.join(PARTS, 'lcdm_%s%s_pol.npz' % (tag, tag_suffix))
        if not os.path.isfile(srcf):
            return None
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


#: the arms this file reads, and the suffix each one's legs carry
ARMS = [('weight only', 'W'), ('continuity only', 'C'), ('Euler only', 'E'),
        ('all three, exact c_a2', 'A1'),
        #: ⌘ ②'s SUBSET, named in `SUBSET_NAMED.md` and committed before this line existed.
        ('the named subset, exact c_a2', 'CE')]


def main():
    print(__doc__)
    os.makedirs(WORK, exist_ok=True)
    rec = {'bands': {'TT': TOL_TT, 'EE': TOL_EE}, 'A_landed': A_LANDED, 'A_WCE': A_WCE}

    rep = run_fit('landed', LANDED)
    rec['landed'] = rep
    bad = [k for k, v in A_LANDED.items() if abs(rep['fits'][k]['best_A'] - v) > 5e-05]
    rec['reproduced'] = not bad
    print('\n-- REPRODUCTION LEG: %s' % ('REPRODUCED' if not bad else '** NOT ** ' + str(bad)))
    if bad:
        print('   ⛔ nothing below is readable until the fit reproduces r7874.')

    rec['arms'] = {}
    for name, suf in ARMS:
        d = legs(suf, suf)
        if d is None:
            print('\n-- %s: legs not on disk yet, skipped' % name)
            continue
        rec['arms'][suf] = dict(name=name, fits=run_fit(suf, d)['fits'])

    print('\n' + '=' * 100)
    print('  THE COMPONENTS, against the landed fit and against all three together')
    print('=' * 100)
    print('%-22s %-9s %10s %10s %10s %12s' % ('arm', 'block|S', 'A landed', 'A here', '|A-1|',
                                              'of excess'))
    for suf, a in rec['arms'].items():
        for k in sorted(a['fits']):
            now = a['fits'][k]['best_A']
            was = A_LANDED[k]
            frac = (abs(was - 1.0) - abs(now - 1.0)) / abs(was - 1.0)
            a['fits'][k]['frac_of_excess'] = frac
            a['fits'][k]['crosses_one'] = bool((was - 1.0) * (now - 1.0) < 0)
            print('%-22s %-9s %10.5f %10.5f %10.5f %+12.4f%s'
                  % (a['name'], k, was, now, abs(now - 1.0), frac,
                     '   CROSSES' if a['fits'][k]['crosses_one'] else ''))

    # ── ①'s verdict, on the weight arm, on the bands fixed in PREDICTION.md ──────────────────
    if 'W' in rec['arms']:
        w = rec['arms']['W']['fits']
        tt = [w['TT|0.30']['best_A'], w['TT|0.60']['best_A']]
        ee = [abs(w['EE|0.30']['best_A'] - 1.0), abs(w['EE|0.60']['best_A'] - 1.0)]
        crosses = any(w['TT|%s' % s]['crosses_one'] for s in ('0.30', '0.60'))
        away = any(w['TT|%s' % s]['frac_of_excess'] < 0.0 for s in ('0.30', '0.60'))
        ee_out = any(v > TOL_EE for v in ee)
        #: ⛔⛭⛭ ** THE REGISTERED ROWS ARE NOT MUTUALLY EXCLUSIVE, AND THE FIRST VERSION OF THIS
        #:   BLOCK HID THAT BEHIND AN `elif` CHAIN. **  *`Ⓒ` fires on a crossing and `Ⓓ` fires on
        #:   EE leaving its band; nothing in `PREDICTION.md` says which governs when both hold,
        #:   and the chain silently preferred `Ⓒ` -- the softer of the two, since `Ⓓ` is the row
        #:   that says the order's expectation is REFUTED.  A precedence invented at reading time
        #:   is a criterion moved after the result.*  ⇒ ** Every row that fires is reported, and
        #:   the overlap is named as a defect of this seat's own registration rather than
        #:   resolved. **  The conditions themselves are untouched: each is the one registered.
        _ROWS = [
            ('A', "the order's expectation HOLDS: the weight change alone is the repair",
             all(abs(x - 1.0) <= TOL_TT for x in tt) and not ee_out and not crosses),
            ('B', 'right direction, not enough -- the fraction of the excess removed is '
                  'reported per sum',
             (not crosses) and (not away) and (not ee_out)
             and not all(abs(x - 1.0) <= TOL_TT for x in tt)),
            ('C', 'the weight change ALONE already overshoots, so the crossing is not the '
                  "continuity or Euler change's doing", crosses),
            ('D', "the order's expectation is REFUTED: the weight change alone moves A away "
                  'from one, or takes EE out of band', away or ee_out),
        ]
        _FIRED = [(k, t) for k, t in [(k, t) for k, t, c in _ROWS if c]]
        v = ('+'.join(k for k, _ in _FIRED) or '-',
             ' ;; '.join(t for _, t in _FIRED) or 'no registered row fires')
        print('\n  ⇒ ① VERDICT (%s): %s' % v)
        if len(_FIRED) > 1:
            print('     ** %d REGISTERED ROWS FIRE AT ONCE -- the registration did not make them '
                  'exclusive, and the overlap is reported, not resolved by a precedence invented '
                  'here. **' % len(_FIRED))
            for k, t in _FIRED:
                print('       (%s) %s' % (k, t))
        print('     TT A = %.5f, %.5f ;  EE |A-1| = %.5f, %.5f  (bands %.2f and %.2f)'
              % (tt[0], tt[1], ee[0], ee[1], TOL_TT, TOL_EE))
        print('     the rows, each evaluated on its own registered condition: %s'
              % ', '.join('%s=%s' % (k, 'FIRES' if c else 'no') for k, _, c in _ROWS))
        rec['verdict_1'], rec['verdict_1_text'] = v
        rec['verdict_1_rows'] = dict((k, bool(c)) for k, _, c in _ROWS)

        # ── the attribution, registered as a measurement and not an assumption ──────────────
        if all(x in rec['arms'] for x in ('W', 'C', 'E')):
            rec['attribution'] = {}
            for s in ('0.30', '0.60'):
                k = 'TT|%s' % s
                d_all = A_WCE[k] - A_LANDED[k]
                d_sum = sum(rec['arms'][x]['fits'][k]['best_A'] - A_LANDED[k]
                            for x in ('W', 'C', 'E'))
                rec['attribution'][s] = dict(summed=d_sum, all_three=d_all,
                                             ratio=(d_sum / d_all) if d_all else None)
                print('     attribution at Sigma %s: summed %+.5f against all-three %+.5f, '
                      'ratio %.4f' % (s, d_sum, d_all, d_sum / d_all))

    # ── ②'s verdict, read on EACH of its two registered arms ────────────────────────────────
    #: ⌗ *`PREDICTION.md` registers TWO arms for item ② -- all three changes live, and again with
    #:   whichever subset ① shows is sound -- and ONE outcome table.  So the table is read on each
    #:   arm separately, which is what "the arms" plus "REGISTERED OUTCOMES" says.  A first version
    #:   read it on the all-three arm alone and left the subset's verdict unstated.*
    #: ⚠ ** AND THE BASELINE IS DECLARED, BECAUSE IT IS NOT LIKE-FOR-LIKE ON THE SUBSET. **  The
    #:   registration fixes "closer to one than `c_s^2 = w` gave" against the LANDED all-three
    #:   figures, `0.86401` and `0.81466`, and those are what both arms are read against here.  A
    #:   `c_s^2 = w` leg of the SUBSET was not run, so for the subset the comparison is against a
    #:   different letter set as well as a different sound speed.  ⇒ *Stated rather than silently
    #:   assumed away: the registration chose the baseline before the result, so it stands, and the
    #:   limit of what it measures is named here.*
    rec['verdict_2_baseline'] = {'TT|0.30': A_WCE['TT|0.30'], 'TT|0.60': A_WCE['TT|0.60'],
                                 'like_for_like_on_the_subset': False}
    rec['verdict_2_arms'] = {}
    for _suf, _what in (('A1', 'all three changes live'),
                        ('CE', 'the named subset, `CE`')):
        if _suf not in rec['arms']:
            continue
        a1 = rec['arms'][_suf]['fits']
        tt = [a1['TT|0.30']['best_A'], a1['TT|0.60']['best_A']]
        ee = [abs(a1['EE|0.30']['best_A'] - 1.0), abs(a1['EE|0.60']['best_A'] - 1.0)]
        ee_out = any(v > TOL_EE for v in ee)
        closer = [abs(tt[i] - 1.0) < abs(A_WCE['TT|%s' % s] - 1.0)
                  for i, s in enumerate(('0.30', '0.60'))]
        better = all(closer)
        inside = all(abs(x - 1.0) <= TOL_TT for x in tt)
        #: the four rows, each on its own registered condition.  ⌗ *Unlike ①'s table these ARE
        #:   mutually exclusive, and that is checked rather than assumed: `Ⓖ` needs closer at BOTH
        #:   sums and `Ⓗ` needs no closer at EITHER, which are complements.*
        _rows = [('E', 'the repair is the physics; the arm of record may follow',
                  inside and not ee_out),
                 ('F', 'REFUSED BY THE CONSTRAINT, not by TT: EE leaves its band, so no limit is '
                       'read', inside and ee_out),
                 ('G', 'a better member of the family, still not the repair',
                  (not inside) and better),
                 ('H', 'the family is the wrong direction, and that is the finding',
                  (not inside) and not better)]
        _fired = [(k, t) for k, t, c in _rows if c]
        v = ('+'.join(k for k, _ in _fired) or '-',
             ' ;; '.join(t for _, t in _fired) or 'no registered row fires')
        print('\n  ⇒ ② VERDICT (%s) on %s: %s' % (v[0], _what, v[1]))
        if len(_fired) != 1:
            print('     ** %d ROWS FIRE -- reported, not resolved by a precedence invented here **'
                  % len(_fired))
        print('     TT A = %.5f, %.5f against c_s2 = w\'s %.5f, %.5f ;  EE |A-1| = %.5f, %.5f'
              % (tt[0], tt[1], A_WCE['TT|0.30'], A_WCE['TT|0.60'], ee[0], ee[1]))
        print('     closer to one than c_s2 = w at 0.30: %s ; at 0.60: %s'
              % (closer[0], closer[1]))
        rec['verdict_2_arms'][_suf] = {
            'verdict': v[0], 'text': v[1], 'closer': [bool(c) for c in closer],
            'rows': dict((k, bool(c)) for k, _, c in _rows),
            'tt': tt, 'ee': ee, 'inside_tt_band': bool(inside), 'ee_out_of_band': bool(ee_out)}
        if _suf == 'A1':
            rec['verdict_2'], rec['verdict_2_text'] = v

    json.dump(rec, io.open(os.path.join(_HERE, 'refit_parts.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True, default=float)
    print('\n  wrote refit_parts.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
