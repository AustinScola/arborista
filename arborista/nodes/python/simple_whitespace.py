"""A Python simple whitespace."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode


class SimpleWhitespace(PythonNode):
    """A Python simple whitespace."""
    def __init__(self, value: str, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = value
