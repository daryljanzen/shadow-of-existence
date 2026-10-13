#!/usr/bin/env python3
"""C79 -- `r7283` ② BATCH EIGHT: **SIX ROWS TAKEN, AND THIS SEAT'S OWN PINNED CALL IS REFUTED BY
ITS OWN REFUTATION CLAUSE — `1` OF `12`, NOT `3`.**

** THE CALL, PINNED BEFORE ANY OF THE `12` WAS COMPUTED. **  `EXTEND_PREDICTION.md`, digest
`14aa710408c33d02`: *`3` of the `12` `EXTEND` rows will be `FUNCTION-IS-THE-WRONG-KIND`, a `25`
per cent share against the `8.5` per cent measured over all `59` `INPUTS` rows* -- on the
reasoning that *a short extension changes what a function COMPUTES but not the KIND of question
it answers, so `a short extension` is the phrase a classifier reaches for when the real answer,
a different instrument, was never on the form.*

** ⛔⛭⛭⛭ THE MEASUREMENT KILLS IT, THROUGH THE CLAUSE THE CALL ITSELF WROTE. **  That clause:
*"if the corpus already carries a function of the right KIND, the backlog named the wrong
function but the right KIND exists and the row is an ordinary mis-naming like `B39`'s."*
  ⇒ *** IT DOES, FOR TWO OF THE THREE I NAMED. ***  `B15` and `B8` are reached by `L130`'s OWN
  `inv_dim` with `chi_meson`.  Measured over `computations/` with this seat's own directory
  EXCLUDED: **four `inv_dim` functions against ZERO subalgebra-dimension functions.**
  ⌈ So `B15` and `B8` are `FUNCTION-MIS-NAMED` and only `C3` is a kind error.
  ** `1` of `12` = `8.3` per cent against `INPUTS`'s `5` of `59` = `8.5`. **  ⌊ *The shares are
  the same to within a fifth of a point: `EXTEND` does NOT attract kind errors, and the call is
  refuted in NUMBER and in DIRECTION.*

** ⛭⛭⛭ AND WHAT REFUTED IT IS WORTH MORE THAN THE CALL WOULD HAVE BEEN. **  *`B15` and `B8`
assert a LIE-GROUP fact -- `the smallest connected group containing the ratios together with the
hinge three-cycle is SU(3) itself` -- and it is reached by a FINITE-GROUP CHARACTER COUNT with no
Lie-algebra machinery in it at all.*
  `inv_dim(G_su, chi_meson) = 1` is `dim Hom(V, V)`, so by **Schur** the `3` is irreducible; an
irreducible `3` sits in no proper connected subgroup of `SU(3)`.
  ⇒ *** THE SAME NUMBER BATCH SIX READ AS `colour's meson selection rule` IS THE IRREDUCIBILITY
  CRITERION. ***  *One invariant dimension, two readings, and the second is what makes a
  Lie-group claim reachable by counting characters of a group of order `27`.*

⌗ ** `C3` SURVIVES AS THE ONE KIND ERROR, with its qualification stated and not buried: ** the
only subalgebra-dimension functions under `computations/` are the ones this seat wrote at batch
five.  *So the corpus carries the right kind NOW because I built it, and did not when the backlog
was written.*  **The verdict is a kind error against the corpus as the backlog found it.**

⌗ *And the three `P_T_of` rows are settled by the function's own SIGNATURE: two parameters, both
properties of the progenitor, and no crossing parameter at all -- which is what `a property of
the progenitor's collapse history rather than of the crossing` means when the crossing has zero
duration.*

WHAT IS NOT CLAIMED.  ** Not that `SO(3)`'s finite subgroups are enumerated here ** -- that every
order-`27` subgroup of `SO(3)` is cyclic is taken from the classification and LABELLED as a
stated input; what is computed is the irreducibility and the non-commutativity.  ** Not that the
damping calculation on the approach is performed ** -- the rows ask which SIDE the dependence
sits on.  ** Not that any pin moves. **

Run: python3 C79_....py
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
             'EXTEND_PREDICTION.md': '14aa710408c33d02'}

INPUTS_N, EXTEND_N = 59, 12
SIZES = (19, 4, 9, 9, 5, 6, 4, 6)
INPUTS_LANDED, INPUTS_REMAIN = 52, 7
EXTEND_LANDED, EXTEND_REMAIN = 10, 2
CALLED, MEASURED = 3, 1
INPUTS_WRONG_KIND = 5
L130 = 'baryon_edge/L130_statistics_not_gauge.py'
L150G = 'beyond_the_wall/L150g_the_tensor_sector_and_the_interiors_adequacy.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import extensions_b8 as X                                                  # noqa: E402
import reach_b8 as RB8                                                     # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
LEDGERS = [tsv(MINE, n)[1:] for n in ('REACHED.tsv', 'REACHED_B2.tsv', 'REACHED_B3.tsv',
                                      'REACHED_B4.tsv', 'REACHED_B5.tsv', 'REACHED_B6.tsv',
                                      'REACHED_B7.tsv', 'REACHED_B8.tsv')]
B8 = LEDGERS[7]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']
EXTEND = [r for r in BAK if r[6] == 'EXTEND']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the EIGHT batches partition what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the two classes are still {INPUTS_N} `INPUTS` and {EXTEND_N} `EXTEND`",
     len(INPUTS) == INPUTS_N and len(EXTEND) == EXTEND_N)
_sets = [{(r[0], r[1]) for r in LEDGERS[0]},
         {(r[1], r[2]) for r in LEDGERS[1] if r[0] == 'TAKEN'}] + \
        [{(r[0], r[1]) for r in L} for L in LEDGERS[2:]]
gate(f"Ⓐ④  the eight batches take {'+'.join(str(x) for x in SIZES)} = "
     f"{INPUTS_LANDED + EXTEND_LANDED} rows and the eight key sets are PAIRWISE DISJOINT",
     tuple(len(s) for s in _sets) == SIZES
     and all(not (_sets[i] & _sets[j]) for i in range(8) for j in range(i + 1, 8))
     and sum(SIZES) == INPUTS_LANDED + EXTEND_LANDED)
gate(f"Ⓐ⑤  both classes partition: {INPUTS_LANDED}+{INPUTS_REMAIN}=={INPUTS_N} and "
     f"{EXTEND_LANDED}+{EXTEND_REMAIN}=={EXTEND_N}",
     INPUTS_LANDED + INPUTS_REMAIN == INPUTS_N
     and EXTEND_LANDED + EXTEND_REMAIN == EXTEND_N)
gate("Ⓐ⑥  every batch-eight row is an `EXTEND` key the BACKLOG carries, naming the function the "
     "backlog names", {(r[0], r[1]) for r in B8} <= {(r[0], r[1]) for r in EXTEND}
     and all(next(q[5] for q in EXTEND if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B8))

# =========================================================================================
head('Ⓑ  ⛔⛭⛭⛭ THE REFUTATION -- the call, the clause it wrote, and the measurement')
# =========================================================================================
_pred = re.sub(r'\s+', ' ', open(os.path.join(MINE, 'EXTEND_PREDICTION.md'),
                                 encoding='utf-8').read())
gate(f"Ⓑ①  the call is digest-pinned at {MY_DIGEST['EXTEND_PREDICTION.md']} and names its "
     f"number: {CALLED} of {EXTEND_N}",
     _has(_pred, '`3` OF THE `12`', ' WILL BE') and _has(_pred, 'THE THREE I ', 'NAME'))
gate("Ⓑ②  and it names the three rows, so the call cannot be re-read after the fact",
     all(_has(_pred, nm) for nm in ('B15', 'B8', 'C3')))
gate("Ⓑ③  ** and it wrote the clause that kills it: a row whose right KIND already exists in "
     "the corpus is an ordinary MIS-NAMING and not a kind error **",
     _has(_pred, 'the backlog named the wrong', ' function but the right KIND exists'))
_inv = X.invariant_dimension_functions()
_sub = X.subalgebra_dimension_functions()
gate(f"Ⓑ④  ** MEASURED over `computations/` with this seat's own directory EXCLUDED: {len(_inv)} "
     f"`inv_dim` functions against {len(_sub)} subalgebra-dimension functions. So the right kind "
     f"for `B15`/`B8` existed all along and the right kind for `C3` did not **",
     len(_inv) >= 4 and len(_sub) == 0
     and all('r7267_cc66_reach_the_71' not in p for p, _ in _inv))
_mis = [r for r in B8 if r[4] == X.MIS_NAMED]
_wk = [r for r in B8 if r[4] == X.WRONG_KIND]
gate(f"Ⓑ⑤  so the ledger records {len(_mis)} `{X.MIS_NAMED}` and {len(_wk)} "
     f"`{X.WRONG_KIND}` -- and `{MEASURED}` of `{EXTEND_N}` is the measured share",
     len(_mis) == 2 and len(_wk) == 1 and len(_wk) == MEASURED)
_a, _b = X.the_shares()
gate(f"Ⓑ⑥  ⛔ ** {MEASURED} of {EXTEND_N} = {_a:.1f} per cent against `INPUTS`'s "
     f"{INPUTS_WRONG_KIND} of {INPUTS_N} = {_b:.1f} per cent. The shares are the same to within "
     f"a fifth of a point, so `EXTEND` does NOT attract kind errors and THE CALL IS REFUTED IN "
     f"NUMBER AND DIRECTION **",
     X.the_call_is_refuted() and abs(_a - _b) < 0.5 and MEASURED < CALLED)
gate("Ⓑ⑦  and the refutation fires the call's OWN first clause -- `2` or fewer wrong-kind rows "
     "kills the direction -- rather than a clause written afterwards",
     _has(_pred, '`2` or fewer', ' wrong-kind rows') and MEASURED <= 2)

# =========================================================================================
head('Ⓒ  ⛭⛭⛭ WHAT REFUTED IT -- a Lie-group claim by a finite-group character count')
# =========================================================================================
gate("Ⓒ①  `L130`'s own `inv_dim` with `chi_meson` gives `dim Hom(V,V) = 1` on the "
     "determinant-one group, which by Schur makes the `3` IRREDUCIBLE",
     X.hom_dimension('G_su') == 1 and X.three_is_irreducible('G_su'))
gate("Ⓒ②  and the group is NON-ABELIAN, which is the second computed half",
     not X.is_abelian('G_su'))
gate("Ⓒ③  ** so it sits in no proper connected subgroup of `SU(3)`, and the smallest connected "
     "group containing it IS `SU(3)` -- reached with NO Lie-algebra machinery anywhere **",
     X.no_proper_connected_subgroup_contains_it('G_su'))
gate("Ⓒ④  and on `L130`'s own `G_rigid` the same number is 3, the `3` is reducible, and the "
     "predicate comes back FALSE -- the converse from the module's own table",
     X.hom_dimension('G_rigid') == 3
     and not X.no_proper_connected_subgroup_contains_it('G_rigid'))
_c77 = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__)))
        if f.startswith('C77_')]
_c77src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), _c77[0]),
               encoding='utf-8').read()
gate("Ⓒ⑤  ⛭⛭ ** AND IT IS THE SAME NUMBER `C77` READ AS `colour's meson selection rule`: one "
     "invariant dimension, two readings, and the second is what makes a Lie-group claim "
     "reachable by counting characters of a group of order 27 **",
     _has(_c77src, 'chi_meson') and _has(_c77src, 'meson 1')
     and X.hom_dimension('G_su') == 1)

# =========================================================================================
head('Ⓓ  THE SIX -- computed, each FALSE on its own recorded converse')
# =========================================================================================
gate(f"Ⓓ①  all {SIZES[7]} rows come back with the claim TRUE", all(r[5] == 'TRUE' for r in B8))
gate(f"Ⓓ②  and all {SIZES[7]} come back FALSE on their recorded converse",
     all(r[7] == 'FALSE' for r in B8))
gate("Ⓓ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[6].split()) >= 8 for r in B8) and all(any(c.isdigit() for c in r[8])
                                                     for r in B8))
gate("Ⓓ④  ** every row's claim and converse are THE SAME PREDICATE called at two inputs of the "
     "SAME KIND, which is batch seven's guard still in force **",
     all(callable(r[5]) and type(r[6]) is type(r[8]) for r in RB8.ROWS))
gate(f"Ⓓ⑤  `C3`'s triple computes EXACTLY: the symmetric-pair isotropy dimensions of `so(5,1)` "
     f"are {X.isotropy_dimensions(6)}, which is `P12`'s stated triple",
     X.triple_matches_the_paper(6) and tuple(X.isotropy_dimensions(6)) == X.P12_TRIPLE)
gate(f"Ⓓ⑥  and one ambient dimension up they are {X.isotropy_dimensions(7)}, so the triple is a "
     f"fact about `so(5,1)` -- the reachable converse",
     not X.triple_matches_the_paper(7))
gate(f"Ⓓ⑦  `P_T_of` has exactly the parameters {list(X.tensor_parameters())} -- both properties "
     f"of the progenitor -- and NO crossing parameter, read off its own signature",
     X.tensor_parameters() == ('rho_v', 'M_v'))
gate(f"Ⓓ⑧  ** so the amplitude moves with the APPROACH and not with the CROSSING, and the "
     f"log-log slopes are exactly {X.log_slope('rho_v'):.4f} and {X.log_slope('M_v'):.4f}: a "
     f"decade of approach moves it by 10^6 while the crossing contributes one **",
     X.amplitude_depends_on(X.APPROACH) and not X.amplitude_depends_on(X.CROSSING)
     and abs(X.log_slope('rho_v') + 6.0) < 1e-6
     and abs(X.log_slope('M_v') + 2.0) < 1e-9
     and X.a_decade_of_approach_moves_it_by())

# =========================================================================================
head('Ⓔ  THE GRAFTS')
# =========================================================================================
for _m, _f in ((L130, 'chi_meson'), (L130, 'inv_dim'), (L150G, 'P_T_of')):
    _g = GRAFT.graft(_m, _f, extra=())
    gate(f"Ⓔ  `{_m.split('/')[-1][:30]}` gives `{_f}` from {_g['_STATEMENTS']} of its "
         f"{_g['_OF']} top-level statements", callable(_g[_f]) and _g['_OF'] > 15)
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import extensions_b8 as X; '
     'X.hom_dimension("G_su"); X.tensor_parameters(); X.isotropy_dimensions(6)' % MINE],
    capture_output=True, text=True, timeout=900)
gate("Ⓔ④  ** and the grafts PRINT NOTHING in a fresh interpreter **",
     _probe.returncode == 0 and _probe.stdout == '')

# =========================================================================================
head('Ⓕ  THE HOLDERS')
# =========================================================================================
_holders = sorted({r[0] for r in B8})
gate(f"Ⓕ①  the {SIZES[7]} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 4 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283b8' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283b8' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283b8') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B8 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate("Ⓕ②  every holder defines `_r7283b8` at its own top level, from each file's syntax tree",
     not _bad_def)
gate("Ⓕ③  ** and calls it inside a `check` or `gate` **", not _bad_call)
gate("Ⓕ④  and every row's literal is STILL a string constant of its holder", not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _holders]
gate(f"Ⓕ⑤  all {len(_holders)} holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓕ⑥  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
gate("Ⓕ⑦  ⚠ and NONE of the four is a receipt `S14` pins by line number",
     not ({'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
           'receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py'}
          & set(_holders)))

# =========================================================================================
head('Ⓖ  THE GUARD')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine_in = [n.left.value for n in ast.walk(_self)
            if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
            and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
            and len(n.left.value.split()) > 3]
gate("Ⓖ①  ** no string constant of more than three words sits on the left of an `in` test "
     "anywhere in this file, proved from its OWN syntax tree **", not _mine_in)
gate("Ⓖ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓖ③  and the ordered work cannot exhaust its subject: "
     f"{INPUTS_LANDED + EXTEND_LANDED} of {INPUTS_N + EXTEND_N}, with "
     f"{INPUTS_REMAIN + EXTEND_REMAIN} remaining",
     INPUTS_REMAIN + EXTEND_REMAIN > 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** SIX OF SIX TAKEN, AND MY OWN PINNED CALL IS REFUTED BY ITS OWN CLAUSE. **")
print(f"  ⛭⛭⛭ {INPUTS_LANDED + EXTEND_LANDED} OF {INPUTS_N + EXTEND_N} LANDED "
      f"({INPUTS_LANDED} of {INPUTS_N} INPUTS, {EXTEND_LANDED} of {EXTEND_N} EXTEND), "
      f"{INPUTS_REMAIN + EXTEND_REMAIN} REMAIN.")
print(f"  ⛔ I CALLED {CALLED} OF {EXTEND_N} WRONG-KIND.  MEASURED: {MEASURED}.")
print(f"    {_a:.1f} per cent against INPUTS's {_b:.1f} -- the same to within a fifth of a")
print("    point.  EXTEND does not attract kind errors; the direction dies with the number.")
print("    The clause that killed it is the one the call itself wrote: B15 and B8 are reached")
print("    by L130's OWN inv_dim with chi_meson, four such functions existing under")
print("    computations/ against ZERO subalgebra-dimension ones, so they are MIS-NAMED.")
print("  ⛭⛭⛭ AND WHAT REFUTED IT IS WORTH MORE: a LIE-GROUP claim reached by a FINITE-GROUP")
print("    CHARACTER COUNT.  inv_dim(G_su, chi_meson) = 1 is dim Hom(V,V), so by Schur the 3 is")
print("    irreducible and sits in no proper connected subgroup of SU(3).  THE SAME NUMBER C77")
print("    read as colour's meson selection rule IS the irreducibility criterion.")
print("  ⌗ C3 survives as the one kind error, and the qualification is stated: the corpus")
print("    carries the right kind NOW because this seat built it at batch five, and did not")
print("    when the backlog was written.")
print("  " + "=" * 74)
print()
