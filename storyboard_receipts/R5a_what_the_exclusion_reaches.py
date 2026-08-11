"""
R5, ROUTE (a): WHAT DOES P15's EXCLUSION REACH?  (r1117)  -- R5's last surface.

** THE ROUTE, as the ledger names it: ** "P15 excludes radiation from L1 only -- the stacking
rate -- 'because content is read off the clock the geometry sets, never summed into it.' That
is a statement about L1, and ** it leaves L2 and the field level entirely open **. A geometric
EM living at L2 would not contradict it; ** nobody has asked what P15's exclusion does or does
not reach. **"

** WHY THIS IS THE ONLY ROUTE LEFT. ** Routes (b) and (c) both died on the same type-check
(R5b): the corpus's two wave-instruments -- P11's TT shear and P11's polarization chirality --
are both SPIN-2, and ** the figure carries no spin-2 sector at all ** (the tensor is identically
zero; the rulings span a Lorentzian plane whose group is a boost, not a rotation). Both failed
on the FIGURE's content. ** Route (a) is about the CORPUS's levels, not the figure, so neither
failure touches it. **

** P15 AT SOURCE (read, not paraphrased): **
  abstract/intro: "the expansion rate is fixed by the cosmological constant alone, ** radiation
                   carries no term in it **, and the present matter density is a reading of the
                   cosmic epoch rather than an independent quantity"
  canon note    : "the OBSERVABLE rate is radiation-free sinh^{2/3} (Nariai proper frame, fixed
                   by Lambda, read LEFTWARD -- ** radiation and matter are inherited content
                   read off the clock, never terms that source the rate **; no
                   radiation-dominated era in the observable rate); ** the PROGENITOR/local
                   dynamics is ordinary GR at the standard Friedmann rate (where the
                   thermodynamics and BBN run) **; the two regimes are DISTINCT and meet at the
                   reassignment seam."

THE QUESTIONS:
  Q1  Does the exclusion reach L2? (The ledger says no. Check it at source.)
  Q2  ** If L2 is not excluded, is it EMPTY? ** -- because "not excluded" and "open" are not the
      same thing, and the ledger's route (a) quietly assumes they are.
  Q3  What would a geometric EM at L2 have to do?

COULD THIS RETURN OTHERWISE? Q1/Q2 are read off P15 and P16 at source. Q3 follows from what
they say. If L2 turns out empty, route (a) is wide open and R5 has a live surface; if L2 turns
out occupied, route (a) narrows to a constraint -- and which it is, is not mine to choose.
"""
import re, os

C = '../corpus/'
p15 = open(C+'CR_cosmology.tex').read()
p16 = open(C+'cosmogenesis_paper.tex').read()

print("="*80)
print("Q1 -- DOES THE EXCLUSION REACH L2?")
print("="*80)
print("""  The exclusion's own words: "radiation carries no term in IT" -- and "it" is ** the expansion
  rate **, the L1 stacking. And the canon note draws the line itself: "the OBSERVABLE rate is
  radiation-free... ** the PROGENITOR/local dynamics is ordinary GR at the standard Friedmann
  rate **; the two regimes are DISTINCT."

  ** So: NO. The exclusion is about the rate, and the rate is L1. The ledger's route (a) is
  correct on this point and it is now checked rather than asserted. **""")

print("\n" + "="*80)
print("Q2 -- ** BUT IS L2 EMPTY?  This is the question route (a) did not ask. **")
print("="*80)
hits = [m.start() for m in re.finditer(r"standard Friedmann rate|ordinary photon--baryon plasma|ordinary photon-baryon", p15+p16)]
both = p15 + p16
print(f"  occurrences of 'standard Friedmann rate' / 'ordinary photon--baryon plasma' in P15+P16: {len(hits)}")
for h in hits[:3]:
    seg = re.sub(r"\s+", " ", both[max(0, h-300):h+180])
    print(f"\n    ...{seg}...")
print("""
  ** L2 IS NOT EMPTY. IT IS OCCUPIED, AND OCCUPIED BY ORDINARY RADIATION. **
  P16's whole result runs there: the progenitor's collapse compresses adiabatically, heats above
  the deuterium bottleneck, re-expands, and cools back through it ** at the standard Friedmann
  rate ** -- and that cooling leg IS a standard BBN, producing helium-4 and deuterium at the
  observed values from one inherited eta. ** That computation requires radiation to be present
  at L2 and to source the rate there. It is not a gap in the corpus; it is one of the corpus's
  two data-confrontation results. **

      >>> "NOT EXCLUDED" IS NOT "OPEN". The ledger's route (a) says the exclusion "leaves L2 and
          the field level entirely open" -- and the first half is right while the second half is
          the slip: L2 is not excluded BECAUSE IT IS ALREADY FULL. <<<""")

print("\n" + "="*80)
print("Q3 -- SO WHAT WOULD A GEOMETRIC EM AT L2 HAVE TO DO?")
print("="*80)
m = re.search(r"conditional on the inherited medium being the ordinary photon--baryon plasma", p15)
if m:
    seg = re.sub(r"\s+", " ", p15[max(0, m.start()-380):m.start()+200])
    print(f"  P15, at source:\n    ...{seg}...")
print("""
  ** THE CONSTRAINT, AND IT IS SHARP. ** P15's peak-height result and P16's abundance result are
  both CONDITIONAL ON THE RADIATION BEING ORDINARY: the acoustic peaks match flat-LCDM's
  "conditional on the inherited medium being the ordinary photon--baryon plasma", and the
  abundances come out at observed values by ORDINARY nuclear physics on a STANDARD cooling leg.
  ** Those are the corpus's two empirical wins. ** So:

      >>> A GEOMETRIC DESCRIPTION OF ELECTROMAGNETIC RADIATION AT L2 WOULD NOT BE FREE TO BE
          ANYTHING. IT WOULD HAVE TO ** BE ** THE ORDINARY PHOTON--BARYON PLASMA -- reproducing
          it exactly, not replacing it -- because the corpus's two data-confrontations are
          staked on that plasma being ordinary. <<<

  ** That is not a refutation of R5 and it is not an opening for it. It is a BOUNDARY CONDITION
  the rhyme did not have before: ** route (a) is not "L2 is empty, put a geometric EM in it."
  It is "L2 is full of ordinary radiation that two empirical results depend on, and any
  geometric account must return exactly that." ** A geometric EM would be a re-derivation of
  ordinary electromagnetism from the substrate, not a new field. ** Which is a far harder and
  far more interesting thing to ask for -- and it is what the rhyme, read strictly, actually
  says: "there is a geometric DESCRIPTION of electromagnetic radiation in that." A description,
  not a replacement.""")

print("\n" + "="*80)
print("WHAT ROUTE (a) RETURNED -- and R5 is now closed on all three routes")
print("="*80)
print("""  ** ⊢ THE EXCLUSION REACHES L1 AND ONLY L1. ** "Radiation carries no term in IT" -- and "it"
  is the expansion rate. P15's canon note draws the line itself: the observable rate is
  radiation-free; ** the progenitor/local dynamics is ordinary GR at the standard Friedmann
  rate **; the two regimes are DISTINCT. ** The ledger's route (a) was right about this, and it
  is now checked at source rather than asserted. **

  ** ⊢ BUT "NOT EXCLUDED" IS NOT "OPEN", AND THAT IS THE FINDING. ** The ledger says the
  exclusion "leaves L2 and the field level ENTIRELY OPEN." The first half is right; the second
  is a slip. ** L2 is not excluded BECAUSE IT IS ALREADY FULL. ** P16's entire abundance result
  runs at L2: the collapse heats above the deuterium bottleneck and cools back through it at the
  standard Friedmann rate, and that cooling leg IS a standard BBN producing He-4 and D at
  observed values from one inherited eta. ** Radiation is present at L2 and sources the rate
  there. It is not a gap; it is one of the corpus's two empirical wins. **

  ** ⊢ SO ROUTE (a) IS NOT AN OPENING. IT IS A BOUNDARY CONDITION, and a sharp one: **
      >>> A geometric description of EM at L2 would have to ** BE ** the ordinary photon--baryon
          plasma -- reproducing it exactly, not replacing it -- because P15's peak-height match
          is explicitly "conditional on the inherited medium being the ordinary photon--baryon
          plasma" and P16's abundances come out by ORDINARY nuclear physics on a STANDARD
          cooling leg. Both of the corpus's data-confrontations are staked on that plasma being
          ordinary. <<<
  ** A geometric EM would be a RE-DERIVATION of ordinary electromagnetism from the substrate,
  not a new field. ** Which is harder and more interesting than the route as written -- and it
  is what the rhyme, read strictly, says: "there is a geometric ** DESCRIPTION ** of
  electromagnetic radiation in that." A description, not a replacement.

  ** R5, ALL THREE ROUTES, DONE: **
    (b),(c) ** CLOSED by one type-check: ** the corpus's two wave-instruments are spin-2 and the
            figure carries no spin-2 sector -- the tensor is identically zero, and the rulings
            span a Lorentzian plane whose group is a boost (real weight), not a rotation (a
            phase). Not "the branches are not waves": ** the instruments cannot be pointed at
            them. **
    (a)     ** CLOSED as an opening and RE-OPENED as a constraint: ** the exclusion reaches L1
            only, L2 is full of ordinary radiation, and any geometric account must return
            exactly that plasma.

  ** WHAT SURVIVES OF R5, STATED AT ITS WEIGHT: ** a real oscillation that is sinh's own (⊢64);
  a real Z_2 that is the cube root's monodromy and not a helicity (⊢65/⊢67); no spin-2 anywhere
  on the figure (R5b); and a sharpened target -- ** not "is there EM in the branches" but "can
  ordinary electromagnetism be re-derived from the substrate at L2, returning the photon--baryon
  plasma exactly?" ** ** The rhyme is returned to Daryl intact, with its three routes worked,
  its instruments type-checked, and its question sharper than it was. **""")
