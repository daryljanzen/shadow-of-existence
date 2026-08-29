#!/usr/bin/env python3
"""TEST 2 -- THE CAUSAL DRAG TEST.  Read even/odd height ratio and the first three peak heights for:
  control  DRAGLEAF 0 vs 1  (GATE: must be byte-identical -- Hl_of == Hc_of on the control arm)
  CR       DRAGLEAF 0 vs 1  (the test: does swapping CR's drag to the control's H move even/odd?)

If CR's even/odd moves from ~0.35 toward the control's ~0.62, the drag is the cause of the 2x
suppression.  If it stays put, every term in the baryon Euler equation (R, Phi, drag) is exonerated
and the even-peak suppression comes from outside it -- transfer, projection, or IC.
"""
import sys, numpy as np
from scipy.signal import argrelextrema

SD = sys.argv[1] if len(sys.argv) > 1 else '.'


def eo(f):
    d = np.load(f)
    ls, Dl = d['ls'], d['Dl']
    idx = argrelextrema(Dl, np.greater, order=3)[0][:3]
    if len(idx) < 3:
        return None, None, None
    P = np.array([float(Dl[i]) for i in idx])
    L = np.array([float(ls[i]) for i in idx])
    return 2 * P[1] / (P[0] + P[2]), P, L


print("=" * 80)
print("  TEST 2 -- CAUSAL DRAG SWAP.  even/odd = 2*P2/(P1+P3) ; heights P1 P2 P3")
print("=" * 80)
res = {}
for tag, f in (("CONTROL DRAGLEAF=0", "lcdm_d0"), ("CONTROL DRAGLEAF=1", "lcdm_d1"),
               ("CR      DRAGLEAF=0", "cr_d0"),   ("CR      DRAGLEAF=1", "cr_d1")):
    try:
        e, P, L = eo(f"{SD}/{f}.npz")
        res[f] = (e, P, L)
        if e is None:
            print(f"  {tag}:  <3 peaks found"); continue
        print(f"  {tag}:  e/o = {e:.4f}   P1,P2,P3 = {P[0]:.3g}, {P[1]:.3g}, {P[2]:.3g}   "
              f"l = {[round(x) for x in L]}")
    except FileNotFoundError:
        print(f"  {tag}:  (missing {f}.npz)"); res[f] = None

print()
# gate
if res.get('lcdm_d0') and res.get('lcdm_d1') and res['lcdm_d0'][0] and res['lcdm_d1'][0]:
    g0, g1 = res['lcdm_d0'][0], res['lcdm_d1'][0]
    ok = abs(g0 - g1) < 1e-9
    print(f"  GATE (control DRAGLEAF no-op): e/o {g0:.4f} vs {g1:.4f}  -> {'PASS' if ok else 'FAIL'}")
# the test
if res.get('cr_d0') and res.get('cr_d1') and res['cr_d0'][0] and res['cr_d1'][0]:
    c0, c1 = res['cr_d0'][0], res['cr_d1'][0]
    ctl = res['lcdm_d0'][0] if res.get('lcdm_d0') and res['lcdm_d0'][0] else float('nan')
    print(f"\n  CR even/odd:  DRAGLEAF=0 (geometric drag) = {c0:.4f}")
    print(f"                DRAGLEAF=1 (control's H drag) = {c1:.4f}")
    print(f"                control target               = {ctl:.4f}")
    moved = c1 - c0
    frac = moved / (ctl - c0) if (ctl == ctl and abs(ctl - c0) > 1e-6) else float('nan')
    print(f"  movement: {moved:+.4f}  ({100*frac:+.0f}% of the way to control) -- "
          f"{'toward' if moved > 0 else 'away from'} control")
    print()
    if abs(moved) < 0.02:
        print("  VERDICT: drag swap does NOT move even/odd -> DRAG EXONERATED.  R, Phi, drag all out;")
        print("           the 2x even-peak suppression is outside the baryon Euler equation.")
    elif moved > 0:
        print("  VERDICT: drag swap moves even/odd TOWARD control -> the drag CARRIES the suppression.")
    else:
        print("  VERDICT: drag swap moves even/odd AWAY from control -> drag FIGHTS it; source > 2x.")
