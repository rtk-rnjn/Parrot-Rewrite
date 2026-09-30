from __future__ import annotations

import re

MAX_EXPRESSION_LENGTH = 256

_IDENTIFIER_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
_FUNCTION_CALL_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*\(")
_ALLOWED_CHARS_RE = re.compile(r"^[A-Za-z0-9_+*/^().=\-\s]+$")

MATH_FUNCTIONS = frozenset({"sqrt", "sin", "cos", "tan", "log"})
MATH_CONSTANTS = frozenset({"pi", "E"})


def looks_like_math(text: str) -> bool:
    """Return whether text is plausibly a supported mathematical expression.

    This is deliberately conservative. It is only a pre-filter; the parser remains
    responsible for deciding whether the expression is actually valid.
    """
    text = text.strip()
    if not text or len(text) > MAX_EXPRESSION_LENGTH:
        return False

    if not _ALLOWED_CHARS_RE.fullmatch(text):
        return False

    if text.count("=") > 1:
        return False

    if "=" in text:
        lhs, rhs = text.split("=", 1)
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", lhs.strip()):
            return False
        if not rhs.strip():
            return True

    function_names = {match.group(1) for match in _FUNCTION_CALL_RE.finditer(text)}
    if any(name not in MATH_FUNCTIONS for name in function_names):
        return False

    identifiers = set(_IDENTIFIER_RE.findall(text))
    identifiers -= MATH_FUNCTIONS | MATH_CONSTANTS

    has_numeric_literal = bool(re.search(r"(?<![A-Za-z_])\d+(?:\.\d*)?(?:[eE][+-]?\d+)?", text))
    has_operator = bool(re.search(r"[+*/^=]", text)) or bool(re.search(r"(?<!^)-", text))

    # Reject ordinary prose such as "I ate 25 apples". A math-looking expression
    # with variables is allowed when it contains a numeric/function signal, or when
    # its variable names are short enough to make a false positive unlikely.
    if identifiers and not has_numeric_literal and not function_names and not all(len(name) <= 2 for name in identifiers):
        return False

    if has_numeric_literal or function_names or has_operator:
        return True

    # A parenthesized expression is a useful mathematical signal even without a
    # numeric literal, e.g. "(x)".
    return "(" in text and ")" in text
