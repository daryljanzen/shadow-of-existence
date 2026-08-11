"""SHAPE — the full spectral shape against ALL of Planck 2018 Table 5, normalised at P1.
Reading only P1/P2 and P1/P3 hid the shape: those two sit at similar depth (r2141)."""
import os, numpy as np
src=open('HIER_photon_hierarchy.py').read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls']),np.array(g['Dl'])
PL=[('P1',220.6,5733),('T1',416.3,1713),('P2',538.1,2586),('T2',675.5,1799),
    ('P3',809.8,2518),('T3',1001.1,1049),('P4',1147.8,1227),('T4',1290.0,747)]
norm=Dl[int(np.argmin(abs(ls-220.6)))]/5733.
print("  SHAPE vs Planck 2018 Table 5 (KMAXL=%s, normalised at P1)"%os.environ.get('KMAXL','?'))
print("    feature    l     Planck    ours     ratio")
for nm,l,D in PL:
    if l>ls[-1]: continue
    i=int(np.argmin(abs(ls-l)))
    print("      %-3s %7.1f %8.0f %8.0f    %6.3f"%(nm,l,D,Dl[i]/norm,(Dl[i]/norm)/D))
