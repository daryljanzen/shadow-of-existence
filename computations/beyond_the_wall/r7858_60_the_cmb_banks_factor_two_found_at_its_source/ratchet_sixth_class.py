# -*- coding: utf-8 -*-
"""r7858 (60) -- A SIXTH INERT CLASS FOR THE `FOURPI` GUARD, MEASURED AGAINST THE BANKED BLOB.

⛔ **WHY THIS FILE EXISTS.**  Adding one environment switch to the shared instrument turns three of
`cc66`'s receipts red: two stamp the instrument's source hash through the AST provenance ratchet and
one stamps its switch census.  Those receipts are NOT this seat's to edit, so the patch is measured
here and ROUTED in `FOR_66_FROM_60.md` rather than applied.

⛭ **THE DOCTRINE THIS FOLLOWS, from `r7854`:** a line rewritten into an equal-valued DIFFERENT form
is a difference the ratchet is right to keep red, so new code is written as *the landed line plus a
guard that is exactly one when the switch is off* -- and the class below is allowed to collapse a
factor ONLY when that guard's own `orelse` is the literal `1.0`.  A factor written `else 2.0` moves
the default output, and the controls show it stays red.

⚠ **STATED SCOPE:** the class certifies the tree is the landed one WHEN THE SWITCH IS UNSET.  It
says nothing about what the switch does when SET, so the same unit factor at a third site passes.
That is the scope of every class in this ratchet, and it is reported below rather than hidden.

    python3 ratchet_sixth_class.py        # rc=0 when all eight hold
"""
import ast as _ast, io, os, subprocess, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
#: ⛔ FOUR dirnames, and an assertion that says so: this file sits three directories below the
#:   repository root, and the same arithmetic written with one too few is the defect `Ⓒ③ᵇ`
#:   caught in this very revision -- a path that resolves to the wrong directory and a sweep that
#:   silently finds nothing.  It cost one run here too, which is why the assertion is on the line.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BLOB = 'e5319ce4968602ca6d8de89fdc871e8f9b0a645e'
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')


def _inert_unit_factors(tree):
    """the names whose OWN assignment is `<something> if FOURPI else 1.0` -- and no others.

    â The collapse below is allowed ONLY for these.  A factor written `else 2.0` is not
    exactly one when the switch is off, so it moves the default output and this ratchet must
    keep it red: that is the whole difference between a guard and an edit."""
    out = set()
    for n in _ast.walk(tree):
        if not isinstance(n, _ast.Assign) or len(n.targets) != 1:
            continue
        t, v = n.targets[0], n.value
        if not (isinstance(t, _ast.Name) and isinstance(v, _ast.IfExp)):
            continue
        if not (isinstance(v.test, _ast.Name) and v.test.id == 'FOURPI'):
            continue
        o = v.orelse
        if (isinstance(o, _ast.Constant) and not isinstance(o.value, bool)
                and isinstance(o.value, (int, float)) and o.value == 1):
            out.add(t.id)
    return out


def make_strip(sixth, unit=frozenset()):
    class _Strip(_ast.NodeTransformer):
        NAMES = ({'_dneff', 'DNEFF', '_yhe', 'YHE', 'MNU', 'ONU', 'BVEL', 'I_DB_F', 'I_TBF'}
                 | (({'FOURPI'} | set(unit)) if sixth else set()))

        def visit_BinOp(self, node):
            r = node.right
            if (isinstance(node.op, (_ast.Add, _ast.Sub)) and isinstance(r, _ast.IfExp)
                    and isinstance(r.test, _ast.Name) and r.test.id == 'BVEL'
                    and isinstance(r.orelse, _ast.Constant) and r.orelse.value == 0):
                return self.visit(node.left)
            # --- sixth class: a factor that is exactly 1.0 unset, applied to a landed expression
            if (sixth and isinstance(node.op, (_ast.Mult, _ast.Div))
                    and isinstance(r, _ast.Name) and r.id in unit):
                return self.visit(node.left)
            self.generic_visit(node)
            if isinstance(node.op, _ast.Sub) and isinstance(node.right, _ast.Name) and node.right.id == 'ONU':
                return node.left
            return node

        def visit_IfExp(self, node):
            self.generic_visit(node)
            if isinstance(node.test, _ast.Name) and node.test.id == 'BVEL':
                return node.orelse
            if sixth and isinstance(node.test, _ast.Name) and node.test.id == 'FOURPI':
                return node.orelse
            return node

        def visit_Expr(self, node):
            if "id='MNU'" in _ast.dump(node) and "id='print'" in _ast.dump(node):
                return None
            self.generic_visit(node)
            return node

        def visit_Call(self, node):
            self.generic_visit(node)
            f = node.func
            if (isinstance(f, _ast.Attribute) and f.attr == 'savez' and node.args
                    and isinstance(node.args[0], _ast.Name) and node.args[0].id == '_POLS'):
                node.keywords = [k for k in node.keywords if k.arg != 'config']
            return node

        def visit_Assign(self, node):
            t = node.targets[0]
            if isinstance(t, _ast.Name) and t.id in self.NAMES:
                return None
            v = node.value
            if (isinstance(v, _ast.IfExp) and isinstance(v.test, _ast.Name) and v.test.id == 'BVEL'):
                return None
            self.generic_visit(node)
            return node

        def visit_Assert(self, node):
            if "id='BVEL'" in _ast.dump(node.test):
                return None
            return node

        def visit_If(self, node):
            s = _ast.dump(node.test)
            if "id='DNEFF'" in s or "id='YHE'" in s:
                return None
            if isinstance(node.test, _ast.Name) and node.test.id == 'BVEL' and not node.orelse:
                return None
            if (isinstance(node.test, _ast.UnaryOp) and isinstance(node.test.op, _ast.Not)
                    and isinstance(node.test.operand, _ast.Name) and node.test.operand.id == 'BVEL'
                    and not node.orelse):
                self.generic_visit(node)
                return node.body
            self.generic_visit(node)
            return node

        def visit_Dict(self, node):
            self.generic_visit(node)
            keep = [(k, v) for k, v in zip(node.keys, node.values)
                    if not (isinstance(k, _ast.Constant) and k.value in ('DNEFF', 'YHE'))]
            node.keys = [k for k, _ in keep]
            node.values = [v for _, v in keep]
            return node
    return _Strip


OLD = subprocess.run(['git', 'cat-file', '-p', BLOB], cwd=ROOT,
                     capture_output=True).stdout.decode()
NEW = open(INST).read()
assert OLD and NEW


def holds(src, sixth=True):
    tree = _ast.parse(src)
    unit = _inert_unit_factors(tree) if sixth else frozenset()
    return _ast.dump(_ast.parse(OLD)) == _ast.dump(make_strip(sixth, unit)().visit(tree))


res = {}
res['the landed FIVE classes leave this tree RED (so the sixth is needed, not decorative)'] = \
    holds(NEW, sixth=False) is False
res['with the sixth class the tree reduces to the banked blob'] = holds(NEW) is True
# controls: three real changes to landed code, and one to the landed side of the new factor
ctl = [
    ('a landed constant moved', NEW.replace('VISC = 16.0 / 45.0', 'VISC = 16.0 / 44.0', 1)),
    ('a landed line deleted', NEW.replace('VISC = 16.0 / 45.0\n', '', 1)),
    ('the LANDED operand of the new factor changed',
     NEW.replace('out[j] = np.sum(P * _tr ** 2) * _FP_ACC',
                 'out[j] = np.sum(P * _tr ** 3) * _FP_ACC', 1)),
    ('the guard made live-when-off (1.0 -> 2.0)',
     NEW.replace('_FP_DL = 2.0 * np.pi if FOURPI else 1.0',
                 '_FP_DL = 2.0 * np.pi if FOURPI else 2.0', 1)),
]
for name, src in ctl:
    changed = src != NEW
    res['control, kept RED: ' + name] = changed and holds(src) is False
res['control, kept RED: a landed default moved (TCSW 3.0 -> 3.5)'] = \
    holds(NEW.replace("os.environ.get('TCSW', '3.0')", "os.environ.get('TCSW', '3.5')", 1)) is False
res['control, kept RED: an UNGUARDED factor on a landed expression'] = \
    holds(NEW.replace('VISC = 16.0 / 45.0', 'VISC = 16.0 / 45.0 * 2.0', 1)) is False
# â STATED LIMIT, measured rather than claimed: the class certifies the tree is the landed one
#   WHEN THE SWITCH IS UNSET, and says nothing about what the switch does when SET -- so the same
#   unit factor added at a THIRD site passes.  That is the scope of every class in this ratchet
#   (an `if DNEFF:` block's contents are dropped wholesale too), and it is reported, not hidden.
_third = NEW.replace('VISC = 16.0 / 45.0', 'VISC = 16.0 / 45.0 * _FP_ACC', 1)
print('  LIMIT  the same unit factor at a THIRD site passes (switch-off output unmoved): %s'
      % holds(_third))

for k, v in res.items():
    print('  %s  %s' % ('OK  ' if v else 'FAIL', k))
print('  %d of %d hold' % (sum(res.values()), len(res)))
import json
with io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          'ratchet_sixth_class.json'), 'w', encoding='utf-8') as fh:
    fh.write(unicode(json.dumps(dict(
        blob=BLOB, holds=all(res.values()), n_hold=sum(res.values()), n=len(res),
        third_site_passes=holds(_third), checks=res), indent=2, sort_keys=True))
        if str is bytes else json.dumps(dict(
            blob=BLOB, holds=all(res.values()), n_hold=sum(res.values()), n=len(res),
            third_site_passes=holds(_third), checks=res), indent=2, sort_keys=True))
sys.exit(0 if all(res.values()) else 1)
