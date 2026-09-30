"""r7079 (70) -- over the twenty-five carriers: does each one DERIVE its number, or HOLD it?

The SENTINEL test (pre-registered in PREDICTION.md beside this file).  In a scratch copy of the carrier,
every source occurrence of the number -- code and strings alike -- is replaced by a different value of the
same form, and the copy is run fresh with the carrier's own directory, `__file__` and `sys.path`.

  output still carries the number                       -> DERIVED
  fails at an assert whose line holds the replaced value -> DERIVED-AND-PINNED
  fails anywhere else                                    -> INCONCLUSIVE (a held input may feed other checks)
  exits 0 and the output no longer carries it            -> HELD
  the number also sits in a file the carrier reads/runs  -> INCONCLUSIVE, whatever the run says
  not in the carrier's source at all, but printed        -> DERIVED (no sentinel needed; dependency check applies)

The class is MECHANICAL.  Whether a HELD number is the paper's own result or a datum read from the world
is 66's read, not this script's.  No receipt is edited: the copies live in a temporary directory.

Usage:  python3 derive_or_hold.py [--jobs N] [--only carrier_prefix,...]
"""
import ast
import glob
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7069_70_transposition_gate'))
import confirm_transpositions as C          # noqa: E402  (its out_carries, with the r7073 mantissa fix)

LOG = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7069_70_transposition_gate', 'confirm_log.txt')
CONTROLS = [   # (carrier, number, expected classes) -- the calibration, a condition of delivery
    ('P16_validate_bbn', '2.5671', ('DERIVED', 'DERIVED-AND-PINNED')),
    ('P16_validate_bbn', '4.4611', ('DERIVED', 'DERIVED-AND-PINNED')),
    ('P15_the_low_ell_minimum_is_at_ell_four', '0.926', ('HELD', 'HELD-BUT-CONSTRAINED')),
    ('P16_nariai_welds', '7.06', ('HELD', 'HELD-BUT-CONSTRAINED')),
]
REPORTED_CONTROL = ('P15_the_exact_transmission_ratios_are_recomputed_and_the_offset_saturates', '0.926')
GLYPH = {Fraction(3, 4): '¾', Fraction(1, 4): '¼', Fraction(1, 2): '½', Fraction(3, 8): '⅜',
         Fraction(1, 8): '⅛', Fraction(5, 8): '⅝', Fraction(7, 8): '⅞', Fraction(6, 5): None}


def pairs_from_log():
    out = []
    for l in open(LOG, encoding='utf-8'):
        m = re.match(r'CONFIRMED\s+(\S+)\s+(\S+)\s+.*\|\s*(\S+)', l)
        if m:
            paper, tok, car = m.groups()
            full = [n for n in C.IDX if n.startswith(car)]
            out.append((paper, tok, full[0] if len(full) == 1 else car))
    return out


# ---------------------------------------------------------------- the sentinel replacement
def _dec_sentinel(s):
    """a different decimal with the same number of places, so the code stays valid"""
    places = len(s.split('.')[1]) if '.' in s else 0
    v = float(s) * 1.37 + 0.11
    return f'{v:.{places}f}' if places else str(int(v))


def _last_digit(s):
    """the smallest change at the literal's own precision: one unit in its last place"""
    if '.' in s:
        places = len(s.split('.')[1])
        return f'{float(s) + 10 ** -places:.{places}f}'
    return str(int(s) + 1)


def replace(src, tok, small=False):
    """returns (new source, number of replacements, the sentinel values used)"""
    n = 0
    used = set()
    sent = _last_digit if small else _dec_sentinel
    if '/' in tok:
        if small:
            return src, 0, used                     # a fraction has no last place; the large run stands alone
        p, q = (abs(int(x)) for x in tok.lstrip('-').split('/'))
        fr = Fraction(p, q)
        p2 = p + q                                  # (p+q)/q -- a different value, same denominator
        used.add(f'{p2}/{q}')

        def sub(pat, rep, s):
            nonlocal n
            s2, k = re.subn(pat, rep, s)
            n += k
            return s2
        src = sub(rf'((?:Rational|Fraction|S)\(\s*-?){p}(\s*,\s*){q}(\s*\))', rf'\g<1>{p2}\g<2>{q}\g<3>', src)
        src = sub(rf'(?<![\w.]){p}(\s*/\s*){q}(?![\w.\d])', rf'{p2}\g<1>{q}', src)
        src = sub(rf'(\\t?frac\{{){p}(\}}\{{){q}(\}})', rf'\g<1>{p2}\g<2>{q}\g<3>', src)
        g = GLYPH.get(fr)
        if g:
            k = src.count(g)
            src = src.replace(g, f'{p2}/{q}')
            n += k
        # the fraction's decimal, when it is written out (0.375, 0.125, 1.2, 0.75)
        dec = float(fr)

        def dsub(m):
            nonlocal n
            if abs(float(m.group(0)) - dec) < 1e-12:
                n += 1
                s2 = _dec_sentinel(m.group(0))
                used.add(s2)
                return s2
            return m.group(0)
        src = re.sub(r'(?<![\w.])\d+\.\d+(?![\d])', dsub, src)
        return src, n, used
    if '.' in tok:
        places = len(tok.split('.')[1])
        target = round(float(tok), places)

        def dsub(m):
            nonlocal n
            mant = m.group(1)
            if '.' in mant and len(mant.split('.')[1]) >= places and round(float(mant), places) == target:
                n += 1
                s2 = sent(mant)
                used.add(s2)
                return s2 + (m.group(2) or '')
            if '.' not in mant and float(tok) == int(float(tok)) and int(mant) == int(float(tok)):
                n += 1
                s2 = sent(mant)
                used.add(s2)
                return s2 + (m.group(2) or '')
            return m.group(0)
        src = re.sub(r'(?<![\w.])(\d+(?:\.\d+)?)([eE][-+]?\d+)?(?![\w.]|\d)', dsub, src)
        return src, n, used
    s2 = sent(tok)
    used.add(s2)
    src, n = re.subn(rf'(?<![\w.]){tok}(?![\w.]|\d)', s2, src)
    return src, n, used


def carries(txt, tok):
    if '/' in tok:
        fr = Fraction(abs(int(tok.lstrip('-').split('/')[0])), int(tok.split('/')[1]))
        if GLYPH.get(fr) and GLYPH[fr] in txt:
            return True
    return C.out_carries(txt, tok)


# ---------------------------------------------------------------- what the carrier reads or runs
def dependencies(path, src):
    d = os.path.dirname(path)
    deps = set()
    try:
        tree = ast.parse(src)
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            for nm in names:
                for base in (d, ROOT):
                    cand = os.path.join(base, *nm.split('.')) + '.py'
                    if os.path.exists(cand):
                        deps.add(cand)
    except SyntaxError:
        pass
    for f in os.listdir(d):
        fp = os.path.join(d, f)
        if fp == path or not os.path.isfile(fp):
            continue
        stem = f[:-3] if f.endswith('.py') else f
        if len(stem) > 4 and stem in src:
            deps.add(fp)
    for name in re.findall(r"['\"]([A-Za-z0-9_]{12,})(?:\.py)?['\"]", src):
        if name in C.IDX and C.IDX[name] != path:
            deps.add(C.IDX[name])
    return sorted(deps)


PIN = re.compile(r'\bassert\b|\bcheck\(|\breport\(|\bok\s*&=')


def dep_holds(deps, tok):
    hits = []
    for fp in deps:
        try:
            s = open(fp, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        live = '\n'.join(l for l in s.splitlines()
                         if not l.lstrip().startswith('#') and not PIN.search(l))
        if replace(live, tok)[1]:
            hits.append(os.path.relpath(fp, ROOT))
    return hits


# ---------------------------------------------------------------- the runs
WRAP = r'''
import sys, os
orig, copy = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.dirname(orig))
sys.argv = [orig]
g = {"__name__": "__main__", "__file__": orig, "__builtins__": __builtins__}
exec(compile(open(copy, encoding="utf-8").read(), orig, "exec"), g)
'''


def run(orig, src, tmp):
    copy = os.path.join(tmp, os.path.basename(orig))
    open(copy, 'w', encoding='utf-8').write(src)
    try:
        r = subprocess.run([sys.executable, '-c', WRAP, orig, copy], cwd=os.path.dirname(orig),
                           capture_output=True, text=True, timeout=2400)
        return r.returncode, (r.stdout + r.stderr).replace('−', '-')
    except subprocess.TimeoutExpired:
        return 'timeout', ''


def failing_line(out, orig):
    ln = None
    for m in re.finditer(r'File "([^"]+)", line (\d+)', out):
        if os.path.abspath(m.group(1)) == os.path.abspath(orig):
            ln = int(m.group(2))
    return ln


FAILMARK = re.compile(r'\bFAIL|✗|✘|\bfail\(s\)|AssertionError|Traceback')


def pinned_by(out0, out1, new_src, orig, used):
    """did the change fail a check that holds the replaced literal?  Either an assert/check frame whose
    source line holds a sentinel, or a NEW failure line in the output that prints a sentinel value"""
    ln = failing_line(out1, orig)
    if ln:
        lines = new_src.splitlines()
        ctx = '\n'.join(lines[max(0, ln - 3):ln])
        if any(u in ctx for u in used) and PIN.search(ctx):
            return f'assert at line {ln}: {lines[ln - 1].strip()[:90]}'
    base = set(out0.splitlines())
    for l in out1.splitlines():
        if l not in base and FAILMARK.search(l) and any(u in l for u in used):
            return f'new failure line: {l.strip()[:110]}'
    return None


def sentinel(orig, src, tok, out0, tmp, small):
    new, k, used = replace(src, tok, small=small)
    if k == 0:
        return None
    rc, out = run(orig, new, tmp)
    r = {'rc': rc, 'carries': carries(out, tok), 'replaced': k}
    if rc not in (0, 'timeout') and not r['carries']:
        r['pinned'] = pinned_by(out0, out, new, orig, used)
        ln = failing_line(out, orig)
        r['fails at'] = (f'line {ln}: {new.splitlines()[ln - 1].strip()[:90]}' if ln else
                         next((l.strip()[:110] for l in out.splitlines() if FAILMARK.search(l)
                               and l not in set(out0.splitlines())), 'no frame, no new failure line'))
    return r


def classify(job):
    paper, tok, car = job
    orig = C.IDX.get(car)
    if not orig:
        return job, 'INCONCLUSIVE', f'carrier {car} not found', {}
    src = open(orig, encoding='utf-8').read()
    held_in_dep = dep_holds(dependencies(orig, src), tok)
    with tempfile.TemporaryDirectory() as tmp:
        rc0, out0 = run(orig, src, tmp)
        info = {'baseline': (rc0, carries(out0, tok)), 'dependency holds': held_in_dep or 'none'}
        if rc0 != 0 or not info['baseline'][1]:
            return job, 'INCONCLUSIVE', 'the unmodified carrier does not run clean and print it here', info
        big = sentinel(orig, src, tok, out0, tmp, small=False)
        if big is None:
            cls = 'INCONCLUSIVE' if held_in_dep else 'DERIVED'
            return job, cls, 'not in the carrier source; printed by its arithmetic' + (
                ' -- but a file it reads or runs holds it' if held_in_dep else ''), info
        sm = sentinel(orig, src, tok, out0, tmp, small=True)
    info['large'] = big
    if sm:
        info['last-digit'] = sm
    runs = [r for r in (big, sm) if r]
    if any(r['rc'] == 'timeout' for r in runs):
        cls, why = 'INCONCLUSIVE', 'a sentinel run timed out'
    elif any(r['carries'] for r in runs):
        cls, why = 'DERIVED', 'the number survives the removal of every literal of it'
    elif any(r.get('pinned') for r in runs):
        cls, why = 'DERIVED-AND-PINNED', 'the replaced literal is checked against a computation, and fails'
    elif all(r['rc'] == 0 for r in runs):
        cls, why = 'HELD', 'exits 0 with the number gone: written in, and nothing fails if it is false'
    elif sm and sm['rc'] == 0:
        cls, why = ('HELD-BUT-CONSTRAINED', 'written in; a last-digit change passes, and only the large change '
                    'fails, at a check away from the literal')
    else:
        cls, why = 'INCONCLUSIVE', 'fails away from the literal: a held input may feed other checks'
    if held_in_dep and cls in ('DERIVED', 'HELD', 'HELD-BUT-CONSTRAINED'):
        cls, why = 'INCONCLUSIVE', why + ' -- but a file it reads or runs also defines it'
    return job, cls, why, info


def main():
    jobs = int(sys.argv[sys.argv.index('--jobs') + 1]) if '--jobs' in sys.argv else 4
    pairs = pairs_from_log()
    todo = [('control', t, c) for c, t, _ in CONTROLS] + [('control',) + REPORTED_CONTROL[::-1]] + pairs
    if '--only' in sys.argv:
        pre = sys.argv[sys.argv.index('--only') + 1].split(',')
        todo = [j for j in todo if any(j[2].startswith(p) for p in pre)]
    with ThreadPoolExecutor(jobs) as ex:
        res = list(ex.map(classify, todo))
    print(f'{len(pairs)} carrier-number pair(s) from the r7069 confirm log, plus {len(CONTROLS) + 1} control(s)\n')
    for (paper, tok, car), cls, why, info in res:
        print(f'{cls:19s} {paper:26s} {tok:8s} {car[:70]}')
        print(f'{"":19s}   {why}')
        print(f'{"":19s}   {info}')
    print('\nCALIBRATION (a condition of delivery):')
    ok = True
    for c, t, want in CONTROLS:
        got = [cls for (p, tk, car), cls, _, _ in res if p == 'control' and car == c and tk == t]
        good = bool(got) and got[0] in want
        ok &= good
        print(f'  [{"ok" if good else "FAIL"}]  {c} {t}: {got[0] if got else "not run"} (want {" or ".join(want)})')
    rc_ = [cls for (p, tk, car), cls, _, _ in res if p == 'control' and car == REPORTED_CONTROL[0]]
    print(f'  [reported]  {REPORTED_CONTROL[0][:60]} {REPORTED_CONTROL[1]}: {rc_[0] if rc_ else "not run"}')
    print('\nSHORTLIST over the twenty-five:')
    for cls in ('HELD', 'HELD-BUT-CONSTRAINED', 'INCONCLUSIVE', 'DERIVED-AND-PINNED', 'DERIVED'):
        sel = [(p, tk, car) for (p, tk, car), c, _, _ in res if c == cls and p != 'control']
        print(f'  {cls:19s} {len(sel)}')
        for p, tk, car in sel:
            print(f'      {p:26s} {tk:8s} {car[:80]}')
    print('\nCALIBRATION HOLDS -- the instrument is built.' if ok else '\nCALIBRATION FAILS -- the instrument is NOT built.')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
