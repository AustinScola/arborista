"""Python arguments."""
from typing import List, Optional

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.python_node import PythonNode


class Arguments(PythonNode):
    """Python arguments."""
    def __init__(self,
                 first: Argument,
                 rest: List[Argument],
                 parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.first: Argument = first
        self.rest: List[Argument] = rest
