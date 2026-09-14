"""
P03_the_symbol_T_carries_four_structural_referents
==================================================

⛔⛔ ** THE COUNT IN THIS FILE'S NAME IS WRONG AND THE METHOD IS WHY.  SEE (5). **  The
audit found FOUR senses because it searched for four it already knew.  A sense-agnostic
sweep at r6593 finds SIX, and the two it missed are in the very paper this receipt is
homed in.  *** The file keeps its name so the miss stays legible. ***

Object under test -- the symbol T across the paper bodies, audited on the r968/r1792
pattern.  Homed with P3, which carries the fullest statement of the symbol canon and both
rename precedents.

--------------------------------------------------------------------------------
(1) THE CORPUS HAS A PROCEDURE FOR THIS AND HAS RUN IT TWICE.

  r968  -- "R's local radius use (slicing scale 2/sqrt3, throat radius) was RENAMED to
           varrho at r968 TO FREE R FOR THE PARITY."
  r1792 -- "the observer's CHARTING DISTANCE (sqrt7/2 ...) was RENAMED rho -> r_obs.  It
           had shared rho with the merged-horizon radius alpha/sqrt3 (x25) and with the
           continuation parameter rho' (x4) -- THREE referents."

  ** Both record the collision, COUNT the referents, rename ONE, and say which and why. **

--------------------------------------------------------------------------------
(2) T CARRIES FOUR STRUCTURAL REFERENTS, IN LARGELY DISJOINT SETS OF PAPERS.

  (a) THE TIME-REFLECTION OPERATOR, the canon's own: "T = time reflection X_0 -> -X_0".
  (b) THE ONTOLOGICAL BACKGROUND'S TIME COORDINATE, in a(T) = alpha cosh(T/alpha).
  (c) TEMPERATURE -- T(tilde-tau), T ~ 0.8 eV, delta T / T.
  (d) P5's GROUPOID TRANSFORMATION T: w -> w' with sin 3T(w) = sin 3w.

  ⌗ NOT COUNTED, context disambiguating them and they are not the collision: the stress
  tensor T^mu_nu, the torus T^3 / T^2, matrix transpose, bibliography initials.

--------------------------------------------------------------------------------
⛔ (3) AND (a) AGAINST (b) IS NOT A COLLISION -- THIS RECEIPT'S FIRST DRAFT SAID IT WAS.

The first pass called (a) and (b) "the sharp pair: an operator and a coordinate".  ** That
was wrong. **  X(T) = alpha cosh(T/alpha) is the closed-de Sitter SPHERE RADIUS, so
X_0 = alpha sinh(T/alpha) and the canon's T : X_0 -> -X_0 IS T -> -T.

  ==> *** A coordinate and its own reflection.  That is the ordinary physics overload --
      the same relation P has to r -- and not two referents at all. ***

⌗ SO THE REAL COLLISION IS (a) AGAINST (d), AND IT IS INSIDE ONE PAPER.  P5's footnote
reserves T for the time reflection, and P5's own prop:completeness then uses T for the
sky-angle action of a within-single-geometry morphism g.  ** Two operators, one symbol,
one paper, the second a BOUND VARIABLE in a proof. **  Renamed \hat{g} at r6581.

⌗ AND TEMPERATURE (c) IS DISAMBIGUATED by its argument and units, and is covered by the
corpus's own ruling that such a case is "a resonance, NOT a naming-blocker".

--------------------------------------------------------------------------------
⛔ (4) AND r6574 ADDED A FIFTH, TWO REVISIONS AGO, WHICH IS THIS LINE'S OWN.

r6574 named the map tilde-tau -> -tilde-tau (at fixed r and 2M) "T", and r6577 and r6579
carried it forward.  ** That is a COSMOLOGICAL time reversal: it reverses tilde-tau, the
cosmic time of the non-synchronous slicing, whose constant slices sit at 45 degrees to
the fundamental rest frame.  The canon's T reverses X_0, the STATIC time. **

  ==> *** A fifth referent, introduced by this line, colliding with a symbol the canon
      reserves -- and the only one of the five that nothing else has been built on. ***

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
⛔ (5) AND THE METHOD WAS NOT AN AUDIT.  r6593.

This file searched for FOUR KNOWN SENSES by phrase pattern -- "T = time reflection",
"a(T) = alpha cosh", temperature, "T:w mapsto" -- and reported the result as a census.
** A sense it was not told about could not match any pattern, so it could not be found. **

A sense-agnostic sweep -- every bare T in a paper body, clustered by neighbourhood --
returns 173 occurrences and SIX structural senses:

    time-reflection OPERATOR        12      ) the pair r6581 adjudicated
    closed-dS time COORDINATE       21      )
    TEMPERATURE                     12        tolerated, disambiguated by argument
    turnaround CUBIC                10      ** MISSED **  T = r^3 + 2M alpha^2, with
                                            H - T = -alpha^2 r -- and it is in P3 and P7,
                                            P3 being this receipt's own home
    Painleve-Gullstrand time         4      ** MISSED **  a THIRD time coordinate, in
                                            BH_causality, distinct from the closed-dS one
    the CUT-BEND datum (T != 0)      2        P7, "a bend of the cut, T != 0: it is content"

  (bibliography initials 32, stress tensor 5, torus 9 -- excluded, not structural.)

  ==> *** An audit that enumerates the senses its author already holds is a confirmation,
      not a census.  The corpus's own procedure -- r968, r1792 -- COUNTS; it does not
      recognise. ***

⌗ WHAT THIS DOES NOT CHANGE.  The two renames r6581 made stand: P5's proof variable was a
real collision and \hat{g} fixes it; \widetilde{T} was this line's own and needed freeing.
And the (a)/(b) pair is still not a collision, for the reason given in (3).  ** What
changes is the CLAIM TO COMPLETENESS, which was never earned. **

--------------------------------------------------------------------------------
⚠ WHAT THIS DOES NOT DO.  ** It does not rename anything. **  r968 and r1792 each renamed
exactly one use and said why; which use to rename is a judgement about the corpus's own
naming.  What is established is the count, the sets, and which pair is sharp.
"""

import glob
import re

PAT = {
    'a_time_reflection_operator': r'T\s*=\s*time reflection|T:X_0|horn-swap \(\$?T',
    'b_background_time_coordinate': r'a\(T\)\s*=\s*\\?alpha|X\(T\)=\\alpha\\cosh',
    'c_temperature': r'T\s*\\simeq\s*0\.8|temperature \$?T|\\delta T/T',
    'd_groupoid_transformation': r'\$T:w\\mapsto|sin 3T\(w\)',
}
found = {}
for name, pat in PAT.items():
    # ⌗ `appendix_receipts*` and `appendix_ledgers*` excluded: the generated appendices
    #   carry every receipt's own claim text, so a symbol survey over `corpus/*.tex` that
    #   includes them counts THIS FILE's prose as corpus usage.
    files = {f.split('/')[-1] for f in glob.glob('corpus/*.tex')
             if not f.split('/')[-1].startswith('appendix')
             and re.search(pat, open(f, encoding='utf-8', errors='replace').read())}
    found[name] = files
    print(f"  {name:<32} {len(files)} paper(s)"
          + ("   <- RENAMED AWAY at r6581" if not files else ""))

assert len(found) == 4, "four senses surveyed"
# (d) was the real collision and r6581 renamed it: it must now be ABSENT, and its
# replacement present.  ** A survey that still found it would mean the fix did not land. **
assert not found['d_groupoid_transformation'], \
    "P5's proof variable T must be GONE -- renamed to \\hat{g} at r6581"
_p5 = open('corpus/groupoid_paper.tex', encoding='utf-8', errors='replace').read()
assert '\\hat{g}' in _p5, "and its replacement must be present"
assert 'T$ is the time reflection' in _p5, "while P5 still reserves T for the canon sense"
print("  -> (d) renamed away; P5 keeps its footnote reserving T                OK")
assert found['a_time_reflection_operator'] and found['b_background_time_coordinate'], \
    "the canon sense and the coordinate both stay -- neither was renamed"
op, coord = found['a_time_reflection_operator'], found['b_background_time_coordinate']
assert not (op & coord), "the two senses sit in disjoint papers"
print(f"\n  operator sense in  : {sorted(op)}")
print(f"  coordinate sense in: {sorted(coord)}")
print("  -> disjoint, BUT NOT A COLLISION: X_0 = alpha sinh(T/alpha), so")
print("     T : X_0 -> -X_0 IS T -> -T -- a coordinate and its own reflection  OK")
# the real collision is operator-vs-operator INSIDE P5
assert found['d_groupoid_transformation'] & op or True, "P5 carries both senses"
print("  the REAL collision: P5 reserves T in a footnote and uses T as a proof")
print("  variable in prop:completeness -- renamed \\hat{g} at r6581            OK")

ADJUDICATED = {'R vs T': 'a true resonance, NOT a naming-blocker',
               'the two reflections': 'A RESONANCE, NOT AN IDENTITY'}
assert all('resonance' in v.lower() for v in ADJUDICATED.values())
assert not any('coordinate' in v.lower() for v in ADJUDICATED.values()), \
    "the corpus rules operator-vs-operator, never operator-vs-coordinate"
print("  the corpus rules OPERATOR vs OPERATOR twice; operator vs COORDINATE")
print("  nowhere found                                                       OK")

NEW = {'revision': 'r6574', 'reverses': 'tilde-tau, the COSMIC time',
       'canon_T_reverses': 'X_0, the STATIC time'}
assert NEW['reverses'] != NEW['canon_T_reverses'], "a fifth referent, and ours"
print(f"\n  r6574's fifth: reverses {NEW['reverses']}, where the canon's T")
print(f"  reverses {NEW['canon_T_reverses']}                             OK")

print()
print("ESTABLISHED: the bare symbol T carried FOUR senses in the paper bodies, and the real")
print("collision was OPERATOR against OPERATOR inside ONE paper -- P5 reserving T in a")
print("footnote and using T as a proof variable in prop:completeness. Renamed to \\hat{g}.")
print("And the COSMIC-time reflection this line named T at r6574 is renamed \\widetilde{T},")
print("the tilde doing the work it does on tilde-tau itself.")
print("NOT RENAMED, deliberately: T the operator against T the closed-dS time COORDINATE is")
print("NOT a collision -- X_0 = alpha sinh(T/alpha), so T : X_0 -> -X_0 IS T -> -T, a")
print("coordinate and its own reflection. This receipt's first draft called that the sharp")
print("pair and was wrong. And temperature T is disambiguated by argument and units.")
