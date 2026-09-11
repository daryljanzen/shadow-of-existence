#!/usr/bin/env python3
r"""
P15 — ** THE LAST CONVENTION, STRIPPED.  THE INSTRUMENT'S OWN STANDING QUESTION IS ANSWERED, AND THE
ANSWER IS NO: THE FITTED ONSET MOVES THE ACOUSTIC SCALE AND DOES NOT MOVE THE FIRST PEAK. **

** THE QUESTION IS THE INSTRUMENT'S, NOT THIS RECEIPT'S. **  `ACOUSTIC_two_arm.py` says why `LATARG`
was exposed, in its own words: *"Exposing it asks the question the front actually needs: GIVEN that
l_A is fitted, is the peak SPACING deficit --- the only acoustic content left after c54.187 and
c54.188 --- an artefact of where the pin was put?"*  ** It was exposed at `r2441` and the question
was never run.**  The work order at `r6435` asked for the last convention stripped; this is it.

** WHAT WAS MEASURED. **  `z_onset` scanned over a factor of $3.6$, CR arm, converged multipole grid
(`LSTEP=2`, the step $8$ default quantises THIS arm and not the control and P15 says so):

      z_onset     r_s        l_A      l_1     l_1/l_A
       4500     113.30     360.6     210      0.5824
       6761     135.46     301.6     206      0.6830   <- the pin, l_A = LATARG
       8600     146.77     278.4     206      0.7399
      16000     170.70     239.3     208      0.8692
       sky                 301.7     220.6    0.7312

*** => l_A RUNS FROM 360.6 TO 239.3 -- A RANGE OF 51% -- AND l_1 SITS AT 206 TO 210 THROUGHOUT,
    A RANGE OF 2%.  THE ONE FITTED NUMBER MOVES THE DENOMINATOR AND LEAVES THE NUMERATOR WHERE
    IT IS. ***

** SO THE ANSWER TO THE INSTRUMENT'S QUESTION IS NO, AND IT IS THE OPPOSITE OF WHAT THE MOVING RATIO
   SUGGESTS. **  $\ell_1/\ell_A$ does move with the pin --- steeply, monotonically, and it crosses
the sky's $0.7312$ between $z=6761$ and $z=8600$.  *But it moves because $\ell_A=\pi D_M/r_s$ moves
with $r_s$, which is an arithmetic consequence of changing the onset and not a statement about the
spectrum.*  ** The physical deficit --- this arm's first peak at $206$ against the sky's $220.6$,
$-6.6\%$ --- DOES NOT MOVE AT ALL. **  It is onset-invariant across the whole scan.
  ⌗ *That is why the ratio was never an artefact of the pin: the pin cannot reach the quantity the
    deficit lives in.*

** AND THE TRADE IS THEN AN IDENTITY RATHER THAN A COINCIDENCE, WHICH IS WORTH MORE THAN THE TRADE.
** With $\ell_1$ fixed, $\ell_1/\ell_A = \ell_1/\ell_A$ has all its onset dependence in $\ell_A$, so
the fractional miss in the ratio is MINUS the fractional miss in the scale, exactly:
  · pin $\ell_A$ to the measured $301.6$  ->  $\ell_1/\ell_A = 0.6830$ against $0.7312$: $-6.59\%$;
  · pin $\ell_1/\ell_A$ to the sky        ->  $\ell_A = 281.7$ against $301.6$:          $-6.59\%$.
*The two agree to better than a hundredth of a per cent, and they agree BECAUSE $\ell_1$ is the same
$206$ in both --- a single deficit booked against either of two observables, not two deficits.*

** THE SECOND HALF: "BOTH PINNED" IS UNREACHABLE, AND NOT FOR WANT OF A KNOB. **  Solving the
control's onset from `LATARG` the way the CR arm's is solved fails outright --- `brentq` reports
$f(a),f(b)$ of one sign on $[1500,60000]$ --- and the reason is measured rather than guessed.  Under
the SYMMETRIC convention (`LRSFROM=start`, added this revision --- see below) the control's scale
falls monotonically as its start recedes and approaches its floor FROM ABOVE:

      LZSTART      r_s        l_A
       6761      109.70     397.1
      20000      131.74     330.6
      60000      140.13     310.8
      3e7        144.53     301.4    <- as shipped, r_s from a ~ 0
                            301.6    <- LATARG, the target, and it is BELOW the floor

  ⇒ ** So the control has no sound-horizon freedom left to spend: $301.4$ is a limit it reaches by
    integrating to $a\to0$, not a root it can be solved to. **  *The asymmetry is not in the VALUE
    --- both arms land within $0.1\%$ of $\ell_A\approx301.5$ --- it is that one arm SPENDS a fitted
    onset to get there and the other ARRIVES there.*

⛭ ** ONE INSTRUMENT CHANGE WAS NEEDED TO RUN THIS AND IT CLOSES A HALF-BUILT KNOB. **  `r3683`
exposed `LZSTART` to match the two arms' STARTS, *"so the late-start counterfactual can be run
SYMMETRICALLY"*.  It did not match their SOUND-HORIZON CONVENTIONS: the control integrated $r_s$
from $a\sim0$ whatever its start.  ** So every "symmetric" run since was half symmetric, and
`LZSTART` alone moves the control's $\ell_A$ by NOTHING --- $301.4$ at $z=1500$, $3000$, $6761$ and
$3\times10^{7}$ alike, measured. **  `LRSFROM=start` supplies the other half.  *Reachability-checked
at the REPORTING path before use, per the practice that came out of the fifth unwired switch: the
header's own `r_s` and `l_A` were seen to move.*

** AND IT IS NOT THE CUTOFF, WHICH IS THE ONE INSTRUMENT FAULT THAT COULD MANUFACTURE IT. **  The
scan runs at `LMAXL=520` because `LMAXL=1300` costs **1207s a point, measured** ($943$ modes against
$376$, the instrument printing both) against $92$s for a point of the scan.  *Re-run at $1300$ ---
the configuration P15 quotes --- at both ends of the interval that brackets the sky:*

      LMAXL=1300, z = 6761 :  l_A = 301.6   peaks at 206, 518, 828, 1188
      LMAXL=1300, z =10000 :  l_A = 266.6   peaks at 206, 510, 792, 1120

  ⇒ ** $\ell_1 = 206$ at both, so the first peak's onset-invariance survives the cutoff that could
    have faked it. **  ⌗ *And the HIGHER peaks move --- $828\to792$, $1188\to1120$ --- so this is
    specifically a statement about the first peak and NOT the weaker claim that the spectrum is
    insensitive to the onset.  The spacing moves about half as much as $\ell_A$ does; the first peak
    does not move at all.*  Run with `--cutoff`, which is off the default path by cost alone.

** SCOPE, STATED RATHER THAN LEFT TO BE FOUND. **
  · ** Driven, at the instrument's defaults, `LMAXL=520`, `LSTEP=2` **, the configuration in which
    this arm returns P15's own quoted first peak of $206$ --- asserted below, so the scan is
    anchored to the paper rather than run beside it.
  · ** Each arm is run on its OWN geometry throughout **, never $\Lambda$CDM's spectrum with the CR
    arm's damping applied to it --- the trap that burned two prior nodes.
  · ** It does not say the construction is wrong **, and it does not shrink the deficit: it says the
    deficit is $\ell_1=206$ against $220.6$, that no choice of the one fitted number touches it, and
    that $0.6830$ and $-6.6\%$ are two spellings of one number rather than two findings.
  · ** It does not touch the handover codings ** (`r6436`, `r6447`), the other half of this row.

** WHAT THIS WITHDRAWS, AND IT IS THIS LINE'S OWN. **  An earlier draft of this receipt read the
same scan on the step-$8$ grid and concluded *"the deficit MOVES with the pin, so it is not
independent of it"*.  ** That is wrong, and the data contradicting it were already in that draft ---
$\ell_1$ read $204$ at every onset in it and the constancy went unremarked. **  The ratio moves; the
deficit does not.  *Recorded because a framing that survives its own refuting data is worth more as
a caution than as a deletion.*

COMPUTES: scope.  z_onset is SCANNED, not pinned: 4500, 6761, 8600, 16000, with 6761 the
instrument's own solved pin (LATARG = 301.6) and the other three forced through ZSTART.  The control
runs at LZSTART = 6761, 20000, 60000 under LRSFROM=start plus its shipped a~0 floor.  Everything
else is the instrument's default: LMAXL = 520 and LSTEP = 2, the grid on which this arm returns
P15's own quoted l_1 = 206 (step 8, the instrument default, reads 204 -- it quantises THIS arm and
not the control, which P15 states and which the first draft of this receipt was misled by).  The sky
is P15's quoted l_1 = 220.6 and l_1/l_A = 0.7312, so l_A,sky = 220.6/0.7312 is derived and not a
second datum.  `--cutoff` re-runs at LMAXL = 1300 and is not on the default path.

Written r6476.  Stated for reversal.
"""
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
FAILED = []

#: the sky, as P15 quotes it: first peak 220.6, and l_1/l_A = 0.7312 so the scale is 220.6/0.7312.
SKY_L1 = 220.6
SKY_RATIO = 0.7312
SKY_LA = SKY_L1 / SKY_RATIO

#: P15's own quoted first peak for this arm, which this configuration must reproduce before its
#: scan is worth reading.
PAPER_L1 = 206
PIN = 6761

ONSETS = (4500, PIN, 8600, 16000)
STARTS = (6761, 20000, 60000)

#: `--cutoff` only: the same question at the configuration P15 quotes.  MEASURED at 1207s a point
#: standalone (943 modes against the scan's 376), which is why it is opt-in rather than trimmed away.
#: Both ends of the interval that brackets the sky.
CUTOFF_ONSETS = (PIN, 10000)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def run(arm, env):
    e = dict(os.environ, ARM=arm, LMAXL='520', LSTEP='2')
    e.update(env)
    e['PYTHONPATH'] = os.pathsep.join(
        [os.path.join(ROOT, 'storyboard_receipts'),
         os.path.join(ROOT, 'computations', 'beyond_the_wall'), e.get('PYTHONPATH', '')])
    out = subprocess.run([sys.executable, INST], capture_output=True, text=True,
                         errors='replace', env=e, cwd=os.path.dirname(INST)).stdout
    la = re.search(r'l_A = pi D/r_s = ([\d.]+)', out)
    l1 = re.search(r'peaks at l = \[(\d+)', out)
    rs = re.search(r'r_s = ([\d.]+) Mpc', out)
    return (float(la.group(1)) if la else None,
            int(l1.group(1)) if l1 else None,
            float(rs.group(1)) if rs else None)


def cutoff_mode():
    """The scan's one instrument fault re-run at P15's own cutoff.  Opt-in: 1207s a point, measured."""
    print('  --cutoff: is the first peak\'s onset-invariance an artefact of LMAXL = 520?')
    print()
    with ThreadPoolExecutor(max_workers=2) as ex:
        got = dict(zip(CUTOFF_ONSETS, ex.map(
            lambda z: run('cr', {'ZSTART': str(z), 'LMAXL': '1300'}), CUTOFF_ONSETS)))
    for z in CUTOFF_ONSETS:
        print(f'      LMAXL=1300, z = {z:>5} :  l_A = {got[z][0]:.1f}   l_1 = {got[z][1]}')
    l1s = {got[z][1] for z in CUTOFF_ONSETS}
    check(f'⓹ l_1 is the same at both ends at the paper\'s own cutoff ({sorted(l1s)}), while l_A '
          f'moves from {got[PIN][0]:.1f} to {got[10000][0]:.1f} -- so the invariance is not made by '
          f'the reduced cutoff the scan runs at',
          len(l1s) == 1)
    check(f'⓹ᵇ and the reduced cutoff agrees with it at the pin, which is what licenses the scan',
          got[PIN][1] == PAPER_L1)
    print()
    return 1 if FAILED else 0


def main():
    print()
    print('  P15 -- the last convention: the fitted number moves the scale, not the peak')
    print()
    if '--cutoff' in sys.argv:
        return cutoff_mode()

    print('  ' + '=' * 74)
    print('  PART 1 -- THE QUESTION IS THE INSTRUMENT\'S OWN, AND SO IS THE PIN')
    print('  ' + '=' * 74)
    inst = open(INST, encoding='utf-8', errors='replace').read()
    p15 = ' '.join(open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                        encoding='utf-8', errors='replace').read().split())
    check('⓵ the instrument solves z_onset by brentq so that l_A hits LATARG rather than letting it '
          'come out as an output',
          'brentq(lambda z: np.pi * D_M / rs_from(z) - _latarg' in inst)
    check('⓵ᵇ and it states the standing question in its own comment -- "GIVEN that l_A is fitted, '
          'is the peak SPACING deficit ... an artefact of where the pin was put?"',
          'an artefact of where the pin was put?' in ' '.join(inst.split()))
    check('⓵ᶜ and P15 states the fit in its own voice, calling z_onset the one fitted number',
          'the one fitted number' in p15)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- THE SCAN, ON THE GRID THAT REPRODUCES P15\'S OWN QUOTED PEAK')
    print('  ' + '=' * 74)
    with ThreadPoolExecutor(max_workers=4) as ex:
        cr = dict(zip(ONSETS, ex.map(lambda z: run('cr', {'ZSTART': str(z)}), ONSETS)))
    print(f"    {'z_onset':>8} {'r_s':>8} {'l_A':>8} {'l_1':>5} {'l_1/l_A':>9}")
    for z in ONSETS:
        la, l1, rs = cr[z]
        print(f'    {z:>8} {rs:>8.2f} {la:>8.1f} {l1:>5} {l1 / la:>9.4f}')
    print(f"    {'sky':>8} {'':>8} {SKY_LA:>8.1f} {SKY_L1:>5} {SKY_RATIO:>9.4f}")

    check(f'⓶ at the pin this configuration returns l_1 = {cr[PIN][1]}, which is P15\'s own quoted '
          f'{PAPER_L1} -- so the scan is anchored to the paper and not run beside it',
          cr[PIN][1] == PAPER_L1)
    las = [cr[z][0] for z in ONSETS]
    l1s = [cr[z][1] for z in ONSETS]
    spread_la = max(las) / min(las) - 1
    spread_l1 = max(l1s) / min(l1s) - 1
    check(f'⓶ᵇ *** the acoustic scale moves {spread_la:.0%} across the scan ({max(las):.1f} down to '
          f'{min(las):.1f}) while the first peak moves {spread_l1:.0%} ({min(l1s)} to {max(l1s)}) '
          f'-- the fitted number moves the denominator and leaves the numerator ***',
          spread_la > 0.4 and spread_l1 < 0.05)
    check('⓶ᶜ and l_A falls monotonically with the onset, which is the arithmetic of r_s and not a '
          'fact about the spectrum',
          all(cr[a][0] > cr[b][0] for a, b in zip(ONSETS, ONSETS[1:])))

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭ SO THE DEFICIT IS ONSET-INVARIANT, AND THE TRADE IS AN IDENTITY')
    print('  ' + '=' * 74)
    misses = {z: cr[z][1] / SKY_L1 - 1 for z in ONSETS}
    for z in ONSETS:
        print(f'      z = {z:>5}:  l_1 = {cr[z][1]} against the sky\'s {SKY_L1}   '
              f'{misses[z]:+.2%}')
    check(f'⓷ *** the first peak misses the sky by {misses[PIN]:+.1%} at the pin and by between '
          f'{min(misses.values()):+.1%} and {max(misses.values()):+.1%} across a factor of '
          f'{max(ONSETS) / min(ONSETS):.1f} in the onset -- the deficit does not move with the pin, '
          f'so it is not an artefact of where the pin was put ***',
          all(m < -0.04 for m in misses.values())
          and max(misses.values()) - min(misses.values()) < 0.03)

    r_pin = cr[PIN][1] / cr[PIN][0]
    la_needed = cr[PIN][1] / SKY_RATIO
    miss_ratio = r_pin / SKY_RATIO - 1
    miss_scale = la_needed / cr[PIN][0] - 1
    print()
    print(f'      pin l_A = {cr[PIN][0]:.1f} (measured)  ->  l_1/l_A = {r_pin:.4f} vs sky '
          f'{SKY_RATIO}    {miss_ratio:+.2%}')
    print(f'      pin l_1/l_A to the sky          ->  l_A = {la_needed:.1f} vs measured '
          f'{cr[PIN][0]:.1f}   {miss_scale:+.2%}')
    check(f'⓷ᵇ the two misses are the SAME number to '
          f'{abs(abs(miss_ratio) - abs(miss_scale)):.4%} -- not nearly symmetric by luck but equal '
          f'by identity, because l_1 is the same {cr[PIN][1]} in both: one deficit booked against '
          f'either of two observables, not two deficits',
          abs(abs(miss_ratio) - abs(miss_scale)) < 1e-3)
    check(f'⓷ᶜ and the ratio DOES move with the pin and crosses the sky -- {r_pin:.4f} at the pin, '
          f'{cr[8600][1] / cr[8600][0]:.4f} at z = 8600 -- so reading the ratio alone gives the '
          f'opposite answer to reading l_1, which is why this had to be run rather than argued',
          r_pin < SKY_RATIO < cr[8600][1] / cr[8600][0])

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- "BOTH PINNED" IS UNREACHABLE: THE CONTROL HAS NO FREEDOM LEFT TO SPEND')
    print('  ' + '=' * 74)
    check('⓸ the symmetric sound-horizon convention exists in the instrument and is off by default, '
          'so nothing already measured moves',
          "_rsfrom = os.environ.get('LRSFROM', 'zero')" in inst
          and "rs_from(Z_START) if _rsfrom == 'start' else rs_from(1e8)" in inst)
    with ThreadPoolExecutor(max_workers=4) as ex:
        sym = dict(zip(STARTS, ex.map(
            lambda z: run('lcdm', {'LZSTART': str(z), 'LRSFROM': 'start', 'NOPROJ': '1'}), STARTS)))
    floor = run('lcdm', {'NOPROJ': '1'})
    print(f"    {'LZSTART':>10} {'r_s':>8} {'l_A':>8}")
    for z in STARTS:
        print(f'    {z:>10} {sym[z][2]:>8.2f} {sym[z][0]:>8.1f}')
    print(f"    {'3e7 (ship)':>10} {floor[2]:>8.2f} {floor[0]:>8.1f}   <- the floor, r_s from a ~ 0")
    print(f"    {'LATARG':>10} {'':>8} {301.6:>8.1f}   <- the target, BELOW the floor")
    check('⓸ᵇ the control\'s scale falls monotonically as its start recedes and approaches its floor '
          'FROM ABOVE, never crossing LATARG',
          all(sym[a][0] > sym[b][0] for a, b in zip(STARTS, STARTS[1:]))
          and sym[STARTS[-1]][0] > floor[0] and floor[0] < 301.6)
    check(f'⓸ᶜ *** so "both pinned" is not a run that was skipped: the target {301.6} lies below the '
          f'control\'s floor of {floor[0]:.1f}, which is why brentq reports endpoints of one sign. '
          f'The control ARRIVES at the scale the CR arm SPENDS its one fitted number to reach ***',
          floor[0] < 301.6 and abs(floor[0] - 301.6) / 301.6 < 0.01)
    check('⓸ᵈ and without the convention the half-symmetric run moves nothing: LZSTART alone leaves '
          'the control\'s r_s at its a ~ 0 value by construction, the branch being unreachable',
          'R_S = rs_from(Z_START) if _rsfrom' in inst)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** THE PIN CANNOT REACH THE DEFICIT.  The one fitted number moves l_A by 51% across')
    print('    the scan and l_1 by 2%, so the first peak sits at 206 against the sky\'s 220.6')
    print('    whatever the onset is.  0.6830 and -6.6% are two spellings of that one number.')
    print('    "Both pinned" is unreachable because the control\'s scale is a limit, not a root.')
    print('    ⌗ Each arm on its own geometry throughout.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
