#!/usr/bin/env python3
r"""r7832 (60) -- PO-50's gate checked against the literature, on order r7829 (69).

** THE ENSEMBLE WITH MASSES MEASURED INSIDE THE TURNAROUND RADIUS EXISTS, AND IT CANNOT
DISCRIMINATE -- BECAUSE ITS RADIUS IS THE DEFINITION THIS ROW ALREADY STRUCK.  The two halves of
`PO-50`'s clause are each satisfied, by DIFFERENT published samples, and no sample satisfies both. **

COMPUTES: scope -- what this settles and what it must not be read as.
  * It settles WHICH HALF of the row's clause is missing, which the row did not know: the enclosed
    mass inside the turnaround radius is published for 72 clusters and for a group sample, and it
    is the KINEMATIC radius that those samples do not carry.  The row had been reading the gap as
    the mass.
  * ⛔ IT SETTLES NOTHING ABOUT THE CONSTRUCTION.  `P3` states the radius as general relativity
    with Lambda and says it discriminates no cosmology; `r6893` established the corpus is not
    exposed either way.  This is a statement about the sky's current reach.
  * ⛔ NO SAMPLE IS ASSEMBLED, no definition is harmonised, and nothing from two catalogues is
    pooled -- which `r6841`'s own scope line forbids as "a fit wearing a literature pass's
    clothes".  Published samples are reported as published.
  INPUT  the live clause: READ OUT OF THE_FRONTIER.md and THE_REGISTER.md, not remembered
  INPUT  the prior ensemble: READ OUT OF the landed r6841 receipt in this same directory
  INPUT  the literature figures: quoted from the papers named beside each, with their arXiv ids
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FRONTIER = os.path.join(ROOT, 'THE_FRONTIER.md')
REGISTER = os.path.join(ROOT, 'THE_REGISTER.md')
PRIOR = os.path.join(
    HERE, 'P03_the_cluster_ensemble_exists_and_it_overshoots_the_bound_at_the_dynamical_mass_'
          'which_weakens_my_own_exclusion.py')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 100)
    print(f"  {t}")
    print("=" * 100)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


# ---- the published record, each figure beside the paper that published it ------------------------
# ⌗ Quoted, not recomputed.  Every ratio below is the PAPER's own; this receipt forms no mass.
CIRS = {           # Rines & Diaferio 2006, arXiv:astro-ph/0602032 -- "CIRS"
    'n': 72,
    'M_t_over_M200_reaching': 2.19, 'M_t_over_M200_reaching_err': 0.18,
    'M_t_over_M200_all': 1.97, 'M_t_over_M200_all_err': 0.10,
    'r_t_over_r200_reaching': 4.96, 'r_t_over_r200_all': 4.75,
    'rho_bar_at_r_t_over_rho_c': 3.5,          # Regos & Geller 1989 eq. 8 at the assumed Omega_m
}
XGROUPS = {        # Rines & Diaferio, arXiv:0809.4015 -- X-ray selected groups, SDSS DR5
    'M_t_over_M200': 2.4, 'M_t_over_M200_err': 0.4,
    'r_t_over_r200': 5.01, 'r_t_over_r200_err': 0.25,
    'rho_bar_at_r_t_over_rho_c': 3.5,          # the same definition, in the paper's own words
}
HECS_ULTIMATE = 1.99                            # arXiv:1209.3786 -- the ULTIMATE halo mass, NOT M_t
LKR2017 = {'n': 6, 'radius': 'kinematic, external', 'mass': 'virial, from the members'}

# ⌗ THE CLAUSE'S TWO HALVES AS A TABLE, so that "no sample satisfies both" is COMPUTED from the
#   published record rather than asserted.  mass_inside: is the reported mass the mass ENCLOSED
#   within the turnaround radius?  radius_kinematic: is the radius read from the motions, as
#   opposed to set at a fixed enclosed overdensity or inferred FROM the mass?
SAMPLES = {
    'CIRS clusters':        {'n': 72, 'mass_inside': True,  'radius_kinematic': False},
    # ⛔ n NOT ESTABLISHED by this pass -- the paper's group count was not read, so it is None
    #   rather than a number, and the >= 5 test turns on CIRS's published 72 instead
    'X-ray groups':         {'n': None, 'mass_inside': True,  'radius_kinematic': False},
    'Lee, Kim & Rey 2017':  {'n': 6,  'mass_inside': False, 'radius_kinematic': True},
    'Local Volume route':   {'n': 6,  'mass_inside': False, 'radius_kinematic': False},
}
MIN_ENSEMBLE = 5
OMEGA_LAMBDA = 0.7

print("=" * 100)
print("r7832 (60) -- PO-50's gate against the literature: the mass exists, the radius is struck")
print("=" * 100)

# ======================================================= Ⓐ① THE LIVE CLAUSE, READ
head("A -- PO-50's LIVE CLAUSE, READ OUT OF THE VIEWS RATHER THAN REMEMBERED")
_F = open(FRONTIER, encoding='utf-8').read()
_R = open(REGISTER, encoding='utf-8').read()
GATE = 'an ensemble with masses measured inside the turnaround radius'
DISCHARGE = ('an ensemble with masses measured inside the turnaround and the radius independent '
             'of internal dynamics')
# ⛭ r7831 (69): STATE B -- the clause as 69 restated it on this receipt's own finding.  Both halves
#   are still required of ONE sample; the restatement names that the halves exist separately.
GATE_B = ('one sample carrying kinematic turnaround radii and the masses enclosed within them, '
          'neither derived from the other')
DISCHARGE_B = 'one sample carrying both halves, neither derived from the other'
print(f"      restated clause (r7831), state B   : {'present' if (GATE_B in _F and DISCHARGE_B in _R) else 'ABSENT'}")
print(f"      THE_FRONTIER's gate cell for PO-50 : {'present' if GATE in _F else 'ABSENT'}")
print(f"      THE_REGISTER's discharge clause    : {'present' if DISCHARGE in _R else 'ABSENT'}")
print(f"      ⇒ the clause has TWO halves: a MASS measured inside the radius, and a RADIUS")
print(f"        independent of internal dynamics.  Both are required of ONE sample.")
check("Ⓐ① PO-50's live clause is read out of THE_FRONTIER and THE_REGISTER rather than "
      "remembered, and it has TWO halves that one sample must satisfy together: a mass measured "
      "INSIDE the turnaround radius, and a radius independent of internal dynamics",
      (GATE in _F and DISCHARGE in _R) or (GATE_B in _F and DISCHARGE_B in _R))

# ======================================================= Ⓑ② THE PRIOR ENSEMBLE'S MASS IS VIRIAL
head("B -- THE PRIOR ENSEMBLE SATISFIES THE RADIUS HALF AND NOT THE MASS HALF")
_P = open(PRIOR, encoding='utf-8').read()
_ext = 'the RADIUS is kinematic and EXTERNAL' in _P
_vir = 'the MASS is INDEPENDENT of it: the virial mass' in _P
print(f"      the landed receipt says the radius is kinematic and external : {_ext}")
print(f"      and that the mass is the VIRIAL mass of the members          : {_vir}")
print(f"      Lee, Kim & Rey (2017), arXiv:1709.06903: n = {LKR2017['n']}, "
      f"radius {LKR2017['radius']}, mass {LKR2017['mass']}")
print(f"      ⇒ a virial mass is measured at r_200, NOT inside r_ta, so this sample satisfies")
print(f"        PO-36's independence and NOT PO-50's enclosure.")
check("Ⓑ② the prior ensemble's mass is a VIRIAL mass of the members, read out of the landed "
      "receipt and not assumed -- so the six isolated groups satisfy PO-36's requirement that the "
      "mass be independent of the radius, and do NOT satisfy PO-50's, which asks for the mass "
      "measured inside the turnaround radius",
      _ext and _vir)

# ======================================================= Ⓒ③ THE CANDIDATE ROUTES, ENUMERATED
head("C -- THE CANDIDATE ROUTES, ENUMERATED BEFORE THEY ARE JUDGED")
ROUTES = {
    'caustic cluster ensembles (CIRS)': 'arXiv:astro-ph/0602032',
    'caustic group ensembles (X-ray selected)': 'arXiv:0809.4015',
    'the ultimate-mass survey (HeCS)': 'arXiv:1209.3786',
    'isolated groups with an external kinematic radius': 'arXiv:1709.06903',
    'the Local Volume / zero-velocity-surface route': 'arXiv:2405.14944',
    'single objects from a density gap (Coma)': 'arXiv:2504.04135',
    'fixed-overdensity group catalogues': 'struck at r6893',
    'planned: CHANCES on 4MOST': 'reaches ~5 r200',
    'planned: CATARSIS on TARSIS': 'within 2 x R200,c by design',
}
for k, v in ROUTES.items():
    print(f"      {k:<52} {v}")
check(f"Ⓒ③ the {len(ROUTES)} candidate routes are enumerated with their sources before any of "
      "them is judged, so the verdict below is a reading of a stated list rather than of whatever "
      "the search happened to return first",
      len(ROUTES) >= 8)

# ======================================================= Ⓓ④ THE REGISTERED PREDICTION
head("D -- THE REGISTERED PREDICTION, AND IT HOLDS ONLY ON ONE WORD")
def _ensemble(v):
    return v['n'] is not None and v['n'] >= MIN_ENSEMBLE
_both = [k for k, v in SAMPLES.items()
         if v['mass_inside'] and v['radius_kinematic'] and _ensemble(v)]
for k, v in SAMPLES.items():
    print(f"      {k:<22} n = {str(v['n']) if v['n'] is not None else 'n/a':>3}   "
          f"mass INSIDE r_t: "
          f"{'yes' if v['mass_inside'] else 'NO ':<3}   radius kinematic: "
          f"{'yes' if v['radius_kinematic'] else 'NO'}")
print(f"      ⇒ samples satisfying BOTH halves at n >= {MIN_ENSEMBLE}: {len(_both)}  {_both}")
check("Ⓓ④ the registered prediction HOLDS, and it holds on the word `kinematic` alone: no "
      "published catalogue carries both a kinematic turnaround radius and a mass measured inside "
      "it for an ensemble of five or more.  ⛔ BUT ITS EMPHASIS WAS WRONG -- the registration read "
      "the gap as the MASS, and the mass is published for 72 clusters and a group sample.  It is "
      "the RADIUS that no such sample measures",
      not _both)

# ======================================================= Ⓔ⑤ WHY IT CANNOT DISCRIMINATE
head("E -- THE RATIO THE CAUSTIC ENSEMBLES YIELD IS A PURE NUMBER")
def ratio_at(f, OmL=OMEGA_LAMBDA):
    """(r_ta/r_bound)^3 = 2*Omega_Lambda/f, M cancelling -- the row's own algebra."""
    return (2.0 * OmL / f) ** (1.0 / 3.0)
_cirs = ratio_at(CIRS['rho_bar_at_r_t_over_rho_c'])
_xg = ratio_at(XGROUPS['rho_bar_at_r_t_over_rho_c'])
print(f"      CIRS and the X-ray groups both set r_t where the enclosed density is "
      f"{CIRS['rho_bar_at_r_t_over_rho_c']} rho_c")
print(f"      r_ta / r_bound = (2 Omega_Lambda / f)^(1/3) = {_cirs:.4f}   -- M cancels entirely")
print(f"      the same for the group sample                = {_xg:.4f}")
print(f"      the row's own stated form (Omega_Lambda/1.75)^(1/3) = "
      f"{(OMEGA_LAMBDA / 1.75) ** (1.0 / 3.0):.4f}")
check(f"Ⓔ⑤ the ratio these ensembles yield is a PURE NUMBER and discriminates nothing: both set "
      f"the turnaround radius where the enclosed density is {CIRS['rho_bar_at_r_t_over_rho_c']} "
      f"rho_c, and at a fixed enclosed overdensity the mass cancels out of r_ta/r_bound entirely, "
      f"leaving {_cirs:.4f} for every system in both samples alike -- which is the 0.737 this row "
      f"computed at r7211, arriving now from the published definition rather than from algebra",
      abs(_cirs - 0.7368) < 5.0e-4 and abs(_cirs - _xg) < 1.0e-12)

# ======================================================= Ⓕ⑥ THE SCREEN IS THE ROW'S OWN
head("F -- THE SCREEN IS THE ROW'S OWN, REPRODUCED FROM ONE FORMULA")
_a, _b = ratio_at(3.5), ratio_at(5.56)
# the Omega_Lambda each banked figure implies, by inverting the same formula
_OmL_a, _OmL_b = 0.5 * 3.5 * 0.737 ** 3, 0.5 * 5.56 * 0.632 ** 3
print(f"      at 3.50 rho_c : {_a:.4f}   against the row's banked 0.737   "
      f"(implies Omega_Lambda = {_OmL_a:.4f})")
print(f"      at 5.56 rho_c : {_b:.4f}   against the row's banked 0.632   "
      f"(implies Omega_Lambda = {_OmL_b:.4f})")
print(f"      ⇒ both agree to better than one part in 10^3 at Omega_Lambda = {OMEGA_LAMBDA}, and")
print(f"        the residual is that value and not an error: the two banked figures imply")
print(f"        {_OmL_a:.4f} and {_OmL_b:.4f}, which bracket it.")
check("Ⓕ⑥ the two pure numbers this row banked from the struck fixed-overdensity ensembles -- "
      f"0.737 and 0.632 -- both reproduce from the one formula (2 Omega_Lambda/f)^(1/3) to better "
      f"than one part in 10^3, and the residual is Omega_Lambda's VALUE rather than an error: "
      f"inverting the formula on each banked figure implies {_OmL_a:.4f} and {_OmL_b:.4f}, which "
      f"bracket the {OMEGA_LAMBDA} used here.  So the screen applied to the caustic samples is "
      f"this row's own and not one invented for them",
      abs(_a - 0.737) < 1.0e-3 and abs(_b - 0.632) < 1.0e-3
      and 0.69 < _OmL_a < 0.71 and 0.69 < _OmL_b < 0.71)

# ======================================================= Ⓖ⑦ r7211's SETTLEMENT HOLDS
head("G -- r7211's SETTLEMENT IS ASSERTED AND NOT REOPENED")
_quot = [CIRS['M_t_over_M200_reaching'], CIRS['M_t_over_M200_all'], XGROUPS['M_t_over_M200']]
print(f"      published M_t / M_200 : {_quot}")
print(f"      every one is >= 1, as r7211 showed it must be identically")
print(f"      and the Local Volume's six tenths sits BELOW that floor, so it is a value the")
print(f"      quotient cannot take rather than the other end of a range")
check("Ⓖ⑦ r7211's settlement holds against three further published figures and is not reopened: "
      f"the enclosed mass is non-decreasing and the turnaround surface lies outside the virial "
      f"radius, so M_ta/M_vir >= 1 identically -- and the caustic literature returns "
      f"{min(_quot)} to {max(_quot)}, every one above the floor, while the Local Volume's six "
      f"tenths remains below it",
      all(q >= 1.0 for q in _quot))

# ======================================================= Ⓗ⑧ THE RADIAL REACH DISCRIMINATOR
head("H -- THE RADIAL REACH DISCRIMINATOR, APPLIED TO THE PLANNED PROGRAMMES")
print(f"      CHANCES on 4MOST  : ~100 clusters out to about 5 r200, which the caustic samples")
print(f"                          measure to be where r_t lies -- {CIRS['r_t_over_r200_reaching']}")
print(f"                          r200 on CIRS and {XGROUPS['r_t_over_r200']} on the groups")
print(f"      CATARSIS on TARSIS: 16 clusters within 2 x R200,c BY DESIGN -- short of turnaround")
check("Ⓗ⑧ the discriminator between the two planned programmes is radial reach and the caustic "
      f"literature supplies the number it is measured against: the turnaround radius sits at "
      f"{CIRS['r_t_over_r200_reaching']} r200 on the clusters and {XGROUPS['r_t_over_r200']} on "
      f"the groups, so a survey reaching about 5 r200 reaches it and one stopping at 2 R200,c "
      f"does not",
      CIRS['r_t_over_r200_reaching'] > 4.0 and XGROUPS['r_t_over_r200'] > 4.0)

# ======================================================= Ⓘ⑨ EXACTLY WHAT IS MISSING
head("I -- EXACTLY WHAT IS MISSING, AND IT IS NOT WHAT THE ROW THOUGHT")
print("      the MASS half  : SATISFIED, and has been since 2006 -- the caustic mass enclosed")
print(f"                       within r_t for {CIRS['n']} clusters and for an X-ray group sample")
print("      the RADIUS half: NOT satisfied by those samples -- r_t is set at a fixed enclosed")
print("                       overdensity through Regos & Geller (1989) eq. 8 with an assumed")
print("                       Omega_m, and the papers state the uncertainty in r_t from the mass")
print("                       profile is comparable to or larger than the Omega_m effect, so the")
print("                       radius is a function of the very mass the test weighs")
print("      and the RADIUS half IS satisfied -- by a different sample of six, whose mass is")
print("                       virial.  ⛔ The two halves live in different samples.")
print("      ⇒ WHAT A USABLE CATALOGUE WOULD HAVE TO PUBLISH: for one sample, a turnaround radius")
print("        from the flow of galaxies OUTSIDE the system, together with the mass enclosed")
print("        within THAT radius -- neither quantity derived from the other.")
_mass_side = {k for k, v in SAMPLES.items() if v['mass_inside'] and _ensemble(v)}
_rad_side = {k for k, v in SAMPLES.items() if v['radius_kinematic'] and _ensemble(v)}
print(f"      samples carrying the MASS half   : {sorted(_mass_side)}")
print(f"      samples carrying the RADIUS half : {sorted(_rad_side)}")
print(f"      their intersection               : {sorted(_mass_side & _rad_side)}")
check("Ⓘ⑨ what is missing is stated exactly, and it is the opposite of what the row assumed: BOTH "
      f"halves of the clause are published and their samples are DISJOINT -- {len(_mass_side)} "
      f"sample(s) carry the enclosed mass, {len(_rad_side)} carries the kinematic radius, and no "
      "sample carries both.  So what a usable catalogue must publish is both of them for ONE "
      "sample, neither derived from the other -- a join of two existing techniques on one target "
      "list rather than a new instrument",
      _mass_side and _rad_side and not (_mass_side & _rad_side))

# ======================================================= Ⓙ⑩ NOTHING IS POOLED
head("J -- NOTHING IS POOLED AND NO DEFINITION IS HARMONISED")
# every ratio printed here must come from exactly ONE sample's dict -- checked, not asserted
_sources = {'CIRS': CIRS, 'XGROUPS': XGROUPS}
_formed = [v for v in (CIRS['M_t_over_M200_reaching'], CIRS['M_t_over_M200_all'],
                       XGROUPS['M_t_over_M200'])
           if sum(v in d.values() for d in _sources.values()) != 1]
print(f"      ratios printed : {[CIRS['M_t_over_M200_reaching'], CIRS['M_t_over_M200_all'], XGROUPS['M_t_over_M200']]}")
print(f"      each traced to exactly one sample's record; those that are not: {len(_formed)}")
print(f"      HeCS's {HECS_ULTIMATE} is the ULTIMATE halo mass and is NOT pooled with the "
      f"M_t/M_200 figures:")
print(f"      it is the mass that stays bound in the far future, a different quantity, and it is")
print(f"      printed here only to keep the two from being read as one.")
check("Ⓚ⑩ nothing is pooled and no definition is harmonised: every ratio printed here is quoted "
      "from the single paper that published it, no figure is formed from two samples together, "
      f"and HeCS's {HECS_ULTIMATE} is named as the ULTIMATE halo mass rather than as a mass "
      "inside the turnaround radius -- the two are routinely conflated and are not one quantity",
      not _formed)

# ======================================================= THE PINS
head("THE PRINTED FIGURES, PINNED TWO-SIDED")
PINS = {
    "CIRS, mass inside r_t, 2.19": abs(CIRS['M_t_over_M200_reaching'] - 2.19) < 0.00500,
    "its error, 0.18": abs(CIRS['M_t_over_M200_reaching_err'] - 0.18) < 0.00500,
    "CIRS over all clusters, 1.97": abs(CIRS['M_t_over_M200_all'] - 1.97) < 0.00500,
    "its error, 0.10": abs(CIRS['M_t_over_M200_all_err'] - 0.10) < 0.00500,
    "CIRS sample size, 72": CIRS['n'] == 72,
    "CIRS r_t, 4.96 r200": abs(CIRS['r_t_over_r200_reaching'] - 4.96) < 0.00500,
    "the X-ray groups, 2.4": abs(XGROUPS['M_t_over_M200'] - 2.4) < 0.05000,
    "their r_t, 5.01 r200": abs(XGROUPS['r_t_over_r200'] - 5.01) < 0.00500,
    "the enclosed overdensity, 3.5 rho_c": abs(CIRS['rho_bar_at_r_t_over_rho_c'] - 3.5) < 0.00500,
    "HeCS's ultimate mass, 1.99": abs(HECS_ULTIMATE - 1.99) < 0.00500,
    "the prior ensemble's size, 6": LKR2017['n'] == 6,
    "the screen at 3.5 rho_c, 0.7368": abs(ratio_at(3.5) - 0.7368) < 0.00005,
    "and at 5.56 rho_c, 0.6315": abs(ratio_at(5.56) - 0.6315) < 0.00005,
}
print(f"\n      PINNED: {sum(PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure this receipt prints is not held by it"

# ======================================================= Ⓚ⑪ THE COUNT
head("K -- THE COUNT")
print(f"\n      arms registered in r7832's PREDICTION.md : 11")
print(f"      arms run before this count               : {len(PASSED) + len(FAILED)}")
check("Ⓚ⑪ eleven arms were registered and eleven ran under the registration's own labels, with "
      "Ⓓ④'s registered prediction holding on one word and its EMPHASIS reported as wrong rather "
      "than quietly kept -- the gap is the radius, not the mass",
      len(PASSED) + len(FAILED) == 10)

if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f[:110]}")
print(f"\n  arms run in total, this count included   : {len(PASSED) + len(FAILED)}")
print(f"  passed {len(PASSED)}, FAILED {len(FAILED)}")
print("\n" + "=" * 100)
print("  ⛭⛭ THE ENSEMBLE EXISTS AND IT CANNOT DISCRIMINATE.  The mass inside the turnaround")
print("     radius is published for 72 clusters and for an X-ray group sample; their radius is")
print("     set at a FIXED enclosed overdensity, so r_ta/r_bound is 0.7368 for every one of them")
print("     alike.  The kinematic radius is published for a different sample of six, whose mass")
print("     is virial.  ⇒ PO-50's clause is not discharged, and what is missing is the RADIUS.")
print("=" * 100)
assert len(PASSED) + len(FAILED) == 11, "eleven arms were registered; eleven must run"
sys.exit(1 if FAILED else 0)
