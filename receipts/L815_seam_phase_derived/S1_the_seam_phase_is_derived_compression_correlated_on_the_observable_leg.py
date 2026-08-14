#!/usr/bin/env python3
r"""S1 -- cc54, PO-7 / PO-seam: THE SEAM PHASE CRPHI IS DERIVED, NOT FREE -- it is CRPHI=0 (a compression
correlated with the potential well), on the OBSERVABLE leg, bracket-checked against the standard adiabatic
mode. This closes PO-7's inversion route ⓷ (the seam datum acquires a derivation) and collapses the {0,pi}
freedom to a single value. It does NOT convert PO-7 (F5): it supplies the derivation, not the verdict.

** WHY THIS IS NOW DERIVABLE, AND WHY L-812 WAS LOOKING IN THE WRONG PLACE. ** L-812 tried to evolve the
inherited mode through the progenitor CONTRACTING leg and hit the turnaround Hc=0 singularity. r2701 /
CR_cosmology.tex sec:what-crosses retires that route as EMPTY, not merely blocked: the collapse-leg
acoustic phase does NOT cross (only amplitude and tilt do, L-805/L-806), and "the potential equation for a
pressureless component contains no k at all once w=0 ... the problem on the observable leg is scale-free,
and a scale-free problem imprints nothing." So the phase is set at/after ONSET, on the monotonic expanding
(observable) leg -- where there is no singularity.

** THE RESIDUE IS ONE SIGN, AND THE CODE NAMES BOTH ENDS. ** The two admissible values are the two signs
of delta_gamma/Phi at the seam (ACOUSTIC_two_arm.py: Ph0=-1, That0=-T(xe)/2, dg0=4(That0-Ph0)cos(CRPHI)):
  CRPHI=0  -> dg0 = +2.07, delta_g>0 in a well (Phi<0): an OVERDENSITY, "a compression correlated with the
             well" (CR_cosmology.tex:940) -> phi/pi = 0.878, disagreement 0.615;
  CRPHI=pi -> dg0 = -2.07, delta_g<0 in a well: an UNDERDENSITY, "a rarefaction against it" -> 0.671,
             disagreement 0.408 (the band's nearest approach).
So the derivation is exactly: is the inherited seam perturbation an OVERDENSITY in the well (adiabatic,
CRPHI=0) or an UNDERDENSITY (anti-adiabatic, CRPHI=pi)?

COMPUTES: the code's seam-phase convention (which CRPHI is an overdensity in the well) and the sign of
delta_g/Phi a pressureless vs a pressured pre-onset delivers to the seam. ** CRPHI here is the DERIVED
output (=0), not a pinned input scope: the receipt evaluates both admissible values (0 and pi) from the
code and shows the physics selects 0. **

** THE DERIVATION. ** (i) The amplitude and tilt cross the seam unaltered as ADIABATIC boundary data
("inherited ... exactly as flat LCDM inherits the baryon-to-photon ratio", CR_cosmology.tex); a standard
adiabatic perturbation is an OVERDENSITY sitting in a potential WELL (delta_g = -2Phi super-horizon:
delta_g>0 where Phi<0). (ii) The pre-onset is PRESSURELESS (c_s=0 identically), so there is NO acoustic
oscillation to swing that sign: a pressureless mode does not oscillate, it keeps the overdensity it
inherited. (iii) At onset the pressure turns on and the mode -- an overdensity at rest (theta_g=0) -- begins
to oscillate from a compression: CRPHI=0. ** It is precisely r2701's pressureless pre-onset that pins the
sign: with pressure the phase would swing through both signs (a k-dependent free datum), which is why the
datum READ as free before the pre-onset was shown pressureless. **

** THE BRACKET (checkable INDEPENDENT of the phase number it yields). ** The standard adiabatic mode --
the LambdaCDM control's OWN initial condition (ARM=lcdm "adiabatic super-horizon initial data") -- is an
overdensity in a well, delta_g=-2Phi, which is delta_g/Phi<0 = CRPHI=0 by the code's convention. The CR
seam inherits the SAME sign (adiabatic amplitude + pressureless no-oscillation), so the reading is checked
against a known case, not against 0.878-vs-0.671.

** WHAT THIS RECEIPT ASSERTS. **
  1. THE CODE CONVENTION: CRPHI=0 is delta_g/Phi<0 (overdensity in a well, compression correlated);
     CRPHI=pi is delta_g/Phi>0 (underdensity, rarefaction anti-correlated) -- computed from That0, Ph0.
  2. PRESSURELESS PINS THE SIGN: a c_s=0 perturbation started as an overdensity does NOT oscillate (its
     sign is fixed), while a pressured (c_s^2=1/3) one swings through both signs -- so only the pressureless
     pre-onset makes the seam sign determinate.
  3. THE ADIABATIC BRACKET: an overdensity in a well is delta_g/Phi<0 = CRPHI=0, and that is the LambdaCDM
     control's own adiabatic IC -- the independent check.
  4. THE VERDICT: the seam inherits an adiabatic overdensity in a well and does not oscillate before the
     seam, so CRPHI=0; the {0,pi} freedom collapses to 0, the disagreement is pinned at 0.615 (the corpus's
     PRIMARY value), and CRPHI=pi (0.408, an underdensity/rarefaction) is anti-adiabatic and INADMISSIBLE.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT a conversion of PO-7 -- F5 forbids a node closing it;
this supplies the derivation route ⓷ asked for and Daryl authorises. NOT a NEW disagreement -- 0.615 is the
corpus's already-primary reading; what is new is that the phase is DERIVED (compression correlated),
collapsing the band rather than leaving a [0.408, 0.615] range. THE ONE ASSUMPTION, flagged: the potential
Phi does not flip sign across the onset (standard pressureless/matter evolution preserves it; a CR onset
that inverted the potential would flip the correlation) -- checkable, and stated for reversal. NOT a claim
that this reduces to L-812's retracted phi=pi -- that pass evaluated the adiabatic relation at the
turnaround (deeply sub-horizon, k*eta_T~250) and is retracted; this evaluates the sign at the seam via the
pressureless no-oscillation argument, which is where the mode actually is.

** Board lead L-815 (cc54's band); closes PO-7 inversion route ⓷'s residue (the progenitor/seam CRPHI
derivation), PO-seam's dark half. Informs L-171 (PO-7), L-202 (PO-seam). The unhold condition Daryl/56 set
-- a sign checkable independent of the number, via a bracket -- is met by the observable-leg route. **

Written r2674 (cc54, L-815). Asserts against ACOUSTIC_two_arm.py's convention, CR_cosmology.tex
sec:what-crosses, and the pressureless/pressured ODE contrast -- never the register. Stated for reversal.
"""
import os

import numpy as np
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- is the seam phase CRPHI derived (compression correlated, CRPHI=0) on the observable leg?')
    print()

    # 1. the code convention: CRPHI=0 <-> overdensity in a well (delta_g/Phi<0)
    xe = 1.0 / np.sqrt(3.0)
    Txe = 3 * (np.sin(xe) - xe * np.cos(xe)) / xe ** 3
    That0 = -Txe / 2.0
    Ph0 = -1.0
    dg0 = {phi: 4 * (That0 - Ph0) * np.cos(phi) for phi in (0.0, np.pi)}
    r0 = {phi: dg0[phi] / Ph0 for phi in (0.0, np.pi)}
    check('CODE CONVENTION: CRPHI=0 gives delta_g>0 in a well (overdensity, delta_g/Phi<0, "compression '
          f'correlated") and CRPHI=pi gives delta_g<0 (underdensity, delta_g/Phi>0, "rarefaction") '
          f'(dg0/Phi: CRPHI=0 -> {r0[0.0]:+.2f}, CRPHI=pi -> {r0[np.pi]:+.2f})',
          dg0[0.0] > 0 and r0[0.0] < 0 and dg0[np.pi] < 0 and r0[np.pi] > 0)

    # 2. pressureless pins the sign (no oscillation); pressure swings it
    def evolve(cs2, e_end=60.0, k=0.3):
        def rhs(e, y):
            dg, v = y
            return [v, -(k ** 2 * cs2) * dg]
        s = solve_ivp(rhs, [0, e_end], [1.0, 0.0], rtol=1e-10, atol=1e-13,
                      dense_output=True, max_step=0.2)
        ee = np.linspace(0, e_end, 4000)
        dg = s.sol(ee)[0]
        return int((np.diff(np.sign(dg)) != 0).sum()), dg.min(), dg.max()
    n_p, lo_p, hi_p = evolve(0.0)
    n_g, lo_g, hi_g = evolve(1.0 / 3.0)
    check('PRESSURELESS PINS THE SIGN: a c_s=0 mode started as an overdensity does NOT oscillate '
          f'({n_p} zero-crossings, delta_g stays [{lo_p:+.2f},{hi_p:+.2f}], sign fixed), while a pressured '
          f'c_s^2=1/3 mode SWINGS through both signs ({n_g} zero-crossings, [{lo_g:+.2f},{hi_g:+.2f}]) -- '
          'so only the pressureless pre-onset (r2701) makes the seam sign determinate',
          n_p == 0 and n_g >= 2 and lo_g < 0 < hi_g)

    # 3. the adiabatic bracket: overdensity in a well is CRPHI=0, = the LCDM control's IC
    #    a pressureless mode started at the adiabatic delta_g/Phi=-2 keeps delta_g/Phi<0 to the seam
    def rhs_p(e, y, k=0.3):
        dg, tg = y
        Phi = -1.0
        Rbig = 1e6
        return [-(4 / 3) * tg, (k ** 2 / (1 + Rbig)) * (dg / 4) + k ** 2 * Phi]
    sol = solve_ivp(lambda e, y: rhs_p(e, y), [0, 20], [-2 * (-1.0), 0.0],
                    rtol=1e-9, atol=1e-12)
    r_seam = sol.y[0, -1] / (-1.0)
    check('THE ADIABATIC BRACKET: the standard adiabatic mode (delta_g=-2Phi, the LambdaCDM control\'s own '
          'IC) is an overdensity in a well -> delta_g/Phi<0 = CRPHI=0; the pressureless CR seam keeps that '
          f'sign (started -2, arrives delta_g/Phi = {r_seam:+.1f} < 0) -- SAME side, bracket-checked',
          r_seam < 0)

    # 4. the corpus supports the pressureless onset and the open first-peak position
    tex = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
               errors='replace').read()
    check('THE CORPUS SUPPORTS THE ROUTE: the onset matter is pressureless and the pre-onset problem is '
          '"scale-free" and "imprints nothing", leaving "the first peak\'s position ... open" -- exactly '
          'the residue this derivation closes',
          'pressureless' in tex and 'scale-free' in tex
          and ('imprints nothing' in tex or 'imprints nothing' in tex.replace('\n', ' '))
          and 'compression correlated with the well' in tex)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-7 route ⓷ residue closed, not converted): the seam phase CRPHI is DERIVED = 0 --')
    print('  the seam inherits an adiabatic OVERDENSITY in the potential well (amplitude/tilt cross')
    print('  unaltered), and the PRESSURELESS pre-onset gives it no oscillation to flip the sign, so it is')
    print('  a compression correlated with the well = CRPHI=0. Bracket-checked against the LambdaCDM')
    print('  control\'s own adiabatic IC. The {0,pi} band collapses to 0.878, the disagreement is pinned at')
    print('  0.615 (the corpus\'s primary value), and CRPHI=pi (0.408, a rarefaction) is anti-adiabatic and')
    print('  inadmissible. F5 unsoftened: cc54 supplied the derivation; the verdict is Daryl\'s. One')
    print('  assumption flagged: Phi does not flip sign across the onset.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
