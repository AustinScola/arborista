"""A Python integer."""
from typing import Any, Optional

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node
from arborista.nodes.python.number import Number


class Integer(Number):
    """A Python integer."""
    def __init__(self, value: int, parent: Optional[Node] = None):
        super().__init__(parent)
        self.value = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
