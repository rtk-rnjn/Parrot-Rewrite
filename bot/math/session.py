from __future__ import annotations

from collections.abc import Hashable, Mapping
from typing import Protocol

from sympy import Expr


class VariableStore(Protocol):
    """Storage interface for scoped mathematical variables."""

    def get(self, scope: Hashable) -> Mapping[str, Expr]:
        ...

    def set(self, scope: Hashable, name: str, value: Expr) -> None:
        ...


class InMemoryVariableStore:
    """In-memory scoped variable storage.

    The scope key is intentionally generic so the caller can later switch from
    user IDs to guild/channel IDs without changing the parser or evaluator.
    """

    def __init__(self) -> None:
        self._scopes: dict[Hashable, dict[str, Expr]] = {}

    def get(self, scope: Hashable) -> Mapping[str, Expr]:
        return self._scopes.get(scope, {})

    def set(self, scope: Hashable, name: str, value: Expr) -> None:
        self._scopes.setdefault(scope, {})[name] = value

    def clear(self, scope: Hashable) -> None:
        self._scopes.pop(scope, None)
