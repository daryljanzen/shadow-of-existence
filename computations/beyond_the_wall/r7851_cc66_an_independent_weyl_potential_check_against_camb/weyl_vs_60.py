"""r7851+cc66: CAMB's WEYL POTENTIAL AGAINST 60's CARRIED TRANSFER, ON 60's OWN GRID.

Order r7851 (69) items ① and ②.  60's r7852 locates their lensing fault in the instrument's
transfer: their Phi keeps decaying through matter domination.  This is the independent curve that
repair will be read against.

** THE GRID IS 60's, READ OFF THEIR CODE AND NOT CHOSEN. **  r7846/phiphi.py:
  k   = logspace(log10(KMIN=2e-4), log10(KMAX=1.0), NKP=220) /Mpc  (48 for the growth solve)
  ETAREF = 4000 Mpc, which their own comment calls "the z = 12.8 the instrument freezes at" --
  and GrowthKDep.a_start comes out 0.0722905, i.e. z = 12.8331, confirming it.

** WHAT IS COMPARED, AND WHY IT IS THE RIGHT PAIR. **  60's `g` is D(a)/a.  In the Poisson
equation the Weyl potential carries Phi ~ delta/(a k^2) ~ D(a)/a times a primordial factor, so
their `g` IS their Phi's time dependence.  Both sides are therefore normalised to THEIR OWN freeze
epoch and compared as pure shapes, which removes every normalisation convention from the answer:

    R_camb(k, z) = Weyl(k, z) / Weyl(k, z_ref)
    R_60(k, z)   = g_of(k, a(z)) / g_of(k, a(z_ref))         z_ref = 12.8331
    frac(k, z)   = R_60 / R_camb - 1

** PPGRID IS GONE. **  60's banked Phi-derived bandpowers lived in
/tmp/claude-0/phiphi_grid_eta4000 and went with the scratch, as their 555-bin mask did at r7847.
So this runs THEIR CODE (growth_kdep.GrowthKDep) rather than reading a vanished artefact -- which
tests the algorithm and reproduces.

COMPUTES: CAMB's Weyl potential on 60's k grid across matter domination, 60's own growth transfer
          on the same grid from their own solver, and the fractional difference between the two as
          shapes normalised at their freeze epoch.  It pins no cosmological parameter as a result.
Run: python3 -I weyl_vs_60.py            (numpy, scipy, camb)
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_'
                                      'lensing_bandpowers'))
import camb                                                                  # noqa: E402
import growth_kdep as GK                                                     # noqa: E402

H0, OM, WB, NS, AS, TAU = 67.40, 0.3150, 0.0224, 0.965, 2.1e-9, 0.054
KMIN, KMAX, NKP = 2e-4, 1.0, 220
NK_SOLVE = 48                      # 60's own choice for the growth solve
ZS = [12.8331, 10.0, 8.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.5, 1.0, 0.7, 0.5, 0.3, 0.15, 0.0]
OUT = os.path.join(HERE, 'weyl_vs_60.json')
NPZ = os.path.join(HERE, 'weyl_vs_60.npz')


def main():
    kk_full = np.logspace(np.log10(KMIN), np.log10(KMAX), NKP)
    kk = np.logspace(np.log10(KMIN), np.log10(KMAX), NK_SOLVE)

    # ---------------------------------------------------------------- 60's side, their own solver
    g = GK.GrowthKDep(mnu_ev=0.0, n_species=3, kk=kk)
    z_ref = 1.0 / float(g.a_start) - 1.0
    print('  60: ETAREF = %.1f Mpc -> a_start = %.7f -> z_ref = %.4f'
          % (GK.ETAREF, g.a_start, z_ref), flush=True)

    # ---------------------------------------------------------------- CAMB's side
    p = camb.set_params(H0=H0, ombh2=WB, omch2=OM * (H0 / 100.0) ** 2 - WB, omk=0,
                        tau=TAU, As=AS, ns=NS, mnu=0.0, num_massive_neutrinos=0)
    p.set_matter_power(redshifts=[0.0], kmax=2.0 * KMAX)
    res = camb.get_results(p)
    zs = np.array([z_ref] + [z for z in ZS if abs(z - z_ref) > 1e-6], float)
    ev = res.get_redshift_evolution(kk, zs, ['Weyl'])      # (nk, nz, 1)
    W = np.asarray(ev[:, :, 0], float)
    print('  CAMB: Weyl tabulated on %d k by %d z' % W.shape, flush=True)

    R_camb = W / W[:, [0]]
    # g_of is VECTORISED and returns (nk, na), so one call does the whole table and the
    # normalisation broadcasts -- a per-(k, z) loop would be the slow path their own surface()
    # docstring warns about
    avals = 1.0 / (1.0 + zs)
    R_60 = g.g_of(kk, avals) / g.g_of(kk, float(g.a_start))
    assert R_60.shape == R_camb.shape, (R_60.shape, R_camb.shape)
    frac = R_60 / R_camb - 1.0

    # ---------------------------------------------------------------- the registered readings
    def at(kv, zv):
        i = int(np.argmin(np.abs(kk - kv)))
        j = int(np.argmin(np.abs(zs - zv)))
        return i, j

    i01, j10 = at(0.01, 10.0)
    _, j1 = at(0.01, 1.0)
    _, j0 = at(0.01, 0.0)
    camb_drift_10_to_1 = abs(R_camb[i01, j1] / R_camb[i01, j10] - 1.0)
    camb_drift_ref_to_0 = abs(R_camb[i01, j0] - 1.0)

    out = dict(
        grid=dict(kmin=KMIN, kmax=KMAX, nkp_kernel=NKP, nk_solve=NK_SOLVE,
                  etaref_mpc=float(GK.ETAREF), z_ref=z_ref, zs=[float(v) for v in zs]),
        control=dict(H0=H0, Om=OM, ombh2=WB, ns=NS, tau=TAU, As=AS),
        camb_weyl_k001=dict(z=[float(v) for v in zs],
                            weyl=[float(v) for v in W[i01]],
                            shape=[float(v) for v in R_camb[i01]]),
        camb_drift_z10_to_z1_at_k001=float(camb_drift_10_to_1),
        camb_drift_zref_to_z0_at_k001=float(camb_drift_ref_to_0),
        frac_at_k001=dict(zip([('%.4f' % v) for v in zs], [float(v) for v in frac[i01]])),
        frac_at_z1=dict(k=[float(v) for v in kk], frac=[float(v) for v in frac[:, j1]]),
        frac_summary=dict(
            at_k001_z10=float(frac[i01, j10]), at_k001_z1=float(frac[i01, j1]),
            at_k001_z0=float(frac[i01, j0]),
            z1_min=float(np.min(frac[:, j1])), z1_max=float(np.max(frac[:, j1])),
            z1_absmin=float(np.min(np.abs(frac[:, j1]))),
            z1_absmax=float(np.max(np.abs(frac[:, j1]))),
            k_spread_factor_at_z1=float(np.max(np.abs(frac[:, j1]))
                                        / max(np.min(np.abs(frac[:, j1])), 1e-30))))
    json.dump(out, open(OUT, 'w'), indent=1)
    np.savez_compressed(NPZ, kk=kk, kk_kernel=kk_full, zs=zs, weyl=W,
                        R_camb=R_camb, R_60=R_60, frac=frac)

    print('\n  CAMB Weyl shape at k = 0.01 /Mpc, normalised at z_ref:')
    for zv, sh in zip(zs, R_camb[i01]):
        print('      z = %7.4f   Phi/Phi_ref = %.6f' % (zv, sh), flush=True)
    print('\n  Ⓐ CAMB drift z = 10 -> z = 1 at k = 0.01: %.4f per cent'
          % (100.0 * camb_drift_10_to_1))
    print('     and z_ref -> z = 0: %.4f per cent' % (100.0 * camb_drift_ref_to_0))
    print('\n  Ⓑ fractional difference (60 / CAMB - 1) at k = 0.01:')
    for zv, fv in zip(zs, frac[i01]):
        print('      z = %7.4f   %+.4f  (%+.2f per cent)' % (zv, fv, 100.0 * fv), flush=True)
    print('\n  Ⓓ across k at z = 1: min %+.4f, max %+.4f, |spread| factor %.3f'
          % (out['frac_summary']['z1_min'], out['frac_summary']['z1_max'],
             out['frac_summary']['k_spread_factor_at_z1']))
    print('\n  wrote %s and %s' % (os.path.basename(OUT), os.path.basename(NPZ)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
