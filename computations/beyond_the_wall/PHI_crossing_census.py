import numpy as np
base='/tmp/claude-0/-home-user-shadow-of-existence/e37412c9-b73d-5dc0-927f-d18006c9d057/scratchpad/'
for f,tag in [('cr_phi.npz','CR (leaf)'),('lcdm_phi.npz','control')]:
    z=np.load(base+f,allow_pickle=True)
    eta=z['eta']; k=z['kpk']; q=z['qpk']; er=float(z['eta_rec']); es=float(z['eta_s'])
    print(f"{tag}: eta_start={es:.1f}  eta_rec={er:.1f}  eta_start/eta_rec={es/er:.3f}")
    for i in range(len(q)):
        kk=float(k[i]); entry=1.0/kk
        keta_s=kk*es
        crossed_in_window = es < entry < er
        print(f"   q={float(q[i]):.2f} k={kk:.4f}: horizon-entry eta=1/k={entry:.1f}  "
              f"k*eta_start={keta_s:5.1f}  "
              f"{'CROSSES during plasma' if crossed_in_window else 'sub-horizon at onset -> NO crossing in [start,rec]'}")
    print()
