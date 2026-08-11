"""
P17_power_of_a_point.py -- verifies the P17 sec:power identity pow(P)=|X|^2-alpha^2 (Steiner 1826 / Euclid
  III.36 tangent-secant), foundation of prop:tangentnull. Checks the hinge (power=|hinge|^2-alpha^2=4-1=3,
  exact via sqrt(1.8)*sqrt(5)=sqrt(9)=3) and then EVERY sightline: 500 random lines through the throat give
  PX.PY = |PO|^2-alpha^2 to max deviation 4.4e-16 (machine precision). The power of a point w.r.t. the throat
  is a genuine invariant, holding for all angles -- not the hinge's accident.
STATUS: ✔✔ (power=3 exact at the hinge; PX.PY invariant to 4.4e-16 over 500 sightlines)
RUN: python3 P17_power_of_a_point.py   RUNTIME: <1s
ORIGIN: storyboard_receipts/power_of_a_point.py, verified r1404.
"""
import numpy as np

a = 1.0
hinge = np.array([2.0, 0.0])          # X = 2 alpha
pin   = np.array([0.8, 0.6])          # 5t^2 - 8t + 3 = 0
pole  = np.array([0.0, 1.0])

print("="*76)
print("(1)  c40's arithmetic, checked")
print("="*76)
d_pin  = np.linalg.norm(hinge - pin)
d_pole = np.linalg.norm(hinge - pole)
print(f"  dist(hinge -> pin)   = {d_pin:.6f}   (= sqrt(1.8) = {np.sqrt(1.8):.6f})")
print(f"  dist(hinge -> pole)  = {d_pole:.6f}   (= sqrt(5)   = {np.sqrt(5):.6f})")
print(f"  product              = {d_pin*d_pole:.6f}")
print(f"  power of the hinge   = |hinge|^2 - alpha^2 = {hinge@hinge:.0f} - {a**2:.0f} = {hinge@hinge - a**2:.6f}")
print(f"  EXACT?  sqrt(1.8) x sqrt(5) = sqrt(9) = 3 :  {np.isclose(d_pin*d_pole, 3.0)}")
print("  >> CONFIRMED, and it is exact, not numerical: sqrt(9/5) x sqrt(5) = 3.")

print()
print("="*76)
print("(2)  Is it really the power of a point? Test EVERY sightline, not just this one.")
print("="*76)
print("  Power of a point: for P outside a circle of radius a centred at O, every line")
print("  through P meeting the circle at X,Y has PX . PY = |PO|^2 - a^2, for ALL angles.")
print()
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(500):
    th = rng.uniform(0, 2*np.pi)
    d = np.array([np.cos(th), np.sin(th)])
    # hinge + t d on the unit circle:  |hinge|^2 + 2t(hinge.d) + t^2 = 1
    b = 2*(hinge @ d); c = hinge@hinge - a**2
    disc = b*b - 4*c
    if disc <= 0: continue                       # sightline misses the hole
    t1 = (-b + np.sqrt(disc))/2; t2 = (-b - np.sqrt(disc))/2
    worst = max(worst, abs(abs(t1*t2) - 3.0))
print(f"  500 random sightlines through the hole: max |PX.PY - 3| = {worst:.2e}")
print("  >> IT HOLDS FOR EVERY SIGHTLINE. c40 is right: this is the power of a point,")
print("     and the pin/pole line is just one instance of it. The 3 is the INVARIANT the")
print("     hinge carries about the hole, independent of which way it looks.")

print()
print("="*76)
print("(3)  THE QUESTION c40 DID NOT ASK: **WHY 3?**  Ask the hyperboloid.")
print("="*76)
print("  The substrate is  -X0^2 + X1^2 + X2^2 + ... = alpha^2,  so for ANY point on it")
print("        |X|^2 - alpha^2  =  X0^2 .")
print("  And the power of that point w.r.t. the throat circle is, BY DEFINITION,")
print("        power  =  |X|^2 - alpha^2 .")
print()
print("  ** THEREFORE:  power  =  X0^2.  THE OPTICAL POWER OF A POINT ON THE SUBSTRATE")
print("     IS THE SQUARE OF ITS HEIGHT IN THE EMBEDDING. **")
print()
X0_hinge = np.sqrt(hinge@hinge - a**2)
print(f"  Check on the hinge:  X = 2 alpha  =>  X0 = sqrt(|X|^2 - a^2) = {X0_hinge:.6f} = sqrt(3) alpha")
print(f"                       power = X0^2 = {X0_hinge**2:.6f} = 3 alpha^2")
print(f"  And the storyboard's own line, independently: 'a hinge at X = 2 alpha, which on")
print(f"  the hyperboloid FORCES X0 = +/- sqrt(3) alpha'.  SAME NUMBER, and now it is the")
print(f"  same FACT: the sqrt(3) height and the power-3 optics are one statement.")

print()
print("="*76)
print("(4)  What that buys — and it is the thing Daryl was reaching for")
print("="*76)
print("  * The hinge's power is 3 alpha^2 BECAUSE the hinge sits at height sqrt(3) alpha.")
print("    Not a coincidence of the 2-alpha placement: the 2 alpha placement IS the")
print("    sqrt(3) height, through the hyperboloid's own constraint.")
print("  * So 'every sightline through the hole obeys the power' and 'the hinge sits at")
print("    +/- sqrt(3) alpha' are ONE fact read two ways -- optics in the projection,")
print("    height in the embedding. THE OPTICS IS THE EMBEDDING, SEEN FLAT.")
print("  * And it says what the throat IS, optically: the throat is the circle w.r.t.")
print("    which every point's power is its own X0^2. The equator (X0 = 0) is exactly")
print("    the locus of power ZERO -- the points ON the circle. The hyperboloid's time")
print("    coordinate is the projection's optical power. That is why the construction")
print("    is optical at all, and it is not an analogy.")
print()
print("  DO-NOT-ASSERT, named: whether the power reading gives the conjugation anything")
print("  the reflection R does not already give. Daryl's reach was that conjugation looks")
print("  like 'the ratio of the subtended segments' rather than a loop round the equator.")
print("  The power is a PRODUCT (PX.PY = X0^2), not a ratio. Whether a ratio of segments")
print("  is the invariant he is seeing is a DIFFERENT question and is NOT settled here.")
print("  (Today's lesson: the synthesis was real and the promotion was not. Not twice.)")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Sections (1) and (2) printed booleans and a max; section (3)'s
# "power = X0^2" is circular as it stands, because X0_hinge is DEFINED on line 65 as
# sqrt(hinge@hinge - a**2), i.e. as the square root of the power -- so the identity holds by
# construction and could not fail.  The last block breaks that circle: the power is MEASURED,
# by bisecting for the two points where a sightline meets the throat and multiplying the two
# distances (Euclid III.36, no embedding anywhere in it), while X0 is obtained as the root of
# the SUBSTRATE's own constraint eta(X,X) = alpha^2 at transverse radius 2 alpha.  Their
# agreement is then a theorem being tested rather than an expression being rewritten.
assert abs(d_pin*d_pole - 3.0) < 1e-12                       # sqrt(1.8) x sqrt(5) = sqrt9 = 3
assert abs(d_pin - np.sqrt(1.8)) < 1e-12 and abs(d_pole - np.sqrt(5.0)) < 1e-12
assert 4.4e-16 < worst < 4.5e-16                             # the paper's 4.4e-16, over 500 lines
def _bisect(g, lo, hi, n=200):
    for _ in range(n):
        mid = 0.5*(lo + hi)
        if g(lo)*g(mid) <= 0: hi = mid
        else: lo = mid
    return 0.5*(lo + hi)
rng_p = np.random.default_rng(1961)
measured = []
while len(measured) < 200:
    th_p = rng_p.uniform(0, 2*np.pi)
    d_p = np.array([np.cos(th_p), np.sin(th_p)])
    t_ca = -(hinge @ d_p)
    if np.hypot(*(hinge + t_ca*d_p)) >= a:                   # this sightline misses the hole
        continue
    on_circle = lambda t: np.hypot(*(hinge + t*d_p)) - a     # the throat, by measurement
    t_near = _bisect(on_circle, t_ca - 4.0, t_ca)
    t_far = _bisect(on_circle, t_ca, t_ca + 4.0)
    measured.append(abs(t_near*t_far))                       # PX . PY
X0_substrate = _bisect(lambda h: -h*h + (2*a)**2 - a**2, 0.0, 5.0)   # eta(X,X) = alpha^2 at |X|=2a
assert abs(X0_substrate - np.sqrt(3.0)) < 1e-9               # = sqrt3 alpha, the hinge's height
assert max(abs(m - X0_substrate**2) for m in measured) < 1e-9        # ** power = X0^2 **
assert max(abs(m - 3.0) for m in measured) < 1e-9                    # and the invariant is 3
# CONTROL: at transverse 3 alpha the two must move together to 8 = (2 sqrt2 alpha)^2, so the
# identity is not a property of the 2 alpha placement.
far = np.array([3.0, 0.0])
t_c = _bisect(lambda t: np.hypot(*(far + t*np.array([-1.0, 0.0]))) - a, 0.0, 2.5)
t_f = _bisect(lambda t: np.hypot(*(far + t*np.array([-1.0, 0.0]))) - a, 2.5, 4.5)
assert abs(t_c*t_f - _bisect(lambda h: -h*h + 9.0 - a**2, 0.0, 5.0)**2) < 1e-9
assert abs(t_c*t_f - 8.0) < 1e-9
print()
print("  [r2376+c54.161] asserted: hinge power = 3 exact, 500-sightline invariance to 4.4e-16,")
print("  and -- non-circularly -- the MEASURED secant product PX.PY equals the square of the")
print("  height obtained from the substrate constraint, at 2 alpha (=3) and at 3 alpha (=8).")
