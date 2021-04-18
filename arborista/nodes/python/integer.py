"""A Python integer."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.number import Number


class Integer(Number):  # pylint: disable=too-many-ancestors
    """A Python integer."""
    def __init__(self, value: int, parent: Optional[Node] = None):
        super().__init__(parent)
        self.value = value
