#!/usr/bin/env python3
"""r7619+cc66 -- is the face's THERMAL TRACE a spectral action for the r7615 triple?

Registered in PREDICTION.md in this directory before a line of this file existed.

The spectral action is Tr f(D/Lambda) and its Yang-Mills coefficient is a MOMENT of f.  The
construction supplies a trace of its own: the horizon's Gibbs weight at beta = 2 pi alpha.  If that
weight is e^{-beta H} with H a FUNCTION of D, then it IS f(D/Lambda) with f the exponential and
Lambda = 1/beta -- and the coupling's normalisation follows.  So the whole row turns on one question
that is countable and exact:

    ** IS THE THERMAL WEIGHT'S GENERATOR A FUNCTION OF D? **

and the trap, registered in advance, is that D COMMUTES with the generator of any isometry, so a naive
reading stops there and says yes.  Commuting is not being a function of.  A function of D is CONSTANT
ON EVERY D-EIGENSPACE, and that is what gets measured here.
"""
import os
import re
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CORPUS = os.path.join(ROOT, 'corpus')
CHECKS = []


def check(name, ok, detail=''):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f'   ->  {detail}' if detail else ''), flush=True)


def head(t):
    print('\n' + '=' * 78 + f'\n {t}\n' + '=' * 78)


def reads(fn, needle):
    """the literal, as the paper prints it -- whitespace-folded so a line break cannot hide it"""
    txt = re.sub(r'\s+', ' ', open(os.path.join(CORPUS, fn), encoding='utf-8',
                                  errors='replace').read())
    return re.sub(r'\s+', ' ', needle) in txt


# =============================================================================================
head('Ⓐ  WHAT THE PAPERS SAY THE THERMAL DATUM IS -- READ, NOT RECALLED')
# =============================================================================================
EUCL = r'a Euclidean continuation of period $\beta=2\pi\alpha$'
SAME = r'and that Euclidean is the \emph{same} face'
HPHYS = r'is solved for the generator of advance, $i\,\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$'

check(f'P13 says what beta is -- READ: "{EUCL}"', reads('boundary_paper.tex', EUCL),
      'found in boundary_paper.tex')
check('** and says the Euclidean section IS THE FACE, which is what makes this order non-trivial: '
      'the thermal circle is a great circle of the very manifold D lives on **',
      reads('boundary_paper.tex', SAME), 'found in boundary_paper.tex')
check("and the construction's own generator of evolution is the deparametrized true Hamiltonian on "
      'COSMIC TIME, not an operator on the face', reads('CR_framework.tex', HPHYS),
      'found in CR_framework.tex')

print("""
  ⇒ TWO readings of "the thermal weight's operator", and they are not equally favourable to the
    order.  ⑴ H_phys, which advances the LAYERS along cosmic time and does not act on spinors over
    the face at all -- under that reading the question is not answered negatively, it is ILL-POSED
    (pre-registered outcome 3, which I undertook not to report as outcome 2).  ⑵ the generator of
    rotation along the face's own great circle of circumference beta -- internal to the face, acting
    on the same spinors as D.  ** ⑵ is the order's suggestion at its strongest, so ⑵ is what gets
    tested below. **""")


# =============================================================================================
head('Ⓑ  THE INSTRUMENT: "IS B A FUNCTION OF A?" -- CONSTANT ON EVERY A-EIGENSPACE')
# =============================================================================================
def eigenspaces(A, tol=1e-9):
    """(eigenvalue, orthonormal basis of its eigenspace) for a hermitian A, degeneracies merged."""
    w, V = np.linalg.eigh(A)
    out, i = [], 0
    while i < len(w):
        j = i
        while j + 1 < len(w) and abs(w[j + 1] - w[i]) < tol:
            j += 1
        out.append((w[i], V[:, i:j + 1]))
        i = j + 1
    return out


def function_of(B, A, tol=1e-7):
    """Is B constant on each A-eigenspace?  Returns (verdict, worst spread, largest eigenspace dim).

    On an eigenspace with basis P, B is scalar there iff P^dag B P is a multiple of the identity;
    the SPREAD of that block's eigenvalues is the measurement.  ⌗ The largest eigenspace dimension
    comes back too, because on a ONE-dimensional eigenspace every operator is scalar and the test
    would pass for free -- the non-vacuity guard r7615 cost me, placed here at the instrument
    rather than at the call site so no caller can forget it.
    """
    worst, dmax = 0.0, 0
    for _lam, P in eigenspaces(A, tol=1e-9):
        blk = P.conj().T @ B @ P
        ev = np.linalg.eigvalsh(blk) if blk.shape[0] > 1 else np.array([blk[0, 0].real])
        worst = max(worst, float(ev.max() - ev.min()))
        dmax = max(dmax, blk.shape[0])
    return worst < tol, worst, dmax


_A_fn = np.diag([1.0, 1.0, 2.0, 3.0])
_B_fn = _A_fn @ _A_fn - 2 * _A_fn            # a polynomial in A, so a function of it by construction
_ok_fn, _sp_fn, _d_fn = function_of(_B_fn, _A_fn)
check('CONTROL: the instrument CERTIFIES a true function pair -- B = A^2 - 2A is constant on every '
      'A-eigenspace, including the degenerate one, so a "no" from it later is worth something',
      _ok_fn and _d_fn > 1, f'function_of = {_ok_fn}, spread = {_sp_fn:.2e}, largest eigenspace = {_d_fn}')

_A_cm = np.diag([1.0, 1.0, 2.0])
_B_cm = np.diag([1.0, 2.0, 3.0])
_comm = float(np.abs(_A_cm @ _B_cm - _B_cm @ _A_cm).max())
_ok_cm, _sp_cm, _d_cm = function_of(_B_cm, _A_cm)
check('** CONTROL, AND IT IS THE HINGE OF THIS ROW: a pair that COMMUTES EXACTLY and is NOT a '
      'function pair -- so commuting and being-a-function-of come apart, and the naive reading that '
      'stops at [D,H]=0 is measurably wrong **',
      _comm == 0.0 and not _ok_cm and _d_cm > 1,
      f'||[A,B]|| = {_comm:.1e} yet function_of = {_ok_cm}, spread = {_sp_cm:.1f} on a '
      f'{_d_cm}-dimensional eigenspace')


# =============================================================================================
head("Ⓒ  THE FACE'S LOWEST DIRAC EIGENSPACE, AND THE GREAT-CIRCLE GENERATOR ON IT")
# =============================================================================================
def gammas_6d():
    """6-dimensional Euclidean Clifford generators, 8x8, built by tensoring Pauli matrices."""
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    kron = lambda *m: np.kron(np.kron(m[0], m[1]), m[2])
    return [kron(sx, I2, I2), kron(sy, I2, I2),
            kron(sz, sx, I2), kron(sz, sy, I2),
            kron(sz, sz, sx), kron(sz, sz, sy)]


G = gammas_6d()
_cliff = max(float(np.abs(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(8)).max())
             for a in range(6) for b in range(6))
check('the Clifford algebra is BUILT and verified, not quoted: {gamma_a, gamma_b} = 2 delta_ab on '
      'all 36 pairs of the 8x8 generators', _cliff < 1e-12, f'max defect = {_cliff:.1e}')

CHI = -1j * G[0] @ G[1] @ G[2] @ G[3] @ G[4] @ G[5]      # the 6d chirality, eigenvalues +-1
_chi_ev = np.round(np.linalg.eigvalsh(CHI), 9)
_n_plus = int((_chi_ev > 0).sum())
check('the chirality splits the 8 spinors into 4 + 4, which is the dimension the MULTIPLICITY '
      'FORMULA independently gives for the face\'s lowest Dirac level -- 2^floor(5/2) * C(4,0) = 4, '
      'so two routes agree on the number before anything is asked of it',
      _n_plus == 4 and 2 ** (5 // 2) * 1 == 4, f'chirality eigenvalues {sorted({round(float(x), 6) for x in _chi_ev})}, '
      f'dim(+) = {_n_plus}, multiplicity formula = {2 ** (5 // 2)}')

# ⌗ ** WHAT THIS BLOCK TAKES AS INPUT RATHER THAN DERIVES, DECLARED SO IT CAN BE CHECKED AGAINST. **
#   Three standard facts about the round five-sphere, none of them in the corpus and none computed
#   here: ⒜ the lowest Dirac eigenspace is the space of Killing spinors; ⒝ it carries ONE chirality
#   4 of Spin(6) (whose dimension the multiplicity formula independently confirms above); ⒞ a
#   rotation of the ambient R^6 in the (1,2)-plane is an isometry of S^5 whose great-circle orbit
#   has circumference 2 pi alpha = beta, and whose spinorial lift is Sigma_12 = (i/2) gamma_1
#   gamma_2.  ** If any of the three is wrong this row is wrong, and that is the exposure. **  What
#   is COMPUTED is everything after: the Clifford algebra, the chirality split, the weights, the
#   commutator, and the thermal weight's spread.
# D is the SAME multiple of the identity on its own eigenspace (5/2alpha), so as an operator there D
# is scalar -- stated explicitly because it is the whole point of the test.
P4 = np.linalg.eigh(CHI)[1][:, _chi_ev > 0]              # 8x4 isometry onto the chirality-4
D_on_4 = np.eye(4, dtype=complex)                        # D = (5/2alpha) * 1 there, up to the scale

# The great circle's rotation generator, lifted to spinors: Sigma_12 = (i/2) gamma_1 gamma_2.
SIG12 = 0.5j * G[0] @ G[1]
H_theta = P4.conj().T @ SIG12 @ P4
_w = np.round(np.linalg.eigvalsh(H_theta), 9)
_spread = float(_w.max() - _w.min())
_wlist = sorted({round(float(x), 6) for x in _w})

_commDH = float(np.abs(D_on_4 @ H_theta - H_theta @ D_on_4).max())
check('** FIRST, THE TRAP IS REAL AND MEASURED: the great-circle generator COMMUTES with D on this '
      'eigenspace, exactly -- which is the step a naive reading would stop at **',
      _commDH < 1e-12, f'||[D, H_theta]|| = {_commDH:.1e}')

_ok_face, _sp_face, _d_face = function_of(H_theta, D_on_4)
check('** AND YET IT IS NOT A FUNCTION OF D: the lowest Dirac eigenspace is FOUR-dimensional and the '
      'great-circle generator takes TWO distinct values on it, so no f can reproduce it -- a function '
      'of D is constant on every D-eigenspace and this is not **',
      (not _ok_face) and _d_face == 4 and _spread > 0.5,
      f'weights on the 4 = {_wlist}, spread = {_sp_face:.1f} on a {_d_face}-dimensional '
      f'D-eigenspace')
check('NON-VACUITY, the guard r7615 cost me: the eigenspace tested is of dimension 4 > 1, so the '
      '"not scalar" above is a measurement -- on a one-dimensional eigenspace every operator is '
      'scalar and the test could not have failed',
      _d_face > 1, f'dim = {_d_face}')

# ⌗ The sharpest form of the failure, in the construction's own number: the thermal weight on this
#   eigenspace is e^{-beta H_theta} with beta/alpha = 2 pi EXACTLY, so its eigenvalues are
#   e^{∓(beta/alpha)(1/2)} = e^{∓pi} -- TWO values where any f(D/Lambda) would give one.
_gibbs = sorted(float(np.exp(-2 * np.pi * float(x))) for x in _wlist)
_ratio = _gibbs[-1] / _gibbs[0]
check('** AND IN THE CONSTRUCTION\'S OWN NUMBER: with beta/alpha = 2 pi exactly, the thermal weight '
      'e^{-beta H_theta} takes the two values e^{-pi} and e^{+pi} on this ONE D-eigenspace -- it '
      'varies across it by a factor of e^{2 pi}, where any f(D/Lambda) is constant by construction **',
      abs(_ratio - np.exp(2 * np.pi)) < 1e-6 and len(_gibbs) == 2,
      f'weights {_gibbs[0]:.4f} and {_gibbs[1]:.4f}, ratio = {_ratio:.2f} = e^(2 pi)')
check('⌗ and one of those exceeds 1, so this generator is not a positive Hamiltonian either -- '
      'recorded because it is a strain on the identification and not a point in its favour',
      _gibbs[-1] > 1, f'max weight = {_gibbs[-1]:.2f} > 1')

print(f"""
  ⇒ The weights are {_wlist}: the rotation acts on the Killing spinors as the U(1) inside
    Spin(6) whose weights on the chirality-4 are +-1/2, NOT as a scalar.  ** So e^{{-beta H_theta}}
    is not f(D/Lambda) for ANY f **, and the favourable reading ⑵ fails on its own terms rather
    than on the Hilbert-space mismatch of reading ⑴.""")


# =============================================================================================
head('Ⓓ  LAMBDA -- THE SLOT r7615\'s DIMENSIONAL ARGUMENT NEVER REACHED')
# =============================================================================================
p_a, p_b = sp.symbols('p_a p_b', real=True)
# a dimensionless monomial alpha^p_a beta^p_b needs p_a + p_b = 0  (r7615's solve)
_dimless = sp.solve([sp.Eq(p_a + p_b, 0)], [p_a], dict=True)
# a monomial of dimension length^-1, which is what Lambda is, needs p_a + p_b = -1
_scale = sp.solve([sp.Eq(p_a + p_b, -1)], [p_a], dict=True)
check('** r7615\'s solve is CORRECT and INCOMPLETE, and the same solver says so: a dimensionless '
      'monomial forces p_a = -p_b, but Lambda is an INVERSE LENGTH and the exponents p_a + p_b = -1 '
      'have solutions -- beta^-1 among them.  So the construction DOES supply a Lambda, and my own '
      'earlier dimensional argument never reached that slot **',
      bool(_dimless) and bool(_scale) and _dimless[0][p_a] == -p_b and _scale[0][p_a] == -p_b - 1,
      f'dimensionless: {_dimless[0][p_a]};  length^-1: p_a = {_scale[0][p_a]}, so beta^-1 qualifies')
al = sp.Symbol('alpha', positive=True)
beta = 2 * sp.pi * al
check('and the scale the construction would supply is EXACTLY 1/(2 pi alpha), computed from '
      'beta = 2 pi alpha rather than named', sp.simplify(1 / beta - 1 / (2 * sp.pi * al)) == 0,
      f'Lambda = 1/beta = {sp.simplify(1 / beta)}')


# =============================================================================================
head('Ⓔ  CONTROL: A CUTOFF FUNCTION THAT *DOES* FIX A COUPLING, AND THE COEFFICIENT MOVES WITH f')
# =============================================================================================
u, k = sp.symbols('u k', positive=True)
mom_exp = sp.integrate(sp.exp(-u) * u ** (k - 1), (u, 0, sp.oo))          # Gamma(k)
mom_gauss = sp.integrate(sp.exp(-u ** 2) * u ** (k - 1), (u, 0, sp.oo))   # Gamma(k/2)/2
m4_exp = sp.simplify(mom_exp.subs(k, 4))
m4_gauss = sp.simplify(mom_gauss.subs(k, 4))
check('CONTROL: given an f, the Yang-Mills order moment is a DEFINITE NUMBER -- the fourth moment '
      'of the exponential cutoff is 6 and of the Gaussian is 1/2, both INTEGRATED here rather than '
      'quoted', m4_exp == 6 and m4_gauss == sp.Rational(1, 2),
      f'exponential: {m4_exp};  Gaussian: {m4_gauss}')
check('** AND IT MOVES WHEN f MOVES, by a factor of 12 on these two -- which is what makes "no f, no '
      'coupling" a measurement rather than a form of words.  That is the charge I levelled at a '
      'dimensional argument in r7615 and must not earn myself **',
      m4_exp != m4_gauss and sp.simplify(m4_exp / m4_gauss) == 12,
      f'ratio = {sp.simplify(m4_exp / m4_gauss)}')
check('and the moment is finite and non-zero for both, so the coefficient is fixed rather than '
      'merely different -- if an f WERE supplied, the coupling would follow',
      m4_exp.is_finite and m4_exp != 0 and m4_gauss.is_finite and m4_gauss != 0,
      'both finite, both non-zero')


# =============================================================================================
head('Ⓕ  THE VERDICT -- INSIDE THE ASSERT, WHERE IT CAN FAIL')
# =============================================================================================
check('** ⑴ THE FAVOURABLE READING FAILS ON ITS OWN TERMS: the face\'s thermal circle is internal to '
      'the face, its generator commutes with D exactly, and it is STILL not a function of D -- two '
      'distinct weights +-1/2 on a four-dimensional D-eigenspace.  No f reproduces it, so the '
      'thermal trace is NOT a spectral action of this triple **',
      _commDH < 1e-12 and not _ok_face and _d_face == 4,
      f'[D,H] = 0 and yet weights {_wlist} on dim {_d_face}')
check('** ⑵ AND THE CONSTRUCTION DOES SUPPLY HALF OF WHAT THE SPECTRAL ACTION NEEDS, WHICH r7615 '
      'MISSED: Lambda = 1/beta is an admissible inverse-length scale, so what is missing is f ALONE '
      '-- and f is exactly what a moment-fixed coupling requires, the moment being 6 against 1/2 on '
      'two explicit cutoffs **',
      bool(_scale) and m4_exp != m4_gauss,
      'Lambda supplied, f not; pre-registered outcome 2, with outcome 3 holding separately for '
      'H_phys')

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print('\n' + '=' * 78 + '\n ' + ('ALL CHECKS PASS' if not bad else 'FAILURES ABOVE') + '\n' + '=' * 78)
assert not bad, f'{len(bad)} check(s) failed: {bad}'
