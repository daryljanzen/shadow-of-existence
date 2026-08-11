import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,BLUE,GREY,BLACK,PURPLE='#c0392b','#2471a3','#8a8f94','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); zmax=2.0
fig=plt.figure(figsize=(15,5.6))

# frame 1: hyperboloid - all four faint + ONE thick red + ONE thick blue ruling
axH=fig.add_subplot(1,3,1,projection='3d')
for zc in np.linspace(-zmax,zmax,9):
    R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80)
    axH.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=BLACK,lw=0.4,alpha=0.22)
zz=np.linspace(-zmax,zmax,40); RR=np.sqrt(1+zz**2)
for phi in np.linspace(0,2*np.pi,13)[:-1]:
    axH.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=GREY,lw=0.5,alpha=0.32)
t=np.linspace(-zmax,zmax,50)
ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
for phi in np.linspace(0,2*np.pi,16)[:-1]:
    x,y,z=ruling(phi,1);  axH.plot(x,y,z,color=RED, lw=0.4,alpha=0.28)
    x,y,z=ruling(phi,-1); axH.plot(x,y,z,color=BLUE,lw=0.4,alpha=0.28)
ph=np.linspace(0,2*np.pi,240); axH.plot(np.cos(ph),np.sin(ph),0*ph,color=PURPLE,lw=3.0)
phi0=np.linspace(0,2*np.pi,16)[3]; tf=np.linspace(-zmax,zmax,50)
axH.plot(np.cos(phi0)+tf*np.sin(phi0),np.sin(phi0)-tf*np.cos(phi0),tf,color=BLUE,lw=3.4)
axH.plot(np.cos(phi0)-tf*np.sin(phi0),np.sin(phi0)+tf*np.cos(phi0),tf,color=RED, lw=3.4)
axH.view_init(elev=12,azim=-58); axH.set_box_aspect((1,1,1.3)); axH.set_axis_off()
axH.set_title('frame 1 - hyperboloid: one thick red $+$ one thick\nblue ruling (become the axes of frame 2)',fontsize=9)

# frame 2: tau-chi ; photons now CROSS the seam into the collapse side (signed r, integrated in tau~)
axO=fig.add_subplot(1,3,2); X0,X1=-1.15,1.15
def rsig(tt): s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=1e-6): return (rsig(tt+h)-rsig(tt-h))/(2*h)
for d in np.linspace(-1.8,2.0,13):
    axO.plot([X0,X1],[d-X0,d-X1],color=BLACK,lw=0.6,alpha=0.30)     # const r (diagonal)
for c in np.linspace(-0.95,0.95,11):
    if abs(c)>1e-6:
        axO.plot([c,c],[X0,X1],color=BLUE,lw=0.7,alpha=0.35)
        axO.plot([X0,X1],[c,c],color=RED, lw=0.7,alpha=0.35)
def photon(chi_seam,Ts=4.0):
    rhs=lambda ttil,y:[1.0/(1.0+rprime(ttil))]
    sP=solve_ivp(rhs,[0,Ts],[chi_seam],max_step=0.01,rtol=1e-8)
    sM=solve_ivp(rhs,[0,-Ts],[chi_seam],max_step=0.01,rtol=1e-8)
    ttil=np.concatenate([sM.t[::-1],sP.t]); chi=np.concatenate([sM.y[0][::-1],sP.y[0]]); tau=ttil-chi
    m=(chi>=X0)&(chi<=X1)&(tau>=X0)&(tau<=X1); return chi[m],tau[m]
for cs in np.linspace(-1.05,1.05,15):
    ch,ta=photon(cs)
    if len(ch)>2: axO.plot(ch,ta,color=GREY,lw=1.2,alpha=0.85)
axO.axvline(0.0,color=BLUE,lw=3.0,zorder=6)                          # chi=0 axis (thick blue)
axO.axhline(0.0,color=RED, lw=3.0,zorder=6)                          # tau=0 axis (thick red)
axO.plot([X0,X1],[-X0,-X1],color=PURPLE,lw=2.4,zorder=5)             # seam r=0
axO.set_xlim(X0,X1); axO.set_ylim(X0,X1); axO.set_aspect('equal')
axO.set_xlabel(r'$\chi$'); axO.set_ylabel(r'$\tau$',labelpad=-2); axO.tick_params(labelsize=7.5)
for s in ['top','right']: axO.spines[s].set_visible(False)
axO.set_title('frame 2 - $(\\tau,\\chi)$: grey photons CROSS the seam\ninto the collapse side ($r{<}0$, below purple)',fontsize=9)

# frame 3: r vs tau~ ; purple collapsed mix (real reading crosses seam; complex contour smooths it)
axR=fig.add_subplot(1,3,3,projection='3d')
def tau_of_r(r): z=(complex(r)/A)**1.5; return (2.0/3.0)*np.arcsinh(z)
rr=np.linspace(2.6,-2.6,500); T=np.array([tau_of_r(r) for r in rr])
axR.plot(T.real,T.imag,rr,color=PURPLE,lw=3.2,label='smooth complex contour')
# the REAL photon reading: tau~ real, signed r, straight through 0 (the cusp) - dashed
rre=np.linspace(2.6,-2.6,400); tre=np.array([(2.0/3.0)*np.arcsinh(np.sign(r)*np.abs(r/A)**1.5) for r in rre])
axR.plot(tre,0*rre,rre,color=GREY,lw=1.6,ls=(0,(5,3)),label='real photon reading ($\\mathrm{Im}=0$, cusp at $r{=}0$)')
axR.scatter([0],[0],[0],color='k',s=22)
axR.text2D(0.0,0.90,'purple: smooth contour ($\\tilde\\tau$ complex).\ndashed grey: the real photon crossing\n($\\tilde\\tau$ real, straight through, cusp at $r{=}0$).\nthe lap is what smooths the cusp.',fontsize=6.6,transform=axR.transAxes)
axR.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
axR.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
axR.set_zlabel(r'$r/\alpha$ (independent, vertical)',fontsize=8,labelpad=3)
axR.set_xlim(-2,2); axR.set_ylim(-1.2,0.2); axR.set_zlim(-2.6,2.6)
axR.view_init(elev=16,azim=-60); axR.tick_params(labelsize=6.5)
axR.set_title('frame 3 - $r$ vs $\\tilde\\tau$: purple contour vs real crossing',fontsize=9)
plt.tight_layout(); plt.savefig('build_all_frames.png',dpi=135,bbox_inches='tight')
print('wrote build_all_frames.png')
