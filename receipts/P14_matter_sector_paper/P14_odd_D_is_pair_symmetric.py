"""
P14_odd_D_is_pair_symmetric.py -- P14 sec:dimension: two further structures that fail at odd $D$,
and they fail for the reason already established there.

** AT ODD $D$ THE HORIZON POLYNOMIAL $r^{D-1}-r^{D-3}+2M$ IS EVEN IN $r$. **  The paper already
uses one consequence -- the mass function's evenness, hence no $\\gamma^{5}$ -- and a companion
receipt adds a second, that $-r_0$ lies in the geometry's own root set.  Two more follow from the
same evenness, and neither was known to be the same fact.

WHAT IS ESTABLISHED.
  1. ** THE POLYNOMIAL IS EVEN IN $r$ EXACTLY AT ODD $D$ ** (asserted at $D=4\\ldots8$), the two
     powers present being $D-1$ and $D-3$, of one parity.
  2. ** SO AT ODD $D$ THE ROOT SET IS STABLE UNDER A FIXED-POINT-FREE INVOLUTION ** ($r=0$ is a
     root only at $2M=0$), and the monodromy over the mass plane commutes with it.  At $D=5$ that
     confines the monodromy group to the centraliser of $(0\\,1)(2\\,3)$ in $S_{4}$, of order eight
     against $|S_{4}|=24$ (both computed and asserted).  ** So the deck group cannot be $S_{D-1}$
     at odd $D$: the four-dimensional statement "the deck group is the full symmetric group on the
     roots" has no odd-dimensional analogue to check. **
  3. ** AND THE ROOT CONFIGURATION IS NOT OF $A_{2}$ TYPE. **  The sum of the roots vanishes at
     every $D$ (no subleading term), but at $D=4$ that is three roots summing to zero -- the
     $A_{2}$ skeleton -- whereas at $D=5$ it is four roots summing to zero \\emph{in $\\pm$ pairs},
     $\\{\\pm a,\\pm b\\}$, which is neither $A_{2}$ nor $A_{3}$.  ** So at $D=5$ there is no $A_{2}$
     whose automorphism group could factorise or fail to. **

** WHAT THIS DOES AND DOES NOT SAY.  It adds two consequences to an exclusion the paper already
makes on other grounds; it does not strengthen the exclusion, which was already complete.  Its
value is that four separate failures at odd $D$ -- the absent mass parity, the reflected root
lying inside the root set, the monodromy's imprimitivity, and the $\\pm$-paired root set -- are one
fact, and were reached separately without that being noticed. **

ORIGIN: computations/baryon_edge/L016w_the_dimension_cluster.py -- built r2376 (c54.83);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also carries the eikonal ringdown
result (receipted separately against P7), a cross-ratio computation, and a degenerate-horizon
control, none of which is a claim of this paper.  ** This copy carries the paper-facing subset:
every assertion here appears in the origin verbatim, and nothing here is absent from it. **⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT c01f56c** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

"""
import itertools
import sympy as sp

print(__doc__)
r, M = sp.symbols('r M', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — EVEN IN r EXACTLY AT ODD D")
print("=" * 78)
print(f"  {'D':>3} {'the horizon polynomial in 2M':>34} {'even in r?':>11}")
for D in range(4, 9):
    P = sp.expand(r**(D-1) - r**(D-3) + 2*M)
    ev = sp.simplify(sp.expand(P.subs(r, -r) - P)) == 0
    print(f"  {D:>3} {str(P):>34} {str(ev):>11}")
    assert ev == (D % 2 == 1)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — SO THE MONODROMY CANNOT BE THE FULL SYMMETRIC GROUP")
print("=" * 78)
S4 = list(itertools.permutations(range(4)))
inv = (1, 0, 3, 2)


def comp(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


cent = [p for p in S4 if comp(p, inv) == comp(inv, p)]
print("  At D=5 the root set is stable under r -> -r with no fixed root (r=0 is a root only at")
print("  2M=0), so the involution is FIXED-POINT-FREE and the monodromy commutes with it.")
print(f"     |S_4| = {len(S4)},   |centraliser of (0 1)(2 3) in S_4| = {len(cent)}")
assert len(S4) == 24 and len(cent) == 8
print()
print("  ** So the monodromy group is contained in a group of order eight and cannot be S_4. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND THE ROOT SET IS NOT OF A_2 TYPE")
print("=" * 78)
print(f"  {'D':>3} {'roots':>7} {'sum of roots':>13} {'structure of the root set':>34}")
for D in range(4, 8):
    P = sp.Poly(r**(D-1) - r**(D-3) + 2*M, r)
    cs = P.all_coeffs()
    s_ = -cs[1]/cs[0]
    shape = ("+/- PAIRED (even polynomial)" if D % 2 else "no pairing (odd polynomial)")
    print(f"  {D:>3} {D-1:>7} {str(sp.simplify(s_)):>13} {shape:>34}")
print()
for s in [
 "⇒ ** $D=4$: THREE roots summing to zero -- the $A_2$ skeleton.  $D=5$: FOUR roots summing to",
 "   zero IN $\\pm$ PAIRS, which is neither $A_2$ nor $A_3$.  So at five there is no $A_2$ whose",
 "   automorphism group could factorise or fail to. **",
 "",
 "⌗⌗ ** FOUR FAILURES AT ODD $D$, ONE FACT: the absent mass parity, the reflected root lying",
 "   inside the root set, the monodromy's imprimitivity, and the $\\pm$-paired root set.  They",
 "   were reached separately and the evenness was never named. **",
]:
    print("  " + s)
