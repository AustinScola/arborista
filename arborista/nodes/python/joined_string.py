"""A Python joined string."""
from typing import Iterable, Iterator, List, Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.string import String


class JoinedString(Expression):
    """A Python joined string."""
    def __init__(self, strings: Iterable[String], parent: Optional[Node] = None):
        super().__init__(parent)

        self.strings: List[String] = list(strings)

    def iterate_children(self) -> Iterator[String]:
        yield from self.strings
