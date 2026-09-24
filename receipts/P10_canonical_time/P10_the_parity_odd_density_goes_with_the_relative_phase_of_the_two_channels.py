"""
P10_the_parity_odd_density_goes_with_the_relative_phase_of_the_two_channels
==========================================================================

Object under test -- the sentence `r6803` put into `P10`.  The caveat used to read that the Pontryagin
density is "non-zero at second order for a *circularly* polarised mode" and that "a linearly polarised
mode returns zero"; node 60 flagged that this invites the one configuration that vanishes, and `r6803`
replaced the prescription with a property of the configuration: the density goes with the relative phase
of the two channels, vanishing a quarter-cycle apart and largest in step.  ** That sentence currently
stands on a scratch computation offered as routing.  This receipt puts a derivation behind it, which is
node 66's own reason for asking: with a receipt the sentence can cite one instead of standing on a
reading. **

** WHAT IS ESTABLISHED ALREADY AND IS RE-RUN HERE RATHER THAN QUOTED. **  `r6766` computed, on `P11`'s
unpolarised Gowdy--de~Sitter form with every metric function arbitrary: a pure plane wave gives *RR == 0
however it is polarised; restoring the areal factor makes it nonzero; and silencing either channel --- by
REBUILDING the metric with that function constant, not by substituting a symbol and leaving its
derivatives standing --- kills it.  ** So the source is the product of the two channels' rates, psi' omega',
and not "the twist" as a thing on its own. **  The machinery is `exec`-imported out of `r6762`'s receipt and
`gowdy` out of `r6766`'s, so the three cannot drift apart.

** WHAT IS NEW: THE CYCLE AVERAGE, WHICH IS WHERE A PHASE CAN LIVE AT ALL. **  Put both channels on one
wavenumber a phase delta apart --- psi = eps sin(k u), omega = eps sin(k u + delta), u the retarded time ---
and average over a wavelength:

      < psi' omega' >  =  (k^2 eps^2 / 2) cos(delta)

      delta = 0          in step                       MAXIMAL, + k^2 eps^2 / 2
      delta = pi/2       a quarter-cycle apart         EXACTLY ZERO
      delta = pi         in anti-phase                 MAXIMAL, - k^2 eps^2 / 2
      either channel silenced                          EXACTLY ZERO

** So the configuration that the old wording reached for is the one that returns nothing, and the
configuration it called a null case --- the two channels in step --- is the maximum. **  *That is `P10`'s
corrected sentence, derived.*

** AND THE PARITY ARGUMENT IS DERIVED IN THE SAME LINE RATHER THAN QUOTED FROM THE OTHER SIDE. **  The
transverse reflection sends omega -> -omega, which on these profiles is delta -> delta + pi, and cos is odd
about pi/2: the density is odd, so its average vanishes on any parity-symmetric ensemble.  ** That is what
`P10` says from the state's side --- "a parity-odd term is not excluded by the geometry, and whatever
excludes it does so through the state" --- and it is here a property of the integrand instead of a
statement about the ensemble. **

⌗ AND THE ONE THING THIS SHARPENS BEYOND THE SENTENCE.  `r6770` closes the baryogenesis-analogue route by
establishing that the two towers are POPULATED ALIKE.  ** Balanced populations do not by themselves kill a
CROSS-correlation, and psi' omega' is a cross-correlation: what kills it is parity-symmetry of the
ensemble, which is a statement about relative phase and not about occupation numbers. **  `r6770`'s
conclusion is not endangered --- the parity argument is the one the corpus actually rests on and it is
computed here --- but the route to it is narrower than "the populations are equal", and if the route is
ever reopened this is where to look.  *Node 66 accepted exactly this reading and said it needs no paper
edit; the receipt is so that the distinction is in the record where a reopening would find it.*

COMPUTES: scope -- what this settles and what it does not.
  * The configuration dependence is derived on the PLANE-WAVE member of the Gowdy form with an areal
    factor --- a torus block.  ** `P10`'s mode is on the three-sphere layer.  These are different
    configurations, so this is support for the sentence's FORM and not a computation of `P10`'s own
    member. **  `r6766` draws the same line and it is not blurred here.
  * One wavenumber, both channels on it, equal amplitudes.  ** That is the configuration in which a
    relative phase is even defined **; nothing here is a statement about a superposition of wavenumbers or
    about unequal amplitudes, and the receipt does not average over an ensemble it has not specified.
  * `eps` and `k` are carried symbolically and cancel out of every ratio.  The only number is the factor
    1/2 in the cycle average, which is exact.
  * ** It does NOT supply a chiral state and does not reopen `r6770`. **  The construction inherits its
    primordial amplitude and tilt; `P14` has it that the geometry permits the chirality-asymmetric action
    and does not select it.  Nothing here changes that and nothing here bears on `PO-7`.

ORIGIN: offered as routing in `FOR_64`, moved to node 66 on its invitation, and receipted at 66's "yes,
please" so `P10`'s corrected caveat can cite a computation.  `r6766`'s three facts are re-run first.
"""
import itertools  # noqa: F401  -- the exec'd machinery needs it
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_RECEIPTS = os.path.dirname(_HERE)
_MACH = os.path.join(_RECEIPTS, 'P14_matter_sector_paper',
                     'P14_the_constituent_count_is_conserved_on_every_static_member'
                     '_and_the_twist_alone_violates_it.py')
_GOWDY = os.path.join(_RECEIPTS, 'P15_CR_cosmology',
                      'P15_the_history_is_spherically_symmetric_throughout_so_the_chern_simons'
                      '_number_never_moves.py')

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

# ** THE MACHINERY IS READ OUT OF THE RECEIPTS THAT BUILT IT, NOT RE-TYPED. **  r6762 holds the
# Pontryagin construction (the curvature antisymmetries as storage) and r6766 holds `gowdy`; taking both
# by source means this receipt cannot drift from either.
with open(_MACH, encoding='utf-8') as fh:
    _src = fh.read()
_a = _src.index('PAIRS = [(0, 1)')
_b = _src.index("t, r, u, th, ph, z, x, y = sp.symbols")
exec(compile(_src[_a:_b], _MACH, 'exec'))                                   # noqa: S102
with open(_GOWDY, encoding='utf-8') as fh:
    _gsrc = fh.read()
_c = _gsrc.index('def gowdy(')
_d = _gsrc.index('\n\n', _gsrc.index('return g', _c))
exec(compile(_gsrc[_c:_d], _GOWDY, 'exec'))                                 # noqa: S102

t, z, x, y = sp.symbols('t z x y', real=True)
CHEAP = sp.cancel
u = t - z
k, eps, dl = sp.symbols('k epsilon delta', positive=True), None, None
k = sp.Symbol('k', positive=True)
eps = sp.Symbol('epsilon', positive=True)
dl = sp.Symbol('delta', real=True)

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — r6766's THREE FACTS RE-RUN, BECAUSE NOTHING BELOW IS READABLE WITHOUT THEM")
print("=" * 94)
F, G = sp.Function('psi')(u), sp.Function('omega')(u)
flat = sp.simplify(pontryagin(gowdy(0, F, G, 1), [t, z, x, y], simp=CHEAP))       # noqa: F821
areal = sp.simplify(pontryagin(gowdy(0, F, G, t), [t, z, x, y], simp=CHEAP))      # noqa: F821
kill_om = sp.simplify(pontryagin(gowdy(0, F, sp.Symbol('om0', real=True), t),     # noqa: F821
                                 [t, z, x, y], simp=CHEAP))
kill_ps = sp.simplify(pontryagin(gowdy(0, sp.Symbol('ps0', real=True), G, t),     # noqa: F821
                                 [t, z, x, y], simp=CHEAP))
print(f"    plane wave, R = 1, both channels arbitrary:   *RR = {flat}")
print(f"    the same with the areal factor R = t:         *RR nonzero: {areal != 0}")
print(f"    omega constant (one channel silenced):        *RR = {kill_om}")
print(f"    psi   constant (the other silenced):          *RR = {kill_ps}")
check("a pure plane wave gives exactly zero, however polarised", flat == 0)
check("restoring the areal factor makes it nonzero", sp.simplify(areal) != 0)
check("silencing either channel kills it, so the source is the PRODUCT of the two",
      sp.simplify(kill_om) == 0 and sp.simplify(kill_ps) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 — THE DENSITY IS psi' omega' TIMES SOMETHING THAT CARRIES NEITHER CHANNEL")
print("=" * 94)
# psi and omega are functions of u = t - z, so d/dt of each IS its rate in the retarded time
# psi and omega are functions of u = t - z, so d/dt of each IS its rate in the retarded time
prod = sp.diff(F, t) * sp.diff(G, t)
quot = sp.simplify(sp.cancel(areal / prod))
print(f"    *RR / (psi' omega') = {quot}")
_ders = quot.atoms(sp.Derivative)
_hasom = G in quot.atoms(sp.Function)
print(f"    derivatives of either channel left in the weight: {_ders if _ders else 'none'}")
print(f"    any omega dependence left in the weight:          {_hasom}")
check("⚑ the density factorises as psi'(u) omega'(u) times a weight carrying NO derivative of "
      "either channel", not _ders)
check("and no omega at all -- the omega dependence is exactly one factor of its rate", not _hasom)
print("""
  ** THE WEIGHT IS exp(2 psi) / t^3 UP TO SIGN, AND THAT MATTERS TWICE. **  It is strictly positive, so
  the density's SIGN and ZEROS are exactly psi' omega''s -- that is exact, not perturbative.  And it is an
  AMPLITUDE factor rather than a rate, so at the order `P10`'s sentence is about -- second order in the
  metric perturbation -- it is 1 + O(eps) and the second-order density is psi' omega' times a positive
  function of t.
""")
_w = sp.simplify(quot * t ** 2 * sp.Abs(t) / -8)
print(f"    weight * t^2 |t| / (-8) = {_w}")
check("the weight is -8 exp(2 psi)/(t^2 |t|), so it never vanishes and never changes sign",
      sp.simplify(_w - sp.exp(2 * F)) == 0)
check("so the zeros of the density are exactly the zeros of psi' omega'",
      sp.solve(sp.Eq(_w, 0), F) == [])

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (THE NEW RESULT) — THE CYCLE AVERAGE, AND THE PHASE IT DEPENDS ON")
print("=" * 94)
print("""
  A relative phase is defined when both channels sit on one wavenumber.  Put them there and average the
  product of the rates over a wavelength in the retarded time.
""")
uu = sp.Symbol('u', real=True)
psi_c, om_c = eps * sp.sin(k * uu), eps * sp.sin(k * uu + dl)
integrand = sp.diff(psi_c, uu) * sp.diff(om_c, uu)
avg = sp.simplify(sp.integrate(integrand, (uu, 0, 2 * sp.pi / k)) / (2 * sp.pi / k))
print(f"    < psi' omega' > = {avg}")
check("⚑ the cycle average is (k^2 eps^2 / 2) cos(delta)",
      sp.simplify(avg - k ** 2 * eps ** 2 * sp.cos(dl) / 2) == 0)
for lab, val, expect in (("in step,           delta = 0", 0, k ** 2 * eps ** 2 / 2),
                         ("quarter-cycle,     delta = pi/2", sp.pi / 2, 0),
                         ("anti-phase,        delta = pi", sp.pi, -k ** 2 * eps ** 2 / 2)):
    got = sp.simplify(avg.subs(dl, val))
    print(f"    {lab:34s} < psi' omega' > = {got}")
    check(f"{lab.split(',')[0].strip()} gives {'zero' if expect == 0 else 'the extremum'}",
          sp.simplify(got - expect) == 0)
check("⛔ so the quarter-cycle configuration returns EXACTLY zero, which is the case the old wording "
      "reached for", sp.simplify(avg.subs(dl, sp.pi / 2)) == 0)
check("and the in-step configuration is the maximum, which the old wording called the null case",
      sp.simplify(avg.subs(dl, 0) - k ** 2 * eps ** 2 / 2) == 0)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 — AND IT IS PARITY-ODD, WHICH IS P10's CANCELLATION DERIVED RATHER THAN QUOTED")
print("=" * 94)
refl = sp.simplify(sp.integrate(sp.diff(psi_c, uu) * sp.diff(-om_c, uu), (uu, 0, 2 * sp.pi / k))
                   / (2 * sp.pi / k))
print(f"    under the transverse reflection omega -> -omega:  < psi' omega' > = {refl}")
print(f"    on these profiles that reflection is delta -> delta + pi:          "
      f"{sp.simplify(avg.subs(dl, dl + sp.pi))}")
check("the reflection flips the sign of the average", sp.simplify(refl + avg) == 0)
check("⚑ and delta -> delta + pi does the same, so the two descriptions agree",
      sp.simplify(avg.subs(dl, dl + sp.pi) + avg) == 0)
check("so a parity-symmetric ensemble averages it to zero, whatever an individual member returns",
      sp.simplify((avg + refl) / 2) == 0)

# =========================================================================================
print()
print("=" * 94)
print("WHAT THIS REVISION ESTABLISHES")
print("=" * 94)
print(f"""
  ** `P10`'s CORRECTED SENTENCE NOW HAS A COMPUTATION BEHIND IT. **  On the plane-wave member with an
  areal factor the parity-odd density factorises as psi'(u) omega'(u) times a STRICTLY POSITIVE weight,
  -8 exp(2 psi)/(t^2 |t|), which carries no derivative of either channel and no omega at all -- so the
  density's sign and zeros are exactly the product's, exactly rather than perturbatively.  Over a cycle,
  at the second order in the amplitude that `P10`'s sentence is about, that product is
  (k^2 eps^2/2) cos(delta): maximal with the channels in step,
  ** exactly zero a quarter-cycle apart **, and zero if either channel is silenced.  *So the
  configuration the old wording prescribed is the one that vanishes, and the one it dismissed is the
  maximum.*

  ** AND THE PARITY CANCELLATION IS A PROPERTY OF THE INTEGRAND HERE. **  omega -> -omega is
  delta -> delta + pi and flips the sign, so a parity-symmetric ensemble kills it without any statement
  about occupation numbers.  ⌗ *Which is the sharpening `r6770` invites: balanced POPULATIONS do not by
  themselves kill a CROSS-correlation.  `r6770`'s conclusion stands on the parity argument, which is
  computed; its route through equal populations is narrower than it reads.*

  ⚠ WHAT THIS IS NOT.  A torus block and not `P10`'s three-sphere layer --- support for the sentence's
  FORM, not a computation of `P10`'s own member.  One wavenumber and equal amplitudes, which is where a
  relative phase is defined at all.  ** And no chiral state is supplied: `r6770` is not reopened, `P14`'s
  reading that the geometry permits the chirality-asymmetric action without selecting it is untouched,
  and nothing here bears on `PO-7`. **
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
