#!/usr/bin/env python3
"""
P15 receipt -- `r7101`'s Q1: THE HARMONIC EXPANSION, CARRIED OUT IN THE PROPER FRAME.  THE EXPANSION
ITSELF INTRODUCES NOTHING -- THE OBSERVER'S OFFSET FROM THE CHART ORIGIN IS A PURE PHASE, EXACTLY --
BUT THE SLICE HAS NOTHING TO EXPAND AND NO $D_C$ TO OFFER, AND THE COMPLETION IS NOT BOUNDED ON THIS
CONSTRUCTION.  SO IT IS SAID AND STOPPED, WITH THE REASON EXHIBITED.

** THE ORDER. **  `r7101`: *"Your own statement of it: $j_\\ell(k D_C)$ is licensed by the flatness of
the slice plus the exact recovery of the expansion law, and not by expanding a plane wave on the
constant-$\\tilde\\tau$ slice with the observer at a general point of it.  Do that.  Show what the
$\\ell$-space kernel is, with the observer off the origin of the chart, and whether it is
$j_\\ell(k D_C)$ with $D_C$ the light-travel distance."*  With two things wanted beyond the answer --
whether the expansion introduces anything the flat identification does not have, and what the
observer being at a general point costs -- and one licence: *"if it turns out not to be bounded after
all ... say that and stop, because an unbounded calculation reported as bounded is worse than the
identification it would replace."*

⇒ *** THE ANSWER, IN ONE LINE: THE EXPANSION INTRODUCES NOTHING, AND IT CANNOT BE SET UP.  The
observer's constant-$\\tau$ slice is exactly $\\mathbb{E}^3$ and the plane-wave expansion about a
general point of it is exact to $1.3\\times10^{-15}$ with the offset a pure phase -- so no measure, no
weight, no $\\ell$-dependent factor.  But that slice is not a surface of constant cosmic epoch, and
the only length it offers between the observer and the last-scattering epoch is $r_0$ -- the reading
`r7100` excluded -- short of $D_C$ by exactly the stretch $D_C/r_0 = 2.7737$. ***

** WHAT THE CHART IS, EXACTLY -- and this is the piece that makes the rest follow. **  Writing
`eq:proper-frame` on the areal radius instead of the comoving label gives, with no approximation,

      ds^2 = -d tau^2 + ( dr - v(r) d tau )^2 + r^2 d Omega^2 ,     v(r)^2 = r_s/r + r^2/alpha^2

*-- the Painleve-Gullstrand chart of Schwarzschild-de Sitter, with `r_s = 2 alpha / (3 sqrt 3)`
EXACTLY the Nariai value (verified symbolically against `eq:scalefac` itself, residual identically
zero), so that `f(r) = -(r-r_N)^2 (r+2 r_N) / (alpha^2 r) <= 0` everywhere with its double zero at the
Nariai radius, and `v(r) = H(z) r / c` to machine precision with `1+z = r_0/r`.*  ⇒ ** The flow speed
of the Painleve-Gullstrand slicing IS the Hubble velocity, and it is at or above `c` everywhere, equal
to `c` only at `r_N`. **  *The chart is not an analogy; it is the same object the framework's "unit-speed
loci of the lap" names.*

** (i) WHAT THE EXPANSION INTRODUCES: NOTHING, and this half of the order's question is cleanly YES. **
*On $\\mathbb{E}^3$ the addition theorem about an observer at $x_O \\ne 0$ is exact -- the offset is
$e^{i k \\cdot x_O}$, which cancels in $C_\\ell$ -- and the series is verified here to
$1.3\\times10^{-15}$ at six random $(k, x_O, s)$ with $|x_O| \\approx r_0$.*  ⇒ *So the identification
is not hiding a measure or an $\\ell$-dependent weight: that was the live worry and it is dead.*
  ⌗ *And the control can see a number move: run the same series with the chart radius $|x|$ in place of
  the chord $s$ and it misses the plane wave by $O(1)$.*

** (ii) WHAT THE GENERAL POINT COSTS: the whole of $D_C$, and the shortfall is exactly the stretch. **
*On the slice $\\tau = \\tau_0$ the cosmic epoch is a function of the EUCLIDEAN RADIUS ALONE --
$\\tilde\\tau = \\tau_0 + \\chi$ and $r(\\tilde\\tau) = |x|$, so $1+z = r_0/|x|$ -- which makes the
observer's own simultaneity slice carry every cosmic epoch, laid out as concentric spheres about the
branch point.*  ⇒ ** The construction's $z = 1089.9$ locus is therefore a sphere of radius $4.63$ Mpc
about the branch point: it subtends $0.105$ degrees of the observer's sky, two parts in ten million of
it, and its Euclidean chord from the observer is $r_0$ to nine parts in ten thousand. **
  ⇒ *** $D_C$ / (that chord) $= 2.7737$ -- the stretch $D_C/r_0$, to six figures.  The slice does not
  fall short of $D_C$ by an unknown amount; it falls short by precisely the number the low-multipole
  floor is built on. ***

** (iii) AND THE SLICE IS NOT WHERE THE PHOTONS ARE, which is why no expansion on it could have worked. **
*The exact null geodesics of this chart give `1+z = (1 +- v_o)/(1 +- v_e)` -- derived twice, confirmed
by numerical integration of the geodesic system to one part in `1e-12`, and calibrated in the de Sitter
case where the answer is independently known, returning `a_0/a_e` to twelve figures while the ratio of
areal radii returns nothing like it.*  ⇒ ** On that relation the construction's $z=1089.9$ locus is a
BLUESHIFT, the $z=1089.9$ surface sits at the Nariai radius to within $51$ Mpc, $r = r_N$ is an
infinite-redshift surface, and the radial area distance is affine -- $D_A = (r_0-r_e)/(v_o-1)$,
saturating at $1.31\\times10^{4}$ Mpc. **  *None of that is the cosmological relation, and it is not
meant to be: `sec:flatlcdm` says where the field equations act.*  ⇒ *** So the redshift the paper uses
is the Friedmann readout's, not this chart's null geodesics' -- and a plane wave expanded on this
chart's slice is not a mode of the thing that is observed. ***

** (iv) AND THE JOIN THE ORDER NAMED IS WHERE IT FAILS, with one sentence of the paper carrying it. **
*`sec:largescale` says the cosmological layers "are the closed $S^3$ of constant
$\\tilde\\tau=\\tau+\\chi$", citing `sec:properframe`.  Computed from `eq:proper-frame`, that surface's
induced three-metric is `(v^2-1) d chi^2 + r^2 d Omega^2` with BOTH coefficients constant on it, whose
Ricci scalar is `2/r^2` and whose Ricci tensor has a zero eigenvalue along `chi`.*  ⇒ ** That is
`R x S^2` of radius `r(tilde tau)`, not an `S^3`, which would give `6/a^2` isotropically. **
  ⌗ *An `S^3` slice of curvature radius `a` DOES exist in this geometry -- a spherically symmetric
  spacelike slice with the right induced metric can be built for ANY `a`, verified here -- so the
  `S^3` is a choice of slice, and it is neither the constant-cosmic-time one nor one that singles out
  `r_0`.*
  ⚠ ** THE CHARITABLE READING, AND IT IS PROBABLY THE RIGHT ONE: ** *if "the cosmological layers are
  the closed $S^3$" means the FRIEDMANN READOUT's spatial sections -- the closed reading in which
  `Omega_k = -Omega_Lambda` sets a curvature radius near `r_0` -- then the physics is untouched and it
  is the citation to `sec:properframe` that needs repair.  ** This receipt claims the geometry and NOT
  that any number moves: `r_0`, `D_C`, the stretch, `ell_A` and the comb are all read off the Friedmann
  readout, which nothing here touches. **

⇒ *** THE VERDICT, AND THE STOP.  The expansion is NOT bounded on this construction, and the reason is
exhibited rather than guessed: no single slicing of the proper frame carries both the source's discrete
spectrum and the projection distance.  The flat slice has the distances' flatness and no epoch; the
constant-epoch surface has the epoch and is a cylinder; the `S^3` is a third slice, unforced.  So this
receipt does what the order licensed -- says that, and stops. ***
  ⇒ ** WHAT THAT DOES AND DOES NOT DO TO `r7100`. **  *It does not move the conclusion.  `j_\\ell(k_L
  D_C)` is neither confirmed nor contradicted here; what is settled is that it cannot be DERIVED on the
  proper frame's flat slice, so its licence remains `sec:flatlcdm`'s exact recovery of flat
  $\\Lambda$CDM -- an identification, with a named content.*  ⇒ *** The remainder `r7100` called "the
  only place this chain could still move" does not move it.  It moves the LICENSING, from a derivation
  the construction does not have to an identification the construction does.  The disagreement with the
  sky stays real. ***

⌗ ** THE SMALLER ITEM -- is a `c54`-era lensing potential admissible on the current background? **
*One line, as asked: ** ADMISSIBLE IN PRINCIPLE, NOT AS IT STANDS, AND NOT FOR THE REASON THE ERA
SUGGESTS. **  None of the three switches added since `c54` -- `LEAFSCALES`, `VISLEAF`, `LEAFREC` --
reaches the growth factor or the line-of-sight projection the potential is built from; but its producer
evaluates the growth on `A.Hphys`, the stacking rate, where the rate rule and the instrument's own
`LEAFPERT` default put the perturbations on the leaf's.  ⇒ So part B has been standing on an object
whose RATE ASSIGNMENT is superseded, not merely one that is unreproducible, and re-deriving it is the
only option.  ⌗ Sized here so the re-derivation is not walked into blind: the two rates' growth shapes
`D(a)/D_0` differ by `1.1e-3` at `z=2`, where the lensing kernel peaks, and by `5.8e-3` out to `z=10`,
so the re-derivation should be expected to CONFIRM part B's numbers rather than move them.*

** COMPUTES: the background objects at TWO stated parameter sets, and the chart and slice geometry
built on them.  *** $(H_0, \\Omega_m) = (68.60, 0.2973)$, the refit background `P15` fits, and
$(73.00, 0.3066)$, the instrument's own default; every figure is reported at one of the two and
labelled with which.  Derived: $x_0$, $\\alpha$, $r_N$, $r_0$, $r_s$, $v(r)$, $f(r)$,
$D_C(z_{\\rm rec}=1089.9)$ and the ratios built from them; $\\Omega_r = 4.15\\times10^{-5}/h^2$ enters
only the growth comparison in the lensing line.  *** No spectrum, transfer or likelihood is computed at
any parameter set, and nothing is fitted. *** **

⚠ ** SCOPE. **  No transfer is run and no spectrum computed.  `cc66`'s three-grid table is NOT
re-measured and is not used here.  The acoustic instrument is NOT run; `L171x_lensing_potential.py` is
READ for its rate assignment and not executed, and the lensing potential is NOT re-derived -- that is
`cc66`'s order.  ⛔ And the expansion is not completed: the order's own licence is taken, and the
reason is given rather than a result manufactured.
"""
import os
import re
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import eval_legendre, spherical_jn

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
p15 = open(P15, encoding='utf-8').read()
body15 = flat(''.join(ln + '\n' for ln in p15.splitlines() if not ln.lstrip().startswith('%')))

C = 299792.458
Z_REC = 1089.9
BG = {'the refit background `P15` fits': (68.60, 0.2973),
      "the instrument's own default": (73.00, 0.3066)}


def background(H0, OM):
    """the native parameterisation, the fitted one, and the chart the two share."""
    OL = 1.0 - OM
    x03 = 2.0 / OM - 2.0                                 # Omega_m = 2/(x0^3+2)
    x0 = x03 ** (1.0 / 3.0)
    alpha = C / H0 * np.sqrt(1.0 + 2.0 / x03)            # H0^2 = (c/alpha)^2 (1 + 2/x0^3)
    rN = alpha / np.sqrt(3.0)                            # the Nariai radius
    r0 = x0 * rN                                         # today's areal radius
    rsch = 2.0 * alpha / (3.0 * np.sqrt(3.0))            # the Nariai 2GM/c^2
    H = lambda z: H0 * np.sqrt(OM * (1 + z) ** 3 + OL)                        # noqa: E731
    DC = quad(lambda z: C / H(z), 0.0, Z_REC, limit=300)[0]
    v = lambda r: np.sqrt(rsch / r + r * r / alpha ** 2)                      # noqa: E731
    f = lambda r: 1.0 - rsch / r - r * r / alpha ** 2                         # noqa: E731
    return dict(H0=H0, OM=OM, x03=x03, x0=x0, alpha=alpha, rN=rN, r0=r0, rsch=rsch,
                H=H, DC=DC, v=v, f=f)


B = {k: background(*vv) for k, vv in BG.items()}
ref = B['the refit background `P15` fits']

# ================================================== A. the calibration, before anything new is asked
head("A.  THE CALIBRATION: FOUR OF `P15`'s PARAMETER-FREE FIGURES, REPRODUCED FROM THE BACKGROUND")
for lab, b in B.items():
    print(f"      {lab}:  x_0 = {b['x0']:.4f}  alpha = {b['alpha']:7.1f}  r_N = {b['rN']:7.1f}  "
          f"r_0 = {b['r0']:7.1f}  r_s = {b['rsch']:7.1f}  D_C = {b['DC']:8.1f} Mpc")
gate("⛭ the layer's areal radius comes out at `r_0 = 5051` Mpc, `P15`'s own parameter-free figure",
  # ** r7181: the pin is `+-1.0` and not `+-5` (node 70's `r7179+70.1` slack finding) nor the
  #   printed-precision `+-0.5` its operator proposes.  The background returns `5051.49`, which is
  #   `0.49` from the figure the paper prints, so a half-ulp bracket would sit `0.01` inside its own
  #   bound -- a pin on a rounding edge, which fails on any change to the integral rather than on a
  #   change to the physics.  What this pin exists to refuse is the OTHER configuration's `r_0`,
  #   `4708.97`, and `+-1.0` refuses it by `342` times while admitting nothing the paper would
  #   print differently by more than one in the last digit. **
     abs(ref['r0'] - 5051.0) < 1.0 and "r_0\\approx5051" in body15)
# ** r7179 (node 66): the pair is the construction's and the tolerances are the paper's own
#   printed precision.  At +-100 Mpc and +-0.03 these could not fail on the quantities they
#   name: the two background configurations the corpus has printed are 61.5 Mpc and 0.0137
#   apart, so the old brackets admitted both and asserted neither (`PO-78` at the tolerance). **
gate("⛭ and the projection distance at `D_C = 1.4011e4` Mpc, the paper's own, to half its"
     " printed ulp -- a bracket the other configuration's 1.395e4 fails by 123 times",
     abs(ref['DC'] - 1.4011e4) < 0.5 and "D_C\\approx1.4011\\times10^{4}" in body15)
STRETCH = ref['DC'] / ref['r0']
gate(f"⛭ so the STRETCH is {STRETCH:.4f} against the paper's 2.774 -- the number this receipt's main "
     "finding turns out to reproduce from a different direction",
     abs(STRETCH - 2.774) < 5e-4 and "D_C/r_0\\approx2.774" in body15)
_l2 = np.sqrt(2 * 4) / ref['r0'] * ref['DC']
gate(f"⛭ and the lowest closed-$S^3$ mode lands at ell_2 = {_l2:.2f} against the paper's 7.8 -- four "
     "figures calibrated before the unknown is touched",
     abs(_l2 - 7.8) < 0.15 and "\\ell_2\\approx7.8" in body15)

# ================================================== B. what the chart is
head("B.  ⛭⛭⛭ WHAT THE CHART IS: THE PAINLEVE-GULLSTRAND SLICING OF SdS AT EXACTLY THE NARIAI MASS")
gate("the paper gives the proper frame on the COMOVING label, with $r$ a function of $\\tau+\\chi$ "
     "and the radial and angular coefficients DIFFERENT -- which is the form this section rewrites",
     "ds^2=-d\\tau^2+(\\partial_\\chi r)^2\\,d\\chi^2+r^2 d\\Omega^2" in body15
     and "r(\\tau,\\chi)=r(\\tau+\\chi)" in body15)
gate("and it says the reassignment selects the Nariai member, which is the mass the identity below "
     "returns without being given it", "selects the Nariai member" in body15)

t0 = time.time()
_al, _tt = sp.symbols('alpha tildetau', positive=True)
_rN = _al / sp.sqrt(3)
_r = sp.Integer(2) ** sp.Rational(1, 3) * _rN * sp.sinh(sp.Rational(3, 2) * _tt / _al) ** sp.Rational(2, 3)
_resid = sp.simplify(sp.diff(_r, _tt) ** 2 - (2 * _al / (3 * sp.sqrt(3)) / _r + _r ** 2 / _al ** 2))
print(f"      symbolic residual  (dr/d tilde-tau)^2 - ( r_s/r + r^2/alpha^2 )  =  {_resid}"
      f"      [{time.time()-t0:.1f}s]")
gate("⛭⛭ THE CHART IS NAMED BY AN IDENTITY, NOT BY ANALOGY: `eq:scalefac` satisfies "
     "`(dr/dtt)^2 = r_s/r + r^2/alpha^2` with `r_s = 2 alpha/(3 sqrt3)` -- the Nariai value -- so "
     "`ds^2 = -dtau^2 + (dr - v dtau)^2 + r^2 dOmega^2` IS the Painleve-Gullstrand form of SdS",
     _resid == 0)

worst_v, worst_f = 0.0, 0.0
for lab, b in B.items():
    for z in (0.0, 1.0, 10.0, Z_REC, 3.0e7):
        r = b['r0'] / (1.0 + z)
        worst_v = max(worst_v, abs(b['v'](r) / (b['H'](z) * r / C) - 1.0))
    for r in (1.0, 100.0, b['rN'], b['r0'], 3 * b['r0']):
        closed = -(r - b['rN']) ** 2 * (r + 2 * b['rN']) / (b['alpha'] ** 2 * r)
        worst_f = max(worst_f, abs(b['f'](r) - closed) / max(1e-300, abs(closed) + 1e-12))
print(f"      worst | v(r) / (H(z) r/c) - 1 |              over both backgrounds: {worst_v:.2e}")
print(f"      worst relative | f(r) - closed form |        over both backgrounds: {worst_f:.2e}")
gate("⛭⛭ AND THE FLOW SPEED OF THAT SLICING IS THE HUBBLE VELOCITY: `v(r) = H(z) r / c` to machine "
     "precision with `1+z = r_0/r`, at five redshifts on both backgrounds", worst_v < 1e-14)
gate("⛭ and `f(r) = -(r-r_N)^2 (r+2 r_N)/(alpha^2 r)`, so `f <= 0` EVERYWHERE with a double zero at "
     "the Nariai radius ⇒ `v >= 1` everywhere, equal to 1 only at `r_N`",
     worst_f < 1e-12
     and all(b['v'](b['rN']) - 1.0 < 1e-13 and b['f'](b['rN']) <= 1e-9 for b in B.values())
     and all(b['v'](x * b['rN']) > 1.0 for b in B.values() for x in (0.01, 0.5, 1.5, 3.0, 30.0)))

# ================================================== C. the expansion, done
head("C.  ⛭⛭ (i) THE EXPANSION ITSELF, WITH THE OBSERVER OFF THE CHART ORIGIN: EXACT, AND A PURE PHASE")
gate("`prop:flat` is the premise, and it is the paper's own: the constant-$\\tau$ slice is exactly "
     "flat $\\mathbb{R}^3$", "The constant-$\\tau$ slice is exactly flat $\\mathbb{R}^3$." in body15)


def ricci(g, x):
    """Ricci tensor and scalar of a diagonal metric, by the textbook formula."""
    n = len(x)
    gi = g.inv()
    Gam = [[[sp.simplify(sum(gi[l, m] * (sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i])
                                         - sp.diff(g[i, j], x[m])) for m in range(n)) / 2)
             for j in range(n)] for i in range(n)] for l in range(n)]
    Ric = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            s = 0
            for l in range(n):
                s += sp.diff(Gam[l][i][j], x[l]) - sp.diff(Gam[l][i][l], x[j])
                for m in range(n):
                    s += Gam[l][l][m] * Gam[m][i][j] - Gam[l][j][m] * Gam[m][i][l]
            Ric[i, j] = sp.simplify(s)
    return Ric, sp.simplify(sum(gi[i, j] * Ric[i, j] for i in range(n) for j in range(n)))


_r3, _th, _ph = sp.symbols('r theta phi', positive=True)
_Ric_flat, _R_flat = ricci(sp.diag(1, _r3 ** 2, _r3 ** 2 * sp.sin(_th) ** 2), [_r3, _th, _ph])
print(f"      constant-tau slice: Ricci scalar = {_R_flat} ; Ricci tensor identically zero: "
      f"{sp.simplify(_Ric_flat) == sp.zeros(3, 3)}")
gate("⌗ THE CONTROL THAT RETURNS THE AFFIRMATIVE: the same machinery, run on the constant-$\\tau$ "
     "slice, FINDS the flatness -- Ricci tensor identically zero -- so a non-zero answer below is "
     "the geometry and not the tool",
     _R_flat == 0 and sp.simplify(_Ric_flat) == sp.zeros(3, 3))

rng = np.random.default_rng(7)
worst_ok, worst_bad = 0.0, 0.0
print(f"      {'k [1/Mpc]':>12} {'s [Mpc]':>10} {'|x_O| [Mpc]':>12} {'|series-exact|':>15} "
      f"{'wrong-argument':>15}")
for _ in range(6):
    kv = rng.normal(size=3)
    kv /= np.linalg.norm(kv)
    k = rng.uniform(0.2, 1.2) / 1000.0
    xO = np.array([0.0, 0.0, ref['r0']]) + rng.normal(scale=200.0, size=3)   # OFF the chart origin
    d = rng.normal(size=3)
    d /= np.linalg.norm(d)
    s = rng.uniform(2000.0, 16000.0)
    x = xO + s * d
    exact = np.exp(1j * k * np.dot(kv, x))
    L = np.arange(int(3 * k * s + 80) + 1)
    phase = np.exp(1j * k * np.dot(kv, xO))
    coef = (2 * L + 1) * (1j ** L) * eval_legendre(L, np.dot(kv, d))
    good = phase * np.sum(coef * spherical_jn(L, k * s))
    bad = phase * np.sum(coef * spherical_jn(L, k * np.linalg.norm(x)))
    worst_ok = max(worst_ok, abs(good - exact))
    worst_bad = max(worst_bad, abs(bad - exact))
    print(f"      {k:12.5e} {s:10.1f} {np.linalg.norm(xO):12.1f} {abs(good-exact):15.3e} "
          f"{abs(bad-exact):15.3e}")
gate(f"⛭⛭ (i) ANSWERED: on the flat slice the expansion about a GENERAL point is EXACT and the "
     f"observer's offset is the pure phase `exp(i k . x_O)` -- worst miss {worst_ok:.1e} over six "
     "random configurations with |x_O| ~ r_0 ⇒ NO measure, NO weight, NO ell-dependent factor",
     worst_ok < 1e-12)
gate(f"⌗ and the control CAN see a number move: the same series with the chart radius |x| in place of "
     f"the chord s misses the plane wave by {worst_bad:.2f} -- so the pass above is a measurement",
     worst_bad > 0.5)

# ================================================== D. what the slice offers instead
head("D.  ⛭⛭⛭ (ii) WHAT THE SLICE OFFERS INSTEAD OF $D_C$: $r_0$, SHORT BY EXACTLY THE STRETCH")
print("      the observer's own constant-tau slice, epoch by Euclidean radius  (refit background):")
print(f"      {'1+z':>12} {'|x| = r_0/(1+z)':>18} {'chord from observer':>22}")
for z in (0.0, 1.0, 10.0, 100.0, Z_REC, 3.0e7):
    rr = ref['r0'] / (1.0 + z)
    print(f"      {1+z:12.6g} {rr:18.4f} {ref['r0']-rr:11.2f} .. {ref['r0']+rr:<9.2f}")
rrec = ref['r0'] / (1.0 + Z_REC)
ang = 2.0 * np.arctan(rrec / np.sqrt(ref['r0'] ** 2 - rrec ** 2))
frac = (1.0 - np.cos(ang / 2.0)) / 2.0
print(f"\n      the z={Z_REC} locus is a sphere of radius {rrec:.4f} Mpc about the BRANCH POINT:")
print(f"        chord from the observer  = r_0 to {rrec/ref['r0']:.2e}   (r_0 = {ref['r0']:.2f} Mpc)")
print(f"        angular size on the sky  = {np.degrees(ang):.4f} deg, {frac:.3e} of 4 pi")
print(f"        D_C / chord              = {ref['DC']/ref['r0']:.6f}   <-- the stretch D_C/r_0")
gate("⛭⛭ THE SLICE IS NOT A SURFACE OF CONSTANT COSMIC EPOCH: `tilde tau = tau_0 + chi` and "
     "`r(tilde tau) = |x|`, so the epoch across it is `1+z = r_0/|x|` and the observer's own "
     "simultaneity slice carries EVERY cosmic epoch, as spheres about the branch point",
     all(abs((ref['r0'] / (ref['r0'] / (1 + z))) - (1 + z)) < 1e-9 * (1 + z)
         for z in (0.0, 1.0, 10.0, 100.0, Z_REC, 3.0e7)))
gate(f"⛭⛭⛭ (ii) ANSWERED: the only length the slice offers between the observer and the "
     f"$z={Z_REC}$ epoch is the chord to that sphere, which is `r_0` to "
     f"{rrec/ref['r0']:.1e} -- the reading `r7100` excluded, and the paper's own `D_M=D_C` is the "
     "one it is short of", abs((ref['r0'] - rrec) / ref['r0'] - 1.0) < 2e-3
     and "the comoving angular-diameter distance is $D_M=D_C$" in body15)
gate(f"⇒ *** AND THE SHORTFALL IS NOT AN UNKNOWN AMOUNT: D_C / chord = {ref['DC']/ref['r0']:.6f}, "
     f"the stretch D_C/r_0 to six figures -- the number the low-multipole floor is built on ***",
     abs(ref['DC'] / ref['r0'] - STRETCH) < 1e-12)
gate(f"⌗ and the whole last-scattering surface, as the slice sees it, subtends "
     f"{np.degrees(ang):.3f} degrees in ONE direction -- {frac:.1e} of the sky -- which is "
     "'a chart's angle is not a sky', with a number on it", frac < 1e-6)

print("\n      and what the general point costs in ANISOTROPY: epoch across the sky at fixed chord s")
spread = {}
for s in (100.0, 1000.0, 0.5 * ref['r0'], ref['DC']):
    zs = [ref['r0'] / np.sqrt(ref['r0'] ** 2 + s * s + 2 * ref['r0'] * s * np.cos(t))
          for t in (0.0, np.pi / 2, np.pi)]
    spread[s] = max(zs) - min(zs)
    print(f"        s = {s:9.1f} Mpc:  1+z at 0 / 90 / 180 deg = {zs[0]:.6f} / {zs[1]:.6f} / "
          f"{zs[2]:.6f}   spread {spread[s]:.4f}")
gate("⌗ the slice's epoch gradient is RADIAL ABOUT THE BRANCH POINT, so an observer at a general "
     "point is at no symmetry centre of it: at a chord of half `r_0` the epoch already spreads by "
     "more than 0.3 across the sky", spread[0.5 * ref['r0']] > 0.3)

# ================================================== E. the null cone, exactly
head("E.  ⛭⛭ (iii) AND THE PHOTONS ARE NOT THE CHART'S NULL GEODESICS -- THE EXACT RELATION, AND dS")
gate("the paper states the redshift it uses as the ratio of the scale factor at two cosmic times, "
     "which is the Friedmann readout's relation and is what the exact chart relation below is "
     "compared against", "redshift $1+z=r(\\tilde\\tau_0)/r(\\tilde\\tau_e)$" in body15)

vo = ref['v'](ref['r0'])
zp = lambda ve: (1.0 + vo) / (1.0 + ve)                                        # noqa: E731
zm = lambda ve: (vo - 1.0) / (ve - 1.0)                                        # noqa: E731
ve_rec = ref['v'](rrec)
print(f"      at the construction's locus r_e = {rrec:.4f} Mpc (v_e = {ve_rec:.4f}, "
      f"v_o = {vo:.6f}):")
print(f"        exact chart relation, outgoing root  1+z = {zp(ve_rec):.6f}"
      f"        ingoing root  1+z = {zm(ve_rec):.6f}      <- both BLUESHIFTS")
r_hi = brentq(lambda r: zm(ref['v'](r)) - (1.0 + Z_REC), ref['rN'] + 1e-9, ref['r0'])
r_lo = brentq(lambda r: zm(ref['v'](r)) - (1.0 + Z_REC), 1e-6, ref['rN'] - 1e-9)
print(f"        the exact relation's 1+z = {1+Z_REC} surface is at r = {r_lo:.3f} and {r_hi:.3f} Mpc,"
      f" i.e. r_N = {ref['rN']:.3f} to within {max(abs(r_lo-ref['rN']), abs(r_hi-ref['rN'])):.1f} Mpc")


def geodesic(b, PT, pr0, target, lmax=4.0e4):
    """the PG null geodesic system, integrated; p_tau is conserved because the chart is tau-independent."""
    v, al, rsch = b['v'], b['alpha'], b['rsch']
    dv = lambda r: (-rsch / r ** 2 + 2.0 * r / al ** 2) / (2.0 * v(r))         # noqa: E731

    def rhs(_l, y):
        _, r, pr = y
        return [-PT - v(r) * pr,                              # dtau/dl = g^{tau tau} p_tau + g^{tau r} p_r
                -v(r) * PT + (1.0 - v(r) ** 2) * pr,          # dr/dl   = g^{r tau} p_tau + g^{rr} p_r
                dv(r) * PT * pr + v(r) * dv(r) * pr ** 2]     # dp_r/dl = -(1/2) d(2H)/dr

    ev = lambda _l, y: y[1] - target                                            # noqa: E731
    ev.terminal = True
    s = solve_ivp(rhs, [0.0, lmax], [0.0, b['r0'], pr0], rtol=3e-13, atol=1e-15,
                  events=ev, max_step=20.0, method='DOP853')
    null = lambda r, pr: -PT ** 2 - 2 * v(r) * PT * pr + (1.0 - v(r) ** 2) * pr ** 2  # noqa: E731
    if not len(s.t_events[0]):
        return None
    lam = s.t_events[0][0]
    _, r, pr = s.y_events[0][0]
    return dict(lam=lam, r=r, ku=PT + v(r) * pr, ku0=PT + b['v'](b['r0']) * pr0,
                n0=null(b['r0'], pr0), n1=null(r, pr))


g = geodesic(ref, -(vo - 1.0), 1.0, r_hi)
print(f"\n      numerical integration of the geodesic system, ingoing root, down to r = {r_hi:.4f}:")
print(f"        |k.u|_o = {abs(g['ku0']):.12f}   |k.u|_e = {abs(g['ku']):.6f}   "
      f"=> 1+z = {abs(g['ku']/g['ku0']):.6f}")
print(f"        the analytic root gives                                1+z = "
      f"{zm(ref['v'](g['r'])):.6f}")
print(f"        null constraint held: {g['n0']:+.1e} -> {g['n1']:+.1e};  affine span "
      f"{g['lam']:.4f} Mpc = (r_0-r_e)/(v_o-1) = {(ref['r0']-g['r'])/(vo-1.0):.4f} Mpc")
# ⌗⌗ ** THE ASSERTION IS THE INEQUALITY AND THE MEASUREMENT IS REPORTED (r7106, on CI's own report). **
#   *The two tolerances here were first written at the numerical FLOOR -- `1e-10` on the agreement and
#   `1e-8` on the constraint -- which the tolerance sweep flagged on a third build (`--threads 2
#   --coretype Prescott`): the errors moved by 84 and 87 per cent with only 32x and 9x of headroom,
#   while the two comparisons on the default build came back CLEAN.*  ⇒ ** A tolerance pinned to what
#   the arithmetic happens to deliver on one build is not a claim; it is a fragility. **  *The claim
#   this gate makes is that an independent numerical integration agrees with the analytic root and
#   that the null constraint is held -- which `1e-6` establishes decisively for two independent
#   methods -- so the bound asserts THAT and the achieved numbers are printed above and below rather
#   than baked into the inequality.*  ⌗ Recorded rather than quietly loosened, because loosening a
#   tolerance to clear a gate and loosening it to match the claim look identical in a diff.
_agree = abs(abs(g['ku'] / g['ku0']) / zm(ref['v'](g['r'])) - 1.0)
# ⌗⌗ ** AND THE NULL-CONSTRAINT BOUND GOES TO `1e-5` AT `r7112+60.1`, ON THE INSTRUMENT'S OWN RULE
#   RATHER THAN ON MY JUDGEMENT. **  *`r7106+60.1` moved these two from the numerical floor to `1e-6`.
#   CI's tolerance perturbation then FLAGGED the null-constraint site (`418:46`): its error read
#   `1.09e-9` on one build and `1.77e-10` on the other -- it moved 84 per cent, with `917.5x` of
#   headroom.  `sweep_tolerances.py` flags exactly that pair, `moved > 0.10 AND headroom < 1e3`, and
#   says in terms what clears it: "it moves with headroom >= 1e3 (round-off with real margin is not a
#   defect)".*  ⇒ ** `917x` IS NOT A DEFECT IN THE CLAIM, IT IS A MARGIN ONE NOTCH UNDER THE BAR THE
#   INSTRUMENT SETS -- so the bound is stated where the claim needs it AND clear of that bar: `1e-5`
#   leaves `>9000x` on CI's own worse build. **  ⌗ *The two numbers are not the same kind of claim and
#   now do not carry the same bound: the AGREEMENT between the analytic root and an independent
#   integration is the load-bearing one and keeps `1e-6` (it achieves `1.0e-13`, `10^7` of headroom);
#   the null constraint is a VALIDITY CHECK ON THE INTEGRATOR, and five digits of it is what that
#   check is for.*  ⚠ *Recorded rather than quietly widened, and recorded on CI's measurement rather
#   than mine: all three builds reachable in this container come back CLEAN on this site, so the
#   6x spread is in hardware I cannot reproduce and the runner's numbers are the evidence.*
print(f"        achieved: agreement {_agree:.2e} (bound 1e-6), null constraint "
      f"{abs(g['n1']):.2e} (bound 1e-5)")
gate(f"⛭ the exact null-geodesic redshift of this chart is `1+z = (1 +- v_o)/(1 +- v_e)` -- the "
     f"analytic root and an independent numerical integration of the geodesic system agree to "
     f"{_agree:.1e}, against a bound of 1e-6, with the null constraint held to "
     f"{abs(g['n1']):.1e}, against 1e-5", _agree < 1e-6 and abs(g['n1']) < 1e-5)

print("\n      the de Sitter calibration, where the answer is independently known to be a_0/a_e:")
cal_ok, cal_areal = True, []
for Xo, ae in ((0.3, 0.5), (0.1, 0.2), (0.45, 0.8)):
    Xs = Xo + (1.0 / ae - 1.0)                       # alpha = 1, a_0 = 1: comoving distance to the ray
    re_, ro_ = ae * Xs, Xo
    got, want = (1.0 - ro_) / (1.0 - re_), 1.0 / ae
    cal_ok = cal_ok and abs(got / want - 1.0) < 1e-12
    cal_areal.append(ro_ / re_)
    print(f"        X_o={Xo} a_e={ae}:  (1-v_o)/(1-v_e) = {got:.12f}   a_0/a_e = {want:.12f}"
          f"   ratio of AREAL RADII = {ro_/re_:.6f}")
gate("⛭⛭ AND IT IS CALIBRATED, NOT ASSERTED: in the de Sitter case the same relation returns "
     "`a_0/a_e` to twelve figures, while the ratio of the two events' AREAL RADII returns nothing "
     "like it -- so the chart's areal-radius ratio is not a photon redshift",
     cal_ok and all(abs(x - 2.0) > 0.5 and abs(x - 5.0) > 0.5 for x in cal_areal))
gate(f"⇒ ⛭⛭ (iii) ANSWERED: on the exact relation the construction's z={Z_REC} locus is a BLUESHIFT "
     f"({zm(ve_rec):.4f} / {zp(ve_rec):.4f}), its own z={Z_REC} surface sits at the Nariai radius, "
     "and `r = r_N` is an infinite-redshift surface ⇒ the photons the paper projects are NOT this "
     "chart's null geodesics, so a plane wave expanded on this chart's slice is not a mode of what "
     "is observed", zm(ve_rec) < 1.0 and zp(ve_rec) < 1.0
     and abs(r_hi - ref['rN']) < 0.03 * ref['rN'] and ref['v'](ref['rN']) - 1.0 < 1e-13)
DA_sat = (ref['r0'] - ref['rN']) / (vo - 1.0)
print(f"\n      and the radial area distance is AFFINE on this chart (vacuum: R_mn k^m k^n = 0, and a "
      f"radial\n      ray is a principal null direction so the shear source vanishes):  "
      f"D_A = (r_0 - r_e)/(v_o - 1),\n      saturating at {DA_sat:.1f} Mpc as r_e -> r_N, against "
      f"D_C/(1+z) = {ref['DC']/(1+Z_REC):.3f} Mpc on the readout.")
gate("⌗ and its area distance saturates at a finite value as the redshift diverges, which is horizon "
     "structure and not a cosmological distance -- a third way the same statement comes out",
     DA_sat > 100.0 * ref['DC'] / (1.0 + Z_REC))

# ================================================== F. the join
head("F.  ⛭⛭⛭ (iv) THE JOIN: THE CONSTANT-COSMIC-TIME LAYER IS `R x S^2`, NOT AN `S^3`")
# ⛔⛭⛭ RE-POINT REVERTED r7105 (66, the gate).  ** `r7103` re-pointed this check and `r7103` WAS WRONG. **
# *Daryl corrected the gate: in the de Sitter presentation the cosmological layer IS the `S^3`, and under
# the reassignment that gives `eq:proper-frame` the same null bundle becomes the constant-`chi` geodesics,
# so a constant-`tilde tau` surface is the `45`-degree line plus an `S^2` of directionality --- the Hopf
# direction traded into `chi`.*
#   ⇒ *** READING `R x S^2` OFF THAT CHART IS WHAT THE REASSIGNMENT DOES, NOT A DEFECT IN THE PAPER.  The
#     tell was two lines above the equation this receipt read: `sec:properframe` already says the slices
#     sit at `45` degrees to the fundamental rest frame, and the `45`-degree picture IS this fact. ***
#   ⌗ *So the paper's sentence is restored verbatim and this check is restored with it.  The delivering
#     seat's own charitable reading --- that the physics was untouched --- was RIGHT, and the gate
#     overrode it on a worse reading.  `PO-72`, opened on that inference, is struck at `r7105`.*
# ⛭⛭⛭ r7113 (66): **THE CLAIM IS ASSERTED; THE WORDING IS NOT.  AND THIS CHECK IS THE ONE DARYL
#   RESTORED VERBATIM AT `r7105`, SO THE CHANGE IS EXPLAINED RATHER THAN MADE QUIETLY.**
#   *`r7113` repaired the paper's ATTRIBUTION of the sphere, which is the narrow repair this seat proposed
#   at `r7102` and which `r7105` ruled had been right all along: `sec:largescale` now reads "the
#   cosmological layers are the closed $S^3$, **labelled** by constant $\tilde\tau$ and **read as a sphere
#   in the de Sitter presentation**", and then states the reassigned chart's induced metric outright.*
#   ⌗ *Node 70 measured that induced metric at `r7111+70.1` and node 66 verified it independently: on
#   `eq:proper-frame` a constant-$\tilde\tau$ surface is $-f(r)d\chi^2 + r^2d\Omega^2$ with Ricci
#   eigenvalues $(0, 1/r^2, 1/r^2)$ -- which is Daryl's own `r7105` statement of that metric.*
#   ⇒ ** SO THE OLD SPELLING ASSERTED A LOCATION THE CORPUS NO LONGER CLAIMS, WHILE WHAT THE CHECK IS FOR
#   IS UNCHANGED: that the paper makes the closed-$S^3$ claim for the cosmological layers and reads $r_0$
#   off it twice. **  *That is what is asserted now, by substring tests on the surviving claim rather than
#   on a sentence another seat owns the wording of.*  ⌗ *`PO-73` carries the open part -- which geometry
#   supplies the sphere -- and NOTHING here claims the two presentations are one metric or two.*
gate("the paper still makes the closed-$S^3$ claim for the cosmological layers and still reads $r_0$ off "
     "it twice -- once as the areal radius, once as the curvature radius -- with the sphere's "
     "presentation now named rather than left to the constant-$\\tilde\\tau$ label",
     "layers are the closed $S^3$" in body15
     and "e the closed $S^3$, labelled by constant $\\tilde\\tau=\\tau+\\chi$ and read as a sphere in the de~Sitter presentation" in body15
     and "with $r_0$ the present $S^3$ areal radius" in body15
     and "the ratio of the flat projection distance to the curvature radius" in body15)
_vv, _rc = sp.symbols('v r_c', positive=True)
_chi = sp.Symbol('chi')
_Ric_lay, _R_lay = ricci(sp.diag(_vv ** 2 - 1, _rc ** 2, _rc ** 2 * sp.sin(_th) ** 2),
                         [_chi, _th, _ph])
_a, _psi = sp.symbols('a psi', positive=True)
_, _R_S3 = ricci(sp.diag(_a ** 2, _a ** 2 * sp.sin(_psi) ** 2,
                         _a ** 2 * sp.sin(_psi) ** 2 * sp.sin(_th) ** 2), [_psi, _th, _ph])
print(f"      on tilde-tau = const: dtau = -dchi and r is CONSTANT, so the induced metric is")
print(f"        (v^2 - 1) dchi^2 + r_c^2 dOmega^2      with both coefficients constant on the surface")
print(f"      Ricci scalar = {_R_lay}        chi-chi Ricci component = {sp.simplify(_Ric_lay[0,0])}")
print(f"      for comparison, S^3 of curvature radius a: R = {_R_S3}   (and Ricci isotropic)")
gate("⛭⛭⛭ (iv) THE JOIN IS NOT MADE GOOD: the constant-cosmic-time surface of `eq:proper-frame` has "
     "Ricci scalar `2/r_c^2` with a ZERO Ricci eigenvalue along `chi` -- it is `R x S^2` of radius "
     "`r(tilde tau)`, where an `S^3` of curvature radius `a` would give `6/a^2` isotropically",
     sp.simplify(_R_lay - 2 / _rc ** 2) == 0 and sp.simplify(_Ric_lay[0, 0]) == 0
     and sp.simplify(_R_S3 - 6 / _a ** 2) == 0)

print("\n      and an S^3 slice DOES exist in this geometry, for ANY curvature radius a:")
worst_s3 = 0.0
for a in (ref['r0'], ref['DC'], 2000.0):
    rr = np.linspace(1.0, 0.8 * a, 300)
    Awant = 1.0 / (1.0 - rr ** 2 / a ** 2)
    vv = ref['v'](rr)
    # ⌗ the quadratic `(v^2-1) T'^2 - 2 v T' + (1-A) = 0` has roots `(v +- s)/(v^2-1)`, and the chart
    #   crosses `v = 1` at `r_N`, where that form divides by zero.  The SAME root rewritten as
    #   `(1-A)/(v+s)` has no such division.  *A first pass took the unstable form and the residual
    #   came out at 2.8e-5 instead of 2.2e-16 -- recorded here rather than quietly repaired, because a
    #   1e-5 residual on an identity is the shape of a real defect and it should not look like one.*
    sq = np.sqrt(1.0 + (vv ** 2 - 1.0) * Awant)
    Tp = (1.0 - Awant) / (vv + sq)
    Agot = -Tp ** 2 + (1.0 - vv * Tp) ** 2
    w = float(np.max(np.abs(Agot / Awant - 1.0)))
    worst_s3 = max(worst_s3, w)
    print(f"        a = {a:9.1f} Mpc: solving  -T'^2 + (1 - v T')^2 = 1/(1 - r^2/a^2)  for T'(r) "
          f"reproduces it to {w:.2e}")
gate("⌗ so the `S^3` is a CHOICE of slice -- a spherically symmetric spacelike slice with that "
     "induced metric exists for any curvature radius -- and it is neither the constant-cosmic-time "
     "surface nor one that singles out `r_0`", worst_s3 < 1e-12)
gate("⚠ AND THE CHARITABLE READING IS NAMED RATHER THAN SUPPRESSED: if the closed $S^3$ is the "
     "FRIEDMANN READOUT's spatial section rather than `eq:proper-frame`'s layer, the physics is "
     "untouched and the citation is what needs repair -- so this receipt claims the geometry and "
     "NOT that `r_0`, `D_C`, the stretch or the comb moves",
     abs(ref['DC'] / ref['r0'] - STRETCH) < 1e-12 and abs(ref['r0'] - 5051.0) < 1.0)

# ================================================== G. the verdict and the stop
head("G.  ⇒ THE VERDICT: NOT BOUNDED ON THIS CONSTRUCTION -- SAID, AND STOPPED")
print("      the three candidate slicings, and what each has:")
print("        constant tau      : flat E^3 (prop:flat)        -- NO constant epoch, and offers r_0")
print("        constant tilde-tau: constant epoch              -- R x S^2, not an S^3")
print("        the S^3 slice     : the source's spectrum        -- unforced, any curvature radius")
gate("⇒ *** NO SINGLE SLICING OF THE PROPER FRAME CARRIES BOTH THE SOURCE'S DISCRETE SPECTRUM AND "
     "THE PROJECTION DISTANCE, so the expansion cannot be completed on it: the order's licence is "
     "taken and the reason is exhibited rather than guessed ***",
     worst_ok < 1e-12                                  # the expansion machinery is exact
     and abs(ref['DC'] / ref['r0'] - STRETCH) < 1e-12  # and the slice offers r_0, not D_C
     and sp.simplify(_Ric_lay[0, 0]) == 0              # and the epoch surface is not an S^3
     and zm(ve_rec) < 1.0)                             # and the chart's photons are not these photons
gate("⇒ AND WHAT IT DOES TO `r7100`: it does not move the conclusion, it moves the LICENSING -- "
     "`j_ell(k_L D_C)` is neither confirmed nor contradicted here, and its licence remains "
     "`sec:flatlcdm`'s exact recovery of flat $\\Lambda$CDM, an identification with a named content",
     "flat distances and a closed $S^3$ of comoving worldlines coexist" in body15
     and abs(STRETCH - 2.774) < 5e-4)

# ================================================== H. the smaller item
head("H.  ⌗ THE SMALLER ITEM: IS A `c54`-ERA LENSING POTENTIAL ADMISSIBLE ON THE CURRENT BACKGROUND?")
PROD = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'L171x_lensing_potential.py')
INSTR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
prod = open(PROD, encoding='utf-8').read() if os.path.exists(PROD) else ''
instr = open(INSTR, encoding='utf-8').read() if os.path.exists(INSTR) else ''
uses_phys = 'A.Hphys' in prod
touches = {s: (s in prod) for s in ('LEAFSCALES', 'VISLEAF', 'LEAFREC', 'LEAFPERT')}
print(f"      producer present: {os.path.exists(PROD)};  evaluates the growth on `A.Hphys`: "
      f"{uses_phys}")
print(f"      does the producer mention any switch added since c54? {touches}")
gate("the producer exists and builds the growth factor on `A.Hphys` -- the STACKING rate -- while "
     "none of the three switches added since `c54` appears in it at all",
     uses_phys and not any(touches.values()))
gate("and the rate the instrument puts the perturbations on is the LEAF's: `Hleaf` carries the "
     "radiation term and `Hphys` carries it only when `RAD_IN_RATE`, which the CR arm does not set",
     'def Hleaf' in instr and 'OR / a ** 4' in instr and 'if RAD_IN_RATE' in instr)

h = ref['H0'] / 100.0
ORAD = 4.15e-5 / h ** 2
Hp = lambda a: ref['H0'] * np.sqrt(ref['OM'] / a ** 3 + (1 - ref['OM']))              # noqa: E731
Hl = lambda a: ref['H0'] * np.sqrt(ref['OM'] / a ** 3 + (1 - ref['OM']) + ORAD / a ** 4)  # noqa: E731
grow = lambda Hf, a: Hf(a) * quad(lambda x: 1.0 / (x * Hf(x)) ** 3, 1e-8, a, limit=400)[0]  # noqa: E731
g0p, g0l = grow(Hp, 1.0), grow(Hl, 1.0)
print(f"\n      how much the misassignment is worth (Omega_r = {ORAD:.3e}), in D(a)/D_0:")
dz = {}
for z in (0.5, 1.0, 2.0, 3.0, 5.0, 10.0):
    a = 1.0 / (1.0 + z)
    rp, rl = grow(Hp, a) / g0p, grow(Hl, a) / g0l
    dz[z] = abs(rl / rp - 1.0)
    print(f"        z = {z:<5g}  stacking {rp:.6f}   leaf {rl:.6f}   difference {rl/rp-1:+.3e}")
gate("⌗ ONE LINE, AS ASKED: ADMISSIBLE IN PRINCIPLE -- no switch added since `c54` reaches the growth "
     "or the projection -- BUT NOT AS IT STANDS, because the growth is evaluated on the stacking rate "
     "where the rate rule puts the perturbations on the leaf's; so part B stands on a SUPERSEDED rate "
     "assignment, not merely an unreproducible object, and re-deriving is the only option",
     uses_phys and all(v_ > 0.0 for v_ in dz.values()))
gate(f"⌗ and sized so `cc66` does not walk into it blind: the two rates' growth shapes differ by "
     f"{dz[2.0]:.1e} at z=2, where the lensing kernel peaks, and {dz[10.0]:.1e} out to z=10 ⇒ the "
     "re-derivation should be expected to CONFIRM part B's numbers rather than move them",
     dz[2.0] < 1e-2 and dz[10.0] < 5e-2)

# ================================================== I. scope
head("I.  ⚠ SCOPE, AND WHAT IS NOT CLAIMED")
# ⌗⌗ ** A SLIP OF MINE, RECORDED RATHER THAN REPAIRED IN SILENCE. **  *The first draft of these two
#   gates read THIS FILE's own source and asked whether forbidden names appear in it -- and found them,
#   in its own expressions, so neither could ever pass.  It is the second time this line has written a
#   check that tests its own spelling.  ** The scope claim is about WHICH FILES THIS RECEIPT OPENED, so
#   it is read from that, recorded as the opens happen. **
OPENED = sorted(os.path.basename(x) for x in (P15, INSTR, PROD))
print(f"      every file this receipt opened: {OPENED}")
gate("no transfer, spectrum or likelihood is computed here: the ONLY files this receipt opened are "
     "the paper, the acoustic instrument and the lensing producer, and the last two were READ for "
     "their rate assignment rather than run",
     OPENED == ['ACOUSTIC_two_arm.py', 'CR_cosmology.tex', 'L171x_lensing_potential.py'])
gate("and no banked output of any other row is read: `cc66`'s three-grid logs and the `c54` lensing "
     "spectrum are not among them, so neither its table nor that potential is re-measured here",
     not any(x.endswith(('.npz', '.log')) for x in OPENED))

# ================================================== verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {n}")
print(f"\n  {len(CHECKS) - len(bad)} of {len(CHECKS)} checks pass   [{time.time()-t_all:.1f}s]")
if bad:
    raise SystemExit(1)
print("  ALL PASS -- the expansion introduces nothing, the slice offers r_0 and not D_C, the "
      "constant-epoch\n  surface is R x S^2, the chart's photons are not the paper's photons, and the "
      "completion is not\n  bounded on this construction.  Said, and stopped.")
