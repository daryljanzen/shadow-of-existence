"""P7 grand synthesis figure (fig:dS_SdS) - 3x2 portrait plate, full-page.
DRIVING DOC (r1036+): ../SYNTHESIS_FIGURE_STORYBOARD.md  (the standing working doc for this figure;
  figure-work queue in its section 7 (E1-E6), incl. both-bundle A/E, the new unfurled-complex panel G,
  and purple restored as the honest both-bundle coincidence marker on A).
COLOUR CODE (settled convention, held across every panel):
  BLUE   = matter      (r>0)
  RED    = antimatter  (r<0); matter and antimatter exchanged at the branch point r=0
  BLACK  = photons     (the at-rest worldlines / null geodesics; the real seam-crossing sheet)
  GREY   = the S^3 layers (the universe)
  light grey = NEUTRAL, only where a panel draws none of the above (f(r) curves, rate regions).
Layout:  A Nariai slicing curve (dS5 substrate) | B dS4 background (null bundles)
         C layered handoff at the seam          | D observer (tau,chi) chart
         E the boing X_1(r)                      | F the cosmological bundle, unfurled."""
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
# Rebuilt r4267, analytically.  Surface -X0^2+X1^2+X2^2 = al^2, waist X0=0 = THE RING.
# Rulings are STRAIGHT ambient lines tangent to the ring at t=0:
#     L_{A,B}(t) = (al cos@ -/+ t sin@ , al sin@ +/- t cos@ , t)
# HINGES run parallel to the axis at rho=2al and meet the surface where
#     4al^2 - X0^2 = al^2  =>  X0 = +/- sqrt3 al   -- the six PUNCTURES.
# LAP LOCI derived on the Nariai member from f(r)=1-2M/r-r^2/al^2, M=al/(3sqrt3):
#     f=0 seam r=al/sqrt3 ; f=1 turnaround r^3=-2M al^2 ; f=2 Euclidean null
#     r^3+al^2 r+2M al^2=0 ; branch point r=0.  Azimuth by phi = 2 pi r /(sqrt3 al),
#     i.e. the panel's own 207.8461 deg per unit r, anchored at the branch point.
axA=fig.add_subplot(gs[0,1],projection='3d')
_MN=al/(3*np.sqrt(3)); _f=lambda r: 1-2*_MN/r-r**2/al**2
_rs=al/np.sqrt(3); _rt=-(2*_MN*al**2)**(1/3)
_rt3=np.roots([1,0,al**2,2*_MN*al**2]); _re=float([x.real for x in _rt3 if abs(x.imag)<1e-12][0])
assert abs(_f(_rs))<1e-12 and abs(_f(_rt)-1)<1e-12 and abs(_f(_re)-2)<1e-12
_lap=lambda r: (np.rad2deg(2*np.pi*r/(np.sqrt(3)*al))+240.0)%360.0   # 0 at the BACK seam
_S3=np.sqrt(3)*al; _ZC=1.95; _N=24
_HL=np.deg2rad(-90.0)                       # the bold bead's tangency, toward the reader

def _rul(th,t,sense):
    sg=1.0 if sense=='A' else -1.0
    return (al*np.cos(th)-sg*t*np.sin(th), al*np.sin(th)+sg*t*np.cos(th), t)

_zz=np.linspace(-_ZC,_ZC,40); _RR=np.sqrt(al**2+_zz**2)
for _phi in np.linspace(0,2*np.pi,16)[:-1]:
    axA.plot(_RR*np.cos(_phi),_RR*np.sin(_phi),_zz,color=BLACK,lw=0.7,alpha=0.30)
for _zcv in np.linspace(-_ZC,_ZC,9):
    _Rc=np.sqrt(al**2+_zcv**2); _ph=np.linspace(0,2*np.pi,120)
    axA.plot(_Rc*np.cos(_ph),_Rc*np.sin(_ph),_zcv+0*_ph,color=GREY,lw=0.9,alpha=0.42)

_tlo=np.linspace(-_ZC,0,60); _thi=np.linspace(0,_ZC,60)
for _k in range(_N):
    _th=2*np.pi*_k/_N
    for _sn,_c0,_c1 in (('A',RED,BLUE),('B',BLUE,RED)):
        for _tt,_cc in ((_tlo,_c0),(_thi,_c1)):
            _x,_y,_z=_rul(_th,_tt,_sn); axA.plot(_x,_y,_z,color=_cc,lw=0.75,alpha=0.55)

_ph=np.linspace(0,2*np.pi,400)
axA.plot(al*np.cos(_ph),al*np.sin(_ph),0*_ph,color=BLACK,lw=1.4,alpha=0.75)
_lp=np.linspace(0,2*np.pi,300)
for _i in range(len(_lp)-1):
    _a=_HL+_lp[_i:_i+2]
    axA.plot(al*np.cos(_a),al*np.sin(_a),[0,0],
             color=RED if _lp[_i]<4*np.pi/3 else BLUE,lw=4.2,solid_capstyle='round')
for _tt,_cc in ((_tlo,RED),(_thi,BLUE)):
    _x,_y,_z=_rul(_HL,_tt,'A'); axA.plot(_x,_y,_z,color=_cc,lw=3.0)

_LOCI=[(0.0,'seam','o',_rs),(_lap(_rt),'turnaround','s',_rt),
       (_lap(_re),'unit speed','D',_re),(240.0,r'$r=0$','o',0.0)]
for _ang,_lab,_mk,_rv in _LOCI:
    _a=_HL+np.deg2rad(_ang)
    axA.scatter([al*np.cos(_a)],[al*np.sin(_a)],[0],color=BLACK,s=46,marker=_mk,
                depthshade=False,edgecolors='w',linewidths=.8,zorder=14)
    axA.text(1.80*al*np.cos(_a),1.80*al*np.sin(_a),0.16,_lab,fontsize=AN-3.5,
             color=BLACK,ha='center',zorder=15)

for _n in range(3):
    _pp=_HL+np.deg2rad(60+120*_n)
    _zh=np.linspace(-_S3,_S3,30)
    axA.plot(np.full_like(_zh,2*al*np.cos(_pp)),np.full_like(_zh,2*al*np.sin(_pp)),_zh,
             color=PURPLE,lw=1.5,ls=(0,(5,3)),alpha=0.9)
    for _sg in (+1,-1):
        axA.scatter([2*al*np.cos(_pp)],[2*al*np.sin(_pp)],[_sg*_S3],color=PURPLE,s=52,
                    marker='s',depthshade=False,edgecolors='k',linewidths=.8,zorder=16)
        axA.text(2.30*al*np.cos(_pp),2.30*al*np.sin(_pp),_sg*_S3*1.06,
                 rf'$p_{{{_n+1}}}^{{{"+" if _sg>0 else "-"}}}$',fontsize=AN-3.5,
                 color=PURPLE,ha='center',zorder=17)

axA.plot([],[],color=BLUE,lw=3,label='matter'); axA.plot([],[],color=RED,lw=3,label='antimatter')
axA.plot([],[],color=BLACK,lw=1.2,label='the ring'); axA.plot([],[],color=PURPLE,lw=1.5,ls=(0,(5,3)),label='hinges')
axA.view_init(elev=17,azim=-68); axA.set_box_aspect((1,1,1.02),zoom=1.30); axA.set_axis_off()
axA.text2D(0.0,1.03,r'(B) the $dS_4$ background',transform=axA.transAxes,fontsize=TIT,va='bottom',fontweight='bold')
axA.legend(loc='lower left',fontsize=AN-4,frameon=True,framealpha=.88,
           handlelength=1.7,borderpad=.35,labelspacing=.28,bbox_to_anchor=(-0.04,0.02))

# ============ (D) the observer (tau,chi) chart ============
axB=fig.add_subplot(gs[1,1]); X0,X1=-1.15,1.15
def rsig(tt): s=np.sinh(1.5*tt); return A*np.sign(s)*np.abs(s)**(2/3)
def rprime(tt,h=1e-6): return (rsig(tt+h)-rsig(tt-h))/(2*h)
for d in np.linspace(-1.8,2.0,13): axB.plot([X0,X1],[d-X0,d-X1],color=GREY,lw=1.0,alpha=0.6)      # grey = S^3 (const r)
for c in np.linspace(-0.9,0.9,9):                                                                  # c=0 included: no mask, no redraw
    axB.plot([c,c],[-c,X1],color=BLUE,lw=1.3,alpha=0.8)                                          # vertical: blue above r=0 diagonal
    axB.plot([c,c],[X0,-c],color=RED, lw=1.3,alpha=0.8)                                          # vertical: red below
    axB.plot([-c,X1],[c,c],color=RED, lw=1.3,alpha=0.8)                                          # horizontal: red right of r=0 diagonal
    axB.plot([X0,-c],[c,c],color=BLUE,lw=1.3,alpha=0.8)                                          # horizontal: blue left
def photon(chi_seam,Ts=4.0):
    rhs=lambda ttil,y:[1.0/(1.0+rprime(ttil))]
    sP=solve_ivp(rhs,[0,Ts],[chi_seam],max_step=0.01,rtol=1e-8); sM=solve_ivp(rhs,[0,-Ts],[chi_seam],max_step=0.01,rtol=1e-8)
    ttil=np.concatenate([sM.t[::-1],sP.t]); chi=np.concatenate([sM.y[0][::-1],sP.y[0]]); tau=ttil-chi
    m=(chi>=X0)&(chi<=X1)&(tau>=X0)&(tau<=X1); return chi[m],tau[m]
for cs in np.linspace(-1.05,1.05,13):
    ch,ta=photon(cs)
    if len(ch)>2: axB.plot(ch,ta,color=BLACK,lw=1.3,alpha=0.8)                                    # black = photons crossing the seam
axB.plot([0,0],[0,X1],color=BLUE,lw=3.6,zorder=6); axB.plot([0,0],[X0,0],color=RED,lw=3.6,zorder=6)  # thick A axis: blue top / red bottom
# --- seam diagonals, BLACK dashed to match the black seam dots of (B)  (added r2099) ---
_Ab=2**(1/3)/np.sqrt(3)
_tSm=-(2/3)*np.arccosh(abs((-2/np.sqrt(3))/_Ab)**1.5)
_tSp=(2/3)*np.arcsinh(((1/np.sqrt(3))/_Ab)**1.5)
def _seamdiag(tt,lab,ls):
    axB.plot([X0,X1],[tt-X0,tt-X1],color=BLACK,lw=1.5,ls=ls,alpha=.9,zorder=7)
    _lo=max(X0,tt-X1); _hi=min(X1,tt-X0); _tm=0.5*(_lo+_hi); _cm=tt-_tm
    axB.text(_cm,_tm,lab,fontsize=AN-2,color=BLACK,ha='center',va='center',rotation=-45,
             rotation_mode='anchor',zorder=9,bbox=dict(fc='white',ec='none',alpha=.8,pad=.5))
_seamdiag(_tSm,'back seam',(0,(5,2)))
_seamdiag(_tSp,'front seam',(0,(5,2)))
_seamdiag(0.0,'turnaround + lift + $r=0$',(0,(1,0)))
#axB.text(-1.08,1.05,'blue $A$ (const $\\chi$)',color=BLUE,fontsize=AN,va='top')
#axB.text(-1.08,-0.88,'red $B$ (const $\\tau$)',color=RED,fontsize=AN)
#axB.text(0.30,0.60,'photons (black,\ncross the seam)',color='k',fontsize=AN-1,ha='center')
axB.set_xlim(X0,X1); axB.set_ylim(X0,X1); axB.set_aspect('equal'); axB.set_xlabel(r'$\chi$',fontsize=AX,labelpad=1); axB.set_ylabel(r'$\tau$',fontsize=AX,labelpad=-6); axB.tick_params(labelsize=TK)
for s in ['top','right']: axB.spines[s].set_visible(False)
axB.text(0.0,1.03,r'(D) the observer $(\tau,\chi)$ chart',transform=axB.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (C) the layered handoff at the seam -- the bead in the REAL-REAL (tau~, r) plane ============
# Both axes are real, so we plot what the bead actually is here. Walking it:
#   expansion r>0 : Im tau~=0        -> r = +A sinh^{2/3}(3 tau~/2a),  tau~: 0 -> +inf
#   the LAP   -A<r<0: Re tau~=0      -> the lap has NOWHERE TO GO on a real tau~ axis: it plots as a
#                                       VERTICAL SEGMENT at tau~=0, r: 0 -> -A. (This is the lap FLATTENED;
#                                       panel F unfurls it into Im tau~.)
#   collapse  r<-A : Im tau~=-pi a/3 -> r = -A cosh^{2/3}(3 Re tau~/2a), Re tau~: 0 -> -inf   [a COSH]
# Continuous: collapse ends at the turnaround r=-A, the lap segment carries r=-A -> 0, expansion leaves r=0.
# (The old -A|sinh|^{2/3} form was the MIRROR of the expansion leg: no lap segment, collapse starting at
#  r=0 rather than the turnaround. See body l.743, which states this continuation.)
axF=fig.add_subplot(gs[1,0])
_tL=np.linspace(-2.3,0,600); _tR=np.linspace(0,2.3,600)
_cL=A*np.cosh(1.5*_tL)**(2/3)          # |r| on the collapse leg (cosh)
_sR=A*np.sinh(1.5*_tR)**(2/3)          # |r| on the expansion leg (sinh)
axF.axvspan(-2.5,0,color='0.94'); axF.axvspan(0,2.5,color='0.98')
axF.fill_between(_tL,-_cL,_cL,color=GREY,alpha=0.10); axF.fill_between(_tR,-_sR,_sR,color=GREY,alpha=0.10)
# bead 1 (the cosmological bundle): antimatter BH (red) -> lap -> matter universe (blue)
axF.plot(_tL,-_cL,color=RED,lw=3.2)                       # collapse, r<0
axF.plot([0,0],[-A,0],color=RED,lw=3.2)                   # THE LAP, flattened to tau~=0
axF.plot(_tR, _sR,color=BLUE,lw=3.2)                      # matter universe, r>0
# bead 2 (the R-conjugate reading): matter BH (blue) -> lap -> antimatter universe (red)
axF.plot(_tL, _cL,color=BLUE,lw=3.2)
axF.plot([0,0],[0,A],color=BLUE,lw=3.2)
axF.plot(_tR,-_sR,color=RED,lw=3.2)
axF.axvline(0,color='0.85',lw=0.8,ls=(0,(3,3)))
# THE LAP = the span between the two Nariai roots (-2a/sqrt3 .. +a/sqrt3) -- exactly what (E) draws.
# It is THREE pieces here: the cosh leg (root -> turnaround), the LIFT (turnaround -> r=0, vertical,
# where Re tau~=0 and all the motion is in Im tau~), and the sinh leg (r=0 -> root). r=0 sits PARTWAY
# THROUGH the lap -- it is the branch point, not the seam. The seams are the lap's two ENDS.
_rSm,_rSp = -2/np.sqrt(3), 1/np.sqrt(3)                       # the two Nariai roots (seams)
_tSm,_tSp = -(2/3)*np.arccosh(abs(_rSm/A)**1.5), (2/3)*np.arcsinh((_rSp/A)**1.5)
axF.plot([_tSm,_tSp],[_rSm,_rSp],ls='none')                    # (span reference)
for _x,_y,_lb,_ha,_off in [(_tSm,_rSm,r'seam  $-2\alpha/\sqrt{3}$','right',(-0.10,-0.32)),
                           (0.0,-A,r'turnaround  $-(2M\alpha^2)^{1/3}$','left',(0.12,-0.40)),
                           (0.0,0.0,r'$r{=}0$','left',(0.12,0.16)),
                           (_tSp,_rSp,r'seam  $+\alpha/\sqrt{3}$','left',(0.10,0.20))]:
    axF.plot(_x,_y,'o',color='k',ms=6,zorder=8)
    axF.annotate(_lb,xy=(_x,_y),xytext=(_x+_off[0],_y+_off[1]),fontsize=AN-3,ha=_ha,color='0.15')
axF.annotate('the lift\n($\\mathrm{Re}\\,\\tilde\\tau{=}0$; unfurled in (F))',xy=(0,-A/2),xytext=(0.75,-1.75),
             fontsize=AN-3,color='0.3',arrowprops=dict(arrowstyle='->',color='0.45',lw=0.7))
axF.annotate('',xy=(_tSm,2.35),xytext=(_tSp,2.35),arrowprops=dict(arrowstyle='<->',color='0.45',lw=0.9))
axF.text((_tSm+_tSp)/2,2.45,'the lap',fontsize=AN-2,color='0.3',ha='center')
axF.text(-1.15,-2.35,'INWARD (collapse)\nleaf local rate\n$-$ radiation gravitates',color='0.25',fontsize=AN,ha='center',va='top')
axF.text(1.2,-2.35,'OUTWARD (expansion)\nfoliation stacking rate\n(geometric: $\\Lambda$ + offset)',color='0.25',fontsize=AN,ha='center',va='top')
axF.text(-0.4,1.32,'deposits: $\\rho_r/\\rho_m\\approx2$ (acoustic scale)\n$\\eta$ (composition)',fontsize=AN,ha='left',bbox=dict(boxstyle='round,pad=0.35',fc='#f4f4f4',ec='0.7',lw=0.7))
axF.annotate('cooling leg = BBN',xy=(0.55,0.55),xytext=(0.85,-0.15),fontsize=AN,color='0.3',ha='left',arrowprops=dict(arrowstyle='->',color='0.4',lw=0.7))
axF.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$',fontsize=AX); axF.set_ylabel(r'$r/\alpha$',fontsize=AX)
axF.set_xlim(-2.3,2.3); axF.set_ylim(-3.5,2.7); axF.tick_params(labelsize=TK)
for sp in ['top','right']: axF.spines[sp].set_visible(False)
axF.text(0.0,1.03,r'(C) the layered handoff at the seam',transform=axF.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (F) the cosmological bundle, strung out and unfurled ============
# ONE privileged worldline (the bold bead of A/B): the antimatter black hole collapsing (RED, r<0)
# through r=0 and continuing as our matter universe (BLUE, r>0). Plotted in (Re tau~, Im tau~, r):
# real r, complex tau~ -- the three axes the cosmological bundle needs. The LAP is UNFURLED here
# (the vertical lift at Re tau~=0) instead of flattened onto one X0.
# Branch: arg r = +pi (NEGATIVE-imaginary), sinh(w) = -i|r/A|^{3/2}, w = 3 tau~/2a.
#   collapse run : u=|sinh|>1 -> Im tau~=-pi/3 fixed, Re tau~=-(2/3)arccosh(u)
#   the LAP lift : u<=1       -> Re tau~=0,           Im tau~=-(2/3)arcsin(u): -pi/3 -> 0
#   matter univ. : r>0        -> Im tau~=0,           Re tau~=+(2/3)arcsinh((r/A)^{3/2})
# The collapse side (run+lift) and the cosmology side (one real curve) are STRUCTURALLY DIFFERENT.
# Seam points (the boing roots of E) land exactly: r=-2a/sqrt3 at |sinh|=2, r=+a/sqrt3 at |sinh|=1/sqrt2,
# whose Re tau~ are -(2/3)arccosh(2) and +(2/3)arcsinh(1/sqrt2) -- EXACTLY 2:1, since
# arccosh(2)=2 arcsinh(1/sqrt2). The 120/240 gearing as a LENGTH RATIO. (receipt: cosmo_bundle.py)
## [r1092] F' -- the FLATTENED cosmological bundle: r against s = arc length along the tau~ path
## (collapse Re tau~<=0 | the lift Im tau~ in [-pi/3,0] | expansion Re tau~>=0), one 2-D curve, both
## bends legible, nothing hidden behind a viewing angle. Replaces the 3-D unfurled F. (receipt: F_flat.py)
axC=fig.add_subplot(gs[2,1])
_Pl=np.pi/3
def _rF(s):
    s=np.asarray(s,float); out=np.empty_like(s)
    m1,m2,m3=s<=0,(s>0)&(s<=_Pl),s>_Pl
    out[m1]=-A*np.cosh(1.5*s[m1])**(2/3)
    out[m2]=-A*np.sin(1.5*(_Pl-s[m2]))**(2/3)
    out[m3]= A*np.sinh(1.5*(s[m3]-_Pl))**(2/3)
    return out
axC.axvspan(0,_Pl,color='0.95',zorder=0)
for _seg,_c in [((-2.0,0),RED),((0,_Pl),RED),((_Pl,2.6),BLUE)]:
    _ss=np.linspace(*_seg,600); axC.plot(_ss,_rF(_ss),color=_c,lw=3.4,zorder=3)
axC.axhline(0,color='0.85',lw=0.8,zorder=1)
axC.text(_Pl/2,2.42,'the lift',fontsize=AN-3,color='0.4',ha='center')
_sSm=-(2/3)*np.arccosh(((2/np.sqrt(3))/A)**1.5)              # back seam, on the collapse leg
_sSp= _Pl+(2/3)*np.arcsinh(((1/np.sqrt(3))/A)**1.5)          # front seam, on the expansion leg
_pts=[(_sSm,-2/np.sqrt(3),'o',r'seam $(r{=}{-}2\alpha/\sqrt{3})$',None),
      (0.0,-A,'s',r'turnaround; $dr/ds{=}0$',r'(horiz.\ tangent)'),
      (_Pl,0.0,'o',r'$r{=}0$; $dr/ds{\to}\infty$',r'(vert.\ tangent)'),
      (_sSp,1/np.sqrt(3),'o',r'seam $(r{=}{+}\alpha/\sqrt{3})$',None)]
for _x,_y,_mk,_l1,_l2 in _pts:
    axC.plot(_x,_y,_mk,color='0.12',ms=6,zorder=6)
    axC.annotate(_l1,xy=(_x,_y),xytext=(_x+0.08,_y-0.06),fontsize=AN-4,ha='left',va='top',color='0.1',zorder=6)
    if _l2: axC.annotate(_l2,xy=(_x,_y),xytext=(_x+0.08,_y-0.24),fontsize=AN-4,ha='left',va='top',color='0.1',zorder=6)
axC.text(-1.28,-0.55,'antimatter\nblack hole',color=RED,fontsize=AN-2,ha='center')
axC.text(1.78,1.78,'matter\nuniverse',color=BLUE,fontsize=AN-2,ha='center')
axC.set_xlabel(r'$s/\alpha$ (path length in $\tilde\tau$)',fontsize=AX); axC.set_ylabel(r'$r/\alpha$',fontsize=AX)
axC.set_xlim(-2.0,2.6); axC.set_ylim(-2.6,2.6)
axC.set_xticks([-2,-1,0,_Pl,2]); axC.set_xticklabels(['$-2$','$-1$','$0$',r'$\pi/3$','$2$'])
axC.tick_params(labelsize=TK)
for sp in ['top','right']: axC.spines[sp].set_visible(False)
axC.text(0.0,1.03,r'(F) the cosmological bundle, flattened',transform=axC.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

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
# the comoving turnaround (1-f=0) is NOT a turning point of this slicing curve (f=0): square, not circle.
_yT=-np.cos(2*np.pi*(-A)/np.sqrt(3)); axD.plot(-A,_yT,'s',color='0.2',ms=7)
axD.annotate('turnaround',xy=(-A,_yT),xytext=(-A+0.02,_yT+0.30),fontsize=AN-1,ha='center')
axD.axhline(0,color='0.6',lw=0.9)
axD.set_xlabel(r'$r/\alpha$',fontsize=AX-1); axD.set_ylabel(r'$X_1/\alpha$',fontsize=AX)
axD.set_xlim(-2.0,1.4); axD.set_ylim(-2.2,2.4); axD.tick_params(labelsize=TK)
for sp in ['top','right']: axD.spines[sp].set_visible(False)
axD.text(0.0,1.03,r'(E) the boing in $X_1$',transform=axD.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

# ============ (A) the Nariai slicing curve, from overhead (N-pole projection) -- both bundles ============
axE=fig.add_subplot(gs[0,0])
_hg=np.array([0,-2.0]); _T=np.array([np.sqrt(3)/2,-0.5]); _Tp=np.array([-np.sqrt(3)/2,-0.5])
_dR=np.array([0.5,np.sqrt(3)/2]); _dL=np.array([-0.5,np.sqrt(3)/2]); _se=np.linspace(0,1.9,2)
def _arc(a0,a1,col): t=np.deg2rad(np.linspace(a0,a1,120)); axE.plot(np.cos(t),np.sin(t),color=col,lw=3.6)
_arc(330,450,BLUE)     # top-right third: blue
_arc(90,210,RED)       # top-left third: red
_arc(210,330,PURPLE)   # bottom (hinge) third: purple
axE.plot([_hg[0],_T[0]],[_hg[1],_T[1]],color=BLUE,lw=3.2)                    # blue in, right
axE.plot(_T[0]+_se*_dR[0],_T[1]+_se*_dR[1],color=RED,lw=3.2)                 # red out, right
axE.plot([_hg[0],_Tp[0]],[_hg[1],_Tp[1]],color=RED,lw=3.2)                   # red in, left
axE.plot(_Tp[0]+_se*_dL[0],_Tp[1]+_se*_dL[1],color=BLUE,lw=3.2)              # blue out, left
axE.plot(0,1,'o',color='k',ms=4); axE.annotate(r'$r{=}0$',(0,1),(0.14,1.05),fontsize=AN)
axE.plot(*_hg,'o',color='k',ms=4); axE.annotate('hinge',_hg,(_hg[0]+0.14,_hg[1]-0.02),fontsize=AN)
axE.plot(*_T,'o',color='k',ms=4);  axE.annotate('equatorial\nseam',_T,(_T[0]+0.12,_T[1]-0.10),fontsize=AN-2)
axE.plot(*_Tp,'o',color='k',ms=4); axE.annotate('equatorial\nseam',_Tp,(_Tp[0]-0.72,_Tp[1]-0.10),fontsize=AN-2)
axE.set_aspect('equal'); axE.set_xlim(-2.2,2.2); axE.set_ylim(-2.3,2.0); axE.set_axis_off()
axE.text(0.0,1.03,r'(A) the Nariai slicing curve ($dS_5$ substrate)',transform=axE.transAxes,fontsize=TIT,va='bottom',fontweight='bold')

plt.savefig('dS-SdS-synthesis.pdf',bbox_inches='tight'); plt.savefig('dS-SdS-synthesis.png',dpi=150,bbox_inches='tight')
print('dS-SdS-synthesis.png')
