"""DARYL'S P13/P14 CONJECTURE -- EVERYTHING IN ONE PLACE.
Four 3-D renderings of the one 4-D object (C_r x C_tau~), plus the ray map that relates them.

  face 1  r REAL,      tau~ complex  -> arg r = 0,180        six branches = FOUR BEADS + TWO MERGERS
  face 2  tau~ REAL,   r complex     -> arg r = 0,120,240    the three sheets (six segments)
  face 4  tau~ IMAG,   r complex     -> arg r = 60,180,300   THE LIFT: |r| <= A, periodic, closes
  face 3  r IMAG,      tau~ complex  -> arg r = 90,270       TRANSVERSE: between the rays, all purple

  ray map: faces 2+4 = the HEXAGON (A2 roots). Face 3 sits off it, on the axis-crossings.

*** THE CONFLICT, MARKED NOT HIDDEN (r1080) ***
Face 1 is coloured by the TAU~ quadrants (Q1,Q3 vs Q2,Q4). The ray map's rule says PURPLE <=> arg r a
multiple of 90 <=> r real or purely imaginary. But face 1 HAS r REAL (arg r = 0 or 180): by the ray
rule face 1 would be ENTIRELY PURPLE. It is not, as drawn. SAME RULE, TWO FACES, TWO ANSWERS.
The rule as stated -- "conjugate when you go from positive to negative, real or imaginary, r or tau~" --
is about MOTION ALONG A BEAD (a path crossing zero), while the quadrant/ray readings are about WHERE A
POINT SITS. Those are not the same thing, and on a slice where a coordinate is pinned to zero the
distinction bites. WHICH READING IS THE OBJECT'S IS EXACTLY [6*] AND IS NOT SETTLED HERE.

*** STATUS: A CONJECTURE. Not derived. Not species = sign(r). No face settles it. THE RHYME STAYS A
RHYME until A3 works the full C_r x C_tau~ object. These pictures carry the conjecture. ***
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
A = 2**(1/3)/np.sqrt(3); rmax = 2.4

def fmt(ax, xl, yl, zl, title, xlim, ylim, zlim):
    ax.scatter([0],[0],[0], color='k', s=34, zorder=10)
    ax.set_xlabel(xl, labelpad=-4, fontsize=8); ax.set_ylabel(yl, labelpad=-4, fontsize=8)
    ax.set_zlabel(zl, labelpad=-5, fontsize=8)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_zlim(*zlim)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.view_init(elev=16, azim=-60); ax.set_box_aspect((1,1,1), zoom=1.16)
    ax.set_title(title, fontsize=9.5, pad=-14)

fig = plt.figure(figsize=(17.5, 9.6))
gs = fig.add_gridspec(2, 3, width_ratios=[1,1,1.15], hspace=0.02, wspace=0.02)

# ---- FACE 1: r real, tau~ complex. six branches; tau~-quadrant colouring ----
ax = fig.add_subplot(gs[0,0], projection='3d')
rp = np.linspace(1e-4, rmax, 300); sx = np.array([(2/3)*np.arcsinh((r/A)**1.5) for r in rp])
rn = np.linspace(-1e-4, -rmax, 360)
def wing(r):
    u = abs(r/A)**1.5
    return (0.0,(2/3)*np.arcsin(u)) if u<=1 else ((2/3)*np.arccosh(u), np.pi/3)
W = np.array([wing(r) for r in rn]); wx, wy = W[:,0], W[:,1]
for ex, ey in [(+1,+1),(-1,+1),(-1,-1),(+1,-1)]:
    ax.plot(ex*wx, ey*wy, rn, color=(BLUE if ex*ey>0 else RED), lw=2.6)
for e in (+1,-1): ax.plot(e*sx, 0*rp, rp, color=PURPLE, lw=3.2)
fmt(ax, r'$\mathrm{Re}\,\tilde\tau$', r'$\mathrm{Im}\,\tilde\tau$', r'$r$',
    'face 1 — $r$ REAL, $\\tilde\\tau$ complex\n$\\arg r=0,180$ · 6 branches $=$ 4 beads $+$ 2 mergers',
    (2,-2),(1.2,-1.2),(-rmax,rmax))

# ---- FACE 2: tau~ real, r complex. three sheets; r-quadrant colouring ----
ax = fig.add_subplot(gs[0,1], projection='3d')
tp = np.linspace(1e-4,2.0,300); tn = np.linspace(-2.0,-1e-4,300)
mod2 = lambda t: A*np.abs(np.sinh(1.5*t))**(2/3)
C2 = {(1,'+'):RED,(1,'-'):BLUE,(2,'+'):BLUE,(2,'-'):RED,(0,'+'):PURPLE,(0,'-'):PURPLE}
for k in (0,1,2):
    for t,sg in ((tp,'+'),(tn,'-')):
        z = mod2(t)*np.exp(2j*np.pi*k/3); ax.plot(t, z.real, z.imag, color=C2[(k,sg)], lw=2.8)
fmt(ax, r'$\tilde\tau$', r'$\mathrm{Re}\,r$', r'$\mathrm{Im}\,r$',
    'face 2 — $\\tilde\\tau$ REAL, $r$ complex\n$\\arg r=0,120,240$ · the three sheets',
    (2,-2),(1.9,-1.9),(-1.9,1.9))

# ---- FACE 4: tau~ imaginary -> THE LIFT: bounded, periodic ----
ax = fig.add_subplot(gs[1,0], projection='3d')
sp = np.linspace(1e-4,2*np.pi/3,400); sn = np.linspace(-2*np.pi/3,-1e-4,400)
mod4 = lambda s: A*np.abs(np.sin(1.5*s))**(2/3)
for deg,(cp,cn) in {60:(BLUE,RED),180:(PURPLE,PURPLE),300:(RED,BLUE)}.items():
    for s,c in ((sp,cp),(sn,cn)):
        z = mod4(s)*np.exp(1j*np.deg2rad(deg)); ax.plot(s, z.real, z.imag, color=c, lw=2.8)
for s0 in (np.pi/3,-np.pi/3): ax.plot([s0],[-A],[0],'s',color='0.15',ms=5,zorder=9)
fmt(ax, r'$\mathrm{Im}\,\tilde\tau$', r'$\mathrm{Re}\,r$', r'$\mathrm{Im}\,r$',
    'face 4 — $\\tilde\\tau$ IMAGINARY, $r$ complex\n$\\arg r=60,180,300$ · THE LIFT: $|r|\\leq A$, periodic',
    (2.2,-2.2),(0.95,-0.95),(-0.95,0.95))

# ---- FACE 3: r imaginary -> TRANSVERSE, all purple ----
ax = fig.add_subplot(gs[1,1], projection='3d')
def tau_of_y(y,sgn):
    u=(abs(y)/A)**1.5; z = sgn*u*np.exp(-1j*np.pi/4) if y>0 else sgn*u*np.exp(+1j*np.pi/4)
    return (2/3)*np.arcsinh(z)
for sgn in (+1,-1):
    for ys in (np.linspace(1e-4,1.8,300), np.linspace(-1.8,-1e-4,300)):
        T = np.array([tau_of_y(y,sgn) for y in ys]); ax.plot(T.real, T.imag, ys, color=PURPLE, lw=2.8)
fmt(ax, r'$\mathrm{Re}\,\tilde\tau$', r'$\mathrm{Im}\,\tilde\tau$', r'$\mathrm{Im}\,r$',
    'face 3 — $r$ IMAGINARY, $\\tilde\\tau$ complex\n$\\arg r=90,270$ · TRANSVERSE · ALL PURPLE',
    (1.9,-1.9),(1.1,-1.1),(-1.9,1.9))

# ---- THE RAY MAP ----
ax = fig.add_subplot(gs[:,2])
def col(t):
    t%=360
    return PURPLE if t%90==0 else (BLUE if (0<t<90 or 180<t<270) else RED)
ax.add_artist(plt.Circle((0,0),1.0,fill=False,color='0.88',lw=1))
ax.plot([np.cos(np.deg2rad(t)) for t in range(0,361,60)],[np.sin(np.deg2rad(t)) for t in range(0,361,60)],
        color='0.78',lw=1.1,ls=(0,(6,4)),zorder=1)
FACE={0:'2',60:'4',90:'3',120:'2',180:'4',240:'2',270:'3',300:'4'}
CHAR={0:'real',60:'imag',90:'cplx',120:'real',180:'imag',240:'real',270:'cplx',300:'imag'}
for th in [0,60,90,120,180,240,270,300]:
    c=col(th); hexed=(th%60==0); x,y=np.cos(np.deg2rad(th)),np.sin(np.deg2rad(th))
    ax.plot([0,x],[0,y],color=c,lw=5 if hexed else 2.4,ls='-' if hexed else (0,(4,3)),zorder=3)
    ax.plot(x,y,'o' if hexed else 's',color=c,ms=12 if hexed else 7,zorder=4)
    ax.annotate(f'${th}^\\circ$\n$\\tilde\\tau$ {CHAR[th]}\nface {FACE[th]}',(x,y),
                xytext=(1.31*x,1.31*y),ha='center',va='center',fontsize=8.5,color='0.15')
ax.axhline(0,color='0.93',lw=0.8,zorder=0); ax.axvline(0,color='0.93',lw=0.8,zorder=0)
ax.plot(0,0,'o',color='k',ms=9,zorder=5); ax.annotate('$r=0$',(0,0),xytext=(0.09,-0.14),fontsize=10)
ax.set_aspect('equal'); ax.set_xlim(-1.8,1.8); ax.set_ylim(-2.05,1.75); ax.axis('off')
ax.set_title('the ray map — the four faces in the complex $r$ plane\n'
             'solid $=$ the hexagon ($A_2$ roots) · dashed $=$ face 3, off it', fontsize=11, pad=4)
ax.text(0,-1.42,'PURPLE $\\Leftrightarrow$ $\\arg r$ a multiple of $90^\\circ$\n$\\Leftrightarrow$ $r$ real or purely imaginary',
        ha='center',fontsize=9.5,color='0.2')
ax.text(0,-1.98,'THE CONFLICT: face 1 has $r$ REAL ($\\arg r=0,180$), so by this rule it\n'
        'would be ENTIRELY PURPLE — but it is drawn red/blue by the $\\tilde\\tau$ quadrants.\n'
        'The rule speaks of MOTION (a bead crossing zero); the map speaks of POSITION.\n'
        'Which is the object\'s is $[6^*]$, and is not settled by any of these five panels.',
        ha='center',fontsize=8.2,color='#8a2b2b',va='bottom')
fig.suptitle("Daryl's P13/P14 conjecture — everything: four 3-D shadows of one 4-D object ($\\mathbb{C}_r\\times\\mathbb{C}_{\\tilde\\tau}$), and the ray map",
             fontsize=14.5, y=0.975)
plt.savefig('daryl_p13p14_EVERYTHING.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_EVERYTHING.png', dpi=150, bbox_inches='tight')
print('all four faces + the ray map, in one image. conflict marked on the map.')
