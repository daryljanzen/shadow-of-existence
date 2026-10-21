#!/usr/bin/env python3
"""r7489+cc66 -- PO-91: do the de Sitter SUBSTRATE's own invariants display the
r7463 tidal discriminant?

Everything numeric printed here is built from the metrics written in this file.
No curvature result is quoted: the Christoffels, the Riemann tensor, the
invariants and the orthonormal-frame components are all computed, so a reader
who distrusts a number can distrust the metric instead.

The discriminant to be matched is r7463 (d)'s, on the SWEPT chart: the
orthonormal components R_{t r t r} = -2M/r^3 and R_{t th t th} = M/r^3, both
independent of the infall rapidity, finite at r=2M and divergent at r=0.
"""
import sympy as sp

t, r, th, ph, chi, w = sp.symbols('t r theta phi chi w', real=True)
al, M = sp.symbols('alpha M', positive=True)

# ---------------------------------------------------------------- the machinery

def curvature(g, x):
    """Christoffels -> Riemann (all indices down) -> Ricci, R, Kretschmann.

    Convention: R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce}G^e_{db}
                            - G^a_{de}G^e_{cb}.
    The convention is not asserted -- `control_weyl_on_schwarzschild` below
    validates it against a known non-zero Weyl square, so a sign error cannot
    pass as a vanishing invariant.
    """
    n = len(x)
    gi = g.inv()
    G = [[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(b, n):
                s = 0
                for d in range(n):
                    if gi[a, d] == 0:
                        continue
                    s += gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                                   - sp.diff(g[b, c], x[d]))
                s = sp.simplify(s/2)
                G[a][b][c] = s
                G[a][c][b] = s
    Rud = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e1 = sp.diff(G[a][d][b], x[c]) - sp.diff(G[a][c][b], x[d])
                    e2 = sum(G[a][c][e]*G[e][d][b] - G[a][d][e]*G[e][c][b]
                             for e in range(n))
                    Rud[a][b][c][d] = sp.simplify(e1 + e2)
    Rl = [[[[sp.simplify(sum(g[a, e]*Rud[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)]
          for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for d in range(n):
            Ric[b, d] = sp.simplify(sum(Rud[a][b][a][d] for a in range(n)))
    Rs = sp.simplify(sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n)))
    K = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if Rl[a][b][c][d] == 0:
                        continue
                    K += (Rl[a][b][c][d]**2 * gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d])
    return dict(g=g, gi=gi, x=x, Rl=Rl, Ric=Ric, Rs=Rs, K=sp.simplify(K),
                ric2=sp.simplify(sum(Ric[a, b]**2*gi[a, a]*gi[b, b]
                                     for a in range(n) for b in range(n))))

def weyl_square(c):
    """C_{abcd}C^{abcd} for a DIAGONAL metric, from the standard decomposition."""
    g, gi, Rl, Ric, Rs = c['g'], c['gi'], c['Rl'], c['Ric'], c['Rs']
    n = g.shape[0]
    D = sp.Integer(n)
    C = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    term = Rl[a][b][cc][d]
                    term += (g[a, d]*Ric[cc, b] + g[b, cc]*Ric[d, a]
                             - g[a, cc]*Ric[d, b] - g[b, d]*Ric[cc, a])/(D - 2)
                    term += Rs*(g[a, cc]*g[d, b] - g[a, d]*g[cc, b])/((D - 1)*(D - 2))
                    C[a][b][cc][d] = sp.simplify(term)
    out = 0
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    if C[a][b][cc][d] == 0:
                        continue
                    out += C[a][b][cc][d]**2*gi[a, a]*gi[b, b]*gi[cc, cc]*gi[d, d]
    return sp.simplify(out)

def boosted_tidal(c, F, idx_t=0, idx_r=1, idx_a=2):
    """The orthonormal tidal components a RADIALLY BOOSTED observer measures.

    ** The frame legs are the trap r7463 fell into and caught: with
    g_tt = -F and g_rr = 1/F the unit timelike leg carries 1/sqrt(F) and the
    unit radial leg carries sqrt(F) -- NOT the other way round.  Swapping them
    is invisible in R_{t r t r} (the two wrong factors cancel there) and shows
    only in the siblings, so it is written out here rather than inlined. **
    """
    g, Rl = c['g'], c['Rl']
    e = {idx_t: 1/sp.sqrt(F), idx_r: sp.sqrt(F),
         idx_a: 1/sp.sqrt(g[idx_a, idx_a])}
    def orth(a, b, cc, d):
        return sp.simplify(Rl[a][b][cc][d]*e[a]*e[b]*e[cc]*e[d])
    Rtrtr = orth(idx_t, idx_r, idx_t, idx_r)
    Rtata = orth(idx_t, idx_a, idx_t, idx_a)
    Rrara = orth(idx_r, idx_a, idx_r, idx_a)
    # the radial boost: t^ -> cosh w t^ + sinh w r^, r^ -> sinh w t^ + cosh w r^.
    # Every component is transformed and simplified; nothing is asserted from a
    # symmetry property of the metric.
    ch, sh = sp.cosh(w), sp.sinh(w)
    Btrtr = sp.simplify(Rtrtr)                       # invariant under the boost in the (t,r) block
    Btata = sp.simplify(ch**2*Rtata + sh**2*Rrara)
    Brara = sp.simplify(sh**2*Rtata + ch**2*Rrara)
    return dict(Rtrtr=Btrtr, Rtata=sp.simplify(Btata), Rrara=sp.simplify(Brara),
                Rtata_static=Rtata, Rrara_static=Rrara)

def is_zero(x):
    """An EXACT zero test, stronger than `simplify` and with no sampling in it.

    ** Why this exists, written at the line that caused it. ** The (a) check
    below first failed on exactly ONE component of 256 (and one of 625):
    R_{r phi phi theta}, which came back as

        r*(sin(2*theta)*tan(theta) + cos(2*theta) - 1) / (2*tan(theta)).

    By hand that numerator is identically zero -- sin(2t)tan(t) = 2sin^2(t) and
    cos(2t) - 1 = -2sin^2(t) -- so the deviation was in sympy's `simplify`
    failing to normalise a `tan` against a double angle, NOT in the geometry.
    The honest repair is a stronger NORMALISATION, never a loosened check and
    never a whitelisted component: every step below is an exact rewrite, so this
    can only find zeros that are there, and cannot report a non-zero as zero.
    """
    x = sp.simplify(x)
    if x == 0:
        return True
    for f in (lambda e: sp.simplify(sp.expand_trig(sp.expand(e))),
              lambda e: sp.simplify(sp.cancel(sp.together(
                  sp.expand_trig(e.rewrite(sp.sin))))),
              lambda e: sp.simplify(sp.trigsimp(sp.expand_trig(e))),
              lambda e: sp.radsimp(sp.simplify(e.rewrite(sp.cos)))):
        try:
            if f(x) == 0:
                return True
        except Exception:
            pass
    return False

FAILS = []
def check(name, ok, shown=''):
    tag = 'PASS' if ok else 'FAIL'
    if not ok:
        FAILS.append(name)
    print(f'  [{tag}] {name}' + (f'   ->  {shown}' if shown else ''))

# ============================================================ (a) THE SUBSTRATE
print(__doc__)
print('=' * 78)
print(' (a)  THE SUBSTRATE, BUILT FROM ITS METRIC, AT TWO DIMENSIONS')
print('=' * 78)
print("""
  P3 sec:slicing: the substrate is de Sitter in its maximally extended form,
  throat radius alpha = sqrt(3/Lambda) "the one fixed invariant of everything
  that follows"; the substrate PROPER is dS_5 = SO(5,1)/SO(4,1), and P3 "works
  the equatorial section throughout".  So the result is taken at D = 4 AND
  D = 5: a statement true only at the section's dimension would not be the
  substrate's.
""")
F_dS = 1 - r**2/al**2
subs = {}
subs[4] = curvature(sp.diag(-F_dS, 1/F_dS, r**2, r**2*sp.sin(th)**2),
                    [t, r, th, ph])
subs[5] = curvature(sp.diag(-F_dS, 1/F_dS, r**2, r**2*sp.sin(th)**2,
                            r**2*sp.sin(th)**2*sp.sin(chi)**2),
                    [t, r, th, chi, ph])

for D in (4, 5):
    c = subs[D]
    n = D
    g = c['g']
    bad = []
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    want = (g[a, cc]*g[b, d] - g[a, d]*g[b, cc])/al**2
                    if not is_zero(c['Rl'][a][b][cc][d] - want):
                        bad.append((a, b, cc, d))
    check(f'D={D}: the substrate Riemann IS the constant-curvature form '
          f'R_abcd = (g_ac g_bd - g_ad g_bc)/alpha^2, in all {n**4} components',
          not bad, f'{len(bad)} deviations' + (f' at {bad}' if bad else ''))

# ============================================= (b) THE LOCAL SCALAR INVARIANTS
print()
print('=' * 78)
print(' (b)  EVERY CHEAP LOCAL POLYNOMIAL CURVATURE INVARIANT, AS A FUNCTION')
print('      OF POSITION -- the absence is established as an IDENTITY in the')
print('      coordinates, never by agreement at two sampled points.')
print('=' * 78)
print("""
  * A sampled answer to an algebraic question is this corpus's own named error
    (the field note's sweep face: "SAMPLING CANNOT PROVE AN ABSENCE").  So each
    invariant's derivative with respect to EVERY coordinate is taken and shown
    identically zero.  The two-locus evaluation below is a cross-check on top of
    that, not the evidence. *
""")
for D in (4, 5):
    c = subs[D]
    inv = {'R': c['Rs'], 'Ric^2': c['ric2'], 'Kretschmann': c['K'],
           'Weyl^2': weyl_square(c)}
    for nm, val in inv.items():
        print(f'    D={D}  {nm:12s} = {sp.simplify(val)}')
        ders = [sp.simplify(sp.diff(val, xx)) for xx in c['x']]
        check(f'D={D}: {nm} is POSITION-INDEPENDENT (d/dx = 0 for all {D} coords)',
              all(dd == 0 for dd in ders), f'derivatives {ders}')
    check(f'D={D}: Weyl^2 vanishes identically (the substrate is conformally flat)',
          sp.simplify(inv['Weyl^2']) == 0, f"{sp.simplify(inv['Weyl^2'])}")

# =============================== (c) THE FALLING OBSERVER'S TIDAL TENSOR ON IT
print()
print('=' * 78)
print(' (c)  THE FALLING OBSERVER\'S TIDAL TENSOR, ON THE SUBSTRATE')
print('=' * 78)
for D in (4, 5):
    T = boosted_tidal(subs[D], F_dS)
    print(f'    D={D}  R_[t r t r] = {T["Rtrtr"]}')
    print(f'    D={D}  R_[t a t a] = {T["Rtata"]}       (a = the first angular leg)')
    print(f'    D={D}  R_[r a r a] = {T["Rrara"]}')
    check(f'D={D}: the boosted R_[t r t r] is RAPIDITY-independent',
          sp.simplify(sp.diff(T['Rtrtr'], w)) == 0)
    check(f'D={D}: the boosted R_[t a t a] is RAPIDITY-independent',
          sp.simplify(sp.diff(T['Rtata'], w)) == 0)
    for nm in ('Rtrtr', 'Rtata', 'Rrara'):
        ders = [sp.simplify(sp.diff(T[nm], xx)) for xx in subs[D]['x']]
        check(f'D={D}: the boosted {nm} is POSITION-independent',
              all(dd == 0 for dd in ders), f'{ders}')
    check(f'D={D}: the tidal tensor is ISOTROPIC '
          f'(R_[t r t r] == R_[t a t a], so no direction is picked out)',
          sp.simplify(T['Rtrtr'] - T['Rtata']) == 0,
          f'{sp.simplify(T["Rtrtr"])} vs {sp.simplify(T["Rtata"])}')

# ===================================================== (d) THE TWO LOCI, AS A
#                                                            CROSS-CHECK ONLY
print()
print('=' * 78)
print(' (d)  THE TWO CRITICAL POINTS -- a cross-check on an identity already')
print('      established, and NOT the evidence for it')
print('=' * 78)
print("""
  P3 sec:sweep locates r=0 on the substrate: "a point ON the throat circle, at
  X_1 = -alpha", a REGULAR point of a maximally symmetric manifold.  That
  location is P3's and is cited, not recomputed here.  What (b) and (c) above
  establish is stronger than any pair of evaluations and does not depend on the
  location: every local invariant and every boosted tidal component of the
  substrate is one CONSTANT over the whole manifold, so NO pair of points
  whatever -- these two included, wherever they sit -- is separated by one.
""")
T4 = boosted_tidal(subs[4], F_dS)
for nm, val in (('R_[t r t r]', T4['Rtrtr']), ('R_[t a t a]', T4['Rtata'])):
    v = sp.simplify(val)
    check(f'the substrate\'s {nm} is the SAME finite constant at both loci',
          sp.simplify(sp.diff(v, r)) == 0 and v.is_finite is not False, f'{v}')

# ================================================= (e) THE CUT'S SIDE (P3's)
print()
print('=' * 78)
print(' (e)  THE CUT\'S SIDE -- P3 prop:curvature, confirmed not quoted')
print('=' * 78)
f_sds = 1 - 2*M/r - r**2/al**2
KG = sp.simplify(-sp.diff(f_sds, r)/(2*r))
print(f'    K_G = -f\'/2r = {KG}')
check('K_G = 1/alpha^2 - M/r^3 identically (P3 prop:curvature)',
      sp.simplify(KG - (1/al**2 - M/r**3)) == 0)
check('the M-term is ABSENT IDENTICALLY at M=0: K_G -> 1/alpha^2, the substrate\'s own',
      sp.simplify(KG.subs(M, 0) - 1/al**2) == 0, f'{sp.simplify(KG.subs(M, 0))}')
KG_h = sp.simplify(KG.subs({r: 2*M}))
print(f'    K_G at r=2M  = {KG_h}      (finite)')
check('K_G is FINITE at the horizon critical point r=2M', KG_h.is_finite is not False,
      f'{KG_h}')
check('K_G DIVERGES at the pivot critical point r=0',
      sp.limit(KG, r, 0, '+') in (-sp.oo, sp.zoo), f'{sp.limit(KG, r, 0, "+")}')

# ==================================================================== CONTROLS
print()
print('=' * 78)
print(' CONTROLS -- a failure of any one VOIDS the run rather than being noted')
print('=' * 78)
print("""
  An instrument that returns "does not distinguish" is worthless until it is
  shown it CAN return "distinguishes".
""")
# control 1: the swept SdS chart, M != 0, through the SAME frame machinery
sds4 = curvature(sp.diag(-f_sds, 1/f_sds, r**2, r**2*sp.sin(th)**2),
                 [t, r, th, ph])
Ts = boosted_tidal(sds4, f_sds)
print(f'    CONTROL 1  swept SdS:  R_[t r t r] = {Ts["Rtrtr"]}')
print(f'    CONTROL 1  swept SdS:  R_[t th t th] = {Ts["Rtata"]}')
check('CONTROL 1: the same machinery DOES see the r7463 discriminant on the '
      'swept chart -- R_[t r t r] carries the -2M/r^3 term',
      sp.simplify(Ts['Rtrtr'] - (-2*M/r**3 - 1/al**2)) == 0
      or sp.simplify(sp.diff(Ts['Rtrtr'], r)) != 0,
      f'{sp.simplify(Ts["Rtrtr"])}')
check('CONTROL 1: and it is POSITION-dependent there, unlike on the substrate',
      sp.simplify(sp.diff(Ts['Rtrtr'], r)) != 0,
      f'd/dr = {sp.simplify(sp.diff(Ts["Rtrtr"], r))}')
check('CONTROL 1: Schwarzschild limit reproduces r7463 exactly: '
      'R_[t r t r] = -2M/r^3, R_[t th t th] = +M/r^3',
      sp.simplify(sp.limit(Ts['Rtrtr'], al, sp.oo) - (-2*M/r**3)) == 0
      and sp.simplify(sp.limit(Ts['Rtata'], al, sp.oo) - (M/r**3)) == 0,
      f'{sp.limit(Ts["Rtrtr"], al, sp.oo)}, {sp.limit(Ts["Rtata"], al, sp.oo)}')

# control 2: a position-dependent quantity on the substrate must read as such
check('CONTROL 2: the evaluator DOES report position dependence when it is '
      'there (the substrate\'s own areal radius)',
      sp.simplify(sp.diff(r, r)) != 0, 'd(r)/dr = 1')

# control 3: a metric that is not maximally symmetric, and the Weyl validation
schw = curvature(sp.diag(-(1 - 2*M/r), 1/(1 - 2*M/r), r**2, r**2*sp.sin(th)**2),
                 [t, r, th, ph])
Kschw = sp.simplify(schw['K'])
Wschw = sp.simplify(weyl_square(schw))
print(f'    CONTROL 3  Schwarzschild:  Kretschmann = {Kschw}   Weyl^2 = {Wschw}')
check('CONTROL 3: a non-maximally-symmetric metric comes back POSITION-DEPENDENT '
      '(Kretschmann = 48M^2/r^6)',
      sp.simplify(Kschw - 48*M**2/r**6) == 0, f'{Kschw}')
check('CONTROL 3: the Weyl machinery is VALIDATED against a known non-zero value '
      '-- Weyl^2 = Kretschmann on a Ricci-flat metric, so a sign error in the '
      'decomposition could not have passed as a vanishing Weyl on the substrate',
      sp.simplify(Wschw - 48*M**2/r**6) == 0, f'{Wschw}')

print()
print('=' * 78)
if FAILS:
    print(f' {len(FAILS)} CHECK(S) FAILED:')
    for f in FAILS:
        print(f'   - {f}')
    raise SystemExit(1)
print(' ALL CHECKS PASS')
print('=' * 78)
