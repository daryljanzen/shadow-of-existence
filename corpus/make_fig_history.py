#!/usr/bin/env python3
"""make_fig_history.py -- P16 fig_history, faithful to its caption (built r1334, Arthur).
Local temperature of the infalling matter along its worldline: adiabatic contraction heats it above the
deuterium bottleneck T_D, peaks at turnaround, expansion cools it back through the window (deuterium
freeze-out, open circle); the observable expansion history begins later at the ~1.6 eV onset. Peak drawn
at its M-independent infall-scale lower bound (exact value open, downstream-irrelevant). Kept in bundle."""
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'serif','mathtext.fontset':'cm','font.size':10})
Tpeak=5e5; TD=7e4; Tonset=1.6            # eV : peak lower-bound, deuterium bottleneck, observable onset
# adiabatic bounce: scale factor a ~ cosh(tau) (min at turnaround), T ~ 1/a
tau=np.linspace(-4,14,1400); T=Tpeak/np.cosh(tau)
fig,ax=plt.subplots(figsize=(6.4,4.3))
ax.semilogy(tau,T,color='steelblue',lw=2)
# deuterium bottleneck (dashed) and the observable onset (dotted)
ax.axhline(TD,ls='--',color='0.45',lw=1); ax.text(13.6,TD*1.25,r'$T_{\mathrm{D}}\simeq0.07$ MeV',ha='right',fontsize=8,color='0.35')
ax.axhline(Tonset,ls=':',color='indianred',lw=1.2); ax.text(13.6,Tonset*1.3,r'$\sim1.6$ eV onset',ha='right',fontsize=8,color='indianred')
# peak (turnaround), M-independent lower bound
ax.plot(0,Tpeak,'o',color='firebrick',ms=6); ax.annotate('peak: $M$-independent\ninfall-scale lower bound',(0,Tpeak),(2.2,Tpeak*0.9),fontsize=8,color='firebrick',ha='left',va='top')
# deuterium freeze-out on the COOLING leg (T back down through T_D)
tf=np.arccosh(Tpeak/TD)                  # cooling-leg crossing of T_D
ax.plot(tf,TD,'o',mfc='white',mec='seagreen',mew=1.8,ms=8); ax.annotate('deuterium\nfreeze-out',(tf,TD),(tf+1.2,TD*3),fontsize=8,color='seagreen')
# annotate legs + completion
ax.annotate('',(-0.3,Tpeak*0.5),(-3.2,TD*0.6),arrowprops=dict(arrowstyle='->',color='0.5'))
ax.text(-3.5,TD*2.5,'contraction\n(adiabatic heating)',fontsize=8,color='0.4',ha='left')
to=np.arccosh(Tpeak/Tonset)
ax.text(to*0.62,Tonset*4,'expansion (cooling);\nBBN complete below onset',fontsize=8,color='0.4')
ax.set_xlabel('proper time along worldline  (turnaround at 0)'); ax.set_ylabel('local temperature  $T$  [eV]')
ax.set_ylim(1.0,2e6); ax.set_xlim(-4,14); ax.set_title('Temperature history of the infalling matter',fontsize=10)
ax.grid(alpha=.2,which='both')
plt.savefig('fig_history.pdf',bbox_inches='tight'); print("built fig_history.pdf")
