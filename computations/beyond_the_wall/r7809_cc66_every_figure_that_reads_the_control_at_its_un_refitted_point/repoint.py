#!/usr/bin/env python3
"""r7809/r7811 item ② -- WHICH PRINTED FIGURES MOVE WHEN THE CONTROL IS RE-POINTED, measured.

** THE METHOD, AND WHY IT IS A MEASUREMENT AND NOT AN ESTIMATE. **  A receipt is run TWICE: once as
the tree stands, and once with `numpy.load` redirected so that every read of a control bank at the
un-refitted point returns the re-pointed bank instead.  The two stdouts are then diffed number by
number.  So a figure is on the list because it MOVED, not because a census inferred that it might.

⛔ ** THE SWAP IS A RESTRICTION AND NEVER AN INTERPOLATION. **  It is allowed only between banks whose
`ls` arrays are IDENTICAL, asserted here before anything runs.  `refit_grid185/lcdm_base.npz` and
`r7807_control_planck2018_L2000.npz` are both 238 samples of `100..1996` step 8 -- the same grid, so
the substitution changes the POINT and nothing else.  `spectra/cc66_lcdm_L2000.npz` is step 2 (950
samples) and has NO step-2 counterpart banked yet, so this harness REFUSES it rather than
interpolating: that half is reported as blocked, which is `r7809+cc66.1`'s finding.

⛔ ** AND A RECEIPT GOING RED UNDER THE SWAP IS THE EXPECTED OUTCOME, NOT A FAILURE OF THIS HARNESS. **
Every such receipt pins its figures, so moving the control must redden it.  The exit code is
therefore IGNORED and the stdout is what is read -- stated here so that a red is never mistaken for
evidence that nothing moved.

Run: python3 repoint.py [receipt-name ...]
"""
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')

#: old bank -> re-pointed bank.  Only grid-identical pairs may appear here.
SWAP = {
    os.path.join(BW, 'refit_grid185', 'lcdm_base.npz'):
        os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz'),
    os.path.join(BW, 'r7093_directions', 'grid_oneclock', 'lcdm_base.npz'):
        os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz'),
    os.path.join(BW, 'r7095_directions', 'grid_licensed', 'lcdm_base.npz'):
        os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control', 'out',
                     'r7807_control_planck2018_L2000.npz'),
    # r7815: the step-2 half, banked at last.  r7813's (a1) ordered the LSTEP=2 LMAXL=2000 control
    # run at Planck's point in resumable pieces; the four pieces are assembled here, and the
    # assembled bank shares the old step-2 bank's 950-sample grid EXACTLY, so this pair is as
    # grid-exact as the three above.
    os.path.join(BW, 'spectra', 'cc66_lcdm_L2000.npz'):
        os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass', 'out',
                     'r7812_control_step2_L2000_assembled.npz'),
    # r7815: (a1) named TWO banks and `cc66_lcdm.npz` is the other one -- LMAXL=1300, 600 samples
    # on 100..1298 step 2, the control P15's `2.10` per bin on the 133-bin unlensed configuration
    # reads (`CONTROL = 'cc66_lcdm'` in that receipt's own source).  Its re-pointed twin is
    # assembled from three slices the same way, and shares its grid exactly.
    os.path.join(BW, 'spectra', 'cc66_lcdm.npz'):
        os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass', 'out_L1300',
                     'r7812_control_step2_L1300_assembled.npz'),
}
#: refused on purpose, with the reason, so the gap is visible rather than silently absent.
#: EMPTY at r7815: the one entry was `spectra/cc66_lcdm_L2000.npz`, refused for want of a step-2
#: re-pointed bank.  (a1) built it, so the refusal is discharged rather than carried.
REFUSED = {}

NUM = re.compile(r'(?<![\w.])(-?\d+\.\d{2,}|-?\d{2,}\.\d+)(?![\w.])')


def assert_grid_identical():
    for old, new in SWAP.items():
        a, b = np.load(old, allow_pickle=True), np.load(new, allow_pickle=True)
        assert np.array_equal(a['ls'], b['ls']), f'grids differ: {old} vs {new} -- swap REFUSED'
    print(f'  {len(SWAP)} swap pair(s), every one grid-identical (asserted, not assumed)')
    for p, why in REFUSED.items():
        print(f'  REFUSED: {os.path.relpath(p, ROOT)}\n      {why}')


def run(receipt_path, swap):
    """stdout of the receipt, with np.load redirected per `swap` (empty = as the tree stands)"""
    shim = ('import numpy as _np, os as _os\n'
            f'_MAP = {swap!r}\n'
            '_real = _np.load\n'
            'def _p(f, *a, **k):\n'
            '    if isinstance(f, str):\n'
            '        f = _MAP.get(_os.path.abspath(f), f)\n'
            '    return _real(f, *a, **k)\n'
            '_np.load = _p\n')
    src = open(receipt_path, encoding='utf-8').read()
    runner = (shim + 'import runpy, sys\n'
              f'sys.argv = [{receipt_path!r}]\n'
              f'runpy.run_path({receipt_path!r}, run_name="__main__")\n')
    r = subprocess.run([sys.executable, '-u', '-c', runner], cwd=os.path.dirname(receipt_path),
                       capture_output=True, text=True, timeout=1800)
    return r.stdout + r.stderr, r.returncode


def figures(text):
    return [m.group(1) for m in NUM.finditer(text)]


def skeletons(text):
    """{line with its numbers blanked: [the numbers, in order]} -- so two runs are compared by
    MATCHING LINES rather than by position.  ⛔ A positional diff of every number in the output is
    meaningless here: the re-pointed run REDDENS, and a red receipt prints extra diagnostic lines, so
    the two streams fall out of step.  That was the first thing this harness got wrong, and the
    skeleton is the fix: a line is compared only with the line that says the SAME WORDS."""
    out = {}
    for ln in text.splitlines():
        nums = [m.group(1) for m in NUM.finditer(ln)]
        if not nums:
            continue
        key = NUM.sub('<#>', ln).strip()
        out.setdefault(key, []).append(nums)
    return out


def main():
    print('=' * 100)
    print('  r7809/r7811 ② -- WHAT MOVES WHEN THE CONTROL IS RE-POINTED (measured by swap)')
    print('=' * 100)
    assert_grid_identical()
    names = sys.argv[1:]
    if not names:
        print('\n  usage: python3 repoint.py <receipt-name> [...]')
        return 0
    for n in names:
        hits = [p for p in
                __import__('glob').glob(os.path.join(ROOT, 'receipts', '**', n + '.py'),
                                        recursive=True)]
        if not hits:
            print(f'\n  {n}: NOT FOUND')
            continue
        path = hits[0]
        print(f'\n{"=" * 100}\n  {n}\n{"=" * 100}')
        base, rc0 = run(path, {})
        swapped, rc1 = run(path, SWAP)
        s0, s1 = skeletons(base), skeletons(swapped)
        print(f'  as the tree stands: rc={rc0}, {len(figures(base))} number(s) on '
              f'{len(s0)} distinct line shape(s)')
        print(f'  control re-pointed: rc={rc1}, {len(figures(swapped))} number(s) on '
              f'{len(s1)} distinct line shape(s)'
              '   (a red here is EXPECTED: the pins hold the old values)')
        shared = [k for k in s0 if k in s1 and len(s0[k]) == len(s1[k])]
        only0 = [k for k in s0 if k not in s1]
        only1 = [k for k in s1 if k not in s0]
        moved, held = [], 0
        for k in shared:
            for a_row, b_row in zip(s0[k], s1[k]):
                for a, b in zip(a_row, b_row):
                    if a == b:
                        held += 1
                    else:
                        moved.append((k, a, b))
        print(f'  matched line shape(s): {len(shared)};  numbers on them: '
              f'{held + len(moved)} ({held} unchanged, {len(moved)} MOVED)')
        print(f'  line shapes only in the un-swapped run: {len(only0)};  only in the swapped run: '
              f'{len(only1)}  (these are the red run\'s own diagnostics, not figures that moved)')
        for k, a, b in moved:
            try:
                print(f'      {a:>14s} -> {b:<14s}  delta {float(b) - float(a):+.6g}   {k[:78]}')
            except ValueError:
                print(f'      {a:>14s} -> {b:<14s}   {k[:78]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
