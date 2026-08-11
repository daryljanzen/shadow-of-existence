"""V1 — IS THE CARTER-CONSTANT CLAIM A NOETHER, KILLING-TENSOR, OR SEPARABILITY STATEMENT?
CONFIRMATION 2 — P9 read whole, and the ledger's premise ('the corpus's wording does not distinguish
them') is WRONG.  P9 distinguishes them explicitly and cites the right sources.  What it has:"""
print("="*80); print("V1 — THE CORPUS HAS THE CHAIN. IT DOES NOT HAVE IT AS A CHAIN."); print("="*80)
print("""
  WHAT P9 ALREADY SAYS, at source:

  (i)  IT SEPARATES VECTORS FROM TENSORS, EXPLICITLY:
       'What governs reachability is the count of Killing VECTORS (the honest isometry, by
        thm:bound), NOT the count of Killing TENSORS.'
       -> so the ledger's worry that the corpus conflates them is unfounded.

  (ii) IT SCOPES cor:carter HONESTLY, in the sentence that matters:
       'The separation is NOT IMPOSED BEYOND THE SEPARABLE FORM.'
       -> the separable (Carter) ansatz IS imposed; what is shown is that the vacuum condition on
          the maximally symmetric substrate then splits OF ITS OWN ACCORD, and the computation is
          exhibited: Delta_r''(r) + Delta_p''(p) = -4 Lambda (r^2 + p^2).
       -> and Carter 1968 is cited BY TITLE: 'Hamilton--Jacobi and Schrodinger separable solutions'.
          So the HJ-separability the Carter constant lives on is the ansatz's, named and sourced.

  (iii) AND THE EXPLANATION THAT DOES NOT ASSUME THE ANSATZ IS ALSO THERE, in the same paper:
       'By the GOLDBERG--SACHS theorem an algebraically special vacuum carries a shear-free null
        geodesic congruence; THE SUBSTRATE'S NULL RULINGS ARE SHEAR-FREE, and a cut that inherits
        one as its principal congruence IS ALGEBRAICALLY SPECIAL -- this is the Type-D [mechanism].'

  (iv) AND THE LAST LINK IS CITED TOO: Walker--Penrose 1970, for the Killing tensor and the Carter
       constant of a Type-D vacuum.
""")
print("  SO THE CHAIN EXISTS, COMPLETE AND SOURCED, IN ONE PAPER:\n")
chain=[("the substrate's null rulings are SHEAR-FREE","P3/P9, the doubly-ruled hyperboloid"),
       ("a cut inheriting one as its principal congruence","P9, the shift--shear link"),
       ("=> ALGEBRAICALLY SPECIAL","Goldberg--Sachs"),
       ("=> TYPE D","P9, the speciality invariant verified"),
       ("=> admits a KILLING TENSOR","Walker--Penrose 1970, cited in P9"),
       ("=> the CARTER CONSTANT","the constant of motion that tensor carries")]
for i,(a,b) in enumerate(chain):
    print(f"    {i+1}. {a:52s}  [{b}]")
print("""
  *** SO V1's ANSWER: the claim is a SEPARABILITY-AND-ALGEBRAIC-SPECIALITY statement, it is correctly
      scoped where it is made, and it needs no Noether theorem -- because the Carter constant is not
      a Noether charge of a point symmetry and P9 never says it is. ***

  WHAT IS ACTUALLY MISSING, and it is small and worth having: THE CHAIN IS NOT STATED AS A CHAIN.
  cor:carter gives step 5-6 on the Carter ansatz; the shift--shear passage gives steps 1-4; and the
  two sit in different sections without the arrow drawn between them.  A reader meeting cor:carter
  alone sees 'the vacuum condition separates on a separable ansatz', which is weaker than what the
  paper has -- the paper can say WHY the cuts are Type D at all, and therefore why a Killing tensor
  is there to be found.
""")
print("="*80)

# ** r2376+c54.161 -- THE CHAIN, ASSERTED (this receipt printed it and never checked it). **
#   The finding is that the chain exists COMPLETE AND SOURCED in one paper but is not stated as a
#   chain: six links, four arrows, every link carrying its source, running from the substrate's
#   shear-free rulings to the Carter constant, with Goldberg--Sachs and Walker--Penrose 1970 at
#   the two steps that are theorems rather than P9's own.
assert len(chain) == 6, len(chain)
assert all(a.strip() and b.strip() for a, b in chain)
assert chain[0][0].endswith("SHEAR-FREE"), chain[0]
assert "CARTER CONSTANT" in chain[-1][0], chain[-1]
assert sum(1 for a, _ in chain if a.startswith("=>")) == 4
assert "Goldberg" in chain[2][1] and "Walker" in chain[4][1] and "1970" in chain[4][1]
assert "ALGEBRAICALLY SPECIAL" in chain[2][0] and "TYPE D" in chain[3][0]
assert "KILLING TENSOR" in chain[4][0]

#   AND LINK 4 IS A COMPUTATION, NOT A CITATION -- which is the part of V1's answer that can be
#   checked here.  TYPE D is the speciality condition I^3 = 27 J^2 on the Weyl invariants.  For a
#   traceless Weyl operator with eigenvalues (2,-1,-1)*lam (two equal: the Type-D pattern),
#   I = tr(Q^2)/2 and J = tr(Q^3)/6 give I = 3 and J = 1 at lam = 1, so I^3 = 27 = 27 J^2 EXACTLY.
#   The generic Type-I pattern (1,0,-1) gives I = 1, J = 0 and I^3 - 27 J^2 = 1, not special.
def _weyl_IJ(eigs):
    assert sum(eigs) == 0, eigs                      # the Weyl operator is traceless
    return sum(e**2 for e in eigs)/2, sum(e**3 for e in eigs)/6
_I_D, _J_D = _weyl_IJ((2, -1, -1))
assert abs(_I_D - 3.0) < 1e-12 and abs(_J_D - 1.0) < 1e-12, (_I_D, _J_D)
assert abs(_I_D**3 - 27*_J_D**2) < 1e-12             # ALGEBRAICALLY SPECIAL: TYPE D, link 4
assert abs(_I_D**3 - 27.0) < 1e-12
_I_I, _J_I = _weyl_IJ((1, 0, -1))
assert abs(_I_I - 1.0) < 1e-12 and abs(_J_I) < 1e-12, (_I_I, _J_I)
assert abs(_I_I**3 - 27*_J_I**2 - 1.0) < 1e-12       # TYPE I: the condition FAILS, as it must
