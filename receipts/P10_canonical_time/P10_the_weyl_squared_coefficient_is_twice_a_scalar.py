"""
P10_the_weyl_squared_coefficient_is_twice_a_scalar
===================================================

Object under test -- `PO-43`, "the Weyl-squared coefficient at second order in the
shear", discharged by "that coefficient with the sub-leading heat-kernel
coefficients, which is the instrument P10 names and stopped short of running".

r6413 fixed WHAT the coefficient multiplies: C^2 = 2 sum_i (sigma_i' + H sigma_i)^2.
This is the coefficient.

** THE LOAD-BEARING STEP IS THE CORPUS'S OWN, NOT AN IMPORT. **  `P10` describes its
tower in its own words: the TT perturbations decompose into S^3 tensor harmonics,
"each mode a harmonic oscillator with time-dependent mass a^3 and frequency mu_n/a".
A minimally coupled massless scalar on FRW reduces to (1/2) int a^3 [phidot^2 -
(k^2/a^2) phi^2] -- mass a^3, frequency k/a.  ** Those match term for term. **  So
the tower is TWO minimally coupled massless scalar degrees of freedom carrying the
TT tensor spectrum, which is also the classic Grishchuk statement about gravitational
waves on FRW.

** AND THE COEFFICIENT OF C^2 IS A PROPERTY OF THE FIELD CONTENT, NOT OF THE
BACKGROUND. **  That is why it can be fixed without redoing the spectrum on a sheared
background: what needed second order was the INVARIANT, which r6413 supplied.  This
also closes the loop with `PO-23`, whose log sits on the degenerate combination and
is a different number for a different invariant -- `PO-43` already says so.

THE DERIVATION.

  Gilkey's second heat-kernel coefficient for a Laplace-type operator on a bundle
  [IMPORTED -- see the bound below]:

    a_2 = (1/(4pi)^2)(1/360) tr{ 60 [] E + 60 R E + 180 E^2 + 30 Omega^2
                                 + (12 [] R + 5 R^2 - 2 Ric^2 + 2 Riem^2) 1 }

  For a single real scalar: E is a multiple of R, Omega = 0, tr 1 = 1.  Every term
  but the last pair is a multiple of [] R or R^2, so the ENTIRE C^2 content sits in
  2 Riem^2 - 2 Ric^2 -- and that is ** independent of the coupling xi **, which is
  why the answer does not need one.

  ** VERIFIED HERE, algebraically and not quoted: **

        2 Riem^2 - 2 Ric^2  =  3 C^2  -  E_4

  so the C^2 coefficient for one real scalar is 3/360 = 1/120, and for the tower

        ** c_tower = 2 x (1/120) = 1/60,  in units of 1/(4pi)^2 **

  equivalently c = 1/(960 pi^2), the coefficient of int sqrt(g) C^2 in the
  logarithmically divergent part of the one-loop effective action.

  CROSS-CHECK, from a different statement of the same physics: the standard trace
  anomaly is <T> = (1/16pi^2)[c C^2 - a E_4] with c = (1/120)(N_0 + 6 N_{1/2} +
  12 N_1).  At N_0 = 2 that is 2/120 = 1/60.  ** Two routes sharing only the physics
  and not the algebra. **

BOUNDS.  ** The result is STATED, and it is reversible on the second of them: if the
physical-mode count is the wrong object, the coefficient goes with it. **  A result
held back for acceptance is not a weaker claim than a stated one -- it is a deferral,
and this file carried one until r6417.

  (1) ** Gilkey's a_2 is IMPORTED. **  The tensor identity that extracts C^2 from it
      is verified here; the formula itself is not derived here and owes its citation
      at the point it lands.

  (2) ** THIS IS THE PHYSICAL-MODE COUNT, AND THAT IS A SCOPING CLAIM. **  A
      covariant spin-2 computation gauge-fixes and carries ghosts, and returns a
      different number for a different object.  `P10` SOLVES the constraints rather
      than gauge-fixing them -- there is no residual gauge freedom in the
      deparametrized tower -- so the physical-mode count is the right one for the
      object `P10` defines.  ** That is an argument from what the construction does,
      not a theorem, and it is where this discharge is most attackable. **

  (3) The overall normalisation by which a_2 enters Gamma_div is convention-
      dependent.  ** The convention-free content is the RATIO: the tower's C^2
      coefficient is exactly twice a real minimally coupled scalar's. **
"""

import numpy as np

n = 4
rng = np.random.default_rng(11)


def random_riemann():
    """A random tensor with Riemann's ALGEBRAIC symmetries.  The identity under
    test is algebraic, so no metric derivatives and no signature are needed."""
    A = rng.normal(size=(n, n, n, n))
    R = (A - A.transpose(1, 0, 2, 3) - A.transpose(0, 1, 3, 2)
         + A.transpose(1, 0, 3, 2))/4
    R = (R + R.transpose(2, 3, 0, 1))/2
    R = R - (R + R.transpose(0, 2, 3, 1) + R.transpose(0, 3, 1, 2))/3
    return R


def invariants(R):
    d = np.eye(n)
    Ric = np.einsum('iajb,ab->ij', R, d)
    Rs = np.einsum('ij,ij->', Ric, d)
    C = (R - 0.5*(np.einsum('ik,jl->ijkl', d, Ric) - np.einsum('il,jk->ijkl', d, Ric)
                  - np.einsum('jk,il->ijkl', d, Ric) + np.einsum('jl,ik->ijkl', d, Ric))
         + (Rs/6)*(np.einsum('ik,jl->ijkl', d, d) - np.einsum('il,jk->ijkl', d, d)))
    Riem2 = np.einsum('ijkl,ijkl->', R, R)
    Ric2 = np.einsum('ij,ij->', Ric, Ric)
    C2 = np.einsum('ijkl,ijkl->', C, C)
    return C, Riem2, Ric2, Rs, C2, Riem2 - 4*Ric2 + Rs**2


# --- the identity, on many independent random tensors ---------------------------
worst = 0.0
for _ in range(200):
    R = random_riemann()
    assert np.allclose(R, -R.transpose(1, 0, 2, 3), atol=1e-12)
    assert np.allclose(R, R.transpose(2, 3, 0, 1), atol=1e-12)
    assert np.allclose(R + R.transpose(0, 2, 3, 1) + R.transpose(0, 3, 1, 2), 0, atol=1e-12)
    C, Riem2, Ric2, Rs, C2, E4 = invariants(R)
    assert abs(np.einsum('iajb,ab->ij', C, np.eye(n))).max() < 1e-10, "Weyl must be traceless"
    lhs, rhs = 2*Riem2 - 2*Ric2, 3*C2 - E4
    worst = max(worst, abs(lhs - rhs)/max(1.0, abs(lhs)))
print(f"  2 Riem^2 - 2 Ric^2 = 3 C^2 - E_4 on 200 random Riemann tensors")
print(f"  worst relative error: {worst:.2e}                              OK")
assert worst < 1e-10

# --- the coefficient -------------------------------------------------------------
GILKEY_DEN = 360          # a_2 = (1/(4pi)^2)(1/360){ ... }  [IMPORTED]
C2_FROM_IDENTITY = 3      # the C^2 content of (2 Riem^2 - 2 Ric^2), verified above
c_scalar = C2_FROM_IDENTITY/GILKEY_DEN
c_tower = 2*c_scalar
print(f"\n  one real scalar : c = {C2_FROM_IDENTITY}/{GILKEY_DEN} = 1/{round(1/c_scalar)}"
      f"   (units of 1/(4pi)^2)")
print(f"  the tower (x2)  : c = 1/{round(1/c_tower)}  =  1/(960 pi^2)")
assert abs(c_scalar - 1/120) < 1e-15 and abs(c_tower - 1/60) < 1e-15

# --- cross-check from the standard anomaly formula, different algebra -------------
def c_standard(N0=0, Nhalf=0, N1=0):
    return (N0 + 6*Nhalf + 12*N1)/120
assert abs(c_standard(N0=1) - c_scalar) < 1e-15
assert abs(c_standard(N0=2) - c_tower) < 1e-15
print(f"  cross-check, c = (N0 + 6 N_1/2 + 12 N_1)/120 at N0=2: "
      f"1/{round(1/c_standard(N0=2))}                OK")

print()
print("ESTABLISHED, at the stated bounds: the tower's C^2 coefficient is EXACTLY")
print("TWICE a real minimally coupled scalar's -- 1/60 in units of 1/(4pi)^2 --")
print("because P10's own description of the tower matches two such scalars term")
print("for term, and because the coefficient is a property of the field content.")
print("IMPORTED: Gilkey's a_2.  SCOPED: the physical-mode count, P10 solving the")
print("constraints rather than gauge-fixing them, which is where this is attackable.")
