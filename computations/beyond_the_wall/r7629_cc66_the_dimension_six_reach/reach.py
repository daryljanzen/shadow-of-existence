"""r7629+cc66 -- PO-89 (a): how big is the dimension-six term on each observable the construction
reads, and what cutoff would it take for that term to reach current precision?

Run from anywhere:  python3 reach.py

** THE DELIVERABLE IS A THRESHOLD, NOT A VERDICT, AND THAT IS THE REGISTRATION'S POINT. **
The order asks for the suppression as "a power of the curvature against the cutoff".  That is the
right suppression -- and `Lambda` is exactly what r7627 established the construction does not fix
(alpha symbolic end to end, every datum a ratio, no absolute scale anywhere).  So "the term lies
below current precision" is NOT computable: it is a statement about an assumed Lambda.  This file
therefore computes, for each observable, the threshold Lambda* at which the dimension-six term
would reach that observable's measured precision, and reports the exit as the inequality
Lambda > Lambda*.  Nobody inherits a cutoff from here.
"""
import math
import sys

# --------------------------------------------------------------------------------------------
# THE LANDED COEFFICIENT.  canonical_time l.1283 and P10's r7601 receipt.
# --------------------------------------------------------------------------------------------
# The complete second order's double logarithm carries 6023/20160 in the unit where the inverse
# cube of the scale factor carries one; its three parts are -1/3 * 197131/6720, 367/48, 389/160.
OBSTRUCTION_PARTS = [
    (-1.0 / 3.0 * 197131.0 / 6720.0, '-(1/3) * 197131/6720'),
    (367.0 / 48.0,                   '367/48'),
    (389.0 / 160.0,                  '389/160'),
]
C6 = 6023.0 / 20160.0            # the total, and this row's |coefficient| at dimension six

# --------------------------------------------------------------------------------------------
# THE MEASURED DATA, each quoted WITH its observable and its scale -- never a bare number.
# ⌗ These are comparison targets, not predictions.  The row's conclusion is reported with its
#   margin in ORDERS OF MAGNITUDE precisely so that a factor of a few in any of them cannot
#   change it; the margins below are checked against that claim in the receipt.
# --------------------------------------------------------------------------------------------
GEV_PER_EV = 1.0e-9
H0_GEV = 1.44e-42          # H0 ~ 67.4 km/s/Mpc expressed as an energy
T_REC_EV = 0.26            # the photon temperature at recombination, ~3000 K
T_CMB_EV = 2.35e-4         # the CMB temperature today, 2.725 K

OBSERVABLES = [
    # (name, characteristic energy E in GeV, fractional precision sigma, how sigma is quoted)
    ('the rate H0',        H0_GEV,              1.0e-2,
     'about 1 per cent, the width of the current H0 determinations'),
    ('the acoustic scale', T_REC_EV * GEV_PER_EV, 2.9e-4,
     '100 theta* = 1.04109 +- 0.00030, so 2.9e-4 fractional'),
    ('the tilt n_s',       T_REC_EV * GEV_PER_EV, 4.4e-3,
     'n_s = 0.9649 +- 0.0042, so 4.4e-3 fractional'),
    ('the tensor amplitude', T_REC_EV * GEV_PER_EV, 3.2e-2,
     'r < 0.032 as an upper limit -- an EXCLUSION, not a measurement (see the caveat)'),
]

# Candidate cutoffs, so "far below" is measured against something rather than asserted.
CUTOFFS = [
    ('the Planck scale',        1.22e19),
    ('a GUT scale',             1.0e16),
    ('the weak scale',          1.0e2),
    ('1 GeV',                   1.0),
    ('1 eV',                    1.0e-9),
    ('the CMB temperature',     T_CMB_EV * GEV_PER_EV),
]


def relative_correction(energy_gev, lambda_gev, dimension, coeff):
    """the relative size of an operator of the given DIMENSION, at `energy`, with cutoff `Lambda`.

    An operator of dimension d enters the action suppressed by Lambda^(4-d), so its effect on a
    dimensionless observable relative to the leading (dimension-four) term is

        delta  =  coeff * (energy / Lambda)^(d - 4)

    ⌗ The dimension is a PARAMETER and not hard-coded, which is what makes the order's
      dimension-four control structural rather than a sentence: at d = 4 the same formula must
      return an UNSUPPRESSED correction, which is why the dimension-four terms are the ones the
      observables actually measure.  See control (1)."""
    if lambda_gev <= 0:
        raise ValueError('a cutoff must be positive')
    return coeff * (energy_gev / lambda_gev) ** (dimension - 4)


def threshold_lambda(energy_gev, sigma, dimension=6, coeff=C6):
    """the cutoff at which the operator's effect would REACH the precision `sigma`.

    Solving coeff * (E/Lambda)^(d-4) = sigma for Lambda:

        Lambda*  =  E * (coeff / sigma)^(1/(d-4))

    ⇒ A cutoff ABOVE Lambda* hides the term; a cutoff BELOW it would make the term visible.  This
      is the row's deliverable: the exit fires as the inequality Lambda > Lambda*, with no cutoff
      assumed anywhere."""
    if dimension <= 4:
        raise ValueError('a threshold is only defined for a suppressed operator (d > 4)')
    return energy_gev * (coeff / sigma) ** (1.0 / (dimension - 4))


def main():
    print()
    print('=' * 96)
    print('r7629+cc66 -- PO-89 (a): THE DIMENSION-SIX TERM AGAINST WHAT IS MEASURED')
    print('=' * 96)

    # ---------------------------------------------------------------- the landed coefficient
    print()
    print('  THE LANDED COEFFICIENT (canonical_time l.1283; P10 receipt at r7601):')
    tot = 0.0
    for v, name in OBSTRUCTION_PARTS:
        tot += v
        print('    %-24s = %+.10f' % (name, v))
    print('    %-24s = %+.10f' % ('their sum', tot))
    print('    %-24s = %+.10f   (6023/20160)' % ('the stated total', C6))
    print('    ⇒ the three parts reproduce the stated total: %s'
          % ('YES' if abs(tot - C6) < 1e-12 else 'NO'))
    print()
    print('  ⌗ AND WHAT IS BEING SIZED, which the row must not misstate: 6023/20160 is the')
    print('    obstruction to COVARIANCE -- the carrier is not covariant from inside, so this is')
    print('    not an invariant\'s coefficient.  It is the magnitude of the dimension-six term whose')
    print('    split between the reduction and the truncation is itself PO-89\'s stated limit.')

    # ------------------------------------------------------- control (1): the dimension-four arm
    print()
    print('-' * 96)
    print('  CONTROL (1) -- THE ORDER\'S NAMED CONTROL: does the same estimate size a')
    print('                 DIMENSION-FOUR quantity correctly?')
    print('-' * 96)
    e, lam = OBSERVABLES[1][1], 1.0           # any cutoff: the point is the exponent
    d4 = relative_correction(e, lam, 4, 1.0)
    d6 = relative_correction(e, lam, 6, 1.0)
    print('    at E = %.3e GeV and Lambda = %.1f GeV, with unit coefficient:' % (e, lam))
    print('      dimension 4 -> relative size %.6f     (UNSUPPRESSED, exponent 0)' % d4)
    print('      dimension 6 -> relative size %.6e     (suppressed by (E/Lambda)^2)' % d6)
    print('    ⇒ The estimator returns NO suppression at dimension four, which is why the')
    print('      dimension-four terms are the ones these observables actually measure, and a')
    print('      suppression of exactly two powers at dimension six.  ** The dimension is a')
    print('      parameter of the function, so this is the estimator\'s own bookkeeping being')
    print('      checked rather than a sentence about it. **')

    # --------------------------------------------- control (2): a REAL dimension-six case, numeric
    print()
    print('-' * 96)
    print('  CONTROL (2) -- the same estimator on a dimension-six operator whose cutoff is KNOWN:')
    print('                 the four-fermion (Fermi) operator, Lambda ~ m_W')
    print('-' * 96)
    m_w, m_mu = 80.4, 0.1057
    fermi = relative_correction(m_mu, m_w, 6, 1.0)
    print('    (m_mu / m_W)^2 = (%.4f / %.1f)^2 = %.3e' % (m_mu, m_w, fermi))
    print('    ⇒ the estimator reproduces the known smallness of a weak-scale dimension-six')
    print('      operator at the muon mass, ~1e-6, which is the right order.  ** So the (E/Lambda)^2')
    print('      form is validated on a case where the answer is independently known, not only')
    print('      asserted for this construction. **')

    # ------------------------------------------------------------------- the thresholds
    print()
    print('-' * 96)
    print('  (1)-(2) THE SIZING AND THE THRESHOLDS -- the row\'s deliverable')
    print('-' * 96)
    print()
    print('    %-22s %12s %10s   %14s %12s' % ('observable', 'E (GeV)', 'sigma', 'Lambda* (GeV)', 'Lambda* (eV)'))
    rows = []
    for name, e, sigma, how in OBSERVABLES:
        lstar = threshold_lambda(e, sigma)
        rows.append((name, e, sigma, lstar, how))
        print('    %-22s %12.3e %10.1e   %14.3e %12.3e' % (name, e, sigma, lstar, lstar / GEV_PER_EV))
    print()
    for name, e, sigma, lstar, how in rows:
        print('    %-22s sigma: %s' % (name, how))

    worst = max(rows, key=lambda r: r[3])
    print()
    print('    ⇒ THE BINDING OBSERVABLE is %s, with the HIGHEST threshold:' % worst[0])
    print('      Lambda* = %.3e GeV = %.3f eV' % (worst[3], worst[3] / GEV_PER_EV))
    print('      ** It binds because it couples a recombination-era energy to the tightest')
    print('         fractional precision of the four. **')

    # ------------------------------------------------- (3) the exit, as an inequality
    print()
    print('-' * 96)
    print('  (3) DOES THE EXIT FIRE?  Reported as Lambda > Lambda*, against candidate cutoffs')
    print('-' * 96)
    print()
    print('    %-24s %14s   %s' % ('candidate cutoff', 'Lambda (GeV)', 'orders of magnitude above the binding Lambda*'))
    margins = []
    for cname, lam in CUTOFFS:
        margin = math.log10(lam / worst[3])
        margins.append((cname, lam, margin))
        verdict = 'HIDDEN' if margin > 0 else 'VISIBLE'
        print('    %-24s %14.3e   %+8.1f   -> the term is %s' % (cname, lam, margin, verdict))

    print()
    print('    ⇒ Every candidate cutoff at or above 1 GeV hides the term, the weakest of those by')
    print('      %.1f orders of magnitude.' % min(m for _, _, m in margins if m > 0))
    print()
    print('    ⚠ AND THE THRESHOLD IS NOT VACUOUS, WHICH IS THE PART WORTH REPORTING.  A cutoff of')
    print('      1 eV sits %.1f orders BELOW the binding Lambda* of %.3f eV, and there the term'
          % (abs(math.log10(1.0e-9 / worst[3])), worst[3] / GEV_PER_EV))
    print('      would stand at about %.0f times the acoustic scale\'s precision -- VISIBLE, not'
          % (relative_correction(worst[1], 1.0e-9, 6, C6) / worst[2]))
    print('      hidden.  ** So the exit does not fire for every cutoff one could write down: it')
    print('      requires Lambda above a few eV, i.e. an atomic scale or higher. **')
    print('      ⌗ An earlier draft of this line claimed the exit failed only below the CMB')
    print('        temperature (%.3e eV).  That was FALSE: Lambda* is %.1f orders of magnitude' % (T_CMB_EV, math.log10((worst[3] / GEV_PER_EV) / T_CMB_EV)))
    print('        ABOVE the CMB temperature, and 1 eV lies between them.  The claim is corrected')
    print('        here rather than quietly dropped, because the margin is the whole result.')

    # ------------------------------------------------- the order's reachable negative
    print()
    print('-' * 96)
    print('  THE ORDER\'S NAMED REACHABLE NEGATIVE -- one observable within an order of magnitude')
    print('  of current precision.  Tested, and MISSED, for each candidate cutoff.')
    print('-' * 96)
    for cname, lam in CUTOFFS:
        hits = []
        for name, e, sigma, lstar, _ in rows:
            delta = relative_correction(e, lam, 6, C6)
            if delta > 0.1 * sigma:
                hits.append('%s (delta/sigma = %.2e)' % (name, delta / sigma))
        print('    cutoff %-24s -> observables within 10x of precision: %s'
              % (cname, ', '.join(hits) if hits else 'NONE'))

    # ------------------------------------------------------------------- the caveats
    print()
    print('-' * 96)
    print('  WHAT THIS ROW DOES NOT CLAIM')
    print('-' * 96)
    print('    a. ** It does not supply a cutoff. **  Every line above is conditional on Lambda,')
    print('       because r7627 established the construction fixes no absolute scale.  The exit')
    print('       fires as an INEQUALITY and the row says so on its face.')
    print('    b. The tensor amplitude enters as an EXCLUSION (r < 0.032), not a measurement, so')
    print('       its threshold is the weakest OF THE THREE READ AT RECOMBINATION and is reported')
    print('       apart rather than averaged in with two measured precisions.')
    print('       ⌗ A draft of this line said "the weakest of the four".  THAT WAS FALSE and this')
    print('         row\'s own table falsified it: the RATE\'s threshold is lower still, %.3e GeV,'
          % min(r[3] for r in rows))
    print('         by about %.0f orders of magnitude -- not because its precision is loose but'
          % abs(math.log10(min(r[3] for r in rows) / max(r[3] for r in rows))))
    print('         because its characteristic energy is H0 itself.  Two different reasons for a')
    print('         low threshold, and the caveat had merged them.')
    print('    c. The characteristic energy of the TILT is the least well defined of the four: it')
    print('       is a property of the primordial spectrum, and which energy the construction')
    print('       reads it at is a reading rather than a computation.  It is carried at the')
    print('       recombination scale and is NOT the binding observable either way.')
    print('    d. 6023/20160 is an obstruction to covariance, not an invariant\'s coefficient, so')
    print('       "the dimension-six term" here means the magnitude whose non-covariant split is')
    print('       PO-89\'s stated limit -- which is what makes (a) the whole of the exit.')

    print()
    print('=' * 96)
    print('  CONCLUSION: the exit FIRES, conditionally and explicitly so.  The binding threshold is')
    print('  Lambda* = %.3f eV, set by the ACOUSTIC SCALE, which binds because it couples a' % (worst[3] / GEV_PER_EV))
    print('  recombination energy to the tightest fractional precision of the four.  Any cutoff above')
    print('  that hides the term on every observable the construction reads; at 1 GeV and above the')
    print('  margin is 8 orders of magnitude or more, and NO observable comes within ten times its')
    print('  precision.  ⚠ But the threshold is not vacuous -- at a 1 eV cutoff the acoustic scale')
    print('  would see the term at ~70x its precision.  ⇒ PO-89 (a) is OUT OF REACH for Lambda above')
    print('  a few eV, and on that condition the dimension-six value is a STATED LIMIT.')
    print('=' * 96)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
