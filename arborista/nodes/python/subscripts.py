"""Python subscription subscripts."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.subscript import Subscript


class Subscripts(PythonNode):
    """Python subscription subscripts."""
    def __init__(self, first: Subscript, rest: List[Subscript], parent: Optional[Node] = None):
        super().__init__(parent)

        self.first: Subscript = first
        self.rest: List[Subscript] = rest
