#!/usr/bin/env python3
"""r7770 (60) -- the successor to r7612's stale-key arm.

READS: the following paths and no others, declared here so the read index scopes this instrument
rather than inferring it (arm 8 compares this list against this file's own syntax tree):
  * computations/beyond_the_wall/r7612_60_whether_the_reassignment_itself_fixes_the_rate_a_photon_
    path_distance_accumulates_at/photonfamily.py   -- for CLAIM and ADJ, read BY AST and not retyped
  * corpus/<stem>.tex for each stem of r7612's own paper map, read BY AST from the same file
  * receipts/**/*.py head docstrings, for the superseded-expression declarations of arm 6

WHAT THIS REPLACES, AND WHY IT IS A SUCCESSOR AND NOT AN EDIT.  r7612's arm (A) computes
`stale = [k for k in ADJ if k not in seen]` and FAILS on any unmatched key.  A key goes unmatched for
two different reasons and that arm cannot tell them apart:
  * STALE      -- the sentence is not in the corpus at all.  The key is dead and should be retired.
  * WITHDRAWN  -- the sentence is STILL IN PRINT but no longer carries a claim word, so it never
                  enters the candidate set.  That is the paper getting MORE careful, reported as a
                  defect.
** THE ASSERTION THIS INSTRUMENT MAKES, stated as the clause its argument reasons FROM: every
adjudication key resolves to exactly one of MATCHED, WITHDRAWN or STALE, and NO key is STALE. **
A WITHDRAWN key is reported, named, and does NOT fail -- because a sentence losing a claim word is a
state the corpus may legitimately produce, and a defence against a paper state changing has to
enumerate the states it may produce rather than pin one.

r7612's probe is NOT edited: it is a landed predicate and its tree is part of it.  Pointing the
published receipt at this file is a change to a gate 69 landed, so it is ROUTED and not applied.
"""
import ast
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))   # .../<repo>
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
# r7612's directory is resolved BY ITS REVISION PREFIX and asserted unique, rather than written out:
# a long literal path is a second copy of a name that can be renamed under it.
_c = sorted(d for d in os.listdir(BTW) if d.startswith('r7612_60_')) if os.path.isdir(BTW) else []
if len(_c) != 1:
    raise SystemExit(f"FATAL: r7612's directory is not uniquely resolvable under {BTW}: {_c}")
R7612 = os.path.join(BTW, _c[0], 'photonfamily.py')
if not os.path.exists(R7612):
    raise SystemExit("FATAL: r7612's probe is not where this reads it from; the instrument has moved.")

DECLARED_READS = (
    'computations/beyond_the_wall/r7612_60_*/photonfamily.py',
    'corpus/*.tex',
    'receipts/**/*.py',
)


# ------------------------------------------------------------------ r7612's own constants, BY AST
def _literals():
    """CLAIM, ADJ and the paper map lifted out of r7612's probe by syntax tree -- never retyped,
    because a retyped constant is a second copy that drifts (r7445's rule, applied to data)."""
    tree = ast.parse(open(R7612, encoding='utf-8', errors='replace').read())
    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name) and t.id in ('CLAIM', 'ADJ', 'PAPER_FILES', 'RATE', 'DIST'):
                try:
                    out[t.id] = ast.literal_eval(node.value)
                except ValueError:
                    pass
    missing = {'CLAIM', 'ADJ', 'PAPER_FILES', 'RATE', 'DIST'} - set(out)
    if missing:
        raise SystemExit(f"FATAL: r7612's probe no longer carries {sorted(missing)} as literals.")
    return out


LIT = _literals()
CLAIM, ADJ, PAPER_FILES, RATE, DIST = (LIT['CLAIM'], LIT['ADJ'], LIT['PAPER_FILES'],
                                       LIT['RATE'], LIT['DIST'])


def live_papers():
    out = {}
    for stem in PAPER_FILES:
        p = os.path.join(ROOT, 'corpus', stem + '.tex')
        if not os.path.exists(p):
            raise SystemExit(f"FATAL: {stem}.tex is not where this reads it from.")
        out[stem] = open(p, encoding='utf-8', errors='replace').read()
    return out


def sentences(t):
    return [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', t)]


def flat(t):
    return ' '.join(t.split())


# ------------------------------------------------------------------ the state machine
STATES = ('MATCHED', 'WITHDRAWN', 'STALE')


def resolve(papers, adj=None, claim=None):
    """Every key of `adj` resolved to exactly one of STATES, with its evidence.

    MATCHED   -- the key occurs in a sentence that is a candidate: it assigns a distance to a rate
                 AND carries a claim word.
    WITHDRAWN -- the key occurs in the papers' FULL TEXT but in no candidate sentence.  The sentence
                 is in print; what it has lost is the claim word.  ** This is the state r7612's arm
                 could not see, because it only ever looked at the candidate set. **
    STALE     -- the key occurs nowhere in the papers' full text.  ** What is SEARCHED, beside the
                 claim: all 18 papers of r7612's own map, each read whole and whitespace-flattened,
                 and the key flattened the same way -- so this is a search over the full text of
                 every paper the instrument covers, not a grep over a sentence list. **  The key is
                 dead and should be retired.
    """
    adj = ADJ if adj is None else adj
    claim = CLAIM if claim is None else claim
    cand = []
    for stem, txt in papers.items():
        for s in sentences(txt):
            if any(k in s for k in RATE) and any(k in s for k in DIST):
                if any(k in s for k in claim):
                    cand.append((stem, s))
    flat_all = {stem: flat(txt) for stem, txt in papers.items()}
    out = {}
    for k in adj:
        kf = flat(k)
        hits = sorted({stem for stem, s in cand if kf in flat(s)})
        if hits:
            out[k] = ('MATCHED', hits)
            continue
        in_print = sorted({stem for stem, t in flat_all.items() if kf in t})
        out[k] = (('WITHDRAWN', in_print) if in_print else ('STALE', []))
    assert set(st for st, _ in out.values()) <= set(STATES), 'state set is not closed'
    return out


def verdict(res):
    """The assertion: no key is STALE.  WITHDRAWN is reported and does not fail."""
    stale = sorted(k for k, (st, _) in res.items() if st == 'STALE')
    withdrawn = sorted(k for k, (st, _) in res.items() if st == 'WITHDRAWN')
    return (not stale), stale, withdrawn


# ------------------------------------------------------------------ arm 6: the provenance detector
SUPERSEDED_DECL = re.compile(
    r'(?:THE\s+)?SUPERSEDED\s+`([^`]{4,120})`|`([^`]{4,120})`\s+IS\s+SUPERSEDED', re.I)
LABEL_WORDS = ('supersed', 'withdraw', 'no longer', 'retracted', 'the error', 'wrongly',
               'static-region', 'mass-inside-radius', 'not the reading')


def norm_expr(e):
    """LaTeX-insensitive normal form, so a receipt's `-3 Omega_r z(1+z)^3` and a paper's
    `-3\\Omega_r z(1+z)^{3}` are the same string."""
    e = re.sub(r'\\(?:emph|textit|texttt|mathrm|tfrac|frac|left|right)\b', '', e)
    e = re.sub(r'[\\{}$\s,]', '', e)
    return e.lower()


REV_ID = re.compile(r'^r\d{3,5}$')


def is_expression(e):
    """A declared-superseded TOKEN is only an expression if it could appear in a paper's mathematics.

    ** The filter exists because the live corpus has a receipt head that reads "SUPERSEDED `r4494`",
    naming a REVISION rather than a formula.  Hunting a revision id through the papers would make the
    detector a string-presence test over an identifier, which is not what it is for.  The rejects are
    REPORTED by the caller rather than dropped silently. **
    """
    if REV_ID.match(e.strip()):
        return False
    return bool(re.search(r'[0-9+\-*/^=()]|\\[A-Za-z]+', e))


def superseded_declarations(receipt_root=None, keep_rejects=False):
    """Expressions some receipt's own head declares superseded, with the receipt that says so."""
    root = os.path.join(ROOT, 'receipts') if receipt_root is None else receipt_root
    out = []
    for dirpath, _dirs, files in os.walk(root):
        for f in sorted(files):
            if not f.endswith('.py'):
                continue
            p = os.path.join(dirpath, f)
            try:
                src = open(p, encoding='utf-8', errors='replace').read(6000)
            except OSError:
                continue
            for m in SUPERSEDED_DECL.finditer(src):
                e = m.group(1) or m.group(2)
                if not e:
                    continue
                row = (norm_expr(e), e.strip(), os.path.relpath(p, ROOT))
                if is_expression(e) or keep_rejects:
                    out.append(row + ((is_expression(e),) if keep_rejects else ()))
    return out


def unlabelled_mentions(papers, decls, window=400):
    """Where a paper still carries a declared-superseded expression WITHOUT a label beside it.

    ** The label is checked and not only the expression, because a paper may legitimately print a
    superseded expression while saying that it is superseded.  A test that fired on both would be a
    presence test and not a detector (arm 7 seeds it both ways). **
    """
    out = []
    for stem, txt in papers.items():
        t = txt
        norm_map = []           # (normalised index -> original index), built once per paper
        buf = []
        for i, ch in enumerate(t):
            if not re.match(r'[\\{}$\s,]', ch):
                buf.append(ch.lower())
                norm_map.append(i)
        tn = ''.join(buf)
        tn = re.sub(r'\\(?:emph|textit|texttt|mathrm|tfrac|frac|left|right)\b', '', tn)
        for key, shown, where in decls:
            start = 0
            while True:
                j = tn.find(key, start)
                if j < 0:
                    break
                start = j + 1
                orig = norm_map[j] if j < len(norm_map) else 0
                ctx = t[max(0, orig - window):orig + window].lower()
                labelled = any(w in ctx for w in LABEL_WORDS)
                if not labelled:
                    out.append((stem, shown, where, orig))
    return out
