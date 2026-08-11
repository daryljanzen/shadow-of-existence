"""
C1 -- is alpha (or a quantity built from it) the intrinsic GRAVITATIONAL mass?  (added 2026-06-30, r547)

P3 sec:mass (l.529) leaves open: "whether alpha, or a quantity built from it, is the correct intrinsic
gravitational mass in the sense of the standard quasi-local or asymptotic mass definitions."  P3
establishes alpha = sqrt(3/Lambda) as the INVARIANT of the slicing construction and M as the
slicing/projection-dependent (perspectival, P-odd) factor, 2M = alpha (s - s^3), s = r0/alpha.  The
construction is careful NOT to claim alpha is the mass; it claims alpha is the invariant.  This script
asks what the STANDARD gravitational-mass definitions actually return for the SdS metric
   f(r) = 1 - 2M/r - r^2/alpha^2     (alpha = sqrt(3/Lambda), the de Sitter / throat radius).

If they return M, the gravitational mass is the perspectival quantity (and alpha is the invariant
LENGTH, not a mass); if they return alpha or a function of it, the alpha-as-mass hope is supported.
"""
import sympy as sp

r, M, alpha, Lam, s = sp.symbols('r M alpha Lambda s', positive=True)
f = 1 - 2*M/r - r**2/alpha**2

print("="*72)
print("C1 -- standard gravitational-mass definitions for SdS  f=1-2M/r-r^2/alpha^2")
print("="*72)

# --- 1. Misner-Sharp quasi-local mass: 1 - 2m/r = |grad r|^2 = g^{rr} = f ---------------------
m_MS = sp.simplify(r*(1 - f)/2)
print("\n[1] Misner-Sharp quasi-local mass  m_MS(r) = (r/2)(1-f):")
print("      m_MS(r) =", m_MS, "  = M + r^3/(2 alpha^2)")
print("      -> mass PARAMETER (r-independent part) = M ;  alpha enters only as the +r^3/(2a^2)")
print("         de Sitter background (the Lambda/6 r^3 vacuum energy inside r).  r->0: m_MS -> M.")

# --- 2. Komar mass (static): m_K(r) = (1/2) r^2 f'(r) ----------------------------------------
m_K = sp.simplify(sp.Rational(1,2)*r**2*sp.diff(f, r))
print("\n[2] Komar mass  m_K(r) = (1/2) r^2 f'(r):")
print("      m_K(r) =", m_K, "  = M - r^3/alpha^2")
print("      -> mass PARAMETER = M ; alpha enters as the -r^3/a^2 de Sitter term (neg. pressure).")
print("         r->0: m_K -> M.  Both quasi-local masses return M as the central mass parameter.")

# --- 3. pure de Sitter (M=0): the invariant geometry carries ZERO mass parameter -------------
print("\n[3] Pure de Sitter (M=0, the P-even invariant geometry):")
print("      m_MS|_{M=0} =", m_MS.subs(M,0), " ;  m_K|_{M=0} =", m_K.subs(M,0))
print("      mass PARAMETER = 0.  alpha is the de Sitter CURVATURE RADIUS (Kretschmann 24/alpha^4,")
print("      curvature scale 1/alpha^2) -- a LENGTH, not a mass.  So alpha is not a gravitational mass.")

# --- 4. asymptotics: SdS is asymptotically de Sitter, not flat -------------------------------
print("\n[4] Asymptotic definitions: SdS is asymptotically de Sitter (not flat), so ADM (flat) does")
print("    not apply; the asymptotically-dS mass (Abbott-Deser / Ashtekar-Das) and the Komar charge")
print("    of the static Killing vector both return the parameter M.  No standard definition returns")
print("    alpha as a mass; alpha is the background curvature scale common to every member.")

# --- 5. the one place a quantity built from alpha IS the mass: the Nariai (physical) member ---
print("\n[5] The physical (cosmological = Nariai) member -- the lone alpha-locked case:")
# Nariai = double root of the horizon cubic r^3 - alpha^2 r + 2 M alpha^2 = 0
cubic = r**3 - alpha**2*r + 2*M*alpha**2
# double root: cubic and its derivative share a root
rc = sp.symbols('rc', positive=True)
sol = sp.solve([cubic.subs(r, rc), sp.diff(cubic, r).subs(r, rc)], [rc, M], dict=True)
print("      double-root (Nariai) solutions (rc, M):")
for d in sol:
    Mn = sp.simplify(d[M]); rcn = sp.simplify(d[rc])
    LamM2 = sp.simplify((3/alpha**2)*Mn**2)     # Lambda M^2 with Lambda = 3/alpha^2
    print(f"        rc = {rcn},   M_Nariai = {Mn},   Lambda*M^2 = {LamM2}")
print("      -> M_Nariai = alpha/(3 sqrt3)  (Lambda M^2 = 1/9, the Nariai condition).  Here, and ONLY")
print("         here, the gravitational mass IS a quantity built from alpha; for a general slicing M")
print("         ranges freely over [0, alpha/(3 sqrt3)] and is independent of alpha.")
Mmax = sp.solve(sp.diff(alpha*(s-s**3), s), s)  # extremum of the slicing profile
print(f"      slicing-profile extremum at s=r0/alpha = {[sp.simplify(x) for x in Mmax]}  -> 2M_max = alpha*2/(3 sqrt3).")

print("\n[VERDICT]")
print(" - Every standard gravitational-mass definition (Misner-Sharp, Komar; asymptotically-dS) returns")
print("   the PARAMETER M, not alpha.  So alpha is NOT the gravitational mass: it is the invariant")
print("   de Sitter curvature RADIUS (a length), and pure dS -- the P-even invariant geometry -- carries")
print("   zero mass.  This does not refute P3; it CONFIRMS it: the gravitational mass the standard")
print("   definitions measure IS the perspectival, P-odd M (computed in the Schwarzschild vantage),")
print("   exactly the quantity P3 sec:mass identifies as the projection.  The invariant is a length, alpha.")
print(" - The lone sense in which 'a quantity built from alpha' is the mass is the physical Nariai")
print("   member, where the double-root condition locks M = alpha/(3 sqrt3) (Lambda M^2 = 1/9).")
print(" - So C1's answer: NO, alpha is not the intrinsic gravitational mass; the gravitational mass is")
print("   the perspectival M, and the standard definitions return it -- the open question resolved in")
print("   the direction that sharpens, not softens, the perspectival reading.  [E] for the mass formulae")
print("   and the Nariai lock; [reading] for the perspectival synthesis.")
print("="*72)
