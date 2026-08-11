#!/usr/bin/env python3
"""
L-146w — `E·1`, "THE OCTOPOLE VERDICT / EXACT LARGE-ANGLE SHAPE". THE VERDICT IS THAT THE OCTOPOLE
IS THE WRONG MULTIPOLE, THE SHAPE IS CROSS-VALIDATED BY TWO INDEPENDENT BOLTZMANN CODES, AND THE
PAPER CURRENTLY CONTRADICTS ITSELF ABOUT BOTH.

`E·1` asks for the exact large-angle shape and a verdict at the octopole.  Both exist.  What does
NOT exist is any statement of either outside a figure caption.

  ** THE PAPER'S BODY, ABSTRACT, RESULTS LIST, SCOPE SECTION AND SUMMARY ALL SAY THE DEFICIT IS
  $\\approx0.47$ AND $0.41$ AT $\\ell=2,3$, "RECOVERING BY $\\ell\\approx7$".  THE FIGURE CAPTION ON THE
  SAME PAGE SAYS THOSE FIGURES ARE *SUPERSEDED* AND GIVES $0.42/0.35/0.29/0.52$ AT $\\ell=2,3,4,5$
  WITH ** A MINIMUM AT $\\ell=4$ ** -- and the caption is the only place in the corpus that says so. **

  PART 1  ** THE TWO CODES, AND THEY AGREE ON THE SHAPE. **
  PART 2  ** THE $\\ell=4$ MINIMUM IS NOT NEW: the registered receipt has printed it since r1395. **
  PART 3  ** THE CAPTION'S SUPERSESSION MISIDENTIFIES ITS TARGET. **
  PART 4  ** THE OCTOPOLE VERDICT: the octopole is not where the weight is -- $\\ell=4$ is. **
  PART 5  The r2241 control worry, and why it does not reach the minimum.
  PART 6  What `L-146` becomes.

Run: python3 L146w_the_low_ell_minimum.py
"""
import os
import re

print(__doc__.split("Run:")[0])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()

# ---- the two profiles, each READ FROM ITS OWN SOURCE rather than retyped ----
# (a) CAMB's exact Delta_l(k) sampled at the discrete k_L -- the registered receipt's depth table,
#     parsed out of the likelihood receipt that consumes it.
LIK = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                        'P15_verify_lowell_likelihood_v2.py'), encoding='utf-8').read()
CAMB = {int(a): float(b) for a, b in
        re.findall(r'(\d+):([\d.]+)', re.search(r'depth\s*=\s*\{([^}]*)\}', LIK).group(1))}
# (b) the programme's own photon hierarchy -- the caption's own numbers, parsed out of the paper.
CAP = [float(x) for x in re.search(
    r'it sits at \$?([\d.]+)\$?, \$?([\d.]+)\$?, \$?([\d.]+)\$?, \$?([\d.]+)\$? of the flat', TEX).groups()]
HIER = dict(zip((2, 3, 4, 5), CAP))

# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO CODES, AND THEY AGREE ON THE SHAPE")
print("=" * 78)
print(f"  {'ell':>5} {'CAMB Delta_l(k) x discrete k_L':>32} {'the programme hierarchy':>26}"
      f" {'ratio':>7}")
for l in (2, 3, 4, 5, 6, 7):
    a, b = CAMB.get(l), HIER.get(l)
    ca = '-' if a is None else f'{a:.3f}'
    cb = '-' if b is None else f'{b:.3f}'
    cr = '-' if (a is None or b is None) else f'{a/b:.3f}'
    print(f"  {l:>5} {ca:>32} {cb:>26} {cr:>7}")
print()
amin = min((2, 3, 4, 5), key=lambda l: CAMB[l])
hmin = min(HIER, key=lambda l: HIER[l])
print(f"  ** the CAMB arm's minimum over 2..5:      ell = {amin} **")
print(f"  ** the hierarchy arm's minimum over 2..5: ell = {hmin} **")
assert amin == hmin == 4
rec_camb = min(l for l in sorted(CAMB) if CAMB[l] > 0.95)
print(f"  ** the CAMB arm recovers (>0.95 of LCDM) at ell = {rec_camb}; the caption says ~8 **")
sp = [CAMB[l]/HIER[l] for l in (2, 3, 4, 5)]
print(f"  ** the depth ratio between the two arms: {min(sp):.2f}--{max(sp):.2f}, i.e. the hierarchy"
      f" runs {100*(1-1/min(sp)):.0f}-{100*(1-1/max(sp)):.0f}% deeper **")
assert 1.10 < sum(sp)/4 < 1.35
print()
for s in [
 "⇒⇒ ** TWO INDEPENDENT BOLTZMANN COMPUTATIONS AGREE ON THE SHAPE OF THE FEATURE -- a dip bottoming",
 "   at $\\ell=4$, recovered by $\\ell\\approx7$--$8$ -- AND DIFFER ONLY IN DEPTH, BY $10$--$25\\%$. **",
 "",
 "⌗ *And that spread is not a discrepancy but a declared quantity: P15 `sec:instrument` states the",
 "programme's own code sits $\\sim4$--$5\\%$ low in the transfer against an independent one, which is",
 "$\\sim8$--$10\\%$ in $C_\\ell$ -- the size seen here.*  ** So the right statement is neither arm's",
 "number alone: it is a cross-validated SHAPE carrying a two-code depth spread. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE ell=4 MINIMUM IS NOT NEW")
print("=" * 78)
BOL = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                        'P15_verify_lowell_boltzmann.py'), encoding='utf-8').read()
prints_l4 = bool(re.search(r'for l in \[2,\s*3,\s*4,', BOL))
print(f"  the registered CAMB receipt tabulates ell=4 in its own output: ** {prints_l4} **")
print(f"  the likelihood receipt CONSUMES the ell=4 depth:               ** {4 in CAMB} "
      f"(depth[4] = {CAMB[4]:.3f}) **")
assert prints_l4 and CAMB[4] < CAMB[3] < CAMB[2]
print()
for s in [
 "⚠⚠ ** SO THE MINIMUM AT $\\ell=4$ WAS IN THE REGISTERED RECEIPT'S OWN PRINTED TABLE FROM r1395, AND",
 "   THE LIKELIHOOD HAS BEEN EATING IT EVER SINCE.  IT WAS NEVER DISCOVERED AND NEVER LOST -- IT WAS",
 "   NEVER QUOTED. **  *The prose quoted $\\ell=2$ and $\\ell=3$, which are the two SHALLOWEST points of",
 "   the feature, and stopped.*",
 "",
 "⌗ *When a later node recomputed the same thing on the programme's own hierarchy it reported the",
 "minimum as **new** -- 'a fresh discriminant on an item previously marked computation-complete'.",
 "** It was a fresh reading of a standing receipt.  That is a different and more useful thing to",
 "know, because it says the corpus's failure was one of QUOTATION, not of computation. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CAPTION'S SUPERSESSION MISIDENTIFIES ITS TARGET")
print("=" * 78)
sup = re.search(r'\\emph\{The earlier leading-order figure[^}]*\}[^\n]*', TEX).group(0)
print("  the caption says, of the figure the BODY still carries:")
print("     " + sup[:150].replace('\\emph{', '').replace('}', '') + " …")
print()
cites_boltz = 'P15_verify_lowell_boltzmann' in TEX
print(f"  but the body attributes $0.47/0.41$ to `verify_lowell_boltzmann.py`: ** {cites_boltz} **")
print(f"  and that receipt's method is: ** CAMB's exact Delta_l(k) (SW + early/late ISW + Doppler),"
      f" gate-validated to four figures against CAMB's own $C_\\ell$ **")
assert cites_boltz and 'get_cmb_transfer_data' in BOL and 'Phi' not in BOL
print()
for s in [
 "⇒ ** THE $\\tfrac13\\Phi$ DIAGNOSIS CANNOT APPLY TO IT: A LINE-OF-SIGHT TRANSFER FROM A BOLTZMANN",
 "   CODE DOES NOT CARRY A HAND-CHOSEN SACHS--WOLFE SOURCE AT ALL. **  *The $\\tfrac13\\Phi$ error is",
 "   real and it belongs to the OLDER SW-analytic estimate ($0.22/0.20$), which the confrontation",
 "   receipt already records as superseded on exactly that ground.*",
 "",
 "⌗ ** SO THE CAPTION SUPERSEDES THE RIGHT NUMBER FOR THE WRONG REASON, AND THE WRONG REASON IS WHAT",
 "   MADE THE CONTRADICTION SURVIVABLE: a reader who checks the receipt finds the criticism does not",
 "   fit it, and has no way to tell which of the paper's two figures to believe. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE OCTOPOLE VERDICT")
print("=" * 78)
import math
obs = {2: 0.20, 3: 0.75, 4: 0.70, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0, 10: 1.0}


def per_ell(depth):
    return {l: (2*l+1)*(obs[l]*(1.0/depth[l] - 1.0) + math.log(depth[l])) for l in range(2, 11)}


pe = per_ell(CAMB)
print(f"  {'ell':>5} {'CR/LCDM':>9} {'observed/LCDM':>15} {'Delta(-2 ln L)':>16}  (>0 disfavours CR)")
for l in range(2, 8):
    print(f"  {l:>5} {CAMB[l]:>9.3f} {obs[l]:>15.2f} {pe[l]:>16.2f}")
tot = sum(pe.values())
print(f"  {'':>5} {'':>9} {'total 2..10':>15} {tot:>16.2f}")
worst = max(range(2, 11), key=lambda l: pe[l])
print()
print(f"  ** the largest single-multipole penalty falls at ell = {worst} "
      f"({pe[worst]:+.2f}), not at the octopole ({pe[3]:+.2f}). **")
assert worst == 4 and pe[4] > pe[3] > 0 > pe[2]
print()
for s in [
 "⇒⇒ ** THE VERDICT `E·1` ASKS FOR IS THAT THE OCTOPOLE IS NOT WHERE THE WEIGHT IS. **  *The",
 "   quadrupole REWARDS the construction, the octopole penalises it mildly, and the largest single",
 "   penalty in the whole sector sits at $\\ell=4$ -- the multipole the papers never name, at the",
 "   minimum they never quote.*",
 "",
 f"⌗ ** AND THE SECTOR-LEVEL VERDICT IS UNCHANGED: the total is ${tot:+.1f}$, a wash inside cosmic",
 "   variance, exactly as the papers say. **  *The correction is to WHERE the sector's weight lies,",
 "   not to whether it discriminates -- which is the honest shape of this disposal: the item's",
 "   headline claim survives and its internal accounting does not.*",
 "",
 "⌗⌗ ** THE PREDICTION THIS LEAVES ON THE TABLE IS SHARPER THAN THE ONE THE PAPERS STATE: not 'a",
 "   mild deficit at $\\ell=2$--$3$' but ** *a dip bottoming at $\\ell=4$ at roughly a third of the",
 "   $\\Lambda$CDM expectation, recovering by $\\ell\\approx7$--$8$, with $\\ell=2$ and $\\ell=3$ on its",
 "   shoulder.* ** Parameter-free, set by $\\Lambda$ through $r_0$ and $D_C$, and cross-validated by",
 "   two codes. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THE r2241 CONTROL WORRY DOES NOT REACH THE MINIMUM")
print("=" * 78)
for s in [
 "*The register's `E·1` body ends at r2241 with: **'the construction does not yet predict $\\ell=2$--$5$",
 "sharply enough to be tested there; controlled for $\\ell\\gtrsim8$'** -- the scalar branch-point",
 "filter's adiabaticity parameter $D/k$ reaching $1.82$, $1.21$, $0.91$, $0.73$ at $\\ell=2,3,4,5$.*",
 "",
 "✔ ** THAT WORRY IS ALREADY SETTLED IN THE SAME CAPTION, ONE PARAGRAPH DOWN, AND THE REGISTER DOES",
 "   NOT CARRY THE SETTLEMENT. **  *The WKB form is an approximation; the mode equation",
 "   $\\psi'' = \\omega^2\\psi$ is well posed at every $k$, and composing exact constant-$\\omega$ transfer",
 "   matrices over the segment gives exact/WKB ratios of $0.926$, $0.913$, $0.901$, $0.891$, $0.889$",
 "   at $\\ell=2,3,5,15,40$.*",
]:
    print("  " + s)
print()
ratios = {2: 0.926, 3: 0.913, 5: 0.901, 15: 0.891, 40: 0.889}
spread = max(ratios.values()) - min(ratios.values())
print(f"  variation of the exact/WKB correction across ell = 2..40: {spread:.3f} "
      f"({100*spread/max(ratios.values()):.1f}%)")
print(f"  its effect on the ell=2 : ell=3 ratio: {100*(ratios[2]/ratios[3] - 1):.1f}%")
assert spread < 0.05
print()
for s in [
 "⇒ ** THE CORRECTION IS ALL BUT $\\ell$-INDEPENDENT, SO IT RESCALES THE WHOLE LOW-$\\ell$ BLOCK AND",
 "   DOES NOT MOVE THE MINIMUM. **  *The adiabaticity parameter was the wrong figure of merit --",
 "   it measures the fractional error in an exponent that is itself small at low $\\ell$.*",
 "",
 "⌗ *So `E·1`'s last recorded status is stale in the direction that matters: the item says the",
 "region is untestable, and the paper it points at says why it is testable after all.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — WHAT `L-146` BECOMES")
print("=" * 78)
for s in [
 "✔ ** THE EXACT LARGE-ANGLE SHAPE: computed, twice, by independent codes that agree on it. **",
 "✔ ** THE OCTOPOLE VERDICT: delivered, and it is that the octopole carries less of the sector's",
 "   weight than $\\ell=4$ does. **",
 "✔ ** THE CONTROL WORRY: settled by the exact transfer-matrix transmission, which is nearly",
 "   $\\ell$-independent and therefore cannot produce or destroy a minimum. **",
 "⇒ ** SO `E·1`'s COMPUTATIONAL CONTENT IS COMPLETE AND `L-146` STRIKES -- but only after the",
 "   corpus is made to say it, because at present the corpus says two incompatible things and the",
 "   true one is in a figure caption. **",
 "",
 "⚠ ** WHAT DOES NOT STRIKE AND MUST NOT BE LOST: the observed sky suppresses $\\ell=2$ ALONE by a",
 "   factor of order three, and nothing in this construction produces a selective quadrupole dip. **",
 "   *The floor starves $\\ell=2$, $3$ and $4$ together and bottoms at $4$; the sky does not.  That",
 "   is an unexplained feature of the data on this construction, it is inside cosmic variance, and",
 "   it belongs on `L-147` (`E·2`, the likelihood-level comparison) where the statistics live.*",
 "",
 "⌗⌗ ** THE BASE RATE, ONE NOTCH FURTHER DOWN. **  *The standing entry says a result lands in the",
 "   section that produced it and does not reach the places that SUMMARISE.  ** This one did not",
 "   reach the body either.  It landed in a figure caption -- the one location that is neither",
 "   argument nor summary, that no gate reads as prose, and that a reader skips. **  And the caption",
 "   knew: it says *superseded*, on the same page as the text it supersedes, and has said so since",
 "   r2204 -- a hundred and seventy revisions of a paper contradicting itself across one page.*",
]:
    print("  " + s)
