#!/usr/bin/env python3
"""r7400 (60) -- THE CONTAINER FROM THE KEY'S OWN TRACE, and how many more dead pins a container-keyed
test finds than a repo-wide one.  Six arms, all registered in `PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ 870 of 1161 (300-1100),
⒝ 40 (5-300), ⒞ 60 (10-300), ⒟ 75 % of ⒞ (40-100 %), ⒠ exact 0 violations, ⒡ 60 s (10-600 s).

⛭ EVERY FIELD COMES FROM THE INSTRUMENT THAT OWNS IT (`r7367` ④'s remedy).  The key, target, tier and
verdict are read from `corpus/quote_pin_baseline.tsv` the way the GATE keys it -- the literal column as
JSON, never raw (`r7365+cc66.38` ⒢).  The read trace is `mutate_assertions.quote()`'s own wide trace,
reached by substituting its extension pattern IN THIS PROCESS ONLY so the whole path token is captured
instead of the bare kind; nothing on disk is edited.  ⛭⛭ And the presence test is
`check_quote_pins._present_at` ITSELF, CALLED AND NOT REIMPLEMENTED: its file list is replaced with the
containers the key's own trace names, by intercepting the one `git grep` it uses to build that list.

⌗ The module level is CHEAP -- the ledger, the tree at `FRAME`, the resolver -- so a receipt can import
it for the resolver and the frame without running the sweep.  The sweep is in `main()`.

    python3 -I cost.py            # the whole SOURCE half
    python3 -I cost.py --limit N  # the first N rows, to price a sample
"""
import argparse
import ast
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter

# the commit that registered PREDICTION.md, BEFORE this ran.  Every container is read AT this commit
# (r7368 ②: a claim about a historical state is read at a pin, never live), and `main` asserts it is an
# ancestor of HEAD and reports whether the `receipts/` tree the trace is parsed from has moved since.
FRAME = '15f27418'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

# the archetype, named rather than remembered: `S17` reached its container as `COMP = tsv('COMPARISON.tsv')`
# with `tsv(name) = open(os.path.join(DIR, name))` and `DIR` a module constant -- a basename literal in the
# trace joined to a directory bound in the same receipt.
ARCHETYPE_DIR = 'computations/beyond_the_wall/r7254_60_mirror_cross_read'
ARCHETYPE = ARCHETYPE_DIR + '/COMPARISON.tsv'
ARCHETYPE_RECEIPT = ('receipts/L_probability/S17_the_cross_read_leaves_six_of_twenty_seven_open_and_all_six'
                     '_are_identity_pins_so_the_residual_is_one_missing_clause_and_not_two_instruments.py')
_KINDS = r'tex|py|md|json|tsv|txt|csv|ya?ml|log'
# the substitute for the instrument's own `_EXT`: the same kinds, with the whole path-shaped token captured
PATHTOK = re.compile(r'([\w./\-]*\.(?:' + _KINDS + r'))\b')


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, path))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


Q = load('corpus/check_quote_pins.py', 'r7400_quote_gate')
M = load('scripts/mutate_assertions.py', 'r7400_mint')
FULL = git('rev-parse', FRAME).strip()


# ===================================================================== the keys, from the ledger the gate reads
def ledger(sha=None):
    """(receipt, lit, target, tier, verdict) for every row, keyed as the GATE keys it, read AT THE FRAME.
    ⛭ r7368 ②: a census is a measurement at a commit, so the population is read at the pin and never
    live -- otherwise every figure here moves the moment any seat registers a key, this revision's own
    registration pass included."""
    out = []
    for ln in git('show', f'{sha or FULL}:corpus/quote_pin_baseline.tsv').split('\n'):
        if '\t' not in ln or ln.startswith('#'):
            continue
        c = ln.split('\t')
        if len(c) < 6:
            continue
        try:
            lit = json.loads(c[1])
        except ValueError:
            continue
        out.append((c[0], ' '.join(lit.split()), c[2], c[3], c[5]))
    return out


# ============================================= the trace, from the instrument, with the PATH captured not the kind
def trace_names():
    """{(receipt, lit): {named path token}} -- the instrument's own wide trace, with `_EXT` substituted in
    THIS PROCESS so `_kinds` carries the NAMES the trace mentions instead of the bare kinds.  The text
    searched is byte-for-byte the wide trace `_rstar` files kinds from, so this cannot see a name the
    instrument's own filing cannot."""
    was = M._EXT
    M._EXT = PATHTOK
    try:
        rows = M.quote(ROOT)
    finally:
        M._EXT = was
    named = {}
    for r in rows:
        named.setdefault((r['receipt'], r['lit']), set()).update(r['_kinds'])
    return named, len(rows)


# ===================================================================================== the tree AT the frame
TREE = [p for p in git('ls-tree', '-r', '--name-only', FULL).split('\n') if p]
TREESET = set(TREE)
BYBASE = {}
for _p in TREE:
    BYBASE.setdefault(os.path.basename(_p), []).append(_p)
DIRS = {os.path.dirname(p) for p in TREE}


# ================================================== the receipt's OWN directory constants, folded from its AST
def fold(src):
    """every module-level name in `src` that folds to a path string: a constant, an `os.path.join` of folded
    parts, or an `os.path.dirname`/`abspath` chain.  A part that is the repo root contributes nothing, so the
    result is root-relative, which is how the tree is keyed.  Nothing is executed; this is a fold over the
    syntax tree, so a receipt that cannot be imported is still read."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {}
    env, out = {}, {}

    def f(n, d=4):
        if d <= 0:
            return None
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            return n.value
        if isinstance(n, ast.Name):
            return env.get(n.id)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if n.func.attr == 'join':
                parts = [f(a, d - 1) for a in n.args]
                if any(p is None for p in parts):
                    return None
                return os.path.normpath('/'.join(p.strip('/') for p in parts if p.strip('/'))) or ''
            if n.func.attr in ('dirname', 'abspath', 'realpath'):
                return ''
        return None

    for n in ast.walk(tree):
        tg = None
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            tg = n.targets[0].id
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name):
            tg = n.target.id
        if tg:
            v = f(n.value)
            if v is not None:
                env[tg] = v
                out[tg] = v
    return out


_DIR_CACHE = {}


def receipt_dirs(receipt):
    """the directories the receipt ITSELF binds, as they exist in the tree at FRAME"""
    if receipt not in _DIR_CACHE:
        p = os.path.join(ROOT, receipt)
        src = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
        _DIR_CACHE[receipt] = sorted({v for v in fold(src).values() if v and v in DIRS})
    return _DIR_CACHE[receipt]


# ===================================================================================== container resolution
def resolve(receipt, token):
    """(paths, how) for one named token.  `how` is PATH (the token is a path in the tree, or a unique suffix
    of one), BASE (a bare basename, unique repo-wide), DIR (a bare basename resolved against a directory the
    RECEIPT ITSELF binds -- the arm ⒝ is about), or '' when nothing resolves.  A receipt is never its own
    container, which is `_present_at`'s own rule (text `from a file it does not own`)."""
    tok = token.strip('./')
    if not tok or tok.startswith('.'):
        return [], ''
    if '/' in tok:
        hits = [tok] if tok in TREESET else [p for p in TREE if p.endswith('/' + tok)]
        hits = [p for p in hits if p != receipt]
        return (hits, 'PATH') if len(hits) == 1 else ([], '')
    wide = [p for p in BYBASE.get(tok, []) if p != receipt]
    if len(wide) == 1:
        return wide, 'BASE'
    here = sorted({os.path.join(d, tok) for d in receipt_dirs(receipt)} & TREESET - {receipt})
    return (here, 'DIR') if here else ([], '')


def containers(receipt, toks):
    """(sorted containers, sorted hows) over every token the key's trace named"""
    got, hows = [], []
    for tk in sorted(toks):
        ps, h = resolve(receipt, tk)
        if ps:
            got += ps
            hows.append(h)
    return sorted(set(got)), sorted(set(hows))


# ============================================ H3 against the containers: `_present_at` itself, file list replaced
class _R:
    def __init__(self, out):
        self.stdout, self.stderr, self.returncode = out, '', 0


def present_in(lit, receipt, conts, sha=None):
    """`_present_at` unchanged, with the one `git grep` that builds its file list intercepted so the list is
    the key's own containers.  Everything else -- the raw arm, the regex arm, `_unmark` on both sides, the
    `git show` cache at the frame -- is the gate's, called and not reimplemented."""
    at = sha or FULL
    real = Q._git

    def fake(*a):
        if a and a[0] == 'grep':
            return _R('\n'.join(f'{at}:{c}' for c in conts))
        return real(*a)
    Q._git = fake
    try:
        return Q._present_at(at, lit, 'SOURCE', receipt)
    finally:
        Q._git = real


def present_repo_wide(lit, receipt, sha=None):
    """`_present_at` as it stands: anywhere in the repo but this receipt -- the test `cc66` found invalid"""
    return Q._present_at(sha or FULL, lit, 'SOURCE', receipt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--sample', type=int, default=50,
                    help='⒠ii: present-in-container keys confirmed present repo-wide')
    a = ap.parse_args()

    head = git('rev-parse', 'HEAD').strip()
    moved = [f for f in git('diff', '--name-only', f'{FULL}..HEAD').split() if f.startswith('receipts/')]
    base = ledger()
    src = [r for r in base if r[2] == 'SOURCE']
    if a.limit:
        src = src[:a.limit]

    t_mint = time.time()
    named, nsite = trace_names()
    t_mint = time.time() - t_mint

    print(f'# r7400 (60) -- the container from the key\'s own trace, at FRAME {FULL[:12]}')
    print(f'# HEAD {head[:12]}; receipts/ files changed since the frame: {len(moved)}')
    print(f'# the mint ran in {t_mint:.1f}s and reported {nsite} site(s); '
          f'{len(base)} ledger row(s), {len(src)} with target SOURCE')
    print(f'# the archetype: {ARCHETYPE}')

    t0 = time.time()
    cls, cof, hof = Counter(), {}, {}
    for receipt, lit, target, tier, verdict in src:
        toks = named.get((receipt, lit), set())
        got, hows = containers(receipt, toks)
        cof[(receipt, lit)], hof[(receipt, lit)] = got, hows
        cls['NO-NAME' if not toks else ('RESOLVED' if got else 'NAMED-UNRESOLVED')] += 1
    t_res = time.time() - t0

    resolved = [r for r in src if cof[(r[0], r[1])]]
    dironly = [r for r in resolved if hof[(r[0], r[1])] == ['DIR']]
    dirany = [r for r in resolved if 'DIR' in hof[(r[0], r[1])]]

    print()
    print(f'# ⒜ RESOLVABLE CONTAINER        {cls["RESOLVED"]:5d} of {len(src)}   (band 300-1100, central 870)')
    print(f'#    named a file, none resolved {cls["NAMED-UNRESOLVED"]:5d}')
    print(f'#    named no file at all        {cls["NO-NAME"]:5d}')
    print(f'# ⒝ ONLY via the receipt\'s own directory constants  {len(dironly):5d}   (band 5-300, central 40)')
    print(f'#    any site resolved that way                     {len(dirany):5d}')
    print('#    how, over resolved keys    :', dict(Counter(tuple(hof[(r[0], r[1])]) for r in resolved)))
    print(f'#    containers per key         : {Counter(len(cof[(r[0], r[1])]) for r in resolved).most_common(6)}')

    t0 = time.time()
    absent = [(r[0], r[1], r[3], r[4]) for r in resolved if not present_in(r[1], r[0], cof[(r[0], r[1])])]
    t_abs = time.time() - t0
    print()
    print(f'# ⒞ ABSENT FROM EVERY RESOLVED CONTAINER  {len(absent):5d} of {len(resolved)} resolved '
          f'= {100 * len(absent) / max(1, len(resolved)):.1f} %   (band 10-300, central 60)')
    print('#    by verdict :', dict(Counter(x[3] for x in absent)))
    print('#    by tier    :', dict(Counter(x[2] for x in absent)))
    print('# ⌗ CANDIDATES, NOT VERDICTS: the green-receipt filter is r7371 ③\'s other half and is NOT')
    print('#   applied, exactly as cc66 reported for the PAPER half.  ⒞ is an UPPER BOUND, reported as one.')
    mine = [x for x in absent if 'S60_the_container' in x[0]]
    print(f'# ⌗ SELF-INSTANCE (r7398\'s rule): {len(mine)} of ⒞ are this revision\'s own receipt; '
          f'⒞ without them is {len(absent) - len(mine)}')

    t0 = time.time()
    gap = [x for x in absent if present_repo_wide(x[1], x[0])]
    t_gap = time.time() - t0
    gapset = {(x[0], x[1]) for x in gap}
    print()
    print(f'# ⒟ OF ⒞, REPORTED PRESENT REPO-WIDE      {len(gap):5d} of {len(absent)} '
          f'= {100 * len(gap) / max(1, len(absent)):.1f} %   (band 40-100 %, central 75 %)')
    print('#    ⇒ these are the dead pins `_present_at`\'s SOURCE branch CANNOT SEE, which is the figure')
    print('#      "how many more dead pins would the mint find" asks for.')
    print('#    by verdict :', dict(Counter(x[3] for x in gap)))

    viol_i = [(r[0], c) for r in resolved for c in cof[(r[0], r[1])] if c == r[0]]
    t0 = time.time()
    keep = {(x[0], x[1]) for x in absent}
    sample = [r for r in resolved if (r[0], r[1]) not in keep][:a.sample]
    viol_ii = [(r[0], r[1][:40]) for r in sample if not present_repo_wide(r[1], r[0])]
    t_snd = time.time() - t0
    print()
    print('# ⒠ SOUNDNESS, point prediction 0')
    print(f'#    i  a container that IS its own receipt                              {len(viol_i)}')
    print(f'#    ii of {len(sample)} present-in-container keys, reported ABSENT repo-wide  {len(viol_ii)}')
    for v in viol_i[:5] + viol_ii[:5]:
        print('#      ⛔', v)

    print()
    print(f'# ⒡ PRICE on this container, {len(src)} SOURCE row(s)   (band 10-600 s, central 60 s)')
    print(f'#    the mint (the trace)        {t_mint:8.1f}s')
    print(f'#    container resolution        {t_res:8.1f}s')
    print(f'#    ⒞ H3 against the containers {t_abs:8.1f}s  = {t_abs / max(1, len(resolved)):.4f}s a row')
    print(f'#    ⇒ THE CENSUS ITSELF         {t_mint + t_res + t_abs:8.1f}s')
    print(f'#    ⒟ repo-wide, {len(absent)} candidate(s)  {t_gap:8.1f}s  '
          f'= {t_gap / max(1, len(absent)):.3f}s a row  [priced APART, run over ⒞ only]')
    print(f'#    ⒠ii sample, {len(sample)} row(s)         {t_snd:8.1f}s')

    print()
    print('# ⒞ in full: receipt, literal (JSON), tier, verdict, container(s), how, repo-wide reading')
    for x in sorted(absent):
        k = (x[0], x[1])
        print('\t'.join((x[0], json.dumps(x[1], ensure_ascii=False), x[2], x[3], ';'.join(cof[k]),
                         ','.join(hof[k]), 'PRESENT-REPO-WIDE' if k in gapset else 'ABSENT-REPO-WIDE')))


if __name__ == '__main__':
    main()
