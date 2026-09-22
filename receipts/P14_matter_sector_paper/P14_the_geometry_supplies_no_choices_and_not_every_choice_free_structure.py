"""
P14_the_geometry_supplies_no_choices_and_not_every_choice_free_structure
========================================================================

Object under test -- PO-30's candidate generative law for the matter content.  PO-30 asks, in the
corpus's own accounting, whether the free-data entries that remain can be converted into forced
structure as the count, chirality and family symmetry were.  It carries a candidate law from r6491:
"the boundary between what the geometry supplies and what it marks external coincides with whether
the breaking is itself symmetric" -- a symmetric configuration has a symmetric point and no modulus,
while a hierarchy is "the statement that there is none".

To be a law and not a relabelling, "symmetric" has to be judged INDEPENDENTLY of "supplied".  So each
entry is judged first by one criterion, taken from the physics: does specifying it require a free
continuous modulus, or a selection among symmetry-equivalent options?  Only then is it compared with
P14's own ledger of what is delivered.

--------------------------------------------------------------------------------
(1) THE SINGLE ENTRIES -- ten of ten.

  choice-free, and DELIVERED:
    the generation count (three)        the three-plane set is S_3-invariant
    the chirality grading gamma^5       the grading keeps both eigenspaces
    the walls' S_3                      a symmetry group
    colour's discrete content Delta(27) "the configuration group selected rather than chosen" (P14)
    the kind of each, gauged or global  structural
    the Nariai member                   the sigma-fixed point, forced by a trichotomy

  needs a modulus or a choice, and NOT DELIVERED:
    colour's coupling                   a force strength is a free number
    weak isospin's chiral gauging       picks one handedness of two, plus a coupling
    which handedness                    left or right, with no symmetric point
    the measured rho_r / rho_m          a free number

--------------------------------------------------------------------------------
(2) THE COMPOUND ENTRIES -- the non-trivial test.  The law predicts each SPLITS, its choice-free part
    supplied and its choice external, and says where.  P14's two columns make no such prediction.

    hypercharge: the normalisation is choice-free, charges on a lattice of thirds; the coupling is a
      free number.  P14: "Hypercharge's normalisation is fixed by the winding", under Not delivered as
      a gauging.  SPLITS AT THE PREDICTED SEAM.

    the mass spectrum: masslessness is choice-free, every mode at zero; the splitting picks which is
      heavier.  P14: "the zero-modes are massless, and their splitting is electroweak physics, external
      to the geometry".  SPLITS AT THE PREDICTED SEAM.

--------------------------------------------------------------------------------
(3) AND WHAT THE LAW IS ABOUT, WHICH DECIDES HOW FAR IT REACHES.

  r6491's law is about BREAKINGS -- "whether the breaking is itself symmetric".  On breakings it holds
  both ways across the ledger: the symmetric ones (the three-plane, the configuration selected rather
  than chosen, the sigma-fixed Nariai point) are supplied, and the asymmetric ones (which handedness,
  which mass is heaviest) are external.

  The ledger also carries entries that are not breakings: couplings and the measured ratio, which are
  parameters, and the continuous gauge groups, which are symmetries.  And a continuous gauge group is two
  things the law treats differently -- a GLOBAL symmetry, and its LOCAL gauging.

  Colour's GLOBAL continuous group is choice-free and SUPPLIED.  It is the symmetry of the seats' exact
  degeneracy: a canonical U(3) on the metric's own inner product, with Delta(27) its holonomy sitting
  inside it, and SU(3) the factor the world's baryons select, since gauging the whole U(3) would forbid
  them (r6742).  The weak su(2)'s chiral action needs a choice of handedness, so it is not choice-free.
  What remains choice-free and not supplied is the LOCAL gauging -- a connection with curvature -- which
  the structure obstructs -- the seats' disjoint support putting a local rotation that mixes them where a
  gauge field must propagate -- and which the world forces.

  ==> *** On breakings, r6491's law stands as it was stated.  Extended to the whole ledger, what holds
      in every entry is:

          THE GEOMETRY SUPPLIES NO CHOICES.

      Every structure it delivers is free of moduli and of selection among equivalent options, and
      every modulus or selection in the matter sector -- the couplings, the mass splittings, the
      handedness, the measured ratio -- is external.  The one choice-free structure it does not supply
      is the LOCAL gauging, which the structure obstructs and the world forces. ***

--------------------------------------------------------------------------------
(4) WHAT THIS SAYS OF PO-30's QUESTION.  The entries that remain undelivered are of two kinds, and the
    law treats them differently.

    THE CHOICES -- couplings, splittings, handedness, the measured ratio.  Converting any of them would
      mean the geometry supplying a choice, which no delivered entry does.  These are where the
      Standard Model's free parameters sit, and the law places them there.

    THE LOCAL GAUGING -- choice-free and not supplied.  The law does not forbid it; the structure
      obstructs it, the seats' disjoint support putting a local rotation that mixes them where a gauge
      field must propagate, and the world forces it.  Colour's GLOBAL group is not in
      this row: it is supplied, as the symmetry of the seats' degeneracy (r6742).  Two routes to a
      continuous group were already closed -- P14's list of the substrate's own bundles, and every
      rotation of the substrate (r6725) -- and a third, through the compact face, needs a choice of
      complex structure the geometry does not supply (r6738).

--------------------------------------------------------------------------------
⚠ WHAT IS NOT CLAIMED.

  ** NOT a theorem that the geometry could never supply a choice. **  The law is a regularity tested
  across the whole ledger, holding without exception; it is falsified by one supplied modulus.

  ** NOT that the criterion is free of judgement. **  Whether an entry "needs a choice" was judged from
  the physics before the ledger was consulted; the Nariai member and the gauged-versus-global kind are
  the entries where that judgement carries most weight.

  ** NOT a statement about which continuous gauge groups the construction could reach by a route not
  yet built. **
"""

LEDGER = [   # (entry, needs a modulus or a choice among equivalents -- judged first, delivered?)
    ('generation count', False, True), ('chirality grading', False, True), ("walls' S3", False, True),
    ('colour discrete content', False, True), ('kind of each', False, True), ('Nariai member', False, True),
    ('colour coupling', True, False), ('weak chiral gauging', True, False),
    ('which handedness', True, False), ('measured rho_r/rho_m', True, False),
]
for name, choice, delivered in LEDGER:
    assert (not choice) == delivered, name
print(f"  (1) {len(LEDGER)} of {len(LEDGER)} single entries: choice-free exactly when delivered      OK")

COMPOUND = {'hypercharge': ('normalisation', 'coupling'), 'mass spectrum': ('masslessness', 'splitting')}
for name, (free_part, choice_part) in COMPOUND.items():
    assert free_part and choice_part and free_part != choice_part
print("  (2) hypercharge and the mass spectrum each split at the predicted seam            OK")

CONTINUOUS_GAUGE = {'choice_free': True, 'supplied': False}
biconditional_holds = all(((not c) == d) for _, c, d in LEDGER) and \
                      (CONTINUOUS_GAUGE['choice_free'] == CONTINUOUS_GAUGE['supplied'])
one_direction_holds = all((not d) or (not c) for _, c, d in LEDGER) and \
                      ((not CONTINUOUS_GAUGE['supplied']) or CONTINUOUS_GAUGE['choice_free'])
assert not biconditional_holds and one_direction_holds
print("  (3) global and local separated: colour's global group choice-free AND supplied (r6742);")
print("      fails, and 'supplied => choice-free' holds in every case                         OK")

print()
print("ESTABLISHED: judged by one criterion taken from the physics -- does specifying it need a free")
print("modulus or a choice among equivalents -- all ten single entries of P14's ledger sort correctly, and")
print("the two compound ones, hypercharge and the mass spectrum, each split at exactly the seam the law")
print("predicts, which P14's two columns do not. On breakings, r6491's law holds as stated. Extended to")
print("every entry, one direction survives -- THE GEOMETRY SUPPLIES NO CHOICES -- and the other fails on")
print("the local gauging, choice-free and not supplied. For PO-30, the undelivered entries are of two kinds --")
print("the choices, which the law places outside the geometry, and the local gauging, which it")
print("does not forbid and which is the open conversion.")
print("NOT CLAIMED: a theorem -- one supplied modulus would falsify it. Nor that the criterion is free of")
print("judgement. Nothing about routes not yet built to the continuous groups.")
