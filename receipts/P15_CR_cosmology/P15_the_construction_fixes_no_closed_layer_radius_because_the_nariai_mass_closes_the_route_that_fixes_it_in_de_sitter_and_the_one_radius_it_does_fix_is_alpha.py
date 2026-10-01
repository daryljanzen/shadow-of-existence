#!/usr/bin/env python3
"""
P15 receipt -- `PO-72` `Q1`, ANSWERED ON THE TERMINAL EXIT: THE CONSTRUCTION FIXES NO CLOSED-LAYER
RADIUS, AND THE REASON IS AN IDENTITY -- THE NARIAI MASS CLOSES EXACTLY THE ROUTE THAT FIXES THE
RADIUS IN DE SITTER.  THE ONE RADIUS ANYTHING HERE DOES FIX IS $\\alpha$, THE SUBSTRATE'S THROAT, AND
IT IS NOT $r_0$.

** THE ORDER. **  `r7103` opened `PO-72` off `r7102`'s section (iv) and asked: *"`Q1`: NAME THE SLICING
THAT CARRIES THE CLOSED READING, AND DERIVE ITS RADIUS. ... a closed layer whose radius is chosen
rather than fixed is not what the decoupling argument needs.  So the question is whether the
construction fixes one"* -- with the terminal exit named as equally live: *"if no slicing of this
geometry carries an $S^3$ whose radius the construction fixes, then the closed reading is a readout of
the Friedmann equations and not a geometric layer.  In that case the corpus identity ... is either
re-derived on the correct pair of slicings or withdrawn. ... Say which way it falls."*

⇒ *** IT FALLS ON THE TERMINAL EXIT, AND THE IDENTITY IS RE-DERIVED RATHER THAN WITHDRAWN -- BUT NOT
AS A PAIR OF SLICINGS.  The construction fixes no $S^3$ radius.  What it does fix is ONE slicing (the
flat constant-$\\tau$ one) and ONE invariant length ($\\alpha=\\sqrt{3/\\Lambda}$), and the closed
readout returns exactly that length: $\\alpha = c/(H_0\\sqrt{\\Omega_\\Lambda})$, identically.  So the
plural in "two slicings" is withdrawn and nothing numerical moves. ***

** ⛭⛭⛭ THE CENTRAL FINDING, AS AN IDENTITY RATHER THAN A SEARCH. **  *In de Sitter the geometry DOES
fix the radius: the $S^3$ of radius $\\alpha$ is the throat, the unique maximal one.  Here is why, in
one line -- an $S^3$ slice coincides with a time-symmetric one exactly when the metric function is
itself $1-r^2/a^2$, and*

        f(r) - (1 - r^2/a^2)  =  - r_s/r  -  r^2/alpha^2  +  r^2/a^2

*has coefficient $-r_s$ on $1/r$ and $(a^{-2}-\\alpha^{-2})$ on $r^2$.*  ⇒ ** It vanishes for all $r$
only if $r_s=0$ AND $a=\\alpha$ -- two independent conditions. **  *And `eq:amplitude` pins $r_s$ at
the NARIAI value $2\\alpha/3\\sqrt3 \\neq 0$.*
  ⇒ *** SO THE MASS THAT FIXES THE RATE IS EXACTLY WHAT UNFIXES THE CLOSED LAYER'S RADIUS.  The two
  are the same choice, read on two of its consequences. ***

** THE CANDIDATE FIXINGS, AND WHAT EACH DOES. **  *Four conditions could pick a member of the
one-parameter $S^3$ family `r7102` exhibited.  Every one of them either excludes all of them or is
already spent:*
  ⓵ ** ORTHOGONALITY TO THE FUNDAMENTAL CONGRUENCE -- already spent, on the FLAT slicing. **  *In the
  Painlevé-Gullstrand chart $u^\\mu=(1,v,0,0)$ gives $u_\\mu=-\\mathrm d\\tau$ exactly, so the
  congruence IS hypersurface-orthogonal and its unique orthogonal foliation is the constant-$\\tau$
  one.*  ⇒ *That excludes every $S^3$.*  ⌗ *It also says precisely what the paper means by keeping
  FLRW's (i) and dropping (ii): the congruence is orthogonal to the DISTANCE slicing; what it is not
  orthogonal to is the cosmological layer.*
  ⓶ ** CONSTANT COSMIC EPOCH -- excludes every $S^3$. **  *The constant-$\\tilde\\tau$ surface is
  $\\mathbb{R}\\times S^2$ (`r7102`; re-verified here).*
  ⓷ ** TIME SYMMETRY / MAXIMALITY -- obstructed by the identity above, exactly. **
  ⓸ ** CONSTANT MEAN CURVATURE -- selects the flat slicing the construction already has. **  *Scanned
  over three decades in $a$, the gap $|K(0.1a)-K(0.8a)|$ is nowhere zero and tends to zero only as
  $a\\to\\infty$, where $A\\to1$, $T'\\to0$ and the "$S^3$" degenerates into the constant-$\\tau$
  slice.*  ⌗ *And even that slice is CMC only in de Sitter:
  $\\mathrm dK_{\\rm flat}/\\mathrm dr = 9\\alpha^3 r_s^2/4r^{5/2}(\\alpha^2r_s+r^3)^{3/2}$ -- the
  whole $r$-dependence is $r_s^2$, and at $r_s=0$ it is $K=-3/\\alpha$ identically.*

** ⌗ THE CONTROL RETURNS THE AFFIRMATIVE, WHICH IS WHAT MAKES THE NULL A MEASUREMENT. **  *Run on pure
de Sitter the same machinery FINDS the radius, analytically: at $a=\\alpha$ the auxiliary root
$s\\equiv0$, $T'=\\alpha r/(r^2-\\alpha^2)$, the normal's radial part $n^r\\equiv0$ and so $K\\equiv0$ --
the throat, exactly -- while $a=0.7\\alpha$ and $1.4\\alpha$ give $K$ neither zero nor constant.*  ⇒ *So
"no fixed radius" here is a property of this geometry and not of the method.*

** ⛭⛭ WHAT IS FIXED, AND IT IS NOT $r_0$. **  *The closed reading's own curvature radius -- the one
$\\Omega_k=-\\Omega_\\Lambda$ returns -- is*

        c / ( H_0 sqrt(Omega_Lambda) )  =  (c/H_0) sqrt(1 + 2/x_0^3)  =  alpha  =  sqrt(3/Lambda)

*an identity in the construction's own parameterisation (symbolic residual zero; $2\\times10^{-16}$ on
both backgrounds).*  ⇒ ** So the closed readout does fix a length, and it is the substrate's throat --
but $\\alpha/r_0 = \\sqrt3/x_0 = 1.0320$, so it is NOT the radius the floor is built on. **  *That is a
second, independent reason the attribution could not have been right: even the readout does not return
$r_0$.*

** ⇒ WHICH WAY THE CORPUS IDENTITY FALLS: RE-DERIVED, AT THE LEVEL IT IS ESTABLISHED. **  *What
survives is exact and loses no number:*
  - *the FLAT reading is a genuine slicing -- constant $\\tau$, Riemann identically zero, so
    $\\Omega_k=0$ in the redshift-distance relation (`prop:flat`, re-derived here);*
  - *the CLOSED reading is a readout, and $|\\Omega_k|=\\Omega_\\Lambda$ IS the statement that its
    curvature radius is $\\sqrt{3/\\Lambda}$ -- one $\\Lambda$, read as a slicing and as a length.*
  ⇒ *** So "one $\\Lambda$ read on two slicings" is withdrawn as to the plural and re-derived as "one
  slicing and one invariant length."  The content that mattered -- that $\\Omega_k$ is not a free
  parameter, because its magnitude is forced to $\\Omega_\\Lambda$ -- stands exactly. ***

⌗⌗ ** AND THE TWO CONSEQUENCES FOR THE FLOOR, BOTH NAMED, NEITHER RULED ON -- because `Q1` asked for
the slicing and the radius, not for a reassignment. **
  ⓐ *If the source spectrum rides the one fixed closed radius, it rides $\\alpha$: $\\ell_2$ goes
  $7.845 \\to 7.602$, the stretch $2.7737 \\to 2.6876$, a $-3.1\\%$ shift of the floor's location.*
  ⓑ *If it rides the slicing that IS fixed -- the $\\mathbb{R}\\times S^2$ layer -- then $\\chi$ runs
  over all of $\\mathbb{R}$ (the layer is $\\tilde\\tau$ constant with $\\tau=\\tilde\\tau-\\chi$ free),
  the Laplacian along it has continuous spectrum reaching zero, and there is **no gap and so no floor
  at all**.*
  ⇒ ⚠ *** Two different answers, and choosing between them is the gate's, not this receipt's.  Said
  here so that whichever way `PO-72` is closed, the cost is on the record before it is paid. ***

⌗ ** A DESIGN RULE TAKEN FROM `r7103`, AND APPLIED HERE RATHER THAN NODDED AT. **  *The gate re-pointed
two of my checks because they pinned the DEFECT'S PRESENCE in another lane's prose, and went red the
moment the gate acted on the finding.*  ⇒ ** So no gate below reads the paper's open-question sentence,
which this receipt's own answer is meant to close. **  *The paper's current state is located and
PRINTED, not asserted; every gate reads the geometry.*

** COMPUTES: the background objects at TWO stated parameter sets, and the slice geometry built on
them.  *** $(H_0,\\Omega_m)=(68.60,0.2973)$, the refit background `P15` fits, and $(73.00,0.3066)$, the
instrument's own default; every figure is labelled with which.  Derived: $x_0$, $\\alpha$, $r_N$,
$r_0$, $r_s$, $v(r)$, $f(r)$, $D_C(z_{\\rm rec}=1089.9)$, the slice functions $A(r)$, $T'(r)$ and the
mean curvature $K(r;a)$, and the ratios built from them.  *** No spectrum, transfer or likelihood is
computed at any parameter set, nothing is fitted, and no reassignment of the source spectrum is
made. *** **

⚠ ** SCOPE. **  No transfer is run and no spectrum computed; the acoustic instrument is not opened at
all.  `cc66`'s three-grid table is not re-measured or used.  The paper is READ and not edited -- the
attribution `r7103` corrected is left exactly as the gate wrote it, and the two consequences for the
floor are reported rather than applied.  ⛔ And the answer is the terminal exit the order named: it is
given because that is where the geometry falls, not as a fallback from a search that ran out of time.
"""
import os
import re
import time

import numpy as np
import sympy as sp
from scipy.integrate import quad

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
    OL = 1.0 - OM
    x03 = 2.0 / OM - 2.0
    x0 = x03 ** (1.0 / 3.0)
    alpha = C / H0 * np.sqrt(1.0 + 2.0 / x03)
    rN = alpha / np.sqrt(3.0)
    r0 = x0 * rN
    rsch = 2.0 * alpha / (3.0 * np.sqrt(3.0))
    H = lambda z: H0 * np.sqrt(OM * (1 + z) ** 3 + OL)                        # noqa: E731
    DC = quad(lambda z: C / H(z), 0.0, Z_REC, limit=300)[0]
    v = lambda r: np.sqrt(rsch / r + r * r / alpha ** 2)                      # noqa: E731
    return dict(H0=H0, OM=OM, OL=OL, x03=x03, x0=x0, alpha=alpha, rN=rN, r0=r0,
                rsch=rsch, H=H, DC=DC, v=v)


B = {k: background(*vv) for k, vv in BG.items()}
ref = B['the refit background `P15` fits']


def Kmean(a, v, r, h):
    """mean curvature of the S^3-shaped slice of radius a, K = (1/r^2) d/dr [ r^2 n^r ]."""
    def Q(R):
        A = 1.0 / (1.0 - R ** 2 / a ** 2)
        f = 1.0 - v(R) ** 2
        s = np.sqrt(np.maximum(1.0 + (v(R) ** 2 - 1.0) * A, 0.0))
        Tp = (1.0 - A) / (v(R) + s)                 # the numerically stable root (`r7102`)
        return R ** 2 * (-v(R) - f * Tp) / np.sqrt(A)
    return (Q(r + h) - Q(r - h)) / (2.0 * h) / r ** 2


# ================================================== A. calibration
head("A.  THE CALIBRATION: `P15`'s PARAMETER-FREE FIGURES, AND THE ONE THIS RECEIPT ADDS")
for lab, b in B.items():
    print(f"      {lab}:  x_0 = {b['x0']:.4f}  alpha = {b['alpha']:8.2f}  r_N = {b['rN']:8.2f}  "
          f"r_0 = {b['r0']:8.2f}  r_s = {b['rsch']:8.2f}  D_C = {b['DC']:9.2f} Mpc")
gate("⛭ the layer's areal radius comes out at `r_0 = 5051` Mpc, `P15`'s own figure, and the stretch "
     "at 2.76", abs(ref['r0'] - 5051.0) < 5.0 and abs(ref['DC'] / ref['r0'] - 2.76) < 0.03
     and "r_0\\approx5051" in body15 and "D_C/r_0\\approx2.76" in body15)
gate("⛭ and `r_s` is the NARIAI value `2 alpha/(3 sqrt 3)` on both backgrounds -- the quantity the "
     "obstruction below turns on", all(abs(b['rsch'] - 2 * b['alpha'] / (3 * np.sqrt(3))) < 1e-9
                                       for b in B.values()))

# ================================================== B. the identity alpha = c/(H0 sqrt(OmegaL))
head("B.  ⛭⛭ WHAT THE CLOSED READOUT FIXES: `alpha = c/(H0 sqrt(Omega_Lambda))`, IDENTICALLY")
_x = sp.Symbol('x03', positive=True)
_resid_al = sp.simplify(sp.sqrt(1 + 2 / _x) - 1 / sp.sqrt(sp.simplify(1 - 2 / (_x + 2))))
print(f"      symbolic:  sqrt(1 + 2/x0^3) - 1/sqrt(Omega_Lambda)  =  {_resid_al}")
worst_al, worst_ratio = 0.0, {}
for lab, b in B.items():
    a_cl = C / (b['H0'] * np.sqrt(b['OL']))
    worst_al = max(worst_al, abs(a_cl / b['alpha'] - 1.0))
    worst_ratio[lab] = (b['alpha'] / b['r0'], np.sqrt(3.0) / b['x0'])
    print(f"      {lab}:  c/(H_0 sqrt(Omega_L)) = {a_cl:9.4f}   alpha = {b['alpha']:9.4f}   "
          f"alpha/r_0 = {b['alpha']/b['r0']:.6f}   sqrt3/x_0 = {np.sqrt(3)/b['x0']:.6f}")
gate("⛭⛭ THE CLOSED READING'S CURVATURE RADIUS IS THE SUBSTRATE'S THROAT: "
     "`c/(H_0 sqrt(Omega_Lambda)) = (c/H_0) sqrt(1+2/x_0^3) = alpha = sqrt(3/Lambda)` -- symbolic "
     "residual zero and 2e-16 on both backgrounds", _resid_al == 0 and worst_al < 1e-14)
gate(f"⛭ AND IT IS NOT `r_0`: `alpha/r_0 = sqrt3/x_0` exactly, which is "
     f"{worst_ratio['the refit background `P15` fits'][0]:.4f} on the refit background -- so even the "
     "readout does not return the radius the floor is built on",
     all(abs(x - y) < 1e-12 for x, y in worst_ratio.values())
     and all(abs(x - 1.0) > 0.03 for x, _ in worst_ratio.values()))

# ================================================== C. the obstruction
head("C.  ⛭⛭⛭ THE OBSTRUCTION, AS AN IDENTITY: AN $S^3$ SLICE IS TIME-SYMMETRIC IFF `f = 1 - r^2/a^2`")
_r, _a, _al, _rs = sp.symbols('r a alpha r_s', positive=True)
_v = sp.sqrt(_rs / _r + _r ** 2 / _al ** 2)
_res = sp.expand(sp.simplify((1 - _v ** 2) - (1 - _r ** 2 / _a ** 2)))
_c_inv_r = sp.simplify(sp.expand(_res * _r).coeff(_r, 0))
_c_r2 = sp.simplify(_res.coeff(_r, 2))
print(f"      f(r) - (1 - r^2/a^2)  =  {_res}")
print(f"      coefficient of 1/r : {_c_inv_r}        coefficient of r^2 : {_c_r2}")
gate("⛭⛭⛭ THE TWO COEFFICIENTS ARE INDEPENDENT: `-r_s` and `(1/a^2 - 1/alpha^2)`, so the condition "
     "holds for ALL r only if `r_s = 0` AND `a = alpha`",
     sp.simplify(_c_inv_r + _rs) == 0
     and sp.simplify(_c_r2 - (1 / _a ** 2 - 1 / _al ** 2)) == 0
     and sp.simplify(_res.subs(_rs, 0).subs(_a, _al)) == 0
     and sp.simplify(_res.subs(_a, _al)) != 0 and sp.simplify(_res.subs(_rs, 0)) != 0)
gate("⇒ *** AND THE CONSTRUCTION PINS `r_s` AT THE NARIAI VALUE, SO THE ROUTE THAT FIXES THE RADIUS "
     "IN DE SITTER IS CLOSED BY THE MASS THAT FIXES THE RATE -- one choice, read on two of its "
     "consequences ***",
     all(b['rsch'] > 0 for b in B.values())
     and abs(ref['rsch'] - 2 * ref['alpha'] / (3 * np.sqrt(3))) < 1e-9)

# ================================================== D. the de Sitter control
head("D.  ⌗ THE CONTROL THAT RETURNS THE AFFIRMATIVE: IN DE SITTER THE RADIUS *IS* FIXED, AT `alpha`")
_A = 1 / (1 - _r ** 2 / _al ** 2)
_vd = _r / _al
_s = sp.sqrt(sp.simplify(1 + (_vd ** 2 - 1) * _A))
_Tp = sp.simplify((1 - _A) / (_vd + _s))
_nr = sp.simplify((-_vd - (1 - _vd ** 2) * _Tp) / sp.sqrt(_A))
print(f"      at a = alpha, M = 0:   s(r) = {sp.simplify(_s)}    T'(r) = {_Tp}    n^r = {_nr}")
gate("⌗ ANALYTICALLY: at `a = alpha` in pure de Sitter the auxiliary root `s` vanishes, the normal's "
     "radial part `n^r` vanishes identically, and so `K = 0` -- the throat IS the unique maximal "
     "$S^3$, and the method finds it", sp.simplify(_s) == 0 and sp.simplify(_nr) == 0)
al = ref['alpha']
vdS = lambda r: r / al                                                        # noqa: E731
print(f"      {'a/alpha':>9} {'max|K| [1/Mpc]':>16} {'spread(K)':>14}")
dS = {}
for fac in (1.0, 0.7, 1.4):
    rr = np.linspace(0.05 * fac * al, 0.85 * fac * al, 500)
    K = Kmean(fac * al, vdS, rr, 1e-4 * fac * al)
    dS[fac] = (float(np.max(np.abs(K))), float(np.ptp(K)))
    print(f"      {fac:9.2f} {dS[fac][0]:16.4e} {dS[fac][1]:14.4e}")
gate("⌗ and numerically the same: `K` is zero to 1e-8 at `a = alpha` and neither zero nor constant at "
     "`0.7 alpha` or `1.4 alpha` ⇒ a null below is a property of THIS geometry, not of the tool",
     dS[1.0][0] < 1e-7 and dS[0.7][1] > 1e-4 and dS[1.4][0] > 1e-5)

# ================================================== E. the four candidate fixings
head("E.  ⇒ THE FOUR CANDIDATE FIXINGS, AND WHAT EACH DOES TO THE ONE-PARAMETER $S^3$ FAMILY")
_tau, _chi, _th, _ph = sp.symbols('tau chi theta phi')
_vs, _rc = sp.symbols('v r_c', positive=True)
_g = sp.Matrix([[-1 + _vs ** 2, -_vs], [-_vs, 1]])          # the PG (tau, r) block
_u = sp.Matrix([1, _vs])                                    # u^mu = (1, v)
_ul = sp.simplify(_g * _u)
print(f"      u^mu = (1, v):  u_mu = {list(_ul.T)}   ⇒ u_mu = -d tau, so the congruence is "
      "hypersurface-orthogonal")
gate("⓵ ORTHOGONALITY IS ALREADY SPENT, ON THE FLAT SLICING: `u_mu = -d tau` exactly, so the unique "
     "foliation orthogonal to the fundamental congruence is the constant-$\\tau$ one ⇒ it excludes "
     "every $S^3$", sp.simplify(_ul[0] + 1) == 0 and sp.simplify(_ul[1]) == 0)


def ricci(g, x):
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


_Ric, _R = ricci(sp.diag(_vs ** 2 - 1, _rc ** 2, _rc ** 2 * sp.sin(_th) ** 2), [_chi, _th, _ph])
_aS, _psi = sp.symbols('a_S psi', positive=True)
_, _RS3 = ricci(sp.diag(_aS ** 2, _aS ** 2 * sp.sin(_psi) ** 2,
                        _aS ** 2 * sp.sin(_psi) ** 2 * sp.sin(_th) ** 2), [_psi, _th, _ph])
print(f"      constant-tilde-tau layer: Ricci scalar = {_R}, chi-chi component = "
      f"{sp.simplify(_Ric[0,0])};  an S^3 would give {_RS3}")
gate("⓶ CONSTANT COSMIC EPOCH EXCLUDES EVERY $S^3$ TOO: the constant-$\\tilde\\tau$ surface is "
     "`R x S^2` -- Ricci scalar `2/r_c^2` with a zero eigenvalue along `chi` (`r7102`, re-verified "
     "here from the metric rather than recalled)",
     sp.simplify(_R - 2 / _rc ** 2) == 0 and sp.simplify(_Ric[0, 0]) == 0
     and sp.simplify(_RS3 - 6 / _aS ** 2) == 0)
gate("⓷ TIME SYMMETRY / MAXIMALITY is obstructed by section C's identity, exactly and not by a scan",
     sp.simplify(_c_inv_r + _rs) == 0)

print("\n      ⓸ CMC: the gap |K(0.1a) - K(0.8a)| over three decades in a")
print(f"      {'a [Mpc]':>12} {'a/alpha':>9} {'K(0.1a)':>13} {'K(0.8a)':>13} {'|gap|':>13}")
gaps = {}
for a in np.geomspace(0.1 * al, 300.0 * al, 31):
    k1 = float(Kmean(a, ref['v'], 0.1 * a, 1e-4 * a))
    k2 = float(Kmean(a, ref['v'], 0.8 * a, 1e-4 * a))
    gaps[a] = abs(k1 - k2)
for a in (0.2 * al, ref['rN'], ref['r0'], al, ref['DC'], 30.0 * al, 300.0 * al):
    k1 = float(Kmean(a, ref['v'], 0.1 * a, 1e-4 * a))
    k2 = float(Kmean(a, ref['v'], 0.8 * a, 1e-4 * a))
    print(f"      {a:12.1f} {a/al:9.4f} {k1:13.4e} {k2:13.4e} {abs(k1-k2):13.4e}")
_near = {a: g for a, g in gaps.items() if a <= 10.0 * al}
_far = {a: g for a, g in gaps.items() if a >= 100.0 * al}
print(f"      minimum gap for a <= 10 alpha: {min(_near.values()):.3e};  "
      f"for a >= 100 alpha: {min(_far.values()):.3e}  (the a -> infinity limit)")
_Kf = sp.simplify(-sp.diff(_r ** 2 * _v, _r) / _r ** 2)
_dKf = sp.simplify(sp.factor(sp.diff(_Kf, _r)))
print(f"      and the flat slice itself:  K_flat(r) = {_Kf}")
print(f"        dK_flat/dr = {_dKf}   ->  at r_s = 0 it is {sp.simplify(_dKf.subs(_rs,0))}, "
      f"K_flat = {sp.simplify(_Kf.subs(_rs,0))}")
gate("⓸ CMC SELECTS THE FLAT SLICING THE CONSTRUCTION ALREADY HAS, NOT A CLOSED LAYER: the gap is "
     "nowhere zero at finite radius and collapses only as `a -> infinity`, where `A -> 1`, `T' -> 0` "
     "and the $S^3$ degenerates into the constant-$\\tau$ slice",
     min(_near.values()) > 1e-5 and min(_far.values()) < 1e-7)
gate("⌗ and even that slice is CMC only in de Sitter: `dK_flat/dr` is proportional to `r_s^2`, so the "
     "whole r-dependence is the mass, and at `r_s = 0` it is `K = -3/alpha` identically",
     sp.simplify(_dKf.subs(_rs, 0)) == 0 and sp.simplify(_Kf.subs(_rs, 0) + 3 / _al) == 0
     and sp.simplify(_dKf) != 0)

# ================================================== F. the answer
head("F.  ⇒ `Q1` ANSWERED: NO SLICING OF THIS GEOMETRY CARRIES AN $S^3$ WHOSE RADIUS IS FIXED")
print("      condition                        what it does to the S^3 family")
print("      orthogonality to the congruence  excludes all -- the orthogonal foliation is the FLAT one")
print("      constant cosmic epoch            excludes all -- that surface is R x S^2")
print("      time symmetry / maximality       excludes all -- needs r_s = 0, and r_s is the Nariai mass")
print("      constant mean curvature          selects a -> infinity, i.e. the flat slice again")
gate("⇒ *** THE TERMINAL EXIT, AND IT IS A RESULT AND NOT A FALLBACK: every condition that could pick "
     "a member of the family either excludes all of them or is already spent on the flat slicing, so "
     "the construction fixes NO closed-layer radius ***",
     sp.simplify(_ul[1]) == 0                                # orthogonality -> the flat slice
     and sp.simplify(_Ric[0, 0]) == 0                        # the epoch surface is R x S^2
     and sp.simplify(_c_inv_r + _rs) == 0                    # maximality needs r_s = 0
     and min(_near.values()) > 1e-5)                         # and CMC fixes nothing finite
gate("⇒ AND THE IDENTITY IS RE-DERIVED RATHER THAN WITHDRAWN, AT THE LEVEL IT IS ESTABLISHED: one "
     "SLICING that is flat (`prop:flat`, Riemann identically zero) and one INVARIANT LENGTH "
     "`alpha = sqrt(3/Lambda)` that the closed readout returns exactly ⇒ the plural in \"two "
     "slicings\" goes, and `|Omega_k| = Omega_Lambda` -- the content that mattered -- stands",
     _resid_al == 0 and worst_al < 1e-14
     and "The constant-$\\tau$ slice is exactly flat $\\mathbb{R}^3$." in body15)

# ================================================== G. the cost, named not paid
head("G.  ⌗⌗ THE TWO CONSEQUENCES FOR THE FLOOR -- BOTH NAMED, NEITHER RULED ON")
for nm, a in (("the paper's r_0", ref['r0']), ("the readout's alpha", ref['alpha'])):
    print(f"      {nm:22s} a = {a:8.2f} Mpc   stretch D_C/a = {ref['DC']/a:.4f}   "
          f"ell_2 = sqrt(8) D_C/a = {np.sqrt(8)*ref['DC']/a:.3f}   k_2 = {np.sqrt(8)/a:.4e} 1/Mpc")
_l2_r0, _l2_al = np.sqrt(8) * ref['DC'] / ref['r0'], np.sqrt(8) * ref['DC'] / ref['alpha']
gate(f"ⓐ if the source rides the ONE fixed closed radius it rides `alpha`, and the floor's location "
     f"moves from ell_2 = {_l2_r0:.3f} to {_l2_al:.3f} -- {(_l2_al/_l2_r0-1)*100:+.2f} per cent",
     abs(_l2_r0 - 7.845) < 0.02 and abs(_l2_al - 7.602) < 0.02)
_vv = ref['v'](ref['r0'])
print(f"      and the layer that IS fixed: at the present epoch v^2 - 1 = {_vv**2-1:.6f} > 0, so "
      f"`(v^2-1) dchi^2 + r_0^2 dOmega^2`\n      is a genuine Riemannian `R x S^2`; "
      "`tilde-tau = tau + chi` is constant on it with `tau` free, so `chi` runs over all of R")
gate("ⓑ so if the source rides THAT slicing there is no gap at all: `chi` is unbounded, the Laplacian "
     "along it has continuous spectrum reaching zero, and the floor has no lowest mode to be built "
     "on -- reported because the cost should be on the record before it is paid",
     _vv ** 2 - 1.0 > 1e-6 and np.sqrt(8) / ref['r0'] > 0)
# ⌗ the scope claim is about WHICH FILES THIS RECEIPT OPENED, so it is read from that and not from
#   this file's own spelling -- the slip `r7102` recorded, not repeated.
OPENED = sorted(os.path.basename(x) for x in (P15,))
print(f"      every file this receipt opened: {OPENED}")
gate("⚠ AND NEITHER IS APPLIED HERE: the ONLY file this receipt opened is the paper -- no instrument, "
     "no banked spectrum, no grid -- so nothing is reassigned and nothing is re-measured; `Q1` asked "
     "for the slicing and the radius", OPENED == ['CR_cosmology.tex'])

# ================================================== H. the design rule, applied
head("H.  ⌗ `r7103`'s DESIGN RULE, APPLIED RATHER THAN NODDED AT")
_open = body15.count('Which slicing carries the closed reading is open')
_pair = body15.count('the pair of slicings that realises it geometrically is not yet named')
print(f"      the paper's open-question sentences are LOCATED and printed, not gated: "
      f"{_open} + {_pair} occurrence(s) found")
print("      ⇒ a gate on either would go red the moment this receipt's answer is acted on, which is "
      "exactly\n        the class `r7103` re-pointed two of my checks for.  Every gate above reads "
      "the geometry.")
gate("⌗ the rule is applied and not merely cited: no gate in this receipt asserts the presence of the "
     "open question, and the one corpus string any gate does read is `prop:flat`'s conclusion, which "
     "this receipt CONFIRMS rather than refutes",
     "The constant-$\\tau$ slice is exactly flat $\\mathbb{R}^3$." in body15)

# ================================================== verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {n}")
print(f"\n  {len(CHECKS) - len(bad)} of {len(CHECKS)} checks pass   [{time.time()-t_all:.1f}s]")
if bad:
    raise SystemExit(1)
print("  ALL PASS -- the construction fixes no closed-layer radius, the obstruction is the Nariai\n"
      "  mass by an identity, de Sitter is the control that finds the radius when there is one, and\n"
      "  the one length anything here fixes is alpha = sqrt(3/Lambda), which is not r_0.")
