import numpy as np
from scipy.special import gammaln, spherical_jn

def phi_hyper_l(l, betas, chi):
    """Vectorised: for fixed l, return Phi^beta_l(chi) for all integer beta in `betas` (>= l+1), chi scalar.
    Normalised Gegenbauer recurrence R_n = C_n^{l+1}(cos chi)/C_n^{l+1}(1) (bounded), prefactor in log-space:
      Phi^beta_l = exp[l*log(2 beta sin chi) + gammaln(l+1) - gammaln(2l+2)] * R_{beta-1-l}."""
    a = l + 1.0; x = np.cos(chi); s = np.sin(chi)
    nmax = int(betas.max()) - 1 - l
    R = np.empty(nmax + 1)
    R[0] = 1.0
    if nmax >= 1: R[1] = x
    for n in range(2, nmax + 1):
        R[n] = (2*(n+a-1)*x*R[n-1] - (n-1)*R[n-2]) / (n + 2*a - 1)
    beta = np.asarray(betas, float)
    n = (beta - 1 - l).astype(int)
    logpre = l*np.log(2*beta*s) + gammaln(l+1) - gammaln(2*l+2)
    out = np.exp(logpre) * R[n]
    out[l > beta-1] = 0.0
    return out

chi = 13927/5064.0
print("== exact-value check (chi=2.750) ==")
for beta,l,ex in ((25,10,0.069844),(5,2,0.202204),(50,10,-0.020297),(300,150,-4.085015e-9),
                  (600,300,-2.555190e-15),(800,400,-2.221035e-19),(1000,500,-2.058397e-23)):
    v=float(phi_hyper_l(l, np.array([beta]), chi)[0])
    ok = abs(v-ex) < 1e-6 + abs(ex)*1e-3
    print(f"  Phi^{beta}_{l} = {v:+.6e}  exact {ex:+.6e}  {'OK' if ok else 'FAIL'}")
print("\n== flat limit: Phi^beta_l(chi_small) -> j_l(beta*chi) ==")
for X,l in ((30,10),(120,40),(300,120)):
    chi_s = 0.02; beta=np.array([X/chi_s])
    vh=float(phi_hyper_l(l,beta,chi_s)[0]); vj=float(spherical_jn(l,X))
    print(f"  X={X} l={l}: hyper {vh:+.5f}  j_l {vj:+.5f}  {'OK' if abs(vh-vj)<5e-3 else 'diff %.2g'%abs(vh-vj)}")
