"""PIN CAMB's T_source: project it with j_l and check it reproduces CAMB's OWN Delta_l(k).
CAMB computes delta_p_l_k independently of the T_source output, so agreement pins the convention."""
import numpy as np, camb
from scipy.special import spherical_jn
p=camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.1e-9, ns=0.965); p.set_for_lmax(1600, lens_potential_accuracy=0)
r=camb.get_results(p)
tr=r.get_cmb_transfer_data()
L=np.array(tr.L); q=np.array(tr.q); D=tr.delta_p_l_k[0]      # (nL, nq)
eta0=r.conformal_time(0.)
print("   eta_0 = %.2f Mpc ; CAMB transfer grid: %d ells, %d k"%(eta0,len(L),len(q)))
# pick a few k in the acoustic range and a few ells
kk=np.array([0.0159,0.0387,0.0588])
etas=np.linspace(150., 700., 1400)
S=r.get_time_evolution(kk, etas, ['T_source'])[:,:,0]        # (nk, neta)
print()
print("   projecting  Delta_l(k) = int deta S(k,eta) j_l(k(eta_0-eta))  and comparing with CAMB's own:")
print("      l      k        mine           CAMB          ratio")
for l in (221, 537, 815):
    iL=int(np.argmin(abs(L-l)))
    for j,k in enumerate(kk):
        x=k*(eta0-etas)
        mine=np.trapezoid(S[j]*spherical_jn(int(L[iL]), x), etas)
        camb_v=np.interp(k, q, D[iL])
        print("     %4d  %.4f  %+13.5e  %+13.5e   %8.4f"%(L[iL],k,mine,camb_v, mine/camb_v if camb_v!=0 else float('nan')))
