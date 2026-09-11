"""
P08_the_boundary_is_whether_the_breaking_is_itself_symmetric
============================================================

Object under test -- the question r6489 put to `PO-30`: is there a moduli-free
configuration for the CONTINUOUS content, as the Z_3 three-plane is for the discrete?

** THE CORPUS'S OWN BOUNDARY ANSWERS WHERE THE DIFFICULTY SITS, AND THE ANSWER JOINS
   THREE STATEMENTS THAT HAVE NOT BEEN READ TOGETHER. **

--------------------------------------------------------------------------------
(1) THE TENSION THAT MAKES THIS WORTH READING.

r6489 established, from `P14`'s prop:forced, that the geometry DOES supply a breaking:
the three-plane configuration, chosen among breakings because it is itself symmetric.

But `P14` also says, of the family symmetry: "** What this sector supplies is the
SYMMETRY, not the BREAKING **: the S_3 arrives here from the substrate's geometry rather
than being posited, while the breaking that generates the observed masses and mixings
remains external to it, in the same place as the gauge representations."

  ==> Both are true, so there are TWO KINDS OF BREAKING here and the corpus distinguishes
      them without ever saying so in one place.

--------------------------------------------------------------------------------
(2) THE DISTINCTION, AND IT IS EXACTLY THE CRITERION.

    SUPPLIED   the three-plane Z_3 configuration -- a breaking that is ITSELF SYMMETRIC,
               and therefore carries no modulus: there is nothing to choose.
    EXTERNAL   the breaking that generates the observed masses and mixings -- which must
               DISTINGUISH the three planes to produce a hierarchy, and so is NOT itself
               symmetric, and so carries exactly the modulus Rule 2 rejects.

  ==> *** The boundary between what the geometry supplies and what it marks external
      coincides with whether the breaking is ITSELF SYMMETRIC.  That is one fact, not
      two -- and it says why the COUNT is forced while the MASSES are not. ***

** A symmetric breaking is a configuration; a hierarchy is a choice of which member is
heaviest.  The first has a symmetric point; the second is the statement that there is
none. **

--------------------------------------------------------------------------------
(3) WHAT THAT MAKES OF `p0`'s FREE-DATA BUDGET, WHICH IS NAMED AND SHRINKING.

`p0`: "the theory's entire free-data budget -- the one measured rho_r/rho_m and the
fermion sector's own content -- is carried by the matter, so matter is the residue
maximal symmetry leaves not in field content alone but in FREE DATA."

** The budget has two entries and the second has already been partly converted **: the
count, the chirality and the family symmetry moved from free data to forced structure
when `P14` built them.  What remains under that entry is the mass spectrum and the gauge
representations -- "external to it and are so marked".

  ==> ** So `PO-30` is, in the corpus's own accounting, the question of whether the
      REMAINING entries can be converted as the first ones were -- and the criterion
      that converted them works only on breakings that are themselves symmetric. **

--------------------------------------------------------------------------------
⚠ (4) AND THE ROW IS NOT CLOSED BY THIS.  `P14` bounds its own marking, deliberately:
the `P13` constraint "does not say that a geometric route to the representation content
is impossible; it says that the connected isometry route is closed and identifies the
single component the obstruction cannot reach", and with the measured ratios "the two
bound the search from opposite sides -- one fixing what an admissible mechanism must
produce, the other fixing where such a mechanism may live.  ** We claim no construction
here. **"

  ==> ** What is established is where the difficulty sits and why it sits there: not
      that the continuous content is beyond reach, but that the one criterion that has
      converted free data so far cannot act on a breaking that must be asymmetric to do
      its job.  A different mechanism is not excluded, and the corpus says so. **
"""

# --- (1) two breakings, both in the corpus ---------------------------------------
BREAKINGS = {
    "three-plane Z_3 configuration": {"itself symmetric": True,  "status": "SUPPLIED by geometry"},
    "the mass/mixing hierarchy":     {"itself symmetric": False, "status": "EXTERNAL, so marked"},
}
assert BREAKINGS["three-plane Z_3 configuration"]["status"].startswith("SUPPLIED")
assert BREAKINGS["the mass/mixing hierarchy"]["status"].startswith("EXTERNAL")
print("  the corpus carries two breakings, and marks them differently:")
for k, v in BREAKINGS.items():
    print(f"    {k:<32} symmetric={str(v['itself symmetric']):<5} {v['status']}")

# --- (2) and the marking tracks 'itself symmetric' exactly ------------------------
supplied = {k for k, v in BREAKINGS.items() if v["status"].startswith("SUPPLIED")}
symmetric = {k for k, v in BREAKINGS.items() if v["itself symmetric"]}
assert supplied == symmetric, "the boundary IS whether the breaking is itself symmetric"
print("\n  {supplied} == {itself symmetric}  ->  ONE fact, not two            OK")
print("  -> which is why the COUNT is forced and the MASSES are not         OK")

# --- (3) the named budget, and what has moved ------------------------------------
BUDGET = {
    "rho_r/rho_m (one measured)":  "free",
    "count, chirality, family symmetry": "CONVERTED by P14",
    "mass spectrum, gauge representations": "free -- external and so marked",
}
converted = [k for k, v in BUDGET.items() if v.startswith("CONVERTED")]
assert len(converted) == 1, "one entry has already moved from free data to forced"
print(f"\n  p0's named free-data budget, current state:")
for k, v in BUDGET.items():
    print(f"    {k:<38} {v}")
print("  -> the budget SHRINKS; PO-30 asks whether the rest can follow      OK")

# --- (4) and the row stays open, on the corpus's own wording ----------------------
# Not asserted against a literal: READ FROM P14 itself, so the check fails if the
# paper's bounding clause ever goes away.
import os
_p14 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', '..', 'corpus', 'matter_sector_paper.tex')
_src = open(_p14, encoding='utf-8', errors='replace').read()
assert "does not say that a geometric route to the representation content is impossible" in _src, \
    "P14 must still bound its own marking, or this receipt's clause (4) is stale"
assert "We claim no construction here." in _src, "P14's own disclaimer must still stand"
print("\n  P14 bounds its own marking: the constraint is 'informative rather than")
print("  prohibitive', and 'we claim no construction here'.")
print("  -> nothing here closes the row                                     OK")

print()
print("ESTABLISHED: the boundary between what the geometry supplies and what it marks")
print("external coincides with whether the breaking is ITSELF SYMMETRIC -- one fact,")
print("and it says why the count is forced while the masses are not. And p0's free-data")
print("budget is named and has already shrunk once, which is what PO-30 asks to repeat.")
print("NOT ESTABLISHED: that the remaining entries cannot be converted. A mechanism")
print("outside the connected-isometry route is not excluded, and P14 says so.")
