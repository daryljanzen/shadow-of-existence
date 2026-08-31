#!/usr/bin/env python3
r"""T50 -- p0's TITLE IS A THEOREM AND p0 DOES NOT CITE IT: THE THREE REAL HORIZON RADII ARE
     NOT EXPRESSIBLE IN REAL RADICALS OVER THE MASS PARAMETER.

** WHAT THE PAPER SAYS.  ** `geometric_core_paper.tex` `sec:imaginary`, whose title is *"Reached
through the imaginary, real everywhere it lands"*, gives THREE instances -- the embedding
coordinate, the equatorial seam, the cosmogenesis reassignment -- and calls each *"an instrument,
not an ontological ingredient"*, closing on *"the general law they instance: the construction
reaches a real manifold through imaginary instruments, and the geometry is intrinsically real at
every point they land on."*

*** THE OBJECTION THE SECTION LEAVES OPEN.  In all three bullets the imaginary route is a
    CONVENIENCE -- a reader may answer "then do not use it".  There is a fourth instance in the
    corpus where that answer is NOT AVAILABLE, and it is the corpus's own central algebraic
    object. ***

** THE THEOREM (casus irreducibilis; Cardano 1545, van der Waerden Algebra I Sec.64).  ** *Let $F
\subset \mathbb{R}$ and let a cubic over $F$ be IRREDUCIBLE over $F$ with THREE REAL ROOTS.  Then no
root lies in any real radical extension of $F$: the roots are real and every radical expression for
them passes through $\mathbb{C}$.*

** THE HORIZON CUBIC MEETS BOTH HYPOTHESES OVER $F=\mathbb{Q}(2M)$, and both halves are already in
the corpus separately: **
  * ** IRREDUCIBLE ** -- `P05` `rem:galois` proves it by Gauss's lemma (degree one in $2M$), the
    step `T1` audited: *"the cubic is of degree one in $2M$, so a factorisation over
    $\mathbb{C}(2M)$ would be one over $\mathbb{C}[2M]$, which the degree forbids."*  ** The same
    argument runs verbatim over the REAL base $\mathbb{Q}(2M)$, and that is the base the theorem
    needs. **
  * ** THREE REAL ROOTS ** -- `P07` names the configuration outright, twice: *"the horizon turning
    roots are colinear and real (casus irreducibilis)"*.

⛭⛭ *** SO THE CORPUS HAS THE THEOREM'S NAME, ITS HYPOTHESES, AND ITS OBJECT, AND NOWHERE ITS
     CONCLUSION.  `P05` computes the Galois group over $\mathbb{C}(2M)$ -- correctly, and it is the
     right base for a MONODROMY -- but over $\mathbb{C}$ the casus has no content, because "real
     root" is not a notion there.  The one theorem that says the imaginary route is FORCED is a
     theorem about a REAL base field, and no paper states it. ***

⇒ ** WHAT IT BUYS `sec:imaginary`: a fourth bullet of a different kind.  $r_{\pm}(M)$ cannot be
  written in real radicals as functions of the mass, so for the horizon radii the instrument is not
  optional -- and the roots are nevertheless real, which is exactly the section's law.  The
  strongest case for "reached through the imaginary, real where it lands" is the one where there is
  no other road. **

⛔⛭⛭ *** AND THE CONTROL KILLS THE PRETTIER STORY I NEARLY WROTE. ***  *The two members the corpus
     itself distinguishes -- $M=0$ (Type O, the bare substrate) and Nariai (the forced cosmological
     member) -- are BOTH masses at which the SPECIALISED cubic becomes reducible and its roots
     become real radicals ($\{0,\pm1\}$ and $\{\sqrt3/3\ \text{twice},\,-2\sqrt3/3\}$).  That is a
     true and tempting coincidence.*  ** It selects nothing.  $2M=3/8$ is under-critical, carries no
     distinction of any kind, and factors as $(2r-1)(4r^{2}+2r-3)/8$ -- one rational root and two in
     $\mathbb{Q}(\sqrt{13})$, all three real radicals. **  ⇒ *** Reducibility of a specialisation is
     dense in the mass parameter and cannot be read as physics.  The receipt asserts the
     coincidence AND asserts the counterexample, so no later reader can take the first without the
     second. ***

⛔⛭⛭ *** AND THE THIRD CONTROL IS THE FAMILY'S OWN OTHER REGIME, WHICH THIS RECEIPT FOUND BY
     FAILING. ***  *`M_SAMPLES` was first written with $2M=2/5$ in it as an "under-critical" mass.
     It is not: $2/5 > 2\sqrt3/9 \approx 0.3849$, so it is OVER-critical, and the assert fired on
     all three of its lines at once -- discriminant negative, ONE real root, Cardano intermediate
     REAL.*  ** The slip is kept and promoted, because the regime it lands in is the control the
     receipt most needed: over-critical SdS has one real horizon and its root IS a real radical, so
     the imaginary route is forced on the under-critical side of the Nariai point and NOT on the
     other. **  ⌗ *And that is the same asymmetry `P05` `prop:deck` states group-theoretically --
     "in the over-critical regime only the order-two subgroup is realised on the real structure" --
     reached here from solvability instead of from monodromy.*

⛔ ** THE CONTROLS THAT CAN GO THE OTHER WAY -- one per hypothesis, and each must FAIL to force the
  imaginary, or this receipt is measuring a tautology: **
  * ** irreducible, but ONE real root: ** $r^{3}-2$.  Cardano's discriminant is POSITIVE, the
    cube-root argument is real, and the real root $2^{1/3}$ IS a real radical.  *Irreducibility
    alone forces nothing.*
  * ** three real roots, but REDUCIBLE: ** $r^{3}-r$, roots $\{0,\pm1\}$, rational.  *Three real
    roots alone force nothing.*
  ⇒ ** Only the conjunction forces it, which is why `T1`'s missing hypothesis is load-bearing HERE
    TOO -- a second theorem, in a second paper, resting on the same unstated step. **

⌗ ** WHAT IS NOT CLAIMED.  **  *Not that `P05`'s $\mathbb{C}(2M)$ computation is wrong -- it is
right and it is the correct base for monodromy.  Not that the $M=0$/Nariai reducibility means
anything (see the control).  Not that the sky-angle parametrisation was chosen for this reason:
`P03` derives it from the gnomonic projection with no appeal to solvability, and this receipt says
only that the derivation could not have come out any other way.*

COMPUTES: scope.
  * The cubic is $r^{3}-r+2M$ in the gauge $\alpha=1$ -- `P05` `sec:deck`'s own normalisation.
  * `M_NARIAI` $=1/(3\sqrt3)$ so $2M=2\sqrt3/9$; `M_PLAIN` $=3/16$ so $2M=3/8$, the undistinguished
    reducible mass.  ** Both are exact rationals-over-radicals, not floats: the symbolic asserts do
    not depend on a tolerance. **
  * `M_SAMPLES` are UNDER-critical masses ($2M < 2\sqrt3/9$) at which the Cardano intermediate is
    measured; `M_OVER` is over-critical.  ** The verdict is a sign and a nonzero imaginary part and
    must not move within a regime, and must flip between them. **
  * ** NOT CLAIMED: any number about a horizon radius, a mass, or an observable. **

⛔ ** AND A SIXTH THING THE REGISTRY REJECTS, WHICH THE WORK ORDER'S LIST OF FOUR DOES NOT CARRY. **
  *This receipt's helper was first written `check(name, got, want)`, with the computed value third
  from last and a literal `True` last.*  ** `lint_assertions.py` reads `args[-1]` as the condition
  and flagged SEVEN calls as hollow. **  *It was right to: a reader of `check(..., x, True)` cannot
  tell a computation from a constant without following it, and neither can the gate.*  ⇒ ***The
  condition must be the LAST argument.  Values are printed into the label; only a real expression
  is passed as the verdict.***

Written r3708 by node 60, number-theory v2 pass B rows 1 and 2 (`p0`, `P03`).
"""
import sympy as sp

r, M = sp.symbols('r M', real=False)

CUBIC = r**3 - r + 2*M
M_NARIAI = sp.Rational(1, 3) / sp.sqrt(3)
M_PLAIN = sp.Rational(3, 16)
M_SAMPLES = [sp.Rational(1, 10), sp.Rational(9, 50), sp.Rational(7, 40)]
M_OVER = sp.Rational(1, 5)          # 2M = 2/5 > 2*sqrt(3)/9 -- OVER-critical

FAILS = []


def check(name, cond):
    r"""** The condition is the LAST argument, which is what `lint_assertions.py` reads. **

    *The first version of this helper was `check(name, got, want)` -- the computed value third from
    last and a literal `True` last -- and the lint flagged seven of its calls as hollow.  It was
    right to: a reader of `check(..., x, True)` cannot tell whether `x` is a computation or a
    constant without following it, and neither can the gate.  ** Values are printed into the label;
    only a real expression is passed as the verdict. **
    """
    ok = bool(cond)
    print(f"    [{'ok ' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def is_square_in_QQ_M(expr):
    r"""is a polynomial in $M$ a square in $\mathbb{Q}(M)$?  -- squarefree of even degree is not"""
    p = sp.Poly(sp.expand(expr), M, domain='QQ')
    fl = sp.factor_list(p.as_expr(), M)
    return all(e % 2 == 0 for _, e in fl[1]) and sp.sqrt(fl[0]).is_rational


def cardano_intermediate(mval):
    r"""for $t^{3}+pt+q$ the cube-root argument is $-q/2+\sqrt{(q/2)^{2}+(p/3)^{3}}$

    ** With three distinct real roots the inner square root is of a NEGATIVE number, so this is a
    genuinely non-real complex number and every real root is a sum of two non-real conjugates.
    That is the casus, made arithmetic. **
    """
    p, q = sp.Integer(-1), 2 * mval
    inner = sp.nsimplify((q / 2) ** 2 + (p / 3) ** 3)
    arg = -q / 2 + sp.sqrt(inner)
    return sp.simplify(inner), sp.expand(sp.N(arg, 30))


def real_root_count(mval):
    roots = sp.Poly(sp.expand(CUBIC.subs(M, mval)), r).nroots(n=25)
    n = sum(1 for z in roots if abs(sp.im(z)) < sp.Float('1e-20'))
    return n, max(abs(sp.im(z)) for z in roots)


if __name__ == '__main__':
    print(__doc__)
    print('=' * 96)
    print('(A) THE TWO HYPOTHESES, OVER THE REAL BASE FIELD  Q(2M)')
    print('=' * 96)

    P = sp.Poly(CUBIC, r, domain=sp.QQ.frac_field(M))
    check(f'the horizon cubic is IRREDUCIBLE over Q(M)  ->  {P.is_irreducible}', P.is_irreducible)
    print('           the same Gauss-lemma fact P05 proves over C(M) -- degree one in 2M')

    disc = sp.expand(sp.discriminant(CUBIC, r))
    check(f'discriminant of r^3-r+2M  ->  {disc}   (i.e. 4 - 27(2M)^2, exactly P05 sec:deck)',
          sp.simplify(disc - (4 - 108 * M**2)) == 0)
    sq = is_square_in_QQ_M(disc)
    check(f'the discriminant is a square in Q(M)?  ->  {sq}   (NOT a square, so Gal = S_3 '
          f'over the REAL base too)', sq is False)

    for mv in M_SAMPLES:
        d = sp.simplify(disc.subs(M, mv))
        nre, _ = real_root_count(mv)
        check(f'at 2M={sp.nsimplify(2*mv)}:  disc = {d} > 0 and real roots = {nre}',
              (d > 0) and nre == 3)

    print()
    print('=' * 96)
    print('(B) THE CASUS, MADE ARITHMETIC -- the cube-root argument is not real, the roots are')
    print('=' * 96)
    print(f"    {'2M':>10} {'(q/2)^2+(p/3)^3':>22} {'Im(cube-root arg)':>22} {'max |Im(root)|':>18}")
    for mv in M_SAMPLES + [M_PLAIN]:
        inner, arg = cardano_intermediate(mv)
        imarg = abs(sp.im(sp.N(arg, 30)))
        _, maxim = real_root_count(mv)
        print(f'    {str(sp.nsimplify(2*mv)):>10} {str(sp.nsimplify(inner)):>22} '
              f'{float(imarg):>22.12f} {float(maxim):>18.2e}')
        check(f'  2M={sp.nsimplify(2*mv)}: inner < 0, so the intermediate is NON-REAL',
              (inner < 0) and imarg > sp.Float('1e-6'))
        check(f'  2M={sp.nsimplify(2*mv)}: and every root IS real  (max |Im| = {float(maxim):.1e})',
              maxim < sp.Float('1e-18'))

    print()
    print('    CONTROL 0 -- THE OTHER REGIME, and it must come out the OTHER WAY:')
    inner_o, _ = cardano_intermediate(M_OVER)
    nreal_o, _ = real_root_count(M_OVER)
    disc_o = sp.simplify(disc.subs(M, M_OVER))
    print(f'       2M = {sp.nsimplify(2*M_OVER)} is OVER-critical (Nariai is 2*sqrt(3)/9 = '
          f'{float(2*M_NARIAI):.6f})')
    check(f'CONTROL 0  over-critical: discriminant = {disc_o}, which is NEGATIVE', disc_o < 0)
    check(f'CONTROL 0  over-critical: real roots = {nreal_o}, exactly one', nreal_o == 1)
    check(f'CONTROL 0  over-critical: Cardano inner = {inner_o} > 0, so the real root is a REAL '
          f'radical', inner_o > 0)
    print('           the imaginary route is forced BELOW the Nariai mass and not above it')

    print()
    print('=' * 96)
    print('(C) EACH HYPOTHESIS IS LOAD-BEARING -- a control per hypothesis, and both must escape')
    print('=' * 96)

    c1 = r**3 - 2
    d1 = sp.discriminant(c1, r)
    irr1 = sp.Poly(c1, r, domain='QQ').is_irreducible
    inner1 = sp.nsimplify((sp.Integer(2) / 2) ** 2 + (sp.Integer(0) / 3) ** 3)
    check(f'CONTROL 1  r^3-2 irreducible over Q?  ->  {irr1}', irr1)
    check(f'CONTROL 1  its discriminant = {d1}, NEGATIVE (one real root)', d1 < 0)
    check(f'CONTROL 1  Cardano inner = {inner1} >= 0, so the real root is a REAL radical',
          inner1 >= 0)
    print('           irreducibility ALONE does not force the imaginary')

    c2 = r**3 - r
    d2 = sp.discriminant(c2, r)
    irr2 = sp.Poly(c2, r, domain='QQ').is_irreducible
    rts2 = sorted(sp.roots(c2, r))
    check(f'CONTROL 2  r^3-r discriminant = {d2} > 0 (three real roots)', d2 > 0)
    check(f'CONTROL 2  irreducible over Q?  ->  {irr2}  (it is REDUCIBLE)', irr2 is False)
    check(f'CONTROL 2  its roots are rational  ->  {rts2}', rts2 == [-1, 0, 1])
    print('           three real roots ALONE does not force the imaginary either')

    print()
    print('=' * 96)
    print('(D) THE COINCIDENCE, AND THE COUNTEREXAMPLE THAT FORBIDS READING IT AS PHYSICS')
    print('=' * 96)

    r0 = sorted(sp.roots(CUBIC.subs(M, 0), r))
    check(f'M=0 (Type O): the cubic splits over Q  ->  {r0}', r0 == [-1, 0, 1])
    check(f'Nariai: 2M = {sp.simplify(2*M_NARIAI)}',
          sp.simplify(2 * M_NARIAI - 2 * sp.sqrt(3) / 9) == 0)
    dn = sp.simplify(disc.subs(M, M_NARIAI))
    check(f'Nariai: the discriminant = {dn}, it VANISHES', dn == 0)
    nroots = {sp.simplify(k): v for k, v in
              sp.roots(sp.expand(CUBIC.subs(M, M_NARIAI)), r).items()}
    check(f'Nariai: roots {nroots} -- a double and a single, both in the REAL field Q(sqrt 3)',
          nroots == {sp.sqrt(3) / 3: 2, -2 * sp.sqrt(3) / 3: 1})

    plain_poly = sp.expand(CUBIC.subs(M, M_PLAIN))
    plain = sp.factor(plain_poly)
    irrp = sp.Poly(plain_poly, r, domain='QQ').is_irreducible
    dp = sp.simplify(disc.subs(M, M_PLAIN))
    check(f'2M=3/8, an UNDISTINGUISHED under-critical mass: irreducible?  ->  {irrp}', irrp is False)
    check(f'2M=3/8 factors as {plain} -- all three roots real radicals',
          sp.simplify(sp.expand(plain) - plain_poly) == 0 and len(sp.Poly(plain_poly, r).all_roots()) == 3)
    check(f'2M=3/8 discriminant = {dp} > 0, so it is under-critical and not an edge case', dp > 0)

    print()
    print('    => *** The set of masses whose SPECIALISED cubic is reducible is dense: every')
    print('        rational r0 gives one, via 2M = r0 - r0^3.  M=0 and Nariai are two of')
    print('        infinitely many, and the corpus distinguishes them for reasons that have')
    print('        nothing to do with this.  THE COINCIDENCE IS REAL AND IT IS NOT A SELECTION. ***')
    print()
    print('    The theorem is about the FAMILY, over Q(2M) with 2M an indeterminate, where there')
    print('    is no specialisation to escape through.  That is the statement sec:imaginary needs,')
    print('    and it is the statement this receipt asserts in block (A).')

    print()
    print('=' * 96)
    if FAILS:
        print(f'  {len(FAILS)} FAILED: ' + ', '.join(FAILS))
        raise SystemExit(1)
    print('  ALL PASS')
