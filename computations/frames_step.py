import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
RED,BLUE,GREY,BLACK,PURPLE='#c0392b','#2471a3','#8a8f94','#111111','#7d3c98'
M2=2/(3*np.sqrt(3)); A=M2**(1/3); zmax=2.0

def hyperboloid(ax,mode,title):
    t=np.linspace(-zmax,zmax,50)
    ruling=lambda phi,sg:(np.cos(phi)-sg*t*np.sin(phi),np.sin(phi)+sg*t*np.cos(phi),t)
    if mode in ('univ','all'):
        for zc in np.linspace(-zmax,zmax,9):                 # black S^3 circles (universe)
            R=np.sqrt(1+zc**2); ph=np.linspace(0,2*np.pi,80)
            ax.plot(R*np.cos(ph),R*np.sin(ph),zc+0*ph,color=BLACK,lw=0.45,alpha=0.32)
        zz=np.linspace(-zmax,zmax,40); RR=np.sqrt(1+zz**2)  # grey photons at rest on the circles
        for phi in np.linspace(0,2*np.pi,15)[:-1]:
            ax.plot(RR*np.cos(phi),RR*np.sin(phi),zz,color=GREY,lw=0.5,alpha=0.5)
    if mode in ('nulls','all'):
        for phi in np.linspace(0,2*np.pi,16)[:-1]:
            x,y,z=ruling(phi,1);  ax.plot(x,y,z,color=RED, lw=0.6,alpha=0.5)   # red bundle
            x,y,z=ruling(phi,-1); ax.plot(x,y,z,color=BLUE,lw=0.6,alpha=0.5)   # blue bundle
        ph=np.linspace(0,2*np.pi,240); ax.plot(np.cos(ph),np.sin(ph),0*ph,color=PURPLE,lw=3.0)  # purple lap
    ax.view_init(elev=12,azim=-58); ax.set_box_aspect((1,1,1.3)); ax.set_axis_off()
    ax.set_title(title,fontsize=9.5)

def tau_of_r(r):
    z=(complex(r)/A)**1.5; return (2.0/3.0)*np.arcsinh(z)

def tau_r_frame(ax):
    rr=np.linspace(2.6,-2.6,600)                 # r = INDEPENDENT variable, sampled top->bottom
    T=np.array([tau_of_r(r) for r in rr])        # tau~(r), complex
    # faint horizontal plane at r=0 and the shadow of the curve onto it, so 'r vertical' is unmistakable
    gx=np.linspace(-1.9,1.9,2); gy=np.linspace(-1.3,0.2,2); GX,GY=np.meshgrid(gx,gy)
    ax.plot_surface(GX,GY,0*GX,color='0.9',alpha=0.25)
    ax.plot(T.real,T.imag,0*rr,color=BLUE,lw=0.8,alpha=0.4)        # shadow in the tau~ plane
    ax.plot(T.real,T.imag,rr,color=BLUE,lw=3.0)                    # THE curve: one blue line
    ax.scatter([0],[0],[0],color='k',s=26)
    # vertical guide lines at a few r to hammer home r is the vertical independent axis
    for r in [2.0,1.0,-1.0,-2.0]:
        tt=tau_of_r(r); ax.plot([tt.real,tt.real],[tt.imag,tt.imag],[0,r],color='0.7',lw=0.5)
    ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=8.5,labelpad=3)
    ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=8.5,labelpad=3)
    ax.set_zlabel(r'$r/\alpha$  (independent, vertical)',fontsize=9,labelpad=6)
    ax.set_zlim(-2.6,2.6); ax.view_init(elev=18,azim=-62); ax.tick_params(labelsize=7)
    ax.set_title(r'$\tilde\tau$ as a function of $r$: $r$ vertical, $\tilde\tau$ in the horizontal complex plane',fontsize=10)

fig=plt.figure(figsize=(15,10))
gs=fig.add_gridspec(2,3,height_ratios=[1,1.25])
axA=fig.add_subplot(gs[0,0],projection='3d'); hyperboloid(axA,'nulls','(1) red $+$ blue null bundles')
axB=fig.add_subplot(gs[0,1],projection='3d'); hyperboloid(axB,'univ', '(2) black $S^3$ circles $+$ grey photons')
axC=fig.add_subplot(gs[0,2],projection='3d'); hyperboloid(axC,'all',  '(3) all four together')
axT=fig.add_subplot(gs[1,:],projection='3d'); tau_r_frame(axT)
plt.tight_layout(); plt.savefig('frames_step.png',dpi=135,bbox_inches='tight')
print('wrote frames_step.png ; A=',round(A,4))
