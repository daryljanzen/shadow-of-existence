"""P7 second figure (fig:bead_frames): the four bundles in the three representations.
(a) substrate hyperboloid   (b) observer (tau,chi) chart   (c) r vs complex tau~.
Colours match the plate: BLUE=A (outgoing null bundle), RED=B (incoming null bundle / synchronous
space), PHL light-blue=at-rest photon congruence, BLACK=S^3 universe, PURPLE=lap / the collapsed real leg."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,PHOT,PHL,BLACK,PURPLE='#c0392b','#2471a3','#5dade2','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); zmax=2.0
fig=plt.figure(figsize=(14.5,5.2))

# (a) hyperboloid
axH=fig.add_subplot(1,3,1,projection='3d')
for zc in np.linspace(-zmax,zmax,9):
    R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80); axH.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=BLACK,lw=0.4,alpha=0.25)
zz=np.linspace(-zmax,zmax,40); RR=np.sqrt(1+zz**2)
for phi in np.linspace(0,2*np.pi,13)[:-1]: axH.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=PHL,lw=0.5,alpha=0.5)
t=np.linspace(-zmax,zmax,50); ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
for phi in np.linspace(0,2*np.pi,16)[:-1]:
    x,y,z=ruling(phi,-1); axH.plot(x,y,z,color=PHOT,lw=0.5,alpha=0.45)
    x,y,z=ruling(phi,1);  axH.plot(x,y,z,color=RED, lw=0.5,alpha=0.45)
ph=np.linspace(0,2*np.pi,240); axH.plot(np.cos(ph),np.sin(ph),0*ph,color=PURPLE,lw=3.0)
axH.view_init(elev=12,azim=-58); axH.set_box_aspect((1,1,1.3)); axH.set_axis_off()
axH.text2D(0.0,1.0,'(a)',transform=axH.transAxes,fontsize=12,fontweight='bold')
axH.text2D(0.12,1.0,'substrate hyperboloid',transform=axH.transAxes,fontsize=9,va='top')

# (b) observer chart
axO=fig.add_subplot(1,3,2); X0,X1=-1.15,1.15
def rsig(tt): s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=1e-6): return (rsig(tt+h)-rsig(tt-h))/(2*h)
for d in np.linspace(-1.8,2.0,13): axO.plot([X0,X1],[d-X0,d-X1],color=BLACK,lw=0.5,alpha=0.28)   # const r
for c in np.linspace(-0.95,0.95,9): axO.plot([X0,X1],[c,c],color=RED,lw=0.9,alpha=0.5)           # B synchronous const tau
for c in np.linspace(-0.9,0.9,10):                                                                # photons const chi (cross seam)
    axO.plot([c,c],[X0,X1],color=PHL,lw=0.9,alpha=0.55)
def nullc(chi_seam,Ts=4.0):                                                                        # blue A null congruence crossing seam
    rhs=lambda ttil,y:[1.0/(1.0+rprime(ttil))]
    sP=solve_ivp(rhs,[0,Ts],[chi_seam],max_step=0.01,rtol=1e-8); sM=solve_ivp(rhs,[0,-Ts],[chi_seam],max_step=0.01,rtol=1e-8)
    ttil=np.concatenate([sM.t[::-1],sP.t]); chi=np.concatenate([sM.y[0][::-1],sP.y[0]]); tau=ttil-chi
    m=(chi>=X0)&(chi<=X1)&(tau>=X0)&(tau<=X1); return chi[m],tau[m]
for cs in np.linspace(-1.05,1.05,13):
    ch,ta=nullc(cs);
    if len(ch)>2: axO.plot(ch,ta,color=PHOT,lw=1.0,alpha=0.7)
axO.plot([X0,X1],[-X0,-X1],color=PURPLE,lw=2.4,zorder=5)
axO.set_xlim(X0,X1); axO.set_ylim(X0,X1); axO.set_aspect('equal'); axO.set_xlabel(r'$\chi$'); axO.set_ylabel(r'$\tau$',labelpad=-2); axO.tick_params(labelsize=7.5)
for s in ['top','right']: axO.spines[s].set_visible(False)
axO.text(0.0,1.02,'(b)',transform=axO.transAxes,fontsize=12,fontweight='bold'); axO.text(0.12,1.02,'observer $(\\tau,\\chi)$ chart',transform=axO.transAxes,fontsize=9,va='bottom')

# (c) r vs complex tau~ : collapse on the real leg (purple), three sheets past the seam
axR=fig.add_subplot(1,3,3,projection='3d')
def tau_smooth(r): z=(complex(r)/A)**1.5; tt=(2.0/3.0)*np.arcsinh(z); return tt.real+1j*abs(tt.imag)
def tau_photon(r): return (2.0/3.0)*np.arcsinh(np.sign(r)*np.abs(r/A)**1.5)
rp=np.linspace(2.6,0,240); rn=np.linspace(0,-2.6,300)
axR.plot([tau_photon(r) for r in rp],0*rp,rp,color=PURPLE,lw=3.2)          # shared real leg (collapse) purple
axR.plot([tau_photon(r) for r in rn],0*rn,rn,color=PHL,lw=2.4)             # photon sheet (real cusp) light blue
Tb=np.array([tau_smooth(r) for r in rn]); axR.plot(Tb.real,+np.abs(Tb.imag),rn,color=PHOT,lw=2.4)  # +pi/3
axR.plot(Tb.real,-np.abs(Tb.imag),rn,color=RED,lw=2.4)                     # -pi/3
axR.scatter([0],[0],[0],color='k',s=26,zorder=9)
axR.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2); axR.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2); axR.set_zlabel(r'$r/\alpha$',fontsize=8,labelpad=2)
axR.set_xlim(-2,2); axR.set_ylim(-1.2,1.2); axR.set_zlim(-2.6,2.6); axR.view_init(elev=15,azim=-62); axR.tick_params(labelsize=6.3)
axR.text2D(0.0,1.0,'(c)',transform=axR.transAxes,fontsize=12,fontweight='bold'); axR.text2D(0.12,1.0,r'$r$ vs complex $\tilde\tau$',transform=axR.transAxes,fontsize=9,va='top')
plt.tight_layout(); plt.savefig('bead-frames.pdf',bbox_inches='tight'); plt.savefig('bead-frames.png',dpi=140,bbox_inches='tight')
print('wrote bead-frames.pdf/.png')
