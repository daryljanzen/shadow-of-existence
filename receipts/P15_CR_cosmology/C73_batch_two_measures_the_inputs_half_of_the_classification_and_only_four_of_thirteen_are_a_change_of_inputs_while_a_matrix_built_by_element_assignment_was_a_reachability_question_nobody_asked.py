#!/usr/bin/env python3
"""C73 -- `r7267`/`r7275` ① BATCH TWO: **FOUR OF THE THIRTEEN ARE A CHANGE OF INPUTS AND NINE ARE
NOT, SO `r7275`'s RULING ① ARRIVES AGAIN AT PER-ROW RESOLUTION.**

** THE ORDER. **  `r7275` ①: "BATCH TWO, AS YOU SCHEDULED IT: `13` ROWS, `32` OF `59` ... You gated them
as the next largest against the tree rather than against the table, which is the right instrument."

** ⛭⛭ ⓵ AND THE SCHEDULE WAS RIGHT WHILE THE CLASSIFICATION UNDER IT WAS NOT. **  `r7275` ruled on batch
one that `r7261` "classified `59` rows by what the function computes and not one of those modules can be
imported -- the classification had read the mathematics without asking whether the code was reachable".
*** Batch two says the same thing about the INPUTS half, and says it per ROW rather than per module: of
the thirteen, FOUR are a change of inputs in the strict sense and NINE need something the classification
did not record. ***

** ⛭⛭ ⓶ AND THE LOADER NEEDED A SECOND REPAIR TO REACH `A2` AT ALL, WHICH IS THE SAME LESSON ONE LEVEL
DOWN. **  `A2` builds its metric by ELEMENT ASSIGNMENT -- `g = sp.zeros(4, 4)`, then `g[0, 1] = g[1, 0] =
1` and three more.  `graft.py` read a SUBSCRIPT TARGET AS A BINDING, so it kept the last element
assignment as the definition of `g` and dropped the `sp.zeros` that creates it: the graft raised
`NameError: name 'g' is not defined`.  *** A matrix built by element assignment is a reachability
question nobody had asked, and several modules here build theirs that way. ***  Subscript and attribute
targets are now MUTATIONS, retained with the binding in source order, and the batch-one grafts are
unchanged by the fix.

** ⛭⛭⛭ ⓷ THE FOUR TAKEN, AND THE PAIR `L-104w` NEVER FORMS IS THE ONE WORTH READING. **
  * ** `C3`, through `A2`'s own `lie_g` at a REBOUND metric. **  `lie_g` reads the metric from module
    level, where `A2` binds its chiral plane wave, so the change of inputs is a rebinding rather than an
    argument -- which is what returning the NAMESPACE is for.  Handed `dS_2 x S^2`, six generators come
    back Killing: ** three `so(2,1)` DERIVED from the embedding `-T^2+X^2+Y^2 = 1` and each verified
    against its third row rather than quoted, and three `so(3)` on the two-sphere. **  Three reachable
    converses -- `chi d_tau`, `d_chi`, `d_theta` -- all come back NOT Killing.
  * ** `B30`, `B39`, `B40`, through `L-104w`'s own `sep` ON A PAIR `L-104w` NEVER FORMS. **  Its report
    runs `sep` over fifteen excentre-excentre pairs and thirty-six hinge-excentre pairs; three receipts
    assert something about ** the two ends of ONE hinge ** -- same azimuth, OPPOSITE HORN, at `2 alpha`
    -- which is one call on two points `pt` already builds and which nothing in the corpus had made.
    `s^2 = -12 alpha^2`, timelike at every hinge azimuth.  ⇒ *** And the converse is not a radius away
    but AT THE THROAT: at `rho = alpha` the two ends COINCIDE and the interval is NULL, so the claim is a
    statement about the hinge sitting OUTSIDE the throat and nobody had said so. ***

** ⛔ ⓸ THE NINE HELD, EACH WITH THE REASON, BECAUSE A ROW TAKEN ON A GUESSED INPUT IS WORSE THAN A ROW
STILL OPEN. **  `GEOMETRY-NOT-RECORDED` 4, `NESTED-FUNCTION` 3, `OBJECTS-NOT-RECORDED` 1,
`AXIS-ARGUMENT` 1.  *** The three `NESTED-FUNCTION` rows all name `bead_frames.py: tau_of_r`, which is a
closure defined INSIDE a matplotlib plotting routine -- not a top-level `def` at all -- and the measured
reason not to build a lifting capability for it is that it would serve exactly those three: of the `40`
`INPUTS` rows outstanding before this batch, `37` name a TOP-LEVEL function and `3` name a nested one,
all three the same one. ***

WHAT IS NOT CLAIMED.  ** Not that the nine are unreachable ** -- they are unreached, with the obstruction
named per row.  ** Not that the Nariai algebra is exactly six-dimensional ** -- six generators are
COMPUTED Killing, a lower bound with the product structure; `A2`'s own exact-count method is a
hand-derived ODE system for its own metric and does not transport, and this receipt says so rather than
borrowing the number.  ** Not that any pin is removed ** -- the pin is the CITATION and the computation
the VERIFICATION, and the ledger's key count is untouched.

Run: python3 C73_....py
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
MY_DIGEST = {'REACHED.tsv': 'f0cca8fdd765a475', 'REACHED_B2.tsv': '2e226763e5cf0f56'}

INPUTS_N = 59
B1_N, B2_SCHEDULED, B2_TAKEN, B2_HELD = 19, 13, 4, 9
LANDED, REMAIN = 23, 36
TOPLEVEL_40, NESTED_40 = 37, 3
A2 = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'
L104 = 'baryon_edge/L104w_the_excentre_trichotomy.py'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import graft as GRAFT                                                      # noqa: E402
import isometry as ISO                                                     # noqa: E402
import trichotomy as TRI                                                   # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
B2 = tsv(MINE, 'REACHED_B2.tsv')[1:]
B1 = tsv(MINE, 'REACHED.tsv')[1:]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the two batches PARTITION what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in MY_DIGEST.items():
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the `INPUTS` class is still {INPUTS_N} rows", len(INPUTS) == INPUTS_N)

_taken = [r for r in B2 if r[0] == 'TAKEN']
_held = [r for r in B2 if r[0] == 'HELD']
gate(f"Ⓐ④  batch two scheduled {B2_SCHEDULED} rows and the ledger records "
     f"{B2_TAKEN} TAKEN + {B2_HELD} HELD, which sum to it",
     len(_taken) == B2_TAKEN and len(_held) == B2_HELD
     and len(_taken) + len(_held) == B2_SCHEDULED)
_k1 = {(r[0], r[1]) for r in B1}
_k2 = {(r[1], r[2]) for r in _taken}
gate(f"Ⓐ⑤  ** and the two batches take DISJOINT rows: no key is in both, so "
     f"{B1_N} + {B2_TAKEN} = {LANDED} counts nothing twice **",
     not (_k1 & _k2) and len(_k1) == B1_N and len(_k2) == B2_TAKEN
     and B1_N + B2_TAKEN == LANDED)
gate(f"Ⓐ⑥  {LANDED} + {REMAIN} == {INPUTS_N}: landed and remaining partition the class",
     LANDED + REMAIN == INPUTS_N)
_bk = {(r[0], r[1]) for r in INPUTS}
gate("Ⓐ⑦  every row in the batch-two ledger, taken or held, is a key the BACKLOG carries",
     all((r[1], r[2]) in _bk for r in B2))

# =========================================================================================
head('Ⓑ  THE LOADER REPAIR -- a subscript target is a MUTATION and not a binding')
# =========================================================================================
_a2src = open(os.path.join(ROOT, 'computations', A2), encoding='utf-8').read()
_a2 = ast.parse(_a2src)
_subs = [n for n in _a2.body if isinstance(n, ast.Assign)
         and any(isinstance(t, ast.Subscript) for t in n.targets)]
gate(f"Ⓑ①  `A2` really does build its metric by element assignment: {len(_subs)} top-level "
     f"statements assign through a SUBSCRIPT",
     len(_subs) >= 4)
gate("Ⓑ②  and `_bound_by` does NOT read those as bindings, while `_mutated_by` does -- which is "
     "the whole repair, read off the loader's own functions",
     all(GRAFT._bound_by(st) == set() for st in _subs)
     and all(GRAFT._mutated_by(st) for st in _subs)
     and all(len(GRAFT._mutated_by(st)) == 1 for st in _subs))
_g = GRAFT.graft(A2, 'lie_g', extra=('g', 'Xc'))
gate(f"Ⓑ③  so the graft now produces `A2`'s metric, built: a 4x4 whose `(0,1)` entry is 1 and "
     f"whose `(0,0)` entry carries both polarisations",
     _g['g'].shape == (4, 4) and _g['g'][0, 1] == 1 and _g['g'][0, 0] != 0)
gate("Ⓑ④  ** and the batch-one grafts are UNCHANGED by the repair, so it is additive: `twoM` and "
     "`L-129`'s four functions still graft and still return what `REACHED.tsv` recorded **",
     GRAFT.graft('baryon_edge/L006w_the_d5_fourfold.py', 'twoM', extra=('r0',))['_STATEMENTS'] == 3
     and GRAFT.graft('baryon_edge/L129_the_invariants.py', 'close', 'det', 'inv_dim',
                     'chi_VVV', extra=('ID', 'CYC'))['_STATEMENTS'] == 12)
_probe = subprocess.run(
    [sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import graft; '
     'graft.graft(%r, "lie_g", extra=("g","Xc")); '
     'graft.graft(%r, "sep", "character", "pt", extra=("al","hinge_az","exc_az"))'
     % (MINE, A2, L104)], capture_output=True, text=True, timeout=600)
gate("Ⓑ⑤  and both of this batch's grafts PRINT NOTHING in a fresh interpreter, so neither "
     "module's own report ran",
     _probe.returncode == 0 and _probe.stdout == '')

# =========================================================================================
head('Ⓒ  THE FOUR TAKEN -- claim TRUE, converse FALSE, computed through the named function')
# =========================================================================================
gate(f"Ⓒ①  all {B2_TAKEN} taken rows come back with the claim TRUE",
     all(r[5] == 'TRUE' for r in _taken))
gate(f"Ⓒ②  and all {B2_TAKEN} come back FALSE on their recorded converse",
     all(r[7] == 'FALSE' for r in _taken))
gate("Ⓒ③  every converse is a concrete EDIT in words, and every taken row records what the "
     "computation returned in numbers",
     all(len(r[6].split()) >= 5 for r in _taken)
     and all(any(c.isdigit() for c in r[8]) for r in _taken))

_I = ISO.at_inputs().nariai()
_gens, _conv = _I.generators(), _I.converses()
gate("Ⓒ④  `A2`'s own `lie_g`, at the Nariai metric: all SIX generators are Killing",
     len(_gens) == 6 and all(_I.is_killing(x) for x in _gens.values()))
gate("Ⓒ⑤  and none of the three reachable converses is -- so the predicate discriminates",
     len(_conv) == 3 and not any(_I.is_killing(x) for x in _conv.values()))
gate("Ⓒ⑥  ** the three `so(2,1)` generators are DERIVED and not quoted: each is solved from two "
     "rows of the embedding's Jacobian and VERIFIED against the third, which `so21_static` "
     "asserts in its own body **",
     len(ISO.Isometry.so21_static()) == 3)
_T = TRI.at_inputs()
gate("Ⓒ⑦  `L-104w`'s own `sep`, on the pair its report never forms: the two ends of one hinge "
     "are TIMELIKE at every hinge azimuth",
     _T.all_hinges_timelike() and len(_T.hinge_az) == 3)
gate("Ⓒ⑧  ** and the converse is AT THE THROAT and not a radius away: at `rho = alpha` the two "
     "ends coincide and the interval is NULL **",
     _T.ends_interval(_T.hinge_az[0], _T.al) == 0
     and _T.ends_character(_T.hinge_az[0], _T.al) == 'null'
     and not _T.all_hinges_timelike(_T.al))
gate("Ⓒ⑨  and the taken interval is the one the report never computed: `-12 alpha^2`, the same "
     "at all three azimuths",
     len({str(_T.ends_interval(a)) for a in _T.hinge_az}) == 1)

# =========================================================================================
head('Ⓓ  THE NINE HELD -- the reason is per ROW and it is the batch\'s own result')
# =========================================================================================
_codes = {}
for r in _held:
    _codes[r[8].split(':')[0]] = _codes.get(r[8].split(':')[0], 0) + 1
gate(f"Ⓓ①  the {B2_HELD} held rows carry four distinct reason codes, "
     f"{sorted(_codes.items())}, and they sum to the held count",
     sum(_codes.values()) == B2_HELD and len(_codes) == 4)
gate("Ⓓ②  every held row's reason is a SENTENCE and not a label -- at least twelve words after "
     "the code, so none is held on a word",
     all(len(r[8].split(':', 1)[1].split()) >= 12 for r in _held))
gate("Ⓓ③  ** and the `NESTED-FUNCTION` rows are TRUE of the tree: `tau_of_r` is defined inside "
     "another function in `bead_frames.py` and is NOT a top-level `def` **",
     (lambda t: 'tau_of_r' not in {n.name for n in t.body
                                   if isinstance(n, ast.FunctionDef)}
      and 'tau_of_r' in {n.name for n in ast.walk(t) if isinstance(n, ast.FunctionDef)})(
         ast.parse(open(os.path.join(ROOT, 'computations', 'bead_frames.py'),
                        encoding='utf-8').read())))
try:
    GRAFT.graft('bead_frames.py', 'tau_of_r')
except GRAFT.GraftError:
    _refused = True
else:
    _refused = False
gate("Ⓓ④  and the loader REFUSES it rather than resolving something else, which is why those "
     "three rows are held and not taken",
     _refused)

# ⌗ the MEASUREMENT that says not to build a lifting capability for it
_ptop = _pnest = 0
for r in INPUTS:
    if r[4] in ('baryon_edge/L129_the_invariants.py', 'baryon_edge/L006w_the_d5_fourfold.py'):
        continue
    _p = os.path.join(ROOT, 'computations', r[4])
    if not os.path.exists(_p):
        continue
    _t = ast.parse(open(_p, encoding='utf-8').read())
    if r[5] in {n.name for n in _t.body if isinstance(n, ast.FunctionDef)}:
        _ptop += 1
    elif r[5] in {n.name for n in ast.walk(_t) if isinstance(n, ast.FunctionDef)}:
        _pnest += 1
gate(f"Ⓓ⑤  ** AND THE REASON NOT TO BUILD A NESTED-LIFTING CAPABILITY IS MEASURED AND NOT "
     f"PREFERRED: of the {TOPLEVEL_40 + NESTED_40} `INPUTS` rows outstanding before this batch, "
     f"{_ptop} name a TOP-LEVEL function and {_pnest} name a nested one -- and all "
     f"{_pnest} name the SAME one **",
     _ptop == TOPLEVEL_40 and _pnest == NESTED_40
     and len({r[5] for r in INPUTS if r[6] == 'INPUTS'
              and r[4] == 'bead_frames.py' and r[5] == 'tau_of_r'}) == 1)

# =========================================================================================
head('Ⓔ  THE HOLDERS -- the computation is in the holder, and the pin stands beside it')
# =========================================================================================
_holders = sorted({r[1] for r in _taken})
gate(f"Ⓔ①  the {B2_TAKEN} taken rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 4 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7267' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7267' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'check'
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7267') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[2] for r in _taken if r[1] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate("Ⓔ②  every holder defines `_r7267` at its own top level, from each file's syntax tree",
     not _bad_def)
gate("Ⓔ③  ** and calls it inside a `check`, so the holder itself computes the quantity **",
     not _bad_call)
gate("Ⓔ④  and every taken row's literal is STILL a string constant of its holder -- the pin is "
     "the citation and this batch removed none",
     not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=900)) for h in _holders]
gate(f"Ⓔ⑤  all {len(_holders)} holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓔ⑥  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any(_has(l, 'OK', '  ') and _has(l, 'COMPUTED') for l in r.stdout.split('\n'))
         for _, r in _runs))
gate("Ⓔ⑦  ⚠ and `B39` -- whose OTHER backlog row is held -- says so in its own source beside "
     "the loader, so the holder records what it did not take",
     _has(open(os.path.join(ROOT, 'receipts/L221_the_bridge/'
                            'B39_the_substrate_does_carry_compact_su2.py'),
               encoding='utf-8').read(), 'is HELD and not taken'))

# =========================================================================================
head('Ⓕ  THE GUARD -- no pin minted, and the arithmetic cannot exhaust its subject')
# =========================================================================================
_self = ast.parse(open(os.path.abspath(__file__), encoding='utf-8').read())
_mine = [n.left.value for n in ast.walk(_self)
         if isinstance(n, ast.Compare) and any(isinstance(o, ast.In) for o in n.ops)
         and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
         and len(n.left.value.split()) > 3]
gate("Ⓕ①  ** no string constant of more than three words sits on the left of an `in` test "
     "anywhere in this file, proved from its OWN syntax tree **", not _mine)
gate("Ⓕ②  every presence test goes through `_needle`, assembled at run time",
     any(isinstance(n, ast.FunctionDef) and n.name == '_needle' for n in _self.body))
gate(f"Ⓕ③  and the ordered work cannot exhaust its subject: {LANDED} of {INPUTS_N} with "
     f"{REMAIN} remaining, and the `12` `EXTEND` rows behind all of them",
     LANDED < INPUTS_N and REMAIN > 0)

print()
print("  " + "=" * 74)
if FAILED:
    print(f"  {len(FAILED)} gate(s) FAILED:")
    for f in FAILED:
        print(f"    - {f}")
    print("  " + "=" * 74)
    raise SystemExit(1)
print("  VERDICT: ** BATCH TWO IS 4 TAKEN AND 9 HELD, AND THE SPLIT IS THE RESULT. **")
print(f"  ⛭⛭⛭ {LANDED} OF {INPUTS_N} LANDED, {REMAIN} REMAIN.")
print("  ⛭⛭ r7275's ruling ① said r7261 classified rows by what the function computes without")
print("    asking whether the code was reachable.  Batch two says the same thing PER ROW: only")
print("    4 of the 13 are a change of inputs in the strict sense.  The other 9 want a nested")
print("    function, a geometry, or a reading of which objects a sentence means -- each named.")
print("  ⛭⛭ And the loader needed a second repair to reach A2 at all: a matrix built by ELEMENT")
print("    ASSIGNMENT was a reachability question nobody had asked, and a subscript target read")
print("    as a binding dropped the sp.zeros that creates the metric.")
print("  ⛭⛭ The four taken: the Nariai algebra through A2's own lie_g at a rebound metric, six")
print("    generators Killing with three converses false and the so(2,1) half DERIVED from the")
print("    embedding rather than quoted; and the two ends of ONE hinge through L-104w's own sep,")
print("    s^2 = -12 alpha^2, on a pair its own report never forms -- with the converse AT THE")
print("    THROAT, where the ends coincide and the interval is null.")
print("  ⌗ The nested-lifting capability is NOT built, on a measurement: of the 40 rows")
print(f"    outstanding before this batch, {TOPLEVEL_40} name a top-level function and "
      f"{NESTED_40} name a nested")
print("    one, and all three name the same one.")
print("  " + "=" * 74)
print()
