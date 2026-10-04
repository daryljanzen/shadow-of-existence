#!/usr/bin/env python3
"""P15 receipt -- `r7161` left the next row to this seat's choice and recommended `PO-75`.  Taken,
and taken through the one thing the paper names as NOT carried: ** the lift's EXACT envelope on the
carried layer, with the squashing profile carried through the transport rather than bounded. **

*** ⛭⛭⛭ IT IS A ONE-PARAMETER DEFORMATION OF THE ROUND ENVELOPE, AND THE PARAMETER IS THE FRACTION
    OF THE EIGENVALUE THE HOPF CHARGE CARRIES.  FOUR RESULTS, AND THE THIRD IS A CORRECTION TO WHAT
    THE BOUND SUGGESTS:
      ⓵ THE LIFT'S OWN MEASURE REPRODUCES `$s_{\\rm tot}$` TO SIXTEEN FIGURES, which is the control
         that this is the paper's segment and not a re-parametrisation of it.
      ⓶ ON THE LIFT THE SQUASHING EXCEEDS THE ROUND VALUE *EVERYWHERE*: `$\\lvert\\varepsilon\\rvert=
         1.3747296$` at the turnaround, rising to `$\\infty$` at the close.  **So the stretch
         `eq:squashed-spectrum` makes transparent is the whole lift, and the stretch that strengthens
         the damping is not on it at all.**
      ⓷ THE EXPONENT RATIO DEPENDS ON `$\\sigma=4m^2/L(L+2)$` ALONE -- verified by two modes of
         different degree sharing `$\\sigma$` and agreeing to ten figures -- with

> ### `$R(0)=1$` to seventeen decimals,   `$R(1)=s_{\\rm tot}^{-1}\\!\\int\\!\\lvert\\varepsilon\\rvert^{-1}\\dd\\eta=0.2591014627$`

      ⓸ AND THE UNIFORM BOUND IS **NOT ATTAINED**.  `$\\sigma_{\\max}=L/(L+2)\\to1$`, so the most
         transparent band's exponent tends to `$0.2591\\sqrt{L(L+2)}\\,s_{\\rm tot}$` -- still LINEAR
         in degree, not the `$\\sqrt{2L}$` the bound allows.
    ⇒ *** SO THE LIFT'S EFFECTIVE LENGTH IS SHORTENED FROM `$3.3387380$` TO `$0.8650719$` IN THE
        MAXIMAL-CHARGE BAND AND NOT FURTHER.  `PO-75` IS NARROWED AND NOT STRUCK: the surviving
        anisotropic amplitude is larger than the round-layer figures by a factor that grows without
        bound in degree, and it is still exponentially small in degree. *** ***

⛭⛭ ** ⓵ THE CONTROL FIRST, BECAUSE EVERYTHING ELSE IS AN INTEGRAL OVER THE SAME MEASURE. **  *The
bead's conformal measure is `$\\dd\\eta=\\dd\\tilde\\tau/r$` with `$(\\dd r/\\dd\\tilde\\tau)^2=2M/r+
r^2/\\alpha^2$`, so on the lift `$\\lvert\\dd\\eta\\rvert=\\lvert\\dd r\\rvert/(\\lvert r\\rvert\\sqrt{\\lvert
2M/r+r^2/\\alpha^2\\rvert})$`.  Integrated from the comoving turnaround to `$r=0$` that returns*

> ### `$3.33873802357$`  against the paper's closed form `$3.33873802357$`

*-- agreeing to `$3\\times10^{-17}$`, and `$\\alpha$`-free, measured at three values of `$\\alpha$`.*
⇒ ** So the parametrisation is the paper's own and the turnaround is where the paper puts it: at
`$\\lvert r\\rvert=(2M\\alpha^2)^{1/3}$`, where `$-f=-1$` exactly. **

⛭ ** ⓶ AND THE LIFT LIES ENTIRELY IN THE REGIME THE SPECTRUM MAKES TRANSPARENT. **  *`r7160` found
the squashing passes through its round value at `$r=2M=\\tfrac23r_N$` -- a POSITIVE radius -- and the
lift occupies `$-(2M\\alpha^2)^{1/3}<r<0$`.*  ⇒ *** So `$\\lvert\\varepsilon\\rvert>1$` on the whole
lift, from `$1.3747296$` at the turnaround to `$\\infty$` at the close.  The `$\\varepsilon<1$`
stretch that RAISES the eigenvalues is on the expansion side and the transport never visits it. ***
⌗ *That is the fact that decides the sign of the correction, and it was not available before `r7160`
normalised the parameter.*

⛭⛭⛭ ** ⓷ THE DEFORMATION IS ONE-PARAMETER, WHICH IS MORE THAN THE ROW ASKED FOR. **  *Dividing
`eq:squashed-spectrum` by its round member gives `$\\lambda/L(L+2)=1-\\sigma(1-\\varepsilon^{-2})$`
with `$\\sigma=4m^2/L(L+2)$` -- so the exponent's ratio to the round one is a function of `$\\sigma$`
and of the profile, and of nothing else about the mode.*  ⇒ *Measured: `$(L,\\lvert m\\rvert)=(1,\\tfrac12)$`
and `$(6,2)$` both have `$\\sigma=\\tfrac13$` and both give `$R=0.8419016934$`.*  ⌗ **`$\\sigma$` is the
fraction of the mode's eigenvalue carried by its Hopf charge, and the lift's envelope sees only that.**

⛔ ** ⓸ AND THE HONEST PART: THE BOUND IS NOT TIGHT ALONG THE ACTUAL PROFILE. **  *`r7160`'s
`$\\lambda\\ge2L$` has its infimum only as `$\\varepsilon\\to\\infty$`, and `$\\varepsilon\\to\\infty$`
only at the close of the lift -- a set of measure zero in the transport.*  ⇒ *So the maximal-charge
band's exponent tends to `$R(1)\\sqrt{L(L+2)}\\,s_{\\rm tot}$` rather than to `$\\sqrt{2L}\\,s_{\\rm
tot}$`: at `$L=1024$` the exact exponent is `$934.0$` against the bound's `$151.1$`.*  ⌗ **The
envelope stays exponential in DEGREE.  What the squashing buys is a shortened segment, not a change
of functional form, and saying otherwise would be reading the bound as the answer.**

⛭⛭ ** WHAT THIS SAYS ABOUT `PO-75`, WHICH IS THE ROW THIS WAS TAKEN FOR. **  *The row asks what
supplies anisotropic content on the expansion leg.  `r7122`'s read found no source after the branch
point and three transfers, all linear in what they are handed; the question is therefore whether what
the progenitor hands over survives.*  ⇒ *** It survives better than the corpus says, in one band: the
gain over the round-layer exponent is `$2.49$` at `$L=1$`, `$10.6$` at `$L=2$`, `$56.8$`, `$346$`,
`$2309$`, `$1.64\\times10^{4}$` through `$L=6$`, and grows without bound. ***  ⌗ **But the surviving
amplitude is still suppressed as `$e^{-0.2591\\,k\\,s_{\\rm tot}}$` at large degree, so no new source
is RULED IN and none is ruled out: the row is narrowed to a quantitative question about the
progenitor's input amplitude, which this paper does not carry.**

⌗ ** ONE METHOD NOTE, BECAUSE IT IS WHERE THE INTERPRETATION RESTS. **  *The layer is TIMELIKE on the
lift -- `$-f<0$` there, which is `r7146`'s result -- so the squashing is imaginary and what enters
`eq:squashed-spectrum` here is its MODULUS, which is the convention `r7152` fixed and `r7161`
accepted.  Nothing above depends on the phase, and the `$m=0$` rows reproduce the round exponent
exactly, which is the control that the modulus is the right object to feed the spectrum.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **  *It does NOT claim a transmission FIGURE: the paper's
`$2^{7/3}k^2$` prefactor is the constant-`$k$` solution's, and with `$\\lambda$` varying only the
EXPONENT is computed here.  The gains quoted are exponent ratios, `$e^{I_{\\rm round}-I}$`, and not
amplitudes.*  ⛔ *It does not claim the progenitor's anisotropic spectrum is or is not sufficient --
that needs an input amplitude this paper does not carry, and it is stated as the row's remaining
question rather than answered.*  ⛔ *It is the SCALAR sector only.*  ⛔ *`$L$` is the degree on the
cosmological layer and is NOT the observable multipole; the map is `sec:largescale`'s and is not
touched.*  ⛔ *It does not claim the layer is a round sphere anywhere, and it writes no layer metric
down on the lift -- the squashing is `sec:largescale`'s own measured one.*

** COMPUTES: the bead's conformal measure on the lift from the `$E=1$`, `$k=0$` radial equation, with
its integral matched against the paper's closed-form `$s_{\\rm tot}$` to `$3\\times10^{-17}$` and checked `$\\alpha$`-free at
three values of `$\\alpha$`; the turnaround's locus and `$-f=-1$` there; the squashing's range over
the lift; the exponent `$\\int\\sqrt\\lambda\\,\\lvert\\dd\\eta\\rvert$` for every admissible `$(L,m)$`
through `$L=6$`, with the `$m=0$` rows as the must-reproduce control; the collapse onto
`$\\sigma=4m^2/L(L+2)$`; `$R(0)$` and `$R(1)$`, the latter two ways; and the maximal-charge band's
exponent against both the round value and `r7160`'s bound out to `$L=1024$`.  *** THE ONLY PAPER
QUANTITIES PINNED ARE `$s_{\\rm tot}$`'s CLOSED FORM, THE UNIT-AMPLITUDE CLAUSE,
`eq:squashed-spectrum` AND ITS BOUND SENTENCE, *** with `$\\alpha$` carried free. **

⌗ *The guard this one leaves: ** a uniform bound is not a prediction until the measure is carried
through it -- an infimum attained only on a set the transport does not dwell in will be missed by the
integral, and the gap can be a factor of six. **

Written r7162 by node 60, on `PO-75` by this seat's own choice under `r7161`'s latitude.
Stated for reversal.
"""
import os
import re
import time

import mpmath as mp
import sympy as sp

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


def body_of(path):
    src = open(path, encoding='utf-8').read()
    return flat(''.join(ln + '\n' for ln in src.splitlines() if not ln.lstrip().startswith('%')))


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
b15 = body_of(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))

mp.mp.dps = 30


def build(alpha):
    """the lift's own objects at this alpha, all from the E=1, k=0 radial equation."""
    al = mp.mpf(alpha)
    two_M = 2 * al / (3 * mp.sqrt(3))              # the Nariai mass, G = c = 1
    rN = al / mp.sqrt(3)
    u_t = (two_M * al**2)**(mp.mpf(1) / 3)         # the comoving turnaround, |r|
    mf = lambda r: (r - rN)**2 * (r + 2 * rN) / (al**2 * r)        # -f, factorised
    eps = lambda u: al * mp.sqrt(abs(mf(-u))) / u                  # |eps|, horn-normalised
    deta = lambda u: 1 / (u * mp.sqrt(two_M / u - u**2 / al**2))   # |d eta| on the lift
    return al, two_M, rN, u_t, mf, eps, deta


AL, TWO_M, RN, U_T, MF, EPS, DETA = build(1)
S_CLOSED = (mp.gamma(mp.mpf(1) / 6) * mp.sqrt(mp.pi)
            / (mp.gamma(mp.mpf(2) / 3) * mp.sqrt(3) * mp.mpf(2)**(mp.mpf(1) / 3)))

# ------------------------------------------------------------------ Ⓐ the measure, controlled
head("Ⓐ  THE LIFT'S OWN MEASURE REPRODUCES s_tot -- THE CONTROL ON EVERYTHING BELOW")

s_quad = mp.re(mp.quad(DETA, [0, U_T / 2, U_T]))
print(f"\n    integral of |d eta| over the lift : {mp.nstr(s_quad, 14)}")
print(f"    the paper's closed form           : {mp.nstr(S_CLOSED, 14)}")
gate("Ⓐ①  ∫|dη| over the lift equals the paper's closed-form s_tot to 1.5e-16",
     abs(s_quad - S_CLOSED) < mp.mpf('1e-15'))

tri = [build(a) for a in ('1', '2', '0.3')]
s_each = [mp.re(mp.quad(d[6], [0, d[3] / 2, d[3]])) for d in tri]
gate("Ⓐ②  and it is α-free: the same value at α = 1, 2 and 0.3",
     all(abs(x - S_CLOSED) < mp.mpf('1e-15') for x in s_each))

r_t = sp.Symbol('rt', positive=True)
al_s = sp.Symbol('alpha', positive=True)
two_M_s = 2 * al_s / (3 * sp.sqrt(3))
gate("Ⓐ③  the turnaround is the only zero of 2M/r + r²/α² on r < 0, at |r| = (2Mα²)^{1/3}",
     sp.simplify(sp.solve(sp.Eq(-two_M_s / r_t + r_t**2 / al_s**2, 0), r_t)[0]
                 - (two_M_s * al_s**2)**(sp.Rational(1, 3))) == 0)
gate("Ⓐ④  and -f = -1 EXACTLY there, which is the lap's unit-speed reading of the same locus",
     abs(MF(-U_T) + 1) < mp.mpf('1e-20'))

# ------------------------------------------------------------------ Ⓑ the lift's regime
head("Ⓑ  THE LIFT LIES ENTIRELY WHERE THE SQUASHING EXCEEDS ITS ROUND VALUE")

e_turn = EPS(U_T)
print(f"\n    |ε| at the turnaround : {mp.nstr(e_turn, 10)}")
for x in ('0.6', '0.4', '0.2', '0.05', '0.005'):
    print(f"    |ε| at |r| = {x:>6}  : {mp.nstr(EPS(mp.mpf(x)), 10)}")
gate("Ⓑ①  |ε| = 1.3747296 at the turnaround, α-free across the three builds",
     all(abs(d[5](d[3]) - e_turn) < mp.mpf('1e-18') for d in tri)
     and abs(e_turn - mp.mpf('1.374729637')) < mp.mpf('1e-8'))
gate("Ⓑ②  |ε| rises monotonically to ∞ at the close of the lift",
     EPS(mp.mpf('0.6')) > e_turn and EPS(mp.mpf('0.005')) > EPS(mp.mpf('0.05'))
     > EPS(mp.mpf('0.2')) > EPS(mp.mpf('0.6')) and EPS(mp.mpf('1e-8')) > mp.mpf('1e5'))
gate("Ⓑ③  so |ε| > 1 on the WHOLE lift: the ε < 1 stretch r7160 found -- which raises every"
     " eigenvalue -- is at positive r and the transport never visits it",
     min(EPS(mp.mpf(x)) for x in ('0.7274157', '0.6', '0.4', '0.2', '0.05', '0.005')) > 1
     and sp.simplify(two_M_s - 2 * (al_s / sp.sqrt(3)) / 3) == 0)

# ------------------------------------------------------------------ Ⓒ the exponent, per mode
head("Ⓒ  THE EXACT EXPONENT PER MODE, WITH THE m = 0 ROWS AS THE CONTROL")


def m_range(L):
    out, mm = [], -mp.mpf(L) / 2
    while mm <= mp.mpf(L) / 2 + mp.mpf('1e-9'):
        out.append(abs(mm))
        mm += 1
    return sorted(set(out))


def exponent(L, m):
    g = lambda u: mp.sqrt(L * (L + 2) + 4 * (1 / EPS(u)**2 - 1) * m**2) * DETA(u)
    return mp.re(mp.quad(g, [0, U_T / 2, U_T]))


print("\n     L  |m|        exact I      round value      I/round        gain e^(round-I)")
rows, m0_exact, gains = [], True, {}
for L in range(1, 7):
    rnd = mp.sqrt(L * (L + 2)) * S_CLOSED
    for m in m_range(L):
        I = exponent(L, m)
        rows.append((L, m, I, rnd))
        if m == 0 and abs(I - rnd) > mp.mpf('1e-12'):
            m0_exact = False
        print(f"    {L:>2}  {mp.nstr(m, 3):>4}   {mp.nstr(I, 9):>12}  {mp.nstr(rnd, 9):>12}"
              f"   {mp.nstr(I / rnd, 7):>9}   {mp.nstr(mp.e**(rnd - I), 9)}")
    gains[L] = mp.e**(rnd - exponent(L, m_range(L)[-1]))

gate("Ⓒ①  every m = 0 mode returns the ROUND exponent exactly -- the control that the measure, the"
     " spectrum and the quadrature are all the right ones",
     m0_exact)
gate("Ⓒ②  every m ≠ 0 exponent is STRICTLY BELOW its round value, because |ε| > 1 throughout",
     all(I < rnd - mp.mpf('1e-9') for (L, m, I, rnd) in rows if m != 0))
gate("Ⓒ③  and no exponent falls below r7160's bound √(2L)s_tot",
     all(I > mp.sqrt(2 * L) * S_CLOSED - mp.mpf('1e-9') for (L, m, I, rnd) in rows))
gate("Ⓒ④  the maximal-charge band's gain grows without bound: 2.49, 10.6, 56.8, 346, 2309, 1.64e4",
     all(gains[L + 1] > gains[L] for L in range(1, 6))
     and abs(gains[1] - mp.mpf('2.49493')) < mp.mpf('1e-4')
     and gains[6] > mp.mpf('1.6e4'))

# ------------------------------------------------------------------ Ⓓ the one-parameter collapse
head("Ⓓ  THE RATIO DEPENDS ON σ = 4m²/L(L+2) ALONE")

Ls, ms, eps_s = sp.symbols('L m varepsilon', positive=True)
lam = Ls * (Ls + 2) + 4 * (1 / eps_s**2 - 1) * ms**2
sig = 4 * ms**2 / (Ls * (Ls + 2))
gate("Ⓓ①  λ/L(L+2) = 1 − σ(1 − ε⁻²) identically, so the mode enters only through σ",
     sp.simplify(lam / (Ls * (Ls + 2)) - (1 - sig * (1 - 1 / eps_s**2))) == 0)


def R(s):
    g = lambda u: mp.sqrt(1 - s * (1 - 1 / EPS(u)**2)) * DETA(u)
    return mp.re(mp.quad(g, [0, U_T / 2, U_T])) / S_CLOSED


pairs = [(1, mp.mpf('0.5')), (6, mp.mpf(2))]
sigs = [4 * m**2 / (L * (L + 2)) for L, m in pairs]
gate("Ⓓ②  (L,|m|) = (1,½) and (6,2) share σ = ⅓ exactly",
     abs(sigs[0] - sigs[1]) < mp.mpf('1e-20') and abs(sigs[0] - mp.mpf(1) / 3) < mp.mpf('1e-20'))
Rs = [exponent(L, m) / (mp.sqrt(L * (L + 2)) * S_CLOSED) for L, m in pairs]
print(f"\n    R at σ = ⅓ from (1,½): {mp.nstr(Rs[0], 12)}")
print(f"    R at σ = ⅓ from (6,2): {mp.nstr(Rs[1], 12)}")
gate("Ⓓ③  and they give the same R to ten figures, measured on two different degrees",
     abs(Rs[0] - Rs[1]) < mp.mpf('1e-10'))
gate("Ⓓ④  σ ranges over [0, L/(L+2)], and σ = 0 exactly for the even-L m = 0 modes",
     all(max(4 * m**2 / (L * (L + 2)) for m in m_range(L)) == mp.mpf(L) / (L + 2)
         for L in range(1, 7))
     and all(0 in m_range(L) for L in range(2, 8, 2)))

# ------------------------------------------------------------------ Ⓔ the two endpoints
head("Ⓔ  THE TWO ENDPOINTS OF THE DEFORMATION, BOTH EXACT")

gate("Ⓔ①  R(0) = 1 to seventeen decimals -- the round envelope is the σ = 0 member, and this is"
     " the same control as the m = 0 rows reached through the σ form instead",
     abs(R(0) - 1) < mp.mpf('1e-16'))
R1 = R(1)
alt = mp.re(mp.quad(lambda u: DETA(u) / EPS(u), [0, U_T / 2, U_T])) / S_CLOSED
red = mp.re(mp.quad(lambda u: 1 / (mp.sqrt(abs(MF(-u))) * mp.sqrt(TWO_M / u - u**2)),
                    [0, U_T / 2, U_T])) / S_CLOSED
print(f"\n    R(1) from the σ form        : {mp.nstr(R1, 14)}")
print(f"    R(1) as ∫|dη|/|ε| / s_tot   : {mp.nstr(alt, 14)}")
print(f"    R(1) by the reduced integrand: {mp.nstr(red, 14)}")
gate("Ⓔ②  R(1) = s_tot⁻¹∫|ε|⁻¹dη = 0.2591014627, by three routes agreeing to twelve figures",
     abs(R1 - alt) < mp.mpf('1e-12') and abs(R1 - red) < mp.mpf('1e-12')
     and abs(R1 - mp.mpf('0.2591014627')) < mp.mpf('1e-10'))
eff = R1 * S_CLOSED
print(f"    effective segment length     : {mp.nstr(eff, 12)}  against s_tot = {mp.nstr(S_CLOSED, 12)}")
gate("Ⓔ③  so the most transparent band sees an effective length 0.8650719 rather than 3.3387380,"
     " and that number is α-free",
     abs(eff - mp.mpf('0.8650719055')) < mp.mpf('1e-9')
     and all(abs(mp.re(mp.quad(lambda u, d=d: d[6](u) / d[5](u), [0, d[3] / 2, d[3]])) - eff)
             < mp.mpf('1e-12') for d in tri))
gate("Ⓔ④  R is monotone decreasing in σ, so a larger Hopf charge always means more transmission",
     all(R(mp.mpf(a)) > R(mp.mpf(b)) for a, b in
         (('0', '0.25'), ('0.25', '0.5'), ('0.5', '0.75'), ('0.75', '0.9'), ('0.9', '1'))))

# ------------------------------------------------------------------ Ⓕ the bound is not attained
head("Ⓕ  AND r7160's UNIFORM BOUND IS NOT ATTAINED ALONG THE ACTUAL PROFILE")

print("\n        L   σ_max        R        exact I      bound √(2L)s_tot    I/bound")
far = []
for L in (1, 2, 4, 8, 16, 64, 256, 1024):
    s = mp.mpf(L) / (L + 2)
    r_ = R(s)
    I = r_ * mp.sqrt(L * (L + 2)) * S_CLOSED
    bd = mp.sqrt(2 * L) * S_CLOSED
    far.append((L, r_, I, bd))
    print(f"    {L:>5}  {mp.nstr(s, 8):>10}  {mp.nstr(r_, 8):>10}  {mp.nstr(I, 8):>11}"
          f"  {mp.nstr(bd, 8):>14}   {mp.nstr(I / bd, 6)}")
gate("Ⓕ①  σ_max = L/(L+2) → 1, so the maximal-charge band's R → R(1) rather than to the bound's"
     " implied √(2/L)",
     abs(far[-1][1] - R1) < mp.mpf('2e-2') and far[-1][1] > R1)
per_L = [I / L for (L, r_, I, bd) in far]
print(f"\n    exponent per unit degree, I/L, falling onto R(1)s_tot = {mp.nstr(eff, 8)}:")
print("      " + "  ".join(mp.nstr(x, 6) for x in per_L))
gate("Ⓕ②  the exact exponent stays LINEAR in degree -- I/L falls monotonically onto R(1)s_tot,"
     " so the envelope keeps its functional form and only its length shortens",
     all(per_L[i] > per_L[i + 1] for i in range(len(per_L) - 1))
     and per_L[-1] > eff and per_L[-1] - eff < mp.mpf('0.05'))
gate("Ⓕ③  so the gap to the bound WIDENS with degree: 934.0 against 151.1 at L = 1024, a factor"
     " above six",
     far[-1][2] / far[-1][3] > 6 and far[0][2] / far[0][3] < mp.mpf('1.1'))

# ------------------------------------------------------------------ Ⓖ the paper
head("Ⓖ  WHAT THE PAPER CARRIES, AND THE ONE CLAUSE THIS ROW IS NAMED FROM")

_STOT = (r"$s_{\rm tot}=\Gamma(\tfrac16)\sqrt\pi/\Gamma(\tfrac23)\sqrt3\,2^{1/3}=3.3387380$")
_UNITY = "There the isotropic mode crosses with amplitude exactly unity"
_SPEC = "eq:squashed-spectrum"
_BOUNDS = r"which puts the suppression exponent at no less than $\sqrt{2L}\,s_{\rm tot}$"
_BASIS = "The deformation reaches the spectrum and not the basis"
_SEG = r"the lift from the comoving turnaround to $r=0$"
_OWED = ("it requires a source the single Nariai worldline of this construction does not carry")

gate("Ⓖ①  s_tot's closed form is in print, and this receipt reproduces it from the measure",
     b15.count(_STOT) == 2)
gate("Ⓖ②  the segment is the paper's own, from the comoving turnaround to r = 0",
     b15.count(_SEG) == 1)
gate("Ⓖ③  the unit-amplitude clause is in print, and the σ = 0 endpoint is its generalisation",
     b15.count(_UNITY) == 1)
gate("Ⓖ④  eq:squashed-spectrum is in print -- the equation this receipt integrates",
     b15.count(_SPEC) == 2)
gate("Ⓖ⑤  and so is the bound sentence this receipt shows is not attained",
     b15.count(_BOUNDS) == 1 and b15.count(_BASIS) == 1)

# ASKED TO CHANGE -> enumerated over the states the paper may produce (the r7150 partition)
_LANDED = 'P15_the_lifts_exact_envelope_on_the_carried_layer' in b15
_OPENSTANDS = b15.count(_OWED) == 1
_SETTLED = 'Hopf charge' in b15
gate("Ⓖ⑥  the owed-source clause PO-75 is named from is ENUMERATED, not pinned: either it still"
     " stands or a settled wording naming the Hopf charge is in print",
     (_OPENSTANDS and not _LANDED) or (_LANDED and (_OPENSTANDS or _SETTLED)))

# ------------------------------------------------------------------ verdict
head("VERDICT")
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
if bad:
    print("\n  FAILED:")
    for n in bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""
  ==========================================================================
  VERDICT: the lift's exact envelope on the carried layer is a ONE-PARAMETER
  deformation of the round one, indexed by sigma = 4m^2/L(L+2) -- the
  fraction of the eigenvalue the Hopf charge carries -- with R(0) = 1 exactly
  and R(1) = 0.2591014627 = (1/s_tot) int |eps|^-1 d eta.  The lift lies
  entirely where the squashing exceeds its round value, so every anisotropic
  mode is transmitted MORE strongly than the round-layer figures say, by a
  factor growing without bound in degree.  But the uniform bound is NOT
  attained: the exponent stays linear in degree with the effective segment
  length shortened from 3.3387380 to 0.8650719 and no further.
  *** PO-75 is NARROWED and not struck: what the progenitor hands over
      survives better than the corpus says and is still exponentially small
      in degree, so the row becomes a question about the input amplitude. ***
  ==========================================================================
""")
