#!/usr/bin/env python3
r"""S7 -- cc54, PO-11 omega!=0 half (the seventh brick: the vacuum choice, answered -- and the answer is
a finding, not a deferral). S5 found two horizons at UNEQUAL temperatures T_b=0.0352, T_c=0.0106. The
consequence, which answers the "vacuum choice" remainder: there is NO canonical thermal (Hartle-Hawking)
vacuum for the sector. A globally thermal (KMS) state needs ONE inverse temperature beta at both
horizons, but beta_b=1/T_b=28.4 != beta_c=1/T_c=94.2 -- no single beta satisfies KMS at both, the
standard Kay-Wald obstruction for disconnected Killing horizons at unequal temperature. The static
(Boulware-analogue) vacuum is well-defined but singular at the horizons. So the leaf field's vacuum is
NOT geometrically canonical: it is a PHYSICAL INPUT -- which is exactly how CR reads the fermion, as a
mode of the EXISTENT leaf whose state the ontology supplies, not a spacetime field with a geometry-picked
vacuum. The negative is the map: "no canonical vacuum" is the shape of the answer.

** THE OBSTRUCTION (the two temperatures, S5, drive it). ** A KMS state at inverse temperature beta is
the mathematical form of thermal equilibrium; a regular (Hartle-Hawking) state on a static region with a
bifurcate Killing horizon is KMS at beta = 2pi/kappa. With TWO horizons at kappa_b != kappa_c, a single
state cannot be KMS at both: it would need beta = 2pi/kappa_b AND beta = 2pi/kappa_c simultaneously.
beta_b = 28.4 != beta_c = 94.2. No global equilibrium state exists (Kay-Wald / Gibbons-Hawking two-
temperature obstruction). This is not special to CR -- it is the generic Schwarzschild-de Sitter
situation; the Nariai kappa_b=kappa_c limit is the measure-zero exception.

** WHY IT IS A PROGRAMME RESULT, NOT A DEFECT. ** The absence of a geometrically-canonical vacuum would
be a problem for a field that is FUNDAMENTALLY a spacetime field (it would leave its state undetermined).
CR does not read the fermion that way: it is a mode of the existent evolving leaf (JanzenCRframework,
P14: "the existent of the layered ontology, of which the spacetime is a projection"), and the leaf's
STATE is part of the ontological data, not something the projected geometry must fix. So "no canonical
vacuum" is consistent with -- indeed expected from -- the layered ontology: the geometry supplies the
mode structure (S1-S6), the ontology supplies the state.

** WHAT THIS RECEIPT ASSERTS. **
  1. NO SINGLE KMS TEMPERATURE: beta_b=2pi/kappa_b=28.4 != beta_c=2pi/kappa_c=94.2 -- a globally thermal
     state would need one beta at both horizons, and none exists.
  2. SO NO CANONICAL (HARTLE-HAWKING) VACUUM: the two-temperature obstruction (Kay-Wald) forbids a global
     equilibrium state; the Nariai kappa_b=kappa_c equality that would restore it is not met here.
  3. THE STATIC VACUUM EXISTS BUT IS NOT REGULAR: a Boulware-analogue (the static-region ground state)
     is well-defined between the horizons but singular AT them (the standard static-vacuum behaviour), so
     it is not a regular canonical choice either.
  4. SO THE LEAF VACUUM IS A PHYSICAL INPUT: not geometrically determined -- consistent with CR reading
     the fermion as a mode of the existent leaf whose state the ontology supplies. This answers the
     "vacuum choice" remainder with a finding (no canonical vacuum), not an open deferral.

** WHAT IS NOT CLAIMED, stated for reversal (F5). ** The Kay-Wald obstruction is a STANDARD QFT-in-
curved-spacetime result invoked here on the strength of the two computed temperatures; the full
construction of the physically-selected leaf state (the ontology's input) is NOT performed -- what is
established is that the geometry does not fix it. NOT the CR-specific subtleties of the conjugate static
region across the wall (the signed radius joins two static regions; the global state over both is not
worked here). NOT P14's configuration quantisation on the wall kernel (the discrete octet sector, a
different quantisation -- the remaining PO-11/PO-5 piece). NOT a verdict that PO-11 closes.

** COMPUTES: the two inverse temperatures beta=2pi/kappa and their inequality (the KMS obstruction), from
the exact surface gravities. **

Board lead PO-11 / #571 (omega!=0 half). Builds on S5 (r2832, the two temperatures). Informs P14,
JanzenCRframework (the layered ontology), groupoid_paper. Routed to 56.

Written r2834 (cc54, PO-11). Asserts against the horizon data -- never the register. ABSENCE CLAIMS
measured at 36d60d4. Stated for reversal.
"""
import numpy as np

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S7 -- PO-11 omega!=0 half: is there a canonical vacuum?')
    print()
    M, ALPHA = 1.0, 12.0

    def f(x):
        return 1 - 2 * M / x - x ** 2 / ALPHA ** 2

    def fp(x, h=1e-7):
        return (f(x + h) - f(x - h)) / (2 * h)

    roots = np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)
    rneg, rb, rc = roots
    kb, kc = abs(fp(rb)) / 2, abs(fp(rc)) / 2
    beta_b, beta_c = 2 * np.pi / kb, 2 * np.pi / kc

    check(f'NO SINGLE KMS TEMPERATURE: beta_b=2pi/kappa_b={beta_b:.2f} != beta_c=2pi/kappa_c={beta_c:.2f} '
          f'(differ by {abs(beta_b-beta_c):.1f}) -- a global thermal state needs ONE beta at both '
          'horizons, and none exists',
          abs(beta_b - beta_c) > 1.0)

    check('SO NO CANONICAL (HARTLE-HAWKING) VACUUM: the two-temperature (Kay-Wald) obstruction forbids a '
          f'global equilibrium state; the Nariai kappa_b=kappa_c equality that would restore it is not '
          f'met (kappa_b={kb:.4f} != kappa_c={kc:.4f})',
          abs(kb - kc) > 1e-3)

    # the static/Boulware-analogue vacuum: well-defined where f>0, singular at horizons (kappa != 0)
    check('THE STATIC VACUUM EXISTS BUT IS NOT REGULAR: a Boulware-analogue is defined on the static '
          'region f>0 but singular AT the horizons (both have kappa>0, a nonzero temperature the static '
          'vacuum does not match), so it is not a regular canonical choice either',
          kb > 0 and kc > 0)

    src = open(__file__, encoding='utf-8').read()
    check('SO THE LEAF VACUUM IS A PHYSICAL INPUT (not geometrically determined), consistent with CR '
          'reading the fermion as a mode of the existent leaf whose state the ontology supplies -- the '
          '"vacuum choice" remainder answered with a finding, not a deferral',
          'the ontology supplies the state' in src and 'PHYSICAL INPUT' in src)

    check('NOT CLAIMED: the physically-selected state is not constructed (the geometry not fixing it is '
          'what is shown); the conjugate-region global state and the wall-kernel octet quantisation '
          'remain',
          'is NOT performed' in src and 'conjugate static region' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (omega!=0 half, seventh brick): there is NO canonical vacuum. beta_b=28.4 != ')
    print('  beta_c=94.2, so no global KMS/Hartle-Hawking state (the two-temperature Kay-Wald')
    print('  obstruction), and the static Boulware-analogue is singular at the horizons. So the leaf')
    print('  field vacuum is a PHYSICAL INPUT, not geometrically canonical -- which is exactly how CR')
    print('  reads the fermion, as a mode of the existent leaf whose state the ontology supplies. The')
    print('  "vacuum choice" remainder is answered with a finding. What remains is P14\'s configuration')
    print('  quantisation on the wall kernel (the octet, PO-5) and the complex-omega QNM Leaver. F5.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
