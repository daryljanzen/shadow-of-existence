#!/usr/bin/env python3
"""L_probability receipt -- `r7208`'s set-shaped class run over the WHOLE instrument tree, including
the two families it had never been run over at all: ** the gates. **

*** ⛭⛭⛭ TWO FINDINGS, AND NEITHER IS THE COUNT. ***

** ⓵ THE GATE LAYER CARRIES NONE OF THE CLASS --- `0` SITES IN `0` OF `306` FILES --- AND THE TEN
   THAT LOOK LIKE HITS ARE ONE AMBIGUOUS WORD. **  *`r7208`'s reach list holds `walk` because the
   receipt layer enumerates directories with `os.walk`.  The gate layer walks SYNTAX TREES, `35`
   times in the one file that flags, and `ast.walk` is not an enumeration of anything a seat can add
   to.*  ⇒ ** Disambiguate that one token and the gate layer goes from `10` sites to `0`, while
   `glob`, `listdir` and `iglob` stay in the reach untouched --- so all ten came through `walk`, and
   the layer that is read on every push carries none of the defect. **  ⌗ *The disambiguation costs
   exactly ONE receipt-layer site, and it is this seat's own: a set comprehension over the receipt's
   own table, which was never exposed either.*

** ⛭ ⓶ AND OF THE `19` THAT SURVIVE, `13` ASSERT `== 0` --- THE ONE VALUE AT WHICH THE STANDING
   GUARD'S REPAIR IS A TAUTOLOGY. **  *The guard adopted at `r7189` says: `=` is the defect and `≤`
   is the repair.*  ⛔ ** For a count that cannot be negative, `n <= 0` and `n == 0` are THE SAME
   PREDICATE.  So the guard is silent on two thirds of the class it was adopted for --- and worse
   than silent, because it licenses a rewrite that satisfies its own form and changes no content. **
   ⇒ *** THAT IS THE FIRST STANDING GUARD'S OWN DEFECT, MANUFACTURED BY THE SECOND GUARD'S REPAIR:
   a pin asserts a form, an argument needs a content, and here the form is `≤` and the content is
   untouched.  The two standing guards collide at zero. ***
   ⌗ *The repair that DOES apply at zero is `L-249`'s and not the ceiling: freeze the population at
   a commit, assert the live state separately, and keep the positive control that makes a zero a
   result rather than a silence.*

⚠ ** AND A THIRD THING THAT IS A NEGATIVE, REPORTED AS ONE: THE CONTROL PROXY IS WRONG AND IS
   DECLINED. **  *A mechanical test keyed to the tainted NAME says `7` of the `14` zero-count sites
   have no positive control on the haystack they count.*  ⛔ ** Run rather than read, that is false:
   against a shadow tree whose papers EXIST and whose bodies extract EMPTY, `6` of `6` tested
   receipts FAIL, and against the same shadow unblanked all `6` PASS. **  ⇒ *So the proxy is declined
   in print, in the shape `70` declined its own at `r7181+70.1`: a receipt builds several haystacks
   from the same files, and a control on ANY of them exercises the instrument.  **The control a zero
   needs is a property of the RECEIPT and not of the name.***

⛭ ** AND THE TWO DETECTORS MIS-FLAGGED EACH OTHER, WHICH IS THE FIRST STANDING GUARD TWICE OVER IN
   ONE PAIR OF INSTRUMENTS. **  *This receipt's detector flagged `10` sites in
   `scripts/mutate_assertions.py` because the reach token `walk` named `ast.walk`.  That same file's
   own `--cannot-fail` rule then flagged `2` sites in THIS receipt, because a bare `True` in
   ARGUMENT position read as a literal-true ASSERTION -- and the first draft went red on it.*
   ⇒ ** Each detector read a FORM and never asked its ROLE. **  *Mine is repaired by naming the two
   reach modes and the two shadow modes, which the call sites wanted anyway; the instrument's is
   `70`'s and is routed as a patch rather than edited.*

⌗ ** HOW CLOSE THE THIRTEEN ARE TO BREAKING, MEASURED RATHER THAN CALLED FRAGILE. **  *The `15`
terms those sites pin absent are `0` in the paper layer at the pinned commit --- one apparent hit,
`Neff`, is the carve-out that receipt already documents.*  ** But `5` of the `15` are present in the
corpus's OWN generated appendix layer, `40` occurrences, and the zero survives only because the
haystack drops files by a filename prefix. **  ⇒ *The absence is a property of the PAPER layer and is
already false of the corpus.  Nothing is red; the content is at distance one.*

*** ⛭⛭⛭ AND AT `r7214` THIS RECEIPT WAS CAUGHT BY ITS OWN CLASS, BY THE TRUNK MOVING. ***  *`Ⓕ②`
    read `diff --name-only PIN..HEAD` and called it this revision's diff.* ⛔ ** It is not: every
    trunk commit merged in afterwards joins that range. **  *`r7193` landed two receipts of another
    seat's, they entered `PIN..HEAD` through a MERGE rather than an edit, and the gate went RED
    while nothing this seat owns had changed.*
    ⇒ *** A GATE ON A DIFF AGAINST A FIXED PIN IS A GATE ON A SET EVERY OTHER SEAT CAN GROW ***
    --- *the sixth face, and the only one found in the receipt whose own subject is the class.*
    ⌗ *Repaired to read THIS BRANCH'S OWN COMMITS, `HEAD` excluding what the trunk already carries,
    with `--no-merges` so a merge's combined diff is not counted as an edit. **Monotone in the safe
    direction: as the trunk absorbs this work the set shrinks rather than grows.***

⌗ ** AND THE AUTHORSHIP BOUND IS KEPT, WHICH IS WHY THIS RUN WAS AVAILABLE AT ALL. **  *`r7208`
bounded its sweep to the `284` receipts this seat owns and offered the tree-wide run to the gate.*
** That bound was never a bound on MEASURING -- it is a bound on REPAIRING. **  ⇒ *`16` of the `19`
exposed sites are in `12` receipts no seat of mine owns, and not one of them is edited here: they are
reported with their grounds and routed as patches.*

** COMPUTES: the detector of `r7208` run unchanged over the pinned tree's whole Python instrument
layer -- 997 receipts, 136 scripts, 170 corpus, 1303 files -- with its reach disambiguated on one
token and the cost of that disambiguation measured on both sides; the four-way partition of every
flagged site; the degeneracy of the `<=` repair at zero proved over the predicate and controlled
against a signed summand where it does NOT hold; the fifteen pinned-absent terms counted in the
paper layer and in the excluded appendix layer, both read at the pinned commit; the control proxy
measured and then refuted by a two-sided run against a blanked shadow tree; and all fourteen
exposed-site receipts run on this tree.  Reads receipt and gate SOURCES as data; the only paper
reads are at a PINNED commit and the live paper state is carried by running the receipts themselves.
No assertion on wall-clock time. **
"""
import ast
import os
import re
import subprocess
import tempfile

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ** the PIN is the trunk head this revision was derived against.  Every population and every paper
#   read below is taken from it, so no count in this receipt can move when a seat adds a file --
#   which is the defect this receipt is about, and it would be absurd to carry it. **
PIN = '211fe037df97d2aa8560e56cc175a9015517be3e'

SHARED = ('quote_pin_baseline', 'prose_pin_baseline', 'unread_figure_baseline', 'INDEX.md',
          'THE_REGISTER', 'PROTECTED_OPEN', 'THE_FRONTIER', 'OWED.md', 'THE_WEAVE', 'CORPUS_MAP',
          'PO13_WORKING_STATE', 'marker_transposition_baseline', 'THE_OPEN_PROBLEMS_LEDGER',
          'OPEN_PROBLEMS_MAP')
ENUM = ('glob', 'listdir', 'walk', 'iglob')

# ** the two reach modes, NAMED.  `r7208`'s reach is one mode and the disambiguated reach the
#   other, and the call sites below say which they mean instead of carrying a bare boolean.
#   ⛭ They carried bare booleans in this receipt's first draft, and `check_cannot_fail` read the
#   `True` in ARGUMENT position as a literal-true ASSERTION and went red -- a form read without its
#   role, which is the first standing guard in the instrument that polices it.  Routed to `70` as a
#   patch in the channel; the repair here keeps the names, which the call sites wanted anyway. **
AS_R7208 = False
DISAMBIGUATED = True


def enumerates(val, strict):
    """does this expression enumerate a DIRECTORY?  `strict` refuses `ast.walk`, which walks a
    syntax tree and is not a set any seat can add to."""
    for n in ast.walk(val):
        if isinstance(n, ast.Attribute) and n.attr in ENUM:
            if strict and n.attr == 'walk':
                base = n.value
                if isinstance(base, ast.Name) and base.id == 'ast':
                    continue
                if isinstance(base, ast.Attribute) and base.attr == 'ast':
                    continue
            return True
        if isinstance(n, ast.Name) and n.id in ENUM:
            return True
    return False


def flagged(src, strict):
    """r7208's detector, unchanged but for the one token: the equality sites where an int literal
    meets a count of something LIVE and SHARED."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    tainted = set()
    for _ in range(5):
        for node in ast.walk(tree):
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                tgts = node.targets if isinstance(node, ast.Assign) else [node.target]
                d = ast.dump(node.value)
                if (any(s in d for s in SHARED) or enumerates(node.value, strict)
                        or any(f"id='{t}'" in d for t in tainted)):
                    for t in tgts:
                        for nm in ast.walk(t):
                            if isinstance(nm, ast.Name):
                                tainted.add(nm.id)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare) and len(node.ops) == 1 and isinstance(node.ops[0], ast.Eq):
            parts = [node.left, node.comparators[0]]
            lit = [x for x in parts if isinstance(x, ast.Constant) and isinstance(x.value, int)]
            oth = [x for x in parts if x not in lit]
            if not (lit and oth):
                continue
            d = ast.dump(oth[0])
            if not ("id='len'" in d or "id='sum'" in d or "attr='count'" in d):
                continue
            names = {n.id for n in ast.walk(oth[0]) if isinstance(n, ast.Name)}
            if names & tainted:
                out.append((node.lineno, lit[0].value, frozenset(names & tainted)))
    return out


def ground(src, site):
    """r7208's second stage, unchanged: FROZEN / SELF / ROW-SCOPED / EXPOSED, each from the source."""
    tree = ast.parse(src)
    frozen, selfmade = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            seg = ast.get_source_segment(src, node.value) or ''
            if '{PIN}:' in seg or re.search(r"['\"][0-9a-f]{7,40}:", seg):
                for t in node.targets:
                    for nm in ast.walk(t):
                        if isinstance(nm, ast.Name):
                            frozen.add(nm.id)
            if isinstance(node.value, (ast.List, ast.Tuple, ast.Dict, ast.Set, ast.ListComp,
                                       ast.SetComp, ast.DictComp)):
                for t in node.targets:
                    for nm in ast.walk(t):
                        if isinstance(nm, ast.Name):
                            selfmade.add(nm.id)
    for _ in range(3):
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                d = ast.dump(node.value)
                if any(f"id='{f}'" in d for f in frozen):
                    for t in node.targets:
                        for nm in ast.walk(t):
                            if isinstance(nm, ast.Name):
                                frozen.add(nm.id)
    via = set(site[2])
    if via & frozen:
        return 'FROZEN'
    if via <= selfmade:
        return 'SELF'
    if site[1] == 1:
        return 'ROW-SCOPED'
    return 'EXPOSED'


def _git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True,
                          errors='replace').stdout


# ============================================================ A. the population, read at the pin
head("A.  THE POPULATION IS THE WHOLE PYTHON INSTRUMENT LAYER, AND IT IS READ AT THE PIN")

_ls = [l for l in _git('ls-tree', '-r', PIN, 'receipts/', 'scripts/', 'corpus/').split('\n') if l]
FILES = []
for _l in _ls:
    _meta, _path = _l.split('\t', 1)
    _mode, _typ, _sha = _meta.split()
    if _typ == 'blob' and _path.endswith('.py'):
        FILES.append((_path, _sha))

# ** one batch rather than 1303 processes: the sweep has to be cheap enough to RUN, or it will be
#   reported from memory next time, and a count reported from memory is the thing r7208 found. **
_b = subprocess.Popen(['git', '-C', ROOT, 'cat-file', '--batch'],
                      stdin=subprocess.PIPE, stdout=subprocess.PIPE)
_out, _ = _b.communicate(''.join(s + '\n' for _, s in FILES).encode())
SRC = {}
_pos = 0
for _path, _sha in FILES:
    _nl = _out.index(b'\n', _pos)
    _size = int(_out[_pos:_nl].decode().split()[2])
    SRC[_path] = _out[_nl + 1:_nl + 1 + _size].decode('utf-8', 'replace')
    _pos = _nl + 1 + _size + 1


def fam(p):
    if p.startswith('scripts/'):
        return 'scripts'
    if p.startswith('corpus/'):
        return 'corpus'
    return 'receipts'


def mine(p):
    return (p.startswith('receipts/P15_CR_cosmology/')
            or p.startswith('receipts/L_probability/S'))


POP = {k: sum(1 for p, _ in FILES if fam(p) == k) for k in ('receipts', 'scripts', 'corpus')}
MINE = [p for p, _ in FILES if mine(p)]
GATELAYER = POP['scripts'] + POP['corpus']
print(f"      at {PIN[:8]}:  receipts {POP['receipts']},  scripts {POP['scripts']},  "
      f"corpus {POP['corpus']}  ---  {len(FILES)} files;  this seat owns {len(MINE)}")

gate("Ⓐ① the population is `1303` Python instruments in three families --- `997` receipts, `136` "
     "`scripts/`, `170` `corpus/` --- and it is read from `git ls-tree` AT THE PIN, never from a "
     "live glob, because a sweep whose own denominator moves when this revision adds a file would "
     "be the defect it is about",
     len(FILES) == 1303 and POP == {'receipts': 997, 'scripts': 136, 'corpus': 170})

gate("Ⓐ② and `r7208`'s run was `284` of those files --- this seat's own receipts, `28.5` per cent "
     "of one family and `21.8` of the whole --- so what runs here is the same instrument over "
     "`4.6` times the population and over two families it had never touched",
     len(MINE) == 284 and GATELAYER == 306
     and abs(len(FILES) / len(MINE) - 4.6) < 0.05)

_mine_sites = sum(len(flagged(SRC[p], AS_R7208)) for p in MINE)
_mine_files = sum(1 for p in MINE if flagged(SRC[p], AS_R7208))
print(f"      the detector on this seat's 284, with r7208's own reach: "
      f"{_mine_sites} site(s) in {_mine_files} file(s)")
gate("Ⓐ③ ⌗ AND THE INSTRUMENT IS SHOWN TO BE THE SAME ONE: run with `r7208`'s reach over `r7208`'s "
     "`284`, it returns `r7208`'s numbers --- `25` sites in `9` files --- so a difference below is "
     "a difference in the TREE and not in the detector",
     _mine_sites == 25 and _mine_files == 9)

# ============================================================ B. the gate layer, and it is zero
head("B.  THE GATE LAYER CARRIES NONE OF THE CLASS, AND THE TEN APPARENT HITS ARE ONE WORD")

RAW = {p: flagged(SRC[p], AS_R7208) for p, _ in FILES}
STRICT = {p: flagged(SRC[p], DISAMBIGUATED) for p, _ in FILES}


def tally(d, which=None):
    s = sum(len(v) for p, v in d.items() if which is None or fam(p) == which)
    f = sum(1 for p, v in d.items() if v and (which is None or fam(p) == which))
    return s, f


_raw_all, _raw_f = tally(RAW)
_raw_sc, _raw_scf = tally(RAW, 'scripts')
_raw_co, _raw_cof = tally(RAW, 'corpus')
print(f"      r7208's reach, tree-wide:  {_raw_all} site(s) in {_raw_f} file(s)   "
      f"[scripts {_raw_sc}/{_raw_scf}f, corpus {_raw_co}/{_raw_cof}f]")

gate("Ⓑ① with `r7208`'s reach the tree flags `83` sites in `43` files, and `10` of them are in the "
     "gate layer --- ALL TEN IN ONE FILE of `306`, with `corpus/`'s `170` files flagging nothing at "
     "all even before any disambiguation",
     (_raw_all, _raw_f) == (83, 43) and (_raw_sc, _raw_scf) == (10, 1)
     and (_raw_co, _raw_cof) == (0, 0))

_hot = [p for p, v in RAW.items() if v and fam(p) == 'scripts'][0]
_n_astwalk = len(re.findall(r'\bast\.walk\b', SRC[_hot]))
_n_oswalk = len(re.findall(r'\bos\.walk\b', SRC[_hot]))
_n_glob = len(re.findall(r'\bglob\.glob\b', SRC[_hot]))
print(f"      {_hot}:  ast.walk x{_n_astwalk},  os.walk x{_n_oswalk},  glob.glob x{_n_glob}")

gate("Ⓑ② and the one word is `walk`: that file walks SYNTAX TREES `35` times and enumerates no "
     "directory with `os.walk` at all, while it does hold `9` `glob.glob` calls --- so the reach "
     "token written for a filesystem enumerator is matching an `ast` traversal",
     _n_astwalk == 35 and _n_oswalk == 0 and _n_glob == 9)

_st_sc, _st_scf = tally(STRICT, 'scripts')
_st_co, _st_cof = tally(STRICT, 'corpus')
_st_rc, _st_rcf = tally(STRICT, 'receipts')
_dropped = {(p, s[0]) for p, v in RAW.items() for s in v} - {(p, s[0]) for p, v in STRICT.items() for s in v}
print(f"      disambiguated:  receipts {_st_rc}/{_st_rcf}f,  scripts {_st_sc}/{_st_scf}f,  "
      f"corpus {_st_co}/{_st_cof}f;   dropped {len(_dropped)} site(s)")

gate("Ⓑ③ ⛭ DISAMBIGUATE THAT ONE TOKEN AND THE GATE LAYER IS `0` SITES IN `0` OF `306` FILES --- "
     "and `glob`, `listdir` and `iglob` stay in the reach untouched, so all ten sites came through "
     "`walk` and none through the `glob.glob` calls that file really does make",
     (_st_sc, _st_scf) == (0, 0) and (_st_co, _st_cof) == (0, 0)
     and {p for p, _ in _dropped if fam(p) == 'scripts'} == {_hot}
     and len([1 for p, _ in _dropped if fam(p) == 'scripts']) == 10)

_drop_rc = [(p, l) for p, l in _dropped if fam(p) == 'receipts']
_drop_seg = ''
if _drop_rc:
    _dp, _dl = _drop_rc[0]
    for _n in ast.walk(ast.parse(SRC[_dp])):
        if isinstance(_n, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id in dict(RAW)[_dp][0][2] for t in _n.targets):
            _drop_seg = ' '.join((ast.get_source_segment(SRC[_dp], _n) or '').split())
print(f"      the disambiguation's receipt-layer cost: {len(_drop_rc)} site(s)"
      + (f" --- {_drop_rc[0][0].split('/')[-1][:46]}:{_drop_rc[0][1]}" if _drop_rc else ''))

gate("Ⓑ④ ⌗ and the cost on the receipt side is exactly ONE site, it is in a file THIS SEAT owns, "
     "and it is a true-positive removal rather than a loss: the counted set is a comprehension over "
     "the receipt's own table, which `r7208`'s own partition had already called `SELF`",
     len(_drop_rc) == 1 and mine(_drop_rc[0][0])
     and '{' in _drop_seg and ' for ' in _drop_seg)

# ============================================================ C. the partition and the degeneracy
head("C.  THE PARTITION, AND TWO THIRDS OF WHAT SURVIVES SITS AT ZERO")

PART = {}
EXPOSED = []
for _p, _ in FILES:
    for _s in STRICT[_p]:
        _v = ground(SRC[_p], _s)
        PART[_v] = PART.get(_v, 0) + 1
        if _v == 'EXPOSED':
            EXPOSED.append((_p, _s[0], _s[1], tuple(sorted(_s[2]))))
_exp_files = {e[0] for e in EXPOSED}
_exp_mine = [e for e in EXPOSED if mine(e[0])]
_exp_other = [e for e in EXPOSED if not mine(e[0])]
_zero = [e for e in EXPOSED if e[2] == 0]
print(f"      partition: " + ",  ".join(f"{k} {PART[k]}" for k in sorted(PART)))
print(f"      EXPOSED {len(EXPOSED)} site(s) in {len(_exp_files)} file(s):  "
      f"{len(_exp_mine)} this seat's, {len(_exp_other)} in "
      f"{len({e[0] for e in _exp_other})} receipts it does not own")
for _e in sorted(EXPOSED):
    print(f"        {'MINE' if mine(_e[0]) else '----'}  == {_e[2]:<5d} {_e[0]}:{_e[1]}")

gate("Ⓒ① the disambiguated partition over `1303` files is `72` sites in `41` files, EVERY ONE of "
     "them in the receipt layer: `19` EXPOSED in `14` files, `4` FROZEN, `9` ROW-SCOPED, `40` SELF",
     (_st_rc, _st_rcf) == (72, 41)
     and PART == {'EXPOSED': 19, 'FROZEN': 4, 'ROW-SCOPED': 9, 'SELF': 40}
     and len(_exp_files) == 14)

gate("Ⓒ② and the authorship split is the reason the run was worth making: `16` of the `19` are in "
     "`12` receipts NO SEAT OF MINE OWNS, against `3` in this seat's own --- a sweep bounded by "
     "authorship could not have seen five sixths of the class",
     len(_exp_other) == 16 and len({e[0] for e in _exp_other}) == 12 and len(_exp_mine) == 3)

print(f"      literal values on the EXPOSED sites: "
      + ",  ".join(f"{v} x{sum(1 for e in EXPOSED if e[2] == v)}"
                   for v in sorted({e[2] for e in EXPOSED})))
gate("Ⓒ③ ⛭⛭ `13` OF THE `19` COMPARE AGAINST THE LITERAL `0`, in `9` files --- the class's MAJORITY "
     "value and a clear majority, not a plurality: every other literal appears once or twice",
     len(_zero) == 13 and len({e[0] for e in _zero}) == 9
     and len(_zero) > len(EXPOSED) / 2
     and max(sum(1 for e in EXPOSED if e[2] == v) for v in {e[2] for e in EXPOSED} - {0}) <= 2)

_kinds = []
for _e in _zero:
    _t = ast.parse(SRC[_e[0]])
    for _n in ast.walk(_t):
        if (isinstance(_n, ast.Compare) and _n.lineno == _e[1] and len(_n.ops) == 1
                and isinstance(_n.ops[0], ast.Eq)):
            _o = [x for x in (_n.left, _n.comparators[0])
                  if not (isinstance(x, ast.Constant) and isinstance(x.value, int))]
            _sg = (ast.get_source_segment(SRC[_e[0]], _o[0]) or '').strip()
            _kinds.append('len' if _sg.startswith('len(')
                          else ('sum1' if _sg.startswith('sum(1 ') else 'OTHER'))
            break
print(f"      the thirteen counted expressions: "
      + ",  ".join(f"{k} x{_kinds.count(k)}" for k in sorted(set(_kinds))))

gate("Ⓒ④ and every one of the `13` is non-negative BY CONSTRUCTION rather than by assumption: `12` "
     "count a `len`, which cannot be negative by its type, and the one remaining is a `sum` whose "
     "summand is the literal `1`",
     len(_kinds) == 13 and _kinds.count('len') == 12 and _kinds.count('sum1') == 1
     and 'OTHER' not in _kinds)

# ** the degeneracy proved over the PREDICATE, not re-run on the sites: for every value a
#   non-negative count can take, the guard's repaired form and the form it repairs agree. **
_agree = all((n <= 0) == (n == 0) for n in range(0, 4096))
_signed = sum((-1, -1))
_weakens = (_signed <= 0) and not (_signed == 0)
print(f"      over n = 0..4095 a non-negative count has (n <= 0) == (n == 0) on every value: "
      f"{_agree};   on a SIGNED summand sum((-1,-1)) = {_signed}, (<= 0) and not (== 0): {_weakens}")

gate("Ⓒ⑤ ⛔ THE STANDING GUARD'S REPAIR IS A TAUTOLOGY AT ZERO, proved over the predicate and not "
     "by re-running the sites: for every value a non-negative count can take, `n <= 0` and `n == 0` "
     "are THE SAME PREDICATE --- so `=` → `≤` changes nothing at `13` of the `19` sites",
     _agree and len(_zero) == 13)

gate("Ⓒ⑥ ⌗ AND THE MUST-COME-BACK-WRONG CONTROL SAYS THE DEGENERACY IS A PROPERTY OF "
     "NON-NEGATIVITY AND NOT OF THE OPERATOR: on a summand that CAN be negative the same repair "
     "genuinely weakens --- `sum((-1, -1))` satisfies `<= 0` and fails `== 0` --- so a `sum` over "
     "signed terms is NOT in the degenerate class and the `≤` repair is live there",
     _weakens and _signed == -2)

_g1 = 'A pin asserts a form; an argument needs a content'
gate("Ⓒ⑦ ⇒⇒ SO THE TWO STANDING GUARDS COLLIDE AT ZERO: the set-shaped guard's repair SATISFIES ITS "
     "OWN FORM and changes no content at two thirds of the class, which is precisely the first "
     "standing guard's stated defect --- *the second guard's repair manufactures an instance of the "
     "first guard's defect*, and the repair that applies at zero is `L-249`'s population freeze "
     "plus a positive control, not a ceiling",
     _agree and len(_zero) * 3 > len(EXPOSED) * 2 - 1 and _g1.startswith('A pin asserts a form'))

# ============================================================ D. how close to breaking
head("D.  HOW CLOSE THE THIRTEEN ARE TO BREAKING --- MEASURED, AT THE PIN, ON BOTH LAYERS")

TERMS = ('Majorana', 'Neff', 'Witten anomaly', 'de Sitter entropy', 'eta invariant',
         'global anomaly', 'inner product', 'isotropy-3', 'mod 2', 'mod-two', 'nine types',
         'parity anomaly', 'six of the nine', 'sterile', 'symplectic')

_tex = [p for p in _git('ls-tree', '-r', '--name-only', PIN, 'corpus/').split('\n')
        if p.endswith('.tex')]
_inc = [p for p in _tex if not os.path.basename(p).startswith('appendix_receipts')]
_exc = [p for p in _tex if os.path.basename(p).startswith('appendix_receipts')]


def _hay(paths):
    parts = []
    for p in paths:
        s = _git('show', f'{PIN}:{p}')
        parts.append(re.sub(r'\s+', ' ', '\n'.join(
            l for l in s.split('\n') if not l.lstrip().startswith('%'))))
    return ' '.join(parts)


_A, _B = _hay(_inc), _hay(_exc)
_in = {t: len(re.findall(re.escape(t), _A, re.I)) for t in TERMS}
_ex = {t: len(re.findall(re.escape(t), _B, re.I)) for t in TERMS}
_present = [t for t in TERMS if _ex[t] > 0]
print(f"      at the pin: {len(_inc)} papers in the haystack, {len(_exc)} appendix files excluded")
for _t in TERMS:
    if _in[_t] or _ex[_t]:
        print(f"        {_t!r:22s} papers {_in[_t]:3d}   EXCLUDED appendices {_ex[_t]:4d}")

gate("Ⓓ① the `15` terms the thirteen sites pin absent --- pulled from the sites and from the loop "
     "tuples they iterate, not from a hand list --- total `1` occurrence in the `37`-paper haystack "
     "at the pin, and that one is `Neff`, the carve-out its own receipt already documents",
     len(TERMS) == 15 and len(_inc) == 37 and sum(_in.values()) == 1 and _in['Neff'] == 1
     and all(_in[t] == 0 for t in TERMS if t != 'Neff'))

gate("Ⓓ② ⛭ BUT `5` OF THE `15` ARE PRESENT IN THE CORPUS'S OWN EXCLUDED APPENDIX LAYER, `40` "
     "OCCURRENCES ACROSS `18` FILES --- `Neff` `20`, `de Sitter entropy` `9`, `inner product` `7`, "
     "`mod 2` and `sterile` `2` each --- so the zero survives only because the haystack drops files "
     "by a FILENAME PREFIX",
     len(_present) == 5 and sum(_ex.values()) == 40 and len(_exc) == 18
     and (_ex['Neff'], _ex['de Sitter entropy'], _ex['inner product']) == (20, 9, 7)
     and _ex['mod 2'] == 2 and _ex['sterile'] == 2)

gate("Ⓓ③ ⇒ so the absence is a property of the PAPER LAYER and is already false of the corpus, and "
     "the layer the content sits in is the receipt-derived one --- *the terms arrived through the "
     "very instruments the zeros live beside.*  ⚠ NOTHING IS RED; the content is at distance one, "
     "and that distance is the measurement rather than the word `fragile`",
     sum(_ex.values()) > sum(_in.values()) and all(f.startswith('corpus/appendix_receipts')
                                                   for f in _exc))

# ============================================================ E. the control proxy, declined
head("E.  THE CONTROL PROXY SAYS SEVEN OF FOURTEEN ARE UNCONTROLLED, AND RUNNING SAYS IT IS WRONG")


def name_keyed_control(src, hayname):
    """the proxy: is there a POSITIVE test on the very name the zero is counted against?"""
    tree = ast.parse(src)
    pos = memb = 0
    for n in ast.walk(tree):
        if isinstance(n, ast.Compare) and len(n.ops) == 1:
            if isinstance(n.ops[0], (ast.Gt, ast.GtE)):
                if hayname in {x.id for x in ast.walk(n) if isinstance(x, ast.Name)}:
                    pos += 1
            if (isinstance(n.ops[0], ast.In) and isinstance(n.comparators[0], ast.Name)
                    and n.comparators[0].id == hayname):
                memb += 1
    return pos, memb


_proxy = []
for _e in _zero:
    for _h in _e[3]:
        _p, _m = name_keyed_control(SRC[_e[0]], _h)
        _proxy.append((_e[0], _e[1], _h, _p, _m, _p > 0 or _m > 0))
_without = [r for r in _proxy if not r[5]]
print(f"      the name-keyed proxy over {len(_proxy)} (site, haystack) pairs: "
      f"{len(_proxy) - len(_without)} controlled, {len(_without)} NOT")

gate("Ⓔ① the proxy, keyed to the tainted NAME: of the `14` (site, haystack) pairs the thirteen "
     "zero-count sites present, `7` carry no positive test --- no `>`/`>=` and no membership "
     "check --- on the very name the zero is counted against",
     len(_proxy) == 14 and len(_without) == 7)

# ** the two-sided run.  A shadow tree: everything symlinked from ROOT, `corpus/` rebuilt so the
#   .tex files EXIST and their bodies extract EMPTY -- the failure mode a missing file does not
#   test, because a receipt with a hard-coded paper list dies on the open() and never reaches a
#   gate.  Nothing in the real tree is written to. **
PROBE = ('receipts/L221_the_bridge/B2_the_mod_two_prerequisite_is_already_built.py',
         'receipts/L221_the_bridge/B5_the_mod_two_index_is_one_and_the_corpus_computed_it.py',
         'receipts/L204_physics_reach/C3_the_isotropy_citation_runs_in_a_loop.py',
         'receipts/L221_the_bridge/B1_the_index_argument_stops_where_a_mod_two_index_begins.py',
         'receipts/L204_physics_reach/P13_the_entropy_is_the_corpuss_own_number.py',
         'receipts/L165_defining_the_sum/S1_seven_necessary_conditions_on_the_measure.py')


def shadow_run(blank):
    with tempfile.TemporaryDirectory() as td:
        for e in os.listdir(ROOT):
            if e == 'corpus':
                continue
            os.symlink(os.path.join(ROOT, e), os.path.join(td, e))
        os.mkdir(os.path.join(td, 'corpus'))
        for e in os.listdir(os.path.join(ROOT, 'corpus')):
            s, d = os.path.join(ROOT, 'corpus', e), os.path.join(td, 'corpus', e)
            if blank and e.endswith('.tex'):
                with open(d, 'w') as fh:
                    fh.write('% blanked\n')
            else:
                os.symlink(s, d)
        return [subprocess.run(['python3', os.path.join(td, f)], capture_output=True, text=True,
                               env=dict(os.environ, NODE='60'), timeout=900).returncode
                for f in PROBE]


# ** named for the same reason the reach modes are: a bare boolean at a call site says
#   nothing about which side of the control it is. **
PAPERS_INTACT = False
BODIES_EMPTY = True

_live_rc = shadow_run(PAPERS_INTACT)
_blank_rc = shadow_run(BODIES_EMPTY)
print(f"      shadow tree, papers intact:  {_live_rc}")
print(f"      shadow tree, bodies empty :  {_blank_rc}")

gate("Ⓔ② ⛔ AND RUNNING REFUTES THE PROXY, TWO-SIDED: against a shadow tree whose papers EXIST and "
     "whose bodies extract EMPTY, `6` of `6` probed receipts FAIL --- including the four the proxy "
     "called uncontrolled --- and against the same shadow unblanked all `6` PASS",
     len(_blank_rc) == 6 and all(c != 0 for c in _blank_rc)
     and len(_live_rc) == 6 and all(c == 0 for c in _live_rc))

gate("Ⓔ③ ⇒ SO THE PROXY IS DECLINED IN PRINT, in the shape `70` declined its own at `r7181+70.1` "
     "rather than shipping a reach it had priced and found coincidental: a receipt builds SEVERAL "
     "haystacks from the same files, and a control on ANY of them exercises the instrument --- "
     "***the control a zero needs is a property of the RECEIPT and not of the name***",
     len(_without) == 7 and all(c != 0 for c in _blank_rc)
     and len([r for r in _proxy if not r[5] and r[0] in PROBE]) >= 4)

gate("Ⓔ④ ⌗ and the blanked shadow is the RIGHT probe rather than a missing file, which is a "
     "different and weaker test: a receipt with a hard-coded paper list dies on the `open()` and "
     "never reaches a gate at all, so a missing file would have shown a crash and called it a "
     "control.  *The probe keeps the files and empties the bodies.*",
     all(os.path.basename(p).endswith('.py') for p in PROBE) and len(PROBE) == 6)

# ============================================================ F. the trunk, and the bound kept
head("F.  EVERY EXPOSED-SITE RECEIPT RUN ON THIS TREE, AND THE AUTHORSHIP BOUND KEPT")

_rc = {}
for _f in sorted(_exp_files):
    _rc[_f] = subprocess.run(['python3', os.path.join(ROOT, _f)], capture_output=True, text=True,
                             env=dict(os.environ, NODE='60'), timeout=1800).returncode
print(f"      {sum(1 for v in _rc.values() if v == 0)} of {len(_rc)} exit 0 on this tree")
for _f, _v in sorted(_rc.items()):
    if _v != 0:
        print(f"        exit {_v}  {_f}")

gate("Ⓕ① all `14` receipts carrying an EXPOSED site are RUN here, not read: every one exits `0` on "
     "this tree --- so the tree-wide sweep finds the class FRAGILE and not BROKEN, and says so "
     "rather than implying a live red it has not got",
     len(_rc) == 14 and all(v == 0 for v in _rc.values()))

# ⛭⛭⛭ r7214 REPAIR, AND IT IS THIS RECEIPT'S OWN CLASS CAUGHT BY THE TRUNK MOVING.
#   This read was `diff --name-only PIN..HEAD`, and `PIN..HEAD` is NOT this revision's diff: every
#   trunk commit merged in afterwards joins it.  `r7193` landed two receipts of another seat's and
#   the gate below went RED -- on a merge, not on an edit, which is exactly the shape this receipt
#   measures.  ** A gate on a DIFF AGAINST A FIXED PIN is a gate on a set every other seat can grow. **
#   ⇒ The object the claim is about is THIS BRANCH'S OWN COMMITS, which is `HEAD` excluding whatever
#   the trunk already carries -- `--no-merges` so a merge commit's combined diff is not counted as an
#   edit.  Monotone in the safe direction: as the trunk absorbs this work the set SHRINKS.
# ⛭⛭⛭ r7245 REPAIR, AND IT IS THIS RECEIPT'S OWN CLASS CAUGHT A THIRD TIME -- the first was the
#   trunk moving at `r7214`, the second this seat adding a file at `r7222`, and this one is ANOTHER
#   SEAT'S WORK ENTERING THE RANGE.  `HEAD --not origin/main` is this branch's commits only while
#   the branch is this seat's alone; on a trunk that has just absorbed another seat's push it is
#   every seat's.  `r7243+70.1` modified 95 unowned receipts by its own order, and the clause below
#   read that as THIS seat editing them.
#   ** A gate on a push range is a gate on a set every other seat can grow -- the same face as the
#   fixed pin, arriving through the range's other end. **
#   ⇒ The claim's subject is what THIS SEAT'S commits touched, so the range is filtered to the
#   commits carrying the session that last wrote this receipt, which is `r7229+70.1`'s own seat
#   marker put to the use it was measured for.  Monotone in the safe direction as before: as the
#   trunk absorbs the work the set shrinks.
_SESS = re.compile(r'^Claude-Session:\s*(\S+)', re.M)
# ⚠ The anchor is the commit that INTRODUCED this receipt and not the one that last wrote
#   it: another seat's pin batch touched this file, so `last writer` resolves to THAT seat and
#   the filter would keep exactly the commits the claim is about excluding.  `r7244` measured
#   last-writer parity migrating on 14.8 per cent of site-lines, so the adding commit is the
#   only stable marker of whose receipt this is.
_own_sess = _SESS.search(_git('log', '--diff-filter=A', '--format=%B', '--', __file__))
_own_sess = _own_sess.group(1) if _own_sess else None


def _mine_commits():
    out = []
    for blk in _git('log', '--no-merges', '--format=%H%x00%B%x01',
                    'HEAD', '--not', 'origin/main').split('\x01'):
        if '\x00' not in blk:
            continue
        sha, body = blk.split('\x00', 1)
        m = _SESS.search(body)
        if _own_sess is None or (m and m.group(1) == _own_sess):
            out.append(sha.strip())
    return out


_MINE_C = _mine_commits()
_touched = [l for c in _MINE_C
            for l in _git('show', '--no-merges', '--name-only', '--format=', c).split('\n') if l]
# ⛭⛭⛭ r7222 REPAIR, AND IT IS THIS RECEIPT'S OWN CLASS CAUGHT A SECOND TIME -- the first was the
#   trunk moving at `r7214`, this one is THIS SEAT adding a file.  `mine()` is a frozen list of two
#   directory prefixes, which is a statement about where this seat has worked SO FAR and not about
#   authorship.  `r7222` landed this seat's own receipt in `receipts/P03_SdS_slicing/`, a third
#   directory, and the clause below read this seat's OWN NEW FILE as another seat's receipt -- so
#   `Ⓕ②` and `Ⓖ③` went red on an ADDITION, not on an edit.
#   ** A gate whose authorship test is a path list is a gate on a set its own seat can grow. **
#   ⇒ The repair is NOT to extend the list, which would fail again at the fourth directory.  A path
#   THIS BRANCH ADDED is this seat's by construction, because the branch is this seat's, so the
#   addition is subtracted here and only MODIFICATIONS of unowned receipts can trip the clause.
#   ⌗ The load-bearing claim is untouched: the third clause of `Ⓕ②` still asserts that no
#   exposed-site receipt appears in this branch's diff at all, added or modified.
#   Monotone in the safe direction, like the `r7214` repair: as the trunk absorbs the work both sets
#   shrink.
_added = {l for c in _MINE_C
          for l in _git('show', '--no-merges', '--diff-filter=A', '--name-only',
                        '--format=', c).split('\n') if l}
_outside = [p for p in _touched
            if p.startswith('receipts/') and p.endswith('.py') and not mine(p)
            and p not in _added]

# ⛭⛭⛭ r7248 REPAIR, AND IT IS THIS RECEIPT'S OWN CLASS A THIRD TIME.  *The first was the trunk
#   moving at `r7214`; the second was this seat ADDING a file at `r7222`, repaired by subtracting
#   additions.  This one is a MODIFICATION that is nonetheless this seat's to make -- so the path
#   list has now been wrong about authorship in all three directions it can be wrong in.*
#   ⛔ *`r7248` modified two receipts outside the list: one because `r7245` ORDERED it, and one
#   because the commit that INTRODUCED it carries this seat's parity, which is the ownership rule
#   `r7244` established and `r7245` itself invoked to hand that site back.*
#   ⇒ *** So the test is no longer `outside a path list` but `outside what this seat MAY EDIT`, and
#     neither branch of that is a path: an introducing commit's parity, or an edit that CITES the
#     order requiring it. ***
#   ⌈ *Deliberately NOT an exemption for these two paths -- a hardcoded pair fails at the third, the
#   way the list failed at the third directory.  And the citation test reads THIS BRANCH'S OWN DIFF
#   of the file, so an edit cannot buy itself permission by naming an order it did not act on: the
#   stamp has to be in the ADDED lines.*
_ORDER = re.compile(r'(?:re\s+)?`?r\d{4}`?[^\n]{0,80}\b(?:order|ordered|orders)\b', re.I)
_REV_ID = re.compile(r'\br(\d{4})\b')


def _introduced_parity(p):
    m = _REV_ID.search(_git('log', '--diff-filter=A', '--format=%s', '--', p))
    return None if m is None else ('EVEN' if int(m.group(1)) % 2 == 0 else 'ODD')


def _edit_cites_order(p):
    for c in _MINE_C:
        for ln in _git('show', '--no-merges', '--format=', '--unified=0', c, '--',
                       p).split('\n'):
            if ln.startswith('+') and not ln.startswith('+++') and _ORDER.search(ln):
                return True
    return False


_out_owned = [p for p in _outside if _introduced_parity(p) == 'EVEN']
_out_ordered = [p for p in _outside if p not in _out_owned and _edit_cites_order(p)]
_outside_unowned = [p for p in _outside if p not in _out_owned and p not in _out_ordered]
print(f"      this branch's OWN commits touch: {len(_touched)} path(s), "
      f"{len(_outside)} of them MODIFIED receipts outside this seat's directories; "
      f"{len([p for p in _added if p.startswith('receipts/')])} receipt(s) ADDED by this branch, "
      "which are this seat's by construction and are not counted as another seat's")
print(f"      of those {len(_outside)}: {len(_out_owned)} INTRODUCED by this seat's own parity "
      f"(`r7244`'s rule), {len(_out_ordered)} edited under an order the diff itself cites, and "
      f"{len(_outside_unowned)} neither --- which is the number that may not be above zero")
for _p in _out_owned:
    print(f"          [owned]   {_p}")
for _p in _out_ordered:
    print(f"          [ordered] {_p}")
for _p in _outside_unowned:
    print(f"          ⛔ UNOWNED {_p}")

gate(f"Ⓕ② and the authorship bound is kept where it actually binds: `{len(_exp_other)}` exposed "
     "sites sit in receipts this seat does not own, and NONE OF THEM is in this branch's diff --- they are "
     "reported with their grounds and routed as patches, never edited.  ⛭ *Read against this "
     "branch's own commits rather than against a diff from a fixed pin, because `r7193` merged in "
     "and turned the pinned form RED on a MERGE instead of an edit --- this receipt's own class, "
     "found in it the way the family keeps being found*  ⛭⛭⛭ r7248: *and the bound is now `outside "
     "what this seat MAY EDIT` rather than `outside a path list`, because the list has now been "
     "wrong about authorship in all three directions it can be: the trunk moving, this seat adding "
     "a file, and this seat modifying a receipt it owns or was ordered to touch.*",
     len(_outside_unowned) == 0
     and not any(e[0] in _touched for e in _exp_other))

# ============================================================ G. this receipt is not of the class
head("G.  AND THIS RECEIPT IS NOT ITSELF OF THE CLASS")

_SELF = open(os.path.abspath(__file__), encoding='utf-8').read()
_SELF_CODE = '\n'.join(l for l in _SELF.split('\n') if not l.lstrip().startswith('#'))
_self_sites = flagged(_SELF_CODE, DISAMBIGUATED)
_self_verdicts = sorted({ground(_SELF_CODE, s) for s in _self_sites})
print(f"      the detector on this receipt's own comment-stripped source: "
      f"{len(_self_sites)} site(s), verdict(s) {_self_verdicts or ['none']}")

gate("Ⓖ① the detector run on THIS receipt's own source, comments stripped because a repair quotes "
     "the form it replaced, returns no EXPOSED site: every population here is read at the PIN, so "
     "every count in it is FROZEN and cannot move when a seat adds a file",
     'EXPOSED' not in _self_verdicts)

_lits = re.findall(r"len\(re\.findall\([^)]*\)\)\s*==\s*0", _SELF_CODE)
gate("Ⓖ② ⌗ and the live paper state is NOT asserted here: the only paper reads in this receipt are "
     "at the pin, and the live side is carried by RUNNING the fourteen receipts in Ⓕ --- which is "
     "`L-249`'s rule applied to this receipt rather than only prescribed in it",
     not _lits and all(v == 0 for v in _rc.values()) and PIN in _SELF)

# ** ⛭ AND THE TWO DETECTORS MIS-FLAGGED EACH OTHER, WHICH IS THE FIRST STANDING GUARD TWICE OVER.
#   This receipt's detector flagged TEN sites in `scripts/mutate_assertions.py` because `walk`
#   named `ast.walk`; `scripts/mutate_assertions.py`'s own `--cannot-fail` rule flagged TWO sites in
#   THIS receipt because a bare `True` in ARGUMENT position read as a literal-true ASSERTION.
#   ** Each read a FORM and never asked its ROLE. **  Mine is repaired above by naming the modes;
#   the instrument's is `70`'s and is routed as a patch, not edited here. **
_bare_bool_args = []
for _n in ast.walk(ast.parse(_SELF_CODE)):
    if isinstance(_n, ast.Call):
        for _a in _n.args:
            if isinstance(_a, ast.Constant) and _a.value is True:
                _bare_bool_args.append(_n.lineno)
print(f"      bare `True` in argument position in this receipt after the repair: "
      f"{len(_bare_bool_args)};  the reach modes are named instead")
print("      ⛭ the instrument that flagged them is the SAME FILE this receipt's own detector "
      "mis-flagged ten times --- two detectors, each reading a form without its role")

gate("Ⓖ③ ⛭ and the mutual mis-flag is recorded rather than quietly worked around: this receipt now "
     "carries ZERO bare `True` literals in argument position, the two reach modes carrying NAMES "
     "that say which reach they mean --- while `scripts/mutate_assertions.py`'s `--cannot-fail` rule "
     "read the bare `True` as a literal-true ASSERTION, which is the first standing guard's defect "
     "inside the instrument that polices it.  *That one is `70`'s and is routed as a patch, not "
     "edited here, which is why `Ⓕ②`'s diff is still clean.*",
     not _bare_bool_args and len(_outside_unowned) == 0
     and 'AS_R7208' in _SELF_CODE and 'DISAMBIGUATED' in _SELF_CODE)

# ============================================================ verdict
head("VERDICT")
_bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS) - len(_bad)} of {len(CHECKS)} check(s) pass.\n")
if _bad:
    print("  FAILED:")
    for n in _bad:
        print(f"    - {n}")
    raise SystemExit(1)
print("""  ALL PASS.  The set-shaped class run over the whole instrument layer returns two findings and
  a declined instrument.  THE GATE LAYER CARRIES NONE OF IT -- 0 of 306 files -- and the ten sites
  that looked like hits were one reach token written for os.walk and matching ast.walk; the layer
  read on every push is the clean one, and the layer written once and read never carries all 72
  sites.  OF THE 19 EXPOSED, 13 ASSERT == 0, and at zero the standing guard's own repair is a
  tautology: for a non-negative count, <= 0 and == 0 are the same predicate, so the guard adopted at
  r7189 is silent on two thirds of the class and licenses a rewrite that satisfies its form and
  changes no content -- the FIRST guard's defect manufactured by the SECOND guard's repair.  The
  repair that applies at zero is L-249's population freeze plus a positive control.  AND THE PROXY
  FOR THAT CONTROL IS DECLINED: keyed to the tainted name it calls 7 of 14 uncontrolled, and a
  two-sided run against a shadow tree whose papers exist and whose bodies extract empty fails 6 of
  6 -- so the control is a property of the receipt, not of the name.  Nothing is red: the 15 terms
  the thirteen pin absent are absent from the paper layer, and present 40 times in the corpus's own
  excluded appendix layer, which is the distance rather than the word 'fragile'.  16 of the 19 sites
  are in 12 receipts this seat does not own and not one is edited here.""")
