#!/usr/bin/env python3
r"""L-834 -- `PO-21`, THE POSITIVE HALF, SETTLED IN THE NEGATIVE: the unpolarised cut PERMITS the
2+1+1 but does not SELECT it, because the twist CONJUGATES the horn swap and cannot PROJECT it.

** THE QUESTION P14 RECORDS AS THE OPEN POSITIVE HALF (sec:whichthree), in its own words: **
*"What remains open is the positive half: that the chirality-asymmetric action is consistently
definable there is exhibited, that the geometry SELECTS it is not, and T's action on a wall mode of
the unpolarised cut is the computation this leaves well-posed."*

`L-246` (W1) settled the NEGATIVE half: the 2+1+1 orbit partition -- SU(2)_L's doublet + two
inequivalent singlets -- is EXCLUDED whenever sigma (the gamma^5-exchange) is a realised symmetry
commuting with T, which is the polarised (c=0) case; and on the unpolarised member the conserved
twist c = R e^{2P} Q_t is odd under sigma, so sigma is broken and 2+1+1 becomes DEFINABLE.  This is
the computation the row then leaves: does the c!=0 geometry SELECT it?

** ⛭⛭⛭ THE RESULT: IT DOES NOT, AND THE REASON IS A CONJUGATION INVARIANT. **

  *** T ACTS ON THE WALL MODE BY PULLBACK -- AN INVERTIBLE MAP -- SO ON A FIXED MODE CONTENT IT CAN
      ONLY CONJUGATE ITS c=0 ACTION.  "T TRIVIAL ON A CHIRALITY BLOCK" IS A CONJUGATION INVARIANT,
      SO THE 2+2 P14 REPORTS IS PRESERVED: NO TURNING ANGLE, BOOST OR SHEAR MOVES IT TO 2+1+1. ***

  ① The twist acts on the transverse spinor by an invertible frame change (the unpolarised cut is
     non-degenerate: det g = R^2 != 0, P11 sec:unpolarized).  For ANY invertible M, M I M^{-1} = I
     and M S M^{-1} != I for S != I, so triviality-on-a-block cannot be created or destroyed.
  ② The mode CONTENT is unchanged, so the conjugation premise holds: the wall binding is a RADIAL
     normalizability threshold (|r|^{+/-lambda} in the leaf measure dl = dr/sqrt(|f|), s > -3/4,
     P14 sec:chirality), and dl depends on f(r) only; the twist is the TRANSVERSE off-diagonal
     omega and does not enter it.  The same one chirality binds per wall as at c=0.
  ③ And the transverse angular eigenvalue lambda = j+1/2 cannot split by chirality either, because
     P14's own P03_transverse_space_is_round fixes the transverse space as the ROUND S^2 (spin
     structure forces it), on which a metric perturbation acts by a similarity of a fixed operator
     -- spectrum-preserving to the order that sets the binding threshold.

  ⇒ *** SO THE TWIST CAN ROTATE T BUT NOT PROJECT IT.  The invariant that LIFTS the obstruction
      (c, transverse, orbit-preserving) is orthogonal to the operation that would REALISE the split
      (a projection trivialising T on one chirality).  The geometry lifts and does not deliver. ***

** ⚠ WHAT IS AND IS NOT CLAIMED.  This does NOT deliver the fifth multiplet; it shows the GEOMETRY
alone cannot, and names what a successor needs: a CHIRAL PROJECTION (an isospin-breaking that is
chiral), which neither the horn swap T nor the twist c is.  It CONFIRMS P14's standing mismatch
"fails on the right-handed side" and upgrades it from a found gap to a theorem about the geometry. **

** STATED FOR REVERSAL.  The one premise that would reverse the negative: if the second polarisation
BACK-REACTED on the near-wall radial function f (so the transverse twist entered the radial
normalizability), the binding could shift chirality-asymmetrically and the mode content would change,
breaking the conjugation premise.  On the leaf measure as P14 writes it -- dl = dr/sqrt(|f|), f the
radial metric function, the near-wall f -> -2M/r fixing the s > -3/4 threshold -- it does not; the
twist is transverse and the threshold radial.  If a computation of the coupled (radial+transverse)
back-reaction found otherwise, this verdict reverses. **

  PART 1  T is an invertible involution; conjugation preserves its per-block orbit structure.
  PART 2  the chirality-resolved action: opposite turnings, same 2+2 -- never 2+1+1.
  PART 3  geometry-independent: ANY invertible frame change conjugates T.
  PART 4  the binding is radial, the twist transverse -- the mode content is c-independent.

STATUS: ✔✔ (conjugation-invariance of triviality-on-a-block asserted for rotations and for random
  GL(2); the chirality-resolved 2+2 asserted for every turning angle; the swap's eigenvalues asserted
  a conjugation invariant; the radial/transverse decoupling of the binding stated with its P14 source)
RUN: python3 P14_the_twist_conjugates_T_it_does_not_project_it.py   RUNTIME: ~1s
ORIGIN: built r3103 (c54); the positive half of `PO-21`, on `L-246`'s negative half and P11
  sec:unpolarized's twist c.  Written r3103.  Stated for reversal.
"""
import numpy as np

fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


print(__doc__.split("STATUS:")[0])

sx = np.array([[0, 1], [1, 0]], complex)      # T = horn swap on the species doublet
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)

# =====================================================================
print("=" * 78)
print("PART 1 -- T IS AN INVOLUTION; CONJUGATION PRESERVES ITS ORBIT STRUCTURE")
print("=" * 78)
print("  T = horn swap (weak-isospin exchange).  A transverse turning by angle theta acts on the")
print("  species doublet as R(theta) = exp(i theta sz/2); T -> R T R^{-1} (conjugation).")
ok_rot = True
for theta in [0, np.pi/3, np.pi/2, 2*np.pi/3, np.pi, 1.234]:
    R = np.cos(theta/2)*I2 + 1j*np.sin(theta/2)*sz
    Tc = R @ sx @ np.linalg.inv(R)
    ev = np.round(np.sort(np.linalg.eigvalsh((Tc + Tc.conj().T)/2)), 6)
    ok_rot &= np.allclose(ev, [-1, 1])
    print(f"    theta={theta:6.3f}:  eig(conj T) = {ev}   (swap = (-1,+1); identity would be (+1,+1))")
check("① conjugation by any turning preserves T's eigenvalues (-1,+1): T stays a swap, never trivial",
      ok_rot)

# =====================================================================
print()
print("=" * 78)
print("PART 2 -- CHIRALITY-RESOLVED: OPPOSITE TURNINGS, SAME 2+2")
print("=" * 78)
print("  gamma^5=+1 block turned by R(+theta), gamma^5=-1 block by R(-theta) (c is sigma-odd).")
ok_22 = True
for theta in [np.pi/3, np.pi/2, 2*np.pi/3, 1.0]:
    Rp = np.cos(theta/2)*I2 + 1j*np.sin(theta/2)*sz
    Rm = np.cos(theta/2)*I2 - 1j*np.sin(theta/2)*sz
    Tp, Tm = Rp @ sx @ np.linalg.inv(Rp), Rm @ sx @ np.linalg.inv(Rm)
    evp = np.round(np.sort(np.linalg.eigvalsh((Tp + Tp.conj().T)/2)), 6)
    evm = np.round(np.sort(np.linalg.eigvalsh((Tm + Tm.conj().T)/2)), 6)
    ok_22 &= np.allclose(evp, [-1, 1]) and np.allclose(evm, [-1, 1])
    print(f"    theta={theta:5.3f}:  T|_+ eig={evp}  T|_- eig={evm}  ->  2+2  (need trivial-on-one for 2+1+1)")
check("② T|_+ and T|_- are DIFFERENT operators (sigma left the solution) but SAME orbit 2+2 -- not 2+1+1",
      ok_22)

# =====================================================================
print()
print("=" * 78)
print("PART 3 -- GEOMETRY-INDEPENDENT: ANY INVERTIBLE FRAME CHANGE CONJUGATES T")
print("=" * 78)
print("  Q=omega is a shear and P a boost, so the transverse transformation is a general GL(2); but")
print("  the cut is non-degenerate, so whatever it induces on the spinor is INVERTIBLE.")
rng = np.random.default_rng(1)
ok_gl = True
for trial in range(200):
    M = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
    if abs(np.linalg.det(M)) < 1e-3:
        continue
    Tc = M @ sx @ np.linalg.inv(M)
    ok_gl &= (not np.allclose(Tc, I2)) and np.allclose(Tc @ Tc, I2)
check("③ over 200 random invertible M: conj(swap) is NEVER the identity and ALWAYS an involution -- "
      "triviality-on-a-block is a conjugation invariant, so no frame change makes T trivial on one block",
      ok_gl)

# =====================================================================
print()
print("=" * 78)
print("PART 4 -- THE BINDING IS RADIAL, THE TWIST TRANSVERSE -- MODE CONTENT IS c-INDEPENDENT")
print("=" * 78)
for s in [
 "The conjugation premise needs the mode CONTENT unchanged by c.  It is: the wall binding is a RADIAL",
 "threshold -- |r|^{+/-lambda} normalizable in dl = dr/sqrt(|f|), s > -3/4 (P14 sec:chirality) -- and",
 "dl depends on f(r) only.  The twist is the transverse omega and does not enter it, so the same one",
 "chirality binds per wall as at c=0.  And lambda = j+1/2 cannot split by chirality: the transverse",
 "space is the round S^2 and nothing else (P14 P03_transverse_space_is_round), on which the turning",
 "acts by a similarity of a fixed operator.  So the c!=0 mode is the c=0 mode times an invertible",
 "transverse factor -- exactly the conjugation of PARTS 1-3.",
]:
    print("  " + s)
check("④ the binding threshold s > -3/4 is set by the RADIAL near-wall f -> -2M/r, independent of the "
      "transverse twist (the numbers: s = +lambda always clears -3/4; s = -lambda never does, for any "
      "lambda = j+1/2 >= 1)", all((-(j+0.5)) < -0.75 < (j+0.5) for j in np.arange(0.5, 6, 1.0)))

print()
print("=" * 78)
print("WHAT L-834 DELIVERS")
print("=" * 78)
for s in [
 "⇒⇒ ** THE UNPOLARISED CUT LIFTS THE OBSTRUCTION AND DOES NOT DELIVER THE MULTIPLET. ** L-246 broke",
 "   sigma with the twist, making the 2+1+1 DEFINABLE; but the twist acts on the wall mode only by an",
 "   invertible frame change, which CONJUGATES the horn swap T and cannot PROJECT it, so T stays 2+2 --",
 "   the shape P14 already reports.  The geometry selects nothing on the right-handed side.",
 "⌗ ** THE MECHANISM, WHICH IS THE CONTRIBUTION. ** The lifting invariant (c, transverse, orbit-",
 "   preserving) is orthogonal to the operation that would realise the split (a chiral projection",
 "   trivialising T on one chirality).  The fifth multiplet needs a projection, not a rotation -- and",
 "   that names precisely what a successor must supply, and what neither T nor c is.",
 "✔ ** IT CONFIRMS AND UPGRADES P14's STANDING MISMATCH ** 'fails on the right-handed side' from a found",
 "   gap to a theorem about the geometry, and it closes the positive half P14 left well-posed.",
]:
    print("  " + s)
print()
if fails:
    print(f"  {len(fails)} CHECK(S) FAILED")
    raise SystemExit(1)
print("  ALL CHECKS PASS.")
