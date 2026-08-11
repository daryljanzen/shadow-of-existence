"""
F_flat.py -- verifies (and draws) panel (F): the cosmological bundle r(s) against arc length s in complex
  cosmic time. The bead's tau~ path is TWO PERPENDICULAR straight legs joined by the lift, so s is the EXACT
  arc length (|dtau~/ds|=1 on each leg): collapse (Im tau~=-pi/3, horizontal), the lift (Re tau~=0, vertical),
  expansion (Im tau~=0, horizontal). r(s) is single-valued, monotonic, smooth; continuous across both joints;
  dr/ds=0 at the turnaround r=-A=-cbrt2 alpha/sqrt3 (horizontal tangent, collapse stops) and dr/ds->inf at
  r=0 (vertical tangent, the bounded crossing); front seam at r=+alpha/sqrt3. [P7 CR_framework -- fig panel F]
STATUS: ✔✔   RUN: python3 F_flat.py   RUNTIME: ~3s (also writes F_flat.pdf/png)
CONTROL: the two horizontal legs and the vertical lift are perpendicular (dot product 0); s is arc length
  because each leg is unit-tau~-speed and straight -- not a numerical fit.
ORIGIN: corpus/F_flat.py, verified + strengthened + canonicalized r1357.
ORIGIN-DIVERGENCE: origin corpus/F_flat.py is the figure script; this is the verified+strengthened variant its INDEX row already names. Adjudicated r2376 (c54.3): THIS COPY AUTHORITATIVE.
"""
import numpy as np
al = 1.0
A  = 2**(1/3) * al / np.sqrt(3)          # = (2M a^2)^{1/3} at Nariai
P  = np.pi/3                             # the lift's length in s

def tau_of_s(s):                         # the tau~-path (complex), piecewise straight
    if s <= 0:      return complex(s, -P)              # collapse: horizontal, Im=-pi/3
    elif s < P:     return complex(0.0, s - P)         # lift: vertical, Re=0
    else:           return complex(s - P, 0.0)         # expansion: horizontal, Im=0
def r_of_s(s):
    s = np.asarray(s, float); out = np.empty_like(s)
    m1, m2, m3 = s <= 0, (s > 0) & (s <= P), s > P
    out[m1] = -A * np.cosh(1.5*s[m1])**(2/3)
    out[m2] = -A * np.sin(1.5*(P - s[m2]))**(2/3)
    out[m3] =  A * np.sinh(1.5*(s[m3] - P))**(2/3)
    return out
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
print("="*72); print("F_flat -- r(s) against exact arc length in complex cosmic time"); print("="*72)
# (1) arc-length exactness: |dtau~/ds|=1 on each leg; legs straight
h=1e-6
for s0,name in [(-0.5,'collapse'),(0.15,'lift'),(0.9,'expansion')]:
    v=(tau_of_s(s0+h)-tau_of_s(s0-h))/(2*h)
    ok&=check(f"|dtau~/ds|=1 on the {name} leg (unit-speed, straight) -> s is exact arc length", abs(abs(v)-1)<1e-4)
# (2) perpendicular legs: collapse/expansion horizontal, lift vertical
v_coll=(tau_of_s(-0.5+h)-tau_of_s(-0.5-h))/(2*h); v_lift=(tau_of_s(0.15+h)-tau_of_s(0.15-h))/(2*h)
ok&=check("collapse leg horizontal (Im const), lift vertical (Re const) -> PERPENDICULAR (dot=0)",
          abs(v_coll.imag)<1e-4 and abs(v_lift.real)<1e-4 and abs(v_coll.real*v_lift.real+v_coll.imag*v_lift.imag)<1e-4)
# (3) continuity across both joints
ok&=check("continuous at s=0 joint: r=-A both sides (the turnaround)", abs(float(r_of_s(-1e-7))-float(r_of_s(1e-7)))<1e-4 and abs(float(r_of_s(0.0))+A)<1e-9)
ok&=check("continuous at s=pi/3 joint: r=0 both sides (the seam)", abs(float(r_of_s(P-1e-7))-float(r_of_s(P+1e-7)))<1e-4 and abs(float(r_of_s(P)))<1e-6)
# (4) monotonic increasing over the whole path
ss=np.linspace(-2.0,2.6,4000); rs=r_of_s(ss)
ok&=check("r(s) single-valued & MONOTONIC increasing over the full path", np.all(np.diff(rs)>0))
# (5) tangents: dr/ds=0 at turnaround (s=0), dr/ds->inf at r=0 (s=pi/3)
dr0=(float(r_of_s(0.0+1e-5))-float(r_of_s(0.0-1e-5)))/(2e-5)
drP=(float(r_of_s(P-1e-9))-float(r_of_s(P-1e-6)))/( (P-1e-9)-(P-1e-6) )
ok&=check("dr/ds=0 at the turnaround r=-A (horizontal tangent, collapse stops)", abs(dr0)<1e-2)
ok&=check("dr/ds -> inf at r=0 (vertical tangent, the bounded crossing)", abs(drP)>50)
# (6) landmark values
ok&=check("turnaround r=-A=-cbrt2 alpha/sqrt3", abs(float(r_of_s(0.0)) - (-2**(1/3)/np.sqrt(3)))<1e-9)
s_seam = P + (2/3)*np.arcsinh(((1/np.sqrt(3))/A)**1.5)     # front seam on expansion leg
ok&=check("front seam reached at r=+alpha/sqrt3 on the expansion leg", abs(float(r_of_s(s_seam)) - 1/np.sqrt(3))<1e-6)
# (bonus) draw the figure
try:
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(6.0,6.0))
    for seg,col in [((-2.0,0),'#c0392b'),((0,P),'#c0392b'),((P,2.6),'#2471a3')]:
        xx=np.linspace(*seg,600); ax.plot(xx,r_of_s(xx),color=col,lw=3)
    ax.set_xlabel('$s/\\alpha$'); ax.set_ylabel('$r/\\alpha$'); ax.axhline(0,color='0.85',lw=0.8)
    plt.tight_layout(); plt.savefig('F_flat.png',dpi=120,bbox_inches='tight'); print("  (figure F_flat.png written)")
except Exception as e:
    print("  (figure skipped:", e, ")")
print("="*72)
print("RESULT:", "ALL PASS -- s is the exact arc length of two perpendicular straight legs + the lift; r(s)\n         single-valued, monotonic, smooth; horizontal tangent at the turnaround, vertical at the seam." if ok else "SOME FAILED")
print("="*72)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Every check above only PRINTED [PASS]/[FAIL] into `ok`, so the
# script exited 0 either way; `ok` is asserted here.  And two things the panel's caption states
# were never computed: the BACK SEAM at r = -2 alpha/sqrt3 (the caption's second seam; only the
# front seam +alpha/sqrt3 is checked above) and the seams' "2:1 spacing along s".  Both are
# computed here -- the back seam by bisecting r(s) on the collapse leg, and the spacing as the
# two seams' s-offsets from the two ends of the lift, which come out in the ratio 2 exactly.
assert ok, "F_flat: one of the printed checks FAILED"
def _bisect_r(target, lo, hi, n=200):
    g = lambda s_: float(r_of_s(s_)) - target
    for _ in range(n):
        mid = 0.5*(lo + hi)
        if g(lo)*g(mid) <= 0: hi = mid
        else: lo = mid
    return 0.5*(lo + hi)
s_back = _bisect_r(-2*al/np.sqrt(3), -3.0, -1e-9)                    # the BACK seam, r = -2a/sqrt3
assert abs(float(r_of_s(s_back)) + 1.1547005) < 1e-6                 # -2 alpha/sqrt3
assert abs(s_back + 0.87797193) < 1e-6                               # = -(2/3) arccosh 2
assert s_back < 0.0 and abs(float(r_of_s(0.0)) + A) < 1e-9           # it is BEFORE the turnaround
assert abs(float(r_of_s(s_seam)) - 0.57735027) < 1e-6                # the front seam, +alpha/sqrt3
ratio_2to1 = (0.0 - s_back)/(s_seam - P)      # back seam -> turnaround, vs lift end -> front seam
assert abs(ratio_2to1 - 2.0) < 1e-9                                  # ** the caption's 2:1 **
assert abs(float(r_of_s(s_back))/float(r_of_s(s_seam)) + 2.0) < 1e-6 # and the radii are 2:1 too
# CONTROL: the turnaround is NOT a seam -- r there is -cbrt2 alpha/sqrt3, not -2 alpha/sqrt3.
assert abs(float(r_of_s(0.0)) + 1.1547005) > 0.4
print(f"  [r2376+c54.161] back seam computed at s = {s_back:.8f}, r = {float(r_of_s(s_back)):.8f}")
print(f"  = -2 alpha/sqrt3; seam s-offsets from the lift's two ends in the ratio {ratio_2to1:.8f}")
print("  -- the caption's 2:1 spacing, and `ok` asserted so a FAIL now stops the run.")
print("="*72)
