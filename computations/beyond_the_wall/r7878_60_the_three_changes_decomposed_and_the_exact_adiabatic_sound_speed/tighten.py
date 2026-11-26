# -*- coding: utf-8 -*-
"""r7878+60 item ③ — THE TIGHTENING, MEASURED BEFORE IT IS ROUTED.

`r7876` found that the landed strip classes drop a new switch's binding BY NAME, so a later change
of that switch's DEFAULT to ON would be invisible to the AST escape hatch: it would certify a tree
whose switch is live.  `69` asked for the same exact-value matching this seat gave its eighth class
to be given to the **fifth** (`BVEL`) and **seventh** (`NUFD`) as well, and for the patch to be
routed rather than landed, because both receipts are shared.

⌗ *This revision also adds two switches of its own, `NUPARTS` and `NUCA`, so the eighth class's own
  exact-value map gains them in the same patch.  One patch, three parts.*

WHAT IS MEASURED, and the third is the one that shows the tightening DOES something:

    ① THE FIXED POINT -- with everything tightened, the working tree still reduces to the banked
       blob, so the hatch still certifies the instrument that produced the bank.
    ② THE FLOOR -- without this revision's two names in the map, the tree does NOT reduce, so the
       eighth class's extension is load-bearing and not decoration.
    ③ THE HOLE, BOTH WAYS -- for every switch whose binding the landed classes drop by name,
       moving its default is measured BEFORE the tightening (it must PASS, which is the hole) and
       AFTER it (it must be RED).  A tightening whose control is red both ways has not been shown
       to do anything.

    NODE=60 python3 tighten.py
"""
import ast
import io
import json
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_ROOT = os.path.dirname(os.path.dirname(_BTW))
INST = os.path.join(_BTW, 'ACOUSTIC_two_arm.py')
ARMNPZ = os.path.join(_BTW, 'spectra', 'cc66_r185_verify_cr_leafrec1.npz')

#: the eighth class as it is landed, plus the two this revision adds
EXACT_EIGHTH = {
    'NUPERT': "os.environ.get('NUPERT', '0') == '1'",
    'NUSHOFF': "os.environ.get('NUSHOFF', '0') == '1'",
    '_NU_NR': '1.0 / 6.0',
    'Wnu_of': 'None',
}
EXACT_R7878 = {
    'NUPARTS': "os.environ.get('NUPARTS', 'WCE')",
    'NUCA': "os.environ.get('NUCA', '0') == '1'",
}
#: ⛭ the tightening: four bindings the landed fifth and seventh classes drop BY NAME, each of which
#:   carries a DEFAULT that a later revision could move without the hatch noticing
EXACT_TIGHTEN = {
    'BVEL': "os.environ.get('BVEL', '0') == '1'",
    'NUFD': ("os.environ.get('NUFD', '0') == '1' "
             "and float(os.environ.get('MNU', '0.0')) != 0.0"),
    '_NU_ON': ("os.environ.get('NUFD', '0') == '1' "
               "and float(os.environ.get('MNU', '0.0')) != 0.0"),
    '_MNU_EARLY': "float(os.environ.get('MNU', '0.0'))",
}
BY_NAME_LANDED = {'_dneff', 'DNEFF', '_yhe', 'YHE', 'MNU', 'ONU', 'BVEL', 'I_DB_F', 'I_TBF'}
CONFIG_LANDED = ('DNEFF', 'YHE', 'BVEL', 'MNU', 'FOURPI', 'PRIMNORM_env', 'NUFD',
                 'NUPERT', 'NUSHOFF')
CONFIG_R7878 = ('NUPARTS', 'NUCA')


def _inert_unit_factors(tree):
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


def make_strip(r7878=True, tighten=True):
    """the receipts' `_Strip`, with this revision's two additions and the tightening switchable"""
    EXACT = dict(EXACT_EIGHTH)
    if r7878:
        EXACT.update(EXACT_R7878)
    if tighten:
        EXACT.update(EXACT_TIGHTEN)
    NAMES0 = set(BY_NAME_LANDED)
    EXTRA0 = {'NUFD', '_NU_ON', '_MNU_EARLY'}
    if tighten:
        NAMES0 -= {'BVEL'}
        EXTRA0 -= {'NUFD', '_NU_ON', '_MNU_EARLY'}
    DROP = CONFIG_LANDED + (CONFIG_R7878 if r7878 else ())

    class _Strip(ast.NodeTransformer):
        NAMES = NAMES0
        UNIT = set()

        def visit_BinOp(self, node):
            r = node.right
            if (isinstance(node.op, ast.Mult) and isinstance(r, ast.Call)
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

        def visit_FunctionDef(self, node):
            if node.name == '_nush':
                return None
            self.generic_visit(node)
            return node

        def visit_Assign(self, node):
            t = node.targets[0]
            if isinstance(t, ast.Name) and t.id in self.NAMES:
                return None
            if (isinstance(t, ast.Name) and t.id in EXACT
                    and ast.dump(node.value)
                    == ast.dump(ast.parse(EXACT[t.id], mode='eval').body)):
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
            if isinstance(node.test, ast.Name) and node.test.id == 'NUPERT':
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
            keep = [(k, v) for k, v in zip(node.keys, node.values)
                    if not (isinstance(k, ast.Constant) and k.value in DROP)]
            node.keys = [k for k, _ in keep]
            node.values = [v for _, v in keep]
            return node

    return _Strip, EXTRA0


def reduces(src, blob_src, r7878=True, tighten=True):
    tr = ast.parse(src)
    S, extra = make_strip(r7878, tighten)
    s = S()
    s.UNIT = _inert_unit_factors(tr)
    s.NAMES = S.NAMES | {'FOURPI'} | s.UNIT | extra
    return ast.dump(ast.parse(blob_src)) == ast.dump(s.visit(tr))


#: ⛭ the controls: each moves a DEFAULT, which is exactly what by-name stripping cannot see
DEFAULT_CONTROLS = [
    ("BVEL's default", ("BVEL = os.environ.get('BVEL', '0') == '1'",
                        "BVEL = os.environ.get('BVEL', '1') == '1'")),
    ("NUFD's default", ("NUFD = (os.environ.get('NUFD', '0') == '1'",
                        "NUFD = (os.environ.get('NUFD', '1') == '1'")),
    ("_NU_ON's default", ("_NU_ON = (os.environ.get('NUFD', '0') == '1'",
                          "_NU_ON = (os.environ.get('NUFD', '1') == '1'")),
    ("the early MNU default", ("_MNU_EARLY = float(os.environ.get('MNU', '0.0'))",
                               "_MNU_EARLY = float(os.environ.get('MNU', '0.1'))")),
    ("NUPARTS's default", ("NUPARTS = os.environ.get('NUPARTS', 'WCE')",
                           "NUPARTS = os.environ.get('NUPARTS', 'W')")),
    ("NUCA's default", ("NUCA = os.environ.get('NUCA', '0') == '1'",
                        "NUCA = os.environ.get('NUCA', '1') == '1'")),
]
#: and the landed controls, which must stay red either way
LANDED_CONTROLS = [
    ('a moved landed constant', ('FNU, Z_REC = 0.4052, 1089.9', 'FNU, Z_REC = 0.4053, 1089.9')),
    ('a deleted landed line', ('OB = OMBH2 / (H0 / 100) ** 2\n', '')),
    ('a changed landed operand', ('OCDM = OM - OB - ONU', 'OCDM = OM - OB - OB')),
]


def main():
    print(__doc__)
    print('=' * 100)
    import numpy as np
    cfg = json.loads(str(np.atleast_1d(np.load(ARMNPZ, allow_pickle=True)['config'])[0]))
    bL = cfg['instrument_blob']
    blob = subprocess.run(['git', 'cat-file', '-p', bL], cwd=_ROOT,
                          capture_output=True).stdout.decode()
    if not blob:
        raise SystemExit('  ⛔ the banked blob %s is not in this object store' % bL[:12])
    cur = io.open(INST, encoding='utf-8').read()
    print('  banked blob %s (%d lines);  working tree %d lines'
          % (bL[:12], blob.count('\n'), cur.count('\n')))

    rec = {'blob': bL}
    rec['fixed_point'] = bool(reduces(cur, blob, r7878=True, tighten=True))
    rec['floor_without_r7878'] = bool(reduces(cur, blob, r7878=False, tighten=True))
    print('\n  ① THE FIXED POINT -- tightened, the tree still reduces to the banked blob: %s'
          % ('YES' if rec['fixed_point'] else '** NO **'))
    print('  ② THE FLOOR -- without this revision\'s two names the tree does NOT reduce: %s'
          % ('YES, so the extension is load-bearing' if not rec['floor_without_r7878']
             else '** NO -- the two names are decoration **'))

    print('\n  ③ THE HOLE, BOTH WAYS -- a moved default must PASS before the tightening and be RED'
          ' after it')
    rec['controls'] = {}
    for name, (a, b) in DEFAULT_CONTROLS:
        if cur.count(a) != 1:
            raise SystemExit('  ⛔ control %r does not occur exactly once' % name)
        mut = cur.replace(a, b, 1)
        try:
            before = reduces(mut, blob, r7878=True, tighten=False)
        except SyntaxError:
            before = False
        try:
            after = reduces(mut, blob, r7878=True, tighten=True)
        except SyntaxError:
            after = False
        #: ⌗ this revision's own two are already exact in the eighth class, so their "before" is
        #:   already red -- that is the point of having written them that way, and it is reported
        #:   rather than dressed up as the tightening's doing
        own = name in ("NUPARTS's default", "NUCA's default")
        good = (not after) and (before or own)
        rec['controls'][name] = dict(passes_before=bool(before), red_after=bool(not after),
                                     this_revisions_own=own, good=bool(good))
        print('     %-24s before: %-9s after: %-9s %s'
              % (name, 'PASSES (the hole)' if before else 'red',
                 'RED' if not after else '** PASSES **',
                 '' if good else '  ** NOT SHOWN **'))

    print('\n  and the landed controls, which must stay red either way')
    rec['landed_controls'] = {}
    for name, (a, b) in LANDED_CONTROLS:
        mut = cur.replace(a, b, 1)
        try:
            red = not reduces(mut, blob, r7878=True, tighten=True)
        except SyntaxError:
            red = True
        rec['landed_controls'][name] = bool(red)
        print('     %-40s %s' % (name, 'stays red' if red else '** PASSES **'))

    ok = (rec['fixed_point'] and not rec['floor_without_r7878']
          and all(v['good'] for v in rec['controls'].values())
          and all(rec['landed_controls'].values()))
    rec['all_pass'] = bool(ok)
    print('\n  ⇒ %s' % ('the tightening is measured on all three counts and is ready to route'
                        if ok else '** NOT MEASURED CLEAN -- do not route it **'))
    json.dump(rec, io.open(os.path.join(_HERE, 'tighten.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote tighten.json')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
