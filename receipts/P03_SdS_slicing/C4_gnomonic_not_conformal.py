"""C4 — which projection does CR force, and what does it cost?
gnomonic: every great circle -> a straight line, NOT conformal.
stereographic: conformal, great circles -> circles.
ORIGIN: storyboard_receipts/C4_gnomonic_not_conformal.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
rng=np.random.default_rng(5)
gn = lambda p: np.array([p[0]/p[2], p[1]/p[2]])              # from the centre onto z=1
st = lambda p: np.array([p[0]/(1+p[2]), p[1]/(1+p[2])])      # from the south pole onto z=0

def great_circle_pts(n, m=9):
    a=np.cross(n,[0,0,1.])
    if np.linalg.norm(a)<1e-8: a=np.cross(n,[0,1.,0])
    a/=np.linalg.norm(a); b=np.cross(n,a)
    out=[]
    for t in np.linspace(0,2*np.pi,200):
        p=np.cos(t)*a+np.sin(t)*b
        if p[2]>0.35: out.append(p)          # keep the upper cap, where both charts are regular
    idx=np.linspace(0,len(out)-1,m).astype(int)
    return [out[i] for i in idx]

def straightness(pts):
    P=np.array(pts); P=P-P.mean(0)
    s=np.linalg.svd(P, compute_uv=False)
    return s[1]/s[0]

print("="*78); print("C4 — WHICH PROJECTION DOES CR FORCE, AND WHAT DOES IT COST?"); print("="*78)
print("\nSTEP 1 — great circles: residual ~0 means the image is a STRAIGHT LINE.")
print(f"  {'great circle':16s} {'gnomonic':>13s} {'stereographic':>16s}")
done=0
_straight=[]                                    # r2376+c54.159: keep the residuals that are printed
for k in range(12):
    n=rng.normal(size=3); n/=np.linalg.norm(n)
    pts=great_circle_pts(n)
    if len(pts)<6: continue
    print(f"  normal {done}          {straightness([gn(p) for p in pts]):13.2e} {straightness([st(p) for p in pts]):16.2e}")
    _straight.append((straightness([gn(p) for p in pts]), straightness([st(p) for p in pts])))
    done+=1
    if done==4: break
# r2376+c54.159 -- PINS STEP 1, the claim INDEX quotes as "residual ~1e-17": the gnomonic sends
# every great circle to a STRAIGHT LINE (second singular value / first = machine zero), and the
# stereographic does NOT (residuals 1.8e-2 .. 1.2e-1 -- circles, not lines).  Seed 5, four circles.
assert len(_straight) == 4, _straight
assert all(g < 1e-12 for g, _ in _straight), _straight
assert all(s > 1.0e-2 for _, s in _straight), _straight
assert abs(_straight[0][1] - 0.03216488) < 1e-7, _straight[0]     # the printed 3.22e-02, pinned
print("  => gnomonic sends every great circle to a STRAIGHT line; stereographic does not.")

print("\nSTEP 2 — conformality, tested on a GENERIC pair of tangent directions")
print("  (the PRINCIPAL pair is preserved by both -- testing it is the trap):")
def ang_after(proj,p,u,v,h=1e-6):
    def push(d):
        q=p+h*d; q/=np.linalg.norm(q); return (proj(q)-proj(p))/h
    U,V=push(u),push(v)
    return np.degrees(np.arccos(np.clip(U@V/(np.linalg.norm(U)*np.linalg.norm(V)),-1,1)))
_angles=[]                                      # r2376+c54.159: keep the printed angle triples
for k in range(4):
    p=rng.normal(size=3); p[2]=abs(p[2])+0.6; p/=np.linalg.norm(p)
    e1=np.cross(p,[0,0,1.]); e1/=np.linalg.norm(e1); e2=np.cross(p,e1)
    th=rng.uniform(0.3,1.2)                       # a GENERIC direction, not principal
    u=e1; v=np.cos(th)*e1+np.sin(th)*e2
    true=np.degrees(np.arccos(np.clip(u@v,-1,1)))
    print(f"   true {true:7.3f} deg  ->  gnomonic {ang_after(gn,p,u,v):8.3f}   stereographic {ang_after(st,p,u,v):8.3f}")
    _angles.append((true, ang_after(gn,p,u,v), ang_after(st,p,u,v)))
# r2376+c54.159 -- PINS STEP 2, the figure INDEX quotes verbatim: on a GENERIC tangent pair the
# gnomonic carries 60.723 deg to 77.500 deg (NOT conformal) while the stereographic returns the
# true angle to 1e-5 deg (conformal).  Every one of the four pairs is distorted by the gnomonic.
assert len(_angles) == 4, _angles
assert abs(_angles[0][0] - 60.7225217) < 1e-5, _angles[0]        # the true angle
assert abs(_angles[0][1] - 77.5002840) < 1e-5, _angles[0]        # gnomonic image -- INDEX's 60.7->77.5
assert all(abs(st_a - tr) < 1e-5 for tr, _, st_a in _angles), _angles     # stereographic is conformal
assert all(abs(gn_a - tr) > 1.5 for tr, gn_a, _ in _angles), _angles      # gnomonic never is
print("  => stereographic PRESERVES the angle (conformal); gnomonic DISTORTS it.")
print("\n" + "="*78)
print("RESULT C4:  P3 forces the GNOMONIC by a straight-line argument -- 'the unique projection")
print("  that sends every great circle to a straight line' -- and names only the orthographic as")
print("  excluded.  THE SAME ARGUMENT EXCLUDES THE STEREOGRAPHIC: it is THE CONFORMAL projection")
print("  and it sends great circles to CIRCLES.")
print("  => CR FORCES THE PROJECTION THAT PRESERVES STRAIGHTNESS OVER THE ONE THAT PRESERVES")
print("     ANGLES.  The celestial sphere is the Mobius group's canonical home; CR uses it")
print("     PROJECTIVELY, not conformally.  That is WHY the conformal apparatus finds no")
print("     purchase in the corpus -- a reason, not an absence.")
print("="*78)
