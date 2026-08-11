"""DARYL'S P13/P14 CONJECTURE -- ALL FOUR FACES TOGETHER, and the ray map that unifies them.

THE RULE THAT FALLS OUT (r1079, verified): for r = |r| e^{i theta}, r^3 = 2M a^2 sinh^2(w) forces
arg sinh(w) = 3 theta/2, which fixes the CHARACTER of tau~:

   arg r    arg sinh w    tau~ is      colour by Daryl's rule
     0         0          REAL         PURPLE   (on the +Re r axis: a quadrant boundary)
    60        90          IMAGINARY    blue     (Q1)
    90       135          complex      PURPLE   (on the +Im r axis)
   120       180          REAL         red      (Q2)
   180       270          IMAGINARY    PURPLE   (on the -Re r axis)  <- r real NEGATIVE
   240         0          REAL         blue     (Q3)
   270        45          complex      PURPLE   (on the -Im r axis)
   300        90          IMAGINARY    red      (Q4)

*** PURPLE <=> arg r is a multiple of 90 <=> r is REAL or PURELY IMAGINARY. ***
Purple is an r-CONDITION. It says nothing about tau~: the purples at 0 (tau~ real), 90 (complex),
180 (tau~ imaginary), 270 (complex) share no tau~ character. But the TWO ON FACE 3 (90, 270) have
tau~ NEITHER purely real NOR purely imaginary -- those purples have no real tau~.

THE FOUR FACES ARE THE FOUR WAYS OF ASKING "which of r, tau~ is real / imaginary":
   face 1  r REAL,      tau~ complex   -> arg r = 0, 180        the smooth bead; the lift as a segment
   face 2  tau~ REAL,   r complex      -> arg r = 0, 120, 240   the three sheets
   face 4  tau~ IMAG,   r complex      -> arg r = 60, 180, 300  THE LIFT: |r| <= A, periodic
   face 3  r IMAG,      tau~ complex   -> arg r = 90, 270       TRANSVERSE: between the rays

THE HEXAGON = faces 2 + 4 = arg r 0,60,120,180,240,300 -- the six roots of A2.
   of its six rays exactly TWO are purple: 0 and 180, i.e. r REAL. Four are coloured: 60,120,240,300.
   Face 3's purples (90,270) sit OFF the hexagon: the axis-crossings BETWEEN the roots.

*** STATUS: A CONJECTURE. Not derived. Not species = sign(r) -- which has no referent at all on
faces 3 and 4's off-real rays. No face settles it; the object is C_r x C_tau~. THE RHYME STAYS A
RHYME until A3 works it whole. These pictures carry the conjecture; they do not test it. ***
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
A = 2**(1/3)/np.sqrt(3)

def col(theta):
    t = theta % 360
    if t % 90 == 0: return PURPLE                       # on an axis: two-in-one
    return BLUE if (0 < t < 90 or 180 < t < 270) else RED

fig = plt.figure(figsize=(14.2, 7.4))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.25], wspace=0.05)

# ---------------- LEFT: the ray map -- all four faces at once, in the complex r plane ----------------
ax = fig.add_subplot(gs[0,0])
ax.add_artist(plt.Circle((0,0), 1.0, fill=False, color='0.85', lw=1))
FACE = {0:'2', 60:'4', 90:'3', 120:'2', 180:'4', 240:'2', 270:'3', 300:'4'}
CHAR = {0:'real', 60:'imag', 90:'cplx', 120:'real', 180:'imag', 240:'real', 270:'cplx', 300:'imag'}
for th in [0,60,90,120,180,240,270,300]:
    c = col(th); on_hex = (th % 60 == 0)
    x, y = np.cos(np.deg2rad(th)), np.sin(np.deg2rad(th))
    ax.plot([0, x],[0, y], color=c, lw=4.5 if on_hex else 2.4, ls='-' if on_hex else (0,(4,3)), zorder=3)
    ax.plot(x, y, 'o' if on_hex else 's', color=c, ms=11 if on_hex else 7, zorder=4)
    ax.annotate(f'${th}^\\circ$\n$\\tilde\\tau$ {CHAR[th]}\nface {FACE[th]}', (x,y),
                xytext=(1.30*x, 1.30*y), ha='center', va='center', fontsize=8.5, color='0.15')
hexx = [np.cos(np.deg2rad(t)) for t in range(0,361,60)]; hexy = [np.sin(np.deg2rad(t)) for t in range(0,361,60)]
ax.plot(hexx, hexy, color='0.75', lw=1.2, ls=(0,(6,4)), zorder=1)
ax.axhline(0, color='0.9', lw=0.8, zorder=0); ax.axvline(0, color='0.9', lw=0.8, zorder=0)
ax.plot(0,0,'o',color='k',ms=9, zorder=5); ax.annotate('$r=0$', (0,0), xytext=(0.10,-0.13), fontsize=10)
ax.set_aspect('equal'); ax.set_xlim(-1.75,1.75); ax.set_ylim(-1.6,1.6); ax.axis('off')
ax.set_title('the ray map — all four faces in the complex $r$ plane\n'
             'solid $=$ the hexagon ($A_2$ roots) · dashed $=$ face 3, off it',
             fontsize=12, pad=2)
ax.text(0, -1.48, 'PURPLE $\\Leftrightarrow$ $\\arg r$ a multiple of $90^\\circ$ $\\Leftrightarrow$ $r$ real or purely imaginary',
        ha='center', fontsize=10, color='0.2')

# ---------------- RIGHT: the table ----------------
ax2 = fig.add_subplot(gs[0,1]); ax2.axis('off')
rows = [(0,'0°','REAL','purple','face 2 · sheet 0 · $r>0$'),
        (60,'90°','IMAGINARY','blue','face 4 · the lift'),
        (90,'135°','complex','purple','face 3 · transverse'),
        (120,'180°','REAL','red','face 2 · sheet 1'),
        (180,'270°','IMAGINARY','purple','face 4 · $r$ real $<0$'),
        (240,'0°','REAL','blue','face 2 · sheet 2'),
        (270,'45°','complex','purple','face 3 · transverse'),
        (300,'90°','IMAGINARY','red','face 4 · the lift')]
ax2.text(0.02, 0.955, '$\\arg r$', fontsize=11, fontweight='bold')
ax2.text(0.20, 0.955, '$\\arg\\sinh w$', fontsize=11, fontweight='bold')
ax2.text(0.45, 0.955, '$\\tilde\\tau$ is', fontsize=11, fontweight='bold')
ax2.text(0.65, 0.955, 'colour', fontsize=11, fontweight='bold')
ax2.text(0.82, 0.955, 'where it lives', fontsize=11, fontweight='bold')
for i,(th,sh,ch,cl,wh) in enumerate(rows):
    y = 0.885 - i*0.105
    c = col(th); hexed = (th % 60 == 0)
    ax2.text(0.02, y, f'${th}^\\circ$', fontsize=11.5, color=c, fontweight='bold' if hexed else 'normal')
    ax2.text(0.20, y, sh, fontsize=10.5, color='0.3')
    ax2.text(0.45, y, ch, fontsize=10.5, color='0.15' if ch!='complex' else '0.45')
    ax2.text(0.65, y, cl, fontsize=10.5, color=c, fontweight='bold')
    ax2.text(0.82, y, wh, fontsize=9, color='0.35')
    if not hexed: ax2.text(0.985, y, '(off hex)', fontsize=8, color='0.6', ha='right')
ax2.text(0.02, 0.045,
 'the four faces are the four ways of asking which of $r,\\tilde\\tau$ is real or imaginary.\n'
 '$\\tilde\\tau$ real $\\rightarrow 0,120,240$ · $\\tilde\\tau$ imaginary $\\rightarrow 60,180,300$ : together, THE HEXAGON.\n'
 '$r$ imaginary $\\rightarrow 90,270$ : off it — the axis-crossings between the roots, and both purple.\n'
 'of the hexagon\'s six rays exactly two are purple: $0^\\circ$ and $180^\\circ$ — i.e. $r$ REAL.',
 fontsize=9.5, color='0.25', va='bottom')
fig.suptitle("Daryl's P13/P14 conjecture — the four faces together", fontsize=15, y=0.985)
plt.savefig('daryl_p13p14_all_faces.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_all_faces.png', dpi=150, bbox_inches='tight')
print('purple rays: 0, 90, 180, 270  (r real or purely imaginary)')
print('hexagon: 0,60,120,180,240,300 -- two purple (0,180 = r real), four coloured')
print('face 3 (90,270): both purple, both OFF the hexagon, tau~ neither real nor imaginary')
