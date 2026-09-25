#!/usr/bin/env python3
"""
make_fig_acoustic_two_arm.py -- the acoustic figure `r6879` ordered, built properly.

Writes:
  corpus/fig_acoustic_two_arm.pdf          the figure P15 carries
  computations/beyond_the_wall/spectra/cc66_fig_acoustic_numbers.npz
                                           every number plotted, banked so the receipt
                                           can recompute independently and gate against it

WHAT IS PLOTTED, AND THE CHOICES ARE STATED RATHER THAN LEFT IN THE CODE.

 (a) LINEAR in ell over the acoustic range, both arms at their VERIFIED 185-bin refit minima
     (`cc66_r185_verify_{lcdm,cr}.npz`, r6825+cc66.25), each carried through P15's own derived
     lensing operator and binned onto plik_lite's TT windows.  ** The single amplitude is fitted
     on the FULL bandpower covariance, not on diagonal errors ** -- the order asks for that
     explicitly, and it matters: on diagonal errors the CR amplitude comes out 0.85% high and the
     residual's band means roughly double.  Planck TT bandpowers with diagonal errors as the
     points, since a point needs one error bar; the fit and the residuals use the covariance.

 (b) LOGARITHMIC in ell from ell = 2, as a RATIO TO THE CONTROL, because that is the form in which
     the corpus carries the low multipoles: `P15_confront_lowell_data.py` holds the observed
     low-ell band as a ratio to flat LCDM (there are no absolute low-ell bandpowers in this tree,
     plik_lite here being high-ell only from ell = 32).  ** Those ratios are put back into D_l by
     multiplying the control's own low-ell D_l from the same CAMB call the lensing operator comes
     from, so the floor is shown as the suppression it is and in the same units as the peaks; the
     reconstruction is named here because it is a reconstruction. **  The floor at ell = 2-8 is the
     banked sweep's
     DECOUPLED adjudicated column (r6825+cc66.26), and the minimum at ell = 4 -- the one shape this
     construction predicts that the standard model does not -- is marked.

 RESIDUALS beneath each panel, both arms on one axis so the shared part is visible.  ** WHITENED
 residuals are plotted **: L^-1 (A m - d) with L the Cholesky factor of the covariance, which have
 unit covariance by construction, so "in sigma" is exact rather than approximate.  The diagonal
 version is banked alongside for comparison and the caption names which is shown.  ** Whitening
 mixes bins, so a whitened point is not attached to one multipole -- it is plotted at its bin's
 centre for legibility and that is a presentational choice, not a claim. **

WHAT IS NOT PLOTTED.  No foreground or beam uncertainty beyond what plik_lite's covariance already
marginalises.  No low-ell absolute spectrum, for the reason above.  The 1900 cut on panel (a)'s
scored bins is the figure's own, so that the shifted-model tests in the companion receipt use the
same bin set; the full 185-bin chi^2 is quoted in the caption from the refit itself.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
LC, FACB = CS.bin_center_and_fac()
X_DATA, COV = CS.X_DATA, CS.COV_TT


def lensing_ratio():
    """P15's own derived lensing operator, imposed on both arms alike."""
    import camb
    p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                        mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    cl = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK', lmax=3000)
    le, un = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    lg = np.arange(len(le), dtype=float)
    r = np.ones_like(le)
    m = un > 0
    r[m] = le[m] / un[m]
    return lg, r


LG, RATIO = lensing_ratio()
arm = lambda t: (lambda d: (d['ls'], d['Dl']))(np.load(os.path.join(SP, f'cc66_r185_verify_{t}.npz')))
binned = lambda ls, Dl: CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO))

KEEP = np.isfinite(binned(*arm('lcdm'))) & (LC >= 100) & (LC <= 1900)
COVK = COV[np.ix_(KEEP, KEEP)]
CHOL = np.linalg.cholesky(COVK)
LINV = np.linalg.inv(CHOL)
FISH = np.linalg.inv(COVK)
DK, LCK, FACK = X_DATA[KEEP], LC[KEEP], FACB[KEEP]
SIG = np.sqrt(np.diag(COVK))


def fit(t, diagonal=False):
    mb = binned(*arm(t))[KEEP]
    if diagonal:
        A = float(np.sum(mb * DK / SIG ** 2) / np.sum(mb ** 2 / SIG ** 2))
    else:
        A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
    r = A * mb - DK
    return A, mb, r, float(r @ FISH @ r), LINV @ r, r / SIG


def main():
    out = {}
    for t in ('lcdm', 'cr'):
        A, mb, r, c2, w, rd = fit(t)
        Ad, _, rdg, c2d, _, rdd = fit(t, diagonal=True)
        out.update({f'{t}_A': A, f'{t}_A_diag': Ad, f'{t}_chi2': c2, f'{t}_chi2_diagfit': c2d,
                    f'{t}_model': A * mb, f'{t}_whitened': w, f'{t}_diagres': rd,
                    f'{t}_diagres_diagfit': rdd})
        print(f"  {t:5s} A(cov)={A:.2f}  A(diag)={Ad:.2f} ({100*(Ad/A-1):+.3f}%)   "
              f"chi2={c2:.2f} over {int(KEEP.sum())} bins ({c2/int(KEEP.sum()):.3f}/bin)")
    out['ell'] = LCK
    out['data'] = DK
    out['sigma'] = SIG
    wl, wc = out['lcdm_whitened'], out['cr_whitened']
    out['shared_cos'] = float(wc @ wl / np.linalg.norm(wc) / np.linalg.norm(wl))
    out['shared_frac'] = float((wc @ wl) ** 2 / ((wl @ wl) * (wc @ wc)))
    out['cr_chi2_minus_control_dir'] = float(wc @ wc - (wc @ wl) ** 2 / (wl @ wl))
    print(f"  shared: cos={out['shared_cos']:+.4f}  fraction of CR chi2 along the control's "
          f"direction={100*out['shared_frac']:.1f}%  remainder={out['cr_chi2_minus_control_dir']:.1f}")

    low = np.load(os.path.join(SP, 'cc66_lowell_sweep.npz'))
    out['low_ell'] = low['ells'].astype(float)
    out['low_cr'] = low['DECOUPLED_adjudicated_KLO_0_1_NS3_60000']
    out['low_ctl'] = low['DECOUPLED_control_KLO_0_1_NS3_60000']
    # the observed low-ell band, as P15_confront_lowell_data.py carries it (ratio to flat LCDM)
    out['obs_ell'] = np.array([2., 3., 4., 5., 6., 8.])
    out['obs_lo'] = np.array([0.15, 0.58, 0.55, 0.70, 0.85, 0.95])
    out['obs_hi'] = np.array([0.25, 1.10, 1.05, 1.10, 1.05, 1.05])

    np.savez(os.path.join(SP, 'cc66_fig_acoustic_numbers.npz'), **out)
    print(f"  banked -> spectra/cc66_fig_acoustic_numbers.npz")

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec

    C_CTL, C_CR, C_DAT = '#3B6EA5', '#B5482A', '#333333'
    fig = plt.figure(figsize=(13.0, 8.4))
    gs = GridSpec(2, 2, height_ratios=[2.5, 1.0], hspace=0.06, wspace=0.22,
                  left=0.075, right=0.985, top=0.945, bottom=0.085)

    # ---- (a) linear in ell -------------------------------------------------------
    ax = fig.add_subplot(gs[0, 0])
    # ** D_l, NOT C_l.  X_data is binned C_l; plotted raw the peaks vanish under the falling
    #    plateau -- the same trap the locator hit at cc66.28, here in the figure. **
    ax.errorbar(LCK, DK * FACK, yerr=SIG * FACK, fmt='o', ms=2.4, lw=0.7, color=C_DAT,
                alpha=0.75, label='Planck TT bandpowers', zorder=2)
    ax.plot(LCK, out['lcdm_model'] * FACK, '-', color=C_CTL, lw=1.7,
            label=r'flat $\Lambda$CDM control', zorder=3)
    ax.plot(LCK, out['cr_model'] * FACK, '-', color=C_CR, lw=1.7, label='CR, crossing arm', zorder=4)
    ax.set_ylabel(r'$\mathcal{D}_\ell=\ell(\ell+1)C_\ell/2\pi$   $[\mu\mathrm{K}^2]$')
    ax.set_xlim(90, 1910)
    ax.legend(frameon=False, fontsize=9, loc='upper right')
    ax.set_title('(a)  both arms at their verified refit minima, linear in $\\ell$', fontsize=10, loc='left')
    ax.tick_params(labelbottom=False)

    axr = fig.add_subplot(gs[1, 0], sharex=ax)
    axr.axhline(0, color='0.6', lw=0.8)
    for lab in (-2, 2):
        axr.axhline(lab, color='0.85', lw=0.6, ls=':')
    axr.plot(LCK, out['lcdm_whitened'], '-', color=C_CTL, lw=1.1, alpha=0.9)
    axr.plot(LCK, out['cr_whitened'], '-', color=C_CR, lw=1.1, alpha=0.9)
    axr.set_xlabel(r'$\ell$')
    axr.set_ylabel(r'whitened residual $[\sigma]$')
    axr.set_ylim(-4.2, 4.2)

    # ---- (b) log in ell from 2, as a ratio ---------------------------------------
    axb = fig.add_subplot(gs[0, 1])
    # the control's low-ell D_l from the same CAMB call the lensing operator came from, so the
    # floor -- which the sweep carries as a RATIO to the flat transfer -- can be shown in D_l
    import camb
    _p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                         mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    _dl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)['total'][:, 0]
    lo_l = out['low_ell'].astype(int)
    base_lo = _dl[lo_l]
    out['low_Dl_ctl'] = base_lo * out['low_ctl']
    out['low_Dl_cr'] = base_lo * out['low_cr']
    axb.plot(LCK, out['lcdm_model'] * FACK, '-', color=C_CTL, lw=1.7, zorder=3)
    axb.plot(LCK, out['cr_model'] * FACK, '-', color=C_CR, lw=1.7, zorder=4)
    axb.errorbar(LCK, DK * FACK, yerr=SIG * FACK, fmt='o', ms=1.8, lw=0.5, color=C_DAT,
                 alpha=0.6, zorder=2)
    axb.plot(lo_l, base_lo, ':', color='0.45', lw=1.4, zorder=3,
             label='no floor (flat transfer)')
    axb.plot(lo_l, out['low_Dl_ctl'], 's--', color=C_CTL, lw=1.3, ms=4.0, zorder=4)
    axb.plot(lo_l, out['low_Dl_cr'], 'o-', color=C_CR, lw=1.8, ms=4.5, zorder=5,
             label=r'the discrete floor, $\ell=2$–$8$')
    axb.fill_between(out['obs_ell'], out['obs_lo'] * _dl[out['obs_ell'].astype(int)],
                     out['obs_hi'] * _dl[out['obs_ell'].astype(int)], color='0.55', alpha=0.30,
                     zorder=1, label=r'observed low-$\ell$ band')
    i4 = int(np.argmin(out['low_cr']))
    axb.annotate(f"minimum at $\\ell={int(lo_l[i4])}$,\nnot at the quadrupole",
                 xy=(lo_l[i4], out['low_Dl_cr'][i4]), xytext=(11.0, 250.0), fontsize=8.5,
                 color=C_CR, arrowprops=dict(arrowstyle='->', color=C_CR, lw=0.9))
    axb.set_xscale('log')
    axb.set_yscale('log')
    axb.set_xlim(1.8, 1910)
    axb.set_ylim(60, 8000)
    axb.set_ylabel(r'$\mathcal{D}_\ell$   $[\mu\mathrm{K}^2]$')
    axb.legend(frameon=False, fontsize=8.5, loc='lower left')
    axb.set_title('(b)  logarithmic from $\\ell=2$: the floor and the peaks in one frame',
                  fontsize=10, loc='left')
    axb.tick_params(labelbottom=False)

    axbr = fig.add_subplot(gs[1, 1], sharex=axb)
    axbr.axhline(0, color='0.6', lw=0.8)
    for lab in (-2, 2):
        axbr.axhline(lab, color='0.85', lw=0.6, ls=':')
    axbr.plot(LCK, out['lcdm_whitened'], '-', color=C_CTL, lw=1.1, alpha=0.9)
    axbr.plot(LCK, out['cr_whitened'], '-', color=C_CR, lw=1.1, alpha=0.9)
    axbr.set_xscale('log')
    axbr.set_xlabel(r'$\ell$')
    axbr.set_ylabel(r'whitened residual $[\sigma]$')
    axbr.set_ylim(-4.2, 4.2)
    axbr.text(0.985, 0.06, 'same residuals as (a), on the log axis', transform=axbr.transAxes,
              ha='right', fontsize=7.5, color='0.45')

    pdf = os.path.join(HERE, 'fig_acoustic_two_arm.pdf')
    fig.savefig(pdf)
    plt.close(fig)
    print(f"  wrote -> corpus/fig_acoustic_two_arm.pdf ({os.path.getsize(pdf)} bytes)")
    print("""
  THE CAPTION, WHICH IS PART OF THE DELIVERABLE:

    Both arms refitted to Planck plik_lite TT on the same bins with the same six-parameter
    freedom, then carried through the same derived lensing operator and binned identically; the
    single remaining amplitude is fitted on the full bandpower covariance.  (a) Linear in ell
    across the acoustic range, in D_l.  (b) The same two arms logarithmic from ell = 2, so the
    discrete closed-S^3 floor sits in the same frame as the peaks; the floor's minimum at ell = 4
    rather than at the quadrupole is the one shape this construction predicts that the standard
    model does not.  The floor is carried by the sweep as a ratio to the flat transfer and is put
    back into D_l against the control's own low-ell spectrum, which is a reconstruction and is
    named as one; the observed low-multipole band is drawn behind it on the same reconstruction.
    Beneath each, whitened residuals for both arms on one axis.  ** The control lands at 1.01 per
    bin and this arm at 1.58: the peak positions and the acoustic comb are right and the SHAPE is
    still rejected, and the lower panels are where that is visible rather than the upper ones. **
""")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
