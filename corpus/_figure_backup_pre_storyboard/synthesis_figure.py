"""P7 grand synthesis figure (fig:dS_SdS) - 3x2 portrait plate, full-page.
COLOUR CODE (settled convention, held across every panel):
  BLUE   = matter      (r>0)
  RED    = antimatter  (r<0); matter and antimatter exchanged at the branch point r=0
  BLACK  = photons     (the at-rest worldlines / null geodesics; the real seam-crossing sheet)
  GREY   = the S^3 layers (the universe)
  light grey = NEUTRAL, only where a panel draws none of the above (f(r) curves, rate regions).
Layout:  A Nariai slicing curve (dS5 substrate) | B dS4 background (null bundles)
         C layered handoff at the seam          | D observer (tau,chi) chart
         E the boing X_1(r)                      | F r vs complex tau~."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from scipy.integrate import solve_ivp
plt.rcParams.update({'font.family':'serif','font.size':16,'mathtext.fontset':'cm'})
BLUE,RED,BLACK,GREY,PURPLE='#2471a3','#c0392b','#111111','#8a8f94','#7d3c98'
NEU='#b7bbbf'
fig=plt.figure(figsize=(13.2,16.6))
gs=fig.add_gridspec(3,2,wspace=0.15,hspace=0.20,left=0.03,right=0.99,top=0.965,bottom=0.04)
al=1.0; M2=2/(3*np.sqrt(3)); A=(M2*al**2)**(1/3); zmax=2
LET=22; TIT=17; AX=16; TK=13; AN=14

# ============ (B) the de Sitter substrate hyperboloid ============
axA=fig.add_subplot(gs[0,1],projection='3d')
# Nariai slicing bead = fundamental cosmological worldline on dS4: blue ruling in -> 120deg arc -> r=0 -> red 240deg arc -> red ruling out.
# spun 20x = the representative bundle; opposite-sense conjugate bead drawn as rulings only. matter=BLUE, antimatter=RED.
_r2=np.sqrt(2); _S=np.array([0,-1.0,0]); _sp=np.linspace(0,1.6,2); _zcm=1.15
_din=np.array([-1,0,1.0])/_r2; _dout=np.array([1,0,-1.0])/_r2
_dou=np.array([1,0,1.0])/_r2;  _dod=np.array([-1,0,-1.0])/_r2
_phb=np.deg2rad(np.linspace(270,390,120)); _barc=np.array([np.cos(_phb),np.sin(_phb),0*_phb])
_phr=np.deg2rad(np.linspace(390,630,220)); _rarc=np.array([np.cos(_phr),np.sin(_phr),0*_phr])
def _ln(d): return _S[:,None]+np.outer(d,_sp)
def _rz(P,psi):
    c,sn=np.cos(psi),np.sin(psi); x,y,z=P; return np.array([x*c-y*sn,x*sn+y*c,z])
def _pl(P,psi,col,lw,al): Q=_rz(P,psi); axA.plot(Q[0],Q[1],Q[2],color=col,lw=lw,alpha=al)
_zzp=np.linspace(-_zcm,_zcm,40); _RRp=np.sqrt(1+_zzp**2)
for _phi in np.linspace(0,2*np.pi,16)[:-1]: axA.plot(_RRp*np.cos(_phi),_RRp*np.sin(_phi),_zzp,color=BLACK,lw=0.9,alpha=0.55)
for _zcv in np.linspace(-_zcm,_zcm,9):
    _Rc=np.sqrt(1+_zcv**2); _ph=np.linspace(0,2*np.pi,120); axA.plot(_Rc*np.cos(_ph),_Rc*np.sin(_ph),_zcv+0*_ph,color=GREY,lw=1.0,alpha=0.5)
for _k in range(20):
    _psi=2*np.pi*_k/20
    _pl(_ln(_din),_psi,BLUE,1.0,0.6); _pl(_barc,_psi,BLUE,1.0,0.6)
    _pl(_rarc,_psi,RED,1.0,0.6);      _pl(_ln(_dout),_psi,RED,1.0,0.6)
    _pl(_ln(_dou),_psi,RED,1.0,0.6);  _pl(_ln(_dod),_psi,BLUE,1.0,0.6)
_pl(_ln(_din),0,BLUE,3.0,1.0); _pl(_barc,0,BLUE,3.0,1.0); _pl(_rarc,0,RED,3.0,1.0); _pl(_ln(_dout),0,RED,3.0,1.0)
axA.plot([],[],color=BLUE,lw=3,label='matter'); axA.plot([],[],color=RED,lw=3,label='antimatter')
axA.plot([],[],color=BLACK,lw=1.2,label='photons'); axA.plot([],[],color=GREY,lw=1.2,label='$S^3$')
axA.view_init(elev=18,azim=-90); axA.set_box_aspect((1,1,0.9),zoom=1.2); axA.set_axis_off()
axA.text2D(0.0,1.03,r'(B) the $dS_4$ background',transform=axA.transAxes,fontsize=TIT,va='bottom',fontweight='bold')
axA.legend(loc='upper left',fontsize=AN-1,frameon=True)

# ============ (D) the observer (tau,chi) chart ============
axB=fig.add_subplot(gs[1,1]); X0,X1=-1.15,1.15
def rsig(tt): s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=1e-6): return (rsig(tt+h)-rsig(tt-h))/(2*h)
for d in np.linspace(-1.8,2.0,13): axB.plot([X0,X1],[d-X0,d-X1],color=GREY,lw=1.0,alpha=0.6)      # grey = S^3 (const r)
for c in np.linspace(-0.9,0.9,9):
    if abs(c)>1e-6:
        axB.plot([c,c],[-c,X1],color=BLUE,lw=1.0,alpha=0.6)                                      # vertical: blue above r=0 diagonal
        axB.plot([c,c],[X0,-c],color=RED, lw=1.0,alpha=0.6)                                      # vertical: red below
        axB.plot([-c,X1],[c,c],color=RED, lw=1.0,alpha=0.6)                                      # horizontal: red right of r=0 diagonal
        axB.plot([X0,-c],[c,c],color=BLUE,lw=1.0,alpha=0.6)                                      # horizontal: blue left
def photon(chi_seam,Ts=4.0):
    rhs=lambda ttil,y:[1.0/(1.0+rprime(ttil))]
    sP=solve_ivp(rhs,[0,Ts],[chi_seam],max_step=0.01,rtol=1e-8); sM=solve_ivp(rhs,[0,-Ts],[chi_seam],max_step=0.01,rtol=1e-8)
    ttil=np.concatenate([sM.t[::-1],sP.t]); chi=np.concatenate([sM.y[0][::-1],sP.y[0]]); tau=ttil-chi
    m=(chi>=X0)&(chi<=X1)&(tau>=X0)&(tau<=X1); return chi[m],tau[m]
for cs in np.linspace(-1.05,1.05,13):
    ch,ta=photon(cs)
    if len(ch)>2: axB.plot(ch,ta,color=BLACK,lw=1.3,alpha=0.8)                                    # black = photons crossing the seam
axB.plot([0,0],[0,X1],color=BLUE,lw=3.6,zorder=6); axB.plot([0,0],[X0,0],color=RED,lw=3.6,zorder=6)  # thick A axis: blue top / red bottom
axB.plot([0,X1],[0,0],color=RED,lw=1.0,alpha=0.6); axB.plot([X0,0],[0,0],color=BLUE,lw=1.0,alpha=0.6)  # central horizontal, thin like the others
axB.plot([X0,0],[-X0,0],color=RED, lw=3.2,zorder=5)                                              # r=0 line: red up-left
axB.plot([0,X1],[0,-X1],color=BLUE,lw=3.2,zorder=5)                                              # r=0 line: blue down-right
#axB.text(-1.08,1.05,'blue $A$ (const $\\chi$)',color=BLUE,fontsize=AN,va='top')
#axB.text(-1.08,-0.88,'red $B$ (const $\\tau$)',color=RED,fontsize=AN)
#axB.text(0.30,0.60,'photons (black,\ncross the seam)',color='k',fontsize=AN-1,ha='center')
axB.set_xlim(X0,X1); axB.set_ylim(X0,X1); axB.set_aspect('equal'); axB.set_xlabel(r'$\chi$',fontsize=AX,labelpad=1); axB.set_ylabel(r'$\tau$',fontsize=AX,labelpad=-6); axB.tick_params(labelsize=TK)
for s in ['top','right']: axB.spines[s].set_visible(False)
axB.text(0.0,1.03,r'(D) the observer $(\tau,\chi)$ chart',transform=axB.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (C) the layered handoff -- grey S^3 envelope; regions/seam NEUTRAL ============
axF=fig.add_subplot(gs[1,0])
sd=np.linspace(-2.3,2.3,600); sd_L=np.linspace(-2.3,0,600); sd_R=np.linspace(0,2.3,600)
env=np.abs(np.sinh(sd))**(2/3); env_L=np.abs(np.sinh(sd_L))**(2/3); env_R=np.abs(np.sinh(sd_R))**(2/3)
axF.axvspan(-2.5,0,color='0.94'); axF.axvspan(0,2.5,color='0.98')
axF.plot(sd_L,-env_L,color=RED, lw=3.2)   # bead 1, left: r<0 red
axF.plot(sd_R, env_R,color=BLUE,lw=3.2)   # bead 1, right: r>0 blue  (red->blue crossing r=0)
axF.plot(sd_L, env_L,color=RED, lw=3.2)   # bead 2, left: r>0 RED  (opposite-coloured conjugate)
axF.plot(sd_R,-env_R,color=BLUE,lw=3.2)   # bead 2, right: r<0 BLUE  (blue->red upward)
axF.fill_between(sd,-env,env,color=GREY,alpha=0.10)  # grey = S^3 layers
axF.axvline(0,color='0.4',lw=1.2,ls=(0,(3,3))); axF.plot(0,0,'o',color='k',ms=8,zorder=6)
axF.annotate('seam',xy=(0,0),xytext=(-0.9,2.35),fontsize=AN,ha='center',arrowprops=dict(arrowstyle='->',lw=0.8))
axF.text(-1.15,-2.35,'INWARD (collapse)\nleaf local rate\n$-$ radiation gravitates',color='0.25',fontsize=AN,ha='center',va='top')
axF.text(1.2,-2.35,'OUTWARD (expansion)\nfoliation stacking rate\n$-$ radiation-free',color='0.25',fontsize=AN,ha='center',va='top')
axF.text(-0.4,1.32,'deposits: $\\rho_r/\\rho_m\\approx2$ (acoustic scale)\n$\\eta$ (composition)',fontsize=AN,ha='left',bbox=dict(boxstyle='round,pad=0.35',fc='#f4f4f4',ec='0.7',lw=0.7))
axF.annotate('cooling leg = BBN',xy=(0.55,0.55),xytext=(0.85,-0.15),fontsize=AN,color='0.3',ha='left',arrowprops=dict(arrowstyle='->',color='0.4',lw=0.7))
axF.set_xlabel(r'$\tilde\tau/\alpha$',fontsize=AX); axF.set_ylabel(r'$r/\alpha$',fontsize=AX)
axF.set_xlim(-2.3,2.3); axF.set_ylim(-3.5,2.7); axF.tick_params(labelsize=TK)
for sp in ['top','right']: axF.spines[sp].set_visible(False)
axF.text(0.0,1.03,r'(C) the layered handoff at the seam',transform=axF.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (F) r vs complex tau~ ============
axC=fig.add_subplot(gs[2,1],projection='3d')
def tau_smooth(r): z=(complex(r)/A)**1.5; tt=(2.0/3.0)*np.arcsinh(z); return tt.real+1j*abs(tt.imag)
def tau_photon(r): return (2.0/3.0)*np.arcsinh(np.sign(r)*np.abs(r/A)**1.5)
rmax=2.6
rpos=np.linspace(rmax,1e-4,240); rn=np.linspace(-1e-4,-rmax,300)
axC.plot([tau_photon(r) for r in rpos],0*rpos,rpos,color=BLUE,lw=3.4)      # matter leg r>0 (our universe) blue
axC.plot([tau_photon(r) for r in rn],0*rn,rn,color=BLACK,lw=3.0)            # photon sheet (real cusp) black
Tb=np.array([tau_smooth(r) for r in rn])
axC.plot(Tb.real,+np.abs(Tb.imag),rn,color=RED,lw=3.0)                      # +wing r<0: antimatter progenitor (came from)
axC.plot(Tb.real,-np.abs(Tb.imag),rn,color=RED, lw=3.0)                     # -wing r<0: antimatter universe (we produce) -- conjugate mirror
axC.scatter([0],[0],[0],color='k',s=34,zorder=9)
axC.text(0,-1.4,0.9,'seam $r{=}0$',fontsize=AN)
axC.text(0.9,0.0,1.9,'matter (us)',color=BLUE,fontsize=AN-1)
axC.text(-1.7,0.7,-1.9,'antimatter\n(came from / we make)',color=RED,fontsize=AN-1)
axC.text(-1.6,0.0,-0.4,'photons',color='0.25',fontsize=AN-1)
#axC.text2D(-0.04,0.96,'real leg: coincide (purple). Past the seam:\nphoton (black), blue $+\\pi\\alpha/3$, red $-\\pi\\alpha/3$\n($\\tilde\\tau{\\to}\\bar{\\tilde\\tau}$; period $2\\pi\\alpha/3$, $r{\\mapsto}e^{2\\pi i/3}r$).',transform=axC.transAxes,fontsize=AN-1,va='top')
axC.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=AX-2,labelpad=6)
axC.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$',fontsize=AX-2,labelpad=6)
axC.set_zlabel(r'$r/\alpha$',fontsize=AX-2,labelpad=7)
axC.set_xlim(-2,2); axC.set_ylim(-1.2,1.2); axC.set_zlim(-rmax,rmax)
axC.set_xticks([-2,0,2]); axC.set_yticks([-1,0,1]); axC.set_zticks([-2,0,2])
axC.set_box_aspect((1,1,1),zoom=1.2); axC.view_init(elev=15,azim=-55); axC.tick_params(labelsize=TK-1,pad=2)
axC.text2D(0.0,1.01,r'(F) $r$ vs complex $\tilde\tau$',transform=axC.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (E) the lap flattened  (blue legs, purple lap; one symmetric Nariai line) ============
axD=fig.add_subplot(gs[2,0])
rA=1/np.sqrt(3); rB=-2/np.sqrt(3)
rl=np.linspace(rB,rA,400); X1lap=-np.cos(2*np.pi*rl/np.sqrt(3))
rR=np.linspace(rA,1.35,60); rLl=np.linspace(-1.9,rB,60)                     # extended symmetrically to 'infinity'
axD.plot(rLl,0.5+np.pi*(rLl-rB),color=RED,lw=3.4)                          # left leg (r<0) red
_mR=rl<=0; _mB=rl>=0
axD.plot(rl[_mR],X1lap[_mR],color=RED,lw=3.6)                              # lap r<0 red
axD.plot(rl[_mB],X1lap[_mB],color=BLUE,lw=3.6)
axD.plot(rR,0.5+np.pi*(rR-rA),color=BLUE,lw=3.4)             # right leg (r>0) blue
for rr,lab,dy in [(rA,'$+\\alpha/\\sqrt{3}$',0.22),(0.0,'$r{=}0$ ($X_1{=}-\\alpha$)',-0.26),(rB,'$-2\\alpha/\\sqrt{3}$',0.22)]:
    yy=-np.cos(2*np.pi*rr/np.sqrt(3)); axD.plot(rr,yy,'o',color='0.2',ms=9); axD.axvline(rr,color='0.85',lw=0.8,ls=':')
    axD.annotate(lab,xy=(rr,yy),xytext=(rr-0.3,yy+dy),fontsize=AN,ha='center')
axD.axhline(0,color='0.6',lw=0.9)
axD.set_xlabel(r'$r/\alpha$',fontsize=AX-1); axD.set_ylabel(r'$X_1/\alpha$',fontsize=AX)
axD.set_xlim(-2.0,1.4); axD.set_ylim(-2.2,2.4); axD.tick_params(labelsize=TK)
for sp in ['top','right']: axD.spines[sp].set_visible(False)
axD.text(0.0,1.03,r'(E) the boing in $X_1$',transform=axD.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (A) the Nariai slicing curve, from overhead (N-pole projection) ============
axE=fig.add_subplot(gs[0,0])
_thf=np.linspace(0,2*np.pi,200); axE.plot(np.cos(_thf),np.sin(_thf),color='0.75',lw=0.8)          # throat circle
_hg=np.array([0,-2.0]); _tp=np.array([np.sqrt(3)/2,-0.5]); _dt=np.array([0.5,np.sqrt(3)/2])
axE.plot([_hg[0],_tp[0]],[_hg[1],_tp[1]],color=BLUE,lw=3.2)                                        # blue ruling: hinge -> tangent
_pb=np.deg2rad(np.linspace(330,450,120)); axE.plot(np.cos(_pb),np.sin(_pb),color=BLUE,lw=3.2)      # blue 120 arc -> r=0 (top)
_pr=np.deg2rad(np.linspace(90,330,200));  axE.plot(np.cos(_pr),np.sin(_pr),color=RED,lw=3.2)       # red 240 arc
_se=np.linspace(0,1.9,2); axE.plot(_tp[0]+_se*_dt[0],_tp[1]+_se*_dt[1],color=RED,lw=3.2)           # red exit up the tangent (seam)
axE.plot(0,1,'o',color='k',ms=4); axE.annotate(r'$r{=}0$',(0,1),(0.12,1.02),fontsize=AN)
axE.plot(*_hg,'o',color='k',ms=4); axE.annotate('hinge',_hg,(_hg[0]+0.12,_hg[1]-0.02),fontsize=AN)
axE.annotate('seam',(_tp[0]+1.9*_dt[0],_tp[1]+1.9*_dt[1]),(_tp[0]+1.9*_dt[0]-0.2,_tp[1]+1.9*_dt[1]+0.12),fontsize=AN)
axE.set_aspect('equal'); axE.set_xlim(-1.7,2.6); axE.set_ylim(-2.3,1.9); axE.set_axis_off()
axE.text(0.0,1.03,r'(A) the Nariai slicing curve ($dS_5$ substrate)',transform=axE.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

plt.savefig('dS-SdS-synthesis.pdf',bbox_inches='tight'); plt.savefig('dS-SdS-synthesis.png',dpi=150,bbox_inches='tight')
print('dS-SdS-synthesis.png')
