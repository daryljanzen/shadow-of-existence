import numpy as np, sympy as sp

print("="*70)
print("STEP 1 — the strung comoving worldline on de Sitter, from scratch")
print("="*70)
# 2+1 Minkowski eta=diag(-1,1,1); one-sheeted hyperboloid -X0^2+X1^2+X2^2 = 1 (alpha=1)
# claim to TEST (not assume): X(tau)=e^{tau}A + e^{-tau}B is a unit timelike geodesic ON it,
# for A,B null with 2 eta(A,B)=1.
t = sp.symbols('tau', real=True)
def eta(u,v): return -u[0]*v[0]+u[1]*v[1]+u[2]*v[2]
# pick A future-null, B past-null, solve eta(A,B)=1/2
# A=(1,1,0)/sqrt2 (future null): eta(A,A)= -1/2+1/2=0 ok, future (A0>0)
# B=(-1, b1, b2): past null, need eta(B,B)=0 and eta(A,B)=1/2
a = sp.Matrix([1,1,0])/sp.sqrt(2)
b1,b2 = sp.symbols('b1 b2', real=True)
b = sp.Matrix([-1,b1,b2])
sol = sp.solve([eta(b,b), eta(a,b)-sp.Rational(1,2)], [b1,b2], dict=True)
print("A =", list(a.T), " (future null, eta(A,A)=%s)"%eta(a,a))
print("B solutions with eta(B,B)=0, eta(A,B)=1/2:", sol)
b = b.subs(sol[0])
print("B =", [sp.nsimplify(x) for x in b.T], " eta(B,B)=%s eta(A,B)=%s"%(sp.simplify(eta(b,b)), sp.simplify(eta(a,b))))
X = sp.exp(t)*a + sp.exp(-t)*b
X = sp.Matrix([sp.simplify(x) for x in X])
print("\nX(tau) =", list(X.T))
print("eta(X,X) =", sp.simplify(eta(X,X)), " (on hyperboloid if =1)")
Xd = sp.diff(X,t)
print("eta(Xdot,Xdot) =", sp.simplify(eta(Xd,Xd)), " (unit timelike if =-1)")
# geodesic check: Xddot should be proportional to X (dS geodesic eqn Xddot = (1/alpha^2) X)
Xdd = sp.diff(X,t,2)
print("Xddot - X =", [sp.simplify(x) for x in (Xdd-X).T], " (geodesic if all 0)")

print("\n"+"="*70)
print("STEP 2 — eta(X,B)=e^{tau}: the synchronous space is the B-ruling (test)")
print("="*70)
print("eta(X,B) =", sp.simplify(eta(X,b)), " (claim: = e^{tau})")

print("\n"+"="*70)
print("STEP 3 — R as the generator-swap A<->B acts as tau->-tau on the worldline")
print("="*70)
X_swap = sp.exp(t)*b + sp.exp(-t)*a   # swap A<->B in the string
X_swap = sp.Matrix([sp.simplify(x) for x in X_swap])
X_mtau = X.subs(t,-t); X_mtau=sp.Matrix([sp.simplify(x) for x in X_mtau])
print("X with A<->B  :", list(X_swap.T))
print("X(-tau)       :", list(X_mtau.T))
print("difference    :", [sp.simplify(x) for x in (X_swap-X_mtau).T], " (0 => swap == tau->-tau)")
