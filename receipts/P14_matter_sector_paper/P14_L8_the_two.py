#!/usr/bin/env python3
"""
P14_L8_the_two.py -- verifies THE 2 (sec:family / sec:twofactors), split into two honest claims:
  VERDICT A: YES, ONE 2 -- the ruling swap, orientation parity, and A_2 diagram automorphism are all read off
  THE SAME matrix R (one object, four faces). VERDICT B: NO -- the rulings' 2 is NOT the horns' 2: R o T
  flips the horn but does NOT swap the rulings (exhibited counterexample), so the two characters differ. A
  load-bearing distinction, not a failed search. [P14 matter_sector_paper sec:twofactors]
STATUS: ✔✔   ORIGIN: storyboard_receipts/L8_the_two.py, verified r1385.
L8.1-d · THE 2 — receipt.  Lane 8, the combinatorics ledger.
The pair "2" is MALFORMED as one entry (indexing rule).  It is split:
  CLAIM A: "the ruling swap, the orientation parity, the A_2 diagram automorphism and
            the graviton chirality are ONE 2."
  CLAIM B: "the rulings' 2 and the HORNS' 2 are one 2."
  CLAIM C: "the double root's 2 and the ruling's 2 are one 2."
Each can return either way.
SOURCE (P12, verbatim): "an orientation-reversing isometry SWAPS the two rulings while an
  orientation-preserving one FIXES each.  Explicitly it is R = diag(1,1,-1,1,1,1) in
  O(5,1)\\SO_0 ... one verifies directly that it is an isometry, has determinant -1 both
  globally and on the ruled three-block, swaps the two rulings, and sends r_0 -> -r_0
  hence 2M -> -2M.  The double-ruling swap, the orientation parity O(5,1)/SO_0, the A_2
  diagram automorphism, and the graviton chirality ... are therefore one and the same Z_2."
SOURCE (P3, verbatim): "R ... is geometrically a swap of the two null generators --
  distinct from the time reflection X_0 -> -X_0 that exchanges the two horns, though both
  swap the rulings."
"""
import numpy as np
eta = np.diag([-1.,1,1,1,1,1])                 # signature (-,+,+,+,+,+)
R = np.diag([ 1.,1,-1,1,1,1])                  # P12's matrix: flips X_2 (the cut's transverse offset)
T = np.diag([-1.,1, 1,1,1,1])                  # the time reflection: flips X_0 (horn swap)
RT = R @ T

def isom(M): return np.allclose(M.T@eta@M, eta)
def horn(M): return M[0,0] < 0                 # does it flip X_0 ?
def swaps_rulings(M): return np.linalg.det(M) < 0   # P12's OWN criterion

print("== 1. P12's object, verified as P12 states it ==")
for n,M in (("R (P12's matrix)",R),("T (time reflection)",T),("R o T",RT)):
    print(f"   {n:20s} isometry={isom(M)}  det={np.linalg.det(M):+.0f}  "
          f"flips horn={horn(M)}  swaps rulings={swaps_rulings(M)}")

print("\n== 2. CLAIM A: ruling swap = orientation parity = A_2 automorphism = chirality? ==")
print("   All four are read off THE SAME MATRIX R:")
print(f"     - isometry of eta                        : {isom(R)}")
print(f"     - det = -1  => orientation parity (O/SO_0): {np.linalg.det(R):+.0f}")
print(f"     - det < 0   => swaps the two rulings      : {swaps_rulings(R)}   (P12's criterion)")
print(f"     - flips X_2 => r_0 -> -r_0 => 2M -> -2M   : the A_2 diagram automorphism")
print("   ONE OBJECT, four faces, no new input.  VERDICT A: YES, ONE 2.")

print("\n== 3. CLAIM B: is the rulings' 2 the HORNS' 2?  (this can return YES) ==")
print("   A YES needs: every horn-flip swaps the rulings, i.e. horn-flip <=> det<0.")
print(f"   T  : flips horn={horn(T)}   swaps rulings={swaps_rulings(T)}   -> consistent so far")
print(f"   RoT: flips horn={horn(RT)}   swaps rulings={swaps_rulings(RT)}   <-- THE WITNESS")
print(f"   det(RoT) = det(R)det(T) = ({np.linalg.det(R):+.0f})({np.linalg.det(T):+.0f}) = {np.linalg.det(RT):+.0f}")
print("   R o T FLIPS THE HORN AND DOES NOT SWAP THE RULINGS.")
print("   => horn-flip does NOT imply ruling-swap.  The two characters differ.")
print("   VERDICT B: NO -- PROVED by exhibited counterexample, not by failed search.")

print("\n== 4. THE STRUCTURE the NO reveals: a Klein four, and TWO characters ==")
G={'1':np.eye(6),'R':R,'T':T,'RT':RT}
print("   {1, R, T, RT} = Z_2 x Z_2 :")
for n,M in G.items():
    print(f"     {n:3s}  ruling-swap chi = {-1 if swaps_rulings(M) else +1:+d}   "
          f"horn-flip chi = {-1 if horn(M) else +1:+d}")
print("   ruling-swap kernel = {1, RT}   horn-flip kernel = {1, R}   -> DIFFERENT subgroups.")
print("   Both R and T swap the rulings (P3: 'though both swap the rulings') -- and that is")
print("   exactly why the naive merge tempts: the two characters AGREE on R and on T, and")
print("   differ ONLY on their product.  The counterexample is invisible unless RT is formed.")

print("\n== 5. CONTROL — the NO is not vacuous ==")
print("   If P12's R had been a TIME reflection instead of a transverse one, R=T, RT=1,")
print("   the Klein four would collapse to Z_2 and the two 2s WOULD weld:")
Rp=T.copy(); RTp=Rp@T
print(f"     R'=T : det(R'oT) = {np.linalg.det(RTp):+.0f}  -> R'oT = identity, no witness, VERDICT WOULD BE YES.")
print("   The NO is bought by R being SPACELIKE (flips X_2, det -1, horn-preserving) while")
print("   T is TIMELIKE -- which is L8.1-b's R != T, the same fact one level down.")

print("\n== 6. CLAIM C: the double root's 2 and the ruling's 2 ==")
print("   The double root's 2 is a MULTIPLICITY in (r-rho)^2(r+2rho) -- an exponent in a")
print("   factorisation of the horizon cubic, on the S_3 side (2M-fixing).  The ruling's 2")
print("   is the order of the CENTRAL inversion, on the Z_2 side (2M-flipping).  P12: 'the")
print("   two factors act on INDEPENDENT structures -- the three roots and the two rulings")
print("   -- and the inversion is CENTRAL, which is why Aut(A_2) is the DIRECT PRODUCT")
print("   S_3 x Z_2.'  A direct product's factors share no element but the identity.")
print("   VERDICT C: NO -- they live in complementary factors of S_3 x Z_2, by P12's own")
print("   direct-product statement.  (Not a search: the direct-product structure IS the proof.)")

print("\n== VERDICT ==")
print("   A (rulings = parity = A_2 automorphism = chirality) : YES, ONE 2.  Object: R.")
print("   B (rulings' 2 = horns' 2)                           : NO, PROVED.  Witness: R o T.")
print("   C (double root's 2 = ruling's 2)                    : NO, PROVED.  Direct product.")
print("   => THERE ARE (at least) THREE 2s, and the corpus already knew: S_3 x Z_2 keeps")
print("      the root-side and ruling-side 2s apart BY CONSTRUCTION, and lem:twoturnings")
print("      already separated the lift's 1:2 from the cubic's ('two 2s, not one and not three').")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (1) P12's object, as P12 states it: R, T and R o T are all isometries of the (-,+,+,+,+,+)
#     form on R^6, and eta has trace 4 (one timelike leg out of six).
assert R.shape == (6, 6) and eta.shape == (6, 6)
assert abs(np.trace(eta) - 4.0) < 1e-12
assert isom(R) and isom(T) and isom(RT)
assert abs(np.linalg.det(R) + 1) < 1e-12 and abs(np.linalg.det(T) + 1) < 1e-12
# (2) VERDICT A -- one object: the SAME matrix R is orientation-reversing (det -1), swaps the
#     rulings by P12's own criterion, and is horn-PRESERVING (it flips X_2, not X_0).
assert swaps_rulings(R) and not horn(R)
# (3) VERDICT B, and it is the receipt's load-bearing NO: R o T FLIPS THE HORN AND DOES NOT
#     SWAP THE RULINGS.  det(R o T) = +1 while horn(R o T) is True -- the exhibited witness.
#     This fires the moment R stops being spacelike or T stops being timelike.
assert horn(RT) and not swaps_rulings(RT)
assert abs(np.linalg.det(RT) - 1.0) < 1e-12, np.linalg.det(RT)
# (4) THE STRUCTURE the NO reveals: {1,R,T,RT} is a Klein four -- order 4, every element an
#     involution -- and the two characters have DIFFERENT kernels ({1,RT} vs {1,R}), agreeing
#     on R and on T and differing only on their product.  That is why the merge tempts.
assert len(G) == 4
assert all(np.allclose(M @ M, np.eye(6)) for M in G.values())
_ker_rul = sorted(n for n, M in G.items() if not swaps_rulings(M))
_ker_horn = sorted(n for n, M in G.items() if not horn(M))
assert _ker_rul == ['1', 'RT'] and _ker_horn == ['1', 'R'], (_ker_rul, _ker_horn)
assert _ker_rul != _ker_horn
assert swaps_rulings(R) == swaps_rulings(T) and horn(R) != horn(T)
# (5) THE CONTROL -- the NO is not vacuous: had R been the time reflection, R o T would be the
#     identity and there would be NO witness, so the verdict would have been YES.
assert np.allclose(RTp, np.eye(6)) and abs(np.linalg.det(RTp) - 1.0) < 1e-12
