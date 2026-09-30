"""
P10_sec_lock_quotes_the_superseding_receipt_everywhere_the_two_mode_shift_sits_under_the_wrong_pair_and_the_four_receipt_group_is_one_chain

r7059 Q1 -> 70: does `P10` `sec:lock`, as it now stands, say what its cited receipts compute?  Pre-registered at
`computations/beyond_the_wall/r7059_70_sec_lock_audit/PREDICTION.md`, committed before any cited receipt was
run.  The method is `r7043`'s: each marker group's numbers are matched at the paper's precision against the
group's source and output, with the receipts re-run.

THE RANGE.  `canonical_time.tex`, from the R^(3) expansion and the two-mode shift down through the
back-reaction paragraph.  Seven receipts in three groups:
  - G1: r7044 + r7048;
  - G2: r7058 + r7056 + r7053 + r7050;
  - G3: r7008.
⌗ One declared clarification of the pre-registration.  The claim window is everything since the previous
marker.  A paragraph break would have handed G2's recoupling, identity and threshold paragraphs to no marker at
all, where the pre-registration assigned them to G2 by name.

⛭ WHAT IS FOUND
  ① NOT FIRED.  Wherever two co-cited receipts give ONE quantity different values, the paper quotes the later:
     - the growth is of the seventh degree against the target's eighth (r7048), where r7044 had eight against
       eight;
     - the sign is positive on the whole tower against 18V = 36 pi^2 (r7058), where r7056 had it mixed below a
       crossing at m = 13;
     - r7050's crossing at m = 136 and r7053's "five powers clear" appear nowhere in the passage.
     Every figure the passage takes from an earlier receipt is one that did NOT move: 175/22, 84/31 and the rest
     are r7056's, used by r7058 exactly as filed; 120575/6 and 19775/6; and the recoupling sums 126/125 through
     81/640.
     ⇒ Nothing is marked stale for its receipt having been corrected elsewhere, as the order asked.
  ② ONE (ii), BELOW ANY HEADLINE.  The R^(3) expansion (6, 48, 160, 336), the calibration (eight, ten), the
     exponential-variable identity and the whole two-mode shift -- 4/27 (63 mu^2 - 200) mu^-4, 19/27 and
     200/63 -- close under G1.
     - G1 computes none of them.
     - All of them are computed by `P10_the_vertex_numbers_are_exact...` (r7008).
     - That receipt IS cited in the passage, but about ninety lines later and on a different sentence (the
       non-resonance and the a^-6 fall-off).
  ③ THE FOUR-RECEIPT GROUP IS ONE CHAIN, NOT FOUR SUPPORTS.
     - r7058 contributes the threshold and nothing else: its own docstring says the degrees, the six ratios and
       the recoupling sums are r7056's, "USED exactly as filed and not recomputed", and its source carries them
       as literals.
     - r7056 computes the six ratios on r7053's identity.
     - r7050 supports no number in the passage, and its own headline (a crossing at m = 136) is superseded.
     ⇒ Behind the sign stand ONE computation of the ratios and ONE new threshold.  The prose does not claim
       more.  Only the four markers on one sentence could read as four.
  ⌗ A note, not classed: "the label times it holding in a narrow band".  m x ratio runs 13.5 to 11.2 from
     m = 5 upward, but 23.9 at m = 3.

⛔ NOT CLAIMED.  No reconciliation of the two anchors' conventions (node 60's).  No physics and no re-derivation.
No prose edited.  No other seat's receipt touched.  `r7056`'s receipt takes 210 s and is gated here on its
source, with its output from the audit run recorded in the reply.  The other six are re-run here.
"""
import os
import re
import subprocess
import sys

FAILS = []


def check(name, cond, got=None):
    ok = bool(cond)
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}" + (f"   {got}" if got is not None else ""))
    if not ok:
        FAILS.append(name)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
N = {
    'r7044': 'P10_the_level_cubic_vanishes_at_every_even_level_and_the_bound_needs_no_bitensor_because_completeness_gives_a_delta',
    'r7048': 'P10_the_same_level_sum_is_orthogonality_rather_than_an_integral_and_the_completeness_bound_was_loose_by_one_power',
    'r7058': 'P10_the_cubic_normalisation_is_written_down_and_it_empties_the_residue_so_the_sign_is_positive_on_the_whole_tower',
    'r7056': 'P10_the_odd_residue_is_five_levels_and_the_sign_is_mixed_because_the_vertex_carries_covariant_not_frame_derivatives',
    'r7053': 'P10_the_cubic_vertex_is_written_down_and_K_is_not_label_independent_so_the_algebraic_channel_is_five_powers_clear',
    'r7050': 'P10_the_odd_residue_is_the_levels_below_a_crossing_linear_in_one_constant_and_a_count_bounds_terms_not_sizes',
    'r7008': 'P10_the_vertex_numbers_are_exact_at_the_level_this_row_owns_and_the_whole_scheme_is_one_series_pole_data',
}
G1, G2, G3 = ['r7044', 'r7048'], ['r7058', 'r7056', 'r7053', 'r7050'], ['r7008']
SRC = {k: open(os.path.join(HERE, v + '.py'), encoding='utf-8').read() for k, v in N.items()}
OUT = {}

print(__doc__)
print("=" * 100)
for k in ('r7008', 'r7058', 'r7048', 'r7044', 'r7050', 'r7053'):
    p = subprocess.run([sys.executable, N[k] + '.py'], cwd=HERE, capture_output=True, text=True, timeout=400)
    OUT[k] = (p.stdout + p.stderr).replace('−', '-')
    check(f"{k} re-run from its own directory exits 0", p.returncode == 0, f"rc={p.returncode}")
OUT['r7056'] = ''


def carries(k, pat):
    return bool(re.search(pat, SRC[k] + '\n' + OUT[k]))


# ---- the passage, the way the paper has it now: REPORTED, never required
tex = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read()
flat = re.sub(r'\s+', ' ', tex)
for frag in (r'\tfrac{4}{27}(63\mu^{2}-200)\mu^{-4}', r'$\tfrac{19}{27}$', '$200/63$', '$18V=36\\pi^{2}$',
             '$175/22$', 'narrow band'):
    print(f"    P10 reads {'WITH' if frag in flat else 'WITHOUT'} `{frag}`")

print()
print("  " + "=" * 96)
print("  ② THE TWO-MODE SHIFT AND THE R^(3) EXPANSION: which receipt computes them")
print("  " + "=" * 96)
PAT = {'4/27 (63 mu^2 - 200) mu^-4': r'63\s*\*\s*mu\*\*2\s*-\s*200',
       '19/27': r'19/27', '200/63': r'200/63|Rational\(200,\s*63\)',
       'R^(3): -48, +160, -336': r'336'}
for lab, pat in PAT.items():
    g1 = [k for k in G1 if carries(k, pat)]
    check(f"{lab}: computed by r7008 and by NEITHER member of G1, the pair it closes under",
          carries('r7008', pat) and not g1, f"G1 carries: {g1 or 'none'}")
check("     ...and r7008 IS cited in the passage, on the non-resonance and a^-6 sentence ninety lines on",
      '\\rcpt{' + N['r7008'] + '}' in tex)

print()
print("  " + "=" * 96)
print("  ① QUANTITIES THE CO-CITED RECEIPTS DISAGREE ON -- the paper is checked against the LATER one")
print("  " + "=" * 96)
check("the growth: r7044 has the bound at degree EIGHT against eight, r7048 corrects it by exactly one power",
      carries('r7044', r'degree EIGHT') and carries('r7048', r'loose by|one factor of d'))
check("     ...and the paper quotes r7048's: seventh against eighth",
      'the coupling\'s own growth is of the seventh' in flat)
check("the sign: r7056 has it MIXED below a crossing at m = 13, and r7058 corrects that to POSITIVE on the whole "
      "tower against 18V = 36 pi^2", carries('r7056', r'MIXED|mixed') and carries('r7058', r'RESIDUE IS EMPTY')
      and carries('r7058', r'36 pi\^2|36\*pi\*\*2'))
check("     ...and the paper quotes r7058's threshold and sign, and neither r7056's crossing nor r7050's m = 136",
      '$18V=36\\pi^{2}$' in flat and 'positive on the whole tower' in flat
      and not re.search(r'm=13\b|m = 13|136', flat[flat.find('The shift at this level'):
                                                       flat.find('supplies the second-order datum')]))
check("the figures carried from EARLIER receipts are ones that did not move: r7058 holds r7056's six ratios as "
      "literals, 175/22 among them", 'RAT = {3:  sp.Rational(175, 22)' in SRC['r7058']
      and 'USED exactly as filed' in SRC['r7058'] and '175/22' in SRC['r7056'])
check("     ...and 120575/6, 19775/6 are r7056's; 126/125 through 81/640 are r7053's",
      '120575/6' in SRC['r7056'] and '19775/6' in SRC['r7056']
      and all(carries('r7053', p) for p in (r'126/125', r'444/1715', r'1441/7875', r'81/640')))
for n in ('131', '206', '277', '346', '414'):
    check(f"     the margin factor {n} is r7058's own", carries('r7058', rf'\b{n}\.\d'))

print()
print("  " + "=" * 96)
print("  ③ THE FOUR-RECEIPT GROUP: one chain, not four supports")
print("  " + "=" * 96)
for k in G2:
    edges = [j for j in G2 if j != k and (N[j] in SRC[k] or f"import {N[j]}" in SRC[k])]
    loads = bool(re.search(r'np\.load|json\.load|pickle\.load', SRC[k]))
    print(f"    {k}: imports/loads another member: {edges or 'none'};  reads a bank: {loads}")
check("no member imports another or reads a bank -- so the dependence is by COPIED LITERALS, which a "
      "file graph cannot show", all(not re.search(r'np\.load|json\.load|pickle\.load', SRC[k]) for k in G2))
check("⛭ r7058 contributes the threshold alone: it says the ratios are r7056's 'USED exactly as filed and not "
      "recomputed', and carries them as a literal table", 'not recomputed here' in SRC['r7058']
      and 'only the threshold' in SRC['r7058'])
g2nums = {k: [n for n in ('175', '126', '444', '1441', '81', '120575', '19775', '131', '36') if carries(k, rf'\b{n}\b')]
          for k in G2}
check("⛭ r7050 supports no number in the passage, and its own headline -- a crossing at m = 136 -- is superseded",
      not g2nums['r7050'] and carries('r7050', r'm = 136'), f"numbers carried: {g2nums['r7050'] or 'none'}")

print()
print("  ⌗ THE NOTE, NOT CLASSED -- 'the label times it holding in a narrow band'")
from fractions import Fraction
tab = s = SRC['r7058'][SRC['r7058'].index('RAT = {'):]
tab = tab[:tab.index('}') + 1]
mr = {int(m): int(m) * float(Fraction(int(a), int(b)))
      for m, a, b in re.findall(r'(\d+):\s*sp\.Rational\((\d+),\s*(\d+)\)', tab)}
check("m x ratio, from r7058's literal copy of r7056's six ratios: 11.2 to 13.5 from m = 5 upward, 23.9 at m = 3",
      len(mr) == 6 and max(mr[m] for m in mr if m >= 5) / min(mr.values()) < 1.25
      and mr[3] / min(mr.values()) > 2, ", ".join(f"{m}: {v:.1f}" for m, v in sorted(mr.items())))

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print()
print("  VERDICT: ** sec:lock quotes the superseding receipt everywhere its co-cited receipts disagree, and")
print("  every figure it carries from an earlier one is a figure that did not move. **")
print("  *One (ii) below any headline: the two-mode shift and the R^(3) expansion close under a pair that")
print("  computes none of them, where r7008 -- cited ninety lines on -- computes all of them.  And the")
print("  four-receipt group is one chain: r7056's ratios computed once, r7058's threshold new, r7050")
print("  supporting nothing quoted.*")
