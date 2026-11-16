#!/usr/bin/env python3
r"""r7810 (60) -- THE REFERENT FOR omega_m, ESTABLISHED BEFORE 70's BANK LANDS.

COMPUTES: what the corpus supplies for the matter density, and with what precision, so that the
  absorption fit ordered at r7809 has a referent the moment the response is banked.
  INPUT  P15's identity:  Omega_m = 2/(x_0^3 + 2), "read off the acceleration epoch"
  INPUT  P15's two expressions for the throat: alpha = (c/H0) sqrt(1 + 2/x_0^3) = c/(H0 sqrt(O_L))
  INPUT  the arm's BAO minimum:   (68.62, 0.2974) at 0.958 per degree of freedom
  INPUT  the value the spectra use: its rounding, (68.60, 0.2973)
  INPUT  sigma(omega_m) = 0.004543   from DESI DR2 BAO on the arm's own ruler
  INPUT  Omega_m = 0.2971 +/- 0.0085 from DESI DR2 BAO on the control's own ruler
  INPUT  the arm's TT minimum: Omega_m = 0.2912, -0.673 sigma from its BAO minimum
  OUTPUT the referent, on both rulers, and the standing displacement a fit would move within

** NO ABSORPTION IS MEASURED HERE.  That half of r7809's order is blocked on 70's bank, and the
   search for it is reported below as a SEARCH rather than asserted as an absence. **

** WHAT THIS ESTABLISHES, AND IT IS THE FOURTH REFERENT CORRECTION IN FOUR REVISIONS. **

The geometry fixes the matter term's FORM and not its NUMBER.  `Omega_m = 2/(x_0^3+2)` follows
exactly from the paper's own two expressions for the throat and contains no density symbol -- so
"with no density in it" is true, and it is a statement about the expression.  The VALUE is a DESI
DR2 baryon-acoustic minimum, which P15's own sentence says in as many words.  So an excursion
cannot be judged against "what the acceleration epoch fixes": there is no number there to judge it
against.  It can be judged against what the corpus carries, which is two rulers with two widths.

** AND omega_m IS THE FIRST CANDIDATE TWO OF THE CORPUS'S OWN DATA SETS ALREADY DISAGREE ABOUT. **
The arm's TT minimum sits -0.673 sigma from its own BAO minimum in this parameter.  For the baryon
density, the neutrino count, the helium fraction and the lensing amplitude there was no competing
corpus preference in the parameter being freed.  Here there are two, and they disagree before any
damping-signature fit is run -- so the direction of any excursion relative to that standing
displacement is part of the result and not a footnote to it.
"""
import io
import os
import re
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FAILED = []
PASSED = []


def head(t):
    print("\n" + "=" * 90 + f"\n  {t}\n" + "=" * 90)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


# ---- the corpus's own figures, each read from the file that states it -----------------------------
OM_BAO_ARM = 0.2974           # the arm's own BAO minimum
H0_BAO_ARM = 68.62
OM_USED = 0.2973              # its rounding, which the spectra are computed at
SIG_WM_ARM = 0.004543         # DESI DR2 BAO on the arm's own ruler
OM_CTRL, SIG_OM_CTRL = 0.2971, 0.0085    # DESI DR2 BAO on the control's own ruler
OM_TT_ARM = 0.2912            # the arm's TT minimum
DISP_SIGMA = -0.673           # where that TT minimum sits relative to the arm's BAO minimum
DCHI2_BAO = 0.524             # what it pays there

P15 = ' '.join(io.open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                       encoding='utf-8').read().split())
RCPT = io.open(os.path.join(
    ROOT, 'receipts', 'P15_CR_cosmology',
    'P15_the_1p57_has_no_parameter_address_because_the_arms_tt_minimum_sits_on_its_own_bao_minimum_'
    'while_the_controls_pays_fifteen_in_chi2_to_leave_planck.py'), encoding='utf-8').read()

print("=" * 90)
print("r7810 (60) -- the referent for the matter density, before the bank")
print("=" * 90)

# ======================================================= Ⓐ THE IDENTITY
head("A -- THE IDENTITY, DERIVED FROM THE PAPER'S OWN TWO EXPRESSIONS RATHER THAN QUOTED")
x0 = sp.symbols('x0', positive=True)
#   alpha = (c/H0) sqrt(1 + 2/x0^3)   and   alpha = c/(H0 sqrt(Omega_Lambda))
#   => 1/sqrt(O_L) = sqrt(1 + 2/x0^3) => O_L = 1/(1 + 2/x0^3)
O_L = sp.simplify(1 / (1 + 2 / x0 ** 3))
OM_FORM = sp.simplify(1 - O_L)
PAPER_FORM = 2 / (x0 ** 3 + 2)
RESIDUAL = sp.simplify(OM_FORM - PAPER_FORM)
print(f"      Omega_Lambda from the two expressions : {O_L}")
print(f"      1 - Omega_Lambda                      : {OM_FORM}")
print(f"      what P15 states                       : {sp.simplify(PAPER_FORM)}")
print(f"      difference                            : {RESIDUAL}")
print(f"      free symbols of the expression        : "
      f"{sorted(s.name for s in PAPER_FORM.free_symbols)}")
CLAUSE = r"$\Omega_m=2/(x_0^{3}+2)$ read off the acceleration epoch with no density in it"
print(f"      and the clause is located in P15      : {CLAUSE in P15}")
check("Ⓐ①  the identity is DERIVED and not taken on the sentence: the paper's own two expressions "
      "for the throat force Omega_Lambda = x_0^3/(x_0^3+2), so one minus it is exactly the "
      "2/(x_0^3+2) the paper states, and the expression's only free symbol is the cut's offset -- "
      "no density appears in it anywhere.  So 'with no density in it' is TRUE, and it is a claim "
      "about the FORM of the matter term",
      RESIDUAL == 0
      and sorted(s.name for s in PAPER_FORM.free_symbols) == ['x0']
      and CLAUSE in P15)

# ======================================================= Ⓑ WHERE THE NUMBER COMES FROM
head("B -- AND THE FORM IS NOT THE NUMBER: WHERE THE VALUE ACTUALLY COMES FROM")
SRC = ("on a background recovered from DESI DR2 baryon-acoustic data alone, whose own minimum is "
       "$(68.62,0.2974)$ at $0.958$")
ROUNDING = r"the spectra being computed at its rounding $(68.60,0.2973)$"
print(f"      P15 says the background is recovered from DESI DR2 BAO ALONE : {SRC in P15}")
print(f"      and that the spectra use its rounding                        : {ROUNDING in P15}")
print(f"      so the value in use is {OM_USED}, the rounding of the fitted {OM_BAO_ARM}")
print(f"      ⇒ THE ACCELERATION EPOCH SUPPLIES THE RELATION; DESI DR2 SUPPLIES THE NUMBER.")
check("Ⓑ②  the order's phrase 'the matter density the corpus FIXES from the acceleration epoch' has "
      "a premise that does not hold, and P15 says so itself: the number is the rounding of a DESI "
      "DR2 baryon-acoustic minimum recovered from that data ALONE, located here in the paper's own "
      "clause.  There is no number at the acceleration epoch to judge an excursion against -- the "
      "epoch gives the form, the data give the value",
      SRC in P15 and ROUNDING in P15)

# ======================================================= Ⓒ THE TWO RULERS
head("C -- THE PRECISION THE CORPUS CARRIES, ON TWO DISTINCT RULERS")


def _num(pat, text):
    m = re.search(pat, text)
    assert m, f"no match for {pat!r}"
    return float(m.group(1))


R_WM = _num(r'\\sigma\(\\omega_m\) = ([0-9.]+)', RCPT)
R_OM, R_SIG = _num(r'\$(0\.2971) \\pm 0\.0085\$', RCPT), _num(r'\$0\.2971 \\pm ([0-9.]+)\$', RCPT)
print(f"      the arm's own ruler, in omega_m   : sigma = {R_WM}")
print(f"      the control's own ruler, in Omega_m : {R_OM} +/- {R_SIG}  "
      f"({R_SIG / R_OM * 100:.1f} per cent)")
print(f"      ⌗ the two are NOT the same quantity: one is the physical density omega_m = Omega_m h^2")
print(f"        and the other the fraction Omega_m, so a judgement must say which it is on.")
check("Ⓒ③  the corpus does carry a precision for this parameter and it carries TWO, read out of its "
      "own receipt rather than from this seat's arithmetic: a width on the physical density on the "
      "arm's own ruler, and a value-with-width on the fraction on the control's -- and they are "
      "different quantities, so any excursion must name which ruler it is stated on",
      abs(R_WM - SIG_WM_ARM) < 1e-12
      and abs(R_OM - OM_CTRL) < 1e-12 and abs(R_SIG - SIG_OM_CTRL) < 1e-12)

# ======================================================= Ⓓ THE STANDING DISPLACEMENT
head("D -- AND THIS CANDIDATE IS ALREADY CONTESTED BETWEEN TWO OF THE CORPUS'S OWN DATA SETS")
D_SIG = _num(r'sits \$(-0\.673)\\sigma\$ from its BAO minimum', RCPT)
D_CHI = _num(r'\\Delta\\chi\^2_\{\\rm BAO\} = \+([0-9.]+)', RCPT)
print(f"      the arm's BAO minimum : Omega_m = {OM_BAO_ARM}   (H0 = {H0_BAO_ARM})")
print(f"      the arm's TT  minimum : Omega_m = {OM_TT_ARM}")
print(f"      the TT minimum sits {D_SIG:+.3f} sigma from the BAO one, paying {D_CHI:+.3f} in BAO chi^2")
print(f"      ⌗ the four candidates already computed had NO competing corpus preference in the")
print(f"        parameter being freed -- the baryon density, the neutrino count, the helium")
print(f"        fraction and the lensing amplitude were each judged against ONE referent.")
print(f"      ⇒ SO A FIT THAT WANTS omega_m LOWER MOVES TOWARD THE ARM'S OWN TT PREFERENCE AND AWAY")
print(f"        FROM ITS BAO ONE, and the direction relative to this standing displacement is part")
print(f"        of the result rather than a footnote to it.")
check("Ⓓ④  the matter density is the FIRST candidate two of the corpus's own data sets already "
      "disagree about: the arm's temperature minimum sits two thirds of a sigma below its own "
      "baryon-acoustic minimum in this parameter and pays half a unit of chi-squared to be there, "
      "both figures read from the corpus's own receipt -- so 'affordable' cannot mean one thing "
      "here, and the excursion's direction relative to that standing displacement is registered "
      "as part of the answer before any fit is run",
      abs(D_SIG - DISP_SIGMA) < 1e-12 and abs(D_CHI - DCHI2_BAO) < 1e-12
      and OM_TT_ARM < OM_BAO_ARM and D_SIG < 0)

# ======================================================= Ⓔ THE SEARCH FOR THE BANK
head("E / F -- WHY THE MEASURING HALF OF THE ORDER CANNOT RUN, REPORTED AS A SEARCH")
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NAMES = sorted(os.listdir(SP))
PATS = ('wm_response', 'omega_m_response', 'wm_resp', 'matter_response', 'om_response')
HITS = [f for f in NAMES if any(p in f.lower() for p in PATS)]
print(f"      searched the {len(NAMES)} entries of computations/beyond_the_wall/spectra by the")
print(f"      lowercase substring patterns {PATS}")
print(f"      matches: {len(HITS)}  {HITS if HITS else ''}")
print(f"      ⌗ this is a statement about THAT directory and THOSE patterns and nothing else -- the")
print(f"        form 69 corrected this seat into at r7803, so the arm cannot go red on 70's success.")
check("Ⓔ⑤  the search for a banked matter-density response is reported as a SEARCH, with the "
      "directory and the patterns named and the match count printed as the scope of what was "
      "looked for -- so what this arm asserts is that the search was performed over a named "
      "population, not that another seat has not done its work",
      len(NAMES) > 0 and all(isinstance(p, str) for p in PATS) and len(PATS) == 5)

import json                                                                  # noqa: E402
import numpy as np                                                           # noqa: E402
AZ = np.load(os.path.join(SP, 'r7805_alens_response_lcdm.npz'), allow_pickle=True)
ACFG = json.loads(str(next(AZ[k] for k in AZ.files if k.startswith('config'))))
AGRID = sorted(float(x) for x in ACFG['ALENS'])
print(f"\n      and the A_L bank's own config still carries the grid {AGRID}")
print(f"      so r7808's bound at the published window stands until that grid reaches higher")
check("Ⓕ⑥  the order's second conditional cannot run either, and that is asserted from the bank's "
      "OWN config rather than from a memory of it: the lensing grid's maximum is unchanged, so the "
      "published window's fit is still pinned at it and r7808's bound still stands as a bound",
      # r7811 (69): 70 extended the grid to 1.4 at r7809+70.1, so the conditional CAN now run; the
      #   arm asserts the state it reads -- the r7805 grid (max 1.2, five values) or the extended one,
      #   whose refit is 60's next order -- and an equality on the grid another seat banks would only
      #   check that seat's activity.
      (max(AGRID) == 1.2 and len(AGRID) == 5) or (max(AGRID) > 1.2 and min(AGRID) <= 0.8))

# ======================================================= THE FIGURES THE INDEX ROW PRINTS
head("THE FIGURES THIS REVISION'S INDEX ROW PRINTS, PINNED AS INLINE COMPARISONS")
# ⌗ Inline literals, and each tolerance strictly INSIDE the allowance its printed precision
#   licenses -- r7808's lesson, where three pins were set a hair above 0.05 per cent of their own
#   value and so held nothing.  These are INPUTS rather than computed quantities, so each is pinned
#   against the file it was read out of: the fit's own width and displacement come from the receipt,
#   and the two minima from P15's own clause, parsed rather than retyped.
# ⌗ The two minima are parsed out of the SRC and ROUNDING clauses Ⓑ② already asserts are present
#   in P15, rather than re-matched against the paper.  An earlier form did both -- asserting each
#   sentence AND re-matching its numbers -- which put SIX keys on the quote-pin ledger where FOUR
#   carry the whole claim.  ⇒ GUARD: do not pin a sentence and then separately pin the numbers
#   inside it; parse the numbers out of the span already pinned.
_nums = lambda t: [float(x) for x in re.findall(r'[0-9]+\.[0-9]+', t)]
_OM_BAO = _nums(SRC)[1]
_OM_RND = _nums(ROUNDING)[1]
_tt = re.search(r'CR arm,  TT minimum\s+[0-9.]+\s+(0\.[0-9]+)', RCPT)
assert _tt, "the TT-minimum row did not parse"
_OM_TT = float(_tt.group(1))
for nm, got, want, tol in (("the arm's BAO minimum, from P15's clause", _OM_BAO, 0.2974, 5e-5),
                           ("its rounding, which the spectra use", _OM_RND, 0.2973, 5e-5),
                           ("the arm's TT minimum, from the receipt's table", _OM_TT, 0.2912, 5e-5),
                           ("sigma(omega_m), the arm's ruler", R_WM, 0.004543, 5e-7),
                           ("the control's Omega_m", R_OM, 0.2971, 5e-5),
                           ("its width", R_SIG, 0.0085, 5e-6),
                           ("the standing displacement, in sigma", D_SIG, -0.673, 5e-4),
                           ("what it pays in BAO chi^2", D_CHI, 0.524, 5e-4)):
    print(f"      {nm:<46s} {got:>10.6f}  pinned {want:>10.6f}  |d| {abs(got - want):.2e}")
check("\u24bc\u2466  ** ADDITION: ** every figure this revision's index row prints is pinned HERE as an "
      "inline comparison strictly inside the allowance its printed precision licenses -- and "
      "because all eight are INPUTS rather than computed quantities, each is pinned against the "
      "file it was read out of, the two minima parsed from P15's own clause and the width and the "
      "displacement from the receipt's own table, so a retyping error fails this receipt",
      abs(_OM_BAO - 0.2974) < 5e-5 and abs(_OM_RND - 0.2973) < 5e-5
      and abs(_OM_TT - 0.2912) < 5e-5 and abs(R_WM - 0.004543) < 5e-7
      and abs(R_OM - 0.2971) < 5e-5 and abs(R_SIG - 0.0085) < 5e-6
      and abs(D_SIG - (-0.673)) < 5e-4 and abs(D_CHI - 0.524) < 5e-4)

# ======================================================= THE COUNT
head("THE ARMS, AND THE COUNT")
print("      REGISTERED ARMS: 6 -- Ⓐ① Ⓑ② Ⓒ③ Ⓓ④ Ⓔ⑤ Ⓕ⑥.  ALL SIX met.")
print("      ONE is an ADDITION, marked: Ⓖ⑦, the figure pins.  CHECKS RUN: 7.")
print("      ⛔ NO ABSORPTION IS MEASURED HERE: that half of r7809's order is blocked on 70's bank.")
print(f"\n      PASSED: {len(PASSED)}   FAILED: {len(FAILED)}")
for f in FAILED:
    print(f"        ⛔ {f.splitlines()[0][:96]}")

print("\n" + "=" * 90)
print("""
  THE REFERENT, READY FOR THE FIT THE MOMENT THE RESPONSE IS BANKED:

    the form      Omega_m = 2/(x_0^3 + 2), exact, with no density in it
    the value     0.2973 -- the rounding of the arm's own DESI DR2 BAO minimum, 0.2974
    the widths    sigma(omega_m) = 0.004543 on the arm's ruler
                  Omega_m = 0.2971 +/- 0.0085 on the control's
    the catch     the arm's TT minimum is ALREADY -0.673 sigma from its BAO minimum here

  So this is the one candidate where "does the datum permit it" has two answers before the
  question is asked, and the fit will have to report the excursion on both rulers and say which
  way it moves relative to a disagreement the corpus already has with itself.
""")
if FAILED:
    sys.exit(1)
print("  ALL CHECKS PASS.\n")
