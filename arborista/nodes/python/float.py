"""A Python float."""
from typing import Any, Optional

from arborista.node import Node
from arborista.nodes.python.number import Number


class Float(Number):
    """A Python float."""
    def __init__(self, value: float, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: float = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Float):
            return False
        return self.value == other.value
