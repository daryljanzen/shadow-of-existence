# -*- coding: utf-8 -*-
"""r7882+60 — THE VALIDATION ON `r7879`'s OWN BANDS, AND GATES Ⓠ⓶ AND Ⓠ⓷.

`r7879`: *"Validate jointly: TT's `A` within `0.03` of one and EE within `0.03` of one, at `0.30`
and `0.60` eV, read on both fitters.  Only then a limit."*  And `PREDICTION.md`'s five rows, which
⛔ **must be mutually exclusive with exactly one firing** — this receipt CHECKS that rather than
assuming it, because `r7878`'s item ① had two rows fire at once and `r7880`'s had a row whose
condition was not defined.

⛔ **Ⓠ⓵ AND Ⓠ⓸ RAN FIRST AND BOTH ARE MET**, which is what makes any number below readable at all:
  `Ⓠ⓵` at `3.052e-05` and `3.331e-05` against `1e-04`; `Ⓠ⓸` on its two registered arms, the floor
  identified as the quadrature's (`floor.json`) and the fit's own reading of the limit at
  `1.161e-03` against `0.003` (`limitfit.json`).

⛔ **NO LIMIT IS READ IN THIS REVISION EVEN UNDER Ⓐ.**  `r7879` puts the limit in item ③, on the
  closed cross-seeded envelope, and that is a separate revision with its own registration.

⌗ NOT RETYPED: the fit is `r7874`'s own `shift.py` and the leg assembly is `limitfit.py`'s, both
  imported.  The `Ⓓ`/`Ⓔ` baseline is READ from `r7878`'s record by `fluid_baseline.json`.

    NODE=60 python3 validate.py
"""
import io
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from limitfit import BLOCKS, LANDED_DIR, A_WAS, amps, run_fit, legs, WORK      # noqa: E402

VSUMS = ('0.30', '0.60')         # here the slots ARE the sums: these legs are fitted on target
#: ⛔ *`R7882_BANKS` narrows the read to banks that EXIST, so the validation verdict can be read
#: as soon as `base` lands rather than waiting on the convergence banks.  It narrows WHAT IS READ;
#: it cannot change a criterion.  Unset, all three are read, and a run that reads fewer MARKS
#: ITSELF PARTIAL in its own record, so a partial read cannot be mistaken for the whole one.*
BANKS = tuple((os.environ.get('R7882_BANKS') or 'base nq24 lmax18').split())
VALID = os.path.join(_HERE, 'valid')
BAND = 0.03                      # r7879's own joint band, taken unchanged
MOVE = 0.003                     # PREDICTION.md's registered tenth of it, for Ⓠ⓶ and Ⓠ⓷


def vlegs(bank):
    """`limitfit.legs` for a `valid/` bank — same assembly, same reason, different source"""
    import shutil
    d = os.path.join(WORK, 'valid_%s' % bank)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    os.symlink(os.path.join(LANDED_DIR, 'lcdm_S000.npz'), os.path.join(d, 'lcdm_S000.npz'))
    for slot in ('S030', 'S060'):
        src = os.path.join(VALID, bank, 'lcdm_%s_pol.npz' % slot)
        if not os.path.isfile(src):
            raise SystemExit('  ⛔ missing leg %s -- run gen_valid.sh first' % src)
        os.symlink(src, os.path.join(d, 'lcdm_%s.npz' % slot))
    return d


def main():
    print(__doc__)
    rec = {'BAND': BAND, 'MOVE': MOVE}
    os.makedirs(WORK, exist_ok=True)

    # ══ THE REPRODUCTION LEG ════════════════════════════════════════════════════════════════════
    base = amps(run_fit('v_reproduction', LANDED_DIR))
    bad = ['%s: %.6f against %.5f' % (k, base[k], A_WAS[k])
           for k in A_WAS if abs(base[k] - A_WAS[k]) > 5e-05]
    rec['reproduction'] = {'A': base, 'expected': A_WAS, 'reproduced': not bad}
    print('\n-- REPRODUCTION LEG: %s' % ('REPRODUCED' if not bad else '** NOT ** ' + '; '.join(bad)))
    if bad:
        raise SystemExit('  ⛔ the fit of record does not reproduce its own landed amplitudes, so '
                         'nothing downstream of it is read')

    # ══ THE THREE BANKS ═════════════════════════════════════════════════════════════════════════
    got = {}
    for bank in BANKS:
        got[bank] = amps(run_fit('valid_%s' % bank, vlegs(bank)))
    rec['A'] = got

    def off_one(bank, blk, s):
        return abs(got[bank]['%s|%s' % (blk, s)] - 1.0)

    print('\n' + '=' * 100)
    print('  THE VALIDATION: the hierarchy at the banked resolution, against CAMB on its own sums')
    print('=' * 100)
    print('%6s %6s %14s %16s   %s' % ('block', 'Sum', 'A', '|A-1|', 'against %.2f' % BAND))
    for blk in BLOCKS:
        for s in VSUMS:
            print('%6s %6s %14.6f %16.5f   %s'
                  % (blk, s, got['base']['%s|%s' % (blk, s)], off_one('base', blk, s),
                     'INSIDE' if off_one('base', blk, s) <= BAND else '** OUTSIDE **'))

    # ══ GATES Ⓠ⓶ AND Ⓠ⓷ ═════════════════════════════════════════════════════════════════════════
    print('\n' + '=' * 100)
    print('  GATES Ⓠ⓶ (the q-grid doubled) AND Ⓠ⓷ (the l-cutoff raised by half)')
    print('=' * 100)
    conv = {}
    for bank, gate in (('nq24', 'Ⓠ⓶'), ('lmax18', 'Ⓠ⓷')):
        if bank not in got:
            print('  %s  NOT READ IN THIS RUN: the %s bank is not built yet, and a gate not'
                  ' read is NOT a gate met.' % (gate, bank))
            conv[gate] = {'bank': bank, 'read': False, 'met': None}
            continue
        moves = dict(('%s|%s' % (b, s),
                      abs(got[bank]['%s|%s' % (b, s)] - got['base']['%s|%s' % (b, s)]))
                     for b in BLOCKS for s in VSUMS)
        worst = max(moves.values())
        conv[gate] = {'bank': bank, 'read': True, 'moves': moves, 'worst': worst,
                      'met': bool(worst < MOVE)}
        print('  %s  worst move in A over both blocks and both sums: %.3e against %.3f  -> %s'
              % (gate, worst, MOVE, 'MET' if worst < MOVE else '** NOT MET **'))
        for k in sorted(moves):
            print('        %-10s %.3e' % (k, moves[k]))
    rec['convergence'] = conv
    rec['partial'] = bool(any(conv[g].get('read') is False for g in conv))
    rec['banks_read'] = list(BANKS)
    rec['converged'] = bool(all(conv[g]['met'] is True for g in conv))
    if rec['partial']:
        print('\n  ⛔ ** A PARTIAL READ: the banks read were %s.  A convergence gate not read'
              % ', '.join(BANKS))
        print('       is NOT a convergence gate met.  The verdict below is the VALIDATION verdict')
        print('       and the convergence gates are reported when their banks land. **')
    if not rec['converged']:
        print('\n  ⛔ ** THE NUMERICS CAN DECIDE THE VERDICT: at least one convergence gate is not')
        print('       met at this cost, so the verdict below is reported WITH that stated and the')
        print('       un-converged direction named.  That is a result about the method\'s cost, as')
        print('       the registration says, and it is not hidden behind the verdict. **')

    # ══ THE FIVE ROWS ═══════════════════════════════════════════════════════════════════════════
    fl = json.load(io.open(os.path.join(_HERE, 'fluid_baseline.json'), encoding='utf-8'))
    bl = dict((s, fl['best_TT_off_one'][s]['value']) for s in VSUMS)
    bl_arm = dict((s, fl['best_TT_off_one'][s]['arm']) for s in VSUMS)
    tt_in = all(off_one('base', 'TT', s) <= BAND for s in VSUMS)
    ee_in = all(off_one('base', 'EE', s) <= BAND for s in VSUMS)
    closer_both = all(off_one('base', 'TT', s) < bl[s] for s in VSUMS)
    rows = {
        'Ⓐ': tt_in and ee_in,
        'Ⓑ': tt_in and not ee_in,
        'Ⓒ': ee_in and not tt_in,
        'Ⓓ': (not tt_in) and (not ee_in) and closer_both,
        'Ⓔ': (not tt_in) and (not ee_in) and not closer_both,
    }
    MEAN = {
        'Ⓐ': 'the repair VALIDATES JOINTLY and a limit may be read -- the first time any candidate '
             'reaches this. The limit itself is item ③, not this revision.',
        'Ⓑ': 'REFUSED BY THE CONSTRAINT: TT is inside at both sums and EE is not, and no limit is '
             'read.',
        'Ⓒ': 'THE HIERARCHY DOES NOT CLOSE THE TT EXCESS, and the fraction it does close is '
             'reported per sum.',
        'Ⓓ': 'A BETTER MODEL OF THE SECTOR AND STILL NOT THE REPAIR, with the improvement '
             'reported as a fraction.',
        'Ⓔ': 'THE SECTOR IS NOT WHERE THE EXCESS IS, and that is the finding.',
    }
    fired = [k for k in rows if rows[k]]
    rec['rows'] = rows
    rec['fired'] = fired
    rec['baseline'] = {'off_one': bl, 'arm': bl_arm, 'TT_closer_at_both': bool(closer_both)}
    rec['validation'] = {'TT_inside_both': bool(tt_in), 'EE_inside_both': bool(ee_in),
                         'off_one': dict(('%s|%s' % (b, s), off_one('base', b, s))
                                         for b in BLOCKS for s in VSUMS)}
    print('\n' + '=' * 100)
    print('  THE FIVE ROWS, and the check that EXACTLY ONE fires')
    print('=' * 100)
    print('  TT inside %.2f at both sums: %s        EE inside at both: %s' % (BAND, tt_in, ee_in))
    print('  the fluid family\'s best TT off one (arm %s / %s): %.5f at 0.30, %.5f at 0.60'
          % (bl_arm['0.30'], bl_arm['0.60'], bl['0.30'], bl['0.60']))
    print('  this revision\'s TT off one:                        %.5f at 0.30, %.5f at 0.60'
          % (off_one('base', 'TT', '0.30'), off_one('base', 'TT', '0.60')))
    print('  TT strictly closer to one than that at BOTH sums: %s' % closer_both)
    for k in ('Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ'):
        print('    %s  %s' % (k, 'FIRES' if rows[k] else '-'))
    if len(fired) != 1:
        rec['exactly_one'] = False
        json.dump(rec, io.open(os.path.join(_HERE, 'validate.json'), 'w', encoding='utf-8'),
                  indent=1, sort_keys=True)
        raise SystemExit('  ⛔ %d row(s) fired, not one: %s -- the registration is defective and '
                         'the verdict is NOT reported until it is repaired'
                         % (len(fired), ', '.join(fired) or 'none'))
    rec['exactly_one'] = True
    print('\n  ⇒ ** VERDICT %s: %s **' % (fired[0], MEAN[fired[0]]))
    if not rec['converged']:
        print('  ⇒ ** AND THE CONVERGENCE GATES DO NOT YET STAND BEHIND IT **, per the lines above.')
    print('\n  ⌗ cc66\'s second fit reads these same legs, which are banked whatever this verdict '
          'is;\n    a disagreement beyond its own reproduction tolerance IS the finding and no '
          'limit is read\n    through either fitter.')
    json.dump(rec, io.open(os.path.join(_HERE, 'validate.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote validate.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
