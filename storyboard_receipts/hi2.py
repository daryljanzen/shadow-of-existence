import os, numpy as np
from scipy.signal import argrelextrema as ar
src=open('HIER_photon_hierarchy.py').read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
def refine(q):
    y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
    t=0.5*(y0-y2)/d if d!=0 else 0.
    return float(ls[q]+t*(ls[1]-ls[0]))
tr=[refine(q) for q in ar(Dl,np.less,order=3)[0] if 880<=ls[q]<=1270]
pk=[refine(q) for q in ar(Dl,np.greater,order=3)[0] if 880<=ls[q]<=1270]
t=tr[0] if tr else float('nan'); p=pk[0] if pk else float('nan')
print("  NODAMP=%s   T3 = %.1f (Planck 1001.1)   P4 = %.1f (Planck 1147.8)   spacing = %.1f (Planck 146.7)"
      %(os.environ.get('NODAMP','0'),t,p,p-t))
