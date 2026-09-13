"""
P17_the_budget_has_three_entries_and_one_has_split
==================================================

Object under test -- `p0`'s free-data budget, read against what this session and node `65`'s
arc have done to it.  ** The question is whether the budget has shrunk, and the honest answer is
that one entry has SPLIT rather than closed. **

--------------------------------------------------------------------------------
(1) WHAT `p0` ACTUALLY SAYS, WHICH IS MORE THAN "TWO ENTRIES".

"the theory's entire free-data budget -- the one measured rho_r/rho_m and the fermion sector's
own content -- is carried by the matter."  And then, at the discrete rung: the generation
multiplicity, the chirality and the family symmetry "is forced within CR, drawn from the
substrate rather than tuned, so it leaves the free-data budget for the residue; ** the budget
then carries the fermion CONTENT alone -- the gauge assignment and the mass values, the ordinary
route, whose deeper structure is the open search. **"

  ==> ** THREE entries, and p0 names them: rho_r/rho_m, the gauge assignment, the mass values. **
      The discrete structure has already left.

--------------------------------------------------------------------------------
(2) AND THE GAUGE-ASSIGNMENT ENTRY HAS SPLIT, WHICH IS THE FINDING.

`P14` factors the twelve coloured legs by the corpus's OWN sheet index -- 3 (graze point) x 2
(horn) x 2 (ruling, R-graded) = 12 -- and reads them against the Standard Model as colour x weak
isospin x chirality, ** with multiplicities agreeing state by state **, four legs per graze point
against u_L, d_L, u_R, d_R at three each.  And the leg naming is not fitted: `P03` already
records sigma -> colour, T -> weak isospin, R -> chirality.

  ** So twelve of the fifteen ARE delivered, with their factors identified. **  And the missing
  three are not merely absent: r6545 traces the absence to the welding of unbranchedness to the
  colour index, which holds iff the hinge count is ODD, hence in EVEN D -- ** so the shortfall is
  the D = 4 result read from the matter side. **

  ==> *** The entry splits into a DELIVERED part and an EXPLAINED ABSENCE.  Neither half is free
      data any longer, and neither half is a derivation of the missing content. ***

--------------------------------------------------------------------------------
(3) AND THE MASS-VALUES ENTRY IS TRACED AND STILL FREE.

r6467 established that a Dirac eigenvalue on the Euclidean face is not a four-dimensional mass,
by either route -- no product for a separation, and no time for a mass to be the eigenvalue OF.
** That says the masses do not come from the face's geometry.  It does not say what they do come
from. **

  ==> *** Tracing where something is NOT fixed is not fixing it. ***  The entry has changed
      character -- it is no longer "somewhere in the fermion sector", it is "outside the face's
      geometry" -- and it remains free.

--------------------------------------------------------------------------------
⇒ (4) SO THE BUDGET HAS NOT SHRUNK TO ONE, AND SAYING SO WOULD BE THE FLATTERING READING.

    rho_r/rho_m        ONE MEASURED NUMBER, free, untouched by any of this
    gauge assignment   SPLIT: twelve delivered factor by factor; three absent, and the
                       absence traced to D = 4
    mass values        TRACED out of the face's geometry, and still FREE

  ** One entry of three is closed in the sense that nothing in it is now unaccounted; one is
  untouched; one is relocated. **  *** The budget is smaller in structure and the same in
  count. ***

⚠ WHAT THIS IS NOT.  Not a claim that the twelve's delivery derives the Standard Model's gauge
group -- `P14` matches factors against it and says so.  Not a claim that the mass values are
closer to being fixed.  ** And not a claim that the budget is one entry, which is what this
reading was opened to test and what the material does not support. **
"""

# --- (1) p0's three entries -------------------------------------------------------
BUDGET = {
    'rho_r/rho_m': 'one measured number',
    'gauge assignment': 'the ordinary route',
    'mass values': 'the ordinary route',
}
LEFT_ALREADY = ('generation multiplicity', 'chirality', 'family symmetry')
assert len(BUDGET) == 3, "p0 names three entries once the discrete structure has left"
assert len(LEFT_ALREADY) == 3, "and three things that left it"
print("  p0's budget, after the discrete structure leaves:")
for k, v in BUDGET.items():
    print(f"    {k:<20} {v}")

# --- (2) the twelve factor by the corpus's own indices ----------------------------
FACTORS = {'graze point -> colour': 3, 'horn -> weak isospin': 2, 'ruling (R) -> chirality': 2}
_prod = 1
for v in FACTORS.values():
    _prod *= v
assert _prod == 12, f"the coloured twelve must factor 3x2x2, got {_prod}"
assert 15 - _prod == 3, "and the colourless remainder is three"
print(f"\n  the twelve factor {' x '.join(str(v) for v in FACTORS.values())} = {_prod}; "
      f"15 - {_prod} = {15 - _prod} colourless")

# --- (3) and the welding that explains the three is a parity statement -------------
def _welded(hinge_count):
    return hinge_count % 2 == 1


assert _welded(3) and not _welded(2) and not _welded(4), \
    "the welding holds for ODD hinge count, and D-1 = 3 at D = 4"
print("  the missing three: welded at odd hinge count, D-1 = 3 at D = 4      OK")

# --- (4) the budget's state, entry by entry ----------------------------------------
STATE = {
    'rho_r/rho_m': 'FREE -- untouched',
    'gauge assignment': 'SPLIT -- twelve delivered, three absent and the absence traced to D=4',
    'mass values': 'TRACED out of the face, and still FREE',
}
_free = [k for k, v in STATE.items() if 'FREE' in v]
assert len(_free) == 2, f"two entries remain free, got {_free}"
assert 'SPLIT' in STATE['gauge assignment'], "one entry has split rather than closed"
print("\n  the budget's state:")
for k, v in STATE.items():
    print(f"    {k:<20} {v}")
print(f"\n  -> {len(_free)} of {len(STATE)} entries still free.  The budget is smaller in")
print("     STRUCTURE and the same in COUNT.                                  OK")

print()
print("ESTABLISHED: p0 names THREE budget entries once the discrete structure has left, and the")
print("gauge-assignment entry has SPLIT -- twelve delivered factor by factor, three absent with")
print("the absence traced to D=4 -- while the mass values are traced out of the face and remain")
print("free, and rho_r/rho_m is untouched.")
print("NOT ESTABLISHED: that the budget is down to one entry. That is the flattering reading and")
print("the material does not support it -- tracing where something is not fixed is not fixing it.")
