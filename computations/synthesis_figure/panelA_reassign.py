"""Panel A - causal reassignment on the dS4 hyperboloid (a cut of the dS5 substrate).
Equilateral one-sheeted hyperboloid x^2+y^2-z^2=alpha^2 (a=b=alpha => null rulings = light cone).
Two straight null ruling families:  F1 (red)  -> reassigned TIMELIKE (fundamental worldlines, sinh^{2/3});
                                     F2 (blue) -> reassigned NULL (photon congruence).
Waist S^3 (z=0) and expanding at-rest S^3 slices (horizontal circles)."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})

zmax=1.9; t=np.linspace(-zmax,zmax,60)
def ruling(phi,sign):
    x=np.cos(phi)-sign*t*np.sin(phi); y=np.sin(phi)+sign*t*np.cos(phi); z=t
    return x,y,z
fig=plt.figure(figsize=(6.0,5.2)); ax=fig.add_subplot(111,projection='3d')
# at-rest S^3 slices (expanding circles) - light grey
for zc in np.linspace(-zmax,zmax,9):
    R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80)
    ax.plot(R*np.cos(ph),R*np.sin(ph),zc*np.ones_like(ph),color='0.7',lw=0.7,alpha=0.7)
# waist S^3 emphasised
ph=np.linspace(0,2*np.pi,120)
ax.plot(np.cos(ph),np.sin(ph),0*ph,color='0.25',lw=2.0)
# ruling families
phis=np.linspace(0,2*np.pi,10)[:-1]
for i,phi in enumerate(phis):
    x,y,z=ruling(phi,+1); ax.plot(x,y,z,color='#c0392b',lw=1.0,alpha=0.30)   # F1 red -> timelike
    x,y,z=ruling(phi,-1); ax.plot(x,y,z,color='#2471a3',lw=1.0,alpha=0.28)  # F2 blue -> null
# highlight ONE reassigned fundamental worldline (red) and ONE photon (blue)
x,y,z=ruling(phis[2],+1); ax.plot(x,y,z,color='#c0392b',lw=3.2)
x,y,z=ruling(phis[2],-1); ax.plot(x,y,z,color='#2471a3',lw=3.0)
# time axis
ax.plot([0,0],[0,0],[-zmax,zmax],color='k',lw=0.8,ls=(0,(4,3)))
ax.text(0,0,zmax+0.15,r'$X_0$ (time)',fontsize=9,ha='center')
# labels
ax.text(2.05,0.0,-1.1,'red ruling $\\to$ TIMELIKE\nfundamental worldline\n($\\sinh^{2/3}$ congruence)',color='#c0392b',fontsize=8.2,ha='center')
ax.text(-2.05,0.0,1.25,'blue ruling $\\to$ NULL\nphoton congruence',color='#2471a3',fontsize=8.2,ha='center')
ax.text(-1.15,-1.15,0.05,'waist $S^3$\n(comoving sphere)',color='0.2',fontsize=8.2,ha='center')
ax.text2D(0.0,0.99,'A',transform=ax.transAxes,fontsize=15,fontweight='bold')
ax.text2D(0.05,0.99,r'Causal reassignment on the dS$_4$ hyperboloid (a cut of dS$_5$)',transform=ax.transAxes,fontsize=10,va='top')
ax.view_init(elev=10,azim=-58); ax.set_box_aspect((1,1,1.25))
ax.set_axis_off()
plt.subplots_adjust(left=0.0,right=0.98,top=0.92,bottom=0.02)
plt.savefig('panelA_reassign.png',dpi=160,bbox_inches='tight',pad_inches=0.25)
plt.savefig('panelA_reassign.pdf',bbox_inches='tight')
print('ok')
