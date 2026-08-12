"""DARYL'S P13/P14 CONJECTURE -- THE HINGES, and the SKEW HEXAGON. (r1085, Daryl's construction.)

The substrate slice -X0^2 + X1^2 + X2^2 = a^2 is a hyperboloid of one sheet: DOUBLY RULED.
    equator : X0 = 0, radius a.        off it : X = sqrt(a^2 + X0^2)
    HINGES  : X = 2a  =>  X0 = +- sqrt(3) a. They sit ABOVE and BELOW the equator, at radius 2a.

THE RULE (computed): a null ruling through the equator at azimuth th reaches X = 2a at azimuth th +- 60.
    family A : (th-60, BELOW)  <->  equator th  <->  (th+60, ABOVE)
    family B : (th+60, BELOW)  <->  equator th  <->  (th-60, ABOVE)
=> hinges connect to hinges 120 apart, ALTERNATING above/below. The cycle closes in six:

    hinge(  0,above) -[equator  60]- hinge(120,below) -[equator 180]- hinge(240,above)
    hinge(240,above) -[equator 300]- hinge(  0,below) -[equator  60]- hinge(120,above)
    hinge(120,above) -[equator 180]- hinge(240,below) -[equator 300]- hinge(  0,above)

*** A CLOSED SKEW HEXAGON -- P13's own words: "the A2 skeleton the slicing paper realises
    geometrically as a SKEW HEXAGON OF NULL RULINGS". SIX HINGES (azimuth 0,120,240, each above AND
    below); SIX EDGES; and they pass through only THREE equator points (60,180,300), EACH USED TWICE. ***

*** AND THE IDENTIFICATION ***
    HINGES    at azimuth   0, 120, 240  =  the REAL-tau~ rays      = face 2 = THE THREE SHEETS
    CROSSINGS at azimuth  60, 180, 300  =  the IMAGINARY-tau~ rays = face 4 = THE LIFT
    The flattened hexagon of the ray map IS THE EQUATOR. Its two triplets are the HINGES and the
    CROSSINGS -- and they are exactly the two tau~-characters. The A2 hexagon is not a diagram drawn
    on the geometry; it IS the hinge/crossing structure of the substrate's own null rulings.

STATUS: the GEOMETRY here is computed and exact (the hinge positions, the +-60 rule, the closed skew
hexagon, the three-crossings-twice). The COLOURING is unseated conjecture, carried over from the ray
map, and is NOT derived. [6*] stands: no face settles it. THE RHYME STAYS A RHYME.
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
al = 1.0; H = np.sqrt(3)*al                      # hinge height
RAYCOL = {0:PURPLE, 60:BLUE, 120:RED, 180:PURPLE, 240:BLUE, 300:RED}
def P(az, X0):                                    # a point on the hyperboloid at azimuth az, height X0
    R = np.sqrt(al**2 + X0**2)
    return np.array([R*np.cos(np.deg2rad(az)), R*np.sin(np.deg2rad(az)), X0])

fig = plt.figure(figsize=(16.6, 8.4))

# ================= LEFT: the skew hexagon on the substrate =================
ax = fig.add_subplot(1,2,1, projection='3d')
zz = np.linspace(-2.0, 2.0, 40); ph = np.linspace(0, 2*np.pi, 80)
ZZ, PH = np.meshgrid(zz, ph); RR = np.sqrt(al**2 + ZZ**2)
ax.plot_wireframe(RR*np.cos(PH), RR*np.sin(PH), ZZ, rstride=8, cstride=5, color='0.86', lw=0.5)
th = np.linspace(0, 2*np.pi, 200)
ax.plot(al*np.cos(th), al*np.sin(th), 0*th, color='0.45', lw=2.2)          # the equator

EDGES = [((0,+H),( 60),(120,-H)), ((120,-H),(180),(240,+H)), ((240,+H),(300),(  0,-H)),
         ((0,-H),( 60),(120,+H)), ((120,+H),(180),(240,-H)), ((240,-H),(300),(  0,+H))]
for (a1,h1), eq, (a2,h2) in EDGES:
    p1, p2 = P(a1,h1), P(a2,h2); c = RAYCOL[eq]
    L = np.linspace(0,1,60)[:,None]*(p2-p1) + p1
    ax.plot(L[:,0], L[:,1], L[:,2], color=c, lw=3.0, alpha=0.95)
    assert abs(np.hypot(*((p1+p2)/2)[:2]) - al) < 1e-9                     # midpoint IS on the equator
for eq in (60,180,300):                                                     # the three crossings
    p = P(eq,0); ax.scatter(*p, color=RAYCOL[eq], s=95, zorder=9, edgecolor='k', linewidth=0.6)
    ax.text(p[0]*1.28, p[1]*1.28, 0.16, f'${eq}^\\circ$', fontsize=9.5, color=RAYCOL[eq], ha='center')
for az in (0,120,240):                                                      # the six hinges
    for h,lb in ((+H,'above'),(-H,'below')):
        p = P(az,h); ax.scatter(*p, color=RAYCOL[az], s=170, marker='D', zorder=10, edgecolor='k', linewidth=0.7)
        ax.text(p[0]*1.13, p[1]*1.13, p[2]+0.22*np.sign(h), f'${az}^\\circ$\n{lb}', fontsize=8.5, color=RAYCOL[az], ha='center')
ax.scatter([0],[0],[0], color='k', s=26)
ax.set_xlim(-2.3,2.3); ax.set_ylim(-2.3,2.3); ax.set_zlim(-2.3,2.3)
ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
ax.set_xlabel('$X_1$', labelpad=-8, fontsize=9); ax.set_ylabel('$X_2$', labelpad=-8, fontsize=9)
ax.set_zlabel('$X_0$', labelpad=-8, fontsize=9)
ax.view_init(elev=17, azim=-58); ax.set_box_aspect((1,1,1), zoom=1.10)
ax.set_title('THE SKEW HEXAGON on the substrate\nsix hinges ($\\diamond$) at $X=2\\alpha$, $X_0=\\pm\\sqrt{3}\\alpha$ · six null rulings ·\n'
             'three equator crossings ($\\bullet$), EACH USED TWICE', fontsize=11, pad=-16)

# ================= RIGHT: the ray map, now read as hinges + crossings =================
ax2 = fig.add_subplot(1,2,2)
ax2.add_artist(plt.Circle((0,0),1.0,fill=False,color='0.5',lw=2.0))
ax2.plot([np.cos(np.deg2rad(t)) for t in range(0,361,60)],[np.sin(np.deg2rad(t)) for t in range(0,361,60)],
         color='0.8',lw=1.2,ls=(0,(6,4)),zorder=1)
for az in (0,120,240):                                        # HINGE directions -- real tau~
    x,y = 1.62*np.cos(np.deg2rad(az)), 1.62*np.sin(np.deg2rad(az))
    ax2.plot([0,x],[0,y], color=RAYCOL[az], lw=5.5, zorder=3)
    ax2.plot(x,y,'D',color=RAYCOL[az],ms=15,zorder=4,markeredgecolor='k',markeredgewidth=0.7)
    ax2.annotate('$'+str(az)+'^\\circ$ HINGES\\n$X_0=\\pm\\sqrt{3}\\alpha$, $X=2\\alpha$\\n$\\tilde\\tau$ REAL - face 2 - the sheets',
                 (x,y), xytext=(1.42*np.cos(np.deg2rad(az)),1.42*np.sin(np.deg2rad(az))),
                 ha='center', va='center', fontsize=8, color='0.1',
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=RAYCOL[az], lw=1))
for eq in (60,180,300):                                       # CROSSING directions -- imaginary tau~
    x,y = np.cos(np.deg2rad(eq)), np.sin(np.deg2rad(eq))
    ax2.plot([0,x],[0,y], color=RAYCOL[eq], lw=3.0, ls=(0,(5,3)), zorder=3)
    ax2.plot(x,y,'o',color=RAYCOL[eq],ms=13,zorder=4,markeredgecolor='k',markeredgewidth=0.6)
    ax2.annotate('$'+str(eq)+'^\\circ$ CROSSINGS\\n$X=\\alpha$ (the equator)\\n$\\tilde\\tau$ IMAGINARY - face 4 - the lift',
                 (x,y), xytext=(0.60*np.cos(np.deg2rad(eq)),0.60*np.sin(np.deg2rad(eq))),
                 ha='center', va='center', fontsize=8, color='0.1',
                 bbox=dict(boxstyle='round,pad=0.3', fc='white', ec=RAYCOL[eq], lw=1))
ax2.plot(0,0,'o',color='k',ms=9,zorder=5)
ax2.set_aspect('equal'); ax2.set_xlim(-2.15,2.15); ax2.set_ylim(-2.35,2.05); ax2.axis('off')
ax2.set_title('the $A_2$ hexagon, read on the substrate\nits TWO TRIPLETS are the HINGES and the CROSSINGS', fontsize=11.5, pad=6)
ax2.text(0,-2.28,'the flattened hexagon of the ray map IS THE EQUATOR. Its two triplets are exactly the two $\\tilde\\tau$-characters:\n'
         'REAL $\\tilde\\tau$ $\\rightarrow$ the hinge directions · IMAGINARY $\\tilde\\tau$ $\\rightarrow$ the crossing directions.\n'
         'The $A_2$ hexagon is not a diagram drawn ON the geometry — it IS the hinge/crossing structure of the substrate\'s own null rulings.',
         ha='center', va='bottom', fontsize=9, color='0.15')

fig.suptitle("Daryl's P13/P14 conjecture — THE HINGES.  The hexagon was flattened: it is the EQUATOR. The hinges live at $X_0=\\pm\\sqrt{3}\\alpha$, $X=2\\alpha$,\n"
             "and the null rulings close a SKEW HEXAGON through three equator crossings, each used twice — the two-up-one-down.",
             fontsize=13, y=0.99)
plt.tight_layout(rect=[0,0,1,0.90])
plt.savefig('daryl_p13p14_HINGES.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_HINGES.png', dpi=150, bbox_inches='tight')
print('skew hexagon verified: every edge midpoint lies EXACTLY on the equator (radius alpha).')
print('hinges: azimuth 0,120,240 at X0=+-sqrt3 a  = the REAL-tau~ rays  (face 2, the sheets)')
print('crossings: azimuth 60,180,300 at X=a       = the IMAG-tau~ rays  (face 4, the lift)')
