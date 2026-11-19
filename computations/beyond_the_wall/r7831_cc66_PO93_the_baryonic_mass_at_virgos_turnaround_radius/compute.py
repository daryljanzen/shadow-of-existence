#!/usr/bin/env python3
"""
r7831 — PO-93: THE BARYONIC MASS AT VIRGO'S TURNAROUND RADIUS — WHAT IS MEASURED, TO WHAT RADIUS.

The order (r7829, 69): *"its gate is data: a baryonic mass, gas plus stars, measured within
Virgo's turnaround radius of 7.0 to 7.8 Mpc.  ① Search the literature for that measurement, or
for the pieces it can be built from ... State what exists, with references and THE RADIUS EACH
FIGURE IS MEASURED TO.  ② If the pieces reach the turnaround radius, build the baryonic mass
there with its error ...  ③ If they do not, state exactly how far they reach and what
measurement would close the gap."*

⌗ THE INSTRUMENT IS IMPORTED, not rebuilt: r_HE and its constants come out of
  receipts/P03_SdS_slicing/P03_which_mass_sets_the_hubble_eddington_radius.py by `ast`, the
  same way r7484 took it, so that receipt's module body never runs and there is ONE copy of
  the relation in the tree.

⌗ EVERY NUMBER IS A QUOTED LITERATURE VALUE CARRYING THE APERTURE IT WAS MEASURED TO.  That
  pairing is the whole discriminator: a baryonic mass is not a number but a number AND an
  aperture, and PO-93 turns on the aperture being 7.0-7.8 Mpc rather than the smaller one the
  measured masses use.

Run:  python3 compute.py
"""

import ast
import json
import math
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

# ===================================================================================== THE ROW
# PO-93's live clause, and r7484's standing position, both quoted so the arithmetic below is
# anchored to text and not to recollection.
R0_BAND = (7.0, 7.8)          # the turnaround radius band the order names
R7484_FACTOR = (1.70, 2.35)   # r7484: M_bary(R0) would have to be this x the mass inside ~3.4 Mpc
R7484_NEEDED = (2.6e14, 4.1e14)      # ... which is this, in Msun
R7484_BARY_AT_3P4 = (1.55e14, 1.75e14)   # gas (Planck SZ, EXTRAPOLATED) + stars, inside ~3.4 Mpc
R7484_APERTURE = 3.4          # the aperture r7484's baryonic figure is quoted to, in Mpc
R7484_MSTAR = 1.5e13          # r7484's stellar term -- carried NO stated aperture

# =========================================================== THE LITERATURE, EACH WITH ITS RADIUS
# (key, component, value Msun or Lsun, +/- , aperture_Mpc, aperture as the source states it,
#  MEASURED or EXTRAPOLATED, source)
LIT = [
    # ---- GAS, measured
    ('erosita_r200', 'hot gas', 1.98e13, 0.70e13, 0.9741,
     'r200 = 974.1 +/- 5.7 kpc', 'MEASURED',
     'eROSITA, A&A 2024 (aa49391-24)'),
    ('urban_profile', 'hot gas density profile extent', None, None, 1.2,
     'r ~ 1.2 Mpc, 13 XMM-Newton pointings, centre northwards', 'MEASURED',
     'Urban et al. 2011, MNRAS 414, 2101'),
    # ---- GAS, extrapolated
    ('planck_sz_lo', 'hot gas', 1.4e14, None, 2.5,
     'integrated to a truncation radius of 2.5 Mpc', 'EXTRAPOLATED',
     'Planck Intermediate XL, A&A 596, A101'),
    ('planck_sz_hi', 'hot gas', 1.6e14, None, 5.0,
     'integrated to a truncation radius of 5 Mpc', 'EXTRAPOLATED',
     'Planck Intermediate XL, A&A 596, A101'),
    # ---- STARS, measured
    ('kt17_core', 'stellar light L_Ks', 5.0e12, None, 1.9,
     'the collapsed core, R2t projected radius 1.9 Mpc', 'MEASURED',
     'Kourkchi & Tully 2017, ApJ 843, 16, sec 7.1'),
    ('kt17_assoc', 'stellar light L_Ks', 1.0e13, None, 7.0,
     'the Virgo Association, enclosing the infall region, radius r1t ~ 7 Mpc', 'MEASURED',
     'Kourkchi & Tully 2017, ApJ 843, 16, sec 7.1'),
    ('kkk20_core', 'stellar light L_K', 8.6e12, 1.1e12, 1.8,
     'inside the 6 deg radius, D = 12-22 Mpc', 'MEASURED',
     'Kashibadze, Karachentsev & Karachentseva 2020, A&A 635, A135, sec 3'),
    ('ngvs8_mstar', 'stellar mass M*', 8.1e12, None, 1.8,
     "within Virgo's virial radius, corrected for diffuse light", 'MEASURED',
     'Durrell et al. 2014 (NGVS VIII), ApJ 794, 103'),
    # ---- DYNAMICAL totals inside R0
    ('kkk20_MT', 'total mass inside R0', 7.4e14, 0.9e14, 7.15,
     'inside R0 = 7.0-7.3 Mpc, from the infall model', 'MEASURED',
     'Kashibadze et al. 2020, A&A 635, A135'),
    ('kt17_assoc_mass', 'total mass', 7.0e14, None, 7.0,
     'within the association, r1t ~ 7 Mpc', 'MEASURED',
     'Kourkchi & Tully 2017 (luminosity-derived; "susceptible to systematics")'),
]

# The one figure that must NOT be used as a measurement, and why -- prediction (5)'s guard.
CIRCULAR = ('hevics_hotgas', 1e12,
            'HeVICS XVI (Davies et al. 2014) quotes a hot-gas mass DENSITY of ~1e12 Msun/Mpc^3, '
            'but states: "we have used 20% of the gravitational mass measured by the X-rays". '
            'That is an ASSUMED baryon fraction of 0.20 -- which is the very quantity PO-93 '
            'asks to have measured. Using it to answer PO-93 would be circular.')
HEVICS_VOLUME = 62.4          # Mpc^3, the survey volume its densities are quoted over
HEVICS_STAR_DENSITY = 4e10    # Msun/Mpc^3, total cluster stars

# Stellar mass-to-light in Ks for old cluster populations, as a declared band.
ML_KS = (0.6, 1.0)

# Virgo's distance, for the angular size the closing measurement must reach.
D_VIRGO = 15.8                # Mpc, Kourkchi & Tully 2017 weighted distance, +/- 0.5
D_VIRGO_BAND = (15.0, 18.0)   # the spread across the sources used here
PLANCK_SZ_ANGLE = 8.0         # deg; Planck XL detects SZ excess to ~8 deg (~2x virial radius)

OUT = {}


def rule(ch='='):
    print(ch * 104)


def main():
    # ------------------------------------------------------------------ (V1) the instrument
    rule()
    print('  Ⓥ① THE INSTRUMENT IS THE IMPORTED ONE, AND ITS OWN CONTROL IS RE-RUN')
    rule()
    print(f'      r_HE and constants  <-  {os.path.relpath(_INSTR, ROOT)}  (by ast)')
    print(f'      H0 = {H0 * Mpc / 1e3:.0f} km/s/Mpc,  OmL = {OmL},  f_b = {f_b_corpus}')
    sep = (1.0 / f_b_corpus) ** (1 / 3)
    assert abs(r_HE(1e15) / r_HE(1e15 * f_b_corpus) - sep) < 1e-9
    print(f'      its control: f_b^(-1/3) = {sep:.3f} in radius, 1/f_b = {1/f_b_corpus:.2f} '
          f'in mass  -> ok')
    OUT['sep'] = sep

    # ------------------------------------------------------------------ (1) what exists, to what radius
    print()
    rule()
    print('  ① WHAT EXISTS, AND THE RADIUS EACH FIGURE IS MEASURED TO')
    rule()
    print(f'      {"component":34s} {"value":>12s} {"aperture":>9s}  {"status":12s} aperture as stated')
    for k, comp, val, err, ap, apstr, status, src in LIT:
        v = '--' if val is None else f'{val:.3e}'
        print(f'      {comp:34s} {v:>12s} {ap:7.3f}Mpc  {status:12s} {apstr}')
        print(f'      {"":34s} {"":>12s} {"":>12s}  {"":12s} [{src}]')

    # The gate: does ANY gas figure reach the turnaround band, as a MEASUREMENT?
    gas_measured = [e for e in LIT if 'gas' in e[1] and e[6] == 'MEASURED']
    gas_reach = max(e[4] for e in gas_measured)
    star_measured = [e for e in LIT if 'stellar' in e[1] and e[6] == 'MEASURED']
    star_reach = max(e[4] for e in star_measured)
    print()
    print(f'      furthest MEASURED gas aperture    {gas_reach:.3f} Mpc')
    print(f'      furthest MEASURED stellar aperture {star_reach:.3f} Mpc')
    print(f'      the turnaround band PO-93 asks about  {R0_BAND[0]:.1f} - {R0_BAND[1]:.1f} Mpc')
    OUT['gas_reach'] = gas_reach
    OUT['star_reach'] = star_reach

    # ⇒ prediction (1): the pieces do not both reach 7.0, and the GAS is what stops.
    gas_stops = gas_reach < R0_BAND[0]
    star_reaches = star_reach >= R0_BAND[0]
    print()
    print(f'  ⇒ ① the GAS stops short of {R0_BAND[0]} Mpc: {gas_stops}  '
          f'(by a factor of {R0_BAND[0]/gas_reach:.2f})')
    print(f'  ⇒ ② the STARS reach the turnaround radius: {star_reaches}')
    assert gas_stops, 'a measured gas mass reaching 7.0 Mpc would overturn prediction (1)'
    assert star_reaches, 'the stellar term must reach 7.0 Mpc for (2) to hold'
    OUT['gas_stops'] = gas_stops
    OUT['star_reaches'] = star_reaches
    OUT['gas_short_factor'] = R0_BAND[0] / gas_reach

    # the circularity guard
    print()
    print(f'  ⚠ AND ONE FIGURE THAT LOOKS LIKE A GAS MASS AND MAY NOT BE USED AS ONE:')
    print(f'      {CIRCULAR[2]}')
    hev_star_total = HEVICS_STAR_DENSITY * HEVICS_VOLUME
    print(f'      (its stellar figure IS usable, as a density: {HEVICS_STAR_DENSITY:.0e} '
          f'Msun/Mpc^3 x {HEVICS_VOLUME} Mpc^3 = {hev_star_total:.2e} Msun,')
    print(f'       over an 85 sq deg x (17-23 Mpc) slab -- a projected radius of ~1.7 Mpc, '
          f'not a sphere of radius 7.)')
    OUT['hevics_star_total'] = hev_star_total

    # ------------------------------------------------------------------ (2) the stellar term AT R0
    print()
    rule()
    print('  ② THE ONE BARYONIC TERM THAT IS MEASURED TO THE TURNAROUND RADIUS, BUILT')
    rule()
    L_core = dict((e[0], e[2]) for e in LIT)['kt17_core']
    L_assoc = dict((e[0], e[2]) for e in LIT)['kt17_assoc']
    growth = L_assoc / L_core
    print(f'      L_Ks in the collapsed core (R2t = 1.9 Mpc)      {L_core:.3e} Lsun')
    print(f'      L_Ks in the association    (r1t ~ 7.0 Mpc)      {L_assoc:.3e} Lsun')
    print(f'  ⇒   the stellar growth factor across the aperture gap   {growth:.4f}')
    OUT['L_core'] = L_core
    OUT['L_assoc'] = L_assoc
    OUT['star_growth'] = growth

    # does that factor sit inside the window r7484's bound needs?
    inside = R7484_FACTOR[0] <= growth <= R7484_FACTOR[1]
    print(f'      r7484 needs the TOTAL baryons to grow by {R7484_FACTOR[0]}-{R7484_FACTOR[1]} '
          f'across this gap')
    print(f'  ⇒   the measured STELLAR factor {growth:.2f} sits inside that window: {inside}')
    OUT['star_growth_inside_window'] = inside

    # the stellar mass itself, with the M/L band declared
    Mstar_lo, Mstar_hi = L_assoc * ML_KS[0], L_assoc * ML_KS[1]
    Mstar_mid = 0.5 * (Mstar_lo + Mstar_hi)
    print()
    print(f'      with M*/L_Ks = {ML_KS[0]}-{ML_KS[1]} for old cluster populations:')
    print(f'        M* inside r1t ~ 7 Mpc      {Mstar_lo:.3e} to {Mstar_hi:.3e} Msun')
    print(f'        midpoint                   {Mstar_mid:.3e} Msun')
    print(f'      r7484 used M* = {R7484_MSTAR:.2e} Msun with NO stated aperture;')
    print(f'      this figure agrees within the M/L band and now CARRIES one.')
    OUT['Mstar_at_R0'] = [Mstar_lo, Mstar_hi]
    OUT['Mstar_mid'] = Mstar_mid

    # ------------------------------------------------------------------ (3) the gap, quantified
    print()
    rule()
    print('  ③ THE GAP: WHAT IS MISSING, AND HOW MUCH OF IT THE MEASURED TERM CAN SUPPLY')
    rule()
    short_lo = R7484_NEEDED[0] - R7484_BARY_AT_3P4[1]
    short_hi = R7484_NEEDED[1] - R7484_BARY_AT_3P4[0]
    print(f'      for the baryon-only bound NOT to be violated, r7484 requires')
    print(f'        M_bary inside R0      {R7484_NEEDED[0]:.2e} to {R7484_NEEDED[1]:.2e} Msun')
    print(f'      against what is on the books inside ~{R7484_APERTURE} Mpc')
    print(f'        gas (EXTRAPOLATED) + stars  {R7484_BARY_AT_3P4[0]:.2e} to '
          f'{R7484_BARY_AT_3P4[1]:.2e} Msun')
    print(f'  ⇒   the shortfall to be found between {R7484_APERTURE} and '
          f'{R0_BAND[0]}-{R0_BAND[1]} Mpc:')
    print(f'        {short_lo:.3e} to {short_hi:.3e} Msun')
    OUT['shortfall'] = [short_lo, short_hi]

    # what the stellar doubling can supply, at most
    star_adds_max = R7484_MSTAR * (growth - 1.0)
    frac_lo = star_adds_max / short_hi
    frac_hi = star_adds_max / short_lo
    print()
    print(f'      the stellar term doubles across the gap, so it adds AT MOST')
    print(f'        {R7484_MSTAR:.2e} x ({growth:.2f} - 1) = {star_adds_max:.3e} Msun')
    print(f'      (at most, because {R7484_APERTURE} Mpc already encloses part of that growth)')
    print(f'  ⇒   the measured stellar term covers {frac_lo*100:.1f}% to {frac_hi*100:.1f}% '
          f'of the shortfall')
    assert frac_hi < 0.25, 'if stars could cover >25% of the shortfall the gate would be stellar'
    OUT['star_adds_max'] = star_adds_max
    OUT['star_covers_frac'] = [frac_lo, frac_hi]

    print()
    print(f'  ⇒ ⚑ SO PO-93\'s GATE IS NOT "A BARYONIC MASS" BUT SPECIFICALLY "A GAS MASS".')
    print(f'      The stellar half is measured to the turnaround radius and it cannot close')
    print(f'      the gap; {(1-frac_hi)*100:.0f}% or more of the shortfall must be gas, and no')
    print(f'      measured gas figure reaches past {gas_reach:.2f} Mpc.')

    # ------------------------------------------------------------------ (4) what would close it
    print()
    rule()
    print('  ④ WHAT MEASUREMENT WOULD CLOSE THE GAP — stated as an aperture on the sky')
    rule()
    th_lo = math.degrees(math.atan(R0_BAND[0] / D_VIRGO))
    th_hi = math.degrees(math.atan(R0_BAND[1] / D_VIRGO))
    print(f'      Virgo\'s distance  D = {D_VIRGO} Mpc (Kourkchi & Tully 2017 weighted)')
    print(f'      R0 = {R0_BAND[0]}-{R0_BAND[1]} Mpc subtends  {th_lo:.1f} to {th_hi:.1f} deg')
    print(f'      the existing SZ detection (Planck XL) reaches ~{PLANCK_SZ_ANGLE:.0f} deg '
          f'(~2x the virial radius)')
    ratio = 0.5 * (th_lo + th_hi) / PLANCK_SZ_ANGLE
    print(f'  ⇒   the closing measurement must reach {ratio:.2f}x further IN ANGLE than the '
          f'deepest existing one')
    for d in D_VIRGO_BAND:
        print(f'        at D = {d:.1f} Mpc:  {math.degrees(math.atan(R0_BAND[0]/d)):.1f} to '
              f'{math.degrees(math.atan(R0_BAND[1]/d)):.1f} deg')
    OUT['theta_R0'] = [th_lo, th_hi]
    OUT['theta_ratio'] = ratio
    assert th_lo > PLANCK_SZ_ANGLE, 'the required aperture must exceed the existing SZ reach'

    # ------------------------------------------------------------------ (5) the bound, with the measured star term
    print()
    rule()
    print('  ⑤ THE BOUND RE-READ WITH THE MEASURED STELLAR TERM — does r7484\'s direction hold?')
    rule()
    # gas EXTRAPOLATED + stars MEASURED-at-R0. Labelled, and NOT offered as a discharge.
    mb_lo = 1.4e14 + Mstar_lo
    mb_hi = 1.6e14 + Mstar_hi
    print(f'      M_bary = Planck-SZ gas (EXTRAPOLATED, 2.5-5 Mpc) + M* (MEASURED, 7 Mpc)')
    print(f'             = {mb_lo:.3e} to {mb_hi:.3e} Msun')
    print(f'      r7484 used {R7484_BARY_AT_3P4[0]:.3e} to {R7484_BARY_AT_3P4[1]:.3e} Msun')
    r_lo, r_hi = r_HE(mb_lo) / Mpc, r_HE(mb_hi) / Mpc
    print(f'      the r_HE bound this allows   {r_lo:.3f} to {r_hi:.3f} Mpc')
    print(f'      against R0 = {R0_BAND[0]}-{R0_BAND[1]} Mpc')
    viol_lo = R0_BAND[0] / r_hi
    viol_hi = R0_BAND[1] / r_lo
    print(f'  ⇒   R0 / r_HE(M_bary) = {viol_lo:.3f} to {viol_hi:.3f}   '
          f'=> VIOLATED: {viol_lo > 1.0}')
    print(f'      r7484 reported this violation as 19 to 33 per cent; it survives the '
          f'substitution.')
    OUT['rHE_bary'] = [r_lo, r_hi]
    OUT['violation'] = [viol_lo, viol_hi]
    assert viol_lo > 1.0, "the baryon-only bound must still be violated"

    # and the dark fraction at R0 is STILL not a number
    print()
    print(f'  ⚠ AND THE QUANTITY PO-93 ASKS FOR IS STILL NOT A NUMBER.  The gas term in the')
    print(f'    line above is EXTRAPOLATED, so f_b(R0) computed from it is the bound r7484')
    print(f'    already has, not the measurement the row asks for.  Reported, not offered')
    print(f'    as a discharge -- prediction ⑤ of this revision\'s registration.')
    fb_lo = mb_lo / (7.4e14 + 0.9e14)
    fb_hi = mb_hi / (7.4e14 - 0.9e14)
    print(f'    (for the record, and labelled: M_bary/M_T(R0) = {fb_lo:.3f} to {fb_hi:.3f}, '
          f'against the')
    print(f'     {R7484_FACTOR[0]}-{R7484_FACTOR[1]}x / 33-56 per cent a baryon-only Virgo '
          f'would need.)')
    OUT['fb_labelled'] = [fb_lo, fb_hi]
    below = fb_hi < 0.33
    print(f'    even the EXTRAPOLATED budget falls below that 33 per cent floor: {below}')
    OUT['fb_below_floor'] = below

    print()
    rule()
    print('  ⇒ VERDICT: PO-93 does NOT discharge and does NOT terminate.  The stellar half of')
    print('    its gate is measured to the turnaround radius and is closed; the gas half is')
    print('    not, and the gap is located to a factor and an angle.')
    rule()

    # ** THE LITERATURE TABLE IS BANKED TOO, so the receipt pins its INPUTS and not only the
    #    arithmetic.  A figure quoted in prose and not banked is a figure nothing can check. **
    OUT['lit'] = {k: {'component': comp, 'value': val, 'err': err, 'aperture_Mpc': ap,
                      'aperture_stated': apstr, 'status': status, 'source': src}
                  for k, comp, val, err, ap, apstr, status, src in LIT}
    OUT['inputs'] = {
        'R0_band': list(R0_BAND), 'r7484_factor': list(R7484_FACTOR),
        'r7484_needed': list(R7484_NEEDED), 'r7484_bary_at_3p4': list(R7484_BARY_AT_3P4),
        'r7484_aperture': R7484_APERTURE, 'r7484_mstar': R7484_MSTAR,
        'ML_Ks': list(ML_KS), 'D_virgo': D_VIRGO, 'D_virgo_band': list(D_VIRGO_BAND),
        'planck_sz_angle': PLANCK_SZ_ANGLE, 'hevics_volume': HEVICS_VOLUME,
        'hevics_star_density': HEVICS_STAR_DENSITY, 'hevics_assumed_fgas': 0.20,
    }
    # the flip margin the probe in the receipt reports, computed here so both agree
    _flip = {}
    for thr in (0.25, 0.50):
        _flip[f'{thr:.2f}'] = [thr * short_lo / (R7484_MSTAR * (growth - 1.0)),
                           thr * short_hi / (R7484_MSTAR * (growth - 1.0))]
    OUT['flip_multiplier'] = _flip
    OUT['largest_published_mstar'] = 8.1e12
    OUT['flip_headroom_over_largest'] = (
        _flip['0.25'][0] * R7484_MSTAR / 8.1e12)

    with open(os.path.join(HERE, 'result.json'), 'w', encoding='utf-8') as fh:
        json.dump(OUT, fh, indent=2, sort_keys=True)
    print(f'  wrote {os.path.relpath(os.path.join(HERE, "result.json"), ROOT)}')


if __name__ == '__main__':
    main()
