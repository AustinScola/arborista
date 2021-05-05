"""A Python return statement."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.flow_statement import FlowStatement


class ReturnStatement(FlowStatement):
    """A Python return statement."""
    def __init__(self, value: Optional[Expression] = None, parent: Optional[Node] = None):
        super().__init__(parent)

        self.value: Optional[Expression] = value
