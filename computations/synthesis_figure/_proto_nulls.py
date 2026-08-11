import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':10,'mathtext.fontset':'cm'})
def rp(ttil):  # r'(tau~) = cosh(1.5 t) sinh(1.5 t)^{-1/3}, for tau~>0
    s=1.5*ttil; return np.cosh(s)*np.abs(np.sinh(s))**(-1/3)
def nullode(chi,tau,sign): return [sign*rp(tau[0]+chi)]
fig,ax=plt.subplots(figsize=(5.4,5.0)); FUND,FLAT,PHOT,SPH='#c0392b','#1e8449','#2471a3','#7d3c98'
X0,X1=-1.2,1.2
# seam tau~=0 (big bang)
ax.plot([X0,X1],[-X0,-X1],color='k',lw=1.6); ax.text(-0.75,0.86,'seam $\\tilde\\tau=0$ (big bang)',fontsize=8,rotation=-45)
# coordinate families (only where tau~=tau+chi>0)
for c in np.linspace(-0.9,0.9,7):  # constant chi (fundamental, vertical, red)
    tt=np.linspace(max(-c+0.02,-1.2),1.2,50); ax.plot([c]*len(tt),tt,color=FUND,lw=1.0,alpha=0.9)
for c in np.linspace(-0.9,0.9,7):  # constant tau (flat space, horizontal, green)
    xx=np.linspace(max(-c+0.02,-1.2),1.2,50); ax.plot(xx,[c]*len(xx),color=FLAT,lw=1.0,alpha=0.9)
for d in np.linspace(0.2,2.0,6):   # constant tau~ (S3 layers, diagonal, purple)
    ax.plot([X0,X1],[d-X0,d-X1],color=SPH,lw=1.0,alpha=0.7)
# NULL geodesics (curved) - integrate dtau/dchi = +- r'(tau+chi)
for tau0 in np.linspace(-0.7,0.7,7):
    for sgn in (+1,-1):
        chi0=-tau0+0.12  # start just above the seam
        sol=solve_ivp(nullode,[chi0,1.25],[tau0],args=(sgn,),max_step=0.01,dense_output=True)
        m=sol.y[0]<1.25
        ax.plot(sol.t[m],sol.y[0][m],color=PHOT,lw=1.6)
ax.set_xlim(X0,X1); ax.set_ylim(X0,X1); ax.set_aspect('equal')
ax.set_xlabel(r'$\chi$'); ax.set_ylabel(r'$\tau$'); ax.set_title('null geodesics (blue), analytic')
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig('_proto_nulls.png',dpi=150,bbox_inches='tight'); print('ok')
