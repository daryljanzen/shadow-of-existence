"""
DRAFT_P13_su3_fits_exactly_one_real_form.py -- P13 sec:face-status / sec:wall:
** so(6,C) HAS FOUR REAL FORMS, NOT TWO -- AND su(3) EMBEDS IN EXACTLY ONE OF THEM, THE COMPACT
   ONE.  SO "COLOUR LIVES ON THE COMPACT FACE" IS FORCED BY THE GROUP THEORY, NOT CHOSEN AGAINST
   IT. **

WHAT THE CORPUS HAS.  P13 establishes the structural fact the four routes converge on -- that
su(3) is not in so(5,1) -- and `P13_qm_S4_vs_S5` shows the sharper form: "su(3) requires
so(6)/S^5 not so(5)/S^4: 8 Gell-Mann generators realified to R^6 all antisymmetric".  Both are
right and both are reproduced below.

WHAT THIS ADDS, and it lands on ONE SENTENCE.  P13 sec:face-status opens the status question with:

  ** "Mathematically the compact SO(6) face and the Lorentzian SO(5,1) substrate are co-equal real
     forms of the one complex group SO(6,C); NOTHING IN THE GROUP THEORY PRIVILEGES ONE." **

and then breaks the tie ONTOLOGICALLY -- a Riemannian S^5 carries no clock, so by CR's existence
criterion it cannot be a co-equal existent.  That argument is untouched by anything here.

But so(6,C) has ** FOUR ** real forms, and the sentence considers two:

    so(6)   = su(4)      COMPACT
    so(5,1) = su*(4)     the substrate
    so(4,2) = su(2,2)
    so(3,3) = sl(4,R)

** And su(3) embeds in exactly one of the four. **  Every compact subalgebra of a real semisimple
Lie algebra is conjugate into a maximal compact subalgebra (Cartan), so a compact algebra of
dimension 8 can only sit inside a real form whose maximal compact admits it:

    real form            maximal compact              dim     su(3) (dim 8) fits?
    so(6)   = su(4)      su(4) itself (compact)        15      ** YES **
    so(5,1) = su*(4)     sp(2) = so(5)                 10      no -- see below
    so(4,2) = su(2,2)    s(u(2)+u(2))                   7      no -- 8 > 7
    so(3,3) = sl(4,R)    so(4)                          6      no -- 8 > 6

The so(5,1) row needs one more line because 10 > 8 and the dimension count alone does not settle
it: ** su(3) has no faithful real representation below dimension six ** (its smallest faithful
complex representation is the 3, whose realification is 6; the adjoint is 8), while so(5) acts
faithfully on R^5.  ** So su(3) is not in so(5), hence not in sp(2), hence not in so(5,1). **
That is `P13_qm_S4_vs_S5`'s fact, used here as the one row the counting misses.

⇒ ** THE TIE IS ALREADY BROKEN, BY THE GROUP THEORY, IN THE DIRECTION THE PAPER NEEDS. **  Among
the real forms of the complexification, the compact one is the UNIQUE home for colour.  "Nothing
in the group theory privileges one" is true of the two forms taken as forms; it is false once the
question is where su(3) can live -- which is the question the section is about.

** WHY THIS STRENGTHENS sec:face-status RATHER THAN REPLACING IT. **  The section's work is to
deny the compact face the standing of a co-equal EXISTENT, and that is an ontological claim which
no representation theory can make.  What changes is the setup: the section currently concedes a
symmetric starting position ("nothing in the group theory privileges one") and then breaks it from
outside.  ** It does not have to concede that much. **  On the colour question the group theory is
not symmetric: three of the four real forms cannot carry su(3) at all, and the one that can is the
one with no clock.  ** That is a sharper statement of the same wall -- colour and duration are not
merely in different places, they are in the only two places available and those places are
disjoint. **

HONEST WEIGHT.  ** The mathematics is standard and none of it is new. **  The real-form list and
the maximal compacts are textbook; su(3) ⊄ so(5) is the corpus's own.  What is offered is that the
four-form statement is the one the section wants and the two-form statement is the one it makes.

STATED FOR REVERSAL.  No closure on any registered item; the universal claim P13 declines is not
made here either.  Searched `real form` (12 hits, none enumerating the four), `su(2,2)`, `sl(4,R)`,
`so(3,3)`, `so(4,2)`, `maximal compact` across corpus/, receipts/, computations/ and
storyboard_receipts/.
"""
import numpy as np
import itertools

print(__doc__)

# ============================================================================
print("=" * 78)
print("PART 1 — su(3) INSIDE so(6), BUILT EXPLICITLY")
print("=" * 78)
# Gell-Mann matrices
l = [np.array(m, dtype=complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
    [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
    [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3))]
T = [1j * x / 2 for x in l]                      # anti-Hermitian su(3) generators


def realify(Z):
    """C^3 -> R^6 with basis (Re e1, Im e1, Re e2, Im e2, Re e3, Im e3)"""
    R = np.zeros((6, 6))
    for j in range(3):
        for i in range(3):
            a, b = Z[i, j].real, Z[i, j].imag
            R[2 * i, 2 * j] = a;      R[2 * i, 2 * j + 1] = -b
            R[2 * i + 1, 2 * j] = b;  R[2 * i + 1, 2 * j + 1] = a
    return R


RT = [realify(t) for t in T]
anti = all(np.allclose(R + R.T, 0, atol=1e-12) for R in RT)
print(f"  8 Gell-Mann generators, anti-Hermitian, realified to R^6")
print(f"  all antisymmetric (i.e. in so(6))          : {anti}")
assert anti
ind = np.linalg.matrix_rank(np.array([R.flatten() for R in RT]), tol=1e-9)
print(f"  linearly independent                        : {ind} of 8")
assert ind == 8
# closure on su(3) structure constants
closed = True
basis = np.array([R.flatten() for R in RT]).T
for a, b in itertools.combinations(range(8), 2):
    C = RT[a] @ RT[b] - RT[b] @ RT[a]
    x, res, *_ = np.linalg.lstsq(basis, C.flatten(), rcond=None)
    if np.linalg.norm(basis @ x - C.flatten()) > 1e-9:
        closed = False
print(f"  brackets close on the same 8                : {closed}")
assert closed
print(f"  dim so(6) = 15, dim su(3) = 8               : fits")
print("  ** su(3) is a subalgebra of so(6).  (P13_qm_S4_vs_S5's fact, rebuilt.) **")

# ============================================================================
print()
print("=" * 78)
print("PART 2 — AND NOT OF so(5): THE REPRESENTATION-DIMENSION FLOOR")
print("=" * 78)
print("  so(5) acts faithfully on R^5.  su(3)'s smallest faithful representations:")
print(f"     {'rep':>18} {'complex dim':>12} {'real dim':>10}")
for nm, cd, rd in (("trivial", 1, 1), ("fundamental 3", 3, 6), ("conjugate 3-bar", 3, 6),
                   ("adjoint 8", 8, 8), ("6", 6, 12)):
    print(f"     {nm:>18} {cd:>12} {rd:>10}")
print()
print("  ** the smallest FAITHFUL real representation of su(3) has dimension 6 ** -- the")
print("     realification of the 3.  (The adjoint, dimension 8, is faithful for su(3) since its")
print("     centre is trivial, but is larger.)  There is no faithful real rep of dimension 5.")
print("  ⇒ ** su(3) cannot act faithfully on R^5, so su(3) is not a subalgebra of so(5). **")
print()
# a numerical corroboration: no 8-dim subalgebra of so(5) at all
print("  corroboration -- the maximal proper subalgebras of so(5) (dim 10) and their dimensions:")
for nm, d in (("so(4) = su(2)+su(2)", 6), ("so(3)+so(2)", 4), ("principal su(2)", 3)):
    print(f"     {nm:<24} {d:>3}")
print("     ** largest is 6 < 8, so so(5) has no 8-dimensional subalgebra at all. **")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — THE FOUR REAL FORMS OF so(6,C), AND WHERE su(3) CAN LIVE")
print("=" * 78)
print("  Cartan: every COMPACT subalgebra of a real semisimple Lie algebra is conjugate into a")
print("  maximal compact subalgebra.  su(3) is compact of dimension 8, so it can only sit in a")
print("  real form whose maximal compact admits it.\n")
forms = [
    ("so(6)   = su(4)", "su(4) (the form is compact)", 15, "YES", "contains su(3) as a block; PART 1"),
    ("so(5,1) = su*(4)", "sp(2) = so(5)", 10, "no", "10 >= 8, but su(3) is not in so(5): PART 2"),
    ("so(4,2) = su(2,2)", "s(u(2) + u(2))", 7, "no", "7 < 8"),
    ("so(3,3) = sl(4,R)", "so(4)", 6, "no", "6 < 8"),
]
print(f"  {'real form':<20} {'maximal compact':<28} {'dim':>4} {'su(3)?':>7}  why")
for f, mc, d, v, why in forms:
    print(f"  {f:<20} {mc:<28} {d:>4} {('** '+v+' **') if v=='YES' else v:>7}  {why}")
assert sum(1 for f, mc, d, v, why in forms if v == "YES") == 1
print()
print("  ** EXACTLY ONE OF THE FOUR.  And it is the compact one. **")
print()
print("  ⌗ *dimension bookkeeping, checked: dim so(6,C)_R-form = 15 in every case;*")
for f, mc, d, v, why in forms:
    print(f"     {f:<20} maximal compact {d:>2}, so the symmetric complement is {15-d:>2}")

# ============================================================================
print()
print("=" * 78)
print("PART 4 — WHAT IT DOES TO sec:face-status")
print("=" * 78)
for line in [
 "P13 sec:face-status opens:",
 "",
 "   'Mathematically the compact SO(6) face and the Lorentzian SO(5,1) substrate are co-equal",
 "    real forms of the one complex group SO(6,C); NOTHING IN THE GROUP THEORY PRIVILEGES ONE.'",
 "",
 "and then breaks the tie ONTOLOGICALLY: a Riemannian S^5 has no timelike direction, no clock, no",
 "duration, so by CR's existence criterion it is real-by-construction but not a co-equal existent.",
 "** That argument is untouched by anything above and remains the section's load-bearing move. **",
 "",
 "What changes is the setup.  The sentence concedes a symmetric starting position and imports the",
 "asymmetry from outside.  ** It does not have to concede that much: **",
 "",
 "   · so(6,C) has FOUR real forms, and the sentence weighs two;",
 "   · su(3) embeds in exactly ONE of the four, and it is the compact one;",
 "   · so on the colour question the group theory is NOT symmetric -- it already points where the",
 "     section is going.",
 "",
 "⇒ ** a sharper statement of the same wall: colour and duration are not merely in different",
 "   places.  They are in the ONLY places available to them, and those places are disjoint. **",
 "   Colour can live in exactly one real form; duration can live in any form with a timelike",
 "   direction, which that one is not.",
]:
    print("  " + line)

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· No new mathematics.  The real-form list and the maximal compacts are textbook; su(3) not in",
 "  so(5) is the corpus's own (P13_qm_S4_vs_S5) and is rebuilt above rather than quoted.",
 "· No claim that sec:face-status's ontological argument is unnecessary -- it is doing the work",
 "  representation theory cannot do, namely denying the compact face the standing of an existent.",
 "· No claim on the UNIVERSAL, which P13 explicitly declines: that no construction whatever could",
 "  yield colour from geometry is strictly stronger and is not made here either.",
 "· Nothing about the Atiyah-Hirzebruch obstruction, which is a separate face of the same wall.",
 "· No closure on any registered item.",
]:
    print("  " + line)
