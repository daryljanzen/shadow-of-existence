import sympy as sp
print("="*78)
print("E=1 congruence through r=0: is collapse one analytic object with expansion?")
print("="*78)
tau,M,al,u,A = sp.symbols('tau M alpha u A', positive=True)

# E=1 marginally-bound radial geodesic in SdS, f=1-2M/r-r^2/al^2:
#   (dr/dtau)^2 = E^2 - f(r) = 2M/r + r^2/al^2     (master eqn; +/- = expand/collapse)
# Candidate: r(tau) = A sinh^{2/3}(3 tau/2 al),  A^3 = 2 M al^2
print("\n(1) MASTER EQUATION (E=1):  (dr/dtau)^2 = 2M/r + r^2/alpha^2")
print("    same equation governs both signs of dr/dtau -> collapse and expansion are ONE eqn")

# symbolic core: substitute r = A sinh(u)^{2/3}, u = 3 tau/(2 al), A^3 = 2 M al^2
# LHS = (A/al)^2 sinh(u)^{-2/3} cosh(u)^2 ; RHS = (A/al)^2 (sinh^{-2/3} + sinh^{4/3})
sh, ch = sp.symbols('sh ch', positive=True)   # sh=sinh u, ch=cosh u
LHS = (A/al)**2 * sh**sp.Rational(-2,3) * ch**2
RHS = sp.Rational(1,1)*( (2*M)/(A*sh**sp.Rational(2,3)) + A**2*sh**sp.Rational(4,3)/al**2 )
RHS = RHS.subs(M, A**3/(2*al**2))            # impose A^3 = 2 M al^2
core = sp.simplify((LHS-RHS)/((A/al)**2*sh**sp.Rational(-2,3)))   # divide common factor
core = sp.simplify(core.subs(ch**2, 1+sh**2))                    # cosh^2 = 1+sinh^2
print("\n(2) LHS-RHS reduces (after A^3=2M al^2, cosh^2=1+sinh^2) to:", core, " -> identity holds")

# numeric residual at sample tau, BOTH signs (expansion tau>0, collapse tau<0 via even power)
print("\n(3) Numeric residual of the master eqn, alpha=1, 2M=2/(3*sqrt3) (Nariai):")
import math
aln=1.0; twoM=2/(3*math.sqrt(3)); Mn=twoM/2; An=(twoM*aln**2)**(1/3)
def r_of(t):  # sinh^{2/3} as a real EVEN function of t (|sinh|^{2/3}) -> covers tau<0 collapse
    s=math.sinh(3*t/(2*aln)); return An*(abs(s))**(2/3)
def drdt(t,h=1e-6): return (r_of(t+h)-r_of(t-h))/(2*h)
for t in [-2.0,-0.5,0.5,2.0]:
    r=r_of(t); lhs=drdt(t)**2; rhs=twoM/r + r**2/aln**2
    print(f"   tau={t:+.2f}: r={r:.6f}  (dr/dtau)^2={lhs:.6f}  2M/r+r^2={rhs:.6f}  resid={lhs-rhs:+.2e}")

# near tau->0 leading behaviour
print("\n(4) Near tau->0 (small u): sinh u ~ u, so")
r_near = A*( (3*tau/(2*al)) )**sp.Rational(2,3)
r_near = sp.simplify(r_near.subs(A,(2*M*al**2)**sp.Rational(1,3)))
print("    r(tau) ~", r_near, " = (9M/2)^{1/3} tau^{2/3}  (marginally-bound Oppenheimer-Snyder dust)")
print("    check coeff:", sp.simplify(r_near/tau**sp.Rational(2,3)), " vs (9M/2)^(1/3)=",sp.cbrt(sp.Rational(9,2)*M))
print("\n(5) STRUCTURE AT r=0 (tau=0): r ~ |tau|^{2/3} -> branch point; dr/dtau ~ |tau|^{-1/3} -> infinite.")
print("    r(tau)=A sinh^{2/3}(3tau/2al) is EVEN in tau: the tau<0 collapse is the exact")
print("    time-reverse of the tau>0 expansion, glued at r=0. ONE analytic congruence,")
print("    collapse and cosmos its two sides, meeting at the r=0 null boundary.")
