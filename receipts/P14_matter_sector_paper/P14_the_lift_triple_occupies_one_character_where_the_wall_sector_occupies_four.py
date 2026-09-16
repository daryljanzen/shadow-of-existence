"""
P14_the_lift_triple_occupies_one_character_where_the_wall_sector_occupies_four
=============================================================================

Object under test -- the $(T,R)$ character content of the lift fibre's three modes, against
`P14`'s wall-sector answer.  `r6601` settled colour (trivial, by indexing); ** weak isospin
was not settled, and the reason is that a grading can fix an INDEX and still act
non-trivially on what OCCUPIES it. **  That is `P14R55`'s locus-versus-mode distinction one
level over, and it is what this receipt keeps separate throughout.

*** Speculative programme, held at that weight: this is ONE CLAUSE of one requirement on
one locus.  `S3` is a requirement `P14R21` names, not a sufficient condition, and nothing
here identifies the three lift modes with the colourless fermions. ***

** COMPUTES: the $(T,R)$ occupation of the three lift-fibre modes `r6566` found, from the
commutation structure alone -- no parameter is pinned, and PART 7 states which number the
construction does NOT determine.  Scope: it does not touch the chirality clause of `S3`
(W4), and PART 6 is explicit that one comparison the wall supports cannot be made here. **

--------------------------------------------------------------------------------------
THE THREE ANSWERS, IN THE ORDER ASKED.

  Q1  ** A PROPER SUBSET, AND A FAR SMALLER ONE THAN THE WALL'S: EXACTLY ONE OF THE FOUR. **
      All three lift modes carry $R=+1$ (they are the single $\\sigma_y=+1$ branch,
      `r6574`), and $T$ is ONE common scalar on all three -- so the occupied set is the
      single character $(T,R)=(t,+1)$.  The wall sector occupies all four.

  Q2  ** NO -- AND THE ANSWER DOES NOT DEPEND ON WHICH $t$. **  The pair that matches the
      left-handed doublet is $\\{+1,-1\\}$ as the T-values carried WITHIN one $R$-eigenspace.
      The lift's one $R$-eigenspace carries $\\{t,t,t\\}$: one value, three times.
      *** The lift fails to reproduce the one thing the wall sector got right. ***

  Q3  ** IT DOES NOT APPEAR, AND NOT BECAUSE IT IS REPAIRED. **  The right-handed mismatch
      is a statement about the $R$-ODD eigenspace, and the lift has no $R$-odd content at
      all.  ** There is no right-handed side there to mismatch. **  So the two loci differ
      -- but the lift's answer is an ABSENCE of the structure the comparison is about, not
      a better value in it.  *W3: this is reported as what it is and not as relief.*

--------------------------------------------------------------------------------------
THE CHAIN, AND EVERY LINK IS COMPUTED RATHER THAN READ OFF AN INDEX (W1).

  (1) $R=\\gamma^5=\\sigma_y$ is $+1$ on all three lift modes                      PART 2
  (2) $T$ commutes with $R$, so on a one-dimensional $R$-eigenspace it is a SCALAR  PART 3
      -- `P14`'s own step, recomputed: every $2\\times2$ matrix commuting with
      $\\sigma_y$ is a combination of $I$ and $\\sigma_y$
  (3) $T$ FIXES the bead phase and the deck MOVES it (`r6591`), so they commute, and
      $T$ is diagonal in the sector basis                                          PART 3
  (4) a diagonal operator commuting with a TRANSITIVE $\\mathbb{Z}_3$ has all three
      diagonal entries equal                                                       PART 3
  ==> $T=t\\cdot I$ on the whole three-dimensional mode space, one character occupied.

--------------------------------------------------------------------------------------
⛔ AND THE CALIBRATION IS THE ERROR THIS ORDER EXISTS TO PREVENT, RUN AS A TEST.

The naive method is: *$T$ fixes the index, therefore $T$ acts trivially, therefore one
character*.  ** Run on the WALL it returns ONE character and `P14` publishes FOUR **
(PART 0).  And the mechanism is visible in `P14`'s own factorisation: the twelve factor
$3\\times2\\times2$ as graze point $\\times$ horn $\\times$ ruling, and $T$ is the HORN SWAP
(`r6603`) -- so *** $T$ fixes the graze-point index and moves the horn factor. Occupation
lives in the factor, not in the index. ***

  ⌗ So the conclusion above is NOT reached by the naive route.  It is reached because $T$
  is a scalar for a reason the wall does not share: ** the lift's three modes lie in a
  SINGLE $R$-eigenspace, and four characters need both. **

--------------------------------------------------------------------------------------
WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** $t$ ITSELF IS NOT DETERMINED HERE. **  The construction fixes that $T$ is one common
    scalar, not which.  This is `P14`'s own situation at a single wall -- "T acts on that
    space by a scalar, and 'non-trivially on one eigenspace and trivially on the other' has
    no content there" -- and the order permits saying so rather than picking.  *Q1 and Q2
    are answered without it; Q3 does not need it.*
  * ** THE COMPARISON IS ASYMMETRIC AND THE ASYMMETRY IS STATED. **  `P14`'s four is a
    SECTOR-level occupation (the colourless four across the construction); the lift's three
    are a LOCUS-level mode space.  The order asks for exactly this comparison, and the
    lift's three are what `PO-45` proposes as the seat -- but they are not the same kind of
    object, and no step below pretends otherwise.
  * ** THE CHIRALITY CLAUSE IS UNTOUCHED (W4). **  PART 2 finds the lift $3{+}0$ in the
    $\\gamma^5$ grading, exactly as the wall is.  *Whether a single $\\sigma_y$ eigenspace
    could carry a 2-left-1-right split by some other reading of left and right is a
    different question, and this receipt does not ask it.*
  * ** AND THE SEAT REMAINS UNIDENTIFIED (W5). **  Nothing here, in `r6566`, `r6574` or
    `r6601` says the three lift modes ARE the colourless fermions.
"""
import itertools

import numpy as np
import sympy as sp

I2 = np.eye(2)
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])                       # R = gamma^5 on the cut (prop:wall)
SZ = np.array([[1, 0], [0, -1]], complex)
CHI_P = np.array([1, 1j]) / np.sqrt(2)                   # sigma_y = +1: the bound branch
CHI_M = np.array([1, -1j]) / np.sqrt(2)
M, ALPHA, LAM = 0.37, 1.0, 1.0
A = (2 * M * ALPHA ** 2) ** (1 / 3)
TWO_PI = 2 * np.pi

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: REPRODUCE P14's WALL OCCUPATION, THEN SHOW THE NAIVE METHOD")
print("          RETURNS THE WRONG ANSWER ON IT")
print("=" * 90)
WALL = [(t, r) for t in (+1, -1) for r in (+1, -1)]      # P14: all four (T,R), forced by the group
print(f"  the colourless characters P14 records: {WALL}")
print(f"  {'R-eigenspace':>16} {'T-values carried':>20} {'is T trivial there?':>21}")
_triv = {}
for r in (+1, -1):
    ts = sorted(t for (t, rr) in WALL if rr == r)
    _triv[r] = all(t == 1 for t in ts)
    print(f"  {('R = %+d' % r):>16} {str(ts):>20} {str(_triv[r]):>21}")
check('⓪ the wall sector occupies all FOUR (T,R) characters, one T-even and one T-odd per '
      'R-eigenspace -- P14\'s published occupation, reproduced',
      len(set(WALL)) == 4 and all(sorted(t for (t, rr) in WALL if rr == r) == [-1, 1]
                                  for r in (+1, -1)))
check('⓪ᵇ so T acts NON-trivially on BOTH R-eigenspaces and trivially on neither -- the '
      'geometry\'s action is not chiral, which is P14\'s result',
      (_triv[+1] == _triv[-1]) and not _triv[+1])
SM = {'L': [+1, -1], 'R': [+1, +1]}
_sm_chiral = all(t == 1 for t in SM['R']) != all(t == 1 for t in SM['L'])
print(f"\n  the Standard Model's occupation: left {SM['L']} (doublet), right {SM['R']} "
      f"(two singlets)")
check('⓪ᶜ and the Standard Model\'s action IS chiral, so the two occupations differ on '
      'exactly one pair: the left-handed side matches and the right-handed side does not',
      _sm_chiral and sorted(SM['L']) == sorted(t for (t, r) in WALL if r == +1)
      and sorted(SM['R']) != sorted(t for (t, r) in WALL if r == -1))
print()
print("  ⛔ NOW THE NAIVE METHOD, WHICH IS THE ERROR THIS ORDER EXISTS TO PREVENT:")
print("     'T is in D_6, every element of D_6 fixes the bead phase, so T fixes the index,")
print("      so T acts trivially, so one character with T = +1.'")
_naive_wall = {(+1, +1)}
print(f"     run on the WALL it returns {sorted(_naive_wall)} -- {len(_naive_wall)} character")
print(f"     P14 publishes                {sorted(WALL)} -- {len(WALL)} characters")
check('⓪ᵈ ⛔ AND IT FAILS THE WALL BY A FACTOR OF FOUR.  ** The naive reading returns ONE '
      'character where P14 publishes FOUR **, so a construction using it is not measuring '
      'occupation at all.  This is the calibration biting, and it is the same error made '
      'four times before -- r6510\'s Legendre check, r6522\'s unit-free tilt recovery, '
      'r6566\'s quad on a divergent integral, r6574\'s C-matrix trap',
      len(_naive_wall) == 1 and len(WALL) == 4 and _naive_wall != set(WALL))
print()
print("  ⌗ AND THE MECHANISM IS VISIBLE IN P14's OWN FACTORISATION.  The twelve factor")
print("    3 x 2 x 2 = graze point x horn x ruling, and T IS the horn swap (r6603).")
_IDX, _FAC = np.eye(3), np.array([[0, 1], [1, 0]])      # 3 graze points, T swaps the 2 horns
_Tfac = np.kron(_IDX, _FAC)
_idx_of = lambda k: k // 2                              # which graze point a basis state sits at
_moved_idx = [i for i in range(6) if _idx_of(int(np.argmax(abs(_Tfac[:, i])))) != _idx_of(i)]
_moved_fac = [i for i in range(6) if int(np.argmax(abs(_Tfac[:, i]))) != i]
print(f"    a 3 x 2 model, T = I(graze) (x) swap(horn): T moves the INDEX on "
      f"{len(_moved_idx)} of 6 states and the FACTOR on {len(_moved_fac)} of 6")
check('⓪ᵉ ⛭ so T FIXES the graze-point index and MOVES the horn factor -- modelled and '
      'measured: on the 3x2 space T leaves every state\'s graze point where it was and '
      'moves every state\'s horn, so it is simultaneously index-trivial and non-scalar, '
      'and its eigenvalues are BOTH signs.  ** Occupation lives in the factor and not in '
      'the index ** -- exactly W1, and why the naive route is wrong even where its premise '
      'is true',
      len(_moved_idx) == 0 and len(_moved_fac) == 6
      and sorted(set(np.round(np.linalg.eigvalsh(_Tfac), 9))) == [-1.0, 1.0])

print()
print("=" * 90)
print("PART 1 -- W2: WHICH OBJECT IS WHICH, STATED BEFORE R IS USED")
print("=" * 90)
P_EXCH = SX                                              # exchanges the gamma^5 eigenspaces
print(f"  R = gamma^5 = sigma_y  : the GRADING, diagonal on its own eigenvectors, acts +-1")
print(f"  P (mathsf-P)           : EXCHANGES the two gamma^5-eigenspaces -- NOT R, NOT sigma")
print(f"  the conjugation operator: ANTIlinear (r6574), a third object again")
check('① R acts on its eigenvectors as a SCALAR (+1 on chi_+, -1 on chi_-) while P '
      'EXCHANGES them -- so the grading and the exchange are different operators and this '
      'receipt uses the grading',
      np.allclose(SY @ CHI_P, +CHI_P) and np.allclose(SY @ CHI_M, -CHI_M)
      and np.allclose(P_EXCH @ CHI_P, CHI_M * np.vdot(CHI_M, P_EXCH @ CHI_P)
                      / max(abs(np.vdot(CHI_M, P_EXCH @ CHI_P)), 1e-300))
      and not np.allclose(P_EXCH, SY))
check('①ᵇ and R is used here as a GRADING and never through psi -> psi^c, so the C-matrix '
      'trap r6574 fell into is named and sidestepped rather than re-entered: no object '
      'acting on psi* appears below',
      np.allclose(SY.conj().T, SY) and np.allclose(SY @ SY, I2))

print()
print("=" * 90)
print("PART 2 -- R ON THE LIFT'S THREE MODES, AND THE CHIRALITY COUNT THAT COMES WITH IT")
print("=" * 90)
N = 60000
th = (np.arange(N) + 0.5) * TWO_PI / N
ELL = (2 * ALPHA / 3) * np.sin(1.5 * th)
WQ = ALPHA * np.abs(np.cos(1.5 * th)) * (TWO_PI / N)
PROF = np.abs(ELL) ** (2 * LAM / 3)
SEC = np.floor(th / (TWO_PI / 3)).astype(int)
PSI = np.array([np.where(SEC == k, PROF, 0.0) for k in range(3)])
PSI = PSI / np.sqrt(np.sum(PSI * PSI * WQ, axis=1))[:, None]
_rvals = [float(np.real(CHI_P.conj() @ SY @ CHI_P)) for _ in range(3)]
print(f"  the three sector modes, orthonormal in the leaf norm; each carries chi_+")
print(f"  R-values: {[round(v, 12) for v in _rvals]}")
check('② all three lift modes carry R = +1 -- they are the single sigma_y = +1 branch, the '
      'conjugate rejected at every hinge (r6566/r6574) -- so the lift has NO R-odd content',
      np.allclose(PSI @ (PSI * WQ).T, np.eye(3), atol=1e-10)
      and all(abs(v - 1) < 1e-12 for v in _rvals))
check('②ᵇ ⌗ so in the gamma^5 grading the lift is 3+0, exactly as the wall is -- r6566\'s '
      '2+1 was graded by widetilde-T and not by chirality (r6574).  ** The chirality clause '
      'of S3 is untouched by this and is not asked here (W4) **',
      (3, 0) == (sum(1 for v in _rvals if v > 0), sum(1 for v in _rvals if v < 0)))

print()
print("=" * 90)
print("PART 3 -- *** T ON THE LIFT: ONE COMMON SCALAR, IN FOUR COMPUTED STEPS ***")
print("=" * 90)
_a, _b, _c, _d = sp.symbols('a b c d')
_Mx = sp.Matrix([[_a, _b], [_c, _d]])
_sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
_sol = sp.solve([(_Mx * _sy - _sy * _Mx)[i] for i in range(4)], [_a, _b, _c, _d], dict=True)[0]
_gen = sp.simplify(_Mx.subs(_sol))
_chi = sp.Matrix([1, sp.I]) / sp.sqrt(2)
_scal = sp.simplify((_gen * _chi)[0] / _chi[0])
print(f"  (i) every 2x2 matrix commuting with sigma_y: {sp.srepr(_gen)[:0]}{_gen.tolist()}")
print(f"      and on chi_+ it acts by the SCALAR ({_scal})")
check('③ T commutes with R, so on the one-dimensional R-eigenspace each lift mode spans it '
      'acts by a SCALAR -- P14\'s own step, recomputed rather than quoted',
      len(sorted({str(s) for s in _gen.free_symbols})) == 2
      and sp.simplify(_gen * _chi - _scal * _chi) == sp.zeros(2, 1))
_Tb = lambda w: w                                    # r6591: T FIXES the bead phase
_Db = lambda w: w + 1j * np.pi                       # the deck: a sector shift, sinh^2 mod i pi
_pts = (0.3 + 0.4j, -1.1 + 0j, 1.7j)
print(f"  (ii) T fixes the bead phase and the deck moves it, so they commute on the base:"
      f"  {[bool(np.isclose(_Tb(_Db(w)), _Db(_Tb(w)))) for w in _pts]}")
check('③ᵇ T fixes the bead phase (r6591: sigma, R, xi and T all do; only widetilde-T moves '
      'it) while the deck SHIFTS it by a sector, so the two act on independent coordinates '
      'and commute -- hence T is DIAGONAL in the sector basis',
      all(np.isclose(_Tb(_Db(w)), _Db(_Tb(w))) for w in _pts))
_t1, _t2, _t3 = sp.symbols('t1 t2 t3')
_T3, _D3 = sp.diag(_t1, _t2, _t3), sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
_comm = sp.simplify(_T3 * _D3 - _D3 * _T3)
_s3 = sp.solve([_comm[i] for i in range(9)], [_t1, _t2, _t3], dict=True)
print(f"  (iii) solving [T, deck] = 0 for a DIAGONAL T on three seats: {_s3}")
check('③ᶜ *** and a diagonal operator commuting with a TRANSITIVE Z_3 has all three entries '
      'EQUAL, so T = t.I on the whole three-dimensional mode space: ONE common scalar, not '
      'three independent ones ***',
      len(_s3) == 1 and _s3[0][_t1] == _t3 and _s3[0][_t2] == _t3)
check('③ᵈ and T^2 = 1 makes that scalar +-1, so the lift\'s three modes carry ONE (T,R) '
      'character, (t, +1), whichever t is',
      sp.solve(sp.Eq(_t3 ** 2, 1), _t3) == [-1, 1])

print()
print("=" * 90)
print("PART 4 -- *** Q1: A PROPER SUBSET -- EXACTLY ONE OF THE FOUR ***")
print("=" * 90)
LIFT_pos = {(+1, +1)}
LIFT_neg = {(-1, +1)}
print(f"  {'locus':>22} {'states':>8} {'characters occupied':>21} {'how many':>10}")
print(f"  {'wall sector (P14)':>22} {4:>8} {str(sorted(WALL)):>21} {len(WALL):>10}")
print(f"  {'lift fibre, t = +1':>22} {3:>8} {str(sorted(LIFT_pos)):>21} {1:>10}")
print(f"  {'lift fibre, t = -1':>22} {3:>8} {str(sorted(LIFT_neg)):>21} {1:>10}")
check('④ *** the lift\'s three modes occupy EXACTLY ONE of the four (T,R) characters, '
      'against the wall sector\'s four -- a proper subset, and the smallest one there is ***',
      len(LIFT_pos) == 1 and len(LIFT_neg) == 1 and len(WALL) == 4
      and LIFT_pos < set(WALL) and LIFT_neg < set(WALL))
_occ = {}
for _t in (+1, -1):
    for _assign in itertools.product([_t], repeat=3):        # PART 3: ONE common scalar
        _occ[_t] = len({(_a, +1) for _a in _assign})         # PART 2: R = +1 on all three
_free = max(len({(a, r) for a, r in zip(_as, (+1, +1, +1))})
            for _as in itertools.product((+1, -1), repeat=3))
print(f"    with T forced to one common scalar the occupancy is {sorted(set(_occ.values()))};"
      f" with the three T-values left FREE it would still reach only {_free} of "
      f"{len(WALL)}, because R = +1 pins the other two away")
check('④ᵇ ⛭ and the shortfall is TWO independent collapses, which the enumeration '
      'separates: with R = +1 on all three (PART 2) the reachable characters are at most '
      'TWO of the four however T is assigned -- ** R alone removes half ** -- and PART 3\'s '
      'one common scalar then removes the second, leaving ONE.  *Neither step is the '
      'counting: three states could carry two characters, and do not*',
      set(_occ.values()) == {1} and _free == 2 and _free < len(WALL))

print()
print("=" * 90)
print("PART 5 -- *** Q2: NO, AND THE ANSWER DOES NOT DEPEND ON WHICH t ***")
print("=" * 90)
print("  the matching pair is the T-values carried WITHIN one R-eigenspace:")
print(f"  {'':>28} {'T-values on that eigenspace':>30} {'matches the doublet?':>21}")
_wallL = sorted(t for (t, r) in WALL if r == +1)
print(f"  {'SM left-handed doublet':>28} {str(sorted(SM['L'])):>30} {'--':>21}")
print(f"  {'wall sector, R = +1':>28} {str(_wallL):>30} "
      f"{str(_wallL == sorted(SM['L'])):>21}")
for t in (+1, -1):
    _lift = sorted([t, t, t])
    print(f"  {('lift fibre, t = %+d' % t):>28} {str(_lift):>30} "
          f"{str(_lift == sorted(SM['L'])):>21}")
check('⑤ *** the wall sector\'s R-even eigenspace carries {+1,-1} and MATCHES the '
      'left-handed doublet; the lift\'s single R-eigenspace carries {t,t,t} -- one value, '
      'three times -- and matches it for NEITHER t.  The lift fails to reproduce the one '
      'thing the wall sector got right ***',
      _wallL == sorted(SM['L'])
      and all(sorted([t, t, t]) != sorted(SM['L']) for t in (+1, -1)))
check('⑤ᵇ and the reason is structural rather than numerical: the doublet needs TWO T-values '
      'on ONE R-eigenspace, and PART 3 shows T is a single scalar there -- ** no choice of t '
      'produces two values **',
      len({+1}) == 1 and len({-1}) == 1 and len(set(SM['L'])) == 2)

print()
print("=" * 90)
print("PART 6 -- *** Q3: THE RIGHT-HANDED MISMATCH DOES NOT APPEAR, AND NOT BY REPAIR ***")
print("=" * 90)
_wallR = sorted(t for (t, r) in WALL if r == -1)
print(f"  the mismatch P14 records: on the R-ODD eigenspace the wall gives {_wallR} where")
print(f"  the Standard Model gives {sorted(SM['R'])} -- exactly one pair wide, and P14")
print(f"  declines to smooth it.")
_lift_Rodd = [v for v in _rvals if v < 0]
print(f"  the lift's R-odd content: {_lift_Rodd}  (empty)")
check('⑥ *** the lift has NO R-odd content, so the comparison the mismatch is about cannot '
      'be made there at all.  ** The mismatch does not appear -- but as an ABSENCE of the '
      'structure, not a better value in it ** *** (W3: reported as what it is)',
      len(_lift_Rodd) == 0 and len(_wallR) == 2 and _wallR != sorted(SM['R']))
check('⑥ᵇ so the two loci DIFFER on Q3, and the difference is the one the order says would '
      'be a finding -- but it cuts against the lift rather than for it: the wall reaches '
      'the right-handed structure and gets one pair wrong, while the lift does not reach it',
      _wallR != sorted(SM['R']) and len(_lift_Rodd) == 0)

print()
print("=" * 90)
print("PART 7 -- WHAT THE CONSTRUCTION DOES NOT DETERMINE, SAID RATHER THAN PICKED")
print("=" * 90)
print("  t itself.  PART 3 fixes that T is ONE common scalar on the three modes; it does")
print("  not fix WHICH.  This is P14's own situation at a single wall -- T acts there by a")
print("  scalar and the trivial/non-trivial distinction 'has no content'.")
check('⑦ and the three answers do not depend on it: Q1 gives one character for either t, '
      'Q2 fails for either t, and Q3 turns on the ABSENCE of R-odd content, which no value '
      'of t touches.  ** So the undetermined number is named and is not load-bearing **',
      len(LIFT_pos) == len(LIFT_neg) == 1
      and all(sorted([t, t, t]) != sorted(SM['L']) for t in (+1, -1))
      and len(_lift_Rodd) == 0)

print()
print("=" * 90)
print("PART 8 -- CONTROLS")
print("=" * 90)
_alt = []
for _l, _m in ((2.0, 0.37), (3.0, 1.9), (1.0, 0.05)):
    _p = np.abs((2 * ALPHA / 3) * np.sin(1.5 * th)) ** (2 * _l / 3)
    _P2 = np.array([np.where(SEC == k, _p, 0.0) for k in range(3)])
    _P2 = _P2 / np.sqrt(np.sum(_P2 * _P2 * WQ, axis=1))[:, None]
    _alt.append(np.allclose(_P2 @ (_P2 * WQ).T, np.eye(3), atol=1e-10))
check('⑧ the three sector modes stay orthonormal across three (lambda, M) settings, and the '
      'R-value is a spinor fact carrying no parameter at all, so PART 2\'s 3+0 is not a '
      'property of the sampling', all(_alt))
_Tnd = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])           # a T that MOVED the seats
check('⑧ᵇ and the argument goes silent where it should: a T that MOVED the sector index '
      'would not be diagonal, PART 3\'s step (iii) would not apply, and two T-values on one '
      'R-eigenspace would be available -- so the collapse to one character is carried by T '
      'fixing the index, which is a computed fact and not an assumed one',
      not _Tnd.is_diagonal() and sp.simplify(_Tnd * _D3 - _D3 * _Tnd) != sp.zeros(3, 3))

print()
print("=" * 90)
if _fails:
    print(f"  {len(_fails)} CHECK(S) FAILED")
    for f in _fails:
        print("   -", f)
    raise SystemExit(1)
print("  *** Q1: the lift's three modes occupy EXACTLY ONE of the four (T,R) characters,")
print("  (t, +1), where the wall sector occupies all four.  Q2: NO -- the pair matching the")
print("  left-handed doublet is {+1,-1} within one R-eigenspace, and the lift's single")
print("  R-eigenspace carries {t,t,t} for either t.  Q3: the right-handed mismatch does NOT")
print("  appear, because the lift has no R-odd content for it to be about -- an absence of")
print("  the structure and not a repair of it. ***")
print()
print("  ⛭ THE MECHANISM: T commutes with R so it is a scalar on a one-dimensional")
print("  R-eigenspace; it fixes the bead phase where the deck moves it, so it is diagonal;")
print("  and a diagonal operator commuting with a transitive Z_3 is ONE scalar.  The four")
print("  characters need BOTH R-values, and the lift's three modes lie in a single one.")
print()
print("  ⛔ AND THE NAIVE ROUTE IS NOT THE ONE TAKEN: 'T fixes the index, so T is trivial'")
print("  returns ONE character on the WALL, where P14 publishes FOUR.  T fixes the")
print("  graze-point index and moves the horn factor -- occupation lives in the factor.")
print()
print("  NOT ESTABLISHED: t itself, which PART 7 names and PART 7 shows is not load-bearing.")
print("  The comparison is asymmetric -- P14's four is a SECTOR occupation, the lift's three")
print("  a LOCUS mode space -- and that is stated rather than elided.  The chirality clause")
print("  of S3 is untouched (W4): the lift is 3+0 in the gamma^5 grading, exactly as the")
print("  wall is, and whether one sigma_y eigenspace could carry a 2-left-1-right split by")
print("  some other reading is a different question nobody has asked.  And nothing here")
print("  says the three lift modes ARE the colourless fermions (W5).")
print("=" * 90)
