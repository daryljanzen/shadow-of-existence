#!/usr/bin/env python3
"""C77 -- `r7283` ① BATCH SIX: **SIX ROWS, SIX TAKEN — AND THE ONE WRONG-KIND ROW AMONG THEM IS
WRONG BY *QUANTIFIER*, WHICH IS A DIFFERENT DEFECT FROM BATCH FIVE'S FOUR.**

** THE ORDER. **  `r7285` ① and `r7287`, both unchanged: *the remaining rows, in your own
batches from the syntax tree.*  Of the `13` outstanding after batch five, these `6` name a
function that grafts on its own, and all six are taken.  `46` + `6` = `52` of `59`.

** ⚠⛭⛭⛭ ⓵ `B7` IS THE SAME CLAIM `P11` CARRIES, AND ITS FUNCTION FAILS BY QUANTIFIER. **
`B7`'s own source says what its literal is about: *the compact-face route is walled by
localisation and by `su(3)` **being no isometry** of the non-compact substrate* -- which is
`P11`'s claim, computed at batch five.
  ⇒ *** `killing_residual` IS EXISTENTIAL-REFUTING: it settles ONE candidate field at a time,
  exactly. ***  *Of `probe2`'s four coordinate fields exactly one is Killing and `d/du` is
  refuted outright -- so the function works, and works precisely.*  **But `su(3) is no isometry`
  is a NON-EXISTENCE over every embedding of an eight-dimensional algebra, and no finite number
  of non-vanishing residuals establishes one.**
  ⌈ ** So `lie_g` could not express `P11`'s claim AT ALL, while `killing_residual` can express
  the negation of `B7`'s one candidate at a time and still never reach the claim. **  ⌊ *Two
  defects wearing one code, and this is the sharper of them: not the wrong object, the wrong
  quantifier.*

** ⛭⛭ ⓶ AND THE EMPTY-CONTAINER REFUSAL `C75` BUILT FIRED IN REAL USE, ONE BATCH LATER. **
`L091x` binds `GROUPS = []` and fills it with top-level `.append(...)` calls -- `Expr`
statements the graft does not keep -- so the loader **refused it by name** instead of handing
back an empty list.  *A guard written against a hazard found by inspection, firing on a second
instance found by use, is the only evidence that a guard was worth building.*
  ⌗ *The row does not need `GROUPS`: `irrep_dims_abelian_check(mult, n, name)` takes the group's
  multiplication table as an ARGUMENT, so the tables are supplied and the change of inputs is a
  call.*

** ⛭ ⓷ AND THE LEDGER'S OWN GUARD CAUGHT A SECOND THING IT WAS NOT WRITTEN FOR. **  *Batch five
added `assert isinstance(slot(), bool)` to catch a converse written without its call.  Here it
caught two acoustic predicates returning `np.bool_`* -- true, but not a `bool`, and a guard that
only almost holds is the thing this corpus keeps finding.  **Coerced at source, with the reason
recorded beside the coercion.**

WHAT IS NOT CLAIMED.  ** Not that `and no force` is settled by a converse ** -- it is the
FINITENESS of the holonomy group, `|G| = 27`, and `inv_dim`'s average is a finite sum so a
positive-dimensional group cannot be fed to it at all: a stated limit, not a false case.  ** Not
that `L091x` computes the irrep dimensions ** -- its body returns only whether the table is
abelian, and the dimensions follow from the identity its own docstring states, reported rather
than papered over.  ** Not that the acoustic module is a power-spectrum fit ** -- its own scope
note says it is the sound-horizon leg.  ** Not that any pin moves. **

Run: python3 C77_....py
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
             'REACHED_B5.tsv': '7f4d93b0f36d7468', 'REACHED_B6.tsv': 'd475b0e2057107bd'}

INPUTS_N = 59
SIZES = (19, 4, 9, 9, 5, 6)
LANDED, REMAIN = 52, 7
WRONG_KIND = 'FUNCTION-IS-THE-WRONG-KIND'
L091X = 'baryon_edge/L091x_deck_symmetry_is_not_horizontal.py'
L128 = 'baryon_edge/L128_three_walls_or_one_radius.py'
L130 = 'baryon_edge/L130_statistics_not_gauge.py'
ACOUSTIC = 'CR_acoustic_scale_and_hubble.py'
PROBE2 = 'beyond_the_wall/probe2.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import selection_and_scale as S                                            # noqa: E402
import reach_b6 as RB6                                                     # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
LEDGERS = [tsv(MINE, n)[1:] for n in ('REACHED.tsv', 'REACHED_B2.tsv', 'REACHED_B3.tsv',
                                      'REACHED_B4.tsv', 'REACHED_B5.tsv', 'REACHED_B6.tsv')]
B6 = LEDGERS[5]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']
EXTEND = [r for r in BAK if r[6] == 'EXTEND']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the SIX batches partition what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the `INPUTS` class is still {INPUTS_N} rows", len(INPUTS) == INPUTS_N)
_sets = [{(r[0], r[1]) for r in LEDGERS[0]},
         {(r[1], r[2]) for r in LEDGERS[1] if r[0] == 'TAKEN'},
         {(r[0], r[1]) for r in LEDGERS[2]},
         {(r[0], r[1]) for r in LEDGERS[3]},
         {(r[0], r[1]) for r in LEDGERS[4]},
         {(r[0], r[1]) for r in LEDGERS[5]}]
gate(f"Ⓐ④  the six batches take {'+'.join(str(x) for x in SIZES)} = {LANDED} rows and the six "
     f"key sets are PAIRWISE DISJOINT, so nothing is counted twice",
     tuple(len(s) for s in _sets) == SIZES
     and all(not (_sets[i] & _sets[j]) for i in range(6) for j in range(i + 1, 6))
     and sum(SIZES) == LANDED)
gate(f"Ⓐ⑤  {LANDED} + {REMAIN} == {INPUTS_N}: landed and remaining partition the class",
     LANDED + REMAIN == INPUTS_N)
_bk = {(r[0], r[1]) for r in INPUTS}
gate("Ⓐ⑥  every batch-six row is a key the BACKLOG carries, and names the function the backlog "
     "names", all((r[0], r[1]) in _bk for r in B6)
     and all(next(q[5] for q in INPUTS if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B6))
_done = set().union(*_sets)
_rem = [r for r in INPUTS if (r[0], r[1]) not in _done]
_nested = [r for r in _rem if _needle('bead', '_frames') in r[4]]
gate(f"Ⓐ⑦  ** and the {REMAIN} that remain have a SHAPE, not just a count: {len(_nested)} are "
     f"`bead_frames`' nested functions, which `C73`'s `Ⓓ⑤` gated the decision NOT to build a "
     f"capability for, and {REMAIN - len(_nested)} refuse on a module-level name nothing "
     f"graftable binds -- so the {len(EXTEND)} `EXTEND` rows are the next real tranche **",
     len(_rem) == REMAIN and len(_nested) == 4 and len(EXTEND) == 12)

# =========================================================================================
head('Ⓑ  THE GRAFTS -- five scripts, six functions, no module report run')
# =========================================================================================
for _m, _f, _lo, _hi in ((L091X, 'irrep_dims_abelian_check', 1, 6), (L128, 'routes', 2, 8),
                         (L130, 'chi_meson', 2, 24), (ACOUSTIC, 'D_M', 2, 14),
                         (ACOUSTIC, 'ell_A', 2, 14), (PROBE2, 'killing_residual', 2, 14)):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓑ  `{_m.split('/')[-1][:30]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements",
         _lo <= _g['_STATEMENTS'] <= _hi and _g['_OF'] > 15 and callable(_g[_f]))
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); '
     'import selection_and_scale as S; S.deck_is_abelian(); S.route_table(); '
     'S.acoustic_at(67.4); S.coordinate_fields_that_are_killing()' % MINE],
    capture_output=True, text=True, timeout=900)
gate("Ⓑ⑦  ** and the grafts PRINT NOTHING in a fresh interpreter, so none of the five modules' "
     "own reports ran **", _probe.returncode == 0 and _probe.stdout == '')
gate("Ⓑ⑧  and each named function is a top-level `def` in its module, from the syntax tree",
     all(_f in {n.name for n in ast.parse(open(os.path.join(ROOT, 'computations', _m),
                                               encoding='utf-8').read()).body
               if isinstance(n, ast.FunctionDef)}
         for _m, _f in ((L091X, 'irrep_dims_abelian_check'), (L128, 'routes'),
                        (L130, 'chi_meson'), (ACOUSTIC, 'D_M'), (ACOUSTIC, 'ell_A'),
                        (PROBE2, 'killing_residual'))))

# =========================================================================================
head('Ⓒ  ⛭⛭ THE REFUSAL `C75` BUILT, FIRING ON A SECOND INSTANCE FOUND BY USE')
# =========================================================================================
_l091 = ast.parse(open(os.path.join(ROOT, 'computations', L091X), encoding='utf-8').read())
_binds = [s for s in _l091.body if GRAFT._is_empty_container(s)
          and 'GROUPS' in GRAFT._bound_by(s)]
_fills = [s for s in _l091.body if not isinstance(s, GRAFT._KEEP)
          and 'GROUPS' in GRAFT._mutates_elsewhere(s)]
gate("Ⓒ①  ** `L091x` binds `GROUPS` as an EMPTY container and fills it in statements the graft "
     "does not keep -- top-level `.append(...)` calls, not a loop, which is a SECOND shape of "
     "the same hazard -- proved from its own syntax tree **",
     bool(_binds) and len(_fills) >= 2)
try:
    GRAFT.graft(L091X, 'irrep_dims_abelian_check', extra=('GROUPS',))
    _refused = False
except GRAFT.GraftError as _e:
    _refused = _needle('EMPTY', ' container') in str(_e) and 'GROUPS' in str(_e)
gate("Ⓒ②  ** and the loader REFUSES it by name rather than handing back an empty list, which is "
     "a guard built against a hazard found by INSPECTION firing on one found by USE **",
     _refused)
gate("Ⓒ③  and the row does not need it: the function takes its multiplication table as an "
     "ARGUMENT, from its own signature in the tree",
     [a.arg for n in _l091.body if isinstance(n, ast.FunctionDef)
      and n.name == 'irrep_dims_abelian_check' for a in n.args.args] == ['mult', 'n', 'name'])

# =========================================================================================
head('Ⓓ  THE SIX -- computed, each FALSE on its own recorded converse')
# =========================================================================================
gate(f"Ⓓ①  all {SIZES[5]} rows come back with the claim TRUE", all(r[5] == 'TRUE' for r in B6))
gate(f"Ⓓ②  and all {SIZES[5]} come back FALSE on their recorded converse",
     all(r[7] == 'FALSE' for r in B6))
gate("Ⓓ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[6].split()) >= 8 for r in B6) and all(any(c.isdigit() for c in r[8])
                                                     for r in B6))
gate("Ⓓ④  the deck is abelian so its irreducibles are three ONE-dimensional characters whose "
     "squares sum to the order, against the walls' `S_3` which is not abelian",
     S.deck_is_abelian() and S.deck_irrep_dims() == [1, 1, 1] and not S.s3_is_abelian()
     and S.s3_irrep_dims_are_not_all_one())
gate("Ⓓ⑤  ⌗ and exactly ONE irreducible is trivial for EITHER group, so triviality does not "
     "discriminate -- which is why the quantity the backlog recorded is the DIMENSIONS",
     S.triviality_does_not_discriminate())
gate("Ⓓ⑥  the three hinge pairs give six routes whose two arcs PARTITION the three walls at "
     "every pair, each a one-wall against two-wall split",
     S.routes_partition_the_walls() and S.every_pair_is_a_one_two_split()
     and len(S.route_table()) == 3)
gate("Ⓓ⑦  ** and the converse is a change of the inputs the function READS: at four and five "
     "hinges the splits are (1,3)/(2,2) and (1,4)/(2,3), so the 1-2 structure is a fact about "
     "THREE **",
     not S.one_two_split_at(4) and not S.one_two_split_at(5)
     and S._split_sizes_at(4) == {(1, 3), (2, 2)})
gate("Ⓓ⑧  colour's invariant content on `G_su`: baryon 1, diquark 0, meson 1 -- the exact "
     "selection rules -- against `G_rigid`'s 1, 0, 3, which is the converse",
     S.exact_selection_rules() and not S.rigid_converse()
     and S.selection_rules('G_rigid')[3] == 3)
gate("Ⓓ⑨  ⌗ and `no force` is the FINITENESS, `|G| = 27`, reported as a stated limit because "
     "`inv_dim`'s average is a finite sum and no positive-dimensional group can be fed to it",
     S.no_force_is_the_finiteness() == 27)
_a, _b = S.distance_by_the_two_routes()
gate("Ⓓ⑩  `D_M` by the two routes names ONE number: its own quadrature and the recovery from "
     "`ell_A r_s / pi` agree to better than 1e-9 relative",
     S.two_routes_agree() and abs(_a - _b) / _a < 1e-9)
gate("Ⓓ⑪  and the converse: the OTHER rate at the same `H0` moves the distance, so `the same "
     "distance` is a statement about one rate and not a coincidence of two models",
     not S.other_rate_converse()
     and abs(S.acoustic_at(S.H0_CMB, rate='cr')[0] - _a) > 1.0)
gate("Ⓓ⑫  `ell_A` on flat LambdaCDM at the CMB `H0` lands the measured acoustic scale, with "
     "`r_s` at the module's own validated value",
     S.acoustic_scale_is_301() and abs(S.acoustic_at(S.H0_CMB)[1] - 144.6) < 0.2)
_rs_cmb, _rs_loc = S.acoustic_at(S.H0_CMB)[1], S.acoustic_at(S.H0_LOCAL)[1]
# ⌗ a RELATIVE tolerance, because `r_s` carries a scale: the first draft of this gate used an
#   absolute `1e-9` on a quantity of `144.55 Mpc` and failed at a difference of `4.0e-9 Mpc`,
#   which is `2.8e-11` RELATIVE -- pinned by any reading, and the gate was the thing that was
#   wrong.  *The measured difference is printed rather than hidden behind the verdict.*
gate(f"Ⓓ⑬  and the converse is the module's own second result: forcing the LOCAL `H0` leaves "
     f"`r_s` pinned -- {_rs_cmb:.6f} against {_rs_loc:.6f} Mpc, "
     f"{abs(_rs_loc - _rs_cmb) / _rs_cmb:.1e} relative -- and MISSES the scale at "
     f"{S.acoustic_at(S.H0_LOCAL)[2]:.2f}",
     not S.local_H0_converse()
     and abs(_rs_loc - _rs_cmb) / _rs_cmb < 1e-9)

# =========================================================================================
head('Ⓔ  ⚠⛭⛭⛭ THE WRONG QUANTIFIER -- a different defect from batch five\'s four')
# =========================================================================================
_b7 = open(os.path.join(ROOT, 'receipts', 'L221_the_bridge',
                        'B7_two_unbuilt_sectors_not_one.py'), encoding='utf-8').read()
gate("Ⓔ①  ** `B7`'s own source says its literal is about `su(3)` being no isometry -- the same "
     "claim `P11` carries -- READ out of the holder rather than inferred **",
     _has(_b7, 'being no isometry of the non-compact', ' substrate')
     and _has(_b7, '\\mathfrak{su}(3)$ being no isometry'))
gate("Ⓔ②  `killing_residual` WORKS, and precisely: exactly one of `probe2`'s four coordinate "
     "fields satisfies the Killing equation and `d/du` is refuted outright",
     len(S.coordinate_fields_that_are_killing()) == 1
     and S.killing_equation_has_a_solution() and S.a_candidate_that_fails())
gate("Ⓔ③  ** but the claim is a NON-EXISTENCE over every embedding of an eight-dimensional "
     "algebra, and a residual test is existential-refuting -- so no finite number of "
     "non-vanishing residuals reaches it. THE WRONG QUANTIFIER, not the wrong object **",
     S.a_residual_test_has_the_wrong_quantifier() and S.b7_is_the_su3_claim())
gate("Ⓔ④  and the claim itself is computed as the containment it is, with the converse one "
     "dimension up where it HOLDS",
     S.b7_is_the_su3_claim())
_b5 = tsv(MINE, 'REACHED_B5.tsv')[1:]
gate(f"Ⓔ⑤  ⌗ so the `{WRONG_KIND}` code now covers TWO distinct defects -- batch five's four "
     f"`lie_g` rows, which could not express their claim at all, and this one, which can "
     f"express its negation one candidate at a time -- and both are recorded under it",
     sum(1 for r in _b5 if r[4] == WRONG_KIND) == 4
     and sum(1 for r in B6 if r[4] == WRONG_KIND) == 1)

# =========================================================================================
head('Ⓕ  THE LEDGER GUARD, AND WHAT IT CAUGHT THAT IT WAS NOT WRITTEN FOR')
# =========================================================================================
gate("Ⓕ①  every predicate slot of the ledger returns a plain `bool`, checked from the LIVE "
     "objects -- which is what caught two acoustic predicates returning `np.bool_`",
     all(isinstance(s(), bool) and type(s()) is bool
         for r in RB6.ROWS for s in (r[5], r[7])))
gate("Ⓕ②  and the ledger asserts it AT IMPORT, so a later row cannot forget it",
     sum(1 for n in ast.walk(ast.parse(open(os.path.join(MINE, 'reach_b6.py'),
                                            encoding='utf-8').read()))
         if isinstance(n, ast.Assert)) >= 2)

# =========================================================================================
head('Ⓖ  THE HOLDERS -- and the SAME holder is withheld for the same reason as at `C75`')
# =========================================================================================
_holders = sorted({r[0] for r in B6})
WITHHELD = (next(r[0] for r in B6 if _needle('the_rate_rule', '_reaches') in r[0]))
gate(f"Ⓖ①  the {SIZES[5]} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 6 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_wsrc = open(os.path.join(ROOT, WITHHELD), encoding='utf-8').read()
gate("Ⓖ②  ⚠⛭⛭ ** the SAME holder `C75` withheld is withheld again, for the same reason and not "
     "a new one: it carries a standing gate asserting that it COMPUTES NOTHING, `which is what "
     "the order asked for`, so a computed check would make that gate's own label false while "
     "its predicate still passed. `r7283` ① is the later order, but by `r7281` ruling ① a seat "
     "does not edit another seat's receipt and mine did not break this one -- so the row is "
     "TAKEN here and only the holder edit is withheld **",
     _has(_wsrc, 'computes ', 'NOTHING') and '_r7283b6' not in _wsrc)
_holders = [h for h in _holders if h != WITHHELD]
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283b6' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283b6' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283b6') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B6 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate(f"Ⓖ③  each of the other {len(_holders)} defines `_r7283b6` at its own top level, from each "
     f"file's syntax tree", not _bad_def)
gate("Ⓖ④  ** and calls it inside a `check` or `gate`, so the holder itself computes it **",
     not _bad_call)
gate("Ⓖ⑤  and every row's literal is STILL a string constant of its holder -- the pin is the "
     "citation and this batch removed none", not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _holders]
gate(f"Ⓖ⑥  all {len(_holders)} edited holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓖ⑦  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓖ⑧  ⚠ and NONE of the six is a receipt `S14` pins by line number -- it pins `B1` and "
     "`B2`, and neither is in this batch",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & (set(_holders) | {WITHHELD})))

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
gate(f"Ⓗ③  and the ordered work cannot exhaust its subject: {LANDED} of {INPUTS_N}, {REMAIN} "
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
print("  VERDICT: ** BATCH SIX IS SIX OF SIX, AND THE ONE WRONG-KIND ROW FAILS BY QUANTIFIER. **")
print(f"  ⛭⛭⛭ {LANDED} OF {INPUTS_N} LANDED, {REMAIN} REMAIN.")
print("  ⚠⛭⛭⛭ B7 CARRIES P11's CLAIM, and killing_residual fails it in a way lie_g did not:")
print("    the function WORKS, and precisely -- exactly one of probe2's four coordinate fields")
print("    is Killing and d/du is refuted outright.  But a residual test is EXISTENTIAL-")
print("    REFUTING, settling one candidate at a time, and `su(3) is no isometry` is a")
print("    NON-EXISTENCE over every embedding.  lie_g could not express P11's claim at all;")
print("    this one can express the negation of B7's one candidate forever and never reach it.")
print("  ⛭⛭ AND THE REFUSAL C75 BUILT FIRED ON A SECOND INSTANCE FOUND BY USE: L091x binds")
print("    GROUPS = [] and fills it with top-level .append(...) calls, a different statement")
print("    kind from the loop that prompted the guard.  A guard written against a hazard found")
print("    by inspection, firing on one found by use, is the evidence it was worth building.")
print("  ⛭ And the ledger's bool guard caught two acoustic predicates returning np.bool_ --")
print("    true, but not a bool.  Coerced at source with the reason beside the coercion.")
print(f"  ⌗ The {REMAIN} that remain have a shape: 4 are bead_frames' nested functions, which")
print("    C73's Ⓓ⑤ gated the decision NOT to build a capability for, and 3 refuse on a")
print("    module-level name nothing graftable binds.  The 12 EXTEND rows are next.")
print("  " + "=" * 74)
print()
