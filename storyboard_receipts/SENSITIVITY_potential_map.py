"""SENSITIVITY  --  a systematic derivative map of the Weyl potential (r2348).

WHY.  The 4.4% potential deficit against CAMB survived ten one-off tests, and reporting nulls
("not this, not that") is the wrong method: what matters is HOW FAR each dial moves the output,
and what it would take to close 4.4%.  A model whose dials do nothing is a broken measurement; a
model whose dials each do a little is a statement about leverage.  This builds the derivative map.

METHOD.  One dial at a time, +/- a stated fractional step, with the BACKGROUND READ BACK from the
module each run so we know the dial actually arrived.  Reported as a logarithmic sensitivity
    S = dln(Weyl) / dln(parameter)
at the k and eta where the deficit lives, so different dials are directly comparable.

READ IT AS.  |S| tells you the fractional change in the potential per fractional change in the
parameter.  To close a 4.4% gap with a dial of sensitivity S you need a fractional parameter change
of 0.044/|S| -- which for small |S| is a change large enough to be excluded by other data.
"""
import os
import subprocess
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
KS = (0.010, 0.035, 0.080)
ETAS = (10.0, 50.0, 200.0)

RUNNER = r'''
import os, sys, numpy as np
sys.path.insert(0, %r)
os.environ.setdefault('ESTORE','0.02'); os.environ.setdefault('STRIDE','1'); os.environ.setdefault('ETAEND','760')
import HIER_photon_hierarchy as H
kk = np.array(%r)
E, Y, esw = H.evolve(kk)
Hc  = np.array([float(H.Hc_of(e)) for e in E])
Onv = np.array([float(H.On_of(e)) for e in E])
Ogv = np.array([float(H.Og_of(e)) for e in E])
W = Y[:,:,2] - 3*(Hc**2)[:,None]*(Onv[:,None]*Y[:,:,3] + Ogv[:,None]*Y[:,:,4])/kk[None,:]**2
o = [float(np.interp(0.6, E, W[:,j])) for j in range(len(kk))]
res = np.array([[float(np.interp(et, E, W[:,j])/o[j]) for j in range(len(kk))] for et in %r])
np.savez(os.environ['OUTF'], res=res, Om=H.Om, Or=H.Or_content, fnu=H.fnu, esw=esw,
         ombh2=H.ombh2, Rb=H.Rb_rec)
''' % (HERE, KS, ETAS)

open('/tmp/_sens_run.py', 'w').write(RUNNER)


def run(tag, env):
    e = dict(os.environ)
    e.update(env)
    e['OUTF'] = '/tmp/_sens_%s.npz' % tag
    r = subprocess.run([sys.executable, '/tmp/_sens_run.py'], env=e, cwd=HERE,
                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=1200)
    if not os.path.exists(e['OUTF']):
        print("   FAILED %s: %s" % (tag, r.stderr.decode()[-200:]))
        return None
    return np.load(e['OUTF'])


# (label, env var, low factor, high factor, which background field to verify)
DIALS = [
    ("Omega_m",        'OMF',  0.90, 1.10, 'Om'),
    ("Omega_r",        'ORF',  0.90, 1.10, 'Or'),
    ("f_nu",           'FNU',  None, None, 'fnu'),      # absolute values, handled below
    ("omega_b",        'OBF',  0.90, 1.10, 'ombh2'),
    ("baryon loading", 'RBF',  0.90, 1.10, 'Rb'),
]

print("=" * 92)
print("SENSITIVITY MAP of the Weyl potential  --  S = dln(Weyl)/dln(param)")
print("=" * 92)

base = run('base', {})
if base is None:
    raise SystemExit("baseline failed")
print("   baseline background: Om=%.5f  Or=%.4e  fnu=%.4f  ombh2=%.5f  e_sw=%.1f"
      % (base['Om'], base['Or'], base['fnu'], base['ombh2'], base['esw']))
print()

rows = []
for label, var, lo, hi, field in DIALS:
    if var == 'FNU':
        lo_env, hi_env = {'FNU': '0.3680'}, {'FNU': '0.4498'}     # +/-10% of 0.4089
        lo_val, hi_val = 0.3680, 0.4498
    else:
        lo_env, hi_env = {var: '%.4f' % lo}, {var: '%.4f' % hi}
        lo_val = hi_val = None
    a = run(label.replace(' ', '_') + '_lo', lo_env)
    b = run(label.replace(' ', '_') + '_hi', hi_env)
    if a is None or b is None:
        continue
    pa = float(a[field]); pb = float(b[field])
    if pa == pb:
        print("   %-16s DIAL DID NOT REACH THE MODULE (%s unchanged at %.5g)" % (label, field, pa))
        continue
    dlnp = np.log(pb / pa)
    S = (np.log(np.abs(b['res'])) - np.log(np.abs(a['res']))) / dlnp
    rows.append((label, field, pa, pb, S))

print("   %-16s %-8s  %-22s" % ("dial", "field", "verified range") +
      "".join("   S(k=%.3f)" % k for k in KS) + "   [at eta=50]")
print("   " + "-" * 88)
for label, field, pa, pb, S in rows:
    print("   %-16s %-8s  %-22s" % (label, field, "%.5g -> %.5g" % (pa, pb)) +
          "".join("%12.4f" % S[1][j] for j in range(len(KS))))

print()
print("   WHAT IT WOULD TAKE to close the 4.4%% deficit at k=0.080, one dial at a time:")
for label, field, pa, pb, S in rows:
    s = S[1][-1]
    if abs(s) < 1e-6:
        print("     %-16s  no leverage" % label)
    else:
        print("     %-16s  fractional change needed: %+8.1f%%" % (label, 100 * 0.044 / s))
print()
print("   (a required change far outside what other data allow means that dial CANNOT be the cause)")
