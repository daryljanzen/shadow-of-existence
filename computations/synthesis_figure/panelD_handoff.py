"""Panel D - the layered handoff at the seam (P15-16 payload).
Areal radius |r(tau)| as a waist pinching at the seam; the fundamental congruence as worldlines.
 INWARD (tau<0, collapse): the LEAF's local rate governs -> radiation gravitates.
 OUTWARD (tau>0, expansion): the FOLIATION stacking rate governs -> radiation-free sinh^{2/3}.
 At the seam the handover deposits the two inherited data: rho_r/rho_m ~ 2 (acoustic scale) and eta (composition);
 infall heats ABOVE the deuterium bottleneck, the cooling expansion leg is the standard BBN run."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
s=np.linspace(-2.3,2.3,600); env=np.abs(np.sinh(s))**(2/3)
fig,ax=plt.subplots(figsize=(6.2,4.7))
# regime shading
ax.axvspan(-2.5,0,color='#2471a3',alpha=0.06); ax.axvspan(0,2.5,color='#c0392b',alpha=0.06)
# areal-radius waist envelope
ax.plot(s,env,color='k',lw=2.4); ax.plot(s,-env,color='k',lw=2.4)
ax.fill_between(s,-env,env,color='0.85',alpha=0.5)
# a few congruence worldlines (scaled copies) - the S^3 comoving points
for c in [0.35,0.6,0.85]:
    ax.plot(s,c*env,color='0.45',lw=0.7); ax.plot(s,-c*env,color='0.45',lw=0.7)
# seam
ax.axvline(0,color='0.4',lw=0.9,ls=(0,(3,3))); ax.plot(0,0,'o',color='k',ms=7,zorder=6)
ax.annotate('seam ($\\tilde\\tau=0$): Nariai\nfinite-curvature branch point',xy=(0,0),xytext=(-1.15,2.35),
            fontsize=8.2,ha='center',arrowprops=dict(arrowstyle='->',lw=0.7))
# regime labels
ax.text(-1.15,-2.7,'INWARD (collapse)\nleaf\'s local rate governs\n$-$ radiation gravitates',color='#1a5276',fontsize=8.4,ha='center',va='top')
ax.text(1.2,-2.7,'OUTWARD (expansion)\nfoliation stacking rate governs\n$-$ radiation-free  $\\sinh^{2/3}$',color='#922b21',fontsize=8.4,ha='center',va='top')
# deposited data at seam
ax.text(0.08,1.15,'handover deposits:\n$\\rho_r/\\rho_m\\approx2$  (sets acoustic scale)\n$\\eta$  (sets composition)',fontsize=8.0,ha='left',
        bbox=dict(boxstyle='round,pad=0.35',fc='#fdf6e3',ec='0.7',lw=0.6))
# BBN placement (cooling leg, just past seam)
ax.annotate('infall heats\nabove the D bottleneck',xy=(-0.55,0.55),xytext=(-2.15,0.9),fontsize=7.6,color='#1a5276',ha='left',arrowprops=dict(arrowstyle='->',color='#1a5276',lw=0.6))
ax.annotate('cooling leg = standard BBN\n(freeze-out; $\\eta$ sets $Y_p$, D/H)',xy=(0.55,0.55),xytext=(0.7,-0.05),fontsize=7.6,color='#922b21',ha='left',arrowprops=dict(arrowstyle='->',color='#922b21',lw=0.6))
ax.set_xlabel(r'cosmic proper time $\tilde\tau$'); ax.set_ylabel(r'areal radius $\pm r$ (the S$^3$ layers)')
ax.set_xlim(-2.3,2.3); ax.set_ylim(-3.4,2.7)
ax.text(-0.11,1.02,'D',transform=ax.transAxes,fontsize=15,fontweight='bold')
ax.text(0.0,1.02,r'The layered handoff at the seam',transform=ax.transAxes,fontsize=10.5,va='bottom')
for sp in ['top','right']: ax.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig('panelD_handoff.png',dpi=160,bbox_inches='tight'); plt.savefig('panelD_handoff.pdf',bbox_inches='tight')
print('ok')
