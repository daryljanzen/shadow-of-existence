"""The two cubics as two REALISATIONS of one abstract A_2 three-fold  (receipt for P7 rem:tworealisations).

    horizon cubic      H(r) = r^3 - a^2 r + 2M a^2 = 0     (f = 0        : the slicing turns)
    turnaround cubic   T(r) = r^3        + 2M a^2 = 0      (1 - f = 0    : the worldline turns)
    H - T = -a^2 r                                          (the de Sitter/flat term)

Both are DEPRESSED (no r^2 term), so each root triple sums to zero -- the defining condition of an
A_2 weight triple.  They realise it differently, and that is exactly why lem:twoturnings finds no
canonical identification between their order-threes:

    HORIZON     : roots colinear-real in r; the 120-degree three-fold lives in the SKY ANGLE,
                  w, w +- 2pi/3, with r_k = (2/sqrt3) sin w_k and 2M = (2/3sqrt3) sin 3w
                  -- the corpus's own route (groupoid paper, prop:autA2, sec:autA2).
    TURNAROUND  : roots equilateral in the COMPLEX r-plane itself, equal moduli, 120-degree spacing.

R : r -> -r (equivalently 2M -> -2M) is the A_2 diagram automorphism on BOTH realisations, conjugating
3 <-> 3bar: on the horizon roots this is prop:autA2 (load-bearing because -1 is NOT in W(A_2)); on the
turnaround triangle it carries the +M triangle onto the -M one, a 60-degree rotation of the same figure.

SCOPE (groupoid paper, rem:a2-distinct, as it now stands): what is walled is the realised colour
ISOMETRY on the Lorentzian substrate (su(3) not contained in so(5,1)); what is do-not-assert is the
world-correspondence. Nothing here names colour, and nothing here is a claim about it. This receipt
concerns two realisations of the abstract root system inside the geometry.
"""
import numpy as np

al = 1.0
NARIAI = 2/(3*np.sqrt(3))

def hroots(twoM): return np.roots([1, 0, -al**2, twoM*al**2])   # horizon
def troots(twoM): return np.roots([1, 0,       0, twoM*al**2])   # turnaround

# ---- 1. both cubics are depressed: every root triple sums to zero (the A_2 weight condition)
for twoM in (0.05, 0.2, 0.3, NARIAI):
    assert abs(hroots(twoM).sum()) < 1e-12, 'horizon triple not zero-sum'
    assert abs(troots(twoM).sum()) < 1e-12, 'turnaround triple not zero-sum'

# ---- 2. H - T = -a^2 r, identically
rr = np.linspace(-3, 3, 3001)
for twoM in (0.05, 0.3, NARIAI):
    H = rr**3 - al**2*rr + twoM*al**2
    T = rr**3 + twoM*al**2
    assert np.allclose(H - T, -al**2*rr), 'H - T is not the de Sitter term'

# ---- 3. the horizon's three-fold lives in the sky angle; its roots are colinear-real
for twoM in (0.05, 0.2, 0.3):
    h = np.sort(hroots(twoM).real)
    assert np.allclose(hroots(twoM).imag, 0, atol=1e-12), 'horizon roots not real (sub-Nariai)'
    w = np.arcsin(twoM/NARIAI)/3
    ws = np.array([w, w + 2*np.pi/3, w - 2*np.pi/3])
    assert np.allclose(np.sort((2/np.sqrt(3))*np.sin(ws)), h), 'sky-angle triple does not give the roots'
    d = np.diff(np.sort(ws))
    assert np.allclose(d, 2*np.pi/3), 'sky angles not equally spaced by 120 degrees'

# ---- 4. the turnaround's three-fold lives in the complex r-plane: equal moduli, 120 degrees
for twoM in (0.05, 0.2, 0.3, NARIAI):
    t = troots(twoM)
    assert np.allclose(np.abs(t), np.abs(t[0])), 'turnaround roots not equal in modulus'
    a = np.sort(np.angle(t))
    assert np.allclose(np.diff(a), 2*np.pi/3), 'turnaround roots not 120 degrees apart'
    assert abs(np.abs(t[0]) - abs(twoM*al**2)**(1/3)) < 1e-12, 'turnaround modulus != (2M a^2)^{1/3}'

# ---- 5. the two realisations are genuinely different: the turnaround triple is NEVER colinear-real
for twoM in (0.05, 0.2, 0.3, NARIAI):
    assert np.sum(np.abs(troots(twoM).imag) < 1e-9) == 1, 'turnaround should have exactly one real root'

# ---- 6. R : r -> -r carries the +M turnaround triangle onto the -M one (a 60-degree rotation)
for twoM in (0.05, 0.2, 0.3, NARIAI):
    tp, tm = troots(twoM), troots(-twoM)
    assert np.allclose(np.sort_complex(-tp), np.sort_complex(tm)), 'R does not exchange the triangles'
    # a triple with 120-degree symmetry negated is that triple turned by 60 degrees (mod 120)
    ap, am = np.sort(np.angle(tp) % (2*np.pi/3)), np.sort(np.angle(tm) % (2*np.pi/3))
    off = np.mod(am - ap, 2*np.pi/3)
    assert np.allclose(off, off[0]), 'the exchange is not a rigid turn of the triangle'
    assert min(abs(off[0] - np.pi/3), abs(off[0] - np.pi/3 + 2*np.pi/3),
               abs(off[0] - np.pi/3 - 2*np.pi/3)) < 1e-9, 'the turn is not 60 degrees'

# ---- 7. R on the horizon roots: the same exchange (prop:autA2's r -> -r on 2M -> -2M)
for twoM in (0.05, 0.2, 0.3):
    assert np.allclose(np.sort(-hroots(twoM).real), np.sort(hroots(-twoM).real)), 'R fails on horizon roots'

# ---- 8. the A_2-specific fact prop:autA2 leans on: -1 is not in W(A_2)
#         W(A_2) = S_3 acting on the plane as rotations by 0, +-120 and three reflections; none is -id.
th = np.array([0, 2*np.pi/3, -2*np.pi/3])
rots = [np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]]) for t in th]
refls = [np.array([[np.cos(2*t), np.sin(2*t)], [np.sin(2*t), -np.cos(2*t)]]) for t in (0, np.pi/3, 2*np.pi/3)]
assert not any(np.allclose(g, -np.eye(2)) for g in rots + refls), '-1 unexpectedly in W(A_2)'

# ---- 9. the massless/de Sitter limit: the two realisations meet only there
assert np.allclose(np.sort(troots(0.0)), 0), 'turnaround triple should collapse to r=0 at 2M=0'
assert np.allclose(np.sort(hroots(0.0).real), np.array([-al, 0.0, al])), 'horizon roots at 2M=0'


# ---- 10. THE FAMILY the affine test could not see: the two cubics are two ENERGIES of one congruence
#          radial geodesics obey (dr/dtau)^2 = E^2 - f, turning where E^2 = f, i.e.
#              r^3 + (E^2 - 1) a^2 r + 2 M a^2 = 0
#          E = 1 (marginally bound, k = 0, the flat leaf)  -> r^3 + 2M a^2       : the TURNAROUND cubic
#          E = 0 (k = +1, the maximally bound member)      -> r^3 - a^2 r + 2M a^2: the HORIZON cubic
#          The corpus already carries the family and -k = E^2 - 1 (slicing-operator paper, eq:Ek).
import sympy as _sp
_r, _E, _M = _sp.symbols('r E M', positive=True)
_f = 1 - 2*_M/_r - _r**2
_turn = _sp.expand(_sp.numer(_sp.together(_E**2 - _f)))
assert _sp.expand(_turn - (_r**3 + (_E**2 - 1)*_r + 2*_M)) == 0, 'turning cubic is not the E-family'
assert _sp.expand(_turn.subs(_E, 1) - (_r**3 + 2*_M)) == 0,      'E=1 member is not the turnaround cubic'
assert _sp.expand(_turn.subs(_E, 0) - (_r**3 - _r + 2*_M)) == 0, 'E=0 member is not the horizon cubic'

# the family's discriminant, and where it vanishes
_D = _sp.factor(_sp.discriminant(_r**3 + (_E**2 - 1)*_r + 2*_M, _r))
assert _sp.simplify(_D - 4*((1 - _E**2)**3 - 27*_M**2)) == 0, 'discriminant of the E-family'
#   Delta = 0  <=>  1 - E^2 = 3 M^{2/3}
for _Mv in (0.02, 0.08, 0.15):
    _lam = 3*_Mv**(2/3)
    assert abs((1 - _lam)**0 * ((_lam)**3 - 27*_Mv**2)) < 1e-12, 'crossing condition'
    assert 0 < _lam < 1, 'sub-Nariai: the crossing lies strictly between the two members'
#   at Nariai the crossing arrives exactly at E = 0 -- the same statement as the double root
_MN = float(1/(3*np.sqrt(3)))
assert abs(3*_MN**(2/3) - 1.0) < 1e-12, 'at Nariai the crossing reaches E=0 exactly'
#   so the configurations differ because the family crosses Delta between them, not because
#   the two three-folds are unrelated: at E=1 equilateral (pure cube), at E=0 colinear-real
for _Ev, _shape in ((1.0, 'equilateral'), (0.0, 'colinear')):
    _rt = np.roots([1, 0, _Ev**2 - 1, 2*0.15])
    if _shape == 'equilateral':
        assert np.ptp(np.abs(_rt)) < 1e-9, 'E=1 roots not equilateral'
    else:
        assert np.abs(_rt.imag).max() < 1e-9, 'E=0 roots not colinear-real'

print('ok | both cubics zero-sum; H-T = -a^2 r; horizon three-fold in the sky angle (colinear-real in r);')
print('   | turnaround three-fold equilateral in the complex r-plane, modulus (2M a^2)^{1/3};')
print('   | R exchanges 3 <-> 3bar on BOTH realisations; -1 not in W(A_2); the two meet only at 2M=0.')
