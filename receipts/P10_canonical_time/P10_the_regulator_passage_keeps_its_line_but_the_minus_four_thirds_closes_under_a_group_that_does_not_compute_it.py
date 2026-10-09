"""
P10_the_regulator_passage_keeps_its_line_but_the_minus_four_thirds_closes_under_a_group_that_does_not_compute_it

r7065 -> 70: the anchors / divergence / regulator passage of `P10` `sec:lock`, three revisions deep, against its
receipts.  Pre-registered at `computations/beyond_the_wall/r7065_70_regulator_passage_audit/PREDICTION.md`,
committed before any cited receipt was run.  The method is `r7043`'s, with the window since the previous
marker.

⛭ WHAT IS FOUND
  ① NOT FIRED -- THE PROSE KEEPS THE LINE WHERE THE RECEIPT KEEPS IT (Q2, judged).
     - The receipt counts subtractions as "its summand's non-negative powers" and withholds the renormalised
       value and the invariant: "the count is three against two, and which geometric invariant carries the
       third is left open rather than guessed".
     - The prose says the same things in the same sentence, nearly word for word, and says "counted rather
       than asserted".
     - The divergence and the definition do not read as in tension.  "no finite value" leads to "must come
       from a regulator", which leads to "the construction's own regulator reaches it".  That is the ordinary
       shape of a regularisation, stated in order.
     ⌗ One word to weigh, not classed: the prose's "the interacting sum is defined" is where the receipt says
       "reaches" and "No value is claimed for the renormalised interacting sum".  The next sentence withholds
       the value, so the line holds.  "Defined" is the strongest word in it.
  ② ONE (ii), AND IT IS THE PASSAGE'S OWN RESULT.
     - -4/3, the regulator-variable summand and the count of three subtractions against two close under group
       B: r7063 two-anchors, r7058, r7056, r7053.
     - NONE of those computes -4/3 or the count.
     - The r7065 regulator receipt computes all of it.  It is cited in the passage, but in group A, on the
       anchors paragraph about a hundred and fifty lines earlier, where it supports only the 19/27 that r7008
       also carries.
     ⇒ It reads as a transposition: the regulator receipt belongs beside -4/3.
  ③ NOT FIRED.  The superseded figure r7065 corrects, r7063's logarithmic coefficient 39/4 at the old offset,
     appears nowhere in `canonical_time.tex` (searched at source).  The paper carries the current 15/4.  The
     figures used as filed are 175/22, the recoupling sums, 120575/6, 19775/6 and 39/40 from r7063.
  ⌗ And `r7059+70.1`'s one (ii) is CLOSED: group A now carries r7008 beside the two-mode shift it computes.

⛔ NOT CLAIMED.  No physics and no check of -4/3 beyond what the receipt computes.  No prose edited and no other
seat's receipt touched.  r7056's receipt (210 s) is gated on its source; the others are re-run here.
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


def report(name, cond, got=None):
    """paper state: REPORTED, never required -- a correction by 66 must not turn this receipt red"""
    print(f"    [{'as found' if cond else 'CHANGED since the audit'}]  {name}" + (f"   {got}" if got is not None else ""))


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
N = {
    'r7065': 'P10_the_construction_own_regulator_reaches_the_interacting_sum_and_spends_one_counterterm_more_than_the_free_case',
    'r7063': 'P10_the_two_anchors_are_already_one_convention_and_they_agree_but_the_candidate_prescription_does_not_close',
    'r7058': 'P10_the_cubic_normalisation_is_written_down_and_it_empties_the_residue_so_the_sign_is_positive_on_the_whole_tower',
    'r7056': 'P10_the_odd_residue_is_five_levels_and_the_sign_is_mixed_because_the_vertex_carries_covariant_not_frame_derivatives',
    'r7053': 'P10_the_cubic_vertex_is_written_down_and_K_is_not_label_independent_so_the_algebraic_channel_is_five_powers_clear',
    'r7008': 'P10_the_vertex_numbers_are_exact_at_the_level_this_row_owns_and_the_whole_scheme_is_one_series_pole_data',
}
SRC = {k: open(os.path.join(HERE, v + '.py'), encoding='utf-8').read() for k, v in N.items()}
OUT = {'r7056': ''}

print(__doc__)
print("=" * 100)
for k in ('r7065', 'r7063', 'r7058', 'r7008', 'r7053'):
    p = subprocess.run([sys.executable, N[k] + '.py'], cwd=HERE, capture_output=True, text=True, timeout=400)
    OUT[k] = (p.stdout + p.stderr).replace('\u2212', '-')
    check(f"{k} re-run from its own directory exits 0", p.returncode == 0, f"rc={p.returncode}")


def has(k, pat):
    return bool(re.search(pat, SRC[k] + '\n' + OUT[k]))


tex = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'), encoding='utf-8').read()
flat = re.sub(r'\s+', ' ', tex)


def group_before(anchor):
    """the marker group that closes the sentence containing `anchor` (empty if the sentence moved)"""
    if anchor not in flat:
        return [], -1
    i = flat.index(anchor)
    m = re.compile(r'((?:\\rcpt\{[^}]*\}[\s,;.~]*)+)').search(flat, i)
    return [re.sub(r'^P10_', '', g) for g in re.findall(r'\\rcpt\{([^}]*)\}', m.group(1))], m.start()


def key(name):
    return next((k for k, v in N.items() if v == 'P10_' + name), name[:24])


print()
print("  " + "=" * 96)
print("  THE PAPER, READ AT SOURCE -- reported, never required")
print("  " + "=" * 96)
gB, posB = group_before('it returns the exact rational $-\\tfrac43$')
gA, posA = group_before('\\emph{Both return the same sign.}')
print(f"    group A (anchors paragraph): {[key(g) for g in gA]}")
print(f"    group B (divergence + regulator paragraphs): {[key(g) for g in gB]}")

print()
print("  " + "=" * 96)
print("  ② -4/3 AND THE COUNT: which receipt computes them")
print("  " + "=" * 96)
QTY = {'-4/3': r'-4/3|Rational\(-4,\s*3\)', 'three subtractions against two': r'three against two',
       'the constant term 52/15': r'52/15'}
KB = ['r7063', 'r7058', 'r7056', 'r7053']   # group B as audited at 3f8fc14a
for lab, pat in QTY.items():
    inB = [k for k in KB if has(k, pat)]
    check(f"{lab}: computed by r7065 and by NO member of group B as audited (r7063, r7058, r7056, r7053)",
          has('r7065', pat) and not inB, f"group B carries: {inB or 'none'}")
report("     ...and r7065 IS cited in the passage, in group A on the anchors paragraph instead",
      'r7065' in [key(g) for g in gA] and 'r7065' not in KB)
report("     ...a hundred-odd lines before the result it computes",
      'it returns the exact rational' in tex and 'Both return the same sign' in tex
      and tex[:tex.index('it returns the exact rational')].count('\n') - tex[:tex.index('Both return the same sign')].count('\n') > 100)

print()
print("  " + "=" * 96)
print("  ① Q2 -- does the prose keep the line where the receipt keeps it")
print("  " + "=" * 96)
check("the receipt counts subtractions as the summand's non-negative powers and withholds the renormalised "
      "value and the invariant", "No value is claimed for the renormalised interacting sum" in SRC['r7065']
      and 's three against two, and\nwhich geometric invariant carries the third is left open rather than guessed' in SRC['r7065'])
report("     ...and the prose says the same in the same sentence as the count",
      'What is not claimed is the renormalised value, and no invariant is named for the third subtraction'
      in flat and 'the count is three against two, and which geometric invariant carries the third is left '
      'open rather than guessed' in flat and 'counted rather than asserted' in flat)
div = flat.find('the mode sum has no finite value')
report("the divergence and the definition are joined in order, not set against each other: 'no finite value' "
      "-> 'must come from a regulator' -> 'the construction's own regulator reaches it'",
      0 <= div < flat.find('must come from a regulator') < flat.find("the construction's own regulator reaches it"))
print("    ⌗ the word to weigh, REPORTED: the prose says 'the interacting sum is defined' "
      f"({'present' if 'the interacting sum is defined' in flat else 'absent'}); the receipt says 'REACHES' "
      "and claims no renormalised value")

print()
print("  " + "=" * 96)
print("  ③ SUPERSEDED FIGURES")
print("  " + "=" * 96)
check("the figure r7065 corrects -- r7063's logarithmic coefficient 39/4 at the superseded offset -- is named "
      "in r7065's receipt", "NAMES THE LOGARITHMIC COEFFICIENT 39/4" in SRC['r7065'])
report("     ...and appears nowhere in canonical_time.tex (searched at source), which carries the current 15/4",
      not re.search(r'39/4(?!\d)|\\tfrac\{39\}\{4\}|\\frac\{39\}\{4\}', tex) and '\\tfrac{15}{4}' in tex)
check("the figures used as filed are the receipts' own: 175/22 (r7058's literal of r7056), 39/40 (r7063)",
      'Rational(175, 22)' in SRC['r7058'] and '39/40' in SRC['r7063'])

print()
print("  ⌗ r7059+70.1's (ii), CLOSED: group A now carries r7008 beside the two-mode shift it computes")
report("r7008 is in group A and computes 200/63 and 19/27", 'r7008' in [key(g) for g in gA]
      and has('r7008', r'200/63') and has('r7008', r'19/27'))

print()
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print()
print("  VERDICT: ** the prose keeps the receipt's line, and the passage's own result closes under the wrong")
print("  group. **  *-4/3 and the three-against-two count are computed by r7065, which is cited a hundred-odd")
print("  lines earlier on the anchors paragraph; the four receipts closing the regulator paragraph compute")
print("  neither.  Nothing superseded is quoted, and r7059's (ii) is closed.*")
