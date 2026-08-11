"""
P10_graviton_lift.py -- verifies sec:lock (the closed-S^3 graviton lift): each tensor harmonic on the layer
  has action S_n = (1/2) int dT a^3 [ phidot_n^2 - (mu_n^2/a^2) phi_n^2 ], with conjugate momentum
  pi_n = a^3 phidot_n. Its Legendre transform is the (time-dependent) oscillator Hamiltonian
    Hphys_n = pi_n^2/(2 a^3) + (1/2) a mu_n^2 phi_n^2,
  so i d_T Psi = Hphys Psi is a unitary cosmic-time evolution of a tower of oscillators (one per harmonic).
  The Euler-Lagrange / Hamilton equations give the graviton mode equation on FLRW:
    phiddot_n + 3 (adot/a) phidot_n + (mu_n^2/a^2) phi_n = 0.  [P10 canonical_time sec:lock]
STATUS: ✔✔   RUN: python3 P10_graviton_lift.py   RUNTIME: ~2s
COMPUTES: pi_n=dL/dphidot=a^3 phidot; Hamiltonian via Legendre H=pi phidot - L = pi^2/2a^3 + (1/2)a mu^2 phi^2;
  Hamilton's equations reproduce the EL mode equation (Hubble-damped time-dependent oscillator). CONTROL: a
  constant a reduces it to the standard harmonic oscillator phiddot + mu^2 phi = 0 (no Hubble friction).
ORIGIN: built new r1371 (P10 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
T=sp.symbols('T', real=True); mu=sp.symbols('mu', positive=True)
a=sp.Function('a')(T); phi=sp.Function('phi')(T)
phidot=sp.diff(phi,T); adot=sp.diff(a,T)
L = sp.Rational(1,2)*a**3*(phidot**2 - (mu**2/a**2)*phi**2)
print("="*70); print("P10 closed-S^3 graviton lift: tensor-harmonic action -> oscillator Hamiltonian"); print("="*70)
# (1) conjugate momentum pi_n = dL/dphidot = a^3 phidot
pi_n = sp.diff(L, phidot)
ok&=check("conjugate momentum pi_n = dL/dphidot = a^3 phidot", sp.simplify(pi_n - a**3*phidot)==0)
# (2) Legendre transform: H = pi phidot - L, expressed in (phi, pi)
pi=sp.Symbol('pi_n'); phidot_of=pi/a**3     # invert pi=a^3 phidot
H = sp.simplify((pi_n*phidot - L).subs(phidot, phidot_of).doit())
# careful: substitute phidot->pi/a^3 everywhere
Hsub = sp.simplify((pi*phidot_of - sp.Rational(1,2)*a**3*(phidot_of**2 - (mu**2/a**2)*phi**2)))
target = pi**2/(2*a**3) + sp.Rational(1,2)*a*mu**2*phi**2
ok&=check("Legendre: Hphys_n = pi phidot - L = pi_n^2/(2 a^3) + (1/2) a mu_n^2 phi_n^2", sp.simplify(Hsub - target)==0)
# (3) Euler-Lagrange mode equation
EL = sp.simplify(sp.diff(sp.diff(L,phidot),T) - sp.diff(L,phi))
mode = sp.simplify(EL/a**3)                 # divide by a^3
target_mode = sp.diff(phi,T,2) + 3*(adot/a)*phidot + (mu**2/a**2)*phi
ok&=check("Euler-Lagrange => phiddot + 3(adot/a)phidot + (mu^2/a^2)phi = 0 (graviton mode eq on FLRW)",
          sp.simplify(mode - target_mode)==0)
# (4) Hamilton's equations reproduce the mode equation
#   phidot = dH/dpi = pi/a^3 ; pidot = -dH/dphi = -a mu^2 phi ; combine
phidot_H = sp.diff(target, pi)
pidot_H = -sp.diff(target, phi)
# from pi = a^3 phidot: d/dT(a^3 phidot) = pidot_H  -> the mode equation
lhs = sp.simplify(sp.diff(a**3*phidot, T))
ok&=check("Hamilton: phidot=pi/a^3 & pidot=-a mu^2 phi combine (pi=a^3 phidot) to d/dT(a^3 phidot)+a mu^2 phi=0, i.e. the mode eq",
          sp.simplify(phidot_H - pi/a**3)==0 and sp.simplify((lhs + a*mu**2*phi)/a**3 - target_mode)==0)
# CONTROL: constant a -> standard harmonic oscillator (no Hubble friction)
a0=sp.symbols('a0', positive=True)
mode_const=sp.simplify(target_mode.subs(a, a0).doit())
ok&=check("CONTROL: constant a=a0 -> phiddot + (mu^2/a0^2)phi = 0 (standard oscillator, no 3H friction)",
          sp.simplify(mode_const - (sp.diff(phi,T,2)+(mu**2/a0**2)*phi))==0)
print("="*70)
print("RESULT:", "ALL PASS -- the tensor-harmonic action Legendre-transforms to the oscillator Hamiltonian\n         pi^2/2a^3 + (1/2)a mu^2 phi^2; i d_T Psi = Hphys Psi is unitary cosmic-time evolution of the graviton tower." if ok else "SOME FAILED")
print("="*70)

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) the PASS/FAIL flag the file previously only PRINTED:
# every check above (momentum, Legendre transform, EL mode equation, Hamilton's equations,
# constant-a control) must actually hold.  (b) the Hubble-friction coefficient of the
# graviton mode equation is exactly 3 -- phiddot + 3(adot/a)phidot + (mu^2/a^2)phi = 0 --
# which is the number sec:lock prints; a 2 or a 4 there would be a different theory.
assert ok, "P10 graviton lift: at least one check FAILED"
friction = sp.simplify(sp.expand(mode).coeff(sp.diff(phi, T))*a/adot)
assert sp.simplify(friction - 3) == 0, "Hubble friction coefficient is %s, not 3" % friction
