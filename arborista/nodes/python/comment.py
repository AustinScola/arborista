"""A Python comment."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode


class Comment(PythonNode):
    """A Python comment."""
    def __init__(self, value: str, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = value
