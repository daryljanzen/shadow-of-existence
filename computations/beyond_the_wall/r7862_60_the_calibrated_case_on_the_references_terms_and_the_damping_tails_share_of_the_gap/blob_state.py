# -*- coding: utf-8 -*-
"""Ⓓ④ THE CONDITION THE ORDER SET FOR DEFERRING ITEM ③, recorded so the receipt need not run git.

⛭ *Item ③ says to add the four provenance keys in the next revision that moves the instrument's blob
for another reason.  So the deferral's condition is that THIS revision does not move it -- and that
is a claim about two states of one file, which this script records: the blob of the instrument as it
is on disk, and the blob of `origin/main`'s copy of the same file.*

⛔ ** AND THE FIRST VERSION OF THAT GATE COMPARED THE WRONG TWO THINGS. **  *It asserted the
instrument on disk hashes to the blob the re-solved grid RECORDED, `6fcc379fd...`, and it does not:
`r7860` re-solved the CMB grid and only then wired `Dl_pairs` at `r7859`'s ruling, so the instrument
moved AFTER that grid was written.  The grid's record is a fact about when the grid was made, not
about what the file is now -- and taking one for the other is the same error as reading a header for
a reported number.*

    python3 blob_state.py
"""
import hashlib
import io
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
REL = os.path.join('computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')


def blob(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def main():
    with open(os.path.join(ROOT, REL), 'rb') as fh:
        disk = fh.read()
    out = dict(path=REL, on_disk_blob=blob(disk), on_disk_bytes=len(disk))
    for ref in ('origin/main', 'HEAD'):
        r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (ref, REL)],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        key = ref.replace('/', '_')
        if r.returncode == 0:
            out[key + '_blob'] = blob(r.stdout)
            out[key + '_bytes'] = len(r.stdout)
        else:
            out[key + '_blob'] = None
            out[key + '_error'] = r.stderr.decode()[-400:]
    rev = subprocess.run(['git', '-C', ROOT, 'rev-parse', 'origin/main'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out['origin_main_rev'] = (rev.stdout.decode().strip() if rev.returncode == 0 else None)
    out['unmoved_by_this_revision'] = bool(out['on_disk_blob'] == out['origin_main_blob'])
    with io.open(os.path.join(HERE, 'blob_state.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True))
    print('    the instrument on disk  : %s  (%d bytes)' % (out['on_disk_blob'],
                                                            out['on_disk_bytes']))
    print('    origin/main\'s copy      : %s' % out['origin_main_blob'])
    print('    unmoved by this revision: %s' % out['unmoved_by_this_revision'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
