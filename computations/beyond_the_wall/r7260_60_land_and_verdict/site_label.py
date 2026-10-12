"""for a (receipt, literal) key, the receipt's OWN LABEL at the asserting site -- so a verdict is
entered against what the receipt says it is checking, not against the literal alone.

Walks the AST, finds every call whose argument list contains the literal (as a whole string constant
or as a piece of an implicitly concatenated one), and returns that call's FIRST argument rendered
back to text when it is a constant or a concatenation of constants, or an f-string's literal parts.
"""
import ast
import os


def _const_text(node):
    """the literal text of a string expression, or None when it is not one"""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):                      # f-string: keep its literal parts
        out = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                out.append(v.value)
            else:
                out.append('{…}')
        return ''.join(out)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = _const_text(node.left), _const_text(node.right)
        return None if a is None or b is None else a + b
    return None


def _strings_in(node):
    for n in ast.walk(node):
        if isinstance(n, ast.Constant) and isinstance(n.value, str):
            yield n.value


def labels_for(path, literal):
    """every (label, call-name, lineno) whose argument list mentions the literal"""
    try:
        tree = ast.parse(open(path, encoding='utf-8').read())
    except SyntaxError:
        return []
    out = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        if not any(literal == s or literal in s for s in _strings_in(n)):
            continue
        name = getattr(n.func, 'id', getattr(n.func, 'attr', '?'))
        lab = None
        for a in n.args:
            lab = _const_text(a)
            if lab:
                break
        out.append((lab or '(no literal label)', name, n.lineno))
    # the innermost call mentioning it is the asserting site; outer ones wrap it
    return sorted(out, key=lambda t: -t[2])


def best_label(root, receipt, literal):
    for lab, name, line in labels_for(os.path.join(root, receipt), literal):
        if name in ('check', 'gate', 'g', 'assert_', 'require', 'ok'):
            return lab, name, line
    got = labels_for(os.path.join(root, receipt), literal)
    return got[0] if got else ('(site not found)', '-', 0)
