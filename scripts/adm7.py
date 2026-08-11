import sympy as sp
print("="*78)
print("ADM-7: the deparametrized physical Hamiltonian H_phys and its tau-evolution")
print("  (CR's actual QG content: an absolute clock that resolves the problem of time)")
print("="*78)
a,p,Lam,rho,tau,A,al=sp.symbols('a p_a Lambda rho_d tau A alpha',positive=True)

# Flat FLRW minisuperspace (G=1, fiducial volume 1), gravitational+Lambda Hamiltonian
# derived from the reduced EH action: H_grav = (2pi/3) p_a^2/a - (Lambda/8pi) a^3
# Dust clock (Brown-Kuchar): constraint H_grav + (dust) = 0; deparametrize -> H_phys = conserved dust energy
H_phys = sp.Rational(2,3)*sp.pi*p**2/a - Lam/(8*sp.pi)*a**3
print("\n(1) Deparametrized physical Hamiltonian (dust/cosmic-time gauge, N=1):")
print("    H_phys(a,p_a) =", H_phys, "   (= conserved comoving dust energy rho_d on-shell)")

# Hamilton's equations -> Friedmann
adot = sp.diff(H_phys,p)          # a' = dH/dp
print("    Hamilton: a_dot = dH/dp_a =", adot)
# on-shell H_phys = rho_d  => solve p^2, sub into a_dot^2
psol = sp.solve(sp.Eq(H_phys,rho), p**2)[0]
adot2 = sp.simplify(adot**2).subs(p**2, psol)
adot2 = sp.simplify(adot2)
print("    => a_dot^2 =", adot2)
print("       i.e. (a_dot/a)^2 =", sp.simplify(adot2/a**2), "  = (8pi/3) rho_d/a^3 + Lambda/3  -> FLAT LCDM")

# verify the established trajectory solves it
print("\n(2) Does a(tau)=A sinh^{2/3}(3 tau/2 alpha), alpha=sqrt(3/Lambda), solve the Friedmann eq?")
alpha_val = sp.sqrt(3/Lam)
atau = A*sp.sinh(3*tau/(2*al))**sp.Rational(2,3)
lhs = sp.simplify(sp.diff(atau,tau)**2)
# Friedmann RHS with rho_d fixed so the dust coeff matches: (8pi/3)rho_d = A^3 * Lambda/3 (Nariai-normalized amplitude)
C = A**3*Lam/3
rhs = sp.simplify(C/atau + Lam/3*atau**2).subs(al, alpha_val)
lhs = sp.simplify(lhs.subs(al, alpha_val))
print("    a_dot^2 - [ (A^3 Lambda/3)/a + (Lambda/3) a^2 ] =", sp.simplify(lhs-rhs))
print("    (0 => the sinh^{2/3} flat-LCDM trajectory is exactly the H_phys dynamics in cosmic time tau.)")

print("\n(3) Quantization structure (the resolution of the problem of time):")
print("    Promote H_phys -> operator on L^2((0,inf), da):  i d/dtau Psi(a,tau) = H_phys^hat Psi.")
print("    This is a genuine time-dependent SCHRODINGER equation generating UNITARY tau-evolution,")
print("    NOT the frozen Wheeler-DeWitt constraint H^hat Psi = 0. The foliation is FIXED by the")
print("    absolute clock, so there is a true Hamiltonian and a true time. That IS the problem-of-time")
print("    resolution. (Technical content: operator ordering of p_a^2/a and the self-adjoint extension")
print("    on the half-line; the spectrum is not fabricated here.)")
