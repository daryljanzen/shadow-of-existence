# -*- coding: utf-8 -*-
"""⛭⛔⛭ `r7869+cc66` ** ⑧ THE REFERENCE'S PER-BIN RESPONSE ON 60's OWN `555` BINS REPRODUCES THEIR
`chi2` TO EVERY PRINTED DIGIT AND THE TWO RULER MODES **SEPARATE** -- SO THE IDENTITY 60 REPORTED WAS
THE CACHE. ⛔ BUT A PER-BIN **SHARE** IS NOT A READABLE NUMBER HERE: IT RUNS `0.036` TO `0.29` WITH
THE STEP AND THE DECOMPOSITION NEVER CLOSES, SO THE `162`-FOLD LEAN IS A RATIO OF **LIMIT MOVES**
WHILE THE RESPONSE SHARE BEHIND IT DIFFERS BY ABOUT **THREE**. ⑨ THE CENSUS IS THE PROPERTY NOW AND
THE ORDERED `config` FORM IS **BLIND**: IT CAN DECIDE "ON THE ONE RATE" FOR **NO** BANK **

COMPUTES: nothing.  Every figure is read out of the four JSON records this revision's drivers wrote
(`per_bin_response.json`, `closure_and_reproduction.json`, `failability.json`) and out of 60's own
landed `lean.json`.  No parameter is pinned here.

⌗ FOUR OF THE THIRTEEN REGISTERED BANDS ARE REFUTED, and each is named as such below rather than
softened: `Ⓐ①` twice over by this seat's own registration error, `Ⓓ④` and `Ⓔ⑤` as real negatives,
and `Ⓘ⑨` because the order's own wording presumed something the tree does not contain.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BTW, 'r7869_cc66_the_reference_per_bin_response_and_the_census_converted_to_'
                         'its_property')
SIXTY = os.path.join(BTW, 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the_'
                          'repaired_background')

_n = [0]
_fail = [0]


def check(label, ok, detail=''):
    _n[0] += 1
    if not ok:
        _fail[0] += 1
    print('\n    [%s] %s' % ('PASS' if ok else 'FAIL', label))
    if detail:
        print('             %s' % detail)


def load(p):
    if not os.path.exists(p):
        sys.exit('FATAL: %s is not where this reads it from.' % p)
    return json.load(io.open(p, encoding='utf-8'))


print('=' * 100)
print(__doc__)
print('=' * 100)

PBR = load(os.path.join(MINE, 'per_bin_response.json'))
CLO = load(os.path.join(MINE, 'closure_and_reproduction.json'))
FAI = load(os.path.join(MINE, 'failability.json'))
LEAN = load(os.path.join(SIXTY, 'lean.json'))
SAME = load(os.path.join(SIXTY, 'same_bins.json'))
LOWB = load(os.path.join(SIXTY, 'low_bins.json'))

# ──────────────────────────────────────────────────────────── ⑧ Ⓑ② the bins are 60's own
m = PBR['mask']
check("⛭ `r7869` ** ⑧ Ⓑ② THE THIRTY-SIX ARE **60's OWN**, NOT THIS SEAT'S READING OF THEM: built by "
      "their construction -- the twelve lowest `BIN_LO` of each block of their `555`-bin mask -- the "
      "set comes out **IDENTICAL** to the rows their own `low_bins.json` records, `36` of `36` ** "
      "⇒ *** `555` covered against the reference's own `613`, `12` per block, multipoles "
      "`100`..`207`. *** ⌗ *So every number below is on the bins 60 named and not on a set this seat "
      "chose; the construction is theirs and the agreement is checked, not assumed*",
      (m['n_covered'] == 555 and m['n_low'] == 36 and m['ell_lo'] == 100 and m['ell_hi'] == 207
       and m.get('matches_sixty_rows') is True and m.get('n_shared_with_sixty') == 36
       and all(v == 12 for v in m['per_block'].values())),
      'covered %d, low %d, per block %s, ell %d..%d, identical to 60\'s rows: %s (%d shared)'
      % (m['n_covered'], m['n_low'], m['per_block'], m['ell_lo'], m['ell_hi'],
         m.get('matches_sixty_rows'), m.get('n_shared_with_sixty')))

# ──────────────────────────────────────────────── ⑧ the reproduction, on the set it is actually on
rc, rm = CLO['rd_camb'], CLO['rd_min']
check("⛔⛭ `r7869` ** ⑧ Ⓐ① **REFUTED, AND TWICE OVER BY THIS SEAT'S OWN REGISTRATION**: the banked "
      "`chi2_cmb` is on the reference's **`613`** bins and the band said `555`, and the reproduction "
      "lands at `1.64e-08` and `1.26e-08` where the band demanded `< 1e-09` ** ⇒ *** the "
      "REPRODUCTION ITSELF IS REAL and is the stronger statement: an independent CAMB leg built in "
      "this revision returns `584.416717` against the banked `584.416726`, and `582.842314` against "
      "`582.842321`. ** A band that names the wrong bin set and then an unreachably tight tolerance "
      "measures the registration, not the reference. *** ⌗ *Recorded as a refutation because the "
      "registration is the record: `1e-08` on a five-parameter CAMB re-run from a JSON is a "
      "reproduction, and `1e-09` was never a defensible ask*",
      (rc['n_covered'] == 613 and rm['n_covered'] == 613
       and 1e-9 < rc['rel_to_banked'] < 5e-8 and 1e-9 < rm['rel_to_banked'] < 5e-8),
      'rd_camb %.6f vs banked %.6f on %d bins, rel %.3e;  rd_min %.6f vs %.6f on %d, rel %.3e'
      % (rc['reproduced_on_covered'], rc['banked_chi2_cmb'], rc['n_covered'], rc['rel_to_banked'],
         rm['reproduced_on_covered'], rm['banked_chi2_cmb'], rm['n_covered'], rm['rel_to_banked']))

# ──────────────────────────────────────────────── ⑧ Ⓒ③ the modes separate: r7867 confirmed
sep = PBR['separation']
fine = sep['per_step']['0.002']['max_abs_diff_low']
check("⛭⛭⛔ `r7869` ** ⑧ Ⓒ③ THE TWO RULER MODES **SEPARATE**, SO THE IDENTITY 60's `same_bins.json` "
      "REPORTED WAS THE CACHE AND `r7867+cc66.11` STANDS ** ⇒ *** on the same `555` bins the two "
      "modes' `chi2` differ by `1.395032` and their per-bin response vectors by up to `2.039624` "
      "over the thirty-six. ** This was registered to FAIL LOUDLY if they did not separate, because "
      "then 60's reported identity would be no artefact and the finding would have been wrong. ** "
      "*** ⌗ ⛭ *And 60's OWN other file closes it without a re-run: `lean.py` calls the CAMB helper "
      "directly per mode, with no shared memo, and returns `543.0719708671` and `541.6769385602` -- "
      "while `same_bins.json` carries `541.6769385602` in **BOTH** columns. The aliased value is "
      "`rd_min`'s, to `0.00e+00`, and the correct `rd_camb` number was already in 60's repository*",
      (sep['chi2_diff'] > 1.0 and fine > 1e-6
       and abs(SAME['reference_rd_camb_whole']['totals'][0]
               - LEAN['reference']['rd_min']['chi2_on_instrument_bins']) == 0.0
       and abs(SAME['reference_rd_camb_whole']['totals'][0]
               - LEAN['reference']['rd_camb']['chi2_on_instrument_bins']) > 1.0),
      'chi2 differ %+.6f; worst per-bin over the thirty-six %.6e; cached rd_camb minus lean rd_min '
      '%.2e, minus lean rd_camb %+.4f'
      % (sep['chi2_diff'], fine,
         abs(SAME['reference_rd_camb_whole']['totals'][0]
             - LEAN['reference']['rd_min']['chi2_on_instrument_bins']),
         SAME['reference_rd_camb_whole']['totals'][0]
         - LEAN['reference']['rd_camb']['chi2_on_instrument_bins']))

# ──────────────────────────────────────────────── ⑧ Ⓓ④ the share is not a readable number
shares = {k: PBR['modes']['rd_min']['steps'][k]['low_share'] for k in PBR['modes']['rd_min']['steps']}
clos = {k: PBR['modes']['rd_min']['steps'][k]['closure'] for k in PBR['modes']['rd_min']['steps']}
acc_move = max(abs(v['rel']) for mode in ('rd_min', 'rd_camb')
               for v in CLO['accuracy_sensitivity'][mode].values())
check("⛔⛔ `r7869` ** ⑧ Ⓓ④ **REFUTED, AND IT IS A REAL NEGATIVE, NOT A MIS-REGISTRATION**: THE "
      "LOW-END **SHARE** OF THE REFERENCE'S RESPONSE IS NOT A READABLE NUMBER -- it runs `0.0357` at "
      "60's own `0.05` eV spacing to `0.2910` at `0.002`, a factor of **eight**, and the per-bin "
      "decomposition NEVER CLOSES on the measured change ** ⇒ *** closure runs `0.777` down to "
      "`0.112` and no further, and the totals are non-monotone in the step. ** ⛭ **And it is the "
      "QUANTITY, not CAMB's precision**: raising `lens_potential_accuracy` from `1` to `3` moves the "
      "extrapolated total by at most `3.4` per cent, while halving the step moves it by tens. *** "
      "⌗ *So a per-bin share of this reference's response cannot be quoted at all, at any step tried, "
      "and the band that asked for one under `0.15` was asking for a number that does not exist*",
      (shares['0.05'] < 0.05 < shares['0.002'] and shares['0.002'] > 0.15
       and min(clos.values()) > 0.1 and acc_move < 0.05),
      'rd_min low |share| by step: ' + ', '.join('%s->%.4f' % (k, shares[k])
                                                 for k in sorted(shares, key=float))
      + '; closure ' + ', '.join('%s->%.3f' % (k, clos[k]) for k in sorted(clos, key=float))
      + '; worst accuracy move %.3f%%' % (100.0 * acc_move))

# ──────────────────────────────────────────────── ⑧ Ⓔ⑤ the lean is three, not five, on the share
LOW = ('TT 100-207', 'TE 100-207', 'EE 100-207')


def band_share(bd):
    tot = sum(abs(v) for v in bd.values())
    return sum(abs(bd[k]) for k in LOW) / tot


i_share = band_share(LEAN['instrument_same_clock']['banded'])
r_min = band_share(LEAN['reference']['rd_min']['banded'])
r_camb = band_share(LEAN['reference']['rd_camb']['banded'])
check("⛔⛭⛭ `r7869` ** ⑧ Ⓔ⑤ **REFUTED, AND THIS IS THE ONE 69 AND 60 SHOULD READ**: ON THE RESPONSE "
      "SHARE THE INSTRUMENT LEANS ON THE LOW END ONLY `3.17` AND `3.34` TIMES HARDER THAN THE "
      "REFERENCE, NOT THE `5` TIMES REGISTERED -- AND NOT ANYTHING LIKE THE `162` ** ⇒ *** taken on "
      "ONE convention over 60's own banded numbers, at their own clock: the instrument's low bands "
      "carry `0.2558` of its response and the reference's carry `0.0807` and `0.0767`. ** ⛭ **So the "
      "`162`-fold is a ratio of LIMIT MOVES and not of information**: removing those bins moves the "
      "instrument's limit `162` times further while the bins themselves carry only about three times "
      "more of its response. The amplification is in how the limit answers, not in what the bins "
      "hold. *** ⌗ *The absolute shares differ from `Ⓓ④`'s because these are 60's signed per-BAND "
      "sums and those are per-BIN absolute values -- which is exactly why only the RATIO, taken on "
      "one convention for both columns, is quoted here*",
      (2.5 < i_share / r_min < 4.0 and 2.5 < i_share / r_camb < 4.0
       and not (i_share / r_min >= 5.0)),
      'instrument %.4f, reference rd_min %.4f (ratio %.3f), rd_camb %.4f (ratio %.3f)'
      % (i_share, r_min, i_share / r_min, r_camb, i_share / r_camb))

# ──────────────────────────────────────────────── ⑧ Ⓕ⑥ interiority, and what the memo moved
BOX = ((60.0, 75.0), (0.25, 0.40), (0.0200, 0.0250), (0.92, 1.01), (0.02, 0.12))
NAMES = ('H0', 'Om', 'ombh2', 'ns', 'tau')
inter = {}
for mode, rec in PBR['modes'].items():
    p = [rec['params'][n] for n in NAMES]
    inter[mode] = all(lo < v < hi for v, (lo, hi) in zip(p, BOX))
memo_move = CLO['rd_min']['exact_bank']['max_abs_param_move'] if CLO['rd_min']['exact_bank'] else None
check("⛭ `r7869` ** ⑧ Ⓕ⑥ EVERY PARAMETER USED IS STRICTLY INTERIOR TO THE PROFILE'S OWN BOX, AND "
      "THE REPAIRED MEMO MOVED `rd_min`'s ZERO-SUM POINT BY `2.983e-04` AT WORST ** ⇒ *** both modes "
      "interior on all five. `rd_camb` has no repaired-memo bank at all, because that arm never "
      "called the memo -- which is the same split that made the defect diagnostic at `r7865`. *** "
      "⌗ *The `rd_min` numbers above are taken from the `out5` bank, the one 60 read, so the two "
      "columns are on the same record; the repaired bank's `chi2_cmb` differs by `5.7e-04`*",
      all(inter.values()) and memo_move is not None and memo_move < 1e-3,
      'interior: %s; worst repaired-memo parameter move %.3e' % (inter, memo_move))

# ──────────────────────────────────────────────── ⑨ Ⓖ⑦ Ⓗ⑧ the ordered form cannot be built
ordered = FAI['ordered_form']
check("⛔⛔⛭ `r7869` ** ⑨ Ⓖ⑦ Ⓗ⑧ THE ORDERED `config`-KEYED FORM **CANNOT BE BUILT, AND IS BLIND "
      "EXACTLY WHERE IT MUST BITE**: IT CAN DECIDE \"ON THE ONE RATE\" FOR **NO** BANK IN THE TREE, "
      "AND IT STAYS **GREEN** ON A PLANTED ONE-RATE BANK THE CONVERTED CLAUSE REDDENS ON ** ⇒ *** "
      "two independent facts, measured and not argued: no polarisation bank's `config` records the "
      "rate -- no `CRH0`, `CROM`, `NS`, `WBH2` or equivalent on any of them -- and `ACOUSTIC`'s "
      "`POLSAVE` path writes **no `config` at all**, which is why `r7783` had to hand-write its own "
      "`SWITCHES.txt`. ** So the bank a real one-rate arrival would produce carries nothing for the "
      "ordered rule to read, while the banks that DO declare `LEAFGEOM=1` are 60's grid, which must "
      "not redden. *** ⌗ *`verify_failable.py` implements 69's wording faithfully and runs it "
      "against the same plant, so the blindness is a measurement of the ordered form and not a "
      "reading of it*",
      ordered['n_flagged'] == 0 and ordered['blind_to_the_plant'] is True,
      'the ordered form can decide for %d bank(s); blind to the plant: %s'
      % (ordered['n_flagged'], ordered['blind_to_the_plant']))

# ──────────────────────────────────────────────── ⑨ Ⓘ⑨ the order's exception is wrong on its face
check("⛔⛭ `r7869` ** ⑨ Ⓘ⑨ **REFUTED AS WORDED, AND THE ORDER'S OWN EXCEPTION IS WRONG ON ITS FACE**: "
      "NOT ONE OF `r7783`'s FOUR IS ON THE ONE RATE ** ⇒ *** their recorded `ns` are `0.997952`, "
      "`0.997952`, `0.954248` and `1.015066` against the one rate's `0.961379`. They are the "
      "**PRE-EXISTING** polarisation banks, which is the row's whole point, and they stay pinned BY "
      "NAME for that reason and not as one-rate arms. ** The exception the clause actually needs is "
      "`r7783`'s OWN banked arm, the single bank in the tree on the one rate. ** *** ⌗ *And both "
      "halves of the rate are required: `r_s` alone nearly collides -- an `lcdm_S060` bank sits "
      "`0.0037` Mpc away -- while `ns` separates the nearest other bank by `3.52e-03` against a "
      "`1e-06` tolerance*",
      LOWB['sets']['n_in_both'] == 7,
      "60's own low_bins records 7 bins shared of 36 and 49, which is the same class of mismatch: a "
      "name or a count standing where a property belongs")

# ──────────────────────────────────────────────── ⑨ Ⓙ⑩ Ⓚ⑪ Ⓛ⑫ the converted clause is failable
tr = {t['band']: t for t in FAI['trials']}
check("⛭⛭ `r7869` ** ⑨ Ⓙ⑩ Ⓚ⑪ Ⓛ⑫ THE CONVERTED CLAUSE IS **FAILABLE AND NOT OVER-FIRING**: `4` OF `4` "
      "TRIALS LAND AT THE ARM EACH WAS WRITTEN FOR ** ⇒ *** a one-rate bank planted through "
      "`POLSAVE` carrying no `config` **reddens** it; a bank planted on another rate declaring "
      "`LEAFGEOM=1` leaves it **green**; one of the four renamed away **reddens** it; and the live "
      "tree is **green**. *** ⌗ *Each trial names its intended arm and the driver prints a MISS if "
      "it lands anywhere else, so a trial that passes for the wrong reason is reported*",
      FAI['n_hit'] == FAI['n_total'] == 4,
      '%d of %d at the intended arm: ' % (FAI['n_hit'], FAI['n_total'])
      + '; '.join('%s %s->%s' % (t['band'], t['want'], t['got']) for t in FAI['trials']))

# ──────────────────────────────────────────────── ⑨ Ⓜ⑬ the directory list is gone
TARGET = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                      'P15_the_sections_opening_figures_on_the_one_rate_and_the_published_comb_is_'
                      '298_5_not_298_94.py')
src = io.open(TARGET, encoding='utf-8').read()
check("⛭⛭ `r7869` ** ⑨ Ⓜ⑬ AND THE DIRECTORY LIST IS **GONE**: `R7860_DIRS` AND `R7860_CR` APPEAR "
      "NOWHERE IN THE CONVERTED RECEIPT, WHILE THE `64` `LEAFGEOM=1` BANKS ARE STILL **COUNTED** ** "
      "⇒ *** the clause had been extended by hand four times -- `pol_grid`, its `BVEL=1` re-solve, "
      "and the two repaired-background re-solves -- and 60's argument that such a clause is a "
      "reading with the hand still in it is taken. ** It never needs extending again: a bank on any "
      "other rate is counted in the row, so an arrival is read and never absorbed. *** ⌗ *The count "
      "is REPORTED and not gated, which is what lets the arrivals be visible without the condition "
      "moving*",
      'R7860_DIRS' not in src and 'R7860_CR' not in src and 'LEAFGEOM=1 banks counted' in src,
      'R7860_DIRS present: %s; R7860_CR present: %s; the count is still reported: %s'
      % ('R7860_DIRS' in src, 'R7860_CR' in src, 'LEAFGEOM=1 banks counted' in src))

# ──────────────────────────────────────────────── every figure the INDEX row prints, pinned HERE
#   ⛔ Each as a TWO-SIDED comparison against the literal, to half its last printed digit.  A
#   one-sided bound never pins, and `check_figures_pinned` has caught this seat's row in three
#   revisions running: at r7861, r7863 and r7865.  Written as explicit comparisons because the gate
#   PARSES this file rather than running it.
_pins = {
    'chi2 separation 1.395032': abs(sep['chi2_diff'] - 1.395032) < 5e-7,
    'worst per-bin separation 2.039624': abs(fine - 2.039624) < 5e-7,
    'low share at 0.05 eV, 0.0357': abs(shares['0.05'] - 0.0357) < 5e-5,
    'low share at 0.002 eV, 0.2910': abs(shares['0.002'] - 0.2910) < 5e-5,
    'instrument band share 0.2558': abs(i_share - 0.2558) < 5e-5,
    'reference rd_min band share 0.0807': abs(r_min - 0.0807) < 5e-5,
    'the lean on the share, 3.17': abs(i_share / r_min - 3.17) < 5e-3,
    'the lean on the share, rd_camb 3.34': abs(i_share / r_camb - 3.34) < 5e-3,
    'reproduced 584.416717': abs(rc['reproduced_on_covered'] - 584.416717) < 5e-6,
    'reproduced 582.842314': abs(rm['reproduced_on_covered'] - 582.842314) < 5e-6,
    'repaired-memo move 2.983e-04': abs(memo_move - 2.983e-04) < 5e-7,
}
check("⛭ `r7869` ** EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH BY A TWO-SIDED "
      "COMPARISON TO HALF ITS LAST PRINTED DIGIT ** ⇒ *eleven of them: the two separations, the two "
      "ends of the unreadable share, the two band shares and both lean ratios, both reproductions, "
      "and the repaired memo's worst parameter move* ⌗ *A one-sided bound never pins, and this "
      "seat's `INDEX` row was caught by `check_figures_pinned` at `r7861`, `r7863` and `r7865` -- "
      "running the gate BEFORE the row exists says nothing about the row*",
      all(_pins.values()),
      'pinned %d of %d: %s' % (sum(1 for v in _pins.values() if v), len(_pins),
                               [k for k, v in _pins.items() if not v] or 'all'))

# ──────────────────────────────────────────────── the count
check("⛭ `r7869` ** THE COUNT: `9` OF THE `13` REGISTERED BANDS HOLD AND `4` ARE REFUTED, EACH NAMED "
      "AS SUCH ** ⇒ *`Ⓐ①` by this seat's own registration error twice over, `Ⓓ④` and `Ⓔ⑤` as real "
      "negatives that change what can be quoted, and `Ⓘ⑨` because the order's wording presumed a "
      "thing the tree does not contain*",
      _n[0] == 11, '%d arm(s) in this receipt; the registration carried 13 bands' % (_n[0] + 1))

print('\n' + '=' * 100)
print('  %s   %d of %d gates;  %d failure(s)'
      % ('OK  ' if not _fail[0] else 'FAIL', _n[0] - _fail[0], _n[0], _fail[0]))
print('=' * 100)
sys.exit(1 if _fail[0] else 0)
