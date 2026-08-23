#!/usr/bin/env python3
"""make_receipt_appendix.py -- generate 'Appendix R -- Computational Receipts' from receipts/INDEX.md.
Single source of truth: the paper's appendix can never drift from the ledger, because it is regenerated.
Usage:  python3 make_receipt_appendix.py <PAPER|corpus> <out.tex>
  <PAPER> e.g. P1 -> that paper's rows, PLUS any receipt that paper's .tex actually cites with
          \rcpt{} but which is registered to another paper (marked 'borrowed from Pn').
  corpus  -> every row, deduplicated by stem (the book appendix).
  Cross-paper support added r1620: before it, a \rcpt{} marker naming another paper's receipt
  had no label in a standalone build, and the only fixes available were a hand-added appendix
  entry (which drifts from the ledger and is destroyed by the next regeneration -- this happened
  at r1612) or a duplicate ledger row (which multiply-defines the label in the book build).
  Both were workarounds for this gap; the ledger stays the single source of truth instead.
Each row -> a labelled \\item[...]{rcpt:<stem>} so \\rcpt{<stem>} in the body links to it."""
import sys, re, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import index_rows        # ** c54.222: the row filter lives ONCE now.  See its head. **
def parse_index(path):
    """The INDEX carries TWO row formats and this reads both.
       (a) | paper | label | claim | path | status | computes | bound | origin |
       (b) | `stem` | paper §label -- claim | detail | path | status | computes | bound | origin |
    Format (b) -- twenty rows, the storyboard bake -- was INVISIBLE to every reader of this
    file until r2376+c54.36, because the filter was ln.startswith('| P') and (b) opens with a
    backtick.  Those receipts were registered, on disk, and absent from every appendix."""
    # ** r2533+c54.203: SAME CASE-SENSITIVITY HOLE AS check_receipts, in the generator. **  The
    # ** filter was `ln.startswith('| P')` and the geometric core paper is written `p0` in
    # ** LOWERCASE, so all nine of its INDEX rows were dropped from every appendix.  The comment
    # ** twenty lines above records this filter causing exactly this class of loss once before
    # ** (r2376+c54.36, the '| `stem`' format) -- and the fix then did not cover the case. **
    #
    # ** \u26ed\u26ed c54.222, AND IT IS THE SAME FILTER A THIRD TIME. **  The paper column also holds an
    # ** EM-DASH for a receipt supporting no paper, and those twenty rows were dropped here too.
    # ** The predicate is gone rather than patched again -- `corpus/index_rows.py` holds it once. **
    #
    # ** \u26d4 AND A GENERATOR-SPECIFIC HALF: THIS FILE EMITTED A ROW'S STATUS CELL AS THE VERDICT AND
    # ** NEVER LOOKED FOR THE FILE. **  Two rows carrying `\u2714\u2714` and `run rNNNN, rc=0` named a `.py`
    # ** that has never existed in any commit, and both were printed into P3's, P7's and the corpus
    # ** appendix marked `[OK]`.  *** A generated appendix inherits the ledger's errors and dresses
    # ** them as verification. ***  Unresolvable rows are now REFUSED here, loudly, as well as being
    # ** failed by `check_receipts`: a generator that can print a false `[OK]` is a second mouth. **
    rows=[]
    _root=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(path)),'..'))
    _missing=[]
    for r in index_rows.rows(index=path, resolve_paths=True, root=_root):
        cells=r.cells
        if len(cells) < 6: continue
        if r.paper.startswith('`'):                    # format (b): cell 0 is the stem
            head = cells[1]
            m = re.match(r'\s*(p0|P\d+)\b[\s]*(.*)', head)
            paper = m.group(1) if m else ''
            label = (m.group(2) if m else head).lstrip(' \u00a7').strip()
            claim, rcpt, status, computes = head, cells[3], cells[4], cells[5]
        else:
            paper,label,claim,rcpt,status,computes = cells[0],cells[1],cells[2],cells[3],cells[4],cells[5]
        bound = cells[6] if len(cells)>6 else ''
        stem = r.stem
        if r.runnable and not r.paths:
            _missing.append((r.lineno, r.token)); continue
        _pth=r.token
        if _pth.startswith('receipts/'): _pth=_pth[len('receipts/'):]
        rows.append(dict(paper=paper,label=label,claim=claim,stem=stem,status=status,computes=computes,bound=bound,path=_pth))
    if _missing:
        sys.stderr.write('\n  \u26d4 REFUSING TO EMIT %d ROW(S) WHOSE FILE DOES NOT EXIST:\n' % len(_missing))
        for lineno, tok in _missing:
            sys.stderr.write('     receipts/INDEX.md line %d: %s\n' % (lineno, tok))
        sys.stderr.write('     ** A reproducibility appendix that lists a computation nobody can run is'
                         ' worse than one that omits it. **\n\n')
    return rows
_ASCII=[('\\',r'\textbackslash{}'),('{',r'\{'),('}',r'\}'),('#',r'\#'),('&',r'\&'),('%',r'\%'),('$',r'\$'),('_',r'\_'),('^',r'\textasciicircum{}'),('|',r'\textbar{}'),('~',r'\textasciitilde{}')]
_UNI={'§':r'\S{}','°':r'\ensuremath{^\circ}','¹':r'\textsuperscript{1}','²':r'\textsuperscript{2}','³':r'\textsuperscript{3}','⁴':r'\textsuperscript{4}','⁶':r'\textsuperscript{6}','¼':r'\ensuremath{\tfrac14}','½':r'\ensuremath{\tfrac12}','¾':r'\ensuremath{\tfrac34}','⅓':r'\ensuremath{\tfrac13}','×':r'\ensuremath{\times}','—':'---','′':r'\ensuremath{{}^\prime}','−':r'\ensuremath{-}','Λ':r'\ensuremath{\Lambda}','α':r'\ensuremath{\alpha}','β':r'\ensuremath{\beta}','η':r'\ensuremath{\eta}','θ':r'\ensuremath{\theta}','π':r'\ensuremath{\pi}','ρ':r'\ensuremath{\rho}','σ':r'\ensuremath{\sigma}','τ':r'\ensuremath{\tau}','ψ':r'\ensuremath{\psi}','₀':r'\ensuremath{_0}','₂':r'\ensuremath{_2}','→':r'\ensuremath{\to}','↔':r'\ensuremath{\leftrightarrow}','↦':r'\ensuremath{\mapsto}','⇒':r'\ensuremath{\Rightarrow}','⟺':r'\ensuremath{\iff}','∀':r'\ensuremath{\forall}','∅':r'\ensuremath{\emptyset}','∘':r'\ensuremath{\circ}','·':r'\ensuremath{\cdot}','√':r'\ensuremath{\surd}','∞':r'\ensuremath{\infty}','⋆':r'\ensuremath{\star}','◐':'(partial)','✔':'','✗':'(x)','✘':'(x)','†':r'\textdagger{}','̃':'', '–':'--', '⊢':r'\ensuremath{\vdash}', 'κ':r'\ensuremath{\kappa}', 'λ':r'\ensuremath{\lambda}', '∓':r'\\ensuremath{\\mp}', '±':r'\ensuremath{\pm}', 'γ':r'\ensuremath{\gamma}', 'δ':r'\ensuremath{\delta}', 'μ':r'\ensuremath{\mu}', 'ν':r'\ensuremath{\nu}', 'φ':r'\ensuremath{\varphi}', 'ω':r'\ensuremath{\omega}', 'Δ':r'\ensuremath{\Delta}', 'Ω':r'\ensuremath{\Omega}', '≤':r'\ensuremath{\le}', '≥':r'\ensuremath{\ge}', '≠':r'\ensuremath{\ne}', '≡':r'\ensuremath{\equiv}', '⊂':r'\ensuremath{\subset}', '∈':r'\ensuremath{\in}', '→':r'\ensuremath{\to}', '‘':"`", '’':"'", '“':"``", '”':"''", '₊':r'\ensuremath{_+}', '₋':r'\ensuremath{_-}', '₁':r'\ensuremath{_1}', '₃':r'\ensuremath{_3}', '₄':r'\ensuremath{_4}', '₅':r'\ensuremath{_5}', '₆':r'\ensuremath{_6}', '⁵':r'\textsuperscript{5}', '⁷':r'\textsuperscript{7}', '⁰':r'\textsuperscript{0}', '⁻':r'\ensuremath{^-}', '⁺':r'\ensuremath{^+}', '∂':r'\ensuremath{\partial}', '∇':r'\ensuremath{\nabla}', '⊗':r'\ensuremath{\otimes}', '⊕':r'\ensuremath{\oplus}', 'Σ':r'\ensuremath{\Sigma}', 'ε':r'\ensuremath{\epsilon}', 'ζ':r'\ensuremath{\zeta}', 'χ':r'\ensuremath{\chi}', 'Γ':r'\ensuremath{\Gamma}', 'ℓ':r'\ensuremath{\ell}', 'ℏ':r'\ensuremath{\hbar}', '∫':r'\ensuremath{\int}', '…':r'\ldots{}', ' ':' ',
# ** THE REGISTERS' OWN MARKER GLYPHS, ADDED r2441+c54.188. **  They are emphasis in a register and
# carry no content a paper needs, so they degrade to nothing rather than to a symbol.  Before this
# the generator emitted them verbatim and LaTeX failed three hundred lines into a log with 'Unicode
# character not set up for use with LaTeX' -- a failure whose cause is nowhere near its report.
'⌗':'', '⚠':'', '⛭':'', '⛔':'', '⚑':'', '⌘':'', '⟐':'',
'⓵':'(1)', '⓶':'(2)', '⓷':'(3)', '⓸':'(4)', '⓹':'(5)',
'①':'(1)', '②':'(2)', '③':'(3)', '④':'(4)', '⑤':'(5)',
'⛯':'', '❓':'', '⇑':'', '⇓':'', '⇐':r'\ensuremath{\Leftarrow}',
# ** CIRCLED LATIN LETTERS, ADDED r2501+c54.197. **  The mathematics-reach stations (r2490-2493)
# label themselves Ⓐ-Ⓗ, so they are CONTENT and not register emphasis: a station's letter is how
# every cross-reference names it, and degrading it to nothing would leave 'station  walked'.
# ** The phase-3 guard caught these -- which is the guard doing exactly its job, four appendices
# ** before pdflatex would have. **
'Ⓐ':'(A)', 'Ⓑ':'(B)', 'Ⓒ':'(C)', 'Ⓓ':'(D)', 'Ⓔ':'(E)', 'Ⓕ':'(F)', 'Ⓖ':'(G)', 'Ⓗ':'(H)',
'Ⓘ':'(I)', 'Ⓙ':'(J)', 'Ⓚ':'(K)', 'Ⓛ':'(L)', 'Ⓜ':'(M)', 'Ⓝ':'(N)', 'Ⓞ':'(O)', 'Ⓟ':'(P)'}
def tex_escape(s):
    for a,b in _ASCII: s=s.replace(a,b)      # phase 1: ASCII specials -> text escapes
    for a,b in _UNI.items(): s=s.replace(a,b)      # phase 2: unicode -> LaTeX (inserted after, not re-escaped)
    # ** phase 3, added r2441+c54.188: NOTHING UNTRANSLATED LEAVES THIS FUNCTION. **  Any character
    # above Latin-1 that phase 2 did not handle reaches pdflatex verbatim and fails there, hundreds
    # of lines into a log, with a message that names the glyph but not the row it came from.
    # ** Failing HERE names both. **  Add the glyph to _UNI; do not delete this check.
    _left = sorted({c for c in s if ord(c) > 0xFF})
    if _left:
        raise SystemExit(
            'make_receipt_appendix: %d glyph(s) with no _UNI translation would reach LaTeX '
            'verbatim: %s\n  in: %s\n  Add them to _UNI (empty string if register emphasis).'
            % (len(_left), ' '.join('U+%04X %s' % (ord(c), c) for c in _left), s[:160]))
    return s
def one_state(s):
    """Print the row's CURRENT state only.

    The index is a ledger and keeps superseded readings on purpose (the dead branch
    is the shape of the maze).  A paper's appendix presents ONE state.  So the
    ledger keeps the 'Original claim:' tail and the generator stops printing it.
    """
    if not s:
        return s
    i = s.find('Original claim:')
    return s[:i].rstrip().rstrip(';,.') if i > 0 else s


def emit(rows, scope, out):
    title = "Appendix R\\quad Computational Receipts" if scope=='corpus' else "Appendix R\\quad Computational Receipts"
    L=[]
    L.append("\\clearpage")
    L.append("\\section*{%s}\\label{app:receipts}" % title)
    L.append("\\addcontentsline{toc}{section}{Appendix R: Computational Receipts}")
    L.append("\\small\\noindent Each computation marked \\rcptmarker\\ in the text is verified by a runnable receipt in the \\texttt{receipts/} directory that ships with this work; status \\textsf{OK} = verified (traced, run, output matches the claim). This appendix is generated from the receipt index, not maintained by hand.\\par\\medskip")
    L.append("\\begingroup\\renewcommand{\\arraystretch}{1.25}")
    L.append("\\begin{description}")
    for r in rows:
        stem_tex = tex_escape(r['stem'])
        st = 'OK' if '✔' in r['status'] else tex_escape(r['status'])
        L.append("\\item[\\label{rcpt:%s}\\texttt{%s}]\\hfill\\textsf{[%s]}\\\\" % (r['stem'], stem_tex, st))
        L.append("\\textit{%s} \\ (%s). %s" % (tex_escape(r['label']), tex_escape(one_state(r['claim'])), ''))
        L.append("\\emph{Computes:} %s" % tex_escape(one_state(r['computes'])))
        if r['bound']:
            L.append(" \\emph{Bound:} %s" % tex_escape(one_state(r['bound'])))
        L.append("\\ \\emph{Run:} \\texttt{python3 receipts/%s}" % tex_escape(r['path']))
    L.append("\\end{description}\\endgroup")
    open(out,'w').write("\n".join(L)+"\n")
    print("wrote %s (%d receipts, scope=%s)" % (out, len(rows), scope))
if __name__=='__main__':
    scope, out = sys.argv[1], sys.argv[2]
    idx = os.path.join(os.path.dirname(__file__),'..','receipts','INDEX.md')
    rows = parse_index(idx)
    if scope!='corpus':
        own = [r for r in rows if r['paper']==scope]
        # cross-paper markers: include rows this paper's own source actually cites
        src = {'P1':'BH_causality_v2','P2':'janzen_circle_v3','P3':'SdS-slicing-curve_v2',
               'P4':'modern_parallax','P5':'groupoid_paper','P6':'shadow_of_existence',
               'P7':'CR_framework','P8':'slicing_operator','P9':'range_paper',
               'P10':'canonical_time','P11':'dynamics_paper','P12':'algebroid_paper',
               'P13':'boundary_paper','P14':'matter_sector_paper','P15':'CR_cosmology',
               'P16':'cosmogenesis_paper','p0':'geometric_core_paper',
               # r2376+c54.41: P17 was absent from this map, so the geometric-core paper's
               # appendix could borrow nothing and any cross-paper \rcpt{} in it rendered dead.
               'P17':'geometric_core_paper'}.get(scope)
        cited=set()
        if src and os.path.exists(src+'.tex'):
            body='\n'.join(l for l in open(src+'.tex',encoding='utf-8',errors='replace')
                            .read().split('\n') if not l.lstrip().startswith('%'))
            cited={m.group(1) for m in re.finditer(r'\\rcpt\{([A-Za-z0-9_]+)\}', body)}
        have={r['stem'] for r in own}
        borrowed=[dict(r, claim=r['claim']+(' [borrowed from %s]'%r['paper']))
                  for r in rows if r['stem'] in cited and r['stem'] not in have]
        rows = own + borrowed
        if borrowed:
            print('  (+%d borrowed: %s)' % (len(borrowed), ', '.join(b['stem'] for b in borrowed)))
        # r2377: the corpus branch below has always deduped by stem; this one did not, so a
        # duplicate ledger row (or one stem borrowed from two papers) emitted \label{rcpt:<stem>}
        # twice and multiply-defined it -- \rcpt{} then resolved to whichever came last.  Same
        # rule, same place: first row for a stem wins.
        seen = set(); ded = []
        for r in rows:
            if r['stem'] in seen: continue
            seen.add(r['stem']); ded.append(r)
        if len(ded) != len(rows):
            print('  (deduped %d duplicate stem(s))' % (len(rows) - len(ded)))
        rows = ded
    else:
        seen=set(); ded=[]
        for r in rows:
            if r['stem'] in seen: continue
            seen.add(r['stem']); ded.append(r)
        if len(ded)!=len(rows):
            print('  (deduped %d duplicate stem(s))' % (len(rows)-len(ded)))
        rows = ded
    emit(rows, scope, out)
