"""Does the 325-mode k-grid under-sample |Delta_l(k)|^2 -- and does the bias grow with l?
Test on CAMB's OWN Delta_l, which is exact: integrate it on the dense grid (truth) and on the
instrument's 325-mode ladder, and compare."""
import numpy as np, camb
p=camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150*0.674**2-0.02237, mnu=0.0, omk=0, tau=0.0)
p.InitPower.set_params(As=2.1e-9, ns=0.965); p.set_for_lmax(1600, lens_potential_accuracy=0)
r=camb.get_results(p); tr=r.get_cmb_transfer_data()
L=np.array(tr.L); q=np.array(tr.q); D=tr.delta_p_l_k[0]
DM=13864.
# the instrument's ladder
stretch=2.75; Lmax=int(900/stretch)+4
Ls=np.arange(2,Lmax); lL=np.sqrt(Ls*(Ls+2))*stretch
kk_inst=lL/DM; kk_inst=kk_inst[lL<=900]
print("   instrument ladder: %d modes, k in [%.5f, %.5f]"%(len(kk_inst),kk_inst[0],kk_inst[-1]))
print("   CAMB dense grid  : %d modes over the same range"%((q>=kk_inst[0])&(q<=kk_inst[-1])).sum())
print()
NS=0.965
print("      l     dense C_l      on the 325-ladder     ratio")
for l in (221,537,815,1130):
    iL=int(np.argmin(abs(L-l)))
    sel=(q>=kk_inst[0])&(q<=kk_inst[-1])
    qd=q[sel]; Dd=D[iL][sel]
    dense=np.trapezoid(qd**(NS-2.)*Dd**2, qd)
    Di=np.interp(kk_inst, q, D[iL])
    lad=np.trapezoid(kk_inst**(NS-2.)*Di**2, kk_inst)
    print("     %4d  %.6e   %.6e   %8.4f"%(L[iL],dense,lad,lad/dense))
print()
print("   ratio < 1 and FALLING with l  ->  the k-grid under-samples, worse at higher l")
