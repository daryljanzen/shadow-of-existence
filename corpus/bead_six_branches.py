"""THE WHOLE STRUCTURE -- all six branches of the bead in (Re tau~, Im tau~, r).

Solving r^3 = 2M a^2 sinh^2(w), w = 3 tau~/2a, for EVERY branch:
    r > 0 : sinh(w) = +-(r/A)^{3/2}, real          -> 2 branches, Im tau~ = 0
    r < 0 : sinh(x+iy) = +- i u,  u = |r/A|^{3/2}
            => cos y = 0 -> y = +- pi/2  ;  cosh x = u -> x = +- arccosh(u)
                                                    -> 4 branches, Re tau~ = +-(2/3)arccosh(u),
                                                                   Im tau~ = +- pi a/3
    TOTAL: SIX.

THE COLOURING RULE (Daryl, r1076) -- A CONJECTURE, NOT A RESULT:
  Colour by the TAU~ QUADRANT. The conjugation flips the colour across BOTH axes of the tau~ plane --
  across Im tau~ = 0 AND across Re tau~ = 0 -- so species tracks sign(Re tau~ * Im tau~):
      Q1 (+,+) and Q3 (-,-) : one colour        Q2 (-,+) and Q4 (+,-) : the other
  Then the PURPLE IS NOT A SPECIAL CASE -- it is the same rule read on the boundary: the two r>0
  branches sit at Im tau~ = 0, i.e. ON the quadrant boundary. +Re straddles Q1/Q4, -Re straddles Q2/Q3.
  Two curves in one -> purple. The neutrality of the real axis and the purple are the same fact.

  *** STATUS: THIS IS A COLOURING CONJECTURE. IT IS NOT DERIVED AND IT IS NOT species = sign(r). ***
  By the corpus's definition sign(r)<0 on ALL FOUR r<0 branches -> all four antimatter, no purple, no
  vertex. This rule and species=sign(r) CANNOT BOTH BE THE GEOMETRY'S. Which one is cannot be settled
  here: sign(r) exists only on the real-r slice, and this whole figure IS that slice. See storyboard
  [6*]. THE RHYME STAYS A RHYME until A3 works the full C_r x C_tau~ object. This picture CARRIES the
  conjecture; it does not test it.

WHAT LIVES IN HERE: every physical reading is a PATH through this structure.
  * the cosmological bundle  = one red r<0 branch, up to r=0, continuing on a purple r>0 branch
  * pair production / annihilation = a purple r>0 branch meeting r=0 and opening into a
    CONJUGATE PAIR (one red, one blue) -- and back
  * r=0 is where all six meet: the conjugation locus, the branch point, the vertex.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)     # red+blue: self-conjugate
al = 1.0; A = 2**(1/3)*al/np.sqrt(3); rmax = 2.4

def tau_re(r): return (2/3)*np.arcsinh((r/A)**1.5)
def wing(r):
    u = abs(r/A)**1.5
    return (0.0, (2/3)*np.arcsin(u)) if u <= 1 else ((2/3)*np.arccosh(u), np.pi/3)
rp = np.linspace(1e-4, rmax, 300); sx = np.array([tau_re(r) for r in rp])
rn = np.linspace(-1e-4, -rmax, 360)
W  = np.array([wing(r) for r in rn]); wx, wy = W[:,0], W[:,1]

fig = plt.figure(figsize=(10.5, 9))
ax = fig.add_subplot(111, projection='3d')

# ---- the four r<0 branches, coloured BY THE TAU~ QUADRANT ----
# the conjugation flips the colour across BOTH axes of the tau~ plane, so species tracks
# sign(Re tau~ * Im tau~):   Q1(+,+) & Q3(-,-) one colour ; Q2(-,+) & Q4(+,-) the other.
for sx_sgn, sy_sgn in [(+1,+1), (-1,+1), (-1,-1), (+1,-1)]:
    col = BLUE if sx_sgn*sy_sgn > 0 else RED            # Q1,Q3 blue ; Q2,Q4 red
    ax.plot(sx_sgn*wx, sy_sgn*wy, rn, color=col, lw=3.4)
# ---- the two r>0 branches: they sit AT Im tau~ = 0, i.e. ON THE QUADRANT BOUNDARY ----
# +Re straddles Q1(blue)/Q4(red) ; -Re straddles Q2(red)/Q3(blue). Two curves in one -> PURPLE.
# The purple is not a special case: it is the same rule, read on the boundary.
for sgn_x in (-1, +1):
    ax.plot(sgn_x*sx, 0*rp, rp, color=PURPLE, lw=4.2)

ax.scatter([0],[0],[0], color='k', s=70, zorder=10)
ax.text(0, 0.20, 0.42, r'$r{=}0$', fontsize=12)
ax.text(-sx[-1]*0.86, 0, rp[-1]*0.99, '$\\mathrm{Im}\\,\\tilde\\tau=0$\n(two in one: purple)', color=PURPLE, fontsize=10.5, ha='center')
ax.text(-wx[-1]*0.92, +wy[-1], rn[-1]*0.99, 'Q2', color=RED,  fontsize=11, ha='center')
ax.text(+wx[-1]*0.92, +wy[-1], rn[-1]*0.99, 'Q1', color=BLUE, fontsize=11, ha='center')
ax.text(-wx[-1]*0.92, -wy[-1], rn[-1]*0.99, 'Q3', color=BLUE, fontsize=11, ha='center')
ax.text(+wx[-1]*0.92, -wy[-1], rn[-1]*0.99, 'Q4', color=RED,  fontsize=11, ha='center')

ax.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$', labelpad=8)
ax.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$', labelpad=8)
ax.set_zlabel(r'$r/\alpha$', labelpad=4)
ax.set_xlim(2,-2); ax.set_ylim(1.2,-1.2); ax.set_zlim(-rmax, rmax)
ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1]); ax.set_zticks([-2,0,2])
ax.view_init(elev=15, azim=-60); ax.set_box_aspect((1,1,1), zoom=1.05)
ax.set_title('the bead, whole — all six branches, coloured by the $\\tilde\\tau$ quadrant\n'
             r'Q1,Q3 vs Q2,Q4 · the $r>0$ pair sits ON the boundary $\rightarrow$ two in one $\rightarrow$ purple',
             fontsize=12.5, pad=-10)
plt.tight_layout()
plt.savefig('bead_six_branches.pdf', bbox_inches='tight')
plt.savefig('bead_six_branches.png', dpi=150, bbox_inches='tight')
print('six branches drawn: 2 purple (r>0, on the fixed locus), 4 red/blue (r<0, conjugate pairs)')
print('purple = red+blue =', tuple(round(c,3) for c in PURPLE))
