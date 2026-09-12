"""
P03_the_last_two_openings_await_the_same_interior
=================================================

Object under test -- whether `PO-25`'s remaining condition is reachable on its own
terms, asked after the instruments were checked and reported nothing else owed.

--------------------------------------------------------------------------------
(1) THE INSTRUMENTS SAY NOTHING ELSE IS OWED.  `check_burndown`: the lead register is
15 struck, 0 open, ID space intact from 1 to the maximum.  `check_unworked_blockers`,
`check_gap_is_held`, `check_deferrals_resolve`, `check_close_names_work`: all clean.
`FOR_56` item 16 (the prefix bands) is REPORTED and not failed, awaiting 56's adoption
-- a person-gate, not work.  ** So the PO- frontier is the live surface and the question
is which of its openings can actually be reached. **

--------------------------------------------------------------------------------
(2) AND `PO-25`'s CONDITION IS A MODELLING TASK, NOT A READING.

r6521 sharpened it to: does the interior mass function stay m(r) = o(1/r) as r -> 0?
** Answering that requires evolving the charged interior, and evolving it requires
matter. **  `P08` states exactly what the construction does and does not supply: the
dynamics GIVEN content is supplied -- the contracted Bianchi identity entailed, a
constitutive relation closing the system into ODEs on the cut -- and *** what is not
supplied is the constitutive relation. ***

  ==> So m(r) near the origin is not determined by the geometry.  It is determined by
      the matter one puts in it.

--------------------------------------------------------------------------------
(3) AND THAT IS THE SAME THING `PO-31`'s REMAINDER AWAITS, IN ITS OWN WORDS.

`PO-31`: the progenitor spectrum is "** a modelling task awaiting a progenitor
interior **".  `PO-25`: what stands in the horizon's place is the dynamical interior's
question.  ** Two rows in two different rooms, both waiting on an interior evolution
that the construction does not hand them. **

  ⌗ AND THE DISTINCTION FROM `PO-30` IS WORTH KEEPING SHARP.  `PO-30` wants a
  GENERATIVE LAW for the content -- why a cut carries what it carries.  ** These two
  want less: a matter MODEL, chosen rather than derived, and an evolution run with it.
  A model would answer them and would not answer `PO-30`. **  So they are not
  downstream of `PO-30`; they are downstream of a modelling step nobody has taken.

--------------------------------------------------------------------------------
⇒ (4) WHAT THIS SAYS ABOUT WHERE TO WORK.

** Neither of the two openings that look nearest is a reading. **  Both are runs of a
kind the corpus has not set up: an interior evolution with a chosen matter model, which
is a different sort of object from the mode sums and likelihood fits the Code node has
been given.

  ⌗ *** This is not a reason to work them badly from here. ***  It is the reason
  `PO-30` keeps being the row that matters: it is the only one of the three whose
  question is answerable without first choosing something arbitrary, and the other two
  would each be answered FOR a choice rather than answered.

⚠ NOT CLAIMED: that a modelling run would be worthless.  A chosen equation of state
would settle whether m(r) = o(1/r) FOR THAT MATTER, which is a real answer to a real
question -- and `P08`'s own point is that general relativity does not supply the
equation of state either.  ** What is claimed is only that it is a run with an input,
not a reading of what the corpus already holds. **
"""

# --- (1) what the instruments report ---------------------------------------------
INSTRUMENTS = {
    'check_burndown': '15 struck, 0 open, ID space intact',
    'check_unworked_blockers': 'no open row carries an unrevisited blocker',
    'check_gap_is_held': "every open row's object is present in the map",
    'check_deferrals_resolve': "every 'not done here' points somewhere",
    'check_close_names_work': 'no struck row rests on a failing receipt',
}
assert all(v for v in INSTRUMENTS.values())
print('  the owed-work instruments, all clean:')
for k, v in INSTRUMENTS.items():
    print(f'    {k:<26} {v}')

# --- (2) what PO-25's condition needs ---------------------------------------------
SUPPLIED = ('the contracted Bianchi identity', 'the ODE system on the cut given content')
NOT_SUPPLIED = ('the constitutive relation',)
assert 'the constitutive relation' in NOT_SUPPLIED
assert not set(SUPPLIED) & set(NOT_SUPPLIED)
print(f"\n  P08 supplies: {'; '.join(SUPPLIED)}")
print(f"  P08 does NOT supply: {NOT_SUPPLIED[0]}")
print("  -> m(r) near the origin is set by the matter, not by the geometry   OK")

# --- (3) and PO-31's remainder awaits the same ------------------------------------
AWAITING = {
    'PO-25': 'the dynamical interior (what stands in the horizon place)',
    'PO-31': 'a progenitor interior (a modelling task, in the row own words)',
}
assert len(AWAITING) == 2 and all('interior' in v for v in AWAITING.values())
print(f"\n  two rows, two rooms, both awaiting an interior:")
for k, v in AWAITING.items():
    print(f'    {k}  {v}')

# --- and the distinction from PO-30 -----------------------------------------------
WANTS = {'PO-30': 'a generative LAW for the content',
         'PO-25': 'a matter MODEL, chosen, and an evolution',
         'PO-31': 'a matter MODEL, chosen, and an evolution'}
law = [k for k, v in WANTS.items() if 'LAW' in v]
model = [k for k, v in WANTS.items() if 'MODEL' in v]
assert law == ['PO-30'] and sorted(model) == ['PO-25', 'PO-31']
print(f"\n  PO-30 wants a LAW; PO-25 and PO-31 want a MODEL.")
print("  -> a model answers those two and does NOT answer PO-30, so they are")
print("     not downstream of it -- they are downstream of a modelling step    OK")

print()
print("ESTABLISHED: nothing else is owed by the instruments; PO-25's condition and")
print("PO-31's remainder both await an interior evolution with chosen matter, which is")
print("a run with an input rather than a reading; and PO-30 remains the only one of the")
print("three answerable without first choosing something arbitrary.")
print("NOT CLAIMED: that such a modelling run would be worthless -- it would answer FOR")
print("a choice, which is a real answer to a real question.")
