"""DARYL'S P13/P14 CONJECTURE -- FACES 3 AND 4: the imaginary cuts.

FACE 4 -- tau~ IMAGINARY (tau~ = i s), r complex.
    w = i sigma, sigma = 3s/2a ;  sinh(i sigma) = i sin sigma  =>  sinh^2 = -sin^2  =>  r^3 <= 0
    => |r| = A |sin(3s/2a)|^{2/3}        arg r = 60, 180, 300
    *** sin IS BOUNDED AND PERIODIC, SO |r| <= A. THE FACE IS BOUNDED. ***
    |r| = A exactly at |sin| = 1, i.e. s = +- pi a/3 -- and A is THE TURNAROUND -(2M a^2)^{1/3}.
    => THIS FACE IS THE LIFT. Face 1 draws the lift as a vertical segment at Re tau~ = 0 with
       Im tau~ : 0 -> +-pi a/3 and |r| : 0 -> A. Face 4 IS that same object, drawn as three rays,
       and it CLOSES: sin(3s/2) has period 4 pi a/3.
    arg r = 180 is r REAL NEGATIVE: the antimatter branch of face 1 lives here, as one of three rays.

FACE 3 -- r IMAGINARY (r = i y), tau~ complex.
    r^3 = -i y^3  =>  sinh(w) = +- (y/A)^{3/2} e^{-i pi/4}  =>  tau~ GENUINELY COMPLEX --
    Im tau~ is not pinned to 0 or +-pi a/3; it SLIDES.
    arg r = 90 / 270, which is NOT one of the six rays (0,60,120,180,240,300).
    => THIS FACE IS TRANSVERSE. It cuts BETWEEN the rays and sees none of them: no r>0 branch
       (r real), no r<0 branch (r real), no sheet. It is the face in the gaps.

TOGETHER WITH FACES 1-2 (see section 4b of the storyboard):
    tau~ real      -> arg r = 0, 120, 240
    tau~ imaginary -> arg r = 60, 180, 300      } SIX RAYS, 60 apart: THE HEXAGON, the A2 roots
    r imaginary    -> arg r = 90, 270           } transverse: between the rays

*** STATUS: A CONJECTURE. The colouring rule extended to these faces is NOT derived, and NOT
species = sign(r) -- on face 4, sign(r) is undefined on two of the three rays, and on face 3 it is
undefined everywhere (r is imaginary). That is the point: no face can settle it. THE RHYME STAYS A
RHYME until A3 works the full C_r x C_tau~ object. ***
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':12,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
al = 1.0; A = 2**(1/3)*al/np.sqrt(3)

fig = plt.figure(figsize=(13.2, 6.4))

# ---------------- FACE 4: tau~ imaginary -> the LIFT, bounded and periodic ----------------
ax1 = fig.add_subplot(1,2,1, projection='3d')
sp = np.linspace(1e-4, 2*np.pi/3, 400); sn = np.linspace(-2*np.pi/3, -1e-4, 400)
mod4 = lambda s: A*np.abs(np.sin(1.5*s))**(2/3)
# the rule on the complex-r plane: 60 -> Q1 -> blue ; 300 -> Q4 -> red ; 180 -> ON the -Re axis
# (Im r = 0) -> the quadrant boundary -> two in one -> PURPLE. tau~ crossing 0 flips.
RAY4 = {60: (BLUE, RED), 180: (PURPLE, PURPLE), 300: (RED, BLUE)}   # (s>0, s<0)
for deg, (cp, cn) in RAY4.items():
    for s, col in ((sp, cp), (sn, cn)):
        z = mod4(s)*np.exp(1j*np.deg2rad(deg))
        ax1.plot(s, z.real, z.imag, color=col, lw=3.8)
for s0 in (np.pi/3, -np.pi/3):                       # |r| = A : THE TURNAROUND, the bound
    z = A*np.exp(1j*np.deg2rad(180)); ax1.plot([s0],[z.real],[z.imag],'s',color='0.15',ms=7,zorder=9)
ax1.scatter([0],[0],[0], color='k', s=52, zorder=10)
ax1.text(0.14, 0, 0.28, r'$r{=}0$', fontsize=10)
ax1.text(np.pi/3, -A, 0.30, 'turnaround\n$|r|{=}A$ at $s{=}\\pi\\alpha/3$', fontsize=8.5, color='0.2', ha='center')
for deg, lb in [(60,'$60^\\circ$'), (180,'$180^\\circ$\n($r$ real $<0$)'), (300,'$300^\\circ$')]:
    z = mod4(sp[-1])*np.exp(1j*np.deg2rad(deg))
    ax1.text(sp[-1], z.real, z.imag, lb, fontsize=8.5, color='0.3', ha='center')
ax1.set_xlabel(r'$s=\mathrm{Im}\,\tilde\tau/\alpha$', labelpad=3, fontsize=9)
ax1.set_ylabel(r'$\mathrm{Re}\,r/\alpha$', labelpad=3, fontsize=9)
ax1.set_zlabel(r'$\mathrm{Im}\,r/\alpha$', labelpad=1, fontsize=9)
ax1.set_xlim(2.2,-2.2); ax1.set_ylim(0.95,-0.95); ax1.set_zlim(-0.95,0.95)
ax1.tick_params(labelsize=7.5); ax1.view_init(elev=16, azim=-60); ax1.set_box_aspect((1,1,1), zoom=1.06)
ax1.set_title('face 4 — $\\tilde\\tau$ imaginary: THE LIFT\n(bounded $|r|\\leq A$, periodic; $\\arg r=60,180,300$)', fontsize=11.5, pad=-8)

# ---------------- FACE 3: r imaginary -> TRANSVERSE, between the rays ----------------
ax2 = fig.add_subplot(1,2,2, projection='3d')
def tau_of_y(y, sgn):
    u = (abs(y)/A)**1.5
    z = sgn*u*np.exp(-1j*np.pi/4) if y > 0 else sgn*u*np.exp(+1j*np.pi/4)
    return (2/3)*np.arcsinh(z)
for sgn, col in ((+1, BLUE), (-1, RED)):
    for ys in (np.linspace(1e-4, 1.8, 300), np.linspace(-1.8, -1e-4, 300)):
        T = np.array([tau_of_y(y, sgn) for y in ys])
        ax2.plot(T.real, T.imag, ys, color=col, lw=3.4)
ax2.scatter([0],[0],[0], color='k', s=52, zorder=10)
ax2.text(0.16, 0, 0.22, r'$r{=}0$', fontsize=10)
ax2.text(0, -0.95, 1.5, '$\\arg r = 90^\\circ/270^\\circ$:\nNOT one of the six rays.\n$\\mathrm{Im}\\,\\tilde\\tau$ slides — it is\npinned to nothing.', fontsize=8.5, color='0.3')
ax2.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$', labelpad=3, fontsize=9)
ax2.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$', labelpad=3, fontsize=9)
ax2.set_zlabel(r'$\mathrm{Im}\,r/\alpha$', labelpad=1, fontsize=9)
ax2.set_xlim(1.9,-1.9); ax2.set_ylim(1.1,-1.1); ax2.set_zlim(-1.9,1.9)
ax2.tick_params(labelsize=7.5); ax2.view_init(elev=16, azim=-60); ax2.set_box_aspect((1,1,1), zoom=1.06)
ax2.set_title('face 3 — $r$ imaginary: TRANSVERSE\n(cuts between the rays; $\\tilde\\tau$ genuinely complex)', fontsize=11.5, pad=-8)

fig.suptitle("Daryl's P13/P14 conjecture — the imaginary cuts: face 4 is the lift, face 3 is transverse",
             fontsize=14, y=0.965)
plt.tight_layout(rect=[0,0,1,0.94])
plt.savefig('daryl_p13p14_faces34.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_faces34.png', dpi=150, bbox_inches='tight')
print('face 4: |r| <= A =', round(A,4), '; bound reached at s = +-pi/3 =', round(np.pi/3,4), '= the turnaround')
print('face 3: arg r = 90/270 -- between the rays; Im tau~ unpinned')
