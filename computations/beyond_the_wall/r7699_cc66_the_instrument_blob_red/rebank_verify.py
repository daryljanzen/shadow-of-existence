"""r7699+cc66 -- RE-BANK `cc66_r185_verify_cr_leafrec1` ON THE CURRENT INSTRUMENT, AND PROVE IT MOVED NOTHING BUT ITS PROVENANCE.

`P15_the_1p57_has_no_parameter_address…`'s gate ⓿⓿ compares the git blob hash of the instrument that
RAN against the one stored in the bank it produced.  `r7695`'s `COMBRHO` switch and `r7699+cc66.5`'s
snapshot key both changed that file's bytes, so the stored hash is stale and the receipt is red on
`main`.  `r7655` endorsed the gate's strictness in terms this script takes literally -- *"a bank's
provenance is the file that made it, not the file's intentions"* -- so the BANK moves, not the gate.

⛔ WHAT THIS REFUSES TO DO: relabel.  Writing the new hash into the old bank would make the gate green
   while making it a lie: the arrays would still be the old instrument's.  The run is re-done.

⛭ AND THE CLAIM "THE EDITS WERE INERT" IS MEASURED HERE, NOT ASSERTED:
   every array must be BYTE-IDENTICAL to the bank being replaced, and the `config` must differ in
   EXACTLY the keys that have to differ (`instrument_blob`, and `COMBRHO` now that it is recorded).
   *If an array moved, the edits were not additive and the right response is to find out why, not to
   bank it.*

    python3 rebank_verify.py <run.npz> [--write]
"""
import hashlib
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, '..', 'spectra'))
INSTR = os.path.abspath(os.path.join(HERE, '..', 'ACOUSTIC_two_arm.py'))
STEM = 'cc66_r185_verify_cr_leafrec1'
RUN = sys.argv[1]
WRITE = '--write' in sys.argv
fail = []

_b = open(INSTR, 'rb').read()
LIVE = hashlib.sha1(b'blob %d\0' % len(_b) + _b).hexdigest()

old = np.load(os.path.join(SP, STEM + '.npz'), allow_pickle=True)
new = np.load(RUN, allow_pickle=True)
co = json.loads(str(np.atleast_1d(old['config'])[0]))
cn = json.loads(str(np.atleast_1d(new['config'])[0]))

print(f"  RE-BANK {STEM}")
print(f"    the instrument on disk now : {LIVE}")
print(f"    the run's own config says  : {cn.get('instrument_blob')}")
print(f"    the bank being replaced    : {co.get('instrument_blob')}")
if cn.get('instrument_blob') != LIVE:
    fail.append(f"the RUN was made by {cn.get('instrument_blob')}, not by the instrument on disk "
                f"({LIVE}) -- re-run it")
if co.get('instrument_blob') == LIVE:
    fail.append('the bank already matches the live instrument; nothing to re-bank')

# ── the arrays: byte-identical or the edits were not inert ──────────────────────────────────────
keys = [k for k in old.files if k not in ('config', 'manifest')]
print(f"\n    {len(keys)} banked array(s), each required BYTE-IDENTICAL:")
for k in keys:
    if k not in new.files:
        fail.append(f'{k}: absent from the run')
        continue
    a, b = np.asarray(old[k]), np.asarray(new[k])
    if a.shape != b.shape or a.dtype != b.dtype:
        fail.append(f'{k}: shape/dtype {a.shape}{a.dtype} vs {b.shape}{b.dtype}')
        print(f"      {k:8s} ⛔ shape/dtype")
        continue
    same = a.tobytes() == b.tobytes() if a.dtype.kind in 'fc' else bool(np.array_equal(a, b))
    if not same:
        _m = float(np.nanmax(np.abs(a.astype(float) - b.astype(float)))) if a.dtype.kind in 'fc' else -1
        fail.append(f'{k}: NOT byte-identical, max |diff| = {_m:.3e}')
    print(f"      {k:8s} {'byte-identical' if same else '⛔ MOVED'}")

# ── the config: exactly the provenance keys ─────────────────────────────────────────────────────
# ⛔⛭ ** AND THE FIRST FORM OF THIS COMPARISON COLLAPSED THE ONE DISTINCTION IT EXISTS TO KEEP. **
#   *It diffed with `co.get(x) != cn.get(x)`.  The new config carries `COMBRHO: None`; the old one has
#   NO `COMBRHO` key -- and `.get()` returns `None` for both, so the two compared EQUAL and the key
#   that was added read as unchanged.*  ⇒ ** "no `COMBRHO` key" and "`COMBRHO` was off" are different
#   statements about a bank -- which is the sentence I put in the instrument when adding the key, and
#   then erased with an idiom in the gate that checks it. **  *So keys ADDED and values CHANGED are
#   counted separately, which is the only way the added-as-None case is visible at all.*
added = sorted(set(cn) - set(co))
removed = sorted(set(co) - set(cn))
changed = sorted(k for k in set(co) & set(cn) if co[k] != cn[k])
print(f"\n    config keys ADDED   : {added}" + (f"  (values {[cn[k] for k in added]})" if added else ""))
print(f"    config keys REMOVED : {removed}")
print(f"    config keys CHANGED : {changed}")
if changed != ['instrument_blob']:
    fail.append(f'config CHANGED in {changed}, wanted exactly [instrument_blob]')
if removed:
    fail.append(f'config LOST keys {removed} -- a re-bank may not drop provenance')
if added not in ([], ['COMBRHO']):
    fail.append(f'config ADDED {added}, wanted nothing or just COMBRHO')
if added == ['COMBRHO'] and cn['COMBRHO'] is not None:
    fail.append(f"config added COMBRHO = {cn['COMBRHO']!r}; this bank is the UNSET run, so it must "
                f"record None -- a non-None value means the wrong run was banked")
want = sorted(set(changed) | set(added))

print()
if fail:
    for f in fail:
        print(f'  ⛔ [FAIL] {f}')
    raise SystemExit(1)

man = dict(json.loads(str(np.atleast_1d(old['manifest'])[0]))) if 'manifest' in old.files else {}
man['reblobbed'] = (f"r7699+cc66: re-run on the instrument carrying COMBRHO (r7695) and its snapshot "
                    f"key (r7699+cc66.5).  Every banked array verified BYTE-IDENTICAL to the "
                    f"{co.get('instrument_blob')[:8]} bank; the config differs in {want} and nothing "
                    f"else.  The gate this serves compares the instrument's hash to the bank's, so "
                    f"the bank is re-made rather than relabelled.")
out = {k: new[k] for k in old.files if k not in ('manifest',)}
out['manifest'] = np.array(json.dumps(man))
print("  ✔ every array byte-identical; the config differs in exactly the provenance keys.")
if WRITE:
    np.savez(os.path.join(SP, STEM + '.npz'), **out)
    print(f"  -> rewrote spectra/{STEM}.npz on the live instrument's provenance")
else:
    print("  (dry run -- pass --write to rewrite the bank)")
