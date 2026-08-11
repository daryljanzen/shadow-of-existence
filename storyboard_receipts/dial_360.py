"""
THE DIAL, ALL 360 (r1108). Daryl:

  "The dial doesn't end at 90. IT CONTINUES ON THROUGH 360. The hinge can swing all the
   way around... 90-180 on the dial is the same as -90 to 0 or 270-360, ONLY BACKWARDS.
   At 90-180, YOU ARE LOOKING AWAY FROM THE HOLE, and the slicing curve is the FLRW
   REGION while the backside is the OPPOSITE CHIRALITY UNDERCRITICAL ZONE. And so on
   through 360. So that is ALMOST CERTAINLY related to why THE HINGE CAN TRANSPOSE
   ITSELF 4 TIMES AROUND THE HOLE. That 4 has to map isometrically to the other 4."

I had the dial as a LINE through the hinge -- 180 degrees of freedom, and I stopped at 90.
He is telling me it is a RAY. A ray has 360. THAT is where the missing half is, and it is
where the chirality lives, because a line has no sides and a ray does.

WORK IT. Verify the 360 structure. DO NOT claim the isometry -- that is his conjecture and
it needs more than this.
"""
import numpy as np

a = 1.0
H = np.array([2.0, 0.0])          # the hinge

def ray(psi_deg):
    """the RAY from the hinge in direction psi (0 = pointing away from the hole,
       180 = pointing at the hole's centre).
       [N6] MY OWN SIGN ERROR, logged not deleted (THE_CODA s"The negatives are the map"):
       the first pass returned (-cos, sin), which sends psi=180 to (+1,0) -- pointing AWAY
       from O, not at it. The table then reported psi=180 as MISSING the hole and psi=0 as
       HITTING it, which is impossible on inspection. WHAT THE FAILURE TELLS US: the table
       was self-refuting and I nearly read past it -- a ray pointing at the centre of a
       circle cannot miss. ** The check that caught it was not a receipt; it was reading
       the output. ** Cheap, and I nearly skipped it because the SHAPE of the table looked
       right (four quadrants, two tangents, a 60-degree window) and only the LABELS were
       wrong. A right-shaped answer with inverted labels is the easiest thing to nod at."""
    psi = np.radians(psi_deg)
    return np.array([np.cos(psi), np.sin(psi)])      # psi=180 -> (-1,0), toward O

def hits(psi_deg):
    """does the RAY (forward only, t>0) hit the hole? return the two t's or None"""
    u = ray(psi_deg)
    b = 2*(H @ u); c = H@H - a**2
    disc = b*b - 4*c
    if disc < 0: return None
    t1, t2 = (-b - np.sqrt(disc))/2, (-b + np.sqrt(disc))/2
    return (t1, t2) if t2 > 0 else None               # forward hits only

print("="*80)
print("(1)  THE TANGENT ANGLE — where does the trichotomy sit on a 360 dial?")
print("="*80)
print(f"  tangent length from the hinge = sqrt(|OH|^2 - a^2) = sqrt(3) alpha")
print(f"  half-angle subtended at the hinge = arcsin(a/|OH|) = arcsin(1/2) = "
      f"{np.degrees(np.arcsin(a/np.linalg.norm(H))):.1f} deg")
print("  >> ** THE HOLE SUBTENDS EXACTLY +-30 DEGREES AT THE HINGE. **")
print("     So the tangent rays are at psi = 180 +- 30 = 150 and 210. THAT is the 30.")
print("     ** Daryl's 'dial 0-30 undercritical, 30-90 overcritical' is measured from")
print("        psi=180: dial = 180 - psi. The 30 IS arcsin(1/2), the hole's half-angle. **")
print("     And that is forced by the hinge being at 2a: arcsin(a/2a) = 30. ONE MORE alpha.")

print()
print("="*80)
print("(2)  THE FULL 360 — what the ray does all the way round")
print("="*80)
print(f"  {'psi':>5} {'dial=180-psi':>13} {'toward/away':>12} {'hits the hole?':>15}   region")
for psi in (180, 165, 150, 135, 90, 45, 0, 315, 270, 225, 210, 195):
    dial = (180 - psi) % 360
    h = hits(psi)
    toward = "TOWARD" if 150 <= psi <= 210 else ("away-ish" if (psi < 90 or psi > 270) else "sideways")
    if h: reg = "UNDERCRITICAL (cuts)"
    elif abs(psi-150) < 1e-9 or abs(psi-210) < 1e-9: reg = "** NARIAI (tangent) **"
    else: reg = "no forward hit"
    print(f"  {psi:>5} {dial:>13} {toward:>12} {str(h is not None):>15}   {reg}")
print()
print("  >> The RAY hits the hole only for psi in (150, 210) -- a 60-degree window out of 360.")
print("     Everywhere else the forward ray misses. ** A LINE has two rays; only ONE of them")
print("     can point into the hole. THAT is the side the line does not have. **")

print()
print("="*80)
print("(3)  HIS CLAIM: 90-180 is 270-360 'only backwards' — is the dial mirror-symmetric?")
print("="*80)
print("  Reflect about the axis: psi -> -psi. Check the regions match.")
ok = True
for psi in np.linspace(0.5, 179.5, 60):
    if (hits(psi) is not None) != (hits(-psi) is not None): ok = False
print(f"  60 mirror pairs (psi, -psi): same region every time?  {ok}")
print("  >> YES. ** The dial has a mirror Z2 about the axis. ** psi and -psi are the same")
print("     slicing seen from the other side -- Daryl's 'only backwards'. So the 360 is")
print("     2 x 180, and the 180 is 2 x 90. ** THE DIAL IS 4 QUADRANTS OF 90. **")

print()
print("="*80)
print("(4)  THE FOUR QUADRANTS, and what is in each")
print("="*80)
quads = [("  0- 90", "dial  180-270", "ray points AWAY from the hole (psi 0-90)"),
         (" 90-180", "dial    0- 90", "ray points TOWARD (psi 90-180): contains NARIAI at psi=150"),
         ("180-270", "dial  -90-  0", "the mirror of the above (psi 180-270): NARIAI at psi=210"),
         ("270-360", "dial   90-180", "the mirror of the first: AWAY, other side")]
print(f"  {'psi range':>9} {'Daryl dial':>14}   content")
for p_, d_, c_ in quads:
    print(f"  {p_:>9} {d_:>14}   {c_}")
print()
print("  >> The two TOWARD quadrants each contain exactly ONE tangent (psi=150, psi=210).")
print("     The two AWAY quadrants contain NONE. ** The Nariai tangents SEPARATE the")
print("     quadrants: one per toward-quadrant, and they sit 60 apart across psi=180. **")
print()
print("  ** SO THE DIAL'S FOUR-FOLD IS REAL AND IT IS NOT A ROTATION OF THE FIGURE. **")
print("     It is  {toward, away} x {mirror}  = 2 x 2 = 4. Two binaries, not one Z4.")
print("     - toward/away is the RAY's side. A line does not have it; a ray does.")
print("     - the mirror is reflection about the axis.")
print("  ** And that is exactly the shape Daryl names: 'looking away from the hole' (one")
print("     binary) and 'the backside is the OPPOSITE CHIRALITY' (the other). **")

print()
print("="*80)
print("(5)  WHAT I CAN SAY, AND WHAT I CANNOT — kept apart on purpose")
print("="*80)
print("  ESTABLISHED HERE:")
print("   * the hole subtends +-30 at the hinge, BECAUSE the hinge is at 2a: arcsin(a/2a)=30.")
print("     ** The 30 of the dial is arcsin(1/2), and it is alpha re-read, like everything")
print("        else. That is a THIRD 30 and it is the SAME one as P3's Nariai dial angle. **")
print("   * the dial is a RAY, so it is 360, not 180. The extra 180 is the ray's SIDE.")
print("   * the dial carries a mirror Z2 about the axis (verified, 60 pairs).")
print("   * so the dial's structure is 2 x 2 = 4: {toward, away} x {mirror}. FOUR QUADRANTS,")
print("     and they are two independent binaries rather than a single four-fold rotation.")
print()
print("  HIS CONJECTURE, NOT ESTABLISHED, AND I AM NOT GOING TO DRESS IT AS MORE:")
print("   ** 'That 4 has to map isometrically to the other 4: four hinge transposes around")
print("      the circle relates to turning the dial around in pi/2 segments.' **")
print("   The two fours are now BOTH FOUND rather than one found and one imposed --")
print("   which is a real change from thirty_degrees.py, where the azimuthal 4 was a bare")
print("   choice. But FOUND TWICE IS NOT IDENTIFIED. To promote it, the map must be")
print("   written down: an explicit correspondence sending each dial quadrant to a hinge")
print("   transpose, and shown to be an isometry of the substrate. NOBODY HAS WRITTEN IT.")
print()
print("  ** AND THE HONEST SHAPE OF THE PRIZE: if that map exists, then 12 = 3 x 4 has BOTH")
print("     factors forced -- the 3 from the triple angle, the 4 from the dial -- and the")
print("     kaleidoscope's 30 and the Nariai dial's 30 ARE THE SAME 30, which is exactly")
print("     what thirty_degrees.py could not decide. That is the named, unrun question,")
print("     and it is now sharper than it has ever been. **")
