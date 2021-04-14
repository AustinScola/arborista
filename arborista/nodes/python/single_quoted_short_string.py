"""A single quoted short string."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.short_string import ShortString


class SingleQuotedShortString(ShortString):
    """A single quoted short string."""
    def __init__(self, value: str, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = value
