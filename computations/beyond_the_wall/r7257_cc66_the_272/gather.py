#!/usr/bin/env python3
"""`r7257` order ① and ②: gather, for each of the `272` `MEANING-HELD` rows, everything a MACHINE can
say about it -- and nothing a machine cannot.

** THE POPULATION IS PINNED, AND THAT IS THE WHOLE POINT. **  It is read with
`git show 2654cd0b:corpus/quote_pin_baseline.tsv`.  `MEANING-HELD` is exactly the column this cycle's
work would move, so selecting the population off the live file is the fail-on-success class instance
`16` under a different name -- my own `measure.py` last cycle selected off the verdict column and
watched its file shrink 475 -> 227 as the batches landed.

What this script does NOT do: decide whether a row is computable.  That is a reading, it is recorded
in READING_*.tsv by hand against the rule frozen in PREDICTION.md, and every row called computable
carries the CONCRETE CONVERSE EDIT that reds its predicate.  This script only lays out the evidence
the reading needs: the asserting site, the container the receipt actually reads, and -- for order ② --
what the HOLDING RECEIPT is already capable of, because a form that needs a quantity the receipt does
not compute is not available to it.
"""
import ast
import collections
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7255_cc66_P15_the_475'))
from containers import Resolver                                     # noqa: E402

PREREG_REV = '2654cd0b'        # the revision this cycle's PREDICTION.md pinned the population to
HELD = 'MEANING-HELD'


def ledger():
    """the ledger AS IT STOOD AT THE PRE-REGISTRATION.  never the live file: see the module note."""
    out = subprocess.run(['git', 'show', f'{PREREG_REV}:corpus/quote_pin_baseline.tsv'],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    rows = []
    for line in out.splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        if len(f) >= 7 and f[5] == HELD:
            rows.append(f)
    return rows


# ───────────────────────────── order ②: what can the HOLDER already do ─────────────────────────────
# ⌗ these are CAPABILITY facts, read off the receipt's own source.  They do not decide carryability on
#   their own -- a receipt that imports `ast` for one purpose may still have no admissible read of the
#   file a given form needs -- but they bound it, and the bound is what order ② asks for.
CAP = {
    'AST':     re.compile(r'\bimport ast\b|\bast\.parse\b|\bast\.walk\b'),
    'NUM':     re.compile(r'\bimport numpy\b|\bimport scipy\b|\bfrom scipy\b|\bnp\.|\bmath\.'),
    'SUBPROC': re.compile(r'\bsubprocess\.(run|check_output|Popen)\b'),
    'GITSHOW': re.compile(r"'show'|\"show\"|git show"),
    'DIGEST':  re.compile(r'\bhashlib\b|\bDIGEST\b|blake2|sha256'),
    'SOLVE':   re.compile(r'odeint|solve_ivp|quad\(|brentq|curve_fit|minimize\(|least_squares'),
    # ⌗ r7257+cc66.5 -- sympy was missing from the first capability set and 108 modules of this corpus
    #   use it.  An exact group-order or parity claim is carried by sympy and not by numpy, so without
    #   this row order ② would have called a carryable algebraic form uncarryable.
    'SYMPY':   re.compile(r'\bimport sympy\b|\bfrom sympy\b|\bsp\.(Matrix|symbols|simplify)'),
    'FRAC':    re.compile(r'\bfrom fractions\b|\bimport fractions\b|\bitertools\b'),
}


def reads(src):
    """WHAT THE HOLDER ALREADY OPENS, by extension and directory -- which is the form order ② needs.

    ⛔ r7257+cc66.1 -- the first draft repeated last cycle's own `os.path.join` bug in a new function:
      it regexed `open\(([^)]*)\)`, which stops at the `)` inside `os.path.join(ROOT, 'corpus', f)`,
      and classified the fragments one at a time, so 197 of the 272 came back reading NOTHING --
      including receipts whose every gate reads a paper.  ** A receipt that pins a paper sentence and
      reads nothing is not a measurement, it is a broken probe, and it was visible in one line of the
      probe's own output. **
    ⌗ r7257+cc66.2 -- and the AST rewrite still missed `open(os.path.join(ROOT, 'corpus', f))`, where
      the FILENAME is a parameter and only the DIRECTORY is a constant.  The question order ② actually
      asks is not "which container kind" but "** is the file an AST form needs already inside what this
      receipt opens **", so the answer is taken by EXTENSION AND DIRECTORY over every path-shaped
      constant in the receipt, whether or not it sits in the `open()` call itself.
    """
    out = set()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    consts = [c.value for c in ast.walk(tree)
              if isinstance(c, ast.Constant) and isinstance(c.value, str)]
    for v in consts:
        q = v.replace('\\', '/')
        if q in ('utf-8', 'replace', 'ignore', 'r', 'rb', 'w'):
            continue
        for ext, tag in (('.tex', 'TEX'), ('.py', 'PY'), ('.tsv', 'TSV'),
                         ('.md', 'MD'), ('.json', 'JSON'), ('.npz', 'NPZ'), ('.pkl', 'PKL')):
            if q.endswith(ext) or ('*' + ext) in q:
                out.add(tag)
        for d, tag in (('corpus', 'D:corpus'), ('receipts', 'D:receipts'),
                       ('computations', 'D:computations'), ('scripts', 'D:scripts')):
            if q == d or q.startswith(d + '/') or ('/' + d + '/') in q:
                out.add(tag)
    return out


def indirect_sites(src):
    """literal -> {(container expr, kind)} for literals the receipt BINDS TO A NAME before testing.

    ⌗ r7257+cc66.2 -- `containers.Resolver` keys a site only when the `in` test's left operand is a
      string CONSTANT, which is the operator's own rule.  17 of the 272 came back `UNRESOLVED` and
      every one is the same shape: the sentence is assigned to a name or collected in a list
      (`P16_NEGATIVES = [...]`, `RULE07 = (...)`, `_not_diffeo = '...'`) and the membership test runs
      over the NAME, directly or through `all(x in body for x in LIST)`.  ** The container is perfectly
      determinate there; only the syntax is indirect. **  Resolved here rather than in `containers`,
      because changing the operator's keying rule is 70's file and not mine to widen.
    """
    out = collections.defaultdict(set)
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    res = Resolver(src)
    bound = collections.defaultdict(list)          # name -> [string constants reachable from it]
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            vals = [c.value for c in ast.walk(n.value)
                    if isinstance(c, ast.Constant) and isinstance(c.value, str) and len(c.value) > 3]
            for t in n.targets:
                if isinstance(t, ast.Name):
                    bound[t.id].extend(vals)

    def give(container_node, names):
        k = res.kind(container_node)
        expr = ast.unparse(container_node)[:60]
        for nm in names:
            for v in bound.get(nm, ()):
                out[v].add((expr, k))

    for n in ast.walk(tree):
        if isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], (ast.In, ast.NotIn)):
            if isinstance(n.left, ast.Name):
                give(n.comparators[0], [n.left.id])
        if isinstance(n, (ast.GeneratorExp, ast.ListComp, ast.SetComp)):
            tgt = {g.target.id for g in n.generators if isinstance(g.target, ast.Name)}
            iters = {g.iter.id for g in n.generators if isinstance(g.iter, ast.Name)}
            for c in ast.walk(n.elt):
                if isinstance(c, ast.Compare) and len(c.ops) == 1 \
                        and isinstance(c.ops[0], (ast.In, ast.NotIn)) \
                        and isinstance(c.left, ast.Name) and c.left.id in tgt:
                    give(c.comparators[0], iters)
                # ⌗ r7257+cc66.4 -- `all(B['P16'].count(ph) == 1 for ph in P16_NEGATIVES)`.  The
                #   remaining 10 UNRESOLVED rows are all this one shape, all in one receipt, and the
                #   container is as determinate as any `in` test: it is the receiver of `.count`.
                #   ⛔ NOTE FOR THE READING: `.count(x) == n` is NOT a form the operator keys, by its
                #   own rule, yet these keys are in the ledger.  That is a fact about how they were
                #   minted, not about this probe, and it is reported rather than smoothed.
                if isinstance(c, ast.Call) and isinstance(c.func, ast.Attribute) \
                        and c.func.attr in ('count', 'find', 'index', 'rfind'):
                    if any(isinstance(a, ast.Name) and a.id in tgt for a in c.args):
                        give(c.func.value, iters)
    return out


def trace_kind(src, expr):
    """resolve a container EXPRESSION to a kind by TRANSITIVE CLOSURE over the receipt's own bindings.

    ⌗ r7257+cc66.3 -- `containers.Resolver` resolves one hop: a name to its assignment, an assignment
      to a path constant.  31 of the 272 came back UNKNOWN because the receipts bind in several hops --
      `_view = re.sub(..., _prose)`, `body15 = flat(''.join(ln for ln in p15.splitlines()))`,
      `p14 = flat_p14()`, `rp = re.sub(..., open(ROOT/'THE_PHYSICS_REACH.md'))` -- and through LOCAL
      FUNCTIONS, where the path lives in the callee's body and not in the call.  ** Every one of the 31
      is determinate; the chain is just longer than one link. **  So: follow names and local calls to
      fixpoint, collect every string constant reachable, and classify by extension first, because an
      extension is a kind even when the directory is a parameter.

    ⌗ EXTENSION FIRST IS THE PART THAT MATTERS.  `open(os.path.join(ROOT, 'corpus', f))` has no path
      constant at all -- the directory is `'corpus'` and the filename is the parameter -- so a
      path-shaped classifier returns nothing.  A `.tex` constant anywhere in the chain says PAPER,
      because every `.tex` in this corpus is a paper.
    """
    from containers import kind_of_path
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return 'UNKNOWN'
    assigns, funcs = collections.defaultdict(list), {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            # ⌗ r7257+cc66.4 -- three binding shapes the one-hop resolver and my own first closure both
            #   missed, each worth rows: `p0, p9 = pub('a.tex'), pub('b.tex')` (TUPLE target, element
            #   aligned); `src, p15, p07 = (open(f) for f in (INSTR, P15, P07))` (tuple target, ONE
            #   value, so every name takes the whole generator); and `B[pid] = body_of(...)` (SUBSCRIPT
            #   target, which is how a receipt builds a dict of paper bodies).  ** A resolver that only
            #   knows `name = value` reads a corpus whose receipts mostly do not write that. **
            for t in n.targets:
                if isinstance(t, ast.Name):
                    assigns[t.id].append(n.value)
                elif isinstance(t, (ast.Tuple, ast.List)):
                    val = n.value
                    elts = val.elts if isinstance(val, (ast.Tuple, ast.List)) else None
                    for i, e in enumerate(t.elts):
                        if not isinstance(e, ast.Name):
                            continue
                        assigns[e.id].append(elts[i] if elts and i < len(elts) else val)
                elif isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name):
                    assigns[t.value.id].append(n.value)
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            # ⌗ `for pid, fn in (('P15', 'CR_cosmology.tex'), ...)` -- a LOOP binding, which is where
            #   the twelve dict-of-bodies rows keep their filenames.  A closure over assignments alone
            #   cannot see it, and `B[pid] = body_of(ROOT/'corpus'/fn)` then resolves to nothing.
            tgts = [t for t in ([n.target] if isinstance(n.target, ast.Name) else
                                getattr(n.target, 'elts', [])) if isinstance(t, ast.Name)]
            for t in tgts:
                assigns[t.id].append(n.iter)
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs[n.name] = n

    seen, frontier, consts = set(), [], []
    root = re.match(r'[A-Za-z_]\w*', expr.strip())
    if not root:
        return 'UNKNOWN'
    frontier.append(('name', root.group(0)))
    while frontier:
        kind, item = frontier.pop()
        if (kind, item) in seen or len(seen) > 400:
            continue
        seen.add((kind, item))
        nodes = assigns.get(item, []) if kind == 'name' else ([funcs[item]] if item in funcs else [])
        for nd in nodes:
            for c in ast.walk(nd):
                if isinstance(c, ast.Constant) and isinstance(c.value, str):
                    consts.append(c.value)
                elif isinstance(c, ast.Name):
                    frontier.append(('name', c.id))
                elif isinstance(c, ast.Call):
                    f = c.func
                    nm = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else None)
                    if nm:
                        frontier.append(('func', nm))
                        frontier.append(('name', nm))

    for v in consts:                                    # extension first: an extension IS a kind
        q = v.replace('\\', '/')
        if q.endswith('.tex') or '*.tex' in q:
            return 'PAPER'
    for v in consts:
        k = kind_of_path(v)
        if k not in ('UNKNOWN', 'OTHER'):
            return k
    # ⌗ `open(os.path.join(ROOT, 'corpus', fn))` -- the directory is constant and the FILENAME is the
    #   loop variable.  Every tracked `corpus/*.tex` is a paper and the receipt reading this also
    #   carries `.tex` constants, so the kind is PAPER; a bare `corpus` fragment resolves to nothing
    #   one piece at a time, which is last cycle's bug wearing a third face.
    if any(v == 'corpus' or v.startswith('corpus/') for v in consts) and \
            any(v.endswith('.tex') for v in consts):
        return 'PAPER'
    for v in consts:
        q = v.replace('\\', '/')
        if q.endswith('.md') or q.endswith('.tsv'):
            return 'REGISTRY'
        if q.endswith('.py'):
            return 'RECEIPT'
    return 'UNKNOWN'


def constant_lines(src):
    """value -> (lineno, the source line) for every string constant, FROM THE AST.

    ⛔ r7257+cc66.1 -- the first draft searched the raw source text for the literal and reported
      `line 0` on 17 rows.  Every one was a false absence: the ledger stores the literal DECODED
      (`\\mathrm` once), while the source as typed carries `\\\\mathrm`, and the same goes for `\\'`
      and for a literal split across two lines by implicit concatenation.  ** A text search over
      source cannot find a Python string; only the parser can. **  Last cycle 13 literals read as
      ABSENT for a cousin of this reason and 7 of them turned out to be pinned reads.
    """
    out = {}
    lines = src.splitlines()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return out
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) > 3:
            ln = getattr(n, 'lineno', 0)
            if n.value not in out and 0 < ln <= len(lines):
                out[n.value] = (ln, lines[ln - 1].strip()[:200])
    return out


def gate_count(src):
    return len(re.findall(r'^\s*gate\(', src, re.M)) or len(re.findall(r'\bgate\(', src))


def main():
    rows = ledger()
    assert len(rows) == 272, f'population moved: {len(rows)} rows, not 272 -- STOP, do not reweight'
    srcs, sites, indirect, caps = {}, {}, {}, {}
    for f in rows:
        stem = f[0]
        if stem in srcs:
            continue
        p = os.path.join(ROOT, stem)
        src = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        srcs[stem] = src
        sites[stem] = Resolver(src).sites() if src else {}
        indirect[stem] = indirect_sites(src) if src else {}
        caps[stem] = ([n for n, rx in CAP.items() if rx.search(src)], sorted(reads(src)),
                      src.count('\n') + 1, gate_count(src))

    # the asserting LINE, so the reading sees what the receipt does with the literal -- taken from
    # the AST, never from a text search over source.  See constant_lines' note.
    cmap = {stem: constant_lines(src) for stem, src in srcs.items()}

    def site_line(stem, lit):
        hit = cmap[stem].get(lit)
        if hit:
            return hit
        for v, (ln, text) in cmap[stem].items():            # a longer constant containing it
            if lit in v:
                return ln, text
        return 0, '-'

    out = []
    for f in rows:
        stem, raw = f[0], f[1]
        try:
            lit = json.loads(raw)
        except Exception:
            lit = raw.strip('"')
        hits = sites[stem].get(lit, set()) or indirect[stem].get(lit, set())
        kinds = sorted({k for _, k in hits}) or ['UNRESOLVED']
        if kinds == ['UNKNOWN'] or (len(kinds) == 1 and kinds[0] == 'UNKNOWN'):
            for e, _ in hits:
                k2 = trace_kind(srcs[stem], e)
                if k2 != 'UNKNOWN':
                    kinds = [k2]
                    break
        ln, text = site_line(stem, lit)
        c = caps[stem]
        out.append([stem, raw, f[2], f[4] or '-', '/'.join(kinds),
                    ';'.join(sorted({e for e, _ in hits}))[:80] or '-', str(ln), text,
                    '+'.join(c[0]) or '-', '+'.join(c[1]) or '-', str(c[2]), str(c[3])])

    dest = os.path.join(HERE, 'GATHERED.tsv')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write(f'# r7257 order ①/② -- the {len(out)} MEANING-HELD rows at {PREREG_REV}, with the\n')
        fh.write('# asserting site, the container the receipt actually reads, and the holder\'s own\n')
        fh.write('# capabilities.  NOTHING here decides computability: that reading is by hand in\n')
        fh.write('# READING_*.tsv against the rule frozen in PREDICTION.md, with a converse per row.\n')
        fh.write('stem\tliteral\tledger_target\tflags\tcontainer\tcontainer_expr\tline\t'
                 'site_text\tholder_caps\tholder_reads\tholder_lines\tholder_gates\n')
        for r in out:
            fh.write('\t'.join(r) + '\n')
    print(f'{len(out)} rows -> {dest}')
    print('container :', collections.Counter(r[4] for r in out).most_common())
    print('caps      :', collections.Counter(r[8] for r in out).most_common(10))
    print('reads     :', collections.Counter(r[9] for r in out).most_common(10))
    print('receipts  :', len(srcs))


if __name__ == '__main__':
    main()
