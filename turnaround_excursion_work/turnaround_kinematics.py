import sympy as sp
r, tau, M, al = sp.symbols('r tau M alpha', positive=True)
print("="*70); print("(8) THE TWO LEGS ARE POTENTIAL-ZEROS vs KINEMATIC-ZEROS of the E=1 worldline"); print("="*70)
f = 1 - 2*M/r - r**2/al**2
print("  metric lapse   f        = 1 - 2M/r - r^2/a^2   ; horizons  f=0    (SLICING turns: causal)")
print("  E=1 kinetic  (dr/dtau)^2 = E^2 - f = 1 - f = 2M/r + r^2/a^2 ; turnaround 1-f=0 (WORLDLINE turns)")
print("  => horizon cubic = zeros of the LAPSE/potential (causal horizons, the REAL/su(3) leg);")
print("     turnaround cubic = zeros of the E=1 radial KINETIC energy (the congruence's turning,")
print("     the COMPLEX/su(3) leg). Same worldline, two kinds of turning.")

print("="*70); print("(9) CHECK: the sinh^{2/3} expansion law IS the E=1 geodesic (a=1)"); print("="*70)
rexp = (2*M)**sp.Rational(1,3) * sp.sinh(3*tau/2)**sp.Rational(2,3)          # outward leg
lhs = sp.simplify(sp.diff(rexp,tau)**2)
rhs = sp.simplify((2*M/rexp + rexp**2).rewrite(sp.exp))
print("   (dr/dtau)^2 - (1-f)  simplifies to:", sp.simplify(sp.expand_trig(lhs - (2*M/rexp+rexp**2))))
print("   -> 0 confirms r=(2M)^{1/3} sinh^{2/3}(3tau/2) solves (dr/dtau)^2 = 2M/r + r^2 (E=1, a=1).")

print("="*70); print("(10) THE COMPLEX LEG IS THE CONJUGATE-BRANCH (COLLAPSE) PHASE STRUCTURE"); print("="*70)
print("   outward  (expansion): r = +(2M a^2)^{1/3} sinh^{2/3}(3 tau/2a),  Im tau = 0")
print("   inward   (collapse) : r = -(2M a^2)^{1/3} cosh^{2/3}(3 Re tau/2a), Im tau = -pi a/3")
print("   turnaround: cosh(0)=1 -> r = -(2M a^2)^{1/3}  (deepest compression, dr/dtau=0).")
print("   the shift tau -> tau + 2 pi i a/3 multiplies r by e^{2pi i/3} (P7 sec:bead): the turnaround")
print("   cubic's equilateral Z/3 IS the cosmic-time imaginary period. The three sheets = the real")
print("   expansion leg (Im tau=0) + the two conjugate collapse wings (Im tau=+-pi a/3).")
print("   => THE COMPLEX LEG = the collapse-branch kinematics the acoustic driving rides:")
print("      the cosh^{2/3} in-fall/turnaround/re-expansion, turning at r=-(2M a^2)^{1/3}.")
print("   and R (r->-r): +M turnaround (r<0, collapse/antimatter branch) <-> -M (r>0),")
print("      = the su(3) 3<->3bar = the bead's matter<->antimatter branches. ONE parity, both.")
