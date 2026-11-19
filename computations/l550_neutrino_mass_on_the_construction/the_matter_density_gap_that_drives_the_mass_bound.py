"""The matter-density gap that drives the cosmological neutrino-mass bound, on the standard model and on
this construction's arm of record.

The DESI DR2 + CMB bound (Sum m_nu < 0.0642 eV, effective mass -0.101 +0.047 -0.056 eV in LambdaCDM;
arXiv:2503.14744) is driven by BAO preferring a lower matter density than the CMB along the theta_*
degeneracy.  With massive neutrinos the late matter the distances see is omega_cb + omega_nu while the
early matter the spectrum's driving sees is omega_cb, so Sum m_nu ~ 93.14 eV x (omega_m,late - omega_cb).

Read here from banked numbers, nothing run:
  LambdaCDM: Planck 2018 (H0 67.36, Om 0.3153) against DESI DR2 BAO (Om 0.2975) at the BAO+theta_* H0 68.5.
  CR: the distances' point (68.60, 0.2973) against the arm's leaf-geometry refit minimum
      (68.585672, 0.294463), receipt P15_with_the_projection_distance_on_the_leaf_rate...
Working computation for the order routed through 69; the bound itself is the arm refit with the mass free.
"""
pl = 0.6736 ** 2 * 0.3153
desi = 0.685 ** 2 * 0.2975
cr_bao = 0.6860 ** 2 * 0.2973
cr_arm = 0.685857 ** 2 * 0.294463
print(f'LCDM: CMB omega_m {pl:.5f}, BAO {desi:.5f}: CMB {100 * (pl / desi - 1):+.2f}% -> crude Sum m_nu {93.14 * (desi - pl):+.3f} eV (full analysis -0.101)')
print(f'CR  : arm omega_m {cr_arm:.5f}, distances {cr_bao:.5f}: arm {100 * (cr_arm / cr_bao - 1):+.2f}% -> crude Sum m_nu {93.14 * (cr_bao - cr_arm):+.3f} eV')
print(f'      scaled by the LCDM crude-to-full ratio {-0.101 / (93.14 * (desi - pl)):.2f}: {93.14 * (cr_bao - cr_arm) * -0.101 / (93.14 * (desi - pl)):+.3f} eV')
