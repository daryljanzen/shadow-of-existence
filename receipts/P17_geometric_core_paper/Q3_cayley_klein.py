"""Q3 — Cayley-Klein: is the substrate's metric a log-cross-ratio against the absolute,
and is alpha the CK scale constant?   Substrate dS_5 = {X in M^6 : eta(X,X)=alpha^2}.
ORIGIN: storyboard_receipts/Q3_cayley_klein.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
a=1.0
eta=np.diag([-1.,1.,1.,1.,1.,1.])
ip=lambda P,Q: P@eta@Q
def on_dS(v):
    n=ip(v,v); assert n>0, f"not spacelike: eta={n}"; return v*a/np.sqrt(n)
def absolute_params(P,Q):
    D=Q-P; A=ip(D,D); B=2*ip(P,D); C=ip(P,P)
    disc=B*B-4*A*C
    if disc<0 or abs(A)<1e-14: return None
    r=np.sqrt(disc); return ((-B+r)/(2*A), (-B-r)/(2*A))
def cross_ratio(l1,l2,l3,l4):
    return ((l1-l3)*(l2-l4))/((l2-l3)*(l1-l4))

print("="*78)
print("Q3 — CAYLEY-KLEIN ON THE SUBSTRATE.   absolute = {eta(X,X)=0};  substrate = its exterior")
print("="*78)
# a point on dS_5, and partners reached by BOOST (timelike sep) or ROTATION (spacelike sep)
P = on_dS(np.array([0.,1,0,0,0,0.]))
print("\nSTEP 1 — the line PQ meets the ABSOLUTE iff |u|>1,  u := eta(P,Q)/a^2.")
print("  Predicted discriminant: 4 a^4 (u^2 - 1).")
print(f"  {'pair':22s} {'u':>10s} {'disc':>12s} {'4a^4(u^2-1)':>14s} {'meets?':>8s}")
for lab,Q in [("boost t=0.8 (timelike)", on_dS(np.array([np.sinh(.8),np.cosh(.8),0,0,0,0.]))),
              ("boost t=1.6 (timelike)", on_dS(np.array([np.sinh(1.6),np.cosh(1.6),0,0,0,0.]))),
              ("rot  s=0.6 (spacelike)", on_dS(np.array([0.,np.cos(.6),np.sin(.6),0,0,0.]))),
              ("rot  s=1.2 (spacelike)", on_dS(np.array([0.,np.cos(1.2),np.sin(1.2),0,0,0.])))]:
    u=ip(P,Q)/a**2
    D=Q-P; A=ip(D,D); B=2*ip(P,D); C=ip(P,P); disc=B*B-4*A*C
    # ** r2376+c54.157: this column read 4*(u*u-1), DROPPING the alpha^4 the paper's formula
    #    carries.  It agreed only because a = 1.0 is set at the top of the file; at alpha = 2.5
    #    the true discriminant is 123.239412 and the printed expression gives 3.154929.  The
    #    receipt-vs-sentence pass found it. **
    _pred = 4 * a**4 * (u * u - 1)
    print(f"  {lab:22s} {u:10.6f} {disc:12.6f} {_pred:14.6f} {str(disc>=0):>8s}")
    assert abs(disc - _pred) < 1e-9, f"disc {disc} != 4 alpha^4 (u^2-1) = {_pred}"

print("\nSTEP 2 — TIMELIKE pairs: does (k/2)|log CR| return the geodesic proper time?  (u = cosh(tau/a))")
print(f"  {'rapidity':>9s} {'u':>10s} {'tau=a.arccosh u':>16s} {'|log CR|':>11s} {'tau / |log CR|':>15s}")
for t in [0.4,0.8,1.2,1.9,2.6]:
    Q=on_dS(np.array([np.sinh(t),np.cosh(t),0,0,0,0.]))
    u=ip(P,Q)/a**2; tau=a*np.arccosh(u)
    lp,lm=absolute_params(P,Q)
    L=abs(np.log(abs(cross_ratio(0.0,1.0,lp,lm))))
    print(f"  {t:9.3f} {u:10.6f} {tau:16.6f} {L:11.6f} {tau/L:15.8f}")

print("\nSTEP 3 — SPACELIKE pairs: the line MISSES the absolute, so the roots are complex.")
print("  CK then gives an ANGLE: sigma = a.arccos(u).  Test (k/2)|log CR| with COMPLEX roots.")
print(f"  {'arc s':>8s} {'u':>10s} {'sigma=a.arccos u':>17s} {'(1/2)|Im log CR|':>18s} {'ratio':>10s}")
for sarc in [0.3,0.6,1.0,1.5,2.0]:
    Q=on_dS(np.array([0.,np.cos(sarc),np.sin(sarc),0,0,0.]))
    u=ip(P,Q)/a**2; sig=a*np.arccos(u)
    D=Q-P; A=ip(D,D); B=2*ip(P,D); C=ip(P,P)
    disc=complex(B*B-4*A*C); r=np.sqrt(disc)
    lp,lm=((-B+r)/(2*A), (-B-r)/(2*A))
    cr=cross_ratio(0.0+0j,1.0+0j,lp,lm)
    val=0.5*abs(np.angle(cr))
    print(f"  {sarc:8.3f} {u:10.6f} {sig:17.6f} {val:18.6f} {sig/val if val>1e-12 else float('nan'):10.6f}")

print("\nSTEP 4 — is alpha really the CK constant, or an artefact of setting a=1?")
for aa in [1.0, 2.5, 7.3]:
    a=aa
    P2=on_dS(np.array([0.,1,0,0,0,0.]))
    t=1.1
    Q2=on_dS(np.array([np.sinh(t),np.cosh(t),0,0,0,0.]))
    u=ip(P2,Q2)/a**2; tau=a*np.arccosh(u)
    lp,lm=absolute_params(P2,Q2)
    L=abs(np.log(abs(cross_ratio(0.0,1.0,lp,lm))))
    print(f"   alpha={aa:5.2f}   tau={tau:9.6f}   |log CR|={L:9.6f}   tau/|log CR| = {tau/L:.8f}  -> k = {2*tau/L:.6f}")
print("\n  => k = alpha exactly, at every alpha.  The CK scale constant IS the throat radius.")

print("\n" + "="*78)
print("RESULT — COMPUTED:")
print("  The substrate's geodesic separation IS the Cayley-Klein log-cross-ratio against the")
print("  absolute {eta(X,X)=0}, with CK constant k = alpha EXACTLY:")
print("     timelike   tau   = (alpha/2)|log CR|          [exact, every rapidity, every alpha]")
print("     spacelike  sigma = (alpha/2)|arg CR|          [exact for sigma < pi.alpha/2;")
print("                                                    past that the principal branch wraps]")
print("  and the discriminant 4.alpha^4(u^2-1), u := eta(P,Q)/alpha^2, decides which:")
print("     |u|>1 -> the line MEETS the absolute (real log)   |u|<1 -> it misses (an angle).")
print("BOUND — TRACED, not computed here: that the SCALE is the CK construction's only free")
print("  constant is standard Cayley-Klein theory, not a result of this script.")
print("="*78)


# =====================================================================
# ** THE DISCRIMINANT AT alpha != 1, added r2376+c54.157. **
# The check above now carries alpha^4, but every row of it still runs at alpha = 1, where alpha^4
# is invisible.  The paper's formula is general, so it is tested generally here.
print()
print("=" * 78)
print("THE DISCRIMINANT'S alpha^4, WHICH alpha = 1 CANNOT SEE")
print("=" * 78)
print(f"  {'alpha':>8} {'rapidity':>10} {'disc':>16} {'4 alpha^4 (u^2-1)':>20}")
for _a in (1.0, 2.5, 7.3):
    for _t in (0.4, 0.8):
        _P = np.array([0.0, _a, 0.0, 0.0, 0.0, 0.0])
        _Q = np.array([_a * np.sinh(_t), _a * np.cosh(_t), 0.0, 0.0, 0.0, 0.0])
        _u = ip(_P, _Q) / _a**2
        _D = _Q - _P
        _A, _B, _C = ip(_D, _D), 2 * ip(_P, _D), ip(_P, _P)
        _disc = _B * _B - 4 * _A * _C
        _pred = 4 * _a**4 * (_u * _u - 1)
        print(f"  {_a:>8.2f} {_t:>10.2f} {_disc:>16.6f} {_pred:>20.6f}")
        assert abs(_disc - _pred) < 1e-6 * max(1.0, abs(_pred)), \
            f"alpha={_a}: disc {_disc} != {_pred}"
print("\n  ** the alpha^4 is now exercised: at alpha = 2.5 the two agree at 123.24, where the")
print("     old expression would have given 3.15. **")
print("  CHECKS PASS")
