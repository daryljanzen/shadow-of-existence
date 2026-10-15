#!/usr/bin/env python3
"""r7374 (60) -- THE KEY THE ENVIRONMENT CHOOSES.

** `r7370` repaired `S39`'s `Ⓑ①` and wrote the cause beside it twice -- in `S39` and in `S56` -- as a
shallow clone's horizon.  Three measurements say it cannot be that, and the third reproduces the exact
signature from a different variable. **

  (i)   no job that runs a receipt is shallow: every receipt-running job in the workflow checks out with
        `fetch-depth: 0`, at the commit the red was recorded against, at the commit carrying the second
        repair, and on the trunk now.  The one default-depth checkout runs LaTeX and no receipts.
  (ii)  all six pinned shas are ancestors of the trunk, so reachable from HEAD at any depth.
  (iii) the gate builds `_SESSION` with `git log --format=%h…` and looks a sha up in it by EXACT STRING.
        `%h` is git's abbreviation and git picks its length from the object count.  At this clone's
        length all six are found; at any other length NONE of them is.

⇒ ** A PIN KEYED BY AN ABBREVIATION IS KEYED BY SOMETHING THE ENVIRONMENT CHOOSES. **

⚠ *Not claimed: that the runner's abbreviation length is any particular value.  It cannot be seen from
here, and asserting it would be the move being corrected.  The defect is that the lookup is an exact
string match against a length the environment picks -- wrong whatever that length is.*

** THE ARMS. **  ⒜ CONSUMING sites -- code that takes git's abbreviated OUTPUT and matches it as a
string (central 3, band 1-10).  ⒝ `corpus/check_*.py` that key a map by one (exact 1).  ⒞ this seat's
own pinned sha constants that are NOT 8 characters (exact 0), this seat's commits selected by the
session marker as `P03` and `S5` were repaired to do.  ⒟ the control: sites that pass a short sha to
git as an ARGUMENT, which git resolves by prefix and which are immune (central 40, band 15-120).

    python3 computations/beyond_the_wall/r7374_60_the_key_the_environment_chooses/cost.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

FRAME = '361efc0f'      # this revision's registration commit: the prediction, committed before this ran
GATE = 'corpus/check_revision_collisions.py'
#: the six `S39` pins, and the lengths the gate's own map-building command was run at
PINS_S39 = ('8afa9ed3', 'fadf708d', '311e7ac6', 'e7b7c7ab', 'a2555f4f', '566a97fc')
ABBREVS = (None, 7, 9, 12)

#: ** THE PRODUCERS: the ways git is asked for an abbreviation of an OBJECT NAME. **
#: ⚠ *`--abbrev-ref` is NOT one of them -- it abbreviates a REF to a branch name, which has no length
#: the environment picks.  The first form of this detector matched it and counted the collision gate's
#: own branch-name read as a site.*
_PROD = ('%h', '--short', '--abbrev=')
_NOT_PROD = ('--abbrev-ref',)
#: a bare hex literal of abbreviation length, in quotes
_HEX = re.compile(r"""['"]([0-9a-f]{7,12})['"]""")
#: an upper-case constant bound to one
_CONST = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*['\"]([0-9a-f]{7,12})['\"]", re.M)
_CONST_TUPLE = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*\(", re.M)
_SESS = re.compile(r'^Claude-Session:\s*(\S+)', re.M)
_GITCALL = re.compile(r"\b(git|_git|subprocess\.run)\s*\(")

RESULT = {}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def tracked(*prefixes):
    out = []
    for p in prefixes:
        out += [x for x in git('ls-files', p).split('\n') if x.endswith('.py')]
    return sorted(set(out))


def code_lines(rel):
    """(lineno, text) for lines that are not comments and not inside the module docstring"""
    try:
        src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    except OSError:
        return []
    parts = src.split('"""')
    body = '"""'.join(parts[2:]) if len(parts) >= 3 else src
    off = src.count('\n', 0, len(src) - len(body))
    out = []
    for i, ln in enumerate(body.split('\n'), start=off + 1):
        s = ln.strip()
        if s and not s.startswith('#'):
            out.append((i, ln))
    return out


def own_session():
    m = _SESS.search(git('show', '-s', '--format=%B', FRAME))
    return m.group(1) if m else None


def introducing_commit(rel, needle):
    shas = git('log', '--reverse', '--format=%H', '-S', needle, FRAME, '--', rel).split()
    return shas[0] if shas else None


# ── (iii) the reproduction, at the gate's own command ────────────────────────────────────────────
def map_at(abbrev):
    args = ['git', '-C', ROOT]
    if abbrev:
        args += ['-c', f'core.abbrev={abbrev}']
    args += ['log', '--format=%h%x09%(trailers:key=Claude-Session,valueonly,separator=%x20)%x09%s']
    out = subprocess.run(args, capture_output=True, text=True, errors='replace').stdout
    keys = set()
    for ln in out.split('\n'):
        if ln.count('\t') >= 2:
            keys.add(ln.split('\t', 1)[0])
    return keys


# ── (i) the workflow's checkout depths, read rather than remembered ──────────────────────────────
def depths(sha):
    """{job: 'full'|'default'} from the workflow as it stands at `sha`"""
    txt = git('show', f'{sha}:.github/workflows/gates.yml').split('\n')
    job, out = None, {}
    for i, ln in enumerate(txt):
        m = re.match(r'^  ([a-z][a-z0-9-]*):\s*$', ln)
        if m:
            job = m.group(1)
        if 'actions/checkout@' in ln and job:
            nxt = txt[i + 1] if i + 1 < len(txt) else ''
            out[job] = 'full' if 'fetch-depth: 0' in nxt else 'default'
    return out


def runs_receipts(sha, job):
    """does this job's block invoke a receipt runner?"""
    txt = git('show', f'{sha}:.github/workflows/gates.yml').split('\n')
    start = None
    for i, ln in enumerate(txt):
        m = re.match(r'^  ([a-z][a-z0-9-]*):\s*$', ln)
        if m:
            if m.group(1) == job:
                start = i
            elif start is not None:
                return any('run_all_receipts' in x or 'receipt_scope' in x for x in txt[start:i])
    return False


# ── the classifier, committed here ───────────────────────────────────────────────────────────────
def _pinned_names(src):
    """names in this file bound to a hex literal of abbreviation length"""
    return {m.group(1) for m in _CONST.finditer(src)}


def _match_lines(src, names):
    """line numbers where an ABBREVIATION is matched, keyed or looked up -- read off the SYNTAX TREE

    ** The first form of this test asked whether any `==`, `in` or subscript stood within six lines of
    a producer, and that is not the question. **  *It counted `len(git(...--format=%h...).split()) == 2`,
    where the `==` compares a COUNT, and it counted a branch-name read.  What makes a producer site a
    defect is that the abbreviation flows into a comparison or a lookup AGAINST A PINNED ABBREVIATION --
    a hex literal of that length, or a name bound to one in this file.*
      ⌗ *So the consumption side is structural: `Compare`, `Subscript`, and `.get`/`.setdefault` nodes
        one of whose operands is such a constant.  `S57`'s lesson, applied one revision later.*
    """
    import ast as _ast
    try:
        tree = _ast.parse(src)
    except SyntaxError:
        return set()

    def _is_pin(node):
        if isinstance(node, _ast.Constant) and isinstance(node.value, str):
            return bool(re.fullmatch(r'[0-9a-f]{7,12}', node.value))
        if isinstance(node, _ast.Name):
            return node.id in names
        if isinstance(node, _ast.Attribute):
            return node.attr in names
        return False

    out = set()
    for node in _ast.walk(tree):
        operands = []
        if isinstance(node, _ast.Compare):
            operands = [node.left, *node.comparators]
        elif isinstance(node, _ast.Subscript):
            operands = [node.slice]
        elif isinstance(node, _ast.Call) and isinstance(node.func, _ast.Attribute) \
                and node.func.attr in ('get', 'setdefault'):
            operands = list(node.args)
        else:
            continue
        for o in operands:
            for sub in _ast.walk(o):
                if _is_pin(sub):
                    out.add(getattr(node, 'lineno', 0))
                    break
    return out


def classify(rel):
    """[(lineno, kind, text)] -- CONSUMING / ABOUT for producer sites, ARGUMENT for the immune form

    ** A site that passes a short sha TO git is safe: git resolves a prefix.  The defect is consuming
    `%h`, `--short` or `--abbrev=` OUTPUT and matching it against a PINNED abbreviation. **  An
    unclassified producer site defaults to CONSUMING, the direction that counts against this seat.
    """
    try:
        src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    except OSError:
        return []
    lines = code_lines(rel)
    matched = _match_lines(src, _pinned_names(src))
    out = []
    for no, ln in lines:
        if any(p in ln for p in _PROD) and not any(q in ln for q in _NOT_PROD):
            near = any(abs(m - no) <= 6 for m in matched)
            out.append((no, 'CONSUMING' if near else 'ABOUT', ln.strip()[:150]))
        elif _HEX.search(ln) and _GITCALL.search(ln):
            out.append((no, 'ARGUMENT', ln.strip()[:150]))
    return out



#: ⛔⛭⛭⛭ ** THE ARM AS REGISTERED CANNOT BE MEASURED, AND THE WAY IT CANNOT IS THE FINDING. **
#: *Arm ⒜ asked for "code that takes git's abbreviated OUTPUT and matches it as a string".  Two forms
#: were tried.  A WINDOW test -- any `==`, `in` or subscript within six lines of a producer -- returned
#: `18` and over-counted: it took `--abbrev-ref`, which abbreviates a REF and has no environment-chosen
#: length, and it took `len(git(...--format=%h...).split()) == 2`, where the `==` compares a COUNT.  A
#: STRUCTURAL test -- the abbreviation flowing into a comparison or lookup against a pinned abbreviation
#: in the same file -- returned `0`, and missed the one site that actually fired.*
#:   ⇒ *** BOTH FAIL FOR ONE REASON: THE TWO ENDS OF THE KEY ARE IN DIFFERENT FILES. ***  The gate
#:       BUILDS a map keyed by `%h` and takes the sha as a parameter; the receipt SUPPLIES the pinned
#:       abbreviation from another file, across a function boundary and across seats.  *A locality
#:       detector cannot see a defect whose halves nobody owns together -- which is why it stood for
#:       five pushes with a green receipt and a red runner.*
#:   ⌊ ** So the measurable thing is the PAIRING, not the site: one map keyed by an abbreviation, and
#:     the callers that hand it a pinned one. **
def pairings():
    """(the gate's own consultation points, the files that reach them with a pinned abbreviation)"""
    gate_src = open(os.path.join(ROOT, GATE), encoding='utf-8').read()
    #: the functions in the gate that read the abbreviation-keyed map
    readers = sorted({m.group(1) for m in
                      re.finditer(r'def (\w+)\([^)]*\):(?:(?!\ndef ).)*?_SESSION\s*\.get',
                                  gate_src, re.S)})
    callers = {}
    for rel in tracked('receipts', 'corpus'):
        if rel == GATE:
            continue
        try:
            src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except OSError:
            continue
        if 'check_revision_collisions' not in src:
            continue
        hit = sorted(r for r in readers if re.search(rf'\.{r}\b', src))
        #: ⚠ *and the pairing's own first form required a `NAME = '<hex>'` BINDING, which excluded the
        #: one caller: `S39` keeps its six shas in a dict literal.  Any hex literal of abbreviation
        #: length in the file is the right test -- the fourth form of one detector in one revision.*
        if hit and _HEX.search(src):
            callers[rel] = hit
    return readers, callers

def measure():
    if RESULT:
        return RESULT
    files = tracked('receipts', 'corpus')
    sites = {}
    for rel in files:
        hits = classify(rel)
        if hits:
            sites[rel] = hits

    consuming = [(r, n, t) for r, hs in sites.items() for n, k, t in hs if k == 'CONSUMING']
    about = [(r, n, t) for r, hs in sites.items() for n, k, t in hs if k == 'ABOUT']
    argument = [(r, n, t) for r, hs in sites.items() for n, k, t in hs if k == 'ARGUMENT']

    #: ⒝ the gate layer: a `corpus/check_*.py` that both produces an abbreviation and keys a map by it
    gates = []
    for rel in files:
        if not os.path.basename(rel).startswith('check_') or not rel.startswith('corpus/'):
            continue
        txt = '\n'.join(t for _n, t in code_lines(rel))
        if '%h' in txt and re.search(r'\w+\[\([^)]*\bsha\b[^)]*\)\]\s*=|\w+\[sha\]\s*=', txt):
            gates.append(rel)

    #: ⒞ pinned sha constants, and whose they are
    sess = own_session()
    consts, mine, not8 = [], [], []
    for rel in files:
        try:
            src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
        except OSError:
            continue
        for m in _CONST.finditer(src):
            name, val = m.group(1), m.group(2)
            consts.append((rel, name, val))
            intro = introducing_commit(rel, f"{name} = '{val}'")
            own = bool(intro) and bool(_SESS.search(git('show', '-s', '--format=%B', intro))) \
                and _SESS.search(git('show', '-s', '--format=%B', intro)).group(1) == sess
            if own:
                mine.append((rel, name, val))
                if len(val) != 8:
                    not8.append((rel, name, val))

    readers, callers = pairings()
    RESULT.update(readers=readers, callers=callers,
                  files=files, sites=sites, consuming=consuming, about=about,
                  argument=argument, gates=gates, consts=consts, mine=mine, not8=not8,
                  session=sess)
    return RESULT


def score(got, lo, hi):
    return 'INSIDE' if lo <= got <= hi else ('BELOW' if got < lo else 'ABOVE')


def main():
    print(__doc__)
    print(f'    frame {FRAME}')
    print()

    print('  (iii) THE REPRODUCTION -- the gate`s own map-building command, at four lengths')
    rows = []
    for ab in ABBREVS:
        keys = map_at(ab)
        found = sum(1 for p in PINS_S39 if p in keys)
        lens = sorted({len(k) for k in keys})
        rows.append((ab, lens, len(keys), found))
        print(f'      core.abbrev={str(ab):5}  key length(s) {lens}  {len(keys)} keys  '
              f'pinned shas found: {found} of {len(PINS_S39)}')
    _here = [r for r in rows if r[0] is None][0]
    _other = [r for r in rows if r[0] is not None]
    print(f'      => found here {_here[3]} of {len(PINS_S39)}; at every other length '
          f'{sorted({r[3] for r in _other})}')
    print()

    print('  (i) THE WORKFLOW`S CHECKOUT DEPTHS, read at three commits')
    for sha in ('cdc16410', '4cb449fe', 'origin/main'):
        d = depths(sha)
        defaults = [j for j, v in d.items() if v == 'default']
        rec = {j: runs_receipts(sha, j) for j in defaults}
        print(f'      {sha:12} {len(d)} checkout(s), full {sum(1 for v in d.values() if v == "full")}, '
              f'default {defaults} -- runs receipts: {rec}')
    print()

    print('  (ii) THE SIX PINNED SHAS AGAINST THE TRUNK')
    _on = [p for p in PINS_S39
           if subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', p, 'origin/main'],
                             capture_output=True).returncode == 0]
    print(f'      {len(_on)} of {len(PINS_S39)} are ancestors of origin/main, so reachable at any depth')
    print()

    R = measure()
    print(f'  THE SCAN -- {len(R["files"])} tracked python file(s) under receipts/ and corpus/')
    print(f'      ⒜ CONSUMING {len(R["consuming"])} (central 3, band 1-10) '
          f'{score(len(R["consuming"]), 1, 10)}')
    print(f'      ⒝ gate-layer maps {len(R["gates"])} (exact 1) '
          f'{"HIT" if len(R["gates"]) == 1 else "MISS"}')
    print(f'      ⒞ this seat`s pins not 8 chars {len(R["not8"])} of {len(R["mine"])} '
          f'(exact 0) {"HIT" if not R["not8"] else "MISS"}')
    print(f'      ⒟ ARGUMENT {len(R["argument"])} (central 40, band 15-120) '
          f'{score(len(R["argument"]), 15, 120)}')
    print(f'      ⌗ ABOUT (printed, not matched) {len(R["about"])}')
    print()

    print('  THE PAIRING -- the arm as registered cannot be measured, and that is the finding')
    print(f'      the gate`s functions that read the abbreviation-keyed map: {R["readers"]}')
    print(f'      files that reach them AND carry a pinned abbreviation: {len(R["callers"])}')
    for rel, hit in sorted(R['callers'].items()):
        print(f'         {rel} -> {hit}')
    print(f'      => 1 map, {len(R["callers"])} caller(s): the two ends of the key in different files')
    print()

    print('  EVERY CONSUMING SITE (structural test; the window test returned 18, over-counting)')
    for rel, no, txt in R['consuming']:
        print(f'      {rel}:{no}')
        print(f'         {txt}')
    print()
    print(f'  THE GATE-LAYER MAPS: {R["gates"]}')
    print()
    print(f'  PINNED SHA CONSTANTS: {len(R["consts"])} in all, {len(R["mine"])} this seat`s')
    _hist = {}
    for _r, _n, v in R['consts']:
        _hist[len(v)] = _hist.get(len(v), 0) + 1
    print(f'      length histogram over all of them: {dict(sorted(_hist.items()))}')
    if R['not8']:
        for rel, name, val in R['not8']:
            print(f'      NOT 8: {rel} {name} = {val!r}')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
