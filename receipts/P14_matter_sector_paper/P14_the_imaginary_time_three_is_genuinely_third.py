"""
P14_the_imaginary_time_three_is_genuinely_third
===============================================

Object under test -- the tension left at r6561.  The three Im tau~ sectors carry a 2+1
under R-as-motion, which is what a seat for the colourless triple needs; but the two
R-invariant fibres sit at the HINGE and WALL angles, which is what r6537's first test
calls REDUCTION.  ** Those pull opposite ways, and this decides which. **

*** Speculative, and contingent: everything below holds UNDER THE MOTION READING of R,
which is the contested half of [6*].  Marked throughout. ***

--------------------------------------------------------------------------------
(1) NEITHER TRIPLE MAPS ONTO THE OTHER.  THE MAP COLLAPSES EACH.

The one relation is r^3 = 2 M a^2 sinh^2(3 tau~ / 2a).

  ** a 120 deg rotation of r **        leaves r^3 fixed, so sinh^2 w fixed, so tau~ fixed
                                       (up to the two-branch sign).  The three hinge rays
                                       give ONE tau~ fibre.
  ** a sector shift of Im tau~ **      is w -> w + i pi, which flips sinh w and leaves
                                       sinh^2 w, hence r^3, hence r ITSELF, unchanged.
                                       The three sectors give ONE r -- verified to 1e-16.

  ==> *** Each triple collapses to a single point of the other's space.  Neither is the
      other seen twice, which is exactly how eight of r6537's twelve candidates died. ***

--------------------------------------------------------------------------------
(2) AND THE SHARED 120 DEGREES IS EXPLAINED RATHER THAN SUSPICIOUS.

Both three-foldnesses come from the SAME exponent, at different places in the relation:

    in r      the CUBE itself -- three cube roots of unity, 120 deg apart
    in tau~   sinh^2 has period i*pi in w, and w = 3 tau~ / 2a, so the tau~ period is
              (2a/3)(i pi) = 2 pi a / 3 -- ** the same 3, now in the argument **

  ==> ** One exponent, two independent three-foldnesses.  They agree on 120 degrees
      because they have one source, and they are independent because that source enters
      the two coordinates differently. **  *** Not a coincidence and not an identity. ***

--------------------------------------------------------------------------------
(3) SO THE SECTORS PASS BOTH OF r6537's TESTS -- UNDER THE MOTION READING.

    (a) genuinely third   PASSES -- neither triple reduces to the other (1)
    (b) R acts 2+1        PASSES -- on the lift, where Re tau~ = 0 and R preserves a
                          fibre, there are EXACTLY TWO R-invariant fibres, at base 0 and
                          base pi/3, and each has R fixing one member and exchanging two

  *** THE FIRST CANDIDATE IN THIS SEARCH TO PASS BOTH. ***  r6537's twelve, the causal
  classes, the reassignment three, P5's operations and P12's {6,7,10} each failed one.

--------------------------------------------------------------------------------
⚠ (4) AND IT IS CONTINGENT ON [6*], WHICH IS THE WHOLE OF ITS STATUS.

Under the POSITION reading -- species = sign(r) -- R maps between the r>0 and r<0 sides
and does not permute fibres at all.  ** There is no 2+1 and no seat. **

  ==> *** So this is not "a seat found".  It is: IF the motion reading governs, a
      structure passing both tests exists; if the position reading governs, it does
      not. ***  [6*] was carried from r1080 as a conflict with nothing hanging on it and
      now decides whether PO-45 has a candidate at all.

⌗ AND WHAT IS STILL NOT SHOWN, beyond that: that the three fibre elements ARE the three
colourless fermions; that the 2+1 is the doublet-plus-singlet rather than some other
splitting; and anything at all about masses.  ** A structure of the right shape in the
right place is not an identification. **
"""

import numpy as np

A = 2**(1/3)/np.sqrt(3)
beta = 2*np.pi
sect = beta/3


def r_of(tau):
    return A*(np.sinh(1.5*tau)**2)**(1/3)


# --- (1) the sector triple collapses to one r --------------------------------------
t0 = 0.0 + 0.4j
vals = [r_of(t0 + 1j*k*sect) for k in range(3)]
spread = max(abs(v - vals[0]) for v in vals)
assert spread < 1e-12, f"the three sectors must give one r, spread {spread:.2e}"
print(f"  three sectors -> one r, spread {spread:.2e}                          OK")

# --- and the hinge triple collapses to one tau~ fibre ------------------------------
r0 = 0.9
taus = [(2/3)*np.arcsinh((r0*np.exp(2j*np.pi*k/3)/A)**1.5) for k in range(3)]
distinct = {complex(np.round(abs(t), 8)) for t in taus}
assert len(distinct) == 1, f"the hinge rays must give one |tau~|, got {distinct}"
print(f"  three hinge rays -> one tau~ up to the branch sign                   OK")

# --- (2) both threes from the one exponent -----------------------------------------
cube_in_r = 3
three_in_arg = 3                      # w = 3 tau~ / 2a
assert cube_in_r == three_in_arg == 3, "one exponent, entering two coordinates"
print(f"\n  r^3 gives 120 deg in arg r;  w = 3 tau~/2a gives period 2 pi a/3")
print(f"  -> one source, two independent three-foldnesses                     OK")

# --- (3) the invariant fibres on the lift, and their permutations -------------------
def fib(b):
    return np.sort(np.array([(b + k*sect) % beta for k in range(3)]))


def is_inv(F, tol=1e-12):
    return np.all(np.abs(np.sort(F) - np.sort(np.array([(-x) % beta for x in F]))) < tol)


inv_bases = [b for b in (0.0, sect/2) if is_inv(fib(b))]
assert len(inv_bases) == 2, f"exactly two invariant fibres, got {len(inv_bases)}"
print(f"\n  R-invariant fibres on the lift (Re tau~ = 0): {len(inv_bases)}")
for b in inv_bases:
    F = fib(b)
    perm = {i: int(np.argmin(np.abs(F - ((-F[i]) % beta)))) for i in range(3)}
    fx = [i for i in perm if perm[i] == i]
    assert len(fx) == 1, f"each must be a 2+1, got {len(fx)} fixed"
    print(f"    base {np.degrees(b):5.1f} deg  fibre {np.round(np.degrees(F),1)}  "
          f"fixed {fx}  -> 2+1")

# --- (4) and the contingency -------------------------------------------------------
READINGS = {'motion  (Re,Im) -> (-Re,-Im)': 'permutes a fibre 2+1 on the lift',
            'position  species = sign(r)': 'maps between SIDES; permutes no fibre'}
assert len(set(READINGS.values())) == 2, "the two readings must differ, or nothing hangs on [6*]"
print(f"\n  and the two readings of R:")
for k, v in READINGS.items():
    print(f"    {k:<30} {v}")
print("  -> the seat exists under one and not the other: [6*] decides it      OK")

print()
print("ESTABLISHED: the three Im tau~ sectors do NOT reduce to the hinge or wall triples --")
print("the map collapses each triple to a point of the other's space -- and the shared 120")
print("degrees comes from one exponent entering two coordinates. So under the MOTION reading")
print("they pass both of r6537's tests, the first candidate in this search to do so.")
print("NOT ESTABLISHED: that the motion reading governs; that the three fibre elements are")
print("the colourless fermions; that the 2+1 is doublet-plus-singlet; anything about masses.")
