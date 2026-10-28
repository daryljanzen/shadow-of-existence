#!/usr/bin/env python3
"""P15 sec:diffusion-scale -- PO-24: THE DAMPING SIGNATURE PRICED ON THE INSTRUMENT'S OWN EXPONENT.  The signature
imposed on the measured spectrum is exp[-alpha (r^2-1)(l/l_D)^2] with alpha = 1.70, the effective exponent the
instrument's own banked pairs measure (r7577+70.2), at l_D = 1951.9, i.e. l_eff = 1497.  On it the sizes move and the
shapes do not.

WHAT IS CHECKED.  70's computation at r7611+70 (computations/beyond_the_wall/r7611_70_faithful_exponent/, registered
before it existed at 5fb7354) is run from source -- four scripts, each a copy of the exponent-one receipt with only the
signature's exponent changed -- and every figure P15 prints from it is pinned against the output:
  * the collapse at the adjudicated ratio, visibility-peak row: 6.53 in chi^2 over the 185 full-range bins, a tilt of
    +0.0065 absorbing seven tenths of it (0.0107 per bin left); the sharp recombination cut 51.0 and -0.0189; the ratio
    1.082 618 and -0.070 -- a 12- and 95-fold collapse;
  * the joint fit at r = 1.0926 on l = 100-1760: 1.062 chi^2 per bin after the tilt, 69.6 per cent absorbed, the
    residual the Gaussian-minus-power-law to a correlation of 1.000000, the displacement running by 6.2 across windows;
  * the wrong absorber: the slope -2 alpha (r^2-1)(l/l_D)^2 at l = 2508 is -1.0877 (printed -1.09), the swing over 30-2508 6989-fold,
    and a fitted tilt equals that slope at l = 419 and nowhere else (the ratio of the two scales out r^2-1);
  * the tail mocks (r7489's fitter, faithful S): the signature's shift on l = 1000-2508 is +0.0218; no window separates
    the two predictions at 2 sigma, the nearest 700-1760 at 1.65; the four windows sit 0.85-1.2 sigma from the
    signature's; deciding on 1000-2508 needs 1.44 times Planck.
  * The scripts' own registered checks that fail on the faithful exponent are asserted to be exactly the ones 70
    reported: the collapse copy's recombination row exceeds a tenth per bin, its r^2-1 scaling loosens (linear to
    about 3 per cent, quadratic to 15), and the joint-fit route's agreement with C62's instrument-route tilt becomes
    18 per cent (26 per cent at the instrument's own r^2-1).  None of those is a figure P15 prints.
INHERITED.  The measured Planck spectrum and the base the exponent-one receipts used; nothing re-fitted to favour either
verdict.
"""
import contextlib
import io
import os
import re
import runpy
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7611_70_faithful_exponent')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def run(script):
    buf = io.StringIO()
    rc = 0
    cwd = os.getcwd()
    try:
        os.chdir(D)
        with contextlib.redirect_stdout(buf):
            runpy.run_path(os.path.join(D, script), run_name='__main__')
    except SystemExit as e:
        rc = e.code or 0
    except AssertionError:
        rc = 1
    finally:
        os.chdir(cwd)
    return rc, buf.getvalue()


# --- the collapse ---------------------------------------------------------------------------------------------------
rc, out = run('collapse_faithful.py')
vis = re.search(r'^\s+visibility peak\s+1951\.9\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([+-][\d.]+)', out, re.M)
rec = re.search(r'^\s+recombination\s+1951\.9\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([+-][\d.]+)', out, re.M)
r1082 = re.search(r'^\s+1\.08200\s+\S+\s+(\S+)\s+\S+\s+\S+\s+([\d.]+)', out, re.M)
gate("collapse: visibility-peak row costs 6.53 over 185 bins, tilt +0.0065, 0.0107 per bin left (seven tenths absorbed)",
     vis and abs(float(vis.group(1)) - 6.529) < 0.01 and abs(float(vis.group(6)) - 0.00653) < 2e-5
     and abs(float(vis.group(4)) - 0.01072) < 1e-4 and abs(1 - float(vis.group(3)) / float(vis.group(1)) - 0.70) < 0.01)
gate("collapse: the sharp recombination cut costs 51.0 with a tilt of -0.0189",
     rec and abs(float(rec.group(1)) - 50.959) < 0.05 and abs(float(rec.group(6)) + 0.01889) < 2e-5)
gate("collapse: at 1.082 the same test costs 618, tilt -0.070 -- a 12- and 95-fold collapse",
     r1082 and abs(float(r1082.group(2)) - 618.33) < 0.1 and abs(float(r1082.group(1)) + 0.0703) < 2e-4
     and round(618.33 / float(rec.group(1))) == 12 and round(618.33 / float(vis.group(1))) == 95)
fails = re.findall(r'^\s+FAIL\s+(.*)$', out, re.M)
gate("collapse: exactly the four checks 70 reported fail (recombination row over a tenth per bin; r^2-1 scaling loosens)",
     rc == 1 and len(fails) == 4 and sum('recombination' in f for f in fails) == 2
     and any('linear in r^2-1' in f for f in fails) and any('SQUARE' in f for f in fails))

# --- the joint fit --------------------------------------------------------------------------------------------------
rc, out = run('jointfit_faithful.py')
gate("joint fit: 3.49 -> 1.062 chi^2 per bin with the tilt, 69.6 per cent absorbed, displacement -0.0694",
     re.search(r'chi\^2/bin\s+3\.49\d+ \(amplitude only\)\s+->\s+1\.06\d+ \(with the tilt\)\s+69\.6% absorbed', out)
     is not None and 'Delta n_s = -0.06936' in out)
gate("joint fit: the residual is the Gaussian-minus-power-law to a correlation of 1.000000",
     'correlates with the analytic (Gaussian - best power law) at 1.000000' in out)
gate("joint fit: the displacement runs by a factor of 6.2 across windows of the same data", 'a factor of 6.2 across windows' in out)
jf = re.findall(r'^\s+FAIL\s+(.*)$', out, re.M)
gate("joint fit: the one check that fails is the route agreement with C62 (18 per cent), as 70 reported",
     rc == 1 and len(jf) == 1 and 'agreeing to 18%' in jf[0])

# --- the wrong absorber ---------------------------------------------------------------------------------------------
rc, out = run('absorber_faithful.py')
gate("absorber: slope at l = 2508 is -1.0877 (printed -1.09) on the faithful exponent, the swing over 30-2508 6989-fold",
     rc == 0 and re.search(r'-1\.08[78]', out) is not None and 'faithful 6989' in out)
gate("absorber: the fitted tilt equals the signature's true slope at one multipole only, l = 419",
     'faithful: the reported -0.0304 equals dn_eff at l = 419 only' in out)

# --- the tail ------------------------------------------------------------------------------------------------------
rc, out = run('tail_faithful.py')
rows = {m.group(1): [float(x) for x in m.group(2).split()]
        for m in re.finditer(r'^\s+(\d+_\d+)\s+((?:[+-]?[\d.]+\s+){8}[+-]?[\d.]+)\s*$', out, re.M)}
d = rows.get('1000_2508')
gate("tail: the signature's shift on 1000-2508 is +0.0218, and deciding there needs 1.44 times Planck",
     d is not None and abs(d[3] - 0.0218) < 1e-4 and abs(d[8] - 1.44) < 0.005)
gate("tail: no window separates the predictions at 2 sigma; the nearest, 700-1760, at 1.65",
     rows and all(r[6] < 2 for r in rows.values()) and abs(rows['700_1760'][6] - 1.65) < 0.005
     and max(rows, key=lambda w: rows[w][6]) == '700_1760')
gate("tail: all four windows sit 0.85-1.2 sigma from the signature's prediction",
     len(rows) == 4 and all(0.84 <= r[7] <= 1.23 for r in rows.values()))

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
