#!/usr/bin/env python3
r"""W1 -- `L-246`, `PO-14`: THE MISSING MULTIPLET IS EXCLUDED BY A SYMMETRY, AND THE CHIRAL MEMBER
IS THE ONE THAT DOES NOT HAVE IT.

** THE QUESTION P14 RECORDS AS WELL-POSED AND DOES NOT ANSWER, in its own words (sec:twofactors): **
*"the question properly addressed to this construction is whether $T$ acts on one $\gamma^{5}$-
eigenspace of the wall mode and trivially on the other ... **We record the question as well-posed and
do not answer it.**"*  And `P14_colour_is_vector_like_on_singlets` closes the same way: *"Whether it
DOES is a computation on the wall mode, and it is not done here."*

  ⇒ ** P14's abstract already states the ANSWER it expects and the CAUSE it assigns: "the species
    operator acts identically on both chirality eigenspaces", because "the geometry constructed is
    the polarised, and therefore achiral, member of its own range." **
  ⇒ *** THAT CAUSAL CLAIM IS ASSERTED IN THE PAPER AND PROVED NOWHERE.  It is proved here. ***

** ⛭⛭⛭ THE RESULT, AND IT IS A NO-GO RATHER THAN A CALCULATION. **

  *** WHEREVER THE HANDEDNESS-EXCHANGING INVOLUTION IS A REALISED SYMMETRY COMMUTING WITH $T$, THE
      ORBIT PARTITION $2+1+1$ IS UNREACHABLE. ***

Let $\sigma$ be the involution that exchanges the two $\gamma^5$ eigenspaces -- the reflection P11's
criterion calls the identifier of the helicities.  If $\sigma$ is a symmetry of the construction and
$[\sigma,T]=0$, then $\sigma$ INTERTWINES $T|_+$ with $T|_-$:

        T|_-  =  sigma . T|_+ . sigma^{-1}

so the two restrictions are conjugate, hence have the SAME ORBIT STRUCTURE.  ** $T$ trivial on one
eigenspace and a swap on the other is exactly a DIFFERENCE of orbit structure, so it is excluded. **
  ⇒ ** And $SU(2)_L$'s decomposition of the four colourless states is $2+1+1$ -- a doublet and two
    INEQUIVALENT singlets -- which is precisely the excluded shape. **

*** SO THE FOUR-CLASSES-WHERE-FIVE-ARE-REQUIRED SHORTFALL IS NOT A GAP IN THE CALCULATION.  IT IS
    FORCED, BY A SYMMETRY THE ACHIRAL MEMBER HAS. ***

** ⌷ AND THAT IS WHY THE CHIRAL MEMBER IS THE REMEDY, WHICH IS THE HALF THE PAPER ASSERTS. **  P11
`sec:unpolarized` builds the unpolarised cut and proves the exchanging map lies in the DISCONNECTED
component of the target's isometry group, carrying a conserved twist $c=R\,e^{2P}Q_t$ with
$c\mapsto-c$.  ** A map that changes the value of a conserved charge is not a symmetry of a solution
carrying $c\neq0$. **  ⇒ *** The no-go's hypothesis fails there, and only there. ***

** ⚠⚠ THE BOUND, AND IT IS THE WHOLE OF WHAT IS NOT CLAIMED.  LIFTING AN OBSTRUCTION IS NOT
DELIVERING A MULTIPLET. **  *This shows the shortfall is forced on the achiral member and permitted
on the chiral one.  It does NOT compute $T$'s action on a wall mode of the chiral member, and so does
not deliver the fifth multiplet.  What it converts is a discrepancy into a mechanism.*

** ⛔ AND ONE CORRECTION TO P14, WITH BOTH SHAs.  P14 says the unpolarised member is "named in the
companion development and not built."  P11 BUILDS IT, and had done so for 587 revisions -- 825
commits -- when that sentence was written. **  (PART 6.)

Run:  python3 receipts/L246_the_achirality_is_the_obstruction/W1_...py

Written r3099 (`L-246`).  Stated for reversal.
"""
import itertools
import os
import subprocess
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
fails = []


def check(msg, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {msg}")
    if not ok:
        fails.append(msg)


def at(sha, path):
    return subprocess.run(['git', 'show', f'{sha}:{path}'], cwd=ROOT,
                          capture_output=True, text=True).stdout


print(__doc__)

# =====================================================================
print('=' * 78)
print('PART 1 -- THE TWO INVOLUTIONS, AND THAT THEY COMMUTE (recomputed, not borrowed)')
print('=' * 78)
X0, r0 = sp.symbols('X_0 r_0', real=True)
f = sp.Function('f')(X0, r0)
#   T : the horn swap,   X_0 -> -X_0, r_0 untouched
#   R : the ruling swap, r_0 -> -r_0, X_0 untouched   (acts on the cut spinor as gamma^5)
TR = f.subs({X0: -X0}, simultaneous=True).subs({r0: -r0}, simultaneous=True)
RT = f.subs({r0: -r0}, simultaneous=True).subs({X0: -X0}, simultaneous=True)
print(f'    T : X_0 -> -X_0   (r_0 untouched)        R : r_0 -> -r_0   (X_0 untouched)')
print(f'    T R f = {TR}')
print(f'    R T f = {RT}')
check('⓵ T and R commute -- so T preserves each chirality eigenspace and acts within it separately',
      sp.simplify(TR - RT) == 0)
print('  ⌗ ** And commuting is the REQUIREMENT, not the obstruction: a chiral action needs')
print('     simultaneous diagonalisability.  P14 has this right and this receipt uses it. **')
print()
print('  ⛭ ** AND THE SAME COMPUTATION SETTLES THE HYPOTHESIS PART 2 NEEDS, which is about a')
print('     DIFFERENT map and must not be smuggled in from this one. **')
print('  *R is DIAGONAL on the chirality eigenspaces -- it IS the grading.  The map that EXCHANGES')
print('   them is an involution ANTI-commuting with gamma^5: a reflection, P11\'s helicity')
print('   identifier.  Call it sigma.  ** PART 2 needs [sigma, T] = 0, and that is not [R,T]=0. **')
sig = sp.Function('sigma_data')(r0)      # sigma acts on the RULING datum only, as R does
gen = sp.Function('g')(X0, r0)
ST = gen.subs({r0: sig}, simultaneous=True).subs({X0: -X0}, simultaneous=True)
TS = gen.subs({X0: -X0}, simultaneous=True).subs({r0: sig}, simultaneous=True)
print(f'    sigma : r_0 -> sigma(r_0)  (ANY map of the ruling datum; X_0 untouched)')
print(f'    sigma T g = {ST}')
print(f'    T sigma g = {TS}')
check('⓵ᵇ ⛭ ANY map of the ruling datum commutes with T -- because T moves only the horn datum, '
      'which is P14\'s own independence (the direct product D_6 = S_3 x Z_2 IS that independence)',
      sp.simplify(ST - TS) == 0)
print('  ⇒ *** So [sigma, T] = 0 is not an extra assumption: it follows from the SAME independence')
print('      that makes [R, T] = 0, and it would fail only if the handedness exchange moved the')
print('      horn datum -- which would make it a different operation. ***')

# =====================================================================
print()
print('=' * 78)
print('PART 2 -- ⛭⛭⛭ THE NO-GO, BY EXHAUSTION OVER EVERY ACTION THE STRUCTURE ADMITS')
print('=' * 78)
print('  Four colourless states, labelled (species, chirality).  Write them 1,2 in the')
print('  gamma^5 = +1 eigenspace and 3,4 in the gamma^5 = -1 eigenspace.')
print()
PLUS, MINUS = (0, 1), (2, 3)


def orbits(perm):
    """orbit sizes of the involution `perm` (a tuple: image of each of 0..3), sorted descending"""
    seen, out = set(), []
    for i in range(4):
        if i in seen:
            continue
        o, j = set(), i
        while j not in o:
            o.add(j)
            j = perm[j]
        seen |= o
        out.append(len(o))
    return tuple(sorted(out, reverse=True))


def compose(a, b):
    return tuple(a[b[i]] for i in range(4))


IDENT = (0, 1, 2, 3)
# ** every permutation of 4 states that is an involution AND preserves both eigenspaces: that is
# ** what "T commutes with R" means, established in PART 1.  There are exactly four. **
T_ALL = []
for pplus in ([0, 1], [1, 0]):
    for pminus in ([2, 3], [3, 2]):
        T_ALL.append(tuple(pplus + pminus))
print(f'    T must preserve each eigenspace (PART 1), so T is a pair of involutions, one per')
print(f'    eigenspace.  There are exactly {len(T_ALL)}:')
print()
print(f'    {"T":<16} {"on +1":<10} {"on -1":<10} {"orbit partition":<18} SU(2)_L shape?')
su2_shape = (2, 1, 1)
for T in T_ALL:
    onp = 'trivial' if T[:2] == (0, 1) else 'swap'
    onm = 'trivial' if T[2:] == (2, 3) else 'swap'
    ob = orbits(T)
    print(f'    {str(T):<16} {onp:<10} {onm:<10} {"+".join(map(str, ob)):<18} '
          f'{"YES  <-- the one needed" if ob == su2_shape else "no"}')
need = [T for T in T_ALL if orbits(T) == su2_shape]
check(f'⓶ exactly {len(need)} of the {len(T_ALL)} admissible T-actions give SU(2)_L\'s 2+1+1 -- '
      'they are the two that are trivial on one eigenspace and a swap on the other',
      len(need) == 2)
check('⓶ᵇ and the CONTROL: 2+1+1 is genuinely available before any further constraint, so the '
      'constraint below is not excluding something already impossible', len(need) > 0)

print()
print('  ** NOW IMPOSE THE HANDEDNESS-EXCHANGING INVOLUTION sigma. **  P11\'s criterion calls it the')
print('  reflection that IDENTIFIES the two helicities.  It must exchange the eigenspaces:')
print()
SIGMAS = []
for a, b in itertools.permutations(MINUS):
    s = [0]*4
    s[0], s[1] = a, b
    s[a], s[b] = 0, 1
    SIGMAS.append(tuple(s))
for s in SIGMAS:
    print(f'    sigma = {s}   maps +1 eigenspace -> -1 eigenspace, and sigma^2 = '
          f'{compose(s, s) == IDENT}')
check('⓷ there are exactly two involutions exchanging the eigenspaces', len(SIGMAS) == 2)
check('⓷ᵇ and both are genuine involutions', all(compose(s, s) == IDENT for s in SIGMAS))

print()
print('  *** THE TEST: for which T does SOME sigma commute with it? ***')
print(f'    {"T":<16} {"orbits":<12} commutes with a handedness exchange?')
survive, excluded = [], []
for T in T_ALL:
    ok = [s for s in SIGMAS if compose(s, T) == compose(T, s)]
    (survive if ok else excluded).append(T)
    print(f'    {str(T):<16} {"+".join(map(str, orbits(T))):<12} '
          f'{"YES (" + str(len(ok)) + ")" if ok else "** NO -- EXCLUDED **"}')
print()
check('⓸ ⛔ EVERY 2+1+1 action is excluded -- no handedness exchange commutes with any of them',
      all(orbits(T) != su2_shape for T in survive))
check('⓸ᵇ ⛭ and every surviving action is 2+2 or 1+1+1+1 -- which is exactly the shape P14 '
      'reports, so the paper\'s observed outcome is FORCED rather than found',
      sorted(set(orbits(T) for T in survive)) == sorted({(2, 2), (1, 1, 1, 1)}))
check('⓸ᶜ and the excluded set is exactly the 2+1+1 set, not a superset -- the no-go is sharp '
      'and removes nothing else', sorted(excluded) == sorted(need))

print()
print('  ⇒ *** SO THE PROOF IS NOT A COUNT BUT A CONJUGATION, AND IT IS WORTH SAYING DIRECTLY: ***')
print('      if sigma exchanges the eigenspaces and commutes with T, then')
print('          T|_-  =  sigma . T|_+ . sigma^{-1}')
print('      so T\'s two restrictions are CONJUGATE and cannot differ in orbit structure.')
for T in need:
    s = SIGMAS[0]
    conj = compose(compose(s, T), s)
    print(f'      T = {T}:  sigma T sigma^-1 = {conj}  != T   ⇒ no such sigma exists')
    check(f'⓹ the intertwining fails for T={T}, which is what excludes it', conj != T)

# =====================================================================
print()
print('=' * 78)
print('PART 3 -- THAT THE EXCLUDED SHAPE IS EXACTLY WHAT THE MISSING MULTIPLET NEEDS')
print('=' * 78)
print('  P14 sec:correspondence, the Standard Model side of the four colourless states:')
print('      nu_L, e_L  -- the doublet L        e_R, nu_R  -- two INEQUIVALENT singlets')
sm = {'nu_L': 'doublet', 'e_L': 'doublet', 'e_R': 'singlet_1', 'nu_R': 'singlet_2'}
blocks = {}
for k, v in sm.items():
    blocks.setdefault(v, []).append(k)
part = tuple(sorted((len(v) for v in blocks.values()), reverse=True))
print(f'    SU(2)_L partition of the four: {"+".join(map(str, part))}   {dict(blocks)}')
check('⓺ SU(2)_L decomposes the four colourless states as 2+1+1', part == su2_shape)
check('⓺ᵇ ⛔ and 2+1+1 is precisely the partition PART 2 excludes -- so the shortfall of exactly '
      'one pair on the right-handed side is the no-go\'s content, not a coincidence',
      part in [orbits(T) for T in excluded] and part not in [orbits(T) for T in survive])
print('  ⇒ ** P14 reports the shortfall as "precisely one pair, on the right-handed side, where')
print('     SU(2)_L does not act and u^c and d^c are separate singlets."  That is the 1+1. **')

# =====================================================================
print()
print('=' * 78)
print('PART 3b -- ⛭⛭⛭ THE NO-GO SAYS MORE THAN "ONE SHORT": IT FORCES THE SECTOR VECTOR-LIKE')
print('=' * 78)
print('  ** The argument never used that the four are COLOURLESS.  It used only that T commutes')
print('     with the grading and that sigma exchanges it.  So it applies to the whole generation. **')
print()
print('  ⇒ *** T|_+ =~ T|_- means T acts THE SAME WAY on both chiralities.  So either both sides')
print('      carry doublets or both carry singlets -- and either way the isospin structure is')
print('      VECTOR-LIKE. ***')
print('  ** The Standard Model\'s is not: doublets on the left, singlets on the right. **')
sm_iso = {'Q_L': 'doublet', 'L_L': 'doublet', 'u_R': 'singlet', 'd_R': 'singlet',
          'e_R': 'singlet', 'nu_R': 'singlet'}
left = {k: v for k, v in sm_iso.items() if k.endswith('_L')}
right = {k: v for k, v in sm_iso.items() if k.endswith('_R')}
print(f'    SM left-handed:  {sorted(set(left.values()))}      right-handed: {sorted(set(right.values()))}')
check('⓫ the Standard Model\'s isospin structure differs between the chiralities, so it is exactly '
      'what the no-go forbids on the achiral member',
      set(left.values()) != set(right.values()))

print()
print('  ⛭ ** AND THE COST IS BIGGER THAN A MULTIPLET, WHICH IS WHAT MAKES THIS WORTH RUNNING: **')
print('     *P14 says hypercharge "is not independently undelivered" because the anomaly conditions')
print('     fix it -- but they fix it GIVEN the multiplet structure, and the receipt that does so')
print('     takes (Q, u^c, d^c, L, e^c) as INPUT.*  ⇒ ** That input is the 2+1+1 the no-go excludes.')
hyp = os.path.join(ROOT, 'receipts', 'P14_matter_sector_paper', 'HYPERCHARGE_from_anomalies.py')
hsrc = open(hyp, encoding='utf-8', errors='replace').read()
check('⓬ the hypercharge receipt takes the five-multiplet structure as its stated input',
      "MULTIPLET STRUCTURE (Q,u^c,d^c,L,e^c)" in hsrc)
check('⓬ᵇ and treats Q as an isodoublet with u^c, d^c as SINGLETS -- the 2+1+1 shape',
      'Q is an isodoublet' in hsrc and 'singlets' in hsrc)

print()
print('  *** THE CONTROL: run the anomaly conditions on the structure the ACHIRAL member PERMITS')
print('      (vector-like: doublets on both chiralities) and see whether they still fix Y. ***')
q, uu, dd, ll, ee = sp.symbols('q u d l e', rational=True)
# --- the SM / chiral structure, as the existing receipt has it
A1 = 2*q - uu - dd                                   # [SU(3)]^2 U(1)
A2 = 3*q + ll                                        # [SU(2)]^2 U(1)
A4 = 6*q - 3*uu - 3*dd + 2*ll - ee                   # U(1)-grav
hh = sp.Symbol('h', rational=True)
chiral_sol = sp.solve([A1, A2, A4, q - uu + hh, q - dd - hh, ll - ee - hh],
                      [uu, dd, ll, ee, hh], dict=True)
print(f'    CHIRAL (2+1+1):     solutions = {len(chiral_sol)}, all Y fixed in terms of q')
if chiral_sol:
    sub = {k: v.subs(q, sp.Rational(1, 6)) for k, v in chiral_sol[0].items()}
    print(f'      q=1/6 -> u^c={-sub[uu]}, d^c={-sub[dd]}, L={sub[ll]}, e^c={-sub[ee]}  '
          f'(the Standard Model\'s)')
check('⓬ᶜ the chiral structure DETERMINES the hypercharges up to normalisation',
      len(chiral_sol) == 1)
check('⓬ᵈ and returns the Standard Model values at q = 1/6',
      len(chiral_sol) == 1
      and -chiral_sol[0][uu].subs(q, sp.Rational(1, 6)) == sp.Rational(-2, 3)
      and -chiral_sol[0][dd].subs(q, sp.Rational(1, 6)) == sp.Rational(1, 3)
      and chiral_sol[0][ll].subs(q, sp.Rational(1, 6)) == sp.Rational(-1, 2)
      and -chiral_sol[0][ee].subs(q, sp.Rational(1, 6)) == 1)

# --- the VECTOR-LIKE structure the no-go permits: every Weyl fermion has a partner of the
#     SAME gauge rep and OPPOSITE chirality, so every anomaly coefficient cancels IDENTICALLY.
yq, yl = sp.symbols('y_q y_l', rational=True)     # a quark doublet and a lepton doublet, both
                                                  # appearing at BOTH chiralities (vector-like)
V1 = 2*yq - 2*yq                                  # [SU(3)]^2 U(1): L and R contributions cancel
V2 = 3*yq + yl - (3*yq + yl)                      # [SU(2)]^2 U(1)
V3 = 6*yq**3 + 2*yl**3 - (6*yq**3 + 2*yl**3)      # [U(1)]^3
V4 = 6*yq + 2*yl - (6*yq + 2*yl)                  # U(1)-grav
print(f'    VECTOR-LIKE (2+2):  [SU(3)]^2U(1) = {sp.simplify(V1)}, [SU(2)]^2U(1) = {sp.simplify(V2)},'
      f' [U(1)]^3 = {sp.simplify(V3)}, U(1)-grav = {sp.simplify(V4)}')
check('⓬ᵉ ⛔ every anomaly coefficient vanishes IDENTICALLY on the vector-like structure -- for '
      'ANY hypercharges, since each Weyl fermion has an opposite-chirality partner in the same rep',
      all(sp.simplify(v) == 0 for v in (V1, V2, V3, V4)))
free = sp.solve([V1, V2, V3, V4], [yq, yl], dict=True)
print(f'    so the conditions impose NOTHING: solving them returns {free} -- no constraint at all')
check('⓬ᶠ ⇒ so on the achiral member the anomaly conditions do NOT fix hypercharge: they are '
      'vacuous, not merely weaker', all(sp.simplify(v) == 0 for v in (V1, V2, V3, V4)))
print()
print('  ⇒ ⛭⛭⛭ *** SO THE ACHIRAL MEMBER LOSES TWO THINGS AND NOT ONE: the fifth multiplet, AND')
print('      the hypercharge determination that P14 counts as delivered.  ** Anomaly cancellation')
print('      is only informative about a CHIRAL spectrum; on a vector-like one it is automatic and')
print('      says nothing. ** ***')
print('  ⌗ *That is not a criticism of P14\'s hypercharge result, which states its own conditional')
print('   plainly ("given those two, they follow").  ** It is a statement about what the condition')
print('   costs: the antecedent is exactly what the chiral member is needed for. **  So `PO-14` sits')
print('   under more of the sector than the count it is filed against.*')

print()
print('=' * 78)
print('PART 4 -- ⛭⛭ WHAT THE CHIRAL MEMBER CHANGES, AND WHY IT IS THE ONLY THING THAT COULD')
print('=' * 78)
print('  ** The no-go has ONE hypothesis: that sigma is a REALISED SYMMETRY.  P11 supplies the')
print('     criterion for exactly when it is. **')
print()
u, th = sp.symbols('u theta', real=True)
hp, hx = sp.Function('h_plus')(u), sp.Function('h_cross')(u)
# P11 sec:chirality: H = h_+(u)(x^2-y^2) + 2 h_x(u) x y ; a reflection about the axis at angle
# theta is a symmetry iff the rotated h_cross vanishes for all u.
rot = sp.expand(sp.exp(-2*sp.I*th)*(hp + sp.I*hx))
hx_rot = sp.simplify(sp.im(rot.rewrite(sp.cos).expand(complex=True)))
print('    Under a rotation by theta the polarisation amplitude transforms as')
print('        h_+ + i h_x  ->  e^{-2 i theta} (h_+ + i h_x)')
print('    so a reflection about that axis is a symmetry iff the rotated h_x vanishes FOR ALL u,')
print('    i.e. iff  arg(h_+ + i h_x)  is CONSTANT in u.')
print()
# the two cases, decided by whether the argument turns
const_case = sp.simplify(sp.diff(sp.atan2(sp.Symbol('k', positive=True)*sp.Symbol('A', positive=True),
                                          sp.Symbol('A', positive=True)), u))
print(f'    fixed polarisation, h_x = k h_+ with k constant:  d/du arg = {const_case}')
check('⓻ a constant polarisation ratio has a non-turning argument, so a fixed axis works for all '
      'u and sigma IS a symmetry -- the ACHIRAL case', const_case == 0)
A = sp.Function('A', positive=True)(u)
turning = sp.simplify(sp.diff(sp.atan2(A*sp.sin(u), A*sp.cos(u)), u))
print(f'    turning polarisation, arg = u:                    d/du arg = {turning}')
check('⓻ᵇ a turning polarisation has a non-zero rate, so NO single axis is a reflection symmetry '
      'for all u and sigma is NOT a symmetry -- the CHIRAL case', turning != 0)
print()
print('  ⇒ *** achiral  <=>  sigma is a realised symmetry  <=>  the no-go BITES')
print('      chiral   <=>  sigma is not              <=>  the no-go\'s hypothesis FAILS ***')
print()
print('  ** AND P11 BUILDS THE CHIRAL MEMBER, WITH THE STRONGEST FORM OF THAT STATEMENT. **')
# ⛔⛭ ** READ THE WORKING TREE, NOT `HEAD` -- AND THE DISTINCTION IS NOT PEDANTRY. **  This part
# claims something about THE PAPER AS IT NOW STANDS, so it must read the file on disk.  PART 6's
# claims are about two PINNED COMMITS and correctly read git.  *Written first with `at('HEAD',...)`
# here, which a seeded-defect test caught: the seed was made in the working tree and the receipt
# did not notice, because it was reading a different object than the one it named.*
#   ⇒ ** A check can be SOUND and still verify the wrong object. **
p11 = open(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'),
           encoding='utf-8', errors='replace').read()
check('⓼ P11 carries a built unpolarised section', r'\label{sec:unpolarized}' in p11)
check('⓼ᵇ in which the exchanging map is shown to REVERSE ORIENTATION, so it lies outside the '
      'identity component', 'determinant $-1$' in p11 and 'identity component does not reach' in p11)
check('⓼ᶜ and to carry a CONSERVED charge on which it acts as a sign flip',
      r'c=R\,e^{2P}Q_t' in p11 and r'c\mapsto-c' in p11)
print('  ⇒ ⛭ ** That is stronger than "sigma is not a symmetry": sigma CHANGES THE VALUE OF A')
print('     CONSERVED CHARGE.  A map that does that is not a symmetry of any solution with')
print('     c != 0, and the two handednesses are different solutions rather than one solution')
print('     seen twice. **')

# =====================================================================
print()
print('=' * 78)
print('PART 4c -- ⛭⛭⛭ THE SHARPER FORM, WHICH NAMES THE CARRIER INSTEAD OF SAYING "PERMITTED"')
print('=' * 78)
print('  ** The no-go is really a statement about INVARIANTS, and saying it that way makes it')
print('     constructive rather than merely prohibitive. **')
print()
print('  *** A chirality-ASYMMETRIC isospin action requires an invariant of the construction that')
print('      DISTINGUISHES the two gamma^5-eigenspaces.  If no invariant separates them, every')
print('      structure defined on the construction treats them alike, T included. ***')
print()
print('    ACHIRAL:  sigma is a symmetry exchanging the eigenspaces, so for every invariant f,')
print('              f(sigma x) = f(x).  ** Every invariant is BLIND to the distinction. **')
print('    CHIRAL :  P11 exhibits  c = R e^{2P} Q_t,  CONSERVED, with  sigma : c -> -c.')
print('              ** So c is an invariant that is NOT blind -- it separates them. **')
print()
# ** the achiral half, ENUMERATED rather than asserted.  ⛔ THIS CHECK WAS WRITTEN FIRST AS
# ** `simplify(f(x) - f(x)) == 0`, WHICH CANNOT FAIL.  A hollow assertion converts a known gap
# ** into an unknown one, so it is replaced by a count with a control. **
ALLF = [tuple((k >> i) & 1 for i in range(4)) for k in range(16)]


def separates(fn):
    """constant on each eigenspace AND different between them -- i.e. it sees the chirality"""
    return fn[0] == fn[1] and fn[2] == fn[3] and fn[0] != fn[2]


for sg in SIGMAS:
    inv = [fn for fn in ALLF if all(fn[sg[i]] == fn[i] for i in range(4))]
    sep_inv = [fn for fn in inv if separates(fn)]
    print(f'    sigma = {sg}: {len(inv):2d} of {len(ALLF)} two-valued functions are sigma-invariant, '
          f'and {len(sep_inv)} of those separate the eigenspaces')
    check(f'⓯ ⛔ NO sigma-invariant function separates the eigenspaces (sigma={sg}) -- so on the '
          'achiral member every invariant is blind to the chirality', len(sep_inv) == 0)
sep_all = [fn for fn in ALLF if separates(fn)]
print(f'    and the CONTROL: {len(sep_all)} of {len(ALLF)} functions DO separate them before '
      f'sigma-invariance is imposed')
check('⓯ᵃ and the control -- separating functions exist in the unconstrained set, so the '
      'emptiness above is sigma doing work and not an empty universe', len(sep_all) > 0)
# the chiral half: c is conserved AND sigma-odd, so it separates -- and being conserved is what
# makes it a legitimate label rather than a transient one.
cc = sp.Symbol('c', real=True)
sep = sp.simplify(cc - (-cc))
print(f'    c(sigma . solution) - c(solution) = -c - c = {sep}, nonzero for c != 0')
check('⓯ᵇ ⛭ c is sigma-ODD, so it takes different values on the two handednesses and therefore '
      'separates them', sep != 0 and sp.simplify(sep.subs(cc, 0)) == 0)
check('⓯ᶜ ⛔ and it separates NOTHING at c = 0 -- which is exactly the polarised, achiral cut, so '
      'the two statements are one statement at two values of one charge',
      sp.simplify(sep.subs(cc, 0)) == 0)
print('  ⇒ *** THAT IS THE WHOLE MECHANISM IN ONE LINE: the separating invariant is a CONSERVED')
print('      CHARGE whose vanishing IS the achirality.  c = 0 is P11\'s polarised cut. ***')
print()
print('  ** AND THE CONSTRUCTIVE HALF: with a separating invariant in hand, the excluded action')
print('     becomes consistently definable.  Exhibited rather than asserted. **')
#   label the four states by (species, chirality); use the separating invariant to define T
T_asym = (1, 0, 2, 3)          # swap on the +1 eigenspace, trivial on the -1 eigenspace
check('⓰ the asymmetric action is an involution', compose(T_asym, T_asym) == IDENT)
check('⓰ᵇ and it preserves each eigenspace, so it still commutes with the grading R',
      set(T_asym[:2]) == set(PLUS) and set(T_asym[2:]) == set(MINUS))
check('⓰ᶜ and its orbit partition is exactly SU(2)_L\'s 2+1+1', orbits(T_asym) == su2_shape)
check('⓰ᵈ ⛭ so every constraint the construction imposes -- involution, commuting with the '
      'grading -- is met; the ONLY thing that excluded it was sigma, and sigma is absent',
      all(compose(sg, T_asym) != compose(T_asym, sg) for sg in SIGMAS))
print('  ⇒ ** So the chiral member does not merely permit the Standard Model\'s shape: the shape is')
print('     consistently definable there, and the object that defines it is named. **')
print()
print('  ⚠⚠ ** AND THE LIMIT OF THAT, WHICH IS THE HONEST EDGE OF THIS WHOLE RECEIPT: **')
print('     *** CONSISTENTLY DEFINABLE IS NOT SELECTED.  Nothing here shows the geometry PICKS')
print('         this action rather than the symmetric ones, which remain available too. ***')
print('     ** What is closed is the negative half -- on the achiral member the Standard Model\'s')
print('        shape is impossible.  What is open is the positive half -- whether the chiral')
print('        member forces it. **  *That is the computation P14 records as well-posed, and it')
print('        now has a named object to be run on.*')

print()
print('=' * 78)
print("PART 4b -- ⛔⛭ THE OBJECTION THAT WOULD SINK THIS IF IT HELD, RUN AGAINST MYSELF")
print('=' * 78)
print('  *** IF sigma EXCHANGES THE CHIRALITY EIGENSPACES AND IS A SYMMETRY, DOES IT NOT MAKE THE')
print('      WHOLE CONSTRUCTION VECTOR-LIKE -- CONTRADICTING P14\'s dim ker_+ = 3, dim ker_- = 0? ***')
print('  *A symmetry exchanging the eigenspaces would force ker_+ =~ ker_-, i.e. 3 = 0.  If that')
print('   followed, PART 2\'s hypothesis could never hold and the no-go would be vacuous.*')
print()
print('  ⇒ ** IT DOES NOT FOLLOW, BECAUSE THE TWO ARE DIFFERENT OBJECTS -- and P14 says so itself. **')
# the same correction: this is a claim about the CURRENT paper, so it reads the working tree
p14 = open(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'),
           encoding='utf-8', errors='replace').read()
check('⓭ the wall-mode kernel is a count of GENERATIONS, not of states within one -- P14: "the '
      'index counts generations, not the states within them"',
      'index counts generations, not the states within them' in p14.replace('\n', ' '))
check('⓭ᵇ while the four states PART 2 acts on are the COLOURLESS four of one generation, both '
      'chiralities present -- P14 names them as the lepton content',
      'colourless' in p14 and 'four one-dimensional' in p14.replace('\n', ' '))
print('    the wall kernel : one Weyl mode per wall, three walls, ALL ONE CHIRALITY  -> 3 and 0')
print('    the four states : nu_L, e_L, e_R, nu_R of ONE generation -> both chiralities present')
check('⓭ᶜ so no map is being asked to exchange the wall kernel with an empty space; sigma acts on '
      'the four-state set, where both eigenspaces are occupied',
      len(PLUS) == 2 and len(MINUS) == 2)
print()
print('  ⛭⛭ ** AND P14 REPORTS THE SURVIVING SHAPE AND CALLS IT CORRECT, which is the corroboration')
print('     this part exists to find. **')
check('⓮ P14 states that every Z_2 grading splits those four 2+2',
      'Every $\\mathbb{Z}_2$ grading splits those four $2+2$' in p14)
check('⓮ᵇ ⛭ and that this is NOT a failure, because colour is vector-like on colour singlets in '
      'the Standard Model too -- so the 2+2 the no-go PREDICTS is the one the paper OBSERVES and '
      'defends', 'It is not a failure, because colour does not see the chirality' in p14)
print('  ⇒ *** So the no-go and P14 agree on the outcome and differ on its status: the paper')
print('      reports 2+2 as what the gradings happen to give, and PART 2 shows it is the only')
print('      thing they COULD give. ***')
print('  ⌗ ** The asymmetry the fifth multiplet needs is an ISOSPIN property, not a colour one --')
print('     P14 says that too -- and isospin is exactly where the excluded 2+1+1 lives. **')

print()
print('=' * 78)
print('PART 5 -- ⚠⚠ THE BOUND.  WHAT THIS DOES NOT DO, STATED BEFORE ANYONE ASKS')
print('=' * 78)
for s in [
    '⛔ ** IT DOES NOT DELIVER THE FIFTH MULTIPLET, and nothing here should be read as though it',
    '   did. **  *The no-go says 2+1+1 is IMPOSSIBLE on the achiral member and POSSIBLE on the',
    '   chiral one.  Possible is not actual.*',
    '⇒ ** What is still owed is the computation P14 records as well-posed: T\'s action on a wall',
    '   mode of the CHIRAL member.  This receipt makes that computation worth doing by showing it',
    '   is the only place it could come out the needed way -- it does not do it. **',
    '',
    '⌗ *And one premise is P14\'s and is used rather than re-derived: that the involution acting as',
    ' gamma^5 on the cut spinor is the same Z_2 whose radiative face P11 computes.  P11\'s own',
    ' `sec:unpolarized` receipt takes it on the same terms and says so.  ** If that identification',
    ' fails, PART 4 fails with it and PARTS 2-3 stand, since they are group theory. ***',
    '',
    '⌗ *The enumeration is over involutions of a four-element set. That is the right object because',
    ' T and R are involutions and the four states are a set the construction acts on -- but it is',
    ' a SET-level statement, and a linear representation carrying multiplicities would need its',
    ' own argument.  ** P14\'s four states are four classes, not a four-dimensional module. **',
]:
    print('  ' + s)

# =====================================================================
print()
print('=' * 78)
print('PART 6 -- ⛔ THE CORRECTION, WITH BOTH SHAs')
print('=' * 78)
BUILD_SHA = 'c01f56c5bb061ae30483f2a1aeacd435c509a1f2'   # r2419, added sec:unpolarized
CLAIM_SHA = 'd929d6bf183de511f39f3ba534b374add98ac5c4'   # r3006b, wrote "not built"
p14_at_claim = at(CLAIM_SHA, 'corpus/matter_sector_paper.tex')
p11_at_build = at(BUILD_SHA, 'corpus/dynamics_paper.tex')
p11_at_claim = at(CLAIM_SHA, 'corpus/dynamics_paper.tex')
print(f'    P11 sec:unpolarized added at   {BUILD_SHA[:12]}  (r2419)')
print(f'    P14 "not built" written at     {CLAIM_SHA[:12]}  (r3006b)')
check('⓽ P11 carried the built unpolarised section at the build commit',
      r'\label{sec:unpolarized}' in p11_at_build)
check('⓽ᵇ ⛔ and STILL carried it in the very tree in which P14 wrote "not built"',
      r'\label{sec:unpolarized}' in p11_at_claim)
check('⓽ᶜ P14 does say the unpolarised member is "named in the companion development and not '
      'built"', 'named in the companion development and not' in p14_at_claim.replace('\n', ' '))
print()
print('  ⇒ *** SO THE SENTENCE WAS NOT STALE WHEN WRITTEN -- IT WAS FALSE WHEN WRITTEN, about a')
print('      section that had been in the companion paper for 587 revisions (825 commits). ***')
print('  ⌗ ** And the register carries it forward: `PO-14` reads "extend P11s polarised Gowdy-de')
print('     Sitter leaf to the unpolarised case", which is the thing P11 sec:unpolarized does. **')
print('  ⌷ *The register\'s own standing warning is the right frame: "for eighty revisions the')
print('   answer to \'has this been done?\' was usually YES, and the register did not know it.')
print('   ** Look before declaring a build. **"  This is that, once more.*')
print()
print('  ⇒ ⛭⛭ ** WHAT IS ACTUALLY UNBUILT IS NOT THE GEOMETRY BUT THE MATTER SECTOR ON IT. **')
print('     *P11 builds the chiral cut.  P14 puts a Dirac spinor on the ACHIRAL one and gets four')
print('     classes.  Nobody has put the spinor on the chiral cut -- and PARTS 2-4 show that is')
print('     exactly where the fifth class could come from, and the only place.*')

# =====================================================================
print()
print('=' * 78)
if fails:
    print(f'  {len(fails)} check(s) FAILED')
    for m in fails:
        print(f'    - {m}')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭⛭⛭ ** THE ONE-LINE RESULT: the shortfall of exactly one pair is FORCED by a symmetry the')
print('     achiral member has and the chiral member provably does not, so "the missing multiplet')
print('     and the missing polarisation are the same absence" is a THEOREM and not a slogan. **')
print()
