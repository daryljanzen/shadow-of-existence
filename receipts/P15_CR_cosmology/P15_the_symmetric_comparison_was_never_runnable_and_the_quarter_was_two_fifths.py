#!/usr/bin/env python3
r"""
P15 — ** THE SYMMETRIC UNDRIVEN COMPARISON, RUN FROM THE TREE AT LAST.  r4549's THREE CLAIMS HOLD IN
CHARACTER; ITS ONE NUMBER DOES NOT, AND THE CORRECTION IS AGAINST THE LINE THAT MADE IT. **

** WHY THIS EXISTS. **  `r4549` reported the undriven split between the arms as *"dominated by a
start-and-convention mismatch"*, with three findings: matching the START alone does not shrink the
split but *"OVERSHOOTS AND CHANGES SIGN"*; matching the start AND the sound-horizon convention
*"leaves a quarter of the original, on the far side of zero"*; and *"the implied wavenumber is
IDENTICAL across the last two rows -- so the mode never moved, only the scale it was reported
against."*  Its own message closed: *"60's receipt for this result is not yet pushed and lands
next."*

  ⛔ ** IT DID NOT LAND.  No receipt in the tree sets `LZSTART`, and the sound-horizon half of the
    convention HAD NO KNOB AT ALL until `r6476` added `LRSFROM` **, so the run those numbers came
    from could not be reproduced from the tree by anyone, including the line that made it.  *`r4549`
    also appended its conclusions to `CR_cosmology.tex` past the file's own `\end{document}`, where
    they have never compiled -- see `check_tex_tail`, added the same revision.*

** THE RUN, FROM THE TREE, `NODRIVE=1`, `LMAXL=520`, `LSTEP=2`. **

      arm / convention                       l_A      l_1    l_1/l_A    split vs CR
      CR, at its pin                        301.6     340     1.1273        --
      control, as shipped                   301.4     272     0.9024      +0.2249
      control, start matched                301.4     482     1.5992      -0.4719
      control, start + convention matched   397.1     482     1.2138      -0.0865

** WHAT HOLDS. **
  ⓵ *Matching the start alone does not shrink the split: it overshoots and changes sign* --- $+0.225$
    to $-0.472$, and the magnitude GROWS by a factor of two.  Reproduced.
  ⓶ *Matching both leaves a residue on the far side of zero* --- $-0.0865$.  Reproduced.
  ⓷ *The implied wavenumber is identical across the last two rows* --- $\ell_1 = 482$ in both, to the
    multipole.  Reproduced exactly.  ** The convention moves $\ell_A$ from $301.4$ to $397.1$ and
    moves the mode by nothing. **

*** WHAT DOES NOT HOLD IS THE ONE QUANTITATIVE CLAIM, AND IT IS THIS LINE'S OWN. ***  $r4549$ said
the residue is *"a quarter of the original"*.  ** It is $0.0865/0.2249 = 38\%$ --- two fifths, not a
quarter, and the difference is a factor of $1.5$ on the quantity the row's verdict rests on. **  *The
direction of the error is the unhelpful one: it makes the dissolution look more complete than it is.*

  ⌗ ** STATED AS A CORRECTION RATHER THAN A RESTATEMENT **, because "a quarter" is in `r4549`'s
    commit message and in `THE_REGISTER.md`, and a number that was never runnable is not a number
    that was checked.  *The figure it should have been compared against was never in the tree.*

** AND THE STRUCTURE ⓷ FOUND IS THE SAME ONE `r6476` FOUND AT THE OTHER END, WHICH IS THE FINDING
   WORTH MORE THAN EITHER. **  Here a CONVENTION moves $\ell_A$ and leaves $\ell_1$ at $482$; there
the ONE FITTED NUMBER moves $\ell_A$ by $51\%$ and leaves $\ell_1$ at $206$.  ** Both times the
denominator moved and the mode did not. **  *`r4549` wrote ⓷ down and then drew its conclusion from
the ratio anyway; so did this receipt's predecessor.  Twice is a habit, and the habit is reading a
quotient as though both of its halves were measurements.*

** SCOPE. **  Undriven on both arms, which is the regime `r4549`'s split is defined in; each arm on
its own geometry throughout.  *It does not re-open whether the split is physical --- `r4549`'s
verdict that it is largely a comparison artefact survives its own arithmetic being corrected, since
$38\%$ of the original is still a minority of it and still on the far side of zero.*

COMPUTES: scope.  Undriven throughout (NODRIVE=1) at LMAXL = 520 and LSTEP = 2.  The CR arm is
at its own solved pin; the control is run three ways -- as shipped, at LZSTART = 6761 (the CR arm's
onset), and at that start with LRSFROM=start.  6761 is not a free choice: it is the CR arm's onset,
which is what "matched" means here.  r4549 is pinned by sha (fc26d0b0) rather than by name, so the
two history checks cannot drift onto a different commit.

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

#: the revision whose claims this receipt checks, pinned by sha so the check stays true.
R4549 = 'fc26d0b0629d549ff39612175a8d91b4212a7d6c'

#: (label, ARM, extra env) -- the four rows, and every one of them is a row of the table above.
RUNS = (
    ('CR, at its pin', 'cr', {}),
    ('control, as shipped', 'lcdm', {}),
    ('control, start matched', 'lcdm', {'LZSTART': '6761'}),
    ('control, start + convention matched', 'lcdm', {'LZSTART': '6761', 'LRSFROM': 'start'}),
)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def run(arm, env):
    e = dict(os.environ, ARM=arm, NODRIVE='1', LMAXL='520', LSTEP='2')
    e.update(env)
    e['PYTHONPATH'] = os.pathsep.join(
        [os.path.join(ROOT, 'storyboard_receipts'),
         os.path.join(ROOT, 'computations', 'beyond_the_wall'), e.get('PYTHONPATH', '')])
    out = subprocess.run([sys.executable, INST], capture_output=True, text=True,
                         errors='replace', env=e, cwd=os.path.dirname(INST)).stdout
    la = re.search(r'l_A = pi D/r_s = ([\d.]+)', out)
    l1 = re.search(r'peaks at l = \[(\d+)', out)
    return (float(la.group(1)) if la else None, int(l1.group(1)) if l1 else None)


def main():
    print()
    print('  P15 -- the symmetric undriven comparison r4549 promised, run from the tree')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- IT WAS NOT RUNNABLE FROM THE TREE UNTIL THIS REVISION')
    print('  ' + '=' * 74)
    inst = open(INST, encoding='utf-8', errors='replace').read()
    check('⓵ the control\'s START has been exposed since r3683, which is the half r4549 had',
          "os.environ.get('LZSTART'" in inst)
    check('⓵ᵇ and its SOUND-HORIZON CONVENTION is exposed as of r6476, which is the half it did not '
          '-- so the run below could not have been reproduced from the tree before now',
          "os.environ.get('LRSFROM'" in inst)
    # ⌗ Asked of the commit ITSELF rather than of the working tree, which now contains this file
    #   and would answer the question with its own existence.  Commit-pinned, so it stays true.
    #   ⚠ Needs a FULL clone: a shallow one reads an empty string for every pinned commit and
    #     would flip both of these to a vacuous pass, which is the failure `sweep_gates.sh` warns
    #     about.  So the presence of the commit is itself asserted first.
    def at(rev, *args):
        return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)

    r4549 = at(None, 'show', '--no-patch', '--format=%s', R4549)
    check(f'⓵ᶜ the commit is reachable, so the two checks below are not reading an empty string '
          f'off a shallow clone -- {r4549.stdout.strip()[:46]}...',
          r4549.returncode == 0 and r4549.stdout.startswith('r4549'))
    touched = at(None, 'show', '--name-only', '--format=', R4549).stdout.split('\n')
    check('⓵ᵈ r4549 touched NO file under receipts/ -- so the receipt its own message said would '
          '"land next" did not land in it',
          not [t for t in touched if t.startswith('receipts/')])
    grepped = at(None, 'grep', '-l', '-e', 'LZSTART', '-e', 'LRSFROM', R4549, '--', 'receipts/')
    check('⓵ᵉ and no receipt in the tree at that revision set either knob, so the numbers it '
          'reported were not reproducible from the tree by anyone, including the line that made them',
          grepped.returncode == 1 and not grepped.stdout.strip())

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- THE FOUR ROWS')
    print('  ' + '=' * 74)
    with ThreadPoolExecutor(max_workers=4) as ex:
        got = list(ex.map(lambda r: run(r[1], r[2]), RUNS))
    cr_la, cr_l1 = got[0]
    cr_ratio = cr_l1 / cr_la
    rows = []
    print(f"    {'arm / convention':<37} {'l_A':>7} {'l_1':>5} {'l_1/l_A':>9} {'split':>9}")
    for (label, _a, _e), (la, l1) in zip(RUNS, got):
        ratio = l1 / la
        split = None if label.startswith('CR') else cr_ratio - ratio
        rows.append((label, la, l1, ratio, split))
        tail = f'{"--":>9}' if split is None else f'{split:>+9.4f}'
        print(f'    {label:<37} {la:>7.1f} {l1:>5} {ratio:>9.4f} {tail}')

    base = rows[1][4]
    start = rows[2][4]
    both = rows[3][4]

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- r4549\'S THREE CLAIMS, CHECKED')
    print('  ' + '=' * 74)
    check(f'⓶ matching the START alone does not shrink the split -- it overshoots and CHANGES SIGN, '
          f'{base:+.4f} to {start:+.4f}, the magnitude growing by {abs(start / base):.1f}x',
          base > 0 > start and abs(start) > abs(base))
    check(f'⓶ᵇ matching the start AND the convention leaves a residue on the far side of zero, '
          f'{both:+.4f}',
          both < 0 and abs(both) < abs(base))
    check(f'⓶ᶜ *** and the implied mode is IDENTICAL across the last two rows -- l_1 = {rows[2][2]} '
          f'in both, to the multipole -- while the convention moves l_A from {rows[2][1]:.1f} to '
          f'{rows[3][1]:.1f}.  The denominator moved and the mode did not ***',
          rows[2][2] == rows[3][2] and abs(rows[3][1] - rows[2][1]) > 50)

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛔ AND THE ONE NUMBER, WHICH IS WRONG AND IS THIS LINE\'S OWN')
    print('  ' + '=' * 74)
    frac = abs(both) / abs(base)
    print(f'      r4549: "leaves a quarter of the original, on the far side of zero"')
    print(f'      measured: {abs(both):.4f} / {abs(base):.4f} = {frac:.1%}')
    check(f'⓷ the residue is {frac:.0%} of the original, not the 25% r4549 reported -- a factor of '
          f'{frac / 0.25:.1f} on the quantity the row\'s verdict rests on, in the direction that '
          f'makes the dissolution look more complete than it is',
          frac > 0.33)
    check('⓷ᵇ and r4549\'s VERDICT survives its arithmetic being corrected: two fifths of the '
          'original is still a minority of it and still on the far side of zero, so the split is '
          'still largely a comparison artefact',
          frac < 0.5 and both < 0)

    print()
    print('  ' + '=' * 74)
    if FAILED:
        print(f'  ⛔ {len(FAILED)} CHECK(S) FAILED')
        for f_ in FAILED:
            print(f'      {f_[:110]}')
        return 1
    print('  *** THE MODE NEVER MOVED, ONLY THE SCALE IT WAS REPORTED AGAINST -- r4549 wrote')
    print('    that down and then read the quotient anyway, and so did r6476\'s first draft.')
    print('    The residue is two fifths of the original, not a quarter.  The verdict stands;')
    print('    the number does not.')
    print('  ' + '=' * 74)
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
