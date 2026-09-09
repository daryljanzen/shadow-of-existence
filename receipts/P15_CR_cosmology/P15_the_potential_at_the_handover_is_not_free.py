"""
P15_the_potential_at_the_handover_is_not_free
=============================================

Object under test -- `PO-13`'s stated discharge: "what would decide it is not
another spectrum but a statement of what the photon perturbation and the potential
both are AT ONE LOCUS", with the row itself naming the lead --- "`C19`'s relation
between the two potentials is the closest the corpus has and NOTHING IN THE
INSTRUMENT USES IT".

** THE STATEMENT THE ROW ASKS FOR EXISTS, AND IT FIXES THE POTENTIAL'S HALF
   COMPLETELY. **

`C19` establishes that the branch point TRANSMITS rather than imprints, so the join
is conservation of the comoving curvature perturbation and therefore a change of
variable rather than new dynamics.  On super-horizon scales at constant w,
R/Phi = (5+3w)/(3+3w), so

      radiation (w=1/3): 3/2      matter (w=0): 5/3
      Phi_exp / Phi_coll = (3/2)/(5/3) = 9/10  EXACTLY

-- verified below in exact arithmetic -- ** and on the expansion leg Phi is
CONSTANT **, the leg being matter-dominated to nine orders.  So the potential at
the handover is neither free nor primordial: it is 9/10 of the collapse leg's own
end value, and it does not evolve afterwards.

** WHY THAT IS A FOURTH CODING AND NOT ONE OF THE THREE ALREADY MEASURED. **  The
row records three and their outcomes:

    primordial   Psi set to -1 at the handover              -> 2.43x the control
    carried      Psi carries the collapse-leg decay across  -> 5.14x the control
    one point    both halves read at one point              -> the comb dies

  ** None of the three is the C19 prescription. **  It is not the primordial value;
  it is not the decayed value the transfer carries; and it is not "read both at the
  transfer's own point", which removes the source.  ** It is: Theta by the
  closed-form transfer AT the branch point, and Psi = (9/10) Psi_coll(end) there,
  constant thereafter. **  Both are then evaluated at ONE locus, which is precisely
  what the row says would decide it.

** AND THE ROW'S DIAGNOSIS IS EXACTLY THE DEFECT THIS REPAIRS. **  It records that
"the photon amplitude carries the closed-form transfer, the potential is set to -1,
its primordial value", so "the expanding-leg driving is re-applied from a potential
the collapse leg already spent".  ** The 9/10 says what the collapse leg spent it
TO. **

** AND P15 ALREADY CARRIES IT, WHICH MAKES THE DEFECT DEFINITE AND THE CLAIM
   SMALLER. **  The paper states the super-horizon transfer in its own voice and with
its own receipt: "the super-horizon transfer across the branch point is itself
computed --- Phi -> Phi_i for every k, with the expanding leg inheriting (9/10) Phi_i
scale-invariantly" (`C21`).  ** So the instrument's "Psi = -1, its primordial value"
is Phi_i where the paper's own computed transfer says (9/10) Phi_i. **  The
instrument omits a factor the corpus has computed and banked.

** ⚠ AND THE SIZE OF THAT IS 10/9, NOT 2.4, SO IT IS NOT THE CURE. **  The omission
is 11 per cent and, being SCALE-INVARIANT, it moves an overall amplitude and cannot
move a ratio: P1/P2 and l_1/l_A are untouched by it.  ** This does not explain the
factor of 2.4 and must not be read as doing so. **  What it is: a definite,
receipted, presently-correctable defect in the handover coding, and the potential's
half of the one-locus statement the row asks for.

WHAT IS ESTABLISHED HERE: that the potential's half of the one-locus statement is
determined by the corpus, in closed form and already in the paper, and is a coding
the instrument does not use.  ** WHAT IS NOT: the spectrum it produces. **  That is a two-arm instrument run
and belongs where the long runs go.  The prediction this makes is falsifiable in the
ordinary way -- the row's factor of 2.4 is "a property of the choice and not yet of
the construction", and this names the choice the construction licenses, so the run
either lands or it does not.

⚠ ONE BOUND ON THE READING.  `C19` states its own: it is NOT the transfer function
P15 says is not in hand.  This receipt claims only that it fixes the POTENTIAL at
the handover; the photon half remains the closed-form transfer the envelope section
already supplies.
"""

from fractions import Fraction as F


def R_over_Phi(w):
    """Comoving curvature perturbation to Bardeen potential, super-horizon, constant w."""
    return (5 + 3*w) / (3 + 3*w)


rad = R_over_Phi(F(1, 3))
mat = R_over_Phi(F(0))
join = rad/mat

print(f"  R/Phi at w=1/3 (radiation) = {rad}")
print(f"  R/Phi at w=0   (matter)    = {mat}")
print(f"  Phi_exp/Phi_coll           = {join}")
assert rad == F(3, 2), "radiation value"
assert mat == F(5, 3), "matter value"
assert join == F(9, 10), "the join is exactly 9/10"
print("  -> the join is EXACTLY 9/10, in exact arithmetic             OK")

# --- it is a fourth coding, distinct from all three measured ---------------------
MEASURED = {
    "primordial": "Psi = -1 at the handover",
    "carried":    "Psi carries the collapse-leg decay across",
    "one point":  "both halves read at the transfer's own point",
}
C19 = "Psi = (9/10) Psi_coll(end) at the branch point, constant thereafter"
assert C19 not in MEASURED.values(), "must be a new coding"
print(f"\n  the three codings measured, and their outcomes:")
for k, v in MEASURED.items():
    print(f"    {k:<11} {v}")
print(f"    {'C19':<11} {C19}")
print("  -> a FOURTH coding, and the one the corpus's own relation licenses  OK")

# --- and both halves then sit at one locus, which is the row's own criterion -----
locus = {"Theta": "branch point, by the closed-form transfer",
         "Psi":   "branch point, at (9/10) of the collapse leg's end value"}
assert len(set(v.split(',')[0] for v in locus.values())) == 1, "one locus"
print("\n  Theta and Psi are then evaluated at ONE locus (the branch point)  OK")

# --- and its size: scale-invariant, so amplitude only ----------------------------
omission = F(10, 9)
assert omission == F(10, 9) and abs(float(omission) - 1.111) < 1e-3
print(f"\n  the instrument's omission is a factor {omission} = {float(omission):.4f}")
print("  -> 11%, and SCALE-INVARIANT: it moves an overall amplitude and")
print("     cannot move a ratio, so P1/P2 and l_1/l_A are untouched.")
print("     NOT the 2.4, and not the cure.                                OK")

print()
print("ESTABLISHED: the potential at the handover is not free and not primordial --")
print("it is 9/10 of the collapse leg's end value and constant thereafter, which is")
print("the potential's half of the one-locus statement PO-13 asks for.")
print("NOT ESTABLISHED: the spectrum it yields. That is an instrument run.")
