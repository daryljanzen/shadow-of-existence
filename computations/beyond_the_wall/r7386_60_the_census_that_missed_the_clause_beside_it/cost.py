#!/usr/bin/env python3
"""r7386 (60) -- THE CENSUS THAT MISSED THE CLAUSE BESIDE IT.

** `r7383` ③ routed `70`'s ported fix to `S54` back to this seat to confirm or replace.  `70`'s form is
right and is CONFIRMED -- it reads `scripts/receipt_scope.py` at the pinned commit `3f30509e` instead of
live, which is `r7368` ②'s ratified rule. **  ⛔ *But the receipt was still red on a clause `70`'s change
never touched: `Ⓑ⑥` read a diff whose BASE was pinned and whose HEAD was live, so `r7370` pinning `S23`'s
commit tuple turned it red for a later revision having done work.*

⇒ ** AND `r7368` ALREADY REPAIRED THIS SHAPE IN THIS FILE, three clauses of it, leaving a note four lines
above the constants that says "three clauses below" and that A RANGE HAS TWO ENDS.  `Ⓑ⑥` is a fourth. **
  ⇒ *** A CENSUS OF A SHAPE INSIDE ONE FILE MISSED AN INSTANCE OF IT. ***

** THE ARMS. **  ⒜ base-pinned, head-live ranges across `receipts/` and `corpus/` (central 8, band
2-30).  ⒝ of those, the subset in a file that ALREADY binds a pin, where the fix costs one identifier
(central 3, band 1-10).  ⒞ the both-ends-pinned control (central 20, band 5-80).  ⒟ `S54`'s own
remaining count after this repair -- exact 0, registered because a non-zero there would be this
revision committing the defect it reports.

    python3 computations/beyond_the_wall/r7386_60_the_census_that_missed_the_clause_beside_it/cost.py
"""
import ast
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))

FRAME = 'cc0445d5'          # this revision's registration commit: the prediction, committed before this ran
S54_PREFIX = 'S54_'
#: `70`'s ported form, confirmed here: the instrument read at a commit rather than live
RS_AT = '3f30509e'

#: a name bound to a hex literal of abbreviation length -- the pin a file already carries
_PIN_BIND = re.compile(r"^\s*([A-Z][A-Z0-9_]*)\s*=\s*['\"]([0-9a-f]{7,12})['\"]", re.M)
#: the live right-hand ends.  `origin/main` and `HEAD` both move; a sha and a bound pin do not.
_LIVE_END = ('HEAD', 'origin/main', 'origin/HEAD')
#: a range expression, in the three spellings this corpus writes
_RANGE = re.compile(r"""['"]?\{?([A-Za-z_][A-Za-z0-9_]*|[0-9a-f]{7,12})\}?(?:~\d+)?\.\.\.?"""
                    r"""\{?([A-Za-z_][A-Za-z0-9_/]*|[0-9a-f]{7,12})\}?['"]?""")
RESULT = {}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


def tracked():
    out = []
    for p in ('receipts', 'corpus'):
        out += [x for x in git('ls-files', p).split('\n') if x.endswith('.py')]
    return sorted(set(out))


def code_lines(rel):
    """(lineno, text) for lines outside the module docstring that are not comments"""
    try:
        src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    except OSError:
        return [], ''
    parts = src.split('"""')
    body = '"""'.join(parts[2:]) if len(parts) >= 3 else src
    off = src.count('\n', 0, len(src) - len(body))
    out = []
    for i, ln in enumerate(body.split('\n'), start=off + 1):
        s = ln.strip()
        if s and not s.startswith('#'):
            out.append((i, ln))
    return out, src


def classify(rel):
    """[(lineno, kind, text)] -- BASE_PINNED_HEAD_LIVE / BOTH_PINNED / OTHER for each range expression

    ** An end is PINNED when it is a hex literal or a name this file binds to one; it is LIVE when it is
    `HEAD` or a remote ref. **  *The defect is a historical claim read over a range only one of whose
    ends is fixed, which is `r7368` ②'s rule; a restraint about work not yet landed is correctly live
    and is that rule's own carve-out, so the classification is of the RANGE and the receipt says which
    clauses state history.*
    """
    lines, src = code_lines(rel)
    pins = {m.group(1) for m in _PIN_BIND.finditer(src)}
    out = []
    for no, ln in lines:
        if '..' not in ln or 'git' not in ln and 'log' not in ln and 'diff' not in ln:
            continue
        for m in _RANGE.finditer(ln):
            a, b = m.group(1), m.group(2)
            a_pin = bool(re.fullmatch(r'[0-9a-f]{7,12}', a)) or a in pins
            b_pin = bool(re.fullmatch(r'[0-9a-f]{7,12}', b)) or b in pins
            b_live = b in _LIVE_END
            if a_pin and b_live:
                out.append((no, 'BASE_PINNED_HEAD_LIVE', ln.strip()[:150], bool(pins)))
            elif a_pin and b_pin:
                out.append((no, 'BOTH_PINNED', ln.strip()[:150], bool(pins)))
    return out



#: ⛔⛭⛭⛭ ** THE SHAPE IS NOT THE DEFECT, AND THIS IS THE FOURTH TIME IN THREE REVISIONS A DETECTOR OF
#: MINE HAS HAD TO BE TOLD SO. **  *Arm ⒟ came in at `2` where an exact `0` was registered, and both
#: sites are the LIVE-REPORTING halves of clauses `r7368` and this revision already repaired: the range
#: is read to be PRINTED beside a pinned assertion, which is exactly what `r7368` ② requires.*
#:   ⇒ ** A base-pinned, head-live range is a defect only when its value reaches an ASSERTION.  Read
#:     off the syntax tree: the name the range is bound to, and whether that name appears inside a
#:     `check`, `gate` or `assert`. **
#: ⌗ *`S57`'s token stream, `r7374`'s structural consumption test, and now this -- every one of them a
#: shape counted where a use was meant.*
_ASSERTING = ('check', 'gate', 'assert')


def asserted_names(src):
    """names that reach a check/gate/assert call, and names bound to a range expression"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return set(), {}
    used = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assert):
            used |= {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
        elif isinstance(node, ast.Call):
            fn = node.func
            name = fn.id if isinstance(fn, ast.Name) else getattr(fn, 'attr', '')
            if name in _ASSERTING:
                #: ⛭⛭ ** THE LABEL IS NOT THE CLAIM. **  *`check(label, cond)` takes the sentence first
                #: and the condition second, and a repaired clause PRINTS its live figure in the label
                #: while asserting the pinned one.  Walking the whole call read all three sites as
                #: ASSERTED because `{len(_s23_live)}` stands in the label f-string.  ⇒ Only the
                #: condition arguments count -- `node.args[1:]` -- which is the structural difference
                #: between reporting a figure and claiming it.*
                for _arg in node.args[1:]:
                    used |= {n.id for n in ast.walk(_arg) if isinstance(n, ast.Name)}
                for _kw in node.keywords:
                    if _kw.arg != 'label':
                        used |= {n.id for n in ast.walk(_kw.value) if isinstance(n, ast.Name)}
    bound = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name):
            bound.setdefault(node.targets[0].id, []).append(
                (getattr(node, 'lineno', 0), getattr(node, 'end_lineno', 0) or getattr(node, 'lineno', 0)))
    return used, bound


#: ⛔⛭⛭⛭ ** AND A LIVE VALUE ASSERTED AS A DIRECTION IS NOT A DEFECT EITHER -- `r7368` ②'s own
#: carve-out, in its own words: a live read asserted only as a CEILING, a DIRECTION or a MAJORITY. **
#: *So ASSERTED splits again: a live name compared with `<`, `>`, `<=` or `>=` states a direction and
#: moves correctly with the work; one in `==`, `!=`, `in` or a bare truth test states a figure and is
#: the defect.  The third split this one detector has needed, after shape-vs-use and label-vs-condition.*
_DIRECTIONAL = (ast.Lt, ast.Gt, ast.LtE, ast.GtE)


def _how_asserted(src, name):
    """DIRECTION when every comparison of `name` inside an asserting call is an inequality"""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 'FIGURE'
    seen = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        fname = fn.id if isinstance(fn, ast.Name) else getattr(fn, 'attr', '')
        if fname not in _ASSERTING:
            continue
        for _arg in node.args[1:]:
            for sub in ast.walk(_arg):
                if isinstance(sub, ast.Compare) and any(
                        isinstance(n, ast.Name) and n.id == name for n in ast.walk(sub)):
                    seen.append(all(isinstance(o, _DIRECTIONAL) for o in sub.ops))
    if not seen:
        return 'FIGURE'
    return 'DIRECTION' if all(seen) else 'FIGURE'


def use_of(rel, no):
    """ASSERTED when the range at line `no` is bound to a name a check/gate/assert reads; REPORTED when
    it is not.  An UNBOUND range -- one written inline inside a call -- counts ASSERTED, the direction
    that counts against this seat."""
    try:
        src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    except OSError:
        return 'ASSERTED'
    used, bound = asserted_names(src)
    for nm, spans in bound.items():
        if any(a <= no <= b for a, b in spans):
            if nm not in used:
                return 'REPORTED'
            return 'ASSERTED-' + _how_asserted(src, nm)
    return 'ASSERTED-FIGURE'

def measure():
    if RESULT:
        return RESULT
    shape, both = [], []
    for rel in tracked():
        for no, kind, txt, has_pin in classify(rel):
            (shape if kind == 'BASE_PINNED_HEAD_LIVE' else both).append((rel, no, txt, has_pin))
    shape = [(rel, no, txt, hp, use_of(rel, no)) for rel, no, txt, hp in shape]
    asserted = [x for x in shape if x[4] == 'ASSERTED-FIGURE']
    with_pin = [x for x in asserted if x[3]]
    in_s54 = [x for x in asserted if S54_PREFIX in os.path.basename(x[0])]
    RESULT.update(shape=shape, both=both, with_pin=with_pin, in_s54=in_s54, asserted=asserted)
    return RESULT


def score(got, lo, hi):
    return 'INSIDE' if lo <= got <= hi else ('BELOW' if got < lo else 'ABOVE')


def main():
    print(__doc__)
    print(f'    frame {FRAME}')
    print()
    _s54 = [x for x in tracked() if S54_PREFIX in os.path.basename(x)]
    _src54 = open(os.path.join(ROOT, _s54[0]), encoding='utf-8').read() if _s54 else ''
    print(f'  70`s PORTED FORM, CONFIRMED: S54 reads the instrument at {RS_AT} rather than live: '
          f'{RS_AT in _src54}')
    print()
    R = measure()
    print(f'  THE SCAN -- {len(tracked())} tracked python file(s) under receipts/ and corpus/')
    print(f'      ⒜ BASE-PINNED, HEAD-LIVE -- the SHAPE {len(R["shape"])}, of which ASSERTED '
          f'{len(R["asserted"])} and REPORTED {len(R["shape"]) - len(R["asserted"])} '
          f'(central 8, band 2-30 on the shape) {score(len(R["shape"]), 2, 30)}')
    from collections import Counter as _C
    print(f'         by use: {dict(_C(x[4] for x in R["shape"]))}')
    print(f'      ⒝ of those, in a file already binding a pin {len(R["with_pin"])} '
          f'(central 3, band 1-10) {score(len(R["with_pin"]), 1, 10)}')
    print(f'      ⒞ BOTH ENDS PINNED {len(R["both"])} (central 20, band 5-80) '
          f'{score(len(R["both"]), 5, 80)}')
    print(f'      ⒟ remaining in S54 itself {len(R["in_s54"])} (exact 0) '
          f'{"HIT" if not R["in_s54"] else "MISS"}')
    print()
    print('  EVERY BASE-PINNED, HEAD-LIVE SITE')
    for rel, no, txt, has_pin, use in R['shape']:
        print(f'      {rel}:{no}  [{use}]  (file binds a pin: {has_pin})')
        print(f'         {txt}')
    print()
    if R['in_s54']:
        print('  ⛔ S54 STILL HOLDS THE SHAPE -- the revision reporting the defect committed it:')
        for rel, no, txt, _p, _u in R['in_s54']:
            print(f'      {rel}:{no}  {txt}')
        print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
