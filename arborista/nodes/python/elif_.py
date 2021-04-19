"""An Python elif."""
from typing import Iterable, Optional

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.suite import Suite


class Elif(PythonNode):
    """An Python elif."""
    def __init__(self, condition: Expression, body: Suite, parent: Optional[Node] = None):
        super().__init__(parent)

        self.condition: Expression = condition
        self.body: Suite = body


Elifs = Iterable[Elif]
