# -*- coding: utf-8 -*-
"""r7884+60 — THE CONTROL'S LIMITS ON THE JOINTLY VALIDATED SECTOR, ON THE CLOSED ENVELOPE.

`r7879` item ③, read now that `r7882` met the order's *"only then"* condition: `A` within `0.03` of
one in TT **and** EE at both sums, with both convergence gates met.

⌗ **NOT RETYPED, AND THAT IS THE POINT.** The ruler, `attach` and the profile reader are `r7864`'s;
the cross-seeding closure, its sum grid, its `Δχ² = 2.71` and its cold starts are `r7870`'s
`envelope_closed.py`, imported whole. **Only the two banks differ.** So a difference between these
numbers and `r7870`'s separating rung is the CLOSURE OF THE NEUTRINO SECTOR and not the method.

⛔ **THE GRID IS ASSEMBLED, NOT RE-RUN, AND THE ASSEMBLY IS CHECKED.** `PREDICTION.md`'s structural
reads: the switch refuses a zero sum because at zero sum the species is exactly massless, so the
eight parameter-offset directions per arm — every one of which the generator runs at `MNU = 0.00` —
and the zero node itself are the SAME spectra either way and are carried from the landed no-offset
rung WITHOUT approximation. Only the five positive nodes per arm were re-solved. Gate `Ⓛ⓵` reads
every carried point's own recorded config and gate `Ⓛ⓶` every new one's, rather than trusting the
directory they sit in.

⚠ **AND A CROSSING ON THE MINIMISED COLUMN IS AN ENVELOPE CROSSING, NEVER A LIMIT** — `r7870`'s own
rule for the file this imports: *"a closed envelope is a lower envelope over the basins REACHED, not
a proved global minimum. Cross-seeding cannot find a basin no node ever entered."* The limit, if one
is read at all, is read on the CALIBRATED column.

⛔ **AND IT IS CONDITIONAL.** `r7879` requires the validation on BOTH fitters and `r7882` is one.
`cc66`'s second fit reads `r7882`'s banked legs, and a disagreement beyond its own reproduction
tolerance IS the finding with no limit read through either. Nothing below is offered as settled
while that is outstanding.

    NODE=60 python3 limits_nuhier.py
"""
import ast
import io
import json
import os
import shutil
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7870 = os.path.join(_BTW, 'r7870_60_the_separating_grid_the_corrected_control_and_the_cache_that'
                           '_relabelled_a_column')

#: the landed no-offset rung, which is THIS revision's generators' own lineage -- the like-for-like
#: comparison, and NOT the `+0.044` corrected rung whose limit is the control's of record
CARRY_POL = os.path.join(BANK, 'pol_grid_bvel1_nufd_only')
CARRY_PP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_only')
NEW_POL = os.path.join(BANK, 'pol_grid_bvel1_nuhier')
NEW_PP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nuhier')
WORK = os.path.join(_HERE, '_legs')
OUT_POL = os.path.join(WORK, 'pol_full')
OUT_PP = os.path.join(WORK, 'pp_full')

ARMS = ('lcdm', 'cr')
NEW_TAGS = ('S006', 'S015', 'S030', 'S045', 'S060')          # the five the hierarchy can run at
CARRY_TAGS = ('S000', 'Sm06', 'Sm12',                        # the zero node and the two negatives
              'H0p', 'H0m', 'OMp', 'OMm', 'WBp', 'WBm', 'NSp', 'NSm')   # every one at MNU = 0.00
#: the sum each carried tag NAMES.  Anything not listed is a parameter-offset leg and sits at 0.00.
#: ⛭ *`Ⓛ⓵` used to demand `MNU == 0.00` of EVERY carried tag, which the two negative nodes in the
#:   line above can never satisfy -- they are carried precisely BECAUSE the hierarchy has no reading
#:   below zero.  So the gate could not pass on the carry set this module itself defines, and it was
#:   never caught because `r7884` landed this file REGISTERED AND UNRUN.  The clause the argument
#:   reasons from is not "every carried sum is zero" but "every carried point is the point its tag
#:   claims", and the four negatives are then COUNTED, because the registered fork `Ⓝ⓷′` turns on
#:   whether the minimum leans on them.*
CARRY_SUMS = {'S000': 0.0, 'Sm06': -0.06, 'Sm12': -0.12}
#: r7870's separating rung, read from its own record -- the like-for-like baseline
BASELINE_CALIB_MEV = 185.958
BASELINE_MIN_AT = 0.06

sys.path.insert(0, R7870)
os.environ.setdefault('RUNG', 'nufd_only')
import envelope_closed as EC                                                   # noqa: E402

#: ⛔ *SET AFTER the import and BEFORE `model6` is imported anywhere.  `envelope_closed` points the
#: keys at its own rung at module level, and `model6` reads `PPGRID` at ITS import time -- which
#: happens inside `main()` below.  `r7866` lost a whole grid to getting this order wrong.*
os.environ['POL_DIR'] = OUT_POL
os.environ['PPGRID'] = OUT_PP

FAILS = []
RAN = []


def gate(name, ok, got=None):
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    RAN.append(name)
    if not ok:
        FAILS.append(name)
    return ok


def _pol_cfg(d, arm, tag):
    with np.load(os.path.join(d, '%s_%s.npz' % (arm, tag)), allow_pickle=True) as z:
        return json.loads(str(z['config']))


def assemble():
    """the full 16-points-per-arm grid: carried where the switch is inert, new where it is not"""
    man = {'carried': [], 'new': [], 'from_carry_pol': os.path.basename(CARRY_POL),
           'from_carry_pp': os.path.basename(CARRY_PP),
           'from_new_pol': os.path.basename(NEW_POL), 'from_new_pp': os.path.basename(NEW_PP)}
    for out in (OUT_POL, OUT_PP):
        if os.path.isdir(out):
            shutil.rmtree(out)
        os.makedirs(out)
    for arm in ARMS:
        for tag in CARRY_TAGS:
            for suf in ('.npz', '_tt.npz'):
                src = os.path.join(CARRY_POL, '%s_%s%s' % (arm, tag, suf))
                if os.path.isfile(src):
                    shutil.copy2(src, os.path.join(OUT_POL, os.path.basename(src)))
            src = os.path.join(CARRY_PP, '%s_%s.json' % (arm, tag))
            if os.path.isfile(src):
                shutil.copy2(src, os.path.join(OUT_PP, os.path.basename(src)))
            man['carried'].append('%s_%s' % (arm, tag))
        for tag in NEW_TAGS:
            for suf in ('.npz', '_tt.npz'):
                src = os.path.join(NEW_POL, '%s_%s%s' % (arm, tag, suf))
                if os.path.isfile(src):
                    shutil.copy2(src, os.path.join(OUT_POL, os.path.basename(src)))
            src = os.path.join(NEW_PP, '%s_%s.json' % (arm, tag))
            if os.path.isfile(src):
                shutil.copy2(src, os.path.join(OUT_PP, os.path.basename(src)))
            man['new'].append('%s_%s' % (arm, tag))
    return man


def main():
    print(__doc__)
    print('=' * 104)
    rec = {'baseline': {'rung': 'r7870 separating (no offset on either arm)',
                        'calibrated_limit_meV': BASELINE_CALIB_MEV,
                        'min_at': BASELINE_MIN_AT},
           'sums': list(EC.SUMS), 'dchi2': float(EC.DCHI2), 'max_passes': int(EC.MAX_PASSES)}

    print('\n  THE ASSEMBLY')
    print('  ' + '-' * 102)
    rec['manifest'] = assemble()
    n_pol = len([f for f in os.listdir(OUT_POL) if f.endswith('.npz')
                 and not f.endswith('_tt.npz')])
    n_pp = len([f for f in os.listdir(OUT_PP) if f.endswith('.json')])
    print('    carried %d point(s) per grid, re-solved %d, assembled %d CMB and %d lensing'
          % (len(CARRY_TAGS) * len(ARMS), len(NEW_TAGS) * len(ARMS), n_pol, n_pp))

    # ══ Ⓛ⓵ THE CARRIED POINTS ARE CARRIABLE ═════════════════════════════════════════════════════
    print('\n  Ⓛ⓵  THE CARRIED POINTS, READ FROM THEIR OWN RECORDED CONFIG')
    bad, negatives = [], []
    for arm in ARMS:
        for tag in CARRY_TAGS:
            try:
                c = _pol_cfg(OUT_POL, arm, tag)
            except Exception as exc:                                        # noqa: BLE001
                bad.append('%s_%s unreadable: %s' % (arm, tag, exc))
                continue
            if c.get('NUHIER'):
                bad.append('%s_%s records the switch ON' % (arm, tag))
            want = CARRY_SUMS.get(tag, 0.0)
            if abs(float(c.get('MNU', -99)) - want) > 1e-12:
                bad.append('%s_%s records MNU = %r, not the %.2f its tag names'
                           % (arm, tag, c.get('MNU'), want))
            if want < 0.0:
                negatives.append('%s_%s' % (arm, tag))
    gate('Ⓛ⓵ every carried point records the switch ABSENT and the sum ITS OWN TAG NAMES, so each '
         'carried point is the point it claims to be -- and the carried set holds EXACTLY the four '
         'negative nodes the registered fork turns on, neither more nor fewer',
         not bad and len(negatives) == 2 * len([t for t in CARRY_SUMS if CARRY_SUMS[t] < 0.0]),
         '; '.join(bad[:4]) if bad else '%d point(s), of which %d negative: %s'
         % (len(CARRY_TAGS) * len(ARMS), len(negatives), ' '.join(negatives)))

    # ══ Ⓛ⓶ THE NEW POINTS ARE THE HIERARCHY'S, AT THE GATED GRID ════════════════════════════════
    print('\n  Ⓛ⓶  THE RE-SOLVED POINTS, READ FROM THEIR OWN RECORDED CONFIG')
    want = {'S006': 0.06, 'S015': 0.15, 'S030': 0.30, 'S045': 0.45, 'S060': 0.60}
    bad2 = []
    for arm in ARMS:
        for tag in NEW_TAGS:
            try:
                c = _pol_cfg(OUT_POL, arm, tag)
            except Exception as exc:                                        # noqa: BLE001
                bad2.append('%s_%s unreadable: %s' % (arm, tag, exc))
                continue
            if c.get('NUHIER') is not True:
                bad2.append('%s_%s does not record the switch ON' % (arm, tag))
            if abs(float(c.get('MNU', -1)) - want[tag]) > 5e-07:
                bad2.append('%s_%s records MNU = %r, not %.2f' % (arm, tag, c.get('MNU'),
                                                                  want[tag]))
            if (c.get('NQ'), c.get('LMAXNU')) != (12, 12):
                bad2.append('%s_%s is at NQ/LMAXNU %r/%r, not the gated 12/12'
                            % (arm, tag, c.get('NQ'), c.get('LMAXNU')))
            if abs(float(c.get('QMAXNU', -1)) - 20.0) > 1e-12:
                bad2.append('%s_%s is at QMAXNU %r, not 20' % (arm, tag, c.get('QMAXNU')))
    gate('Ⓛ⓶ every re-solved point records the switch ON, its own sum, and the grid r7882\'s gates '
         'fixed -- so these spectra are known to be the validated closure\'s', not bad2,
         '; '.join(bad2[:4]) if bad2 else '%d point(s)' % (len(NEW_TAGS) * len(ARMS)))

    # ══ Ⓛ⓷ THE MACHINERY IS THE ONE OF RECORD ═══════════════════════════════════════════════════
    print('\n  Ⓛ⓷  THE MACHINERY')
    #: ⛭ READ THE STRUCTURE, NOT THE SOURCE TEXT.  This gate used to ask `'def closed_envelope' not
    #:   in src` of its own file -- and its own assertion contains that very string, so the test was
    #:   false for every file that carried the test.  It also asked `'import envelope_closed as EC'
    #:   in src`, which its own text made trivially TRUE.  So one half could never pass and the other
    #:   could never fail, and neither was caught because this file landed REGISTERED AND UNRUN.
    #:   The parse tree cannot be fooled by the question being written down.
    src = io.open(os.path.join(_HERE, os.path.basename(__file__)), encoding='utf-8').read()
    _tree = ast.parse(src)
    _defines = {n.name for n in ast.walk(_tree)
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    _forbidden = sorted(d for d in _defines
                        if d == 'closed_envelope' or d.startswith(('_fit', '_cold')))
    _imports_ec = any(isinstance(n, ast.Import)
                      and any(al.name == 'envelope_closed' and al.asname == 'EC' for al in n.names)
                      for n in ast.walk(_tree))
    gate('Ⓛ⓷ the closure, its sum grid, its threshold and its fitters are IMPORTED from the file of '
         'record, and this file defines none of them -- read off the PARSE TREE, so the gate cannot '
         'be satisfied or defeated by its own wording',
         _imports_ec and not _forbidden
         and abs(EC.DCHI2 - 2.71) < 1e-12
         and list(EC.SUMS) == [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
         and min(EC.SUMS) >= 0.0,
         'imports EC as EC: %s; defines forbidden: %s; DCHI2 %.2f, %d sums, lowest %.2f'
         % (_imports_ec, _forbidden or 'none', EC.DCHI2, len(EC.SUMS), min(EC.SUMS)))

    import model3 as M3                                                     # noqa: E402
    import distances as DI                                                  # noqa: E402
    import model6 as M6                                                     # noqa: E402

    # ══ Ⓛ⓸ THE GRIDS IN USE ARE THE ASSEMBLED ONES ══════════════════════════════════════════════
    print('\n  Ⓛ⓸  THE GRIDS THIS MODEL ACTUALLY HOLDS')
    print('    the CMB grid in use     : %s' % os.environ['POL_DIR'])
    print('    the lensing grid in use : %s' % M6.GRID)
    gate('Ⓛ⓸ the model holds the ASSEMBLED grids, not the rung the imported file points at -- read '
         'off the model rather than off the environment',
         os.path.realpath(M6.GRID) == os.path.realpath(OUT_PP)
         and os.path.realpath(os.environ['POL_DIR']) == os.path.realpath(OUT_POL),
         os.path.basename(M6.GRID))
    rec['plumbing'] = {'pol_dir': os.path.basename(OUT_POL), 'pp_grid': os.path.basename(M6.GRID),
                       'holds_assembled': bool(os.path.realpath(M6.GRID)
                                               == os.path.realpath(OUT_PP))}

    # ══ Ⓛ⓹ THE LENSING POINTS ARE THE HIERARCHY'S TOO, READ OFF THEIR OWN RECORDS ═══════════════
    #: ⛭ *r7884+60, added after the first banked point was looked at.  Ⓛ⓵ and Ⓛ⓶ read the CMB
    #: side's `config`, and there was NO gate on the lensing side at all -- not because it passed,
    #: but because `phiphi_point.py` did not record the four switches, so the check was
    #: IMPOSSIBLE.  ⛔ The lensing bandpowers go into the same limit, so an unverifiable half is an
    #: unverified limit.  The recorder is completed in the same revision and this reads it.*
    print('\n  Ⓛ⓹  THE LENSING POINTS, READ FROM THEIR OWN RECORDED SWITCHES')
    bad5 = []
    for arm in ARMS:
        for tag in NEW_TAGS:
            f = os.path.join(OUT_PP, '%s_%s.json' % (arm, tag))
            try:
                d = json.loads(io.open(f, encoding='utf-8').read())
            except Exception as exc:                                        # noqa: BLE001
                bad5.append('%s_%s unreadable: %s' % (arm, tag, exc))
                continue
            sw = d.get('switches', {})
            if sw.get('NUHIER') != '1':
                bad5.append('%s_%s records NUHIER = %r, not on' % (arm, tag, sw.get('NUHIER')))
            if (sw.get('NQ'), sw.get('LMAXNU')) != ('12', '12'):
                bad5.append('%s_%s is at NQ/LMAXNU %r/%r, not the gated 12/12'
                            % (arm, tag, sw.get('NQ'), sw.get('LMAXNU')))
            if sw.get('QMAXNU') != '20':
                bad5.append('%s_%s is at QMAXNU %r, not 20' % (arm, tag, sw.get('QMAXNU')))
            if abs(float(d.get('mnu', -1)) - want[tag]) > 5e-07:
                bad5.append('%s_%s records mnu = %r, not %.2f' % (arm, tag, d.get('mnu'),
                                                                  want[tag]))
    gate('Ⓛ⓹ every re-solved LENSING point records the switch on, the gated grid and its own sum '
         'in its OWN file -- the half of the limit that had no gate because the record did not '
         'exist, not because it passed', not bad5,
         '; '.join(bad5[:4]) if bad5 else '%d point(s)' % (len(NEW_TAGS) * len(ARMS)))
    rec['lensing_provenance'] = {'checked': len(NEW_TAGS) * len(ARMS), 'bad': bad5}

    if FAILS:
        rec['gates_failed'] = FAILS
        json.dump(rec, io.open(os.path.join(_HERE, 'limits_nuhier.json'), 'w', encoding='utf-8'),
                  indent=1, sort_keys=True, default=float)
        raise SystemExit('\n  ⛔ %d PLUMBING GATE(S) FAILED: %s\n     ** NO LIMIT NUMBER IS READ. '
                         'A limit read through unverified plumbing is not a limit, and this line '
                         'has already spent one whole grid on the wrong reading of a re-point. **'
                         % (len(FAILS), '; '.join(FAILS)))
    #: ⛭ COUNT THE GATES THAT RAN; DO NOT TYPE THE NUMBER.  This line said "all four plumbing gates
    #:   pass" after a FIFTH gate had been added beside it, so the module understated its own
    #:   checking in its own output.  A printed count that is typed rather than derived goes stale the
    #:   moment a gate is added -- the same shape as a receipt pinning a figure it does not measure.
    print('\n  ⇒ all %d plumbing gate(s) pass, so a number below is readable at all' % len(RAN))

    # ══ THE TWO READS, ON THE CLOSED ENVELOPE ═══════════════════════════════════════════════════
    def _mod():
        m = M6.Model6('lcdm')
        raw = m.amp_cmb
        m.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        return m

    rec['minimised'] = EC.closed_envelope(
        _mod(), 'THE RULER MINIMISED, on the envelope CLOSED under cross-seeding')
    r_inst = EC.L7864.Ruler(os.path.join(EC.R7864, 'rd_grid_nufd.npz'), 'r_drag',
                            "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                            'instrument')
    modc = _mod()
    EC.L7864.attach(modc, r_inst, M3, DI)
    rec['calibrated'] = EC.closed_envelope(
        modc, 'CALIBRATED on the repaired drag epoch, envelope CLOSED under cross-seeding')

    # ══ THE REGISTERED FORK, ON WHERE THE MINIMUM FALLS ═════════════════════════════════════════
    cal, mini = rec['calibrated'], rec['minimised']
    at = float(cal['min_at'])
    print('\n  THE REGISTERED FORK: where does the CALIBRATED profile\'s minimum fall?')
    print('  ' + '-' * 102)
    print('    the minimum sits at Sum = %.3f eV' % at)
    if at >= 0.06 - 1e-9:
        branch, read = 'Ⓝ⓵′', True
        why = ('the minimum is at 0.06 eV or above, so every profile point from it upward is '
               'supported by nodes this revision solved plus the exactly-carried zero node')
    elif abs(at) < 1e-9:
        branch, read = 'Ⓝ⓶′', True
        why = ('the minimum is at the zero node, which is exactly carriable, and the crossing runs '
               'upward through nodes this revision solved')
    else:
        branch, read = 'Ⓝ⓷′', False
        why = ('the minimum is at 0.03 eV, whose interpolation leans on a carried NEGATIVE node -- '
               'not like for like -- so the minimum\'s own location would rest on the landed '
               'closure. The grid needs the negative nodes re-solved, and the hierarchy has no '
               'reading there')
    rec['fork'] = {'branch': branch, 'min_at': at, 'limit_readable': read, 'why': why}
    print('    ⇒ branch %s: %s' % (branch, why))

    if not read:
        print('\n  ⛔ ** NO LIMIT IS READ, AND THE GRID IS REPORTED INSUFFICIENT FOR THIS SECTOR '
              'RATHER THAN PATCHED. ** That is the finding.')
    else:
        #: ⛭ `closed_envelope` returns `crossing_meV`; there has never been a `limit_meV` key, and
        #:   this line asked for one -- a `KeyError` AFTER both envelope reads had completed, so the
        #:   whole read was spent and then thrown away.  The THIRD defect in this module from landing
        #:   it REGISTERED AND UNRUN, after `Ⓛ⓵`'s impossible clause and `Ⓛ⓷` reading its own wording.
        #:   ⌗ *The key is a CROSSING in both columns. Calling the calibrated one a limit is this
        #:   module's registered judgement -- the minimised column is an envelope crossing and never
        #:   a limit -- and not a rename of the number.*
        lim = cal['crossing_meV']
        print('\n  THE CALIBRATED READ, AGAINST r7870\'s SEPARATING RUNG')
        print('  ' + '-' * 102)
        print('    this revision, closed envelope : %s'
              % ('%.3f meV' % lim if lim is not None else 'NO LIMIT -- the profile dips'))
        print('    r7870, same rung, no closure   : %.3f meV' % BASELINE_CALIB_MEV)
        if lim is not None:
            rec['moved_meV'] = float(lim) - BASELINE_CALIB_MEV
            rec['moved_frac'] = rec['moved_meV'] / BASELINE_CALIB_MEV
            print('    the move                       : %+.3f meV  (%+.2f per cent)'
                  % (rec['moved_meV'], 100.0 * rec['moved_frac']))
        else:
            print('    ⇒ the CALIBRATED profile dips above its minimum, which r7864\'s discipline '
                  'reports as NO LIMIT rather than as a limit with a caveat')
    print('\n  AND THE MINIMISED COLUMN, WHICH IS NOT A LIMIT EITHER WAY')
    print('  ' + '-' * 102)
    print('    crossing %s;  monotonic above the minimum: %s'
          % ('%.3f meV' % mini['crossing_meV'] if mini.get('crossing_meV') else 'none',
             mini['monotonic_above_min']))
    print('    ⌗ r7870 measured this column as ALREADY unreadable on this rung, with a dip at '
          '0.200 eV of -0.0206,\n      and called the rung unseparated.  So an unreadable minimised '
          'profile here is NOT evidence\n      about the closure, and a crossing on it is an '
          'ENVELOPE crossing and never a limit.')
    print('\n  ⛔ ** AND THE WHOLE READ IS CONDITIONAL: ** r7879 requires the validation on BOTH '
          'fitters and\n     r7882 is one of them.  Until cc66\'s second fit returns, nothing here '
          'is settled.')
    json.dump(rec, io.open(os.path.join(_HERE, 'limits_nuhier.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True, default=float)
    print('\n  wrote limits_nuhier.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
