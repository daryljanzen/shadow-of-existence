"""Item (3): the dissociation thresholds T_9 = 1.2 (D) and 15.8 (He-4) in P16 sec:network.

Two criteria are computed and kept apart:
  (a) the crude single-exponential tail:  B/kT = ln(1/eta)
  (b) nuclear statistical equilibrium:    the eta^(A-1) scaling WITH the
      (m_N/kT)^{3(A-1)/2} statistical factor and the spin/mass weights
"""
from math import log, pi, sqrt

# --- data, named so the pins are parseable ---------------------------------
B_D    = 2.224573      # MeV, deuteron binding
B_HE4  = 28.295674     # MeV, alpha binding
K_PER_MEV = 1.160451812e10   # K per MeV
M_N    = 939.5654133   # MeV, neutron mass (the nucleon scale in the entropy factor)
ETA    = 6.09e-10      # Planck 2018 baryon-to-photon ratio

T9_D_PRINTED, T9_HE_PRINTED = 1.2, 15.8

mev = lambda t9: t9 * 1e9 / K_PER_MEV          # T_9 -> kT in MeV
t9  = lambda kt: kt * K_PER_MEV / 1e9          # kT in MeV -> T_9

print('== what the printed pair implies, read backwards ==')
x_d  = B_D   / mev(T9_D_PRINTED)
x_he = B_HE4 / mev(T9_HE_PRINTED)
print(f'   B/kT at the printed T_9: deuterium {x_d:.2f}, helium-4 {x_he:.2f}')
print(f'   they differ by {abs(x_d-x_he)/((x_d+x_he)/2)*100:.2f} per cent')
print(f'   ln(1/eta) at eta={ETA:.3g} is {log(1/ETA):.2f}')

print()
print('== (a) the crude single-exponential criterion  B/kT = ln(1/eta) ==')
x_single = log(1.0 / ETA)
for name, B, printed in (('deuterium', B_D, T9_D_PRINTED), ('helium-4', B_HE4, T9_HE_PRINTED)):
    kt = B / x_single
    print(f'   {name:10s} kT = {kt:.4f} MeV -> T_9 = {t9(kt):.3f}   (printed {printed})'
          f'   miss {abs(t9(kt)-printed)/printed*100:.1f}%')

print()
print('== (b) nuclear statistical equilibrium, eta^(A-1) with the statistical weights ==')
# X_A ~ 1 when  g_A A^{3/2} 2^{-A} (zeta(3)/pi^2 * 4)^{A-1} eta^{A-1}
#                 (2 pi m_N / kT)^{-3(A-1)/2} * ... exp(B/kT) = 1
# Solve  B/kT = (A-1)[ ln(1/eta) + (3/2) ln(m_N/kT) ] + ln(W_A)  iteratively.
ZETA3 = 1.2020569031595943
def nse_threshold(B, A, Z, g_A, label):
    # W_A collects the order-one weights: g_A A^{3/2} / 2^A and the (zeta3*4/pi^2)^{A-1}
    # and the (2 pi)^{-3(A-1)/2}; written explicitly so the arithmetic is visible.
    kt = B / (A - 1 + 1) / 1.0 if A > 1 else B
    kt = 0.1  # MeV, seed
    for _ in range(200):
        lnW = (log(g_A) + 1.5 * log(A) - A * log(2.0)
               + (A - 1) * log(4.0 * ZETA3 / pi**2)
               - 1.5 * (A - 1) * log(2.0 * pi))
        x = (A - 1) * (log(1.0 / ETA) + 1.5 * log(M_N / kt)) + lnW
        kt_new = B / x
        if abs(kt_new - kt) < 1e-12:
            kt = kt_new
            break
        kt = kt_new
    return kt, x

for name, B, A, Z, g, printed in (('deuterium', B_D, 2, 1, 3.0, T9_D_PRINTED),
                                  ('helium-4', B_HE4, 4, 2, 1.0, T9_HE_PRINTED)):
    kt, x = nse_threshold(B, A, Z, g, name)
    print(f'   {name:10s} B/kT = {x:7.2f}   kT = {kt:.5f} MeV -> T_9 = {t9(kt):.3f}'
          f'   (printed {printed})  factor {printed/t9(kt):.2f} off')

print()
print("== the paper's own other deuterium figure, for consistency ==")
print(f'   P16 sec:peak states T_D = 0.07 MeV, which is T_9 = {t9(0.07):.3f}')
print(f'   that corresponds to B/kT = {B_D/0.07:.2f}, NOT {x_d:.2f}')
