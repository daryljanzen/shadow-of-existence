#!/usr/bin/env python3
"""r7342+60 -- THE WRONG REFERENT: the arithmetic of the registration, written and pushed BEFORE the
ordered repair.

** WHAT WAS ORDERED. **  `r7341` ①: *`L165/S10` owes a one-line repair and it is in your registered
block.  `S10` asserts `C^2 = sigma^2(4 + 16 sigma^2/3)` and NAMES NO METRIC, so any reader supplies a
family and gets a different answer -- which is what happened.  The repair is one line, because
`L549/Q1` computes the same polynomial symbolically from a named metric and passes: `S10` names Q1's
family or cites Q1.  Do not re-derive it.*

⛭ ** AND THE ORDER UNDERSTATES THE DEFECT, WHICH IS WHY THIS REVISION MEASURES THE CLASS RATHER THAN
ONLY CLOSING THE ONE ROW. **  `S10` does not name NO metric.  It names `diag(-2 sigma, sigma, sigma)`
and the invariant `6 sigma^2` -- *which is `71`'s family, not `Q1`'s* -- and asserts `Q1`'s polynomial
beside them.  `families.py` computes both from their metrics: the triple `S10` names gives
`12 sigma^2 (H - 2 sigma)^2`, which carries exactly the `-48 H sigma^3` term `71` reported.  ⇒ ** `71`
did not supply an arbitrary family.  It used the one `S10` HANDED it. **  So the defect is a WRONG
referent and not an absent one, and the thing that could not fail is `S10`'s own trace-free check: it
is true of every traceless triple, so it cannot tell the family the polynomial comes from from the
family the receipt names.

** COMPUTES: ** the registered band and its decisive fraction under an exact binomial, and the census
of the class over this block's receipts read at a pinned commit.  No paper quantity.
"""
import ast
import os
import re
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))

# ── the pin: the population is enumerated HERE, before the registration commit itself ────────────
PIN = '28edd3c6'
PREFIXES = ('L165_interacting_tower', 'L211_closure_adjacency',
            'L175_dimensional_descent', 'L204_physics_reach')

# ── the arm: receipts of this block carrying an UNREFERENCED CLOSED FORM ─────────────────────────
#   ⚠ The population is the WHOLE block -- every `.py` gate under the four prefixes -- and not the
#   `19` receipts that had owed rows.  *That is the point of the order: `S10`'s two ledger rows are
#   both DELIBERATE, so the owed count could never look at it.*
A_CENTRAL = 4
A_BAND = (2, 7)
#   ⒜ fails LOW at `<= 1`, which says `S10` is an isolated defect and not a class, and the owed
#      count's blind spot on this block is one receipt wide.
#   ⒝ fails HIGH at `>= 8`, which says the blind spot is wider on this block than the whole of what
#      the owed count still has left on it, and the phase is priced on the wrong instrument.

# ── the arbiter, fixed here and not after the count ──────────────────────────────────────────────
#   A receipt carries an UNREFERENCED CLOSED FORM when all three hold:
#     ① it writes a POLYNOMIAL OUT BY HAND in a sympy symbol of its own -- a power of a name bound by
#        `Symbol`/`symbols`, with a numeric coefficient beside it;
#     ② it does not DERIVE that polynomial -- the module builds no metric (`diag`/`Matrix`) and calls
#        no curvature routine; and
#     ③ it does not TIE it to the source that does -- no string in its CODE names another receipt,
#        and no other receipt module is imported.
#   ⌗ ** A citation in the PROSE does not count, and the registration says so before the count. **
#   The module docstring is excluded from ③ by construction: a formula is tied to its referent when a
#   CHECK can fail if the tie breaks, and a sentence cannot fail.  *That is the whole of the repair
#   form this phase is built on -- assert what the claim IS -- applied to the receipt's own citation.*
_SYMBOL_CALLS = ('Symbol', 'symbols')
_DERIVERS = ('invariants', 'weyl_sq', 'christoffel', 'riemann', 'ricci', 'curvature')
_METRIC_CTORS = ('diag', 'Matrix')
_RECEIPT_PY = re.compile(r'[A-Za-z]+\d+[A-Za-z0-9_]*\.py')


def decisive(space, central, band):
    """P(outcome outside the band | the registration's own central), exact binomial."""
    p = central / space
    return sum(comb(space, k) * p ** k * (1 - p) ** (space - k)
               for k in range(space + 1) if k < band[0] or k > band[1])


def _git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def population(sha=PIN):
    """every `.py` gate under the four prefixes, enumerated at the pin"""
    out = []
    for line in _git('ls-tree', '-r', '--name-only', sha).split('\n'):
        if (line.startswith('receipts/') and line.endswith('.py')
                and line.count('/') == 2 and line.split('/')[1] in PREFIXES):
            out.append(line)
    return sorted(out)


def _source(path, sha=PIN):
    return _git('show', f'{sha}:{path}')


def _call_names(tree):
    out = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            out.add(f.attr if isinstance(f, ast.Attribute) else
                    (f.id if isinstance(f, ast.Name) else ''))
    return out


def _symbol_names(tree):
    """names bound by a `Symbol`/`symbols` call anywhere in the module"""
    out = set()
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Assign, ast.AnnAssign)):
            continue
        v = n.value
        if not isinstance(v, ast.Call):
            continue
        f = v.func
        name = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else '')
        if name not in _SYMBOL_CALLS:
            continue
        tgts = n.targets if isinstance(n, ast.Assign) else [n.target]
        for t in tgts:
            if isinstance(t, ast.Name):
                out.add(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                out.update(e.id for e in t.elts if isinstance(e, ast.Name))
    return out


def hardcoded(tree):
    """① a power of a module-local sympy symbol with a numeric coefficient in the same expression"""
    syms = _symbol_names(tree)
    if not syms:
        return []
    hits = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.BinOp):
            continue
        sub = list(ast.walk(n))
        powered = any(isinstance(k, ast.BinOp) and isinstance(k.op, ast.Pow)
                      and isinstance(k.left, ast.Name) and k.left.id in syms for k in sub)
        if not powered:
            continue
        numeric = any(isinstance(k, ast.Constant) and isinstance(k.value, (int, float))
                      and k.value not in (0, 1) for k in sub)
        if not numeric:
            numeric = any(isinstance(k, ast.Call) and getattr(k.func, 'attr', '') == 'Rational'
                          for k in sub)
        if numeric:
            hits.append(ast.unparse(n))
    return sorted({h for h in hits}, key=len, reverse=True)


def derives(tree):
    """② the module builds a metric or calls a curvature routine of its own"""
    calls = _call_names(tree)
    return bool(calls & set(_DERIVERS)) or bool(calls & set(_METRIC_CTORS))


def tied(path, tree):
    """③ a string in the CODE -- never the prose -- names another receipt, or one is imported"""
    own = os.path.basename(path)
    docstrings = set()
    for n in ast.walk(tree):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            d = ast.get_docstring(n, clean=False)
            if d is not None:
                docstrings.add(id(n.body[0].value))
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docstrings:
            for m in _RECEIPT_PY.findall(n.value):
                if m != own:
                    return m
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = getattr(n, 'module', '') or ''
            for m in _RECEIPT_PY.findall(mod + ' ' + ' '.join(a.name for a in n.names)):
                if m != own:
                    return m
    return ''


def census(sha=PIN):
    """{path: the longest hand-written closed form} for the members of the class"""
    members, seen = {}, {}
    for p in population(sha):
        try:
            tree = ast.parse(_source(p, sha))
        except SyntaxError:
            continue
        h = hardcoded(tree)
        seen[p] = (bool(h), derives(tree), bool(tied(p, tree)))
        if h and not derives(tree) and not tied(p, tree):
            members[p] = h[0]
    return members, seen


RESULT = {}                     # filled by the result block appended after the census is run


def scored():
    got = RESULT.get('A_MEMBERS')
    space = RESULT.get('A_SPACE')
    if got is None or not space:
        return (None, A_BAND, None, None)
    return (got, A_BAND, A_BAND[0] <= got <= A_BAND[1], decisive(space, A_CENTRAL, A_BAND))


if __name__ == '__main__':
    _pop = population()
    _mem, _seen = census()
    print()
    print('  r7342+60 -- THE WRONG REFERENT, REGISTERED BEFORE THE ORDERED REPAIR')
    print()
    print(f'    the block at {PIN}: {len(_pop)} gates under the four prefixes')
    print(f'    arm (a): central {A_CENTRAL} of {len(_pop)}, band {A_BAND[0]}-{A_BAND[1]}, '
          f'two-sided, decisive {decisive(len(_pop), A_CENTRAL, A_BAND):.3f}')
    print()
    print(f'    members: {len(_mem)}')
    for _p, _h in sorted(_mem.items()):
        print(f'      {_p.split("/")[-1][:62]}')
        print(f'         {_h[:100]}')
    print()
    _hc = sum(1 for v in _seen.values() if v[0])
    _dv = sum(1 for v in _seen.values() if v[0] and v[1])
    _ti = sum(1 for v in _seen.values() if v[0] and not v[1] and v[2])
    print(f'    of the {len(_pop)}: {_hc} write a closed form by hand; of those {_dv} DERIVE it and '
          f'{_ti} TIE it in code')
    print()
