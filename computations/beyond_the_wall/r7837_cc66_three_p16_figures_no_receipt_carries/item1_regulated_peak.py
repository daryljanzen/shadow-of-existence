"""Item (1): the regulated peak on P16's own background."""
from math import pi, sqrt

G, C = 6.67430e-11, 2.99792458e8
MPC = 3.0856775814913673e22
GYR = 3.1556952e16   # s in a Julian Gyr

def lam(H0_kms_mpc, om):
    H0 = H0_kms_mpc * 1e3 / MPC
    return 3.0 * H0**2 * (1.0 - om) / C**2

print('== Lambda on the two backgrounds ==')
LAM_P16 = lam(68.60, 0.2973)      # the distance data's point, which P16 states
LAM_SM  = lam(67.36, 0.3153)      # Planck 2018 TT,TE,EE+lowE+lensing
print(f'   P16 background (68.60, 0.2973): Lambda = {LAM_P16:.4e} m^-2   (paper prints 1.1593e-52)')
print(f'   Planck  (67.36, 0.3153):        Lambda = {LAM_SM:.4e} m^-2   (order prints 1.1056e-52)')

print()
print('== alpha = sqrt(3/Lambda) and the lap turnaround pi*alpha/3 ==')
for label, L, printed in (('P16 background', LAM_P16, 17.8), ('standard model', LAM_SM, 18.2)):
    alpha = sqrt(3.0 / L)
    tau = pi * alpha / 3.0 / C / GYR
    print(f'   {label:15s} alpha = {alpha:.5e} m   pi*alpha/3 = {tau:.3f} Gyr   (printed {printed})'
          f'   miss {abs(tau-printed):.3f} Gyr')

print()
print('== the Nariai cap:  A <= 2*alpha/(3*sqrt3), with A the mass parameter 2GM/c^2 ==')
for label, L in (('P16 background', LAM_P16), ('standard model', LAM_SM)):
    alpha = sqrt(3.0 / L)
    A_max = 2.0 * alpha / (3.0 * sqrt(3.0))
    M_max = A_max * C**2 / (2.0 * G)
    print(f'   {label:15s} M_Nariai = {M_max:.4e} kg')
    print(f'        P16 worked progenitor 4.17e52 kg sits at {4.17e52/M_max:.4f} of the cap')

print()
print('== the collapse-branch extremum r^3 = 2 M alpha^2, in units of R_s = 2GM/c^2 ==')
alpha = sqrt(3.0 / LAM_P16)
for M in (4.17e52, 1.0e52, 1.989e30):
    Rs = 2.0 * G * M / C**2
    # r^3 = 2 M alpha^2 is dimensionally (length)^3 only with M as a LENGTH: use A = 2GM/c^2
    r_ext = (2.0 * (G * M / C**2) * alpha**2) ** (1.0 / 3.0)
    print(f'   M = {M:.3e} kg: R_s = {Rs:.4e} m, r_ext = {r_ext:.4e} m, r_ext/R_s = {r_ext/Rs:.4e}')
print('   => r_ext/R_s scales as M^(-2/3): not a pure number, the mass must be named.')
