#!/usr/bin/env python3
"""check_explainer_pins.py -- THE EXPLAINER MAY NOT FALL BEHIND THE WORK WITHOUT SOMEONE NOTICING.

** THE ERROR THIS EXISTS FOR. **  `EXPLAINER.md` is the plain-language account of the whole picture, and the
README makes it the last read of every spin-up: it is the map a new reader, or a fresh node, takes as where
the work stands.  Most of it is geometry and does not move.  A few passages state where an open question
sits, or quote a number a fit produces -- and those go stale the moment the work moves, silently, because
nothing ties the prose to the row or the paper it was written from.  A stale map read last is worse than
none: it is the picture the reader leaves with.

** THE PIN. **  Each time-sensitive paragraph carries a marker on its own line, directly above it:

    <!-- watch: <id> | rows: PO-75@1a2b3c4d PO-31@5e6f7a8b | in corpus/CR_cosmology.tex: "10^{113}" -->

  rows:   register rows the passage was written from, each with the first 8 hex of the SHA-256 of that
          row's line in THE_REGISTER.md (whitespace-collapsed) AS IT STOOD WHEN THE PASSAGE WAS LAST READ
          AGAINST IT.  Struck or open, the line is digested as it stands.
  in:     literals that must still be present in the named file -- the number or phrase the passage
          paraphrases.  Repeatable, one per `in` clause, double-quoted.  A literal may name a SECTION
          as well as a file, which restricts both the search and the uniqueness requirement to it:

              in corpus/CR_cosmology.tex#sec:transmission: "the crossing accumulates no divergent phase"

** AND A PIN MUST NAME ONE SITE, WHICH IS WHAT `r7183+70.1` MEASURED AND `r7189` ENFORCES. **  A literal
that occurs more than once in its scope is a pin on the FILE and not on the CLAIM: the sentence it was
written for can be deleted and the pin stays green on an unrelated copy.  That is not hypothetical --
`r7183` removed `P15`'s projection-distance claim and the explainer's pin on `by three independent
routes` stayed green, because another section carried the same four words about a different quantity.
Node 70 then counted the class: 139 of 722 receipt pins and 8 of 18 of this file's pins were multi-site,
and a section scope alone would single-site only 47 per cent of them, the rest repeating inside one
section.  So the scope and the uniqueness requirement are both needed and both are enforced here: a
literal occurring twice is a FAILURE, whether or not a section is named, and the remedy is to name a
section or to lengthen the literal until it names one site.

  sec:    a whole SECTION of a paper, stamped like a row:

              sec corpus/CR_cosmology.tex#sec:refit-bound@1a2b3c4d

          For a passage that tracks a paper's live edge.  A literal sees only the sentence it was hung on:
          claims ADDED beside it leave it green (r7217, and again r7221 -- the same blindness twice).
          A section stamp fires on any change to the section's text, so additions are seen too.  It is
          deliberately coarse: use it only where the passage follows work that moves every revision,
          and expect a reread each time it does.

  The marker is an HTML comment, so the page generator skips it (`md_to_html`, which escapes `<` in prose,
  drops comment lines instead of printing them).

** WHAT FAILS. **
  MOVED      a pinned row's line, or a pinned section's text, no longer digests to its stamp.
  GONE       a pinned row is no longer in the register, or a pinned file is gone.
  DROPPED    a pinned literal is no longer in its file -- the number or wording the passage rests on changed.
  MULTISITE  a pinned literal occurs more than once in its scope, so the pin is on the file and not on the
             claim.  Remedy: name a section, or lengthen the literal until it names one site.
  NOSECTION  a pinned literal names a section label that does not resolve to exactly one `\\label{...}`.
  MALFORMED  a marker that does not parse, carries an unstamped row, or does not sit directly above a
             paragraph; or a `<!--` anywhere but at the start of its own line (the generator would print it).

** WHAT TO DO WHEN IT FIRES. **  Read the row (or the paper at the literal) as it now stands, then reread the
passage against it.  Revise the passage if the picture moved; leave it if it did not.  Then:
      python3 corpus/check_explainer_pins.py --restamp <id>     (re-digests that marker's rows)
  A DROPPED literal is not restamped: the pin itself changes -- point it at the new figure once the passage
  says what the paper now says.  The restamp is the record that the passage was reread, so it is never run
  without the read.

      --list      every watch, with its passage's opening words and current status.
"""
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPL = os.path.join(ROOT, 'EXPLAINER.md')
REG = os.path.join(ROOT, 'THE_REGISTER.md')

MARK = re.compile(r'^<!--\s*watch:\s*(.*?)\s*-->\s*$')
ROWPIN = re.compile(r'^(PO-\d+)@([0-9a-f]{8}|-{8})$')
SECPIN = re.compile(r'^sec\s+([^\s#]+)#([A-Za-z0-9:_\-]+)@([0-9a-f]{8}|-{8})$')
INCL = re.compile(r'^in\s+([^\s#:]+?)(?:#([A-Za-z0-9:_\-]+))?:\s*"([^"]+)"$')
SECCMD = re.compile(r'\\(?:sub)*section\*?\s*\{')


def section_body(text, label):
    """The named section's own text, or (None, why) if the label does not resolve to exactly one site.

    Scope runs from the \\label{...} to the next sectioning command of any depth, which is the
    conservative reading: a subsection's scope ends at the next subsection, and a section's ends at
    its first subsection.  A pin that needs to reach across a subsection boundary should name the
    subsection it is actually in."""
    hits = [m for m in re.finditer(r'\\label\{' + re.escape(label) + r'\}', text)]
    if len(hits) != 1:
        return None, f'resolves to {len(hits)} \\label{{{label}}} sites, not 1'
    start = hits[0].end()
    nxt = SECCMD.search(text, start)
    return text[start:nxt.start() if nxt else len(text)], None


def norm(s):
    return ' '.join(s.split())


def digest(line):
    return hashlib.sha256(norm(line).encode('utf-8')).hexdigest()[:8]


def register_rows():
    rows = {}
    with open(REG, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'^\|\s*(?:~~)?\*\*(PO-\d+)\*\*(?:~~)?\s*\|', line)
            if m:
                rows.setdefault(m.group(1), []).append(line.rstrip('\n'))
    return rows


def parse(lines):
    """-> (watches, errors). Each watch: dict(id, line, rows[(po, stamp)], lits[(path, lit)], passage)."""
    watches, errors, seen = [], [], set()
    for i, raw in enumerate(lines):
        st = raw.strip()
        if '<!--' in raw and not st.startswith('<!--'):
            errors.append(f'MALFORMED  line {i+1}: `<!--` inside prose; the generator would print it')
            continue
        if not st.startswith('<!--'):
            continue
        if not st.endswith('-->'):
            errors.append(f'MALFORMED  line {i+1}: a comment must open and close on its own line')
            continue
        m = MARK.match(st)
        if not m:
            continue  # an ordinary comment: skipped by the generator, not a pin
        parts = [p.strip() for p in m.group(1).split('|')]
        wid = parts[0]
        w = dict(id=wid, line=i + 1, rows=[], lits=[], secs=[], passage='')
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', wid):
            errors.append(f'MALFORMED  line {i+1}: watch id {wid!r} must be lower-case words joined by hyphens')
        if wid in seen:
            errors.append(f'MALFORMED  line {i+1}: watch id {wid!r} is used twice')
        seen.add(wid)
        for p in parts[1:]:
            if p.startswith('rows:'):
                for tok in p[5:].split():
                    rm = ROWPIN.match(tok)
                    if not rm:
                        errors.append(f'MALFORMED  [{wid}] row pin {tok!r}: write PO-n@<8 hex>')
                    else:
                        w['rows'].append((rm.group(1), rm.group(2)))
            elif p.startswith('sec '):
                sm = SECPIN.match(p)
                if not sm:
                    errors.append(f'MALFORMED  [{wid}] {p!r}: write sec <path>#<label>@<8 hex>')
                else:
                    w['secs'].append((sm.group(1), sm.group(2), sm.group(3)))
            elif p.startswith('in '):
                im = INCL.match(p)
                if not im:
                    errors.append(f'MALFORMED  [{wid}] {p!r}: write in <path>: "<literal>"')
                else:
                    w['lits'].append((im.group(1), im.group(2), im.group(3)))
            else:
                errors.append(f'MALFORMED  [{wid}] unknown clause {p!r}')
        if not w['rows'] and not w['lits'] and not w['secs']:
            errors.append(f'MALFORMED  [{wid}] pins nothing')
        nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
        if not nxt or nxt.startswith('#') or nxt.startswith('<!--'):
            errors.append(f'MALFORMED  [{wid}] must sit directly above the paragraph it watches')
        else:
            w['passage'] = nxt
        watches.append(w)
    return watches, errors


def opening(text, n=90):
    t = re.sub(r'[*`]', '', text)
    return t if len(t) <= n else t[:n].rsplit(' ', 1)[0] + '…'


def evaluate(w, rows, cache):
    probs = []
    for po, stamp in w['rows']:
        cur = rows.get(po)
        if not cur:
            probs.append(f'GONE     {po} is no longer a row of THE_REGISTER.md')
        elif len(cur) > 1:
            probs.append(f'MALFORMED {po} appears {len(cur)} times in THE_REGISTER.md; the pin is ambiguous')
        elif stamp == '-' * 8:
            probs.append(f'UNSTAMPED {po}: read it against the passage, then --restamp {w["id"]}')
        elif digest(cur[0]) != stamp:
            struck = cur[0].lstrip('| ').startswith('~~')
            probs.append(f'MOVED    {po} has changed since the passage was read against it'
                         + (' (it is now STRUCK)' if struck else ''))
    for path, sec, stamp in w.get('secs', []):
        full = os.path.join(ROOT, path)
        if path not in cache:
            cache[path] = open(full, encoding='utf-8').read() if os.path.isfile(full) else None
        if cache[path] is None:
            probs.append(f'GONE     {path} does not exist')
            continue
        body, why = section_body(cache[path], sec)
        if body is None:
            probs.append(f'NOSECTION {path}#{sec}: {why}')
        elif stamp == '-' * 8:
            probs.append(f'UNSTAMPED {path}#{sec}: read it against the passage, then --restamp {w["id"]}')
        elif digest(body) != stamp:
            probs.append(f'MOVED    {path}#{sec} has changed since the passage was read against it')
    for path, sec, lit in w['lits']:
        full = os.path.join(ROOT, path)
        if path not in cache:
            cache[path] = open(full, encoding='utf-8').read() if os.path.isfile(full) else None
        if cache[path] is None:
            probs.append(f'GONE     {path} does not exist')
            continue
        where = path + (('#' + sec) if sec else '')
        hay = cache[path]
        if sec:
            hay, why = section_body(cache[path], sec)
            if hay is None:
                probs.append(f'NOSECTION {where}: {why}')
                continue
        n = hay.count(lit)
        if n == 0:
            probs.append(f'DROPPED  "{lit}" is no longer in {where}')
        elif n > 1:
            probs.append(f'MULTISITE "{lit}" occurs {n} times in {where} -- the pin is on the '
                         f'{"section" if sec else "file"} and not on the claim.  '
                         + ('Lengthen the literal until it names one site.' if sec
                            else 'Name a section with #sec:label, or lengthen the literal.'))
    return probs


def restamp(ids, lines, watches, rows):
    want = set(ids)
    hit = set()
    for w in watches:
        if w['id'] not in want:
            continue
        hit.add(w['id'])
        new = []
        for po, _ in w['rows']:
            cur = rows.get(po)
            if not cur or len(cur) != 1:
                sys.exit(f'⛔ [{w["id"]}] {po} cannot be stamped: it is not exactly one row of the register')
            new.append(f'{po}@{digest(cur[0])}')
        newsec = {}
        for path, sec, _ in w.get('secs', []):
            txt = open(os.path.join(ROOT, path), encoding='utf-8').read()
            body, why = section_body(txt, sec)
            if body is None:
                sys.exit(f'⛔ [{w["id"]}] {path}#{sec} cannot be stamped: {why}')
            newsec[(path, sec)] = f'sec {path}#{sec}@{digest(body)}'
        old = lines[w['line'] - 1]
        body = MARK.match(old.strip()).group(1)
        parts = [p.strip() for p in body.split('|')]
        parts = [('rows: ' + ' '.join(new)) if p.startswith('rows:') else p for p in parts]
        def _sec(p):
            sm = SECPIN.match(p)
            return newsec[(sm.group(1), sm.group(2))] if sm else p
        parts = [_sec(p) for p in parts]
        lines[w['line'] - 1] = '<!-- watch: ' + ' | '.join(parts) + ' -->'
        print(f'restamped [{w["id"]}]: ' + ' '.join(new + list(newsec.values())))
    missing = want - hit
    if missing:
        sys.exit('⛔ no such watch: ' + ', '.join(sorted(missing)))
    with open(EXPL, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main(argv):
    with open(EXPL, encoding='utf-8') as f:
        text = f.read()
    lines = text.split('\n')
    watches, errors = parse(lines)
    rows = register_rows()

    if argv[:1] == ['--restamp']:
        if errors:
            print('\n'.join(errors))
            sys.exit('⛔ fix the malformed markers before restamping')
        if len(argv) < 2:
            sys.exit('usage: check_explainer_pins.py --restamp <id> [<id> ...]')
        restamp(argv[1:], lines, watches, rows)
        return 0

    cache, fails = {}, 0
    for w in watches:
        probs = evaluate(w, rows, cache)
        if argv[:1] == ['--list']:
            state = 'ok' if not probs else probs[0].split()[0]
            print(f'{w["id"]:<22} {state:<9} line {w["line"]:<4} {opening(w["passage"], 70)}')
            continue
        if probs:
            fails += 1
            print(f'⛔ [{w["id"]}] EXPLAINER.md line {w["line"] + 1}: “{opening(w["passage"])}”')
            for p in probs:
                print('     ' + p)
    if argv[:1] == ['--list']:
        for e in errors:
            print(e)
        return 1 if errors else 0
    for e in errors:
        print('⛔ ' + e)
    if fails or errors:
        print('\nThe explainer may be behind the work.  Read what moved, reread the passage against it, revise it if\n'
              'the picture changed, then:  python3 corpus/check_explainer_pins.py --restamp <id>\n'
              '(A DROPPED literal is re-pointed, not restamped.  The restamp records the reread; never run it without one.)')
        return 1
    print(f'✓ explainer pins: {len(watches)} watched passages, '
          f'{sum(len(w["rows"]) for w in watches)} row pins, {sum(len(w["lits"]) for w in watches)} literal pins, '
          f'{sum(len(w.get("secs", [])) for w in watches)} section pins -- all current')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
