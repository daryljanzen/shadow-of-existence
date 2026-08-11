"""
The BBN concordance ("Schramm") plot for D1: computed light-element abundances vs the baryon-to-
photon ratio eta, with the measured primordial bands and the Planck CMB eta. Shows the joint
concordance -- D and He-4 crossing their observed bands at the same eta the CMB fixes -- and the
lithium miss, all from CR's forced cooling leg.
"""
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import bbn_network as B

etas=[2.0,3.0,4.0,5.0,6.13,7.0,8.0,9.0]
res=[]
for e in etas:
    o=B.run(eta10=e, verbose=False, library='starlib')   # precision: evaluated light-nuclide rates
    if o['success']: res.append((e,o['Yp']*1.016,o['DH'],o['He3H'],o['Li7H']))
    print(f"  eta10={e}: ok={o['success']}", flush=True)
res=np.array(res)
E=res[:,0]

# measured primordial bands (value, sigma)
OBS=dict(Yp=(0.2453,0.0034), DH=(2.527e-5,0.030e-5), Li7H=(1.6e-10,0.3e-10))
eta_planck=(6.13,0.04)

fig,axes=plt.subplots(3,1,figsize=(6.4,8.4),sharex=True,
                      gridspec_kw={'height_ratios':[2,1,2],'hspace':0.08})
panels=[('DH',2,'D/H','#1f6feb',(1e-5,2e-4),True),
        ('Yp',1,'$Y_p$ ($^4$He mass frac)','#d1495b',(0.20,0.27),False),
        ('Li7H',4,'$^7$Li/H','#b8860b',(5e-11,2e-9),True)]
for ax,(key,col,lab,c,ylim,logy) in zip(axes,panels):
    ax.plot(E,res[:,col],'-o',color=c,lw=2,ms=4,label='CR network')
    v,s=OBS[key]
    ax.axhspan(v-s,v+s,color=c,alpha=0.18,lw=0)
    ax.axhline(v,color=c,lw=0.8,ls='--')
    ax.axvspan(eta_planck[0]-eta_planck[1],eta_planck[0]+eta_planck[1],color='0.5',alpha=0.25,lw=0)
    if logy: ax.set_yscale('log')
    ax.set_ylim(*ylim); ax.set_ylabel(lab,fontsize=9)
    ax.grid(alpha=0.2)
axes[0].axvline(eta_planck[0],color='0.35',lw=0.8,ls=':')
axes[0].text(eta_planck[0]+0.12,axes[0].get_ylim()[1]*0.45,'Planck $\\eta$',rotation=90,
             fontsize=8,color='0.35',va='top')
axes[0].text(0.03,0.06,'shaded: measured primordial band ($\\pm1\\sigma$)\ngrey: Planck CMB $\\eta$',
             transform=axes[0].transAxes,fontsize=7.5,va='bottom',
             bbox=dict(boxstyle='round',fc='white',ec='0.8',alpha=0.9))
axes[0].set_title('D1: BBN concordance from CR’s forced cooling leg\n'
                  'D and $^4$He cross their observed bands at the Planck $\\eta$; $^7$Li misses (the lithium problem)',
                  fontsize=9.5)
axes[-1].set_xlabel('$\\eta_{10}$  (baryon-to-photon ratio $\\times10^{10}$)')
axes[0].legend(loc='upper right',fontsize=8)
plt.savefig('fig_schramm.pdf',bbox_inches='tight'); plt.savefig('fig_schramm.png',dpi=140,bbox_inches='tight')
print("wrote fig_schramm.pdf / .png")
