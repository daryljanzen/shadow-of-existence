#!/usr/bin/env python3
"""r7327+cc66 -- WHERE check_quote_pins' EIGHTEEN MINUTES ACTUALLY GO, and why no constant can be a budget.

`r7327` item ④ corrected my `r7323` framing: the gate runs in `233` s on the chat seat's container and
`1096.1` s on this one, so the false red was a property of ONE CONTAINER and not of the tree.  Taken.
⇒ But neither framing -- mine ("the runtimes moved and nobody re-measured") nor the cache caveat -- says
what the gate SPENDS, and the answer is measurable and is neither.

  * the INSTRUMENT (`mutate_assertions.py --quote`, the AST scan over every receipt) is ~27 s, under
    3 per cent of the gate, and a second consecutive run is only ~11 per cent faster -- so it is not the
    scan and not the page cache;
  * the gate's cost is GIT SUBPROCESS CALLS in `held_check`, run once per MEANING-HELD row, dominated by
    H5's PATH-SCOPED `git log --format=%H -- <receipt>` over a 5,046-commit history.

That makes the runtime track process spawn and object-store IO, which differ by multiples between
containers -- and it GROWS with the history and with the held-row count, which only rise.  So no constant
can be a budget, for a stronger reason than either of us gave.

⛔ AND IT CONTAINS A TRAP, which is why this script exists instead of a patch: the obvious speedup -- one
`git log --name-only` pass building receipt -> commits -- is 28.6x faster on that phase and DISAGREES WITH
THE GATE ON 19 OF 143 HELD RECEIPTS.  A performance repair that changes a gate's answers is a defect.
The safe repair is named at the foot and is NOT applied here.

  python3 decompose.py          # ~4 minutes; the two instrument runs are the slow part
"""
import io
import os
import subprocess
import sys
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
BASELINE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
HELD = 'MEANING-HELD'


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace')


def timed(fn, n=3):
    ts = []
    for _ in range(n):
        t0 = time.time()
        fn()
        ts.append(time.time() - t0)
    return min(ts), sum(ts) / len(ts)


def held_rows():
    out = []
    for ln in io.open(BASELINE, encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln.strip() or ln.startswith('#'):
            continue
        p = ln.split('\t')
        if len(p) >= 6 and p[5] == HELD:
            out.append(p[0])
    return out


def main():
    rows = held_rows()
    receipts = sorted(set(rows))
    commits = git('rev-list', '--count', 'HEAD').stdout.strip()
    print()
    print('  WHAT check_quote_pins SPENDS -- measured on this container, nothing asserted')
    print()
    print(f'    history: {commits} commits;  {HELD} rows: {len(rows)} over {len(receipts)} distinct receipts')
    print()
    print('  ⒜ the per-call cost of the four git calls held_check makes per row (min of 3):')
    rc = receipts[0]
    for label, args in (('rev-parse --verify            H1', ['rev-parse', '--verify', '--quiet', 'HEAD^{commit}']),
                        ('merge-base --is-ancestor      H2', ['merge-base', '--is-ancestor', 'HEAD~5', 'HEAD']),
                        ('log --format=%H -- <receipt>  H5', ['log', '--format=%H', '--', rc]),
                        ('show HEAD:<receipt>           H3', ['show', f'HEAD:{rc}'])):
        lo, av = timed(lambda a=args: git(*a))
        print(f'      {label}: {lo:6.3f} s')
    lo5, _ = timed(lambda: git('log', '--format=%H', '--', rc))
    print(f'  ⇒ H5 alone, once per row: {len(rows)} x {lo5:.3f} = {len(rows) * lo5:6.1f} s')
    print(f'    and the four together:  {len(rows)} x ~{lo5 + 0.24:.2f}  = {len(rows) * (lo5 + 0.24):6.1f} s')

    print()
    print('  ⒝ the instrument alone, twice in a row -- the cache test r7327 item ④ asks for:')
    for i in (1, 2):
        t0 = time.time()
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'scripts', 'mutate_assertions.py'), '--quote'],
                           cwd=ROOT, capture_output=True, text=True, env=dict(os.environ, NODE='ci'))
        el = time.time() - t0
        sites = sum(1 for l in r.stdout.splitlines() if '[QUOTE-PIN]' in l)
        print(f'      run {i}: {el:6.1f} s, rc={r.returncode}, {sites} site lines')
    print('  ⇒ the AST scan is a small fraction of the gate and a repeat barely moves, so neither the')
    print('    scan nor the page cache is what the gate spends.')

    print()
    print('  ⒞ ⛔ THE TRAP IN THE OBVIOUS SPEEDUP.  One `git log --name-only` pass builds the same')
    print('     receipt -> commits map in one call.  Equivalence, checked on every held receipt:')
    t0 = time.time()
    per = {r: set(git('log', '--format=%H', '--', r).stdout.split()) for r in receipts}
    t_per = time.time() - t0
    t0 = time.time()
    one, cur = {}, None
    for line in git('log', '--format=%x00%H', '--name-only').stdout.split('\n'):
        if line.startswith('\x00'):
            cur = line[1:].strip()
        elif line.strip() and cur:
            one.setdefault(line.strip(), set()).add(cur)
    t_one = time.time() - t0
    bad = [r for r in receipts if per[r] != one.get(r, set())]
    print(f'      per-receipt calls ({len(receipts)}): {t_per:6.1f} s      one pass: {t_one:5.1f} s'
          f'      {t_per / t_one:.1f}x')
    print(f'      ⛔ DISAGREE on {len(bad)} of {len(receipts)} receipts '
          f'({100 * len(bad) / len(receipts):.0f} per cent) -- so it is NOT a drop-in repair:')
    for r in bad[:5]:
        a, b = per[r], one.get(r, set())
        print(f'        {os.path.basename(r)[:58]:58s} per-row {len(a):2d}  one-pass {len(b):2d}')
    print('      A performance repair that changes a gate s answers is a defect.  Not proposed.')

    print()
    print(f'  ⇒ THE SAFE REPAIR, routed and NOT applied: held_check calls the path-scoped `git log` once')
    print(f'    per ROW, and there are {len(rows)} rows over only {len(receipts)} receipts.  Memoising that one')
    print(f'    call per receipt is the SAME function on the SAME arguments -- identical answers by')
    print(f'    construction -- and turns {len(rows)} calls into {len(receipts)}: about '
          f'{(len(rows) - len(receipts)) * lo5:.0f} s saved on this container.')
    print(f'    It is a gate s internals and another seat drafted it, so it is routed, not pushed.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
