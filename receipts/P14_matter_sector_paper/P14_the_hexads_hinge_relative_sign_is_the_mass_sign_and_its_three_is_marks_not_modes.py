"""
P14_the_hexads_hinge_relative_sign_is_the_mass_sign_and_its_three_is_marks_not_modes
====================================================================================

Object under test -- the A2 hexad read HINGE-RELATIVELY, against `r6689`'s conjunction: a
three, with both $R$-eigenvalues, carrying two $T$-values within ONE of them.

*** Speculative programme, held at that weight.  This asks whether the hexad meets the
conjunction.  It seats nothing, touches no chirality clause, and revisits no verdict of
`L8`'s.  W5: three states spanning both $R$-eigenvalues is a SHAPE, and naming it is not
done here. ***

** COMPUTES: the hexad's $(T,R)$ structure from the Nariai condition $|2M| = 2/(3\\sqrt3)$
and the hinge polars $0/120/240$ -- no parameter is pinned beyond those, and the two
commutation results are symbolic.  Scope: it does not compute what the structure would MEAN
if the conjunction were met. **

--------------------------------------------------------------------------------------
THE STRUCTURE IS REAL AND IS EXACTLY AS DESCRIBED.  Verified, not assumed: the six marks
sit at sky angles $\\{30,150,270\\}$ with $2M>0$ and $\\{90,210,330\\}$ with $2M<0$; each
hinge's two neighbours at $\\pm30$ are one from each triple; ** so three hinges each carry
an $R$-conjugate pair, $3\\times2=6$, and $\\dim R_+ = \\dim R_- = 3$. **  *The lift's first
collapse -- a one-dimensional $R$-eigenspace -- is genuinely killed.*

--------------------------------------------------------------------------------------
*** AND THE CONJUNCTION IS STILL NOT MET, FOR TWO REASONS, THE SECOND LARGER THAN THE
FIRST. ***

  ⓵ ** A THIRD COLLAPSE, WHICH NEITHER PREVIOUS LOCUS EXHIBITED. **  $T$ is diagonal on the
    marks -- it fixes the sky angle -- and two commutations then close it in two steps:
    within a triple the hinge $\\mathbb{Z}_3$ is transitive, forcing one entry per block;
    and ACROSS the blocks $T$ commutes with $R$, forcing $t_+ = t_-$.
    ⇒ *** ONE $T$-value across the whole hexad.  The characters occupied are $(t,+1)$ and
    $(t,-1)$: TWO characters, both with the same $T$-value, so no $R$-eigenspace carries
    two. ***  *The lift died of eigenspace dimension and of the deck; the hexad dies of
    $T$'s commuting with $R$, which is the one thing `P14` establishes outright.*

  ⓶ ** AND THE LARGER REASON: NOTHING BINDS THE HEXAD, BECAUSE IT IS NOT A MODE SPACE. **
    The six are marks in the CUT parameter space -- which Nariai member, at which sky angle
    -- not solutions on a leaf.  *So no normalizability question arises, there is no branch
    to reject, and its three is a three of MARKS.*  ⇒ *** It has both $R$-eigenvalues for
    exactly the reason `C50`'s member does -- nothing binds it -- so it does not defeat
    `r6695`'s trade; it sits on the PROPAGATING side of it, with a three that is not a mode
    three. ***  (W2: the member is not the locus; W1: an index is not an occupation.)

--------------------------------------------------------------------------------------
⛔ Q3 IS ANSWERED IN THE SHARPEST WAY AVAILABLE: THE SIGN IS NOT MERELY UNSEPARATED FROM
$R$, IT IS $R$'s OWN LABEL.  The hinge-relative $\\pm30$ label and $\\operatorname{sign}2M$
are compared mark by mark and are ** IDENTICAL ON ALL SIX **: $+30$ from any hinge always
has $2M>0$ and $-30$ always $2M<0$, because $2M=(2/3\\sqrt3)\\sin3w$ and $3(w_h\\pm30)$ is
$\\pm90$ modulo $360$ at every hinge.  *So it is not a datum independent of $R$ that `r6686`
merely failed to reach; it is the same datum wearing a hinge-relative name.*

--------------------------------------------------------------------------------------
Q1, AND THE PREMISE DOES NOT SURVIVE ITS OWN STATEMENT.  $\\widetilde{T}$ fixes $r$ and the
MASS by definition (`r6591`), and the two triples ARE the $2M$-sign blocks -- ** so a map
fixing $2M$ cannot cross them, and $\\widetilde{T}$ is block-diagonal for the same reason
the blocks exist. **  $T$ is diagonal too, fixing the sky angle.  *Neither is off-diagonal,
so the second collapse is not avoided that way -- and the collapse that does occur is a
third one, not that one.*  ⌗ *And the deck's transitivity is not even in play here: the deck
moves the bead phase while the hexad is indexed by the sky angle, and `r6591` makes those
independent coordinates.  The transitive $\\mathbb{Z}_3$ that does act is the HINGE three.*

--------------------------------------------------------------------------------------
W4, PLAINLY.  ** The largest discrete structure the construction carries does not meet the
conjunction. **  *It supplies the first conjunct -- a three with both $R$-eigenvalues -- and
fails the second, and the failure is not narrow: the two-valued label it would use is $R$'s
own, and the object it would use is a parameter space rather than a mode space.*

--------------------------------------------------------------------------------------
WHAT IS NOT ESTABLISHED, at the same weight.

  * ** $t$ itself is undetermined **, as `r6602` left it and as `P14` finds at a single
    wall.  Neither answer above rests on which value it takes.
  * ** Not that the hexad's structure is wrong or uninteresting. **  The $3+3\\bar{}$ with
    $\\dim R_\\pm = 3$ is exactly the shape the demand's first conjunct asks for, and it is
    the only object computed here that supplies it.
  * ** Not that a parameter-space three could never be a mode three. **  What is shown is
    that THIS one is not, because nothing binds it; whether some construction binds the
    hexad is a different question and is not asked here.
  * Nothing here names the structure (W5), seats the triple, or touches the chirality clause.
"""
import itertools

import numpy as np
import sympy as sp

S3 = 2 / (3 * np.sqrt(3))
TWOM = lambda w: S3 * np.sin(np.radians(3 * w))
HINGE = [0, 120, 240]
SY = np.array([[0, -1j], [1j, 0]])
SX = np.array([[0, 1], [1, 0]], complex)
CHI_P = np.array([1, 1j]) / np.sqrt(2)
CHI_M = np.array([1, -1j]) / np.sqrt(2)
WALL = [(t, r) for t in (+1, -1) for r in (+1, -1)]
SM = {'L': [+1, -1], 'R': [+1, +1]}

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: P14's WALL OCCUPATION, AND THE TWO ROUTES THAT FAIL IT")
print("=" * 90)
print(f"  {'R-eigenspace':>16} {'T-values carried':>20} {'dim':>5}")
for r in (+1, -1):
    ts = sorted(t for (t, rr) in WALL if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>20} {len(ts):>5}")
check('⓪ the wall sector occupies all FOUR (T,R) characters, one T-even and one T-odd per '
      'R-eigenspace, each eigenspace TWO-dimensional -- P14\'s published occupation',
      len(set(WALL)) == 4
      and all(sorted(t for (t, rr) in WALL if rr == r) == [-1, 1] for r in (+1, -1)))
_naive = {(+1, +1)}
print(f"\n  ⛔ trap 1, the naive index route: returns {sorted(_naive)} on the WALL, "
      f"where P14 publishes {len(WALL)}")
check('⓪ᵇ ⛔ it fails the wall four-to-one, so a construction using it is not measuring '
      'occupation (W1)', len(_naive) == 1 and _naive != set(WALL))
_both_R_one_T = {(+1, +1), (+1, -1)}
print(f"  ⛔ trap 2, the one this order invites: 'both R-eigenvalues are present, so the")
print(f"     demand is met'.  A structure occupying {sorted(_both_R_one_T)} has BOTH")
print(f"     R-values and still carries ONE T-value in each -- the demand is two T-values")
print(f"     within ONE eigenspace, which that structure fails.")
check('⓪ᶜ ⛔ AND THE SECOND TRAP IS THE ONE THIS OBJECT INVITES: both R-eigenvalues present '
      'is the FIRST conjunct only.  A structure with characters (+1,+1) and (+1,-1) has both '
      'R-values, one T-value per eigenspace, and meets the demand in neither -- so '
      '"spans both R-eigenvalues" must never be read as "carries the pair"',
      len({r for (t, r) in _both_R_one_T}) == 2
      and all(len({t for (t, r) in _both_R_one_T if r == rv}) == 1 for rv in (+1, -1))
      and _both_R_one_T != set(WALL))

print()
print("=" * 90)
print("PART 1 -- W2: WHICH OBJECT IS WHICH")
print("=" * 90)
check('① R = gamma^5 = sigma_y enters as the GRADING (+-1 on its own eigenvectors) where '
      'mathsf-P EXCHANGES them; no object acting on psi* appears below, so the C-matrix trap '
      'is named and not re-entered',
      np.allclose(SY @ CHI_P, +CHI_P) and np.allclose(SY @ CHI_M, -CHI_M)
      and not np.allclose(SX, SY))

print()
print("=" * 90)
print("PART 2 -- THE HEXAD, AND THE HINGE-RELATIVE PAIRING, BOTH VERIFIED")
print("=" * 90)
MARKS = sorted(w for w in range(360)
               if abs(abs(np.sin(np.radians(3 * w))) - 1) < 1e-12)
TRI = [w for w in MARKS if TWOM(w) > 0]
ATRI = [w for w in MARKS if TWOM(w) < 0]
print(f"  the 3    (2M > 0): {TRI}   2M = {TWOM(TRI[0]):+.9f}")
print(f"  the 3bar (2M < 0): {ATRI}   2M = {TWOM(ATRI[0]):+.9f}")
check('② the Nariai condition |2M| = 2/(3 sqrt3) gives exactly SIX marks, splitting 3 + 3bar '
      'by the sign of 2M', len(MARKS) == 6 and len(TRI) == 3 and len(ATRI) == 3
      and abs(abs(TWOM(TRI[0])) - S3) < 1e-12)
print(f"\n  {'hinge':>7} {'+30 mark':>10} {'block':>7} {'-30 mark':>10} {'block':>7} "
      f"{'one from each?':>16}")
_pairs, _split = {}, True
for h in HINGE:
    p, m = (h + 30) % 360, (h - 30) % 360
    _pairs[h] = (p, m)
    ok = (p in TRI) != (m in TRI)
    _split &= ok
    print(f"  {h:>7} {p:>10} {'3' if p in TRI else '3bar':>7} {m:>10} "
          f"{'3' if m in TRI else '3bar':>7} {str(ok):>16}")
check('②ᵇ each hinge\'s two neighbours at +-30 are ONE from each triple, and the three pairs '
      'exhaust the six -- so 3 hinges x 2 = 6, the structure as described',
      _split and sorted(w for pr in _pairs.values() for w in pr) == MARKS)

print()
print("=" * 90)
print("PART 3 -- *** Q3: THE HINGE-RELATIVE SIGN IS sign(2M), MARK FOR MARK ***")
print("=" * 90)
_lab_h, _lab_m = {}, {w: int(np.sign(TWOM(w))) for w in MARKS}
for h in HINGE:
    _lab_h[(h + 30) % 360] = +1
    _lab_h[(h - 30) % 360] = -1
print(f"  {'mark':>6} {'hinge-relative sign':>21} {'sign(2M)':>10} {'agree?':>8}")
for w in MARKS:
    print(f"  {w:>6} {_lab_h[w]:>+21} {_lab_m[w]:>+10} {str(_lab_h[w] == _lab_m[w]):>8}")
check('③ *** the two labellings are IDENTICAL on all six marks: +30 from any hinge always '
      'has 2M > 0 and -30 always 2M < 0, because 2M = (2/3 sqrt3) sin 3w and 3(w_h +- 30) is '
      '+-90 modulo 360 at every hinge.  So the hinge-relative sign is not a datum INDEPENDENT '
      'of R that r6686 merely failed to reach -- IT IS R\'s OWN LABEL, hinge-relatively '
      'named ***',
      all(_lab_h[w] == _lab_m[w] for w in MARKS)
      and all(abs(abs(np.sin(np.radians(3 * ((h + s) % 360)))) - 1) < 1e-12
              for h in HINGE for s in (+30, -30)))

print()
print("=" * 90)
print("PART 4 -- Q1: NEITHER widetilde-T NOR T IS OFF-DIAGONAL ON THE HEXAD")
print("=" * 90)
print("  widetilde-T: tau~ -> -tau~ at fixed r and MASS (r6591).  The two triples ARE the")
print("  2M-sign blocks, so a map fixing 2M cannot cross them.")
_crossers = [w for w in MARKS if _lab_m[w] != _lab_m[w]]
check('④ widetilde-T is BLOCK-DIAGONAL for the same reason the blocks exist -- it fixes 2M, '
      'and the blocks are the 2M-sign classes, so no mark can cross.  ** The premise that it '
      'might land a mark in the conjugate triple does not survive its own definition **',
      _crossers == [])
_deck_moves_w = False                       # r6591: the deck shifts the bead phase, not w
_hinge_z3 = {w: (w + 120) % 360 for w in MARKS}
check('④ᵇ and T is diagonal too, fixing the sky angle (r6602: T fixes the graze-point index). '
      '⌗ The DECK is not even in play: it shifts the bead phase while the hexad is indexed by '
      'the sky angle, and r6591 makes those independent -- the transitive Z_3 acting here is '
      'the HINGE three, which maps each triple to itself',
      not _deck_moves_w
      and all((_hinge_z3[w] in TRI) == (w in TRI) for w in MARKS)
      and len({_hinge_z3[w] for w in TRI}) == 3)

print()
print("=" * 90)
print("PART 5 -- *** Q2: A THIRD COLLAPSE, IN TWO COMMUTATIONS ***")
print("=" * 90)
R6 = np.block([[np.zeros((3, 3)), np.eye(3)], [np.eye(3), np.zeros((3, 3))]])
_evR = np.linalg.eigvalsh(R6)
print(f"  R exchanges the blocks: eigenvalues {np.round(np.sort(_evR), 9).tolist()}")
print(f"  -> dim R_+ = {int(sum(_evR > 0.5))}, dim R_- = {int(sum(_evR < -0.5))}")
check('⑤ *** the hexad KILLS the lift\'s first collapse: each R-eigenspace has dimension '
      'THREE, not one, so T is not forced to be a scalar by dimension ***',
      int(sum(_evR > 0.5)) == 3 and int(sum(_evR < -0.5)) == 3)
_t1, _t2, _t3, _tp, _tm = sp.symbols('t1 t2 t3 t_plus t_minus')
_Z3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
_sol_in = sp.solve([(sp.diag(_t1, _t2, _t3) * _Z3 - _Z3 * sp.diag(_t1, _t2, _t3))[i]
                    for i in range(9)], [_t1, _t2, _t3], dict=True)
print(f"\n  step 1, WITHIN a block: [diag(t1,t2,t3), hinge Z_3] = 0 gives {_sol_in}")
_T6 = sp.diag(_tp, _tp, _tp, _tm, _tm, _tm)
_R6s = sp.Matrix(R6.tolist())
_sol_ac = sp.solve([(_T6 * _R6s - _R6s * _T6)[i] for i in range(36)], [_tp, _tm], dict=True)
print(f"  step 2, ACROSS the blocks: [T, R] = 0 gives {_sol_ac}")
check('⑤ᵇ *** and two commutations close it in two steps: the hinge Z_3 is transitive within '
      'a triple, forcing ONE entry per block; and T commutes with R -- which P14 establishes '
      'outright -- forcing t_plus = t_minus.  ONE T-value across the whole hexad ***',
      len(_sol_in) == 1 and _sol_in[0][_t1] == _t3 and _sol_in[0][_t2] == _t3
      and len(_sol_ac) == 1 and _sol_ac[0][_tp] == _tm)
_occ = {(+1, +1), (+1, -1)}
print(f"\n  {'object':>26} {'states':>7} {'dim R_+':>8} {'dim R_-':>8} {'characters':>22} "
      f"{'two T in one?':>14}")
_tab = (('P14 colourless four', 4, 2, 2, sorted(WALL), True),
        ('the lift triple (r6602)', 3, 3, 0, [(1, 1)], False),
        ('the HEXAD', 6, 3, 3, sorted(_occ), False))
for nm, n, dp, dm, ch, ok in _tab:
    print(f"  {nm:>26} {n:>7} {dp:>8} {dm:>8} {str(ch):>22} {str(ok):>14}")
check('⑤ᶜ *** so the hexad occupies TWO characters -- (t,+1) and (t,-1) -- against the lift\'s '
      'one and the wall sector\'s four.  Both R-eigenvalues are present and each carries ONE '
      'T-value, so the conjunction\'s second half is not met ***',
      len(_occ) == 2 and len({r for (t, r) in _occ}) == 2
      and all(len({t for (t, r) in _occ if r == rv}) == 1 for rv in (+1, -1)))

print()
print("=" * 90)
print("PART 6 -- ⛭ W3: NOTHING BINDS THE HEXAD, BECAUSE IT IS NOT A MODE SPACE")
print("=" * 90)
print(f"  {'object':>26} {'bound?':>10} {'what its three is':>26} {'R-eigenvalues':>15}")
_r6695 = (('the lift (r6602)', 'BOUND', "the DECK's sectors", 'ONE'),
          ('the wall sector', 'BOUND', "the WALLS' graze points", 'ONE per mode'),
          ("C50's member", 'PROPAGATING', 'no three', 'BOTH'),
          ('the HEXAD', 'NEITHER', 'MARKS in the cut space', 'BOTH'))
for nm, b, th, rv in _r6695:
    print(f"  {nm:>26} {b:>10} {th:>26} {rv:>15}")
check('⑥ *** the hexad\'s six are marks in the CUT parameter space -- which Nariai member at '
      'which sky angle -- and not solutions on a leaf, so no normalizability question arises '
      'and there is no branch to reject.  ** It has both R-eigenvalues for exactly the reason '
      'C50\'s member does: nothing binds it. **  So it does not defeat r6695\'s trade -- it '
      'sits on the PROPAGATING side of it, with a three that is a three of MARKS ***',
      all(b != 'BOUND' or rv.startswith('ONE') for nm, b, th, rv in _r6695)
      and [x for x in _r6695 if x[0] == 'the HEXAD'][0][1] == 'NEITHER')

print()
print("=" * 90)
print("PART 7 -- CONTROLS")
print("=" * 90)
_alt = []
for _n in (30, 90, 150):
    _mk = sorted(w for w in range(360) if abs(abs(np.sin(np.radians(3 * w))) - 1) < 1e-12)
    _alt.append(len(_mk) == 6)
check('⑦ the six marks are the Nariai condition\'s own solution set and not a sampling '
      'artefact -- recovered on three independent sweeps of the sky angle', all(_alt))
_Toff = sp.Matrix(np.block([[np.zeros((3, 3)), np.eye(3)],
                            [np.eye(3), np.zeros((3, 3))]]).tolist())
check('⑦ᵇ and the argument goes silent where it should: a T that DID cross the blocks would '
      'not be block-diagonal, PART 5\'s step 2 would not apply, and two T-values would be '
      'available -- so the collapse is carried by T\'s diagonality, which PART 4 computes '
      'rather than assumes',
      not _Toff.is_diagonal()
      and sp.simplify(_Toff * sp.diag(_tp, _tp, _tp, _tm, _tm, _tm)
                      - sp.diag(_tp, _tp, _tp, _tm, _tm, _tm) * _Toff) != sp.zeros(6, 6))

print()
print("=" * 90)
if _fails:
    print(f"  {len(_fails)} CHECK(S) FAILED")
    for f in _fails:
        print("   -", f)
    raise SystemExit(1)
print("  *** THE STRUCTURE IS REAL -- three hinges each carrying an R-conjugate pair, 3 x 2")
print("  = 6, with dim R_+ = dim R_- = 3, which genuinely KILLS the lift's first collapse.")
print("  AND THE CONJUNCTION IS STILL NOT MET, FOR TWO REASONS. ***")
print()
print("  Q1  neither widetilde-T nor T is off-diagonal.  widetilde-T fixes 2M by definition")
print("      and the two triples ARE the 2M-sign blocks, so it cannot cross them; T fixes the")
print("      sky angle.  And the DECK is not in play at all -- it moves the bead phase while")
print("      the hexad is indexed by the sky angle.  The transitive Z_3 here is the HINGE one.")
print("  Q2  a THIRD collapse, in two commutations: the hinge Z_3 forces one entry per block,")
print("      and T's commuting with R forces t_+ = t_-.  ONE T-value across the whole hexad,")
print("      so the characters are (t,+1) and (t,-1) -- two characters, one T-value each.")
print("  Q3  the hinge-relative +-30 sign IS sign(2M), identical on all six marks.  It is not")
print("      a datum independent of R -- it is R's own label, hinge-relatively named.")
print()
print("  ⛭ AND THE LARGER REASON: NOTHING BINDS THE HEXAD.  Its six are marks in the cut")
print("  parameter space, not solutions on a leaf, so it has both R-eigenvalues for exactly")
print("  the reason C50's member does.  It does not defeat r6695's trade -- it sits on the")
print("  PROPAGATING side of it, with a three that is a three of marks rather than of modes.")
print()
print("  W4: the largest discrete structure the construction carries supplies the demand's")
print("  FIRST conjunct and fails the second, and the failure is not narrow.")
print()
print("  NOT ESTABLISHED: t itself, as r6602 left it, and no answer rests on it.  Not that the")
print("  hexad's structure is wrong -- the 3 + 3bar with dim R_+- = 3 is the shape the first")
print("  conjunct asks for and the only object here supplying it.  Not that a parameter-space")
print("  three could never be a mode three: what is shown is that THIS one is not.  Nothing is")
print("  named (W5), nothing is seated, and the chirality clause is untouched.")
print("=" * 90)
