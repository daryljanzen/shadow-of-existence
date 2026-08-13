#!/usr/bin/env python3
"""check_silent.py -- WHEN A CRITERION IS SILENT, SILENT IS THE ANSWER.

** WHY.  ** Twice now a node has carried a settled matter to Daryl as an open decision.

  * ** r2599, `PO-7`: ** the receipt stood "complete, and waiting" while its own inversion check listed
    two live routes.  *** The decision did not exist. ***
  * ** r2643, `PO-9`: ** the receipt asked for authorisation on "is the substrate's dimension settled?"
    when P12 states the criterion "** is silent on the dimension itself **".  *** The decision existed
    and was not about what it was presented as being about: the physics was answered, and only the
    CLOSURE was reserved. ***

  ⇒ ** Daryl, r2643: ** "I have no idea why it would be restricted in any way beyond structural
  requirements like empirical evidence.  ** Isn't that just a least-arbitrariness question you put to
  me? **"

** WHAT THIS GATE CHECKS. **  That no `kills/` receipt asks for a judgement on a question the corpus
records the criterion as SILENT on.  ** A criterion answering "I do not settle this" is a finding **, and
the only thing left is whether to record it.

  ⚠ ** It cannot tell a real authorisation from a manufactured one in general ** -- that is a reading.
  *** What it can do is fail when a receipt pairs an authorisation request with a corpus phrase declaring
  the criterion silent on that same object, which is the specific shape both failures took. ***

    python3 corpus/check_silent.py

Written r2643.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

ASKS = re.compile(r"(asks? for authorisation|awaiting authorisation|and Daryl authorises"
                  r"|requests? a judgement)", re.I)
SILENT = re.compile(r"(is silent on|the criterion is silent|criterion has been put and it returned "
                    r"silent|silent is the answer)", re.I)
SUPERSEDED = re.compile(r"(no longer asks|does not ask|corrected r\d{4}|rewritten r\d{4}"
                        r"|was never|superseded)", re.I)


def main():
    print()
    print('  check_silent -- does a receipt ask for a judgement the criterion already declined?')
    print()
    bad = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'kills', '*.md'))):
        t = re.sub(r'\s+', ' ', open(f, encoding='utf-8', errors='replace').read())
        for m in ASKS.finditer(t):
            win = t[max(0, m.start() - 400):m.end() + 400]
            if SUPERSEDED.search(win):
                continue
            if SILENT.search(t):
                bad.append((os.path.basename(f), m.group(0)))
    if bad:
        print()
        for f, phrase in bad:
            print(f'    [FAIL] {f} says "{phrase}" while the corpus records the criterion as SILENT')
        print()
        print('    ⛔ ** A CRITERION ANSWERING "I DO NOT SETTLE THIS" IS A FINDING. **  *** Do not carry')
        print('       the silence to a human as an open question -- the only thing left is whether to')
        print('       record it. ***')
        return 1
    print('  no receipt asks for a judgement on a question the criterion has declined.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
