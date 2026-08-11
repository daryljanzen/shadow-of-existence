"""
A1.4 figure: the Hubble tension resolved across the BAO distance ladder.
Left  -- the BAO Hubble diagram: DR12 D_M/r_d and D_H/r_d with CR (Om fixed, any H0) tracking the
         data at the LOCAL H0=73, LCDM(67.4) also on it, LCDM(73) missing.
Right -- chi^2(H0) from BAO: LCDM is a steep parabola pinned at ~67 (excludes 73); CR is FLAT in H0
         (the radiation-free rate makes the BAO ratios H0-independent), so it admits the SH0ES H0=73.
That contrast IS the tension and its structural resolution.
"""
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
trapz=np.trapezoid; c=299792.458
wb,wg=0.02237,2.47e-5; R0=3*wb/(4*wg)
def cs(z): return c/np.sqrt(3*(1+R0/(1+z)))
zrec,z_drag=1090.0,1059.94
# CR: Om the invariant (H0-independent), radiation-free
def Ecr(z,Om): return np.sqrt(Om*(1+z)**3+(1-Om))
def DMcr(z,H0,Om,n=4000): zz=np.linspace(0,z,n); return trapz(c/(H0*Ecr(zz,Om)),zz)
def DHcr(z,H0,Om): return c/(H0*Ecr(z,Om))
def rdcr(H0,Om,zo,n=120000):
    u=np.linspace(np.log(1+z_drag),np.log(1+zo),n); z=np.exp(u)-1
    return trapz(cs(z)/(H0*Ecr(z,Om))*(1+z),u)
def theta(H0,Om,zo):
    u=np.linspace(np.log(1+zrec),np.log(1+zo),120000); z=np.exp(u)-1
    rs=trapz(cs(z)/(H0*Ecr(z,Om))*(1+z),u); return rs/DMcr(zrec,H0,Om)
Om=0.31; THETA=0.0104085
zo=brentq(lambda z: theta(70.0,Om,z)-THETA,1200,5e4)
# LCDM: wm fixed (radiation-era physical density), Om=wm/h^2, radiation in rate
wm,wr=0.1430,4.15e-5
def El(z,h): O=wm/h**2; Or=wr/h**2; return np.sqrt(O*(1+z)**3+Or*(1+z)**4+1-O-Or)
def DMl(z,H0,n=4000): zz=np.linspace(0,z,n); return trapz(c/(H0*El(zz,H0/100)),zz)
def DHl(z,H0): return c/(H0*El(z,H0/100))
def rdl(H0,n=120000):
    u=np.linspace(np.log(1+z_drag),np.log(1+1e8),n); z=np.exp(u)-1
    return trapz(cs(z)/(H0*El(z,H0/100))*(1+z),u)
DR12=[(0.38,10.27,0.15,24.89,0.58),(0.51,13.38,0.18,22.43,0.48),(0.61,15.45,0.22,20.86,0.44)]
def chi2_cr(H0): rd=rdcr(H0,Om,zo); return sum(((DMcr(z,H0,Om)/rd-dm)/sdm)**2+((DHcr(z,H0,Om)/rd-dh)/sdh)**2 for z,dm,sdm,dh,sdh in DR12)
def chi2_l(H0): rd=rdl(H0); return sum(((DMl(z,H0)/rd-dm)/sdm)**2+((DHl(z,H0)/rd-dh)/sdh)**2 for z,dm,sdm,dh,sdh in DR12)

fig,(axL,axR)=plt.subplots(1,2,figsize=(11,4.6))
# LEFT: BAO Hubble diagram
zg=np.linspace(0.2,0.75,60)
rd_cr=rdcr(73.0,Om,zo); rd67=rdl(67.4); rd73=rdl(73.0)
axL.plot(zg,[DMcr(z,73,Om)/rd_cr for z in zg],'-',color='#1f6feb',lw=2,label='CR  ($\\Omega_m$ fixed, any $H_0$ incl. 73)')
axL.plot(zg,[DMl(z,67.4)/rd67 for z in zg],'--',color='#2e8b57',lw=1.6,label='$\\Lambda$CDM  $H_0$=67.4')
axL.plot(zg,[DMl(z,73.0)/rd73 for z in zg],':',color='#d1495b',lw=1.8,label='$\\Lambda$CDM  $H_0$=73 (misses)')
axL.plot(zg,[DHcr(z,73,Om)/rd_cr for z in zg],'-',color='#1f6feb',lw=2)
axL.plot(zg,[DHl(z,67.4)/rd67 for z in zg],'--',color='#2e8b57',lw=1.6)
axL.plot(zg,[DHl(z,73.0)/rd73 for z in zg],':',color='#d1495b',lw=1.8)
for z,dm,sdm,dh,sdh in DR12:
    axL.errorbar(z,dm,yerr=sdm,fmt='o',color='0.2',ms=5,capsize=3,zorder=5)
    axL.errorbar(z,dh,yerr=sdh,fmt='s',color='0.2',ms=5,capsize=3,zorder=5)
axL.text(0.66,16.2,'$D_M/r_d$',fontsize=10); axL.text(0.66,20.2,'$D_H/r_d$',fontsize=10)
axL.set_xlabel('redshift $z$'); axL.set_ylabel('BAO distance / $r_d$')
axL.set_title('BAO Hubble diagram (SDSS DR12)',fontsize=10)
axL.legend(loc='center left',fontsize=8,framealpha=0.9); axL.grid(alpha=0.2)
# RIGHT: chi^2(H0)
H0s=np.linspace(63,77,50)
axR.plot(H0s,[chi2_l(h) for h in H0s],'-',color='#2e8b57',lw=2,label='$\\Lambda$CDM (radiation-pinned $r_d$)')
axR.plot(H0s,[chi2_cr(h) for h in H0s],'-',color='#1f6feb',lw=2,label='CR (radiation-free: $H_0$-independent)')
axR.axvspan(72,74,color='#d1495b',alpha=0.15,lw=0); axR.axvline(73,color='#d1495b',lw=1,ls='--')
axR.text(73.1,axR.get_ylim()[1]*0.0+42,'SH0ES\n$H_0$=73',fontsize=8,color='#b23',va='top')
axR.set_ylim(0,55); axR.set_xlabel('$H_0$  (km/s/Mpc)'); axR.set_ylabel('$\\chi^2$  (DR12 BAO, 6 pts)')
axR.set_title('BAO $\\chi^2$ vs $H_0$: $\\Lambda$CDM pinned to 67, CR admits 73',fontsize=10)
axR.legend(loc='upper center',fontsize=8,framealpha=0.9); axR.grid(alpha=0.2)
fig.suptitle('A1.4: the radiation-free rate resolves the Hubble tension across the BAO distance ladder',
             fontsize=11,y=1.00)
plt.tight_layout()
plt.savefig('fig_hubble_bao.pdf',bbox_inches='tight'); plt.savefig('fig_hubble_bao.png',dpi=140,bbox_inches='tight')
print(f"wrote fig_hubble_bao; z_onset={zo:.0f}, rd_cr(73)={rd_cr:.1f}, chi2 CR@73={chi2_cr(73):.2f} LCDM@73={chi2_l(73):.1f} LCDM@67.4={chi2_l(67.4):.2f}")
