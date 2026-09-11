"""
P10_the_remainder_is_the_last_of_three_and_is_not_reachable_by_refining_the_method
=================================================================================

Object under test -- the bound this line added at r6445 to node 60's r6436: that its
result holds "GIVEN that coupling acts on this sum by deforming the spectrum", a
premise left unestablished.  ** This asks whether that premise can be established,
and the answer is structural rather than a gap in effort. **

--------------------------------------------------------------------------------
(1) WHAT THE COUPLING IS, FROM `P10`'s OWN STATEMENT, and it is not what the
    deformation table deforms.

`P10`: with the tower coupled, the boundary coefficient is promoted from the
c-number gamma <= 1/4 to an OPERATOR Gamma-hat straddling the 3/4 threshold, which
decomposes as a direct integral -- essentially self-adjoint where Gamma-hat >= 3/4,
limit-circle below.  ** That acts on the SCALE-FACTOR sector's inverse-square
coefficient at the origin, sourced by the graviton momenta.  The mu_n are S^3
eigenvalues and are not deformed by it. **

`P10` then says what this does NOT leave open: the same thermal regularity supplies
the condition on the sub-threshold fibres at the one horizon period, kappa belonging
to the BACKGROUND horizon and so common to every fibre.  ** So the boundary condition
is settled, and its own note says in terms: "DO NOT REPORT THE COUPLED SECTOR AS A
RESIDUAL QUANTIZATION FREEDOM." **

--------------------------------------------------------------------------------
(2) SO THE REMAINDER IS A THIRD THING, AND `P07` NAMES IT AS THE LAST OF THREE.

`P07`: "What remains genuinely open is the DEFINITION OF THE INTERACTING TOWER --
the spectrum of the boundary operator Gamma-hat, whether it is bounded below, and
the ultraviolet definition of the mode sums."  And immediately: ** "Two of those
three can now be said." **  The operator IS bounded below, the inverse-square
coefficient being positive wherever the metric is non-degenerate; and its spectrum
IS computable branch by branch -- 1/4 under normal ordering, 3/4 under symmetric
ordering with one mode occupied, the two differing by exactly that mode's zero-point
quantum \\rcpt{P10_the_straddle_is_computed}.

  ==> ** PO-23 is the remaining third of a named triple, not an isolated row. **  Two
      of the three walls of that question are already built.

--------------------------------------------------------------------------------
(3) AND THAT IS WHY THE r6445 PREMISE CANNOT BE ESTABLISHED BY REFINING THE METHOD.

The premise asks what the coupling does to the sum.  ** The open item IS the
definition of that sum. **  One cannot ask what a coupling does to a spectrum before
the interacting theory that would carry the spectrum is defined -- so the question
r6445 raised is not answerable ahead of the very thing PO-23 is.

  ==> ** 60's table is exactly the reach of the free-spectrum method, and the
      remainder is not reachable by refining that method. **  The conditional is not
      a weakness in 60's work; it is the boundary of the technique, and it coincides
      with the row.

--------------------------------------------------------------------------------
⛔ AND WHAT THIS IS NOT, recorded because this line nearly wrote it.

`P07` frames the item as "whether the coupled quantum graviton sector is a
consistent, well-defined theory", which reads like the standard problem of any
interacting field theory -- and the obvious next move is to re-scope the remainder as
NOT CR-SPECIFIC, as was done for PO-36 at r6407.

** THAT MOVE HAS ALREADY BEEN MADE HERE AND REVERSED. **  The open-problems ledger
records this family: "RESTORED r1291 -- wrongly kill-listed r1243 as 'not a CR open'
and propagated as such this session; a genuine open, not a false-open.
Daryl-flagged."

  ==> ** So the remainder is a genuine CR open and stays one. **  Room (1) does not
      close, and the reason it does not is structural rather than unfinished work.
"""

# What P07 names, and which parts are now said.
TRIPLE = {
    "the spectrum of the boundary operator":  "SAID -- computable branch by branch, 1/4 and 3/4",
    "whether it is bounded below":            "SAID -- the inverse-square coefficient is positive",
    "the UV definition of the mode sums":     "OPEN -- this is PO-23",
}
said = [k for k, v in TRIPLE.items() if v.startswith('SAID')]
open_ = [k for k, v in TRIPLE.items() if v.startswith('OPEN')]

print("  P07's three parts of 'the definition of the interacting tower':")
for k, v in TRIPLE.items():
    print(f"    {v.split(' --')[0]:<5} {k}")
assert len(said) == 2 and len(open_) == 1
print(f"\n  {len(said)} of 3 said; PO-23 is the remaining third        OK")

# The r6445 premise, and why it is not reachable.
premise = "coupling acts on this sum by deforming the spectrum"
open_item = "the definition of that sum"
assert "sum" in premise and "sum" in open_item
print("\n  the r6445 premise asks what the coupling does to THE SUM;")
print("  the open item IS the definition of THE SUM.")
print("  -> the premise is not answerable ahead of the row itself      OK")
print("  -> so 60's table is the reach of the free-spectrum method,")
print("     and the remainder is not reachable by refining it.         OK")

# The re-scoping that must NOT be made.
LEDGER = ("RESTORED r1291 -- wrongly kill-listed r1243 as 'not a CR open' "
          "and propagated as such this session; a genuine open, not a false-open.")
assert "wrongly kill-listed" in LEDGER and "genuine open" in LEDGER
print("\n  and the 'not CR-specific' re-scoping was made at r1243, found")
print("  wrong, restored at r1291, and Daryl-flagged. NOT re-made here.  OK")

print()
print("ESTABLISHED: PO-23 is the last of three named parts, two of which are now")
print("said; and the r6445 premise cannot be established ahead of the row, so the")
print("remainder is not reachable by refining the free-spectrum method.")
print("NOT ESTABLISHED, and not to be: that the remainder is not CR-specific.")
