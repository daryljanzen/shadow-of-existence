#!/usr/bin/env python3
"""r7279+70.1: the narrow figure-pin detector, as pre-registered in PREDICTION.md (0a4ec067).

A FIGURE in a citing claim is PINNED by the cited receipt when some comparison in the receipt's parsed source holds it
within its ALLOWANCE -- the coarser of half a unit in its last printed digit and 0.05 % of its magnitude.  A site is
FLAGGED when one of its figures is not pinned.  Populations are r7267's census.py, rebuilt at this tree.

    python3 detector.py            # seeds, then writes sites.tsv and prints the counts
"""
import ast
import math
import os
import re
import sys
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7267_70_citation_reach'))
import census as C  # noqa: E402

NUM = re.compile(r'(?<![\w.])(\d+\.\d{2,}|\d{2,}\.\d+)(?![\w.])')
REVTAG = re.compile(r'(?:r\d+\+|\+c?\d*\.?|\+)$')
DEFAULTS = {'isclose': (1e-9, 0.0), 'approx': (1e-6, 1e-12), 'allclose': (1e-5, 1e-8),
            'assertAlmostEqual': (0.0, 0.5e-7)}


def figures(claim):
    """[(value, allowance)] for every figure the claim prints; a percent figure also yields value/100"""
    out = []
    for m in NUM.finditer(claim):
        if REVTAG.search(claim[max(0, m.start() - 8):m.start()]):
            continue
        s = m.group(1)
        x = float(s)
        d = len(s.split('.')[1])
        a = max(0.5 * 10 ** -d, 5e-4 * abs(x))
        alts = [(x, a)]
        if re.match(r'\s*\\?%', claim[m.end():m.end() + 3]):
            alts.append((x / 100, a / 100))
        out.append((s, alts))
    return out


def _consts(tree):
    out = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            v = _num(n.value, {})
            if v is not None:
                out[n.targets[0].id] = v
    return out


def _num(n, consts):
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
        return float(n.value)
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        v = _num(n.operand, consts)
        return -v if v is not None else None
    if isinstance(n, ast.Name) and n.id in consts:
        return consts[n.id]
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow):
        a, b = _num(n.left, consts), _num(n.right, consts)
        if a is not None and b is not None and abs(b) < 400:
            try:
                return float(a ** b)
            except (OverflowError, ZeroDivisionError, TypeError):
                return None
    return None


def _fname(call):
    f = call.func
    return f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''


def _inner_nums(n, consts):
    out = []
    for m in ast.walk(n):
        v = _num(m, consts)
        if v is not None:
            out.append(v)
    return out


def pins(src):
    """[(c, t)]: value c held to tolerance t by some comparison in the source"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    consts = _consts(tree)
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Compare):
            ops, xs = n.ops, [n.left] + n.comparators
            if all(isinstance(o, (ast.Eq, ast.Is)) for o in ops):
                for i, x in enumerate(xs):
                    c = _num(x, consts)
                    if c is None:
                        continue
                    t = 0.0
                    for y in xs[:i] + xs[i + 1:]:
                        if isinstance(y, ast.Call) and _fname(y) == 'round' and len(y.args) == 2:
                            k = _num(y.args[1], consts)
                            if k is not None:
                                t = 0.5 * 10 ** -k
                    out.append((c, t))
            elif len(xs) == 2 and all(isinstance(o, (ast.Lt, ast.LtE, ast.Gt, ast.GtE)) for o in ops):
                a, b = xs if isinstance(ops[0], (ast.Lt, ast.LtE)) else xs[::-1]
                t = _num(b, consts)
                if t is None:
                    continue
                scale = 1.0
                if isinstance(a, ast.BinOp) and isinstance(a.op, ast.Div):
                    d = _num(a.right, consts)
                    if d is not None:
                        scale, a = abs(d), a.left
                    else:
                        cs = [v for v in _inner_nums(a.right, consts)]
                        scale, a = (abs(cs[0]) if cs else 1.0), a.left
                if isinstance(a, ast.Call) and _fname(a) in ('abs', 'fabs') and a.args:
                    for c in _inner_nums(a.args[0], consts):
                        out.append((c, t * scale))
            elif len(xs) == 3 and all(isinstance(o, (ast.Lt, ast.LtE)) for o in ops) or \
                    len(xs) == 3 and all(isinstance(o, (ast.Gt, ast.GtE)) for o in ops):
                lo, hi = _num(xs[0], consts), _num(xs[2], consts)
                if lo is not None and hi is not None:
                    out.append(((lo + hi) / 2, abs(hi - lo) / 2))
        elif isinstance(n, ast.Call) and _fname(n) in DEFAULTS:
            rel, ab = DEFAULTS[_fname(n)]
            for kw in n.keywords:
                v = _num(kw.value, consts)
                if v is None:
                    continue
                if kw.arg in ('rel_tol', 'rtol', 'rel'):
                    rel = v
                elif kw.arg in ('abs_tol', 'atol', 'abs', 'delta'):
                    ab = v
                elif kw.arg == 'places':
                    ab = 0.5 * 10 ** -v
            for arg in n.args:
                c = _num(arg, consts)
                if c is not None:
                    out.append((c, max(ab, rel * abs(c))))
    return out


@lru_cache(maxsize=None)
def receipt_pins(name):
    return pins(C.src_text(name)[1])


def unpinned(claim, ps):
    """the printed figures of `claim` that no pin in `ps` holds within their allowance"""
    out = []
    for s, alts in figures(claim):
        if not any(abs(abs(c) - x) <= a and t <= a for x, a in alts for c, t in ps):
            out.append(s)
    return out


def _seeds():
    src = ('X = 0.315162424\n'
           'assert abs(v - X) < 1e-6\n'
           'check("l2", abs(l2 - 7.8) < 0.3)\n'
           'assert m < 348\n'
           'assert round(q, 2) == 2.10\n'
           'assert 1.23 < w < 1.25\n'
           'assert math.isclose(z, 4.5678, rel_tol=1e-6)\n'
           'assert 41.04 < y < 41.06\n')
    ps = pins(src)
    cases = [('a tight named-constant pin', 'the root is 0.315162424', False),
             ('a slack pin on a nearby value', 'the multipole is 7.78', True),
             ('a one-sided bound', 'the ratio is 207.8', True),
             ('a round()==c pin', 'the reduced value 2.10', False),
             ('a two-sided bracket at the allowance', 'the value 1.24', True),
             ('a two-sided bracket inside the allowance', 'the value 41.05', False),
             ('an isclose pin', 'the figure 4.5678', False),
             ('a figure no check names', 'the share 46.53', True),
             ('a revision tag is not a figure', 'answered at r7267+70.1', False),
             ('a percent figure against its fraction', 'a shift of 0.065\\%', True)]
    bad = []
    for label, claim, want in cases:
        got = bool(unpinned(claim, ps))
        if got != want:
            bad.append(f'{label}: expected {"flag" if want else "pass"}, got {"flag" if got else "pass"}')
    ps2 = pins('assert abs(r - 0.00065) < 1e-7\n')
    if unpinned('a shift of 0.065\\%', ps2):
        bad.append('a percent figure pinned as its fraction must pass')
    return bad


def sites():
    rows = []
    for pop, paper, name, claim, _s, _n in C.prose() + C.appendix():
        if not claim or name not in C.FILES or not figures(claim):
            continue
        rows.append((pop, paper, name, claim, unpinned(claim, receipt_pins(name))))
    return rows


if __name__ == '__main__':
    bad = _seeds()
    print('unit seeds:', 'hold' if not bad else bad)
    rows = sites()
    by = {}
    for r in rows:
        by.setdefault(r[2], []).append(r)
    real = {'S+1 N05': ('P16_the_interior_to_observed_mode_map', '7.78', True),
            'S+2 N13': ('P13_mass_cubic_carries_no_hierarchy', '207.8', True),
            'S-1 N07': ('P15_the_growth_root_is_a_moment_balance_pivoting_on_the_nariai_radius', '0.315162424', False),
            'miss N02': ('P03_the_hubble_eddington_radius_is_the_slices_flat_locus_and_the_bend_takes_whatever_gravitates',
                         '1.2599', None),
            'miss N18': ('P15_the_133_bin_pair_is_computed_and_asserted_and_the_hardcoded_row_carried_the_other_arm',
                         '279.4', None)}
    for lab, (name, fig, want) in real.items():
        ps = receipt_pins(name)
        got = fig in unpinned(f'the figure {fig}', ps)
        tag = '' if want is None else ('ok' if got == want else 'LOST')
        print(f'  {lab}: {fig} {"FLAGS" if got else "passes"} {tag}')
    # S-2: a claim printing a constant the receipt asserts at a tight tolerance, taken from S-1's own source
    print('  S-2 synthetic: ', 'ok' if not unpinned('the root 0.315162424', [(0.315162424, 1e-9)]) else 'LOST')
    with open(os.path.join(HERE, 'sites.tsv'), 'w', encoding='utf-8') as f:
        f.write('# population\tpaper\treceipt\tunpinned figures\tclaim\n')
        for pop, paper, name, claim, u in rows:
            f.write('\t'.join([pop, paper, name, ' '.join(u), claim[:500].replace('\t', ' ')]) + '\n')
    k = len(rows)
    fl = sum(bool(r[4]) for r in rows)
    for pop in ('PROSE', 'APPENDIX'):
        rr = [r for r in rows if r[0] == pop]
        print(f'{pop}: {len(rr)} figure-bearing; flagged {sum(bool(r[4]) for r in rr)}')
    print(f'F-a {k} figure-bearing sites; F-b flagged {fl} ({100 * fl / k:.1f}%)')
