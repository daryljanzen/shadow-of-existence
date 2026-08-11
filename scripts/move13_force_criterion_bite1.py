import sympy as sp
# FORCE-vs-ADMIT, bite 1: is P4's branched-cover monodromy a quantization-FORCING obstruction,
# or a trivial/gauge cover (ADMIT-only)? Criterion: a nontrivial monodromy on a classical
# PERIOD forces single-valuedness -> integrality (Bohr-Sommerfeld/holonomy). Test against the
# built horizon cubic. Allowed to return ADMIT.
r, M = sp.symbols('r M', real=True)                       # gauge alpha=1
cubic = r**3 - r + 2*M                                     # roots sum 0 = A2; P4's cover base = M-line
disc  = sp.discriminant(cubic, r)
print("cubic:", cubic, "  discriminant(M):", sp.factor(disc))
M_branch = sp.solve(sp.Eq(disc,0), M)
print("branch points (double root / Nariai):", M_branch)

# local structure at a branch point: how do the colliding roots behave? (ramification order)
Mb = sp.Rational(1,1)*M_branch[1]      # +Nariai (physical, M>0): M_N = 1/(3 sqrt3)
print("\nphysical Nariai M_N =", sp.nsimplify(Mb), "=", sp.N(Mb,6))
# expand roots near M_N: r = r_N + eps  -> the two colliding roots split as +/- sqrt(M_N - M)
rN = sp.solve(cubic.subs(M,Mb), r)
print("roots at Nariai:", rN, " (double root = ramification point)")
eps = sp.symbols('epsilon', positive=True)
# substitute M = M_N - eps, find how the double root splits
roots_near = sp.solve(cubic.subs(M, Mb-eps), r)
split = [sp.series(rt, eps, 0, 2).removeO() for rt in roots_near]
print("roots for M=M_N-eps (leading split):")
for s in split: print("   ", sp.simplify(s))

print("""
READING (criterion, honest):
- The two colliding roots split as +/- sqrt(eps) = +/- sqrt(M_N - M): a SQUARE-ROOT branch point.
  Encircling M_N once swaps them -> local monodromy = a transposition, order 2 (Z/2). Global deck = S_3 (P4).
- So the cover IS nontrivially monodromic (not a trivial 3-sheet split). That clears the FIRST gate of FORCE:
  a classical quantity that is a function of the *individual* root (a single horizon's data) is genuinely
  MULTI-VALUED over the M-line -- single-valuedness is obstructed.
- BUT multi-valued != quantization-forcing. The FORCE step needs a *period* (a closed action integral
  over the cover) whose monodromy is the obstruction, and whose single-valuedness forces oint p dq in 2*pi*Z.
  S_3-symmetric functions of the roots (elementary symmetric polys = the cubic's coefficients) are
  SINGLE-VALUED (monodromy-invariant): the discriminant, the trace, etc. carry no obstruction.
- So the criterion sharpens to a precise, runnable next question:
  Is the relevant classical action/period a SYMMETRIC function of the roots (-> single-valued -> ADMIT only),
  or does the physical phase space genuinely depend on the INDIVIDUAL (monodromic) root data
  (-> obstruction -> candidate FORCE)?  THAT is the bite-2 computation, and it can return ADMIT.
""")
