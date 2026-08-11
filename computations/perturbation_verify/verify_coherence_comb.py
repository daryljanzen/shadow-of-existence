"""
COHERENCE FROM THE NULL SEAM (P12 sec:coherence) -- upgrading the [I] illustration to a computed [R].
CLAIM under test: the sharp acoustic comb requires a COMMON phase across modes of a given k; the null
seam supplies exactly one datum per mode (characteristic/Goursat data on a null surface is the field
along the generators, NOT field+momentum), hence one phase, hence coherence. The contrast that carries
the claim: integrate the tightly-coupled acoustic oscillator forward with (a) a common seam phase vs
(b) phases drawn at random per mode, and compare the angular power.

Tightly-coupled monopole at last scattering (standard WKB): Theta(k) ~ cos(k r_s + phi_k) * D(k),
D(k)=exp(-(k/k_D)^2) the Silk-damping envelope. Coherent: phi_k=const (the seam's single datum).
Incoherent: phi_k ~ U(0,2pi) per mode (a hypothetical second, free datum -- the Cauchy case).
C_ell ~ Theta(k)^2 at k = ell/D_C (flat projection, the banked CR distance).

This is the Albrecht-Coulson-Ferreira-Magueijo coherence demonstration applied to the seam: it shows
WHY one-datum-per-mode is sufficient for the comb, not merely asserts it. It does NOT replace a full
seam-to-recombination Boltzmann solve -- that remains the honest [R] flag; what is closed is the
illustration -> computation step and the quantitative coherent/incoherent contrast.
"""
import numpy as np
rs=147.0          # sound horizon at last scattering [Mpc]
D_C=13864.0       # banked CR comoving distance (flat projection)
kD=0.13           # Silk damping scale [1/Mpc]
ell=np.arange(2,1500); k=ell/D_C
env=np.exp(-(k/kD)**2)
# coherent: single common seam phase (adiabatic growing mode, phi=0)
Cc=(np.cos(k*rs)**2)*env**2
# incoherent: random phase per mode, averaged over realisations
rng=np.random.default_rng(0); N=400
Ci=np.zeros_like(k)
for _ in range(N): Ci+=(np.cos(k*rs+rng.uniform(0,2*np.pi,len(k)))**2)*env**2
Ci/=N
# comb diagnostics: peak/trough contrast in the first three acoustic orders
def contrast(C):
    # peaks near k rs = n pi, troughs near (n-1/2) pi
    out=[]
    for n in (1,2,3):
        kp=n*np.pi/rs; kt=(n-0.5)*np.pi/rs
        ip=np.argmin(abs(k-kp)); it=np.argmin(abs(k-kt))
        out.append(C[ip]/max(C[it],1e-12))
    return out
print(f"acoustic comb spacing: Delta-k = pi/r_s = {np.pi/rs:.4f}/Mpc  ->  Delta-ell ~ {np.pi/rs*D_C:.0f}")
print(f"first three peak multipoles ell_n ~ n*pi*D_C/r_s = "
      f"{', '.join(f'{int(n*np.pi*D_C/rs)}' for n in (1,2,3))}")
print("\npeak/trough contrast (large = sharp comb, ~1 = washed out):")
print(f"  COHERENT (common seam phase):   orders 1-3 = {[f'{c:.0f}' for c in contrast(Cc)]}")
print(f"  INCOHERENT (random per mode):   orders 1-3 = {[f'{c:.2f}' for c in contrast(Ci)]}")
print(f"\ncoherent power variation across the band (max/min): {Cc[ell<1000].max()/max(Cc[ell<1000].min(),1e-12):.0f}")
print(f"incoherent power variation (max/min):                {Ci[ell<1000].max()/Ci[ell<1000].min():.2f}")
print("\nVERDICT: a common seam phase -> sharp regular comb (peak/trough >> 1); random phases -> flat,")
print("no comb (contrast ~1). The null seam's single characteristic datum per mode IS one phase per")
print("mode, so it lands in the coherent column by construction. Mechanism computed, not just asserted;")
print("the full seam-to-recombination transfer remains the honest open [R].")

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# Print-only receipt: the coherent/incoherent contrast was computed and displayed but never
# tested.  P15 sec:coherence quotes this receipt for the comb spacing Delta-ell ~ 296 and for
# "peak-to-trough contrast ~1 against the coherent comb's many orders of magnitude"; INDEX.md
# row 112 quotes the peak multipoles 296, 592, 888.  All pinned here.
_dell = np.pi / rs * D_C
assert abs(_dell - 296.29) < 0.05, f"Delta-ell = {_dell}, receipt prints 296"
assert abs(_dell - 296.0) < 1.0, "P15 sec:coherence quotes Delta-ell ~ 296"
assert [int(n * np.pi * D_C / rs) for n in (1, 2, 3)] == [296, 592, 888]
_cc = contrast(Cc); _ci = contrast(Ci)
# the coherent column: sharp comb, many orders of magnitude (receipt prints 398572/41929/106736)
assert min(_cc) > 1e4, f"coherent comb contrast collapsed to {min(_cc)}"
assert abs(_cc[0] - 398572.0) < 500.0, f"order-1 coherent contrast = {_cc[0]}"
# the incoherent control: washed out, contrast ~1 (receipt prints 0.94/0.86/0.83 over 400 draws)
assert max(_ci) < 1.2 and min(_ci) > 0.7, f"incoherent contrast {_ci} is not ~1"
assert abs(_ci[0] - 0.936) < 0.02
# the discriminator must actually separate the two columns by orders of magnitude
assert min(_cc) > 1e4 * max(_ci), "coherent and incoherent are not separated -- no control"
# band-wide power variation: 420477 coherent vs 2.13 incoherent
assert abs(Cc[ell < 1000].max() / max(Cc[ell < 1000].min(), 1e-12) - 420477.0) < 500.0
assert abs(Ci[ell < 1000].max() / Ci[ell < 1000].min() - 2.13) < 0.02
print("\n[assertions r2376+c54.160] Delta-ell 296 (peaks 296/592/888), coherent 3.99e5 vs incoherent 0.94: pinned.")
