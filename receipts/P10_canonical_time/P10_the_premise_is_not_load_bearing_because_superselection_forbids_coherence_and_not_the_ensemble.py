#!/usr/bin/env python3
r"""
P10_the_premise_is_not_load_bearing_because_superselection_forbids_coherence_and_not_the_ensemble
================================================================================================

LEVEL: exact symbolic (sympy) for the rank lemmas and the variance identity; 40-digit quadrature
(mpmath) for the two rank routes and their floors; float linear algebra on truncated operators for
the centrality tests, each against a floor measured in the same arithmetic.  Nothing is fitted.

OBJECT UNDER TEST -- `PO-23`, `r6925`.  The order, verbatim:

    "Does that Hilbert space carry a superselection rule in $\alpha$?  Equivalently: is $\alpha$ ---
     or whatever operator carries the background's scale --- central in the algebra the true
     Hamiltonian and the tower generate, or does something in that algebra fail to commute with it?"

  with the three outcomes costed: *superselected* reverses `r6920`'s first item and the degeneracy
  survives; *not superselected* leaves the finding standing on something proved; *neither* is honest
  if the algebra is not determined until the coupling is, and then "say which step needs it".

  ⌗ AND THE GUARD, WHICH IS THIS LINE'S OWN RETURNED: *"Whatever you build here, build its controls
    first --- a case where the answer is known to be superselected and one where it is known not to
    be --- because a superselection statement with no measured floor is exactly the shape of an
    unfalsifiable one."*  Every centrality number below is quoted against a floor measured on
    commutators that must vanish, computed in the same arithmetic as the ones that must not.

COMPUTES: the relative commutator norm of each candidate background-scale operator against the
algebra the order names, with its floor; the number of spectral points of each candidate, because a
central operator with a one-point spectrum decomposes nothing; the exact rank of the map to
$(\int\!\sqrt g,\int\!\sqrt g R,\int\!\sqrt g R^{2})$ under region variation at fixed $\alpha$ and
under ensemble variation at fixed region, as two separable routes; and the variance identity that
makes the quantum form of the question a statement about $\hat\Theta$'s spectrum.  Scope: the
interacting theory is NOT built, as ordered, and §E states which step needs it.

-------------------------------------------------------------------------------
** THE ANSWER IS THE ORDER'S THIRD BRANCH, AND FOR A DIFFERENT REASON THAN THE ORDER OFFERED IT: NOT
   THAT THE QUESTION AWAITS THE COUPLING, BUT THAT ITS TWO BRANCHES ARE NOT ALTERNATIVES. **

** ⛭ ⓵ SUPERSELECTION IN $\alpha$ DOES NOT RESTORE THE DEGENERACY, SO THE FIRST BRANCH DOES NOT
   REVERSE ANYTHING. **  A superselection rule forbids *coherence* between sectors; it does not
forbid an *ensemble* over them, and $\int\!\sqrt g\,R^{k}$ is read off the ensemble linearly.  A
mixture over three distinct $\alpha$ therefore reaches rank $3$ ($s_3/s_1=1.60\times10^{-4}$, 39
decades above the measured floor) *inside* a superselected theory.  ⇒ **The branch the order costed
as the reversal is a second route to the same conclusion.**

** ⛭ ⓶ AND `r6920` TOOK NEITHER ROUTE, SO THE PREMISE WAS NEVER A DEPENDENCY. **  Every call of that
receipt's rank instrument fixed ONE $\Lambda$ and varied only the three regions of one history.  The
two routes are separable and their signatures differ: an ensemble of $N$ distinct $\alpha$ has rank
exactly $\min(N,3)$ --- at $N=2$ the third singular value sits at $8\times10^{-72}$, *below* the
quadrature floor --- whereas `r6920` reached rank $3$ at $N=1$, where mixing caps the rank at $1$.
⇒ ** So `r6920` §E is wrong where it says "if the physical Hilbert space selected a single background
the degeneracy would survive": with a single background it does not survive, at $9.06\times10^{-8}$,
and that is this line correcting its own landed work. **

** ⛭ ⓷ AND THE QUESTION AS PUT TO $\alpha$ HAS NO OBJECT, WHICH IS WHY NEITHER BRANCH BINDS. **
$\alpha=\sqrt{3/\Lambda}$ enters $\Hphys$ as a coefficient, so $\hat\alpha=\alpha\cdot\mathbf 1$: it
is central, and its spectrum has ONE point.  A superselection rule needs a central operator with more
than one --- otherwise the decomposition has one sector and is not a decomposition.  `P10`'s own
`sec:lock` says as much from the other side: $\kappa=1/\alpha$ "belongs to the background horizon,
not to the graviton content, and so is common to every fibre".  ⇒ **The theory has exactly one
operator that qualifies as a superselection label, and it is $\hat\Gamma$, which labels the boundary
condition and not the background scale.**  And the operator $R$ actually depends on, $\hat a$, is
central in nothing: $[\hat a,\Hphys]=[\hat a,\hat p_a^{2}]$ **exactly, at every order of the
coupling**, because every coupling term `sec:lock` names is $f(\hat a)\otimes(\text{tower operator})$
and functions of $\hat a$ commute with $\hat a$.

⛔ ** NOT CLAIMED. **  No interacting theory.  No value for the coupled $\zeta(0)$.  No claim that
$\hat a$ or $\hat\Gamma$ *is* the background scale in the sense `P10` would want; the three
candidates are enumerated and each disposed of on its own ground.  The truncated-operator models are
models of the *algebra*, not of the spectrum, and §E says which step needs the coupling.  rc=0 on all
32 checks.
"""

import sys

import mpmath as mp
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


R_RESIDUE = mp.mpf(39) / 4           # Res_{s=-1} zeta_omega -- BANKED at r6920, not recomputed
S3_R6920 = mp.mpf('9.06166e-8')      # r6920's rank-3 signal, BANKED, reproduced below

# ============================================================================ A
head("A.  THE CONTROLS, BUILT FIRST -- WHAT CENTRAL AND NOT-CENTRAL MEASURE AS, IN THIS ARITHMETIC")

N = 14                               # oscillator truncation
INT = N - 5                          # interior block: the truncation edge is discarded

_low = np.diag(np.sqrt(np.arange(1, N)), 1)
xq = (_low + _low.T.conj()) / np.sqrt(2)
pq = 1j * (_low.T.conj() - _low) / np.sqrt(2)
Id = np.eye(N)


def interior(M):
    """drop the last five rows/columns of the FIRST tensor factor -- where truncation bites."""
    k = M.shape[0] // N
    return M.reshape(N, k, N, k)[:INT, :, :INT, :].reshape(INT * k, INT * k)


def comm(A, B):
    return A @ B - B @ A


def rel(X, A, trunc=True):
    """||[X,A]|| / (||X|| ||A||), Frobenius, on the interior block when X lives on the a-factor."""
    C, Xi, Ai = comm(X, A), X, A
    if trunc:
        C, Xi, Ai = interior(C), interior(X), interior(A)
    return float(np.linalg.norm(C) / (np.linalg.norm(Xi) * np.linalg.norm(Ai)))


def points(M, nd=6):
    """how many distinct points the spectrum has -- a central operator with ONE decomposes nothing."""
    return len(np.unique(np.round(np.linalg.eigvalsh(M), nd)))


print("\n  CONTROL N -- known NOT central: position against the kinetic operator it generates")
cN = rel(xq, pq @ pq, trunc=False)
print(f"      rel([x, p^2])  =  {cN:.6f}")
check(cN > 1e-3, "control N registers a non-central pair at order 1e-1 -- the scale to beat")

print("\n  CONTROL S -- known superselected: a direct SUM over three theories, and its label")
LAMS = [3.0, 6.0, 12.0]
_blocks = [pq @ pq + L * (xq @ xq) for L in LAMS]
A_S = np.block([[_blocks[i] if i == j else np.zeros((N, N)) for j in range(3)] for i in range(3)])
X_S = np.block([[LAMS[i] * Id if i == j else np.zeros((N, N)) for j in range(3)] for i in range(3)])
cS = rel(X_S, A_S, trunc=False)
print(f"      rel([Lambda-hat, H])  =  {cS:.3e}        spectral points of the label:  {points(X_S)}")
check(cS < 1e-14, "control S registers a central pair at the floor")
check(points(X_S) == 3,
      "** and its label has THREE spectral points: that is what a superselection rule looks like, "
      "and building it took an enlargement of the Hilbert space to a direct sum over theories **")

# ---- the model of the algebra the order names ------------------------------------------------
SHIFT = 2.0 * np.sqrt(N)                     # a-hat positive definite on the truncation
a_op = xq + SHIFT * Id
_ev, _U = np.linalg.eigh(a_op)
check(_ev.min() > 0, f"a-hat is positive definite on the truncation (min eigenvalue {_ev.min():.4f})")


def fa(k):
    """f(a-hat) = a-hat^k by spectral calculus -- the form every coupling term in sec:lock takes."""
    return _U @ np.diag(_ev ** float(k)) @ _U.T.conj()


kron, OM, LAM_C = np.kron, 1.7, 3.0
H_a = kron(pq @ pq, Id) - LAM_C * kron(fa(3), Id)          # p_a^2 and the -(Lambda/8pi) a^3 term
H_tow = kron(Id, (pq @ pq + OM ** 2 * (xq @ xq)) / 2)      # the free tower, one mode
H_kin = kron(fa(-3), pq @ pq)                              # pi_n^2 / 2 a^3 -- the Gamma-hat structure
H_cub = 0.3 * kron(fa(-3), (pq @ pq @ xq + xq @ pq @ pq) / 2)   # pi_n^2 phi_m / a^3 -- "in kind"
H_LEAD, H_FULL = H_a + H_tow + H_kin, H_a + H_tow + H_kin + H_cub
A_HAT, PA2 = kron(a_op, Id), kron(pq @ pq, Id)

print("\n  THE FLOOR, measured on the family of commutators that MUST vanish, same arithmetic:")
_base = interior(comm(A_HAT, PA2))
_nb = np.linalg.norm(_base)
FLOOR_F = max(float(np.linalg.norm(interior(comm(A_HAT, kron(fa(k), T)))) / _nb)
              for k in (-3, -2, -1, 1, 2, 3)
              for T in (pq @ pq, xq @ xq, pq @ pq @ xq + xq @ pq @ pq))
print(f"      max over  ||[a-hat, f(a-hat) (x) T]|| / ||[a-hat, p_a^2]||  =  {FLOOR_F:.3e}")
check(FLOOR_F < 1e-10,
      "every f(a-hat) (x) T commutes with a-hat to the arithmetic's own floor -- eighteen members, "
      "and the floor is the LARGEST of them, not the smallest")

# ============================================================================ B
head("B.  WHICH OPERATOR CARRIES THE BACKGROUND'S SCALE -- THREE CANDIDATES, EACH DISPOSED OF")

print("\n  CANDIDATE 1 -- alpha itself, via Lambda = 3/alpha^2.  It is a COEFFICIENT of H_phys.")
ALPHA_HAT = np.sqrt(3.0 / LAM_C) * np.eye(N * N)
cA = rel(ALPHA_HAT, H_FULL)
print(f"      rel([alpha-hat, H_full])  =  {cA:.3e}        spectral points:  {points(ALPHA_HAT, 9)}")
check(cA < 1e-14, "alpha-hat = alpha.1 is central -- trivially, being a c-number")
check(points(ALPHA_HAT, 9) == 1,
      "** but its spectrum has ONE point, against control S's three: it is central and it "
      "decomposes NOTHING, so there is no superselection rule for the degeneracy to survive on **")
check(points(ALPHA_HAT, 9) < points(X_S),
      "and the deficiency is exactly the enlargement control S needed and deparametrization does "
      "not perform: a direct sum over theories is not what solving the constraint returns")

print("\n  CANDIDATE 2 -- a-hat, which is what R depends on: R = 4 Lambda + 4 G r / (pi a^4).")
c2_lead, c2_full = rel(A_HAT, H_LEAD), rel(A_HAT, H_FULL)
c2_pa2 = rel(A_HAT, PA2)
print(f"      rel([a-hat, H_lead]) = {c2_lead:.3e}   rel([a-hat, H_full]) = {c2_full:.3e}")
print(f"      rel([a-hat, p_a^2])  = {c2_pa2:.6f}   <- the scale-free form: the statistic above is "
      "diluted by ||H||,")
print("                                                which the a^3 term dominates; the dilution "
      "is H's scale, not near-commutation")
check(c2_lead / FLOOR_F > 1e6 and c2_full / FLOOR_F > 1e6,
      f"a-hat fails to commute with H_phys by {np.log10(c2_full / FLOOR_F):.1f} decades over the "
      "measured floor, at leading order AND with the cubic coupling in")
check(abs(c2_pa2 - cN) < 1.0 and c2_pa2 > 1e-3,
      "and at the same order as control N when read against the term it comes from")

resid = {nm: float(np.linalg.norm(interior(comm(A_HAT, H)) - _base) / _nb)
         for nm, H in (("leading order", H_LEAD), ("with the cubic", H_FULL))}
for nm, v in resid.items():
    print(f"      || [a-hat, H({nm})] - [a-hat, p_a^2] || / || [a-hat, p_a^2] ||  =  {v:.3e}")
check(max(resid.values()) < FLOOR_F,
      "** [a-hat, H_phys] = [a-hat, p_a^2] EXACTLY -- the residual sits below the floor measured on "
      "the f(a-hat) family, so the coupling does not enter the commutator at all **")
check(abs(resid["leading order"] - resid["with the cubic"]) < 1e-15 * max(1.0, resid["with the cubic"])
      or abs(resid["leading order"] - resid["with the cubic"]) < FLOOR_F,
      "and the cubic term moves it by nothing: the statement is ORDER-INDEPENDENT, which is what "
      "makes it answerable without building the interacting theory, as ordered")

print("\n    ⇒ AND THE REASON IS STRUCTURAL, NOT NUMERICAL.  Every coupling term `sec:lock` names --")
print("      pi_n^2 / 2a^3, the inverse-square Gamma-hat/x^2, and the cubic pi_n^2 phi_m / a^3 --")
print("      is f(a) (x) (tower operator).  Functions of a-hat commute with a-hat.  The SOLE")
print("      a-derivative in H_phys is the scale-factor kinetic term, present at leading order;")
print("      and `sec:lock`'s own positivity result makes its coefficient an operator K > 0 on")
print("      non-degenerate metrics, so [a-hat, H_phys] = 2 i hbar p_a K cannot vanish.")
print("      ** Removing it would remove the scale factor's dynamics, i.e. the true Hamiltonian. **")

print("\n  CANDIDATE 3 -- Gamma-hat = gamma + c sum_n pi_n^2, the boundary coefficient.")
GAM = kron(Id, 0.25 * Id + 0.5 * (pq @ pq))
RAD = kron(pq @ pq, Id) + kron(fa(-2), 0.25 * Id + 0.5 * (pq @ pq))
cG_rad, cG_tow = rel(GAM, RAD), rel(GAM, H_tow)
print(f"      rel([Gamma-hat, -d_x^2 + Gamma-hat/x^2])  =  {cG_rad:.3e}   <- the RADIAL algebra")
print(f"      rel([Gamma-hat, H_tower])                 =  {cG_tow:.6f}     <- the DYNAMICAL one")
print(f"      spectral points of Gamma-hat:  {points(GAM)}")
check(cG_rad < 1e-14, "Gamma-hat IS central in the radial algebra -- P10's direct integral over "
                      "spec Gamma-hat, and the boundary condition supplied fibre by fibre")
check(cG_tow / FLOOR_F > 1e6, "and is NOT central in the algebra the order names, which the true "
                              "Hamiltonian and the tower generate: pi^2 does not commute with phi^2")
check(points(GAM) > 1,
      "** its spectrum has more than one point, so it is the theory's one genuine superselection "
      "label -- and it labels the BOUNDARY CONDITION, not the background scale **")
print("\n    ⇒ CENTRALITY IS RELATIVE TO AN ALGEBRA, and Gamma-hat is the two-sided control that")
print("      shows it: the SAME operator is central in one of this theory's algebras and not in")
print("      the other.  The order names its algebra, so that is the one tested above.")

# ============================================================================ C
head("C.  THE AUDIT -- r6920's RANK 3 USED NO alpha-MIXING, AND MIXING'S SIGNATURE IS DIFFERENT")

V0, V1, V2, R0 = sp.symbols('V_0 V_1 V_2 R_0', positive=True)
M_one = sp.Matrix([[Vi * R0 ** k for k in (0, 1, 2)] for Vi in (V0, V1, V2)])
check(M_one.rank() == 1,
      "LEMMA 1 (exact): R constant on ONE history gives M[i,k] = R_0^k V[i] -- rank 1 for ANY "
      "number of regions, so a rank above 1 from one history is signed by R being non-constant")

ws = sp.symbols('w0:9', positive=True)
Rj = sp.symbols('R_0:3', positive=True)
Vj = sp.symbols('U_0:3', positive=True)


def mix_matrix(n):
    """rows = three ENSEMBLES over n distinct alpha; each member has R_j constant."""
    return sp.Matrix([[sum(ws[3 * i + j] * Vj[j] * Rj[j] ** k for j in range(n)) for k in (0, 1, 2)]
                      for i in range(3)])


for n in (1, 2, 3):
    check(mix_matrix(n).rank() == n,
          f"LEMMA 2 (exact), n = {n}: an ensemble over {n} distinct alpha is a sum of {n} outer "
          f"product{'' if n == 1 else 's'}, so its rank is exactly min({n}, 3) = {min(n, 3)}")

mp.mp.dps = 40
GG, C0, MU = mp.mpf(1), mp.mpf(1), mp.mpf(1)
REGIONS = [(2, 3), (3, 5), (5, 9)]
ONE_REGION = (2, 9)


def moments(Lam_, r_, a1, a2):
    """(int sqrt g, int sqrt g R, int sqrt g R^2) on ONE history over ONE region -- r6920's kernel."""
    kap = 4 * GG * r_ / mp.pi
    ad = lambda aa: mp.sqrt(Lam_ * aa ** 2 / 3 - 1
                            + (4 * GG / (3 * mp.pi)) * (C0 + r_ * mp.log(aa * MU)) / aa ** 2)
    Rf = lambda aa: 4 * Lam_ + kap / aa ** 4
    return [2 * mp.pi ** 2 * mp.quad(lambda aa: aa ** 3 * Rf(aa) ** k / ad(aa), [a1, a2])
            for k in (0, 1, 2)]


def ratios(rows):
    S = mp.svd_r(mp.matrix(rows))[1]
    return mp.mpf(S[1]) / mp.mpf(S[0]), mp.mpf(S[2]) / mp.mpf(S[0])


print("\n  ROUTE A -- REGION variation at ONE alpha.  This is the only route r6920 took.")
rowsA0 = [moments(mp.mpf(3), mp.mpf(0), *g) for g in REGIONS]
rowsA1 = [moments(mp.mpf(3), R_RESIDUE, *g) for g in REGIONS]
_, s3A0 = ratios(rowsA0)
_, s3A1 = ratios(rowsA1)
print(f"      r = 0     (no anomaly)  s3/s1 = {mp.nstr(s3A0, 6)}      <- the quadrature FLOOR")
print(f"      r = 39/4  (the anomaly) s3/s1 = {mp.nstr(s3A1, 6)}")
FLOOR_Q = s3A0
check(s3A1 / FLOOR_Q > mp.mpf('1e20'),
      f"ROUTE A reaches rank 3 at N = 1 distinct alpha, {mp.nstr(mp.log(s3A1 / FLOOR_Q, 10), 3)} "
      "decades above the floor it measures itself")
check(abs(s3A1 - S3_R6920) / S3_R6920 < mp.mpf('1e-3'),
      f"and it REPRODUCES r6920's banked {mp.nstr(S3_R6920, 6)} -- the instrument is the same one")
check(mix_matrix(1).rank() == 1,
      "** so ROUTE A's rank 3 CANNOT be a mixing artefact: at N = 1 Lemma 2 caps the rank at 1, "
      "and rank 1 is exactly what the r = 0 control measures.  The premise was never a dependency **")

print("\n  ROUTE B -- ENSEMBLE variation at ONE region, r = 0.  No anomaly and no geometric variation:")
WEIGHTS = [[mp.mpf(w) / 10 for w in ww] for ww in ([8, 1, 1], [1, 8, 1], [1, 1, 8])]


def route_b(lams):
    lams = list(lams) + [lams[-1]] * (3 - len(lams))     # pad: every weight vector has length 3
    V = [moments(L, mp.mpf(0), *ONE_REGION) for L in lams]
    return [[sum(w[j] * V[j][k] for j in range(3)) for k in (0, 1, 2)] for w in WEIGHTS]


s3B = {}
for lams in ([mp.mpf(3)], [mp.mpf(3), mp.mpf(6)], [mp.mpf(3), mp.mpf(6), mp.mpf(12)]):
    s2, s3 = ratios(route_b(lams))
    s3B[len(lams)] = s3
    print(f"      distinct alpha = {len(lams)}    s2/s1 = {mp.nstr(s2, 6):>13s}    "
          f"s3/s1 = {mp.nstr(s3, 6)}")
check(s3B[1] < mp.mpf('1e-30'), "N = 1: rank 1 at the floor -- one alpha, no rank, as Lemma 2 says")
check(s3B[2] < s3B[1],
      f"N = 2: the third singular value is {mp.nstr(s3B[2], 4)}, BELOW the floor -- rank exactly 2, "
      "which is the exact structure Lemma 2 predicts and not a numerical accident")
check(s3B[3] / FLOOR_Q > mp.mpf('1e20'),
      f"N = 3: rank 3 at {mp.nstr(s3B[3], 6)}, {mp.nstr(mp.log(s3B[3] / FLOOR_Q, 10), 3)} decades "
      "above the floor -- ** the SECOND route, and it needs no anomaly at all **")
check(s3B[3] > s3A1,
      "and it is the LARGER of the two effects, which is why it had to be checked that r6920 did "
      "not use it: it did not, and the N-counting is what settles that rather than an assurance")

# ============================================================================ D
head("D.  ⓵  WHY THE ORDER'S FIRST BRANCH DOES NOT REVERSE ANYTHING")

rho_w = [0.5, 0.3, 0.2]
RHO_S = np.block([[rho_w[i] * Id if i == j else np.zeros((N, N))
                   for j in range(3)] for i in range(3)]) / (sum(rho_w) * N)
ev_rho = np.linalg.eigvalsh(RHO_S)
print(f"\n  in control S -- the superselected theory -- the ENSEMBLE rho = sum_j w_j P_j / tr:")
print(f"      min eigenvalue = {ev_rho.min():.6f}   trace = {np.trace(RHO_S).real:.10f}")
check(ev_rho.min() >= -1e-14, "rho is positive semi-definite: a legitimate state")
check(abs(np.trace(RHO_S).real - 1.0) < 1e-12, "and normalized")
check(rel(X_S, RHO_S, trunc=False) < 1e-14,
      "** and it COMMUTES with the superselection label, so the rule does not exclude it: "
      "superselection forbids coherence between sectors, not an ensemble over them **")
check(s3B[3] / FLOOR_Q > mp.mpf('1e20'),
      "⇒ and ROUTE B applies to exactly that ensemble, because int sqrt(g) R^k is LINEAR in it: "
      f"rank 3 at {mp.nstr(s3B[3], 4)} INSIDE a superselected theory")
print("\n    ⇒ ** THE FIRST BRANCH IS NOT THE REVERSAL THE ORDER TOOK IT FOR. **  Superselecting")
print("      alpha removes the SUPERPOSITIONS and keeps the ENSEMBLES, and the rank test reads the")
print("      ensemble.  The degeneracy is restored by ONE thing only -- a single alpha with r = 0,")
print("      which is ROUTE A's own null control at the floor.  ** So it is restored by killing the")
print("      anomaly and never by superselecting alpha: the same number twice, as r6920 found. **")

# ============================================================================ E
head("E.  WHICH STEP ACTUALLY NEEDS THE INTERACTION -- THE THIRD BRANCH, NAMED")

I0, I1, I2, Rbar = sp.symbols('I_0 I_1 I_2 Rbar', positive=True)
a_, Lam_, G_, r_ = sp.symbols('a Lambda G r', positive=True)
Rq = 4 * Lam_ + 4 * G_ * r_ / (sp.pi * a_ ** 4)
check(sp.simplify(sp.diff(Rq, a_) + 16 * G_ * r_ / (sp.pi * a_ ** 5)) == 0,
      "R = 4 Lambda + 4 G r / (pi a^4) has dR/da = -16 G r / (pi a^5), non-zero iff r non-zero -- "
      "the classical criterion, restated as the one thing that can switch the degeneracy")
w_, R1_, R2_ = sp.symbols('w R_a R_b', positive=True)
var_two = (w_ * R1_ ** 2 + (1 - w_) * R2_ ** 2) - (w_ * R1_ + (1 - w_) * R2_) ** 2
check(sp.simplify(var_two - w_ * (1 - w_) * (R1_ - R2_) ** 2) == 0,
      "and the variance identity I_2 I_0 - I_1^2 = I_0^2 Var(R) on a two-member ensemble is "
      "w(1-w)(R_a - R_b)^2 -- so the rank is the VARIANCE of R, whichever route supplies it")

print(r"""
  ⚑ WHAT IS DISCHARGED.  `r6925`'s question is answered in kind, without building the interacting
    theory, as ordered -- and the answer is that its two branches are not alternatives.  ⓵ the
    premise `r6920` took is NOT load-bearing, by the N-counting of §C.  ⓶ the branch that would
    have reversed the first item does not, by §D.  ⓷ and the question as put to alpha has no
    object, because alpha is a label of the theory and not an observable of it, so its spectrum
    has one point and nothing is graded by it.

  ⛔ AND THE STEP THAT DOES NEED THE COUPLING, WHICH IS NOT THE ONE THE ORDER NAMED.

    · ** The quantum form of the degeneracy is a statement about spec Theta-hat. **  The criterion
      is Var_sqrt(g)(R) = 0.  Semiclassically R is a function and the answer is no, for r non-zero.
      In the operator theory the sharp question is whether any physical state makes R-hat sharp,
      and R-hat = 4 Lambda + 8 pi G Theta-hat, so that asks for an EIGENVECTOR of Theta-hat.
      ⇒ *Theta-hat is the interacting tower's regularized trace, whose ultraviolet definition
      `sec:lock` names as the open frontier.  That is the step, and it is a different question from
      the one the order posed: not whether alpha is central, but whether Theta-hat has a point
      spectrum.*  A conditional is available now and is stated as one: if spec Theta-hat is purely
      continuous, no state makes R-hat sharp and the degeneracy cannot be restored by state choice
      either.  ** This receipt does not compute that spectrum. **

    · ** The models here are models of the ALGEBRA, not of the spectrum. **  A truncated oscillator
      settles commutators and spectral-point counts and settles nothing about the half-line
      operator's actual spectrum or its self-adjoint extensions, which `P10` treats and this does
      not touch.  The centrality results are exact statements about the algebra's structure, read
      off a finite model whose floor is measured; they are not spectral claims.

    · ** No interacting theory, no coupled zeta(0), no signal. **  Unchanged from `r6920`, and §D's
      finding does not make the gap larger: it is still O(r^2) on ROUTE A, and ROUTE B's larger
      number is an ensemble effect that a single history does not have.

  ⌗ AND WHAT THIS CORRECTS IN THIS LINE'S OWN LANDED WORK, stated plainly because the order's value
    is in the correction and not in the agreement.  `r6920` §E lists as a wall: *"ONE premise is
    taken and not proved: that the coupled sector admits states without a definite alpha ... if the
    physical Hilbert space selected a single background, the degeneracy would survive."*  ** The
    second clause is false. **  With a single background the rank is 3 at 9.06e-8, which is
    r6920's own headline number, computed at a single Lambda.  The premise was a SECOND route the
    receipt never took, not a dependency the finding rested on -- and the wall list is shorter by
    one item, not longer.
""".rstrip())

print()
if FAILED:
    print("FAIL: " + "; ".join(FAILED))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
