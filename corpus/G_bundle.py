"""G, extended: the cosmological bundle around the whole lap in (Re tau~, Im tau~, r).
cosmo(r) is lifted verbatim from corpus/G_explore.py -- the three branches keyed on |sinh|.
Added: the MATTER congruence (constant chi, the reassigned timelike bundle) and the PHOTON
congruence (dchi/dtau~ = 1/(1+r')) carried around the lap, through the lift, on the same contour."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE,RED,BLACK,GREY='#2471a3','#c0392b','#111111','#8a8a8a'
al=1.0; M2=2/(3*np.sqrt(3)); A=(M2*al**2)**(1/3); rmax=2.0
def cosmo(r):                                    # r -> (Re tau~, Im tau~)   [G_explore]
    if r>=0: return (2/3)*np.arcsinh((r/A)**1.5), 0.0
    u=abs(r/A)**1.5
    if u<=1: return 0.0, -(2/3)*np.arcsin(u)
    return -(2/3)*np.arccosh(u), -np.pi/3
def curve(rs):
    P=np.array([cosmo(r) for r in rs]); return P[:,0],P[:,1],np.asarray(rs)
# arc length s along the contour, and r'(s) = dr/ds -- the quantity the null cone rides on
def rp_of_r(r,h=1e-6):
    x0,y0=cosmo(max(r-h,-rmax)); x1,y1=cosmo(min(r+h,rmax))
    ds=np.hypot(x1-x0,y1-y0)
    return 2*h/ds if ds>0 else np.inf
fig=plt.figure(figsize=(13.2,6.4))
for pane,(elev,azim,ttl) in enumerate([(22,-62,'(a) the bundle, unfurled'),
                                       (90,-90,r'(b) from above: the $(\mathrm{Re}\,\tilde\tau,\mathrm{Im}\,\tilde\tau)$ contour')]):
    ax=fig.add_subplot(1,2,pane+1,projection='3d')
    # --- the privileged worldline (the bold bead)
    xr,yr,rr=curve(np.linspace(-rmax,-1e-6,700)); xb,yb,rb=curve(np.linspace(0,rmax,500))
    ax.plot(xr,yr,rr,color=RED,lw=3.4,zorder=6); ax.plot(xb,yb,rb,color=BLUE,lw=3.4,zorder=6)
    # --- THE MATTER BUNDLE: neighbouring worldlines, offset in chi (a rigid shift of Re tau~)
    for dch in np.linspace(-0.55,0.55,7):
        if abs(dch)<1e-9: continue
        ax.plot(xr+dch,yr,rr,color=RED,lw=.8,alpha=.42); ax.plot(xb+dch,yb,rb,color=BLUE,lw=.8,alpha=.42)
    # --- THE PHOTON BUNDLE: dchi/dtau~ = 1/(1+r'), integrated in r along the SAME contour
    for c0 in np.linspace(-0.5,0.5,9):
        rs=np.linspace(-rmax,rmax,900); ch=np.empty_like(rs); acc=c0
        i0=np.argmin(abs(rs)); ch[i0]=acc
        for i in range(i0+1,len(rs)):                     # outward
            rpv=rp_of_r(rs[i]); x0,y0=cosmo(rs[i-1]); x1,y1=cosmo(rs[i])
            acc+= np.hypot(x1-x0,y1-y0)/(1+rpv) if np.isfinite(rpv) else 0.0
            ch[i]=acc
        acc=c0
        for i in range(i0-1,-1,-1):                       # inward
            rpv=rp_of_r(rs[i]); x0,y0=cosmo(rs[i+1]); x1,y1=cosmo(rs[i])
            acc-= np.hypot(x1-x0,y1-y0)/(1+rpv) if np.isfinite(rpv) else 0.0
            ch[i]=acc
        X=np.array([cosmo(r)[0] for r in rs]); Y=np.array([cosmo(r)[1] for r in rs])
        ax.plot(X+ch-c0,Y,rs,color=BLACK,lw=.85,alpha=.55)
    # --- the loci
    for r,lab,mk in [(-2/np.sqrt(3),'back seam','o'),(-A,'turnaround','s'),(0.0,r'$r{=}0$','o'),
                     (1/np.sqrt(3),'front seam','o')]:
        x,y=cosmo(r); ax.scatter([x],[y],[r],color=BLACK,s=52,marker=mk,depthshade=False,
                                 edgecolors='w',linewidths=.8,zorder=14)
        ax.text(x,y+0.05,r+0.20,lab,fontsize=8.5,color=BLACK)
    ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=9,labelpad=2)
    ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=9,labelpad=2)
    ax.set_zlabel(r'$r/\alpha$',fontsize=9,labelpad=2)
    ax.set_title(ttl,fontsize=10,fontweight='bold'); ax.view_init(elev=elev,azim=azim)
    ax.tick_params(labelsize=7); ax.set_box_aspect((1.5,1,1.1))
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/bundle_complex.png',dpi=150,bbox_inches='tight')
print('lift extent: Im tau~ from %.4f to 0  (= -pi/3 = %.4f)'%(-np.pi/3,-np.pi/3))
print('wrote bundle_complex.png')
