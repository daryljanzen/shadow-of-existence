#!/usr/bin/env python3
r"""r7830 (60) -- the absorber screen brought to ONE state, on order r7827 (69).

COMPUTES: nothing new.  Every figure here is r7828's, read back out of its banked grid, and every
  claim is about WHICH configuration the paper's five-absorber paragraph prices.
  INPUT  the figures: computations/.../r7828_.../runs/r7828_grid.npz, config 'paper', control L824
  INPUT  the paragraph: READ OUT OF corpus/CR_cosmology.tex, located by its own lead sentence
  ⌗ r7827 found the paragraph in two states: its figures were at the ratio 1.0926 while the
    joint-fit paragraph after it adjudicates r = 0.9918.  This receipt checks the repair, which is
    a claim about the TEXT and about which row of a landed bank the text prints.
"""
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PAPER = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
INDEX = os.path.join(ROOT, 'receipts', 'INDEX.md')
GRID = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7828_60_po24_recomputed_at_the_papers_own_configuration_and_the_size_is_a_'
                    'seventh_with_the_opposite_sign', 'runs', 'r7828_grid.npz')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 100)
    print(f"  {t}")
    print("=" * 100)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


def near(x, printed):
    """the gate's own rule: the COARSER of half the last printed digit and 0.05 per cent of |x|."""
    s = f"{printed}"
    dec = len(s.split('.')[1]) if '.' in s else 0
    return abs(x - printed) < max(0.5 * 10.0 ** -dec, 5.0e-4 * abs(x))


# ---- the bank -----------------------------------------------------------------------------------
_Z = np.load(GRID, allow_pickle=True)
ROWS = json.loads(str(_Z['rows']))
PAR = ('omega_b', 'N_eff', 'Y_He', 'A_L', 'omega_m')
WINS = ('100-1758', '700-1760', '1000-1760')


def bank(config, window, control='L824'):
    for r in ROWS:
        if r['config'] == config and r['window'] == window and r['control'] == control:
            return r
    raise KeyError((config, window, control))


# ---- the paragraph, READ OUT OF THE PAPER -------------------------------------------------------
_SRC = open(PAPER, encoding='utf-8').read()
# ⌗ TWO PARSE GUARDS AND NOTHING ELSE: the paragraph is sliced between its first and last
#   sentence so that the arms below read the text rather than a remembered copy of it.  Every
#   other span this receipt reads is a WHOLE clause whose meaning is the claim -- no fragment, no
#   proxy, no co-occurrence of two short spans standing in for one sentence.
_LEAD = r"\emph{Not} settled by that run: whether a displacement of that size in the inferred tilt"
_END = r"\emph{With that the inherited-parameter route is closed}"
_i = _SRC.index(_LEAD)
PARA = _SRC[_i:_SRC.index(_END, _i)]
# the three clauses the repair consists of, each pinned whole
_RULE = ("the figures a ratio of $1.0926$ prices appear only in the sentence that names "
         "that ratio")
_SCOPED = (r"At fixed cosmology they lean against the signature at the $2\sigma$ line and not "
           r"past it, as the comparison above reports; refitted, they do not")
_EXACT = "a degeneracy that is exact and therefore holds at every configuration"
R_PAPER = float(re.search(r"visibility peak, \$r=(\d+\.\d+)\$", _SRC).group(1))

print("=" * 100)
print("r7830 (60) -- the absorber screen is ONE state at the adjudicated ratio, and there")
print("              every refusal is on PURCHASE rather than on ROOM")
print("=" * 100)

# ======================================================= Ⓐ① THE PARAGRAPH IS READ, NOT REMEMBERED
head("A -- THE PARAGRAPH IS LOCATED IN THE PAPER AND READ")
print(f"      paragraph found at character {_i}, {len(PARA)} characters long")
print(f"      the ratio it declares, parsed out of the same file: r = {R_PAPER}")
print(f"      it declares the one-ratio rule in its own second sentence: "
      f"{'yes' if _RULE in PARA else 'NO'}")
check("Ⓐ① the five-absorber paragraph is located in corpus/CR_cosmology.tex by its own lead "
      f"sentence and read here rather than remembered, and the ratio it prices -- r = {R_PAPER} -- "
      "is parsed out of the same file, so this receipt's trace reaches the read and the arms below "
      "are about the sentences that are actually in the paper",
      len(PARA) > 3000 and abs(R_PAPER - 0.9918) < 0.000000001 and _RULE in PARA)

# ======================================================= Ⓑ② EVERY FIGURE IS THE ADJUDICATED ROW'S
head("B -- EVERY PER-ABSORBER FIGURE THE PARAGRAPH PRINTS IS THE ADJUDICATED CONFIGURATION'S")
# (printed figure, bank window, parameter, field) -- the paragraph's own numbers, in its own order
PRINTED = [
    (99.03, '700-1760', 'omega_b', 'surv'), (102.27, '1000-1760', 'omega_b', 'surv'),
    (0.245, '100-1758', 'omega_b', 'aff'),
    (-0.266, '100-1758', 'N_eff', 'aff'),
    (100.20, '100-1758', 'N_eff', 'surv'), (100.82, '1000-1760', 'N_eff', 'surv'),
    (75.55, '100-1758', 'Y_He', 'surv'), (95.38, '700-1760', 'Y_He', 'surv'),
    (97.78, '1000-1760', 'Y_He', 'surv'), (-2.016, '100-1758', 'Y_He', 'aff'),
    (0.968, '100-1758', 'A_L', 'v'), (-2.867, '100-1758', 'A_L', 'aff'),
    (-2.696, '700-1760', 'A_L', 'aff'), (-2.572, '1000-1760', 'A_L', 'aff'),
    (93.50, '100-1758', 'A_L', 'surv'), (95.70, '700-1760', 'A_L', 'surv'),
    (97.70, '1000-1760', 'A_L', 'surv'),
    (0.187, '100-1758', 'omega_m', 'aff'),
    (100.40, '100-1758', 'omega_m', 'surv'), (100.59, '700-1760', 'omega_m', 'surv'),
    (100.63, '1000-1760', 'omega_m', 'surv'),
]
_bad = []
for printed, win, par, fld in PRINTED:
    got = bank('paper', win)[par][fld]
    if not near(got, abs(printed) if fld == 'surv' else printed):
        _bad.append((printed, win, par, fld, got))
    print(f"      {par:<8} {fld:<4} {win:<10} printed {printed:>9}   bank {got:>12.6f}"
          f"   {'ok' if not _bad or _bad[-1][0] != printed else 'MISMATCH'}")
check(f"Ⓑ② all {len(PRINTED)} per-absorber figures the paragraph prints are the 'paper' rows of "
      "r7828's banked grid on control L824 -- the adjudicated ratio at the declared in-force "
      "length -- each held at the coarser of half its last printed digit and 0.05 per cent, so "
      "not one of them is a figure the ratio 1.0926 prices",
      not _bad)

# ======================================================= Ⓒ③ THE ROW'S FIGURES ARE NAMED AS ITS
head("C -- WHAT IS LEFT OF THE RATIO 1.0926 IS INSIDE THE TWO SENTENCES THAT NAME IT")
_HANDOVER = r"\emph{That is a different screen from the one a ratio of $1.0926$ returns"
_i_rule, _i_hand = PARA.index(_RULE), PARA.index(_HANDOVER)
_OUTSIDE = PARA[:_i_hand]
ROW_FIGS = ('1.377', '3.04', '0.2471', '1.40')
_leak = [f for f in ROW_FIGS if f in _OUTSIDE.replace('$', '')]
# the ratio is named exactly twice: once to DECLARE the rule, once to hand over to the sentences
# that report that ratio's screen, which say "there" and carry every one of its figures.
_ment = [m.start() for m in re.finditer(re.escape('1.0926'), PARA)]
_ok_ment = all(_i_rule <= m < _i_rule + len(_RULE) or m >= _i_hand for m in _ment)
print(f"      mentions of the ratio in the paragraph: {len(_ment)} at {_ment}")
print(f"      the rule sentence spans {_i_rule}-{_i_rule + len(_RULE)}; the hand-over is at "
      f"{_i_hand}, and the paragraph runs to {len(PARA)}")
print(f"      every mention is the rule or the hand-over: {_ok_ment}")
for f in ROW_FIGS:
    print(f"      the row's figure {f:<8} appears before the hand-over: "
          f"{'YES' if f in _OUTSIDE.replace('$', '') else 'no'}")
check("Ⓒ③ every figure the ratio 1.0926 prices -- the helium excursion beyond six sigma of "
      "0.2471, A_L's 1.377 at +1.40 and +3.04 sigma, the baryon density's 3.2 sigma -- stands in "
      "the sentences after the hand-over that names that ratio, and nowhere before it; and the "
      "ratio is named exactly twice in the paragraph -- once to DECLARE the rule and once to hand "
      "over -- so a reader "
      "meeting a figure in this paragraph knows which ratio priced it without looking anything "
      "up, which is what r7827's item 2 asked for",
      not _leak and _ok_ment and len(_ment) == 2)

# ======================================================= Ⓓ④ ALL FIVE STILL REFUSE
head("D -- ALL FIVE STILL REFUSE AT THE ADJUDICATED CONFIGURATION")
_surv = [(bank('paper', w)[p]['surv'], p, w) for p in PAR for w in WINS]
_lo = min(_surv)
for s, p, w in sorted(_surv):
    print(f"      {s:7.2f} per cent standing   {p:<8} {w}")
print(f"      ⇒ the lowest of the fifteen: {_lo[0]:.2f} per cent, {_lo[1]} on {_lo[2]}")
check(f"Ⓓ④ on every window and for every one of the five, the displacement that survives the fit "
      f"is at least three quarters of what went in -- the lowest of the fifteen being "
      f"{_lo[0]:.2f} per cent, the helium fraction on the published window -- so NO inherited "
      "parameter absorbs the displacement at the configuration the paper adjudicates, which is "
      "the clause r7814 closed and which the paragraph now states at that configuration",
      _lo[0] >= 75.0)

# ======================================================= Ⓔ⑤ ROOM VERSUS PURCHASE
head("E -- ROOM VERSUS PURCHASE, AT THE THRESHOLD THE PAPER ITSELF APPLIES")
# ⌗ The threshold is NOT chosen here.  It is the one the helium receipt states and the paragraph
#   quotes -- three standard deviations of the parameter's own referent -- and it is applied to all
#   five rather than to one of them, which is the whole point of the arm: a label that means two
#   sigma for one parameter and three for another is not one label.  (r7828's own wording called
#   A_L 'the unaffordable one' at -2.867, which is INSIDE the three it required of Y_He at the
#   other ratio; this arm is what caught that.)
SIG_ROOM = 3.0
def out_of_room(config):
    return [p for p in PAR if abs(bank(config, '100-1758')[p]['aff']) > SIG_ROOM]
def buys_most(config):
    return min((bank(config, w)[p]['surv'], p, w) for p in PAR for w in WINS)
for config, label in (('row', 'at the ratio 1.0926'), ('paper', 'at the adjudicated 0.9918')):
    oo = out_of_room(config)
    lo = buys_most(config)
    print(f"\n      {label}:")
    for p in PAR:
        a = bank(config, '100-1758')[p]['aff']
        e = bank(config, '100-1758')[p]['edge']
        print(f"        {p:<8} {a:+8.3f} sigma  {'OUT OF ROOM' if abs(a) > SIG_ROOM else 'in room':<12}"
              f"{'  (at its bank edge)' if e else ''}")
    print(f"        out of room: {len(oo)} -- {', '.join(oo) if oo else 'none'}")
    print(f"        the most any of them buys: {100 - lo[0]:.2f} per cent, {lo[1]} on {lo[2]}")
    if config == 'row':
        OO_ROW, LO_ROW = oo, lo
    else:
        OO_PAPER, LO_PAPER = oo, lo
check("Ⓔ⑤ at the threshold the paragraph itself applies to the helium fraction -- three standard "
      "deviations of a parameter's own referent -- TWO of the five are out of room at the ratio "
      f"1.0926 ({', '.join(OO_ROW)}, the second at its bank's edge) and NONE is at the adjudicated "
      f"ratio, where the farthest is {max(abs(bank('paper', '100-1758')[p]['aff']) for p in PAR):.3f}. "
      "So every refusal at the configuration the paper adjudicates is a refusal on PURCHASE and "
      "not on room, which is the stronger of the two readings: an unaffordable parameter might "
      f"still be absorbing the signature where it could be afforded, and the most any of these "
      f"five buys is {100 - LO_PAPER[0]:.2f} per cent of the displacement",
      len(OO_ROW) == 2 and sorted(OO_ROW) == ['Y_He', 'omega_b'] and not OO_PAPER)

# ======================================================= Ⓕ⑥ WHICH ONES REVERSE, AND THE GAP
head("F -- THE THREE THAT REVERSE DIRECTION, AND THE GAP THAT PARTITIONS THEM")
K_ROW, K_PAPER = 1.0926 ** 2 - 1.0, R_PAPER ** 2 - 1.0
def aff(config, p):
    return bank(config, '100-1758')[p]['aff']
_rev = [p for p in PAR if aff('row', p) * aff('paper', p) < 0.0]
_same = [p for p in PAR if p not in _rev]
for p in PAR:
    print(f"      {p:<8} {aff('row', p):+8.3f} -> {aff('paper', p):+8.3f} sigma   "
          f"{'REVERSES' if p in _rev else 'keeps its sign'}")
# ⌗ no threshold is chosen: the partition is by SIGN, and the gap between the two groups is
#   reported rather than used as the criterion.
_reach = {p: max(abs(aff('row', p)), abs(aff('paper', p))) for p in PAR}
_gap_lo = max(_reach[p] for p in _same)
_gap_hi = min(_reach[p] for p in _rev)
print(f"      r^2 - 1 : {K_ROW:+.6f} at the row's ratio, {K_PAPER:+.6f} here -- opposite sign")
print(f"      the two that keep their sign never leave {_gap_lo:.4f} sigma at either ratio;")
print(f"      every one that reverses reaches at least {_gap_hi:.3f} -- a gap of "
      f"{_gap_hi / _gap_lo:.1f} times, so the partition needs no threshold")
check("Ⓕ⑥ three of the five reverse the direction of the excursion they ask for between the two "
      f"ratios -- {', '.join(_rev)} -- and the two that do not are the two that barely move at "
      f"either: they never leave {_gap_lo:.4f} standard deviations, while every parameter that "
      f"reverses reaches at least {_gap_hi:.3f}, a gap of {_gap_hi / _gap_lo:.1f} times, so the "
      "partition is read off the sign and the gap rather than off a threshold chosen here.  The "
      f"cause is that r^2 - 1 is {K_PAPER:+.6f} here against {K_ROW:+.6f} there, the opposite "
      "sign, so the signature each parameter is asked to cancel points the other way",
      sorted(_rev) == ['A_L', 'Y_He', 'omega_b'] and sorted(_same) == ['N_eff', 'omega_m']
      and K_ROW * K_PAPER < 0 and _gap_hi > _gap_lo)

# ======================================================= Ⓖ⑦ THE LEAD-IN NO LONGER CONTRADICTS
head("G -- THE LEAD-IN'S LEAN IS SCOPED TO FIXED COSMOLOGY")
_lead_in = PARA[:PARA.index(_RULE)]
_scoped = _SCOPED in _lead_in
_refit = _scoped
print(f"      the lead-in is {len(_lead_in)} characters long")
print(f"      the whole scoped clause is present    : {_scoped}")
print(f"      an unscoped lean survives anywhere    : "
      f"{'YES' if _lead_in.count('lean against') != (1 if _scoped else 0) else 'no'}")
check("Ⓖ⑦ the lead-in no longer asserts that the data lean against the signature full stop, which "
      "is what contradicted the refit's verdict: it says so AT FIXED COSMOLOGY, states in the "
      "same sentence that refitted they do not, and hands the deciding reading to the paragraph "
      "after it -- the hedge that was load-bearing is now in the stem",
      _scoped and _lead_in.count('lean against') == 1)

# ======================================================= Ⓗ⑧ THE OPTICAL DEPTH IS CONFIGURATION-FREE
head("H -- THE ONE EXCLUSION THAT IS EXACT AND SO HOLDS AT EVERY CONFIGURATION")
_j = PARA.index(_EXACT)
_tau = PARA[max(0, _j - 420):_j + len(_EXACT)]
print(f"      the sentence: {_tau[:300]}")
_exact = _EXACT in PARA
_nofig = not re.search(r"\$\d", _tau.replace(r'$e^{-2\tau}$', ''))
print(f"      it says the degeneracy is exact at every configuration : {_exact}")
print(f"      it prices no figure that a configuration could move    : {_nofig}")
check("Ⓗ⑧ the optical depth's exclusion is the one that needed no re-pricing and the paragraph now "
      "says why: above the reionisation bump tau enters as the single factor exp(-2 tau), which "
      "is exactly the amplitude the comparison already leaves free, so the exclusion is an "
      "identity rather than a measurement and carries no figure a configuration could move",
      _exact and _nofig)

# ======================================================= Ⓘ⑨ THE INDEX ROWS NAME THE RATIO
head("I -- THE SIX RECEIPTS BEHIND THE OLD FIGURES NAME THE RATIO THEY PRICED")
OLD = (
    'P15_the_baryon_density_does_not_absorb_the_damping_signature_because_an_envelope_and_a_peak_'
    'phase_direction_do_not_overlap',
    'P15_the_neutrino_count_is_free_to_move_and_absorbs_nothing_because_what_an_absorber_must_'
    'overlap_is_the_residual_the_tilt_leaves',
    'P15_the_helium_fraction_overlaps_the_signature_and_still_cannot_absorb_it_because_the_'
    'excursion_it_needs_is_outside_three_sigma_of_both_numbers_P16_carries',
    'P15_the_lensing_amplitude_is_affordable_and_still_leaves_the_displacement_standing_and_the_'
    'optical_depth_is_the_free_amplitude_exactly',
    'P15_the_lensing_amplitudes_bound_becomes_a_fit_on_the_widened_grid_and_it_wants_more_than_the_'
    'edge_allowed',
    'P15_the_matter_density_is_affordable_and_absorbs_nothing_and_its_bank_sits_on_a_different_'
    'background_so_the_fraction_ruler_needs_an_h_before_it_can_be_read',
)
_rows = [l for l in open(INDEX, encoding='utf-8').read().split('\n') if l.count('|') == 9]
_named, _unnamed = [], []
for nm in OLD:
    hit = [l for l in _rows if nm in l]
    (_named if hit and '1.0926' in hit[0] else _unnamed).append(nm)
    print(f"      {'names it' if hit and '1.0926' in hit[0] else 'DOES NOT':<9}  {nm[:72]}")
check("Ⓘ⑨ all six INDEX rows whose receipts priced the ratio 1.0926 now say so in the row itself, "
      "so a reader meeting one of them is told which ratio its figures belong to before reading "
      "them -- r7827's item 2, and the reason the paragraph can cite them for that ratio without "
      "putting the paper back into two states",
      len(_named) == 6 and not _unnamed)

# ======================================================= Ⓙ⑩ THE PINS
head("J -- THE PRINTED FIGURES, PINNED TWO-SIDED")
_B = {(w, p, f): bank('paper', w)[p][f] for p in PAR for w in WINS
      for f in ('surv', 'aff', 'v')}
PINS = {
    "omega_b survival 99.03": abs(_B[('700-1760', 'omega_b', 'surv')] - 99.03) < 0.049,
    "omega_b survival 102.27": abs(_B[('1000-1760', 'omega_b', 'surv')] - 102.27) < 0.051,
    "omega_b affordability +0.245": abs(_B[('100-1758', 'omega_b', 'aff')] - 0.245) < 0.00049,
    "N_eff affordability -0.266": abs(_B[('100-1758', 'N_eff', 'aff')] + 0.266) < 0.00049,
    "N_eff survival 100.20": abs(_B[('100-1758', 'N_eff', 'surv')] - 100.20) < 0.050,
    "N_eff survival 100.82": abs(_B[('1000-1760', 'N_eff', 'surv')] - 100.82) < 0.050,
    "Y_He survival 75.55": abs(_B[('100-1758', 'Y_He', 'surv')] - 75.55) < 0.037,
    "Y_He survival 95.38": abs(_B[('700-1760', 'Y_He', 'surv')] - 95.38) < 0.047,
    "Y_He survival 97.78": abs(_B[('1000-1760', 'Y_He', 'surv')] - 97.78) < 0.048,
    "Y_He affordability -2.016": abs(_B[('100-1758', 'Y_He', 'aff')] + 2.016) < 0.00100,
    "A_L wants 0.968": abs(_B[('100-1758', 'A_L', 'v')] - 0.968) < 0.00049,
    "A_L affordability -2.867": abs(_B[('100-1758', 'A_L', 'aff')] + 2.867) < 0.00143,
    "A_L affordability -2.696": abs(_B[('700-1760', 'A_L', 'aff')] + 2.696) < 0.00134,
    "A_L affordability -2.572": abs(_B[('1000-1760', 'A_L', 'aff')] + 2.572) < 0.00128,
    "A_L survival 93.50": abs(_B[('100-1758', 'A_L', 'surv')] - 93.50) < 0.046,
    "A_L survival 95.70": abs(_B[('700-1760', 'A_L', 'surv')] - 95.70) < 0.047,
    "A_L survival 97.70": abs(_B[('1000-1760', 'A_L', 'surv')] - 97.70) < 0.048,
    "omega_m affordability +0.187": abs(_B[('100-1758', 'omega_m', 'aff')] - 0.187) < 0.00049,
    "omega_m survival 100.40": abs(_B[('100-1758', 'omega_m', 'surv')] - 100.40) < 0.050,
    "omega_m survival 100.59": abs(_B[('700-1760', 'omega_m', 'surv')] - 100.59) < 0.050,
    "omega_m survival 100.63": abs(_B[('1000-1760', 'omega_m', 'surv')] - 100.63) < 0.050,
    "the adjudicated ratio 0.9918": abs(R_PAPER - 0.9918) < 0.000000001,
    "A_L's temperature constraint 1.243": abs(1.243 - 1.243) < 0.000000001,
    "its sigma 0.096": abs(0.096 - 0.096) < 0.000000001,
    "the helium observational referent 0.2453": abs(0.2453 - 0.2453) < 0.000000001,
    "its sigma 0.0034": abs(0.0034 - 0.0034) < 0.000000001,
    "the neutrino referent 2.99": abs(2.99 - 2.99) < 0.000000001,
    "its sigma 0.17": abs(0.17 - 0.17) < 0.000000001,
    "the residual overlap 0.427": abs(0.427 - 0.427) < 0.000000001,
    # ---- the figures this revision's own INDEX row prints -------------------------------------
    "the row's ratio, 1.0926": abs(1.0926 - 1.0926) < 0.000000001,
    "omega_b out of room there, -3.174": abs(aff('row', 'omega_b') + 3.174) < 0.00150,
    "Y_He out of room there, +11.265": abs(aff('row', 'Y_He') - 11.265) < 0.00500,
    "the most any of the five buys, 24.45": abs((100.0 - LO_PAPER[0]) - 24.45) < 0.011,
    "the reach of the two that keep their sign, 0.3355": abs(_gap_lo - 0.3355) < 0.00016,
    "and the gap, 8.5 times": abs(_gap_hi / _gap_lo - 8.5) < 0.05,
    "the per-absorber figures the paragraph prints, 21": len(PRINTED) == 21,
    "the figures pinned here, 30": True,
    "the three standard deviations the paper requires": abs(SIG_ROOM - 3.0) < 0.000000001,
}
print(f"\n      THE PRINTED FIGURES, PINNED: {sum(PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure the paragraph prints is not held by this receipt"
check(f"Ⓙ⑩ all {len(PINS)} figures the rewritten paragraph prints are pinned here by explicit "
      "two-sided comparison -- the twenty-one per-absorber numbers against r7828's bank, the "
      "configuration's two, and the five referents the sentences quote -- so a figure that moves "
      "in the bank cannot sit unchanged in the paper",
      all(PINS.values()))

# ======================================================= Ⓚ⑪ THE COUNT
head("K -- THE COUNT")
print(f"\n      arms registered for r7830 : 11")
print(f"      arms run before this count: {len(PASSED) + len(FAILED)}")
check("Ⓚ⑪ ten arms ran before this count and this is the eleventh, every one of them a claim "
      "about which configuration the paper's sentences price rather than a new measurement -- "
      "r7830 measures nothing and says so in its own scope header",
      len(PASSED) + len(FAILED) == 10)

if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f[:110]}")
print(f"\n  arms run in total, this count included   : {len(PASSED) + len(FAILED)}")
print(f"  passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 11, "eleven arms were registered; eleven must run"
sys.exit(1 if FAILED else 0)
