#!/usr/bin/env python3
"""recogniser.py (r7285+70.1; drafted as corpus/check_live_exact_count.py and NOT placed -- see results.md) -- DOES A RECEIPT GATE A LIVE READ AGAINST AN EXACT INTEGER?

** r7285+70.1, on 66's r7283 ② / r7285 ORDER: THE 71st MEMBER AS A GATE. **  A clause that compares a count read
LIVE -- a shared ledger from the working tree, a `git` call against a moving end -- with an exact integer is green on
the day it is written and red the first time another seat edits that file, with the receipt's own claim unmoved.
`C71` `Ⓐ⑤` (r7273), `S25` `Ⓑ①` and two more faces in `S25` (r7283) are the instances; the rule was written three
times and inherited none, so it is refused here instead.

** THE RECOGNISER (pre-registered, computations/beyond_the_wall/r7285_70_live_exact_count/PREDICTION.md). **  A
taint pass over each receipt's syntax tree, run to a fixed point:
  * SOURCES (NARROW, the gate's width) -- a working-tree read of a SHARED LEDGER (`open`/`read_text`, directly or
    through a helper whose body opens its argument) on a path naming a `corpus/*.tsv`, `receipts/INDEX.md`,
    `THE_*.md`, `FOR_*.md` or a `*LEDGER*.md`; and any `git` call (direct or through a helper that runs git) that
    is not PINNED -- pinned means every revision named is a literal sha (or a module constant bound to one, f-strings
    included), none is `HEAD`/`origin`/`main`/`--cached`, and a `diff` names two.
    (`--wide` adds every working-tree read: any `open`, `read_text`, `listdir`, `glob`, `walk` -- reported only.)
  * PROPAGATION -- assignment, augmented assignment, `for` targets, comprehensions, any call or operation with a
    tainted operand, and a function whose return is tainted.
  * A REFUSED CLAUSE -- `==`/`!=` (chained pairs too) between a tainted side and an INTEGER (a literal, or a module
    name bound to one), not `0`, outside any f-string and any `print` -- so a LABEL that keeps the old number is
    never read, which is how every repair so far has written it.  A direction (`<=`, `>=`) or a pinned read is the
    remedy, and is not refused.

** THE RATCHET. **  Today's refused sites are named in `KNOWN`, each routed; a NEW site fails; a KNOWN site no longer
refused is STALE and fails, so the list can only shrink.

    python3 corpus/check_live_exact_count.py
    python3 corpus/check_live_exact_count.py --wide | --zero | --list
"""
import ast
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SHA = re.compile(r'^[0-9a-f]{7,40}$')
MOVING = re.compile(r'HEAD|^origin\b|^main$|--cached|@\{')
LEDGER_MD = re.compile(r'(?:^|/)(?:receipts/)?INDEX\.md$|(?:^|/)THE_[A-Z0-9_]+\.md$|(?:^|/)FOR_[A-Z0-9_]+\.md$|LEDGER[^/]*\.md$')
CORPUS_TSV = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tsv'))}
OPEN_FNS = {'open', 'read_text', 'read_bytes'}
WALK_FNS = {'listdir', 'glob', 'iglob', 'walk', 'scandir', 'rglob'}

#: (receipt path, line) -> routing note; refused on the tree at r7285+70.1 and routed to their owners
KNOWN = {}


def _fname(call):
    f = call.func
    return f.attr if isinstance(f, ast.Attribute) else f.id if isinstance(f, ast.Name) else ''


class Receipt:
    def __init__(self, src, wide=False, zero=False):
        self.tree = ast.parse(src)
        self.wide, self.zero = wide, zero
        self.consts = {}
        ok = lambda v: isinstance(v, ast.Constant) and isinstance(v.value, (str, int)) and not isinstance(v.value, bool)
        for n in self.tree.body:
            if isinstance(n, ast.Assign) and len(n.targets) == 1:
                t, v = n.targets[0], n.value
                if isinstance(t, ast.Name) and ok(v):
                    self.consts[t.id] = v.value
                elif isinstance(t, ast.Tuple) and isinstance(v, ast.Tuple) and len(t.elts) == len(v.elts):
                    for a, b in zip(t.elts, v.elts):
                        if isinstance(a, ast.Name) and ok(b):
                            self.consts[a.id] = b.value
        self.parent = {}
        for p in ast.walk(self.tree):
            for c in ast.iter_child_nodes(p):
                self.parent[c] = p
        self.funcs = {n.name: n for n in ast.walk(self.tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.openers, self.gitters, self.gitcall = set(), set(), {}
        for name, fn in self.funcs.items():
            params = {a.arg for a in fn.args.args + fn.args.kwonlyargs} | ({fn.args.vararg.arg} if fn.args.vararg else set())
            for c in ast.walk(fn):
                if isinstance(c, ast.Call):
                    if _fname(c) in OPEN_FNS and any(isinstance(x, ast.Name) and x.id in params
                                                     for a in c.args[:1] + [getattr(c.func, 'value', None)] if a is not None
                                                     for x in ast.walk(a)):
                        self.openers.add(name)
                    if self._is_git_call(c) and any(isinstance(x, ast.Name) and x.id in params for x in ast.walk(c.args[0])):
                        self.gitters.add(name)
                        self.gitcall[name] = (fn, c)
        self.tainted, self.taint_fns = set(), set()

    # ---- strings an expression can be resolved to
    def _strs(self, e):
        out = []
        for x in ast.walk(e):
            if isinstance(x, ast.Constant) and isinstance(x.value, str):
                out.append(x.value)
            elif isinstance(x, ast.Name) and isinstance(self.consts.get(x.id), str):
                out.append(self.consts[x.id])
        return out

    def _is_git_call(self, c):
        if _fname(c) not in ('run', 'check_output', 'Popen', 'call', 'check_call', 'getoutput'):
            return False
        a0 = c.args[0] if c.args else None
        if isinstance(a0, (ast.List, ast.Tuple)) and a0.elts:
            return any(isinstance(e, ast.Constant) and e.value == 'git' for e in a0.elts[:1])
        if isinstance(a0, ast.BinOp) and isinstance(a0.left, ast.List) and a0.left.elts:
            return isinstance(a0.left.elts[0], ast.Constant) and a0.left.elts[0].value == 'git'
        return False

    def _git_pinned(self, args):
        """args: the git argument expressions at the call site"""
        toks, unknown = [], False
        for a in args:
            if isinstance(a, ast.Starred):
                unknown = True
                continue
            if isinstance(a, ast.JoinedStr):
                s = ''
                for v in a.values:
                    if isinstance(v, ast.Constant):
                        s += str(v.value)
                    elif isinstance(v, ast.FormattedValue) and isinstance(v.value, ast.Name) \
                            and isinstance(self.consts.get(v.value.id), str):
                        s += self.consts[v.value.id]
                    elif isinstance(v, ast.FormattedValue) and isinstance(v.value, ast.Constant):
                        s += str(v.value.value)
                    else:
                        s += '\x00'
                toks.append(s)
            elif isinstance(a, ast.Constant) and isinstance(a.value, str):
                toks.append(a.value)
            elif isinstance(a, ast.Name) and isinstance(self.consts.get(a.id), str):
                toks.append(self.consts[a.id])
            elif isinstance(a, (ast.List, ast.Tuple)):
                return self._git_pinned(a.elts)
            else:
                toks.append('\x00')
        sub = next((t for t in toks if t and not t.startswith('-') and t != 'git'), '')
        revs = []
        for t in toks:
            if t == 'git' or t == sub:
                continue
            head = t.split(':', 1)[0].split('^')[0].split('~')[0]
            if '..' in head:
                revs += head.split('..')
            elif SHA.match(head) or MOVING.search(t) or '\x00' in head:
                revs.append(head)
        if unknown or any(MOVING.search(r) or '\x00' in r for r in revs):
            return False
        shas = [r for r in revs if SHA.match(r)]
        if not shas:
            return False
        return sub != 'diff' or len(shas) >= 2

    def _argv(self, c):
        a0 = c.args[0]
        if isinstance(a0, (ast.List, ast.Tuple)):
            return list(a0.elts)
        return list(a0.left.elts) + [ast.Starred(value=a0.right)]

    def _substituted(self, name, call):
        """the helper's git argv with its parameters replaced by this call site's arguments"""
        fn, inner = self.gitcall[name]
        params = [a.arg for a in fn.args.args]
        env = {p: a for p, a in zip(params, call.args) if not isinstance(a, ast.Starred)}
        va = fn.args.vararg.arg if fn.args.vararg else None
        rest = list(call.args[len(params):]) if va else []

        def sub(e):
            if isinstance(e, ast.Starred) and isinstance(e.value, ast.Name) and e.value.id == va:
                return rest
            if isinstance(e, ast.Starred) and isinstance(e.value, ast.Call) and _fname(e.value) == 'list' \
                    and e.value.args and isinstance(e.value.args[0], ast.Name) and e.value.args[0].id == va:
                return rest
            if isinstance(e, ast.Name) and e.id in env:
                return [env[e.id]]
            if isinstance(e, ast.JoinedStr):
                vals = []
                for v in e.values:
                    if isinstance(v, ast.FormattedValue) and isinstance(v.value, ast.Name) and v.value.id in env:
                        vals.append(ast.FormattedValue(value=env[v.value.id], conversion=-1, format_spec=None))
                    else:
                        vals.append(v)
                return [ast.JoinedStr(values=vals)]
            return [e]
        out = []
        for e in self._argv(inner):
            if isinstance(e, ast.Starred) and isinstance(e.value, ast.Call) and _fname(e.value) == 'list':
                e = ast.Starred(value=e.value.args[0]) if e.value.args else e
            out += sub(e)
        return out

    def _is_ledger_path(self, e):
        for s in self._strs(e):
            b = os.path.basename(s)
            if (s.endswith('.tsv') and b in CORPUS_TSV) or LEDGER_MD.search(s):
                return True
        return False

    def is_source(self, c):
        n = _fname(c)
        if n in OPEN_FNS:
            target = c.args[0] if c.args else getattr(c.func, 'value', None)
            if target is not None and (self.wide or self._is_ledger_path(target)):
                return True
        if n in self.openers and c.args and (self.wide or self._is_ledger_path(c.args[0])):
            return True
        if self.wide and n in WALK_FNS:
            return True
        if self._is_git_call(c):
            if any(call is c for _, call in self.gitcall.values()):
                return False                       # judged at each call site of its helper, with the arguments in
            return not self._git_pinned(self._argv(c)[1:])
        if n in self.gitters:
            return not self._git_pinned(self._substituted(n, c)[1:])
        return n in self.taint_fns

    def is_tainted(self, e):
        for x in ast.walk(e):
            if isinstance(x, ast.Name) and x.id in self.tainted:
                return True
            if isinstance(x, ast.Call) and self.is_source(x):
                return True
        return False

    def _targets(self, t):
        return [x.id for x in ast.walk(t) if isinstance(x, ast.Name)]

    def propagate(self):
        changed = True
        while changed:
            changed = False
            for n in ast.walk(self.tree):
                pairs = []
                if isinstance(n, ast.Assign):
                    for t in n.targets:
                        if isinstance(t, (ast.Tuple, ast.List)) and isinstance(n.value, (ast.Tuple, ast.List)) \
                                and len(t.elts) == len(n.value.elts):
                            pairs += list(zip(t.elts, n.value.elts))     # `a, b = live, pinned`: element-wise
                        else:
                            pairs.append((t, n.value))
                elif isinstance(n, (ast.AugAssign, ast.AnnAssign)) and n.value is not None:
                    pairs = [(n.target, n.value)]
                elif isinstance(n, ast.For):
                    # a comprehension's own targets are NOT propagated: they are local to it, and a name reused
                    # by a later pinned comprehension must not inherit the taint (C71 @ 664c5ab2^ reuses `f`, `l`).
                    # A comprehension is tainted through its iterable, which `is_tainted` reads directly.
                    pairs = [(n.target, n.iter)]
                elif isinstance(n, ast.withitem) and n.optional_vars is not None:
                    pairs = [(n.optional_vars, n.context_expr)]
                elif isinstance(n, ast.NamedExpr):
                    pairs = [(n.target, n.value)]
                for t, v in pairs:
                    if self.is_tainted(v):
                        for name in self._targets(t):
                            if name not in self.tainted:
                                self.tainted.add(name)
                                changed = True
                if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) and n.name not in self.taint_fns:
                    if any(isinstance(r, ast.Return) and r.value is not None and self.is_tainted(r.value)
                           for r in ast.walk(n)):
                        self.taint_fns.add(n.name)
                        changed = True

    def _int(self, e):
        if isinstance(e, ast.Constant) and isinstance(e.value, int) and not isinstance(e.value, bool):
            return e.value
        if isinstance(e, ast.UnaryOp) and isinstance(e.op, ast.USub):
            v = self._int(e.operand)
            return -v if v is not None else None
        if isinstance(e, ast.Name) and isinstance(self.consts.get(e.id), int):
            return self.consts[e.id]
        return None

    def _in_label(self, n):
        p = self.parent.get(n)
        while p is not None:
            if isinstance(p, ast.JoinedStr) or (isinstance(p, ast.Call) and _fname(p) == 'print'):
                return True
            p = self.parent.get(p)
        return False

    def refused(self):
        self.propagate()
        out = []
        for n in ast.walk(self.tree):
            if not isinstance(n, ast.Compare) or self._in_label(n):
                continue
            xs = [n.left] + n.comparators
            for i, op in enumerate(n.ops):
                if not isinstance(op, (ast.Eq, ast.NotEq)):
                    continue
                a, b = xs[i], xs[i + 1]
                for k, other in ((self._int(a), b), (self._int(b), a)):
                    if k is not None and (k != 0 or self.zero) and self._int(other) is None and self.is_tainted(other):
                        out.append((n.lineno, k, ast.unparse(n)[:120]))
                        break
                else:
                    continue
                break
        return out


def scan(src, **kw):
    try:
        return Receipt(src, **kw).refused()
    except SyntaxError:
        return []


def receipts():
    out = subprocess.run(['git', '-C', ROOT, 'ls-files', 'receipts'], capture_output=True, text=True).stdout.split()
    return sorted(p for p in out if p.endswith('.py'))


def _git_show(rev, path):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{rev}:{path}'], capture_output=True, text=True,
                          errors='replace').stdout


def _seeds():
    bad = []
    built = [
        ('a label keeping 700 with a <= gate', "L = open('corpus/quote_pin_baseline.tsv').read().split()\n"
         "gate(f'{len(L)} remain (700 when written)', len(L) <= 700)\n", False),
        ('a live ledger count gated == 700', "L = open('corpus/quote_pin_baseline.tsv').read().split()\n"
         "gate('x', len(L) == 700)\n", True),
        ('a ledger read at a literal sha, == 700', "A = 'a2dfa7ab'\nimport subprocess\n"
         "t = subprocess.run(['git', 'show', f'{A}:corpus/quote_pin_baseline.tsv'], capture_output=True).stdout\n"
         "assert len(t.split()) == 700\n", False),
        ('a diff against ONE sha (the working tree) counted == 3', "B = 'a2dfa7ab'\nimport subprocess\n"
         "def _git(*a):\n    return subprocess.run(['git'] + list(a), capture_output=True, text=True).stdout\n"
         "touched = _git('diff', '--name-only', B).split()\nassert len(touched) == 3\n", True),
        ('a diff between TWO shas counted == 3', "B = 'a2dfa7ab'\nC = '438cd783'\nimport subprocess\n"
         "def _git(*a):\n    return subprocess.run(['git'] + list(a), capture_output=True, text=True).stdout\n"
         "touched = _git('diff', '--name-only', B, C).split()\nassert len(touched) == 3\n", False),
        ('a constant table', "T = [1, 2, 3]\nassert len(T) == 3\n", False),
        ('a live ledger read gated == 0 (none)', "L = open('corpus/quote_pin_baseline.tsv').read().split()\n"
         "assert len([x for x in L if x == 'BAD']) == 0\n", False),
    ]
    for label, src, want in built:
        if bool(scan(src)) != want:
            bad.append(f'{label}: expected {"refused" if want else "passed"}')
    s25 = 'receipts/L_probability/S25_the_backlog_is_a_verdicting_job_after_all_but_two_thirds_of_it_is_pins_on_' \
          'what_a_paper_means_and_the_one_open_flagged_sentence_is_the_same_sentence_twice.py'
    c71 = 'receipts/P15_CR_cosmology/C71_the_census_is_sixty_two_per_cent_ast_and_the_backlog_has_a_nearest_' \
          'function_for_eighty_three_per_cent_but_the_fourteen_that_do_not_are_one_hole_and_a_cheaper_form_' \
          'lowers_the_strict_count.py'
    for label, rev, path, want, needle in (('S25 before its repair', '438cd783', s25, True, '700'),
                                           ('C71 before its repair', '664c5ab2^', c71, True, 'DRIFT')):
        src = _git_show(rev, path)
        if not src:
            bad.append(f'{label}: {rev} not in this history')
            continue
        r = scan(src)
        if want and not any(needle in t or str(k) == needle for _, k, t in r):
            bad.append(f'{label} @ {rev}: expected its live exact clause refused, got {r[:3]}')
    return bad


def main():
    wide, zero = '--wide' in sys.argv, '--zero' in sys.argv
    print()
    print('  LIVE EXACT COUNT -- does a receipt gate a live read against an exact integer?')
    print()
    bad = _seeds()
    if bad:
        print('  ⛔ the seeds lost a direction:')
        for b in bad:
            print(f'      {b}')
        return 1
    print('    seeds hold: S25 and C71 refused before their repairs; a label, a pinned read, a two-sha diff, a '
          'constant table and a "none" gate pass')
    found = {}
    for p in receipts():
        src = open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
        for line, k, text in scan(src, wide=wide, zero=zero):
            found[(p, line)] = (k, text)
    mode = ' (WIDE: every working-tree read)' * wide + ' (with 0)' * zero
    print(f'    {len(receipts())} receipt(s) read; {len(found)} refused clause(s) in '
          f'{len({p for p, _ in found})} receipt(s){mode}')
    if '--list' in sys.argv or wide or zero:
        for (p, line), (k, text) in sorted(found.items()):
            print(f'    [{"KNOWN" if (p, line) in KNOWN else "LIVE=="}] {p}:{line}  == {k}  {text[:90]}')
        return 0
    new = sorted(k for k in found if k not in KNOWN)
    stale = sorted(k for k in KNOWN if k not in found)
    rc = 0
    if new:
        rc = 1
        print()
        for p, line in new:
            print(f'    [LIVE==] {p}:{line}  {found[(p, line)][1][:100]}')
        print()
        print('  ⛔ A RECEIPT GATES A LIVE READ AGAINST AN EXACT INTEGER: GREEN TODAY, RED AT THE NEXT SEAT\'S EDIT.')
        print('     Assert a DIRECTION (`<=`, `>=`) on the live value, or read the value at a literal sha.  A label may')
        print('     keep the number; only the gated comparison is refused.')
    if stale:
        rc = 1
        print()
        for p, line in stale:
            print(f'    [STALE KNOWN] {p}:{line} -- no longer refused; remove it from KNOWN')
    if rc == 0:
        print('  no receipt gates a live read against an exact integer, beyond the named sites.')
    return rc


if __name__ == '__main__':
    sys.exit(main())
