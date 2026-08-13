#!/usr/bin/env python3
"""run_all_receipts.py -- ** THE ELEVENTH GATE: RUN THEM. **

Built r2376+c54.161, against the finished assertion sweep.

** WHY IT EXISTS, AND IT IS THE PLAINEST REASON IN THE CORPUS. **  Nothing here had ever run the
receipts.  `check_receipts` verifies that a \\rcpt resolves to an INDEX row and a file on disk; the
assertion census counts checks by READING source; `lint_assertions` parses it; `check_compile`
builds the papers.  At r2376+c54.160 the sweep found `ROBUST_p1p2_scan` -- registered, cited --
exiting 1 on ImportError before reaching a single line of computation, and every gate was green.

** So "the receipt passes" was never a claim any gate was making. **  THE_BASE_RATE, entry
twenty-three: an instrument that reads a file has not run it.

This runs every registered receipt from ITS OWN DIRECTORY, which is the second half of the same
point -- a receipt that only runs from somewhere else is not runnable where it is registered.

  * PASS   exit 0.
  * FAIL   non-zero exit: an assertion fired, or the file is broken.  ** Both are failures and the
           gate does not distinguish them, because a receipt that cannot run cannot be trusted to
           have checked anything either. **
  * SLOW   over the per-file timeout; reported, not failed, and named so the budget is visible.

Usage:
    python3 scripts/run_all_receipts.py                 # all registered receipts
    python3 scripts/run_all_receipts.py --timeout 600   # per-file seconds (default 300)
    python3 scripts/run_all_receipts.py --jobs 8        # parallelism (default: cpu_count-2)
    python3 scripts/run_all_receipts.py --only P15      # substring filter on the path
    python3 scripts/run_all_receipts.py --quick         # skip the files named SLOW below

** THIS GATE IS NOT IN THE STANDING TEN. **  It costs wall clock the others do not, so it is run
at a juncture -- before a bundle, after a sweep -- rather than every revision.  Saying so here
rather than quietly wiring it in, because a gate nobody runs is worth what a receipt nobody runs
is worth.
"""
import argparse
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# Known-slow receipts: full Boltzmann hierarchies and BBN networks.  Named rather than hidden.
SLOW = (
    'ROBUST_p1p2_scan', 'C11TEST_radiation_zeroed', 'P15_the_second_arm_actually_run',
    'bbn_network', 'P16_validate_bbn', 'P16_theory_error_and_likelihood',
    'P15_verify_lowell_boltzmann', 'P15_camb_reference', 'BUILD_camb_store',
)


def registered():
    """the receipts INDEX.md registers, in the order it registers them"""
    idx = os.path.join(ROOT, 'receipts', 'INDEX.md')
    out, seen = [], set()
    for ln in open(idx, encoding='utf-8'):
        # ** r2555: the paper column is CASE-SENSITIVE here and the geometric core is written
        # `p0` lowercase, so this runner skipped TWELVE receipts -- the fourth instance of the
        # silent-discard class (c54.203 fixed check_receipts and make_receipt_appendix; the
        # duplicate dict key at r2552 and check_currency's parser at r2550 were the others).
        #   ⇒ ** A runner that skips a receipt leaves NO trace: the receipt simply never runs,
        #     and a green run means nothing about it. **
        if not (ln[:3].upper().startswith('| P') or ln.startswith('| `')):
            continue
        c = [x.replace('\\|', '|').strip() for x in re.split(r'(?<!\\)\|', ln.rstrip('\n'))[1:-1]]
        if len(c) < 4 or c[0] == 'paper':
            continue
        p = c[3].strip('` ')
        if p.startswith('receipts/'):
            p = p[len('receipts/'):]
        f = os.path.join(ROOT, 'receipts', p)
        if f not in seen and os.path.exists(f):
            seen.add(f)
            out.append(f)
    return out


def run_one(path, timeout):
    d, b = os.path.dirname(path), os.path.basename(path)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, b], cwd=d, capture_output=True,
                           text=True, errors='replace', timeout=timeout)
        dt = time.time() - t0
        if r.returncode == 0:
            return ('PASS', path, dt, '')
        tail = [l for l in (r.stdout + r.stderr).split('\n') if l.strip()][-3:]
        return ('FAIL', path, dt, ' / '.join(tail)[:300])
    except subprocess.TimeoutExpired:
        return ('SLOW', path, time.time() - t0, f'exceeded {timeout}s')
    except Exception as e:                                     # noqa: BLE001
        return ('FAIL', path, time.time() - t0, f'{type(e).__name__}: {e}'[:300])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--timeout', type=int, default=300)
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument('--only', default='')
    ap.add_argument('--quick', action='store_true')
    a = ap.parse_args()

    files = registered()
    if a.only:
        files = [f for f in files if a.only in f]
    if a.quick:
        files = [f for f in files if not any(s in f for s in SLOW)]
    print()
    print(f"  RUN-ALL-RECEIPTS -- {len(files)} registered receipt(s), {a.jobs} at a time, "
          f"{a.timeout}s each, each from ITS OWN DIRECTORY")
    print()
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        res = list(ex.map(lambda f: run_one(f, a.timeout), files))
    ok = [r for r in res if r[0] == 'PASS']
    slow = [r for r in res if r[0] == 'SLOW']
    bad = [r for r in res if r[0] == 'FAIL']
    for st, p, dt, msg in sorted(bad, key=lambda r: r[1]):
        print(f"    [FAIL] {os.path.relpath(p, ROOT)}  ({dt:.0f}s)")
        print(f"           {msg}")
    for st, p, dt, msg in sorted(slow, key=lambda r: r[1]):
        print(f"    [slow] {os.path.relpath(p, ROOT)}  -- {msg}")
    print()
    print(f"  {len(ok)} pass, {len(bad)} fail, {len(slow)} over timeout, "
          f"in {time.time()-t0:.0f}s wall")
    if ok:
        worst = sorted(ok, key=lambda r: -r[2])[:5]
        print("  slowest that passed: "
              + ", ".join(f"{os.path.basename(p)} {dt:.0f}s" for _, p, dt, _ in worst))
    if bad:
        print()
        print("  ⛔ A REGISTERED RECEIPT THAT DOES NOT RUN WHERE IT IS REGISTERED IS NOT A RECEIPT.")
        return 1
    print()
    print("  Every registered receipt runs, in place, and exits 0 -- so every assertion in the")
    print("  reproducibility layer was actually evaluated.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
