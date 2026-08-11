import sympy as sp

# ======================================================================
# F1 — completing the MODE-LEVEL so(5,1) bracket table at the symmetric cut.
#
# Step 4 (f1_mode_level_closure.py) verified [m,m] subset h at the mode level:
#   {H_perp[X_a], H_perp[X_b]} -> H_a[xi_ab],  xi_ab a Killing vector = M_ab.
# This script does the two REMAINING bracket types, in the SAME construction:
#   [h,m] subset m :  {H_a[xi_ab], H_perp[X_c]} = H_perp[L_{xi_ab} X_c]
#                     =?= H_perp[ delta_bc X_a - delta_ac X_b ]   (closes into m)
#   [h,h] subset h :  {H_a[xi_ab], H_a[xi_cd]} = H_a[[xi_ab,xi_cd]_Lie]
#                     =?= H_a[ d_bc xi_ad - d_ac xi_bd - d_bd xi_ac + d_ad xi_bc ]
# Falsifiable: any bracket could fail to close, or close with the wrong constant.
# Construction is step 4's verbatim: dS4 static-patch S^3 spatial leaf, X_a the
# de Sitter embedding coords, the standard smeared HDA brackets.
# ======================================================================

rho, th, ph, al = sp.symbols('rho theta phi alpha', positive=True)
f = 1 - rho**2/al**2
g = sp.diag(1/f, rho**2, rho**2*sp.sin(th)**2)          # leaf 3-metric (rho,theta,phi)
hinv = g.inv()                                          # h^{ab}
coords = [rho, th, ph]

# coset-lapse modes N_a = X_a | leaf  (t=0, X5=0)
X = {1: rho*sp.sin(th)*sp.cos(ph),
     2: rho*sp.sin(th)*sp.sin(ph),
     3: rho*sp.cos(th),
     4: sp.sqrt(al**2 - rho**2)}

def d(expr, i): return sp.diff(expr, coords[i])

def hda_xi(Na, Nb):
    # {H_perp[Na],H_perp[Nb]} -> xi^c = h^{cd}(Na d_d Nb - Nb d_d Na)
    return [sp.simplify(sum(hinv[c,e]*(Na*d(Nb,e) - Nb*d(Na,e)) for e in range(3)))
            for c in range(3)]

def Lie_g(xi):
    # (L_xi g)_{ab}, to confirm xi is Killing (re-verify step 4's [m,m])
    L = sp.zeros(3,3)
    for a in range(3):
        for b in range(3):
            t  = sum(xi[c]*d(g[a,b],c) for c in range(3))
            t += sum(g[c,b]*d(xi[c],a) for c in range(3))
            t += sum(g[a,c]*d(xi[c],b) for c in range(3))
            L[a,b] = sp.simplify(t)
    return L

def lie_drag_scalar(xi, S):       # L_xi S = xi^d d_d S   (acting on a lapse mode)
    return sp.simplify(sum(xi[c]*d(S,c) for c in range(3)))

def lie_bracket_vec(u, v):        # [u,v]^k = u^d d_d v^k - v^d d_d u^k
    return [sp.simplify(sum(u[e]*d(v[k],e) - v[e]*d(u[k],e) for e in range(3)))
            for k in range(3)]

# antisymmetric xi_{ab} := HDA{X_a, X_b}; xi_{ba} = -xi_{ab}; xi_{aa}=0
_cache = {}
def XI(a, b):
    if a == b: return [sp.Integer(0)]*3
    if (a,b) in _cache: return _cache[(a,b)]
    if (b,a) in _cache: return [sp.simplify(-x) for x in _cache[(b,a)]]
    v = hda_xi(X[a], X[b]); _cache[(a,b)] = v; return v

idx = [1,2,3,4]
def delta(i,j): return 1 if i==j else 0

print("="*78)
print("[m,m] re-verify (step 4): xi_ab := HDA{X_a,X_b} is Killing for all a<b in 1..4")
print("="*78)
mm_ok = True
for a in idx:
    for b in idx:
        if a < b:
            L = Lie_g(XI(a,b))
            ok = (L == sp.zeros(3,3))
            mm_ok &= ok
            print(f"   xi_{a}{b}: Killing? {'YES' if ok else 'NO  '+str(L)}")
print("  [m,m] all Killing:", mm_ok)

print("\n" + "="*78)
print("[h,m] subset m :  L_{xi_ab} X_c  =?=  delta_bc X_a - delta_ac X_b")
print("="*78)
hm_ok = True
for a in idx:
    for b in idx:
        if a < b:
            for c in idx:
                lhs = lie_drag_scalar(XI(a,b), X[c])
                rhs = delta(b,c)*X[a] - delta(a,c)*X[b]
                ok = sp.simplify(lhs - rhs) == 0
                hm_ok &= ok
                tag = "" if ok else "   <-- MISMATCH"
                if (not ok) or (lhs != 0):
                    print(f"   [xi_{a}{b}, X_{c}] -> {sp.simplify(lhs)}   expect {sp.simplify(rhs)}   {'ok' if ok else 'FAIL'}{tag}")
print("  [h,m] closes into m term-for-term:", hm_ok)

print("\n" + "="*78)
print("[h,h] subset h :  [xi_ab, xi_cd]_Lie =?= d_bc xi_ad - d_ac xi_bd - d_bd xi_ac + d_ad xi_bc")
print("="*78)
hh_ok = True
pairs = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
for (a,b) in pairs:
    for (c,dd) in pairs:
        lhs = lie_bracket_vec(XI(a,b), XI(c,dd))
        rhs = [delta(b,c)*XI(a,dd)[k] - delta(a,c)*XI(b,dd)[k]
               - delta(b,dd)*XI(a,c)[k] + delta(a,dd)*XI(b,c)[k] for k in range(3)]
        diff = [sp.simplify(lhs[k]-rhs[k]) for k in range(3)]
        ok = all(x == 0 for x in diff)
        hh_ok &= ok
        if not ok:
            print(f"   [xi_{a}{b}, xi_{c}{dd}] FAIL: lhs={lhs} rhs={rhs}")
print("  [h,h] closes into h term-for-term (so(4) structure constants):", hh_ok)

print("\n" + "="*78)
print("VERDICT")
print("="*78)
print("  [m,m] (step 4, re-verified):", "PASS" if mm_ok else "FAIL")
print("  [h,m] -> m term-for-term   :", "PASS" if hm_ok else "FAIL")
print("  [h,h] -> h term-for-term   :", "PASS" if hh_ok else "FAIL")
print("  Full finite so(5,1)|spatial-leaf realized as a CLOSED subalgebra")
print("  inside the smeared HDA at the symmetric cut:", "YES" if (mm_ok and hm_ok and hh_ok) else "NO")
