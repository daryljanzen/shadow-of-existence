"""
Working the M-cancellation (finding C-K, r1065) against the TWO readings the thread
gave it, neither of which I can take on trust.

  READING 1 (r1065): "the singularity is neither in the substrate nor in the mass --
      it's what the SO(3) sweep makes of a smooth passage read through an areal radius
      shrinking at infinite rate ... the sharpest possible vindication of 'M is a stupid
      number': even the singularity doesn't know about it."

  READING 2 (r1087, the last message of the thread): "K being M-free along the bead
      doesn't mean mass is absent -- it means every root returns the same 2M, that the
      degeneracy is forced, that there is no asymmetric handle in the mass parameter.
      That's the corpus's generation result. I found its signature and read it as its
      refutation."

Reading 2 arrives immediately after Daryl catches Reading 1 contradicting prop:bend.
That is exactly the shape of an over-correction, so it does not get a pass either.
Question owed: are these the same statement?  Could this check return "no"?
"""
import numpy as np

alpha = 1.0

def r_of_tau(tt, M2):
    """r^3 = 2M a^2 sinh^2(3 tt / 2a); take the real branch"""
    r3 = M2 * alpha**2 * np.sinh(1.5*tt/alpha)**2
    return np.sign(r3) * abs(r3)**(1/3)

def K(r, M2):
    return 48*(M2/2)**2 / r**6 + 24/alpha**4

print("="*76)
print("(A)  What the cancellation IS -- and it is one line of dimensional analysis")
print("="*76)
print("  K   = 48 M^2 / r^6 + 24/a^4")
print("  bead: r^3 = 2M a^2 sinh^2(w)   =>   r^6 = 4 M^2 a^4 sinh^4(w)")
print("  so  48 M^2 / r^6 = 48 M^2 / (4 M^2 a^4 sinh^4) = 12 / (a^4 sinh^4)")
print("  =>  K = (12/a^4)(sinh^-4(w) + 2)      <- M gone")
print()
print("  The mechanism is the EXPONENT, not a conspiracy:")
print("     r ~ M^(1/3)  and  K's mass term ~ M^2 / r^6 ~ M^2 / M^(6/3) = M^2/M^2 = M^0.")
print("     6 x (1/3) = 2 exactly. The 1/3 in the amplitude is what eats the M^2.")
print("  => M is a PURE AMPLITUDE on the bead: it scales r and NOTHING that is built")
print("     from r at that power. Not 'mass is absent'; not 'the degeneracy of roots'.")

print()
print("="*76)
print("(B)  Reading 2 checked: is the M-cancellation the 'every root returns the same 2M'")
print("     result?   (across-M-at-fixed-w   vs   across-roots-at-fixed-M)")
print("="*76)
print("  the corpus's statement: for ONE cubic r^3 - r + 2M = 0, each of its THREE roots")
print("  r0 returns the SAME 2M via 2M = r0 - r0^3. Check it:")
for M2 in (0.10, 0.2887, 0.3849):
    roots = np.roots([1, 0, -1, M2])
    back = [rr - rr**3 for rr in roots]
    print(f"     2M={M2:.4f}  roots={[f'{x.real:+.4f}' for x in roots]}  "
          f"-> r0-r0^3 = {[f'{b.real:+.4f}' for b in back]}")
print("  ...same 2M from every root. TRUE, and it is a statement at FIXED M about")
print("  the three roots of ONE cubic.")
print()
print("  the K-cancellation: K(w) is the same across DIFFERENT M. Check it:")
for w in (0.3, 1.0):
    row = []
    for M2 in (0.002, 0.3849, 10.0):
        r = r_of_tau(w*2*alpha/3, M2)
        row.append((M2, r, K(r, M2)))
    print(f"     w={w}: " + "  ".join(f"[2M={m:.3f} r={r:.4f} K={k:.6f}]" for m, r, k in row))
print("  ...same K across FOUR ORDERS of M. TRUE, and it is a statement across the")
print("  FAMILY in M about one point of the bead.")
print()
print("  --- VERDICT on Reading 2 ---")
print("  These are DIFFERENT statements. One quantifies over the three roots at fixed M;")
print("  the other over M at fixed w. Neither implies the other, and the K-cancellation")
print("  says nothing about root degeneracy or about generations.")
print("  Reading 2 is an OVER-CORRECTION -- the flip-flop running the other way, one turn")
print("  after being caught. It should not be baked. The catch that provoked it (that the")
print("  Q^2/r^2 term IS the EM stress-energy, prop:bend's own worked example) is CORRECT")
print("  and stands; the generation identification tacked onto it does not follow.")

print()
print("="*76)
print("(C)  Reading 1 checked: does 'even the singularity doesn't know about M' hold?")
print("="*76)
print("  Scope, as the thread's own honest note had it: M != 0 gates whether there is a")
print("  singularity AT ALL (at M=0 there is no bead and K = 24/a^4 everywhere, regular).")
for M2 in (0.0, 1e-6, 0.3849):
    w = 0.3
    if M2 == 0:
        print(f"     2M=0        : r == 0 identically; K = 24/a^4 = {24/alpha**4:.4f}  REGULAR, no bead")
    else:
        r = r_of_tau(w*2*alpha/3, M2)
        print(f"     2M={M2:<9.6f}: r={r:.6e}  K={K(r,M2):.6f}   (same K as every other M!=0)")
print()
print("  --- VERDICT on Reading 1 ---")
print("  The M-independence is REAL and holds for every M != 0. But 'M is a stupid number'")
print("  overshoots in the other direction: M is what makes the bead exist. The precise")
print("  statement both readings were reaching past:")
print("     ** M sets the SCALE of the bead and NOT ITS SHAPE. Along cosmic time the")
print("        curvature profile K(tau~) is UNIVERSAL -- every progenitor, whatever its")
print("        mass, meets the identical curvature at the identical cosmic time. **")

print()
print("="*76)
print("(D)  The 2/3 exponent does THREE jobs, and they are one job")
print("="*76)
print("  near r=0:  r ~ A (3 s'/2)^(2/3)")
eps = 1e-4
for s in (1e-3, 1e-4, 1e-5):
    A = (0.3849*alpha**2)**(1/3)
    r = A*(1.5*s)**(2/3)
    drds = (r - A*(1.5*(s-eps*s))**(2/3))/(eps*s)
    print(f"     s'={s:.0e}   r={r:.3e}   dr/ds~{drds:.3e}   K~{48*(0.3849/2)**2/r**6:.3e}")
print()
print("  (i)   dr/ds ~ s'^(-1/3)  -> the VERTICAL TANGENT of F_flat at r=0")
print("  (ii)  K     ~ s'^(-4)    -> the SINGULARITY's strength")
print("  (iii) 6 x (1/3) = 2      -> the M-CANCELLATION")
print("  All three are the SAME exponent read three ways. The 2/3 in the sinh^(2/3) law")
print("  is doing the vertical tangent, the singularity, and the M-independence at once.")
print("  That is the honest unification the thread has three separate notes for.")
