#!/usr/bin/env bash
# check_bibliography.sh — run at the END OF EACH FIELD BAKE (and any time).
# Catches: citations with no bibitem, duplicate bibitems, and classical claims
# introduced without a source. Exit 0 = clean.
cd "$(dirname "$0")/../corpus" || exit 1
python3 - <<'PYEOF'
import re, glob, os, sys
bad = 0
papers = [f for f in sorted(glob.glob('*.tex')) if not os.path.basename(f).startswith('appendix')]

print("① UNDEFINED CITATIONS — every \\cite key needs a \\bibitem in its own file")
for f in papers:
    s = open(f, encoding='utf-8', errors='replace').read()
    cites = set(k.strip() for m in re.findall(r'\\cite\{([^}]+)\}', s) for k in m.split(','))
    bibs  = set(re.findall(r'\\bibitem\{([A-Za-z0-9_]+)\}', s))
    if not bibs:
        continue
    missing = cites - bibs
    if missing:
        print(f"   ⚠ {os.path.basename(f)[:28]:30s} {sorted(missing)}"); bad += 1
print(f"   → {bad} file(s) with undefined citations\n")

print("② DUPLICATE BIBITEMS")
d0 = 0
for f in sorted(glob.glob('*.tex')):
    s = open(f, encoding='utf-8', errors='replace').read()
    keys = re.findall(r'\\bibitem\{([A-Za-z0-9_]+)\}', s)
    dups = sorted(k for k in set(keys) if keys.count(k) > 1)
    if dups:
        print(f"   ⚠ {os.path.basename(f)[:28]:30s} {dups}"); d0 += 1; bad += 1
print(f"   → {d0} file(s) with duplicates\n")

print("③ NAMED CLASSICAL RESULTS WITHOUT A SOURCE — the bake-hygiene check")
# a named result is a proper-noun-bearing phrase; each should have a \cite in its sentence
named = [r"Cayley--Klein", r"equianharmonic", r"Lyapunov", r"Rindler", r"Möbius", r"M\\\"obius",
         r"stereographic", r"gnomonic", r"Segre", r"Klein correspondence", r"Casey",
         r"Ptolemy", r"La Hire", r"Euler's", r"Segre symbol"]
u0 = 0
for f in papers:
    s = open(f, encoding='utf-8', errors='replace').read()
    body = s.split('\\begin{thebibliography}')[0]
    # strip LaTeX comment lines: mastheads are not the paper
    body = '\n'.join(ln for ln in body.split('\n') if not ln.lstrip().startswith('%'))
    for pat in named:
        for m in re.finditer(pat, body):
            # a named result needs a source SOMEWHERE in the paper, not in every sentence
            occ = [mm.start() for mm in re.finditer(pat, body)]
            anywhere = any(re.search(r'\\cite\{|\\rcpt\{',
                            body[max(0, o-400):o+400]) for o in occ)
            lo = body.rfind('.', 0, m.start()) + 1
            hi = body.find('.', m.end())
            sent = body[lo:hi if hi > 0 else m.end()+200]
            if not anywhere:
                print(f"   ⚠ {os.path.basename(f)[:24]:26s} '{pat[:18]}' uncited: "
                      f"{re.sub(chr(92)+'s+',' ',sent)[:90]}")
                u0 += 1; bad += 1
            break
print(f"   → {u0} named result(s) with no source in their sentence\n")
print("CLEAN" if bad == 0 else f"{bad} ISSUE(S)")
sys.exit(0 if bad == 0 else 1)
PYEOF
