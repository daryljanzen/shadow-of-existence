"""
P08_nariai_signed_roots.py -- the SIGNED Nariai root structure behind P8 sec:open's
"where the forced scale 2/sqrt3 sits". VERDICT: the magnitude 2/sqrt3 is carried by FOUR
distinct quantities (Nariai offset |r_0|, ellipse focal distance, throat-image radius, and
the lone/backward-radial ROOT) of which only the last is signed and only the last is a root;
on the M>0 member the pair is degenerate at +1/sqrt3 and the lone root is -2/sqrt3, the signs
being one vantage's (P2 sec:ring). [P8 slicing_operator sec:open]
STATUS: OK   ORIGIN: storyboard_receipts/nariai_signed_roots.py, built r1612.
"""
import numpy as np

s3 = np.sqrt(3)
TOL = 1e-12

def roots_of(twoM):
    """the three horizon roots at a given 2M, sorted ascending"""
    return np.sort(np.roots([1.0, 0.0, -1.0, twoM]).real)

def twoM_of(r0):
    """the mass the offset r_0 designates"""
    return r0 - r0**3

# ---------------------------------------------------------------- 1. the Nariai masses
twoM_crit = 2/(3*s3)
disc = lambda twoM: -4*(-1)**3 - 27*twoM**2      # discriminant of r^3 - r + 2M
assert abs(disc(+twoM_crit)) < 1e-12, "‑ +2/(3sqrt3) is not a double-root mass"
assert abs(disc(-twoM_crit)) < 1e-12, "‑ -2/(3sqrt3) is not a double-root mass"
print(f"1. Nariai masses: 2M = +/- {twoM_crit:.9f}  (= +/- 2/(3sqrt3));  discriminant 0 at both.")

# ------------------------------------------------- 2. the signed roots at each member
rp = roots_of(+twoM_crit)      # the M>0 member -- the one the cosmology selects
rm = roots_of(-twoM_crit)      # the R-conjugate member
print(f"2. M>0 member (2M=+2/(3sqrt3)): roots = {np.round(rp,9)}")
print(f"   M<0 member (2M=-2/(3sqrt3)): roots = {np.round(rm,9)}")

# M>0: double root at +1/sqrt3, lone root at -2/sqrt3
assert abs(rp[1] - 1/s3) < 1e-8 and abs(rp[2] - 1/s3) < 1e-8, "M>0 pair not at +1/sqrt3"
assert abs(rp[0] + 2/s3) < 1e-8, "M>0 lone root not at -2/sqrt3"
# M<0: the exact mirror
assert abs(rm[0] + 1/s3) < 1e-8 and abs(rm[1] + 1/s3) < 1e-8, "M<0 pair not at -1/sqrt3"
assert abs(rm[2] - 2/s3) < 1e-8, "M<0 lone root not at +2/sqrt3"
assert np.allclose(np.sort(-rp), rm, atol=1e-8), "the two members are not R-conjugate"
print("   -> M>0: DOUBLE at +1/sqrt3, LONE at -2/sqrt3.   M<0: the exact negation.")
print("   -> R (r -> -r) carries the whole set to the conjugate reading: P2 sec:ring's caveat holds.")

# ------------------------------------------------ 3. a doubled root sits at ONE value
assert abs(rp[1]-rp[2]) < 1e-9, "the pair is not degenerate"
print("3. The merged pair is DEGENERATE -- one value, not two -- so '-/+1/sqrt3' cannot name it.")

# ------------------------------------- 4. the offset is not the root (though it is A root)
for r0 in (+2/s3, -2/s3):
    tm = twoM_of(r0)
    rs = roots_of(tm)
    assert min(abs(rs - r0)) < 1e-8, "r_0 must itself be a root"
    lone = rs[0] if abs(rs[1]-rs[2]) < 1e-9 else rs[2]
    print(f"4. offset r_0 = {r0:+.6f} designates 2M = {tm:+.9f}; roots {np.round(rs,6)}; "
          f"r_0 IS the lone root ({lone:+.6f}) -- so offset and root COINCIDE here, "
          f"which is how the conflation got in.")
# the sign that matters: which offset gives the cosmology's M>0 member?
assert twoM_of(-2/s3) > 0 and twoM_of(+2/s3) < 0
print("   -> and the sign is the point: r_0 = -2/sqrt3 gives 2M>0 (the cosmology's member),")
print("      r_0 = +2/sqrt3 gives 2M<0. P3 sec:ellipse's (r_0, r) = (+/-2/sqrt3, -/+1/sqrt3) is")
print("      an (OFFSET, ROOT) pair -- reading both entries as roots is the error.")

# ------------------------------- 5. 'larger' is true in magnitude only, false in value
assert abs(-2/s3) > abs(1/s3)          # magnitude
assert (-2/s3) < (1/s3)                # value, on the M>0 member
print("5. 'the LARGER of the two Nariai roots': true in MAGNITUDE (2/sqrt3 > 1/sqrt3),")
print("   FALSE in value on the M>0 member (-2/sqrt3 < +1/sqrt3). The word needs 'in magnitude'.")

# --------------------- 6. the four distinct quantities that all have magnitude 2/sqrt3
M_ = np.array([[1,0.5],[0.5,1]])                      # r^2 + r r_0 + r_0^2 = 1
ev = np.linalg.eigvalsh(M_)
a, b = 1/np.sqrt(ev.min()), 1/np.sqrt(ev.max())       # semi-axes sqrt2, sqrt(2/3)
focal = np.sqrt(a**2 - b**2)
quantities = {
    "Nariai offset |r_0|         (a slicing parameter)": 2/s3,
    "ellipse focal distance      (a distance on the major axis)": focal,
    "throat-image radius         (gnomonic, on the sky)": 2/s3,
    "lone root, M>0 member       (a SIGNED areal radius)": -2/s3,
}
print("6. Four distinct quantities, all of magnitude 2/sqrt3 -- P3's abstract warns these are")
print("   'never to be conflated'. Only the last is signed, and only the last is a root:")
for k, v in quantities.items():
    print(f"     {k:<58} = {v:+.9f}")
assert abs(focal - 2/s3) < 1e-12
assert quantities["lone root, M>0 member       (a SIGNED areal radius)"] < 0
print("\nVERIFIED: the signed structure, the degeneracy, the offset/root distinction, and the")
print("four same-magnitude quantities. The correction is to NAME the quantity and the vantage,")
print("not to flip a sign -- flipping alone would privilege one vantage, which P2 forbids.")
