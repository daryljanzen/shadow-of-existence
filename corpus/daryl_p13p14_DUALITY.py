"""DARYL'S P13/P14 CONJECTURE -- THE DUALITY (r1081, Daryl's call, verified).

The colouring rule has TWO readings, and they are DUAL:
    r-RULE     : purple <=> arg r    is a multiple of 90  <=>  r    is real or purely imaginary
    tau~-RULE  : purple <=> arg tau~ is a multiple of 90  <=>  tau~ is real or purely imaginary
and colour otherwise by quadrant: Q1,Q3 blue ; Q2,Q4 red.

EACH FACE IS PINNED IN ONE VARIABLE -- and is therefore ALL PURPLE under THAT variable's rule and
COLOURED under the other's:

                        r-RULE                        tau~-RULE
    face 1  r REAL      ALL PURPLE                    coloured (purple where tau~ hits an axis)
    face 3  r IMAG      ALL PURPLE                    coloured
    face 2  tau~ REAL   coloured (purple at arg r=0)   ALL PURPLE
    face 4  tau~ IMAG   coloured (purple at arg r=180) ALL PURPLE

That is the whole of the "conflict" flagged at r1080: not a contradiction, a DUALITY. A face pinned in
r cannot see r's quadrants (it has none), so it reads colour off tau~ -- and vice versa. Each face is
blind to exactly the variable it fixed. NEITHER READING IS PRIVILEGED BY ANY FACE.

*** AND THAT IS PRECISELY WHY [6*] CANNOT BE SETTLED ON A FACE. *** The object is C_r x C_tau~; a
slice that pins a variable destroys that variable's colour information by construction. Only the full
4-D object can say whether the r-rule, the tau~-rule, or their combination is the geometry's.
STATUS: A CONJECTURE. THE RHYME STAYS A RHYME until A3 works it whole.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
A = 2**(1/3)/np.sqrt(3); rmax = 2.4; EPS = 1e-9

def colour_of(z):
    """Daryl's rule on one complex plane: on an axis -> purple ; Q1,Q3 -> blue ; Q2,Q4 -> red."""
    x, y = z.real, z.imag
    if abs(x) < 1e-6 or abs(y) < 1e-6: return PURPLE          # on an axis: two-in-one
    return BLUE if x*y > 0 else RED

def seg(ax, T, R, xs, ys, zs, rule):
    """draw one branch, colouring each point by the chosen rule (r or tau~)."""
    C = [colour_of(R[i] if rule=='r' else T[i]) for i in range(len(xs))]
    for i in range(len(xs)-1):
        ax.plot(xs[i:i+2], ys[i:i+2], zs[i:i+2], color=C[i], lw=2.6)

def fmt(ax, title, xlim, ylim, zlim):
    ax.scatter([0],[0],[0], color='k', s=26, zorder=10)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_zlim(*zlim)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.view_init(elev=16, azim=-60); ax.set_box_aspect((1,1,1), zoom=1.30)
    ax.set_title(title, fontsize=9, pad=-16)

# ---- branch generators: each returns list of (T array, R array, x, y, z) ----
def face1():
    out=[]; rp=np.linspace(1e-4,rmax,240); sx=np.array([(2/3)*np.arcsinh((r/A)**1.5) for r in rp])
    rn=np.linspace(-1e-4,-rmax,300)
    def wing(r):
        u=abs(r/A)**1.5
        return (0.0,(2/3)*np.arcsin(u)) if u<=1 else ((2/3)*np.arccosh(u), np.pi/3)
    W=np.array([wing(r) for r in rn]); wx,wy=W[:,0],W[:,1]
    for ex,ey in [(+1,+1),(-1,+1),(-1,-1),(+1,-1)]:
        T=ex*wx+1j*ey*wy; R=rn+0j; out.append((T,R,ex*wx,ey*wy,rn))
    for e in (+1,-1):
        T=e*sx+0j; R=rp+0j; out.append((T,R,e*sx,0*rp,rp))
    return out, (2,-2),(1.2,-1.2),(-rmax,rmax)
def face2():
    out=[]
    for t in (np.linspace(1e-4,2.0,240), np.linspace(-2.0,-1e-4,240)):
        for k in range(3):
            R=A*np.abs(np.sinh(1.5*t))**(2/3)*np.exp(2j*np.pi*k/3); T=t+0j
            out.append((T,R,t,R.real,R.imag))
    return out, (2,-2),(1.9,-1.9),(-1.9,1.9)
def face4():
    out=[]
    for s in (np.linspace(1e-4,2*np.pi/3,300), np.linspace(-2*np.pi/3,-1e-4,300)):
        for d in (60,180,300):
            R=A*np.abs(np.sin(1.5*s))**(2/3)*np.exp(1j*np.deg2rad(d)); T=1j*s
            out.append((T,R,s,R.real,R.imag))
    return out, (2.2,-2.2),(0.95,-0.95),(-0.95,0.95)
def face3():
    out=[]
    def tau_of_y(y,sg):
        u=(abs(y)/A)**1.5; z=sg*u*np.exp(-1j*np.pi/4) if y>0 else sg*u*np.exp(+1j*np.pi/4)
        return (2/3)*np.arcsinh(z)
    for sg in (+1,-1):
        for ys in (np.linspace(1e-4,1.8,240), np.linspace(-1.8,-1e-4,240)):
            T=np.array([tau_of_y(y,sg) for y in ys]); R=1j*ys
            out.append((T,R,T.real,T.imag,ys))
    return out, (1.9,-1.9),(1.1,-1.1),(-1.9,1.9)

FACES=[('face 1 — $r$ REAL', face1), ('face 2 — $\\tilde\\tau$ REAL', face2),
       ('face 3 — $r$ IMAG', face3), ('face 4 — $\\tilde\\tau$ IMAG', face4)]
fig = plt.figure(figsize=(17.0, 9.2))
for row, rule in enumerate(['r','tau']):
    for col_i,(nm,fn) in enumerate(FACES):
        ax = fig.add_subplot(2,4,row*4+col_i+1, projection='3d')
        branches, xl, yl, zl = fn()
        for T,R,x,y,z in branches:
            T = np.atleast_1d(T)*np.ones(len(np.atleast_1d(x))); R = np.atleast_1d(R)*np.ones(len(np.atleast_1d(x)))
            seg(ax, T, R, np.atleast_1d(x)*np.ones(len(T)), np.atleast_1d(y)*np.ones(len(T)), np.atleast_1d(z), rule)
        allp = ('ALL PURPLE' if ((rule=='r' and col_i in (0,2)) or (rule=='tau' and col_i in (1,3))) else '')
        fmt(ax, nm + ('\n' + allp if allp else ''), xl, yl, zl)
fig.text(0.005, 0.72, 'coloured by\nthe $r$-RULE\n\npurple $\\Leftrightarrow$\n$r$ real or\npurely imag.',
         fontsize=10.5, color='0.2', va='center')
fig.text(0.005, 0.27, 'coloured by\nthe $\\tilde\\tau$-RULE\n\npurple $\\Leftrightarrow$\n$\\tilde\\tau$ real or\npurely imag.',
         fontsize=10.5, color='0.2', va='center')
fig.suptitle("Daryl's P13/P14 conjecture — THE DUALITY: each face is ALL PURPLE under the rule of the variable it pins,\n"
             "and coloured under the other's. Not a contradiction — a duality. Neither reading is privileged by any face.",
             fontsize=13, y=0.985)
plt.tight_layout(rect=[0.055,0,1,0.93])
plt.savefig('daryl_p13p14_DUALITY.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_DUALITY.png', dpi=150, bbox_inches='tight')
print('r-RULE   : faces 1 and 3 (r pinned) -> ALL PURPLE ; faces 2,4 coloured')
print('tau~-RULE: faces 2 and 4 (tau~ pinned) -> ALL PURPLE ; faces 1,3 coloured')
print('=> DUAL. Each face is blind to exactly the variable it fixed.')
