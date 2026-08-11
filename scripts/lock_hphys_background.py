import sympy as sp

print("="*78)
print("THE LOCK'S H_phys: the TT graviton mode on the BACKGROUND GEOMETRY")
print("(closed dS4, a(T)=alpha cosh(T/alpha)), deparametrized on cosmic time T.")
print("="*78)

T, al, mu, phi0 = sp.symbols('T alpha mu phi', real=True)
a  = al*sp.cosh(T/al)                 # background-geometry scale factor (closed dS4)
H  = sp.diff(a,T)/a
phi = sp.Function('phi')(T)
pi  = sp.Function('pi')(T)

print("\n[0] Background: ds^2=-dT^2+a(T)^2 dOmega3^2,  a(T)=alpha cosh(T/alpha).")
print("    H = a'/a =", sp.simplify(H), "  (de Sitter: H -> 1/alpha as T->inf).")

# --- TT tensor mode action on closed FLRW (one S^3 tensor harmonic, eigenvalue mu^2) ---
# S_n = (1/2) \int dT a^3 [ phidot^2 - (mu^2/a^2) phi^2 ];  mu^2 = S^3 TT-harmonic eigenvalue.
print("\n[1] TT mode action (per S^3 tensor harmonic n, eigenvalue mu_n^2):")
print("    S_n = (1/2) int dT a^3 [ phidot^2 - (mu^2/a^2) phi^2 ]")
L = sp.Rational(1,2)*a**3*(sp.diff(phi,T)**2 - (mu**2/a**2)*phi**2)
EL = sp.simplify(sp.diff(sp.diff(L,sp.diff(phi,T)),T) - sp.diff(L,phi))
print("    Euler-Lagrange (=0):", sp.simplify(EL/a**3), " * a^3")
mode_eq = sp.simplify(sp.expand(EL/a**3))
print("    => mode equation:  phidd + 3H phidot + (mu^2/a^2) phi = 0  ?")
check = sp.simplify(mode_eq - (sp.diff(phi,T,2) + 3*H*sp.diff(phi,T) + (mu**2/a**2)*phi))
print("    residual vs phidd+3H phidot+(mu^2/a^2)phi =", check, " (0 => the standard TT eqn)")

# --- Hamiltonian form ---
print("\n[2] Hamiltonian:  pi = dL/dphidot = a^3 phidot ;  H_phys = pi^2/(2a^3) + (a mu^2/2) phi^2")
Hphys = pi**2/(2*a**3) + sp.Rational(1,2)*a*mu**2*phi**2
# Hamilton's equations:
phidot_H = sp.diff(Hphys, pi)                       # = dH/dpi
pidot_H  = -sp.diff(Hphys, phi)                      # = -dH/dphi
print("    phidot = dH/dpi   =", phidot_H, "   (= pi/a^3)")
print("    pidot  = -dH/dphi =", sp.simplify(pidot_H), "   (= -a mu^2 phi)")
# substitute pi=a^3 phidot, differentiate to recover 2nd order eqn:
pi_sub = a**3*sp.diff(phi,T)
pidot_recovered = sp.diff(pi_sub, T)
ham_mode_eq = sp.simplify((pidot_recovered - pidot_H.subs(pi, pi_sub))/a**3)
print("    Hamilton -> 2nd order:", sp.simplify(ham_mode_eq),
      "  (= phidd+3H phidot+(mu^2/a^2)phi, matches [1])")

print("\n[3] Deparametrization on cosmic time T (P8 structure):")
print("    i d/dT Psi = H_phys^hat Psi,   H_phys^hat = sum_n [ pi_n^2/(2a^3) + (a mu_n^2/2) phi_n^2 ]")
print("    = a TOWER of time-dependent harmonic oscillators, one per S^3 TT tensor harmonic,")
print("    frequency-squared omega_n^2(T) = mu_n^2/a(T)^2, mass m(T)=a(T)^3. Well-defined,")
print("    unitary T-evolution (the standard graviton-on-de Sitter squeezing Hamiltonian).")

print("\n" + "="*78)
print("VERDICT: on the background geometry the lock's H_phys CLOSES structurally:")
print(" - the TT graviton modes are the propagating DOF (P8's abstract (q^A,p_A));")
print(" - H_phys is a discrete tower of time-dependent oscillators (S^3 spectrum mu_n^2);")
print(" - it deparametrizes on cosmic time, i d/dT Psi = H_phys^hat Psi, unitary;")
print(" - NO obstruction at the structural level (each mode a clean oscillator).")
print("Open: explicit mu_n^2 (S^3 TT-harmonic spectrum); the Nariai representational")
print("reading (matter bend); self-adjointness/ordering. Background level; M!=0 = the rep.")
