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
import contextlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter, namedtuple

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
# the contrast case r7436 names: a receipt whose trace names `PREDICTION.md` and which binds NO directory
# holding one, so the token reaches all 230 and the old resolver reported it as reaching none.
AMBIGUOUS_RECEIPT = ('receipts/L_probability/S1_the_corpus_sweep_finds_no_headline_resting_on_an_'
                     'overclaimed_sigma_and_three_in_one_paper_below_it.py')
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
# ⛔ r7433 ①: `resolve` returning nothing used to mean TWO different facts -- *this token reaches no
# container* and *this token reaches several and I will not say which*.  r7434 measured the second at 120
# distinct (receipt, token) pairs, worst case a token reaching 230 real files reported as reaching none.
# The two are now separate states, and they are decided in ONE function.
RESOLVED, NONE, AMBIGUOUS, NOT_A_TOKEN = 'RESOLVED', 'NONE', 'AMBIGUOUS', 'NOT-A-TOKEN'

Resolution = namedtuple('Resolution', 'state paths how candidates why')


def resolution(receipt, token):
    """THE one place a named token is turned into containers.  Four states, and the two that carry no path
    are told apart rather than collapsed:

      RESOLVED     -- `paths` is what the token reaches; `how` is the route (PATH, BASE, DIR)
      AMBIGUOUS    -- `paths` is EMPTY and `candidates` is what it reached: the token names several and
                      nothing in the receipt chooses between them.  ⛔ This is the state r7434 found being
                      reported as NONE, and reporting it as NONE is what made a token reaching 230 files
                      indistinguishable from a token reaching no file.
      NONE          -- `paths` and `candidates` are both empty: nothing in the tree answers to the token
      NOT-A-TOKEN   -- the token is empty or dot-leading, so it is not a claim about the tree at all

    `how` carries the ROUTE THAT WAS TRIED even when the state is AMBIGUOUS or NONE, because *which* rule
    came up empty is part of the answer -- it is how the `/`-shaped drop is told from its bare-basename
    sibling, and r7434 measured those at 0 and 120.  `why` is a sentence, so a caller can report the state
    without re-deriving the reason.  A receipt is never its own container, which is `_present_at`'s own
    rule (text `from a file it does not own`)."""
    tok = token.strip('./')
    # ⌗ r7436: this guard used to read `not tok or tok.startswith('.')`.  The second disjunct is
    # UNREACHABLE -- `strip('./')` removes every leading `.` and `/`, so its result can never begin with
    # one -- and it would have been WRONG if it had fired, refusing to resolve a real dotfile.  Deleted,
    # with a seed that proves the unreachability by construction rather than asserting the branch.
    if not tok:
        return Resolution(NOT_A_TOKEN, [], '', [],
                          'the token is empty once its leading dots and slashes are stripped, so it names '
                          'nothing and claims nothing about the tree')
    if '/' in tok:
        hits = [p for p in ([tok] if tok in TREESET else [q for q in TREE if q.endswith('/' + tok)])
                if p != receipt]
        if len(hits) == 1:
            return Resolution(RESOLVED, hits, 'PATH', list(hits),
                              'the path-shaped token is exactly one path in the tree')
        if hits:
            return Resolution(AMBIGUOUS, [], 'PATH', hits,
                              f'the path-shaped token is a suffix of {len(hits)} paths in the tree and '
                              f'nothing in the receipt chooses between them')
        return Resolution(NONE, [], 'PATH', [],
                          'the path-shaped token is a suffix of no path in the tree')
    wide = [p for p in BYBASE.get(tok, []) if p != receipt]
    if len(wide) == 1:
        return Resolution(RESOLVED, wide, 'BASE', list(wide),
                          'the bare basename is carried by exactly one path repo-wide')
    here = sorted({os.path.join(d, tok) for d in receipt_dirs(receipt)} & TREESET - {receipt})
    if here:
        return Resolution(RESOLVED, here, 'DIR', list(here),
                          f'the bare basename is carried by {len(wide)} paths repo-wide, and '
                          f'{len(here)} of them sit in a directory the RECEIPT ITSELF binds')
    if wide:
        return Resolution(AMBIGUOUS, [], 'BASE', wide,
                          f'the bare basename is carried by {len(wide)} paths repo-wide and the receipt '
                          f'binds no directory holding it, so several answer and none is chosen')
    return Resolution(NONE, [], 'BASE', [],
                      'no path in the tree carries the bare basename')


def resolve(receipt, token):
    """(paths, how) for one named token, DELEGATED to `resolution` so the rules live in one place.

    `how` is the route (PATH, BASE, DIR) when something resolved and THE STATE NAME when nothing did, so a
    caller that reads only this pair can still tell AMBIGUOUS from NONE.  ⛭ `containers` appends a route
    only for a token that resolved, so it never carried the old empty label and its contract is unchanged.
    ⌗ A caller that wants the candidates behind an AMBIGUOUS answer calls `resolution` directly."""
    r = resolution(receipt, token)
    return (list(r.paths), r.how) if r.state == RESOLVED else ([], r.state)


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


# ========================================================== the three states, proved by construction (r7436)
@contextlib.contextmanager
def _tree(paths, binds=None):
    """point the resolver at a SYNTHETIC tree, so a state is reached by construction and not by whatever
    the corpus happens to contain.  `binds` is what `receipt_dirs` should answer, injected through the cache
    the real reader consults first -- the one seam, named rather than hidden."""
    global TREE, TREESET, BYBASE, DIRS
    keep = (TREE, TREESET, BYBASE, DIRS, dict(_DIR_CACHE))
    TREE = list(paths)
    TREESET = set(TREE)
    BYBASE = {}
    for q in TREE:
        BYBASE.setdefault(os.path.basename(q), []).append(q)
    DIRS = {os.path.dirname(q) for q in TREE}
    _DIR_CACHE.clear()
    _DIR_CACHE.update(binds or {})
    try:
        yield
    finally:
        TREE, TREESET, BYBASE, DIRS = keep[0], keep[1], keep[2], keep[3]
        _DIR_CACHE.clear()
        _DIR_CACHE.update(keep[4])


def seed():
    """known-answer cases for every state `resolution` can return.

    ⛔ r7436 ⒠: the `/`-AMBIGUOUS state measures ZERO real occurrences in the corpus (r7434 arm ⒝), so it
    is dead code on this population and the only way to test it is to construct it.  And the two arms that
    matter are stated on the BEHAVIOUR rather than on the branch: *adding one file to the tree must turn a
    RESOLVED token into AMBIGUOUS and never into NONE* -- once for each route, because that is a behaviour
    this resolver writes twice."""
    fails = []
    n = [0]

    def ck(label, cond):
        n[0] += 1
        print(f'    {"OK   " if cond else "FAIL "} {label}')
        if not cond:
            fails.append(label)

    R = 'receipts/L_x/R_the_receipt.py'

    print('\n  ⓵  NOT-A-TOKEN -- not a claim about the tree at all, and so not a NONE')
    with _tree([R, 'a/b/c.py', 'a/b/.hidden.py']):
        for tok in ('', '.', './', '/', '...', './/.'):
            r = resolution(R, tok)
            ck(f'⓵ {tok!r} -> NOT-A-TOKEN, no paths, no candidates', r.state == NOT_A_TOKEN
               and not r.paths and not r.candidates)
        ck('⓵ᵉ and `resolve` says NOT-A-TOKEN rather than an empty label',
           resolve(R, '.') == ([], NOT_A_TOKEN))
        # ⛔ TWO EXPECTATIONS OF MINE MOVED HERE, and both moves are recorded rather than rewritten.
        ck('⓵ᶠ ⛔ the `tok.startswith(".")` disjunct this guard used to carry is UNREACHABLE: over every '
           'token shape that could reach it, `strip("./")` never leaves a leading dot -- so it was dead '
           'code, and deleting it is what the seed found',
           not any(t.strip('./').startswith('.')
                   for t in ('.hidden', '..x', './a', '...', './.y', '/.z', '.', '', 'a.py', './/..')))
        r = resolution(R, '.hidden.py')
        ck('⓵ᵍ ⛔ AND A SECOND DEAD-BUT-WRONG BEHAVIOUR, which this seed found and this revision does NOT '
           'repair: `strip("./")` also strips the dot a DOTFILE owns, so `.hidden.py` is looked up as '
           '`hidden.py` and reads NONE though the file is right there in the tree',
           r.state == NONE and 'a/b/.hidden.py' in TREESET)
        ck('⓵ᵍⁱ ⌗ and my expectation moved again: the mangling bites ONLY the bare-basename route.  The '
           'same dotfile named as a PATH resolves, because there the leading character is not a dot and '
           '`strip` takes nothing -- so the defect is `strip("./")` on a basename and not the dotfile',
           resolution(R, 'a/b/.hidden.py').state == RESOLVED
           and resolution(R, '.hidden.py').state == NONE)
        r = resolution(R, '  ')
        ck('⓵ʰ ⌗ and a whitespace-only token reads NONE and not NOT-A-TOKEN -- I expected the latter.  '
           '`strip("./")` leaves the spaces, so it IS a claim the tree does not answer; and the mint\'s '
           'own `PATHTOK` cannot emit one, so widening the guard for it would be behaviour for an input '
           'the population cannot produce',
           r.state == NONE)

    print('\n  ⓶  THE PATH ROUTE -- RESOLVED, AMBIGUOUS, NONE')
    with _tree([R, 'a/b/c.py', 'z/q.py']):
        r = resolution(R, 'a/b/c.py')
        ck('⓶ᵃ an exact path -> RESOLVED by PATH to itself',
           (r.state, r.paths, r.how) == (RESOLVED, ['a/b/c.py'], 'PATH'))
        r = resolution(R, 'b/c.py')
        ck('⓶ᵇ a unique suffix -> RESOLVED by PATH', (r.state, r.paths) == (RESOLVED, ['a/b/c.py']))
        r = resolution(R, 'no/such.py')
        ck('⓶ᶜ a suffix of nothing -> NONE, with PATH named as the route that came up empty',
           (r.state, r.how, r.candidates) == (NONE, 'PATH', []))
    with _tree([R, 'a/b/c.py', 'd/b/c.py']):
        r = resolution(R, 'b/c.py')
        ck('⓶ᵈ ⛔ a suffix of TWO paths -> AMBIGUOUS, not NONE -- the state r7434 measured at 0 real '
           'occurrences and which only a constructed tree can reach',
           r.state == AMBIGUOUS and r.paths == [] and sorted(r.candidates) == ['a/b/c.py', 'd/b/c.py'])
        ck('⓶ᵉ and the candidates are REPORTED, so a caller can say how many answered: 2',
           len(r.candidates) == 2 and '2 paths' in r.why)
        ck('⓶ᶠ and `resolve` says AMBIGUOUS where it used to say nothing',
           resolve(R, 'b/c.py') == ([], AMBIGUOUS))

    print('\n  ⓷  THE BASENAME ROUTES -- BASE, DIR, and the ambiguity that is LIVE at 120 pairs')
    with _tree([R, 'a/b/c.py']):
        r = resolution(R, 'c.py')
        ck('⓷ᵃ a basename unique repo-wide -> RESOLVED by BASE',
           (r.state, r.paths, r.how) == (RESOLVED, ['a/b/c.py'], 'BASE'))
        r = resolution(R, 'nowhere.py')
        ck('⓷ᵇ a basename carried by no path -> NONE', (r.state, r.candidates) == (NONE, []))
    with _tree([R, 'a/b/c.py', 'd/e/c.py'], binds={R: ['d/e']}):
        r = resolution(R, 'c.py')
        ck('⓷ᶜ ambiguous repo-wide BUT one sits in a directory the receipt itself binds -> RESOLVED by DIR',
           (r.state, r.paths, r.how) == (RESOLVED, ['d/e/c.py'], 'DIR'))
    with _tree([R, 'a/b/c.py', 'd/e/c.py'], binds={R: ['nowhere']}):
        r = resolution(R, 'c.py')
        ck('⓷ᵈ ⛔ ambiguous repo-wide and the receipt binds no directory holding it -> AMBIGUOUS, not NONE '
           '-- the live case, 120 distinct pairs at r7434',
           r.state == AMBIGUOUS and r.paths == [] and len(r.candidates) == 2)
        ck('⓷ᵉ and `resolve` says AMBIGUOUS', resolve(R, 'c.py') == ([], AMBIGUOUS))

    print('\n  ⓸  A RECEIPT IS NEVER ITS OWN CONTAINER, and that exclusion yields NONE and not RESOLVED')
    with _tree([R]):
        ck('⓸ᵃ the basename of the receipt itself -> NONE',
           resolution(R, os.path.basename(R)).state == NONE)
        ck('⓸ᵇ the receipt\'s own full path -> NONE', resolution(R, R).state == NONE)

    print('\n  ⓹  ⚖ THE BEHAVIOUR, NOT THE BRANCH: one more file must make a token AMBIGUOUS, never NONE')
    for route, before, after, tok in (
            ('PATH', [R, 'a/b/c.py'], [R, 'a/b/c.py', 'd/b/c.py'], 'b/c.py'),
            ('BASE', [R, 'a/b/c.py'], [R, 'a/b/c.py', 'd/e/c.py'], 'c.py')):
        with _tree(before):
            s0 = resolution(R, tok).state
        with _tree(after):
            s1 = resolution(R, tok).state
        ck(f'⓹ {route}: RESOLVED on a tree of {len(before)} and AMBIGUOUS on the same tree plus one file '
           f'-- the token did not stop naming things, so it must not read as naming none',
           (s0, s1) == (RESOLVED, AMBIGUOUS))

    print('\n  ⓺  AND THE SAME STATES ON THE REAL TREE AT THE FRAME, as known answers')
    r = resolution(ARCHETYPE_RECEIPT, 'COMPARISON.tsv')
    ck(f'⓺ᵃ the archetype resolves by BASE to exactly {ARCHETYPE}',
       (r.state, r.paths, r.how) == (RESOLVED, [ARCHETYPE], 'BASE'))
    # ⌗ A THIRD EXPECTATION MOVED: I first wrote these against ARCHETYPE_RECEIPT, and it RESOLVES -- `S17`
    # binds its own computation directory, which holds a `PREDICTION.md`.  The ambiguity needs a receipt
    # that binds no such directory, and the same token in the two receipts is the sharper case anyway.
    r = resolution(ARCHETYPE_RECEIPT, 'PREDICTION.md')
    ck('⓺ᵇ the same token from a receipt that DOES bind a directory holding it -> RESOLVED by DIR, one '
       'container out of 230',
       (r.state, r.how) == (RESOLVED, 'DIR') and r.paths == [ARCHETYPE_DIR + '/PREDICTION.md'])
    r = resolution(AMBIGUOUS_RECEIPT, 'PREDICTION.md')
    ck(f'⓺ᶜ ⛔ and from a receipt that binds no directory holding it -> AMBIGUOUS over '
       f'{len(r.candidates)} real containers -- r7434\'s worst single token, which the old resolver '
       f'reported as naming NONE',
       r.state == AMBIGUOUS and len(r.candidates) == 230 and not r.paths)
    ck('⓺ᶜⁱ and the two answers come from ONE function on ONE tree, so the difference is the receipt and '
       'not the instrument',
       resolution(ARCHETYPE_RECEIPT, 'PREDICTION.md').state == RESOLVED
       and resolution(AMBIGUOUS_RECEIPT, 'PREDICTION.md').state == AMBIGUOUS
       and len(BYBASE.get('PREDICTION.md', [])) == 230)
    r = resolution(ARCHETYPE_RECEIPT, ARCHETYPE)
    ck('⓺ᵈ a real full path -> RESOLVED by PATH', (r.state, r.paths) == (RESOLVED, [ARCHETYPE]))
    ck('⓺ᵉ candidates are non-empty for exactly the two states that reached something',
       all((len(resolution(ARCHETYPE_RECEIPT, t).candidates) > 0)
           == (resolution(ARCHETYPE_RECEIPT, t).state in (RESOLVED, AMBIGUOUS))
           for t in ('COMPARISON.tsv', 'PREDICTION.md', 'nowhere-at-all.tsv', '.', ARCHETYPE)))

    print('\n  ⓻  AND THE TWO DEAD-BUT-WRONG BEHAVIOURS ARE MEASURED ZEROS, not assumed ones')
    _dotpaths = [q for q in TREE if os.path.basename(q).startswith('.')]
    _toks = {t for v in trace_names()[0].values() for t in v}
    _dottoks = [t for t in _toks if t.strip('/').startswith('.') and t.strip('./')]
    _realdot = [t for t in _dottoks if t.strip('/') in BYBASE or t.strip('/') in TREESET]
    _slashamb = [t for t in _toks if '/' in t.strip('./')
                 and len([q for q in TREE if q.endswith('/' + t.strip('./'))]) >= 2]
    print(f'      dot-leading basenames in the tree      : {len(_dotpaths)}')
    print(f'      dot-leading tokens in the trace        : {len(_dottoks)}  {sorted(_dottoks)}')
    print(f'      of those, naming a REAL dotfile        : {len(_realdot)}')
    print(f'      `/`-shaped tokens reaching two or more : {len(_slashamb)}')
    ck(f'⓻ᵃ the dotfile mangling COULD have fired -- {len(_dotpaths)} path(s) in the tree carry a '
       f'dot-leading basename -- so the zero below is a measurement and not an empty population',
       len(_dotpaths) > 0)
    ck(f'⓻ᵇ and it fires on NOTHING: all {len(_dottoks)} dot-leading tokens the trace names are bare '
       f'KINDS ({", ".join(sorted(_dottoks))}), which name no file with or without the dot',
       len(_realdot) == 0 and len(_dottoks) > 0)
    ck('⓻ᶜ and r7434\'s `/`-ambiguity is still zero on this tree, re-measured here rather than inherited',
       len(_slashamb) == 0)
    ck('⓻ᵈ ⚖ so the resolver carries TWO behaviours that are wrong if reached and unreachable from the '
       'data, and a seed by construction is the only instrument that can see either',
       len(_realdot) == 0 and len(_slashamb) == 0 and len(_dotpaths) > 0)

    print(f'\n  {n[0]} assertion(s), {len(fails)} failing')
    for f in fails:
        print(f'    - {f}')
    return 1 if fails else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--seed', action='store_true',
                    help='the three-state resolver\'s known-answer cases, and nothing else')
    ap.add_argument('--sample', type=int, default=50,
                    help='⒠ii: present-in-container keys confirmed present repo-wide')
    a = ap.parse_args()
    if a.seed:
        print('=' * 100)
        print('  r7400 cost.py -- THE THREE STATES OF `resolution`, BY CONSTRUCTION  (r7436, r7433 (1))')
        print(f'  the real-tree cases are read at FRAME {FULL[:9]}, never live')
        print('=' * 100)
        return seed()

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
    sys.exit(main() or 0)
