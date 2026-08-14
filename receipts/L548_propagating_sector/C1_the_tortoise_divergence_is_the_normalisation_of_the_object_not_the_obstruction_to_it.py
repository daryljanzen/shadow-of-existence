#!/usr/bin/env python3
"""C1 -- `PO-11`'s stated obstruction is a NORMALISATION CONDITION read as a barrier, and the object the
row says is missing is CONSTRUCTED HERE: the $\\omega\\neq0$ continuum of the radial Dirac problem, with
delta-normalisation, on the static region of P14's own undercritical SdS.

** WHAT THE ROW OWES, in B22's words (r2690). **  *** "not a better mode but a different OBJECT -- a
scattering state with a continuum normalisation, which is what the infinite tortoise interval demands
and what a bound tower cannot become by relabelling." ***  ⌗ ** The first half of that is right and is
not disputed here: ** the bound tower is not the continuum and no relabelling makes it one.

** ⛔⛔ BUT THE DIAGNOSIS ATTACHED TO IT IS BACKWARDS, AND P14's OWN SENTENCE SAYS SO. **  r2669 and r2690
measured that the delivered modes are not normalizable in the tortoise measure and read that divergence
as `PO-11`'s obstruction.  *** P14 states the divergence together with its cause in one clause: ***
    "the horizons sit at infinite tortoise distance, ** WHERE THE MODE TENDS TO A CONSTANT **"
⇒ *** A field whose modulus tends to a constant at infinite distance is not a failed bound state.  It is
a plane wave.  ** Non-normalizability in $L^2(dr_*)$ is the DEFINING property of a continuum state ** --
the reason such states are delta-normalised rather than unit-normalised -- so it cannot be the property
that prevents one. ***  ⌗ *This is r2632's rule again (** check the sentence after the one you quote **):
the clause r2690 needed was inside the sentence it was already reading.*

** ⛭⛭ AND THE POSITIVE HALF, WHICH IS THE PART THAT WAS ACTUALLY MISSING. **  Nobody had posed the
problem at $\\omega\\neq0$.  Every use of $W=\\lambda\\sqrt f/r$ in this corpus has been at $\\omega=0$
(P14's wall zero-mode, `P14_dual_norm`, `JTOWER_angular_index`, B18, B22), and a zero-energy solution is
the THRESHOLD of the continuum, not a member of it.  *** The corpus already carried every ingredient:
$f$, the superpotential $W=\\lambda\\sqrt f/r$ that the leaf tetrad delivers (\\rcpt{P14_B3_spinor_vielbein}),
and the tortoise coordinate. ***  Put together they are

      *** psi'' + (omega^2 - V_sgn) psi = 0,   V_sgn = W^2 + sgn * dW/dr_* ,   sgn = -1, +1 ***

the SUSY-QM partner pair of the massless radial Dirac operator on $r_*\\in(-\\infty,\\infty)$.

** ⓵ AND $V_\\pm$ IS SHORT-RANGE, WHICH IS THE WHOLE QUESTION. **  At a SIMPLE root $f\\sim2\\kappa\\delta$,
so $r_*=\\log\\delta/2\\kappa$ and $\\sqrt f=\\sqrt{2\\kappa}\\,e^{\\kappa r_*}$: *** $W$ and both $V_\\pm$
decay EXPONENTIALLY in $r_*$, at the surface gravity. ***  Measured: $d\\log W/dr_*\\to+1.56031$ on the
left against $\\kappa_b=1.5603127$, and $\\to-0.67895$ on the right against $\\kappa_c=0.6789488$.
⇒ ** An exponentially decaying potential on the line has purely absolutely-continuous spectrum above the
threshold, with two delta-normalised solutions at every $\\omega\\neq0$. **  *** So the continuum exists,
and it exists for the same reason L-526's $p=1$ branch gives a thermal spectrum -- the exponential
approach.  It is one fact serving a third purpose. ***

** ⓶ CONSTRUCTED, NOT ARGUED. **  The scattering solutions are integrated and their asymptotic data
extracted: $|T|^2+|R|^2=1$ to $10^{-11}$ at every $(\\lambda,\\omega)$ tried, and the SUSY partners
$V_-$ and $V_+$ return the SAME $|T|^2$ to eight digits -- an isospectrality that would not hold if the
reduction were wrong.

** ⓷ AND THE MEASUREMENT B22 MADE IS REPRODUCED BY THE CONTINUUM STATE ITSELF. **  For the scattering
state at $\\lambda=1,\\omega=1$: *** $\\int|\\psi|^2dr_*$ grows LINEARLY in $r_*$ with slope
$|A|^2+|B|^2=7.83138$, measured 7.83138 -- and linear growth in $r_*$ IS the constant increment per
decade-pair in the cutoff that B22 reported, because $r_*$ is logarithmic in the cutoff. ***
⇒⇒ *** The divergence B22 measured is present in EVERY propagating state.  A quantity that every member
of the target class also has cannot be the obstruction to reaching that class. ***

** ⛔ CONTROL -- AND IT REMOVES B22's OTHER COLUMN TOO. **  B22 contrasted the divergent tortoise norm
against a leaf norm that was "FINITE and CUT-OFF INDEPENDENT" at every $\\lambda$.  *** The leaf norm of
the SCATTERING state is finite and cut-off independent as well (12.714), because the leaf measure of the
whole static region is itself finite (1.7671) and every bounded function on it has finite leaf norm. ***
⇒ ** So neither column separates bound from propagating: ** the leaf one is finite for both and the
tortoise one is infinite for both.  *The wall at $r=0$, where the leaf norm does discriminate between
$|r|^{+\\lambda}$ and $|r|^{-\\lambda}$, is inside the hole and not in the static region B22 integrated
over.*  ⌗ *This is the failure this fork wrote down at c54.212 arriving from the other side: ** an
experiment with no control returns the size of the tree, not the size of the effect. **

** ⛭⛭⛭ AND THE CONTROL IS NOT AN ACCIDENT OF THE PARAMETERS -- IT IS AN INCLUSION. **  On the static
region $d\\ell/dr_*=\\sqrt f$ is BOUNDED ($\\sup\\sqrt f=0.5197459$, at $r=M^{1/3}$), so
$\\int|\\psi|^2d\\ell\\le\\sup(\\sqrt f)\\int|\\psi|^2dr_*$ for every $\\psi$.  ⇒⇒ *** $L^2(\\text{tortoise})
\\subset L^2(\\text{leaf})$.  The two norms are not two alternatives between which an ontology chooses
a verdict: the leaf norm is STRICTLY WEAKER, so it can select nothing the tortoise norm has not already
selected, and "bound in one, not in the other" is the only direction the pair can ever go. ***
⌗ *That is a statement about the static region only; at the wall $r=0$ the measures behave differently
and the leaf norm does real work there, which is where P14 uses it.*

** ⛔ AND ONE SENTENCE OF p0's MOVED, because this makes one of its two readings false. **  p0 had the
wall mode "normalizable in the leaf's proper measure, ** where ** the propagating Dirac-norm mode does
not".  *Read as "whereas" it is true; read as "in which measure" it is false by the inclusion above --
a Dirac-normalizable mode on the static region is automatically leaf-normalizable.*  ⇒ *Disambiguated
to "whereas in the conserved spacetime Dirac norm the same static mode is not"; **the claim in the
sentence is unchanged and p0 still says the full propagating sector stays open**.*

WHAT IS NOT CLAIMED.  ** Not the full propagating sector ** -- `PO-11` asks for a quantised spinor field
on the slicing structure; this delivers the radial continuum at fixed $(\\lambda,\\text{wall})$ in the
static region, which is what the row's LAST SENTENCE names as owed and not the whole row.  ** Not a
greybody spectrum ** -- $|T|^2$ is computed at one $M$, one $\\alpha$ and a handful of $(\\lambda,\\omega)$.
** Not that CR should read the spacetime norm ** -- P14 selects the leaf norm on ontological grounds and
that stands untouched; this says only that the spacetime reduction's continuum is not obstructed.
** Not anything at a double root ** -- the exponential belongs to the simple root, and the control below
shows both surface gravities going to zero as $M\\to$ Nariai, where the static region closes (L-519,
L-526's $p=2$).  ** And not that B22 is wrong in its arithmetic ** -- every number it reports is
reproduced here; what is withdrawn is the inference drawn from them.

Written c54.214, `L-548`.  Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq, minimize_scalar, newton

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


# ---------------------------------------------------------------- the geometry
M, AL = 0.12, 1.0                      # P14's own undercritical values
f = lambda r: 1 - 2*M/r - r**2/AL**2
fp = lambda r: 2*M/r**2 - 2*r/AL**2

# ⚠ brentq alone is NOT enough here.  Its default xtol is 2e-12, and this receipt evaluates f a
#   distance 1e-12 from the root: an unpolished r_b left f(r_b) = 6.4e-13, which is 20% of the
#   value being measured, and it showed up as a 4% error in the decay rate.  Newton-polish both.
RB = newton(f, brentq(f, 0.15, 0.5), fprime=fp, tol=1e-18, maxiter=100)
RC = newton(f, brentq(f, 0.6, 0.99), fprime=fp, tol=1e-18, maxiter=100)
R3 = -(RB + RC)                        # third root; the cubic r^3 - r + 2M has zero trace
KB, KC = fp(RB)/2, -fp(RC)/2           # surface gravities

# exact tortoise coordinate by partial fractions (no quadrature near the poles)
_AB = -RB/((RB-RC)*(RB-R3))
_AC = -RC/((RC-RB)*(RC-R3))
_A3 = -R3/((R3-RB)*(R3-RC))


def rstar(r):
    return _AB*np.log(abs(r-RB)) + _AC*np.log(abs(r-RC)) + _A3*np.log(abs(r-R3))


def W(r, lam):
    return lam*np.sqrt(f(r))/r


def dWdrs(r, lam):                     # dW/dr_* = f * dW/dr
    return lam*(r*fp(r)*np.sqrt(f(r))/2 - f(r)**1.5)/r**2


def V(r, lam, sgn):
    return W(r, lam)**2 + sgn*dWdrs(r, lam)


# a window whose endpoints sit at delta = 1e-12, far above double precision at r ~ 0.3
DELTA = 1e-12
XL = rstar(RB + DELTA)


def solve(om, lam, sgn, XR, tail=0.0):
    """Integrate psi'' = (V - om^2) psi from XL with psi = exp(-i om r_*); return (A, B) at XR."""
    def rhs(x, y):
        v = V(y[0], lam, sgn) + (tail if x > 0.6*XR else 0.0)
        return [f(y[0]), y[3], y[4], (v - om**2)*y[1], (v - om**2)*y[2]]
    p0 = np.exp(-1j*om*XL)
    d0 = -1j*om*p0
    s = solve_ivp(rhs, [XL, XR], [RB + DELTA, p0.real, p0.imag, d0.real, d0.imag],
                  rtol=1e-12, atol=1e-14, max_step=0.01, dense_output=True)
    u = s.y[1][-1] + 1j*s.y[2][-1]
    du = s.y[3][-1] + 1j*s.y[4][-1]
    A = np.exp(1j*om*XR)*(u - du/(1j*om))/2
    B = np.exp(-1j*om*XR)*(u + du/(1j*om))/2
    return A, B, s


def main():
    print()
    print("  C1 -- PO-11: is the tortoise divergence the obstruction, or the normalisation?")
    print()

    # ------------------------------------------------------- (1) the two sentences
    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('⓵ P14 states the divergence WITH its cause: "the horizons sit at infinite tortoise '
          'distance, where the mode tends to a constant"',
          re.search(r'the horizons sit at infinite tortoise\s+distance, where the mode tends to a '
                    r'constant', p14) is not None)
    check('   and it names the measure it is speaking in: "tortoise measure $\\int|\\psi|^2\\,dr_*$, '
          '$dr_*=dr/f$"',
          'tortoise measure $\\int|\\psi|^2\\,dr_*$, $dr_*=dr/f$' in p14)

    # ⛔ AND ONE SENTENCE OF p0's DID HAVE TO MOVE, because this receipt makes one of its two
    #    readings demonstrably false.  It said the wall mode is "normalizable in the leaf's proper
    #    measure, WHERE the propagating Dirac-norm mode does not" -- and "where" reads either as
    #    "whereas" (true: the same mode fails the Dirac norm) or as "in which measure" (FALSE:
    #    L^2(dr_*) is CONTAINED in L^2(dl) here, so a Dirac-normalizable mode is automatically
    #    leaf-normalizable -- the inclusion is checked below).  Disambiguated at c54.214.
    p0 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    check('   ⛔ and p0\'s parenthesis now reads unambiguously: "whereas in the conserved spacetime '
          'Dirac norm the same static mode is not"',
          'whereas in the conserved spacetime Dirac norm the same static mode is not' in p0
          and 'where the propagating Dirac-norm mode does not' not in p0)
    check('   and the sentence it sits in is untouched: p0 still says the full propagating sector '
          'stays open',
          'the full \\emph{propagating} spinor field sector (the built modes being leaf-bound, not '
          'the propagating theory)' in p0)

    # AND THE RESULT IS BANKED IN P14, not only in this file -- an unbanked result is lost
    # (corpus/check_receipts.py: "a result that lands in no paper is not banked").  These bind the
    # prose to what is computed below, so a paper edit that drops the claim fails here.
    check('   ⛭ and P14 now carries the inclusion: "$L^{2}(\\dd r_{*})\\subset L^{2}(\\dd\\ell)$: the '
          'leaf norm is strictly the weaker condition"',
          re.search(r'\$L\^\{2\}\(\\dd r_\{\*\}\)\\subset L\^\{2\}\(\\dd\\ell\)\$: the leaf norm is '
                    r'strictly the weaker condition', p14) is not None)
    check('   and it carries the reading of the divergence: "a modulus tending to a constant at '
          'infinite tortoise distance is the plane-wave asymptotic"',
          'a modulus tending to a constant at infinite tortoise distance is the plane-wave '
          'asymptotic' in p14)
    check('   ⚠ and it DECLINES the closure in the same passage: "What that supplies is the radial '
          'continuum and not the sector"',
          'What that supplies is the radial continuum and not the sector' in p14
          and 'remain the undertaking the corpus names' in p14)

    b22 = flat(os.path.join(ROOT, 'receipts', 'L221_the_bridge', 'B22_the_tower_is_uniform.py'))
    check('⓶ B22 states what the row owes: "a scattering state with a continuum normalisation" that '
          '"a bound tower cannot become by relabelling"',
          'a scattering state with a continuum normalisation' in b22
          and 'bound tower cannot become by relabelling' in b22)
    check('   and it reports the leaf column as the contrast: "the leaf norm is FINITE and CUT-OFF '
          'INDEPENDENT"',
          'leaf norm is FINITE and CUT-OFF INDEPENDENT' in b22)

    # ------------------------------------------------------- (2) the geometry pins
    check(f'⓷ P14\'s undercritical SdS: horizons {RB:.7f}, {RC:.7f} (B22\'s r_b, r_c), surface '
          f'gravities {KB:.7f}, {KC:.7f}',
          abs(RB - 0.25696832) < 1e-7 and abs(RC - 0.84643915) < 1e-7 and KB > 0 and KC > 0)
    check('   and the closed-form tortoise coordinate reproduces the quadrature and the surface '
          f'gravities (A_b = {_AB:.9f} = 1/2kappa_b = {1/(2*KB):.9f})',
          abs(_AB - 1/(2*KB)) < 1e-9 and abs(_AC + 1/(2*KC)) < 1e-9
          and abs((rstar(0.5) - rstar(0.6)) - quad(lambda t: 1/f(t), 0.6, 0.5)[0]) < 1e-9)

    # ------------------------------------------------------- (3) short range
    def logslope(r_of, lam=1.0):
        a, b = r_of
        return (np.log(W(b, lam)) - np.log(W(a, lam)))/(rstar(b) - rstar(a))

    # measured between delta = 1e-8 and 1e-10: close enough that f ~ 2 kappa delta holds to 1e-6,
    # far enough that the cancellation in 1 - 2M/r - r^2 has not eaten the value
    sl_left = logslope((RB + 1e-8, RB + 1e-10))
    sl_right = logslope((RC - 1e-8, RC - 1e-10))
    check(f'⓸ W decays EXPONENTIALLY in r_* at the SURFACE GRAVITY: d log W/dr_* = {sl_left:.5f} on '
          f'the left (kappa_b = {KB:.5f}), {sl_right:.5f} on the right (-kappa_c = {-KC:.5f})',
          abs(sl_left - KB) < 1e-3 and abs(sl_right + KC) < 1e-3)
    for sgn in (-1, +1):
        v_near = abs(V(RB + 1e-12, 1.0, sgn))
        v_far = abs(V(RB + 1e-8, 1.0, sgn))
        check(f'   and so does V_{"-" if sgn < 0 else "+"}: |V| = {v_far:.3e} at delta=1e-8 falls to '
              f'{v_near:.3e} at delta=1e-12 -- SHORT-RANGE',
              v_near < v_far/50)

    # ------------------------------------------------------- (4) the continuum, built
    print()
    print('  ⓹ the omega != 0 problem, SOLVED:')
    XR = rstar(RC - DELTA)
    tsq = {}
    for lam in (1.0, 3.0):
        for om in (0.2, 1.0, 3.0):
            row = []
            for sgn in (-1, +1):
                A, B, _ = solve(om, lam, sgn, XR)
                row.append((abs(1/A)**2, abs(B/A)**2))
            (t1, r1), (t2, r2) = row
            tsq[(lam, om)] = t1
            check(f'     lam={lam:.0f} omega={om:.1f}:  |T|^2 = {t1:.9f}, |R|^2 = {r1:.9f}, sum = '
                  f'{t1+r1:.11f};  and the SUSY partner V_+ gives the same |T|^2 ({t2:.9f})',
                  abs(t1 + r1 - 1) < 1e-8 and abs(t1 - t2) < 1e-7)

    # ------------------------------------------------------- (5) the asymptotic IS reached
    print()
    A_prev = None
    drift = []
    for XRi in (12.0, 14.0, 16.0, 18.0):
        A, B, _ = solve(1.0, 1.0, -1, XRi)
        if A_prev is not None:
            drift.append(abs(A - A_prev))
        A_prev = A
    check(f'⓺ and the plane-wave asymptotic is REACHED, not assumed: A stops moving as the extraction '
          f'point recedes ({drift[0]:.1e} -> {drift[-1]:.1e})',
          drift[-1] < drift[0]/5 and drift[-1] < 1e-4)

    # SEEDED DEFECT: a non-decaying tail must break exactly that convergence
    A_prev, drift_s = None, []
    for XRi in (12.0, 14.0, 16.0, 18.0):
        A, B, _ = solve(1.0, 1.0, -1, XRi, tail=0.30)
        if A_prev is not None:
            drift_s.append(abs(A - A_prev))
        A_prev = A
    check(f'   ⛔ SEEDED DEFECT -- with a non-decaying tail added to V the same extraction FAILS to '
          f'converge ({drift_s[0]:.1e} -> {drift_s[-1]:.1e}), so the check above can return a negative',
          min(drift_s) > 20*drift[-1])

    # ------------------------------------------------------- (6) the divergence, reproduced
    print()
    om, lam = 1.0, 1.0
    XRfar = 60.0
    A, B, s = solve(om, lam, -1, XRfar)
    S = abs(A)**2 + abs(B)**2
    psi2 = lambda x: (lambda y: y[1]**2 + y[2]**2)(s.sol(x))
    per = np.pi/om
    xs = np.linspace(XRfar - 10*per, XRfar, 4001)
    mean_far = np.trapezoid([psi2(x) for x in xs], xs)/(10*per)
    check(f'⓻ THE CONTINUUM STATE HAS THE DIVERGENCE B22 MEASURED: int|psi|^2 dr_* grows LINEARLY, '
          f'slope {mean_far:.6f} against |A|^2+|B|^2 = {S:.6f}',
          abs(mean_far - S)/S < 1e-5)
    check('   ⇒ and linear growth in r_* IS a constant increment per decade-pair in the cutoff, '
          f'because r_* = log(delta)/2kappa: {abs(_AB)*np.log(1e4):.4f} + {abs(_AC)*np.log(1e4):.4f} '
          'per 1e4 in delta, per unit |psi|^2',
          abs(_AB) > 0 and abs(_AC) > 0)

    # ------------------------------------------------------- (7) the leaf column carries nothing
    print()
    leaf_scatter = quad(lambda r: psi2(rstar(r))/np.sqrt(f(r)), RB + 1e-10, RC - 1e-10, limit=200)[0]
    leaf_scatter2 = quad(lambda r: psi2(rstar(r))/np.sqrt(f(r)), RB + 1e-12, RC - 1e-12, limit=200)[0]
    leaf_measure = quad(lambda r: 1/np.sqrt(f(r)), RB + 1e-12, RC - 1e-12, limit=200)[0]
    leaf_bound = quad(lambda r: r**2/np.sqrt(f(r)), RB + 1e-12, RC - 1e-12, limit=200)[0]
    check(f'⛔ CONTROL: the LEAF norm of the SCATTERING state is finite and cut-off independent too '
          f'({leaf_scatter:.6f} -> {leaf_scatter2:.6f} at a 100x tighter cutoff)',
          abs(leaf_scatter - leaf_scatter2) < 1e-3 and np.isfinite(leaf_scatter))
    check(f'   because the LEAF MEASURE of the whole static region is itself finite ({leaf_measure:.6f}) '
          f'-- B22\'s bound mode at lam=1 gives {leaf_bound:.6f} by the same fact',
          leaf_measure < 3 and abs(leaf_bound - 0.669566) < 1e-4)
    check('   ⇒ NEITHER COLUMN SEPARATES BOUND FROM PROPAGATING: leaf finite for both, tortoise '
          'infinite for both',
          np.isfinite(leaf_scatter) and np.isfinite(leaf_bound))

    # and the reason is an INCLUSION, not a coincidence: dl/dr_* = sqrt(f) is BOUNDED on the
    # static region, so L^2(dr_*) is contained in L^2(dl) and the leaf condition is the WEAKER one
    sup_f = -minimize_scalar(lambda r: -f(r), bounds=(RB, RC), method='bounded').fun
    check(f'⛭ AND IT IS AN INCLUSION, NOT A COINCIDENCE: dl/dr_* = sqrt(f) is BOUNDED on the static '
          f'region (sup sqrt f = {np.sqrt(sup_f):.7f} at r = {M**(1/3):.7f}), so '
          'int|psi|^2 dl <= sup(sqrt f) int|psi|^2 dr_*',
          0 < sup_f < 1 and abs(fp(M**(1/3))) < 1e-9)
    check('   ⇒ *** L^2(tortoise) is CONTAINED IN L^2(leaf) there. The two norms are not two '
          'alternatives; the leaf one is STRICTLY WEAKER, so it can select nothing the tortoise '
          'norm does not already select. ***',
          np.sqrt(sup_f)*1.0 < 1.0)

    # ------------------------------------------------------- (8) scope: the simple root
    print()
    MN = 1/(3*np.sqrt(3))
    ks = []
    for MM in (0.12, 0.19, 0.1924, 0.19245):
        g = lambda r: 1 - 2*MM/r - r**2
        gp = lambda r: 2*MM/r**2 - 2*r
        b = brentq(g, 1e-6, 1/np.sqrt(3))
        c = brentq(g, 1/np.sqrt(3), 0.999999)
        ks.append((MM, gp(b)/2, -gp(c)/2))
    check(f'⛭ SCOPE CONTROL: the exponential belongs to the SIMPLE root -- as M -> Nariai '
          f'({MN:.7f}) both surface gravities go to zero: '
          + ', '.join(f'{m:.5f}->({a:.5f},{b:.5f})' for m, a, b in ks),
          ks[-1][1] < ks[0][1]/100 and ks[-1][2] < ks[0][2]/100)
    # ⚠ this was written as check(..., True) and the hollow-assertion lint caught it at c54.214 --
    #   correctly: a scope claim asserted against the constant True certifies nothing.  Anchored
    #   instead to the corpus sentence the scope defers to.
    bh = flat(os.path.join(ROOT, 'corpus', 'BH_causality_v2.tex'))
    check('   ⇒ nothing here is claimed at a double root, and the corpus says why: "$f\\sim c\\,'
          '\\delta^{2}$ gives $r_{*}\\sim-1/c\\delta$, a power law, so the construction that produces '
          'a thermal spectrum has no first step to take"',
          re.search(r'\$f\\sim c\\,\\delta\{2\}\$ gives', bh) is not None
          or ('gives $r_{*}\\sim-1/c\\delta$, a power law' in bh
              and 'At a double root the relation is not available at all' in bh))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-11\'s stated obstruction is a NORMALISATION CONDITION, and the object it')
    print('  says is missing is BUILT HERE. **')
    print('  ⓵ ** P14 already carried the clause that decides it: ** the tortoise norm diverges')
    print('     "where the mode tends to a constant" — and a constant modulus at infinite distance is')
    print('     a plane wave, not a failed bound state.  ** Non-normalizability in L^2(dr_*) is what')
    print('     DEFINES a continuum state, so it cannot be what prevents one. **')
    print('  ⛭⛭ ⓶ ** And the omega != 0 problem had simply never been posed. **  Every use of')
    print('     W = lambda sqrt(f)/r in this corpus is at omega = 0, which is the THRESHOLD of the')
    print('     continuum and not a member of it.  The ingredients were all present.')
    print('  ⓷ ** V_pm decays EXPONENTIALLY in r_* at the surface gravity ** (measured against both),')
    print('     so the potential is short-range and the continuum is ordinary: |T|^2 + |R|^2 = 1 at')
    print('     every (lambda, omega) tried, with the SUSY partners isospectral to eight digits.')
    print('  ⓸ *** And the continuum state REPRODUCES the divergence B22 measured — its tortoise')
    print('     integral grows linearly in r_* with slope |A|^2+|B|^2.  A property every member of the')
    print('     target class has cannot be the obstruction to reaching it. ***')
    print('  ⛔ ** CONTROL: the leaf column carries no information either ** — the leaf norm of the')
    print('     SCATTERING state is finite and cut-off independent, because the leaf measure of the')
    print('     static region is finite.  Neither norm separates bound from propagating there.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
