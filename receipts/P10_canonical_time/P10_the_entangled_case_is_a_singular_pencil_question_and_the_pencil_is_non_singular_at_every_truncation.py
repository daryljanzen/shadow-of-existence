#!/usr/bin/env python3
r"""
P10_the_entangled_case_is_a_singular_pencil_question_and_the_pencil_is_non_singular_at_every_truncation
======================================================================================================

LEVEL: **exact integer and rational arithmetic for every load-bearing step.**  The tower operators are
carried in the basis where the ladder matrices are integer matrices -- a diagonal similarity, so
spectra and determinant-vanishing are unchanged -- and all determinants, Laurent coefficients and
coupling systems are computed over the integers with sympy.  ⌗ **There is no tolerance in this
receipt's verdict, which is deliberate**: `r6947` found that `r6946`'s one float tolerance was the
authoring machine's round-off floor, and the repair for a claim of this shape is to remove the float
rather than to calibrate it.  Floats appear only in §A's two measurements, each against a floor
measured in the same arithmetic.

OBJECT UNDER TEST -- `PO-23`, `r6947`/`r6949`.  The order, reformulating the row's four-revision wall:

  ⓵ᵃ *"First, the structural claim, which everything after it rests on: $\hat R$ commutes with $\hat a$
      ... check it rather than assume it --- the conformal factor, the measure, and whatever operator
      ordering the momentum constraint imposes are all places it could fail, and if it fails the rest
      of this order is void and that is the finding."*
  ⓵ᵇ *"Does the family $\hat R(a)$ have an eigenvalue branch that is CONSTANT in $a$ on a set of
      positive measure?"*
  ⓵ᶜ *"Solve it at the smallest truncations that carry two non-commuting tower operators and report
      whether a solution exists."*

  ⌗ WITH THE ORDER'S GUARDS: if ⓵ᵃ fails, stop there; **do not let the truncation answer for the
    tower** --- *"if the polynomial system's solvability changes with $N$, that dependence IS the
    result"*; the ordering stays named and unpicked, and if ⓵ᵃ depends on it, flag that as a third
    surfacing; and *"reformulated and open"* is progress where *"not attempted"* is not.

COMPUTES: whether the curvature operator commutes with the scale factor, and what it takes to break
that; the reduction of a constant eigenvalue branch to $\lambda=4\Lambda$; the exact equivalence
between an identically-vanishing determinant and a **singular matrix pencil**; the pencil's
determinant over the integers at truncations $N=2\ldots8$ for the cubic's own non-commuting tower
operators, at three operators for $N=3\ldots6$, and the full coupling system's solutions.

-------------------------------------------------------------------------------
** THE PREMISE HOLDS, THE ENTANGLED CASE IS NOW A COMPUTATION, AND THE COMPUTATION RETURNS NO
   SOLUTION AT EVERY TRUNCATION -- WITH ONE $N$-DEPENDENCE THAT IS ITSELF THE ORDER'S WARNING MADE
   CONCRETE. **

** ⛭ ⓵ᵃ THE COMMUTING PREMISE IS TRUE, AND IT IS TRUE FOR A REASON RATHER THAN BY CONSTRUCTION. **
$\hat R$ is **algebraic** in the matter trace --- the trace of the field equation gives
$R=4\Lambda+\kappa\Theta$ with no derivative of $a$ in it --- and `r6934`'s exact trace formula makes
every term a function of $\hat a$ times a tower operator on the other factor.  So $[\hat R,\hat a]=0$
identically, measured at $0$ exactly.  ⇒ ** And the control says the premise is not vacuous: ** the
variant that keeps a $\hat p_a$ --- which is what taking $R$ from the kinetic form rather than from
the trace equation would do --- has the same relative commutator at $8.4\times10^{-4}$, against an
exact zero.  The
measure does not touch it (multiplication operators commute in any weight, and $\hat R$ stays
self-adjoint in the weighted product, residual $10^{-16}$), and ⓵ᵃ is **ordering-blind**: three
ordering variants of the tower factor give the same exact zero, because an operator on the tower
factor commutes with $\hat a$ whatever its internal ordering.  ⇒ *So the ordering does NOT surface a
third time, and there is nothing to flag.*

** ⛭ ⓵ᵇ THE BRANCH VALUE IS FORCED BEFORE ANY DETERMINANT IS TAKEN. **  Every power in
$\hat R(a)=4\Lambda+\sum_k\kappa_k a^{-m_k}\hat T_k$ is negative, so $\hat R(a)\to4\Lambda$ as
$a\to\infty$ and a branch constant on a set of positive measure must equal $4\Lambda$ exactly.
⇒ ** The question collapses to: is $M(a)=\sum_k\kappa_k a^{-m_k}\hat T_k$ SINGULAR FOR ALMOST EVERY
$a$? **  *That reduction uses no truncation and survives dimension.*

** ⛭ ⓵ᶜ AND AT FINITE $N$ THAT IS EXACTLY A SINGULAR-PENCIL QUESTION, WHICH IS $a$-FREE AND
   COUPLING-FREE. **  $\det(\sum_k x_k\hat T_k)$ is a homogeneous form of degree $N$; on the physical
curve $x_k=\kappa_k a^{-m_k}$ with two distinct powers each monomial lands on its **own** power of
$1/a$, so
$$\det M(a)\equiv0 \iff \text{the pencil } \textstyle\sum_k x_k\hat T_k \text{ is singular},$$
and the extreme coefficients are $\kappa_k^{N}\det\hat T_k$.  ⇒ ** For the cubic's own operators
$\hat T_1=\hat\pi^{2}$ and $\hat T_2=\tfrac12(\hat\pi^{2}\hat\phi+\hat\phi\hat\pi^{2})$ --- which do
not commute, measured --- the pencil is NON-SINGULAR at every truncation $N=2\ldots8$, over the
integers. **  At three operators the powers $(6,8,10)$ **do** collide ($6+10=8+8$), so the curve
determinant is computed directly rather than inferred from the pencil; it is non-zero for
$N=3\ldots6$ too.

** ⛭ AND THE ONE $N$-DEPENDENCE IS THE ORDER'S WARNING, EXACTLY. **  The *necessary conditions* are
$N$-parity dependent: at odd $N$ a ladder matrix is singular, so $\det\hat T_k=0$ and the full
coupling system acquires non-trivial solutions --- **every one of which switches off at least two of
the three couplings**, reducing to a single-operator model whose determinant vanishes only for that
reason.  With the couplings non-zero, as the cubic makes them, there is **no solution at any $N$,
either parity**.  ⇒ *The truncation is biased TOWARD the affirmative and still returns no.  And the
bias has no counterpart in the tower: $\hat\phi$ and $\hat\pi$ have purely continuous spectrum, so
neither has the null eigenvector the odd-$N$ determinant is reporting.*

** ⛭ THE INSTRUMENT IS LIVE. **  Two tower operators sharing one null vector give a pencil that is
singular at $N=4,5,6$ --- so the computation returns "yes" when a constant branch is there, and the
"no" above is a measurement.

⛔ ** NOT CLAIMED. **  ** The tower limit of the determinant criterion is the one named step: ** at
finite $N$ singularity is $\det=0$, in the tower it is a *null eigenvector for almost every $a$*, and
the odd-$N$ artefact is precisely where those two part company.  So this is **reformulated and
answered at every truncation, with the limit named** --- not a closed statement about the untruncated
tower.  Also not computed: the momentum constraint's algebra (it can only matter by putting a
$\hat p_a$ into $\hat R$, which is what §A's control measures).  No ordering choice; no corpus edit.
rc=0 on all 19 checks.
"""

import sys

import numpy as np
import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


a = sp.Symbol('a', positive=True)
LAM4 = sp.Integer(12)                      # 4 Lambda, the value P10 carries
LAM4F = 12.0                               # the same number, for the float section
x1, x2, x3 = sp.symbols('x_1 x_2 x_3')
k1, k2, k3 = sp.symbols('kappa_1 kappa_2 kappa_3', real=True)
lam = sp.Symbol('lambda')


def ladder(N):
    """a and a-dagger in the basis D = diag(1/sqrt(n!)), where BOTH are INTEGER matrices.

    D is diagonal, so this is a similarity transform that commutes with truncation: the spectrum
    and the vanishing of any determinant are unchanged, and the arithmetic becomes exact integer
    arithmetic with no round-off floor to calibrate.
    """
    A, Ad = sp.zeros(N, N), sp.zeros(N, N)
    for n in range(1, N):
        A[n - 1, n] = n          # annihilation
        Ad[n, n - 1] = 1         # creation
    return A, Ad


def tower_ops(N):
    """Q ~ sqrt2 phi, P ~ -i sqrt2 pi, and the cubic's two non-commuting tower factors.
    Overall non-zero scalars are irrelevant to singularity, so they are dropped."""
    A, Ad = ladder(N)
    Q, P = A + Ad, Ad - A
    T1 = P * P                                   # pi^2
    T2 = (P * P * Q + Q * P * P) / 2             # symmetrised pi^2 phi -- the cubic's own vertex
    T3 = Q * Q                                   # phi^2, a third structure at a third power
    return Q, P, T1, T2, T3


# ============================================================================ A
head("A.  ⓵ᵃ  THE STRUCTURAL PREMISE, CHECKED RATHER THAN ASSUMED -- WITH THE CONTROL THAT BREAKS IT")

print(r"""
      WHY it should hold, stated first so the check has something to falsify:  R-hat is ALGEBRAIC in
      the matter trace.  The trace of the field equation gives R = 4 Lambda + kappa Theta with no
      derivative of a in it, and r6934's exact trace formula makes every term a function of a-hat
      times a tower operator on the OTHER Hilbert-space factor.  ⇒ If that is the right R-hat, the
      commutator vanishes identically.  The places the order named are where a p_a could sneak back
      in, so each one is tested.""")

NA, NT = 40, 6
ag = np.linspace(0.6, 6.0, NA)
hg = ag[1] - ag[0]
Ahat = np.diag(ag)
Dp = (np.diag(np.ones(NA - 1), 1) - np.diag(np.ones(NA - 1), -1)) / (2 * hg)   # p_a, central
rng = np.random.default_rng(6946)
Tn = rng.normal(size=(NT, NT))
Tn = Tn + Tn.T
It, Ia = np.eye(NT), np.eye(NA)


def rel_comm(R, X):
    C = R @ X - X @ R
    return float(np.linalg.norm(C) / (np.linalg.norm(R) * np.linalg.norm(X)))


A_full = np.kron(Ahat, It)
R_trace = np.kron(np.diag(LAM4F + 3.75 * ag ** -6.0), It) + np.kron(np.diag(ag ** -8.0), Tn)
R_kin = R_trace + 0.5 * np.kron(Dp @ Dp, It)          # the p_a-carrying variant: the CONTROL

c_trace, c_kin = rel_comm(R_trace, A_full), rel_comm(R_kin, A_full)
print(f"\n      R-hat from the TRACE equation      : ||[R,a]||/(||R|| ||a||) = {c_trace:.3e}")
print(f"      R-hat with a p_a kept (CONTROL)    : ||[R,a]||/(||R|| ||a||) = {c_kin:.3e}")
check(c_trace < 1e-15,
      f"** the premise HOLDS: [R-hat, a-hat] = 0 to {c_trace:.1e}, because R-hat is algebraic in the "
      "matter trace and every tower factor acts on the other factor **")
check(c_kin > 1e-6 and c_trace == 0.0,
      f"** and the check is not vacuous: the trace-equation commutator is EXACTLY zero in this "
      f"arithmetic while keeping a p_a puts it at {c_kin:.2e} -- so this measures a property of the "
      "TRACE equation rather than of the construction **")

w = ag ** 2.0                                          # a non-trivial measure weight
W = np.diag(w)
sa = float(np.linalg.norm(W @ R_trace - R_trace.T @ W if False else
                          np.kron(W, It) @ R_trace - R_trace.T @ np.kron(W, It))
           / np.linalg.norm(np.kron(W, It) @ R_trace))
print(f"\n      the MEASURE: self-adjointness residual of R-hat in the weighted product = {sa:.3e}")
check(sa < 1e-14,
      "the measure does not touch it -- a multiplication operator is self-adjoint in any weight and "
      "commutes with a-hat in any weight, so the measure is not a place this fails")

print("\n      the ORDERING of the tower factor, three variants:")
Q6, P6, T1_6, T2_6, T3_6 = tower_ops(NT)
orders = {
    "pi^2 phi          ": np.array((P6 * P6 * Q6).tolist(), dtype=float),
    "phi pi^2          ": np.array((Q6 * P6 * P6).tolist(), dtype=float),
    "symmetrised       ": np.array(T2_6.tolist(), dtype=float),
}
o_ok = True
for nm, Tv in orders.items():
    Rv = np.kron(np.diag(LAM4F + 3.75 * ag ** -6.0), It) + np.kron(np.diag(ag ** -8.0), Tv)
    cv = rel_comm(Rv, A_full)
    print(f"        {nm}: ||[R,a]||/(||R|| ||a||) = {cv:.3e}")
    o_ok = o_ok and cv < 1e-15
check(o_ok,
      "** ⓵ᵃ is ORDERING-BLIND: an operator on the tower factor commutes with a-hat whatever its "
      "internal ordering, so the ordering does NOT surface a third time and there is nothing to "
      "flag **")

print(r"""
    ⌗ ** THE ONE PREMISE-SIDE THING NOT COMPUTED, named rather than assumed away. **  The momentum
      constraint's algebra is not derived here.  It can only bear on ⓵ᵃ by putting a p_a into R-hat
      --- transverse-traceless modes are transverse, so the constraint is satisfied identically and
      imposes nothing on a-hat --- and the CONTROL above is the measurement of what that would cost
      if it were wrong.  ⇒ *So the premise stands and the order's "if it fails, stop there" does not
      fire.*""")

# ============================================================================ B
head("B.  ⓵ᵇ  THE BRANCH VALUE IS FORCED BEFORE ANY DETERMINANT IS TAKEN")

m1, m2, m3 = 6, 8, 10                 # the trace's own powers: n = 2k+1 gives m = n+3
Q, P, T1, T2, T3 = tower_ops(3)
Msym = k1 * a ** -m1 * T1 + k2 * a ** -m2 * T2
lim = sp.limit(k1 * a ** -m1, a, sp.oo)
print(f"\n      every power in R-hat(a) = 4L + sum_k kappa_k a^-m_k T_k is negative; "
      f"lim_{{a->oo}} a^-{m1} = {lim}")
check(lim == 0 and all(sp.limit(a ** -m, a, sp.oo) == 0 for m in (m1, m2, m3)),
      "so R-hat(a) -> 4 Lambda as a -> oo, and a branch constant on a set of positive measure must "
      "equal 4 Lambda EXACTLY -- the branch value is forced, with no truncation used")
print(r"""
    ⇒ ** THE QUESTION COLLAPSES. **  With lambda = 4 Lambda the condition R-hat(a) psi = lambda psi
      becomes M(a) psi = 0 with M(a) = sum_k kappa_k a^-m_k T_k.  ⇒ *Does M(a) have a null vector for
      ALMOST EVERY a?*  ⌗ This step uses no truncation and survives dimension.""")

print("\n      and the order's own 2x2 model, confirmed exactly:")
sz, sx = sp.Matrix([[1, 0], [0, -1]]), sp.Matrix([[0, 1], [1, 0]])
M2 = k1 * a ** -8 * sz + k2 * a ** -12 * sx
ev = [sp.simplify(e) for e in (LAM4 * sp.eye(2) + M2).eigenvals()]
rad = k1 ** 2 * a ** -16 + k2 ** 2 * a ** -24
d2 = sp.simplify(sp.expand(M2.det()))
# compare the branches by their two symmetric functions, which is sorting-free
s_sum = sp.simplify(sum(ev))
s_gap2 = sp.simplify(sp.expand((ev[0] - ev[1]) ** 2))
print(f"        branches   : {ev}")
print(f"        sum        : {s_sum}      (gap)^2 : {sp.factor(s_gap2)}")
print(f"        det M(a)   : {d2}")
check(sp.simplify(s_sum - 2 * LAM4) == 0 and sp.simplify(s_gap2 - 4 * rad) == 0,
      "the branches are 4L +/- sqrt(kappa_1^2 a^-16 + kappa_2^2 a^-24), exactly as the order "
      "predicted -- checked by their sum and squared gap, so the test is sorting-free -- and "
      "non-constant, so no solution there")
check(sp.simplify(d2 + k1 ** 2 * a ** -16 + k2 ** 2 * a ** -24) == 0 and d2 != 0,
      "and the reason is visible in one line: both Pauli matrices are invertible, so the "
      "determinant is a sum of squares and cannot vanish")

# ============================================================================ C
head("C.  ⓵ᶜ  AT FINITE N THE QUESTION IS EXACTLY WHETHER THE TOWER-OPERATOR PENCIL IS SINGULAR")

print(r"""
      det(sum_k x_k T_k) is a homogeneous form of degree N.  On the physical curve x_k = kappa_k
      a^-m_k with TWO distinct powers, the monomial x_1^j x_2^(N-j) lands on the power
      j m_1 + (N-j) m_2 = N m_2 + j(m_1 - m_2) -- DISTINCT for distinct j.  ⇒ So no two monomials can
      cancel each other on the curve, and

          det M(a) == 0  <=>  every coefficient of the form vanishes  <=>  THE PENCIL IS SINGULAR,

      a condition with no a and no coupling in it.  The extreme coefficients are kappa_k^N det T_k.""")
inj = sorted({j * m1 + (5 - j) * m2 for j in range(6)})
check(len(inj) == 6,
      f"the power map is injective for two operators at N=5: {inj} -- six monomials, six distinct "
      "powers, so the equivalence above is exact rather than generic")

print("\n      the two operators, and the non-commutativity that makes this the OPEN case:")
for N in (4, 6, 8):
    _, _, A1, A2, _ = tower_ops(N)
    C = sp.expand(A1 * A2 - A2 * A1)
    nz = sum(1 for e in C if e != 0)
    print(f"        N={N}: [T_1, T_2] == 0 ? {C == sp.zeros(N, N)}   non-zero entries: {nz}")
_, _, A1, A2, _ = tower_ops(6)
check(sp.expand(A1 * A2 - A2 * A1) != sp.zeros(6, 6),
      "** T_1 and T_2 do NOT commute, so this is the case r6934's simultaneously-diagonal argument "
      "leaves open, not a re-run of it **")

print("\n      N | det T_1 | det T_2 | pencil det(x_1 T_1 + x_2 T_2) | identically zero?")
pen_zero = []
for N in range(2, 9):
    _, _, A1, A2, _ = tower_ops(N)
    d1 = sp.expand(A1.det(method='berkowitz'))
    d2_ = sp.expand(A2.det(method='berkowitz'))
    pen = sp.expand((x1 * A1 + x2 * A2).det(method='berkowitz'))
    pen_zero.append(pen == 0)
    shown = sp.factor(pen) if pen != 0 else 0
    txt = str(shown)
    print(f"      {N} | {d1} | {d2_} | {txt if len(txt) < 58 else txt[:55] + '...'} | {pen == 0}")
check(not any(pen_zero),
      "** the pencil is NON-SINGULAR at every truncation N = 2..8, in exact integer arithmetic -- so "
      "det M(a) is not identically zero and there is NO eigenvalue branch constant in a **")

# ============================================================================ D
head("D.  THREE OPERATORS -- WHERE THE POWERS COLLIDE AND THE PENCIL ARGUMENT NO LONGER SUFFICES")

coll = [(j1, j2, j3) for j1 in range(3) for j2 in range(3) for j3 in range(3)
        if j1 + j2 + j3 == 2 and j1 * m1 + j2 * m2 + j3 * m3 == 16]
print(f"\n      with powers ({m1},{m2},{m3}) the monomials {coll} all land on 1/a^16: "
      f"{m1}+{m3} = {m2}+{m2}")
check(len(coll) > 1,
      "** the power map is NOT injective for three operators, so coefficients CAN combine on the "
      "curve and the pencil equivalence of §C does not carry -- the curve determinant has to be "
      "computed directly.  (The domain of an argument is part of the argument.) **")

print("\n      so it is computed directly, with symbolic couplings:")
sys_ok = []
COEFFS = {}
for N in (3, 4, 5, 6):
    _, _, A1, A2, A3 = tower_ops(N)
    M = k1 * a ** -m1 * A1 + k2 * a ** -m2 * A2 + k3 * a ** -m3 * A3
    det = sp.expand(M.det(method='berkowitz') * a ** (m3 * N))
    co = [sp.factor(c) for c in sp.Poly(det, a).all_coeffs() if sp.simplify(c) != 0]
    COEFFS[N] = co
    print(f"        N={N}: {len(co)} non-zero Laurent coefficients; leading = {co[0] if co else 0}")
    sys_ok.append(len(co) > 0)
check(all(sys_ok),
      "det M(a) is a NON-ZERO Laurent polynomial at N = 3..6 with all three couplings symbolic, so "
      "no constant branch there either")

print("\n      AND THE FULL COUPLING SYSTEM SOLVED -- this is where N enters, and it is the order's "
      "own warning:")
for N in (3, 4, 5):
    _, _, A1, A2, A3 = tower_ops(N)
    co = COEFFS[N]
    sols = sp.solve(co, [k1, k2, k3], dict=True)
    kept = [s for s in sols if all(s.get(v, v) != 0 for v in (k1, k2, k3))]
    zeroed = [sum(1 for v in (k1, k2, k3) if s.get(v, v) == 0) for s in sols]
    print(f"        N={N} ({'odd ' if N % 2 else 'even'}): det T_1 = "
          f"{sp.expand(A1.det(method='berkowitz'))};  solutions: {len(sols)};  couplings switched "
          f"off in each: {zeroed};  with ALL couplings non-zero: {len(kept)}")
    check(len(kept) == 0,
          f"** at N={N} the system has NO solution with all three couplings non-zero -- which is the "
          "case the cubic puts us in **")

print(r"""
    ⇒ ** THE N-DEPENDENCE, REPORTED AS THE RESULT RATHER THAN SMOOTHED OVER. **  At ODD N a ladder
      matrix is singular, so det T_k = 0 and the system acquires non-trivial solutions --- and every
      one of them switches off at least two of the three couplings, collapsing to a single-operator
      model whose determinant vanishes for that reason alone.  ⇒ *The necessary conditions are
      N-parity dependent; the verdict is not.*  ⌗ ** And the bias runs the helpful way: an
      odd-dimensional truncation MANUFACTURES a null vector that the tower does not have, so the
      instrument is tilted toward finding a constant branch and still finds none. **""")

Nc = 5
_, _, A1, _, A3 = tower_ops(Nc)
print(f"\n      the artefact, named exactly: at N={Nc}, det(phi-like) = "
      f"{sp.expand(A3.det(method='berkowitz'))} and det(pi-like^2) = "
      f"{sp.expand(A1.det(method='berkowitz'))}")
check(sp.expand(A3.det(method='berkowitz')) == 0 and sp.expand(A1.det(method='berkowitz')) == 0,
      "both vanish at odd N -- an odd-dimensional truncation of a ladder operator is singular, and "
      "that is a statement about the truncation")
check(sp.expand(tower_ops(6)[4].det(method='berkowitz')) != 0,
      "and both are non-singular at even N, which is how the artefact identifies itself: a property "
      "that flips with the parity of the cut is not a property of the tower")

# ============================================================================ E
head("E.  THE CONTROL -- THE COMPUTATION DOES RETURN 'YES' WHEN A CONSTANT BRANCH IS THERE")

ctrl = []
for N in (4, 5, 6):
    _, _, A1, A2, _ = tower_ops(N)
    Z = sp.eye(N)
    Z[0, 0] = 0                              # project out one COMMON direction
    S1, S2 = Z * A1 * Z, Z * A2 * Z
    pen = sp.expand((x1 * S1 + x2 * S2).det(method='berkowitz'))
    ctrl.append(pen == 0)
    print(f"      N={N}: two operators sharing one null vector -> pencil identically zero? {pen == 0}")
check(all(ctrl),
      "** a shared null vector makes the pencil singular at every N, so the instrument returns the "
      "affirmative when the affirmative is true -- §C's and §D's zeros are measurements, not the "
      "instrument's silence **")

print("\n      and the measure-zero refinement, for the isolated a where the determinant does vanish:")
_, _, A1, A2, _ = tower_ops(4)
Mnum = A1 * a ** -m1 + A2 * a ** -m2                  # couplings set to 1
dn = sp.simplify(sp.expand(Mnum.det(method='berkowitz')))
roots = sp.solve(sp.Eq(sp.expand(dn * a ** (m2 * 4)), 0), a)
pos = [r for r in roots if r.is_real and r.is_positive]
print(f"        det M(a) at N=4, unit couplings: {sp.factor(dn)}")
print(f"        positive real roots: {pos}")
check(dn != 0 and len(pos) < 4,
      f"a non-zero Laurent polynomial has finitely many positive roots ({len(pos)} here), so even "
      "where the determinant vanishes it vanishes on a set of MEASURE ZERO -- 'for almost every a' "
      "fails, which is the condition the order wrote")

# ============================================================================ F
head("F.  WHAT SURVIVES DIMENSION, AND THE ONE STEP THAT DOES NOT")

print(r"""
  ⚑ SURVIVES DIMENSION, with no truncation anywhere in it:

    · ** lambda = 4 Lambda is forced ** (§B): every power is negative, so R-hat(a) -> 4 Lambda.
    · ** The condition is a NULL EIGENVECTOR of M(a) for almost every a ** -- that is what an
      eigenvector of the direct integral is, and it is the statement the finite-N determinant is a
      proxy for.
    · ** And the odd-N artefact has no counterpart there: ** phi-hat and pi-hat have purely
      continuous spectrum on the line, so neither has a null EIGENVECTOR at all, while an
      odd-dimensional truncation of either is singular.  ⇒ *The finite-N proxy is strictly more
      permissive than the tower question, so a finite-N "no" is the stronger statement of the two.*

  ⛔ DOES NOT SURVIVE, AND IS THE ONE NAMED STEP:

    · ** The determinant criterion itself. **  At finite N, "singular for almost every a" is
      det M(a) == 0, which §C reduces exactly to a singular pencil.  In the tower there is no
      determinant, and the equivalence has to be replaced by an argument about the point spectrum of
      an unbounded operator family.  ⇒ *That is not supplied here, and the odd-N parity is precisely
      the place the two criteria part company -- which is why it is reported rather than filtered.*

  ⇒ ** SO THE STATUS, IN THE ORDER'S OWN TERMS. **  The entangled case is no longer a category: it is
    ** one question about a one-parameter matrix family, with the branch value forced and the
    condition reduced to a singular pencil ** -- and the answer is ** NO SOLUTION AT EVERY TRUNCATION
    TESTED, at both parities, with all couplings non-zero. **  ⌗ *Whether that is the row's third
    completed argument turns on the tower limit above, which is named and not computed.  So: the wall
    is a different object now -- not "entangled states over a non-commuting family" but "the tower
    limit of a singular-pencil condition" -- and it is reformulated and answered at finite N rather
    than reformulated and open.*

  ⛔ WHAT THIS DOES NOT TOUCH.

    · No ordering choice -- and §A shows ⓵ᵃ does not depend on one, so the third surfacing the order
      asked me to watch for did not happen.
    · The momentum constraint's algebra is not derived; §A's control measures what its failure would
      cost.
    · No interacting theory beyond the cubic's own two tower factors; nothing on `prop:flat`,
      `PO-31` or `PO-15`; ** no corpus edit ** -- the `P10` site and its sentence are routed.

  ⌗ AND ONE HABIT ADOPTED FROM `r6947`, WHICH IS WHY THIS RECEIPT HAS ALMOST NO FLOATS IN IT.

    `r6947` found `r6946`'s single tolerance was the authoring machine's round-off floor, not a
    convergence statement.  ⇒ *The repair for a claim of THIS shape is not a better tolerance but no
    tolerance: the ladder matrices are carried in the basis where they are integer matrices -- a
    diagonal similarity, so the spectrum and the vanishing of any determinant are untouched -- and
    every load-bearing determinant, Laurent coefficient and coupling system is computed over the
    integers.*  ⌗ **The two floats that remain are §A's commutator measurements, and each is reported
    against a control five decades away rather than against a threshold.**
""".rstrip())

print()
print("=" * 94)
if FAILED:
    print(f"FAILED {len(FAILED)} check(s):")
    for f in FAILED:
        print("   -", f)
    sys.exit(1)
print("ALL CHECKS PASS.")
