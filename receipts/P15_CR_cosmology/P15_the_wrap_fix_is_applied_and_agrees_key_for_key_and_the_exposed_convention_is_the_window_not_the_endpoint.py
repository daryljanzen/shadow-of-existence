r"""
RECEIPT -- P15: ** `r7225` ORDERED TWO THINGS: `apply the collapse in S7/S8 and ship the corrected
numbers`, and `measure how much the r_D endpoint convention moves the 16 per cent floor`.
*** BOTH DONE, AND BOTH CARRY A CORRECTION TO SOMETHING THAT WAS ASSUMED. *** **

  ⓵ ** ITEM ①, THE RE-MEASURE: SIX ROWS, SIX EXACT AGREEMENTS -- AFTER `70`'s BANK CAUGHT A BUG IN
  MY OWN PREFILTER. **  *`ABSENT` `218`->`98`, `REVERSAL` `442`->`475`, `DISCRIMINATING` `279`->`324`
  on the paper half; source `ABSENT` `469`->`454`, `CODE` `218`->`202`, `REVERSAL+PARTIAL`
  `270`->`288`.  **Every one is `70`'s number to the digit, and the headline strengthens to `25.7`
  per cent against `18.4`, `z = 2.84`.***  ⌈ ⛔ *It did NOT agree at first: two `'3 nu'` keys split
  the other way, and the cause was mine -- my byte prefilter took the literal's longest token as its
  anchor and FELL BACK TO THE RAW LITERAL when no token reached four characters, silently
  reintroducing the blindness for every short-token key.  **A total that agreed would have hidden it;
  the key-by-key diff against `70`'s bank is what found it**, which is the whole value of a second
  implementation and is why `r7225` asked for one.*

  ⓶ ** AND THE FIX HAS A FALSE POSITIVE, WHICH BOTH IMPLEMENTATIONS SHARE AND NEITHER NAMED. **
  *Widening a literal's spaces to `\s+` lets `'3 nu'` match `2K_3\n      null` across a line break
  between two unrelated tokens in `L831/G1`.  That spurious site is what carries those two keys into
  `REVERSAL-PARTIAL`.*  ⇒ **So the corrected numbers are right as the shared rule defines them, and
  the rule admits cross-token matches for short multi-token literals.  Stated as a limit rather than
  repaired here, because repairing it would move `70`'s banked split too.**

  ⓷ ⛭⛭⛭ ** AND ONE PIN WAS DOING TWO JOBS, WHICH MOVING IT EXPOSED. **  *`S8` pinned the INSTRUMENT
  and the POPULATION with the same sha.  Re-pinning it to the corrected `S7` silently took the key
  count from `1,489 + 1,154` to `1,566 + 1,196` -- its own gates caught it -- so `same sample,
  corrected instrument`, which is exactly what this revision is, was not expressible.  **Two pins
  now: `PIN` for the baseline, the tree and the bodies, `BLOCK_PIN` for the instrument alone.**

  ⓸ ** ITEM ②, THE FLOOR: `$0.085$` PERCENTAGE POINTS, SO `a sixth` IS SAFE. **  *The arm's own
  `$r_D$` moves `$+1.59$` per cent between the visibility-peak and recombination conventions, and
  the floor goes `$16.01$` to `$15.92$` per cent -- nowhere near a seventh or a fifth.*  ⌗ *The
  prediction's BAND held and its central value was `$1.9\times$` high, because it converted `cc66`'s
  `$3.10$`-point two-arm SIGNATURE swing into a `$3.10$` per cent change in the arm's own LENGTH:
  refuting outcome ④ as written, an input error and not an arithmetic one.*

  ⓹ ⛔⛭⛭ ** BUT THE DIFFERENCE IS NOT CONVENTION-SAFE, AND `r7225` SAID IT WAS. **  *`the convention
  is common to both and cancels, which your own two-ratio identity guarantees` -- the identity
  guarantees the phase depends on `$r_D/D_M$`, and it does NOT guarantee the two arms' `$r_D$` move
  together.  **They move in OPPOSITE directions: `$+1.59$` per cent on the arm and `$-1.51$` on the
  control.**  So the arms' `$r_D/D_M$` separation goes `$0.27$` to `$2.79$` per cent and the kernel's
  phase difference goes `$-0.0141^{\circ}$` to `$+0.1448^{\circ}$` -- **a factor of ten AND a change
  of sign.***  ⌈ *`r7236`'s clearance SURVIVES it -- `$2.82$` orders below the residual on the worse
  convention against `$3.84$` on the shipped one -- but `r7236`'s reported SIGN was never a
  convention-independent quantity, so the sign I published as a failed prediction could not have been
  got right without naming the endpoint.*  ⇒ *And `$1.59+1.51=3.10$` reproduces `cc66`'s straddle-zero
  figure on a DIFFERENT configuration, which is the one piece of this that is a confirmation.*

  ⇒ ⛭ ** AND THE PRE-REGISTERED THIRD OUTCOME FIRES BY A FACTOR OF A HUNDRED AND EIGHTY: THE EXPOSED
  CONVENTION IS THE WINDOW, NOT THE ENDPOINT. **  *`running` is defined over `$104\le\ell\le1886$`,
  which is the paper's fitting window and not a property of the kernel.  Move it and the floor goes
  `$9.11$` per cent (`$200$`-`$1886$`) to `$24.13$` (`$50$`-`$1886$`) -- **a fifteen-point range
  against the endpoint's `$0.085$`.***  ⇒ **So the sentence in print wants the `$\ell$`-WINDOW named
  beside the floor and not the endpoint, and the published `$16$` per cent is right precisely because
  the window it is taken over is the residual's own.**

** COMPUTES: the corrected S7/S8 bucket counts under wrap-tolerant location, checked key for key
   against 70's banked split; and the kernel phase floor of r7236 re-evaluated at both r_D endpoint
   conventions and over six l-windows, with the two arms' endpoint swings taken from cc66's own
   standalone integration run at the one-clock grid's parameters and banked beside this receipt.
   *** S7 and S8 are re-run by this receipt as subprocesses rather than reimplemented. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; 39s MEASURED)
"""
import glob
import json
import os
import re
import subprocess
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []
ran = []


def gate(label, ok):
    ran.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BW, 'r7238_60_the_wrap_fix_applied_and_the_rD_convention_priced')
SEVENTY = os.path.join(BW, 'r7223_70_detector_blindnesses')
S7 = glob.glob(os.path.join(ROOT, 'receipts', 'L_probability', 'S7_*.py'))[0]
S8 = glob.glob(os.path.join(ROOT, 'receipts', 'L_probability', 'S8_*.py'))[0]
for _p in (MINE, SEVENTY, S7, S8):
    if not os.path.exists(_p):
        print(f"  ⛔ AN INPUT THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

RESIDUAL = -96.6
NS = 0.96
DEG = 180.0 / np.pi
ARM = dict(rs=145.32808432693113, DM=13941.629043038241, rD=7.12)
CTL = dict(rs=144.52814273163971, DM=13864.662802960762, rD=7.10)


def kernel_phase(rs, DM, rD, lo=104.0, hi=1886.0, nu=20000, reach=80.0):
    """r7236's window, read as a complex integral: the RUNNING phase in the paper's sign convention"""
    o = []
    for l in (lo, hi):
        tmax = np.arccosh(max(1.0 + 1e-12, reach * DM / (l * rD)))
        t = np.linspace(0.0, tmax, nu)
        x = l * np.cosh(t)
        k = x / DM
        W = k ** (NS - 2) * np.exp(-2.0 * (k * rD) ** 2) / x
        o.append(float(np.angle(np.trapezoid(W * np.exp(2j * (x - l) * rs / DM), t))))
    return -(o[1] - o[0]) * DEG


def run_receipt(path, env=None):
    e = dict(os.environ)
    e.update(env or {})
    r = subprocess.run([sys.executable, path], cwd=ROOT, capture_output=True, text=True, env=e)
    return r.returncode, r.stdout


# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓐ  ITEM ① -- S7 AND S8 RE-RUN, AND THEIR CORRECTED COUNTS READ OFF THEIR OWN OUTPUT")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_rc7, _o7 = run_receipt(S7)
_dump = os.path.join('/tmp', 'r7238_s8_split.tsv')
_rc8, _o8 = run_receipt(S8, {'S8DUMP': _dump})
gate("Ⓐ① both receipts run to exit 0 on this tree, so the counts below are a passing measurement "
     f"and not a reading of a red run (S7 rc={_rc7}, S8 rc={_rc8})", _rc7 == 0 and _rc8 == 0)


def tally(out, names):
    t = {}
    for n in names:
        m = re.search(rf'^\s+{re.escape(n)}\s+(\d+)\s*$', out, re.M)
        t[n] = int(m.group(1)) if m else None
    return t


T7 = tally(_o7, ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'UNFLIPPABLE', 'MARKUP',
                 'ABSENT', 'SATURATED'))
T8 = tally(_o8, ('REVERSAL', 'REVERSAL-PARTIAL', 'CODE', 'UNFLIPPABLE', 'MARKUP', 'ABSENT',
                 'SATURATED'))
print(f"    S7: {T7}")
print(f"    S8: {T8}")
SEV = {'S7_ABSENT': 98, 'S7_REVERSAL': 475, 'S7_DISCRIMINATING': 324,
       'S8_ABSENT': 454, 'S8_CODE': 202, 'S8_REVPART': 288}
_got = {'S7_ABSENT': T7['ABSENT'], 'S7_REVERSAL': T7['REVERSAL'],
        'S7_DISCRIMINATING': T7['DISCRIMINATING'], 'S8_ABSENT': T8['ABSENT'],
        'S8_CODE': T8['CODE'], 'S8_REVPART': T8['REVERSAL'] + T8['REVERSAL-PARTIAL']}
for k in SEV:
    print(f"    {k:20s} 70 = {SEV[k]:4d}   mine = {_got[k]:4d}   {'AGREE' if SEV[k] == _got[k] else 'DIFFER'}")
gate("Ⓐ② EVERY ONE of 70's six rows is reproduced to the digit by an independent implementation",
     all(SEV[k] == _got[k] for k in SEV))
gate("Ⓐ③ and the fall in S7's ABSENT is the 120 the order singles out, more than half of 218",
     _got['S7_ABSENT'] == 98 and 218 - _got['S7_ABSENT'] == 120)
_hl = re.search(r'([\d.]+)% of its readable keys would go red against the paper half\'s ([\d.]+)%', _o8)
print(f"    headline: source {_hl.group(1)}% against paper {_hl.group(2)}%")
gate("Ⓐ④ the headline SURVIVES AND STRENGTHENS on the corrected population: 25.7 against 18.4",
     bool(_hl) and _hl.group(2) == '25.7' and _hl.group(1) == '18.4')
_z = re.search(r'two-proportion z = ([\d.]+),\s+p = ([\d.]+)', _o8)
gate("Ⓐ⑤ and the separation sharpens rather than softening: z = 2.84 where it was 2.77",
     bool(_z) and _z.group(1) == '2.84')

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓑ  THE KEY-BY-KEY DIFF AGAINST 70's BANK, WHICH IS WHAT FOUND THE BUG IN MY OWN PREFILTER")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_theirs = {}
for ln in open(os.path.join(SEVENTY, 'wrap_tolerant_source_270.tsv'), encoding='utf-8').read().split('\n')[1:]:
    if ln.strip() and not ln.startswith('#'):
        f = ln.split('\t')
        _theirs[(f[0], f[1])] = f[-1]
_mine = {}
for ln in open(_dump, encoding='utf-8').read().split('\n')[1:]:
    if ln.strip():
        rec, lit, cls = ln.split('\t')
        _mine[(rec, json.loads(lit))] = cls
_disputed = [k for k, v in _theirs.items() if _mine.get(k) == 'DISCRIMINATING']
_revboth = sum(1 for k, v in _theirs.items() if v == 'REVERSAL' and _mine.get(k) == 'REVERSAL')
print(f"    70's split: {len(_theirs)} keys.  mine dumped: {len(_mine)} (REVERSAL + DISCRIMINATING)")
print(f"    REVERSAL agreed on {_revboth} keys; keys 70 calls REVERSAL/PARTIAL and I call "
      f"DISCRIMINATING: {len(_disputed)}")
gate("Ⓑ① the two splits now agree key for key -- no key is REVERSAL for one and DISCRIMINATING for "
     "the other", len(_disputed) == 0)
gate("Ⓑ② and REVERSAL agrees on all 160 of 70's, so the agreement is of the SETS and not of the "
     "totals", _revboth == 160 and sum(1 for v in _theirs.values() if v == 'REVERSAL') == 160)
_s7src = open(S7, encoding='utf-8').read()
gate("Ⓑ③ the prefilter's length floor is GONE and the reason is in the source, because a fallback to "
     "the raw literal reintroduces exactly the blindness this revision removes",
     'NO LENGTH FLOOR' in _s7src and 'return toks[0] if toks else' in _s7src)
gate("Ⓑ④ and the haystack is NOT collapsed -- the design choice that keeps CLAUSE_DELIM's blank-line "
     "clause break alive", 'THE HAYSTACK IS NOT COLLAPSED' in _s7src and 'def flat(' in _s7src)

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓒ  AND THE FALSE POSITIVE THE SHARED RULE ADMITS, EXHIBITED RATHER THAN DESCRIBED")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_g1 = glob.glob(os.path.join(ROOT, 'receipts', 'L831_graph_theory', 'G1_*.py'))
_txt = open(_g1[0], encoding='utf-8').read() if _g1 else ''
_m = re.search(r'3\s+nu', _txt)
print(f"    the literal '3 nu' matched in L831/G1 as: {(_txt[_m.start():_m.end()] if _m else None)!r}")
gate("Ⓒ① a wrap-tolerant match of `3 nu` lands across a line break between `2K_3` and `null`, two "
     "unrelated tokens -- so the rule admits cross-token matches for short multi-token literals",
     bool(_m) and '\n' in _txt[_m.start():_m.end()] and 'K_3' in _txt[max(0, _m.start() - 4):_m.start() + 1])
gate("Ⓒ② and it is stated as a LIMIT rather than repaired here, because repairing it would move 70's "
     "banked split as well as this one",
     'false positive' in __doc__.lower() and 'Stated as a limit' in __doc__)

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓓ  ONE PIN WAS DOING TWO JOBS, AND MOVING IT MOVED THE POPULATION")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_s8src = open(S8, encoding='utf-8').read()
gate("Ⓓ① S8 now carries TWO pins -- the population's and the instrument's -- and says why",
     bool(re.search(r"^PIN = '[0-9a-f]{40}'", _s8src, re.M))
     and bool(re.search(r"^BLOCK_PIN = '[0-9a-f]{40}'", _s8src, re.M))
     and 'TWO PINS' in _s8src)
# ⛭⛭⛭ r7240 (60): ** THE TOTAL IS MONOTONE NOW AND THE READ SITE IS STILL EXACT. **  r7240 swept
#   this seat's work for an exact count asserted against a set another seat can grow and this gate
#   was the one genuine EXPOSED site it found: `_s8src` is S8's LIVE source, and r7227 is the cycle
#   that proved another seat edits this seat's receipts when the gate requires it -- three of them.
#   The claim is that the instrument slice is read on ONE line, so that half stays `== 1`; the total
#   occurrence count was never the claim.
gate("Ⓓ② and only the instrument slice reads BLOCK_PIN, so the sample cannot move with the "
     "instrument again", _s8src.count('_at(BLOCK_PIN,') == 1 and _s8src.count('BLOCK_PIN') >= 2)
_half = re.search(r'the two halves are (\d+) and (\d+) keys of the pinned baseline', _o8)
print(f"    the pinned population is still {_half.group(1)} + {_half.group(2)} keys")
gate("Ⓓ③ and the population is the one r7230 measured, 1489 + 1154, so the corrected numbers are "
     "`same sample, corrected instrument`",
     bool(_half) and _half.group(1) == '1489' and _half.group(2) == '1154')

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓔ  ITEM ② -- THE FLOOR AT BOTH r_D ENDPOINT CONVENTIONS")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
RD = json.load(open(os.path.join(MINE, 'rd_two_conventions.json'), encoding='utf-8'))
_fa = 1.0 + RD['arm']['swing_percent'] / 100.0
_fc = 1.0 + RD['control']['swing_percent'] / 100.0
print(f"    the arm's own r_D moves {RD['arm']['swing_percent']:+.2f}% between conventions, the "
      f"control's {RD['control']['swing_percent']:+.2f}% -- OPPOSITE directions")
gate("Ⓔ① and their difference reproduces cc66's straddle-zero figure, 3.10 points, on a DIFFERENT "
     "configuration from the one it measured",
     abs(abs(RD['arm']['swing_percent']) + abs(RD['control']['swing_percent'])
         - RD['two_arm_swing_points']) < 0.02 and RD['arm']['swing_percent'] * RD['control']['swing_percent'] < 0)
_pa0 = kernel_phase(ARM['rs'], ARM['DM'], ARM['rD'])
_pa1 = kernel_phase(ARM['rs'], ARM['DM'], ARM['rD'] * _fa)
_f0, _f1 = 100 * abs(_pa0 / RESIDUAL), 100 * abs(_pa1 / RESIDUAL)
print(f"    floor at the visibility peak {_f0:.2f}%   at recombination {_f1:.2f}%   "
      f"RANGE {abs(_f0 - _f1):.3f} percentage points")
gate("Ⓔ② the floor reproduces r7236's published 16.0 per cent at the shipped convention, so nothing "
     "downstream of it is being quietly restated", bool(15.9 < _f0 < 16.1))
gate("Ⓔ③ and the endpoint convention moves it by under a fifth of a percentage point",
     bool(abs(_f0 - _f1) < 0.2))
gate("Ⓔ④ so `a sixth` is SAFE: the floor stays between a seventh and a fifth by a wide margin on "
     "both conventions", bool(all(14.3 < f < 20.0 for f in (_f0, _f1))))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓕ  ⛔ BUT THE DIFFERENCE IS NOT CONVENTION-SAFE, AND THE ORDER SAID IT WAS")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
_pc0 = kernel_phase(CTL['rs'], CTL['DM'], CTL['rD'])
_pc1 = kernel_phase(CTL['rs'], CTL['DM'], CTL['rD'] * _fc)
_d0, _d1 = _pa0 - _pc0, _pa1 - _pc1
_sep0 = abs(ARM['rD'] / ARM['DM'] - CTL['rD'] / CTL['DM']) / (ARM['rD'] / ARM['DM'])
_sep1 = abs(ARM['rD'] * _fa / ARM['DM'] - CTL['rD'] * _fc / CTL['DM']) / (ARM['rD'] * _fa / ARM['DM'])
print(f"    visibility peak : arms separated by {100*_sep0:.2f}% in r_D/D_M  ->  {_d0:+.4f} deg  "
      f"({np.log10(abs(RESIDUAL / _d0)):.2f} orders below)")
print(f"    recombination   : arms separated by {100*_sep1:.2f}% in r_D/D_M  ->  {_d1:+.4f} deg  "
      f"({np.log10(abs(RESIDUAL / _d1)):.2f} orders below)")
gate("Ⓕ① the arms' separation in r_D/D_M is an ORDER larger on the other convention, so the "
     "convention does not cancel from the difference", bool(_sep1 > 5 * _sep0))
gate("Ⓕ② the phase difference grows by about a factor of ten AND changes sign",
     bool(abs(_d1) > 5 * abs(_d0) and _d0 * _d1 < 0))
gate("Ⓕ③ ⛔ so r7236's reported SIGN was never a convention-independent quantity -- the sign this "
     "seat published as a failed prediction could not have been got right without naming the endpoint",
     bool(_d0 < 0 < _d1))
gate("Ⓕ④ and r7236's CLEARANCE survives it: more than two orders of magnitude below the residual on "
     "the worse convention", bool(abs(RESIDUAL / _d1) > 1e2))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓖ  THE PRE-REGISTERED THIRD OUTCOME: THE EXPOSED CONVENTION IS THE WINDOW, NOT THE ENDPOINT")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
WINS = ((104.0, 1886.0), (150.0, 1600.0), (104.0, 1500.0), (200.0, 1886.0), (104.0, 2200.0), (50.0, 1886.0))
_fl = {}
for lo, hi in WINS:
    p = kernel_phase(ARM['rs'], ARM['DM'], ARM['rD'], lo=lo, hi=hi)
    _fl[(lo, hi)] = 100 * abs(p / RESIDUAL)
    print(f"    l in [{lo:6.0f}, {hi:6.0f}]:  floor {_fl[(lo, hi)]:6.2f}%")
_spread = max(_fl.values()) - min(_fl.values())
print(f"    ⇒ the WINDOW moves the floor by {_spread:.2f} points against the ENDPOINT's "
      f"{abs(_f0 - _f1):.3f} -- a factor of {_spread / abs(_f0 - _f1):.0f}")
gate("Ⓖ① the l-window moves the floor by WHOLE POINTS", bool(_spread > 5.0))
gate("Ⓖ② and by more than a hundred times what the endpoint convention moves it, so the exposed "
     "choice is the window", bool(_spread / abs(_f0 - _f1) > 100))
_pt = ' '.join(open(os.path.join(MINE, 'PREDICTION.md'), encoding='utf-8').read().split())
gate("Ⓖ③ which is the THIRD OUTCOME written down before either item was run, in those words",
     'the WINDOW and not the endpoint' in _pt and 'third outcome' in _pt.lower())
print(f"    the prediction: 0.16 percentage points, band 0.05 to 0.5.  measured: {abs(_f0-_f1):.3f}")
gate("Ⓖ④ the prediction's BAND holds", bool(0.05 <= abs(_f0 - _f1) <= 0.5))
gate("Ⓖ⑤ ⛔ and its CENTRAL VALUE is high by about a factor of two -- refuting outcome ④ as written, "
     "an input error: cc66's 3.10 points is a TWO-ARM signature swing and the arm's own length moves "
     "1.59 per cent",
     bool(1.5 < 0.16 / abs(_f0 - _f1) < 2.5 and 'the swing is not' in _pt.lower()))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("Ⓗ  WHAT THIS DOES NOT SETTLE")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print("    ⌗ the endpoint swings are taken from cc66's standalone integration run at the one-clock")
print("      grid's parameters, and applied as a RATIO to the instrument's own reported r_D, because")
print("      the two machineries differ in absolute r_D -- a gap cc66's own receipt documents.")
print("    ⌗ the false positive is exhibited on one literal and not counted across the backlog.")
print("    ⌗ nothing here adjudicates a baseline key: the corrected buckets are a measurement and")
print("      the verdicts remain the baseline owner's.")
gate("Ⓗ① the ratio-not-absolute choice is declared, and the receipt reads the swings from a banked "
     "file carrying its own script rather than from numbers typed here",
     os.path.exists(os.path.join(MINE, 'rd_two_conventions.py')) and '_applied_as' in RD)
gate("Ⓗ② and the floor is quoted WITH its window throughout, which is the recommendation this "
     "receipt makes", bool(_fl[(104.0, 1886.0)] and abs(_fl[(104.0, 1886.0)] - _f0) < 1e-9))

# ═════════════════════════════════════════════════════════════════════════════════════════════════
head("SUMMARY")
# ═════════════════════════════════════════════════════════════════════════════════════════════════
print(f"    gates run: {len(ran)}    failed: {len(fail)}")
for f in fail:
    print(f"      FAILED: {f}")
print()
print("    ⇒ ITEM ①: six rows, six exact agreements with 70, after their bank caught my prefilter's")
print(f"      length floor.  The headline strengthens to {_hl.group(2)}% against {_hl.group(1)}%.")
print(f"    ⇒ ITEM ②: the endpoint moves the floor {abs(_f0-_f1):.3f} points, so `a sixth` is safe --")
print(f"      and the WINDOW moves it {_spread:.1f}, so the window is what the sentence needs.")
print(f"    ⇒ AND the arm-control DIFFERENCE is not convention-safe: {_d0:+.4f} to {_d1:+.4f} deg.")

if fail:
    raise SystemExit(1)
