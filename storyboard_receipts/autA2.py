# The three cube-root sheets of the bead, WITH the mass reflection R and complex conjugation,
# generate D6 = Aut(A2). States = arg(r) in units of pi/3 (mod 6). Element = (a, eps): arg -> eps*arg + a.
#   S (sheet monodromy, *e^{2pi i/3}) : a=2      [order 3, the cube-root cycle around r=0]
#   R (MASS REFLECTION r->-r, 2M->-2M, *(-1)) : a=3  [the species flip 3<->3bar; = gamma^5;
#       the OUTER Z2 of Aut(A2)=D6. NOT charge conjugation: R moves the horizon roots, Q->-Q fixes
#       them, so C adjoins an INDEPENDENT Z2, D6 -> D6 x Z2 (rem:C-not-R, P13). Corrected r1065.]
#   K (complex conjugation)          : eps=-1
def comp(g,h):
    a1,e1=g; a2,e2=h; return ((e1*a2+a1)%6, e1*e2)
gens=[('S',(2,1)),('R',(3,1)),('K',(0,-1))]
G={(0,1)}; fr=[(0,1)]
while fr:
    x=fr.pop()
    for _,g in gens:
        y=comp(g,x)
        if y not in G: G.add(y); fr.append(y)
assert len(G)==12                      # D6 = Aut(A2)
R=(3,1); assert all(comp(R,g)==comp(g,R) for _,g in gens)   # R central
S3={(0,1)}; fr=[(0,1)]                  # <S,K> = S3 (order 6)
while fr:
    x=fr.pop()
    for g in [(2,1),(0,-1)]:
        y=comp(g,x)
        if y not in S3: S3.add(y); fr.append(y)
assert len(S3)==6
print("group = D6 = Aut(A2), order", len(G), "= S3 x Z2 ;  Z2=<R>(outer, MASS reflection) ;  S3=<S,K>(sheets)")
print("6 vertices = 3 sheets {arg 0,2,4} x species {+ , R:+3} = the 6 roots of A2 (hexagon)")
