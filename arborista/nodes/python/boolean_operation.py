"""A Python boolean operation."""
from typing import Any, Optional

from arborista.node import Node, NodeIterator
from arborista.nodes.python.boolean_operator import BooleanOperator
from arborista.nodes.python.expression import Expression


class BooleanOperation(Expression):
    """A Python boolean operation."""
    def __init__(self,
                 left: Expression,
                 operator: BooleanOperator,
                 right: Expression,
                 parent: Optional[Node] = None):
        super().__init__(parent)

        self.left: Expression = left
        self.operator: BooleanOperator = operator
        self.right: Expression = right

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, BooleanOperation):
            return False

        return (self.left == other.left and self.operator == other.operator
                and self.right == other.right)

    def iterate_children(self) -> NodeIterator:
        yield self.left
        yield self.operator
        yield self.right