import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,BLUE,GREY,BLACK,PURPLE='#c0392b','#2471a3','#8a8f94','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); zmax=2.0

def hyperboloid(ax,which,title):
    # universe = BLACK S^3 circles (skip equator)
    for zc in np.linspace(-zmax,zmax,9):
        if abs(zc)<1e-6: continue
        R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80)
        ax.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=BLACK,lw=0.4,alpha=0.28)
    # photons = GREY at-rest geodesics (meridians)
    zz=np.linspace(-zmax,zmax,40); RR=np.sqrt(1+zz**2)
    for phi in np.linspace(0,2*np.pi,13)[:-1]:
        ax.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=GREY,lw=0.5,alpha=0.30)
    # null rulings
    t=np.linspace(-zmax,zmax,50)
    ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
    for phi in np.linspace(0,2*np.pi,16)[:-1]:
        if which in ('red','both'):
            x,y,z=ruling(phi,1);  ax.plot(x,y,z,color=RED, lw=0.6,alpha=0.5)
        if which in ('blue','both'):
            x,y,z=ruling(phi,-1); ax.plot(x,y,z,color=BLUE,lw=0.6,alpha=0.5)
    # the lap (equator): red / blue / purple(mix)
    ph=np.linspace(0,2*np.pi,240)
    lapcol=PURPLE if which=='both' else (RED if which=='red' else BLUE)
    ax.plot(np.cos(ph),np.sin(ph),0*ph,color=lapcol,lw=3.0)
    ax.view_init(elev=12,azim=-58); ax.set_box_aspect((1,1,1.3)); ax.set_axis_off()
    ax.set_title(title,fontsize=9)

def observer(ax):
    X0,X1=-1.15,1.15
    def rp(tt): s=1.5*np.clip(tt,3e-3,3.0); return np.cosh(s)*np.sinh(s)**(-1/3)
    for c in np.linspace(-0.95,0.95,11):
        ax.plot([c,c],[X0,X1],color=BLUE,lw=0.9,alpha=0.55)   # blue = const chi (vertical)
        ax.plot([X0,X1],[c,c],color=RED, lw=0.9,alpha=0.55)   # red  = const tau (horizontal)
    for d in np.linspace(-1.6,2.0,12):
        ax.plot([X0,X1],[d-X0,d-X1],color=BLACK,lw=0.5,alpha=0.35)  # black = const tau~ (diagonal, S^3)
    def nc(chi0,tau0):
        sol=solve_ivp(lambda chi,y:[rp(y[0]+chi)],[chi0,X1],[tau0],max_step=0.008,rtol=1e-7)
        ch,ta=sol.t,sol.y[0]; tt=ta+ch; m=(ta>=X0)&(ta<=X1)&(tt>=0.08); return ch[m],ta[m]
    for tau0 in np.linspace(-1.0,1.0,10):
        chi0=max(X0,0.10-tau0); ch,ta=nc(chi0,tau0)
        if len(ch)>2: ax.plot(ch,ta,color=GREY,lw=1.1,alpha=0.8)   # grey = assigned null geodesics
    ax.plot([X0,X1],[-X0,-X1],color=PURPLE,lw=2.6)                 # purple overlay at r=0 (tau~=0)
    ax.set_xlim(X0,X1); ax.set_ylim(X0,X1); ax.set_aspect('equal')
    ax.set_xlabel(r'$\chi$'); ax.set_ylabel(r'$\tau$',labelpad=-2); ax.tick_params(labelsize=7.5)
    for s in ['top','right']: ax.spines[s].set_visible(False)
    ax.set_title('observer chart: blue=const $\\chi$, red=const $\\tau$,\ngrey=null geodesics, black=$S^3$ (const $\\tilde\\tau$), purple=$r{=}0$',fontsize=8)

def tau_r(ax):
    def tau_of_r(r): z=(complex(r)/A)**1.5; return (2.0/3.0)*np.arcsinh(z)
    rr=np.linspace(2.6,-2.6,500); T=np.array([tau_of_r(r) for r in rr])
    ax.plot(T.real,T.imag,rr,color=BLUE,lw=2.8)                    # ONE blue line, from scratch
    ax.scatter([0],[0],[0],color='k',s=24)
    ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
    ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
    ax.set_zlabel(r'$r/\alpha$',fontsize=8,labelpad=2)
    ax.view_init(elev=16,azim=-60); ax.tick_params(labelsize=6.5)
    ax.set_title(r'$\tilde\tau(r)$, one blue line ($r$ vertical)',fontsize=9)

fig=plt.figure(figsize=(15,9.2))
ax1=fig.add_subplot(2,3,1,projection='3d'); hyperboloid(ax1,'red', 'red null bundle (with lap)')
ax2=fig.add_subplot(2,3,2,projection='3d'); hyperboloid(ax2,'blue','blue null bundle (with lap)')
ax3=fig.add_subplot(2,3,3,projection='3d'); hyperboloid(ax3,'both','all four sets together')
ax4=fig.add_subplot(2,3,4); observer(ax4)
ax5=fig.add_subplot(2,3,5,projection='3d'); tau_r(ax5)
ax6=fig.add_subplot(2,3,6); ax6.axis('off')
ax6.text(0.05,0.9,'four sets of lines:',fontsize=10,fontweight='bold',transform=ax6.transAxes)
for i,(c,lab) in enumerate([(RED,'red null rulings (bundle $B$, incoming)'),
                            (BLUE,'blue null rulings (bundle $A$, outgoing)'),
                            (BLACK,'black circles = the $S^3$ universe'),
                            (GREY,'grey geodesics = at-rest photons')]):
    ax6.plot([0.05,0.15],[0.78-i*0.09]*2,color=c,lw=3,transform=ax6.transAxes)
    ax6.text(0.18,0.78-i*0.09,lab,fontsize=8.5,va='center',transform=ax6.transAxes)
ax6.text(0.05,0.30,'double-speed nulls: parked (no physical\nmotivation yet; needs honest thought later)',fontsize=8,style='italic',transform=ax6.transAxes)
plt.tight_layout(); plt.savefig('bead_frames.png',dpi=135,bbox_inches='tight')
print('wrote bead_frames.png')
