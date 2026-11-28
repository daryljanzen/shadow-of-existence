#!/usr/bin/env python3
"""
make_p3_figs.py  --  reproducible generator for P3's fig2,3,4,5,7 (fig6 has its own script).
Faithful renderings from the paper's OWN math (captions of SdS-slicing-curve_v2.tex), kept IN the
bundle so they cannot drop out of the lineage again (they did: r934 built them one-off, no script
survived; r1105 restored PDFs from an old tar; they vanished again). Built r1334 (Arthur), matching
the r934/r548 spec verified against the captions. Offered as faithful renderings for Daryl's
review/replacement if he holds different originals.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','mathtext.fontset':'cm','font.size':10,'savefig.bbox':'tight'})


def _save(stem):
    """PDF for the typeset paper, PNG for the HTML edition -- written from the
    same figure in the same run so the two cannot disagree.  r4601: the HTML
    chapter could not show a PDF figure and was linking six of eleven out."""
    plt.savefig(f'figs/{stem}.pdf')
    plt.savefig(f'figs/{stem}.png', dpi=180)

import os; os.makedirs('figs', exist_ok=True)
al=1.0; r3=np.sqrt(3)

# ---------- fig2_throat_circle : (a) 3D one-sheeted hyperboloid + throat, (b) equator-on ----------
fig=plt.figure(figsize=(9,4.2))
axa=fig.add_subplot(1,2,1,projection='3d')
u=np.linspace(-1.4,1.4,40); th=np.linspace(0,2*np.pi,60); U,T=np.meshgrid(u,th)
# -X0^2+X1^2+X2^2=al^2 : X0=al*sinh u, radius=al*cosh u
X0=al*np.sinh(U); R=al*np.cosh(U); X1=R*np.cos(T); X2=R*np.sin(T)
axa.plot_surface(X1,X2,X0,alpha=0.28,color='steelblue',lw=0,rstride=2,cstride=2)
tc=np.linspace(0,2*np.pi,120); axa.plot(al*np.cos(tc),al*np.sin(tc),0*tc,color='firebrick',lw=2)  # throat
for s in (-1,1):  # asymptotic null cone (dashed)
    axa.plot([0,2*s],[0,0],[0,2*s*al],'k--',lw=.7); axa.plot([0,0],[0,2*s],[0,2*s*al],'k--',lw=.7)
axa.set_title('(a) de Sitter one-sheeted hyperboloid',fontsize=9); axa.set_axis_off()
axa.text(0,0,-2.2,r'throat circle (radius $\alpha$)',color='firebrick',ha='center',fontsize=8)
# (b) equatorial section viewed from the north pole: the three parallel planes through the three hinges.
# Each plane's perpendicular offset d_k from the axis gives the root d_k/sqrt3 of the horizon cubic.
axb=fig.add_subplot(1,2,2); axb.set_aspect('equal'); axb.axis('off')
axb.plot(al*np.cos(tc),al*np.sin(tc),color='firebrick',lw=2)
wv=np.radians(20.0)
tdir=np.array([-np.cos(wv),np.sin(wv)]); nrm=np.array([np.sin(wv),np.cos(wv)])
cols=['navy','teal','darkorange']
for k in range(3):
    ph=2*np.pi*k/3; H=2*al*np.array([np.cos(ph),np.sin(ph)])
    L=np.array([H-4.2*tdir,H+4.2*tdir])
    axb.plot(L[:,0],L[:,1],color=cols[k],lw=1.6 if k==0 else 1.0)
    dk=nrm@H; F=dk*nrm
    axb.plot([0,F[0]],[0,F[1]],ls='--',color=cols[k],lw=.8); axb.plot(*F,'o',color=cols[k],ms=3)
    axb.plot(*H,'o',color='k',ms=5)
    off=np.array([0.14,0.0]) if k==0 else (np.array([-0.38,0.08]) if k==1 else np.array([-0.38,-0.2]))
    axb.text(*(H+off),f'$h_{k}$',fontsize=8)
    lab=F+0.2*nrm*np.sign(dk if abs(dk)>1e-9 else 1)+0.24*tdir
    axb.text(*lab,f'${dk/r3:+.2f}$',color=cols[k],fontsize=7,ha='center',va='center')
axb.plot(0,0,'k+',ms=6)
axb.plot(-al,0,'ks',ms=5); axb.text(-al-0.07,-0.2,'$r=0$',ha='right',fontsize=8)
axb.text(-2.35,-2.45,r'roots $=$ offsets$/\sqrt{3}$, at $w=20^{\circ}$',ha='left',fontsize=8)
axb.set_title('(b) equatorial section: three parallel planes',fontsize=9)
axb.set_xlim(-2.4,2.4); axb.set_ylim(-2.6,2.3)
_save('fig2_throat_circle'); plt.close()

# ---------- fig3_cubic_involution : (a) 2M=r0-r0^3, (b) sigma involution ----------
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,3.8))
r0=np.linspace(-1.2,1.2,400); twoM=r0-r0**3
a1.plot(r0,twoM,color='steelblue',lw=1.8)
for rc in (1/r3,-1/r3): a1.plot(rc,rc-rc**3,'o',color='firebrick',ms=5)
a1.axhline(0.3,ls=':',color='0.6',lw=.8)  # a mass level meeting 3 roots
roots=np.sort(np.roots([-1,0,1,-0.3]).real)
a1.plot(roots,[0.3]*3,'kv',ms=5)
a1.text(1/r3,2/(3*r3)+0.03,'Nariai $+1/\\sqrt{3}$',fontsize=7.5,ha='center',color='firebrick')
a1.set_xlabel('$r_0$'); a1.set_ylabel('$2M$'); a1.set_title('(a) horizon cubic $2M=r_0-r_0^3$',fontsize=9); a1.grid(alpha=.25)
x=np.linspace(0,1,300); sig=0.5*(-x+np.sqrt(4-3*x**2))
a2.plot(x,sig,color='steelblue',lw=1.8); a2.plot([0,1],[0,1],'k:',lw=.8)
a2.plot(1/r3,1/r3,'o',color='firebrick',ms=6); a2.text(1/r3+0.02,1/r3-0.08,'fixed $1/\\sqrt{3}$',fontsize=8,color='firebrick')
a2.plot([0,1],[1,0],'s',color='navy',ms=5); a2.text(0.02,0.94,'$\\sigma(0)=1$',fontsize=8); a2.text(0.7,0.03,'$\\sigma(1)=0$',fontsize=8)
a2.set_xlabel('$r_0$'); a2.set_ylabel('$\\sigma(r_0)$'); a2.set_title('(b) root-exchange involution $\\sigma$',fontsize=9); a2.grid(alpha=.25)
_save('fig3_cubic_involution'); plt.close()

# ---------- fig5_triple_angle : (a) 2M=(2/3sqrt3) sin 3w, (b) r0=(2/sqrt3) sin w ----------
fig,(a1,a2)=plt.subplots(1,2,figsize=(9,3.8))
w=np.linspace(0,np.pi/3,400)
a1.plot(w,(2/(3*r3))*np.sin(3*w),color='steelblue',lw=1.8)
a1.plot(np.pi/6,2/(3*r3),'o',color='firebrick',ms=5); a1.text(np.pi/6,2/(3*r3)+0.008,'Nariai crest $w=\\pi/6$',ha='center',fontsize=7.5,color='firebrick')
a1.set_xlabel('sky angle $w$'); a1.set_ylabel('$2M$'); a1.set_title('(a) $2M=\\frac{2}{3\\sqrt{3}}\\sin 3w$',fontsize=9); a1.grid(alpha=.25)
a1.set_xticks([0,np.pi/6,np.pi/3]); a1.set_xticklabels(['0','$\\pi/6$','$\\pi/3$'])
a2.plot(w,(2/r3)*np.sin(w),color='steelblue',lw=1.8)
a2.plot(np.pi/3,1.0,'o',color='navy',ms=5); a2.text(np.pi/3,1.02,'throat-tangent $w=\\pi/3$',ha='right',fontsize=7.5,color='navy')
a2.set_xlabel('sky angle $w$'); a2.set_ylabel('$r_0$'); a2.set_title('(b) $r_0=\\frac{2}{\\sqrt{3}}\\sin w$',fontsize=9); a2.grid(alpha=.25)
a2.set_xticks([0,np.pi/6,np.pi/3]); a2.set_xticklabels(['0','$\\pi/6$','$\\pi/3$'])
_save('fig5_triple_angle'); plt.close()

# ---------- fig4_seam : Riemannian r=rho sin th  ->  Lorentzian r=rho cosh psi, C^1 at throat ----
fig,ax=plt.subplots(figsize=(6.4,4.0)); rho=1.0
th=np.linspace(0,np.pi/2,200); psi=np.linspace(0,1.1,200)
sR=rho*np.sin(th)     # spherical piece, param by theta in [0,pi/2] -> r: 0..rho
sL=rho*np.cosh(psi)   # dual piece, param by psi -> r: rho..
# lay them on one axis: arc parameter s (theta then psi past the throat)
ax.plot(th, sR, color='seagreen', lw=2, label=r'Riemannian $r=\varrho\sin\theta$  (+,+)')
ax.plot(np.pi/2+psi, sL, color='indianred', lw=2, label=r'Lorentzian $r=\varrho\cosh\psi$  ($-$,+)')
ax.axhline(rho, ls=':', color='0.6', lw=.8); ax.axvline(np.pi/2, ls=':', color='0.6', lw=.8)
ax.plot(np.pi/2, rho, 'ko', ms=6); ax.text(np.pi/2+0.03, rho-0.13, r'throat $r=\varrho$, $C^1$ join', fontsize=8)
ax.text(np.pi/2, ax.get_ylim()[1]*0.96, r'$\theta\mapsto\pi/2+i\psi$', ha='center', fontsize=9)
ax.set_xlabel(r'continuation parameter ($\theta$, then $\psi$)'); ax.set_ylabel('$r$')
ax.set_title('The equatorial seam: signature flips $(+,+)\\to(-,+)$', fontsize=9)
ax.set_xticks([0,np.pi/2]); ax.set_xticklabels(['0','$\\pi/2$']); ax.legend(fontsize=7.5,loc='upper left'); ax.grid(alpha=.25)
_save('fig4_seam'); plt.close()

# ---------- fig7_curvature : K_G = 1/al^2 - M/r^3 , sign change at r* = (M al^2)^{1/3} ----------
fig,ax=plt.subplots(figsize=(6.4,4.0)); M=0.12
r=np.linspace(0.12,2.2,400); KG=1/al**2 - M/r**3
rstar=(M*al**2)**(1/3)
ax.plot(r,KG,color='steelblue',lw=2); ax.axhline(0,color='0.5',lw=.8)
ax.plot(rstar,0,'o',color='firebrick',ms=6); ax.text(rstar+0.03,0.06,r'$r_\star=(M\alpha^2)^{1/3}$',fontsize=8,color='firebrick')
ax.fill_between(r,KG,0,where=(KG<0),color='indianred',alpha=.15)
ax.fill_between(r,KG,0,where=(KG>0),color='seagreen',alpha=.15)
ax.text(0.4,-2.0,'Schwarzschild-like\n$K_G<0$',fontsize=8,color='indianred')
ax.text(1.6,0.55,'de Sitter-like\n$K_G>0$',fontsize=8,color='seagreen')
ax.set_xlabel('$r$'); ax.set_ylabel('$K_G$'); ax.set_ylim(-4,1.2)
ax.set_title(r'Gaussian curvature $K_G=1/\alpha^2-M/r^3$',fontsize=9); ax.grid(alpha=.25)
_save('fig7_curvature'); plt.close()

print("built: figs/fig2_throat_circle.pdf fig3_cubic_involution.pdf fig4_seam.pdf fig5_triple_angle.pdf fig7_curvature.pdf")


# ---------- X1_vs_r_conjugate_wave : the Nariai lap, X1 against the lap's arc-length radius parameter ----------
# One turn of the throat spans sqrt3*alpha in r, from the merged pair +1/sqrt3 to the lone root -2/sqrt3, so the
# azimuth from the hinge is theta = pi - k r with k = 2 pi / sqrt3; the ruling legs leave tangentially (C^1).
k=2*np.pi/r3
rl=np.linspace(-2/r3,1/r3,600); X1l=al*np.cos(np.pi-k*rl)
slope=k*np.sin(np.pi-k*(1/r3))
fig,ax=plt.subplots(figsize=(7,4.2))
rr=np.linspace(1/r3,1.05,50); ax.plot(rr,0.5+slope*(rr-1/r3),color='0.55',lw=2,label='real ruling leg (straight)')
rr=np.linspace(-1.35,-2/r3,50); ax.plot(rr,0.5+slope*(rr+2/r3),color='0.55',lw=2)
ax.plot(rl,X1l,color='firebrick',lw=2.4,label='conjugate lap')
for x,y,t in ((1/r3,0.5,r'merged pair $+\alpha/\sqrt{3}$ (enter)'),(0,-1,r'$r=0$, back of the throat ($X_1=-\alpha$)'),(-2/r3,0.5,r'lone root $-2\alpha/\sqrt{3}$ (lap closes)')):
    ax.plot(x,y,'o',color='firebrick',ms=5); ax.text(x+0.03,y+(0.1 if y>0 else -0.14),t,fontsize=8)
ax.axhline(0,color='k',lw=.5)
ax.set_xlabel(r'$r$ (the lap parameter: arc length along the closed curve, one turn $=\sqrt{3}\,\alpha$)')
ax.set_ylabel(r'$X_1$ (embedding coordinate)')
ax.set_title('The Nariai lap: straight on the ruling legs, a cosine around the throat',fontsize=10)
ax.legend(loc='lower left',fontsize=8)
plt.savefig('X1_vs_r_conjugate_wave.png',dpi=150); plt.close()
