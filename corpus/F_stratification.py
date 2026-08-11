"""The causal stratification of the cosmogenetic contour: five spans, four characters, three joints.
Chalkboard-simple by design -- the algebra of P5 and the physics of P7 land on one picture."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
a=1.0; M=a/(3*np.sqrt(3)); f=lambda r: 1-2*M/r-r*r/a**2
A=(2*M*a**2)**(1/3); rN=a/np.sqrt(3); rB=-2*a/np.sqrt(3)
fig,ax=plt.subplots(figsize=(11,4.4))
spans=[(-2.0,rB,'#c44','collapse horn','timelike | real'),
       (rB,-A,'#4a7','seam $\\to$ turnaround','spacelike | real'),
       (-A,0.0,'#48c','the lift','spacelike | IMAGINARY'),
       (0.0,rN,'#c44','$r=0\\ \\to$ front seam','timelike | real'),
       (rN,1.9,'#c44','cosmological horn','timelike | real')]
for x0,x1,c,lab,ch in spans:
    ax.add_patch(Rectangle((x0,0),x1-x0,1,facecolor=c,alpha=.28,edgecolor='none'))
    ax.text((x0+x1)/2,.72,lab,ha='center',fontsize=8.5,weight='bold')
    ax.text((x0+x1)/2,.52,ch,ha='center',fontsize=7.6,style='italic')
for r,lab,note in ((rB,'back seam','timelike$\\to$spacelike'),(-A,'turnaround','real$\\to$imaginary'),
                   (0.0,'branch point','BOTH, through $\\infty$')):
    ax.axvline(r,color='k',lw=2.2,zorder=5)
    ax.text(r,1.14,lab,ha='center',fontsize=9,weight='bold')
    ax.text(r,1.045,note,ha='center',fontsize=7.4)
ax.axvline(rN,color='k',lw=1.4,ls=(0,(4,3)),zorder=5)
ax.text(rN,1.14,'front seam',ha='center',fontsize=9)
ax.text(rN,1.045,'unit speed, NO change',ha='center',fontsize=7.4,style='italic')
ax.annotate('',xy=(rN,.20),xytext=(1.9,.20),arrowprops=dict(arrowstyle='<->',color='#a22',lw=1.3))
ax.annotate('',xy=(0.0,.20),xytext=(rN,.20),arrowprops=dict(arrowstyle='<->',color='#a22',lw=1.3))
ax.text((0+1.9)/2,.10,'ONE causal character: the front seam does not divide',
        ha='center',fontsize=8,color='#a22',weight='bold')
for r,m in ((rB,'o'),(-0.344142,'D'),(rN,'o')):
    ax.plot(r,1.30,m,ms=7,color='k',zorder=6)
ax.text(-0.344142,1.38,'Euclidean null',ha='center',fontsize=7.6)
ax.text(-1.97,1.44,'$|\\mathrm{d}r/\\mathrm{d}s|=1$ met three times (L8.4)',fontsize=7.6,style='italic')
ax.set_xlim(-2.0,1.9); ax.set_ylim(0,1.56); ax.set_yticks([])
ax.set_xticks([rB,-A,0,rN]); ax.set_xticklabels(['$-2\\alpha/\\sqrt{3}$','$-(2)^{1/3}\\alpha/\\sqrt{3}$','$0$','$+\\alpha/\\sqrt{3}$'])
ax.set_xlabel('$r/\\alpha$'); ax.set_title('FIVE spans, FOUR characters, THREE joints',fontsize=11,weight='bold')
for sp in ('top','right','left'): ax.spines[sp].set_visible(False)
plt.tight_layout(); plt.savefig('F_stratification.png',dpi=170)
print('  figure written: F_stratification.png')
