"""C1 — is the substrate's CONFORMAL group its ISOMETRY group?
Substrate dS_5 = {eta(X,X)=alpha^2} in M^6;  absolute = {eta(X,X)=0}, the null cone.
ORIGIN: storyboard_receipts/C1_conformal_vs_isometric.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
a=1.0; eta=np.diag([-1.,1.,1.,1.,1.,1.])
ip=lambda P,Q: P@eta@Q
rng=np.random.default_rng(3)

def random_O51():
    """a random element of O(5,1): exponentiate a random eta-antisymmetric generator."""
    A=rng.normal(size=(6,6))*0.4
    G=eta@ (A - A.T) /2          # eta-antisymmetric: eta.G antisymmetric
    from scipy.linalg import expm
    return expm(G)

print("="*78); print("C1 — CONFORMAL vs ISOMETRIC ON THE SUBSTRATE"); print("="*78)
print("\nSTEP 1 — which linear maps preserve the ABSOLUTE {eta(X,X)=0}?")
print("  A linear L preserves the null cone iff  eta(Lx,Lx) = f . eta(x,x)  for a scalar f>0,")
print("  i.e. L is a CONFORMAL LINEAR MAP: an O(5,1) element TIMES A DILATION.")
print("  Check on random O(5,1) elements scaled by a factor:")
try:
    from scipy.linalg import expm
    ok=True
except Exception as e:
    ok=False; print("   scipy unavailable:", e)
if ok:
    for k in range(3):
        L=random_O51()
        for lam in [1.0, 1.7, 0.35]:
            M=lam*L
            xs=rng.normal(size=(200,6))
            lhs=np.array([ip(M@x,M@x) for x in xs]); rhs=np.array([ip(x,x) for x in xs])
            ratio=lhs/rhs
            print(f"   L in O(5,1), dilation lambda={lam:5.2f}:  eta(Lx,Lx)/eta(x,x) constant? "
                  f"{np.allclose(ratio, ratio[0], rtol=1e-9)}  value={ratio[0]:.6f}  (= lambda^2 = {lam**2:.6f})")
            # r2376+c54.158 -- pins STEP 1's own printed figures, which are the claim "L is a
            # CONFORMAL linear map, an O(5,1) element TIMES a dilation": across 200 random
            # vectors the ratio eta(Lx,Lx)/eta(x,x) is CONSTANT (a map that merely preserved the
            # cone pointwise-scaled by a non-constant factor would not be linear-conformal), and
            # its value is exactly lambda^2 -- printed 1.000000, 2.890000, 0.122500 for the
            # three dilations 1.00, 1.70, 0.35.  The eta(5,1) signature is what makes the
            # non-constancy a real alternative: rhs = eta(x,x) changes sign over the sample.
            assert np.allclose(ratio, ratio[0], rtol=1e-9), (lam, ratio[:4])
            assert abs(float(ratio[0]) - {1.0: 1.0, 1.7: 2.89, 0.35: 0.1225}[lam]) < 1e-9, (lam, ratio[0])
            assert float(np.min(rhs)) < 0 < float(np.max(rhs))

print("\nSTEP 2 — does a DILATION preserve the SUBSTRATE {eta(X,X)=alpha^2}?")
print("  eta(lambda.X, lambda.X) = lambda^2 . alpha^2.  So a dilation maps the substrate of")
print("  radius alpha to the substrate of radius lambda.alpha -- A DIFFERENT ONE.")
for lam in [1.7, 0.35, 2.0]:
    X=np.array([0.,1,0,0,0,0.])*a
    print(f"   lambda={lam:5.2f}:  eta(X,X)={ip(X,X):.4f} -> eta(lX,lX)={ip(lam*X,lam*X):.4f}"
          f"   alpha: {a:.3f} -> {lam*a:.3f}")
    # r2376+c54.158 -- pins STEP 2, which is C1's actual conclusion: the dilation does NOT preserve
    # the substrate eta(X,X) = alpha^2 = 1.  It carries it to lambda^2 alpha^2 -- printed 2.8900,
    # 0.1225, 4.0000 for lambda = 1.70, 0.35, 2.00 -- i.e. to a DIFFERENT substrate every time,
    # never back to the one it started on.  That is why the conformal group of the absolute is
    # STRICTLY larger than the isometry group of any one substrate, and alpha is what it moves.
    assert abs(ip(lam*X, lam*X) - {1.7: 2.89, 0.35: 0.1225, 2.0: 4.0}[lam]) < 1e-9, lam
    assert abs(ip(lam*X, lam*X) - ip(X, X)) > 1e-3, lam
print("\n" + "="*78)
print("RESULT C1 + C2 — one fact, two questions:")
print("  * ISOMETRY group of the substrate      = O(5,1).")
print("  * CONFORMAL group of the ABSOLUTE      = O(5,1) x R+ (dilations).  STRICTLY LARGER.")
print("  * The extra generator is the DILATION, and it does NOT preserve any single substrate:")
print("    it carries alpha -> lambda.alpha.")
print("  => THE CORPUS'S HOMOTHETY  r0 -> lambda.r0,  alpha -> lambda.alpha  IS EXACTLY THAT")
print("     DILATION.  P5 calls it 'the map between de Sitter representations of different")
print("     alpha' and never says what kind of map it is: it is the conformal group's scale")
print("     factor, and it acts BETWEEN substrates BY CONSTRUCTION rather than by choice.")
print("\n  AND THE CONSEQUENCE FOR alpha, which is Q3's statement seen from the other side:")
print("    Q3: 'the scale is the only free constant a Cayley-Klein construction carries.'")
print("    C1: 'the scale is exactly what the conformal group of the absolute moves.'")
print("    => THE NULL CONE FIXES THE GEOMETRY UP TO alpha, AND alpha IS PRECISELY THE ONE")
print("       THING THE CAUSAL STRUCTURE DOES NOT FIX.  Two statements, one fact.")
print("="*78)
