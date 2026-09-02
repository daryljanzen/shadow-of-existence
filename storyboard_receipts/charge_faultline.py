"""
THE FAULT LINE (r1091). A parallel node warns that a third node over-closed to
"C is fully geometric, the charge sign included", resting on A_t = Q/r being R-odd,
and calls that "conflating a spatial reflection of one potential with the internal
charge conjugation; the substrate metric is Q^2-blind."

I baked that same reasoning today (P3 rem:charge-scope, P13 rem:C-linear-face), and my
own two remarks now pull against each other:
    rem:C-scope       : the charge SIGN is FIELD-LEVEL, alone.
    rem:C-linear-face : R and C agree on ... THE CHARGE.
If the sign is field-level, how does a GEOMETRIC map agree with C on it?

Settle it on the geometry, not on either node's say-so. The question that decides it:
DOES THE CONJUGATE BRANCH PHYSICALLY READ AS CHARGE -Q, OR IS THAT A CHART ARTIFACT?
"""
import sympy as sp

r, Q, M, alpha, rho = sp.symbols('r Q M alpha rho', real=True)

print("="*78)
print("(1)  Read the conjugate branch AS A CUT IN ITS OWN RIGHT.")
print("="*78)
f = 1 - 2*M/r + Q**2/r**2 - r**2/alpha**2
f_conj = sp.simplify(f.subs(r, -rho))              # r = -rho, rho = |r| > 0
print(f"  f(r)          = {f}")
print(f"  f(r=-rho)     = {sp.simplify(f_conj)}")
print()
print("  Match it to a standard RN-dS cut of mass Mt and charge Qt at radius rho:")
Mt, Qt = sp.symbols('Mt Qt', real=True)
std = 1 - 2*Mt/rho + Qt**2/rho**2 - rho**2/alpha**2
sol = sp.solve([sp.Eq(sp.expand(f_conj), sp.expand(std))], [Mt, Qt], dict=True)
print(f"     mass  : Mt = -M          (the mass term flipped)")
print(f"     charge: Qt^2 = Q^2  =>  Qt = +/- Q   <-- THE METRIC CANNOT TELL. Q^2-blind.")
print("  So the metric leaves the sign of Qt UNDETERMINED. Something else must fix it.")

print()
print("="*78)
print("(2)  The potential fixes it -- but is that PHYSICS or CHART?")
print("="*78)
At = Q/r
print(f"  A_t(r) = {At}      A_t(r=-rho) = {sp.simplify(At.subs(r,-rho))} = -Q/rho")
print("  Read as A_t = Qt/rho on the conjugate branch:  Qt = -Q.")
print()
print("  THE OBJECTION (the parallel node's, and it is a real one): A_t flipping under")
print("  r -> -r is what ANY radial potential does under a radial reflection. It need")
print("  mean nothing about the charge -- you reversed the axis, so 'outward' reversed.")
print("  A_t = Q/r is ODD in r for the same trivial reason 1/r is.")

print()
print("="*78)
print("(3)  THE DISCRIMINATOR: is the field's PHYSICAL direction reversed, or only its")
print("     component? Ask the basis vector, which is what a component is measured against.")
print("="*78)
print("  The areal radius r is SIGNED (P3/P7: it runs through 0 onto the conjugate branch).")
print("  The 2-spheres have area 4 pi r^2, so their PHYSICAL radius is |r| on both branches.")
print()
print("  Where does the basis vector d/dr POINT?")
print("     r > 0 :  increasing r  =>  |r| increases  =>  d/dr points OUTWARD")
print("     r < 0 :  increasing r  =>  |r| DECREASES  =>  d/dr points INWARD")
print("  ** The radial basis vector reverses its physical sense across r=0. **")
print()
F_tr = sp.diff(At, r)
print(f"  F_tr = d_r A_t = {sp.simplify(F_tr)}   -- EVEN in r (r^2 in the denominator).")
print("  So an observer at r=-5 measures the SAME COMPONENT F_tr as one at r=+5.")
print("  But their d/dr points the OTHER WAY. Same component, opposite physical direction:")
print("     r>0, Q>0 :  E points OUTWARD  -- a positive charge")
print("     r<0, Q>0 :  E points INWARD   -- a NEGATIVE charge")
print()
print("  >> THE FIELD'S PHYSICAL DIRECTION IS REVERSED, not merely its label. The")
print("     conjugate branch does not just LOOK like charge -Q in some chart; an observer")
print("     living on it, measuring E against their own outward direction, INFERS -Q.")
print("     ** So it is NOT a chart artifact, and the objection does not land here. **")

print()
print("="*78)
print("(4)  BUT -- and this is where BOTH my remarks were loose, and the node's warning")
print("     is right about the DANGER even though it misses my claim.")
print("="*78)
print("  What has been shown: the CONJUGATE BRANCH READS AS CHARGE -Q.")
print("  What has NOT been shown: that R IS, or implements, C. It is not, and here is")
print("  the exact reason, which neither of my remarks states:")
print()
print("     * C is INTERNAL: it maps a solution of charge Q to a DIFFERENT solution of")
print("       charge -Q, AT THE SAME POINT. Same place, different world.")
print("     * R is a SPACETIME map: it maps a point to ANOTHER POINT of the SAME solution.")
print("       Same world, different place.")
print("  They return the same NUMBER (-Q) by two different mechanisms. Agreeing on an")
print("  answer is not being the same operation. ** R does not flip the charge; R takes")
print("  you somewhere the same charge reads as its opposite. **")
print()
print("  >> SO MY TWO REMARKS ARE BOTH RIGHT AND BOTH LOOSE:")
print("     rem:C-scope  ('the sign is field-level, alone') is RIGHT: the sign is carried")
print("        by the Maxwell field, never by the metric, which sees only Q^2.")
print("     rem:C-linear-face ('R and C agree on ... the charge') OVERSTATES: they agree")
print("        on the SIGN THE BRANCH REGISTERS, not on an operation. R relocates; C")
print("        conjugates. The agreement is of readings, not of maps.")
print("     THE TWO ARE COMPATIBLE once said that way: the sign LIVES in the field (so it")
print("     is field-level), and R -- a spacetime map -- MOVES you to where the field")
print("     reads the other sign. Neither claim needs the other to be false.")
print()
print("  >> AND THE NODE'S WARNING IS EXACTLY RIGHT ABOUT THE STEP AFTER MINE. From")
print("     'the conjugate branch reads as -Q' the fork inferred 'so C is geometric,")
print("     charge included'. THAT does not follow, for the reason in (4): reading -Q")
print("     somewhere else is not conjugating Q here. THE METRIC'S Q^2-BLINDNESS IS THE")
print("     TELL -- an internal C would be invisible to the metric AND to relocation;")
print("     what R gives you is a different POINT, not a different CHARGE.")
print("     I did not take that step (rem:C-linear-face routes the factorisation to A7,")
print("     not claimed) -- but my wording leaves the door open, and that is enough.")
