"""A Python index."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.subscript import Subscript


class Index(Subscript):
    """A Python index."""
    def __init__(self, value: Expression, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: Expression = value
