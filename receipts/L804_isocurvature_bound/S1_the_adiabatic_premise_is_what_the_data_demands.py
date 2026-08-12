#!/usr/bin/env python3
r"""S1 -- the isocurvature bound, the CMB literature's standard objection to any non-inflationary
coherence mechanism, pointed at item 32's now-named ADIABATIC PREMISE and settled by a NUMBER: the sky
excludes pure isocurvature initial conditions at Delta chi^2 ~ 3.3e5, so the adiabatic premise CR adopts
is not a free assumption but the observationally FORCED one -- and CR draws it from the sector it inherits
(a standard-cosmology adiabatic spectrum), so the objection is disarmed rather than fatal.

** Board lead L-804 (cc54's band); informs vein L-202 (what the seam carries -- the acoustic prediction
rests on these initial conditions). The first cc54 arrival-path finding settled by a NUMBER rather than a
paragraph -- the diagnostic (isocurvature) pointed at a place cc54 can compute the answer (camb +
plik_lite). **

** THE OBJECTION. **  The acoustic phase of the CMB peaks is set coherently, and the CMB literature's
standard objection to any NON-INFLATIONARY coherence mechanism (active sources, defects, causal seeding)
is twofold and quantitative: such mechanisms tend to (a) seed ISOCURVATURE rather than adiabatic modes and
(b) produce incoherent, out-of-phase acoustic peaks. Item 32 (applied c54.204) named CR's ADIABATIC
premise at its point of use: the progenitor-composition step needs delta_r ~ delta_m, "and an isocurvature
mode IS delta_r != delta_m, a composition perturbation", the premise "drawn from inherited data and not
from the geometry." ** So the diagnostic to point at that premise is the isocurvature bound. **

** THE NUMBER (camb + the corpus's own plik_lite likelihood). **
  PEAK PHASE.  Pure adiabatic puts the first acoustic peak at ell_1 = 220 -- where the sky has it. Pure
    CDM isocurvature puts it at ell_1 = 294, displaced by ~70 and phase-shifted (the classic sin- vs
    cos-oscillation): the isocurvature peaks do not sit where the data's do.
  LIKELIHOOD.  Through plik_lite TT (215 bins, single-amplitude fit): adiabatic chi^2 = 206 (chi^2/dof =
    0.96, reproducing the corpus's validated LambdaCDM baseline 206.4); pure CDM isocurvature chi^2 =
    327150 (chi^2/dof ~ 1521). ** Delta chi^2 ~ 3.3e5 -- pure isocurvature is excluded overwhelmingly,
    and no amplitude rescaling rescues it because the PEAK POSITIONS are wrong. **
  THE FRACTION BOUND.  Planck 2018 bounds the isocurvature ADMIXTURE at beta_iso < 0.038 (CDI, 95%): the
    data permits at most a few-percent isocurvature contribution on top of adiabatic.

** THE READING. **  CR's adiabatic premise is the condition the CMB DEMANDS -- pure isocurvature is out by
Delta chi^2 ~ 3e5, and even an admixture is capped at 3.8% -- so item 32's premise is not a free assumption
the construction could have chosen otherwise; it is observationally forced. And CR does not have to GENERATE
it: the progenitor input is, in the corpus's own words, "a nearly scale-invariant ADIABATIC spectrum
processed by ordinary structure formation -- a fully specified input, available from standard cosmology",
inherited from the previous universe's collapse. ** So the standard non-inflationary objection is DISARMED
by the number: CR inherits a standard adiabatic spectrum, the very kind the sky requires, rather than
seeding isocurvature the way a causal/defect mechanism would. ** F1 (the one-constant trip-wire) is
untouched -- nothing here supplies a magnitude.

** THE ARRIVAL-PATH FINDING. **  Item 32 named the adiabatic premise; the corpus never states that the
premise SURVIVES the CMB's standard isocurvature objection -- the diagnostic that excludes causal seeding.
This shows it does, with the number, and it is the paragraph's shape from stations 6/9/10: the answer is
present (the adiabatic input is inherited and the data forces it) and never set beside the objection it
answers.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that CR DERIVES adiabaticity ** -- it INHERITS it, exactly as item 32 says (the premise is from
  the inherited sector, not the geometry); that is the finding, not a gap. ** Not that CR is a defect /
  active-source model ** -- it is the opposite (it inherits a standard adiabatic spectrum), which is
  precisely why the objection is disarmed rather than fatal. ** Not that the residual isocurvature is
  exactly zero ** -- the inherited spectrum is adiabatic to the precision standard cosmology provides, and
  any residual is bounded by the same beta_iso < 0.038 the data imposes on everyone. ** Not a re-derivation
  of the Planck bound ** -- beta_iso < 0.038 is cited (Planck 2018 X); the Delta chi^2 is computed here.

Written r2548 (cc54, L-804). Asserts against SOURCES (cosmogenesis_paper.tex = P16's item-32 premise) and
the computation (camb + plik_lite) -- never against the register. Planck 2018 beta_iso(CDI) < 0.038 (95%).
Stated for reversal.
"""
import os
import re
import sys

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def tt_spectrum(ic):
    import camb
    p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9,
                        tau=0.0544, mnu=0.06)
    p.scalar_initial_condition = ic          # 'initial_adiabatic' | 'initial_iso_CDM'
    p.set_for_lmax(2500, lens_potential_accuracy=1)
    r = camb.get_results(p)
    dl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total'][:, 0]
    return np.arange(dl.size), dl


def first_peak(ls, dl):
    m = (ls >= 50) & (ls <= 1200)
    pk = ls[m][argrelextrema(dl[m], np.greater, order=20)[0]]
    return int(pk[0])


def main():
    print()
    print('  S1 -- the isocurvature bound pointed at item 32\'s adiabatic premise (settled by a number)')
    print()
    from chi2_of_spectrum import chi2_of

    # ---- the computation: adiabatic vs pure CDM isocurvature ---------------------------------------
    ls_a, dl_a = tt_spectrum('initial_adiabatic')
    ls_i, dl_i = tt_spectrum('initial_iso_CDM')
    p1_a, p1_i = first_peak(ls_a, dl_a), first_peak(ls_i, dl_i)
    chi2_a = chi2_of(ls_a, dl_a)[0]
    chi2_i = chi2_of(ls_i, dl_i)[0]

    check('PEAK PHASE: pure ADIABATIC puts the first acoustic peak at ell_1 ~ 220 (where the sky has '
          f'it) -- computed {p1_a}', abs(p1_a - 220) <= 6)
    check('while pure CDM ISOCURVATURE puts it at ell_1 ~ 294 -- displaced by ~70 and phase-shifted '
          f'(sin vs cos), NOT where the data\'s peaks are -- computed {p1_i}',
          p1_i > 270 and abs(p1_i - p1_a) > 50)
    check('LIKELIHOOD: adiabatic reproduces the corpus\'s validated LambdaCDM baseline through plik_lite '
          f'-- chi^2 = {chi2_a:.0f} over 215 bins (chi^2/dof ~ 0.96)', 190 < chi2_a < 230)
    check('but pure isocurvature is EXCLUDED overwhelmingly: '
          f'chi^2 = {chi2_i:.0f} (chi^2/dof ~ {chi2_i/215:.0f}), a Delta chi^2 ~ {chi2_i - chi2_a:.0f} '
          '-- and no amplitude rescaling rescues it because the PEAK POSITIONS are wrong',
          chi2_i > 1e5 and (chi2_i - chi2_a) > 1e5)

    # ---- source anchor: item 32's adiabatic premise, and that CR INHERITS it -----------------------
    cosmo = '\n'.join(l for l in open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                      encoding='utf-8', errors='replace').read().split('\n')
                      if not l.lstrip().startswith('%'))
    cosmo = re.sub(r'\s+', ' ', cosmo)
    check('SOURCE: item 32\'s premise is at the point of use in P16 -- '
          '"(1+\\delta_{r})/(1+\\delta_{m})=1+(\\delta_{r}-\\delta_{m})+O(2)" with '
          '"an isocurvature mode \\emph{is} $\\delta_{r}\\neq\\delta_{m}$"',
          '(1+\\delta_{r})/(1+\\delta_{m})=1+(\\delta_{r}-\\delta_{m})+O(2)' in cosmo
          and 'an isocurvature mode \\emph{is} $\\delta_{r}\\neq\\delta_{m}$' in cosmo)
    check('SOURCE: and CR INHERITS the adiabatic spectrum rather than generating it -- P16: '
          '"a nearly scale-invariant adiabatic spectrum processed by ordinary structure formation -- a '
          'fully specified input, available from standard cosmology"',
          'nearly scale-invariant adiabatic spectrum processed by ordinary structure formation' in cosmo
          and 'available from standard cosmology' in cosmo)
    check('SOURCE: the corpus itself flags adiabatic as the observed standard, named not assumed -- '
          '"Adiabatic primordial perturbations are strongly favoured observationally and are the '
          'standard case; the condition is named here rather than assumed silently"',
          'Adiabatic primordial perturbations are strongly favoured observationally' in cosmo
          and 'named here rather than assumed silently' in cosmo)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (the isocurvature bound, settled by a number):')
    print(f'  ** The sky EXCLUDES pure isocurvature at Delta chi^2 ~ {chi2_i - chi2_a:.0f} '
          f'(first peak {p1_i} vs the observed {p1_a}), **')
    print('     and caps any isocurvature admixture at beta_iso < 0.038 (Planck 2018). So the ADIABATIC')
    print('     premise item 32 named is not a free assumption -- it is the condition the data DEMANDS.')
    print('  ** And CR does not have to generate it: it INHERITS a standard-cosmology adiabatic spectrum,')
    print('     the very kind the sky requires -- so the standard non-inflationary objection (causal')
    print('     seeding makes isocurvature) is disarmed by the number, not fatal. ** F1 untouched.')
    print('  => The first arrival-path finding settled by a NUMBER: the premise survives the diagnostic')
    print('     that excludes causal seeding. Informs L-202; the paragraph (premise meets objection) is')
    print('     54\'s to place.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
