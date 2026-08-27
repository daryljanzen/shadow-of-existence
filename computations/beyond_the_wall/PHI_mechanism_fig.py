#!/usr/bin/env python3
"""The crossing-during-plasma mechanism, derived from Phi(eta,k): control modes cross the
horizon DURING the plasma (Phi decaying through the crossing -> driving impulse); CR modes are
switched on already deep sub-horizon at the common onset -> no crossing, no impulse."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

base='/tmp/claude-0/-home-user-shadow-of-existence/e37412c9-b73d-5dc0-927f-d18006c9d057/scratchpad/'
cr=np.load(base+'cr_phi.npz',allow_pickle=True)
lc=np.load(base+'lcdm_phi.npz',allow_pickle=True)

fig,axes=plt.subplots(1,2,figsize=(12,4.7),sharey=True)
for ax,z,tag,col in [(axes[0],lc,'CONTROL (LCDM)','#2166ac'),
                     (axes[1],cr,'CR arm (leaf rate)','#b2182b')]:
    eta=z['eta']; phi=z['phi']; dg=z['dg']; k=z['kpk']; q=z['qpk']
    er=float(z['eta_rec']); es=float(z['eta_s'])
    i=1                                            # the q~1.86 mid mode
    x=eta/er
    ax.plot(x, phi[i]/abs(phi[i][0]), color=col, lw=2.2, label=r'$\Phi(\eta)$ (potential)')
    ax.plot(x, dg[i]/4/abs(dg[i][0]/4)*0.5, color='#777', lw=1.4, label=r'$\Theta_0(\eta)$ (oscillation)')
    entry=(1.0/float(k[i]))/er
    if es < 1.0/float(k[i]) < er:
        ax.axvline(entry, color='#1a9850', ls='--', lw=1.6)
        ax.text(entry+0.02, 1.15, 'horizon crossing\nDURING plasma\n'+r'($\Phi$ decaying through it)',
                color='#1a9850', fontsize=9, va='top',
                bbox=dict(boxstyle='round', fc='white', ec='#1a9850', alpha=0.9))
    ax.axvline(es/er, color='k', ls=':', lw=1.4)
    ax.text(es/er+0.01, 0.72, 'onset', color='k', fontsize=9)
    if es/er>0.05:
        ax.axvspan(0, es/er, color='k', alpha=0.05)
        ax.text(es/er/2, 0.72, 'mode\nnot yet\nlaunched', ha='center', va='top', fontsize=8, color='#555')
        ax.text(entry, 0.9, f'entry 1/k at {entry:.2f}\n(before onset:\nno crossing)',
                ha='center', fontsize=8, color='#b2182b')
        ax.axvline(entry, color='#b2182b', ls='--', lw=1.2, alpha=0.6)
    ax.set_title(f'{tag}\n'+r'$q=k r_s/\pi=$'+f'{float(q[i]):.2f},  '+r'$k\eta_{\rm onset}=$'+f'{float(k[i])*es:.1f}', fontsize=10)
    ax.set_xlabel(r'$\eta/\eta_{\rm rec}$'); ax.set_xlim(0,1); ax.grid(alpha=0.25)
    ax.legend(loc='lower right', fontsize=8, framealpha=0.9)
axes[0].set_ylabel('normalised amplitude')
fig.suptitle('Driving is imparted at horizon crossing.  The control crosses during the plasma; '
             'the CR mode is launched already sub-horizon at the onset and never crosses.',
             fontsize=10.5, y=1.02)
fig.tight_layout()
fig.savefig(base+'mechanism.png', dpi=140, bbox_inches='tight')
print('wrote', base+'mechanism.png')
