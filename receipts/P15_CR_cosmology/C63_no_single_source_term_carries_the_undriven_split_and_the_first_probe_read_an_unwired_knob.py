#!/usr/bin/env python3
r"""
C63 — ** NO SINGLE LINE-OF-SIGHT SOURCE TERM CARRIES PO-13's 23% UNDRIVEN SPLIT.  ** It survives the
removal of the monopole, of the Doppler dipole and of the integrated term, one at a time, never
falling below 23% and reaching 29% when the integrated term is the one removed.  *So the question as
posed --- Psi term, integrated term, or Doppler term --- has the answer NONE OF THE THREE, and what
sets the undriven peak position is common to all three sources.*

** WHAT WAS ASKED.  ** Undriven, this arm's first peak sits at $1.1273$ of the acoustic scale and the
control's at $0.9158$ --- opposite sides of the adiabatic $k r_s = \pi$, with both arms carrying the
same acoustic scale to a part in four hundred and `qscan` returning $Q=1$ on both.  ** The oscillator
is therefore excluded and the split is in the PROJECTION **, which is where this receipt looks.

** THE MEASUREMENT.  ** `ACOUSTIC_two_arm.py`, `NODRIVE=1`, one source term removed at a time.

                                     CR      control   CR/ctrl    split
      all three terms              1.1273    0.9158    1.2309     23.1%
      integrated removed  NOISW=1  1.0477    0.8096    1.2941     29.4%
      Doppler removed    DPSRC=0   1.1008    0.8893    1.2378     23.8%
      monopole removed   SWSRC=0   1.4721    1.1547    1.2749     27.5%

*** => THE SPLIT NEVER COLLAPSES.  Removing any one term leaves 23-29%, and removing the INTEGRATED
term WIDENS it. ***

⌗ ** AND THE "OPPOSITE SIDES OF $k r_s = \pi$" FRAMING IS A PROPERTY OF THE BASELINE, NOT OF THE
SPLIT. **  With the monopole removed BOTH arms sit above $\pi$ --- $1.4721$ and $1.1547$ --- and the
split is still $27.5\%$.  *The ratio is also far steadier than its parts: $1.23$-$1.29$ across
configurations whose individual peak positions move by up to 30%.*

** ⛔⛭ THE FIRST PROBE MEASURED AN UNWIRED KNOB, AND ITS ANSWER WAS CLEAN, TIDY AND FALSE. **
`SWSRC`/`DPSRC` were first put on the `_project` path at the foot of `main()`, which the reported
spectrum does not take.  The matrix came back saying that deleting the MONOPOLE changed the spectrum
not at all, on both arms, to the last digit --- which reads as "the integrated term carries the whole
split", since `NOISW` was then the only switch that moved anything.
  ⇒ *** That is not a null.  A knob that reports NO CHANGE is indistinguishable from a knob that is
    not connected, until it has been shown that it CAN change something. ***  So this receipt
    CALIBRATES before it reads: `SWSRC=0` must move the CR arm's first peak, and it moves it from
    $1.1273$ to $1.4721$.
  ⌗ ** Identical shape to `r4492`, in this same file: "`NOISW` NAMED A TERM IT COULD NOT REACH" --- a
    silent no-op on two of the three paths that produce every reported spectrum. **  The general rule
    both instances teach: *an instrument with more than one path needs every switch wired on every
    path, and section 5.6's rule --- calibrate a detector against a known instance before believing
    its zero --- applies to CONTROL KNOBS and not only to detectors.*

** THE SAMPLING CONTROL, WHICH THE INSTRUMENT ITSELF DEMANDS.  ** The CR arm samples 2.3 points per
Bessel period and the file says in its own voice that this *"is not aliasing --- but it is only not
aliasing if the answer does not depend on it.  Run KCONT=1 to check."*  Run: `KCONT=1` takes the CR
arm from 943 to 1656 modes and 2.3 to 4.0 points per period, and ** every one of the four CR first
peaks is unchanged **: 340, 316, 332, 444.
  ⌗ *Stated as the bound it is rather than as an identity: the reported multipole grid is `LSTEP=8`
    wide, so unchanged peaks bound the sampling shift below one grid step --- $8/301.6 = 2.65\%$ in
    $\ell_1/\ell_A$ --- against a 23% effect.*

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** This is a NEGATIVE result and is not a mechanism. **  It says where the split is NOT.  It does
    not say what sets the undriven peak position, and it does not close PO-13.
  · ** It does not touch the DRIVING. **  `DRC`/`DRE` are driving couplings and are identically zero
    under `NODRIVE=1`, so they cannot carry an undriven effect; the driven question is `r4519`'s and
    is untouched here.
  · ** Only SINGLE removals were run. **  That no one term carries the split does not exclude a
    cancellation between two of them, which is a different measurement and is not made here.
  · ** The next discriminator is named and NOT run: ** the projection kernel rather than the source
    --- the visibility function and the damping scale, which differ between the arms.

** COMPUTES: the undriven first-peak position $\ell_1/\ell_A$ on both arms, under each single
removal of a line-of-sight source term.  *** At the instrument's own default cosmology --- $H_0=73.0$,
$\Omega_m=0.3066$, `LEAFPERT` on, `NODRIVE=1` --- and at `LMAXL=520`, `LSTEP=8`.  The pinned integers
are MULTIPOLE INDICES on that grid, not fitted parameters, and the claim is about the RATIO between
the arms at one shared setting: both arms are run at the same `LMAXL`, `LSTEP` and `NODRIVE`, so a
parameter the sentence citing this might mean differently would move BOTH sides and leave the split
alone. *** **

⌗ ** PREFIX: filed as `C62` and renamed to `C63` at r4558 before pushing. **  `C62` was allocated by
another node and is already on `origin/main`; `check_receipt_prefixes` names the rule --- *the PUSHED
file owns the slot* --- and this is the local half of the collision it was built for, which no amount
of looking at my own directory would have shown.

This receipt runs at `LMAXL=520`, where all eight first peaks reproduce the full-resolution values
EXACTLY (340/316/332/444 and 276/244/268/348 at `LMAXL=1300`); the reduction is a cost measure and
is verified, not assumed.  Written r4558.  Stated for reversal.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
FAILED = []

#: l_1 measured at LMAXL=1300 -- what the reduced run must reproduce.  (arm, env) -> l_1
FULL = {('cr',   ()):                340, ('lcdm', ()):                276,
        ('cr',   (('NOISW', '1'),)): 316, ('lcdm', (('NOISW', '1'),)): 244,
        ('cr',   (('DPSRC', '0'),)): 332, ('lcdm', (('DPSRC', '0'),)): 268,
        ('cr',   (('SWSRC', '0'),)): 444, ('lcdm', (('SWSRC', '0'),)): 348}
L_A = {'cr': 301.6, 'lcdm': 301.4}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def run(arm, env):
    e = dict(os.environ, NODRIVE='1', ARM=arm, LMAXL='520', LSTEP='8')
    e.update(dict(env))
    e['PYTHONPATH'] = os.pathsep.join(
        [os.path.join(ROOT, 'storyboard_receipts'),
         os.path.join(ROOT, 'computations', 'beyond_the_wall'), e.get('PYTHONPATH', '')])
    out = subprocess.run([sys.executable, INST], capture_output=True, text=True,
                         errors='replace', env=e, cwd=os.path.dirname(INST)).stdout
    m = re.search(r'peaks at l = \[(\d+)', out)
    return (int(m.group(1)) if m else None), out


def main():
    print()
    print('  C63 -- which line-of-sight source term carries the 23% undriven split')
    print()

    # ============================================================ (0) the switches are REACHABLE
    print('  ' + '=' * 74)
    print('  PART 0 -- ⛔ THE SWITCHES ARE READ ON THE PATH THAT PRODUCES THE NUMBERS')
    print('  ' + '=' * 74)
    src = open(INST, encoding='utf-8').read()
    # the body of los_spectrum's source(), which is the only path these numbers come from
    i = src.index('def los_spectrum(')
    j = src.index('def ', src.index('def source(', i) + 10)
    body = src[src.index('def source(', i):j]
    for nm in ('_SWSRC', '_ISW', '_DPSRC'):
        check(f'⓪ {nm} is read inside los_spectrum.source() -- not only elsewhere in the file, '
              f'which is exactly how r4492 found NOISW naming a term it could not reach',
              nm in body)

    # ============================================================ (1) and they are CALIBRATED
    print()
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ CALIBRATED BEFORE READ: A SWITCH THAT CANNOT MOVE ANYTHING')
    print('             READS THE SAME AS A TERM THAT DOES NOT MATTER')
    print('  ' + '=' * 74)
    got = {}
    for (arm, env), want in FULL.items():
        l1, out = run(arm, env)
        got[(arm, env)] = l1
        tag = '+'.join(f'{k}={v}' for k, v in env) or 'all three terms'
        check(f'⓵ {arm:<4} {tag:<22} l_1 = {l1} at LMAXL=520, reproducing the LMAXL=1300 value '
              f'{want} EXACTLY -- so the reduction is a cost measure and not a different question',
              l1 == want)
    base_cr, base_lc = got[('cr', ())], got[('lcdm', ())]
    check(f'⓵ᵇ ⛭ SWSRC=0 MOVES the CR arm -- {base_cr} -> {got[("cr", (("SWSRC", "0"),))]} -- so the '
          f'monopole switch demonstrably reaches the term it names, and a null read off it would '
          f'mean something.  ** The first probe of this question put SWSRC on a path the spectrum '
          f'does not take and measured NO change at all. **',
          got[('cr', (('SWSRC', '0'),))] != base_cr)
    check(f'⓵ᶜ and DPSRC=0 moves it too -- {base_cr} -> {got[("cr", (("DPSRC", "0"),))]}',
          got[('cr', (('DPSRC', '0'),))] != base_cr)

    # ============================================================ (2) the split never collapses
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- *** THE SPLIT SURVIVES EVERY SINGLE-TERM REMOVAL ***')
    print('  ' + '=' * 74)
    print(f"    {'configuration':<26} {'CR':>8} {'control':>9} {'CR/ctrl':>9} {'split':>8}")
    splits = {}
    for env, nm in ((), 'all three terms'), ((('NOISW', '1'),), 'integrated removed'), \
                   ((('DPSRC', '0'),), 'Doppler removed'), ((('SWSRC', '0'),), 'monopole removed'):
        rc, rl = got[('cr', env)] / L_A['cr'], got[('lcdm', env)] / L_A['lcdm']
        splits[nm] = rc / rl
        print(f'    {nm:<26} {rc:>8.4f} {rl:>9.4f} {rc/rl:>9.4f} {rc/rl - 1:>7.1%}')
    check(f'⓶ the baseline split is the 23% the row carries: {splits["all three terms"] - 1:.1%}',
          0.225 < splits['all three terms'] - 1 < 0.235)
    check(f'⓶ᵇ *** and NO single removal collapses it -- the smallest surviving split is '
          f'{min(splits.values()) - 1:.1%} *** , so the split is not carried by the monopole, by '
          f'the Doppler dipole or by the integrated term',
          min(splits.values()) - 1 > 0.22)
    check(f'⓶ᶜ removing the INTEGRATED term WIDENS it to {splits["integrated removed"] - 1:.1%}, '
          f'which is the opposite of carrying it',
          splits['integrated removed'] > splits['all three terms'])
    rc_no = got[('cr', (('SWSRC', '0'),))] / L_A['cr']
    rl_no = got[('lcdm', (('SWSRC', '0'),))] / L_A['lcdm']
    check(f'⓶ᵈ ⌗ and "opposite sides of k r_s = pi" is a property of the BASELINE, not of the '
          f'split: with the monopole removed both arms sit ABOVE pi ({rc_no:.4f}, {rl_no:.4f}) and '
          f'the split is still {rc_no/rl_no - 1:.1%}',
          rc_no > 1 and rl_no > 1 and rc_no / rl_no - 1 > 0.22)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f in FAILED:
            print(f'      {f[:110]}')
        return 1
    print('  ⛭ NO SINGLE SOURCE TERM CARRIES THE SPLIT.  The answer to "Psi, integrated, or')
    print('    Doppler" is NONE OF THE THREE, and the next discriminator is the projection')
    print('    kernel -- the visibility function and the damping scale -- not the source.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
