"""An Python else."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.suite import Suite


class Else(PythonNode):
    """An Python else."""
    def __init__(self, body: Suite, parent: Optional[Node] = None):
        super().__init__(parent)

        self.body: Suite = body
