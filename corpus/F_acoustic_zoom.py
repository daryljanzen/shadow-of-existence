"""The acoustic sector as successive zooms of P7 panel (D).  Structure lifted verbatim
from synthesis_figure.py's (D): grey = S^3 (const r), blue/red = the A and B congruences,
black = photons crossing the seam, thick blue/red = the r=0 diagonal."""
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, ConnectionPatch
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':9,'mathtext.fontset':'cm'})
BLUE,RED,BLACK,GREY,PURPLE='#2471a3','#c0392b','#111111','#8a8a8a','#7d3c98'
AN=7.4; A=2**(1/3)/np.sqrt(3); al=16.09          # Gyr per unit alpha
def rsig(tt):
    s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=None):
    h=h if h else max(1e-12,abs(tt)*1e-6+1e-14)
    return (rsig(tt+h)-rsig(tt-h))/(2*h)
t_of=lambda r:(2/3)*np.arcsinh((r/A)**1.5)
t0=(2/3)*np.arcsinh(np.sqrt(0.6934/0.3066)); r0=rsig(t0)
tSm=-(2/3)*np.arccosh(abs((-2/np.sqrt(3))/A)**1.5); tSp=t_of(1/np.sqrt(3))

def panelD(ax,S,loci,unit,scale):
    X0,X1=-S,S
    for d in np.linspace(-1.8*S,2.0*S,13): ax.plot([X0,X1],[d-X0,d-X1],color=GREY,lw=1.0,alpha=.6)
    for c in np.linspace(-0.9*S,0.9*S,9):
        ax.plot([c,c],[-c,X1],color=BLUE,lw=1.2,alpha=.8); ax.plot([c,c],[X0,-c],color=RED,lw=1.2,alpha=.8)
        ax.plot([-c,X1],[c,c],color=RED,lw=1.2,alpha=.8);  ax.plot([X0,-c],[c,c],color=BLUE,lw=1.2,alpha=.8)
    def photon(cs,Ts):
        rhs=lambda tt,y:[1.0/(1.0+rprime(tt))]
        sP=solve_ivp(rhs,[0,Ts],[cs],max_step=Ts/400,rtol=1e-9)
        sM=solve_ivp(rhs,[0,-Ts],[cs],max_step=Ts/400,rtol=1e-9)
        tt=np.concatenate([sM.t[::-1],sP.t]); ch=np.concatenate([sM.y[0][::-1],sP.y[0]]); ta=tt-ch
        m=(ch>=X0)&(ch<=X1)&(ta>=X0)&(ta<=X1); return ch[m],ta[m]
    for cs in np.linspace(-0.95*S,0.95*S,13):
        ch,ta=photon(cs,3.5*S)
        if len(ch)>2: ax.plot(ch,ta,color=BLACK,lw=1.2,alpha=.85)
    ax.plot([0,0],[0,X1],color=BLUE,lw=3.2,zorder=6); ax.plot([0,0],[X0,0],color=RED,lw=3.2,zorder=6)

    H=[]
    for lab,tt,ls,col in loci:
        if not (X0*2<tt<X1*2): continue
        ln,=ax.plot([X0,X1],[tt-X0,tt-X1],color=col,lw=1.7,ls=ls,alpha=.95,zorder=7,
                    label=lab+r'   ($\tilde\tau=$'+f'{tt*scale:.4g} '+unit.split(' / ')[1]+')')
        H.append(ln)
    leg=ax.legend(handles=H,fontsize=6.3,loc='upper left',framealpha=.92,
                  borderpad=.35,labelspacing=.32,handlelength=2.4)
    leg.set_zorder(20)
    ax.set_xlim(X0,X1); ax.set_ylim(X0,X1); ax.set_aspect('equal')
    tk=np.linspace(X0,X1,5)
    ax.set_xticks(tk); ax.set_yticks(tk)
    ax.set_xticklabels([f'{v*scale:.3g}' for v in tk],fontsize=6.6)
    ax.set_yticklabels([f'{v*scale:.3g}' for v in tk],fontsize=6.6)
    ax.set_xlabel(r'$\chi$  ('+unit+')',fontsize=8,labelpad=1)
    ax.set_ylabel(r'$\tau$  ('+unit+')',fontsize=8,labelpad=-2)
    for s_ in ['top','right']: ax.spines[s_].set_visible(False)

SPANS=[(1.15,'Gly / Gyr',al,'(a) the lap, seam to seam'),
       (1.0e-3,'Mly / Myr',al*1e3,r'(b) $\times1150$'),
       (5.0e-5,'Mly / Myr',al*1e3,r'(c) $\times20$: the acoustic sector')]
GRN,ORG,MAG='#1e8449','#d68910','#8e44ad'
LOCI=[[('back seam',tSm,(0,(5,2)),BLACK),('turnaround $+$ lift $+\\ r{=}0$',0.0,'-',BLACK),
       ('front seam',tSp,(0,(5,2)),BLACK),('today',t0,(0,(1,2)),MAG)],
      [('$r{=}0$ (the seam)',0.0,'-',BLACK),('recombination',t_of(r0/1090.9),(0,(5,2)),GRN)],
      [('$r{=}0$ (the seam)',0.0,'-',BLACK),(r'$z_{\rm onset}$',t_of(r0/6762),(0,(4,2)),ORG),
       ('matter--radiation equality',t_of(r0/3937),(0,(1,2)),MAG),
       ('recombination',t_of(r0/1090.9),(0,(5,2)),GRN)]]
fig,axs=plt.subplots(1,3,figsize=(13.2,4.8))
for ax,(S,u,sc,ttl),lo in zip(axs,SPANS,LOCI):
    panelD(ax,S,lo,u,sc); ax.set_title(ttl,fontsize=9.5,fontweight='bold')
for i in (0,1):
    Sn=SPANS[i+1][0]
    axs[i].add_patch(Rectangle((-Sn,-Sn),2*Sn,2*Sn,fill=False,ec=PURPLE,lw=1.5,zorder=14))
    for yA,yB in [(Sn,SPANS[i+1][0]),(-Sn,-SPANS[i+1][0])]:
        fig.add_artist(ConnectionPatch(xyA=(Sn,yA),coordsA=axs[i].transData,
                                       xyB=(-SPANS[i+1][0],yB),coordsB=axs[i+1].transData,
                                       color=PURPLE,lw=.9,ls=(0,(4,2)),zorder=20))
plt.tight_layout(); plt.savefig('/mnt/user-data/outputs/acoustic_zoom.png',dpi=155,bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/acoustic_zoom.pdf',bbox_inches='tight')
print('wrote acoustic_zoom.png/.pdf')
