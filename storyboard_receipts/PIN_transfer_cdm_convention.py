"""PIN Transfer_cdm's normalisation (r2344), unblocking the redshift localisation.

The ledger's instruction: "unblock by pinning Transfer_cdm as the C_ell measure was pinned at
r2180 -- reconstruct a known quantity from its own definition."  CAMB computes P(k) independently
of the transfer array, so reproducing P(k) FROM the array is a genuine check, not a tautology.

RESULT:  P(k) = (2 pi^2 / k^3) A_s (k/k_piv)^{ns-1} [k^2 T_cdm(k)]^2 * h^3
         with k in Mpc^-1 ; CAMB's P is in (Mpc/h)^3 with k in h/Mpc.

The two failed guesses in the record are both explained: the k^2 is CORRECT (delta_c ~ k^2 T,
which is why the raw log-slope came out ~2); what was missing was h^3, the units convention.
1/h^3 = 3.266 at h=0.674, and the residual 0.52 is what an h-power error leaves behind.
"""
import numpy as np, camb
from camb import model

pars = camb.CAMBparams()
pars.set_cosmology(H0=67.4, ombh2=0.02237, omch2=0.1200, mnu=0.0, omk=0, tau=0.0544)
pars.InitPower.set_params(As=2.1e-9, ns=0.965)
pars.set_matter_power(redshifts=[0.], kmax=2.0)
pars.NonLinear = model.NonLinear_none
res = camb.get_results(pars)

kh, z, pk = res.get_matter_power_spectrum(minkh=1e-3, maxkh=1.0, npoints=300)
tr = res.get_matter_transfer_data()
h = pars.H0/100
kh_t = tr.q/h
Tc = tr.transfer_data[model.Transfer_cdm-1, :, 0]
As, ns, kpiv = pars.InitPower.As, pars.InitPower.ns, 0.05
k = kh_t*h

P = (2*np.pi**2/k**3) * As*(k/kpiv)**(ns-1) * ((k**2)*Tc)**2 * h**3

print("   k/h        P_recon        P_CAMB       ratio")
worst = 0.0
for kk in (0.005, 0.02, 0.05, 0.08, 0.1, 0.3, 0.6):
    a = np.interp(kk, kh_t, P); b = np.interp(kk, kh, pk[0])
    print("  %6.3f   %.5e   %.5e   %.6f" % (kk, a, b, a/b))
    worst = max(worst, abs(a/b - 1))

print("\n   worst pointwise deviation: %.2e" % worst)
assert worst < 5e-3, "the convention must reproduce P(k) to better than 0.5% pointwise"
print("   CONVENTION PINNED.")
