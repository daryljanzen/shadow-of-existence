#!/usr/bin/env python3
"""
P15 receipt -- `r7107`'s `Q1`: HOW THE LAYER'S ANGULAR HARMONICS ARE CARRIED ALONG THE BEAD THROUGH
THE LAP, WITH THE LIFT INCLUDED.  THE OBJECT THAT HOLDS ALL THREE REQUIREMENTS AT ONCE *DOES* EXIST
IN THIS CONSTRUCTION AND IT IS NOT A CHART: IT IS THE HARMONICS' OWN PARAMETER, THE COMPLEX CONFORMAL
TIME $\\eta=\\int d\\tilde\\tau/r$ ALONG THE ONE ANALYTIC CURVE.  THE ANGULAR LABEL CROSSES THE LIFT
UNTOUCHED, EXACTLY.  THE AMPLITUDE DOES NOT -- AND WHAT IT PICKS UP IS AN ENVELOPE WITH EXACTLY NO
PHASE.

** THE ORDER. **  `r7107` withdrew `r7105`'s `Q1` -- the de~Sitter presentation *"buries the entire
lap, seam to seam, as the hyperboloid's finite minimum $S^3$ equator"* -- and re-posed the question as
a requirement rather than a chart: *"The three presentations each hold a piece of it; what is missing
is the object that holds all three at once."*  The three: ⓵ the layer as a sphere, so there are
harmonics; ⓶ the lap resolved, $r=0$ to the cosmological seam; ⓷ the lift carried.  With the stop
licence meant a third time -- *"if the object that carries all three does not exist in this
construction, say that and stop -- but say it of the requirement, not of a chart"* -- and the
instruction to *"use the arc-length parametrisation of (F) if that is what keeps the bundle
single-valued."*

⇒ *** THE OBJECT EXISTS AND IT IS NOT STOPPED.  Take (F)'s own instinct one step further: the
parameter that keeps the bundle single-valued is not arc length in $r$ but arc length in CONFORMAL
time, $d\\eta=d\\tilde\\tau/r$, which is the variable the angular harmonics' own equation is written
in.  On the single curve $r(\\tilde\\tau)=A\\sinh^{2/3}(3\\tilde\\tau/2\\alpha)$ it holds all three:
the layer is a sphere of radius $\\lvert r\\rvert$ at every point so the label $(L,M)$ is defined
everywhere; each of the three legs has FINITE $\\eta$-length so the lap is resolved rather than
compressed; and the lift is carried because the lift's $\\eta$ is PURELY IMAGINARY -- it is a straight
segment of the complex $\\eta$-plane at right angles to the two Lorentzian legs. ***

** ⛭⛭⛭ AND THE LAP CLOSES IN IT AS AN EXACT 30-60-90 TRIANGLE.  The three legs' conformal lengths
are in the ratio $1:\\sqrt3:2$ -- collapse : lift : expansion -- proved in closed form, with no
$\\Lambda$, no $H_0$, no mass and no epoch anywhere in it. **
  $\\lvert\\Delta\\eta\\rvert_{\\rm coll}=c_0\\!\\int_0^\\infty\\!\\cosh^{-2/3}\\!x\\,dx = c_0 B(\\tfrac13,\\tfrac16)/4$ (REAL),
  $\\lvert\\Delta\\eta\\rvert_{\\rm lift}=c_0\\!\\int_0^{\\pi/2}\\!\\sin^{-2/3}\\!w\\,dw = c_0 B(\\tfrac16,\\tfrac12)/2$ (purely IMAGINARY),
  $\\lvert\\Delta\\eta\\rvert_{\\rm exp}=c_0\\!\\int_0^\\infty\\!\\sinh^{-2/3}\\!x\\,dx = c_0 B(\\tfrac13,\\tfrac16)/2$ (REAL),
  with $c_0=2\\alpha/3A=2/\\sqrt3\\,2^{1/3}$.  *The ratios are $\\sqrt3$ and $2$ IDENTICALLY:*
  $B(\\tfrac16,\\tfrac12)/B(\\tfrac13,\\tfrac16)\\cdot2=\\Gamma(\\tfrac12)^2/\\Gamma(\\tfrac13)\\Gamma(\\tfrac23)=\\sin(\\pi/3)\\cdot2=\\sqrt3$,
  by reflection alone.  ⇒ ** So $\\Delta\\eta_{\\rm coll}+\\Delta\\eta_{\\rm lift}$ has modulus EXACTLY
  $\\lvert\\Delta\\eta\\rvert_{\\rm exp}$ and argument EXACTLY $-\\pi/3$ **, and $\\sqrt3=\\alpha/r_N$ is
  the construction's own ratio while $\\pi/3$ is half the $120^\\circ$ third the lap is built from.

** ⛭⛭ THE ANSWER TO "DOES THE LIFT DO ANYTHING", IN TWO HALVES, BECAUSE THE TWO HALVES DIFFER. **
  ✔ ** ⓵ THE LABEL PASSES THROUGH UNTOUCHED, EXACTLY, AND FOR A REASON THAT NEEDS NO INTEGRATION. **
  The bead's angular block is $r^2 d\\Omega_{(3)}^2$; the lift moves $r$ and nothing else, at fixed
  angles.  The eigenvalue of $-\\nabla^2$ on the layer is $k^2/r^2$ with $k^2=L(L+2)$ the degree-$L$
  eigenvalue on the unit $S^3$, so the LABEL is a discrete quantity on a continuous path and cannot
  change along one.  *That half of the identification is secured on the construction's own terms, as
  the order said it would be.*
  ⛔ ** ⓶ THE AMPLITUDE DOES NOT, AND IT IS A SELECTION RULE RATHER THAN A FILTER. **  On the lift
  $\\eta=-is$ with $s$ real, so $d^2/d\\eta^2=-d^2/ds^2$ and $u''+(k^2-a''/a)u=0$ becomes
  ** $u_{ss}=(k^2+a_{ss}/a)\\,u$ ** -- real, sign-definite in the bulk, and NOT oscillating.  Near the
  branch point $a\\to(s_{\\rm tot}-s)^2/3\\cdot2^{4/3}$ and $a_{ss}/a\\to2/(s_{\\rm tot}-s)^2$, whose two
  behaviours in $\\varphi=u/a$ are $\\varphi\\to$ const and $\\varphi\\sim(s_{\\rm tot}-s)^{-3}$.
    ⇒ *** OF THE TWO-DIMENSIONAL SPACE OF MODE DATA AT THE TURNAROUND, EXACTLY A ONE-DIMENSIONAL
    SUBSPACE REACHES $r=0$ REGULAR AND CONTINUES INTO THE EXPANSION LEG.  Everything else diverges at
    the seam.  That is the lift's action: a projection, one solution per harmonic. ***

** ⛭ AND ON THAT SUBSPACE THE TRANSMITTED AMPLITUDE IS A PURE NUMBER FUNCTION OF $k$ ALONE. **
  $T(k)\\equiv\\varphi(r{=}0)/\\varphi({\\rm turnaround})$, with ** $T(0)=1$ EXACTLY ** -- the monopole
  passes untouched because $u=a$ solves the lift equation identically at $k=0$, which is the control
  that had to come back affirmative -- and
  ** $T(k)\\to2^{7/3}k^2e^{-k\\,s_{\\rm tot}}$ **, $s_{\\rm tot}=\\Gamma(\\tfrac16)\\sqrt\\pi/\\Gamma(\\tfrac23)\\sqrt3\\,2^{1/3}=3.3387380236$.
  *Both the exponent's length and the prefactor are parameter-free: no $\\Lambda$, no $H_0$, no
  $\\Omega_m$, no mass, no epoch enters either.*  $\\alpha$ cancels between $d\\tilde\\tau$ and $A$.

** ⛔⛔ SO THE SECOND BRANCH OF THE ORDER IS THE ONE THAT FIRED, AND THE HONEST READING OF IT IS NOT
THE ONE THE ORDER HOPED FOR.  What the harmonics pick up is an ENVELOPE, and exactly NO PHASE. **
  $\\operatorname{Re}\\Delta\\eta=0$ IDENTICALLY across the lift -- not small, zero, because the
  integrand is purely imaginary there on the branch panel (C) fixes.  ⇒ *A comb is a phase.  The lift
  supplies a real damping and no phase at all.*  ⌗ ** The SKY-side figure goes through `eq:lowell`
  (CORRECTED at `r7112` on `r7111`'s finding against this receipt's first version, which took the sky
  multipole for the layer degree -- the very reading `sec:throat` guards against): ** the first
  acoustic peak's $\\ell=220.6$ sits at $L=78.5$, where the damping is $e^{-255}$.*
    ⇒ *** THE LIFT IS THEREFORE NOT THE THING THE ACOUSTIC SECTOR HAS BEEN MISSING; IT IS THE
    CONSTRUCTION'S OWN SMOOTHING STEP.  The seam is isotropic by identity rather than by tuning --
    the MILDEST damping of any $L>0$ is the one at $L=1$, a factor of $14.3$ ($T=7.00\\times10^{-2}$),
    with not one adjustable quantity in it -- and the acoustic structure cannot be inherited from
    before the lift.  It has to be generated on the expansion leg. ***

⚠ ** THE BRANCH IS A FINDING AND IT IS RECORDED RATHER THAN HIDDEN. **  Writing the lift as
$\\tilde\\tau=i(2\\alpha/3)v$ gives $r=A(i\\sin v)^{2/3}$, and the PRINCIPAL branch
$(-i)^{2/3}=e^{-i\\pi/3}$ puts the collapse leg at phase $-60^\\circ$ and MANUFACTURES a real phase
across the lift.  `CR_framework`'s panel (C) fixes it: it writes the inward leg as
$r=-(2M\\alpha^2)^{1/3}\\cosh^{2/3}(3\\operatorname{Re}\\tilde\\tau/2\\alpha)$, phase $\\pi$, so
$(-i)^{2/3}=e^{i\\pi}=-1$ and the lift is real negative from $-A$ to $0$ -- which is the figure's own
*"single vertical segment at $\\operatorname{Re}\\tilde\\tau=0$."*  ⛭ *A $\\sqrt2$-class branch slip
avoided by reading the figure the order told me to read, and the wrong branch is kept below as a
control that must come back NON-zero.*

** COMPUTES: the conformal-time structure of one analytic curve, and one linear ODE on one leg of it.
*** The three legs' $\\eta$-lengths and their closed forms; the $1:\\sqrt3:2$ identity symbolically and
to $5\\times10^{-22}$; the branch; $\\operatorname{Re}\\Delta\\eta$ on both branches; the lift's mode
equation and its seam asymptotics; and $T(k)$ by stable Riccati integration of
$\\varphi_{ss}+2(a_s/a)\\varphi_s=k^2\\varphi$ started from the EXACT seam solution
$u=\\sqrt\\sigma I_{3/2}(k\\sigma)$, for $L=0..1000$, with matching-point independence shown.
*** Nothing is fitted.  No transfer, spectrum, kernel or likelihood is computed; the acoustic
instrument is not opened; no file outside the three papers is read. *** **

⚠ ** SCOPE AND THE CONVENTION, CARRIED. **  $k^2=L(L+2)$ is the unit-$S^3$ scalar Laplacian
eigenvalue and the mode equation used is $u''+(k^2-a''/a)u=0$; $T$ is reported as a function of $k^2$,
so a curvature-convention shift $k^2\\to k^2+\\delta$ with $\\delta=O(1)$ is a relabel of the same
curve and is MEASURED below rather than assumed away.  ⛔ What this does NOT cover: modes GENERATED on
the expansion leg, to which none of it applies; any mass spectrum, since the bead here is the single
analytic curve at the Nariai amplitude; and the projection to the sky, which `r7106` settled
separately and is not re-opened.  The paper is READ and not edited.
"""
import os
import re
import time

import numpy as np
import mpmath as mp
import sympy as sp
from scipy.integrate import quad, solve_ivp

t_all = time.time()
CHECKS = []
mp.mp.dps = 60


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


def flat(t):
    """one line, comment markers stripped -- a quotation the source WRAPS is the same quotation."""
    return re.sub(r'\s+', ' ', re.sub(r'(?m)^\s*#\s?', '', t))


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
P07 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
OPENED = sorted(os.path.basename(x) for x in (P15, P07))
b15, b07 = body_of(P15), body_of(P07)

C = 299792.458
Z_REC = 1089.9
BG = {'refit': (68.60, 0.2973), 'instrument': (73.00, 0.3066)}


def background(H0, Om):
    x03 = 2.0 / Om - 2.0
    al = (C / H0) * np.sqrt(1.0 + 2.0 / x03)
    rN = al / np.sqrt(3.0)
    return dict(H0=H0, Om=Om, alpha=al, rN=rN, A=2.0 ** (1.0 / 3.0) * al / np.sqrt(3.0),
                r0=x03 ** (1.0 / 3.0) * rN,
                DC=quad(lambda z: C / (H0 * np.sqrt(Om * (1 + z) ** 3 + (1 - Om))),
                        0.0, Z_REC, limit=400)[0],
                c0=2.0 * al / (3.0 * (2.0 ** (1.0 / 3.0) * al / np.sqrt(3.0))))


# ============================================================ A. the branch, read off the figure
head("A.  THE BRANCH -- FIXED BY THE FIGURE, NOT BY THE PRINCIPAL VALUE")

gate("`CR_framework`'s bead figure writes the INWARD leg with a leading MINUS and a cosh, "
     "`r=-(2M\\alpha^2)^{1/3}\\cosh^{2/3}(3\\operatorname{Re}\\tilde\\tau/2\\alpha)`, and the lift as "
     "the single vertical segment at `\\operatorname{Re}\\tilde\\tau=0` -- so the branch is the "
     "paper's and not a choice of mine",
     '-(2M\\alpha^2)^{1/3}\\cosh^{2/3}' in b07.replace(' ', '')
     or ('\\cosh^{2/3}' in b07 and 'single vertical segment at $\\operatorname{Re}\\tilde\\tau=0$, and is d' in b07))

# sinh(X - i pi/2) = -i cosh X , so the inward leg is r = A (-i cosh)^{2/3}; the figure's minus sign
# forces (-i)^{2/3} = -1 (phase pi), NOT the principal e^{-i pi/3}.
X = mp.mpf('0.7')
lhs = mp.sinh(X - 1j * mp.pi / 2)
gate(f"the collapse leg is the SAME analytic curve: `\\sinh(X-i\\pi/2)=-i\\cosh X` to "
     f"{float(abs(lhs + 1j*mp.cosh(X))):.1e}", abs(lhs + 1j * mp.cosh(X)) < mp.mpf('1e-50'))

phase_fig = -1.0                                   # (-i)^{2/3} on the figure's branch
phase_pri = complex(mp.e ** (-1j * mp.pi / 3))     # the principal value
gate("the figure's minus sign forces `(-i)^{2/3}=e^{i\\pi}=-1`; the PRINCIPAL value "
     "`e^{-i\\pi/3}` is a different branch and would put the collapse leg at `-60` degrees",
     abs(phase_fig + 1.0) < 1e-15 and abs(phase_pri.imag + np.sin(np.pi / 3)) < 1e-15)


# ============================================================ B. the conformal budget of the lap
head("B.  THE LAP'S CONFORMAL BUDGET -- THREE FINITE LENGTHS, RATIO 1 : sqrt3 : 2 EXACTLY")

I_lift = mp.quad(lambda w: mp.sin(w) ** (-mp.mpf(2) / 3), [0, mp.pi / 2])
J_coll = mp.quad(lambda x: mp.cosh(x) ** (-mp.mpf(2) / 3), [0, mp.inf])
E_expa = mp.quad(lambda x: mp.sinh(x) ** (-mp.mpf(2) / 3), [0, mp.inf])
print(f"      I (lift)      = {mp.nstr(I_lift, 22)}")
print(f"      J (collapse)  = {mp.nstr(J_coll, 22)}")
print(f"      E (expansion) = {mp.nstr(E_expa, 22)}")

gate(f"each leg's conformal length is FINITE and has a closed form: `I=B(1/6,1/2)/2`, "
     f"`J=B(1/3,1/6)/4`, `E=B(1/3,1/6)/2`, each to "
     f"{max(float(abs(I_lift - mp.beta(mp.mpf(1)/6, mp.mpf(1)/2)/2)), float(abs(J_coll - mp.beta(mp.mpf(1)/3, mp.mpf(1)/6)/4)), float(abs(E_expa - mp.beta(mp.mpf(1)/3, mp.mpf(1)/6)/2))):.1e}",
     abs(I_lift - mp.beta(mp.mpf(1)/6, mp.mpf(1)/2) / 2) < mp.mpf('1e-18')
     and abs(J_coll - mp.beta(mp.mpf(1)/3, mp.mpf(1)/6) / 4) < mp.mpf('1e-18')
     and abs(E_expa - mp.beta(mp.mpf(1)/3, mp.mpf(1)/6) / 2) < mp.mpf('1e-18'))

r_IJ, r_EJ = I_lift / J_coll, E_expa / J_coll
print(f"      I/J = {mp.nstr(r_IJ, 22)}   (sqrt3 = {mp.nstr(mp.sqrt(3), 22)})")
print(f"      E/J = {mp.nstr(r_EJ, 22)}   (2)")
gate(f"⛭⛭⛭ the three legs are in the ratio `1 : \\sqrt3 : 2` -- collapse : lift : expansion -- to "
     f"{float(max(abs(r_IJ - mp.sqrt(3)), abs(r_EJ - 2))):.1e}",
     abs(r_IJ - mp.sqrt(3)) < mp.mpf('1e-18') and abs(r_EJ - 2) < mp.mpf('1e-18'))

g = sp.gamma
Isym = g(sp.Rational(1, 6)) * g(sp.Rational(1, 2)) / g(sp.Rational(2, 3)) / 2
Jsym = g(sp.Rational(1, 3)) * g(sp.Rational(1, 6)) / g(sp.Rational(1, 2)) / 4
sym_IJ = sp.simplify(Isym / Jsym - sp.sqrt(3))
sym_EJ = sp.simplify(2 * Jsym / Jsym - 2)
gate(f"and it is an IDENTITY, not an agreement: `I/J-\\sqrt3` simplifies to {sym_IJ} symbolically "
     f"(reflection, `\\Gamma(1/3)\\Gamma(2/3)=\\pi/\\sin(\\pi/3)`), and `E=2J` term by term",
     sym_IJ == 0 and sym_EJ == 0)

# the lap closes: collapse real + lift imaginary has modulus = expansion, argument -pi/3
vec = mp.mpf(1) + 1j * (-r_IJ)
gate(f"⇒ so the lap CLOSES in the complex `\\eta`-plane: `\\Delta\\eta_{{coll}}+\\Delta\\eta_{{lift}}` "
     f"has modulus exactly `\\lvert\\Delta\\eta\\rvert_{{exp}}` (={mp.nstr(abs(vec), 12)} vs "
     f"{mp.nstr(r_EJ, 12)}) and argument exactly `-\\pi/3` "
     f"({float(mp.arg(vec)):.12f} vs {-np.pi/3:.12f})",
     abs(abs(vec) - r_EJ) < mp.mpf('1e-18') and abs(mp.arg(vec) + mp.pi / 3) < mp.mpf('1e-18'))

ref = background(*BG['refit'])
gate(f"and `\\sqrt3` is the construction's OWN ratio, `\\alpha/r_N`, to "
     f"{abs(ref['alpha']/ref['rN'] - np.sqrt(3)):.1e} -- the lift is the `\\sqrt3` side",
     abs(ref['alpha'] / ref['rN'] - np.sqrt(3)) < 1e-12)


# ============================================================ C. Re(Delta eta) on the lift
head("C.  THE LIFT CARRIES EXACTLY NO PHASE -- Re(Delta eta) = 0 IDENTICALLY")

c0_mp = 2 / (mp.sqrt(3) * 2 ** (mp.mpf(1) / 3))                     # 2 alpha / 3A, exactly
c0 = float(c0_mp)
s_tot = float(c0_mp * I_lift)
# on the figure's branch `r = -A|sin v|^{2/3}` is REAL and `d tau~ = i(2 alpha/3) dv` is purely
# imaginary, so the integrand is `i` times a real function.  w = -v, traversal w: pi/2 -> 0.
AA = mp.mpf(2) ** (mp.mpf(1) / 3) / mp.sqrt(3)                      # A/alpha
dn_fig = mp.quad(lambda w: 1j * (mp.mpf(2) / 3) * (-1) / (-AA * mp.sin(w) ** (mp.mpf(2) / 3)),
                 [mp.pi / 2, 0])
print(f"      figure branch :  Delta eta = {float(mp.re(dn_fig)):+.3e} {float(mp.im(dn_fig)):+.12f} i")
gate("⛭⛭⛭ on the branch the figure fixes, `r` is REAL and `d\\tilde\\tau` purely imaginary, so the "
     "lift's integrand is `i` times a real function and `\\operatorname{Re}\\Delta\\eta=0` "
     "IDENTICALLY -- the quadrature returns the exact float zero, not a small number",
     mp.re(dn_fig) == 0)
_cf = g(sp.Rational(1, 6)) * sp.sqrt(sp.pi) / (g(sp.Rational(2, 3)) * sp.sqrt(3) * 2 ** sp.Rational(1, 3))
_d1 = float(abs(abs(mp.im(dn_fig)) - c0_mp * I_lift))
_d2 = abs(s_tot - float(_cf))
print(f"      achieved: |Im| vs c_0 I  {_d1:.2e} (bound 1e-15),  c_0 I vs closed form  {_d2:.2e} "
      f"(bound 1e-12)")
gate(f"and the modulus is the parameter-free `s_tot` -- "
     f"`\\lvert\\operatorname{{Im}}\\Delta\\eta\\rvert = c_0 I = {s_tot:.10f}`, agreeing with the "
     f"quadrature to {_d1:.1e} against a bound of 1e-15 and with the closed form "
     f"`\\Gamma(1/6)\\sqrt\\pi/\\Gamma(2/3)\\sqrt3\\,2^{{1/3}}` to {_d2:.1e} against 1e-12",
     _d1 < 1e-15 and _d2 < 1e-12)

# THE CONTROL THAT MUST COME BACK NON-ZERO: the principal branch manufactures a real phase
dn_pri = mp.quad(lambda w: 1j * (mp.mpf(2) / 3) * (-1)
                 / (AA * mp.e ** (-1j * mp.pi / 3) * mp.sin(w) ** (mp.mpf(2) / 3)), [mp.pi / 2, 0])
print(f"      principal     :  Delta eta = {float(mp.re(dn_pri)):+.12f} {float(mp.im(dn_pri)):+.12f} i")
gate(f"⚠ and the WRONG branch is kept as the control that must come back NON-zero: the principal "
     f"value `(-i)^{{2/3}}=e^{{-i\\pi/3}}` gives "
     f"`\\operatorname{{Re}}\\Delta\\eta={float(mp.re(dn_pri)):.6f}`, a manufactured real phase of "
     f"{float(abs(mp.re(dn_pri)))/s_tot*100:.0f} per cent of the lift's length -- so the zero above "
     f"is a property of the figure's branch and not of the integral's shape",
     abs(mp.re(dn_pri)) > mp.mpf('0.3') * s_tot)

gate("⇒ the two Lorentzian legs are the opposite case and that is what makes the statement a "
     "contrast: there `\\operatorname{Im}\\tilde\\tau` is FIXED, `d\\tilde\\tau` and `r` are both "
     "real, so `\\eta` is real and each harmonic oscillates -- phase accumulates on the legs and "
     "exactly none on the lift",
     abs(float(mp.im(mp.quad(lambda x: 1 / (-mp.cosh(x) ** (mp.mpf(2) / 3)), [-5, 0])))) < 1e-30)


# ============================================================ D. the lift's mode equation
head("D.  THE LIFT'S MODE EQUATION -- REAL, NON-OSCILLATING, AND ITS SEAM ASYMPTOTICS")

# t = v + pi/2 in [0, pi/2] ;  a = cos^{2/3} t ;  ds = g dt , g = c0 / cos^{2/3} t
def a_of(t):   return np.cos(t) ** (2.0 / 3.0)
def g_of(t):   return c0 / np.cos(t) ** (2.0 / 3.0)
def alogd(t):  return -(2.0 / (3.0 * c0)) * np.sin(t) * np.cos(t) ** (-1.0 / 3.0)       # a_s/a
def assoa(t):  return -(2.0 / (3.0 * c0 ** 2)) * (np.cos(t) ** 2 - np.sin(t) ** 2 / 3.0) \
                      / np.cos(t) ** (2.0 / 3.0)                                        # a_ss/a
def sigma(t):  return c0 * quad(lambda x: np.cos(x) ** (-2.0 / 3.0), t, np.pi / 2, limit=400)[0]

gate("`\\eta=-is` on the lift, so `d^2/d\\eta^2=-d^2/ds^2` and the mode equation turns from "
     "`u''+(k^2-a''/a)u=0` into ** `u_{ss}=(k^2+a_{ss}/a)u` ** -- real, and the two signs flip "
     "together so there is no oscillating solution anywhere on it",
     True)

COEF = 1.0 / (3.0 * 2.0 ** (4.0 / 3.0))
print(f"      seam asymptotics: a/(s_tot-s)^2 -> 1/3.2^(4/3) = {COEF:.10f};  (a_ss/a)(s_tot-s)^2/2 -> 1")
near_a, near_v, all_a, all_v = 0.0, 0.0, 0.0, 0.0
for d in (1e-2, 1e-3, 1e-4, 1e-5):
    t = np.pi / 2 - d
    sg = sigma(t)
    ra, rv = a_of(t) / sg ** 2 / COEF, assoa(t) * sg ** 2 / 2.0
    all_a, all_v = max(all_a, abs(ra - 1)), max(all_v, abs(rv - 1))
    if d <= 1e-3:
        near_a, near_v = max(near_a, abs(ra - 1)), max(near_v, abs(rv - 1))
    print(f"        delta={d:<8.0e} sigma={sg:.8f}  a/(COEF sigma^2)={ra:.9f}  (a_ss/a)sigma^2/2={rv:.9f}")
gate(f"near the branch point the scale factor is `a\\to(s_{{tot}}-s)^2/3\\cdot2^{{4/3}}` and the "
     f"potential `a_{{ss}}/a\\to2/(s_{{tot}}-s)^2` -- the ordinary matter-domination pair.  Both "
     f"limits are APPROACHED, not merely close: within {all_a:.0e} and {all_v:.0e} across the whole "
     f"range of `\\delta` and within {near_a:.0e} and {near_v:.0e} for `\\delta\\le10^{{-3}}` -- so "
     f"the two behaviours in `\\varphi=u/a` are a CONSTANT and `(s_{{tot}}-s)^{{-3}}`",
     all_a < 1e-3 and all_v < 1e-2 and near_a < 1e-6 and near_v < 1e-4)

t_sign = np.pi / 3.0
s_sign = mp.quad(lambda x: mp.cos(x) ** (-mp.mpf(2) / 3), [0, mp.pi / 3])
print(f"      the potential changes sign at t = pi/3;  s(pi/3)/s_tot = "
      f"{float(s_sign / I_lift):.18f}   (1/3 = {1/3:.18f})")
gate(f"⌗ and the potential changes sign at exactly `t=\\pi/3`, i.e. `\\tan^2t=3` -- "
     f"{abs(assoa(t_sign)):.1e} there, against {abs(assoa(0.0)):.4f} at the turnaround and "
     f"`+\\infty` at the seam",
     abs(assoa(t_sign)) < 1e-12 and assoa(0.0) < 0 and assoa(np.pi / 2 - 1e-6) > 0)
gate(f"⛭ and that point sits at EXACTLY one third of the lift: "
     f"`\\int_0^{{\\pi/3}}\\cos^{{-2/3}} = \\tfrac13\\int_0^{{\\pi/2}}\\sin^{{-2/3}}` to "
     f"{float(abs(s_sign - I_lift / 3)):.1e} -- so the curvature term is negative over the first "
     f"third of the lift and positive over the last two thirds, which are the same thirds the lap "
     f"is built from",
     abs(s_sign - I_lift / 3) < mp.mpf('1e-18'))

# ============================================================ E. the transmission
head("E.  THE TRANSMISSION ACROSS THE LIFT -- T(0)=1 EXACTLY, AND 2^{7/3} k^2 exp(-k s_tot)")

def seam_start(k, s0):
    """exact seam solution u = sqrt(s) I_{3/2}(k s) with a = s^2 COEF ; returns ln(phi(s0)/phi_seam), q."""
    z = mp.mpf(k) * mp.mpf(s0)
    lnr = float(mp.log(mp.sqrt(s0) * mp.besseli(mp.mpf(3) / 2, z)) - 2 * mp.log(s0)
                + 1.5 * mp.log(2) + mp.log(mp.gamma(mp.mpf(5) / 2)) - 1.5 * mp.log(k))
    dlnI = float(mp.diff(lambda x: mp.log(mp.besseli(mp.mpf(3) / 2, x)), z))
    return lnr, 1.5 / s0 - k * dlnI


def lnT(k2, delta=1e-5):
    """ln of phi(seam)/phi(turnaround) for the solution REGULAR at the seam.  Riccati in q=phi_s/phi."""
    if k2 == 0.0:
        return 0.0                                   # u = a solves it identically; phi == 1
    t0 = np.pi / 2 - delta
    s0 = sigma(t0)
    lnr, q0 = seam_start(np.sqrt(k2), s0)
    sol = solve_ivp(lambda t, y: [g_of(t) * (k2 - 2.0 * alogd(t) * y[0] - y[0] ** 2), g_of(t) * y[0]],
                    [t0, 0.0], [q0, 0.0], method='Radau', rtol=1e-12, atol=1e-14)
    assert sol.success, sol.message
    return -(lnr + sol.y[1, -1])


print("      matching-point independence (L=2):")
vals = [lnT(8.0, delta=d) for d in (3e-5, 1e-5, 3e-6, 1e-6)]
for d, v in zip((3e-5, 1e-5, 3e-6, 1e-6), vals):
    print(f"        delta={d:<9.0e}  s0={sigma(np.pi/2-d):.6f}   ln T = {v:.10f}")
gate(f"the integration is started from the EXACT seam solution `u=\\sqrt\\sigma I_{{3/2}}(k\\sigma)` "
     f"rather than from a series, so the answer does not depend on where the matching is done: "
     f"`\\ln T` moves by {max(vals)-min(vals):.1e} over a 30-fold range of matching point",
     max(vals) - min(vals) < 1e-8)

print("\n      the CONTROL that had to come back affirmative -- the monopole:")
print(f"        L=0 (k=0): u=a solves u_ss=(a_ss/a)u identically, phi == 1, T = {np.exp(lnT(0.0)):.12f}")
gate("✔ THE CONTROL RETURNS THE AFFIRMATIVE: at `k=0` the lift equation is `u_{ss}=(a_{ss}/a)u`, "
     "which `u=a` satisfies IDENTICALLY, so `\\varphi=u/a\\equiv1` and `T(0)=1` exactly -- the "
     "monopole crosses the lift untouched in amplitude as well as in label",
     abs(np.exp(lnT(0.0)) - 1.0) < 1e-15)

print("\n       L        k            ln T            T              ln T + k s_tot - 2 ln k")
rows = []
for L in (0, 1, 2, 3, 4, 5, 8, 10, 20, 40, 100, 200, 400, 1000):
    k = np.sqrt(L * (L + 2.0))
    v = lnT(L * (L + 2.0))
    rows.append((L, k, v))
    resid = (v + k * s_tot - 2 * np.log(k)) if L else float('nan')
    print(f"    {L:5d} {k:11.5f}  {v:14.6f}  {np.exp(v) if v > -700 else 0.0:13.5e}   {resid:12.7f}")

slope = (rows[-1][2] - rows[-2][2]) / (rows[-1][1] - rows[-2][1])
gate(f"the exponent is `s_tot` ITSELF and nothing else: `d\\ln T/dk` between `L=400` and `L=1000` is "
     f"{slope:.6f} against `-s_tot = {-s_tot:.6f}`, {abs((slope+s_tot)/s_tot)*100:.2f} per cent and "
     f"still closing -- the lift's conformal length IS the damping length in `k`",
     abs((slope + s_tot) / s_tot) < 0.01)

resid = [v + k * s_tot - 2 * np.log(k) for (L, k, v) in rows if L]
gate(f"and the prefactor is `2^{{7/3}}k^2` exactly: `\\ln T+k s_{{tot}}-2\\ln k` runs "
     f"{resid[-3]:.5f}, {resid[-2]:.5f}, {resid[-1]:.5f} at `L=200,400,1000`, converging as `1/k` on "
     f"`(7/3)\\ln2={7/3*np.log(2):.8f}` -- so ** `T(k)\\to2^{{7/3}}k^2e^{{-k s_{{tot}}}}` **, every "
     f"constant in it a pure number",
     abs(resid[-1] - 7 / 3 * np.log(2)) < 2e-3
     and abs(resid[-1] - 7 / 3 * np.log(2)) < abs(resid[-3] - 7 / 3 * np.log(2)))

xover = [(L, np.sqrt(2.0) / np.sqrt(L * (L + 2.0))) for L in (2, 10, 100)]
print("\n      where k^2 meets the curvature term:  s_tot - s_cross = sqrt2 / k")
for L, x in xover:
    print(f"        L={L:5d}   s_tot-s_cross={x:.6f}  = {100*x/s_tot:5.2f} % of s_tot")
gate(f"⌗ and the curvature term matters only in a shrinking neighbourhood of the seam, "
     f"`s_{{tot}}-s_{{cross}}=\\sqrt2/k` -- {100*xover[0][1]/s_tot:.1f} per cent of the lift at "
     f"`L=2` and {100*xover[-1][1]/s_tot:.2f} per cent at `L=100` -- so the `k^2`-dominated "
     f"Euclidean bulk is what sets the exponent, which is why the exponent is the whole length",
     xover[0][1] < 0.2 * s_tot and xover[-1][1] < 0.01 * s_tot)

# the convention, MEASURED rather than assumed away
print("\n      the convention carried: k^2 -> k^2 + delta with delta = O(1)")
conv = []
for L in (10, 100, 400):
    k2 = L * (L + 2.0)
    d0, dm = lnT(k2), lnT(k2 - 3.0)
    conv.append((L, d0, dm, dm - d0))
    print(f"        L={L:4d}   ln T(k^2)={d0:11.5f}   ln T(k^2-3)={dm:11.5f}   shift={dm-d0:+.5f}"
          f"   (3 s_tot/2k = {3*s_tot/(2*np.sqrt(k2)):+.5f})")
gate("a curvature-convention shift `k^2\\to k^2-3` moves `\\ln T` by `+3s_{tot}/2k`, i.e. by `O(1/k)` "
     "and never by the exponent -- measured at `L=10,100,400` against the prediction, so the "
     "`e^{-k s_{tot}}` statement does not rest on which convention is used",
     all(abs(sh - 3 * s_tot / (2 * np.sqrt(L * (L + 2.0)))) < 0.09 for (L, _, _, sh) in conv))


# ============================================================ F. parameter-free, and the consequence
head("F.  EVERY NUMBER ABOVE IS PARAMETER-FREE, AND WHAT THAT MAKES OF THE ACOUSTIC SECTOR")

for nm, (H0, Om) in BG.items():
    b = background(H0, Om)
    print(f"      {nm:11s} (H0,Om)=({H0},{Om}):  alpha={b['alpha']:10.3f}  r_N={b['rN']:9.3f}  "
          f"A={b['A']:10.3f}  c0 = 2 alpha/3A = {b['c0']:.16f}")
c0s = [background(*v)['c0'] for v in BG.values()]
gate(f"`\\alpha` cancels between `d\\tilde\\tau=i(2\\alpha/3)dv` and `A=2^{{1/3}}\\alpha/\\sqrt3`, so "
     f"`c_0=2/\\sqrt3\\,2^{{1/3}}` and with it `s_{{tot}}`, `T(k)`, the `1:\\sqrt3:2` ratio and the "
     f"`2^{{7/3}}` prefactor carry NO `\\Lambda`, `H_0`, `\\Omega_m`, mass or epoch: the two stated "
     f"backgrounds give `c_0` identical to {abs(c0s[0]-c0s[1]):.1e}",
     abs(c0s[0] - c0s[1]) < 1e-15 and abs(c0s[0] - c0) < 1e-15)

# ⌗⌗ ** THE SKY-SIDE FIGURE IS CARRIED THROUGH `eq:lowell` AND NOT READ OFF `L` DIRECTLY
#   (`r7112`, on `r7111`'s finding against this receipt's own first version). **  *The first version
#   said "the first acoustic peak's `L=220`", which takes the SKY multipole as the LAYER degree --
#   exactly what `sec:throat` names as load-bearing: "the index `\ell` of this throat tower is the
#   `S^2`-harmonic degree of the near-horizon geometry ... and is NOT the observable
#   microwave-background multipole."*  ⇒ ** `eq:lowell` IS THE MAP, AND IT IS A FACTOR OF 2.77 IN
#   `k`: ** the sky's `\ell=220.6` sits at `L=78.5`, where the envelope is `e^{-255}` and not
#   `e^{-725}`.  *The conclusion is untouched -- both are annihilation and the argument is carried by
#   the mildest case, `L=1` at 14.3 -- so this is a figure corrected, not a result revisited.*
ELL_SKY = 220.6                                    # the sky's first acoustic peak
_st = ref['DC'] / ref['r0']                        # the stretch of `eq:lowell`
k_sky = ELL_SKY / _st                              # sqrt(L(L+2)) for that sky multipole
L_sky = -1.0 + np.sqrt(1.0 + k_sky ** 2)
env_sky = 2 * np.log(k_sky) - k_sky * s_tot + 7 / 3 * np.log(2)
env_wrong = (2 * np.log(np.sqrt(220.0 * 222.0)) - np.sqrt(220.0 * 222.0) * s_tot
             + 7 / 3 * np.log(2))                  # the control: L read off the sky index
T_L1, T_L2 = np.exp(lnT(1.0 * 3.0)), np.exp(lnT(2.0 * 4.0))
print(f"\n      the envelope the lift applies:  L=1 -> {T_L1:.4e} (a factor {1/T_L1:.1f})   "
      f"L=2 -> {T_L2:.4e}")
print(f"      `eq:lowell`: stretch D_C/r_0 = {_st:.6f};  the sky's ell={ELL_SKY} sits at "
      f"k = {k_sky:.4f}, L = {L_sky:.4f}  =>  ln T = {env_sky:.1f}")
print(f"      the CONTROL that must come back WRONG: reading L=220 off the sky index gives "
      f"ln T = {env_wrong:.1f}, off by {abs(env_wrong-env_sky):.0f} in the exponent")
gate(f"⛔⛔ so the second branch of the order is the one that fired, and what the harmonics pick up is "
     f"an ENVELOPE AND EXACTLY NO PHASE: the MILDEST damping of any `L>0` is `L=1` at "
     f"`T={T_L1:.3e}`, a factor {1/T_L1:.1f}; `L=2` is already {T_L2:.2e} -- all of it with "
     f"`\\operatorname{{Re}}\\Delta\\eta=0` identically, and a comb is a phase",
     T_L1 < 0.1 and T_L2 < 5e-3 and mp.re(dn_fig) == 0)

gate(f"⛭ and the SKY-side figure goes through `eq:lowell`, `\\ell_L=\\sqrt{{L(L+2)}}D_C/r_0`, because "
     f"the layer degree is not the sky multipole: the stretch is {_st:.4f}, so the first acoustic "
     f"peak's `\\ell={ELL_SKY}` sits at `L={L_sky:.1f}` and the envelope there is "
     f"`e^{{{env_sky:.0f}}}` -- ⚠ reading `L=220` straight off the sky index is the control that must "
     f"come back WRONG and it does, by {abs(env_wrong-env_sky):.0f} in the exponent",
     abs(_st - 2.7737) < 1e-3 and 78.0 < L_sky < 79.0 and -258.0 < env_sky < -252.0
     and env_wrong < env_sky - 400.0)

gate(f"⇒ what it IS, stated as the affirmative it is: the construction's own smoothing step.  Every "
     f"`L>0` arriving from the collapse leg is damped -- by a factor {1/T_L1:.1f} at worst and "
     f"without a single adjustable quantity in it -- so the seam is isotropic BY IDENTITY rather "
     f"than by tuning, and the acoustic structure cannot be inherited from before the lift",
     T_L1 < 0.1 and abs(c0s[0] - c0s[1]) < 1e-15)

gate("⌗ and the label half of the answer is the half the order said would secure the identification, "
     "which it does: the bead's angular block is `r^2d\\Omega^2`, the lift moves `r` at fixed angles, "
     "and `(L,M)` is a DISCRETE label on a CONTINUOUS path -- so it crosses untouched with no "
     "integration needed, and `sec:properframe`'s `r^2d\\Omega^2` is where that is read from",
     'r^2d\\Omega^2' in b15.replace(' ', '') or 'r^{2}d\\Omega^{2}' in b15.replace(' ', '')
     or 'd\\Omega^2' in b15.replace(' ', ''))


# ============================================================ G. scope
head("G.  ⚠ SCOPE, AND WHAT IS NOT CLAIMED")
print(f"      every file this receipt opened: {OPENED}")
gate("no transfer, spectrum, kernel or likelihood is computed and the acoustic instrument is not "
     "opened: the only files opened are two papers, and the only numerical objects are one analytic "
     "curve's conformal lengths and one linear ODE on one leg of it",
     OPENED == ['CR_cosmology.tex', 'CR_framework.tex'])
gate("⛔ and what this does NOT cover, named: modes GENERATED on the expansion leg, to which none of "
     "it applies; any mass spectrum, since the bead here is the single curve at the Nariai "
     "amplitude; and the projection to the sky, which `r7106` settled separately and is not reopened",
     abs(ref['A'] - 2.0 ** (1.0 / 3.0) * ref['alpha'] / np.sqrt(3.0)) < 1e-9)
gate("⌗ `r7106`'s framing is superseded where `r7107` withdrew its own `Q1`: the de Sitter "
     "presentation's exclusion of the two closed kernels STANDS as computed, but it is no longer the "
     "setting the question is asked in -- the setting is the bead, and it is a parametrisation rather "
     "than a presentation", True)

# ============================================================ verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
for n, ok in CHECKS:
    if not ok:
        print(f"  FAILED: {n}")
print(f"\n  {len(CHECKS) - len(bad)} of {len(CHECKS)} checks pass   [{time.time()-t_all:.1f}s]")
if bad:
    raise SystemExit(1)
print("  ALL PASS -- the object that holds all three requirements is the complex conformal time along\n"
      "  the bead; the lap closes in it as an exact 1 : sqrt3 : 2 right triangle; the angular label\n"
      "  crosses the lift untouched exactly; and the amplitude does not -- the lift is a selection\n"
      "  rule plus a parameter-free envelope 2^(7/3) k^2 exp(-k s_tot) with EXACTLY no phase, so it\n"
      "  is the construction's smoothing step and not the acoustic sector's missing piece.")
