"""Item (2): the band-period obstacle -- c_s from 0.018, int c_s deta = 0.304 vs frozen 3.565."""
from math import pi, sqrt, cos, sin, acos
from scipy.optimize import brentq
from scipy.integrate import quad

# closed dust+radiation interior:  a'' + a = A/2,  a'^2 = B + A a - a^2
# with a(0)=0:   a(eta) = (A/2)(1-cos eta) + sqrt(B) sin eta
# rho_m a^3 ~ A, rho_r a^4 ~ B  =>  rho_m/rho_r = (A/B) a
# c_s^2 = 4 rho_r / (3 (4 rho_r + 3 rho_m)) = 4 / (3 (4 + 3 (A/B) a))
def a_of(eta, A, B):
    return 0.5 * A * (1.0 - cos(eta)) + sqrt(B) * sin(eta)

def cs_of(eta, A, B):
    return sqrt(4.0 / (3.0 * (4.0 + 3.0 * (A / B) * a_of(eta, A, B))))

def lap_end(A, B):
    # the lap closes where a returns to zero
    lo = pi
    return brentq(lambda e: a_of(e, A, B), lo, 2.0 * pi - 1e-14)

def turnaround(A, B):
    return brentq(lambda e: 0.5 * A * sin(e) + sqrt(B) * cos(e), 0.1, pi)

B = 1.0  # scale is free; only A/B enters c_s, and only A/sqrt(B) enters the shape
CS_TURN_PRINTED, INT_RUN_PRINTED, INT_FROZEN_PRINTED, FACTOR_PRINTED = 0.018, 0.304, 3.565, 11.7

print('== fix A by requiring c_s at turnaround = 0.018 ==')
f = lambda A: cs_of(turnaround(A, B), A, B) - CS_TURN_PRINTED
A = brentq(f, 1.0, 1e9)
eta_t, eta_e = turnaround(A, B), lap_end(A, B)
print(f'   A/sqrt(B) = {A/sqrt(B):.4f}')
print(f'   turnaround at eta = {eta_t:.6f}, a_max = {a_of(eta_t,A,B):.6f}')
print(f'   c_s at turnaround = {cs_of(eta_t,A,B):.6f}   (printed {CS_TURN_PRINTED})')
print(f'   lap closes at eta = {eta_e:.6f}   (2*pi = {2*pi:.6f})')

run = quad(cs_of, 0.0, eta_e, args=(A, B), limit=400)[0]
frozen = eta_e / sqrt(3.0)
print()
print('== the two integrals over the lap ==')
print(f'   running  int c_s deta = {run:.4f}    (printed {INT_RUN_PRINTED})   miss {abs(run-INT_RUN_PRINTED)/INT_RUN_PRINTED*100:.1f}%')
print(f'   frozen   eta_end/sqrt3 = {frozen:.4f}  (printed {INT_FROZEN_PRINTED})  miss {abs(frozen-INT_FROZEN_PRINTED)/INT_FROZEN_PRINTED*100:.1f}%')
print(f'   factor   {frozen/run:.3f}             (printed {FACTOR_PRINTED})')
print()
print('== is the printed factor independent, or derived? ==')
print(f'   printed 3.565 / printed 0.304 = {INT_FROZEN_PRINTED/INT_RUN_PRINTED:.4f}  -> rounds to '
      f'{round(INT_FROZEN_PRINTED/INT_RUN_PRINTED,1)}')
print()
print('== what eta_end the printed frozen integral implies ==')
print(f'   3.565 * sqrt3 = {INT_FROZEN_PRINTED*sqrt(3.0):.5f}   against the computed {eta_e:.5f}')
print(f'   and 2*pi (pure dust, no radiation) = {2*pi:.5f}')
