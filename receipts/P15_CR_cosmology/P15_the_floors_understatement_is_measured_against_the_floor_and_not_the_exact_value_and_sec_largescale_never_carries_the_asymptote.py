#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:throat`, `sec:largescale`: ** THE `r7173` FLOOR SENTENCE'S FIVE PERCENTAGES
ARE MEASURED AGAINST THE FLOOR AND NOT AGAINST THE EXACT VALUE, AND THE SENTENCE DOES NOT SAY
WHICH. **  `30`, `17`, `12`, `9`, `7.5` are $(T_{\rm exact}-T_{\rm asym})/T_{\rm asym}$ -- exact at
the paper's own precision.  *Read the other way, as a fraction of the exact value the floor
understates, the same two columns of figures give ** `23.2`, `14.6`, `10.7`, `8.5`, `7.0` ** --- a
seven-point spread at the lowest degree, which is the degree the sentence singles out.*

*** THIS IS `PO-78`'s RULE IN THE REVISION THAT REPAIRED THE PREVIOUS SILENCE IN THE SAME CLAUSE:
a figure that names no quantity is read against whichever quantity the reader has in hand. ***
`r7173` added the floor wording because the arrow alone did not say which side the limit is
approached from.  *The side is now stated and the denominator is not.*

### ✔ AND THE WORRY `r7173` NAMED DOES NOT ARISE, FOR A BETTER REASON THAN ABSENCE

** `sec:largescale` never carries the asymptotic form at all ** -- zero occurrences of
`2^{7/3}`, `T(k)`, `T(0)` or `s_tot` in it.  *It computes the branch-point filter on that same
segment itself, by composing exact constant-$\omega$ transfer matrices, and reports exact/WKB
ratios rather than the exponential form.*  ⌗ *So a reader of `sec:largescale` is not handed the
asymptote to carry anywhere; and `sec:throat` already guards the index separately, flagging that
the throat tower's degree is not the observable multipole.*

⛔ ** WHAT IS WORTH KNOWING INSTEAD IS THAT `floor` NOW NAMES TWO UNRELATED QUANTITIES IN ADJACENT
CROSS-REFERENCING SECTIONS. **  `sec:throat`'s floor (new at `r7173`) is a lower bound on a
transmission amplitude; `sec:largescale`'s `low-multipole floor` -- its own section title, and in
the corpus since `r2419` -- is a bound on observable multipole built on $r_0$ and the discrete
spectrum.  *`sec:throat` cross-references `sec:largescale` by name three lines from its own floor
sentence.*

Built r7173+cc66.140 (node 66, code seat), answering the chat seat's `r7173` invitation -- *"if a
reader of `sec:largescale` would carry the asymptote into the low-multipole comparison and be a
third low at the floor degree, that is worth knowing and you are the one who would see it"* -- by
reading both sections rather than by judging the reading.

===================================================================================================
** WHAT IS READ RATHER THAN TYPED **
===================================================================================================

  ** THE TEN FIGURES AND THE SEGMENT LENGTH ARE READ OUT OF THE PAPER. **  The five percentages and
  the five exact transmissions are captured from their own sentences in `sec:throat`; `s_tot` is
  taken from the paper's closed form and also RECOMPUTED from the Gamma expression the paper prints
  beside it, so the decimal is checked and not trusted.

  ** AND THE FLOOR IS REBUILT FROM THE PAPER'S OWN EXPRESSION, NOT FROM A TYPED COEFFICIENT. **
  `2^{7/3}k^2e^{-k s_tot}` with `k^2=L(L+2)` -- the form is located in the paper first, so a drifted
  form REFUSES rather than being silently replaced by this file's memory of it.

** COMPUTES: which denominator the five percentages use, decided by comparing both candidates
   against the paper's printed values at the paper's own precision; the seven-point spread the
   unstated denominator leaves at L=2; the absence of the asymptotic form from sec:largescale; and
   the two distinct quantities the word `floor` now names. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy only; < 1 s)
"""
import math
import os
import re
import sys

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
SRC = open(TEX, encoding='utf-8').read()
FLAT = re.sub(r'\s+', ' ', SRC)

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE FIGURES, READ OUT OF `sec:throat` **")
print(BAR)

# ⛭ r7175: the sentence this locates was REPAIRED on this receipt's own finding, so the locator
#   moves with it.  The repair is the three words this receipt asked for -- the denominator, now
#   named as the asymptotic value -- and `floor` is gone from the clause, because `low-multipole
#   floor` is `sec:largescale`'s own term and this bound is a different object.  ** The locator
#   REQUIRES the denominator phrase, so it is a guard on the repair and not a record of the
#   defect: drop those words again and this refuses. **  (66, under the one exception a seat has
#   on another seat's receipt -- the edit that broke it.)
PCT = (r"understates every one of them and the lowest by most\}---exceeding it by \$([0-9.]+)\$, "
       r"\$([0-9.]+)\$, \$([0-9.]+)\$, \$([0-9.]+)\$ and \$([0-9.]+)\$ per cent \\emph\{of the "
       r"asymptotic value\} in turn")
EX = (r"the transmission is a number and not an envelope: \$([0-9.]+)\\times10\^\{-([0-9]+)\}\$, "
      r"\$([0-9.]+)\\times10\^\{-([0-9]+)\}\$, \$([0-9.]+)\\times10\^\{-([0-9]+)\}\$, "
      r"\$([0-9.]+)\\times10\^\{-([0-9]+)\}\$ and \$([0-9.]+)\\times10\^\{-([0-9]+)\}\$ "
      r"at \$L=2,4,6,8,10\$")
STOT = r"s_\{\\rm tot\}=\\Gamma\(\\tfrac16\)\\sqrt\\pi/\\Gamma\(\\tfrac23\)\\sqrt3\\,2\^\{1/3\}=([0-9.]+)\$"
FORM = r"T\(k\)\\to2\^\{7/3\}k\^2e\^\{-k\\,s_\{\\rm tot\}\}"

for name, pat, want in (('the five percentages', PCT, 1),
                        ('the five exact transmissions', EX, 1),
                        ('the asymptotic FORM', FORM, None)):
    n = len(re.findall(pat, FLAT))
    if (want is not None and n != want) or (want is None and n < 1):
        print(f"  \u26d4 REFUSED: {name} matches {n} time(s).  The wording this receipt reads has "
              f"DRIFTED, and a figure that cannot be located is not a figure that can be checked.  "
              f"Nothing is asserted.")
        sys.exit(1)

PCT_S = list(re.findall(PCT, FLAT)[0])          # the paper's strings, kept for precision
PCT_V = [float(x) for x in PCT_S]
# ** The printed string carries the precision and the float does not: the paper writes `30`
#    and `7.5`, so dp is 0 and 1.  Reading dp off `str(30.0)` gives 1 and makes the check
#    demand a tenth the paper never claimed -- which is this file asserting against its own
#    reformatting of the text rather than against the text.  Caught by this receipt failing.
PCT_DP = [len(t.split('.')[1]) if '.' in t else 0 for t in PCT_S]
_e = re.findall(EX, FLAT)[0]
EX_V = [float(_e[i]) * 10.0 ** (-int(_e[i + 1])) for i in range(0, 10, 2)]
_s = re.findall(STOT, FLAT)
if not _s:
    print("  \u26d4 REFUSED: the paper's closed form for s_tot is not located.  Nothing is asserted.")
    sys.exit(1)
S_PAPER = float(_s[0])
S_GAMMA = math.gamma(1 / 6) * math.sqrt(math.pi) / (
    math.gamma(2 / 3) * math.sqrt(3) * 2 ** (1 / 3))
L_VALS = [2, 4, 6, 8, 10]

print(f"  the five percentages        : {PCT_V}")
print(f"  the five exact transmissions: {['%.3e' % v for v in EX_V]}")
print(f"  s_tot, as the paper prints it         : {S_PAPER}")
print(f"  s_tot, recomputed from its own Gammas : {S_GAMMA:.7f}")
check("the printed s_tot is its own Gamma expression to 6 decimals -- the decimal is checked, "
      "not trusted", round(S_GAMMA, 6) == round(S_PAPER, 6))

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** THE FLOOR REBUILT FROM THE PAPER'S FORM, AND BOTH CANDIDATE DENOMINATORS **")
print(BAR)
print("  2^(7/3) k^2 exp(-k s_tot) with k^2 = L(L+2), the form located in PART 1.\n")
print(f"  {'L':>3} {'k^2':>4} {'floor':>12} {'exact':>12} {'(e-a)/a %':>10} {'(e-a)/e %':>10} "
      f"{'paper':>6}")
ROWS = []
for L, ex in zip(L_VALS, EX_V):
    k2 = L * (L + 2)
    asym = 2 ** (7 / 3) * k2 * math.exp(-math.sqrt(k2) * S_PAPER)
    r_floor = 100 * (ex - asym) / asym
    r_exact = 100 * (ex - asym) / ex
    ROWS.append((L, k2, asym, ex, r_floor, r_exact))
    print(f"  {L:>3} {k2:>4} {asym:>12.4e} {ex:>12.4e} {r_floor:>10.1f} {r_exact:>10.1f} "
          f"{PCT_V[L_VALS.index(L)]:>6}")

check("the floor is below the exact value at every one of the five degrees -- it is a floor, "
      "as the paper says", all(a < e for _L, _k, a, e, _rf, _re in ROWS))

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** WHICH DENOMINATOR: DECIDED, NOT ASSUMED **")
print(BAR)
print("  Each printed percentage is required to EQUAL one candidate rounded to its own precision.\n")
for (L, _k2, _a, _e, r_floor, r_exact), p, dp in zip(ROWS, PCT_V, PCT_DP):
    hit_floor = round(r_floor, dp) == p
    hit_exact = round(r_exact, dp) == p
    print(f"  L={L:>2}  paper says {p:>4} ({dp}dp)   floor-relative {round(r_floor, dp):>5} "
          f"{'MATCH' if hit_floor else '     '}   exact-relative {round(r_exact, dp):>5} "
          f"{'MATCH' if hit_exact else ''}")
    check(f"L={L}: the printed {p} is the FLOOR-relative figure", hit_floor)
    check(f"L={L}: the printed {p} is NOT the exact-relative figure", not hit_exact)

_spread = abs(ROWS[0][4] - ROWS[0][5])
print(f"""
  ⇒ *** ALL FIVE ARE $(T_{{\\rm exact}}-T_{{\\rm asym}})/T_{{\\rm asym}}$ AND NONE IS THE OTHER
  READING.  The sentence says "understates ... by {PCT_V[0]:.0f} per cent" and does not say per cent OF
  WHAT. ***  At L={ROWS[0][0]} -- the degree the clause singles out as understated by most -- the two readings
  are {ROWS[0][4]:.1f} and {ROWS[0][5]:.1f}, a spread of {_spread:.1f} points on one pair of numbers.""")
check(f"the unstated denominator leaves more than five points of spread at L={ROWS[0][0]}, so the "
      "reading is not academic", _spread > 5.0)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** `sec:largescale` DOES NOT CARRY THE ASYMPTOTE, AND `floor` NAMES TWO THINGS **")
print(BAR)


def section(label):
    i = SRC.find(r'\label{%s}' % label)
    if i < 0:
        return None
    j = SRC.find('\n\\section', i)
    return re.sub(r'\s+', ' ', SRC[i:j if j > 0 else len(SRC)])


LS, TH = section('sec:largescale'), section('sec:throat')
if LS is None or TH is None:
    print("  \u26d4 REFUSED: one of the two sections carries no label.  Nothing is asserted.")
    sys.exit(1)
print(f"  sec:throat {len(TH)} chars, sec:largescale {len(LS)} chars (flattened)\n")
for tok, lab in ((r'2\^\{7/3\}', '2^{7/3}'), (r'T\(k\)', 'T(k)'), (r'T\(0\)', 'T(0)'),
                 (r's_\{\\rm tot\}', 's_tot')):
    n_th, n_ls = len(re.findall(tok, TH)), len(re.findall(tok, LS))
    print(f"  {lab:>10}:  sec:throat {n_th:>2}   sec:largescale {n_ls:>2}")
    check(f"`{lab}` does not appear in sec:largescale", n_ls == 0)

n_ls_floor = len(re.findall(r'floor', LS))
n_th_floor = len(re.findall(r'floor', TH))
print(f"\n  {'floor':>10}:  sec:throat {n_th_floor:>2}   sec:largescale {n_ls_floor:>2}")
# ** A `floor` COUNT WAS ASSERTED HERE AND IS REMOVED, on `check_prose_pins`' verdict before this
#    file landed: `n_ls_floor >= 5` is a pin on a COUNT OF MATCHES, which is the class that
#    ratchet exists for.  *And it was a PROXY for what the next check establishes directly --
#    that `sec:largescale` NAMES its own distinct quantity.  A count of a word is not the naming
#    of a quantity, the name is available, so the count earned nothing and cost an adjudication.*
#    The count is still PRINTED above because it is informative; it is simply not asserted on.
# ** The wording is the paper's, checked against it: `the quantity the low-multipole floor is
#    built on is $r_0$`.  The first draft of this check typed `is built on $r_0$`, which the paper
#    does not say, and it FAILED -- this file asserting against its own paraphrase.
check("and names it as a MULTIPOLE floor built on r_0, not a transmission bound",
      'low-multipole floor is built on is $r_0$' in LS
      and r'\paragraph{The low-multipole floor.}' in LS)
# ⛭ r7175: this asserted sec:throat called the transmission bound a `floor`, one cross-reference
#   from sec:largescale's own `low-multipole floor`.  ** The collision is REPAIRED: sec:throat
#   now says `a lower bound on this sector's transmission`, and `floor on this sector` is gone. **
#   So the assertion is inverted to guard the repair -- the old phrase must be ABSENT, and the
#   new one present -- which is this receipt's own finding arriving in the paper.  (66, under the
#   exception for the edit that broke it.)
check("and sec:throat no longer calls the transmission bound a floor: `floor on this sector` is "
      "GONE and `lower bound on this sector's transmission` is in its place, so the two senses "
      "no longer collide",
      'floor on this sector' not in TH
      and "lower bound on this sector's transmission" in TH)
check("and sec:throat cross-references sec:largescale by name, so the two sit one reference apart",
      r'\S\ref{sec:largescale}' in TH or r'\ref{sec:largescale}' in TH)
check("sec:largescale computes the filter on that segment itself rather than quoting the form",
      'transfer matrices' in LS and 'exact/WKB' in LS)

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES")
print(BAR)
print(f"""
  ** THE INVITATION'S WORRY DOES NOT ARISE, AND FOR A BETTER REASON THAN ABSENCE. **  `sec:largescale`
  carries no occurrence of the asymptotic form; it composes exact transfer matrices on the same
  segment and reports exact/WKB ratios.  *A reader of that section is never handed the asymptote to
  carry, and `sec:throat` guards the index separately.*

  ⛔ ** WHAT THE SAME SENTENCE LEFT OPEN WAS ITS OWN DENOMINATOR, AND IT IS NAMED IN PRINT AT
  `r7175`. **  The five percentages are floor-relative, exactly; read as fractions of the exact value
  they would be {', '.join('%.1f' % r[5] for r in ROWS)}, and at the degree the clause singles out the two
  readings are seven points apart.  *`PO-78`'s rule, in the clause whose previous silence `r7173` had
  just repaired: the side the limit was approached from was stated and the quantity the percentage was
  of was not.*  ⇒ ** The clause now reads `exceeding it by ... per cent OF THE ASYMPTOTIC VALUE`, and
  the locator above REQUIRES those words, so this receipt is a guard on the repair rather than a
  record of the defect. **

  ⌗ ** AND `floor` HAD NAMED TWO UNRELATED BOUNDS ONE CROSS-REFERENCE APART **, the transmission one
  new at `r7173` and the multipole one in the corpus since `r2419`.  *Both were correct in their own
  section; neither said which it was when the other was in the reader's hand.*  ⇒ ** Repaired the
  same way, by giving the newer object its own words: `sec:throat` now says `a lower bound on this
  sector's transmission`, `floor on this sector` is gone, and the check above asserts both halves --
  the old phrase ABSENT and the new one PRESENT. **  *So `floor` in `P15` means the multipole floor
  again, which is `sec:largescale`'s own term and the older one.*""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  \u2713 ALL CHECKS PASSED")
print(BAR)
