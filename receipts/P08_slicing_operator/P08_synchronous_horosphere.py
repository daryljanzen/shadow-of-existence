"""
P08_synchronous_horosphere.py -- verifies sec:synchronous: the flat synchronous slicing of the de Sitter
  substrate is the horosphere family, strung between two NULL directions. DERIVES from the 5D embedding:
    (i)  the flat-slicing embedding lies on the hyperboloid -X0^2+X1^2+..+X4^2=alpha^2;
    (ii) its INDUCED metric is ds^2=-dtau^2+e^{2 tau/alpha}(dx^2+dy^2+dz^2) -- FLAT (k=0) spatial slices;
    (iii)X(tau)=e^{tau/a}A+e^{-tau/a}B with A,B NULL (eta(A,A)=eta(B,B)=0), eta(A,B)=alpha^2/2 (eq:embed);
    (iv) the "direct computation" eta(X,B)=(alpha^2/2)e^{tau/alpha} -- constant on each tau=const slice, so the
         flat synchronous slices are the LEVEL SETS of eta(X,B); as tau->-inf, eta(X,B)->0 (the horospheres
         pile onto the null plane through B: the cosmological singularity). [P8 slicing_operator sec:synchronous]
STATUS: ✔✔   RUN: python3 P08_synchronous_horosphere.py   RUNTIME: ~5s
CONTROL: eta(X,B) is INDEPENDENT of the transverse x,y,z (same on a whole slice) -- that is why its level
  sets are exactly the flat slices; the comoving-worldline limit recovers X~e^{tau/a}A (future null generator).
ORIGIN: built new r1363 (P8 cited no receipts; the claim is a "direct computation", not a numbered prop).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
al = sp.symbols('alpha', positive=True); tau,x,y,z = sp.symbols('tau x y z', real=True)
u = x**2+y**2+z**2
X0 = al*sp.sinh(tau/al) + sp.exp(tau/al)*u/(2*al)
X1 = al*sp.cosh(tau/al) - sp.exp(tau/al)*u/(2*al)
X2, X3, X4 = sp.exp(tau/al)*x, sp.exp(tau/al)*y, sp.exp(tau/al)*z
X=[X0,X1,X2,X3,X4]; eta=sp.diag(-1,1,1,1,1)
print("="*70); print("P08 synchronous / horosphere: the flat de Sitter slicing between two null directions"); print("="*70)
# (i) on the hyperboloid
onhyp=sp.simplify(sp.expand((-X0**2+X1**2+X2**2+X3**2+X4**2).rewrite(sp.exp)))
ok&=check("flat-slicing embedding lies on the hyperboloid -X0^2+..+X4^2 = alpha^2", sp.simplify(onhyp-al**2)==0)
# (ii) induced metric = -dtau^2 + e^{2 tau/a}(dx^2+dy^2+dz^2) : FLAT slices
q=[tau,x,y,z]
gind=sp.Matrix(4,4, lambda i,j: sp.simplify(sp.expand((sum(eta[m,m]*sp.diff(X[m],q[i])*sp.diff(X[m],q[j]) for m in range(5))).rewrite(sp.exp))))
tgt=sp.diag(-1, sp.exp(2*tau/al), sp.exp(2*tau/al), sp.exp(2*tau/al))
ok&=check("induced metric = -dtau^2 + e^{2 tau/a}(dx^2+dy^2+dz^2)  -- FLAT (k=0) synchronous slices (DERIVED)",
          sp.simplify(gind-tgt)==sp.zeros(4))
# (iii) the two null directions A (tau->+inf) and B (tau->-inf)
A=sp.Matrix([al/2, al/2, 0,0,0]); B=sp.Matrix([-al/2, al/2, 0,0,0])
def dot(P,Q): return sum(eta[m,m]*P[m]*Q[m] for m in range(5))
ok&=check("A,B are NULL (eta(A,A)=eta(B,B)=0) and eta(A,B)=alpha^2/2",
          sp.simplify(dot(A,A))==0 and sp.simplify(dot(B,B))==0 and sp.simplify(dot(A,B)-al**2/2)==0)
# comoving worldline (x=y=z=0): X -> e^{tau/a} A as tau->+inf
Xw=[Xi.subs({x:0,y:0,z:0}) for Xi in X]
lead=sp.Matrix([sp.limit(sp.simplify(Xw[i]/sp.exp(tau/al)), tau, sp.oo) for i in range(5)])
ok&=check("comoving worldline X -> e^{tau/a} A as tau->+inf (asymptotes the future null generator A)",
          sp.simplify(lead-A)==sp.zeros(5,1))
# (iv) the direct computation eta(X,B) = (alpha^2/2) e^{tau/a}, INDEPENDENT of x,y,z
Xv=sp.Matrix(X); etaXB=sp.simplify(dot(Xv,B))
ok&=check("direct computation: eta(X,B) = (alpha^2/2) e^{tau/a}  (proportional to e^{tau/a})",
          sp.simplify(etaXB-(al**2/2)*sp.exp(tau/al))==0)
ok&=check("eta(X,B) is INDEPENDENT of transverse x,y,z => its level sets ARE the flat tau=const slices",
          sp.diff(etaXB,x)==0 and sp.diff(etaXB,y)==0 and sp.diff(etaXB,z)==0)
ok&=check("as tau->-inf, eta(X,B)->0 (horospheres pile onto the null plane through B: cosmological singularity)",
          sp.limit(etaXB, tau, -sp.oo)==0)
print("="*70)
print("RESULT:", "ALL PASS -- the flat synchronous slicing is the horosphere family: e^{2 tau/a} flat slices\n         derived from the 5D embedding, strung between two null directions A,B, with eta(X,B)=(a^2/2)e^{tau/a}\n         labelling the slices and vanishing at the tau->-inf singularity." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   AND THE HOROSPHERE LABEL EVALUATED ON A SLICE, which is the 'direct computation' the section
#   rests on.  At alpha = 2 and tau = 2 ln 2 (so e^{tau/alpha} = 2, at transverse x=y=z=1):
#     eta(A,B)   = alpha^2/2                   = 2.0     (the two null directions' pairing)
#     eta(X,B)   = (alpha^2/2) e^{tau/alpha}   = 4.0     (the slice's label)
#     g_xx       = e^{2 tau/alpha}             = 4.0     (the flat slice's scale factor squared)
_pt = {al: sp.Integer(2), tau: 2*sp.log(2), x: 1, y: 1, z: 1}
_AB = float(sp.simplify(dot(A, B)).subs(al, 2))
assert abs(_AB - 2.0) < 1e-12, _AB
_lab = float(sp.simplify(etaXB.subs(_pt)))
assert abs(_lab - 4.0) < 1e-12, _lab
_gxx = float(sp.simplify(gind[1, 1].subs(_pt)))
assert abs(_gxx - 4.0) < 1e-12, _gxx
assert abs(float(sp.simplify(gind[0, 0])) - (-1.0)) < 1e-12    # synchronous: lapse exactly 1
#   the label doubles per alpha ln 2 of proper time and NEVER vanishes at finite tau -- the
#   singularity is the tau -> -inf end, not a horizon at finite label.
_prev = float(sp.simplify(etaXB.subs({al: sp.Integer(2), tau: 0, x: 1, y: 1, z: 1})))
assert abs(_prev - 2.0) < 1e-12, _prev                         # eta(X,B) = alpha^2/2 at tau = 0
assert abs(_lab/_prev - 2.0) < 1e-12, (_lab, _prev)            # doubles per alpha ln 2 of tau
assert _prev > 0.0 and sp.limit(etaXB, tau, -sp.oo) == 0
