#!/usr/bin/env python3
"""r7440 (60) -- A PINNED CLAIM TESTED AT A FRAME IS A DIFFERENT CLAIM.  Six arms, registered in
PREDICTION.md at `e6ad17b6` before this ran.  `r7439` ⑤ is the order.

TWO REPAIRS, both in THIS measurement layer and neither in another seat's instrument:

  ⒜ TEMPLATE  -- an f-string is an `ast.JoinedStr`; the text the extractor harvested from its SOURCE is a
                 skeleton and not anything's assertion target.  Such keys leave the literal population.
  ⒝ PIN       -- where a receipt resolves its containers at a commit (a module-level commit-like constant
                 passed first to an `at` / `at_many` / `tree_of` / `_at` call), BOTH the container
                 resolution AND the presence test are done at THAT commit.

⛔ The presence test is still `check_quote_pins._present_at` itself, through `cost.present_in`, called and
not reimplemented -- only the tree it reads and the file list it is given change.

    python3 -I pinned.py
"""
import ast
import json
import os
import subprocess
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R7400 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7400_60_the_container_from_the_keys_own_trace')
sys.path.insert(0, R7400)
import cost as C                                            # noqa: E402

AT_CALLS = {'at', 'at_many', 'tree_of', '_at'}
# r7439's own table: the control, supplied by the party that overturned r7438's finding
R7439_TABLE = {
    'STAMP': ('S2', 'S3', 'S4'),
    'TARGETS = sorted({r[0] for r in MINE})': ('S2',),
    '_all_bodies.count(RETIRED) == 0': ('S6',),
    'len(_removed) == 1 and len(_added) == 8': ('S6',),
    'def shadow_run(': ('S5', 'S6'),
    'for f in PROBE': ('S5',),
}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def _src(receipt, sha=None):
    if sha:
        return git('show', f'{sha}:{receipt}')
    p = os.path.join(ROOT, receipt)
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


# ──────────────────────────────────────────────────────────── ⒜ the template skeletons a receipt contains
def templates(receipt):
    """the format-string SKELETONS of every f-string in the receipt -- literal parts joined by `{}`, which
    is what an extractor reading the SOURCE harvests.  ⛔ These are not assertion targets: nothing in any
    file is asserted to contain them, so a key whose literal IS one is a TEMPLATE and not a literal."""
    try:
        tree = ast.parse(_src(receipt))
    except (SyntaxError, ValueError):
        return set()
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.JoinedStr):
            sk = ''.join(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str) else '{}'
                         for v in n.values)
            if sk.strip():
                out.add(' '.join(sk.split()))
    return out


# ───────────────────────────────────────────────────────────────── ⒝ the commit a receipt reads its tree at
def pin_of(receipt, sha=None):
    """(commit, name) when the receipt resolves its containers AT A COMMIT, else (None, None).

    BY SHAPE, NOT BY A HAND LIST: a module-level assignment of a commit-like string, which is then passed
    as the FIRST POSITIONAL ARGUMENT of a call to `at` / `at_many` / `tree_of` / `_at`.  A hand list would
    pass this revision's arm and miss the next receipt that adopts the practice."""
    try:
        tree = ast.parse(_src(receipt, sha))
    except (SyntaxError, ValueError):
        return None, None
    consts = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Constant) \
                and isinstance(n.value.value, str):
            v = n.value.value
            if 7 <= len(v) <= 40 and all(c in '0123456789abcdef' for c in v):
                for t in n.targets:
                    if isinstance(t, ast.Name):
                        consts[t.id] = v
    if not consts:
        return None, None
    used = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and n.args:
            fn = n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, 'id', None)
            a0 = n.args[0]
            if fn in AT_CALLS and isinstance(a0, ast.Name) and a0.id in consts:
                used.append(a0.id)
    if not used:
        return None, None
    name = Counter(used).most_common(1)[0][0]
    return consts[name], name


# ─────────────────────────────────────────── resolving and testing AT a commit, through cost's own resolver
def _tree_at(sha):
    return [p for p in git('ls-tree', '-r', '--name-only', sha).split('\n') if p]


def resolve_at(sha, receipt, toks):
    """the AMBIGUOUS candidates of each token, resolved against the tree AT `sha` rather than at the frame.
    `receipt_dirs` is fed from the receipt's own source AT `sha` too, so the DIR route is not read live."""
    paths = _tree_at(sha)
    binds = {receipt: sorted({v for v in C.fold(_src(receipt, sha)).values()
                              if v and v in {os.path.dirname(p) for p in paths}})}
    cands = set()
    with C._tree(paths, binds=binds):
        for tk in sorted(toks):
            r = C.resolution(receipt, tk)
            if r.state == C.AMBIGUOUS:
                cands.update(r.candidates)
            elif r.state == C.RESOLVED:
                cands.update(r.paths)
    return sorted(cands)


def main():
    t0 = time.time()
    print('=' * 100)
    print('  r7440 -- A PINNED CLAIM TESTED AT A FRAME IS A DIFFERENT CLAIM')
    print(f'  the frame is still r7400\'s {C.FRAME} ({C.FULL[:9]}); a PINNED receipt is read at ITS pin')
    print('=' * 100)

    named, _ = C.trace_names()
    rows = C.ledger()
    half = {(r[0], r[1]): r[2] for r in rows}
    verdict = {(r[0], r[1]): r[4] for r in rows}

    # the r7438 population, re-derived
    hidden = {}
    for key, toks in named.items():
        res = {tk: C.resolution(key[0], tk) for tk in toks}
        if any(r.state == C.RESOLVED for r in res.values()):
            continue
        cands = sorted({p for r in res.values() if r.state == C.AMBIGUOUS for p in r.candidates})
        if cands:
            hidden[key] = cands
    print(f'\n  ⓪ THE r7438 POPULATION, RE-DERIVED: {len(hidden)} keys, '
          f'halves {dict(Counter(half.get(k, "?") for k in hidden))}')

    # ── ⒜ templates ──────────────────────────────────────────────────────────────────────────────────
    print('\n  ⓵ ⒜ THE TEMPLATES LEAVE THE LITERAL POPULATION')
    tmpl_cache, tmpl_keys = {}, []
    for key in sorted(hidden):
        rc, lit = key
        if rc not in tmpl_cache:
            tmpl_cache[rc] = templates(rc)
        if lit in tmpl_cache[rc]:
            tmpl_keys.append(key)
    print(f'      keys in the r7438 population whose literal IS an f-string skeleton : {len(tmpl_keys)}')
    for k in tmpl_keys:
        print(f'        {k[1]!r}')
        print(f'          in {k[0].split("/")[-1][:62]}')
    allkeys = sorted(named)
    tmpl_all = []
    for key in allkeys:
        rc, lit = key
        if rc not in tmpl_cache:
            tmpl_cache[rc] = templates(rc)
        if lit in tmpl_cache[rc]:
            tmpl_all.append(key)
    print(f'      and corpus-wide over all {len(allkeys)} traced keys                       : '
          f'{len(tmpl_all)}')

    # ── ⒝ pins by shape ──────────────────────────────────────────────────────────────────────────────
    print('\n  ⓶ ⒝ PIN-BEARING RECEIPTS, DETECTED BY SHAPE')
    receipts = sorted({k[0] for k in hidden})
    pins = {}
    for rc in receipts:
        p, nm = pin_of(rc)
        if p:
            pins[rc] = (p, nm)
    print(f'      receipts in the population                 : {len(receipts)}')
    print(f'      of them resolving their containers AT A PIN : {len(pins)}')
    for rc, (p, nm) in sorted(pins.items()):
        print(f'        {nm} = {p}   in {rc.split("/")[-1][:58]}')
    all_rc = sorted({k[0] for k in allkeys})
    pins_all = {rc: pin_of(rc) for rc in all_rc}
    pins_all = {rc: v for rc, v in pins_all.items() if v[0]}
    print(f'      and corpus-wide over {len(all_rc)} traced receipts     : {len(pins_all)}')

    # ── ⒠ the control FIRST: r7439's own table ───────────────────────────────────────────────────────
    print('\n  ⓷ ⒠ THE CONTROL — r7439\'s OWN TABLE, REPRODUCED OR NOT')
    s10 = [rc for rc in pins if 'S10_the_sweep_for_exact_counts' in rc]
    ctl_ok, ctl_bad = 0, []
    if s10:
        rc = s10[0]
        pin = pins[rc][0]
        at_paths = _tree_at(pin)
        for lit, want in sorted(R7439_TABLE.items()):
            holders = [p for p in at_paths
                       if p.startswith('receipts/L_probability/') and p != rc
                       and lit in git('show', f'{pin}:{p}')]
            stems = sorted({os.path.basename(p).split('_')[0] for p in holders})
            good = all(w in stems for w in want)
            print(f'      {"OK   " if good else "⛔   "} {lit!r}')
            print(f'             expected {list(want)}, found {stems or "(none)"}')
            ctl_ok += 1 if good else 0
            if not good:
                ctl_bad.append(lit)
    else:
        print('      ⛔ S10 was not detected as pin-bearing — the control cannot run')
    print(f'      ⇒ {ctl_ok} of {len(R7439_TABLE)} reproduced'
          f'{"" if not ctl_bad else "  MISSING: " + str(ctl_bad)}')

    # ── ⒞ / ⒟ the re-run ─────────────────────────────────────────────────────────────────────────────
    print('\n  ⓸ ⒞⒟ THE RE-RUN, WITH BOTH REPAIRS IN')
    t1 = time.time()
    present, absent, skipped = [], [], []
    moved_to_absent, moved_to_present = [], []
    for key in sorted(hidden):
        rc, lit = key
        if key in tmpl_keys:
            skipped.append(key)
            continue
        pin = pins.get(rc, (None, None))[0]
        if pin:
            cands = resolve_at(pin, rc, named[key])
            ok = bool(cands) and C.present_in(lit, rc, cands, sha=pin)
        else:
            cands = hidden[key]
            ok = C.present_in(lit, rc, cands)
        was = C.present_in(lit, rc, hidden[key])          # what r7438 said, recomputed here
        (present if ok else absent).append(key)
        if was and not ok:
            moved_to_absent.append(key)
        if ok and not was:
            moved_to_present.append(key)
    t_test = time.time() - t1
    print(f'      excluded as TEMPLATE                : {len(skipped)}')
    print(f'      present in at least one candidate   : {len(present)}')
    print(f'      ABSENT from every candidate         : {len(absent)}')
    print(f'      ⇒ r7438 said 7 absent; this says {len(absent)}')
    print(f'      verdicts moved PRESENT -> ABSENT    : {len(moved_to_absent)}')
    print(f'      verdicts moved ABSENT  -> PRESENT   : {len(moved_to_present)}')
    print(f'      ⌗ the second column is the direction r7439 predicted; the FIRST is the one the order')
    print(f'        did not claim and PREDICTION.md registered as possible, because a literal present at')
    print(f'        the frame may postdate the pin.')
    if absent:
        print('      the survivors:')
        for k in absent:
            print(f'        {verdict.get(k, "?"):12} {k[1]!r}')
            print(f'                     in {k[0].split("/")[-1][:60]}')
    print(f'\n      ⒟ r7438\'s 100 present, re-measured through both repairs: '
          f'{len(present)} + {len(skipped)} excluded = {len(present) + len(skipped)} of {len(hidden)}')

    out = os.path.join(HERE, 'rerun.tsv')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('# receipt\tliteral(json)\tverdict\tpin\tstate\n')
        for k in sorted(hidden):
            st = ('TEMPLATE' if k in skipped else ('PRESENT' if k in present else 'ABSENT'))
            fh.write('\t'.join((k[0], json.dumps(k[1]), verdict.get(k, '?'),
                               pins.get(k[0], ('', ''))[0] or '-', st)) + '\n')

    print('\n  ⓹ ⒡ THE PRICE')
    print(f'      the presence test over {len(hidden)} keys : {t_test:.1f} s')
    print(f'      the whole run                              : {time.time() - t0:.1f} s')
    print(f'      r7438\'s whole run, for comparison          : 43.6 s')
    print('\n' + '=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
