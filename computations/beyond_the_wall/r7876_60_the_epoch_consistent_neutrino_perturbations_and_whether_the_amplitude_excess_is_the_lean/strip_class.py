# -*- coding: utf-8 -*-
"""r7876+60 — THE EIGHTH STRIP CLASS, MEASURED BEFORE IT IS ROUTED.

This revision added two environment switches to the instrument, so the instrument's blob moved and
two shared `P15` receipts that compare the working tree against a BANKED blob go red. Those receipts
carry an AST escape hatch -- strip the inert additions a later revision made and compare what is
left against the banked tree -- and each seat that adds a switch extends it, by routing a patch that
`69` applies: `BVEL` at `r7851`, `FOURPI` at `r7857`, `NUFD` at `r7865`, all from this line's
patches, and `POLSAVE` at `r7807` from `cc66`'s.

⌗ **THIS FILE IS THE MEASUREMENT THE CONVENTION ASKS FOR, NOT THE EDIT.** The receipts are not
  touched. What is measured here is exactly what those earlier patches measured:

    ① THE FIXED POINT -- the eighth class reduces the working tree to the banked blob.
    ② THE FLOOR      -- the seven landed classes WITHOUT the eighth leave it red, so the eighth is
                        doing the work and is not a no-op riding on the others.
    ③ THE CONTROLS   -- six mutations of the LANDED code each stay red, so the class strips this
                        revision's additions and not the code they were added to.

    NODE=60 python3 strip_class.py
"""
import ast
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
INST = os.path.join(BW, 'ACOUSTIC_two_arm.py')
#: the bank whose stored blob the two receipts compare against
ARMNPZ = os.path.join(BW, 'spectra', 'cc66_r185_verify_cr_leafrec1.npz')

#: ⛭ ** THE EIGHTH CLASS IS TIGHTER THAN ITS PREDECESSORS, AND ON PURPOSE. **  The landed classes
#: strip a new switch's binding BY NAME, so a later change to that switch's DEFAULT would be
#: invisible to the hatch -- it would certify a tree whose switch is live.  This class strips the
#: four statements the revision adds only in their EXACT default-off form, so moving any of them
#: keeps the row red.  *The first cut of this file used the landed by-name shape and its own
#: "moved default" control PASSED, which is what found the hole.*
NEW_STATEMENTS = {
    'NUPERT': "os.environ.get('NUPERT', '0') == '1'",
    'NUSHOFF': "os.environ.get('NUSHOFF', '0') == '1'",
    '_NU_NR': '1.0 / 6.0',
    'Wnu_of': 'None',                      # `Wnu_of = Wdot_of = None`, the switch-off binding
}
NEW_CONFIG_KEYS = ('NUPERT', 'NUSHOFF')
LANDED_CONFIG_KEYS = ('DNEFF', 'YHE', 'BVEL', 'MNU', 'FOURPI', 'PRIMNORM_env', 'NUFD')


def _inert_unit_factors(tree):
    """the sixth class's helper, verbatim in behaviour: `x = <...> if FOURPI else 1.0`"""
    out = set()
    for n in ast.walk(tree):
        if not isinstance(n, ast.Assign) or len(n.targets) != 1:
            continue
        t, v = n.targets[0], n.value
        if not (isinstance(t, ast.Name) and isinstance(v, ast.IfExp)):
            continue
        if not (isinstance(v.test, ast.Name) and v.test.id == 'FOURPI'):
            continue
        o = v.orelse
        if (isinstance(o, ast.Constant) and not isinstance(o.value, bool)
                and isinstance(o.value, (int, float)) and o.value == 1):
            out.add(t.id)
    return out


def make_strip(eighth=True):
    """the receipts' `_Strip`, with the eighth class switchable so ② can be measured"""

    class _Strip(ast.NodeTransformer):
        NAMES = {'_dneff', 'DNEFF', '_yhe', 'YHE', 'MNU', 'ONU', 'BVEL', 'I_DB_F', 'I_TBF'}
        UNIT = set()

        def visit_BinOp(self, node):
            r = node.right
            # --- EIGHTH CLASS (a): a `* _nush(...)` factor is exactly 1.0 unset, so the whole
            #     product collapses to its landed left operand.  Scoped to a CALL of that one name,
            #     so a multiplication by anything else is untouched.
            if (eighth and isinstance(node.op, ast.Mult) and isinstance(r, ast.Call)
                    and isinstance(r.func, ast.Name) and r.func.id == '_nush'):
                return self.visit(node.left)
            if (isinstance(node.op, (ast.Mult, ast.Div)) and isinstance(r, ast.Name)
                    and r.id in self.UNIT):
                return self.visit(node.left)
            if (isinstance(node.op, (ast.Add, ast.Sub)) and isinstance(r, ast.IfExp)
                    and isinstance(r.test, ast.Name) and r.test.id == 'BVEL'
                    and isinstance(r.orelse, ast.Constant) and r.orelse.value == 0):
                return self.visit(node.left)
            self.generic_visit(node)
            if isinstance(node.op, ast.Sub) and isinstance(node.right, ast.Name) \
                    and node.right.id == 'ONU':
                return node.left
            return node

        def visit_IfExp(self, node):
            self.generic_visit(node)
            if isinstance(node.test, ast.Name) and node.test.id == 'BVEL':
                return node.orelse
            return node

        def visit_Expr(self, node):
            if "id='MNU'" in ast.dump(node) and "id='print'" in ast.dump(node):
                return None
            self.generic_visit(node)
            return node

        def visit_Call(self, node):
            self.generic_visit(node)
            f = node.func
            if (isinstance(f, ast.Attribute) and f.attr == 'savez' and node.args
                    and isinstance(node.args[0], ast.Name) and node.args[0].id == '_POLS'):
                node.keywords = [k for k in node.keywords if k.arg != 'config']
            return node

        # --- EIGHTH CLASS (b): the one function the switch introduces, whose unset body is
        #     `return 1.0`.  Scoped to that name.
        def visit_FunctionDef(self, node):
            if eighth and node.name == '_nush':
                return None
            self.generic_visit(node)
            return node

        def visit_Assign(self, node):
            t = node.targets[0]
            if isinstance(t, ast.Name) and t.id in self.NAMES:
                return None
            # --- EIGHTH CLASS (d): the four statements the switch adds, each matched on its EXACT
            #     value expression, so a moved default or a moved marker keeps the row red.
            if (eighth and isinstance(t, ast.Name) and t.id in NEW_STATEMENTS
                    and ast.dump(node.value)
                    == ast.dump(ast.parse(NEW_STATEMENTS[t.id], mode='eval').body)):
                return None
            v = node.value
            if isinstance(v, ast.IfExp) and isinstance(v.test, ast.Name) and v.test.id == 'BVEL':
                return None
            self.generic_visit(node)
            return node

        def visit_Assert(self, node):
            if "id='BVEL'" in ast.dump(node.test):
                return None
            return node

        def visit_If(self, node):
            s = ast.dump(node.test)
            if "id='DNEFF'" in s or "id='YHE'" in s:
                return None
            if isinstance(node.test, ast.Name) and node.test.id == 'NUFD':
                return None
            if isinstance(node.test, ast.Name) and node.test.id == '_NU_ON':
                if not node.orelse:
                    return None
                return [self.visit(n) for n in node.orelse]
            # --- EIGHTH CLASS (c): `if NUPERT: <new> else: <landed>` reduces to its landed `else`;
            #     `if NUPERT: <new>` with no `else` goes.  The same shape the seventh class takes.
            if eighth and isinstance(node.test, ast.Name) and node.test.id == 'NUPERT':
                if not node.orelse:
                    return None
                out = []
                for n in node.orelse:
                    r = self.visit(n)
                    if r is None:
                        continue
                    out.extend(r if isinstance(r, list) else [r])
                return out
            if isinstance(node.test, ast.Name) and node.test.id == 'BVEL' and not node.orelse:
                return None
            if (isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not)
                    and isinstance(node.test.operand, ast.Name)
                    and node.test.operand.id == 'BVEL' and not node.orelse):
                self.generic_visit(node)
                return node.body
            self.generic_visit(node)
            return node

        def visit_Dict(self, node):
            self.generic_visit(node)
            drop = LANDED_CONFIG_KEYS + (NEW_CONFIG_KEYS if eighth else ())
            keep = [(k, v) for k, v in zip(node.keys, node.values)
                    if not (isinstance(k, ast.Constant) and k.value in drop)]
            node.keys = [k for k, _ in keep]
            node.values = [v for _, v in keep]
            return node

    return _Strip


def reduces(src, blob_src, eighth=True):
    """does `src`, stripped, equal the banked tree?"""
    tr = ast.parse(src)
    S = make_strip(eighth)
    s = S()
    s.UNIT = _inert_unit_factors(tr)
    extra = {'NUFD', '_NU_ON', '_MNU_EARLY'}
    s.NAMES = S.NAMES | {'FOURPI'} | s.UNIT | extra
    return ast.dump(ast.parse(blob_src)) == ast.dump(s.visit(tr))


def main():
    print(__doc__)
    print('=' * 100)
    cfg = json.loads(str(__import__('numpy').atleast_1d(
        __import__('numpy').load(ARMNPZ, allow_pickle=True)['config'])[0]))
    bL = cfg['instrument_blob']
    blob = subprocess.run(['git', 'cat-file', '-p', bL], cwd=ROOT,
                          capture_output=True).stdout.decode()
    if not blob:
        raise SystemExit('  ⛔ the banked blob %s is not in this object store' % bL[:12])
    cur = io.open(INST, encoding='utf-8').read()
    print('  banked blob %s (%d lines);  working tree %d lines'
          % (bL[:12], blob.count('\n'), cur.count('\n')))

    rec = {'blob': bL}
    rec['fixed_point'] = bool(reduces(cur, blob, eighth=True))
    rec['floor'] = bool(reduces(cur, blob, eighth=False))
    print('\n  ① THE FIXED POINT -- the eighth class reduces the tree to the banked blob: %s'
          % ('YES' if rec['fixed_point'] else '** NO **'))
    print('  ② THE FLOOR -- the seven landed classes ALONE leave it red: %s'
          % ('YES, so the eighth is doing the work' if not rec['floor']
             else '** NO -- the eighth class is a no-op riding on the others **'))

    # ③ six mutations of the LANDED code, each of which must stay red
    CONTROLS = [
        ('a moved landed constant',
         ('FNU, Z_REC = 0.4052, 1089.9', 'FNU, Z_REC = 0.4053, 1089.9')),
        ('a deleted landed line',
         ('OB = OMBH2 / (H0 / 100) ** 2\n', '')),
        ('a changed landed operand',
         ('OCDM = OM - OB - ONU', 'OCDM = OM - OB - OB')),
        ('the guard made live-when-off',
         ('        if NUPERT:\n            _w, _wd = float(Wnu_of(e)), float(Wdot_of(e))',
          '        if not NUPERT:\n            _w, _wd = float(Wnu_of(e)), float(Wdot_of(e))')),
        ('a moved LANDED default',
         ("GSRC = os.environ.get('GSRC', '0') == '1'",
          "GSRC = os.environ.get('GSRC', '1') == '1'")),
        ('⛭ a moved default of THIS revision\'s own switch -- the control that found the hole',
         ("NUPERT = os.environ.get('NUPERT', '0') == '1'",
          "NUPERT = os.environ.get('NUPERT', '1') == '1'")),
        ('⛭ a moved marker of THIS revision\'s own shear arm',
         ('_NU_NR = 1.0 / 6.0', '_NU_NR = 1.0 / 5.0')),
        ('an unguarded factor in place of the guarded one',
         ('sig = _NUFS * F[:, 0] / 2 * _nush(e)', 'sig = _NUFS * F[:, 0] / 2 * _other(e)')),
    ]
    rec['controls'] = {}
    print('\n  ③ THE CONTROLS -- a mutation of the LANDED code must keep the row red')
    for name, (a, b) in CONTROLS:
        if cur.count(a) < 1:
            raise SystemExit('  ⛔ control %r does not occur in the instrument' % name)
        mut = cur.replace(a, b, 1)
        try:
            red = not reduces(mut, blob, eighth=True)
        except SyntaxError:
            red = True
        rec['controls'][name] = bool(red)
        print('     %-50s %s' % (name, 'stays red' if red else '** PASSES, which it must not **'))

    ok = rec['fixed_point'] and not rec['floor'] and all(rec['controls'].values())
    rec['all_pass'] = bool(ok)
    print('\n  ⇒ %s' % ('the eighth class is measured on all three counts and is ready to route'
                        if ok else '** THE EIGHTH CLASS IS NOT MEASURED CLEAN -- do not route it **'))
    json.dump(rec, io.open(os.path.join(HERE, 'strip_class.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote strip_class.json')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
