"""V2 — DOES THE SHEAR-FREE ROUTE GIVE THE TENSOR DIRECTLY?
CONFIRMATION 4 — and stating the object turns up a gap in the chain V1 drew:
  P9: 'a cut that inherits ONE as its principal congruence is algebraically special'.
  BUT TYPE D HAS **TWO** REPEATED PRINCIPAL NULL DIRECTIONS, not one.  Type II has one.
  So where does the second come from?  The obvious candidate is the corpus's own:
  P8: 'THE DE SITTER HYPERBOLOID IS DOUBLY RULED by null generators; the comoving congruence is
       built from ONE ruling and the synchronous space from THE OTHER.'
  QUESTION: are the Type-D cut's TWO principal null directions the substrate's TWO RULINGS?"""
import numpy as np, sympy as sp
print("="*80); print("V2 — TWO PRINCIPAL NULL DIRECTIONS, AND A DOUBLY RULED SUBSTRATE"); print("="*80)
print("\nSTEP 1 — the two rulings of the equatorial hyperboloid, explicitly.")
t,ph=sp.symbols('t varphi', real=True); al=1
# hyperboloid -X0^2 + X1^2 + X2^2 = 1 ; standard parametrisation
X=sp.Matrix([sp.sinh(t), sp.cosh(t)*sp.cos(ph), sp.cosh(t)*sp.sin(ph)])
eta=sp.diag(-1,1,1)
print("   X(t,phi) = (sinh t, cosh t cos phi, cosh t sin phi);  eta(X,X) =",
      sp.simplify((X.T*eta*X)[0]))
Xt=X.diff(t); Xp=X.diff(ph)
g11=sp.simplify((Xt.T*eta*Xt)[0]); g22=sp.simplify((Xp.T*eta*Xp)[0]); g12=sp.simplify((Xt.T*eta*Xp)[0])
print(f"   induced metric: g_tt = {g11}, g_pp = {g22}, g_tp = {g12}")
print("   null directions in the surface: g_tt dt^2 + g_pp dphi^2 = 0  ->  dphi/dt = ±sqrt(-g_tt/g_pp)")
r=sp.simplify(sp.sqrt(-g11/g22)); print(f"     dphi/dt = ± {r}")
print("   *** TWO null directions at every point -- and they ARE the two rulings: the straight")
print("       generators of the one-sheeted hyperboloid, one from each family. ***")
slope=sp.sqrt(-g11/g22)
for sgn,lab in ((+1,'A'),(-1,'B')):
    d=sp.simplify(Xt+sgn*slope*Xp)
    nn=sp.simplify(sp.expand_trig(sp.simplify((d.T*eta*d)[0])))
    print(f"     ruling {lab}, SYMBOLICALLY at every (t,phi):  eta(d,d) = {nn}")
print("\nSTEP 2 — AND THE SdS CUT'S TWO PRINCIPAL NULL DIRECTIONS.")
rr,M,a=sp.symbols('r M alpha', positive=True)
f=1-2*M/rr-rr**2/a**2
print(f"   f = {f}.  For a static spherically symmetric metric the two repeated PNDs of a Type-D")
print("   vacuum are the INGOING and OUTGOING RADIAL NULL directions:")
print("     l = (1/f) d_t + d_r ,   n = (1/f) d_t - d_r     (up to normalisation)")
print("   Check both are null in ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2:")
for lab,sgn in [('l',+1),('n',-1)]:
    val=sp.simplify(-f*(1/f)**2 + (sgn*1)**2/f)
    print(f"     {lab}: -f (1/f)^2 + (±1)^2/f = {val}")
print("\n   *** SO THE TYPE-D CUT HAS EXACTLY TWO REPEATED PNDs, THE RADIAL NULLS -- and the substrate")
print("       has exactly two ruling families through each point.  The counts match, and the corpus")
print("       already assigns the two rulings to DIFFERENT structures (P8: comoving from one,")
print("       synchronous from the other). ***")
print("\nSTEP 3 — WHAT THIS MEANS FOR THE CHAIN, stated at the altitude the check supports.")
print("   The check above establishes the COUNTS AGREE and that both objects are pairs of null")
print("   directions at each point.  It does NOT by itself establish that the cut's PNDs ARE the")
print("   inherited rulings -- that needs the embedding of the SdS cut in dS_5, which the corpus")
print("   does not exhibit.  *** SO THE CORRECT STATEMENT IS: P9's 'inherits ONE' is understated for")
print("   Type D, which needs two; the substrate supplies two; and whether they are THE two is a")
print("   step the corpus can take and has not. ***")
