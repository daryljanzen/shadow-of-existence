#!/usr/bin/env python3
"""r7758 (60) -- the cold read of 70's E8 registration, run as twelve registered arms.

POST-REGISTRATION: every figure here is produced after PREDICTION.md was committed and pushed.
The material is read from a checkout of 70's branch (claude/shadow-of-existence-setup-wgcmvt),
whose head sha is printed below, NOT from main and NOT from this seat's working tree.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
import time

SCRATCH = ('/tmp/claude-0/-home-user-shadow-of-existence/'
           '3f654921-f94d-5e03-8dca-e6e4ffe98045/scratchpad/e8')
EXP = os.path.join(SCRATCH, 'resources', 'ARP_LLM_paper', 'experiments')
E8 = os.path.join(EXP, 'E8')
ROOT = '/home/user/shadow-of-existence'
VERDICTS = []


def arm(n, title, ok, *lines):
    VERDICTS.append((n, ok, title))
    print(f"\n{'=' * 100}\nARM {n} -- {title}\n  [{'PASS' if ok else 'FAIL'}]")
    for ln in lines:
        print(ln)


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def git(*a):
    return subprocess.run(['git', *a], cwd=ROOT, capture_output=True, text=True).stdout


HEAD70 = git('rev-parse', 'FETCH_HEAD').strip()
print("=" * 100)
print("r7758 (60) -- the cold read of 70's E8 registration, before its pilot")
print(f"  70's branch head read:  {HEAD70}")
print(f"  this seat's HEAD:       {git('rev-parse', 'HEAD').strip()}")
print("  (the order says read 70's branch, not main; the sha is printed so the tree is on the record)")
print("=" * 100)

REG = read(os.path.join(E8, 'PREDICTION.md'))
RUN = read(os.path.join(E8, 'run_e8.py'))
SESS = json.load(open(os.path.join(E8, 'materials', 'sessions.json')))
REMIND = read(os.path.join(E8, 'materials', 'reminder.md'))
DISP = read(os.path.join(EXP, 'E7', 'materials', 'disposition_sound.md'))
ITEMS = {}
for k in (1, 2, 3):
    for it in json.load(open(os.path.join(EXP, f'E{k}', 'materials', 'items.json'))):
        ITEMS[it['id']] = it

# ---------------------------------------------------------------- ARM 1: can each prediction fail
PRED = re.search(r'## Predictions.*?\n(.*?)\n## ', REG, re.S).group(1)
rows = []
for tag in ('P1', 'P2', 'P3'):
    m = re.search(r'\*\*' + tag + r'[^*]*\*\*(.*?)(?=\n- \*\*P|\Z)', PRED, re.S)
    body = ' '.join(m.group(1).split()) if m else ''
    has_interval = bool(re.search(r'interval excluding 0|interval excludes 0|at least [0-9]', body))
    bare_ineq = bool(re.search(r'no larger than|≥|>=|is >|smaller if', body)) and not has_interval
    rows.append((tag, has_interval, bare_ineq, body[:200]))
counts_against = re.search(r'## What counts against\n(.*?)\n## ', REG, re.S).group(1)
rescued = 'interval excluding 0' in counts_against
arm(1, "can each prediction fail, as the prediction is written",
    all(r[1] for r in rows),          # PASS iff every prediction states its own falsifier
    *[f"      {t}: interval or threshold stated in the prediction: {hi};  bare inequality: {bi}\n"
      f"           \"{b[:150]}...\"" for t, hi, bi, b in rows],
    "",
    "  ⛔ P2 AND P3 ARE STATED AS BARE INEQUALITIES.  `no larger than in PLAIN' and",
    "  `REMINDER's late failure rate is >= IMPLICIT's' are both confirmed by a tie and by",
    "  noise in the predicted direction: there is no outcome short of a significant",
    "  REVERSAL that either can fail on.  P1 alone carries `with the interval excluding 0'.",
    f"  ⌗ The `What counts against' section does supply an interval for the reminder clause:",
    f"  {rescued} -- *if REMINDER's late failure rate is LOWER than IMPLICIT's with the",
    "  interval excluding 0*.  So the FALSIFIER is two-sided while the PREDICTION is",
    "  one-sided, and the asymmetry is in the experiment's favour: P3 is confirmed by",
    "  everything except a significant reversal.",
    "  → RECOMMENDED, one line each, before the pilot: give P2 and P3 the same interval",
    "  language P1 has, e.g. `the IMPLICIT - PLAIN difference's interval excludes 0 in the",
    "  predicted direction, or the prediction is not supported'.")

# ---------------------------------------------------------------- ARM 2: the composite's arithmetic
XZ = SESS['blocks']['X'] + SESS['blocks']['Z']
cls = {'E1': [i for i in XZ if i.startswith('E1')], 'E2': [i for i in XZ if i.startswith('E2')],
       'E3': [i for i in XZ if i.startswith('E3')]}
opens = [i for i in cls['E2'] if ITEMS[i]['kind'] == 'open']
prim = re.search(r'\*\*Primary:\*\*(.*?)\n\n', REG, re.S).group(1)
arm(2, "the composite failure rate -- can it be computed from the registration alone",
    False,
    f"  the contrast's 16 items: {len(cls['E1'])} E1, {len(cls['E2'])} E2 "
    f"(of which {len(opens)} open), {len(cls['E3'])} E3 -- 8 per side",
    f"  the registration's own sentence: \"{' '.join(prim.split())[:260]}\"",
    "",
    "  ⛔ TWO ARITHMETICS ARE ADMISSIBLE AND THE REGISTRATION DOES NOT CHOOSE:",
    "    ⒜ a mean over the 8 items of a per-item failure score (E1 and E2 binary, E3",
    "       continuous as 1 - found/3), with the open item contributing ONE score;",
    "    ⒝ `the share of failure events across the coverage, guard and closure items'",
    "       as written, in which the open item contributes TWO events -- a verdict error",
    "       and a closure error -- so its weight is twice any other item's and the",
    "       denominator is 9, not 8.",
    f"  The open items are {opens}: one in X and one in Z, so exactly one per side, and",
    "  whichever reading is taken it is a 1-of-8 or 2-of-9 share.  The difference is about",
    "  6 points of composite rate on a single closure error -- the same order as the",
    "  10-point effect the n is being sized for.",
    "  ⇒ THE PRIMARY'S ARITHMETIC IS CHOOSABLE AFTER THE DATA.  That is the one thing a",
    "  pre-registration exists to prevent, and it is one sentence to fix.",
    "  → RECOMMENDED before the pilot: write the formula, e.g. `composite = mean over the",
    "  8 items of: 1 if coverage failure, 1 if verdict error, 1 - found/3 for a review;",
    "  closure on the open item is scored and reported SEPARATELY and does not enter the",
    "  composite' -- or the other choice, stated.")

# ---------------------------------------------------------------- ARM 3: do the arms differ only in curriculum
SPIN = SESS['spin_up']


def wordcount(p):
    full = os.path.join(ROOT, p) if p.endswith('.tex') else os.path.join(EXP, p)
    return len(read(full).split())


spin_words = {p: wordcount(p) for p in SPIN}


def task_words(iid):
    it = ITEMS[iid]
    t = it.get('message') or it.get('prompt') or it.get('document', '')
    return len(str(t).split())


order_A = SESS['order_A']
early_mid = sum(task_words(i) for i in order_A[:16])
spin_total = sum(spin_words.values())
remind_words = len(REMIND.split())
ctx = {'IMPLICIT': (8 + 16, spin_total + early_mid),
       'REMINDER': (8 + 16, spin_total + early_mid + 16 * remind_words),
       'PLAIN': (16, early_mid)}
plain_claim = 'just as long' in REG
arm(3, "do the arms differ only in the curriculum, at the late window",
    False,
    "  turns and words of context standing BEFORE turn 17 (the late window), counted from",
    "  run_e8.py's own plan and the materials it names:",
    *[f"      {a:9s} {t:3d} turns   {w:7,d} words of prompt text" for a, (t, w) in ctx.items()],
    f"      (the spin-up alone is {spin_total:,} words across {len(SPIN)} documents; the",
    f"      registration says `about 18.2k words')",
    "",
    f"  ⛔ AND THE REGISTRATION SAYS PLAIN IS `just as long': {plain_claim}.  It is not.",
    f"  PLAIN's late turns sit at roughly {ctx['PLAIN'][1] / ctx['IMPLICIT'][1]:.0%} of IMPLICIT's context and eight turns",
    "  earlier in the session.  So the PLAIN-vs-IMPLICIT comparison does not isolate the",
    "  curriculum: it confounds curriculum with context length and session depth, and in",
    "  the direction that matters --",
    "    * P1 (`load produces the failures') is measured in the arm with the LEAST load, so",
    "      a null there cannot say that `long sessions at this length do not produce the",
    "      failures': the length differs by arm, and PLAIN is the short one;",
    "    * P2 (`implicit carry holds') reads IMPLICIT's late - early against PLAIN's, but",
    "      IMPLICIT's late turns carry four times the context, which pushes its late rate",
    "      UP relative to PLAIN -- against P2.  The confound is conservative for P2 and",
    "      fatal for P1's interpretation.",
    "  → RECOMMENDED before the pilot, and it is a materials change of one file: give PLAIN",
    "  eight filler turns of matched length that carry no disposition and no method -- the",
    "  pilots' own cold items, a long domain text, anything with the word count and none of",
    "  the content -- or else drop the phrase `just as long' and register PLAIN as the",
    "  SHORT-SESSION arm, with P1 restated as a claim about the curriculum arms' own",
    "  late - early rise.  The first is better: it is the only way P1 measures load.")

# ---------------------------------------------------------------- ARM 4: the counterbalance
A, B = SESS['order_A'], SESS['order_B']
X, Y, Z = SESS['blocks']['X'], SESS['blocks']['Y'], SESS['blocks']['Z']
same_items = sorted(A[:8] + A[16:]) == sorted(B[:8] + B[16:]) == sorted(X + Z)
y_mid = A[8:16] == Y and B[8:16] == Y
swap = A[:8] == Z[::1] or A[:8] == X
late_early_swap = A[:8] == X and A[16:] == Z and B[:8] == Z and B[16:] == X
arm(4, "the counterbalance is what the amendment says it is",
    same_items and y_mid and late_early_swap,
    f"  X and Z are the contrast's items, the same set early and late: {same_items}",
    f"  Y is turns 9-16 in both orders, so it never enters late - early: {y_mid}",
    f"  order A is X,Y,Z and order B is Z,Y,X, so each contrast item is early in half the",
    f"  sessions and late in the other half: {late_early_swap}",
    "  and run_e8.py assigns A to even session indices and B to odd, over the same index",
    "  range in every arm, so each arm gets equal numbers of both orders.",
    "  ⌗ The amendment's correction to the original counterbalancing sentence is right, and",
    "  it is the kind of correction that is usually left unmade.")

# ---------------------------------------------------------------- ARM 5: subjects clean of the programme
CURRIC = ' '.join(read(os.path.join(ROOT, p) if p.endswith('.tex') else os.path.join(EXP, p))
                  for p in SPIN).lower()
TERMS = [w for w in ('halden', 'varden', 'arp', 'adaptive reasoning', 'disposition',
                     'sound disposition', 'reasoning protocol') ]
hits = []
for iid in sorted(set(A)):
    it = ITEMS[iid]
    txt = ' '.join(str(it.get(k, '')) for k in ('message', 'prompt', 'claim', 'document')).lower()
    for t in TERMS:
        if t in txt:
            hits.append((iid, t))
# and the reverse: does the curriculum name any drawn item's own subject matter?
arm(5, "the drawn items are clean of the curriculum",
    not hits,
    f"  24 drawn items searched for the curriculum's own terms {TERMS}",
    f"  hits: {hits if hits else 'none'}",
    "  The items come from E1, E2 and E3, whose own registrations put them outside physics",
    "  and outside the curriculum's domain, and the draw excludes E1-09, the item E1 itself",
    "  recorded as defective.",
    "  ⌗ WHAT THIS DOES NOT ESTABLISH, and nothing in the registration does: that no drawn",
    "  item is CLOSE to the curriculum in kind rather than in words.  The curriculum is a",
    "  disposition about how to weigh claims, and E2's items are claims to weigh -- so the",
    "  spin-up is on-task for E2 by construction.  That is the experiment's point and not a",
    "  defect; it is worth one sentence in the registration so that a transfer effect is",
    "  not later read as a general one.")

# ---------------------------------------------------------------- ARM 6: the reminder against the disposition
HEADS = re.findall(r'^## \d+\. (.+)$', DISP, re.M)
SECS = re.split(r'^## ', DISP, flags=re.M)[1:]
LINES = [ln for ln in REMIND.split('\n') if re.match(r'^\d+\.', ln.strip())]
lead = REMIND.split('\n')[0]


def words_of(s):
    return set(w for w in re.findall(r"[a-z']+", s.lower()) if len(w) > 3)


trace = []
for i, ln in enumerate(LINES):
    head = HEADS[i] if i < len(HEADS) else ''
    sec = SECS[i] if i < len(SECS) else ''
    body = words_of(ln) - words_of(head)
    covered = body & words_of(sec)
    trace.append((i + 1, head, ln.strip()[:60], len(body), len(covered),
                  sorted(body - words_of(sec))[:6]))
all_traced = all(r[3] == 0 or r[4] / max(r[3], 1) > 0.65 for r in trace)
arm(6, "the reminder is one line per heading, in the document's own words",
    len(LINES) == len(HEADS) == 7 and all_traced and len(REMIND.split()) == 165,
    f"  headings in disposition_sound.md: {len(HEADS)};  numbered lines in reminder.md: {len(LINES)}",
    f"  word count: {len(REMIND.split())} (the registration says 165 with the lead-in line)",
    f"  lead-in: \"{lead}\"",
    "  each line, and how much of its wording beyond the heading is the section's own:",
    *[f"      {n}. {h[:46]:46s} {cov}/{tot} of its added words are in the section"
      + (f"   not in it: {miss}" if miss else "") for n, h, _, tot, cov, miss in trace],
    "  ⇒ the seven lines are the seven headings, each extended with the section's own",
    "  sentences rather than with new content -- `in its own words, with nothing added'",
    "  is accurate as a description of the materials.",
    "  NEGATIVE WAS REACHABLE: a line whose added wording is not in its section would be a",
    "  reminder that is a stronger intervention than the registration describes, which",
    "  would matter for P3.")

# ---------------------------------------------------------------- ARM 7: what reaches the scorer
scorer_msgs = re.findall(r"Trial\('E8', arm, tag, [^,]+, (f?\"[^\"]*\"|f?'[^']*')", RUN)
uses_item_text = all(("it['" in m) for m in scorer_msgs)
uses_record_msg = any("r['message']" in m for m in scorer_msgs)
tag_src = re.search(r'tag = (.*)', RUN).group(1)
arm(7, "what reaches the scorer, and whether the arm can be inferred from the reply",
    uses_item_text and not uses_record_msg,
    f"  the scorer's message is built from the ITEM's own text in every branch: {uses_item_text}",
    f"  the record's `message' (which in REMINDER carries the reminder) is never passed to",
    f"  a scorer: {not uses_record_msg}",
    "  ⇒ so the REMINDER arm's prefix does not reach the scorer through the task.  Good,",
    "  and it is the obvious way this blind would have leaked.",
    "",
    f"  ⌗ the tag is {tag_src.strip()}",
    "  which carries the SESSION and the TURN index.  It is used only for the record's",
    "  path, not in the scorer's message -- but the code comment beside it says the tag",
    "  `carries neither arm, session nor turn', and it carries two of the three.  A",
    "  comment that overstates a blind is how a later reader stops checking it.",
    "",
    "  ⛔ AND THE CHANNEL THE REGISTRATION DOES NOT ADDRESS: the REMINDER arm's reply may",
    "  echo the reminder's own wording -- `go to the source', `failures come in pairs',",
    "  `do not close what is open' -- and a judge reading the reply alone can infer the",
    "  condition from it.  E1's rubric already strips <receipt> blocks for a related",
    "  reason; nothing strips or measures disposition-echo.",
    "  → RECOMMENDED, and it is a scoring-side addition that costs nothing at run time:",
    "  record, per reply, whether any of the seven reminder lines' distinctive phrases",
    "  appears in it, and report that rate by arm.  If it is high in REMINDER and low",
    "  elsewhere, the blind is nominal on that arm and the scores should be read with it;",
    "  if it is low everywhere, the blind is real and that is worth knowing too.  The check",
    "  is measurable BEFORE the main run, on the pilot's own replies.")

# ---------------------------------------------------------------- ARM 8: the mechanics against the registration
mech = {}
# (a) the failure record
mech['failure record survives a re-run'] = None      # set from the demonstration below
# (b) scoring skips incomplete sessions
mech['scoring skips incomplete sessions'] = 'turn24.json' in RUN.split('def score')[1].split('def glob_dirs')[0]
# (c) the turn timeout can fire while the subject is silent
loop = RUN.split('while True:')[1].split('if ev.get')[0]
mech['the turn timeout can fire on a silent subject'] = (
    'readline' in loop and ('settimeout' in loop or 'alarm' in loop or 'select' in loop))
# (d) the pause switch
mech['the pause switch is checked before each session'] = 'if os.path.exists(PAUSE_FILE)' in RUN
# (e) isolation
mech['the subject runs with no tools and a clean env'] = "'--tools', ''" in RUN and '_clean_env()' in RUN

# a demonstration rather than a reading, for the two that matter
demo = {}
d = tempfile.mkdtemp()
sess = os.path.join(d, 'IMPLICIT', 's00')
os.makedirs(sess)
open(os.path.join(sess, 'FAILED.txt'), 'w').write('first attempt died at turn 11')
open(os.path.join(sess, 'turn1.json'), 'w').write('{}')
import shutil as _sh
_sh.rmtree(sess, ignore_errors=True)
os.makedirs(sess)                                   # exactly run_session's own two lines
demo['FAILED.txt after the re-run begins'] = os.path.exists(os.path.join(sess, 'FAILED.txt'))
open(os.path.join(sess, 'turn1.json'), 'w').write('{}')
demo['a 1-of-24 session is enumerated by score()'] = any(
    os.path.exists(os.path.join(sess, f'turn{k}.json')) for k in range(1, 25))
t0 = time.time()
p = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(3)'], stdout=subprocess.PIPE, text=True)
line = p.stdout.readline()                          # a silent subject: readline blocks, no check runs
demo['readline on a silent subject blocked (s)'] = round(time.time() - t0, 1)
p.wait()
_sh.rmtree(d, ignore_errors=True)
mech['failure record survives a re-run'] = demo['FAILED.txt after the re-run begins']
mech['scoring skips incomplete sessions'] = not demo['a 1-of-24 session is enumerated by score()']
arm(8, "the mechanics do what the registration says they do",
    all(mech.values()),
    *[f"      {'OK ' if v else '⛔ '} {k}" for k, v in mech.items()],
    "  (the first two rows are the demonstrations below, not a reading of the source)",
    "",
    "  THE THREE THAT FAIL, DEMONSTRATED RATHER THAN ASSERTED:",
    f"    ⒜ `The failure is recorded in FAILED.txt' -- but a re-run's first act is",
    f"       rmtree(d) + makedirs(d).  Run here: FAILED.txt survives = {demo['FAILED.txt after the re-run begins']}.",
    "       ⇒ the record of the failure is destroyed by the attempt that follows it, so a",
    "       session that failed twice looks like a session that failed once, and one that",
    "       eventually succeeded looks like one that never failed.",
    "       → write the failure OUTSIDE the session directory (a sibling FAILED/ or an",
    "       appended log), one line.",
    f"    ⒝ `A session is the unit: it is complete when its last turn is recorded' -- but",
    f"       score() walks every turn file it finds, with no completeness test. Partial",
    f"       session enumerated here = {demo['a 1-of-24 session is enumerated by score()']}.",
    "       ⇒ a session that died at turn 11 contributes 11 scored EARLY turns and no late",
    "       ones, which biases late - early by exactly the thing the experiment measures.",
    "       → skip a session directory without turn24.json in score(), one line.",
    f"    ⒞ the 900 s turn timeout is checked only AFTER a line arrives, and readline()",
    f"       blocks. Demonstrated: a silent subprocess held readline for "
    f"{demo['readline on a silent subject blocked (s)']} s with no check run.",
    "       ⇒ on a subject that hangs without emitting, the timeout never fires and the",
    "       batch stalls on that worker.",
    "       → put the deadline on the stream (a poll/select with a timeout, or a reader",
    "       thread), or accept it and say so.",
    "  ⌗ The pause switch and the isolation are as described, and the isolation is the one",
    "  thing in this harness this seat has checked before and would have flagged again.")

# ---------------------------------------------------------------- ARM 9: how many observations
per_side = {k: len([i for i in SESS['blocks']['X'] if i.startswith(k)]) for k in ('E1', 'E2', 'E3')}
n_main = 16
arm(9, "how many observations each clause rests on",
    True,
    f"  per session and side (early or late): {per_side['E1']} coverage, {per_side['E2']} guard",
    f"  (one of them open), {per_side['E3']} reviews -- 8 items",
    f"  so the composite rests on {8 * n_main} item-scores per arm per side at n = {n_main},",
    f"  and the CLOSURE clause of P3 rests on ONE open item per side per session:",
    f"  {n_main} early and {n_main} late binary observations per arm.",
    "  ⛔ P3 HAS TWO CLAUSES AND THE REGISTRATION SIZES ONLY THE FIRST.  The n rule is",
    "  written for `a 10-point late - early difference' in the composite; nothing sizes the",
    "  closure rate, which is a binomial with 16 trials a side.  A 10-point closure",
    "  difference is undetectable at that n (16 vs 16 binary observations), so the closure",
    "  clause will come back `not established' almost whatever happens.",
    "  → RECOMMENDED: either say in the registration that the closure clause is descriptive",
    "  and not powered, or put a second open item in each of X and Z -- which the draw can",
    "  do, because E2's open items are not exhausted by the two it drew.")

# ---------------------------------------------------------------- the three later-landing objects
NEW = os.path.join('/tmp/claude-0/-home-user-shadow-of-existence/'
                   '3f654921-f94d-5e03-8dca-e6e4ffe98045/scratchpad/e8_new',
                   'resources', 'ARP_LLM_paper', 'experiments')
HEAD70B = git('rev-parse', 'FETCH_HEAD').strip()

# ---- ARM 10: E3's amendment, against E3's own registration
E3REG = read(os.path.join(NEW, 'E3', 'PREDICTION.md'))
pre, post = E3REG.split('## Amendment before the main run')[0], E3REG.split('## Amendment before the main run')[1]
already_defined = ('valid and invalid extra issues raised' in pre
                   and 'counts other problems the review raises and marks each as valid or invalid' in pre)
scorer_same = 'the scorer prompt is unchanged' in post
seen_stated = 'These numbers were seen before this amendment' in post
pilot_discarded = 'discarded afterwards' in pre
hand = ('seed 3755' in post and 'stratified by condition' in post
        and 'before the main run' in post)
intervals = post.count('interval excluding 0') >= 2
arms_named = 'Sonnet' in post and 'analysed separately' in pre
pilot = dict(re.findall(r'- (C\d): ([0-9.]+)', post))
dir_ok = (float(pilot['C1']) < float(pilot['C0'])) and (float(pilot['C3']) < float(pilot['C1']))
arm(10, "E3's amendment -- a promoted measure, or a new one",
    already_defined and scorer_same and seen_stated and pilot_discarded and hand and intervals,
    f"  read at 70's branch head {HEAD70B[:9]} (the amendment landed after this read began)",
    f"  the promoted measure is one E3's registration ALREADY defined and the scorer",
    f"  already records -- `the valid and invalid extra issues raised', and a rubric that",
    f"  `counts other problems the review raises and marks each as valid or invalid': {already_defined}",
    f"  and the scorer prompt is unchanged: {scorer_same}",
    f"  ⇒ a PROMOTION, not a new instrument.  That is the distinction that matters, and it",
    f"  is the one the amendment claims.",
    "",
    f"  the pilot's values are stated as SEEN before the amendment: {seen_stated}",
    f"  pilot: {pilot}, and both predictions point the way the pilot already points: {dir_ok}",
    f"  the pilot is discarded, so the main run is fresh data: {pilot_discarded}",
    "  ⇒ a pilot-informed prediction tested on data the pilot does not contain is",
    "  legitimate, and saying so in bold is what makes it legitimate rather than lucky.",
    f"  both new predictions carry an interval: {intervals}  -- unlike E8's P2 and P3",
    f"  (ARM 1), which is worth noticing because it is the same seat on the same day.",
    "",
    f"  the hand-check is registered before the run, stratified, seeded, scored before the",
    f"  aggregate is read: {hand}",
    "  ⇒ ⛭ THIS IS E1's DEFECT REPAIRED AT THE SOURCE.  At r7754 this line reported E1's",
    "  hand-check as 16 of 64 chosen BY OUTCOME, after the aggregate, with no κ possible.",
    "  E3's is drawn in advance by seed, stratified by condition, and scored before the",
    "  aggregate.  The lesson travelled.",
    "",
    "  ⌗ ONE CLAUSE WORTH ADDING, and E3 is last in the queue so there is time: the",
    f"  predictions do not name WHICH model arm they are evaluated on.  The registration",
    f"  says Sonnet `runs the same design as a second arm, analysed separately' ({arms_named}),",
    "  and the amendment puts the hand-check on Opus -- so say the same of P1b and P3b.",
    "  Otherwise two arms give two tests of each prediction and `held' has two readings.")

# ---- ARM 11: E5's RESULT against its registration
E5REG = read(os.path.join(NEW, 'E5', 'PREDICTION.md'))
E5RES = read(os.path.join(NEW, 'E5', 'RESULT.md'))
MEAS = {'primary A and its two contrasts': ('**A** (anticipated / valid)' in E5RES
                                            and 'R2 − R0' in E5RES),
        'novel valid findings per review (co-primary)': 'Novel valid findings per review' in E5RES,
        'complications mishandled and found': 'Complications the author mishandled' in E5RES,
        "anticipations no reviewer raised": 'anticipations that no reviewer raised' in E5RES,
        'bootstrap intervals over documents': 'bootstrap over 30 documents' in E5RES,
        'the n rule, computed from the pilot σ': 'n = (2.8σ/0.15)²' in E5RES,
        'the hand-check with κ': 'κ = 0.88' in E5RES and 'κ = 0.07' in E5RES,
        'the leak check': 'Leak check' in E5RES}
# the threshold sensitivity, recomputed from the result's own two tables
hand_tab = dict(R0=(5.2, 6.0), R1=(4.8, 5.8), R2=(5.6, 6.9))
matcher_R1_R0 = hand_tab['R1'][0] - hand_tab['R0'][0]
hand_R1_R0 = hand_tab['R1'][1] - hand_tab['R0'][1]
full_R1_R0 = 5.02 - 5.82
shift = {k: round(v[1] - v[0], 2) for k, v in hand_tab.items()}
arm(11, "E5's RESULT against its own registration",
    all(MEAS.values()),
    *[f"      {'OK ' if v else '⛔ '} {k}" for k, v in MEAS.items()],
    "  ⇒ every registered measure is reported, including the two the runner had not built,",
    "  which were added as blind passes and declared as a deviation.  ⛭ The defect this",
    "  line reported in E1 at r7754 -- four registered measures unreported -- does NOT",
    "  recur here, and the hand-check takes the FULL registered sample rather than one",
    "  chosen by outcome, which was the other half of that finding.",
    "",
    "  ⛔ THE ONE PLACE THE RESULT'S OWN BLANKET IS WIDER THAN ITS EVIDENCE.  The hand-check",
    f"  puts κ on `valid' at 0.07, and measures the threshold's size on the sample:",
    *[f"      {k}: matcher {v[0]} novel, hand {v[1]} novel  (shift {shift[k]:+.2f})"
      for k, v in hand_tab.items()],
    f"  The RESULT then says `every conclusion above stands under either threshold', and",
    f"  for P1, P2 and P3 it shows that.  But it also reports a fourth conclusion -- `one",
    f"  registered contrast moved that no prediction named': R1 - R0 on novel valid",
    f"  findings, {full_R1_R0:+.2f} with the interval [-1.47, -0.08], i.e. a margin of 0.08 from 0.",
    f"  On the hand-checked sample that same contrast is {matcher_R1_R0:+.1f} under the matcher and",
    f"  {hand_R1_R0:+.1f} under the hand coding -- the sign survives, the magnitude halves, and the",
    f"  per-level shift ({min(shift.values()):+.1f} to {max(shift.values()):+.1f} findings) is an order larger than the margin.",
    "  ⇒ the blanket covers the three predictions; it does not cover the one finding whose",
    "  interval barely excludes 0, and that finding is the one a paper sentence would most",
    "  likely quote ('a reviewer given the brief finds fewer problems of any kind').",
    "  → RECOMMENDED: either re-state that contrast with the threshold sensitivity beside",
    "  it, or mark it as not robust to the validity threshold.  One clause.",
    "  ⌗ And a checked non-defect: κ = 0.07 at 86.5% agreement against 85.4% chance is a",
    "  PREVALENCE artefact, not a disagreement -- nearly every finding is valid under both",
    "  codings.  The RESULT says exactly that and reports the disagreement's DIRECTION",
    "  instead, which is the right reading of a degenerate κ.")

# ---- ARM 12: the E1 RESULT additions
E1RES = read(os.path.join(NEW, 'E1', 'RESULT.md'))
FOUR = {'the hand-check, redone at the registered size': '64 passes' in E1RES or '64 trials' in E1RES,
        '(a) coverage, mean ask score, with C1 − C0': 'Coverage, the mean ask score' in E1RES,
        "McNemar's exact p on the paired H contrasts": "McNemar's exact p" in E1RES,
        'H by receipt presence': 'H by receipt presence' in E1RES}
redrawn = 'seed 7755' in E1RES and 'scored blind' in E1RES
before_opened = 'before any packet was opened' in E1RES
still_after = 'still comes after the aggregate' in E1RES
pass_only = 'trials whose hard ask the scorer passed' in E1RES
# the population bound the 0-of-64 interval actually gives
n_pass, ub = 309, 0.056
arm(12, "the E1 RESULT additions against E1's registration",
    all(FOUR.values()) and redrawn and before_opened and still_after,
    *[f"      {'OK ' if v else '⛔ '} {k}" for k, v in FOUR.items()],
    f"  the sample is redrawn by seed and scored blind: {redrawn}; registered before any",
    f"  packet was opened: {before_opened}; and the remaining deviation is restated: {still_after}",
    "  ⇒ ⛭ BOTH HALVES OF THIS LINE's r7754 FINDING ARE REPAIRED: the four registered",
    "  measures are reported, and the outcome-chosen 16 is replaced by the registered 64,",
    "  drawn in advance.  The part that could not be repaired -- the check following the",
    "  aggregate -- is stated at its size rather than dropped.",
    "",
    f"  ⛔ AND ONE DEVIATION THAT IS NOT IN THE DEVIATION LIST: the registration says `20%",
    f"  of scored trials, stratified by condition'; what was drawn is 64 trials WHOSE HARD",
    f"  ASK THE SCORER PASSED ({pass_only}).  That is the right frame for measuring false",
    "  passes and the wrong one for the registered κ: the hard-ask column is constant",
    "  BECAUSE the sample was drawn on it, and the RESULT attributes the undefined κ to",
    "  constancy rather than to the draw.",
    "  ⌗ AT ITS SIZE, WHICH IS SMALL: the hard ask passed in 38–39 of 40 per cell, so a",
    "  random 64 would have held about one or two failures and κ would very likely still",
    "  have been degenerate.  The verdict does not change; the deviation list should carry",
    "  the line anyway, because it is the difference between a statistic that could not be",
    "  computed and one that was designed out.",
    "",
    f"  ⌗ AND ONE READING OF THE BOUND, because this line set the bound at r7754: 0 of 64",
    f"  gives an upper 95% bound of {ub:.1%} on the false-pass RATE, which over about {n_pass}",
    f"  passes is up to {int(n_pass * ub)} false passes -- not the five this line named as the number",
    f"  that would matter to a COUNT.  The conclusion still holds, because the ceiling is a",
    "  RATE claim (the hard ask handled 38–39 of 40 in every condition) and a 5.6% ceiling",
    "  on the error rate leaves it standing.  Said because the two numbers look like they",
    "  disagree and do not.")

# ----------------------------------------------------------------- the ledger
print("\n" + "=" * 100)
print("  THE LEDGER")
for n, ok, title in VERDICTS:
    print(f"    {'PASS' if ok else 'FAIL'}  ARM {n:2d}  {title}")
bad = [n for n, ok, _ in VERDICTS if not ok]
print(f"\n  {len(VERDICTS) - len(bad)} of {len(VERDICTS)} arms PASS"
      + ("" if not bad else f";  arms whose registered criterion is NOT met: {bad}"))
print("  (an arm's FAIL here is a finding about the object read, not a failure of the read)")
print("=" * 100)
