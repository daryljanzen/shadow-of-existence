"""
IS sigma A LIGHT-PATH?  (r1110)  Successor to U1c_the_light_path.py.

WHERE THIS STANDS. U1c found tau IS a light-path: two ruling-steps = a dial turn of 120 =
tau, six steps = tau^3 = id, the 6-cycle. And it found the asymmetry:

    ** THE RULINGS GIVE tau AND NOT sigma. ** No walk on the 24-hinge graph produces the
    root-exchange. P5 gives sigma and tau equal standing as D_3's two generators; the light
    cone does not.

It named the successor: is sigma a light-path at the NARIAI member, where the cut degenerates
into the two null rulings themselves (thales_is_the_dial.py tab18) and sigma has its fixed
point (w=30)? "That is the one place sigma and the rulings are forced to meet."

** THE SOURCE, PULLED FIRST RATHER THAN RE-DERIVED (P5 prop:monodromy, read at source): **
    "The monodromy of the horizon cubic about a Nariai branch point is the transposition
     exchanging the two roots that collide there... sigma IS THE ANALYTIC CONTINUATION of the
     slicing description ONCE AROUND the configuration at which its two designated horizons
     merge."
    proof: "continuing the roots along 2M = 2M* + eps.e^{i.phi}, phi: 0 -> 2pi"

** THAT ALREADY ANSWERS PART OF IT, AND I NEARLY MISSED IT BY ASKING THE FIGURE INSTEAD OF
   THE PAPER. ** sigma is a loop in the COMPLEX 2M-PLANE. A ruling is a real null line in the
substrate. Those are not the same kind of object and not in the same space. So the question
is not "which walk is sigma" -- it is:

    Q1  does sigma act on the two Nariai rulings at all, and how -- fix each, or swap them?
    Q2  is sigma's fixed point (w=30) the SAME degeneracy as the cut's (d=alpha)?
    Q3  and the honest one: is "is sigma a light-path" even a well-posed question, given
        prop:monodromy says sigma lives in complex 2M and the rulings live in real X?

COULD THIS RETURN OTHERWISE? Yes: Q1 is a computation on the two rulings; Q2 compares two
independently-computed degeneracy loci; and Q3's answer could be "yes, via the continuation"
if the monodromy's loop had a real shadow on the rulings -- which is checkable and is checked.
"""
import numpy as np

a = 1.0
S3 = np.sqrt(3)

def roots_of(M2):
    """the three horizon roots: r^3 - r + 2M = 0  (alpha=1)."""
    return np.roots([1.0, 0.0, -1.0, M2])

print("="*80)
print("0. THE TWO DEGENERACIES, COMPUTED SEPARATELY -- are they the same locus?  (Q2)")
print("="*80)
# (i) sigma's fixed point: sigma(r0) = 1/2(-r0 + sqrt(4 - 3 r0^2)),  fixed at r0 = 1/sqrt3
def sigma_r0(r0):
    return 0.5*(-r0 + np.sqrt(4 - 3*r0**2))
r0N = 1/S3
print(f"  sigma's fixed point:   sigma({r0N:.6f}) = {sigma_r0(r0N):.6f}   fixed: {abs(sigma_r0(r0N)-r0N)<1e-12}")
# (ii) the cut's degeneracy: d = alpha, the plane tangent to the throat
#      the dial: r0 = (2/sqrt3) sin w ; at w=30, r0 = (2/sqrt3)(1/2) = 1/sqrt3
w_deg = 30.0
r0_dial = (2/S3)*np.sin(np.radians(w_deg))
print(f"  the dial at w=30:      r0 = (2/sqrt3) sin 30 = {r0_dial:.6f}")
# (iii) the cubic's discriminant zero
M2N = r0N - r0N**3
disc = 4 - 27*M2N**2
print(f"  the cubic's branch pt: 2M = {M2N:.6f} = 2/(3 sqrt3) = {2/(3*S3):.6f}   discriminant = {disc:.2e}")
assert abs(sigma_r0(r0N)-r0N) < 1e-12 and abs(r0_dial - r0N) < 1e-12 and abs(disc) < 1e-12
print(f"""
  ** ALL THREE ARE ONE LOCUS: r0 = alpha/sqrt3, w = 30, 2M = 2/(3 sqrt3), discriminant = 0. **
  sigma's fixed point, the dial's tangency, and the cubic's branch point coincide. Q2: YES.
  (This is not new -- it is one_thirty.py's chain read backwards -- but it had to be checked
  here, because the whole question is whether the two objects meet AT ALL.)""")

print("\n" + "="*80)
print("1. THE CUT AT NARIAI IS THE TWO RULINGS -- re-verified, since everything rests on it")
print("="*80)
# the plane at perpendicular distance d from the axis cuts -X0^2 + s^2 = d^2 - alpha^2
for d, name in [(2*a, "the hinge's own vertex"), (1.2*a, "overcritical"),
                (a, "** NARIAI **"), (0.5*a, "undercritical")]:
    rhs = d**2 - a**2
    kind = ("two-sheeted hyperbola" if rhs > 1e-12 else
            "TWO STRAIGHT NULL LINES  s = +-X0" if abs(rhs) < 1e-12 else "one-sheeted (secant)")
    print(f"  d = {d:.4f}  ({name:>22}) :  X0^2 - s^2 = {rhs:+.4f}   ->  {kind}")
print("""
  ** At d = alpha the conic degenerates: X0^2 = s^2, i.e. s = +-X0 -- two straight lines,
  and each is null (spatial run = time drop). THE CUT AT NARIAI IS THE TWO RULINGS. **""")

print("\n" + "="*80)
print("2. Q1 -- DOES sigma ACT ON THE TWO RULINGS?  (fix each, or swap them?)")
print("="*80)
print("""  sigma exchanges the two roots that collide at Nariai. AT Nariai those two roots ARE one
  number -- the double root r = alpha/sqrt3. So ask what sigma exchanges, approaching:""")
print(f"\n  {'2M':>12} {'the three roots':>34} {'the colliding pair':>22}")
for eps in [0.06, 0.02, 0.004, 0.0]:
    M2 = M2N - eps
    rr = np.sort(roots_of(M2).real[abs(roots_of(M2).imag) < 1e-9])
    pair = [x for x in rr if x > 0]
    print(f"  {M2:>12.6f} {str(np.round(rr,5)):>34} {str(np.round(pair,5)):>22}")
print(f"""
  ** The colliding pair are the TWO POSITIVE roots. They merge at 2M = 2/(3 sqrt3) into the
  double root {r0N:.6f} = alpha/sqrt3. The third root ({-2/S3:.5f} = -2alpha/sqrt3) is FIXED by
  sigma -- it is the backward-radial root and it does not collide. **""")

print("""
  NOW THE RULINGS. At Nariai the cut is s = +X0 and s = -X0 -- two null lines. Do the two
  colliding ROOTS correspond to the two RULINGS? Check by counting, which is the honest test:""")
print(f"    the colliding roots     : 2   (the two positive horizons, merging)")
print(f"    the third root          : 1   (backward-radial, fixed by sigma)")
print(f"    the rulings at Nariai   : 2   (s = +X0 and s = -X0)")
print("""
  ** TWO AND TWO. The count matches -- which is exactly the kind of match this corpus forbids
  taking for a finding (the adjective/flavour trap, faces 18/19/26). A count is not a map. **
  So test it properly: the rulings are objects at ONE member (Nariai). The colliding roots are
  objects of the FAMILY -- they exist as two only OFF Nariai, and at Nariai they are one
  number. ** The rulings are two AT the point where the roots are ONE. ** The two 2s are not
  in the same place: one is the degeneracy's cause, the other is its consequence, and they
  live at different values of 2M.""")

print("\n" + "="*80)
print("3. ** Q3 -- AND THIS IS THE ANSWER: sigma IS A LOOP IN COMPLEX 2M, NOT A PATH IN X **")
print("="*80)
print("""  P5 prop:monodromy, at source: sigma is the analytic continuation along
      2M = 2M* + eps.e^{i.phi},   phi : 0 -> 2pi
  -- a loop in the COMPLEX 2M-PLANE, encircling the branch point. Run it and watch the roots:""")
eps = 0.03
r_prev = None
start = None
print(f"\n  {'phi':>7} {'2M':>26} {'the two colliding roots':>34}")
for phi in np.linspace(0, 2*np.pi, 9):
    M2c = M2N + eps*np.exp(1j*phi)
    rr = np.roots([1.0, 0.0, -1.0, M2c])
    rr = sorted(rr, key=lambda z: abs(z + 2/S3))[1:]     # drop the far (backward) root
    rr = sorted(rr, key=lambda z: np.angle(z - r0N))
    if phi == 0: start = [complex(x) for x in rr]
    if phi in (np.linspace(0, 2*np.pi, 9)[0], np.linspace(0, 2*np.pi, 9)[4], np.linspace(0, 2*np.pi, 9)[-1]) or True:
        print(f"  {np.degrees(phi):>7.1f} {str(np.round(M2c,5)):>26} "
              f"{str([complex(round(z.real,4), round(z.imag,4)) for z in rr]):>34}")
# the honest monodromy test: continue by continuity, not by sorting
def continue_roots(M2N, eps, n=4000):
    phis = np.linspace(0, 2*np.pi, n)
    cur = np.roots([1.0, 0.0, -1.0, M2N + eps])
    track = list(cur)
    for phi in phis[1:]:
        nxt = np.roots([1.0, 0.0, -1.0, M2N + eps*np.exp(1j*phi)])
        new = []
        avail = list(nxt)
        for z in track:
            j = int(np.argmin([abs(z - y) for y in avail]))
            new.append(avail.pop(j))
        track = new
    return np.roots([1.0, 0.0, -1.0, M2N + eps]), track
start_r, end_r = continue_roots(M2N, eps)
print(f"\n  continuing by CONTINUITY once around (4000 steps):")
print(f"    started at : {[complex(round(z.real,5), round(z.imag,5)) for z in start_r]}")
print(f"    returned as: {[complex(round(z.real,5), round(z.imag,5)) for z in end_r]}")
perm = [int(np.argmin([abs(e - s) for s in start_r])) for e in end_r]
print(f"    the permutation induced: {perm}")
swapped = perm != [0, 1, 2]
print(f"    ** a transposition (two roots exchanged): {swapped} **")
print("""
  ** SO sigma IS EXACTLY WHAT P5 SAYS: a loop in complex 2M that comes back having swapped
  the two roots. IT IS NOT A PATH IN THE SUBSTRATE AT ALL. **

      >>> tau IS A LIGHT-PATH. sigma IS A MONODROMY. THEY ARE NOT THE SAME KIND OF OBJECT,
          AND THE QUESTION "IS sigma A LIGHT-PATH" IS NOT OPEN -- IT IS ILL-POSED. <<<

  tau moves along real null lines of the real substrate: it is a walk you could take.
  sigma moves 2M around a branch point in the complex plane: there is no substrate path
  underneath it, because 2M is not a direction in the substrate -- it is a LABEL ON THE
  FAMILY. A ruling connects two points of one manifold; sigma connects two DESCRIPTIONS of
  one geometry, and it does so through a complex parameter no observer walks along.""")

print("\n" + "="*80)
print("4. SO WHAT IS THE ASYMMETRY U1c FOUND?  -- named properly now")
print("="*80)
print(f"""  U1c: "the rulings give tau and not sigma", and called it an asymmetry between D_3's two
  generators. That was right and the reason is now exact, and it is not about the rulings:

    tau   is the SKY-ANGLE PERIODICITY -- a rotation of the dial. By tab23 (the_isometry.py)
          a dial turn IS a hinge transpose IS an azimuthal rotation, ** a genuine isometry of
          the substrate, inside SO(5,1) **. So tau has a substrate motion under it, and the
          rulings realise it.
    sigma is the ROOT-EXCHANGE -- the monodromy about the branch point. ** It is not a
          substrate isometry at all. ** P5 says so in another register: the Weyl S_3 "is the
          deck/monodromy symmetry of the solution space, NO isometry."

  ** THAT IS ALREADY THE CORPUS'S OWN KIND-DISTINCTION, AND THIS RECEIPT JUST WALKED INTO IT
  FROM THE FIGURE SIDE. ** P5's rem "The family symmetry is global, not gauged": the
  orientation Z_2 IS a substrate isometry, so chirality descends GAUGED; the Weyl S_3 is NO
  isometry, so a family symmetry it grades is GLOBAL.

      >>> THE RULINGS REALISE EXACTLY THE PART OF D_3 THAT IS A SUBSTRATE ISOMETRY, AND
          NOTHING ELSE. tau IS A MOTION; sigma IS A RELABELLING. THE LIGHT CONE CAN ONLY
          WALK THE MOTIONS. <<<

  and that is why the count in section 2 was a trap: two rulings and two colliding roots, at
  different values of 2M, in different spaces, one a motion and one a monodromy.""")

print("\n" + "="*80)
print("WHAT THIS RETURNED")
print("="*80)
print(f"""  ** THE QUESTION WAS ILL-POSED, AND THE SOURCE SAID SO. ** "Is sigma a light-path at
  Nariai" presupposes sigma is the kind of thing a path could be. P5 prop:monodromy, read at
  source: sigma is the analytic continuation of 2M once around the branch point -- ** a loop
  in the complex 2M-plane **. Verified here by continuing the roots through 4000 steps: they
  come back transposed. A ruling is a real null line in the real substrate. Different objects,
  different spaces. Not open -- ill-posed.

  ** AND THE ASYMMETRY U1c FOUND IS REAL, AND IT IS THE CORPUS'S OWN KIND-DISTINCTION,
  REACHED FROM THE FIGURE SIDE: **
      tau   -- the dial's rotation -- IS a substrate isometry (tab23: hinge transpose = dial
               turn = azimuthal rotation in SO(5,1)). So the rulings can walk it.
      sigma -- the root-exchange -- is NOT (P5: "the Weyl S_3 is the deck/monodromy symmetry
               of the solution space, NO isometry").
  >>> THE RULINGS REALISE EXACTLY THE PART OF D_3 THAT IS A SUBSTRATE ISOMETRY. tau IS A
      MOTION; sigma IS A RELABELLING. THE LIGHT CONE CAN ONLY WALK THE MOTIONS. <<<

  This is P5's own gauged/global argument (the orientation Z_2 IS an isometry -> chirality
  gauged; the Weyl S_3 is not -> flavour global) arriving from the null-ruling side. Not a new
  claim -- a second route to a standing one, which is the thing the interference engine is for.

  CONFIRMED EN ROUTE (Q2): sigma's fixed point, the dial's tangency, and the cubic's branch
  point are ONE locus -- r0 = alpha/sqrt3, w = 30, 2M = 2/(3 sqrt3), discriminant 0. Checked
  because the whole question was whether the two objects meet at all.

  ⚠ AND THE TRAP THAT WAS AVOIDED, logged because it is the live one: at Nariai there are TWO
  rulings and TWO colliding roots. ** The count matches and the match means nothing. ** The
  rulings are two AT the member where the roots are ONE; the roots are two only OFF it. Two
  2s, different values of 2M, different spaces. A count is not a map.""")
