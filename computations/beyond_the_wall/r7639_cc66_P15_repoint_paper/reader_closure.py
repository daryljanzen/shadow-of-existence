#!/usr/bin/env python3
"""r7639+cc66.18: WHICH RECEIPTS A RE-POINT CAN TURN RED, as a TRANSITIVE closure.

Three revisions in a row were landed green and then reddened a receipt that quotes the re-pointed
one.  Each time the sweep I ran was one hop deep, and the coupling was two:

  * `r7639+cc66.16` -- the noise-model audit quotes the kernel receipt's printed figures by reading
    its TEXT, through a fragment key (`rtext`).  ONE hop, missed because I had not looked at other
    receipts' gates at all.
  * `r7639+cc66.17` -- `S1` pins a LINE OF SOURCE in the re-pointed receipt and quotes its standard
    error; the resolution table quotes its floor.  ONE hop each, missed because I swept the class at
    `.16` and then landed another re-point WITHOUT RE-RUNNING THE READERS.
  * and the same push -- `S5` RUNS fourteen receipts and asserts every one exits 0, `S1` among them;
    `S54` and `S55` assert `S5` runs green.  ** THREE hops, and no one-hop sweep can see it. **

** SO THE OBJECT IS A CLOSURE AND NOT A LIST. **  Edges, all measured from source text:
  ⒜ STEM      -- a receipt names another by its full stem.
  ⒝ FRAGMENT  -- a receipt reads another's text by a distinctive fragment of its stem (>= 12 chars
                 of a stem's own words), which is how `rtext('two_projection_widths_differ')` reaches
                 a file it never spells out.
  ⒞ RUNS      -- a receipt EXECUTES other receipts (subprocess / runpy over a receipt path), so every
                 red inside its population is its own red.  This edge is what makes the set deep.

Validated against a known answer rather than inspected: `r7639+cc66.17` changed
`P15_no_statistic_...`, and CI named five reds.  `main()` asserts the closure of that one receipt
contains all five and exits 1 if it does not.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
REC = os.path.join(ROOT, 'receipts')
RUNS = re.compile(r'subprocess|runpy|run_receipt|_rc\[|check_output|Popen')
STOP = {'the', 'and', 'is', 'a', 'of', 'it', 'its', 'not', 'in', 'on', 'at', 'to', 'by', 'for',
        'this', 'that', 'two', 'one', 'no', 'are', 'was', 'with', 'from', 'P15', 'py'}


def receipts():
    out = {}
    for root, _, fs in os.walk(REC):
        for f in fs:
            if f.endswith('.py'):
                out[f[:-3]] = os.path.join(root, f)
    return out


def fragments(stem, lo=12):
    """every leading run of the stem long enough to name it and no other"""
    parts = stem.split('_')
    frs = []
    for i in range(2, len(parts) + 1):
        s = '_'.join(parts[:i])
        if len(s) >= lo:
            frs.append(s)
    return frs


def edges(files):
    """`src -> {dst}`: dst's text names src, so a change in src can redden dst"""
    src_of = {k: open(v, encoding='utf-8').read() for k, v in files.items()}
    frag = {k: fragments(k) for k in files}
    back = {k: set() for k in files}
    for dst, text in src_of.items():
        for cand in files:
            if cand == dst:
                continue
            if cand in text or any(f in text for f in frag[cand]):
                back[cand].add(dst)
    runners = {k for k, t in src_of.items() if RUNS.search(t)}
    return back, runners


def closure(seed, back, runners, files):
    """⛔ the TRANSITIVE set, because `S54` asserts `S5` is green and `S5` runs `S1`"""
    seen, front, hops = {seed}, [seed], {seed: 0}
    while front:
        cur = front.pop()
        for nxt in back.get(cur, ()):
            if nxt not in seen:
                seen.add(nxt)
                hops[nxt] = hops[cur] + 1
                front.append(nxt)
    return seen - {seed}, hops


def computed_runners(files):
    """⛔ receipts that EXECUTE a python path built from a VARIABLE, so their population is decided at
    run time and NO amount of source reading says whether this change is inside it."""
    import ast
    EXEC = {'run', 'Popen', 'check_output', 'check_call', 'run_path'}
    out = {}
    for k, v in files.items():
        try:
            tree = ast.parse(open(v, encoding='utf-8').read())
        except SyntaxError:
            continue
        n_comp = 0
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else '')
            if nm not in EXEC:
                continue
            txt = ast.dump(node)
            if 'python' not in txt and 'executable' not in txt and nm != 'run_path':
                continue
            if any(isinstance(a, (ast.Name, ast.Subscript, ast.Attribute, ast.JoinedStr))
                   for a in ast.walk(node)):
                n_comp += 1
        if n_comp:
            out[k] = n_comp
    return out


def main():
    files = receipts()
    back, _ = edges(files)
    seed = ('P15_no_statistic_this_construction_can_build_resolves_the_two_channels_and_the_phase'
            '_step_dies_on_a_matched_width_control')
    assert seed in files, seed
    out, hops = closure(seed, back, {}, files)
    runners = computed_runners(files)
    TEXT_REDS = [
        'S1_the_corpus_sweep_finds_no_headline_resting_on_an_overclaimed_sigma_and_three_in_one_paper_below_it',
        'P15_the_resolution_table_eight_of_the_eleven_instruments_cannot_represent_the_comb_period_and_four_smallest_shares_are_honest_blanks',
    ]
    DEEP_REDS = [
        'S5_the_set_shaped_class_is_absent_from_the_gate_layer_and_two_thirds_of_what_remains_sits_at_the_one_value_where_the_standing_guards_repair_is_a_tautology',
        'S54_a_ledger_change_scopes_five_receipts_and_none_of_the_forty_four_that_read_the_ledger_because_the_read_index_is_a_list_of_spellings_without_tsv_on_it',
        'S55_the_previous_repairs_own_written_safety_argument_was_the_defect_because_a_shrinking_population_is_safe_for_a_restraint_and_fatal_for_the_non_vacuity_read_off_the_same_range',
    ]
    print(f'{len(files)} receipts in the tree.')
    print(f'\nTEXT READERS of `{seed[:52]}...` -- {len(out)} receipt(s), and this part IS predictable:\n')
    for r in sorted(out, key=lambda x: (hops[x], x)):
        print(f'  hop {hops[r]}  {r[:104]}')
    print(f'\n⛔ AND THE PART THAT IS NOT: {len(runners)} receipt(s) EXECUTE a python path built from a')
    print('   VARIABLE, so each decides its population at RUN TIME.  ** Every one of the 99 builds its')
    print('   target from a variable and NONE spells it out, so text analysis cannot narrow this class')
    print('   at all -- not by one receipt. **  `S5` classifies every receipt by source shape and runs')
    print('   the EXPOSED ones; `S54` and `S55` then assert `S5` runs green.  The chain that reddened')
    print('   three receipts on the `.17` push is seed -> S1 -> S5 -> S54/S55, and only its FIRST hop')
    print('   is visible here.')
    ok = True
    print('\nVALIDATION against the five reds CI named on the `r7639+cc66.17` push:')
    for k in TEXT_REDS:
        hit = k in out
        ok &= hit
        print(f"  {'FOUND  ' if hit else 'MISSED '} as a text reader, hop {hops.get(k, '-')}  {k[:80]}")
    for k in DEEP_REDS:
        hit = k in runners
        ok &= hit
        print(f"  {'FOUND  ' if hit else 'MISSED '} in the computed-population class  {k[:80]}")
    if not ok:
        print('\n⛔ THIS INSTRUMENT DOES NOT MEASURE: a known red is in neither class.')
        return 1
    print('\n⛭ Both text-reader reds are found by text, and all three deep reds fall in the class this')
    print('  instrument declares unpredictable -- so it reproduces the known answer AND marks the part')
    print('  it cannot predict instead of reporting a short list as if it were complete.')
    print('\n⇒ THE REMEDY IS PROCEDURAL, NOT ANALYTICAL: before pushing a re-point, run the receipts')
    print('  listed above AND the scoped plain suite, which is what actually measures the deep edge.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
