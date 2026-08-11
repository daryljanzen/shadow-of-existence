"""Panel C - the horizon trichotomy that FORCES Nariai (alpha=1).
f(r)=1-2M/r-r^2 ; horizons at f=0 i.e. 2M=r-r^3, max at r=1/sqrt3 -> Nariai 2M_N=2/(3 sqrt3).
 M<M_N : two roots (BH + cosmo horizon)  -> reassigned null crosses TRANSVERSE  (x: not the limiting orientation)
 M=M_N : double root (r=1/sqrt3)          -> TANGENT / grazes its own horizon    (check: forced)
 M>M_N : no root                           -> NO horizon                          (x: a collapse forms one)
"""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
r=np.linspace(0.06,1.32,600)
def f(M): return 1-2*M/r-r**2
MN=1/(3*np.sqrt(3))
fig,ax=plt.subplots(figsize=(5.7,4.7))
ax.axhline(0,color='0.6',lw=0.8)
# undercritical
ax.plot(r,f(0.14),color='#2471a3',lw=2.2,label=r'$M<M_{\rm Nariai}$: two horizons (transverse)')
# Nariai
ax.plot(r,f(MN),color='#c0392b',lw=2.8,label=r'$M=M_{\rm Nariai}$: merged double root (tangent)')
# overcritical
ax.plot(r,f(0.26),color='#7f8c8d',lw=2.0,ls=(0,(5,3)),label=r'$M>M_{\rm Nariai}$: no horizon')
# mark undercritical roots
ru=[rr for rr in np.roots([-1,0,1,-2*0.14]) if abs(rr.imag)<1e-6 and rr.real>0]
for rr in sorted([x.real for x in ru]):
    ax.plot(rr,0,'o',color='#2471a3',ms=6)
# Nariai double root
rN=1/np.sqrt(3); ax.plot(rN,0,'o',color='#c0392b',ms=8,zorder=5)
ax.annotate('Nariai: two horizons merge\n$r=1/\\sqrt{3}$, grazed tangentially\n(finite curvature)',
            xy=(rN,0),xytext=(rN+0.14,0.30),fontsize=8.4,color='#c0392b',
            arrowprops=dict(arrowstyle='->',color='#c0392b',lw=0.8))
ax.annotate('BH horizon',xy=(sorted([x.real for x in ru])[0],0),xytext=(0.12,-0.42),fontsize=7.6,color='#2471a3',arrowprops=dict(arrowstyle='->',color='#2471a3',lw=0.7))
ax.annotate('cosmological\nhorizon',xy=(sorted([x.real for x in ru])[1],0),xytext=(1.02,-0.5),fontsize=7.6,color='#2471a3',arrowprops=dict(arrowstyle='->',color='#2471a3',lw=0.7))
ax.text(0.03,0.62,'collapse forms a horizon $\\Rightarrow$ rules out $M>M_{\\rm N}$;\nlimiting orientation is tangent $\\Rightarrow$ rules out transverse\n$\\therefore$ Nariai, forced $-$ fixed by $\\Lambda$ alone',fontsize=8.4,va='top',
        bbox=dict(boxstyle='round,pad=0.4',fc='#fdf6e3',ec='0.7',lw=0.6))
ax.set_xlabel(r'areal radius $r/\alpha$'); ax.set_ylabel(r'$f(r)=1-2M/r-r^2/\alpha^2$')
ax.set_ylim(-0.75,0.85); ax.set_xlim(0,1.32)
ax.text(-0.13,1.02,'C',transform=ax.transAxes,fontsize=15,fontweight='bold')
ax.text(0.0,1.02,r'Why Nariai: the horizon trichotomy',transform=ax.transAxes,fontsize=10.5,va='bottom')
ax.legend(loc='lower right',fontsize=7.6,frameon=False)
for s in ['top','right']: ax.spines[s].set_visible(False)
plt.tight_layout(); plt.savefig('panelC_trichotomy.png',dpi=160,bbox_inches='tight'); plt.savefig('panelC_trichotomy.pdf',bbox_inches='tight')
print('ok  M_N=%.4f  2M_N=%.4f (=2/(3sqrt3)=%.4f)'%(MN,2*MN,2/(3*np.sqrt(3))))
