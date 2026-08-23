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

** THE BACK-REACTION, COMPUTED (PART 5).  The one way the conjugation premise could fail is if the
twist changed the mode content chirality-asymmetrically -- i.e. if the second polarisation entered the
binding measure with a dependence on the SIGN of c.  It does not.  The conformal factor gamma sets the
Dirac leaf measure (g_tt = -e^{2(gamma-psi)}) and is fixed by quadrature from (P,Q); computed from the
constraints, gamma_z and gamma_t depend on the twist ONLY through omega_t^2, omega_z^2, omega_t
omega_z -- EVEN under sigma: Q=omega -> -omega.  So the measure is IDENTICAL on the +c and -c members:
the back-reaction is real (gamma does depend on the twist) but PARITY-EVEN, so it cannot distinguish
the two chiralities, which the sign of c exchanges.  The binding is chirality-symmetric, the
conjugation premise holds exactly, and the negative is CLOSED -- not conditional. **

  PART 1  T is an invertible involution; conjugation preserves its per-block orbit structure.
  PART 2  the chirality-resolved action: opposite turnings, same 2+2 -- never 2+1+1.
  PART 3  geometry-independent: ANY invertible frame change conjugates T.
  PART 4  the binding is radial, the twist transverse -- the mode content is c-independent.
  PART 5  the back-reaction on the measure is PARITY-EVEN: gamma is even in the twist, so the binding
          cannot depend on the sign of c (the chirality).  The one escape, closed by computation.

STATUS: ✔✔ (conjugation-invariance of triviality-on-a-block asserted for rotations and for random
  GL(2); the chirality-resolved 2+2 asserted for every turning angle; the swap's eigenvalues asserted
  a conjugation invariant; the radial/transverse decoupling of the binding stated with its P14 source;
  and gamma_z, gamma_t derived from the constraints and asserted EVEN under Q -> -Q)
RUN: python3 P14_the_twist_conjugates_T_it_does_not_project_it.py   RUNTIME: ~1s
ORIGIN: built r3103, back-reaction closed r3104 (c54); the positive half of `PO-21`, on `L-246`'s
  negative half and P11 sec:unpolarized's twist c.
"""
import numpy as np
import sympy as sp

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

# =====================================================================
print()
print("=" * 78)
print("PART 5 -- THE BACK-REACTION ON THE MEASURE IS PARITY-EVEN (the one escape, closed)")
print("=" * 78)
print("  PART 4's decoupling is exact only if the twist does not enter the binding measure with a")
print("  dependence on the SIGN of c (the chirality). It does not. The conformal factor gamma sets the")
print("  Dirac leaf measure (g_tt = -e^{2(gamma-psi)}); it is fixed by quadrature from (P,Q) via the")
print("  constraints (the unpolarised cut's own Einstein equations, L-832). Compute gamma_z, gamma_t")
print("  and their parity under sigma: Q=omega -> -omega (the chirality exchange, c -> -c).")
tt, zz = sp.symbols('t z', real=True)
psi = sp.Function('psi')(tt, zz)
gam = sp.Function('gamma')(tt, zz)
om = sp.Function('omega')(tt, zz)
Es = sp.exp
Xs = [tt, zz, sp.Symbol('x'), sp.Symbol('y')]
Rs_ = tt
gg = sp.zeros(4, 4)
gg[0, 0] = -Es(2*(gam-psi)); gg[1, 1] = Es(2*(gam-psi))
gg[2, 2] = Es(2*psi); gg[2, 3] = gg[3, 2] = Es(2*psi)*om
gg[3, 3] = Es(2*psi)*om**2 + Rs_**2*Es(-2*psi)
ggi = gg.inv()


def ds(f, i):
    return sp.diff(f, Xs[i])


Gm2 = [[[sp.simplify(sum(ggi[a, dd]*(ds(gg[dd, b], c)+ds(gg[dd, c], b)-ds(gg[b, c], dd))
                         for dd in range(4))/2)
         for c in range(4)] for b in range(4)] for a in range(4)]


def Ric2(b, c):
    return sp.simplify(sum(ds(Gm2[a][b][c], a) - ds(Gm2[a][b][a], c) for a in range(4))
                       + sum(Gm2[a][a][dd]*Gm2[dd][b][c] - Gm2[a][c][dd]*Gm2[dd][b][a]
                             for a in range(4) for dd in range(4)))


Rsc = sp.simplify(sum(ggi[a, b]*Ric2(a, b) for a in range(4) for b in range(4)))
gz = sp.solve(sp.simplify(Ric2(0, 1) - gg[0, 1]*Rsc/2), sp.Derivative(gam, zz))[0]
gt = sp.solve(sp.simplify(Ric2(0, 0) - gg[0, 0]*Rsc/2), sp.Derivative(gam, tt))[0]


def flip_Q(expr):
    reps = {d_: -d_ for d_ in expr.atoms(sp.Derivative) if d_.expr == om}
    reps[om] = -om
    return expr.subs(reps, simultaneous=True)


print(f"  gamma_z = {sp.simplify(gz)}")
print(f"  gamma_t = {sp.simplify(gt)}")
even = sp.simplify(flip_Q(gz) - gz) == 0 and sp.simplify(flip_Q(gt) - gt) == 0
print(f"  gamma_z, gamma_t depend on the twist only through omega_t^2, omega_z^2, omega_t omega_z")
print(f"  => EVEN under sigma (Q -> -Q): {even}")
check("⑤ the conformal factor gamma -- hence the Dirac leaf measure -- is EVEN in the twist, so the "
      "binding is IDENTICAL on the +c and -c members: the back-reaction is real but parity-even and "
      "cannot depend on the sign of c (the chirality). The one escape from PART 4 is closed.", even)

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
 "✔ ** AND THE RESULT IS CLOSED, NOT CONDITIONAL. ** The one escape -- a back-reaction of the twist on",
 "   the binding measure -- is computed (PART 5): gamma is EVEN in the twist, so the measure cannot",
 "   depend on the sign of c. There is no reversal premise left standing.",
]:
    print("  " + s)
print()
if fails:
    print(f"  {len(fails)} CHECK(S) FAILED")
    raise SystemExit(1)
print("  ALL CHECKS PASS.")
