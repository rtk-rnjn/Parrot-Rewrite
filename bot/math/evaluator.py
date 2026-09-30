from __future__ import annotations

from typing import Hashable

import sympy

from .parser import Assignment, Expression, MathParseError, parse_input
from .session import VariableStore


class EvaluationError(ValueError):
    """Raised when a parsed expression cannot be evaluated safely."""


def _format_value(value: sympy.Expr) -> str:
    if value.count_ops() > 500:
        raise EvaluationError("Expression is too complicated.")

    return sympy.sstr(value)


def evaluate_input(text: str, store: VariableStore, scope: Hashable) -> str:
    """Parse, evaluate, store assignments, and return a Discord-ready result."""
    try:
        result = parse_input(text, store, scope)
    except MathParseError as exc:
        raise EvaluationError(str(exc)) from exc

    if isinstance(result, Assignment):
        store.set(scope, result.name, result.value)
        return f"{result.name} = {_format_value(result.value)}"

    return _format_value(result.value)
