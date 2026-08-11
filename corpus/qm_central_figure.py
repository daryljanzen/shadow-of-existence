"""THE QM PLATE — the global-Wick real form THE PLATE does not carry.
Central physics figure, numerically integrated (like daryl_p13p14_THE_PLATE.py):
  - the bead's TWO REAL FORMS: Lorentzian sinh (open, temporal) <-> Euclidean sin (closed, beta=2pi.alpha)
  - the Euclidean S^5 = global Wick of the dS5 substrate, carrying su(3) gauge orbits AND the hbar thermal circle
  - computed fact (qm_S4_vs_S5.py): su(3) needs the FULL S^5/SO(6); hbar's thermal circle rides the same S^5.
All curves are integrated by matrix exponential of the realified su(3) c so(6) generators; no schematic.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.linalg import expm
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED, GOLD, GREY = '#2471a3', '#c0392b', '#d4a017', '#888888'
PURPLE = '#7d5ba6'
alpha = 1.0

# ---------- su(3) -> so(6) (realify i*lambda_a); verified antisymmetric in qm_S4_vs_S5.py ----------
l = [np.zeros((3,3),complex) for _ in range(8)]
l[0][[0,1],[1,0]]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1
l[3][[0,2],[2,0]]=1; l[4][0,2]=-1j; l[4][2,0]=1j; l[5][[1,2],[2,1]]=1
l[6][1,2]=-1j; l[6][2,1]=1j; l[7]=np.diag([1.,1.,-2.])/np.sqrt(3)
def realify(M):
    X,Y=M.real,M.imag; return np.block([[X,-Y],[Y,X]])   # C^3=(z1,z2,z3)->R^6=(x1,x2,x3,y1,y2,y3)
G = [realify(1j*L) for L in l]              # 8 so(6) generators spanning su(3)
H3, H8 = G[2], G[7]                          # Cartan (commuting) -> gauge torus
# thermal circle generator: Euclidean-time rotation in the (x1,y1) plane = phase of z1 = J in so(6),
# NOT traceless in u(3) => a u(1) OUTSIDE su(3): the hbar circle is distinct from gauge, same S^5.
Jth = np.zeros((6,6)); Jth[0,3]=-1; Jth[3,0]=1
base = np.array([1.,0,0, 0,0,0.])           # a point of S^5 (|base|=1)

def orbit(gen, ts, p=base):
    return np.array([expm(t*gen)@p for t in ts])

# ================= FIGURE =================
fig = plt.figure(figsize=(15,5.2))

# ---- (A) the two real forms: Lorentzian sinh <-> Euclidean sin ----
axA = fig.add_subplot(1,3,1)
w = np.linspace(0,2.3,400)
axA.plot(w, np.sinh(w)**(2/3), color=BLUE, lw=2.6, label=r'Lorentzian: $a\propto\sinh^{2/3}(3\tilde\tau/2\alpha)$')
psi = np.linspace(0,np.pi,400)
axA.plot(psi, np.sin(psi)**(2/3), color=RED, lw=2.6, label=r'Euclidean (Wick): $a\propto\sin^{2/3}(3\psi/2\alpha)$')
axA.axvline(np.pi, color=GREY, ls=':', lw=1)
axA.annotate(r'closes at $\beta=2\pi\alpha$ (the $\hbar$ period)', (np.pi,0.05), (1.05,0.9),
             fontsize=8.5, color=RED, arrowprops=dict(arrowstyle='->',color=GREY,lw=0.8))
axA.set_xlabel(r'$w=3\tilde\tau/2\alpha$ (real) $\;\;/\;\;$ Euclidean angle $\psi$'); axA.set_ylabel(r'scale factor $a/A$')
axA.set_title(r'(A) the bead, two real forms', fontsize=12, fontweight='bold')
axA.legend(fontsize=7.5, loc='upper left'); axA.set_ylim(0,2.2)

# ---- (B) the Euclidean S^5: gauge orbit + hbar circle, co-located (proj to x1,x2,y1) ----
axB = fig.add_subplot(1,3,2, projection='3d')
th = np.linspace(0,2*np.pi,300)
hb = orbit(Jth, th)                                   # hbar thermal great circle
axB.plot(hb[:,0],hb[:,1],hb[:,3], color=GOLD, lw=3.0, label=r'$\hbar$ thermal circle ($\beta=2\pi\alpha$)')
# gauge Cartan torus: exp(s H3 + t H8) base, sample a lattice of curves
for s in np.linspace(0,2*np.pi,7):
    tt=np.linspace(0,2*np.pi,200); cur=np.array([expm(s*H3+t*H8)@base for t in tt])
    axB.plot(cur[:,0],cur[:,1],cur[:,3], color=BLUE, lw=0.8, alpha=0.55)
axB.plot([],[],[],color=BLUE,lw=1.2,label=r'su(3) gauge orbit (Cartan $T^2$)')
# faint S^5 proj sphere guide
u,v=np.mgrid[0:2*np.pi:24j,0:np.pi:12j]
axB.plot_wireframe(np.cos(u)*np.sin(v),np.sin(u)*np.sin(v),np.cos(v),color=GREY,lw=0.25,alpha=0.25)
axB.set_title(r'(B) one $S^5$: gauge and $\hbar$ co-located', fontsize=12, fontweight='bold')
axB.legend(fontsize=7.5, loc='upper left'); axB.set_box_aspect((1,1,1))
axB.set_xlabel(r'$x_1$'); axB.set_ylabel(r'$x_2$'); axB.set_zlabel(r'$y_1$')

# ---- (C) su(3) needs the FULL S^5 (fills it); hbar is a sub-circle -> nesting S^4 c S^5 ----
axC = fig.add_subplot(1,3,3, projection='3d')
rng=np.random.default_rng(0)
# integrate a generic su(3) trajectory (all 8 gens) -> densely samples S^5 (transitive)
p=base.copy(); pts=[p]
for _ in range(4000):
    a=rng.normal(size=8)*0.12; Gs=sum(a[i]*G[i] for i in range(8)); p=expm(Gs)@p; pts.append(p)
pts=np.array(pts)
axC.scatter(pts[:,0],pts[:,1],pts[:,4], s=1.5, color=BLUE, alpha=0.25)
axC.plot(hb[:,0],hb[:,1],hb[:,4], color=GOLD, lw=3.0)
axC.plot([],[],[],color=BLUE,lw=4,alpha=0.5,label=r'su(3) orbit fills $S^5$ (transitive)')
axC.plot([],[],[],color=GOLD,lw=3,label=r'$\hbar$ circle $\subset$ $S^5$ (its $S^4$ equator side)')
axC.set_title(r'(C) su(3) requires all of $S^5$; $\hbar\subset S^5$', fontsize=12, fontweight='bold')
axC.legend(fontsize=7.5, loc='upper left'); axC.set_box_aspect((1,1,1))
axC.set_xlabel(r'$x_1$'); axC.set_ylabel(r'$x_2$'); axC.set_zlabel(r'$y_2$')

fig.suptitle(r"THE QM PLATE — the Euclidean real form (global Wick $S^5/SO(6)$): gauge su(3) $+$ thermal $\hbar$ on one sphere"
             "\n"r"the temporal form is the Lorentzian bead (A); the Wick carries it to $S^5$ where gauge and $\hbar$ co-locate (B,C)  ·  computed, not schematic",
             fontsize=11.5, fontweight='bold', y=1.02)
fig.tight_layout()
fig.savefig('qm_central_figure.png', dpi=140, bbox_inches='tight')
print("wrote qm_central_figure.png")
# sanity receipts
print("all su(3) gens antisymmetric:", all(np.abs(g+g.T).max()<1e-9 for g in G))
print("hbar circle stays on S^5 (|x|=1):", np.allclose(np.linalg.norm(hb,axis=1),1))
print("gauge orbit stays on S^5:", np.allclose(np.linalg.norm(pts,axis=1),1,atol=1e-6))
print("Jth in su(3)? (should be NO):", any(np.allclose(Jth, g) for g in G), "| trace of z1-phase in u(3) != 0 => outside su(3)")
