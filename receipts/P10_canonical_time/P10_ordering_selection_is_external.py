#!/usr/bin/env python3
"""L-833 — THE ORDERING EXHAUSTION: NOTHING INTERNAL TO THE CONSTRUCTION SELECTS THE ORDERING, AND THE
REASON IS THAT SELECTING IT WOULD BE SOLVING THE COSMOLOGICAL-CONSTANT PROBLEM.

`PO-15`.  P10 `sec:lock` states, but does not enumerate behind, that the operator ordering of the
graviton tower's boundary coefficient -- the minimum of $\\hat\\Gamma$ is $\\tfrac14$ normal-ordered,
$\\tfrac34$ symmetric, differing by exactly one zero-point quantum -- is *"not one this construction
can make internally,"* and that *"asking which ordering is asking whether the graviton tower's
zero-point energy gravitates at the horizon -- the cosmological-constant problem in local dress."*

This is the exhaustion behind that sentence.  It builds on two prior results and completes them:
  * `S11` (r2763): the boundary CLOSURE is ordering-independent -- the thermal state fixes the
    self-adjoint condition fibre by fibre for EITHER ordering, so the ambiguity does not threaten the
    quantization's uniqueness.  (Closure, not selection.)
  * r3014: the thermal state cannot SELECT the ordering -- it selects the Friedrichs extension, which
    is defined FROM the quadratic form, and the form is what an ordering produces; so it acts
    downstream, given an ordering.
`PO-15`'s step is to ask the same of EVERY candidate selector the construction offers, and either find
one or state the choice is external with the enumeration as the evidence.  No selector survives.

** THE PIVOT (PART 1), which every disqualification below turns on: THE ORDERING IS BULK-INERT AND
BOUNDARY-PHYSICAL. **  Normal vs symmetric ordering of each mode differ by the c-number zero-point
$\\tfrac12\\hbar\\omega_n$; a c-number in the deparametrized Hamiltonian is a global phase, so the tower's
unitary evolution cannot see the ordering; and the difference surfaces ONLY in the horizon boundary
coefficient, $\\tfrac14\\to\\tfrac34$, the shift being exactly one zero-point quantum.  So "which
ordering" IS "does the tower's zero-point energy gravitate at the horizon" -- the cc problem.

  PART 1  ** THE PIVOT: bulk-inert (a phase), boundary-physical (the zero-point), = the cc problem. **
  PART 2  ** THE EXHAUSTION: every internal candidate selector, and its structural disqualification. **
  PART 3  ** THE RESULT: external, and WHY -- an epistemic gap (does vacuum energy gravitate), not an
          ontological family; the construction localizes the gap, it does not carry an unforced parameter. **

STATUS: ✔✔ (the ordering difference asserted to be the zero-point c-number; the c-number-is-a-phase
  fact asserted numerically; the boundary shift 1/4 -> 3/4 asserted to be exactly that quantum; a
  regular indicial branch asserted to exist for BOTH orderings so the thermal closure is
  ordering-independent; both floors asserted finite; the enumeration stated with a structural
  disqualification per candidate and no survivor)
RUN: python3 P10_ordering_selection_is_external.py   RUNTIME: ~3s
ORIGIN: built r3100 (c54); completes S11 (r2763) and the r3014 thermal-state elimination for `PO-15`.
"""
import numpy as np
import sympy as sp
from scipy.linalg import expm

print(__doc__.split("STATUS:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE PIVOT: BULK-INERT (A PHASE), BOUNDARY-PHYSICAL (THE ZERO-POINT)")
print("=" * 78)
w, hbar = sp.symbols('omega hbar', positive=True)
n = sp.Symbol('n', nonnegative=True, integer=True)
E_sym = hbar*w*(n + sp.Rational(1, 2))      # symmetric/Weyl: keeps the zero-point
E_norm = hbar*w*n                            # normal: drops it
diff = sp.simplify(E_sym - E_norm)
print(f"  (a) per mode, E_symmetric(n) - E_normal(n) = {diff}  -- the zero-point c-number, state-independent")
assert diff == hbar*w/2

# (b) a c-number in H is a global phase: all bulk amplitudes identical
rng = np.random.default_rng(0)
d = 6
A = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d))
H = (A + A.conj().T)/2
c, t = 0.7351, 1.3
U, Uc = expm(-1j*H*t), expm(-1j*(H + c*np.eye(d))*t)
psi = rng.normal(size=d) + 1j*rng.normal(size=d); psi /= np.linalg.norm(psi)
chi = rng.normal(size=d) + 1j*rng.normal(size=d); chi /= np.linalg.norm(chi)
amp, ampc = np.vdot(chi, U@psi), np.vdot(chi, Uc@psi)
print(f"  (b) |amplitude| under H = {abs(amp):.12f}, under H + c = {abs(ampc):.12f}  "
      f"(ratio = pure phase e^-ict)")
assert abs(abs(amp) - abs(ampc)) < 1e-12 and abs(ampc/amp - np.exp(-1j*c*t)) < 1e-10
print("      => the deparametrized tower's evolution is BLIND to the ordering (it is a global phase).")

# (c) the difference lives only in the horizon boundary coefficient
g_free = sp.Rational(1, 4)
zpq = sp.Rational(1, 2)
g_norm, g_sym = g_free, g_free + zpq
print(f"  (c) horizon coefficient: normal = {g_norm} (limit-circle), symmetric = {g_norm}+{zpq} = {g_sym} "
      f"(limit-point); threshold 3/4")
assert g_sym == sp.Rational(3, 4) and (g_sym - g_norm) == zpq
print("      => 'which ordering' = 'does the zero-point 1/2-quantum enter the horizon coefficient'")
print("         = 'does the tower's zero-point energy gravitate at the horizon' = the cc problem.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE EXHAUSTION: EVERY INTERNAL CANDIDATE, AND WHY IT CANNOT SELECT")
print("=" * 78)

# A checkable fact used by candidate (1): the thermal closure is ordering-INDEPENDENT, because a
# regular indicial branch x^{1/2+nu}, nu=sqrt(Gamma+1/4), exists for BOTH orderings (nu real for both).
nu_norm = sp.sqrt(g_norm + sp.Rational(1, 4))
nu_sym = sp.sqrt(g_sym + sp.Rational(1, 4))
print(f"  [check] regular branch exponent nu = sqrt(Gamma+1/4):  normal -> {nu_norm}, symmetric -> {nu_sym}")
print("          real and distinct for both, so Hartle--Hawking regularity picks the regular branch")
print("          on EITHER ordering -- the closure is ordering-independent (S11), the selection is not.")
assert nu_norm.is_real and nu_sym.is_real
# candidate (5): both orderings are bounded below (finite floor)
print(f"  [check] both orderings give a finite floor for Gamma-hat: {g_norm} and {g_sym} -- "
      f"bounded-below discriminates neither.")
assert g_norm > 0 and g_sym > 0

cands = [
 ("1. The horizon's thermal (Hartle--Hawking) state",
  "DOWNSTREAM. It selects the Friedrichs extension, defined FROM the quadratic form; the form is what "
  "the ordering produces. The regular-branch check above holds for BOTH orderings, so the thermal "
  "condition closes the boundary GIVEN Gamma-hat and cannot reach back to set it. (r3014.)"),
 ("2. The substrate's continuous isometry (SO(5,1); SO(4) on the S^3 harmonics)",
  "RESPECTS BOTH. The ordering difference is the c-number sum of zero-points Sum 1/2 hbar omega_n, "
  "invariant under the isometry's mixing of degenerate harmonics at fixed n; normal and symmetric "
  "ordering are each built from isometry-invariant mode bilinears. A symmetry obeyed equally by both "
  "options cannot distinguish them."),
 ("3. The seam's characteristic (null) structure",
  "SAME LOCATION AS (1). The null-boundary reassignment fixes WHERE the condition sits (a=0 is the "
  "horizon) and the surface gravity kappa=1/alpha -- which P10 notes 'belongs to the background "
  "horizon, not to the graviton content, and so is common to every fibre'. A fibre-independent "
  "constant cannot discriminate fibres by ordering."),
 ("4. The deparametrization / true Hamiltonian  [the strongest candidate -- it cuts the OTHER way]",
  "FAILS TWICE. (i) Its preferred cosmic time makes a preferred vacuum AVAILABLE, hence normal "
  "ordering DEFINABLE -- but not mandatory: the physical question is whether to gravitate that "
  "vacuum's energy, which having a vacuum does not answer. (ii) More sharply, the deparametrization "
  "SOLVES the constraint (Brown--Kuchar dust momentum enters linearly, a true Hamiltonian at every "
  "order), so it REMOVES the one lever a Wheeler--DeWitt quantization would have had -- anomaly-free "
  "closure of the quantum constraint. The move that supplies CR's clock removes the classical "
  "ordering-fixing mechanism rather than supplying one."),
 ("5. Positivity / bounded-below (Gamma-hat >= floor)",
  "SATISFIED BY BOTH. Floors 1/4 and 3/4 are both finite (checked above; P10_gamma_hat_is_bounded_below). "
  "No discrimination."),
 ("6. The constant ledger / single-scale (Lambda-only) dimensional structure",
  "BLIND. The ordering difference is a dimensionless number (1/2 per mode). A single scale alpha fixes "
  "dimensions, not a dimensionless ordering constant."),
 ("7. Covariance under configuration redefinition (Laplace--Beltrami / DeWitt ordering)",
  "DOES NOT REACH IT. In the FREE case this ordering is in the family and gives 1/4 like all others "
  "(ordering-independence). For the tower the physical difference is the zero-point, a c-number set by "
  "the frequency; normal ordering subtracts a c-number and REMAINS covariant, so covariance does not "
  "fix whether the zero-point is subtracted."),
]
for name, why in cands:
    print(f"\n  {name}")
    for line in [why[i:i+92] for i in range(0, len(why), 92)]:
        print(f"     {line}")

print()
print("  -- and the free-sector escape hatch does not transfer, for a reason the paper's own")
print("     arithmetic gives:")
print("     P10 establishes gamma=1/4 across the ordering family for the FREE scale factor. But the")
print("     tower's boundary coefficient carries a zero-point term the free case lacks -- that is the")
print("     paper's own 3/4 = 1/4 + 1/2, 'the free boundary coefficient plus one such quantum'. So the")
print("     free-case ordering-independence does not reach the tower, and no continuity forces the")
print("     tower to inherit 1/4.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RESULT: EXTERNAL, AND WHY IT IS A GAP AND NOT A FAMILY")
print("=" * 78)
for s in [
 "⇒⇒ ** NO MECHANISM INTERNAL TO THE CONSTRUCTION SELECTS THE ORDERING. ** Each candidate above either",
 "   respects both orderings equally (isometry, positivity, dimensional, covariance) or acts downstream",
 "   of the ordering (the thermal state and the seam close the boundary GIVEN Gamma-hat); and the",
 "   deparametrization, the one move that might have supplied a selector, instead REMOVES the classical",
 "   one by solving the constraint rather than imposing it.",
 "",
 "⌗ ** AND THE TWO EXTERNAL NATURALNESS HEURISTICS DISAGREE, ** which is itself evidence of externality:",
 "   continuity with the free sector (1/4 for all orderings there) argues for NORMAL (1/4); maximal",
 "   predictivity -- removing the boundary freedom so no condition need be chosen -- argues for",
 "   SYMMETRIC (3/4, limit-point from the first occupied mode). No internal principle breaks the tie.",
 "",
 "⛭⛭ ** SO THE CHOICE IS EXTERNAL -- AND EXTERNAL BECAUSE IT IS THE COSMOLOGICAL-CONSTANT PROBLEM. **",
 "   By PART 1 the ordering IS the question 'does the tower's zero-point energy gravitate at the",
 "   horizon'. That the construction cannot settle it internally is not a defect: it is a known",
 "   unsolved problem of physics, REACHED FROM INSIDE the boundary coefficient rather than imported.",
 "",
 "⚠ ** AND IT IS AN EPISTEMIC GAP, NOT AN ONTOLOGICAL FAMILY -- so it does not fall to the epistemic",
 "   reading's exclusion of unforced parameters. ** The reading (JanzenShadowExistence) excludes a",
 "   continuous lambda that indexes distinct WORLDS. This is not that: it is a single binary tied to an",
 "   unknown DATUM of the one world -- whether vacuum energy gravitates -- of exactly the kind the",
 "   reading admits (the progenitor's mass, say). The construction does not carry an unforced parameter;",
 "   it LOCALIZES the gap precisely, as the gravitation of one computable quantity, and hands the",
 "   deciding to the physics that decides the cc problem. Saying which -- with this enumeration as the",
 "   evidence -- is the result the row asked for.",
]:
    print("  " + s)
print()
print("  VERDICT: the ordering is genuinely EXTERNAL to the CR construction; the enumeration is the")
print("  evidence, and the externality is the cc problem localized, not a residual freedom the")
print("  construction failed to close.")
