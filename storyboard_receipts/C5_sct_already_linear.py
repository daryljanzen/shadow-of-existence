"""TWO CLOSURES.
 (A) X3r's open question: sin is real on the real axis AND on every line Re z = pi/2 + k.pi.
     The crossings are at z = pi/2 + k.pi.  Are the odd ones the corpus's BACK seam as the even
     ones are its FRONT?
 (B) The conformal queue's last entry: 'C1 computed the LINEAR conformal maps only; the SPECIAL
     CONFORMAL TRANSFORMATIONS are untested -- the one place the conformal field could still bite.'"""
import numpy as np, sympy as sp
print("="*78); print("(A) THE REALITY-LINE CROSSINGS OF sin"); print("="*78)
print("\n  crossings at z = pi/2 + k.pi, and r = sin z there (gauge alpha=1):")
_cross=[]                                     # r2376+c54.159: keep the printed crossing values
for k in range(-1,4):
    z=np.pi/2+k*np.pi
    print(f"   k={k:+d}:  z = {z:+.6f},  r = sin z = {np.sin(z):+.1f}  = {'+alpha' if np.sin(z)>0 else '-alpha'}")
    _cross.append((k, z, np.sin(z)))
# r2376+c54.159 -- PINS (A)'s first claim: the reality-line crossings sit at z = pi/2 + k.pi with
# z(k=-1) = -1.570796 and z(k=+3) = +10.995574, and r = sin z ALTERNATES +alpha, -alpha there --
# never anything between.  (Five crossings, k = -1..3.)
assert len(_cross)==5 and abs(_cross[0][1] + 1.5707963268) < 1e-9, _cross[0]
assert abs(_cross[4][1] - 10.9955742876) < 1e-9, _cross[4]
assert all(abs(abs(s) - 1.0) < 1e-12 for _,_,s in _cross), _cross          # |r| = alpha at every crossing
assert [1 if s>0 else -1 for _,_,s in _cross] == [-1,1,-1,1,-1], _cross    # and it alternates
print("\n  So the crossings alternate r = +alpha, -alpha.  ARE THOSE SEAMS?")
print("  Confirmation 1/3 -- section 0: a seam is a turning point of the slicing curve, a zero of f.")
print("  For the DE SITTER member the mass vanishes, so the horizon cubic (gauge alpha=1) is")
r=sp.symbols('r'); cub=r**3-r
print(f"     r^3 - r = 0   ->  roots r = {sp.solve(cub, r)}")
print("  *** THE TWO NONZERO ROOTS ARE EXACTLY r = +alpha AND r = -alpha -- the crossings. ***")
print("  And the third root r = 0 is NOT a crossing: sin vanishes on the REAL AXIS, away from them.")
# r2376+c54.159 -- PINS (A)'s reading: the de Sitter horizon triple is EXACTLY {-alpha, 0, +alpha}
# (gauge alpha=1), so the two nonzero roots coincide with the crossing values just pinned and the
# third root is the r = 0 branch point, which is NOT one of them.
assert sorted(sp.solve(cub, r)) == [-1, 0, 1], sp.solve(cub, r)
assert sorted({s for _,_,s in _cross}) == [-1.0, 1.0], _cross     # 0 is not a crossing value
print("\n  READ IT: for the de Sitter member the horizon triple is {+alpha, 0, -alpha}, and")
print("    +alpha  = the de Sitter horizon / equatorial-xi seam  (section 0's r entry, verbatim)")
print("    -alpha  = its backward-radial partner, the R-image")
print("    0       = the back-seam branch point, on the real axis")
print("  So the reality GRID sorts the de Sitter triple by TYPE: the two R-conjugate horizons sit at")
print("  crossings of two reality lines; the branch point sits on one reality line only.")
print("  *** The alternation +alpha/-alpha IS the R-conjugation, read on the grid. ***")

print("\n" + "="*78); print("(B) THE SPECIAL CONFORMAL TRANSFORMATIONS"); print("="*78)
print("""
  Confirmation 4 -- state the object before running.  The classical fact:
    THE CONFORMAL GROUP OF R^{p,q} IS O(p+1,q+1), ACTING *LINEARLY* ON THE NULL CONE IN R^{p+1,q+1}.
  Translations, rotations, dilations AND special conformal transformations are all linear there; an
  SCT looks non-linear only in an affine chart of the cone's projectivisation.  Demonstrated:
""")
n=2
def Nl(x):
    x=np.atleast_1d(np.asarray(x,float)); return np.concatenate([[1.0], x, [x@x]])
def Qf(V):
    u=V[0]; xx=V[1:-1]; v=V[-1]; return xx@xx - u*v
def sct(x,b):
    x=np.asarray(x,float); b=np.asarray(b,float)
    d=1-2*(b@x)+(b@b)*(x@x); return (x - b*(x@x))/d
def S(b):
    b=np.asarray(b,float); M=np.zeros((n+2,n+2))
    M[0,0]=1; M[0,1:n+1]=-2*b; M[0,n+1]=b@b
    M[1:n+1,1:n+1]=np.eye(n); M[1:n+1,n+1]=-b; M[n+1,n+1]=1
    return M
b=np.array([0.37,0.12])
_sct=[]                                        # r2376+c54.159: keep the printed ratios
for t in [np.array([0.3,-1.1]), np.array([2.0,0.5]), np.array([-1.4,2.2])]:
    L=S(b)@Nl(t); R=Nl(sct(t,b)); ratio=L/R
    print(f"   x={np.round(t,2)}:  S(b).N(x)/N(SCT x) = {np.round(ratio,9)}"
          f"   constant? {np.allclose(ratio, ratio[0])}   Q preserved? {abs(Qf(L))<1e-9}")
    _sct.append((ratio, abs(Qf(L))))
# r2376+c54.159 -- PINS (B)'s claim, the closure of the conformal queue: the matrix S(b) acting
# LINEARLY on the null cone reproduces the SCT up to an overall scale on every test point -- the
# printed ratios 1.238690, 0.043025, 2.536840, each constant across all four cone coordinates --
# and the image stays ON the cone (Q = 0).  So the SCT is already inside the linear group.
assert len(_sct)==3, _sct
assert all(np.allclose(ra, ra[0]) for ra,_ in _sct), _sct           # linear: one scale, not four
assert all(q < 1e-9 for _,q in _sct), _sct                          # and Q is preserved
assert abs(_sct[0][0][0] - 1.238690) < 1e-6, _sct[0][0]
assert abs(_sct[1][0][0] - 0.043025) < 1e-6, _sct[1][0]
assert abs(_sct[2][0][0] - 2.536840) < 1e-6, _sct[2][0]
print("""
  *** THE SCT IS A LINEAR MAP ON THE CONE, PRESERVING Q. ***
  So the 'special' in 'special conformal transformation' is an artefact of the affine chart.  On the
  null cone the WHOLE conformal group is O(n+1,1) acting linearly.  C1 computed the linear maps
  preserving the substrate's absolute and got O(5,1) x R+.  THE SCTs WERE ALREADY INSIDE IT.
  The conformal queue's last entry -- 'the one place the conformal field could still bite' -- therefore
  closes: there is no untested remainder.  C1's result was the whole conformal group all along.
""")
print("="*78)
