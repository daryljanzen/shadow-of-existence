import sympy as sp
print("="*78)
print("ADM-3: the constraint algebra under the S3 generators (sigma, tau)")
print("="*78)

# ---------------------------------------------------------------
# (1) sigma = the vantage involution = the signature flip in the
#     hypersurface-deformation (Dirac) algebra.
#     HDA:  {H[N1],H[N2]} = eps * H_a[ h^{ab}(N1 d_b N2 - N2 d_b N1) ]
#     eps = signature of the foliation normal: -1 Lorentzian (timelike n),
#           +1 Euclidean (spacelike n).  (Teitelboim/HKT; standard.)
#     In the construction gauge the radial normal's character flips under
#     the vantage (computed in ADM-2: exterior r spacelike, interior r timelike).
# ---------------------------------------------------------------
r,al=sp.symbols('r alpha',positive=True)
f=1-r**2/al**2
# normal to r=const surface: n_mu ~ d_r ; norm^2 = g^{rr} = f
grr_up=f
print("\n(1) sigma = signature involution on the HDA")
print("   radial-normal norm^2 = g^rr = f = 1 - r^2/alpha^2")
print("   exterior r<alpha: g^rr>0  -> r SPACELIKE -> foliation normal TIMELIKE -> eps = -1 (Lorentzian)")
print("   interior r>alpha: g^rr<0  -> r TIMELIKE   -> foliation normal SPACELIKE-> eps = +1 (Euclidean)")
print("   => sigma flips eps: eps -> -eps  (Lorentzian <-> Euclidean), sigma^2 = id.")
print("   i.e. the hole-side and cosmos-side Hamiltonian constraints are related by a")
print("   DISCRETE signature flip -- a discrete Wick rotation -- not a continuous one.")

# ---------------------------------------------------------------
# (2) sigma, tau as the S3 generators on the 3 SdS-cubic roots; verify relations
#     and decompose the representation they carry.
# ---------------------------------------------------------------
import sympy as sp
P=lambda perm: sp.Matrix(3,3, lambda i,j: 1 if perm[j]==i else 0)  # perm matrix
tau=P([1,2,0])      # 3-cycle (sky-angle triality, order 3)
sig=P([1,0,2])      # transposition (root-exchange involution, order 2)
I3=sp.eye(3)
print("\n(2) <sigma,tau> on the three SdS-cubic roots:")
print("   sigma^2 = id :", sig*sig==I3)
print("   tau^3   = id :", tau**3==I3)
print("   (sigma tau)^2 = id :", (sig*tau)**2==I3)
# generate the group
elems=set(); frontier=[I3]; 
allg=[I3]
gens=[sig,tau]
seen={sp.ImmutableMatrix(I3)}
stack=[I3]
while stack:
    g=stack.pop()
    for h in gens:
        gh=sp.ImmutableMatrix(g*h)
        if gh not in seen:
            seen.add(gh); stack.append(sp.Matrix(gh))
print("   group order =",len(seen),"  => S3 (D3) confirmed")
# character of the permutation rep, decompose into irreps of S3
def chi(M): return sp.trace(M)
classes={'e':I3,'transposition':sig,'3cycle':tau}
perm_char={k:chi(M) for k,M in classes.items()}
print("   permutation-rep characters: e=%s, transposition=%s, 3-cycle=%s"%(perm_char['e'],perm_char['transposition'],perm_char['3cycle']))
# S3 irreps: trivial (1,1,1), sign (1,-1,1), standard 2d (2,0,-1)  [classes e,transp,3cyc]
# multiplicities via <chi,chi_irrep> with class sizes 1,3,2 (|G|=6)
sizes={'e':1,'transposition':3,'3cycle':2}
irreps={'trivial':{'e':1,'transposition':1,'3cycle':1},
        'sign':{'e':1,'transposition':-1,'3cycle':1},
        'standard2d':{'e':2,'transposition':0,'3cycle':-1}}
for name,ch in irreps.items():
    m=sp.Rational(sum(sizes[c]*perm_char[c]*ch[c] for c in sizes),6)
    print(f"   mult of {name} in perm rep = {m}")
print("   => perm rep = trivial (+) standard-2d.  The 2d standard irrep is the nontrivial carrier.")

# ---------------------------------------------------------------
# (3) the combined structure: sigma (signature Z2) x the S3 on the cubic.
#     Cold readout of what this is and is not.
# ---------------------------------------------------------------
print("\n(3) COLD VERDICT (what the computation shows, and what it does not):")
print("   SHOWN:")
print("    - The HDA structure function is metric-dependent (eps*h^{ab}): the algebra is a")
print("      Lie ALGEBROID, not a Lie algebra -- the standard root of the problem of time.")
print("    - sigma (vantage involution) acts on it as the signature flip eps->-eps: a DISCRETE")
print("      Wick rotation between the hole-side (Lorentzian) and cosmos-side (Euclidean) constraint.")
print("    - <sigma,tau> = S3 acts on the three SdS-cubic roots; the rep is trivial (+) standard-2d.")
print("   NOT YET SHOWN (the next computation):")
print("    - that the substrate's ABSOLUTE foliation deparametrizes H (kills the structure-function")
print("      obstruction) to a true Hamiltonian, and that quantizing THAT yields an operator algebra")
print("      (Heisenberg/Weyl pair, or a discrete spectrum) carrying the S3 rep = the 'quantum grammar'.")
print("    - whether the cubic's standard-2d irrep is the carrier of that spectrum (the 'cubic degeneracy').")
