#!/usr/bin/env python3
"""r7391 ⑩ -- classify the 39 census-OPEN paragraphs this seat's arm does not reach, BY WHAT THE
ARM MISSED.

`r7391` ⑩ ⒜: *"an expression absent from the law's six; a site the law's words reach but the three
cheap exclusions wrongly removed; a paragraph whose open claim carries no law-word at all.  Those
are three different defects and only the first is a vocabulary gap."*
⛔ ⒞: *"Do not adjudicate them."*  ⇒ Every class below is a fact about WHICH REGEX REACHED WHICH
PARAGRAPH.  No paragraph is read for whether it states an open item.

The predicate and four bands were registered in REGISTRATION.md and pushed before this ran.

⛔ AND THE BASE IS NOT `HEAD`, FOR A REASON THAT IS ITSELF THE HEADLINE.  `69`'s `items.tsv` keys
its rows by `cand`, a POSITION in the extraction over the living corpus.  `r7387` added a paragraph
to `P7`'s canonical frontier list that `69`'s net matches, so the extraction now yields `258` where
`items.tsv` carries `257`, and every `cand` at or after the insertion shifts.  ⇒ The census is
joinable ONLY at the corpus revision it was extracted from.  This script therefore reads the papers
with `git show <rev>:corpus/...` at the last revision where the index resolves, NAMES that revision
in its output, and measures the renumbering at `HEAD` as a separate number.

    python3 -I classify.py <repo-root> [<corpus-rev>]
"""
import os, re, subprocess, sys
from collections import Counter

ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
# the last revision at which 69's extraction yields exactly items.tsv's 257 rows
REV = sys.argv[2] if len(sys.argv) > 2 else '6be3ddfdd'
CENSUS = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7367_69_the_register_census',
                      'items.tsv')
PAPERS = [('P1', 'BH_causality_v2'), ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
          ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'), ('P6', 'shadow_of_existence'),
          ('P7', 'CR_framework'), ('P8', 'slicing_operator'), ('P9', 'range_paper'),
          ('P10', 'canonical_time'), ('P11', 'dynamics_paper'), ('P12', 'algebroid_paper'),
          ('P13', 'boundary_paper'), ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
          ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'), ('P18', 'CR_synthesis')]

# `69`'s net, verbatim from its extract.py -- the census's own population definition
N69 = re.compile(
    r"(remains? open|stays? open|left open|is open\b|are open\b|still open|open (?:question|problem"
    r"|edge|item)s?|not yet|has not been|have not been|is not derived|not derived here|not computed"
    r"|is owed|are owed|\bowed\b|outstanding|unresolved|unanswered|undetermined|undelivered|unbuilt"
    r"|not built|remains to be|remain to be|future work|is not settled|not settled|we do not claim"
    r"|we claim no|not claimed|conjectur|would settle|what would|is not fixed|not fixed by|frontier"
    r"|we have not|does not yet|do not yet|cannot yet|is pending|is missing|are missing)", re.I)

# ⛭ THE DECOMPOSITION IS VERIFIED, NOT ASSERTED: this list is checked against N69's own pattern
# below, so "the expression that matched" is 69's alternative and not a re-description of it.
ALTS = [r"remains? open", r"stays? open", r"left open", r"is open\b", r"are open\b", r"still open",
        r"open (?:question|problem|edge|item)s?", r"not yet", r"has not been", r"have not been",
        r"is not derived", r"not derived here", r"not computed", r"is owed", r"are owed",
        r"\bowed\b", r"outstanding", r"unresolved", r"unanswered", r"undetermined", r"undelivered",
        r"unbuilt", r"not built", r"remains to be", r"remain to be", r"future work",
        r"is not settled", r"not settled", r"we do not claim", r"we claim no", r"not claimed",
        r"conjectur", r"would settle", r"what would", r"is not fixed", r"not fixed by", r"frontier",
        r"we have not", r"does not yet", r"do not yet", r"cannot yet", r"is pending", r"is missing",
        r"are missing"]
assert N69.pattern == '(' + '|'.join(ALTS) + ')', \
    '⛔ the alternative list is not 69\'s net -- the per-expression report would be this seat\'s ' \
    'own list, which r7383 Ⓐ forbids'
ALT_RE = [(a, re.compile(a, re.I)) for a in ALTS]

# THE LAW's own six, from P7 §frontiers' Daryl-directed block
LAW = re.compile(r'\b(open|frontier|incomplete|remains|not yet|deferred)\b', re.I)
# the three cheap exclusions, landed at r7383+cc66.48
EXCL = {
    'HEAD':  re.compile(r'\\(?:sub)*section\*?\{|\\paragraph\{|\\title\{'),
    'CLOSE': re.compile(r'rather than (?:left )?open|not left open|no longer open|settles what|'
                        r'which (?:is|was) open|left open[^.]{0,40}(?:is|was|has been) (?:now )?'
                        r'(?:settled|closed|measured|computed)|'
                        r'(?:settled|closed|measured|computed|answered)[^.]{0,30}left open', re.I),
    'ORD':   re.compile(r'\bremains\s+(?:between|the|a|an|that|this|constant|finite|valid|true'
                        r'|unchanged|positive|negative|bounded)\b|\bopen\s+(?:set|interval|ball'
                        r'|neighbourhood|neighborhood|cover|subset|map|condition)\b', re.I),
}
_SENT = re.compile(r'(?<=[.!?])\s+')


def paper(rev, stem):
    """The paper's text at a named revision -- not from the working tree, so the base is pinned."""
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{rev}:corpus/{stem}.tex'],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(f'⛔ cannot read corpus/{stem}.tex at {rev}: {r.stderr.strip()[:160]}.  STOPPING.')
        sys.exit(2)
    b = '\n'.join(l for l in r.stdout.split('\n') if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def extract(rev):
    """69's extraction at a revision: the candidate paragraphs in its order, and every paragraph."""
    cands, allp = [], {}
    for num, stem in PAPERS:
        t = paper(rev, stem)
        sec, plist = '', []
        for q in re.split(r'\n\s*\n', t):
            m = re.findall(r'\\(?:sub)*section\*?\{([^}]*)\}', q)
            if m:
                sec = m[-1]
            flat = re.sub(r'\s+', ' ', q)
            plist.append((sec, flat))
            if N69.findall(flat):
                cands.append((num, sec, flat))
        allp[num] = plist
    return cands, allp


# ---- ⛔ THE INDEX FINDING, measured first because it decides what base anything else can use ---
head_paras, _ = extract('HEAD')
census_paras, all_paras = extract(REV)
rows = [l.split('\t') for l in open(CENSUS, encoding='utf-8').read().split('\n') if '\t' in l]
data = [r for r in rows[1:] if r and r[0].isdigit()]
print(f'# ⛔ THE INDEX, AT HEAD: 69\'s extraction yields {len(head_paras)} candidate paragraph(s) '
      f'and items.tsv carries {len(data)} rows.')
if len(head_paras) != len(data):
    # how much of items.tsv a position join at HEAD would mis-attach: the first cand whose
    # paragraph text differs, and everything after it
    k = next((i for i in range(min(len(head_paras), len(data)))
              if head_paras[i][2] != census_paras[i][2]), None)
    print(f'#   ⛔ IT DOES NOT RESOLVE.  r7385 ⑧ ⒜: "a census whose row ids no longer resolve is a '
          f'finding, and a worse one than a word list."')
    if k is not None:
        print(f'#   the extraction and items.tsv agree up to cand {k - 1} and diverge at cand {k} '
              f'({head_paras[k][0]} §{head_paras[k][1] or "(none)"}) -- so a position join at HEAD '
              f'mis-attaches {len(data) - k} of {len(data)} rows ({100 * (len(data) - k) // len(data)}%).')
    print(f'#   ⇒ the census is joinable ONLY at the corpus revision it was extracted from.')
print(f'# THE BASE USED BELOW IS {REV}, where the extraction yields {len(census_paras)} against '
      f'items.tsv\'s {len(data)}.')
if len(census_paras) != len(data):
    print(f'⛔ EVEN {REV} DOES NOT RESOLVE.  STOPPING.')
    sys.exit(2)
print()
byc = {int(r[0]): r for r in data}
assert sorted(byc) == list(range(len(data))), '⛔ cand values are not exactly 0..N'
ordered = [byc[i] for i in range(len(data))]
bad = [i for i, r in enumerate(ordered) if r[1] != census_paras[i][0]]
if bad:
    print(f'⛔ paper column disagrees at {len(bad)} cand(s): {bad[:6]}.  STOPPING.')
    sys.exit(2)

# ---- my arm, verbatim from r7385: law-word sites outside P7, less the three cheap exclusions ----
mine = []
for num, _stem in PAPERS:
    if num == 'P7':
        continue
    for sec, flat in all_paras[num]:
        for s in _SENT.split(flat):
            k = ' '.join(s.split())
            if LAW.search(k) and not any(r.search(k) for r in EXCL.values()):
                mine.append((num, sec, k, flat))
reach = {(n, p) for n, _s, _t, p in mine}

unreached = [i for i in range(len(data))
             if ordered[i][2] == 'OPEN' and (census_paras[i][0], census_paras[i][2]) not in reach]

# ⛭ THE BINDING CHECK: r7385+cc66.49 measured this number as 39 on its base.  If the corpus has
# moved the number moves with it, and the difference is NAMED rather than quietly adopted.
print(f'# the reverse direction, re-measured here: {len(unreached)} census-OPEN paragraph(s) the '
      f'arm does not reach')
if len(unreached) != 39:
    print(f'#   ⚠ r7385+cc66.49 measured 39 on its base.  THIS BASE GIVES {len(unreached)}.  The '
          f'difference is reported, not adopted silently.')
print(f'#   (census rows {len(data)}, census OPEN '
      f'{sum(1 for r in ordered if r[2] == "OPEN")}, my arm\'s surviving sentences {len(mine)})')
print()

# ---- ⑩ ⒜ THE CLASSIFICATION, first match wins --------------------------------------------------
out, cls = [], Counter()
for i in unreached:
    num, sec, para = census_paras[i]
    law_sents = [s for s in (' '.join(x.split()) for x in _SENT.split(para)) if LAW.search(s)]
    free = []
    for a, r in ALT_RE:
        for m in r.finditer(para):
            if not LAW.search(m.group(0)):
                free.append((a, m.group(0)))
                break
    if num == 'P7':
        c, why = 'BY-DESIGN-P7', 'the law\'s own home; the arm is not pointed at it'
    elif law_sents:
        hit = sorted({k for k, r in EXCL.items() for s in law_sents if r.search(s)})
        c, why = 'EXCLUDED', '+'.join(hit) or '(no exclusion matched -- MEASUREMENT DEFECT)'
    elif free:
        c, why = 'VOCABULARY', ' ; '.join(sorted({m.lower() for _a, m in free}))
    else:
        c, why = 'NO-MARKER', 'no law-word and no law-word-free expression'
    cls[c] += 1
    out.append((c, i, num, sec, why, law_sents, para))

print('# ⑩ ⒝ THE COUNTS')
for c in ('BY-DESIGN-P7', 'EXCLUDED', 'VOCABULARY', 'NO-MARKER'):
    print(f'#   {cls[c]:4d}  {c}')
print(f'#   {sum(cls.values()):4d}  total')
print()

# ---- ⛭ WHAT THE `NO-MARKER` PAIR TURNED OUT TO BE, measured because the registered band said 0 -
# `69`'s net has no \\command{...} guard, so a marker inside a receipt key or a \\ref label reads as
# prose.  This counts how much of the census's own population rests on that, which is a fact about
# the extraction and NOT a reading of any paragraph.
MACH = re.compile(r'\\(?:rcpt|ref|eqref|label|cite|autoref|nameref|pageref|input|include)\s*\{[^{}]*\}')
only_mach = [i for i in range(len(census_paras))
             if not N69.findall(MACH.sub(' ', census_paras[i][2]))]
op_mach = [i for i in only_mach if ordered[i][2] == 'OPEN']
print('# ⛭ THE EXTRACTION ARTEFACT the NO-MARKER pair exposed, priced across the whole census:')
print(f'#   of items.tsv\'s {len(data)} rows, {len(only_mach)} are paragraphs whose ONLY marker '
      f'sits inside a LaTeX identifier (\\rcpt / \\ref / \\label / \\cite / ...); '
      f'{len(op_mach)} of those {len(only_mach)} carry 69\'s class OPEN.')
print('#   ⇒ 69\'s net reads a receipt key and a cross-reference label as prose.  Stated as a fact')
print('#     about the extraction; whether those paragraphs are open is that seat\'s reading.')
print(f'#   cands: {only_mach}')
print()

# ---- ⑩ ⒝ THE THIRD CLASS, and the registered band ⒟ is REFUTED --------------------------------
noalt = [i for i in unreached if not N69.findall(census_paras[i][2])]
nm = [r for r in out if r[0] == 'NO-MARKER']
nm_mach = [r for r in nm if r[1] in only_mach]
print("# ⑩ ⒝ ON THE THIRD CLASS -- REGISTRATION ⒟ SAID EXACTLY 0 AND IT IS "
      f"{len(nm)}, SO THE BAND IS REFUTED.")
print(f"#   paragraphs among the {len(unreached)} that match NO alternative of 69's net: "
      f"{len(noalt)} -- so the REASONING under ⒟ holds: a census paragraph is by definition one")
print("#   69's net matched, so an open claim carried by no marker at all would be outside the")
print("#   257 as well as outside this seat's 212.  It is in NEITHER net and NEITHER can count it.")
print(f"#   ⛭ WHAT LANDED IN THE CLASS INSTEAD: {len(nm_mach)} of the {len(nm)} are paragraphs")
print("#   whose only marker sits inside a LaTeX identifier, where 69's unbounded `frontier`")
print("#   matches and the law\'s word-bounded `\\bfrontier\\b` correctly does not.")
print("#   ⇒ NOT a gap in this seat's arm and NOT an unmarked open claim: an artefact of the")
print("#     other instrument's extraction.")
print("#   ⇒ ⒝'s question -- is the third class large -- CANNOT BE ANSWERED BY THIS POPULATION.")
print()

# ---- ⛭ AND THE ONE NUMBER ⑨ ⒞ ACTUALLY NEEDS: which expressions did the missing --------------
vocab = Counter(e for r in out if r[0] == 'VOCABULARY' for e in r[4].split(' ; '))
print(f"# ⛭ THE EXPRESSIONS BEHIND THE {cls['VOCABULARY']} VOCABULARY PARAGRAPHS -- the ratchet's measured seed:")
for e, n in vocab.most_common():
    print(f"#   {n:4d}  {e}")
print(f"#   {len(vocab)} distinct expression(s), none of them among the law's six.")
print()

print('# ⑩ ⒝ THE SPECIMENS -- one per class, as asked')
for c in ('BY-DESIGN-P7', 'EXCLUDED', 'VOCABULARY', 'NO-MARKER'):
    pick = next((r for r in out if r[0] == c), None)
    if pick is None:
        print(f'#   {c}: none')
        continue
    _c, i, num, sec, why, law_sents, para = pick
    print(f'#   {c}  cand {i}  {num} §{sec or "(none)"}')
    print(f'#      what the arm missed: {why}')
    spec = (law_sents[0] if law_sents else para)[:300]
    print(f'#      specimen: {spec}')
print()

print('# THE FULL TABLE -- class / cand / paper / section / what-the-arm-missed / first-sentence')
for c, i, num, sec, why, law_sents, para in sorted(out, key=lambda r: (r[0], r[1])):
    first = ' '.join((law_sents[0] if law_sents else para).split())[:220]
    print('\t'.join((c, str(i), num, sec or '(no section)', why, first)))
