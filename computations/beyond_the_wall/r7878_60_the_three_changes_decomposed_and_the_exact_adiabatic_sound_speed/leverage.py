#!/usr/bin/env python3
"""r7878+60 — ** AN UNREGISTERED READ, DECLARED AS SUCH. **

⛔ *`PREDICTION.md` registers nothing about this, and it was computed AFTER ①'s and ②'s verdicts
  were fixed and committed.  Nothing in the result depends on it, no criterion is moved by it, and
  it is offered as the NEXT QUESTION rather than as a finding of this revision.*  It is written down
  because the registered rows say which arms fail and not WHY, and the reason turns out to be one
  number per arm.

Each change moves TT and EE together.  What the data wants is a particular RATIO of those two
moves: TT must come `\\lvert A_TT - 1 \\rvert` and EE only `\\lvert A_EE - 1 \\rvert`, so

    required leverage  =  |A_TT - 1| / |A_EE - 1|      on the arm of record

and each arm delivers a leverage of its own, `|dA_TT| / |dA_EE|`.  An arm with the right leverage
and too small a move is a different situation from an arm with the wrong leverage, and the
registered table cannot tell them apart.

    NODE=60 python3 leverage.py
"""
import io
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(io.open(os.path.join(_HERE, 'refit_parts.json'), encoding='utf-8'))
L, A = D['A_landed'], D['arms']
SUMS = ('0.30', '0.60')
NAME = {'W': 'the weight change', 'C': 'the continuity change', 'E': 'the Euler change',
        'A1': 'all three, exact c_a2', 'CE': 'the named subset CE, exact c_a2'}

rec = {'declared': 'UNREGISTERED -- computed after the verdicts were fixed', 'required': {},
       'arms': {}}
for s in SUMS:
    tt, ee = abs(L['TT|%s' % s] - 1.0), abs(L['EE|%s' % s] - 1.0)
    rec['required'][s] = {'tt': tt, 'ee': ee, 'leverage': tt / ee}

print(__doc__)
print('=' * 100)
print('  the arm of record is %.5f from one in TT and %.5f in EE at Sigma = 0.30, and %.5f and '
      '%.5f at 0.60' % (rec['required']['0.30']['tt'], rec['required']['0.30']['ee'],
                        rec['required']['0.60']['tt'], rec['required']['0.60']['ee']))
print('  ⇒ REQUIRED LEVERAGE: %.3f at 0.30 and %.3f at 0.60\n'
      % (rec['required']['0.30']['leverage'], rec['required']['0.60']['leverage']))
print('  arm                              sum      dA_TT      dA_EE   leverage   of required'
      '   of the TT excess')
for suf in ('W', 'C', 'E', 'A1', 'CE'):
    if suf not in A:
        continue
    rec['arms'][suf] = {}
    for s in SUMS:
        f = A[suf]['fits']
        dtt = L['TT|%s' % s] - f['TT|%s' % s]['best_A']
        dee = L['EE|%s' % s] - f['EE|%s' % s]['best_A']
        lev = abs(dtt) / abs(dee)
        rec['arms'][suf][s] = {'d_tt': dtt, 'd_ee': dee, 'leverage': lev,
                               'of_required': lev / rec['required'][s]['leverage'],
                               'frac_of_excess': f['TT|%s' % s]['frac_of_excess']}
        print('  %-32s %4s %10.5f %10.5f %10.3f %13.3f %18.4f'
              % (NAME[suf], s, dtt, dee, lev, rec['arms'][suf][s]['of_required'],
                 f['TT|%s' % s]['frac_of_excess']))

#: the one statement the table makes, computed rather than eyeballed
_right = [suf for suf in rec['arms']
          if all(0.75 <= rec['arms'][suf][s]['of_required'] <= 1.5 for s in SUMS)]
_weak = [suf for suf in _right
         if all(rec['arms'][suf][s]['frac_of_excess'] < 0.75 for s in SUMS)]
_strong = [suf for suf in rec['arms']
           if any(rec['arms'][suf][s]['frac_of_excess'] >= 0.75 for s in SUMS)]
_strong_wrong = [suf for suf in _strong
                 if any(rec['arms'][suf][s]['of_required'] < 0.75 for s in SUMS)]
rec['right_leverage'] = sorted(_right)
rec['right_leverage_but_too_weak'] = sorted(_weak)
rec['strong_enough'] = sorted(_strong)
rec['strong_but_wrong_leverage'] = sorted(_strong_wrong)
print('\n  ⇒ right leverage (within a factor 4/3 of required at both sums): %s'
      % ', '.join(NAME[x] for x in rec['right_leverage']) or 'none')
print('  ⇒ and EVERY ONE OF THEM REMOVES LESS THAN THREE QUARTERS OF THE TT EXCESS: %s'
      % ', '.join(NAME[x] for x in rec['right_leverage_but_too_weak']))
print('  ⇒ the only arm that removes three quarters or more: %s -- and its leverage is WRONG: %s'
      % (', '.join(NAME[x] for x in rec['strong_enough']),
         ', '.join(NAME[x] for x in rec['strong_but_wrong_leverage'])))
rec['one_statement'] = bool(rec['right_leverage_but_too_weak']
                            and rec['strong_but_wrong_leverage']
                            and not (set(rec['right_leverage'])
                                     & set(rec['strong_but_wrong_leverage'])))
print('\n  ⇒ %s' % ('THE TWO SETS DO NOT OVERLAP: no member of this family has both the right '
                     'leverage and enough of the move.  ⌗ UNREGISTERED -- the next question, not '
                     'a result of this revision.'
                     if rec['one_statement'] else
                     'the two sets overlap, so the table does not make that statement'))
json.dump(rec, io.open(os.path.join(_HERE, 'leverage.json'), 'w', encoding='utf-8'),
          indent=1, sort_keys=True)
print('  wrote leverage.json')
