import io, re
import numpy as np, mpmath as mp
CLIGHT=299792.458; H0,OM=68.6,0.2973
OMR=4.15e-5/(H0/100.0)**2; OL=1.0-OM; hub=H0/CLIGHT
X0=(2*OL/OM)**(1/3); ALPHA=1.0/(hub*np.sqrt(OL)); R0=ALPHA*X0/np.sqrt(3.0)
TWOM=2*R0**3/(ALPHA**2*X0**3); KRAD=hub**2*OMR*R0**4
RT=(TWOM*ALPHA**2)**(1/3)
mp.mp.dps=60
A_,M_,K_=mp.mpf(ALPHA),mp.mpf(TWOM),mp.mpf(KRAD); S0=K_/M_
def rad(s,K=None):
    k = K_ if K is None else mp.mpf(K)
    return -M_/s + k/s**2 + s**2/A_**2
def drad(s,K=None):
    k = K_ if K is None else mp.mpf(K)
    return M_/s**2 - 2*k/s**3 + 2*s/A_**2
print(f"alpha={ALPHA:.3f} r0={R0:.3f} 2M={TWOM:.4f} K={KRAD:.3f} r_t={RT:.6f} K/2M={float(S0):.9f}")

# ---- B4: vacuum radicand sign on (0, r_t)
rt_v = mp.findroot(lambda s: rad(s, 0), mp.mpf(RT))
print("\nB4 vacuum radicand on (0, r_t):")
neg_all = True
for frac in ('1e-9','1e-6','1e-3','0.01','0.1','0.3','0.5','0.7','0.9','0.99','0.999'):
    s = rt_v*mp.mpf(frac); v = rad(s, 0)
    neg_all = neg_all and v < 0
    print(f"   s/r_t={frac:>7s}  radicand={mp.nstr(v,8)}")
print("   all strictly negative:", neg_all)

# ---- B5: bent radicand sign, and the two zeros
s_in = mp.findroot(lambda s: rad(s), S0)
s_out = mp.findroot(lambda s: rad(s), mp.mpf(RT)*mp.mpf('0.9995'))
print(f"\nB5 bent zeros: inner={mp.nstr(s_in,16)}  outer={mp.nstr(s_out,16)}  (vac r_t={mp.nstr(rt_v,16)})")
below = [(f, rad(s_in*mp.mpf(f))) for f in ('1e-6','1e-3','0.01','0.1','0.5','0.9','0.99')]
inside = [(f, rad(s_in + (s_out-s_in)*mp.mpf(f))) for f in ('0.001','0.01','0.1','0.5','0.9','0.99','0.999')]
print("   BELOW the inner zero (should be POSITIVE):")
for f,v in below: print(f"     s/s_in={f:>7s}  radicand={mp.nstr(v,8)}")
print("   BETWEEN the zeros (should be NEGATIVE):")
for f,v in inside: print(f"     t={f:>7s}  radicand={mp.nstr(v,8)}")
print("   below all positive:", all(v>0 for _,v in below), " between all negative:", all(v<0 for _,v in inside))

# ---- C6: endpoint shift as a fraction of the band's r-extent
frac_shift = s_in/rt_v
print(f"\nC6 band upper endpoint moves off r=0 by {mp.nstr(s_in,12)} Mpc")
print(f"   as a fraction of the band's r-extent (r_t): {mp.nstr(frac_shift,12)}")
print(f"   K/2M / r_t = {mp.nstr(S0/rt_v,12)}  (the naive radius, for comparison)")

# ---- C7: the fourth segment's advance in Re tau-tilde
def seg_real(lo, hi, sing_at_hi):
    """integral ds / sqrt(radicand) over (lo,hi); the singular end is a SIMPLE zero,
    removed exactly by u^2 = |s - s_end|.  Guard on the radicand's VALUE, not u==0."""
    L = mp.sqrt(hi-lo); end = hi if sing_at_hi else lo
    lim = 1/mp.sqrt(abs(drad(end)))
    def g(u):
        s = hi - u**2 if sing_at_hi else lo + u**2
        v = rad(s)
        return lim if v <= 0 else u/mp.sqrt(v)
    return 2*mp.quad(g, [0, L])
adv = seg_real(mp.mpf(0), s_in, True)
print(f"\nC7 the fourth segment's advance in Re tau-tilde = {mp.nstr(adv,14)} Mpc")
# the lap's real-time extent: collapse leg from -inf is unbounded, so use the lift's own
# imaginary extent pi*alpha/3 as the panel's comparable scale, plus the expansion to r_0
bound = mp.pi*A_/3
print(f"   against pi*alpha/3 = {mp.nstr(bound,14)} Mpc :  share = {mp.nstr(adv/bound,8)}")
exp_leg = mp.quad(lambda s: 1/mp.sqrt(rad(s)), [s_out*mp.mpf('1.0000001'), mp.mpf(R0)])
print(f"   the expansion leg out to r_0 ~ {mp.nstr(exp_leg,10)} Mpc : share = {mp.nstr(adv/exp_leg,8)}")

# ---- C8: dr/ds at the branch point on the bent cut -- the exponent
print("\nC8 approach exponent at the branch point, BENT cut (fit r ~ C*t^p on the 4th segment):")
for leg in ('matter',):
    pts=[]
    for e in (14,13,12,11,10,9,8):
        s = s_in*mp.mpf(10)**(-e)
        t = seg_real(mp.mpf(0), s, False) if False else None
        # real-time from the branch point to s: integral 0..s of ds/sqrt(rad)
        t = mp.quad(lambda x: 1/mp.sqrt(rad(x)), [mp.mpf(0), s])
        pts.append((t, s))
    for i in range(len(pts)-1):
        (t1,s1),(t2,s2) = pts[i],pts[i+1]
        p = mp.log(s2/s1)/mp.log(t2/t1)
        print(f"   p = {mp.nstr(p,10)}   between s/s_in = 1e-{14-i} and 1e-{13-i}")
# and dr/ds at r->0: with r ~ t^p, dr/dt ~ t^(p-1) -> infinity iff p<1
print("   ⇒ dr/d(real time) diverges at the branch point iff p < 1")
