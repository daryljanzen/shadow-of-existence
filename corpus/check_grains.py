#!/usr/bin/env python3
"""check_grains.py -- the gate on GRAIN FRESHNESS, seventh of the corpus's gates.

** The failure this exists for happened in the open and nothing caught it. **  Across
r2376+c54.42-c54.58 the register (`THE_LIVE_ARC.md`) was kept current every single revision
while `THE_PLAN.md`, `THE_OPEN_PROBLEMS_LEDGER.md` and `THE_WEAVE.md` sat 22 revisions behind
and `OPEN_PROBLEMS_MAP.md` 17.  Nine revisions of the matter sector's deepest work -- nine
receipts, P14 grown by 2,900 words -- had reached none of them.  Daryl asked whether we were
working against a current picture of the whole arc, and we were not.

** Six gates policed claims, closure, the register, compilation, currency and queues.  NONE
policed whether the documents that hold the SHAPE OF THE WORK had heard about the work. **
A stale strategic grain is worse than an absent one, because a node reads it and believes it:
at c54.61 the ledger's own family-(12) table still assigned the hinge three to the generations,
an identification P14 had withdrawn thirty revisions earlier -- so the family was hunting for
colour in the one three-fold it believed was free, and the free one was the other.

THE RULE.  A grain may lag the register, because propagation is a real act and should not
happen on every revision.  ** It may not lag it silently, and it may not lag it far. **

  · WARN at   GRAIN_WARN   revisions behind the register
  · FAIL at   GRAIN_FAIL   revisions behind

Exit 1 on a grain past the fail window.  Warnings otherwise: this gate is meant to be read.

** r2378 -- THE GATE SILENTLY SKIPPED FOR EVERY NODE WORKING FROM A BUNDLE. **  It measured lag in
GIT COMMITS, and a bundle carries no .git, so `rev_of` returned None and the gate printed
"[SKIP] ... gate cannot run" and exited ZERO -- one line inside a run whose every other line said
clean.  A gate that skips is worse than no gate: the absence of a failure reads as a pass.  This is
the same defect three of the corpus's rules carried at r2378 (the changelog's 108 unlogged
revisions, the dependency matrix stale for a whole fork) -- a rule that is correct, and nothing
fails when it is skipped.

THE FALLBACK.  When git is unavailable the lag is measured from the fork-revision markers the
documents carry themselves -- the same measure `check_currency` uses -- against the register's own
marker.  The two measures are NOT the same quantity (commits since last touched, versus revisions
behind the front) and the gate says which one it used, every run.  ** It never skips. **  If it can
measure neither, that is a FAILURE and not a pass.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

REGISTER = 'THE_LIVE_ARC.md'

# The documents that hold the shape of the work, coarsest first.  A document earns a place
# here by being one a node would CONSULT to decide what to do next -- not by being important.
GRAINS = [
    ('THE_PLAN.md', 'top grain: the driver, the standing orders, the crosswalk'),
    ('THE_OPEN_PROBLEMS_LEDGER.md', 'family grain: the open problems as worked families'),
    ('OPEN_PROBLEMS_MAP.md', 'item grain: every open problem, clustered by work-kind'),
    ('THE_WEAVE.md', 'weave grain: how the parts are one object'),
]

GRAIN_WARN = 8
GRAIN_FAIL = 20


def marker_of(path):
    """the highest fork revision the file mentions -- the no-git fallback"""
    import re
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return None
    rs = [int(x) for x in re.findall(r'c54\.(\d+)',
          open(full, encoding='utf-8', errors='replace').read())]
    return max(rs) if rs else None


def have_git():
    return subprocess.run(['git', 'rev-parse', '--git-dir'], cwd=ROOT,
                          capture_output=True, text=True).returncode == 0


def rev_of(path):
    """the number of commits since this file was last touched"""
    h = subprocess.run(['git', 'log', '-1', '--format=%H', '--', path],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if not h:
        return None
    n = subprocess.run(['git', 'rev-list', f'{h}..HEAD', '--count'],
                       cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return int(n) if n.isdigit() else None


def main():
    print()
    print("  GRAIN FRESHNESS -- do the documents that hold the shape of the work know about it?")
    print()

    mode = 'git'
    reg = rev_of(REGISTER) if have_git() else None
    if reg is None:
        # no git (a bundle): measure from the documents' own fork markers instead
        mode = 'markers'
        front = marker_of(REGISTER)
        if front is None:
            print(f"  [FAIL] cannot measure {REGISTER} by git OR by fork marker.")
            print( "         This gate does not skip: an unmeasurable grain layer is a failure,")
            print( "         because the absence of a finding reads as a pass.")
            return 1
        reg = 0
        print(f"  measure: FORK MARKERS (no git history -- this tree is a bundle)")
        print(f"  register {REGISTER}: c54.{front}")
    else:
        print(f"  measure: GIT COMMITS")
        print(f"  register {REGISTER}: last moved {reg} revision(s) ago"
              f"{'  (current)' if reg == 0 else ''}")
    print()

    failures, warnings = [], []
    print(f"  {'grain':>32} {'behind register':>16}   what it holds")
    front = marker_of(REGISTER) if mode == 'markers' else None
    for fn, what in GRAINS:
        if mode == 'markers':
            m = marker_of(fn)
            if m is None:
                print(f"  {fn:>32} {'(no marker)':>16}   {what}")
                failures.append((fn, None))
                continue
            lag = max(0, front - m)
        else:
            n = rev_of(fn)
            if n is None:
                print(f"  {fn:>32} {'(no history)':>16}   {what}")
                continue
            lag = max(0, n - reg)
        mark = '   ' if lag < GRAIN_WARN else ('  !' if lag < GRAIN_FAIL else ' ⛔')
        print(f"  {fn:>32} {lag:>16}{mark}  {what}")
        if lag >= GRAIN_FAIL:
            failures.append((fn, lag))
        elif lag >= GRAIN_WARN:
            warnings.append((fn, lag))

    print()
    for fn, lag in warnings:
        print(f"  [WARN] {fn} is {lag} revisions behind the register.")
    for fn, lag in failures:
        if lag is None:
            print(f"  [FAIL] {fn} carries no fork marker, so its freshness cannot be read at all.")
            continue
        print(f"  [FAIL] {fn} is {lag} revisions behind the register -- past the {GRAIN_FAIL} "
              f"window.  ** A node consulting it will be told the shape of work that no longer "
              f"exists. **  Propagate, or state in the document itself what it does not cover.")

    if failures:
        print()
        print("  ⛔ Grain freshness FAILED.  The register is not the map; keeping one current")
        print("     while the others rot is how c54.42-c54.58 happened.")
        print(f"     (measured by {mode})")
        return 1

    if warnings:
        print()
        print("  Grains are lagging but inside the window.  Propagation is owed, not overdue.")
    else:
        print("  All grains current within the window.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
