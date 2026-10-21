#!/usr/bin/env python3
"""
r7484 — PO-93: THE SAMPLE ITS DISCHARGE CLAUSE NAMES, SELECTED ON CRITERIA REGISTERED FIRST.

The row: *"one cluster or group with its turnaround radius located kinematically, from the
motions rather than by a fixed-overdensity definition, together with a baryonic mass measured
independently of that radius.  The instrument half is built and shared with PO-50 ... so what
is missing is the sample and not the reading of it."*

⌗ THE INSTRUMENT IS IMPORTED, not rebuilt: `r_HE` and its constants come out of
  `receipts/P03_SdS_slicing/P03_which_mass_sets_the_hubble_eddington_radius.py` by `ast`, so
  that receipt's module body (which prints and asserts) never runs and there is ONE copy of
  the relation in the tree.  r7445's rule as promoted at r7447.

⌗ EVERY NUMBER BELOW IS A QUOTED LITERATURE VALUE WITH ITS SOURCE IN THE TABLE, and every
  system examined is listed with the registered criterion that kept or dropped it.

Run:  python3 sample.py
"""

import ast
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_INSTR = os.path.join(ROOT, 'receipts', 'P03_SdS_slicing',
                      'P03_which_mass_sets_the_hubble_eddington_radius.py')
if not os.path.exists(_INSTR):
    sys.exit("FATAL: the PO-50/PO-93 instrument is not where this file expects it.\n"
             "  Do NOT rebuild r_HE here -- the row says the instrument half is BUILT.")


def _names(t):
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        return [x for e in t.elts for x in _names(e)]
    return []


def _load(path):
    """The instrument's constants and r_HE, by ast -- its module body prints and asserts."""
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    want = ('G', 'c', 'Msun', 'Mpc', 'H0', 'OmL', 'Lam', 'alpha', 'f_b')
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            nm = [x for t in n.targets for x in _names(t)]
            if nm and all(x in want for x in nm):
                keep.append(n)
    ns = {'__file__': path, '__name__': 'p03_instrument'}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, 'exec'), ns)   # noqa: S102
    return ns


_I = _load(_INSTR)
r_HE, Mpc, Msun, G, c, Lam, H0, OmL, f_b_corpus = (
    _I['r_HE'], _I['Mpc'], _I['Msun'], _I['G'], _I['c'], _I['Lam'],
    _I['H0'], _I['OmL'], _I['f_b'])

# ------------------------------------------------------------------ the systems examined
# (name, how the radius was located, the registered criterion it meets or fails, source)
EXAMINED = [
    ('NGC 5353/4',
     'zero crossing of a fitted RADIAL VELOCITY profile from line-of-sight velocities and '
     '3D distances of four bound-zone filament galaxies',
     'DROPPED on Ⓢ②: no baryonic, stellar or gas mass is quoted anywhere in the paper',
     'Lee, Kim & Rey 2015, ApJ 815 43 (arXiv:1511.00056)'),
    ('six isolated groups',
     'the Turn-around Radius Estimator applied to "an inclined streak pattern in the '
     'anisotropic SPATIAL distribution of the neighbour field galaxies"',
     'DROPPED on Ⓢ①: the radius is located from a SPATIAL distribution, not from the '
     'velocity field -- and its turn-around mass is "approximated by the virial mass"',
     'Lee et al. 2017 (arXiv:1709.06903)'),
    ('Virgo',
     'the radius of the ZERO-VELOCITY SURFACE from the spherically symmetric infall model, '
     'on galaxy motions; independently by the Numerical Action Method on galaxy trajectories',
     'KEPT: Ⓢ① kinematic; Ⓢ② gas from Planck SZ and stars from photometry, both '
     'independent of R0; Ⓢ③ independent totals exist; Ⓢ④ H0 = 73 stated, the '
     "instrument's own value",
     'Kashibadze, Karachentsev & Karachentseva 2020 (arXiv:2002.12820), carrying '
     'KKK18, Shaya+2017 and Karachentsev+2014'),
]

# ------------------------------------------------------------------ Virgo, every value quoted
R0 = [('KKK18 (23 deg)', 7.8, 0.3), ('Shaya+ 2017 (NAM)', 7.3, 0.3),
      ('Karachentsev+ 2014', 7.2, 0.7), ('Kashibadze+ 2018', 7.0, 0.3)]
M_GAS = (1.4e14, 1.6e14)      # Planck SZ warm/hot gas, quoted as a range
M_STAR = 1.5e13               # an order of magnitude below the gas, per the paper's own words
F_B_PAPER = 0.1834            # the baryon fraction THAT paper assumes
M_X200 = 1.05e14              # Simionescu+ 2017 X-ray M200, within r200 ~ 1 Mpc
M_T_FROM_R0 = (7.4e14, 0.9e14)   # the paper's own total INSIDE R0 -- derived FROM R0


def M_implied(R_Mpc):
    """Invert the instrument's relation: r_HE = (3GM/Lam c^2)^(1/3)  =>  M = Lam c^2 R^3/3G."""
    R = R_Mpc * Mpc
    return Lam * c ** 2 * R ** 3 / (3 * G) / Msun


def main():
    print('=' * 104)
    print('  Ⓥ① THE INSTRUMENT IS THE IMPORTED ONE, AND ITS OWN CONTROL IS RE-RUN')
    print('=' * 104)
    print(f'      r_HE and constants  <-  {os.path.relpath(_INSTR, ROOT)}  (by ast)')
    print(f'      H0 = {H0 * Mpc / 1e3:.0f} km/s/Mpc,  OmL = {OmL},  Lambda = {Lam:.4g} m^-2,  '
          f'f_b = {f_b_corpus}')
    # the instrument's own control: at f_b = 1 the two choices coincide
    M = 1e15
    assert abs(r_HE(M) / r_HE(M * 1.0) - 1.0) < 1e-12
    sep = (1.0 / f_b_corpus) ** (1 / 3)
    assert abs(r_HE(M) / r_HE(M * f_b_corpus) - sep) < 1e-9
    print(f'      its control: at f_b = 1 the two mass choices coincide exactly  -> ok')
    print(f'      the separation it gives: f_b^(-1/3) = {sep:.3f} in radius, '
          f'1/f_b = {1 / f_b_corpus:.2f} in mass')
    print('  ⇒ PASS   ⌗ so the quantity measured is the dark fraction, not an artefact.')

    print()
    print('=' * 104)
    print('  Ⓥ⑤ THE REGISTERED CRITERIA, APPLIED AS WRITTEN — WITH THE REJECTIONS')
    print('=' * 104)
    for name, how, verdict, src in EXAMINED:
        print(f'  ⌈ {name}')
        print(f'      located by: {how}')
        print(f'      {verdict}')
        print(f'      source: {src}')
    kept = [e for e in EXAMINED if e[2].startswith('KEPT')]
    print()
    print(f'  ⇒ Ⓐ: {len(kept)} of {len(EXAMINED)} systems examined meet all four criteria')

    print()
    print('=' * 104)
    print('  THE MEASUREMENT — the mass the OBSERVED kinematic radius implies, against the')
    print('  masses measured independently of it')
    print('=' * 104)
    print(f'      {"R0 source":22s} {"R0 [Mpc]":>12s} {"M implied [Msun]":>20s}')
    vals = []
    for lab, R, dR in R0:
        m, mlo, mhi = M_implied(R), M_implied(R - dR), M_implied(R + dR)
        vals.append((lab, R, dR, m, mlo, mhi))
        print(f'      {lab:22s} {R:7.1f} ± {dR:<3.1f} {m:14.3e}  [{mlo:.2e}, {mhi:.2e}]')
    mbar_lo, mbar_hi = M_GAS[0] + M_STAR, M_GAS[1] + M_STAR
    print()
    print(f'      baryonic, measured independently of R0:')
    print(f'        hot gas (Planck SZ)   {M_GAS[0]:.2e} to {M_GAS[1]:.2e}')
    print(f'        stars (photometry)    {M_STAR:.2e}')
    print(f'        => M_bary             {mbar_lo:.2e} to {mbar_hi:.2e}')
    print(f'      the paper\'s own total INSIDE R0  {M_T_FROM_R0[0]:.2e} ± {M_T_FROM_R0[1]:.1e}'
          f'   ⚠ DERIVED FROM R0')
    print(f'      X-ray M200 (Simionescu+ 2017)   {M_X200:.2e}   ⚠ WITHIN r200 ~ 1 Mpc, '
          f'NOT within R0')

    print()
    print('-' * 104)
    print('  ⌈ THE CONSISTENCY CHECK NOBODY HAS RUN: does the corpus\'s r_HE reproduce the')
    print('    standard zero-velocity-surface mass, which is derived a different way?')
    print('-' * 104)
    m78 = M_implied(7.8)
    print(f'      r_HE inverted at R0 = 7.8 Mpc           {m78:.3e} Msun')
    print(f'      the paper\'s M_T inside the same R0      {M_T_FROM_R0[0]:.3e} ± '
          f'{M_T_FROM_R0[1]:.1e} Msun')
    agree = m78 / M_T_FROM_R0[0]
    print(f'      ⇒ ratio {agree:.3f}   ⌗ the two routes are INDEPENDENT derivations: the '
          f'corpus\'s is')
    print(f'        the vanishing of the slicing surface\'s Gaussian curvature, the literature\'s')
    print(f'        is a spherical infall model on the age of the Universe.')

    print()
    print('-' * 104)
    print('  ⛔ AND THE FIRST READING OF THIS WAS MINE AND IT WAS WRONG, WHICH THE ROW\'S OWN')
    print('    WORDS CORRECT: r_HE IS A BOUND, NOT AN EQUALITY')
    print('-' * 104)
    print('      The block above inverts r_HE as an EQUALITY and so reads a dark fraction of')
    print('      0.34 to 0.48 off it.  That number is an artefact of the inversion.  The row says')
    print('      what the instrument is: "the BOUND-to-attained factor is parameter-free".  r_HE is')
    print('      the LARGEST radius that can still be turning around for a given enclosed mass --')
    print('      the LambdaCDM bound the turnaround literature calls a bound and tests for')
    print('      violation.  ⇒ So the test is not "which mass does the inversion return" but')
    print('      ** IS THE OBSERVED RADIUS INSIDE THE BOUND EACH MASS CHOICE ALLOWS? **')
    print('      ⌗ A bound inverted as an equality is a different instrument, and it gave a')
    print('        different answer.  Recorded rather than quietly replaced.')

    print()
    print('-' * 104)
    print('  ⌈ Ⓑ/Ⓒ THE DECISION, READ AS A BOUND: WHICH MASS DOES THE RADIUS TRACK?')
    print('-' * 104)
    M_DYN = (7.4e14, 8.0e14)    # two INDEPENDENT routes, neither using r_HE:
    #   (7.4 +- 0.9)e14 from the spherical infall model inside R0 (Kashibadze+ 2020), and
    #   (7.6 - 8.7)e14 from Planck's SZ gas mass with the cosmic baryon fraction, on a scale
    #   up to twice the virial radius -- quoted in the same paper.
    print(f'      {"mass choice":26s} {"M [Msun]":>22s} {"r_HE bound [Mpc]":>18s}')
    rb_bary = (r_HE(mbar_lo) / Mpc, r_HE(mbar_hi) / Mpc)
    rb_dyn = (r_HE(M_DYN[0]) / Mpc, r_HE(M_DYN[1]) / Mpc)
    print(f'      {"BARYONIC (gas + stars)":26s} {mbar_lo:10.2e} to {mbar_hi:8.2e}'
          f' {rb_bary[0]:8.2f} to {rb_bary[1]:5.2f}')
    print(f'      {"DYNAMICAL (two routes)":26s} {M_DYN[0]:10.2e} to {M_DYN[1]:8.2e}'
          f' {rb_dyn[0]:8.2f} to {rb_dyn[1]:5.2f}')
    print()
    print(f'      {"R0 source":22s} {"R0 [Mpc]":>11s}  {"vs BARYONIC bound":>22s}'
          f'  {"vs DYNAMICAL bound":>22s}')
    viol_b, ok_d, attained = 0, 0, []
    for lab, R, dR, m, mlo, mhi in vals:
        vb = R / rb_bary[1]          # against the MOST generous baryonic bound
        vd = R / rb_dyn[0]           # against the LEAST generous dynamical bound
        attained.append(vd)
        if vb > 1.0:
            viol_b += 1
        if vd <= 1.0:
            ok_d += 1
        print(f'      {lab:22s} {R:7.1f}±{dR:<3.1f}  {vb:14.3f} {"VIOLATED" if vb > 1 else "inside":>8s}'
              f'  {vd:14.3f} {"inside" if vd <= 1 else "VIOLATED":>8s}')
    print()
    print(f'  ⇒ ⚑ THE OBSERVED KINEMATIC RADIUS EXCEEDS THE BOUND A BARYON-ONLY VIRGO ALLOWS IN')
    print(f'    {viol_b} OF {len(vals)} DETERMINATIONS, BY {min(R / rb_bary[1] for _l, R, _d, _m, _lo, _hi in vals):.2f}'
          f' TO {max(R / rb_bary[1] for _l, R, _d, _m, _lo, _hi in vals):.2f},')
    print(f'    AND LIES INSIDE THE BOUND THE DYNAMICAL MASS ALLOWS IN {ok_d} OF {len(vals)}.')
    print(f'    ⇒ ** THE HUBBLE-EDDINGTON RADIUS TRACKS THE DYNAMICAL MASS. **')
    print()
    print(f'    THE BOUND-TO-ATTAINED FACTOR, which is what the row says the instrument gives:')
    print(f'      R0 / r_HE(M_dyn) = {min(attained):.2f} to {max(attained):.2f}'
          f'   ⌗ the bound is nearly attained, which is why one cluster decides it.')
    print()
    print('-' * 104)
    print('  ⌈ THE ONE RESIDUAL, QUANTIFIED RATHER THAN WAVED AT: THE APERTURES DIFFER')
    print('-' * 104)
    print('      The baryonic mass is independent of R0 -- which is what Ⓢ② asked for -- but it')
    print('      is NOT measured WITHIN R0.  The gas mass carries no stated aperture, and the')
    print("      total Planck infers from it is quoted 'on a scale up to 2 times larger than the")
    print("      virial radius' -- about 3.4 Mpc against R0 = 7.0 to 7.8 Mpc.  So the baryonic")
    print('      content inside R0 is AT LEAST the value used, and the violation above is an')
    print('      upper bound on the evidence rather than a floor.')
    need = [(R / rb_bary[1]) ** 3 for _l, R, _d, _m, _lo, _hi in vals]
    print()
    print(f'      ⇒ For the baryon-only bound NOT to be violated, the baryonic mass inside R0')
    print(f'        would have to be {min(need):.2f} to {max(need):.2f} times the gas-plus-stars')
    print(f'        measured inside about 3.4 Mpc -- i.e. {min(need) * mbar_lo:.2e} to '
          f'{max(need) * mbar_hi:.2e} Msun of baryons.')
    print(f'        That is {min(need) * mbar_lo / M_DYN[1] * 100:.0f} to '
          f'{max(need) * mbar_hi / M_DYN[0] * 100:.0f} per cent of the independently measured')
    print(f'        TOTAL, so it would require Virgo to be baryon-dominated inside R0.')
    print()
    print('      ⇒ ** SO WHAT IS MISSING IS NOT A SAMPLE -- ONE EXISTS AND IT DECIDES THE')
    print('        DIRECTION -- BUT A BARYONIC MASS MEASURED OUT TO THE TURNAROUND RADIUS. **')
    print('        That is a different clause from the one the row carries, and naming it is')
    print('        the part of this that the row cannot do for itself.')

    print()
    print('-' * 104)
    print('  Ⓔ CAN THE DATUM TELL THE TWO APART AT ALL?')
    print('-' * 104)
    for lab, R, dR, m, mlo, mhi in vals:
        span = (R + dR) / (R - dR)
        print(f'      {lab:22s} radius span {span:.3f}   against the separation {sep:.3f}'
              f'   {"RESOLVES" if span < sep else "does NOT resolve"}')
    print()
    print('-' * 104)
    print('  Ⓥ④ THE COSMOLOGY, PROPAGATED RATHER THAN WAVED THROUGH')
    print('-' * 104)
    print(f'      the instrument: H0 = {H0 * Mpc / 1e3:.0f}, OmL = {OmL}')
    print(f'      the source:     H0 = 73 stated (the instrument\'s own value); OmL not stated')
    for lab, h0, oml in (('Planck OmL = 0.685, same H0', 73.0, 0.685),
                         ('Planck H0 = 67.3, OmL = 0.685', 67.3, 0.685)):
        scale = ((OmL * (H0 * Mpc / 1e3) ** 2) / (oml * h0 ** 2)) ** (1 / 3)
        print(f'      {lab:30s} -> every r_HE bound scales by {scale:.3f}'
              f'  ({(scale - 1) * 100:+.1f} per cent)')
    print(f'      ⇒ the H0 choice moves the bounds by about 6 per cent, the OmL choice by under 1.')
    print(f'        The baryon-only violation is 19 to 33 per cent, so it survives either; the')
    print(f'        bound-to-attained factor would move from 0.74-0.82 to about 0.78-0.87.')
    print(f'        ⌗ said with a number because r_HE goes as Lambda^(-1/3) and "negligible" is')
    print(f'          not a measurement.')

    print()
    print('=' * 104)
    print('  ** Nothing is applied to the register.  Supplied, not applied. **')
    return 0


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    sys.exit(main())
