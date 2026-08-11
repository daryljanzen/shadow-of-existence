import numpy as np
from scipy.integrate import solve_ivp
# Covariant (Laplace-Beltrami) ordering of (2pi/3) p_a^2/a:
#   minisuperspace metric G_aa = 3a/4pi (from T = (1/2)G_aa adot^2), geodesic coord
#   x = ∫ sqrt(G_aa) da ∝ a^{3/2}.  Then kinetic -> -d^2/dx^2 on L^2((0,∞),dx),
#   and V = -(Λ/8π)a^3 ∝ -a^3 = -(x^{2/3})^3 = -x^2.  So H ∝ -d^2/dx^2 - c x^2.
# Self-adjointness = Weyl limit-point/limit-circle at x=0 and x=∞.
#  x=0: potential negligible, free -ψ''=±iψ, both solutions L^2 near 0  -> limit-CIRCLE (def +1).
#  x=∞: the load-bearing, slightly subtle claim -- check it numerically below.
# Deficiency test at ∞: solve (-ψ'' - x^2 ψ) = i ψ outward; if |ψ| decays slower than x^{-1/2}
# the solution is NOT L^2 (∫|ψ|^2 dx diverges) -> limit-POINT at ∞ (def +0).
def rhs(x, y):
    psi, dpsi = y
    return [dpsi, -(1j*psi + x**2*psi)]   # ψ'' = -(i + x^2)ψ
x0, xf = 1.0, 200.0
sol = solve_ivp(rhs, [x0, xf], [1+0j, 0+0j], rtol=1e-9, atol=1e-12, dense_output=True,
                method='RK45', max_step=0.01)
xs = np.linspace(50, 200, 16)
amp = np.abs(sol.sol(xs)[0])
# WKB predicts amplitude ~ x^{-1/2}; fit log|ψ| vs log x
p = np.polyfit(np.log(xs), np.log(amp), 1)
print(f"large-x amplitude scaling  |ψ| ~ x^p,  fitted p = {p[0]:+.3f}   (WKB predicts -0.5)")
print(f"=> |ψ|^2 ~ x^(2p) = x^{2*p[0]:+.3f};  ∫|ψ|^2 dx { 'DIVERGES (not L^2) -> limit-POINT at ∞' if 2*p[0] > -1 else 'converges' }")
print()
print("RESULT (covariant ordering): limit-circle at a=0, limit-point at a=∞")
print(" => H_phys is NOT essentially self-adjoint; deficiency indices (1,1);")
print("    a one-parameter U(1) family of self-adjoint extensions, fixed by a")
print("    boundary condition at a=0 alone.  The -Λa^3 term (->-x^2, the marginal case) does")
print("    NOT force a condition at infinity.")
