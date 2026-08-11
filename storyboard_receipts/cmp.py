import os, numpy as np
src=open('HIER_photon_hierarchy.py').read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
C=np.load('/tmp/camb_D.npy')
no=float(np.interp(50.,ls,Dl)); nc=C[50]
print("  OURS vs CAMB  (identical parameters, both UNLENSED, both tau=0), normalised at l=50")
print("      l     ours/D50   CAMB/D50    ratio")
for L in (15,100,220,300,416,538,675,810,1000,1148):
    if L>ls[-1]: continue
    o=float(np.interp(L,ls,Dl))/no; c=C[L]/nc
    print("   %5d    %8.4f   %8.4f   %6.3f"%(L,o,c,o/c))
