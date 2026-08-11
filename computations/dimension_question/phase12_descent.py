"""PHASE 1-2: does a higher substrate break the range or the algebroid?
Bookkeeping first -- WHERE does the corpus's worked geometry actually live?"""
import sympy as sp
d=lambda n: n*(n+1)//2                      # dim so(n,1) = dim so(n+1) = n(n+1)/2
print("="*80); print(" (1) WHERE THE WORKED GEOMETRY LIVES  -- dS_n in R^{1,n}: throat (X0=0) is S^{n-1}")
print("="*80)
for n in (4,5,6,7):
    print("   dS_%d  embeds in R^{1,%d} (coords X0..X%d)   throat at X0=0 is  S^%d"%(n,n,n,n-1))
print("\n   CORPUS (ONTOLOGY sec-0): embedding '-X0^2+X1^2+...+X4^2 = alpha^2', throat = S^3.")
print("   => that is dS_4.  Section 0 flags it: this embedding is RUNG (2), the BACKGROUND.")
print("   => the throat-S^3, the hinges, the horizon cubic, the hexad, the GENERATIONS")
print("      are all worked on the FOUR-geometry, not on the substrate.")
print()
print("="*80); print(" (2) THE ALGEBROID GRADING AT EACH RUNG OF A DESCENT  dS_D -> ... -> dS_4")
print("="*80)
print("   symmetric space dS_n = SO(n,1)/SO(n-1,1):  so(n,1) = h + m,  [m,m] subset h")
print("   rung       | isometry   dim | isotropy   dim | coset m | P12's match?")
for n in (7,6,5):
    print("   dS_%d -> dS_%d | so(%d,1)  %3d  | so(%d,1)  %3d  |   %2d    | %s"
          %(n,n-1,n,d(n),n-1,d(n-1),d(n)-d(n-1),
            "YES -- this IS P12's so(5,1)=so(4,1)+m" if n==5 else "same form, one rung up"))
print("\n   *** P12 identifies GR's Dirac algebra with the grading of the LAST step, so(5,1)/so(4,1).")
print("       A descent 7->6->5->4 has EXACTLY that as its final step.")
print("       => the algebroid keystone constrains the PENULTIMATE RUNG, not the substrate. NOT KILLED.")
print()
print("="*80); print(" (3) WHERE su(3) COULD SIT, AND THE COST")
print("="*80)
for D in (5,6,7,10):
    mc=D-1                                   # maximal compact of isotropy so(D-1,1) is so(D-1)
    layer=3                                  # the existent layer is 3-dimensional (P7 axiom)
    print("   dS_%-2d: isotropy so(%d,1), max compact so(%d) %s su(3);  spatial dirs %d = layer %d + extra %d"
          %(D,D-1,D-1,"CONTAINS" if mc>=6 else "lacks   ",mc,layer,mc-layer))
print("\n   su(3) acts IRREDUCIBLY on R^6.  At D=7 there are only 3 extra spatial directions,")
print("   so the 6 it needs must OVERLAP the 3 layer directions -> spacetime/internal mixing.")
print("   Disjoint from the layer needs 6 extra spatial dirs -> D-1 >= 9 -> D >= 10.")
print("   *** THE FORK IS SHARP AND IS NOT A BOOKKEEPING QUESTION:")
print("       overlap  -> D>=7,  but su(3) rotates layer directions into internal ones;")
print("       disjoint -> D>=10, layer untouched, colour purely internal.")
