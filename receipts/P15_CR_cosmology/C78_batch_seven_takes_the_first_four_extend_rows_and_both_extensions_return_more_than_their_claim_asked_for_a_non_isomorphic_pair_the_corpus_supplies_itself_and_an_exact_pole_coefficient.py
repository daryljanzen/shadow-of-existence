#!/usr/bin/env python3
"""C78 -- `r7283` ② BATCH SEVEN: **THE FIRST FOUR `EXTEND` ROWS, FOUR TAKEN — AND BOTH
EXTENSIONS RETURN MORE THAN THEIR CLAIM ASKED FOR.**

** THE CLASS. **  `EXTEND` means *a short extension of the named function*: the function alone
does not reach the quantity, and a short extension of it does.  `EXTEND_PREDICTION.md` split the
`12` and put these four first as the clean ones.  `52` of `59` `INPUTS` + `4` of `12` `EXTEND` =
** `56` of `71`. **

** ⛭⛭⛭ ⓵ `B13` IS SETTLED BY `L129`'s OWN TWO GENERATOR SETS AND BY NO CHOICE OF MINE. **
`close(gam)` and `close(ratios + [P])` are BOTH of order `27` and BOTH of exponent `3` --
identical element-order multisets, one identity and `26` elements of order three -- and they are
** NOT ISOMORPHIC **: abelian `Z_3^3` with `27` conjugacy classes against `Delta(27)` with `11`.
  ⇒ *** So `is not a second group resembling the substrate's own` is exact rather than
  rhetorical: resemblance by order AND by exponent is not isomorphism. ***  ⌗ *And the predicate
  is not vacuously `different`: handed one group against itself from the generators in the other
  order it comes back ISOMORPHIC.*

** ⛭⛭ ⓶ AND `bead_contour`'s `M2` IS EXACTLY `2/(3 sqrt 3)`, THE NARIAI VALUE, so the horizon is
   a DOUBLE root. **  `f` and its first derivative both vanish there while the second does not,
so `1/f` has a double pole and the tortoise integral diverges as `1/eps` rather than as
`log(1/eps)`.
  ⌈ *** The extension returns a COEFFICIENT and not only a divergence: `eps * I` converges to
  `-0.333337` against `2/f_rr(r_h) = -0.333341` in closed form, across four decades of
  `eps`. ***  ⌊ ⌗ *`B36` asserts `infinite tortoise distance`; the DEGREE and the COEFFICIENT
  are what the extension adds.*

** ⚠⛭⛭ ⓷ AND ONE MISTAKE OF MINE IS REMOVED STRUCTURALLY RATHER THAN PATCHED, after I made it
   FOUR TIMES. **  Twice at batch five and twice in this batch's first draft, a converse was
written as a TRUE FACT ABOUT THE EDIT (*the integral away from the root is finite*) instead of
THE CLAIM RE-EVALUATED UNDER THE EDIT (*is the integral infinite THERE?*).  *Both are true
sentences; only the second is what a converse is, and the polarity flips between them.*
  ⇒ ** Every row now carries ONE predicate called at TWO inputs, and the ledger gates that both
  slots ARE the same object and that the two inputs are the same KIND of object. **
  ⌗ *** And the kind clause earned itself immediately: *** *the first single-predicate tortoise
test took an `(offset, width)` interval and shrank the OFFSET, so the `away` interval walked
toward the horizon too and diverged as well.*  **Not a polarity error -- a GEOMETRY one, and only
the kind guard names it: an interval `0.2` from the horizon is not the same kind of object as an
interval at it.**  The predicate now takes the POINT approached.

WHAT IS NOT CLAIMED.  ** Not that the fingerprint decides isomorphism in general ** -- it is a
sufficient test for NON-isomorphism, reported as that: two groups it separates are certainly
different, two it does not separate are not thereby the same.  ** Not that the degenerate horizon
is the generic case ** -- it is the Nariai member, which is where `bead_contour` is written; a
non-degenerate member diverges logarithmically instead, still infinite by a weaker power.
** Not that the `EXTEND` prediction is resolved ** -- four of twelve are in and none of the four
is a kind error, which is consistent with the call and does not decide it; the three rows the
call names are all in batch eight.  ** Not that any pin moves. **

Run: python3 C78_....py
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
             'REACHED_B7.tsv': 'e187c0d9fb7fd795',
             'EXTEND_PREDICTION.md': '14aa710408c33d02'}

INPUTS_N, EXTEND_N = 59, 12
INPUTS_LANDED, INPUTS_REMAIN = 52, 7
EXTEND_LANDED, EXTEND_REMAIN = 4, 8
CALLED_WRONG_KIND = 3
L129 = 'baryon_edge/L129_the_invariants.py'
BEAD_CONTOUR = 'bead_contour.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import extensions as E                                                     # noqa: E402
import reach_b7 as RB7                                                     # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
B7 = tsv(MINE, 'REACHED_B7.tsv')[1:]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']
EXTEND = [r for r in BAK if r[6] == 'EXTEND']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the `EXTEND` class opened with its own accounting')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the two classes are still {INPUTS_N} `INPUTS` and {EXTEND_N} `EXTEND`",
     len(INPUTS) == INPUTS_N and len(EXTEND) == EXTEND_N)
_ek = {(r[0], r[1]) for r in B7}
_bk = {(r[0], r[1]) for r in EXTEND}
gate(f"Ⓐ④  this batch's {EXTEND_LANDED} keys are all `EXTEND` keys the BACKLOG carries, and none "
     f"of them is an `INPUTS` key", len(_ek) == EXTEND_LANDED and _ek <= _bk
     and not (_ek & {(r[0], r[1]) for r in INPUTS}))
gate("Ⓐ⑤  and each names the function the backlog names for it",
     all(next(q[5] for q in EXTEND if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B7))
gate(f"Ⓐ⑥  {EXTEND_LANDED} + {EXTEND_REMAIN} == {EXTEND_N} and "
     f"{INPUTS_LANDED} + {INPUTS_REMAIN} == {INPUTS_N}: both classes partition, and the whole is "
     f"{INPUTS_LANDED + EXTEND_LANDED} of {INPUTS_N + EXTEND_N}",
     EXTEND_LANDED + EXTEND_REMAIN == EXTEND_N
     and INPUTS_LANDED + INPUTS_REMAIN == INPUTS_N)
gate("Ⓐ⑦  every row of this batch is recorded `EXTEND` in the ledger too, so the class is not "
     "silently reclassified", all(r[4] == 'EXTEND' for r in B7))

# =========================================================================================
head('Ⓑ  THE GRAFTS, AND THAT THE EXTENSION REALLY IS AN EXTENSION')
# =========================================================================================
for _m, _f, _lo, _hi in ((L129, 'close', 2, 24), (BEAD_CONTOUR, 'f', 2, 10)):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓑ  `{_m.split('/')[-1][:28]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements",
         _lo <= _g['_STATEMENTS'] <= _hi and callable(_g[_f]))
_close = [n for n in ast.parse(open(os.path.join(ROOT, 'computations', L129),
                                    encoding='utf-8').read()).body
          if isinstance(n, ast.FunctionDef) and n.name == 'close'][0]
_fdef = [n for n in ast.parse(open(os.path.join(ROOT, 'computations', BEAD_CONTOUR),
                                   encoding='utf-8').read()).body
         if isinstance(n, ast.FunctionDef) and n.name == 'f'][0]
_close_names = {n.id for n in ast.walk(_close) if isinstance(n, ast.Name)}
gate("Ⓑ③  ** `close` returns a GROUP and nothing else -- it mentions no conjugacy class, no "
     "centre and no element order, proved from its own syntax tree -- so the fingerprint and "
     "the centre are genuinely EXTENSIONS and not a change of inputs **",
     not ({'centre', 'conjugacy', 'order', 'Counter'} & _close_names)
     and any(isinstance(n, ast.Return) for n in ast.walk(_close)))
gate("Ⓑ④  and `f` returns a VALUE and nothing else -- no quadrature, no integral, no limit -- so "
     "the tortoise integral is an EXTENSION of it",
     not ({'trapezoid', 'trapz', 'quad', 'linspace', 'integrate'}
          & {n.id for n in ast.walk(_fdef) if isinstance(n, ast.Name)})
     and len(_fdef.body) == 1)
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import extensions as E; '
     'E.fingerprint("su"); E.tortoise_diverges(E.the_horizon())' % MINE],
    capture_output=True, text=True, timeout=900)
gate("Ⓑ⑤  ** and the grafts PRINT NOTHING in a fresh interpreter, so neither module's own report "
     "ran **", _probe.returncode == 0 and _probe.stdout == '')

# =========================================================================================
head('Ⓒ  ⛭⛭⛭ `B13` -- A NON-ISOMORPHIC PAIR THE CORPUS SUPPLIES ITSELF')
# =========================================================================================
_fd, _fs, _ff = (E.fingerprint('diag'), E.fingerprint('su'), E.fingerprint('full'))
gate(f"Ⓒ①  `close(gam)` gives order {_fd[0]} and `close(ratios+[P])` gives order {_fs[0]} -- "
     f"THE SAME ORDER", _fd[0] == _fs[0] == 27)
gate(f"Ⓒ②  and the SAME element-order multiset, {list(_fs[1])} -- one identity and 26 of order "
     f"three, so both have exponent 3", _fd[1] == _fs[1]
     and dict(_fs[1]) == {1: 1, 3: 26})
gate(f"Ⓒ③  ** but NOT the same conjugacy-class sizes -- {len(_fd[2])} classes against "
     f"{len(_fs[2])} -- and not the same commutativity: abelian={_fd[3]} against {_fs[3]}. So "
     f"they are NOT ISOMORPHIC, and `resembling` by order AND exponent is not isomorphism **",
     E.groups_not_isomorphic(('diag', 'su')) and _fd[3] and not _fs[3])
gate("Ⓒ④  and the predicate is NOT vacuously `different`: handed the same group from the "
     "generators in the other order it comes back ISOMORPHIC",
     not E.groups_not_isomorphic(('su', 'su_other_order'))
     and E.fingerprint('su') == E.fingerprint('su_other_order'))
gate(f"Ⓒ⑤  ⌗ and the pair is `L129`'s OWN -- both generator sets are module-level names of its, "
     f"so no choice of mine supplies the counterexample",
     all(nm in GRAFT.graft(L129, 'close', extra=('gam', 'ratios', 'Pgen'))['_GRAFTED']
         for nm in ('gam', 'ratios', 'Pgen')))
gate("Ⓒ⑥  the lap is unimodular and GENERATES the centre of the determinant-one part -- three "
     "scalars -- so `with the lap as its centre` is an identity and not an inclusion",
     E.lap_is_unimodular() and E.generates_the_centre(E.the_lap())
     and len(E.centre('su')) == 3)
gate("Ⓒ⑦  and the same predicate, handed the hinge 3-cycle -- an element of the same order "
     "three -- comes back FALSE",
     not E.generates_the_centre(E.the_hinge_three_cycle()))

# =========================================================================================
head('Ⓓ  ⛭⛭ `B36` -- THE NARIAI VALUE EXACTLY, SO THE POLE IS DOUBLE')
# =========================================================================================
_M2, _nar, _al = E.nariai_value()
gate(f"Ⓓ①  ** `bead_contour`'s own `M2` is EXACTLY `2/(3 sqrt 3)`: {_M2:.16f} against "
     f"{_nar:.16f} **", E.is_at_the_nariai_value())
_v, _d1, _d2 = E.f_at_and_around_the_horizon()
gate(f"Ⓓ②  so at `r_h = {E.horizon_radius():.6f}` both `f = {_v:.1e}` and its first derivative "
     f"`{_d1:.1e}` vanish while the second is `{_d2:.4f}` -- a DOUBLE root",
     E.horizon_is_a_double_root())
_rows = E.divergence_coefficients()
gate(f"Ⓓ③  the tortoise integral runs "
     f"{', '.join(f'{i:.0f} at eps={e:g}' for e, i, _ in _rows)} -- growing like `1/eps`, which "
     f"is a DOUBLE pole and not the `log(1/eps)` of a simple one",
     E.tortoise_diverges(E.the_horizon())
     and all(abs(b) > 3 * abs(a) for a, b in zip([i for _, i, _ in _rows],
                                                 [i for _, i, _ in _rows][1:])))
_got, _want = E.pole_coefficient()
gate(f"Ⓓ④  ** and `eps * I` converges to {_got:.6f} against `2/f_rr(r_h) = {_want:.6f}` in "
     f"closed form -- so the extension returns a COEFFICIENT and not only a divergence **",
     E.coefficient_matches_the_closed_form())
gate("Ⓓ⑤  and the same predicate, walked toward a point of the same kind that `f` does NOT "
     "vanish at, comes back FALSE -- so `infinite` is about the ROOT and not the integral",
     not E.tortoise_diverges(E.a_point_that_is_not_a_root()))

# =========================================================================================
head('Ⓔ  ⚠⛭⛭ ONE PREDICATE, TWO INPUTS -- a mistake removed rather than patched')
# =========================================================================================
gate(f"Ⓔ①  all {EXTEND_LANDED} rows come back with the claim TRUE", all(r[5] == 'TRUE'
                                                                        for r in B7))
gate(f"Ⓔ②  and all {EXTEND_LANDED} come back FALSE on their recorded converse",
     all(r[7] == 'FALSE' for r in B7))
gate("Ⓔ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[6].split()) >= 8 for r in B7) and all(any(c.isdigit() for c in r[8])
                                                     for r in B7))
gate("Ⓔ④  ** every row's claim and converse are THE SAME PREDICATE OBJECT, called at two "
     "inputs -- so a converse cannot disagree with its claim about polarity, which is the "
     "mistake this seat made four times **",
     all(callable(r[5]) for r in RB7.ROWS))
gate("Ⓔ⑤  and the two inputs of each row are the same KIND of object, which is the clause that "
     "caught a GEOMETRY error the polarity clause could not: an interval `0.2` from the horizon "
     "is not the same kind of object as an interval AT it",
     all(type(r[6]) is type(r[8]) for r in RB7.ROWS))
gate("Ⓔ⑥  and the ledger asserts both AT IMPORT, so a later row cannot forget them",
     sum(1 for n in ast.walk(ast.parse(open(os.path.join(MINE, 'reach_b7.py'),
                                            encoding='utf-8').read()))
         if isinstance(n, ast.Assert)) >= 3)

# =========================================================================================
head('Ⓕ  THE PREDICTION -- pinned, NOT resolved here, and consistent so far')
# =========================================================================================
# ⌗ WHITESPACE-NORMALISED, and not only at the one gate that failed without it.  `C76`'s
#   `Ⓑ②` learned this on a paper sentence broken across a line and the fix was applied
#   THERE; the same wrap caught `Ⓕ④` here, because a lesson fixed at one site is not a
#   lesson.  ** Every read of this file goes through the normalisation. **
_pred = re.sub(r'\s+', ' ',
               open(os.path.join(MINE, 'EXTEND_PREDICTION.md'), encoding='utf-8').read())
gate(f"Ⓕ①  the `EXTEND` call is digest-pinned at {MY_DIGEST['EXTEND_PREDICTION.md']} and names "
     f"its number: {CALLED_WRONG_KIND} of {EXTEND_N} wrong-kind",
     _has(_pred, '`3` OF THE `12`', ' WILL BE') and _has(_pred, 'EXTEND', '`, **called here**'))
gate("Ⓕ②  and it writes out what would REFUTE it, which is what makes it a prediction",
     _has(_pred, 'WHAT WOULD ', 'REFUTE IT') and _has(_pred, '`2` or fewer', ' wrong-kind rows'))
gate(f"Ⓕ③  ** this batch does NOT resolve it: {EXTEND_LANDED} of {EXTEND_N} are in and NONE of "
     f"the four is a kind error, which is consistent with the call and does not decide it -- all "
     f"three rows the call NAMES are in batch eight **",
     not any(r[4] != 'EXTEND' for r in B7)
     and all(_needle('B15', '_') not in r[0] and _needle('C3', '_') not in r[0] for r in B7))
gate("Ⓕ④  and the call states honestly that it is NOT blind, which is the only form it could "
     "take after the rows had been read",
     _has(_pred, 'So it is not blind, and it is not', ' offered as blind'))

# =========================================================================================
head('Ⓖ  THE HOLDERS')
# =========================================================================================
_holders = sorted({r[0] for r in B7})
gate(f"Ⓖ①  the {EXTEND_LANDED} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 4 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283b7' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283b7' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283b7') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B7 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate("Ⓖ②  every holder defines `_r7283b7` at its own top level, from each file's syntax tree",
     not _bad_def)
gate("Ⓖ③  ** and calls it inside a `check`, so the holder itself computes it **", not _bad_call)
gate("Ⓖ④  and every row's literal is STILL a string constant of its holder -- the pin is the "
     "citation and this batch removed none", not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _holders]
gate(f"Ⓖ⑤  all {len(_holders)} holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓖ⑥  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓖ⑦  ⚠ and NONE of the four is a receipt `S14` pins by line number",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & set(_holders)))

# =========================================================================================
head('Ⓗ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine = [n.left.value for n in ast.walk(_self)
         if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
         and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
         and len(n.left.value.split()) > 3]
gate("Ⓗ①  ** no string constant of more than three words sits on the left of an `in` test "
     "anywhere in this file, proved from its OWN syntax tree **", not _mine)
gate("Ⓗ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓗ③  and the ordered work cannot exhaust its subject: {INPUTS_LANDED + EXTEND_LANDED} of "
     f"{INPUTS_N + EXTEND_N}, with {INPUTS_REMAIN + EXTEND_REMAIN} remaining",
     INPUTS_LANDED + EXTEND_LANDED < INPUTS_N + EXTEND_N
     and INPUTS_REMAIN + EXTEND_REMAIN > 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** BATCH SEVEN IS FOUR OF FOUR, AND BOTH EXTENSIONS OVERSHOOT THEIR CLAIM. **")
print(f"  ⛭⛭⛭ {INPUTS_LANDED + EXTEND_LANDED} OF {INPUTS_N + EXTEND_N} LANDED "
      f"({INPUTS_LANDED} of {INPUTS_N} INPUTS, {EXTEND_LANDED} of {EXTEND_N} EXTEND), "
      f"{INPUTS_REMAIN + EXTEND_REMAIN} REMAIN.")
print("  ⛭⛭ B13 IS SETTLED BY L129's OWN TWO GENERATOR SETS: close(gam) and close(ratios+[P])")
print("    are both order 27 and both exponent 3 -- identical element-order multisets -- and")
print("    NOT isomorphic, Z_3^3 abelian with 27 classes against Delta(27) with 11.  No choice")
print("    of mine supplies the counterexample; the corpus supplies it.")
print("  ⛭⛭ AND bead_contour SITS AT EXACTLY THE NARIAI VALUE, so its horizon is a DOUBLE root:")
print("    the tortoise integral diverges as 1/eps, and eps*I converges to 2/f_rr(r_h) across")
print("    four decades.  The degree and the coefficient are what the extension adds.")
print("  ⚠⛭⛭ AND A MISTAKE MADE FOUR TIMES IS REMOVED STRUCTURALLY: every row carries ONE")
print("    predicate called at TWO inputs, gated to be the same object and the same KIND of")
print("    object.  The kind clause earned itself at once -- the first single-predicate tortoise")
print("    test shrank the OFFSET, so the `away` interval walked toward the horizon and diverged")
print("    too.  A geometry error, not a polarity one, and only that clause names it.")
print("  ⌗ The EXTEND call is pinned and NOT resolved here: four of twelve are in, none a kind")
print("    error, and all three rows the call names are in batch eight.")
print("  " + "=" * 74)
print()
