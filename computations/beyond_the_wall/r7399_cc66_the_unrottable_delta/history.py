#!/usr/bin/env python3
"""r7399 ⑪ -- run both routes against the history, as the order requires before choosing.

⑪: *"Measure before you choose: how many revisions since `r7371` would each route have caught, run
against the history."*

The two routes are not the same kind of thing and the translation is in REGISTRATION.md, written
before this ran:
  ROUTE A -- the generator persists the previous total itself.  It PREVENTS, so "caught" is
    translated: at how many revisions would its computed `was` have DIFFERED from the published one.
  ROUTE B -- a gate on `steps-last-revision == 0` while `steps-left != 0`.  It DETECTS, so "caught"
    is literal: at how many revisions was that condition true.

    python3 -I history.py <repo-root>
"""
import importlib.util, os, re, subprocess, sys, tempfile

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
REVS = [f'r{n}' for n in range(7371, 7400, 2)]


def sh(*a):
    r = subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def last_commit_for(rev):
    """The last first-parent commit on origin/main whose SUBJECT carries this revision marker."""
    out = sh('log', '--first-parent', '--format=%H\t%s', 'origin/main')
    hits = [l.split('\t', 1) for l in out.split('\n') if '\t' in l]
    pat = re.compile(r'(?<![0-9])' + rev + r'(?![0-9])')
    for sha, subj in hits:                      # newest first, so the first hit is the last commit
        if pat.search(subj):
            return sha, subj
    return None, None


def load_est(sha, tmp):
    src = sh('show', f'{sha}:scripts/regen_frontier.py')
    if src is None:
        return None, None
    p = os.path.join(tmp, 'rf.py')
    open(p, 'w', encoding='utf-8').write(src)
    spec = importlib.util.spec_from_file_location('rf_hist', p)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except Exception as e:                       # a historical generator that will not import
        print(f'#   ⚠ {sha[:9]}: regen_frontier.py does not import ({type(e).__name__})')
        return None, None
    return getattr(m, 'EST', None), getattr(m, 'ORDER', None)


def live_at(sha):
    raw = sh('show', f'{sha}:THE_REGISTER.md')
    if raw is None:
        return None
    out = set()
    for line in raw.split('\n'):
        m = re.match(r'\|\s*(~~)?\s*\*\*(PO-\d+[a-z]?)\*\*', line)
        if m and not (m.group(1) or line.lstrip('|').lstrip().startswith('~~')):
            out.add(m.group(2))
    return out


def published(sha):
    """The headline the file actually carried: (open, steps, was)."""
    raw = sh('show', f'{sha}:THE_FRONTIER.md')
    if raw is None:
        return None
    m = re.search(r'\*\*(\d+) OPEN · (\d+) STEPS LEFT\*\*\s*\*\(was (\d+) last revision\)\*', raw)
    return (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None


rows = []
with tempfile.TemporaryDirectory() as tmp:
    for rev in REVS:
        sha, subj = last_commit_for(rev)
        if sha is None:
            rows.append((rev, None, None, None, None, None, None, 'no commit carries this marker'))
            continue
        EST, ORDER = load_est(sha, tmp)
        live = live_at(sha)
        pub = published(sha)
        if EST is None or ORDER is None or live is None or pub is None:
            rows.append((rev, sha, None, None, None, None, None, 'unreadable at this commit'))
            continue
        steps = sum(EST[p][1] for p in ORDER if p in live and p in EST)
        was = sum(EST[p][2] for p in ORDER if p in live and p in EST)
        zeros = [p for p in ORDER if p in live and p in EST and EST[p][2] == 0 and EST[p][1] != 0]
        rows.append((rev, sha, pub[0], pub[1], pub[2], steps, was, zeros))

print('# ⑪ THE HISTORY -- one row per revision, read at the last commit carrying its marker')
print(f'# {"rev":7s} {"sha":10s} {"pub OPEN":>8s} {"pub steps":>9s} {"pub was":>7s} '
      f'{"calc steps":>10s} {"calc was":>8s}  ROUTE-B zero rows')
prev_steps = None
routeA, routeB, n = 0, 0, 0
for r in rows:
    rev, sha, popen, psteps, pwas, steps, was, zeros = r
    if sha is None or steps is None:
        print(f'# {rev:7s} {"-":10s} {"":>8s} {"":>9s} {"":>7s} {"":>10s} {"":>8s}  {zeros}')
        continue
    n += 1
    a_was = prev_steps                    # Route A: the previous revision's own total
    a_hit = (a_was is not None and a_was != pwas)
    b_hit = bool(zeros)
    routeA += 1 if a_hit else 0
    routeB += 1 if b_hit else 0
    mark = ('A' if a_hit else '-') + ('B' if b_hit else '-')
    print(f'# {rev:7s} {sha[:9]:10s} {popen:8d} {psteps:9d} {pwas:7d} {steps:10d} {was:8d}  '
          f'[{mark}] {len(zeros)} zero: {" ".join(zeros) if zeros else "(none)"}'
          + (f'   routeA would publish was={a_was}' if a_was is not None else '   (no prior rev)'))
    prev_steps = steps

print()
print(f'# ⒜ ROUTE B caught {routeB} of {n} revision(s) read  '
      f'(condition: a live row with steps-last-revision 0 and steps-left non-zero)')
print(f'# ⒝ ROUTE A would have differed from the published `was` at {routeA} of {n} '
      f'(first revision has no prior total, so it cannot differ)')
print()
print('# ⌗ Route A is scored only where a PRIOR revision exists in the window; Route B needs no')
print('#   prior revision, which is itself a difference between them and not a bookkeeping detail.')
