import numpy as np
# FIX (r823): peak envelope = acoustic amplitude x baryon loading x SILK DAMPING only.
# NO BBKS/CDM matter transfer on the effective temperature (that was the r823a error).
rs=147.0; D_C=13864.0; R=0.6; cs=1/np.sqrt(3*(1+R)); ns=0.965
ell=np.arange(2,1800); k=ell/D_C
def pattern(a,label,kD=0.098):
    M=a*np.cos(k*rs)-R                 # effective temperature (monopole+Psi), baryon shift
    Dp=a*cs*np.sin(k*rs)               # Doppler dipole
    Dl=(M**2+Dp**2)*np.exp(-2*(k/kD)**2)*(k*D_C)**(ns-1)
    def pk(n):
        ip=np.argmin(abs(k-n*np.pi/rs));lo,hi=max(ip-16,0),min(ip+16,len(k));return Dl[lo:hi].max()
    p=[pk(n) for n in (1,2,3)]
    hi=p[0]==max(p)
    print(f"{label:34} a={a:4.2f}  P2/P1={p[1]/p[0]:.2f} P3/P1={p[2]/p[0]:.2f}  P1/P2={p[0]/p[1]:.2f}  P1 top? {hi}")
    return p[0]/p[1]
print(f"c_s={cs:.3f}, R={R}. Observed: P2/P1~0.46 P3/P1~0.46 P1/P2~2.2\n")
print("VALIDATE on LCDM (radiation driving -> a~3):")
for a in (2.6,3.0,3.4): pattern(a,"  LCDM driven")
print("\nCR: geometric stacking rate -> little driving -> a near adiabatic:")
a_ad=0.5+R
for a in (a_ad,1.5,2.0,2.6,3.0):
    lab="  CR undriven adiabatic" if abs(a-a_ad)<1e-9 else "  CR if handover -> a="
    pattern(a,lab)
print(f"\nadiabatic undriven a=1/2+R={a_ad:.2f}")
print("\nReading: observed P1/P2~2.2 needs a~3 (the DRIVEN value). CR's little driving")
print("sits at a~1.1 (adiabatic) -> P1/P2 far too large UNLESS the seam handover supplies a~3.")
