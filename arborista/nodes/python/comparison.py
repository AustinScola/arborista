"""A Python comparison."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

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

    @equal_type
    def __eq__(self, other: Any) -> bool:
        if self.left != other.left:
            return False

        if self.comparison_operator != other.comparison_operator:
            return False

        if self.right != other.right:
            return False

        return True
