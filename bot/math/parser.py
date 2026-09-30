from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

import sympy
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication,
    parse_expr,
    standard_transformations,
)

from .detector import MAX_EXPRESSION_LENGTH
from .session import VariableStore

TRANSFORMATIONS = standard_transformations + (implicit_multiplication, convert_xor)

# Deliberately small. Adding a function later only requires updating this mapping.
ALLOWED_FUNCTIONS: dict[str, Any] = {
    "sqrt": sympy.sqrt,
    "sin": sympy.sin,
    "cos": sympy.cos,
    "tan": sympy.tan,
    "log": sympy.log,
}

ALLOWED_CONSTANTS: dict[str, Any] = {
    "pi": sympy.pi,
    "E": sympy.E,
}

# parse_expr() generates calls to these names as part of its transformations.
# Keeping the global namespace explicit avoids exposing SymPy's full namespace.
PARSER_GLOBALS: dict[str, Any] = {
    "Symbol": sympy.Symbol,
    "Integer": sympy.Integer,
    "Float": sympy.Float,
    "Rational": sympy.Rational,
    "Add": sympy.Add,
    "Mul": sympy.Mul,
    "Pow": sympy.Pow,
}

_IDENTIFIER_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_FUNCTION_CALL_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*\(")


class MathParseError(ValueError):
    """Raised when user input is outside the supported math syntax."""


@dataclass(frozen=True)
class Expression:
    value: sympy.Expr


@dataclass(frozen=True)
class Assignment:
    name: str
    value: sympy.Expr


def _validate_text(text: str) -> str:
    text = text.strip()
    if not text:
        raise MathParseError("Expression is empty.")
    if len(text) > MAX_EXPRESSION_LENGTH:
        raise MathParseError("Expression is too long.")
    if not re.fullmatch(r"[A-Za-z0-9_+*/^().=\-\s]+", text):
        raise MathParseError("Unsupported characters.")
    if "__" in text:
        raise MathParseError("Invalid identifier.")
    return text


def _parse_expression(text: str, variables: dict[str, sympy.Expr]) -> sympy.Expr:
    local_dict: dict[str, Any] = {}
    local_dict.update(ALLOWED_FUNCTIONS)
    local_dict.update(ALLOWED_CONSTANTS)
    local_dict.update(variables)

    for name in {match.group(1) for match in _FUNCTION_CALL_RE.finditer(text)}:
        if name not in ALLOWED_FUNCTIONS:
            raise MathParseError(f"Unknown function: {name}")

    try:
        result = parse_expr(
            text,
            local_dict=local_dict,
            global_dict=PARSER_GLOBALS,
            transformations=TRANSFORMATIONS,
            evaluate=True,
        )
    except (ArithmeticError, NameError, SyntaxError, TypeError, ValueError) as exc:
        raise MathParseError("Invalid mathematical expression.") from exc

    if not isinstance(result, sympy.Expr):
        raise MathParseError("Expression did not produce a mathematical value.")

    if len(result.count_ops()) if False else False:
        # Kept out of the normal path; complexity is checked by count_ops below.
        pass

    if result.count_ops() > 500:
        raise MathParseError("Expression is too complicated.")

    return result


def parse_input(text: str, store: VariableStore, scope: object) -> Expression | Assignment:
    """Parse an expression or simple variable assignment for a scope."""
    text = _validate_text(text)

    if text.count("=") > 1:
        raise MathParseError("Only simple assignments are supported.")

    variables = dict(store.get(scope))

    if "=" in text:
        lhs, rhs = text.split("=", 1)
        name = lhs.strip()
        if not _IDENTIFIER_RE.fullmatch(name or ""):
            raise MathParseError("The left side of an assignment must be a variable name.")
        if name in ALLOWED_FUNCTIONS or name in ALLOWED_CONSTANTS:
            raise MathParseError(f"Cannot assign to {name}.")
        if not rhs.strip():
            raise MathParseError("Assignment is missing a value.")

        value = _parse_expression(rhs, variables)
        return Assignment(name=name, value=value)

    return Expression(value=_parse_expression(text, variables))
