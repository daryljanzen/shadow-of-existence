"""DARYL'S P13/P14 CONJECTURE -- THE PLATE. Everything, together, as one object.

ONE 4-D object: C_r x C_tau~, the bead r^3 = 2M a^2 sinh^2(3 tau~/2a).
TEN panels, one story, read top to bottom:

  ROWS 1-2  THE FOUR FACES, EACH DRAWN TWICE -- once per colouring rule.
            A face PINS one variable (r or tau~ real/imaginary). It therefore has NO quadrants in
            that variable, and must read colour off the OTHER one. So each face is ALL PURPLE under
            the rule of the variable it pins, and coloured under the other's. THE DUALITY IS EXACT.
            Every face is blind to exactly the variable it fixed.

  ROW 3     THE TWO MAPS -- the same ray map drawn once per rule, in each variable's own plane.
            WHAT IS A RAY ON ONE MAP IS A WHOLE FACE ON THE OTHER:
                r-plane   : 0/180 axis IS face 1  ;  90/270 axis IS face 3
                tau~-plane: 0/180 axis IS face 2  ;  90/270 axis IS face 4
            Each map turns its own two faces into its four purple axes.
            AND THE DUALITY BREAKS HERE, in exactly one place: the HEXAGON exists only on the r-map.
            The three-foldness is the cube root -- a property of r, not tau~. The tau~ plane carries
            a STRIP of width 2 pi a/3 instead. That break is the 1/3-2/3, and it is the only thing
            that distinguishes r from tau~ at all.

WHAT LIVES IN THE OBJECT (the readings are PATHS through it):
  the cosmological bead  = one bead, alone: red (r<0) through r=0, turning blue (r>0). Not purple:
                           nothing merges with it.
  pair production /      = two beads onto one track: a red and a blue arrive with opposite colours
  annihilation             -> red+blue = PURPLE. The merger IS the vertex. Reverse the arrows and
                           production becomes annihilation. One geometry.
  r = 0                  = where they all meet. ONE conjugation event: the single place where r AND
                           tau~ both vanish in real and imaginary parts. Asymmetric: Nariai, 1/3-2/3.

STILL FLATTENED (Daryl, r1084): the hexagon here is drawn in the r-plane. P13's own words are that
the A2 skeleton is realised as a SKEW HEXAGON OF NULL RULINGS -- and it MAPS OUT TO THE HINGES.
That is a further dimension this plate does not carry. TO BE PLOTTED.

*** STATUS: A CONJECTURE. Not derived. Not species = sign(r). No face and no map can settle it --
each destroys the colour information of the variable it pins, by construction. Only C_r x C_tau~
whole can. [6*] / arc A3. These pictures carry the conjecture; they do not test it. ***
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
from mpl_toolkits.mplot3d import Axes3D  # noqa
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
A = 2**(1/3)/np.sqrt(3); rmax = 2.4

def colour_of(z):
    x, y = z.real, z.imag
    if abs(x) < 1e-6 or abs(y) < 1e-6: return PURPLE
    return BLUE if x*y > 0 else RED

def face1():
    out=[]; rp=np.linspace(1e-4,rmax,200); sx=np.array([(2/3)*np.arcsinh((r/A)**1.5) for r in rp])
    rn=np.linspace(-1e-4,-rmax,260)
    def wing(r):
        u=abs(r/A)**1.5
        return (0.0,(2/3)*np.arcsin(u)) if u<=1 else ((2/3)*np.arccosh(u), np.pi/3)
    W=np.array([wing(r) for r in rn]); wx,wy=W[:,0],W[:,1]
    for ex,ey in [(+1,+1),(-1,+1),(-1,-1),(+1,-1)]:
        out.append((ex*wx+1j*ey*wy, rn+0j, ex*wx, ey*wy, rn))
    for e in (+1,-1): out.append((e*sx+0j, rp+0j, e*sx, 0*rp, rp))
    return out,(2,-2),(1.2,-1.2),(-rmax,rmax)
def face2():
    out=[]
    for t in (np.linspace(1e-4,2.0,200), np.linspace(-2.0,-1e-4,200)):
        for k in range(3):
            R=A*np.abs(np.sinh(1.5*t))**(2/3)*np.exp(2j*np.pi*k/3)
            out.append((t+0j, R, t, R.real, R.imag))
    return out,(2,-2),(1.9,-1.9),(-1.9,1.9)
def face3():
    out=[]
    def ty(y,sg):
        u=(abs(y)/A)**1.5; z=sg*u*np.exp(-1j*np.pi/4) if y>0 else sg*u*np.exp(+1j*np.pi/4)
        return (2/3)*np.arcsinh(z)
    for sg in (+1,-1):
        for ys in (np.linspace(1e-4,1.8,200), np.linspace(-1.8,-1e-4,200)):
            T=np.array([ty(y,sg) for y in ys]); out.append((T, 1j*ys, T.real, T.imag, ys))
    return out,(1.9,-1.9),(1.1,-1.1),(-1.9,1.9)
def face4():
    out=[]
    for s in (np.linspace(1e-4,2*np.pi/3,260), np.linspace(-2*np.pi/3,-1e-4,260)):
        for d in (60,180,300):
            R=A*np.abs(np.sin(1.5*s))**(2/3)*np.exp(1j*np.deg2rad(d))
            out.append((1j*s, R, s, R.real, R.imag))
    return out,(2.2,-2.2),(0.95,-0.95),(-0.95,0.95)

FACES=[('face 1  ·  $r$ REAL','$\\arg r=0,180$ · 6 branches $=$ 4 beads $+$ 2 mergers',face1),
       ('face 2  ·  $\\tilde\\tau$ REAL','$\\arg r=0,120,240$ · the three sheets',face2),
       ('face 3  ·  $r$ IMAGINARY','$\\arg r=90,270$ · transverse, between the rays',face3),
       ('face 4  ·  $\\tilde\\tau$ IMAGINARY','$\\arg r=60,180,300$ · THE LIFT: $|r|\\leq A$, closes',face4)]

fig = plt.figure(figsize=(19, 15.2))
gs = fig.add_gridspec(3, 4, height_ratios=[1,1,1.28], hspace=0.14, wspace=0.02)

for row, rule in enumerate(['r','tau']):
    for ci,(nm,sub,fn) in enumerate(FACES):
        ax = fig.add_subplot(gs[row,ci], projection='3d')
        branches, xl, yl, zl = fn()
        for T,R,x,y,z in branches:
            n=len(np.atleast_1d(z)); T=np.atleast_1d(T)*np.ones(n); R=np.atleast_1d(R)*np.ones(n)
            x=np.atleast_1d(x)*np.ones(n); y=np.atleast_1d(y)*np.ones(n); z=np.atleast_1d(z)
            C=[colour_of(R[i] if rule=='r' else T[i]) for i in range(n)]
            for i in range(n-1): ax.plot(x[i:i+2],y[i:i+2],z[i:i+2],color=C[i],lw=2.7)
        ax.scatter([0],[0],[0],color='k',s=30,zorder=10)
        ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_zlim(*zl)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
        ax.view_init(elev=16,azim=-60); ax.set_box_aspect((1,1,1),zoom=1.30)
        allp = ((rule=='r' and ci in (0,2)) or (rule=='tau' and ci in (1,3)))
        ax.set_title((nm if row==0 else '') + ('\n' + sub if row==0 else '') +
                     ('\n' if row==0 else '') + ('ALL PURPLE' if allp else 'coloured'),
                     fontsize=8.6, pad=-16, color=('#5a3a6a' if allp else '0.35'))
fig.text(0.008,0.845,'coloured by the\n$r$-RULE\n\npurple $\\Leftrightarrow$ $r$ real\nor purely imaginary',fontsize=10,color='0.15',va='center')
fig.text(0.008,0.545,'coloured by the\n$\\tilde\\tau$-RULE\n\npurple $\\Leftrightarrow$ $\\tilde\\tau$ real\nor purely imaginary',fontsize=10,color='0.15',va='center')

# ---------------- ROW 3: the two maps ----------------
def col(th):
    t=th%360
    return PURPLE if t%90==0 else (BLUE if (0<t<90 or 180<t<270) else RED)
axL = fig.add_subplot(gs[2,0:2])
axL.add_artist(plt.Circle((0,0),1.0,fill=False,color='0.88',lw=1))
axL.plot([np.cos(np.deg2rad(t)) for t in range(0,361,60)],[np.sin(np.deg2rad(t)) for t in range(0,361,60)],
         color='0.78',lw=1.2,ls=(0,(6,4)),zorder=1)
FC={0:'face 2',60:'face 4',90:'face 3',120:'face 2',180:'face 4',240:'face 2',270:'face 3',300:'face 4'}
CH={0:'real',60:'imag',90:'cplx',120:'real',180:'imag',240:'real',270:'cplx',300:'imag'}
for th in [0,60,90,120,180,240,270,300]:
    c=col(th); hx=(th%60==0); x,y=np.cos(np.deg2rad(th)),np.sin(np.deg2rad(th))
    axL.plot([0,x],[0,y],color=c,lw=5.5 if hx else 2.6,ls='-' if hx else (0,(4,3)),zorder=3)
    axL.plot(x,y,'o' if hx else 's',color=c,ms=12 if hx else 7,zorder=4)
    axL.annotate(f'${th}^\\circ$\n$\\tilde\\tau$ {CH[th]}\n{FC[th]}',(x,y),xytext=(1.33*x,1.33*y),
                 ha='center',va='center',fontsize=8,color='0.15')
axL.plot(0,0,'o',color='k',ms=9,zorder=5); axL.annotate('$r=0$',(0,0),xytext=(0.09,-0.15),fontsize=9.5)
axL.set_aspect('equal'); axL.set_xlim(-1.85,1.85); axL.set_ylim(-1.95,1.75); axL.axis('off')
axL.set_title('the $r$-MAP — the complex $r$ plane.   THE HEXAGON LIVES HERE (solid): the six $A_2$ roots.\n'
              'the $0/180^\\circ$ axis IS face 1 · the $90/270^\\circ$ axis IS face 3', fontsize=10.5, pad=2)
axL.text(0,-1.88,'purple $\\Leftrightarrow$ $\\arg r$ on an axis $\\Leftrightarrow$ $r$ real or purely imaginary',
         ha='center',fontsize=9,color='0.25')

axR = fig.add_subplot(gs[2,2:4])
axR.axhline(0,color=PURPLE,lw=5.5,zorder=3); axR.axvline(0,color=PURPLE,lw=5.5,zorder=3)
for sg in (+1,-1):
    y=sg*np.pi/3
    axR.plot([-1.85,0],[y,y],color=(RED if sg>0 else BLUE),lw=3.2,zorder=2)
    axR.plot([0,1.85],[y,y],color=(BLUE if sg>0 else RED),lw=3.2,zorder=2)
axR.fill_between([-1.85,1.85],-np.pi/3,np.pi/3,color=PURPLE,alpha=0.07,zorder=0)
axR.plot(0,0,'o',color='k',ms=9,zorder=5); axR.annotate('$\\tilde\\tau=0$',(0,0),xytext=(0.10,-0.17),fontsize=9.5)
axR.annotate('$\\mathrm{Im}\\,\\tilde\\tau=0$ · $r$ real $>0$ · face 2 (the sheets)',(1.8,0),xytext=(1.78,-0.16),ha='right',fontsize=8)
axR.annotate('$\\mathrm{Re}\\,\\tilde\\tau=0$ · THE LIFT · face 4',(0,1.5),xytext=(0.08,1.48),fontsize=8)
for sg in (+1,-1):
    axR.annotate(f'$\\mathrm{{Im}}\\,\\tilde\\tau={"+" if sg>0 else "-"}\\pi\\alpha/3$ · $r$ real $<0$ · face 1 legs',
                 (1.8,sg*np.pi/3),xytext=(1.78,sg*np.pi/3+0.10*sg),ha='right',fontsize=8)
for q,(x,y) in {'Q1':(1.15,0.68),'Q2':(-1.15,0.68),'Q3':(-1.15,-0.68),'Q4':(1.15,-0.68)}.items():
    axR.text(x,y,q,fontsize=10.5,color=(BLUE if q in ('Q1','Q3') else RED),ha='center',alpha=0.8)
axR.set_aspect('equal'); axR.set_xlim(-1.85,1.85); axR.set_ylim(-1.95,1.75)
axR.set_xticks([-1,0,1]); axR.set_yticks([-np.pi/3,0,np.pi/3]); axR.set_yticklabels(['$-\\pi/3$','$0$','$+\\pi/3$'])
axR.tick_params(labelsize=8)
for sp in ('top','right'): axR.spines[sp].set_visible(False)
axR.set_title('the $\\tilde\\tau$-MAP — the complex $\\tilde\\tau$ plane.   NO HEXAGON: a STRIP of width $2\\pi\\alpha/3$.\n'
              'the $0/180^\\circ$ axis IS face 2 · the $90/270^\\circ$ axis IS face 4', fontsize=10.5, pad=2)
axR.text(0,-1.88,'THE BREAK: the three-foldness IS the cube root $r^3=2M\\alpha^2\\sinh^2$ — it belongs to $r$, not $\\tilde\\tau$.\n'
         'Exact in colour, broken in structure. That break is the $1/3$–$2/3$, and it is the ONLY thing distinguishing $r$ from $\\tilde\\tau$.',
         ha='center',fontsize=8.6,color='#8a2b2b')

fig.suptitle("Daryl's P13/P14 conjecture — THE PLATE.   One 4-D object ($\\mathbb{C}_r\\times\\mathbb{C}_{\\tilde\\tau}$), four faces, two rules, two maps.\n"
             "Each face is ALL PURPLE under the rule of the variable it pins — the duality is exact — and it breaks in exactly one place: the hexagon is $r$'s alone.",
             fontsize=13.5, y=0.985)
plt.savefig('daryl_p13p14_THE_PLATE.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_THE_PLATE.png', dpi=140, bbox_inches='tight')
print('THE PLATE: 8 face-panels (4 faces x 2 rules) + 2 maps. One object, one story.')
