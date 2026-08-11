"""CR's discrete mode set has a FLOOR: k_L = sqrt(L(L+2))/r_0 for L >= 2, so the lowest source mode
sits at l = sqrt(8)*2.75 = 7.78.  LambdaCDM has a continuous measure reaching k -> 0.  That is a
parameter-free CR prediction living at low l, where the instrument is validated to 1%."""
import os, numpy as np
src=open(os.environ['MOD']).read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
from PLANCK_theory_curve import planck_TT
n_o=float(np.interp(50.,ls,Dl)); n_p=float(planck_TT(50.))
lab=os.environ.get('LAB','?')
print("  %-28s lowest mode l_L = %.2f   (%d modes)"%(lab,g['kk'][0]*g['DM'] if 'kk' in g else float('nan'),len(g['kk']) if 'kk' in g else -1))
print("      l     ours/plateau-norm   Planck    ratio")
for L in (2,3,4,5,6,8,10,12,15,20,30,50):
    if L<ls[0] or L>ls[-1]: continue
    o=float(np.interp(L,ls,Dl))/n_o; p=float(planck_TT(L))/n_p
    print("   %4d       %10.4f      %8.4f   %6.3f"%(L,o,p,o/p))
