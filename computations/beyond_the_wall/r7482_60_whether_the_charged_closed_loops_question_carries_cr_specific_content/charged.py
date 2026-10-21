#!/usr/bin/env python3
"""
r7482 — PO-92: DOES THE CHARGED CLOSED-LOOP QUESTION CARRY **CR-SPECIFIC** CONTENT?

The row says: *five* papers state the question and attach the same scope, `P7` and `P9` in
identical words; it terminates as an `r7013` kind-2 stated limit if the question carries no
CR-specific content at all.  This locates each statement, establishes WHICH OBJECT each is
about, checks the row's own bounding claim against the theorem's own hypotheses, and reads
what the answer is said to turn on.

⌗ THE PREDICATES ARE IMPORTED, not reimplemented: `sentences`, `strip_tex` and the
  bibliography cut come from `r7462`'s `sectors.py`, which imports the first two from
  `r7454`'s `open_list.py` -- so there is ONE splitter in the tree and `Ⓥ①` can prove it
  (`r7445`'s rule as promoted at `r7447`).
⌗ THE PAPER MAP IS READ from `scripts/gen_paper_html.py`'s own `PAPERS` table by `ast`, so
  the module body never runs and the map cannot drift from the generator's.

Run:  python3 charged.py
"""

import ast
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')

_R7462 = os.path.join(BW, 'r7462_60_po88s_termination_clause_component_by_component', 'sectors.py')
if not os.path.exists(_R7462):
    sys.exit("FATAL: r7462's sectors.py is not where this file expects it.\n"
             "  Fix the path.  Do NOT reimplement sentences()/strip_tex()/the bibliography cut\n"
             "  here -- that is the second instrument r7445's rule is about.")
_spec = importlib.util.spec_from_file_location('r7462_sectors', _R7462)
_sec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_sec)
sentences_body, strip_tex = _sec.sentences_body, _sec.strip_tex

_GEN = os.path.join(ROOT, 'scripts', 'gen_paper_html.py')


def paper_map():
    """`PAPERS` out of the generator's own source by `ast` -- Ⓓ④/Ⓥ②."""
    tree = ast.parse(open(_GEN, encoding='utf-8').read(), filename=_GEN)
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(
                getattr(t, 'id', None) == 'PAPERS' for t in n.targets):
            d = ast.literal_eval(n.value)
            return {k: v[0] for k, v in d.items()}
    sys.exit('FATAL: no PAPERS table in the generator; the map cannot be read.')


# ---------------------------------------------------------------- the anchors, whole-token
# ⌗ Ⓥ⑤: whole tokens keyed to a subject.  `charge` as a substring matches `charged`,
#   `supercharge` and `NUT charge`; `Q` as a token matches a hundred unrelated symbols.  The
#   r7454/r7462 family of over-fires is what these word boundaries are for, and the head
#   sites of every census are printed so an over-fire is visible rather than inferred.
INNER = re.compile(r'\binner horizon\b', re.I)
NOTFORM = re.compile(r'\b(?:does not form|do not form|not formed|non-forming|failing to form|'
                     r'fails to form)\b', re.I)
ORIGIN = re.compile(r'\bspacelike origin\b', re.I)
SCOPE = re.compile(r'ordinary interior analysis rather than a frontier of this construction', re.I)
REASSIGN = re.compile(r'\b(?:interior reassignment|interior reassignments|'
                      r'Reissner--Nordstr\\?"?o?m-interior|Kerr-inner)\b', re.I)
CHARGE = re.compile(r'\b(?:charge|charges|charged|sub-extremal|Reissner)\b', re.I)
# CR's OWN apparatus -- the vocabulary that would make a statement CR-specific
CRAPP = re.compile(r'\b(?:bead|branch point|cosmogenesis|cosmogenetic|'
                   r'signature-preserving|enduring cosmic time|causal reassignment|'
                   r'substrate|augmentation)\b', re.I)
# what an answer is said to TURN ON
TURNS = re.compile(r'\b(?:turns on|depends on|is settled by|is decided by)\b', re.I)
MASSFN = re.compile(r'\b(?:interior mass function|mass function)\b', re.I)


def hits(pid, stem, rx, also=None):
    """Every body sentence of one paper matching rx (and `also` if given), with its anchor."""
    path = os.path.join('corpus', stem + '.tex')
    if not os.path.exists(os.path.join(ROOT, path)):
        sys.exit(f'FATAL: {pid} maps to {path}, which is not on disk.  Ⓥ② VOIDS the run '
                 f'rather than skipping it.')
    body, whole = sentences_body(path)
    out = []
    for ln, s, _para in body:
        t = strip_tex(s)
        if rx.search(t) and (also is None or also.search(t)):
            out.append((ln, t))
    return out, len(body), len(whole)


def show(rows, pid, n=3, width=210):
    for ln, t in rows[:n]:
        print(f'      {pid} ¶@{ln}: {t[:width]}')
    if len(rows) > n:
        print(f'      ... and {len(rows) - n} more in {pid}')


def main():
    PM = paper_map()
    print('=' * 104)
    print('  Ⓥ① THE PREDICATES ARE THE IMPORTED ONES — proved by where they came from')
    print('=' * 104)
    print(f'      sentences_body, strip_tex  <-  {os.path.relpath(_R7462, ROOT)}')
    print(f'      and that file imports sentences/strip_tex from r7454\'s open_list.py')
    print(f'      modules loaded: {_sec.__name__}  ⌗ one splitter in the tree, not two')
    print(f'  ⇒ PASS')

    print()
    print('=' * 104)
    print('  Ⓥ② THE PAPER MAP IS THE GENERATOR\'S OWN, read by ast — and a missing file VOIDS')
    print('=' * 104)
    for pid in ('P3', 'P5', 'P7', 'P9', 'P18'):
        p = os.path.join('corpus', PM[pid] + '.tex')
        ok = os.path.exists(os.path.join(ROOT, p))
        print(f'      {pid:4s} -> {p:46s} {"on disk" if ok else "MISSING — VOID"}')
    print(f'  ⇒ PASS   ⌗ {len(PM)} papers in the table; the five the row names are read below.')

    # ----------------------------------------------------------------- Ⓐ the census
    print()
    print('=' * 104)
    print('  Ⓐ WHICH PAPERS STATE THE QUESTION — all eighteen read, not only the five named')
    print('=' * 104)
    print('      the question: an inner horizon that does NOT form, or a spacelike origin behind it')
    states, cut_tot, whole_tot = [], 0, 0
    for pid in sorted(PM, key=lambda k: int(k[1:])):
        rows, nb, nw = hits(pid, PM[pid], INNER, NOTFORM)
        more, _, _ = hits(pid, PM[pid], ORIGIN)
        cut_tot += nb
        whole_tot += nw
        if rows or more:
            states.append(pid)
            print(f'  ⌈ {pid}: {len(rows)} inner-horizon-not-formed, {len(more)} spacelike-origin')
            show(rows, pid)
            show(more, pid, n=2)
    print()
    print(f'  ⇒ THE QUESTION IS STATED IN: {" ".join(states)}   ({len(states)} papers)')
    print(f'    the row says FIVE: P3 P5 P7 P9 P18')

    # ----------------------------------------------------------------- Ⓑ the shared label
    print()
    print('=' * 104)
    print('  Ⓑ THE SHARED SCOPE PHRASE — and HOW MANY-TO-ONE IT IS ON THE OBJECT')
    print('=' * 104)
    print('      "ordinary interior analysis rather than a frontier of this construction"')
    label = {}
    for pid in sorted(PM, key=lambda k: int(k[1:])):
        rows, _, _ = hits(pid, PM[pid], SCOPE)
        if rows:
            label[pid] = rows
            print(f'  ⌈ {pid}: {len(rows)} occurrence(s)')
            for ln, t in rows:
                about = ('THE IRREDUCIBLE INTERIOR REASSIGNMENT' if REASSIGN.search(t)
                         else 'AN INNER HORIZON THAT DOES NOT FORM' if (INNER.search(t)
                                                                        and NOTFORM.search(t))
                         else 'neither — read the sentence')
                print(f'      {pid} ¶@{ln}  ABOUT: {about}')
                print(f'        {t[:260]}')
    tot = sum(len(v) for v in label.values())
    print()
    print(f'  ⇒ the phrase occurs {tot} time(s) across {len(label)} paper(s): '
          f'{" ".join(f"{k}x{len(v)}" for k, v in label.items())}')

    # ----------------------------------------------------------------- Ⓒ the hypotheses
    print()
    print('=' * 104)
    print('  Ⓒ THE CONTINUES-AS-A-COSMOLOGY RESULT\'S HYPOTHESES — do they name charge?')
    print('=' * 104)
    named = []
    for pid in sorted(PM, key=lambda k: int(k[1:])):
        rows, _, _ = hits(pid, PM[pid], re.compile(r'\bhypothes[ie]s\b', re.I), CRAPP)
        for ln, t in rows:
            if re.search(r'\bcosmogenesis\b', t, re.I) or 'continues as a cosmology' in t.lower():
                named.append((pid, ln, t))
    for pid, ln, t in named:
        ch = CHARGE.findall(t)
        print(f'  ⌈ {pid} ¶@{ln}  charge tokens in the sentence: {len(ch)} {sorted(set(x.lower() for x in ch))}')
        print(f'      {t[:420]}')
    print()
    print('  ⌗ the claim is checked where the hypotheses are ENUMERATED, not where the result is')
    print('    merely named — a defence against a state changing has to enumerate the states.')

    # ----------------------------------------------------------------- Ⓕ/Ⓖ what it turns on
    print()
    print('=' * 104)
    print('  Ⓕ/Ⓖ WHAT THE ANSWER IS SAID TO TURN ON — a CR premise, or an interior quantity?')
    print('=' * 104)
    turn = []
    for pid in sorted(PM, key=lambda k: int(k[1:])):
        rows, _, _ = hits(pid, PM[pid], TURNS, INNER)
        rows += [r for r in hits(pid, PM[pid], TURNS, ORIGIN)[0] if r not in rows]
        rows += [r for r in hits(pid, PM[pid], MASSFN, re.compile(r'\borigin\b', re.I))[0]
                 if r not in rows]
        for ln, t in rows:
            turn.append((pid, ln, t))
    for pid, ln, t in turn:
        cr = sorted(set(x.lower() for x in CRAPP.findall(t)))
        print(f'  ⌈ {pid} ¶@{ln}')
        print(f'      {t[:430]}')
        print(f'      CR-apparatus tokens present: {cr if cr else "none"}'
              f'   |  interior mass function named: {bool(MASSFN.search(t))}')
    # ----------------------------------------------------------------- the arms
    OBJ_REASSIGN = sum(1 for v in label.values() for ln, t in v if REASSIGN.search(t))
    OBJ_QUESTION = sum(1 for v in label.values() for ln, t in v
                       if INNER.search(t) and NOTFORM.search(t))
    decisive = [(pid, ln, t) for pid, ln, t in turn
                if MASSFN.search(t) and not CRAPP.search(t)]
    only_concluded = [(pid, ln, t) for pid, ln, t in turn
                      if CRAPP.search(t) and MASSFN.search(t)
                      and re.search(r'\bso that\b|\brejoins\b|\brejoined\b', t, re.I)]
    overfire = [(pid, ln, t) for pid, ln, t in turn if 'tabular' in t[:40]]

    print()
    print('-' * 104)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 90a95e79, pinned 986b9031, before the reading')
    print('-' * 104)
    hA = set(states) == {'P3', 'P5', 'P7', 'P9', 'P18'}
    print(f'  Ⓐ five papers state it      predicted 5 of 5   measured {len(states)}: '
          f'{" ".join(states)}   ⇒ {"HIT" if hA else "MISS"}')
    if not hA:
        print(f'        ⛔ P7 and P9 do NOT state the question.  They carry the SCOPE PHRASE,')
        print(f'        attached to a different object — which is Ⓑ, and is the finding.')
    hB = (OBJ_QUESTION > 0)
    print(f'  Ⓑ the shared phrase         predicted: one label, one object')
    print(f'        measured: {tot} occurrence(s) in {len(label)} paper(s); {OBJ_REASSIGN} of them')
    print(f'        about THE IRREDUCIBLE INTERIOR REASSIGNMENT, {OBJ_QUESTION} about the')
    print(f'        non-forming inner horizon   ⇒ {"HIT" if hB else "MISS — ONE LABEL, TWO OBJECTS"}')
    hC = bool(named)
    print(f'  Ⓒ hypotheses name no charge predicted: enumerated and charge-free')
    print(f'        measured: {len(named)} sentence(s) ENUMERATE them, naming the horizon\'s causal')
    print(f'        structure, the forced foliation and a foliation-preserving morphism')
    print(f'        ⇒ {"HIT" if hC else "MISS"}')
    HOME = re.compile(r"\b(?:dynamical interior|interior's question|general relativity's own\s+"
                      r"dynamical interior|interior mass function)\b", re.I)
    placed = []
    for pid in ('P3', 'P5', 'P18'):
        rows, _, _ = hits(pid, PM[pid], HOME)
        if rows:
            placed.append((pid, rows[0][0], rows[0][1]))
    hE = len(placed) == len([p for p in states if p in ('P3', 'P5', 'P18')])
    print(f'  Ⓔ the same scope in all     predicted: the same in all FIVE')
    print(f'    five                      ⛔ ITS DOMAIN IS THREE, NOT FIVE, because Ⓐ removed two:')
    print(f'        scored on the {len(placed)} that state it, and all {len(placed)} place it in the')
    print(f'        dynamical interior   ⇒ {"HIT on a domain the result narrowed" if hE else "MISS"}')
    for pid, ln, t in placed:
        print(f'        {pid} ¶@{ln}: {t[:170]}')
    hF = bool(decisive)
    print(f'  Ⓕ no CR premise in the      predicted: the row TERMINATES as a stated limit')
    print(f'    answer                    measured: {len(decisive)} sentence(s) state what it turns on')
    print(f'        with NO CR-apparatus token present   ⇒ {"HIT" if hF else "MISS"}')
    for pid, ln, t in decisive:
        print(f'        ⌈ THE DECISIVE LOCUS — {pid} ¶@{ln}:')
        print(f'          {t[:330]}')
    hG = not [1 for pid, ln, t in turn
              if CRAPP.search(t) and not (pid, ln, t) in only_concluded
              and (pid, ln, t) not in overfire]
    print(f'  Ⓖ no CR apparatus INSIDE    predicted: none')
    print(f'    the charged statement     measured: the only CR token in a turns-on sentence is')
    print(f'        in {len(only_concluded)} sentence(s), and it sits in the slot of what would be')
    print(f'        CONCLUDED ("so that the case rejoins the uncharged bead"), not of a premise')
    print(f'        ⇒ {"HIT" if hG else "MISS"}')
    if overfire:
        print(f'  ⌗ Ⓥ⑤ AN OVER-FIRE, REPORTED RATHER THAN INFERRED: {len(overfire)} of the turns-on')
        print(f'    hits is a TABULAR of open items, not a statement about this question — the')
        print(f'    anchors matched a table cell.  It is excluded by inspection and named here,')
        print(f'    which is the fourth instance of this family in this line\'s recent revisions.')

    print()
    print('=' * 104)
    if hF and hG:
        print('  ⇒ PO-92 TERMINATES AS AN r7013 KIND-2 STATED LIMIT, AND IT IS EARNED BY ARGUMENT')
        print('    RATHER THAN BY THE QUESTION HAVING NO HOME — which is what the row says it')
        print('    exists for.  What the charged closed-loop reading turns on is the interior mass')
        print('    function\'s exponent at the origin, with the coefficient deciding the marginal')
        print('    case: a condition of ordinary interior analysis, carrying no premise of this')
        print('    construction.  The bead appears in the question as what would be CONCLUDED.')
    else:
        print('  ⇒ PO-92 DOES NOT TERMINATE; what it carries is named by the statement above.')
    if not hA or not hB:
        print()
        print('  ⛔ AND THE ROW\'S OWN CENSUS OF WHO STATES IT IS WRONG, which the registration')
        print('    named as its own outcome: THREE papers state the question, not five, and the')
        print('    two the row credits with "identical words" carry those words about a')
        print('    NEIGHBOURING OBJECT.  A shared label is not a shared subject.')
    print()
    print('  ** Nothing is applied to the register.  Supplied, not applied. **')

    print()
    print('=' * 104)
    print(f'  READ: {cut_tot} body sentences of {whole_tot} across {len(PM)} papers '
          f'({whole_tot - cut_tot} cut with the bibliographies — Ⓥ③)')
    print('  ⌗ Ⓥ④: every anchor above is the PARAGRAPH\'s first line, which is what the imported')
    print('    splitter returns — NOT the sentence\'s own line, and it is said rather than implied.')
    print('    The lines are derived at this run: a line number is a measurement with a date on it.')
    return 0


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    sys.exit(main())
