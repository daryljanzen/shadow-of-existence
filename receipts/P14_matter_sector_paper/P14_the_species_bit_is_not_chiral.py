"""
P14_the_species_bit_is_not_chiral.py -- P14 sec:whichthree: the sector's isospin reading is now
bounded from both sides, and the second bound is a NEGATIVE result stated at full weight.

** $T$ ACTS THE SAME ON BOTH $R$-EIGENSPACES.  The construction supplies a species LABEL and not
$SU(2)_L$'s chiral gauging -- and the mismatch with the Standard Model is exactly one pair wide. **

WHAT PROMPTED IT.  A companion receipt establishes that no $\\mathbb{Z}_2$ GRADING can reproduce
$SU(2)_L$'s $2{+}1{+}1$ decomposition, and points at the one thing a $\\mathbb{Z}_2$ COULD carry:
the orbit structure -- an action swapping the species on one chirality eigenspace and trivial on
the other.  That is the question this receipt answers.

WHAT IS ESTABLISHED.
  1. ** AT A SINGLE WALL THE QUESTION IS NOT WELL-POSED. **  Proposition prop:wall's zero-mode is
     the $\\sigma_y=+1$ eigenspinor with the conjugate branch rejected, so the bound content is a
     ONE-dimensional $R$-eigenspace with no partner.  And every $2\\times2$ matrix commuting with
     $\\sigma_y$ is a combination of the identity and $\\sigma_y$ (solved and asserted), so any
     operator commuting with $R$ -- as $T$ does -- acts on that space by a scalar.  "Non-trivially
     on one eigenspace and trivially on the other" has no content there.
  2. ** SO IT IS A QUESTION ABOUT THE SECTOR'S OCCUPATION OF THE AVAILABLE CHARACTERS, AND THE
     COUNT ANSWERS IT. **  The colourless sector is the four characters of $S_3\\times\\mathbb{Z}_2$
     trivial on the deck, indexed by $(T,R)$, and all four are present -- forced by the group.
     Each $R$-eigenspace therefore carries one $T$-even and one $T$-odd state, so $T$ acts
     non-trivially on BOTH and trivially on NEITHER (asserted).
  3. ** AND THE REASON IS STRUCTURAL: on a character of a DIRECT product the two factors' values
     are independent by construction. **  An action depending on the chirality would require the
     product not to be direct, and its directness is itself computed -- $T$ and $R$ act on
     independent data and commute.
  4. ** THE STANDARD MODEL'S OWN OCCUPATION DIFFERS ON EXACTLY ONE PAIR ** (asserted, with the
     Standard Model's action confirmed chiral by the same test): its left-handed pair is a doublet
     the isospin $\\mathbb{Z}_2$ exchanges, giving $T$-values $\\{+1,-1\\}$ -- which the geometry
     matches -- while its right-handed pair is two singlets each fixed, giving $\\{+1,+1\\}$, where
     the geometry gives $\\{+1,-1\\}$.  ** The construction reproduces the left-handed side's shape
     exactly and fails on the right-handed side, by making a distinction there that the Standard
     Model does not make. **

** WHAT THIS DOES AND DOES NOT DAMAGE.  The generation count, the chirality, the within-state
$S_3$, the deck $\\mathbb{Z}_3$, the discrete content of colour and the two-bit labelling of the
colourless four are all untouched: none of them rests on the clause.  What is withdrawn is the
reading of $T$ as $SU(2)_L$'s chiral gauging. **

** AND THE FALSIFIABLE DIRECTION IS RECORDED AS SUCH: if a right-handed weak structure
distinguishing $\\nu_R$ from $e_R$ by an isospin-like $\\mathbb{Z}_2$ were found, the geometry would
be right and this comparison wrong.  The mismatch is recorded as a mismatch. **

ORIGIN: computations/baryon_edge/L110y_is_the_species_bit_chiral.py -- built r2376 (c54.91);
edit the origin, not this copy.

ORIGIN-DIVERGENCE: DELIBERATE AND SUBTRACTIVE.  The origin also carries the clause-by-clause
verdict on the sector's standing discharge specification, which is register bookkeeping rather
than a paper claim.  ** This copy carries the paper-facing subset: every assertion here appears in
the origin verbatim, and nothing here is absent from it. **"""
import sympy as sp

print(__doc__)

# =====================================================================
print("=" * 78)
print("PART 1 — AT A SINGLE WALL THE QUESTION IS NOT WELL-POSED")
print("=" * 78)
print("     H = -i sigma_x d_x + m(x) sigma_z,   m odd, crossing zero at the throat")
print("     psi(x) = exp(-int_0^x m dx') chi_+,  chi_+ the sigma_y = +1 eigenspinor;")
print("     ** the conjugate branch chi_- grows and is REJECTED, so the bound content is one")
print("        ONE-dimensional R-eigenspace with no partner. **")
print()
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
a, b, c, d = sp.symbols('a b c d')
Mx = sp.Matrix([[a, b], [c, d]])
comm = sp.simplify(Mx*sy - sy*Mx)
sol = sp.solve([comm[i] for i in range(4)], [a, b, c, d], dict=True)[0]
gen = sp.simplify(Mx.subs(sol))
print("  Every 2x2 matrix commuting with sigma_y = R:")
sp.pprint(gen)
assert len(sorted({s for s in gen.free_symbols}, key=str)) == 2
print("     -- a two-parameter family, the span of the identity and sigma_y.")
print()
print("  ** T commutes with R, so T is diagonal in the sigma_y basis and acts on a")
print("     one-dimensional eigenspace by a SCALAR.  The clause has no content at one wall. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE OCCUPATION, WHICH IS WHAT THE CLAUSE IS REALLY ASKING")
print("=" * 78)
GEO = [(t, r) for t in (+1, -1) for r in (+1, -1)]
print(f"  {'the four colourless characters':>32} {'T':>4} {'R':>4}")
for t, r in GEO:
    print(f"  {'(T,R) = (%+d,%+d)' % (t, r):>32} {t:>4} {r:>4}")
print()
print(f"  {'R-eigenspace':>16} {'the T-values it carries':>28} {'is T trivial there?':>21}")
for r in (+1, -1):
    ts = sorted(t for (t, rr) in GEO if rr == r)
    print(f"  {('R = %+d' % r):>16} {str(ts):>28} {str(all(t == 1 for t in ts)):>21}")
triv = {r: all(t == 1 for (t, rr) in GEO if rr == r) for r in (+1, -1)}
chiral_geo = (triv[+1] != triv[-1])
print(f"\n  ** IS THE GEOMETRY'S ACTION CHIRAL?  {chiral_geo} **")
assert chiral_geo is False
print()
print("  ⇒ NO: each R-eigenspace carries one T-even and one T-odd state.  And the reason is")
print("     structural -- on a character of a DIRECT product the two factors' values are")
print("     independent by construction, and the product's directness is itself computed.")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE STANDARD MODEL'S OCCUPATION, AND WHERE THEY DIFFER")
print("=" * 78)
print(f"  {'states':>22} {'chirality R':>12} {'SU(2)_L':>13} {'what T does':>22} {'T-values':>12}")
SM = [("nu_L, e_L", "L", "doublet", "exchanges them", [+1, -1]),
      ("nu_R, e_R", "R", "two singlets", "fixes each", [+1, +1])]
for nm, ch, ir, act, ts in SM:
    print(f"  {nm:>22} {ch:>12} {ir:>13} {act:>22} {str(ts):>12}")
sm_triv = {ch: all(t == 1 for t in ts) for nm, ch, ir, act, ts in SM}
chiral_sm = (sm_triv['L'] != sm_triv['R'])
print(f"\n  ** IS THE STANDARD MODEL'S ACTION CHIRAL?  {chiral_sm} **")
assert chiral_sm is True
print()
print(f"  {'':>16} {'R-even side':>26} {'R-odd side':>26}")
print(f"  {'THE GEOMETRY':>16} {'{+1, -1}':>26} {'{+1, -1}':>26}")
print(f"  {'THE SM':>16} {'{+1, -1}  (the doublet)':>26} {'{+1, +1}  (two singlets)':>26}")
print()
for s in [
 "⇒⇒ ** THEY AGREE ON ONE $R$-EIGENSPACE AND DIFFER ON THE OTHER, AND THE DIFFERENCE IS EXACTLY",
 "   ONE PAIR WIDE. **  The construction reproduces the left-handed side's shape exactly and",
 "   fails on the right-handed side, by making a distinction there the Standard Model does not.",
 "",
 "⌗ *Falsifiable in the honest direction: a right-handed weak structure distinguishing $\\nu_R$",
 "from $e_R$ by an isospin-like $\\mathbb{Z}_2$ would make the geometry right and this comparison",
 "wrong.  ** The corpus should not want that, and records the mismatch as a mismatch. ***",
]:
    print("  " + s)
