#!/usr/bin/env python3
"""tolerance_builds.py -- THE COMPARE HALF OF THE SPLIT TOLERANCE JOB: WHICH BUILD WAS MEASURED, SAID BY NAME.
r7441 ②-③ (66, adopting 60's ⒝), built r7441+70.

** WHY.  **  `scope-tolerance` ran its three probes in sequence inside one 120-minute job.  When the job ran out
of time (60 isolated a clean 125-minute cancellation, r7441 ①), the whole scope went unmeasured as one block, and
since r7432 a cancelled run files `never probed` rather than red, so the condition was QUIET.  The split gives each
build its own job and budget; this script is what the compare job runs over whatever the three delivered.
** A split that fails closed is a budget raise with extra steps ** (r7441 ③): so a missing or timed-out build is
NAMED here, the comparison it is not part of still runs, and its own comparison is reported as not run.

** EACH BUILD IS ONE OF FOUR, read off what its probe job left (`STATUS` holds the probe's exit code):  **
    MEASURED    the probe exited 0 and every receipt in scope has a log
    PARTIAL     the probe ran out of its own budget (`timeout` rc 124/137), or the job was stopped from outside
                before it wrote `STATUS` -- k of n receipts have a log, the rest were never reached
    BROKEN      the probe exited non-zero and not by its budget
    UNMEASURED  no directory arrived, or the probe never started (`STATUS` says rc=none)
** THE COMPARISONS ARE THE OLD ONES, CALLED AND NOT REIMPLEMENTED: ** `sweep_tolerances --compare A B` and
`--compare A C`, each run when both of its builds delivered a directory.  Their PO-67 bits are OR-ed exactly as
the single job did (1 = a site flagged, 2 = a receipt unmeasured, 3 = both); a build that is not MEASURED adds
bit 2, because `not_swept` walks build A's logs only and cannot see a receipt A never reached.
A log that does not parse (a probe killed mid-write) is set aside as `.torn` and counted, never compared.

    python3 scripts/tolerance_builds.py --scope LIST --dirs DIR_A DIR_B DIR_C
    python3 scripts/tolerance_builds.py --seed        # the constructed cases, both directions
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOL = os.path.join(HERE, 'sweep_tolerances.py')
BUILDS = (('A', "the runner's one thread"), ('B', 'four threads'), ('C', 'the Prescott kernel at two threads'))
TIMEOUT_RCS = ('124', '137')
VERDICT = {0: 'CLEAN', 1: 'FLAGGED -- every receipt was measured', 2: 'NOT A SWEEP -- nothing flagged, a receipt unmeasured',
           3: 'FLAGGED AND NOT A SWEEP'}


def key(rel):
    return rel.replace('/', '_')


def read_build(d, scope):
    """(state, why, k) for one build's directory"""
    n = len(scope)
    if not os.path.isdir(d):
        return 'UNMEASURED', 'no probe directory arrived -- the job did not deliver', 0
    torn = 0
    for f in sorted(os.listdir(d)):
        if f.endswith('.json'):
            try:
                json.load(open(os.path.join(d, f)))
            except (ValueError, OSError):
                os.rename(os.path.join(d, f), os.path.join(d, f + '.torn'))
                torn += 1
    have = {f[:-5] for f in os.listdir(d) if f.endswith('.json')}
    k = sum(1 for r in scope if key(r) in have)
    st = os.path.join(d, 'STATUS')
    rc = open(st).read().split('rc=', 1)[-1].split()[0] if os.path.exists(st) else None
    tail = f'{k} of {n} probed' + (f', {torn} torn log(s) set aside' if torn else '')
    if rc is None:
        return 'PARTIAL', f'no STATUS: the job was stopped from outside before the probe finished -- {tail}', k
    if rc == 'none':
        return 'UNMEASURED', f'the probe never started -- {tail}', k
    if rc in TIMEOUT_RCS:
        return 'PARTIAL', f'the probe ran out of its own budget (rc {rc}) -- {tail}', k
    if rc != '0':
        return 'BROKEN', f'the probe exited rc {rc}, not by its budget -- {tail}', k
    if k < n or torn:
        return 'PARTIAL', f'the probe exited 0 but not every receipt has a log -- {tail}', k
    return 'MEASURED', tail, k


def verdict(scope, dirs, tol=TOL, out=print):
    states = {}
    for (b, label), d in zip(BUILDS, dirs):
        states[b] = read_build(d, scope)
    out(f'  TOLERANCE, SPLIT BY BUILD (r7441) -- {len(scope)} receipt(s) in scope')
    for b, label in BUILDS:
        s, why, _ = states[b]
        out(f'    build {b} ({label}): {s} -- {why}')
    rc = 0
    for b in ('B', 'C'):
        da, db = dirs[0], dirs['ABC'.index(b)]
        if os.path.isdir(da) and os.path.isdir(db):
            out(f'  ── comparison A↔{b}')
            r = subprocess.run([sys.executable, tol, '--compare', da, db], capture_output=True, text=True)
            for ln in (r.stdout + r.stderr).rstrip('\n').split('\n'):
                out(ln)
            rc |= r.returncode if r.returncode in (0, 1, 2, 3) else 2
        else:
            miss = [x for x, dd in (('A', da), (b, db)) if not os.path.isdir(dd)]
            out(f'  ── comparison A↔{b}: NOT RUN -- build {" and ".join(miss)} delivered nothing to compare')
            rc |= 2
    short = [b for b in 'ABC' if states[b][0] != 'MEASURED']
    if short:
        rc |= 2
    named = '; '.join(f'build {b} {states[b][0]}' for b in short)
    out(f'  VERDICT (both comparisons): {VERDICT[rc]}' + (f' -- {named}' if short else ''))
    return rc, states


# ------------------------------------------------------------------------------ the seed
def seed():
    """the constructed cases.  A stand-in `--compare` returns a chosen code per pair, so the OR and the
    naming are tested apart from the numerics; the real `--compare` is the same call in CI."""
    res = {}
    tmp = tempfile.mkdtemp(prefix='r7441_seed_')
    try:
        scope = ['receipts/X/R1.py', 'receipts/X/R2.py']
        fake = os.path.join(tmp, 'fake_tol.py')

        def setup(codes, builds):
            """builds: {b: (STATUS or None or 'ABSENT', [receipts logged], torn)}"""
            open(fake, 'w').write('import sys,os\nc=' + repr(codes) + '\n'
                                  'k=os.path.basename(sys.argv[3])\nprint("  VERDICT: stub", k)\nsys.exit(c.get(k,0))\n')
            dirs = []
            for b in 'ABC':
                d = os.path.join(tmp, 'run', 't' + b)
                shutil.rmtree(d, ignore_errors=True)
                st, logged, torn = builds.get(b, ('0', scope, False))
                dirs.append(d)
                if st == 'ABSENT':
                    continue
                os.makedirs(d)
                if st is not None:
                    open(os.path.join(d, 'STATUS'), 'w').write(f'rc={st}\n')
                for r in logged:
                    open(os.path.join(d, key(r) + '.json'), 'w').write('{"rc": 0, "sites": {}}')
                if torn:
                    open(os.path.join(d, key(scope[-1]) + '.json'), 'w').write('{"rc": 0, "si')
            return dirs

        def run(codes, builds):
            lines = []
            rc, st = verdict(scope, setup(codes, builds), tol=fake, out=lines.append)
            return rc, st, '\n'.join(lines)

        # ⓪–③ all three measured: the rc is the OR of the two comparisons, as the single job's was
        for name, codes, want in (('clean', {}, 0), ('flag', {'tB': 1}, 1), ('unswept', {'tC': 2}, 2),
                                  ('both', {'tB': 1, 'tC': 2}, 3)):
            rc, st, txt = run(codes, {})
            res[f'S{want}. all measured, {name}: rc {want} = the old OR, and no build named'] = \
                rc == want and all(s[0] == 'MEASURED' for s in st.values()) and ' -- build' not in txt.split('VERDICT')[-1]
        # ④ B absent: B named, A↔C still RUN, A↔B reported not run, bit 2 set
        rc, st, txt = run({'tC': 1}, {'B': ('ABSENT', [], False)})
        res['S4. B delivered nothing: B named UNMEASURED, A↔C still run and its flag kept (rc 3)'] = \
            st['B'][0] == 'UNMEASURED' and 'comparison A↔C\n' in txt + '\n' and 'A↔B: NOT RUN' in txt \
            and rc == 3 and 'build B UNMEASURED' in txt
        # ⑤ A absent: neither comparison runs, both reported, rc 2, A named
        rc, st, txt = run({}, {'A': ('ABSENT', [], False)})
        res['S5. A delivered nothing: both comparisons NOT RUN, A named, rc 2'] = \
            rc == 2 and txt.count('NOT RUN') == 2 and 'build A UNMEASURED' in txt
        # ⑥ B timed out at its budget with one of two logged
        rc, st, txt = run({}, {'B': ('124', scope[:1], False)})
        res['S6. B ran out of its budget: B named PARTIAL with 1 of 2, A↔B still run, rc 2'] = \
            st['B'][0] == 'PARTIAL' and '1 of 2 probed' in st['B'][1] and 'comparison A↔B' in txt and rc == 2
        # ⑦ a torn log is set aside and counted, never parsed by the comparison
        rc, st, txt = run({}, {'C': ('124', scope, True)})
        res['S7. a torn log in C is set aside as .torn and C reads PARTIAL'] = \
            st['C'][0] == 'PARTIAL' and 'torn' in st['C'][1] and \
            os.path.exists(os.path.join(tmp, 'run', 'tC', key(scope[-1]) + '.json.torn'))
        # ⑧ no STATUS (stopped from outside) and a non-timeout failure are told apart
        rc, st, txt = run({}, {'B': (None, scope[:1], False), 'C': ('1', scope, False)})
        res['S8. no STATUS reads PARTIAL (stopped from outside); rc 1 reads BROKEN, not PARTIAL'] = \
            st['B'][0] == 'PARTIAL' and 'from outside' in st['B'][1] and st['C'][0] == 'BROKEN' and rc & 2
        # ⑨ the probe never started
        rc, st, txt = run({}, {'C': ('none', [], False)})
        res['S9. STATUS rc=none reads UNMEASURED (the probe never started)'] = st['C'][0] == 'UNMEASURED' and rc == 2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    {"OK  " if v else "FAIL"}  {k}')
    bad = [k for k, v in res.items() if not v]
    print(f'  {len(res) - len(bad)} of {len(res)} hold')
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scope')
    ap.add_argument('--dirs', nargs=3)
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    if a.seed:
        return seed()
    scope = [l.strip() for l in open(a.scope) if l.strip()] if a.scope and os.path.exists(a.scope) else []
    return verdict(scope, a.dirs)[0]


if __name__ == '__main__':
    sys.exit(main())
