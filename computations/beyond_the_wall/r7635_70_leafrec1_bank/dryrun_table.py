"""r7635+70: tabulate the dry re-point outputs (old/new receipt stdout, from dry_repoint.sh) into DRYRUN.md and
dry/<stem>.diff.txt, with the seat that owns each receipt (receipts/INDEX.md provenance + the receipt's own seat
tags: r7029/r7033/r7055 are 70's, r7234 is 60's, the c54 receipts have no living author and fall to 70)."""
import os, re, subprocess, sys
S = sys.argv[1]          # the directory holding <k>.old / <k>.new and clean_list.txt
OWN = {'70': ('the_resolution_table_eight', 'the_three_instruments_with_no', 'the_phase_systematic_leaves'),
       '60': ('the_spacing_drift_is_made',),
       '70 (c54, ownerless)': ('where_the_likelihood_sits', 'the_height_target', 'the_control_entered_the_regime',
                               'the_photon_hierarchy_in', 'the_floor_is_a_distance', 'the_phase_is_the_driving',
                               'the_phase_moves_with_the_datum')}


def owner(r):
    return next((s for s, ps in OWN.items() if any(r.startswith('P15_' + p) for p in ps)), 'cc66')


os.makedirs('dry', exist_ok=True)
rows = []
for line in open(os.path.join(S, 'clean_list.txt')):
    st, r = line.split()
    k = r[4:60]
    if not os.path.exists(f'{S}/{k}.new') or not os.path.exists(f'{S}/{k}.old'):
        rows.append((r, owner(r), 'waits on the second half of the bank', '', '')); continue
    o, n = open(f'{S}/{k}.old').read(), open(f'{S}/{k}.new').read()
    d = subprocess.run(['diff', f'{S}/{k}.old', f'{S}/{k}.new'], capture_output=True, text=True).stdout
    open(f'dry/{r}.diff.txt', 'w').write(d)
    fl = [re.sub(r'\s+', ' ', x.split('[FAIL]')[1]).strip()[:110] for x in n.splitlines() if '[FAIL]' in x]
    rows.append((r, owner(r), f'{o.strip().splitlines()[-1][:14]} → {n.strip().splitlines()[-1][:14]}',
                 f'{o.count("[FAIL]")} → {n.count("[FAIL]")}', '; '.join(fl[:2]).replace('|', '/')))
with open('DRYRUN.md', 'w') as f:
    f.write('# Dry re-point: every §B receipt run on the arm of record, unedited (r7635+70)\n\n'
            'Made with `dry_repoint.sh`: a worktree with each `<stem>_leafrec1.npz` copied over `<stem>.npz`, the '
            'receipt run in both trees. Each receipt\'s old→new diff is `dry/<stem>.diff.txt`; its `[FAIL]` lines are '
            'the pins that move. Nothing here is a re-pointed receipt. ⚠ Receipts that also read CONTROL files whose '
            'coefficients were solved from the old arm (r6911 `SRCXS`, the r6959 tapers, r6975 mix, r6983 joint) mix '
            'an old-arm coefficient with the new arm. ⚠ An exit of 1 on BOTH sides is this shallow clone, not the arm '
            '(the receipt reads git history).\n\n'
            '| receipt | seat | exit | [FAIL] | first moved checks |\n|---|---|---|---|---|\n')
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        f.write(f'| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} | {r[4]} |\n')
print(len(rows), 'rows')
