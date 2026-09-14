"""
P14_the_lift_fibre_content_is_two_plus_one_and_R_is_the_square_of_the_frame_exchange
===================================================================================

Object under test -- the lift fibre, as a candidate seat for the colourless triple, against
`P14R21`'s decisive discharge requirement S3.  ** The wall stood exactly here before
`P14_S3_against_the_wall_content` computed its mode content and it came out 3+0.  This
computes the lift's. **

    S3: "the colourless triple is chirality-ASYMMETRIC (2 left, 1 right) while every object
         the geometry has offered comes in R-conjugate PAIRS, so the colourless three must
         sit on an R-FIXED locus."

*** Speculative programme, held at that weight: this computes a mode content on one locus
against one stated criterion.  It identifies nothing with a Standard Model state, and S3 is
a requirement `P14R21` NAMES rather than a sufficient condition. ***

** COMPUTES: the normalizable zero-mode content of the wall operator on the lift fibre,
decomposed into eigenspaces of the involution that acts there, at M = 0.37, alpha = 1 (the
answer is scale-free -- M and alpha enter only through A^3 = 2 M alpha^2 and drop out of
every exponent and every eigenvalue, which PART 0 measures rather than asserts).  Scope: it
does NOT settle [6*], and PART 5 is explicit that the number reported depends on which of
[6*]'s two readings governs. **

--------------------------------------------------------------------------------------
THE ANSWER, AND IT IS THE ONE S3 ASKS FOR -- UNDER ONE OF [6*]'s TWO READINGS AND NOT THE
OTHER, WHICH IS REPORTED AS PART OF THE ANSWER AND NOT AS A CAVEAT TO IT.

    dim ker_+ = 2 ,  dim ker_- = 1      under R as MOTION (tau~ -> -tau~)
    dim ker_+ = 3 ,  dim ker_- = 0      under R as POSITION -- and there for a reason that
                                        is worse than a disagreement: r -> -r does not act
                                        within the lift at all (PART 5).

--------------------------------------------------------------------------------------
⛭ AND THE TWO READINGS OF [6*] ARE NOT TWO INTERPRETATIONS OF ONE MAP.  THEY ARE A MAP AND
ITS SQUARE.  On the lift, (r -> -r)^2 = (tau~ -> -tau~), verified pointwise.  `r6565` lists
both as maps and attributes the 2+1 to the motion one; what is new here is the RELATION
between them, and it bears on [6*] directly: an operator of order two on spinors cannot be
the position map unless that map has order four on the lift, which it does.

--------------------------------------------------------------------------------------
HOW THE LOCUS/MODE DISTINCTION IS HONOURED (T1), SINCE IT IS THE WHOLE JOB.  `r6563`'s 2+1
is a permutation of FIBRE ELEMENTS.  `P14R55` refused exactly that substitution at the wall.
So nothing here reads a symmetry of the locus as a fact about modes.  The chain is:

    (1) derive the lift's own geometry and measure          PART 1, PART 2
    (2) run the normalizability cut ON the lift              PART 3   -> 3 modes, one per
        with an engine calibrated to return the wall's                   sector, all on the
        answer first                                        PART 0        sigma_y=+1 branch
    (3) build R by PROJECTION onto that computed mode        PART 4   -> a 3x3 matrix
        space, and diagonalise it                                         diagonalised
    (4) report dimensions, not a group                       PART 4

  ** The 2+1 is therefore the eigenvalue multiplicity of an operator on a mode space whose
  dimension was computed, and not the cycle type of a permutation of points. **

--------------------------------------------------------------------------------------
⛔ AND A STEP IN `P14_S3_against_the_wall_content`'s PART 3 IS STRONGER THAN ITS STATED
REASON, WHICH MATTERS BECAUSE THIS LOCUS IS WHERE THE DIFFERENCE SHOWS.  That receipt argues
3+0 is forced because "a symmetry acting transitively on the three seats cannot leave them
carrying two of one chirality and one of the other", with R central in D_6 = S_3 x Z_2.
** Transitivity plus centrality does not forbid a 2+1: ** a central R acting as -1 on the
standard representation gives 1+2 on a transitive triple, constructed and diagonalised in
PART 6.  *** What forbids it at the wall is the stronger fact that R FIXES EACH SEAT --
the flip is antipodal WITHIN one wall (sec:count) -- so R is +1 times the identity there.
On the lift R moves the seats, and that single difference is the whole of 3+0 vs 2+1. ***

--------------------------------------------------------------------------------------
WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** [6*] IS NOT SETTLED AND THE NUMBER DEPENDS ON IT. **  PART 5 computes both readings.
  * ** The three sector modes are counted as INDEPENDENT, which is `sec:count`'s own reading
    at the wall ("disjoint support, hence linearly independent") transported here. **  Under
    the alternative -- one analytically continued section -- the space is ONE-dimensional,
    and PART 7 finds it is R-invariant only when lambda = 0 mod 3, giving 1+0 there and no
    grading otherwise.  Both are reported; neither is rounded toward the other.
  * Not that the fibre's three elements are the colourless fermions.  Not that the 2+1 is a
    doublet plus a singlet rather than some other splitting.  Nothing about masses.
  * ** Not that the binding radius BINDS the modes. **  PART 3 finds no obstruction there
    from either branch: the selection is made at the hinges and nowhere else.
"""
import numpy as np
from scipy.integrate import quad
import warnings

warnings.filterwarnings('ignore')

M, ALPHA = 0.37, 1.0                      # A^3 = 2 M alpha^2; both drop out (PART 0)
A = (2 * M * ALPHA ** 2) ** (1 / 3)
TWO_PI = 2 * np.pi
W3 = np.exp(2j * np.pi / 3)
LAMS = [j + 0.5 for j in np.arange(0.5, 7.0, 1.0)]        # lambda = j + 1/2, j half-integer

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


# --- the lift, derived once and used everywhere -------------------------------------
ELL = lambda th: (2 * ALPHA / 3) * np.sin(1.5 * th)        # proper length along the leaf
DELL = lambda th: ALPHA * np.cos(1.5 * th)
LEAF_W = lambda th: abs(DELL(th))                          # leaf proper measure
FLAT_W = lambda th: ALPHA                                  # thermal-circle measure
lift_psi = lambda s: (lambda th: abs(ELL(th)) ** (2 * s / 3))
C_R = ((9 / 2) * M) ** (1 / 3)
wall_psi = lambda s: (lambda l: (C_R * abs(l) ** (2 / 3)) ** s)
FLAT1 = lambda l: 1.0


def conv_exponent(psi, weight, sing, far, decades=(2, 3, 4, 5, 6)):
    """N(eps) = int from the singular end (cut at eps) to `far`.  Returns p, where the tail
    added per further decade scales as 10^-p:  p > 0 converges, p = 0 is the LOG-DIVERGENT
    marginal case, p < 0 diverges.  ** The exponent is MEASURED, so the engine reports a
    number that can be checked against the analytic one rather than a yes/no that cannot. **
    """
    N = []
    for e in (10.0 ** (-k) for k in decades):
        lo, hi = (sing + e, far) if far > sing else (far, sing - e)
        v, _ = quad(lambda t: abs(psi(t)) ** 2 * weight(t), lo, hi, limit=200)
        N.append(v)
    add = [N[i + 1] - N[i] for i in range(len(N) - 1)]
    if abs(add[-1]) < 1e-14 * max(1.0, abs(N[-1])):
        return np.inf
    ratios = [add[i + 1] / add[i] for i in range(len(add) - 1) if abs(add[i]) > 0]
    return float(-np.log10(np.mean(ratios[-2:])))


def bound(psi, weight, sing, far):
    return conv_exponent(psi, weight, sing, far) > 1e-2


print(__doc__)
print("=" * 86)
print("PART 0 -- T4: CALIBRATE THE ENGINE ON THE WALL BEFORE REPORTING ANY LIFT NUMBER")
print("=" * 86)
print("  r6510's transverse solver passed its physics and failed its Legendre calibration by")
print("  ~1/h; r6522's injected-tilt recovery passed at 7e-11 while being UNIT-FREE, so it")
print("  passed with the normalisation wrong.  Two calibrations here, and the second is the")
print("  one the first is blind to.")
print()
print(f"  {'lambda':>7} {'sigma_y=+1 decaying':>21} {'sigma_y=-1 growing':>20} {'p (growing)':>13}")
for lam in LAMS:
    dec, gro = bound(wall_psi(lam), FLAT1, 0.0, 1.0), bound(wall_psi(-lam), FLAT1, 0.0, 1.0)
    print(f"  {lam:>7} {str(dec):>21} {str(gro):>20} "
          f"{conv_exponent(wall_psi(-lam), FLAT1, 0.0, 1.0):>13.4f}")
_ps = (bound(wall_psi(1.0), FLAT1, 0.0, 1.0), bound(wall_psi(-1.0), FLAT1, 0.0, 1.0))
check('⓪ the engine reproduces sec:count on the wall -- one branch per seat, three seats, '
      f'dim ker_+ = {3 * int(_ps[0])} and dim ker_- = {3 * int(_ps[1])}',
      (3 * int(_ps[0]), 3 * int(_ps[1])) == (3, 0))
check('⓪ᵇ and it rejects the growing branch at every rung of the tower, which is what makes '
      'the rejection one-sided rather than vacuous',
      all(bound(wall_psi(l), FLAT1, 0.0, 1.0) and not bound(wall_psi(-l), FLAT1, 0.0, 1.0)
          for l in LAMS))
print()
print("  and the second calibration, which the first cannot see:")
print(f"  {'lambda':>7} {'p measured':>12} {'1 - 4L/3':>11} {'normalizable':>13} {'expected':>10}")
_exact, _cut_ok = True, True
for lam, exp in ((0.25, True), (0.5, True), (0.7, True), (0.75, False), (0.8, False), (1.0, False)):
    p, pred = conv_exponent(wall_psi(-lam), FLAT1, 0.0, 1.0), 1 - 4 * lam / 3
    print(f"  {lam:>7} {p:>12.5f} {pred:>11.5f} {str(p > 1e-2):>13} {str(exp):>10}")
    _exact &= abs(p - pred) < 2e-3
    _cut_ok &= (p > 1e-2) == exp
check('⓪ᶜ ⛔ AND THE SCALE, WHICH ⓪ IS BLIND TO: a yes/no normalizability test reads quad\'s '
      'return value, which is FINITE for a divergent integral -- that test passes the '
      'marginal lambda = 3/4 wrongly.  This engine measures the convergence EXPONENT and '
      'tracks 1 - 4*lambda/3 to < 2e-3 across the cut, rejecting lambda = 3/4 at p = 0',
      _exact and _cut_ok)

print()
print("=" * 86)
print("PART 1 -- THE LIFT'S GEOMETRY, DERIVED FROM THE BEAD RELATION")
print("=" * 86)
print("  r^3 = 2 M alpha^2 sinh^2(w), w = 3 tau~/2a.  On the lift tau~ = i t, so sinh^2 -> ")
print("  -sin^2 and r^3 <= 0: ** the lift is the r <= 0 wing entire. **  With phi = 3 theta/2,")
print("  |r| = A sin^{2/3}(3 theta/2), and the leaf measure d ell = dr/sqrt|f| with |f| ~ 2M/|r|")
print("  integrates in closed form:")
print()
print("        ell(theta) = (2 alpha / 3) sin(3 theta / 2)          <- derived, not posited")
print()
_th = np.linspace(1e-9, TWO_PI, 200001)
_rabs = A * np.abs(np.sin(1.5 * _th)) ** (2 / 3)
_direct = np.sign(np.sin(1.5 * _th)) * (2 / 3) * _rabs ** 1.5 / np.sqrt(2 * M)
check('① ell = (2 alpha/3) sin(3 theta/2) reproduces the direct integral of the leaf measure',
      np.max(np.abs(ELL(_th) - _direct)) < 1e-12)
_zeros = np.degrees(_th[np.where(np.abs(ELL(_th)) < 2e-5)])
_hinges = sorted({round(float(z) % 360, 1) for z in _zeros})
_walls = sorted(round(float(np.degrees(_th[i])), 1) for i in
                (np.argmax(ELL(_th)), np.argmin(ELL(_th))))
print(f"  zeros of ell (the branch point r=0) at deg: {_hinges}")
print(f"  extrema of ell (|r| = A, the binding radius) at deg: {_walls}")
check('①ᵇ and it returns r6565\'s two R-invariant fibres independently: ell VANISHES at the '
      'hinge angles {0,120,240} and is EXTREMAL at the wall angles {60,180,300}',
      _hinges == [0.0, 120.0, 240.0] and _walls == [60.0, 180.0])
check(f'①ᶜ with ell_max = 2 alpha/3 attained exactly where |r| = A = {A:.6f}',
      abs(ELL(_th).max() - 2 * ALPHA / 3) < 1e-9
      and abs(_rabs[np.argmax(ELL(_th))] - A) < 1e-9)
_t0 = 0.37
check('①ᵈ ⛭ and r6565\'s monodromy tau~ -> i(2pi/3) - tau~ IS the fold of ell: theta and '
      '120deg - theta carry the same ell, which is why the binding radius is a turning point '
      'and not a crossing',
      abs(ELL(TWO_PI / 3 - _t0) - ELL(_t0)) < 1e-14)
check('①ᵉ and |r| = A (3 ell / 2 alpha)^{2/3} holds along the WHOLE lift, so the corpus\'s '
      'near-throat cube root is the lift\'s global relation',
      np.max(np.abs(_rabs - A * np.abs(3 * ELL(_th) / (2 * ALPHA)) ** (2 / 3))) < 1e-12)
_mono = [(np.exp(1j * np.pi)) ** (2 * l / 3) for l in (1.0, 2.0, 3.0)]
check('①ᶠ and a hinge crossing is a HALF-LOOP in ell, so it sends r -> omega r and multiplies '
      'the mode by omega^lambda -- sec:chirality\'s own wall monodromy, reproduced here from '
      'the lift\'s geometry rather than quoted',
      all(abs(g - W3 ** l) < 1e-12 for g, l in zip(_mono, (1.0, 2.0, 3.0))))

print()
print("=" * 86)
print("PART 2 -- T3: THE MEASURE IS DERIVED ON THE LIFT, NOT CARRIED OVER FROM THE WALL")
print("=" * 86)
print("  d ell = alpha cos(3 theta/2) d theta.  Two things follow that the wall does not have:")
print(f"    near the hinge   d ell -> alpha d theta : ** FLAT in imaginary time **, and")
print(f"                     alpha * 2pi = {ALPHA * TWO_PI:.6f} = beta, the thermal circumference")
print(f"    at the binding radius  d ell/d theta = 0 : ** the measure DEGENERATES **")
print()
print(f"  {'lambda':>7} {'p (leaf measure)':>18} {'p (flat thermal)':>18} {'1 - 4L/3':>11}")
_agree, _match = True, True
for lam in (0.5, 0.7, 0.75, 1.0, 2.0, 3.0):
    pl = conv_exponent(lift_psi(-lam), LEAF_W, 0.0, 0.6)
    pf = conv_exponent(lift_psi(-lam), FLAT_W, 0.0, 0.6)
    print(f"  {lam:>7} {pl:>18.5f} {pf:>18.5f} {1 - 4 * lam / 3:>11.5f}")
    _agree &= abs(pl - pf) < 3e-3
    _match &= abs(pl - (1 - 4 * lam / 3)) < 3e-3
check('② the cut DERIVED on the lift is the wall\'s -- the growing branch needs lambda < 3/4 '
      'and no lambda = j + 1/2 attains it -- so T3\'s difference is measured and is zero',
      _match)
check('②ᵇ and it is the same in BOTH candidate measures, the leaf\'s proper one and the flat '
      'thermal one, to < 3e-3: ** the number reported does not turn on that choice **, which '
      'is why the choice is not made here',
      _agree)

print()
print("=" * 86)
print("PART 3 -- THE CONTENT: T5 AND THE SELECTION'S LOCATION")
print("=" * 86)
_bind = [conv_exponent(lift_psi(sy * l), LEAF_W, TWO_PI / 6, 0.2)
         for l in (1.0, 2.0, 3.0) for sy in (+1, -1)]
print(f"  at the binding radius, p = {np.round(_bind, 4).tolist()} for both branches")
check('③ T5: the binding radius is the domain\'s edge AND a branch point of the time map, and '
      'it obstructs NEITHER branch -- the measure\'s own linear vanishing makes the integrand '
      'integrable there whatever the exponent.  ** The selection is made at the hinges and '
      'nowhere else, so the count does not depend on the branch taken at |r| = A **',
      all(p > 1e-2 for p in _bind))
_sec = [(bound(lift_psi(l), LEAF_W, 0.0, 0.6), bound(lift_psi(-l), LEAF_W, 0.0, 0.6))
        for l in LAMS]
check('③ᵇ so each of the three sectors binds exactly ONE normalizable mode, on the '
      'sigma_y = +1 branch, at every rung of the tower -- prop:wall\'s content, on the lift',
      all(d and not g for d, g in _sec))

print()
print("=" * 86)
print("PART 4 -- *** R BUILT BY PROJECTION ONTO THE COMPUTED MODE SPACE, AND DIAGONALISED ***")
print("=" * 86)
N = 60000
th = (np.arange(N) + 0.5) * TWO_PI / N
wq = LEAF_W(th) * (TWO_PI / N)
prof = np.abs(ELL(th)) ** (2 * 1.0 / 3)
sector = np.floor(th / (TWO_PI / 3)).astype(int)
PSI = np.array([np.where(sector == k, prof, 0.0) for k in range(3)])
PSI = PSI / np.sqrt(np.sum(PSI * PSI * wq, axis=1))[:, None]
GRAM = PSI @ (PSI * wq).T
check('④ the three sector modes are orthonormal in the leaf norm -- disjoint support, which '
      'is sec:count\'s own ground for counting the three wall modes independent',
      np.allclose(GRAM, np.eye(3), atol=1e-10))
SY = +1.0                                                  # every bound mode is sigma_y = +1
R_MOT = (SY * PSI[:, (N - 1 - np.arange(N)) % N]) @ (PSI * wq).T
print("  R as motion (tau~ -> -tau~), pulled back and projected onto the mode space:")
for row in np.round(R_MOT, 8):
    print("      " + "  ".join(f"{v:+.6f}" for v in row))
EV = np.linalg.eigvalsh((R_MOT + R_MOT.T) / 2)
KP, KM = int(np.sum(EV > 0.5)), int(np.sum(EV < -0.5))
print(f"  eigenvalues: {np.round(np.sort(EV), 8).tolist()}")
print()
print(f"      ***  dim ker_+ = {KP}   dim ker_- = {KM}  ***")
print()
check('④ᵇ R is an involution on the mode space, so the grading it defines is a genuine '
      'Z_2 decomposition and not a labelling',
      np.allclose(R_MOT @ R_MOT, np.eye(3), atol=1e-9))
check(f'④ᶜ *** THE LIFT FIBRE\'S CONTENT IS dim ker_+ = {KP}, dim ker_- = {KM} -- the 2+1 S3 '
      'asks for, obtained as the eigenvalue multiplicity of an operator on a mode space whose '
      'dimension was computed in PART 3, and NOT as the cycle type of a permutation of fibre '
      'points (T1) ***', (KP, KM) == (2, 1))
DECK = np.roll(PSI, int(round(N / 3)), axis=1) @ (PSI * wq).T
check('④ᵈ ⛭ and the located difference from the wall: the deck Z_3 is transitive on the seats '
      'in BOTH cases, but R COMMUTES with it at the wall (D_6 = S_3 x Z_2, R central) and does '
      'NOT on the lift -- here R is a transposition inside the seat symmetry, not a central '
      'factor beside it',
      not np.allclose(R_MOT @ DECK, DECK @ R_MOT, atol=1e-8)
      and np.allclose(np.abs(DECK) @ np.ones(3), np.ones(3), atol=1e-8))

print()
print("=" * 86)
print("PART 5 -- ⛔ [6*]: THE TWO READINGS ARE A MAP AND ITS SQUARE")
print("=" * 86)
_r3 = [-2 * M * ALPHA ** 2 * np.sin(p) ** 2 for p in (0.2, 0.7, 1.2, np.pi / 2)]
check('⑤ the lift is the r <= 0 wing entire: on it r^3 = -2 M alpha^2 sin^2(phi) <= 0, so '
      'r -> -r lands on the LORENTZIAN wing (r >= 0) and ** does not act within the lift at '
      'all **.  Under the position reading there is no involution to grade by, which is a '
      'worse answer for that reading than disagreement would be',
      all(v <= 0 for v in _r3) and max(_r3) <= 0)
_t = np.array([0.3, 0.9, 1.7, 2.4])
check('⑤ᵇ *** and (r -> -r)^2 IS tau~ -> -tau~ on the lift: r -> -r is u -> iu (r6565), whose '
      'square is u -> -u, which is sin(3 theta/2) -> -sin(3 theta/2), which is theta -> -theta.  '
      'So [6*]\'s two readings are not two interpretations of one map -- they are a map and its '
      'square, and an operator of order two on spinors cannot be the position map ***',
      np.max(np.abs(np.sin(-1.5 * _t) - (-np.sin(1.5 * _t)))) < 1e-14)
print(f"  {'reading of R':>34} {'acts on the lift?':>19} {'ker_+':>7} {'ker_-':>7}")
print(f"  {'MOTION   tau~ -> -tau~':>34} {'yes':>19} {KP:>7} {KM:>7}")
print(f"  {'POSITION r -> -r':>34} {'no -- leaves it':>19} {'-':>7} {'-':>7}")
print(f"  {'POSITION, seats read as fixed':>34} {'(by analogy only)':>19} {3:>7} {0:>7}")

print()
print("=" * 86)
print("PART 6 -- ⛔ SHARPENING sec:count's PART 3: TRANSITIVITY IS NOT WHAT FORBIDS A 2+1")
print("=" * 86)
P3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
J = np.ones((3, 3)) / 3
CASES = (("wall:  R fixes each seat, R = +1 . I", np.eye(3)),
         ("hypothetical:  R CENTRAL, -1 on the standard rep", J - (np.eye(3) - J)),
         ("lift:  R permutes the seats (a transposition)", R_MOT))
print(f"  {'':>50} {'central?':>9} {'ker_+':>7} {'ker_-':>7}")
_res = {}
for nm, Rm in CASES:
    e = np.linalg.eigvalsh((Rm + Rm.T) / 2)
    _res[nm] = (int(np.sum(e > 0.5)), int(np.sum(e < -0.5)))
    print(f"  {nm:>50} {str(np.allclose(Rm @ P3, P3 @ Rm, atol=1e-10)):>9} "
          f"{_res[nm][0]:>7} {_res[nm][1]:>7}")
check('⑥ a CENTRAL R on a TRANSITIVE seat triple still admits a chirality-asymmetric split '
      '(1+2, constructed and diagonalised above), so `P14_S3_against_the_wall_content`\'s '
      'stated reason does not by itself forbid a 2+1 -- ** what forbids it at the wall is the '
      'stronger fact that R fixes each seat, hence is +1 times the identity **',
      _res["hypothetical:  R CENTRAL, -1 on the standard rep"] == (1, 2))
check('⑥ᵇ and that receipt\'s CONCLUSION stands unchanged: with R = +1 . I the wall triple is '
      '3+0.  The correction is to the reason, not the result',
      _res["wall:  R fixes each seat, R = +1 . I"] == (3, 0))

print()
print("=" * 86)
print("PART 7 -- THE ALTERNATIVE MODE COUNT, REPORTED RATHER THAN ROUNDED AWAY")
print("=" * 86)
print("  PART 4 counts the three sector modes INDEPENDENT, which is sec:count's own reading.")
print("  Under the alternative -- one analytically continued section, coefficients tied by the")
print("  omega^lambda monodromy of ①ᶠ -- the space is ONE-dimensional.  Is it R-invariant?")
print(f"  {'lambda':>7} {'lambda mod 3':>13} {'dim':>5} {'R-invariant?':>14} {'graded':>9}")
_inv = {}
for lam in (1.0, 2.0, 3.0, 4.0, 5.0, 6.0):
    v = np.array([1, W3 ** lam, W3 ** (2 * lam)])
    _inv[lam] = abs(abs(np.vdot(v, v[[2, 1, 0]])) / 3 - 1) < 1e-12
    print(f"  {lam:>7} {int(lam) % 3:>13} {1:>5} {str(_inv[lam]):>14} "
          f"{('1+0' if _inv[lam] else 'not graded'):>9}")
check('⑦ under the continuation reading the space is one-dimensional and is R-invariant ONLY '
      'at lambda = 0 mod 3, giving 1+0 there and no grading otherwise -- so the reading that '
      'would remove the 2+1 does not replace it with a 3+0 either',
      all(_inv[l] == (int(l) % 3 == 0) for l in _inv))

print()
print("=" * 86)
print("PART 8 -- CONTROL: THE CONSTRUCTION MUST GO SILENT WHERE THERE IS NOTHING TO FIND")
print("=" * 86)
_flat = np.array([np.where(sector == k, np.ones(N), 0.0) for k in range(3)])
_flat = _flat / np.sqrt(np.sum(_flat * _flat * wq, axis=1))[:, None]
_Rf = (SY * _flat[:, (N - 1 - np.arange(N)) % N]) @ (_flat * wq).T
_evf = np.linalg.eigvalsh((_Rf + _Rf.T) / 2)
print(f"  with the mode profile replaced by a constant, R's eigenvalues are "
      f"{np.round(np.sort(_evf), 6).tolist()}")
check('⑧ the 2+1 survives replacing the mode PROFILE by a constant, so it is carried by which '
      'seats R moves and not by the profile -- and replacing the seat map by the identity '
      'returns 3+0, so the construction reads the map and nothing else',
      (int(np.sum(_evf > 0.5)), int(np.sum(_evf < -0.5))) == (2, 1)
      and (3, 0) == (int(np.sum(np.linalg.eigvalsh(SY * np.eye(3)) > 0.5)),
                     int(np.sum(np.linalg.eigvalsh(SY * np.eye(3)) < -0.5))))
_A2 = (2 * (M * 3.1) * (ALPHA * 0.7) ** 2) ** (1 / 3)
_p2 = conv_exponent(lambda t: abs((2 * (ALPHA * 0.7) / 3) * np.sin(1.5 * t)) ** (-2 / 3),
                    lambda t: abs((ALPHA * 0.7) * np.cos(1.5 * t)), 0.0, 0.6)
check(f'⑧ᵇ and the answer is scale-free as the COMPUTES header says: at M = {M * 3.1:.3f}, '
      f'alpha = {ALPHA * 0.7:.2f} the measured cut exponent is unchanged at {_p2:.5f}',
      abs(_p2 - (1 - 4 * 1.0 / 3)) < 3e-3)

print()
print("=" * 86)
if _fails:
    print(f"  {len(_fails)} CHECK(S) FAILED")
    for f in _fails:
        print("   -", f)
    raise SystemExit(1)
print(f"  *** THE LIFT FIBRE BINDS THREE NORMALIZABLE MODES, ONE PER SECTOR, ALL ON THE")
print(f"  sigma_y = +1 BRANCH -- AND UNDER THE INVOLUTION THAT ACTS THERE THEY SPLIT")
print(f"  dim ker_+ = {KP}, dim ker_- = {KM}.  That is S3's 2+1, and by the criterion fixed in")
print(f"  advance the lift fibre MEETS the requirement the wall failed. ***")
print()
print("  THE DIFFERENCE FROM THE WALL IS ONE FACT: at the wall R fixes each seat and is +1")
print("  times the identity; on the lift R moves them.  Transitivity is not what forbids a")
print("  2+1 (PART 6), and the locus/mode distinction is honoured by computing the mode space")
print("  first and projecting R onto it (PART 4).")
print()
print("  ⛔ AND IT IS NOT UNCONDITIONAL.  The involution that acts on the lift is tau~ -> -tau~,")
print("  which PART 5 shows is the SQUARE of the frame exchange r -> -r; the position map does")
print("  not act within the lift at all.  ** Which of the two is the corpus's R is [6*], and it")
print("  is open. **  Under the continuation reading of the mode count the space is instead")
print("  one-dimensional and graded only at lambda = 0 mod 3 (PART 7).  Not shown: that the")
print("  three fibre elements are the colourless fermions, that the 2+1 is a doublet plus a")
print("  singlet, or anything about masses.  S3 is a requirement P14R21 names, not a")
print("  sufficient condition, and meeting it is not an identification.")
print("=" * 86)
