"""A Python name."""
from typing import Any, Optional

from arborista.node import Node
from arborista.nodes.python.atom import Atom


class Name(Atom):
    """A Python name."""
    def __init__(self, value: str, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Name):
            return False
        return self.value == other.value
