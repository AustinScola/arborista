"""A Python joined string."""
from typing import Any, Iterable, Iterator, List, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.string import String


class JoinedString(Expression):
    """A Python joined string."""
    def __init__(self, strings: Iterable[String], parent: Optional[Node] = None):
        super().__init__(parent)

        self.strings: List[String] = list(strings)

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.strings != other.strings:
            return False

        return True

    def iterate_children(self) -> Iterator[String]:
        yield from self.strings
