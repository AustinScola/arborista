"""A string of characters."""
from typing import Any, Optional

from arborista.decorators.equality.equal_type import equal_type
from arborista.node import Node


class String(Node):
    """A string of characters."""
    def __init__(self, value: str = '', parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: str = value

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.value == other.value
        return equality
