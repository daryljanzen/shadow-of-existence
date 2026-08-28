#!/usr/bin/env python3
"""RECEIPT — complex-analysis bake `C9`: ** P16 COMPUTES A UNIPOTENT MONODROMY AT THE BRANCH POINT r=0
AND CALLS IT "unipotent" AND "indicial" -- BUT NOT "FUCHSIAN" OR "regular singular point".  THE
UNIPOTENCE IS A FUCHSIAN THEOREM: IT IS FORCED BY THE INDICIAL EXPONENTS DIFFERING BY AN INTEGER. **

LEVEL: NO RATE -- a monodromy matrix and the order of its unipotence.

WHY THIS PROBE.  The r3500 measurement found this ledger at 12% reach, and P16 -- the cosmogenesis
  paper -- was unread by the field despite carrying `monodromy` x11, `indicial` x3, `resonance` x1,
  `unipotent` x1.  It is the corpus's second monodromy paper (after P05) and the field is "complex
  analysis AND monodromy".

WHAT P16 CLAIMS.  Continuing the perturbation modes around the branch point r=0 (a regular singular
  point of the mode equation): "the resulting monodromy is unipotent with off-diagonal 2 pi i p", and
  "the scalar off-diagonal is -4 pi i / rho, twice the tensor's" (rcpt
  P16_the_scalar_monodromy_is_four_pi_over_rho).  A parabolic (unipotent) transfer around a point
  the paper elsewhere calls a "branch point".

THE FIELD'S QUESTION.  WHY is the monodromy unipotent rather than diagonalisable?  P16 states the
  fact and the number; the classification behind it -- a regular singular point whose two indicial
  exponents differ by an INTEGER, the resonant/logarithmic case -- is a Fuchsian theorem, and P16
  never names it.

VERIFIED, SYMBOLICALLY.  At a regular singular point a solution basis is
      y1 = z^s * (analytic, =1 at lead),   y2 = c*log(z)*y1 + z^s*(analytic)
  and analytic continuation z -> z e^{2 pi i} sends log(z) -> log(z) + 2 pi i, z^s -> e^{2 pi i s} z^s,
  so on (y1, y2):
      M = e^{2 pi i s} [[1, 2 pi i c], [0, 1]].
  When the exponents differ by an integer with common integer part (s in Z), e^{2 pi i s} = 1 and
      M = [[1, 2 pi i c], [0, 1]]   -- UNIPOTENT: (M - I)^2 = 0, det = 1, trace = 2, one eigenvalue 1.
  The off-diagonal is exactly 2 pi i c, matching P16's "2 pi i p" with p = c the log-coefficient.

  AND THE RATIO IS STRUCTURAL.  If the scalar sector's log-coefficient is twice the tensor's
  (c_scalar = 2 c_tensor, P16's physics of which variable each sector propagates -- receipted
  separately), the off-diagonals are in ratio 2: -4 pi i / rho = 2 x (-2 pi i / rho).  The FIELD
  claims only the unipotence and the 2 pi i c form; the value -1/rho is P16's ODE, not this probe's.

THE FIELD SUPPLIES THE CLASSIFICATION P16 DOES NOT NAME.  `Fuchsian` x0 and `regular singular` x0 in
  P16.  The paper computes a resonant-exponent unipotent monodromy and never calls it a Fuchsian
  regular-singular-point monodromy -- the same anonymity as P02's meromorphic Kretschmann (C5) and
  P05's Mobius seam (C6): the corpus does the complex analysis and does not name it.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  C9 — P16's branch-point monodromy is a Fuchsian (resonant) unipotent monodromy")
print("=" * 78)

z, c, s = sp.symbols('z c s')
I = sp.I
twopii = 2 * sp.pi * I
mu = sp.exp(twopii * s)

# monodromy on the basis (y1, y2) under z -> z e^{2 pi i}
M = sp.Matrix([[mu, mu * twopii * c], [0, mu]])
print(f"\n  general resonant point, exponents with fractional part s:")
print(f"      M = {M.tolist()}")

M0 = sp.simplify(M.subs(s, 0))
print(f"\n  integer-differing exponents (s = 0):")
print(f"      M = {M0.tolist()}")

assert sp.simplify((M0 - sp.eye(2))**2) == sp.zeros(2), "must be unipotent: (M-I)^2 = 0"
assert sp.simplify(M0.det()) == 1, "det must be 1"
assert sp.simplify(M0.trace()) == 2, "trace must be 2"
eig = list(M0.eigenvals().keys())
assert eig == [sp.Integer(1)], "single eigenvalue 1"
assert sp.simplify(M0[0, 1] - twopii * c) == 0, "off-diagonal must be 2 pi i c"
print("  ** VERDICT 1: UNIPOTENT -- (M-I)^2 = 0, det = 1, trace = 2, one eigenvalue 1,")
print(f"     off-diagonal = {M0[0,1]} = 2 pi i c.  This is P16's '2 pi i p'. **")

# the ratio: scalar log-coefficient twice the tensor's -> off-diagonals in ratio 2
rho = sp.symbols('rho', positive=True)
off_tensor = twopii * (-1 / rho)     # c_tensor = -1/rho
off_scalar = twopii * (-2 / rho)     # c_scalar = 2 c_tensor
assert sp.simplify(off_scalar - 2 * off_tensor) == 0, "scalar off-diag must be twice tensor's"
assert sp.simplify(off_scalar - (-4 * sp.pi * I / rho)) == 0, "scalar off-diag = -4 pi i / rho"
assert sp.simplify(off_tensor - (-2 * sp.pi * I / rho)) == 0, "tensor off-diag = -2 pi i / rho"
print("  ** VERDICT 2: with c_scalar = 2 c_tensor, off-diagonals are -4 pi i/rho and -2 pi i/rho,")
print("     ratio exactly 2 -- P16's 'twice the tensor's'.  (The value -1/rho is P16's ODE;")
print("     the FIELD claims the unipotence and the 2 pi i c form.) **")

# a concrete Fuchsian ODE realising the log case: Euler equation z^2 y'' + z y' = 0
# exponents both 0 (differ by integer 0); solutions 1 and log z -> resonant, unipotent monodromy
zc = sp.symbols('z')
y = sp.Function('y')
ode = sp.Eq(zc**2 * y(zc).diff(zc, 2) + zc * y(zc).diff(zc), 0)
sol = sp.dsolve(ode, y(zc))
print(f"\n  concrete realisation -- Euler ODE z^2 y'' + z y' = 0 (a regular singular point at 0):")
print(f"      {sol}")
# indicial exponents: substitute y=z^r -> r(r-1)+r = r^2 = 0, double root r=0 (differ by integer 0)
r = sp.symbols('r')
indicial = sp.expand(r * (r - 1) + r)
roots = sp.solve(indicial, r)
assert indicial == r**2 and roots == [0], "indicial r^2, double root 0 -> resonant"
print(f"      indicial polynomial = {indicial}, double root r = 0 -> exponents differ by integer,")
print("      so a log solution appears and the monodromy is unipotent, not diagonalisable.")
print("  ** VERDICT 3: unipotence is FORCED by the integer-differing indicial exponents -- a Fuchsian")
print("     theorem.  P16 has `Fuchsian` x0 and `regular singular` x0; it names 'unipotent' and")
print("     'indicial' but not the classification that makes the unipotence necessary. **")

# confirm P16 names the pieces but not the classification
import os
p16 = open(os.path.join(os.path.dirname(__file__), '..', 'corpus', 'cosmogenesis_paper.tex'),
           encoding='utf-8', errors='replace').read().lower()
p16 = '\n'.join(l for l in p16.split('\n') if not l.lstrip().startswith('%'))
assert p16.count('unipotent') >= 1, "P16 says 'unipotent'"
assert p16.count('indicial') >= 1, "P16 says 'indicial'"
assert 'fuchsian' not in p16, "P16 does not say 'Fuchsian'"
assert 'regular singular' not in p16, "P16 does not say 'regular singular'"
print("  ** VERDICT 4: verified in the paper body -- 'unipotent' and 'indicial' present,")
print("     'Fuchsian' and 'regular singular' absent. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
