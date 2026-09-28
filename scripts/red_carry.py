#!/usr/bin/env python3
"""red_carry.py -- ** PO-65: A SCOPED RED PERSISTS IN THE REPOSITORY UNTIL A RUN COVERS IT AND PASSES. **

Built r6999+70.1 by node 70.

** THE DEFECT.  **  A scoped job's verdict is a statement about the PUSH, not about the tree.  Push N's
tolerance scope holds receipt R and R is red; push N+1 touches nothing R reads, so R is out of N+1's scope
and N+1 reads green -- with R exactly as red as it was.  `main`'s tolerance job went green after r6981 while
three flagged sites in a P10 receipt sat where they were.  ** Nothing was wrong with the detector or the
scope; the red was simply never asked about again. **

** THE REMEDY, AS ORDERED (carry-forward, not the monthly backstop).  **  Every scoped job, on every
push, writes what it found for its class to a LEDGER, and every scoped job, on every event, runs its
natural scope UNION everything the ledger carries.  A carried receipt leaves the ledger only when a run
that INCLUDED it came back green on it -- never by time, never by a push that missed it (the union means
no push misses it), and never by a green on a different scope (a green clears only the receipts it ran).

** WHERE THE LEDGER LIVES, AND WHY THERE.  **  In the repository, as the ref `refs/ci/carry`: a chain of
commits, each holding `carry.json`, each message saying which push, which class and what moved.
  * Not a file on the branch: the job would have to commit to the branch it is testing, which moves the
    head under the seat that pushed it, and a commit made with the workflow's token triggers no CI of
    its own -- the head would then carry no verdict at all.
  * Not the job's history (artifacts, caches, the API): those expire and are not what a seat reads.
  * A ref outside `refs/heads/` is not fetched by a plain `git fetch`, so it never shows up as a
    remote-tracking branch -- the band gate's "contained in another remote ref" test cannot see it.
  ⌗ Read it with   git fetch origin refs/ci/carry && git show FETCH_HEAD:carry.json
       and its history with   git log -p FETCH_HEAD

** WHO WRITES, AND FOR WHICH LINE.  **  Only `push` events write, keyed by the pushed branch.  A
`pull_request` event READS its head branch's carry (and main's) and writes nothing: its scope is already
the whole PR, so a PR red is asked about again on the next PR event anyway.  Every branch also runs
`main`'s carry, because a branch forked after the red holds the same tree -- and cannot clear it: only a
green on `main` clears `main`'s entry.

** WHAT COUNTS AS RED, PER CLASS.  **
  suite       a receipt the runner reported `[FAIL]` or `[slow]` (over timeout is not a pass)
  tolerance   a receipt with an unjudged FLAG or FLIP on either comparison, or one that did not run to
              exit 0 on every build (NOT A SWEEP)
  reads       a receipt FLAGGED by the trace, red under it, or over its budget
  ⛔ And when the job failed but no receipt can be named (the install died, the job hit its limit, the
    evidence is missing), the WHOLE scope is carried: a red nobody can attribute is still a red.

** CONCURRENCY.  **  A write is a fast-forward push of `refs/ci/carry`; if another job moved it first the
push is refused, and the write re-reads the ledger and re-applies ITS OWN delta (add these reds, clear
these greens) on top.  Two jobs disagreeing about one receipt: red wins.

** WHAT IT CANNOT DO -- STATED AS ITS LIMITS.  **
  * A receipt DELETED from the tree cannot run green.  It leaves the ledger at the first push where it is
    no longer registered, and the ledger commit says so by name: the deletion is in the diff and is the
    reviewer's to see.  A RENAMED receipt carries to its new path.
  * A pull request from a FORK gets a read-only token, so its runs cannot write; nothing here uses forks.
  * The ENVIRONMENT is still not in any diff -- `check_env_fingerprint` and the backstop hold that half.

Usage:
    python3 scripts/red_carry.py --union CLASS --list SCOPE          # add what is carried; rewrites SCOPE
    python3 scripts/red_carry.py --record CLASS --list SCOPE --outcome O [--suite-log F | --tol-dirs A B C
                                 | --trace DIR]                      # write this push's verdict
    python3 scripts/red_carry.py --show                              # print the ledger
    python3 scripts/red_carry.py --replay N                          # PO-65 ⓶: what carrying costs
    python3 scripts/red_carry.py --seed                              # PO-65 ⓷: both ways, on a real remote
"""
import argparse
import datetime
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REF = 'refs/ci/carry'
CLASSES = ('suite', 'tolerance', 'reads')
TRIES = 6


def _mod(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def git(root, *a, check=False, env=None):
    r = subprocess.run(['git', *a], cwd=root, capture_output=True, text=True,
                       env=None if env is None else {**os.environ, **env})
    if check and r.returncode:
        raise SystemExit(f'git {" ".join(a)}: {r.stderr.strip()}')
    return r


# ------------------------------------------------------------------------------------ the ledger
def fetch(root, remote='origin'):
    """(ledger, commit) at the remote's current tip, or ({}, None) if nobody has written one yet"""
    r = git(root, 'fetch', '-q', remote, f'+{REF}:{REF}')
    if r.returncode:
        if "couldn't find remote ref" in r.stderr or 'not our ref' in r.stderr:
            return {}, None
        raise SystemExit(f'red_carry: cannot read {REF} from {remote}: {r.stderr.strip()}')
    tip = git(root, 'rev-parse', REF, check=True).stdout.strip()
    return json.loads(git(root, 'show', f'{tip}:carry.json', check=True).stdout), tip


def write(root, ledger, parent, msg, remote='origin'):
    """one fast-forward push of the ref; False if another writer got there first"""
    ident = {'GIT_AUTHOR_NAME': 'red-carry', 'GIT_AUTHOR_EMAIL': 'red-carry@ci',
             'GIT_COMMITTER_NAME': 'red-carry', 'GIT_COMMITTER_EMAIL': 'red-carry@ci'}
    body = json.dumps(ledger, indent=1, sort_keys=True) + '\n'
    blob = subprocess.run(['git', 'hash-object', '-w', '--stdin'], cwd=root, input=body,
                          capture_output=True, text=True, check=True).stdout.strip()
    tree = subprocess.run(['git', 'mktree'], cwd=root, input=f'100644 blob {blob}\tcarry.json\n',
                          capture_output=True, text=True, check=True).stdout.strip()
    c = git(root, 'commit-tree', tree, *(['-p', parent] if parent else []), '-m', msg, check=True,
            env=ident).stdout.strip()
    return git(root, 'push', '-q', remote, f'{c}:{REF}').returncode == 0


def branches(env=os.environ):
    """(the branch whose ledger this event reads and writes, the lines it also runs, writes?)"""
    ev = env.get('GITHUB_EVENT_NAME', 'push')
    if ev == 'pull_request':
        b = env.get('GITHUB_HEAD_REF', '')
        return b, [x for x in (b, env.get('GITHUB_BASE_REF', 'main'), 'main') if x], False
    b = env.get('GITHUB_REF_NAME', '') or 'main'
    return b, [b] if b == 'main' else [b, 'main'], True


def carried(ledger, lines, which):
    out = {}
    for b in lines:
        for rec, e in (ledger.get(b, {}).get(which) or {}).items():
            out.setdefault(rec, {**e, 'line': b})
    return out


def apply(ledger, branch, which, ran, red, sha, run, gone):
    """this push's delta: every receipt it RAN is cleared unless red; every red is added (keeping the
    first push it was seen at); a receipt no longer registered leaves, by name"""
    cur = ledger.setdefault(branch, {}).setdefault(which, {})
    added, cleared, kept = [], [], []
    for rec in sorted(ran):
        if rec in red:
            if rec in cur:
                kept.append(rec)
            else:
                cur[rec] = {'since': sha, 'run': run}
                added.append(rec)
        elif rec in cur:
            del cur[rec]
            cleared.append(rec)
    removed = []
    for rec in sorted(gone):
        if rec in cur:
            del cur[rec]
            removed.append(rec)
    if not cur:
        del ledger[branch][which]
    if not ledger[branch]:
        del ledger[branch]
    return added, cleared, kept, removed


# ------------------------------------------------------------------------------------ evidence
SUITE_RED = re.compile(r'^    \[(FAIL|slow)\] (\S+)', re.M)
SUITE_VERDICT = re.compile(r'^  (\d+) pass, (\d+) fail, (\d+) over timeout', re.M)


def reds_suite(log):
    t = open(log, encoding='utf-8', errors='replace').read()
    v = SUITE_VERDICT.search(t)
    if not v:
        return None
    red = {m.group(2) for m in SUITE_RED.finditer(t)}
    # the verdict counts are the check on the parse: a red we cannot name is a red we cannot clear
    return red if len(red) == int(v.group(2)) + int(v.group(3)) else None


def reds_tolerance(dirs, root, scope):
    st = _mod('sweep_tolerances')
    key = {r.replace('/', '_'): r for r in scope}
    red, a = set(), dirs[0]
    for b in dirs[1:]:
        if not (os.path.isdir(a) and os.path.isdir(b)):
            return None
        flags = [r for r in st.compare(a, b) if r['kind'] in ('FLAG', 'FLIP')]
        judged, _ = st.split_judged(flags, os.path.join(root, st.JUDGED), root)
        for r in flags:
            if r not in judged:
                red.add(r['receipt'])
        red.update(n for n, _ in st.not_swept(a, b))
    for d in dirs:
        have = {os.path.basename(p)[:-5] for p in os.listdir(d) if p.endswith('.json')} if os.path.isdir(d) else set()
        red.update(k for k in key if k not in have)              # never probed at all
    return {key.get(r, key.get(r + '.py', r)) for r in red}


def reds_reads(trace, root, scope):
    if not os.path.isdir(trace):
        return None
    srr = _mod('sweep_runner_reads')
    red, seen = set(), set()
    for p in os.listdir(trace):
        if not p.endswith('.json'):
            continue
        d = json.load(open(os.path.join(trace, p)))
        rel = os.path.relpath(d['receipt'], root) if d['receipt'].startswith('/') else d['receipt']
        seen.add(rel)
        if d.get('timeout') or d['rc'] not in (0, None) or srr.classify(d, root)[0]:
            red.add(rel)
    return red | (set(scope) - seen)


# ------------------------------------------------------------------------------------ the two CI steps
def do_union(root, which, path, remote):
    branch, lines, _ = branches()
    ledger, tip = fetch(root, remote)
    regs = set(_mod('receipt_scope').registered(root))
    natural = [l.strip() for l in open(path) if l.strip()]
    carry = carried(ledger, lines, which)
    add = sorted(r for r in carry if r not in natural and r in regs)
    absent = sorted(r for r in carry if r not in regs)
    with open(path, 'w') as fh:
        fh.write(''.join(r + '\n' for r in natural + add))
    print(f'  CARRIED ({which}): {len(carry)} receipt(s) red on {"/".join(lines)} and not yet run green '
          f'-- ledger {REF} @ {(tip or "none")[:10]}; {len(add)} added to this scope of {len(natural)}',
          file=sys.stderr)
    for r in sorted(carry):
        e = carry[r]
        print(f'    carried since {e["since"][:10]} on {e["line"]}: {r}'
              + ('  (NOT REGISTERED here -- cannot run)' if r in absent else ''), file=sys.stderr)
    return 0


def do_record(root, which, path, outcome, evidence, remote):
    branch, _, writes = branches()
    if not writes:
        print(f'  red_carry: a {os.environ.get("GITHUB_EVENT_NAME")} event reads the ledger and does not '
              f'write it (its scope is the whole PR, asked again on every PR event)', file=sys.stderr)
        return 0
    ran = [l.strip() for l in open(path) if l.strip()] if os.path.exists(path) else []
    if outcome == 'success':
        red, how = set(), 'the run passed'
    else:
        red = evidence()
        if not red:
            red, how = set(ran), (f'the job ended "{outcome}" with no receipt it can name -- '
                                  f'the WHOLE scope of {len(ran)} is carried')
        else:
            how = f'{len(red)} named red'
    regs = set(_mod('receipt_scope').registered(root))
    sha, run = os.environ.get('GITHUB_SHA', 'HEAD'), (
        f'{os.environ.get("GITHUB_SERVER_URL", "")}/{os.environ.get("GITHUB_REPOSITORY", "")}'
        f'/actions/runs/{os.environ.get("GITHUB_RUN_ID", "")}')
    for _ in range(TRIES):
        ledger, tip = fetch(root, remote)
        gone = {r for r in (ledger.get(branch, {}).get(which) or {}) if r not in regs}
        added, cleared, kept, removed = apply(ledger, branch, which, ran, red, sha, run, gone)
        still = sorted((ledger.get(branch, {}).get(which) or {}))
        print(f'  RECORD ({which}, {branch} @ {sha[:10]}): ran {len(ran)}, {how}; '
              f'+{len(added)} carried, {len(cleared)} cleared by a green, {len(kept)} still red, '
              f'{len(removed)} no longer registered; {len(still)} carried after this push', file=sys.stderr)
        for tag, xs in (('+ carried', added), ('- cleared', cleared), ('= still red', kept),
                        ('- UNREGISTERED, leaves by name', removed)):
            for r in xs:
                print(f'    {tag}: {r}', file=sys.stderr)
        if not (added or cleared or removed):
            return 0
        msg = (f'{which} @ {branch} {sha[:10]}: +{len(added)} -{len(cleared)} ={len(kept)}'
               + (f' unregistered {len(removed)}' if removed else '') + f'\n\n{run}\n'
               + ''.join(f'\n{t} {r}' for t, xs in (('+', added), ('-', cleared), ('x', removed)) for r in xs))
        if write(root, ledger, tip, msg, remote):
            return 0
        print('  red_carry: another job moved the ledger first -- re-reading and re-applying', file=sys.stderr)
    raise SystemExit(f'red_carry: could not write {REF} in {TRIES} tries')


# ------------------------------------------------------------------------------------ PO-65 ⓶: the cost
def replay(root, n, index=None):
    """Over main's last N first-parent pushes, per class: for every (push, receipt in its scope) -- every
    place a red can be born -- how many pushes until the receipt is in a scope AGAIN on its own.  That is
    how long a red born there is SILENT today, and the least time the carry holds it (a repair has to
    touch the receipt or what it reads, so the repair push is itself one of those natural covers).  Each
    push in between is a push the carry adds the receipt's seconds to."""
    rs = _mod('receipt_scope')
    idx, traced, _, _ = rs.load(root, index)
    shas = rs.git(root, 'rev-list', '--first-parent', f'-{n}', 'origin/main').split()[::-1]
    when = [int(rs.git(root, 'show', '-s', '--format=%ct', s).strip()) for s in shas]
    med = sorted(e['s'] or 0 for e in idx.values())[len(idx) // 2]
    sec = {r: (e['s'] if e['s'] is not None else med) for r, e in idx.items()}
    diffs = [rs.diff(root, f'{s}^1..{s}') for s in shas]
    q = lambda xs, f: sorted(xs)[int(f * (len(xs) - 1))] if xs else 0
    N = len(shas)
    print(f'\n  PO-65 ⓶ -- {N} first-parent pushes to main ({datetime.datetime.utcfromtimestamp(when[0]):%m-%d} '
          f'.. {datetime.datetime.utcfromtimestamp(when[-1]):%m-%d}), index traced at {traced["commit"][:10]}')
    rows = {}
    for which in CLASSES:
        mult = 3 if which == 'tolerance' else 1
        sc = [set(rs.scope(idx, *d, which)) for d in diffs]
        nxt, lag_p, lag_h, cost, cens = {}, [], [], [], 0
        for i in range(N - 1, -1, -1):
            for r in sc[i]:
                j = nxt.get(r)
                if j is None:
                    cens += 1
                    j_, h = N, (when[-1] - when[i]) / 3600
                else:
                    j_, h = j, (when[j] - when[i]) / 3600
                lag_p.append(j_ - i)
                lag_h.append(h)
                cost.append(sec[r] * mult * (j_ - i - 1))
            for r in sc[i]:
                nxt[r] = i
        births = sum(len(s) for s in sc)
        base = sum(sum(sec[r] for r in s) for s in sc) * mult / N
        rows[which] = dict(births=births, cens=cens, lag_p=lag_p, lag_h=lag_h, cost=cost, base=base)
        print(f'\n  {which.upper()}  ({births} receipt-runs in {N} pushes; natural scope {base:,.0f} s per push'
              + (', x3 builds' if mult == 3 else '') + ')')
        print(f'    a red born there stays SILENT today for (pushes)   median {q(lag_p, .5)}, p90 {q(lag_p, .9)}, '
              f'max {max(lag_p) if lag_p else 0}')
        print(f'                                        (hours)    median {q(lag_h, .5):.1f}, p90 {q(lag_h, .9):.1f}, '
              f'max {max(lag_h) if lag_h else 0:.1f}')
        print(f'    ... never covered again inside the window     {cens} of {births} '
              f'({100 * cens / max(births, 1):.1f}%) -- carried to the window\'s end, a LOWER bound')
        tot = sum(cost)
        print(f'    what ONE red costs the carry, total           median {q(cost, .5):,.0f} s, mean '
              f'{tot / max(births, 1):,.0f} s, p90 {q(cost, .9):,.0f} s, max {max(cost) if cost else 0:,.0f} s')
        print(f'    ⇒ at b reds born per push, the carry adds     b x {tot / max(births, 1):,.0f} s per push  '
              f'(b x {100 * tot / max(births, 1) / max(base, 1):.0f}% of this job\'s natural scope)')
    return rows


# ------------------------------------------------------------------------------------ PO-65 ⓷: seed
def seed():
    """Both ways, on a real bare remote, through the same two functions CI calls.  A fake runner reads
    each receipt's red/green from a file the "pushes" edit, so what is red is decided by the tree."""
    tmp = tempfile.mkdtemp(prefix='po65_seed_')
    res, root, remote = {}, os.path.join(tmp, 'w'), os.path.join(tmp, 'remote.git')
    try:
        subprocess.run(['git', 'init', '-q', '--bare', remote], check=True)
        subprocess.run(['git', 'init', '-q', root], check=True)
        git(root, 'remote', 'add', 'origin', remote)
        regs = {'receipts/A/R1.py', 'receipts/A/R2.py', 'receipts/A/R3.py'}
        st = {r: 'green' for r in regs}

        def push(branch, scope, sha, carry=True, ev='push'):
            env = {'GITHUB_EVENT_NAME': ev, 'GITHUB_REF_NAME': branch, 'GITHUB_SHA': sha,
                   'GITHUB_HEAD_REF': branch if ev == 'pull_request' else ''}
            old = dict(os.environ)
            os.environ.update(env)
            try:
                b, lines, writes = branches()
                ledger, _ = fetch(root)
                run = set(scope) | (set(carried(ledger, lines, 'suite')) & regs if carry else set())
                red = {r for r in run if st[r] == 'red'}
                if writes:
                    for _ in range(TRIES):
                        L, tip = fetch(root)
                        apply(L, b, 'suite', run, red, sha, 'seed', {r for r in (L.get(b, {}).get('suite') or {}) if r not in regs})
                        if write(root, L, tip, f'seed {sha}'):
                            break
                return ('red' if red else 'green'), sorted(red)
            finally:
                os.environ.clear()
                os.environ.update(old)

        def ledger_of(b):
            return sorted((fetch(root)[0].get(b, {}).get('suite') or {}))

        st['receipts/A/R1.py'] = 'red'                                   # push 1 breaks R1, in scope
        res['1. a push that breaks R1 and covers it is red'] = push('main', {'receipts/A/R1.py'}, 's1')[0] == 'red'
        res['   ... and R1 is carried'] = ledger_of('main') == ['receipts/A/R1.py']
        # push 2 touches only R2: WITHOUT the carry this is the defect, a green over a red tree
        res['2. WITHOUT the carry, a push that misses R1 reads GREEN (the defect)'] = \
            push('main', {'receipts/A/R2.py'}, 's2x', carry=False)[0] == 'green'
        # ... reset what that uncarried run cleared (it wrote nothing about R1: R1 never ran)
        res['   ... and even then it cannot CLEAR R1, which it never ran'] = ledger_of('main') == ['receipts/A/R1.py']
        v, red = push('main', {'receipts/A/R2.py'}, 's2')
        res['3. WITH the carry, a push that misses R1 is RED at the end of that push'] = (v, red) == ('red', ['receipts/A/R1.py'])
        res['   ... and R1 is still carried'] = ledger_of('main') == ['receipts/A/R1.py']
        # a branch forked after the red runs main's carry, and its green on R1 cannot clear main's entry
        st['receipts/A/R1.py'] = 'green'
        v, _ = push('fix', {'receipts/A/R3.py'}, 'b1')
        res['4. a branch runs main\'s carry (R1 fixed there: green)'] = v == 'green'
        res['   ... and a branch green does not clear MAIN\'s entry'] = ledger_of('main') == ['receipts/A/R1.py']
        st['receipts/A/R1.py'] = 'red'
        # a green on a different scope, with the carry off, cannot clear R1
        push('main', {'receipts/A/R3.py'}, 's3x', carry=False)
        res['5. a later green on a DIFFERENT scope does not clear R1'] = ledger_of('main') == ['receipts/A/R1.py']
        # a pull_request event reads and does not write
        st['receipts/A/R1.py'] = 'green'
        push('main', {'receipts/A/R1.py'}, 'pr1', ev='pull_request')
        res['6. a pull_request event does not write, even green'] = ledger_of('main') == ['receipts/A/R1.py']
        # the repair lands on main: the run that covers R1 and passes clears it
        v, _ = push('main', {'receipts/A/R3.py'}, 's4')
        res['7. the push that covers R1 and PASSES clears it'] = v == 'green' and ledger_of('main') == []
        # a racing writer: the second write is refused, re-reads, re-applies
        st['receipts/A/R2.py'] = 'red'
        L0, tip0 = fetch(root)
        push('main', {'receipts/A/R2.py'}, 's5')                         # moves the ref under L0
        L0.setdefault('main', {}).setdefault('suite', {})['receipts/A/R3.py'] = {'since': 'race', 'run': 'x'}
        res['8. a stale writer is refused (fast-forward only)'] = write(root, L0, tip0, 'stale') is False
        res['   ... and the ledger still holds the first writer\'s red'] = ledger_of('main') == ['receipts/A/R2.py']
        # the job failed and named nothing: the whole scope carries
        L, tip = fetch(root)
        apply(L, 'main', 'suite', {'receipts/A/R1.py', 'receipts/A/R3.py'}, {'receipts/A/R1.py', 'receipts/A/R3.py'}, 's6', 'x', set())
        write(root, L, tip, 'unattributed')
        res['9. an unattributable failure carries its whole scope'] = ledger_of('main') == sorted(regs)
        # a receipt removed from the tree leaves by name
        regs.discard('receipts/A/R3.py')
        L, tip = fetch(root)
        _, _, _, removed = apply(L, 'main', 'suite', set(), set(), 's7', 'x', {'receipts/A/R3.py'})
        write(root, L, tip, 'removed')
        res['10. a receipt no longer registered leaves the ledger by name'] = removed == ['receipts/A/R3.py'] \
            and 'receipts/A/R3.py' not in ledger_of('main')
        log = git(root, 'log', '--format=%s', REF).stdout.split('\n')
        res['11. the ledger is a history in the repository, one commit per write'] = len([l for l in log if l]) >= 6
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in res.items():
        print(f'    [{"ok" if v else "FAIL"}]  {k}')
    ok = all(res.values())
    print(f'\n  carried exactly when it should be, cleared exactly when it should be: {ok}')
    return 0 if ok else 1


# ------------------------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    ap.add_argument('--remote', default='origin')
    ap.add_argument('--union', choices=CLASSES)
    ap.add_argument('--record', choices=CLASSES)
    ap.add_argument('--list', metavar='SCOPE')
    ap.add_argument('--outcome', help="the run step's outcome: success, failure, cancelled, skipped")
    ap.add_argument('--suite-log')
    ap.add_argument('--tol-dirs', nargs='+')
    ap.add_argument('--trace')
    ap.add_argument('--show', action='store_true')
    ap.add_argument('--replay', type=int, metavar='N')
    ap.add_argument('--index')
    ap.add_argument('--seed', action='store_true')
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    if a.seed:
        print('\n  red_carry --seed: is a red carried until a run covers it and passes, and only then cleared?\n')
        return seed()
    if a.replay:
        replay(root, a.replay, a.index)
        return 0
    if a.show:
        ledger, tip = fetch(root, a.remote)
        print(f'  {REF} @ {(tip or "none")[:10]}')
        print(json.dumps(ledger, indent=1, sort_keys=True))
        return 0
    if a.union:
        return do_union(root, a.union, a.list, a.remote)
    if a.record:
        scope = [l.strip() for l in open(a.list) if l.strip()] if a.list and os.path.exists(a.list) else []
        ev = {'suite': lambda: reds_suite(a.suite_log) if a.suite_log and os.path.exists(a.suite_log) else None,
              'tolerance': lambda: reds_tolerance(a.tol_dirs, root, scope) if a.tol_dirs else None,
              'reads': lambda: reds_reads(a.trace, root, scope) if a.trace else None}[a.record]
        return do_record(root, a.record, a.list, a.outcome or 'failure', ev, a.remote)
    ap.print_help()
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
