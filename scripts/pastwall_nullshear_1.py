import sympy as sp

print("="*78)
print("PAST THE WALL — probe 0: is the de Sitter substrate's null ruling SHEAR-FREE?")
print("Crux for the candidate. type N (past wall) is alg. special => shear-free PND")
print("(Goldberg-Sachs); the D->I 'shear' reaches type I (WITHIN range). Verify the")
print("substrate ruling's optical shear from scratch on dS.")
print("="*78)

t, r, th, ph, al = sp.symbols('t r theta phi alpha', positive=True)
f = 1 - r**2/al**2                       # pure de Sitter substrate (M=0), static chart
coords = [t,r,th,ph]
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
ginv = g.inv()

# outgoing radial null congruence k^a = (1/f, 1, 0, 0):  null & geodesic on dS
kup = sp.Matrix([1/f, 1, 0, 0])
nullcheck = sp.simplify((kup.T*g*kup)[0])
print("\n[0] k null?  g_ab k^a k^b =", nullcheck, " (0 => null)")

# Christoffels
def christ(g,ginv,x):
    n=len(x); G=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                G[a][b][c]=sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d])) for d in range(n))/2)
    return G
G = christ(g,ginv,coords)

# geodesic check: k^b nabla_b k^a = (kappa) k^a  (affine up to rescaling)
kdown = g*kup
acc = []
for a in range(4):
    s = sum(kup[b]*(sp.diff(kup[a],coords[b]) + sum(G[a][b][c]*kup[c] for c in range(4))) for b in range(4))
    acc.append(sp.simplify(s))
print("[1] geodesic accel k^b D_b k^a =", [sp.simplify(x) for x in acc],
      " (proportional to k^a => geodesic; here non-affine param ok)")

# nabla_a k_b  (covariant derivative of the 1-form k_b)
def cov_kdown(kdown):
    n=4; Dk=sp.zeros(n,n)
    for a in range(n):
        for b in range(n):
            Dk[a,b]=sp.simplify(sp.diff(kdown[b],coords[a]) - sum(G[c][a][b]*kdown[c] for c in range(n)))
    return Dk
Dk = cov_kdown(kdown)

# transverse 2-metric on the (theta,phi) screen; project the symmetric part of Dk
# expansion theta = h^{ab} D_a k_b ; shear = trace-free transverse symmetric part.
# screen = the 2-sphere (indices 2,3). For a radial null cong this is the natural screen.
hT = sp.diag(r**2, r**2*sp.sin(th)**2)          # transverse metric (theta,phi)
hTinv = hT.inv()
S = sp.zeros(2,2)
for i,a in enumerate([2,3]):
    for j,b in enumerate([2,3]):
        S[i,j]=sp.simplify((Dk[a,b]+Dk[b,a])/2)
print("\n[2] transverse symmetric Dk_(ab) on the (theta,phi) screen:")
print("    S =", S)
theta_exp = sp.simplify(sum(hTinv[i,j]*S[i,j] for i in range(2) for j in range(2)))
print("    expansion  theta = h^ab S_ab =", theta_exp, " (nonzero => expanding ruling)")
# shear = S_ab - (1/2) theta h_ab ; check it vanishes
shear = sp.zeros(2,2)
for i in range(2):
    for j in range(2):
        shear[i,j]=sp.simplify(S[i,j]-sp.Rational(1,2)*theta_exp*hT[i,j])
print("    SHEAR sigma_ab = S_ab - 1/2 theta h_ab =", shear)
sig2 = sp.simplify(sum(hTinv[i,k]*hTinv[j,l]*shear[i,j]*shear[k,l] for i in range(2) for j in range(2) for k in range(2) for l in range(2)))
print("    |sigma|^2 =", sig2, "   (0 => SHEAR-FREE)")

print("\n" + "="*78)
print("READING (grounded, stated for reversal):")
print("="*78)
print("""
 - The substrate's radial null ruling is SHEAR-FREE (|sigma|^2=0) and EXPANDING
   (theta != 0): confirmed from scratch, consistent with the corpus (range sec:petrov,
   "the substrate's null rulings are shear-free").
 - So the notebook's past-the-wall candidate, framed as "the D->I shear ... advancing a
   shearing profile", is aimed wrong if "past the wall" means type N: the optical D->I
   SHEAR reaches type I, which is WITHIN the range. Type N is algebraically special, hence
   (Goldberg-Sachs) sits on a SHEAR-FREE null geodesic congruence -- the SAME shear-free
   structure the substrate's null rulings already have. The "locally varying orientation"
   that type N needs comes from the TRANSVERSE WAVE PROFILE carried on a shear-free ruling,
   NOT from optical shear of the congruence (which would only reach type I).
 - REFINED candidate (supersedes the notebook's shear framing, for reversal): the way past
   the wall, if generative at all, is a TRANSVERSE WAVE PROFILE advanced along the
   substrate's shear-free, expanding null ruling -- i.e. a type-N de Sitter wave aligned
   with a substrate null generator. The open question becomes sharp: is such a wave a CUT
   (generated along the ruling) or only ORDINARY EVOLUTION of the leaf (range sec:wall's
   settled reading -- the operator's generative boundary)? That is the next computation:
   build the type-N dS wave on a shear-free null ruling from scratch and test which it is.
""")
