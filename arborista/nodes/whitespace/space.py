"""A space character."""
from typing import Any

from arborista.nodes.whitespace.whitespace import Whitespace


class Space(Whitespace):
    """A space character."""
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Space)

    def __str__(self) -> str:
        return ' '
