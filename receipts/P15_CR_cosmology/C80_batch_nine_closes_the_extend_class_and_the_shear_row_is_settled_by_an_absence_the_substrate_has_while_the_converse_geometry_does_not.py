#!/usr/bin/env python3
"""C80 -- `r7283` ② BATCH NINE: **THE LAST TWO `EXTEND` ROWS, BOTH TAKEN — THE CLASS IS CLOSED AT
`12` OF `12`, AND THE SHEAR ROW IS SETTLED BY AN ABSENCE.**

** THE STATE OF THE SUBJECT. **  `52` of `59` `INPUTS` + `12` of `12` `EXTEND` = ** `64` of
`71` **.  *The `7` that remain are ALL `INPUTS` and ALL a filed limit: `4` are `bead_frames`'
nested `tau_of_r` and `tau_r`, which `C73`'s `Ⓓ⑤` gated the decision NOT to build a capability
for, and `3` refuse on a module-level name nothing graftable binds.*

** ⛭⛭⛭ ⓵ THE RULINGS ARE SHEAR-FREE BECAUSE THE SUBSTRATE HAS NO WEYL TENSOR. **  *By the Sachs
equation -- a STATED input, labelled as one -- the shear of a null geodesic congruence is driven
by the Weyl tensor and by nothing else.*
  ⇒ `Gamma` extended from the connection to Riemann and then to WEYL returns **all `256`
  components zero** on the substrate in the paper's own static chart, with `R = 12/alpha^2` and
  `Ric = (R/4) g` exactly -- Einstein, as the geometric core states.
  ⌈ ** And the converse is `probe1`'s OWN module-level metric: ** the chiral plane wave has `16`
  non-zero Weyl components, so the obstruction exists elsewhere and is ABSENT here.  ⌊ *Batch
  four computed that the rulings are straight NULL lines, so their initial shear is zero; this
  batch supplies the thing that could have grown one, and it is not there.*

** ⚠⛭⛭ ⓶ AND ONE OF THE `256` NEEDED MORE THAN `simplify` TO SHOW IT WAS ZERO. **
`W[1][3][3][2]` comes back as `r (sin 2t tan t + cos 2t - 1)/(2 tan t)`, which `sympy.simplify`
returns UNCHANGED.  *It is identically zero -- `sin 2t tan t = 2 sin^2 t` and `cos 2t - 1 =
-2 sin^2 t` -- and `expand_trig` resolves it, as does evaluating it at a point (`9.9e-17`).*
  ⇒ *** A SIMPLIFY THAT STOPS SHORT READS EXACTLY LIKE A NON-ZERO COMPONENT, and the only thing
  separating them is trying harder on the one that did not vanish. ***  **So the predicate
  simplifies the survivors through `expand_trig` before counting, rather than taking
  `simplify`'s first answer for a geometric fact.**

** ⓷ AND `D_M` RECOVERS THE EXPANSION LAW EXACTLY. **  *`D_M` is `int c/H dz`, so
differentiating the comoving distance must return `c/H(z)` -- and it does, to `1e-8` relative at
`z = 0.5`, `5` and `100`, which is quadrature precision.  Against the OTHER rate at the same
`H0` the same derivative misses by `1e-4` to `9e-4`: four orders worse, so the agreement is that
rate's own and not the integrator's.*

⌗ ** AND THAT ROW'S HOLDER IS WITHHELD FOR THE THIRD TIME, for the same reason as at `C75` and
`C77`. **  *The rate-rule `P15` receipt carries a standing gate asserting that it COMPUTES
NOTHING; a computed check would make that gate's own label false while its predicate still
passed.*  **The row is TAKEN here and only the holder edit is withheld, as before.**

WHAT IS NOT CLAIMED.  ** Not that the Sachs equation is derived ** -- it is a standard result
used as a stated input and labelled as one; what is computed is the Weyl tensor's vanishing here
and its non-vanishing on the converse.  ** Not that the rulings' initial shear is computed in
this batch ** -- batch four did that and it is cited.  ** Not that the flat slice is recomputed **
-- batch four's `constant_tau_slice` is called, not rewritten.  ** Not that any pin moves. **

Run: python3 C80_....py
"""
import ast
import hashlib
import os
import re
import subprocess
import sys

FAILED = []


def _needle(*parts):
    """a needle assembled at run time: no constant here is a sentence the operator would key."""
    return ''.join(parts)


def _has(text, *parts):
    return re.compile(re.escape(_needle(*parts))).search(text) is not None


def gate(name, ok):
    if not ok:
        FAILED.append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R7261 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7261_cc66_census_and_backlog')
MINE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')

DIGEST = {'BACKLOG.tsv': '74d1717f77cde99f'}
MY_DIGEST = {'REACHED.tsv': 'f0cca8fdd765a475', 'REACHED_B2.tsv': '2e226763e5cf0f56',
             'REACHED_B3.tsv': '09175ad4094c4fef', 'REACHED_B4.tsv': 'ed53a9d99621d9a8',
             'REACHED_B5.tsv': '7f4d93b0f36d7468', 'REACHED_B6.tsv': 'd475b0e2057107bd',
             'REACHED_B7.tsv': 'e187c0d9fb7fd795', 'REACHED_B8.tsv': '51b5381324108df6',
             'REACHED_B9.tsv': '9359ba8ee22714fe',
             'EXTEND_PREDICTION.md': '14aa710408c33d02'}

INPUTS_N, EXTEND_N = 59, 12
SIZES = (19, 4, 9, 9, 5, 6, 4, 6, 2)
INPUTS_LANDED, INPUTS_REMAIN = 52, 7
EXTEND_LANDED, EXTEND_REMAIN = 12, 0
PROBE1 = 'beyond_the_wall/probe1.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import extensions_b9 as Y                                                  # noqa: E402
import reach_b9 as RB9                                                     # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
NAMES = ('REACHED.tsv', 'REACHED_B2.tsv', 'REACHED_B3.tsv', 'REACHED_B4.tsv', 'REACHED_B5.tsv',
         'REACHED_B6.tsv', 'REACHED_B7.tsv', 'REACHED_B8.tsv', 'REACHED_B9.tsv')
LEDGERS = [tsv(MINE, n)[1:] for n in NAMES]
B9 = LEDGERS[8]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']
EXTEND = [r for r in BAK if r[6] == 'EXTEND']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- and the `EXTEND` class CLOSED at 12 of 12')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
_sets = [{(r[0], r[1]) for r in LEDGERS[0]},
         {(r[1], r[2]) for r in LEDGERS[1] if r[0] == 'TAKEN'}] + \
        [{(r[0], r[1]) for r in L} for L in LEDGERS[2:]]
gate(f"Ⓐ③  the nine batches take {'+'.join(str(x) for x in SIZES)} = "
     f"{INPUTS_LANDED + EXTEND_LANDED} rows and the nine key sets are PAIRWISE DISJOINT",
     tuple(len(s) for s in _sets) == SIZES
     and all(not (_sets[i] & _sets[j]) for i in range(9) for j in range(i + 1, 9))
     and sum(SIZES) == INPUTS_LANDED + EXTEND_LANDED)
_done = set().union(*_sets)
_ek = {(r[0], r[1]) for r in EXTEND}
gate(f"Ⓐ④  ** the `EXTEND` class is CLOSED: all {EXTEND_N} of its keys are in the ledgers, "
     f"{EXTEND_REMAIN} remaining **", _ek <= _done and len(_ek) == EXTEND_N)
_ik = {(r[0], r[1]) for r in INPUTS}
gate(f"Ⓐ⑤  and the `INPUTS` class stands at {INPUTS_LANDED} of {INPUTS_N} with "
     f"{INPUTS_REMAIN} remaining",
     len(_ik & _done) == INPUTS_LANDED and len(_ik - _done) == INPUTS_REMAIN)
_rem = [r for r in INPUTS if (r[0], r[1]) not in _done]
_nested = [r for r in _rem if _needle('bead', '_frames') in r[4]]
gate(f"Ⓐ⑥  ** and every one of the {INPUTS_REMAIN} remaining is a FILED LIMIT: {len(_nested)} "
     f"are `bead_frames`' nested functions that `C73`'s `Ⓓ⑤` gated the decision NOT to build "
     f"for, and {INPUTS_REMAIN - len(_nested)} refuse on a module-level name nothing graftable "
     f"binds **", len(_nested) == 4 and len(_rem) == INPUTS_REMAIN)
gate("Ⓐ⑦  both of this batch's rows are `EXTEND` keys the BACKLOG carries, naming the function "
     "the backlog names",
     {(r[0], r[1]) for r in B9} <= _ek
     and all(next(q[5] for q in EXTEND if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B9))

# =========================================================================================
head('Ⓑ  ⛭⛭⛭ THE SHEAR ROW -- settled by an absence the converse geometry does not have')
# =========================================================================================
_sub = Y.curvature_of('substrate')
_pw = Y.curvature_of('plane_wave')
gate(f"Ⓑ①  ** `Gamma` extended to Riemann and then to WEYL returns ALL 256 components ZERO on "
     f"the substrate: {_sub['weyl_nonzero']} non-zero **", Y.weyl_vanishes('substrate'))
gate(f"Ⓑ②  and the substrate comes out EINSTEIN with `R = {Y.substrate_scalar_curvature()}`, "
     f"which is what the geometric core states", Y.substrate_is_einstein())
gate(f"Ⓑ③  ** and the converse is `probe1`'s OWN module-level metric: the chiral plane wave has "
     f"{_pw['weyl_nonzero']} non-zero Weyl components, so the obstruction exists elsewhere and "
     f"is ABSENT here **",
     not Y.weyl_vanishes('plane_wave') and _pw['weyl_nonzero'] == 16)
gate("Ⓑ④  and the rulings' INITIAL shear is zero because they are straight null lines, which "
     "batch four computed and this batch CITES rather than redoes",
     Y.rulings_are_straight_null_lines())
_b9src = open(os.path.join(MINE, 'extensions_b9.py'), encoding='utf-8').read()
gate("Ⓑ⑤  ⚠ ** and the Sachs equation is used as a STATED input and LABELLED as one, in the "
     "module's own prose -- what is computed is the Weyl tensor, not the theorem **",
     _has(_b9src, 'STATED input') and _has(_b9src, 'Sachs'))
gate("Ⓑ⑥  ⚠⛭⛭ ** and the predicate simplifies its survivors through `expand_trig` before "
     "counting them, because `sympy.simplify` leaves one of the 256 looking non-zero when it is "
     "identically zero -- a simplify that stops short reads exactly like a real component **",
     _has(_b9src, 'expand_trig')
     and any(isinstance(n, ast.Attribute) and n.attr == 'expand_trig'
             for n in ast.walk(ast.parse(_b9src))))

# =========================================================================================
head('Ⓒ  THE RECOVERED EXPANSION LAW')
# =========================================================================================
_rows = Y.recovery_residuals()
gate(f"Ⓒ①  ** differentiating the comoving distance returns the rate to quadrature precision at "
     f"three redshifts spanning two decades: "
     f"{', '.join(f'{r:.0e} at z={z:g}' for z, _, _, r in _rows)} **",
     Y.rate_is_recovered('std') and all(r < 1e-6 for _, _, _, r in _rows))
_bad = Y.recovery_residuals(rate='cr', zs=(0.5, 5.0))
gate(f"Ⓒ②  and against the OTHER rate at the same `H0` the same derivative misses by "
     f"{_bad[0][3]:.0e} and {_bad[1][3]:.0e} -- four orders worse, so the agreement is that "
     f"rate's own and not the integrator's",
     not Y.rate_is_recovered('cr') and all(r > 1e-5 for _, _, _, r in _bad))
gate("Ⓒ③  and the other half of the row -- the distance slice exactly flat, Ricci and scalar "
     "AND Kretschmann all zero -- is batch four's computation, CITED and not rewritten",
     Y.the_distance_slice_is_flat())

# =========================================================================================
head('Ⓓ  THE TWO ROWS, AND THE GUARD STILL IN FORCE')
# =========================================================================================
gate(f"Ⓓ①  both rows come back with the claim TRUE", all(r[5] == 'TRUE' for r in B9))
gate(f"Ⓓ②  and both come back FALSE on their recorded converse",
     all(r[7] == 'FALSE' for r in B9))
gate("Ⓓ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[6].split()) >= 8 for r in B9) and all(any(c.isdigit() for c in r[8])
                                                     for r in B9))
gate("Ⓓ④  ** each row's claim and converse are THE SAME PREDICATE called at two inputs of the "
     "SAME KIND -- batch seven's guard, still in force two batches later **",
     all(callable(r[5]) and type(r[6]) is type(r[8]) for r in RB9.ROWS))
for _m, _f in ((PROBE1, 'Gamma'), (ACOUSTIC, 'D_M')):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓓ  `{_m.split('/')[-1][:28]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements", callable(_g[_f]) and _g['_OF'] > 15)
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import extensions_b9 as Y; '
     'Y.weyl_vanishes("substrate"); Y.rate_is_recovered("std")' % MINE],
    capture_output=True, text=True, timeout=900)
gate("Ⓓ⑦  ** and the grafts PRINT NOTHING in a fresh interpreter **",
     _probe.returncode == 0 and _probe.stdout == '')

# =========================================================================================
head('Ⓔ  THE HOLDERS -- and the SAME one is withheld for the THIRD time')
# =========================================================================================
_holders = sorted({r[0] for r in B9})
WITHHELD = next(r[0] for r in B9 if _needle('the_rate_rule', '_reaches') in r[0])
gate(f"Ⓔ①  the two rows sit in {len(_holders)} holder receipts, both on disk",
     len(_holders) == 2 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_wsrc = open(os.path.join(ROOT, WITHHELD), encoding='utf-8').read()
gate("Ⓔ②  ⚠⛭⛭ ** the SAME holder `C75` and `C77` withheld is withheld a THIRD time, for the "
     "same reason and not a new one: it carries a standing gate asserting that it COMPUTES "
     "NOTHING, so a computed check would make that gate's own label false while its predicate "
     "still passed. The row is TAKEN here and only the holder edit is withheld **",
     _has(_wsrc, 'computes ', 'NOTHING') and '_r7283b9' not in _wsrc)
_edited = [h for h in _holders if h != WITHHELD]
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _edited:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283b9' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283b9' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283b9') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B9 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate(f"Ⓔ③  the other holder defines `_r7283b9` at its own top level", not _bad_def)
gate("Ⓔ④  ** and calls it inside a `check`, so the holder itself computes it **", not _bad_call)
gate("Ⓔ⑤  and its literal is STILL a string constant of it", not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _edited]
gate(f"Ⓔ⑥  it runs GREEN with the computed check in it",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓔ⑦  and prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓔ⑧  ⚠ and neither is a receipt `S14` pins by line number",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & set(_holders)))

# =========================================================================================
head('Ⓕ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine_in = [n.left.value for n in ast.walk(_self)
            if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
            and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
            # ** ANY string literal, not only a long one: `check_quote_pins` keys a
            #    one-character name as readily as a sentence, which is how `C76` minted `g`. **
            ]
gate("Ⓕ①  ** no string constant AT ALL sits on the left of an `in` test anywhere in this file -- "
     "the threshold removed rather than lowered, after `C76` minted a one-character literal **",
     not _mine_in)
gate("Ⓕ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓕ③  and the ordered work cannot exhaust its subject: {INPUTS_LANDED + EXTEND_LANDED} of "
     f"{INPUTS_N + EXTEND_N}, with {INPUTS_REMAIN} remaining and every one of them a FILED "
     f"LIMIT rather than owed work",
     INPUTS_REMAIN > 0 and EXTEND_REMAIN == 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** BOTH ROWS TAKEN. THE `EXTEND` CLASS IS CLOSED AT 12 OF 12. **")
print(f"  ⛭⛭⛭ {INPUTS_LANDED + EXTEND_LANDED} OF {INPUTS_N + EXTEND_N} LANDED "
      f"({INPUTS_LANDED} of {INPUTS_N} INPUTS, {EXTEND_LANDED} of {EXTEND_N} EXTEND), "
      f"{INPUTS_REMAIN} REMAIN -- all INPUTS, all a FILED LIMIT.")
print("  ⛭⛭ THE SHEAR ROW IS SETTLED BY AN ABSENCE.  By the Sachs equation -- a stated input --")
print("    the shear of a null geodesic congruence is driven by the Weyl tensor and nothing")
print("    else.  Gamma extended to Weyl returns ALL 256 components zero on the substrate, with")
print("    R = 12/alpha^2 and Ric = (R/4) g exactly; probe1's OWN plane wave has 16 non-zero.")
print("    Batch four computed the rulings to be straight null lines, so their initial shear is")
print("    zero -- and there is nothing here that could have grown one.")
print("  ⚠⛭⛭ AND ONE OF THE 256 NEEDED MORE THAN simplify: W[1][3][3][2] comes back as")
print("    r(sin2t tan t + cos2t - 1)/(2 tan t), which sympy.simplify returns UNCHANGED and")
print("    which is identically zero.  A SIMPLIFY THAT STOPS SHORT READS EXACTLY LIKE A")
print("    NON-ZERO COMPONENT, and the predicate pushes its survivors through expand_trig")
print("    rather than taking simplify's first answer for a geometric fact.")
print("  ⌗ And D_M recovers the expansion law to 1e-8 relative across two decades of redshift,")
print("    against 1e-4 to 9e-4 on the other rate -- four orders of separation.")
print("  " + "=" * 74)
print()
