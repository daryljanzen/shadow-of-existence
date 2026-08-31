"""P7 grand synthesis figure (fig:dS_SdS) - 2x3 plate, ALL physical curves rendered analytically.
Colour key (figure-wide): RED fundamental/timelike | GREEN flat synchronous space |
                          BLUE null/photon | PURPLE S^3 layers | grey neutral.
(a) dS4 hyperboloid  (b) reassigned (tau,chi) with analytic null geodesics  (c) the lap r(tau~)
(d) why Nariai       (e) layered handoff (analytic +-r)                      (f) the lap's cos oscillation."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
FUND,FLAT,PHOT,SPH,GRY='#c0392b','#1e8449','#2471a3','#7d3c98','#7f8c8d'
fig=plt.figure(figsize=(13.6,8.7))
gs=fig.add_gridspec(2,3,wspace=0.16,hspace=0.24,left=0.02,right=0.99,top=0.93,bottom=0.06)

# ============ (a) dS4 hyperboloid ============
axA=fig.add_subplot(gs[0,0],projection='3d')
zmax=1.9; t=np.linspace(-zmax,zmax,60)
ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
for zc in np.linspace(-zmax,zmax,9):
    R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80); axA.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=SPH,lw=0.6,alpha=0.45)
ph=np.linspace(0,2*np.pi,120); axA.plot(np.cos(ph),np.sin(ph),0*ph,color=SPH,lw=2.0)
for phi in np.linspace(0,2*np.pi,7)[:-1]:
    x,y,z=ruling(phi,1); axA.plot(x,y,z,color=FUND,lw=0.7,alpha=0.18)
    x,y,z=ruling(phi,-1); axA.plot(x,y,z,color=FLAT,lw=0.7,alpha=0.18)
for phi in np.linspace(0,2*np.pi,7)[:-1]:
    zz=np.linspace(-zmax,zmax,50); RR=np.sqrt(1+zz**2); axA.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=PHOT,lw=0.7,alpha=0.22)
pa=np.linspace(0,2*np.pi,7)[1]
x,y,z=ruling(pa,1); axA.plot(x,y,z,color=FUND,lw=3.0)
x,y,z=ruling(pa,-1); axA.plot(x,y,z,color=FLAT,lw=3.0)
zz=np.linspace(-zmax,zmax,50); RR=np.sqrt(1+zz**2); pm=np.linspace(0,2*np.pi,7)[4]
axA.plot(RR*np.cos(pm),RR*np.sin(pm),zz,color=PHOT,lw=3.0)
axA.plot([0,0],[0,0],[-zmax,zmax],color='k',lw=0.7,ls=(0,(4,3))); axA.text(0,0,zmax+0.2,r'$X_0$',fontsize=8,ha='center')
axA.view_init(elev=10,azim=-60); axA.set_box_aspect((1,1,1.3)); axA.set_axis_off()
axA.text2D(0.0,1.0,'(a)',transform=axA.transAxes,fontsize=13,fontweight='bold')
axA.text2D(0.11,1.0,'de Sitter substrate (dS$_4$)',transform=axA.transAxes,fontsize=9.5,va='top')
axA.text2D(0.0,0.0,'null rulings A (red), B (green): null\nat-rest worldlines (blue): timelike\n$S^3$ (purple): space',transform=axA.transAxes,fontsize=7.2)

# ============ (b) reassigned (tau,chi) with analytic null geodesics ============
axB=fig.add_subplot(gs[0,1]); X0,X1=-1.15,1.15
def rp(tt):
    s=1.5*np.clip(tt,3e-3,3.0); return np.cosh(s)*np.sinh(s)**(-1/3)
axB.plot([X0,X1],[-X0,-X1],color='k',lw=1.5)
for c in np.linspace(-0.85,0.85,5):
    tt=np.linspace(max(-c+0.03,X0),X1,40); axB.plot([c]*len(tt),tt,color=FUND,lw=1.0,alpha=0.85)
    xx=np.linspace(max(-c+0.03,X0),X1,40); axB.plot(xx,[c]*len(xx),color=FLAT,lw=1.0,alpha=0.85)
for d in np.linspace(0.35,2.0,5): axB.plot([X0,X1],[d-X0,d-X1],color=SPH,lw=1.0,alpha=0.6)
for tau0 in np.linspace(-0.6,0.6,5):
    for sgn in (+1,-1):
        chi0=-tau0+0.16
        sol=solve_ivp(lambda chi,y:[sgn*rp(y[0]+chi)],[chi0,1.2],[tau0],max_step=0.008)
        m=(sol.y[0]<1.18)&(sol.y[0]>X0); axB.plot(sol.t[m],sol.y[0][m],color=PHOT,lw=1.7)
axB.text(-0.42,-0.12,'seam $\tilde\tau{=}0$\n(big bang)',fontsize=7.2,rotation=-45,color='k',ha='center')
axB.text(0.9,0.0,'fundamental\n(timelike)',color=FUND,fontsize=7.0,ha='center',rotation=90,va='center')
axB.text(0.0,-1.02,'flat Euclidean space',color=FLAT,fontsize=7.2,ha='center')
axB.text(0.72,0.66,'$S^3$ layers\n$\\tilde\\tau{=}\\tau{+}\\chi$',color=SPH,fontsize=7.0,ha='center')
axB.text(0.30,0.5,'null\ngeodesics\n(photons)',color=PHOT,fontsize=7.2,ha='center')
axB.set_xlim(X0,X1); axB.set_ylim(X0,X1); axB.set_aspect('equal'); axB.set_xlabel(r'$\chi$',labelpad=1); axB.set_ylabel(r'$\tau$',labelpad=-2); axB.tick_params(labelsize=7.5)
for s in ['top','right']: axB.spines[s].set_visible(False)
axB.text(0.0,1.02,'(b)',transform=axB.transAxes,fontsize=13,fontweight='bold')
axB.text(0.11,1.02,r'reassigned $(\tau,\chi)$ $-$ null cones tip to the seam',transform=axB.transAxes,fontsize=9.0,va='bottom')

# ============ (c) the lap ============
axC=fig.add_subplot(gs[0,2],projection='3d')
s=np.linspace(-2.3,2.3,1000); r=np.sinh(s.astype(complex))**(2/3); Re,Im=r.real,r.imag; ex,co=s>0,s<0
ss,rr=np.meshgrid(np.linspace(-2.3,2.3,2),np.linspace(-1.6,3.4,2)); axC.plot_surface(ss,rr,np.zeros_like(ss),color='0.5',alpha=0.05,linewidth=0)
axC.plot(s[ex],Re[ex],Im[ex],color=FUND,lw=2.6); axC.plot(s[co],Re[co],Im[co],color=PHOT,lw=2.6)
for i in range(0,co.sum(),120):
    idx=np.where(co)[0][i]; axC.plot([s[idx]]*2,[Re[idx]]*2,[0,Im[idx]],color=PHOT,lw=0.5,alpha=0.33)
axC.plot(s[co],-np.abs(r[co]),0*np.abs(r[co]),color=GRY,lw=1.3,ls=(0,(5,3)))
axC.scatter([0],[0],[0],color='k',s=34,zorder=8)
axC.text(1.8,Re[ex][-1]*0.9,0.1,'expansion\n$\\sinh^{2/3}$',color=FUND,fontsize=7.2,ha='center')
axC.text(-2.1,Re[co][0],Im[co][0]+0.15,'prior collapse\n(phase $2\\pi/3$)',color=PHOT,fontsize=7.2,ha='center')
axC.text(-1.3,-1.3,0.0,'forced-real:\nfake cusp',color='#555',fontsize=7.0,ha='center')
axC.text(-0.1,1.7,2.4,'seam: branch point\n(not the singularity)',fontsize=7.2,ha='center',va='center'); axC.plot([0,-0.1],[0,1.5],[0,2.0],color='k',lw=0.5)
axC.set_xlabel(r'$\tilde\tau$',labelpad=-5,fontsize=8); axC.set_ylabel(r'$\mathrm{Re}\,r$',labelpad=-5,fontsize=8); axC.set_zlabel(r'$\mathrm{Im}\,r$',labelpad=-5,fontsize=8)
axC.tick_params(labelsize=6); axC.view_init(elev=17,azim=-40); axC.set_box_aspect((2.3,1.5,1.15))
axC.text2D(0.0,1.0,'(c)',transform=axC.transAxes,fontsize=13,fontweight='bold')
axC.text2D(0.11,1.0,r'the lap: $r(\tilde\tau)$ through the seam',transform=axC.transAxes,fontsize=9.2,va='top')

# ============ (d) why Nariai ============
axD=fig.add_subplot(gs[1,0])
rv=np.linspace(0.06,1.32,600); f=lambda M:1-2*M/rv-rv**2; MN=1/(3*np.sqrt(3))
axD.axhline(0,color='0.6',lw=0.8)
axD.plot(rv,f(0.14),color=GRY,lw=1.8,label=r'$M<M_{\rm N}$: two horizons (transverse)')
axD.plot(rv,f(MN),color=FUND,lw=2.6,label=r'$M=M_{\rm N}$: double root (tangent)')
axD.plot(rv,f(0.26),color=GRY,lw=1.6,ls=(0,(5,3)),label=r'$M>M_{\rm N}$: no horizon')
for rr in sorted([x.real for x in np.roots([-1,0,1,-2*0.14]) if abs(x.imag)<1e-6 and x.real>0]): axD.plot(rr,0,'o',color=GRY,ms=5)
rN=1/np.sqrt(3); axD.plot(rN,0,'o',color=FUND,ms=7,zorder=5)
axD.annotate('Nariai: horizons merge,\ngrazed tangentially',xy=(rN,0),xytext=(rN+0.08,0.34),fontsize=7.2,color=FUND,arrowprops=dict(arrowstyle='->',color=FUND,lw=0.7))
axD.text(0.03,0.66,'collapse forms a horizon $\\Rightarrow$ no $M{>}M_{\\rm N}$;\ntangent limiting orientation $\\Rightarrow$ no transverse\n$\\therefore$ Nariai, fixed by $\\Lambda$ alone',fontsize=7.4,va='top',bbox=dict(boxstyle='round,pad=0.35',fc='#fdf6e3',ec='0.7',lw=0.6))
axD.set_xlabel(r'areal radius $r/\alpha$',fontsize=8.5); axD.set_ylabel(r'$f(r)=1-2M/r-r^2/\alpha^2$',fontsize=8.5)
axD.set_ylim(-0.75,0.9); axD.set_xlim(0,1.32); axD.tick_params(labelsize=7.5); axD.legend(loc='lower right',fontsize=6.7,frameon=False)
for sp in ['top','right']: axD.spines[sp].set_visible(False)
axD.text(-0.12,1.02,'(d)',transform=axD.transAxes,fontsize=13,fontweight='bold'); axD.text(0.09,1.02,r'why Nariai: the horizon trichotomy',transform=axD.transAxes,fontsize=9.2,va='bottom')

# ============ (e) layered handoff (analytic +-r only) ============
axE=fig.add_subplot(gs[1,1])
sd=np.linspace(-2.3,2.3,600); env=np.abs(np.sinh(sd))**(2/3)
axE.axvspan(-2.5,0,color=PHOT,alpha=0.06); axE.axvspan(0,2.5,color=FUND,alpha=0.06)
axE.plot(sd,env,color=SPH,lw=2.6); axE.plot(sd,-env,color=SPH,lw=2.6); axE.fill_between(sd,-env,env,color=SPH,alpha=0.08)
axE.axvline(0,color='0.4',lw=0.9,ls=(0,(3,3))); axE.plot(0,0,'o',color='k',ms=6,zorder=6)
axE.annotate('seam',xy=(0,0),xytext=(-0.9,2.3),fontsize=7.4,ha='center',arrowprops=dict(arrowstyle='->',lw=0.6))
axE.text(-1.15,-2.75,'INWARD (collapse)\nleaf local rate\n$-$ radiation gravitates',color='#1a5276',fontsize=7.4,ha='center',va='top')
axE.text(1.2,-2.75,'OUTWARD (expansion)\nfoliation stacking rate\n$-$ geometric stacking',color='#922b21',fontsize=7.4,ha='center',va='top')
axE.text(0.06,1.25,'deposits: $\\rho_r/\\rho_m\\approx2$ (acoustic scale)\n$\\eta$ (composition)',fontsize=7.2,ha='left',bbox=dict(boxstyle='round,pad=0.3',fc='#fdf6e3',ec='0.7',lw=0.6))
axE.annotate('cooling leg = BBN',xy=(0.55,0.55),xytext=(0.8,-0.15),fontsize=7.0,color='#922b21',ha='left',arrowprops=dict(arrowstyle='->',color='#922b21',lw=0.5))
axE.set_xlabel(r'cosmic proper time $\tilde\tau$',fontsize=8.5); axE.set_ylabel(r'areal radius $\pm r(\tilde\tau)$ ($S^3$ layers)',fontsize=8.5)
axE.set_xlim(-2.3,2.3); axE.set_ylim(-3.5,2.7); axE.tick_params(labelsize=7.5)
for sp in ['top','right']: axE.spines[sp].set_visible(False)
axE.text(-0.12,1.02,'(e)',transform=axE.transAxes,fontsize=13,fontweight='bold'); axE.text(0.09,1.02,r'the layered handoff at the seam',transform=axE.transAxes,fontsize=9.2,va='bottom')

# ============ (f) the lap's cos oscillation (analytic) ============
axF=fig.add_subplot(gs[1,2])
rA=1/np.sqrt(3); rB=-2/np.sqrt(3)
rl=np.linspace(rB,rA,400); X1lap=-np.cos(2*np.pi*rl/np.sqrt(3))
axF.plot(rl,X1lap,color=FUND,lw=2.6,label='conjugate lap: $X_1=-\\cos(2\\pi r/\\sqrt{3})$')
rR=np.linspace(rA,1.05,50); axF.plot(rR,0.5+np.pi*(rR-rA),color=GRY,lw=2.0)
rLl=np.linspace(-1.32,rB,50); axF.plot(rLl,0.5+np.pi*(rLl-rB),color=GRY,lw=2.0,label='real ruling legs (straight, slope $\\pi$)')
for rr,lab,dy in [(rA,'$+\\alpha/\\sqrt{3}$ (enter, $A{=}B$)',0.18),(0.0,'$r{=}0$ (trough, $X_1{=}-\\alpha$)',-0.22),(rB,'$-2\\alpha/\\sqrt{3}$ (close)',0.18)]:
    yy=-np.cos(2*np.pi*rr/np.sqrt(3)); axF.plot(rr,yy,'o',color=FUND,ms=6); axF.axvline(rr,color='0.8',lw=0.6,ls=':')
    axF.annotate(lab,xy=(rr,yy),xytext=(rr,yy+dy),fontsize=6.8,ha='center')
axF.axhline(0,color='0.6',lw=0.7)
axF.set_xlabel(r'signed areal radius $r/\alpha$ (arc length along the bead)',fontsize=8.2); axF.set_ylabel(r'$X_1/\alpha$ (embedding coordinate)',fontsize=8.5)
axF.set_xlim(-1.35,1.1); axF.set_ylim(-1.35,2.15); axF.tick_params(labelsize=7.5); axF.legend(loc='upper left',fontsize=6.7,frameon=False)
for sp in ['top','right']: axF.spines[sp].set_visible(False)
axF.text(-0.12,1.02,'(f)',transform=axF.transAxes,fontsize=13,fontweight='bold'); axF.text(0.09,1.02,r'the lap oscillation the hyperboloid flattens',transform=axF.transAxes,fontsize=9.2,va='bottom')

plt.savefig('dS-SdS-synthesis.pdf',bbox_inches='tight'); plt.savefig('dS-SdS-synthesis.png',dpi=145,bbox_inches='tight')
print('wrote analytic 2x3 plate')
