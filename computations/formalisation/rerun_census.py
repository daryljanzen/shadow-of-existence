#!/usr/bin/env python3
"""rerun_census.py <out-file> -- r7365 (3): the census is re-runnable from what is committed, or it is a claim.

THE SELECTOR (committed with the measurement, per cc66's rule), for each ROWS.tsv row whose status begins with DONE:
  rule 1: every identifier in the row's text that names a `theorem` or `lemma` declared in the Lean tree at HEAD
          (ShadowEngine.lean, ShadowFormal/, probes/);
  rule 2: every `theorem` or `lemma` declared inside a section the source names for that row: `section Inst_R<row>`,
          or `section SweepB<k>` where a committed run record's header reads "B<k> (row <row>)".
Nothing else is selected, and nothing is selected by hand.

THE MEASUREMENT: each file holding a selected declaration is rebuilt at HEAD with `#print axioms` appended for every
selected name in it (ShadowEngine through `lake build ShadowEngine` and an importing check file; a probe through a
temporary copy, so the committed file is not touched). A declaration is CLEAN when Lean prints an axiom list inside
[propext, Classical.choice, Quot.sound].

Reported, per row: the cited declarations that resolve, and each one's verdict. Rows whose text resolves to NO
declaration are listed by name: they are claims this script cannot re-run, whatever their prose says.

What the machine has installed (toolchain, dependency revisions, wall times) is PRINTED and asserted of nothing
(60's rule). The pinned inputs are lean/lean-toolchain and lean/lake-manifest.json, both committed.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LEAN = os.path.join(HERE, 'lean')
ROWS = os.path.join(HERE, 'r7325_71_inventory', 'ROWS.tsv')
TMP = os.path.join(LEAN, '.rerun_census')
STD = {'propext', 'Classical.choice', 'Quot.sound'}
DECL = re.compile(r'^\s*(?:private\s+|protected\s+)?(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_\'.]*)', re.M)
NS = re.compile(r'^\s*namespace\s+([A-Za-z_][A-Za-z0-9_.]*)', re.M)
AX = re.compile(r"'([^']+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)")


def lean_files():
    out = [os.path.join(LEAN, 'ShadowEngine.lean')]
    for d in ('ShadowFormal', 'probes'):
        for f in sorted(os.listdir(os.path.join(LEAN, d))):
            if f.endswith('.lean'):
                out.append(os.path.join(LEAN, d, f))
    return out


def index():
    decl = {}
    for f in lean_files():
        txt = open(f, encoding='utf-8').read()
        nss = NS.findall(txt)
        for m in DECL.finditer(txt):
            name = m.group(1).split('.')[-1]
            decl.setdefault(name, []).append((f, nss))
    return decl


SEC = re.compile(r'^section\s+(\S+)\s*$(.*?)^end\s+\1\s*$', re.M | re.S)


def sections():
    """(section name) -> declared names inside it, over the whole tree."""
    out = {}
    for f in lean_files():
        for m in SEC.finditer(open(f, encoding='utf-8').read()):
            out.setdefault(m.group(1), set()).update(x.split('.')[-1] for x in DECL.findall(m.group(2)))
    return out


def b_rows():
    """B<k> -> row, read from the committed run records' headers."""
    out = {}
    for d in sorted(os.listdir(HERE)):
        dd = os.path.join(HERE, d)
        if not (os.path.isdir(dd) and d.startswith('r7')):
            continue
        for f in os.listdir(dd):
            if f.startswith('PROBE_RUN'):
                for m in re.finditer(r'\bB(\d+) \(row (\d+)\)', open(os.path.join(dd, f), encoding='utf-8',
                                                                     errors='replace').read(400)):
                    out.setdefault(m.group(2), set()).add('SweepB' + m.group(1))
    return out


def selected(decl):
    secs, brow = sections(), b_rows()
    rows = []
    for line in open(ROWS, encoding='utf-8').read().split('\n')[1:]:
        f = line.split('\t')
        if len(f) < 4 or not f[2].startswith('DONE'):
            continue
        toks = set(re.findall(r'[A-Za-z_][A-Za-z0-9_\']*', f[3]))
        names = {t for t in toks if t in decl}
        for sec in ['Inst_R' + f[0]] + sorted(brow.get(f[0], ())):
            names |= {n for n in secs.get(sec, ()) if n in decl}
        rows.append((f[0], f[2], sorted(names)))
    return rows


def run(cmd, cwd):
    t = time.time()
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=True)
    return p.returncode, p.stdout + p.stderr, time.time() - t


def main():
    out = sys.argv[1]
    env_path = os.path.expanduser('~/.elan/bin') + os.pathsep + os.environ.get('PATH', '')
    os.environ['PATH'] = env_path
    decl = index()
    rows = selected(decl)
    by_file = {}
    for _, _, names in rows:
        for n in names:
            for f, nss in decl[n]:
                by_file.setdefault(f, (set(), nss))[0].add(n)
    log = []
    p = log.append
    p('# RERUN RECORD -- computations/formalisation/rerun_census.py (r7365 (3))')
    p(f'# date (UTC): {time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}')
    p('# tree commit: ' + subprocess.run('git rev-parse HEAD', shell=True, cwd=HERE, capture_output=True,
                                         text=True).stdout.strip())
    p('# PRINTED, asserted of nothing: ' + run('lean --version', LEAN)[1].strip())
    p('# pinned toolchain (committed): ' + open(os.path.join(LEAN, 'lean-toolchain')).read().strip())
    for pk in json.load(open(os.path.join(LEAN, 'lake-manifest.json')))['packages']:
        p(f'# pinned dependency (committed): {pk["name"]} {pk.get("rev")}')
    shutil.rmtree(TMP, ignore_errors=True)
    os.makedirs(TMP)
    verdict = {}
    for f, (names, nss) in sorted(by_file.items()):
        rel = os.path.relpath(f, LEAN)
        opens = ' '.join(nss)
        prints = ''.join((f'open {opens} in\n' if opens else '') + f'#print axioms {n}\n' for n in sorted(names))
        if rel == 'ShadowEngine.lean':
            code, txt, wall = run('lake build ShadowEngine', LEAN)
            chk = os.path.join(TMP, 'EngineCheck.lean')
            open(chk, 'w').write('import ShadowEngine\n' + prints)
            c2, txt2, w2 = run(f'lake env lean {os.path.relpath(chk, LEAN)}', LEAN)
            code, txt, wall = max(code, c2), txt + txt2, wall + w2
        else:
            cp = os.path.join(TMP, os.path.basename(f))
            open(cp, 'w').write(open(f, encoding='utf-8').read().rstrip('\n') + '\n\n' + prints)
            code, txt, wall = run(f'lake env lean {os.path.relpath(cp, LEAN)}', LEAN)
        errs = len(re.findall(r': error', txt))
        p(f'## {rel}: exit {code}, {errs} error lines, wall {wall:.0f} s (printed, asserted of nothing), '
          f'{len(names)} selected')
        for m in AX.finditer(txt):
            short = m.group(1).split('.')[-1]
            if short in names:
                ax = {a.strip() for a in (m.group(2) or '').split(',') if a.strip()}
                ok = ax <= STD and code == 0
                verdict[(short, f)] = ok
                p(f'{rel}\t{short}\t{"CLEAN" if ok else "NOT CLEAN"}\t[{", ".join(sorted(ax))}]')
        for n in sorted(names):
            if (n, f) not in verdict:
                verdict[(n, f)] = False
                p(f'{rel}\t{n}\tNO AXIOM LINE (did not elaborate)')
    shutil.rmtree(TMP, ignore_errors=True)
    p('## per row (DONE rows only): row, status, cited declarations resolved, verdict')
    unresolved, bad = [], []
    for r, st, names in rows:
        oks = [all(verdict.get((n, f), False) for f, _ in decl[n]) for n in names]
        if not names:
            unresolved.append(r)
            v = 'UNRESOLVED: its text names no declaration at HEAD'
        elif all(oks):
            v = 'RE-RUN CLEAN'
        else:
            bad.append(r)
            v = 'NOT CLEAN: ' + ', '.join(n for n, o in zip(names, oks) if not o)
        p(f'{r}\t{st}\t{len(names)}\t{v}')
    p(f'## SUMMARY: {len(rows)} DONE rows; {len(rows) - len(unresolved) - len(bad)} re-run clean from HEAD; '
      f'{len(bad)} not clean {bad}; {len(unresolved)} unresolved {unresolved}')
    open(out, 'w').write('\n'.join(log) + '\n')
    print(log[-1])


if __name__ == '__main__':
    main()
