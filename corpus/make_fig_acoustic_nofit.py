#!/usr/bin/env python3
r"""make_fig_acoustic_nofit.py -- THE CONFRONTATION THE PAPER HAS NEVER CARRIED.

** WHAT THIS IS FOR, AND WHY IT IS A SECOND FIGURE RATHER THAN A PANEL. **  `fig:acoustic` plots both
arms at their REFIT minima -- four parameters given to each arm and the amplitude closed-form.  *That
is the right figure for `freedom does not close the gap`, and it is the wrong one for the question a
reader asks first:* ** what does the comb do on the background the DISTANCES fix, with nothing fitted
to the microwave data at all? **  ⇒ Ordered at `r7183` ⓵ as *"the stronger of the two
confrontations"*, which it is, because the background it is computed on is recoverable from DESI DR2
BAO alone -- `(68.6169, 0.29735)` at `0.958` per degree of freedom, `r7181+cc66.144` -- so scoring
the spectrum against it is out of sample in the strong sense.

  ⌗ *Kept as its own figure because the two confrontations want different y-scales: at `3.0` per bin
  the no-fit arm's residual would flatten the refit panel's structure if they shared an axis.*

** THE TWO THINGS THE EXISTING PANEL DOES NOT DO, BOTH ORDERED. **
  ⓵ ** The residual is binned at the COMB'S OWN PERIOD -- AND FOLDED BY PHASE WITHIN IT, WHICH IS
    THE OPERATION THAT ACTUALLY SHOWS A MODULATION AT THAT PERIOD. **  *`fig:acoustic` plots it raw,
    where a reader sees scatter; the corpus's own finding is that the rejection is MODULATED at the
    acoustic period.*  ⛔ ** But averaging in bins one period wide is precisely the operation that
    CANCELS a modulation whose phase is that period: it integrates each cycle to its own mean. **
    *Measured -- in `l_A`-wide bins the no-fit arm's band means change sign twice across six bands,
    a slow swing rather than a per-period alternation.*  ⇒ *** Folded by phase within the period,
    anchored on the first peak, the same residual carries a single harmonic at `l_A` of amplitude
    `1.373 +- 0.151` -- `9.1` sigma -- against the control's `0.203 +- 0.113`, `1.8` sigma.  Both
    panels are drawn, because the ordered one is what a reader will look for and the fold is what
    answers the question it was ordered for. ***
  ⓶ ** Both confrontations' chi^2 per bin are ON THE FIGURE. **  *So `nothing fitted` and `refitted
    like the standard model` are distinguishable without reading the caption.*

** NO NEW PHYSICS RUN.  EVERY SPECTRUM IS BANKED, AND EACH IS IDENTIFIED BY ITS OWN STORED `D_M`
   RATHER THAN BY ITS FILENAME. **  A bank swapped under this script's feet refuses instead of
   plotting someone else's arm:

     nothing fitted   refit_grid185/lcdm_base.npz          D_M = 13864.6627   (67.40, 0.3150)
                      refit_grid185/cr_base.npz            D_M = 14011.4567   (68.60, 0.2973)
     refitted         spectra/cc66_r185_verify_lcdm.npz    D_M = 13954.3535
                      spectra/cc66_r185_verify_cr.npz      D_M = 14017.0386

** SCORING IS THE EXISTING FIGURE'S, UNCHANGED, SO THE TWO FIGURES ARE COMPARABLE. **  Planck
plik_lite TT with its full covariance, `P15`'s own derived CAMB lensing operator imposed on both arms
alike, the amplitude closed-form at the covariance-weighted optimum, bins `100 <= l <= 1900`.

    python3 corpus/make_fig_acoustic_nofit.py            # writes the PDF and banks the numbers
    python3 corpus/make_fig_acoustic_nofit.py --numbers  # bank and print only, no plot

Built r7183+cc66.145 (node 66, code seat), discharging order ⓵ of the chat seat's `r7183`.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
G185 = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'refit_grid185')
# ⛭ The figure's derived numbers are NOT a banked spectrum and do not belong in a bank:
#   `check_banked_config` scans `spectra/`, `refit_grid/` and `refit_grid185/` and requires a
#   resolved instrument `config` on everything in them.  *This file is a figure's own
#   arithmetic over four spectra; giving it an `ARM` and a `VISLEAF` to satisfy the gate would
#   be writing a provenance it does not have.*  ⇒ It goes in this revision's own directory,
#   which is where the other rounds' working artefacts live.
OUTDIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7183_nofit_figure')
LC, FACB = CS.bin_center_and_fac()
X_DATA, COV = CS.X_DATA, CS.COV_TT

# ** the four spectra, each with the `D_M` its own `.npz` must carry -- the identity check. **
SPECTRA = {
    'nofit_lcdm': (os.path.join(G185, 'lcdm_base.npz'), 13864.6627, 'control, nothing fitted'),
    'nofit_cr': (os.path.join(G185, 'cr_base.npz'), 14011.4567, 'CR arm, nothing fitted'),
    'refit_lcdm': (os.path.join(SP, 'cc66_r185_verify_lcdm.npz'), 13954.3535, 'control, refitted'),
    'refit_cr': (os.path.join(SP, 'cc66_r185_verify_cr.npz'), 14017.0386, 'CR arm, refitted'),
}
L_A = 298.0          # the comb's own period, as the arm's own fit returns it (r6760+cc66.2)


def lensing_ratio():
    """P15's own derived lensing operator, imposed on both arms alike -- the existing figure's."""
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


def load(tag):
    """read a banked spectrum and REFUSE unless its own stored `D_M` identifies it"""
    path, dm_want, _ = SPECTRA[tag]
    if not os.path.exists(path):
        raise SystemExit(f"  ⛔ REFUSED: {os.path.relpath(path, ROOT)} is not banked.  This "
                         f"figure plots banked spectra and does not run the instrument; say which "
                         f"one is missing rather than filling it with a grid.")
    z = np.load(path, allow_pickle=True)
    dm = float(np.atleast_1d(z['D_M'])[0])
    if abs(dm - dm_want) > 0.05:
        raise SystemExit(f"  ⛔ REFUSED: {os.path.relpath(path, ROOT)} carries D_M = {dm:.4f}, "
                         f"not the {dm_want:.4f} this figure's {tag} slot is.  ** A bank whose "
                         f"contents have moved is not a bank this figure may plot under the old "
                         f"label. **  Nothing is written.")
    return z['ls'], z['Dl'], dm


def main(numbers_only=False):
    LG, RATIO = lensing_ratio()

    def binned(ls, Dl):
        return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO))

    RAW = {t: load(t) for t in SPECTRA}
    B = {t: binned(RAW[t][0], RAW[t][1]) for t in SPECTRA}
    KEEP = np.isfinite(B['refit_lcdm']) & (LC >= 100) & (LC <= 1900)
    COVK = COV[np.ix_(KEEP, KEEP)]
    FISH = np.linalg.inv(COVK)
    LINV = np.linalg.inv(np.linalg.cholesky(COVK))
    DK, LCK, SIG = X_DATA[KEEP], LC[KEEP], np.sqrt(np.diag(COV[np.ix_(KEEP, KEEP)]))
    # ⛔ ** D_l, NOT C_l.  `X_DATA` is binned C_l; plotted raw the peaks vanish under the
    #    falling plateau -- `make_fig_acoustic_two_arm.py` carries that warning in its own
    #    source, naming it as the trap the locator hit at `cc66.28`, and this file walked into
    #    it anyway on the first draft.  The factor is applied at every plot call below. **
    FACK = FACB[KEEP]
    NB = int(KEEP.sum())

    out = {'ell': LCK, 'data': DK, 'sigma': SIG, 'nbins': NB, 'l_A': L_A, 'fac': FACK}
    print(f"  {NB} bins, ell {LCK[0]:.0f}-{LCK[-1]:.0f}   (the existing figure's range)")
    for t in SPECTRA:
        mb = B[t][KEEP]
        A = float(mb @ FISH @ DK / (mb @ FISH @ mb))
        res = A * mb - DK
        c2 = float(res @ FISH @ res)
        out.update({f'{t}_A': A, f'{t}_chi2': c2, f'{t}_chi2_per_bin': c2 / NB,
                    f'{t}_model': A * mb, f'{t}_whitened': LINV @ res, f'{t}_D_M': RAW[t][2]})
        print(f"    {SPECTRA[t][2]:26s} chi2 = {c2:8.2f}   {c2 / NB:6.3f} per bin   "
              f"(D_M = {RAW[t][2]:.4f})")
    rn = out['nofit_cr_chi2'] / out['nofit_lcdm_chi2']
    rr = out['refit_cr_chi2'] / out['refit_lcdm_chi2']
    out['ratio_nofit'], out['ratio_refit'] = rn, rr
    print(f"  arm/control:  nothing fitted {rn:.3f}x     refitted {rr:.3f}x")

    # ---- the residual binned at the COMB'S OWN PERIOD -------------------------------------------
    edges = np.arange(100.0, LCK[-1] + L_A, L_A)
    bands, counts = [], []
    for i in range(len(edges) - 1):
        s = (LCK >= edges[i]) & (LCK < edges[i + 1])
        if s.sum() == 0:
            continue
        bands.append((edges[i], edges[i + 1]))
        counts.append(int(s.sum()))
    out['band_lo'] = np.array([b[0] for b in bands])
    out['band_hi'] = np.array([b[1] for b in bands])
    out['band_n'] = np.array(counts)
    print(f"\n  the whitened residual binned at the comb's own period, l_A = {L_A:.0f}:")
    hdr = f"  {'band':>13} {'n':>4} " + "".join(f"{t:>13}" for t in SPECTRA)
    print(hdr)
    for t in SPECTRA:
        w = out[f'{t}_whitened']
        mu, se = [], []
        for (lo, hi) in bands:
            s = (LCK >= lo) & (LCK < hi)
            mu.append(float(w[s].mean()))
            se.append(float(w[s].std(ddof=1) / np.sqrt(s.sum())))
        out[f'{t}_band_mean'] = np.array(mu)
        out[f'{t}_band_sem'] = np.array(se)
    for i, (lo, hi) in enumerate(bands):
        row = f"  {lo:5.0f}-{hi:5.0f} {counts[i]:4d} "
        for t in SPECTRA:
            row += f"{out[f'{t}_band_mean'][i]:+13.4f}"
        print(row)
    _m = out['nofit_cr_band_mean']
    _sgn = int(np.sum(np.diff(np.sign(_m)) != 0))
    out['nofit_cr_band_sign_changes'] = _sgn
    print(f"\n  the no-fit arm's band means change sign {_sgn} time(s) across {len(_m)} bands, "
          f"range {_m.min():+.3f} to {_m.max():+.3f}  -- a slow swing, NOT a per-period alternation")

    # ---- THE FOLD: phase within the comb's period, anchored on the first peak -------------------
    # ** Binning AT the period averages each cycle to its own mean, which cancels a modulation whose
    #    phase IS the period.  The fold is the operation that shows one. **
    PEAK1 = 222.0                       # the arm's own first peak, r6760+cc66.2's run
    out['peak1'] = PEAK1
    ph = ((LCK - PEAK1) % L_A) / L_A
    NPH = 6
    out['phase_centre'] = (np.arange(NPH) + 0.5) / NPH
    DES = np.array([np.cos(2 * np.pi * (LCK - PEAK1) / L_A),
                    np.sin(2 * np.pi * (LCK - PEAK1) / L_A)]).T
    print(f"\n  folded by phase within the period (0 = a peak, 0.5 = a trough), {NPH} phase bins:")
    for t_ in SPECTRA:
        w = out[f'{t_}_whitened']
        mu = np.array([w[(ph >= i / NPH) & (ph < (i + 1) / NPH)].mean() for i in range(NPH)])
        sem = np.array([w[(ph >= i / NPH) & (ph < (i + 1) / NPH)].std(ddof=1)
                        / np.sqrt(((ph >= i / NPH) & (ph < (i + 1) / NPH)).sum())
                        for i in range(NPH)])
        beta = np.linalg.lstsq(DES, w, rcond=None)[0]
        rr = w - DES @ beta
        s2 = float(np.sum(rr ** 2) / (len(w) - 2))
        cv = s2 * np.linalg.inv(DES.T @ DES)
        amp = float(np.hypot(*beta))
        eamp = float(np.sqrt((beta[0] ** 2 * cv[0, 0] + beta[1] ** 2 * cv[1, 1]
                              + 2 * beta[0] * beta[1] * cv[0, 1]) / amp ** 2))
        out[f'{t_}_phase_mean'] = mu
        out[f'{t_}_phase_sem'] = sem
        out[f'{t_}_harm_amp'] = amp
        out[f'{t_}_harm_err'] = eamp
        out[f'{t_}_harm_sigma'] = amp / eamp
        print(f"    {SPECTRA[t_][2]:26s} " + " ".join(f"{m:+.3f}" for m in mu)
              + f"   |  one harmonic at l_A: {amp:.4f} +- {eamp:.4f}  ({amp / eamp:.2f} sigma)")

    os.makedirs(OUTDIR, exist_ok=True)
    np.savez(os.path.join(OUTDIR, 'nofit_figure_numbers.npz'), **out)
    print(f"  banked -> {os.path.relpath(OUTDIR, ROOT)}/nofit_figure_numbers.npz")
    if numbers_only:
        return 0

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(11.6, 8.3))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.95, 1.0], width_ratios=[1.62, 1.0],
                          hspace=0.33, wspace=0.26)

    ax = fig.add_subplot(gs[0, :])
    FK = out['fac']
    ax.errorbar(LCK, DK * FK, yerr=SIG * FK, fmt='o', ms=2.1, lw=0.7, color='0.35', alpha=0.75,
                label='Planck TT bandpowers', zorder=2)
    ax.plot(LCK, out['nofit_lcdm_model'] * FK, '-', lw=1.9, color='#1f77b4', zorder=4,
            label=r'control, nothing fitted  ($\chi^2/\mathrm{bin}=%.2f$)' % out['nofit_lcdm_chi2_per_bin'])
    ax.plot(LCK, out['nofit_cr_model'] * FK, '-', lw=1.9, color='#d62728', zorder=5,
            label=r'CR arm, nothing fitted  ($\chi^2/\mathrm{bin}=%.2f$)' % out['nofit_cr_chi2_per_bin'])
    ax.plot(LCK, out['refit_lcdm_model'] * FK, '--', lw=1.1, color='#1f77b4', alpha=0.6, zorder=3,
            label=r'control, refitted  ($%.2f$)' % out['refit_lcdm_chi2_per_bin'])
    ax.plot(LCK, out['refit_cr_model'] * FK, '--', lw=1.1, color='#d62728', alpha=0.6, zorder=3,
            label=r'CR arm, refitted  ($%.2f$)' % out['refit_cr_chi2_per_bin'])
    ax.set_ylabel(r'$\mathcal{D}_\ell=\ell(\ell+1)C_\ell/2\pi$   $[\mu\mathrm{K}^2]$')
    ax.set_xlim(LCK[0] - 20, LCK[-1] + 20)
    ax.legend(loc='upper right', fontsize=8.4, framealpha=0.92)
    ax.set_title('The comb on the background the distances fix, with nothing fitted to the '
                 'microwave data', fontsize=10.6)
    ax.text(0.013, 0.035,
            'background from DESI DR2 BAO alone: $(68.62,\\,0.2974)$ at $0.958$/dof\n'
            f'{NB} bins, $100\\leq\\ell\\leq1900$; amplitude closed-form, four parameters free only '
            'in the dashed curves',
            transform=ax.transAxes, fontsize=7.6, va='bottom', color='0.3')

    axb = fig.add_subplot(gs[1, 0])
    ctr = 0.5 * (out['band_lo'] + out['band_hi'])
    wbar = 0.115 * L_A          # four bars must fit INSIDE one band, not straddle its edges
    for j, (t, col, lab) in enumerate((
            ('nofit_cr', '#d62728', 'CR arm, nothing fitted'),
            ('refit_cr', '#ff9896', 'CR arm, refitted'),
            ('nofit_lcdm', '#1f77b4', 'control, nothing fitted'),
            ('refit_lcdm', '#aec7e8', 'control, refitted'))):
        axb.bar(ctr + (j - 1.5) * wbar, out[f'{t}_band_mean'], width=wbar * 0.92,
                yerr=out[f'{t}_band_sem'], color=col, ecolor='0.35', capsize=1.8,
                error_kw=dict(lw=0.7), label=lab, zorder=3)
    axb.axhline(0.0, color='0.2', lw=0.8, zorder=4)
    for e in out['band_lo'][1:]:
        axb.axvline(e, color='0.85', lw=0.6, zorder=1)
    axb.set_xlabel(r'multipole $\ell$')
    axb.set_ylabel('whitened residual,\nband mean')
    axb.set_xlim(LCK[0] - 20, LCK[-1] + 20)
    axb.set_ylim(min(-1.25, 1.18 * min(out[f'{k}_band_mean'].min() for k in SPECTRA)),
                 1.62 * max(out[f'{k}_band_mean'].max() for k in SPECTRA))
    axb.legend(loc='upper center', fontsize=7.0, ncol=2, framealpha=0.93, borderpad=0.35)
    axb.set_title(r"binned AT the period $\ell_A=%.0f$ -- a slow swing, because averaging"
                  "\n"
                  r"over one cycle cancels a modulation whose phase IS that cycle" % L_A,
                  fontsize=8.8)

    # ---- the fold: the panel that actually shows a modulation AT the period --------------------
    axf = fig.add_subplot(gs[1, 1])
    pc = out['phase_centre']
    for t_, col, mk, lab in (('nofit_cr', '#d62728', 'o', 'CR arm, nothing fitted'),
                             ('refit_cr', '#ff9896', 's', 'CR arm, refitted'),
                             ('nofit_lcdm', '#1f77b4', '^', 'control, nothing fitted'),
                             ('refit_lcdm', '#aec7e8', 'v', 'control, refitted')):
        axf.errorbar(pc, out[f'{t_}_phase_mean'], yerr=out[f'{t_}_phase_sem'], fmt=mk + '-',
                     ms=4.0, lw=1.3, color=col, ecolor=col, capsize=2.0,
                     label=f"{lab}  (${out[f'{t_}_harm_sigma']:.1f}\sigma$)", zorder=3)
    axf.axhline(0.0, color='0.2', lw=0.8, zorder=4)
    axf.set_xlabel(r'phase within the comb period' '\n' r'($0=$ a peak, $0.5=$ a trough)', fontsize=9)
    axf.set_ylabel('whitened residual,\nphase-bin mean')
    axf.set_xlim(0.0, 1.0)
    axf.legend(loc='lower left', fontsize=7.2, framealpha=0.92)
    axf.set_title(r'FOLDED by phase within $\ell_A$ -- one harmonic at $\ell_A$:'
                  '\n'
                  r'arm $%.2f\pm%.2f$ ($%.1f\sigma$) against control $%.2f\pm%.2f$ ($%.1f\sigma$)'
                  % (out['nofit_cr_harm_amp'], out['nofit_cr_harm_err'],
                     out['nofit_cr_harm_sigma'], out['nofit_lcdm_harm_amp'],
                     out['nofit_lcdm_harm_err'], out['nofit_lcdm_harm_sigma']), fontsize=8.8)

    pdf = os.path.join(HERE, 'fig_acoustic_nofit.pdf')
    fig.savefig(pdf, bbox_inches='tight')
    print(f"  wrote -> {os.path.relpath(pdf, ROOT)}")
    return 0


if __name__ == '__main__':
    sys.exit(main(numbers_only='--numbers' in sys.argv))
