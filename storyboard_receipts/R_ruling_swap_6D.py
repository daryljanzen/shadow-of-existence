"""
R_ruling_swap_6D.py  --  L4 sub-lines (a) + (b) (built r1326, Arthur).  Companion to
R_gamma5_Cl_derivation.py (which derived, at the tangent-spinor level, that the transverse
cut-normal reflection acts on the cut spinor as gamma^5, GRADING, exchange excluded).

Here we render the two things that receipt honestly left open, in the 6D embedding where the
reflection R = diag(1,1,-1,1,1,1) in O(5,1) actually lives:

  (a) THE BRIDGE.  R, as an isometry of dS_5 = {<X,X>=1} in R^{1,5}, fixes the 4D cut {X_2=0}
      and, on the tangent space at a fixed point, reflects exactly the transverse (X_2, cut-normal)
      direction while fixing the four spacetime legs -- i.e. R RESTRICTS to the very transverse
      tangent reflection whose spinor lift was shown = gamma^5.  So the 6D R and the tangent-level
      gamma^5 are the same operation.

  (b) THE RULING-SWAP (the origin of the old 'exchange' error).  On the ruled section R SWAPS the two
      null-ruling families -- and THIS is what the discarded reading mis-read as a spinor exchange.
      The point: the swap of the rulings (geometric) and the GRADING of chirality (spinor, gamma^5)
      are BOTH true and NOT in tension -- 'R swaps the rulings' does not imply 'R exchanges the Weyl
      components'.  The swap is realised on the cut spinor as gamma^5 (diagonal, grading), by (a) + the
      companion receipt.  That is the exchange reading retired at the level it first went wrong.
"""
import numpy as np
np.set_printoptions(precision=3, suppress=True)

eta = np.diag([-1.,1.,1.,1.,1.,1.])            # R^{1,5}, signature (1,5)
def ip(u,v): return u@eta@v
R6 = np.diag([1.,1.,-1.,1.,1.,1.])             # the corpus's R: flips X_2 (the transverse cut-normal)

results={}
def check(tag,cond): results[tag]=bool(cond); print(f"  [{'PASS' if cond else 'FAIL'}] {tag}")

print("="*80); print("R_ruling_swap_6D  --  (a) bridge to the transverse reflection, (b) ruling swap"); print("="*80)

# R6 is an isometry of R^{1,5} with det -1 (orientation-reversing), so it preserves dS_5.
check("R in O(1,5): R^T eta R = eta", np.allclose(R6.T@eta@R6, eta))
check("det R = -1 (orientation-reversing, in O(5,1)\\SO_0)", np.isclose(np.linalg.det(R6), -1))

# ---- (a) THE BRIDGE: R fixes the 4D cut {X_2=0} and reflects the transverse tangent direction ----
# a sample point on dS_5 with X_2 = 0 (so it is FIXED by R6):
Xstar = np.array([0.,0.,0.,0.,0.,0.]); 
# pick <X,X>=1 with X_2=0: put weight on spacelike X_1
Xstar = np.array([0.0, np.sqrt(1.0), 0.0, 0.0, 0.0, 0.0])   # <X,X> = 0+1+0..=1, X_2=0
check("sample cut point X* is on dS_5 (<X*,X*>=1) and has X_2=0", np.isclose(ip(Xstar,Xstar),1) and Xstar[2]==0)
check("R fixes X* (X* lies in the cut)", np.allclose(R6@Xstar, Xstar))

# tangent space at X*: {v : <X*,v> = 0}, 5-dimensional.  R6 maps it to itself (isometry fixing X*).
# basis of the ambient R^{1,5}; project to tangent; see how R6 acts.
def tangent_basis(X):
    B=[]
    for k in range(6):
        e=np.zeros(6); e[k]=1.0
        v = e - (ip(e,X)/ip(X,X))*X          # project off the normal X
        B.append(v)
    # reduce to a basis (rank 5)
    M=np.array(B); 
    # orthonormal-ish basis via QR on the 6xk transposed (metric-agnostic for span)
    q,_=np.linalg.qr(M.T)
    return q[:, :5]                          # 6x5, columns span the tangent
Tb = tangent_basis(Xstar)
# R6 restricted to the tangent, in the tangent basis:
R_tan = np.linalg.pinv(Tb) @ R6 @ Tb        # 5x5
# eigenvalues of R_tan: should be four +1 (fixed legs) and one -1 (flipped transverse)
ev = np.sort(np.round(np.linalg.eigvals(R_tan).real,6))
check("R on the 4D+1 tangent has eigenvalues {-1,+1,+1,+1,+1}: one flip (transverse), four fixed (legs)",
      np.allclose(ev, [-1,1,1,1,1]))
# and the flipped direction is e_2 (the transverse cut-normal): e_2 is tangent (since <X*,e2>=X*_2=0)
e2=np.array([0,0,1.,0,0,0])
check("the transverse direction e_2 is a tangent vector at X* (<X*,e_2>=0)", np.isclose(ip(Xstar,e2),0))
check("R flips exactly e_2 (R e_2 = -e_2) and fixes the orthogonal cut legs",
      np.allclose(R6@e2, -e2))
print("     => (a) R restricts, at the fixed cut, to the transverse cut-normal reflection")
print("        (four legs fixed, transverse flipped) -- the very reflection whose cut-spinor lift is")
print("        gamma^5 (R_gamma5_Cl_derivation.py).  Bridge established.")

# ---- (b) THE RULING-SWAP on the ruled section (X0,X1,X2): -X0^2+X1^2+X2^2 = 1 ---------------------
print("-"*80)
def neck(p):  return np.array([0.0, np.cos(p), np.sin(p)])      # neck point (X2 = sin p)
def tang(p):  return np.array([0.0, -np.sin(p), np.cos(p)])     # neck tangent
axial = np.array([1.0,0.0,0.0])                                 # timelike X0 axis
eta3 = np.diag([-1.,1.,1.]); ip3=lambda u,v:u@eta3@v
R3 = np.diag([1.,1.,-1.])                                       # R on the section (flips X2)
def rulings(p): return axial+tang(p), axial-tang(p)             # (d_plus, d_minus): the two null rulings

# sanity: the rulings are null and tangent at the neck point
p0=0.7; dP,dM=rulings(p0)
check("ruling directions are null (<d,d>=0) and tangent (<X,d>=0) at the neck",
      np.isclose(ip3(dP,dP),0) and np.isclose(ip3(dM,dM),0)
      and np.isclose(ip3(neck(p0),dP),0) and np.isclose(ip3(neck(p0),dM),0))

# R maps neck(p) -> neck(-p); check whether R pushes the d_plus family to the d_minus family (SWAP)
swap_ok=True; fix_ok=True
for p in np.linspace(0.1,1.4,7):
    dP,dM = rulings(p)
    RdP = R3@dP; RdM = R3@dM
    dPm,dMm = rulings(-p)                          # rulings at the image neck point neck(-p)
    # R(neck(p)) should equal neck(-p):
    if not np.allclose(R3@neck(p), neck(-p)): swap_ok=False
    # is R d_plus(p) proportional to d_minus(-p)?  (that is the SWAP)
    def prop(u,v): return np.linalg.matrix_rank(np.vstack([u,v]),tol=1e-9)==1
    if not (prop(RdP, dMm) and prop(RdM, dPm)): swap_ok=False
    # would 'fix each ruling' look like?  R d_plus(p) prop to d_plus(-p) -- check it is NOT that:
    if prop(RdP, dPm): fix_ok=False
check("R maps neck(p) -> neck(-p) and SWAPS the families: R d_+(p) ~ d_-(-p), R d_-(p) ~ d_+(-p)", swap_ok)
check("R does NOT fix each ruling (it is the orientation-reversing case: det R|section = -1)",
      fix_ok and np.isclose(np.linalg.det(R3),-1))
print("     => (b) R swaps the two null rulings.  Yet by (a)+companion its cut-spinor action is gamma^5,")
print("        DIAGONAL/grading -- NOT an off-diagonal Weyl exchange.  'R swaps the rulings' and 'R grades")
print("        chirality' are both true and not in tension; the old reading wrongly inferred the second")
print("        from the first.  Exchange reading retired at its geometric origin.")

print("="*80)
ok=all(results.values())
print("RESULT:", "ALL PASS -- (a) bridge + (b) ruling-swap rendered; L4 fully worked." if ok
      else "SOME FAILED -- see above.")
print("="*80)
