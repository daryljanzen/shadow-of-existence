"""DARYL'S P13/P14 CONJECTURE -- THE OTHER FACE: tau~ real, r COMPLEX. The same three, inverted.

Hold tau~ REAL and let r go complex. Then sinh^2(3 tau~/2a) is real and >= 0, so r^3 is real and >= 0:
    r = |r| e^{2 pi i k/3},  k = 0,1,2   -- THE THREE SHEETS, at arg r = 0, 120, 240 degrees
    |r| = A |sinh(3 tau~/2a)|^{2/3},   A = (2M a^2)^{1/3} = cbrt(2) a/sqrt3 at Nariai

*** WHAT EACH FACE CANNOT SEE (the reason both are needed) ***
  * r real NEGATIVE is arg r = 180 deg -- NOT one of 0/120/240. So the FOUR r<0 branches of the other
    face DO NOT EXIST HERE. They require complex tau~.
  * sheets 1,2 have arg r = 120/240: r is genuinely COMPLEX. They DO NOT EXIST on the other face,
    which holds r real.
  * the two faces share ONLY sheet 0 at r>0 with real tau~ -- ONE LINE.
  => six segments on each face, two shared: TEN in all. Neither face is the object. Both are shadows.

THE RULE (Daryl), read on the COMPLEX r PLANE -- and it mirrors exactly:
  conjugate when you go from positive to negative, real or imaginary, r or tau~; and it is ONE EVENT,
  at the origin, where r AND tau~ both vanish in real and imaginary parts. Asymmetric: Nariai, 1/3 vs 2/3.
    sheet 1 (arg r = 120) -> Q2 of the r-plane -> red        sheet 2 (arg r = 240) -> Q3 -> blue
    sheet 0 (arg r = 0)   -> ON the Re r axis = the quadrant BOUNDARY -> two in one -> PURPLE
  and crossing tau~ = 0 flips them all.

  (1) THE COSMOLOGICAL BEAD -- sheet 2, alone: red (tau~<0, the antimatter black hole) turning blue
      (tau~>0, our matter universe) at the origin. Not purple: nothing merges with it.
  (2) PAIR PRODUCTION / ANNIHILATION -- sheets 1 and 2 at tau~<0 (one blue, one red) crossing the
      origin onto sheet 0 at tau~>0: red+blue = PURPLE. The merger IS the vertex.
  (3) THE WHOLE STRUCTURE -- three sheets, six segments, colour flipping at tau~ = 0.

*** STATUS: A COLOURING CONJECTURE. NOT DERIVED, AND NOT species = sign(r). ***
On THIS face sign(r) is not even defined off sheet 0 -- there is no sign of a 120-degree r. That is
precisely why neither face can settle it, and why A3 must work the full C_r x C_tau~ object.
THE RHYME STAYS A RHYME. This picture CARRIES the conjecture; it does not test it.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
al = 1.0; A = 2**(1/3)*al/np.sqrt(3); tmax = 2.0

tp = np.linspace(1e-4, tmax, 300); tn = np.linspace(-tmax, -1e-4, 300)
mod = lambda t: A*np.abs(np.sinh(1.5*t))**(2/3)
def sheet(t, k):
    z = mod(t)*np.exp(2j*np.pi*k/3); return z.real, z.imag
# colour: sheet1 -> Q2 -> red at tau~>0 ; sheet2 -> Q3 -> blue at tau~>0 ; flip at tau~=0
COL = {(1,'+'):RED, (1,'-'):BLUE, (2,'+'):BLUE, (2,'-'):RED, (0,'+'):PURPLE, (0,'-'):PURPLE}

def frame(ax, title):
    ax.scatter([0],[0],[0], color='k', s=52, zorder=10)
    ax.text(0.16, 0, 0.30, r'$r{=}0$', fontsize=10)
    ax.set_xlabel(r'$\tilde\tau/\alpha$', labelpad=3, fontsize=9)
    ax.set_ylabel(r'$\mathrm{Re}\,r/\alpha$', labelpad=3, fontsize=9)
    ax.set_zlabel(r'$\mathrm{Im}\,r/\alpha$', labelpad=1, fontsize=9)
    ax.set_xlim(2,-2); ax.set_ylim(1.9,-1.9); ax.set_zlim(-1.9,1.9)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([-1,0,1])
    ax.tick_params(labelsize=7.5); ax.view_init(elev=16, azim=-60); ax.set_box_aspect((1,1,1), zoom=1.08)
    ax.set_title(title, fontsize=12, pad=-6)

def draw(ax, ks):
    for k in ks:
        for t, sg in ((tp,'+'), (tn,'-')):
            x, y = sheet(t, k); ax.plot(t, x, y, color=COL[(k,sg)], lw=3.6 if k else 4.2)

fig = plt.figure(figsize=(16.8, 6.2))

ax1 = fig.add_subplot(1,3,1, projection='3d'); draw(ax1, [2])
frame(ax1, '(1) the cosmological bead — one bead, alone')
x,y = sheet(tn,2); ax1.text(tn[0], x[0], y[0], 'antimatter\nblack hole', color=RED, fontsize=9.5, ha='center')
x,y = sheet(tp,2); ax1.text(tp[-1], x[-1], y[-1], 'matter\nuniverse', color=BLUE, fontsize=9.5, ha='center')

ax2 = fig.add_subplot(1,3,2, projection='3d')
for t, sg, k in ((tn,'-',1), (tn,'-',2)):                     # the pair, at tau~ < 0
    x,y = sheet(t,k); ax2.plot(t, x, y, color=COL[(k,sg)], lw=3.6)
x,y = sheet(tp,0); ax2.plot(tp, x, y, color=PURPLE, lw=4.4)   # the merged track, at tau~ > 0
frame(ax2, '(2) pair production $\\rightleftarrows$ annihilation — two beads, one track')
x,y = sheet(tn,1); ax2.text(tn[0], x[0], y[0], 'blue bead', color=BLUE, fontsize=9.5, ha='center')
x,y = sheet(tn,2); ax2.text(tn[0], x[0], y[0], 'red bead',  color=RED,  fontsize=9.5, ha='center')
x,y = sheet(tp,0); ax2.text(tp[-1], x[-1], y[-1], 'purple:\ntwo beads,\none track', color=PURPLE, fontsize=9.5, ha='center')

ax3 = fig.add_subplot(1,3,3, projection='3d'); draw(ax3, [0,1,2])
frame(ax3, '(3) the whole structure — three sheets, six segments')
for k, lb in [(0,'sheet 0\n($\\arg r=0$)'), (1,'sheet 1\n($120^\\circ$)'), (2,'sheet 2\n($240^\\circ$)')]:
    x,y = sheet(tp,k); ax3.text(tp[-1], x[-1], y[-1], lb, fontsize=8.5, color='0.25', ha='center')

fig.suptitle("Daryl's P13/P14 conjecture, the other face — $\\tilde\\tau$ real, $r$ complex: the three sheets",
             fontsize=14.5, y=0.965)
plt.tight_layout(rect=[0,0,1,0.94])
plt.savefig('daryl_p13p14_conjecture_face2.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_conjecture_face2.png', dpi=150, bbox_inches='tight')
print('face 2: 3 sheets x 2 halves = 6 segments. Shares only sheet 0 (r>0, real tau~) with face 1.')
print('the 4 r<0 branches of face 1 CANNOT appear here (arg r = 180 is not a cube root of a positive real).')
