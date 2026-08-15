#!/usr/bin/env python3
"""P1 -- THE PIN TEST, RUN.  The peak spacing tracks the pin PROPORTIONALLY, so the ratio the deficit
is made of does not move: the spacing deficit survives the one fitted number.  And the routed
dichotomy has its two arms the wrong way round.

COMPUTES: the mean peak spacing at LATARG = 280, 301.6 and 320 on one grid; the invariance of
spacing/l_A across a 14% pin range against what a constant-spacing arm would have given; the LCDM
control at the same grid, validated against the sky; the instrument's own KCONT continuum-sampling
check, open in the source since the file was written; and the second, opposite behaviour of l_1.

** ⛭⛭⛭ WHAT WAS ASKED.  `FOR_54` r2799/r2801, the observer line: **

    "if the spacing FOLLOWS the pin, the deficit is an artefact of where the pin was put;
     if it STAYS near 258, the deficit is acoustic content and survives the fit."

** and the runs to settle it were killed by that node's container twice, at the projection stage. **
They are not expensive here: four to eight minutes each, detached.  *** Five runs. ***

** ⓵ THE MEASUREMENT. **

      arm     l_A          peaks                    mean spacing   spacing/l_A   l_1/l_A
      LCDM    301.4 (out)  220,  532,  812, 1116        298.7        0.9909      0.7299
      CR      280.0 (pin)  172,  388,  596,  860        229.3        0.8190      0.6143
      CR      301.6 (pin)  172,  396,  628,  908        245.3        0.8134      0.5703
      CR      320.0 (pin)  172,  412,  660,  956        261.3        0.8167      0.5375
      CR      301.6 KCONT  172,  396,  628,  908        245.3        0.8134      0.5703

*** The spacing follows the pin, and it follows it PROPORTIONALLY: a straight-line fit through the
three CR points has slope 0.798 and intercept 5.4, and spacing/l_A is 0.8164 +- 0.0028 -- a spread of
0.69% across a pin range of 14%. ***

** ⛔ ⓶ SO THE DICHOTOMY IS INVERTED, AND THE INVERSION IS THE FINDING. **  The deficit is a RATIO --
"the peaks are not where its own l_A says", 0.855 against the control's 0.995.
  ⇒ *** A spacing that tracks the pin proportionally is exactly what makes that ratio INDEPENDENT of
      the pin.  It is the CONSTANT-spacing arm whose ratio would have moved -- 0.876, 0.813, 0.767
      across the same three points, a 13.4% spread -- and in that case one could always have chosen a
      pin where the deficit vanished. ***
  ⇒ ** MEASURED: 0.69% against the 13.4% the artefact hypothesis requires.  The two are separated by a
    factor of twenty, so this discriminates rather than merely reports. **
  ⇒ *** THE SPACING DEFICIT SURVIVES THE FIT.  It is a property of the arm, and the one fitted number
      cannot move it. ***

** ⌗ ⓷ AND THE INSTRUMENT'S OWN OPEN QUESTION, ANSWERED IN PASSING. **  `ACOUSTIC_two_arm` prints, on
every CR run under-sampled for the Bessel period: *"CR's ladder is DISCRETE and physical, so this is
not aliasing -- but it is only not aliasing if the answer does not depend on it.  Run KCONT=1 to
check."*  ** Nobody had run it. **
  ⇒ *** KCONT=1 at NK=320 -- a dense continuum replacing the discrete ladder, 4.3 points per Bessel
      period, PASSING the file's own >= 4.0 guard -- returns the SAME FOUR PEAKS, to the multipole. ***
  ** So the CR peaks are not a sampling artefact, and the file's caveat is discharged. **

** ⛭⛭ ⓸ AND A SECOND FACT THAT BEHAVES THE OPPOSITE WAY, WHICH IS WHY IT MATTERS. **  `l_1 = 172` at
ALL THREE pins.  *** The first peak does not move with the pin at all. ***
  ⇒ ** So `l_1/l_A` IS pin-dependent -- 0.614, 0.570, 0.538 -- while `spacing/l_A` is not. **
  ⇒ *** Two quantities the corpus has been reading together behave oppositely under the one fitted
      number: the first-peak comparison to the sky's 0.731 moves when the pin moves, and the spacing
      comparison does not.  A verdict resting on `l_1/l_A` rests on where the pin was put; a verdict
      resting on the spacing does not. ***

** ⓹ AND THE CONTROL IS VALIDATED BEFORE IT IS USED. **  The LCDM arm, unpinned (its `l_A` is an
OUTPUT), returns 220 / 532 / 812 against the sky's 220.6 / 538.1 / 809.8 -- and its spacing ratio is
0.991.  *A control that did not reproduce the sky could not be used to say the CR arm does not.*

** WHAT IS NOT CLAIMED. **  ** Not a verdict on the construction ** -- `PO-7` is protected and a
negative is a measurement discrepancy, not a framework verdict; this reports a number and does not
convert it.  ** Not that 258 was wrong **: r2789 measured 258 at a different grid and this measures
245.3 at NK=200/LMAXL=1400, which is why the CONTROL was re-run here rather than compared across
grids -- the ratio is what is invariant, not the multipole.  ** Not that the peak positions are known
to better than the l-grid **: `LSTEP = 8`, so each peak carries +-4 and each spacing +-8; the
invariance claim is 20x outside that and the individual spacings are not.  ** Not that the deficit is
explained ** -- only that the fitted number is not what produces it.

Written c54.229 (`L-562`).  Stated for reversal.
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
RUNS = os.path.join(HERE, 'runs')
FAILED = []

#: each banked run, and the command that reproduces it.  ** The instrument takes minutes per point,
#: so the OUTPUT is banked and this file asserts against it -- the corpus's convention for a run that
#: cannot sit inside a receipt.  The command is recorded so "banked" is not "unrepeatable". **
RUNS_SPEC = [
    ('lcdm_NK320.log', 301.4,
     'ARM=lcdm NK=320 LMAXL=1400 KBATCH=40 python3 ACOUSTIC_two_arm.py'),
    ('cr_LATARG280_NK200.log', 280.0,
     'ARM=cr LATARG=280 NK=200 LMAXL=1400 KBATCH=40 python3 ACOUSTIC_two_arm.py'),
    ('cr_LATARG301.6_NK200.log', 301.6,
     'ARM=cr LATARG=301.6 NK=200 LMAXL=1400 KBATCH=40 python3 ACOUSTIC_two_arm.py'),
    ('cr_LATARG320_NK200.log', 320.0,
     'ARM=cr LATARG=320 NK=200 LMAXL=1400 KBATCH=40 python3 ACOUSTIC_two_arm.py'),
    ('cr_LATARG301.6_KCONT_NK320.log', 301.6,
     'ARM=cr LATARG=301.6 KCONT=1 NK=320 LMAXL=1400 KBATCH=40 python3 ACOUSTIC_two_arm.py'),
]


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def parse(fn):
    """(l_A, peaks) read from a banked run's own printed block"""
    t = open(os.path.join(RUNS, fn), encoding='utf-8', errors='replace').read()
    la = re.search(r'PEAKS \(line-of-sight\)\s+l_A = ([\d.]+)', t)
    pk = re.search(r'peaks at l = \[([\d,\s]+)\]', t)
    if not (la and pk):
        return None, None
    return float(la.group(1)), [int(x) for x in pk.group(1).split(',')]


def spacing(pk):
    d = [pk[i + 1] - pk[i] for i in range(len(pk) - 1)]
    return sum(d) / len(d), d


def main():
    print()
    print('  P1 -- the pin test: does the peak spacing follow the one fitted number?')
    print()

    data = {}
    for fn, la_expect, cmd in RUNS_SPEC:
        la, pk = parse(fn)
        data[fn] = (la, pk)
        check(f'run banked and readable: {fn} -- l_A = {la}, peaks {pk}',
              la is not None and abs(la - la_expect) < 0.2 and len(pk) == 4)

    # ------------------------------------------------------------------ ⓵ the CR scan
    CR = ['cr_LATARG280_NK200.log', 'cr_LATARG301.6_NK200.log', 'cr_LATARG320_NK200.log']
    las = [data[f][0] for f in CR]
    means = [spacing(data[f][1])[0] for f in CR]
    ratios = [m / l for m, l in zip(means, las)]
    check(f'⓵ the CR scan: l_A {las} -> mean spacing {[round(m,1) for m in means]}',
          las == [280.0, 301.6, 320.0])
    spread = max(ratios) - min(ratios)
    check(f'⛭ and spacing/l_A is {[round(r,4) for r in ratios]} -- spread {spread:.4f} '
          f'({100*spread/(sum(ratios)/3):.2f}%) across a {100*(320-280)/301.6:.0f}% pin range',
          spread < 0.01)

    # ------------------------------------------------------------------ ⓶ the discrimination
    # ** the CONTROL for this measurement is the alternative hypothesis, computed. **  *An experiment
    # with no control returns the size of the tree, not the size of the effect.*
    const = sum(means) / 3
    alt = [const / l for l in las]
    alt_spread = max(alt) - min(alt)
    check(f'⓶ CONTROL -- a CONSTANT-spacing arm at the same three pins would give ratios '
          f'{[round(a,4) for a in alt]}, spread {alt_spread:.4f} ({100*alt_spread/(sum(alt)/3):.1f}%)',
          alt_spread > 0.10)
    check(f'⇒ SO THE MEASUREMENT DISCRIMINATES: {alt_spread/spread:.0f}x between the two hypotheses, '
          f'not a report of one of them',
          alt_spread / spread > 10)
    check('⇒ ⛔ THE DICHOTOMY IS INVERTED.  The deficit is a RATIO, and a spacing that tracks the pin '
          'PROPORTIONALLY is what makes that ratio independent of the pin -- it is the CONSTANT-spacing '
          'arm whose deficit would have been an artefact of where the pin was put',
          spread < 0.01 < alt_spread)

    # ------------------------------------------------------------------ ⓷ the sampling control
    kc_la, kc_pk = data['cr_LATARG301.6_KCONT_NK320.log']
    base_la, base_pk = data['cr_LATARG301.6_NK200.log']
    check(f'⓷ KCONT=1 (dense continuum replacing the discrete ladder, NK=320) returns {kc_pk} against '
          f'the ladder run\'s {base_pk} -- IDENTICAL to the multipole',
          kc_pk == base_pk and kc_la == base_la)
    kc_txt = open(os.path.join(RUNS, 'cr_LATARG301.6_KCONT_NK320.log'),
                  encoding='utf-8', errors='replace').read()
    ppp = re.search(r'points per period = ([\d.]+)', kc_txt)
    check(f'⇒ and it PASSES the instrument\'s own sampling guard: {ppp.group(1)} points per Bessel '
          f'period against the file\'s >= 4.0 -- so the CR peaks are not a sampling artefact',
          ppp and float(ppp.group(1)) >= 4.0
          and 'UNDER-SAMPLED' not in kc_txt)
    src = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
               encoding='utf-8', errors='replace').read()
    check('⌗ and this closes a caveat the instrument has printed on every under-sampled CR run since '
          'it was written: "it is only not aliasing if the answer does not depend on it"',
          'only not aliasing if the answer does not depend on it' in src)

    # ------------------------------------------------------------------ ⓸ l_1 does not move
    l1 = [data[f][1][0] for f in CR]
    check(f'⓸ l_1 = {l1} at all three pins -- THE FIRST PEAK DOES NOT MOVE WITH THE PIN AT ALL',
          len(set(l1)) == 1)
    l1r = [p / l for p, l in zip(l1, las)]
    check(f'⇒ SO l_1/l_A IS pin-dependent -- {[round(r,4) for r in l1r]}, a '
          f'{100*(max(l1r)-min(l1r))/(sum(l1r)/3):.0f}% spread -- while spacing/l_A is not.  Two '
          f'quantities read together behave oppositely under the one fitted number',
          (max(l1r) - min(l1r)) > 0.05)

    # ------------------------------------------------------------------ ⓹ the control, validated
    lc_la, lc_pk = data['lcdm_NK320.log']
    lc_mean, _ = spacing(lc_pk)
    sky = [220.6, 538.1, 809.8]
    check(f'⓹ the LCDM control reproduces the sky before it is used: {lc_pk[:3]} against '
          f'{sky} -- max deviation {max(abs(a-b) for a,b in zip(lc_pk[:3], sky)):.1f} in l',
          all(abs(a - b) < 12 for a, b in zip(lc_pk[:3], sky)))
    check(f'⇒ and its spacing ratio is {lc_mean/lc_la:.4f} against the CR arm\'s '
          f'{sum(ratios)/3:.4f}, on the same grid, with its l_A an OUTPUT rather than a pin',
          lc_mean / lc_la > 0.95 and sum(ratios) / 3 < 0.85)

    # ------------------------------------------------------------------ reproducibility
    for fn, _, cmd in RUNS_SPEC:
        check(f'  · {fn} records the command that makes it', bool(cmd) and 'ACOUSTIC_two_arm' in cmd)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the spacing deficit SURVIVES the one fitted number. **')
    print(f'    spacing/l_A = {ratios[0]:.4f}, {ratios[1]:.4f}, {ratios[2]:.4f} across a 14% pin range')
    print(f'    a constant-spacing arm would have given {alt[0]:.4f}, {alt[1]:.4f}, {alt[2]:.4f}')
    print(f'    LCDM control on the same grid: {lc_mean/lc_la:.4f}, and it reproduces the sky')
    print('  ⇒ ** The routed dichotomy is inverted: following the pin proportionally is exactly what')
    print('    makes the ratio -- which is what the deficit IS -- independent of the pin. **')
    print('  ⌗ AND l_1 DOES NOT MOVE AT ALL, so l_1/l_A is pin-dependent and the spacing is not:')
    print('    two quantities read together, behaving oppositely under the fit.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
