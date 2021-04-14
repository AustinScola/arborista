"""A single quoted long string."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.long_string import LongString


class SingleQuotedLongString(LongString):
    """A single quoted long string."""
    def __init__(self, value: str, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = value
