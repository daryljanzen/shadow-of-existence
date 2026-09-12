"""
P03_can_the_charge_be_read_from_the_acting_count
================================================
WHAT IT ASKS.  P3R49 identified two counts on a constituent's route: n, the signed
graze-point count P3's winding measures, and nu, the OWN-WALL count that actually acts
on the bound mode under the three-vantage reading.  Since nu is the operative one, the
question is whether the CHARGE should be read from nu rather than from n.

That is not a free relabelling.  P3 sec:winding derives the thirds from three inputs:
the two-route fact (the partner relation y = x - 1), three constituents, and closure
(the upper-headed total x + 2y and the lower-headed y + 2x must both be integers).
Substituting the candidate label into that derivation either returns thirds or does
not, and that is decidable.

WHAT WOULD FALSIFY THE HEADLINE.  If the nu-reading reproduced the partner relation
AND forced the thirds, it would be a live alternative to the n-reading and the choice
between them would be open.
"""
from fractions import Fraction as F

# The two routes, signed, from P3R49's enumeration.
# ccw short route: crosses the third hinge's wall only     -> n = +1, own-wall nu = 0
# cw  long route : crosses own wall and the destination's  -> n = -2, own-wall nu = -1
ROUTES = [("short (ccw)", +1, 0), ("long (cw)", -2, -1)]

print("=" * 78)
print("PART 1 — THE TWO COUNTS, SIGNED")
print("=" * 78)
for nm, n, nu in ROUTES:
    print(f"  {nm:>12}:  n = {n:+d}   nu = {nu:+d}")
sgn = lambda z: (z > 0) - (z < 0)
print(f"  signed relation: nu = n - sgn(n) ?  "
      f"{all(nu == n - sgn(n) for _, n, nu in ROUTES)}")
print("  (unsigned this is P3R49's nu = n - 1)")

print()
print("=" * 78)
print("PART 2 — RUN P3's DERIVATION ON EACH CANDIDATE LABEL")
print("=" * 78)

def run(label_name, xa, xb):
    """P3 sec:winding: partner relation, then closure of both horn-headed triples."""
    print(f"  -- candidate: {label_name}")
    print(f"     the two routes carry  x = {xa}  and  y = {xb}")
    partner = (xb == xa - 1)
    print(f"     partner relation y = x - 1 (the two routes differ by ONE LAP): {partner}")
    if not partner:
        print(f"        actual difference y - x = {xb - xa}, not -1")
    # closure: x + 2y and y + 2x integral, with y = x - 1 these are 3x-2 and 3x-1
    up, lo = xa + 2 * xb, xb + 2 * xa
    print(f"     upper-headed total x+2y = {up} ; lower-headed y+2x = {lo}")
    print(f"     both integers: {up.denominator == 1 and lo.denominator == 1}")
    forced = partner and (xa.denominator == 3)
    print(f"     ** thirds FORCED by this label: {forced} **")
    print()
    return forced

n_a, n_b = F(ROUTES[0][1], 3), F(ROUTES[1][1], 3)
nu_a, nu_b = F(ROUTES[0][2], 3), F(ROUTES[1][2], 3)
nuint_a, nuint_b = F(ROUTES[0][2]), F(ROUTES[1][2])

r1 = run("charge = n/3   (P3's winding, as written)", n_a, n_b)
r2 = run("charge = nu/3  (acting count, same units)", nu_a, nu_b)
r3 = run("charge = nu    (acting count, integral)", nuint_a, nuint_b)

print("=" * 78)
print("PART 3 — WHY THE nu-READING CANNOT CARRY THE CHARGE")
print("=" * 78)
print("  nu counts crossings of ONE wall -- the mode's own -- and over the two routes")
print("  it takes the values 0 and -1.  ** It is integer-valued by construction. **")
print("  A label that is already an integer cannot have integrality impose anything:")
print("  closure is satisfied identically and no denominator is forced.")
print()
print("  ** So the thirds exist precisely BECAUSE the charge-carrying count and the")
print("  monodromy-acting count are different counts. **  n runs over all three walls")
print("  and is fractional in thirds of a lap; nu runs over one wall and is integral.")
print("  Reading the charge off the acting count would remove the very quantisation")
print("  the section derives.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(f"  charge = n/3   : partner relation holds, thirds forced   -> {r1}")
print(f"  charge = nu/3  : partner relation fails                  -> {r2}")
print(f"  charge = nu    : partner relation holds, thirds NOT forced -> {r3}")
print()
print("  ** ANSWERED, AND IN THE NEGATIVE: the charge cannot be read from the acting")
print("  count. **  P3's n is the right label, and P3R49's nu = n - 1 is not a rival")
print("  reading of the same quantity but a statement that TWO counts live on one")
print("  route, doing two jobs: n carries the charge and is fractional, nu carries the")
print("  monodromy and is integral.")
print()
print("  AND THE STANDING ASSUMPTION IS UNCHANGED BY THIS: n = t (mod 3) relates the")
print("  charge-carrying count to the triality, and nothing here bears on it.  What is")
print("  removed is one candidate route to deriving it -- via the acting count -- which")
print("  is now closed rather than untried.")
