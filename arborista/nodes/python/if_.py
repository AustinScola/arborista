"""An Python if."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.suite import Suite


class If(PythonNode):
    """An Python if."""
    def __init__(self, condition: Expression, body: Suite, parent: Optional[Node] = None):
        super().__init__(parent)

        self.condition: Expression = condition
        self.body: Suite = body
