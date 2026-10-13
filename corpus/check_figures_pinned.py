#!/usr/bin/env python3
"""check_figures_pinned.py -- DOES A FIGURE A CITING SENTENCE PRINTS FAIL ITS RECEIPT WHEN IT IS WRONG?

** r7279+70.2, on 66's r7279 ORDER: THE NARROW `\\rcpt{}` DETECTOR, SHAPE 2 OF `r7267`'s THREE. **  A sentence that
cites a receipt and prints a figure -- `7.78`, `207.8`, `0.065\\%` -- claims the receipt would FAIL if that figure were
wrong.  Most do not: the receipt prints it, or gates it one-sidedly, or holds it to a tolerance wider than the digits
the sentence prints, or never computes it.  `r7267`'s census read that shape in 16 of 20 `NUMBER` flags.

** THE RULE (pre-registered, computations/beyond_the_wall/r7279_70_figure_pin/PREDICTION.md, `0a4ec067`). **  A
FIGURE is a decimal of two or more significant digits in the claim (a revision tag is not one; `X\\%` is also read
as `X/100`).  Its ALLOWANCE is the coarser of half a unit in its last printed digit and 0.05 % of |X|.  It is PINNED
when a comparison in the cited receipt's parsed source holds it within the allowance: `== c` (with `round(.,k)`),
`abs(.. c ..) < t`, `a < . < b`, or `isclose`/`approx`/`allclose`/`assertAlmostEqual` with their tolerances; named
module constants are substituted.  A one-sided bound never pins.  Sites are every `\\rcpt{X}` in a non-appendix
paper (the claim is its sentence) and every `receipts/INDEX.md` row (the claim is its claim cell).

** WHY IT IS A GATE -- MEASURED, AND AGAINST THE BASE RATE 66 SET. **  A blinded read of 25 flagged and all 23
unflagged sites, by the same rubric: precision `17/20` = 85 %, over-reach among the unflagged `1/22` = 4.5 %, Fisher
one-sided p = 7e-8.  The wide census failed exactly this comparison (40 % against 55 %); this one does not.
  ⌗ *What the same read says, and it is the larger finding: the detector flags 93 % of figure-bearing sites, so about
    80 % of the figures the corpus prints beside a citation are not held by the receipt it cites.  The list is
    therefore BASELINED, not repaired here -- it is routed per paper -- and this gate's work is forward: a NEW figure
    printed beside a receipt that does not pin it fails, and a baselined one that comes to be pinned (or leaves the
    sentence) is STALE and fails, so the baseline can only shrink.*

** KNOWN BLIND SPOTS, named before the read and seen in it. **  A SYMBOLIC pin (sympy's exact identity behind a
printed `151.2`) and a DERIVED pin (`round(chi2/133,2)==2.10` behind a printed `279.4`) FLAG although the receipt
holds the figure; a constant used only as a DIVISOR inside another quantity's pin passes although the figure is never
computed.  The read put all three classes together at 4 of 42 claim sites.  A site the gate flags wrongly is
baselined with the rest; its verdict column says so when read.

** THE KEY is (population, paper, receipt, figure) with a COUNT, so editing a sentence's words moves nothing. **

    python3 corpus/check_figures_pinned.py
    python3 corpus/check_figures_pinned.py --write-baseline     # after a reviewed change only
"""
import ast
import glob
import os
import re
import sys
from collections import Counter
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import check_quote_pins as Q  # noqa: E402

BASELINE = os.path.join(HERE, 'figure_pin_baseline.tsv')
NUM = re.compile(r'(?<![\w.])(\d+\.\d{2,}|\d{2,}\.\d+)(?![\w.])')
REVTAG = re.compile(r'(?:r\d+\+|\+c?\d*\.?|\+)$')
DEFAULTS = {'isclose': (1e-9, 0.0), 'approx': (1e-6, 1e-12), 'allclose': (1e-5, 1e-8),
            'assertAlmostEqual': (0.0, 0.5e-7)}
SLACK = 1 + 1e-9          # a pin exactly at the allowance holds it (the float edge the read found at F05)


def figures(claim):
    """[(printed string, [(value, allowance), ...])]; a percent figure also yields value/100"""
    out = []
    for m in NUM.finditer(claim):
        if REVTAG.search(claim[max(0, m.start() - 8):m.start()]):
            continue
        s = m.group(1)
        x = float(s)
        a = max(0.5 * 10 ** -len(s.split('.')[1]), 5e-4 * abs(x))
        alts = [(x, a)]
        if re.match(r'\s*\\?%', claim[m.end():m.end() + 3]):
            alts.append((x / 100, a / 100))
        out.append((s, alts))
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


def _inner(n, consts):
    return [v for v in (_num(m, consts) for m in ast.walk(n)) if v is not None]


def pins(src):
    """[(c, t)]: a value c held to tolerance t by some comparison in the source"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    consts = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            v = _num(n.value, {})
            if v is not None:
                consts[n.targets[0].id] = v
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
                    if d is None:
                        cs = _inner(a.right, consts)
                        d = cs[0] if cs else 1.0
                    scale, a = abs(d), a.left
                if isinstance(a, ast.Call) and _fname(a) in ('abs', 'fabs') and a.args:
                    out += [(c, t * scale) for c in _inner(a.args[0], consts)]
            elif len(xs) == 3 and (all(isinstance(o, (ast.Lt, ast.LtE)) for o in ops)
                                   or all(isinstance(o, (ast.Gt, ast.GtE)) for o in ops)):
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
            out += [(c, max(ab, rel * abs(c))) for c in (_num(x, consts) for x in n.args) if c is not None]
    return out


def unpinned(claim, ps):
    return [s for s, alts in figures(claim)
            if not any(abs(abs(c) - x) <= a * SLACK and t <= a * SLACK for x, a in alts for c, t in ps)]


FILES = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}


@lru_cache(maxsize=None)
def receipt_pins(name):
    return pins(open(FILES[name], encoding='utf-8', errors='replace').read())


def _sentence(text, i):
    a = max(text.rfind('. ', 0, i), text.rfind('\n\n', 0, i)) + 1
    b = text.find('. ', i)
    return text[a:b + 1 if b >= 0 else len(text)]


def sites():
    """[(population, paper, receipt, claim)] -- r7267's census populations"""
    out = []
    for t in sorted(glob.glob(os.path.join(HERE, '*.tex'))):
        paper = os.path.basename(t)
        if paper.startswith('appendix'):
            continue
        flat = Q._flat(open(t, encoding='utf-8', errors='replace').read())
        for m in re.finditer(r'\\rcpt\{([^}]+)\}', flat):
            name = m.group(1).split(',')[0].strip()
            if name in FILES:
                claim = Q._unmark(re.sub(r'\\(?:rcpt|ldg)\{[^}]*\}', ' ', _sentence(flat, m.start())))
                out.append(('PROSE', paper, name, claim))
    for ln in open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8', errors='replace'):
        c = [x.strip() for x in re.split(r'(?<!\\)\|', ln)]
        if len(c) >= 6 and c[4].startswith('`'):
            name = os.path.basename(c[4].strip('`'))[:-3]
            if name in FILES:
                out.append(('APPENDIX', c[1], name, c[3]))
    return out


def live():
    k = Counter()
    for pop, paper, name, claim in sites():
        if figures(claim):
            for s in unpinned(claim, receipt_pins(name)):
                k[(pop, paper, name, s)] += 1
    return k


def baseline():
    out = {}
    if os.path.exists(BASELINE):
        for ln in open(BASELINE, encoding='utf-8'):
            q = ln.rstrip('\n').split('\t')
            if len(q) >= 5 and not ln.startswith('#'):
                out[tuple(q[:4])] = int(q[4])
    return out


def _seeds():
    src = ('X = 0.315162424\nassert abs(v - X) < 1e-6\ncheck("l2", abs(l2 - 7.8) < 0.3)\nassert m < 348\n'
           'assert round(q, 2) == 2.10\nassert 1.23 < w < 1.25\nassert math.isclose(z, 4.5678, rel_tol=1e-6)\n'
           'assert 41.04 < y < 41.06\nassert abs(dlnob + 0.305) < 0.005\n')
    ps = pins(src)
    cases = [('a tight named-constant pin', 'the root is 0.315162424', False),
             ('a slack pin on a nearby value', 'the multipole is 7.78', True),
             ('a one-sided bound', 'the ratio is 207.8', True),
             ('a round()==c pin', 'the reduced value 2.10', False),
             ('a bracket wider than the allowance', 'the value 1.24', True),
             ('a bracket inside the allowance', 'the value 41.05', False),
             ('an isclose pin', 'the figure 4.5678', False),
             ('a figure no check names', 'the share 46.53', True),
             ('a revision tag is not a figure', 'answered at r7267+70.1', False),
             ('a percent figure with no pin', 'a shift of 0.065\\%', True),
             ('a pin exactly at the allowance', 'the slope 0.31', False)]
    bad = [f'{lab}: expected {"flag" if want else "pass"}, got {"flag" if not want else "pass"}'
           for lab, claim, want in cases if bool(unpinned(claim, ps)) != want]
    if unpinned('a shift of 0.065\\%', pins('assert abs(r - 0.00065) < 1e-7\n')):
        bad.append('a percent figure pinned as its fraction: expected pass, got flag')
    return bad


def main():
    print()
    print('  FIGURES PINNED -- does a figure a citing sentence prints fail its receipt when it is wrong?')
    print()
    bad = _seeds()
    if bad:
        print('  ⛔ the seeds lost a direction:')
        for b in bad:
            print(f'      {b}')
        return 1
    print('    seeds hold: slack, one-sided and absent pins flag; tight, rounded, bracketed, isclose and percent pins '
          'pass; a revision tag is not a figure')
    now = live()
    if '--write-baseline' in sys.argv:
        with open(BASELINE, 'w', encoding='utf-8') as f:
            f.write(open(BASELINE, encoding='utf-8').read().split('\n# ---\n')[0] + '\n# ---\n'
                    if os.path.exists(BASELINE) else '# ---\n')
            for k in sorted(now):
                f.write('\t'.join([*k, str(now[k])]) + '\n')
        print(f'    baseline written: {len(now)} key(s), {sum(now.values())} unpinned figure(s)')
        return 0
    base = baseline()
    new = sorted((k, n - base.get(k, 0)) for k, n in now.items() if n > base.get(k, 0))
    stale = sorted((k, base[k] - now.get(k, 0)) for k in base if now.get(k, 0) < base[k])
    print(f'    {sum(now.values())} unpinned figure(s) live under {len(now)} key(s); baseline {sum(base.values())}')
    rc = 0
    if new:
        rc = 1
        print()
        for (pop, paper, name, s), d in new:
            print(f'    [UNPINNED] {paper}  {s}  cites {name[:70]}' + (f'  (+{d})' if d > 1 else ''))
        print()
        print('  ⛔ A SENTENCE PRINTS A FIGURE BESIDE A RECEIPT THAT WOULD NOT FAIL IF IT WERE WRONG.')
        print('     Pin it in the receipt within half a printed digit (or four significant figures), cite the receipt')
        print('     that does pin it, or print fewer digits.  The rule is in this file\'s docstring.')
    if stale:
        rc = 1
        print()
        for (pop, paper, name, s), d in stale:
            print(f'    [STALE] {paper}  {s}  cites {name[:70]}  -- now pinned or gone; lower the row by {d}')
        print('     (`--write-baseline` after reading them)')
    if rc == 0:
        print('  no figure is printed beside a receipt that does not pin it, beyond the baselined sites.')
    return rc


if __name__ == '__main__':
    sys.exit(main())
