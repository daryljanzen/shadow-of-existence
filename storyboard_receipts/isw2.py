import os, numpy as np
src=open(os.environ['MOD']).read().replace('if __name__ == "__main__":','if True:')
g={'__name__':'x'}; exec(compile(src,'h','exec'),g)
ls,Dl=np.array(g['ls'],dtype=float),np.array(g['Dl'],dtype=float)
# normalise to the l=25-30 level, as the old receipt does
m=(ls>=25)&(ls<=30); n=float(Dl[m].mean()) if m.any() else float(np.interp(27.5,ls,Dl))
print("  %-26s ETAEND=%s  eta_0=%.0f"%(os.environ.get('LAB','?'),os.environ.get('ETAEND'),g['eta_0']))
print("     l:   "+"  ".join("%6d"%L for L in (2,3,4,5,6,8,10)))
print("   ours:  "+"  ".join("%6.3f"%(float(np.interp(L,ls,Dl))/n) for L in (2,3,4,5,6,8,10)))
print("   old receipt SW only :   0.12   0.10   0.20   0.65")
print("   old receipt SW+ISW  :   0.50   0.41   0.47   0.85")
