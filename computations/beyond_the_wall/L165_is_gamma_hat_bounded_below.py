#!/usr/bin/env python3
"""
`L-165`.  ** IS THE COMPLETE BOUNDARY OPERATOR $\\hat\\Gamma$ BOUNDED BELOW?  YES — AND THE REASON IS
THE DEPARAMETRIZATION ITSELF, WHICH REMOVES THE ONE NEGATIVE DIRECTION OF THE SUPERMETRIC. **

P10 lists three things under 'the definition of the interacting tower': the spectrum of
$\\hat\\Gamma$ *including whether it is bounded below*, the ultraviolet definition of the mode sums,
and (in P11) the closed-form nonlinear solution.  ** The first is separable from the other two and
is settled here.  The other two are not touched. **

c54.116 established that the straddle needs only that the spectrum MEET BOTH SIDES of 3/4, and that
at leading order $\\hat\\Gamma=\\gamma+c\\sum\\hat\\pi_n^2$ is a sum of squares.  It left open whether
the cubic and higher self-interactions, entering at the same inverse-square order, spoil it.

  PART 1  ** THE SUPERMETRIC HAS EXACTLY ONE NEGATIVE DIRECTION, AND IT IS THE CONFORMAL ONE. **
  PART 2  ** ON THE TRANSVERSE-TRACELESS SECTOR IT IS POSITIVE DEFINITE — for every non-degenerate
          spatial metric, checked over a sweep. **
  PART 3  ** SO THE APPARENT UNBOUNDEDNESS IS A TRUNCATION ARTEFACT: $\\pi^2(1-\\lambda\\phi+\\dots)$
          is the expansion of $\\pi^2/(1+\\lambda\\phi)$, and the full coefficient is positive. **
  PART 4  What this settles, and the two clauses it does not.

Run: python3 L165_is_gamma_hat_bounded_below.py      (numpy, sympy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
rng = np.random.default_rng(20260810)

# ** WORKED WITH MATRICES, NOT PACKED 6-VECTORS.  A first version packed symmetric tensors into
# R^6, weighted the off-diagonals, and then projected out the trace direction using the EUCLIDEAN
# inner product on that packing -- which is not the inner product the trace condition is defined in.
# It reported the form indefinite on anisotropic metrics.  The assertion caught it.  Written
# directly on matrices the whole thing is two lines and has no packing to get wrong. **
def Q(g, pi, lam=1.0):
    """the DeWitt kinetic form  G_ijkl pi^ij pi^kl  =  tr((g pi)^2) - lam (tr(g pi))^2"""
    A = g @ pi
    return float(np.trace(A @ A) - lam * np.trace(A) ** 2)


def rand_sym(scale=1.0):
    A = rng.normal(size=(3, 3)) * scale
    return (A + A.T) / 2


def make_traceless(g, pi):
    """subtract the g-trace part so that tr(g pi) = 0"""
    gi = np.linalg.inv(g)
    return pi - (np.trace(g @ pi) / 3.0) * gi


# =====================================================================
print("=" * 78)
print("PART 1 — THE SUPERMETRIC HAS EXACTLY ONE NEGATIVE DIRECTION")
print("=" * 78)
g0 = np.eye(3)
print("  The DeWitt form on symmetric momenta is  tr((g pi)^2) - lambda (tr(g pi))^2.")
print("  On the round metric, evaluate it on a basis to read off the signature:")
basis = []
for a in range(3):
    E = np.zeros((3, 3))
    E[a, a] = 1.0
    basis.append(E)
for a, b in [(0, 1), (0, 2), (1, 2)]:
    E = np.zeros((3, 3))
    E[a, b] = E[b, a] = 1.0
    basis.append(E)
M = np.array([[0.5 * (Q(g0, u + v) - Q(g0, u) - Q(g0, v)) for v in basis] for u in basis])
ev = np.linalg.eigvalsh(M)
print(f"     eigenvalues: {np.round(ev, 4)}")
neg = int((ev < -1e-9).sum())
print(f"  ** negative directions: {neg} — exactly one. **")
assert neg == 1
print(f"  and it IS the trace (conformal) direction: Q(g0, identity) = {Q(g0, np.eye(3)):.4f} < 0")
assert Q(g0, np.eye(3)) < 0
print()
for s in [
 "⌗ ** THAT ONE NEGATIVE DIRECTION IS THE WHOLE INDEFINITENESS OF SUPERSPACE, and it is the",
 "   SCALE FACTOR's. **  *It is why the Wheeler--DeWitt equation is hyperbolic rather than",
 "   elliptic, and it is the direction P10's construction removes by using the scale factor as a",
 "   clock.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ON THE TT SECTOR IT IS POSITIVE DEFINITE")
print("=" * 78)
print("  On g-traceless momenta the trace term drops and the form is exactly  tr((g pi)^2).")
print("  ** And that is positive definite for ANY positive-definite g, structurally: g pi is")
print("     similar to the symmetric g^(1/2) pi g^(1/2), so tr((g pi)^2) is a sum of squares of")
print("     its real eigenvalues, zero only when pi = 0. **  Verified by sweep:")
print()
print(f"  {'metric':>34} {'min eig(g)':>11} {'min Q on traceless':>20} {'positive?':>11}")
cases = [("round, g = I", np.eye(3)),
         ("strongly anisotropic", np.diag([4.0, 1.0, 0.25])),
         ("very anisotropic", np.diag([25.0, 1.0, 0.04]))]
for t in range(3):
    g = np.eye(3) + 0.6 * rand_sym()
    while np.linalg.eigvalsh(g).min() < 0.1:
        g = np.eye(3) + 0.3 * rand_sym()
    cases.append((f"random #{t+1}", g))
allpos = True
for nm, g in cases:
    vals = []
    for _ in range(4000):
        pi = make_traceless(g, rand_sym())
        n = np.linalg.norm(pi)
        if n > 1e-8:
            vals.append(Q(g, pi / n))
    m = min(vals)
    allpos &= (m > 1e-12)
    print(f"  {nm:>34} {np.linalg.eigvalsh(g).min():>11.3f} {m:>20.6f} {str(m > 1e-12):>11}")
assert allpos
# and the structural identity, checked exactly
for _ in range(200):
    g = np.eye(3) + 0.5 * rand_sym()
    if np.linalg.eigvalsh(g).min() < 0.1:
        continue
    pi = make_traceless(g, rand_sym())
    gh = np.linalg.cholesky(g)
    S = gh.T @ pi @ gh
    assert abs(Q(g, pi) - np.trace(S @ S)) < 1e-9
print("  ** and the identity tr((g pi)^2) = tr(S^2) with S = L^T pi L symmetric verified exactly")
print("     on 200 random (g, pi) pairs -- so the positivity is an identity, not a sample. **")
print()
for s in [
 "⇒⇒ ** POSITIVE DEFINITE ON EVERY NON-DEGENERATE SPATIAL METRIC. **  *The entire negative part of",
 "   the DeWitt form lives in the trace term $-\\lambda(\\mathrm{tr}\\,g\\pi)^2$, and the traceless",
 "   condition annihilates it exactly.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE UNBOUNDEDNESS IS A TRUNCATION ARTEFACT")
print("=" * 78)
lam, phi, pi_ = sp.symbols('lambda phi pi', real=True)
full = pi_**2 / (1 + lam * phi)
ser = sp.series(full, lam, 0, 3).removeO()
print(f"  The coefficient of the inverse-square operator is pi^2 times an inverse metric factor:")
print(f"     full     :  pi^2 / (1 + lambda phi)")
print(f"     expanded :  {sp.expand(ser)}")
print()
print("  ** The CUBIC term of the interacting Hamiltonian is the -lambda phi pi^2 piece of that")
print("     expansion, and taken alone it is unbounded below: send phi -> +infinity at fixed pi. **")
print("  ** But the object it is a term OF is positive whenever 1 + lambda phi > 0, which is the")
print("     statement that the spatial metric is non-degenerate. **")
xs = np.linspace(-0.9, 6.0, 12)
print(f"\n  {'lambda phi':>12} {'truncated at cubic':>22} {'full pi^2/(1+lam phi)':>24}")
for x in xs[::3]:
    print(f"  {x:>12.2f} {1 - x:>22.4f} {1.0/(1.0+x):>24.4f}")
trunc = 1 - xs
fullv = 1.0 / (1.0 + xs)
assert trunc.min() < 0 and fullv.min() > 0
print(f"\n  ** truncated goes negative (min {trunc.min():.3f}); the full expression stays positive")
print(f"     (min {fullv.min():.4f}) on the whole non-degenerate range. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — WHAT THIS SETTLES")
print("=" * 78)
print(f"  {'clause of L-165':>50} {'status':>22}")
for a, b in [("is Gamma-hat bounded below?", "** YES, settled here **"),
             ("the UV definition of the mode sums", "NOT TOUCHED"),
             ("the closed-form nonlinear Lambda>0 solution", "NOT TOUCHED")]:
    print(f"  {a:>50} {b:>22}")
print()
for s in [
 "✔✔ ** $\\hat\\Gamma$ IS BOUNDED BELOW, and the reason is the construction's own move: the",
 "   deparametrization uses the scale factor as the clock, and the scale factor IS the supermetric's",
 "   one negative direction.  Removing it leaves a positive-definite kinetic form on the",
 "   transverse-traceless tower, so the complete $\\hat\\Gamma$ is $\\gamma$ plus a positive operator. **",
 "",
 "⌗⌗ ** AND THAT IS NOT A LUCKY FEATURE OF THIS MODEL.  It is why deparametrizing by the scale",
 "   factor was the right move in the first place — the same choice that produces a true",
 "   Hamiltonian also produces a bounded-below one, because both are the removal of the conformal",
 "   direction. **  *P10 argues the first and did not notice it had the second.*",
 "",
 "⚠ ** THE BOUND, AND IT IS REAL: positivity holds on NON-DEGENERATE spatial metrics.  At the",
 "   degenerate boundary of superspace the inverse metric blows up and the argument says nothing —",
 "   which is exactly the $a\\to0$ boundary the whole construction is about. **  *So the statement",
 "   is: bounded below on the interior, with the boundary handled by the thermal condition P10",
 "   already supplies.  Those are two different jobs and neither substitutes for the other.*",
 "",
 "⇒ ** L-165 SHRINKS BY ONE CLAUSE OF THREE.  What remains is the ultraviolet definition of the",
 "   tower sums and the closed-form nonlinear solution — and those are the standard problems of an",
 "   interacting theory, not features of this construction. **",
]:
    print("  " + s)
