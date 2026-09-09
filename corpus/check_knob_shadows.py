#!/usr/bin/env python3
"""check_knob_shadows.py -- A KNOB THAT IS INERT UNDER ANOTHER KNOB MUST SAY SO.

** THE FAILURE THIS CATCHES, AND IT HAS HAPPENED FIVE TIMES. **  A knob read inside a branch
tested on ANOTHER knob is inert whenever that branch is not taken.  Setting it then changes
nothing -- and ** identical numbers read as a NULL RESULT rather than as a dead knob **.  Node
60's r6436 run names `CRIC=branchpoint` as the fifth instance: it takes a branch that sets its
own super-horizon data and never reaches the handover block, so `CRPSI` is inert under it, and
four runs returned identical numbers to the last digit before the cause was found.

** THE DEFECT IS NOT THE SHADOWING. **  Both shadowings in this instrument are by design: the
control arm does not take CR knobs, and a branch-point initial condition legitimately replaces
the handover.  *** The defect is that the shadowing was UNDECLARED, so the only way to find it
was to run four times and notice the numbers were identical. ***

** WHY STATIC, AND WHAT WAS MEASURED BEFORE THIS WAS BUILT. **  Two cheaper checks were tried
and both returned zero on a tree that has the defect:
  * "a knob read and never used" -- ZERO.  `CRPSI` IS used, three times; the defect is
    REACHABILITY, not non-use.
  * a first parse-based detector -- ZERO, and it was WRONG: it passed each statement to the
    walker and then examined only that statement's CHILDREN, so an assignment that IS the env
    read was never itself tested.  ** A detector returning zero on a tree known to contain the
    defect is a detector under test, not a clean tree. **
The corrected walk finds all four shadowings, including the one 60 could only find by running.

⌗ SAME REMEDY AS `node_roster.txt` AND `receipt_home.txt`: the shadowings are DATA, in
`corpus/knob_shadows.txt`, and this gate fails only on an UNDECLARED one.  Nothing is asked to
change; a new shadowing is a one-line edit in the same commit as the code that creates it.

⚠ WHAT THIS DOES NOT DO.  It does not stop a node SETTING an inert knob at runtime -- that wants
the instrument to raise, which is the instrument owner's change and is routed rather than made
here.  This makes the shadowing discoverable by reading instead of by four runs.
"""
import ast
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DECL = os.path.join(HERE, 'knob_shadows.txt')
ROOTS = [os.path.join(HERE, '..', 'computations', 'beyond_the_wall')]
ENV = re.compile(r"os\.(environ\.get|getenv)")


def declared():
    out = set()
    if os.path.exists(DECL):
        for ln in open(DECL, encoding='utf-8'):
            ln = ln.strip()
            if ln and not ln.startswith('#'):
                f = ln.split(None, 3)
                if len(f) >= 3:
                    out.add((f[0], f[1], f[2]))
    return out


def env_knob(node):
    if (isinstance(node, ast.Assign) and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Attribute)
            and ENV.search(ast.unparse(node.value.func))
            and node.value.args and isinstance(node.value.args[0], ast.Constant)):
        return node.value.args[0].value
    return None


def scan(path):
    """(knob, shadowing_knob, lineno) for every knob read inside a branch on another knob."""
    try:
        tree = ast.parse(open(path, encoding='utf-8').read())
    except SyntaxError:
        return []
    knobvar = {}
    for n in ast.walk(tree):
        k = env_knob(n)
        if k:
            for t in n.targets:
                if isinstance(t, ast.Name):
                    knobvar[t.id] = k
    found = []

    def visit(node, stack):
        k = env_knob(node)                      # test the NODE ITSELF, not only its children
        if k and stack:
            for g in sorted({g for gs in stack for g in gs} - {k}):
                found.append((k, g, node.lineno))
        if isinstance(node, ast.If):
            names = {x.id for x in ast.walk(node.test) if isinstance(x, ast.Name)}
            gk = {knobvar[v] for v in names if v in knobvar}
            for sub in node.body + node.orelse:
                visit(sub, stack + ([gk] if gk else []))
            return
        for ch in ast.iter_child_nodes(node):
            visit(ch, stack)

    visit(tree, [])
    return found


def main():
    dec = declared()
    if not dec:
        print('  [FAIL] corpus/knob_shadows.txt is absent -- the shadowings are data and must exist')
        return 1
    print()
    print('  KNOB SHADOWS -- a knob inert under another knob must be declared')
    print()
    undeclared, total = [], 0
    for root in ROOTS:
        if not os.path.isdir(root):
            continue
        for f in sorted(os.listdir(root)):
            if not f.endswith('.py'):
                continue
            for knob, by, ln in scan(os.path.join(root, f)):
                total += 1
                if (f, knob, by) not in dec:
                    undeclared.append((f, knob, by, ln))
    print(f'    {total} shadowing(s) found, {len(dec)} declared')
    print()
    if undeclared:
        print(f'  ⛔ {len(undeclared)} UNDECLARED SHADOWING(S):')
        for f, knob, by, ln in undeclared:
            print(f'    [FAIL] {f}:{ln}  {knob} is inert whenever the branch on {by} is not taken')
        print('     Setting it then changes nothing, and identical numbers read as a null')
        print('     result.  Declare it in corpus/knob_shadows.txt, in the same commit.')
        print()
        return 1
    print('  every shadowing is declared.')
    print('  ⌗ This makes an inert knob discoverable by READING.  It does not stop one being')
    print('    set at runtime -- that wants the instrument to raise, and is the owner\'s change.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
