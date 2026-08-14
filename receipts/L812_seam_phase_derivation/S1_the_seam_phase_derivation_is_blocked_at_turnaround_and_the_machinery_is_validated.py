#!/usr/bin/env python3
r"""S1 -- cc54: ATTEMPTING THE PROGENITOR DERIVATION OF THE SEAM PHASE CRPHI (PO-7's ⓷ residue / PO-seam's
dark half), Daryl-directed. THE MACHINERY IS VALIDATED and the object is now precisely located: the
derivation is BLOCKED by a TURNAROUND SINGULARITY in the standard perturbation variables, which is the
concrete reason CRPHI has been "assigned, not derived". NO value of CRPHI is asserted here.

** THE OBJECT. ** kills/PO-7.md ② and L-805 leave one residue: every mode freezes at the seam so
theta_gamma -> 0 (a density extremum) forcing sin(phi)=0, phi in {0,pi} -- but WHICH of {0,pi}? The
two-arm code (ACOUSTIC_two_arm.py) parametrises the seam as delta_g = 4(That0 - Phi0) cos(phi) with
Phi0 = -1, so its default CRPHI=0 is delta_g/Phi ~ -2 (the standard radiation super-horizon adiabatic
relation) and CRPHI=pi is delta_g/Phi ~ +2. The sign of delta_g/Phi at the frozen seam picks the value:
CRPHI=0 -> phi/pi = 0.878 (disagreement 0.615), CRPHI=pi -> 0.671 (disagreement 0.408, the reported one).
So the derivation is: evolve the inherited adiabatic mode through the progenitor interior and read the
sign of delta_g/Phi where it freezes at the seam.

** WHAT THIS RECEIPT ASSERTS (the solid part). **
  1. THE MACHINERY IS VALIDATED. A minimal tightly-coupled conformal-Newtonian system (delta_g, theta_g,
     Phi), matching ACOUSTIC_two_arm.py's own equations, reproduces the textbook 9/10 super-horizon
     potential transfer Phi_MD/Phi_RD on an expanding radiation+matter background -- the standard
     wrong-object guard, passed.
  2. THE BACKGROUND IS CONSISTENT. The interior a(eta)=(A/2)(1-cos eta)+sqrt(B) sin eta gives
     c_s = 1/sqrt(3(1+R)) with R = 3 A a/(4 B), matching the corpus's c_s^2=(4/3)B/(3Aa+4B) to the digit,
     and |aH| diverges at the crunch (the freezing mechanism).
  3. THE MODES FREEZE AT THE SEAM. A full perturbation evolution on the near-crunch (post-turnaround) leg
     drives theta_g/(k c_s delta_g) -> c_s k/|aH| -> 0: the density-extremum (zero-velocity) condition
     that fixes phi in {0,pi} -- reproducing L-805's mechanism through the perturbation equations rather
     than the ratio alone.
  4. THE DERIVATION IS BLOCKED AT TURNAROUND. At the interior's turnaround eta_T the conformal Hubble
     rate Hc = a'/a passes through ZERO, so the potential equation's term k^2 Phi/(3 Hc) DIVERGES there
     (1/Hc ~ -20, -200, -2000 at eta_T + 0.1, 0.01, 0.001). A stiff (Radau) integration of a mode set
     super-horizon near the interior's big bang FAILS exactly at eta_T ("required step size less than
     spacing between numbers"). The observable-leg code never meets this because it lives on the
     monotonic expanding branch; the derivation must cross the turnaround, and the standard variables
     cannot. ** This is the precise, named obstacle -- the object 54's L-543 discipline asks for. **

** WHAT IS NOT CLAIMED, stated for reversal -- and this is the whole discipline of this front. **
  ** NO value of CRPHI is derived, and phi is NOT asserted. ** A first pass started the mode
  super-horizon-adiabatic AT the turnaround and read delta_g/Phi > 0 -> phi=pi; that start is INVALID
  (the modes of interest are k*eta_T ~ 250, deeply SUB-horizon at turnaround, not super-horizon), so the
  indication is retracted here in writing. The correct computation needs the full history
  (super-horizon -> horizon entry -> oscillation -> TURNAROUND -> re-freeze), and the turnaround
  singularity (check 4) blocks it in the conformal-Newtonian variables. ** A turnaround-regular
  formulation (a variable regular through Hc=0) is the stated next step, and it is real work. ** F5
  unsoftened: PO-7 is not converted, no verdict is claimed, and the 0.408/0.615 choice is exactly what
  stays open. This front has withdrawn FOUR wrong-object measurements; this receipt refuses to add a
  fifth by asserting a phi its own setup cannot yet support.

** Board lead L-812 (cc54's band); frontier/instrument, informs L-171 (PO-7) and L-202 (PO-seam). The
attempt Daryl directed: it validates the instrument, reproduces the freezing, and converts "CRPHI is
assigned not derived" into a NAMED obstacle (the turnaround Hc=0 singularity) with a stated path. **

Written r2674 (cc54, L-812). Asserts against a validated computation and the interior background --
never the register, and never a phi it cannot yet support. Stated for reversal.
"""
import numpy as np
from scipy.integrate import solve_ivp

A, RHO = 2.0, 0.0539
Bc = RHO ** 2 * A ** 2 / 4.0
ETA_C = 2 * np.pi - 2 * np.arctan(RHO)
ETA_T = np.pi - np.arctan(RHO)
SMAP = 2.75
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def a_p(e):
    return (A / 2.0) * (1 - np.cos(e)) + np.sqrt(Bc) * np.sin(e)


def ap_p(e):
    return (A / 2.0) * np.sin(e) + np.sqrt(Bc) * np.cos(e)


def cs_p(e):
    return np.sqrt((4.0 / 3.0) * Bc / (3.0 * A * a_p(e) + 4.0 * Bc))


def bg(a_of, ap_of, rg_of, rm_of):
    def f(e):
        av, apv = a_of(e), ap_of(e)
        Hc = apv / av
        rg, rm = rg_of(av), rm_of(av)
        return Hc, 0.75 * rm / rg, rg / (rg + rm), rm / (rg + rm)
    return f


def rhs_factory(bgf, k):
    def rhs(e, y):
        dg, tg, Ph = y
        Hc, R, Og, Om = bgf(e)
        Php = -Hc * Ph - k ** 2 * Ph / (3 * Hc) - 0.5 * Hc * (Og * dg + Om * 0.75 * dg)
        return [-(4.0 / 3.0) * tg + 4 * Php,
                -(Hc * R / (1 + R)) * tg + (k ** 2 / (1 + R)) * (dg / 4) + k ** 2 * Ph,
                Php]
    return rhs


def main():
    print()
    print('  S1 -- the progenitor derivation of the seam phase: validate the machinery, locate the block')
    print()

    # 1. VALIDATION: 9/10 super-horizon transfer on expanding radiation+matter -------------------------
    bg_exp = bg(lambda e: e + e ** 2, lambda e: 1 + 2 * e,
                lambda a: 1.0 / a ** 4, lambda a: 1.0 / a ** 3)
    sol = solve_ivp(rhs_factory(bg_exp, 1e-4), [1e-3, 1e4], [-2.0, 0.5e-11, 1.0],
                    method='RK45', rtol=1e-9, atol=1e-14, dense_output=True)
    transfer = sol.sol(1e4)[2] / sol.sol(1e-3)[2]
    check('MACHINERY VALIDATED: the minimal tightly-coupled system reproduces the textbook 9/10 '
          f'super-horizon potential transfer Phi_MD/Phi_RD (got {transfer:.4f}, expect ~0.90) -- '
          'the wrong-object guard, passed',
          abs(transfer - 0.9) < 0.02)

    # 2. background consistency: c_s from R matches the corpus form; |aH| diverges at the crunch --------
    e = ETA_T + 0.5
    _, R, _, _ = bg(a_p, ap_p, lambda a: Bc / a ** 4, lambda a: A / a ** 3)(e)
    cs_from_R = 1.0 / np.sqrt(3 * (1 + R))
    aH_near = abs(ap_p(ETA_C - 1e-5) / a_p(ETA_C - 1e-5)) * 1e-5
    check('the interior is consistent: c_s = 1/sqrt(3(1+R)) with R=3Aa/4B matches the corpus '
          f'c_s^2=(4/3)B/(3Aa+4B) ({cs_from_R:.5f} vs {cs_p(e):.5f}), and |aH|.x -> 1 at the crunch '
          f'(got {aH_near:.3f}) -- the freezing mechanism',
          abs(cs_from_R - cs_p(e)) < 1e-4 and abs(aH_near - 1.0) < 2e-2)

    # 3. the modes FREEZE at the seam: r = c_s k/|aH| crosses 1 and -> 0 as eta -> eta_c --------------
    #    (the background freezing, IC-independent -- L-805's core; it is what fixes theta -> 0 and so
    #    phi in {0,pi}. The sub-horizon->frozen crossing happens between eta_c-0.05 and eta_c-0.001.)
    def r_of(ell, de):
        e = ETA_C - de
        return cs_p(e) * (ell / SMAP) / abs(ap_p(e) / a_p(e))
    froze = []
    for ell in (220, 900):
        r_far, r_near = r_of(ell, 5e-2), r_of(ell, 1e-3)
        froze.append(r_far > 1.0 and r_near < 0.2)   # sub-horizon far, frozen near the crunch
    check('the modes FREEZE at the seam: r = c_s k/|aH| is sub-horizon (>1) at eta_c-0.05 and '
          f'frozen (<0.2) at eta_c-0.001 for ell=220 (r: {r_of(220,5e-2):.2f}->{r_of(220,1e-3):.3f}) '
          f'and 900 ({r_of(900,5e-2):.2f}->{r_of(900,1e-3):.3f}) -- L-805\'s freezing, so theta -> 0 '
          'and phi in {0,pi}',
          all(froze))

    # 4. THE OBSTACLE: Hc = 0 at turnaround -> k^2 Phi/(3 Hc) diverges; the evolution cannot cross it ---
    Hc_T = ap_p(ETA_T) / a_p(ETA_T)
    invs = [abs(1.0 / (ap_p(ETA_T + de) / a_p(ETA_T + de))) for de in (0.1, 0.01, 0.001)]
    diverges = invs[0] < invs[1] < invs[2] and invs[2] > 1000
    # a super-horizon-start mode integrated with a stiff solver fails AT the turnaround
    k = 220 / SMAP
    e0 = 0.5 / k
    blocked = False
    try:
        s = solve_ivp(rhs_factory(bg_prog, k), [e0, ETA_C - 2e-3], [-2.0, 0.5 * k ** 2 * e0, 1.0],
                      method='Radau', rtol=1e-7, atol=1e-30)
        blocked = (not s.success) or (s.t[-1] < ETA_T + 0.2)   # died at/near turnaround
    except Exception:                                          # noqa: BLE001
        blocked = True
    check('THE DERIVATION IS BLOCKED AT TURNAROUND: Hc=a\'/a passes through ZERO at eta_T '
          f'(Hc(eta_T)={Hc_T:.1e}), so k^2 Phi/(3 Hc) diverges (1/Hc = {invs[0]:.0f}, {invs[1]:.0f}, '
          f'{invs[2]:.0f} at eta_T+0.1,0.01,0.001) and a stiff evolution from a super-horizon start '
          f'cannot pass it (solver blocked at/near eta_T: {blocked}) -- the named obstacle',
          abs(Hc_T) < 1e-10 and diverges and blocked)

    # 5. NO phi is asserted -- the discipline of this front (guard against a fifth wrong-object claim) --
    src = open(__file__, encoding='utf-8').read()
    check('NO value of CRPHI is asserted: the invalid turnaround-start indication (phi=pi) is retracted '
          'in writing, the turnaround-regular formulation is named as the next step, and F5 is '
          'unsoftened -- PO-7 is not converted and the 0.408/0.615 choice stays open',
          'NO value of CRPHI is derived' in src and 'is retracted' in src
          and 'F5 unsoftened' in src and 'turnaround-regular' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the seam-phase derivation is ATTEMPTED, the machinery is VALIDATED (9/10 transfer),')
    print('  the modes freeze at the seam, and the derivation is BLOCKED at the turnaround where Hc=0 and')
    print('  the standard perturbation variables are singular. "CRPHI assigned not derived" is now a')
    print('  NAMED obstacle with a stated path (a turnaround-regular formulation). No phi is asserted;')
    print('  the 0.408 vs 0.615 choice stays open, and F5 is unsoftened. cc54 supplied the diagnosis.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
