"""A Python expression statement."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.small_statement import SmallStatement


class ExpressionStatement(SmallStatement):
    """A Python expression statement."""
    def __init__(self, expression: Expression, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.expression: Expression = expression
