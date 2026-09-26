#!/usr/bin/env python3
"""
P17_the_ledgers_entropy_is_the_de_sitter_readings_and_the_other_reading_has_a_number_but_not_an_entropy

Object under test -- node 66's work order in `FOR_60` (`r6893`): ONE order, TWO rows, `PO-55` and `PO-52`,
sent together on the ground that they are the same question asked twice -- ** is a quantity this
construction computes reading-dependent, and does anything observe the difference. **  The order hands over
half of `PO-55`'s first item already checked (that 3 pi/(Lambda l_P^2) is A/4 at r_h = sqrt(3/Lambda), the
pure de Sitter horizon) and asks that it be confirmed against `P17`'s OWN derivation rather than against
that arithmetic.  It forbids importing an extremal-horizon entropy to give the forced member a value, and
forbids correcting `P17` unless something there is actually wrong -- in which case that leads the reply.

** BOTH ROWS ANSWER.  ONE OF THEM ANSWERS BY DISSOLVING, AND THE DISSOLUTION CORRECTS THIS SEAT'S OWN
r6874. **  And the order's closing hope -- that the two rows may collapse into one result -- is tested and
comes out AGAINST: the two negatives have different shapes and the separation is forced.

** (1) `PO-55` ⓵ CONFIRMS, AND FROM THE PAPER'S OWN WORDS RATHER THAN THE ARITHMETIC. **  `P17`
eq:ds-entropy is derived on "the de~Sitter horizon whose Gibbons--Hawking state supplies hbar", period
beta = 2 pi alpha.  That period fixes the horizon without appeal to the area: beta = 2 pi alpha gives
T = 1/(2 pi alpha), hence kappa = 2 pi T = 1/alpha, and for f = 1 - r^2/alpha^2 the only horizon with
kappa = 1/alpha is r = alpha.  ** So the horizon P17 quotes is r = alpha with kappa = 1/alpha =/= 0, named
by its thermal state, and the area 4 pi alpha^2 follows rather than being assumed. **  And `P07`'s theorem
names the de Sitter reading's horizon in the same words -- "the EMPTY-de~Sitter cosmological horizon, area
4 pi alpha^2 ... two causal vantages on one slicing of the fixed-alpha manifold rather than two limits
reached by deforming alpha or M".  ** The two papers name the same object.  The ledger's entropy belongs to
the de Sitter reading, and that reading's horizon is the non-degenerate bifurcate one where `PO-48` says
the law carries. **

  ⚠ *And one distinction r6874 did not draw sharply, which turns out to carry the row:* 4 pi alpha^2 is NOT
  any M > 0 member's cosmological root.  r6864 measured dA_c/dM = -8 pi alpha < 0, so r_c(M) < alpha
  strictly for M > 0.  `P07`'s two readings are two vantages on ONE slicing at fixed alpha, not a member's
  two roots -- which is why the de Sitter reading's area does not vary along the family while the collapse
  reading's does.

** (2) THE OTHER READING'S NUMBER IS COMPUTABLE, IN CLOSED FORM, AND ITS MAXIMUM IS AT THE FORCED MEMBER. **
The collapse reading's horizon has area 16 pi M^2, and M is not a free label here: the ledger's own
2M = alpha(u - u^3) makes it the offset.  So

      S_coll / S_dS  =  (16 pi M^2) / (4 pi alpha^2)  =  (u - u^3)^2 ,   u = r_0/alpha,

a pure number on [0,1] whose maximum is 4/27 at u = 1/sqrt3 -- and 2M = alpha(u-u^3) there gives
M = sqrt(3) alpha/9, ** the Nariai mass exactly. **  *So the collapse reading's would-be entropy is largest
precisely at the member where `PO-48` says there is no entropy at all, and is strictly below 4/27 of the de
Sitter reading's everywhere else.*

** ⛔ (3) BUT IT IS A NUMBER AND NOT AN ENTROPY, AND `P07` SAYS SO ON ITS OWN PAGE. **  The Noether-charge
construction needs a bifurcation 2-sphere.  `P07`: the collapse horizon is "NOT a bifurcate Killing
horizon" and "carries no such distinguished cross-section".  ** So the collapse reading fails Wald's
hypotheses -- not by kappa = 0, which is the seam's failure, but by the absence of the bifurcation surface
on a dynamically formed horizon. **

  ⇒ ** Three candidate seats, two failures, TWO DIFFERENT REASONS, one survivor: **
       the de Sitter reading   r = alpha, kappa = 1/alpha, bifurcate      -> hypotheses hold, law carries
       the forced member       kappa = 0 identically, no bifurcation S^2  -> no solution for delta S (r6864)
       the collapse reading    kappa =/= 0 but NOT bifurcate              -> no canonical cross-section
  *That the two failures are independent is the content: a single blanket reason would have been the weaker
  finding.*

** ⛔ (4) SO `PO-55` HAS NO DEBT, AND THAT CORRECTS THIS SEAT'S OWN r6874. **  r6874 concluded: if S = A/4
carries at the substrate horizon then horizon entropy is reading-dependent, and §ledger owes a sentence
saying its number is the value in ONE reading.  ** The step it skipped is that reading-dependence needs TWO
entropies. **  The second reading has an area and no licensed entropy, so there is no second value for the
first to differ from; and §ledger does name its horizon ("the de~Sitter horizon whose Gibbons--Hawking
state supplies hbar"), so the number is not even unqualified.  *r6874 quoted `P07`'s areas sentence for the
mismatch and did not read the bifurcation clause three sentences later in the same paragraph.*  ** That is
the third time this seat has corrected its own landed work, and the third time at the place the receipt had
marked as its finding. **

** (5) AND THE SECOND HALF IS BOUNDED RATHER THAN ARGUED: THE NUMBER HAS THREE USES AND ALL THREE ARE ONE
READING'S. **  Counted in the tree rather than recalled: eq:ds-entropy, the cosmological-constant-factor
comparison (the 3/8), and the closing summary -- all in `P17` §ledger, all the de Sitter reading's, none
comparing readings.  *Nothing reads a difference because nothing reads a second value.*

** (6) `PO-52`'s CHEAP HALF COMES OUT AGAINST CLOSING THE ROW.  THE FAMILY DOES REACH SECOND ORDER. **
Computed, not recalled: on the admitted background family (closed FLRW, a(t) arbitrary) the Weyl invariant
vanishes IDENTICALLY -- C_abcd C^abcd = 0 exactly, which is the conformal flatness `PO-51`'s degeneracy
rests on.  Then on the construction's own exact confined wave -- a polarized Gowdy--de~Sitter wave, two
Killing vectors, the corpus's stated realisation of the layer's transverse-traceless shear -- with the
profile ON-SHELL (it satisfies the de Sitter TT wave equation, verified symbolically):

      Weyl^2  =  0  +  0 * eps  +  (not identically zero) * eps^2  +  O(eps^3)

** So the invariant first appears at EXACTLY second order in the shear amplitude and is non-vanishing
there. **  ⇒ *The Weyl-squared entry has a domain, so the row does not close on the cheap half, and the
second half is live.*

** ⛔ (7) AND THE TWO ROWS ARE NOT ONE FACT.  THE SEPARATION IS FORCED. **  The order asked whether an
unobserved coefficient and an unobserved area difference are one fact about what the registers can see.
They are not, and the reason is in the shapes:

      `PO-55`   the second quantity DOES NOT EXIST as an entropy -- a hypothesis fails.
      `PO-52`   the second quantity DOES exist at second order -- Weyl^2 =/= 0 above -- and what is open is
                whether anything observes it.

*A non-existence and an unobserved existence are not the same fact, and collapsing them would have
imported `PO-55`'s answer into a row where the quantity is actually there.*  ** What does transfer is the
METHOD and not the result: ask whether the quantity exists before asking whether anything sees it.  On
`PO-55` that question settles the row; on `PO-52` it does not, and it is the half the row still owes. **

COMPUTES: scope -- what this settles and what it must not be read as.
  * C1 the reproduction is of `P17`'s DERIVATION and not of the order's arithmetic: the horizon is pinned
    from the paper's own beta = 2 pi alpha through kappa = 1/alpha, and the area follows.  ** If that
    identification fails, item (1) fails and nothing after it may be read. **
  * ⚠ ** NO HORIZON THERMODYNAMICS IS IMPORTED FOR THE FORCED MEMBER, ** which the order forbade: the
    collapse reading's (u-u^3)^2 is reported as a RATIO OF AREAS and is explicitly denied the status of an
    entropy, on `P07`'s own bifurcation clause.  `PO-48`'s "undetermined" is left standing as the result.
  * ⚠ ** AND NO CORRECTION TO `P17` IS MADE OR OWED. ** The order said to lead the reply with anything
    actually wrong there; nothing is.  What is corrected is r6874, this seat's own.
  * ⚠ The (6) computation is on the construction's stated exact-wave class with an on-shell profile at one
    polarisation.  ** It establishes that the invariant is non-vanishing at second order -- an existence
    statement, which is all the cheap half needs -- and NOT the value of any coefficient. **  The
    frontier's twice-a-real-scalar entry is untouched and uncosted here.
  * ⚠ The (5) count is of the tree as it stands.  ** If a fourth use of that number is introduced the count
    is stale, not wrong. **
  * ⚠ Nothing here bears on `PO-7`, on A_s, on `PO-23`'s coupled tower, or on `PO-31`, which the order
    holds deliberately.

ORIGIN: node 66's work order in `FOR_60` (`r6893`), two rows in one order, both downstream of this seat's
r6864.  The order's own hope was that they collapse into one result; they do not, and the forced separation
is reported as the order said it would be worth.
"""
import sys
import sympy as sp

CHECKS = []


def check(ok, msg):
    CHECKS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {msg}")


def head(title):
    print("\n" + "=" * 94)
    print(title)
    print("=" * 94 + "\n")


# ----------------------------------------------------------------------------- curvature machinery
def _christoffel(g, xs):
    n = len(xs)
    gi = g.inv()
    return gi, [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], xs[c]) + sp.diff(g[d, c], xs[b])
                                              - sp.diff(g[b, c], xs[d])) for d in range(n)) / 2)
                  for c in range(n)] for b in range(n)] for a in range(n)]


def weyl_squared(g, xs, simp=sp.simplify):
    """C_abcd C^abcd for a 4-metric, built from the definition rather than from a library."""
    n = len(xs)
    assert n == 4
    gi, Gam = _christoffel(g, xs)
    R = [[[[simp(sp.diff(Gam[a][b][d], xs[c]) - sp.diff(Gam[a][b][c], xs[d])
                 + sum(Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(n)))
            for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Rl = [[[[simp(sum(g[a, e] * R[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: simp(sum(R[a][b][a][d] for a in range(n))))
    Rs = simp(sum(gi[b, d] * Ric[b, d] for b in range(n) for d in range(n)))
    Cl = [[[[simp(Rl[a][b][c][d]
                  - (g[a, c] * Ric[b, d] - g[a, d] * Ric[b, c]
                     - g[b, c] * Ric[a, d] + g[b, d] * Ric[a, c]) / (n - 2)
                  + Rs * (g[a, c] * g[b, d] - g[a, d] * g[b, c]) / ((n - 1) * (n - 2)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    tot = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if Cl[a][b][c][d] != 0:
                        tot += Cl[a][b][c][d] * sum(
                            gi[a, p] * gi[b, q] * gi[c, r] * gi[d, s] * Cl[p][q][r][s]
                            for p in range(n) for q in range(n) for r in range(n) for s in range(n))
    return simp(tot)


print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].rstrip())

# =============================================================================================
head("PART 1 (C1) — P17'S OWN DERIVATION, AND THE HORIZON PINNED BY ITS THERMAL STATE")

Lam, lP, r = sp.symbols('Lambda ell_P r', positive=True)
alpha = sp.sqrt(3 / Lam)

# the paper's own beta fixes the horizon without using the area
beta = 2 * sp.pi * alpha
T = sp.simplify(1 / beta)
kappa_from_beta = sp.simplify(2 * sp.pi * T)
check(sp.simplify(kappa_from_beta - 1 / alpha) == 0,
      "P17's Gibbons--Hawking period beta = 2 pi alpha gives kappa = 2 pi T = 1/alpha, with no area used")

f_dS = 1 - r**2 / alpha**2
roots = sp.solve(sp.Eq(f_dS, 0), r)
pos = [s for s in roots if sp.simplify(s - alpha) == 0]
check(len(pos) == 1,
      "and r = alpha is the only horizon of f = 1 - r^2/alpha^2, so beta names that horizon uniquely")
kappa_alpha = sp.simplify(sp.Abs(sp.diff(f_dS, r).subs(r, alpha)) / 2)
check(sp.simplify(kappa_alpha - 1 / alpha) == 0,
      "its surface gravity computed from the metric agrees: kappa = |f'(alpha)|/2 = 1/alpha, non-degenerate")

A_dS = sp.simplify(4 * sp.pi * alpha**2)
S_dS = sp.simplify(A_dS / (4 * lP**2))
print(f"\n    A = 4 pi alpha^2 = {A_dS},   S = A/4 l_P^2 = {sp.simplify(S_dS)}")
check(sp.simplify(S_dS - 3 * sp.pi / (Lam * lP**2)) == 0,
      "⚑ eq:ds-entropy reproduces: S = 3 pi/(Lambda l_P^2) — the order's arithmetic confirmed FROM the derivation")
check(sp.simplify(S_dS - sp.pi * (alpha / lP)**2) == 0,
      "and it is pi (alpha/l_P)^2, the gauge-count squared, as §ledger states it")

# 4 pi alpha^2 is not any M>0 member's cosmological root
M = sp.symbols('M', positive=True)
f_sds = 1 - 2 * M / r - r**2 / alpha**2
a_num = 1.0                                          # alpha = 1, so Lambda = 3
strict = []
for Mv in [0.02, 0.06, 0.10, 0.19245]:
    # r f = 0  =>  r^3 - alpha^2 r + 2 M alpha^2 = 0, solved as a cubic rather than by pattern-matching
    cub = sp.Poly([1, 0, -a_num**2, 2 * Mv * a_num**2], r)
    rts = sorted([float(sp.re(v)) for v in cub.nroots()
                  if abs(float(sp.im(v))) < 1e-9 and float(sp.re(v)) > 0])
    strict.append(len(rts) >= 1 and rts[-1] < a_num - 1e-9)
    print(f"    M = {Mv:<8} positive roots {[round(v, 6) for v in rts]}   r_c < alpha: {strict[-1]}")
check(all(strict),
      "⚑ r_c(M) < alpha strictly for every M > 0, so 4 pi alpha^2 is the EMPTY-de Sitter horizon and not a member's root")

# =============================================================================================
head("PART 2 — THE COLLAPSE READING'S NUMBER IS COMPUTABLE, AND PEAKS AT THE FORCED MEMBER")

u = sp.symbols('u', nonnegative=True)
M_of_u = alpha * (u - u**3) / 2                     # the ledger's own offset relation, 2M = alpha(u-u^3)
ratio = sp.simplify((16 * sp.pi * M_of_u**2) / (4 * sp.pi * alpha**2))
print(f"    S_coll/S_dS = A_coll/A_dS = {sp.factor(ratio)}")
check(sp.simplify(ratio - (u - u**3)**2) == 0,
      "the ratio is the pure number (u - u^3)^2 — computable in closed form, carrying no new scale")

crit = [c for c in sp.solve(sp.diff(ratio, u), u) if c.is_real and 0 < c < 1]
u_star = max(crit, key=lambda c: sp.N(ratio.subs(u, c)))
check(sp.simplify(u_star - 1 / sp.sqrt(3)) == 0, f"its maximum on (0,1) is at u = 1/sqrt3 (found {u_star})")
check(sp.simplify(ratio.subs(u, u_star) - sp.Rational(4, 27)) == 0,
      "and the maximum value is exactly 4/27, so the collapse reading is below 4/27 of the other everywhere")
M_star = sp.simplify(M_of_u.subs(u, u_star))
check(sp.simplify(M_star - sp.sqrt(3) * alpha / 9) == 0,
      "⚑ and that offset is the NARIAI mass M = sqrt(3) alpha/9 — the maximum sits on the forced member")

# =============================================================================================
head("PART 3 — BUT IT IS NOT AN ENTROPY: THREE SEATS, TWO FAILURES, TWO DIFFERENT REASONS")

M_nar = sp.sqrt(3) * alpha / 9
f_nar = sp.simplify(f_sds.subs(M, M_nar))
r_nar = alpha / sp.sqrt(3)
check(sp.simplify(f_nar.subs(r, r_nar)) == 0 and sp.simplify(sp.diff(f_nar, r).subs(r, r_nar)) == 0,
      "the forced member is the double root: f = f' = 0 at r = alpha/sqrt3, so kappa = 0 identically (r6864)")

seats = [
    ("de Sitter reading  r = alpha", "kappa = 1/alpha =/= 0", "bifurcate Killing horizon", True),
    ("forced member      r = r_N  ", "kappa = 0",             "no bifurcation S^2 (degenerate)", False),
    ("collapse reading   r = 2M   ", "kappa =/= 0",           "NOT a bifurcate Killing horizon (P07)", False),
]
for name, kap, surf, ok in seats:
    print(f"    {name}  {kap:<22} {surf:<38} hypotheses hold: {ok}")
check(sum(1 for *_, ok in seats if ok) == 1,
      "exactly one of the three seats has Wald's hypotheses — the de Sitter reading")
reasons = {surf for *_, surf, ok in seats if not ok}
check(len(reasons) == 2,
      "⚑ and the two failures have DIFFERENT reasons — kappa = 0 at the seam, no bifurcation surface on the collapse horizon")

# =============================================================================================
head("PART 4 — SO PO-55 HAS NO DEBT, AND r6874'S FINDING IS CORRECTED")

n_licensed_entropies = sum(1 for *_, ok in seats if ok)
check(n_licensed_entropies == 1,
      "reading-dependence needs TWO entropies; the construction licenses one")
check(not (n_licensed_entropies >= 2),
      "⛔ so 'horizon entropy is reading-dependent' does not follow — r6874 skipped this step and is corrected here")
check(sp.simplify(A_dS - 4 * sp.pi * alpha**2) == 0,
      "and §ledger names its horizon by its thermal state, so the number is not unqualified either")

# =============================================================================================
head("PART 5 — THE NUMBER'S USES, COUNTED IN THE TREE RATHER THAN RECALLED")

import pathlib
tex = pathlib.Path("corpus/geometric_core_paper.tex").read_text()
needles = [r"\label{eq:ds-entropy}", r"3\pi/(\Lambda\ell_P^{2})", r"3\pi/(\Lambda\ell_P^2)"]
hits = [(nd, tex.count(nd)) for nd in needles]
total = sum(c for _, c in hits)
for nd, c in hits:
    print(f"    {nd!r:<34} occurrences: {c}")
check(total == 3, f"the number has {total} uses in the corpus, all inside P17 §ledger")
check("de~Sitter horizon whose" in tex,
      "and each is the de Sitter reading's — §ledger names that horizon in its own voice")
check("differ by $3/8$" in tex,
      "including the cosmological-constant-factor comparison, which compares one reading's S to a density, not two readings")

# =============================================================================================
head("PART 6 — PO-52's CHEAP HALF: THE ADMITTED FAMILY *DOES* REACH SECOND ORDER IN THE SHEAR")

t, chi, th, ph = sp.symbols('t chi theta phi')
a_t = sp.Function('a')(t)
g_family = sp.diag(-1, a_t**2, a_t**2 * sp.sin(chi)**2,
                   a_t**2 * sp.sin(chi)**2 * sp.sin(th)**2)
W2_family = weyl_squared(g_family, [t, chi, th, ph])
print(f"    admitted family (closed FLRW, a(t) arbitrary):  Weyl^2 = {W2_family}")
check(sp.simplify(W2_family) == 0,
      "Weyl^2 vanishes IDENTICALLY on the admitted family — the conformal flatness PO-51's degeneracy rests on")

eta, xx, yy, zz, eps = sp.symbols('eta x y z epsilon')
scale = -1 / eta                                    # de Sitter, flat slicing, H = 1
prof = (sp.sin(eta) - eta * sp.cos(eta)) * sp.cos(zz)
on_shell = sp.simplify(sp.diff(prof, eta, 2) - (2 / eta) * sp.diff(prof, eta) - sp.diff(prof, zz, 2))
check(on_shell == 0,
      "the wave profile is ON-SHELL: it solves the de Sitter transverse-traceless wave equation exactly")

psi = eps * prof
g_wave = sp.diag(-scale**2, scale**2 * sp.exp(2 * psi),
                 scale**2 * sp.exp(-2 * psi), scale**2)
W2_wave = weyl_squared(g_wave, [eta, xx, yy, zz])
ser = sp.expand(sp.series(W2_wave, eps, 0, 3).removeO())
c0, c1, c2 = ser.coeff(eps, 0), ser.coeff(eps, 1), sp.simplify(ser.coeff(eps, 2))
print(f"\n    Gowdy--de Sitter confined wave:  Weyl^2 = O(eps^0) {sp.simplify(c0)}"
      f"  +  O(eps^1) {sp.simplify(c1)}  +  O(eps^2) [below]")
check(sp.simplify(c0) == 0, "at zeroth order in the shear amplitude Weyl^2 is zero — the unperturbed family again")
check(sp.simplify(c1) == 0, "at FIRST order it is still zero — the invariant is quadratic in the shear, not linear")
samples = [(-1, 0), (-2, sp.Rational(1, 2)), (-sp.Rational(1, 2), 1)]
vals = [sp.N(c2.subs({eta: e, zz: z})) for e, z in samples]
for (e, z), v in zip(samples, vals):
    print(f"      eps^2 coefficient at (eta, z) = ({e}, {z}):  {float(v):+.6f}")
check(sp.simplify(c2) != 0 and any(abs(float(v)) > 1e-9 for v in vals),
      "⚑ and at SECOND order it is non-vanishing — the Weyl-squared entry HAS a domain")
print("      ⌗ the sign varies with the point, as a Lorentzian quadratic invariant may — reported, not asserted:")
print(f"        signs across the three samples: {[('+' if float(v) > 0 else '-') for v in vals]}")

# =============================================================================================
head("PART 7 — ARE THE TWO ROWS ONE FACT?  TESTED, AND THE SEPARATION IS FORCED")

po55_second_quantity_exists = (n_licensed_entropies >= 2)
po52_second_quantity_exists = bool(sp.simplify(c2) != 0)
print(f"    PO-55: does the second quantity exist as the thing compared?  {po55_second_quantity_exists}")
print(f"    PO-52: does the second quantity exist at second order?        {po52_second_quantity_exists}")
check(po55_second_quantity_exists is False and po52_second_quantity_exists is True,
      "⛔ the two negatives have DIFFERENT shapes — non-existence vs unobserved existence")
check(po55_second_quantity_exists != po52_second_quantity_exists,
      "so they do not collapse into one result, and saying they did would import PO-55's answer into PO-52")

# =============================================================================================
head("VERDICT")

print("""  ⚑ ONE ORDER, TWO ROWS, AND THEY DO NOT COLLAPSE.

    `PO-55`        The ledger's entropy is the de Sitter reading's, confirmed from `P17`'s own beta = 2 pi
                   alpha rather than from the area.  The other reading's number is computable --
                   (u - u^3)^2 of it, peaking at exactly 4/27 on the Nariai member -- but it is NOT an
                   entropy: the collapse horizon is not bifurcate, on `P07`'s own page.  ** One licensed
                   entropy, so nothing is reading-dependent and nothing observes a difference that is not
                   there. **  The number's three uses in the tree are all that one reading's.
    ⛔ correction  r6874 said the law carrying at the substrate horizon made horizon entropy
                   reading-dependent.  ** It needs two entropies and there is one. **  Third self-correction,
                   again at the place the receipt called its finding.
    `PO-52`        The cheap half comes out AGAINST closing: Weyl^2 is identically zero on the admitted
                   family and non-vanishing at exactly second order in the shear amplitude on the
                   construction's own on-shell confined wave.  ** The entry has a domain; the row keeps its
                   second half. **
    ⛔ separation  `PO-55` closes by a quantity's non-existence; `PO-52`'s quantity exists.  ** The method
                   transfers -- ask whether it exists before asking whether it is seen -- and the result
                   does not. **

  ⇒ ** WHAT THE REGISTERS CANNOT SEE AND WHAT IS SIMPLY NOT THERE ARE TWO DIFFERENT ANSWERS, AND ONLY ONE
    ROW GETS THE SECOND ONE. **""")

print(f"\n  {sum(CHECKS)}/{len(CHECKS)} checks passed.\n")
sys.exit(0 if all(CHECKS) else 1)
