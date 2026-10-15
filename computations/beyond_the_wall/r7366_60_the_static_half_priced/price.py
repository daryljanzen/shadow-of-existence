#!/usr/bin/env python3
"""`r7365`'s pricing item, discharged: WHAT THE STATIC HALF COSTS PER RUN, AND HOW OFTEN IT RUNS.

** WHY A PRICE AND NOT A PATCH. **  `r7364` routed two causes for the read index being unable to see
a ledger read: the static half's extension list has no `tsv` on it, and the traced half is weeks old
because the sweep that refreshes it runs monthly.  `r7365` ② ruled the list change **priced first**
-- wall-clock per run, and how often each gate that reads the index runs it -- and **not ordered
until the price is in**.  *This is the price.  The instrument is `70.1`'s and is not edited here.*

** WHAT IS MEASURED. **  `receipt_scope.load()` -- the call every scoped job makes -- timed three
times on each of three variants of the same file, written to a temporary directory and imported
there, so the live instrument is untouched:
      ⓵ as committed, the extension list without `tsv`
      ⓶ the MINIMAL change: `tsv` added to the list
      ⓷ the STRUCTURAL change: the list replaced by any extension, still bounded by `repo_names`
        -- which `load()` and `emit()` both already intersect against, so the list buys no safety
        it does not already have
Beside each: the `suite` scope a change to the quote-pin ledger produces, and the number of static
names the index carries.  ⌗ *The scope number is the thing the price is being weighed against: `5`
receipts scoped for a ledger change, against `44` that read the ledger.*

** RE-RUNNABLE: ** `python3 computations/beyond_the_wall/r7366_60_the_static_half_priced/price.py`.
The selector of what it measures is the three substitutions written above, in this file, beside the
measurement -- which is `r7365` ③'s standing rule applied to this revision's own reading.
"""
import importlib.util, io, os, re, subprocess, sys, time, tempfile
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

def load_mod(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s); sys.modules[name] = m; s.loader.exec_module(m)
    return m

def timed(mod, n=3):
    ts = []
    for _ in range(n):
        t = time.perf_counter(); mod.load(ROOT); ts.append(time.perf_counter() - t)
    return min(ts), sum(ts)/len(ts), max(ts)

live = load_mod(os.path.join(ROOT, 'scripts', 'receipt_scope.py'), 'rs_live')
print('NAME_RE now :', live.NAME_RE.pattern)

src = io.open(os.path.join(ROOT, 'scripts', 'receipt_scope.py'), encoding='utf-8').read()
variants = {
    'as committed (no tsv)': src,
    'minimal: + tsv': src.replace('py|tex|md|txt|npz', 'py|tex|md|txt|tsv|npz', 1),
    'structural: any extension, bounded by repo_names':
        src.replace("r'([A-Za-z0-9_.-]+\\.(?:py|tex|md|txt|npz|npy|json|dat|csv|bib))'",
                    "r'([A-Za-z0-9_.-]+\\.[A-Za-z0-9]{1,6})'", 1),
}
tmp = tempfile.mkdtemp()
out = {}
for label, body in variants.items():
    p = os.path.join(tmp, 'v_%d.py' % len(out)); io.open(p, 'w', encoding='utf-8').write(body)
    m = load_mod(p, 'rs_%d' % len(out))
    lo, av, hi = timed(m)
    idx = m.load(ROOT)[0]
    LED = 'corpus/quote_pin_baseline.tsv'
    sc = len(m.scope(idx, {LED}, set(), set(), 'suite'))
    names = sum(len(e['names']) for e in idx.values())
    out[label] = (lo, av, hi, sc, names)
    print(f'  {label:52s} load {lo:5.2f}/{av:5.2f}/{hi:5.2f}s   ledger scope {sc:4d}   '
          f'static names {names}')
print()
print('CALLERS -- how often the index is read:')
wf = io.open(os.path.join(ROOT, '.github', 'workflows', 'gates.yml'), encoding='utf-8').read()
for step in ('--scope suite', '--scope tolerance', '--scope reads', '--emit'):
    print(f'  workflow mentions {step!r}: {wf.count(step)}')


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT, from the run on this container.  ⚠ Wall-clock is machine-dependent and is REPORTED as
# a ratio as well as in seconds, so the conclusion does not rest on this machine's speed.
# ══════════════════════════════════════════════════════════════════════════════════════════════════
RESULT = {
    # label: (min load seconds, ledger `suite` scope, static names carried)
    'as_committed':  (2.95, 5, 2322),
    'minimal_tsv':   (3.12, 50, 2480),
    'structural':    (3.48, 50, 2501),
    #: the index is read by `load()` once per scoped step; the workflow has three (`suite`,
    #: `tolerance`, `reads`), and both `push` and `pull_request` fire them, so up to SIX reads per
    #: push.  `red_carry` reads it again per scoped step when it records.
    'reads_per_push': 6,
}

#: ⛭⛭⛭ THE PRICE, AND IT DOES NOT DECIDE AGAINST EITHER CHANGE.
#:   ⓶ minimal:    `+0.17` s a read = `+1.0` s a push, `+5.8` per cent of one load.
#:   ⓷ structural: `+0.53` s a read = `+3.2` s a push, `+18` per cent of one load.
#: *Against a scoped suite that runs ten to twenty-five minutes, both are inside the noise of a
#: single receipt.*  ⇒ ** Either change takes the ledger's `suite` scope from `5` to `50` -- the
#: whole of the `44` readers plus the five that were already there. **
#:   ⌗ And the structural form carries `21` MORE static names than the minimal one at `0.36` s more
#:     a read: it also sees the extensions nobody has hit yet, which is the difference between
#:     retiring the class and adding one spelling to it.
#: ⇒⇒ *** RECOMMENDATION: THE STRUCTURAL FORM.  The list buys no safety `repo_names` does not
#:     already provide, the price is three seconds a push, and `L254`'s `A1` is the standing name for
#:     why a list of spellings misses the next one. ***
#: ⚠ *The instrument is `70.1`'s: this revision prices the choice and does not make it.*
