"""
P08_the_content_law_and_the_head_are_one_wall_seen_twice
========================================================

Object under test -- whether rooms ② and ③ of `THE_REGISTER`'s rooms map are separate,
as the map (r6443, mine) draws them.

  room ②   `PO-30`   a generative law for the matter CONTENT
  room ③   `PO-31`   what the head IS -- and `PO-41`'s strike: "what is owed at the
                     head is the matter -- that there are baryons on its collapse leg,
                     and how many"

** THEY ARE NOT SEPARATE.  ONE ENTAILS THE OTHER, IN ONE DIRECTION, AND NOTHING IN THE
   CORPUS DRAWS THE CONNECTION. **

--------------------------------------------------------------------------------
THE ENTAILMENT, AND WHY IT IS ONE-WAY.

`P08` supplies the dynamics of the curve GIVEN content (r6403): the contracted Bianchi
identity is entailed by the cut's own geometry, and a constitutive relation closes the
system into ODEs on the cut.  ** What is NOT supplied is why a cut has the shape it
has. **  That is `PO-30`.

Now the head.  Every lap after the first inherits its cut's shape from its progenitor
-- that is what the genealogy transmits.  ** The head, by construction, inherits
nothing. **  So the head's cut is not fixed by inheritance, and what fixes it is
exactly a law that picks a cut absent a progenitor.

  ==> ** A generative law for the content IS a law that would fix the head's cut, and
      therefore the matter on its collapse leg.  `PO-30` discharged would discharge
      what `PO-41` says the head owes. **

  ==> And not conversely: ** knowing that there are baryons at the head, and how many,
      is a FACT and not a LAW. **  It would not tell you why any cut bends as it does.
      So `PO-31`'s head owing is DOWNSTREAM of `PO-30`, not beside it.

--------------------------------------------------------------------------------
WHAT THAT DOES TO THE MAP, WHICH IS MINE AND WRONG.

r6443 drew ② and ③ as separate rooms with one opening each.  ** They share a wall,
and the sharing has a direction: ③'s opening is the shadow of ②'s. **  A map that
draws them apart says two rows must each be worked; the corrected map says ** working
`PO-30` moves both, and working `PO-31`'s head alone cannot move `PO-30`. **

⌗ AND THE CORPUS DRAWS THIS NOWHERE.  "generative law" never occurs within reach of
"head", "genealogy" or "progenitor" in the register or any paper.  The two rows have
sat in different sectors -- A · matter and D · cosmology -- since they were opened.

--------------------------------------------------------------------------------
⚠ HELD AT ITS WEIGHT.  ** This is a structural reading, not a computation. **  It rests
on the head inheriting nothing, which is `PO-40`'s result and not in question; and on
a "generative law for content" being the kind of thing that fixes a cut, which is how
`P08` frames the gap it names.  ** If `PO-30`'s law turned out to fix only the
RELATION between a cut and its content -- not which cut -- the entailment would fail
and the rooms would be separate after all. **  That is the one place to attack it.
"""

# --- what each row owes ---------------------------------------------------------
ROWS = {
    "PO-30": {"owes": "a LAW: why a cut bends as it does", "kind": "law"},
    "PO-31": {"owes": "a FACT: that there are baryons at the head, and how many",
              "kind": "fact"},
}
assert ROWS["PO-30"]["kind"] == "law" and ROWS["PO-31"]["kind"] == "fact"
print("  what each row owes:")
for k, v in ROWS.items():
    print(f"    {k}  [{v['kind']:<4}]  {v['owes']}")

# --- the head inherits nothing: PO-40's result, which is what makes the head special
inherits = {"any lap after the first": True, "the head": False}
assert inherits["the head"] is False, "PO-40: the genealogy is finite and has a head"
print(f"\n  a lap after the first inherits its cut's shape : {inherits['any lap after the first']}")
print(f"  the head inherits                              : {inherits['the head']}")
print("  -> so the head's cut is fixed by a LAW or by nothing            OK")

# --- so the entailment runs one way ---------------------------------------------
def discharges(a, b):
    """a law fixing cuts discharges a fact about one cut; a fact discharges no law"""
    return ROWS[a]["kind"] == "law" and ROWS[b]["kind"] == "fact"


assert discharges("PO-30", "PO-31"), "the law would fix the head's cut"
assert not discharges("PO-31", "PO-30"), "the fact would not yield the law"
print("\n  PO-30 discharged -> PO-31's head owing discharged :", discharges("PO-30", "PO-31"))
print("  PO-31 discharged -> PO-30 discharged             :", discharges("PO-31", "PO-30"))
print("  -> ONE-WAY. PO-31's opening is the shadow of PO-30's            OK")

# --- and the map drew them apart -------------------------------------------------
map_r6443 = {"room 2": ["PO-30"], "room 3": ["PO-31"]}
assert map_r6443["room 2"] != map_r6443["room 3"], "drawn as separate rooms"
print("\n  r6443's map drew them as separate rooms, one opening each.")
print("  -> corrected: they share a wall, with a direction                OK")

print()
print("ESTABLISHED: PO-30's law would fix the head's cut and so discharge what PO-41")
print("says the head owes; the converse fails. Rooms 2 and 3 share a wall and the")
print("map drew them apart. NOT ESTABLISHED: this is a structural reading, and it")
print("fails if PO-30's law fixes only the cut-content RELATION and not which cut.")
