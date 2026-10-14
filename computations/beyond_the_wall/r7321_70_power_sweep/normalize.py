#!/usr/bin/env python3
"""r7321+70: turn the four raw extractions (EXTRACTED_A-D.tsv, written by blind-to-the-outcome extraction agents and
committed unedited) into ENTRIES.tsv, every number in percentage points, by the explicit table SPEC below.

    python3 normalize.py && python3 sweep.py

Every classable row is named in SPEC; nothing is inferred by heuristic.  Rows the SPEC does not name are census (C) or
pending (P) by their extracted kind/outcome, and the script asserts that no other row slips through.

SPEC value: (kind, central, band_lo, band_hi, line, k, n, k2, n2, basis, outcome, note)
  outcome: PASS / FAIL as the scoring seat stated it, mapped from its own word (see WORDS); 'PASS*' / 'FAIL*' where the
  scoring gave a figure and no verdict word and the registered band places it (disclosed); 'NONE' where there is
  neither word nor band (no verdict was ever reached).
Interpretations fixed here, beyond PREDICTION.md (each disclosed in RESULT.md):
  (i)  a band with no central takes its midpoint as the central (the band's half-width is the tolerance registered);
  (ii) a one-sided band whose central sits on an edge takes the distance to the far edge;
  (iii) a line test whose own seat registered a central for the same quantity elsewhere in the same file takes it
       (r7303 (1) <- R-a 80; r7311 (1) <- J-d 89; WIDENS/NARROWS <- J-a 50; HOLDS/DILUTES <- J-b 100; below-55 <- J-e);
  (iv) zone readings against two lines (44.3 / 65.9) have no central: 'no delta registered'.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS_PASS = {'HELD', 'PASS', 'NOT_FIRED', 'HOLDS', 'HOLD', 'SURVIVES', "ADOPTS CC66'S THRESHOLD", 'MOVES ALL THREE UP'}
WORDS_FAIL = {'REFUTED', 'FAIL', 'FAILED', 'FAILS', 'FIRED', 'OVER_BAND', 'WRONG WAY', 'NOT CREDITED', 'NOT WIDENED',
              'NOT ATTRIBUTED', 'NOT YET'}
N = None
c69 = lambda x: 100 * x / 69
SPEC = {
    'r7285_70_live_exact_count|E-e': ('band', 70, 30, 100, N, 4, 68, N, N, 'rate', N, ''),
    'r7287_70_never_moved|N-a': ('band', 85, 60, 98, N, 458, 562, N, N, 'rate', 'PASS*', 'no verdict word; 81 inside 60-98'),
    'r7287_70_never_moved|N-b': ('band', 45, 20, 75, N, 296, 458, N, N, 'rate', 'PASS*', 'no verdict word; 65 inside 20-75'),
    'r7287_70_never_moved|N-c': ('not_proportion', N, N, N, N, N, 13, N, N, '', 'PASS*', 'Spearman, n=13 prefixes; no interval reported; +0.21 inside +0.15-+0.70'),
    'r7287_70_never_moved|N-d': ('not_proportion', N, N, N, N, N, 13, N, N, '', N, 'Spearman, no interval reported'),
    'r7287_70_never_moved|neg-1': ('not_proportion', N, N, N, N, N, 13, N, N, '', N, 'Spearman line, no interval reported'),
    'r7287_70_never_moved|neg-2': ('not_proportion', N, N, N, N, N, 13, N, N, '', N, 'difference of two Spearmans, no interval reported'),
    'r7287_cc66_L174_L203_prereg|①-mode': ('rate_vs_line', N, N, N, N, 37, 50, N, N, 'rate', N, 'registered HIGH, no number'),
    'r7287_cc66_L174_L203_prereg|①-L174': ('rate_vs_line', N, N, N, N, 37, 50, N, N, 'rate', N, 'central 56 with no band or line'),
    'r7287_cc66_L174_L203_prereg|①-L203': ('rate_vs_line', N, N, N, N, 27, 41, N, N, 'rate', N, 'central 39 with no band or line'),
    'r7287_cc66_L174_L203_prereg|①-order': ('difference', N, N, N, 10, 37, 50, 27, 41, 'diff', N, ''),
    'r7287_cc66_L174_L203_prereg|①-mech': ('rate_vs_line', N, N, N, 85, 31, 37, N, N, 'rate', N, ''),
    'r7287_cc66_L174_L203_prereg|③-a': ('rate_vs_line', N, N, N, 20, 37, 50, N, N, 'rate', N, ''),
    'r7287_cc66_L174_L203_prereg|③-b': ('rate_vs_line', N, N, N, 85, 37, 50, N, N, 'rate', N, ''),
    'r7287_cc66_L174_L203_prereg|③-c': ('difference', N, N, N, 0, 37, 50, 27, 41, 'diff', N, 'line 0: direction only'),
    'r7287_cc66_L174_L203_prereg|③-d': ('band', N, 20, 50, N, 37, 50, N, N, 'rate', N, 'refuter band; midpoint central (i)'),
    'r7287_cc66_L174_L203_prereg|③-e': ('rate_vs_line', N, N, N, 85, 31, 37, N, N, 'rate', N, ''),
    'r7289_70_move_sweep|M-c': ('band', 35, 10, 80, N, 0, 2, N, N, 'rate', 'FAIL*', 'no verdict word; 0 of 2 outside 10-80'),
    'r7289_70_move_sweep|M-d': ('band', 50, 15, 85, N, 2, 2, N, N, 'rate', 'FAIL*', 'no verdict word; 2 of 2 outside 15-85'),
    'r7289_70_move_sweep|neg-half': ('rate_vs_line', N, N, N, 50, 2, 183, N, N, 'rate', N, ''),
    'r7289_cc66_endgame_five|③-pin': ('difference', N, N, N, 25, 8, 10, 3, 10, 'diff', N, ''),
    'r7289_cc66_endgame_five|③-P14': ('rate_vs_line', N, N, N, N, 7, 12, N, N, 'rate', 'NONE', 'central only, no band; no verdict word'),
    'r7289_cc66_endgame_five|③-L150': ('rate_vs_line', N, N, N, N, 6, 11, N, N, 'rate', 'NONE', 'central only, no band; no verdict word'),
    'r7289_cc66_endgame_five|③-L803': ('rate_vs_line', N, N, N, N, 8, 11, N, N, 'rate', 'NONE', 'central only, no band; no verdict word'),
    'r7289_cc66_endgame_five|③-L210': ('rate_vs_line', N, N, N, N, 8, 10, N, N, 'rate', 'NONE', 'central only, no band; no verdict word'),
    'r7289_cc66_endgame_five|③-L258': ('rate_vs_line', N, N, N, N, 3, 10, N, N, 'rate', 'NONE', 'central only, no band; no verdict word'),
    'r7289_cc66_endgame_five|③-total': ('band', 100 * 38 / 54, 100 * 30 / 54, 100 * 46 / 54, N, 32, 54, N, N, 'rate', N, 'band 30-46 keys of 54'),
    'r7289_cc66_endgame_five|③-poles': ('difference', N, N, N, 5, 8, 11, 6, 11, 'diff', N, ''),
    'r7289_cc66_endgame_five|④-⒜': ('difference', N, N, N, 25, 8, 10, 3, 10, 'diff', N, 'duplicate of (3)-pin, listed'),
    'r7289_cc66_endgame_five|④-⒝': ('difference', N, N, N, 20, 8, 11, 6, 11, 'diff', N, ''),
    'r7289_cc66_endgame_five|④-⒞': ('not_proportion', N, N, N, N, N, 5, N, N, '', N, 'Spearman n=5, no interval reported'),
    'r7289_cc66_endgame_five|④-⒟': ('difference', N, N, N, 25, 1, 1, 0, 4, 'diff', N, ''),
    'r7290_60_the_tier_mix|ⓑ-overall': ('rate_vs_line', N, N, N, 50, 5, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓑ-subject': ('rate_vs_line', N, N, N, 15, 0, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓑ-MH': ('rate_vs_line', N, N, N, 30, 1, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓒ-overall': ('band', 55, 50, 80, N, 5, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓒ-subject': ('band', 7, 0, 15, N, 0, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓒ-MH': ('band', 15, 0, 30, N, 1, 29, N, N, 'rate', N, ''),
    'r7290_60_the_tier_mix|ⓒ-DEL': ('band', 25, 10, 45, N, 12, 29, N, N, 'rate', N, ''),
    'r7293_70_agreement|n* (L19-L30)': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'a required n, not an interval'),
    'r7293_70_agreement|neg-tau2 (L40-41)': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'tau2, no interval reported'),
    'r7293_cc66_pin_discipline|⓵ PIN share (L32)': ('band', 45, 33, 57, N, 12, 24, N, N, 'rate', N, ''),
    'r7293_cc66_pin_discipline|⓵ not share (L33)': ('band', 70, 58, 82, N, 10, 19, N, N, 'rate', N, ''),
    'r7293_cc66_pin_discipline|⓵ gap (L34)': ('band', 25, 5, 45, N, 10, 19, 12, 24, 'diff', N, 'lower edge 5 registered; symmetric upper edge assumed (ii)'),
    'r7293_cc66_pin_discipline|⓵ total (L35)': ('rate_vs_line', N, N, N, N, 22, 43, N, N, 'rate', 'NONE', 'central 56, no band; no verdict'),
    'r7293_cc66_pin_discipline|⒜ (L46)': ('difference', N, N, N, 5, 10, 19, 12, 24, 'diff', N, ''),
    'r7293_cc66_pin_discipline|⒝ (L47)': ('difference', N, N, N, 0, 10, 19, 12, 24, 'diff', N, 'line 0: direction only'),
    'r7293_cc66_pin_discipline|⒞ (L48)': ('difference', N, N, N, 0, 3, 3, 10, 19, 'diff', N, 'line 0: direction only'),
    'r7293_cc66_pin_discipline|⒟ (L49)': ('band', 70, 58, 82, N, 10, 19, N, N, 'rate', N, '12-point tolerance per group; physics group shown'),
    'r7296_60_the_four_unread|ⓐ P14 RO (L20)': ('band', N, 30, 70, N, 4, 12, N, N, 'rate', N, '60\'s scoring; 66 ruled the registration void (FOR_60.md:507-537)'),
    'r7296_60_the_four_unread|ⓐ P14 MH (L20)': ('band', N, 0, 35, N, 5, 12, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L150 RO (L21)': ('band', N, 30, 70, N, 5, 11, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L150 MH (L21)': ('band', N, 0, 40, N, 6, 11, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L803 RO (L22)': ('band', N, 0, 30, N, 5, 11, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L803 MH (L22)': ('band', N, 0, 25, N, 0, 11, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L210 RO (L23)': ('band', N, 10, 55, N, 6, 10, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓐ L210 MH (L23)': ('band', N, 0, 35, N, 0, 10, N, N, 'rate', N, 'as above'),
    'r7296_60_the_four_unread|ⓑ L803 neg (L37-40)': ('rate_vs_line', N, N, N, 30, 5, 11, N, N, 'rate', N, ''),
    'r7299_70_two_scores|①': ('rate_vs_line', N, N, N, N, 37, 41, N, N, 'rate', N, 'zone reading (iv)'),
    'r7299_70_two_scores|①-agree': ('difference', N, N, N, N, 20, 41, 30, 41, 'diff', N, 'direction only, no threshold registered'),
    'r7299_70_two_scores|⑤': ('band', 55, 40, 70, N, 37, 41, N, N, 'rate', N, ''),
    'r7299_70_two_scores|②-notation-dec': ('band', 0, 0, 25, N, 1, 4, N, N, 'rate', N, 'counts of 4; one-sided (ii)'),
    'r7299_70_two_scores|②-short-dec': ('band', 100, 100 * 5 / 6, 100, N, 7, 7, N, N, 'rate', N, 'counts of 6; one-sided (ii)'),
    'r7299_70_two_scores|②-MH-dec': ('band', 80, 60, 100, N, 4, 4, N, N, 'rate', N, 'counts of 5'),
    'r7299_70_two_scores|N-C1': ('rate_vs_line', N, N, N, N, 37, 41, N, N, 'rate', N, 'zone reading (iv)'),
    'r7299_70_two_scores|N-D1': ('rate_vs_line', N, N, N, 100 * 6 / 11, 11, 11, N, N, 'rate', N, ''),
    'r7300_60_the_blind_read|①': ('band', 100 * 3 / 7, 100 * 2 / 7, 100 * 4 / 7, N, 1, 7, N, N, 'rate', N, 'counts of 7'),
    'r7300_60_the_blind_read|①-hi': ('rate_vs_line', N, N, N, 100 * 5 / 7, 1, 7, N, N, 'rate', N, ''),
    'r7300_60_the_blind_read|①-lo': ('rate_vs_line', N, N, N, 100 / 7, 1, 7, N, N, 'rate', N, ''),
    'r7300_60_the_blind_read|rule-1': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'a length cut-off, no interval'),
    'r7300_60_the_blind_read|rule-2': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'a length cut-off, no interval'),
    'r7300_60_the_blind_read|rule-3': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'a length cut-off, no interval'),
    'r7300_60_the_blind_read|rule-4': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'a length cut-off, no interval'),
    'r7303_70_redraft_score|①': ('rate_vs_line', 80, N, N, 73.8, 56, 64, N, N, 'rate', N, 'central from R-a (iii)'),
    'r7303_70_redraft_score|①-undec-gap': ('difference', N, N, N, 10, 3, 69, 4, 69, 'diff', N, ''),
    'r7303_70_redraft_score|②-70': ('rate_vs_line', N, N, N, N, 47, 66, N, N, 'rate', N, 'zone reading (iv)'),
    'r7303_70_redraft_score|②-71': ('rate_vs_line', N, N, N, N, 48, 65, N, N, 'rate', N, 'zone reading (iv)'),
    'r7303_70_redraft_score|②-pooled': ('rate_vs_line', N, N, N, N, 95, 131, N, N, 'rate', N, 'zone reading (iv); 131 applications, not keys'),
    'r7303_70_redraft_score|②-check': ('band', N, 30, 60, N, 13, 69, N, N, 'rate', N, ''),
    'r7303_70_redraft_score|N-2': ('rate_vs_line', N, N, N, 20, 4, 69, N, N, 'rate', N, ''),
    'r7303_70_redraft_score|R-a': ('band', 80, 70, 90, N, 56, 64, N, N, 'rate', N, ''),
    'r7303_70_redraft_score|R-b': ('rate_vs_line', 80, N, N, 73.8, 56, 64, N, N, 'rate', N, 'the same test as (1) (iii)'),
    'r7303_70_redraft_score|R-c': ('band', 60, 45, 75, N, 95, 131, N, N, 'rate', N, ''),
    'r7303_70_redraft_score|R-d': ('rate_vs_line', N, N, N, N, 95, 131, N, N, 'rate', N, 'zone reading (iv)'),
    'r7307_71_redraft_blind|neg-1': ('rate_vs_line', N, N, N, 20, 4, 69, N, N, 'rate', N, ''),
    'r7307_71_redraft_blind|neg-2': ('rate_vs_line', N, N, N, 50, 30, 69, N, N, 'rate', N, ''),
    'r7307_71_redraft_blind|neg-3': ('rate_vs_line', N, N, N, 10, 26, 65, N, N, 'rate', N, ''),
    'r7307_71_redraft_blind|P-1': ('band', c69(6), c69(2), c69(14), N, 4, 69, N, N, 'rate', N, 'counts of 69'),
    'r7307_71_redraft_blind|P-2': ('band', 100 * 15 / 65, 100 * 6 / 65, 100 * 30 / 65, N, 26, 65, N, N, 'rate', N, 'counts of 65'),
    'r7307_71_redraft_blind|P-3': ('band', 50, 35, 65, N, 48, 65, N, N, 'rate', N, ''),
    'r7311_70_redraft2_score|① IS IT A RULE': ('rate_vs_line', 89, N, N, 73.8, 59, 65, N, N, 'rate', N, 'central from J-d (iii)'),
    'r7311_70_redraft2_score|① UNDECIDED gap': ('difference', N, N, N, 10, 1, 69, 4, 69, 'diff', N, ''),
    'r7311_70_redraft2_score|② calibration': ('rate_vs_line', N, N, N, N, 103, 133, N, N, 'rate', N, 'zone reading (iv)'),
    'r7311_70_redraft2_score|② credit condition': ('band', N, 30, 60, N, 6, 69, N, N, 'rate', N, ''),
    'r7311_70_redraft2_score|WIDENS': ('rate_vs_line', 50, N, N, 34.4, 24, 65, N, N, 'rate', N, 'central from J-a (iii)'),
    'r7311_70_redraft2_score|NARROWS': ('rate_vs_line', 50, N, N, 34.4, 24, 65, N, N, 'rate', N, 'central from J-a (iii)'),
    'r7311_70_redraft2_score|HOLDS': ('rate_vs_line', 100, N, N, 73.8, 24, 24, N, N, 'rate', N, 'central from J-b (iii)'),
    'r7311_70_redraft2_score|DILUTES': ('rate_vs_line', 100, N, N, 73.8, 24, 24, N, N, 'rate', N, 'central from J-b (iii)'),
    'r7311_70_redraft2_score|N-J': ('difference', N, N, N, 20, 13, 65, 26, 64, 'diff', N, '70\'s scoring; 71 scores the same rule NOT FIRED'),
    'r7311_70_redraft2_score|N-J overlap': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'overlap against independence, no interval'),
    'r7311_70_redraft2_score|J-a': ('band', 50, 35, 65, N, 24, 65, N, N, 'rate', N, ''),
    'r7311_70_redraft2_score|J-b': ('band', 100, 93, 100, N, 24, 24, N, N, 'rate', N, 'one-sided (ii)'),
    'r7311_70_redraft2_score|J-c': ('not_proportion', N, N, N, N, N, N, N, N, '', N, 'categorical verdict'),
    'r7311_70_redraft2_score|J-d': ('band', 89, 80, 96, N, 59, 65, N, N, 'rate', N, ''),
    'r7311_70_redraft2_score|J-e': ('band', 65, 50, 80, N, 103, 133, N, N, 'rate', N, '133 applications, not keys'),
    'r7311_70_redraft2_score|below-55 check': ('rate_vs_line', 65, N, N, 55, 103, 133, N, N, 'rate', N, 'central from J-e (iii)'),
    'r7311_70_redraft2_score|L-a (70)': ('band', 15, 0, 35, N, 22, 26, 25, 42, 'diff', N, ''),
    'r7311_70_redraft2_score|L-a (71)': ('band', 15, 0, 35, N, 40, 52, 5, 13, 'diff', N, ''),
    'r7311_70_redraft2_score|L-b': ('band', 0, 0, 100 / 3, N, 0, 6, N, N, 'rate', N, 'count of 6 ledger-owed keys; one-sided (ii)'),
    'r7313_71_redraft2_blind|Neg UNDECIDED>20%': ('rate_vs_line', N, N, N, 20, 4, 69, N, N, 'rate', N, ''),
    'r7313_71_redraft2_blind|Neg UNDECIDED+flagged>50%': ('rate_vs_line', N, N, N, 50, 17, 69, N, N, 'rate', N, ''),
    'r7313_71_redraft2_blind|Neg both<=10%': ('rate_vs_line', N, N, N, 10, 13, 65, N, N, 'rate', N, ''),
    'r7313_71_redraft2_blind|N-J (71 restated)': ('difference', N, N, N, 20, 13, 65, 26, 65, 'diff', N, '71\'s own denominator'),
    'r7313_71_redraft2_blind|Q-1': ('band', c69(2), 0, c69(7), N, 4, 69, N, N, 'rate', N, 'counts of 69'),
    'r7313_71_redraft2_blind|Q-2': ('band', 100 * 16 / 65, 100 * 6 / 65, 100 * 30 / 65, N, 13, 65, N, N, 'rate', N, 'counts of 65'),
    'r7313_71_redraft2_blind|Q-3': ('band', 68, 52, 82, N, 50, 65, N, N, 'rate', N, ''),
    'r7315_70_widens_reregistered|X verdict 70 (TEXT/NOT ATTRIBUTED/AGAINST)': ('difference', 5, N, N, 0, 23, 40, 40, 69, 'diff', N, 'central from W-c'),
    'r7315_70_widens_reregistered|W-c': ('band', 5, -10, 20, N, 23, 40, 40, 69, 'diff', N, ''),
    'r7320_60_the_early_era_sampled|⑤ band': ('band', 27.5, 20, 40, N, 27, 40, N, N, 'rate', N, 'counts of 40'),
    'r7320_60_the_early_era_sampled|⑤ refute-low': ('rate_vs_line', 27.5, N, N, 12.5, 27, 40, N, N, 'rate', N, ''),
    'r7320_60_the_early_era_sampled|⑤ refute-high': ('rate_vs_line', 27.5, N, N, 62.5, 27, 40, N, N, 'rate', N, ''),
}

for _pfx, _ro, _mh, _n, _kro, _kmh in (('L256', (30, 70), (0, 40), 7, 2, 2), ('L801', (35, 75), (0, 45), 7, 3, 3),
                                        ('L276', (25, 65), (0, 35), 7, 3, 1), ('L277', (20, 60), (0, 30), 5, 2, 1),
                                        ('L809', (30, 70), (0, 45), 5, 1, 3), ('L551', (25, 75), (0, 50), 4, 2, 1),
                                        ('L230', (0, 67), (0, 34), 3, 0, 1)):
    SPEC[f'r7300_60_the_blind_read|ⓑ-{_pfx}-RO'] = ('band', N, _ro[0], _ro[1], N, _kro, _n, N, N, 'rate', N,
                                                    'counts read back from S34 by the extraction agent; midpoint (i)')
    SPEC[f'r7300_60_the_blind_read|ⓑ-{_pfx}-MH'] = ('band', N, _mh[0], _mh[1], N, _kmh, _n, N, N, 'rate', N,
                                                    'counts read back from S34 by the extraction agent; midpoint (i)')
OWN = [('computations/beyond_the_wall/r7321_70_power_sweep/PREDICTION.md', e, q) for e, q in
       (('PS-a', 'entries in scope'), ('PS-b', 'U-PASS share'), ('PS-c', 'R share'),
        ('PS-d', 'class changes under clustering'), ('PS-e', 'entries with no delta'))]
COLS = ['file', 'entry_id', 'quantity', 'kind', 'central', 'band_lo', 'band_hi', 'line', 'scored_k', 'scored_n', 'arm2_k',
        'arm2_n', 'observed', 'outcome', 'outcome_word', 'outcome_source', 'keys', 'receipts', 'effect_basis', 'h_override',
        'notes']


def fmt(x):
    return '' if x is None else (f'{x:.4f}'.rstrip('0').rstrip('.') if isinstance(x, float) else str(x))


def main():
    raw = []
    for x in 'ABCD':
        raw += list(csv.DictReader(open(os.path.join(HERE, f'EXTRACTED_{x}.tsv'), encoding='utf-8'), delimiter='\t'))
    out, seen = [], set()
    for r in raw:
        key = r['file'].split('/')[-2] + '|' + r['entry_id']
        word = r['outcome'].strip().upper()
        base = {c: r.get(c, '') for c in COLS}
        base['outcome_word'] = r['outcome']
        if key in SPEC:
            seen.add(key)
            kind, c, lo, hi, line, k, n, k2, n2, basis, outc, note = SPEC[key]
            if outc is None:
                assert word in WORDS_PASS | WORDS_FAIL, (key, word)
                outc = 'PASS' if word in WORDS_PASS else 'FAIL'
            base.update(kind=kind, central=fmt(c), band_lo=fmt(lo), band_hi=fmt(hi), line=fmt(line), scored_k=fmt(k),
                        scored_n=fmt(n), arm2_k=fmt(k2), arm2_n=fmt(n2), effect_basis=basis, outcome=outc,
                        notes=(note + ' | ' if note else '') + r['notes'])
        elif word in ('PENDING', 'NOT SPENT'):
            base.update(outcome='PENDING')
        elif r['kind'] == 'census':
            base.update(outcome='PASS' if word in WORDS_PASS else 'FAIL' if word in WORDS_FAIL else 'NONE')
        else:
            raise SystemExit(f'unclassified row: {key} {r["kind"]} {word}')
        out.append(base)
    assert seen == set(SPEC), set(SPEC) - seen
    for f, e, q in OWN:
        out.append({**{c: '' for c in COLS}, 'file': f, 'entry_id': e, 'quantity': q, 'kind': 'band',
                    'outcome': 'PENDING', 'notes': 'this sweep\'s own registration, in scope by its own rule'})
    with open(os.path.join(HERE, 'ENTRIES.tsv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter='\t')
        w.writeheader()
        w.writerows(out)
    print(f'{len(out)} entries ({len(raw)} extracted + {len(OWN)} own); {len(SPEC)} classable by SPEC')


if __name__ == '__main__':
    main()
