"""A Python integer."""
from typing import Any, Optional

from arborista.node import Node
from arborista.nodes.python.number import Number


class Integer(Number):
    """A Python integer."""
    def __init__(self, value: int, parent: Optional[Node] = None):
        super().__init__(parent)
        self.value = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Integer):
            return False
        return self.value == other.value
