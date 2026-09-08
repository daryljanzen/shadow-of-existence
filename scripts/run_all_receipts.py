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
    python3 scripts/run_all_receipts.py --timeout 900   # per-file seconds (default 600)
    python3 scripts/run_all_receipts.py --jobs 8        # parallelism (default: cpu_count-2)
    python3 scripts/run_all_receipts.py --only P15      # substring filter on the path
    python3 scripts/run_all_receipts.py --quick         # skip the files named SLOW below
    python3 scripts/run_all_receipts.py --resume CACHE --wall 500   # resumable, bounded invocation

** ⛔⛭ RESUMABILITY, r4512, AND IT IS NOT A CONVENIENCE. **  This gate's own `--how` text says to
launch the runner DETACHED and poll.  *On the container this line runs in, a detached process --
`nohup`, and `setsid nohup ... < /dev/null` exactly as that text prescribes -- IS REAPED AT THE END
OF THE TURN THAT STARTED IT.*  Three launches were killed between 15 and 20 minutes in, each
leaving the five-line header and no verdict, and the header-only `RUN_RESULT.txt` sitting in the
tree is the residue of an earlier one.  ** So the documented way to run this gate does not run it
here, and the failure presents as a file that looks like a run. **
  ⇒ *** The fix is not a longer wait: it is for the work to SURVIVE being interrupted. ***  With
      `--resume`, each receipt's result is written to the cache the moment it finishes, so an
      invocation killed at any point loses only what was in flight.  `--wall` stops cleanly at a
      budget instead of being killed at one.  Successive foreground invocations converge, and the
      final one prints the whole result.
  ⌗ ** The cache is keyed by TREE-DIGEST and discarded whole when it changes **, so a result can
    never be reused across a tree it was not measured on -- which is the same rule the cached
    `RUN_RESULT.txt` lives under, one level in.

** THIS GATE IS NOT IN THE STANDING TEN. **  It costs wall clock the others do not, so it is run
at a juncture -- before a bundle, after a sweep -- rather than every revision.  Saying so here
rather than quietly wiring it in, because a gate nobody runs is worth what a receipt nobody runs
is worth.
"""
import os

# ** NODE=ci FOR THE CHILD RECEIPTS -- 59, r3695, answering 60's route from r3726. **
# *Five registered receipts shell out to `check_revision_collisions`, which since 59's r3679
# REFUSES to run with `NODE` unset rather than defaulting to `PARITY = 0`.  That refusal is
# what stopped twenty-one collisions and it stays.*
#   ⇒ ** But a RUNNER is not a LINE. ** *The refusal exists to stop a node committing without
#   declaring which half it holds; a harness verifying that a receipt executes holds no half and
#   is claiming none.  `ci` is a DECLARED value meaning exactly that, and the gate under it
#   reports "the band is NOT CHECKED this run" -- which is the honest answer for a runner, not a
#   silent default.  60's reasoning is accepted as given.*
# ⌗ *This is NOT the r3679 defect one layer out: that defect was a gate INFERRING a band nobody
#  declared. This declares one, and the declared one holds no band.*
os.environ.setdefault('NODE', 'ci')
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
import json
import re
import threading
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
    # ** ADDED c54.226 (`L-560`).  This file had been FAILING FAST since r2682+c54.212 on a seed left
    # ** in it, and c54.222 removed the seed -- so the first run that actually EXECUTED it is the one
    # ** that discovered it is slow.  It exceeded the 900s budget under six-way contention. **
    #   ⇒ *** A file that fails in its first second has no measured cost, so removing a seed can move a
    #       receipt from "instant" to "over budget" with nothing in between.  Named here rather than
    #       left to surprise the next run: the tuple exists to make the budget visible. ***
    'P16_the_scalar_monodromy_is_four_pi_over_rho',
)

# ---------------------------------------------------------------- r4006
# ** A DECLARED PER-RECEIPT BUDGET, BECAUSE ONE RECEIPT IS LONGER THAN ANY CAP THE SUITE CAN CARRY. **
# `C59` is a convergence study: eight distinct Boltzmann projections, the heaviest 1260 modes to
# k_max = 2400 through the hierarchy path, and no redundant work in it (PART 2b reuses PART 1's
# results rather than re-running -- checked, not assumed).  ** Measured end to end on an idle
# machine: 1302s, all 23 assertions evaluated, exit 0. **  It had never once been seen to finish:
# the 300s cap filed it as a failure, the 600s cap as SLOW, and a detached 1200s attempt died 102
# seconds short of the verdict.
#   ⇒ *** AND `SLOW` IS NOT A PASS.  *** A receipt killed at the cap has evaluated nothing, so a
#       green run that reports it as `over timeout` is making no claim about it at all -- which is
#       precisely the hole this runner was built to close ("a registered receipt that does not run
#       where it is registered is not a receipt").  The cap was hiding one inside its own report.
# ⌗ *Declared here BY NAME with its measured cost beside it, never inferred from a file being slow.*
#   The global cap stays where it is; this buys the one receipt that needs it the room to finish,
#   and the number is the measurement plus headroom rather than a round figure chosen to feel safe.
LONG = {
    'C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation.py': 1800,  # measured 1302s
}


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


# ---------------------------------------------------------------- r4008
# ** ONE THREAD PER RECEIPT, BECAUSE A WALL-CLOCK CAP ON AN OVERSUBSCRIBED MACHINE MEASURES THE
#    SCHEDULER AND NOT THE RECEIPT. **
# `subprocess.run` inherited this process's environment, so every child was free to open as many
# BLAS/OpenMP threads as there are cores WHILE `--jobs N` was already running N of them.  The
# machine was oversubscribed by construction and each receipt's measured time was a fact about
# what happened to be running beside it.
#   ⛔ *** MEASURED, AND IT IS NOT A SMALL EFFECT. ***  The same tree, the same cap, two runs
#       differing only in whether C59 was allowed to finish:
#           C1  398s -> 493s   (+24%)
#           H1  423s -> OVER 600s, filed SLOW   (+42% at least)
#       ** H1 passed in one run and was killed in the next without one line of it changing. **
#       C59 is multithreaded -- 25:36 of CPU in 18:43 of wall on the solo probe -- so allowing it
#       to run pushed two neighbours over a cap that is supposed to describe them.
#   ⇒ ** A budget applied to a quantity that depends on what else is running is not a budget. **
#     Pinning to one thread each makes `--jobs N` mean N cores, and makes a receipt's time a
#     property of the receipt.  *This is the contaminated-measurement failure the corpus already
#     names, living inside the instrument that does the measuring.*
_ONE_THREAD = {
    'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
    'NUMEXPR_NUM_THREADS': '1', 'VECLIB_MAXIMUM_THREADS': '1',
}


def budget(path, default):
    """The per-file timeout: the declared one if this receipt has it, else the global cap."""
    return LONG.get(os.path.basename(path), default)


def run_one(path, timeout):
    d, b = os.path.dirname(path), os.path.basename(path)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, b], cwd=d, capture_output=True,
                           text=True, errors='replace', timeout=timeout,
                           env=dict(os.environ, **_ONE_THREAD))
        dt = time.time() - t0
        if r.returncode == 0:
            return ('PASS', path, dt, '')
        tail = [l for l in (r.stdout + r.stderr).split('\n') if l.strip()][-3:]
        return ('FAIL', path, dt, ' / '.join(tail)[:300])
    except subprocess.TimeoutExpired:
        return ('SLOW', path, time.time() - t0, f'exceeded {timeout}s')
    except Exception as e:                                     # noqa: BLE001
        return ('FAIL', path, time.time() - t0, f'{type(e).__name__}: {e}'[:300])


class Cache:
    """per-receipt results at ONE tree digest, written as each receipt finishes

    *A cache that survives a kill is the whole point, so it is rewritten on every completion
    rather than at the end -- 712 short rows, and the cost is invisible beside a receipt run.*
    """

    def __init__(self, paths, digest):
        names = [p for p in (paths or '').split(',') if p]
        self.path = names[0] if names else ''
        self.digest, self.lock = digest, threading.Lock()
        self.results, self.invocations, self.wall = {}, 0, 0.0
        self.reused = 0
        for i, path in enumerate(names):
            if not os.path.exists(path):
                continue
            try:
                d = json.load(open(path, encoding='utf-8'))
            except (ValueError, OSError):
                d = {}
            if d.get('digest') == digest:
                self.results.update(d.get('results', {}))
                self.invocations += int(d.get('invocations', 0))
                self.wall += float(d.get('wall', 0.0))
            elif d:
                print(f"  ⌗ resume cache {path} discarded: it was taken against tree "
                      f"{d.get('digest')!r}, not {digest} -- a result measured on another tree "
                      f"is not a result about this one")
        self.reused = len(self.results)

    def get(self, rel):
        r = self.results.get(rel)
        return (r[0], os.path.join(ROOT, rel), float(r[1]), r[2]) if r else None

    def put(self, st, path, dt, msg):
        if not self.path:
            return
        with self.lock:
            self.results[os.path.relpath(path, ROOT)] = [st, dt, msg]
            self._write()

    def _write(self):
        tmp = self.path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump({'digest': self.digest, 'invocations': self.invocations,
                       'wall': self.wall, 'results': self.results}, fh)
        os.replace(tmp, self.path)


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
    # ** r3997: default raised 300 -> 600.  A cap that kills a receipt and files it as a
    #   FAILURE is manufacturing failures, and three receipts were being failed by the cap
    #   alone.  The slowest receipt that PASSES takes 163s, so there is a 137s gap with
    #   nothing in it: raising the cap cannot mask a slowdown in anything currently green,
    #   because nothing green is near it.  ** Measure, then decide -- not defer. **
    ap.add_argument('--timeout', type=int, default=600)
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument('--only', default='')
    ap.add_argument('--quick', action='store_true')
    # ⌗ *`--resume a.json,b.json` reads every cache named and WRITES ONLY THE FIRST.*  The one
    #   receipt declared LONG (C59, measured 1302s) is longer than any foreground tool call this
    #   line can make, so it runs in its own invocation against its own cache while the rest run in
    #   bounded ones -- and the final invocation reads both.  ** A union of per-receipt results
    #   taken at the SAME digest is one run's worth of evidence; taken at different digests it is
    #   nothing, which is why the digest gates every cache separately. **
    ap.add_argument('--resume', default='', help='JSON cache(s), comma-separated; the first is written')
    ap.add_argument('--skip', default='', help='substring filter: EXCLUDE paths containing it')
    ap.add_argument('--wall', type=int, default=0, help='stop cleanly after N seconds')
    a = ap.parse_args()

    files, unresolved = registered()
    if a.only:
        files = [f for f in files if a.only in f]
    if a.skip:
        files = [f for f in files if a.skip not in f]
    if a.quick:
        files = [f for f in files if not any(s in f for s in SLOW)]
    print()
    print(f"  RUN-ALL-RECEIPTS -- {len(files)} registered receipt(s), {a.jobs} at a time, "
          f"{a.timeout}s each, each from ITS OWN DIRECTORY")
    for _b, _t in sorted(LONG.items()):
        if any(os.path.basename(f) == _b for f in files):
            print(f"  DECLARED LONG: {_b} runs on {_t}s, not {a.timeout}s -- named, with its "
                  f"measured cost in the source")
    # r2656+c54.208: the result of this run is CACHED and read by check_receipts_run.  A cache with
    # no expiry is a green verdict about a tree that no longer exists -- the file on disk at r2419
    # was still being read as current at r2656, 294 commits later, and reported "no receipt fails
    # for a reason inside the corpus" while 24 did.  So the run stamps WHAT IT RAN AGAINST.
    _digest = tree_digest()
    print(f"  TREE-DIGEST: {_digest}")
    print()
    t0 = time.time()
    cache = Cache(a.resume, _digest)
    cache.invocations += 1
    todo = [f for f in files if cache.get(os.path.relpath(f, ROOT)) is None]
    if a.resume:
        print(f"  RESUME: {len(files) - len(todo)} result(s) reused from {a.resume}, "
              f"{len(todo)} left to run"
              + (f", stopping cleanly at {a.wall}s" if a.wall else ""))
        print()
    incomplete = []
    if a.wall:
        # ** A BUDGET THAT STOPS THE RUNNER IS NOT THE SAME AS ONE THAT KILLS IT. **  Futures not
        # yet started are cancelled and the invocation reports what it did NOT reach by name, so
        # "incomplete" is a stated outcome rather than a truncated file.
        from concurrent.futures import as_completed
        ex = ThreadPoolExecutor(max_workers=a.jobs)
        fut = {ex.submit(run_one, f, budget(f, a.timeout)): f for f in todo}
        deadline = t0 + a.wall
        try:
            for f_ in as_completed(list(fut), timeout=max(1.0, deadline - time.time())):
                cache.put(*f_.result())
        except Exception:                                      # noqa: BLE001  (TimeoutError)
            pass
        for f_, src in fut.items():
            if f_.done() and not f_.cancelled():
                try:
                    cache.put(*f_.result())
                except Exception:                              # noqa: BLE001
                    pass
            else:
                f_.cancel()
                incomplete.append(src)
        ex.shutdown(wait=False, cancel_futures=True)
    else:
        with ThreadPoolExecutor(max_workers=a.jobs) as ex:
            for r in ex.map(lambda f: run_one(f, budget(f, a.timeout)), todo):
                cache.put(*r)
    cache.wall += time.time() - t0
    if a.resume:
        cache._write()
    res = [cache.get(os.path.relpath(f, ROOT)) for f in files]
    res = [r for r in res if r is not None]
    if incomplete:
        print(f"  ⛔ INCOMPLETE: this invocation stopped at its {a.wall}s budget with "
              f"{len(incomplete)} receipt(s) not reached.  ** Run it again with the same "
              f"--resume cache; nothing already measured is re-run. **")
        for f_ in sorted(incomplete)[:8]:
            print(f"      not reached: {os.path.relpath(f_, ROOT)}")
        if len(incomplete) > 8:
            print(f"      ... and {len(incomplete) - 8} more")
        print()
    ok = [r for r in res if r[0] == 'PASS']
    slow = [r for r in res if r[0] == 'SLOW']
    bad = [r for r in res if r[0] == 'FAIL']
    for st, p, dt, msg in sorted(bad, key=lambda r: r[1]):
        print(f"    [FAIL] {os.path.relpath(p, ROOT)}  ({dt:.0f}s)")
        print(f"           {msg}")
    for st, p, dt, msg in sorted(slow, key=lambda r: r[1]):
        print(f"    [slow] {os.path.relpath(p, ROOT)}  -- {msg}")
    print()
    _wall = cache.wall if a.resume else time.time() - t0
    print(f"  {len(ok)} pass, {len(bad)} fail, {len(slow)} over timeout, "
          f"in {_wall:.0f}s wall")
    if a.resume:
        # *The verdict line above must not be read as one elapsed clock when it is not one.*
        print(f"  ⌗ ASSEMBLED ACROSS {cache.invocations} INVOCATION(S) AT THIS DIGEST: "
              f"{cache.reused} result(s) reused, {len(res) - cache.reused} measured here.  Every "
              f"receipt ran exactly once against tree {_digest}, and the cache is discarded whole "
              f"the moment that digest changes.  The wall figure is the SUM of the invocations, "
              f"not a single elapsed clock.")
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
    if incomplete:
        print()
        print("  ⛔ THIS RUN IS NOT A VERDICT: receipts were not reached.  Re-invoke with the same")
        print("     --resume cache until it reports none.")
        return 2
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
