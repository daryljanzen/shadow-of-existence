#!/usr/bin/env python3
"""r7289+70: the move-based sweep's perturbation.  In a scratch worktree at a given commit, make the ORDINARY edits other
seats make every cycle -- one new row in every shared ledger, and HEAD advanced by one empty commit -- and nothing else.

    python3 perturb.py WORKTREE BASE      # creates WORKTREE at BASE, writes the perturbation as two commits, prints the tip

The ledgers are fixed by rule (PREDICTION.md): every tracked `corpus/*.tsv`, `receipts/INDEX.md`, and every root-level
`THE_*.md`, `FOR_*.md`, `*LEDGER*.md`, `PROTECTED_OPEN.md`, `OWED.md`.  The row each gains is shaped like that file's
own last row, so a reader that parses rows reads it as a row; its content names a receipt and a revision that do not
exist (`receipts/ZZ_move_sweep/P1_perturbation.py`, `r9999`), so nothing real can match it."""
import glob
import os
import re
import subprocess
import sys

ROW_TSV = 'receipts/ZZ_move_sweep/P1_perturbation.py'


def sh(cwd, *a):
    return subprocess.run(list(a), cwd=cwd, capture_output=True, text=True, check=True).stdout


def ledgers(root):
    out = sorted(glob.glob(os.path.join(root, 'corpus', '*.tsv')))
    out += [os.path.join(root, 'receipts', 'INDEX.md')]
    for pat in ('THE_*.md', 'FOR_*.md', '*LEDGER*.md', 'PROTECTED_OPEN.md', 'OWED.md'):
        out += sorted(glob.glob(os.path.join(root, pat)))
    return sorted(set(p for p in out if os.path.isfile(p)))


def new_row(path, text):
    lines = [l for l in text.rstrip('\n').split('\n')]
    last = next((l for l in reversed(lines) if l.strip() and not l.startswith('#')), '')
    if path.endswith('.tsv'):
        cells = last.split('\t')
        cells[0] = ROW_TSV
        for i in range(1, len(cells)):
            c = cells[i]
            if c.startswith('"') and c.endswith('"'):
                cells[i] = '"the move sweep perturbation row"'
            elif re.fullmatch(r'-?\d+', c):
                cells[i] = '1'
        return '\t'.join(cells) + '\n'
    if last.lstrip().startswith('|'):
        n = last.count('|') - 1
        cells = ['`' + ROW_TSV + '`' if i == 3 else ('r9999 move-sweep perturbation row' if i == 2 else 'ZZ')
                 for i in range(max(n, 1))]
        return '| ' + ' | '.join(cells) + ' |\n'
    return '\n## `r9999` — move-sweep perturbation row (not a claim)\n\n*A row the move sweep appends; nothing reads it as content.*\n'


def main():
    wt, base = sys.argv[1], sys.argv[2]
    root = sh('.', 'git', 'rev-parse', '--show-toplevel').strip()
    sh(root, 'git', 'worktree', 'add', '-q', '--detach', wt, base)
    touched = []
    for p in ledgers(wt):
        t = open(p, encoding='utf-8', errors='replace').read()
        with open(p, 'a', encoding='utf-8') as fh:
            if not t.endswith('\n'):
                fh.write('\n')
            fh.write(new_row(p, t))
        touched.append(os.path.relpath(p, wt))
    env = dict(os.environ, GIT_AUTHOR_NAME='move sweep', GIT_AUTHOR_EMAIL='sweep@local',
               GIT_COMMITTER_NAME='move sweep', GIT_COMMITTER_EMAIL='sweep@local')
    subprocess.run(['git', 'add', '-A'], cwd=wt, check=True)
    subprocess.run(['git', 'commit', '-q', '-m', 'r9999 move sweep: one row per shared ledger'], cwd=wt, check=True, env=env)
    subprocess.run(['git', 'commit', '-q', '--allow-empty', '-m', 'r9999 move sweep: HEAD advanced'], cwd=wt,
                   check=True, env=env)
    print(len(touched), 'ledger(s) perturbed; tip', sh(wt, 'git', 'rev-parse', 'HEAD').strip())


if __name__ == '__main__':
    main()
