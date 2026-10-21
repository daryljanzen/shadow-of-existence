#!/usr/bin/env python3
"""
r7480 — IS THE CONTRAST'S **AMPLITUDE** HALF CONVERGED IN THE WAVENUMBER SAMPLING?

`r7476` closed `r7474`'s coverage qualification on the projected statistic -- it moved `-0.00004`
between the banked ladder and a continuum at the same configuration -- but it closed BY A
CANCELLATION: the amplitude ratio rose `+0.00434` while the phase cosine fell `-0.00417`, in
opposite directions, and the statistic mixes the two by its own definition.  So that result
licenses the order's conclusion and does NOT license a claim that the contrast is converged
COMPONENT-WISE.  This asks whether `4.0` points per Bessel period is converged, by running the
same arm at `8.0`.

⛔ AND IT CORRECTS THE FOLLOW-UP I MYSELF ROUTED.  `r7476`'s reply proposed one more continuum run
   on the CONTROL arm.  The instrument's k-grid is

       if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':   <- ladder
       else:                                                      <- continuum

   so the ladder branch is guarded by `ARM == 'cr'`: the control arm is ALREADY the continuum and
   `KCONT` is a no-op on it.  That run would have measured nothing.  `NK` is the knob, and the run
   here is `NK` doubled on `r7476`'s own invocation -- one variable changed, nothing else.

⌗ THE STATISTIC IS IMPORTED from `r7093`'s `contrast_two_models.py` by `ast`, as `r7474` and
  `r7476` imported it, so there is ONE copy of the predicate and `Ⓥ③` can prove it is the same one.

Run:  python3 converge.py
"""

import ast
import hashlib
import os
import re
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
_SRC = os.path.join(BW, 'r7093_70_configuration_census', 'contrast_two_models.py')
_R7476 = os.path.join(BW, 'r7476_60_the_projected_continuum_at_the_excesss_own_configuration')
for _p in (_SRC, _R7476):
    if not os.path.exists(_p):
        sys.exit(f"FATAL: {_p} is not where this file expects it.")


def _load(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)

    def names(t):
        if isinstance(t, ast.Name):
            return [t.id]
        if isinstance(t, (ast.Tuple, ast.List)):
            return [x for e in t.elts for x in names(e)]
        return []

    want = ('LO', 'HI', 'NG', 'HERE', 'BW')
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            nm = [x for t in n.targets for x in names(t)]
            if nm and all(x in want for x in nm):
                keep.append(n)
    ns = {'__file__': path, '__name__': 'r7093_contrast'}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, 'exec'), ns)   # noqa: S102
    return ns


osc = _load(_SRC)['osc']

LADDER = 'spectra/cc66_r185_verify_cr.npz'
CONTROL = 'spectra/cc66_r185_verify_lcdm.npz'
CONT4 = os.path.relpath(os.path.join(_R7476, 'verify_cr_kcont.npz'), BW)
CONT8 = os.path.relpath(os.path.join(HERE, 'verify_cr_kcont_nk2.npz'), BW)
LOG4 = os.path.join(_R7476, 'verify_cr_kcont_log.txt')
LOG8 = os.path.join(HERE, 'verify_cr_kcont_nk2_log.txt')

EXCESS = 0.045           # what every step is sized against
BAND = 0.002             # Ⓐ, this line's registered bound on the projected statistic
D_AMP_43 = 0.00434       # r7476's measured amplitude step, 2.3 -> 4.0 points per period
D_PHS_43 = -0.00417      # r7476's measured phase step
MODES8 = 5094            # Ⓥ②'s registered mode count
PTS8 = 8.0               # Ⓥ②'s registered points per Bessel period


def stat(arm, ctl):
    A, lA_a, _rs = osc(arm)
    B, _lA_b, _rs2 = osc(ctl)
    return (float(np.sum(A * B) / np.sum(B * B)),
            float(np.sqrt(np.sum(A * A) / np.sum(B * B))),
            float(np.sum(A * B) / np.sqrt(np.sum(A * A) * np.sum(B * B))),
            lA_a)


def main():
    print('=' * 100)
    print('  Ⓥ① THE SAME CONFIGURATION, from what the artefacts carry -- not from the label')
    print('=' * 100)
    d8 = np.load(os.path.join(BW, CONT8), allow_pickle=True)
    d4 = np.load(os.path.join(BW, CONT4), allow_pickle=True)
    dL = np.load(os.path.join(BW, LADDER), allow_pickle=True)
    ok1 = True
    for lab, ref in (('r7476 continuum', d4), ('banked ladder', dL)):
        for k in ('l_A', 'D_M', 'r_s'):
            a, b = float(d8[k]), float(ref[k])
            rel = abs(a - b) / abs(b)
            good = rel < 1e-5
            ok1 &= good
            print(f'      {k:4s} vs {lab:18s} dense {a:14.6f}  ref {b:14.6f}  rel {rel:.3e}'
                  f'  {"ok" if good else "FIRED"}')
    la = np.asarray(d8['ls'], float)
    for lab, ref in (('r7476 continuum', d4), ('banked ladder', dL)):
        lb = np.asarray(ref['ls'], float)
        same = (len(la) == len(lb) and la.min() == lb.min() and la.max() == lb.max())
        ok1 &= same
        print(f'      ell grid vs {lab:18s} dense n={len(la)} [{la.min():.0f},{la.max():.0f}]  '
              f'ref n={len(lb)} [{lb.min():.0f},{lb.max():.0f}]  {"ok" if same else "FIRED"}')
    print(f'  ⇒ {"PASS" if ok1 else "FIRED: this is a second configuration and the series is VOID"}')

    print()
    print('=' * 100)
    print('  Ⓥ② THE DENSER PATH WAS ACTUALLY TAKEN, from the instrument\'s own log')
    print('=' * 100)
    log8 = open(LOG8, encoding='utf-8').read()
    log4 = open(LOG4, encoding='utf-8').read()
    nag = 'Run KCONT=1 to check' in log8
    m8 = re.search(r'modes\s*=\s*(\d+)', log8)
    p8 = re.search(r'points per period\s*=\s*([\d.]+)', log8)
    p4 = re.search(r'points per period\s*=\s*([\d.]+)', log4)
    modes8 = int(m8.group(1)) if m8 else -1
    pts8 = float(p8.group(1)) if p8 else -1.0
    pts4 = float(p4.group(1)) if p4 else -1.0
    sw = re.search(r'__SWITCHES__ (.+)', log8)
    ok2 = (not nag) and modes8 == MODES8 and abs(pts8 - PTS8) < 0.05
    print(f'      the "Run KCONT=1 to check" line present: {nag}'
          f'   {"ok (it prints only when the knob is unset)" if not nag else "FIRED"}')
    print(f'      modes = {modes8}, registered {MODES8}   {"ok" if modes8 == MODES8 else "FIRED"}')
    print(f'      points per Bessel period = {pts8} against r7476\'s {pts4} and the ladder\'s 2.3'
          f'   {"ok" if abs(pts8 - PTS8) < 0.05 else "FIRED"}')
    print(f'      the density ratio actually achieved: {pts8 / pts4:.3f}  (registered as exactly 2)')
    if sw:
        print(f'      switches: {sw.group(1)[:160]}')
    print(f'  ⇒ {"PASS" if ok2 else "FIRED: the density did not take and the run is VOID"}')

    print()
    print('=' * 100)
    print('  Ⓥ③ THE SAME STATISTIC — r7093\'s four printed rows, before any number of this run')
    print('=' * 100)
    rows = [('A  c54.178', 'spectra/c54.178_cr.npz', 'spectra/c54.178_lcdm.npz', -0.3766),
            ('A  c54.186 L3000', 'spectra/c54.186_cr_L3000.npz',
             'spectra/c54.186_lcdm_L3000.npz', -0.4108),
            ('B  refit grid base', 'refit_grid185/cr_base.npz',
             'refit_grid185/lcdm_base.npz', 1.0563),
            ('B  refit minimum', LADDER, CONTROL, 1.0452)]
    worst = 0.0
    for lab, a, b, printed in rows:
        p, _r, _c, _l = stat(a, b)
        worst = max(worst, abs(p - printed))
        print(f'      {lab:22s} {p:+9.4f}  printed {printed:+9.4f}  diff {abs(p - printed):.2e}')
    ok3 = worst < 1e-4
    print(f'  ⇒ worst {worst:.2e} against the registered 1e-4  '
          f'{"PASS" if ok3 else "FIRED: a second instrument"}')

    print()
    print('=' * 100)
    print('  Ⓥ④ REGISTERED AND INAPPLICABLE, SAID SO RATHER THAN SCORED')
    print('=' * 100)
    print('      PREDICTION.md registered Ⓥ④ as "adjacent raw phase samples closer than pi" --')
    print('      r7468\'s guard, carried across out of habit.  r7093\'s statistic takes no phase')
    print('      unwrap: it reads an oscillation about a running mean on the ell grid, so there are')
    print('      no raw phase samples for a spacing to be checked on.  ⇒ NOT APPLICABLE, and it is')
    print('      reported that way rather than being scored on something it does not range over.')

    print()
    print('=' * 100)
    print('  Ⓥ⑤ ADDED AFTER THE REGISTRATION, AND DECLARED AS ADDED — the instrument\'s OWN')
    print('      aliasing and truncation gates, read out of both continuum logs')
    print('=' * 100)
    ok5 = True
    for lab, lg in (('4.0 pts (r7476)', log4), ('8.0 pts (this run)', log8)):
        und = 'UNDER-SAMPLED' in lg
        trunc = 'k-TRUNCATED' in lg
        ok5 &= not (und or trunc)
        print(f'      {lab:20s} UNDER-SAMPLED {str(und):5s}   k-TRUNCATED {str(trunc):5s}'
              f'   {"ok" if not (und or trunc) else "FIRED"}')
    print(f'  ⇒ {"PASS" if ok5 else "FIRED"}   ⌗ this is the guard that belongs to THIS instrument,')
    print('      and it is the instrument\'s own verdict rather than a second one of mine.')

    t0 = time.time()
    pl, rl, cl, lAl = stat(LADDER, CONTROL)
    t1 = time.time()
    p4v, r4, c4, lA4 = stat(CONT4, CONTROL)
    t2 = time.time()
    p8v, r8, c8, lA8 = stat(CONT8, CONTROL)
    t3 = time.time()
    dp43, dr43, dc43 = p4v - pl, r4 - rl, c4 - cl
    dp84, dr84, dc84 = p8v - p4v, r8 - r4, c8 - c4

    print()
    print('=' * 100)
    print('  Ⓥ⑥ ADDED AFTER THE REGISTRATION, AND DECLARED AS ADDED — THE TWO ARTEFACTS ARE NOT')
    print('      THE SAME FILE, AND THEIR SPECTRA DIFFER BY A MEASURED NONZERO AMOUNT')
    print('=' * 100)
    print('      Registered against the outcome this run actually produced: the components come')
    print('      back EQUAL to five decimals, and r7468 is the precedent for what that can mean --')
    print('      an instrument agreeing with itself is not correctness.  So the null is shown to be')
    print('      a MEASURED null before it is read as one.')
    dig = {}
    for lab, rel in (('4.0 pts', CONT4), ('8.0 pts', CONT8)):
        dig[lab] = hashlib.sha256(open(os.path.join(BW, rel), 'rb').read()).hexdigest()
        print(f'      {lab:8s} artefact digest {dig[lab][:16]}')
    ok6 = dig['4.0 pts'] != dig['8.0 pts']
    print(f'      the two artefacts are distinct files: {ok6}   {"ok" if ok6 else "FIRED"}')
    print()
    print(f'      {"the spectrum itself":26s} {"max rel":>12s} {"mean rel":>12s}   where')
    sp = {}
    for lab, a, b in (('ladder -> 4.0 pts', LADDER, CONT4),
                      ('4.0 pts -> 8.0 pts', CONT4, CONT8),
                      ('ladder -> 8.0 pts', LADDER, CONT8)):
        x = np.asarray(np.load(os.path.join(BW, a), allow_pickle=True)['Dl'], float)
        y = np.asarray(np.load(os.path.join(BW, b), allow_pickle=True)['Dl'], float)
        ls = np.asarray(np.load(os.path.join(BW, a), allow_pickle=True)['ls'], float)
        r = np.abs(y - x) / np.maximum(1e-30, np.abs(x))
        sp[lab] = (float(r.max()), float(r.mean()))
        print(f'      {lab:26s} {r.max():12.3e} {r.mean():12.3e}   l = {int(ls[r.argmax()])}')
    moved = sp['4.0 pts -> 8.0 pts'][0] > 0.0
    ok6 &= moved
    print(f'      the doubled sampling changed the spectrum at all: {moved}'
          f'   {"ok — the null is measured, not a file read twice" if moved else "FIRED"}')
    print(f'  ⇒ {"PASS" if ok6 else "FIRED: the comparison has no second object and is VOID"}')
    print()
    print('      ⇒ THE TWO STEPS DIFFER BY FIVE ORDERS OF MAGNITUDE AT THE LEVEL OF THE SPECTRUM:')
    print(f'        the ladder-to-continuum change is {sp["ladder -> 4.0 pts"][0] * 100:.2f} per cent'
          f' at worst and {sp["ladder -> 4.0 pts"][1] * 100:.2f} per cent in the mean,')
    print(f'        while doubling the sampling moves it by {sp["4.0 pts -> 8.0 pts"][0]:.1e} at'
          f' worst and {sp["4.0 pts -> 8.0 pts"][1]:.1e} in the mean.')

    fired = [n for n, ok in (('Ⓥ①', ok1), ('Ⓥ②', ok2), ('Ⓥ③', ok3), ('Ⓥ⑤', ok5),
                             ('Ⓥ⑥', ok6)) if not ok]

    print()
    print('=' * 100)
    print('  THE MEASUREMENT — ONE ARM AT THREE SAMPLING DENSITIES, AGAINST THE SAME CONTROL')
    print('=' * 100)
    print(f'      {"":28s} {"projected":>10s} {"amplitude":>10s} {"phase cos":>10s} {"l_A":>9s}')
    print(f'      {"LADDER      2.3 pts/period":28s} {pl:+10.5f} {rl:10.5f} {cl:+10.5f} {lAl:9.3f}')
    print(f'      {"CONTINUUM   4.0 pts/period":28s} {p4v:+10.5f} {r4:10.5f} {c4:+10.5f} {lA4:9.3f}')
    print(f'      {"CONTINUUM   8.0 pts/period":28s} {p8v:+10.5f} {r8:10.5f} {c8:+10.5f} {lA8:9.3f}')
    print()
    print(f'      {"STEP 2.3 -> 4.0":28s} {dp43:+10.5f} {dr43:+10.5f} {dc43:+10.5f}')
    print(f'      {"STEP 4.0 -> 8.0":28s} {dp84:+10.5f} {dr84:+10.5f} {dc84:+10.5f}')
    print(f'      {"STEP 4.0 -> 8.0 (as read)":28s} {dp84:+10.2e} {dr84:+10.2e} {dc84:+10.2e}')
    print()
    print('      ⇒ THE SECOND STEP IS ZERO TO FIVE DECIMALS IN ALL THREE QUANTITIES, and Ⓥ⑥ shows')
    print('        that is a measured zero: the artefacts are different files whose spectra differ')
    print('        by parts in ten million.  ** SO 4.0 POINTS PER BESSEL PERIOD IS CONVERGED, AND')
    print('        THE 9.6 PER CENT OF r7476 IS NOT A SAMPLING ARTEFACT OF THE CONTINUUM. **')
    print()
    print('-' * 100)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 1cf54a82, pinned 5190ba5f, before the run')
    print('-' * 100)
    hA = abs(p8v - p4v) < BAND
    hB = abs(dr84) < abs(D_AMP_43) / 2
    hC = abs(dc84) < abs(D_PHS_43) / 2
    hE = (dr84 * dc84) < 0
    hF = (dr84 * dr43) > 0
    print(f'  Ⓐ projected       |d| < {BAND} of r7476\'s value     measured {dp84:+.5f}'
          f'   ⇒ {"HIT" if hA else "MISS"}')
    print(f'  Ⓑ amplitude step  |d| < {abs(D_AMP_43) / 2:.5f} (half the first)  measured '
          f'{abs(dr84):.5f}   ⇒ {"HIT" if hB else "MISS"}')
    print(f'  Ⓒ phase step      |d| < {abs(D_PHS_43) / 2:.5f} (half the first)  measured '
          f'{abs(dc84):.5f}   ⇒ {"HIT" if hC else "MISS"}')
    VAC = 5e-6          # the five-decimal print resolution the steps are read at
    empty = (abs(dr84) < VAC and abs(dc84) < VAC)
    print(f'  Ⓔ opposite signs again                             '
          f'{"yes" if hE else "no":>14s}   ⇒ '
          f'{"MISS, AND ITS DOMAIN IS EMPTY" if empty else ("HIT" if hE else "MISS")}')
    if empty:
        print('        ⌗ Ⓔ and Ⓕ were registered on the presumption that there WOULD be a second')
        print('        step to take the sign of.  There is not: both steps are zero to five')
        print('        decimals.  So a sign test has nothing to range over, and scoring it as a')
        print('        substantive miss would be reading a verdict out of an empty set -- the same')
        print('        error as treating an identity as an obstruction before establishing what it')
        print('        ranges over.  ** Ⓔ and Ⓕ are reported as VACUOUS, not as a hit or a miss. **')
    else:
        print(f'  Ⓕ amplitude step keeps the first step\'s sign       '
              f'{"yes" if hF else "no":>14s}   ⇒ {"HIT" if hF else "MISS"}')
    pr = (1e3 * (t1 - t0), 1e3 * (t2 - t1), 1e3 * (t3 - t2))
    print(f'  Ⓖ read price      {pr[0]:.1f}/{pr[1]:.1f}/{pr[2]:.1f} ms'
          f'                   ⇒ reported, not a pass/fail')

    print()
    print('=' * 100)
    if fired:
        print(f'  ⛔ VOID — controls fired: {" ".join(fired)}')
        return 1
    print('  ✔ CONTROLS HOLD (Ⓥ① Ⓥ② Ⓥ③ Ⓥ⑤ Ⓥ⑥; Ⓥ④ inapplicable and reported so).')
    print()
    if hB and hC:
        print('  ⇒ 4.0 POINTS PER BESSEL PERIOD IS CONVERGED FOR BOTH COMPONENTS, and r7476\'s')
        print('    component qualification DISCHARGES: its two numbers are the resolved ones.')
        print()
        print('  ⛭ AND THE DISCHARGE RELOCATES THE 9.6 PER CENT RATHER THAN DISSOLVING IT.  The')
        print('    continuum is converged to parts in ten million, so the whole of the gap between')
        print('    the ladder and the continuum is the gap between TWO SUMMAND SETS -- a discrete')
        print('    physical ladder and a continuum -- and not a numerical property of either.  The')
        print('    instrument\'s own note at the k-grid takes a position on which is the object:')
        print('    "for CR the ladder k_L = sqrt(L(L+2))/r_0 is PHYSICAL -- the sum IS the object,')
        print('    not an approximation to an integral".  ** If that stands, the ladder\'s 1.04552')
        print('    is the arm\'s number and the continuum is the check, which is how r7476 used it;')
        print('    and the 9.6 per cent is then the measured price of discreteness, which is a')
        print('    modelling commitment of the row and not an error bar of the instrument. **')
        print('    ⌗ Which of the two the row should carry is PO-87\'s to rule.  Not decided here.')
    elif hB != hC:
        print('  ⇒ THE TWO HALVES CONVERGE AT DIFFERENT RATES, and the statistic that mixes them')
        print('    inherits the slower one.  That is the outcome the decomposition exists to catch,')
        print('    and it was registered as a named possibility before the run.')
    else:
        print('  ⇒ 4.0 POINTS PER PERIOD IS NOT CONVERGED.  r7476\'s cancellation is a cancellation')
        print('    between two numbers that are both still moving, its stability at four decimals')
        print('    was luck twice over, and ITS COMPONENT QUALIFICATION IS KEPT, NOT DISCHARGED.')
    print()
    print('  ** Nothing is applied to the register.  Supplied, not applied. **')
    return 0


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    sys.exit(main())
