"""
U2 — A = cbrt(2) * rho, RUN. (r1110)

Named and unrun since the double-root entry went into the glossary. r1109 said it is
"the vertical gap between the turnaround curve and the ellipse at the Nariai ordinate,
drawable since 2012." Nobody computed it.

WHAT IT IS. lem:twoturnings (P7): the slicing turns where f=0, the cosmic-time reading
turns where 1-f=0. Two cubics, affinely inequivalent: no AFFINE change of variable identifies
their root sets. They are nonetheless the E=1 and E=0 ends of one family of turning points,
r^3+(E^2-1)a^2 r+2M a^2 (rem:tworealisations); the obstruction is at fixed cubic.

    f = 0    ->  r^3 - a^2 r + 2M a^2 = 0      the HORIZON cubic       roots incl. rho
    1 - f = 0 -> r^3 + 2M a^2 = 0              the TURNAROUND cubic    root  r = -A

  rho = a/sqrt3          the Nariai merged horizon (the double root)
  A   = (2M a^2)^(1/3)   the bead's amplitude AND |comoving turnaround| (P7 thm:bead)

THE QUESTION lem:twoturnings DOES NOT ANSWER: it denies an identification of the two
SYMMETRIES. It says nothing about a RATIO BETWEEN TWO RADII. So: what is A/rho?

COULD THIS RETURN OTHERWISE? Yes. A/rho is a number; it is cbrt(2) or it is not, and if
Nariai were not the double root it would not be. Checked off-Nariai too, where it fails.
"""
import numpy as np

a = 1.0                      # gauge
rho = a/np.sqrt(3)           # Nariai merged horizon, the double root
TwoM_N = 2*a/(3*np.sqrt(3))  # the Nariai mass

print("="*78)
print("U2 -- A = cbrt(2) * rho, at Nariai")
print("="*78)

A = (TwoM_N * a**2)**(1/3)
print(f"  rho (merged horizon, a/sqrt3)   = {rho:.12f}")
print(f"  A   (amplitude = |turnaround|)  = {A:.12f}")
print(f"  A / rho                         = {A/rho:.12f}")
print(f"  cbrt(2)                         = {2**(1/3):.12f}")
print(f"  |A/rho - cbrt(2)|               = {abs(A/rho - 2**(1/3)):.3e}")
assert abs(A/rho - 2**(1/3)) < 1e-14
print("  ** A = cbrt(2) * rho  HOLDS, exactly. **")

print("\n" + "="*78)
print("WHY -- it is the double root's own factorisation, and BOTH 2s are the same 2")
print("="*78)
print("""  A monic depressed cubic with a double root rho factors exactly one way:
        (r - rho)^2 (r + 2rho) = r^3 - 3rho^2 r + 2rho^3
  Match to the HORIZON cubic  r^3 - a^2 r + 2M a^2:
        p:  a^2    = 3 rho^2     ->  rho = a/sqrt3          <- THE SEAM
        q:  2M a^2 = 2 rho^3     ->  M a^2 = rho^3          <- THE NARIAI CONDITION
  And the TURNAROUND cubic gives  A^3 = 2M a^2  = q =  2 rho^3   ->  A = cbrt(2) rho.

  So the -2rho of the third root and the 2rho^3 of the constant term are THE SAME 2,
  and A is the cube root of the horizon cubic's own constant term.""")
q = 2*rho**3
print(f"\n  constant term q = 2M a^2 = {TwoM_N*a**2:.12f}")
print(f"  2 rho^3                  = {q:.12f}   match: {abs(TwoM_N*a**2 - q):.3e}")
print(f"  A^3                      = {A**3:.12f}")
assert abs(A**3 - 2*rho**3) < 1e-14
print("  ** A^3 = q = 2 rho^3.  The amplitude IS the cube root of the constant term. **")

print("\n" + "="*78)
print("THE 2012 FIGURE -- where it is drawn (gauge a=1, the (r0, r) plane)")
print("="*78)
r0 = rho                       # the Nariai ordinate
# the fundamental ellipse  r^2 + r r0 + r0^2 = 1  -> the two non-designated roots
c = [1.0, r0, r0**2 - 1.0]
ell = np.sort(np.roots(c))
# the turnaround curve r = -(2M)^(1/3) with 2M = r0 - r0^3
TwoM = r0 - r0**3
r_turn = -(TwoM)**(1/3)
print(f"  at the Nariai ordinate r0 = {r0:.6f}:")
print(f"    ellipse roots            : {ell[0]:+.6f}, {ell[1]:+.6f}")
print(f"      -> the DOUBLE ROOT rho : {ell[1]:+.6f}   (= a/sqrt3)")
print(f"      -> the BACKWARD root   : {ell[0]:+.6f}   (= -2a/sqrt3)")
print(f"    turnaround curve         : {r_turn:+.6f}   (= -A)")
assert abs(ell[1] - rho) < 1e-12 and abs(ell[0] + 2*rho) < 1e-12
assert abs(r_turn + A) < 1e-12

print(f"""
  ** THE READING, CORRECTED. ** r1109 called it "the vertical gap between the turnaround
  curve and the ellipse." It is not a gap between two curves -- it is the RATIO OF TWO
  ORDINATES AT ONE ABSCISSA:

        |turnaround|  = {A:.6f} = A
        ellipse's designated root = {ell[1]:.6f} = rho
        ratio = {A/rho:.6f} = cbrt(2)

  Both are read off the SAME vertical line r0 = a/sqrt3 on the 2012 figure. The bridge is
  drawable there, and has been since 2012 -- but as a ratio of two heights, not a gap.""")

print("\n" + "="*78)
print("THE FALSIFIER -- off Nariai it must FAIL, or the result is vacuous")
print("="*78)
print(f"  {'r0':>10} {'A':>12} {'designated':>12} {'A/rho_desig':>14}  cbrt2?")
bad = 0
for x in [0.20, 0.35, rho, 0.70, 0.90]:
    TwoM_x = x - x**3
    A_x = (TwoM_x)**(1/3) if TwoM_x > 0 else float('nan')
    ratio = A_x/x
    hit = abs(ratio - 2**(1/3)) < 1e-9
    if hit and abs(x-rho) > 1e-9: bad += 1
    tag = "  <== NARIAI  ** cbrt2 **" if hit else ""
    print(f"  {x:>10.6f} {A_x:>12.6f} {x:>12.6f} {ratio:>14.6f}{tag}")
assert bad == 0
print("\n  ** The ratio is cbrt(2) at Nariai and nowhere else. Not vacuous. **")

print("\n" + "="*78)
print("SCOPE -- what this does NOT do")
print("="*78)
print("""  lem:twoturnings stands untouched. It denies a canonical identification of the two
  Z3 SYMMETRIES -- the comoving turning roots form an equilateral triangle in the complex
  r-plane, the horizon roots are colinear and real (casus irreducibilis), and the two
  cubics are affinely inequivalent. NONE of that is disturbed by a ratio between two
  specific real radii at one specific member.

  What is established: at Nariai, and only at Nariai, the bead's amplitude and the merged
  horizon stand in the ratio cbrt(2), because both are read off the ONE double-root
  factorisation -- rho from its p, A^3 from its q.

  What is NOT established: any relation between the two Z3s. U2 asked for the ratio; the
  ratio is what it returns.""")
print("\nU2: RUN. A = cbrt(2) * rho, exact, Nariai-only, lem:twoturnings intact.")
