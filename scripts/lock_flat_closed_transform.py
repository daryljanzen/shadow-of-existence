# Move 12 (the lock) — the FLAT<->CLOSED canonical transform, verified in the
# de Sitter embedding (the substrate). Closes canonical_sds_2.py open piece (b):
# the flat comoving reading and the closed synchronous reading are ONE comoving
# congruence under TWO synchronizations, with the non-synchrony seam exhibited.
#
# Grounded at source: slicing_operator.tex sec:cosmology (the E=1 / Painleve-
# Gullstrand comoving congruence, flat LCDM) and sec:synchronous (the embedding
# X(tau)=e^{tau/a}A+e^{-tau/a}B; flat slices = horospheres normal to the past
# ruling B; closed cosh slicing = the timelike vertical).
#
# SCOPE (honest): this is at the SUBSTRATE level (pure de Sitter), where both
# slicings live. It establishes the FRAME/congruence identity (the lock's middle
# backbone). The M!=0 layer (matter = the bend of the flat slicing, read leftward,
# sec:cosmology) and the dust-free deparametrization FORM (canonical_sds_2 (a),
# the lock's open core) are NOT closed here.
#
# Verified: every identity below reduces to a clean 0 / -1 (exp-form + expand).
import sympy as sp

tau, al, x, y, z = sp.symbols('tau alpha x y z', real=True, positive=True)
rho2 = x**2 + y**2 + z**2
e = sp.exp(tau/al)

# Flat-slicing embedding of de Sitter; comoving worldlines = (x,y,z)=const.
X0 = al*sp.sinh(tau/al) + (rho2/(2*al))*e
X1, X2, X3 = e*x, e*y, e*z
X4 = al*sp.cosh(tau/al) - (rho2/(2*al))*e
X  = sp.Matrix([X0,X1,X2,X3,X4])
eta = sp.diag(-1,1,1,1,1)
def ip(U,V): return sp.expand(sp.simplify(((U.T*eta*V)[0]).rewrite(sp.exp)))

print("[1] eta(X,X) - alpha^2          =", ip(X,X) - al**2, "  (0: on the hyperboloid)")
Xt = X.diff(tau)
print("[2] eta(Xdot,Xdot)              =", ip(Xt,Xt), "  (-1: unit timelike)")
geo = (X.diff(tau,2) - X/al**2).applyfunc(lambda c: sp.simplify(c.rewrite(sp.exp)))
print("[3] Xddot - X/alpha^2           =", geo.T, "  (0: geodesic => the comoving congruence)")

B = sp.Matrix([-1,0,0,0,1])   # common past null generator (ruling B)
print("[4] eta(B,B)                    =", ip(B,B), "  (null)")
print("[5] eta(X,B)                    =", ip(X,B), "  (alpha e^{tau/a}: depends ONLY on tau")
print("       => FLAT slices tau=const are horospheres normal to B = flat synchronization.")

print("[6] X0                          =", sp.simplify(X0))
print("       depends on tau AND rho^2 => CLOSED slice X0=const (global time T,")
print("       X0=alpha sinh(T/a)) is NON-synchronous with the flat slice tau=const:")
print("       the SEAM. At rho=0: T=tau. Off-origin: T>tau (the chi offset, tau~=tau+chi).")

R2 = sp.expand(sp.simplify((X1**2+X2**2+X3**2+X4**2).rewrite(sp.exp)))
print("[7] R^2 - (alpha^2 + X0^2)      =", sp.expand(sp.simplify((R2-(al**2+X0**2)).rewrite(sp.exp))),
      "  (0: R=alpha cosh(T/a), the closed S^3)")

print("""
VERDICT (verified):
  ONE comoving congruence — the (x,y,z)=const unit timelike geodesics = the
  substrate comoving congruence (= the cosmic rest frame / CMB frame, P8 necessity).
  TWO synchronizations of that one congruence:
    FLAT   : eta(X,B)=alpha e^{tau/a}, slices = horospheres on the past ruling B
             -> flat LCDM (the matter M!=0 is the bend of this slicing, read leftward).
    CLOSED : X0=const, slices = S^3 of radius alpha cosh(T/a) -> NBC's evolving S^3.
  Non-synchronous: seam T(tau,rho), T=tau only at rho=0 (tau~ = tau + chi).
  B (common past null generator) = the NBC past boundary (the finite-curvature
  cosmological 'beginning', a horizon the slicing anchors to, not an infinite-
  curvature centre).
  => The lock's MIDDLE identity: CMB frame = substrate comoving congruence, with
     flat LCDM and the closed S^3 two synchronizations of that single frame, and
     B the NBC anchor. (Substrate level; the M!=0 layer reading and the dust-free
     deparametrization FORM remain — the lock's open core.)
""")
