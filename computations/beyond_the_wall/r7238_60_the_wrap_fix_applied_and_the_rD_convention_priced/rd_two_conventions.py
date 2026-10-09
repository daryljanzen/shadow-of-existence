import os, sys, numpy as np, importlib.util
ROOT='/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT,'storyboard_receipts'))
spec = importlib.util.spec_from_file_location('cc', os.path.join(ROOT,'receipts','P15_CR_cosmology','P15_the_damping_signature_error_budget_and_the_convention_dominates_it.py'))
# the receipt runs on import; instead replicate machinery by exec'ing only its definition
src = open(spec.origin, encoding='utf-8').read()
i = src.index('def machinery('); j = src.index('\ndef budget') if '\ndef budget' in src else src.index('\nbase = machinery')
head = src[:src.index('print(__doc__')] + src[src.index('C = 299792.458'):src.index('def machinery(')]
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total
g = {'__name__':'cc','__file__':spec.origin, 'xe_history':xe_history, 'n_H0_of':n_H0_of,
     'sigT':sigT, 'Mpc_m':Mpc_m, 'xe_total':xe_total, 'np':__import__('numpy'),
     'os':__import__('os'), 'sys':__import__('sys')}
exec(compile(head + src[i:j], 'cc(machinery)', 'exec'), g)
machinery = g['machinery']
CASES = (('arm     (cr)',   dict(H0=68.60, Om=0.2973, Ombh2=0.0224, z_rec=1090.2, leaf_clock=True,  radiation_in_rate=False)),
         ('control (lcdm)', dict(H0=67.40, Om=0.3150, Ombh2=0.0224, z_rec=1089.0, leaf_clock=True,  radiation_in_rate=True)))
out={}
for nm,kw in CASES:
    m = machinery(**kw)
    rd_rec = m['r_D'](m['a_rec']); rd_vis = m['r_D'](m['a_vis'])
    out[nm]=(rd_rec, rd_vis, m['a_rec'], m['a_vis'])
    print(f"  {nm}: a_rec={m['a_rec']:.6e} (z={1/m['a_rec']-1:.1f})  a_vis={m['a_vis']:.6e} (z={1/m['a_vis']-1:.1f})")
    print(f"  {'':14s}  r_D to RECOMBINATION = {rd_rec:7.4f} Mpc    r_D to VISIBILITY PEAK = {rd_vis:7.4f} Mpc"
          f"    swing {100*(rd_rec/rd_vis-1):+.2f}%")
a, c = out['arm     (cr)'], out['control (lcdm)']
print()
print(f"  the ARM's own r_D moves {100*(a[0]/a[1]-1):+.2f}% between conventions; the CONTROL's {100*(c[0]/c[1]-1):+.2f}%")
