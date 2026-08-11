import os, numpy as np
src=open('HIER_photon_hierarchy.py').read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
i1=int(np.argmax(Dl))
PL={6:848.5,10:817.2,12:824.0,18:878.6,30:1054.7}
print("  THE DISCRIMINATION:  P1 / D(low l)   ours vs Planck best-fit theory")
print("     l      ours D_l     P1/D_l(ours)   Planck P1/D_l   ours/Planck")
for L,DP in PL.items():
    i=int(np.argmin(abs(ls-L)))
    if abs(ls[i]-L)>3: continue
    r_ours=Dl[i1]/Dl[i]; r_pl=5730.1/DP
    print("   %4.0f    %10.6f    %10.3f      %10.3f       %7.3f"%(ls[i],Dl[i],r_ours,r_pl,r_ours/r_pl))
print()
print("   our P1 at l=%.0f"%ls[i1])
print("   NOTE: Planck's curve carries reionisation (suppresses l~220 by e^-2tau=0.897, not l~10)")
print("         and lensing (<1% at these l).  Ours has neither, so the like-for-like Planck")
print("         ratio is 5730.1/0.897 / D_l  ->  multiply the Planck column by 1.115.")
