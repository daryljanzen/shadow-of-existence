"""`r7713+cc66` exercise the pre-registered `analyse.py` on SYNTHETIC spectra, BEFORE the real data.

⛔ The point is NOT to learn anything about the physics. It is to find out whether a four-hour
   computation would end in a traceback, and whether every branch of the registered decision table
   can actually fire. Nothing here touches the real pseudo/ directory.
"""
import importlib.util
import json
import os
import shutil
import sys

import numpy as np

D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location('an', os.path.join(D, 'analyse.py'))
an = importlib.util.module_from_spec(spec)
spec.loader.exec_module(an)

TMP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pseudo')   # gitignored
an.OUT = TMP
# ⛔ AND REDIRECT THE VERDICT FILE TOO.  The first form of this script left `an.HERE` alone, so every
#    synthetic scenario overwrote the REAL `analyse.json` beside the real data -- a synthetic verdict
#    sitting exactly where a real one goes, which is the same fault this revision has been catching all
#    evening: one object's output in the place that names another's.
an.HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(an.HERE, 'analyse.json')

LA = 301.5427
LS = np.arange(int(np.ceil(0.80 * LA)), int(np.floor(3.10 * LA)) + 1)
Q = LS / LA
rng = np.random.default_rng(7713)


def base(q):
    """something with acoustic-looking structure so the band RMS is not degenerate"""
    return 1e-6 * (1.0 + 0.4 * np.cos(2 * np.pi * q)) * np.exp(-0.15 * q)


def write(name, y):
    np.savez(os.path.join(TMP, name), q=Q, y=y, ls=LS, l_A=LA,
             meta=json.dumps(dict(source='synthetic', kernel='synthetic', n_l=len(y), block=25)))


NOISE = [0.002]


def scenario(tag, f_ker, f_src, interact=0.0):
    """f_ker, f_src: multiplicative shapes in q applied for the kernel / source difference;
    interact: size of a NON-factorising cross term, which is what the well-posedness test looks for"""
    if os.path.isdir(TMP):
        shutil.rmtree(TMP)
    os.makedirs(TMP)
    y00 = base(Q)
    ker = f_ker(Q)
    src = f_src(Q)
    cross = 1.0 + interact * ker * src
    n = lambda: 1.0 + NOISE[0] * rng.standard_normal(len(Q))
    write('pseudo__S_lcdm__K_lcdm.npz', y00 * n())
    write('pseudo__S_cr__K_lcdm.npz', y00 * ker * n())
    write('pseudo__S_lcdm__K_cr.npz', y00 * src * n())
    write('pseudo__S_cr__K_cr.npz', y00 * ker * src * cross * n())
    print("\n" + "#" * 100)
    print(f"#  SCENARIO: {tag}")
    print("#" * 100)
    rc = an.main()
    j = json.load(open(JSON))
    print(f"#  -> rc={rc}  verdict={j.get('verdict')}  stopped_at={j.get('stopped_at')}")
    return j.get('verdict'), j.get('stopped_at'), rc


seen = []
# ⓵ a kernel difference that grows with q and a source difference that goes the other way
seen.append(scenario('kernel difference dominant, source difference opposite sign',
                     lambda q: 1.0 + 0.09 * (q - 1.0), lambda q: 1.0 - 0.05 * (q - 1.0)))
# ⓶ the mirror image
seen.append(scenario('source difference dominant, kernel difference opposite sign',
                     lambda q: 1.0 - 0.05 * (q - 1.0), lambda q: 1.0 + 0.09 * (q - 1.0)))
# ⓷ neither difference has any q dependence at all
seen.append(scenario('both differences flat in q',
                     lambda q: 1.0 + 0.0 * q, lambda q: 1.0 + 0.0 * q))
# ⓸ both differences the same sign and comparable
seen.append(scenario('both differences same sign and comparable',
                     lambda q: 1.0 + 0.07 * (q - 1.0), lambda q: 1.0 + 0.07 * (q - 1.0)))
# ⓹ a large NON-factorising cross term -- the well-posedness test must refuse
seen.append(scenario('a large non-factorising interaction',
                     lambda q: 1.0 + 0.09 * (q - 1.0), lambda q: 1.0 - 0.05 * (q - 1.0),
                     interact=0.60))
# ⓺ the kernel swap made inert -- the control must stop the run before anything is read
if os.path.isdir(TMP):
    shutil.rmtree(TMP)
os.makedirs(TMP)
y00 = base(Q)
for nm in ('pseudo__S_lcdm__K_lcdm.npz', 'pseudo__S_cr__K_lcdm.npz',
           'pseudo__S_lcdm__K_cr.npz', 'pseudo__S_cr__K_cr.npz'):
    write(nm, y00.copy())
print("\n" + "#" * 100)
print("#  SCENARIO: the kernel swap is INERT (all four identical)")
print("#" * 100)
rc = an.main()
j = json.load(open(JSON))
print(f"#  -> rc={rc}  live={j.get('live')}  stopped_at={j.get('stopped_at')}")
seen.append((j.get('verdict'), j.get('stopped_at'), rc))
# ⛭ REACHABILITY: can the three verdict rows fire AT ALL?  Lower scatter, larger planted effects.
#    This asks about the INSTRUMENT, not about the physics: a decision table whose rows cannot be
#    reached by any data is not a decision table.
NOISE[0] = 0.0004
seen.append(scenario('REACHABILITY: kernel dominant, source opposite -- expect CREATES',
                     lambda q: 1.0 + 0.12 * (q - 1.0), lambda q: 1.0 - 0.06 * (q - 1.0)))
seen.append(scenario('REACHABILITY: source dominant, kernel opposite -- expect FAILS TO CANCEL',
                     lambda q: 1.0 - 0.06 * (q - 1.0), lambda q: 1.0 + 0.12 * (q - 1.0)))
seen.append(scenario('REACHABILITY: both same sign and comparable -- expect NEITHER (b)',
                     lambda q: 1.0 + 0.10 * (q - 1.0), lambda q: 1.0 + 0.10 * (q - 1.0)))
seen.append(scenario('REACHABILITY: kernel strong, source same sign but middling -- expect UNLICENSED',
                     lambda q: 1.0 + 0.12 * (q - 1.0), lambda q: 1.0 + 0.012 * (q - 1.0)))
NOISE[0] = 0.002

# ⓻ a partial grid -- must refuse and name what is missing
os.remove(os.path.join(TMP, 'pseudo__S_cr__K_cr.npz'))
print("\n" + "#" * 100)
print("#  SCENARIO: three of four present")
print("#" * 100)
rc = an.main()
print(f"#  -> rc={rc}")
seen.append((None, 'refused_partial', rc))

print("\n" + "=" * 100)
print("  BRANCHES REACHED:")
for v in seen:
    print("   ", v)
print("=" * 100)
