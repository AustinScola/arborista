"""A Python newline."""
from typing import Optional

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode


class Newline(PythonNode):
    """A Python newline."""
    def __init__(self, value: Optional[str] = None, parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.value: str = '\n' if value is None else value
