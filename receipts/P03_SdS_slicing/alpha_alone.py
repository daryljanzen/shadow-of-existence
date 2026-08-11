# ── AVENUE 11 VERIFICATION HEADER (r1339, Arthur) ──────────────────────────────
# VERIFIES: α alone sets the whole construction — 2α is OUTPUT not input (the Thales circle built from
#   the hole ends at 2α), and every anchor (hinge height √3α, power 3α², tangent √3α, ruling 60°, tangency)
#   is forced from α as the sole gauge/unit. [P3 SdS-slicing-curve_v2, hinge-placement / α-as-gauge]
# STATUS: ✔✔  (original is print-based; an assert-block + a discriminating control appended below at the
#   foot of this canonical copy — tangency holds ONLY at R=2α; every anchor asserted from α=1)
# BOUND: works Daryl's claim at the weight offered; the anchors are forced-from-α, a geometric fact, not a
#   physical prediction. RUN: python3 alpha_alone.py
# ORIGIN: storyboard_receipts/alpha_alone.py (r1108), verified + strengthened + canonicalized r1339.
# ───────────────────────────────────────────────────────────────────────────────
"""
DARYL'S CLAIM, WORKED (r1108). Not assessed -- worked, at the weight it was offered.

He says, of my "the construction has one free choice -- put the hinge at 2 alpha":

  "The hinge's location isn't arbitrary. WHERE WOULD YOU PLACE A HINGE IN THE GEOMETRY
   AT ALL? The position is set on alpha itself as gauge... ALPHA ALONE SETS THE WHOLE
   ENTIRETY OF EVERYTHING and all we are doing here is doing a thorough job of dropping
   every forced anchor. THE THALES CIRCLE SETS ITSELF, centred on the edge of the hole
   closest to the hinge and spanning from the hole centre to the hinge... Every point and
   circle all determined by the one circle at the centre. THE HOLE. Which is what MAKES
   it a kaleidoscope."

I called 2 alpha a choice. TEST WHETHER IT IS ONE.
The test that could go either way: is there a construction, using ONLY the hole, that
LANDS on 2 alpha? If yes, 2 alpha is output, not input, and my "one free choice" is wrong.
"""
import numpy as np

a = 1.0
print("="*78)
print("(1)  THE THALES CIRCLE 'SETS ITSELF' — does it? And where does it land?")
print("="*78)
print("  Daryl's spec, verbatim: 'centred on the EDGE OF THE HOLE closest to the hinge,")
print("  and SPANNING FROM THE HOLE CENTRE TO THE HINGE.'")
print()
print("  Build it from the hole alone. The hole: centre O=(0,0), radius alpha.")
print("  Its edge, on the axis: E = (alpha, 0).   <- the ONLY point 'the edge, that way' can mean")
print("  A circle centred at E and passing through O has radius |EO| = alpha.")
print("     -> the Thales circle IS THE HOLE, TRANSLATED TO SIT ON ITS OWN EDGE.")
print("  Its far intersection with the axis is at E + alpha = 2 alpha.")
O = np.array([0.0, 0.0]); E = np.array([a, 0.0])
r_thales = np.linalg.norm(E - O)
far = E + np.array([r_thales, 0.0])
print(f"     radius = |EO| = {r_thales:.6f} alpha      far end = {far[0]:.6f} alpha")
print()
print("  >> ** THE HINGE IS NOT PLACED. IT IS WHERE THE THALES CIRCLE ENDS. **")
print("     And the Thales circle is not placed either -- it is the hole, moved by its own")
print("     radius, in the only direction the axis offers. NOTHING WAS CHOSEN.")
print("     ** 2 alpha is OUTPUT, not input. My 'one free choice' was WRONG. **")

print()
print("="*78)
print("(2)  So what does the hole alone determine? Follow it through with NO other input.")
print("="*78)
X0 = np.sqrt(far[0]**2 - a**2)
power = far[0]**2 - a**2
L_tan = np.sqrt(power)
ang = np.degrees(np.arctan2(X0, a))
chain = [
 ("the hole",                     f"centre O, radius alpha = {a:.4f}",              "GIVEN — the only object"),
 ("its edge on the axis",         f"E = ({E[0]:.4f}, 0)",                            "forced: |OE| = alpha"),
 ("the Thales circle",            f"centre E, radius {r_thales:.4f} = alpha",        "forced: passes through O"),
 ("THE HINGE",                    f"({far[0]:.4f}, 0) = 2 alpha",                    "forced: the circle's far end"),
 ("its height on dS",             f"X0 = {X0:.6f} = sqrt(3) alpha",                  "forced: -X0^2+|X|^2 = alpha^2"),
 ("its power w.r.t. the hole",    f"{power:.6f} = 3 alpha^2",                        "forced: = X0^2 (r1107)"),
 ("its tangent length",           f"{L_tan:.6f} = sqrt(3) alpha",                    "forced: = sqrt(power)"),
 ("the ruling angle",             f"{ang:.4f} deg = 60",                             "forced: arctan(X0/alpha)"),
 ("the hinge circle",             f"radius 2 alpha, DIAMETER {2*far[0]:.4f} = 4 alpha","forced: the hinges live on it"),
]
print(f"  {'object':<28} {'value':<34} why")
for n, v, w in chain:
    print(f"  {n:<28} {v:<34} {w}")
print()
print("  >> NINE OBJECTS. ONE INPUT: alpha. AND alpha IS THE GAUGE -- it is not a number,")
print("     it is THE UNIT. Set alpha=1 and the construction has NO free parameters at all.")
print("     ** Daryl is right: alpha alone sets the entirety. The rest is alpha, re-read. **")

print()
print("="*78)
print("(3)  THE TANGENCY — is even THAT forced, or is it a happy accident of 2 alpha?")
print("="*78)
print("  The hinge triangle's sides are tangent to the hole, touching at their MIDPOINTS.")
print("  For an equilateral triangle of circumradius R, the inradius is R/2 and the incircle")
print("  touches at the side midpoints. So the sides are tangent to the hole IFF R/2 = alpha,")
print("  i.e. IFF R = 2 alpha.")
Rtri = 2*a
h = [Rtri*np.array([np.cos(np.deg2rad(d)), np.sin(np.deg2rad(d))]) for d in (0,120,240)]
mids = [(h[i]+h[(i+1)%3])/2 for i in range(3)]
print(f"     circumradius R = {Rtri:.4f} alpha  ->  inradius = {np.linalg.norm(mids[0]):.6f} alpha")
print(f"     tangent to the hole?  {np.isclose(np.linalg.norm(mids[0]), a)}")
print()
print("  >> ** THE TANGENCY IS NOT A BONUS OF 2 alpha. IT IS THE SAME FACT. **")
print("     The hinge sits at 2 alpha because the Thales circle ends there; the triangle on")
print("     those hinges has inradius alpha because 2alpha/2 = alpha; so its sides are")
print("     tangent to the hole. ONE FACT, THREE READINGS.")
print("     (And this is why the 2:1 that killed the su(3) identification is not a defect")
print("      either -- it is the SAME 2. The rotation, the ratio, the tangency and the")
print("      hinge's placement are one statement. I logged the 2:1 as a cause of death and")
print("      never noticed it was the construction's own signature.)")

print()
print("="*78)
print("(4)  WHERE I WAS WRONG, precisely — and what it does to the 30-degree walk")
print("="*78)
print("  I wrote (thirty_degrees.py): 'the kaleidoscope's 4 is CHOSEN. The stamp contains")
print("  3-fold structure, 2-fold structure (the poles), and orthogonalities -- but no 4-fold")
print("  ORBIT. Every n coprime to 3 closes evenly; the geometry does not prefer 4.'")
print()
print("  THAT TEST IS STILL SOUND -- as a test of the STAMP as I had it: a figure in a plane,")
print("  asking which rotations close. But it took the stamp as GIVEN and asked what could be")
print("  done TO it. Daryl's claim is upstream of that: he is not asking which rotation to")
print("  apply, he is saying THE FIGURE'S EVERY LENGTH IS alpha RE-READ, so the question")
print("  'which n?' is asking the wrong object -- it treats a rotation as an input to a")
print("  construction that has no inputs.")
print()
print("  ** WHAT I CANNOT SETTLE HERE, AND WILL NOT PRETEND TO: whether the 90-degree shifts")
print("     are forced. ** Daryl names two right angles that ARE in the construction and are")
print("     NOT choices: (i) THALES ITSELF -- every point of the Thales circle sees O-to-hinge")
print("     at 90 degrees; that is what a Thales circle IS; (ii) 'the hinge's own CONJUGATE")
print("     circle set by the PERPENDICULAR slicing curve'. Both are 90s the hole hands you.")
print("     My test asked whether the stamp has a 4-fold ROTATIONAL ORBIT and answered no.")
print("     That does not answer whether a right angle the construction ALREADY CONTAINS")
print("     generates the four. ** DIFFERENT QUESTION. MINE DID NOT REACH IT. **")
print()
print("  NAMED, UNRUN, and now sharper than 'can the Thales tangent derive the quarter turn':")
print("     what IS the hinge's conjugate circle -- the one set by the perpendicular slicing")
print("     curve? Daryl says it has its own radius. COMPUTE IT. If it is forced by the hole")
print("     the way the Thales circle is, then the 90 is in the construction and the 12 is")
print("     3 x 4 with BOTH factors forced -- and the two 30s become one after all.")

# ── APPENDED ASSERT-VERIFICATION (r1339, Arthur) — self-check + discriminating control ──
import numpy as _np
_a = 1.0
_thales_far = _a + _a                                   # Thales circle from the hole: far end
assert abs(_thales_far - 2*_a) < 1e-12,               "2a is the Thales far end"
_X0 = _np.sqrt((2*_a)**2 - _a**2)                       # -X0^2+|X|^2=a^2 at |X|=2a
assert abs(_X0 - _np.sqrt(3)*_a) < 1e-12,             "height = sqrt3 a"
_power = _X0**2
assert abs(_power - 3*_a**2) < 1e-12,                 "power = X0^2 = 3 a^2"
assert abs(_np.sqrt(_power) - _np.sqrt(3)*_a) < 1e-12,"tangent length = sqrt3 a"
assert abs(_np.degrees(_np.arctan2(_X0, _a)) - 60) < 1e-9, "ruling angle 60 deg"
# CONTROL: equilateral inradius=R/2 is tangent to the hole (radius a) ONLY at R=2a
_hits = [R for R in (1.0,1.5,2.0,2.5,3.0) if abs(R/2 - _a) < 1e-9]
assert _hits == [2.0],                                "tangency forced ONLY at R=2a"
print("\n>> AVENUE 11 ASSERTS PASSED: every anchor forced from alpha; 2a = Thales far end; tangency only at R=2a.")
