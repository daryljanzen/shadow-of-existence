#!/usr/bin/env python3
r"""`r7797` ** EVERY MULTIPOLE `P15` PRINTS, `l = 2` THROUGH `8`, ON THE RATE THE UNIVERSE HAS --
AND THE CROSS-VALIDATION FIGURE GOES FROM `2.9` TO `3.0` PER CENT, WHICH IS WHAT `P7` AND `P18`
ALREADY SAY. **

      l                 2         3         4         5         6         7         8
      (L)          0.4848    0.4407    0.3536    0.6569    0.9087    0.9828    0.9992   -> 0.485 ... 0.999
      one rate     0.4898    0.4351    0.3594    0.6677    0.9120    0.9856    0.9973   -> 0.490 ... 0.997

** THE MINIMUM STAYS AT `l = 4` AND THE RECOVERY STAYS AT `l = 8` UNDER BOTH CLOCKS, ** which the
order asked to have pinned.  ** AND THE SIGN ALTERNATES: ** the quadrupole, `l = 4`, `5`, `6`, `7`
rise and the octopole FALLS, so the move is not a rescaling of the curve -- it is `r7779`'s finding
carried to all seven.

** THE `l = 3` REVERSAL IS THE LADDER'S, AND ⑦ CARRIES THAT MECHANISM IN AS A CHECK, ** as the order
asked: the discrete ladder `k_L = sqrt(L(L+2))/r_0` carries NO projection distance, so moving the
distance acts the way moving `r_0` does -- and moving `r_0` alone, at fixed transfer, reproduces the
measured sign at `5` of `5` multipoles, the `l = 3` reversal included, with the `L = 2` floor term
alone carrying that sign at `4` of `4`.

Built `r7797+cc66.2`, discharging orders ① and ③ of the chat seat's `r7797` as ONE receipt, which is
what the order asked for -- *"All of them move together, so I need the whole run in one receipt"* and
*"add the mechanism to ①'s receipt as a check"*.  Registered before it existed in
`computations/beyond_the_wall/r7797_cc66_the_low_ell_depths_all_eight/PREDICTION.md`.

===================================================================================================
** COMPUTES: ** the low-multipole depths at every `l = 2..8` -- the ratio of the boundary-quantised
   discrete sum to the continuum integral OF THE SAME TRANSFER, per multipole -- read from the banked
   arms under both clocks, and the arm-to-arm cross-validation those depths carry.  ⑦ runs the
   `r7783` ladder computation from source, which builds its own CAMB transfer at the producer's own
   accuracy settings.  No likelihood, no significance, no new instrument run.
===================================================================================================

⛭ ** WHAT MOVES IN THE PAPER, AND WHAT DOES NOT. **  `P15` prints the seven depths once
(`sec:scope`), the quartet at four sites, the `l = 4` minimum and `l ~ 8` recovery at several, and the
clause *"to `2.9` per cent at every multipole"* at ** five ** sites -- ③ counts them.  ** All five
become `3.0`.  The companion clause, *"to under one per cent above `l = 5`"*, SURVIVES UNCHANGED **
(`0.2971` -> `0.3653` per cent), which ④ measures, so that clause needs no edit.

⛭⛭ ** AND THE MOVE TAKES `P15` INTO AGREEMENT WITH ITS OWN COMPANIONS RATHER THAN AWAY FROM THEM,
WHICH ⑤ MEASURES AND WHICH IS WORTH KNOWING BEFORE THE REWRITE. **  `P7` already says the transfers
are *"cross-validated between two independent transfers to three per cent"* and `P18` *"the two
transfers agreeing to three per cent at every multipole"*.  ** Both already round to three.  So only
`P15`'s five `2.9`s move, and after they move the three papers agree. **

⛭ ** THE CROSS-VALIDATION IS NAMED BY BUILD, NOT GUESSED -- ④. **  It is arm A against arm B's
** DECOUPLED ** build at the ** distances' ** point: `2.9129` per cent under (L), the paper's `2.9`.
Arm B's ** FROZEN ** build at the same point gives `6.1934`, so the build is a measurement and not a
reading of the prose.  *Both maxima fall at `l = 4`, which is also where the dip bottoms -- the
deepest point is the hardest to cross-validate, and that is a property of the ratio and not a defect.*

⛔ ** THE DISTANCES-POINT ARM B PAIR IS BLOB-CONFOUNDED AND IS READ ON `r7779`'s R2-PRIME LICENCE. **
Its two legs came off different instrument versions; `r7779` established by normalised-AST equality
that the newer blob IS the same program with `SPLITCLOCK` unset, and that every rate object the
dynamics read is bit-identical.  ** That licence is inherited here and named rather than relied on
silently; ④'s one-rate column is the only row that needs it. **

⛔ ** AND THE PAPER PINS ARE DISJUNCTIONS WHEREVER `69`'s REWRITE IS THE SUCCESS CONDITION. **  This
receipt exists so that `69` can move those very sentences.  A pin on the current wording would go red
on the success it is for -- `check_quote_pins`'s own named failure mode -- so ①, ②, ⑤ and ⑥ test that
the sentence prints one of the two sets this receipt measures, and report WHICH.
"""
import ast as _ast
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
TEX_P7 = os.path.join(ROOT, 'corpus', 'CR_framework.tex')
TEX_P18 = os.path.join(ROOT, 'corpus', 'CR_synthesis.tex')
LADDER = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                      'r7783_cc66_the_ell_three_sign_reversal', 'ladder.py')
CHECKS = []


def check(name, ok, witness=''):
    CHECKS.append((name, bool(ok)))
    print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    if witness:
        print(f'             {witness}')


def bank(stem):
    p = os.path.join(SPEC, stem + '.npz')
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the bank has moved.')
    with np.load(p, allow_pickle=True) as z:
        return {k: z[k] for k in z.files}


AA = bank('p15_lowell_depths_armA_leafpert_leafrec1')
LP = bank('p15_lowell_depths_leafpert_leafrec1')
OC = bank('p15_lowell_depths_distances_oneclock_leafrec1')
ELLS = [int(x) for x in AA['ells']]
A_L = np.asarray(AA['distances__armA__L'], float)
A_1 = np.asarray(AA['distances__armA__one_clock_gate'], float)
BD_L = np.asarray(LP['distances__armB_decoupled__L'], float)
BD_1 = np.asarray(OC['armB_decoupled'], float)
BF_L = np.asarray(LP['distances__armB_frozen__L'], float)
RF_L = np.asarray(LP['refit__armB_frozen__L'], float)
RF_1 = np.asarray(LP['refit__armB_frozen__one_clock'], float)

tex = ' '.join(open(TEX, encoding='utf-8').read().split())
tex7 = ' '.join(open(TEX_P7, encoding='utf-8').read().split())
tex18 = ' '.join(open(TEX_P18, encoding='utf-8').read().split())

SEVEN_L = tuple(round(float(v), 3) for v in A_L)
SEVEN_1 = tuple(round(float(v), 3) for v in A_1)

print('=' * 100)
print(__doc__)
print('=' * 100)
print(f"      {'l':>4}" + ''.join(f'{e:>10}' for e in ELLS))
for lab, v in (('(L)', A_L), ('one rate', A_1), ('armB dec (L)', BD_L), ('armB dec 1R', BD_1)):
    print(f'      {lab:<14}' + ''.join(f'{float(x):>10.4f}' for x in v))
print()

# ------------------------------------------------------------------ ① the seven the paper prints
_m7 = re.search(r'the deficits are \$(\d\.\d{3})\$, \$(\d\.\d{3})\$, \$(\d\.\d{3})\$, '
                r'\$(\d\.\d{3})\$, \$(\d\.\d{3})\$, \$(\d\.\d{3})\$ and \$(\d\.\d{3})\$ of the '
                r'flat expectation at \$\\ell=2\$ through \$8\$', tex)
printed7 = tuple(float(x) for x in _m7.groups()) if _m7 else None
SETS7 = {'the arm of record, (L)': SEVEN_L, 'the one rate': SEVEN_1}
which7 = next((k for k, v in SETS7.items() if printed7 == v), None)
check("⛭⛭⛭ `r7797` ** ① THE SEVEN DEPTHS `P15` PRINTS AT `l = 2` THROUGH `8` ARE ARM A's UNDER **(L)** "
      "AT THE DISTANCES' POINT, TO THE DIGIT AT ALL SEVEN: `0.485 / 0.441 / 0.354 / 0.657 / 0.909 / "
      "0.983 / 0.999` ** ⇒ *** the `r7783` receipt pinned four of them; the order asked for the whole "
      "run, and all seven come off the same arm at the same point. *** ⌗ *Tested as the DISJUNCTION of "
      "the two sets this receipt measures, because `69`'s rewrite to the one-rate set is the success "
      "this row is for -- a pin on the current wording would redden on it*",
      printed7 is not None and which7 is not None
      and SEVEN_L == (0.485, 0.441, 0.354, 0.657, 0.909, 0.983, 0.999),
      f"the sentence prints {printed7}, which is {which7!r}; armA (L) rounds to {SEVEN_L}")

# ------------------------------------------------------------------ ② the one-rate seven
check("⛭⛭⛭ `r7797` ** ② AND ON THE RATE THE UNIVERSE HAS, AT THE SAME ARM AND POINT, THE SEVEN ARE "
      "`0.4898 / 0.4351 / 0.3594 / 0.6677 / 0.9120 / 0.9856 / 0.9973`, WHICH IS `0.490 / 0.435 / "
      "0.359 / 0.668 / 0.912 / 0.986 / 0.997` TO THREE DECIMALS ** ⇒ *** these are the seven numbers "
      "`sec:scope`'s sentence takes under `SPLITCLOCK` unset. ** The sign ALTERNATES -- the quadrupole "
      "and `l = 4,5,6,7` rise while the OCTOPOLE falls, and `l = 8` falls too -- so the move is not a "
      "rescaling of the curve. ** *** ⌗ *①'s disjunction is carried here as a condition, so a sentence "
      "printing neither set reddens this row as well*",
      which7 is not None
      and SEVEN_1 == (0.490, 0.435, 0.359, 0.668, 0.912, 0.986, 0.997)
      and [float(a) < float(b) for a, b in zip(A_L, A_1)] == [True, False, True, True, True, True, False],
      f"one rate rounds to {SEVEN_1}; per-multipole direction (one rate above (L)) "
      f"{[bool(float(a) < float(b)) for a, b in zip(A_L, A_1)]}; moves in per cent "
      f"{[round(100 * (float(b) / float(a) - 1), 3) for a, b in zip(A_L, A_1)]}")

# ------------------------------------------------------------------ ③ the minimum and the recovery
def argmin_ell(v):
    lo = [i for i, e in enumerate(ELLS) if e <= 5]
    return ELLS[min(lo, key=lambda i: float(v[i]))]


def recovery(v):
    return next((e for e, x in zip(ELLS, v) if e >= 5 and float(x) >= 0.99), None)


_min_L, _min_1 = argmin_ell(A_L), argmin_ell(A_1)
_rec_L, _rec_1 = recovery(A_L), recovery(A_1)
_sites_min = tex.count('minimum falls at $\\ell=4$') + tex.count('minimum stays at $\\ell=4$')
check("⛭⛭⛭ `r7797` ** ③ AND THE TWO THINGS THE ORDER ASKED TO HAVE PINNED DO NOT MOVE: THE MINIMUM "
      "STAYS AT `l = 4` AND THE RECOVERY STAYS AT `l = 8`, UNDER **BOTH** CLOCKS ** ⇒ *** so the "
      "SHAPE claim `P15` makes at several sites -- *\"a dip whose minimum falls at $\\ell=4$\"*, "
      "recovering by `l ~ 8` -- survives the clock unchanged, and only the DEPTHS move. *** ⌗ *The "
      "recovery is defined as the first `l >= 5` whose depth reaches `0.99`, which is the "
      "definition the `r7779` bank computed it on, not one chosen here*",
      _min_L == 4 and _min_1 == 4 and _rec_L == 8 and _rec_1 == 8 and _sites_min >= 1,
      f"minimum over l<=5: (L) l={_min_L}, one rate l={_min_1}; recovery (first l>=5 at depth>=0.99): "
      f"(L) l={_rec_L}, one rate l={_rec_1}; the paper states the l=4 minimum at {_sites_min} site(s)")

# ------------------------------------------------------------------ ④ the cross-validation, by build
def spread(a, b, lo=2):
    return max(100.0 * abs(1.0 - float(y) / float(x))
               for e, x, y in zip(ELLS, a, b) if e >= lo)


XV_L, XV_1 = spread(A_L, BD_L), spread(A_1, BD_1)
XV_FROZEN = spread(A_L, BF_L)
AB_L, AB_1 = spread(A_L, BD_L, lo=6), spread(A_1, BD_1, lo=6)
_clause = re.findall(r'\$(\d\.\d)\$ per cent at every multipole', tex)
_one_pc = len(re.findall(r'to under one per cent above \$\\ell=5\$', tex))
check("⛭⛭⛭ `r7797` ** ④ AND THE CROSS-VALIDATION FIGURE GOES `2.9129 -> 3.0328` PER CENT, SO THE "
      "PAPER'S `2.9` BECOMES `3.0` AT ALL **FIVE** SITES THAT PRINT IT -- WHILE THE COMPANION CLAUSE "
      "*\"to under one per cent above $\\ell=5$\"* **SURVIVES UNCHANGED** AT `0.2971 -> 0.3653` ** ⇒ "
      "*** named by BUILD and not by the prose: it is arm A against arm B's **DECOUPLED** build at the "
      "**distances'** point, arm B's **FROZEN** build at the same point giving `6.1934` instead. ** "
      "Both maxima fall at `l = 4`, where the dip bottoms. ** *** ⌗ *So `69` edits five numerals and "
      "leaves the above-`l=5` clause alone, which is the part of this row that saves work*",
      abs(XV_L - 2.9129) < 0.0001 and abs(XV_1 - 3.0328) < 0.0001
      and abs(XV_FROZEN - 6.1934) < 0.0001 and XV_FROZEN > 2 * XV_L
      and abs(AB_L - 0.2971) < 0.0001 and abs(AB_1 - 0.3653) < 0.0001
      and max(AB_L, AB_1) < 1.0
      and _clause == ['2.9'] * 5 and _one_pc >= 1
      and round(XV_L, 1) == 2.9 and round(XV_1, 1) == 3.0,
      f"arm A vs arm B decoupled, distances point: (L) {XV_L:.4f}% -> one rate {XV_1:.4f}%; "
      f"arm B FROZEN at the same point {XV_FROZEN:.4f}%; above l=5: {AB_L:.4f}% -> {AB_1:.4f}%; "
      f"the paper prints the clause at {len(_clause)} sites, all {set(_clause)}, and the "
      f"under-one-per-cent clause at {_one_pc}")

# ------------------------------------------------------------------ ⑤ P7 and P18 already say three
_p7_quartet = re.search(r'\$\\approx(\d\.\d{3})\$, \$(\d\.\d{3})\$, \$(\d\.\d{3})\$, \$(\d\.\d{3})\$'
                        r' of the expectation at \$\\ell=2,3,4,5\$', tex7)
# ⛔ WORD-OR-NUMERAL, NOT A LITERAL.  The FINDING is that `P7` and `P18` already round to THREE.
# A pin on the word "three" would redden the day either paper prints `$3.0$` instead -- which would
# not change the finding at all, and is `check_quote_pins`'s own named failure mode.  ⇒ Each read
# accepts the word or the numeral, and the spelling found is reported.
_THREE = r'(?:three|\$3(?:\.0)?\$)'
_m_p7_three = re.search(r'cross-validated between two independent transfers to ' + _THREE
                        + r' per cent', tex7)
_m_p18_three = re.search(r'agreeing to ' + _THREE + r' per cent at every multipole', tex18)
_m_p18_min = re.search(r'bottoming at \$\\ell=4\$|minimum (?:falls|sits|stays) at \$\\ell=4\$', tex18)
_p7_three = _m_p7_three is not None
_p18_three = _m_p18_three is not None
_p18_min = _m_p18_min is not None
_p7_set = tuple(float(x) for x in _p7_quartet.groups()) if _p7_quartet else None
_p7_which = next((k for k, v in SETS7.items() if _p7_set == v[:4]), None)
check("⛭⛭⛭ `r7797` ** ⑤ AND THE MOVE TAKES `P15` **INTO** AGREEMENT WITH ITS OWN COMPANIONS: `P7` "
      "AND `P18` ALREADY SAY *\"three per cent\"*, IN WORDS, SO ONLY `P15`'s FIVE `2.9`s MOVE AND "
      "AFTER THEY MOVE THE THREE PAPERS AGREE ** ⇒ *** the order said the depths *\"sit in `P7` and "
      "`P18`\"* and they do, differently: `P7` prints the QUARTET and the three-per-cent clause, "
      "`P18` prints the `l = 4` minimum and the clause but NO depths. ** So `P7` needs its quartet "
      "moved and `P18` needs nothing. ** *** ⌗ *`P7`'s quartet is read as the same disjunction, for "
      "the same reason*",
      _p7_quartet is not None and _p7_which is not None and _p7_three and _p18_three and _p18_min,
      f"P7 prints {_p7_set}, which is {_p7_which!r}, and spells its cross-validation "
      f"{_m_p7_three.group(0)[-18:]!r}; P18 spells its own "
      f"{_m_p18_three.group(0)[-32:]!r} and states the l=4 minimum as "
      f"{_m_p18_min.group(0)!r}; P7 carries a depth quartet {_p7_quartet is not None}")

# ------------------------------------------------------------------ ⑥ the abstract's trio
_mt = re.search(r'\$(\d\.\d{2})\$ of the \$\\Lambda\$CDM expectation there, \$(\d\.\d{3})\$ and '
                r'\$(\d\.\d{3})\$ at \$\\ell=2\$ and \$3\$', tex)
trio = tuple(float(x) for x in _mt.groups()) if _mt else None
TRIOS = {'the arm of record, (L)': (round(SEVEN_L[2], 2), SEVEN_L[0], SEVEN_L[1]),
         'the one rate': (round(SEVEN_1[2], 2), SEVEN_1[0], SEVEN_1[1])}
which_t = next((k for k, v in TRIOS.items() if trio == v), None)
check("⛭⛭ `r7797` ** ⑥ AND THE ABSTRACT'S OWN TRIO MOVES WITH THEM: `0.35` AT `l = 4` WITH `0.485` AND "
      "`0.441` AT `l = 2` AND `3` BECOMES `0.36`, `0.490` AND `0.435` ** ⇒ *the order named the "
      "abstract separately and it states the figures in a different ORDER and to a different "
      "PRECISION -- two decimals at `l = 4`, three at `l = 2,3` -- so it is parsed on its own terms "
      "rather than assumed to echo `sec:scope`*",
      trio is not None and which_t is not None
      and TRIOS['the arm of record, (L)'] == (0.35, 0.485, 0.441)
      and TRIOS['the one rate'] == (0.36, 0.490, 0.435),
      f"the abstract prints {trio}, which is {which_t!r}; the two readings are "
      f"{TRIOS['the arm of record, (L)']} and {TRIOS['the one rate']}")

# ------------------------------------------------------------------ ⑦ the mechanism, as a check
pr = subprocess.run([sys.executable, '-I', LADDER], capture_output=True, text=True, timeout=7200)
lad = {}
for ln in pr.stdout.splitlines():
    m = re.match(r'\s*(\d+)\s+(\d\.\d{4})\s+([+-]\d+\.\d{4})\s+([+-]\d+\.\d{4})\s+'
                 r'(\d\.\d{4})\s+([+-]\d+\.\d{4})\s*$', ln)
    if m:
        lad[int(m.group(1))] = (float(m.group(4)), float(m.group(6)))
_floor = {}
for ln in pr.stdout.splitlines():
    m = re.match(r'\s*(\d+)\s+([+-]\d+\.\d{5})\s+([+-]\d+\.\d{5})\s+(True|False)\s*$', ln)
    if m:
        _floor[int(m.group(1))] = m.group(4) == 'True'
meas = {e: 100.0 * (float(b) / float(a) - 1.0) for e, a, b in zip(ELLS, RF_L, RF_1)}
sign_ok = [e for e in (2, 3, 4, 5, 6)
           if e in lad and (lad[e][0] > 0) == (meas[e] < 0)]
check("⛭⛭⛭ `r7797` ** ⑦ AND THE `l = 3` REVERSAL'S MECHANISM IS CARRIED IN AS A CHECK, AS THE ORDER "
      "ASKED: THE LADDER CARRIES NO PROJECTION DISTANCE, AND MOVING `r_0` ALONE REPRODUCES THE "
      "MEASURED SIGN AT `5` OF `5` MULTIPOLES -- THE `l = 3` REVERSAL INCLUDED -- WITH THE `L = 2` "
      "FLOOR TERM ALONE CARRYING THAT SIGN AT `4` OF `4` ** ⇒ *** so the reversal is not in the "
      "dynamics and not in the clock: the depth is the `L = 2`-floored Riemann sum of the very "
      "integral it is divided by, the ladder `k_L = sqrt(L(L+2))/r_0` holds no distance, and the hard "
      "floor sets each multipole's response -- the `l = 3` reversal is commensurability between the "
      "floor and the `l = 3` kernel. *** ⛭ *This row builds a CAMB transfer at the producer's own "
      "accuracy settings, so it is the receipt's whole runtime; the cost is declared rather than "
      "hidden*",
      pr.returncode == 0 and len(sign_ok) == 5 and sum(_floor.values()) == 4
      and len(_floor) == 4,
      f"ladder rc={pr.returncode}; signs agreeing {sign_ok} ({len(sign_ok)} of 5); "
      f"measured moves {{{', '.join(f'{e}: {meas[e]:+.3f}%' for e in (2, 3, 4, 5, 6))}}}; "
      f"-dln(depth)/dln r0 {{{', '.join(f'{e}: {lad[e][0]:+.4f}' for e in sorted(lad))}}}; "
      f"floor-term sign agreement {_floor}")

# ------------------------------------------------------------------ ⑧ scope, by AST
_FORBIDDEN = {'chi2', 'chisq', 'pvalue', 'p_value', 'likelihood', 'curve_fit', 'minimize',
              'minimize_scalar', 'lstsq', 'polyfit', 'cho_solve', 'nsigma'}
_names = set()
for _n in _ast.walk(_ast.parse(open(__file__, encoding='utf-8').read())):
    if isinstance(_n, _ast.Name):
        _names.add(_n.id)
    elif isinstance(_n, _ast.Attribute):
        _names.add(_n.attr)
_hits = sorted(_names & _FORBIDDEN)
check("⛭⛭ `r7797` ** ⑧ AND THE SCOPE LIMIT IS ASSERTED RATHER THAN PROMISED: NO LIKELIHOOD, NO "
      "SIGNIFICANCE, NO NEW INSTRUMENT RUN, AND NO CLAIM THAT THE ONE-RATE DEPTHS FIT THE SKY BETTER "
      "OR WORSE ** ⇒ *the `Delta(-2 ln L) = +1.7` scoring `sec:largescale` prints is untouched by this "
      "receipt, and whether the depths should be REPRINTED is `69`'s. ⌗ Asserted by walking this "
      "file's own AST, not by searching its text for its own token list*",
      not _hits,
      f"fitting and significance names in this file's AST: {_hits or 'none'}")

# ------------------------------------------------------------------ ⑨ every figure, by comparison
_mv = [100.0 * (float(b_) / float(a_) - 1.0) for a_, b_ in zip(A_L, A_1)]
_pins = dict(
    # the seven under (L), as the INDEX row prints them to four decimals
    L2=abs(float(A_L[0]) - 0.4848) < 0.00005, L3=abs(float(A_L[1]) - 0.4407) < 0.00005,
    L4=abs(float(A_L[2]) - 0.3536) < 0.00005, L5=abs(float(A_L[3]) - 0.6569) < 0.00005,
    L6=abs(float(A_L[4]) - 0.9087) < 0.00005, L7=abs(float(A_L[5]) - 0.9828) < 0.00005,
    L8=abs(float(A_L[6]) - 0.9992) < 0.00005,
    # and on the one rate
    R2=abs(float(A_1[0]) - 0.4898) < 0.00005, R3=abs(float(A_1[1]) - 0.4351) < 0.00005,
    R4=abs(float(A_1[2]) - 0.3594) < 0.00005, R5=abs(float(A_1[3]) - 0.6677) < 0.00005,
    R6=abs(float(A_1[4]) - 0.9120) < 0.00005, R7=abs(float(A_1[5]) - 0.9856) < 0.00005,
    R8=abs(float(A_1[6]) - 0.9973) < 0.00005,
    # the three-decimal forms the paper and the row both print
    p2=abs(float(A_L[0]) - 0.485) < 0.0005, p3=abs(float(A_L[1]) - 0.441) < 0.0005,
    q2=abs(float(A_1[0]) - 0.490) < 0.0005, q3=abs(float(A_1[1]) - 0.435) < 0.0005,
    q4=abs(float(A_1[2]) - 0.359) < 0.0005, q5=abs(float(A_1[3]) - 0.668) < 0.0005,
    q6=abs(float(A_1[4]) - 0.912) < 0.0005, q7=abs(float(A_1[5]) - 0.986) < 0.0005,
    q8=abs(float(A_1[6]) - 0.997) < 0.0005,
    # the abstract's two-decimal l = 4 figure, before and after
    abs_L4=abs(float(A_L[2]) - 0.35) < 0.005, abs_R4=abs(float(A_1[2]) - 0.36) < 0.005,
    # the per-multipole moves the row prints, the octopole's reversal among them
    m2=abs(_mv[0] - 1.031) < 0.0005, m3=abs(_mv[1] - (-1.271)) < 0.0005,
    m4=abs(_mv[2] - 1.640) < 0.0005, m5=abs(_mv[3] - 1.644) < 0.0005,
    m6=abs(_mv[4] - 0.363) < 0.0005, m7=abs(_mv[5] - 0.285) < 0.0005,
    m8=abs(_mv[6] - (-0.190)) < 0.0005,
    # the ladder's own sensitivities, as ⑦'s table prints them
    lad2=abs(lad[2][0] - (-1.4940)) < 0.00005, lad3=abs(lad[3][0] - 2.1727) < 0.00005,
    lad4=abs(lad[4][0] - (-3.8724)) < 0.00005, lad5=abs(lad[5][0] - (-2.8292)) < 0.00005,
    lad6=abs(lad[6][0] - (-0.7551)) < 0.00005,
    # and the measured moves ⑦ tests those signs against
    rf2=abs(meas[2] - 1.451) < 0.0005, rf3=abs(meas[3] - (-1.524)) < 0.0005,
    rf4=abs(meas[4] - 1.351) < 0.0005, rf5=abs(meas[5] - 2.015) < 0.0005,
    rf6=abs(meas[6] - 0.744) < 0.0005,
)
check("⛭⛭ `r7797` ** ⑨ AND EVERY FIGURE THE `INDEX` ROW PUBLISHES IS PINNED HERE BY A COMPARISON, NOT "
      "ONLY THE ONES A ROW ABOVE HAPPENS TO TEST -- ALL FOURTEEN DEPTHS AT BOTH PRECISIONS, THE SEVEN "
      "PER-MULTIPOLE MOVES, THE ABSTRACT'S TWO-DECIMAL `l = 4` FIGURE BEFORE AND AFTER, AND THE "
      "LADDER'S FIVE SENSITIVITIES WITH THE FIVE MEASURED MOVES THEY ARE TESTED AGAINST ** ⇒ "
      "*`check_figures_pinned` PARSES rather than runs, so a figure a citing row prints has to appear "
      "inside a tolerance comparison in this file -- a tuple equality is not one, which is what the "
      "gate caught in this receipt's first form.  ⌗ Every value compared here is the MEASURED one, so "
      "the row moves if a bank or the ladder moves rather than if I retyped a number*",
      all(_pins.values()),
      f"{sum(_pins.values())} of {len(_pins)} pinned; NOT pinned: "
      f"{sorted(k for k, v in _pins.items() if not v) or 'none'}")

print()
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass")
if bad:
    for n in bad:
        print(f"  FAILED: {n}")
    sys.exit(1)
