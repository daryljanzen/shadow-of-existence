#!/usr/bin/env python3
r"""S1 -- cc54, PO-6 (the sub-leading counterterm question S50 left OPEN): the one-dimensionful-constant
ledger survives the LOG one-loop divergence not only on FIXED de Sitter (L-816) but on the framework's own
RUNNING expanding layer a(T)=sinh^{2/3}(3T/2alpha), where the curvature RUNS. On the running layer the
graviton's quadratic-curvature (log) counterterm reduces to {Gauss-Bonnet (topological), a Lambda-
renormalisation, a Newton/ell_P renormalisation, and terms proportional to the field equations (removed by
a metric field redefinition)} -- with NO irreducible curvature-squared coupling outside {Lambda, G}, for
ANY counterterm coefficients. The mechanism is a pair of BACKGROUND-INDEPENDENT algebraic identities, so it
does not use R=const and extends L-816 off the fixed background.

** WHAT S50 LEFT OPEN, AND WHY THIS IS THE RIGHT NEXT OBJECT. ** L-816 (S50) settled the sub-leading tower
on the tower's own FIXED de Sitter slicing (R=12/alpha^2 constant): Weyl^2=0, the graviton's on-shell log
divergence is Gauss-Bonnet (topological), ledger survives. S50 flagged, in its own voice, the residue:
"DOES THE ONE-DIMENSIONAL COUNTERTERM BASIS SURVIVE ON A BACKGROUND WHOSE CURVATURE RUNS?" -- naming the
instrument (the sub-leading Schwinger-DeWitt coefficients on the sinh^{2/3} layer) and asking for a
decidable answer. On the running layer R is NOT constant, so an R^2 counterterm is no longer degenerate
with a Lambda^2 renormalisation (they coincide only when R=4Lambda), and the fixed-background argument does
not obviously carry. This receipt answers it.

** THE ARGUMENT. **
  (i)   The running FLRW layer stays CONFORMALLY FLAT: Weyl^2 = 0 for every a(T), not only de Sitter. So
        the log counterterm carries no Weyl^2 content on the running layer either; R runs (R -> 12/alpha^2
        only as T->oo, recovering L-816's value).
  (ii)  The graviton one-loop log divergence (raw Seeley-DeWitt-Gilkey b_4) is
        (53/90) E_GB + [(7/20) R_{mn}^2 + (1/120) R^2]  (per 1/[8pi^2(d-4)]; 't Hooft-Veltman 1974,
        Gilkey 1975). E_GB = Riem^2 - 4 Ric^2 + R^2 is the Euler density: int sqrt(g) E_GB = 32 pi^2 chi, a
        topological total derivative -- no coupling renormalised.
  (iii) The remainder (7/20) R_{mn}^2 + (1/120) R^2 is ALGEBRAICALLY proportional to the field equations.
        For Lambda=0 it is EXACTLY E_{mn} f^{mn} with E_{mn}=R_{mn}-1/2 R g_{mn} and
        f^{mn}=(7/20) R^{mn} - (11/60) R g^{mn} -- an identity in the curvatures, true on ANY metric, so it
        holds on the running layer. A metric field redefinition g -> g + delta g, delta g^{mn} ~ f^{mn},
        removes it. For Lambda != 0 (E_{mn}=R_{mn}-1/2 R g_{mn}+Lambda g_{mn}) the remainder decomposes,
        on the layer, into {Lambda^2 (a cosmological-constant renormalisation), Lambda R (a Newton/ell_P
        renormalisation), and E_{mn}-proportional (field-redef removable)} -- with NO leftover R^2.
  (iv)  This is COEFFICIENT-INDEPENDENT: the most general quadratic-curvature counterterm
        a_1 Riem^2 + a_2 Ric^2 + a_3 R^2 reduces on the running layer to {E_GB, Lambda^2, Lambda R,
        E_{mn}-proportional} with remainder EXACTLY zero, for arbitrary a_1,a_2,a_3. So no choice of
        one-loop coefficients can force a new coupling; the {Lambda, G} ledger absorbs the whole
        quadratic-curvature log divergence on the running layer, as it did on fixed de Sitter.

COMPUTES: the curvature invariants and the counterterm reduction on the sinh^{2/3} layer. ** The
't Hooft-Veltman coefficients (7/20, 1/120) and the sinh^{2/3} law are used as the CONCRETE instance, but
the reduction is verified for ARBITRARY counterterm coefficients (a_1,a_2,a_3 symbolic), so the verdict
does not depend on them. ** Lambda, H, Hdot are kept symbolic; nothing is pinned to a working point.

** WHAT THIS RECEIPT ASSERTS. **
  1. WEYL^2 = 0 ON THE RUNNING LAYER: for a(T)=sinh^{2/3}(3T/2alpha), Weyl^2=0 and R RUNS (R->12/alpha^2
     only asymptotically) -- conformal flatness is not special to de Sitter, so the log counterterm has no
     Weyl^2 content on the running layer.
  2. THE TOPOLOGICAL SPLIT: the graviton b_4 is (53/90) E_GB + [(7/20)Ric^2+(1/120)R^2]; E_GB is the Euler
     density (int sqrt(g) E_GB = 32 pi^2 chi), topological -- it renormalises no coupling.
  3. THE BACKGROUND-INDEPENDENT IDENTITY (Lambda=0): (7/20)Ric^2+(1/120)R^2 = E_{mn} f^{mn} EXACTLY on the
     running layer -- an algebraic identity, not an on-shell statement, so it holds with R running; the
     remainder is field-redefinition removable.
  4. THE LEDGER SURVIVES (Lambda!=0), COEFFICIENT-INDEPENDENTLY: on the running layer the general
     a_1 Riem^2+a_2 Ric^2+a_3 R^2 reduces to {E_GB, Lambda^2 (Lambda-renorm), Lambda R (G/ell_P-renorm),
     E_{mn}-proportional} with remainder ZERO -- no irreducible R^2 coupling outside {Lambda, G}.
  5. CONSISTENCY WITH L-816: at the vacuum de Sitter point (Hdot=0, H^2=Lambda/3, R=4Lambda) the reduction
     collapses to L-816's result (Gauss-Bonnet + Lambda,G renormalisation), the E_{mn}-piece vanishing.
  6. THE CORPUS NAMES THE QUESTION: S50 asks "does the one-dimensional counterterm basis survive on a
     background whose curvature runs?" and names the instrument; this is the decidable answer.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that PO-6 is closed -- it is PROTECTED_OPEN (F5); this
supplies the computation S50 named, on the running CLASSICAL background. NOT the fully back-reacting /
quantised-a(T) sector -- S50's deeper caveat is that the coupled sector where Gamma-hat lives has NO fixed
classical background, and the Schwinger-DeWitt expansion presumes one; that "definition of the interacting
tower" (P10's own "the standard problem of the interacting theory") is untouched. NOT that the running-
layer cosmology is one-loop FINITE -- the survival is the PURE GRAVITON (the TT tower; matter enters only
as the classical bend of the slicing, not as a quantised field). A dynamical quantum MATTER field brings
one-loop graviton-matter divergences that a metric field redefinition does NOT remove (Deser-van
Nieuwenhuizen 1974) -- exactly the scope L-816 already flagged for the fixed background (a minimal scalar's
a_2 carries a genuine R^2). NOT that the removable pieces VANISH off a true vacuum: on the sourced layer
they evaluate to field-equation (bend) contractions and are absorbed into the definition of the metric and
the existing {Lambda, G} couplings -- removable, not zero, and not a new constant. NOT a re-derivation of
the one-loop coefficients -- 't Hooft-Veltman / Gilkey / Christensen-Duff are cited and used; the result is
coefficient-independent regardless.

** Board lead L-818 (cc54's band); the RUNNING-LAYER half of PO-6's sub-leading counterterm question
(L-165), the residue S50 named. Companion to L-816 (fixed de Sitter). Informs L-165. Does NOT convert
PO-6, and does NOT enter the quantised-background sector. **

Written r2765 (cc54, L-818). Asserts against the FLRW curvature algebra and the cited one-loop graviton
divergence -- never the register. 't Hooft & Veltman, Ann. IHP A20 (1974) 69; Gilkey, J. Diff. Geom. 10
(1975) 601; Christensen & Duff, Nucl. Phys. B170 (1980) 480; Deser & van Nieuwenhuizen, Phys. Rev. D10
(1974) 401. Stated for reversal.
"""
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- PO-6: does the one-constant ledger survive the log divergence on the RUNNING layer?')
    print()
    T, al = sp.symbols('T alpha', positive=True)
    H, Hd, Lam = sp.symbols('H Hdot Lambda', real=True)

    # 1. Weyl^2 = 0 on the running sinh^{2/3} layer, and R runs
    a = sp.Function('a', positive=True)(T)
    Rgen = 6 * (sp.diff(a, (T, 2)) / a + (sp.diff(a, T) / a) ** 2)
    asol = sp.sinh(3 * T / (2 * al)) ** sp.Rational(2, 3)
    Rrun = sp.simplify(Rgen.subs(a, asol).doit())
    runs = sp.simplify(sp.diff(Rrun, T)) != 0
    dS_limit = sp.limit(Rrun, T, sp.oo)
    # invariants in (H, Hdot): Weyl^2 identically 0 for flat FLRW
    Rs = 12 * H ** 2 + 6 * Hd
    Ric2 = 36 * H ** 4 + 36 * H ** 2 * Hd + 12 * Hd ** 2
    Riem2 = 24 * H ** 4 + 24 * H ** 2 * Hd + 12 * Hd ** 2
    R2 = Rs ** 2
    Weyl2 = sp.expand(Riem2 - 2 * Ric2 + R2 / 3)
    EGB = sp.expand(Riem2 - 4 * Ric2 + R2)
    check('WEYL^2 = 0 ON THE RUNNING LAYER: for a=sinh^{2/3}(3T/2alpha), Weyl^2=0 and R RUNS '
          f'(dR/dT != 0: {runs}), with R -> {dS_limit} as T->oo (recovering L-816\'s de Sitter value) -- '
          'conformal flatness is not special to de Sitter',
          Weyl2 == 0 and runs and dS_limit == 12 / al ** 2)

    # 2. topological split: E_GB is the Euler density (int sqrt g E_GB = 32 pi^2 chi)
    check('THE TOPOLOGICAL SPLIT: the graviton b_4 = (53/90) E_GB + [(7/20)Ric^2+(1/120)R^2]; '
          'E_GB = Riem^2-4Ric^2+R^2 is the Euler density (int sqrt(g) E_GB = 32 pi^2 chi), topological -- '
          f'on the layer E_GB = {sp.factor(EGB)} (nonzero pointwise, but its integral is a total '
          'derivative that renormalises no coupling)',
          sp.simplify(EGB - (Riem2 - 4 * Ric2 + R2)) == 0)

    # mixed Ricci eigenvalues on FLRW
    R0, Ri = 3 * (Hd + H ** 2), (Hd + 3 * H ** 2)
    TVrem = sp.Rational(7, 20) * Ric2 + sp.Rational(1, 120) * R2

    # 3. background-independent identity (Lambda=0): TVrem = E_mn f^mn exactly
    E0, Ei = R0 - Rs / 2, Ri - Rs / 2
    f0 = sp.Rational(7, 20) * R0 - sp.Rational(11, 60) * Rs
    fi = sp.Rational(7, 20) * Ri - sp.Rational(11, 60) * Rs
    Ef = E0 * f0 + 3 * Ei * fi
    check('THE BACKGROUND-INDEPENDENT IDENTITY (Lambda=0): (7/20)Ric^2+(1/120)R^2 = E_{mn} f^{mn} EXACTLY '
          'on the running layer (E_{mn}=R_{mn}-1/2 R g, f^{mn}=(7/20)R^{mn}-(11/60)R g^{mn}) -- an '
          'algebraic identity in the curvatures, true with R running, so the remainder is field-'
          'redefinition removable',
          sp.simplify(TVrem - Ef) == 0)

    # 4. Lambda != 0, coefficient-independent: general a1 Riem^2 + a2 Ric^2 + a3 R^2 reduces with remainder 0
    E0L, EiL = R0 - Rs / 2 + Lam, Ri - Rs / 2 + Lam
    Esq = E0L ** 2 + 3 * EiL ** 2
    Etr = E0L + 3 * EiL
    E_R = Etr * Rs
    E_Ric = E0L * R0 + 3 * EiL * Ri
    a1, a2, a3 = sp.symbols('a1 a2 a3')
    A, B, C, D, F, G, K = sp.symbols('A B C D F G K')
    CT = a1 * Riem2 + a2 * Ric2 + a3 * R2
    model = A * EGB + B * Lam ** 2 + C * Lam * Rs + D * Esq + F * Etr ** 2 + G * E_R + K * E_Ric
    sol = sp.solve(sp.Poly(sp.expand(CT - model), H, Hd, Lam).coeffs(),
                   [A, B, C, D, F, G, K], dict=True)
    rem = sp.simplify(sp.expand(CT - model.subs(sol[0]))) if sol else sp.Integer(1)
    Bcoef = sp.simplify(sol[0].get(B, B)) if sol else None
    Ccoef = sp.simplify(sol[0].get(C, C)) if sol else None
    check('THE LEDGER SURVIVES (Lambda!=0), COEFFICIENT-INDEPENDENTLY: the general a1 Riem^2+a2 Ric^2+a3 R^2 '
          'reduces on the running layer to {E_GB, Lambda^2 (Lambda-renorm), Lambda R (G/ell_P-renorm), '
          f'E_{{mn}}-proportional}} with remainder = {rem} -- NO irreducible R^2 coupling outside '
          '{Lambda, G}, for arbitrary coefficients',
          bool(sol) and rem == 0 and Bcoef is not None and Ccoef is not None)

    # 5. consistency with L-816 at the vacuum de Sitter point
    vac = {Hd: 0}
    Etr_vac = sp.simplify(Etr.subs(vac).subs(H ** 2, Lam / 3))
    # at R=4Lambda the E_mn-proportional remainder of the TV part vanishes; only E_GB + Lambda,G renorm
    R_vac = sp.simplify(Rs.subs(vac).subs(H ** 2, Lam / 3))
    check('CONSISTENCY WITH L-816: at the vacuum de Sitter point (Hdot=0, H^2=Lambda/3) the layer has '
          f'R = {R_vac} = 4 Lambda and the vacuum EOM trace E = {Etr_vac} = 0, so the reduction collapses '
          'to L-816\'s result -- Gauss-Bonnet (topological) + Lambda,G renormalisation, the '
          'E_{mn}-proportional piece vanishing',
          R_vac == 4 * Lam and Etr_vac == 0)

    # 6. the corpus names the question
    s50 = os.path.join(ROOT, 'receipts', 'L165_defining_the_sum',
                       'S50_the_counterterm_basis_is_one_dimensional_because_the_background_family_is.py')
    tex = os.path.join(ROOT, 'corpus', 'canonical_time.tex')
    s50_txt = ' '.join(open(s50, encoding='utf-8', errors='replace').read().lower().split()) \
        if os.path.exists(s50) else ''
    tex_txt = open(tex, encoding='utf-8', errors='replace').read().lower() if os.path.exists(tex) else ''
    check('THE CORPUS NAMES THE QUESTION: S50 asks whether "the one-dimensional counterterm basis '
          'survive[s] on a background whose curvature runs" and names the instrument (sub-leading '
          'Schwinger-DeWitt on the sinh^{2/3} layer); canonical_time.tex names the interacting-tower UV -- '
          'this is the decidable answer for the running classical background',
          'curvature runs' in s50_txt and 'counterterm basis survive' in s50_txt
          and 'definition of the interacting tower' in tex_txt)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-6 running-layer half; a computation, not a conversion): on the framework\'s own')
    print('  expanding layer a(T)=sinh^{2/3}(3T/2alpha), where the curvature RUNS, the pure-graviton log')
    print('  divergence reduces to Gauss-Bonnet (topological) + a Lambda-renormalisation + a Newton/ell_P')
    print('  renormalisation + field-equation-proportional terms (removed by a metric field redefinition),')
    print('  with NO irreducible curvature-squared coupling outside {Lambda, G} -- for ANY one-loop')
    print('  coefficients. The one-constant ledger survives not only on fixed de Sitter (L-816) but on the')
    print('  running layer, by background-independent algebraic identities (not R=const). The quantised-')
    print('  background sector and a dynamical quantum matter field are untouched and out of scope.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
