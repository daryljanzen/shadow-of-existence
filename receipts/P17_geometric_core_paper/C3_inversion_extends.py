"""C3 — does INVERSION in the throat extend off the equatorial plane, as polarity did (Q1/Q6)?
Minkowski inversion in the quadric eta(X,X)=alpha^2:   P* = alpha^2 P / eta(P,P).
ORIGIN: storyboard_receipts/C3_inversion_extends.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
a=1.0; eta=np.diag([-1.,1.,1.,1.,1.,1.])
ip=lambda P,Q: P@eta@Q
rng=np.random.default_rng(13)
inv = lambda P: a**2*P/ip(P,P)

print("="*78); print("C3 — INVERSION IN THE THROAT, OFF THE EQUATORIAL PLANE"); print("="*78)
print("\nSTEP 1 — the classical relation: the INVERSE of P lies on the POLAR of P.")
print("  polar(P) = {X : eta(P,X) = alpha^2}.   Check eta(P, P*) = alpha^2 identically:")
print(f"  {'point':34s} {'eta(P,P)':>10s} {'eta(P,P*)':>12s} {'= a^2?':>8s}")
for k in range(6):
    P=rng.normal(size=6)
    if abs(ip(P,P))<1e-6: continue
    Ps=inv(P)
    lab = "equatorial" if abs(P[0])<1e-9 else ("spacelike, off-plane" if ip(P,P)>0 else "TIMELIKE, off-plane")
    print(f"  {lab:34s} {ip(P,P):10.5f} {ip(P,Ps):12.8f} {abs(ip(P,Ps)-a**2)<1e-12!s:>8s}")
print("\n  => eta(P,P*) = alpha^2 . eta(P,P)/eta(P,P) = alpha^2, ALGEBRAICALLY, for every signature")
print("     of eta(P,P).  So the relation 'the inverse lies on the polar' is INDEPENDENT of the")
print("     equatorial restriction and independent of whether P is spacelike or timelike.")

print("\nSTEP 2 — is inversion an INVOLUTION here, as in the Euclidean case?")
for k in range(4):
    P=rng.normal(size=6)
    if abs(ip(P,P))<1e-6: continue
    print(f"   P** == P ?  {np.allclose(inv(inv(P)), P, atol=1e-12)}   (eta(P,P)={ip(P,P):+.4f})")

print("\nSTEP 3 — and the FIXED SET is the substrate itself, not just the throat:")
for k in range(4):
    v=rng.normal(size=6)
    if ip(v,v)<=0: v[1:]*=4
    P=v*a/np.sqrt(ip(v,v))                      # on the substrate
    print(f"   P on the substrate: inv(P) == P ?  {np.allclose(inv(P),P,atol=1e-12)}")
print("\n" + "="*78)
print("RESULT C3: inversion extends, and it extends TRIVIALLY -- 'the inverse lies on the polar'")
print("  is an algebraic identity in eta, holding off the equatorial plane and at any signature.")
print("  It is an involution, and its fixed set is the WHOLE SUBSTRATE eta(X,X)=alpha^2, of which")
print("  the throat is the equatorial section.  So p0's third route carries exactly what the")
print("  first carries, and Q1's bound -- rho58 extends to the projective setting -- bounds it too.")
print("  THREE CLASSICAL ROUTES, ONE OBJECT, ONE BOUND.")
print("="*78)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Everything above printed booleans in a table, so the run could
# not fail.  Pinned here: eta(P,P*) = alpha^2 at BOTH signatures (and the sample is REQUIRED to
# contain both, or "at any signature" is untested), the involution, and the fixed set = the
# whole substrate WITH a control point off it that must move.  The file runs entirely at
# alpha = 1, where alpha^2 and alpha cannot be told apart; the last loop re-runs the relation at
# alpha = 2.5, where the polar constant must be 6.25 and not 2.5.
rng_a = np.random.default_rng(1961)
signatures = set()
for _ in range(200):
    P = rng_a.normal(size=6)
    if abs(ip(P, P)) < 1e-6:
        continue
    signatures.add(ip(P, P) > 0)
    assert abs(ip(P, inv(P)) - 1.0) < 1e-12          # eta(P,P*) = alpha^2 = 1   (STEP 1)
    assert np.allclose(inv(inv(P)), P, atol=1e-12)   # involution                (STEP 2)
assert signatures == {True, False}                   # spacelike AND timelike P both sampled
for _ in range(60):                                  # STEP 3: the fixed set, and a control
    v = rng_a.normal(size=6)
    if ip(v, v) <= 0:
        v[1:] *= 4
    if ip(v, v) <= 1e-6:
        continue
    P_on = v / np.sqrt(ip(v, v))                     # eta(P,P) = alpha^2 = 1: ON the substrate
    assert abs(ip(P_on, P_on) - 1.0) < 1e-12
    assert np.allclose(inv(P_on), P_on, atol=1e-12)
    P_off = 2.0 * P_on                               # eta = 4 alpha^2: OFF it, so NOT fixed
    assert np.linalg.norm(inv(P_off) - P_off) > 1.0
a_second = 2.5                                       # a SECOND scale: alpha^2 = 6.25
inv_second = lambda P: a_second**2 * P / ip(P, P)
for _ in range(60):
    P = rng_a.normal(size=6)
    if abs(ip(P, P)) < 1e-6:
        continue
    assert abs(ip(P, inv_second(P)) - 6.25) < 1e-12
    assert np.allclose(inv_second(inv_second(P)), P, atol=1e-12)
print("  [r2376+c54.161] eta(P,P*) = alpha^2 asserted at both signatures over 200 points, with")
print("  the involution, the fixed set (and an off-substrate control), and the same at alpha=2.5.")
