"""A string of characters."""
from typing import Any, Optional

from arborista.node import Node


class String(Node):
    """A string of characters."""
    def __init__(self, value: str = '', parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, String):
            return False

        return self.value == other.value
