"""A Python comparison."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.comparison_operator import ComparisonOperator
from arborista.nodes.python.expression import Expression


class Comparison(Expression):
    """A Python comparison."""
    def __init__(self,
                 left: Expression,
                 comparison_operator: ComparisonOperator,
                 right: Expression,
                 parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.left: Expression = left
        self.comparison_operator: ComparisonOperator = comparison_operator
        self.right: Expression = right
