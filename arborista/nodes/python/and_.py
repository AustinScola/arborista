"""A Python and operator."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.boolean_operator import BooleanOperator


class And(BooleanOperator):
    """A Python and operator."""
    def __init__(self, parent: Optional[Node] = None):
        super().__init__(parent)
