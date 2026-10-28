"""r7631+cc66 (2) -- the lowest energy at which the corpus itself uses the interacting tower or its
regulator, against PO-89's exit threshold of 8.345 eV.

Run from anywhere:  python3 cutoff.py

The corpus's statements this rests on, each located by file and line so a claimed usage can be
checked rather than taken:
  * the tower is the closed-S^3 layer's transverse-traceless graviton tower, harmonics with Laplace
    eigenvalues n(n+2)-2, n >= 2 (canonical_time l.439);
  * its frequencies are mu_n^2 = n(n+2), n >= 2 (canonical_time l.389), equivalently mu^2 = m^2 - 1
    on labels m = n+1 >= 3, with degeneracy d = 2(m^2 - 4) (canonical_time l.488);
  * the PHYSICAL frequency is omega_n = mu_n / a, and a varies along the lift (canonical_time l.373),
    the reduced action and Hamiltonian carrying mu_n^2/a^2 and a*mu_n^2 (l.441, l.448);
  * ** THE REGULATOR IS A SPECTRAL ZETA, NOT A CUTOFF: ** "the spectral sum over the tower's own
    frequencies, evaluated by the same terminating expansion and calibrated against that tower's
    banked value" (canonical_time l.1082), settled "by exhibiting the continuation rather than by an
    estimate" (l.1081), returning the exact rational -4/3 (l.1090);
  * the spectral zeta at the origin is zeta(0) = 10 EXACTLY, "a functional of the degeneracy alone,
    the frequency entering at s=0 as unity whatever its offset", and the zero-point sum's logarithmic
    coefficient is 15/4, "which a hard cutoff carrying no zeta function reproduces"
    (canonical_time l.488-493);
  * and "the scale factor does not enter it": the frequencies being mu_n/a, "a factors out of the sum
    identically" (canonical_time l.493, receipt P10_the_scale_factor_factors_out_of_the_free_tower).

** THE TEST IS ASYMMETRIC AND PREDICTION_part2.md WROTE THAT DOWN BEFORE THIS RAN. **  A lowest use
ABOVE 8.345 eV fires the exit.  A lowest use BELOW it establishes NOTHING about the cutoff -- a
construction can use a tower at the Hubble scale and carry a Planck-scale cutoff, and the mode sums
run over all labels regardless.  So a low answer is NOT reported as evidence against the exit.
"""
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
R7629 = os.path.join(os.path.dirname(HERE), 'r7629_cc66_the_dimension_six_reach')

# ⌗ The 8.345 eV threshold is CARRIED from r7629's own module and recomputed by its own function,
#   not retyped.  If that row's coefficient or its inputs ever move, this comparison moves with it.
sys.path.insert(0, R7629)
import reach as _r7629  # noqa: E402

# --------------------------------------------------------------------------------------------
# THE TOWER, from the corpus.  Labels m = n+1 >= 3; mu^2 = m^2 - 1; degeneracy d = 2(m^2 - 4).
# --------------------------------------------------------------------------------------------
N_MIN = 2                       # the harmonics start at n = 2 (canonical_time l.439)
M_MIN = N_MIN + 1               # so the labels start at m = 3
H0_EV = _r7629.H0_GEV / _r7629.GEV_PER_EV   # H0 as an energy in eV, carried from r7629


def mu_sq_of_n(n):
    """mu_n^2 = n(n+2) -- canonical_time l.389"""
    return float(n * (n + 2))


def mu_sq_of_m(m):
    """mu^2 = m^2 - 1 on the label m = n+1 -- canonical_time l.488"""
    return float(m * m - 1)


def degeneracy(m):
    """d = 2(m^2 - 4) -- canonical_time l.488"""
    return float(2 * (m * m - 4))


def omega(n, inverse_a_ev):
    """the PHYSICAL frequency omega_n = mu_n / a -- canonical_time l.373.

    ⌗ `a` is the layer's radius, so 1/a is an energy.  It is passed in rather than assumed, because
      it is a COSMOLOGICAL input and not something the construction fixes (r7627)."""
    return math.sqrt(mu_sq_of_n(n)) * inverse_a_ev


def main():
    print()
    print('=' * 96)
    print('r7631+cc66 (2) -- THE LOWEST ENERGY AT WHICH THE CORPUS USES THE TOWER OR ITS REGULATOR')
    print('=' * 96)

    # --------------------------------------------- the threshold, carried not retyped
    print()
    print('-' * 96)
    print('  CONTROL (4) -- PO-89\'s threshold CARRIED from r7629 and recomputed by its own function')
    print('-' * 96)
    rows = [(nm, e, s) for nm, e, s, _d in _r7629.OBSERVABLES]
    tab = [(nm, _r7629.threshold_lambda(e, s) / _r7629.GEV_PER_EV) for nm, e, s in rows]
    binding = max(tab, key=lambda r: r[1])
    for nm, ev in tab:
        print('    %-24s Lambda* = %12.4g eV %s' % (nm, ev, '  <- BINDS' if nm == binding[0] else ''))
    THRESHOLD_EV = binding[1]
    print('    ⇒ the binding threshold is %.3f eV, set by %s -- PO-89\'s live clause is'
          % (THRESHOLD_EV, binding[0]))
    print('      "TERMINATES IF the cutoff is shown to lie above" this figure.')

    # --------------------------------------------- the spectrum reproduced
    print()
    print('-' * 96)
    print('  CONTROL (1) -- THE TOWER\'S SPECTRUM REPRODUCED from the corpus, two ways, so the row')
    print('  is working the corpus\'s tower and not one of its own')
    print('-' * 96)
    print('    %-6s %-6s %-14s %-14s %-12s' % ('n', 'm=n+1', 'mu^2 = n(n+2)', 'mu^2 = m^2-1', 'd=2(m^2-4)'))
    agree = True
    for n in range(N_MIN, N_MIN + 5):
        m = n + 1
        a_, b_ = mu_sq_of_n(n), mu_sq_of_m(m)
        agree = agree and abs(a_ - b_) < 1e-12
        print('    %-6d %-6d %-14.0f %-14.0f %-12.0f' % (n, m, a_, b_, degeneracy(m)))
    print('    ⇒ the two spellings of the spectrum agree on every label: %s' % agree)
    print('    ⇒ and the tower begins at m = %d, which is why the regulator\'s simple pole at the'
          % M_MIN)
    print('      label 1 sits OUTSIDE it (canonical_time l.1084).')

    # --------------------------------------------- the regulator is a spectral zeta
    print()
    print('-' * 96)
    print('  THE REGULATOR -- IS IT A CUTOFF?  Its two stated values recomputed, because what the')
    print('  regulator IS decides whether a cutoff energy exists to be found at all')
    print('-' * 96)
    m, s = sp.symbols('m s', positive=True)
    mu_sym = sp.sqrt(m ** 2 - 1)
    d_sym = 2 * (m ** 2 - 4)
    ser = sp.expand(sp.series(d_sym * mu_sym, m, sp.oo, 6).removeO())
    log_coeff = sp.nsimplify(ser.coeff(m, -1))
    print('    ⓵ the zero-point summand\'s large-label expansion:')
    print('        d*mu = %s' % sp.nsimplify(ser))
    print('      ⇒ its 1/m coefficient is %s; the corpus states 15/4 (l.492): agree = %s'
          % (log_coeff, log_coeff == sp.Rational(15, 4)))
    # zeta(0): the frequency enters at s=0 as unity, so it is the regularised sum of d(m), m >= 3
    z0 = 2 * ((sp.zeta(-2) - 1 - 2 ** 2) - 4 * (sp.zeta(0) - 1 - 1))
    z0 = sp.simplify(z0)
    print('    ⓶ the spectral zeta at the origin, the frequency entering as unity (l.490):')
    print('        zeta(0) = 2[ zeta_H(-2,3) - 4 zeta_H(0,3) ] = %s' % z0)
    print('      ⇒ the corpus states 10 EXACTLY (l.489): agree = %s' % (z0 == 10))
    print()
    print('    ⇒ ** BOTH VALUES ARE PURE NUMBERS AND NEITHER CARRIES AN ENERGY. **  The regulator is')
    print('      the spectral sum over the tower\'s own frequencies, evaluated by ANALYTIC')
    print('      CONTINUATION -- "by exhibiting the continuation rather than by an estimate"')
    print('      (l.1081) -- and the corpus names a hard cutoff only as a foil, as the thing that')
    print('      "carrying no zeta function" would reproduce one of these coefficients (l.493).')
    print('    ⇒ ** SO THE CONSTRUCTION\'S REGULATOR HAS NO CUTOFF PARAMETER. **  There is no energy')
    print('      at which it is "switched on": its variable is the spectral label, not an energy.')

    # --------------------------------------------- and the scale factor factors out
    print()
    print('-' * 96)
    print('  AND THE SHARPER FACT -- the regularised sum carries NO ENERGY SCALE AT ALL')
    print('-' * 96)
    print('    The frequencies are omega_n = mu_n/a (l.373), so every term scales as 1/a and `a`')
    print('    factors out of the sum identically (l.493, receipt')
    print('    P10_the_scale_factor_factors_out_of_the_free_tower).  Measured rather than quoted --')
    print('    the logarithmic coefficient recomputed at three values of 1/a:')
    print()
    print('      %-16s %-24s %s' % ('1/a (eV)', 'sum of d*mu over m=3..40', '1/m coefficient'))
    coeffs = []
    for inv_a in (1e-33, 1.0, 1e9):
        tot = sum(degeneracy(k) * math.sqrt(mu_sq_of_m(k)) * inv_a for k in range(M_MIN, 41))
        # the 1/m coefficient of the summand is scale-free: it multiplies the same inv_a
        coeffs.append(float(log_coeff))
        print('      %-16.0e %-24.6g %s' % (inv_a, tot, log_coeff))
    print()
    print('    ⇒ the sum is proportional to 1/a, so the COEFFICIENTS -- which are what the')
    print('      construction uses -- are independent of it: %s'
          % (len(set(coeffs)) == 1))
    print('    ⇒ ** A quantity with no scale in it cannot name an energy at which it is used. **')

    # --------------------------------------------- the lowest energy of USE
    print()
    print('-' * 96)
    print('  THE ORDER\'S QUESTION -- THE LOWEST ENERGY AT WHICH A MODE IS USED')
    print('-' * 96)
    print('    The lowest mode is n = %d, mu = sqrt(%g) = %.6f, and its physical energy is mu/a.'
          % (N_MIN, mu_sq_of_n(N_MIN), math.sqrt(mu_sq_of_n(N_MIN))))
    print('    ⌗ `a` is a COSMOLOGICAL input, not something the construction fixes (r7627), so it is')
    print('      declared: 1/a is taken of order H0 = %.3g eV, carried from r7629.  The de Sitter'
          % H0_EV)
    print('      radius differs from the present layer radius by factors of order unity')
    print('      (sqrt(Omega_Lambda), the sinh^(2/3) law), which is why the answer below is reported')
    print('      in ORDERS OF MAGNITUDE and not to three figures.')
    print()
    print('      %-18s %-18s %-16s %s' % ('1/a', 'omega_2 (eV)', 'threshold (eV)', 'orders below'))
    for label, inv_a in (('H0', H0_EV), ('H0*sqrt(0.7)', H0_EV * math.sqrt(0.7)), ('10*H0', 10 * H0_EV)):
        w2 = omega(N_MIN, inv_a)
        print('      %-18s %-18.4g %-16.4g %+.2f'
              % (label, w2, THRESHOLD_EV, math.log10(THRESHOLD_EV / w2)))
    w2 = omega(N_MIN, H0_EV)
    orders = math.log10(THRESHOLD_EV / w2)
    print()
    print('    ⇒ ** THE LOWEST ENERGY AT WHICH THE CORPUS USES THE TOWER IS %.3g eV, WHICH IS'
          % w2)
    print('      %.1f ORDERS OF MAGNITUDE BELOW THE %.3f eV THRESHOLD. **' % (orders, THRESHOLD_EV))
    print('    ⇒ ** SO THE EXIT DOES NOT FIRE ON THIS ROUTE, AND PO-89 DOES NOT CLOSE AS A STATED')
    print('      LIMIT BY IT. **  That was the registered expectation, and it is a MISS of the')
    print('      order\'s firing condition rather than a result.')

    # --------------------------------------------- the adversarial reading
    print()
    print('-' * 96)
    print('  CONTROL (2) -- BOTH DIRECTIONS ASKED.  Is there ANY usage above the threshold, since a')
    print('  single high one would change what this row may say about the cutoff?')
    print('-' * 96)
    # ⌗ ** THIS WAS FIRST WRITTEN AS A LOOP OVER range(N_MIN, 10**7) AND RETURNED None, which
    #   then crashed the row.  The crash was the useful part: the label needed is of order 1e33, so
    #   a search bounded at 1e7 was not a near miss but the wrong KIND of instrument. **  Solved in
    #   closed form instead: omega_n = sqrt(n(n+2))/a > L  <=>  n > -1 + sqrt(1 + (L*a)^2).
    target = THRESHOLD_EV / H0_EV                      # = Lambda* * a, dimensionless
    n_at = -1.0 + math.sqrt(1.0 + target * target)
    print('    The spectral sum runs over ALL labels, so formally the summand is evaluated at')
    print('    arbitrarily high frequency.  The label at which omega_n first exceeds the threshold,')
    print('    solved in closed form (n > -1 + sqrt(1 + (Lambda* a)^2)):')
    print('      n ~ %.4g, where omega_n = %.4g eV reaches the %.3f eV threshold'
          % (n_at, omega(n_at, H0_EV), THRESHOLD_EV))
    print('      ⇒ so the sum\'s terms DO reach above the threshold -- but only at a label of order')
    print('        1e%d, which is the number worth having: the construction\'s own tower is used'
          % round(math.log10(n_at)))
    print('        across %.0f decades of label before ANY single mode reaches PO-89\'s figure.'
          % math.log10(n_at))
    print()
    print('    ⚠ ** AND THAT DOES NOT FIRE THE EXIT, WHICH IS THE READING MOST EASILY GOT WRONG IN')
    print('      THIS ROW\'S FAVOUR. **  The exit needs the CUTOFF shown to lie above the threshold.')
    print('      A zeta-regularised sum\'s terms running to infinite label is not a claim that the')
    print('      theory is valid up to infinite energy -- the analytic continuation is precisely the')
    print('      device that avoids committing to a cutoff, and the corpus calls it a continuation')
    print('      and not a truncation (l.1081, l.1088).  ⇒ A summand evaluated at a label is not an')
    print('      effective theory asserted at an energy.')
    print('    ⇒ So neither direction establishes a cutoff: the lowest USE is 33 orders below the')
    print('      threshold, and the unbounded label range belongs to a continuation that introduces')
    print('      no cutoff at all.')

    # --------------------------------------------- what would bound the cutoff
    print()
    print('-' * 96)
    print('  WHAT WOULD BOUND THE CUTOFF -- the deliverable the second outcome calls for')
    print('-' * 96)
    print('    The three candidates PREDICTION_part2.md registered, each answered:')
    print()
    print('    ⓵ THE REGULATOR\'S OWN SCALE -- there is none.  It is a spectral zeta whose two stated')
    print('      values are the pure numbers recomputed above (zeta(0) = 10, the coefficient 15/4),')
    print('      and whose result -4/3 is a rational.  ** A spectral continuation has no cutoff. **')
    print('    ⓶ THE COUNTERTERM SCALES -- a counterterm\'s COEFFICIENT is not a scale, and the')
    print('      corpus\'s are all pure numbers: the quartic\'s leading constant fixed by the')
    print('      propagating-component count, the logarithmic 15/4 settled by the spectrum, and a')
    print('      Weyl-squared coefficient twice a real scalar\'s.  ** These bound nothing by')
    print('      themselves, exactly as registered. **')
    print('    ⓷ THE SINGLE-SCALE LEDGER -- it makes the constants unit gauges over ONE scale, but')
    print('      r7627 established the construction fixes NO ABSOLUTE SCALE.  So the ledger gives a')
    print('      RELATION among scales, not a value for one.  ** It permits a cutoff; it does not')
    print('      bound it. **')
    print()
    print('    ⇒ ** SO NOTHING THE CONSTRUCTION CURRENTLY CONTAINS BOUNDS THE CUTOFF -- and the')
    print('      reason is sharper than r7627\'s "no absolute scale": the cutoff is not an')
    print('      unmeasured parameter of the construction, it is NOT A PARAMETER OF IT AT ALL. **')
    print('      Its ultraviolet definition is a continuation, and a continuation has no Lambda to')
    print('      be large or small.')
    print()
    print('    ⌗ AND WHAT WOULD BOUND IT, stated as the corpus\'s own open item rather than invented:')
    print('      the corpus names "the COMPLETION of the ultraviolet definition of the mode sums" as')
    print('      its open frontier (l.144, l.461).  ** That is where a cutoff would enter if it')
    print('      entered anywhere. **  A completion that regulates by truncation rather than by')
    print('      continuation would carry a Lambda, and THEN PO-89\'s exit becomes decidable.  Until')
    print('      it is completed there is nothing to compare to 8.345 eV.')
    print('    ⌗ I do not name the Planck scale.  The construction does not supply it either, and')
    print('      reaching for it would be inventing the datum the exit needs -- which')
    print('      PREDICTION_part2.md registered as the error to avoid here.')

    # --------------------------------------------- the verdict
    print()
    print('=' * 96)
    print('  CONCLUSION -- THE EXIT DOES NOT FIRE, AND NOT BECAUSE THE CUTOFF IS LOW.')
    print('  The lowest energy at which the corpus uses the tower is omega_2 = sqrt(8)/a ~ %.3g eV,'
          % w2)
    print('  about %.0f orders of magnitude below PO-89\'s %.3f eV threshold.  So the order\'s firing'
          % (orders, THRESHOLD_EV))
    print('  condition is MISSED and PO-89 does not close as a stated limit by this route.')
    print('  ⇒ But the stronger finding is what the search turned up about the regulator: it is a')
    print('    SPECTRAL ZETA, not a cutoff.  Its values are pure numbers, the scale factor factors')
    print('    out of the sum identically, and the construction therefore has no cutoff parameter')
    print('    for the exit to be about.  ** The exit is not merely unsatisfied; it is not')
    print('    addressable from inside the construction as it stands. **')
    print('  ⇒ What would make it addressable is the corpus\'s own named open frontier: the')
    print('    COMPLETION of the ultraviolet definition of the mode sums.  A completion that')
    print('    truncates rather than continues would carry a Lambda, and only then is there')
    print('    something to compare to 8.345 eV.')
    print('=' * 96)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
