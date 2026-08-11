"""G -- the cosmological bundle, strung out and unfurled.
ONE privileged worldline (the bold bead of panels A/B), plotted in (Re tau~, Im tau~, r): the
antimatter black hole collapsing (RED, r<0) through r=0 and continuing as our matter universe
(BLUE, r>0). Real r, complex tau~ -- the three axes the cosmological bundle needs.

The branch is the NEGATIVE-imaginary one (arg r = +pi): sinh(w) = -i|r/A|^{3/2}, w=3tau~/2a.
  collapse run : |sinh|>1 -> Im tau~ = -pi/3 fixed, Re tau~ = -(2/3)arccosh(u)   (comes in from -Re)
  the LAP lift : |sinh|<1 -> Re tau~ = 0,           Im tau~ = -(2/3)arcsin(u) : -pi/3 -> 0
  matter univ. : r>0      -> Im tau~ = 0,           Re tau~ = +(2/3)arcsinh((r/A)^{3/2})
The collapse side and the cosmology side are STRUCTURALLY DIFFERENT curves -- the collapse is a run
plus a lift (the lap, here unfurled instead of jagged); the cosmology is a single real curve.

Seam points (the boing roots of panel E) land exactly:
  r=-2a/sqrt3 : |sinh|=2      -> Re tau~ = -(2/3)arccosh(2)
  r=+a/sqrt3  : |sinh|=1/sqrt2-> Re tau~ = +(2/3)arcsinh(1/sqrt2)
and arccosh(2) = 2 arcsinh(1/sqrt2) EXACTLY -> the two seam points sit at -2d and +d: the 2:1 (120/240)."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':15,'mathtext.fontset':'cm'})
BLUE,RED='#2471a3','#c0392b'
al=1.0; M2=2/(3*np.sqrt(3)); A=(M2*al**2)**(1/3); rmax=2.4
def cosmo(r):
    if r>=0: return (2/3)*np.arcsinh((r/A)**1.5), 0.0
    u=abs(r/A)**1.5
    if u<=1: return 0.0, -(2/3)*np.arcsin(u)
    return -(2/3)*np.arccosh(u), -np.pi/3
def curve(rs):
    P=np.array([cosmo(r) for r in rs]); return P[:,0],P[:,1],np.asarray(rs)

fig=plt.figure(figsize=(9.6,8.2)); ax=fig.add_subplot(111,projection='3d')
xr,yr,rr=curve(np.linspace(-rmax,-1e-6,600))    # antimatter: collapse run + lap lift
xb,yb,rb=curve(np.linspace(0,rmax,400))         # matter universe
ax.plot(xr,yr,rr,color=RED,lw=4.0)
ax.plot(xb,yb,rb,color=BLUE,lw=4.0)
# the three marked points: the boing roots / seam points
for r,lab,col,dz in [(-2/np.sqrt(3),r'$r{=}{-}2\alpha/\sqrt{3}$'+'\n(seam)',RED,-0.42),
                     (0.0,r'$r{=}0$',  'k',0.30),
                     (1/np.sqrt(3), r'$r{=}{+}\alpha/\sqrt{3}$'+'\n(seam)',BLUE,0.34)]:
    x,y=cosmo(r); ax.scatter([x],[y],[r],color='k',s=52,zorder=10)
    ax.text(x,y+0.06,r+dz,lab,fontsize=11.5,color=col)
ax.text(xr[0],yr[0],rr[0]*0.99,'antimatter\nblack hole',color=RED,fontsize=12.5)
ax.text(xb[-1],0,rb[-1]*0.99,'matter\nuniverse',color=BLUE,fontsize=12.5)
ax.text(-0.05,-0.62,-0.55,'the lap\n(unfurled)',color='0.3',fontsize=11)
ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',labelpad=8); ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',labelpad=8)
ax.set_zlabel(r'$r/\alpha$',labelpad=6)
ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.15,0.55); ax.set_zlim(-rmax,rmax)
ax.set_yticks([-1.0,-0.5,0.0,0.5]); ax.view_init(elev=17,azim=-62); ax.set_box_aspect((1,0.75,1),zoom=1.05)
ax.set_title('the cosmological bundle: antimatter black hole $\\to$ matter universe',fontsize=15,pad=4)
plt.tight_layout(); plt.savefig('G_explore.pdf',bbox_inches='tight'); plt.savefig('G_explore.png',dpi=150,bbox_inches='tight')
print('rendered')
