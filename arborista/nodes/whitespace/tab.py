"""A tab character."""
from typing import Any

from arborista.nodes.whitespace.whitespace import Whitespace


class Tab(Whitespace):
    """A tab character."""
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Tab)

    def __str__(self) -> str:
        return '\t'
