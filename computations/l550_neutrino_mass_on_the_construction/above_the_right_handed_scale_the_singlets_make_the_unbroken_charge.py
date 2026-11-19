"""Above the right-handed scale: what the singlets make, whether gauged B-L neutrality removes it, and whether it
survives the breaking.  Unbroken Pati-Salam phase, flavour-universal chemical potentials, doublet realisation.
Working file for the L550 close-out; resolves Y16's bound line (the order-one conversion factor taken as one).
Result: the singlets' decays make n(chi_R) - n(chi_L), which is exactly B-L_SM -- the charge the v_R breaking leaves
unbroken -- so it carries through with factor one; gauged B-L is zero identically in the symmetric phase, so
neutrality removes nothing; the washout weight is 0.104 per unit charge against 0.100 for the charge in one
channel's species alone."""
import numpy as np, sympy as sp
# unbroken Pati-Salam phase, flavour-universal chemical potentials
# species: F_L (4,2,1) 24 Weyl, F_R (4bar,1,2) 24 Weyl, chi_L (4bar,2,1) 8 complex, chi_R (4,1,2) 8 complex
g=np.array([24,24,2*8,2*8],float)          # asymmetry weights (bosons x2)
m1,m2,m3,m4=sp.symbols('m1 m2 m3 m4')
mu=[m1,m2,m3,m4]; n=[g[i]*mu[i] for i in range(4)]
# gauge B-L of each multiplet's components sums to zero (traceless), so neutrality holds identically
# fast: Dirac-type mass operator (F_L chi_L)(F_R chi_R)/M': m1+m2+m3+m4=0
q=sp.symbols('q')
# conserved: Q = n(chi_R)-n(chi_L)  [= B-L_SM, gauge part zero], P = n(F_L)-n(F_R), n(F_L)-n(chi_L)
# the singlets' decays to F_L chi_L change (n1,n3) by (+1,+1) and to F_R chi_R (n2,n4) by (+1,+1)
# so a produced asymmetry Q=q carries P=-q and n1-n3=0
sol=sp.solve([m1+m2+m3+m4, n[3]-n[2]-q, n[0]-n[1]+q, n[0]-n[2]],[m1,m2,m3,m4],dict=True)[0]
print('PS phase mu:',sol)
cL=sp.simplify((sol[m1]+sol[m3])/q); cR=sp.simplify((sol[m2]+sol[m4])/q)
print('washout weights: left channel (mu_F+mu_chi)/q =',cL,' right =',cR,' net =',sp.simplify(cL-cR))
# the charge left unbroken at v_R: B-L_SM = (B-L)_gauge + n(chi_R) - n(chi_L); check neutrality of the vevs
BL_g={'chiL_nu':+1,'chiR_nuc':-1}
print('B-L_SM of <chi_L>:', BL_g['chiL_nu'] - 1, ' of <chi_R>:', BL_g['chiR_nuc'] + 1)
# operators: (F_L chi_L)^2, (F_L chi_L)(F_R chi_R), (F_R chi_R)^2 : change of n(chi_R)-n(chi_L)
for name,(dl,dr) in {'(F_L chi_L)^2':(2,0),'Dirac':(1,1),'(F_R chi_R)^2':(0,2)}.items():
    print(name,'changes B-L_SM by', dr-dl)
