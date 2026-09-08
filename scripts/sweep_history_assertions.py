#!/usr/bin/env python3
"""** THE HORIZON SWEEP: which registered receipts rest on history this clone may not reach? **

Three instrument defects in this corpus have been found by NEEDING them rather than by auditing
for them -- the k-truncation (r3870), the LSTEP quantisation (r4138) and NOISW (r4492).  All three
were invisible to the gates and silently wrong for hundreds of revisions.  ** This sweep is the
first thing this line runs that looks for that class deliberately. **

It reports THREE passes, because the class has two directions and only one of them is visible from
a truncated clone:

  A  NAMED COMMITS.  Every 7-40 hex SHA a receipt hands to git, checked for reachability from HEAD
     and across all refs.  *A receipt naming a commit the clone cannot reach asserts over an empty
     string.*  This is the direction 61 found four of, and it FAILS loudly on a shallow clone.

  B  HEAD-LIMITED WALKS.  `git log` / `rev-list` without `--all`, which return a different answer
     on a truncated clone than on a whole one.  *A green from a shallow clone is not a weaker claim
     than a green from a full one; it is a claim about a different and much smaller thing.*

  C  NEGATIVE ASSERTIONS OVER HISTORY.  A check that asserts something is ABSENT from history
     passes MORE easily the less history there is.  ** This is the direction that is invisible from
     a short clone ** -- N1's TESTIMONY seed (r4132) passed on a shallow clone precisely because the
     ids it should have named were beyond the horizon.

Run:  python3 scripts/sweep_history_assertions.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RCPT = os.path.join(ROOT, 'receipts')

SHA = re.compile(r"['\"]([0-9a-f]{7,40})['\"]")
GITCALL = re.compile(r"['\"]git['\"]\s*,\s*['\"](\w[\w-]*)['\"]")
NEG = re.compile(r"\bnot in\b|\bis None\b|==\s*0\b|len\([^)]*\)\s*==\s*0|\bassert not\b|"
                 r"\bnever\b|\bno such\b|\babsent\b", re.I)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True)


def horizon():
    sh = os.path.exists(os.path.join(ROOT, '.git', 'shallow'))
    head = len([l for l in git('log', '--format=%s', 'HEAD').stdout.split('\n')
                if re.match(r'^r\d+', l)])
    allr = len([l for l in git('log', '--all', '--format=%s').stdout.split('\n')
                if re.match(r'^r\d+', l)])
    return sh, head, allr


def files():
    out = []
    for dp, _, fs in os.walk(RCPT):
        for f in sorted(fs):
            if f.endswith('.py'):
                out.append(os.path.join(dp, f))
    return sorted(out)


def main():
    sh, head, allr = horizon()
    print()
    print("  " + "=" * 74)
    print("  THE HORIZON SWEEP — receipts that rest on history")
    print("  " + "=" * 74)
    print(f"  this clone: {'SHALLOW' if sh else 'FULL'};  {head} revision-numbered commits from "
          f"HEAD, {allr} across all refs")
    if sh:
        print("  ⛔ ON A SHALLOW CLONE PASS C IS BLIND BY CONSTRUCTION.  Run this where the")
        print("     history is whole, or its clean result means nothing.")
    print()

    fs = files()
    A, B, C = [], [], []
    for p in fs:
        src = open(p, encoding='utf-8', errors='replace').read()
        rel = os.path.relpath(p, ROOT)
        if "'git'" not in src and '"git"' not in src:
            continue
        # ⛔⛭ ** THE FIRST WRITING OF THIS PASS MATCHED ANY HEX LITERAL IN A FILE THAT USED GIT
        #    ANYWHERE, AND RETURNED 21 -- ALL OF THEM OPEN-LEDGER ROW HASHES. **  `233a615f2f` and
        #    `9921e78365` are ledger ids, not commits; `A4_the_ledger_seven_swept` is named for what
        #    it reads.  *A filter built around what I expected to find rather than what is there is
        #    the failure this corpus records at r3932, r3922 and r3906, and this sweep committed it
        #    on its own first run.*  ⇒ ** A hex literal counts only if it is actually HANDED TO GIT:
        #    on a git line itself, or through a variable that is. **
        lines = src.split('\n')
        gitlines = [i for i, ln in enumerate(lines)
                    if re.search(r"['\"]git['\"]|\bgit\(", ln)]
        near = set()
        for i in gitlines:
            for j in range(max(0, i - 2), min(len(lines), i + 3)):
                near.add(j)
        varhex = {m.group(1): m.group(2) for ln in lines
                  for m in [re.match(r"\s*([A-Z_][A-Z0-9_]*)\s*=\s*['\"]([0-9a-f]{7,40})['\"]",
                                     ln)] if m}
        handed = set()
        for i in sorted(near):
            for m in SHA.finditer(lines[i]):
                handed.add(m.group(1))
            for name, h in varhex.items():
                if re.search(r'\b' + name + r'\b', lines[i]):
                    handed.add(h)
        # ** A DEPENDENCY THAT IS DECLARED IS NOT A DEFECT. **  `R1` shows the pattern the corpus
        #    already has for this: it refuses to certify an absence unless enough commits were
        #    searched (`len(allrefs) >= 486 and not ever`).  *A receipt that guards its own SHA and
        #    exits naming the reason has stated its dependency; one that does not will fail as a
        #    mystery, or -- worse, in the Pass C direction -- pass.*
        def guarded(h):
            names = [n for n, v in varhex.items() if v == h] + [h]
            return any(re.search(r'cat-file', ln) and any(re.search(r'\b' + re.escape(n) + r'\b',
                       ln) for n in names) for ln in lines)

        for s_ in sorted(handed):
            is_commit = git('cat-file', '-e', s_ + '^{commit}').returncode == 0
            if not is_commit:
                A.append((rel, s_, 'NOT A COMMIT'))
            elif git('merge-base', '--is-ancestor', s_, 'HEAD').returncode != 0:
                A.append((rel, s_, 'guarded, not from HEAD' if guarded(s_) else 'not from HEAD'))
        verbs = set(GITCALL.findall(src))
        if verbs & {'log', 'rev-list'} and '--all' not in src:
            B.append((rel, sorted(verbs & {'log', 'rev-list'})))
        # ⛔⛭ ** THE KEYWORD NET MISSED THE SHARPEST FORM, AND THE CORPUS'S OWN RULE CAUGHT IT. **
        #    r3932: "before trusting a filter's MISSES, read three of them."  Doing that here found
        #    `D1`, which asserts `git('diff','--stat',A,B,...).strip() == ''` with no guard: ** if
        #    either commit were absent git returns the empty string and the check PASSES. **  That is
        #    the pass-because-absent failure in its purest form and no keyword appears in it.
        #    ⇒ *A vacuity test has to look for the SHAPE -- git output compared to empty -- and not
        #      for words about absence.*
        VACUOUS = re.compile(r"git\([^)]*\)[^\n]{0,40}(==\s*['\"]{2}|\.strip\(\)\s*==\s*['\"]{2}"
                             r"|==\s*0\b|len\([^)]*\)\s*==\s*0)")
        has_guard = bool(re.search(r'cat-file|shallow|>= *[0-9]{3}', src))
        for ln in lines:
            st = ln.strip()
            if st.startswith('#') or 'subprocess' in ln:
                continue
            shape = VACUOUS.search(ln)
            word = ('git' in ln or 'commit' in ln) and NEG.search(ln) and re.search(r'check\(|assert ', ln)
            if shape or word:
                C.append((rel, ('VACUOUS-SHAPE' if shape else 'keyword') +
                          ('' if has_guard else ', UNGUARDED'), st[:88]))
                break

    _unguarded = [a for a in A if 'guarded' not in a[2]]
    print(f"  PASS A — commits named and not reachable:  {len(A)}"
          f"   ({len(_unguarded)} UNGUARDED)")
    for rel, s, why in A[:20]:
        print(f"      {why:>14}  {s}  {rel}")
    print(f"\n  PASS B — HEAD-limited history walks (no --all):  {len(B)}")
    for rel, v in B[:20]:
        print(f"      {'/'.join(v):>14}  {rel}")
    _cu = [c for c in C if 'UNGUARDED' in c[1]]
    print(f"\n  PASS C — assertions that pass more easily the less history there is:  {len(C)}"
          f"   ({len(_cu)} UNGUARDED)")
    for rel, kind, ln in C[:20]:
        print(f"      [{kind}] {rel}")
        print(f"          {ln}")
    print()
    print("  " + "=" * 74)
    print(f"  A={len(A)}  B={len(B)}  C={len(C)}   over {len(fs)} receipt file(s)")
    print("  ⌗ A is a defect wherever it is non-zero.  B and C are EXPOSURE, not defect: each")
    print("    needs reading to say whether the answer would change on a whole history.")
    print("  " + "=" * 74)
    return 1 if _unguarded else 0


if __name__ == '__main__':
    sys.exit(main())
