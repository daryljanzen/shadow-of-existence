#!/usr/bin/env python3
"""C75 -- `r7283` ① BATCH FOUR: **NINE SCHEDULED, NINE TAKEN — AND THE LOADER NOW REFUSES AN
EMPTY TABLE IT USED TO HAND BACK IN SILENCE, WHICH WOULD HAVE MADE A ROW VACUOUS RATHER THAN
WRONG.**

** THE ORDER. **  `r7283` ①: "The remaining `27`, in batches as you have been scheduling them
from the syntax tree.  Your schedule from the syntax tree has been right four times; I am not
re-deciding it."

** ⓵ FOUR PAIRS, NINE ROWS, NOTHING HELD. **  `L128b: diag_at` takes the two flat-bundle rows,
`L50b: key_of` with `apply` takes the two discreteness rows and the hop, `r7111: curvature`
takes the two `P15` rows, `panelA_reassign: ruling` takes the two `P1` rows.  `32` + `9` = `41`
of `59`.

** ⚠⛭⛭⛭ ⓶ AND THE PART THAT IS NOT A ROW COUNT: THE LOADER COULD RETURN AN EMPTY TABLE AND SAY
NOTHING. **  `L50b` binds `ends = {}` and `L128b` binds `leg_wall = {}` at top level, and both
fill them in a `for` loop — which is not a graftable statement kind.  *So the graft saw the
binding, kept it, dropped the loop, and handed back an EMPTY dict.*
  *** A row taken through `ends` would have been VACUOUS RATHER THAN WRONG, and that is the
  worse of the two failures because it PASSES. ***  ⇒ `graft.py` now refuses a kept binding to
  an empty container that a non-graftable statement fills, naming the name and the line.
  ⌗ ** And the measurement that says not to build the loop-keeping capability instead: of the
  `30` rows outstanding AFTER this batch, the named function grafts ON ITS OWN in `23`; of the
  other `7`, three read a module-level name nothing graftable binds and four are the
  nested-function limit already filed at `r7267` ③.  NOT ONE of the `30` needs a filled
  container. **
  ⌗ ⚠ *The figure `0323b526` pushed was `27` of `30`, measured on the pre-batch set, which
  counted batch four's own nine as outstanding and batch two's nine HELD rows as settled.  On
  the set that is actually outstanding the figure is `23`, and the `4` nested-function rows it
  adds were already filed as a stated limit rather than as owed work.*  *The six ends
  are rebuilt from `L50b`'s own `theta`, `A` and `sq3` and GATED on `L50b`'s own substrate
  equation, so the rebuild is checked rather than trusted.*

** ⛭⛭ ⓷ AND A REACHABLE CONVERSE SHARPENED A PREDICATE, WHICH IS THE RULE EARNING ITS KEEP. **
`The constant-tau slice is exactly flat` read off the SCALAR curvature would have **PASSED on
the Schwarzschild spatial slice**, whose `Rs` is `0` and whose Kretschmann is `6 r_s^2/r^6`.
*The converse did not fail the row — it found the predicate reading a quantity that does not
separate flat from Ricci-flat.*  The predicate reads the Kretschmann invariant, and that slice
is recorded as the converse that exposed it.

** ⛭ ⓸ TWO DOUBTS WERE CHECKED BEFORE THE ROWS WERE TAKEN, because batch two's `B39` showed the
backlog can name a function one notch off the quantity. **  Both resolved in the rows' favour:
`key_of` with `apply` reaches BOTH halves of `is a discrete horn swap` — the swap as three
2-cycles each joining one hinge's two ends, and its order `2` inside a group of order `12`; and
`ruling` is the quadric's two straight-line families, with the converse named in the module's
OWN docstring (`a=b=alpha => null rulings = light cone`).

WHAT IS NOT CLAIMED.  ** Not that the plaquette is the only form flatness has ** -- it is the
form a connection given by monodromies has, and the winding-one holonomy is reported beside it
so `flat` is visibly not `trivial`.  ** Not that three stations is explained here ** -- the
five-station converse shows `a hop to a NEIGHBOURING hinge` is a fact about there being three,
and that is recorded as the converse and not as a new claim.  ** Not that any pin moves ** --
the pin is the citation and the computation the verification, as in all three earlier batches.

Run: python3 C75_....py
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
             'REACHED_B3.tsv': '09175ad4094c4fef', 'REACHED_B4.tsv': 'ed53a9d99621d9a8'}

INPUTS_N = 59
B1_N, B2_N, B3_N, B4_N = 19, 4, 9, 9
LANDED, REMAIN = 41, 18
OUTSTANDING = 30                 # the 18 INPUTS still open plus the 12 EXTEND behind them
L128B = 'baryon_edge/L128b_leg_and_arc.py'
L50B = 'baryon_edge/L50b_three_hinges_six_ends.py'
GEOM = 'beyond_the_wall/r7111_70_layer_geometry_audit/geometry.py'
PANELA = 'synthesis_figure/panelA_reassign.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import flat_ruled_and_discrete as F                                        # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
B1 = tsv(MINE, 'REACHED.tsv')[1:]
B2 = tsv(MINE, 'REACHED_B2.tsv')[1:]
B3 = tsv(MINE, 'REACHED_B3.tsv')[1:]
B4 = tsv(MINE, 'REACHED_B4.tsv')[1:]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']
EXTEND = [r for r in BAK if r[6] == 'EXTEND']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the FOUR batches partition what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the `INPUTS` class is still {INPUTS_N} rows", len(INPUTS) == INPUTS_N)
_k1 = {(r[0], r[1]) for r in B1}
_k2 = {(r[1], r[2]) for r in B2 if r[0] == 'TAKEN'}
_k3 = {(r[0], r[1]) for r in B3}
_k4 = {(r[0], r[1]) for r in B4}
_sets = (_k1, _k2, _k3, _k4)
gate(f"Ⓐ④  the four batches take {B1_N} + {B2_N} + {B3_N} + {B4_N} = {LANDED} rows and the four "
     f"key sets are PAIRWISE DISJOINT, so nothing is counted twice",
     [len(s) for s in _sets] == [B1_N, B2_N, B3_N, B4_N]
     and all(not (_sets[i] & _sets[j]) for i in range(4) for j in range(i + 1, 4))
     and B1_N + B2_N + B3_N + B4_N == LANDED)
gate(f"Ⓐ⑤  {LANDED} + {REMAIN} == {INPUTS_N}: landed and remaining partition the class",
     LANDED + REMAIN == INPUTS_N)
_bk = {(r[0], r[1]) for r in INPUTS}
gate("Ⓐ⑥  every batch-four row is a key the BACKLOG carries, and names the function it names",
     all((r[0], r[1]) in _bk for r in B4)
     and all(next(q[5] for q in INPUTS if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B4))
gate(f"Ⓐ⑦  and the outstanding work is {REMAIN} `INPUTS` plus {len(EXTEND)} `EXTEND` = "
     f"{OUTSTANDING} rows, which is the denominator the capability measurement uses",
     REMAIN + len(EXTEND) == OUTSTANDING and len(EXTEND) == 12)

# =========================================================================================
head('Ⓑ  THE GRAFTS -- four scripts, five functions, no module report run')
# =========================================================================================
for _m, _f, _lo, _hi in ((L128B, 'diag_at', 2, 8), (L50B, 'key_of', 2, 8),
                         (L50B, 'apply', 2, 8), (GEOM, 'curvature', 2, 8),
                         (PANELA, 'ruling', 2, 8)):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓑ  `{_m.split('/')[-1]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements",
         _lo <= _g['_STATEMENTS'] <= _hi and _g['_OF'] > 20 and callable(_g[_f]))
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); '
     'import flat_ruled_and_discrete as F; F.bundle_is_flat(); F.six_ends(); '
     'F.doubly_ruled_by_straight_null_lines()' % MINE],
    capture_output=True, text=True, timeout=900)
gate("Ⓑ⑥  ** and the grafts PRINT NOTHING in a fresh interpreter, so none of the four modules' "
     "own reports ran -- including the one that would have written a figure to disk **",
     _probe.returncode == 0 and _probe.stdout == '')
gate("Ⓑ⑦  and each named function is a top-level `def` in its module, proved from the syntax "
     "tree -- which is why this batch holds nothing",
     all(_f in {n.name for n in ast.parse(open(os.path.join(ROOT, 'computations', _m),
                                               encoding='utf-8').read()).body
               if isinstance(n, ast.FunctionDef)}
         for _m, _f in ((L128B, 'diag_at'), (L50B, 'key_of'), (L50B, 'apply'),
                        (GEOM, 'curvature'), (PANELA, 'ruling'))))

# =========================================================================================
head('Ⓒ  ⚠⛭⛭⛭ THE REFUSAL THE LOADER DID NOT HAVE -- an empty table returned in silence')
# =========================================================================================
_hollow = []
for _m, _nm in ((L50B, 'ends'), (L128B, 'leg_wall')):
    _tree = ast.parse(open(os.path.join(ROOT, 'computations', _m), encoding='utf-8').read())
    _binds = [s for s in _tree.body if GRAFT._is_empty_container(s)
              and _nm in GRAFT._bound_by(s)]
    _fills = [s for s in _tree.body if not isinstance(s, GRAFT._KEEP)
              and _nm in GRAFT._mutates_elsewhere(s)]
    _hollow.append(bool(_binds) and bool(_fills))
gate("Ⓒ①  ** both modules bind the table as an EMPTY container at top level AND fill it in a "
     "statement the graft does not keep, proved from each module's own syntax tree **",
     all(_hollow))
_refused = []
for _m, _nm in ((L50B, 'ends'), (L128B, 'leg_wall')):
    try:
        GRAFT.graft(_m, 'key_of' if 'L50b' in _m else 'diag_at', extra=(_nm,))
        _refused.append(False)
    except GRAFT.GraftError as _e:
        _refused.append(_needle('EMPTY', ' container') in str(_e) and _nm in str(_e))
gate("Ⓒ②  ** and the loader now REFUSES both by name rather than handing back an empty dict, "
     "which is what would have made a row VACUOUS RATHER THAN WRONG **", all(_refused))
_pairs, _own, _other = set(), 0, 0
_done = {(r[0], r[1]) for r in B1} | {(r[1], r[2]) for r in B2 if r[0] == 'TAKEN'} \
    | {(r[0], r[1]) for r in B3} | {(r[0], r[1]) for r in B4}
for _r in BAK:
    if _r[6] in ('INPUTS', 'EXTEND') and (_r[0], _r[1]) not in _done:
        _pairs.add((_r[4], _r[5]))
_counts = {}
for _r in BAK:
    if _r[6] in ('INPUTS', 'EXTEND') and (_r[0], _r[1]) not in _done:
        _counts[(_r[4], _r[5])] = _counts.get((_r[4], _r[5]), 0) + 1
_hollow_needed = 0
for (_m, _f), _n in _counts.items():
    try:
        GRAFT.graft(_m, _f)
        _own += _n
    except GRAFT.GraftError as _e:
        _other += _n
        if _needle('EMPTY', ' container') in str(_e):
            _hollow_needed += _n
    except Exception:
        _other += _n
gate(f"Ⓒ③  ** the measurement that says NOT to build the loop-keeping capability: of the "
     f"{OUTSTANDING} rows outstanding AFTER this batch the named function grafts ON ITS OWN in "
     f"{_own}, the other {_other} fail on causes already filed, and NOT ONE needs a filled "
     f"container **",
     _own + _other == OUTSTANDING and _hollow_needed == 0 and _own == 23 and _other == 7)
gate("Ⓒ④  and the six ends are rebuilt and GATED on `L50b`'s own substrate equation "
     "-X0^2 + X1^2 + X2^2 = A^2, so the rebuild is checked and not trusted",
     F.ends_are_on_the_substrate() and len(F.six_ends()) == 6)
gate("Ⓒ⑤  the refusal is additive: every function the three earlier batches grafted still "
     "grafts, so no landed row is withdrawn by this guard",
     all(callable(GRAFT.graft(_m, _f)[_f]) for _m, _f in (
         ('baryon_edge/L006w_the_d5_fourfold.py', 'twoM'),
         ('baryon_edge/L129_the_invariants.py', 'close'),
         ('beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py', 'lie_g'),
         ('baryon_edge/L012w_the_two_splits.py', 'roots_at'))))

# =========================================================================================
head('Ⓓ  THE NINE -- and the one whose converse sharpened the predicate')
# =========================================================================================
gate(f"Ⓓ①  all {B4_N} rows come back with the claim TRUE", all(r[4] == 'TRUE' for r in B4))
gate(f"Ⓓ②  and all {B4_N} come back FALSE on their recorded converse",
     all(r[6] == 'FALSE' for r in B4))
gate("Ⓓ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[5].split()) >= 5 for r in B4) and all(any(c.isdigit() for c in r[7]) for r in B4))
import sympy as _sp                                                        # noqa: E402
gate("Ⓓ④  `L128b`'s own `diag_at` gives a flat bundle: the plaquette round two walls in both "
     "orders is the identity, and so is the zero-winding class",
     F.bundle_is_flat() and F.plaquette() == _sp.eye(3))
gate("Ⓓ⑤  ** and flat is not TRIVIAL: on a winding-one loop the holonomy is a primitive cube "
     "root of unity, so the predicate is not vacuously true **",
     F.flat_is_not_trivial() and _sp.simplify(F.holonomy((1, 0, 0))[0, 0] ** 3) == 1)
gate("Ⓓ⑥  and the converse is reachable: give one wall a NON-diagonal monodromy of the same "
     "order 3 and the plaquette stops being the identity, so the holonomy is path-dependent",
     not F.nonabelian_converse())
gate("Ⓓ⑦  the horn swap is a map of the six ends -- a fixed-point-free involution whose three "
     "2-cycles each join ONE hinge's two ends -- and it is DISCRETE, of order 2 in a group of "
     "order 12",
     F.swap_is_three_two_cycles() and F.horn_swap_order() == 2
     and F.group_order_under_key_of() == 12)
gate("Ⓓ⑧  and the converse: the same keying on a ONE-PARAMETER rotation gives 12 distinct keys "
     "in 12 steps and never closes, so `discrete` is a predicate and not a label",
     F.continuous_converse() == 12)
gate("Ⓓ⑨  the root transposition sends each moved hinge ONE step at three stations, and TWO "
     "steps at five -- so `a hop to a neighbouring hinge` is a fact about there being three",
     F.every_moved_hinge_is_a_neighbour(3) and not F.every_moved_hinge_is_a_neighbour(5))
gate("Ⓓ⑩  the constant-tau slice of `r7111`'s OWN metric is exactly flat -- Ricci zero, scalar "
     "zero, KRETSCHMANN zero -- with 10 of 27 Christoffels non-zero, so it is not a coordinate "
     "accident",
     F.slice_is_exactly_flat() and F.slice_christoffels_nonzero() == 10)
_rs, _k = F.ricci_flat_converse()
gate("Ⓓ⑪  ** and the converse SHARPENED the predicate: the Schwarzschild spatial slice has "
     "scalar curvature 0 and Kretschmann 6 r_s^2/r^6, so a predicate reading the SCALAR would "
     "have passed it -- which is why this one reads the invariant **",
     _rs == 0 and _sp.simplify(_k) != 0 and F.sphere_converse() == 6)
_seam, _at_seam, _at_zero = F.seam_is_finite_and_the_origin_is_not()
gate("Ⓓ⑫  the SdS seam is a root of `f` at finite positive radius where the Kretschmann "
     "invariant is FINITE, while at r -> 0 the same invariant diverges",
     _seam > 0 and _at_seam < float('inf') and _at_zero == _sp.oo)
gate("Ⓓ⑬  both ruling families lie on the quadric, are straight, and are NULL in the ambient "
     "signature -- all three to better than 1e-12",
     F.doubly_ruled_by_straight_null_lines() and max(F.ruling_residuals()) < 1e-12)
_PANELA_SRC = open(os.path.join(ROOT, 'computations', PANELA), encoding='utf-8').read()
gate("Ⓓ⑭  and the converse the module's OWN docstring names -- READ here rather than attributed, "
     "since a claim about a source is worth only as much as opening it: make the quadric "
     "non-equilateral and the tangent norm stops vanishing, so the lines are no longer null",
     F.ruling_residuals(b=1.5)[2] > 1.0
     and _has(_PANELA_SRC, 'a=b=alpha', ' => null rulings'))
gate("Ⓓ⑮  every line of BOTH families meets each at-rest slice exactly once, so that slicing "
     "inherits both rulings; slicing by planes through the axis does not, because a line lies "
     "IN one slice rather than meeting it",
     F.slicing_inherits_both_rulings(2, 0.5)
     and not F.slicing_inherits_both_rulings(0, 0.5)
     and set(F.crossings_per_line(2, 0.5)) == {1})

# =========================================================================================
head('Ⓕ  THE HOLDERS -- the computation is in the holder, and the pin stands beside it')
# =========================================================================================
_holders = sorted({r[0] for r in B4})
WITHHELD = (P15R := 'receipts/P15_CR_cosmology/P15_the_rate_rule_reaches_the_projection_only_'
            'through_the_identification_because_P7_gives_the_lapse_the_rate_and_the_shift_the_'
            'appearance_as_distance.py')
gate(f"Ⓕ①  the {B4_N} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 8 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_withheld_src = open(os.path.join(ROOT, WITHHELD), encoding='utf-8').read()
gate("Ⓕ②  ⚠⛭⛭ ** ONE of the eight is WITHHELD AND ROUTED RATHER THAN EDITED: it carries a "
     "standing gate asserting that it COMPUTES NOTHING, `which is what the order asked for`. "
     "A computed check would make that gate's own label false while its predicate still "
     "passed -- the store-live-state shape again -- and `r7283` ① is a LATER order than the "
     "one that gate cites, so the conflict is 66's to rule and not mine to resolve by editing "
     "another seat's claim **",
     _has(_withheld_src, 'computes ', 'NOTHING') and '_r7283' not in _withheld_src)
_holders = [h for h in _holders if h != WITHHELD]
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B4 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate(f"Ⓕ③  each of the other {len(_holders)} holders defines `_r7283` at its own top level, "
     f"from each file's syntax tree", not _bad_def)
gate("Ⓕ④  ** and calls it inside a `check` or `gate`, so the holder itself computes it **",
     not _bad_call)
gate("Ⓕ⑤  and every row's literal is STILL a string constant of its holder -- the pin is the "
     "citation and this batch removed none",
     not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _holders]
gate(f"Ⓕ⑥  all {len(_holders)} edited holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓕ⑦  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓕ⑧  ⚠ and NONE of the eight is a receipt `S14` pins by line number -- it pins `B1` and "
     "`B2`, and neither is in this batch, so no injection target moves",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & set(_holders)))

# =========================================================================================
head('Ⓖ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine = [n.left.value for n in ast.walk(_self)
         if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
         and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
         and len(n.left.value.split()) > 3]
gate("Ⓖ①  ** no string constant of more than three words sits on the left of an `in` test "
     "anywhere in this file, proved from its OWN syntax tree **", not _mine)
gate("Ⓖ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓖ③  and the ordered work cannot exhaust its subject: {LANDED} of {INPUTS_N}, {REMAIN} "
     f"remaining, with the {len(EXTEND)} `EXTEND` rows behind all of them",
     LANDED < INPUTS_N and REMAIN > 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** BATCH FOUR IS NINE OF NINE, AND THE LOADER GREW A REFUSAL. **")
print(f"  ⛭⛭⛭ {LANDED} OF {INPUTS_N} LANDED, {REMAIN} REMAIN.")
print("  ⚠⛭⛭⛭ THE LOADER COULD RETURN AN EMPTY TABLE AND SAY NOTHING.  L50b binds `ends = {}`")
print("    and L128b binds `leg_wall = {}` at top level and fill them in a `for` loop, which is")
print("    not a graftable statement kind -- so the graft kept the binding, dropped the loop and")
print("    handed back an empty dict.  A row taken through it would have been VACUOUS RATHER")
print("    THAN WRONG, which is the worse failure because it passes.  The loader now refuses")
print("    that case by name and line, and the refusal is additive: every earlier graft stands.")
print("  ⛭⛭ AND NOT ONE OF THE 30 ROWS OUTSTANDING AFTER THIS BATCH NEEDS A FILLED CONTAINER --")
print("    23 of their named functions graft on their own, three of the other seven read a")
print("    module-level name nothing graftable binds, and four are the nested-function limit")
print("    already filed -- so the refusal is the whole of the fix and the loop-keeping")
print("    capability is not built.")
print("  ⛭⛭ AND A CONVERSE SHARPENED A PREDICATE RATHER THAN FAILING A ROW: `the constant-tau")
print("    slice is exactly flat` read off the SCALAR curvature would have passed on the")
print("    Schwarzschild spatial slice, whose Rs is 0 and whose Kretschmann is 6 r_s^2/r^6.")
print("    The predicate reads the invariant, and that slice is the recorded converse.")
print("  " + "=" * 74)
print()
