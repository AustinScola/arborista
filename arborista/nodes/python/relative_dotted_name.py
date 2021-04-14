"""A relative dotted name."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.python_node import PythonNode


class RelativeDottedName(PythonNode):
    """A relative dotted name."""
    def __init__(self, dots: int, dotted_name: Optional[DottedName], parent: Optional[Node] = None):
        super().__init__(parent)

        self.dots: int = dots
        self.dotted_name: Optional[DottedName] = dotted_name
