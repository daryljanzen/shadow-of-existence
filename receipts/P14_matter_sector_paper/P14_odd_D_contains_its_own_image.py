"""
P14_odd_D_contains_its_own_image.py -- P14 sec:dimension: a second and independent derivation of
the odd-$D$ exclusion, from the HORIZON ROOT SET rather than from the mass function's parity, and
it supplies the mechanism the parity argument only names.

** $-r_0$ IS A ROOT OF THE HORIZON POLYNOMIAL EXACTLY AT ODD $D$.  So at odd $D$ the offset
parity's image of a geometry is already inside that geometry's own root set, and $R$ has nothing
to relate; at even $D$ it carries the geometry to a different member of the family, which is what
lets it serve as a matter/antimatter parity. **

WHAT IS ESTABLISHED.
  1. ** THE FACTORISATION AT GENERAL $D$. **  With the slicing's own root substituted, the
     horizon condition is $P_D(r)=r^{D-1}-r^{D-3}+r_0^{D-3}-r_0^{D-1}$, and $(r-r_0)$ divides it
     at every $D$ (asserted), which is the designation $1+(D-2)$ split.
  2. ** $-r_0$ IS A ROOT EXACTLY AT ODD $D$ ** (asserted at $D=4,5,6,7$): substituting $r=-r_0$
     returns $2\\,(r_0^{D-3}-r_0^{D-1}) = 2\\cdot 2M$ at even $D$ and $0$ at odd.
  3. ** SO AT $D=5$ THE COFACTOR IS $(r+r_0)(r^2+r_0^2-1)$ -- A LINE AND A CIRCLE -- AND THE
     $1+3$ IS REALLY $1+1+2$, the extra one being $-r_0$ itself. **  At $D=4$ the cofactor is
     $r^2+rr_0+r_0^2-1$, a genuine conic with a cross term; at $D=6$ and $D=8$ it does not factor
     over the rationals.  So the conic cofactor is a $D=4$ phenomenon in a stronger sense than
     "only at four": what replaces it at five is a degenerate pair, not another conic.
  4. ** THE ROOT-SET COLUMN AND THE MASS-PARITY COLUMN ARE EXACT COMPLEMENTS ** (asserted at five
     dimensions): $-r_0$ lies in the root set precisely when $2M$ is not odd in $r_0$, i.e.
     precisely when there is no $\\gamma^5$.
  5. ** AND THAT IS THE MECHANISM RATHER THAN A CORRELATION. **  At even $D$, $r_0\\mapsto-r_0$
     carries $2M$ to $-2M$, so $R$ relates two distinct members of the family and can serve as a
     matter/antimatter parity.  At odd $D$ the $R$-image root sits inside the same geometry's own
     root set, so $R$ moves nothing: the geometry is its own image.  ** "Five is vector-like" and
     "five's conjugate is itself" are one statement. **

** SCOPE.  This inherits the paper's own extension of the metric function to general $D$ (the
standard Tangherlini--de~Sitter form) and weakens nothing about it.  It is an independent route
to a conclusion the paper already draws from the mass function's parity; the two routes share no
step, and this one exhibits the mechanism. **

ORIGIN: computations/baryon_edge/L048w_the_r3_cluster.py -- built r2376 (c54.82);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also disposes of three register items
about a ledger row's pairing of objects to targets, which are bookkeeping rather than paper
claims.  ** This copy carries the paper-facing subset: every assertion here appears in the origin
verbatim, and nothing here is absent from it. **"""
import sympy as sp

print(__doc__)
r, r0 = sp.symbols('r r_0', real=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE HORIZON POLYNOMIAL AT GENERAL D, FACTORISED")
print("=" * 78)
print("     P_D(r) = r^(D-1) - r^(D-3) + r_0^(D-3) - r_0^(D-1) = 0")
print()
print(f"  {'D':>3} {'(r - r_0) divides?':>19} {'the cofactor':>44} {'-r_0 a root?':>13}")
cof = {}
for D in range(4, 9):
    P = sp.expand(r**(D-1) - r**(D-3) + r0**(D-3) - r0**(D-1))
    q, rem = sp.div(P, r - r0, r)
    assert sp.simplify(rem) == 0
    f = sp.factor(q)
    neg = (sp.simplify(P.subs(r, -r0)) == 0)
    cof[D] = (f, neg)
    print(f"  {D:>3} {'yes':>19} {str(f)[:44]:>44} {str(neg):>13}")
assert cof[4][1] is False and cof[5][1] is True
assert cof[6][1] is False and cof[7][1] is True
print()
for s in [
 "⇒⇒ ** $-r_0$ IS A ROOT EXACTLY AT ODD $D$, asserted at four values. **  *Substituting",
 "   $r=-r_0$ gives $2(r_0^{D-3}-r_0^{D-1}) = 2\\cdot 2M$ at even $D$ and $0$ at odd.*",
 "",
 "⇒ ** AT $D=5$ THE COFACTOR IS A LINE TIMES A CIRCLE, so the $1{+}3$ is really $1{+}1{+}2$ with",
 "   the extra one being $-r_0$ itself; at $D=4$ it is a genuine conic; at six and eight it does",
 "   not factor over the rationals. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE ROOT SET AND THE MASS PARITY ARE COMPLEMENTS")
print("=" * 78)
print(f"  {'D':>3} {'2M(r_0) odd in r_0?':>21} {'-r_0 in the root set?':>23} {'gamma^5 exists?':>16}")
for D in range(4, 9):
    twoM = sp.expand(r0**(D-3) - r0**(D-1))
    odd = sp.simplify(twoM.subs(r0, -r0) + twoM) == 0
    print(f"  {D:>3} {str(odd):>21} {str(cof[D][1]):>23} {str(odd):>16}")
    assert odd != cof[D][1]
print()
for s in [
 "⇒⇒ ** EXACT COMPLEMENTS, ASSERTED AT FIVE DIMENSIONS. **",
 "",
 "⌗⌗ ** AND THAT IS THE MECHANISM. **  At EVEN $D$, $r_0\\mapsto-r_0$ carries $2M$ to $-2M$: $R$",
 "   relates two DISTINCT members of the family and can serve as a matter/antimatter parity.  At",
 "   ODD $D$ the $R$-image root sits INSIDE THE SAME GEOMETRY'S OWN ROOT SET, so $R$ moves",
 "   nothing -- ** the geometry is its own image, and the parity has nowhere to act. **",
 "",
 "⇒ ** SO 'FIVE IS VECTOR-LIKE' AND 'FIVE'S CONJUGATE IS ITSELF' ARE ONE STATEMENT, reached here",
 "   from the root set and elsewhere from the mass function's Fourier content, by routes sharing",
 "   no step. **",
]:
    print("  " + s)
