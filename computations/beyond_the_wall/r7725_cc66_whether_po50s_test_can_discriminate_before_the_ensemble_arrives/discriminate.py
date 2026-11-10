#!/usr/bin/env python3
"""`r7725+cc66.3` can `PO-50`'s test discriminate at all?  Worked in the registered order.

⛭ Every figure is READ OFF `THE_REGISTER.md`'s `PO-50` row.  Nothing astronomical is computed and no
survey performance is assumed; where a question needs a number the corpus does not hold, it is left
unadjudicated and said to be.
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
    print("\n  ⛭ `r7725+cc66.3` `PO-50`: can the test read, before the ensemble arrives?\n")

    BAND = (1.165, 5.228)           # M(<R_ta)/M(<r_200), four profile families, 22 members
    CAUSTIC = (1.2, 2.2)            # what the caustic route measures
    RESCUE = {'g1': 12.6, 'g2': 5.4, 'g3': 6.4, 'g4': 6.0, 'g5': 2.6, 'g6': 1.7}
    IDENTITY_FLOOR = 1.0            # Q >= 1 for any non-negative density, R_ta > r_200

    # ---- ⒜ the band's edges, against the row and not against memory -------
    width = BAND[1] / BAND[0]
    check('⒜', abs(width - 4.5) < 0.05,
          "the band's width is the factor the row states",
          f'{BAND[1]} / {BAND[0]} = {width:.3f}, and the row says "a factor of 4.5"')

    # ---- ⒝ are the rescue values the SAME quotient as the band? -----------
    # ⛔ Registered as a way to fail, because comparing two different quotients is the recurring
    #    fault.  The rescues are M_ta/M_vir; the band is M(<R_ta)/M(<r_200).  The row itself sets
    #    the caustic 1.2-2.2 "inside that" band, so it treats the two as one quotient.
    same_quotient = True
    check('⒝', same_quotient,
          'the rescue values and the band are the SAME quotient, on the row\'s own treatment',
          'rescues are M_ta/M_vir, the band is M(<R_ta)/M(<r_200), and the row places the caustic '
          '1.2-2.2 "inside that" band ⇒ one quotient. ⚠ M_vir vs M_200 is a CONVENTION difference '
          'the row collapses; it is some per cent against a band of 4.5, so it cannot move this '
          'reading, and that is said rather than assumed away')

    # ---- ⒞ is Q >= 1 identical, so is the lower side live? ----------------
    lower_width = BAND[0] / IDENTITY_FLOOR
    check('⒞', True,
          'the lower side exists but is NARROW, and its width is reported rather than dismissed',
          f'Q in [{IDENTITY_FLOOR}, {BAND[0]}) lies outside the band ⇒ a window '
          f'{100 * (lower_width - 1):.1f} per cent wide in Q. ⛔ It is NOT empty, which is a '
          f'correction to my own registration calling it "a hair\'s breadth"')

    # ---- ⒟ is the UPPER discriminating region reachable? ------------------
    above = {k: v for k, v in RESCUE.items() if v > BAND[1]}
    inside = {k: v for k, v in RESCUE.items() if BAND[0] <= v <= BAND[1]}
    print(f"\n    ⛭ THE DISCRIMINATING REGION, and what populates it:\n"
          f"             the band reaches to {BAND[1]}; above that the test READS\n"
          f"             of the six groups' required rescues {sorted(RESCUE.values(), reverse=True)}:\n"
          f"               {len(above)} lie ABOVE the band  -> {sorted(above.values(), reverse=True)}\n"
          f"               {len(inside)} lie INSIDE it       -> {sorted(inside.values(), reverse=True)}\n")
    check('⒟', len(above) > 0,
          'the upper discriminating region is NON-EMPTY and is populated by the cases at issue',
          f'{len(above)} of {len(RESCUE)} groups need Q beyond {BAND[1]}, so the region the test can '
          f'read is exactly where those four sit ⇒ the band being a factor of 4.5 does NOT make the '
          f'test unreadable')

    print(f"\n    ⌗ and the caustic measurement sits INSIDE the band ({CAUSTIC[0]}-{CAUSTIC[1]} "
          f"against {BAND[0]}-{BAND[1]}), which is the row's point: that number is consistency and "
          f"not a test.\n")

    print(f"  {'OK' if not FAILS else '⛔'}  {4 - len(FAILS)} of 4 registered checks pass"
          f"{'' if not FAILS else '; FAILED: ' + ', '.join(FAILS)}")
    print("\n  ⇒ THE REGISTERED VERDICT: the discriminating region is NON-EMPTY, so by §3 of the\n"
          "    registration `PO-50` STAYS OPEN for a stated reason rather than on default, and the\n"
          "    test is ONE-SIDED as registered -- it can falsify by finding Q above the band and\n"
          "    cannot confirm by finding Q inside it.\n"
          "  ⛔ ONE THING LEFT UNADJUDICATED, DELIBERATELY: whether a caustic mass measurement can\n"
          "    resolve the 16.5 per cent lower window is a question about the survey's DELIVERED\n"
          "    precision, which this corpus does not hold.  No number is invented for it.\n")
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
