"""Reassignment as TWO representations: dS4 hyperboloid + reassigned (tau,chi) frame.
Four structures tracked by colour across both:
  FUND red    = null ruling A  -> TIMELIKE fundamental worldlines (sinh^{2/3})
  FLAT green  = null ruling B  -> SPACELIKE flat Euclidean synchronous space ("the second ruling")
  PHOT blue   = at-rest cosh worldlines (timelike) -> NULL photon congruence
  SPH  purple = the S^3 spheres -> stay SPACELIKE (cosmological layers)"""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':10,'mathtext.fontset':'cm'})
FUND,FLAT,PHOT,SPH='#c0392b','#1e8449','#2471a3','#7d3c98'
fig=plt.figure(figsize=(11,5.2))

# ---- LEFT: dS4 hyperboloid ----
axA=fig.add_subplot(1,2,1,projection='3d')
zmax=1.9; t=np.linspace(-zmax,zmax,60)
ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
# S3 circles (purple, faint scaffold)
for zc in np.linspace(-zmax,zmax,9):
    R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80); axA.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=SPH,lw=0.6,alpha=0.5)
ph=np.linspace(0,2*np.pi,120); axA.plot(np.cos(ph),np.sin(ph),0*ph,color=SPH,lw=2.0)   # waist S3 bold
# ruling A (red) and ruling B (green), a few each faint
for phi in np.linspace(0,2*np.pi,8)[:-1]:
    x,y,z=ruling(phi,1); axA.plot(x,y,z,color=FUND,lw=0.8,alpha=0.22)
    x,y,z=ruling(phi,-1); axA.plot(x,y,z,color=FLAT,lw=0.8,alpha=0.22)
# at-rest cosh meridians (blue) faint
for phi in np.linspace(0,2*np.pi,8)[:-1]:
    zz=np.linspace(-zmax,zmax,50); RR=np.sqrt(1+zz**2); axA.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=PHOT,lw=0.8,alpha=0.28)
# bold representative of each
pa=np.linspace(0,2*np.pi,8)[1]
x,y,z=ruling(pa,1); axA.plot(x,y,z,color=FUND,lw=3.0)
x,y,z=ruling(pa,-1); axA.plot(x,y,z,color=FLAT,lw=3.0)
zz=np.linspace(-zmax,zmax,50); RR=np.sqrt(1+zz**2); pm=np.linspace(0,2*np.pi,8)[5]
axA.plot(RR*np.cos(pm),RR*np.sin(pm),zz,color=PHOT,lw=3.0)
axA.plot([0,0],[0,0],[-zmax,zmax],color='k',lw=0.7,ls=(0,(4,3))); axA.text(0,0,zmax+0.15,r'$X_0$',fontsize=8,ha='center')
axA.view_init(elev=10,azim=-60); axA.set_box_aspect((1,1,1.25)); axA.set_axis_off()
axA.text2D(0.0,1.0,'(a)',transform=axA.transAxes,fontsize=13,fontweight='bold')
axA.text2D(0.09,1.0,'de Sitter substrate (dS$_4$)',transform=axA.transAxes,fontsize=9.5,va='top')
axA.text2D(0.0,0.02,'null ruling A (red), null ruling B (green): both null\nat-rest worldlines (blue): timelike   $\\bullet$   $S^3$ (purple): space',transform=axA.transAxes,fontsize=7.4)

# ---- RIGHT: reassigned (tau,chi) frame ----
axB=fig.add_subplot(1,2,2)
axB.set_xlim(-1.05,1.05); axB.set_ylim(-1.05,1.05)
# fundamental timelike worldlines: constant chi (VERTICAL, red)
for x in np.linspace(-0.9,0.9,7): axB.plot([x,x],[-1,1],color=FUND,lw=1.3)
# flat Euclidean space: constant tau (HORIZONTAL, green)
for y in np.linspace(-0.9,0.9,7): axB.plot([-1,1],[y,y],color=FLAT,lw=1.3)
# cosmological S^3 layers: constant tau+chi (DIAGONAL slope -1, purple)
for c in np.linspace(-1.6,1.6,9): axB.plot([-1,1],[c+1,c-1],color=SPH,lw=1.1,alpha=0.9)
# photon null cone (blue) from a point, symmetric about the vertical timelike axis
x0,y0=0.0,-0.15
for m in [2.4,-2.4]:
    axB.plot([x0,x0+0.55],[y0,y0+0.55*m],color=PHOT,lw=2.2)
axB.plot(x0,y0,'o',color=PHOT,ms=4)
axB.text(0.02,0.55,'photon\nnull cone',color=PHOT,fontsize=7.6,ha='left')
# labels
axB.annotate('fundamental\nworldlines\n(timelike)',xy=(0.6,0.6),color=FUND,fontsize=7.6,ha='center')
axB.annotate('flat Euclidean\nspace (spacelike)',xy=(-0.62,-0.62),color=FLAT,fontsize=7.6,ha='center')
axB.annotate('$S^3$ layers\n$\\tilde\\tau=\\tau+\\chi$ (space)',xy=(0.62,-0.7),color=SPH,fontsize=7.6,ha='center')
axB.set_xlabel(r'$\chi$'); axB.set_ylabel(r'$\tau$')
axB.text(0.0,1.02,'(b)',transform=axB.transAxes,fontsize=13,fontweight='bold')
axB.text(0.09,1.02,r'reassigned $(\tau,\chi)$ frame: the characters swap',transform=axB.transAxes,fontsize=9.5,va='bottom')
axB.set_aspect('equal'); axB.tick_params(labelsize=8)
for s in ['top','right']: axB.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig('panels_reassign2.png',dpi=155,bbox_inches='tight')
print('ok')
