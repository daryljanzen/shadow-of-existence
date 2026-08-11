import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,BLUE,GREY,BLACK,PURPLE='#c0392b','#2471a3','#8a8f94','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); zmax=2.0
fig=plt.figure(figsize=(15,5.4))

# frame 1: hyperboloid
axH=fig.add_subplot(1,3,1,projection='3d')
t=np.linspace(-zmax,zmax,50)
ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
for phi in np.linspace(0,2*np.pi,16)[:-1]:
    x,y,z=ruling(phi,1);  axH.plot(x,y,z,color=RED, lw=0.6,alpha=0.5)
    x,y,z=ruling(phi,-1); axH.plot(x,y,z,color=BLUE,lw=0.6,alpha=0.5)
ph=np.linspace(0,2*np.pi,240); axH.plot(np.cos(ph),np.sin(ph),0*ph,color=PURPLE,lw=3.0)
axH.view_init(elev=12,azim=-58); axH.set_box_aspect((1,1,1.3)); axH.set_axis_off()
axH.set_title('frame 1 - hyperboloid:\nred $+$ blue null bundles',fontsize=9.5)

# frame 2: tau-chi
axO=fig.add_subplot(1,3,2); X0,X1=-1.15,1.15
for c in np.linspace(-0.95,0.95,13):
    axO.plot([c,c],[X0,X1],color=BLUE,lw=1.0,alpha=0.6)
    axO.plot([X0,X1],[c,c],color=RED, lw=1.0,alpha=0.6)
axO.plot([X0,X1],[-X0,-X1],color=PURPLE,lw=2.6)
axO.set_xlim(X0,X1); axO.set_ylim(X0,X1); axO.set_aspect('equal')
axO.set_xlabel(r'$\chi$'); axO.set_ylabel(r'$\tau$',labelpad=-2); axO.tick_params(labelsize=7.5)
for s in ['top','right']: axO.spines[s].set_visible(False)
axO.set_title('frame 2 - $(\\tau,\\chi)$: blue$=$const $\\chi$,\nred$=$const $\\tau$, purple$=r{=}0$',fontsize=9.5)

# frame 3: r vertical vs tau~ complex; the orbit collapses to one curve
axR=fig.add_subplot(1,3,3,projection='3d')
def tau_of_r(r): z=(complex(r)/A)**1.5; return (2.0/3.0)*np.arcsinh(z)
rr=np.linspace(2.6,-2.6,500); T=np.array([tau_of_r(r) for r in rr])
axR.plot(T.real,T.imag,rr,color=BLUE,lw=3.0)                       # the one blue curve
# markers along the r>0 leg = 'all the blue rulings pile here'
for r in [2.2,1.6,1.0,0.5]:
    tt=tau_of_r(r); axR.scatter([tt.real],[tt.imag],[r],color=BLUE,s=34,edgecolor='k',lw=0.4,zorder=8)
axR.scatter([0],[0],[0],color='k',s=24)
axR.text2D(0.0,0.90,'rotate the blue curve around the equator $\\Rightarrow$\nevery ruling lands on THIS one curve\n($r$ is globally a function of $\\tilde\\tau$: the orbit\ncollapses here; it only fans out if $\\tilde\\tau$ goes complex)',fontsize=7.0,transform=axR.transAxes)
axR.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
axR.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8,labelpad=2)
axR.set_zlabel(r'$r/\alpha$ (independent, vertical)',fontsize=8,labelpad=3)
axR.set_xlim(-2,2); axR.set_ylim(-1.2,0.2); axR.set_zlim(-2.6,2.6)
axR.view_init(elev=16,azim=-60); axR.tick_params(labelsize=6.5)
axR.set_title('frame 3 - $r$ vs $\\tilde\\tau$: the blue orbit collapses',fontsize=9.5)
plt.tight_layout(); plt.savefig('build1_frames.png',dpi=135,bbox_inches='tight')
print('wrote build1_frames.png')
