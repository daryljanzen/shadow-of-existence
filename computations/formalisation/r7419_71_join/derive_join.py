#!/usr/bin/env python3
"""r7419+71 — the selector for ROWS.tsv's `receipt` and `decl` columns.

Indexes every declaration in computations/formalisation/lean (theorem, lemma, def, abbrev, structure,
instance, inductive), with its namespace, by file. For each row, candidate names come from
  (1) the row's own `what it needs next` cell,
  (2) JOIN_SCOPE.tsv's identifiers_named (66's measurement at r7419),
  (3) SWEEP_MAP below: the r7315 sweep's row -> step B<k> table, whose new declarations per step are
      read off consecutive PROBE_RUN_B<k>.txt files (the 11 rows JOIN_SCOPE marks ABSENT are all here).
A candidate enters `decl` ONLY if it is declared in the index; a name declared in several files is
written with the file the row's own cell names if it names one, else every file that declares it is
reported for a decision (printed, not guessed).
Writes JOIN.tsv (index, receipt, decl, sources, unresolved) beside this file. Run from the repo root.
"""
import csv, re, sys, pathlib, collections

ROOT = pathlib.Path('.')
F = ROOT / 'computations/formalisation'
LEAN = F / 'lean'
HERE = F / 'r7419_71_join'

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?'
                  r'(theorem|lemma|def|abbrev|structure|instance|inductive|class)\s+([^\s:({\[]+)')
NS = re.compile(r'^\s*namespace\s+(\S+)')
END = re.compile(r'^\s*end\s+(\S+)')
SEC = re.compile(r'^\s*section\b(?:\s+(\S+))?')


def index():
    idx = collections.defaultdict(set)          # short name -> {(file, fullname)}
    files = [p for p in LEAN.rglob('*.lean') if '.lake' not in p.parts]
    for p in files:
        stack = []
        for line in p.read_text(encoding='utf-8').splitlines():
            m = NS.match(line)
            if m:
                stack.append(('ns', m.group(1))); continue
            m = SEC.match(line)
            if m and not line.strip().startswith('section_'):
                stack.append(('sec', m.group(1) or '')); continue
            m = END.match(line)
            if m:
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i][1] == m.group(1):
                        del stack[i:]; break
                continue
            if line.strip() == 'end' and stack:
                stack.pop(); continue
            m = DECL.match(line)
            if m:
                name = m.group(2)
                ns = '.'.join(s[1] for s in stack if s[0] == 'ns')
                full = f'{ns}.{name}' if ns and not name.startswith('_root_') else name
                rel = str(p.relative_to(LEAN))
                idx[name.split('.')[-1]].add((rel, full))
    return idx


# r7315_71_sweep/RESULT.md's `# | row` table; the declarations are those new at each step's PROBE_RUN.
SWEEP_STEPS = {99: 1, 109: 2, 11: 3, 34: 4, 36: 5, 103: 6, 32: 7, 38: 8, 56: 9, 44: 10, 78: 11, 55: 12,
               8: 13, 76: 14, 22: 15, 4: 16, 5: 17}


# Rows no automatic source reaches, each read by hand from the file cited.
MANUAL = {
    60: (['invariant_basis', 'second_order_identity', 'B_unique', 'scal_second_order', 'control_frame_constant', 'part_B', 'seven_level_values', 'weights_nonzero', 'level_sums_sign', 'part_C', 'cross_factorises', 'faulhaber', 'sign_algebra'],
         'r7443_71_campaign45/PROBE_RUN_A.txt; Row60Levels.lean #print axioms list (r7443+71.36: one-word names the cell selector skips)'),
    96: (['eps4_sign', 'eps4_det', 'sum_eps', 'pontryaginLC_eq', 'riemLC_tab', 'csLC_tab', 'tabs_bridge', 'pontryagin_parity', 'cs_parity', 'csArr_three', 'warped_pontryagin', 'warped_cs', 'sph_pontryagin_zero', 'sph_cs_zero', 'polarised_pontryagin_zero', 'nariai_general_pontryagin_zero', 'nariai_rotated_pontryagin_zero', 'nariai_pontryagin_zero', 'nariai_apply', 'GW_apply', 'gowdy_pontryagin', 'gowdy_cs', 'gowdy_plane_wave_pontryagin', 'gowdy_areal_pontryagin', 'gowdy_areal_silenced', 'areal_profile_exists', 'GM_apply', 'member_cs', 'member_pontryagin', 'unpolarised_nonzero', 'member_divergence', 'member_stokes', 'member_volume', 'net_count'],
         'r7443_71_campaign42/PROBE_RUN_A.txt; Row96ChernSimons.lean #print axioms list (r7443+71.33: one-word names the cell selector skips)'),
    70: (['conj_zero', 'gen_solves', 'fake_vev', 'fake_zero', 'deviation', 'cubic_nonres', 'cubic_channel', 'dE2_closed', 'dE2_receipt_sizes', 'conj_q3', 'conj_q3qpq', 'fake_receipt', 'locus', 'no_cancellation', 'pure_cubic_even', 'g3_derivs', 'trace_cube', 'trace_cube_cases', 'bookkeeping', 'frw_tab_k', 'fRk_maxsym', 'closed_dS', 'ms_q', 'frame_values', 'frame_weyl', 'eight_homogeneous', 'RiemQ_eq', 'RlT_bi', 'bianchi_connection', 'bi_scal', 'bi_gradient', 'bi_q', 'control', 'ratios_distinct', 'derivative_test', 'gauge_ratio', 'combo_homogeneous', 'ranks', 'residue_scheme', 'cited_bound', 'any_target'],
         'r7443_71_campaign41/PROBE_RUN_A.txt; Row70Quartic.lean #print axioms list (r7443+71.27: one-word names the cell selector skips)'),
    52: (['open_leaf_curv', 'horo_on_hyperboloid'], 'r7323_71_instances/PROBE_RUN_R52.txt; CurvatureInstances.lean "Row 52"'),
    75: (['gowdy_tz_field'], 'r7323_71_instances/PROBE_RUN_R75.txt; CurvatureInstances.lean "Row 75"'),
    72: (['frw_closed'], 'r7335_70_row72/PROBE_RUN_FRW.txt; SecondSeatFRW.lean "Row 72"'),
    99: (['two_surface_gravities'], 'r7315_71_sweep RESULT table step B1; ShadowEngine.lean section SweepB1'),
    64: (['rank_A', 'kernel_A', 'phase_A', 'substrate', 'R_deformed', 'inv_poly', 'orders', 'log_structure', 'ranks_by_order', 'L_coeff', 'rate_factor', 'log_coeff', 'control_weight', 'conventions_three', 'kernel_rotates', 'one_number', 'A6_factor'],
         'r7443_71_campaign35/PROBE_RUN_A.txt; Row64Descent.lean #print axioms list (r7443+71.21: one-word names the cell selector skips)'),
    68: (['completeness', 'orthonormal', 'traceless', 'trace_P', 'level_three', 'drop_one', 'exponent_zero', 'two_point', 'wick', 'wick_receipt', 'support', 'factorises', 'contract', 'eight_values', 'eight_homogeneous', 'value_rank_one', 'pow_homogeneous_3_to_6', 'combo_homogeneous', 'trivia'],
         'r7443_71_campaign36/PROBE_RUN_A.txt; Row68Overlap.lean #print axioms list (r7443+71.21: one-word names the cell selector skips)'),
    73: (['misner', 'unimodular', 'R3_round', 'R3_milnor', 'taylor', 'shapes', 'calibration', 'kinetic_linear', 'kinetic_exponential', 'unit_jacobian', 'quartic_vev', 'cubic_three_quanta', 'one_quantum_cancels', 'cubic_shift', 'fock_receipt', 'normalisation', 'total_shift', 'at_level_three', 'threshold', 'density_a6', 'linear_solves', 'rank_two', 'dmu_residues', 'dovmu_residues', 'faulhaber', 'log_coeff', 'residue_product'],
         'r7443_71_campaign37/PROBE_RUN_A.txt; Row73Vertex.lean #print axioms list (r7443+71.21: one-word names the cell selector skips)'),
    57: (['rank_eq_of_factor', 'Exp3', 'Exp3', 'turnover_unique', 'eps_size', 'inv_exp', 'source_moves', 'gradient_six', 'gradient_eight', 'realizable_cubics', 'dK_split', 'sector_orders', 'P_closed', 'ranks_by_order', 'second_direction', 'L_coeff', 'harmonic_closed', 'log_coeff', 'no_fourth_convention', 'zeta_face', 'trace_face', 'curvature_face', 'control_weight', 'faces_together', 'two_halves', 'vertex_scaled'],
         'r7443_71_campaign39/PROBE_RUN_A.txt; Row57Second.lean #print axioms list'),
    69: (['eps4_sign', 'eps4_det', 'eps4_zero_of_not_injective', 'eps4_antisymm', 'sum_eps', 'pontryaginLC_eq', 'GW_apply', 'gowdy_pontryagin', 'gowdy_plane_wave_pontryagin', 'gowdy_areal_pontryagin', 'gowdy_areal_weight', 'gowdy_areal_silenced', 'gowdy_areal_psi_constant', 'gowdy_areal_omega_constant', 'areal_profile_exists', 'cycle_average', 'cycle_average_quarter', 'cycle_average_in_step', 'cycle_average_anti_phase', 'cycle_average_bound', 'reflection_is_half_turn'],
         'r7443_71_campaign40/PROBE_RUN_A.txt; Row69Pontryagin.lean #print axioms list'),
    63: (['A1_cosh', 'A2_variance', 'A2_const', 'A2_sign', 'A2_sample', 'A3_radiation', 'A3_flat', 'B1_bare', 'B2_trace', 'B3_R', 'B3_slope', 'B3_iff', 'rank_one_of_const', 'moment_det_neg', 'C_controls', 'C_tower', 'C_receipt', 'adot_sq', 'Rtow_eq', 'zeta_rule_eq', 'Bj_zero', 'B3_zero', 'zeta_free_tower', 'zeta_protected', 'zeta_odd', 'series_inputs', 'rule_is_limit'],
         'r7443_71_campaign38/PROBE_RUN_A.txt; Row63Anomaly.lean #print axioms list (r7443+71.21: one-word names the cell selector skips)'),
}


def sweep_map():
    out, prev = {}, set()
    for k in range(1, 18):
        txt = (F / f'r7315_71_sweep/PROBE_RUN_B{k}.txt').read_text(encoding='utf-8')
        cur = set(re.findall(r"'ShadowProbe\.([^']+)'", txt))
        new = cur - prev
        prev = cur
        row = [r for r, s in SWEEP_STEPS.items() if s == k][0]
        out[row] = sorted(new) if k > 1 else []   # B1's run prints the whole earlier probe; read by hand
    return out


def main(join_scope):
    idx = index()
    rows = list(csv.reader(open(F / 'r7325_71_inventory/ROWS.tsv', encoding='utf-8'), delimiter='\t'))
    head, body = rows[0], [r for r in rows[1:] if len(r) > 3 and r[0].strip().isdigit()]
    readings = {r[0]: r[1] for r in csv.reader(open(F / 'r7285_71_restate/READINGS.tsv', encoding='utf-8'),
                                                  delimiter='\t') if r and r[0].isdigit()}
    js = {}
    for r in csv.reader(open(join_scope, encoding='utf-8'), delimiter='\t'):
        if r and r[0].isdigit():
            js[r[0]] = r
    sw = sweep_map()
    out = []
    for r in body:
        i, status, cell = r[0], r[2], r[3]
        files_named = set(re.findall(r'probes/[A-Za-z0-9_]+\.lean', cell))
        cands = collections.OrderedDict()
        for tok in re.findall(r"[A-Za-z_][A-Za-z0-9_'₀-₉]*", cell):
            if tok in idx and '_' in tok and len(tok) > 3:
                cands.setdefault(tok, 'cell')
        if i in js:
            for tok in js[i][5].split(';'):
                if tok and tok != '-':
                    cands.setdefault(tok, 'join_scope')
        for tok in sw.get(int(i), []):
            cands.setdefault(tok, 'sweep')
        for tok in MANUAL.get(int(i), ([], ''))[0]:
            cands.setdefault(tok, 'manual')
        decl, unres = [], []
        for tok, src in cands.items():
            hits = idx.get(tok, set())
            if not hits:
                unres.append(f'{tok}(not declared)'); continue
            pick = [h for h in hits if f'probes/{pathlib.Path(h[0]).name}' in files_named or h[0] in files_named]
            if not pick:
                pick = sorted(hits) if len(hits) == 1 else []
            if not pick:
                unres.append(f'{tok}(in {len(hits)} files: ' + ','.join(sorted(h[0] for h in hits)) + ')'); continue
            for f_, full in pick:
                decl.append(f'{full} @ {f_}')
        out.append([i, status, readings.get(i, ''), '; '.join(decl), ','.join(sorted(set(cands.values()))),
                    '; '.join(unres)])
    with open(HERE / 'JOIN.tsv', 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, delimiter='\t', lineterminator='\n')
        w.writerow(['index', 'status', 'receipt', 'decl', 'sources', 'unresolved'])
        w.writerows(out)
    # the registered PARSE score: an identifier named with a file, NOT declared in that file
    bad = []
    for i, r in js.items():
        if r[3] != 'PARSE':
            continue
        named = [f for f in r[4].split(';') if f and f != '-']
        miss = [t for t in r[5].split(';') if t and t != '-'
                and not any(h[0] == f for h in idx.get(t, set()) for f in named)]
        if miss:
            bad.append((i, miss))
    print(f'PARSE rows: {sum(1 for r in js.values() if r[3] == "PARSE")}; naming an identifier not declared in the named file: {len(bad)}')
    for i, m in bad:
        print(f'   row {i}: {m}')
    absent = [i for i, r in js.items() if r[3] == 'ABSENT']
    print(f'ABSENT rows: {len(absent)}; resolved to declared names: {sum(1 for o in out if o[0] in absent and o[3])}')
    print(f'{len(out)} rows; with decl {sum(1 for o in out if o[3])}; with unresolved {sum(1 for o in out if o[5])}')


BUILT = ('DONE', 'LIMIT OF A DONE ROW', 'ORDER: ENGINE-REACHABLE')


def write_rows():
    """Lift JOIN.tsv into ROWS.tsv's two new columns. `receipt` for every row; `decl` only where something is
    built (DONE, its halves, LIMIT's carrying theorems, the ORDER row's built part) -- never for ROW / LIBRARY GAP /
    GENERIC-METRIC, whose cells may NAME a theorem without being carried by it. Grouped by file, repo-relative."""
    join = {r[0]: r for r in csv.reader(open(HERE / 'JOIN.tsv', encoding='utf-8'), delimiter='\t')}
    path = F / 'r7325_71_inventory/ROWS.tsv'
    lines = path.read_text(encoding='utf-8').split('\n')
    out = []
    for n, line in enumerate(lines):
        f = line.split('\t')
        if n == 0:
            out.append('\t'.join(f[:5] + ['receipt', 'decl'])); continue
        if len(f) < 5 or not f[0].isdigit():
            out.append(line); continue
        j = join[f[0]]
        decl = ''
        if f[2].startswith(BUILT) and j[3]:
            byfile = collections.OrderedDict()
            for d in j[3].split('; '):
                name, f_ = d.split(' @ ')
                byfile.setdefault(f_, []).append(name)
            decl = ' | '.join(f'computations/formalisation/lean/{f_}: ' + ', '.join(ns) for f_, ns in byfile.items())
        out.append('\t'.join(f[:5] + [j[2], decl]))
    path.write_text('\n'.join(out), encoding='utf-8')

if __name__ == '__main__':
    main(sys.argv[1])
    if '--write' in sys.argv:
        write_rows()
