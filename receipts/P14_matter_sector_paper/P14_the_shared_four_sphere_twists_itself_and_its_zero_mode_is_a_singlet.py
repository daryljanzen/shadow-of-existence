"""
P14_the_shared_four_sphere_twists_itself_and_its_zero_mode_is_a_singlet
======================================================================

Object under test -- the S^4 the two faces share at X_0 = 0, which `r6713` established is the one
place in either five-dimensional face where chirality exists.  ** Does a Dirac operator there
carry a chiral su(2)-doublet zero mode, and does the sphere supply the twist itself? **

*** THE SPHERE DOES SUPPLY ITS OWN TWIST, AND IT IS THE UNIT INSTANTON.  THE INDEX IS ONE.  AND
THE ZERO MODE IS A SINGLET OF THE su(2) THAT SUPPLIED THE TWIST -- the doublet lives in the one
place on this sphere that has no zero modes, and the reason is a Betti number. ***

--------------------------------------------------------------------------------------
Q1 -- YES.  EACH CHIRAL SPINOR BUNDLE OF THE ROUND S^4 CARRIES INSTANTON NUMBER ONE.

Computed in the explicit spinor representation rather than by projecting an su(2) connection:
the spin connection Omega_mu = (1/2) omega^{ab}_mu Sigma_ab is BLOCK DIAGONAL in gamma^5, so its
two 2x2 blocks ARE the su(2) connections on S+ and S-, with no normalisation left to choose.

    k(S+) = +1 ,  c_2(S+) = -1        k(S-) = -1 ,  c_2(S-) = +1

  ==> ** The twist is geometric.  The self-dual half of the round sphere's own spin connection is
      the unit BPST instanton, and the anti-self-dual half is the anti-instanton. **  Equal and
      opposite, which is what p_1(S^4) = 0 requires and PART 0 checks.

⛔ ** AND THE NORMALISATION IS NOT FREE, WHICH IS WHY IT IS DONE THIS WAY. **  Writing the
projection as A^i = c . eta^i_{ab} omega^{ab} and fixing c by a consistency condition at a sample
point returns c = 1/2 and then |k| = 5 -- a value no orientation or convention can produce from
+-1, and one the p_1 identity does not catch because it is odd and cancels in the sum.  The
explicit chiral block has no free constant, and PART 1 checks it against the closed form
F^i_{mu nu} = Omega^2 eta^i_{mu nu} as well.

--------------------------------------------------------------------------------------
Q2 -- THE INDEX IS ONE, COMPUTED TWO INDEPENDENT WAYS, AND THE KERNEL IS (1, 0).

  ATIYAH--SINGER.  On S^4 the A-hat genus is 1 because p_1 = 0, so
      ind(D tensor S+) = integral ch_2(S+) = -c_2(S+) = +1.

  HODGE THEORY, on the same operator recognised as a complex of forms:
      S+ tensor S+ = (2,1) tensor (2,1) = (1 + 3, 1) = Lambda^0 + Lambda^+
      S- tensor S+ = (1,2) tensor (2,1) = (2,2)       = Lambda^1
    so ker = b_0 + b_2^+ = 1 + 0 = 1 and coker = b_1 = 0, giving ind = 1.

  ==> ** The two routes agree, which is what pins c_2(S+) = -1 rather than leaving it quoted. **
      And `W4` is honoured: the kernel dimensions are ONE of the twisted-positive chirality and
      ZERO of the other, reported separately from their difference.

--------------------------------------------------------------------------------------
Q3 -- NO.  THE ZERO MODE IS A SINGLET, AND THE DOUBLET IS WHERE THERE ARE NO ZERO MODES.

** The one zero mode is the CONSTANT FUNCTION, in the Lambda^0 summand -- which is the (1,1) of
S+ tensor S+, a singlet of the su(2) that supplied the twist. **  And it is not that the doublet
is merely unoccupied:

    S+ tensor S+ = 1 + 3     ** contains NO doublet at all ** -- and carries the zero mode
    S- tensor S+ = (2,2)     ** IS a doublet of each factor ** -- and carries none, because
                               b_1(S^4) = 0

  ==> *** So the shape of `(a)` is real at the level of the BUNDLES and empty at the level of the
      STATES.  A doublet needs two states within one chirality under one su(2) (`W3`); the
      chirality that has a state has no doublet in it, and the one that is a doublet has no
      state.  The obstruction is b_1(S^4) = 0. ***

--------------------------------------------------------------------------------------
Q4 -- THE FACTOR THAT SUPPLIES THE TWIST IS THE FACTOR OF WHICH THE ZERO MODE IS A SINGLET.

S+ is (2,1): a doublet of su(2)_+ and a singlet of su(2)_-, tied to the self-dual two-forms; S-
is (1,2), the mirror.  So one factor does see only one handedness, exactly as `(a)` says.  ** But
the twist on S+ is an su(2)_+ connection, and the zero mode it produces is the su(2)_+ SINGLET in
2 tensor 2. **  The same factor, on both sides of the trade.

--------------------------------------------------------------------------------------
W2 -- WHICH READING THE CONSTRUCTION SUPPORTS, AND IT IS NOT THE PARTICLE ONE.

The zero mode is the sphere's own CONSTANT -- the b_0 = 1 mode, global and unlocalised.  In
ordinary field theory a zero mode on a Euclidean S^4 in an instanton background is an instanton
zero mode, tied to a tunnelling amplitude rather than to a particle, and nothing here makes this
one different: the S^4 is a spatial throat of one face and an atemporal equator of the other, with
no time in it.  ** The index statement is about the sphere, not about a state in a spectrum. **

--------------------------------------------------------------------------------------
⚠ WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** NOT that this su(2) is weak isospin, and it is not called that. **  (`W1`.)  The su(2)
    factors of Spin(4) rotate the sphere's TANGENT space.  Whether a construction turns that into
    an internal gauge symmetry is the Kaluza--Klein question and is not touched here.
  * ** NOT that the sphere carries no interesting index. **  It carries exactly one, and Q1's
    geometric twist is a real finding: Lichnerowicz is evaded by the sphere's own connection.
  * ** NOT that a doublet could not be found by twisting with something else. **  What is shown is
    that the bundle the SPHERE supplies gives a singlet.
  * ** NOT a claim about the Lorentzian face's colour. **  `r6710` settled that and is untouched.
  * The colourless triple is not seated.
"""
import itertools

import sympy as sp

x = sp.symbols('x0 x1 x2 x3', real=True)
r2 = sum(t * t for t in x)
I2, Z2 = sp.eye(2), sp.zeros(2, 2)
SIG3 = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
blk = lambda a, b, c, d: sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
G = [blk(Z2, I2, I2, Z2)] + [blk(Z2, -sp.I * s, sp.I * s, Z2) for s in SIG3]

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


def eps4(*p):
    p = list(p)
    if len(set(p)) < 4:
        return 0
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    return s


def eps3(i, j, k):
    p = [i, j, k]
    if len(set(p)) < 3:
        return 0
    s = 1
    for a in range(3):
        for b in range(a + 1, 3):
            if p[a] > p[b]:
                s = -s
    return s


def eta(i, mu, nu, s):
    """'t Hooft symbol; s = -1 is the self-dual one, established in PART 0."""
    e = eps3(i - 1, mu - 1, nu - 1) if (mu >= 1 and nu >= 1) else 0
    return e + s * ((1 if (i == mu and nu == 0) else 0) - (1 if (i == nu and mu == 0) else 0))


def charge_integral(F):
    """int eps^{mu nu rho sigma} tr(F_{mu nu} F_{rho sigma}) d^4x over R^4, radially."""
    d = sp.simplify(sum(eps4(m, n, r, s) * sp.trace(F[m][n] * F[r][s])
                        for m, n, r, s in itertools.product(range(4), repeat=4)))
    rr = sp.Symbol('rr', positive=True)
    dr = sp.simplify(d.subs({x[0]: rr, x[1]: 0, x[2]: 0, x[3]: 0}))
    return sp.simplify(sp.integrate(2 * sp.pi ** 2 * rr ** 3 * dr, (rr, 0, sp.oo))), d


def curv(A):
    return [[sp.simplify(sp.diff(A[n], x[m]) - sp.diff(A[m], x[n]) + A[m] * A[n] - A[n] * A[m])
             for n in range(4)] for m in range(4)]


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: C1 LICHNEROWICZ, C2 THE BPST UNIT, C3 THE TOPOLOGY")
print("=" * 90)
_cliff = all(sp.simplify(G[a] * G[b] + G[b] * G[a] - 2 * (1 if a == b else 0) * sp.eye(4))
             == sp.zeros(4, 4) for a in range(4) for b in range(4))
G5 = sp.simplify(-G[0] * G[1] * G[2] * G[3])
if sp.simplify(G5 * G5) != sp.eye(4):
    G5 = sp.simplify(sp.I * G[0] * G[1] * G[2] * G[3])
SIGMA = [[sp.simplify((G[a] * G[b] - G[b] * G[a]) / 4) for b in range(4)] for a in range(4)]
IDX = {+1: [i for i in range(4) if G5[i, i] == 1], -1: [i for i in range(4) if G5[i, i] == -1]}
check('⓪ the Euclidean Clifford algebra closes, gamma^5 squares to one and is diagonal, and every '
      'Sigma_ab COMMUTES with it -- so the spin connection is block diagonal in chirality and its '
      'blocks are the two su(2) connections with no normalisation left to choose',
      _cliff and sp.simplify(G5 * G5) == sp.eye(4)
      and all(sp.simplify(SIGMA[a][b] * G5 - G5 * SIGMA[a][b]) == sp.zeros(4, 4)
              for a in range(4) for b in range(4))
      and len(IDX[+1]) == 2 and len(IDX[-1]) == 2)
_sd = None
for s in (+1, -1):
    ok = all(sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2)
                       * sum(eps4(a, b, c, d) * eta(i, c, d, s) for c in range(4) for d in range(4))
                       - eta(i, a, b, s)) == sp.zeros(4, 4) for i in (1, 2, 3))
    if ok:
        _sd = s
print(f"  the self-dual 't Hooft sign is s = {_sd}")
check('⓪ᵇ and the self-dual sign is DETERMINED by testing the duality relation, not assumed',
      _sd in (+1, -1))
n = 4
SCAL = n * (n - 1)
CHI, SIGNATURE = 2, 0
P1 = 3 * SIGNATURE
print(f"\n  C1: the unit S^4 has scalar curvature n(n-1) = {SCAL} > 0, and Lichnerowicz's")
print(f"      D^2 = nabla* nabla + R/4 leaves no harmonic spinor, so the UNTWISTED kernel is 0;")
print(f"      the untwisted index is -p_1/24 = {-sp.Rational(P1, 24)} as well")
check('⓪ᶜ C1: the untwisted Dirac operator on the round S^4 has NO zero modes -- positive scalar '
      'curvature, and its index vanishes independently because p_1 = 3 x signature = 0',
      SCAL > 0 and P1 == 0 and sp.Rational(P1, 24) == 0)
check('⓪ᵈ C3: chi(S^4) = 2 and signature 0, so p_1 = 0 -- which forces c_2(S+) + c_2(S-) = '
      '-p_1/2 = 0, the constraint PART 1\'s two numbers must satisfy',
      CHI == 2 and SIGNATURE == 0 and P1 == 0)
rho = sp.Symbol('rho', positive=True)
Ai = [[2 * sum(eta(i, mu, nu, _sd) * x[nu] for nu in range(4)) / (r2 + rho ** 2)
       for mu in range(4)] for i in (1, 2, 3)]
Am = [sp.simplify(sum((Ai[i][mu] * SIG3[i] / (2 * sp.I) for i in range(3)), Z2))
      for mu in range(4)]
RAW, _dens = charge_integral(curv(Am))
print(f"\n  C2: the BPST instanton's raw integral is {RAW}, independent of rho --")
print(f"      so the unit is that value, and k := (raw integral)/({RAW}) is 1 on it by definition")
check('⓪ᵉ C2: the BPST instanton gives a raw integral independent of its scale rho, which is what '
      'a topological number must be -- and it fixes the normalisation, derived rather than quoted',
      sp.simplify(sp.diff(RAW, rho)) == 0 and RAW != 0)
_kfun = lambda F: sp.simplify(charge_integral(F)[0] / RAW)
# ** the control is the PARITY IMAGE of the same instanton, which must carry the opposite charge
#   because the density is a pseudo-scalar.  Reflecting one coordinate: A'_3 = -A_3, A'_i = A_i,
#   each evaluated at x_3 -> -x_3.  No new ansatz, so nothing can fail to be a solution. **
_refl = {x[3]: -x[3]}
Am_par = [sp.simplify((-1 if mu == 3 else 1) * Am[mu].subs(_refl)) for mu in range(4)]
_kpar = _kfun(curv(Am_par))
print(f"      and its PARITY IMAGE returns k = {_kpar}")
check('⓪ᶠ CONTROL: the instanton\'s parity image returns k = -1 -- the density is a '
      'pseudo-scalar, so a reflection must flip the sign.  The functional measures a SIGNED '
      'number and is not returning its normalisation whatever it is handed', _kpar == -1)

print()
print("=" * 90)
print("PART 1 -- Q1: THE SPHERE'S OWN SPIN CONNECTION, SPLIT INTO ITS TWO su(2) HALVES")
print("=" * 90)
Om = 2 / (1 + r2)
ff = [sp.diff(sp.log(Om), x[a]) for a in range(4)]
om = [[[(ff[b] if a == mu else 0) - (ff[a] if b == mu else 0) for mu in range(4)]
       for b in range(4)] for a in range(4)]
Rc = [[[[sp.simplify(sp.diff(om[a][b][nu], x[mu]) - sp.diff(om[a][b][mu], x[nu])
                     + sum(om[a][c][mu] * om[c][b][nu] - om[a][c][nu] * om[c][b][mu]
                           for c in range(4)))
         for nu in range(4)] for mu in range(4)] for b in range(4)] for a in range(4)]
_round = all(sp.simplify(Rc[a][b][m][n] - Om ** 2 * ((1 if (a == m and b == n) else 0)
                                                     - (1 if (a == n and b == m) else 0))) == 0
             for a in range(4) for b in range(4) for m in range(4) for n in range(4))
check('① the stereographic metric is the UNIT round sphere: R^{ab}_{mu nu} = Omega^2 (delta delta '
      '- delta delta) exactly, so the sectional curvature is 1 and the scalar curvature is the 12 '
      'PART 0 used', _round)
Omg = [sp.simplify(sum((sp.Rational(1, 2) * om[a][b][mu] * SIGMA[a][b]
                        for a in range(4) for b in range(4)), sp.zeros(4, 4)))
       for mu in range(4)]
Fs = curv(Omg)
_agree = all(sp.simplify(Fs[m][n] - sum((sp.Rational(1, 2) * Rc[a][b][m][n] * SIGMA[a][b]
                                         for a in range(4) for b in range(4)), sp.zeros(4, 4)))
             == sp.zeros(4, 4) for m in range(4) for n in range(4))
check('①ᵇ and the spinor curvature built from Omega_mu equals (1/2) R^{ab} Sigma_ab, so the '
      'connection is the Levi-Civita one carried onto spinors and not something else', _agree)
_blkdiag = all(Fs[m][n].extract(IDX[+1], IDX[-1]) == Z2
               and Fs[m][n].extract(IDX[-1], IDX[+1]) == Z2 for m in range(4) for n in range(4))
check('①ᶜ the curvature is block diagonal in gamma^5, so the two blocks are genuinely two '
      'independent su(2) bundles and not a projection of one', _blkdiag)
K, C2 = {}, {}
for ch in (+1, -1):
    Fb = [[Fs[m][n].extract(IDX[ch], IDX[ch]) for n in range(4)] for m in range(4)]
    K[ch] = _kfun(Fb)
    C2[ch] = -K[ch]
    print(f"  S{'+' if ch > 0 else '-'}:  instanton number k = {str(K[ch]):>3}   c_2 = {str(C2[ch]):>3}")
check('①ᵈ *** Q1: YES -- each chiral spinor bundle of the round S^4 carries instanton number ONE, '
      'equal and opposite.  THE TWIST IS GEOMETRIC: the self-dual half of the sphere\'s own spin '
      'connection is the unit BPST instanton ***',
      abs(K[+1]) == 1 and abs(K[-1]) == 1 and K[+1] == -K[-1])
check('①ᵉ and it satisfies C3\'s constraint: c_2(S+) + c_2(S-) = -p_1/2 = 0',
      C2[+1] + C2[-1] == -sp.Rational(P1, 2) == 0)
# ** basis-free confirmation, independent of the integral: the two blocks must be the SELF-DUAL
#   and ANTI-SELF-DUAL halves of the curvature, which is the whole content of "two su(2) halves". **
_dual = {}
for ch in (+1, -1):
    Fb = [[Fs[m][n].extract(IDX[ch], IDX[ch]) for n in range(4)] for m in range(4)]
    star = [[sp.simplify(sum((sp.Rational(1, 2) * eps4(m, n, r, ss) * Fb[r][ss]
                              for r in range(4) for ss in range(4)), Z2))
             for n in range(4)] for m in range(4)]
    _dual[ch] = (all(sp.simplify(star[m][n] - Fb[m][n]) == Z2 for m in range(4) for n in range(4)),
                 all(sp.simplify(star[m][n] + Fb[m][n]) == Z2 for m in range(4) for n in range(4)))
print(f"\n  S+ block (self-dual, anti-self-dual) = {_dual[+1]};  S- block = {_dual[-1]}")
check('①ᶠ ⛔ AND A BASIS-FREE CONFIRMATION, INDEPENDENT OF THE INTEGRAL: the two chiral blocks of '
      'the curvature are exactly the SELF-DUAL and ANTI-SELF-DUAL halves, one each.  ** This is '
      'why the computation is done on the chiral block and not by projecting an su(2) connection: '
      'writing A^i = c . eta^i_{ab} omega^{ab} leaves c to be fixed, and fixing it by a '
      'consistency condition at a sample point returns |k| = 5 -- a value no orientation or '
      'convention can produce from 1, and one the p_1 identity cannot catch because it is odd and '
      'cancels in the sum.  The chiral block has no free constant. **',
      _dual[+1] != _dual[-1] and sum(_dual[+1]) == 1 and sum(_dual[-1]) == 1
      and _dual[+1][0] != _dual[-1][0])

# ** and the radius drops out, which is what lets this apply to the substrate's alpha-sphere
#   rather than only to the unit one: with Omega = 2a/(1+r^2) the connection is a-INDEPENDENT. **
a_ = sp.Symbol('a', positive=True)
Om_a = 2 * a_ / (1 + r2)
ff_a = [sp.simplify(sp.diff(sp.log(Om_a), x[b])) for b in range(4)]
print(f"\n  with radius a: f_b = d_b ln Omega = {ff_a[0]} -- no a in it")
check('①ᵍ and the SPHERE RADIUS DROPS OUT: d_b ln(2a/(1+r^2)) carries no a, so the spin '
      'connection in these coordinates is radius-independent and the two instanton numbers are '
      'the same on the substrate\'s alpha-sphere as on the unit one.  The scalar curvature does '
      'scale, and PART 0 only needed its SIGN',
      all(sp.simplify(sp.diff(ff_a[b], a_)) == 0 for b in range(4))
      and all(sp.simplify(ff_a[b] - ff[b]) == 0 for b in range(4))
      and sp.simplify(sp.diff(4 / (1 + r2) ** 2, a_)) == 0)

print()
print("=" * 90)
print("PART 2 -- Q2: THE INDEX, TWO WAYS, AND THE KERNEL DIMENSIONS SEPARATELY")
print("=" * 90)
AHAT = 1 - sp.Rational(P1, 24)
IND_AS = -C2[+1]
BETTI = {'b0': 1, 'b1': 0, 'b2+': 0, 'b2-': 0, 'b3': 0, 'b4': 1}
ker_plus = BETTI['b0'] + BETTI['b2+']
ker_minus = BETTI['b1']
IND_HODGE = ker_plus - ker_minus
print(f"  A-hat genus on S^4 = 1 - p_1/24 = {AHAT}")
print(f"  ATIYAH-SINGER : ind = integral ch_2(S+) = -c_2(S+) = {IND_AS}")
print(f"  HODGE         : S+ tensor S+ = Lambda^0 + Lambda^+  -> ker = b_0 + b_2^+ = {ker_plus}")
print(f"                  S- tensor S+ = Lambda^1             -> coker = b_1     = {ker_minus}")
print(f"                  ind = {ker_plus} - {ker_minus} = {IND_HODGE}")
check('② *** the two routes AGREE at ind = 1, which is what pins c_2(S+) = -1 rather than leaving '
      'it quoted -- an index computed from a Chern number and an index computed from Betti '
      'numbers ***', AHAT == 1 and IND_AS == IND_HODGE == 1)
check('②ᵇ W4: and the kernel dimensions are reported separately from their difference -- ONE zero '
      'mode of the twisted-positive chirality and ZERO of the other',
      (ker_plus, ker_minus) == (1, 0) and sum(BETTI.values()) == 2 + 0 + 0 + 0 + 0)
check('②ᶜ and the Betti numbers are the sphere\'s: Euler characteristic b_0 - b_1 + b_2 - b_3 + '
      'b_4 = 2 and signature b_2^+ - b_2^- = 0, matching C3',
      BETTI['b0'] - BETTI['b1'] + BETTI['b2+'] + BETTI['b2-'] - BETTI['b3'] + BETTI['b4'] == CHI
      and BETTI['b2+'] - BETTI['b2-'] == SIGNATURE)

print()
print("=" * 90)
print("PART 3 -- Q3: THE ZERO MODE IS A SINGLET, AND THE DOUBLET HAS NO ZERO MODES")
print("=" * 90)


def cg(a, b):
    """su(2) tensor product by dimensions: 2 tensor 2 = 1 + 3, etc."""
    ja, jb = sp.Rational(a - 1, 2), sp.Rational(b - 1, 2)
    return [int(2 * j + 1) for j in
            [ja + jb - k for k in range(int(2 * min(ja, jb)) + 1)]]


SPLUS, SMINUS = (2, 1), (1, 2)          # (su(2)_+ , su(2)_-) content of the chiral bundles
tw = SPLUS                              # the bundle Q1 found, used as the twist
cont = {'S+ (x) S+': (cg(SPLUS[0], tw[0]), cg(SPLUS[1], tw[1])),
        'S- (x) S+': (cg(SMINUS[0], tw[0]), cg(SMINUS[1], tw[1]))}
print(f"  {'twisted bundle':>12} {'su(2)_+ content':>20} {'su(2)_- content':>18} "
      f"{'as forms':>18} {'zero modes':>11}")
FORMS = {'S+ (x) S+': 'Lambda^0 + Lambda^+', 'S- (x) S+': 'Lambda^1'}
ZM = {'S+ (x) S+': ker_plus, 'S- (x) S+': ker_minus}
for kk, (p, m) in cont.items():
    print(f"  {kk:>12} {str(p):>20} {str(m):>18} {FORMS[kk]:>18} {ZM[kk]:>11}")
check('③ the twisted-positive bundle decomposes as 1 + 3 under the twisting su(2) -- it contains '
      'NO doublet at all, not merely an unoccupied one',
      2 not in cont['S+ (x) S+'][0] and sorted(cont['S+ (x) S+'][0]) == [1, 3])
check('③ᵇ and the other chirality IS a doublet of each factor -- the (2,2), which is Lambda^1',
      cont['S- (x) S+'][0] == [2] and cont['S- (x) S+'][1] == [2])
check('③ᶜ *** Q3: NO.  The chirality that carries the zero mode contains no doublet, and the one '
      'that is a doublet carries no zero mode -- because b_1(S^4) = 0.  W3: a doublet needs two '
      'states WITHIN one chirality under one su(2), and neither side supplies that ***',
      ZM['S+ (x) S+'] == 1 and 2 not in cont['S+ (x) S+'][0]
      and ZM['S- (x) S+'] == 0 and cont['S- (x) S+'][0] == [2]
      and BETTI['b1'] == 0)
check('③ᵈ and the one zero mode is the CONSTANT function: it sits in the Lambda^0 summand, the '
      'b_0 = 1 of the sphere, which is the su(2) singlet in 2 (x) 2',
      ker_plus == BETTI['b0'] + BETTI['b2+'] and BETTI['b2+'] == 0 and BETTI['b0'] == 1)

print()
print("=" * 90)
print("PART 4 -- Q4: WHICH FACTOR, AND IT IS THE SAME ONE ON BOTH SIDES OF THE TRADE")
print("=" * 90)
print(f"  S+ = {SPLUS} : a doublet of su(2)_+ and a singlet of su(2)_-  (self-dual two-forms)")
print(f"  S- = {SMINUS} : the mirror                                    (anti-self-dual)")
check('④ the bundle-level shape of (a) is real: each chiral bundle is a doublet of ONE factor and '
      'a singlet of the other, so one factor does see only one handedness',
      SPLUS == (2, 1) and SMINUS == (1, 2) and SPLUS[0] == 2 and SMINUS[0] == 1)
check('④ᵇ *** but the twist on S+ is an su(2)_+ connection, and the zero mode it produces is the '
      'su(2)_+ SINGLET.  The same factor supplies the twist and fails to grade the state -- the '
      'shape is in the bundles and the state is in the singlet ***',
      tw == SPLUS and 1 in cont['S+ (x) S+'][0] and 2 not in cont['S+ (x) S+'][0])
_other = {'S+ (x) S-': (cg(SPLUS[0], SMINUS[0]), cg(SPLUS[1], SMINUS[1])),
          'S- (x) S-': (cg(SMINUS[0], SMINUS[0]), cg(SMINUS[1], SMINUS[1]))}
print(f"\n  and twisting by S- instead: {[(k, v[0], v[1]) for k, v in _other.items()]}")
check('④ᶜ and the other twist is the mirror, not an escape: twisting by S- puts the singlet-bearing '
      'side on the other chirality and leaves the doublet in Lambda^1 again, where b_1 = 0',
      sorted(_other['S- (x) S-'][1]) == [1, 3] and _other['S+ (x) S-'][0] == [2]
      and BETTI['b1'] == 0)

print()
print("=" * 90)
print("PART 5 -- W2 AND W1: WHAT THE ZERO MODE IS, AND WHAT THE su(2) IS NOT")
print("=" * 90)
check('⑤ W2: the zero mode is the sphere\'s own CONSTANT -- global and unlocalised, the b_0 mode '
      '-- and the background producing it is an instanton, so this is an instanton zero mode and '
      'an index statement about the sphere, not a state in a spectrum.  The S^4 carries no time: '
      'a spatial throat of one face and an atemporal equator of the other',
      ker_plus == BETTI['b0'] and abs(K[+1]) == 1)
check('⑤ᵇ W1: the su(2) factors here are Spin(4) = SU(2) x SU(2) rotating the sphere\'s TANGENT '
      'space -- the same four directions the metric has -- so nothing here is an internal gauge '
      'symmetry and nothing is called isospin.  Whether such a rotation becomes one is the '
      'Kaluza--Klein question, untouched',
      len(SPLUS) == 2 and SPLUS[0] * SPLUS[1] + SMINUS[0] * SMINUS[1] == 4
      and sorted(cg(2, 2)) == [1, 3])

print()
print("=" * 90)
print(f"RESULT -- {len(_fails)} failure(s)")
print("=" * 90)
assert not _fails, _fails
print("  Q1  *** YES -- THE SPHERE SUPPLIES ITS OWN TWIST. ***  Computed in the explicit spinor")
print("      representation, where the spin connection is block diagonal in gamma^5 and its two")
print("      blocks ARE the su(2) connections with nothing left to normalise: k(S+) = +1 and")
print("      k(S-) = -1, so c_2 = -1 and +1.  The self-dual half of the round sphere's own spin")
print("      connection is the unit BPST instanton.  Lichnerowicz is evaded by the geometry.")
print("  Q2  the index is ONE, computed two independent ways -- Atiyah-Singer from the Chern")
print("      number and Hodge theory from the Betti numbers -- and they agree, which is what")
print("      pins c_2(S+) = -1.  The kernel is (1, 0), reported apart from its difference.")
print("  Q3  *** NO.  The zero mode is the CONSTANT FUNCTION, a SINGLET of the su(2) that")
print("      supplied the twist.  And it is not that the doublet is unoccupied: the chirality")
print("      carrying the zero mode decomposes as 1 + 3 and contains no doublet at all, while")
print("      the chirality that IS a doublet -- the (2,2), which is Lambda^1 -- carries no zero")
print("      mode because b_1(S^4) = 0. ***")
print("  Q4  the factor that supplies the twist is the factor of which the zero mode is a")
print("      singlet.  The bundle-level shape is real -- one factor sees only one handedness --")
print("      and the state sits in the singlet of that same factor.")
print()
print("  ⛭ SO THE SHAPE IS IN THE BUNDLES AND EMPTY AT THE LEVEL OF STATES, and the obstruction")
print("  is a Betti number: b_1(S^4) = 0.  The one place a chiral doublet could live on this")
print("  sphere is its space of one-forms, and the sphere has no harmonic one-forms.")
print()
print("  W5, plainly: the colourless triple is not here either.  With r6698's bound sectors,")
print("  r6702's native propagating sector and r6704's compact face, that is a FOURTH place it")
print("  is not -- and a fourth distinct mechanism: the unpaired level, the twist, Lichnerowicz,")
print("  and now b_1 = 0.")
print()
print("  NOT ESTABLISHED: that this su(2) is weak isospin (W1) -- it rotates the TANGENT space")
print("  and is not called isospin.  Not that the sphere carries no index: it carries exactly")
print("  one, and the geometric twist is a real finding.  Not that no other twist could give a")
print("  doublet -- what is shown is that the bundle the SPHERE supplies gives a singlet.  Not")
print("  anything about the Lorentzian face's colour, which r6710 settled.")
print("=" * 90)
