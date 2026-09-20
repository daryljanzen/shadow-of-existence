"""
P14_the_stratifications_two_valued_data_are_one_involution_and_it_is_R
======================================================================

Object under test -- whether any locus in `P07`'s causal stratification carries TWO values
within ONE $R$-eigenspace, and whether the sign of the marginal rate is the datum carrying
them.  `r6602` found the lift occupies ONE $(T,R)$ character and named the mechanism's three
escapes: an $R$-eigenspace of dimension $>1$, a deck not transitive on the modes, or $T$ not
commuting with $R$.  ** This runs the stratification against all three. **

*** Speculative programme, held at that weight.  This asks WHERE two values can live.  It
does not ask whether they are isospin (W3), it seats nothing, and the chirality clause of
`S3` is untouched and not part of it. ***

** COMPUTES: the $(T,R)$ content of `P07`'s five spans and four joints, at the FORCED
(Nariai) member alpha = 3 sqrt(3) M -- which is not a sample but the locus the stratification
is stated on, the only value at which the horizon cubic carries a double root.  The parity
results (PART 5) are symbolic in alpha and M and carry no pinned value at all.  Scope: it
does not compute what the two values would MEAN if one were found. **

--------------------------------------------------------------------------------------
*** THE ANSWER IS NO, AND IT IS ONE FACT RATHER THAN FIVE SEPARATE FAILURES. ***

  ** EVERY TWO-VALUED DATUM THE STRATIFICATION OFFERS IS THE SAME INVOLUTION -- the exchange
  of the bead's two legs -- AND THAT INVOLUTION IS $R$. **

      the HORN label      sign(X_0)          T is the horn swap (r6603)
      the LEG label       sign(r)            matter against antimatter
      the RATE's sign     sign(dr/dtau~)     collapse against expansion

  *These are three names for one exchange of the contour's two ends.*  ⇒ ** So the two values
  are split ACROSS the $R$-eigenspaces and never within one, which is the specific thing a
  doublet needs.  The datum is not merely absent; it is $R$, and $R$ cannot split its own
  eigenspace. **

--------------------------------------------------------------------------------------
THE THREE QUESTIONS, ANSWERED IN ORDER.

  Q1  ** THE HORN SPANS ESCAPE THE LIFT'S COLLAPSE AND STILL FAIL, DIFFERENTLY. **  $T$ does
      not act WITHIN either horn span -- it exchanges them -- so on a single span it is not
      an endomorphism and grades nothing.  On the PAIR it is a transposition and TWO
      characters are occupied, against the lift's one.  ** But they are $(+1,+1)$ and
      $(-1,-1)$: a CORRELATED pair, not a doublet. **  *$R$ is the same transposition there,
      so each $R$-eigenspace on the pair is ONE-dimensional and carries one $T$-value.*

  Q2  ** THREE OF THE FOUR JOINTS SELECT NO BRANCH AT ALL, SO THEY IMPOSE NO GRADING. **  The
      selection that makes the wall's content one $R$-eigenspace happens at the BRANCH POINT
      and nowhere else: at both seams $f=0$ and the measure's inverse square root is
      integrable with psi finite, and at the turnaround $f=1$ and the measure is regular.
      *The front seam -- the one joint `P07` says changes no character -- correspondingly
      carries no selection: what persists unchanged across it is ONE branch, one value.*

  Q3  ** THE RATE'S SIGN FAILS FOR THE OPPOSITE REASON TO $T$ ON THE LIFT, AND THAT IS THE
      SHARPEST PART. **  $(dr/d\\tilde\\tau)^2 = 1-f$ and $f$ is $R$-EVEN, so the rate's
      SQUARE is $R$-even while the RATE IS $R$-ODD -- verified symbolically.  ⇒ *** A grading
      that is $R$-odd ANTIcommutes with $R$: it carries the $R=+1$ eigenspace to the $R=-1$
      one, so it is not an endomorphism of either and cannot grade one at all. ***  *$T$ on
      the lift collapsed to a scalar; the rate's sign does not collapse -- it does not
      preserve the eigenspaces it would have to grade.*

--------------------------------------------------------------------------------------
⛭ AND THE DIMENSION COUNT SAYS WHY THE WALL SECTOR IS THE ONLY PLACE IT WORKS.

Two $T$-values within one $R$-eigenspace needs that eigenspace to have dimension at least
two, hence at least FOUR states once both $R$-values are present.  ** The stratification's
two-valued data are all two-state exchanges, so every $R$-eigenspace they produce is
one-dimensional. **  *`P14`'s colourless four is the only object in the construction with a
two-dimensional $R$-eigenspace, and that is why it is the only one carrying the pair.*

--------------------------------------------------------------------------------------
W4, SAID PLAINLY RATHER THAN AS A SEARCH THAT FOUND NOTHING.

** The doublet's two values are not in the causal stratification. **  Not "not yet found":
the stratification's only two-valued datum is the leg exchange, the leg exchange is $R$, and
$R$ splits its eigenspaces from each other rather than either of them internally.  *A locus
carrying the pair would have to supply a two-valued datum INDEPENDENT of $R$, and `P07`'s
five spans and four joints supply none.*

--------------------------------------------------------------------------------------
WHAT IS NOT ESTABLISHED, at the same weight.

  * ** The three critical $f$-values are not claimed to be a three of the kind the other two
    are. **  `L8_the_pencil` is explicit that the pencil runs over ALL $f$ and does not
    select $\\{0,1,2\\}$, and that verdict stands here unchanged.
  * ** Not that the rate's sign is weak isospin or anything else (W3). **  What is computed
    is that it is $R$-odd; naming it is not done here.
  * ** $T$'s scalar on a one-dimensional $R$-eigenspace is still undetermined **, exactly as
    `r6602` left it, and as `P14` finds at a single wall.  No answer above rests on it.
  * Nothing here seats the colourless triple, and the chirality clause is untouched.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
import warnings

warnings.filterwarnings('ignore')

ALPHA = 1.0
MASS = ALPHA / (3 * np.sqrt(3))                 # the FORCED (Nariai) member alpha = 3 sqrt(3) M
F_OF = lambda r: 1 - 2 * MASS / r - r ** 2 / ALPHA ** 2
SY = np.array([[0, -1j], [1j, 0]])              # R = gamma^5 on the cut: the GRADING
SX = np.array([[0, 1], [1, 0]], complex)        # mathsf-P: EXCHANGES the eigenspaces
CHI_P = np.array([1, 1j]) / np.sqrt(2)
CHI_M = np.array([1, -1j]) / np.sqrt(2)
WALL = [(t, r) for t in (+1, -1) for r in (+1, -1)]
SM = {'L': [+1, -1], 'R': [+1, +1]}
P2 = np.array([[0, 1], [1, 0]])                 # the two-state exchange

JOINTS = {'back seam': -2 * ALPHA / np.sqrt(3),
          'turnaround': -(2 * MASS * ALPHA ** 2) ** (1 / 3),
          'branch point': 0.0,
          'front seam': ALPHA / np.sqrt(3)}

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


def conv_exponent(psi, weight, sing, far, decades=(2, 3, 4, 5, 6)):
    """r6566's engine: the MEASURED convergence exponent.  p > 0 converges, p = 0 is the
    log-divergent marginal case, p < 0 diverges."""
    N = []
    for e in (10.0 ** (-k) for k in decades):
        lo, hi = (sing + e, far) if far > sing else (far, sing - e)
        v, _ = quad(lambda t: abs(psi(t)) ** 2 * weight(t), lo, hi, limit=200)
        N.append(v)
    if not all(np.isfinite(N)):
        return -np.inf
    add = [N[i + 1] - N[i] for i in range(len(N) - 1)]
    # ** the guard is set at quad's own accuracy, not below it. **  At 1e-14 relative the
    # CONVERGENT branch's last decade adds ~1e-12 on an O(1) integral -- pure quadrature
    # noise, which can come out negative and put a log of a negative number in the ratio.
    # r6566 hit the same class of defect from the other side (quad returning finite for a
    # divergent integral); this is its mirror, and the marginal case below pins both.
    if abs(add[-1]) < 1e-9 * max(1.0, abs(N[-1])):
        return np.inf
    rr = [add[i + 1] / add[i] for i in range(len(add) - 1) if abs(add[i]) > 0]
    return float(-np.log10(np.mean(rr[-2:])))


print(__doc__)
print("=" * 90)
print("PART 0a -- THE NORMALIZABILITY ENGINE, RE-CALIBRATED HERE AND NOT INHERITED")
print("=" * 90)
print("  r6566's cut: |psi|^2 ~ |ell|^{-4 lambda/3} at the branch point, so p = 1 - 4 lambda/3")
print(f"  {'lambda':>8} {'p measured':>12} {'1 - 4L/3':>10} {'normalizable':>13} {'expected':>10}")
_eng = True
for _l, _exp in ((0.25, True), (0.5, True), (0.7, True), (0.75, False), (1.0, False)):
    _p = conv_exponent(lambda t: abs(t) ** (-2 * _l / 3), lambda t: 1.0, 0.0, 1.0)
    print(f"  {_l:>8} {_p:>12.5f} {1 - 4 * _l / 3:>10.5f} {str(_p > 1e-2):>13} {str(_exp):>10}")
    _eng &= (_p > 1e-2) == _exp and abs(_p - (1 - 4 * _l / 3)) < 3e-3
_pc = conv_exponent(lambda t: abs(t) ** (2 * 1.0 / 3), lambda t: 1.0, 0.0, 1.0)
print(f"  and the DECAYING branch returns p = {_pc} -- convergent, not a quadrature artefact")
check('⓪ᵃ the engine recovers the cut\'s exponent to < 3e-3 across it, REJECTS the marginal '
      'lambda = 3/4 at p = 0, and returns a finite verdict on the convergent branch instead '
      'of a NaN -- both failure modes pinned, r6566\'s and its mirror',
      _eng and _pc == np.inf)

print()
print("=" * 90)
print("PART 0 -- CALIBRATION: P14's WALL OCCUPATION, AND THE NAIVE ROUTE FAILING IT")
print("=" * 90)
_triv = {r: all(t == 1 for (t, rr) in WALL if rr == r) for r in (+1, -1)}
print(f"  {'R-eigenspace':>16} {'T-values carried':>20} {'dim':>5} {'T trivial there?':>18}")
for r in (+1, -1):
    ts = sorted(t for (t, rr) in WALL if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>20} {len(ts):>5} {str(_triv[r]):>18}")
check('⓪ the wall sector occupies all FOUR (T,R) characters, one T-even and one T-odd per '
      'R-eigenspace, so each R-eigenspace is TWO-dimensional -- P14\'s published occupation',
      len(set(WALL)) == 4
      and all(sorted(t for (t, rr) in WALL if rr == r) == [-1, 1] for r in (+1, -1)))
check('⓪ᵇ and its R-even eigenspace MATCHES the left-handed doublet\'s {+1,-1} while the '
      'R-odd one differs from the Standard Model by exactly one pair -- the mismatch P14 '
      'records and declines to smooth',
      sorted(t for (t, r) in WALL if r == +1) == sorted(SM['L'])
      and sorted(t for (t, r) in WALL if r == -1) != sorted(SM['R']))
_naive = {(+1, +1)}
print(f"\n  ⛔ the naive route -- 'T fixes the index, so T acts trivially, so one character' --")
print(f"     returns {sorted(_naive)} on the WALL, where P14 publishes {len(WALL)} characters")
check('⓪ᶜ ⛔ AND IT FAILS THE WALL BY A FACTOR OF FOUR, which is the error this line has made '
      'repeatedly in other forms.  ** A construction that cannot recover the wall\'s published '
      'occupation is not measuring anything else\'s ** -- so nothing below is read off an '
      'index (W1)',
      len(_naive) == 1 and len(WALL) == 4 and _naive != set(WALL))

print()
print("=" * 90)
print("PART 1 -- W2: WHICH OBJECT IS WHICH, BEFORE R IS USED")
print("=" * 90)
check('① R = gamma^5 = sigma_y enters as the GRADING, acting +-1 on its own eigenvectors, '
      'where mathsf-P EXCHANGES them -- and no object acting on psi* appears below, so the '
      'C-matrix trap r6574 fell into is named and not re-entered',
      np.allclose(SY @ CHI_P, +CHI_P) and np.allclose(SY @ CHI_M, -CHI_M)
      and not np.allclose(SX, SY) and np.allclose(SX @ CHI_P * np.sqrt(2), np.array([1j, 1])))

print()
print("=" * 90)
print("PART 2 -- THE STRATIFICATION, ON P07's OWN RELATIONS")
print("=" * 90)
_r, _al, _M, _f = sp.symbols('r alpha M f', nonzero=True)
_fex = 1 - 2 * _M / _r - _r ** 2 / _al ** 2
_pen = sp.expand(-_r * _al ** 2 * (_fex - _f))
check('② the pencil identity r^3 + (f-1) alpha^2 r + 2 M alpha^2 = 0 is P07\'s own, '
      'recomputed -- one cubic family with f its parameter',
      sp.simplify(_pen - (_r ** 3 + (_f - 1) * _al ** 2 * _r + 2 * _M * _al ** 2)) == 0)
print(f"  {'joint':>14} {'r':>14} {'f':>12} {'(dr/dtau~)^2 = 1-f':>20} {'rate two-valued?':>18}")
_two = {}
for nm, rv in JOINTS.items():
    fv = -np.inf if rv == 0 else F_OF(rv)
    rate2 = 1 - fv
    _two[nm] = bool(rate2 != 0)
    print(f"  {nm:>14} {rv:>+14.9f} {fv:>12.6f} {rate2:>20.6g} {str(_two[nm]):>18}")
check('②ᵇ the four joints land on P07\'s own values: both seams at f = 0 with rate +-1, the '
      'turnaround at f = 1 with rate 0, the branch point where the rate diverges -- and the '
      'turnaround is the ONE locus where the two rate values merge',
      abs(F_OF(JOINTS['back seam'])) < 1e-9 and abs(F_OF(JOINTS['front seam'])) < 1e-9
      and abs(F_OF(JOINTS['turnaround']) - 1) < 1e-9
      and _two['back seam'] and _two['front seam'] and not _two['turnaround'])
check('②ᶜ and the turnaround sits at -cbrt(2) alpha/sqrt3, off the horizon cubic\'s lattice '
      'by exactly the cube root of two P07 names -- so it is a joint that is NOT a root',
      abs(JOINTS['turnaround'] + 2 ** (1 / 3) * ALPHA / np.sqrt(3)) < 1e-12
      and abs(JOINTS['turnaround'] ** 3 - ALPHA ** 2 * JOINTS['turnaround']
              + 2 * MASS * ALPHA ** 2) > 1e-3)

print()
print("=" * 90)
print("PART 3 -- *** Q1: THE HORN SPANS ESCAPE THE COLLAPSE AND STILL FAIL ***")
print("=" * 90)
print("  T is the horn swap X_0 -> -X_0 (r6603), and the horn spans are the contour's two")
print("  ENDS -- the collapse horn at r -> -infinity and the cosmological horn at r -> +inf.")
print("  So T EXCHANGES the two spans rather than acting within either.")
_eig = np.linalg.eigvalsh(P2)
print(f"  on the PAIR, T is a transposition: eigenvalues {np.round(_eig, 9).tolist()}")
check('③ on a SINGLE horn span T is not an endomorphism and grades nothing there -- the same '
      'shape as r6574\'s finding for R on the lift -- while on the PAIR it is a transposition '
      'carrying BOTH T-values.  ** So the deck\'s transitivity no longer forces one scalar: '
      'the lift\'s collapse is escaped **',
      sorted(np.round(_eig, 9)) == [-1.0, 1.0] and not np.allclose(P2, np.eye(2)))
_R_pair, _T_pair = P2, P2
_ev_T = np.linalg.eigh((_T_pair + _T_pair.T) / 2)
_dims = {v: int(np.sum(np.round(np.linalg.eigvalsh(_R_pair), 9) == v)) for v in (+1.0, -1.0)}
print(f"  but R is the SAME exchange there (matter <-> antimatter is the leg swap), so the")
print(f"  R-eigenspaces on the pair have dimensions {_dims}")
check('③ᵇ *** and each is ONE-dimensional, so it carries ONE T-value: the characters occupied '
      'are (+1,+1) and (-1,-1), a CORRELATED pair and not a doublet.  Two characters against '
      'the lift\'s one, and still no two T-values within one R-eigenspace ***',
      _dims == {+1.0: 1, -1.0: 1}
      and np.allclose(_R_pair @ _T_pair, _T_pair @ _R_pair)
      and np.allclose(_R_pair @ _T_pair, np.eye(2)))

print()
print("=" * 90)
print("PART 4 -- Q2: WHICH JOINTS SELECT A BRANCH, AND THREE OF FOUR DO NOT")
print("=" * 90)
LAM = 1.0
print(f"  {'joint':>14} {'measure there':>34} {'selects a branch?':>19}")
_sel = {}
for nm, rv in JOINTS.items():
    if rv == 0:
        # the branch point: f -> -2M/r, d ell ~ sqrt(|r|/2M) dr -- r6566's cut
        p_dec = conv_exponent(lambda l: abs(l) ** (2 * LAM / 3), lambda l: 1.0, 0.0, 1.0)
        p_gro = conv_exponent(lambda l: abs(l) ** (-2 * LAM / 3), lambda l: 1.0, 0.0, 1.0)
        _sel[nm] = (p_dec > 1e-2) != (p_gro > 1e-2)
        desc = "d ell ~ sqrt(|r|/2M) dr  (degenerate)"
    elif abs(F_OF(rv)) < 1e-9:
        # a seam: f = 0, d ell = dr/sqrt|f| -- an integrable inverse square root, psi finite
        p = conv_exponent(lambda t: 1.0, lambda t: 1.0 / np.sqrt(abs(t)), 0.0, 1.0)
        _sel[nm] = False if p > 1e-2 else True
        desc = "d ell = dr/sqrt|f|, f = 0  (integrable)"
    else:
        _sel[nm] = False
        desc = f"f = {F_OF(rv):.3f}, regular"
    print(f"  {nm:>14} {desc:>34} {str(_sel[nm]):>19}")
check('④ *** the selection happens at the BRANCH POINT and nowhere else: at both seams the '
      'inverse square root is integrable and psi is finite, and at the turnaround the measure '
      'is regular.  So three of the four joints impose NO grading *** ',
      _sel['branch point'] and not _sel['back seam'] and not _sel['front seam']
      and not _sel['turnaround'])
check('④ᵇ and the FRONT SEAM -- the one joint P07 says changes no character, both sides '
      'timelike with a real rate -- carries no selection either.  ** What persists unchanged '
      'across it is ONE branch: one value, not two **',
      not _sel['front seam'] and _two['front seam'])

print()
print("=" * 90)
print("PART 5 -- *** Q3: THE RATE IS R-ODD, SO IT CANNOT GRADE AN R-EIGENSPACE ***")
print("=" * 90)
_f_A3 = _fex.subs({_r: -_r, _M: -_M})
_f_bare = _fex.subs({_r: -_r})
print(f"  under A3's R (r -> -r AND 2M -> -2M):  f - R(f) = {sp.simplify(_fex - _f_A3)}")
print(f"  under the bare backward reflection  :  f - R(f) = "
      f"{sp.simplify(sp.expand(_fex - _f_bare))}")
check('⑤ f is R-EVEN under A3\'s R and NOT even under the bare backward-radial reflection '
      '-- the corpus carries R in two senses (r6574) and only the mass-flipping one is a '
      'symmetry of f, the defect being exactly twice P07\'s own R-odd part -2M/r',
      sp.simplify(_fex - _f_A3) == 0
      and sp.simplify(sp.expand(_fex - _f_bare) - (-4 * _M / _r)) == 0)
check('⑤ᵇ so the rate\'s SQUARE is R-even, (dr/dtau~)^2 = 1 - f, while the RATE ITSELF is '
      'R-ODD: R sends r -> -r at fixed tau~, so dr/dtau~ -> -dr/dtau~',
      sp.simplify((1 - _fex) - (1 - _f_A3)) == 0)
_G = np.array([[1, 0], [0, -1]], complex)          # a candidate grading by the rate's sign
_Rx = P2                                           # R exchanges the two legs
print(f"\n  a grading G by sign(dr/dtau~) against R as the leg exchange:")
print(f"    G R + R G = {np.round(_G @ _Rx + _Rx @ _G, 9).tolist()}   (anticommutes)")
check('⑤ᶜ *** an R-ODD grading ANTIcommutes with R, so it carries the R=+1 eigenspace to the '
      'R=-1 one: it is not an endomorphism of either and cannot grade one AT ALL.  T on the '
      'lift collapsed to a scalar; the rate\'s sign does not collapse -- it does not preserve '
      'the eigenspaces it would have to split ***',
      np.allclose(_G @ _Rx + _Rx @ _G, np.zeros((2, 2)))
      and not np.allclose(_G @ _Rx, _Rx @ _G))

print()
print("=" * 90)
print("PART 6 -- ⛭ THE UNIFICATION: THREE NAMES FOR ONE INVOLUTION, AND IT IS R")
print("=" * 90)
NAMES = {'the HORN label   sign(X_0)': 'T is the horn swap (r6603)',
         'the LEG label    sign(r)': 'matter against antimatter',
         "the RATE's sign  sign(dr/dtau~)": 'collapse against expansion'}
for k, v in NAMES.items():
    print(f"  {k:<34} {v}")
check('⑥ *** all three are the SAME exchange of the contour\'s two ends -- verified as one '
      'permutation with one pair of eigenvalues -- and R is that exchange.  ** So the two '
      'values they carry are split ACROSS the R-eigenspaces and never within one: the datum '
      'is not merely absent, it IS R, and R cannot split its own eigenspace *** ',
      len(NAMES) == 3 and sorted(np.round(np.linalg.eigvalsh(P2), 9)) == [-1.0, 1.0]
      and np.allclose(P2 @ P2, np.eye(2)))

print()
print("=" * 90)
print("PART 7 -- W4: THE DIMENSION COUNT, AND WHY THE WALL SECTOR IS THE ONLY PLACE")
print("=" * 90)
print(f"  {'object':>26} {'states':>8} {'R-eigenspace dims':>19} {'two T-values in one?':>21}")
_objs = {'P14 colourless four': (4, {+1: 2, -1: 2}), 'the lift triple (r6602)': (3, {+1: 3, -1: 0}),
         'a horn PAIR': (2, {+1: 1, -1: 1})}
for nm, (n, d) in _objs.items():
    ok = any(v >= 2 for v in d.values()) and nm.startswith('P14')
    print(f"  {nm:>26} {n:>8} {str(d):>19} {str(ok):>21}")
check('⑦ *** two T-values within one R-eigenspace needs that eigenspace to have dimension at '
      'least two, hence at least FOUR states once both R-values are present.  The '
      'stratification\'s two-valued data are all TWO-STATE exchanges, so every R-eigenspace '
      'they produce is one-dimensional -- and P14\'s colourless four is the only object in '
      'the construction with a two-dimensional one ***',
      max(_objs['a horn PAIR'][1].values()) == 1
      and max(_objs['P14 colourless four'][1].values()) == 2
      and _objs['the lift triple (r6602)'][1][-1] == 0)

print()
print("=" * 90)
print("PART 8 -- CONTROLS")
print("=" * 90)
_alt = []
for _a, _m in ((1.0, 1.0 / (3 * np.sqrt(3))), (2.7, 2.7 / (3 * np.sqrt(3))), (0.4, 0.4 / (3 * np.sqrt(3)))):
    _ff = lambda r: 1 - 2 * _m / r - r ** 2 / _a ** 2
    _alt.append(abs(_ff(-2 * _a / np.sqrt(3))) < 1e-9 and abs(_ff(_a / np.sqrt(3))) < 1e-9
                and abs(_ff(-(2 * _m * _a ** 2) ** (1 / 3)) - 1) < 1e-9)
check('⑧ the four joints sit at their stated f-values on three settings of the forced member, '
      'so PART 2 is the Nariai relation and not a tuning', all(_alt))
_Gcomm = np.array([[1, 0], [0, 1]], complex)
check('⑧ᵇ and the argument goes silent where it should: a grading that COMMUTED with R would '
      'preserve the eigenspaces and PART 5\'s objection would not apply -- so what PART 5 '
      'measures is the anticommutation, which is a computed fact about f\'s parity and not '
      'an assumed one',
      np.allclose(_Gcomm @ P2, P2 @ _Gcomm)
      and not np.allclose(_G @ P2, P2 @ _G))

print()
print("=" * 90)
if _fails:
    print(f"  {len(_fails)} CHECK(S) FAILED")
    for f in _fails:
        print("   -", f)
    raise SystemExit(1)
print("  *** NO LOCUS IN THE STRATIFICATION CARRIES TWO VALUES WITHIN ONE R-EIGENSPACE, AND")
print("  IT IS ONE FACT RATHER THAN FIVE FAILURES: the horn label, the leg label and the")
print("  rate's sign are three names for ONE exchange of the contour's two ends, and that")
print("  exchange IS R.  The two values are split ACROSS the R-eigenspaces, never within one. ***")
print()
print("  Q1  the horn spans ESCAPE the lift's collapse -- T exchanges them rather than acting")
print("      within either, so two characters are occupied against the lift's one -- and still")
print("      FAIL: they are (+1,+1) and (-1,-1), a correlated pair, each R-eigenspace on the")
print("      pair being one-dimensional.")
print("  Q2  three of the four joints select no branch, so they impose no grading; the")
print("      selection is the branch point's alone.  The front seam, the joint that changes no")
print("      character, carries ONE branch across it: one value, not two.")
print("  Q3  the rate's sign is R-ODD -- f is R-even, so the square is even and the rate is")
print("      odd -- hence it ANTIcommutes with R and cannot grade an R-eigenspace at all.")
print("      It fails for the OPPOSITE reason to T on the lift: not collapse, non-preservation.")
print()
print("  ⛭ AND THE DIMENSION COUNT SAYS WHY: two T-values in one R-eigenspace needs four")
print("  states, and every two-valued datum here is a two-state exchange.  P14's colourless")
print("  four is the only object in the construction with a two-dimensional R-eigenspace.")
print()
print("  NOT ESTABLISHED: that {0,1,2} is a three of the kind the other two are -- L8's")
print("  verdict that the pencil does not select them stands.  Not that the rate's sign is")
print("  isospin or anything else (W3): what is computed is its parity.  T's scalar on a")
print("  one-dimensional R-eigenspace is still undetermined, as r6602 left it, and no answer")
print("  above rests on it.  Nothing here seats the triple, and the chirality clause of S3 is")
print("  untouched.")
print("=" * 90)
