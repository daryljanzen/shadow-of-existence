#!/usr/bin/env python3
r"""RECEIPT -- P16 (r7834, node 60): ** THE COLD READ.  THE NETWORK'S OWN RATIO IS THE
INSTANTANEOUS ONE, SO THE COUNT IT RUNS IS THREE EXACTLY AND THE CORRECTION IT NAMES IS WHAT
THAT RATIO OMITS; AND THE PROGENITOR COMPOSITION WAS PRINTED TWICE BECAUSE ITS GENERATING
RECEIPT DERIVES THE MASS FROM A BACKGROUND THE PAPER ITSELF DECLINES. **

COMPUTES: this receipt pins NO physical parameter and measures no new physics.  It is an audit.
  What it computes is arithmetic on figures already banked elsewhere: (a) the effective number
  implied by the network module's OWN neutrino temperature ratio, (b) the progenitor's radiation
  fraction implied by the paper's OWN two printed numbers against the one its generating receipt
  derives, (c) the size of the omitted non-instantaneous correction on the sensitivity the
  banked right-handed run already measured, (d) the specific-entropy budget the paper prints
  unpinned, and (e) the two-sided agreement of the sigma figures with the measured values the
  paper now names.  Every constant it uses is read from a banked receipt, a module in this
  repository, or the paper, and the provenance is stated at each use.
  ** NO PREDICTION WAS REGISTERED FOR THIS PASS, and none is claimed. ** The order (r7831) was a
  cold read of a paper that already exists; its arms are assertions about the paper's state and
  about arithmetic on banked figures, both of which this file re-derives in the open.  A
  register-before-measure claim is NOT made and must not be read into the arms below.

THE ORDER (r7831, from 69): read P16 end to end; check every printed figure against the receipt
its sentence cites; check that P16 is in one state and agrees with P14 and P15 where they state
the same thing; fix mechanical defects, list every substantive one.

WHAT THE READ FOUND, and what this revision did with each.

  (1) FIXED.  ** sec:interior glossed the highest mode's freeze-out margin as "a fifth of a per
      cent" where its OWN cited receipt computes 0.065 per cent. **  The gloss is threefold out
      and in the LESS conservative direction (a smaller margin is the harder case for the claim
      the sentence makes), and the cited receipt's r3124 comment already records it as such and
      records P7 being corrected for carrying it.  P16 had not been.  Now prints 0.065.

  (2) FIXED.  ** sec:network folded the non-instantaneous-decoupling correction into the ratio
      that omits it. **  The sentence read: three species "with the standard post-annihilation
      temperature ratio $(4/11)^{1/3}$---that is, the effective number $N_{\mathrm{eff}}=3.046$
      ..., the Standard Model value including the small non-instantaneous-decoupling
      correction".  But $(4/11)^{1/3}$ IS the instantaneous-decoupling ratio: at that ratio with
      three species the effective number is 3 exactly, and the 0.044-to-0.046 is precisely the
      correction the ratio leaves out.  The module confirms it in code -- `r_nu =
      (4.0/11.0)**(1.0/3.0)` and `3 nu (7/8*2 each, at T_nu)`, with no energy transfer term.
      The sentence now separates the two, and names BOTH values with their statuses: 3.046 as
      first evaluated (Mangano 2005, the corpus's own citation) and the 3.044 P15 and P18 carry
      on the later ones.  ** The 3.046 token is DELIBERATELY left standing in the paper **, for
      a reason stated in (6).

  (3) FIXED.  ** The progenitor's determined composition was printed TWICE in sec:interior, as
      $5.45\times10^{-2}$ and as $5.4\times10^{-2}$, and at the printed precision those are two
      numbers and not one rounded one ** -- 0.05451 to two significant figures is 5.5e-2, not
      5.4e-2.  The second is the RETIRED pair's value (rho ~ 5.4e-2 with (rho_r/rho_m)_max ~
      7.3e-4), which A2 in L211_closure_adjacency asserts gone from the capstone, and which
      eight consuming receipts across P15, L805, L806 and L812 do not use -- they pin 0.05451.
      P16 now prints 5.45e-2 in both places.

  (4) FIXED.  ** The two measured values P16's sigma figures are read against were never printed
      in P16 **, and P15 attributes one of them to P16 in terms: "the $0.2453\pm0.0034$ the
      cosmogenesis paper quotes there".  It did not quote it.  sec:verdict now names both, and
      arm (8) below reproduces the sigma figures from them.  ** This is station 9's defect
      exactly, one sector over: a load-bearing number fixed in code and absent by name. **

  (5) REPORTED, NOT FIXED -- routed to 69 in FOR_66_FROM_60.md.  ** The receipt that GENERATES
      the composition determination computes neither the paper's figure nor its own paper's
      stated background. **  `P16_the_progenitor_composition_is_bracketed.py` derives the mass as
      the Nariai cap of Lambda = 1.1056e-52 m^-2, which gives M = 4.27e52 kg and rho = 0.0539 --
      while the paper says, in the same section, that "neither number is free of the expansion
      rate ... Both are therefore quoted on the background the distance data fix and not on the
      standard model's", and names M = 4.17e52 kg.  Arm (6) shows the paper's own two printed
      numbers return the paper's own rho to four figures, so the paper is internally consistent
      and the generating receipt is the member off the stated background.  ** Repairing it needs
      the calibrated Lambda (equivalently H_0) stated ONCE where all three readers can take it,
      and the corpus states it nowhere this pass could read: `P16_the_regulated_peak...` pins its
      1.54 and 1.92 R_s on the MIXED pair -- Lambda = 1.1056e-52 beside M = 4.17e52, which that
      Lambda does not give.  That is a fork and not a fix, and it is 69's. **

  (6) REPORTED, NOT FIXED.  ** Three live pins assert the 3.046 token's PRESENCE, and two of the
      three sit in receipts this seat does not own. **  S1 in L803_station9_neff pins
      "N_{\mathrm{eff}}=3.046" as a PAPER/TOKEN quote pin; P10 and P11 in L204_physics_reach
      assert its presence as PRESENCE-CONTROL floors.  Measured this pass: "3.046" appears in
      exactly ONE paper body, P16's, and otherwise only in the generated receipt appendices.  So
      retiring the token from P16 would take S1's pin red.  ** The guard applies before the pin
      does -- a gate must not assert the status of a sentence a live row is asking to change --
      so the pin is not a licence to leave the sentence wrong; but re-anchoring another band's
      receipt is routing work, not editing work. **  Arm (7) establishes why nothing numerical
      waits on it: every sigma figure P16 prints rounds IDENTICALLY on 3.044 and on 3.046, so the
      defect was a naming one throughout.  The sentence now names both, which is one state, and
      the token survives for S1.

  (7) REPORTED, NOT FIXED.  ** Three clusters of printed figures are carried by no receipt their
      sentence cites. **  Measured in arm (9).  (A) the specific-entropy paragraph in sec:peak --
      3.60 k_B, 2.77 k_B, 1.15e10 k_B, 5.5e-10, "one part in 2e9" -- in a paragraph that calls
      itself "quantitative" and cites N7, which measures BITS and carries none of them.  Arm
      (10) reproduces all five from banked constants, so this cluster is pinnable and is pinned
      HERE.  (B) the band-period obstacle in sec:interior -- 0.304 against 3.565, "a factor of
      11.7", and c_s "runs from 0.018 at turnaround" -- cited to
      `P16_the_passage_is_phase_only_above_the_first_peak`, which carries none of the four.  Not
      reproduced this pass; routed.  (C) the dissociation thresholds in sec:network -- T_9 ~ 1.2
      for deuterium and 15.8 for helium-4 -- in a sentence that cites nothing.  Arm (11) shows a
      single-exponential tail model does NOT return the pair (it needs B/T = 21.5 for deuterium
      against 20.8 for helium-4), so these come from a fuller nuclear-statistical-equilibrium
      accounting that no receipt in the corpus carries.  Routed, with that measurement attached.

  (8) REPORTED, NOT FIXED.  ** sec:scoping still says whether the tilt displacement is a tension
      "needs a constraint on $n_s$ that does not run through the damping tail". **  P15's own
      reading moved at r7830: the fit still supplies no off-tail constraint, but the comparison
      does, and at fixed cosmology the data lean against the signature at the 2-sigma line and
      not past it.  P16 states the need and not the supply.  A wording question for 69, since the
      sentence is not false -- only incomplete about what the companion now reports.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that 5.45e-2 is the right physics ** -- arm (6) shows it is what the paper's own two
  printed numbers return, which is a consistency statement about the paper and NOT a
  re-derivation of the determination.  Which background fixes it is (5), and it is 69's.
  ** Not that 3.044 is derived here, or that the corpus's citation for it is adequate ** -- the
  corpus carries it uncited in P15, P18 and Y11, and this pass did not repair that.
  ** Not that clusters (B) and (C) are wrong ** -- only that no receipt carries them, which is a
  statement about the corpus's bookkeeping and not about the figures.
  ** Not that the unpinned figures of cluster (A) were in doubt ** -- arm (10) reproduces them.

rc=0 on success.  Run: python3 P16_the_network_runs_three_exactly_...py        (no deps)
"""
import io
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
ARMS = []


def check(label, ok, extra=''):
    ARMS.append(label)
    print(('  %-4s %s' % ('PASS' if ok else 'FAIL', label)) + (('   [%s]' % extra) if extra else ''))
    if not ok:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', io.open(os.path.join(ROOT, path), encoding='utf-8',
                                      errors='replace').read())


P16 = flat('corpus/cosmogenesis_paper.tex')
P15 = flat('corpus/CR_cosmology.tex')
P18 = flat('corpus/CR_synthesis.tex')

# ---------------------------------------------------------------------------
# Constants, each with its provenance stated at the point of use.  No figure below
# originates in this file.
# ---------------------------------------------------------------------------
# the measured primordial values and their errors, as Y10 in L550_third_mechanism uses them
OBS_YP, SIG_YP = 0.2453, 0.0034                    # Aver et al. 2021, via Y10
OBS_D, SIG_D = 2.527e-5, 0.030e-5                  # Cooke et al. 2018, via Y10
# the network's own outputs, as P16_theory_error_and_likelihood reports them (StarLib, eta10=6.13)
NET_YP, NET_D = 0.2471, 2.505e-5
# the propagated nuclear-rate theory errors, same receipt
THEO_YP_FRAC, THEO_D_FRAC = 0.006, 0.011
# the banked right-handed run's pairs, Y10's own control and finding
DN_FLOOR, DN_BOUND = 0.141, 0.292                  # Y11: the floor and the collider-bound case
YP_FLOOR, YP_BOUND = 0.2489, 0.2509                # Y10
D_FLOOR, D_BOUND = 2.55e-5, 2.60e-5                # Y10
NEFF_LATER, NEFF_FIRST = 3.044, 3.046              # P15/P18/Y11, and Mangano 2005
ACT_JOINT, ACT_SIG = 2.89, 0.11                    # ACT DR6 + light elements, via Y11
# ** the paper's own two printed numbers for the progenitor are READ OUT OF THE PAPER and not
#    retyped: a check whose label says "the paper's" and whose value is a literal stays green when
#    the paper moves, which is the defect check_unread_figure exists to catch. **
_m = re.search(r'a mass \$(\d+\.\d+)\\times10\^\{(\d+)\}\$~kg', P16)
M_PAPER_KG = float(_m.group(1)) * 10.0 ** int(_m.group(2))
_a = re.search(r'against the observable leg\'s \$(\d+\.\d+)\$', P16)
A_EQ_MPC = float(_a.group(1))
_c = re.search(r'\$A\\rho\^2/4=(\d+\.\d+)\$~Mpc', P16)
CLOSURE_PRINTED = float(_c.group(1))
_r = re.findall(r'\\rho(?:\\;)?\\simeq(?:\\;)?(\d+\.\d+)\\times10\^\{-2\}', P16)
RHO_PRINTED = float(_r[0]) * 1e-2
# and the generating receipt's own Lambda is read out of ITS source, so this pin fails if it moves
_GEN = 'P16_the_progenitor_composition_is_bracketed'
SRC_GEN = io.open(os.path.join(HERE, _GEN + '.py'), encoding='utf-8', errors='replace').read()
# ⛭ r7833 (69): FORK (1) RULED -- branch (i), the receipt takes the background the distance data fix.
#   STATE A: the generating receipt still carries the standard model's literal Lambda (the defect).
#   STATE B: it computes Lambda from the distances' point (H0, Omega_m) = (68.60, 0.2973) (repaired).
_mA = re.search(r'^LAM, MPC = ([0-9.e+-]+),', SRC_GEN, re.M)
_mB = re.search(r'^_H0_SI = ([0-9.]+)e3 / 3\.0857e22\nLAM = 3\.0 \* _H0_SI \*\* 2 \* \(1\.0 - ([0-9.]+)\)', SRC_GEN, re.M)
GEN_STATE_B = _mA is None and _mB is not None
if _mA is not None:
    LAM_RECEIPT = float(_mA.group(1))
else:
    _h = float(_mB.group(1)) * 1e3 / 3.0857e22
    LAM_RECEIPT = 3.0 * _h ** 2 * (1.0 - float(_mB.group(2))) / 2.99792458e8 ** 2
print('  generating receipt: %s, Lambda = %.4e' % ('STATE B -- on the distances\' background' if GEN_STATE_B
                                               else 'STATE A -- the standard model\'s literal', LAM_RECEIPT))
# the frozen-mode margin, read from the receipt's own print line AND from the paper
SRC_FROZEN = io.open(os.path.join(HERE, 'P16_every_mode_is_frozen_at_the_crossing.py'),
                     encoding='utf-8', errors='replace').read()
MARGIN_RECEIPT = float(re.search(r'freezes with ([0-9.]+)% of the leg to spare', SRC_FROZEN).group(1))
MARGIN_PAPER = float(re.search(r'\$([0-9.]+)\$ per cent of the collapsing leg', P16).group(1))
# the two dissociation thresholds, read from the paper rather than retyped
_t9 = re.search(r'T_9\\simeq([0-9.]+)\$ for deuterium and \$([0-9.]+)\$ for helium-4', P16)
T9_D, T9_HE = float(_t9.group(1)), float(_t9.group(2))
# the three papers' Standard Model values, read at source
NEFF_P16 = float(re.search(r'the \$(\d\.\d+)\$ the companion cosmology quotes', P16).group(1))
NEFF_P16_FIRST = float(re.search(r'effective number \$N_\{\\mathrm\{eff\}\}=(\d\.\d+)\$', P16).group(1))
NEFF_P15 = float(re.search(r"the Standard Model's \$(\d\.\d+)\$", P15).group(1))
NEFF_P18 = float(re.search(r'N_\{\\rm eff\}=(\d\.\d+)', P18).group(1))
# the measured values the paper now prints, read out of it
_yp = re.search(r'\$Y_p=(\d\.\d+)\\pm(\d\.\d+)\$', P16)
_dh = re.search(r'\$D/H=\((\d\.\d+)\\pm(\d\.\d+)\)\\times10\^\{-5\}\$', P16)
YP_PAPER, SIG_YP_PAPER = float(_yp.group(1)), float(_yp.group(2))
# the same sentence's group prints the Planck pair this receipt's arm runs at, so they are pinned
# here too rather than left standing beside a citation that would not fail if they were wrong
ETA10_PAPER = float(re.search(r'eta_\{10\}=(\d\.\d+)\\pm', P16).group(1))
OMBH2_PAPER = float(re.search(r'\\Omega_bh\^2=(\d\.\d+)', P16).group(1))
D_PAPER, SIG_D_PAPER = float(_dh.group(1)) * 1e-5, float(_dh.group(2)) * 1e-5
# cluster A's four, read out of the paper
_cA = (float(re.search(r'\\simeq([0-9.]+)\\,k_B\n?\s*per baryon', P16.replace('\n', ' ')).group(1))
       if False else None)
CL_A = [float(x) for x in (
    re.search(r'adds \$\\tfrac43 E/T\\simeq([0-9.]+)\\,k_B\$', P16).group(1),
    re.search(r'\$([0-9.]+)\\,k_B\$ at four', P16).group(1),
    re.search(r's/n_b\\simeq([0-9.]+)\\times10\^\{10\}', P16).group(1),
    re.search(r'perturbing \$\\eta\$ by \$([0-9.]+)\\times10\^\{-10\}', P16).group(1))]
# physical constants
G, C, MPC = 6.674e-11, 2.99792458e8, 3.0857e22
M_N_MEV, T_PK_MEV = 938.91898, 174.0               # PDG nucleon mass; P16_peak_temperature's T_pk
ETA10 = 6.13                                       # Planck 2018, as P16 sec:verdict prints it
ZETA3 = 1.2020569031595943
B_D_MEV, B_HE4_MEV = 2.224566, 28.29567            # AME2020 binding energies
K_PER_MEV = 1.160451e10

print(__doc__.split('rc=0')[0])
print('=' * 78)
print('PART 1 -- THE TWO FIXES THAT ARE ARITHMETIC')
print('=' * 78)

# ---------------------------------------------------------------------- A (1)
src_frozen = SRC_FROZEN
gloss_factor = 0.2 / MARGIN_RECEIPT
print('  the retired gloss read 0.2 per cent against the table\'s 0.065, a factor of %.2f,' % gloss_factor)
print('  and 0.2 > 0.065, so the gloss claimed a SMALLER margin than the computation gives --')
print('  the harder case for the claim, which is why it is not a conservative slip.')
check('Ⓐ① the cited receipt carries its own 0.065 figure and its r3124 record of the gloss, the '
      'gloss is threefold out (factor %.2f) and in the less conservative direction, and P16 now '
      'prints 0.065 while the retired wording is gone' % gloss_factor,
      'a fifth of a per cent' in src_frozen            # the r3124 record of the error
      and 2.9 < gloss_factor < 3.2 and 0.2 > MARGIN_RECEIPT
      and abs(MARGIN_PAPER - MARGIN_RECEIPT) < 0.0004      # the pin: paper against receipt
      and abs(MARGIN_RECEIPT - 0.065) < 0.0004
      and 'a fifth of a per cent' not in P16,
      'factor %.3f' % gloss_factor)

# ---------------------------------------------------------------------- B (2)
src_net = io.open(os.path.join(ROOT, 'receipts', 'P16_cosmogenesis_paper', 'bbn_network.py'),
                  encoding='utf-8', errors='replace').read()
r_nu = (4.0 / 11.0) ** (1.0 / 3.0)
# N_eff == (8/7)(11/4)^{4/3} rho_nu/rho_gamma; with three species at exactly r_nu that is 3.
n_eff_module = 3.0 * (r_nu ** 4) * (11.0 / 4.0) ** (4.0 / 3.0)
print()
print('  the module sets r_nu = (4/11)^(1/3) = %.6f and counts 3 species at it, so the effective'
      % r_nu)
print('  number the integration runs on is N_eff = %.12f -- three exactly, the correction absent.'
      % n_eff_module)
check('Ⓑ② the network module carries the instantaneous ratio and three species with no energy-'
      'transfer term, so the count it runs on is 3 exactly',
      '(4.0/11.0)**(1.0/3.0)' in src_net
      and '3 nu(7/8*2 each, at T_nu)' in src_net
      and abs(n_eff_module - 3.0) < 0.0000000001,
      'N_eff = %.12f' % n_eff_module)

# ---------------------------------------------------------------------- C (3)
dyp_dn = (YP_FLOOR - NET_YP) / DN_FLOOR            # Y10's own pair, per unit N_eff
dd_dn = (D_FLOOR - 2.50e-5) / DN_FLOOR             # Y10's baseline is 2.50e-5
omitted = NEFF_FIRST - 3.0                         # what the ratio leaves out, 0.046
omitted_later = NEFF_LATER - 3.0                   # 0.044
frac_of_floor = omitted_later / DN_FLOOR
shift_yp = dyp_dn * omitted_later
shift_d_frac = dd_dn * omitted_later / 2.50e-5
sig_yp_tot = math.sqrt(SIG_YP ** 2 + (THEO_YP_FRAC * NET_YP) ** 2)
print()
print('  Y10\'s banked pair gives dY_p/dN_eff = %.5f and d(D/H)/dN_eff = %.4e per unit.'
      % (dyp_dn, dd_dn))
print('  The omitted %.3f therefore moves Y_p by %.5f and D/H by %.2f per cent -- %.3f of what'
      % (omitted_later, shift_yp, 100 * shift_d_frac, frac_of_floor))
print('  the three right-handed states move them at their floor, and in the same direction.')
check('Ⓒ③ the omitted non-instantaneous correction moves helium-4 and deuterium in the same '
      'direction as the right-handed states and by less than a third of their floor shift, and '
      'the helium move is inside the measurement-plus-theory error',
      0.0 < frac_of_floor < 0.3333333333
      and shift_yp > 0 and shift_d_frac > 0
      and shift_yp < sig_yp_tot
      and abs(omitted - 0.046) < 0.0000001 and abs(omitted_later - 0.044) < 0.0000001,
      'frac %.4f, dY_p %.5f vs sigma %.5f' % (frac_of_floor, shift_yp, sig_yp_tot))

# ---------------------------------------------------------------------- D (4)
check('Ⓓ④ P16 now names the instantaneous ratio, the count 3, both values with their statuses, '
      'and keeps the 3.046 token S1 pins; P15 and P18 carry 3.044 and P16 now does too',
      'instantaneous}-decoupling ratio' in P16
      and 'the count the integration itself runs on is $3$ exactly' in P16
      and 'the effective number $N_{\\mathrm{eff}}=3.046$' in P16
      and 'the $3.044$ the companion cosmology quotes' in P16
      and "the Standard Model's $3.044$" in P15
      and 'N_{\\rm eff}=3.044' in P18
      and abs(NEFF_P16 - 3.044) < 0.0004 and abs(NEFF_P15 - 3.044) < 0.0004
      and abs(NEFF_P18 - 3.044) < 0.0004 and abs(NEFF_P16_FIRST - 3.046) < 0.0004
      and abs(NEFF_P16 - 3.0 - omitted_later) < 0.0000001
      and abs(NEFF_P16_FIRST - 3.0 - omitted) < 0.0000001,
      'P16 %.3f and %.3f, P15 %.3f, P18 %.3f' % (NEFF_P16_FIRST, NEFF_P16, NEFF_P15, NEFF_P18))

print()
print('=' * 78)
print('PART 2 -- WHICH BACKGROUND THE DETERMINATION IS ON')
print('=' * 78)

# ---------------------------------------------------------------------- E (5)
# 0.05451 to two significant figures is 5.5e-2, so "5.4e-2" was not a coarser printing of it.
two_sig = float('%.2g' % 0.05451)
print('  0.05451 printed to two significant figures is %.3g, not 0.054, so the paper\'s two'
      % two_sig)
print('  figures named two numbers rather than one number twice.')
check('Ⓔ⑤ 5.45e-2 and 5.4e-2 are two values and not one rounded one, and P16 now prints the '
      'former in both places with the retired one gone',
      abs(two_sig - 0.055) < 0.0000001
      and abs(RHO_PRINTED - 0.0545) < 0.00002
      and abs(RHO_PRINTED * 1e2 - 5.45) < 0.002
      and all(abs(float(x) * 1e-2 - 0.0545) < 0.00002 for x in _r)
      and bool(_r) and set(_r) == {'5.45'}
      and '5.4\\times10^{-2}' not in P16,
      'the paper prints %s' % ', '.join(_r))

# ---------------------------------------------------------------------- F (6)
# rho = sqrt(4 a_eq / A) with A = 2M, on the paper's OWN two printed numbers.
A_paper = 2.0 * (G * M_PAPER_KG / C ** 2) / MPC                    # Mpc
rho_paper = math.sqrt(4.0 * A_EQ_MPC / A_paper)
alpha_receipt = math.sqrt(3.0 / LAM_RECEIPT) / MPC                 # Mpc
A_receipt = 2.0 * alpha_receipt / (3.0 * math.sqrt(3.0))           # the Nariai cap, as the receipt takes it
M_receipt_kg = (A_receipt / 2.0) * MPC * C ** 2 / G
rho_receipt = math.sqrt(4.0 * (5065.0 / 3399.0) / A_receipt)       # the receipt's own a_eq too
print()
print('  on the paper\'s own M = %.2e kg:  A = %.1f Mpc, and rho = sqrt(4 a_eq/A) = %.5f'
      % (M_PAPER_KG, A_paper, rho_paper))
print('  on the generating receipt\'s Lambda = %.4e: M = %.2e kg, A = %.1f Mpc, rho = %.5f'
      % (LAM_RECEIPT, M_receipt_kg, A_receipt, rho_receipt))
print('  ** the paper\'s two printed numbers return the paper\'s own figure; the difference is')
print('     the MASS and nothing else, and it is the number r6921 corrected. **')
check('Ⓕ⑥ the paper\'s own printed mass and equality radius return 0.0545, and the generating '
      'receipt\'s Nariai cap on Lambda = 1.1056e-52 returns 0.05386, which it prints as 0.0539, '
      'with a mass of 4.269e52 kg '
      'rather than the 4.17e52 the paper names',
      abs(rho_paper - 0.05450) < 0.00002
      and abs(M_PAPER_KG * 1e-52 - 4.17) < 0.004
      and ((not GEN_STATE_B
            and abs(rho_receipt - 0.05386) < 0.00002
            and abs(M_receipt_kg - 4.269e52) / 4.269e52 < 0.0004
            and abs(LAM_RECEIPT * 1e52 - 1.1056) < 0.0004
            and rho_paper > rho_receipt)
           # STATE B: the receipt's Nariai cap IS the paper's mass and returns the paper's rho
           or (GEN_STATE_B
               and abs(M_receipt_kg - M_PAPER_KG) / M_PAPER_KG < 0.002
               and abs(rho_receipt - rho_paper) < 0.00005)),
      'paper %.5f, receipt %.5f, M_receipt %.3e' % (rho_paper, rho_receipt, M_receipt_kg))

# ---------------------------------------------------------------------- G (7)
# the closure the paper asserts to four figures, on each self-consistent pair and on the mix
clos_paper = A_paper * rho_paper ** 2 / 4.0
clos_receipt = A_receipt * rho_receipt ** 2 / 4.0
clos_mixed = A_receipt * rho_paper ** 2 / 4.0
print()
print('  A rho^2/4 = %.4f Mpc on the paper\'s pair, %.4f on the receipt\'s, and %.4f if the'
      % (clos_paper, clos_receipt, clos_mixed))
print('  paper\'s rho is read with the receipt\'s mass -- %.1f per cent out.'
      % (100 * abs(clos_mixed - A_EQ_MPC) / A_EQ_MPC))
check('Ⓖ⑦ the four-figure closure the paper asserts holds on either self-consistent pair and '
      'fails by more than two per cent only when the two are mixed, so the closure identifies '
      'the mass as the single quantity that moved',
      abs(clos_paper - A_EQ_MPC) < 0.0005
      and abs(clos_receipt - A_EQ_MPC) < 0.0015
      and (GEN_STATE_B or abs(clos_mixed - A_EQ_MPC) / A_EQ_MPC > 0.02)
      and abs(CLOSURE_PRINTED - clos_paper) < 0.0005
      and abs(A_EQ_MPC - 1.4905) < 0.00004,
      'paper %.4f, receipt %.4f, mixed %.4f' % (clos_paper, clos_receipt, clos_mixed))

# ---------------------------------------------------------------------- H (8)
sig_d_tot = math.sqrt(SIG_D ** 2 + (THEO_D_FRAC * NET_D) ** 2)
t_yp = (NET_YP - OBS_YP) / sig_yp_tot
t_d = (NET_D - OBS_D) / sig_d_tot
print()
print('  from the values P16 now prints: helium %+.2f sigma, deuterium %+.2f sigma' % (t_yp, t_d))
check('Ⓗ⑧ P16 now prints both measured values, and the +0.5 and -0.5 sigma it reports are '
      'reproduced from them with the propagated theory errors',
      abs(YP_PAPER - OBS_YP) < 0.00004 and abs(SIG_YP_PAPER - SIG_YP) < 0.00004
      and abs(D_PAPER - OBS_D) < 0.0004e-5 and abs(SIG_D_PAPER - SIG_D) < 0.0004e-5
      and abs(YP_PAPER - 0.2453) < 0.00004 and abs(SIG_YP_PAPER - 0.0034) < 0.00004
      and abs(D_PAPER * 1e5 - 2.527) < 0.0004 and abs(SIG_D_PAPER * 1e5 - 0.030) < 0.0004
      and abs(ETA10_PAPER - 6.13) < 0.004 and abs(ETA10_PAPER - ETA10) < 0.0000001
      and abs(OMBH2_PAPER - 0.02237) < 0.000004
      and abs(round(t_yp, 1) - 0.5) < 0.0000001
      and abs(round(t_d, 1) + 0.5) < 0.0000001
      and 'the $0.2453\\pm0.0034$ the cosmogenesis paper quotes there' in P15,
      '%+.3f and %+.3f' % (t_yp, t_d))

print()
print('=' * 78)
print('PART 3 -- THE FIGURES NO CITED RECEIPT CARRIES')
print('=' * 78)

# ---------------------------------------------------------------------- I (9)
CLUSTERS = {
    'A  sec:peak, the entropy budget': (
        ['3.60', '2.77', '1.15\\times10^{10}', '5.5\\times10^{-10}'],
        ['N7_the_peak_is_an_erasure_channel_and_its_output_is_the_conserved_charge']),
    'B  sec:interior, the band period': (
        ['0.304', '3.565', '11.7', '0.018'],
        ['P16_the_passage_is_phase_only_above_the_first_peak']),
    'C  sec:network, the thresholds': (
        ['1.2', '15.8'], []),
}
unpinned = {}
for name, (figs, keys) in CLUSTERS.items():
    src = ''
    for k in keys:
        for d in os.listdir(os.path.join(ROOT, 'receipts')):
            p = os.path.join(ROOT, 'receipts', d, k + '.py')
            if os.path.exists(p):
                src += io.open(p, encoding='utf-8', errors='replace').read()
    bare = [f.replace('\\times10^{', 'e').replace('}', '').replace('{', '') for f in figs]
    missing = [b for b in bare if b not in src]
    unpinned[name] = missing
    print('  %-34s printed %d, carried by the cited receipt %d'
          % (name, len(figs), len(figs) - len(missing)))
check('Ⓘ⑨ all three clusters are printed in P16 and no figure of any of them is carried by the '
      'receipt its sentence cites (cluster C\'s sentence cites none at all)',
      all(len(m) == len(CLUSTERS[n][0]) for n, m in unpinned.items())
      and '3.60\\,k_B' in P16 and '0.304' in P16 and 'T_9\\simeq1.2' in P16,
      '; '.join('%s %d/%d' % (n.split()[0], len(m), len(CLUSTERS[n][0]))
                for n, m in sorted(unpinned.items())))

# ---------------------------------------------------------------------- J (10)
# cluster A, reproduced -- so it is pinnable, and this arm pins it.
e_infall = M_N_MEV / 2.0                                  # the infall energy per nucleon
s_thermalise = (4.0 / 3.0) * e_infall / T_PK_MEV           # k_B per baryon
s_erase = 4.0 * math.log(2.0)                              # four bits
g_s = 2.0 + 3.0 * (7.0 / 8.0) * 2.0 * (4.0 / 11.0)         # photons + 3 nu post-annihilation
eta = ETA10 * 1e-10
s_per_b = (2.0 * math.pi ** 2 / 45.0) * g_s / (eta * 2.0 * ZETA3 / math.pi ** 2)
d_eta_rel = (s_thermalise + s_erase) / s_per_b
one_part_in = 1.0 / d_eta_rel
print()
print('  4/3 E/T   = %.4f k_B      (E = m_N c^2/2, T = T_pk = %.0f MeV)' % (s_thermalise, T_PK_MEV))
print('  four bits = %.4f k_B' % s_erase)
print('  s/n_b     = %.4e k_B      (g_*s = %.3f, eta = %.2fe-10)' % (s_per_b, g_s, ETA10))
print('  the sum over it = %.4e, i.e. one part in %.3e' % (d_eta_rel, one_part_in))
check('Ⓙ⑩ cluster A reproduces from banked constants to the precision P16 prints it -- 3.60, '
      '2.77, 1.15e10, 5.5e-10 and one part in 2e9 -- so it is pinnable and is pinned here',
      abs(s_thermalise - CL_A[0]) < 0.004
      and abs(s_erase - CL_A[1]) < 0.004
      and abs(s_per_b - CL_A[2] * 1e10) < 0.004e10
      and abs(d_eta_rel - CL_A[3] * 1e-10) < 0.048e-10
      and abs(round(one_part_in / 1e9) - 2.0) < 0.0000001
      and abs(CL_A[0] - 3.60) < 0.004 and abs(CL_A[2] - 1.15) < 0.004,
      '%.4f %.4f %.4e %.4e 1/%.3e' % (s_thermalise, s_erase, s_per_b, d_eta_rel, one_part_in))

# ---------------------------------------------------------------------- K (11)
# cluster C, NOT reproduced: one exponential tail cannot carry both thresholds.
x_d = B_D_MEV / (T9_D / K_PER_MEV * 1e9)
x_he = B_HE4_MEV / (T9_HE / K_PER_MEV * 1e9)
print()
print('  the two printed thresholds imply B/T = %.2f for deuterium and %.2f for helium-4,'
      % (x_d, x_he))
print('  so no single exponential-tail criterion returns both: the pair comes from a fuller')
print('  nuclear-statistical-equilibrium accounting, which no receipt in the corpus carries.')
check('Ⓚ⑪ cluster C is not reproduced by a single-exponential tail model -- the two printed '
      'thresholds need different B/T, 21.5 against 20.8 -- so it is routed rather than pinned, '
      'and this receipt asserts the gap and not the figures',
      (abs(x_d - 21.5) < 0.05 and abs(x_he - 20.8) < 0.05 and x_d > x_he)
      # r7835 (69): STATE B -- cc66's r7837 returns the pair with one exponent, ln(1/eta) = 21.22, to the
      #   printed digits once helium-4 prints 15.5; P16 now names that criterion and cites cc66's receipt
      or (abs(T9_HE - 15.5) < 1e-9 and abs(x_he - 21.18) < 0.05 and abs(x_d - 21.5) < 0.05),
      'B/T %.3f vs %.3f' % (x_d, x_he))

print()
print('=' * 78)
check('Ⓛ⑫ eleven substantive arms were registered above this one and all of them ran',
      len(ARMS) == 11)
print('=' * 78)
if FAILED:
    print('\n%d ARM(S) FAILED:' % len(FAILED))
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('\nALL %d ARMS PASS' % len(ARMS))
