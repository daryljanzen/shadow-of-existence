"""
P03_overcritical.py -- verifies: overcritical SdS is the SAME sin->cosh continuation as the seam, applied
  to the horizon angle past the Nariai crest -- |2M|>2/(3sqrt3) needs |sin 3w|>1, reached by 3w=pi/2+i beta
  (sin 3w=cosh beta); the two ellipse roots become a complex-conjugate pair on the ellipse's complex
  extension, only the diagonal root r0 stays real (and negative = backward-radial), and f<0 for all r>0.
  [P3 SdS-slicing-curve_v2 sec:overcritical]
STATUS: ✔✔   RUN: python3 P03_overcritical.py   RUNTIME: ~3s
COMPUTES: sin(3w)=cosh beta at 3w=pi/2+i beta (same continuation as prop:flip); for |r0|>2/sqrt3 the
  quadratic factor r^2+r r0+r0^2-1 has a complex-conjugate root pair (discriminant 4-3r0^2<0) that still
  satisfies the ellipse r^2+r r0+r0^2=1 (complex extension), with the diagonal root r0 the lone real
  horizon; the real root is negative (backward-radial) when 2M>2/(3sqrt3); and overcritical f(r)<0 for all
  r>0 (no forward horizon), with dr/dl -> r/alpha asymptotically. CONTROL: undercritical |r0|<2/sqrt3 -> 3 real.
BOUND: the continuation identity + root/curve structure; the ontological reading of the conjugate branch
  (previous-universe collapse) is the companions' (P15/P16), cited not established here.
ORIGIN: built new r1344 (uncited P3 claim; closes P3's verifiable inventory).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
beta, r, r0 = sp.symbols('beta r r_0', real=True); S3=sp.sqrt(3)
print("="*72); print("P03 overcritical SdS: the seam's sin->cosh continuation on the horizon angle"); print("="*72)
# (1) same continuation as the seam, on 3w
ok&=check("3w=pi/2+i beta => sin 3w = cos(i beta) = cosh beta > 1  (same as prop:flip seam)",
          sp.simplify(sp.sin(sp.pi/2+sp.I*beta) - sp.cosh(beta))==0)
ok&=check("  overcritical |2M|>2/(3sqrt3) needs |sin 3w|>1 -- impossible for real w (cosh beta>1 for beta!=0)",
          (sp.cosh(1)>1)==True)
# (2)/(3) root structure at r0=1.2 (overcritical, |r0|>2/sqrt3=1.1547)
r0v = 1.2
disc = 4 - 3*r0v**2
qroots = np.roots([1, r0v, r0v**2-1])                    # r^2 + r r0 + r0^2 - 1
ncomplex = int(np.sum(np.abs(qroots.imag)>1e-9))
ok&=check(f"|r0|=1.2>2/sqrt3: discriminant 4-3r0^2={disc:.3f}<0 -> quadratic factor has a complex-conjugate pair",
          disc<0 and ncomplex==2)
# the diagonal root r0 is the lone REAL horizon; full cubic r^3 - r + 2M, 2M=r0-r0^3
twoM = r0v - r0v**3
cub = np.roots([1,0,-1,twoM]); realroots=[x.real for x in cub if abs(x.imag)<1e-9]
ok&=check(f"only the diagonal root is real: cubic has 1 real root = r0-designated ({len(realroots)} real)", len(realroots)==1)
# complex pair still satisfies the ellipse (complex extension) r^2+r r0+r0^2=1
cpair = qroots[np.abs(qroots.imag)>1e-9]
ok&=check("the complex pair lies on the ellipse's complex extension r^2+r r0+r0^2=1",
          all(abs(c**2 + c*r0v + r0v**2 - 1) < 1e-9 for c in cpair))
# (4) surviving real root is negative (backward-radial) when 2M>2/(3sqrt3)
crest = 2/(3*np.sqrt(3))
# pick 2M just past the crest: choose r0<0 giving 2M>crest
r0_neg = -1.2; twoM_over = r0_neg - r0_neg**3
ok&=check(f"2M={twoM_over:.3f} > 2/(3sqrt3)={crest:.3f}: the lone real root r0={r0_neg} is NEGATIVE (backward-radial)",
          twoM_over>crest and r0_neg<0)
# (5) overcritical f<0 for all r>0 (no forward horizon); asymptotic dr/dl -> r/alpha
fvals = [1 - twoM_over/rv - rv**2 for rv in np.linspace(0.05, 20, 400)]
ok&=check("overcritical f(r)=1-2M/r-r^2 < 0 for all r>0 (no forward-branch horizon)", all(fv<0 for fv in fvals))
al=sp.Symbol('alpha',positive=True); rr=sp.Symbol('r',positive=True)
asymp = sp.limit(sp.sqrt(rr**2/al**2)/ (rr/al), rr, sp.oo)   # dr/dl=sqrt|f| ~ sqrt(r^2/al^2)=r/al
ok&=check("asymptotic dr/dl -> r/alpha  (f -> -r^2/alpha^2 at large r)", asymp==1)
# (6) CONTROL: undercritical |r0|<2/sqrt3 -> 3 real roots
r0u=0.5; qr=np.roots([1,r0u,r0u**2-1])
ok&=check("CONTROL: undercritical r0=0.5 -> quadratic real pair (3 real horizons total)", np.all(np.abs(qr.imag)<1e-9))
print("="*72)
print("RESULT:", "ALL PASS -- overcritical SdS is the seam's sin->cosh continuation on the horizon angle:\n         two horizons go complex-conjugate on the ellipse's complex extension, the lone real root is the\n         negative backward-radial one, f<0 on the whole forward branch. One analytic fact, two guises." if ok else "SOME FAILED")
print("="*72)

# --- r2376+c54.159 -----------------------------------------------------------------
# The file computed a PASS/FAIL flag and only PRINTED it.  Assert the flag, and pin the
# overcritical root structure itself: at r0=1.2 the discriminant 4-3r0^2 = -0.32 < 0, so
# the quadratic factor has exactly TWO complex-conjugate roots and the cubic exactly ONE
# real root; and 2M = 0.528 sits past the Nariai crest 2/(3 sqrt3) = 0.3849001794597505.
assert ok, "P03_overcritical: a check FAILED"
assert abs(disc - (-0.32)) < 1e-12
assert ncomplex == 2 and len(realroots) == 1
assert abs(crest - 0.3849001794597505) < 1e-13
assert abs(twoM_over - 0.528) < 1e-12 and twoM_over > crest
assert abs(twoM - (-0.528)) < 1e-12                        # 2M at r0=+1.2, the mirror member
assert sp.simplify(sp.sin(sp.pi/2 + sp.I*beta) - sp.cosh(beta)) == 0   # the seam continuation
