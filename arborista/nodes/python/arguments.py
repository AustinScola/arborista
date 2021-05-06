"""Python arguments."""
from typing import Iterable, List, Optional

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.python_node import PythonNode


class Arguments(PythonNode):
    """Python arguments."""
    def __init__(self,
                 arguments: Optional[Iterable[Argument]] = None,
                 parent: Optional[Node] = None) -> None:
        super().__init__(parent)

        self.arguments: List[Argument] = [] if arguments is None else list(arguments)
