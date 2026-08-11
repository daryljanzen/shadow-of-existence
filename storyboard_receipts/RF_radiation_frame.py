"""RF — THE RADIATION IN ITS OWN FRAME.  Corpus structure (P8 sec:synchronous), normalisation fixed.
  comoving worldline X(tau) strung between null A (future horizon) and null B (COMMON past asymptote);
  synchronous slices = level sets of eta(X,B); 'the synchronous space IS the second ruling'.
QUESTION: what does a null fluid weigh on the slices that ruling defines?"""
import sympy as sp
al,tau=sp.symbols('alpha tau', positive=True)
eta=sp.diag(-1,1,1)
A=sp.Matrix([1,1,0]); B=sp.Matrix([1,-1,0])
print("="*80); print("RF — A NULL FLUID ON THE HOROSPHERES ITS OWN RULING DEFINES"); print("="*80)
X=(al/sp.sqrt(2))*(sp.exp(tau/al)*A + sp.exp(-tau/al)*B/2)
print(f"\n  eta(A,A)={(A.T*eta*A)[0]}  eta(B,B)={(B.T*eta*B)[0]}  eta(A,B)={(A.T*eta*B)[0]}")
print(f"  eta(X,X) = {sp.simplify((X.T*eta*X)[0])}   <- on the hyperboloid")
u=sp.simplify(sp.diff(X,tau))
print(f"  u = dX/dtau,  eta(u,u) = {sp.simplify((u.T*eta*u)[0])}   <- unit timelike")
f=sp.simplify((X.T*eta*B)[0])
print(f"  the synchronous function eta(X,B) = {f}   (P8: constant on each slice)")
print("""
STEP 1 — THE UNIT NORMAL TO THE HOROSPHERES.  n is the gradient of eta(X,B) within the hyperboloid,
  normalised.  Since eta(X,B) is linear in X, its ambient gradient is B itself; projecting onto the
  tangent space of the hyperboloid at X and normalising gives n.
""")
gB=B - ((B.T*eta*X)[0]/al**2)*X          # project B onto T_X(hyperboloid)
nn=sp.simplify((gB.T*eta*gB)[0])
print(f"   projected B:  eta(gB,gB) = {sp.simplify(nn)}")
n=sp.simplify(gB/sp.sqrt(sp.simplify(-nn)))
print(f"   after normalising, eta(n,n) = {sp.simplify((n.T*eta*n)[0])}   <- TIMELIKE unit normal")
print("""
STEP 2 — AND NOW THE ENERGY DENSITY OF A NULL FLUID ON THAT SLICE:  rho_slice = rho (eta(k,n))^2.
""")
for lab,k in [("k = B  (the ruling that DEFINES the slicing)", B),
              ("k = A  (the other ruling, the future horizon)", A)]:
    w=sp.simplify(((k.T*eta*n)[0])**2)
    print(f"   {lab}\n      (eta(k,n))^2 = {sp.simplify(sp.powsimp(w, force=True))}")
wB=sp.simplify(((B.T*eta*n)[0])**2); wA=sp.simplify(((A.T*eta*n)[0])**2)
print(f"\n   ratio  A/B = {sp.simplify(sp.powsimp(wA/wB, force=True))}")
print("""
STEP 3 — READ IT, and do not overreach.
  Neither vanishes.  A null fluid streaming along B does NOT have zero weight on the horospheres B
  defines -- the projection that builds the unit normal from B is what saves it, and n is timelike.
  *** SO THE TEMPTING RESULT -- 'radiation along the slicing ruling does not gravitate' -- IS FALSE,
      and it is worth having checked rather than assumed. ***
  What IS true is the ratio: the two rulings' weights differ by exp(-4 tau/alpha) = a^-4, so the
  a^-4 dilution of radiation appears here as the RELATIVE BOOST BETWEEN THE TWO RULINGS rather than
  as an equation of state.  That is a geometric restatement of standard physics, not a new mechanism.
""")
print("="*80)
