import re, os, sys, glob
ROOT='/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT,'corpus'))
import importlib.util
spec=importlib.util.spec_from_file_location('cqp', os.path.join(ROOT,'corpus','check_quote_pins.py'))
m=importlib.util.module_from_spec(spec)
sys.modules['cqp']=m
try: spec.loader.exec_module(m)
except SystemExit: pass
_unmark=m._unmark
def body(f):
    b='\n'.join(l for l in open(f,encoding='utf-8',errors='replace').read().split('\n') if not l.lstrip().startswith('%'))
    j=b.find('\\begin{thebibliography}'); return b[:j] if j>0 else b
p15=_unmark(re.sub(r'\s+',' ',body(os.path.join(ROOT,'corpus','CR_cosmology.tex'))))
# every literal/locator my 14 repairs read against CR_cosmology
SPANS=[
 ('C15','geometric rate gives a diffusion length'),('C15','10.8'),
 ('C16','302.2'),('C16','301'),
 ('C19/C21','progenitor-supplied content'),('C19/C21','transmits'),('C19/C21','imprinting'),
 ('C21','whose regular solution is elementary'),('C21',r'x=k\eta/\sqrt'),
 ('C38/C39','which the rate carries and the baryon-acoustic data fix'),('C38/C39',r'$\Omega_m=2/(x_{0}^{3}+2)$'),
 ('C40','against the measured'),
 ('C31/C33','the expansion rate, the matter and baryon densities and the tilt free in each arm'),
 ('C31/C33','the amplitude in closed form'),
 ('C30','the odd/even asymmetry is imprinted afterwards, on the expansion side at $R\\approx0.6$, which is ordinary content physics on the observable leg'),
 ('C30','the whole difference is carried by $H(a)$'),
 ('C28','returns $r_{s}=146.4$~Mpc against $145.4$ on the radiation-included rate---within $0.7\\%$ of each other'),
 ('C28','the common distance cancels'),('C28',r'$\theta_{D}/\theta_{*}$'),
 ('C22','The constancy argument runs on'),('C22',r'\emph{super-horizon} equation'),
 ('C29',r'\emph{contains no $k$ at all once $w=0$}'),('C29','on a radiation-free rate the problem is scale-free'),
 ('C34',r'\emph{The single-locus reading is not inside that trade}'),('C34','returns the first peak at $222$'),
]
print(f'{"receipt":10s} {"raw":>4s} {"unmarked":>8s}  span')
bad=[]
for who,s in SPANS:
    n=p15.count(_unmark(s)); raw=re.sub(r'\s+',' ',body(os.path.join(ROOT,'corpus','CR_cosmology.tex'))).count(s)
    flag='' if n==1 else '  <== NOT UNIQUE under the rule'
    if n!=1: bad.append((who,s,raw,n))
    print(f'{who:10s} {raw:4d} {n:8d}  {s[:58]!r}{flag}')
print(f'\nspans measured {len(SPANS)};  non-unique under the rule normalisation: {len(bad)}')
