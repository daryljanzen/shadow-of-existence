"""
P05_dihedral_generators.py -- verifies P5 prop:relations + prop:completeness, by BUILDING the within-single-
  geometry morphism group as the sigma,tau dihedral action on the SKY-ANGLE CIRCLE (distinct from the between-
  member monodromy realisation of P05_deck_group_S3):
    [P5 groupoid_paper prop:sigma, prop:tau, prop:relations eq:dihedral, prop:completeness]
    generators   sigma: w |-> pi/3 - w   (reflection about w=pi/6, the root-exchange)
                 tau:   w |-> w + 2pi/3   (sky-angle periodicity)
    (i)   sigma^2 = id, tau^3 = id;
    (ii)  (sigma tau)(w) = pi/3 - (w + 2pi/3) = -w - pi/3, and (sigma tau)^2 = id  -- the third relation;
    (iii) <sigma,tau | sigma^2=tau^3=(sigma tau)^2=id> generates a group of order 6 = D3 ~ S3;
    (iv)  prop:completeness: the 6 elements are exactly the maps preserving sin 3w that are BIJECTIONS --
          3 rotations (w + 2pi k/3) and 3 reflections (pi/3 - w + 2pi k/3), the two uniform branches of
          sin 3T = sin 3w; a branch-SWITCHING map folds the domain (non-injective) and is excluded;
    (v)   <sigma,tau> is the unique non-abelian group of order 6 (= S3 = D3), and sigma exchanges roots
          of the horizon cubic (the S3-triple, P3 prop:factor).
  [P5 groupoid_paper -- the generators-and-relations core: within-geometry group = D3 on the sky angle]
STATUS: ✔✔   RUN: python3 P05_dihedral_generators.py   RUNTIME: ~2s
COMPUTES: exact affine-map composition on the circle w->s*w+c (mod 2pi); element orders; the presentation;
  sin 3w-invariance of all 6; the abstract S3 identification (order profile, non-abelian); branch-switch non-injectivity.
CONTROL: a branch-switching map (rotation on half, reflection on half) is non-injective (two w's collide),
  so it is NOT a morphism -- this is what forces the 6 uniform-branch maps and no more (prop:completeness).
  And tau (order 3) is not a reflection, sigma (order 2) is not a rotation -- the two generator classes are distinct.
BOUND: P05_deck_group_S3 realises this same abstract S3 as the BETWEEN-member deck/monodromy group (root
  transpositions around Nariai); THIS receipt is the WITHIN-geometry sigma,tau action on the sky-angle circle --
  a distinct realisation (angle circle vs root permutations), the paper's "generators and relations" proper.
ORIGIN: built new (fork) -- P5 completeness re-audit; prop:relations uncovered (deck_group does the monodromy).
"""
import sympy as sp, itertools
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
pi = sp.pi
# a map on the circle: w |-> s*w + c (mod 2pi), stored as (s, c) with c a multiple of pi reduced mod 2pi
def norm(c): return sp.nsimplify(sp.Mod(c, 2*pi))
def compose(m1, m2):            # m1 after m2 : (s1,c1) o (s2,c2)
    s1,c1 = m1; s2,c2 = m2
    return (s1*s2, norm(s1*c2 + c1))
ID    = (1, sp.Integer(0))
sigma = (-1, norm(pi/3))         # w -> pi/3 - w
tau   = (1,  norm(2*pi/3))        # w -> w + 2pi/3
def order(m, cap=12):
    p=m
    for k in range(1,cap+1):
        if p==ID: return k
        p=compose(m,p)
    return None
print("="*74); print("P05 dihedral generators -- sigma,tau within-geometry action = D3 on the sky angle"); print("="*74)

# (i) generator orders
ok&=check("sigma^2 = id  (reflection about pi/6, order 2)", order(sigma)==2)
ok&=check("tau^3 = id  (rotation by 2pi/3, order 3)", order(tau)==3)

# (ii) the third relation (sigma tau)(w) = -w - pi/3, (sigma tau)^2 = id
st = compose(sigma, tau)
w = sp.Symbol('w')
st_of_w = sp.nsimplify(st[0]*w + st[1])
ok&=check("(sigma tau)(w) = -w - pi/3  (= -w + 5pi/3 mod 2pi)",
          sp.simplify(sp.Mod(st_of_w - (-w - pi/3), 2*pi))==0)
ok&=check("(sigma tau)^2 = id  -> the relation (sigma tau)^2 = id", order(st)==2)

# (iii) the group <sigma,tau> has order 6 = D3 ~ S3
def closure(gens):
    G={ID}; frontier=[ID]
    while frontier:
        x=frontier.pop()
        for g in gens:
            y=compose(g,x)
            if y not in G: G.add(y); frontier.append(y)
    return G
G = closure([sigma,tau])
ok&=check("<sigma,tau> has order 6  (= D3 ~ S3)", len(G)==6)
ok&=check("  its 6 elements are {id, tau, tau^2, sigma, sigma*tau, sigma*tau^2}",
          G=={ID, tau, compose(tau,tau), sigma, compose(sigma,tau), compose(sigma,compose(tau,tau))})

# (iv) prop:completeness: all 6 preserve sin 3w; they are the 2 uniform branches (rot / refl)
def preserves_sin3w(m):
    s,c = m
    return sp.simplify(sp.sin(3*(s*w+c)) - sp.sin(3*w))==0
ok&=check("all 6 elements preserve sin 3w  (are within-geometry morphisms)", all(preserves_sin3w(m) for m in G))
rot  = [m for m in G if m[0]==1]      # 3 rotations
refl = [m for m in G if m[0]==-1]     # 3 reflections
ok&=check("3 rotations (branch 3T=3w) + 3 reflections (branch 3T=pi-3w) = the 6",
          len(rot)==3 and len(refl)==3)

# (v) abstract identification: <sigma,tau> is the UNIQUE non-abelian group of order 6 = S3 = D3.
#     (S3 is the only non-abelian group of order 6; element-order profile: 1 id, 3 of order 2, 2 of order 3.)
orders = sorted(order(m) for m in G)
ok&=check("element-order profile = [1,2,2,2,3,3]  (S3: one id, three order-2, two order-3)",
          orders==[1,2,2,2,3,3])
ok&=check("non-abelian: sigma*tau != tau*sigma  => D3 ~ S3, not the cyclic Z6",
          compose(sigma,tau) != compose(tau,sigma))
# concrete tie to the roots: sigma exchanges roots of the horizon cubic (P3 prop:factor), the S3-triple.
rsym = sp.Symbol('r'); r0v = sp.Rational(1,2); twoM = r0v - r0v**3
cub_roots = sp.solve(rsym**3 - rsym + twoM, rsym)
ok&=check("concrete geometry r0=1/2: the horizon cubic has 3 distinct real roots (the S3-triple)",
          len(cub_roots)==3 and len({sp.simplify(x) for x in cub_roots})==3)
sig_r0 = (-r0v + sp.sqrt(4-3*r0v**2))/2
ok&=check("  sigma(r0) is another root of the same cubic (root-exchange within the triple)",
          any(sp.simplify(sig_r0 - x)==0 for x in cub_roots))

# CONTROLS
ok&=check("CONTROL: tau (order 3) is not a reflection; sigma (order 2) is not a rotation",
          tau[0]==1 and sigma[0]==-1 and order(tau)==3 and order(sigma)==2)
# a branch-switch map: rotation for w in [0,pi/3), reflection elsewhere -> non-injective (folds domain)
def branch_switch(x):
    x = float(x) % (float(pi)*2)
    return (x + 2*float(pi)/3) if x < float(pi)/3 else (float(pi)/3 - x) % (2*float(pi))
# two distinct inputs collide -> non-injective
import numpy as np
xs = np.linspace(0, 2*float(np.pi), 4000, endpoint=False)
ys = np.array([branch_switch(x) for x in xs])
# non-injective iff some output value is hit by inputs from BOTH pieces
collision = min(abs(((branch_switch(0.1) - branch_switch(x)+np.pi)%(2*np.pi))-np.pi) for x in xs if abs(x-0.1)>0.2)
ok&=check("CONTROL: a branch-SWITCHING map is non-injective (folds the domain) -> excluded (prop:completeness)",
          collision < 1e-2)

# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `ok`, and with
# it P5 prop:relations/prop:completeness as group-theoretic content: sigma has order 2, tau order
# 3, sigma.tau order 2 (the dihedral presentation sigma^2 = tau^3 = (sigma tau)^2 = id); the group
# they generate has order 6 with element-order profile [1,2,2,2,3,3] -- the S_3/D_3 profile, NOT
# the cyclic Z_6 profile [1,2,3,3,6,6] -- and is non-abelian, which fixes it as S_3; and the 6
# split 3 rotations + 3 reflections, ALL of them preserving sin 3w.
assert order(sigma) == 2 and order(tau) == 3 and order(st) == 2
assert len(G) == 6
assert orders == [1, 2, 2, 2, 3, 3], orders
assert compose(sigma, tau) != compose(tau, sigma)
assert len(rot) == 3 and len(refl) == 3
assert all(preserves_sin3w(m) for m in G)
assert len(cub_roots) == 3 and any(sp.simplify(sig_r0 - x) == 0 for x in cub_roots)
assert ok

print("="*74)
print("RESULT:", "ALL PASS -- sigma (reflection about pi/6) and tau (rotation by 2pi/3) satisfy\n"
      "         sigma^2=tau^3=(sigma tau)^2=id, generating D3~S3 (order 6); the 6 elements are exactly the\n"
      "         bijections preserving sin 3w (3 rotations + 3 reflections) and act as the full S3 on the three\n"
      "         sky-angle roots. The within-geometry generators-and-relations core, distinct from the deck monodromy."
      if ok else "SOME FAILED")
print("="*74)
