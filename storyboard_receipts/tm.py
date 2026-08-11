"""EXACT transmission across the Euclidean segment by TRANSFER MATRIX, composed in small steps,
integrated in the STABLE direction.  d^2 psi/d eta^2 = w^2 psi,  w = k c_s,  d eta = ds/a.
For constant w over a step the propagator is exact:  [[cosh, sinh/w],[w sinh, cosh]].
The decaying solution (turnaround -> branch point) is GROWING when built backwards, so we build
it backwards and invert: transmission = 1 / (backward growth)."""
import numpy as np
al=1.0; M=al/(3*np.sqrt(3)); A=(2*M*al**2)**(1./3); smax=np.pi*al/3.0
absr=lambda s: abs(-A*np.abs(np.sin(1.5*s/al))**(2./3))
R0=0.60/A; cs=lambda s: 1.0/np.sqrt(3.0*(1.0+R0*absr(s)))
DA=2.580
def transmission(l, N=400000, eps=1e-8):
    k=l/DA
    s=np.linspace(eps, smax, N)              # s: branch point -> turnaround
    a=np.abs(np.array([absr(x) for x in s])); w=k/np.sqrt(3.0*(1.0+R0*a))
    deta=np.diff(s)/(0.5*(a[1:]+a[:-1]))     # conformal-time steps
    wm=0.5*(w[1:]+w[:-1])
    # build the solution that GROWS from the branch point toward the turnaround (stable direction)
    psi=1.0; dpsi=w[0]                        # locally growing branch
    logamp=0.0
    for wi,de in zip(wm,deta):
        x=wi*de; ch=np.cosh(x); sh=np.sinh(x)
        p=ch*psi+(sh/wi)*dpsi; d=wi*sh*psi+ch*dpsi
        psi,dpsi=p,d
        if psi>1e100: logamp+=np.log(psi); dpsi/=psi; psi=1.0   # rescale to avoid overflow
    logamp+=np.log(psi)
    Iw=np.sum(wm*deta)
    return np.exp(-logamp), np.exp(-Iw), Iw, np.sum(deta)
print("   |Delta eta| over the segment = %.4f"%transmission(2)[3])
print()
print("       l      EXACT transmission      WKB exp(-int w d eta)     exact/WKB")
for l in (2,3,4,5,8,15,40):
    ex,wk,Iw,_=transmission(l)
    print("     %4d       %.6e           %.6e         %8.4f"%(l,ex,wk,ex/wk))
