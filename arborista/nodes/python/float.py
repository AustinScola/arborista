"""A Python float."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.number import Number


class Float(Number):  # pylint: disable=too-many-ancestors
    """A Python float."""
    def __init__(self, value: float, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: float = value
