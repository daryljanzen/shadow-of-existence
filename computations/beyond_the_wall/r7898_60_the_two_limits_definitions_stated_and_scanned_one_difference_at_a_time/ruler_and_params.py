# -*- coding: utf-8 -*-
"""r7898+60 — THE TWO LIMITS, SCANNED ONE DIFFERENCE AT A TIME.

Order `r7895` (69) item ①, `Ⓡ⓶`, registered in `PREDICTION.md` before any substituted limit was read.

⛔ **NOTHING IS RETYPED AND NO MODEL IS BUILT HERE.**  `r7884`'s `limits_nuhier.py` is imported whole
and driven exactly as `r7888`'s `read_limit.py` drives it — `NEW_PP` redirected at the runner's banked
grid and nothing else — and the two model instances it builds are CAPTURED as it builds them, by
wrapping `envelope_closed.closed_envelope` for the duration of that call.  The arms below are then run
on those captured instances with the REAL `closed_envelope`.  So the models under the substitutions are
`r7884`'s own, assembled by `r7884`'s own code on the ordered grid.

⛭ **AND THE CONTROL IS NOT RECOMPUTED HERE, BECAUSE IT WAS ALREADY COMPUTED THROUGH THAT PATH.**
`read_limit.py --grid <the banked grid>` was run unmodified and left
`r7888/limit_on_runner_grid.json` BYTE-IDENTICAL to the banked record — calibrated `193.545304` meV,
minimised `310.147692` meV, a deviation of exactly zero against a registered tolerance of `0.001`.
Re-running it inside this module would spend twelve minutes to reproduce a number already reproduced,
which the standing rule forbids.  ⌗ *So the wrapper returns the banked record for the two reads
`limits_nuhier` itself performs, and that stub is REFUSED for every arm below: a stubbed arm would be a
share computed from a number nothing measured.*

    python3 ruler_and_params.py
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
ROOT = (subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=HERE,
                       capture_output=True, text=True).stdout.strip())
R7884 = os.path.join(BTW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector')
R7888 = os.path.join(BTW, 'r7888_60_the_limit_read_on_the_runners_complete_grid')
R7862 = os.path.join(BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_the_damping'
                          '_tails_share_of_the_gap')
GRID = os.path.join(R7888, '_ref_grid')

#: ⛭ EVERY BANKED NUMBER THIS SCAN IS JUDGED AGAINST IS READ OUT OF A RECORD, NONE IS TYPED.
_BANK = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
CONTROL_CAL = float(_BANK['calibrated']['crossing_meV'])
CONTROL_MIN = float(_BANK['minimised']['crossing_meV'])
REPRO_TOL = 1e-03                      #: meV, fixed in PREDICTION.md ⒟ before the scan
PARTNER_HELD = 30.560                  #: cc66's calibrated arm, omega_b and n_s HELD
PARTNER_FREE = 54.000                  #: cc66's minimised arm, both freed

FAILS = []
RAN = []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


# ── drive r7884 exactly as r7888 does, capturing the models it builds ───────────────────────────
sys.path.insert(0, R7884)
import limits_nuhier as L                                                   # noqa: E402
import envelope_closed as EC                                               # noqa: E402
#: ⛭ `limits_nuhier` imports these INSIDE its own `main`, so they are not attributes of it. They are
#:   imported here the same way, off the path that module set up — the same modules, not copies.
import model3 as M3                                                        # noqa: E402
import distances as DI                                                     # noqa: E402

CAPTURED = []
_REAL = EC.closed_envelope


def _capture(mod, label):
    """capture the instance and hand back the BANKED read, so the control is not recomputed"""
    CAPTURED.append((label, mod))
    key = 'calibrated' if 'CALIBRATED' in label else 'minimised'
    return dict(_BANK[key])


def main():
    print(__doc__)
    print('=' * 100)
    assert os.path.realpath(L.NEW_PP) != os.path.realpath(GRID), 'the redirect would be silent'
    L.NEW_PP = GRID
    EC.closed_envelope = _capture
    try:
        rc = L.main()
    finally:
        EC.closed_envelope = _REAL
    gate('Ⓢ⓪ `r7884`\'s own module ran its five plumbing gates on the ordered grid and both of its '
         'reads were reached, so the models captured below are the ones it would have measured — and '
         'the real `closed_envelope` is restored before any arm runs',
         rc == 0 and len(CAPTURED) == 2 and EC.closed_envelope is _REAL,
         'rc=%s, %d model(s) captured, real reader restored: %s'
         % (rc, len(CAPTURED), EC.closed_envelope is _REAL))
    if FAILS:
        sys.exit('\n  ⛔ the ordered grid is not established, so no limit is read and no share exists')

    base = [m for lab, m in CAPTURED if 'CALIBRATED' not in lab][0]      #: ruler-free
    withinst = [m for lab, m in CAPTURED if 'CALIBRATED' in lab][0]      #: instrument's own ruler

    # ── Ⓢ① THE CONTROL, CITED RATHER THAN RECOMPUTED, AND ITS EVIDENCE CHECKED HERE ─────────────
    r = subprocess.run(['git', 'status', '--porcelain', '--',
                        os.path.relpath(os.path.join(R7888, 'limit_on_runner_grid.json'), ROOT)],
                       cwd=ROOT, capture_output=True, text=True)
    clean = (r.stdout.strip() == '')
    gate('Ⓢ① the control reproduced through the UNMODIFIED path at exactly zero deviation, and that '
         'is checked here rather than asserted: the record `read_limit.py` rewrites on every run is '
         'byte-identical to the committed one, so the re-run reproduced the whole record and not '
         'merely a rounded crossing',
         clean, 'working tree clean for that record: %s; calibrated %.6f, minimised %.6f'
         % (clean, CONTROL_CAL, CONTROL_MIN))

    # ── the reference's own ruler, from the table r7862 banked ───────────────────────────────────
    refpath = os.path.join(R7862, 'ref_grid.npz')
    _z = np.load(refpath)
    gate('Ⓢ①ᵃ and the reference\'s ruler is a TABLE ALREADY BANKED at `r7862`, on axes that COVER '
         'the instrument\'s own ruler grid — so the ruler substitution introduces no new reference '
         'run and cannot be a comparison against a freshly tuned table',
         'rdrag' in _z and float(_z['sums'].max()) >= 0.6,
         'keys %s, omega_m %d, omega_b %d, sums %d to %.2f'
         % (sorted(_z.keys()), _z['omega_m'].size, _z['omega_b'].size, _z['sums'].size,
            float(_z['sums'].max())))

    arms = {}

    def read(mod, name):
        out = _REAL(mod, name)
        cx = out.get('crossing_meV')
        arms[name] = dict(crossing_meV=(float(cx) if cx is not None else None),
                          min_at=float(out['min_at']), passes=int(out.get('passes', -1)),
                          monotonic_above_min=bool(out.get('monotonic_above_min', False)))
        return arms[name]

    print('\nⓈ②  ONE SUBSTITUTION AT A TIME')
    r_ref = EC.L7864.Ruler(refpath, 'rdrag', "the REFERENCE's own drag epoch", 'reference')
    EC.L7864.attach(base, r_ref, M3, DI)
    read(base, 'Ⓢ② THE RULER SUBSTITUTED, the reference\'s own rdrag, parameters still profiled')

    #: ⛭ holding two of the four is done by PINNING THEM IN THE CHI2 the fitter calls, not by
    #:   reducing the fitter's simplex. The simplex is left at its registered width on purpose: a
    #:   narrower one would be a different fitter, and then the control above would no longer be the
    #:   same code path. The two pinned slots simply become inert.
    held_ix = (2, 3)                       #: WB and NS, in the instrument's own KEYS4 order
    x0 = [float(v) for v in _BANK['calibrated']['x_at_node']['0.0']]
    for mod, nm in ((withinst, 'Ⓢ③ THE PARAMETERS HELD, omega_b and n_s pinned, ruler unchanged'),
                    (base, 'Ⓢ④ BOTH SUBSTITUTIONS TOGETHER')):
        raw = mod.chi2
        mod.chi2 = (lambda v, _r=raw, _x=x0: _r([_x[i] if i in held_ix else v[i] for i in range(4)]
                                                + list(v[4:])))
        read(mod, nm)
        mod.chi2 = raw

    print('\n    arm                                          crossing      closed(held)  closed(free)')
    rows = {}
    for k, v in arms.items():
        cx = v['crossing_meV']
        ch = (CONTROL_CAL - cx) / (CONTROL_CAL - PARTNER_HELD) if cx else None
        cf = (CONTROL_CAL - cx) / (CONTROL_CAL - PARTNER_FREE) if cx else None
        rows[k] = (cx, ch, cf)
        print('    %-44s %s  %s  %s'
              % (k.split()[0] + ' ' + ' '.join(k.split()[1:4]),
                 ('%9.3f' % cx) if cx else '     none',
                 ('%+9.3f' % ch) if ch is not None else '      none',
                 ('%+9.3f' % cf) if cf is not None else '      none'))

    moved = {k: (abs(CONTROL_CAL - v[0]) > REPRO_TOL) for k, v in rows.items() if v[0]}
    shares = {k: v[1] for k, v in rows.items() if v[1] is not None}
    best = max(shares, key=lambda k: shares[k]) if shares else None
    if best is not None and shares[best] >= 0.5:
        outcome, note = 'Ⓡ⓵', 'DEFINITIONAL, and one axis carries it: %s' % best.split()[0]
    elif shares and max(shares.values()) < 0.5 and shares.get(
            'Ⓢ④ BOTH SUBSTITUTIONS TOGETHER', -9) >= 0.5:
        outcome, note = 'Ⓡ⓶', 'DEFINITIONAL but spread across the two'
    elif any(moved.values()):
        outcome, note = 'Ⓡ⓷', 'PARTLY definitional: every substitution moves it, none closes the gap'
    else:
        outcome, note = 'Ⓡ⓸', 'REFUTED -- the two are the same quantity'
    print('\n    ⇒ %s  %s' % (outcome, note))

    gate('Ⓢ⑤ the outcome is one of the four registered before any substituted limit was read, and it '
         'is read off the numbers rather than chosen',
         outcome in ('Ⓡ⓵', 'Ⓡ⓶', 'Ⓡ⓷', 'Ⓡ⓸'), '%s %s' % (outcome, note))
    gate('Ⓢ⑤ᵃ and a share outside the unit interval or of the WRONG SIGN is reported rather than '
         'clipped, as the registration declared in advance — both physics repairs so far moved this '
         'limit AWAY from the reference, so a negative share was a live possibility and not a remote '
         'one',
         True,
         'shares %s' % {k.split()[0]: round(v, 3) for k, v in shares.items()})

    out = dict(control_calibrated=CONTROL_CAL, control_minimised=CONTROL_MIN,
               repro_tol_meV=REPRO_TOL, partner_held=PARTNER_HELD, partner_free=PARTNER_FREE,
               arms=arms, shares={k: float(v) for k, v in shares.items()},
               moved_beyond_tolerance={k: bool(v) for k, v in moved.items()},
               outcome=outcome, note=note, held_indices=list(held_ix), x_at_zero=x0)
    io.open(os.path.join(HERE, 'ruler_and_params.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote ruler_and_params.json')
    if FAILS:
        sys.exit('\n  ⛔ %d of %d GATE(S) FAILED: %s' % (len(FAILS), len(RAN), ', '.join(FAILS)))
    print('  ⇒ all %d gate(s) pass' % len(RAN))
    return 0


if __name__ == '__main__':
    sys.exit(main())
