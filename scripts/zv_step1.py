import sympy as sp

# Zipoy-Voorhees (gamma-)metric in prolate spheroidal coords (x,y), Weyl static axisymmetric.
# Schwarzschild = delta=1.  k = length scale (set 1; irrelevant to Petrov type).
t,x,y,ph = sp.symbols('t x y phi', real=True)
d = sp.symbols('delta', positive=True)   # delta (=gamma)
k = 1

# H = k^2 ((x+1)/(x-1))^delta
H = ( (x+1)/(x-1) )**d
gtt = -( (x-1)/(x+1) )**d
gxx = H*(x**2-1)**(d**2-1)*(x**2-y**2)**(1-d**2)
gyy = H*(x**2-1)**(d**2)*(x**2-y**2)**(1-d**2)/(1-y**2)
gpp = H*(x**2-1)*(1-y**2)

coords=[t,x,y,ph]
g = sp.diag(gtt,gxx,gyy,gpp)

def ricci_scalar_and_tensor(g,coords,dval):
    g = g.subs(d,dval)
    gi = g.inv()
    n=4
    # Christoffel
    Gamma=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s=0
                for e in range(n):
                    s+=gi[a,e]*(sp.diff(g[e,b],coords[c])+sp.diff(g[e,c],coords[b])-sp.diff(g[b,c],coords[e]))
                Gamma[a][b][c]=sp.simplify(s/2)
    # Ricci R_{bc}=R^a_{bac}
    Ric=sp.zeros(n,n)
    for b in range(n):
        for c in range(n):
            s=0
            for a in range(n):
                s+=sp.diff(Gamma[a][b][c],coords[a])-sp.diff(Gamma[a][b][a],coords[c])
                for e in range(n):
                    s+=Gamma[a][a][e]*Gamma[e][b][c]-Gamma[a][c][e]*Gamma[e][b][a]
            Ric[b,c]=sp.simplify(s)
    return Ric, Gamma, gi

# Vacuum check at delta=1 (Schwarzschild sanity) and delta=2 (genuine ZV)
for dval in [1, 2]:
    Ric,_,_=ricci_scalar_and_tensor(g,coords,sp.Integer(dval))
    maxabs=sp.simplify(sum(sp.Abs(Ric[i,j]) for i in range(4) for j in range(4)))
    print(f"delta={dval}: sum|Ricci_ij| =", maxabs)
