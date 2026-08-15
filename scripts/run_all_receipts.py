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
import os
import sys

# ---------------------------------------------------------------- r2656+c54.208
# ** `scripts/queue.py` SHADOWS THE STDLIB `queue`, WHICH `concurrent.futures` IMPORTS. **
# Running this file as `python3 scripts/run_all_receipts.py` puts `scripts/` first on sys.path,
# so ThreadPoolExecutor dies on `queue.SimpleQueue` before a single receipt runs.  The runner has
# therefore been UNRUNNABLE since `scripts/queue.py` was added -- which is why the cached
# `RUN_RESULT.txt` this gate reads had not moved in 294 commits.
#   ⇒ *** A 9-minute out-of-band job that crashes in its first second leaves the LAST GOOD RESULT
#       sitting on disk, so the failure presents as a stale success rather than as a failure. ***
# Dropping this file's own directory from sys.path fixes THIS script.  The hazard is general --
# any script here that touches threads inherits it -- and the rename is the observer line's to
# make, so it is routed rather than done under them.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or '.') != _HERE]

import argparse
import glob
import hashlib
import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** c54.222: the INDEX row filter lives in ONE place now.  `corpus/` is appended rather than
# prepended so it cannot shadow the stdlib the way `scripts/` did (see the note above). **
sys.path.append(os.path.join(ROOT, 'corpus'))
import index_rows  # noqa: E402

# Known-slow receipts: full Boltzmann hierarchies and BBN networks.  Named rather than hidden.
SLOW = (
    'ROBUST_p1p2_scan', 'C11TEST_radiation_zeroed', 'P15_the_second_arm_actually_run',
    'bbn_network', 'P16_validate_bbn', 'P16_theory_error_and_likelihood',
    'P15_verify_lowell_boltzmann', 'P15_camb_reference', 'BUILD_camb_store',
)


def registered():
    """the receipts INDEX.md registers, in file order -- AND what it names but cannot resolve

    Returns `(paths, unresolved)`.

    ** r2555: the paper column is CASE-SENSITIVE here and the geometric core is written `p0`
    lowercase, so this runner skipped TWELVE receipts -- the fourth instance of the silent-discard
    class (c54.203 fixed check_receipts and make_receipt_appendix; the duplicate dict key at r2552
    and check_currency's parser at r2550 were the others). **
      ⇒ ** A runner that skips a receipt leaves NO trace: the receipt simply never runs, and a green
        run means nothing about it. **

    ** ⛭⛭ c54.222 -- THE FIFTH INSTANCE, AND THE FILTER IS NOW GONE RATHER THAN PATCHED AGAIN. **  The
    predicate decided membership by the PAPER column, and the corpus writes an EM-DASH there for a
    receipt that supports no paper: ** TWENTY rows dropped, EIGHTEEN naming a file on disk, none of
    them ever run by this gate -- and one of the eighteen FAILS. **  It lives once now, in
    `corpus/index_rows.py`, with the four earlier patches folded in; see that file's head.

    ** ⛔ AND THE SECOND HALF OF THE SAME SILENCE: A FAILING `os.path.exists` WAS A `continue`. **
    Four registered rows name `storyboard_receipts/...` at the repository ROOT, which this function
    prepended `receipts/` to and then dropped; two more name files that have never existed in any
    commit.  *** Unresolvable is RETURNED now, and the caller reports it.  A runner permitted to
    silently not-run a registered receipt is not a gate. ***
    """
    seen, out, unresolved = set(), [], []
    for r in index_rows.rows(resolve_paths=True, root=ROOT):
        if not r.runnable:
            continue                      # a `.md` kill record is registered and is not runnable
        if not r.paths:
            unresolved.append((r.lineno, r.token))
            continue
        for f in r.paths:
            if f not in seen:
                seen.add(f)
                out.append(f)
    return out, unresolved


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


def tree_digest():
    """A digest of everything a receipt can check: the papers it quotes and the receipts themselves.

    ** Deliberately NOT the git HEAD. **  Requiring an exact-HEAD match would fail the gate on every
    commit that touches a register file, which trains the caller to skip it; hashing only what a
    receipt can actually READ fails exactly when the result could have gone stale and at no other
    time.  The digest is over content, so a revert restores the old digest and the cached run is
    valid again -- which is correct, because it is.
    """
    h = hashlib.sha256()
    for pat in ('corpus/*.tex', 'receipts/**/*.py', 'computations/**/*.py'):
        for f in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
            h.update(os.path.relpath(f, ROOT).encode())
            h.update(open(f, 'rb').read())
    return h.hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--timeout', type=int, default=300)
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument('--only', default='')
    ap.add_argument('--quick', action='store_true')
    a = ap.parse_args()

    files, unresolved = registered()
    if a.only:
        files = [f for f in files if a.only in f]
    if a.quick:
        files = [f for f in files if not any(s in f for s in SLOW)]
    print()
    print(f"  RUN-ALL-RECEIPTS -- {len(files)} registered receipt(s), {a.jobs} at a time, "
          f"{a.timeout}s each, each from ITS OWN DIRECTORY")
    # r2656+c54.208: the result of this run is CACHED and read by check_receipts_run.  A cache with
    # no expiry is a green verdict about a tree that no longer exists -- the file on disk at r2419
    # was still being read as current at r2656, 294 commits later, and reported "no receipt fails
    # for a reason inside the corpus" while 24 did.  So the run stamps WHAT IT RAN AGAINST.
    print(f"  TREE-DIGEST: {tree_digest()}")
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
    # ** c54.222: an UNRESOLVABLE row is reported HERE, next to the failures, and it fails the gate
    # even when every file that does exist passes. **  *A registry entry naming nothing is not a
    # smaller defect than a receipt that exits 1 -- it is the same defect one step earlier, and it
    # was the one with no reader.*
    if unresolved and not a.only:
        print()
        print(f"  ⛔ {len(unresolved)} REGISTERED ROW(S) NAME A `.py` THAT DOES NOT EXIST:")
        for lineno, tok in unresolved:
            print(f"    [FAIL] receipts/INDEX.md line {lineno}: {tok}")
        print("    ⇒ Searched `receipts/<path>` AND `<path>` from the repository root, globbed.")
        print("      ** A row is a claim that a computation exists.  An unresolvable row is a false")
        print("      one, and it is printed into the reproducibility appendix as `[OK]`. **")
    if bad or (unresolved and not a.only):
        print()
        print("  ⛔ A REGISTERED RECEIPT THAT DOES NOT RUN WHERE IT IS REGISTERED IS NOT A RECEIPT.")
        return 1
    print()
    print("  Every registered receipt runs, in place, and exits 0 -- so every assertion in the")
    print("  reproducibility layer was actually evaluated.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
