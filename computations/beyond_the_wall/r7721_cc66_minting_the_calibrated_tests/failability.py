#!/usr/bin/env python3
"""`r7721+cc66` FAILABILITY of the minted receipt — a GREEN CONTROL first, then one leg per gate.

⛔ A LEG REPORTING `0` FAIL MEANS THE PERTURBATION WENT **TOWARDS** THE GATE, not that the gate is
   sound.  That happened at `r7705` leg A (a factor applied the wrong way SHRANK the departure the
   gate was watching), so every leg below states which direction it pushes and why that direction
   should break the gate it names.

⛔⛔ AND THE FIRST RUN OF THIS FILE GOT ITS OWN LEG A WRONG, WHICH IS WORTH MORE THAN THE LEG.  It
   reported "THE NAMED GATE DID NOT GO RED" while that very gate was the FIRST ENTRY in the red list
   it had just printed.  The cause was the MATCHER and not the gate: the gate's name is upper-case
   and the string sought was lower-case.  ⇒ *A statement about the matcher's miss read as a statement
   about the gate's soundness -- the same fault this seat has been counting, a tenth time, and this
   time it would have made me distrust a gate that works.  The comparison is case-folded now, and
   every red is printed beside the verdict so the two can be checked against each other.*
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_located_transition_is_beyond_a_million_step_free_surrogates_and_'
                    'the_source_exclusions_printed_clause_is_licensed_only_at_the_two_wider_'
                    'smoothings.py')
SRC = open(RCPT, encoding='utf-8').read()

# each leg: (name, what it perturbs and WHICH WAY, the substitution, the gate it must break)
LEGS = [
    ("A  the located step SHRUNK to a tenth -- pushes it INTO the surrogate spread, so the "
     "'beyond every one of a million' gate must lose it",
     ("    return (float(R[hi].mean() - R[lo].mean()),",
      "    return (0.1 * float(R[hi].mean() - R[lo].mean()),"),
     "beyond every one of a million"),
    ("B  the SOURCE ratio's own curve given a large real step -- pushes its `p` DOWN out of the "
     "0.40-0.90 window the gate requires",
     ("    return cs, np.array([_ratio(st, c - half, c + half) for c in cs])",
      "    _v = np.array([_ratio(st, c - half, c + half) for c in cs])\n"
      "    return cs, _v + (0.03 if st is _STK else 0.0) * (cs > 1.8)"),
     "SOURCE RATIO'S OWN STEP IS NOTHING"),
    ("C  the printed multiple's bar LOWERED to 3 -- makes the NARROWEST smoothing clear it too, so "
     "the gate's 'and NOT at the narrowest' arm must break",
     ("PRINTED_MULTIPLE = 6.0", "PRINTED_MULTIPLE = 3.0"),
     'PRINTED "MORE THAN SIX TIMES"'),
    ("D  the power requirement LOWERED to 0.5 -- makes the narrowest clear it, so the gate's "
     "'BELOW it at the narrowest' arm must break",
     ("POWER_REQ = 0.95", "POWER_REQ = 0.5"),
     "POWER IS WHAT LICENSES THAT RESTRICTION"),
    ("F  one PINNED literal moved by ten times its allowance -- pushes the measured value OUTSIDE "
     "the band, so the index-row pinning gate must break.  ⌗ This gate needed no leg to prove "
     "failable: it went red twice for real reasons while being written -- once on a literal the row "
     "does not print, once on a tolerance narrower than the printed precision",
     ("abs(_x_mid - 6.60) <= 0.005", "abs(_x_mid - 6.55) <= 0.005"),
     "PINNED HERE BY A TWO-SIDED COMPARISON"),
    ("E  the restricting words sought in the .tex CHANGED to words that are not there -- so the "
     "scope gate must stop finding them",
     ("_SCOPE = ' '.join(['at', 'the', 'two', 'wider', 'smoothings'])",
      "_SCOPE = ' '.join(['at', 'all', 'three', 'smoothings'])"),
     "SCOPE OF THE PRINTED CLAIM IS ITSELF GATED"),
]


def run(text):
    with tempfile.NamedTemporaryFile('w', suffix='.py', dir=os.path.dirname(RCPT),
                                     delete=False, encoding='utf-8') as f:
        f.write(text)
        p = f.name
    try:
        r = subprocess.run([sys.executable, '-u', p], capture_output=True, text=True, timeout=1800)
        out = r.stdout + r.stderr
        return out.count('[FAIL]'), out.count('[PASS]'), re.findall(r'\[FAIL\] (.{0,150})', out)
    finally:
        os.unlink(p)


print("\n  ⛭ GREEN CONTROL FIRST -- the unperturbed receipt must be clean, or no leg means anything")
nf, np_, _ = run(SRC)
print(f"       unperturbed: {np_} PASS, {nf} FAIL  "
      f"⇒ {'CONTROL GOOD' if nf == 0 and np_ == 7 else '⛔ CONTROL BAD -- stop'}")
if nf or np_ != 7:
    sys.exit(1)

ok = True
for name, (old, new), must in LEGS:
    print(f"\n  ⛔ LEG {name}")
    if old not in SRC:
        print("       ⛔ the anchor is not in the receipt -- the leg is not testing what it claims")
        ok = False
        continue
    nf, np_, names = run(SRC.replace(old, new, 1))
    hit = any(must.casefold() in n.casefold() for n in names)   # ⛔ case-folded: see header
    print(f"       {np_} PASS, {nf} FAIL")
    for n in names:
        print(f"         red: {n[:110]}")
    print(f"       ⇒ {'✓ the named gate went red' if hit else '⛔ THE NAMED GATE DID NOT GO RED'}"
          + ("" if nf else "  ⛔ AND NOTHING WENT RED: the perturbation went TOWARDS the gate"))
    ok = ok and hit

print(f"\n  ⇒ failability {'ESTABLISHED on every leg' if ok else '⛔ NOT established'}")
sys.exit(0 if ok else 1)
