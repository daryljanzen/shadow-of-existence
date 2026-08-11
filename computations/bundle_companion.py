import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
FUND,PHOT,SPH='#c0392b','#2471a3','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3)
def rc(tt): return A*(np.sinh(1.5*tt))**(2/3)   # complex r(tau~)

fig=plt.figure(figsize=(15,6.2))
# ---- panel 1: blues only (Im tau~ >=0 half = one bundle) ----
def draw(ax,both):
    U=np.linspace(-1.5,1.5,140)
    vmax=np.pi/3
    Vs = np.linspace(-vmax,vmax,25) if both else np.linspace(0,vmax,13)
    # rulings = constant-Im(tau~) lines (each a "rotated" ruling), colored by wing
    for v in Vs:
        r=np.array([rc(u+1j*v) for u in U]).real
        if abs(v)<1e-9: c,lw,al=SPH,2.6,1.0
        elif v>0:       c,lw,al=PHOT,1.0,0.7
        else:           c,lw,al=FUND,1.0,0.7
        ax.plot(U*0+U, U*0+v, r, color=c,lw=lw,alpha=al)   # (Re tau~, Im tau~, r)
    # a few along-ruling (constant u) hoops to show the sweep
    for u in np.linspace(-1.2,1.2,9):
        r=np.array([rc(u+1j*v) for v in np.linspace(Vs[0],Vs[-1],60)]).real
        ax.plot(u+0*np.linspace(Vs[0],Vs[-1],60), np.linspace(Vs[0],Vs[-1],60), r, color='0.6',lw=0.5,alpha=0.5)
    # seam locus: where Re r = 0  (u=0 line, and the turnarounds)
    vv=np.linspace(Vs[0],Vs[-1],120); rseam=np.array([rc(0+1j*v) for v in vv]).real
    ax.plot(0*vv, vv, rseam, color='k', lw=1.8)
    ax.scatter([0],[0],[0],color='k',s=30)
    ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=-2)
    ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=-2)
    ax.set_zlabel(r'$r/\alpha$',fontsize=8,labelpad=-2)
    ax.view_init(elev=16,azim=-60); ax.tick_params(labelsize=6.5,pad=-1)
ax1=fig.add_subplot(1,2,1,projection='3d'); draw(ax1,False)
ax1.set_title('blue bundle only: rulings = constant-$\\mathrm{Im}\\,\\tilde\\tau$ (the rotation),\nswept from the real expansion leg (purple) up to $+\\pi\\alpha/3$',fontsize=8.5)
ax2=fig.add_subplot(1,2,2,projection='3d'); draw(ax2,True)
ax2.set_title('blue + red (complementary) bundles: the two wings $\\pm\\pi\\alpha/3$,\nthe purple lap the shared real leg; black = seam locus $r(0{+}iv)$',fontsize=8.5)
plt.tight_layout(); plt.savefig('bundle_companion.png',dpi=140,bbox_inches='tight')
print('wrote bundle_companion.png ; A=',round(A,4),' bound pi/3=',round(np.pi/3,4))
# diagnostics: is the seam locus (u=0) real or does Re r wander?
for v in [0,0.3,0.6,np.pi/3,0.9]:
    print(f' r(0+{v:.3f}i) = {rc(1j*v):.4f}')
