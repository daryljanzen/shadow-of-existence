#!/usr/bin/env python3
"""
`L-150`, front #1.  ** THE CORPUS CARRIES TWO ACCOUNTS OF WHAT THE COLLAPSE LEG DOES TO THE SPECTRUM.
THEY ARE COMPATIBLE — EACH HOLDS ON ITS OWN SIDE OF ONE BREAK, AT $\\ell\\simeq115$ — AND CHECKING THAT
RETRACTS c54.138's TIGHTENING OF THE BOUND, WHICH RESTED ON THE VACUUM DATA c54.137 HAD ALREADY
REMOVED. **

  P15 `rem:transmission-leg`  : horizon entry at $x=k\\eta/\\sqrt3=1/\\sqrt3$ for every $k$ — the
                                RADIATION era's own scale invariance — so **the leg multiplies the
                                spectrum by a constant and the tilt is the progenitor's.**
  c54.122 / c54.137           : the leg is $\\beta=2$, a MATTER-dominated contraction, and modes
                                exiting there freeze — so **the leg would manufacture the tilt.**

  PART 1  ** ONE NUMBER DECIDES WHICH ACCOUNT COVERS WHICH MODE, and at the bound the corpus already
          had, they PARTITION the observed range rather than contradict. **
  PART 2  ** THE RETRACTION.  c54.138 tightened the bound tenfold by asking where the FLAT BRANCH
          exists — but a flat branch is what VACUUM data manufactures, and there is none.
          c54.133's original crossover bound survives, because the leaked/direct RATIO does not
          depend on the normalisation at all. **
  PART 3  ** WHAT SURVIVES AS A CONSTRAINT ON THE PARENT, WITH NO ASSUMPTION ABOUT THE DATA. **
  PART 4  ** THE ONE PLACE THE PICTURE IS STILL STRAINED: faithful content wants a factor ~20 more
          radiation than the crossover bound allows. That is front #1's real content. **

Run: python3 L150h_which_side_of_equality_did_the_observed_modes_cross.py      (numpy)
"""
import numpy as np

print(__doc__.split("Run:")[0])

MPC, LAM = 3.0857e22, 1.1056e-52
alpha = np.sqrt(3.0 / LAM) / MPC
M_nar = alpha / (3 * np.sqrt(3))
S_MAP, K_MAX, K_MIN = 2.750, 909.0, 5.0
R0, Z_EQ = 5065.0, 3399.0
CS = 1.0 / np.sqrt(3.0)

# =====================================================================
print("=" * 78)
print("PART 1 — ONE NUMBER DECIDES, AND IT PARTITIONS RATHER THAN CONTRADICTS")
print("=" * 78)
print("  On the leg the comoving horizon is |a'|/a with a = M(rho|sigma| + sigma^2/2):")
print(f"  {'regime':>28} {'aH':>12} {'a mode exits at':>18} {'so it exits there iff':>24}")
for nm, aH, ex, cond in [("matter (|sigma| >> 2 rho)", "2/|sigma|", "|sigma| = 2/k", "k < 1/rho"),
                         ("radiation (|sigma| << 2 rho)", "1/|sigma|", "|sigma| = 1/k", "k > 1/(2 rho)")]:
    print(f"  {nm:>28} {aH:>12} {ex:>18} {cond:>24}")
rho_133 = 2 * np.pi * np.sqrt(3) / K_MAX
k_split = 1.0 / (2 * rho_133)
print(f"\n  At c54.133's bound rho = {rho_133:.3e} the split falls at interior mode "
      f"{k_split:.0f}, i.e. l = {k_split*S_MAP:.0f}:")
print(f"  {'multipole range':>22} {'exits in':>14} {'account that applies':>34}")
for a_, b_, c_ in [(f"l <~ {k_split*S_MAP:.0f}", "matter", "the beta = 2 freezing (c54.122)"),
                   (f"l >~ {k_split*S_MAP:.0f}", "radiation", "P15's transmission (rem:transmission-leg)")]:
    print(f"  {a_:>22} {b_:>14} {c_:>34}")
print()
for s in [
 "⇒⇒ ** SO THE TWO ACCOUNTS ARE NOT RIVALS: they PARTITION the observed range, and the boundary is",
 "   the progenitor's own matter--radiation equality seen in mode number. **  *P15's envelope claim",
 "   is explicitly for the acoustic modes, $k\\gtrsim10k_s$ — which is exactly the radiation side.",
 "   The matter side is the large-angle end, where the corpus's parameter-free low-$\\ell$ deficit",
 "   already lives.*",
 "",
 "⌗ ** AND THAT ANSWERS FRONT #1's QUESTION IN THE ONLY FORM IT HAS: 'which composition does the",
 "   collapse need' is 'where does this split fall', and the sky places it near $\\ell\\sim100$. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE RETRACTION")
print("=" * 78)
print("  c54.138 argued: the flat branch exists only for k < 1/rho, so flatness to k = 909 needs")
print("  rho <= 1.1e-3 -- a tenfold tightening of c54.133.  ** That argument is wrong, and its error")
print("  is one this arc had already exposed one revision earlier. **")
print()
print("  The 'flat branch' is flat because VACUUM data supply N_k = 1/sqrt(2 c_s k).  c54.137")
print("  established the data are NOT vacuum, by a factor 1e94.  With inherited data there is no")
print("  manufactured flat branch to lose, so nothing breaks at k = 1/rho.")
print()
print("  ** WHAT DOES SURVIVE IS c54.133's CROSSOVER, BECAUSE IT IS A RATIO. **  The survivor")
print("  receives direct c_1 and leaked 2 pi i p c_0, and WKB fixes |c_0|/|c_1| = 1/(c_s k)")
print("  whatever the normalisation, so")
print("     ** P_out(k) ∝ k^3 N_k^2 (c_s k + 2 pi/rho)^2   and   P_out/P_in ∝ (c_s k + 2 pi/rho)^2 **")
print("  -- a transfer independent of N_k entirely.")
print()
print(f"  {'rho':>12} {'k_x = 2 pi sqrt3/rho':>22} {'transfer log-slope over k = 5..909':>36}")
for rv in [1.0e-1, rho_133, 1.1e-3]:
    ks = np.array([K_MIN, K_MAX])
    T = (CS * ks + 2 * np.pi / rv)**2
    sl = np.diff(np.log(T))[0] / np.diff(np.log(ks))[0]
    print(f"  {rv:>12.3e} {2*np.pi*np.sqrt(3)/rv:>22.1f} {sl:>36.3f}")
sl_133 = np.diff(np.log((CS * np.array([K_MIN, K_MAX]) + 2 * np.pi / rho_133)**2))[0] / \
    np.diff(np.log(np.array([K_MIN, K_MAX])))[0]
print(f"\n  ** so c54.133's bound is exactly the statement that this transfer stays flat to within")
print(f"     {sl_133:.2f} in the log-slope across the observed range, and it needs NO assumption")
print(f"     about where the incoming amplitude came from. **")
assert sl_133 < 0.3
print()
for s in [
 "⚠⚠⚠ ** SO c54.138's TIGHTENING IS WITHDRAWN AND c54.133's ORIGINAL BOUND STANDS:",
 f"   rho <= {rho_133:.2e}, i.e. rho_r/rho_m <= {rho_133**2/4:.1e} at maximum expansion. **",
 "   *Everything c54.138 evaluated AT the tightened bound moves with it, and every such number moves",
 "   in the safe direction — the tensor floor, the vacuum shortfall and the shear margin all get",
 "   LARGER at larger $\\rho$, since all three scale as $\\rho^{-6}$.*",
 "",
 "⌗⌗ ** AND THE SHAPE OF THE ERROR IS WORTH MORE THAN THE NUMBER: c54.137 removed the vacuum",
 "   assumption from the amplitude and I re-used it, one revision later, to sharpen a bound. **",
 "   *The assumption was retired in one sector and left standing in the next, by the same node in",
 "   consecutive revisions.  **That is the propagation failure the corpus has documented seven times",
 "   in other people's text, occurring at the shortest range it can occur at.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT SURVIVES, ASSUMPTION-FREE")
print("=" * 78)
rho_bbn = 2.61e-6
print(f"  {'constraint':>44} {'gives':>22} {'rests on':>22}")
for a_, b_, c_ in [("BBN radiation-dominated at 1 MeV (c54.137)", f"rho >= {rho_bbn:.1e}", "standard BBN"),
                   ("the crossover transfer stays flat (c54.133)", f"rho <= {rho_133:.1e}", "** nothing else **"),
                   ("~withdrawn: the flat branch exists~", "~rho <= 1.1e-3~", "~vacuum data~")]:
    print(f"  {a_:>44} {b_:>22} {c_:>22}")
print(f"\n  ***  {rho_bbn:.1e}  <=  rho  <=  {rho_133:.1e}  ***")
print(f"  ***  {rho_bbn**2/4:.1e}  <=  rho_r/rho_m at maximum expansion  <=  {rho_133**2/4:.1e}  ***")
print(f"  a window {rho_133/rho_bbn:.0f}-fold wide -- eleven times wider than c54.138 reported, and")
print(f"  standing on less.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE ONE PLACE THE PICTURE IS STILL STRAINED")
print("=" * 78)
a_eq_ours = R0 / Z_EQ
rho_content = np.sqrt(2 * a_eq_ours / M_nar)
a_eq_parent = M_nar * rho_133**2 / 2
print("  If the content crosses the branch point faithfully -- which P15's transmission and P16's")
print("  nucleosynthesis both assume -- then rho_r/rho_m at a given areal radius is continuous, so")
print("  the progenitor's matter-radiation equality is OUR OWN:")
print(f"  {'quantity':>44} {'value':>16}")
for nm, v in [("our equality radius r_0/(1+z_eq)  [Mpc]", a_eq_ours),
              ("the parent's, at the crossover bound  [Mpc]", a_eq_parent),
              ("ratio", a_eq_ours / a_eq_parent),
              ("rho that faithful content would require", rho_content),
              ("rho the crossover bound allows", rho_133)]:
    print(f"  {nm:>44} {v:>16.4g}")
print()
for s in [
 "⚠⚠ ** SO THE TWO DISAGREE BY A FACTOR ~20 IN THE EQUALITY RADIUS, ~4.5 IN $\\rho$ — and THAT, not",
 "   'derive the composition', is what front #1 actually contains. **",
 "   *Faithful transmission wants the parent to carry as much radiation per unit matter as we do;",
 "   the observed spectrum's flatness wants it to carry twenty times less.*",
 "",
 "⌗ ** IT IS NOT YET A CONTRADICTION AND IT IS NOT DRESSED AS ONE.  Both sides are order-of-magnitude",
 "   at present: the crossover bound uses a nominal $k_{\\max}=909$ and $c_s=1/\\sqrt3$ at the crunch,",
 "   and the content estimate uses $M$ at the Nariai cap and our own $z_{\\rm eq}$. **  *A factor of",
 "   twenty is exactly the size that either survives sharpening or dissolves under it, and which one",
 "   is a calculation rather than a judgement.*",
 "",
 "⇒ ** WHAT WOULD SETTLE IT: the parent's equality is fixed by ITS matter-to-photon ratio, which is",
 "   the same datum P16's nucleosynthesis network already carries as $\\eta$ — so the comparison can",
 "   be made in the network's own variables rather than in scale factors. **  *That is one",
 "   calculation, on machinery the corpus already has, and it is front #1's owed step.*",
 "",
 "⌗ *This is registered and NOT landed in a paper: what is established here is a strain, not its",
 "   resolution.  The plan carries work; the papers carry results.*",
]:
    print("  " + s)
