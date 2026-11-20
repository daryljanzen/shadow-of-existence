#!/usr/bin/env python3
r"""r7831 (cc66) -- PO-93's gate: which baryonic terms are MEASURED at Virgo's turnaround radius.

COMPUTES: for each published Virgo baryonic figure, whether its APERTURE reaches the turnaround
  band PO-93 names (7.0-7.8 Mpc); and, for the one term that does, whether it can close the gap
  r7484 left.
  INPUT  the banked literature table and arithmetic:  r7831's result.json, PARSED here and not
                         remembered -- every figure in it carries the aperture its source states
  INPUT  r7484's standing position:  M_bary(R0) would have to be 1.70-2.35x the gas-plus-stars
                         measured inside ~3.4 Mpc, i.e. 2.6-4.1e14 Msun
  INPUT  the instrument: r_HE out of P03 by `ast`, the same single copy r7484 used
  OUTPUT which apertures reach 7.0 Mpc, the stellar growth factor across the gap, the fraction of
         the shortfall that term can supply, the angular reach the closing measurement needs, and
         whether r7484's direction survives the substitution

** THE STELLAR HALF REACHES THE TURNAROUND RADIUS.  THE GAS HALF STOPS AT 1.2 Mpc. **

  furthest MEASURED gas aperture          1.20 Mpc     (Urban+ 2011 profile extent)
  furthest MEASURED stellar aperture      7.00 Mpc     (Kourkchi & Tully 2017, the Association)
  the band PO-93 asks about               7.0 - 7.8 Mpc
  => the gas is short by a factor of      5.8333

  L_Ks core (R2t = 1.9 Mpc)               5.000e12 Lsun
  L_Ks association (r1t ~ 7.0 Mpc)        1.000e13 Lsun
  the stellar growth factor               2.0000      -- inside r7484's 1.70-2.35 window
  M*(r1t) at M/L_Ks = 0.6-1.0             6.0e12 to 1.0e13 Msun

  the shortfall r7484's bound needs       8.50e13 to 2.55e14 Msun
  what the stellar doubling can add       1.50e13 Msun  AT MOST
  => the measured stellar term covers     5.9% to 17.6% of it

=> ** So PO-93's gate is not "a baryonic mass" but specifically a GAS mass: >= 82 per cent of the
   missing mass must be gas, and no measured gas figure reaches past 1.2 Mpc.  The row NARROWS to
   its gas half; it does not discharge.  Striking or narrowing the row is 69's; THE_REGISTER.md is
   untouched here. **

** AND ONE FIGURE IS EXCLUDED AS CIRCULAR, WHICH IS A FINDING AND NOT A HOUSEKEEPING NOTE. **
HeVICS XVI quotes a hot-gas mass density of ~1e12 Msun/Mpc^3 over a 62.4 Mpc^3 volume -- a figure
that looks like a large-aperture gas mass.  Its own parenthesis says "we have used 20% of the
gravitational mass measured by the X-rays".  That is an ASSUMED baryon fraction of 0.20, which is
the quantity PO-93 exists to have measured.  => Ⓕ⑥ asserts it enters no baryon total here.
Two further traps in the same paper, both of which would have produced a wrong number: its totals
are DENSITIES in Msun/Mpc^3 and misread as masses by a factor of ~62; and its 62.4 Mpc^3 is an
85 sq deg x (17-23 Mpc) slab, a projected radius of ~1.7 Mpc, not a sphere of radius 7.

** WHAT THIS RECEIPT DOES NOT CLAIM. **  It does not supply f_b at the turnaround radius.  Every
line here that uses a gas mass past 1.2 Mpc uses an EXTRAPOLATED one and says so; the substitution
in Ⓔ⑤ re-verifies r7484's DIRECTION and is not a measurement of the dark fraction.  PO-93 stays
open on its gas half.

Run:  python3 P15_..._and_the_gas_half_is_not.py     (rc 0 = all arms held)
"""

import ast
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
R7831 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7831_cc66_PO93_the_baryonic_mass_at_virgos_turnaround_radius',
                     'result.json')
_INSTR = os.path.join(ROOT, 'receipts', 'P03_SdS_slicing',
                      'P03_which_mass_sets_the_hubble_eddington_radius.py')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


def _names(t):
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        return [x for e in t.elts for x in _names(e)]
    return []


def _load(path):
    """r_HE and its constants by ast -- P03's module body prints and asserts."""
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
r_HE, Mpc, f_b_corpus = _I['r_HE'], _I['Mpc'], _I['f_b']

# ** THE FIGURES ARE PARSED OUT OF THE BANKED RUN, not remembered. **  A receipt that hardcodes
# what it must check compares against a memory of it and stays green if the computation moves.
J = json.load(open(R7831, encoding='utf-8'))
_L, _IN = J['lit'], J['inputs']

R0_BAND = (7.0, 7.8)
R7484_FACTOR = (1.70, 2.35)
R7484_NEEDED = (2.6e14, 4.1e14)
R7484_BARY = (1.55e14, 1.75e14)
PLANCK_SZ_ANGLE = 8.0
D_VIRGO = 15.8

# ======================================================= Ⓐ① THE APERTURES -- the central claim
head("Ⓐ① THE APERTURES: WHICH TERMS REACH THE TURNAROUND BAND")
print(f"      furthest MEASURED gas aperture       {J['gas_reach']:.3f} Mpc")
print(f"      furthest MEASURED stellar aperture   {J['star_reach']:.3f} Mpc")
print(f"      the band PO-93 asks about            {R0_BAND[0]} - {R0_BAND[1]} Mpc")
_short = R0_BAND[0] / J['gas_reach']
print(f"      the gas is short by a factor of      {_short:.4f}")
# TWO-SIDED: the gas must fall short AND the stars must reach.  Either flipping flips the finding.
check("the gas stops short of 7.0 Mpc and the stars reach it",
      J['gas_reach'] < R0_BAND[0] and J['star_reach'] >= R0_BAND[0]
      and abs(_short - J['gas_short_factor']) < 1e-12)

# ======================================================= Ⓑ② THE STELLAR TERM AT R0
head("Ⓑ② THE ONE TERM MEASURED AT THE TURNAROUND RADIUS, AND ITS GROWTH ACROSS THE GAP")
_g = J['L_assoc'] / J['L_core']
print(f"      L_Ks core        (R2t = 1.9 Mpc)     {J['L_core']:.3e} Lsun")
print(f"      L_Ks association (r1t ~ 7.0 Mpc)     {J['L_assoc']:.3e} Lsun")
print(f"      the growth factor                    {_g:.4f}")
print(f"      r7484's window for the TOTAL         {R7484_FACTOR[0]} - {R7484_FACTOR[1]}")
print(f"      M*(r1t), M/L_Ks = 0.6-1.0            {J['Mstar_at_R0'][0]:.3e} to "
      f"{J['Mstar_at_R0'][1]:.3e} Msun")
# the growth factor is RE-DERIVED from the two luminosities, not read from the banked scalar
check("the stellar growth factor re-derives to 2.0 and sits inside r7484's window",
      abs(_g - 2.0) < 1e-12 and abs(_g - J['star_growth']) < 1e-12
      and R7484_FACTOR[0] <= _g <= R7484_FACTOR[1] and J['star_growth_inside_window'])

# ======================================================= Ⓒ③ THE SHORTFALL -- the result
head("Ⓒ③ THE SHORTFALL, AND THE FRACTION THE MEASURED TERM CAN SUPPLY")
_slo = R7484_NEEDED[0] - R7484_BARY[1]
_shi = R7484_NEEDED[1] - R7484_BARY[0]
_adds = 1.5e13 * (_g - 1.0)
_flo, _fhi = _adds / _shi, _adds / _slo
print(f"      required inside R0                   {R7484_NEEDED[0]:.2e} to "
      f"{R7484_NEEDED[1]:.2e} Msun")
print(f"      on the books inside ~3.4 Mpc         {R7484_BARY[0]:.2e} to {R7484_BARY[1]:.2e} Msun")
print(f"      the shortfall                        {_slo:.3e} to {_shi:.3e} Msun")
print(f"      the stellar doubling adds, at most   {_adds:.3e} Msun")
print(f"      => it covers                         {_flo*100:.1f}% to {_fhi*100:.1f}%")
print(f"      => so the gas must supply at least   {(1-_fhi)*100:.1f}%")
check("the shortfall re-derives and the measured stellar term covers under a quarter of it",
      abs(_slo - J['shortfall'][0]) < 1e6 and abs(_shi - J['shortfall'][1]) < 1e6
      and abs(_flo - J['star_covers_frac'][0]) < 1e-12
      and abs(_fhi - J['star_covers_frac'][1]) < 1e-12 and _fhi < 0.25)

# ======================================================= Ⓓ④ THE ANGULAR REACH
head("Ⓓ④ THE GAP AS AN ANGULAR REACH -- what the closing measurement must cover")
_tlo = math.degrees(math.atan(R0_BAND[0] / D_VIRGO))
_thi = math.degrees(math.atan(R0_BAND[1] / D_VIRGO))
_ratio = 0.5 * (_tlo + _thi) / PLANCK_SZ_ANGLE
print(f"      R0 at D = {D_VIRGO} Mpc subtends        {_tlo:.3f} to {_thi:.3f} deg")
print(f"      the deepest existing SZ detection    ~{PLANCK_SZ_ANGLE:.0f} deg (Planck XL)")
print(f"      => further in angle by               {_ratio:.4f}x")
print(f"      ⌗ and that ratio is the r1t/r2t = 3.14 +/- 0.28 of Tully 2015, because the aperture")
print(f"        gap IS the first-to-second turnaround gap.  An identity, not a second finding.")
check("the required angular radius exceeds the deepest existing SZ reach",
      _tlo > PLANCK_SZ_ANGLE and abs(_tlo - J['theta_R0'][0]) < 1e-9
      and abs(_thi - J['theta_R0'][1]) < 1e-9 and abs(_ratio - J['theta_ratio']) < 1e-9)

# ======================================================= Ⓔ⑤ r7484's DIRECTION UNDER SUBSTITUTION
head("Ⓔ⑤ r7484's DIRECTION, RE-VERIFIED WITH THE MEASURED STELLAR TERM SUBSTITUTED IN")
_mblo = 1.4e14 + J['Mstar_at_R0'][0]
_mbhi = 1.6e14 + J['Mstar_at_R0'][1]
_rlo, _rhi = r_HE(_mblo) / Mpc, r_HE(_mbhi) / Mpc
_vlo, _vhi = R0_BAND[0] / _rhi, R0_BAND[1] / _rlo
print(f"      M_bary = gas (EXTRAPOLATED) + M* (MEASURED at 7 Mpc)")
print(f"                                           {_mblo:.3e} to {_mbhi:.3e} Msun")
print(f"      the r_HE bound it allows             {_rlo:.4f} to {_rhi:.4f} Mpc")
print(f"      R0 / r_HE(M_bary)                    {_vlo:.4f} to {_vhi:.4f}")
print(f"      => the baryon-only bound is violated: {_vlo > 1.0}")
check("the baryon-only bound is still violated under the substitution",
      _vlo > 1.0 and abs(_rlo - J['rHE_bary'][0]) < 1e-9
      and abs(_rhi - J['rHE_bary'][1]) < 1e-9 and abs(_vlo - J['violation'][0]) < 1e-9)

# ======================================================= Ⓕ⑥ THE CIRCULARITY EXCLUSION
head("Ⓕ⑥ THE CIRCULAR FIGURE IS EXCLUDED FROM EVERY BARYON TOTAL -- asserted, not promised")
# HeVICS's gas figure, had it been admitted, would be ~1e12 x 62.4 = 6.24e13 Msun.  Assert that
# no baryon total in the banked run contains it, within any pairing of the terms that ARE used.
_hev_gas = 1e12 * 62.4
_totals = [_mblo, _mbhi, R7484_BARY[0], R7484_BARY[1]]
_contaminated = [t for t in _totals
                 if any(abs(t - (base + _hev_gas)) < 1e12
                        for base in (1.4e14, 1.6e14, 0.0, J['Mstar_at_R0'][0],
                                     J['Mstar_at_R0'][1]))]
print(f"      the HeVICS gas figure, if admitted   {_hev_gas:.3e} Msun")
print(f"      baryon totals used here              {', '.join(f'{t:.3e}' for t in _totals)}")
print(f"      totals containing it                 {len(_contaminated)}")
print(f"      ⌗ its STELLAR density is usable and is reported: 4e10 x 62.4 = "
      f"{J['hevics_star_total']:.3e} Msun")
print(f"        over a slab of projected radius ~1.7 Mpc -- a core-aperture figure, not a 7 Mpc one")
check("no baryon total used here contains the circular HeVICS gas figure",
      len(_contaminated) == 0 and abs(J['hevics_star_total'] - 2.496e12) < 1e9)

# ======================================================= Ⓖ⑦ THE PROBE -- can the finding fail?
head("Ⓖ⑦ THE PROBE: THE 'GATE IS GAS' FINDING IS SENSITIVE TO THE DATA, NOT STRUCTURALLY TRUE")
# A conclusion that cannot be overturned by any input is not a measurement.  Perturb the ONE
# quantity the finding turns on -- the stellar term's size -- and watch the verdict flip.
print(f"      the finding: stars cover {_fhi*100:.1f}% of the shortfall, so the gate is GAS")
_flipped = None
for mult in (1, 2, 5, 10, 20):
    adds = 1.5e13 * mult * (_g - 1.0)
    frac = adds / _slo
    verdict = 'GAS' if frac < 0.25 else 'STELLAR'
    print(f"        M* x {mult:<3d} -> stars cover {frac*100:6.1f}%  => the gate is {verdict}")
    if verdict == 'STELLAR' and _flipped is None:
        _flipped = mult
print(f"      => the verdict flips at M* x {_flipped}, i.e. a stellar mass {_flipped}x the measured")
print(f"         one.  The finding is a measurement of the stellar term's size, not a tautology.")
check("the finding flips under a bounded perturbation of the stellar term",
      _flipped is not None and _flipped > 1
      and (1.5e13 * 1 * (_g - 1.0)) / _slo < 0.25
      and (1.5e13 * _flipped * (_g - 1.0)) / _slo >= 0.25)

# ======================================================= THE PINS
PINS = {
    'the gas reach, 1.20 Mpc':              abs(J['gas_reach'] - 1.20) < 5.0e-4,
    'the stellar reach, 7.00 Mpc':          abs(J['star_reach'] - 7.00) < 3.5e-3,
    'the gas short by 5.8333':              abs(J['gas_short_factor'] - 5.8333) < 2.9e-3,
    'L_Ks core, 5.000e12':                  abs(J['L_core'] - 5.000e12) < 2.5e9,
    'L_Ks association, 1.000e13':           abs(J['L_assoc'] - 1.000e13) < 5.0e9,
    'the stellar growth factor, 2.0000':    abs(J['star_growth'] - 2.0000) < 1.0e-12,
    'M*(r1t) lower, 6.0e12':                abs(J['Mstar_at_R0'][0] - 6.0e12) < 3.0e9,
    'M*(r1t) upper, 1.0e13':                abs(J['Mstar_at_R0'][1] - 1.0e13) < 5.0e9,
    'M*(r1t) midpoint, 8.0e12':             abs(J['Mstar_mid'] - 8.0e12) < 4.0e9,
    'the shortfall lower, 8.50e13':         abs(J['shortfall'][0] - 8.50e13) < 4.2e10,
    'the shortfall upper, 2.55e14':         abs(J['shortfall'][1] - 2.55e14) < 1.2e11,
    'the stellar term adds 1.500e13':       abs(J['star_adds_max'] - 1.500e13) < 7.5e9,
    'stars cover 5.9 per cent, lower':      abs(J['star_covers_frac'][0] - 0.059) < 5.0e-4,
    'stars cover 17.6 per cent, upper':     abs(J['star_covers_frac'][1] - 0.176) < 5.0e-4,
    'the angular radius lower, 23.895':     abs(J['theta_R0'][0] - 23.895) < 5.0e-4,
    'the angular radius upper, 26.274':     abs(J['theta_R0'][1] - 26.274) < 5.0e-4,
    'the angular ratio, 3.1356':            abs(J['theta_ratio'] - 3.1356) < 5.0e-5,
    'the r_HE bound lower, 5.5216':         abs(J['rHE_bary'][0] - 5.5216) < 5.0e-5,
    'the r_HE bound upper, 5.8089':         abs(J['rHE_bary'][1] - 5.8089) < 5.0e-5,
    'the violation lower, 1.2050':          abs(J['violation'][0] - 1.2050) < 5.0e-5,
    'the violation upper, 1.4126':          abs(J['violation'][1] - 1.4126) < 5.0e-5,
    'f_b labelled, 0.176 to 0.262':         (abs(J['fb_labelled'][0] - 0.176) < 5.0e-4
                                             and abs(J['fb_labelled'][1] - 0.262) < 5.0e-4),
    'f_b is below the 33 per cent floor':   J['fb_below_floor'] is True,
    "the HeVICS stellar total, 2.496e12":   abs(J['hevics_star_total'] - 2.496e12) < 1.3e9,
    "the instrument's separation, 1.8537":  abs(J['sep'] - 1.8537) < 5.0e-5,
    # as RESULT.md prints them: equality at the printed decimals
    'RESULT prints the growth as 2.00':     round(J['star_growth'], 2) == 2.00,
    'RESULT prints the gas short by 5.83':  round(J['gas_short_factor'], 2) == 5.83,
    'RESULT prints stars covering 5.9':     round(J['star_covers_frac'][0] * 100, 1) == 5.9,
    'RESULT prints stars covering 17.6':    round(J['star_covers_frac'][1] * 100, 1) == 17.6,
    'RESULT prints the gas floor as 82':    round((1 - J['star_covers_frac'][1]) * 100) == 82,
    'RESULT prints the angle as 23.9-26.3': (round(J['theta_R0'][0], 1) == 23.9
                                             and round(J['theta_R0'][1], 1) == 26.3),
    'RESULT prints the ratio as 3.14':      round(J['theta_ratio'], 2) == 3.14,
    # ---- THE INPUTS, pinned from the bank too: a figure quoted in prose and not banked is a
    #      figure nothing can check, and the INDEX row prints these as well as the arithmetic.
    "r7484's window, 1.70 to 2.35":         (abs(_IN['r7484_factor'][0] - 1.70) < 1.0e-12
                                             and abs(_IN['r7484_factor'][1] - 2.35) < 1.0e-12),
    "r7484's required band, 2.6-4.1e14":    (abs(_IN['r7484_needed'][0] - 2.6e14) < 1.3e11
                                             and abs(_IN['r7484_needed'][1] - 4.1e14) < 2.1e11),
    "r7484's on-books band, 1.55-1.75e14":  (abs(_IN['r7484_bary_at_3p4'][0] - 1.55e14) < 7.8e10
                                             and abs(_IN['r7484_bary_at_3p4'][1] - 1.75e14) < 8.8e10),
    "r7484's aperture, 3.4 Mpc":            abs(_IN['r7484_aperture'] - 3.4) < 1.7e-3,
    "r7484's stellar input, 1.5e13":        abs(_IN['r7484_mstar'] - 1.5e13) < 7.5e9,
    'M/L_Ks band, 0.6 to 1.0':              (abs(_IN['ML_Ks'][0] - 0.6) < 1.0e-12
                                             and abs(_IN['ML_Ks'][1] - 1.0) < 1.0e-12),
    "Virgo's distance, 15.8 Mpc":           abs(_IN['D_virgo'] - 15.8) < 7.9e-3,
    'the SZ reach, 8 deg':                  abs(_IN['planck_sz_angle'] - 8.0) < 4.0e-3,
    "HeVICS's assumed f_gas, 0.20":         abs(_IN['hevics_assumed_fgas'] - 0.20) < 1.0e-12,
    "HeVICS's volume, 62.4 Mpc^3":          abs(_IN['hevics_volume'] - 62.4) < 3.2e-2,
    'eROSITA M_gas(r200), 1.98e13':         abs(_L['erosita_r200']['value'] - 1.98e13) < 9.9e9,
    'eROSITA r200, 0.9741 Mpc':             abs(_L['erosita_r200']['aperture_Mpc'] - 0.9741) < 5.0e-5,
    "Urban's profile extent, 1.2 Mpc":      abs(_L['urban_profile']['aperture_Mpc'] - 1.2) < 5.0e-4,
    'Planck gas lower, 1.4e14 at 2.5 Mpc':  (abs(_L['planck_sz_lo']['value'] - 1.4e14) < 7.0e10
                                             and abs(_L['planck_sz_lo']['aperture_Mpc'] - 2.5) < 1.3e-3),
    'Planck gas upper, 1.6e14 at 5 Mpc':    (abs(_L['planck_sz_hi']['value'] - 1.6e14) < 8.0e10
                                             and abs(_L['planck_sz_hi']['aperture_Mpc'] - 5.0) < 2.5e-3),
    'NGVS M*, 8.1e12 at the virial radius': abs(_L['ngvs8_mstar']['value'] - 8.1e12) < 4.1e9,
    'Kashibadze L_K, 8.6e12 +/- 1.1e12':    (abs(_L['kkk20_core']['value'] - 8.6e12) < 4.3e9
                                             and abs(_L['kkk20_core']['err'] - 1.1e12) < 5.5e8),
    'Kashibadze M_T, 7.4e14 +/- 0.9e14':    (abs(_L['kkk20_MT']['value'] - 7.4e14) < 3.7e11
                                             and abs(_L['kkk20_MT']['err'] - 0.9e14) < 4.5e10),
    "K&T's association mass, 7.0e14":       abs(_L['kt17_assoc_mass']['value'] - 7.0e14) < 3.5e11,
    'the core aperture, R2t = 1.9 Mpc':     abs(_L['kt17_core']['aperture_Mpc'] - 1.9) < 9.5e-4,
    # ---- the flip margin
    'the flip at 25 per cent, 1.42-4.25x':  (abs(J['flip_multiplier']['0.25'][0] - 1.42) < 5.0e-3
                                             and abs(J['flip_multiplier']['0.25'][1] - 4.25) < 5.0e-3),
    'the flip at half, 2.83-8.50x':         (abs(J['flip_multiplier']['0.50'][0] - 2.83) < 5.0e-3
                                             and abs(J['flip_multiplier']['0.50'][1] - 8.50) < 5.0e-3),
    'the flip masses, 2.12-6.375e13':       (abs(J['flip_multiplier']['0.25'][0] * 1.5e13 - 2.12e13) < 1.06e11
                                             and abs(J['flip_multiplier']['0.25'][1] * 1.5e13 - 6.375e13) < 3.2e10),
    'the flip masses at half, 4.25-12.75e13': (abs(J['flip_multiplier']['0.50'][0] * 1.5e13 - 4.25e13) < 2.2e11
                                               and abs(J['flip_multiplier']['0.50'][1] * 1.5e13 - 12.75e13) < 6.4e10),
    'the headroom over the largest, 2.62x': abs(J['flip_headroom_over_largest'] - 2.62) < 5.0e-3,
    'the largest published M*, 8.1e12':     abs(J['largest_published_mstar'] - 8.1e12) < 4.1e9,
    'NGVS instead covers 3.2 to 9.5pc':     (abs(8.1e12 / J['shortfall'][1] - 0.032) < 5.0e-4
                                             and abs(8.1e12 / J['shortfall'][0] - 0.095) < 5.0e-4),
    # ---- THE MANTISSAS AS THE INDEX ROW PRINTS THEM.  check_figures_pinned reads the bare
    #      decimal a claim prints, so a pin written on the SCALED value does not match the
    #      figure the row shows; these pin the mantissa itself, within half its last digit.
    'the row prints the adds as 1.500':     abs(J['star_adds_max'] / 1e13 - 1.500) < 7.0e-4,
    'the row prints HeVICS stars as 2.496': abs(J['hevics_star_total'] / 1e12 - 2.496) < 1.2e-3,
    'the row prints the shortfall as 2.55': abs(J['shortfall'][1] / 1e14 - 2.55) < 4.0e-3,
}
print("\n" + "=" * 92)
print(f"  THE PRINTED FIGURES, PINNED: {sum(bool(v) for v in PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure RESULT.md or the INDEX row prints is not held by this receipt"

print("\n" + "=" * 92)
print("  ⌗ WHAT THIS RECEIPT DOES NOT DO: it does not supply f_b at the turnaround radius, which")
print("    is what PO-93 asks for and what no measured gas figure can yet give.  It establishes")
print("    that the row's STELLAR half is measured at that radius and closed, that its GAS half")
print("    is not, and that the gap is >= 82 per cent gas reaching out to ~24-26 deg from M87.  Narrowing the row")
print("    is 69's act; THE_REGISTER.md is untouched here.")
print("=" * 92)
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print(f"\n  arms run: {len(PASSED) + len(FAILED)}   passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 7, "seven arms were registered; seven must run"
sys.exit(1 if FAILED else 0)
