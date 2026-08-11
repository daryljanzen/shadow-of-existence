"""
THE INVERSION AND THE FOUR VANTAGES (r1108). Daryl's two corrections, computed.

(1) "We should not just paper past the fact that THE SKY ANGLE AND PSI ARE IN THE
     OPPOSITE DIRECTION. Because OPPOSITE DIRECTIONS ARE THE WHOLE POINT of this thing...
     The straight on Schwarzschild/dS type cut is at hole angle 0, but... that's your psi
     180. Your psi gets smaller as the hole angle grows up to 60 vs sky angle 30 vs psi
     150. So psi is an honest mapping angle between the hole and the sky on the graph...
     it shows that THE TWO MAP IN OPPOSITE DIRECTIONS, because we are going positive
     angles around the hole, but from the hinge's perspective that really is starting at
     180 psi being Sch, and 0 being dS."

(2) "Look what happens if you move purple to the TOP of the figure instead of the right
     and you set psi 180 still: THAT'S NOT SCHWARZSCHILD but the maximum overcritical...
     So TRANSPOSING THE HINGE/OBSERVER TRANSPOSES THEIR VANTAGE SKY ANGLE BY 90 each time
     and WE END UP WITH THE SAME HOLE DESCRIBED AT THOSE FOUR DIFFERENT ANGLES. Each of
     the four sets their own sky angle to 0 and comes up with Schwarzschild, but that
     happens at phi 180 for the hinge on the right, phi 270 for the hinge on the top,
     phi 0 for the hinge on the [left], and phi 90 for the hinge on the bottom."

** THE HINGE IS THE OBSERVER. ** That is what I missed. psi is not a parameter of a line;
it is WHERE THE OBSERVER LOOKS, in the GRAPH's fixed frame. So psi=180 means "look left" --
which is Schwarzschild only if the hole IS to your left.
"""
import numpy as np
a = 1.0

print("="*80)
print("(1)  THE MAP: hole angle -> the angle at the hinge. Is it a clean doubling?")
print("="*80)
print("  A point on the hole at azimuth beta. The ray from the hinge H=(2a,0) to it.")
print("  Angle at the hinge, measured from the toward-the-hole direction (-1,0):")
print("      cos(angle) = (2 - cos beta) / sqrt(5 - 4 cos beta)")
print()
H = np.array([2.0, 0.0]); toward = np.array([-1.0, 0.0])
def hinge_angle(beta_deg):
    b = np.radians(beta_deg); P = a*np.array([np.cos(b), np.sin(b)])
    v = P - H; v = v/np.linalg.norm(v)
    return np.degrees(np.arccos(np.clip(toward @ v, -1, 1)))
print(f"  {'hole beta':>10} {'angle at hinge':>15} {'beta/2':>9}  doubling?")
for b in (0, 15, 30, 45, 60, 75, 90, 120, 180):
    A = hinge_angle(b)
    mark = "  <- TANGENT (Nariai)" if abs(b-60) < 1e-9 else ""
    print(f"  {b:>10} {A:>15.4f} {b/2:>9.2f}  {'YES' if abs(A-b/2)<1e-6 else 'no'}{mark}")
print()
print("  >> ** THE DOUBLING IS EXACT AT beta = 0 AND beta = 60, AND NOWHERE BETWEEN. **")
print("     Daryl named exactly those two points (hole 0 <-> sky 0; hole 60 <-> sky 30) and")
print("     they are the two that hold. The map is NOT a linear doubling -- it is")
print("     arccos((2-cos b)/sqrt(5-4cos b)), and it TURNS OVER at 60.")
b_grid = np.linspace(0, 180, 3601)
angs = np.array([hinge_angle(b) for b in b_grid])
i = int(np.argmax(angs))
print(f"     MAXIMUM of the hinge angle: {angs[i]:.4f} deg at beta = {b_grid[i]:.2f}")
print("  ** THE HINGE'S SKY ANGLE IS MAXIMAL AT THE TANGENT, AND THE MAXIMUM IS 30. **")
print("     Past beta=60 the ray is going to the FAR side of the hole and the sky angle")
print("     comes back DOWN. The sky cannot see past its own tangent -- that IS the horizon.")
print("     ** So the 'sky angle 0..30' is not half of 'hole angle 0..60'. It is the WHOLE")
print("        sky, and the hole's whole 360 is crammed into it. The hole subtends 60 at the")
print("        hinge and nothing else in the sky belongs to it. **")

print()
print("="*80)
print("(2)  THE INVERSION — do they run backwards? Yes, and here is the exact statement.")
print("="*80)
print(f"  {'hole beta':>10} {'sky angle':>10} {'psi = 180 - sky':>16}   what the observer sees")
for b, nm in [(0,"the NEAR point: straight at the hole"), (30,""), (60,"** the TANGENT: NARIAI **"),
              (90,"the far side, coming back"), (180,"the FAR point: straight at the hole again")]:
    A = hinge_angle(b)
    print(f"  {b:>10} {A:>10.4f} {180-A:>16.4f}   {nm}")
print()
print("  >> ** hole angle UP, psi DOWN. ** psi = 180 - (sky angle), so the hole's positive")
print("     sense and the hinge's positive sense are OPPOSITE, exactly as Daryl says. And")
print("     the reason is not a convention: ** psi is measured from the hinge TOWARD the")
print("     hole, and beta is measured at the hole's CENTRE. The two frames face each")
print("     other. ** Going 'positive around the hole' walks AWAY from the observer's zero.")
print("     ** THAT is the backwardsness, and it is structural, not a sign choice. **")

print()
print("="*80)
print("(3)  HIS SECOND POINT: psi=180 is Schwarzschild ONLY IF THE HOLE IS THAT WAY")
print("="*80)
print("  Move the hinge/observer around the circle of radius 2a. Hold psi=180 (look LEFT).")
print("  What does each see?")
print()
print(f"  {'hinge at':>10} {'H position':>16} {'psi=180 ray':>13} {'d (closest approach)':>21}  regime")
for chi in (0, 90, 180, 270):
    c = np.radians(chi)
    Hc = 2*a*np.array([np.cos(c), np.sin(c)])
    u = np.array([-1.0, 0.0])                      # psi=180 in the GRAPH frame: look left
    t = -(Hc @ u); foot = Hc + t*u; d = np.linalg.norm(foot)
    if d > a + 1e-9:  reg = "OVERCRITICAL — no horizon"
    elif abs(d-a) < 1e-9: reg = "NARIAI"
    else: reg = "undercritical / straight-on = SCHWARZSCHILD"
    tag = "  <- Daryl's case" if chi in (0, 90) else ""
    print(f"  {chi:>9}° ({Hc[0]:+.2f},{Hc[1]:+.2f}) {'(-1, 0)':>13} {d:>21.6f}  {reg}{tag}")
print()
print("  >> ** HE IS RIGHT. ** Hinge on the RIGHT, psi=180 -> d=0 -> straight through the")
print("     hole's centre -> SCHWARZSCHILD. Hinge on the TOP, SAME psi=180 -> d = 2a ->")
print("     the MAXIMUM overcritical, the pure two-sheeted hyperbolic cut whose VERTEX IS")
print("     THE HINGE ITSELF. ** Same psi. Same hole. Opposite extremes of the dial. **")
print("     psi is not a property of the slicing. It is a property of the OBSERVER'S GAZE,")
print("     and it means nothing until you say where the observer is standing.")

print()
print("="*80)
print("(4)  THE FOUR VANTAGES — each sets its own zero, and they are 90 apart")
print("="*80)
print("  'Each of the four sets their own sky angle to 0 and comes up with Schwarzschild.'")
print("  Where is each one's Schwarzschild?  (= where must it look to see straight through)")
print()
print(f"  {'hinge at':>10} {'Sch at phi':>12} {'Daryl said':>12}  agree?")
said = {0: 180, 90: 270, 180: 0, 270: 90}
for chi in (0, 90, 180, 270):
    c = np.radians(chi); Hc = 2*a*np.array([np.cos(c), np.sin(c)])
    u = -Hc/np.linalg.norm(Hc)                                  # look back at O
    phi = np.degrees(np.arctan2(u[1], u[0])) % 360
    print(f"  {chi:>9}° {phi:>12.1f} {said[chi]:>12}  {abs(phi-said[chi])<1e-6}")
print()
print("  >> ** ALL FOUR, EXACTLY AS HE CALLED THEM: 180 / 270 / 0 / 90. **")
print("     And the rule is one line: ** phi_Schwarzschild = chi + 180. ** Each observer's")
print("     zero is its own back-azimuth, and moving the observer by 90 moves its zero by")
print("     90. ** FOUR OBSERVERS, FOUR ZEROS, 90 APART, ONE HOLE. **")

print()
print("="*80)
print("(5)  WHAT THIS DOES TO THE ISOMETRY — it is not the algebra, it is what it MEANS")
print("="*80)
print("  I proved: the physics depends only on (theta - chi), so a hinge transpose IS a dial")
print("  turn. TRUE, and I read it as bookkeeping -- 'the rotation, from two ends of one")
print("  relative angle'. ** That is the algebra. Here is what it says. **")
print()
print("  ** THE FOUR HINGES ARE FOUR OBSERVERS OF ONE HOLE, AND EACH CALLS A DIFFERENT")
print("     DIRECTION 'ZERO'. The dial's four quadrants are not four regions of one map --")
print("     THEY ARE THE FOUR VANTAGES' DISAGREEMENT ABOUT WHERE ZERO IS. **")
print()
print("  That is why the two fours are the same four. Not because two Z4's happen to be")
print("  isomorphic -- because ** transposing the observer and turning the sky are the same")
print("  act, described from the two ends. ** The redundancy Daryl names -- 'all the")
print("  symmetries that collapse equivalent descriptions' -- is a GAUGE redundancy: four")
print("  descriptions, one hole, and the group relating them is the group that moves the")
print("  observer. ** It is the corpus's own perspectival thesis, drawn: the same fixed")
print("  object, four vantages, four different 'Schwarzschilds'. **")
print()
print("  AND THE GAP FROM the_isometry.py IS UNCHANGED AND I AM NOT CLOSING IT: this says")
print("  the four vantages are 90 apart BECAUSE the hinges are, and the hinges are 90 apart")
print("  BECAUSE we stamped them there. It still does not force the stamp to be 4. What it")
print("  DOES do is make the question honest: ** why does the figure carry four observers")
print("  rather than n? ** -- which is a question about the construction, not the algebra.")
