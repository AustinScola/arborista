"""A Python expression statement."""
from typing import Any, Optional

from seligimus.python.decorators.operators.equality.equal_type import equal_type

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.small_statement import SmallStatement


class ExpressionStatement(SmallStatement):
    """A Python expression statement."""
    def __init__(self, expression: Expression, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.expression: Expression = expression

    @equal_type
    def __eq__(self, other: Any) -> bool:
        equality: bool = self.expression == other.expression
        return equality
