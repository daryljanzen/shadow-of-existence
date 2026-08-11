"""Is N_c = 3 forced by anomaly freedom, or is it free?
Generalise: su(N)xsu(2)xu(1) with one 'generation' Q=(N,2), u^c=(Nbar,1), d^c=(Nbar,1), L=(1,2), e^c=(1,1).
Solve the linear anomaly + Yukawa conditions for the hypercharges at general N, then test the CUBIC."""
import sympy as sp
N=sp.symbols('N', positive=True)
q,u,d,l,e,h=sp.symbols('q u d l e h', rational=True)
A_NN1 = 2*q - u - d                 # [SU(N)]^2 U(1): Q doublet weight 2 ; u^c,d^c singlets
A_221 = N*q + l                     # [SU(2)]^2 U(1): colour N for Q, 1 for L
A_grav= 2*N*q - N*u - N*d + 2*l - e # U(1)-grav
Y1=q-u+h; Y2=q-d-h; Y3=l-e-h
sol=sp.solve([A_NN1,A_221,A_grav,Y1,Y2,Y3],[u,d,l,e,h],dict=True)
print("   linear solution at general N:")
s=sol[0]
for k in (u,d,l,e,h): print("      %s = %s"%(k, sp.simplify(s[k])))
cubic = 2*N*q**3 + N*(-s[u])**3 + N*(-s[d])**3 + 2*s[l]**3 + (-s[e])**3
cub=sp.simplify(sp.expand(cubic))
print()
print("   [U(1)]^3 residual after imposing the linear conditions:")
print("      ", sp.factor(cub))
print()
roots=sp.solve(sp.Eq(cub,0), N)
print("   values of N for which the cubic ALSO vanishes:", roots)
