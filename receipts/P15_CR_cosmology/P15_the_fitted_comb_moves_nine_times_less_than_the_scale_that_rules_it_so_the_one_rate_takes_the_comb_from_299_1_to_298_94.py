#!/usr/bin/env python3
r"""`r7779` ** THE PROJECTION'S DISTANCE ON THE RATE THE UNIVERSE HAS MOVES `l_A` BY `-0.4984 %` AND
THIS RECEIPT'S THREE-PEAK SUB-GRID COMB BY `-0.0549 %` -- NINE TIMES LESS. **

⛔⛔⛭ ** CORRECTION, `r7783+cc66.9`, AT THE TOP BECAUSE THIS RECEIPT'S OWN TITLE IS WRONG: THE FIGURE
IS `298.5`, NOT THE `298.94` THIS FILE'S NAME AND ITS OLD GATE `⑧` CARRIED. **  `P15`'s printed comb
and its printed phase intercept are the ** FOUR-PEAK ** fit through the matched seven-window locator.
⌗ *The four-peak and three-peak values of both quantities, on both arms, are measured and pinned in
the receipt named below; they are deliberately NOT restated here, because a figure printed in a
receipt that does not compute it is what `check_marker_transposition` exists to catch -- and writing
them into this docstring is how that gate caught me.*  ** What `⑥` below measures is a
THREE-PEAK SUB-GRID comb on a DIFFERENT locator: no lensing ratio, no binning, no seven-window
average.  That measurement stands.  What was wrong was applying ITS move to the paper's four-peak
number -- one estimator's move on another estimator's figure. **  Read off the one-rate arm through
the paper's own locator and fit, the comb is `298.527`, i.e. `298.5`.  *The figure and its provenance
are in
`receipts/P15_CR_cosmology/P15_the_sections_opening_figures_on_the_one_rate_and_the_published_comb_is_298_5_not_298_94.py`;
`⑧` here now asserts this receipt's SCOPE LIMIT instead of a figure it cannot reach.*
  ⌗ *The file name still says `298_94`.  Renaming it would move the `\rcpt{}` key the paper cites, so
  the rename is routed to `69` rather than taken here.*

Built `r7779+cc66.3`, discharging order `(2)` of the chat seat's `r7779`: *"Mint a receipt for item 2
(the comb's move against the ruler's, same point, LEAFGEOM the only difference) so 298.94 can be
quoted."*

===================================================================================================
** COMPUTES: ** `l_A`, `D_M`, `r_s` and the fitted acoustic comb of the crossing arm at the
   distances' point `(CRH0 68.60, CROM 0.2973)`, read from two banked `ACOUSTIC_two_arm.py` runs that
   differ in `LEAFGEOM` -- the projection distance on the stacking rate (`LEAFGEOM` unset) against the
   leaf rate (`LEAFGEOM=1`, radiation included).  The comb is fitted by the SAME least-squares
   procedure `P15` runs on the sky, lifted from the comb receipt rather than reimplemented, on the
   first three peaks, with a PARABOLIC sub-grid refinement of each peak's position.  Nothing is
   fitted to data and no likelihood is formed.  The published `299.1` is parsed out of
   `corpus/CR_cosmology.tex` and the derived `298.94` is `299.1` times the MEASURED comb ratio.
===================================================================================================

⛔ ** THE ORDER SAYS "LEAFGEOM THE ONLY DIFFERENCE", AND IN THE BANK IT IS NOT -- SAID BEFORE ANY
NUMBER. **  The two arms also carry different instrument blobs: the `LEAFGEOM` unset leg was produced
by `d8b4a62a0…` and the `LEAFGEOM=1` leg by `e5319ce49…`, which is the blob the working tree carries.
So the pair differs by instrument VERSION as well as by the switch, and a receipt that quoted the move
without settling that would be quoting a confound.  ** `(3)` settles it rather than assuming it: **
the whole executable difference between the blobs falls in four named classes, all inert under the
switches these runs recorded --

  `(a)` the `COMBRHO` plumbing: `_kbs = kb * COMBRHO if COMBRHO is not None else kb`, so `_kbs is kb`
        when the switch is unset, and `ks=_kbs` threaded into `_project`, where `ks is None` restores
        `ks = kb`.  Every `kb -> ks` substitution inside `_project` is the identity here.
  `(b)` the `COMBRHO`/`SRCINJ` mutual-exclusion `raise`, which cannot fire with `COMBRHO is None`.
  `(c)` the `'COMBRHO'` key added to the stored config dict -- metadata, not the spectrum.  *Both
        banks' own configs record what this is: the newer one stores `COMBRHO: null`.*
  `(d)` the `SRCFIELD` output machinery (`_SFLD`, `_SFLD_B` and two `if _SFLD:` blocks), off unless
        asked.

and `(3)` applies exactly those four reductions to the newer blob's AST and asserts the result is
** IDENTICAL ** to the older blob's.  *The test cannot be vacuous in the direction that matters: a
difference outside the four classes survives the reductions and shows up as an AST mismatch.*

⛭ ** WHY THE SUB-GRID REFINEMENT IS NOT A REFINEMENT BUT THE MEASUREMENT. **  The banks are on a
`dl = 2` grid, which quantises a peak position to an integer, and the comb fitted to the raw grid
maxima reads `297.000` on ** both ** arms.  *Read that way the answer would be "the comb does not
move at all", which is the grid speaking and not the spectrum.*  `(7)` asserts the refinement changes
the answer, so the row cannot be passed by a locator that has no resolution.

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that `298.94` is a better fit to the sky than `299.1`. **  The sky's `298.4` is nearer
   `298.94`; no significance is computed and none is implied.
 * ** Not that the comb's insensitivity is derived. **  `(6)` measures the ratio `9.1`; the mechanism
   is not asserted here.
 * ** Not that the other arms move this way. **  Every number is at the distances' point, `LMAXL
   2000`, `KFAC 2.0`, `ZSTART 3e7`, `LEAFSCALES=1`, `LEAFREC=1`, as `(1)` asserts field by field.

⛔ ** A DEFECT OF MY OWN, RECORDED BECAUSE IT IS THE SECOND INSTANCE IN ONE REVISION. **  `(8)` went
through three formulations before it asserted its own claim.  The first parsed `comb ... $x$` loosely
and matched a DIFFERENT comb -- the paper's `comb at $49.4$` -- then took the smallest match, so it
computed `49.37`; the second required EVERY three-digit comb site in the paper to read `299.1`, which
is false and not the claim (the paper legitimately prints `144.0`, `297.0` and `485.5` in comb-adjacent
sentences).  ** Both failures are the same shape as item `(1)`'s `R2` in this same revision: a test
that asserts something STRONGER and INCIDENTAL instead of the claim. **  What `(8)` asserts now is the
claim: the `sec:scope` sentence parses UNIQUELY as `299.1` against the sky's `298.4`, and the derived
figure rounds to `298.94`.  *The rule I am taking from the pair: a pin names the sentence it pins, and
its failure condition must be the claim's negation and nothing wider.*

⛭ ** FAILABILITY, MEASURED. **  Scaling the `LEAFGEOM=1` arm's `Dl` argument of the locator by a
`1 + 3e-3` stretch in `ls` reddens `(6)`, `(7)` and `(8)` -- the comb ratio, the refinement row and
the published-figure pin -- while `(1)`-`(5)` hold, since they read the configs, the blobs and the
stored `l_A`/`D_M`/`r_s` and not the peak positions.  Measured in
`computations/beyond_the_wall/r7779_cc66_the_low_ell_depths_on_the_one_rate/failability_comb.py`.

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; a few seconds)
10 gates.  `(10)` pins every figure the INDEX row prints, each to half its last printed digit.
"""
import ast
import os
import re
import subprocess
import sys

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
STACK = 'cc66_cr_x_h686_L2000_leafrec1_distances'          # LEAFGEOM unset: stacking-rate distance
LEAF = 'r7749_leafgeom_nofit_L2000_cr'                     # LEAFGEOM=1:    leaf-rate distance
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f'             {witness}')


def arm(tag):
    p = os.path.join(SPEC, tag + '.npz')
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the bank has moved.')
    with np.load(p, allow_pickle=True) as z:
        return {k: z[k] for k in z.files}


def cfg(a):
    import json
    v = a['config']
    try:
        v = v.item()
    except Exception:
        pass
    return json.loads(str(v)) if isinstance(v, str) else dict(v)


def fit_comb(pk, n=3):
    """the comb fitter P15 runs on the sky: least squares on the first n peaks"""
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(pk[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def peaks(ls, Dl, n=4, refine=True):
    q = argrelextrema(Dl, np.greater, order=3)[0][:n]
    out = []
    for i in q:
        if refine and 0 < i < ls.size - 1:
            y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
            den = y0 - 2.0 * y1 + y2
            s = 0.5 * (y0 - y2) / den if den != 0 else 0.0
            out.append(float(ls[i] + s * (ls[i + 1] - ls[i])))
        else:
            out.append(float(ls[i]))
    return out


print('=' * 100)
print(__doc__)
print('=' * 100)

S, L = arm(STACK), arm(LEAF)
cS, cL = cfg(S), cfg(L)

# ---------------------------------------------------------------- (1) the intended difference
HELD = ('ARM', 'KFAC', 'LEAFREC', 'LEAFSCALES', 'LMAXL', 'NODRIVE', 'STACKPERT', 'VISLEAF', 'ZSTART')
differ = [k for k in HELD if cS.get(k) != cL.get(k)]
check("⛭ `r7779` ** ① THE PAIR'S INTENDED DIFFERENCE IS `LEAFGEOM` AND THE BANKS RECORD IT: `false` "
      "AGAINST `true`, WITH EVERY OTHER SWITCH HELD ** ⇒ *** `ARM=cr`, `KFAC 2.0`, `LEAFREC=1`, "
      "`LEAFSCALES=1`, `LMAXL 2000`, `STACKPERT` off, `VISLEAF 0`, `ZSTART 3e7` all equal, and the two "
      "manifests carry the same point `(CRH0 68.60, CROM 0.2973)`. *** ⌗ *`LEAFSCALES=1` on BOTH is what "
      "makes this the distance's move and not the scales': `r_s` is therefore identical, which `④` "
      "asserts rather than assumes*",
      cS.get('LEAFGEOM') is False and cL.get('LEAFGEOM') is True and not differ,
      f"LEAFGEOM {cS.get('LEAFGEOM')} vs {cL.get('LEAFGEOM')}; switches that differ besides it: "
      f"{differ if differ else 'none'}")

def _tree_is_bL_plus_dneff(bL):
    """⛭ `r7801+70`: the working tree may be LATER than the LEAFGEOM=1 leg's blob by exactly two additions,
    the `DNEFF` and `YHE` knobs (PO-24's N_eff and Y_He response banks): their assignments, their
    `if ... is not None` blocks and their config keys.  Unset, none of it runs, so the instrument that produced the leg is still the one on
    disk.  Strip exactly those and compare the ASTs; any other difference keeps this row red.

    ⛭ EXTENDED `r7807+cc66`: a THIRD addition, `POLSAVE`'s `config=_resolved_config()` keyword, added
    at `69`'s r7807 order so the polarisation bank is decidable.  It is the SAME CLASS as the already
    named `(c)` -- a metadata key written into a stored array, not a change to the spectrum -- and it
    is dropped here on that ground and no other.  `POLSAVE` is off unless asked, so on this pair's
    legs the call does not even execute.  ⛔ *It is dropped ONLY on a `savez` call, so an added
    `config=` anywhere that could reach a spectrum still keeps this row red.*"""
    import ast as _ast
    # --- sixth class -- r7857 (69), applied from 60's r7858 patch: `FOURPI` and the unit factors whose OWN
    #     assignment is `<something> if FOURPI else 1.0` (and no others) are inert unset; a `Mult`/`Div` by one
    #     of them collapses to its landed left operand.  60 measured it 8 of 8 against the banked blob: the five
    #     classes alone leave the head red, the sixth reduces it to the blob, and six controls (a moved landed
    #     constant, a deleted landed line, a changed landed operand, the guard made live-when-off, a moved
    #     landed default, an unguarded factor) all stay red.
    def _inert_unit_factors(tree):
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
    class _Strip(_ast.NodeTransformer):
        # the landed four classes, with BVEL added as the fifth -- r7851 (69), applied from 60's r7854 patch,
        #   measured by 60 on the LEAFGEOM=1 leg's blob: the landed blob is a fixed point, three real changes to
        #   the landed code and one to the landed branch of the guard keep the row red, and only the dead-unset
        #   BVEL branch passes
        NAMES = {'_dneff', 'DNEFF', '_yhe', 'YHE', 'MNU', 'ONU',
                 'BVEL', 'I_DB_F', 'I_TBF'}
        UNIT = set()

        # --- fifth class (a): a BVEL-guarded term added to or subtracted from a landed expression,
        #     whose `orelse` is Constant 0, collapses the whole BinOp back to the landed left operand.
        def visit_BinOp(self, node):
            # ⛔ the BVEL test is read BEFORE the children are visited, because `visit_IfExp` below
            #   would otherwise have already collapsed the guard to its `orelse` and left a `+ 0`.
            r = node.right
            if (isinstance(node.op, (_ast.Mult, _ast.Div)) and isinstance(r, _ast.Name)
                    and r.id in self.UNIT):
                return self.visit(node.left)
            if (isinstance(node.op, (_ast.Add, _ast.Sub)) and isinstance(r, _ast.IfExp)
                    and isinstance(r.test, _ast.Name) and r.test.id == 'BVEL'
                    and isinstance(r.orelse, _ast.Constant) and r.orelse.value == 0):
                return self.visit(node.left)
            self.generic_visit(node)
            if isinstance(node.op, _ast.Sub) and isinstance(node.right, _ast.Name) and node.right.id == 'ONU':
                return node.left
            return node

        # --- fifth class (b): any other IfExp on BVEL is the landed expression in its `orelse`.
        def visit_IfExp(self, node):
            self.generic_visit(node)
            if isinstance(node.test, _ast.Name) and node.test.id == 'BVEL':
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
            # ⛔ an assignment whose VALUE IS ITSELF a BVEL guard is dead unset -- and the test is on the
            #   whole value and not on its contents, so `out[...] = (-tb if BVEL else -tg) + ...`, whose
            #   value is a BinOp, is REDUCED to the landed line rather than dropped.  `tb` is a landed
            #   name elsewhere in this file, which is why this is not a name rule.
            v = node.value
            if (isinstance(v, _ast.IfExp) and isinstance(v.test, _ast.Name) and v.test.id == 'BVEL'):
                return None
            self.generic_visit(node)
            return node

        # --- fifth class (c): an added assertion that only states the layout invariant.
        #     ⛔ *Scoped to an assert whose test NAMES `BVEL`, and not to asserts generally: a blanket
        #     assert-drop would let a REMOVED assert through this ratchet, which is the opposite of
        #     what it is for.*
        def visit_Assert(self, node):
            if "id='BVEL'" in _ast.dump(node.test):
                return None
            return node

        def visit_If(self, node):
            s = _ast.dump(node.test)
            if "id='DNEFF'" in s or "id='YHE'" in s:
                return None
            # --- fifth class (d): `if BVEL:` is dead unset, so it goes;
            #     `if not BVEL:` wraps a landed statement, so the wrapper goes and the body stays.
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
    try:
        old = subprocess.run(['git', 'cat-file', '-p', bL], cwd=ROOT, capture_output=True).stdout.decode()
        new = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')).read()
        if not old:
            return False
        _tr = _ast.parse(new)
        _s = _Strip()
        _s.UNIT = _inert_unit_factors(_tr)
        _s.NAMES = _Strip.NAMES | {'FOURPI'} | _s.UNIT
        return _ast.dump(_ast.parse(old)) == _ast.dump(_s.visit(_tr))
    except (OSError, SyntaxError):
        return False

# ---------------------------------------------------------------- (2) but the blobs differ
bS, bL = cS.get('instrument_blob'), cL.get('instrument_blob')
cur = subprocess.run(['git', 'hash-object', 'computations/beyond_the_wall/ACOUSTIC_two_arm.py'],
                     cwd=ROOT, capture_output=True, text=True).stdout.strip()
check("⛭⛔⛭ `r7779` ** ② AND THE ORDER'S \"LEAFGEOM THE ONLY DIFFERENCE\" IS NOT TRUE OF THE BANK: THE "
      "TWO LEGS CARRY DIFFERENT INSTRUMENT BLOBS ** ⇒ *** `LEAFGEOM` unset was produced by `d8b4a62a0…`, "
      "`LEAFGEOM=1` by `e5319ce49…`, and the working tree carries the LATTER. ** So the pair is a "
      "confound until `③` disposes of it, and this row exists so that no number below can be read as "
      "resting on an assumption. ** *** ⌗ *The same shape of confound as the low-`ℓ` pair in item `①` of "
      "this revision, found the same way -- by reading the configs rather than the file names*",
      bS is not None and bL is not None and bS != bL and (cur == bL or _tree_is_bL_plus_dneff(bL)),
      f"LEAFGEOM-unset blob {bS}; LEAFGEOM=1 blob {bL}; working tree {cur}"
      + ("" if cur == bL else " (differs from it only by r7801+70's DNEFF and YHE blocks and their config"
                              " keys, inert unset, and r7807+cc66's POLSAVE `config=` keyword, the same"
                              " metadata class and off unless asked)"))

# ---------------------------------------------------------------- (3) and the confound is inert
def _blob(sha):
    return subprocess.run(['git', 'cat-file', '-p', sha], cwd=ROOT, capture_output=True).stdout.decode()


class Reduce(ast.NodeTransformer):
    """the four named classes, and nothing else: reduce the newer blob to its COMBRHO-unset,
    SRCFIELD-unset form.  Anything outside them survives and shows up as an AST mismatch."""

    DROP_NAMES = {'_CRHO', 'COMBRHO', '_SFLD', '_SFLD_B', '_kbs'}

    def visit_Assign(self, node):                                           # (a) (d)
        t = node.targets[0]
        if isinstance(t, ast.Name) and t.id in self.DROP_NAMES:
            return None
        self.generic_visit(node)
        return node

    def visit_If(self, node):
        src = ast.dump(node.test)
        if "'_SFLD'" in src or '"_SFLD"' in src:                            # (d) output-only blocks
            return None
        if "'COMBRHO'" in src and 'SRCINJ' in src:                          # (b) the refusal
            return None
        if "id='ks'" in src and 'None' in src:                              # (a) ks is None -> ks = kb
            return None
        self.generic_visit(node)
        return node

    def visit_Dict(self, node):                                             # (c) the stored key
        self.generic_visit(node)
        keep = [(k, v) for k, v in zip(node.keys, node.values)
                if not (isinstance(k, ast.Constant) and k.value == 'COMBRHO')]
        node.keys = [k for k, _ in keep]
        node.values = [v for _, v in keep]
        return node

    def visit_Name(self, node):                                             # (a) ks is kb here
        if node.id in ('ks', '_kbs'):
            return ast.copy_location(ast.Name(id='kb', ctx=node.ctx), node)
        return node

    def visit_FunctionDef(self, node):                                      # (a) the threaded arg
        self.generic_visit(node)
        if node.name == '_project':
            drop = [i for i, a in enumerate(node.args.args) if a.arg == 'ks']
            if drop:
                node.args.args = [a for a in node.args.args if a.arg != 'ks']
                node.args.defaults = node.args.defaults[:-len(drop)] or []
        return node

    def visit_Call(self, node):                                             # (a) the keyword at the call
        self.generic_visit(node)
        node.keywords = [k for k in node.keywords if k.arg != 'ks']
        return node


try:
    old = ast.dump(ast.parse(_blob(bS)))
    red = Reduce().visit(ast.parse(_blob(bL)))
    ast.fix_missing_locations(red)
    new_reduced = ast.dump(red)
    inert = old == new_reduced
    why = 'identical' if inert else 'differ after the four reductions'
except Exception as exc:                                                    # a missing blob in a
    inert, why = False, f'{type(exc).__name__}: {exc}'                      # shallow clone says so
check("⛭⛔⛭ `r7779` ** ③ AND THE CONFOUND IS **INERT**: REDUCE THE NEWER BLOB BY THE FOUR NAMED CLASSES "
      "AND ITS AST IS **IDENTICAL** TO THE OLDER BLOB'S ** ⇒ *** so with `COMBRHO` and `SRCFIELD` unset "
      "the newer instrument IS the older program, not merely one that behaves like it, and the pair is "
      "`LEAFGEOM`-only after all. ** The four classes are `(a)` the `COMBRHO` plumbing, where `_kbs is "
      "kb`, `(b)` its mutual-exclusion `raise`, `(c)` the `'COMBRHO'` config key, `(d)` the `SRCFIELD` "
      "output blocks. ** *** ⌗ *A difference OUTSIDE the four survives the reductions and reddens this "
      "row, which is why the test is not a licence to assume what it checks*",
      inert, f'older blob AST vs reduced newer blob AST: {why}')

# ---------------------------------------------------------------- (4) the ruler's numerator is held
rsS, rsL = float(S['r_s']), float(L['r_s'])
check("⛭ `r7779` ** ④ `r_s` IS **IDENTICAL** ACROSS THE PAIR, SO WHAT MOVES IS THE DISTANCE AND NOTHING "
      "ELSE ** ⇒ *`LEAFSCALES=1` on both legs puts the plasma's scales on the leaf rate in both, so the "
      "sound horizon is the same number to the bit; `LEAFGEOM` moves only the length the kernel takes*",
      rsS == rsL, f'r_s = {rsS:.6f} Mpc on both legs (difference exactly {rsL - rsS:.1e})')

# ---------------------------------------------------------------- (5) l_A moves WITH its distance
dmS, dmL = float(S['D_M']), float(L['D_M'])
laS, laL = float(S['l_A']), float(L['l_A'])
mv_dm, mv_la = dmL / dmS - 1.0, laL / laS - 1.0
check("⛭ `r7779` ** ⑤ `l_A` MOVES **EXACTLY WITH** ITS DISTANCE: `-0.4984 %` AGAINST `-0.4984 %`, "
      "`D_M` `14011.457 -> 13941.629` Mpc ** ⇒ *** `l_A = π D_M / r_s` with `r_s` held by `④`, so this "
      "row is a consistency check on the bank rather than a discovery -- and it is the row that fixes "
      "the SCALE the next two are measured against. *** ⌗ *The licence is absolute in units of the "
      "move itself, not relative: both quantities are far from zero, but their DIFFERENCE is not*",
      abs(mv_la - mv_dm) < 1e-6 * abs(mv_dm) + 1e-9,
      f'D_M {dmS:.4f} -> {dmL:.4f} ({100*mv_dm:+.4f}%); l_A {laS:.4f} -> {laL:.4f} '
      f'({100*mv_la:+.4f}%); |difference| {abs(mv_la-mv_dm):.3e}')

# ---------------------------------------------------------------- (6) the comb does NOT follow it
PS = peaks(np.asarray(S['ls'], float), np.asarray(S['Dl'], float))
PL = peaks(np.asarray(L['ls'], float), np.asarray(L['Dl'], float))
cbS, cbL = fit_comb(PS)[0], fit_comb(PL)[0]
mv_cb = cbL / cbS - 1.0
ratio = abs(mv_la / mv_cb)
check("⛭⛭⛭ `r7779` ** ⑥ BUT THE FITTED COMB MOVES **NINE TIMES LESS** THAN THE SCALE THAT RULES IT: "
      "`-0.0549 %` AGAINST `-0.4984 %`, `296.904 -> 296.741` ** ⇒ *** so the published comb does NOT "
      "follow `l_A`, and a reader who scaled `299.1` by the distance's half per cent would print `297.6` "
      "where the spectrum gives `298.94`. ** The quantity the paper quotes is the one FITTED TO THE "
      "PEAKS by the sky's own procedure, and the peaks are held in place by the acoustic physics the two "
      "legs share. ** *** ⌗ *The ratio is `9.1`, measured; no mechanism is asserted for it here*",
      mv_cb < 0 and 8.0 < ratio < 11.0 and abs(ratio - 9.07) < 0.005
      and abs(100 * mv_cb + 0.0549) < 0.00005 and abs(100 * mv_la + 0.4984) < 0.00005,
      f'comb {cbS:.4f} -> {cbL:.4f} ({100*mv_cb:+.4f}%) against l_A {100*mv_la:+.4f}%; '
      f'ratio {ratio:.2f}; peaks {[round(p,2) for p in PS[:3]]} -> {[round(p,2) for p in PL[:3]]}')

# ---------------------------------------------------------------- (7) and the grid would hide it
gS = fit_comb(peaks(np.asarray(S['ls'], float), np.asarray(S['Dl'], float), refine=False))[0]
gL = fit_comb(peaks(np.asarray(L['ls'], float), np.asarray(L['Dl'], float), refine=False))[0]
check("⛭⛔⛭ `r7779` ** ⑦ AND ON THE RAW `dl = 2` GRID THE ANSWER WOULD BE \"IT DOES NOT MOVE AT ALL\" -- "
      "`297.000` ON **BOTH** LEGS ** ⇒ *** the grid quantises a peak to an integer, so the unrefined "
      "locator has no resolution at the size of this move. ** This row asserts that the parabolic "
      "refinement CHANGED the answer, so `⑥` cannot be passed by a locator that cannot see it. ** *** "
      "⌗ *This is the row that would have caught my own first reading of this pair, which came off the "
      "grid*",
      gS == gL and cbS != cbL,
      f'unrefined comb {gS:.3f} on both legs; refined {cbS:.4f} vs {cbL:.4f}, '
      f'a refinement of {abs(cbS-gS):.4f} and {abs(cbL-gL):.4f} multipoles')

# ---------------------------------------------------------------- (8) the scope limit, CORRECTED
# ⛔ `r7783+cc66.9`: this gate USED to compute `299.1 x (1 + the move of ⑥)` and pin `298.94`.  That
#   was wrong -- `⑥`'s estimator is not the paper's -- and the paper now carries the wrong figure at
#   three sites on this receipt's authority.  The gate now asserts the SCOPE LIMIT that was missing:
#   that this receipt's comb is a three-peak sub-grid fit and so CANNOT supply the paper's figure.
tex = open(TEX, encoding='utf-8').read()
sent = re.findall(r"returns a comb of \$(\d+\.\d)\$ against the sky's \$(\d+\.\d)\$", tex)
sites = sorted({float(v) for v in re.findall(r'comb[^.$]{0,70}\$(\d{3}\.\d)\$', tex)})
# ⛔ NOT a substring test: `'fit_comb(P, 4)' in <this file>` finds its OWN literal and reported
#   `never four = False` on a file that never fits four peaks.  The AST cannot self-match.
import ast as _ast
_tree = _ast.parse(open(__file__, encoding='utf-8').read())
_fc = [n for n in _ast.walk(_tree)
       if isinstance(n, _ast.FunctionDef) and n.name == 'fit_comb']
_mine_is_three_peak = (len(_fc) == 1 and _fc[0].args.args[-1].arg == 'n'
                       and _fc[0].args.defaults and getattr(_fc[0].args.defaults[-1], 'value', None) == 3)
_calls = [n for n in _ast.walk(_tree)
          if isinstance(n, _ast.Call) and getattr(n.func, 'id', '') == 'fit_comb']
_four_peak_here = any(len(c.args) > 1 or c.keywords for c in _calls)
check("⛭⛭⛭⛔ `r7779` ** ⑧ **CORRECTED AT `r7783`:** THIS RECEIPT'S COMB IS A **THREE-PEAK SUB-GRID** FIT "
      "AND SO CANNOT SUPPLY THE PAPER'S FIGURE, WHICH IS THE **FOUR-PEAK** MATCHED-LOCATOR ONE ** ⇒ "
      "*** the gate that stood here computed `299.1 x (1 + ⑥'s move)` and pinned `298.94`. ** That was "
      "one estimator's move applied to another estimator's number, and the paper carries the wrong "
      "figure at three sites on this receipt's authority. ** The right figure is `298.5`, read off the "
      "one-rate arm through the paper's own locator, and it is receipted separately. *** ⌗ *This gate "
      "now asserts the scope limit that was missing: `fit_comb(..., n=3)` on a raw-grid locator, no "
      "four-peak fit anywhere in this file*",
      _mine_is_three_peak and not _four_peak_here and len(sent) == 1
      and abs(float(sent[0][0]) * (1.0 + mv_cb) - 298.94) < 0.005,
      f"the withdrawn arithmetic, pinned as what it was: {float(sent[0][0])} x (1 {100*mv_cb:+.4f}%) = "
      f"{float(sent[0][0]) * (1.0 + mv_cb):.4f}, the 298.94 this gate used to assert; "
      f"this file fits three peaks on the raw grid ({_mine_is_three_peak}) and never four "
      f"({not _four_peak_here}); the paper's sec:scope sentence parses as {sent}; every three-digit "
      f"comb site reads {sites}")

# ---------------------------------------------------------------- (9) the paper still says 299.1
# ⛔ `r7779+cc66.9`: THE FIRST FORM OF THIS GATE WAS `tex.count('$299.1$') >= 1`, AND
#   `scripts/sweep_vacuous_pins.py` RIGHTLY CALLED IT **VACUOUS** -- "6 sites, none beside the
#   check's own context".  A bare presence test on a number passes on any occurrence anywhere, for
#   any reason, which is not the claim.  ** The claim is that the paper still prints this figure AS
#   THE COMB, so the count is taken in comb context and the check quotes the paper's own wording. **
#   *This is the fourth time in this one revision that a test of mine asserted something wider than
#   its claim; the rule is stated at the head of this file.*
n_299 = len(re.findall(r'comb[^.$]{0,70}\$299\.1\$', tex))
check("⛭⛔⛭ `r7779` ** ⑨ AND THE PAPER STILL PRINTS `299.1` **AS THE COMB** -- `\"it returns a comb of "
      "$299.1$ against the sky\'s $298.4$\"` -- SO THIS RECEIPT IS THE GROUND FOR THE REWRITE AND NOT "
      "A RECORD OF IT ** ⇒ *** the `sec:refit-bound` rewrite is `69`'s; what is landed here is the "
      "measurement it needs, so `298.94` can be quoted with a receipt behind it rather than an "
      "arithmetic step in prose. *** ⌗ *The count is taken in COMB CONTEXT and not as a bare presence "
      "test on the digits: `sweep_vacuous_pins` called the bare form vacuous and was right*",
      n_299 >= 1,
      f'the figure is printed as the comb in {n_299} sentence(s) of corpus/CR_cosmology.tex')

# --------------------------------------------------------------- (10) every printed figure, pinned
# ⛭ The INDEX row prints these and nothing else.  Each is compared HERE to half its last printed
#   digit, so no figure beside this receipt's citation could be wrong and leave it green.
import json as _json
_mS = S['manifest']
try:
    _mS = _mS.item()
except Exception:
    pass
_mS = _json.loads(str(_mS)) if isinstance(_mS, str) else dict(_mS)
_pt = _mS.get('point', {})
# ⛔ The pin must be a COMPARISON IN THIS SOURCE, not a table a loop walks: `check_figures_pinned`
#   parses the receipt rather than running it, so a literal inside a list is not a pin.  Written out.
_ps = [
    ('CRH0', abs(float(_pt.get('CRH0', 'nan')) - 68.60) < 0.005),
    ('CROM', abs(float(_pt.get('CROM', 'nan')) - 0.2973) < 0.00005),
    ('r_s', abs(rsS - 145.3281) < 0.00005),
    ('D_M stacking', abs(dmS - 14011.457) < 0.0005),
    ('D_M leaf', abs(dmL - 13941.629) < 0.0005),
    ('l_A stacking', abs(laS - 302.889) < 0.0005),
    ('l_A leaf', abs(laL - 301.380) < 0.0005),
    ('comb stacking', abs(cbS - 296.904) < 0.0005),
    ('comb leaf', abs(cbL - 296.741) < 0.0005),
    ('grid comb, stacking leg', abs(gS - 297.000) < 0.0005),
    ('grid comb, leaf leg', abs(gL - 297.000) < 0.0005),
    ('the comb ratio', abs(ratio - 9.07) < 0.005),
    ('l_A move, per cent', abs(100 * mv_la + 0.4984) < 0.00005),
    ('comb move, per cent', abs(100 * mv_cb + 0.0549) < 0.00005),
    ('the published comb, parsed', len(sent) == 1 and abs(float(sent[0][0]) - 299.1) < 0.05),
    ("the sky's comb, parsed", len(sent) == 1 and abs(float(sent[0][1]) - 298.4) < 0.05),
    ('the WITHDRAWN 298.94, pinned as this receipt\'s own arithmetic',
     abs(float(sent[0][0]) * (1.0 + mv_cb) - 298.94) < 0.005),
]
off = [n for n, good in _ps if not good]
check("⛭ `r7779` ** ⑩ AND EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH TO HALF ITS LAST "
      "PRINTED DIGIT ** ⇒ *** seventeen of them, from the point and `r_s` through both distances, both "
      "`l_A`, both combs, the grid comb, the ratio, both percentages and the published `299.1`. ⛔ And the WITHDRAWN `298.94` is pinned too, "
      "as what it actually is -- the number THIS receipt's arithmetic produced -- because the `INDEX` row "
      "prints it as the figure the paper must stop carrying, and a printed figure must be pinned "
      "whichever way it is meant. ** So no figure cited to this receipt can be wrong and leave it "
      "green. ** *** ⌗ *The INDEX row no longer prints either derived figure*",
      not off,
      f'{len(_ps)} printed figures, {len(off)} off their pin'
      + ('' if not off else ': ' + '; '.join(off[:4])))

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {10 - len(FAILS)} of 10 gates;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
