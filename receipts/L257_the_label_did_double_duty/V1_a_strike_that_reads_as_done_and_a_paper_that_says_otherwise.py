#!/usr/bin/env python3
"""V1 -- five qualifications in three papers had no verdict in the open ledger, and reading the first
of them turned up a struck register clause whose LABEL contradicts, in terms, the paper it protects.

** ⛭ ⓵ WHAT WAS UNVERDICTED. **  `check_open_ledger` fails when a qualification appears in a paper
and nobody records a reading of it -- *"a grep is not a list of what is owed; it is a list of places
to look, and the looking has to be written down or it does not count."*  ⇒ Five stood open: three in
`P07`, one in `P10`, one in `P14`.

** ⛔⛭⛭ ⓶ AND THE FIRST OF THEM IS A CONTRADICTION IN TERMS WITH A STRUCK ROW. **

  * `P07`'s frontier item: *"only the ultraviolet definition of the mode sums remains open here ...
    ** the shared character of the wall does not settle it ** ... the latter is a genuine open
    frontier of the programme's quantum sector, carried as such and to be worked."*
  * `PO-6`, ** STRUCK r3001 **, clause ③: *"** THE UV DEFINITION: MET, NOT OWED ** -- generic to
    every interacting QFT."*

  ⇒ *** Read at face value the row says the shared character DOES settle it and the paper says it
      does not, about the same object, with the strike 582 revisions later than the sentence. ***

** ⌗ ⓷ AND IT IS NOT A DISAGREEMENT -- THE LABEL IS DOING DOUBLE DUTY, which is worse than a
disagreement because nothing marks it. **  `kills/PO-6.md`'s actual argument is that ** CR's SPECIFIC
part ** is bounded to a one-dimensional counterterm basis by conformal flatness -- *"a generic problem
on unusually good terms"*.  ⇒ *** So "NOT OWED" means ** CR adds no burden of its own **, not that the
generic construction exists.  On that reading the strike and the paper agree exactly, and `P10` says
the same thing in the same words: "the standard problem of the interacting theory rather than a
residual freedom in the quantization". ***
  ⇒ ** A THREE-CLAUSE ROW STRUCK AS A WHOLE CARRIES ONE VERDICT WORD PER CLAUSE, and a clause whose
    honest verdict is "not ours" reads, in the strike's grammar, as "done". **

** ⓸ THE OTHER FOUR, AND ONE OF THEM CARRIES ITS OWN LIMIT. **  `P10`'s straddle-as-a-computed-fact
is `NAMED-UNBUILT` -- *and the same sentence says what does not turn on it*: "how the straddle falls
does not bear on the closure below, which is supplied fibre by fibre".  ⇒ ** Both halves are recorded,
because an owed item that is not load-bearing and an owed item that is are different debts. **

WHAT IS NOT CLAIMED.  ** Not that `PO-6`'s strike is wrong ** -- the reconciliation is that it is
right and its clause label is ambiguous; nothing is unstruck.  ** Not that the papers were edited **
-- no `.tex` file is touched by this revision; what is written is the ledger reading.  ** Not that
the `P14` verdict is a reading of `P14` ** -- it rests on this line's own `PO-14` work at r3099, the
grounds are given in the entry, and it is marked so it can be overturned in one step.  ** And not
that the ledger's WARN backlog is addressed ** -- six entries name sentences no longer in any paper,
which `--rebuild` would re-derive, and rebuilding is not this revision's business.

    python3 receipts/L257_the_label_did_double_duty/V1_a_strike_that_reads_as_done_and_a_paper_that_says_otherwise.py

Written r3130, `L-257`.  Stated for reversal.
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
BEFORE = '74555e6d'          # r3128 -- before this revision's ledger entries
FIVE = {'114e4d9ede': ('CR_framework', 'NAMED-UNBUILT'),
        'dc0202b02d': ('CR_framework', 'NAMED-UNBUILT'),
        'fb2d798ceb': ('CR_framework', 'SELF-ANSWERED'),
        'f36eef9790': ('canonical_time', 'NAMED-UNBUILT'),
        '988eda39e1': ('matter_sector_paper', 'SCOPE-BY-DESIGN')}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def main():
    print()
    print('  V1 -- five unverdicted qualifications, and a label doing double duty')
    print()
    spec = importlib.util.spec_from_file_location(
        '_ol', os.path.join(ROOT, 'corpus', 'check_open_ledger.py'))
    ol = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    spec.loader.exec_module(ol)

    # ============================================================ (1) they were unverdicted
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ FIVE QUALIFICATIONS WITH NO RECORDED READING')
    print('  ' + '=' * 74)
    was = git('show', f'{BEFORE}:corpus/open_ledger.txt')
    check(f'⓵ at {BEFORE} none of the five was in the ledger: '
          f'{[k for k in FIVE if k not in was]}', all(k not in was for k in FIVE))
    # ** ⛭⛭⛭ RE-PINNED r3962, AND ALL FOUR OF THIS FILE'S REMAINING FAILURES ARE ONE DIAGNOSIS:
    # ** *** THE CORPUS ACTED ON WHAT THIS RECEIPT FOUND. ***  Two of the five opens were CLOSED --
    # ** `f36eef9790` at r3803 ("the straddle is a computed fact: build 3 of 3 closed") and
    # ** `dc0202b02d` at r3811 ("five stale sentences closed, including one in P07's ABSTRACT") --
    # ** so the gate's scan no longer raises them and there is no row to carry a verdict.  A third,
    # ** `114e4d9ede`, was RECLASSIFIED NAMED-UNBUILT -> REGISTERED at r3872 on the ledger's own
    # ** criterion, its home being `PO-23`.
    #   ⇒ ** A claim leaving the scan because the paper settled it is a STRONGER outcome than the
    #     verdict this file pinned, and pinning the verdict made the stronger outcome read as a
    #     failure. **  What is asserted now is the invariant: *each of the five has a recorded
    #     reading*, which is a live verdict OR a closure -- and WHICH, measured, for each.
    #   ⌗ This is the same class as `C19` and `L560/P1`, met a third time in one pass (r3962): a
    #     receipt that argues for a change and pins the unchanged state fails when it succeeds.
    cur = ol.scan()
    led = ol.read_ledger()
    # ⛭ ADDED r4548 -- ONE READER FOR A ROW, LIVE *OR* RETIRED, because three call sites below
    #   each assumed liveness and one of them said so by CRASHING.  ** Retirement in this ledger
    #   COMMENTS THE LINE OUT under `ORPHANED BY A REWORDING`; it does not delete it, exactly so
    #   the verdict and its note survive the rewording. **  ⇒ *A reworded row still has a recorded
    #   reading, and every claim this file makes is about the reading, not about which block of
    #   the file the line sits in.*
    _ORPH = {}
    for _l in open(os.path.join(ROOT, 'corpus', 'open_ledger.txt'), encoding='utf-8'):
        _m = re.match(r'#\s*([0-9a-f]{10})\s*\|', _l)
        if _m and _l.count('|') >= 3:
            _p = [x.strip() for x in _l.lstrip('# ').split('|', 3)]
            _ORPH.setdefault(_p[0], (_p[1], _p[2], _p[3]))

    def row(k):
        """(verdict, note, 'live'|'retired') for a ledger row -- (None, None, None) if absent."""
        for i, v in led.items():
            if i.startswith(k):
                return v[1], v[2], 'live'
        if k in _ORPH:
            return _ORPH[k][1], _ORPH[k][2], 'retired'
        return None, None, None

    got = {k: next((v[1] for i, v in led.items() if i.startswith(k)), None) for k in FIVE}
    scanned = {k: any(i.startswith(k) for i in cur) for k in FIVE}
    # ⛭ r4548: `not scanned` used to mean one thing and now means two, and the difference is the
    #   whole of this revision.  A claim can leave the papers' scan by being ** WITHDRAWN ** (no
    #   row anywhere) or by being ** REWORDED ** (row retired, verdict intact, object re-raised
    #   under a new id).  Collapsing them read a rewording as a closure.
    gone = sorted(k for k in FIVE if not scanned[k])
    closed = [k for k in gone if row(k)[2] is None]
    reworded = [k for k in gone if row(k)[2] == 'retired']
    check(f'⓵ᵇ each of the five is EITHER still a qualification the papers hold, by the gate\'s own '
          f'scan, OR closed since -- and none is half in: {scanned}',
          all(scanned[k] == (got[k] is not None) for k in FIVE))
    # ⌗ the VALUES are not this file's thesis and pinning all three is what broke the old check --
    #   a verdict is a reviewed judgement and may be revised, as `114e4d9ede`'s was at r3872.  What
    #   is asserted is that each has one and none is UNVERDICTED; and then, separately and by name,
    #   the ONE row this file's argument turns on.
    check(f'⓵ᶜ the three the papers still hold each carry a recorded verdict and none is blank: '
          f'{ {k: got[k] for k in FIVE if scanned[k]} }',
          all(got[k] and got[k] != 'UNVERDICTED' for k in FIVE if scanned[k]))
    check('⓵ᶜᐟ ⛭ and the row this file is ABOUT -- P07\'s "only the ultraviolet definition of the '
          'mode sums remains open here" -- reads REGISTERED, reclassified from NAMED-UNBUILT at '
          'r3872 because it has a home, and the home is PO-23',
          row('114e4d9ede')[0] == 'REGISTERED' and 'PO-23' in (row('114e4d9ede')[1] or ''))
    # ⛔⛭ r4548 -- AND THE ROW WAS RETIRED AT THIS REVISION, WITH ITS OWN SENTENCE UNTOUCHED.
    #   `r4525` rewrote the sentence AFTER it.  `check_open_ledger.scan()` cuts a claim at the
    #   next `'. '` -- a period followed by a SPACE -- and this row's sentence ends
    #   `...remains open here.}}`, a period followed by BRACES.  So the hashed 120 characters ran
    #   ON into the next sentence: `'...remains open here.}} This is t'`.  ** Rewording the
    #   FOLLOWING sentence moved THIS row's id. **
    #   ⇒ *The object did not go anywhere: it is raised again as `38005b708a`, live and REGISTERED
    #     at PO-23, and the r4525 note on that row restates it.*  What is checked is the
    #     conservation -- exactly one of the pair is live, and it is the one the papers raise.
    # ** r6931+70.1: LEFT RED, class (d) -- the finding holds and the REGISTER is what moved. **
    #    `4a453403` (r6819 follow-up, "open ledger ... carried with the correction") rewrote
    #    `corpus/open_ledger.txt` and 15 re-emitted live rows lost their `##` notes -- among them
    #    `38005b708a`, whose note read "OPEN and carried at PO-23, restated r4525 ... SUCCEEDS
    #    114e4d9ede".  The row still reads REGISTERED, but REGISTERED means "carried by a register row"
    #    and the row no longer names one.  PO-23 is still live (THE_OPEN_PROBLEMS_LEDGER family 8).
    #    Routed to node 66: restore the note.  Not loosened here.
    # ** ⛭⛭⛭ RE-POINTED r7083 (66), AND THE REASON IS THIS FILE'S OWN DIAGNOSIS TURNED ON ITSELF. **
    #    This check asserted that one of the pair is LIVE and reads REGISTERED naming `PO-23`.  At
    #    `r7077` `PO-23` was STRUCK -- its object, the ultraviolet definition of the mode sums,
    #    delivered at `r7064` and costed at `r7074` -- and `38005b708a` was retired with `P07`'s
    #    qualification when the item it recorded was discharged.  ** So the check went red because the
    #    object it was guarding was FINISHED, which is the symptom-pinning class this line has now met
    #    four times. **  Line 220 below already names the hazard -- "re-pinning only the old wording
    #    would have asserted the defect as though it were still live" -- and this check committed the
    #    same error on the other axis: it asserted the object's OPENNESS where the finding was only
    #    ever its CONSERVATION.
    #   ⇒ *** What the finding was: the r4525 rewording did not LOSE the object.  That is checked by
    #     conservation and not by liveness -- every member of the pair is accounted for, either live
    #     and naming a register row, or retired with a recorded reason. ***  A row that is neither is
    #     the defect this file exists to catch, and it is the only state that should fail here.
    _PAIR = ('114e4d9ede', '38005b708a')
    _acct = {k: row(k) for k in _PAIR}
    print(f'    ⌗ REPORTED, never required: the pair\'s states are '
          f'{ {k: (v[0], v[2]) for k, v in _acct.items()} } -- `PO-23` was struck at r7077 and '
          f'`38005b708a` retired with `P07`\'s qualification at the same revision')
    check('⓵ᶜᐢ ⛭ and no rewording LOST the object -- every member of '
          f'{_PAIR} is accounted for, each either LIVE and naming a register row or RETIRED with a '
          'reason recorded beside it, so the r4525 move was a rewording and the r7077 move a '
          'discharge, and neither was a withdrawal',
          all((v[2] == 'live' and v[1] and 'PO-' in v[1])
              or (v[2] == 'retired' and v[1] and len(v[1].strip()) > 40)
              for v in _acct.values()))
    # ⌗ r7441+cc66: this check is a CONJUNCTION of three and its label named only the first, so a
    #   red here said "two were closed" and left the reader to find which half had moved.  The three
    #   are reported separately now, for the same reason `r7439`'s tally prints a running total:
    #   *the place a conjunction goes false should be visible without re-deriving it.*
    print(f'    ⌗ REPORTED, never required: closed={closed}; reworded={reworded}; '
          f'rows surviving the closed pair={ {k: row(k) for k in closed} }')
    check(f'⛭ and the other {len(closed)} were CLOSED rather than left unread -- {closed} -- so the '
          f'scan no longer raises them at all AND no row survives them anywhere: r3803 computed '
          f'the straddle and r3811 closed five stale sentences, both AFTER this file named them; '
          f'while {reworded} left the scan a THIRD way, by being reworded, its row retired with '
          f'its verdict and note intact',
          # ⬭ r7441+cc66, on 66's `r7441` ⑥ -- the OTHER two failures, which 66 left undiagnosed.
          #   ** THIS ONE IS A MAINTENANCE COST AND NOT A FINDING, and the distinction is `r7441`'s
          #   own: a pin breaks because the text moved or because the claim did. **  *`fb2d798ceb`
          #   left the papers' scan the SAME legitimate way `114e4d9ede` did -- reworded, its row
          #   retired into the ledger's orphan block with its `SELF-ANSWERED` verdict and its note
          #   intact (`corpus/open_ledger.txt`).  Nothing was withdrawn and nothing was lost.*
          #   ⇒ *** The defect is that this conjunct pinned the LIST and the check's subject is the
          #     PROPERTY.  Rewording is a recurring, legitimate event; its identity on any given day
          #     is an accident of timing, and freezing it made a correct corpus turn this red. ***
          #   ⌗ `closed` is deliberately STILL pinned by identity, and that is not an inconsistency:
          #     its content is that THOSE TWO closures are evidenced (`r3803` computed the straddle,
          #     `r3811` closed five stale sentences, both after this file named them).  A closure
          #     asserted by property alone would pass a silent WITHDRAWAL, which is the one thing
          #     this check exists to tell apart.  ** The list stays where the evidence is specific
          #     and the property replaces it where the event recurs. **
          closed == ['dc0202b02d', 'f36eef9790']
          and all(row(k) == (None, None, None) for k in closed)
          and '114e4d9ede' in reworded
          and all(row(k)[2] == 'retired' and row(k)[0]
                  and row(k)[1] and len(row(k)[1].strip()) > 40 for k in reworded))
    # ** r6931+70.1: LEFT RED, class (d). **  The same `4a453403` added FOUR rows as UNVERDICTED --
    #    0cea1492c1 (P07), f7cc119e8a, c1ff64096b, 8b92369a04 (P18) -- "the only bucket that means
    #    work".  They are real unread qualifications; they leave by being read, not by this check
    #    being relaxed.  Routed to node 66.
    unv = [k for k, v in led.items() if v[1] == 'UNVERDICTED']
    check(f'⓵ᵈ and nothing is left UNVERDICTED: {len(unv)}', unv == [])

    # ============================================================ (2) the contradiction in terms
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ THE STRUCK CLAUSE AND THE PAPER, READ SIDE BY SIDE')
    print('  ' + '=' * 74)
    p7 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'),
              encoding='utf-8', errors='replace').read()
    prot = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8').read()
    kill = open(os.path.join(ROOT, 'kills', 'PO-6.md'), encoding='utf-8', errors='replace').read()
    # ** r6931+70.1: RE-PINNED, class (c) STALE -- reworded, same claim. **  `440623b6` (r6719, the
    #    cowork read worked across eleven papers) rewrote the tail of P07's sentence from "the latter
    #    is a genuine open frontier of the programme's quantum sector, carried as such and to be
    #    worked" to "the latter is the open item of the programme's quantum sector".  *The claim this
    #    check needs is unchanged: P07 still says the shared wall does not settle it and still carries
    #    the UV definition as OPEN in its quantum sector* -- which is the half that makes the strike's
    #    "MET, NOT OWED" read as a label doing double duty.  Both clauses are pinned in ONE sentence so
    #    the openness cannot be satisfied by an unrelated "open item" elsewhere in the paper.
    # ** ⛭⛭⛭ RE-POINTED r7083 (66) -- AND THIS IS THE CHECK THAT WENT RED BECAUSE ITS FINDING WON. **
    #    It pinned `P07`'s sentence verbatim: "the latter is the open item of the programme's quantum
    #    sector".  At `r7077` that item was SETTLED and the sentence rewritten, so a check asserting
    #    the paper's openness fails exactly when the paper stops being open.  ** That is the mirror of
    #    the mistake line 220 warns against, committed in this very function. **
    #   ⇒ *** AND THE FINDING SURVIVES THE SETTLEMENT, SHARPER THAN IT WAS. ***  This file's argument
    #     is that `PO-6`'s clause ③ -- "THE UV DEFINITION: MET, NOT OWED --- generic to every
    #     interacting QFT" -- was a label doing double duty.  The item is now settled, so the clause's
    #     VERDICT reads right; *** but it is not settled on the clause's GROUNDS. ***  `PO-6` said the
    #     item was met because the wall is generic; the corpus settled it by computing the
    #     construction's OWN regulator to an exact value and costing its counterterm.  ** A label that
    #     reaches the right verdict by an argument the corpus then declined to use is still a label
    #     doing double duty, and the register must not retroactively adopt it. **
    #   ⌗ So what is asserted is the thing that stays true either way: `P07` states the item's standing
    #     in its own voice rather than resting on the shared character of the wall, and the register
    #     keeps clause ③ marked SUPERSEDED rather than vindicated.  ⓶ᵇ below carries that second half
    #     and is unchanged.
    _p7f = re.sub(r'\s+', ' ', p7)
    _shared = 'the shared character of the wall' in _p7f
    # ⬭⬭ r7355+cc66, the TWO P5 ROWS were repaired onto one span -- `r7285+69`'s own prescription
    #   taken verbatim, with the pronoun's antecedent brought inside it and two co-occurring
    #   fragments of one `P5` passage retired on one span.  ** That repair was right and it is kept
    #   below as the HISTORICAL pin; what follows is why it could not stay the only pin. **
    #
    # ⬭⬭⬭ r7441+cc66, ON 66's `r7441` ⑤ ⑥ -- AND IT IS NOT A RELAXATION OF THE ASSERTION.
    # ** `P07` DID NOT REWORD.  IT WITHDREW A SETTLEMENT, AND THE REGISTER MOVED WITH IT. **
    #   *This check pinned "all three are settled, the ultraviolet definition of the mode sums with
    #   them".  `r7401` (`557b94da3`) removed that span and put the opposite of its load-bearing half
    #   in its place: "So two of the three items named above are settled, and the third is not: a
    #   definition of the mode sums is delivered, and its completion stands open."*
    #   ⇒ *** So the pin did not break because the TEXT moved.  It broke because the CLAIM moved --
    #     the first is a maintenance cost, the second is a finding, and the red was the system
    #     working.  It held a red open on `main` for five lines and that is the cost of reading it
    #     as the former. ***
    #   ⌗ RE-DERIVED HERE, not restated from the ruling -- `r7441` ①'s own rule, that a number a
    #     seat measures is a measurement and a number restated in a ruling belongs to whoever
    #     restated it.  Measured on both sides: of the two spans the old conjunction required, the
    #     regulator clause still stands ONCE and the `all three are settled` span stands ZERO times,
    #     while `of the three items named above` and `ultraviolet definition of the mode sums` each
    #     still occur once -- so the SENTENCE survived and its VERDICT changed.
    #   ⇒ ** THE SHAPE OF THE FIX IS `L-249`'s, and it is what `r7439` found six of `60`'s seven
    #     candidates already doing: pin what the paper SAID AT THE COMMIT IT SAID IT, and assert the
    #     CURRENT state separately. **  *Three checks where there was one, because there are three
    #     facts: a historical claim this file's argument rests on, a live claim it must not
    #     contradict, and a register that moved with the paper rather than against it.  Relaxing the
    #     assertion would have thrown the finding away.*
    _WAS = '15c6a1d9b'          # `r7401`'s parent: the last commit at which `P07` still said it
    _P5 = ('So of the three items named above, all three are settled, the ultraviolet definition '
           'of the mode sums with them')
    _REG = "s, and the definition is the construction's own"
    _NOW = ('So two of the three items named above are settled, and the third is not: a definition '
            'of the mode sums is delivered, and its')
    # ⌗ `\emph{completion}` sits inside the sentence, so the span stops before the markup rather
    #   than carrying it -- the same reason the other pins in this file read a flattened body.
    _p7_was = re.sub(r'\s+', ' ', git('show', f'{_WAS}:corpus/CR_framework.tex'))
    _said_then = _P5 in _p7_was and _REG in _p7_was
    # ⛭⛭ r7441+cc66, SECOND PASS -- AND THE DEFECT WAS MINE AND IT WAS THIS FILE'S OWN SUBJECT.
    #   *My first pass asserted the paper's NEW sentence and three ledger/register sentences, and
    #   `check_quote_pins` named SIX new quote-pin keys for it.*  ** A repair of a pin that broke when
    #   another seat reworded, which creates four more pins on other seats' wording, has learned
    #   nothing. **  The gate's own address says which way out: *"If the claim is the sentence's
    #   MEANING, assert what the sentence is for ... if the wording itself is the claim, say so in the
    #   baseline as DELIBERATE."*
    #   ⇒ *** The WITHDRAWAL needs no live quote at all.  It is established by the span being PRESENT
    #     at `_WAS` (a fixed commit, which no rewording can touch) and ABSENT now -- a presence and an
    #     absence, and an absence pins nothing. ***  The paper's new wording is REPORTED instead, in
    #     this file's own idiom, where it illustrates the finding without asserting it.
    #   ⌗ Verified rather than assumed: this file's existing `_shared` literal is reported and never
    #     asserted, and it carries NO baseline row -- so a reported literal is not swept as a pin.
    _withdrawn = _P5 not in _p7f
    _reg_voice = _REG in _p7f
    _led = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_OPEN_PROBLEMS_LEDGER.md'),
                                    encoding='utf-8', errors='replace').read())
    _regs = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_REGISTER.md'),
                                     encoding='utf-8', errors='replace').read())
    # ⌗ ONE pin, not four, and it is the one where the wording IS the claim: the ledger's own verdict
    #   sentence on `PO-23`.  If the ledger rewords THAT, this seat wants to know.  The rest is a
    #   STRUCTURAL absence (`PO-89` is not struck -- an absence pins nothing) plus reported context.
    _moved = ("`PO-23`'s strike is upheld" in _led
              and '~~**PO-89**~~' not in _regs)
    _ctx = ('the definition and its completion are two objects' in _led,
            '| **PO-89** |' in _regs,
            "THE COMPLETION OF THE INTERACTING TOWER'S DEFINITION" in _regs)
    print(f'    ⌗ REPORTED, never required: P07 still argues from the shared wall: {_shared}; '
          f'P07 names the construction\'s own regulator: {_reg_voice}')
    print(f'    ⌗ REPORTED, never required -- the paper\'s CURRENT wording, illustrating the '
          f'withdrawal rather than asserting it: {_NOW in _p7f and "stands open." in _p7f}; '
          f'and the register context (two objects, PO-89 row present, its title): {_ctx}')
    check(f'⓶ ⛭ AT {_WAS} -- the commit before `r7401` -- `P07` DID state the UV definition settled, '
          'in its own voice and on the construction\'s own regulator rather than on the wall being '
          'shared: "all three are settled, the ultraviolet definition of the mode sums with them".  '
          '** That is the historical claim this file\'s argument rests on, and it is pinned AT ITS '
          'COMMIT so no later edit to the paper can take it away -- which is exactly what a later '
          'edit then did **',
          _said_then)
    check(f'⓶ᵃ ⛔ AND `P07` HAS SINCE WITHDRAWN THAT SETTLEMENT, which is a different thing from '
          f'rewording it: the span present at {_WAS} is ABSENT from the paper now.  ** Asserted as '
          'an ABSENCE against a presence pinned at a commit, so this check cannot itself break on a '
          'rewording -- which is the failure it was written to repair.  What the paper says INSTEAD '
          'is reported above and deliberately not asserted **',
          _withdrawn)
    check('⓶ᵃᐟ ⚖ and the REGISTER MOVED WITH THE PAPER rather than against it, which is what makes '
          'this a withdrawal and not a drift: the ledger states in its own verdict that `PO-23`\'s '
          'strike is UPHELD for the definition that was delivered, and `PO-89` -- the row carrying '
          'the completion -- is NOT struck.  ** Paper, ledger and register all current and all '
          'agreeing; the receipt was the one layer that had not moved **',
          _moved)
    po6 = [l for l in prot.split('\n') if re.match(r'\|\s*~*\*\*PO-6\*\*', l)]
    # ** ⛭⛭⛭ AND HERE IS THE FINDING BEING ACTED ON, IN THE REGISTER ITSELF (re-pinned r3962). **
    # ** This file's whole argument is that clause ③ read "THE UV DEFINITION: MET, NOT OWED" while
    # ** P07 carried the item as a live frontier -- a label doing double duty.  *** r3809 SUPERSEDED
    # ** the clause and opened `PO-23`, and the register now demotes the old reading to past tense:
    # ** "⛔ THIS CLAUSE IS SUPERSEDED -- see PO-23, opened r3809.  *It read MET, NOT OWED*". ***
    #   ⇒ ** Both ends are pinned: the strike stands, and the clause that made it ambiguous no longer
    #     does.  Re-pinning only the old wording would have asserted the defect as though it were
    #     still live -- which is the mirror of the mistake this file was written to catch. **
    check('⓶ᵇ ⛔ PO-6 is STRUCK, and clause ③ is now marked SUPERSEDED with the item rehomed to '
          'PO-23 (r3809) -- the "MET, NOT OWED" reading this file flagged is stated in the PAST '
          'tense, as a reading the row once carried',
          len(po6) == 1 and po6[0].lstrip('| ').startswith('~~')
          and 'THIS CLAUSE IS SUPERSEDED' in po6[0] and 'PO-23, opened r3809' in po6[0]
          and '*It read MET, NOT OWED*' in po6[0]
          and 'THE UV DEFINITION: **MET, NOT OWED**' not in po6[0])
    # ** the ORDER matters: the strike is the later statement, so it is not superseded prose **
    sent = git('log', '-S', 'the shared character of the wall does not settle it', '--format=%h',
               '--', 'corpus/CR_framework.tex').split()
    strike = git('log', '-S', 'THE UV DEFINITION: **MET, NOT OWED**', '--format=%h',
                 '--', 'PROTECTED_OPEN.md').split()
    later = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor',
                            sent[-1], strike[-1]], capture_output=True).returncode == 0
    check(f'⓶ᶜ and the STRIKE is the later statement ({strike[-1]} after {sent[-1]}), so this is '
          'not old prose left behind a newer verdict -- the newer one is the ambiguous one', later)

    # ============================================================ (3) the reconciliation
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ AND IT IS A LABEL DOING DOUBLE DUTY, NOT A DISAGREEMENT')
    print('  ' + '=' * 74)
    check('⓷ the kill file\'s ARGUMENT is about CR\'s SPECIFIC part -- a counterterm basis "one-'
          'dimensional by conformal flatness" -- and calls the result "a generic problem on '
          'unusually good terms", which is "not ours", not "done"',
          'one-dimensional by conformal flatness' in kill
          and 'A generic problem on unusually good terms' in kill)
    p10 = open(os.path.join(ROOT, 'corpus', 'canonical_time.tex'),
               encoding='utf-8', errors='replace').read()
    # ** ⛭ RE-PINNED r3962 (moved prose).  P10 said "the standard problem of the interacting theory
    # ** rather than a residual freedom in the quantization"; it now makes the SAME distinction in
    # ** other words, and the distinction is the whole of what this check is for. **
    check('⓷ᵇ and P10 draws the same distinction in its own voice -- what remains open is "the '
          'ultraviolet definition of the tower sums---a different thing from a residual freedom in '
          'the quantization at the boundary, and not settled by being shared with every interacting '
          'field theory" -- so the two papers agree and it is the ROW\'s one-word label that reads '
          'otherwise',
          # ⬭⬭ r7355+cc66, REPAIR of the OTHER CO-OCCURRENCE pair, and again 69's prescription
          #   ("the one sentence from `What remains genuinely open`") taken after measuring it.
          #   Both fragments came out of ONE P10 sentence: the first is a noun phrase clipped
          #   from "What remains genuinely open is accordingly the ...", its subject outside it;
          #   the second is a bare participle ("not settled by being shared with ...").  Pinned
          #   apart, the paper could carry them in unrelated places and the check would pass.
          #   ⌗ Verified before adopting: the whole sentence stands ONCE in the flattened
          #     `canonical_time.tex` and once under `_unmark`.
          'What remains genuinely open is accordingly the ultraviolet definition of the tower '
          'sums---a different thing from a residual freedom in the quantization at the boundary, '
          'and not settled by being shared with every interacting field theory'
          in re.sub(r'\s+', ' ', p10))
    # ⛔⛭ AMENDED r4548, AND IT *** CRASHED *** RATHER THAN FAILING -- the third receipt in this
    #    line's work with a bare `next(...)`/`led[id]` over the ledger and no default.  ** r4525
    #    corrected the sentence FOLLOWING this row's claim, which moved the row's hash, so the row
    #    left the live set and this line raised StopIteration before the verdict. **
    #    ⇒ *The claim here is that THE RECONCILIATION IS WRITTEN INTO THE LEDGER ENTRY -- not that
    #      the row is live.*  A retired row keeps its note, by design: retirement comments the line
    #      out, it does not delete it.  So the entry is looked for in the live rows AND in the
    #      retired block, and its ABSENCE fails here with a reason instead of a traceback.
    _ENTRY_ID = '114e4d9ede'
    entry, _where = (row(_ENTRY_ID)[1] or ''), row(_ENTRY_ID)[2]
    if _where != 'live':
        print(f'    ⌗ {_ENTRY_ID} is {_where.upper() if _where else "ABSENT"}, not live -- read '
              f'from the ledger\'s orphan block, where retirement preserves the row and its note '
              f'rather than deleting them ({len(entry)} characters)')
    check(f'⓷ᶜ⁰ the {_ENTRY_ID} entry is READABLE at all, live or retired -- so what follows is a '
          f'statement about its text and not about an empty string', len(entry) > 200)
    # ** ⛭ RE-PINNED r3962, AND THE OLD NOTE WAS RETIRED FOR BEING STALE -- BY NAME, IN THIS ROW. **
    # ** The entry used to reconcile via PO-6's clause ③ warrant ("MET, NOT OWED" / "CR ADDS NO
    # ** BURDEN OF ITS OWN").  r3871 marked that warrant SUPERSEDED and r3872 rewrote the note, which
    # ** says so in terms: *"the strike and this sentence agree", but `kills/PO-6.md` marks that
    # ** warrant SUPERSEDED r3871 ... the live row is PO-23*.
    #   ⇒ ** The reconciliation is still written into the ledger, which is what this check is for --
    #     it is written against the LIVE row instead of the retired warrant. **  Pinning the old
    #     warrant's words would have re-certified the very reconciliation the corpus withdrew.
    check('⓷ᶜ and the reconciliation is written into the ledger entry rather than left to be '
          'rediscovered -- now against the LIVE row PO-23, the entry recording that PO-6\'s clause '
          '③ warrant was superseded at r3871 and naming what replaced it',
          'PO-23' in entry and 'SUPERSEDED r3871' in entry
          and 'the live row is PO-23' in entry)
    check('⓷ᵈ ⌗ and nothing is unstruck: PO-6 stays struck, because the reconciliation is that the '
          'strike is RIGHT',
          po6[0].lstrip('| ').startswith('~~'))

    # ============================================================ (4) the owed-but-not-load-bearing
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⌗ AN OWED ITEM THAT IS NOT LOAD-BEARING IS A DIFFERENT DEBT')
    print('  ' + '=' * 74)
    # ** ⛭⛭⛭ AND THIS ONE IS NOT A RE-PIN, BECAUSE THE ITEM IS NO LONGER OWED (r3962). **  This check
    # ** read that P10 "names the straddle-as-a-computed-fact as OPEN".  *** P10 now COMPUTES it: ***
    # ** "The straddle itself is now a computed fact\rcpt{P10_the_straddle_is_computed}: the spectrum
    # ** does occupy both sides of $\tfrac34$" -- $\operatorname{spec}\hat\Gamma=[\gamma,\infty)$ with
    # ** $\gamma\le\tfrac14<\tfrac34$ below and unboundedness above.
    #   ⇒ ** Re-pinning would have preserved a sentence that says the opposite of the paper. **  The
    #     debt-shaped half is REPLACED by the discharge; the load-bearing half -- that the closure does
    #     not turn on it -- is unchanged and still pinned, and it is the half PART 4 is actually about.
    #     *An owed item that is not load-bearing is a different debt; an item that has been PAID and is
    #     not load-bearing is not a debt at all, and the section keeps its point either way.*
    _p10 = re.sub(r'\s+', ' ', p10)
    # ** r6931+70.1: RE-PINNED, class (b) DISCHARGED -- and pointed at WHAT discharged it. **
    #    `440623b6` (r6719) dropped the word "now" from "The straddle itself is now a computed fact"
    #    -- a paper presents one state, so the sentence no longer narrates its own change.  The
    #    discharge is untouched: the sentence still cites `\rcpt{P10_the_straddle_is_computed}` and
    #    still carries the computation (spec Gamma-hat = [gamma, infinity) with gamma <= 1/4 < 3/4).
    #    ⇒ So the pin follows the discharge rather than the adverb: the sentence, its receipt citation,
    #      the receipt FILE existing where it is cited, and the spectrum statement that is the
    #      computation itself.  The old open wording must still be absent.
    _straddle_rcpt = os.path.join(ROOT, 'receipts', 'P10_canonical_time',
                                  'P10_the_straddle_is_computed.py')
    check('⓸ P10 has since SETTLED the straddle -- "The straddle itself is a computed fact", citing '
          '`P10_the_straddle_is_computed` (which exists), with spec Gamma-hat = [gamma, inf) and '
          'gamma <= 1/4 < 3/4 -- so the item PART 4 carried as owed-but-not-load-bearing is paid',
          'The straddle itself is a computed fact\\rcpt{P10_the_straddle_is_computed}' in _p10
          and os.path.exists(_straddle_rcpt)
          and 's occupy both sides of $\\tfrac34$, since $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$ with $c>0$ has $\\operatorname{spec}\\hat\\Gamma=[\\gamma,\\infty)' in _p10
          and '$\\gamma\\le\\tfrac14<\\tfrac34$ places spectrum strictly below the threshold' in _p10
          and 'not the floor but the straddle itself as a computed fact' not in _p10)
    check('⓸ᵃ ⌗ and the half this section turns on is untouched: the closure "is supplied fibre by '
          'fibre and so cannot be broken by the size of the sub-threshold set" -- which is why the '
          'reading held while the item was open and holds now that it is closed',
          # ⬭⬭ r7355+cc66, REPAIR of the DANGLING span (69's ⓵ and ⓷): it reads as a complete
          #   proposition and opens on a predicate, its subject -- "the closure below, which is"
          #   -- sitting outside it.  *** That is the case the subject rule exists for: a span
          #   that reads complete is the one a reader will not re-check. ***  69's prescribed
          #   widening names the subject and is taken verbatim.
          #   ⌗ Verified before adopting: ONCE in the flattened `canonical_time.tex`, once under
          #     `_unmark`.  The widening adds no new document and no new claim -- the same
          #     sentence, read from its subject.
          'How the straddle falls does not bear on the closure below, which is supplied fibre by '
          'fibre and so cannot be broken by the size of the sub-threshold set'
          in _p10)
    # ** ⛔ AND THIS ONE DID NOT FAIL, IT CRASHED (repaired r3962). **  `next(...)` with no default
    # ** raised `StopIteration` when the `f36eef9790` row left the ledger at r3803 -- so PART 5 never
    # ** ran and the file exited on a traceback instead of a verdict.  *** A lookup that assumes its
    # ** key still exists turns a closed item into a crash, and a crash reports nothing. ***  The
    # ** entry is gone because the OPEN is gone: the straddle is computed, ⓸ above measures it in
    # ** P10's own words, and there is no ledger row left to record two halves of a live debt.
    e = next((v[2] for i, v in led.items() if i.startswith('f36eef9790')), None)
    check('⓸ᵇ and the ledger no longer carries a row for it AT ALL -- r3803 closed the item, so the '
          'entry that recorded "not load-bearing" and "fibre by fibre" was retired with the open it '
          'described, which is the ledger working rather than the record being lost',
          e is None and not any(i.startswith('f36eef9790') for i in cur))
    e14 = next(v[2] for i, v in led.items() if i.startswith('988eda39e1'))
    check('⓸ᶜ ⚠ and the P14 entry says in itself that it is a LEDGER verdict on another line\'s '
          'paper, resting on this line\'s own PO-14 work, so it can be overturned in one step',
          'LEDGER VERDICT ON A' in e14 and 'PO-14' in e14)

    # ============================================================ (5) the gate
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- THE GATE, AND WHAT IS STILL OWED IN IT')
    print('  ' + '=' * 74)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'corpus', 'check_open_ledger.py')],
                       capture_output=True, text=True, errors='replace', timeout=600)
    check(f'⓹ check_open_ledger exits {r.returncode}', r.returncode == 0)
    # ** ⛭ RE-PINNED r3962: THE WARN BACKLOG WAS PAID. **  This read `warns >= 1` and said so in
    # ** terms -- "reported, not repaired ... not this revision's business".  Six entries named
    # ** sentences no longer in any paper; the gate now reports ZERO.  *** A check that requires a
    # ** backlog to still exist fails when the backlog is cleared, which is the direction nobody
    # ** writes a test for. ***  Asserted as a RATCHET in the corpus's own idiom: the count may fall
    # ** to zero and stay there, and it fails if the backlog GROWS past what this file recorded.
    # ** r6931+70.1: LEFT RED, class (d) -- exactly the case this check names. **  The one WARN is
    #    `8c089c7d7b` (open_ledger.txt, REGISTERED, "the depth is open"): P18 now states the depth as
    #    ESTABLISHED, the two transfers agreeing to three per cent (`4e82b053`, CR_synthesis.tex
    #    ~l.1463).  A paper moved out from under a ledger row; the row must be retired as answered.
    # ** ⛔ r7441+cc66: LEFT RED AGAIN, same class (d), and READ as 66's `r7441` ⑥ asked.  TWO WARNs,
    #    both `CR_cosmology`, and ** both are the MIRROR of this file's own `⓶` **: there the receipt
    #    claimed settled while the paper had withdrawn the settlement; here the LEDGER carries open
    #    what the paper has since SETTLED.  *Measured against the paper, not inferred:*
    #      `b2b0f5faef` | REGISTERED | pinned "What the kernel's exponent is, as against its length,
    #         is **not settled here**, and the gap is a factor and not a detail".  `CR_cosmology` now
    #         reads "...is a factor and not a detail, and it **is settled rather than left to the
    #         reader**: the kernel has one frequency slot".  ⇒ the paper CLOSED it.
    #      `63935975cb` | REGISTERED | pinned "Which of the two the segment's own field obeys
    #         **remains open**".  The paper now states it flat: "**The segment's own field is the
    #         substrate one**, and the ground is empirical rather than geometric".  ⇒ answered.
    #    ⌗ Both rows are 66's, opened `r7129` on node 70's audit and carried by `THE_REGISTER`
    #      `PO-77`, so retiring them as ANSWERED is a register verdict on another paper's open
    #      problem -- ** not this seat's to write **, and routed in `FOR_66.md` rather than taken.
    #    ⇒ *** So this stays RED, for the right reason and with the reason in the source: the check
    #      is working.  A WARN reappearing is exactly the signal it was built to give, and the
    #      remedy is a verdict, not an edit to this receipt. ***
    warns = r.stdout.count('[WARN]')
    #   ⌗ and the bound is the MEASURED value, not a slack one.  `min(warns, 6) == warns` would pass
    #     at anything up to six and so would notice nothing; ZERO is what the gate reports, so zero
    #     is what is asserted, and a single WARN returning is a finding worth stopping for.
    check(f'⓹ᵇ ⌗ {warns} WARN(s) remain -- entries naming sentences no longer in any paper.  This '
          f'file recorded SIX and routed them rather than rebuilding; the backlog is now PAID, and '
          f'a WARN reappearing means a paper moved out from under a ledger row again',
          warns == 0)
    # ** ⛔ AND THIS ONE COMPARED AGAINST `HEAD`, WHICH IS NOT WHAT IT MEANT (repaired r3962). **
    # ** "no .tex file is touched by THIS REVISION" is a claim about r3130's own diff.  Written as
    # ** `BEFORE..HEAD` it silently became a claim about *** every revision that would ever follow
    # ** ***, and the corpus has edited .tex files on hundreds of them since -- correctly.
    #   ⇒ ** A check pinned to `HEAD` is pinned to the present, and the present moves. **  That is
    #     the class `L259_the_distance_from_the_present/D1` is named for, met here in its purest
    #     form.  The range is now the revision's OWN, end to end, and it cannot drift again.
    AFTER = 'ae749cb6'          # r3130 -- this revision's own commit
    check(f'⓹ᶜ and no .tex file was touched by THIS revision ({BEFORE}..{AFTER}) -- the reading was '
          f'written in the ledger, not in the papers',
          not [f for f in git('diff', '--name-only', BEFORE, AFTER).split()
               if f.endswith('.tex') and not f.startswith('corpus/appendix_receipts')])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a three-clause row struck as a whole carries one verdict word per clause,')
    print('  and a clause whose honest verdict is "not ours" reads, in the strike\'s grammar, as')
    print('  "done". **  *`PO-6` ③ says "THE UV DEFINITION: MET, NOT OWED"; `P07` says the shared')
    print('  character of the wall does not settle it and carries the item as a frontier.*')
    print('  ⌗ ** They agree. **  The kill file\'s argument is that CR\'s SPECIFIC part is bounded to')
    print('     a one-dimensional counterterm basis -- "not ours", not "done" -- and `P10` says so')
    print('     in the same words.  *Nothing is unstruck; the reconciliation is written down.*')
    print('  ⛭ ** And an owed item that is not load-bearing is a different debt: ** the straddle is')
    print('     `NAMED-UNBUILT` and the paper says the closure below does not turn on it.  Both')
    print('     halves recorded, because recording one is how a debt gets mis-priced.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
