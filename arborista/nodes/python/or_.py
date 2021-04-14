"""A Python or operator."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.boolean_operator import BooleanOperator


class Or(BooleanOperator):
    """A Python or operator."""
    def __init__(self, parent: Optional[Node] = None):
        super().__init__(parent)
