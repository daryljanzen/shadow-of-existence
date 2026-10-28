"""r7633+70: writes CENSUS.md from census_rows.tsv (P15 line, receipt, LEAFREC=0 CR spectra it reads, nearby figures) and
census_receipts.txt (each P15 receipt and the banked CR spectra it loads), both built by scanning the receipts for the
stems of the 90 banked CR spectra and the paper for each receipt's \\rcpt citations."""
rows = [(l.split('\t') + ['', ''])[:4] for l in open('census_rows.tsv').read().splitlines()]
PEAK = {'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too',
        'P15_there_is_no_phase_residual_and_the_fourth_peak_is_not_the_damping_envelope',
        'P15_the_full_range_refit_holds_the_background_and_the_phase_residual_was_quantised',
        'P15_the_refit_leaves_the_background_where_the_distances_put_it_and_does_not_close_the_phase',
        'P15_three_quarters_of_the_arms_residual_is_the_controls_and_what_is_left_is_position_not_amplitude',
        'P15_the_height_target_was_below_the_resolution_of_its_own_statistic'}
A = open('census_head.md').read()
out = [A, "| P15 line | receipt | banked CR spectra it reads | figures near the citation |", "|---|---|---|---|"]
for ln, name, sp, figs in rows:
    tag = ' **(peak family: see A)**' if name in PEAK else ''
    out.append(f"| {ln} | `{name}`{tag} | {sp} | {figs.replace('|', '/')} |")
open('CENSUS.md', 'w').write('\n'.join(out) + '\n')
print(f"{len(rows)} citations, {len({r[1] for r in rows})} receipts")
