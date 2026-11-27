# -*- coding: utf-8 -*-
"""r7884+60 — r7882's ADDITION TAUGHT TO THE EIGHTH STRIP CLASS, MEASURED BEFORE ROUTING.

⛔ **THIS IS A DEBT `r7882` INCURRED AND IT IS NAMED AS ONE.** `r7882` added the massive species'
own hierarchy behind four environment switches, and three SHARED receipts went red from that diff:

  ⓵ `P15_the_1p57_has_no_parameter_address_…py` — its `⓿⓿` arm compares this run's resolved
     snapshot against the bank's stored `config` **and the instrument's source hash**, where the
     hash is of the REDUCED tree.
  ⓶ `P15_the_fitted_comb_moves_nine_times_less_…py` — the same blob comparison.
  ⓷ `P15_the_free_streaming_knob_…py` — the switch CENSUS, which rolls every switch by name and
     asserted NINETY-FIVE. It now measures `99 switches used, 99 bound`.

⌗ **ALL THREE ARE `cc66`'s OR `70`'s, so the patch is ROUTED and none of them is edited** — the same
rule and the same shape as `r7878`'s own tightening, which `r7879` then applied.

⌗ **NOT RETYPED: `r7878`'s `tighten.py` IS the machinery**, imported. `reduces` is rebuilt here on a
SUBCLASS of its `_Strip` so the landed behaviour is inherited rather than copied.

⛭ **THE FIRST DRAFT OF THIS FILE WAS WRONG IN A WAY WORTH RECORDING.** It assumed the patch was the
four bindings, because the four bindings are what the CENSUS counts. The blob comparison is not a
census: it is an equality, and `r7882` added a module-level block, four functions, nine guarded
statements, two offsets, two aliases and a narrowed handover slice *as well as* the four bindings.
The residual diff was read, not guessed, and the patch is the NINE mechanisms below. *A gate that
reads a hash tells you the trees differ and nothing about where — so the difference was printed.*

THE PATCH, each part named by what in the diff forces it:

    Ⓔ the four bindings, matched on their EXACT VALUES (never by name — see ③)
    Ⓚ the four keys dropped from the recorded `config`, which the banked blob has none of
    Ⓕ the four `_nuhier_*` functions dropped whole, as the landed class drops `_nush`
    Ⓘ a statement guarded by `if NUHIER:` dropped whole, BOTH BRANCHES — the module-level block's
      `else` binds the quadrature to `None`, which the landed file does not do either
    Ⓧ `… if NUHIER else X` reduced to `X`, as the landed class does for `BVEL`
    Ⓞ `± _NH` dropped from an offset, as the landed class drops `- ONU`
    Ⓝ `_NH`, `I_PN`, `_PSI` dropped by name: each is wholly this revision's
    Ⓐ the two ALIASES `I_PNH → NVH` and `_dnp → dn`, each a new name for a quantity the landed
      file already had, renamed back — Ⓞ and Ⓧ then leave `NVH = NVH` and `dn = dn`, and a
      self-assignment is dropped
    Ⓢ `yF[:, :yF.shape[1]]`, left by Ⓞ, is the whole of `yF`

WHAT IS MEASURED:
    ① THE FIXED POINT — with the patch, the working tree reduces to the banked blob again, so the
       hatch certifies the instrument that produced the bank.
    ①′ EACH HALF IS NECESSARY, FIRST HALF — Ⓔ and Ⓚ alone, in r7878's UNEXTENDED machinery, do
       NOT reduce. ⌗ *That is the patch this revision first wrote, kept as a callable: it is what
       shows parts Ⓕ–Ⓢ are load-bearing.*
    ② EACH HALF IS NECESSARY, SECOND HALF — parts Ⓕ–Ⓢ with Ⓔ OMITTED do not reduce either, which
       is what shows Ⓔ is load-bearing. ⛔ *These two are not the same measurement and neither
       implies the other, and they were the wrong way round in this file once: ①′ drops eight
       parts and keeps the bindings, ② keeps the eight and drops the bindings.*
    ③ THE HOLE, BOTH WAYS — for each of the four, moving its DEFAULT must PASS with the bindings
       taken BY NAME (that is the hole `r7878` closed for the fifth and seventh classes) and be RED
       with Ⓔ. A control red both ways has shown nothing.

    NODE=60 python3 tighten_nuhier.py
"""
import ast
import io
import json
import os
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_ROOT = os.path.dirname(os.path.dirname(_BTW))
R7878 = os.path.join(_BTW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic'
                           '_sound_speed')
sys.path.insert(0, R7878)
import tighten as T                                                            # noqa: E402

#: Ⓔ r7882's four, each the instrument's OWN line -- gate ⓪ reads them at source
EXACT_R7882 = {
    'NUHIER': "os.environ.get('NUHIER', '0') == '1'",
    'NQ': "int(os.environ.get('NQ', '12'))",
    'LMAXNU': "int(os.environ.get('LMAXNU', '12'))",
    'QMAXNU': "float(os.environ.get('QMAXNU', '20'))",
}
#: Ⓚ the same four as recorded-config keys
CONFIG_R7882 = tuple(sorted(EXACT_R7882))
#: Ⓕ dropped whole
FUNCS_R7882 = {'_nuhier_moments', '_nuhier_rhs', '_nuhier_sigma', '_nuhier_seed'}
#: Ⓝ wholly this revision's
NAMES_R7882 = {'_NH', 'I_PN', '_PSI'}
#: Ⓐ new name -> the landed name for the same quantity
ALIAS_R7882 = {'I_PNH': 'NVH', '_dnp': 'dn'}
#: ⛭ each control moves a DEFAULT, which is exactly what by-name stripping cannot see
CONTROLS = [
    ("NUHIER's default", ("NUHIER = os.environ.get('NUHIER', '0') == '1'",
                          "NUHIER = os.environ.get('NUHIER', '1') == '1'")),
    ("NQ's default", ("NQ = int(os.environ.get('NQ', '12'))",
                      "NQ = int(os.environ.get('NQ', '24'))")),
    ("LMAXNU's default", ("LMAXNU = int(os.environ.get('LMAXNU', '12'))",
                          "LMAXNU = int(os.environ.get('LMAXNU', '18'))")),
    ("QMAXNU's default", ("QMAXNU = float(os.environ.get('QMAXNU', '20'))",
                          "QMAXNU = float(os.environ.get('QMAXNU', '15'))")),
]
FAILS = []


def make_strip_r7882(how):
    """r7878's `_Strip` plus the nine parts.  `how` places Ⓔ: 'exact', 'byname' or 'off'

    'off' keeps Ⓚ and parts Ⓕ…Ⓢ and leaves the four bindings standing, which is gate ②'s floor.
    """
    _cfg0 = T.CONFIG_R7878
    try:
        T.CONFIG_R7878 = tuple(_cfg0) + CONFIG_R7882              #: Ⓚ, in every mode
        base, extra = T.make_strip(True, True)
    finally:
        T.CONFIG_R7878 = _cfg0

    class _Strip82(base):
        NAMES = set(base.NAMES) | NAMES_R7882 | (set(EXACT_R7882) if how == 'byname' else set())
        EXACT82 = dict(EXACT_R7882) if how == 'exact' else {}

        def visit_Name(self, node):                                           #: Ⓐ
            if node.id in ALIAS_R7882:
                return ast.copy_location(ast.Name(id=ALIAS_R7882[node.id], ctx=node.ctx), node)
            return node

        def visit_FunctionDef(self, node):                                    #: Ⓕ
            if node.name in FUNCS_R7882:
                return None
            return super().visit_FunctionDef(node)

        def visit_If(self, node):                                             #: Ⓘ
            if isinstance(node.test, ast.Name) and node.test.id == 'NUHIER':
                return None
            return super().visit_If(node)

        def visit_IfExp(self, node):                                          #: Ⓧ
            if isinstance(node.test, ast.Name) and node.test.id == 'NUHIER':
                return self.visit(node.orelse)
            return super().visit_IfExp(node)

        def visit_BinOp(self, node):                                          #: Ⓞ
            if (isinstance(node.op, (ast.Add, ast.Sub)) and isinstance(node.right, ast.Name)
                    and node.right.id == '_NH'):
                return self.visit(node.left)
            return super().visit_BinOp(node)

        def visit_Subscript(self, node):                                      #: Ⓢ
            self.generic_visit(node)
            s = node.slice
            if (isinstance(node.value, ast.Name) and isinstance(s, ast.Tuple) and len(s.elts) == 2
                    and all(isinstance(e, ast.Slice) for e in s.elts)
                    and s.elts[0].lower is s.elts[0].upper is s.elts[0].step is None
                    and s.elts[1].lower is None and isinstance(s.elts[1].upper, ast.Subscript)
                    and isinstance(s.elts[1].upper.value, ast.Attribute)
                    and s.elts[1].upper.value.attr == 'shape'
                    and isinstance(s.elts[1].upper.value.value, ast.Name)
                    and s.elts[1].upper.value.value.id == node.value.id
                    and isinstance(s.elts[1].upper.slice, ast.Constant)
                    and s.elts[1].upper.slice.value == 1):
                return ast.copy_location(ast.Name(id=node.value.id, ctx=node.ctx), node)
            return node

        def visit_Assign(self, node):                                         #: Ⓔ, then Ⓐ's tail
            t = node.targets[0]
            if (isinstance(t, ast.Name) and t.id in self.EXACT82
                    and ast.dump(node.value)
                    == ast.dump(ast.parse(self.EXACT82[t.id], mode='eval').body)):
                return None
            out = super().visit_Assign(node)
            if out is None:
                return None
            tt = out.targets[0]
            if (len(out.targets) == 1 and isinstance(tt, ast.Name)
                    and isinstance(out.value, ast.Name) and tt.id == out.value.id):
                return None
            return out

    return _Strip82, extra


def reduces(src, blob_src, how):
    """`r7878.reduces`, rebuilt on the subclass -- same assembly of `UNIT`, `FOURPI` and `extra`"""
    tr = ast.parse(src)
    S, extra = make_strip_r7882(how)
    s = S()
    s.UNIT = T._inert_unit_factors(tr)
    s.NAMES = S.NAMES | {'FOURPI'} | s.UNIT | extra
    return ast.dump(ast.parse(blob_src)) == ast.dump(s.visit(tr))


def reduces_bindings_only(src, blob_src):
    """`r7878`'s UNEXTENDED machinery with `Ⓔ` and `Ⓚ` alone -- the patch this revision FIRST wrote

    ⛭ *Kept as a callable rather than described, because the receipt asserts it: the four bindings
    on their own do NOT reduce, and that is the error, measured.*
    """
    e0, c0 = T.EXACT_R7878, T.CONFIG_R7878
    try:
        T.EXACT_R7878 = dict(e0)
        T.EXACT_R7878.update(EXACT_R7882)
        T.CONFIG_R7878 = tuple(c0) + CONFIG_R7882
        return T.reduces(src, blob_src, True, True)
    finally:
        T.EXACT_R7878, T.CONFIG_R7878 = e0, c0


def gate(name, ok, got=None):
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name)
    return ok


def main():
    print(__doc__)
    print('=' * 104)
    cfg = json.loads(str(np.atleast_1d(np.load(T.ARMNPZ, allow_pickle=True)['config'])[0]))
    bL = cfg['instrument_blob']
    blob = subprocess.run(['git', 'cat-file', '-p', bL], cwd=_ROOT,
                          capture_output=True).stdout.decode()
    if not blob:
        raise SystemExit('  ⛔ the banked blob %s is not in this object store' % bL[:12])
    cur = io.open(T.INST, encoding='utf-8').read()
    print('  banked blob %s (%d lines);  working tree %d lines'
          % (bL[:12], blob.count('\n'), cur.count('\n')))
    rec = {'blob': bL, 'bindings': EXACT_R7882, 'config_keys': list(CONFIG_R7882),
           'funcs': sorted(FUNCS_R7882), 'by_name': sorted(NAMES_R7882), 'aliases': ALIAS_R7882}

    gate('⓪ the four bindings are the instrument\'s OWN lines, read at source not remembered',
         all(('%s = %s' % (k, v)) in cur for k, v in EXACT_R7882.items()),
         '%d of 4 verbatim' % sum(1 for k, v in EXACT_R7882.items()
                                  if ('%s = %s' % (k, v)) in cur))

    rec['fixed_point'] = bool(reduces(cur, blob, 'exact'))
    gate('① THE FIXED POINT -- with the patch the tree reduces to the banked blob again, so '
         'the hatch certifies the instrument that produced the bank', rec['fixed_point'])

    rec['bindings_only_in_r7878_machinery'] = bool(reduces_bindings_only(cur, blob))
    gate('\u2460\u2032 EACH HALF IS NECESSARY, FIRST HALF -- the four bindings in r7878\'s '
         'unextended machinery do NOT reduce, so parts \u24bb-\u24c8 are load-bearing (a census '
         'is a count where the blob comparison is an equality)',
         not rec['bindings_only_in_r7878_machinery'],
         'reduces anyway' if rec['bindings_only_in_r7878_machinery']
         else 'does not reduce -- this is the error this revision made and corrected')

    rec['floor_bindings_only'] = bool(reduces(cur, blob, 'off'))
    gate('② EACH HALF IS NECESSARY, SECOND HALF -- parts Ⓕ-Ⓢ with Ⓔ OMITTED do not reduce '
         'either, so Ⓔ is load-bearing', not rec['floor_bindings_only'],
         'reduces anyway' if rec['floor_bindings_only'] else 'does not reduce, as required')

    print('\n  ③ THE HOLE, BOTH WAYS -- a moved DEFAULT must PASS by-name and be RED on exact '
          'value')
    rec['controls'] = {}
    for name, (a, b) in CONTROLS:
        if cur.count(a) != 1:
            raise SystemExit('  ⛔ control %r does not occur exactly once' % name)
        mut = cur.replace(a, b, 1)
        before = bool(reduces(mut, blob, 'byname'))
        after = bool(reduces(mut, blob, 'exact'))
        rec['controls'][name] = {'byname_passes': before, 'exact_red': not after}
        gate('   %-20s by-name PASSES (the hole) and exact value is RED (closed)' % name,
             before and not after, 'by-name %s, exact %s'
             % ('passes' if before else 'RED', 'RED' if not after else 'passes'))

    json.dump(rec, io.open(os.path.join(_HERE, 'tighten_nuhier.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('\n' + '=' * 104)
    print('  %d gate(s) failed' % len(FAILS))
    for f in FAILS:
        print('    FAILED: %s' % f)
    print('=' * 104)
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
