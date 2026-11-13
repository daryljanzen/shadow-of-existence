"""E6 runner: self-review (S) vs two-seat game with receipts and cold readers (G-ARP) vs the same without receipts
(G-noR), 6 calls each; blind scoring of the final version.  Usage:  python3 run_e6.py pilot|main"""
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from subject import Trial, run_one, run_batch  # noqa: E402

SYS = 'You are a helpful assistant.'
PILOT = ['E6-01', 'E6-07', 'E6-13', 'E6-19']
RECEIPT = ('Here is an analysis and a review of it. First, under "Receipt", restate in your own words each point the '
           'review makes and what it would change. Then produce an improved version.')
NORECEIPT = 'Here is an analysis and a review of it. Produce an improved version.'
SCORER = ('You are scoring a final version of an analysis against a key. You are given the question, the data, the '
          'four known flaws of the original draft (with corrections), the list of valuable extensions, and the FINAL '
          'VERSION. For each flaw, 1 if the final version gets it right (corrected), else 0 (a mention without a fix '
          'is 0). For each extension, 1 if present and valid. Count new errors the final version introduces that were '
          'not in the original flaws. Also guess: was this written by a single author or several (single/several)? '
          'Reply with JSON only: {"corrected": {"1":0|1,"2":0|1,"3":0|1,"4":0|1}, "extensions": [0|1, ...], '
          '"introduced_errors": n, "authorship_guess": "single|several"}')


def strip_receipt(t):
    m = re.search(r'(?im)^\W*receipt\W*$', t or '')
    if not m:
        return t
    rest = t[m.end():]
    n = re.search(r'(?im)^\W*(improved|revised|final)?\s*(version|analysis)\W*$', rest)
    return rest[n.end():].strip() if n else t


def ctx(task):
    return f"QUESTION:\n{task['question']}\n\nDATA:\n{task['data']}\n\n"


def chain(task, cond, rep, base):
    d = os.path.join(base, cond, f"{task['id']}__r{rep}")
    call = lambda j, msg: run_one(Trial('E6', cond, task['id'], SYS, msg, os.path.join(d, f'step{j}.json'), rep=rep))['response']  # noqa: E731
    v = task['draft']
    if cond == 'S':
        for j in range(1, 7):
            v = call(j, ctx(task) + f"Here is your current analysis:\n\n<analysis>\n{v}\n</analysis>\n\n"
                                    "Review it critically and produce an improved version.")
        return v
    instr = RECEIPT if cond == 'G-ARP' else NORECEIPT
    a = call(1, ctx(task) + f"Here is a draft analysis:\n\n<analysis>\n{v}\n</analysis>\n\nProduce an improved version.")
    a = strip_receipt(a)
    r1 = call(2, ctx(task) + f"<analysis>\n{a}\n</analysis>\n\nPlease review this analysis.")
    b = strip_receipt(call(3, ctx(task) + f"<analysis>\n{a}\n</analysis>\n\n<review>\n{r1}\n</review>\n\n{instr}"))
    r2 = call(4, ctx(task) + f"<analysis>\n{b}\n</analysis>\n\nPlease review this analysis.")
    a2 = strip_receipt(call(5, ctx(task) + f"<analysis>\n{b}\n</analysis>\n\n<review>\n{r2}\n</review>\n\n{instr}"))
    return call(6, ctx(task) + f"<analysis>\n{a2}\n</analysis>\n\nProduce the final version of this analysis.")


def main():
    phase = sys.argv[1]
    tasks = json.load(open(os.path.join(HERE, 'materials', 'tasks.json')))
    if phase == 'pilot':
        tasks = [t for t in tasks if t['id'] in PILOT]
    reps = 1 if phase == 'pilot' else 2
    base = os.path.join(HERE, 'runs_' + phase)
    jobs = [(t, c, k) for t in tasks for c in ('S', 'G-ARP', 'G-noR') for k in range(reps)]
    with ThreadPoolExecutor(4) as ex:
        finals = list(ex.map(lambda j: chain(*j, base), jobs))
    sc = []
    for (t, c, k), fv in zip(jobs, finals):
        key = '\n'.join(f"{f['f']}. [{f['type']}] {f['description']} CORRECTION: {f['correction']}" for f in t['flaws'])
        ext = '\n'.join(f"- {e}" for e in t['open_extensions'])
        msg = f"{ctx(t)}KNOWN FLAWS:\n{key}\n\nEXTENSIONS:\n{ext}\n\nFINAL VERSION:\n{strip_receipt(fv)}"
        sc.append(Trial('E6', c, t['id'], SCORER, msg, os.path.join(HERE, 'scores_' + phase, c, f"{t['id']}__r{k}.json"),
                        role='scorer', rep=k))
    run_batch(sc, workers=4)


if __name__ == '__main__':
    main()
