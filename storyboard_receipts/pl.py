import os, numpy as np
src=open('HIER_photon_hierarchy.py').read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
fnu=g['fnu']; Psi_i=1.0/(1.0+0.4*fnu)
# the source at recombination is (Theta_0+Psi) = 0.4006 Psi  (measured r2141, rho_r/rho_m=0.317 there)
pred=(0.4006*Psi_i)**2/2.0
print("  PLATEAU with the mode grid extended to l_min=%s   (n_s=1, ISW off, closed form applies)"%os.environ.get('LLMIN'))
print("     exact SW plateau for our normalisation = (0.4006 Psi_i)^2/2 = %.6f"%pred)
print("       l     l*eta_rec/D    ours          ratio")
for L in (8,10,14,20,30,45):
    i=int(np.argmin(abs(ls-L)))
    if abs(ls[i]-L)>3: continue
    print("     %4.0f      %8.3f     %10.6f     %7.3f"%(ls[i],ls[i]*g['eta_rec']/g['DM'],Dl[i],Dl[i]/pred))
i1=int(np.argmax(Dl))
print()
print("     P1 at l=%.0f: D=%.6f  ->  P1/plateau = %.2f"%(ls[i1],Dl[i1],Dl[i1]/pred))
