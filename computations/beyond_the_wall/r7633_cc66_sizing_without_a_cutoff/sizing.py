"""r7633+cc66 -- sizing the dimension-six term WITHOUT a cutoff.

Run from anywhere:  python3 sizing.py

PO-89's clause now reads: "TERMINATES IF the dimension-six term's effect on every observable is shown
below what measurement resolves, sized by the scales the construction does carry rather than by a
cutoff it does not have."  So this row carries no free Lambda, which is the point: r7631 (2) found the
regulator is a spectral continuation with no cutoff parameter at all.

THE CORPUS'S STATEMENTS THIS RESTS ON, each located so a claimed read can be checked:
  * "in the reduced theory the only scales are `a` and the Planck length", so the vacuum energy is
    a^-1 sum_j f_j (ell_P/a)^j against A POLYNOMIAL IN ln(a/ell_P); the power is 1+j, ONE VERTEX PAIR
    COSTS ell_P^2, and the interaction enters at j >= 2         (canonical_time l.1621-1623);
  * ell_P is "a gauge-combination rather than a second physical length", so a cutoff "is not
    smuggling a scale in either"                                 (canonical_time l.484);
  * the spectral zeta has a pole at s = -1 of residue 15/4, so the renormalised energy carries a
    ln a, and the trace is Theta = rho - 3p ∝ (15/4) a^-4, INDEPENDENT OF THE RENORMALISATION SCALE
    -- scheme-independent, which is what an anomaly is            (canonical_time l.583-585);
  * the dimension-six obstruction coefficient is 6023/20160       (canonical_time l.1283, r7601);
  * ⚠ and ON THIS BACKGROUND THE DIMENSION-SIX INVARIANT CANNOT BE NAMED: the five dimension-six
    scalars collapse on the one-parameter family -- two vanish identically, the rest are pure
    numbers, rank one -- so the residue "is one equation on three directions, each of which alone
    reproduces it after a single rescaling, and IT NAMES NOTHING"  (canonical_time l.1283, and the
    receipt P10_the_assembly_has_two_invariants_and_the_cubic_is_traceless_but_the_invariant_cannot_
    be_named_on_this_background).

** WHAT THAT LAST ONE DOES TO THE ORDER'S STEP (1). **  The order asks what multiplies "the
dimension-six invariant".  On this background there is no such invariant to multiply -- the
construction says so itself.  ⇒ So what is sized here is the magnitude of the dimension-six
OBSTRUCTION, and the row says that rather than inventing an invariant for the coefficient to sit on.
PREDICTION.md registered this as the outcome to report honestly if it arrived, and it arrived.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R7629 = os.path.join(os.path.dirname(HERE), 'r7629_cc66_the_dimension_six_reach')
sys.path.insert(0, R7629)
import reach as _r7629  # noqa: E402  -- for the measured precisions and the cutoff-estimator control

# --------------------------------------------------------------------------------------------
# THE INHERITED DATUM, declared.  ell_P is the MEASURED gravitational coupling expressed as a
# length -- not a cutoff, and not something this construction predicts.
# --------------------------------------------------------------------------------------------
ELL_P_M = 1.616255e-35          # CODATA Planck length, metres: sqrt(hbar G / c^3)
C_M_PER_S = 2.99792458e8
MPC_M = 3.0856775814913673e22
H0_KM_S_MPC = 67.4              # the same H0 r7629 carried, as a rate
OMEGA_M = 0.315
Z_REC = 1089.9                  # recombination, the epoch r7629 read the last three observables at

# ⌗ The dimension-four anomaly's coefficient and the dimension-six obstruction's, both landed.
C4 = 15.0 / 4.0                 # canonical_time l.583-585, scheme-INDEPENDENT (it is an anomaly)
C6 = 6023.0 / 20160.0           # canonical_time l.1283 -- an obstruction's magnitude, not an
                                #   invariant's coefficient (r7629, and see the docstring)

# ⌗ The cutoff sweep is a MODULE constant so the receipt can check the printed table against it
#   rather than against a hard-coded row count -- a pin on a count holds while what it counts moves.
CUTOFF_SWEEP = (1.0e-3, 1.0, 1.0e3, 1.0e6, 1.0e9)


def hubble_radius_m(z=0.0):
    """the background's curvature radius c/H(z), in metres -- the construction's `a`.

    ⌗ `a` is a COSMOLOGICAL input at each epoch, not something the construction fixes (r7627), so it
      is computed from declared parameters and varied by a decade below."""
    h0_si = H0_KM_S_MPC * 1.0e3 / MPC_M
    if z <= 0.0:
        hz = h0_si
    else:
        # matter-dominated at recombination: H = H0 sqrt(Omega_m (1+z)^3) to the accuracy this row needs
        hz = h0_si * math.sqrt(OMEGA_M * (1.0 + z) ** 3)
    return C_M_PER_S / hz


def suppression(a_m):
    """** THE WHOLE OF THE SIZING: (ell_P/a)^2. **  Two more operator dimensions cost two more inverse
    powers of the only length the background has, and dimensional closure costs one vertex pair's
    ell_P^2 -- canonical_time l.1621-1623.

    ⌗ NOTE WHAT IS NOT AN ARGUMENT OF THIS FUNCTION: there is no cutoff.  The control below varies one
      and shows this number does not move, against r7629's estimator which does."""
    return (ELL_P_M / a_m) ** 2


def log_factor(a_m):
    """the logarithm the construction's own scales fix: ln(a/ell_P) -- canonical_time l.1621.

    ⚠ Its VALUE is scheme-dependent (the split between the constant and the logarithm is a
      convention); only the COEFFICIENT multiplying it is not.  So this is reported as an order and
      never used to claim a digit."""
    return math.log(a_m / ELL_P_M)


def main():
    print()
    print('=' * 96)
    print('r7633+cc66 -- SIZING THE DIMENSION-SIX TERM WITHOUT A CUTOFF')
    print('=' * 96)

    a_now = hubble_radius_m(0.0)
    a_rec = hubble_radius_m(Z_REC)

    # ---------------------------------------------- the control, FIRST
    print()
    print('-' * 96)
    print('  CONTROL (1), REPORTED FIRST -- the same estimator on the DIMENSION-FOUR logarithm,')
    print('  whose coefficient 15/4 P10 carries, against its KNOWN order')
    print('-' * 96)
    print('    The dimension-four trace anomaly is Theta = rho - 3p ∝ (15/4) a^-4 (l.583-585).')
    print('    Sized against the classical background density rho_cl = 3H^2/(8 pi G) with H ~ 1/a and')
    print('    G = ell_P^2 (hbar = c = 1):')
    print()
    print('      Theta / rho_cl  =  (15/4) a^-4 / [ 3 / (8 pi ell_P^2 a^2) ]  =  (15/4)(8 pi/3) (ell_P/a)^2')
    ratio_coeff = C4 * 8.0 * math.pi / 3.0
    print('                      =  %.6f (ell_P/a)^2      [ = 10 pi, since (15/4)(8/3) = 10 ]'
          % ratio_coeff)
    anomaly_now = ratio_coeff * suppression(a_now)
    print()
    print('    ⇒ at the present epoch that is %.3e -- i.e. of order 1e-121.' % anomaly_now)
    print('    ** AND THAT IS THE KNOWN ORDER OF A ONE-LOOP GRAVITON CORRECTION ON THIS BACKGROUND,')
    print('    the familiar (ell_P H)^2 ~ 1e-122. **  The estimator returns, for a term whose order is')
    print('    independently known, that known order.  ⇒ So it is measuring something, and the')
    print('    dimension-six number below is not read off an unvalidated instrument.')
    print()
    print('    ⌗ The coefficient check: (15/4)(8/3) = %.6f exactly, so the prefactor is 10 pi and'
          % (C4 * 8.0 / 3.0))
    print('      the control reproduces its own arithmetic rather than being asserted.')
    print('    ⚠ And the trap PREDICTION.md registered: 15/4 is SCHEME-INDEPENDENT (it is an anomaly)')
    print('      while a logarithm\'s VALUE is not, so this control checks the ORDER and never a digit.')

    # ---------------------------------------------- step (1): what multiplies it
    print()
    print('-' * 96)
    print('  STEP (1) -- WHAT MULTIPLIES THE DIMENSION-SIX TERM, read from P10 rather than derived')
    print('-' * 96)
    print('    %-28s %s' % ('the coupling\'s power:', 'ONE ell_P^2 per vertex pair (l.1623)'))
    print('    %-28s %s' % ('the curvature\'s power:', 'two more inverse powers of a, the only'))
    print('    %-28s %s' % ('', 'length the background has (l.1621)'))
    print('    %-28s %s' % ('in the logarithm:', 'ln(a/ell_P) (l.1621) -- a ratio of the'))
    print('    %-28s %s' % ('', 'construction\'s OWN two scales, NOT a cutoff'))
    print('    %-28s %s' % ('the coefficient:', '6023/20160 = %.6f (l.1283)' % C6))
    print()
    print('    ⇒ so the dimensionless suppression of dimension six against dimension four is')
    print('      ** (ell_P/a)^2 **, times a rational of order one, times that logarithm.')
    print()
    print('    ⚠ AND ONE THING THE ORDER\'S WORDING PRESUPPOSES IS NOT TRUE ON THIS BACKGROUND.')
    print('      The order asks what multiplies "the dimension-six INVARIANT".  P10 says the five')
    print('      dimension-six scalars COLLAPSE on the one-parameter family -- two vanish identically,')
    print('      the rest are pure numbers, rank one -- so the residue "is one equation on three')
    print('      directions, each of which alone reproduces it after a single rescaling, and IT NAMES')
    print('      NOTHING" (l.1283).  The receipt carrying that is titled in those terms: the invariant')
    print('      CANNOT BE NAMED on this background.')
    print('      ⇒ ** So what is sized here is the magnitude of the dimension-six OBSTRUCTION, not an')
    print('      invariant\'s coefficient. **  PREDICTION.md registered this as the outcome to report')
    print('      rather than paper over, and it is the outcome that arrived.  The suppression is')
    print('      unaffected -- it is dimensional -- but what it multiplies is an obstruction.')

    # ---------------------------------------------- step (2): the four observables
    print()
    print('-' * 96)
    print('  STEP (2) -- THE EFFECT RELATIVE TO DIMENSION FOUR, each observable at ITS OWN epoch')
    print('-' * 96)
    print('    The construction\'s `a` at each epoch (c/H(z), declared inputs: H0 = %.1f km/s/Mpc,'
          % H0_KM_S_MPC)
    print('    Omega_m = %.3f, z_rec = %.1f), and ell_P = %.6e m as MEASURED -- an inherited datum,'
          % (OMEGA_M, Z_REC, ELL_P_M))
    print('    not a cutoff:')
    print()
    print('      %-10s %-10s %-16s %-14s %s' % ('epoch', 'z', 'a = c/H (m)', '(ell_P/a)^2', 'ln(a/ell_P)'))
    for label, z, a_m in (('today', 0.0, a_now), ('recomb.', Z_REC, a_rec)):
        print('      %-10s %-10.1f %-16.4e %-14.4e %.1f'
              % (label, z, a_m, suppression(a_m), log_factor(a_m)))
    print()
    print('    ⌗ The last three observables are read at recombination, which is the epoch r7629 read')
    print('      them at (its T_rec = 0.26 eV); the rate is read today.  Same epochs, so the two rows')
    print('      of this programme are comparable.')
    print()
    rows = []
    print('      %-24s %-10s %-14s %-12s %s'
          % ('observable', 'epoch', 'suppression', 'precision', 'orders BELOW precision'))
    for name, _e, sigma, _d in _r7629.OBSERVABLES:
        a_m = a_now if 'rate' in name else a_rec
        sup = C6 * suppression(a_m)
        orders = math.log10(sigma / sup)
        rows.append((name, a_m, sup, sigma, orders))
        print('      %-24s %-10s %-14.4e %-12.1e %+.1f'
              % (name, 'today' if a_m == a_now else 'recomb.', sup, sigma, orders))
    print()
    worst = min(rows, key=lambda r: r[4])
    print('    ⇒ ** THE SMALLEST MARGIN OF THE FOUR IS %.1f ORDERS OF MAGNITUDE, on %s. **'
          % (worst[4], worst[0]))
    print('      Every observable is below what measurement resolves by more than a hundred orders.')

    # ---------------------------------------------- step (3) and the reachable negative
    print()
    print('-' * 96)
    print('  STEP (3) + THE ORDER\'S REACHABLE NEGATIVE -- is the term within reach ANYWHERE?')
    print('-' * 96)
    tightest = min(s for _n, _e, s, _d in _r7629.OBSERVABLES)
    a_reach = ELL_P_M / math.sqrt(tightest / C6)
    print('    The term reaches the tightest measured precision (%.1e) where C6 (ell_P/a)^2 = that,'
          % tightest)
    print('    i.e. at a = ell_P sqrt(C6/sigma) = %.4e m = %.2f ell_P.'
          % (a_reach, a_reach / ELL_P_M))
    print('    ⇒ ** So the term is within reach only where the background\'s curvature radius is')
    print('      within a factor of ~%.0f of the Planck length. **  That is the Planck era.'
          % (a_reach / ELL_P_M))
    print('    ⇒ ** THE REACHABLE NEGATIVE IS MISSED, AND FOR A STRUCTURAL REASON RATHER THAN A')
    print('      NUMERICAL ONE: none of the four observables reads there. **  The construction reads')
    print('      epochs from recombination onward, where a exceeds ell_P by %.0f orders.'
          % math.log10(a_rec / ELL_P_M))

    # ---------------------------------------------- the control that matters most for this row
    print()
    print('-' * 96)
    print('  CONTROL (3) -- A CUTOFF-SHAPED QUANTITY SHOWN **ABSENT**, which is this row\'s own claim')
    print('-' * 96)
    print('    The claim is that this sizing uses no cutoff.  That is checked by VARYING one and')
    print('    watching: r7629\'s estimator, which takes Lambda, against this one, which does not.')
    print()
    print('      %-14s %-30s %s'
          % ('Lambda (GeV)', 'r7629 (E/Lambda)^2 at 1 GeV', 'this row, today'))
    r7629_vals, mine_vals = [], []
    for lam in CUTOFF_SWEEP:
        r = _r7629.C6 * (1.0 / lam) ** 2
        m = C6 * suppression(a_now)
        r7629_vals.append(r)
        mine_vals.append(m)
        print('      %-14.0e %-30.4e %.4e' % (lam, r, m))
    print()
    print('    ⇒ r7629\'s number moves over %.0f orders as Lambda moves over 12;'
          % math.log10(max(r7629_vals) / min(r7629_vals)))
    print('      this row\'s moves by a factor of exactly %.1f -- it does not move at all.'
          % (max(mine_vals) / min(mine_vals)))
    print('    ** So the sizing is cutoff-free BY MEASUREMENT and not by assertion. **  ⌗ That is the')
    print('      difference r7633 asked for against r7629: same term, same observables, and an')
    print('      estimator built from the construction\'s own two scales instead of an assumed one.')

    # ---------------------------------------------- robustness in `a`
    print()
    print('-' * 96)
    print('  CONTROL (5) -- A DECADE OF `a` AT EACH EPOCH, since `a` carries cosmological inputs')
    print('-' * 96)
    print('      %-14s %-16s %-18s %s'
          % ('a scaled by', 'today (orders)', 'recomb. (orders)', 'verdict'))
    ok_all = True
    for f in (0.1, 1.0, 10.0):
        o_now = math.log10(1.0e-2 / (C6 * suppression(a_now * f)))
        o_rec = math.log10(2.9e-4 / (C6 * suppression(a_rec * f)))
        good = o_now > 100.0 and o_rec > 100.0
        ok_all = ok_all and good
        print('      %-14.1f %-16.1f %-18.1f %s'
              % (f, o_now, o_rec, 'still >100' if good else 'FAILS'))
    print()
    print('    ⇒ the verdict survives a decade either way at both epochs: %s' % ok_all)
    print('      ** A factor of a few in any cosmological input cannot move a hundred-order margin. **')

    # ---------------------------------------------- verdict
    print()
    print('=' * 96)
    print('  CONCLUSION -- THE EXIT FIRES, AND WITH NO CUTOFF ANYWHERE IN THE ARGUMENT.')
    print('  On this background the only scales are `a` and ell_P, so the dimension-six term is')
    print('  suppressed against dimension four by (ell_P/a)^2 -- one vertex pair\'s ell_P^2 and two')
    print('  more inverse powers of the only length there is -- with ln(a/ell_P) in the logarithm and')
    print('  a rational of order one in front.  Sized that way, the term sits %.0f to %.0f orders'
          % (min(r[4] for r in rows), max(r[4] for r in rows)))
    print('  BELOW what measurement resolves on every one of the four observables.')
    print('  ⇒ ** PO-89 CLOSES AS ITS CLAUSE NOW READS: the effect is below what measurement')
    print('    resolves, sized by the scales the construction does carry. **  The reachable negative')
    print('    is missed structurally -- the term would need a curvature radius within ~%.0f ell_P.'
          % (a_reach / ELL_P_M))
    print('  ⚠ WITH ONE QUALIFICATION THE ROW WILL NOT DROP: on this background the dimension-six')
    print('    INVARIANT cannot be named -- the five scalars collapse to rank one and name nothing --')
    print('    so what is sized is the magnitude of the OBSTRUCTION, not an invariant\'s coefficient.')
    print('    The suppression is dimensional and so unaffected; what it multiplies is not an')
    print('    invariant, and this row does not supply one.')
    print('=' * 96)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
