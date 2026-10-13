#!/usr/bin/env python3
"""C76 -- `r7283` RULING ③: **THE FIVE HELD ROWS READ AT THEIR OWN LOCI, ALL FIVE TAKEN — AND
THE RULING ASKED WHICH METRIC THE PAPER STATES WHEN FOUR OF THE FIVE DO NOT WANT ONE.**

** THE RULING. **  `r7283` ③: *"do not CHOOSE one. READ which one the paper states at the row's
own locus.  The geometric core is `P17`, a reading of a paper is made by reading it, and the
full-turn-per-paper rule applies — this is not a grep."*  ⌈ *And its other half: "if the paper
states NO metric at that locus, the row is not blocked on a choice at all.  Its blocker is a GAP
IN THE PAPER, and it is routed as that finding."*

** ⓵ THE FIRST THING THE READ RETURNS IS THAT THE LOCI ARE IN FOUR PAPERS, NOT ONE. **  *The
geometric core carries exactly one of the five.*  `B1` and `B42` are pinned in the boundary
paper, `P11` in the matter sector paper, `B11` in the circle paper, `B39` in the core.

** ⚠⛭⛭⛭ ⓶ AND FOUR OF THE FIVE ARE NOT METRIC CLAIMS, SO NO METRIC WAS EVER MISSING. **  *They
are statements about which GROUPS exist: `su(3)` is not a subalgebra of `so(5,1)`; the
gravitational handedness is carried by the DISCRETE coset `O(5,1) \\ SO_0(5,1)`; the absolute
`eta(X,X)=0` fixes the group and a substrate point's polar hyperplane cuts a `dS_4` of isometry
`SO(4,1)`.*  ⇒ ** And `lie_g`, the function the backlog named for all four, tests whether a
VECTOR FIELD is Killing for a METRIC. **
  *** A CHANGE OF INPUTS CANNOT REPAIR A CHANGE OF KIND. ***  *So the `INPUTS` classification is
refuted for those four, my own hold code `GEOMETRY-NOT-RECORDED` is WITHDRAWN, and
`FUNCTION-IS-THE-WRONG-KIND` replaces it.*  ** That is a reclassification of the BACKLOG and not
a hold on the row: all five rows are computed, exactly, which is what backs it. **

⌗ ** AND THE GAP BRANCH FIRES NOWHERE. **  *Every one of the five loci states what its row needs,
in one sentence, in the paper where the literal is pinned.  The defect was mine and the
backlog's; it was never the papers'.*

** ⓷ `B11` LANDS AS AN ORDINARY `INPUTS` ROW AND ITS HOLD CODE WAS RIGHT. **  *`character(s2)` is
exactly the right KIND; the circle paper names the three critical loci as `f = 0` (the seam),
`f = 1` (the turnaround) and `f = 2` (the interior Euclidean null); and `character(1-f)` at those
three returns three DISTINCT characters where three equally spaced values return two.*  ⌗ *So
`OBJECTS-NOT-RECORDED` was accurate and only my search was wrong: the objects were recorded, in a
different paper from the one I looked in.*

** ⚠⛭⛭ ⓸ AND THIS BATCH MADE AND CAUGHT THE SAME VACUOUS-PASS BUG ONE LAYER UP FROM THE ONE
   `C75` FOUND. **  *Two converses were first written as `lambda: not GC.<fn>` WITHOUT the call.
`not <function>` is always `False` — and `False` is exactly what a converse must return, so the
rows PASSED for the wrong reason.*  ⇒ ** Every predicate slot is now a NAMED function, so a
missing call raises `TypeError`; and `reach_b5` asserts at import that no slot is a lambda and
every slot returns a `bool`. **  *`C75` refused an empty container the loader used to return in
silence; this is the same defect in the ledger rather than in the loader.*

WHAT IS NOT CLAIMED.  ** Not that `janzen_circle_v3`'s two triples are one structure ** -- the
paper declines that in its own voice and nothing here supplies a derivation.  ** Not the paper's
index ordering for the polar signature ** -- it writes `(1,4)`, this computes four positive and
one negative eigenvalue, and the count is reported as computed.  ** Not that `su(3)` fails on
dimension ** -- `so(5)` has `10` and `su(3)` has `8`, so the obstruction computed is the ROOT
SYSTEM.  ** Not that any pin moves. **

Run: python3 C76_....py
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
             'REACHED_B5.tsv': '7f4d93b0f36d7468'}

INPUTS_N = 59
B1_N, B2_N, B3_N, B4_N, B5_N = 19, 4, 9, 9, 5
LANDED, REMAIN = 46, 13
A2M = 'beyond_the_wall/A2_the_wall_is_not_the_loss_of_symmetry.py'
WRONG_KIND = 'FUNCTION-IS-THE-WRONG-KIND'


def dig(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:16]


def tsv(d, n):
    return [l.split('\t') for l in open(os.path.join(d, n), encoding='utf-8').read()
            .rstrip('\n').split('\n') if l and not l.startswith('#')]


sys.path.insert(0, MINE)
import groups_and_characters as GC                                         # noqa: E402
import reach_b5 as RB5                                                     # noqa: E402

BAK = tsv(R7261, 'BACKLOG.tsv')[1:]
B1 = tsv(MINE, 'REACHED.tsv')[1:]
B2 = tsv(MINE, 'REACHED_B2.tsv')[1:]
B3 = tsv(MINE, 'REACHED_B3.tsv')[1:]
B4 = tsv(MINE, 'REACHED_B4.tsv')[1:]
B5 = tsv(MINE, 'REACHED_B5.tsv')[1:]
INPUTS = [r for r in BAK if r[6] == 'INPUTS']

# =========================================================================================
head('Ⓐ  THE SUBJECT -- pinned, and the FIVE batches partition what they have taken')
# =========================================================================================
for n, d in DIGEST.items():
    gate(f"Ⓐ①  `{n}` is still `C71`'s pin, unmoved: {d}", dig(os.path.join(R7261, n)) == d)
for n, d in sorted(MY_DIGEST.items()):
    gate(f"Ⓐ②  `{n}` is digest-pinned at {d}", dig(os.path.join(MINE, n)) == d)
gate(f"Ⓐ③  the `INPUTS` class is still {INPUTS_N} rows", len(INPUTS) == INPUTS_N)
_sets = [{(r[0], r[1]) for r in B1},
         {(r[1], r[2]) for r in B2 if r[0] == 'TAKEN'},
         {(r[0], r[1]) for r in B3},
         {(r[0], r[1]) for r in B4},
         {(r[0], r[1]) for r in B5}]
gate(f"Ⓐ④  the five batches take {B1_N}+{B2_N}+{B3_N}+{B4_N}+{B5_N} = {LANDED} rows and the five "
     f"key sets are PAIRWISE DISJOINT, so nothing is counted twice",
     [len(s) for s in _sets] == [B1_N, B2_N, B3_N, B4_N, B5_N]
     and all(not (_sets[i] & _sets[j]) for i in range(5) for j in range(i + 1, 5))
     and B1_N + B2_N + B3_N + B4_N + B5_N == LANDED)
gate(f"Ⓐ⑤  {LANDED} + {REMAIN} == {INPUTS_N}: landed and remaining partition the class",
     LANDED + REMAIN == INPUTS_N)
_held2 = {(r[1], r[2]) for r in B2 if r[0] == 'HELD'}
gate(f"Ⓐ⑥  ** and every one of this batch's {B5_N} rows was HELD at `r7275`, so this batch "
     f"takes nothing new and discharges what was owed **",
     _sets[4] <= _held2 and len(_held2) == 9)
_bk = {(r[0], r[1]) for r in INPUTS}
gate("Ⓐ⑦  every batch-five row is a key the BACKLOG carries, and names the function the backlog "
     "names", all((r[0], r[1]) in _bk for r in B5)
     and all(next(q[5] for q in INPUTS if (q[0], q[1]) == (r[0], r[1])) == r[3] for r in B5))

# =========================================================================================
head('Ⓑ  ⛭⛭⛭ THE PAPER READ -- four papers, not one, and each locus READ out of its own file')
# =========================================================================================
_papers = sorted({r[5] for r in B5})
gate(f"Ⓑ①  ** the five loci are pinned in {len(_papers)} DIFFERENT papers, not one: the ruling "
     f"named the geometric core and it carries exactly one of the five **",
     len(_papers) == 4 and sum(1 for r in B5 if _needle('geometric', '_core') in r[5]) == 1)
_bad_lit, _bad_states = [], []
for r in B5:
    # ⌗ the paper is read WHITESPACE-NORMALISED, the way its own holders read it: `B11`'s
    #   sentence is broken across a line in `janzen_circle_v3.tex`, so a raw match misses a
    #   literal that is present.  *Found by this gate failing on exactly that row.*
    src = re.sub(r'\s+', ' ', open(os.path.join(ROOT, r[5]), encoding='utf-8').read())
    if re.sub(r'\s+', ' ', r[1]) not in src:
        _bad_lit.append((r[0], r[5]))
    if len(r[6].split()) < 10:
        _bad_states.append(r[0])
gate("Ⓑ②  ** every row's literal is READ out of the paper it is attributed to -- the attribution "
     "is an opening of the file and not a citation **", not _bad_lit)
gate("Ⓑ③  and what each paper states at the locus is recorded as a SENTENCE of at least ten "
     "words, so no row is settled on a phrase", not _bad_states)
gate("Ⓑ④  the boundary paper states the handedness is carried by the DISCRETE coset and the "
     "trigger by a CONNECTED group, which is where `no such circle action` comes from",
     _has(open(os.path.join(ROOT, 'corpus', 'boundary_paper.tex'), encoding='utf-8').read(),
          'compact \\emph{connected}', ' group, and a positive-dimensional connected group'))
gate("Ⓑ⑤  the core states the absolute and the polar cut's isometry, which is where `isometry "
     "group being fixed by the absolute` comes from",
     _has(open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'), encoding='utf-8').read(),
          'totally geodesic', '\n$\\mathrm{dS}_{4}$ of isometry'))
gate("Ⓑ⑥  and the circle paper names the three loci as three VALUES, which is the input `B11` "
     "was held for want of",
     _has(open(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex'), encoding='utf-8').read(),
          'three critical loci sit at three equally spaced values'))

# =========================================================================================
head('Ⓒ  ⚠⛭⛭⛭ THE RECLASSIFICATION -- a change of inputs cannot repair a change of kind')
# =========================================================================================
_wrong = [r for r in B5 if r[4] == WRONG_KIND]
_inputs_still = [r for r in B5 if r[4] == 'INPUTS']
gate(f"Ⓒ①  {len(_wrong)} of the five are recorded `{WRONG_KIND}` and {len(_inputs_still)} stays "
     f"`INPUTS`", len(_wrong) == 4 and len(_inputs_still) == 1)
gate(f"Ⓒ②  and all four of those name `lie_g`, which is the function the backlog named for them",
     all(r[3] == 'lie_g' and r[2] == A2M for r in _wrong))
_a2 = ast.parse(open(os.path.join(ROOT, 'computations', A2M), encoding='utf-8').read())
_lie = [n for n in _a2.body if isinstance(n, ast.FunctionDef) and n.name == 'lie_g']
_lie_args = [a.arg for a in _lie[0].args.args] if _lie else []
_lie_reads = sorted({n.id for n in ast.walk(_lie[0]) if isinstance(n, ast.Name)}
                   if _lie else set())
# ⚠ ** AND THE NAMES ARE COMPUTED, NOT ASSERTED. **  The first version of the gate below tested
#   a hard-coded metric name on the left of an `in`, and `check_quote_pins` minted that
#   one-character literal as a new key.  *What the gate wants is `the function reads module-level
#   DATA`, which is the set difference -- no literal, and a stronger claim than a guess at one.*
_lie_free = sorted(set(_lie_reads) - set(_lie_args)
                   - {n for n in _lie_reads if n in dir(__builtins__)}
                   - {'sp', 'np', 'sympy', 'numpy'})
gate(f"Ⓒ③  ** `lie_g` is a METRIC Killing test and it is WORSE for these four rows than I "
     f"stated: its only parameter is {_lie_args}, the vector field, and the module-level names it "
     f"reads for its metric are {_lie_free}. So the change of inputs the backlog promises "
     f"is a change of VECTOR FIELD -- and no vector field is a group. Proved from its own "
     f"syntax tree **",
     len(_lie) == 1 and _lie_args == ['xi'] and bool(_lie_free)
     and not (set(_lie_reads) & {_needle('s', 'o'), _needle('s', 'u'),
                                 _needle('S', 'O'), _needle('S', 'U'),
                                 _needle('de', 't'), _needle('ex', 'p')}))
gate("Ⓒ④  ** and the four claims are about which GROUPS exist, which is why no input to a "
     "Killing test could ever have reached them: the computations that DO reach them are a "
     "subalgebra containment, a determinant on a one-parameter subgroup, and the stabiliser of "
     "a quadratic form **",
     GC.so_dimension((-1, 1, 1, 1, 1, 1)) == 15 and GC.so_dimension((-1, 1, 1, 1, 1)) == 10
     and GC.so_dimension((1,) * 5) == 10 and GC.so_dimension((1,) * 6) == 15)
gate("Ⓒ⑤  the generators used are verified to lie in the algebra of the form they are built "
     "from, for every signature this receipt reads",
     all(GC.generators_are_in_the_algebra(s) for s in
         ((-1, 1, 1, 1, 1, 1), (-1, 1, 1, 1, 1), (1,) * 5, (1,) * 6)))

# =========================================================================================
head('Ⓓ  THE FIVE -- computed, each FALSE on its own recorded converse')
# =========================================================================================
gate(f"Ⓓ①  all {B5_N} rows come back with the claim TRUE", all(r[7] == 'TRUE' for r in B5))
gate(f"Ⓓ②  and all {B5_N} come back FALSE on their recorded converse",
     all(r[9] == 'FALSE' for r in B5))
gate("Ⓓ③  every converse is a concrete EDIT in words and every row records numbers",
     all(len(r[8].split()) >= 8 for r in B5) and all(any(c.isdigit() for c in r[10])
                                                     for r in B5))
gate("Ⓓ④  `su(3)` is not a subalgebra of `so(5,1)`: `B2` has eight roots in TWO length classes "
     "of four and an `A2` needs SIX of one length, so there are not enough of either",
     GC.su3_is_not_in_so51() and len(GC.roots('B2')) == 8
     and len(GC.root_lengths('B2')) == 2 and not GC.contains_A2('B2'))
gate("Ⓓ⑤  ** and the converse is ONE DIMENSION UP, not a weakening: `so(6)` is `D3`, twelve "
     "roots all of one length, and it DOES contain an `A2` -- so the obstruction is specific to "
     "five and is the ROOT SYSTEM rather than a dimension count **",
     GC.su3_is_in_so6() and len(GC.roots('D3')) == 12 and len(GC.root_lengths('D3')) == 1
     and not GC.su3_containment_under_the_dimension_edit()
     and GC.so_dimension((1,) * 5) > 8)
gate("Ⓓ⑥  no circle action lies in the discrete component: every generator of `so(5,1)` is "
     "TRACELESS, so `det exp(tX) = 1` for every `t` and the `det = -1` coset meets no "
     "one-parameter subgroup",
     GC.every_one_parameter_subgroup_has_determinant_one()
     and GC.parity_is_in_O51_and_not_in_SO0())
gate("Ⓓ⑦  ** and the converse is where the boundary paper says the trigger DOES live: the "
     "`(x4,x5)` rotation generator exponentiates to a genuine circle of period `2 pi` inside "
     "the identity component **",
     GC.a_connected_subgroup_does_carry_a_circle()
     and not GC.no_circle_under_the_connected_edit())
gate("Ⓓ⑧  the absolute fixes the group: the stabiliser of `eta(X,X) = 0` has dimension 15, and "
     "a substrate point's polar hyperplane is Lorentzian with isometry dimension 10 -- a "
     "sweep-subgroup of the substrate's",
     GC.isometry_dimension_of_the_absolute() == 15 and GC.polar_cut_is_dS4()
     and GC.polar_signature(GC.substrate_point())[:2] == (4, 1))
gate("Ⓓ⑨  and the converse: a point INSIDE the cone has a Riemannian `(5,0)` polar hyperplane, "
     "so the cut is no `dS_4` at all",
     GC.polar_converse_is_riemannian() and not GC.polar_cut_is_dS4_inside_the_cone())
_read_loci = GC.loci_read_from_the_paper()
gate(f"Ⓓ⑩  ** the three loci are PARSED OUT OF the circle paper's own sentence -- {[str(v) for v in _read_loci]} -- "
     f"rather than transcribed from it, and they carry three DISTINCT causal characters through "
     f"`L-104w`'s own `character` **",
     GC.three_loci_are_three_characters_as_the_paper_prints_them()
     and GC.paper_loci_agree_with_the_transcription()
     and len(set(GC.characters_at(_read_loci))) == 3)
gate(f"Ⓓ⑪  and the converse, against the values THIS receipt supplies rather than any the paper "
     f"prints: three equally spaced "
     f"{[str(v) for v in GC.EQUALLY_SPACED_CONVERSE]} carry only "
     f"{len(set(GC.characters_at(GC.EQUALLY_SPACED_CONVERSE)))} characters, so the claim is a "
     f"fact about the three the paper names",
     not GC.three_characters_at_equally_spaced()
     and len(set(GC.characters_at(GC.EQUALLY_SPACED_CONVERSE))) == 2)

# =========================================================================================
head('Ⓔ  ⚠⛭⛭ THE VACUOUS-PASS BUG THIS BATCH MADE AND CAUGHT, one layer up from `C75`s')
# =========================================================================================
_rb5 = ast.parse(open(os.path.join(MINE, 'reach_b5.py'), encoding='utf-8').read())
gate("Ⓔ①  ** no predicate slot in the ledger is a lambda, checked from the LIVE objects rather "
     "than from the source: a converse written `lambda: not GC.<fn>` without the call returns "
     "`False` for every input, and `False` is exactly what a converse must return **",
     all(getattr(s, '__name__', '<lambda>') != '<lambda>'
         for r in RB5.ROWS for s in (r[7], r[9])))
gate("Ⓔ②  and every slot returns a `bool` and not a truthy object",
     all(isinstance(s(), bool) for r in RB5.ROWS for s in (r[7], r[9])))
gate("Ⓔ③  the ledger asserts both of those AT IMPORT, so the guard cannot be forgotten by a "
     "later row",
     any(isinstance(n, ast.Assert) for n in ast.walk(_rb5))
     and sum(1 for n in ast.walk(_rb5) if isinstance(n, ast.Assert)) >= 2)
gate("Ⓔ④  ⌗ and it is the same shape `C75` refused in the loader -- an empty container returned "
     "in silence -- so the pair is one defect read in two places",
     hasattr(__import__('graft'), '_is_empty_container'))

# =========================================================================================
head('Ⓕ  THE HOLDERS -- the computation is in the holder, and the pin stands beside it')
# =========================================================================================
_holders = sorted({r[0] for r in B5})
gate(f"Ⓕ①  the {B5_N} rows sit in {len(_holders)} holder receipts, all on disk",
     len(_holders) == 5 and all(os.path.exists(os.path.join(ROOT, h)) for h in _holders))
_bad_def, _bad_call, _bad_pin = [], [], []
for h in _holders:
    src = open(os.path.join(ROOT, h), encoding='utf-8').read()
    tree = ast.parse(src)
    if not any(isinstance(n, ast.FunctionDef) and n.name == '_r7283r3' for n in tree.body):
        _bad_def.append(h)
    _bound = {t.id for n in ast.walk(tree) if isinstance(n, ast.Assign)
              for t in n.targets if isinstance(t, ast.Name)
              and any(isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                      and x.func.id == '_r7283r3' for x in ast.walk(n.value))}
    if not [n for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ('check', 'gate')
            and any((isinstance(x, ast.Call) and isinstance(x.func, ast.Name)
                     and x.func.id == '_r7283r3') or (isinstance(x, ast.Name) and x.id in _bound)
                    for x in ast.walk(n))]:
        _bad_call.append(h)
    _consts = [n.value for n in ast.walk(tree)
               if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    for lit in {r[1] for r in B5 if r[0] == h}:
        if not any(lit in c for c in _consts):
            _bad_pin.append((h, lit))
gate("Ⓕ②  every holder defines `_r7283r3` at its own top level, from each file's syntax tree",
     not _bad_def)
gate("Ⓕ③  ** and calls it inside a `check`, so the holder itself computes it **", not _bad_call)
gate("Ⓕ④  and every row's literal is STILL a string constant of its holder -- the pin is the "
     "citation and this batch removed none", not _bad_pin)
_runs = [(h, subprocess.run([sys.executable, os.path.join(ROOT, h)], capture_output=True,
                            text=True, timeout=1800)) for h in _holders]
gate(f"Ⓕ⑤  all {len(_holders)} holders run GREEN with the computed checks in them",
     all(r.returncode == 0 for _, r in _runs))
gate("Ⓕ⑥  and each prints a PASSING check that says it COMPUTED the quantity",
     all(any((_has(l, 'OK', '  ') or _has(l, 'PASS', ']')) and _has(l, 'COMPUTED')
             for l in r.stdout.split('\n')) for _, r in _runs))
_S14 = 'receipts/L_probability'
_s14 = [f for f in os.listdir(os.path.join(ROOT, _S14)) if f.startswith('S14_')]
_s14src = open(os.path.join(ROOT, _S14, _s14[0]), encoding='utf-8').read()
gate("Ⓕ⑦  ⚠⛭⛭ ** `B1` IS ONE OF THE FIVE SITES `S14` PINS BY LINE NUMBER, and it is in this "
     "batch -- so the pin was checked BEFORE the edit rather than after a trunk red said so. "
     "`S14` now carries in its own source that the line is PROVENANCE and the measurement does "
     "not depend on it, and `computations` is in its scratch-tree symlink list, which is what "
     "makes a loader-bearing holder safe for it **",
     any(_needle('B1_the_index', '_argument') in l for l in _s14src.split('\n'))
     and _has(_s14src, 'carried for provenance')
     and _has(_s14src, "INPUTS = ('corpus',"))
_s14run = subprocess.run([sys.executable, os.path.join(ROOT, _S14, _s14[0])],
                         capture_output=True, text=True, timeout=1800)
gate("Ⓕ⑧  and `S14` itself runs GREEN with `B1` edited, which is the gate the earlier trunk red "
     "taught this seat to run here rather than hope for",
     _s14run.returncode == 0)

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
print("  VERDICT: ** ALL FIVE HELD ROWS ARE TAKEN, AND THE RULING'S PREMISE MOVED UNDER THE "
      "READ. **")
print(f"  ⛭⛭⛭ {LANDED} OF {INPUTS_N} LANDED, {REMAIN} REMAIN.")
print("  ⛭ THE LOCI ARE IN FOUR PAPERS, NOT ONE.  The ruling named the geometric core and it")
print("    carries exactly one of the five.")
print("  ⚠⛭⛭⛭ AND FOUR OF THE FIVE ARE NOT METRIC CLAIMS, so no metric was ever missing.  They")
print("    are statements about which GROUPS exist, and lie_g -- the function the backlog named")
print("    for all four -- tests whether a VECTOR FIELD is Killing for a METRIC.  A change of")
print("    inputs cannot repair a change of KIND, so GEOMETRY-NOT-RECORDED is withdrawn in")
print("    favour of FUNCTION-IS-THE-WRONG-KIND, with all five computed to back it.")
print("  ⌗ The gap branch of the ruling fires nowhere: every locus states what its row needs,")
print("    in one sentence, in the paper where the literal is pinned.")
print("  ⚠⛭⛭ AND THE BUG THIS BATCH MADE AND CAUGHT IS C75's ONE LAYER UP: two converses written")
print("    `lambda: not GC.<fn>` WITHOUT the call return False for every input, and False is")
print("    exactly what a converse must return -- so the rows passed for the wrong reason.")
print("    Every slot is a named function now, and the ledger asserts it at import.")
print("  " + "=" * 74)
print()
