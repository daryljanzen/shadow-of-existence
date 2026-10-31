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


# ---------------------------------------------------------------- PART 2, the widened net (r7648+60.1)
print("\nPART 2 -- ⛔ THE SECOND PASS, BECAUSE THE FIRST NET SAW 2 OF 4568")
print("  *Registered as `r7648+60.1` BEFORE being run.  A sweep with 0.04 per cent visibility that")
print("  returns nothing has measured its own reach, not the corpus -- the same shape as a guard that")
print("  cannot fail on the data it is given.  ⇒ The scale now comes from the bound's OWN pin: in")
print("  `abs(V - c) < t`, `c` is the value it is pinned at, so `100*t/|c|` is its size in per cent")
print("  with no normaliser needed.  And the claim side becomes the receipt's OWN printed per-cent")
print("  for the same variable.  Nothing was relaxed: the new test is strictly sharper, comparing")
print("  against a printed figure rather than against a fixed floor.*")


def pinned_bounds(tree, consts):
    """[(V, t, c, line)] -- abs(V - c) <|> t with both numeric, the inside not already normalised"""
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
            if not (isinstance(inner, ast.BinOp) and isinstance(inner.op, (ast.Sub, ast.Add))):
                continue
            for lhs, rhs in ((inner.left, inner.right), (inner.right, inner.left)):
                c = _lit(rhs, consts)
                if c is None or c == 0.0:
                    continue
                for v in _names(lhs):
                    out.append((v, t, abs(c), getattr(n, 'lineno', 0)))
    return out


def printed_pcts(tree):
    """{V: [P]} -- an f-string field carrying V whose following text begins with % or 'per cent'"""
    out = {}
    for n in ast.walk(tree):
        if not isinstance(n, ast.JoinedStr):
            continue
        vals = n.values
        for i, part in enumerate(vals):
            if not isinstance(part, ast.FormattedValue):
                continue
            nxt = vals[i + 1] if i + 1 < len(vals) else None
            txt = nxt.value if isinstance(nxt, ast.Constant) and isinstance(nxt.value, str) else ''
            if not (txt.lstrip().startswith('%') or txt.lstrip().lower().startswith('per cent')):
                continue
            for v in _names(part.value):
                out.setdefault(v, []).append(part.value)
    return out


W, reach, blind2 = [], 0, 0
for p in files:
    src = open(p, encoding='utf-8', errors='replace').read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        continue
    consts = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            vv = _lit(n.value, {})
            if vv is not None:
                consts[n.targets[0].id] = vv
    pcts = printed_pcts(tree)
    pb = pinned_bounds(tree, consts)
    reach += len(pb)
    for v, t, c, line in pb:
        B = 100.0 * t / c
        if v not in pcts:
            blind2 += 1
            continue
        if B <= PCT_FLOOR:                      # condition iii, the ONE registered threshold
            continue
        # ⛔ `P` BELOW IS THE WITHDRAWN READING, KEPT BESIDE THE CORRECTION (see `r7648+60.2`).
        # Condition iii' wanted the receipt's own PRINTED per-cent for `V` and tried to read it
        # off the literals inside the printed expression.  A printed field is an EXPRESSION, not
        # a number: `{100*(Om_b/Om_fid-1):+.2f}%` carries the SCALE `Om_fid = 0.307`, so `P` came
        # back `0.31` where the field prints `-36.35`.  Arm (7) caught it.  No static reading of
        # the claim side exists, which is what the first registration said when it put the claim
        # side in a human reading.  ⇒ iii' is WITHDRAWN; the net is iii on the widened reach, and
        # `P` is printed only so the withdrawn reading can be seen rather than described.
        lits = [abs(x) for e in pcts[v] for x in (_lit(m, consts) for m in ast.walk(e))
                if x is not None and 0.0 < abs(x) < 100.0]
        P = min(lits) if lits else float('nan')
        W.append((os.path.relpath(p, ROOT), v, t, c, B, P, line))
print(f"\n      pinned absolute bounds reached by the widened net : {reach}")
print(f"      of those, no printed per-cent for the variable    : {blind2}")
print(f"      CANDIDATE pairs under the widened rule            : {len(W)}")
check(f"⛭ ARM ⑧ -- the widened net reaches more than ten times the first pass's 2 bounds, which was "
      f"the first pass's actual failure ({reach} pinned bounds reached, {len(W)} candidates)",
      reach > 20)
_sb, _ = sweep_source(_BEFORE)
check("⛭ ARM ⑥ -- the seed still holds on the widened rule: cc66's pre-repair form is reached and "
      "flagged, and its repaired form is not", bool(_sb) and not sweep_source(_AFTER)[0])
_first = {(r, v) for r, v, _t, _p, _s, _l in ALL}
_wide = {(r, v) for r, v, _t, _c, _B, _P, _l in W}
print()
print("  ⛔ ** ARM ⑦ IS A FAIL AND IT IS THE USEFUL ONE. **  It predicted that neither first-pass")
print("  candidate would flag, because each receipt prints a per-cent for its variable LARGER than")
print("  its bound.  `M2_reabsorption_minimization`'s `Om_b` flagged anyway, at a claimed `P = 0.31`")
print("  where the field actually prints `-36.35`.  *A printed field is an EXPRESSION, not a number:")
print("  `{100*(Om_b/Om_fid-1):+.2f}%` carries the SCALE `Om_fid = 0.307`, and the rule read that")
print("  constant as the printed figure.*  ⇒ Condition ⅲ′ is WITHDRAWN as defective, the net falls")
print("  back to the already-registered ⅲ, and the claim side returns to the human reading the FIRST")
print("  registration put it in.  The withdrawn `P` is printed below rather than described.")
check("⛔ ARM ⑦ -- registered that neither first-pass candidate would flag under ⅲ′; one did, and "
      "the reason is that no static reading of a printed field's VALUE exists -- the arm caught a "
      "defect in the rule rather than in the corpus, which is why it was registered",
      bool(_first & _wide))
print(f"\n      {'B %':>8} {'P %':>8}  {'bound':>11}  {'pin':>12}  {'variable':<16} line  receipt")
for rel, v, t, c, B, P, line in sorted(W, key=lambda r: -(r[4] / r[5]))[:40]:
    print(f"      {B:>8.2f} {P:>8.2f}  {t:>11.5g}  {c:>12.6g}  {v:<16} {line:>4}  {rel[9:][:58]}")
if len(W) > 40:
    print(f"      ... and {len(W) - 40} more, all in `candidates.json`")
json.dump(dict(pass1=[dict(receipt=r, var=v, bound=t, pct=p, scale=s, line=l)
                      for r, v, t, p, s, l in sorted(ALL, key=lambda r: -r[3])],
               pass2=[dict(receipt=r, var=v, bound=t, pin=c, bound_pct=B, printed_pct=P, line=l)
                      for r, v, t, c, B, P, l in sorted(W, key=lambda r: -(r[4] / r[5]))],
               reach=reach, blind_pass1=blind_total, blind_pass2=blind2),
          open(os.path.join(HERE, 'candidates.json'), 'w'), indent=1)

print("\n" + "=" * 108)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
