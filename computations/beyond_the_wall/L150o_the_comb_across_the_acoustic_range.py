#!/usr/bin/env python3
"""
`L-150` + `L-171`.  ** THE COMB, CENSUSED ON ALL 420 PHYSICAL MODES FROM $\\ell=200$ TO $2505$.  IT IS
NOT UNIFORM: ABOVE $\\ell\\simeq700$ IT IS A $\\le27\\%$ RIPPLE ON SIX PER CENT OF MODES, AND BELOW
$\\ell\\simeq350$ IT REACHES $2.6\\times10^{3}$ IN POWER.  SO THE CHAIN IS EXCLUDED — BY THE FIRST-PEAK
REGION — AND WITH IT THE COMB STOPS BEING A PREDICTION FOR OUR SKY. **

c54.147 censused $|\\lambda(k)|^2$ over $1100\\le\\ell\\le1375$, found $92\\%$ of modes stable, and read
that as the acoustic range.  ** It is the acoustic range's MIDDLE.  The full census is run here and
the low end behaves completely differently. **

  PART 1  ** THE CENSUS: every physical mode $k_L=\\sqrt{L(L+2)}$, $L=72$–$910$, Wronskian-gated. **
  PART 2  ** THE PROFILE: a steeply decaying envelope below $\\ell\\simeq350$, nothing above $700$. **
  PART 3  ** WHAT IT EXCLUDES, AND THE LOGIC IS NOW CLOSED IN BOTH BRANCHES. **

Run: python3 L150o_the_comb_across_the_acoustic_range.py      (numpy, json — reads the saved census)
"""
import json
import os

import numpy as np

print(__doc__.split("Run:")[0])
SMAP = 2.75
CENSUS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'L150o_census.json')

# =====================================================================
print("=" * 78)
print("PART 1 — THE CENSUS")
print("=" * 78)
rows = json.load(open(CENSUS))
R = [(r[0], r[2], r[3]) for r in rows if r[4] < 1e-2]
op = [(L, l, lam) for L, l, lam in R if lam > 1.0001]
print(f"  {len(rows)} physical modes L = {rows[0][0]}–{rows[-1][0]} "
      f"(l = {rows[0][2]:.0f}–{rows[-1][2]:.0f}), every one Wronskian-gated at |det T - 1| < 1e-2.")
print(f"  In open (instability) bands: {len(op)} of {len(R)} = {100*len(op)/len(R):.1f}%.")
print(f"  ** But the fraction is not the story.  The AMPLITUDE is, and it is not uniform. **")
assert len(R) == len(rows)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE PROFILE")
print("=" * 78)
print(f"  {'l range':>16} {'modes':>7} {'open':>6} {'% open':>8} {'median |lam|^2':>16} "
      f"{'max |lam|^2':>13}")
for lo, hi in [(200, 350), (350, 500), (500, 700), (700, 1000),
               (1000, 1500), (1500, 2000), (2000, 2600)]:
    seg = [x for x in R if lo <= x[1] < hi]
    so = np.array([x[2]**2 for x in op if lo <= x[1] < hi]) if any(
        lo <= x[1] < hi for x in op) else np.array([1.0])
    print(f"  [{lo:>5},{hi:>5}) {len(seg):>7} {len(so):>6} {100*len(so)/len(seg):>7.1f}% "
          f"{np.median(so):>16.3f} {so.max():>13.1f}")
hi_side = [x[2]**2 for x in op if x[1] >= 700]
lo_side = [x[2]**2 for x in op if x[1] < 350]
print(f"\n  ** above l = 700 : {len(hi_side)} open modes of {len([x for x in R if x[1]>=700])}, "
      f"max |lambda|^2 = {max(hi_side):.3f} **")
print(f"  ** below l = 350 : {len(lo_side)} open modes of {len([x for x in R if x[1]<350])}, "
      f"max |lambda|^2 = {max(lo_side):.0f} **")
assert max(hi_side) < 1.5 and max(lo_side) > 100
print(f"\n  the steep end, mode by mode:")
print(f"  {'L':>5} {'l':>7} {'|lambda|^2':>13}")
for L, l, lam in sorted([x for x in op if x[1] < 300], key=lambda t: t[1])[:10]:
    print(f"  {L:>5} {l:>7.0f} {lam**2:>13.1f}")
print()
for s in [
 "⇒⇒ ** SO IT IS NOT A COMB OF UNIFORM TEETH.  It is a steeply decaying ENVELOPE: $2.6\\times10^3$ in",
 "   power at $\\ell=201$, $10^2$ by $\\ell=245$, $2$ by $\\ell=400$, and $1.3$ — a ripple — everywhere",
 "   above $\\ell\\simeq500$. **",
 "",
 "⚠ ** AND THAT CORRECTS c54.147's SCOPE.  Its census ran at $1100\\le\\ell\\le1375$ and reported",
 "   $92\\%$ stability 'across the acoustic range'.  That is true of the range's MIDDLE and UPPER end",
 "   and false at its bottom, where four modes in five are unstable. **  *A census quoted outside",
 "   the window it was taken in — the same failure this arc has now documented at four different",
 "   scales.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT IT EXCLUDES, AND BOTH BRANCHES CLOSE")
print("=" * 78)
print("  |lambda| is the amplification PER CYCLE.  It acts on the observable leg only if that leg")
print("  inherited its perturbations through a prior branch point -- i.e. only if cosmogenesis is a")
print("  CHAIN.  So the census is a test of the chain, and the two branches are:")
print()
print(f"  {'branch':>34} {'consequence':>44}")
for a_, b_ in [("the chain is real", "the spectrum carries |lambda|^2"),
               ("", "-> 1e3 at l ~ 200, 1 at l ~ 700"),
               ("", "** EXCLUDED by the first-peak region **"),
               ("the chain is not real", "the incoming state at the parent's crunch"),
               ("", "is free; nothing in the construction fixes it"),
               ("", "** so NO spectral bound follows, either way **")]:
    print(f"  {a_:>34} {b_:>44}")
print()
for s in [
 "⇒⇒⇒ ** BOTH BRANCHES GIVE THE SAME ANSWER TO THE QUESTION THE FRONT WAS ASKING: the observed",
 "   spectrum places NO bound on the progenitor's composition.  The determination",
 "   $\\rho=5.4\\times10^{-2}$ stands, and it stands unconditionally rather than on the cyclic",
 "   premise c54.147 used. **",
 "",
 "✔✔✔ ** AND THE CENSUS SETTLES A SEPARATE QUESTION IN THE PROCESS: COSMOGENESIS IS NOT A CHAIN AT",
 "   THE LEVEL OF THE PERTURBATIONS.  A single prior passage would amplify the power at $\\ell=201$",
 "   by $2.6\\times10^3$ relative to $\\ell=700$, and the first acoustic peak sits at $\\ell=220$ and is",
 "   entirely ordinary. **  *c54.144 reached the same verdict on the idealised potential and by the",
 "   large-angle modes; this reaches it on the true variable and by the FIRST-PEAK region, which is",
 "   where the data is strongest.*",
 "",
 "⇒ ** SO THE COMB IS NOT A PREDICTION FOR OUR SKY, AND c54.147's closing claim is withdrawn: it is",
 "   the signature of a chain, and the chain is what this excludes. **  *What survives as a",
 "   prediction is the conditional one — if a universe in this construction has a parent that itself",
 "   came through a branch point, its first-peak region is destroyed.  That is a statement about",
 "   which members of the family can look like ours, and it says: only the first.*",
]:
    print("  " + s)
