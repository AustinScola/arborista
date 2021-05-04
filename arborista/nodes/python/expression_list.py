"""Python expression list."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.python_node import PythonNode


class ExpressionList(PythonNode):
    """Python expression list."""
    def __init__(self, first: Expression, rest: List[Expression], parent: Optional[Node] = None):
        super().__init__(parent)

        self.first: Expression = first
        self.rest: List[Expression] = rest
