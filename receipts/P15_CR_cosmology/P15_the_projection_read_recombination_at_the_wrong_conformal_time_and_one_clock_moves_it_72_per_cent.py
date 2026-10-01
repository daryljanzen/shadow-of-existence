#!/usr/bin/env python3
"""
P15 receipt -- `r7091`: THE PROJECTION KERNEL READ RECOMBINATION AT A CONFORMAL TIME 72 PER CENT AWAY
FROM WHERE THE PLASMA'S OWN CLOCK PUTS IT, AND MAKING THE TRANSFER CARRY ONE CLOCK REMOVES IT --
BUT IT DOES NOT FLATTEN THE RESIDUAL'S SWING, WHICH IS THE HALF THAT HAD TO BE SAID.

** THE DEFECT, AND IT IS DERIVABLE FROM THE BACKGROUNDS ALONE. **  The two-arm instrument built its
conformal-time grid from the STACKING rate `Hphys` -- and therefore `a(eta)`, `eta_rec`, `eta_0`,
`D_M = eta_0 - eta_rec`, every spline's abscissa, and the projection kernel's own argument
`x0 = eta_0 - eta` -- while the acoustic phase, the perturbations (`LEAFPERT`, default on) and, under
`LEAFSCALES=1`, the sound horizon all accumulate on the LEAF rate `Hleaf`.
  ⇒ *** So Delta_l = INT S(k, eta) j_l(k(eta_0 - eta)) d eta had S parametrised by one clock and j_l's
  argument by the other: two parametrisations of one history inside one integral. ***  That is not a
  preference between two rates -- it is an internal inconsistency, and this receipt measures its size
  WITHOUT running the instrument, because the backgrounds are closed-form.

** THE SIZE. **  At the arm's refit best fit, recombination sits at
      eta_rec = 485.5 Mpc on the STACKING clock   and   282.3 Mpc on the LEAF clock,
a gap of 41.8 per cent -- and the comparison that says what that means is the CONTROL, whose own
eta_rec is 281.8 Mpc: ** the arm's LEAF value is 0.18 per cent from the control's and its STACKING
value is 72.3 per cent away. **  *The same recombination, the same redshift, and a 72 per cent
disagreement about when it happened -- carried into the kernel's argument and nowhere else.*
  ⌗ `D_M` moves only -0.50 per cent (14017 -> 13947 Mpc) because it is `eta_0 - eta_rec` and
  `eta_0` moves with `eta_rec`: radiation is negligible late, so the two clocks agree there.  ** A
  reader watching D_M would have called this a half-per-cent effect. **

** WHAT WAS BUILT: `LEAFGEOM=1`, the one piece of the clock assignment that had no switch. **
`LEAFPERT` moved the perturbation dynamics, `LEAFSCALES` the two scales, `PHASEONLY` the oscillator's
phase -- *the TIME VARIABLE itself was reachable by nothing.*  With `LEAFGEOM=1`, `LEAFSCALES=1` and
`LEAFPERT` the instrument carries ONE clock end to end, and the claim's three consequences are
asserted by the instrument at run time rather than argued: `max|Jac - 1| = 0` exactly,
`max|Phi2 - 1| = 0`, and the two sound-horizon accumulators identical to 0 Mpc.
  ⌗ ** On the CONTROL it is a provable no-op ** -- `Hleaf` and `Hphys` are character-identical when
  radiation is in the rate -- *and that was checked bit-level on the REPORTING path rather than left
  as a reading of the source, which is this sector's own knob-shadow practice.*

⛭ ** THE COMB AS AN OUTPUT AND NOT A PINNED INPUT, WITH THE ONSET HELD. **  *`r7091` asks for "the
comb as a prediction" and that exact phrase is REGISTERED AS WITHDRAWN with the full-lap Floquet
apparatus (`c54.149`, not reinstated `c54.150`), so it is not borrowed here: what is meant is the
narrower and checkable thing, that the comb comes OUT of a held onset instead of going in.*  `r7091` forbids spending the
one free time origin on dragging the comb to a target, so both runs hold `ZSTART=3e7` and the comb is
an OUTPUT: `l_1/l_A` goes 0.7290 -> 0.7326 against the sky's 0.7312 -- ** from 0.0022 out to 0.0014
out, a factor 1.6 closer, with nothing fitted to it. **  *And the peak HEIGHTS move the other way:
P1/P2 2.142 -> 2.080 and P1/P3 2.173 -> 2.094 against the sky's 2.217 and 2.277.  Reported together
because they disagree.*

⛔⛔ ** AND THE DELIVERABLE IS THE RESIDUAL'S SHAPE, WHICH DOES NOT FLATTEN. **  The order fixes the
rule in advance: *a chi^2 that improves while the swing stays is not the fix, and a swing that
flattens is the fix even if chi^2 moves little.*
  - At FIXED parameters the swing looks far WORSE: chi^2 +3.0 per cent, crossings 34 -> 25, and the
    longest run of one sign 16 -> 35 bins -- one unbroken positive excursion from ell 100 to 414.
  - ⌗ ** That is a TILT artefact and the fixed-parameter comparison cannot see it. **  The geometry
    moves `D_M` and the visibility's width in eta, so the best-fit parameters move with it, and these
    are the OLD geometry's.  With an amplitude and a power-law tilt in ell fitted -- the two
    directions a refit moves first -- *chi^2 goes 265.5 -> 215.0, **-19.0 per cent**, the worst
    excursion 6.10 -> 4.12 sigma and the rms 1.59 -> 1.42 sigma.*
  - ⇒ *** But the SWING ITSELF does not flatten: the longest run goes 16 -> 18 bins and the crossings
    36 -> 30. ***  **By the order's own rule this is not the fix.**  *The one-clock build is a real
    improvement that a fixed-parameter comparison hides, AND the alternating residual Daryl is reading
    off the plot survives it. Both halves are the result.*

⚠ ** AND ONE THING FOUND IN PASSING THAT IS NOT THIS REVISION'S DOING. **  The refit's own VERIFIED
minimum, `/tmp/n66/refit/verify_cr.npz`, is NO LONGER REPRODUCIBLE from the tree: a fresh run at its
settings differs by `max|dD_l| = 7.14e-3`.  ** The PRE-patch code differs from it by the same amount
to every digit, so the drift predates this build ** -- *checked that way round on purpose, because a
difference found while holding a patch is the patch's until it is shown not to be.*  ⇒ So the
before/after here is same-revision on both sides and the banked spectrum is used for neither.

** COMPUTES: the two conformal times at recombination and the comoving distance, on each congruence's
own rate, at the CR arm's refit best fit (H0 = 68.581133, Omega_m = 0.297209, omega_b = 0.021524) and at
the control's (67.410309, 0.309826, 0.021966), with z_rec = 1089.9 and Omega_r = 4.15e-5/h^2. **
*** Nothing else is computed here: the comb and the residual's shape are BANKED from the runs named
below, at those same parameters, and are not re-derived. ***  ⌗ *The scope matters because the clock gap
is a ratio of two integrals over the SAME background -- it is nearly parameter-independent, and the
receipt would read the same at any nearby H0 -- while the comb and the shape are not.*

⌗ ** WHAT THIS RECEIPT CAN AND CANNOT RE-DERIVE. **  The clock gap, `D_M`, and the control comparison
are computed here from the closed-form backgrounds and nothing else -- *that is the finding's own
subject, and it needs no spectrum.*  The comb and the shape come from runs whose spectra live in
`/tmp/n66/r7091/` and are not in the repository, so those are banked below with their provenance, as
the resolution-table and band-RMS receipts do for the same bank.
"""
import numpy as np
from scipy.integrate import quad

C = 299792.458
Z_REC = 1089.9
A_REC = 1.0 / (1.0 + Z_REC)

# the arm and the control at the refit best fit -- the parameters both runs were made at
ARM = dict(H0=68.581133, OM=0.297209)
CTL = dict(H0=67.410309, OM=0.309826)


def rates(H0, OM, rad_in_rate):
    """(H_stack, H_leaf) -- the two congruences' rates, the ONLY place the arms differ"""
    OR = 4.15e-5 / (H0 / 100) ** 2
    OL = 1.0 - OM

    def H_stack(a):
        t = OM / a ** 3 + OL
        return H0 * np.sqrt(t + OR / a ** 4 if rad_in_rate else t)

    def H_leaf(a):
        return H0 * np.sqrt(OM / a ** 3 + OL + OR / a ** 4)

    return H_stack, H_leaf


def eta_of(H, a):
    """conformal time, INT C da / (a^2 H) -- the quantity the kernel's argument is built from"""
    return quad(lambda x: C / (x ** 2 * H(x)), 1e-16, a, limit=400)[0]


# ---- the defect, from the backgrounds alone ------------------------------------------------------
Hs, Hl = rates(ARM['H0'], ARM['OM'], rad_in_rate=False)      # the arm: radiation is CONTENT
e_stack, e_leaf = eta_of(Hs, A_REC), eta_of(Hl, A_REC)
e0_stack, e0_leaf = eta_of(Hs, 1.0), eta_of(Hl, 1.0)
Hcs, Hcl = rates(CTL['H0'], CTL['OM'], rad_in_rate=True)     # the control: radiation gravitates
e_ctl = eta_of(Hcs, A_REC)

# ⛭ the control's two rate expressions are CHARACTER-IDENTICAL, so its clocks cannot part company --
#   which is why `LEAFGEOM` is a provable no-op there.  Asserted, not asserted-in-prose.
assert abs(eta_of(Hcs, A_REC) / eta_of(Hcl, A_REC) - 1.0) < 1e-12, \
    "the control's two clocks must be the same clock"
assert abs(Hcs(0.3) - Hcl(0.3)) < 1e-12 and abs(Hcs(1e-4) - Hcl(1e-4)) < 1e-9

gap = 1.0 - e_leaf / e_stack
assert 0.415 < gap < 0.421, f"the clock gap at recombination is 41.8%, not {100*gap:.1f}%"
assert abs(e_stack - 485.5) < 0.2 and abs(e_leaf - 282.4) < 0.2, \
    f"eta_rec must be 485.5 (stack) and 282.3 (leaf), got {e_stack:.1f} and {e_leaf:.1f}"
# *** the sentence this receipt exists for: the SAME recombination, 72 per cent apart. ***
off_leaf = abs(e_leaf / e_ctl - 1.0)
off_stack = abs(e_stack / e_ctl - 1.0)
assert off_leaf < 0.005, f"the arm's leaf eta_rec must sit at the control's, off by {100*off_leaf:.2f}%"
assert 0.70 < off_stack < 0.75, f"its stacking eta_rec must be ~72% away, got {100*off_stack:.1f}%"
assert off_stack / off_leaf > 300, "the two readings must not be comparably far from the control"

# ---- and D_M hides it, which is why nobody watching D_M would have found it ----------------------
DM_stack, DM_leaf = e0_stack - e_stack, e0_leaf - e_leaf
assert abs(DM_stack - 14017.0) < 1.0 and abs(DM_leaf - 13947.1) < 1.0
move = abs(DM_leaf / DM_stack - 1.0)
assert move < 0.006, f"D_M must move under a per cent, it moves {100*move:.2f}%"
assert gap / move > 70, ("the point is the RATIO: the clock gap is two orders above the move in D_M, "
                         "so a reader watching D_M calls a 42% inconsistency a half-per-cent effect")

# ---- the run-level results, banked with their provenance -----------------------------------------
# ** from `computations/beyond_the_wall/r7091_directions/launch.sh`, HIER=1 (the reporting path),
#    LMAXL=1300, LSTEP=8, 943 modes, ZSTART=3e7 held (the onset is NOT pinned), LEAFSCALES=1, at the
#    refit best fit on both sides; before and after are SAME-REVISION runs. **
COMB = {'l_A': (301.8, 300.3), 'l_1_over_l_A': (0.7290, 0.7326),
        'P1_over_P2': (2.142, 2.080), 'P1_over_P3': (2.173, 2.094)}
SKY = {'l_1_over_l_A': 0.7312, 'P1_over_P2': 2.217, 'P1_over_P3': 2.277}
ETA_RUN = {'eta_rec': (485.5, 282.3), 'vis_peak_eta': (485.99, 282.34),
           'vis_FWHM': (43.59, 38.38), 'r_D_at_peak': (7.47, 7.24),
           'hierarchy_handover_eta': (307.1, 136.8)}
# the residual's shape, scored to ell <= 1040 over 104 bins (above ~0.8*LMAXL scores the k truncation)
SHAPE_A = dict(chi2=(266.7, 274.8), crossings=(34, 25), longest=(16, 35),
               mean_ex=(1.23, 1.36), max_ex=(5.94, 3.93), rms=(1.59, 1.57))
SHAPE_AT = dict(chi2=(265.5, 215.0), crossings=(36, 30), longest=(16, 18),
                mean_ex=(1.20, 1.26), max_ex=(6.10, 4.12), rms=(1.59, 1.42),
                tilt=(-0.0046, -0.0324))

# the instrument's own eta_rec must be the one derived here -- the run and the closed form agree
assert abs(ETA_RUN['eta_rec'][0] - e_stack) < 0.2 and abs(ETA_RUN['eta_rec'][1] - e_leaf) < 0.2

# the comb is CLOSER and the heights are FURTHER: both, because they disagree
b, a = COMB['l_1_over_l_A']
assert abs(a - SKY['l_1_over_l_A']) < abs(b - SKY['l_1_over_l_A']), "l_1/l_A must move toward the sky"
assert abs(b - SKY['l_1_over_l_A']) / abs(a - SKY['l_1_over_l_A']) > 1.4, "and by over a factor 1.4"
for q in ('P1_over_P2', 'P1_over_P3'):
    b, a = COMB[q]
    assert abs(a - SKY[q]) > abs(b - SKY[q]), f"{q} moves AWAY from the sky and is reported so"

# ⛔ THE VERDICT, by the rule the order fixed in advance and this receipt does not get to choose
assert SHAPE_A['chi2'][1] > SHAPE_A['chi2'][0], "at fixed parameters chi2 gets worse"
assert SHAPE_A['longest'][1] > 2 * SHAPE_A['longest'][0], "and the longest run more than doubles"
assert SHAPE_AT['chi2'][1] < 0.85 * SHAPE_AT['chi2'][0], \
    "with a tilt marginalised chi2 improves by over 15 per cent -- the fixed-parameter read was a tilt"
assert SHAPE_AT['max_ex'][1] < 0.75 * SHAPE_AT['max_ex'][0], "and the worst excursion drops a third"
# *** and the swing does NOT flatten: more crossings AND shorter runs AND smaller extrema is the rule ***
flattened = (SHAPE_AT['crossings'][1] > SHAPE_AT['crossings'][0]
             and SHAPE_AT['longest'][1] < SHAPE_AT['longest'][0]
             and SHAPE_AT['mean_ex'][1] < SHAPE_AT['mean_ex'][0])
assert not flattened, "the swing does not flatten, and the receipt must say so"
assert SHAPE_AT['crossings'][1] < SHAPE_AT['crossings'][0], "crossings fall rather than rise"
assert SHAPE_AT['longest'][1] >= SHAPE_AT['longest'][0], "the longest run does not shorten"

print("P15_the_projection_read_recombination_at_the_wrong_conformal_time -- PASS")
print(f"  THE DEFECT, from the backgrounds alone and no spectrum:")
print(f"    arm  eta_rec   stacking {e_stack:7.2f} Mpc   leaf {e_leaf:7.2f} Mpc   gap {100*gap:.1f}%")
print(f"    ctrl eta_rec   {e_ctl:7.2f} Mpc  ->  the arm's LEAF reading is {100*off_leaf:.2f}% from it,")
print(f"                                        its STACKING reading {100*off_stack:.1f}% away")
print(f"    D_M            {DM_stack:8.1f} -> {DM_leaf:8.1f} Mpc  ({100*(DM_leaf/DM_stack-1):+.2f}%)"
      f"  -- {gap/move:.0f}x smaller than the gap, which is how it stayed hidden")
print(f"  THE COMB, with the onset HELD and the comb an output:")
print(f"    l_1/l_A        {COMB['l_1_over_l_A'][0]:.4f} -> {COMB['l_1_over_l_A'][1]:.4f}"
      f"   sky {SKY['l_1_over_l_A']:.4f}  (closer by "
      f"{abs(COMB['l_1_over_l_A'][0]-SKY['l_1_over_l_A'])/abs(COMB['l_1_over_l_A'][1]-SKY['l_1_over_l_A']):.1f}x)")
print(f"    P1/P2, P1/P3   {COMB['P1_over_P2'][0]:.3f}->{COMB['P1_over_P2'][1]:.3f} and "
      f"{COMB['P1_over_P3'][0]:.3f}->{COMB['P1_over_P3'][1]:.3f}   sky {SKY['P1_over_P2']:.3f} and "
      f"{SKY['P1_over_P3']:.3f}  -- AWAY")
print(f"  THE SHAPE, scored to ell <= 1040 over 104 bins:")
print(f"    amplitude only  chi2 {SHAPE_A['chi2'][0]:.1f} -> {SHAPE_A['chi2'][1]:.1f}"
      f"   longest run {SHAPE_A['longest'][0]} -> {SHAPE_A['longest'][1]} bins")
print(f"    + a tilt        chi2 {SHAPE_AT['chi2'][0]:.1f} -> {SHAPE_AT['chi2'][1]:.1f}"
      f"  ({100*(SHAPE_AT['chi2'][1]/SHAPE_AT['chi2'][0]-1):+.1f}%)"
      f"   worst excursion {SHAPE_AT['max_ex'][0]:.2f} -> {SHAPE_AT['max_ex'][1]:.2f} sigma")
print(f"    ⇒ the swing does NOT flatten: crossings {SHAPE_AT['crossings'][0]} -> "
      f"{SHAPE_AT['crossings'][1]}, longest run {SHAPE_AT['longest'][0]} -> {SHAPE_AT['longest'][1]} bins")
print("    ⇒ a real improvement a fixed-parameter comparison hides, and NOT the fix for the swing")
