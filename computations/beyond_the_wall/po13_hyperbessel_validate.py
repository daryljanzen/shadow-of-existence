import numpy as np
from scipy.special import gammaln, spherical_jn

def phi_grid(l, beta, chi):
    """Phi^beta_l(chi), flat-normalised. Rescaled log-space normalised-Gegenbauer recurrence:
    true_R = workingR*exp(scale); rescale working R up when it underflows, track log|R| + sign.
    Phi = sign_R * exp(logpre + log|R|). Handles low-l/high-beta (logpre large, R tiny)."""
    beta = np.asarray(beta); l = int(l); chi = np.atleast_1d(np.asarray(chi, float))
    a = l + 1.0; x = np.cos(chi); s = np.sin(chi); nc = len(chi)
    nmax = int(beta.max()) - 1 - l
    if nmax < 0:
        return np.zeros((nc, len(beta)))
    logR = np.empty((nmax + 1, nc)); sgn = np.empty((nmax + 1, nc))
    Rm2 = np.ones(nc); Rm1 = x.copy(); scale = np.zeros(nc)
    logR[0] = 0.0; sgn[0] = 1.0
    if nmax >= 1:
        logR[1] = np.log(np.abs(x) + 1e-320); sgn[1] = np.sign(x)
    for n in range(2, nmax + 1):
        Rn = (2 * (n + a - 1) * x * Rm1 - (n - 1) * Rm2) / (n + 2 * a - 1)
        logR[n] = np.log(np.abs(Rn) + 1e-320) + scale
        sgn[n] = np.where(Rn >= 0, 1.0, -1.0)
        Rm2, Rm1 = Rm1, Rn
        m = np.abs(Rm1) < 1e-100
        if m.any():
            Rm1[m] *= 1e100; Rm2[m] *= 1e100; scale[m] -= 100 * np.log(10.0)
    beta = np.asarray(beta, float); nidx = (beta - 1 - l).astype(int)
    logpre = l * np.log(2 * beta[:, None] * s[None, :]) + gammaln(l + 1) - gammaln(2 * l + 2)  # (nk,nc)
    val = np.take(sgn, nidx.clip(min=0), axis=0) * np.exp(logpre + np.take(logR, nidx.clip(min=0), axis=0))
    val[nidx < 0, :] = 0.0
    return val.T   # (nc, nk)

chi = 13927/5064.0
import mpmath as mp; mp.mp.dps = 60; cchi = mp.cos(mp.mpf(13927)/mp.mpf(5064)); schi = mp.sin(mp.mpf(13927)/mp.mpf(5064))
def dfact(n):
    r = mp.mpf(1)
    while n > 1: r *= n; n -= 2
    return r
def Phi_mp(beta, l):
    if l > beta-1: return mp.mpf(0)
    n = beta-1-l; N = mp.mpf(beta)**l/(dfact(2*l+1)*mp.gegenbauer(n, l+1, 1))
    return N*schi**l*mp.gegenbauer(n, l+1, cchi)
print("== validate incl. LOW-l/HIGH-beta (the case that broke) ==")
tests = [(25,10),(300,150),(800,400),(1000,100),(1000,50),(1000,10),(500,20),(2000,150),(1500,300)]
for beta,l in tests:
    v = float(phi_grid(l, np.array([beta]), chi)[0,0]); vm = float(Phi_mp(beta,l))
    ok = abs(v-vm) < 1e-9 + abs(vm)*2e-3
    print(f"  Phi^{beta}_{l:3d} = {v:+.6e}  mpmath {vm:+.6e}  {'OK' if ok else 'FAIL'}")
print("== flat limit ==")
for X,l in ((30,10),(300,120)):
    cs=0.02; b=np.array([X/cs]); print(f"  X={X} l={l}: {float(phi_grid(l,b,cs)[0,0]):+.5f} vs j_l {float(spherical_jn(l,X)):+.5f}")
