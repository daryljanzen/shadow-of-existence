"""
ruling_swaps.py  --  RESOLVE THE FLAG: who swaps the two null rulings?

Claim to test (against storyboard sec3, which says "R swaps A<->B is wrong / the
A<->B swap is charge-neutral and is sigma's"):

  P3 (l451/l460) and P12 state: BOTH R and T swap the two null rulings, and they
  are DISTINCT reflections -- R spacelike (offset X2, 2M->-2M, species-flipping),
  T timelike (X0, horn-flip, species-preserving). sigma permutes the three ROOTS
  and does NOT swap the rulings (P12: "the two factors act on INDEPENDENT
  structures -- the Weyl S3 on the three roots, the inversion R on the two rulings").

We verify on the doubly-ruled hyperboloid (the ruled three-block P12 works on):
  -X0^2 + X1^2 + X2^2 = 1.
"""
import numpy as np

# ---- the two null ruling families of  -X0^2 + X1^2 + X2^2 = 1 -------------
# At a waist point p(phi) = (0, cos phi, sin phi), a ruling direction d satisfies
# eta(p,d)=0 and eta(d,d)=0. Solve => d = (1, -sin phi, cos phi) [+ family]
#                                      d = (1,  sin phi,-cos phi) [- family]  (up to scale)
eta = np.diag([-1.0, 1.0, 1.0])
def waist(phi):      return np.array([0.0, np.cos(phi), np.sin(phi)])
def dplus(phi):      return np.array([1.0, -np.sin(phi),  np.cos(phi)])
def dminus(phi):     return np.array([1.0,  np.sin(phi), -np.cos(phi)])

def on_surface(X):   return abs(X@eta@X - 1.0) < 1e-9
def is_null(d):      return abs(d@eta@d) < 1e-9
# sanity: the ruling really lies on the surface
for phi in np.linspace(0, 2*np.pi, 7):
    p=waist(phi)
    for d in (dplus(phi), dminus(phi)):
        assert is_null(d)                      # d is null
        assert abs(p@eta@d) < 1e-9             # eta(p,d)=0
        for s in (-1.3, 0.7, 2.0):
            assert on_surface(p+s*d)
print("[ok] both null ruling families verified to lie on the hyperboloid.")

def family_of(base, direc):
    """Return +1 or -1: which ruling family the null line (base,direc) belongs to,
    by matching its direction (up to sign/scale) to d+/d- at its waist crossing."""
    # the line's waist crossing is where X0=0: base + s*direc has X0=0 => s=-base0/direc0
    s = -base[0]/direc[0]
    X = base + s*direc
    phi = np.arctan2(X[2], X[1])
    dp, dm = dplus(phi), dminus(phi)
    # normalise directions (fix X0=+1) and compare
    v  = direc/direc[0]
    for fam, dd in ((+1, dp/dp[0]), (-1, dm/dm[0])):
        if np.allclose(v, dd, atol=1e-7): return fam
    return 0

def swaps_rulings(Lmat, label):
    """Does linear map L send ruling-family (+) to (-)? Test on several lines."""
    verdicts=set()
    for phi in np.linspace(0.1, 2*np.pi-0.1, 8):
        p=waist(phi)
        for fam0, d in ((+1, dplus(phi)), (-1, dminus(phi))):
            Lp, Ld = Lmat@p, Lmat@d
            if not on_surface(Lp):
                verdicts.add("not-a-symmetry"); continue
            fam1 = family_of(Lp, Ld)
            verdicts.add("swap" if fam1==-fam0 else ("keep" if fam1==fam0 else "?"))
    v = verdicts - {"?"}
    print(f"  {label:34s}: {sorted(verdicts)}")
    return v=={"swap"}

print("\n--- action on the two ruling families ---")
T   = np.diag([-1.0, 1.0, 1.0])   # time reflection  X0 -> -X0
R   = np.diag([ 1.0, 1.0,-1.0])   # transverse spacelike reflection X2 -> -X2  (the offset/mass reflection on the block)
Rax = np.diag([ 1.0,-1.0, 1.0])   # reflection along the point's own axis X1
RT  = T@R                          # composition
sT = swaps_rulings(T,  "T   = X0->-X0  (det %+d)"%round(np.linalg.det(T)))
sR = swaps_rulings(R,  "R   = X2->-X2  (det %+d)"%round(np.linalg.det(R)))
sX = swaps_rulings(Rax,"X1->-X1        (det %+d)"%round(np.linalg.det(Rax)))
sRT= swaps_rulings(RT, "R.T            (det %+d)"%round(np.linalg.det(RT)))
# a genuine rotation/boost (det +1) for contrast
th=0.7; Boost=np.array([[np.cosh(th),np.sinh(th),0],[np.sinh(th),np.cosh(th),0],[0,0,1.0]])
sBo= swaps_rulings(Boost,"boost in (X0,X1) (det %+d)"%round(np.linalg.det(Boost)))
print(f"\n  KEY FACT: swaps the two rulings  <=>  det = -1 (orientation-reversing).")
print(f"  det-(-1) reflections T,R,axis all SWAP; det-(+1) maps (R.T, boost) KEEP.")
assert sT and sR and sX and not sRT and not sBo

print("\n--- the A<->B swap of the strung worldline is tau -> -tau ---")
# X(tau) = e^{tau} A + e^{-tau} B ; swapping A<->B:
# X_swapped(tau) = e^{tau} B + e^{-tau} A = e^{-(-tau)} A + e^{(-tau)}... = X(-tau)
import sympy as sp
tau = sp.symbols('tau', real=True)
A, B = sp.symbols('A B')  # symbolic placeholders (vectors); track coefficients
Xtau      = sp.exp(tau)*A + sp.exp(-tau)*B
Xswap     = sp.exp(tau)*B + sp.exp(-tau)*A       # A<->B
Xminustau = Xtau.subs(tau, -tau)
print("  X(tau) with A<->B :", Xswap)
print("  X(-tau)           :", sp.expand(Xminustau))
assert sp.simplify(Xswap - Xminustau)==0
print("  [ok] A<->B swap == tau -> -tau  (time reversal of the worldline).")
print("       tau->-tau keeps the worldline at the same r (same sign(r)) => SPECIES-PRESERVING.")
print("       So the A<->B swap of ONE worldline is the T-flavoured ruling swap, NOT sigma,")
print("       and NOT R (R's ruling swap comes WITH 2M->-2M, i.e. a species flip).")

print("""
VERDICT  (the resolution)
  The ruling-swap is NOT a distinguishing property: EVERY orientation-reversing
  isometry (det = -1) swaps the two null rulings -- T does, R does, any reflection
  does. What tells the reflections apart is their OTHER (non-ruling) action:
    - R (spacelike offset X2 -> -X2): 2M -> -2M -- SPECIES-FLIPPING (matter<->antimatter,
      3 <-> 3bar). The mass/species reflection, the D6 outer Z2.
    - T (timelike X0 -> -X0): horn-flip -- SPECIES-PRESERVING. The worldline's time reversal.
    - sigma (Weyl): permutes the three ROOTS at fixed 2M -- charge-neutral; P12 puts it
      on the roots, R on the rulings, as INDEPENDENT factors.
  And the A<->B swap of the strung worldline X(tau)=e^{tau}A+e^{-tau}B is exactly
  tau -> -tau = T: species-preserving, the charge-neutral swap the storyboard sensed.

  => THE CORPUS (P3 l451/l460, P8, P12) IS CORRECT and needs no change: R swaps the
     rulings (with a species flip); T swaps them (species-preserving); P3 already says
     "both swap the rulings" and distinguishes them. The A<->B-of-a-worldline swap is T.
  => THE STORYBOARD sec3 NOTE is the outlier and is wrong on ONE substantive point:
     "the corpus's 'R swaps A<->B' is wrong" -- NO, R does swap the rulings. The
     storyboard mistook a GENERIC property (every reflection swaps them) for a
     distinguishing one, and so tried to deny it of R. The species content, not the
     ruling-swap, is what separates R from the charge-neutral swaps (sigma, T).
""")
print("ALL CHECKS PASSED.")
