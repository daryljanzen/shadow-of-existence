# -*- coding: utf-8 -*-
"""r7869+cc66 ⑨ -- IS Ⓜ⑬'s STRUCTURAL TEST NON-VACUOUS?

`Ⓜ⑬`'s first cut asserted that the identifier `R7860_DIRS` does not appear in the target's source.
`check_quote_pins` reported that as three new quote-pin keys and was right to: a clause keyed on a
spelling in another file goes green the moment the list is renamed.  The arm is structural now --
no `check()` condition may depend on a module-level name bound to a collection of path-like strings.

A structural test that cannot fail is worth nothing, so it is run against the target AS IT STOOD
BEFORE the conversion, read out of git rather than reconstructed.

    NODE=cc66 python3 structural_arm_failability.py
"""
import ast
import io
import json
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
REL = ('receipts/P15_CR_cosmology/P15_the_sections_opening_figures_on_the_one_rate_and_the_'
       'published_comb_is_298_5_not_298_94.py')
PRE_REV = '6cac7e41b'          # this revision's own registration commit, before the conversion
OUT = os.path.join(_HERE, 'structural_arm_failability.json')


def _is_pathish(node):
    elts = None
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        elts = node.elts
    elif isinstance(node, ast.Call) and getattr(node.func, 'id', None) == 'frozenset' and node.args:
        inner = node.args[0]
        elts = inner.elts if isinstance(inner, (ast.Tuple, ast.List, ast.Set)) else None
    if not elts:
        return False
    for e in ast.walk(node):
        if isinstance(e, ast.Constant) and isinstance(e.value, str):
            if os.sep in e.value or e.value in ('computations', 'beyond_the_wall', 'bank'):
                return True
        if isinstance(e, ast.Call) and isinstance(e.func, ast.Attribute) and e.func.attr == 'join':
            return True
    return False


def analyse(src):
    tree = ast.parse(src)
    names = set()
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name) and _is_pathish(n.value):
            names.add(n.targets[0].id)
    gated, conds = set(), 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and getattr(n.func, 'id', None) == 'check' and len(n.args) >= 2:
            conds += 1
            for s in ast.walk(n.args[1]):
                if isinstance(s, ast.Name):
                    gated.add(s.id)
    return dict(pathish=sorted(names), gated_on=sorted(names & gated), conditions=conds)


def main():
    print(__doc__)
    print('=' * 100)
    pre = subprocess.run(['git', 'show', '%s:%s' % (PRE_REV, REL)], cwd=ROOT,
                         stdout=subprocess.PIPE, check=True).stdout.decode('utf-8')
    post = io.open(os.path.join(ROOT, REL), encoding='utf-8').read()
    a, b = analyse(pre), analyse(post)
    a['arm_fails'] = bool(a['gated_on'])
    b['arm_fails'] = bool(b['gated_on'])
    for label, r in (('PRE-conversion (%s)' % PRE_REV, a), ('POST-conversion (live)', b)):
        print('  %-28s path-like %-24s gated on %-20s conditions %d  ⇒ arm %s'
              % (label, r['pathish'], r['gated_on'] or 'NONE', r['conditions'],
                 'FAILS' if r['arm_fails'] else 'passes'))
    ok = a['arm_fails'] and not b['arm_fails']
    print('\n  ⇒ the structural test is %s: it fails on the clause as it stood and passes on the '
          'converted one.' % ('NON-VACUOUS' if ok else '⛔ VACUOUS'))
    io.open(OUT, 'w', encoding='utf-8').write(
        json.dumps(dict(pre=a, post=b, non_vacuous=ok, pre_rev=PRE_REV, target=REL),
                   indent=1, sort_keys=True))
    print('  written %s' % os.path.relpath(OUT, ROOT))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
