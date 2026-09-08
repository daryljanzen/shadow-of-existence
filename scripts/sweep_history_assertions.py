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

  D  BASELINES READ AT A PINNED COMMIT AND USED AS A BOUND.  *`git show <SHA>:path` on a clone that
     cannot reach `<SHA>` returns THE EMPTY STRING, and a baseline of zero is a bound nothing can
     fail.*  ** This pass was written because reading Pass B's four found one ** -- `P1`, whose
     `n_now >= n_before` is the REPAIR (r3108) for a baseline that had gone degenerate against a
     moving HEAD.  *The fix for one horizon defect introduced another.*  It is reported at two
     scopes, because they are different facts: the ASSERTION is vacuous, and the FILE may still
     fail loudly somewhere else -- which is protection, but protection that names the wrong cause.

  C  NEGATIVE ASSERTIONS OVER HISTORY.  A check that asserts something is ABSENT from history
     passes MORE easily the less history there is.  ** This is the direction that is invisible from
     a short clone ** -- N1's TESTIMONY seed (r4132) passed on a shallow clone precisely because the
     ids it should have named were beyond the horizon.

Run:  python3 scripts/sweep_history_assertions.py
"""
import ast
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


# ======================================================================================
# ** PASS D -- and it took THREE writings of a filter to get here. **
#   The first Pass D joined continuation lines by counting brackets, and `len(re.findall(r'\bcheck\(',
#   src))` has an unbalanced `\(` INSIDE A STRING, so the counter never closed and swallowed the rest
#   of the function.  *`P1`, the very file that motivated the pass, was invisible to it.*  ⇒ The
#   structure is read with `ast`, which is the only thing that knows a paren in a string is not a
#   paren.  ** That is three filters in this one sweep that failed the way the sweep is looking for. **
# ======================================================================================
def _names(node):
    return {x.id for x in ast.walk(node) if isinstance(x, ast.Name)}


def _pinned_and_derived(tree, src):
    """names holding a read AT A NAMED REVISION, and everything computed from them"""
    seg = lambda n: (ast.get_source_segment(src, n) or '')
    assigns = [n for n in ast.walk(tree) if isinstance(n, ast.Assign)]
    d = set()
    for n in assigns:
        t = seg(n.value)
        if re.search(r"['\"]show['\"]", t) and ':' in t:
            for tg in n.targets:
                d |= _names(tg)
    for _ in range(4):                       # transitive closure, cheap and bounded
        for n in assigns:
            if _names(n.value) & d:
                for tg in n.targets:
                    d |= _names(tg)
    return d


def _loud(expr, d, want=None):
    """does this expression contain a term that FAILS when the pinned read came back empty?

    ** `want` narrows it to a term over THOSE names. **  *A file that fails loudly somewhere is
    protected; a baseline whose OWN name is pinned by a positive control is GUARDED, and the
    difference is whether the failure says "the horizon" or says something else.*
    """
    d = d & want if want is not None else d
    if not d:
        return False
    for c in ast.walk(expr):
        if not isinstance(c, ast.Compare) or not c.ops:
            continue
        op, L, R = c.ops[0], c.left, c.comparators[0]
        if isinstance(op, ast.In) and _names(R) & d:
            return True                      # a needle sought IN the read -- empty fails
        if isinstance(op, ast.Eq) and (_names(L) | _names(R)) & d:
            other = R if _names(L) & d else L
            if not (isinstance(other, ast.Constant) and other.value in (0, '', None)):
                return True                  # pinned to an exact non-empty value
        if isinstance(op, (ast.Gt, ast.GtE)) and _names(L) & d and not _names(R) & d:
            return True                      # the read itself must be big enough
        if isinstance(op, (ast.Lt, ast.LtE)) and _names(R) & d and not _names(L) & d:
            return True
    return False


def _conds(tree):
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'check' \
                and len(n.args) >= 2:
            yield n.args[-1]
        elif isinstance(n, ast.Assert):
            yield n.test


def pass_d(src):
    """-> list of (vacuous-bound source, file-fails-loudly-elsewhere)"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    seg = lambda n: (ast.get_source_segment(src, n) or '')
    d = _pinned_and_derived(tree, src)
    if not d:
        return []
    conds = list(_conds(tree))
    elsewhere = any(_loud(c, d) for c in conds)
    out = []
    for cond in conds:
        if _loud(cond, d):
            continue
        for c in ast.walk(cond):
            if not isinstance(c, ast.Compare) or not c.ops:
                continue
            op, L, R = c.ops[0], c.left, c.comparators[0]
            vac = ((isinstance(op, (ast.GtE, ast.Gt)) and _names(R) & d)
                   or (isinstance(op, (ast.LtE, ast.Lt)) and _names(L) & d))
            if vac:
                side = R if isinstance(op, (ast.GtE, ast.Gt)) else L
                own = _names(side) & d
                on_baseline = any(o is not cond and _loud(o, d, want=own) for o in conds)
                out.append((' '.join(seg(c).split())[:88],
                            'own baseline' if on_baseline else
                            ('elsewhere' if elsewhere else None)))
                break
    return out


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
    A, B, C, D = [], [], [], []
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
        for _vac, _loudly in pass_d(src):
            D.append((rel, _vac, _loudly))

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
    _dl = [d for d in D if d[2] is None]
    _dw = [d for d in D if d[2] == 'elsewhere']
    print(f"\n  PASS D — baselines read at a pinned commit and used as a BOUND:  {len(D)}"
          f"   ({len(_dl)} with nothing loud anywhere, {len(_dw)} loud only about something else)")
    _WHY = {'own baseline': 'guarded ON ITS OWN BASELINE',
            'elsewhere': 'file fails loudly, about SOMETHING ELSE',
            None: 'NOTHING LOUD IN FILE'}
    for rel, vac, loudly in D[:20]:
        print(f"      [{_WHY[loudly]}] {rel}")
        print(f"          {vac}")
    print()
    print("  " + "=" * 74)
    print(f"  A={len(A)}  B={len(B)}  C={len(C)}  D={len(D)}   over {len(fs)} receipt file(s)")
    print("  ⌗ A is a defect wherever it is non-zero.  B, C and D are EXPOSURE, not defect: each")
    print("    needs reading to say whether the answer would change on a whole history.")
    print("  ⌗ A PASS-D HIT IS AN ASSERTION-LEVEL FACT.  'file fails loudly elsewhere' means the")
    print("    receipt does not go green on a short clone -- but it fails at a check about something")
    print("    else, so the failure names the wrong cause.  That is protection, not a guard.")
    print("  " + "=" * 74)
    return 1 if _unguarded else 0


if __name__ == '__main__':
    sys.exit(main())
