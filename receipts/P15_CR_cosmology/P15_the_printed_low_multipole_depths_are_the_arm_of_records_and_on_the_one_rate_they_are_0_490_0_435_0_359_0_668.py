#!/usr/bin/env python3
r"""`r7783` ** `P15`'s PRINTED LOW-MULTIPOLE DEPTHS `0.485 / 0.441 / 0.354 / 0.657` ARE THE ARM OF
RECORD'S, AT THE DISTANCES' POINT.  ON THE RATE THE UNIVERSE HAS THEY ARE
`0.490 / 0.435 / 0.359 / 0.668` -- AND THE SHAPE CLAIMS DO NOT MOVE: THE MINIMUM STAYS AT `l = 4`
AND THE RECOVERY STAYS AT `l = 8`. **

** AND THE PAPER'S `2.9` PER CENT CROSS-VALIDATION IS NAMED EXACTLY: IT IS ARM A AGAINST ARM B's
**DECOUPLED** BUILD, AT THE DISTANCES' POINT, UNDER (L) -- `2.91 %`.  THE **FROZEN** BUILD GIVES
`6.19 %` THERE, SO IT IS NOT THE SENTENCE'S. **

Built `r7783+cc66.1`, discharging order ① of the chat seat's `r7783`: *"Take them at the arm and point
those sentences quote, under `SPLITCLOCK` unset, so I can rewrite them to the one-rate values. Say in
the receipt which point the paper's 2.9 per cent cross-validation is taken at."*

===================================================================================================
** COMPUTES: ** the low-multipole depths of `P15` `sec:largescale` and the abstract -- the ratio of the
   boundary-quantised discrete sum to the continuum integral of the SAME transfer, per `l` -- read off
   four banked legs at the DISTANCES' point `(H0 68.60, Om 0.2973, omega_b 0.02237, radiation
   4.1833e-5/h^2)`: arm A (CAMB's exact transfer with the hierarchy's projection) and arm B (the photon
   hierarchy), each under (L) -- the arm of record, grid and projection on the stacking rate -- and
   under `SPLITCLOCK` unset, the one rate.  The paper's printed figures are PARSED out of
   `corpus/CR_cosmology.tex` and compared; nothing is retyped.  No likelihood, nothing fitted.
===================================================================================================

⛔ ** THE ORDER'S WORDING RUNS TWO NUMBERS TOGETHER, AND THIS RECEIPT SEPARATES THEM BEFORE IT
REPORTS EITHER. **  The order says *"Say in the receipt which point the paper's 2.9 per cent
cross-validation is taken at.  Your 3.39 and 3.51 are at the refit point."*  ** Those are two
different comparisons, not one comparison at two points: **

 * the paper's ** `2.9` per cent ** is ** arm A against arm B ** -- the exact transfer against the
   photon hierarchy, two independent Boltzmann treatments.  Its own sentence says so: *"the hierarchy
   agrees to `2.9` per cent at every multipole"*.  `(4)` locates it and names the build.
 * my ** `3.39` / `3.51` ** is ** frozen against decoupled **, two tower builds INSIDE arm B -- the
   depth receipt's own standard, *"Both variants are reported; they agree to `3 %`, which is the point
   of running both"*.  `(6)` keeps it separate, with its point.

*So `r7779+cc66.2`'s `R5'` did not measure the paper's number at another point; it measured a
different quantity.  Neither may be carried into the paper as the other.*

⛭ ** AND THE PAPER'S SECOND CLAUSE FIXES WHAT "ABOVE `l = 5`" MEANS. **  *"and to under one per cent
above `l = 5`"* holds on the reading `l > 5` -- `0.30 %` over `l = 6,7,8` -- and ** does not hold ** on
the reading `l >= 5`, where the same pair is `1.20 %`.  *So the sentence is committed to the strict
reading, which is worth knowing before it is rewritten.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that the one-rate depths fit the sky better or worse. **  No likelihood is formed and the
   paper's `Delta(-2 ln L) = +1.7` scoring is untouched.
 * ** Not that the paper's figures were wrong. **  They are the arm of record's, correctly, and `(1)`
   confirms them against the paper's own text.  What moves is which configuration the paper means to
   report, which is `69`'s call and not this receipt's.
 * ** Not a new instrument run. **  Every number is a banked array; `(7)` is why the one pair with a
   blob mismatch may be read at all.

⛭ ** FAILABILITY, MEASURED. **  Scaling the one-rate arm-A leg by `1 + 2e-3` reddens `(2)`, `(5)` and
`(8)` -- the one-rate figures, the one-rate cross-validation and the figure pins -- while `(1)`, `(3)`,
`(4)`, `(6)` and `(7)` hold, since they read the (L) legs, the paper's text, the refit point and the
two blobs.  Measured in
`computations/beyond_the_wall/r7783_cc66_the_low_ell_depths_receipt_on_the_one_rate/failability.py`.

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy; seconds)
8 gates.  `(8)` pins every figure the INDEX row prints, each to half its last printed digit.
"""
import ast
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f'             {witness}')


def bank(stem):
    p = os.path.join(SPEC, stem + '.npz')
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the bank has moved.')
    with np.load(p, allow_pickle=True) as z:
        return {k: z[k] for k in z.files}


LP, OC, AA = (bank('p15_lowell_depths_leafpert_leafrec1'),
              bank('p15_lowell_depths_distances_oneclock_leafrec1'),
              bank('p15_lowell_depths_armA_leafpert_leafrec1'))
ELLS = [int(x) for x in LP['ells']]
A_L = np.asarray(AA['distances__armA__L'], float)
A_1 = np.asarray(AA['distances__armA__one_clock_gate'], float)
tex = open(TEX, encoding='utf-8').read()

print('=' * 100)
print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------- (1) the printed figures are armA (L)
# ⛔ `check_quote_pins` NAMED THIS EXACTLY RIGHT AND THE FIRST FORM OF THIS GATE WAS WRONG FOR IT:
#   *"A gate that asserts another seat's sentence is present fails when that seat rewords -- and fails
#   on SUCCESS when the sentence said something was open."*  ** This receipt exists so that 69 can
#   rewrite that very sentence to the one-rate quartet. **  A pin on its CURRENT wording would
#   therefore go red on the success it is for.  ⇒ The gate tests the DISJUNCTION: the sentence must
#   print one of the two quartets this receipt measures, and which one it is, is reported rather than
#   demanded.  Adjudicated `ALT-OK` in `corpus/quote_pin_baseline.tsv` in the same pass.
QUARTETS = {'the arm of record, (L)': (0.485, 0.441, 0.354, 0.657),
            'the one rate': (0.490, 0.435, 0.359, 0.668)}
_m = re.search(r'\$\\approx(\d\.\d{3})\$,\s+\$(\d\.\d{3})\$,\s+\$(\d\.\d{3})\$\s+and\s+'
               r'\$(\d\.\d{3})\$\s+of\s+the\s+flat-\$\\Lambda\$CDM\s+expectation\s+at\s+'
               r'\$\\ell=2,3,4,5\$', tex)
printed = tuple(float(x) for x in _m.groups()) if _m else None
which = next((k for k, v in QUARTETS.items() if printed == v), None)
hit_L = [abs(round(float(v), 3) - w) < 1e-9 for v, w in zip(A_L[:4], QUARTETS['the arm of record, (L)'])]
hit_1 = [abs(round(float(v), 3) - w) < 1e-9 for v, w in zip(A_1[:4], QUARTETS['the one rate'])]
check("⛭⛭⛭ `r7783` ** ① THE QUARTET `sec:largescale` PRINTS IS ONE OF THESE TWO, AND THEY ARE THE SAME "
      "ARM AND POINT UNDER THE TWO CLOCKS: `0.485 / 0.441 / 0.354 / 0.657` IS ARM A UNDER **(L)** AT THE "
      "DISTANCES' POINT, AND `0.490 / 0.435 / 0.359 / 0.668` IS THAT ARM ON THE ONE RATE ** ⇒ *** so the "
      "paper is quoting the ARM OF RECORD at the point its distances are quoted at, and the rewrite's "
      "target is the other member of the pair. ** Both quartets reproduce to the digit from the banked "
      "legs, which is what makes the disjunction a measurement and not a hedge. ** *** ⌗ *The gate tests "
      "the DISJUNCTION on purpose: a pin on the sentence's CURRENT wording would go red on the very "
      "rewrite this receipt is for, which is `check_quote_pins`'s own named failure mode*",
      printed is not None and which is not None and all(hit_L) and all(hit_1),
      f"the sentence prints {printed}, which is {which!r}; armA (L) rounds to "
      f"{[round(float(v), 3) for v in A_L[:4]]} and armA one-rate to "
      f"{[round(float(v), 3) for v in A_1[:4]]}")

# ---------------------------------------------------------------- (2) the one-rate values
check("⛭⛭⛭ `r7783` ** ② AND ON THE RATE THE UNIVERSE HAS, AT THE SAME ARM AND POINT, THEY ARE "
      "`0.4898 / 0.4351 / 0.3594 / 0.6677` -- `0.490 / 0.435 / 0.359 / 0.668` AT THE PAPER'S OWN "
      "PRECISION ** ⇒ *** these are the four numbers the `sec:largescale` and abstract sentences take "
      "under `SPLITCLOCK` unset. ** The quadrupole and the fifth multipole rise, the octopole falls: "
      "the move is NOT a uniform rescaling, which is the `r7779` finding restated at the paper's own "
      "arm. ** *** ⌗ *Pinned to half the last printed digit, so a bank that moved would redden this*",
      abs(A_1[0] - 0.4898) < 0.00005 and abs(A_1[1] - 0.4351) < 0.00005
      and abs(A_1[2] - 0.3594) < 0.00005 and abs(A_1[3] - 0.6677) < 0.00005,
      f"one rate at l=2..5: {[round(float(v), 4) for v in A_1[:4]]}; "
      f"(L) {[round(float(v), 4) for v in A_L[:4]]}; "
      f"relative moves {[f'{100*(a/b-1):+.2f}%' for a, b in zip(A_L[:4], A_1[:4])]}")


def recovery(d):
    return next((l for l, v in zip(ELLS, d) if l >= 5 and v >= 0.99), None)


# ---------------------------------------------------------------- (3) the shape claims survive
mn_L, mn_1 = ELLS[int(np.argmin(A_L[:4]))], ELLS[int(np.argmin(A_1[:4]))]
check("⛭ `r7783` ** ③ AND THE PAPER'S TWO SHAPE CLAIMS DO NOT MOVE: THE MINIMUM STAYS AT `l = 4` AND "
      "THE RECOVERY STAYS AT `l = 8` ** ⇒ *** *\"a dip whose minimum falls at `l=4`\"* and *\"recovering "
      "by `l` ≈ `8`\"* stand unchanged on the one rate, so ONLY the four numbers need rewriting. ** The "
      "clock reshapes the deficit without moving where it closes. ** *** ⌗ *The recovery test is the "
      "bank's own definition, first `l >= 5` with depth `>= 0.99`*",
      mn_L == 4 and mn_1 == 4 and recovery(A_L) == 8 and recovery(A_1) == 8,
      f"minimum at l={mn_L} under (L) and l={mn_1} on the one rate; recovery multipole "
      f"{recovery(A_L)} and {recovery(A_1)}")

# ---------------------------------------------------------------- (4) the 2.9 per cent, NAMED
xv = {}
for build in ('frozen', 'decoupled'):
    for clock, (a, b) in (('L', (A_L, np.asarray(LP[f'distances__armB_{build}__L'], float))),
                          ('one', (A_1, np.asarray(OC[f'armB_{build}'], float)))):
        r = np.abs(b / a - 1.0) * 100.0
        xv[(build, clock)] = (float(r.max()), float(r[4:].max()))
print(f"\n      {'armA vs armB':34} {'max over l=2..8':>16} {'max over l>5':>14}")
for k in (('decoupled', 'L'), ('frozen', 'L'), ('decoupled', 'one'), ('frozen', 'one')):
    print(f"      {k[0]+', '+('(L)' if k[1]=='L' else 'one rate'):34} "
          f"{xv[k][0]:>15.2f}% {xv[k][1]:>13.2f}%")
ge5 = float(np.max(np.abs(np.asarray(LP['distances__armB_decoupled__L'], float) / A_L - 1.0)[3:]) * 100)
check("⛭⛭⛭ `r7783` ** ④ THE PAPER'S `2.9` PER CENT IS ARM A AGAINST ARM B's **DECOUPLED** BUILD, AT THE "
      "DISTANCES' POINT, UNDER (L): `2.91 %` ** ⇒ *** and the **frozen** build gives `6.19 %` there, so "
      "the sentence is NOT frozen's -- the cross-validation is named by BUILD and not only by point. ** "
      "Its second clause fixes its own reading: *\"under one per cent above `l = 5`\"* holds at `0.30 %` "
      "on `l > 5` and FAILS at `1.20 %` on `l >= 5`, so the sentence is committed to the strict "
      "reading. ** *** ⌗ *This is the identification the order asked for, sharpened: point, clock AND "
      "build*",
      abs(xv[('decoupled', 'L')][0] - 2.91) < 0.05 and xv[('decoupled', 'L')][1] < 1.0
      and xv[('frozen', 'L')][0] > 5.0 and ge5 > 1.0,
      f"decoupled vs armA under (L): {xv[('decoupled','L')][0]:.2f}% over l=2..8, "
      f"{xv[('decoupled','L')][1]:.2f}% over l>5, {ge5:.2f}% over l>=5; frozen vs armA "
      f"{xv[('frozen','L')][0]:.2f}%")

# ---------------------------------------------------------------- (5) and on the one rate
check("⛭ `r7783` ** ⑤ ON THE ONE RATE THAT CROSS-VALIDATION IS `3.03 %`, AND THE SECOND CLAUSE STILL "
      "HOLDS AT `0.37 %` ** ⇒ *** so *\"agrees to `2.9` per cent\"* becomes *\"`3.0` per cent\"* and "
      "*\"under one per cent above `l = 5`\"* needs no change. ** The two independent transfers "
      "cross-validate on the one rate as they do on the arm of record -- the rate moves both of them "
      "the same way. ** *** ⌗ *A `0.12` percentage-point move, measured, not an argument that it should "
      "be small*",
      abs(xv[('decoupled', 'one')][0] - 3.03) < 0.05 and xv[('decoupled', 'one')][1] < 1.0,
      f"one rate: {xv[('decoupled','one')][0]:.2f}% over l=2..8 and "
      f"{xv[('decoupled','one')][1]:.2f}% over l>5, against (L)'s "
      f"{xv[('decoupled','L')][0]:.2f}% and {xv[('decoupled','L')][1]:.2f}%")

# ---------------------------------------------------------------- (6) the OTHER three per cent
fd = {}
for clock, suf in (('L', 'L'), ('one', 'one_clock')):
    f = np.asarray(LP[f'refit__armB_frozen__{suf}'], float)
    d = np.asarray(LP[f'refit__armB_decoupled__{suf}'], float)
    fd[clock] = float(np.max(np.abs(f / d - 1.0)) * 100)
has_oc_dist = any(k.startswith('distances__armB') and k.endswith('one_clock') for k in LP)
check("⛭⛔⛭ `r7783` ** ⑥ AND MY OWN `3.39 / 3.51` IS A DIFFERENT COMPARISON ENTIRELY -- FROZEN AGAINST "
      "DECOUPLED, INSIDE ARM B, AT THE **REFIT** POINT ** ⇒ *** it is the depth receipt's own "
      "frozen/decoupled standard and NOT the paper's arm-A-against-arm-B figure, so neither may be "
      "carried into the paper as the other. ** At the distances' point only the (L) legs of that pair "
      "are banked, so there is no one-rate frozen/decoupled figure there without a new run, which this "
      "item does not order. ** *** ⌗ *`r7779+cc66.2`'s `R5'` measured this and reported it as the "
      "paper's `3 %`; `④` is what the paper's sentence actually is*",
      abs(fd['L'] - 3.39) < 0.05 and abs(fd['one'] - 3.51) < 0.05 and not has_oc_dist,
      f"frozen vs decoupled at the refit point: {fd['L']:.2f}% under (L), {fd['one']:.2f}% on the one "
      f"rate; a distances-point one-clock armB row in the leafpert bank: {has_oc_dist}")

# ---------------------------------------------------------------- (7) the blob licence, re-run
import json as _json
cL = _json.loads(str(LP['config'].item() if LP['config'].shape == () else LP['config']))
cO = _json.loads(str(OC['config'].item() if OC['config'].shape == () else OC['config']))


class Norm(ast.NodeTransformer):
    """reduce a tree to what it IS when SPLITCLOCK is unset, so _SPLITL is False"""

    def visit_Name(self, node):
        if node.id == '_Hdyn':
            return ast.copy_location(ast.Name(id='Hc_of', ctx=node.ctx), node)
        return node

    def visit_IfExp(self, node):
        self.generic_visit(node)
        if isinstance(node.test, ast.Name) and node.test.id == '_SPLITL':
            return node.orelse
        return node

    def visit_If(self, node):
        self.generic_visit(node)
        if isinstance(node.test, ast.Name) and node.test.id == '_SPLITL':
            return node.orelse or None
        return node

    def visit_Assign(self, node):
        self.generic_visit(node)
        t = node.targets[0]
        if isinstance(t, ast.Name):
            if t.id == '_SPLITL':
                return None
            if t.id == 'Hc_of' and isinstance(node.value, ast.Name) and node.value.id == 'Hc_of':
                return None
        return node

    def visit_BoolOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.Or):
            keep = [v for v in node.values if not (isinstance(v, ast.Name) and v.id == '_SPLITL')]
            if len(keep) != len(node.values):
                return keep[0] if len(keep) == 1 else ast.BoolOp(op=node.op, values=keep)
        return node


def blob(sha):
    return subprocess.run(['git', 'cat-file', '-p', sha], cwd=ROOT, capture_output=True).stdout.decode()


try:
    old = ast.dump(ast.parse(blob(cO['HIER_blob'])))
    red = Norm().visit(ast.parse(blob(cL['HIER_blob'])))
    ast.fix_missing_locations(red)
    inert = old == ast.dump(red)
except Exception as exc:
    inert = False
    old = f'{type(exc).__name__}: {exc}'
check("⛭⛔⛭ `r7783` ** ⑦ AND THE ONE-RATE LEG'S BLOB MISMATCH IS RE-TESTED HERE RATHER THAN CITED: "
      "NORMALISE THE NEWER BLOB FOR `SPLITCLOCK` UNSET AND ITS AST IS **IDENTICAL** TO THE OLDER "
      "BLOB'S ** ⇒ *** the (L) legs were produced at `c66bfff27…` and the one-rate leg at "
      "`5936a51b8…`, so that pair differs by instrument VERSION as well as by clock -- and with the "
      "switch unset the newer blob IS the older program, not merely one that behaves like it. ** So "
      "`②` and `⑤` rest on a test this file runs, not on a claim it inherits. ** *** ⌗ *A difference "
      "outside the reductions survives them and reddens this row*",
      inert and cL['HIER_blob'] != cO['HIER_blob'],
      f"(L) blob {cL['HIER_blob'][:9]}…, one-rate blob {cO['HIER_blob'][:9]}…; normalised ASTs "
      f"{'identical' if inert else 'differ'}")

# ---------------------------------------------------------------- (8) every printed figure, pinned
_ps = [
    ('paper l=2', abs(float(A_L[0]) - 0.4848) < 0.00005),
    ('paper l=3', abs(float(A_L[1]) - 0.4407) < 0.00005),
    ('paper l=4', abs(float(A_L[2]) - 0.3536) < 0.00005),
    ('paper l=5', abs(float(A_L[3]) - 0.6569) < 0.00005),
    ('one rate l=2', abs(float(A_1[0]) - 0.4898) < 0.00005),
    ('one rate l=3', abs(float(A_1[1]) - 0.4351) < 0.00005),
    ('one rate l=4', abs(float(A_1[2]) - 0.3594) < 0.00005),
    ('one rate l=5', abs(float(A_1[3]) - 0.6677) < 0.00005),
    ('decoupled vs armA, (L)', abs(xv[('decoupled', 'L')][0] - 2.91) < 0.005),
    ('decoupled vs armA, one rate', abs(xv[('decoupled', 'one')][0] - 3.03) < 0.005),
    ('frozen vs armA, (L)', abs(xv[('frozen', 'L')][0] - 6.19) < 0.005),
    ('above l>5, (L)', abs(xv[('decoupled', 'L')][1] - 0.30) < 0.005),
    ('above l>5, one rate', abs(xv[('decoupled', 'one')][1] - 0.37) < 0.005),
    ('on l>=5, (L)', abs(ge5 - 1.20) < 0.005),
    ('frozen vs decoupled, refit, (L)', abs(fd['L'] - 3.39) < 0.005),
    ('frozen vs decoupled, refit, one rate', abs(fd['one'] - 3.51) < 0.005),
]
off = [n for n, good in _ps if not good]
check("⛭ `r7783` ** ⑧ AND EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH TO HALF ITS LAST "
      "PRINTED DIGIT ** ⇒ *** sixteen of them: the paper's four, the one rate's four, both "
      "cross-validations and the frozen build's, both above-`l>5` figures, the `l >= 5` figure that "
      "shows the clause's reading, and my two refit-point figures. ** So no figure cited to this "
      "receipt can be wrong and leave it green. *** ⌗ *The `1.20` is pinned precisely BECAUSE it is the "
      "reading the paper's clause EXCLUDES*",
      not off, f'{len(_ps)} printed figures, {len(off)} off their pin'
               + ('' if not off else ': ' + '; '.join(off[:4])))

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {8 - len(FAILS)} of 8 gates;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
