"""
ATTACKING sec:closure's unification claim.

MY CLAIM: "The levels ... are what makes the paper's own negative results intelligible
as a set: C != R because R is L1 and C is L3; C != (Q->-Q) because that is L3's even
face only; C not-in D6 x Z2 because C is not at L1 at all. EACH OF THOSE FAILURES IS
THE SAME FAILURE -- AN ATTEMPT TO FIND C AT THE WRONG LEVEL."

This is a claim about the paper's OTHER remarks. I wrote it without re-reading them
against it. Test each of the three, using the ledger's own level assignments and the
r1073 WELD (which CORRECTED [1] and [2]'s stated reasons).

THE LEDGER'S LEVELS (D-Canat, verbatim):
    L1  substrate ISOMETRY            real, LINEAR, det +-1     R=gamma^5, P, T, sigma
    L2  substrate COMPLEX-ANALYTIC    ANTIHOLOMORPHIC           tau~ <-> conj(tau~)
    L3  FIELD                         ANTILINEAR on the field   C proper; A_t = Q/r
and the ledger puts Q->-Q at:  "L3 (metric shadow adjoins a Z2)".
"""

print("="*80)
print("TEST 1 — is 'wrong LEVEL' the reason each candidate fails?")
print("="*80)
rows = [
    ("C = R ?",            "L1", "L3", "LINEAR",  "ANTILINEAR", "different level AND character"),
    ("C = Q->-Q ?",        "L3", "L3", "LINEAR",  "ANTILINEAR", "SAME LEVEL, different character"),
    ("C = R x (Q->-Q) ?",  "L1xL3","L3","LINEAR",  "ANTILINEAR", "mixed level, different character"),
]
print(f"  {'candidate':<20} {'cand lvl':>8} {'C lvl':>6} {'cand char':>11} {'C char':>12}   diagnosis")
for a,b,c,d,e,f in rows:
    print(f"  {a:<20} {b:>8} {c:>6} {d:>11} {e:>12}   {f}")
print()
print("  >> ** THE CLAIM IS FALSE FOR THE SECOND ONE. ** Q->-Q sits at L3 -- the ledger")
print("     says so explicitly -- which is EXACTLY WHERE C IS. It is at the RIGHT level")
print("     and still is not C. So 'an attempt to find C at the wrong level' does not")
print("     cover the set, and my 'each of those failures is the same failure' unified")
print("     on an axis that does not do the work.")

print()
print("="*80)
print("TEST 2 — then what DOES cover the set? Try CHARACTER.")
print("="*80)
print("  C is ANTILINEAR (psi^c = C gamma^0T psi*, the corpus's stated convention).")
print("  Every candidate offered:")
print("     R           : real reflection in O(5,1)            LINEAR")
print("     Q -> -Q     : a sign flip of a parameter           LINEAR")
print("     R x (Q->-Q) : a product of two linear maps         LINEAR")
print("  >> ALL THREE ARE LINEAR. C IS NOT. ONE reason, covering all three.")
print()
print("  And this is not a new reason -- it is rem:C-not-R's OWN load-bearing argument,")
print("  the one r1088 stage 1 restored and the r1073 weld confirmed was 'always its")
print("  real argument'.")

print()
print("="*80)
print("TEST 3 — the WELD already killed the reasons I gave. Check.")
print("="*80)
print("  [1] my reason: 'R is L1, C is L3'  ~ the old 'R is mass-odd, C mass-even'.")
print("      WELD: WRONG -- |2M| is the physical mass and R PRESERVES it; only the SIGN")
print("      flips, and the sign is the relational branch label. 'I compared a label to")
print("      a mass.' The surviving reason is LINEARITY.")
print("  [2] my reason: 'Q->-Q is L3's even face only'.")
print("      WELD: 'Q->-Q fixes species' was WRONG -- Q->-Q IS the species flip. What")
print("      survives is that it is C's EVEN FACE: a PART/WHOLE relation, not a level")
print("      one. And the reason it is not C is again LINEARITY.")
print("  [3] my reason: 'C is not at L1 at all'.")
print("      Post-weld the old reason ('R x (Q->-Q) flips mass, C doesn't') is ALSO dead:")
print("      R flips sign(2M) = the branch label = the species label, and C flips species,")
print("      so they AGREE there. The surviving reason is -- again -- LINEARITY.")
print()
print("  >> ALL THREE of my stated reasons were the PRE-WELD ones, re-dressed in level")
print("     language. I baked the weld into P13 this morning and then, an hour later,")
print("     wrote a synthesis on top of the reasons the weld had killed.")

print()
print("="*80)
print("VERDICT — and the fix is a strengthening")
print("="*80)
print("  THE CLAIM AS WRITTEN IS WRONG. The set is not unified by LEVEL. It is unified")
print("  by CHARACTER: every candidate is LINEAR and C is ANTILINEAR. One reason, three")
print("  failures, and it is the paper's own argument.")
print()
print("  AND THE LEVELS ARE NOT REDUNDANT -- THEY HAVE A DIFFERENT JOB, and conflating")
print("  the two jobs is what produced the error:")
print("     * CHARACTER (linear vs antilinear) answers: WHY DOES EVERY C-CANDIDATE FAIL?")
print("     * LEVEL (L1 / L2 / L3) answers: WHERE WAS THE PERIMETER DRAWN, AND WHAT DID")
print("       IT NOT REACH?  -- which is [5], the whole content of rem:C-scope: the")
print("       premise covers L1 isometries; L2 is antilinear AND geometric; so")
print("       not-an-isometry != not-geometric.")
print()
print("  The two axes CROSS, and that is the actual structure:")
print(f"     {'':22} {'LINEAR':>12} {'ANTILINEAR':>12}")
print(f"     {'L1 (isometry)':22} {'R, P, T, sigma':>12} {'--':>12}")
print(f"     {'L2 (cplx-analytic)':22} {'--':>12} {'tau~<->conj':>12}")
print(f"     {'L3 (field)':22} {'Q -> -Q':>12} {'C proper':>12}")
print("  Read it: the LINEAR column is why the candidates fail. The L1 ROW is where the")
print("  perimeter was drawn. The L2 cell -- antilinear AND geometric -- is the one the")
print("  premise never reached, and it is the single cell the whole correction is about.")
print("  ** A 2x3 table, not a 1x3 list. My sentence collapsed a column into a row. **")
