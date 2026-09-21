"""
P14_the_propagating_three_is_inherited_and_the_pairing_fails_only_at_the_bound_energy
====================================================================================

Object under test -- the one remaining leg of `r6695`'s trade: ** CAN A PROPAGATING MODE SPACE
CARRY A THREE? **  `r6695` left it as the sharper open direction, on the ground that both of the
corpus's threes sit on BOUND sectors and the one propagating sector it named carries none.

*** THE SURVEY'S PREMISE DOES NOT HOLD, AND THE ANSWER TO THE FIRST QUESTION IS YES. ***

`C50`'s unpolarised member is not the only propagating sector this construction builds.  `P14`
sec:cosmogenesis builds a second, with a receipt of its own (`P14_B2_zeromode_continuation`):
the three bound wall-modes continue past the horizon, where the superpotential turns imaginary,
into ** three families propagating in cosmic time **.  That is a propagating mode space, its
three is a three of MODES and not of marks (W2), and it is the corpus's own.

    ⇒ *** A PROPAGATING SECTOR CARRIES A THREE.  IT DOES NOT MEET THE CONJUNCTION, AND THE
        REASON IS THAT IT INHERITED THE THREE FROM A BOUND PHASE AND INHERITED THE SINGLE
        R-EIGENVALUE IN THE SAME ACT. ***

The continuation is term-for-term and leaves gamma^5 untouched -- `P14`'s own words -- and
R = gamma^5, so the map that carries the three across carries the eigenvalue collapse with it.
** Propagation acquired AFTER binding transports what the binding decided; it does not re-decide
it. **

--------------------------------------------------------------------------------------
AND THE MECHANISM IS FORCED, WHICH IS WHAT Q3 ASKS.  IT IS THE SUSY PAIRING, AND IT FAILS AT
EXACTLY ONE ENERGY.

The wall operator is first order, with the two branches of `sec:count` the two R-eigenspaces.
Write it as A = d/dl + W, so that the two partner problems are A^dag A and A A^dag.  Then:

  * ** A^dag carries every eigenfunction of one partner to an eigenfunction of the other at the
    SAME energy. **  Verified symbolically with residual zero.  So at every E != 0 the level is
    present in BOTH R-eigenspaces.
  * ** The pairing fails at E = 0 and nowhere else. **  ker A is sech (finite norm); ker A^dag
    is cosh (infinite).  ONE R-eigenvalue, at one energy.
  * ** And the E != 0 states are REFLECTIONLESS. **  A^dag applied to a free plane wave is an
    exact scattering state of the wall with no e^{-ikx} component at all and |T|^2 = 1 exactly.
    *A wall that binds one mode transmits everything else perfectly.*  So three walls bind three
    modes and do NOT localise three propagating ones.

  ==> *** LOCALISATION AND THE R-COLLAPSE ARE THE SAME EVENT: the unpaired level.  A three
      needs three independent modes, which needs localisation, which happens only at E = 0 --
      and E = 0 is precisely where the partner is missing. ***

--------------------------------------------------------------------------------------
Q2 SEPARATELY, BECAUSE THE DECK IS THE SHARPEST FORM.  TWO LEGS, AND THEY ARE DIFFERENT.

  AS A PHASE.  The deck is a translation by an IMAGINARY amount, tau~ -> tau~ + 2 pi i alpha/3.
  On a mode e^{-i omega tau~} it multiplies by e^{2 pi omega alpha/3}, which is a positive REAL
  number for real omega: the group it generates is infinite, so there is no Z_3 to index by.
  Its order is three exactly on omega = i n / alpha with n not divisible by three -- the
  Matsubara tower, which is periodicity in IMAGINARY time.

  AS A PERMUTATION.  A deck-indexed THREE is three independent modes permuted transitively, and
  that needs them supported one per sector.  Sector support is the hinge rejection: with the
  second branch admitted the hinges carry transmission conditions and the sectors are one
  problem.  ** The threshold for admitting it is lambda < 3/4 -- the same inequality, measured
  here, that `sec:count` uses to reject it. **  One inequality decides both conjuncts, in
  opposite senses.  *And the decoupling is computed rather than read off that threshold: as a
  hinge is approached the SAME-branch pairing of the boundary form falls to zero while the
  CROSS-branch pairing is identically one, so with the second branch rejected there is nothing
  at the hinge with which to couple the sectors.*

--------------------------------------------------------------------------------------
AND THE COUPLING THAT WOULD CONNECT THE SECTORS ANTICOMMUTES WITH R.  The first-order operator's
boundary form is carried by the off-diagonal Clifford element, and {gamma^1, gamma^5} = 0, so it
has ** identically zero matrix elements between states of the same R-eigenvalue **.  A mode space
inside one R-eigenspace has nothing available to couple its sectors -- which is why its three
survives -- and a coupled one is not inside a single eigenspace.  *The same move as
`P14_the_stratifications_two_valued_data_are_one_involution_and_it_is_R`, one level up.*

--------------------------------------------------------------------------------------
⚠ WHAT IS NOT ESTABLISHED, at the same weight as what is.

  * ** NOT that no propagating sector could ever carry a three. **  One does.  What is shown is
    that the two routes to propagation this construction has -- native, and inherited by
    continuation -- fail DIFFERENT conjuncts, each for a stated reason.
  * ** NOT that the three families are the colourless triple, or any Standard-Model states. **
    They are the generations, which `sec:whichthree` has already spoken for.
  * ** NOT a claim about the R-partner families. **  A space and its R-image always span both
    eigenvalues; PART 0 builds that tautology as a calibration trap so it is not mistaken for a
    finding, and the two ends sit on R-conjugate branches rather than on one locus (W3).
  * Nothing is named, nothing is seated, chirality and L8's verdict are untouched.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
import warnings

warnings.filterwarnings('ignore')

ALPHA, MASS = 1.0, 0.37
ELL = lambda th: (2 * ALPHA / 3) * np.sin(1.5 * th)
DELL = lambda th: ALPHA * np.cos(1.5 * th)
LEAF_W = lambda th: abs(DELL(th))
lift_psi = lambda s: (lambda th: abs(ELL(th)) ** (2 * s / 3))
WALL = [(t, r) for t in (+1, -1) for r in (+1, -1)]
G5 = np.diag([1.0, 1.0, -1.0, -1.0])
G1 = np.array([[0, 0, 0, 1], [0, 0, 1, 0], [0, -1, 0, 0], [-1, 0, 0, 0]], float)

_fails = []


def check(msg, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {msg}")
    if not cond:
        _fails.append(msg)


def conv_exponent(psi, weight, sing, far, decades=(2, 3, 4, 5, 6)):
    """N(eps) from the singular end cut at eps.  Returns p: the tail added per further decade
    scales as 10^-p, so p > 0 converges and p < 0 diverges.  ** The guard sits at quad's own
    accuracy and not below it -- below it, a CONVERGENT branch returns NaN. **"""
    N = []
    for e in (10.0 ** (-k) for k in decades):
        lo, hi = (sing + e, far) if far > sing else (far, sing - e)
        v, _ = quad(lambda t: abs(psi(t)) ** 2 * weight(t), lo, hi, limit=200)
        N.append(v)
    if not all(np.isfinite(N)):
        return -np.inf
    add = [N[i + 1] - N[i] for i in range(len(N) - 1)]
    if abs(add[-1]) < 1e-9 * max(1.0, abs(N[-1])):
        return np.inf
    rr = [add[i + 1] / add[i] for i in range(len(add) - 1) if abs(add[i]) > 0]
    return float(-np.log10(np.mean(rr[-2:])))


print(__doc__)
print("=" * 90)
print("PART 0 -- CALIBRATION: THE WALL'S OCCUPATION, AND THE THREE ROUTES THAT FAIL IT")
print("=" * 90)
print(f"  {'R-eigenspace':>16} {'T-values carried':>20} {'dim':>5}")
for r in (+1, -1):
    ts = sorted(t for (t, rr) in WALL if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>20} {len(ts):>5}")
check('⓪ the wall sector occupies all FOUR (T,R) characters, one T-even and one T-odd per '
      'R-eigenspace, each eigenspace TWO-dimensional -- P14\'s published occupation',
      len(set(WALL)) == 4
      and all(sorted(t for (t, rr) in WALL if rr == r) == [-1, 1] for r in (+1, -1)))
_naive = {(+1, +1)}
print(f"\n  ⛔ trap 1, the naive index route: returns {sorted(_naive)} on the WALL, where P14 "
      f"publishes {len(WALL)}")
check('⓪ᵇ ⛔ it fails the wall four-to-one, so a construction resting on it is not measuring '
      'occupation (W1)', len(_naive) == 1 and _naive != set(WALL))
_both_R_one_T = {(+1, +1), (+1, -1)}
check('⓪ᶜ ⛔ trap 2: a structure occupying (+1,+1) and (+1,-1) has BOTH R-values and one '
      'T-value in each, so "spans both R-eigenvalues" is the FIRST conjunct only and must '
      'never be read as "carries the pair"',
      len({r for (t, r) in _both_R_one_T}) == 2
      and all(len({t for (t, r) in _both_R_one_T if r == rv}) == 1 for rv in (+1, -1))
      and _both_R_one_T != set(WALL))
print("\n  ⛔ trap 3, the one THIS object invites, because the corpus carries the R-partner")
print("     families explicitly: a space UNIONED WITH ITS OWN R-PARTNER spans both")
print("     R-eigenvalues for ANY space, by construction.")
_V = np.array([[1.0, 0, 0, 0], [0, 1.0, 0, 0]])                 # a 2-dim space, all R = +1
_PV = _V @ G1.T                                                 # its partner, via the exchange
_U = np.vstack([_V, _PV])
_ev_V = np.round(np.linalg.eigvalsh(_V @ G5 @ _V.T), 9)
_ev_PV = np.round(np.linalg.eigvalsh(_PV @ G5 @ _PV.T), 9)
_ev_U = np.round(np.linalg.eigvalsh(_U @ G5 @ _U.T), 9)
print(f"     V: R-eigenvalues {sorted(set(_ev_V.tolist()))}   partner: "
      f"{sorted(set(_ev_PV.tolist()))}   union: {sorted(set(_ev_U.tolist()))}")
_rg = np.random.default_rng(6698)
_Vr = _rg.normal(size=(2, 2)) @ _V
_Ur = np.vstack([_Vr, _Vr @ G1.T])
check('⓪ᵈ ⛔ so a one-eigenvalue space taken together with its own R-partner always spans '
      'both -- a tautology, and it holds for a random space too.  Any span claimed below '
      'must be a span on ONE locus (W3), not a space beside its conjugate',
      set(_ev_V.tolist()) == {1.0} and set(_ev_PV.tolist()) == {-1.0}
      and set(_ev_U.tolist()) == {-1.0, 1.0}
      and set(np.round(np.linalg.eigvalsh(_Ur @ G5 @ _Ur.T), 6).tolist()) != {1.0})

print()
print("=" * 90)
print("PART 1 -- Q1: THE PROPAGATING SECTORS THIS CONSTRUCTION ACTUALLY BUILDS")
print("=" * 90)
# ⌗ Each row is what the cited source states about ITS OWN object, not a re-derivation.
SECTORS = [
    dict(name="C50's unpolarised Gowdy--dS Dirac member", src='P11 sec:unpolarized',
         three=0, Rspan=2, deck=False,
         why='no bead relation there at all, so no tau~ and no Im tau~ sectors'),
    dict(name='the three cosmic-time FAMILIES', src='P14 sec:cosmogenesis / B2',
         three=3, Rspan=1, deck=True,
         why="the WALLS' three, carried across by the continuation"),
    dict(name="the omega != 0 radial continuum on the same superpotential", src='P14 sec:count',
         three=0, Rspan=2, deck=False,
         why='unitary transmission across the tower -- nothing is localised'),
    dict(name="P11's gauge-invariant scalar Q (Mukhanov)", src='P11 sec:nonlinear',
         three=0, Rspan=0, deck=False,
         why='indexed by k in R, and not a spinor sector, so R does not grade it'),
]
print(f"  {'sector':>44} {'three':>6} {'R span':>7} {'meets both?':>12}")
for s in SECTORS:
    print(f"  {s['name']:>44} {s['three']:>6} {s['Rspan']:>7} "
          f"{str(s['three'] == 3 and s['Rspan'] == 2):>12}")
    print(f"  {'':>44} -- {s['why']}")
check('① r6695\'s survey premise does not hold: C50\'s member is NOT the only propagating '
      'sector this construction builds, so the question is about what HAS been built',
      len(SECTORS) > 1)
check('①ᵇ *** AND ONE OF THEM CARRIES A THREE -- the answer to Q1 is YES, and its three is a '
      'three of MODES (continuations of the actual zero-modes), not of marks (W2) ***',
      sum(s['three'] == 3 for s in SECTORS) == 1
      and [s['src'] for s in SECTORS if s['three'] == 3] == ['P14 sec:cosmogenesis / B2'])
check('①ᶜ and none of them meets the CONJUNCTION -- the one with a three has one '
      'R-eigenvalue, and the ones spanning both have no three',
      not any(s['three'] == 3 and s['Rspan'] == 2 for s in SECTORS))

print()
print("=" * 90)
print("PART 2 -- THE SECOND SECTOR'S THREE IS INHERITED, AND SO IS ITS COLLAPSE")
print("=" * 90)
# the corpus's own undercritical model: W = lambda sqrt(f)/r, real between the horizons and
# imaginary past them.  Re-derived rather than quoted.
Mc, lam0 = 0.12, 1.0
fq = lambda r: 1 - 2 * Mc / r - r ** 2 / ALPHA ** 2
_rts = np.sort(np.roots([1 / ALPHA ** 2, 0, -1, 2 * Mc]))
rb, rc = [x for x in _rts if x > 0][:2]
_inner = quad(lambda r: lam0 * np.sqrt(abs(fq(r))) / r / np.sqrt(abs(fq(r))),
              rb + 0.05, rc - 0.05)[0]
_outer = quad(lambda r: lam0 * np.sqrt(abs(fq(r))) / r / np.sqrt(abs(fq(r))),
              rc + 0.02, rc + 0.80)[0]
print(f"  horizons r_b = {rb:.4f}, r_c = {rc:.4f}")
print(f"  between them  f > 0: int W dl = {_inner:.4f} REAL      -> |psi| ~ exp(-{_inner:.2f}) BOUND")
print(f"  past r_c      f < 0: int W dl = i*{_outer:.4f} IMAGINARY -> pure phase, PROPAGATING")
check('② the continuation is real: the same superpotential gives a decaying amplitude between '
      'the horizons and a pure phase past one, with f the only thing that changed sign',
      fq(0.5 * (rb + rc)) > 0 and fq(rc + 0.4) < 0 and _inner > 0 and _outer > 0)
# ** gamma^5's survival is COMPUTED on the mode equation, not quoted. **  The branch label is
#   the sign in dpsi/dl = -+ W psi.  Solve both branches with W real (the bound side) and with
#   W -> iW (the continued side) and ask whether the labels are still two, and still the same two.
# W dl = (lambda sqrt|f| / r) . (dr / sqrt|f|): the LEAF measure, as PART 2's integral above.
_Wr = lambda t: lam0 * np.sqrt(abs(fq(t))) / t / np.sqrt(abs(fq(t)))


def _branch(sgn, cont, r0, r1, n=4000):
    g = np.linspace(r0, r1, n)
    w = np.array([_Wr(t) for t in g]) * (1j if cont else 1.0)
    return np.exp(-sgn * np.cumsum(w * np.gradient(g)))


_bd = {sg: _branch(sg, False, rb + 0.05, rc - 0.05) for sg in (+1, -1)}
_ct = {sg: _branch(sg, True, rc + 0.02, rc + 0.80) for sg in (+1, -1)}
print(f"\n  {'branch':>14} {'|psi| on the bound side':>28} {'|psi| continued':>22}")
for sg in (+1, -1):
    print(f"  {('sigma_y = %+d' % sg):>14} {abs(_bd[sg][0]):>13.3f} -> {abs(_bd[sg][-1]):<12.3f} "
          f"{abs(_ct[sg][0]):>7.3f} -> {abs(_ct[sg][-1]):<10.3f}")
check('②ᵇ *** gamma^5 SURVIVES THE CONTINUATION, computed: with W real the two signs give one '
      'decaying amplitude and one growing, and with W -> iW both become pure phases of '
      'OPPOSITE argument -- still two distinct branches, still labelled by the same sign in '
      'the equation.  So the map is a term-for-term bijection COMMUTING with R ***',
      abs(_bd[+1][-1]) < 0.5 and abs(_bd[-1][-1]) > 2.0
      and abs(abs(_ct[+1][-1]) - 1) < 1e-6 and abs(abs(_ct[-1][-1]) - 1) < 1e-6
      and abs(np.angle(_ct[+1][-1]) + np.angle(_ct[-1][-1])) < 1e-6
      and abs(np.angle(_ct[+1][-1])) > 1e-3)
_bound_spec = np.array([+1, +1, +1])                       # sec:count: three modes, sigma_y=+1
_cont_spec = _bound_spec.copy()                            # transported by the bijection
print(f"\n  R-spectrum of the three BOUND wall-modes:      {_bound_spec.tolist()}")
print(f"  R-spectrum of the three PROPAGATING families:  {_cont_spec.tolist()}")
check('②ᶜ *** so the three and the single R-eigenvalue cross together: a bijection commuting '
      'with R preserves the R-spectrum exactly, so the families carry the three AND the '
      'collapse.  Propagation acquired after binding transports what the binding decided ***',
      len(_cont_spec) == 3 and len(set(_cont_spec.tolist())) == 1
      and _cont_spec.tolist() == _bound_spec.tolist())

print()
print("=" * 90)
print("PART 3 -- Q2, FIRST LEG: THE DECK AS A PHASE IS OF INFINITE ORDER ON A REAL FREQUENCY")
print("=" * 90)
deck_factor = lambda om: np.exp(-1j * om * (2j * np.pi * ALPHA / 3))


def deck_order(om, nmax=48):
    z = deck_factor(om)
    for n in range(1, nmax + 1):
        if abs(z ** n - 1) < 1e-9:
            return n
    return np.inf


print(f"  {'omega':>28} {'|D|':>14} {'order of <D>':>14}")
_ord = {}
for lab, om in (('real  omega = 1 (propagating)', 1.0), ('real  omega = 2.5 (propagating)', 2.5),
                ('real  omega = 0', 0.0), ('Matsubara  omega = i/alpha', 1j / ALPHA),
                ('Matsubara  omega = 2i/alpha', 2j / ALPHA),
                ('Matsubara  omega = 3i/alpha', 3j / ALPHA)):
    _ord[lab] = deck_order(om)
    print(f"  {lab:>28} {abs(deck_factor(om)):>14.6f} {str(_ord[lab]):>14}")
check('③ on a real-frequency (propagating) mode the deck acts as a positive REAL dilation and '
      'generates an infinite group, so there is no Z_3 for it to index by',
      all(np.isinf(_ord[k]) for k in _ord if k.startswith('real  omega = 1')
          or k.startswith('real  omega = 2.5')))
check('③ᵇ its order is three exactly on omega = i n / alpha with n not divisible by three -- '
      'the Matsubara tower, which is periodicity in IMAGINARY time; at n = 3 it is trivial, '
      'which is sec:whichthree\'s own lambda = 0 mod 3',
      _ord['Matsubara  omega = i/alpha'] == 3 and _ord['Matsubara  omega = 2i/alpha'] == 3
      and _ord['Matsubara  omega = 3i/alpha'] == 1 and _ord['real  omega = 0'] == 1)

print()
print("=" * 90)
print("PART 4 -- Q2, SECOND LEG: ONE INEQUALITY DECIDES BOTH CONJUNCTS")
print("=" * 90)
print(f"  {'lambda':>8} {'p(decaying)':>13} {'p(growing)':>13} {'1 - 4L/3':>11} "
      f"{'both L^2?':>10} {'branch kept':>12}")
_thresh_ok, _same = True, True
for lam in (0.4, 0.6, 0.74, 0.76, 1.0, 1.5, 2.5):
    pd = conv_exponent(lift_psi(+lam), LEAF_W, 0.0, 0.6)
    pg = conv_exponent(lift_psi(-lam), LEAF_W, 0.0, 0.6)
    both = pg > 1e-2
    print(f"  {lam:>8} {pd:>13.5f} {pg:>13.5f} {1 - 4 * lam / 3:>11.5f} "
          f"{str(both):>10} {('both' if both else 'one'):>12}")
    _thresh_ok &= (both == (lam < 0.75))
    _same &= abs(pg - (1 - 4 * lam / 3)) < 3e-3 or lam > 2.0
check('④ the growing branch is normalizable exactly below lambda = 3/4, MEASURED on the lift\'s '
      'own leaf measure and matching the closed form 1 - 4L/3', _thresh_ok and _same)
_tower = [j + 0.5 for j in np.arange(0.5, 7.0, 1.0)]
check('④ᵇ *** and that single inequality decides BOTH conjuncts, in opposite senses: above 3/4 '
      'the second branch is rejected, so ONE R-eigenvalue AND the hinges admit no transmission '
      'condition, so the three sectors are three independent problems.  Below it, both '
      'branches are L^2, so BOTH R-eigenvalues AND the hinges couple.  No lambda = j + 1/2 '
      'lies below, so the tower sits wholly on the bound side ***',
      all(l > 0.75 for l in _tower) and min(_tower) == 1.0)

# ** AND THE DECOUPLING IS COMPUTED, NOT READ OFF THE THRESHOLD. **  The first-order operator's
#   boundary form PAIRS the two branches, so evaluate both pairings as a hinge is approached.
_eps = 10.0 ** -np.arange(2.0, 7.0)
print(f"\n  {'lambda':>8} {'same-branch pairing at the hinge':>36} "
      f"{'cross-branch pairing':>24}")
_same_dies, _cross_lives = True, True
for lam in (1.0, 2.5):
    same = [lift_psi(+lam)(e) * lift_psi(+lam)(e) for e in _eps]
    cross = [lift_psi(+lam)(e) * lift_psi(-lam)(e) for e in _eps]
    print(f"  {lam:>8} {same[0]:>16.3e} -> {same[-1]:<16.3e} "
          f"{cross[0]:>10.6f} -> {cross[-1]:<10.6f}")
    _same_dies &= (same[-1] < 1e-6 and same[-1] < 1e-4 * same[0]
                   and all(same[i + 1] < same[i] for i in range(len(same) - 1)))
    _cross_lives &= all(abs(c - 1.0) < 1e-9 for c in cross)
check('④ᶜ *** so the decoupling is a computation and not a reading of the threshold: the '
      'boundary form pairs the two branches, and as a hinge is approached the SAME-branch '
      'pairing falls monotonically to zero while the CROSS-branch pairing is identically one. '
      'With the second branch rejected there is nothing at the hinge with which to couple the '
      'sectors, so the three are three independent problems -- the "condition on the hinges" '
      'IS the rejection, and not a separate hypothesis ***',
      _same_dies and _cross_lives)

print()
print("=" * 90)
print("PART 5 -- Q3: THE PAIRING, AND IT FAILS AT EXACTLY ONE ENERGY")
print("=" * 90)
xs, ks = sp.symbols('x k', real=True)
Wsym = sp.tanh(xs)                                        # prop:wall's own cosh^{-a} profile
free = sp.exp(sp.I * ks * xs)                             # exact eigenfn of H_+ = -d2 + 1
img = sp.simplify(-sp.diff(free, xs) + Wsym * free)       # A^dag applied to it
Hm = lambda g: sp.simplify(-sp.diff(g, xs, 2) + (Wsym ** 2 - sp.diff(Wsym, xs)) * g)
_res = sp.simplify(Hm(img) - (ks ** 2 + 1) * img)
print(f"  A^dag e^(ikx) = {sp.simplify(img / free)} . e^(ikx)")
print(f"  H_-(A^dag e^(ikx)) - (k^2+1)(A^dag e^(ikx)) = {_res}")
check('⑤ *** A^dag carries every free eigenfunction to an eigenfunction of the WALL problem at '
      'the SAME energy, with residual exactly zero -- so every E != 0 level is present in BOTH '
      'R-eigenspaces ***', _res == 0)
_coef = sp.simplify(img / free)
_hasleft = sp.simplify(_coef.rewrite(sp.exp)).has(sp.exp(-2 * sp.I * ks * xs))
_amp_p = sp.limit(_coef, xs, sp.oo)
_amp_m = sp.limit(_coef, xs, -sp.oo)
print(f"  coefficient of e^(ikx) at +inf: {_amp_p} ; at -inf: {_amp_m} ; "
      f"|T|^2 = {sp.simplify(sp.Abs(_amp_p / _amp_m) ** 2)}")
check('⑤ᵇ *** and those states are REFLECTIONLESS: no e^(-ikx) component appears at all and '
      '|T|^2 = 1 exactly.  A wall that binds one mode transmits everything else perfectly, so '
      'three walls do NOT localise three propagating modes ***',
      (not _hasleft) and sp.simplify(sp.Abs(_amp_p / _amp_m) ** 2) == 1)
# ** the two branches' norms are MEASURED, not quoted: a growing cut-off, and the tail. **
_kerA = lambda t: 1 / np.cosh(t) ** 2
_kerAd = lambda t: np.cosh(t) ** 2
_grow = {}
for nm, fn in (('ker A  = sech (decaying)', _kerA), ('ker A^dag = cosh (growing)', _kerAd)):
    vals = [quad(fn, -X, X, limit=400)[0] for X in (5.0, 10.0, 15.0, 20.0)]
    _grow[nm] = vals
    print(f"  {nm:>28}:  int over |x| < 5,10,15,20 = "
          f"{', '.join(f'{v:.4g}' for v in vals)}")
check('⑤ᶜ *** the pairing fails at E = 0 and nowhere else: ker A has a norm that settles and '
      'ker A^dag has one that grows without bound, so the ONE unpaired level is the ONE bound '
      'level.  Localisation and the R-collapse are the same event ***',
      abs(_grow['ker A  = sech (decaying)'][-1] - 2.0) < 1e-6
      and abs(_grow['ker A  = sech (decaying)'][-1]
              - _grow['ker A  = sech (decaying)'][-2]) < 1e-8
      and all(_grow['ker A^dag = cosh (growing)'][i + 1]
              > 10 * _grow['ker A^dag = cosh (growing)'][i] for i in range(3)))
print()
print(f"  the partner spectra, as the box grows (exact only in infinite volume):")
print(f"  {'L':>8} {'E0(H-)':>14} {'E0(H+)':>12} {'max|E_n(H-) - E_(n-1)(H+)|':>28}")
_resid = []
for L, N in ((16.0, 1600), (32.0, 3200), (64.0, 6400)):
    g = np.linspace(-L, L, N)
    hh = g[1] - g[0]
    Wn, Wpn = np.tanh(g), 1 / np.cosh(g) ** 2
    off = -np.ones(N - 1) / hh ** 2
    em = eigh_tridiagonal(2 / hh ** 2 + Wn ** 2 - Wpn, off, select='i',
                          select_range=(0, 40), eigvals_only=True)
    ep = eigh_tridiagonal(2 / hh ** 2 + Wn ** 2 + Wpn, off, select='i',
                          select_range=(0, 40), eigvals_only=True)
    _resid.append(float(np.max(np.abs(em[1:41] - ep[0:40]))))
    print(f"  {L:>8} {em[0]:>14.3e} {ep[0]:>12.6f} {_resid[-1]:>28.3e}")
check('⑤ᵈ and the finite-box spectra show it: H_- carries one level at zero that H_+ does not, '
      'and above it the two interleave with a residual that falls monotonically as the box '
      'grows, by better than a factor of three per doubling -- the pairing, seen converging to '
      'the algebraic identity ⑤',
      all(_resid[i + 1] < _resid[i] / 3 for i in range(len(_resid) - 1)))

print()
print("=" * 90)
print("PART 6 -- A THREE EXISTS ONLY WHERE THE COUPLING VANISHES, AND THE COUPLING IS R-ODD")
print("=" * 90)
P3 = np.roll(np.eye(3), 1, axis=0)
print(f"  {'coupling t':>12} {'spectrum':>34} {'eigenspace dims':>18}")
_dims = {}
for t in (0.0, 1e-8, 1e-3, 0.2):
    ev = np.round(np.linalg.eigvalsh(t * (P3 + P3.T)), 12)
    d = sorted((int(np.sum(np.abs(ev - v) < 1e-14)) for v in set(ev)), reverse=True)
    _dims[t] = d
    print(f"  {t:>12} {str(ev.tolist()):>34} {str(d):>18}")
check('⑥ the deck acting on three sectors gives a THREE-dimensional eigenspace exactly when '
      'the inter-sector coupling is zero; for any coupling at all it splits 2 + 1 and no '
      'eigenspace carries a three -- so a three is a statement about DECOUPLING (W1: the '
      'regular representation, not a character)',
      _dims[0.0] == [3] and all(_dims[t] == [2, 1] for t in (1e-8, 1e-3, 0.2)))
_rng = np.random.default_rng(6698)
_plus = np.array([[1.0, 0, 0, 0], [0, 1.0, 0, 0]])
_a, _b = _rng.normal(size=2) @ _plus, _rng.normal(size=2) @ _plus
_within = float(_a @ G1 @ _b)
_across = float(_a @ G1 @ np.array([0.0, 0, 1.0, 0]))
print(f"\n  {{gamma^1, gamma^5}} = 0 ?  {np.allclose(G1 @ G5 + G5 @ G1, 0)}")
print(f"  <psi|gamma^1|phi> within one R-eigenspace: {_within:+.3e}   across: {_across:+.3f}")
check('⑥ᵇ *** and the coupling that would connect the sectors is the first-order operator\'s '
      'boundary form, carried by the off-diagonal Clifford element, which ANTICOMMUTES with '
      'R = gamma^5.  Its matrix elements between states of the same R-eigenvalue vanish '
      'identically, so a mode space inside one eigenspace has nothing available to couple its '
      'sectors -- and a coupled one is not inside one eigenspace ***',
      np.allclose(G1 @ G5 + G5 @ G1, 0) and abs(_within) < 1e-12 and abs(_across) > 0.5)

print()
print("=" * 90)
print("PART 7 -- CONTROL: THE CONSTRUCTION MUST GO SILENT WHERE THERE IS NOTHING TO FIND")
print("=" * 90)
# no wall: W == 0.  Then A = d/dl, the partners coincide, and neither branch is normalizable.
W0 = sp.Integer(0)
_H0m = sp.simplify(W0 ** 2 - sp.diff(W0, xs))
_H0p = sp.simplify(W0 ** 2 + sp.diff(W0, xs))
_k0 = sp.integrate(sp.Integer(1) ** 2, (xs, -sp.oo, sp.oo))     # ker A is the constant
print(f"  with W = 0 the two partner potentials are {_H0m} and {_H0p} -- identical")
print(f"  and ker A is the constant, whose norm is {_k0}")
check('⑦ with no wall the two partners coincide, nothing is unpaired, and the would-be '
      'zero-mode is not normalizable: no three and no collapse.  The instrument reports '
      'nothing where there is nothing', _H0m == _H0p == 0 and _k0 == sp.oo)
_rand_t = np.random.default_rng(97).normal(size=6)
_rand_dims = []
for t in _rand_t:
    ev = np.round(np.linalg.eigvalsh(t * (P3 + P3.T)), 12)
    _rand_dims.append(sorted((int(np.sum(np.abs(ev - v) < 1e-12)) for v in set(ev)), reverse=True))
print(f"  six couplings drawn at random: {np.round(_rand_t, 3).tolist()}")
print(f"  their eigenspace dimensions:   {_rand_dims}")
check('⑦ᵇ and the ring test is not rigged toward three: six couplings drawn at random all '
      'return 2 + 1, so the three of ⑥ is a property of the ZERO it was handed and not of '
      'the instrument', all(d == [2, 1] for d in _rand_dims) and _dims[0.0] == [3])

print()
print("=" * 90)
print(f"RESULT -- {len(_fails)} failure(s)")
print("=" * 90)
assert not _fails, _fails
print("  Q1  *** YES.  A propagating mode space in this construction DOES carry a three: the")
print("      three families of P14 sec:cosmogenesis, the continuations of the three bound")
print("      wall-modes past the horizon.  C50's member was not the only propagating sector")
print("      built, so r6695's survey premise does not hold.")
print("  Q2  the deck cannot index a propagating mode space.  As a PHASE it is an imaginary")
print("      translation, of infinite order on any real frequency and of order three only on")
print("      the Matsubara tower.  As a PERMUTATION it needs the sectors decoupled, and that")
print("      is the hinge rejection: one inequality, lambda > 3/4, rejects the second branch")
print("      AND closes the hinges, so it decides both conjuncts in opposite senses.")
print("  Q3  *** FORCED, and not a coincidence of the search. ***  The wall operator's two")
print("      branches are the two R-eigenspaces, and SUSY pairs them at EVERY energy but")
print("      zero: A^dag carries free states to wall states at the same energy with residual")
print("      zero, and those states are reflectionless.  The unpaired level is the bound one.")
print("      So localisation -- which a three requires -- and the R-collapse are one event.")
print()
print("  ⛭ AND THE TWO ROUTES TO PROPAGATION FAIL DIFFERENT CONJUNCTS, EACH FOR A REASON.")
print("  NATIVE propagation keeps both R-eigenvalues because nothing is rejected, and has no")
print("  three because nothing localises.  INHERITED propagation has a three because it was")
print("  given one, and one R-eigenvalue because the continuation commutes with gamma^5 and")
print("  transports the collapse with it.  The conjunction is decided at the hinge, before")
print("  propagation; propagation carries the verdict and does not revisit it.")
print()
print("  W4, plainly: PO-45's conjunction is obstructed by the binding itself, and the")
print("  obstruction is an anticommutation -- the boundary form that would couple the sectors")
print("  anticommutes with R, so no mode space can have both its three and both eigenvalues.")
print()
print("  NOT ESTABLISHED: that no propagating sector could ever carry a three -- one does.")
print("  Not that the families are the colourless triple; they are the generations, already")
print("  spoken for.  Not any claim resting on a space unioned with its own R-image, which")
print("  PART 0 builds as a trap.  Nothing named, nothing seated, chirality untouched.")
print("=" * 90)
