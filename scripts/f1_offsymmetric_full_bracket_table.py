import sympy as sp

# ======================================================================
# F1 — the OFF-symmetric (vacuum-M) MODE-level bracket table: the [h,m] and
# [h,h] companion to r270 (which closed the full table AT M=0) and to steps 5-6
# (which leaked only [m,m] off M=0). Completes the per-stratum grading for the
# WHOLE table: at the symmetric cut the so(5)-spatial subalgebra closes (r270);
# off it the SO(3) rotations are retained and every broken-generator bracket
# leaks = the algebroid connection (driven by d_M f = -2/rho, vanishing at M=0).
#
# Falsifiable: an SO(3) bracket could unexpectedly leak (break the retained
# subalgebra), or an X4-bracket could stay closed (break the uniform connection).
# Construction = step 5's verbatim (SdS leaf, dS harmonics X_a, xi:=HDA{X_a,X_b}).
# ======================================================================

rho, th, ph, al, M = sp.symbols('rho theta phi alpha M', positive=True)
f = 1 - 2*M/rho - rho**2/al**2                          # SdS leaf, vacuum straight cut
g = sp.diag(1/f, rho**2, rho**2*sp.sin(th)**2)
hinv = g.inv()
coords = [rho, th, ph]
X = {1: rho*sp.sin(th)*sp.cos(ph), 2: rho*sp.sin(th)*sp.sin(ph),
     3: rho*sp.cos(th),           4: sp.sqrt(al**2 - rho**2)}

def d(e,i): return sp.diff(e, coords[i])
def hda(a,b):                                            # xi_ab^c = h^cd(X_a d_d X_b - X_b d_d X_a)
    Na, Nb = X[a], X[b]
    return [sp.simplify(sum(hinv[c,e]*(Na*d(Nb,e)-Nb*d(Na,e)) for e in range(3))) for c in range(3)]
_C={}
def XI(a,b):
    if a==b: return [sp.Integer(0)]*3
    if (a,b) in _C: return _C[(a,b)]
    if (b,a) in _C: return [sp.simplify(-x) for x in _C[(b,a)]]
    v=hda(a,b); _C[(a,b)]=v; return v
def dr(i,j): return 1 if i==j else 0
def Ldrag(xi,S): return sp.simplify(sum(xi[c]*d(S,c) for c in range(3)))           # L_xi (scalar)
def Lbr(u,v): return [sp.simplify(sum(u[e]*d(v[k],e)-v[e]*d(u[k],e) for e in range(3))) for k in range(3)]

def vanishes_at_M0(expr): return sp.simplify(sp.sympify(expr).subs(M,0))==0

print("="*78); print("[h,m] OFF-symmetric:  L_{xi_ab} X_c  vs  delta_bc X_a - delta_ac X_b"); print("="*78)
hm_retained_ok=True; hm_leak_seen=False; hm_leak_vanishes_M0=True
cases_hm=[ (1,2,1,"SO(3)"),(1,2,3,"SO(3)"),(1,3,1,"SO(3)"),     # SO(3) rotations among X1,X2,X3
           (1,4,1,"broken"),(1,4,4,"broken"),(2,4,2,"broken") ] # X4-involving (broken dS-translations)
for a,b,c,kind in cases_hm:
    lhs=Ldrag(XI(a,b),X[c]); rhs=dr(b,c)*X[a]-dr(a,c)*X[b]
    dev=sp.simplify(lhs-rhs)
    if kind=="SO(3)":
        ok=(dev==0); hm_retained_ok&=ok
        print(f"  [xi_{a}{b},X_{c}] {kind}: deviation = {dev}  -> {'CLOSED all M' if ok else 'LEAKS (unexpected!)'}")
    else:
        leaks=(dev!=0); v0=vanishes_at_M0(dev); hm_leak_seen|=leaks; hm_leak_vanishes_M0&=v0
        print(f"  [xi_{a}{b},X_{c}] {kind}: deviation = {sp.simplify(dev)}")
        print(f"        leaks(M!=0)={leaks} ; deviation|_(M=0)=0 ? {v0}")

print("\n"+"="*78); print("[h,h] OFF-symmetric:  [xi_ab,xi_cd]  vs  so(4) structure-constant combo of xi's"); print("="*78)
hh_retained_ok=True; hh_leak_seen=False; hh_leak_vanishes_M0=True
def so4combo(a,b,c,dd,k):
    return (dr(b,c)*XI(a,dd)[k]-dr(a,c)*XI(b,dd)[k]-dr(b,dd)*XI(a,c)[k]+dr(a,dd)*XI(b,c)[k])
cases_hh=[ ((1,2),(1,3),"SO(3)"),((1,2),(2,3),"SO(3)"),         # so(3) closes
           ((1,4),(1,2),"broken"),((1,4),(2,4),"broken") ]      # X4-involving leak
for (a,b),(c,dd),kind in cases_hh:
    lhs=Lbr(XI(a,b),XI(c,dd)); dev=[sp.simplify(lhs[k]-so4combo(a,b,c,dd,k)) for k in range(3)]
    if kind=="SO(3)":
        ok=all(x==0 for x in dev); hh_retained_ok&=ok
        print(f"  [xi_{a}{b},xi_{c}{dd}] {kind}: deviation = {dev} -> {'CLOSED all M' if ok else 'LEAKS (unexpected!)'}")
    else:
        leaks=any(x!=0 for x in dev); v0=all(vanishes_at_M0(x) for x in dev)
        hh_leak_seen|=leaks; hh_leak_vanishes_M0&=v0
        print(f"  [xi_{a}{b},xi_{c}{dd}] {kind}: leaks(M!=0)={leaks} ; deviation|_(M=0)=0 ? {v0}")

print("\n"+"="*78); print("the connection driving the leak"); print("="*78)
print("  d_M(h^rr)=d_M f =", sp.simplify(sp.diff(f,M)), " (= -2/rho, the structure-function connection, steps 1-3)")

print("\n"+"="*78); print("VERDICT (off-symmetric full bracket table)"); print("="*78)
print("  [h,m] SO(3) retained exactly (all M):", hm_retained_ok)
print("  [h,m] broken generators leak, leak->0 at M=0:", hm_leak_seen and hm_leak_vanishes_M0)
print("  [h,h] SO(3) closes exactly (all M):", hh_retained_ok)
print("  [h,h] broken generators leak, leak->0 at M=0:", hh_leak_seen and hh_leak_vanishes_M0)
allok = hm_retained_ok and hm_leak_seen and hm_leak_vanishes_M0 and hh_retained_ok and hh_leak_seen and hh_leak_vanishes_M0
print("  Full table off M=0: SO(3) retained subalgebra + connection-leak elsewhere,"
      " uniform across [m,m],[h,m],[h,h]:", "YES" if allok else "NO")
