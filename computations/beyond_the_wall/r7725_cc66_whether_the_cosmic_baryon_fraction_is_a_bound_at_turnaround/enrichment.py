#!/usr/bin/env python3
"""`r7725+cc66.2` the four registered checks on `PO-93`'s escape branch.

⛔ Registered in `PREDICTION.md`, pushed before this file existed.  ⒜–⒟ are that file's four named
ways this step reports FAILED rather than "inconclusive", worked in the order registered.

⛭ Every cluster number is a QUOTED LITERATURE VALUE, taken from node `60`'s `r7484` sample, which the
green receipt `P03_the_hubble_eddington_radius_tracks_the_dynamical_mass_on_virgo` runs unchanged.
**Nothing astronomical is computed here and nothing of 60's is re-derived**; the arithmetic is on
figures that receipt already pins.
"""
import sys

FAILS = []


def check(tag, ok, text, witness=''):
    print(f"    [{'PASS' if ok else 'FAIL'}] {tag}  {text}")
    if witness:
        print(f"             {witness}")
    if not ok:
        FAILS.append(tag)
    return ok


def main():
    print("\n  ⛭ `r7725+cc66.2` is the cosmic baryon fraction a BOUND at the turnaround radius?\n")

    # ---- the pinned figures, from the green receipt ------------------------
    R0 = (7.0, 7.8)                 # Mpc, the four kinematic determinations' span
    APERTURE = 3.4                  # Mpc, the scale the baryonic total is quoted on
    NEEDED = (1.70, 2.35)           # x the measured baryons, for the baryon-only bound to survive
    FRAC_OF_TOTAL = (0.33, 0.56)    # that, as a fraction of the measured total
    F_B_INSTRUMENT = 0.157          # the value 60's instrument uses
    F_B_PROSE = 0.18                # the value 60's RESULT.md prose states

    # ---- ⒜ is the baryonic mass really in a SMALLER aperture than R0? -----
    check('⒜', APERTURE < R0[0],
          'the baryonic mass is enclosed in a SMALLER aperture than R0, so the escape branch exists',
          f'aperture {APERTURE} Mpc against R0 = {R0[0]}-{R0[1]} Mpc; '
          f'ratio {R0[0] / APERTURE:.2f}-{R0[1] / APERTURE:.2f} in radius')

    # ---- ⒝ the background fraction: TWO numbers for one quantity ----------
    # ⛔ The registration named this before looking: which of the two is right is decided by
    #    whether it reproduces the SAME sample's own two derived figures, and not by preference.
    r_from_inst = F_B_INSTRUMENT ** (-1.0 / 3.0)
    l_from_inst = 1.0 / F_B_INSTRUMENT
    r_from_prose = F_B_PROSE ** (-1.0 / 3.0)
    l_from_prose = 1.0 / F_B_PROSE
    ok_inst = abs(r_from_inst - 1.85) < 0.005 and abs(l_from_inst - 6.4) < 0.05
    ok_prose = abs(r_from_prose - 1.85) < 0.005 and abs(l_from_prose - 6.4) < 0.05
    check('⒝', ok_inst and not ok_prose,
          'the background fraction is settled AGAINST THE SAME SAMPLE\'S OWN DERIVED FIGURES',
          f'f_b = {F_B_INSTRUMENT} gives radius factor {r_from_inst:.3f} and Lambda factor '
          f'{l_from_inst:.2f}, matching the printed 1.85 and 6.4; '
          f'f_b = {F_B_PROSE} gives {r_from_prose:.3f} and {l_from_prose:.2f}, matching neither '
          f'⇒ the "~18 per cent" in that RESULT.md prose is the stray, not the instrument')

    # ---- ⒞ is the region CLOSED? ------------------------------------------
    # ⛔ Registered as a way to FAIL, and it does not pass as stated.  The zero-velocity surface is
    #    a MEAN-FLOW boundary, not a one-way membrane: material on radial orbits can cross outward
    #    (backsplash).  So "nothing has left" is an idealisation.
    closed_exactly = False
    check('⒞', closed_exactly,
          'the accretion region is STRICTLY closed at r_ta  ⇒ IT IS NOT, and this is reported',
          'the zero-velocity surface bounds the MEAN flow; material on radial orbits crosses '
          'outward, so the enclosed mass at r_ta is not the whole accreted mass')

    # ---- ⒟ the enrichment factor the escape branch needs ------------------
    enrich = (FRAC_OF_TOTAL[0] / F_B_INSTRUMENT, FRAC_OF_TOTAL[1] / F_B_INSTRUMENT)
    print(f"\n    ⛭ THE REGISTERED QUANTITY -- the enrichment the escape branch requires:\n"
          f"             f_b(<R0) = {FRAC_OF_TOTAL[0]}-{FRAC_OF_TOTAL[1]} against a background "
          f"{F_B_INSTRUMENT}\n"
          f"             ⇒ ENRICHMENT FACTOR {enrich[0]:.2f} to {enrich[1]:.2f}\n"
          f"             (the baryons needed are {NEEDED[0]}-{NEEDED[1]}x those measured in the "
          f"{APERTURE} Mpc aperture)\n")
    # ⛔ NO THRESHOLD IS APPLIED.  The registration says the factor is REPORTED and that whether a
    #    patch-to-patch fluctuation of that size is available is a standard-cosmology question the
    #    corpus reads and does not own.  Inventing a bar here would be answering it myself.
    check('⒟', True,
          'the enrichment factor is computed exactly rather than quoted, and NOT adjudicated here',
          f'{enrich[0]:.2f}-{enrich[1]:.2f}x the background; whether a fluctuation that large is '
          f'available on a cluster-mass patch is not the corpus\'s question')

    print(f"\n  {'OK' if not FAILS else '⛔'}  {4 - len(FAILS)} of 4 registered checks pass"
          f"{'' if not FAILS else '; FAILED: ' + ', '.join(FAILS)}")
    print("\n  ⇒ ⒞ FAILS AS REGISTERED, so the step does NOT deliver the clean bound it was\n"
          "    registered to test.  What survives is weaker and is stated as such in VERDICT.md:\n"
          "    the leak's composition bias runs AGAINST the escape branch, because feedback expels\n"
          "    baryons preferentially and no process expels dark matter preferentially.  That makes\n"
          "    the background fraction a bound up to a correction of KNOWN SIGN -- not the exact\n"
          "    bound ⒞ would have given.\n")
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
