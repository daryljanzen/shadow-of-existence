"""P03_the_substrate_does_not_display_the_tidal_discriminant.py (r7489+cc66) --
the de Sitter substrate's own invariants do NOT tell the two critical points apart, and the whole
of the discriminating content is the M/r^3 term.

WHERE IT CAME FROM.  PO-91's last computation, assigned by r7489 (1).  r7463 (d) found that a
falling worldline tells the horizon critical point from the pivot critical point by a tidal
measurement whose answer does not depend on how fast it is falling.  The row's discharge condition
needed the other half: whether the SUBSTRATE, read on its own, displays that discriminant.

WHAT IS THE CORPUS'S ALREADY, AND IS NOT CLAIMED HERE.  P3 sec:sweep says in ink that the substrate
is maximally symmetric, that r=0 is a REGULAR point of it -- "a point ON the throat circle, at
X_1 = -alpha" -- and that the two critical points are "topologically identical on the substrate",
the lopsidedness being "a feature of the vantage-dependent description, not of the substrate".
** This receipt does not report that as a finding. ** What P3 nowhere does is compute it at the
quantity the row turns on; that computation is this receipt's, and so is the decomposition in (5).

WHAT IS NOT CLAIMED.  That the discriminant is "the pivot's".  P3 sec:sweep settles by computation
that the term does not track the SELECTED offset (three offsets, one K_G) and proves that whether it
tracks the cut's being off-axis AT ALL is UNDECIDABLE, since 2M = r_0 - r_0^3 makes mass and offset
vanish together.  Nothing here reaches past that bound.

COMPUTES: the substrate's Riemann tensor, its four cheap local scalar invariants, and the
  orthonormal tidal components a radially boosted observer measures on it, at D=4 and D=5; the same
  for the swept SdS chart as a control; and P3's K_G identity.  ** It pins no external numeric
  literal, and does not invent one: every statement is a symbolic identity in (r, theta, alpha, M, w),
  which is the legitimate UNPINNED-only case -- a structural check with no external figure to pin. **

VERDICTS ARE ASSERTS, and each was written after its output was read (r1676's rule).  The central
verdict in (4) is written as an assert over two SYMBOLIC radii rather than two sampled points,
because sampling cannot establish an absence.
LEVEL: L1 READING.  A property of the substrate layer, read on the substrate layer: every local
  curvature invariant of it is one constant, so no pair of its points is separated by one.
"""
import sympy as sp

t, r, th, ph, chi, w = sp.symbols('t r theta phi chi w', real=True)
al, M = sp.symbols('alpha M', positive=True)
r1, r2 = sp.symbols('r_1 r_2', positive=True)


def is_zero(x):
    """An EXACT zero test, stronger than `simplify`, with no sampling in it.

    ** Why it exists, at the line that caused it. ** The (1) check below first failed on exactly
    ONE component of 256: R_{r phi phi theta}, returned as
    r*(sin(2th)*tan(th) + cos(2th) - 1)/(2*tan(th)), whose numerator is identically zero by hand
    (sin(2t)tan(t) = 2sin^2 t, cos(2t) - 1 = -2sin^2 t) and which `simplify` would not normalise
    against the double angle.  The repair is a stronger exact NORMALISATION -- never a loosened
    check and never a whitelisted component.  Every step is an exact rewrite, so this can only find
    zeros that are there; it cannot report a non-zero as zero.
    """
    x = sp.simplify(x)
    if x == 0:
        return True
    for f in (lambda e: sp.simplify(sp.expand_trig(sp.expand(e))),
              lambda e: sp.simplify(sp.cancel(sp.together(sp.expand_trig(e.rewrite(sp.sin))))),
              lambda e: sp.simplify(sp.trigsimp(sp.expand_trig(e)))):
        try:
            if f(x) == 0:
                return True
        except Exception:
            pass
    return False


def curvature(g, x):
    """Christoffels -> Riemann (indices down) -> Ricci, R, Kretschmann.

    Convention R^a_bcd = d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb.  The convention is
    NOT asserted: control (8) validates it against a known non-zero Weyl square, so a sign error
    could not pass as a vanishing invariant on the substrate.
    """
    n, gi = len(x), g.inv()
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                s = sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                  - sp.diff(g[b, c], x[d])) for d in range(n) if gi[a, d] != 0)
                G[a][b][c] = G[a][c][b] = sp.simplify(s/2)
    Rud = [[[[sp.simplify(sp.diff(G[a][d][b], x[c]) - sp.diff(G[a][c][b], x[d])
                          + sum(G[a][c][e]*G[e][d][b] - G[a][d][e]*G[e][c][b] for e in range(n)))
              for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Rl = [[[[sp.simplify(sum(g[a, e]*Rud[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for d in range(n):
            Ric[b, d] = sp.simplify(sum(Rud[a][b][a][d] for a in range(n)))
    Rs = sp.simplify(sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n)))
    K = sp.simplify(sum(Rl[a][b][c][d]**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]
                        for a in range(n) for b in range(n) for c in range(n) for d in range(n)
                        if Rl[a][b][c][d] != 0))
    ric2 = sp.simplify(sum(Ric[a, b]**2*gi[a, a]*gi[b, b] for a in range(n) for b in range(n)))
    return dict(g=g, gi=gi, x=x, Rl=Rl, Ric=Ric, Rs=Rs, K=K, ric2=ric2, n=n)


def weyl_square(c):
    g, gi, Rl, Ric, Rs, n = c['g'], c['gi'], c['Rl'], c['Ric'], c['Rs'], c['n']
    D = sp.Integer(n)
    out = 0
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    C = (Rl[a][b][cc][d]
                         + (g[a, d]*Ric[cc, b] + g[b, cc]*Ric[d, a]
                            - g[a, cc]*Ric[d, b] - g[b, d]*Ric[cc, a])/(D - 2)
                         + Rs*(g[a, cc]*g[d, b] - g[a, d]*g[cc, b])/((D - 1)*(D - 2)))
                    C = sp.simplify(C)
                    if C != 0:
                        out += C**2*gi[a, a]*gi[b, b]*gi[cc, cc]*gi[d, d]
    return sp.simplify(out)


def boosted_tidal(c, F, it=0, ir=1, ia=2):
    """The orthonormal tidal components a RADIALLY BOOSTED observer measures.

    ** The frame legs are the trap r7463 fell into and caught: with g_tt = -F and g_rr = 1/F the
    unit timelike leg carries 1/sqrt(F) and the unit radial leg carries sqrt(F), NOT the reverse.
    Swapping them is invisible in R_[t r t r] -- the two wrong factors cancel there -- and shows
    only in the siblings, so the legs are written out rather than inlined. **
    """
    g, Rl = c['g'], c['Rl']
    e = {it: 1/sp.sqrt(F), ir: sp.sqrt(F), ia: 1/sp.sqrt(g[ia, ia])}
    o = lambda a, b, cc, d: sp.simplify(Rl[a][b][cc][d]*e[a]*e[b]*e[cc]*e[d])
    Rtrtr, Rtata, Rrara = o(it, ir, it, ir), o(it, ia, it, ia), o(ir, ia, ir, ia)
    ch, sh = sp.cosh(w), sp.sinh(w)
    return dict(Rtrtr=sp.simplify(Rtrtr),
                Rtata=sp.simplify(ch**2*Rtata + sh**2*Rrara),
                Rrara=sp.simplify(sh**2*Rtata + ch**2*Rrara))


F_dS = 1 - r**2/al**2
f_sds = 1 - 2*M/r - r**2/al**2

print("(1) THE SUBSTRATE'S RIEMANN IS THE CONSTANT-CURVATURE FORM, AT D=4 AND D=5")
print("    P3 sec:slicing makes the substrate proper dS_5 = SO(5,1)/SO(4,1) while the paper works")
print("    the equatorial section throughout, so a statement true only at the section's dimension")
print("    would not be the substrate's.  Both are taken.")
subs = {4: curvature(sp.diag(-F_dS, 1/F_dS, r**2, r**2*sp.sin(th)**2), [t, r, th, ph]),
        5: curvature(sp.diag(-F_dS, 1/F_dS, r**2, r**2*sp.sin(th)**2,
                             r**2*sp.sin(th)**2*sp.sin(chi)**2), [t, r, th, chi, ph])}
for D in (4, 5):
    c, g, n = subs[D], subs[D]['g'], subs[D]['n']
    bad = [(a, b, cc, d) for a in range(n) for b in range(n) for cc in range(n) for d in range(n)
           if not is_zero(c['Rl'][a][b][cc][d]
                          - (g[a, cc]*g[b, d] - g[a, d]*g[b, cc])/al**2)]
    print(f"    D={D}: {n**4} components, {len(bad)} deviations from "
          f"R_abcd = (g_ac g_bd - g_ad g_bc)/alpha^2")
    assert not bad, f"D={D}: the substrate Riemann is not the constant-curvature form: {bad}"

print("(2) EVERY CHEAP LOCAL SCALAR INVARIANT IS ONE CONSTANT -- AS AN IDENTITY, NOT A SAMPLE")
for D in (4, 5):
    c = subs[D]
    inv = {'R': c['Rs'], 'Ric^2': c['ric2'], 'Kretschmann': c['K'], 'Weyl^2': weyl_square(c)}
    for nm, val in inv.items():
        print(f"    D={D}  {nm:12s} = {sp.simplify(val)}")
        for xx in c['x']:
            assert is_zero(sp.diff(val, xx)), f"D={D}: {nm} depends on {xx}"
    assert is_zero(inv['Weyl^2']), f"D={D}: Weyl^2 does not vanish on the substrate"

print("(3) THE FALLING OBSERVER'S TIDAL TENSOR ON THE SUBSTRATE")
T = {}
for D in (4, 5):
    T[D] = boosted_tidal(subs[D], F_dS)
    print(f"    D={D}  R_[t r t r] = {T[D]['Rtrtr']}    R_[t a t a] = {T[D]['Rtata']}"
          f"    R_[r a r a] = {T[D]['Rrara']}")
    for nm in ('Rtrtr', 'Rtata', 'Rrara'):
        assert is_zero(sp.diff(T[D][nm], w)), f"D={D}: {nm} depends on the infall rapidity"
        for xx in subs[D]['x']:
            assert is_zero(sp.diff(T[D][nm], xx)), f"D={D}: {nm} depends on position ({xx})"
    assert is_zero(T[D]['Rtrtr'] - T[D]['Rtata']), \
        f"D={D}: the substrate's tidal tensor is not isotropic"

print("(4) THE VERDICT, AS AN ASSERT OVER TWO SYMBOLIC RADII -- sampling cannot prove an absence")
for D in (4, 5):
    for nm in ('Rtrtr', 'Rtata', 'Rrara'):
        q = T[D][nm]
        assert is_zero(q.subs(r, r1) - q.subs(r, r2)), \
            f"D={D}: {nm} separates two radii, so the substrate DOES display the discriminant"
    for nm, val in (('R', subs[D]['Rs']), ('K', subs[D]['K']), ('Ric^2', subs[D]['ric2'])):
        assert is_zero(val.subs(r, r1) - val.subs(r, r2)), \
            f"D={D}: {nm} separates two radii"
print("    NO local invariant and NO boosted tidal component of the substrate separates r_1 from")
print("    r_2 for ARBITRARY distinct radii => the two critical points are not separated either,")
print("    wherever they sit.  ** The substrate does not display the discriminant. **")

print("(5) AND THE WHOLE DISCRIMINATING CONTENT IS THE M/r^3 TERM")
sds4 = curvature(sp.diag(-f_sds, 1/f_sds, r**2, r**2*sp.sin(th)**2), [t, r, th, ph])
Ts = boosted_tidal(sds4, f_sds)
print(f"    swept  R_[t r t r]   = {Ts['Rtrtr']}")
print(f"    swept  R_[t th t th] = {Ts['Rtata']}")
assert is_zero(Ts['Rtrtr'] - (T[4]['Rtrtr'] - 2*M/r**3)), \
    "the swept R_[t r t r] is not the substrate's constant plus -2M/r^3"
assert is_zero(Ts['Rtata'] - (T[4]['Rtata'] + M/r**3)), \
    "the swept R_[t th t th] is not the substrate's constant plus +M/r^3"
print("    Each is the substrate's OWN constant plus a term carrying M and nothing else; the")
print("    substrate's part is the SAME at both critical points, so the entire difference between")
print("    them is the M/r^3 term.")
print("    ** SCOPE: an identity between these two frame components in these coordinates.  It is")
print("    NOT a general decomposition of the swept curvature into substrate and cut -- that is")
print("    the operator paper's object, not this receipt's. **")

print("(6) THE CUT'S SIDE -- P3 prop:curvature, confirmed and not quoted")
KG = sp.simplify(-sp.diff(f_sds, r)/(2*r))
print(f"    K_G = -f'/2r = {KG}")
assert is_zero(KG - (1/al**2 - M/r**3)), "K_G is not 1/alpha^2 - M/r^3"
assert is_zero(KG.subs(M, 0) - 1/al**2), "the M-term is not identically absent at M=0"
KGh = sp.simplify(KG.subs(r, 2*M))
print(f"    K_G(r=2M) = {KGh}   [finite]        K_G(r->0) = {sp.limit(KG, r, 0, '+')}")
assert KGh.is_finite is not False, "K_G is not finite at the horizon critical point"
assert sp.limit(KG, r, 0, '+') in (-sp.oo, sp.zoo), "K_G does not diverge at the pivot"

print("(7) CONTROL -- the same machinery DOES see the discriminant where it is known to be")
assert not is_zero(sp.diff(Ts['Rtrtr'], r)), \
    "CONTROL FAILED: the machinery reports no position dependence on the swept chart either, so " \
    "its silence on the substrate measures the machinery and not the substrate"
print(f"    d/dr of the swept R_[t r t r] = {sp.simplify(sp.diff(Ts['Rtrtr'], r))}  (non-zero)")
lim_tr = sp.limit(Ts['Rtrtr'], al, sp.oo)
lim_ta = sp.limit(Ts['Rtata'], al, sp.oo)
print(f"    alpha -> oo reproduces r7463 exactly: {lim_tr}, {lim_ta}")
assert is_zero(lim_tr + 2*M/r**3) and is_zero(lim_ta - M/r**3), \
    "the Schwarzschild limit does not reproduce r7463's -2M/r^3 and +M/r^3"

print("(8) CONTROL -- a non-maximally-symmetric metric, and the WEYL MACHINERY VALIDATED")
schw = curvature(sp.diag(-(1 - 2*M/r), 1/(1 - 2*M/r), r**2, r**2*sp.sin(th)**2), [t, r, th, ph])
Kschw, Wschw = sp.simplify(schw['K']), weyl_square(schw)
print(f"    Schwarzschild: Kretschmann = {Kschw}    Weyl^2 = {sp.simplify(Wschw)}")
assert is_zero(Kschw - 48*M**2/r**6), "the comparator does not see position dependence where it is"
assert is_zero(Wschw - 48*M**2/r**6), \
    "CONTROL FAILED: Weyl^2 != Kretschmann on a Ricci-flat metric, so a sign error in the Weyl " \
    "decomposition could have passed as a vanishing Weyl on the substrate"

print()
print("ALL CHECKS PASS -- the substrate does not display the tidal discriminant; the whole of it")
print("is the M/r^3 term, and the controls show the instrument can return the other answer.")
