"""DARYL'S P13/P14 CONJECTURE -- colour by the tau~ quadrant, drawn on three readings.

THE RULE (Daryl, r1077):
    YOU CONJUGATE WHEN YOU GO FROM POSITIVE TO NEGATIVE -- real or imaginary, r or tau~.
    AND IT IS ONE EVENT, NOT A TALLY: conjugation happens AT THE ORIGIN -- the single place where
    r AND tau~ both go to zero, in their real AND imaginary parts. Not two crossings that might
    cancel; one place where everything vanishes at once. That is where it happens.
    AND IT IS ASYMMETRIC -- Nariai, 1/3 vs 2/3. The asymmetry IS the symmetry-breaking, not a
    footnote to it.
    Read on the tau~ plane at r<0 the rule gives the quadrants: Q1 (+,+) & Q3 (-,-) one colour,
    Q2 (-,+) & Q4 (+,-) the other.

THE CONJECTURE, in one line: THIS IS THE GEOMETRIC OBJECT THAT CONNECTS THESE EVENTS.
PURPLE IS NOT A THIRD SPECIES. It is TWO BEADS SHARING A TRACK. The r<0 branches pair by their
Re tau~ sign -- Q1,Q4 both at +Re ; Q2,Q3 both at -Re -- so each pair continues onto the SAME r>0
line. Those two beads had OPPOSITE colours at r<0, so they arrive at r>0 with opposite colours:
red and blue on one line -> purple. Hence SIX branches but FOUR CONTINUOUS BEADS WITH TWO MERGERS.

  (1) THE COSMOLOGICAL BEAD -- one bead, alone. Red antimatter black hole (r<0) up to r=0, turning
      blue as our matter universe (r>0). NOT purple: nothing merges with it. It is a single bead
      doing what gets done along a bead. Red turns to blue.
  (2) PAIR PRODUCTION / ANNIHILATION -- two beads. A red and a blue at r<0 cross r=0 onto the same
      r>0 track, flipping to blue and red: red+blue = PURPLE. Read one way it is annihilation, the
      other production. The merger IS the vertex.
  (3) THE WHOLE STRUCTURE -- all six branches: four beads, two mergers, both r>0 tracks purple.

*** STATUS: A COLOURING CONJECTURE. NOT DERIVED, AND NOT species = sign(r). ***
By the corpus's definition sign(r)<0 on ALL FOUR r<0 branches -> all four antimatter, no purple, no
vertex. This rule and species=sign(r) CANNOT BOTH BE THE GEOMETRY'S, and WHICH ONE IS CANNOT BE
SETTLED HERE: sign(r) exists only on the real-r slice, and this whole figure IS that slice. The full
object is C_r x C_tau~ (4 real dims); this is a 3-D projection of it. See storyboard [6*].
THE RHYME STAYS A RHYME until A3 works the full analytic object. These pictures CARRY the conjecture;
they do not test it. The connection to Feynman lies beyond this projection, not inside it.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
al = 1.0; A = 2**(1/3)*al/np.sqrt(3); rmax = 2.4

def tau_re(r): return (2/3)*np.arcsinh((r/A)**1.5)
def wing(r):
    u = abs(r/A)**1.5
    return (0.0, (2/3)*np.arcsin(u)) if u <= 1 else ((2/3)*np.arccosh(u), np.pi/3)
rp = np.linspace(1e-4, rmax, 300); sx = np.array([tau_re(r) for r in rp])
rn = np.linspace(-1e-4, -rmax, 360)
W = np.array([wing(r) for r in rn]); wx, wy = W[:,0], W[:,1]
QUAD = {  # (Re sign, Im sign) -> (xs, ys, colour at r<0)
 'Q1': (+wx, +wy, BLUE), 'Q2': (-wx, +wy, RED), 'Q3': (-wx, -wy, BLUE), 'Q4': (+wx, -wy, RED)}

def frame(ax, title):
    ax.scatter([0],[0],[0], color='k', s=52, zorder=10)
    ax.text(0, 0.20, 0.42, r'$r{=}0$', fontsize=10)
    ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$', labelpad=3, fontsize=9)
    ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$', labelpad=3, fontsize=9)
    ax.set_zlabel(r'$r/\alpha$', labelpad=1, fontsize=9)
    ax.set_xlim(2,-2); ax.set_ylim(1.2,-1.2); ax.set_zlim(-rmax, rmax)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([-2,0,2])
    ax.tick_params(labelsize=7.5); ax.view_init(elev=15, azim=-60); ax.set_box_aspect((1,1,1), zoom=1.08)
    ax.set_title(title, fontsize=12, pad=-6)

fig = plt.figure(figsize=(16.8, 6.2))

# ---------- (1) the cosmological bead: ONE bead, alone. red -> blue. no merger, no purple ----------
ax1 = fig.add_subplot(1,3,1, projection='3d')
xs, ys, _ = QUAD['Q2']
ax1.plot(xs, ys, rn, color=RED,  lw=4.0)                    # Q2 red at r<0: the antimatter black hole
ax1.plot(+sx, 0*rp, rp, color=BLUE, lw=4.0)                 # continues onto the OTHER track: crosses Re tau~=0 too
frame(ax1, '(1) the cosmological bead — one bead, alone')
ax1.text(xs[-1], ys[-1], rn[-1]*0.98, 'antimatter\nblack hole', color=RED, fontsize=9.5, ha='center')
ax1.text(+sx[-1], 0, rp[-1]*0.98, 'matter\nuniverse', color=BLUE, fontsize=9.5, ha='center')
ax1.text(-1.5, 0, 1.4, 'crosses $r{=}0$ AND\n$\\mathrm{Re}\\,\\tilde\\tau{=}0$.\nred turns to blue.\nnothing merges with it:\nnot purple', fontsize=8.5, color='0.35')

# ---------- (2) the vertex: TWO beads onto ONE track -> purple ----------
ax2 = fig.add_subplot(1,3,2, projection='3d')
for q in ('Q2','Q3'):                                        # the pair on NEGATIVE tau~ (both at -Re)
    xs, ys, col = QUAD[q]; ax2.plot(xs, ys, rn, color=col, lw=3.6)
ax2.plot(sx, 0*rp, rp, color=PURPLE, lw=4.4)                 # the merged track: red+blue
frame(ax2, '(2) pair production $\\rightleftarrows$ annihilation — two beads, one track')
ax2.text(QUAD['Q3'][0][-1], QUAD['Q3'][1][-1], rn[-1]*0.98, 'blue bead', color=BLUE, fontsize=9.5, ha='center')
ax2.text(QUAD['Q2'][0][-1], QUAD['Q2'][1][-1], rn[-1]*0.98, 'red bead',  color=RED,  fontsize=9.5, ha='center')
ax2.text(sx[-1], 0, rp[-1]*0.98, 'purple:\ntwo beads,\none track', color=PURPLE, fontsize=9.5, ha='center')

# ---------- (3) the whole structure: six branches = four beads, two mergers ----------
ax3 = fig.add_subplot(1,3,3, projection='3d')
for q in ('Q1','Q2','Q3','Q4'):
    xs, ys, col = QUAD[q]; ax3.plot(xs, ys, rn, color=col, lw=3.2)
for sgn in (+1,-1):                                          # both r>0 tracks carry two beads -> purple
    ax3.plot(sgn*sx, 0*rp, rp, color=PURPLE, lw=4.2)
frame(ax3, '(3) the whole structure — four beads, two mergers')
for q, ha in [('Q1','center'),('Q2','center'),('Q3','center'),('Q4','center')]:
    xs, ys, col = QUAD[q]
    ax3.text(xs[-1], ys[-1], rn[-1]*0.98, q, color=col, fontsize=10.5, ha=ha)

fig.suptitle("Daryl's P13/P14 conjecture — colour by the $\\tilde\\tau$ quadrant; purple is two beads on one track",
             fontsize=14.5, y=0.965)
plt.tight_layout(rect=[0,0,1,0.94])
plt.savefig('daryl_p13p14_conjecture.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_conjecture.png', dpi=150, bbox_inches='tight')
print('six branches = four beads (Q1,Q2,Q3,Q4) + two mergers (the +Re and -Re tracks at r>0)')
print('purple = red+blue =', tuple(round(c,3) for c in PURPLE))
