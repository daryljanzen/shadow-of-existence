#!/usr/bin/env python3
"""r7430 -- WHICH OF THIS SEAT'S GATES HAVE A POPULATION THAT CAN BE EMPTY, AND WHICH ASSERT IT CANNOT.

`r7421` ③, promoted as a standing rule: ** a gate whose population can be empty must prove IN ITS OWN RUN
that it could have fired ** -- `70`'s test, *"after it, a zero is a measured zero"*.  `r7426` built the
first gate to it, `r7428` extended it to a second condition, and both raised this question without
answering it.

** THE POPULATION IS DERIVED AND NOT READ. **  `receipts/INDEX.md` names exactly ONE gate in a
`corpus/check_*` receipt column, so reading the index would have measured a population of one.  This takes
the commit that ADDED each gate under `corpus/` and keeps the ones whose subject carries an EVEN revision
id -- this line's band since `r3563`.  ⚠ Its stated limit: it measures who WROTE a gate, not who owes it.

⛔⛭⛭⛭ ** AND THIS CENSUS IS ITSELF A DETECTOR, WHICH IS WHAT THIS SEAT HAS GOT WRONG FOURTEEN TIMES. **
*The `9`th instance was a vocabulary detector that could not tell a false claim from the true claim sharing
its words.  A census that decided "does this gate assert non-vacuity" by grepping for `empty`, `no rows` or
`0 of` would be the fifteenth.*
  ⇒ *** So it reads the AST, and it answers `r7417` ④'s three ways rather than two: ***
      `ASSERTS`      -- a failure path is reachable FROM a test of the population's own emptiness
      `DOES NOT`     -- it loops a derived population and no such path exists
      `UNDECIDABLE`  -- it cannot be read this way, and that is ITS OWN ANSWER and not either side
  ⌈ *An `UNDECIDABLE` folded into `DOES NOT` would overstate the debt; folded into `ASSERTS` it would hide
    it.  `r7417` ④ ruled on exactly this asymmetry for a different population.*
  ⌊ ** And the classifier is run against CONSTRUCTED gates before any real figure is read ** -- `r7420`,
    `r7424`, `r7426` and `r7428` each caught a control of this seat's that was in the right shape and the
    wrong place.  *The habit is proving the instrument and not the run.*

    python3 computations/beyond_the_wall/r7430_60_*/census.py            # the census
    python3 computations/beyond_the_wall/r7430_60_*/census.py --seed     # the classifier's own cases
"""
import ast
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
GATES = os.path.join(ROOT, 'corpus')

ASSERTS, DOES_NOT, UNDECIDABLE = 'ASSERTS', 'DOES NOT', 'UNDECIDABLE'


# ── the population, derived from authorship ────────────────────────────────────────────────────────
def this_lines_gates():
    """[(name, adding-commit subject), ...] -- gates whose ADDING commit carries an EVEN revision id."""
    out = []
    for f in sorted(os.listdir(GATES)):
        if not (f.startswith('check_') and f.endswith('.py')):
            continue
        r = subprocess.run(['git', '-C', ROOT, 'log', '--diff-filter=A', '--format=%s',
                            '--', os.path.join('corpus', f)], capture_output=True, text=True)
        subj = [l for l in r.stdout.strip().split('\n') if l.strip()]
        subj = subj[-1] if subj else ''
        m = re.match(r'^r(\d+)', subj)
        if m and int(m.group(1)) % 2 == 0:
            out.append((f, subj))
    return out


# ── the classifier ────────────────────────────────────────────────────────────────────────────────
#   ⛭ It asks ONE structural question and nothing about wording: ** is there a statement that can fail,
#   reached from a test of a container's emptiness? **  Three shapes count as such a test, and they are
#   the three Python offers:
#       `if not X:`            / `if X:` with the fail in the `else`
#       `if len(X) == 0:`      / `== 0`, `< 1`, `!= 0` against a `len()`
#       `if not X` inside a boolean operator
#   and a statement "can fail" when it calls a failing function, raises, or exits non-zero.
_FAILING_CALLS = ('fail', 'die', 'bad', 'err', 'problem', 'red')


class _Reader(ast.NodeVisitor):
    """collects, per module: the loops over subscriptable/derived populations, and the emptiness tests
    from which a failing statement is reachable."""

    def __init__(self):
        self.loops = []           # (lineno, iterated-expression source segment)
        self.empty_guards = []    # (lineno, the guard's source segment)
        self.fail_names = set()   # functions in this module that raise or exit non-zero
        self.exits = set()        # the function name(s) this module exits WITH
        self.presence_guards = []  # guards that test a FILE's presence, not a population's size
        self.candidates = []       # (lineno, src, names) -- shaped guards, pending population linkage
        self.in_loop = 0           # lexical loop depth: a guard INSIDE the iteration is per-item
        self.fn = None            # the function currently being visited
        self.src = ''

    # a function is "failing" when its body raises, calls sys.exit with a non-zero/unknown arg, or
    # appends to a module-level failures list.  Derived from the body, never from the name.
    def collect_failing(self, tree):
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            for sub in ast.walk(node):
                if isinstance(sub, ast.Raise):
                    self.fail_names.add(node.name); break
                if isinstance(sub, ast.Call) and _dotted(sub.func) in ('sys.exit', 'exit'):
                    self.fail_names.add(node.name); break
                if (isinstance(sub, ast.Call) and _dotted(sub.func).endswith('.append')
                        and re.search(r'(?i)fail|bad|red|err|problem', _dotted(sub.func))):
                    self.fail_names.add(node.name); break

    def visit_FunctionDef(self, node):
        prev, self.fn = self.fn, node.name
        self.generic_visit(node)
        self.fn = prev

    def visit_For(self, node):
        self.loops.append((node.lineno, _seg(self.src, node.iter)))
        self.in_loop += 1
        self.generic_visit(node)
        self.in_loop -= 1

    # ⛔⛭⛭⛭ AND A COMPREHENSION IS A LOOP, which was this revision's FOURTH classifier defect and
    #   the one the anchor caught.  *`check_register_columns` carries a textbook
    #   `if not rows: ... return 1`, and the census read it UNDECIDABLE because `rows` is iterated by
    #   `[... for (i, l), n in zip(rows, counts) ...]` -- a comprehension generator, which is not an
    #   `ast.For` and so never entered the looped-population set.*  ⇒ **In these gates the
    #   comprehension IS the idiom**, so reading only `for` statements measured the wrong half of the
    #   corpus's own grammar.  ⌗ *Fourth time in one revision; each one was found by a case whose
    #   answer was known in advance, and none of them by reading the code and feeling satisfied.*
    def _comp(self, node):
        for gen in node.generators:
            self.loops.append((node.lineno, _seg(self.src, gen.iter)))
        self.in_loop += 1
        self.generic_visit(node)
        self.in_loop -= 1

    visit_ListComp = _comp
    visit_SetComp = _comp
    visit_DictComp = _comp
    visit_GeneratorExp = _comp

    def visit_If(self, node):
        g = node.test
        # ⛭ `return <nonzero>` counts only inside the function the module exits with -- see
        #   `exit_targets`, and the measurement that made this necessary.
        def fails(b):
            if _can_fail(b, self.fail_names):
                return True
            return self.fn in self.exits and _returns_nonzero(b)
        for test, body, tag in ((g, node.body, ''),
                                (g, node.orelse, 'else of ') if node.orelse else (None, [], '')):
            if test is None or not body:
                continue
            shaped = _is_empty_test(test) if not tag else _is_truthy_container(test)
            if not (shaped and fails(body)):
                continue
            if self.in_loop:
                # ⛔⛭⛭⛭ A GUARD INSIDE THE ITERATION IS PER-ITEM BY CONSTRUCTION, and this is the
                #   structural discriminator the first four repairs were groping at.  *`check_kind`'s
                #   `if not hits:` and `check_map_overturns`'s `if not SELFMARK.search(...)` both sit
                #   INSIDE a loop and both passed the name-based linkage by coincidence -- `hits` and
                #   `t` happen to be iterated elsewhere.*
                #   ⇒ *** A POPULATION'S NON-VACUITY IS ASSERTED BEFORE THE ITERATION, NEVER WITHIN
                #     IT: a test that runs once per item cannot say anything about whether there were
                #     any items. ***  ⌗ Recorded as a candidate so the gate reads `UNDECIDABLE` rather
                #   than `DOES NOT` -- the reader saw a shaped guard and declined it, which is not the
                #   same as finding none.
                self.candidates.append((node.lineno, tag + _seg(self.src, test) + ' [inside the loop]',
                                        set()))
                continue
            if _tests_a_presence(test):
                # a file-presence guard: shaped like an emptiness test, about a different thing.
                self.presence_guards.append((node.lineno, tag + _seg(self.src, test)))
                continue
            self.candidates.append((node.lineno, tag + _seg(self.src, test), _names_in(test)))
        self.generic_visit(node)


def _dotted(n):
    if isinstance(n, ast.Name):
        return n.id
    if isinstance(n, ast.Attribute):
        return _dotted(n.value) + '.' + n.attr
    return ''


def _seg(src, node):
    try:
        return ast.get_source_segment(src, node) or ''
    except Exception:                                            # noqa: BLE001
        return ''


def _is_truthy_container(t):
    """`if X:` where X is a name or a call -- a container's own truthiness."""
    return isinstance(t, (ast.Name, ast.Call, ast.Attribute, ast.Subscript))


_PRESENCE = ('os.path.exists', 'os.path.isfile', 'os.path.isdir', 'os.path.islink')


def _names_in(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _tests_a_presence(t):
    """⛔⛭⛭⛭ A MISSING-FILE GUARD IS NOT A POPULATION GUARD, and conflating them was this revision's
    THIRD classifier defect and the one that mattered most.

    *`5` of the `13` gates the census first called `ASSERTS` were decided on
    `if not os.path.exists(REG): ... return 1` -- which asserts that a FILE is there and says nothing
    about whether the rows read out of it are any.  **A file can exist and yield zero rows, which is
    exactly the state `r7421` ③ is about.*** ⇒ *So the ASSERTS bucket was ~69 per cent false positives,
    in the direction that OVERSTATES compliance -- and `r7430`'s own registered arm ⒜ had predicted
    precisely this: an empty `UNDECIDABLE` column is evidence the detector is guessing.*"""
    for n in ast.walk(t):
        if isinstance(n, ast.Call) and _dotted(n.func) in _PRESENCE:
            return True
    return False


def _is_empty_test(t):
    """`not X`, `len(X) == 0`, `len(X) < 1`, `X == 0`, or either inside a boolean operator."""
    if isinstance(t, ast.UnaryOp) and isinstance(t.op, ast.Not):
        return _is_truthy_container(t.operand)
    if isinstance(t, ast.Compare) and len(t.ops) == 1:
        left, op, right = t.left, t.ops[0], t.comparators[0]
        zeroish = [n for n in (left, right)
                   if isinstance(n, ast.Constant) and n.value in (0, 1)]
        other = [n for n in (left, right) if n not in zeroish]
        if zeroish and other and isinstance(op, (ast.Eq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.NotEq)):
            o = other[0]
            if isinstance(o, ast.Call) and _dotted(o.func) == 'len':
                return True
            if isinstance(o, (ast.Name, ast.Attribute, ast.Subscript)):
                return True
    if isinstance(t, ast.BoolOp):
        return any(_is_empty_test(v) for v in t.values)
    return False


def exit_targets(tree):
    """the function names this module exits WITH -- `sys.exit(main())` gives {'main'}.

    ⛔⛭⛭⛭ `r7430` MEASURED THIS AFTER ITS OWN FIRST READING WAS WRONG.  The first classifier counted
    only `raise`, `sys.exit` and an append to a failures list as "can fail", and MISSED `return 1` --
    which is present in **122 of the 135** gates under `corpus/`, the dominant failure idiom in the very
    corpus this census was pointed at.  *So it read `check_register_columns`, whose `if not rows: ...
    return 1` is a textbook non-vacuity assertion, as asserting nothing.*
      ⌈ ⇒ *** THE FIFTEENTH INSTANCE OF THIS SEAT'S DETECTOR FAMILY, and the same shape as the
        eleventh: I ENUMERATED THE IDIOMS I COULD THINK OF INSTEAD OF DERIVING THEM FROM THE CORPUS. ***
      ⌊ *And `r7430`'s own `PREDICTION.md` is what caught it: it registered `UNDECIDABLE` at `3`--`20`
        and said an empty third column would be evidence the detector was GUESSING rather than evidence
        the gates were uniform.  The measurement came back `0`, so the arm was read as a MISS and the
        classifier was read by hand -- which is where this was found.*
    ⌗ `return <nonzero>` counts ONLY inside the function the module actually exits with, read from the
    module's own `sys.exit(...)` call rather than assumed to be named `main`: a helper returning a
    non-zero COUNT is not a failure, and counting it would overstate every gate's compliance, which is
    the dangerous direction."""
    out = set()

    def _args_of(call):
        for a in call.args:
            if isinstance(a, ast.Call):
                n = _dotted(a.func).split('.')[-1]
                if n:
                    out.add(n)

    for node in ast.walk(tree):
        # ⛔⛭ AND THIS LIST IS DERIVED TOO, AFTER THE SAME MISTAKE A SECOND TIME IN ONE REVISION.
        #   The first version of this function read only `sys.exit(...)`/`exit(...)`, so it returned
        #   an EMPTY set for `check_register_columns`, whose last line is `raise SystemExit(main())`
        #   -- and the gate went on reading `DOES NOT` with its `if not rows: ... return 1` in plain
        #   sight.  Measured across the 135 gates: `sys.exit(...)` 89 occurrences and
        #   `raise SystemExit(...)` **66**, so the idiom I had left out covers forty-odd per cent of
        #   the corpus.  ⇒ *Twice in one revision I enumerated what I could think of instead of
        #   measuring what is there; the second time is recorded because the first did not stop it.*
        if isinstance(node, ast.Call) and _dotted(node.func) in ('sys.exit', 'exit'):
            _args_of(node)
        if (isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call)
                and _dotted(node.exc.func).split('.')[-1] == 'SystemExit'):
            _args_of(node.exc)
    return out


def _returns_nonzero(body):
    for node in body:
        for sub in ast.walk(node):
            if (isinstance(sub, ast.Return) and isinstance(sub.value, ast.Constant)
                    and sub.value.value not in (0, None, False)):
                return True
    return False


def _can_fail(body, fail_names):
    """does this block contain a statement that raises, exits, or calls a failing function?"""
    for node in body:
        for sub in ast.walk(node):
            if isinstance(sub, ast.Raise):
                return True
            if isinstance(sub, ast.Call):
                d = _dotted(sub.func)
                if d in ('sys.exit', 'exit'):
                    return True
                if d.split('.')[-1] in fail_names:
                    return True
                tail = d.split('.')[-1].lower()
                if any(tail == w or tail.startswith(w + '_') for w in _FAILING_CALLS):
                    return True
                if d.endswith('.append') and re.search(r'(?i)fail|bad|red|err|problem', d):
                    return True
    return False


def classify_source(src, name='<src>'):
    """(verdict, detail) for one gate's SOURCE -- the ONE path the real gates and the seeds both take."""
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return UNDECIDABLE, f'does not parse ({e.msg}), so nothing can be read from it'
    r = _Reader()
    r.src = src
    r.exits = exit_targets(tree)
    r.collect_failing(tree)
    r.visit(tree)
    looped = set()
    for _ln, seg in r.loops:
        try:
            looped |= _names_in(ast.parse(seg, mode='eval'))
        except SyntaxError:
            looped |= set(re.findall(r'[A-Za-z_]\w*', seg or ''))
    for ln, seg, names in r.candidates:
        # ⛭ THE LINKAGE: the guard must test an object the gate ACTUALLY LOOPS.  Without it, a
        #   per-item regex test (`not MARKED.search(window)`) inside a loop reads as a population
        #   assertion -- 4 of the first 13 `ASSERTS` were exactly that.
        if names & looped:
            r.empty_guards.append((ln, seg))
    if not r.loops:
        # ⛔ NOT `DOES NOT`.  A gate with no `for` loop may assert over a comprehension, a recursive
        #   walk, or a single object -- and this reader does not read those.  Saying "no control" here
        #   would be asserting something about a shape it did not look at.
        return UNDECIDABLE, 'no `for` loop over a population, so this reader has no population to judge'
    if r.empty_guards:
        ln, g = r.empty_guards[0]
        return ASSERTS, f'line {ln}: a failing path is reachable from `{g[:60]}`'
    if r.candidates or r.presence_guards:
        # ⛔ SHAPED LIKE AN ASSERTION BUT NOT LINKED TO THE POPULATION, OR ABOUT A FILE INSTEAD.
        #   This reader cannot tell "asserts in a shape I do not model" from "does not assert", so it
        #   says so.  Folding these into `DOES NOT` would invent a debt; into `ASSERTS`, hide one.
        why = []
        if r.presence_guards:
            why.append(f'{len(r.presence_guards)} file-presence guard(s) e.g. '
                       f'`{r.presence_guards[0][1][:44]}`')
        if r.candidates:
            why.append(f'{len(r.candidates)} guard(s) not linked to a looped population e.g. '
                       f'`{r.candidates[0][1][:44]}`')
        return UNDECIDABLE, '; '.join(why)
    pops = sorted({g for _ln, g in r.loops if g})[:3]
    return DOES_NOT, f'{len(r.loops)} loop(s) over e.g. {", ".join(repr(p[:40]) for p in pops)}'


def classify(path):
    return classify_source(open(path, encoding='utf-8', errors='replace').read(), os.path.basename(path))


# ── ⛭⛭⛭ THE CLASSIFIER'S OWN CASES, RUN BEFORE ANY REAL FIGURE IS READ ────────────────────────────
#   Each is a CONSTRUCTED gate and a statement about the classifier, never about the corpus.
_SEEDS = [
    # ⒜ the negative control: loops a population, reports success on zero.
    ('a gate that loops a population and never tests it for emptiness', DOES_NOT, '''
import sys
def main():
    rows = read_rows()
    bad = 0
    for r in rows:
        if r["x"] != r["y"]:
            print("FAIL"); bad += 1
    return 1 if bad else 0
sys.exit(main())
'''),
    # ⒝ the positive control shape: `if not pop: fail(...)`
    ('...and one that FAILS when the population is empty', ASSERTS, '''
FAILED = []
def fail(m):
    FAILED.append(m)
def main():
    rows = read_rows()
    if not rows:
        fail("no rows at all, so a clean verdict would be a silence")
    for r in rows:
        if r["x"] != r["y"]:
            fail("mismatch")
'''),
    # ⒞ the len()==0 shape, which is the same assertion written the other way
    ('...the same assertion written as a length comparison', ASSERTS, '''
import sys
def main():
    rows = read_rows()
    if len(rows) == 0:
        raise SystemExit("population is empty")
    for r in rows:
        pass
'''),
    # ⒟ the `else` shape: `if pop: ... else: fail`
    ('...and written as the `else` of a truthiness test', ASSERTS, '''
FAILS = []
def fail(m): FAILS.append(m)
def main():
    found = collect()
    if found:
        for f in found:
            pass
    else:
        fail("nothing was found, which is not the same as nothing being wrong")
'''),
    # ⒠ ⛔ THE CASE THAT MUST NOT READ AS `ASSERTS`: an emptiness test that only PRINTS.
    #    This is r7425 ④ as a classifier case -- a branch with no reachable consequence is not an
    #    assertion, and a detector that counted it would overstate every gate's compliance.
    ('a gate whose emptiness test only PRINTS is NOT asserting', DOES_NOT, '''
def main():
    rows = read_rows()
    if not rows:
        print("  note: no rows")
    for r in rows:
        pass
'''),
    # ⒡ ⛔⛭⛭⛭ THE CASE THE FIRST CLASSIFIER GOT WRONG, and it is this corpus's DOMINANT idiom --
    #    `return 1` from the function the module exits with, present in 122 of the 135 gates.
    #    *The first reader counted only `raise`, `sys.exit` and a failures-list append, and so read a
    #    textbook non-vacuity assertion as asserting nothing.  Seeded here so it cannot regress.*
    ('⛔ `if not rows: ... return 1` from the module\'s exit function IS asserting', ASSERTS, '''
import sys
def main():
    rows = read_rows()
    if not rows:
        print("  [FAIL] no rows found -- the reader is broken, not the file")
        return 1
    for r in rows:
        pass
    return 0
sys.exit(main())
'''),
    # ⒡ᵇ ...and the same `return 1` in a HELPER the module does not exit with must NOT count:
    #    a helper returning a non-zero COUNT is not a failure, and counting it would overstate
    #    compliance, which is the dangerous direction.
    ('...but `return 1` from a helper the module does not exit with does NOT count', DOES_NOT, '''
import sys
def how_many(rows):
    if not rows:
        return 1
    return len(rows)
def main():
    rows = read_rows()
    n = how_many(rows)
    for r in rows:
        pass
    return 0
sys.exit(main())
'''),
    # ⒡ᶜ ⛔ AND THE SECOND EXIT IDIOM, which the first `exit_targets` also left out: measured at 66
    #    occurrences against `sys.exit`'s 89, so it is not a corner.
    ('...and `raise SystemExit(main())` is an exit idiom too, measured at 66 uses', ASSERTS, '''
def main():
    rows = read_rows()
    if not rows:
        print("  [FAIL] no rows")
        return 1
    for r in rows:
        pass
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
'''),
    # ⒡ᵈ ⛔⛭⛭⛭ A FILE-PRESENCE GUARD IS NOT A POPULATION GUARD -- the defect that mattered most.
    #    5 of the first 13 `ASSERTS` were decided on exactly this shape.  A file can exist and yield
    #    zero rows, which is the state the rule is about.
    ('⛔ `if not os.path.exists(F): return 1` is NOT a population assertion', UNDECIDABLE, """
import os, sys
REG = "x.md"
def main():
    if not os.path.exists(REG):
        print("  [FAIL] missing")
        return 1
    rows = read_rows()
    for r in rows:
        pass
    return 0
sys.exit(main())
"""),
    # ⒡ᵉ ⛔ AND A PER-ITEM TEST INSIDE A LOOP IS NOT A POPULATION GUARD EITHER: 4 more of the 13.
    ('⛔ a per-item regex test inside the loop is NOT a population assertion', UNDECIDABLE, """
import re, sys
MARKED = re.compile("x")
def main():
    bad = 0
    for window in windows():
        if not MARKED.search(window):
            print("  [FAIL] unmarked")
            bad += 1
            return 1
    return 0
sys.exit(main())
"""),
    # ⒡ᶠ ⛔⛭⛭⛭ AND THE STRUCTURAL ONE: a guard INSIDE the iteration is per-item, whatever it tests
    #    and whatever names it shares with the population.  2 of the 4 surviving `ASSERTS` were this.
    ('⛔ `if not hits:` INSIDE the loop is per-item, not a population assertion', UNDECIDABLE, '''
import sys
def main():
    bad = []
    for r in read_rows():
        hits = [d for d in corpus() if r in d]
        if not hits:
            bad.append(r)
            return 1
    return 0
sys.exit(main())
'''),
    # ⒡ᵍ ...and the SAME guard hoisted OUT of the loop IS the assertion.
    ('...and the same guard hoisted OUT of the iteration IS the assertion', ASSERTS, '''
import sys
def main():
    rows = read_rows()
    if not rows:
        print("  [FAIL] no rows at all")
        return 1
    for r in rows:
        pass
    return 0
sys.exit(main())
'''),
    # ⒢ ⛔ AND THE CASE THAT MUST READ `UNDECIDABLE`: no `for` loop at all.
    #    Saying `DOES NOT` here would assert something about a shape the reader never looked at.
    # ⛭ THIS CASE MOVED, AND THE SEED IS WHAT MOVED IT.  It was registered expecting `UNDECIDABLE`
    #   on the premise "no `for` statement, so no population" -- and once the reader was taught that a
    #   COMPREHENSION is a loop, the premise was false: this gate DOES iterate `rows`, and asserts
    #   nothing about it.  ⇒ *The expectation is corrected to `DOES NOT` and the move is recorded
    #   rather than quietly rewritten, because the seed failing is how the reader's fourth defect was
    #   confirmed fixed rather than merely patched.*
    ('a gate whose only population is a COMPREHENSION still has a population', DOES_NOT, '''
import sys
def main():
    rows = read_rows()
    bad = [r for r in rows if r["x"] != r["y"]]
    if bad:
        sys.exit(1)
'''),
    # ⒢ᵇ and a gate with NO population at all -- no loop and no comprehension -- is undecidable:
    #    the rule is conditional on there being a population that can be empty.
    ('a gate with NO population at all reads UNDECIDABLE', UNDECIDABLE, '''
import sys
def main():
    a = open("x").read()
    b = open("y").read()
    if a != b:
        print("  [FAIL] they differ")
        return 1
    return 0
sys.exit(main())
'''),
    # ⒣ and a file that does not parse is undecidable rather than compliant or not
    ('a gate that does not parse reads UNDECIDABLE', UNDECIDABLE, '''
def main(:
    pass
'''),
]


def seed():
    bad = 0
    for label, want, src in _SEEDS:
        got, detail = classify_source(src)
        ok = got == want
        print(f'    [{"ok" if ok else "FAIL"}]  {label}')
        print(f'              want {want!r}, got {got!r} -- {detail[:90]}')
        bad += 0 if ok else 1
    # the one REAL anchor: the gate built to this rule at r7426/r7428 must read ASSERTS.
    p = os.path.join(GATES, 'check_formalisation_join.py')
    got, detail = classify(p)
    ok = got == ASSERTS
    print(f'    [{"ok" if ok else "FAIL"}]  the one gate KNOWN to satisfy the rule reads {ASSERTS}')
    print(f'              got {got!r} -- {detail[:90]}')
    bad += 0 if ok else 1
    print(f'\n  {len(_SEEDS) + 1} case(s), {bad} failing')
    return 1 if bad else 0


def main():
    print('=' * 100)
    print('  r7430 -- WHICH OF THIS SEAT\'S GATES HAVE A POPULATION THAT CAN BE EMPTY')
    print('=' * 100)

    # ⛭ the classifier's own cases FIRST.  A census whose classifier is unproven is not a census.
    print('\n  ⓪ THE CLASSIFIER\'S OWN CASES, run before any real figure is read')
    if seed():
        print('\n  ⛔ the classifier failed its own cases, so no census is reported from it')
        return 1

    pop = this_lines_gates()
    allg = [f for f in sorted(os.listdir(GATES)) if f.startswith('check_') and f.endswith('.py')]
    print(f'\n  ⓵ THE POPULATION, DERIVED FROM AUTHORSHIP AND NOT READ FROM A LIST')
    print(f'      gates under corpus/                        : {len(allg)}')
    print(f'      of those, ADDED by an EVEN revision id     : {len(pop)}   <- this line\'s band')
    print(f'      ⌗ `receipts/INDEX.md` names {sum(1 for l in open(os.path.join(ROOT, "receipts", "INDEX.md"), encoding="utf-8") if "corpus/check_" in l)} gate row(s), which is why the')
    print(f'        population is derived: reading the index would have measured a population of one.')

    buckets = {ASSERTS: [], DOES_NOT: [], UNDECIDABLE: []}
    for name, _subj in pop:
        v, detail = classify(os.path.join(GATES, name))
        buckets[v].append((name, detail))

    print(f'\n  ⓶ THE CENSUS, THREE WAYS (`r7417` ④: a verdict the instrument cannot reach is its own answer)')
    for v in (ASSERTS, DOES_NOT, UNDECIDABLE):
        print(f'      {v:12s}: {len(buckets[v]):3d} of {len(pop)}')

    print(f'\n  ⓷ THE GATES THAT OWE A CONTROL, NAMED WITH THE POPULATION THEY LOOP')
    print(f'      (`r7425` ④ applied to a measurement: it must name an address the remedy can be written to)')
    for name, detail in buckets[DOES_NOT]:
        print(f'      ⛔ corpus/{name}')
        print(f'           loops: {detail[:110]}')

    print(f'\n  ⓸ THE GATES THAT ASSERT IT, AND WHERE')
    for name, detail in buckets[ASSERTS]:
        print(f'      ✔ corpus/{name}  --  {detail[:95]}')

    print(f'\n  ⓹ AND THE ONES THIS READER REFUSES, WHICH IS AN ANSWER AND NOT A GAP')
    print(f'      ⌗ Each needs reading by hand; counting them as compliant would hide a debt and counting')
    print(f'        them as non-compliant would invent one.')
    for name, detail in buckets[UNDECIDABLE]:
        print(f'      ? corpus/{name}  --  {detail[:95]}')

    print('\n' + '=' * 100)
    print(f'  {len(buckets[ASSERTS])} assert it, {len(buckets[DOES_NOT])} do not, '
          f'{len(buckets[UNDECIDABLE])} are undecidable by this reader, of {len(pop)}.')
    print('  ⌗ A gate reading `DOES NOT` is not thereby WRONG: the rule is conditional on the population')
    print('    being able to be empty, and whether each one can is per-gate work this census does not do.')
    print('=' * 100)
    return 0


if __name__ == '__main__':
    if '--seed' in sys.argv:
        sys.exit(seed())
    sys.exit(main())
