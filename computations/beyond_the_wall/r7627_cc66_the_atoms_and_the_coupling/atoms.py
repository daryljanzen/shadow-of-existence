"""r7627+cc66 -- the gauge half's atoms: what dimensionless numbers the construction's data
form, and what it would take to turn one into a gauge coupling at a scale.

Run from anywhere:  python3 atoms.py

The atom list is the one FROZEN in PREDICTION.md before any of this existed.  Nothing here
reads a number off the corpus that is not cited beside it in that file.

** THE ORDER'S NAMED NEGATIVE IS "a number formed from the data lands near the measured strong
   coupling".  THIS FILE IS BUILT SO THAT SUCH A HIT CANNOT BE REPORTED AS A RESULT WITHOUT THE
   COUNT OF CANDIDATES BESIDE IT. **  The rule, the degree bound, the window and the expected
   number of chance hits are all declared BEFORE the comparison runs, because with ~12 atoms and
   pi the formable set is dense at the per-cent level wherever alpha_s lives.  The r7615 lesson
   was that a test which cannot fail says nothing; this is its mirror -- a test that cannot help
   but succeed.
"""
import math
import random
import sys

# --------------------------------------------------------------------------------------------
# THE ATOMS, exactly as frozen in PREDICTION.md.  (value, name, where it is landed)
# --------------------------------------------------------------------------------------------
# The two LENGTHS form exactly one dimensionless ratio (r7615), and the spectrum contributes one
# more dimensionless product.  Everything else is an integer the construction posits or derives.
DIMENSIONLESS_FROM_GEOMETRY = [
    (2 * math.pi,      'beta/alpha = 2 pi',       'r7615 -- the ONLY dimensionless monomial the two lengths form'),
    (5 * math.pi,      'gap * beta = 5 pi',       "r7627's own figure; (5/2a)(2 pi a) = 5 pi"),
]
INTEGERS = [
    (3,   'matrix factor / generations',  'P13 M_3(C) on C^3; the generations Z_3'),
    (4,   'spinor rank 2^floor(5/2)',     'r7619, r7621'),
    (5,   'face dimension',               'P13 -- the round five-sphere'),
    (6,   "walls' S_3 order",             'CR_framework l.1935'),
    (9,   'commutant on the bimodule',    'r7615'),
    (10,  'two-forms at p = 5',           'r7615'),
    (20,  'multiplicity at k = 1',        'r7621 -- 2^2 * C(5,1)'),
    (27,  'Delta(27) in SU(3)',           'CR_framework l.1935; P07/P13 receipts'),
    (60,  'multiplicity at k = 2',        'r7621 -- 2^2 * C(6,2)'),
    (81,  'wall/hinge holonomy in U(3)',  'CR_framework l.1935'),
]
# The eigenvalue ratios (5/2 + k)/(5/2) = 1 + 2k/5 are rational in 5 and small integers; the
# first three are carried explicitly so the list is not quietly narrower than the frozen one.
EIGENVALUE_RATIOS = [
    (7 / 5,  'eigenvalue ratio k=1',  'r7615 -- 1 + 2k/5'),
    (9 / 5,  'eigenvalue ratio k=2',  'r7615'),
    (11 / 5, 'eigenvalue ratio k=3',  'r7615'),
]

ATOMS = DIMENSIONLESS_FROM_GEOMETRY + INTEGERS + EIGENVALUE_RATIOS

# --------------------------------------------------------------------------------------------
# THE MEASURED DATUM, quoted WITH its scale -- never as a bare number (control 4).
# --------------------------------------------------------------------------------------------
ALPHA_S_MZ = 0.1180           # the measured strong coupling at mu = M_Z
ALPHA_S_MZ_ERR = 0.0009       # its quoted uncertainty
M_Z_GEV = 91.1876
# and the same datum in the normalisation a Lagrangian actually carries:
INV_G2_MZ = 1.0 / (4 * math.pi * ALPHA_S_MZ)     # 1/g^2 = 1/(4 pi alpha_s)

# --------------------------------------------------------------------------------------------
# THE FORMATION RULE AND ITS BOUND, declared before any comparison (registration item 1).
# --------------------------------------------------------------------------------------------
DEGREE_BOUNDS = (1, 2, 3, 4)
WINDOW_REL = 0.01             # "lands near" := within 1 per cent, declared in advance
WINDOW_REL_LOOSE = 0.05       # and a looser reading, also declared in advance
SEED = 7627                   # the chance-hit Monte Carlo is deterministic


def enumerate_monomials(atoms, degree):
    """every product of integer powers of the atoms with sum|exponent| <= degree.

    ⌗ Recurses over the SUPPORT -- which atoms carry a nonzero exponent -- rather than sweeping
      the full exponent grid.  The grid is (2D+1)^len(atoms), which at D=4 over 15 atoms is
      9^15 ~ 2e14 and does not finish; the monomials with sum|e| <= 4 number only tens of
      thousands.  ** The first version of this file swept the grid and had to be killed. **

    ⌗ Returns a dict keyed by VALUE (log10, rounded) -> (value, degree, spelling), so two
      spellings of one number count ONCE.  Counting spellings would inflate N and make the
      chance-hit control look better than it is -- the direction that would flatter a hit."""
    out = {}

    def rec(i, budget, value, parts, used):
        if used > 0:
            key = round(math.log10(value), 10)
            prev = out.get(key)
            if prev is None or used < prev[1]:
                out[key] = (value, used, ' * '.join(parts))
        if i >= len(atoms) or budget == 0:
            return
        val, name, _ = atoms[i]
        rec(i + 1, budget, value, parts, used)          # exponent 0 on this atom
        for e in range(1, budget + 1):
            for s in (1, -1):
                se = s * e
                spelling = name if se == 1 else '%s^%d' % (name, se)
                rec(i + 1, budget - e, value * (val ** se), parts + [spelling], used + e)

    rec(0, degree, 1.0, [], 0)
    return out


def hits_near(values, target, rel):
    lo, hi = target * (1 - rel), target * (1 + rel)
    return [v for v in values if lo <= v <= hi]


def expected_chance_hits(values, target, rel, trials=4000, seed=SEED):
    """the look-elsewhere control: how many numbers land within `rel` of a target chosen at
    random from the same decades, averaged over `trials`.

    ⌗ This is the whole point of the row's method clause.  A hit near alpha_s is a result only
      if the observed count exceeds what ANY target in the same range would collect by chance."""
    rng = random.Random(seed)
    logs = [math.log10(v) for v in values]
    lo, hi = min(logs), max(logs)
    # the target's own decade band, so the comparison is local rather than global
    t = math.log10(target)
    band_lo, band_hi = max(lo, t - 1.0), min(hi, t + 1.0)
    if band_hi <= band_lo:
        return 0.0, 0
    tot = 0
    for _ in range(trials):
        x = 10 ** rng.uniform(band_lo, band_hi)
        tot += len(hits_near(values, x, rel))
    return tot / trials, trials


def toy_kk_coupling():
    """CONTROL 1, the one the order asks for by name: a construction whose data DO fix its coupling.

    Kaluza-Klein: a gauge field in 5 dimensions on a circle of radius R, with five-dimensional
    coupling g5sq (which has the dimensions of a LENGTH).  The four-dimensional coupling is

        1/g4^2  =  2 pi R / g5sq                                            [determinate]

    ⇒ and the point of the control is WHAT MAKES IT DETERMINATE: not the geometry, but g5sq --
      an independent DIMENSIONFUL datum, the action's own normalisation.  Strip it and keep only
      the geometry, and 1/g4^2 is not a number at all.  That is precisely the face's situation."""
    R, g5sq = 1.0, 0.5          # units are arbitrary and cancel: the point is the RATIO exists
    return 2 * math.pi * R / g5sq


def main():
    print()
    print('=' * 94)
    print('r7627+cc66 -- THE ATOMS, THE NUMBERS THEY FORM, AND WHAT A COUPLING WOULD STILL NEED')
    print('=' * 94)

    print()
    print('  THE ATOM LIST, frozen in PREDICTION.md before any of this ran: %d atoms' % len(ATOMS))
    for val, name, where in ATOMS:
        print('    %-34s = %-18.10g   [%s]' % (name, val, where))

    print()
    print('  THE MEASURED DATUM, with its scale (never a bare number):')
    print('    alpha_s(M_Z = %.4f GeV) = %.4f +- %.4f' % (M_Z_GEV, ALPHA_S_MZ, ALPHA_S_MZ_ERR))
    print('    the same datum as a Lagrangian normalisation: 1/g^2 = 1/(4 pi alpha_s) = %.6f' % INV_G2_MZ)

    # ------------------------------------------------------------------ the enumeration
    print()
    print('-' * 94)
    print('  (1) THE ENUMERATION -- rule and bound declared in advance, count REPORTED')
    print('-' * 94)
    tables = {}
    for D in DEGREE_BOUNDS:
        tables[D] = enumerate_monomials(ATOMS, D)
        print('    sum|exponent| <= %d :  N = %7d distinct values' % (D, len(tables[D])))

    D = max(DEGREE_BOUNDS)
    table = tables[D]
    values = [v for (v, _, _) in table.values()]
    print()
    print('    the working bound is D = %d, N = %d' % (D, len(table)))

    # ------------------------------------------------------------- observed vs expected hits
    print()
    print('-' * 94)
    print('  (2) DOES A NUMBER LAND NEAR THE MEASURED COUPLING -- AND HOW MANY WOULD, BY CHANCE')
    print('-' * 94)
    for label, target in (('alpha_s(M_Z)', ALPHA_S_MZ), ('1/g^2(M_Z)', INV_G2_MZ)):
        for rel in (WINDOW_REL, WINDOW_REL_LOOSE):
            obs = hits_near(values, target, rel)
            exp, trials = expected_chance_hits(values, target, rel)
            ratio = (len(obs) / exp) if exp > 0 else float('inf')
            print()
            print('    target %-14s window +-%4.1f%%   OBSERVED %5d    EXPECTED BY CHANCE %8.2f'
                  % (label, 100 * rel, len(obs), exp))
            print('      ratio observed/expected = %.2f   (%d random targets in the same two decades)'
                  % (ratio, trials))
            if obs:
                near = sorted(obs, key=lambda v: abs(v / target - 1))[:3]
                for v in near:
                    sp = table[round(math.log10(v), 10)][2]
                    print('        %.6f  (%+.2f%%)  = %s' % (v, 100 * (v / target - 1), sp))

    # ------------------------------------------------------- the enumeration shown able to MISS
    print()
    print('-' * 94)
    print('  (5) THE ENUMERATION SHOWN ABLE TO MISS -- a counter that cannot miss counts nothing')
    print('-' * 94)
    for label, target in (('1e-30', 1e-30), ('1e+30', 1e30)):
        obs = hits_near(values, target, WINDOW_REL)
        print('    target %-8s window +-1%%  ->  %d hit(s)' % (label, len(obs)))

    # ------------------------------------------------------------------- the positive control
    print()
    print('-' * 94)
    print('  (3) POSITIVE CONTROL -- the machinery returns a DETERMINATE number when there is one')
    print('-' * 94)
    two_pi = 2 * math.pi
    found = hits_near(values, two_pi, 1e-12)
    print('    beta/alpha = 2 pi = %.10f is in the set: %s' % (two_pi, bool(found)))
    print('    ⇒ so "no coupling comes out" is not the machinery failing to produce numbers.')

    # ---------------------------------------------------------------------- the toy control
    print()
    print('-' * 94)
    print('  (4) CONTROL THE ORDER ASKS FOR BY NAME -- a construction whose data DO fix its coupling')
    print('-' * 94)
    inv_g4sq = toy_kk_coupling()
    print('    Kaluza-Klein on a circle:  1/g4^2 = 2 pi R / g5sq = %.6f   [determinate]' % inv_g4sq)
    print('    and WHAT makes it determinate is g5sq -- a DIMENSIONFUL datum, the action\'s own')
    print('    normalisation.  Keep only the geometry (R) and 1/g4^2 is not a number at all.')

    # ------------------------------------------------- what a mechanism needs, and the dimensions
    print()
    print('-' * 94)
    print('  (6) WHAT ANY MECHANISM NEEDS, AND WHETHER THE CONSTRUCTION SUPPLIES IT')
    print('-' * 94)
    print('    a. A REFERENCE SCALE at which the coupling is quoted.')
    print('       The construction fixes NO absolute scale: alpha is carried symbolically end to')
    print('       end (r7615, r7619, r7621 all declare it so), and every datum above is either')
    print('       dimensionless or a ratio of the two lengths.  A coupling is quoted AT AN ENERGY;')
    print('       a set of pure ratios names no energy.  ⇒ NOT SUPPLIED.')
    print('    b. And even taking the construction\'s OWN two scales rather than an absolute one,')
    print('       r7621 measured Lambda = 1/(2 pi alpha) BELOW the gap 5/(2 alpha), with ZERO modes')
    print('       between: Lambda/mu = 1/(5 pi) = %.6f < 1.  ⇒ no interval to run over.'
          % (1.0 / (5 * math.pi)))
    print('    c. A MATCHING CONDITION -- a statement that some particular number IS the coupling')
    print('       at that scale.  Nothing in the data picks WHICH of the %d numbers, or where.' % len(table))
    print('       ⇒ NOT SUPPLIED.')
    print()
    print('    ⛭ AND THE REASON UNDERNEATH ALL THREE, which is dimensional and not numerical:')
    print('      a gauge coupling IS an action normalisation.  The atoms are lengths, integers and')
    print('      spectral ratios -- geometry.  The toy fixes its coupling because it is GIVEN an')
    print('      independent dimensionful coupling; this construction is given no such datum for a')
    print('      gauge field.  ⇒ No monomial in these atoms is a coupling REGARDLESS of its value,')
    print('      which is why the near-misses above are numerology and not evidence.')

    print()
    print('=' * 94)
    print('  CONCLUSION: numbers DO land near the measured coupling, there are far too many of them')
    print('  for that to count, and the construction names neither the scale nor the matching that')
    print('  would turn one into a coupling.  The coupling enters as a MEASURED DATUM.')
    print('=' * 94)
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
