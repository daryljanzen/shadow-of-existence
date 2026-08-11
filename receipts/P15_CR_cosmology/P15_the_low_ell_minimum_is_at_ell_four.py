"""
P15_the_low_ell_minimum_is_at_ell_four.py -- the shape of the low-multipole deficit, and where the
sector's statistical weight actually falls.

** THE PARAMETER-FREE LOW-MULTIPOLE DEFICIT IS NOT A MONOTONE RECOVERY FROM THE QUADRUPOLE.  IT IS A
DIP WHOSE MINIMUM FALLS AT $\\ell=4$ -- and the quadrupole and octopole, the two multipoles the paper
quoted, are its two SHALLOWEST points. **

** AND THE SHAPE IS CROSS-VALIDATED.  Two independent Boltzmann treatments of the same discrete
source -- a standard code's exact $\\Delta_\\ell(k)$ sampled at the discrete $k_L$, and the photon
hierarchy built for this programme -- return the SAME minimum at $\\ell=4$ and the SAME recovery, and
differ only in depth, uniformly by $10$--$25\\%$, which is the size of the residual P15
`sec:instrument` declares.  What is cross-validated is the shape; the depth carries their spread. **

WHAT PROMPTED IT.  The paper carried two incompatible figures for this depth: the body, abstract,
results list, scope section and summary said $\\approx0.47/0.41$ at $\\ell=2,3$ "recovering by
$\\ell\\approx7$", while the figure caption on the same page declared those superseded and gave
$0.42/0.35/0.29/0.52$ at $\\ell=2,3,4,5$ with a minimum at $\\ell=4$.  The caption's stated ground for
superseding -- that the earlier figure took the Sachs--Wolfe source as $\\tfrac13\\Phi$ -- does not fit
the receipt the body cites, which is a line-of-sight transfer from a Boltzmann code and carries no
hand-chosen Sachs--Wolfe source at all.  That ground belongs to the older SW-analytic estimate
($0.22/0.20$), which both Boltzmann arms supersede.

WHAT IS ESTABLISHED.
  1. ** THE TWO ARMS AGREE ON THE SHAPE **: both minimise at $\\ell=4$ over $\\ell=2\\ldots5$ and both
     recover by $\\ell\\approx7$--$8$; their depth ratio runs $1.13$--$1.30$.
  2. ** THE $\\ell=4$ MINIMUM WAS NEVER A NEW RESULT **: the registered CAMB receipt
     (`P15_verify_lowell_boltzmann.py`, r1395) tabulates $\\ell=4$ in its own printed output at
     $0.356$, and the likelihood receipt has consumed that value ever since.  The failure was one of
     QUOTATION, not of computation -- the prose quoted the two shallowest points and stopped.
  3. ** THE SECTOR'S WEIGHT DOES NOT LIE AT THE OCTOPOLE **: on the exact cosmic-variance likelihood
     the quadrupole REWARDS this cosmology ($-2.63$), the octopole penalises it at $+1.31$, and the
     largest single-multipole penalty in the sector is the $+2.10$ at $\\ell=4$ -- the prediction's
     own minimum, and the one multipole of the four the large-angle literature does not treat as
     anomalous.  The sector total is unchanged at $+1.8$: a wash inside cosmic variance.
  4. ** THE BRANCH-POINT FILTER'S ADIABATICITY CANNOT MOVE THE MINIMUM **: the exact/WKB transmission
     ratios ($0.926$, $0.913$, $0.901$, $0.891$, $0.889$ at $\\ell=2,3,5,15,40$) vary by $4\\%$ across a
     factor of twenty in $\\ell$, so the correction rescales the low-$\\ell$ block nearly uniformly.

WHAT IS NOT CLAIMED.  Nothing here relieves the observed sky's selective suppression of $\\ell=2$
alone by a factor of order three, which this construction does not produce and which stays inside
cosmic variance.  The depth is quoted to a two-code spread and not to better.

STATUS: ✔✔ (both arms' minima asserted at ell=4; the ell=4 depth asserted present in the standing
  receipt; the per-multipole likelihood re-derived and its argmax asserted at ell=4)
RUN: python3 P15_the_low_ell_minimum_is_at_ell_four.py   RUNTIME: <1s (stdlib only)
ORIGIN: computations/frontier_audit/L146w_the_low_ell_minimum.py, built r2376 (c54.103).
ORIGIN-DIVERGENCE: deliberate and in one direction.  The origin is a LEAD DISPOSAL -- it argues that
  the corpus contradicted itself and that the caption's supersession misidentified its target, which
  is a statement about the corpus's history and belongs in the ledger, not in a paper receipt.  This
  receipt keeps the four load-bearing assertions (the two arms' shared minimum, the standing
  receipt's own ell=4 depth, the likelihood's argmax, the transmission spread) and REPLACES the
  origin's historical part with a check that the corrected statement now reaches all eight corpus
  sites -- a check the origin could not make, because it ran before the sites were fixed.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()
LIK = open(os.path.join(HERE, 'P15_verify_lowell_likelihood_v2.py'), encoding='utf-8').read()
BOL = open(os.path.join(HERE, 'P15_verify_lowell_boltzmann.py'), encoding='utf-8').read()

# arm A: a standard code's exact Delta_l(k) sampled at the discrete k_L -- read off the standing
#        likelihood receipt's own depth table rather than retyped.
CAMB = {int(a): float(b) for a, b in
        re.findall(r'(\d+):([\d.]+)', re.search(r'depth\s*=\s*\{([^}]*)\}', LIK).group(1))}
# arm B: the programme's own photon hierarchy -- read off the paper's caption.
HIER = dict(zip((2, 3, 4, 5), [float(x) for x in re.search(
    r'it sits at \$?([\d.]+)\$?, \$?([\d.]+)\$?, \$?([\d.]+)\$?, \$?([\d.]+)\$? of the flat',
    TEX).groups()]))

print("=" * 78)
print("1 — THE TWO ARMS, AND THEY AGREE ON THE SHAPE")
print("=" * 78)
print(f"  {'ell':>5} {'exact Delta_l(k) x discrete k_L':>33} {'programme hierarchy':>22} {'ratio':>7}")
for l in (2, 3, 4, 5, 6, 7):
    a, b = CAMB.get(l), HIER.get(l)
    print(f"  {l:>5} {('-' if a is None else f'{a:.3f}'):>33} "
          f"{('-' if b is None else f'{b:.3f}'):>22} "
          f"{('-' if (a is None or b is None) else f'{a/b:.3f}'):>7}")
amin = min((2, 3, 4, 5), key=lambda l: CAMB[l])
hmin = min(HIER, key=lambda l: HIER[l])
rec = min(l for l in sorted(CAMB) if CAMB[l] > 0.95)
sp = [CAMB[l]/HIER[l] for l in (2, 3, 4, 5)]
print()
print(f"  ** minimum over ell=2..5:  arm A at ell={amin}   arm B at ell={hmin} **")
print(f"  ** arm A recovers (>0.95) at ell={rec}; arm B's caption says ~8 **")
print(f"  ** depth ratio A/B = {min(sp):.2f}--{max(sp):.2f}: arm B runs "
      f"{100*(1-1/min(sp)):.0f}-{100*(1-1/max(sp)):.0f}% deeper, uniformly **")
assert amin == hmin == 4
assert 1.10 < sum(sp)/4 < 1.35

print()
print("=" * 78)
print("2 — THE ell=4 MINIMUM WAS ALWAYS IN THE STANDING RECEIPT")
print("=" * 78)
prints_l4 = bool(re.search(r'for l in \[2,\s*3,\s*4,', BOL))
print(f"  the r1395 CAMB receipt tabulates ell=4 in its printed output: ** {prints_l4} **")
print(f"  the likelihood receipt consumes depth[4]:                    ** {CAMB[4]:.3f} **")
print(f"  and it is the deepest of ell=2,3,4:                          "
      f"** {CAMB[4] < CAMB[3] < CAMB[2]} **")
assert prints_l4 and CAMB[4] < CAMB[3] < CAMB[2]
print("  ⇒ ** the minimum was computed, printed and consumed from r1395 and never QUOTED. **")

print()
print("=" * 78)
print("3 — THE SECTOR'S WEIGHT: WHERE THE LIKELIHOOD ACTUALLY LOADS")
print("=" * 78)
obs = {2: 0.20, 3: 0.75, 4: 0.70, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}
pe = {l: (2*l+1)*(obs[l]*(1.0/CAMB[l] - 1.0) + math.log(CAMB[l])) for l in range(2, 11)}
print(f"  {'ell':>5} {'CR/LCDM':>9} {'obs/LCDM':>10} {'Delta(-2 ln L)':>16}   (>0 disfavours CR)")
for l in range(2, 8):
    print(f"  {l:>5} {CAMB[l]:>9.3f} {obs[l]:>10.2f} {pe[l]:>16.2f}")
tot = sum(pe.values())
worst = max(range(2, 11), key=lambda l: pe[l])
print(f"  {'':>5} {'':>9} {'total 2..10':>10} {tot:>16.2f}")
print()
print(f"  ** the largest single-multipole penalty is at ell={worst} ({pe[worst]:+.2f}), "
      f"not at the octopole ({pe[3]:+.2f}) **")
print(f"  ** and the quadrupole REWARDS the construction ({pe[2]:+.2f}) **")
assert worst == 4 and pe[4] > pe[3] > 0 > pe[2]
assert abs(tot - 1.8) < 0.15

print()
print("=" * 78)
print("4 — THE BRANCH-POINT FILTER CANNOT MOVE THE MINIMUM")
print("=" * 78)
ratios = {2: 0.926, 3: 0.913, 5: 0.901, 15: 0.891, 40: 0.889}
spread = max(ratios.values()) - min(ratios.values())
print(f"  exact/WKB transmission at ell = {sorted(ratios)}: "
      f"{[f'{v:.3f}' for v in ratios.values()]}")
print(f"  variation across a factor of twenty in ell: {spread:.3f} "
      f"({100*spread/max(ratios.values()):.1f}%)")
print(f"  effect on the ell=2 : ell=3 ratio:          "
      f"{100*(ratios[2]/ratios[3]-1):.1f}%")
assert spread < 0.05
print("  ⇒ ** nearly ell-independent: it rescales the block and does not make or unmake a minimum. **")

print()
print("=" * 78)
print("5 — THE PAPER NOW SAYS IT")
print("=" * 78)
# ** r2376+c54.161: these eight patterns pin the PAPER'S PROSE, and six of them broke when
#    c54.155 inserted a \rcpt{} marker into the very sentences they match.  The claims were all
#    still true -- the citation moved, not the physics.  ** Found by the run-all-receipts gate on
#    its first pass; nothing had run this receipt since the paper was rewritten. **  The patterns
#    now tolerate an intervening citation marker, which is what they should always have done:
#    they are about what the paper SAYS, not about where its citations sit.
_R = r'(?:\\rcpt\{[^}]*\})?'          # an optional citation marker, anywhere inside a phrase
CHECKS = [
    ("the body states the minimum at ell=4",
     r'minimum falls at \$\\ell=4\$\}' + _R + r'---and the quadrupole and octopole'),
    ("the body carries the four-multipole profile",
     r'\$\\approx0\.47\$, \$0\.41\$, \$0\.36\$ and \$0\.68\$'),
    ("the body states the two-code cross-validation",
     r'two independent Boltzmann treatments cross-validate is the shape'),
    ("the abstract carries the minimum",
     r'minimum falls at \$\\ell=4\$\}' + _R + r' \(\$\\approx0\.36\$'),
    ("the scope section carries the minimum",
     r'a dip whose minimum falls at \$\\ell=4\$' + _R + r'(?:,| ---| ---)? ?(?:not at the quadrupole|---and)'),
    ("the likelihood item names ell=4 as the largest penalty",
     r"largest single-multipole penalty sits not at the octopole but at \$\\ell=4\$"),
    ("the summary carries the minimum", r'\$D_C\$---bottoming at \$\\ell=4\$'),
    ("the caption no longer calls the Boltzmann figure leading-order",
     r'neither supersedes the other'),
]
for what, pat in CHECKS:
    hit = bool(re.search(pat, TEX))
    print(f"  {what:>58}  ** {'yes' if hit else 'NO':>3} **")
    assert hit, what
print()
print("  ** all eight sites carry it; the figure caption is no longer the only one. **")
print("=" * 78)
