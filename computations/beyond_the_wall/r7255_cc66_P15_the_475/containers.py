#!/usr/bin/env python3
"""r7255 order ②: resolve, per key, WHAT CONTAINER THE RECEIPT ACTUALLY READS -- from the receipt's
syntax tree, not from where the literal happens to occur.

** WHY THIS EXISTS, AND IT IS A CORRECTION TO THIS CYCLE'S OWN cc66.173. **  That pass measured
`real_target` by counting occurrences of the literal in the papers, the instruments and the
receipts, and reported 66 of the 475 as target mislabels.  Reading the sites showed the probe was
conflating two different questions.  `full-spectrum likelihood` is read out of `po10` -- a REGISTRY
ROW -- and also occurs twelve times in the papers, so an occurrence count calls it PAPER while the
receipt is reading a registry.  ** Where the literal occurs is not what the receipt reads. **

So the container is taken from the AST: the right-hand side of the `in` test, or the second argument
of `re.search`, traced back through its assignment to the FILE the receipt opened.  The kinds are
PAPER (corpus/*.tex), INSTRUMENT (computations/), RECEIPT (receipts/*.py), REGISTRY (a ledger, an
index, an order file, a registry row) and PINNED (a `git show <commit>:path` read of a historical
state, which is L-249's own prescribed form and not a live read at all).
"""
import ast
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))

REGISTRY_HINT = re.compile(r'INDEX\.md|FOR_\w+\.md|_MAP\.md|WORKING_STATE|HANDOFF|RUN_SPEC|'
                           r'frontier|registry|baseline\.tsv|\bPO-|\bL-\d|open_items|ledger')


def kind_of_path(p):
    q = p.replace('\\', '/')
    if REGISTRY_HINT.search(q):
        return 'REGISTRY'
    if '/corpus/' in q or q.startswith('corpus/'):
        return 'PAPER' if q.endswith('.tex') else 'REGISTRY'
    if '/computations/' in q or q.startswith('computations/'):
        return 'INSTRUMENT'
    if '/receipts/' in q or q.startswith('receipts/') or q.endswith('.py'):
        return 'RECEIPT'
    return 'OTHER'


class Resolver:
    """name -> kind, by walking the receipt's assignments once."""

    def __init__(self, src):
        self.tree = ast.parse(src)
        self.assign = {}
        for n in ast.walk(self.tree):
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    if isinstance(t, ast.Name):
                        self.assign.setdefault(t.id, n.value)
                    elif isinstance(t, ast.Tuple):
                        for i, e in enumerate(t.elts):
                            if isinstance(e, ast.Name) and isinstance(n.value, ast.Tuple) \
                                    and i < len(n.value.elts):
                                self.assign.setdefault(e.id, n.value.elts[i])
        self.memo = {}

    def kind(self, node, depth=0):
        if depth > 8 or node is None:
            return 'UNKNOWN'
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return kind_of_path(node.value)
        if isinstance(node, ast.Name):
            if node.id in self.memo:
                return self.memo[node.id]
            self.memo[node.id] = 'UNKNOWN'          # cycle guard
            k = self.kind(self.assign.get(node.id), depth + 1)
            self.memo[node.id] = k
            return k
        if isinstance(node, ast.Call):
            txt = ast.unparse(node)
            # a historical read is PINNED whatever the path, because that is L-249's own form
            if 'git' in txt and 'show' in txt:
                return 'PINNED'
            if re.search(r'_?p\w*_at\(|_at_commit\(|at_rev\(|_then\(', txt):
                return 'PINNED'
            if re.match(r'rcpt\(', txt):
                return 'RECEIPT'
            # ⌗ os.path.join('corpus', 'CR_cosmology.tex') classifies as nothing one fragment at a
            #   time -- neither piece is a path.  Join every string constant in the call's subtree
            #   first.  The first draft returned UNKNOWN on 302 of the 475 for exactly this.
            frags = [c.value for c in ast.walk(node)
                     if isinstance(c, ast.Constant) and isinstance(c.value, str)]
            if frags:
                k = kind_of_path('/'.join(frags))
                if k not in ('UNKNOWN', 'OTHER'):
                    return k
            for a in list(node.args) + [node.func]:
                k = self.kind(a, depth + 1)
                if k not in ('UNKNOWN', 'OTHER'):
                    return k
            return 'UNKNOWN'
        if isinstance(node, (ast.Attribute,)):
            return self.kind(node.value, depth + 1)
        if isinstance(node, (ast.Subscript,)):
            return self.kind(node.value, depth + 1)
        if isinstance(node, (ast.BinOp,)):
            for a in (node.left, node.right):
                k = self.kind(a, depth + 1)
                if k not in ('UNKNOWN', 'OTHER'):
                    return k
            return 'UNKNOWN'
        if isinstance(node, (ast.JoinedStr, ast.ListComp, ast.GeneratorExp)):
            for a in ast.walk(node):
                if a is node:
                    continue
                if isinstance(a, (ast.Constant, ast.Name, ast.Call)):
                    k = self.kind(a, depth + 1)
                    if k not in ('UNKNOWN', 'OTHER'):
                        return k
            return 'UNKNOWN'
        return 'UNKNOWN'

    def sites(self):
        """literal -> set of (container expression, resolved kind)"""
        out = collections.defaultdict(set)
        for n in ast.walk(self.tree):
            if isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], (ast.In, ast.NotIn)):
                if isinstance(n.left, ast.Constant) and isinstance(n.left.value, str):
                    c = n.comparators[0]
                    out[n.left.value].add((ast.unparse(c)[:60], self.kind(c)))
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) \
                    and n.func.attr in ('search', 'match', 'findall', 'fullmatch', 'count', 'partition', 'index'):
                args = n.args
                if n.func.attr in ('count', 'partition', 'index'):
                    if args and isinstance(args[0], ast.Constant) and isinstance(args[0].value, str):
                        out[args[0].value].add((ast.unparse(n.func.value)[:60], self.kind(n.func.value)))
                elif len(args) > 1 and isinstance(args[0], ast.Constant) and isinstance(args[0].value, str):
                    out[args[0].value].add((ast.unparse(args[1])[:60], self.kind(args[1])))
        return out


def main():
    meas = os.path.join(HERE, 'MEASURED.tsv')
    rows = [l.rstrip('\n').split('\t') for l in open(meas, encoding='utf-8')
            if l.strip() and not l.startswith('#')]
    cache = {}
    out = []
    for r in rows:
        stem = r[0]
        if stem not in cache:
            cache[stem] = Resolver(open(os.path.join(ROOT, stem), encoding='utf-8').read()).sites()
        try:
            raw = json.loads(r[5])
        except Exception:
            raw = r[5].strip('"')
        hits = cache[stem].get(raw, set())
        exprs = sorted({e for e, _ in hits})
        kinds = sorted({k for _, k in hits})
        kind = kinds[0] if len(kinds) == 1 else ('/'.join(kinds) if kinds else 'UNRESOLVED')
        out.append(r + [kind, ';'.join(exprs)[:90] or '-'])
    dest = os.path.join(HERE, 'CONTAINERS.tsv')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('# r7255 order ② -- MEASURED.tsv plus the container the receipt ACTUALLY READS,\n')
        fh.write('# resolved from each receipt\'s syntax tree.  See this file\'s builder for why the\n')
        fh.write('# occurrence-based real_target column of cc66.173 is not the same question.\n')
        fh.write('# ...MEASURED columns...\tcontainer_kind\tcontainer_expr\n')
        for r in out:
            fh.write('\t'.join(r) + '\n')
    print(f'{len(out)} rows -> {dest}')
    print(collections.Counter(r[-2] for r in out).most_common())


if __name__ == '__main__':
    main()
