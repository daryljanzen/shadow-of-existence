"""DARYL'S P13/P14 CONJECTURE -- THE TWO MAPS. The ray map, drawn twice: once per rule.

  the r-MAP     (complex r plane)     : the r-RULE's map     -- purple <=> arg r    on an axis
  the tau~-MAP  (complex tau~ plane)  : the tau~-RULE's map  -- purple <=> arg tau~ on an axis

*** WHAT IS A RAY ON ONE MAP IS A WHOLE FACE ON THE OTHER (r1082, verified) ***
    r-plane   : the 0/180 axis IS face 1 (r real)      ; the 90/270 axis IS face 3 (r imaginary)
    tau~-plane: the 0/180 axis IS face 2 (tau~ real)   ; the 90/270 axis IS face 4 (tau~ imaginary)
  EACH MAP TURNS ITS OWN TWO FACES INTO ITS FOUR PURPLE AXES. That is the duality, exactly.

*** AND IT IS BROKEN IN ONE PLACE -- WHICH IS THE POINT ***
  THE HEXAGON EXISTS ONLY ON THE r-MAP. There is no hexagon in the tau~ plane: the three-foldness is
  a property of r -- it IS the cube root r^3 = 2M a^2 sinh^2 -- not of tau~. What the tau~ plane
  carries instead is THREE HORIZONTAL LINES: Im tau~ = 0 (r real > 0: the sheets' shared ray) and
  Im tau~ = +- pi a/3 (r real < 0: face 1's collapse legs). Not a hexagon: a strip of width 2 pi a/3.
  => THE DUALITY IS EXACT IN THE COLOURING AND BROKEN IN THE STRUCTURE, and the break is the
     1/3 - 2/3 asymmetry again -- the same one that forbids smooth passage on face 2 (120 != 180).

*** STATUS: A CONJECTURE. Not derived, not species = sign(r). No face and no map settles it: each
kills the colour information of the variable it pins. Only C_r x C_tau~ whole can. [6*]. ***
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
def col(th):
    t = th % 360
    return PURPLE if t % 90 == 0 else (BLUE if (0 < t < 90 or 180 < t < 270) else RED)

fig, (axL, axR) = plt.subplots(1, 2, figsize=(15.6, 7.8))

# ================= LEFT: the r-MAP =================
axL.add_artist(plt.Circle((0,0), 1.0, fill=False, color='0.88', lw=1))
axL.plot([np.cos(np.deg2rad(t)) for t in range(0,361,60)],
         [np.sin(np.deg2rad(t)) for t in range(0,361,60)], color='0.78', lw=1.2, ls=(0,(6,4)), zorder=1)
FACE={0:'face 2',60:'face 4',90:'face 3',120:'face 2',180:'face 4',240:'face 2',270:'face 3',300:'face 4'}
CHAR={0:'real',60:'imag',90:'cplx',120:'real',180:'imag',240:'real',270:'cplx',300:'imag'}
for th in [0,60,90,120,180,240,270,300]:
    c=col(th); hexed=(th%60==0); x,y=np.cos(np.deg2rad(th)),np.sin(np.deg2rad(th))
    axL.plot([0,x],[0,y], color=c, lw=5.5 if hexed else 2.6, ls='-' if hexed else (0,(4,3)), zorder=3)
    axL.plot(x,y,'o' if hexed else 's', color=c, ms=13 if hexed else 8, zorder=4)
    axL.annotate(f'${th}^\\circ$\n$\\tilde\\tau$ {CHAR[th]}\n{FACE[th]}', (x,y), xytext=(1.32*x,1.32*y),
                 ha='center', va='center', fontsize=8.5, color='0.15')
axL.axhline(0, color=PURPLE, lw=1.4, alpha=0.35, zorder=0); axL.axvline(0, color=PURPLE, lw=1.4, alpha=0.35, zorder=0)
axL.plot(0,0,'o',color='k',ms=10,zorder=5); axL.annotate('$r=0$',(0,0),xytext=(0.09,-0.15),fontsize=10)
axL.set_aspect('equal'); axL.set_xlim(-1.85,1.85); axL.set_ylim(-2.15,1.8); axL.axis('off')
axL.set_title('the $r$-MAP — the complex $r$ plane\npurple $\\Leftrightarrow$ $\\arg r$ on an axis',
              fontsize=12.5, pad=6)
axL.text(0,-1.42,'THE HEXAGON LIVES HERE (solid) — the six $A_2$ roots.\n'
         'the $0/180^\\circ$ axis IS face 1 · the $90/270^\\circ$ axis IS face 3', ha='center', fontsize=9.5, color='0.2')

# ================= RIGHT: the tau~-MAP =================
axR.axhline(0, color=PURPLE, lw=5.5, zorder=3)                                  # Im tau~ = 0 : face 2
axR.axvline(0, color=PURPLE, lw=5.5, zorder=3)                                  # Re tau~ = 0 : face 4
for sgn in (+1,-1):                                                              # Im tau~ = +- pi/3 : face 1's legs
    y = sgn*np.pi/3
    for xa, xb, c in [(-1.85, 0, RED if sgn>0 else BLUE), (0, 1.85, BLUE if sgn>0 else RED)]:
        axR.plot([xa,xb],[y,y], color=c, lw=3.2, zorder=2)
    axR.annotate(f'$\\mathrm{{Im}}\\,\\tilde\\tau={"+" if sgn>0 else "-"}\\pi\\alpha/3$\n$r$ real $<0$ · face 1 legs',
                 (1.55, y), xytext=(1.55, y+0.20*sgn), ha='center', fontsize=8.5, color='0.2')
axR.plot(0,0,'o',color='k',ms=10,zorder=5); axR.annotate('$\\tilde\\tau=0$',(0,0),xytext=(0.10,-0.16),fontsize=10)
axR.annotate('$\\mathrm{Im}\\,\\tilde\\tau=0$\n$r$ real $>0$ · face 2 (the sheets)', (1.55,0), xytext=(1.52,-0.20),
             ha='center', fontsize=8.5, color='0.2')
axR.annotate('$\\mathrm{Re}\\,\\tilde\\tau=0$\nthe LIFT · face 4', (0,1.55), xytext=(0.42,1.52),
             ha='center', fontsize=8.5, color='0.2')
for q,(x,y) in {'Q1':(0.95,0.62),'Q2':(-0.95,0.62),'Q3':(-0.95,-0.62),'Q4':(0.95,-0.62)}.items():
    axR.text(x,y,q, fontsize=11, color=(BLUE if q in ('Q1','Q3') else RED), ha='center', alpha=0.75)
axR.set_aspect('equal'); axR.set_xlim(-1.85,1.85); axR.set_ylim(-2.15,1.8)
axR.set_xlabel(r'$\mathrm{Re}\,\tilde\tau/\alpha$', fontsize=10); axR.set_ylabel(r'$\mathrm{Im}\,\tilde\tau/\alpha$', fontsize=10)
axR.set_xticks([-1,0,1]); axR.set_yticks([-np.pi/3,0,np.pi/3]); axR.set_yticklabels(['$-\\pi/3$','$0$','$+\\pi/3$'])
for sp in ('top','right'): axR.spines[sp].set_visible(False)
axR.set_title('the $\\tilde\\tau$-MAP — the complex $\\tilde\\tau$ plane\npurple $\\Leftrightarrow$ $\\arg\\tilde\\tau$ on an axis',
              fontsize=12.5, pad=6)
axR.text(0,-1.98,'NO HEXAGON HERE. The three-foldness is a property of $r$ — it IS the cube root\n'
         '$r^3=2M\\alpha^2\\sinh^2$ — not of $\\tilde\\tau$. What this plane carries is a STRIP of width $2\\pi\\alpha/3$.\n'
         'the $0/180^\\circ$ axis IS face 2 · the $90/270^\\circ$ axis IS face 4',
         ha='center', fontsize=9.5, color='0.2')

fig.suptitle("Daryl's P13/P14 conjecture — the ray map, drawn twice: one per rule.  What is a RAY on one map is a whole FACE on the other.\n"
             "The duality is EXACT in the colouring and BROKEN in the structure — the hexagon lives only on the $r$-map. That break is the 1/3–2/3.",
             fontsize=12.5, y=0.99)
plt.tight_layout(rect=[0,0,1,0.90])
plt.savefig('daryl_p13p14_TWO_MAPS.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_TWO_MAPS.png', dpi=150, bbox_inches='tight')
print('r-map: hexagon + face3 rays. tau~-map: two purple axes (faces 2,4) + the +-pi/3 legs (face 1). NO hexagon.')
