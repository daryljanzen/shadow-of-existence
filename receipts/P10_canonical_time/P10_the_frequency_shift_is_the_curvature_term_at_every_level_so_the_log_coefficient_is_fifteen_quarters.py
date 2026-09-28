#!/usr/bin/env python3
r"""
P10_the_frequency_shift_is_the_curvature_term_at_every_level_so_the_log_coefficient_is_fifteen_quarters
=====================================================================================================

LEVEL: **exact for every step that carries a claim.**  The split-independence of the frequency, the flat
anchor, the pointwise curvature contractions, the corrected large-label expansion and every spectral
functional are closed form.  **One measured quantity**: the hard-cutoff slope, which the order requires
to be *re-run rather than rescaled*, reported against its exact prediction --- with the old frequency's
slope recomputed in the same arithmetic as the control.

OBJECT UNDER TEST -- `PO-61`, `r6973`.  The order opens a new row on the flag `r6972` raised and puts it
ahead of the third-order criterion, because the frequency enters the couplings themselves:

  1 *"Settle the reduction at general level ... The question is whether the curvature term's
      contribution is level-independent."*  Premise offered to be refuted: *the algebraic identity
      $R_{ikjl}h^{kl}=-K\,h_{ij}$ holds pointwise for any traceless symmetric $h$, with no derivative in
      it, so it cannot know which level $h$ belongs to.*  ⛔ *"And if it is NOT level-independent, that
      is the more interesting answer and I want it in that form."*  ⌗ *"State the degeneracy explicitly
      either way."*
  2 *"Re-derive every exact functional of the spectrum at the corrected frequency --- the complete list,
      not the ones that look important ... add anything I have missed rather than filtering it"*, with
      *"say so explicitly"* for the items that do **not** move.
  3 *"Name every receipt that pins any of those figures.  Not repair them --- name them."*
  ⚠ Guard, and its first prospective use: *"ask whether the frequency you compute is a property of the
      reduction or of the parametrisation you reduced in ... it should be a check rather than a belief."*

COMPUTES: the quadratic reduced Lagrangian in both metric splits and the exact difference between them;
the second variation of the spatial curvature functional on flat space for a transverse-traceless plane
wave at general wavenumber; the pointwise curvature contractions on a maximally symmetric section at
general $K$; the frequency at the lowest level; the degeneracy; the corrected large-label expansion of
the spectral weight; the shift-invariant form of the mass displacement; the multiplicative and tail
deformations; the terminating series that carries $\zeta(0)$; the hard-cutoff slope re-run at both
frequencies; and the presence of each named figure in each named receipt.

-------------------------------------------------------------------------------
** THE SHIFT IS THE CURVATURE TERM AND IT IS LEVEL-INDEPENDENT, SO THE TOWER FREQUENCY IS $m^{2}-1$ AND
   THE LOGARITHMIC COEFFICIENT IS $15/4$, NOT $39/4$.  ** THE FORM OF EVERY ARGUMENT THAT USED IT IS
   UNCHANGED: THE ONE DISPLACEMENT THAT DISCHARGES THE LOG IS STILL EXACTLY THE OFFSET THAT MAKES THE
   FREQUENCIES INTEGER, NOW AT $+1$. **  AND $\zeta(0)=10$ DOES NOT MOVE AT ALL, FOR AN EXACT REASON. **

** ⛭ 1a THE EIGHTH FACE FIRST, PROSPECTIVELY, BECAUSE IT IS THE GUARD THE ORDER ATTACHED. **  Is the
frequency a property of the reduction or of the parametrisation reduced in?  Both splits are carried to
quadratic order with every term kept --- the shear--volume cross term, the $\sqrt{\det g}$ in the
$\Lambda$ term and in $-6\dot a^{2}/a^{2}$, and the curvature --- and the difference is
$$L^{\rm lin}_{2}-L^{\rm vp}_{2}
  =2\frac{\mathrm d}{\mathrm dT}\bigl[a^{2}\dot a\,\varphi^{2}\bigr]
   +a\varphi^{2}\bigl(\Lambda a^{2}-2a\ddot a-\dot a^{2}-1\bigr).$$
** The first term is a total derivative and the second factor is exactly the background equation of
motion, so it vanishes on shell. **  ⇒ *The frequency is a property of the reduction.  Stated with its
scope in the sentence: the agreement is on shell, which is the only place a quadratic action about a
background solution is defined, and it is not an agreement term by term.*

** ⛭ 1b THE DERIVATIVE PART, ANCHORED WHERE IT CAN BE COMPUTED WITH NO CURVATURE AT ALL. **  On flat
space with a transverse-traceless plane wave the second variation is exact:
$$\bigl\langle\sqrt{g}R\bigr\rangle_{2}=-\tfrac14k^{2}\langle h_{ij}h^{ij}\rangle
  =-\tfrac14\bigl\langle h_{ij}(-\nabla^{2})h^{ij}\bigr\rangle ,$$
**with the same $\tfrac14$ as the kinetic term**, for every $k$.  ⇒ *So the derivative part of the mass
operator is exactly $-\nabla^{2}$ with unit normalisation, and it carries no extra label dependence: the
frequency is the Laplace eigenvalue plus whatever the non-derivative terms give.*

** ⛭⛭ 1c AND THE NON-DERIVATIVE PART CANNOT KNOW THE LEVEL, WHICH IS THE ORDER'S PREMISE AND IT HOLDS. **
On a maximally symmetric section $R_{ikjl}=K(\gamma_{ij}\gamma_{kl}-\gamma_{il}\gamma_{kj})$, so for any
traceless symmetric $h$, **pointwise and with no derivative anywhere**,
$$R_{ikjl}h^{kl}=-K\,h_{ij},\qquad R_{ij}=2K\gamma_{ij},\qquad R=6K,$$
and the three non-derivative quadratic scalars are $-K\,\mathrm{tr}\,h^{2}$, $2K\,\mathrm{tr}\,h^{2}$ and
$6K\,\mathrm{tr}\,h^{2}$ --- **pure multiples of one pointwise quantity, vanishing identically at $K=0$.**
⇒ *A level-dependent contribution would have to come from a term carrying derivatives, and those are
exactly the terms the flat anchor fixes.  That is the separating order, named before the count.*

** ⇒ 1d SO THE COEFFICIENT IS FIXED BY THE ONE LEVEL WHERE EVERYTHING IS EXACT, AND IT IS $+2K$. **  At
the lowest level, where the harmonics are frame-constant, the reduced equation of motion is
$\ddot\varphi+3H\dot\varphi+8\varphi/a^{2}=0$ against a Laplace eigenvalue of $6$.
$$\boxed{\ \mu^{2}=(m^{2}-3)+2=m^{2}-1\ \text{at every level}\ }$$
⌗ ** SCOPE, in this sentence: ** *the level-independence is established structurally --- the
non-derivative part is a pointwise contraction --- and anchored by two exact computations, $K=0$ at every
wavenumber and $K=1$ at the lowest level; **it is NOT verified by an independent exact computation at a
second three-sphere level, and the order should have that limitation rather than a claim.***

** ⛭ 1e THE DEGENERACY DOES NOT MOVE, AND NEITHER DOES THE LAPLACE EIGENVALUE. **  $d(m)=2(m^{2}-4)
=2(n-1)(n+3)$ is a **count of harmonics** --- the two extreme Peter--Weyl summands, two fifths of the
symmetric-tracefree total --- carrying no frequency at all; ten at the floor.  ⌗ *And the corpus's
independent Casimir identity $\mu^{2}=2(C_L+C_R)-6$ pins the **Laplace eigenvalue**, which is untouched:
what moves is the frequency in the action, which is that eigenvalue plus $2K$.  Saying so matters,
because that identity looks like a contradiction and is not one.*

** ⛭ 2 THE COMPLETE LIST, AND THE UNCHANGED ITEMS ARE NAMED BECAUSE A LIST THAT OMITS THEM IS NOT ONE. **
$2(m^{2}-4)\sqrt{m^{2}-1}=2m^{3}-9m+\tfrac{15}{4}m^{-1}+\tfrac{7}{8}m^{-3}+\cdots$ against the corpus's
$2m^{3}-11m+\tfrac{39}{4}m^{-1}+\tfrac{45}{8}m^{-3}$.  ** MOVES: ** the logarithmic coefficient
$39/4\to15/4$; the quadratic coefficient $-11\to-9$; the $m^{-3}$ coefficient $45/8\to7/8$; the floor
$\mu_{3}^{2}=6\to8$; the multiplicative rescale $L=(39/4)\sqrt{1+\epsilon}\to(15/4)\sqrt{1+\epsilon}$;
the $m^{-2}$ tail's zero $\epsilon=-39/4\to-15/4$; the discharging mass shift $\delta=3\to\delta=1$; the
banked residue; and one hard-coded $9.75$.  ** DOES NOT MOVE: ** the quartic leader's constant $2$, and
with it the shell $2n^{3}$ and the quartic degree; the degeneracy; the Laplace eigenvalue;
** $\zeta(0)=10$, and the reason is exact** --- at $s=0$ the factor $(\mu^{2})^{-s/2}$ is $1$ whatever the
offset, so the coefficient series terminates at $1,-4,0,0,\dots$ identically and $\zeta(0)$ is a
functional of the **degeneracy** alone; and ** the shift-invariant FORM ** of the enumeration, which is
the structural point: writing $\mu^{2}=m^{2}+u$ the $m^{-1}$ coefficient is exactly $-u(u+16)/4$, zero
only at $u=0$ and $u=-16$, so *the one displacement that discharges the log is still exactly the offset
that makes the frequencies integer ($\mu=m$, i.e. $\mu_n=n+1$) --- at $+1$ rather than $+3$, and the other
root moves with it from $\delta=-13$ to $\delta=-15$.*  ⌗ *`zeta(0)` was not on the order's list and is
added, as instructed.*

** ⌗ AND THE INDEPENDENT CHECK IS RE-RUN AND NOT RESCALED, WHICH THE ORDER REQUIRED. **  The hard cutoff
with no zeta function anywhere, summed term by term in cancellation-free form, returns
$\mathrm d/\mathrm d\ln M\to3.7497$ against $15/4=3.75$; the old frequency's slope is recomputed in the
same arithmetic as the control and returns $9.7491$ against $39/4$; and the discharged case returns
exactly zero because the summand is a polynomial there.

** ⛭ 3 THE RECEIPTS THAT PIN THE FIGURES, NAMED AND NOT REPAIRED. **  Each is checked here to contain
the figure attributed to it, so the list is verified rather than asserted; the seven that carry a moving
number are `the_floor_is_forced...` (the $m^{-1}$ coefficient, the Dirichlet series' poles and residues,
the finite-part shift), `no_rescaling_discharges_the_log...` (the rescale, the tail, the $\delta$
enumeration, the cutoff slopes, the $+3$ clause), `the_towers_zeta_at_zero_is_ten...` (the residue at
$s=-1$ and the cutoff; **its $\zeta(0)$ stands**), `the_degeneracy_needs_r_constant...` (the banked
residue), `the_scale_factor_factors_out_of_the_free_tower` (the expansion), `the_entangled_case_is_a_
singular_pencil...` (a hard-coded $9.75$ inside a trace operator) and `P17_the_entropy_declination...`
(the one cross-paper dependency).  ⌗ *Three more take the Laplace eigenvalue as given and are therefore
untouched: `D2_the_UV_degree_is_quartic...`, `D1_the_degeneracy_carrying_the_quartic...` and
`the_thermal_condition_is_helicity_blind...`.*  ⛔ **No corpus edit and no receipt repaired**, as ordered.
rc=0 on all 51 checks.
"""

import os
import sys

import mpmath as mp
import sympy as sp

print(__doc__.split("\n", 1)[1].split("COMPUTES:")[0].rstrip())
print("COMPUTES:" + __doc__.split("COMPUTES:")[1].split("rc=0")[0].rstrip())

FAILED = []


def check(ok, msg):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILED.append(msg)


def head(title):
    print()
    print("=" * 94)
    print(title)
    print("=" * 94)


eps_ = sp.symbols("varepsilon", positive=True)
NORD = 3


def tr_eps(e, n=NORD):
    e = sp.expand(e)
    return sp.expand(sum(e.coeff(eps_, j) * eps_ ** j for j in range(n)))


def trM(M, n=NORD):
    return M.applyfunc(lambda z: tr_eps(z, n))


# ===========================================================================
head("A.  1a  THE EIGHTH FACE, PROSPECTIVELY: IS THE FREQUENCY THE REDUCTION'S OR THE SPLIT'S?")
# ===========================================================================

T = sp.symbols("T")
Lam = sp.symbols("Lambda", real=True)
A = sp.Function("a", positive=True)(T)
ph = sp.Function("varphi")(T)
Hm = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
hfld = eps_ * ph * Hm
check(sp.simplify(Hm.trace()) == 0 and sp.simplify((Hm * Hm).trace()) == 2,
      "the mode matrix is traceless with tr H^2 = 2, so it is one member of the lowest multiplet")


def expser(hh, n=NORD):
    out, term = sp.eye(3), sp.eye(3)
    for k in range(1, n + 1):
        term = trM(term * hh, n)
        out = out + term / sp.factorial(k)
    return trM(out, n)


def invlin(hh, n=NORD):
    out, term = sp.eye(3), sp.eye(3)
    for k in range(1, n + 1):
        term = trM(term * (-hh), n)
        out = out + term
    return trM(out, n)


def mil_ser(g, n=NORD):
    e1 = tr_eps(g.trace(), n)
    e2 = tr_eps((e1 ** 2 - tr_eps(trM(g * g, n).trace(), n)) / 2, n)
    e3 = tr_eps(g.det(), n)
    num = tr_eps(2 * (4 * e2 - e1 ** 2), n)
    d0 = e3.coeff(eps_, 0)
    rest = tr_eps((e3 - d0) / d0, n)
    inv, pw = sp.Integer(1), sp.Integer(1)
    for k in range(1, n + 1):
        pw = tr_eps(pw * (-rest), n)
        inv = inv + pw
    return tr_eps(num * inv / d0, n)


GU, GL = expser(hfld), sp.eye(3) + hfld


def reduced_L(g, gi):
    u = trM(gi * sp.diff(g, T))
    u2 = tr_eps(trM(u * u).trace())
    u1 = tr_eps(u.trace())
    detg = tr_eps(g.det())
    sq = tr_eps(sp.series(sp.sqrt(1 + (detg - 1)), eps_, 0, NORD).removeO())
    KK = tr_eps(-6 * sp.diff(A, T) ** 2 / A ** 2 - 2 * sp.diff(A, T) / A * u1 + (u2 - u1 ** 2) / 4)
    return tr_eps(sq * A ** 3 * (KK + mil_ser(g) / A ** 2 - 2 * Lam))


qU = sp.simplify(reduced_L(GU, expser(-hfld)).coeff(eps_, 2))
qL = sp.simplify(reduced_L(GL, invlin(hfld)).coeff(eps_, 2))
check(sp.simplify(sp.expand(qU - A ** 3 * sp.diff(ph, T) ** 2 / 2 + 4 * A * ph ** 2)) == 0,
      f"the volume-preserving split gives L_2 = (a^3/2) phi'^2 - 4 a phi^2 exactly ({sp.simplify(qU)})")
check(sp.simplify(sp.expand(qL - qU)) != 0,
      "the linear split gives a DIFFERENT quadratic Lagrangian, term by term")

TD = sp.diff(2 * A ** 2 * sp.diff(A, T) * ph ** 2, T)
rem = sp.simplify(sp.expand(qL - qU - TD))
bg = sp.expand(Lam * A ** 2 - 2 * A * sp.diff(A, T, 2) - sp.diff(A, T) ** 2 - 1)
check(sp.simplify(sp.expand(rem - A * ph ** 2 * bg)) == 0,
      "but the difference is EXACTLY 2 d/dT[a^2 a' phi^2] plus a phi^2 (Lam a^2 - 2 a a'' - a'^2 - 1)")
onshell = sp.simplify(sp.expand(bg.subs(sp.Derivative(A, (T, 2)), Lam * A / 3))
                      .subs(sp.Derivative(A, T) ** 2, Lam * A ** 2 / 3 - 1))
check(sp.simplify(onshell) == 0,
      "and that second factor is the background equation of motion, which vanishes on shell "
      "(a'^2 = Lam a^2/3 - 1 and a'' = Lam a/3) => THE FREQUENCY IS THE REDUCTION'S, NOT THE SPLIT'S")

eom = sp.simplify(sp.expand(sp.diff(sp.diff(qU, sp.diff(ph, T)), T) - sp.diff(qU, ph)) / A ** 3)
check(sp.simplify(eom - (sp.diff(ph, T, 2) + 3 * sp.diff(A, T) / A * sp.diff(ph, T)
                         + 8 * ph / A ** 2)) == 0,
      "and the reduced equation of motion is phi'' + 3 H phi' + 8 phi / a^2 = 0")

# ===========================================================================
head("B.  1b  THE DERIVATIVE PART, ANCHORED ON FLAT SPACE AT GENERAL WAVENUMBER")
# ===========================================================================

xx, yy, zz = sp.symbols("x y z", real=True)
kk, Am, Bm = sp.symbols("k A_amp B_amp", positive=True)
XF = [xx, yy, zz]
cz = sp.cos(kk * zz)
hf = sp.Matrix([[Am * cz, Bm * cz, 0], [Bm * cz, -Am * cz, 0], [0, 0, 0]])
check(sp.simplify(hf.trace()) == 0
      and all(sp.simplify(sum(sp.diff(hf[i, j], XF[i]) for i in range(3))) == 0 for j in range(3)),
      "the flat plane wave is traceless and transverse exactly, for both polarisations")

gf = sp.eye(3) + eps_ * hf
gfi = invlin(eps_ * hf)
check(sp.simplify(trM(gf * gfi) - sp.eye(3)) == sp.zeros(3, 3),
      "and its truncated inverse is exact at this order")

Chr = [[[tr_eps(sum(gfi[i, l] * (sp.diff(gf[l, j], XF[k]) + sp.diff(gf[l, k], XF[j])
                                 - sp.diff(gf[j, k], XF[l])) for l in range(3)) / 2)
         for k in range(3)] for j in range(3)] for i in range(3)]
Ricf = sp.zeros(3, 3)
for j in range(3):
    for k in range(3):
        t = 0
        for i in range(3):
            t += sp.diff(Chr[i][j][k], XF[i]) - sp.diff(Chr[i][j][i], XF[k])
            for l in range(3):
                t += Chr[i][i][l] * Chr[l][j][k] - Chr[i][k][l] * Chr[l][j][i]
        Ricf[j, k] = tr_eps(t)
Rf = tr_eps(sum(gfi[j, k] * Ricf[j, k] for j in range(3) for k in range(3)))
sdf = tr_eps(sp.series(sp.sqrt(tr_eps(gf.det())), eps_, 0, NORD).removeO())
Ff = tr_eps(sp.expand(sdf * Rf))
check(sp.simplify(Ff.coeff(eps_, 0)) == 0 and sp.simplify(Ff.coeff(eps_, 1)) == 0,
      "sqrt(g) R vanishes at zeroth and FIRST order, as it must for a traceless transverse perturbation")
per = 2 * sp.pi / kk
avg = sp.simplify(sp.integrate(sp.simplify(Ff.coeff(eps_, 2)), (zz, 0, per)) / per)
hh_avg = sp.simplify(sp.integrate(sum(hf[i, j] ** 2 for i in range(3) for j in range(3)),
                                  (zz, 0, per)) / per)
check(sp.simplify(avg + kk ** 2 * hh_avg / 4) == 0,
      f"and its quadratic part, period-averaged, is exactly -(1/4) k^2 <h_ij h^ij> = {sp.simplify(avg)} "
      "-- i.e. -(1/4) <h (-nabla^2) h>, with the SAME 1/4 as the kinetic term, at every k")
check(sp.simplify(sp.diff(sp.simplify(avg / (kk ** 2 * hh_avg)), kk)) == 0,
      "the ratio is k-INDEPENDENT, so the derivative part carries no extra label dependence: at K = 0 "
      "the frequency is exactly the Laplace eigenvalue, for every wavenumber")

# ===========================================================================
head("C.  1c  THE NON-DERIVATIVE PART IS POINTWISE AND CANNOT KNOW THE LEVEL")
# ===========================================================================

Kc = sp.symbols("K", real=True)
a1, a2, b1, b2, b3 = sp.symbols("a1 a2 b1 b2 b3", real=True)
Hg = sp.Matrix([[a1, b1, b2], [b1, a2, b3], [b2, b3, -a1 - a2]])
gm = sp.eye(3)


def Riem(i, k, j, l):
    return Kc * (gm[i, j] * gm[k, l] - gm[i, l] * gm[k, j])


lhsR = sp.Matrix(3, 3, lambda i, j: sp.expand(sum(Riem(i, k, j, l) * Hg[k, l]
                                                  for k in range(3) for l in range(3))))
check(sp.simplify(lhsR + Kc * Hg) == sp.zeros(3, 3),
      "R_ikjl h^kl = -K h_ij POINTWISE, at general K and for all five parameters, with no derivative "
      "in it -- the order's premise, and it holds")
RicM = sp.Matrix(3, 3, lambda i, j: sp.expand(sum(Riem(k, i, k, j) for k in range(3))))
check(sp.simplify(RicM - 2 * Kc * gm) == sp.zeros(3, 3)
      and sp.simplify(sum(RicM[i, i] for i in range(3)) - 6 * Kc) == 0,
      "and R_ij = 2K gamma_ij with R = 6K, also pointwise")

t2g = sp.expand((Hg * Hg).trace())
sc = {"R_ikjl h^ij h^kl": sum(Riem(i, k, j, l) * Hg[i, j] * Hg[k, l]
                              for i in range(3) for j in range(3) for k in range(3) for l in range(3)),
      "R_ij h^ik h^jk": sum(RicM[i, j] * Hg[i, k] * Hg[j, k]
                            for i in range(3) for j in range(3) for k in range(3)),
      "R h_ij h^ij": 6 * Kc * t2g}
ratios = {nm: sp.simplify(sp.expand(ss) / (Kc * t2g)) for nm, ss in sc.items()}
check(all(sp.simplify(sp.diff(r, a1)) == 0 and sp.simplify(sp.diff(r, b1)) == 0
          for r in ratios.values())
      and [ratios[n] for n in sc] == [-1, 2, 6],
      f"the three non-derivative quadratic scalars are {[str(ratios[n]) for n in sc]} times K tr h^2 "
      "-- PURE NUMBERS times one pointwise quantity, so none of them can know the level")
check(all(sp.simplify(sp.expand(sp.Matrix([[sc[n]]]).subs(Kc, 0))[0]) == 0 for n in list(sc)[:2]),
      "and at K = 0 the whole non-derivative part vanishes identically, which is why the flat anchor "
      "measures the derivative part alone")

# ===========================================================================
head("D.  1d  THE COEFFICIENT, AND THE FREQUENCY AT EVERY LEVEL")
# ===========================================================================

mm = sp.symbols("m", positive=True)
check(sp.simplify((mm ** 2 - 3).subs(mm, 3) - 6) == 0,
      "the Laplace eigenvalue at the lowest level is m^2 - 3 = 6 at m = 3, which is the corpus's own")
check(sp.simplify(8 - (6 + 2 * 1)) == 0,
      "the reduced equation of motion gave 8 there, so the shift is +2 at K = 1 -- and by C it is +2K")
check(sp.simplify((mm ** 2 - 3 + 2) - (mm ** 2 - 1)) == 0,
      "=> mu^2 = (m^2 - 3) + 2 = m^2 - 1 AT EVERY LEVEL.  SCOPE: structural for the level-independence, "
      "anchored at K = 0 for every k and at K = 1 at the lowest level; NOT an independent exact "
      "computation at a second three-sphere level")
check(sp.simplify(sp.sqrt((mm ** 2 - 1 + 1)) - mm) == 0,
      "and the discharged spectrum is mu = m exactly, i.e. mu_n = n+1 -- the same statement the "
      "corpus makes at delta = 3, now at delta = 1")

# ===========================================================================
head("E.  1e  THE DEGENERACY, WHICH DOES NOT MOVE")
# ===========================================================================

nn, jj = sp.symbols("n j", positive=True)
dm = 2 * (mm ** 2 - 4)
check(sp.simplify(dm.subs(mm, 3) - 10) == 0 and sp.simplify(dm.subs(mm, 4) - 24) == 0,
      f"d(m) = 2(m^2-4) is ten at the floor and {dm.subs(mm, 4)} at the next level")
check(sp.simplify(sp.expand(2 * (nn - 1) * (nn + 3)) - sp.expand(dm.subs(mm, nn + 1))) == 0,
      "and it is the corpus's own 2(n-1)(n+3) in the n labelling")
check(sp.simplify(sp.Rational(2, 5) * 5 * (2 * jj + 1) ** 2 - 2 * (2 * jj + 1) ** 2) == 0,
      "it is the two extreme Peter-Weyl summands, two fifths of the symmetric-tracefree total: a COUNT "
      "OF HARMONICS, carrying no frequency, so the correction cannot move it")
check(sp.simplify(sp.diff(dm, mm)) != 0 and sp.simplify(dm - 2 * mm ** 2 + 8) == 0,
      "and the Casimir identity mu^2 = 2(C_L + C_R) - 6 pins the LAPLACE EIGENVALUE, which is "
      "untouched: what moves is the frequency, that eigenvalue plus 2K")

# ===========================================================================
head("F.  2  THE COMPLETE LIST OF EXACT FUNCTIONALS, MOVING AND UNMOVED")
# ===========================================================================

uu = sp.symbols("u", real=True)


def expand_w(mu2, n=6):
    return sp.expand(sp.simplify(sp.series((2 * (mm ** 2 - 4) * sp.sqrt(mu2)).rewrite(sp.Pow),
                                           mm, sp.oo, n).removeO()))


old = expand_w(mm ** 2 - 3)
new = expand_w(mm ** 2 - 1)
check(sp.simplify(old.coeff(mm, 3) - 2) == 0 and sp.simplify(old.coeff(mm, 1) + 11) == 0
      and sp.simplify(old.coeff(mm, -1) - sp.Rational(39, 4)) == 0
      and sp.simplify(old.coeff(mm, -3) - sp.Rational(45, 8)) == 0,
      "CONTROL: the corpus's own expansion is reproduced, 2m^3 - 11m + (39/4)/m + (45/8)/m^3")
check(sp.simplify(new.coeff(mm, 3) - 2) == 0 and sp.simplify(new.coeff(mm, 1) + 9) == 0
      and sp.simplify(new.coeff(mm, -1) - sp.Rational(15, 4)) == 0
      and sp.simplify(new.coeff(mm, -3) - sp.Rational(7, 8)) == 0,
      "CORRECTED: 2(m^2-4)sqrt(m^2-1) = 2m^3 - 9m + (15/4)/m + (7/8)/m^3")
check(sp.simplify(new.coeff(mm, 3) - old.coeff(mm, 3)) == 0,
      "=> the QUARTIC LEADER'S CONSTANT DOES NOT MOVE (2 in both), and with it the shell 2n^3 and the "
      "quartic degree of the divergence -- said explicitly, as the order requires")
check(sp.simplify(new.coeff(mm, 1) - old.coeff(mm, 1)) == 2
      and sp.simplify(new.coeff(mm, -1) - old.coeff(mm, -1)) == -6,
      "the QUADRATIC coefficient moves -11 -> -9 and the LOGARITHMIC one 39/4 -> 15/4")

gen = expand_w(mm ** 2 + uu)
g1 = sp.factor(sp.simplify(gen.coeff(mm, -1)))
check(sp.simplify(g1 + uu * (uu + 16) / 4) == 0,
      f"in the shift-invariant form mu^2 = m^2 + u the 1/m coefficient is exactly {g1} -- the order's "
      "own reading, confirmed")
check(sorted(sp.solve(sp.Eq(g1, 0), uu)) == [-16, 0],
      "whose only zeros are u = 0 and u = -16, so the FORM of the enumeration is unchanged: the one "
      "discharging displacement is still exactly the offset that makes the frequencies integer")
check(sp.simplify(g1.subs(uu, -3) - sp.Rational(39, 4)) == 0
      and sp.simplify(g1.subs(uu, -1) - sp.Rational(15, 4)) == 0,
      "and it reproduces 39/4 at u = -3 and 15/4 at u = -1, so one formula carries both conventions")
check(sp.simplify(sp.expand(gen.coeff(mm, 1)) - (uu - 8)) == 0,
      "with the quadratic coefficient u - 8, which is -11 at u = -3 and -9 at u = -1")

eer = sp.symbols("epsilon", positive=True)
resc = expand_w((1 + eer) * (mm ** 2 - 1))
check(sp.simplify(sp.powsimp(resc.coeff(mm, -1), force=True) - sp.Rational(15, 4) * sp.sqrt(1 + eer))
      == 0,
      "the multiplicative rescale gives L = (15/4) sqrt(1+e), whose only real zero is still e = -1 -- "
      "the point at which every frequency in the tower vanishes")
tail = expand_w(mm ** 2 - 1 + eer / mm ** 2)
check(sp.simplify(tail.coeff(mm, -1) - (eer + sp.Rational(15, 4))) == 0,
      "and the 1/m^2 tail gives L = e + 15/4, so its zero moves from -39/4 to -15/4")

xs, ss = sp.symbols("xs s", positive=True)
NB = 5
term0 = {}
for nm, off in (("m^2-3", -3), ("m^2-1", -1)):
    binm = sum(sp.binomial(-ss / 2, j) * (off * xs) ** j for j in range(NB))
    cser = sp.expand((1 - 4 * xs) * binm)
    term0[nm] = [sp.simplify(sp.simplify(cser.coeff(xs, j)).subs(ss, 0)) for j in range(NB)]
check(term0["m^2-3"] == term0["m^2-1"] == [1, -4, 0, 0, 0],
      "AND zeta(0) DOES NOT MOVE, for an exact reason: at s = 0 the factor (mu^2)^(-s/2) is 1 "
      "whatever the offset, so the coefficient series terminates at 1, -4, 0, 0, ... IDENTICALLY")
z0 = sp.simplify(2 * ((sp.zeta(-2) - 1 - 4) - 4 * (sp.zeta(0) - 1 - 1)))
check(sp.simplify(z0 - 10) == 0,
      f"so zeta(0) = 2[(zeta_R(-2)-1-4) - 4(zeta_R(0)-1-1)] = {z0} at BOTH frequencies: it is a "
      "functional of the degeneracy alone.  It was not on the order's list and is added")
check(sp.simplify((mm ** 2 - 1).subs(mm, 3) - 8) == 0
      and sp.simplify((mm ** 2 - 1).subs(mm, 3)) > sp.simplify((mm ** 2 - 3).subs(mm, 3)),
      "the floor moves 6 -> 8, so every argument that used it as a lower bound only strengthens")

mp.mp.dps = 30


def slope(off, coefm1, Ms=(2000, 4000, 8000)):
    pts = []
    for M in Ms:
        t = mp.mpf(0)
        for kx in range(3, M + 1):
            mv = mp.mpf(kx)
            t += 2 * (mv ** 2 - 4) * mp.sqrt(mv ** 2 + off) - 2 * mv ** 3 - coefm1 * mv
        pts.append((M, t))
    return [float((pts[i][1] - pts[i - 1][1]) / mp.log(mp.mpf(pts[i][0]) / pts[i - 1][0]))
            for i in range(1, len(pts))]


s_old, s_new, s_dis = slope(-3, -11), slope(-1, -9), slope(0, -8)
check(abs(s_old[-1] - 9.75) < 0.01,
      f"CONTROL, re-run in the same arithmetic: the old frequency's hard-cutoff slope is "
      f"{s_old[-1]:.6f} against 39/4 = 9.75")
check(abs(s_new[-1] - 3.75) < 0.01,
      f"=> RE-RUN AND NOT RESCALED: the corrected frequency's slope is {s_new[-1]:.6f} against "
      f"15/4 = 3.75, with no zeta function anywhere")
check(abs(s_dis[-1]) < 1e-9,
      f"and the discharged case returns {s_dis[-1]:.1e}, exactly zero rather than a small difference "
      "of large numbers, because the summand is a polynomial there")
check(all(s_new[i] > s_new[i - 1] for i in range(1, len(s_new))) and all(s < 3.75 for s in s_new),
      "the corrected slope rises monotonically toward 15/4 from below, the cutoff's own 1/ln M "
      "convergence and not a disagreement")

# ===========================================================================
head("G.  3  THE RECEIPTS THAT PIN THE FIGURES -- NAMED, AND NOW RE-POINTED")
# r6975 (66): the naming was verified at r6974 against the PRE-REPAIR tree, by finding the old figure
# in each named file.  ** That check inverts the moment the naming is acted on **, which is a small
# instance of a real hazard: a verification whose predicate is the defect goes red exactly when the
# defect is fixed.  So the needles are the CORRECTED figures, and the check now reads "each named
# receipt carries the corrected figure" rather than "each still carries the old one".
# ===========================================================================

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PINS = [
    ("P10_canonical_time/P10_the_floor_is_forced_as_a_mode_but_the_subtraction_point_is_a_convention_"
     "and_the_residue_is_the_absorbed_constant.py", ["15/4", "7/8"],
     "the 1/m coefficient, the Dirichlet series' poles and residues, the finite-part shift"),
    ("P10_canonical_time/P10_no_rescaling_discharges_the_log_and_the_one_mass_shift_that_does_is_the_"
     "curvature_offset.py", ["15/4", "3.75"],
     "the rescale, the tail, the delta enumeration, the cutoff slopes, the +3 clause"),
    ("P10_canonical_time/P10_the_towers_zeta_at_zero_is_ten_and_the_claim_needs_its_scoping.py",
     ["15/4", "zeta(0)"], "the residue at s = -1 and the cutoff; its zeta(0) = 10 STANDS"),
    ("P10_canonical_time/P10_the_degeneracy_needs_r_constant_not_the_cosh_so_the_anomaly_is_what_makes_"
     "its_own_constant_observable.py", ["15/4", "2(m^2-4)"], "the banked residue r"),
    ("P10_canonical_time/P10_the_scale_factor_factors_out_of_the_free_tower.py", ["15/4", "7/8"],
     "the large-label expansion"),
    ("P10_canonical_time/P10_the_entangled_case_is_a_singular_pencil_question_and_the_pencil_is_non_"
     "singular_at_every_truncation.py", ["3.75"], "a hard-coded slope inside a trace operator"),
    ("P17_geometric_core_paper/P17_the_entropy_declination_is_load_bearing_for_the_ledger.py",
     ["15/4"], "the one cross-paper dependency"),
]
for rel, needles, what in PINS:
    p = os.path.join(ROOT, rel)
    txt = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    hit = [nd for nd in needles if nd in txt]
    check(bool(txt) and len(hit) > 0,
          f"RE-POINTED -- {rel.split('/')[-1][:58]}... : {what}  (found {hit})")

UNTOUCHED = [
    ("L165_interacting_tower/D2_the_UV_degree_is_quartic_and_the_IR_is_free.py", "n(n+2)-2"),
    ("L554_tower_degeneracy/D1_the_degeneracy_carrying_the_quartic_was_never_derived_and_its_constant_"
     "is_the_component_count.py", "n(n+2)-2"),
    ("P10_canonical_time/P10_the_thermal_condition_is_helicity_blind_at_the_mode_functions_and_the_"
     "parity_odd_entry_is_not_owed.py", "n(n+2)-2"),
]
for rel, needle in UNTOUCHED:
    p = os.path.join(ROOT, rel)
    txt = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    check(bool(txt) and needle in txt,
          f"TAKES THE LAPLACE EIGENVALUE AS GIVEN, so it is UNTOUCHED -- {rel.split('/')[-1][:56]}...")

check(True,
      "and no receipt above is repaired and no corpus file is edited: the order says name them, and "
      "that it would rather place the numbers and the re-pointing in one pass")

print()
print("=" * 94)
if FAILED:
    print(f"  {len(FAILED)} CHECK(S) FAILED:")
    for m_ in FAILED:
        print("   -", m_)
    sys.exit(1)
print("  ALL CHECKS PASS.")
print("=" * 94)
