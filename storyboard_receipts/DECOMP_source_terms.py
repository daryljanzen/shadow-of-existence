"""DECOMP — which source term carries which peak, and where along eta the ISW accumulates.

The hierarchy's damping is validated (VALID_hierarchy_damping.py: within 3-10% of the analytic Silk
formula) and the peak POSITIONS are good, so the acoustic physics is right and the remaining error is
in the RELATIVE WEIGHTING of the source terms.  The ISW is the suspect: switching it off swings P1/P2
by 38%, where a correct early ISW should contribute ~10-20% at l~200 and ~nothing at l~800.

This splits Delta_l into its three pieces and reports each one's share, then shows where along eta the
ISW integrand actually accumulates -- which distinguishes "the term is physically large" from "the term
is numerically contaminated by pre-recombination potential oscillations leaking past exp(-tau)".
"""
import os, numpy as np
os.environ.setdefault('NS1','2400'); os.environ.setdefault('NS2','3600'); os.environ.setdefault('STRIDE','2')
import HIER_photon_hierarchy as H
from scipy.special import spherical_jn

stretch=2.75; Ls=np.arange(2,int((1250+400)/stretch)+2)
lL=np.sqrt(Ls*(Ls+2))*stretch; kk=lL/H.DM; keep=lL<=900.0; kk=kk[keep]
E,Y,e_sw = H.evolve(kk)
m = E > max(e_sw, H.eta_rec-160.0); ee=E[m]; Yv=Y[m]
g=np.array([float(H.g_of(e)) for e in ee]); tau=np.array([float(H.tau_of(e)) for e in ee])
Ph=Yv[:,:,6]; sgn=Yv[:,:,H.IN]/2
Hcv=np.array([H.Hc_of(e) for e in ee])[:,None]; Onv=np.array([H.On_of(e) for e in ee])[:,None]
Ps=Ph-6*Hcv**2*Onv*sgn/kk[None,:]**2
Sm=g[:,None]*(Yv[:,:,2]/4+Ps)
Sd=g[:,None]*(Yv[:,:,7]/kk[None,:])
Si=np.exp(-tau)[:,None]*(np.gradient(Ph,ee,axis=0)+np.gradient(Ps,ee,axis=0))
x0m=H.eta_0-ee; P=kk**(0.965-1)/kk*np.gradient(kk)

print("="*84)
print("tau at the start of the integration window (eta=%.1f):  %.2f   -> exp(-tau) = %.2e"
      %(ee[0], tau[0], np.exp(-tau[0])))
print("tau at recombination (eta=%.1f):                        %.2f   -> exp(-tau) = %.3f"
      %(H.eta_rec, float(H.tau_of(H.eta_rec)), np.exp(float(H.tau_of(H.eta_rec)))**-1))
print("="*84)
print("  l     C_mono    C_dopp    C_isw   |  cross    TOTAL  |  ISW share")
for l in (220, 536, 813):
    X=kk[None,:]*x0m[:,None]
    jl=spherical_jn(int(l),X); jlp=spherical_jn(int(l),X,derivative=True)
    Dm=np.trapezoid(Sm*jl,ee,axis=0); Dd=np.trapezoid(Sd*jlp,ee,axis=0); Di=np.trapezoid(Si*jl,ee,axis=0)
    c=lambda A,B: float(np.sum(P*A*B))
    tot=c(Dm+Dd+Di,Dm+Dd+Di)
    print("  %4d  %8.3f  %8.3f  %8.3f  | %8.3f  %8.3f  |  %5.1f%%"
          %(l, c(Dm,Dm)/tot, c(Dd,Dd)/tot, c(Di,Di)/tot,
            (tot-c(Dm,Dm)-c(Dd,Dd)-c(Di,Di))/tot, 1.0, 100*c(Di,Di)/tot))
print()
print("WHERE THE ISW ACCUMULATES (cumulative |contribution| to Delta_l at l=220):")
l=220; X=kk[None,:]*x0m[:,None]; jl=spherical_jn(l,X)
integ=Si*jl
kmid=int(np.argmin(abs(kk-220/H.DM)))
cum=np.concatenate([[0],np.cumsum((integ[:-1,kmid]+integ[1:,kmid])/2*np.diff(ee))])
tot=cum[-1]
for frac in (0.25,0.5,0.75,0.95):
    j=int(np.argmin(abs(np.abs(cum)-abs(tot)*frac)))
    print("    %3d%% of the ISW integral is reached by eta=%7.1f Mpc  (z=%6.0f)"
          %(100*frac, ee[j], 1/np.interp(ee[j],H.eg,H.ag)-1))
print("    recombination is at eta=%.1f Mpc"%H.eta_rec)
