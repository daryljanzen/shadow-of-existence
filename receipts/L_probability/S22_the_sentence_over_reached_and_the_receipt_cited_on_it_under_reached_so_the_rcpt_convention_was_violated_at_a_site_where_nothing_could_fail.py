#!/usr/bin/env python3
r"""S22 -- `r7261`'s `M17`, worked: its two halves are ONE defect at THREE grains, and the grain that
makes it visible is the RECEIPT rather than the paper.

** WHAT `r7261` QUEUED. **  *** `M17` -- `P12`'s central Atiyah sequence stated exact over a base its
own next section says the isotropy drops on (`10, 4, 2, 3, 2, 0`), plus a stratum omitted two
sentences before it is tested. ***  *And `r7263` added a lens rather than an item: `71` found checks
that are SOUND AND WEAKER than the claim they are filed under, and asked for a line of its own if
`P12`'s receipt does the same.*

** ⛭⛭⛭ ⓵ THE FIRST HALF IS SHARPER THAN THE ORDER SAYS: A HYPOTHESIS NAMED AND THEN NOT HONOURED. **
*The sentence reads `For a homogeneous space the action algebroid of G on G/H IS the Atiyah algebroid
of the principal bundle G -> G/H` -- and then writes the sequence over `so(5,1) x C`, with `C` the
whole space of cuts, and calls it exact `at every term`.*
  ⇒ *** `C` is exactly what that hypothesis fails: the same paper's next section says `the so(5,1)
      action on C is NON-TRANSITIVE`, with the mass a modulus transverse to the orbits. ***
  ⌗ ** So it is not an unstated scope.  The sentence NAMES the hypothesis its theorem needs and then
    applies the conclusion to an object that does not satisfy it ** -- *which is worse, because the
    sentence is itself the evidence that the author knew which hypothesis was required.*

** ⛔⛭⛭ ⓶ THE SECOND HALF IS CONTRADICTED BY THE NEXT PARAGRAPH OF ITS OWN SECTION. **  *The strata
list omitted Nariai, isotropy SIX -- while the paragraph after it names Nariai as one of EXACTLY TWO
strata where the grading survives and prints the ordering `10 > 6 > 4 > 3 > 2 > 0` with the six in it,
and the paragraph after that states `the isotropy jumps from four to six` at the seam.*
  ⇒ *** One sentence out of step with the three statements following it, in a list that is read as a
      count of first integrals -- so the entry had to carry what the others carry and not a dimension
      alone. ***

** ⛔⛭⛭⛭ ⓷ AND `r7263`'s LENS LANDS ON THE RECEIPT ATTACHED TO THAT VERY SENTENCE. **  *`I55` quotes
the paper, checks three algebraic identities AT THE SYMMETRIC CUT on explicit matrices with a
two-sided control, and declares in its own `COMPUTES` header that it claims nothing about `C`.*
  ⇒ *** So if the sequence had NOT been exact over `C`, `I55` would still have PASSED. ***  *The
      `\rcpt{}` convention bound at `r2376+c54.166` is `the claim in this sentence is CHECKED by X,
      and X would FAIL if the claim were false`* -- ** and it was violated at a site where nothing
      could fail. **
  ⌈ *This is `71`'s shape and not the fifty-nine before it: **there was never a defect for a gate to
    see, because no gate was asked the wider question.**  The receipt is sound; it is the citation
    that over-reached.*
  ⌊ ** AND THE REPAIR IS THE NARROWING AND NOT AN EXTENSION OF THE RECEIPT. **  *The paper is
    restricted to the orbit -- which its own stratification section already said -- and `I55` now
    ASSERTS that restriction is there, so the two cannot drift apart again.  Extending the receipt to
    the wider claim would have been the other way to close it and it would have been the wrong way:
    the wider claim is false.*

** ⌗ ⓸ WHAT THE READ TURNED UP THAT IS ON NEITHER LIST, at loose grain. **  *The orbit dimensions:
`15 - dim h` is right at every stratum, but the sentence named `a generic eleven` where the generic
orbits are eleven, twelve and thirteen.  **One of four, named as the one.**  Repaired; the sentence's
own point -- the most symmetric cut has the smallest orbit -- is untouched.*

** ⌗ ⓹ THE BANDS. **  *Four pre-registered and pushed before the read.  Two centres missed DOWNWARD
and two dead on, and **both reachable negatives fail to fire**: the Atiyah sentence carried no base
qualifier at all, and a receipt of this paper does show `66`'s shape -- where zero would have been the
more interesting answer.*

⛔ *Sources: the `r7261` order's `M17`; `r7263`'s lens; `PREDICTION.md` and `READING_NOTES.md` of this
revision, pushed before the paper was edited; `P12` read end to end at the trunk and after; `I55`'s
own source at both commits; and the `\rcpt{}` convention as bound at `r2376+c54.166`.*
"""

import ast
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED three-armed instrument

CHECKS = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


_WORD = re.compile(r'\w')


def flat(t):
    return re.sub(r'\s+', ' ', t or '')


def read(rel):
    with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


# ⛔⛭⛭⛭ THE REFERENCE COMMIT IS A LITERAL SHA AND NOT `merge-base HEAD origin/main`, AND THAT IS THE
#   SECOND HALF OF `L-249`'s RULE THIS LINE GOT WRONG.
#   *The first cut of this receipt read `before` at the merge base with `origin/main`.  **On a branch
#   ahead of the trunk that is the right commit; the moment the work MERGES, `merge-base` collapses
#   onto `HEAD` and every historical read returns the LIVE file** -- so each before-and-after gate
#   compares a tree with itself and goes red.  `S21` was red on `main` in the runner-read sweep for
#   exactly this, and the carry ledger named it there before any seat did.*
#     ⇒ *** A historical pin computed against a MOVING REF is not a historical pin.  `L-249` says to
#         pin the state at the commit it stood at; a commit is a sha. ***
#   ⌗ *`S19`'s repair used a literal sha and is immune.  This receipt and its sibling used
#     `merge-base` -- the same seat, the same revision, the right choice once and the wrong one
#     twice -- which is why the guard below asserts the sha RESOLVES and DIFFERS rather than trusting
#     it.*
BEFORE = '412e2aa7'      # the commit r7264's subjects stood at, before this revision edited them


def before_resolves():
    """(the sha resolves, it is an ancestor of HEAD) -- so a bad pin fails LOUDLY and not silently"""
    ok = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'],
                        cwd=ROOT, capture_output=True, text=True).returncode == 0
    anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'],
                         cwd=ROOT, capture_output=True, text=True).returncode == 0
    return ok, anc


def at_base(rel):
    r = subprocess.run(['git', 'show', f'{BEFORE}:{rel}'], cwd=ROOT, capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def held(lit, hay):
    i, n, ok = hay.find(lit), 0, True
    while i >= 0:
        b = hay[i - 1] if i else ' '
        a = hay[i + len(lit)] if i + len(lit) < len(hay) else ' '
        if (_WORD.match(lit[0]) and _WORD.match(b)) or (_WORD.match(lit[-1]) and _WORD.match(a)):
            ok = False
        n += 1
        i = hay.find(lit, i + 1)
    return (n > 0 and ok), n


P12 = 'corpus/algebroid_paper.tex'
I55 = ('receipts/P12_algebroid_paper/'
       'I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_is_not_available.py')
p12, p12_base = flat(read(P12)), flat(at_base(P12))
i55, i55_base = read(I55), at_base(I55)

print()
print('=' * 100)
print("S22 -- M17 worked: the sentence over-reached, the receipt under-reached, and the list that")
print('       would have caught it was missing the stratum')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE HISTORICAL READ IS SHOWN TO WORK BEFORE ANYTHING IS READ THROUGH IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
gate(f'Ⓐ① ⛔⛭⛭ the REFERENCE COMMIT resolves, is an ancestor of HEAD, and both files come back from '
     f'it DIFFERING from the working tree '
     f'(`{len(p12_base)}` against `{len(p12)}` characters of `P12`; `{len(i55_base or "")}` against '
     f'`{len(i55)}` of the receipt).  ** Without this a shallow clone hands every before-and-after '
     f'gate below an empty string and they all pass on nothing -- the defect `r7262` found in its own '
     f'`L-249` work, carried forward as a habit **',
     all(before_resolves())
     and len(p12_base) > 20000 and len(i55 or '') > 4000 and len(i55_base or '') > 4000
     and p12_base != p12 and i55_base != i55)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  ⓵ THE HYPOTHESIS WAS NAMED AND NOT HONOURED, AND IT IS NOW HONOURED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_K_HOM = 'For a \\emph{homogeneous} space the action algebroid of $G$ on $G/H$'
_WIDE = '\\so(5,1)\\times\\C\;\\xrightarrow{\;\\text{anchor}\;}\;T\\C'
_NARROW = '\\so(5,1)\\times\\mathcal{O}\;\\xrightarrow{\;\\text{anchor}\;}\;T\\mathcal{O}'
gate('Ⓑ① ⛔ the sequence stood over the WHOLE base at the trunk and stands over an ORBIT now --- '
     'asserted as a before-and-after on the equation itself and not on prose about it',
     _WIDE in p12_base and _WIDE not in p12 and _NARROW in p12)

_K_NONTRANS = '$\\so(5,1)$-action on $\\C$ is \\emph{non-transitive}'
gate('Ⓑ② ⛔⛭ and the thing that made the wider statement wrong is the PAPER\'s OWN, unmoved by this '
     'revision: the same paper says the action on the base is non-transitive, at the trunk and after',
     _K_NONTRANS in p12_base and _K_NONTRANS in p12)

_ok, _n = held(_K_HOM, p12)
gate(f'Ⓑ③ ⛭ and the hypothesis is now MARKED as a hypothesis where it was carried as a lead-in --- '
     f'`{_n}` occurrence(s), word-aligned',
     _K_HOM in p12 and _ok)

_K_ORBIT = 'the identification is available over an orbit and not over $\\C$'
gate('Ⓑ④ ✔ and the restriction is STATED rather than left to the equation --- a reader who does not '
     'read the subscript still reads the scope',
     _K_ORBIT in p12 and _K_ORBIT not in p12_base)

_K_LEAK = 'that failure is exactly the algebroid connection'
gate('Ⓑ⑤ ✔⛭⛭ AND THE REPAIR STRENGTHENS THE PAPER RATHER THAN WEAKENING IT, which is the one-state '
     'rule working: the failure of the count off the two symmetric strata IS the algebroid '
     'connection, so the restriction states the paper\'s own result instead of retreating from it',
     _K_LEAK in p12)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  ⓶ THE OMITTED STRATUM, AND WHAT THE LIST IS READ AS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_K_ENTRY = ('and, at the double root where the two horizons merge, the Nariai member $\\dS_2\\times '
            'S^2$ with isotropy $\\so(2,1)\\oplus\\so(3)$, dimension six')
gate('Ⓒ① ⛔ the stratum was absent from the list at the trunk and is in it now, with its isotropy '
     'named rather than only its dimension',
     _K_ENTRY in p12 and _K_ENTRY not in p12_base)

_K_ORDERING = 'the ordering $10>6>4>3>2>0$'
_K_TWO = 'it survives at exactly two: Type O'
gate('Ⓒ② ⛔⛭⛭ AND THE CONTRADICTION WAS INTERNAL TO ONE SECTION, asserted at the TRUNK so the finding '
     'is not an artefact of the repair: the next paragraph already printed the ordering WITH the six '
     'in it and already named Nariai as one of exactly two symmetric strata',
     _K_ORDERING in p12_base and _K_TWO in p12_base
     and _K_ORDERING in p12 and _K_TWO in p12)

_K_INTEGRALS = ('the Nariai member, isotropy six, supplies the norm together with the $\\so(3)$ '
                "factor's $L^{2}$ and $L_{z}$")
gate('Ⓒ③ ⛭ and the entry carries what the list is READ as --- a count of first integrals --- rather '
     'than a dimension alone, which is what the pre-registration forbade adding by arithmetic',
     _K_INTEGRALS in p12)

# ⛭ *Cut to the clause that NAMES ITS SUBJECT: the whole sentence opens on `As`, a subordinator,
#   and `r7257`'s adopted test flags it --- which it did, before this key was written.*
_K_ABSTRACT = "its strata are the range paper's Petrov classes"
gate('Ⓒ④ ✔⛭ and the ABSTRACT carries the same sentence WITHOUT a dimension list, so it never carried '
     'the defect and is left alone --- asserted, because `the repair is one site` is a claim and not '
     'a convenience',
     _K_ABSTRACT in p12 and _K_ABSTRACT in p12_base and 'dimension' not in _K_ABSTRACT)

# the loose grain the read turned up: the generic orbit dimensions, computed
_ISO = {'Type O': 10, 'Nariai': 6, 'SdS': 4, 'Bianchi': 3, 'Kerr-dS': 2, 'ZV': 2, 'wall': 0}
_ORB = {k: 15 - v for k, v in _ISO.items()}
_generic = sorted({_ORB[k] for k in ('SdS', 'Bianchi', 'Kerr-dS', 'ZV')})
gate(f'Ⓒ⑤ ⌗ AND THE ONE NEW DEFECT IS ARITHMETIC AND IS COMPUTED HERE, not read off the sentence: '
     f'`15 - dim h` gives `{_ORB["Type O"]}` and `{_ORB["Nariai"]}` at the two symmetric strata and '
     f'`{_generic}` at the generic ones, so `a generic eleven` named ONE OF {len(_generic)}',
     _generic == [11, 12, 13] and _ORB['Type O'] == 5 and _ORB['Nariai'] == 9
     and _ORB['wall'] == 15)

_K_GENERIC = 'against generic orbits of eleven, twelve and thirteen'
gate('Ⓒ⑥ ⌗ and it is repaired, with the stratum names attached so the three numbers are checkable '
     'rather than assertable',
     _K_GENERIC in p12 and 'a generic eleven' in p12_base and 'a generic eleven' not in p12)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  ⓷ THE RECEIPT WAS SOUND AND STRICTLY WEAKER THAN THE SENTENCE IT WAS CITED ON ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_K_RCPT = ('with them the exactness of the sequence at every term'
           '\\rcpt{I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_is_not_available}')
gate('Ⓓ① ⛔ the citation sat on the WIDER sentence at the trunk --- the `\\rcpt{}` and the words `at '
     'every term` in one span, with no scope between them',
     _K_RCPT in p12_base)


def names_of(src):
    """every string literal and every Name the receipt's source carries, by PARSING"""
    lits, names = set(), set()
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            lits.add(n.value)
        elif isinstance(n, ast.Name):
            names.add(n.id)
    return lits, names


_lits_base, _names_base = names_of(i55_base)
_STRAT_WORDS = ('non-transitive', 'stratum', 'strata', 'orbit', 'Nariai', 'Petrov', 'isotropy drops')
_reach = [w for w in _STRAT_WORDS
          if any(w.lower() in l.lower() for l in _lits_base)]
gate(f'Ⓓ② ⛔⛭⛭⛭ AND THE RECEIPT COULD NOT SEE THE WIDER CLAIM, READ BY PARSING ITS OWN SOURCE AT THE '
     f'TRUNK: not one of `{len(_STRAT_WORDS)}` words naming the base\'s stratification appears in any '
     f'string literal it carries (`{len(_reach)}` found), and its assertions are over `so(5,1)` '
     f'matrices and a word census alone.  ** So a FALSE wider claim leaves every one of its gates '
     f'green, and the `\\rcpt{{}}` convention -- `X would FAIL if the claim were false` -- was '
     f'violated at a site where nothing could fail **',
     not _reach and 'contained_in' in _names_base and 'basis_so51' in _names_base)

gate('Ⓓ③ ⛭⛭ and the receipt said so about itself all along, which is why this is `71`\'s shape and '
     'not a gate blind to a defect: its own `COMPUTES` header declares `NOT CLAIMED: anything about '
     '$\\C$\'s topology`.  ** The check was sound and the CITATION over-reached **',
     'NOT CLAIMED: anything about $\\C$\'s topology' in i55_base)

_K_I55_ORBIT = "the orbit $\\mathcal{O}$ of the symmetric cut, where the isotropy is constant"
_K_I55_RULE = 'violated at that site'
gate('Ⓓ④ ✔⛭ and the repair is the NARROWING: the receipt now quotes the scoped sentence and asserts '
     'the restriction is in the paper, so the citation claims exactly what the receipt checks',
     _K_I55_ORBIT in i55 and _K_I55_RULE in i55 and _K_I55_ORBIT not in (i55_base or ''))

_i55_run = subprocess.run([sys.executable, os.path.join(ROOT, I55)],
                          cwd=ROOT, capture_output=True, text=True, timeout=600)
gate(f'Ⓓ⑤ ✔ and the repaired receipt RUNS and passes, asserted by running it here rather than by '
     f'citing it (exit `{_i55_run.returncode}`), with its new section reporting all three halves of '
     f'the restriction',
     _i55_run.returncode == 0 and 'ALL PASS' in _i55_run.stdout
     and 'the sequence is NO LONGER written over C     : True' in _i55_run.stdout)

gate('Ⓓ⑥ ⛭ and the receipt\'s own locator into the paper was STALE and is repaired with it --- it '
     'cited a section and line the Atiyah material had moved out of, and quoted wording the paper no '
     'longer carried',
     '`sec:anchor` L186:' in (i55_base or '') and '`sec:anchor` L186:' not in i55
     and '`sec:bracket`' in i55 and 'sec:anchor L186' in i55)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE FOUR PRE-REGISTERED BANDS, PARSED OUT OF THE PUSHED FILE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PRED = read('computations/beyond_the_wall/r7264_60_the_sequence_and_its_base/PREDICTION.md')
_ROW = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROW.finditer(_PRED)]
gate(f'Ⓔ① ⛭ the bands are PARSED out of the pushed pre-registration and not retyped --- '
     f'`{len(_bands)}` rows, each with a central value inside its own band',
     len(_bands) == 4 and all(lo <= c <= hi for _, c, lo, hi in _bands))

_MEASURED = [0, 0, 1, 1]      # further base-less sites; strata-list repeats; new defects; I20-shape receipts
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m = _MEASURED[_i]
    _in = _lo <= _m <= _hi
    gate(f'Ⓔ{"②③④⑤"[_i]} {"✔" if _in and _m == _c else "⌗" if _in else "⛔"} `{_name.strip()}` --- '
         f'pre-registered `{_c}` in `{_lo}`–`{_hi}`, measured **`{_m}`**'
         + ('' if _m == _c else f'; central value missed by `{abs(_m - _c)}` and the band '
                                f'{"holds" if _in else "BREAKS"}'),
         _in)

gate('Ⓔ⑥ ⌗ and the first negative does NOT fire: the Atiyah sentence carried no base qualifier at '
     'all at the trunk --- not `at the symmetric cut`, not `where the isotropy is constant` --- so '
     'the repair is an ADDITION and not the MOVE I allowed for.  *What it carried instead was the '
     'theorem\'s own hypothesis, which is a third shape and is the finding*',
     'at the symmetric cut' not in flat(at_base(P12) or '').split('the sequence')[0][-400:]
     and 'For a homogeneous space' in p12_base)

gate('Ⓔ⑦ ⛔⛭ and the SECOND negative does not fire either, and the direction matters: I allowed that '
     'NO `P12` receipt would show `66`\'s shape, calling zero the more interesting answer.  **One '
     'does, and it is the receipt attached to the very sentence the order\'s item names** --- so the '
     'lens is not about a population of receipts but reaches the single site under repair',
     not _reach and _K_RCPT in p12_base)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE STANDING RULES: THE DANGLING TEST BEFORE EACH KEY, AND NO NARRATION ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_MINE = [_K_NONTRANS, _K_ORBIT, _K_LEAK, _K_ORDERING, _K_TWO, _K_INTEGRALS, _K_ABSTRACT,
         _K_GENERIC, _K_I55_ORBIT]
def words_only(k):
    """the span with its LaTeX replaced by a placeholder WORD, not deleted

    ⛔ *Deleting it was the first cut and it MANUFACTURED a dangle: `... and not over $\\C$` became
    `... and not over`, which ends on a preposition and flags.  **A normaliser that changes the
    span's last word is measuring its own output**, which is the r7258 lesson about haystacks read
    the other way round.*
    """
    k = re.sub(r'\$[^$]*\$', 'symbol', k)
    k = re.sub(r'\\(?:emph|textit|textbf)\{([^{}]*)\}', r'\1', k)
    return re.sub(r'[\\{}]', '', k)


_dang = [k for k in _MINE if D.dangles(words_only(k))]
gate(f'Ⓕ① ✔⛭ `r7257`\'s order ③ applied as the keys are written and not after: none of the '
     f'`{len(_MINE)}` prose keys dangles under the three-armed test (`{len(_dang)}` flagged), the '
     f'markup stripped first so the test reads words and not control sequences',
     not _dang and D.self_test()[0] is True)

_NARRATION = ['was formerly stated', 'formerly stated as', 'previously stated', 'had stated',
              'an earlier revision', 'in an earlier version', 'corrected from', 'this was wrong',
              'the paper formerly', 'has been corrected', 'used to say']
_hits = [s for s in _NARRATION if s in p12]
gate(f'Ⓕ② ⛭⛭ the one-state rule, in the only form a gate can check: not one of `{len(_NARRATION)}` '
     f'narration phrases is in the repaired paper.  **The history is in this receipt, where the order '
     f'says it goes**',
     not _hits)

# ⛔⛭⛭ MEASURED AGAINST THIS REVISION'S OWN FIRST COMMIT and not against the trunk.  *The first
#   cut diffed the merge-base, which spans the PREVIOUS revision too -- so a `touched nothing else`
#   gate would have reported two papers this revision never opened.  **A restraint gate has to know
#   where the restraint starts.***
_START = subprocess.run(['git', 'log', '--format=%H', '--grep=r7264 pre-registration', '-1'],
                        cwd=ROOT, capture_output=True, text=True).stdout.strip()
_changed = subprocess.run(['git', 'diff', '--name-only', _START], cwd=ROOT,
                          capture_output=True, text=True).stdout.split()
gate(f'Ⓕ③ ⛭ and the repair touched the paper and its own receipt and NOTHING ELSE of the corpus '
     f'bodies --- asserted against the working-tree diff rather than against intention',
     bool(_START) and P12 in _changed and I55 in _changed
     and not [f for f in _changed if f.startswith('corpus/') and f.endswith('.tex')
              and f != P12 and not f.startswith('corpus/appendix_')])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = [l for l, ok in CHECKS if not ok]
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print()
print('  ⓵ ** The hypothesis was NAMED and then not honoured ** -- the sentence wrote `for a')
print('     homogeneous space` and then applied the conclusion to a base its own next section')
print('     calls non-transitive.  Worse than an unstated scope, not better.')
print('  ⓶ ** The omitted stratum was contradicted by the next paragraph of its own section, **')
print('     which already printed the isotropy ordering with the six in it.')
print('  ⛔ ⓷ ** And the receipt cited on the sentence was SOUND AND STRICTLY WEAKER than it: ** a')
print('     false wider claim would have left every one of its gates green, so the rcpt convention')
print('     was violated at a site where nothing could fail.  The repair is the narrowing.')
print('  ⌗ ⓸ ** One new defect, arithmetic: ** a generic orbit dimension named as one value where')
print('     the computation gives three.')
print('  ⌗ ⓹ ** Two centres missed downward, two dead on, and NEITHER negative fires. **')
print()

if _fail:
    raise SystemExit(1)
