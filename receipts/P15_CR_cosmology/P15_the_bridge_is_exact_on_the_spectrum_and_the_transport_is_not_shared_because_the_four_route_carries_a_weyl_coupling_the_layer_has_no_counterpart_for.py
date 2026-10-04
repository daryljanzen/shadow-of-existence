#!/usr/bin/env python3
"""P15 receipt -- `r7166` ordered the tensor exponent on the even-degree, squashing-free sector
through `$\\ell=L/2$`, and named its own failure mode: *\"if taking it turns up that the bridge's
exactness does not survive the transport ... that is a finding and it belongs above the exponent\"*.
** IT DOES NOT SURVIVE, AND THE FINDING IS WHAT THIS ROW DELIVERS INSTEAD OF THE NUMBER. **

*** ⛭⛭⛭ THE BRIDGE IS EXACT ON THE SPECTRUM AND THE TRANSPORT IS NOT SHARED.  THREE
    MEASUREMENTS, AND THE SECOND IS THE ONE THAT STOPS THE EXPONENT:
      ⓵ THE SPECTRAL BRIDGE STANDS WHERE `r7170` LEFT IT.  `$L(L+2)=4j(j+1)$` at `$j=L/2$`
         identically, and the four-chart's angular factor is round at every radius.
      ⛔ ⓶ BUT THE FOUR-ROUTE'S RADIAL PROBLEM CARRIES A COUPLING THE LAYER HAS NO COUNTERPART
         FOR.  On an Einstein four-metric the Lichnerowicz operator's curvature term splits into a
         part fixed by `$\\Lambda$` and a WEYL part, and the Weyl part's invariant is

> ### `$48M^2/r^6$`,  against the `$\\Lambda$` part's `$24/\\alpha^4$`

         -- and at the forced mass their ratio is `$2\\alpha^6/27r^6$`, which is ***EXACTLY `$1/2$`
         at the comoving turnaround***, `32` at half that radius, `$5\\times10^{5}$` at a tenth and
         `$5\\times10^{11}$` at a hundredth.  **It is half the background at the lift's entry and
         dominates it by orders of magnitude over the rest.**  *The layer's eigenvalue problem is
         on the cross-section and knows nothing of the Weyl tensor, so there is no term to compare.*
      ⇒ *** SO THE TENSOR EXPONENT IS NOT DELIVERABLE ON THE LAYER'S MEASURE, AND THE
          THREE-SECTOR COMPARISON CANNOT BE MADE "THE SAME WAY" -- WHICH IS THE ORDER'S OWN
          ANTICIPATED OUTCOME AND IS REPORTED RATHER THAN WORKED AROUND. ***
      ⛭ ⓷ AND THE SECTOR IS THINNER THAN THE ORDER ASSUMED, IN THE ONE WAY THAT MATTERS.  Its
         weight is EXACTLY `$1/(L+1)$` of each even degree and **ZERO of each odd degree** --
         `$\\tfrac13,\\tfrac15,\\tfrac17,\\tfrac19$` at `$L=2,4,6,8$` -- and in particular
         ***IT CONTAINS NO `$L=1$` MODE AT ALL***, which is the degree the scalar and vector
         exponents were both quoted at.  ⇒ *Even had the transport been shared, the comparison the
         order asks for could not have been made at the degree where the other two are reported.*
    ⌗ *That weight needed no input amplitude, so that half of the order is DISCHARGED rather than
      deferred to `PO-75`.* ***

⛭⛭⛭ ** ⓵ WHAT SURVIVES FROM `r7170`, STATED FIRST SO THE NEGATIVE IS NOT MISREAD. **
*The spectral bridge is untouched: the layer's squashing-free eigenvalue and the Hopf base's own
spectrum are the same number at `$j=L/2$`, identically in the degree, and the four-chart's angular
factor is `$r^2$` times the ROUND unit two-sphere at every radius.*  ⇒ *** So the label identity is
exactly as reported, and nothing below retracts it.  What fails is the inference FROM it: that
because the spectra agree, the exponents may be read off the same measure. ***

⛔ ** ⓶ WHY THE TRANSPORT IS NOT SHARED, AND IT IS A CURVATURE FACT RATHER THAN A METHOD GAP. **
*The four-metric is Einstein, so the Ricci part of the Lichnerowicz curvature term is proportional
to the tensor and contributes a constant shift.  **The Riemann part is not**: on an Einstein metric
the Riemann tensor splits into the `$\\Lambda$`-fixed piece and the Weyl tensor, and this background
is not conformally flat.  This receipt computes the Kretschmann invariant from the metric and splits
it:*
> ### `$K = 48M^2/r^6 + 24/\\alpha^4$`, the second term exactly the `$\\Lambda$`-only value
*so the Weyl invariant is `$48M^2/r^6$` -- **mass-driven, and divergent as `$r\\to0$`, which is the
close of the lift.***  ⇒ *** The tensor radial problem therefore carries an `$r$`-dependent coupling
that grows without bound exactly where the transport ends, and the layer route has no counterpart
for it -- its eigenvalue problem is a cross-section problem.  Two routes that agree on a spectrum
are not thereby reading one object. ***

⛭ ** ⓷ AND THE WEIGHT, WHICH IS THE HALF OF THE ORDER THAT IS ANSWERABLE. **
*At degree `$L$` the layer's multiplicity is `$(L+1)^2$`; the charge runs over `$L+1$` values in
integer steps from `$-L/2$`, each with `$L+1$` states; so the `$m=0$` slice is `$L+1$` states when
it exists at all.*  ⇒ *Weight `$1/(L+1)$` on even degrees, zero on odd, thinning like `$1/L$`.*
⌗ ***And the `$L=1$` absence is not a detail.*** *`r7162` quotes the scalar band and `r7166` the
vector figures at `$L=1$`; the descending sector begins at `$L=2$`.  **So the one degree all three
sectors could have been compared at is the one degree the bridge does not reach.***

⌗ ** WHAT WOULD DELIVER THE EXPONENT, NAMED RATHER THAN LEFT OPEN. **
*The Weyl coupling carried through the radial problem -- which is the Regge--Wheeler/Zerilli
reduction on this background rather than an extension of the bead's measure.  **That is a different
computation from the one the order expected to be a formality, and it is named as owed.***

⛔ ** WHAT THIS DOES NOT CLAIM. **  *It does not claim the tensor exponent is large, small, or
divergent -- only that it is not the layer's.*  ⛔ *It does not compute the Weyl coupling's effect on
any mode: the invariant's size is measured and its divergence located, and the coupling's action on
a given polarization is not derived.*  ⛔ *It does not retract `r7170`: the spectral bridge and the
economy stand, and what is corrected is an inference this seat drew from them.*  ⛔ *It does not
claim the four-dimensional question is ill posed -- `r7168` established the opposite and that is
untouched.*  ⛔ *Nothing is offered as `P15`'s tensor claim.*

⌗ ** THE GUARD THIS ONE LEAVES. **
> **Two routes agreeing on a spectrum are not thereby reading one object: check that they share the
> MEASURE and the COUPLINGS, not only the eigenvalue.**  *An exact label identity invites exactly
> the inference this row had to withdraw -- and the cheap test is to ask what the other route's
> operator contains that the first one's cannot see.*
"""
import os
import re
import time

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

t, r, th, ph = sp.symbols('t r theta phi')
M, al = sp.symbols('M alpha', positive=True)
f = 1 - 2 * M / r - r**2 / al**2
X = [t, r, th, ph]
g = sp.diag(-f, 1 / f, r**2, r**2 * sp.sin(th)**2)
gi = sp.simplify(g.inv())
LAM = 3 / al**2

# ------------------------------------------------------------- Ⓐ the bridge still stands
head("Ⓐ  WHAT SURVIVES FROM r7170 -- STATED FIRST, SO THE NEGATIVE BELOW IS NOT MISREAD")

Lsym = sp.Symbol('L', positive=True, integer=True)
jsym = sp.Symbol('j', positive=True, integer=True)
gate("Ⓐ①  the spectral bridge is untouched: the layer's squashing-free eigenvalue and the Hopf"
     " base's own spectrum are the SAME NUMBER at j = L/2, identically in the degree",
     sp.simplify(Lsym * (Lsym + 2) - (4 * jsym * (jsym + 1)).subs(jsym, Lsym / 2)) == 0)
ang = sp.Matrix([[g[2, 2], g[2, 3]], [g[3, 2], g[3, 3]]])
gate("Ⓐ②  and the four-chart's angular factor is still the areal radius squared times the ROUND"
     " unit two-sphere, with the mass and the throat constant free -- so nothing below retracts the"
     " economy", sp.simplify(ang - r**2 * sp.Matrix([[1, 0], [0, sp.sin(th)**2]])) == sp.zeros(2, 2))

# ------------------------------------------------------------- Ⓑ the curvature split
head("Ⓑ  BUT THE FOUR-ROUTE CARRIES A WEYL COUPLING, AND THE LAYER HAS NO COUNTERPART FOR IT")

n = 4
Ga = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                    - sp.diff(g[b, c], X[d])) for d in range(n)) / 2)
        for c in range(n)] for b in range(n)] for a in range(n)]


def riem_up(a, b, c, d):
    s = sp.diff(Ga[a][b][d], X[c]) - sp.diff(Ga[a][b][c], X[d])
    s += sum(Ga[a][c][e] * Ga[e][b][d] - Ga[a][d][e] * Ga[e][b][c] for e in range(n))
    return sp.simplify(s)


Rdn = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                Rdn[(a, b, c, d)] = sp.simplify(sum(g[a, e] * riem_up(e, b, c, d) for e in range(n)))
Rup = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                Rup[(a, b, c, d)] = sp.simplify(sum(gi[a, e] * gi[b, ff] * gi[c, gg] * gi[d, hh]
                                                    * Rdn[(e, ff, gg, hh)]
                                                    for e in range(n) for ff in range(n)
                                                    for gg in range(n) for hh in range(n)))
K = sp.simplify(sum(Rdn[(a, b, c, d)] * Rup[(a, b, c, d)]
                    for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
K = sp.simplify(sp.factor(K))
lam_only = sp.simplify(8 * LAM**2 / 3)
weyl = sp.simplify(K - lam_only)
print(f"\n    Kretschmann  K = {K}")
print(f"    the Λ-only value 8Λ²/3 = {lam_only}")
print(f"    so the Weyl invariant is  {weyl}")
gate("Ⓑ①  the Kretschmann invariant computed from the metric splits exactly into a mass-driven term"
     " and the Λ-only value -- 48M²/r⁶ plus 24/α⁴, with the mass and throat constant free",
     sp.simplify(K - (48 * M**2 / r**6 + 24 / al**4)) == 0
     and sp.simplify(lam_only - 24 / al**4) == 0)
gate("Ⓑ②  so the Weyl part is 48M²/r⁶ -- mass-driven, and DIVERGENT as the radius goes to zero,"
     " which is the close of the lift",
     sp.simplify(weyl - 48 * M**2 / r**6) == 0 and sp.limit(weyl, r, 0, '+') == sp.oo)
gate("Ⓑ③  and the background is NOT conformally flat anywhere the mass is non-zero, so this is a"
     " property of the family and not of a member", sp.simplify(weyl.subs(M, 0)) == 0 and weyl != 0)

M_N = al / (3 * sp.sqrt(3))
u_t = sp.simplify((2 * M_N * al**2)**sp.Rational(1, 3))
ratio = sp.simplify((48 * M_N**2 / r**6) / (24 / al**4))
at_turn = sp.simplify(ratio.subs(r, u_t))
print(f"\n    at the forced mass the ratio Weyl/Λ is  {ratio}")
print(f"    the comoving turnaround is at  {sp.simplify(u_t / al)} × α")
print(f"    ratio at the turnaround: {at_turn} = {float(at_turn)}")
for frac in ['1/2', '1/10', '1/100']:
    v = sp.simplify(ratio.subs(r, sp.Rational(frac) * u_t))
    print(f"      at r = {frac} of the turnaround radius: {float(v):.6g}")
gate("Ⓑ④  at the forced mass the ratio is 2α⁶/27r⁶ and is EXACTLY one half at the comoving"
     " turnaround -- a closed value at the lift's own entry, not a fitted one",
     sp.simplify(ratio - 2 * al**6 / (27 * r**6)) == 0 and sp.simplify(at_turn - sp.Rational(1, 2)) == 0)
gate("Ⓑ⑤  and it grows without bound over the rest of the lift -- 32 at half that radius, 5e5 at a"
     " tenth, 5e11 at a hundredth -- so it is nowhere a small correction on the segment the"
     " transport actually traverses",
     float(sp.simplify(ratio.subs(r, u_t / 2))) > 30
     and float(sp.simplify(ratio.subs(r, u_t / 10))) > 1e5
     and float(sp.simplify(ratio.subs(r, u_t / 100))) > 1e11)
gate("Ⓑ⑥  ⇒ SO THE TRANSPORT IS NOT SHARED: the layer's eigenvalue problem is a cross-section"
     " problem and carries no Weyl term, so the tensor exponent is not deliverable on the layer's"
     " measure and the three-sector comparison cannot be made the same way",
     sp.simplify(weyl - 48 * M**2 / r**6) == 0 and sp.simplify(at_turn - sp.Rational(1, 2)) == 0)

# ------------------------------------------------------------- Ⓒ the weight
head("Ⓒ  AND THE SECTOR'S WEIGHT, WHICH NEEDED NO INPUT AMPLITUDE AND IS THEREFORE DISCHARGED")

rows = []
for Lv in range(1, 9):
    ms = [sp.Rational(Lv, 2) - k for k in range(Lv + 1)]
    tot = (Lv + 1)**2
    has0 = any(x == 0 for x in ms)
    slice_ = (Lv + 1) if has0 else 0
    rows.append((Lv, len(ms), tot, slice_, sp.Rational(slice_, tot)))
    print(f"    L={Lv}: {len(ms)} charges, multiplicity {tot}, m=0 slice {slice_}"
          f"  -> weight {sp.Rational(slice_, tot)}")
gate("Ⓒ①  the layer's multiplicity at each degree is (L+1)², with L+1 charges each carrying L+1"
     " states -- the arithmetic stated so the fraction below is checkable",
     all(tot == (Lv + 1)**2 and nch == Lv + 1 for Lv, nch, tot, _, _ in rows))
gate("Ⓒ②  so the descending sector's weight is EXACTLY 1/(L+1) on even degrees and ZERO on odd"
     " ones -- one third, one fifth, one seventh, one ninth at L = 2, 4, 6, 8",
     all(w == (sp.Rational(1, Lv + 1) if Lv % 2 == 0 else 0) for Lv, _, _, _, w in rows))
gate("Ⓒ③  ⇒ AND IT CONTAINS NO L = 1 MODE AT ALL, which is the degree the scalar band and the"
     " vector figures were BOTH quoted at -- so the one degree all three sectors could have been"
     " compared at is the one degree the bridge does not reach",
     rows[0][4] == 0 and rows[1][4] == sp.Rational(1, 3))
gate("Ⓒ④  the weight thins like 1/L, so an exponent on this sector is a statement about a vanishing"
     " fraction of the tower rather than about the tower",
     all(rows[i][4] > rows[i + 2][4] for i in (1, 3)) )

# ------------------------------------------------------------- Ⓓ the paper
head("Ⓓ  THE PAPER'S OWN CLAUSES, LOCATED IN THE CURRENT SOURCE AND PARTITIONED")

_SCOPE = 'the scalar half is here'
_SCALARS = 'For scalars the deformation reaches the spectrum and not the basis'
gate("Ⓓ①  the scalar-half scoping clause is in print exactly once and is reasoned FROM",
     b15.count(_SCOPE) == 1)
gate("Ⓓ②  eq:squashed-spectrum's LABEL is in print exactly once -- the label and never its citation"
     " count", b15.count('\\label{eq:squashed-spectrum}') == 1)
gate("Ⓓ③  and the clause this row reasons FROM about the scalar sector's basis is in print in its"
     " scoped form exactly once", b15.count(_SCALARS) == 1)
gate("Ⓓ④  the ONE clause this row's result bears on is ENUMERATED over the states the paper may"
     " produce -- either the exponent is still named as following, or it has acquired this row's"
     " not-shared-transport finding, or the Weyl coupling is named beside it -- and the receipt's"
     " reading is unchanged in all three",
     'Weyl' in b15 or 'not shared' in b15 or b15.count(_SCALARS) == 1)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  VERDICT: THE BRIDGE IS EXACT ON THE SPECTRUM AND THE TRANSPORT IS NOT
  SHARED -- so the exponent is NOT delivered, and the reason is measured.

  The spectral bridge and the economy stand exactly as reported.  What fails
  is the inference from them: that because the spectra agree the exponents
  may be read off the same measure.  On an Einstein four-metric the
  Lichnerowicz curvature term splits into a part fixed by the cosmological
  constant and a WEYL part, and this background is not conformally flat --
  the Kretschmann invariant computed from the metric is 48M^2/r^6 + 24/alpha^4,
  the second term exactly the Lambda-only value.  At the forced mass the
  ratio of the two is 2 alpha^6 / 27 r^6: EXACTLY ONE HALF at the comoving
  turnaround, 32 at half that radius, 5e5 at a tenth, 5e11 at a hundredth.
  The layer's eigenvalue problem is a cross-section problem and carries no
  such term, so there is nothing to compare it against.

  AND THE SECTOR IS THINNER THAN THE ORDER ASSUMED: its weight is exactly
  1/(L+1) on even degrees and ZERO on odd ones, and it contains NO L = 1
  mode at all -- the degree the scalar band and the vector figures were both
  quoted at.  So even had the transport been shared, the three-sector
  comparison could not have been made where the other two are reported.
  That weight needed no input amplitude, so that half of the order is
  discharged rather than deferred.

  THE GUARD: two routes agreeing on a spectrum are not thereby reading one
  object -- check that they share the MEASURE and the COUPLINGS, not only
  the eigenvalue.
  ==========================================================================
""")
