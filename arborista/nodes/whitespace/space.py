"""A space character."""
from typing import Any

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.nodes.whitespace.whitespace import Whitespace


class Space(Whitespace):
    """A space character."""
    @equal_type
    def __eq__(self, other: Any) -> bool:
        return True

    def __str__(self) -> str:
        return ' '
