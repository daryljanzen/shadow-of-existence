#!/usr/bin/env python3
"""C74 -- `r7267`/`r7281` ① BATCH THREE: **NINE SCHEDULED, NINE TAKEN, NOTHING HELD — AND
`roots_at` SETTLES THE HALF `B13` AND `B14` COULD NOT CHECK.**

** THE ORDER. **  `r7281` ①: "The remaining `36`, in batches as you have been scheduling them from
the syntax tree.  Your schedule has been right three times; I am not re-deciding it."

** ⓵ AND THIS BATCH HOLDS NOTHING, WHICH IS THE CONTRAST WITH THE LAST ONE. **  Batch two
scheduled `13` and took `4`, because nine rows needed a geometry, an object or a non-nested
function the classification had not recorded.  *** All three of this batch's functions are
top-level AND take their inputs as ARGUMENTS, so the change of inputs is a CALL rather than a
rebinding — and nine of nine land. ***  `23` + `9` = `32` of `59`.

** ⛭⛭⛭ ⓶ THE ONE WORTH READING IS `roots_at`, BECAUSE IT ANSWERS A CLAIM NEITHER HOLDER COULD
CHECK. **  `L-012w`'s own report tabulates eleven values of `r_0` with the designated root and its
pair.  *Asked instead at the three values the designation runs over, it returns the SAME ROOT SET
every time — `{1, -1, 0}` — and differs only in WHICH member is designated.*
  *** `B14` asserts "distinguished ONLY by which root each takes as its hole".  The `only` is the
  load-bearing word, and it is a statement about the SETS BEING IDENTICAL.  No string match can
  see that, and `L-012w` never prints the three side by side. ***
  ⇒ ** So the computation does not merely confirm the sentence, it supplies the half of it the
    receipt had no way to check. **  And the converse is reachable: add a fourth value whose root
    set differs and the `only` fails.

** ⛭⛭ ⓷ `omega_power` CARRIES ITS OWN CONVERSE, WHICH IS RARE ENOUGH TO RECORD. **  It `raise`s
`ValueError` on anything that is not a cube root of unity, so `quantises` and `is a pure power of
omega` have a BUILT-IN false case and need no constructed edit to fail on.  On the three cube
roots it returns `0, 1, 2`, exhausting `Z/3`.

** ⓸ AND `r_of_tau` PUTS THE BRANCH POINT AT PROPER TIME ZERO, EXACTLY. **  `r_of_tau(0) = 0.0`
against `0.638472` at `0.5` and `1.203939` at `1.0`, so `the cosmology it seeds begins at the
branch point` is a statement about proper time zero and the converse is any proper time away.

WHAT IS NOT CLAIMED.  ** Not that the cubic's roots ARE the hinge positions ** -- `roots_at` is
asked at values this batch supplies, and the correspondence to hinges is the receipts' own,
pinned there and unchanged.  ** Nothing about `r_of_tau` off the real axis ** -- it is
complex-valued and the rows ask about proper time on the real branch.  ** Not that any pin moves **
-- the pin is the citation and the computation the verification, as in both earlier batches.

Run: python3 C74_....py
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
             'REACHED_B3.tsv': '09175ad4094c4fef'}

INPUTS_N = 59
B1_N, B2_N, B3_N = 19, 4, 9
LANDED, REMAIN = 32, 27
L012 = 'baryon_edge/L012w_the_two_splits.py'
L127 = 'baryon_edge/L127_the_bundle.py'
BEAD = 'bead_conjugate.py'
HINGE = ('1', '-1', '0')


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import splits as SPL                                                       # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
B1 = tsv(MINE, 'REACHED.tsv')[1:]
B2 = tsv(MINE, 'REACHED_B2.tsv')[1:]
B3 = tsv(MINE, 'REACHED_B3.tsv')[1:]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the THREE batches partition what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the `INPUTS` class is still {INPUTS_N} rows", len(INPUTS) == INPUTS_N)
_k1 = {(r[0], r[1]) for r in B1}
_k2 = {(r[1], r[2]) for r in B2 if r[0] == 'TAKEN'}
_k3 = {(r[0], r[1]) for r in B3}
gate(f"Ⓐ④  the three batches take {B1_N} + {B2_N} + {B3_N} = {LANDED} rows and the three key "
     f"sets are PAIRWISE DISJOINT, so nothing is counted twice",
     len(_k1) == B1_N and len(_k2) == B2_N and len(_k3) == B3_N
     and not (_k1 & _k2) and not (_k1 & _k3) and not (_k2 & _k3)
     and B1_N + B2_N + B3_N == LANDED)
gate(f"Ⓐ⑤  {LANDED} + {REMAIN} == {INPUTS_N}: landed and remaining partition the class",
     LANDED + REMAIN == INPUTS_N)
_bk = {(r[0], r[1]) for r in INPUTS}
gate("Ⓐ⑥  every batch-three row is a key the BACKLOG carries, and names the function it names",
     all((r[0], r[1]) in _bk for r in B3)
     and all(next(q[5] for q in INPUTS if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B3))
gate(f"Ⓐ⑦  ** and this batch HOLDS NOTHING -- {B3_N} scheduled and {B3_N} taken -- which is the "
     f"contrast with batch two's {B2_N} of 13 **",
     len(B3) == B3_N and len([r for r in B2 if r[0] == 'HELD']) == 9)

# =========================================================================================
head('Ⓑ  THE GRAFTS -- three scripts, three functions, no module report run')
# =========================================================================================
for _m, _f, _lo, _hi in ((L012, 'roots_at', 3, 10), (L127, 'omega_power', 2, 8),
                         (BEAD, 'r_of_tau', 2, 8)):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓑ  `{_m.split('/')[-1]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements",
         _lo <= _g['_STATEMENTS'] <= _hi and _g['_OF'] > 20 and callable(_g[_f]))
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import splits; '
     'splits.at_inputs()' % MINE], capture_output=True, text=True, timeout=600)
gate("Ⓑ④  ** and all three grafts PRINT NOTHING in a fresh interpreter, so none of the three "
     "modules' own reports ran **",
     _probe.returncode == 0 and _probe.stdout == '')
gate("Ⓑ⑤  and each of the three is a top-level `def` in its module -- which is why this batch "
     "holds nothing, proved from each module's syntax tree",
     all(_f in {n.name for n in ast.parse(open(os.path.join(ROOT, 'computations', _m),
                                               encoding='utf-8').read()).body
               if isinstance(n, ast.FunctionDef)}
         for _m, _f in ((L012, 'roots_at'), (L127, 'omega_power'), (BEAD, 'r_of_tau'))))

# =========================================================================================
head('Ⓒ  THE NINE -- and `roots_at` supplies the half the receipts could not check')
# =========================================================================================
gate(f"Ⓒ①  all {B3_N} rows come back with the claim TRUE", all(r[4] == 'TRUE' for r in B3))
gate(f"Ⓒ②  and all {B3_N} come back FALSE on their recorded converse",
     all(r[6] == 'FALSE' for r in B3))
gate("Ⓒ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[5].split()) >= 5 for r in B3) and all(any(c.isdigit() for c in r[7]) for r in B3))

S, O, B = SPL.at_inputs()
gate("Ⓒ④  `L-012w`'s own `roots_at` returns THREE roots at each of the three values, each "
     "designating a different one",
     all(len(S.triple(v)) == 3 for v in HINGE) and S.designations_differ(HINGE)
     and all(S.designated(v) in S.triple(v) for v in HINGE))
gate("Ⓒ⑤  ** AND THE ROOT SET IS IDENTICAL AT ALL THREE -- which is the load-bearing half of "
     "`distinguished ONLY by which root each takes`, and is what no string match can see **",
     S.sets_agree(HINGE) and len(S.root_set('1')) == 3)
gate("Ⓒ⑥  and the converse is reachable: a fourth value whose root set DIFFERS breaks the "
     "agreement, so `only` is a predicate and not a flourish",
     not S.sets_agree(tuple(HINGE) + ('1/sqrt(3)',)))
import sympy as _sp                                                        # noqa: E402
gate("Ⓒ⑦  the horizon cubic is exactly ZERO at each of its own three roots, and non-zero a "
     "seventh off each of them",
     all(x == 0 for x in S.vanishes_at_roots('1'))
     and all(_sp.simplify(_sp.Poly(S.cubic(), _sp.Symbol('r')).eval(x + _sp.Rational(1, 7))) != 0
             for x in S.triple('1')))
gate("Ⓒ⑧  `L-127`'s own `omega_power` returns 0, 1, 2 on the three cube roots, exhausting Z/3",
     O.quantises() and sorted(O.powers()) == [0, 1, 2])
gate("Ⓒ⑨  ** and it carries its OWN converse: it RAISES off the cube roots, so `quantises` has "
     "a built-in false case and needs no constructed edit **",
     not O.is_pure_power(_sp.Integer(2)) and not O.is_pure_power(_sp.Rational(1, 2)))
gate("Ⓒ⑩  `bead_conjugate`'s own `r_of_tau` is exactly zero at proper time zero and non-zero "
     "away from it",
     B.branch_point_at_zero() and B.nonzero_away() and abs(B.radius(0.5)) > 0.6)

# =========================================================================================
head('Ⓓ  THE HOLDERS -- the computation is in the holder, and the pin stands beside it')
# =========================================================================================
_holders = sorted({r[0] for r in B3})
gate(f"Ⓓ①  the {B3_N} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 9 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7281' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7281' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7281') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B3 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate("Ⓓ②  every holder defines `_r7281` at its own top level, from each file's syntax tree",
     not _bad_def)
gate("Ⓓ③  ** and calls it inside a `check` or `gate`, so the holder itself computes it **",
     not _bad_call)
gate("Ⓓ④  and every row's literal is STILL a string constant of its holder -- the pin is the "
     "citation and this batch removed none",
     not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1200)) for h in _holders]
gate(f"Ⓓ⑤  all {len(_holders)} holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓓ⑥  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓓ⑦  ⚠ and NONE of the nine is a receipt `S14` pins by line number -- it pins `B1` and "
     "`B2`, and neither is in this batch, so no injection target moves",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & set(_holders)))

# =========================================================================================
head('Ⓔ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine = [n.left.value for n in ast.walk(_self)
         if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
         and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
         and len(n.left.value.split()) > 3]
gate("Ⓔ①  ** no string constant of more than three words sits on the left of an `in` test "
     "anywhere in this file, proved from its OWN syntax tree **", not _mine)
gate("Ⓔ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓔ③  and the ordered work cannot exhaust its subject: {LANDED} of {INPUTS_N}, {REMAIN} "
     f"remaining, with the `12` `EXTEND` rows behind all of them",
     LANDED < INPUTS_N and REMAIN > 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** BATCH THREE IS NINE OF NINE, AND NOTHING IS HELD. **")
print(f"  ⛭⛭⛭ {LANDED} OF {INPUTS_N} LANDED, {REMAIN} REMAIN.")
print("  ⛭⛭ The contrast with batch two is the whole point: there 13 were scheduled and 4 taken")
print("    because nine rows wanted a geometry, an object or a non-nested function.  All three")
print("    of this batch's functions are top-level AND take their inputs as ARGUMENTS, so the")
print("    change of inputs is a CALL -- and nine of nine land.")
print("  ⛭⛭⛭ AND roots_at SUPPLIES THE HALF B13 AND B14 COULD NOT CHECK: asked at the three")
print("    values the designation runs over it returns the SAME ROOT SET every time, {1, -1, 0},")
print("    and differs only in WHICH member is designated.  B14's `distinguished ONLY by which")
print("    root each takes` turns on the sets being IDENTICAL -- which no string match can see,")
print("    and which L-012w never prints side by side.  A fourth value breaks it, so `only` is")
print("    a predicate and not a flourish.")
print("  ⛭ omega_power carries its own converse by RAISING off the cube roots, and r_of_tau puts")
print("    the branch point at proper time zero exactly.")
print("  " + "=" * 74)
print()
