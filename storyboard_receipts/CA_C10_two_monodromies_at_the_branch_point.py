#!/usr/bin/env python3
"""RECEIPT — complex-analysis bake `C10`: ** THE BRANCH POINT r=0 CARRIES TWO DIFFERENT MONODROMIES,
AND THEY ARE ONLY SEPARABLE ACROSS PAPERS: THE BACKGROUND'S Z_3 CUBE-ROOT (P08, P15, = this ledger's
own s4a cover) AND THE PERTURBATIONS' UNIPOTENT FUCHSIAN MONODROMY (P16, C9). SAME POINT, DIFFERENT
OBJECTS. **

LEVEL: NO RATE -- monodromy groups and a branch order.

WHY THIS PROBE.  Reading P08, P10, P15 and P16 for reach (r3506) put four statements about the SAME
  point r=0 in one view, and they are about two different things:
    - P08: "the whole branch structure of r sits in u^{2/3}: one circuit multiplies r by e^{4 pi i/3},
      a primitive cube root of unity ... a Z_3 monodromy" (rcpt P08_the_branch_point_monodromy_is_Z3).
    - P15: r(tau) = A sinh^{2/3}(b tau) is "one analytic function ... the branch point at tau=0 ...
      where the curve leaves the real plane onto a conjugate branch at constant phase 2 pi/3".
    - P10: "near the branch point |r| ~ s^{2/3}, so the integrand grows only as s^{-2/3}" and the
      action integral converges.
    - P16: the PERTURBATION modes around the same point have a UNIPOTENT monodromy, indicial (0,1)
      (C9, rcpt P16_the_scalar_monodromy_is_four_pi_over_rho).

WHAT THE FIELD SAYS, AND IT IS ONLY VISIBLE ACROSS THE PAPERS.
  (1) The BACKGROUND monodromy is the CUBE-ROOT branch of the scale factor: r ~ (b tau)^{2/3}, branch
      order 3, one circuit multiplies r by e^{4 pi i/3}, DIAGONALISABLE of ORDER 3 -- the group Z_3.
      This is the SAME cube-root cover w^3=z this ledger worked at s4a (deck Z_3, monodromy S_3), now
      recognised in the cosmology's own scale factor.  P08's "e^{4 pi i/3}" and P15's "phase 2 pi/3"
      are the two determinations of one cube root: e^{4 pi i/3} = conjugate of e^{2 pi i/3}.
  (2) P10's integrability is the SAME 2/3 exponent: |r| ~ s^{2/3} makes the integrand s^{-2/3}, and
      -2/3 > -1 so it converges.  The cube root that gives the Z_3 monodromy is what makes the
      Euclidean action finite.
  (3) The PERTURBATION monodromy is UNIPOTENT (C9): (M-I)^2 = 0, INFINITE order.  A finite-order
      diagonalisable Z_3 and an infinite-order unipotent are DIFFERENT monodromies at one point --
      one acts on the background areal radius, the other on the mode pair.

WHAT IS NOT CLAIMED.  The Z_3 (P08) and the unipotent off-diagonals (P16) are each already receipted;
  this probe claims only the CUBE-ROOT identification of the background branch, the s^{-2/3}
  integrability as that same exponent, and the DISTINCTNESS of the two monodromies.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  C10 — two monodromies at r=0: background Z_3 cube-root vs perturbation unipotent")
print("=" * 78)

tau, b, A, s = sp.symbols('tau b A s', positive=True)

# (1) background: r = A sinh(b tau)^(2/3) -> cube-root branch, one circuit multiplies r by e^{4 pi i/3}
lead = sp.series(sp.sinh(b * tau), tau, 0, 2).removeO()
exponent = sp.Rational(2, 3)
assert sp.simplify(lead - b * tau) == 0, "sinh(b tau) ~ b tau near 0"
assert sp.denom(exponent) == 3, "2/3 power -> cube-root branch, order 3"
circuit = sp.exp(2 * sp.I * sp.pi * exponent)           # tau -> tau e^{2 pi i}
assert sp.simplify(circuit - sp.exp(sp.Rational(4, 3) * sp.I * sp.pi)) == 0, "e^{4 pi i/3}"
neg_branch = sp.exp(sp.I * sp.pi)**exponent             # (-1)^{2/3} principal = phase 2 pi/3
assert sp.simplify(neg_branch - sp.exp(2 * sp.I * sp.pi / 3)) == 0
sheets = {sp.simplify(circuit**k) for k in range(1, 4)}
assert len(sheets) == 3, "three sheets -> Z_3"
print(f"\n  (1) r ~ A(b tau)^(2/3): branch order {sp.denom(exponent)}, one circuit x e^(4 pi i/3),")
print(f"      conjugate branch at phase 2 pi/3, {len(sheets)} sheets -> Z_3 (P08's e^(4 pi i/3),")
print("      P15's phase 2 pi/3, = s4a's cube-root cover w^3=z).")
print("  ** VERDICT 1: the background branch point is a CUBE-ROOT branch, monodromy Z_3. **")

# (2) P10 integrability: |r| ~ s^{2/3} -> integrand s^{-2/3}, integrable
Iact = sp.integrate(s**(-exponent), (s, 0, 1))
assert Iact == 3 and (-exponent) > -1, "s^{-2/3} integrable"
print(f"\n  (2) |r| ~ s^(2/3) -> integrand 1/|r| ~ s^(-2/3); int_0^1 s^(-2/3) ds = {Iact} (finite).")
print("  ** VERDICT 2: P10's finite Euclidean action is the SAME 2/3 exponent -- the cube root that")
print("     gives the Z_3 monodromy is what makes the action converge. **")

# (3) distinctness: Z_3 diagonalisable finite order vs unipotent infinite order
w = sp.exp(2 * sp.I * sp.pi / 3)
M_bg = sp.Matrix([[w, 0], [0, sp.conjugate(w)]])        # background: order 3, diagonalisable
M_pt = sp.Matrix([[1, 1], [0, 1]])                      # perturbation: unipotent (C9), infinite order
assert sp.simplify(M_bg**3) == sp.eye(2), "background monodromy order 3"
assert M_bg**1 != sp.eye(2) and M_bg**2 != sp.eye(2), "order exactly 3"
assert sp.simplify((M_pt - sp.eye(2))**2) == sp.zeros(2), "perturbation unipotent"
assert M_pt**3 != sp.eye(2), "unipotent is infinite order"
print("\n  (3) background monodromy: diagonalisable, order 3 (M^3 = I, M, M^2 != I).")
print("      perturbation monodromy: unipotent, (M-I)^2 = 0, INFINITE order (M^n != I for n>=1).")
print("  ** VERDICT 3: a finite-order diagonalisable Z_3 and an infinite-order unipotent are")
print("     DIFFERENT monodromies at the one point r=0 -- the background's areal radius carries the")
print("     first, the perturbation mode pair carries the second.  Only the cross-paper read")
print("     (P08/P15 background, P16 perturbation) separates them. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
