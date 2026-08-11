"""DARYL'S P13/P14 CONJECTURE -- THE RHYME BOARD.
*** THIS IS NOT A RESULT. IT IS A COLLECTION OF RHYMES, MARKED AS RHYMES. ***
Each panel states what the geometry ACTUALLY gives (left, in black) and what it RHYMES with
(right, in grey), plus WHAT IT WOULD TAKE to promote the rhyme. Nothing here is asserted.
Built at Daryl's request (r1083): "collect that up visually and descriptively and openly without
worrying about rigour ... and then give an honest idea of what the conjecture might be saying."
"""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
import matplotlib.colors as mc
plt.rcParams.update({'font.family':'serif','font.size':11,'mathtext.fontset':'cm'})
BLUE, RED = '#2471a3', '#c0392b'
PURPLE = tuple((np.array(mc.to_rgb(RED)) + np.array(mc.to_rgb(BLUE)))/2)
GREY = '0.42'
fig = plt.figure(figsize=(16.5, 10.6))
gs = fig.add_gridspec(2, 3, hspace=0.30, wspace=0.22)

def head(ax, t, sub):
    ax.set_title(t, fontsize=12.5, pad=8, fontweight='bold')
    ax.text(0.5, 1.005, sub, transform=ax.transAxes, ha='center', va='bottom', fontsize=8.5, color=GREY)

# ---- 1. THE HEXAGON ----
ax = fig.add_subplot(gs[0,0])
for th in range(0,360,60):
    c = PURPLE if th%180==0 else (BLUE if th in (60,240) else RED)
    x,y = np.cos(np.deg2rad(th)), np.sin(np.deg2rad(th))
    ax.plot([0,x],[0,y], color=c, lw=4.5); ax.plot(x,y,'o',color=c,ms=10)
    ax.annotate(f'${th}^\\circ$',(x,y),xytext=(1.24*x,1.24*y),ha='center',va='center',fontsize=9)
ax.plot([np.cos(np.deg2rad(t)) for t in range(0,361,60)],[np.sin(np.deg2rad(t)) for t in range(0,361,60)],
        color='0.8',lw=1,ls=(0,(5,4)))
ax.plot(0,0,'o',color='k',ms=8); ax.set_aspect('equal'); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.55,1.45); ax.axis('off')
head(ax,'the hexagon','GEOMETRY: $\\arg r$ from "is $\\tilde\\tau$ real or imaginary"')
ax.text(0,-1.5,'RHYMES WITH: the six roots of $A_2$ — the root system of $\\mathfrak{su}(3)$, i.e. COLOUR.\n'
        'TO PROMOTE: $\\mathfrak{su}(3)\\not\\subset\\mathfrak{so}(5,1)$ (P13). So it can be a Weyl\n'
        'SHADOW at most — the corpus already says exactly this, and calls it necessary, not sufficient.',
        ha='center',va='top',fontsize=8.2,color=GREY)

# ---- 2. THE 1/3 - 2/3 ----
ax = fig.add_subplot(gs[0,1])
th1 = np.linspace(0,120,200); th2 = np.linspace(120,360,300)
ax.plot(np.cos(np.deg2rad(th1)),np.sin(np.deg2rad(th1)),color=BLUE,lw=6)
ax.plot(np.cos(np.deg2rad(th2)),np.sin(np.deg2rad(th2)),color=RED,lw=6)
ax.annotate('$120^\\circ=\\frac{1}{3}$',(np.cos(np.deg2rad(60)),np.sin(np.deg2rad(60))),
            xytext=(0.62,0.86),fontsize=11,color=BLUE)
ax.annotate('$240^\\circ=\\frac{2}{3}$',(np.cos(np.deg2rad(240)),np.sin(np.deg2rad(240))),
            xytext=(-0.95,-0.95),fontsize=11,color=RED)
ax.plot(0,0,'o',color='k',ms=8); ax.set_aspect('equal'); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.55,1.45); ax.axis('off')
head(ax,'the $1/3$ – $2/3$ split','GEOMETRY: the wrap, before and after $r=0$')
ax.text(0,-1.5,'RHYMES WITH: the quark charges. $d=-\\frac{1}{3}$, $u=+\\frac{2}{3}$.\n'
        '$p=uud=\\frac{2}{3}+\\frac{2}{3}-\\frac{1}{3}=+1$ · $n=udd=0$.\n'
        'TO PROMOTE: needs a reason the wrap FRACTION is a CHARGE. None here. The\n'
        'geometry gives an angle; charge is $Q\\mapsto-Q$, which the metric cannot even see.',
        ha='center',va='top',fontsize=8.2,color=GREY)

# ---- 3. ONE + TWO ----
ax = fig.add_subplot(gs[0,2])
for th,c,lb in [(0,BLUE,'$0^\\circ$'),(120,RED,'$120^\\circ$'),(240,RED,'$240^\\circ$')]:
    x,y = np.cos(np.deg2rad(th)), np.sin(np.deg2rad(th))
    ax.plot([0,x],[0,y],color=c,lw=5); ax.plot(x,y,'o',color=c,ms=11)
    ax.annotate(lb,(x,y),xytext=(1.26*x,1.26*y),ha='center',va='center',fontsize=9)
ax.plot(0,0,'o',color='k',ms=8); ax.set_aspect('equal'); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.55,1.45); ax.axis('off')
head(ax,'one $+$ two','GEOMETRY: the 3 sheets on the real-$r$ slice: 1 blue, 2 red')
ax.text(0,-1.5,'RHYMES WITH: $uud$ — two of one, one of the other. Also: 3 generations;\n'
        'also 3 colours. The corpus reads $\\mathrm{Aut}(A_2)=S_3\\times\\mathbb{Z}_2$ as\n'
        '3 generations $\\times$ 2 chiralities — as a CONJECTURE, asserted nowhere as more.\n'
        'TO PROMOTE: the 1+2 is an artifact of taking $r$ REAL. Off that slice all three\n'
        'sheets are alike. §9 U-AutA$_2$ already showed sheets $\\neq$ generations.',
        ha='center',va='top',fontsize=8.2,color=GREY)

# ---- 4. THE BROKEN DUALITY ----
ax = fig.add_subplot(gs[1,0])
for th in range(0,360,60):
    x,y=0.62*np.cos(np.deg2rad(th)),0.62*np.sin(np.deg2rad(th))
    ax.plot([0,x],[0,y],color='0.55',lw=2.6)
ax.text(0,0.86,'complex $r$\nSIX RAYS',ha='center',fontsize=9.5,color='0.2')
ax.add_patch(plt.Rectangle((1.35,-0.42),1.5,0.84,fc=PURPLE,alpha=0.22,ec=PURPLE,lw=1.4))
ax.plot([1.35,2.85],[0,0],color='0.55',lw=2.6)
ax.text(2.1,0.86,'complex $\\tilde\\tau$\nA STRIP, width $2\\pi\\alpha/3$',ha='center',fontsize=9.5,color='0.2')
ax.text(1.05,0,'$\\neq$',ha='center',va='center',fontsize=22,color='#8a2b2b')
ax.set_xlim(-0.95,3.1); ax.set_ylim(-1.5,1.25); ax.axis('off')
head(ax,'the broken duality  (\*)','GEOMETRY: colour-dual, structure-NOT')
ax.text(1.05,-0.62,'The two planes are EXACTLY dual in the colouring (each face is all-purple\n'
        'under the rule of the variable it pins). But the THREE-FOLDNESS lives only in $r$ —\n'
        'it IS the cube root $r^3=2M\\alpha^2\\sinh^2$. $\\tilde\\tau$ has no hexagon, only a strip.\n'
        '$\\Rightarrow$ THIS IS THE ONLY THING DISTINGUISHING $r$ FROM $\\tilde\\tau$ AT ALL.\n'
        'It is also what forbids smooth passage on face 2 ($120^\\circ\\neq180^\\circ$).',
        ha='center',va='top',fontsize=8.2,color=GREY)

# ---- 5. THE NUMBERS ----
ax = fig.add_subplot(gs[1,1]); ax.axis('off')
head(ax,'the numbers that are exact','GEOMETRY: derived, receipted, not rhymes')
rows = [('$\\mathrm{arccosh}\\,2 = 2\\,\\mathrm{arcsinh}\\frac{1}{\\sqrt{2}}$','the two seams sit $2\\!:\\!1$ in cosmic time'),
        ('$K=\\frac{12}{\\alpha^4}\\!\\left(\\sinh^{-4}\\!\\frac{3\\tilde\\tau}{2\\alpha}+2\\right)$','$M$ CANCELS — the singularity is $M$-free'),
        ('$A=\\sqrt[3]{2}\\,\\alpha/\\sqrt{3}$','turnaround $=\\sqrt[3]{2}\\times$ seam'),
        ('$r\\simeq A(3s\\!/2)^{2/3}$','ONE exponent gives the vertical tangent AND $K\\sim s^{-4}$'),
        ('$|r|\\leq A$ on face 4','the lift is BOUNDED and CLOSES, period $4\\pi\\alpha/3$')]
for i,(a,b) in enumerate(rows):
    y = 0.86 - i*0.185
    ax.text(0.02,y,a,fontsize=11.5); ax.text(0.02,y-0.072,b,fontsize=8.5,color=GREY)
ax.text(0.02,-0.06,'These are the parts that are NOT rhymes. They are computed and receipted.\n'
        'Note what they have in common: they are all about $\\alpha$ and the $2/3$ power.\n'
        'None of them mentions charge, colour, generation, or mass.',
        fontsize=8.5,color='#2f5d3a',va='top')

# ---- 6. THE HONEST LEDGER ----
ax = fig.add_subplot(gs[1,2]); ax.axis('off')
head(ax,'what the conjecture might be saying','and what it is NOT saying')
ax.text(0.02,0.90,'IF it holds:', fontsize=10.5, fontweight='bold')
ax.text(0.02,0.79,'the $r=0$ crossing is ONE conjugation event, and the\n'
        'cosmogenesis, pair production and annihilation are THREE\n'
        'WALKS ON IT. Not three things that resemble each other —\n'
        'one object, read at three scales. "$C$" would then factorise\n'
        'into two GEOMETRIC faces ($R$ linear, $\\tilde\\tau\\!\\leftrightarrow\\!\\bar{\\tilde\\tau}$ antilinear),\n'
        'with only the charge SIGN left at field level.',
        fontsize=8.6, va='top')
ax.text(0.02,0.40,'IT IS NOT SAYING:', fontsize=10.5, fontweight='bold', color='#8a2b2b')
ax.text(0.02,0.31,'that our universe is an electron. That $\\mathfrak{su}(3)$ lives on $dS_5$\n'
        '(it cannot: P13, and the corpus says so). That the sheets ARE\n'
        'generations (§9 showed they are not). That any of this is derived.',
        fontsize=8.6, va='top', color='#8a2b2b')
ax.text(0.02,0.06,'THE ONE THING THAT WOULD DECIDE IT:\n'
        'work $\\mathbb{C}_r\\times\\mathbb{C}_{\\tilde\\tau}$ WHOLE. Every face kills the colour\n'
        'information of the variable it pins. That is why no picture here —\n'
        'however striking — is evidence. [6*] · arc A3.',
        fontsize=8.6, va='top', color='#2f5d3a')

fig.suptitle("Daryl's P13/P14 conjecture — THE RHYME BOARD.   Marked as rhymes, not results: what the geometry gives, what it rhymes with, and what each would take to promote.",
             fontsize=12.5, y=0.975)
plt.savefig('daryl_p13p14_RHYME_BOARD.pdf', bbox_inches='tight')
plt.savefig('daryl_p13p14_RHYME_BOARD.png', dpi=150, bbox_inches='tight')
print('rhyme board built: 3 rhymes, 1 structural break, the exact numbers, the honest ledger.')
