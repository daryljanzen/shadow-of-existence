"""
P13_sigma_lift.py -- verifies sec:sigma (a real involution is not the Wick rotation): the tempting bridge
  "sigma IS the Wick rotation, so the real A_2 skeleton lifts continuously to su(3)" FAILS in embedding
  coordinates. Three operations co-localised at the r=sqrt(3/Lambda) equatorial seam are DISTINCT:
    (sigma)  real Weyl(A_2) reflection of the sky/root plane -- REAL, fixes x_0, preserves BOTH signatures,
             so it is an isometry of the Lorentzian substrate (in O(5,1)); it changes nothing.
    (Wick)   x_0 -> i x_0 -- IMAGINARY, sends eta_L -> eta_E, reaches S^5 with SO(6) sup su(3).
  DISCRIMINATOR: sigma preserves eta_L (stays in so(5,1)); the Wick does NOT (eta_L->eta_E). Reaching
  so(6) sup su(3) REQUIRES leaving eta_L, so sigma cannot be the bridge. CLINCHER (C2): a Lorentzian boost
  M_{05} becomes a real Euclidean ROTATION under the Wick (so(6) created) but stays a BOOST under sigma
  (so(5,1) preserved) -- so sigma cannot supply the so(6)\\so(5) generators su(3) needs. su(3) is faithful
  on R^6 => su(3) not subset so(5), so neither sigma nor the SO(5) seam hosts colour; only the Wick face does.
  A NEGATIVE result: colour-from-geometry VIA THE sigma-LIFT does not hold. [P13 boundary_paper sec:sigma]
STATUS: ✔✔   RUN: python3 P13_sigma_lift.py   RUNTIME: ~2s
DO NOT ASSERT: this does NOT deny colour lives on the Wick SO(6) face (it does); it denies that the REAL
  involution sigma is the operation reaching it. The A_2 skeleton stays real, forced, discrete.
ORIGIN: built new r1383 (sec:sigma "clincher (C2)", computed in embedding coordinates; previously unreceipted).
"""
import numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
etaL=np.diag([-1,1,1,1,1,1]).astype(complex)   # Lorentzian M^{5,1}, dS_5 substrate
etaE=np.diag([ 1,1,1,1,1,1]).astype(complex)    # Euclidean, S^5
print("="*72); print("P13 sec:sigma -- a real involution (sigma) is not the Wick rotation"); print("="*72)

# --- Wick rotation J: x_0 -> i x_0 ---
J=np.diag([1j,1,1,1,1,1])
ok&=check("Wick J=diag(i,1,1,1,1,1) sends eta_L -> eta_E  (J^T eta_L J = eta_E): Lorentzian -> Euclidean",
          np.allclose(J.T@etaL@J, etaE))
ok&=check("Wick J is IMAGINARY (has a non-real entry)", not np.allclose(J.imag,0))

# --- sigma: a genuine Weyl(A_2)-angle real reflection of the (x_1,x_2) root plane, fixing x_0 ---
phi=2*np.pi/3   # A_2 reflection angle (root exchange w <-> pi/3 - w)
refl=np.array([[np.cos(phi), np.sin(phi)],[np.sin(phi), -np.cos(phi)]])  # 2D reflection, det=-1
sigma=np.eye(6,dtype=complex); sigma[1:3,1:3]=refl
ok&=check("sigma is REAL (all entries real)", np.allclose(sigma.imag,0))
ok&=check("sigma is orthogonal & an involution (sigma^2=I)", np.allclose(sigma@sigma,np.eye(6)))
ok&=check("sigma fixes x_0 (row/col 0 = e_0)", np.allclose(sigma[0,:],[1,0,0,0,0,0]) and np.allclose(sigma[:,0],[1,0,0,0,0,0]))
ok&=check("sigma preserves the LORENTZIAN signature (sigma^T eta_L sigma = eta_L) => sigma in O(5,1)",
          np.allclose(sigma.T@etaL@sigma, etaL))
ok&=check("sigma preserves the EUCLIDEAN signature too (sigma^T eta_E sigma = eta_E) => not a signature change at all",
          np.allclose(sigma.T@etaE@sigma, etaE))

# --- DISCRIMINATOR: sigma preserves eta_L, the Wick does not ---
ok&=check("DISCRIMINATOR: the Wick changes eta_L (J^T eta_L J != eta_L) while sigma preserves it => sigma != Wick",
          (not np.allclose(J.T@etaL@J, etaL)) and np.allclose(sigma.T@etaL@sigma, etaL))

# --- CLINCHER (C2): a Lorentzian boost M_{05} -> Euclidean ROTATION under Wick, but stays a BOOST under sigma ---
B=np.zeros((6,6),complex); B[0,5]=1; B[5,0]=1     # boost generator: eta_L-antisymmetric ((eta_L B)^T=-(eta_L B))
def is_etaL_antisym(X): return np.allclose((etaL@X).T, -(etaL@X))
def is_rotation(X):     return np.allclose(X.T, -X)      # eta_E-antisymmetric (real rotation generator)
ok&=check("M_{05} is a genuine Lorentzian boost (eta_L-antisymmetric)", is_etaL_antisym(B))
Bwick = -1j*(np.linalg.inv(J)@B@J)     # conjugate by Wick, strip the i
ok&=check("under the WICK, the boost becomes a REAL Euclidean rotation (so(6) is CREATED)",
          np.allclose(Bwick.imag,0) and is_rotation(Bwick.real))
Bsig = np.linalg.inv(sigma)@B@sigma
ok&=check("under SIGMA, the boost STAYS a Lorentzian boost (so(5,1) preserved -- no so(6) created)",
          is_etaL_antisym(Bsig) and not is_rotation(Bsig.real))

# --- su(3) is faithful on R^6 => not subset so(5): neither sigma nor the SO(5) seam can host colour ---
lam=[np.zeros((3,3),complex) for _ in range(8)]
lam[0][0,1]=lam[0][1,0]=1; lam[1][0,1]=-1j; lam[1][1,0]=1j; lam[2][0,0]=1; lam[2][1,1]=-1
lam[3][0,2]=lam[3][2,0]=1; lam[4][0,2]=-1j; lam[4][2,0]=1j; lam[5][1,2]=lam[5][2,1]=1
lam[6][1,2]=-1j; lam[6][2,1]=1j; lam[7]=np.diag([1,1,-2])/np.sqrt(3)
# realify: the 8 generators i*lambda act on R^6 = C^3; moved real coords:
moved=set()
for a in range(8):
    G=1j*lam[a]
    M=np.zeros((6,6))
    for r in range(3):
        for c in range(3):
            M[2*r,2*c]=G[r,c].real;   M[2*r,2*c+1]=-G[r,c].imag
            M[2*r+1,2*c]=G[r,c].imag; M[2*r+1,2*c+1]=G[r,c].real
    for k in range(6):
        if not np.allclose(M[k,:],0) or not np.allclose(M[:,k],0): moved.add(k)
ok&=check("su(3) is faithful on R^6 (moves all 6 real coords) => su(3) not subset so(5)/S^4; needs so(6)/S^5",
          moved==set(range(6)))
# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `ok`, and pin
# the three things sec:sigma's bounded NEGATIVE rests on, since a green flag alone would not show
# that any of them still says what it said.
#   (1) sigma is a genuine REFLECTION of the root plane at the Weyl(A_2) angle 2pi/3 = 120 degrees:
#       det sigma = -1, with eigenvalues five (+1) and exactly one (-1).  A rotation dressed up as
#       an involution would give det +1 and no fixed hyperplane, and would not be a Weyl element.
#   (2) THE CLINCHER (C2), as numbers rather than as a predicate.  Under the Wick the boost M_05
#       becomes the REAL antisymmetric generator with entries -1 at (0,5) and +1 at (5,0) -- a
#       Euclidean rotation, so so(6) is created.  Under sigma the boost is returned UNCHANGED,
#       entry for entry: sigma commutes with M_05 and creates nothing.  That is why sigma cannot
#       supply the so(6)\so(5) generators, and it is the whole of the negative.
#   (3) su(3) needs all 6 real coordinates (8 generators, R^6 faithful), so so(5)/S^4 is one
#       dimension short and the SO(5) seam cannot host colour either.
assert abs(np.linalg.det(sigma).real + 1) < 1e-12, np.linalg.det(sigma)
assert sorted(np.round(np.linalg.eigvalsh(sigma.real), 9).tolist()) == [-1.0] + [1.0]*5
assert abs(np.degrees(phi) - 120.0) < 1e-12
assert abs(Bwick[0,5] - (-1.0)) < 1e-12 and abs(Bwick[5,0] - 1.0) < 1e-12, Bwick[0,5]
assert np.allclose(Bsig, B) and not np.allclose(Bwick, B)
assert len(lam) == 8 and moved == set(range(6)), moved
assert ok
print("="*72)
print("RESULT:", "ALL PASS -- sigma is a real signature-preserving isometry of the substrate; the Wick is an\n         imaginary signature-change. The boost->rotation clincher shows sigma cannot create the so(6)\\so(5)\n         generators su(3) needs. colour-from-geometry VIA THE sigma-lift does not hold (bounded negative)." if ok else "SOME FAILED")
print("="*72)
