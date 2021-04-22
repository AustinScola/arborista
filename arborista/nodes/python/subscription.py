"""A Python subsctiption."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.subscripts import Subscripts


class Subscription(Expression):
    """A Python subsctiption."""
    def __init__(self, value: Expression, subscripts: Subscripts, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: Expression = value
        self.subscripts: Subscripts = subscripts
