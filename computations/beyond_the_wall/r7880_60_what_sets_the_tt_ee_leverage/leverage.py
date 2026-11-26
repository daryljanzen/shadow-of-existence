# -*- coding: utf-8 -*-
"""r7880+60 item ① — WHAT SETS THE TT:EE LEVERAGE, on banks that already exist.

Order `r7879` (69) item ①, branch (b), bounded to one revision: *"Ask what in the instrument sets
the TT:EE response ratio, on banks that already exist.  If a sector outside the neutrinos carries a
TT-heavy signature (10.8 at 0.30 eV, 6.4 at 0.60), name it.  If nothing does, say so, and (b) is
closed."*

⌗ **NOT RETYPED.**  The fit is `r7874`'s own `shift.py`, executed with exactly the two lines
  `r7876` rebinds, and **the rebinding function itself is imported** from `r7876`'s `refit.py`.
  There is no second copy of the fit and no second copy of the rebinding anywhere.

⌗ **THE REPRODUCTION LEG RUNS FIRST** on the landed bank and must return `r7874`'s four headline
  amplitudes, or nothing below it is readable -- the same gate `r7878` ran under.

⌗ The candidate set, the band and the four outcomes were CLOSED in `PREDICTION.md` and pushed
  before this file existed.

    NODE=60 python3 leverage.py
"""
import io
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7876 = os.path.join(_BTW, 'r7876_60_the_epoch_consistent_neutrino_perturbations_and_whether_the'
                            '_amplitude_excess_is_the_lean')
_R7874 = os.path.join(_BTW, 'r7874_60_the_sum_response_by_source_term_and_the_correction'
                            '_that_decides_one_object')
SHIFT = os.path.join(_R7874, 'shift.py')
BANK = os.path.join(_BTW, 'bank')

sys.path.insert(0, _R7876)
from refit import the_two_rebindings                                            # noqa: E402

SUMS = ('0.30', '0.60')
BLOCKS = ('TT', 'EE')
#: `r7874`'s four headline amplitudes on the landed bank -- the reproduction gate
A_WAS = {'TT|0.30': 1.15162, 'TT|0.60': 1.29592, 'EE|0.30': 1.01405, 'EE|0.60': 1.04630}
BAND = 4.0 / 3.0                      # PREDICTION.md: r7878's own band, taken unchanged
#: ⛔⛭⛭ ** A GAP IN THIS SEAT'S OWN REGISTRATION, NAMED RATHER THAN QUIETLY FILLED. **
#:   *`PREDICTION.md` puts "has no readable move" in `Ⓓ`'s row and never says what READABLE means.
#:   One candidate turns out to move `A` by parts in a million, and a ratio of two such numbers is
#:   not a leverage -- it is a ratio of two roundings.*  ⇒ The threshold is taken from the FIT and
#:   not from this measurement, which is what keeps it from being a criterion chosen after the
#:   result: `shift.py` reports `A` to five decimals, so `1e-05` is the smallest move it can
#:   distinguish at all, and a leverage is readable only when BOTH blocks move more than that.
#:   ⌘ *Whether the gap is filled this way or the candidate is simply dropped, the verdict row is
#:   the same -- which is stated because a repair that could have changed the answer would need
#:   more than a footnote.*
READABLE = 1e-05                      # the fit's own last printed digit in `A`
REFERENCE = 'nufd_only'               # the landed configuration every candidate is read against

#: ⛔ the candidate set, exactly as `PREDICTION.md` closed it.  `bank` is the directory; `against`
#:   is the configuration the candidate is a change FROM; `recorded` is whether BOTH banks' own
#:   configs record the switch that distinguishes them, or only their directory names do.
CANDIDATES = [
    ('⓵ DNEFF = 0.0293', 'pol_grid_bvel1_nufd_dneff', REFERENCE, True),
    ('⓶ DNEFF = 0.044', 'pol_grid_bvel1_nufd_dneff044', REFERENCE, True),
    ('⓷ NUFD off', 'pol_grid_bvel1_nufd_off', REFERENCE, True),
    ('⓸ BVEL off', 'pol_grid', 'bvel1', False),
]
BANKS = {REFERENCE: 'pol_grid_bvel1_nufd_only', 'bvel1': 'pol_grid_bvel1'}


def run_fit(label, bank_dir):
    """execute `r7874`'s fit against this bank and hand back its own record"""
    out = os.path.join(_HERE, 'fit_%s.json' % label)
    keep = dict(os.environ)
    os.environ['R7876_ON'], os.environ['R7876_OUT'] = bank_dir, out
    ns = {'__name__': '_shift_of_r7874', '__file__': SHIFT}
    try:
        sys.path.insert(0, _R7874)
        print('\n' + '#' * 100)
        print('#  %s   (%s)' % (label, os.path.basename(bank_dir)))
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
    rec = {'band': BAND, 'reference': REFERENCE}

    # ══ THE REPRODUCTION LEG ════════════════════════════════════════════════════════════════════
    base = {}
    base[REFERENCE] = amps(run_fit(REFERENCE, os.path.join(BANK, BANKS[REFERENCE])))
    bad = ['%s: %.6f against %.5f' % (k, base[REFERENCE][k], w)
           for k, w in A_WAS.items() if abs(base[REFERENCE][k] - w) > 5e-05]
    rec['reproduced'] = not bad
    rec['landed'] = base[REFERENCE]
    print('\n-- REPRODUCTION LEG: %s'
          % ('REPRODUCED' if not bad else '** NOT ** ' + '; '.join(bad)))
    if bad:
        raise SystemExit('  ⛔ nothing below is readable until the fit reproduces r7874.')

    # ══ THE REQUIRED LEVERAGE, from the arm of record itself ════════════════════════════════════
    rec['required'] = {}
    for s in SUMS:
        tt, ee = (abs(base[REFERENCE]['TT|%s' % s] - 1.0),
                  abs(base[REFERENCE]['EE|%s' % s] - 1.0))
        rec['required'][s] = {'tt': tt, 'ee': ee, 'leverage': tt / ee}
    print('\n  REQUIRED LEVERAGE, read off the arm of record this run fitted, not remembered:')
    for s in SUMS:
        r = rec['required'][s]
        print('    Sigma %s:  TT is %.5f from one, EE %.5f  ->  %.3f'
              % (s, r['tt'], r['ee'], r['leverage']))

    # ══ EACH CANDIDATE ══════════════════════════════════════════════════════════════════════════
    base['bvel1'] = amps(run_fit('bvel1', os.path.join(BANK, BANKS['bvel1'])))
    rec['arms'] = {}
    for name, bank, against, recorded in CANDIDATES:
        tag = bank.replace('pol_grid', 'pg')
        a = amps(run_fit(tag, os.path.join(BANK, bank)))
        ref = base[against] if against in base else None
        if ref is None:
            raise SystemExit('  ⛔ no reference fit for %r' % against)
        row = {'bank': bank, 'against': against, 'provenance_recorded': bool(recorded),
               'amps': a, 'ref_amps': ref, 'sums': {}}
        for s in SUMS:
            dtt = ref['TT|%s' % s] - a['TT|%s' % s]
            dee = ref['EE|%s' % s] - a['EE|%s' % s]
            readable = min(abs(dtt), abs(dee)) > READABLE
            lev = (abs(dtt) / abs(dee)) if (readable and dee) else None
            row['sums'][s] = {
                'd_tt': dtt, 'd_ee': dee, 'leverage': lev, 'readable': bool(readable),
                'of_required': (lev / rec['required'][s]['leverage']) if lev else None,
                'in_band': bool(lev is not None
                                and 1.0 / BAND <= lev / rec['required'][s]['leverage'] <= BAND)}
        rec['arms'][name] = row

    print('\n' + '=' * 100)
    print('  EACH CANDIDATE\'S SUM-RESPONSE LEVERAGE, against what the arm of record requires')
    print('=' * 100)
    print('  %-18s %-7s %5s %11s %11s %10s %12s %8s'
          % ('candidate', 'recorded', 'sum', 'dA_TT', 'dA_EE', 'leverage', 'of required', 'in band'))
    for name, _b, _a, _r in CANDIDATES:
        row = rec['arms'][name]
        for s in SUMS:
            q = row['sums'][s]
            print('  %-18s %-7s %5s %11.6f %11.6f %10s %12s %8s'
                  % (name, 'yes' if row['provenance_recorded'] else 'NAME ONLY', s,
                     q['d_tt'], q['d_ee'],
                     '%.3f' % q['leverage'] if q['leverage'] is not None else 'UNREADABLE',
                     '%.3f' % q['of_required'] if q['of_required'] is not None
                     else 'no move > %g' % READABLE,
                     'YES' if q['in_band'] else 'no'))

    # ══ THE STEP CONTROL: the two DNEFF values must agree on the leverage ═══════════════════════
    #: *`PREDICTION.md` registers that a leverage differing between two steps of the same sector is
    #:  a property of the STEP and not of the sector.  `DNEFF` is the one candidate the banks give
    #:  at two step sizes, so it is the one that can be controlled this way.*
    d1, d2 = rec['arms']['⓵ DNEFF = 0.0293'], rec['arms']['⓶ DNEFF = 0.044']
    rec['step_control'] = {}
    for s in SUMS:
        a, b = d1['sums'][s]['leverage'], d2['sums'][s]['leverage']
        ok = bool(a and b and 1.0 / BAND <= a / b <= BAND)
        rec['step_control'][s] = {'small': a, 'large': b,
                                  'ratio': (a / b) if (a and b) else None, 'agrees': ok}
    print('\n  THE STEP CONTROL on the one sector banked at two step sizes:')
    for s in SUMS:
        c = rec['step_control'][s]
        print('    Sigma %s:  %s against %s  ->  ratio %s, %s'
              % (s, '%.3f' % c['small'] if c['small'] else '--',
                 '%.3f' % c['large'] if c['large'] else '--',
                 '%.3f' % c['ratio'] if c['ratio'] else '--',
                 'a property of the SECTOR' if c['agrees'] else
                 '** a property of the STEP -- UNREADABLE **'))

    # ══ THE ONE FIRING ROW ══════════════════════════════════════════════════════════════════════
    both = [n for n, _b, _a, _r in CANDIDATES
            if all(rec['arms'][n]['sums'][s]['in_band'] for s in SUMS)]
    one = [n for n, _b, _a, _r in CANDIDATES
           if any(rec['arms'][n]['sums'][s]['in_band'] for s in SUMS) and n not in both]
    unreadable = [n for n, _b, _a, _r in CANDIDATES
                  if all(rec['arms'][n]['sums'][s]['leverage'] is None for s in SUMS)]
    rows = [
        ('A', 'a sector outside the neutrinos carries it -- NAMED: %s' % ', '.join(both),
         bool(both)),
        ('B', 'named as PARTIAL -- in band at one sum and not the other: %s' % ', '.join(one),
         bool(one) and not both),
        ('C', 'nothing outside the neutrinos carries it, and (b) is CLOSED',
         not both and not one and len(unreadable) < len(CANDIDATES)),
        ('D', 'the existing banks cannot answer it -- every candidate unreadable; (b) stays OPEN',
         len(unreadable) == len(CANDIDATES)),
    ]
    fired = [(k, t) for k, t, c in rows if c]
    rec['rows'] = dict((k, bool(c)) for k, _t, c in rows)
    rec['verdict'] = '+'.join(k for k, _ in fired) or '-'
    rec['verdict_text'] = ' ;; '.join(t for _, t in fired) or 'no registered row fires'
    rec['exactly_one_fires'] = len(fired) == 1
    print('\n  ⇒ ① VERDICT (%s): %s' % (rec['verdict'], rec['verdict_text']))
    print('     the rows, each on its own registered condition: %s'
          % ', '.join('%s=%s' % (k, 'FIRES' if c else 'no') for k, _t, c in rows))
    print('     exactly one row fires: %s' % rec['exactly_one_fires'])
    if not rec['exactly_one_fires']:
        print('     ** THE REGISTRATION DID NOT MAKE THE ROWS EXCLUSIVE -- reported, not resolved **')
    json.dump(rec, io.open(os.path.join(_HERE, 'leverage.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True, default=float)
    print('\n  wrote leverage.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
