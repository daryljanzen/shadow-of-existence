#!/usr/bin/env python3
"""sweep_runner_reads.py -- ** PO-60 ⓶ᵇ: THE NEVER-GREEN-UNDER-THE-RUNNER, SWEPT ACROSS EVERY RECEIPT. **

Built r6931+70.3 by node 70.  NOT wired into CI: `--seed` below is the both-ways seeding the
order requires before any wiring, and a full sweep costs what a suite run costs.

** THE CLASS. **  A receipt that has never run in the environment the suite runs it in.  Four
were found inside PO-59's 83: born reading `corpus/...` relative to the REPOSITORY ROOT while
`run_all_receipts` runs every receipt from ITS OWN FAMILY DIRECTORY.  ⛔ And the sharp form: a check
that iterates a glob and asserts over its members is vacuously true when the glob is empty, so a
receipt can be green for years while reading nothing at all.

** WHAT THIS MEASURES.  It does not read source and guess: it RUNS each receipt exactly as the
runner does -- from its own directory, `NODE=ci`, one thread, twice the runner's per-file budget (a trace is not a timing) --
with its filesystem reads observed** (`open`, `io.open`, `pathlib.Path.open`, `glob.glob`,
`glob.iglob`, `os.listdir`, `Path.glob`, `Path.rglob`):

    FLAGGED   a RELATIVE path that resolves to nothing from the receipt's directory -- an `open`
              of a missing file, or a relative glob that returns empty.  That is the class exactly:
              the read the author meant does not happen where the suite runs it.
    TRIAGE    an ABSOLUTE in-repo glob or listdir that returned empty.  ** Reported and judged by
              hand, never flagged automatically **, because a resolver that probes several roots
              for one file returns empty on every root but one by design -- and at r6931+70.3 both
              receipts in this bucket are exactly that (L556/R1, L559/O1, INDEX-token resolvers).

** THE MEASUREMENT (r6931+70.3). **
  * HEAD, all 858 registered, traced: FLAGGED 0 -- the four PO-59 found were repaired there.
  * SEEDED ON THE REAL INSTANCES: at `31f3276` (PO-59's start) all four are FLAGGED; at HEAD, where
    they are repaired, none is.  See `--seed` for the synthetic pair.
  * THE POPULATION BOTH WAYS: the pre-repair tree `31f3276` traced whole -- 855 receipts, ~80 of
    them red -- FLAGS EXACTLY FOUR, and they are exactly PO-59's four (P03 T, P03 w, P14 lifts, P17
    ledgers).  ** 0 false positives on a population that contains the class, 4 of 4 recovered. **
    ⚠ The first tracer missed P17 ledgers, which reads through `Path.read_text` and so never
    touches `builtins.open`; the seeding found it and `Path.open` / `io.open` are hooked now.
  ⚠ ** WHAT IT CANNOT SEE: ** a read made in a SUBPROCESS the receipt spawns (git show, a child
    python), and a read through a C extension (numpy.load, np.loadtxt) -- those bypass the Python
    hooks.  Stated as recall limits.

Usage:
    python3 scripts/sweep_runner_reads.py --out DIR [--jobs 4] [--root R]   # trace every receipt
    python3 scripts/sweep_runner_reads.py --report DIR                       # summarise a trace
    python3 scripts/sweep_runner_reads.py --seed                             # both-ways seeding
    python3 scripts/sweep_runner_reads.py --trace-one LOG FILE               # internal: one receipt
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.abspath(__file__)
_ONE_THREAD = {'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
               'NUMEXPR_NUM_THREADS': '1', 'VECLIB_MAXIMUM_THREADS': '1', 'NODE': 'ci'}


# ------------------------------------------------------------------------------------ the tracer
def trace_one(log, target):
    """Run one receipt in THIS process, from the current directory, with its reads observed."""
    import builtins
    import glob as _glob
    import io as _io
    import pathlib
    import runpy

    events = []
    real_open, real_popen = builtins.open, pathlib.Path.open

    def note(kind, arg, n=None, ok=None):
        if len(events) < 400:
            events.append({'kind': kind, 'arg': str(arg)[:300], 'n': n, 'ok': ok})

    def _open(file, *a, **k):
        if isinstance(file, (str, os.PathLike)) and not os.path.isabs(os.fspath(file)):
            note('open_rel', os.fspath(file), ok=os.path.exists(os.fspath(file)))
        return real_open(file, *a, **k)

    def _popen(self, *a, **k):
        if not self.is_absolute():
            note('open_rel', str(self), ok=self.exists())
        return real_popen(self, *a, **k)

    rg, rig, rld = _glob.glob, _glob.iglob, os.listdir
    pg, prg = pathlib.Path.glob, pathlib.Path.rglob

    def _globw(pat, *a, **k):
        r = rg(pat, *a, **k)
        if not r:
            note('glob_empty', pat, 0)
        if not os.path.isabs(os.fspath(pat)):
            note('glob_rel', pat, len(r))
        return r

    def _iglobw(pat, *a, **k):
        r = list(rig(pat, *a, **k))
        if not r:
            note('glob_empty', pat, 0)
        if not os.path.isabs(os.fspath(pat)):
            note('glob_rel', pat, len(r))
        return iter(r)

    def _ldw(p='.'):
        r = rld(p)
        if not r:
            note('listdir_empty', p, 0)
        return r

    def _pgw(self, pat, *a, **k):
        r = list(pg(self, pat, *a, **k))
        if not r:
            note('glob_empty', f'{self}/{pat}', 0)
        if not self.is_absolute():
            note('glob_rel', f'{self}/{pat}', len(r))
        return iter(r)

    def _prgw(self, pat, *a, **k):
        r = list(prg(self, pat, *a, **k))
        if not r:
            note('glob_empty', f'{self}/**/{pat}', 0)
        if not self.is_absolute():
            note('glob_rel', f'{self}/**/{pat}', len(r))
        return iter(r)

    builtins.open = _io.open = _open
    pathlib.Path.open = _popen
    _glob.glob, _glob.iglob, os.listdir = _globw, _iglobw, _ldw
    pathlib.Path.glob, pathlib.Path.rglob = _pgw, _prgw
    rc = 0
    try:
        sys.argv = [target]
        sys.path.insert(0, os.path.dirname(os.path.abspath(target)))   # as `python3 FILE` does
        runpy.run_path(target, run_name='__main__')
    except SystemExit as e:
        rc = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    except BaseException as e:                                          # noqa: BLE001
        rc = 1
        note('exception', f'{type(e).__name__}: {e}')
    finally:
        with real_open(log, 'w') as fh:
            json.dump({'receipt': os.path.abspath(target), 'rc': rc, 'events': events}, fh)
        sys.stdout.flush()
    os._exit(rc)


def _run(root, rel, budget, out):
    key = rel.replace('/', '_')
    log = os.path.join(out, key + '.json')
    if os.path.exists(log):
        return
    d, f = os.path.split(os.path.join(root, rel))
    env = dict(os.environ, **_ONE_THREAD)
    try:
        subprocess.run([sys.executable, HERE, '--trace-one', log, f], cwd=d, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=budget)
    except subprocess.TimeoutExpired:
        pass
    if not os.path.exists(log):
        with open(log, 'w') as fh:
            json.dump({'receipt': os.path.join(root, rel), 'rc': None, 'events': [],
                       'timeout': True}, fh)


def sweep(root, out, jobs):
    import importlib.util
    from concurrent.futures import ThreadPoolExecutor
    spec = importlib.util.spec_from_file_location('rar', os.path.join(root, 'scripts',
                                                                      'run_all_receipts.py'))
    m = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, ['x']
    spec.loader.exec_module(m)
    sys.argv = argv
    files, _ = m.registered()
    os.makedirs(out, exist_ok=True)
    with ThreadPoolExecutor(max_workers=jobs) as ex:
        list(ex.map(lambda f: _run(root, os.path.relpath(f, root), 2 * max(900, m.budget(f, 600)), out),
                    files))
    return len(files)


# ------------------------------------------------------------------------------------ the report
def classify(d, root):
    """FLAGGED: a relative read that resolved to nothing.  TRIAGE: an absolute in-repo empty glob."""
    root = os.path.abspath(root)
    flag, triage = [], []
    for e in d['events']:
        a = e['arg']
        if (e['kind'] == 'open_rel' and not e['ok']) or (e['kind'] == 'glob_rel' and e['n'] == 0):
            flag.append(a)
        elif e['kind'] in ('glob_empty', 'listdir_empty') and os.path.isabs(a) and a.startswith(root):
            triage.append(a[len(root):])
    return sorted(set(flag)), sorted(set(triage))


def report(out, root):
    import glob
    logs = sorted(glob.glob(os.path.join(out, '*.json')))
    flagged, triage, timeouts, red = [], [], [], []
    for p in logs:
        d = json.load(open(p))
        rel = os.path.relpath(d['receipt'], root) if d['receipt'].startswith('/') else d['receipt']
        if d.get('timeout'):
            timeouts.append(rel)
            continue
        if d['rc'] not in (0, None):
            red.append(rel)
        f, t = classify(d, root)
        if f:
            flagged.append((rel, d['rc'], f))
        if t:
            triage.append((rel, d['rc'], t))
    print(f'\n  RUNNER-READ SWEEP -- {len(logs)} receipt(s) traced from their own directories')
    print(f'    FLAGGED (a relative read that resolved to nothing) : {len(flagged)}')
    print(f'    TRIAGE  (an absolute in-repo glob that was empty)  : {len(triage)}  -- judged by hand')
    print(f'    red under the trace                                : {len(red)}')
    print(f'    over the budget, not traced to the end             : {len(timeouts)}')
    for rel, rc, f in flagged:
        print(f'  ⛔ rc={rc}  {rel}\n       {f[:3]}')
    for rel, rc, t in triage:
        print(f'  ⌗ rc={rc}  {rel}  ({len(t)} empty probe(s), e.g. {t[0][:80]})')
    for rel in timeouts:
        print(f'  ⚠ timeout  {rel}')
    print()
    return 1 if flagged else 0


# ------------------------------------------------------------------------------------ seeding
_SEEDS = {
    # PLANTED: the root-relative read the four PO-59 instances made -- red under the runner
    'S1_planted_relative_read.py':
        "t = open('corpus/seed_paper.tex').read()\nassert 'Seed' in t\n",
    # PLANTED, the sharp form: a relative glob, empty from the family dir, and an all() over it
    'S2_planted_green_on_an_empty_glob.py':
        "import glob\nfs = glob.glob('corpus/*.tex')\n"
        "assert all('Seed' in open(f).read() for f in fs)\n",
    # LEGITIMATE: anchored to the repository root from the file's own location
    'S3_legit_anchored_read.py':
        "import os\nROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))\n"
        "assert 'Seed' in open(os.path.join(ROOT, 'corpus', 'seed_paper.tex')).read()\n",
    # LEGITIMATE: an anchored glob that is empty BECAUSE the thing was removed, asserted as absence
    'S4_legit_absence_asserted.py':
        "import glob, os\nROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))\n"
        "assert glob.glob(os.path.join(ROOT, 'corpus', 'withdrawn_*.tex')) == []\n",
}


def seed():
    tmp = tempfile.mkdtemp(prefix='po60b_seed_')
    try:
        os.makedirs(os.path.join(tmp, 'corpus'))
        os.makedirs(os.path.join(tmp, 'receipts', 'SEED'))
        open(os.path.join(tmp, 'corpus', 'seed_paper.tex'), 'w').write('\\section{Seed}\n')
        out = os.path.join(tmp, 'trace')
        os.makedirs(out)
        for name, body in _SEEDS.items():
            open(os.path.join(tmp, 'receipts', 'SEED', name), 'w').write(body)
            _run(tmp, os.path.join('receipts', 'SEED', name), 60, out)
        got = {}
        for name in _SEEDS:
            d = json.load(open(os.path.join(out, f'receipts_SEED_{name}.json')))
            f, t = classify(d, tmp)
            got[name] = ('FLAGGED' if f else ('TRIAGE' if t else 'clean'), d['rc'])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in got.items():
        print(f'    {k:40} {v[0]:8} rc={v[1]}')
    planted = got['S1_planted_relative_read.py'][0] == 'FLAGGED' \
        and got['S2_planted_green_on_an_empty_glob.py'] == ('FLAGGED', 0)
    legit = got['S3_legit_anchored_read.py'] == ('clean', 0) \
        and got['S4_legit_absence_asserted.py'] == ('TRIAGE', 0)
    print(f'  planted instances flagged (S2 green, as the sharp form is): {planted}')
    print(f'  legitimate reads not flagged (S4 reaches triage only)       : {legit}')
    return 0 if planted and legit else 1


def main():
    if len(sys.argv) == 4 and sys.argv[1] == '--trace-one':
        trace_one(sys.argv[2], sys.argv[3])
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(HERE)))
    ap.add_argument('--out')
    ap.add_argument('--report')
    ap.add_argument('--jobs', type=int, default=4)
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        print('\n  sweep_runner_reads --seed: does it catch a planted instance AND let a legitimate one through?\n')
        return seed()
    if a.out:
        n = sweep(os.path.abspath(a.root), a.out, a.jobs)
        print(f'  traced {n} registered receipt(s) into {a.out}')
        return report(a.out, os.path.abspath(a.root))
    if a.report:
        return report(a.report, os.path.abspath(a.root))
    ap.print_help()
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
