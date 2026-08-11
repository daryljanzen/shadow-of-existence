import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,BLUE,GREY,BLACK,PURPLE='#c0392b','#2471a3','#8a8f94','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); bound=np.pi/3
def tau_smooth(r): z=(complex(r)/A)**1.5; tt=(2.0/3.0)*np.arcsinh(z); return tt.real+1j*abs(tt.imag)  # +pi/3 wing
def tau_photon(r): return (2.0/3.0)*np.arcsinh(np.sign(r)*np.abs(r/A)**1.5)                            # real, cusp
rp=np.linspace(2.6,0,240); rn=np.linspace(0,-2.6,300)
Tsh=np.array([tau_photon(r) for r in rp])            # shared expansion leg (all collapse) - real
Tph=np.array([tau_photon(r) for r in rn])            # photon: stays real (cusp) for r<0
Tbl=np.array([tau_smooth(r) for r in rn])            # blue bundle: +pi/3 wing
Trd=np.array([tau_smooth(r) for r in rn])            # red bundle: -pi/3 wing (conjugate)

fig=plt.figure(figsize=(14,6.2))
# ---- 3D ----
ax=fig.add_subplot(1,2,1,projection='3d')
ax.plot(Tsh,0*rp,rp,color=PURPLE,lw=3.4)                       # r>0 shared: purple (the mix)
ax.plot(Tph,0*rn,rn,color=GREY,lw=2.6)                         # photon: real floor (grey)
ax.plot(Tbl.real,+np.abs(Tbl.imag),rn,color=BLUE,lw=2.6)      # blue: +pi/3 wing
ax.plot(Trd.real,-np.abs(Trd.imag),rn,color=RED, lw=2.6)      # red:  -pi/3 wing
ax.scatter([0],[0],[0],color='k',s=32,zorder=9)
ax.text(0,0,0.4,'seam $r{=}0$',fontsize=7)
ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
ax.set_zlabel(r'$r/\alpha$ (vertical)',fontsize=8,labelpad=2)
ax.set_xlim(-2,2); ax.set_ylim(-1.2,1.2); ax.set_zlim(-2.6,2.6)
ax.view_init(elev=15,azim=-62); ax.tick_params(labelsize=6.5)
ax.set_title('3D: purple (mix) on $r{>}0$; splits at the seam into\ngrey photon, blue $+\\pi\\alpha/3$, red $-\\pi\\alpha/3$',fontsize=9)

# ---- 2D (Im tau~ vs r): the split is cleanest here ----
ax2=fig.add_subplot(1,2,2)
ax2.plot(0*rp,rp,color=PURPLE,lw=3.6)                          # shared r>0 at Im=0
ax2.plot(0*rn,rn,color=GREY,lw=2.6)                            # photon stays Im=0
ax2.plot(+np.abs(Tbl.imag),rn,color=BLUE,lw=2.6)             # blue -> +pi/3
ax2.plot(-np.abs(Trd.imag),rn,color=RED, lw=2.6)             # red  -> -pi/3
ax2.scatter([0],[0],color='k',s=34,zorder=6); ax2.annotate('seam $r{=}0$: they split',xy=(0,0),xytext=(0.15,0.7),fontsize=8)
ax2.text(bound,-2.4,'$+\\pi\\alpha/3$',color=BLUE,fontsize=8,ha='center'); ax2.text(-bound,-2.4,'$-\\pi\\alpha/3$',color=RED,fontsize=8,ha='center')
ax2.text(0.02,-1.6,'photon\n(real)',color=GREY,fontsize=8)
ax2.set_xlabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=9); ax2.set_ylabel(r'$r/\alpha$ (vertical)',fontsize=9)
ax2.set_xlim(-1.3,1.3); ax2.set_ylim(-2.6,2.6)
for s in ['top','right']: ax2.spines[s].set_visible(False)
ax2.set_title(r'$\mathrm{Im}\,\tilde\tau$ vs $r$: purple mix, then three prongs',fontsize=9)
plt.tight_layout(); plt.savefig('lap_rounding.png',dpi=140,bbox_inches='tight')
print('wrote lap_rounding.png')
