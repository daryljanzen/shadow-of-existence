#!/usr/bin/env python3
"""r7648 (60) -- THE SWEEP FOR ABSOLUTE BOUNDS STANDING IN FOR RELATIVE CLAIMS.

** THE ORDER (`r7647`, 69), from cc66's find at `r7645+cc66.69`: ** a gate read `abs(d_om) > 0.01`
-- an ABSOLUTE bound on Omega_m.  At 0.2973 that bound is 3.4 PER CENT, standing beside a claim of a
thirtieth of one per cent, so it passed the namesake's 0.20% and the arm of record's 2.16% alike and
** could never fail for what it names. **  Sweep for the class, count it, repair this seat's, route
the rest.

** THE DETECTOR IS `PREDICTION.md`'s, FIXED BEFORE IT WAS RUN, AND IT IS STATIC -- it parses sources
and runs no receipt. **  A `(receipt, variable)` pair is a CANDIDATE when, in one file:
  i   an ABSOLUTE bound: `abs(V) <|> t`, `abs(V +- c) <|> t`, with `t` a numeric literal and the
      bounded expression carrying NO division by a constant and NO factor of 100;
  ii  the receipt's OWN NORMALISER for the same `V`: `V / S * 100`, `100 * V / S`, `abs(V / S) * 100`
      -- the only way a scale is knowable without supplying physics, and exactly how cc66's case was
      visible, since the receipt that bounded `d_om` absolutely also printed `abs(d_om / 0.2973)*100`;
  iii the bound in per-cent terms, `100*t/|S|`, is GREATER THAN ONE PER CENT -- the single free
      threshold, named in the registration rather than chosen once the output was read.
Each candidate is then ADJUDICATED BY READING the sentence beside it.  *The static test supplies
recall, the reading supplies precision, and the candidate list is printed whole so the adjudication
can be checked rather than taken.*
"""
import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RCPT = os.path.join(ROOT, 'receipts')
PCT_FLOOR = 1.0                      # condition iii, from PREDICTION.md
_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


# ---------------------------------------------------------------- the parser
def _lit(n, consts):
    """the numeric value of a node, or None -- literals, unary minus, names bound to literals"""
    if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
        return float(n.value)
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        v = _lit(n.operand, consts)
        return None if v is None else -v
    if isinstance(n, ast.Name):
        return consts.get(n.id)
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div):
        a, b = _lit(n.left, consts), _lit(n.right, consts)
        return a / b if a is not None and b not in (None, 0.0) else None
    return None


def _names(n):
    return {m.id for m in ast.walk(n) if isinstance(m, ast.Name)}


def _has_div_or_100(n, consts):
    """does this expression already normalise -- a division by a constant, or a factor of 100?"""
    for m in ast.walk(n):
        if isinstance(m, ast.BinOp) and isinstance(m.op, ast.Div) and _lit(m.right, consts) is not None:
            return True
        if isinstance(m, ast.BinOp) and isinstance(m.op, ast.Mult):
            for s in (m.left, m.right):
                if _lit(s, consts) == 100.0:
                    return True
    return False


def _fname(call):
    f = call.func
    return f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''


def normalisers(tree, consts):
    """{V: {S}} -- V/S appearing inside a per-cent context (a factor of 100)"""
    out = {}
    for n in ast.walk(tree):
        if not (isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult)):
            continue
        hund = [s for s in (n.left, n.right) if _lit(s, consts) == 100.0]
        if not hund:
            continue
        other = n.right if _lit(n.left, consts) == 100.0 else n.left
        for m in ast.walk(other):
            if isinstance(m, ast.BinOp) and isinstance(m.op, ast.Div):
                S = _lit(m.right, consts)
                if S is None or S == 0.0:
                    continue
                for v in _names(m.left):
                    out.setdefault(v, set()).add(abs(S))
    return out


def abs_bounds(tree, consts):
    """[(V, t, text)] -- abs(... V ...) compared to a numeric literal, the inside NOT normalised"""
    out = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Compare) or len(n.comparators) != 1:
            continue
        if not isinstance(n.ops[0], (ast.Lt, ast.LtE, ast.Gt, ast.GtE)):
            continue
        for a, b in ((n.left, n.comparators[0]), (n.comparators[0], n.left)):
            if not (isinstance(a, ast.Call) and _fname(a) in ('abs', 'fabs') and a.args):
                continue
            t = _lit(b, consts)
            if t is None or t <= 0.0:
                continue
            inner = a.args[0]
            if _has_div_or_100(inner, consts):
                continue
            for v in _names(inner):
                out.append((v, t, getattr(n, 'lineno', 0)))
    return out


def sweep_source(src):
    """[(V, t, pct, S, line)] candidates, plus the count of absolute bounds with NO normaliser"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return [], 0
    consts = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            v = _lit(n.value, {})
            if v is not None:
                consts[n.targets[0].id] = v
    norm = normalisers(tree, consts)
    cands, blind = [], 0
    for v, t, line in abs_bounds(tree, consts):
        if v not in norm:
            blind += 1
            continue
        for S in sorted(norm[v]):
            pct = 100.0 * t / S
            if pct > PCT_FLOOR:
                cands.append((v, t, pct, S, line))
    return cands, blind


print(__doc__)
print("=" * 108)
print("  r7648 (60) -- absolute bounds standing in for relative claims")
print("=" * 108)

# ---------------------------------------------------------------- PART 0, the seed
print("\nPART 0 -- ⚑ THE SEED: THE DETECTOR ON cc66's DEFECT, BOTH BEFORE AND AFTER ITS REPAIR")
print("  *A sweep that cannot find the one case it was built from is not a sweep, and one that also")
print("  flags the repair would be a detector of the shape rather than of the defect.*")
_BEFORE = """
d_om = fit()
print(f"Omega_m moves {abs(d_om / 0.2973) * 100:.2f}%")
if not (abs(d_om) > 0.01):
    fail.append("Omega_m did not move")
"""
_AFTER = """
d_om = fit()
print(f"Omega_m moves {abs(d_om / 0.2973) * 100:.2f}%")
_POM = 100 * d_om / 0.2973
if not (abs(_POM) > 1 / 30. and abs(_POM + 2.164128) < 5e-4):
    fail.append("Omega_m moved wrong")
"""
_b, _ = sweep_source(_BEFORE)
_a, _ = sweep_source(_AFTER)
print(f"      pre-repair  : {[(v, t, round(p, 2)) for v, t, p, _s, _l in _b]}")
print(f"      post-repair : {[(v, t, round(p, 2)) for v, t, p, _s, _l in _a]}")
check("⛭ the detector FLAGS cc66's pre-repair form -- `abs(d_om) > 0.01` beside its own "
      "`abs(d_om / 0.2973) * 100`, at 3.36 per cent", any(v == 'd_om' and abs(p - 3.3636) < 0.01
                                                          for v, _t, p, _s, _l in _b))
check("⛭ and does NOT flag the repaired form, whose bound is on the per-cent quantity itself",
      not any(v in ('d_om', '_POM') for v, _t, _p, _s, _l in _a))

# ---------------------------------------------------------------- PART 1, the corpus
print("\nPART 1 -- THE SWEEP OVER EVERY RECEIPT")
files = []
for dp, _dn, fn in os.walk(RCPT):
    for f in fn:
        if f.endswith('.py'):
            files.append(os.path.join(dp, f))
files.sort()
ALL, blind_total, with_bounds = [], 0, 0
for p in files:
    src = open(p, encoding='utf-8', errors='replace').read()
    c, b = sweep_source(src)
    blind_total += b
    if c or b:
        with_bounds += 1
    for v, t, pct, S, line in c:
        ALL.append((os.path.relpath(p, ROOT), v, t, pct, S, line))
print(f"      receipts parsed                                   : {len(files)}")
print(f"      receipts carrying an absolute bound               : {with_bounds}")
print(f"      ⛔ absolute bounds with NO normaliser (invisible)  : {blind_total}")
print(f"      CANDIDATE (receipt, variable) pairs               : {len(ALL)}")
check(f"⛭ ARM ③ -- the candidate set is under 200 pairs, so adjudicating it by reading is "
      f"affordable ({len(ALL)})", len(ALL) < 200)
print("  ⌗ *The blind count is printed because the net's own limit was registered: a bound whose")
print("  scale its receipt never writes down is invisible here, and that is a stated limit rather")
print("  than an absence of the defect.*")

print(f"\n      {'per cent':>9}  {'bound':>12}  {'scale':>12}  {'variable':<18} line  receipt")
for rel, v, t, pct, S, line in sorted(ALL, key=lambda r: -r[3]):
    print(f"      {pct:>9.2f}  {t:>12.6g}  {S:>12.6g}  {v:<18} {line:>4}  {rel[9:][:62]}")

import json
json.dump([dict(receipt=r, var=v, bound=t, pct=p, scale=s, line=l)
           for r, v, t, p, s, l in sorted(ALL, key=lambda r: -r[3])],
          open(os.path.join(HERE, 'candidates.json'), 'w'), indent=1)
print(f"\n      the whole candidate list is written to `candidates.json` beside this receipt, so the")
print(f"      adjudication below can be checked rather than taken.")

print("\n" + "=" * 108)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
